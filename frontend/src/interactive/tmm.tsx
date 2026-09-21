import { useState } from "react";
import { Controls, Figure, Readout, Slider, path } from "./ui";

/** tmm-02 — Tenzorning koordinata almashtirishi: komponentalar o'zgaradi, invariantlar yo'q. */
export function TensorTransform() {
  const [sx, setSx] = useState(120);
  const [sy, setSy] = useState(40);
  const [txy, setTxy] = useState(50);
  const [ang, setAng] = useState(20);

  const th = (ang * Math.PI) / 180;
  const c = Math.cos(th), s = Math.sin(th);
  // s' = Q s Qᵀ
  const sxp = sx * c * c + sy * s * s + 2 * txy * s * c;
  const syp = sx * s * s + sy * c * c - 2 * txy * s * c;
  const txyp = (sy - sx) * s * c + txy * (c * c - s * s);

  const I1 = sx + sy;
  const I2 = sx * sy - txy * txy;
  const I1p = sxp + syp;
  const I2p = sxp * syp - txyp * txyp;
  const thP = (Math.atan2(2 * txy, sx - sy) * 90) / Math.PI;

  const W = 720, H = 380;
  const cx = 250, cy = 190, a = 78;

  const arrow = (dx: number, dy: number, mag: number, color: string, key: string) => {
    const len = Math.max(Math.min(Math.abs(mag) * 0.3, 60), 4) * Math.sign(mag || 1);
    return (
      <line key={key} x1={cx + dx * a} y1={cy + dy * a}
            x2={cx + dx * (a + len)} y2={cy + dy * (a + len)}
            stroke={color} strokeWidth="3" />
    );
  };

  return (
    <div>
      <Figure width={W} height={H} label="Tenzorning koordinata almashtirishda o'zgarishi"
              note="Elementni buring — komponentalar o'zgaradi, I₁ va I₂ esa o'zgarmaydi.">
        {/* boshlang'ich element */}
        <g opacity="0.28">
          <rect x={cx - a} y={cy - a} width={2 * a} height={2 * a}
                fill="none" stroke="var(--rule)" strokeWidth="1.6" strokeDasharray="5 4" />
        </g>
        {/* burilgan element */}
        <g transform={`rotate(${-ang} ${cx} ${cy})`}>
          <rect x={cx - a} y={cy - a} width={2 * a} height={2 * a}
                fill="var(--paper)" fillOpacity="0.55" stroke="var(--ink)" strokeWidth="2" />
          {arrow(1, 0, sxp, "var(--tension)", "r")}
          {arrow(-1, 0, sxp, "var(--tension)", "l")}
          {arrow(0, -1, syp, "var(--compress)", "t")}
          {arrow(0, 1, syp, "var(--compress)", "b")}
          <line x1={cx + a} y1={cy - a * 0.55} x2={cx + a} y2={cy - a * 0.55 - Math.min(Math.abs(txyp) * 0.3, 40) * Math.sign(txyp || 1)}
                stroke="var(--mark)" strokeWidth="2.6" />
          <line x1={cx - a} y1={cy + a * 0.55} x2={cx - a} y2={cy + a * 0.55 + Math.min(Math.abs(txyp) * 0.3, 40) * Math.sign(txyp || 1)}
                stroke="var(--mark)" strokeWidth="2.6" />
        </g>
        <text x={cx} y={cy + a + 52} textAnchor="middle" fontSize="12" fill="var(--ink-soft)"
              fontFamily="var(--font-mono)">θ = {ang}°</text>

        {/* matritsa */}
        <g fontFamily="var(--font-mono)" fontSize="14">
          <text x={470} y={110} fill="var(--ink-soft)" fontSize="11">σ′ (burilgan kadr)</text>
          <text x={470} y={140} fill="var(--tension)">σ′ₓₓ = {sxp.toFixed(1)}</text>
          <text x={470} y={166} fill="var(--compress)">σ′ᵧᵧ = {syp.toFixed(1)}</text>
          <text x={470} y={192} fill={Math.abs(txyp) < 0.5 ? "var(--tension)" : "var(--mark)"}>
            σ′ₓᵧ = {txyp.toFixed(2)}
          </text>
          <line x1={470} y1={208} x2={690} y2={208} stroke="var(--rule-faint)" strokeWidth="1" />
          <text x={470} y={232} fill="var(--ink-soft)" fontSize="11">Invariantlar</text>
          <text x={470} y={256} fill="var(--ink)">I₁ = {I1p.toFixed(3)}</text>
          <text x={470} y={280} fill="var(--ink)">I₂ = {I2p.toFixed(1)}</text>
        </g>
      </Figure>

      <Controls>
        <Slider label="σₓ" value={sx} min={-100} max={250} step={5} unit="MPa" onChange={setSx} />
        <Slider label="σᵧ" value={sy} min={-100} max={250} step={5} unit="MPa" onChange={setSy}
                color="var(--compress)" />
        <Slider label="σₓᵧ" value={txy} min={-120} max={120} step={5} unit="MPa" onChange={setTxy}
                color="var(--mark)" />
        <Slider label="Burilish θ" value={ang} min={0} max={180} step={1} unit="°" onChange={setAng} />
      </Controls>

      <Readout items={[
        { label: "I₁ boshlang'ich", value: I1.toFixed(3) },
        { label: "I₁ burilgan", value: I1p.toFixed(3), color: "var(--compress)" },
        { label: "I₂ farqi", value: Math.abs(I2 - I2p).toExponential(1), color: "var(--compress)" },
        { label: "Bosh o'q", value: `θ = ${thP.toFixed(1)}°`, color: "var(--tension)" },
      ]} />
      <p className="tiny muted" style={{ marginTop: 6 }}>
        θ ni bosh o'q burchagiga tenglang — σ′ₓᵧ nolga aylanadi. Invariantlar
        esa har qanday burchakda bir xil qoladi: tenzorning ta'rifi shunda.
      </p>
    </div>
  );
}

/** tmm-21 — Mizes va Treska: qaysi mezon oldin oqadi. */
export function YieldSurfaces() {
  const [s1, setS1] = useState(180);
  const [s2, setS2] = useState(-60);
  const [sy, setSy] = useState(250);

  const vm = Math.sqrt(s1 * s1 - s1 * s2 + s2 * s2);
  const tresca = Math.max(Math.abs(s1), Math.abs(s2), Math.abs(s1 - s2));
  const nVM = sy / vm;
  const nTr = sy / tresca;

  const W = 720, H = 400;
  const cx = 250, cy = 200, k = 150 / sy;

  // Mizes ellipsi: s1^2 - s1 s2 + s2^2 = sy^2
  const mises: [number, number][] = [];
  for (let i = 0; i <= 240; i += 1) {
    const t = (i / 240) * 2 * Math.PI;
    // parametrik: bosh o'qlarda 45° ga burilgan ellips
    const u = Math.cos(t) * Math.SQRT2, v = Math.sin(t) * Math.sqrt(2 / 3);
    const a1 = ((u + v) / 2) * sy, a2 = ((u - v) / 2) * sy;
    mises.push([cx + a1 * k, cy - a2 * k]);
  }
  const hex: [number, number][] = [[1, 0], [1, 1], [0, 1], [-1, 0], [-1, -1], [0, -1], [1, 0]]
    .map(([u, v]) => [cx + u * sy * k, cy - v * sy * k]);

  return (
    <div>
      <Figure width={W} height={H} label="Mizes va Treska oqish yuzalari"
              note="Treska (ko'k olti burchak) har doim Mizes (qizil ellips) ichida — konservativroq.">
        <line x1={40} y1={cy} x2={460} y2={cy} stroke="var(--ink)" strokeWidth="1.2" />
        <line x1={cx} y1={30} x2={cx} y2={H - 30} stroke="var(--ink)" strokeWidth="1.2" />
        <text x={452} y={cy - 8} fontSize="12" fill="var(--ink-soft)" fontFamily="var(--font-mono)">σ₁</text>
        <text x={cx + 8} y={40} fontSize="12" fill="var(--ink-soft)" fontFamily="var(--font-mono)">σ₂</text>

        <path d={path(mises) + "Z"} fill="var(--tension)" fillOpacity="0.07"
              stroke="var(--tension)" strokeWidth="2.4" />
        <path d={path(hex)} fill="var(--compress)" fillOpacity="0.07"
              stroke="var(--compress)" strokeWidth="2.2" />

        <line x1={cx} y1={cy} x2={cx + s1 * k} y2={cy - s2 * k}
              stroke="var(--mark)" strokeWidth="1.6" strokeDasharray="4 3" />
        <circle cx={cx + s1 * k} cy={cy - s2 * k} r="6.5"
                fill={nVM >= 1 ? "var(--compress)" : "var(--tension)"} />

        <g fontFamily="var(--font-mono)" fontSize="13">
          <text x={495} y={95} fill="var(--ink-soft)" fontSize="11">Ekvivalent kuchlanish</text>
          <text x={495} y={124} fill="var(--tension)">Mizes  = {vm.toFixed(1)} MPa</text>
          <text x={495} y={150} fill="var(--compress)">Treska = {tresca.toFixed(1)} MPa</text>
          <line x1={495} y1={166} x2={700} y2={166} stroke="var(--rule-faint)" strokeWidth="1" />
          <text x={495} y={192} fill="var(--ink-soft)" fontSize="11">Zaxira koeffitsienti</text>
          <text x={495} y={220} fill={nVM >= 1 ? "var(--compress)" : "var(--tension)"}>
            n(Mizes)  = {nVM.toFixed(2)}
          </text>
          <text x={495} y={246} fill={nTr >= 1 ? "var(--compress)" : "var(--tension)"}>
            n(Treska) = {nTr.toFixed(2)}
          </text>
          <text x={495} y={284} fill={nTr >= 1 ? "var(--compress)" : "var(--tension)"} fontSize="12">
            {nTr >= 1 ? "elastik" : "PLASTIK OQISH"}
          </text>
        </g>
      </Figure>

      <Controls>
        <Slider label="σ₁" value={s1} min={-350} max={350} step={5} unit="MPa" onChange={setS1} />
        <Slider label="σ₂" value={s2} min={-350} max={350} step={5} unit="MPa" onChange={setS2}
                color="var(--compress)" />
        <Slider label="Oqish chegarasi σᵧ" value={sy} min={120} max={500} step={10} unit="MPa"
                onChange={setSy} color="var(--mark)" />
      </Controls>

      <Readout items={[
        { label: "Mezonlar farqi", value: `${((tresca / vm - 1) * 100).toFixed(1)} %`, color: "var(--mark)" },
        { label: "Sof siljish (σ₁=−σ₂)", value: "farq 15,5 %" },
        { label: "Holat", value: nTr >= 1 ? "elastik" : "oqish boshlandi",
          color: nTr >= 1 ? "var(--compress)" : "var(--tension)" },
      ]} />
      <p className="tiny muted" style={{ marginTop: 6 }}>
        σ₁ = −σ₂ qiling (sof siljish) — farq maksimal 15,5 % ga chiqadi.
        Bir o'qli holatda (σ₂ = 0) ikkala mezon aynan mos tushadi.
      </p>
    </div>
  );
}
