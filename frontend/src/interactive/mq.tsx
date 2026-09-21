import { useState } from "react";
import { Choice, Controls, Figure, Hatch, Readout, Slider, path } from "./ui";

type LoadKind = "udl" | "point" | "both";

/** mq-12 — Q va M epyuralari: yuk o'zgarsa epyuralar jonli qayta chiziladi. */
export function BeamDiagrams() {
  const [kind, setKind] = useState<LoadKind>("udl");
  const [q, setQ] = useState(10);        // kN/m
  const [P, setP] = useState(40);        // kN
  const [aRel, setARel] = useState(0.5); // kuch joyi, L ulushi
  const L = 6;                           // m

  const N = 201;
  const xs = Array.from({ length: N }, (_, i) => (i / (N - 1)) * L);
  const a = aRel * L;

  const qq = kind === "point" ? 0 : q;
  const PP = kind === "udl" ? 0 : P;

  // tayanch reaksiyalari (ikki tayanchli balka)
  const RA = (qq * L) / 2 + (PP * (L - a)) / L;
  const RB = (qq * L) / 2 + (PP * a) / L;

  const Q = xs.map((x) => RA - qq * x - (x > a ? PP : 0));
  const M = xs.map((x) => RA * x - (qq * x * x) / 2 - (x > a ? PP * (x - a) : 0));

  const qAbs = Math.max(...Q.map(Math.abs), 1e-9);
  const mMax = Math.max(...M, 1e-9);
  const mMaxAt = xs[M.indexOf(Math.max(...M))];

  const W = 720, H = 430;
  const x0 = 70, x1 = W - 40;
  const yBeam = 70, yQ = 210, yM = 350;

  return (
    <div>
      <Figure width={W} height={H} label="Kesuvchi kuch va eguvchi moment epyuralari"
              note="Q epyurasi nolni kesgan joyda M maksimumga chiqadi — dM/dx = Q.">
        {/* balka */}
        <line x1={x0} y1={yBeam} x2={x1} y2={yBeam} stroke="var(--ink)" strokeWidth="4" />
        {/* tayanchlar */}
        {[x0, x1].map((X, i) => (
          <g key={i}>
            <polygon points={`${X},${yBeam} ${X - 10},${yBeam + 16} ${X + 10},${yBeam + 16}`}
                     fill="none" stroke="var(--ink)" strokeWidth="1.8" />
            <line x1={X - 13} y1={yBeam + 16} x2={X + 13} y2={yBeam + 16}
                  stroke="var(--rule)" strokeWidth="1.6" />
          </g>
        ))}
        {/* taqsimlangan yuk */}
        {qq > 0 && (
          <g>
            <line x1={x0} y1={yBeam - 34} x2={x1} y2={yBeam - 34}
                  stroke="var(--compress)" strokeWidth="1.6" />
            {Array.from({ length: 11 }, (_, i) => {
              const X = x0 + ((x1 - x0) * i) / 10;
              return <line key={i} x1={X} y1={yBeam - 34} x2={X} y2={yBeam - 6}
                           stroke="var(--compress)" strokeWidth="1.6" />;
            })}
            <text x={x0 + 6} y={yBeam - 40} fontSize="12" fill="var(--compress)"
                  fontFamily="var(--font-mono)">q = {qq} kN/m</text>
          </g>
        )}
        {/* to'plangan kuch */}
        {PP > 0 && (
          <g>
            <line x1={x0 + (x1 - x0) * aRel} y1={yBeam - 52}
                  x2={x0 + (x1 - x0) * aRel} y2={yBeam - 6}
                  stroke="var(--tension)" strokeWidth="3" />
            <polygon points={`${x0 + (x1 - x0) * aRel},${yBeam - 4} ${x0 + (x1 - x0) * aRel - 5},${yBeam - 14} ${x0 + (x1 - x0) * aRel + 5},${yBeam - 14}`}
                     fill="var(--tension)" />
            <text x={x0 + (x1 - x0) * aRel + 8} y={yBeam - 46} fontSize="12"
                  fill="var(--tension)" fontFamily="var(--font-mono)">P = {PP} kN</text>
          </g>
        )}

        <text x={20} y={yQ + 4} fontSize="14" fill="var(--ink)" fontFamily="var(--font-display)">Q</text>
        <Hatch base={{ x0, y0: yQ, x1 }} values={Q} scale={55 / qAbs} n={40} />
        <text x={x0 + 4} y={yQ - 55 * (Q[0] / qAbs) - 6} fontSize="11" fill="var(--tension)"
              fontFamily="var(--font-mono)">{Q[0].toFixed(1)}</text>

        <text x={20} y={yM + 4} fontSize="14" fill="var(--ink)" fontFamily="var(--font-display)">M</text>
        <Hatch base={{ x0, y0: yM, x1 }} values={M} scale={58 / mMax} n={40} />
        <text x={x0 + (x1 - x0) * (mMaxAt / L)} y={yM - 58 - 8} textAnchor="middle"
              fontSize="12" fill="var(--tension)" fontFamily="var(--font-mono)">
          M_max = {mMax.toFixed(1)} kN·m
        </text>
        <line x1={x0 + (x1 - x0) * (mMaxAt / L)} y1={yQ} x2={x0 + (x1 - x0) * (mMaxAt / L)} y2={yM}
              stroke="var(--mark)" strokeWidth="1.2" strokeDasharray="4 4" />
      </Figure>

      <Controls>
        <Choice label="Yuk turi" value={kind} onChange={setKind}
                options={[{ value: "udl", label: "tarqoq q" },
                          { value: "point", label: "to'plangan P" },
                          { value: "both", label: "ikkalasi" }]} />
        {kind !== "point" && (
          <Slider label="Tarqoq yuk q" value={q} min={0} max={30} step={1} unit="kN/m"
                  onChange={setQ} color="var(--compress)" />
        )}
        {kind !== "udl" && (
          <>
            <Slider label="Kuch P" value={P} min={0} max={120} step={5} unit="kN"
                    onChange={setP} />
            <Slider label="Kuch joyi a/L" value={aRel} min={0.05} max={0.95} step={0.01}
                    onChange={setARel} color="var(--mark)" />
          </>
        )}
      </Controls>

      <Readout items={[
        { label: "R_A", value: `${RA.toFixed(1)} kN` },
        { label: "R_B", value: `${RB.toFixed(1)} kN` },
        { label: "M_max", value: `${mMax.toFixed(1)} kN·m`, color: "var(--tension)" },
        { label: "M_max joyi", value: `x = ${mMaxAt.toFixed(2)} m`, color: "var(--mark)" },
        { label: "Muvozanat", value: `ΣR − ΣF = ${(RA + RB - qq * L - PP).toFixed(6)}` },
      ]} />
      <p className="tiny muted" style={{ marginTop: 6 }}>
        Kuch joyini suring: M maksimumi Q epyurasi nolni kesgan joyga ergashadi.
        Muvozanat nazorati har doim nol bo'lib qolishiga e'tibor bering.
      </p>
    </div>
  );
}

/** mq-19 — Mor doirasi: kesim burilganda kuchlanishlar qanday o'zgaradi. */
export function MohrCircle() {
  const [sx, setSx] = useState(120);
  const [sy, setSy] = useState(40);
  const [txy, setTxy] = useState(50);
  const [ang, setAng] = useState(0);

  const c = (sx + sy) / 2;
  const R = Math.hypot((sx - sy) / 2, txy);
  const s1 = c + R, s2 = c - R;
  const tmax = R;
  const thP = (Math.atan2(2 * txy, sx - sy) * 90) / Math.PI; // gradus

  const th = (ang * Math.PI) / 180;
  const sn = c + ((sx - sy) / 2) * Math.cos(2 * th) + txy * Math.sin(2 * th);
  const ts = -((sx - sy) / 2) * Math.sin(2 * th) + txy * Math.cos(2 * th);

  const W = 720, H = 400;
  const cx = 300, cy = 200;
  const k = 120 / Math.max(R, 1e-6) * 0.85;
  const sc = Math.min(k, 1.6);

  const P = (s: number, t: number): [number, number] => [cx + (s - c) * sc, cy - t * sc];
  const [px1, py1] = P(sn, ts);
  const [pxX, pyX] = P(sx, txy);
  const [pxY, pyY] = P(sy, -txy);

  return (
    <div>
      <Figure width={W} height={H} label="Mor doirasi"
              note="Kesim θ ga burilsa, Mor doirasida nuqta 2θ ga buriladi.">
        <line x1={40} y1={cy} x2={W - 200} y2={cy} stroke="var(--ink)" strokeWidth="1.2" />
        <line x1={cx} y1={40} x2={cx} y2={H - 40} stroke="var(--ink)" strokeWidth="1.2" />
        <text x={W - 208} y={cy - 8} fontSize="12" fill="var(--ink-soft)" fontFamily="var(--font-mono)">σ</text>
        <text x={cx + 8} y={48} fontSize="12" fill="var(--ink-soft)" fontFamily="var(--font-mono)">τ</text>

        <circle cx={cx} cy={cy} r={R * sc} fill="none" stroke="var(--ink)" strokeWidth="2.2" />
        <circle cx={cx} cy={cy} r="3.5" fill="var(--rule)" />

        <line x1={pxX} y1={pyX} x2={pxY} y2={pyY} stroke="var(--rule-faint)" strokeWidth="1.6" />
        <circle cx={pxX} cy={pyX} r="4" fill="var(--rule)" />
        <circle cx={pxY} cy={pyY} r="4" fill="var(--rule)" />

        <line x1={cx} y1={cy} x2={px1} y2={py1} stroke="var(--compress)" strokeWidth="2.4" />
        <circle cx={px1} cy={py1} r="6" fill="var(--compress)" />
        <text x={px1 + 9} y={py1 - 8} fontSize="12" fill="var(--compress)"
              fontFamily="var(--font-mono)">({sn.toFixed(0)}, {ts.toFixed(0)})</text>

        <circle cx={cx + (s1 - c) * sc} cy={cy} r="5" fill="var(--tension)" />
        <circle cx={cx + (s2 - c) * sc} cy={cy} r="5" fill="var(--compress)" />
        <text x={cx + (s1 - c) * sc} y={cy + 20} textAnchor="middle" fontSize="11"
              fill="var(--tension)" fontFamily="var(--font-mono)">σ₁={s1.toFixed(0)}</text>
        <text x={cx + (s2 - c) * sc} y={cy + 20} textAnchor="middle" fontSize="11"
              fill="var(--compress)" fontFamily="var(--font-mono)">σ₂={s2.toFixed(0)}</text>
        <circle cx={cx} cy={cy - R * sc} r="4.5" fill="var(--mark)" />
        <text x={cx + 8} y={cy - R * sc - 8} fontSize="11" fill="var(--mark)"
              fontFamily="var(--font-mono)">τ_max={tmax.toFixed(0)}</text>

        {/* burilgan element */}
        <g transform={`translate(${W - 130} ${cy}) rotate(${-ang})`}>
          <rect x={-42} y={-42} width={84} height={84} fill="var(--paper)"
                stroke="var(--ink)" strokeWidth="1.8" />
          <line x1={46} y1={0} x2={46 + Math.min(Math.abs(sn) * 0.28, 46) * Math.sign(sn)} y2={0}
                stroke="var(--tension)" strokeWidth="3" />
          <line x1={-46} y1={0} x2={-46 - Math.min(Math.abs(sn) * 0.28, 46) * Math.sign(sn)} y2={0}
                stroke="var(--tension)" strokeWidth="3" />
          <line x1={42} y1={-6} x2={42} y2={-6 - Math.min(Math.abs(ts) * 0.3, 34) * Math.sign(ts)}
                stroke="var(--compress)" strokeWidth="2.6" />
        </g>
        <text x={W - 130} y={cy + 76} textAnchor="middle" fontSize="11" fill="var(--ink-soft)"
              fontFamily="var(--font-mono)">kesim θ = {ang}°</text>
      </Figure>

      <Controls>
        <Slider label="σₓ" value={sx} min={-150} max={250} step={5} unit="MPa" onChange={setSx} />
        <Slider label="σᵧ" value={sy} min={-150} max={250} step={5} unit="MPa" onChange={setSy}
                color="var(--compress)" />
        <Slider label="τₓᵧ" value={txy} min={-120} max={120} step={5} unit="MPa" onChange={setTxy}
                color="var(--mark)" />
        <Slider label="Kesim burchagi θ" value={ang} min={0} max={180} step={1} unit="°"
                onChange={setAng} color="var(--compress)" />
      </Controls>

      <Readout items={[
        { label: "σ₁", value: `${s1.toFixed(1)} MPa`, color: "var(--tension)" },
        { label: "σ₂", value: `${s2.toFixed(1)} MPa`, color: "var(--compress)" },
        { label: "τ_max", value: `${tmax.toFixed(1)} MPa`, color: "var(--mark)" },
        { label: "Bosh o'q burchagi", value: `${thP.toFixed(1)}°` },
        { label: "Invariant σₓ+σᵧ", value: (sx + sy).toFixed(1) },
      ]} />
      <p className="tiny muted" style={{ marginTop: 6 }}>
        θ ni bosh o'q burchagiga tenglang — urinma kuchlanish nolga aylanadi.
        σₓ+σᵧ yig'indisi burchakdan qat'i nazar o'zgarmasligiga e'tibor bering.
      </p>
    </div>
  );
}

/** mq-25 — Eyler ustuvorligi: mahkamlash usuli kritik kuchni qanday belgilaydi. */
export function EulerBuckling() {
  const [mu, setMu] = useState(1.0);
  const [Lm, setLm] = useState(3.0);
  const [d, setD] = useState(60);

  const E = 210e9;
  const I = (Math.PI * (d / 1000) ** 4) / 64;
  const A = (Math.PI * (d / 1000) ** 2) / 4;
  const i = Math.sqrt(I / A);
  const lam = (mu * Lm) / i;
  const Pcr = (Math.PI ** 2 * E * I) / (mu * Lm) ** 2 / 1000; // kN
  const sCr = (Pcr * 1000) / A / 1e6;                          // MPa
  const lamLim = Math.PI * Math.sqrt(E / 200e6);

  const W = 720, H = 380;
  const names: Record<string, string> = {
    "0.5": "ikki uchi qisilgan", "0.7": "qisilgan–sharnirli",
    "1": "ikki uchi sharnirli", "2": "konsol",
  };
  const key = String(mu);

  const shape = (): [number, number][] => {
    const pts: [number, number][] = [];
    const base = H - 60, top = 60, cxx = 200;
    for (let k = 0; k <= 120; k += 1) {
      const t = k / 120;
      const y = base - (base - top) * t;
      let dx: number;
      if (mu === 2) dx = 34 * (1 - Math.cos((Math.PI * t) / 2));
      else if (mu === 0.5) dx = 30 * (1 - Math.cos(2 * Math.PI * t)) / 2;
      else if (mu === 0.7) dx = 32 * Math.sin(Math.PI * t) * (1 - 0.35 * t);
      else dx = 34 * Math.sin(Math.PI * t);
      pts.push([cxx + dx, y]);
    }
    return pts;
  };

  return (
    <div>
      <Figure width={W} height={H} label="Eyler ustuvorligi va keltirilgan uzunlik"
              note="μ — keltirilgan uzunlik koeffitsienti: mahkamlash usuliga bog'liq.">
        <line x1={200} y1={H - 60} x2={200} y2={60} stroke="var(--rule-faint)"
              strokeWidth="1.4" strokeDasharray="5 4" />
        <path d={path(shape())} fill="none" stroke="var(--tension)" strokeWidth="3.4" />
        <line x1={150} y1={H - 44} x2={250} y2={H - 44} stroke="var(--ink)" strokeWidth="3" />
        <line x1={175} y1={44} x2={225} y2={44} stroke="var(--compress)" strokeWidth="3" />
        <polygon points="200,58 194,44 206,44" fill="var(--compress)" />
        <text x={200} y={34} textAnchor="middle" fontSize="13" fill="var(--compress)"
              fontFamily="var(--font-mono)">P</text>
        <text x={200} y={H - 24} textAnchor="middle" fontSize="12" fill="var(--ink-soft)"
              fontFamily="var(--font-display)">{names[key] ?? ""}</text>

        {/* lambda o'qi */}
        <line x1={360} y1={H - 80} x2={W - 40} y2={H - 80} stroke="var(--ink)" strokeWidth="1.2" />
        <line x1={360} y1={H - 80} x2={360} y2={70} stroke="var(--ink)" strokeWidth="1.2" />
        <text x={(360 + W - 40) / 2} y={H - 52} textAnchor="middle" fontSize="11"
              fill="var(--ink-soft)" fontFamily="var(--font-display)">moslashuvchanlik λ</text>
        <text x={344} y={72} textAnchor="end" fontSize="11" fill="var(--ink-soft)"
              fontFamily="var(--font-display)">σ_cr</text>
        {(() => {
          const pts: [number, number][] = [];
          for (let l = 20; l <= 220; l += 2) {
            const s = Math.min((Math.PI ** 2 * E) / (l * l) / 1e6, 260);
            pts.push([360 + ((l - 20) / 200) * (W - 400), H - 80 - (s / 260) * (H - 160)]);
          }
          return <path d={path(pts)} fill="none" stroke="var(--tension)" strokeWidth="2.4" />;
        })()}
        <line x1={360 + ((lamLim - 20) / 200) * (W - 400)} y1={70}
              x2={360 + ((lamLim - 20) / 200) * (W - 400)} y2={H - 80}
              stroke="var(--mark)" strokeWidth="1.4" strokeDasharray="4 4" />
        <text x={360 + ((lamLim - 20) / 200) * (W - 400) + 5} y={88} fontSize="10"
              fill="var(--mark)" fontFamily="var(--font-mono)">λ_lim={lamLim.toFixed(0)}</text>
        {lam >= 20 && lam <= 220 && (
          <circle cx={360 + ((lam - 20) / 200) * (W - 400)}
                  cy={H - 80 - (Math.min(sCr, 260) / 260) * (H - 160)} r="5.5"
                  fill="var(--compress)" />
        )}
      </Figure>

      <Controls>
        <Choice label="Mahkamlash" value={key as never} onChange={(v) => setMu(Number(v))}
                options={[{ value: "0.5" as never, label: "μ=0,5" },
                          { value: "0.7" as never, label: "μ=0,7" },
                          { value: "1" as never, label: "μ=1,0" },
                          { value: "2" as never, label: "μ=2,0" }]} />
        <Slider label="Uzunlik L" value={Lm} min={0.5} max={6} step={0.1} unit="m" onChange={setLm} />
        <Slider label="Diametr d" value={d} min={20} max={140} step={2} unit="mm"
                onChange={setD} color="var(--compress)" />
      </Controls>

      <Readout items={[
        { label: "P_cr", value: `${Pcr.toFixed(1)} kN`, color: "var(--tension)" },
        { label: "σ_cr", value: `${sCr.toFixed(0)} MPa` },
        { label: "λ", value: lam.toFixed(0), color: "var(--compress)" },
        { label: "Rejim", value: lam > lamLim ? "Eyler o'rinli" : "Eyler O'RINSIZ (qisqa sterjen)",
          color: lam > lamLim ? "var(--compress)" : "var(--tension)" },
      ]} />
      <p className="tiny muted" style={{ marginTop: 6 }}>
        μ ni 2,0 dan 0,5 ga o'zgartiring: kritik kuch 16 barobar oshadi, chunki
        u (μL)² ga teskari proporsional. λ &lt; λ_lim bo'lsa Eyler formulasi yaroqsiz.
      </p>
    </div>
  );
}
