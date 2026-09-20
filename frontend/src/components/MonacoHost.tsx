import Editor, { loader } from "@monaco-editor/react";
import * as monaco from "monaco-editor";
import editorWorker from "monaco-editor/editor/editor.worker?worker";
import { useEffect } from "react";
import type { CodeEditorProps } from "./CodeEditor";

// Monaco'ni O'Z paketimizdan beramiz — CDN'ga chiqmaydi, demak
// internetsiz muhitda ham ishlaydi.
self.MonacoEnvironment = {
  getWorker() {
    return new editorWorker();
  },
};
loader.config({ monaco });

const THEME_LIGHT = "mexanika-light";
const THEME_DARK = "mexanika-dark";

function defineThemes(m: typeof monaco) {
  m.editor.defineTheme(THEME_LIGHT, {
    base: "vs", inherit: true,
    rules: [
      { token: "comment", foreground: "9A968C", fontStyle: "italic" },
      { token: "string", foreground: "2B5A74" },
      { token: "number", foreground: "B2402E" },
      { token: "keyword", foreground: "17191C", fontStyle: "bold" },
    ],
    colors: { "editor.background": "#FFFEFB", "editorLineNumber.foreground": "#9A968C" },
  });
  m.editor.defineTheme(THEME_DARK, {
    base: "vs-dark", inherit: true,
    rules: [
      { token: "comment", foreground: "6D6A63", fontStyle: "italic" },
      { token: "string", foreground: "6AA8CC" },
      { token: "number", foreground: "E2705C" },
      { token: "keyword", foreground: "E8E6E0", fontStyle: "bold" },
    ],
    colors: { "editor.background": "#1E2126", "editorLineNumber.foreground": "#6D6A63" },
  });
}

function prefersDark(): boolean {
  const attr = document.documentElement.getAttribute("data-theme");
  if (attr === "dark") return true;
  if (attr === "light") return false;
  return window.matchMedia?.("(prefers-color-scheme: dark)").matches ?? false;
}

export default function MonacoHost({
  value, onChange, onRun, height = 320, readOnly = false,
  ariaLabel = "Python kodi",
}: CodeEditorProps) {
  useEffect(() => { defineThemes(monaco); }, []);

  return (
    <div style={{ border: "1px solid var(--rule-faint)", borderRadius: "var(--radius)",
                  overflow: "hidden" }}>
      <Editor
        height={height}
        defaultLanguage="python"
        value={value}
        theme={prefersDark() ? THEME_DARK : THEME_LIGHT}
        onChange={(v) => onChange(v ?? "")}
        onMount={(editor, m) => {
          defineThemes(m as unknown as typeof monaco);
          editor.updateOptions({ ariaLabel });
          editor.addCommand(m.KeyMod.CtrlCmd | m.KeyCode.Enter, () => onRun?.());
        }}
        options={{
          readOnly,
          fontSize: 12.5,
          fontFamily: "var(--font-mono), monospace",
          minimap: { enabled: false },
          scrollBeyondLastLine: false,
          lineNumbersMinChars: 3,
          renderLineHighlight: "none",
          tabSize: 4,
          automaticLayout: true,
          padding: { top: 8, bottom: 8 },
        }}
      />
    </div>
  );
}
