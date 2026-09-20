import { useCallback, useEffect, useRef, useState } from "react";

export interface AsyncState<T> {
  data: T | null;
  loading: boolean;
  error: string | null;
  reload: () => void;
}

/** Ma'lumot yuklash: yuklanish, xato va qayta urinish bitta joyda. */
export function useAsync<T>(fn: () => Promise<T>, deps: unknown[]): AsyncState<T> {
  const [data, setData] = useState<T | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [tick, setTick] = useState(0);
  const alive = useRef(true);

  useEffect(() => {
    alive.current = true;
    setLoading(true);
    setError(null);
    fn()
      .then((d) => { if (alive.current) setData(d); })
      .catch((e: unknown) => {
        if (alive.current) {
          setError(e instanceof Error ? e.message : "Noma'lum xatolik");
        }
      })
      .finally(() => { if (alive.current) setLoading(false); });
    return () => { alive.current = false; };
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [...deps, tick]);

  const reload = useCallback(() => setTick((t) => t + 1), []);
  return { data, loading, error, reload };
}
