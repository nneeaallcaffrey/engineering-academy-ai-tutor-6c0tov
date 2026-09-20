"""Kurikulum butunligi — 150 mavzuning tuzilishi va sifati.

Bu testlar backend API orqali ishlaydi, ya'ni ular kurikulum Python
modullarini emas, foydalanuvchiga YETIB BORADIGAN ma'lumotni tekshiradi.
"""

from __future__ import annotations

import re

import pytest

from app.sandbox.executor import run_code
from app.sandbox.policy import check

SUBJECT_ORDER = ["nazariy-mexanika", "materiallar-qarshiligi", "tutash-muhitlar",
                 "plastinalar-qobiqlar", "sonli-usullar"]
PREFIX = {"nazariy-mexanika": "nm-", "materiallar-qarshiligi": "mq-",
          "tutash-muhitlar": "tmm-", "plastinalar-qobiqlar": "pq-",
          "sonli-usullar": "su-"}


@pytest.fixture(scope="module")
def topics(client) -> list[dict]:
    return client.get("/api/topics?limit=300").json()


@pytest.fixture(scope="module")
def details(client, topics) -> list[dict]:
    return [client.get(f"/api/topics/{t['id']}").json() for t in topics]


def test_exactly_five_subjects_thirty_each(client) -> None:
    rows = client.get("/api/subjects").json()
    assert [s["id"] for s in rows] == SUBJECT_ORDER
    assert all(s["topic_count"] == 30 for s in rows)


def test_exactly_150_topics_no_duplicates(topics) -> None:
    assert len(topics) == 150
    ids = [t["id"] for t in topics]
    assert len(set(ids)) == 150
    titles = [t["title"].strip().lower() for t in topics]
    assert len(set(titles)) == 150, "takrorlangan sarlavha bor"


def test_topic_ids_follow_subject_prefix(topics) -> None:
    for t in topics:
        assert t["id"].startswith(PREFIX[t["subject_id"]]), t["id"]


def test_topics_numbered_1_to_30(topics) -> None:
    for sid, pref in PREFIX.items():
        orders = sorted(t["order"] for t in topics if t["subject_id"] == sid)
        assert orders == list(range(1, 31)), sid


def test_prerequisites_exist_and_come_earlier(topics) -> None:
    order = {t["id"]: t["global_order"] for t in topics}
    for t in topics:
        for dep in t["prerequisites"]:
            assert dep in order, f"{t['id']}: '{dep}' mavjud emas"
            assert order[dep] < order[t["global_order"] and t["id"]], \
                f"{t['id']} o'zidan keyingi '{dep}' ga tayanadi"


def test_next_topic_chain_is_consistent(topics) -> None:
    ids = {t["id"] for t in topics}
    by_id = {t["id"]: t for t in topics}
    for t in topics:
        nxt = t["next_topic"]
        if nxt is None:
            continue
        assert nxt in ids, f"{t['id']} -> '{nxt}' mavjud emas"
        assert by_id[nxt]["global_order"] > t["global_order"], \
            f"{t['id']} -> {nxt} orqaga qaragan"


def test_every_topic_has_18_section_lesson(details) -> None:
    required = ("physical_problem", "concepts", "derivation", "formula_meaning",
                "equations", "conditions", "worked_example", "computation",
                "visualization", "interpretation", "common_mistakes", "quiz",
                "bridge_to_next", "research_extension")
    for d in details:
        for key in required:
            assert d["lesson"].get(key), f"{d['id']}: '{key}' bo'sh"
        for key in ("learning_objective", "mathematical_core",
                    "engineering_application"):
            assert d.get(key) or d["lesson"].get(key), f"{d['id']}: '{key}' bo'sh"


def test_derivations_have_at_least_three_steps(details) -> None:
    for d in details:
        steps = d["lesson"]["derivation"]
        assert len(steps) >= 3, f"{d['id']}: {len(steps)} qadam"
        for s in steps:
            assert s["title"] and s["latex"] and s["explanation"], d["id"]


def test_quiz_between_5_and_10(details) -> None:
    for d in details:
        quiz = d["lesson"]["quiz"]
        assert 5 <= len(quiz) <= 10, f"{d['id']}: {len(quiz)} savol"
        for q in quiz:
            assert q["question"] and q["answer"], d["id"]
            if q.get("options"):
                assert 0 <= q["correct_index"] < len(q["options"]), d["id"]


def test_worked_examples_are_complete(details) -> None:
    for d in details:
        w = d["lesson"]["worked_example"]
        assert w["statement"] and w["given"] and w["steps"] and w["answer"], d["id"]
        for s in w["steps"]:
            assert s["latex"] and s["text"], d["id"]


def test_every_topic_has_runnable_lab(details) -> None:
    for d in details:
        comp = d["lesson"]["computation"]
        assert comp["code"].strip(), f"{d['id']}: kod yo'q"
        assert comp["caption"], d["id"]
        assert "labkit" in comp["code"], f"{d['id']}: labkit ishlatilmagan"


def test_lab_parameters_are_sane(details) -> None:
    for d in details:
        for p in d["lesson"]["computation"].get("parameters", []):
            assert p["minimum"] <= p["default"] <= p["maximum"], f"{d['id']}/{p['key']}"
            assert p["step"] > 0
            assert p["label"], f"{d['id']}/{p['key']}"


def test_all_lab_code_passes_policy(details) -> None:
    """Platformaning O'Z kodi o'z xavfsizlik siyosatidan o'tishi shart."""
    bad = [(d["id"], check(d["lesson"]["computation"]["code"]).reason)
           for d in details if not check(d["lesson"]["computation"]["code"]).ok]
    assert not bad, f"siyosatdan o'tmadi: {bad}"


def test_visualization_is_specified(details) -> None:
    tools = {"React/SVG", "Canvas", "Matplotlib", "Manim",
             "React/SVG + Matplotlib", "React/SVG + Manim"}
    for d in details:
        v = d["lesson"]["visualization"]
        assert v["kind"] and v["description"] and v["how_to_draw"], d["id"]
        assert v["tool"] in tools, f"{d['id']}: '{v['tool']}'"


def test_no_placeholder_text(details) -> None:
    """40-talab: TODO, 'keyinroq', bo'sh joy to'ldiruvchi matn bo'lmasin.

    Belgilar SO'Z CHEGARASI bilan qidiriladi: oddiy substring qidiruvi
    "meTODOlogik" so'zini va "w_xxxx" (to'rtinchi hosila) yozuvini
    noto'g'ri belgilaydi.
    """
    marks = re.compile(r"\b(TODO|FIXME|XXX|HACK)\b")
    phrases = ("keyinchalik amalga", "to be implemented", "hozircha bo'sh",
               "lorem ipsum", "coming soon", "not implemented")
    for d in details:
        blob = str(d)
        found = marks.search(blob)
        assert found is None, f"{d['id']}: '{found.group()}' topildi"
        low = blob.lower()
        for p in phrases:
            assert p not in low, f"{d['id']}: '{p}' topildi"


def test_cross_subject_links_exist(topics) -> None:
    """Fanlar zanjiri: keyingi fan oldingisiga tayanishi kerak."""
    cross = 0
    for t in topics:
        pref = PREFIX[t["subject_id"]]
        cross += sum(1 for dep in t["prerequisites"] if not dep.startswith(pref))
    assert cross >= 20, f"fanlararo havolalar juda kam: {cross}"


@pytest.mark.parametrize("topic_id", ["nm-01", "mq-13", "tmm-21", "pq-13",
                                      "su-15", "su-29", "su-30"])
def test_representative_labs_execute(client, topic_id: str) -> None:
    """Har bir fandan namunaviy laboratoriya haqiqatan ishlaydi."""
    d = client.post(f"/api/topics/{topic_id}/run", json={"params": {}}).json()
    assert d["ok"] is True, f"{topic_id}: {d['error']}"
    assert d["values"] or d["series"] or d["tables"], f"{topic_id}: natija bo'sh"


@pytest.mark.slow
def test_every_single_lab_executes(details) -> None:
    """BARCHA 150 laboratoriya sandbox'da xatosiz bajariladi (sekin test)."""
    failures = []
    for d in details:
        comp = d["lesson"]["computation"]
        params = {p["key"]: p["default"] for p in comp.get("parameters", [])}
        r = run_code(comp["code"], params)
        if not r.ok:
            failures.append((d["id"], r.error_type, r.error[:100]))
    assert not failures, f"{len(failures)} ta laboratoriya yiqildi: {failures[:5]}"
