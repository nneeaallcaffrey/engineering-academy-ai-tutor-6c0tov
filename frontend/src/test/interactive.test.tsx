import { render, screen, fireEvent } from "@testing-library/react";
import { describe, expect, it } from "vitest";
import { INTERACTIVE } from "../interactive/registry";
import { VectorMoment, Resonance } from "../interactive/nm";
import { BeamDiagrams, MohrCircle } from "../interactive/mq";
import { YieldSurfaces } from "../interactive/tmm";
import { PlateModes } from "../interactive/pq";
import { FDStability, Isoparametric } from "../interactive/su";

const PREFIX = ["nm-", "mq-", "tmm-", "pq-", "su-"];

describe("registry", () => {
  it("har bir fanda kamida 2 ta chizma bor", () => {
    for (const p of PREFIX) {
      const n = Object.keys(INTERACTIVE).filter((k) => k.startsWith(p)).length;
      expect(n, `${p} uchun chizmalar soni`).toBeGreaterThanOrEqual(2);
    }
  });

  it("har bir yozuvda sarlavha va komponent bor", () => {
    for (const [k, v] of Object.entries(INTERACTIVE)) {
      expect(v.title, k).toBeTruthy();
      expect(typeof v.Component, k).toBe("function");
    }
  });
});

describe("hammasi yiqilmasdan chiziladi", () => {
  it.each(Object.entries(INTERACTIVE))("%s", (_key, entry) => {
    const { container } = render(<entry.Component />);
    expect(container.querySelector("svg")).toBeTruthy();
  });
});

describe("VectorMoment", () => {
  it("burchak 0 ga tushsa moment nolga aylanadi", () => {
    render(<VectorMoment />);
    const sliders = screen.getAllByRole("slider");
    fireEvent.change(sliders[1], { target: { value: "0" } });   // burchak
    expect(screen.getByText(/0\.000 m/)).toBeTruthy();          // yelka d = 0
  });
});

describe("Resonance", () => {
  it("dempfirlash kamaysa cho'qqi o'sadi", () => {
    const { container } = render(<Resonance />);
    const s = screen.getAllByRole("slider")[0];
    fireEvent.change(s, { target: { value: "0.5" } });
    const low = container.textContent ?? "";
    fireEvent.change(s, { target: { value: "0.02" } });
    const high = container.textContent ?? "";
    const num = (t: string) => Number(/Maksimum M\s*([\d.]+)/.exec(t)?.[1] ?? 0);
    expect(num(high)).toBeGreaterThan(num(low));
  });
});

describe("BeamDiagrams", () => {
  it("muvozanat nazorati doim nol", () => {
    const { container } = render(<BeamDiagrams />);
    expect(container.textContent).toMatch(/ΣR − ΣF = 0\.000000/);
  });

  it("yuk turini almashtirish mumkin", () => {
    const { container } = render(<BeamDiagrams />);
    expect(container.textContent).not.toMatch(/Kuch joyi a\/L/);
    fireEvent.click(screen.getByRole("button", { name: /to'plangan P/ }));
    expect(container.textContent).toMatch(/Kuch joyi a\/L/);   // yangi surgich chiqdi
  });
});

describe("MohrCircle", () => {
  it("σₓ+σᵧ invarianti burchakka bog'liq emas", () => {
    const { container } = render(<MohrCircle />);
    const inv = () => /Invariant σₓ\+σᵧ\s*([-\d.]+)/.exec(container.textContent ?? "")?.[1];
    const before = inv();
    const sliders = screen.getAllByRole("slider");
    fireEvent.change(sliders[3], { target: { value: "37" } });  // burchak
    expect(inv()).toBe(before);
  });
});

describe("YieldSurfaces", () => {
  it("bir o'qli holatda ikkala mezon mos tushadi", () => {
    const { container } = render(<YieldSurfaces />);
    const sliders = screen.getAllByRole("slider");
    fireEvent.change(sliders[0], { target: { value: "200" } });
    fireEvent.change(sliders[1], { target: { value: "0" } });
    const t = container.textContent ?? "";
    const vm = Number(/Mizes\s*=\s*([\d.]+)/.exec(t)?.[1] ?? 0);
    const tr = Number(/Treska\s*=\s*([\d.]+)/.exec(t)?.[1] ?? 0);
    expect(Math.abs(vm - tr)).toBeLessThan(0.5);
  });
});

describe("PlateModes", () => {
  it("tugun chiziqlari soni (m-1)+(n-1)", () => {
    const { container } = render(<PlateModes />);
    const sliders = screen.getAllByRole("slider");
    fireEvent.change(sliders[0], { target: { value: "3" } });
    fireEvent.change(sliders[1], { target: { value: "2" } });
    expect(container.textContent).toMatch(/tugun chiziqlari:\s*3/);
  });
});

describe("FDStability", () => {
  it("r > 0,5 da portlaydi", () => {
    const { container } = render(<FDStability />);
    expect(container.textContent).toMatch(/BARQAROR/);
    fireEvent.change(screen.getAllByRole("slider")[0], { target: { value: "0.65" } });
    expect(container.textContent).toMatch(/PORTLADI/);
  });
});

describe("Isoparametric", () => {
  it("tugunni juda ichkariga tortsa element ag'dariladi", () => {
    const { container } = render(<Isoparametric />);
    expect(container.textContent).toMatch(/akslantirish teskarilanadi/);
    fireEvent.change(screen.getAllByRole("slider")[1], { target: { value: "1.6" } });
    expect(container.textContent).toMatch(/AG'DARILDI/);
  });
});
