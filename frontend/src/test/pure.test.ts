import { describe, expect, it } from "vitest";
import { fmtTick, ticks } from "../components/Plot";
import { splitMath } from "../components/Latex";
import { fmt } from "../components/Lab";

describe("ticks", () => {
  it("oraliqni qoplaydi va 'chiroyli' qadam tanlaydi", () => {
    const t = ticks(0, 10, 5);
    expect(t[0]).toBeGreaterThanOrEqual(0);
    expect(t[t.length - 1]).toBeLessThanOrEqual(10);
    expect(t.length).toBeGreaterThan(2);
    const step = t[1] - t[0];
    expect([1, 2, 2.5, 5, 10]).toContain(Number(step.toPrecision(2)));
  });

  it("nol kenglikdagi oraliqda yiqilmaydi", () => {
    expect(ticks(3, 3, 5)).toEqual([3]);
  });

  it("juda kichik sonlarda ham ishlaydi", () => {
    const t = ticks(1e-9, 5e-9, 4);
    expect(t.length).toBeGreaterThan(1);
    expect(t.every(Number.isFinite)).toBe(true);
  });
});

describe("fmtTick / fmt", () => {
  it("nolni qisqa yozadi", () => {
    expect(fmtTick(0)).toBe("0");
    expect(fmt(0)).toBe("0");
  });

  it("juda katta va juda kichik sonlar uchun eksponenta", () => {
    expect(fmtTick(1.2e7)).toMatch(/e/);
    expect(fmt(3.5e-8)).toMatch(/e/);
  });

  it("odatiy sonlarni o'qiladigan qiladi", () => {
    expect(fmt(91.83531)).toBe("91.8353");
    expect(fmtTick(250)).toBe("250");
  });

  it("chekli bo'lmagan qiymatni belgilaydi", () => {
    expect(fmt(Number.NaN)).toBe("—");
    expect(fmt(Number.POSITIVE_INFINITY)).toBe("—");
  });
});

describe("splitMath", () => {
  it("matn va formulani ajratadi", () => {
    const p = splitMath("Tenglama $E=mc^2$ mashhur.");
    expect(p.map((x) => x.kind)).toEqual(["text", "inline", "text"]);
    expect(p[1].body).toBe("E=mc^2");
  });

  it("blok formulani tanidi", () => {
    const p = splitMath("$$\\nabla^4 w = q/D$$");
    expect(p).toHaveLength(1);
    expect(p[0].kind).toBe("block");
  });

  it("formulasiz matnni butun qoldiradi", () => {
    const p = splitMath("Oddiy matn");
    expect(p).toEqual([{ kind: "text", body: "Oddiy matn" }]);
  });

  it("dollar belgisi yolg'iz bo'lsa yiqilmaydi", () => {
    expect(() => splitMath("narx 5$ edi")).not.toThrow();
  });
});
