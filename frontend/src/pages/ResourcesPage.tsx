import { api } from "../api/client";
import type { SubjectBrief } from "../api/types";
import { ErrorBox, Loading } from "../components/Layout";
import { useAsync } from "../hooks/useAsync";

export function ResourcesPage({ subjects }: { subjects: SubjectBrief[] }) {
  const { data, loading, error, reload } = useAsync(() => api.resources(), []);

  if (loading) return <Loading what="Manbalar yuklanmoqda" />;
  if (error) return <ErrorBox message={error} onRetry={reload} />;
  if (!data) return null;

  return (
    <div style={{ padding: "1.3rem 0" }}>
      <h1>Manbalar</h1>
      <p className="muted" style={{ maxWidth: "60ch" }}>
        Har bir fan uchun asosiy darsliklar va qo'shimcha adabiyot.
      </p>
      {subjects.map((s) => {
        const list = data.filter((r) => r.subject_id === s.id);
        if (list.length === 0) return null;
        return (
          <section key={s.id} style={{ marginBottom: "1.4rem" }}>
            <h2 style={{ fontSize: "var(--t-md)", marginBottom: "0.5rem" }}>
              <span className="tag">{s.code}</span> {s.title}
            </h2>
            <table>
              <thead>
                <tr><th>Nomi</th><th>Muallif</th><th>Yil</th><th>Tur</th></tr>
              </thead>
              <tbody>
                {list.map((r) => (
                  <tr key={r.id}>
                    <td>{r.title}
                      {r.note && <><br /><span className="tiny muted">{r.note}</span></>}
                    </td>
                    <td className="small">{r.author}</td>
                    <td className="mono tiny">{r.year}</td>
                    <td><span className="tag">{r.kind}</span></td>
                  </tr>
                ))}
              </tbody>
            </table>
          </section>
        );
      })}
    </div>
  );
}
