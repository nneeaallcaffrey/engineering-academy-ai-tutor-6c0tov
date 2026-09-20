import { useState } from "react";
import { api } from "../api/client";
import type { SubjectBrief } from "../api/types";
import { CodeEditor } from "../components/CodeEditor";
import { EpureRule } from "../components/Epure";
import { RichText } from "../components/Latex";
import { ErrorBox, Loading } from "../components/Layout";
import { useAsync } from "../hooks/useAsync";

export function ProjectsPage({ subjects }: { subjects: SubjectBrief[] }) {
  const { data, loading, error, reload } = useAsync(() => api.projects(), []);
  const [openCode, setOpenCode] = useState<string | null>(null);

  if (loading) return <Loading what="Loyihalar yuklanmoqda" />;
  if (error) return <ErrorBox message={error} onRetry={reload} />;
  if (!data) return null;

  const name = (id: string) => subjects.find((s) => s.id === id)?.title ?? id;

  return (
    <div style={{ padding: "1.3rem 0" }}>
      <h1>Yakuniy loyihalar</h1>
      <p className="muted" style={{ maxWidth: "64ch" }}>
        Har bir fan bitta yakuniy loyiha bilan yakunlanadi. Boshlang'ich
        kod ishlaydigan holatda beriladi va o'zini mustaqil tekshiradi —
        uni kengaytirish sizning vazifangiz.
      </p>

      {data.map((p) => (
        <section key={p.id} className="card"
                 style={{ padding: "1rem 1.1rem", marginBottom: "1rem" }}>
          <p className="mono tiny muted" style={{ margin: 0 }}>{name(p.subject_id)}</p>
          <h2 style={{ fontSize: "var(--t-md)", margin: "0.2rem 0 0.5rem" }}>{p.title}</h2>
          <RichText text={p.problem_statement} className="small" />

          <EpureRule />

          <div style={{ display: "grid", gap: "1rem",
                        gridTemplateColumns: "repeat(auto-fit, minmax(260px, 1fr))" }}>
            <div>
              <h3 className="mono tiny muted" style={{ letterSpacing: "0.1em" }}>BOSQICHLAR</h3>
              <ol style={{ paddingLeft: "1.1rem", margin: 0 }}>
                {p.stages.map((s, i) => (
                  <li key={i} style={{ marginBottom: "0.45rem" }}>
                    <strong className="display" style={{ fontSize: "var(--t-base)" }}>
                      {s.name}
                    </strong>
                    <br />
                    <span className="small muted">{s.detail}</span>
                  </li>
                ))}
              </ol>
            </div>
            <div>
              <h3 className="mono tiny muted" style={{ letterSpacing: "0.1em" }}>TOPSHIRILADI</h3>
              <ul style={{ paddingLeft: "1.1rem", margin: "0 0 0.9rem" }}>
                {p.deliverables.map((d, i) => <li key={i} className="small">{d}</li>)}
              </ul>
              <h3 className="mono tiny muted" style={{ letterSpacing: "0.1em" }}>BAHOLASH</h3>
              <ul style={{ paddingLeft: "1.1rem", margin: 0 }}>
                {p.evaluation.map((e, i) => <li key={i} className="small">{e}</li>)}
              </ul>
            </div>
          </div>

          <div style={{ marginTop: "0.9rem" }}>
            <button type="button" className="mono tiny"
                    onClick={() => setOpenCode(openCode === p.id ? null : p.id)}
                    style={{ border: "1px solid var(--rule)", padding: "3px 9px" }}>
              {openCode === p.id ? "Kodni yashirish" : "Boshlang'ich kodni ko'rish"}
            </button>
            {openCode === p.id && (
              <div style={{ marginTop: "0.6rem" }}>
                <CodeEditor value={p.starter_code} onChange={() => undefined}
                            readOnly height={420}
                            ariaLabel={`${p.title} boshlang'ich kodi`} />
              </div>
            )}
          </div>
        </section>
      ))}
    </div>
  );
}
