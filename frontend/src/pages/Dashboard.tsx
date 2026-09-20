import { Link } from "react-router-dom";
import { api } from "../api/client";
import type { SubjectBrief, TopicBrief } from "../api/types";
import { Epure, EpureRule } from "../components/Epure";
import { ErrorBox, Loading } from "../components/Layout";
import { useAsync } from "../hooks/useAsync";
import { useProgress } from "../hooks/useProgress";

export function Dashboard({ subjects }: { subjects: SubjectBrief[] }) {
  const { data: topics, loading, error, reload } =
    useAsync(() => api.topics({ limit: 300 }), []);
  const { isDone, countDone } = useProgress();

  if (loading) return <Loading what="Kurikulum yuklanmoqda" />;
  if (error) return <ErrorBox message={error} onRetry={reload} />;
  if (!topics) return null;

  const bySubject = new Map<string, TopicBrief[]>();
  for (const t of topics) {
    const arr = bySubject.get(t.subject_id) ?? [];
    arr.push(t);
    bySubject.set(t.subject_id, arr);
  }
  const doneTotal = countDone(topics.map((t) => t.id));
  const next = topics.find((t) => !isDone(t.id));

  return (
    <div>
      <section style={{ padding: "1.6rem 0 0.4rem" }}>
        <p className="mono tiny muted" style={{ letterSpacing: "0.14em", margin: 0 }}>
          NAZARIY MEXANIKADAN HISOBLASH MEXANIKASIGACHA
        </p>
        <h1 style={{ fontSize: "var(--t-2xl)", margin: "0.3rem 0 0.5rem", maxWidth: "22ch" }}>
          Besh fan, bitta uzluksiz zanjir
        </h1>
        <p className="muted" style={{ maxWidth: "62ch", margin: 0 }}>
          150 mavzuning har biri 18 bo'limli darsdan iborat: fizik masaladan
          boshlanib, qadam-baqadam chiqarish, sandbox'da bajariladigan
          hisob va keyingi mavzuga ko'prik bilan tugaydi.
        </p>

        <div style={{ display: "flex", alignItems: "center", gap: "1.2rem",
                      margin: "1.1rem 0 0", flexWrap: "wrap" }}>
          <Stat n={String(subjects.length)} label="fan" />
          <Stat n={String(topics.length)} label="mavzu" />
          <Stat n={String(topics.filter((t) => t.has_lab).length)} label="laboratoriya" />
          <Stat n={`${doneTotal}`} label="o'zlashtirilgan" accent />
        </div>

        {next && (
          <p style={{ marginTop: "1rem" }}>
            <Link to={`/mavzu/${next.id}`} className="display" style={{
              display: "inline-block", padding: "0.5rem 0.9rem",
              background: "var(--ink)", color: "var(--paper)",
              borderRadius: "var(--radius)", textDecoration: "none",
            }}>
              {doneTotal === 0 ? "Kursni boshlash" : "Davom etish"} → {next.id} · {next.title}
            </Link>
          </p>
        )}
      </section>

      <EpureRule />

      <ol style={{ listStyle: "none", padding: 0, margin: 0, display: "grid", gap: "0.9rem" }}>
        {subjects.map((s) => {
          const list = bySubject.get(s.id) ?? [];
          const done = countDone(list.map((t) => t.id));
          return (
            <li key={s.id} className="card" style={{ padding: "0.95rem 1.05rem" }}>
              <div style={{ display: "flex", gap: "0.8rem", alignItems: "baseline",
                            flexWrap: "wrap" }}>
                <span className="mono tag" aria-hidden="true">{s.code}</span>
                <h2 style={{ fontSize: "var(--t-md)" }}>
                  <Link to={`/fan/${s.id}`}>{s.order}. {s.title}</Link>
                </h2>
                <span className="mono tiny muted" style={{ marginLeft: "auto" }}>
                  {done} / {list.length}
                </span>
              </div>
              <p className="muted small" style={{ margin: "0.3rem 0 0.6rem", maxWidth: "70ch" }}>
                {s.tagline}
              </p>
              <Epure values={list.map((t) => isDone(t.id))} height={34}
                     title={`${s.title}: ${done} / ${list.length} o'zlashtirilgan`} />
            </li>
          );
        })}
      </ol>
    </div>
  );
}

function Stat({ n, label, accent = false }: { n: string; label: string; accent?: boolean }) {
  return (
    <span style={{ display: "flex", alignItems: "baseline", gap: 6 }}>
      <strong className="display" style={{
        fontSize: "var(--t-lg)", color: accent ? "var(--tension)" : "var(--ink)",
      }}>{n}</strong>
      <span className="muted small">{label}</span>
    </span>
  );
}
