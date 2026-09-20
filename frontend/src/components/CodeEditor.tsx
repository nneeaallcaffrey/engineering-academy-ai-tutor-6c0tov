import { Suspense, lazy, useRef, useState } from "react";

/**
 * Kod muharriri.
 *
 * Monaco O'ZIMIZNING paketimizdan yuklanadi (CDN emas), shuning uchun u
 * internetsiz Docker muhitida ham ishlaydi. Agar u baribir yuklanmasa
 * (eski brauzer, bloklangan worker), muharrir jonli `textarea` variantiga
 * o'tadi: u ham qator raqamlari, Tab bilan chekinish va Ctrl+Enter ni
 * qo'llab-quvvatlaydi. Ya'ni ikkala yo'l ham ISHLAYDI.
 */
const MonacoEditor = lazy(() => import("./MonacoHost"));

export interface CodeEditorProps {
  value: string;
  onChange: (next: string) => void;
  onRun?: () => void;
  height?: number;
  readOnly?: boolean;
  ariaLabel?: string;
}

export function CodeEditor(props: CodeEditorProps) {
  const [monacoFailed, setMonacoFailed] = useState(false);

  if (monacoFailed) return <PlainEditor {...props} />;

  return (
    <ErrorBoundary onError={() => setMonacoFailed(true)}
                   fallback={<PlainEditor {...props} />}>
      <Suspense fallback={<PlainEditor {...props} />}>
        <MonacoEditor {...props} />
      </Suspense>
    </ErrorBoundary>
  );
}

/** Monaco'siz ham to'liq ishlaydigan muharrir. */
export function PlainEditor({
  value, onChange, onRun, height = 320, readOnly = false,
  ariaLabel = "Python kodi",
}: CodeEditorProps) {
  const ref = useRef<HTMLTextAreaElement>(null);
  const gutter = useRef<HTMLDivElement>(null);
  const lines = value.split("\n").length;

  const onKeyDown = (e: React.KeyboardEvent<HTMLTextAreaElement>) => {
    if ((e.ctrlKey || e.metaKey) && e.key === "Enter") {
      e.preventDefault();
      onRun?.();
      return;
    }
    if (e.key === "Tab") {
      e.preventDefault();
      const el = e.currentTarget;
      const { selectionStart: a, selectionEnd: b } = el;
      const next = `${value.slice(0, a)}    ${value.slice(b)}`;
      onChange(next);
      requestAnimationFrame(() => el.setSelectionRange(a + 4, a + 4));
    }
  };

  return (
    <div style={{ display: "flex", border: "1px solid var(--rule-faint)",
                  background: "var(--surface)", borderRadius: "var(--radius)" }}>
      <div ref={gutter} aria-hidden="true"
           style={{
             padding: "8px 6px 8px 8px", textAlign: "right",
             fontFamily: "var(--font-mono)", fontSize: 12.5, lineHeight: "1.55",
             color: "var(--rule)", background: "var(--paper)",
             borderRight: "1px solid var(--rule-faint)", userSelect: "none",
             minWidth: 38, overflow: "hidden", height,
           }}>
        {Array.from({ length: lines }, (_, i) => <div key={i}>{i + 1}</div>)}
      </div>
      <textarea
        ref={ref}
        value={value}
        readOnly={readOnly}
        aria-label={ariaLabel}
        spellCheck={false}
        onChange={(e) => onChange(e.target.value)}
        onKeyDown={onKeyDown}
        onScroll={(e) => {
          if (gutter.current) gutter.current.scrollTop = e.currentTarget.scrollTop;
        }}
        style={{
          flex: 1, height, padding: "8px 10px", border: "none", resize: "vertical",
          fontFamily: "var(--font-mono)", fontSize: 12.5, lineHeight: "1.55",
          color: "var(--ink)", background: "transparent", outline: "none",
          whiteSpace: "pre", overflowWrap: "normal", overflowX: "auto", tabSize: 4,
        }}
      />
    </div>
  );
}

/* --- Monaco yuklanmasa ushlab qoladigan chegara --- */
import { Component, type ErrorInfo, type ReactNode } from "react";

class ErrorBoundary extends Component<
  { children: ReactNode; fallback: ReactNode; onError: () => void },
  { failed: boolean }
> {
  state = { failed: false };

  static getDerivedStateFromError() {
    return { failed: true };
  }

  componentDidCatch(_e: Error, _info: ErrorInfo) {
    this.props.onError();
  }

  render() {
    return this.state.failed ? this.props.fallback : this.props.children;
  }
}
