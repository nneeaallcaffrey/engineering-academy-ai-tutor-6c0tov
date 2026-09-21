import { describe, expect, it } from "vitest";
import { ExprError, compile, evaluate, safeEval } from "../interactive/expr";

const V = { x: 2, a: 3, h: 0.5, p: 10 };

describe("evaluate", () => {
  it("arifmetika va ustunlik", () => {
    expect(evaluate("1+2*3", {})).toBe(7);
    expect(evaluate("(1+2)*3", {})).toBe(9);
    expect(evaluate("2^3^2", {})).toBe(512);      // o'ngdan chapga
    expect(evaluate("-2^2", {})).toBe(-4);
    expect(evaluate("10/4", {})).toBe(2.5);
  });

  it("o'zgaruvchilar va konstantalar", () => {
    expect(evaluate("x*a", V)).toBe(6);
    expect(evaluate("pi", {})).toBeCloseTo(Math.PI, 12);
    expect(evaluate("2*pi*a", V)).toBeCloseTo(2 * Math.PI * 3, 12);
  });

  it("funksiyalar", () => {
    expect(evaluate("sin(0)", {})).toBe(0);
    expect(evaluate("sqrt(16)", {})).toBe(4);
    expect(evaluate("max(3, 7)", {})).toBe(7);
    expect(evaluate("hypot(3, 4)", {})).toBe(5);
    expect(evaluate("abs(0-5)", {})).toBe(5);
  });

  it("haqiqiy mexanika ifodasi", () => {
    // sigma = 3 p a^2 / (4 h^2)
    const s = evaluate("3*p*a^2/(4*h^2)", V);
    expect(s).toBeCloseTo((3 * 10 * 9) / (4 * 0.25), 10);
  });

  it("taqqoslash va shartli", () => {
    expect(evaluate("x > 1", V)).toBe(1);
    expect(evaluate("x < 1", V)).toBe(0);
    expect(evaluate("(x > 1) ? 10 : 20", V)).toBe(10);
    expect(evaluate("(x < 1) ? 10 : 20", V)).toBe(20);
  });

  it("eksponensial yozuv", () => {
    expect(evaluate("2.1e3", {})).toBe(2100);
    expect(evaluate("1e-3", {})).toBeCloseTo(0.001, 12);
  });

  it("noma'lum nom xato beradi", () => {
    expect(() => evaluate("qqq+1", {})).toThrow(ExprError);
  });

  it("buzuq ifoda xato beradi", () => {
    expect(() => compile("2*(3+")).toThrow(ExprError);
    expect(() => evaluate("2 $ 3", {})).toThrow(ExprError);
  });

  it("safeEval yiqilmaydi", () => {
    expect(Number.isNaN(safeEval("qqq", {}))).toBe(true);
    expect(Number.isNaN(safeEval("1/0", {}))).toBe(true);
    expect(safeEval("2+2", {})).toBe(4);
  });

  it("eval ishlatilmaydi — kod bajarilmaydi", () => {
    expect(() => evaluate("constructor", {})).toThrow(ExprError);
    expect(() => evaluate("globalThis", {})).toThrow(ExprError);
  });
});
