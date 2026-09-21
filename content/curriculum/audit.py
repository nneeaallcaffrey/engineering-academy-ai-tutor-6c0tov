"""Avtomatik akademik audit (28- va 36-talablar).

15 ta tekshiruv bajariladi va natija tuzilgan hisobot sifatida qaytariladi.
`python -m content.curriculum.audit` — konsolda hisobotni chiqaradi.
"""

from __future__ import annotations

import sys
from dataclasses import dataclass, field

from content.curriculum.projects import PROJECTS
from content.curriculum.registry import (
    SUBJECTS,
    all_topics,
    global_order,
    module_index,
    topic_index,
)

EXPECTED_SUBJECTS = 5
EXPECTED_TOPICS_PER_SUBJECT = 30
EXPECTED_TOTAL_TOPICS = 150

#: Har bir fanda bo'lishi shart bo'lgan fundamental tayanch tushunchalar.
REQUIRED_KEYWORDS: dict[str, list[str]] = {
    "nazariy-mexanika": ["kinematika", "nyuton", "energiya", "lagranj", "tebranish"],
    "materiallar-qarshiligi": ["kuchlanish", "deformatsiya", "egilish", "buralish", "ustuvorlik"],
    "tutash-muhitlar": ["tenzor", "balans", "elastik", "plastik", "suyuqlik"],
    "plastinalar-qobiqlar": ["plastina", "qobiq", "egilish", "tebranish", "ustuvorlik"],
    "sonli-usullar": ["xatolik", "chekli ayirma", "fem", "dqm", "xususiy qiymat"],
}


@dataclass
class CheckResult:
    key: str
    title: str
    passed: bool
    detail: str
    problems: list[str] = field(default_factory=list)


@dataclass
class AuditReport:
    checks: list[CheckResult]

    @property
    def passed(self) -> bool:
        return all(c.passed for c in self.checks)

    @property
    def summary(self) -> dict[str, int]:
        return {
            "subjects": len(SUBJECTS),
            "topics": len(all_topics()),
            "modules": len(module_index()),
            "projects": len(PROJECTS),
            "checks_total": len(self.checks),
            "checks_passed": sum(1 for c in self.checks if c.passed),
        }

    def to_dict(self) -> dict:
        return {
            "passed": self.passed,
            "summary": self.summary,
            "checks": [
                {
                    "key": c.key,
                    "title": c.title,
                    "passed": c.passed,
                    "detail": c.detail,
                    "problems": c.problems,
                }
                for c in self.checks
            ],
        }


def _haystack(topic) -> str:
    """Mavzuning matnli tarkibi — kalit so'z qidiruvi uchun."""
    lesson = topic.lesson
    parts = [
        topic.title, topic.description, topic.learning_objective,
        topic.mathematical_core, topic.engineering_application,
        topic.computational_component, topic.visualization_component,
        " ".join(topic.tags), lesson.physical_problem, lesson.formula_meaning,
        " ".join(c.term for c in lesson.concepts),
        " ".join(d.title for d in lesson.derivation),
    ]
    return " ".join(parts).casefold()


def run_audit() -> AuditReport:  # noqa: C901 - tekshiruvlar ro'yxati uzun bo'lishi tabiiy
    topics = all_topics()
    order = global_order()
    index = topic_index()
    checks: list[CheckResult] = []

    # 1. Fanlar soni
    checks.append(CheckResult(
        "subject_count", "Aynan 5 ta fan bormi?",
        len(SUBJECTS) == EXPECTED_SUBJECTS,
        f"{len(SUBJECTS)}/{EXPECTED_SUBJECTS}",
    ))

    # 2. Har bir fanda 30 ta mavzu
    bad = [f"{s.id}: {len(s.topics)}" for s in SUBJECTS
           if len(s.topics) != EXPECTED_TOPICS_PER_SUBJECT]
    checks.append(CheckResult(
        "topics_per_subject", "Har bir fanda aynan 30 ta mavzumi?",
        not bad,
        "barcha fanlar 30 tadan" if not bad else "; ".join(bad), bad,
    ))

    # 3. Jami 150 ta mavzu
    checks.append(CheckResult(
        "total_topics", "Jami aynan 150 ta mavzumi?",
        len(topics) == EXPECTED_TOTAL_TOPICS,
        f"{len(topics)}/{EXPECTED_TOTAL_TOPICS}",
    ))

    # 4. Duplicate id va sarlavhalar
    ids = [t.id for t in topics]
    titles = [t.title.casefold().strip() for t in topics]
    dup_ids = sorted({i for i in ids if ids.count(i) > 1})
    dup_titles = sorted({t for t in titles if titles.count(t) > 1})
    checks.append(CheckResult(
        "duplicates", "Duplicate mavzular bormi?",
        not dup_ids and not dup_titles,
        "duplicate topilmadi" if not dup_ids and not dup_titles
        else f"id: {dup_ids}, sarlavha: {dup_titles}",
        [*dup_ids, *dup_titles],
    ))

    # 5. Fundamental mavzular yetishmayaptimi?
    missing_kw: list[str] = []
    for subject in SUBJECTS:
        blob = " ".join(_haystack(t) for t in subject.topics)
        for kw in REQUIRED_KEYWORDS.get(subject.id, []):
            if kw.casefold() not in blob:
                missing_kw.append(f"{subject.id}: '{kw}'")
    checks.append(CheckResult(
        "fundamentals", "Fundamental mavzular qamrab olinganmi?",
        not missing_kw,
        "barcha tayanch tushunchalar mavjud" if not missing_kw else "; ".join(missing_kw),
        missing_kw,
    ))

    # 6. Prerequisite mavjudligi
    unknown = [f"{t.id} -> {pre}" for t in topics for pre in t.prerequisites if pre not in index]
    checks.append(CheckResult(
        "prereq_exists", "Barcha prerequisite'lar mavjudmi?",
        not unknown,
        "barcha havolalar to'g'ri" if not unknown else "; ".join(unknown), unknown,
    ))

    # 7. Prerequisite tartibi (A mavzu B dan oldin kelishi shart)
    violations = [
        f"{t.id} (#{order[t.id]}) <- {pre} (#{order[pre]})"
        for t in topics for pre in t.prerequisites
        if pre in order and order[pre] >= order[t.id]
    ]
    checks.append(CheckResult(
        "prereq_order", "Prerequisite tartibi buzilmaganmi?",
        not violations,
        "tartib to'g'ri" if not violations else "; ".join(violations), violations,
    ))

    # 8. Fanlar orasida keraksiz takrorlanish
    overlaps: list[str] = []
    for i, s1 in enumerate(SUBJECTS):
        for s2 in SUBJECTS[i + 1:]:
            t1 = {t.title.casefold() for t in s1.topics}
            t2 = {t.title.casefold() for t in s2.topics}
            common = t1 & t2
            if common:
                overlaps.append(f"{s1.id} ↔ {s2.id}: {sorted(common)}")
    checks.append(CheckResult(
        "cross_overlap", "Fanlar orasida takrorlanish bormi?",
        not overlaps,
        "takrorlanish yo'q" if not overlaps else "; ".join(overlaps), overlaps,
    ))

    # 9. Difficulty jump
    rank = {"kirish": 0, "asosiy": 1, "murakkab": 2, "ilg'or": 3}
    jumps: list[str] = []
    for subject in SUBJECTS:
        for prev, cur in zip(subject.topics, subject.topics[1:]):
            if rank[cur.difficulty] - rank[prev.difficulty] > 1:
                jumps.append(f"{prev.id}({prev.difficulty}) -> {cur.id}({cur.difficulty})")
    checks.append(CheckResult(
        "difficulty_jump", "Murakkablik keskin sakramaganmi?",
        not jumps,
        "murakkablik bosqichma-bosqich o'sadi" if not jumps else "; ".join(jumps), jumps,
    ))

    # 10. Nazariya → amaliyot progressiyasi (har mavzuda masala va kod bor)
    no_practice = [t.id for t in topics
                   if not t.lesson.worked_example.steps or not t.lesson.computation.code.strip()]
    checks.append(CheckResult(
        "theory_practice", "Har bir mavzuda yechilgan masala va hisob bormi?",
        not no_practice,
        "barcha mavzuda masala + Python bor" if not no_practice else "; ".join(no_practice),
        no_practice,
    ))

    # 11. Matematik tayyorgarlik
    no_math = [t.id for t in topics
               if not t.mathematical_core.strip() or len(t.lesson.derivation) < 3]
    checks.append(CheckResult(
        "math_depth", "Matematik tayanch va derivatsiya yetarlimi (≥3 qadam)?",
        not no_math,
        "barcha mavzuda ≥3 qadamli derivatsiya" if not no_math else "; ".join(no_math),
        no_math,
    ))

    # 12. Sonli usullar oldingi mexanika bilimlariga tayanadimi?
    numerics = next((s for s in SUBJECTS if s.id == "sonli-usullar"), None)
    cross_refs = 0
    if numerics:
        cross_refs = sum(
            1 for t in numerics.topics for pre in t.prerequisites
            if not pre.startswith("su-")
        )
    checks.append(CheckResult(
        "numerics_grounded", "Sonli usullar mexanika bilimlariga tayanadimi?",
        cross_refs >= 10,
        f"{cross_refs} ta fanlararo prerequisite havola (kamida 10 kerak)",
    ))

    # 13. Plastina/qobiq uchun kontinuum asoslari
    plates = next((s for s in SUBJECTS if s.id == "plastinalar-qobiqlar"), None)
    continuum_refs = 0
    if plates:
        continuum_refs = sum(
            1 for t in plates.topics for pre in t.prerequisites
            if pre.startswith(("tmm-", "mq-"))
        )
    checks.append(CheckResult(
        "plates_grounded", "Plastina/qobiq nazariyasi kontinuum asosiga tayanadimi?",
        continuum_refs >= 8,
        f"{continuum_refs} ta tmm-/mq- prerequisite havola (kamida 8 kerak)",
    ))

    # 14. Research progression uzluksizmi?
    no_research = [t.id for t in topics
                   if len(t.research_extension.strip()) < 40
                   or len(t.lesson.research_extension.strip()) < 40]
    checks.append(CheckResult(
        "research_chain", "Research extension barcha mavzularda bormi?",
        not no_research,
        "150/150 mavzuda research extension mavjud" if not no_research
        else "; ".join(no_research), no_research,
    ))

    # 15. Python va vizualizatsiya mavzuga mos joylashtirilganmi?
    bad_vis = [t.id for t in topics
               if not t.lesson.visualization.how_to_draw.strip()
               or not t.lesson.visualization.tool]
    checks.append(CheckResult(
        "viz_placement", "Vizualizatsiya vositasi va usuli ko'rsatilganmi?",
        not bad_vis,
        "barcha mavzuda vizualizatsiya spetsifikatsiyasi bor" if not bad_vis
        else "; ".join(bad_vis), bad_vis,
    ))

    # Qo'shimcha: next_topic zanjiri va loyihalar
    broken_links = [f"{t.id} -> {t.next_topic}" for t in topics
                    if t.next_topic and t.next_topic not in index]
    checks.append(CheckResult(
        "topic_links", "next_topic havolalari to'g'rimi?",
        not broken_links,
        "barcha havolalar to'g'ri" if not broken_links else "; ".join(broken_links),
        broken_links,
    ))

    project_subjects = {p.subject_id for p in PROJECTS}
    missing_projects = [s.id for s in SUBJECTS if s.id not in project_subjects]
    checks.append(CheckResult(
        "projects", "Har bir fan uchun final project bormi?",
        not missing_projects and len(PROJECTS) == EXPECTED_SUBJECTS,
        f"{len(PROJECTS)}/{EXPECTED_SUBJECTS} loyiha",
        missing_projects,
    ))

    # Lab parametrlari va quiz soni
    bad_quiz = [t.id for t in topics if not 5 <= len(t.lesson.quiz) <= 10]
    checks.append(CheckResult(
        "quiz_count", "Har bir mavzuda 5–10 ta mustahkamlash savoli bormi?",
        not bad_quiz,
        "barcha mavzuda 5–10 savol" if not bad_quiz else "; ".join(bad_quiz), bad_quiz,
    ))

    # Interaktiv chizmalar: har bir mavzuda kamida ikkitadan
    few_fig = [f"{t.id}({len(t.lesson.figures)})" for t in topics
               if len(t.lesson.figures) < 2]
    checks.append(CheckResult(
        "figures_min", "Har bir mavzuda kamida 2 ta interaktiv chizma bormi?",
        not few_fig,
        (f"barcha {len(topics)} mavzuda \u2265 2 chizma "
         f"(jami {sum(len(t.lesson.figures) for t in topics)} ta)")
        if not few_fig else "; ".join(few_fig), [x.split("(")[0] for x in few_fig],
    ))

    # Chizma spetsifikatsiyasining to'liqligi
    bad_fig = []
    for t in topics:
        for i, f in enumerate(t.lesson.figures):
            where = f"{t.id}#{i + 1}"
            if not f.params:
                bad_fig.append(f"{where}: surgich yo'q")
            elif not f.curves:
                bad_fig.append(f"{where}: egri chiziq yo'q")
            elif not f.readouts:
                bad_fig.append(f"{where}: ko'rsatkich yo'q")
            elif len(f.note) < 30:
                bad_fig.append(f"{where}: izoh juda qisqa")
    checks.append(CheckResult(
        "figures_complete", "Har bir chizmada surgich, egri chiziq, ko'rsatkich va izoh bormi?",
        not bad_fig,
        "barcha chizma to'liq" if not bad_fig else "; ".join(bad_fig[:8]), bad_fig[:20],
    ))

    return AuditReport(checks=checks)


def main() -> int:
    report = run_audit()
    print("=" * 72)
    print("AKADEMIK AUDIT HISOBOTI")
    print("=" * 72)
    for key, value in report.summary.items():
        print(f"  {key:<16}: {value}")
    print("-" * 72)
    for check in report.checks:
        mark = "PASS" if check.passed else "FAIL"
        print(f"[{mark}] {check.title}")
        print(f"       {check.detail}")
    print("=" * 72)
    print("NATIJA:", "PASS" if report.passed else "FAIL")
    return 0 if report.passed else 1


if __name__ == "__main__":  # pragma: no cover
    sys.exit(main())
