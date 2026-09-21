import { describe, expect, it } from "vitest";
import { readFileSync } from "node:fs";
import { resolve } from "node:path";
import type { FigureSpec } from "../api/types";
import { defaults, readoutValues, screenPoints, stableFrame } from "../interactive/SpecFigure";

const J = JSON.parse(readFileSync(
  resolve(__dirname, "../../../content/generated/curriculum.json"), "utf8"));

/** Surgich surilganda chizma ekranda eng ko'pi bilan necha piksel siljiydi. */
function shift(spec: FigureSpec, key: string, value: number): number {
  const d = defaults(spec);
  const frame = stableFrame(spec);
  const a = screenPoints(spec, d, frame);
  const b = screenPoints(spec, { ...d, [key]: value }, frame);
  if (a.length !== b.length) return 999;
  let m = 0;
  for (let i = 0; i < a.length; i += 1) {
    for (let k = 0; k < Math.min(a[i].length, b[i].length); k += 1) {
      m = Math.max(m, Math.abs(a[i][k][0] - b[i][k][0]),
                      Math.abs(a[i][k][1] - b[i][k][1]));
    }
  }
  return m;
}

/** Surgich ko'rsatkichlar qiymatini o'zgartiradimi. */
function readoutsChange(spec: FigureSpec, key: string, value: number): boolean {
  const d = defaults(spec);
  const a = readoutValues(spec, d).join("|");
  return [value].some((v) => readoutValues(spec, { ...d, [key]: v }).join("|") !== a);
}

describe("chizmalarning interaktivligi", () => {
  it("har bir surgich yo rasmni siljitadi, yo ko'rsatkichni o'zgartiradi", () => {
    const dead: string[] = [];
    let moves = 0, total = 0;
    for (const t of J.topics) {
      for (const [i, f] of (t.lesson.figures as FigureSpec[]).entries()) {
        for (const p of f.params) {
          total += 1;
          const picture = shift(f, p.key, p.minimum) > 4 || shift(f, p.key, p.maximum) > 4;
          if (picture) moves += 1;
          const readout = readoutsChange(f, p.key, p.minimum)
                       || readoutsChange(f, p.key, p.maximum);
          if (!picture && !readout) dead.push(`${t.id}#${i + 1}/${p.key}`);
        }
      }
    }
    console.log(`surgichlar: ${total} ta, shundan ${moves} tasi rasmni siljitadi, `
      + `qolgani ko'rsatkichni o'zgartiradi`);
    if (dead.length) console.log("mutlaqo harakatsiz:", dead.slice(0, 60).join(", "));
    expect(dead).toEqual([]);
  });

  it("birinchi surgich ham rasmni siljitadi (foydalanuvchi birinchi shuni suradi)", () => {
    const dead: string[] = [];
    for (const t of J.topics) {
      for (const [i, f] of (t.lesson.figures as FigureSpec[]).entries()) {
        const p = f.params[0];
        if (!p) { dead.push(`${t.id}#${i + 1}/surgich yo'q`); continue; }
        if (!(shift(f, p.key, p.minimum) > 4 || shift(f, p.key, p.maximum) > 4)) {
          dead.push(`${t.id}#${i + 1}/${p.key}`);
        }
      }
    }
    console.log("birinchi surgichi harakatsiz:", dead.length);
    if (dead.length) console.log(dead.slice(0, 60).join(", "));
    expect(dead).toEqual([]);
  });
});
