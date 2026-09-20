import { useId } from "react";

/**
 * Epyura — platformaning signature elementi.
 *
 * Mexanikada har bir kattalik epyura sifatida chiziladi: bazaviy chiziqqa
 * perpendikulyar shtrixlar bilan to'ldirilgan diagramma, ishorasi esa
 * chiziqning qaysi tomonida yotishiga qarab beriladi. Bu yerda ham xuddi
 * shunday: tugallangan mavzular bazaviy chiziqdan YUQORIDA (cho'zilish),
 * tugallanmaganlari PASTDA (siqilish) shtrixlanadi.
 *
 * Shtrix SVG <pattern> bilan haqiqiy chiziladi, rasm emas.
 */
export function Epure({
  values,
  height = 40,
  barWidth = 6,
  gap = 2,
  title,
}: {
  /** Har bir mavzu: true = o'zlashtirilgan */
  values: boolean[];
  height?: number;
  barWidth?: number;
  gap?: number;
  title?: string;
}) {
  const id = useId().replace(/:/g, "");
  const w = values.length * (barWidth + gap);
  const mid = height / 2;
  const amp = height / 2 - 3;

  return (
    <svg
      width="100%"
      viewBox={`0 0 ${Math.max(w, 1)} ${height}`}
      height={height}
      preserveAspectRatio="none"
      role="img"
      aria-label={title ?? `${values.filter(Boolean).length} / ${values.length} mavzu o'zlashtirilgan`}
      style={{ display: "block", overflow: "visible" }}
    >
      <defs>
        <pattern id={`h-up-${id}`} width="3" height="3" patternUnits="userSpaceOnUse"
                 patternTransform="rotate(45)">
          <line x1="0" y1="0" x2="0" y2="3" stroke="var(--tension)" strokeWidth="1.2" />
        </pattern>
        <pattern id={`h-dn-${id}`} width="3" height="3" patternUnits="userSpaceOnUse"
                 patternTransform="rotate(-45)">
          <line x1="0" y1="0" x2="0" y2="3" stroke="var(--rule)" strokeWidth="0.9" />
        </pattern>
      </defs>

      {values.map((done, i) => {
        const x = i * (barWidth + gap);
        const h = done ? amp : amp * 0.45;
        return (
          <rect
            key={i}
            x={x}
            y={done ? mid - h : mid}
            width={barWidth}
            height={h}
            fill={done ? `url(#h-up-${id})` : `url(#h-dn-${id})`}
            stroke={done ? "var(--tension)" : "var(--rule-faint)"}
            strokeWidth="0.6"
          />
        );
      })}

      {/* bazaviy chiziq — epyuraning o'qi */}
      <line x1="0" y1={mid} x2={Math.max(w, 1)} y2={mid}
            stroke="var(--ink)" strokeWidth="1" />
    </svg>
  );
}

/** Bo'lim ajratkichi: bazaviy chiziq + qisqa shtrix qatori. */
export function EpureRule() {
  return <div className="epure-rule" aria-hidden="true" />;
}
