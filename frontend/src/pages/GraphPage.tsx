import { useMemo, useState } from "react";
import { Link } from "react-router-dom";
import { api } from "../api/client";
import type { GraphNode, SubjectBrief } from "../api/types";
import { ErrorBox, Loading } from "../components/Layout";
import { useAsync } from "../hooks/useAsync";
import { useProgress } from "../hooks/useProgress";

const COLS = 5;

/**
 * Bog'liqlik xaritasi. Mavzular fan bo'yicha ustunlarga joylashadi,
 * bog'lanishlar esa egri chiziq bilan chiziladi. Mavzu ustiga kelganda
 * uning BUTUN oldingi zanjiri yoritiladi — bu DESIGN.md dagi asosiy
 * interaktiv g'oya.
 */
export function GraphPage({ subjects }: { subjects: SubjectBrief[] }) {
  const { data, loading, error, reload } = useAsync(() => api.graph(), []);
  const [focus, setFocus] = useState<string | null>(null);
  const { isDone } = useProgress();

  const layout = useMemo(() => {
    if (!data) return null;
    const order = new Map(subjects.map((s, i) => [s.id, i]));
    const perCol = new Map<string, GraphNode[]>();
    for (const n of data.nodes) {
      const arr = perCol.get(n.subject_id) ?? [];
      arr.push(n);
      perCol.set(n.subject_id, arr);
    }
    const pos = new Map<string, { x: number; y: number }>();
    const colW = 200;
    const rowH = 21;
    for (const [sid, list] of perCol) {
      const ci = order.get(sid) ?? 0;
      list.sort((a, b) => a.order - b.order);
      list.forEach((n, i) => pos.set(n.id, { x: 28 + ci * colW, y: 54 + i * rowH }));
    }
    const height = 54 + 30 * rowH + 20;
    return { pos, width: 28 + COLS * colW, height };
  }, [data, subjects]);

  const ancestors = useMemo(() => {
    if (!data || !focus) return new Set<string>();
    const back = new Map<string, string[]>();
    for (const e of data.edges) {
      back.set(e.target, [...(back.get(e.target) ?? []), e.source]);
    }
    const seen = new Set<string>();
    const stack = [focus];
    while (stack.length) {
      const cur = stack.pop()!;
      for (const p of back.get(cur) ?? []) {
        if (!seen.has(p)) { seen.add(p); stack.push(p); }
      }
    }
    return seen;
  }, [data, focus]);

  if (loading) return <Loading what="Graf yuklanmoqda" />;
  if (error) return <ErrorBox message={error} onRetry={reload} />;
  if (!data || !layout) return null;

  const byId = new Map(data.nodes.map((n) => [n.id, n]));

  return (
    <div style={{ padding: "1.3rem 0" }}>
      <h1>Bog'liqlik xaritasi</h1>
      <p className="muted" style={{ maxWidth: "62ch" }}>
        Har bir strelka — prerequisite bog'lanishi. Mavzu ustiga
        kelsangiz, uning butun oldingi zanjiri yoritiladi:
        shu mavzuga yetib borish uchun nimalarni bilish kerakligi
        darhol ko'rinadi.
      </p>
      <p className="mono tiny muted">
        {data.nodes.length} tugun · {data.edges.length} bog'lanish
        {focus && ` · ${focus} uchun ${ancestors.size} ta oldingi mavzu`}
      </p>

      <div style={{ overflowX: "auto", border: "1px solid var(--rule-faint)",
                    background: "var(--surface)" }}>
        <svg viewBox={`0 0 ${layout.width} ${layout.height}`}
             width={layout.width} height={layout.height}
             role="img" aria-label="Mavzular bog'liqlik grafi"
             onMouseLeave={() => setFocus(null)}>
          {subjects.map((s, i) => (
            <text key={s.id} x={28 + i * 200} y={30} fontSize="12"
                  fontFamily="var(--font-display)" fill="var(--ink)"
                  fontWeight="600" letterSpacing="0.06em">
              {s.code}
            </text>
          ))}

          {data.edges.map((e, i) => {
            const a = layout.pos.get(e.source);
            const b = layout.pos.get(e.target);
            if (!a || !b) return null;
            const lit = focus !== null &&
              (ancestors.has(e.target) || e.target === focus) && ancestors.has(e.source);
            const mx = (a.x + b.x) / 2;
            return (
              <path key={i}
                d={`M${a.x + 6} ${a.y} C ${mx} ${a.y}, ${mx} ${b.y}, ${b.x - 6} ${b.y}`}
                fill="none"
                stroke={lit ? "var(--tension)" : "var(--rule-faint)"}
                strokeWidth={lit ? 1.5 : 0.6}
                opacity={focus && !lit ? 0.25 : 1} />
            );
          })}

          {data.nodes.map((n) => {
            const p = layout.pos.get(n.id);
            if (!p) return null;
            const lit = focus === n.id || ancestors.has(n.id);
            const done = isDone(n.id);
            return (
              <g key={n.id} onMouseEnter={() => setFocus(n.id)}
                 style={{ cursor: "pointer" }}>
                <circle cx={p.x} cy={p.y} r={focus === n.id ? 5 : 3.4}
                        fill={done ? "var(--tension)" : lit ? "var(--mark)" : "var(--surface)"}
                        stroke={lit ? "var(--ink)" : "var(--rule)"} strokeWidth="1" />
                <text x={p.x + 9} y={p.y + 3.4} fontSize="9"
                      fontFamily="var(--font-mono)"
                      fill={lit ? "var(--ink)" : "var(--ink-soft)"}
                      opacity={focus && !lit ? 0.35 : 1}>
                  {n.id}
                </text>
                <title>{n.id} — {n.title}</title>
              </g>
            );
          })}
        </svg>
      </div>

      {focus && byId.get(focus) && (
        <div className="card" style={{ padding: "0.8rem 1rem", marginTop: "0.8rem" }}>
          <p className="mono tiny muted" style={{ margin: 0 }}>{focus}</p>
          <p style={{ margin: "2px 0 6px" }}>
            <Link to={`/mavzu/${focus}`}>{byId.get(focus)!.title}</Link>
          </p>
          <p className="small muted" style={{ margin: 0 }}>
            Bu mavzuga yetib borish uchun {ancestors.size} ta oldingi mavzu kerak.
          </p>
        </div>
      )}
    </div>
  );
}
