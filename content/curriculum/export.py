"""Kurrikulumni JSON seed fayliga eksport qilish.

Ishlatish:
    python -m content.curriculum.export            # content/generated/curriculum.json
    python -m content.curriculum.export --out X    # boshqa joyga

Backend faqat shu JSON bilan ishlaydi — kontent qatlami backend'dan mustaqil.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict
from datetime import date
from pathlib import Path
from typing import Any

from content.curriculum.audit import run_audit
from content.curriculum.projects import PROJECTS
from content.curriculum.registry import SUBJECTS, all_topics, dependency_edges, global_order
from content.curriculum.schema import NOTATION, SIGN_CONVENTION

DEFAULT_OUT = Path(__file__).resolve().parents[1] / "generated" / "curriculum.json"

SCHEMA_VERSION = "1.0"


def build_payload() -> dict[str, Any]:
    order = global_order()
    topics = all_topics()

    subjects_payload = []
    for subject in SUBJECTS:
        data = asdict(subject)
        # Mavzular alohida ro'yxatda saqlanadi — fan obyektida faqat id'lar qoladi.
        data["topic_ids"] = [t.id for t in subject.topics]
        data.pop("topics")
        data["topic_count"] = len(subject.topics)
        subjects_payload.append(data)

    topics_payload = []
    for topic in topics:
        data = asdict(topic)
        data["global_order"] = order[topic.id]
        data["has_lab"] = bool(topic.lesson.computation.parameters)
        data["has_manim"] = topic.lesson.manim is not None
        topics_payload.append(data)

    audit = run_audit()

    return {
        "schema_version": SCHEMA_VERSION,
        "generated_at": date.today().isoformat(),
        "language": "uz-Latn",
        "meta": {
            "title": "Mexanika ta'lim platformasi",
            "subtitle": "Nazariy mexanikadan hisoblash mexanikasigacha — 5 fan, 150 mavzu",
            "notation": NOTATION,
            "sign_convention": SIGN_CONVENTION,
            "counts": {
                "subjects": len(SUBJECTS),
                "modules": sum(len(s.modules) for s in SUBJECTS),
                "topics": len(topics),
                "projects": len(PROJECTS),
                "labs": sum(1 for t in topics if t.lesson.computation.parameters),
                "manim_scenes": len({t.lesson.manim.scene for t in topics if t.lesson.manim}),
                "quiz_items": sum(len(t.lesson.quiz) for t in topics),
                "derivation_steps": sum(len(t.lesson.derivation) for t in topics),
            },
        },
        "subjects": subjects_payload,
        "topics": topics_payload,
        "projects": [asdict(p) for p in PROJECTS],
        "graph": {
            "nodes": [
                {
                    "id": t.id,
                    "title": t.title,
                    "subject_id": t.subject_id,
                    "module_id": t.module_id,
                    "order": t.order,
                    "global_order": order[t.id],
                    "difficulty": t.difficulty,
                }
                for t in topics
            ],
            "edges": [{"from": a, "to": b} for a, b in dependency_edges()],
        },
        "audit": audit.to_dict(),
    }


def write(out_path: Path | None = None) -> Path:
    path = Path(out_path) if out_path else DEFAULT_OUT
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = build_payload()
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=1), encoding="utf-8")
    return path


def main() -> int:
    parser = argparse.ArgumentParser(description="Kurrikulumni JSON ga eksport qilish")
    parser.add_argument("--out", type=Path, default=None, help="Chiqish fayli yo'li")
    args = parser.parse_args()

    path = write(args.out)
    payload = json.loads(path.read_text(encoding="utf-8"))
    counts = payload["meta"]["counts"]
    audit_ok = payload["audit"]["passed"]

    size_kb = path.stat().st_size / 1024
    print(f"Yozildi: {path}  ({size_kb:.1f} KB)")
    print(f"  fanlar: {counts['subjects']}, modullar: {counts['modules']}, "
          f"mavzular: {counts['topics']}")
    print(f"  laboratoriyalar: {counts['labs']}, Manim sahnalari: {counts['manim_scenes']}, "
          f"savollar: {counts['quiz_items']}")
    print(f"  audit: {'PASS' if audit_ok else 'FAIL'}")
    return 0 if audit_ok else 1


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
