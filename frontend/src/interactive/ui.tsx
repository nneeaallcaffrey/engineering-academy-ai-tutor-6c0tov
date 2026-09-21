import type { ReactNode } from "react";

/** Interaktiv chizmalar uchun umumiy boshqaruv va ramka elementlari. */

export function Slider({
  label, value, min, max, step, unit = "", onChange, color = "var(--tension)",
  fmt = (v: number) => String(Number(v.toPrecision(4))),
}: {
  label: string; value: number; min: number; max: number; step: number;
  unit?: string; onChange: (v: number) => void; color?: string;
  fmt?: (v: number) => string;
}) {
  return (
    <label style={{ display: "block" }}>
      <span className="small" style={{ display: "flex", justifyContent: "space-between", gap: 8 }}>
        <span>{label}</span>
        <span className="mono tiny" style={{ color }}>{fmt(value)}{unit && ` ${unit}`}</span>
      </span>
      <input
        type="range" min={min} max={max} step={step} value={value}
        onChange={(e) => onChange(Number(e.target.value))}
        style={{ width: "100%", accentColor: color }}
      />
    </label>
  );
}

export function Choice<T extends string>({
  label, value, options, onChange,
}: {
  label: string; value: T; options: { value: T; label: string }[];
  onChange: (v: T) => void;
}) {
  return (
    <div>
      <span className="small" style={{ display: "block", marginBottom: 3 }}>{label}</span>
      <div style={{ display: "flex", gap: 3, flexWrap: "wrap" }}>
        {options.map((o) => (
          <button
            key={o.value}
            type="button"
            onClick={() => onChange(o.value)}
            aria-pressed={value === o.value}
            className="mono tiny"
            style={{
              padding: "3px 9px", borderRadius: "var(--radius)",
              border: `1px solid ${value === o.value ? "var(--ink)" : "var(--rule-faint)"}`,
              background: value === o.value ? "var(--ink)" : "transparent",
              color: value === o.value ? "var(--paper)" : "var(--ink-soft)",
            }}
          >
            {o.label}
          </button>
        ))}
      </div>
    </div>
  );
}

/** Boshqaruvlar paneli — grid, mobilda bitta ustunga tushadi. */
export function Controls({ children }: { children: ReactNode }) {
  return (
    <div style={{
      display: "grid", gap: "0.6rem 1.3rem",
      gridTemplateColumns: "repeat(auto-fit, minmax(190px, 1fr))",
      margin: "0.7rem 0",
    }}>
      {children}
    </div>
  );
}

/** Hisoblangan qiymatlar qatori. */
export function Readout({ items }: { items: { label: string; value: string; color?: string }[] }) {
  return (
    <div style={{ display: "flex", flexWrap: "wrap", gap: "0.35rem 1.4rem", marginTop: "0.5rem" }}>
      {items.map((it) => (
        <span key={it.label} style={{ display: "flex", gap: 6, alignItems: "baseline" }}>
          <span className="tiny muted">{it.label}</span>
          <span className="mono small" style={{ color: it.color ?? "var(--ink)" }}>{it.value}</span>
        </span>
      ))}
    </div>
  );
}

/** SVG ramkasi — barcha chizmalar bir xil ko'rinishda. */
export function Figure({
  width = 720, height = 380, children, label, note,
}: {
  width?: number; height?: number; children: ReactNode; label: string; note?: string;
}) {
  return (
    <figure style={{ margin: 0 }}>
      <svg
        viewBox={`0 0 ${width} ${height}`}
        width="100%"
        role="img"
        aria-label={label}
        style={{
          display: "block", background: "var(--surface)",
          border: "1px solid var(--rule-faint)", borderRadius: "var(--radius)",
        }}
      >
        {children}
      </svg>
      {note && <figcaption className="tiny muted" style={{ marginTop: 4 }}>{note}</figcaption>}
    </figure>
  );
}

/** Chizmalar uchun o'q, to'r va yorliqlar. */
export function Axes({
  x, y, w, h, xLabel, yLabel, xTicks = [], yTicks = [], fmt = tickFmt,
}: {
  x: number; y: number; w: number; h: number;
  xLabel?: string; yLabel?: string;
  xTicks?: { at: number; text?: string }[];
  yTicks?: { at: number; text?: string }[];
  fmt?: (v: number) => string;
}) {
  return (
    <g>
      {yTicks.map((t, i) => (
        <g key={`y${i}`}>
          <line x1={x} y1={t.at} x2={x + w} y2={t.at} stroke="var(--rule-faint)"
                strokeWidth="0.7" strokeDasharray="2 3" />
          <text x={x - 6} y={t.at + 3.5} textAnchor="end" fontSize="10"
                fill="var(--ink-soft)" fontFamily="var(--font-mono)">
            {t.text ?? fmt(0)}
          </text>
        </g>
      ))}
      {xTicks.map((t, i) => (
        <g key={`x${i}`}>
          <line x1={t.at} y1={y} x2={t.at} y2={y + h} stroke="var(--rule-faint)"
                strokeWidth="0.7" strokeDasharray="2 3" />
          <text x={t.at} y={y + h + 14} textAnchor="middle" fontSize="10"
                fill="var(--ink-soft)" fontFamily="var(--font-mono)">
            {t.text ?? ""}
          </text>
        </g>
      ))}
      <line x1={x} y1={y} x2={x} y2={y + h} stroke="var(--ink)" strokeWidth="1.2" />
      <line x1={x} y1={y + h} x2={x + w} y2={y + h} stroke="var(--ink)" strokeWidth="1.2" />
      {xLabel && (
        <text x={x + w / 2} y={y + h + 30} textAnchor="middle" fontSize="11"
              fill="var(--ink-soft)" fontFamily="var(--font-display)">{xLabel}</text>
      )}
      {yLabel && (
        <text x={x - 34} y={y + h / 2} textAnchor="middle" fontSize="11"
              fill="var(--ink-soft)" fontFamily="var(--font-display)"
              transform={`rotate(-90 ${x - 34} ${y + h / 2})`}>{yLabel}</text>
      )}
    </g>
  );
}

export function tickFmt(v: number): string {
  if (v === 0) return "0";
  const a = Math.abs(v);
  if (a >= 1e5 || a < 1e-3) return v.toExponential(1).replace("e+", "e");
  if (a >= 100) return v.toFixed(0);
  if (a >= 10) return v.toFixed(1);
  return String(Number(v.toPrecision(3)));
}

/** Nuqtalar ro'yxatidan SVG yo'li. */
export function path(pts: [number, number][]): string {
  return pts.map((p, i) => `${i ? "L" : "M"}${p[0].toFixed(2)} ${p[1].toFixed(2)}`).join("");
}

/** Epyura shtrixi — bazaviy chiziqqa perpendikulyar chiziqlar. */
export function Hatch({
  base, values, scale, n = 26, positive = "var(--tension)", negative = "var(--compress)",
}: {
  base: { x0: number; y0: number; x1: number };
  values: number[];
  scale: number;
  n?: number;
  positive?: string;
  negative?: string;
}) {
  const { x0, y0, x1 } = base;
  const pts: [number, number][] = [];
  const lines: ReactNode[] = [];
  for (let i = 0; i < n; i += 1) {
    const t = i / (n - 1);
    const v = values[Math.round(t * (values.length - 1))] ?? 0;
    const X = x0 + (x1 - x0) * t;
    const Y = y0 - v * scale;
    pts.push([X, Y]);
    lines.push(
      <line key={i} x1={X} y1={y0} x2={X} y2={Y}
            stroke={v >= 0 ? positive : negative} strokeWidth="1.6" />,
    );
  }
  return (
    <g>
      {lines}
      <path d={path(pts)} fill="none" stroke="var(--ink)" strokeWidth="1.8" />
      <line x1={x0} y1={y0} x2={x1} y2={y0} stroke="var(--ink)" strokeWidth="2" />
    </g>
  );
}
