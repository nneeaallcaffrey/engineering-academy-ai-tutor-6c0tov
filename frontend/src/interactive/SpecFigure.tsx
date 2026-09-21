import { useEffect, useMemo, useState } from "react";
import type { FigureSpec } from "../api/types";
import { safeEval } from "./expr";
import { Controls, Figure, Readout, Slider, path, tickFmt } from "./ui";

const COLOR: Record<string, string> = {
  tension: "var(--tension)",
  compress: "var(--compress)",
  mark: "var(--mark)",
  rule: "var(--rule)",
  ink: "var(--ink)",
};

const W = 720, H = 360;
const L = 68, R = 26, T = 24, B = 50;
const IW = W - L - R, IH = H - T - B;

/**
 * Kurikulumdagi spetsifikatsiyadan interaktiv chizma quradi.
 *
 * Ifodalar `expr.ts` dagi xavfsiz hisoblagich bilan baholanadi — `eval`
 * ishlatilmaydi. Surgich surilganda hammasi brauzerda qayta hisoblanadi,
 * backendga murojaat qilinmaydi.
 */
/**
 * Tor ekranda SVG konteynerga sig'ish uchun ~0,47 marta kichrayadi, shuning
 * uchun yozuv o'lchamlari shunga yarasha kattalashtiriladi — aks holda o'q
 * belgilari telefonda o'qilmaydi.
 */
function useTextScale(): number {
  const [narrow, setNarrow] = useState(
    () => typeof window !== "undefined"
      && window.matchMedia("(max-width: 640px)").matches);
  useEffect(() => {
    const m = window.matchMedia("(max-width: 640px)");
    const on = () => setNarrow(m.matches);
    m.addEventListener("change", on);
    return () => m.removeEventListener("change", on);
  }, []);
  return narrow ? 1.85 : 1;
}

export function SpecFigure({ spec }: { spec: FigureSpec }) {
  const [vals, setVals] = useState<Record<string, number>>(() => defaults(spec));

  // O'lchov ramkasi surgichlarning BUTUN diapazoni bo'yicha bir marta hisoblanadi:
  // shunda surgich surilganda egri chiziq ramka ichida ko'tariladi yoki tushadi.
  // Avtomatik masshtab har safar qayta moslashtirilsa, rasm qimirlamagandek ko'rinardi.
  const fs = useTextScale();
  const frame = useMemo(() => stableFrame(spec), [spec]);
  const data = useMemo(() => build(spec, vals, frame, fs), [spec, vals, frame, fs]);

  return (
    <div>
      <Figure width={W} height={H} label={spec.title} note={spec.caption}>
        <Grid data={data} spec={spec} fs={fs} />
        {data.series.map((s, i) => (
          <path key={i} d={path(s.pts)} fill="none" stroke={COLOR[s.color] ?? COLOR.ink}
                strokeWidth={s.dashed ? 2 : 2.6}
                strokeDasharray={s.dashed ? "6 4" : undefined}
                strokeLinejoin="round" />
        ))}
        {data.series.length > 1 && data.series.map((s, i) => (
          <g key={`lg${i}`}>
            <line x1={L + 12} y1={T + 14 + i * 16 * fs} x2={L + 32} y2={T + 14 + i * 16 * fs}
                  stroke={COLOR[s.color] ?? COLOR.ink} strokeWidth="2.6"
                  strokeDasharray={s.dashed ? "5 3" : undefined} />
            <text x={L + 38} y={T + 18 + i * 16 * fs} fontSize={11 * fs} fill="var(--ink-soft)"
                  fontFamily="var(--font-mono)">{s.label}</text>
          </g>
        ))}
      </Figure>

      {spec.params.length > 0 && (
        <Controls>
          {spec.params.map((p) => (
            <Slider key={p.key} label={p.label} value={vals[p.key] ?? p.default}
                    min={p.minimum} max={p.maximum} step={p.step} unit={p.unit}
                    onChange={(v) => setVals((s) => ({ ...s, [p.key]: v }))} />
          ))}
        </Controls>
      )}

      {data.readouts.length > 0 && <Readout items={data.readouts} />}
      {spec.note && (
        <p className="tiny muted" style={{ marginTop: 6 }}>{spec.note}</p>
      )}
    </div>
  );
}

interface Series { label: string; color: string; dashed: boolean; pts: [number, number][]; }
interface Built {
  series: Series[];
  readouts: { label: string; value: string; color?: string }[];
  xTicks: { at: number; text: string }[];
  yTicks: { at: number; text: string }[];
  xLabel: string; yLabel: string;
  empty: boolean;
}

/** Surgichlarning sukutdagi holati. */
export function defaults(spec: FigureSpec): Record<string, number> {
  return Object.fromEntries(spec.params.map((p) => [p.key, p.default]));
}

/** Berilgan parametrlarda egri chiziqlar egallaydigan y oralig'i. */
export function yRange(spec: FigureSpec, vals: Record<string, number>): [number, number] {
  let lo = Infinity, hi = -Infinity;
  for (const r of sample(spec, vals)) {
    for (const [, y] of r.xy) { if (y < lo) lo = y; if (y > hi) hi = y; }
  }
  return Number.isFinite(lo) ? [lo, hi] : [0, 1];
}

/**
 * Surgichlarning chekka holatlarini ham qamrab oladigan barqaror o'lchov ramkasi.
 *
 * Har bir surgich alohida-alohida minimal va maksimal holatga qo'yiladi. Agar
 * natijada sukutdagi egri chiziq balandlikning 12% idan kam joy egallasa (masalan
 * parametr diapazoni bir necha tartibga cho'zilgan bo'lsa), ramka sukutdagi
 * ko'rinishga qaytariladi — aks holda boshlang'ich rasm o'qilmas bo'lib qolardi.
 */
export function stableFrame(spec: FigureSpec): [number, number] {
  const d = defaults(spec);
  const base = yRange(spec, d);
  let lo = base[0], hi = base[1];
  for (const p of spec.params) {
    for (const v of [p.minimum, p.maximum]) {
      const r = yRange(spec, { ...d, [p.key]: v });
      if (Number.isFinite(r[0]) && r[0] < lo) lo = r[0];
      if (Number.isFinite(r[1]) && r[1] > hi) hi = r[1];
    }
  }
  const span = hi - lo, baseSpan = base[1] - base[0];
  if (!(span > 0) || baseSpan / span < 0.12) return base;
  return [lo, hi];
}

interface Raw { label: string; color: string; dashed: boolean; xy: [number, number][]; }

/** Ko'rsatkichlarning ko'rinadigan qiymatlari — testlar uchun ochiq. */
export function readoutValues(spec: FigureSpec, vals: Record<string, number>): string[] {
  return build(spec, vals, [0, 1]).readouts.map((r) => r.value);
}

/** Chizmaning ekran koordinatalaridagi nuqtalari — testlar uchun ochiq. */
export function screenPoints(spec: FigureSpec, vals: Record<string, number>,
                             frame: [number, number]): [number, number][][] {
  return build(spec, vals, frame).series.map((s) => s.pts);
}

function sample(spec: FigureSpec, vals: Record<string, number>): Raw[] {
  const x0 = safeEval(spec.x_min, vals);
  const x1 = safeEval(spec.x_max, vals);
  const lo = Number.isFinite(x0) ? x0 : 0;
  const hi = Number.isFinite(x1) && x1 !== x0 ? x1 : lo + 1;
  const N = 200;
  const raw: Raw[] = [];
  for (const c of spec.curves) {
    if (c.when && !(safeEval(c.when, vals) > 0)) continue;
    const xy: [number, number][] = [];
    for (let i = 0; i <= N; i += 1) {
      const x = lo + ((hi - lo) * i) / N;
      const y = safeEval(c.expr, { ...vals, x });
      if (Number.isFinite(y)) xy.push([x, y]);
    }
    if (xy.length > 1) raw.push({ label: c.label, color: c.color, dashed: c.dashed, xy });
  }
  return raw;
}

function build(spec: FigureSpec, vals: Record<string, number>,
               frame: [number, number], fs = 1): Built {
  const nx = fs > 1.3 ? 3 : 6;
  const ny = fs > 1.3 ? 3 : 5;
  const x0 = safeEval(spec.x_min, vals);
  const x1 = safeEval(spec.x_max, vals);
  const lo = Number.isFinite(x0) ? x0 : 0;
  const hi = Number.isFinite(x1) && x1 !== x0 ? x1 : lo + 1;

  const raw = sample(spec, vals);

  // Joriy ma'lumot bilan sukutdagi ramkaning BIRLASHMASI: egri chiziq hech qachon
  // kesilmaydi, ammo masshtab har surishda qaytadan moslashtirilmaydi.
  const [dLo, dHi] = yRange(spec, vals);
  let yLo = Math.min(dLo, frame[0]);
  let yHi = Math.max(dHi, frame[1]);
  if (!Number.isFinite(yLo) || !Number.isFinite(yHi)) { yLo = 0; yHi = 1; }
  if (yLo === yHi) { yLo -= 0.5; yHi += 0.5; }
  const pad = (yHi - yLo) * 0.08;
  yLo -= pad; yHi += pad;

  const X = (x: number) => L + ((x - lo) / (hi - lo)) * IW;
  const Y = (y: number) => T + IH - ((y - yLo) / (yHi - yLo)) * IH;

  const series: Series[] = raw.map((r) => ({
    label: r.label, color: r.color, dashed: r.dashed,
    pts: r.xy.map(([x, y]) => [X(x), Y(y)] as [number, number]),
  }));

  const readouts = spec.readouts.map((r) => {
    const v = safeEval(r.expr, vals);
    let value: string;
    if (r.text) {
      const opts = r.text.split("|");
      value = v > 0 ? (opts[0] ?? "") : (opts[1] ?? "");
    } else {
      value = Number.isFinite(v) ? `${fmtVal(v)}${r.unit ? ` ${r.unit}` : ""}` : "—";
    }
    return { label: r.label, value, color: COLOR[r.color] ?? COLOR.ink };
  });

  return {
    series, readouts,
    xTicks: ticks(lo, hi, nx).map((v) => ({ at: X(v), text: tickFmt(v) })),
    yTicks: ticks(yLo, yHi, ny).map((v) => ({ at: Y(v), text: tickFmt(v) })),
    xLabel: spec.x_label, yLabel: spec.y_label,
    empty: series.length === 0,
  };
}

function Grid({ data, spec, fs }: { data: Built; spec: FigureSpec; fs: number }) {
  return (
    <g>
      {data.yTicks.map((t, i) => (
        <g key={`y${i}`}>
          <line x1={L} y1={t.at} x2={L + IW} y2={t.at} stroke="var(--rule-faint)"
                strokeWidth="0.7" strokeDasharray="2 3" />
          <text x={L - 7} y={t.at + 3.5 * fs} textAnchor="end" fontSize={10 * fs}
                fill="var(--ink-soft)" fontFamily="var(--font-mono)">{t.text}</text>
        </g>
      ))}
      {data.xTicks.map((t, i) => (
        <g key={`x${i}`}>
          <line x1={t.at} y1={T} x2={t.at} y2={T + IH} stroke="var(--rule-faint)"
                strokeWidth="0.7" strokeDasharray="2 3" />
          <text x={t.at} y={T + IH + 14 * fs} textAnchor="middle" fontSize={10 * fs}
                fill="var(--ink-soft)" fontFamily="var(--font-mono)">{t.text}</text>
        </g>
      ))}
      <line x1={L} y1={T} x2={L} y2={T + IH} stroke="var(--ink)" strokeWidth="1.2" />
      <line x1={L} y1={T + IH} x2={L + IW} y2={T + IH} stroke="var(--ink)" strokeWidth="1.2" />
      <text x={L + IW / 2} y={H - 12} textAnchor="middle" fontSize={11 * fs}
            fill="var(--ink-soft)" fontFamily="var(--font-display)">{spec.x_label}</text>
      <text x={18} y={T + IH / 2} textAnchor="middle" fontSize={11 * fs}
            fill="var(--ink-soft)" fontFamily="var(--font-display)"
            transform={`rotate(-90 18 ${T + IH / 2})`}>{spec.y_label}</text>
      {data.empty && (
        <text x={L + IW / 2} y={T + IH / 2} textAnchor="middle" fontSize={12 * fs}
              fill="var(--rule)" fontFamily="var(--font-mono)">
          bu parametrlarda egri chiziq yo'q
        </text>
      )}
    </g>
  );
}

function ticks(a: number, b: number, n: number): number[] {
  const span = b - a;
  if (!(span > 0)) return [a];
  const raw = span / n;
  const mag = 10 ** Math.floor(Math.log10(raw));
  const norm = raw / mag;
  const step = (norm >= 7.5 ? 10 : norm >= 3.5 ? 5 : norm >= 1.5 ? 2 : 1) * mag;
  const out: number[] = [];
  for (let v = Math.ceil(a / step) * step; v <= b + step * 1e-9; v += step) {
    out.push(Number(v.toFixed(12)));
  }
  return out;
}

function fmtVal(v: number): string {
  const a = Math.abs(v);
  if (v === 0) return "0";
  if (a >= 1e6 || a < 1e-4) return v.toExponential(3).replace("e+", "e");
  return String(Number(v.toPrecision(5)));
}
