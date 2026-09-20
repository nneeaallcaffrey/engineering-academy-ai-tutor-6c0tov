import { useId, useMemo, useState } from "react";
import type { RunSeries } from "../api/types";

const PALETTE = [
  "var(--tension)", "var(--compress)", "var(--mark)",
  "#5E7F4B", "#7A4B7F", "#8A6A3B", "#3E7F77", "#96435C",
];

interface Box { w: number; h: number; l: number; r: number; t: number; b: number; }
const BOX: Box = { w: 720, h: 380, l: 62, r: 16, t: 18, b: 48 };

/**
 * Bir nechta seriyani bitta o'qda chizadi. Tashqi grafik kutubxona
 * ishlatilmaydi: o'qlar, belgilar va chiziqlar SVG'da qo'lda quriladi —
 * shunda ular epyura tilidan chetga chiqmaydi.
 */
export function Plot({ series, logY = false }: { series: RunSeries[]; logY?: boolean }) {
  const id = useId().replace(/:/g, "");
  const [hidden, setHidden] = useState<Set<number>>(new Set());
  const shown = series.filter((_, i) => !hidden.has(i));

  const scale = useMemo(() => computeScale(shown, logY), [shown, logY]);

  if (series.length === 0) return null;
  const { w, h, l, r, t, b } = BOX;
  const iw = w - l - r;
  const ih = h - t - b;

  const px = (x: number) => l + ((x - scale.x0) / (scale.x1 - scale.x0 || 1)) * iw;
  const py = (y: number) => {
    const v = logY ? Math.log10(Math.max(y, Number.MIN_VALUE)) : y;
    return t + ih - ((v - scale.y0) / (scale.y1 - scale.y0 || 1)) * ih;
  };

  const xlabel = series.find((s) => s.xlabel)?.xlabel ?? "";
  const ylabel = series.find((s) => s.ylabel)?.ylabel ?? "";

  return (
    <div>
      <svg viewBox={`0 0 ${w} ${h}`} width="100%" role="img"
           aria-label={`Grafik: ${series.map((s) => s.label).join(", ")}`}
           style={{ display: "block", background: "var(--surface)", border: "1px solid var(--rule-faint)" }}>
        {/* to'r */}
        {scale.yTicks.map((v, i) => (
          <g key={`y${i}`}>
            <line x1={l} y1={py(logY ? 10 ** v : v)} x2={w - r} y2={py(logY ? 10 ** v : v)}
                  stroke="var(--rule-faint)" strokeWidth="0.7" strokeDasharray="2 3" />
            <text x={l - 7} y={py(logY ? 10 ** v : v) + 3.5} textAnchor="end"
                  fontSize="10" fill="var(--ink-soft)" fontFamily="var(--font-mono)">
              {fmtTick(logY ? 10 ** v : v)}
            </text>
          </g>
        ))}
        {scale.xTicks.map((v, i) => (
          <g key={`x${i}`}>
            <line x1={px(v)} y1={t} x2={px(v)} y2={t + ih}
                  stroke="var(--rule-faint)" strokeWidth="0.7" strokeDasharray="2 3" />
            <text x={px(v)} y={t + ih + 15} textAnchor="middle"
                  fontSize="10" fill="var(--ink-soft)" fontFamily="var(--font-mono)">
              {fmtTick(v)}
            </text>
          </g>
        ))}

        {/* o'qlar: chizmadagi kabi qalinroq */}
        <line x1={l} y1={t} x2={l} y2={t + ih} stroke="var(--ink)" strokeWidth="1.2" />
        <line x1={l} y1={t + ih} x2={w - r} y2={t + ih} stroke="var(--ink)" strokeWidth="1.2" />

        {shown.map((s) => {
          const idx = series.indexOf(s);
          const color = PALETTE[idx % PALETTE.length];
          const d = buildPath(s, px, py);
          return (
            <g key={s.label}>
              <path d={d} fill="none" stroke={color} strokeWidth="1.7"
                    strokeLinejoin="round" strokeLinecap="round" />
              {s.x.length <= 40 &&
                s.x.map((xv, k) => (
                  <circle key={k} cx={px(xv)} cy={py(s.y[k])} r="2.4" fill={color} />
                ))}
            </g>
          );
        })}

        {xlabel && (
          <text x={l + iw / 2} y={h - 8} textAnchor="middle" fontSize="11"
                fill="var(--ink-soft)" fontFamily="var(--font-display)">{xlabel}</text>
        )}
        {ylabel && (
          <text x={14} y={t + ih / 2} textAnchor="middle" fontSize="11"
                fill="var(--ink-soft)" fontFamily="var(--font-display)"
                transform={`rotate(-90 14 ${t + ih / 2})`}>{ylabel}</text>
        )}
      </svg>

      {series.length > 1 && (
        <ul style={{ display: "flex", flexWrap: "wrap", gap: "4px 14px",
                     listStyle: "none", padding: "8px 0 0", margin: 0 }}>
          {series.map((s, i) => (
            <li key={s.label}>
              <button
                type="button"
                onClick={() => setHidden((prev) => {
                  const n = new Set(prev);
                  n.has(i) ? n.delete(i) : n.add(i);
                  return n;
                })}
                aria-pressed={!hidden.has(i)}
                className="tiny"
                style={{
                  display: "flex", alignItems: "center", gap: 6,
                  opacity: hidden.has(i) ? 0.4 : 1,
                  fontFamily: "var(--font-mono)",
                }}
              >
                <span aria-hidden="true" style={{
                  width: 13, height: 3, background: PALETTE[i % PALETTE.length],
                  display: "inline-block",
                }} />
                {s.label}
              </button>
            </li>
          ))}
        </ul>
      )}
      <span id={`plot-${id}`} hidden />
    </div>
  );
}

function buildPath(s: RunSeries, px: (n: number) => number, py: (n: number) => number): string {
  let d = "";
  for (let i = 0; i < s.x.length; i += 1) {
    const X = px(s.x[i]);
    const Y = py(s.y[i]);
    if (!Number.isFinite(X) || !Number.isFinite(Y)) continue;
    d += `${d === "" ? "M" : "L"}${X.toFixed(2)} ${Y.toFixed(2)}`;
  }
  return d;
}

interface Scale { x0: number; x1: number; y0: number; y1: number; xTicks: number[]; yTicks: number[]; }

function computeScale(series: RunSeries[], logY: boolean): Scale {
  if (series.length === 0) {
    return { x0: 0, x1: 1, y0: 0, y1: 1, xTicks: [], yTicks: [] };
  }
  let x0 = Infinity, x1 = -Infinity, y0 = Infinity, y1 = -Infinity;
  for (const s of series) {
    for (const v of s.x) { if (v < x0) x0 = v; if (v > x1) x1 = v; }
    for (const v of s.y) {
      const t = logY ? (v > 0 ? Math.log10(v) : NaN) : v;
      if (!Number.isFinite(t)) continue;
      if (t < y0) y0 = t;
      if (t > y1) y1 = t;
    }
  }
  if (!Number.isFinite(x0)) { x0 = 0; x1 = 1; }
  if (!Number.isFinite(y0)) { y0 = 0; y1 = 1; }
  if (x0 === x1) { x0 -= 0.5; x1 += 0.5; }
  if (y0 === y1) { y0 -= 0.5; y1 += 0.5; }
  const pad = (y1 - y0) * 0.06;
  y0 -= pad; y1 += pad;
  return { x0, x1, y0, y1, xTicks: ticks(x0, x1, 6), yTicks: ticks(y0, y1, 5) };
}

export function ticks(a: number, b: number, n: number): number[] {
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

export function fmtTick(v: number): string {
  if (v === 0) return "0";
  const a = Math.abs(v);
  if (a >= 1e5 || a < 1e-3) return v.toExponential(1).replace("e+", "e");
  if (a >= 100) return v.toFixed(0);
  if (a >= 1) return String(Number(v.toFixed(2)));
  return String(Number(v.toPrecision(3)));
}
