import { useState } from "react";
import { Axes, Choice, Controls, Figure, Readout, Slider, path } from "./ui";

/** nm-01 — Vektor ko'paytma va moment: yelka o'zgarsa moment qanday o'zgaradi. */
export function VectorMoment() {
  const [r, setR] = useState(3.2);          // yelka uzunligi, m
  const [ang, setAng] = useState(35);       // kuch burchagi, gradus
  const [F, setF] = useState(120);          // kuch, N

  const W = 720, H = 380;
  const O = { x: 150, y: 250 };             // tayanch nuqtasi
  const px = 52;                            // 1 m = 52 px
  const tip = { x: O.x + r * px, y: O.y };

  const th = (ang * Math.PI) / 180;
  const fx = Math.cos(th), fy = -Math.sin(th);
  const flen = 78;
  const fend = { x: tip.x + fx * flen, y: tip.y + fy * flen };

  // M = r x F  (z komponenta); yelka d = r*sin(th)
  const M = r * F * Math.sin(th);
  const d = r * Math.sin(th);

  // Perpendikulyar yelka: O ni kuchning ta'sir chizig'iga proyeksiyalaymiz.
  const ux = fx, uy = fy;
  const wx = O.x - tip.x, wy = O.y - tip.y;
  const proj = wx * ux + wy * uy;
  const foot2 = { x: tip.x + ux * proj, y: tip.y + uy * proj };

  return (
    <div>
      <Figure width={W} height={H} label="Vektor moment: yelka va kuch burchagi"
              note="Yelka d — tayanchdan kuch ta'sir chizig'igacha bo'lgan perpendikulyar masofa.">
        {/* ta'sir chizig'i */}
        <line x1={tip.x - ux * 400} y1={tip.y - uy * 400}
              x2={tip.x + ux * 400} y2={tip.y + uy * 400}
              stroke="var(--rule-faint)" strokeWidth="1" strokeDasharray="4 4" />
        {/* yelka vektori r */}
        <line x1={O.x} y1={O.y} x2={tip.x} y2={tip.y} stroke="var(--rule)" strokeWidth="3" />
        <text x={(O.x + tip.x) / 2} y={O.y + 20} textAnchor="middle" fontSize="13"
              fill="var(--rule)" fontFamily="var(--font-mono)">r = {r.toFixed(2)} m</text>
        {/* perpendikulyar yelka d */}
        <line x1={O.x} y1={O.y} x2={foot2.x} y2={foot2.y}
              stroke="var(--mark)" strokeWidth="2" strokeDasharray="5 3" />
        <text x={(O.x + foot2.x) / 2 - 6} y={(O.y + foot2.y) / 2 - 8} fontSize="12"
              fill="var(--mark)" fontFamily="var(--font-mono)">d = {d.toFixed(2)} m</text>
        {/* kuch F */}
        <defs>
          <marker id="nm-arrow" markerWidth="9" markerHeight="7" refX="8" refY="3.5" orient="auto">
            <polygon points="0 0, 9 3.5, 0 7" fill="var(--tension)" />
          </marker>
        </defs>
        <line x1={tip.x} y1={tip.y} x2={fend.x} y2={fend.y} stroke="var(--tension)"
              strokeWidth="3.4" markerEnd="url(#nm-arrow)" />
        <text x={fend.x + 10} y={fend.y} fontSize="13" fill="var(--tension)"
              fontFamily="var(--font-mono)">F = {F} N</text>
        {/* parallelogramm — |r x F| yuzasi */}
        <path d={path([[O.x, O.y], [tip.x, tip.y], [fend.x, fend.y],
                       [O.x + (fend.x - tip.x), O.y + (fend.y - tip.y)]])} 
              fill="var(--tension)" fillOpacity="0.12" stroke="var(--tension)"
              strokeWidth="1" strokeDasharray="3 3" />
        {/* tayanch */}
        <circle cx={O.x} cy={O.y} r="6" fill="var(--ink)" />
        <text x={O.x - 6} y={O.y + 26} fontSize="13" fill="var(--ink)"
              fontFamily="var(--font-display)">O</text>
        {/* moment yoyi */}
        <path d={`M ${O.x + 40} ${O.y} A 40 40 0 0 ${M >= 0 ? 0 : 1} ${O.x + 40 * Math.cos(0.9)} ${O.y - 40 * Math.sin(0.9) * (M >= 0 ? 1 : -1)}`}
              fill="none" stroke="var(--compress)" strokeWidth="2.4" />
        <text x={O.x + 52} y={O.y - 34} fontSize="14" fill="var(--compress)"
              fontFamily="var(--font-mono)">M = {M.toFixed(1)} N·m</text>
      </Figure>

      <Controls>
        <Slider label="Yelka r" value={r} min={0.8} max={5} step={0.1} unit="m"
                onChange={setR} color="var(--rule)" />
        <Slider label="Kuch burchagi" value={ang} min={0} max={180} step={1} unit="°"
                onChange={setAng} />
        <Slider label="Kuch F" value={F} min={20} max={300} step={5} unit="N"
                onChange={setF} color="var(--tension)" />
      </Controls>

      <Readout items={[
        { label: "M = F·d", value: `${M.toFixed(2)} N·m`, color: "var(--compress)" },
        { label: "yelka d = r·sin θ", value: `${d.toFixed(3)} m`, color: "var(--mark)" },
        { label: "θ = 0° yoki 180°", value: M === 0 || Math.abs(M) < 1e-9 ? "moment = 0" : "—" },
      ]} />
      <p className="tiny muted" style={{ marginTop: 6 }}>
        Burchakni 0° ga tushiring: kuch yelka bo'ylab yo'naladi, yelka d nolga
        aylanadi va moment yo'qoladi. Maksimum 90° da.
      </p>
    </div>
  );
}

/** nm-27 — Amplituda-chastota tavsifi: dempfirlash cho'qqini qanday cheklaydi. */
export function Resonance() {
  const [zeta, setZeta] = useState(0.08);
  const [beta, setBeta] = useState(1.0);

  const W = 720, H = 380;
  const L = 70, R = 24, T = 20, B = 52;
  const iw = W - L - R, ih = H - T - B;
  const bMax = 2.6, mMax = 7;

  const X = (b: number) => L + (b / bMax) * iw;
  const Y = (m: number) => T + ih - (Math.min(m, mMax) / mMax) * ih;

  const curve = (z: number): [number, number][] => {
    const out: [number, number][] = [];
    for (let i = 0; i <= 320; i += 1) {
      const b = (i / 320) * bMax;
      const m = 1 / Math.sqrt((1 - b * b) ** 2 + (2 * z * b) ** 2);
      out.push([X(b), Y(m)]);
    }
    return out;
  };

  const Mcur = 1 / Math.sqrt((1 - beta * beta) ** 2 + (2 * zeta * beta) ** 2);
  const peak = zeta < Math.SQRT1_2 ? 1 / (2 * zeta * Math.sqrt(1 - zeta * zeta)) : 1;
  const bPeak = zeta < Math.SQRT1_2 ? Math.sqrt(1 - 2 * zeta * zeta) : 0;
  const phase = (Math.atan2(2 * zeta * beta, 1 - beta * beta) * 180) / Math.PI;

  return (
    <div>
      <Figure width={W} height={H} label="Amplituda-chastota tavsifi"
              note="Kulrang egri chiziqlar — boshqa dempfirlash qiymatlari uchun.">
        <Axes x={L} y={T} w={iw} h={ih} xLabel="β = ω / ωₙ" yLabel="Kuchaytirish M"
              xTicks={[0, 0.5, 1, 1.5, 2, 2.5].map((b) => ({ at: X(b), text: String(b) }))}
              yTicks={[0, 1, 2, 3, 4, 5, 6, 7].map((m) => ({ at: Y(m), text: String(m) }))} />
        {[0.02, 0.05, 0.15, 0.3, 0.7].map((z) => (
          <path key={z} d={path(curve(z))} fill="none" stroke="var(--rule-faint)" strokeWidth="1.4" />
        ))}
        <line x1={X(1)} y1={T} x2={X(1)} y2={T + ih} stroke="var(--mark)"
              strokeWidth="1.4" strokeDasharray="4 4" />
        <path d={path(curve(zeta))} fill="none" stroke="var(--tension)" strokeWidth="2.8" />
        {bPeak > 0 && (
          <circle cx={X(bPeak)} cy={Y(peak)} r="4.5" fill="var(--mark)" />
        )}
        <line x1={X(beta)} y1={T} x2={X(beta)} y2={T + ih} stroke="var(--compress)" strokeWidth="1.4" />
        <circle cx={X(beta)} cy={Y(Mcur)} r="5.5" fill="var(--compress)" />
        <text x={X(beta) + 9} y={Y(Mcur) - 8} fontSize="12" fill="var(--compress)"
              fontFamily="var(--font-mono)">M = {Mcur.toFixed(2)}</text>
      </Figure>

      <Controls>
        <Slider label="Dempfirlash ζ" value={zeta} min={0.01} max={0.8} step={0.01}
                onChange={setZeta} />
        <Slider label="Chastota nisbati β" value={beta} min={0.05} max={2.5} step={0.01}
                onChange={setBeta} color="var(--compress)" />
      </Controls>

      <Readout items={[
        { label: "Joriy kuchaytirish", value: Mcur.toFixed(3), color: "var(--compress)" },
        { label: "Maksimum M", value: peak.toFixed(2), color: "var(--mark)" },
        { label: "Cho'qqi β", value: bPeak > 0 ? bPeak.toFixed(3) : "yo'q" },
        { label: "Faza siljishi", value: `${phase.toFixed(0)}°` },
      ]} />
      <p className="tiny muted" style={{ marginTop: 6 }}>
        ζ ni kamaytiring — cho'qqi 1/(2ζ) kabi o'sadi. ζ &gt; 0,707 da cho'qqi
        umuman yo'qoladi: tizim rezonansga kirmaydi.
      </p>
    </div>
  );
}

/** nm-24 — Mayatnik fazaviy portreti: separatrisa ikki rejimni ajratadi. */
export function PhasePortrait() {
  const [E, setE] = useState(1.2);
  const [mode, setMode] = useState<"one" | "family">("family");

  const W = 720, H = 380;
  const cx = W / 2, cy = H / 2 + 10;
  const sx = 95, sy = 62;

  const orbit = (energy: number): [number, number][][] => {
    const up: [number, number][] = [];
    const dn: [number, number][] = [];
    const lim = energy < 2 ? Math.acos(1 - energy) : Math.PI * 1.15;
    for (let i = 0; i <= 260; i += 1) {
      const th = -lim + (2 * lim * i) / 260;
      const v2 = 2 * (energy - (1 - Math.cos(th)));
      if (v2 < 0) continue;
      const v = Math.sqrt(v2);
      up.push([cx + th * sx, cy - v * sy]);
      dn.push([cx + th * sx, cy + v * sy]);
    }
    return [up, dn];
  };

  const [cu, cd] = orbit(E);
  const closed = E < 2;
  const family = [0.25, 0.7, 1.3, 2.0, 2.8, 3.8];

  return (
    <div>
      <Figure width={W} height={H} label="Mayatnik fazaviy portreti"
              note="Qizil — separatrisa (E = 2). Uning ichida tebranish, tashqarisida to'liq aylanish.">
        <line x1={20} y1={cy} x2={W - 20} y2={cy} stroke="var(--ink)" strokeWidth="1.2" />
        <line x1={cx} y1={24} x2={cx} y2={H - 30} stroke="var(--ink)" strokeWidth="1.2" />
        <text x={W - 34} y={cy - 8} fontSize="12" fill="var(--ink-soft)" fontFamily="var(--font-mono)">θ</text>
        <text x={cx + 8} y={32} fontSize="12" fill="var(--ink-soft)" fontFamily="var(--font-mono)">θ̇</text>

        {mode === "family" && family.map((e) => {
          const [a, b] = orbit(e);
          return (
            <g key={e}>
              <path d={path(a)} fill="none" stroke="var(--rule-faint)" strokeWidth="1.3" />
              <path d={path(b)} fill="none" stroke="var(--rule-faint)" strokeWidth="1.3" />
            </g>
          );
        })}

        {/* separatrisa */}
        {(() => {
          const [a, b] = orbit(1.999);
          return (
            <g>
              <path d={path(a)} fill="none" stroke="var(--tension)" strokeWidth="2.4" />
              <path d={path(b)} fill="none" stroke="var(--tension)" strokeWidth="2.4" />
            </g>
          );
        })()}

        <path d={path(closed ? [...cu, ...[...cd].reverse(), cu[0]] : cu)}
              fill="none" stroke="var(--compress)" strokeWidth="3" />
        {!closed && <path d={path(cd)} fill="none" stroke="var(--compress)" strokeWidth="3" />}

        <circle cx={cx} cy={cy} r="4.5" fill="var(--ink)" />
        <circle cx={cx + Math.PI * sx} cy={cy} r="4.5" fill="var(--tension)" />
        <circle cx={cx - Math.PI * sx} cy={cy} r="4.5" fill="var(--tension)" />
        <text x={cx + Math.PI * sx - 26} y={cy + 22} fontSize="11" fill="var(--tension)"
              fontFamily="var(--font-mono)">egar</text>
        <text x={cx + 8} y={cy + 22} fontSize="11" fill="var(--ink-soft)"
              fontFamily="var(--font-mono)">markaz</text>
      </Figure>

      <Controls>
        <Slider label="To'liq energiya E" value={E} min={0.1} max={4} step={0.05}
                onChange={setE} color="var(--compress)" />
        <Choice label="Ko'rinish" value={mode} onChange={setMode}
                options={[{ value: "family", label: "oila bilan" },
                          { value: "one", label: "faqat bittasi" }]} />
      </Controls>

      <Readout items={[
        { label: "Rejim", value: closed ? "tebranish (yopiq orbita)" : "aylanish (ochiq orbita)",
          color: closed ? "var(--compress)" : "var(--mark)" },
        { label: "Maksimal burchak", value: closed ? `${((Math.acos(1 - E) * 180) / Math.PI).toFixed(0)}°` : "cheksiz" },
        { label: "Separatrisa", value: "E = 2", color: "var(--tension)" },
      ]} />
      <p className="tiny muted" style={{ marginTop: 6 }}>
        E ni 2 ga yaqinlashtiring: orbita separatrisaga yopishadi va davr
        cheksizga intiladi. E &gt; 2 da mayatnik to'liq aylanadi.
      </p>
    </div>
  );
}
