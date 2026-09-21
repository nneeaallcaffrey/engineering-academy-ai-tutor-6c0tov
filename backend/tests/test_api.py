"""API testlari."""

from __future__ import annotations

import pytest

EXPECTED_SUBJECTS = 5
EXPECTED_TOPICS = 150


def test_health(client) -> None:
    r = client.get("/health")
    assert r.status_code == 200
    d = r.json()
    assert d["status"] == "ok"
    assert d["database"] == "ok"
    assert d["seeded"] is True
    assert d["counts"]["topics"] == EXPECTED_TOPICS


def test_health_sandbox(client) -> None:
    d = client.get("/health/sandbox").json()
    assert d["ok"] is True
    assert d["values"][0]["value"] == 1.0


def test_subjects_are_in_pedagogical_order(client) -> None:
    rows = client.get("/api/subjects").json()
    assert len(rows) == EXPECTED_SUBJECTS
    assert [s["order"] for s in rows] == [1, 2, 3, 4, 5]
    assert [s["code"] for s in rows] == ["NM", "MQ", "TMM", "PQ", "SU"]
    assert all(s["topic_count"] == 30 for s in rows)


def test_subject_detail(client) -> None:
    d = client.get("/api/subjects/sonli-usullar").json()
    assert len(d["topics"]) == 30
    assert len(d["modules"]) == 5
    assert d["topics"][0]["id"] == "su-01"
    assert d["topics"][-1]["id"] == "su-30"


def test_subject_404(client) -> None:
    assert client.get("/api/subjects/yoq").status_code == 404


def test_topics_listing_and_paging(client) -> None:
    rows = client.get("/api/topics?limit=300").json()
    assert len(rows) == EXPECTED_TOPICS
    assert rows[0]["id"] == "nm-01"
    assert rows[-1]["id"] == "su-30"
    page = client.get("/api/topics?limit=10&offset=10").json()
    assert [t["id"] for t in page] == [t["id"] for t in rows[10:20]]


def test_topic_search(client) -> None:
    rows = client.get("/api/topics?q=plastina").json()
    assert rows, "qidiruv natija bermadi"
    assert all("plastina" in (t["title"] + t["description"]).lower()
               for t in rows)


def test_topic_detail_has_all_lesson_sections(client) -> None:
    d = client.get("/api/topics/su-30").json()
    lesson = d["lesson"]
    for key in ("physical_problem", "concepts", "derivation", "formula_meaning",
                "equations", "conditions", "worked_example", "computation",
                "visualization", "interpretation", "common_mistakes", "quiz",
                "bridge_to_next", "research_extension"):
        assert lesson.get(key), f"'{key}' bo'limi bo'sh"
    assert d["prev_topic"] == "su-29"
    assert d["next_topic"] is None          # oxirgi mavzu


def test_topic_404(client) -> None:
    assert client.get("/api/topics/yoq-99").status_code == 404


def test_lab_parameters(client) -> None:
    rows = client.get("/api/topics/su-30/lab").json()
    assert rows
    for p in rows:
        assert p["minimum"] <= p["default"] <= p["maximum"]
        assert p["step"] > 0


def test_run_with_default_params(client) -> None:
    d = client.post("/api/topics/su-30/run", json={"params": {}}).json()
    assert d["ok"] is True, d["error"]
    labels = {v["label"]: v["value"] for v in d["values"]}
    assert labels["w_max aniq"] == pytest.approx(91.8353, rel=1e-4)
    assert labels["Muvozanat nazorati"] == pytest.approx(0.0, abs=1e-9)


def test_run_reacts_to_parameters(client) -> None:
    """a^4 qonuni HTTP orqali tekshiriladi."""
    def w(a: float) -> float:
        d = client.post("/api/topics/su-30/run",
                        json={"params": {"a": a, "h": 1.2, "p": 0.5}}).json()
        assert d["ok"], d["error"]
        return next(v["value"] for v in d["values"] if v["label"] == "w_max aniq")

    assert w(40.0) / w(25.0) == pytest.approx((40.0 / 25.0) ** 4, rel=1e-6)


def test_run_rejects_malicious_code(client) -> None:
    d = client.post("/api/topics/su-30/run",
                    json={"code": "import os\nos.system('id')"}).json()
    assert d["ok"] is False
    assert d["error_type"] == "PolicyError"


def test_run_ignores_unknown_parameters(client) -> None:
    d = client.post("/api/topics/su-30/run",
                    json={"params": {"__evil__": 1.0}}).json()
    assert d["ok"] is True


def test_run_on_missing_topic(client) -> None:
    assert client.post("/api/topics/yoq-99/run", json={}).status_code == 404


def test_projects(client) -> None:
    rows = client.get("/api/projects").json()
    assert len(rows) == EXPECTED_SUBJECTS
    for p in rows:
        assert p["stages"] and p["deliverables"] and p["evaluation"]
        assert p["starter_code"].strip()
    one = client.get("/api/projects/proj-su").json()
    assert one["subject_id"] == "sonli-usullar"
    assert client.get("/api/projects/yoq").status_code == 404


def test_resources(client) -> None:
    rows = client.get("/api/resources").json()
    assert rows
    per = client.get("/api/resources?subject_id=nazariy-mexanika").json()
    assert per and all(r["subject_id"] == "nazariy-mexanika" for r in per)


def test_curriculum_graph(client) -> None:
    g = client.get("/api/curriculum/graph").json()
    assert len(g["nodes"]) == EXPECTED_TOPICS
    ids = {n["id"] for n in g["nodes"]}
    assert g["edges"]
    for e in g["edges"]:
        assert e["source"] in ids and e["target"] in ids


def test_graph_filtered_keeps_external_sources(client) -> None:
    """Fan bo'yicha filtrlaganda fanlararo bog'lanish yo'qolmasligi kerak."""
    g = client.get("/api/curriculum/graph?subject_id=sonli-usullar").json()
    ids = {n["id"] for n in g["nodes"]}
    assert any(not n["id"].startswith("su-") for n in g["nodes"]), \
        "fanlararo prerequisite tugunlari tushib qolgan"
    for e in g["edges"]:
        assert e["source"] in ids and e["target"] in ids


def test_curriculum_audit_passes(client) -> None:
    d = client.get("/api/curriculum/audit").json()
    failed = [c["question"] for c in d["checks"] if not c["passed"]]
    assert d["passed"] is True, f"audit yiqildi: {failed}"
    assert d["counts"]["topics"] == EXPECTED_TOPICS


def test_every_topic_serves_at_least_two_figures(client) -> None:
    """Chizmalar kontentdan bazaga, bazadan API'ga uzilmasdan yetib borishi kerak."""
    ids = [t["id"] for t in client.get("/api/topics?limit=200").json()]
    assert len(ids) == EXPECTED_TOPICS
    total = 0
    for tid in ids:
        figures = client.get(f"/api/topics/{tid}").json()["lesson"]["figures"]
        assert len(figures) >= 2, f"{tid}: {len(figures)} ta chizma"
        for f in figures:
            assert f["params"] and f["curves"] and f["readouts"], f"{tid}: chizma to'liq emas"
            for p in f["params"]:
                assert p["minimum"] <= p["default"] <= p["maximum"], f"{tid}/{p['key']}"
        total += len(figures)
    assert total >= 2 * EXPECTED_TOPICS


def test_openapi_is_valid(client) -> None:
    d = client.get("/openapi.json").json()
    assert d["info"]["title"]
    for path in ("/health", "/api/subjects", "/api/topics",
                 "/api/topics/{topic_id}/run", "/api/projects",
                 "/api/resources", "/api/curriculum/graph",
                 "/api/curriculum/audit"):
        assert path in d["paths"], f"{path} OpenAPI'da yo'q"


def test_internal_errors_do_not_leak(client) -> None:
    r = client.get("/api/topics/su-30")
    assert "Traceback" not in r.text
