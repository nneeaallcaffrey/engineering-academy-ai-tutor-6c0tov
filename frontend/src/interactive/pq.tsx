import { useState } from "react";
import { Choice, Controls, Figure, Readout, Slider, path } from "./ui";

/** Navye qatori: kvadrat bo'lmagan SSSS plastina uchun w(x,y). */
function navierW(xr: number, yr: number, ab: number, nmax = 11): number {
  let s = 0;
  for (let m = 1; m <= nmax; m += 2) {
    for (let n = 1; n <= nmax; n += 2) {
      const den = m * n * (m * m + (n * n) / (ab * ab)) ** 2;
      s += (Math.sin(m * Math.PI * xr) * Math.sin(n * Math.PI * yr)) / den;
    }
  }
  return (16 / Math.PI ** 6) * s;
}

/** pq-07 — Navye yechimi: plastina egilish sirti va uning tomonlar nisbatiga bog'liqligi. */
export function PlateDeflection() {
  const [ab, setAb] = useState(1.0);   // a/b
  const [h, setH] = useState(8);       // mm
  const [q, setQ] = useState(10);      // kPa
  const [terms, setTerms] = useState(5);

  const a = 1.2, E = 210e9, nu = 0.3;
  const D = (E * (h / 1000) ** 3) / (12 * (1 - nu * nu));
  const alpha = navierW(0.5, 0.5, ab, terms);
  const wmax = (alpha * (q * 1000) * a ** 4) / D * 1000;   // mm
  const alphaExact = navierW(0.5, 0.5, ab, 79);
  const err = Math.abs((alpha - alphaExact) / alphaExact) * 100;

  const W = 720, H = 400;
  const gx = 26, gy = 22;
  const px0 = 60, py0 = 40, pw = 330, ph = 330 / ab;
  const phc = Math.min(ph, 300);

  // kontur: sath chiziqlari o'rniga rang bosqichlari
  const cells: JSX.Element[] = [];
  for (let i = 0; i < gx; i += 1) {
    for (let j = 0; j < gy; j += 1) {
      const xr = (i + 0.5) / gx, yr = (j + 0.5) / gy;
      const v = navierW(xr, yr, ab, terms) / alpha;
      const t = Math.max(0, Math.min(1, v));
      cells.push(
        <rect key={`${i}-${j}`} x={px0 + (i * pw) / gx} y={py0 + (j * phc) / gy}
              width={pw / gx + 0.6} height={phc / gy + 0.6}
              fill="var(--compress)" fillOpacity={0.06 + 0.72 * t} stroke="none" />,
      );
    }
  }

  // kesim profili y = b/2 bo'ylab
  const prof: [number, number][] = [];
  for (let i = 0; i <= 120; i += 1) {
    const xr = i / 120;
    const v = navierW(xr, 0.5, ab, terms) / alpha;
    prof.push([460 + xr * 220, 200 + 70 - v * 70]);
  }

  return (
    <div>
      <Figure width={W} height={H} label="Plastinaning egilish sirti (Navye yechimi)"
              note="Chapda — egilish xaritasi (to'q rang = katta egilish), o'ngda — o'rta kesim profili.">
        {cells}
        <rect x={px0} y={py0} width={pw} height={phc} fill="none" stroke="var(--ink)" strokeWidth="2" />
        <text x={px0 + pw / 2} y={py0 + phc + 22} textAnchor="middle" fontSize="11"
              fill="var(--ink-soft)" fontFamily="var(--font-mono)">a = {a} m</text>
        <text x={px0 - 12} y={py0 + phc / 2} textAnchor="middle" fontSize="11"
              fill="var(--ink-soft)" fontFamily="var(--font-mono)"
              transform={`rotate(-90 ${px0 - 12} ${py0 + phc / 2})`}>b = {(a / ab).toFixed(2)} m</text>
        <circle cx={px0 + pw / 2} cy={py0 + phc / 2} r="5" fill="var(--tension)" />

        <line x1={460} y1={270} x2={690} y2={270} stroke="var(--rule)" strokeWidth="1.2" />
        <path d={path(prof)} fill="none" stroke="var(--tension)" strokeWidth="2.8" />
        <text x={575} y={300} textAnchor="middle" fontSize="11" fill="var(--ink-soft)"
              fontFamily="var(--font-display)">o'rta kesim w(x, b/2)</text>
        <text x={460} y={120} fontSize="12" fill="var(--tension)" fontFamily="var(--font-mono)">
          w_max = {wmax.toFixed(3)} mm
        </text>
        <text x={460} y={144} fontSize="12" fill="var(--ink)" fontFamily="var(--font-mono)">
          α = {alpha.toFixed(6)}
        </text>
        <text x={460} y={168} fontSize="11" fill="var(--mark)" fontFamily="var(--font-mono)">
          qator xatosi: {err.toFixed(3)} %
        </text>
      </Figure>

      <Controls>
        <Slider label="Tomonlar nisbati a/b" value={ab} min={0.4} max={2.5} step={0.05}
                onChange={setAb} />
        <Slider label="Qalinlik h" value={h} min={3} max={25} step={0.5} unit="mm"
                onChange={setH} color="var(--compress)" />
        <Slider label="Yuk q" value={q} min={1} max={40} step={1} unit="kPa" onChange={setQ} />
        <Slider label="Qator hadlari (m,n ≤)" value={terms} min={1} max={19} step={2}
                onChange={setTerms} color="var(--mark)" />
      </Controls>

      <Readout items={[
        { label: "w_max", value: `${wmax.toFixed(3)} mm`, color: "var(--tension)" },
        { label: "D", value: `${D.toFixed(1)} N·m` },
        { label: "w/h", value: (wmax / h).toFixed(3),
          color: wmax / h > 0.2 ? "var(--tension)" : "var(--compress)" },
        { label: "Kirxhoff o'rinlimi", value: wmax / h < 0.2 ? "ha" : "YO'Q (katta siljish)",
          color: wmax / h < 0.2 ? "var(--compress)" : "var(--tension)" },
      ]} />
      <p className="tiny muted" style={{ marginTop: 6 }}>
        Hadlar sonini 1 ga tushiring — xato atigi 2,4 %. Qalinlikni kamaytiring:
        w/h &gt; 0,2 bo'lganda Kirxhoff nazariyasi yaroqsiz bo'lib qoladi.
      </p>
    </div>
  );
}

/** pq-22 — Tebranish shakllari: tugun chiziqlari (Xladni figuralari). */
export function PlateModes() {
  const [m, setM] = useState(2);
  const [n, setN] = useState(1);
  const [ab, setAb] = useState(1.0);

  const W = 720, H = 380;
  const S = 260;
  const px0 = 90, py0 = 55;
  const pw = S, ph = S / ab;
  const phc = Math.min(ph, 280);

  const g = 40;
  const cells: JSX.Element[] = [];
  for (let i = 0; i < g; i += 1) {
    for (let j = 0; j < g; j += 1) {
      const xr = (i + 0.5) / g, yr = (j + 0.5) / g;
      const v = Math.sin(m * Math.PI * xr) * Math.sin(n * Math.PI * yr);
      cells.push(
        <rect key={`${i}-${j}`} x={px0 + (i * pw) / g} y={py0 + (j * phc) / g}
              width={pw / g + 0.5} height={phc / g + 0.5}
              fill={v >= 0 ? "var(--tension)" : "var(--compress)"}
              fillOpacity={0.08 + 0.6 * Math.abs(v)} stroke="none" />,
      );
    }
  }

  const omega = Math.PI ** 2 * (m * m + (n * n) / (ab * ab));
  const om11 = Math.PI ** 2 * (1 + 1 / (ab * ab));

  return (
    <div>
      <Figure width={W} height={H} label="Plastinaning tebranish shakllari va tugun chiziqlari"
              note="Qizil va ko'k sohalar qarama-qarshi tomonga tebranadi; oq chiziqlar — tugunlar.">
        {cells}
        {Array.from({ length: m - 1 }, (_, i) => (
          <line key={`vx${i}`} x1={px0 + (pw * (i + 1)) / m} y1={py0}
                x2={px0 + (pw * (i + 1)) / m} y2={py0 + phc}
                stroke="var(--paper)" strokeWidth="3.4" />
        ))}
        {Array.from({ length: n - 1 }, (_, j) => (
          <line key={`hy${j}`} x1={px0} y1={py0 + (phc * (j + 1)) / n}
                x2={px0 + pw} y2={py0 + (phc * (j + 1)) / n}
                stroke="var(--paper)" strokeWidth="3.4" />
        ))}
        <rect x={px0} y={py0} width={pw} height={phc} fill="none" stroke="var(--ink)" strokeWidth="2" />

        <g fontFamily="var(--font-mono)" fontSize="13">
          <text x={410} y={100} fill="var(--ink-soft)" fontSize="11">Shakl ({m}, {n})</text>
          <text x={410} y={130} fill="var(--ink)">tugun chiziqlari: {(m - 1) + (n - 1)}</text>
          <text x={410} y={158} fill="var(--tension)">ω/ω₁₁ = {(omega / om11).toFixed(3)}</text>
          <text x={410} y={186} fill="var(--ink-soft)" fontSize="11">
            ω = π²(m²/a² + n²/b²)·√(D/ρh)
          </text>
          <line x1={410} y1={206} x2={690} y2={206} stroke="var(--rule-faint)" strokeWidth="1" />
          <text x={410} y={232} fill="var(--ink-soft)" fontSize="11">Kvadrat plastinada (a=b)</text>
          <text x={410} y={258} fill={ab === 1 && m !== n ? "var(--mark)" : "var(--ink)"}>
            (m,n) va (n,m) — {ab === 1 ? "bir xil chastota" : "turli chastota"}
          </text>
        </g>
      </Figure>

      <Controls>
        <Slider label="m (x bo'yicha yarim to'lqin)" value={m} min={1} max={5} step={1}
                onChange={setM} />
        <Slider label="n (y bo'yicha yarim to'lqin)" value={n} min={1} max={5} step={1}
                onChange={setN} color="var(--compress)" />
        <Slider label="Tomonlar nisbati a/b" value={ab} min={0.5} max={2.5} step={0.05}
                onChange={setAb} color="var(--mark)" />
      </Controls>

      <Readout items={[
        { label: "Tugun chiziqlari", value: String((m - 1) + (n - 1)) },
        { label: "Nisbiy chastota", value: (omega / om11).toFixed(3), color: "var(--tension)" },
        { label: "Karrali ildiz", value: ab === 1 && m !== n ? "HA — (n,m) bilan bir xil" : "yo'q",
          color: ab === 1 && m !== n ? "var(--mark)" : "var(--ink)" },
      ]} />
      <p className="tiny muted" style={{ marginTop: 6 }}>
        Kvadrat plastinada (a/b = 1) (2,1) va (1,2) shakllari bir xil chastotaga
        ega — karrali ildiz. Nisbatni ozgina o'zgartiring va ular ajraladi.
      </p>
    </div>
  );
}

/** pq-13 — Doiraviy plastina: qisilgan va sharnirli chetlar taqqoslanadi. */
export function CircularPlate() {
  const [edge, setEdge] = useState<"clamped" | "simple">("clamped");
  const [aMm, setAMm] = useState(250);
  const [h, setH] = useState(12);
  const [p, setP] = useState(0.5);

  const nu = 0.3, E = 210e9;
  const a = aMm / 1000;
  const D = (E * (h / 1000) ** 3) / (12 * (1 - nu * nu));
  const coef = edge === "clamped" ? 1 / 64 : (5 + nu) / (64 * (1 + nu));
  const wmax = (coef * p * 1e6 * a ** 4) / D * 1e6;   // mkm
  const sEdge = edge === "clamped" ? (3 * p * 1e6 * a * a) / (4 * (h / 1000) ** 2) / 1e6 : 0;
  const sCent = edge === "clamped"
    ? (3 * p * 1e6 * a * a * (1 + nu)) / (8 * (h / 1000) ** 2) / 1e6
    : (3 * p * 1e6 * a * a * (3 + nu)) / (8 * (h / 1000) ** 2) / 1e6;
  const ratio = ((5 + nu) / (64 * (1 + nu))) / (1 / 64);

  const W = 720, H = 380;
  const cx = 360, cy = 170, R = 250;

  const shape = (kind: "clamped" | "simple"): [number, number][] => {
    const k0 = (5 + nu) / (1 + nu);
    const pts: [number, number][] = [];
    for (let i = 0; i <= 200; i += 1) {
      const t = -1 + (2 * i) / 200;
      const v = kind === "clamped"
        ? (1 - t * t) ** 2
        : ((1 - t * t) * (k0 - t * t)) / k0;
      const amp = kind === "clamped" ? 1 : ratio;
      pts.push([cx + t * R, cy + 30 + v * amp * 46]);
    }
    return pts;
  };

  return (
    <div>
      <Figure width={W} height={H} label="Doiraviy plastinaning o'qsimmetrik egilishi"
              note="Kulrang — ikkinchi variant, taqqoslash uchun. Egilish 4,08 barobar farq qiladi.">
        <line x1={cx - R} y1={cy + 30} x2={cx + R} y2={cy + 30}
              stroke="var(--rule)" strokeWidth="1.2" strokeDasharray="4 4" />
        {Array.from({ length: 13 }, (_, i) => {
          const X = cx - R * 0.92 + (R * 1.84 * i) / 12;
          return <line key={i} x1={X} y1={cy - 24} x2={X} y2={cy + 24}
                       stroke="var(--compress)" strokeWidth="1.6" />;
        })}
        <text x={cx} y={cy - 34} textAnchor="middle" fontSize="12" fill="var(--compress)"
              fontFamily="var(--font-mono)">p = {p} MPa</text>

        <path d={path(shape(edge === "clamped" ? "simple" : "clamped"))} fill="none"
              stroke="var(--rule-faint)" strokeWidth="2" />
        <path d={path(shape(edge))} fill="none" stroke="var(--tension)" strokeWidth="3.2" />

        {/* chet mahkamlash belgisi */}
        {[cx - R, cx + R].map((X, i) => (
          <g key={i}>
            {edge === "clamped" ? (
              <>
                <line x1={X} y1={cy + 6} x2={X} y2={cy + 56} stroke="var(--ink)" strokeWidth="3" />
                {Array.from({ length: 4 }, (_, k) => (
                  <line key={k} x1={X} y1={cy + 14 + k * 12}
                        x2={X + (i ? 14 : -14)} y2={cy + 24 + k * 12}
                        stroke="var(--rule)" strokeWidth="1.4" />
                ))}
              </>
            ) : (
              <polygon points={`${X},${cy + 30} ${X - 9},${cy + 48} ${X + 9},${cy + 48}`}
                       fill="none" stroke="var(--ink)" strokeWidth="1.8" />
            )}
          </g>
        ))}
        <text x={cx} y={H - 22} textAnchor="middle" fontSize="12" fill="var(--ink-soft)"
              fontFamily="var(--font-display)">
          {edge === "clamped" ? "chetlari qisilgan" : "chetlari sharnirli"}
        </text>
      </Figure>

      <Controls>
        <Choice label="Chet sharti" value={edge} onChange={setEdge}
                options={[{ value: "clamped", label: "qisilgan" },
                          { value: "simple", label: "sharnirli" }]} />
        <Slider label="Radius a" value={aMm} min={80} max={500} step={10} unit="mm"
                onChange={setAMm} />
        <Slider label="Qalinlik h" value={h} min={3} max={30} step={0.5} unit="mm"
                onChange={setH} color="var(--compress)" />
        <Slider label="Bosim p" value={p} min={0.05} max={3} step={0.05} unit="MPa"
                onChange={setP} color="var(--mark)" />
      </Controls>

      <Readout items={[
        { label: "w_max", value: `${wmax.toFixed(1)} mkm`, color: "var(--tension)" },
        { label: "Koeffitsient", value: coef.toFixed(5) },
        { label: "σ markazda", value: `${sCent.toFixed(0)} MPa` },
        ...(edge === "clamped" ? [{ label: "σ chetda", value: `${sEdge.toFixed(0)} MPa`, color: "var(--tension)" }] : []),
        { label: "sharnirli / qisilgan", value: `${ratio.toFixed(3)}×`, color: "var(--mark)" },
      ]} />
      <p className="tiny muted" style={{ marginTop: 6 }}>
        Chet shartini almashtiring: sharnirli plastina qisilganidan 4,08 barobar
        ko'proq egiladi. Qisilganida eng katta kuchlanish CHETDA, sharnirlida — markazda.
      </p>
    </div>
  );
}
