import { Link, useParams } from "react-router-dom";
import { api } from "../api/client";
import { Epure, EpureRule } from "../components/Epure";
import { ErrorBox, Loading } from "../components/Layout";
import { RichText } from "../components/Latex";
import { interactiveFor } from "../interactive/registry";
import { useAsync } from "../hooks/useAsync";
import { useProgress } from "../hooks/useProgress";

export function SubjectPage() {
  const { subjectId = "" } = useParams();
  const { data, loading, error, reload } =
    useAsync(() => api.subject(subjectId), [subjectId]);
  const { isDone, countDone } = useProgress();

  if (loading) return <Loading what="Fan yuklanmoqda" />;
  if (error) return <ErrorBox message={error} onRetry={reload} />;
  if (!data) return null;

  const done = countDone(data.topics.map((t) => t.id));

  return (
    <article style={{ padding: "1.4rem 0" }}>
      <p className="mono tiny muted" style={{ letterSpacing: "0.14em", margin: 0 }}>
        {data.code} · {data.order}-FAN
      </p>
      <h1 style={{ margin: "0.25rem 0 0.4rem", maxWidth: "26ch" }}>{data.title}</h1>
      <p className="muted" style={{ maxWidth: "66ch", marginTop: 0 }}>{data.tagline}</p>

      <Epure values={data.topics.map((t) => isDone(t.id))} height={40}
             title={`${done} / ${data.topics.length} o'zlashtirilgan`} />
      <p className="mono tiny muted">{done} / {data.topics.length} mavzu o'zlashtirilgan</p>

      {data.description && (
        <RichText text={data.description} className="small" />
      )}

      <EpureRule />

      {data.modules.map((m) => {
        const list = data.topics.filter((t) => t.module_id === m.id);
        return (
          <section key={m.id} style={{ marginBottom: "1.6rem" }}>
            <h2 style={{ fontSize: "var(--t-md)" }}>
              <span className="sec-no">{String(m.order).padStart(2, "0")}</span>{" "}
              {m.title}
            </h2>
            <p className="muted small" style={{ margin: "0.2rem 0 0.7rem", maxWidth: "70ch" }}>
              {m.summary}
            </p>
            <ol style={{ listStyle: "none", padding: 0, margin: 0, display: "grid", gap: 1 }}>
              {list.map((t) => (
                <li key={t.id}>
                  <Link to={`/mavzu/${t.id}`} style={{
                    display: "flex", gap: "0.7rem", alignItems: "baseline",
                    padding: "0.42rem 0.6rem", borderBottom: "1px solid var(--rule-faint)",
                    textDecoration: "none",
                  }}>
                    <span aria-hidden="true" style={{
                      width: 9, height: 9, flex: "0 0 auto", marginTop: 5,
                      border: `1px solid ${isDone(t.id) ? "var(--tension)" : "var(--rule)"}`,
                      background: isDone(t.id) ? "var(--tension)" : "transparent",
                    }} />
                    <span className="mono tiny muted" style={{ minWidth: 48 }}>{t.id}</span>
                    <span style={{ flex: 1 }}>{t.title}</span>
                    {interactiveFor(t.id) && (
                      <span className="tag" style={{
                        borderColor: "var(--tension)", color: "var(--tension)",
                      }}>◆ chizma</span>
                    )}
                    {t.has_lab && <span className="tag">lab</span>}
                    <span className="mono tiny muted">{t.estimated_minutes}′</span>
                  </Link>
                </li>
              ))}
            </ol>
          </section>
        );
      })}

      {data.assessments.length > 0 && (
        <section>
          <EpureRule />
          <h2 style={{ fontSize: "var(--t-md)", marginBottom: "0.6rem" }}>Baholash</h2>
          <table>
            <thead>
              <tr><th>Tur</th><th>Nomi</th><th>Qamrov</th><th className="num">Ulush</th></tr>
            </thead>
            <tbody>
              {data.assessments.map((a, i) => (
                <tr key={i}>
                  <td className="mono tiny">{a.kind}</td>
                  <td>{a.title}</td>
                  <td className="mono tiny muted">{a.covers}</td>
                  <td className="num">{a.weight}%</td>
                </tr>
              ))}
            </tbody>
          </table>
        </section>
      )}
    </article>
  );
}
