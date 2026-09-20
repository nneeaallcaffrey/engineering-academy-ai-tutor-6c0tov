import { useEffect, useState } from "react";
import { NavLink, Link } from "react-router-dom";
import type { SubjectBrief } from "../api/types";

type Theme = "auto" | "light" | "dark";
const THEME_KEY = "mexanika:theme";

function readTheme(): Theme {
  try {
    const v = localStorage.getItem(THEME_KEY);
    return v === "light" || v === "dark" ? v : "auto";
  } catch {
    return "auto";
  }
}

/** Sarlavha bloki — chizma varag'ining title block'i kabi. */
export function TitleBlock({ subjects }: { subjects: SubjectBrief[] }) {
  const [theme, setTheme] = useState<Theme>(readTheme);

  useEffect(() => {
    const root = document.documentElement;
    if (theme === "auto") root.removeAttribute("data-theme");
    else root.setAttribute("data-theme", theme);
    try { localStorage.setItem(THEME_KEY, theme); } catch { /* ixtiyoriy */ }
  }, [theme]);

  const cycle = () =>
    setTheme((t) => (t === "auto" ? "light" : t === "light" ? "dark" : "auto"));

  return (
    <header style={{
      borderBottom: "1px solid var(--rule)", background: "var(--paper)",
      position: "sticky", top: 0, zIndex: 20,
    }}>
      <div className="wrap" style={{
        display: "flex", alignItems: "center", gap: "1rem",
        minHeight: 52, flexWrap: "wrap",
      }}>
        <Link to="/" className="display" style={{
          fontSize: "1.05rem", letterSpacing: "0.06em", fontWeight: 700,
          textTransform: "uppercase", whiteSpace: "nowrap",
        }}>
          Mexanika<span style={{ color: "var(--rule)" }}> / </span>Akademiyasi
        </Link>

        <nav aria-label="Fanlar" style={{ display: "flex", gap: 4, flexWrap: "wrap" }}>
          {subjects.map((s) => (
            <NavLink
              key={s.id}
              to={`/fan/${s.id}`}
              title={s.title}
              className="mono tiny"
              style={({ isActive }) => ({
                padding: "3px 8px",
                border: `1px solid ${isActive ? "var(--ink)" : "var(--rule-faint)"}`,
                background: isActive ? "var(--ink)" : "transparent",
                color: isActive ? "var(--paper)" : "var(--ink-soft)",
                borderRadius: "var(--radius)", textDecoration: "none",
              })}
            >
              {s.code}
            </NavLink>
          ))}
        </nav>

        <div style={{ marginLeft: "auto", display: "flex", gap: 12, alignItems: "center" }}>
          <NavLink to="/xarita" className="small">Xarita</NavLink>
          <NavLink to="/loyihalar" className="small">Loyihalar</NavLink>
          <NavLink to="/manbalar" className="small">Manbalar</NavLink>
          <button type="button" onClick={cycle} className="mono tiny"
                  aria-label={`Mavzu: ${theme}. O'zgartirish uchun bosing`}
                  title={`Rejim: ${theme}`}
                  style={{ border: "1px solid var(--rule-faint)", padding: "3px 7px",
                           borderRadius: "var(--radius)" }}>
            {theme === "auto" ? "◐" : theme === "light" ? "☀" : "☾"}
          </button>
        </div>
      </div>
    </header>
  );
}

export function Loading({ what = "Yuklanmoqda" }: { what?: string }) {
  return <p className="muted small" role="status">{what}…</p>;
}

export function ErrorBox({ message, onRetry }: { message: string; onRetry?: () => void }) {
  return (
    <div className="card" role="alert" style={{
      padding: "0.9rem 1rem", borderLeft: "3px solid var(--tension)",
    }}>
      <strong className="display" style={{ display: "block", marginBottom: 4 }}>
        Xatolik
      </strong>
      <span className="small">{message}</span>
      {onRetry && (
        <div style={{ marginTop: 8 }}>
          <button type="button" onClick={onRetry} className="mono tiny"
                  style={{ border: "1px solid var(--rule)", padding: "3px 9px" }}>
            Qayta urinish
          </button>
        </div>
      )}
    </div>
  );
}
