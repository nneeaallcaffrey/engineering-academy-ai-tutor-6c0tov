import katex from "katex";
import { useMemo } from "react";

/** Bitta LaTeX ifodani chizadi. Xato bo'lsa — manbani ko'rsatadi. */
export function Latex({ tex, display = false }: { tex: string; display?: boolean }) {
  const html = useMemo(() => {
    try {
      return katex.renderToString(tex, {
        displayMode: display,
        throwOnError: false,
        strict: false,
        trust: false,          // \href va \url ishlamaydi — XSS yo'li yopiq
      });
    } catch {
      return null;
    }
  }, [tex, display]);

  if (html === null) {
    return <code className="mono small">{tex}</code>;
  }
  return <span dangerouslySetInnerHTML={{ __html: html }} />;
}

/**
 * Matn ichidagi $...$ va $$...$$ bo'laklarini formulaga aylantiradi.
 * Kurikulum matnida formulalar aynan shu ko'rinishda yoziladi.
 */
export function RichText({ text, className }: { text: string; className?: string }) {
  const parts = useMemo(() => splitMath(text), [text]);
  return (
    <div className={className}>
      {parts.map((p, i) =>
        p.kind === "text" ? (
          <Markdownish key={i} text={p.body} />
        ) : (
          <Latex key={i} tex={p.body} display={p.kind === "block"} />
        ),
      )}
    </div>
  );
}

type Part = { kind: "text" | "inline" | "block"; body: string };

export function splitMath(text: string): Part[] {
  const out: Part[] = [];
  const re = /\$\$([\s\S]+?)\$\$|\$([^$\n]+?)\$/g;
  let last = 0;
  let m: RegExpExecArray | null;
  while ((m = re.exec(text)) !== null) {
    if (m.index > last) out.push({ kind: "text", body: text.slice(last, m.index) });
    if (m[1] !== undefined) out.push({ kind: "block", body: m[1] });
    else out.push({ kind: "inline", body: m[2] });
    last = m.index + m[0].length;
  }
  if (last < text.length) out.push({ kind: "text", body: text.slice(last) });
  return out;
}

/** Juda cheklangan markdown: **qalin** va yangi qator. HTML kiritilmaydi. */
function Markdownish({ text }: { text: string }) {
  const nodes = useMemo(() => {
    const chunks = text.split(/(\*\*[^*]+\*\*)/g);
    return chunks.map((c, i) =>
      c.startsWith("**") && c.endsWith("**") && c.length > 4
        ? <strong key={i}>{c.slice(2, -2)}</strong>
        : <span key={i} style={{ whiteSpace: "pre-wrap" }}>{c}</span>,
    );
  }, [text]);
  return <>{nodes}</>;
}
