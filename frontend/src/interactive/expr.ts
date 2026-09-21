/**
 * Kichik matematik ifoda hisoblagichi.
 *
 * Kurikulumdagi chizma spetsifikatsiyalari matn ko'rinishidagi ifodalarni
 * beradi ("3*p*a^2/(4*h^2)"). Ularni baholash uchun `eval` ISHLATILMAYDI:
 * ifoda shunting-yard algoritmi bilan teskari polshcha yozuviga
 * o'tkaziladi va faqat ruxsat etilgan amallar hamda funksiyalar bajariladi.
 * Shu tariqa kontentdagi xato kodga aylanib ketmaydi.
 */

type Token =
  | { t: "num"; v: number }
  | { t: "name"; v: string }
  | { t: "op"; v: string }
  | { t: "lp" }
  | { t: "rp" }
  | { t: "comma" };

const has = (o: object, k: string) => Object.prototype.hasOwnProperty.call(o, k);

const FUNCS: Record<string, (...a: number[]) => number> = {
  sin: Math.sin, cos: Math.cos, tan: Math.tan,
  asin: Math.asin, acos: Math.acos, atan: Math.atan,
  sinh: Math.sinh, cosh: Math.cosh, tanh: Math.tanh,
  exp: Math.exp, sqrt: Math.sqrt, abs: Math.abs,
  log: Math.log, log10: Math.log10, log2: Math.log2,
  sign: Math.sign, floor: Math.floor, ceil: Math.ceil, round: Math.round,
  min: Math.min, max: Math.max,
  atan2: Math.atan2, pow: Math.pow, hypot: Math.hypot,
  // mexanikada tez-tez kerak bo'ladiganlar
  step: (x: number) => (x >= 0 ? 1 : 0),
  clamp: (x: number, a: number, b: number) => Math.min(Math.max(x, a), b),
};

const CONSTS: Record<string, number> = { pi: Math.PI, e: Math.E };

const PREC: Record<string, number> = {
  "?": 0, ":": 0,
  "||": 1, "&&": 2,
  "<": 3, ">": 3, "<=": 3, ">=": 3, "==": 3, "!=": 3,
  "+": 4, "-": 4,
  "*": 5, "/": 5, "%": 5,
  "^": 7,
  "u-": 6,
};
const RIGHT = new Set(["^", "u-"]);

export class ExprError extends Error {}

function tokenize(src: string): Token[] {
  const out: Token[] = [];
  let i = 0;
  const two = ["<=", ">=", "==", "!=", "&&", "||"];
  while (i < src.length) {
    const c = src[i];
    if (c === " " || c === "\t" || c === "\n") { i += 1; continue; }
    if (/[0-9.]/.test(c)) {
      let j = i;
      while (j < src.length && /[0-9.]/.test(src[j])) j += 1;
      if (src[j] === "e" || src[j] === "E") {
        let k = j + 1;
        if (src[k] === "+" || src[k] === "-") k += 1;
        if (/[0-9]/.test(src[k] ?? "")) {
          j = k;
          while (j < src.length && /[0-9]/.test(src[j])) j += 1;
        }
      }
      const v = Number(src.slice(i, j));
      if (!Number.isFinite(v)) throw new ExprError(`son o'qilmadi: ${src.slice(i, j)}`);
      out.push({ t: "num", v });
      i = j;
      continue;
    }
    if (/[A-Za-z_]/.test(c)) {
      let j = i;
      while (j < src.length && /[A-Za-z0-9_]/.test(src[j])) j += 1;
      out.push({ t: "name", v: src.slice(i, j) });
      i = j;
      continue;
    }
    if (c === "(") { out.push({ t: "lp" }); i += 1; continue; }
    if (c === ")") { out.push({ t: "rp" }); i += 1; continue; }
    if (c === ",") { out.push({ t: "comma" }); i += 1; continue; }
    const pair = src.slice(i, i + 2);
    if (two.includes(pair)) { out.push({ t: "op", v: pair }); i += 2; continue; }
    if ("+-*/%^<>?:".includes(c)) { out.push({ t: "op", v: c }); i += 1; continue; }
    throw new ExprError(`noma'lum belgi: '${c}'`);
  }
  return out;
}

/** Ifodani teskari polshcha yozuviga o'tkazadi (bir marta bajariladi). */
export function compile(src: string): Token[] {
  const toks = tokenize(src);
  const out: Token[] = [];
  const ops: Token[] = [];
  let prev: Token | null = null;

  const isValue = (t: Token | null) =>
    t !== null && (t.t === "num" || t.t === "name" || t.t === "rp");

  for (const tk of toks) {
    if (tk.t === "num") { out.push(tk); prev = tk; continue; }
    if (tk.t === "name") {
      if (has(FUNCS, tk.v)) ops.push(tk);
      else out.push(tk);
      prev = tk;
      continue;
    }
    if (tk.t === "comma") {
      while (ops.length && ops[ops.length - 1].t !== "lp") out.push(ops.pop()!);
      prev = tk;
      continue;
    }
    if (tk.t === "op") {
      let op = tk.v;
      if ((op === "-" || op === "+") && !isValue(prev)) op = op === "-" ? "u-" : "u+";
      if (op === "u+") { prev = tk; continue; }
      const p = PREC[op];
      if (p === undefined) throw new ExprError(`noma'lum amal: ${op}`);
      // Unar minus prefiks va o'ngdan chapga: undan oldin hech narsa
      // tushirilmaydi, aks holda 2^-1 noto'g'ri yig'iladi.
      while (op !== "u-" && ops.length) {
        const top = ops[ops.length - 1];
        if (top.t !== "op") break;
        const tp = PREC[top.v];
        if (tp > p || (tp === p && !RIGHT.has(op))) out.push(ops.pop()!);
        else break;
      }
      ops.push({ t: "op", v: op });
      prev = { t: "op", v: op };
      continue;
    }
    if (tk.t === "lp") { ops.push(tk); prev = tk; continue; }
    if (tk.t === "rp") {
      while (ops.length && ops[ops.length - 1].t !== "lp") out.push(ops.pop()!);
      if (!ops.length) throw new ExprError("qavs yopilmagan");
      ops.pop();
      if (ops.length && ops[ops.length - 1].t === "name") out.push(ops.pop()!);
      prev = tk;
      continue;
    }
  }
  while (ops.length) {
    const t = ops.pop()!;
    if (t.t === "lp") throw new ExprError("ortiqcha ochilgan qavs");
    out.push(t);
  }
  return out;
}

/** Kompilyatsiya qilingan ifodani berilgan o'zgaruvchilar bilan baholaydi. */
export function evalRPN(rpn: Token[], vars: Record<string, number>): number {
  const st: number[] = [];
  for (const tk of rpn) {
    if (tk.t === "num") { st.push(tk.v); continue; }
    if (tk.t === "name") {
      if (has(FUNCS, tk.v)) {
        const f = FUNCS[tk.v];
        const n = f.length || 1;
        const args = st.splice(Math.max(0, st.length - n), n);
        st.push(f(...args));
        continue;
      }
      if (has(vars, tk.v)) { st.push(vars[tk.v]); continue; }
      if (has(CONSTS, tk.v)) { st.push(CONSTS[tk.v]); continue; }
      throw new ExprError(`noma'lum nom: ${tk.v}`);
    }
    if (tk.t === "op") {
      if (tk.v === "u-") { st.push(-(st.pop() ?? 0)); continue; }
      if (tk.v === "?") continue;           // ternar ':' bilan birga ishlanadi
      if (tk.v === ":") {
        const b = st.pop() ?? 0, a = st.pop() ?? 0, c = st.pop() ?? 0;
        st.push(c ? a : b);
        continue;
      }
      const b = st.pop() ?? 0;
      const a = st.pop() ?? 0;
      switch (tk.v) {
        case "+": st.push(a + b); break;
        case "-": st.push(a - b); break;
        case "*": st.push(a * b); break;
        case "/": st.push(a / b); break;
        case "%": st.push(a % b); break;
        case "^": st.push(a ** b); break;
        case "<": st.push(a < b ? 1 : 0); break;
        case ">": st.push(a > b ? 1 : 0); break;
        case "<=": st.push(a <= b ? 1 : 0); break;
        case ">=": st.push(a >= b ? 1 : 0); break;
        case "==": st.push(a === b ? 1 : 0); break;
        case "!=": st.push(a !== b ? 1 : 0); break;
        case "&&": st.push(a && b ? 1 : 0); break;
        case "||": st.push(a || b ? 1 : 0); break;
        default: throw new ExprError(`bajarilmaydigan amal: ${tk.v}`);
      }
      continue;
    }
    throw new ExprError("kutilmagan token");
  }
  if (st.length !== 1) throw new ExprError("ifoda to'liq emas");
  return st[0];
}

const cache = new Map<string, Token[]>();

/** Ifodani baholaydi (kompilyatsiya natijasi keshlanadi). */
export function evaluate(src: string, vars: Record<string, number>): number {
  let rpn = cache.get(src);
  if (!rpn) {
    rpn = compile(src);
    cache.set(src, rpn);
  }
  return evalRPN(rpn, vars);
}

/** Xatoda yiqilmaydigan variant — NaN qaytaradi. */
export function safeEval(src: string, vars: Record<string, number>): number {
  try {
    const v = evaluate(src, vars);
    return Number.isFinite(v) ? v : NaN;
  } catch {
    return NaN;
  }
}
