import { useCallback, useEffect, useMemo, useState } from "react";
import { api } from "../api/client";
import type { Computation, RunResponse } from "../api/types";
import { CodeEditor } from "./CodeEditor";
import { Plot } from "./Plot";

/**
 * Interactive Lab: parametrni o'zgartirasiz → Run → hisob sandbox'da
 * bajariladi → grafik va qiymatlar yangilanadi.
 *
 * Kod backendga yuboriladi va u yerda IZOLYATSIYALANGAN jarayonda
 * bajariladi; brauzerda hech narsa hisoblanmaydi.
 */
export function Lab({ topicId, computation }: { topicId: string; computation: Computation }) {
  const initial = useMemo(
    () => Object.fromEntries(computation.parameters.map((p) => [p.key, p.default])),
    [computation.parameters],
  );
  const [params, setParams] = useState<Record<string, number>>(initial);
  const [code, setCode] = useState(computation.code);
  const [edited, setEdited] = useState(false);
  const [result, setResult] = useState<RunResponse | null>(null);
  const [busy, setBusy] = useState(false);
  const [err, setErr] = useState<string | null>(null);

  useEffect(() => {
    setParams(initial);
    setCode(computation.code);
    setEdited(false);
    setResult(null);
    setErr(null);
  }, [initial, computation.code]);

  const run = useCallback(async () => {
    setBusy(true);
    setErr(null);
    try {
      const r = await api.run(topicId, {
        params,
        ...(edited ? { code } : {}),
      });
      setResult(r);
    } catch (e) {
      setErr(e instanceof Error ? e.message : "Noma'lum xatolik");
    } finally {
      setBusy(false);
    }
  }, [topicId, params, code, edited]);

  return (
    <div>
      <p className="muted small" style={{ marginTop: 0 }}>{computation.caption}</p>

      {computation.parameters.length > 0 && (
        <div style={{
          display: "grid", gap: "0.7rem 1.4rem",
          gridTemplateColumns: "repeat(auto-fit, minmax(210px, 1fr))",
          margin: "0.8rem 0",
        }}>
          {computation.parameters.map((p) => (
            <label key={p.key} style={{ display: "block" }}>
              <span className="small" style={{ display: "flex", justifyContent: "space-between", gap: 8 }}>
                <span>{p.label}</span>
                <span className="mono tiny" style={{ color: "var(--tension)" }}>
                  {fmt(params[p.key] ?? p.default)}{p.unit && ` ${p.unit}`}
                </span>
              </span>
              <input
                type="range"
                min={p.minimum} max={p.maximum} step={p.step}
                value={params[p.key] ?? p.default}
                onChange={(e) =>
                  setParams((prev) => ({ ...prev, [p.key]: Number(e.target.value) }))}
                style={{ width: "100%", accentColor: "var(--tension)" }}
              />
              <span className="mono tiny muted" style={{ display: "flex", justifyContent: "space-between" }}>
                <span>{fmt(p.minimum)}</span><span>{fmt(p.maximum)}</span>
              </span>
            </label>
          ))}
        </div>
      )}

      <details style={{ margin: "0.6rem 0" }}>
        <summary className="small" style={{ cursor: "pointer" }}>
          Kodni ko'rish va tahrirlash
        </summary>
        <div style={{ marginTop: "0.6rem" }}>
          <CodeEditor
            value={code}
            onChange={(v) => { setCode(v); setEdited(true); }}
            onRun={run}
            height={360}
            ariaLabel={`${topicId} uchun Python kodi`}
          />
          <div style={{ display: "flex", gap: 10, marginTop: 6, alignItems: "center" }}>
            <span className="mono tiny muted">Ctrl+Enter — ishga tushirish</span>
            {edited && (
              <button type="button" className="mono tiny"
                      onClick={() => { setCode(computation.code); setEdited(false); }}
                      style={{ border: "1px solid var(--rule-faint)", padding: "2px 7px" }}>
                Asl kodga qaytarish
              </button>
            )}
          </div>
        </div>
      </details>

      <div style={{ display: "flex", gap: 10, alignItems: "center", margin: "0.7rem 0" }}>
        <button type="button" onClick={run} disabled={busy} className="display"
                style={{
                  padding: "0.42rem 1.1rem", background: busy ? "var(--rule)" : "var(--ink)",
                  color: "var(--paper)", borderRadius: "var(--radius)",
                  cursor: busy ? "progress" : "pointer",
                }}>
          {busy ? "Hisoblanmoqda…" : "▶ Ishga tushirish"}
        </button>
        {result && (
          <span className="mono tiny muted">{result.duration_ms} ms</span>
        )}
        {edited && <span className="tag">kod o'zgartirilgan</span>}
      </div>

      {err && (
        <div className="card" role="alert" style={{ padding: "0.7rem 0.9rem",
             borderLeft: "3px solid var(--tension)" }}>
          <span className="small">{err}</span>
        </div>
      )}

      {result && <RunOutput result={result} />}

      {!result && computation.expected_output && (
        <div className="card" style={{ padding: "0.7rem 0.9rem" }}>
          <p className="mono tiny muted" style={{ margin: "0 0 4px" }}>KUTILAYOTGAN NATIJA</p>
          <p className="small" style={{ margin: 0 }}>{computation.expected_output}</p>
        </div>
      )}
    </div>
  );
}

function RunOutput({ result }: { result: RunResponse }) {
  if (!result.ok) {
    return (
      <div className="card" role="alert" style={{ padding: "0.8rem 0.95rem",
           borderLeft: "3px solid var(--tension)" }}>
        <p className="display" style={{ margin: "0 0 4px" }}>
          Hisob bajarilmadi{result.error_type && ` — ${result.error_type}`}
        </p>
        <pre className="mono tiny" style={{ whiteSpace: "pre-wrap", margin: 0 }}>
          {result.error}
        </pre>
      </div>
    );
  }
  return (
    <div style={{ display: "grid", gap: "1rem" }}>
      {result.values.length > 0 && (
        <div>
          <h4 className="mono tiny muted" style={{ letterSpacing: "0.1em" }}>QIYMATLAR</h4>
          <table>
            <tbody>
              {result.values.map((v, i) => (
                <tr key={i}>
                  <td>{v.label}</td>
                  <td className="num" style={{ color: v.value < 0 ? "var(--compress)" : "var(--ink)" }}>
                    {fmt(v.value)}
                  </td>
                  <td className="mono tiny muted" style={{ width: "1%", whiteSpace: "nowrap" }}>
                    {v.unit}
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}

      {result.series.length > 0 && (
        <div>
          <h4 className="mono tiny muted" style={{ letterSpacing: "0.1em" }}>GRAFIKLAR</h4>
          <Plot series={result.series} />
        </div>
      )}

      {result.tables.map((t, i) => (
        <div key={i}>
          <h4 className="mono tiny muted" style={{ letterSpacing: "0.1em" }}>
            {t.title.toUpperCase()}
          </h4>
          <div style={{ overflowX: "auto" }}>
            <table>
              <thead><tr>{t.headers.map((h, k) => <th key={k}>{h}</th>)}</tr></thead>
              <tbody>
                {t.rows.map((r, k) => (
                  <tr key={k}>{r.map((c, j) => <td key={j} className={isNum(c) ? "num" : ""}>{c}</td>)}</tr>
                ))}
              </tbody>
            </table>
          </div>
        </div>
      ))}

      {result.notes.map((n, i) => (
        <p key={i} className="small" style={{
          borderLeft: "2px solid var(--mark)", paddingLeft: "0.7rem", margin: 0,
        }}>{n}</p>
      ))}

      {result.stdout.trim() && (
        <details>
          <summary className="mono tiny muted">print() chiqishi</summary>
          <pre className="mono tiny" style={{ whiteSpace: "pre-wrap" }}>{result.stdout}</pre>
        </details>
      )}
    </div>
  );
}

function isNum(s: string): boolean {
  return /^[-+]?[\d\s.,eE×^+-]+$/.test(s.trim()) && /\d/.test(s);
}

export function fmt(v: number): string {
  if (!Number.isFinite(v)) return "—";
  if (v === 0) return "0";
  const a = Math.abs(v);
  if (a >= 1e6 || a < 1e-4) return v.toExponential(4).replace("e+", "e");
  return String(Number(v.toPrecision(6)));
}
