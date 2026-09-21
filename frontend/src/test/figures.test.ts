import { readFileSync } from "node:fs";
import { resolve } from "node:path";
import { describe, expect, it } from "vitest";
import { compile, evalRPN } from "../interactive/expr";
import type { FigureSpec } from "../api/types";

const JSON_PATH = resolve(__dirname, "../../../content/generated/curriculum.json");

interface TopicLite { id: string; lesson: { figures?: FigureSpec[] } }

const data = JSON.parse(readFileSync(JSON_PATH, "utf-8")) as { topics: TopicLite[] };
const withFigs = data.topics.filter((t) => (t.lesson.figures ?? []).length > 0);

function vars(f: FigureSpec, x = 1): Record<string, number> {
  const v: Record<string, number> = { x };
  for (const p of f.params) v[p.key] = p.default;
  return v;
}

describe("chizma spetsifikatsiyalari", () => {
  it("kurikulumda chizmalar bor", () => {
    expect(withFigs.length).toBeGreaterThan(0);
  });

  it("har bir chizmada sarlavha, izoh va kamida bitta egri yoki qiymat bor", () => {
    const bad: string[] = [];
    for (const t of withFigs) {
      for (const f of t.lesson.figures!) {
        if (!f.title || !f.caption) bad.push(`${t.id}: sarlavha/izoh bo'sh`);
        if (f.curves.length === 0 && f.readouts.length === 0) {
          bad.push(`${t.id}/${f.title}: na egri, na qiymat`);
        }
      }
    }
    expect(bad).toEqual([]);
  });

  it("barcha ifodalar kompilyatsiya bo'ladi", () => {
    const bad: string[] = [];
    for (const t of withFigs) {
      for (const f of t.lesson.figures!) {
        const all = [
          ...f.curves.map((c) => [`egri '${c.label}'`, c.expr] as const),
          ...f.curves.filter((c) => c.when).map((c) => [`when '${c.label}'`, c.when] as const),
          ...f.readouts.map((r) => [`qiymat '${r.label}'`, r.expr] as const),
          ["x_min", f.x_min] as const, ["x_max", f.x_max] as const,
        ];
        for (const [what, src] of all) {
          try { compile(src); } catch (e) {
            bad.push(`${t.id}/${f.title} ${what}: ${(e as Error).message}  <<${src}>>`);
          }
        }
      }
    }
    expect(bad).toEqual([]);
  });

  it("standart parametrlarda barcha ifodalar CHEKLI son beradi", () => {
    const bad: string[] = [];
    for (const t of withFigs) {
      for (const f of t.lesson.figures!) {
        const v = vars(f);
        const lo = evalRPN(compile(f.x_min), v);
        const hi = evalRPN(compile(f.x_max), v);
        if (!Number.isFinite(lo) || !Number.isFinite(hi) || hi <= lo) {
          bad.push(`${t.id}/${f.title}: x oralig'i noto'g'ri (${lo} … ${hi})`);
          continue;
        }
        for (const r of f.readouts) {
          const val = evalRPN(compile(r.expr), v);
          if (!Number.isFinite(val)) {
            bad.push(`${t.id}/${f.title} qiymat '${r.label}' = ${val}  <<${r.expr}>>`);
          }
        }
        for (const c of f.curves) {
          let ok = 0;
          for (let i = 0; i <= 40; i += 1) {
            const x = lo + ((hi - lo) * i) / 40;
            const y = evalRPN(compile(c.expr), { ...v, x });
            if (Number.isFinite(y)) ok += 1;
          }
          if (ok < 20) {
            bad.push(`${t.id}/${f.title} egri '${c.label}': 41 nuqtadan faqat ${ok} tasi chekli`);
          }
        }
      }
    }
    expect(bad).toEqual([]);
  });

  it("surgichlar mantiqiy", () => {
    const bad: string[] = [];
    for (const t of withFigs) {
      for (const f of t.lesson.figures!) {
        for (const p of f.params) {
          if (!(p.minimum <= p.default && p.default <= p.maximum)) {
            bad.push(`${t.id}/${f.title}/${p.key}: default oraliqdan tashqarida`);
          }
          if (p.step <= 0) bad.push(`${t.id}/${f.title}/${p.key}: step musbat emas`);
          if (!p.label) bad.push(`${t.id}/${f.title}/${p.key}: yorliq yo'q`);
        }
      }
    }
    expect(bad).toEqual([]);
  });
});
