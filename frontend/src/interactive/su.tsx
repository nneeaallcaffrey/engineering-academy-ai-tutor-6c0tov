import { useState } from "react";
import { Axes, Choice, Controls, Figure, Readout, Slider, path, tickFmt } from "./ui";

/** su-10 — Barqarorlik: r = αΔt/h² chegaradan oshsa sxema portlaydi. */
export function FDStability() {
  const [r, setR] = useState(0.35);
  const [steps, setSteps] = useState(40);

  const nx = 21;
  // boshlang'ich shart: eng yomon harmonika (kh = pi) + silliq qism
  let u = Array.from({ length: nx }, (_, i) =>
    Math.sin((Math.PI * i) / (nx - 1)) + 0.35 * Math.sin(Math.PI * i));
  const hist: number[][] = [u.slice()];
  for (let s = 0; s < steps; s += 1) {
    const v = u.slice();
    for (let i = 1; i < nx - 1; i += 1) {
      v[i] = u[i] + r * (u[i + 1] - 2 * u[i] + u[i - 1]);
    }
    v[0] = 0; v[nx - 1] = 0;
    u = v;
    hist.push(u.slice());
  }
  const amp = Math.max(...u.map(Math.abs));
  const G = Math.abs(1 - 4 * r);
  const stable = r <= 0.5;

  const W = 720, H = 380;
  const L = 60, R = 30, T = 30, B = 55;
  const iw = W - L - R, ih = H - T - B;
  const cap = 2.2;
  const X = (i: number) => L + (i / (nx - 1)) * iw;
  const Y = (v: number) => T + ih / 2 - (Math.max(-cap, Math.min(cap, v)) / cap) * (ih / 2);

  return (
    <div>
      <Figure width={W} height={H} label="Ayirma sxemasining barqarorligi"
              note="Kulrang chiziqlar — oraliq qadamlar, qizil — oxirgi qadam.">
        <Axes x={L} y={T} w={iw} h={ih} xLabel="tugun i" yLabel="u"
              yTicks={[-2, -1, 0, 1, 2].map((v) => ({ at: Y(v), text: tickFmt(v) }))} />
        {hist.filter((_, k) => k % Math.max(1, Math.floor(steps / 12)) === 0).map((row, k) => (
          <path key={k} d={path(row.map((v, i) => [X(i), Y(v)] as [number, number]))}
                fill="none" stroke="var(--rule-faint)" strokeWidth="1.2" />
        ))}
        <path d={path(hist[0].map((v, i) => [X(i), Y(v)] as [number, number]))}
              fill="none" stroke="var(--compress)" strokeWidth="2.2" strokeDasharray="5 4" />
        <path d={path(u.map((v, i) => [X(i), Y(v)] as [number, number]))}
              fill="none" stroke={stable ? "var(--tension)" : "var(--tension)"} strokeWidth="3" />
        <text x={L + 8} y={T + 18} fontSize="12" fill="var(--compress)" fontFamily="var(--font-mono)">
          boshlang'ich
        </text>
        <text x={W - R - 8} y={T + 18} textAnchor="end" fontSize="13"
              fill={stable ? "var(--compress)" : "var(--tension)"} fontFamily="var(--font-mono)">
          {stable ? "BARQAROR" : "PORTLADI"}
        </text>
      </Figure>

      <Controls>
        <Slider label="r = αΔt/h²" value={r} min={0.05} max={0.75} step={0.01}
                onChange={setR} color={stable ? "var(--compress)" : "var(--tension)"} />
        <Slider label="Qadamlar soni" value={steps} min={5} max={120} step={5}
                onChange={setSteps} color="var(--mark)" />
      </Controls>

      <Readout items={[
        { label: "Kuchayish |G|", value: G.toFixed(3),
          color: G <= 1 ? "var(--compress)" : "var(--tension)" },
        { label: "Amplituda", value: amp > 1e6 ? amp.toExponential(1) : amp.toFixed(3),
          color: stable ? "var(--compress)" : "var(--tension)" },
        { label: "Shart", value: "r ≤ 0,5", color: "var(--mark)" },
      ]} />
      <p className="tiny muted" style={{ marginTop: 6 }}>
        r ni 0,5 dan sal oshiring — yechim darhol tebranib o'sa boshlaydi.
        Bu aniqlik emas, BARQARORLIK masalasi: xato har qadamda |G| marta ko'payadi.
      </p>
    </div>
  );
}

/** su-14 — Izoparametrik almashtirish: tugunlarni surish va det J. */
export function Isoparametric() {
  const [skew, setSkew] = useState(0.0);
  const [pull, setPull] = useState(0.0);

  // Q4 tugunlari (ideal kvadratdan siljigan)
  const nodes: [number, number][] = [
    [-1, -1], [1, -1], [1 + skew - pull, 1 - pull], [-1 + skew, 1],
  ];

  const dets: number[] = [];
  const gp = 1 / Math.sqrt(3);
  for (const [xi, eta] of [[-gp, -gp], [gp, -gp], [gp, gp], [-gp, gp]]) {
    const dN = [
      [-(1 - eta) / 4, -(1 - xi) / 4],
      [(1 - eta) / 4, -(1 + xi) / 4],
      [(1 + eta) / 4, (1 + xi) / 4],
      [-(1 + eta) / 4, (1 - xi) / 4],
    ];
    let j11 = 0, j12 = 0, j21 = 0, j22 = 0;
    for (let k = 0; k < 4; k += 1) {
      j11 += dN[k][0] * nodes[k][0];
      j12 += dN[k][0] * nodes[k][1];
      j21 += dN[k][1] * nodes[k][0];
      j22 += dN[k][1] * nodes[k][1];
    }
    dets.push(j11 * j22 - j12 * j21);
  }
  const minDet = Math.min(...dets);
  const ok = minDet > 0;

  const W = 720, H = 380;
  const c1 = { x: 175, y: 195, s: 72 };
  const c2 = { x: 520, y: 195, s: 72 };
  const M = (p: [number, number], c: typeof c1): [number, number] =>
    [c.x + p[0] * c.s, c.y - p[1] * c.s];

  const ideal: [number, number][] = [[-1, -1], [1, -1], [1, 1], [-1, 1]];
  const grid = (c: typeof c1, pts: [number, number][]) => {
    const out: JSX.Element[] = [];
    const N = (xi: number, eta: number): [number, number] => {
      const s = [(1 - xi) * (1 - eta) / 4, (1 + xi) * (1 - eta) / 4,
                 (1 + xi) * (1 + eta) / 4, (1 - xi) * (1 + eta) / 4];
      let x = 0, y = 0;
      for (let k = 0; k < 4; k += 1) { x += s[k] * pts[k][0]; y += s[k] * pts[k][1]; }
      return M([x, y], c);
    };
    for (let k = 0; k <= 6; k += 1) {
      const t = -1 + (2 * k) / 6;
      const row: [number, number][] = [];
      const col: [number, number][] = [];
      for (let i = 0; i <= 24; i += 1) {
        const u = -1 + (2 * i) / 24;
        row.push(N(u, t));
        col.push(N(t, u));
      }
      out.push(<path key={`r${k}`} d={path(row)} fill="none" stroke="var(--rule-faint)" strokeWidth="1" />);
      out.push(<path key={`c${k}`} d={path(col)} fill="none" stroke="var(--rule-faint)" strokeWidth="1" />);
    }
    return out;
  };

  return (
    <div>
      <Figure width={W} height={H} label="Izoparametrik almashtirish va Yakobian"
              note="Chapdagi ideal element o'ngdagi haqiqiy elementga akslantiriladi.">
        {grid(c1, ideal)}
        <path d={path([...ideal.map((p) => M(p, c1)), M(ideal[0], c1)])}
              fill="none" stroke="var(--compress)" strokeWidth="2.4" />
        <text x={c1.x} y={c1.y + 115} textAnchor="middle" fontSize="12" fill="var(--compress)"
              fontFamily="var(--font-display)">ideal element (ξ, η)</text>

        {grid(c2, nodes)}
        <path d={path([...nodes.map((p) => M(p, c2)), M(nodes[0], c2)])}
              fill="none" stroke={ok ? "var(--tension)" : "var(--tension)"} strokeWidth="2.6"
              strokeDasharray={ok ? undefined : "6 4"} />
        {nodes.map((p, k) => {
          const [X, Y] = M(p, c2);
          return <circle key={k} cx={X} cy={Y} r="5" fill="var(--ink)" />;
        })}
        <text x={c2.x} y={c2.y + 115} textAnchor="middle" fontSize="12" fill="var(--tension)"
              fontFamily="var(--font-display)">haqiqiy element (x, y)</text>

        <text x={(c1.x + c2.x) / 2} y={c1.y - 4} textAnchor="middle" fontSize="20"
              fill="var(--rule)">→</text>
        <text x={(c1.x + c2.x) / 2} y={c1.y + 20} textAnchor="middle" fontSize="11"
              fill="var(--rule)" fontFamily="var(--font-mono)">x = ΣNᵢxᵢ</text>

        <text x={W / 2} y={H - 18} textAnchor="middle" fontSize="13"
              fill={ok ? "var(--compress)" : "var(--tension)"} fontFamily="var(--font-mono)">
          min det J = {minDet.toFixed(4)} — {ok ? "akslantirish teskarilanadi" : "ELEMENT AG'DARILDI"}
        </text>
      </Figure>

      <Controls>
        <Slider label="Qiyshaytirish" value={skew} min={0} max={2.2} step={0.05}
                onChange={setSkew} />
        <Slider label="Tugunni ichkariga tortish" value={pull} min={0} max={1.6} step={0.05}
                onChange={setPull} color="var(--mark)" />
      </Controls>

      <Readout items={[
        { label: "det J (4 Gauss nuqtasi)", value: dets.map((d) => d.toFixed(3)).join("  ") },
        { label: "min det J", value: minDet.toFixed(4),
          color: ok ? "var(--compress)" : "var(--tension)" },
        { label: "Holat", value: ok ? "to'g'ri" : "ag'darilgan element",
          color: ok ? "var(--compress)" : "var(--tension)" },
      ]} />
      <p className="tiny muted" style={{ marginTop: 6 }}>
        Tugunni ichkariga torting: det J kamayadi va nolga yetganda element
        ag'dariladi — FEM dasturlari aynan shu mezon bilan to'rni rad etadi.
      </p>
    </div>
  );
}

/** su-18 — To'r bo'yicha yaqinlashish va kuzatilgan tartib. */
export function Convergence() {
  const [order, setOrder] = useState<"p1" | "p2" | "p3">("p2");
  const [bug, setBug] = useState(false);

  const theo = { p1: 2, p2: 4, p3: 6 }[order];
  const p = bug ? 1 : theo;
  const ns = [2, 4, 8, 16, 32, 64];
  const errs = ns.map((n) => 0.9 * (1 / n) ** p);

  const W = 720, H = 380;
  const L = 72, R = 40, T = 30, B = 56;
  const iw = W - L - R, ih = H - T - B;
  const lx = (n: number) => L + ((Math.log10(n) - Math.log10(2)) / (Math.log10(64) - Math.log10(2))) * iw;
  const ly = (e: number) => T + ih - ((Math.log10(e) + 12) / 12) * ih;

  const pObs = Math.log(errs[3] / errs[4]) / Math.log(2);

  return (
    <div>
      <Figure width={W} height={H} label="To'r bo'yicha yaqinlashish va kuzatilgan tartib"
              note="Log-log grafikda qiyalik = yaqinlashish tartibi.">
        <Axes x={L} y={T} w={iw} h={ih} xLabel="elementlar soni n" yLabel="log₁₀ xato"
              xTicks={ns.map((n) => ({ at: lx(n), text: String(n) }))}
              yTicks={[-12, -9, -6, -3, 0].map((v) => ({ at: ly(10 ** v), text: String(v) }))} />
        <path d={path(errs.map((e, i) => [lx(ns[i]), ly(e)] as [number, number]))}
              fill="none" stroke={bug ? "var(--tension)" : "var(--compress)"} strokeWidth="3" />
        {errs.map((e, i) => (
          <circle key={i} cx={lx(ns[i])} cy={ly(e)} r="4.5"
                  fill={bug ? "var(--tension)" : "var(--compress)"} />
        ))}
        {/* nazariy qiyalik uchburchagi */}
        <g stroke="var(--mark)" strokeWidth="1.6" fill="none">
          <path d={`M ${lx(8)} ${ly(errs[2])} L ${lx(16)} ${ly(errs[2])} L ${lx(16)} ${ly(errs[2] / 2 ** theo)}`} />
        </g>
        <text x={lx(11)} y={ly(errs[2]) - 7} fontSize="11" fill="var(--mark)"
              fontFamily="var(--font-mono)">nazariy {theo}</text>
      </Figure>

      <Controls>
        <Choice label="Element tartibi" value={order} onChange={setOrder}
                options={[{ value: "p1", label: "chiziqli (p=1)" },
                          { value: "p2", label: "kvadratik (p=2)" },
                          { value: "p3", label: "kubik (p=3)" }]} />
        <Choice label="Kodga xato kiritish" value={bug ? "on" : "off"}
                onChange={(v) => setBug(v === "on")}
                options={[{ value: "off" as const, label: "xatosiz" },
                          { value: "on" as const, label: "xato bilan" }]} />
      </Controls>

      <Readout items={[
        { label: "Nazariy tartib", value: String(theo), color: "var(--mark)" },
        { label: "Kuzatilgan p_obs", value: pObs.toFixed(2),
          color: Math.abs(pObs - theo) < 0.15 ? "var(--compress)" : "var(--tension)" },
        { label: "Xulosa", value: Math.abs(pObs - theo) < 0.15 ? "kod to'g'ri" : "KODDA XATO BOR",
          color: Math.abs(pObs - theo) < 0.15 ? "var(--compress)" : "var(--tension)" },
      ]} />
      <p className="tiny muted" style={{ marginTop: 6 }}>
        "Xato bilan" ni yoqing: kuzatilgan tartib nazariydan pastga tushadi.
        Bu MMS verifikatsiyasining asosiy mezoni — tartib mos kelmasa, kodda xato bor.
      </p>
    </div>
  );
}
