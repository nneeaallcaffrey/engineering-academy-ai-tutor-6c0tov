import { useCallback, useEffect, useState } from "react";

const KEY = "mexanika:progress:v1";

type Progress = Record<string, { done: boolean; quiz?: number }>;

function read(): Progress {
  // localStorage maxfiy rejimda yoki bloklanganda xato beradi —
  // bu holda progress shunchaki bo'sh bo'ladi, interfeys ishlayveradi.
  try {
    const raw = localStorage.getItem(KEY);
    return raw ? (JSON.parse(raw) as Progress) : {};
  } catch {
    return {};
  }
}

function write(p: Progress): void {
  try {
    localStorage.setItem(KEY, JSON.stringify(p));
  } catch { /* saqlab bo'lmadi — bu halokatli emas */ }
}

/** Mavzuni o'zlashtirish holati (faqat shu brauzerda saqlanadi). */
export function useProgress() {
  const [progress, setProgress] = useState<Progress>(read);

  useEffect(() => {
    const onStorage = (e: StorageEvent) => {
      if (e.key === KEY) setProgress(read());
    };
    window.addEventListener("storage", onStorage);
    return () => window.removeEventListener("storage", onStorage);
  }, []);

  const setDone = useCallback((id: string, done: boolean) => {
    setProgress((prev) => {
      const next = { ...prev, [id]: { ...prev[id], done } };
      write(next);
      return next;
    });
  }, []);

  const setQuizScore = useCallback((id: string, score: number) => {
    setProgress((prev) => {
      const next = { ...prev, [id]: { ...prev[id], done: prev[id]?.done ?? false, quiz: score } };
      write(next);
      return next;
    });
  }, []);

  const isDone = useCallback((id: string) => Boolean(progress[id]?.done), [progress]);

  const countDone = useCallback(
    (ids: string[]) => ids.reduce((n, id) => n + (progress[id]?.done ? 1 : 0), 0),
    [progress],
  );

  const reset = useCallback(() => { write({}); setProgress({}); }, []);

  return { progress, isDone, setDone, setQuizScore, countDone, reset };
}
