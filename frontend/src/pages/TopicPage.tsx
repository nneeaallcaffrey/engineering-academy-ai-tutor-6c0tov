import { useEffect, useState } from "react";
import { Link, useParams } from "react-router-dom";
import { api } from "../api/client";
import type { QuizItem } from "../api/types";
import { EpureRule } from "../components/Epure";
import { Lab } from "../components/Lab";
import { Latex, RichText } from "../components/Latex";
import { ErrorBox, Loading } from "../components/Layout";
import { interactiveFor } from "../interactive/registry";
import { SpecFigure } from "../interactive/SpecFigure";
import { useAsync } from "../hooks/useAsync";
import { useProgress } from "../hooks/useProgress";

/** Matn ustuni o'lchovi: qulay o'qish uchun taxminan 76 ta belgi. */
const MEASURE = "76ch";

/** Darsning 18 bo'limi — tartib MAJBURIY va shuning uchun nomerlanadi. */
export function TopicPage() {
  const { topicId = "" } = useParams();
  const { data, loading, error, reload } = useAsync(() => api.topic(topicId), [topicId]);
  const { isDone, setDone } = useProgress();

  useEffect(() => { window.scrollTo(0, 0); }, [topicId]);

  if (loading) return <Loading what="Mavzu yuklanmoqda" />;
  if (error) return <ErrorBox message={error} onRetry={reload} />;
  if (!data) return null;

  const L = data.lesson;
  const interactive = interactiveFor(data.id);
  const figures = L.figures ?? [];
  let n = 0;
  const no = () => String(++n).padStart(2, "0");

  return (
    <article style={{ padding: "1.3rem 0 2rem" }}>
      <p className="mono tiny muted"
         style={{ letterSpacing: "0.12em", margin: 0, maxWidth: MEASURE }}>
        <Link to={`/fan/${data.subject_id}`}>{data.subject_title}</Link>
        {" · "}{data.id}{" · "}{data.difficulty}{" · "}{data.estimated_minutes} daqiqa
      </p>

      <h1 style={{ margin: "0.3rem 0 0.5rem", maxWidth: MEASURE }}>{data.title}</h1>
      {(interactive || figures.length > 0) && (
        <p style={{ margin: "0 0 0.6rem" }}>
          <a href="#interaktiv" className="tag" style={{
            borderColor: "var(--tension)", color: "var(--tension)",
          }}>◆ {figures.length + (interactive ? 1 : 0)} ta interaktiv chizma</a>
        </p>
      )}

      <Section no={no()} title="Maqsad">
        <RichText text={data.learning_objective} />
      </Section>

      <Section no={no()} title="Talab qilinadigan bilim">
        {data.prerequisites.length === 0
          ? <p className="muted small">Oldindan talab yo'q — bu kirish mavzusi.</p>
          : <ul className="small" style={{ margin: 0, paddingLeft: "1.1rem" }}>
              {data.prerequisites.map((p) => (
                <li key={p}><Link to={`/mavzu/${p}`} className="mono">{p}</Link></li>
              ))}
            </ul>}
      </Section>

      {data.previous_link && (
        <Section no={no()} title="Oldingi mavzu bilan bog'lanish">
          <RichText text={data.previous_link} />
        </Section>
      )}

      <Section no={no()} title="Fizik masala">
        <RichText text={L.physical_problem} />
      </Section>

      <Section no={no()} title="Asosiy tushunchalar">
        <dl style={{ margin: 0 }}>
          {L.concepts.map((c, i) => (
            <div key={i} style={{ marginBottom: "0.6rem" }}>
              <dt className="display" style={{ fontSize: "var(--t-base)" }}>{c.term}</dt>
              <dd style={{ margin: "0.15rem 0 0 0" }}>
                <RichText text={c.definition} className="small" />
              </dd>
            </div>
          ))}
        </dl>
      </Section>

      <Section no={no()} title="Chiqarish">
        <ol style={{ listStyle: "none", padding: 0, margin: 0 }}>
          {L.derivation.map((d, i) => (
            <li key={i} style={{
              borderLeft: "2px solid var(--rule-faint)", paddingLeft: "0.9rem",
              marginBottom: "1rem",
            }}>
              <p className="display" style={{ margin: "0 0 0.3rem" }}>
                <span className="sec-no">{i + 1}.</span> {d.title}
              </p>
              <Latex tex={d.latex} display />
              <RichText text={d.explanation} className="small" />
            </li>
          ))}
        </ol>
      </Section>

      <Section no={no()} title="Formulalarning fizik ma'nosi">
        <RichText text={L.formula_meaning} />
      </Section>

      <Section no={no()} title="Asosiy tenglamalar">
        {L.equations.map((e, i) => (
          <div key={i} className="card" style={{ padding: "0.6rem 0.9rem", marginBottom: "0.6rem" }}>
            {e.name && <p className="mono tiny muted" style={{ margin: "0 0 3px" }}>
              {e.name.toUpperCase()}</p>}
            <Latex tex={e.latex} display />
            <RichText text={e.description} className="small muted" />
          </div>
        ))}
      </Section>

      <Section no={no()} title="Chegaraviy va boshlang'ich shartlar">
        <RichText text={L.conditions} />
      </Section>

      <Section no={no()} title="Yechilgan masala">
        <RichText text={L.worked_example.statement} />
        <p className="mono tiny muted" style={{ margin: "0.7rem 0 0.2rem" }}>BERILGAN</p>
        <ul className="small" style={{ margin: 0, paddingLeft: "1.1rem" }}>
          {L.worked_example.given.map((g, i) => <li key={i}>{g}</li>)}
        </ul>
        <ol style={{ paddingLeft: "1.1rem", marginTop: "0.8rem" }}>
          {L.worked_example.steps.map((s, i) => (
            <li key={i} style={{ marginBottom: "0.7rem" }}>
              <Latex tex={s.latex} display />
              <RichText text={s.text} className="small" />
            </li>
          ))}
        </ol>
        <div className="card" style={{ padding: "0.7rem 0.9rem",
             borderLeft: "3px solid var(--tension)" }}>
          <p className="mono tiny muted" style={{ margin: "0 0 3px" }}>JAVOB</p>
          <RichText text={L.worked_example.answer} />
        </div>
        {L.worked_example.engineering_note && (
          <p className="small" style={{ borderLeft: "2px solid var(--mark)",
             paddingLeft: "0.7rem", marginTop: "0.8rem" }}>
            <RichText text={L.worked_example.engineering_note} />
          </p>
        )}
      </Section>

      <Section no={no()} title="Interactive Lab" wide>
        <Lab topicId={data.id} computation={L.computation} />
      </Section>

      <Section no={no()} title="Vizualizatsiya" wide>
        <p className="small"><span className="tag">{L.visualization.tool}</span>{" "}
          {L.visualization.kind}</p>
        {interactive && (
          <div id="interaktiv" className="card"
               style={{ padding: "0.9rem 1rem", margin: "0.7rem 0 1rem", scrollMarginTop: 70 }}>
            <p className="mono tiny muted" style={{ margin: "0 0 2px", letterSpacing: "0.1em" }}>
              INTERAKTIV CHIZMA
            </p>
            <p className="display" style={{ fontSize: "var(--t-base)", margin: "0 0 0.6rem" }}>
              {interactive.title}
            </p>
            <interactive.Component />
          </div>
        )}
        {figures.map((f, i) => (
          <div key={i} id={i === 0 && !interactive ? "interaktiv" : undefined} className="card"
               style={{ padding: "0.9rem 1rem", margin: "0.7rem 0 1rem", scrollMarginTop: 70 }}>
            <p className="mono tiny muted" style={{ margin: "0 0 2px", letterSpacing: "0.1em" }}>
              INTERAKTIV CHIZMA {String(i + 1).padStart(2, "0")} / {String(figures.length).padStart(2, "0")}
            </p>
            <SpecFigure spec={f} />
          </div>
        ))}
        <RichText text={L.visualization.description} className="small" />
        <details style={{ marginTop: "0.5rem" }}>
          <summary className="small" style={{ cursor: "pointer" }}>Qanday chiziladi</summary>
          <RichText text={L.visualization.how_to_draw} className="small muted" />
        </details>
        {L.manim && (
          <div className="card" style={{ padding: "0.6rem 0.9rem", marginTop: "0.6rem" }}>
            <p className="mono tiny muted" style={{ margin: "0 0 3px" }}>
              MANIM SAHNASI · {L.manim.scene}
            </p>
            <p className="small" style={{ margin: 0 }}>{L.manim.summary}</p>
            <p className="mono tiny muted" style={{ margin: "5px 0 0" }}>{L.manim.module}</p>
          </div>
        )}
      </Section>

      <Section no={no()} title="Natijalarning talqini">
        <RichText text={L.interpretation} />
      </Section>

      <Section no={no()} title="Tipik xatolar">
        <ul style={{ margin: 0, paddingLeft: "1.1rem" }}>
          {L.common_mistakes.map((m, i) => (
            <li key={i} style={{ marginBottom: "0.4rem" }}>
              <RichText text={m} className="small" />
            </li>
          ))}
        </ul>
      </Section>

      <Section no={no()} title="Mustahkamlash savollari">
        <Quiz items={L.quiz} topicId={data.id} />
      </Section>

      <Section no={no()} title="Keyingi mavzuga ko'prik">
        <RichText text={L.bridge_to_next} />
      </Section>

      <Section no={no()} title="Tadqiqot yo'nalishi">
        <RichText text={L.research_extension} className="small" />
      </Section>

      <EpureRule />

      <div style={{ display: "flex", alignItems: "center", gap: "1rem", flexWrap: "wrap" }}>
        <label className="small" style={{ display: "flex", gap: 7, alignItems: "center" }}>
          <input type="checkbox" checked={isDone(data.id)}
                 onChange={(e) => setDone(data.id, e.target.checked)}
                 style={{ accentColor: "var(--tension)" }} />
          Bu mavzuni o'zlashtirdim
        </label>
      </div>

      <nav style={{ display: "flex", justifyContent: "space-between", gap: "1rem",
                    marginTop: "1rem", flexWrap: "wrap" }}>
        {data.prev_topic
          ? <Link to={`/mavzu/${data.prev_topic}`} className="small">← {data.prev_topic}</Link>
          : <span />}
        {data.next_topic
          ? <Link to={`/mavzu/${data.next_topic}`} className="display" style={{
              padding: "0.45rem 0.9rem", background: "var(--ink)", color: "var(--paper)",
              borderRadius: "var(--radius)", textDecoration: "none",
            }}>Keyingi: {data.next_topic} →</Link>
          : <span className="tag">Kurs yakuni</span>}
      </nav>
    </article>
  );
}

function Section({ no, title, children, wide = false }: {
  no: string; title: string; children: React.ReactNode; wide?: boolean;
}) {
  return (
    // Matn 76ch o'lchovida o'qiladi; chizma va laboratoriya bo'limlari esa
    // konteynerning butun kengligini egallaydi (300 ta chizma shu yerda turadi).
    <section style={{ margin: "1.5rem 0", maxWidth: wide ? "none" : MEASURE }}>
      <h2 style={{ fontSize: "var(--t-md)", marginBottom: "0.5rem" }}>
        <span className="sec-no">{no}</span>{"  "}{title}
      </h2>
      {children}
    </section>
  );
}

function Quiz({ items, topicId }: { items: QuizItem[]; topicId: string }) {
  const [open, setOpen] = useState<Set<number>>(new Set());
  const [picked, setPicked] = useState<Record<number, number>>({});
  const { setQuizScore } = useProgress();

  const score = items.reduce((acc, q, i) =>
    acc + (q.options.length > 0 && picked[i] === q.correct_index ? 1 : 0), 0);
  const answerable = items.filter((q) => q.options.length > 0).length;

  useEffect(() => {
    if (answerable > 0 && Object.keys(picked).length === answerable) {
      setQuizScore(topicId, score);
    }
  }, [picked, answerable, score, topicId, setQuizScore]);

  return (
    <div>
      {answerable > 0 && (
        <p className="mono tiny muted">
          {Object.keys(picked).length} / {answerable} javob berildi · to'g'ri: {score}
        </p>
      )}
      <ol style={{ paddingLeft: "1.1rem", margin: 0 }}>
        {items.map((q, i) => (
          <li key={i} style={{ marginBottom: "0.9rem" }}>
            <p style={{ margin: "0 0 0.35rem" }}>
              <RichText text={q.question} />
              <span className="tag" style={{ marginLeft: 6 }}>{q.kind}</span>
            </p>
            {q.options.length > 0 ? (
              <ul style={{ listStyle: "none", padding: 0, margin: 0, display: "grid", gap: 3 }}>
                {q.options.map((o, k) => {
                  const chosen = picked[i] === k;
                  const reveal = picked[i] !== undefined;
                  const correct = k === q.correct_index;
                  return (
                    <li key={k}>
                      <button type="button"
                        onClick={() => setPicked((p) => (p[i] === undefined ? { ...p, [i]: k } : p))}
                        disabled={reveal}
                        className="small"
                        style={{
                          display: "block", width: "100%", textAlign: "left",
                          padding: "0.3rem 0.55rem", borderRadius: "var(--radius)",
                          border: `1px solid ${
                            reveal && correct ? "var(--tension)"
                              : chosen ? "var(--rule)" : "var(--rule-faint)"}`,
                          background: reveal && correct
                            ? "color-mix(in srgb, var(--tension) 10%, transparent)"
                            : "transparent",
                          cursor: reveal ? "default" : "pointer",
                        }}>
                        {o}
                        {reveal && correct && <span style={{ color: "var(--tension)" }}> ✓</span>}
                      </button>
                    </li>
                  );
                })}
              </ul>
            ) : null}
            <button type="button" className="mono tiny"
              onClick={() => setOpen((s) => {
                const n = new Set(s); n.has(i) ? n.delete(i) : n.add(i); return n;
              })}
              style={{ marginTop: 5, color: "var(--ink-soft)", textDecoration: "underline" }}>
              {open.has(i) ? "Javobni yashirish" : "Javobni ko'rsatish"}
            </button>
            {open.has(i) && (
              <div style={{ borderLeft: "2px solid var(--mark)", paddingLeft: "0.7rem",
                            marginTop: 5 }}>
                <RichText text={q.answer} className="small" />
              </div>
            )}
          </li>
        ))}
      </ol>
    </div>
  );
}
