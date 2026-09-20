import { render, screen, fireEvent, waitFor } from "@testing-library/react";
import { MemoryRouter } from "react-router-dom";
import { beforeEach, describe, expect, it, vi } from "vitest";
import { Epure } from "../components/Epure";
import { Plot } from "../components/Plot";
import { PlainEditor } from "../components/CodeEditor";
import { Lab } from "../components/Lab";
import type { Computation } from "../api/types";

describe("Epure", () => {
  it("har bir mavzu uchun bitta ustun chizadi", () => {
    const { container } = render(<Epure values={[true, false, true]} />);
    expect(container.querySelectorAll("rect")).toHaveLength(3);
  });

  it("o'zlashtirilganlar sonini aytadi", () => {
    render(<Epure values={[true, true, false]} />);
    expect(screen.getByRole("img")).toHaveAttribute(
      "aria-label", expect.stringContaining("2 / 3"));
  });

  it("bo'sh ro'yxatda yiqilmaydi", () => {
    expect(() => render(<Epure values={[]} />)).not.toThrow();
  });
});

describe("Plot", () => {
  const s = [{ label: "A", x: [1, 2, 3], y: [1, 4, 9], xlabel: "x", ylabel: "y" }];

  it("seriya bo'lmasa hech narsa chizmaydi", () => {
    const { container } = render(<Plot series={[]} />);
    expect(container.querySelector("svg")).toBeNull();
  });

  it("chiziq yo'lini quradi", () => {
    const { container } = render(<Plot series={s} />);
    const path = container.querySelector("path");
    expect(path?.getAttribute("d")).toMatch(/^M[\d.]+ [\d.]+L/);
  });

  it("bir nechta seriyada afsona ko'rsatadi va yashira oladi", () => {
    const two = [...s, { label: "B", x: [1, 2], y: [2, 3], xlabel: "", ylabel: "" }];
    const { container } = render(<Plot series={two} />);
    expect(screen.getByText("B")).toBeInTheDocument();
    expect(container.querySelectorAll("path").length).toBe(2);
    fireEvent.click(screen.getByText("B"));
    expect(container.querySelectorAll("path").length).toBe(1);
  });
});

describe("PlainEditor", () => {
  it("qator raqamlarini ko'rsatadi", () => {
    render(<PlainEditor value={"a\nb\nc"} onChange={() => undefined} />);
    expect(screen.getByText("3")).toBeInTheDocument();
  });

  it("Tab bosilganda 4 bo'sh joy qo'yadi", () => {
    const onChange = vi.fn();
    render(<PlainEditor value="x" onChange={onChange} />);
    const ta = screen.getByRole("textbox");
    (ta as HTMLTextAreaElement).setSelectionRange(1, 1);
    fireEvent.keyDown(ta, { key: "Tab" });
    expect(onChange).toHaveBeenCalledWith("x    ");
  });

  it("Ctrl+Enter kodni ishga tushiradi", () => {
    const onRun = vi.fn();
    render(<PlainEditor value="x" onChange={() => undefined} onRun={onRun} />);
    fireEvent.keyDown(screen.getByRole("textbox"), { key: "Enter", ctrlKey: true });
    expect(onRun).toHaveBeenCalledOnce();
  });
});

describe("Lab", () => {
  const computation: Computation = {
    caption: "Sinov hisobi",
    code: "from labkit import value\nvalue('x', 1)",
    expected_output: "x = 1",
    parameters: [{ key: "a", label: "Radius", minimum: 1, maximum: 10,
                   default: 5, step: 1, unit: "mm" }],
  };

  beforeEach(() => {
    vi.restoreAllMocks();
  });

  it("parametrni ko'rsatadi va o'zgartirganda qiymat yangilanadi", () => {
    render(<MemoryRouter><Lab topicId="t-1" computation={computation} /></MemoryRouter>);
    expect(screen.getByText("Radius")).toBeInTheDocument();
    expect(screen.getByText("5 mm")).toBeInTheDocument();
    fireEvent.change(screen.getByRole("slider"), { target: { value: "8" } });
    expect(screen.getByText("8 mm")).toBeInTheDocument();
  });

  it("Run bosilganda backendga so'rov yuboradi va natijani chizadi", async () => {
    const fetchMock = vi.fn().mockResolvedValue({
      ok: true,
      json: async () => ({
        ok: true, values: [{ label: "w", value: 91.8353, unit: "um" }],
        notes: [], series: [], tables: [], stdout: "", error: "",
        error_type: "", duration_ms: 42,
      }),
    });
    vi.stubGlobal("fetch", fetchMock);

    render(<MemoryRouter><Lab topicId="su-30" computation={computation} /></MemoryRouter>);
    fireEvent.click(screen.getByRole("button", { name: /Ishga tushirish/ }));

    await waitFor(() => expect(screen.getByText("91.8353")).toBeInTheDocument());
    expect(fetchMock).toHaveBeenCalledWith(
      "/api/topics/su-30/run", expect.objectContaining({ method: "POST" }));
    const body = JSON.parse(fetchMock.mock.calls[0][1].body);
    expect(body.params).toEqual({ a: 5 });
    expect(body.code).toBeUndefined();     // kod tahrirlanmagan — yuborilmaydi
  });

  it("sandbox xatosini ko'rsatadi, ilovani yiqitmaydi", async () => {
    vi.stubGlobal("fetch", vi.fn().mockResolvedValue({
      ok: true,
      json: async () => ({
        ok: false, values: [], notes: [], series: [], tables: [], stdout: "",
        error: "'os' modulini import qilish taqiqlangan",
        error_type: "PolicyError", duration_ms: 3,
      }),
    }));
    render(<MemoryRouter><Lab topicId="su-30" computation={computation} /></MemoryRouter>);
    fireEvent.click(screen.getByRole("button", { name: /Ishga tushirish/ }));
    await waitFor(() =>
      expect(screen.getByRole("alert")).toHaveTextContent("PolicyError"));
  });

  it("tarmoq uzilsa tushunarli xabar beradi", async () => {
    vi.stubGlobal("fetch", vi.fn().mockRejectedValue(new Error("network")));
    render(<MemoryRouter><Lab topicId="su-30" computation={computation} /></MemoryRouter>);
    fireEvent.click(screen.getByRole("button", { name: /Ishga tushirish/ }));
    await waitFor(() =>
      expect(screen.getByRole("alert")).toHaveTextContent(/ulanib bo'lmadi/));
  });
});
