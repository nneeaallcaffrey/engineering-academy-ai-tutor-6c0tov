import { api } from "../api/client";
import { ErrorBox, Loading } from "../components/Layout";
import { useAsync } from "../hooks/useAsync";

/** Akademik audit natijasi — kurikulum sifati ochiq ko'rsatiladi. */
export function AuditPage() {
  const { data, loading, error, reload } = useAsync(() => api.audit(), []);

  if (loading) return <Loading what="Audit yuklanmoqda" />;
  if (error) return <ErrorBox message={error} onRetry={reload} />;
  if (!data) return null;

  return (
    <div style={{ padding: "1.3rem 0" }}>
      <h1>Akademik audit</h1>
      <p className="muted" style={{ maxWidth: "62ch" }}>
        Kurikulum har bir eksportda avtomatik tekshiruvdan o'tadi:
        mavzular soni, takrorlanish, prerequisite tartibi, chiqarish
        chuqurligi, savollar soni va boshqalar.
      </p>

      <p className="display" style={{
        display: "inline-block", padding: "0.35rem 0.9rem",
        background: data.passed ? "var(--compress)" : "var(--tension)",
        color: "var(--paper)", borderRadius: "var(--radius)",
      }}>
        {data.passed ? "Barcha tekshiruvlar o'tdi" : "Tekshiruvlarda muammo bor"}
      </p>

      <ul style={{ listStyle: "none", padding: 0, margin: "1rem 0" }}>
        {data.checks.map((c) => (
          <li key={c.key} style={{
            display: "flex", gap: "0.7rem", alignItems: "baseline",
            padding: "0.4rem 0", borderBottom: "1px solid var(--rule-faint)",
          }}>
            <span aria-hidden="true" style={{
              width: 9, height: 9, flex: "0 0 auto",
              background: c.passed ? "var(--compress)" : "var(--tension)",
            }} />
            <span style={{ flex: 1 }}>{c.question}</span>
            <span className="mono tiny muted">{c.detail}</span>
          </li>
        ))}
      </ul>

      <h2 style={{ fontSize: "var(--t-md)" }}>Sonlar</h2>
      <table style={{ maxWidth: 420 }}>
        <tbody>
          {Object.entries(data.counts).map(([k, v]) => (
            <tr key={k}><td>{k}</td><td className="num">{v}</td></tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
