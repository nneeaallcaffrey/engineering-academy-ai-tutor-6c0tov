"""PQ: plastina masalalarining yechim usullari."""
from __future__ import annotations

import numpy as np
from manim import Create, FadeIn, FadeOut, Line, Polygon, Write, VGroup, DOWN, LEFT, RIGHT, UP

from _common import (
    COMPRESS, INK, MARK, MexanikaScene, RULE, TENSION, axis_pair, curve, dashed, dot_at,
    formula, label, sampled,
)


def _navier_w(nmax, x=0.5, y=0.5):
    """Kvadrat SSSS plastina markazidagi koeffitsient (a=b=1, q=1, D=1)."""
    s = 0.0
    for m in range(1, nmax + 1, 2):
        for n in range(1, nmax + 1, 2):
            sg = (-1) ** ((m - 1) // 2) * (-1) ** ((n - 1) // 2)
            s += sg / (m * n * (m**2 + n**2) ** 2)
    return 16.0 / np.pi**6 * s


class NavierSeriesScene(MexanikaScene):
    """Qator juda tez yig'iladi: bir nechta had yetarli."""

    subject_code = "PQ-07"
    scene_title = "Navye qatorining yig'ilishi"

    def construct(self):
        block = self.show_title()
        O = np.array([-4.4, -1.9, 0.0])
        axes = axis_pair(O, x_len=8.6, y_len=4.0, x_label="hadlar soni", y_label=r"\alpha_w")
        self.play(Create(axes))

        exact = _navier_w(199)
        ns = list(range(1, 20, 2))
        vals = [_navier_w(n) for n in ns]
        sy = 3.2 / exact * 0.88
        pts = [O + np.array([0.42 * i + 0.4, v * sy, 0.0]) for i, v in enumerate(vals)]
        self.play(Create(curve(pts, color=TENSION, width=2.6)), run_time=1.2)
        self.play(FadeIn(VGroup(*[dot_at(p, color=TENSION) for p in pts])))

        lvl = Line(O + np.array([0.2, exact * sy, 0.0]), O + np.array([8.2, exact * sy, 0.0]),
                   color=INK, stroke_width=1.8)
        self.play(Create(lvl))
        self.play(Write(label(f"aniq: {exact:.6f}", O + np.array([6.2, exact * sy + 0.3, 0.0]),
                              scale=0.34, color=INK, mono=True)))

        rows = VGroup()
        for k, n in enumerate((1, 3, 5, 9)):
            v = _navier_w(n)
            err = abs(v - exact) / exact * 100
            rows.add(label(f"m,n <= {n:2d}:  {v:.6f}   xato {err:6.3f}%",
                           np.array([2.2, 2.35 - 0.42 * k, 0.0]), scale=0.34,
                           color=MARK if n == 1 else RULE, mono=True))
        self.play(Write(rows))

        eq = formula(r"w = \frac{16q}{\pi^6 D}\sum_{m,n\ \text{toq}} "
                     r"\frac{\sin\frac{m\pi x}{a}\sin\frac{n\pi y}{b}}"
                     r"{mn\left(\frac{m^2}{a^2}+\frac{n^2}{b^2}\right)^2}",
                     np.array([-0.6, -2.8, 0.0]), scale=0.5)
        self.play(Write(eq))
        self.play(FadeIn(self.caption(
            "Birinchi hadning o'zi 2,4% aniqlik beradi — maxraj m^5 kabi o'sadi")))
        self.wait(1.4)
        self.play(FadeIn(block))


class LevySolutionScene(MexanikaScene):
    """Bir yo'nalishda qator, ikkinchisida aniq yechim."""

    subject_code = "PQ-08"
    scene_title = "Levi yechimi va chekka effekti"

    def construct(self):
        block = self.show_title()
        c = np.array([-2.4, 0.3, 0.0])
        a, b = 2.6, 1.8
        plate = Polygon(c + np.array([-a, -b, 0]), c + np.array([a, -b, 0]),
                        c + np.array([a, b, 0]), c + np.array([-a, b, 0]),
                        color=INK, stroke_width=2.4, fill_opacity=0.05)
        self.play(Create(plate))
        self.play(Write(label("sharnirli", c + np.array([0.0, b + 0.3, 0.0]),
                              scale=0.32, color=COMPRESS)),
                  Write(label("sharnirli", c + np.array([0.0, -b - 0.3, 0.0]),
                              scale=0.32, color=COMPRESS)),
                  Write(label("ixtiyoriy", c + np.array([-a - 0.65, 0.0, 0.0]),
                              scale=0.32, color=TENSION)),
                  Write(label("ixtiyoriy", c + np.array([a + 0.65, 0.0, 0.0]),
                              scale=0.32, color=TENSION)))

        for y in np.linspace(-b * 0.8, b * 0.8, 5):
            self.add(curve([c + np.array([x, y, 0.0]) for x in np.linspace(-a, a, 40)],
                           color=RULE, width=1.2))

        eq = formula(r"w(x,y)=\sum_m Y_m(y)\sin\frac{m\pi x}{a}",
                     np.array([2.9, 1.9, 0.0]), scale=0.55)
        self.play(Write(eq))
        self.play(Write(label("y bo'yicha ODE, x bo'yicha qator",
                              np.array([2.9, 1.35, 0.0]), scale=0.32, color=RULE)))

        O = np.array([1.0, -2.4, 0.0])
        ax2 = axis_pair(O, x_len=4.6, y_len=2.3, x_label="y", y_label="M")
        self.play(Create(ax2))
        pts = sampled(lambda t: np.exp(-3.2 * t) * np.cos(3.2 * t),
                      0.0, 1.35, n=120, sx=3.2, sy=1.9, origin=O)
        self.play(Create(curve(pts, color=TENSION, width=2.6)), run_time=1.0)
        self.play(Write(label("chekka effekti tez so'nadi",
                              O + np.array([2.4, 1.6, 0.0]), scale=0.32, color=TENSION)))
        self.play(FadeIn(self.caption(
            "Ikki qarama-qarshi chekka sharnirli bo'lsa — Levi, to'rttasi ham — Navye")))
        self.wait(1.4)
        self.play(FadeIn(block))


class RitzMethodScene(MexanikaScene):
    """Sinov funksiyalari soni ortgani sari energiya pasayadi."""

    subject_code = "PQ-09"
    scene_title = "Ritz usuli: energiyani minimallashtirish"

    def construct(self):
        block = self.show_title()
        O = np.array([-4.6, -2.0, 0.0])
        axes = axis_pair(O, x_len=9.2, y_len=4.2, x_label="hadlar soni N", y_label=r"\Pi")
        self.play(Create(axes))

        exact = 1.0
        vals = [1.52, 1.16, 1.052, 1.019, 1.0075, 1.003]
        pts = [O + np.array([1.3 * i + 0.7, (v - 0.95) * 6.0, 0.0])
               for i, v in enumerate(vals)]
        self.play(Create(curve(pts, color=COMPRESS, width=2.6)),
                  FadeIn(VGroup(*[dot_at(p, color=COMPRESS) for p in pts])), run_time=1.3)

        lvl = Line(O + np.array([0.2, (exact - 0.95) * 6.0, 0.0]),
                   O + np.array([8.8, (exact - 0.95) * 6.0, 0.0]),
                   color=TENSION, stroke_width=2.2)
        self.play(Create(lvl))
        self.play(Write(label("aniq yechim", O + np.array([7.2, (exact - 0.95) * 6.0 - 0.35, 0.0]),
                              scale=0.34, color=TENSION)))
        self.play(Write(label("Ritz HAR DOIM yuqoridan yaqinlashadi",
                              O + np.array([3.4, 3.5, 0.0]), scale=0.36, color=COMPRESS)))

        eq = VGroup(
            formula(r"w \approx \sum_{i=1}^{N} c_i \varphi_i(x,y)",
                    np.array([2.4, 2.3, 0.0]), scale=0.58),
            formula(r"\frac{\partial \Pi}{\partial c_i} = 0",
                    np.array([2.4, 1.6, 0.0]), scale=0.58, color=MARK),
        )
        self.play(Write(eq[0])); self.play(Write(eq[1]))
        self.play(FadeIn(self.caption(
            "Sinov funksiyalari MAJBURIY chegaraviy shartlarni qanoatlantirishi shart")))
        self.wait(1.4)
        self.play(FadeIn(block))


class FiniteDifferenceScene(MexanikaScene):
    """Bigarmonik shablon 13 nuqtali; chekkada fiktiv tugun kerak."""

    subject_code = "PQ-10"
    scene_title = "Bigarmonik shablon va fiktiv tugunlar"

    def construct(self):
        block = self.show_title()
        c = np.array([-2.6, 0.1, 0.0])
        s = 0.72

        grid = VGroup()
        for i in range(-3, 4):
            grid.add(Line(c + np.array([-3 * s, i * s, 0]), c + np.array([3 * s, i * s, 0]),
                          color=RULE, stroke_width=0.9))
            grid.add(Line(c + np.array([i * s, -3 * s, 0]), c + np.array([i * s, 3 * s, 0]),
                          color=RULE, stroke_width=0.9))
        self.play(Create(grid), run_time=1.0)

        stencil = {(0, 0): 20, (1, 0): -8, (-1, 0): -8, (0, 1): -8, (0, -1): -8,
                   (1, 1): 2, (1, -1): 2, (-1, 1): 2, (-1, -1): 2,
                   (2, 0): 1, (-2, 0): 1, (0, 2): 1, (0, -2): 1}
        for (i, j), v in stencil.items():
            p = c + np.array([i * s, j * s, 0.0])
            col = TENSION if v > 0 else COMPRESS
            self.add(dot_at(p, color=col, r=0.09 if abs(v) > 5 else 0.065))
            self.add(label(f"{v:+d}", p + np.array([0.0, 0.26, 0.0]), scale=0.28,
                           color=col, mono=True))
        self.play(FadeIn(VGroup()), run_time=0.4)
        self.play(Write(label(f"{len(stencil)} nuqtali shablon",
                              c + np.array([0.0, -3.0, 0.0]), scale=0.36, color=INK)))

        edge = Line(c + np.array([3 * s, -3 * s, 0]), c + np.array([3 * s, 3 * s, 0]),
                    color=INK, stroke_width=3)
        self.play(Create(edge))
        ghost = VGroup(*[dot_at(c + np.array([4 * s, j * s, 0.0]), color=MARK, r=0.075)
                         for j in range(-3, 4)])
        self.play(FadeIn(ghost))
        self.play(Write(label("fiktiv tugunlar", c + np.array([4 * s + 0.9, 0.0, 0.0]),
                              scale=0.34, color=MARK)))

        eq = formula(r"\nabla^4 w \approx \frac{1}{h^4}\Big(20w_0 - 8\sum w_{\pm} "
                     r"+ 2\sum w_{d} + \sum w_{\pm 2}\Big) = \frac{q}{D}",
                     np.array([0.4, -3.35, 0.0]), scale=0.48)
        self.play(Write(eq))
        self.play(Write(label("Fiktiv tugun chegaraviy shartdan topiladi",
                              np.array([3.0, 2.1, 0.0]), scale=0.34, color=MARK)))
        self.wait(1.4)
        self.play(FadeIn(block))


class OrthotropicPlateScene(MexanikaScene):
    """Gofr va qovurg'a: bir yo'nalishda bikrlik keskin oshadi."""

    subject_code = "PQ-12"
    scene_title = "Geometrik ortotropiya: gofr va qovurg'a"

    def construct(self):
        block = self.show_title()

        # gofrlangan varaq
        y0 = 1.6
        pts = [np.array([x, y0 + 0.28 * np.sin(4.2 * x), 0.0])
               for x in np.linspace(-5.0, 5.0, 220)]
        self.play(Create(curve(pts, color=INK, width=2.6)), run_time=1.2)
        self.play(Write(label("gofrlangan varaq", np.array([0.0, y0 + 0.75, 0.0]),
                              scale=0.36, color=RULE)))

        # qovurg'ali panel
        y1 = -0.4
        skin = Line(np.array([-5.0, y1, 0.0]), np.array([5.0, y1, 0.0]),
                    color=INK, stroke_width=3)
        self.play(Create(skin))
        ribs = VGroup(*[Line(np.array([x, y1, 0.0]), np.array([x, y1 - 0.75, 0.0]),
                             color=COMPRESS, stroke_width=4)
                        for x in np.linspace(-4.0, 4.0, 6)])
        self.play(Create(ribs))
        self.play(Write(label("qovurg'ali panel", np.array([0.0, y1 - 1.15, 0.0]),
                              scale=0.36, color=RULE)))

        bars = VGroup()
        for k, (name, val, col) in enumerate([("D_x", 21.5, TENSION), ("D_y", 1.0, COMPRESS)]):
            w = 0.24 * np.log10(val * 9 + 1) * 3.4
            y = -2.3 - 0.45 * k
            bars.add(Line(np.array([-3.0, y, 0.0]), np.array([-3.0 + w, y, 0.0]),
                          color=col, stroke_width=11))
            bars.add(label(f"{name} = {val:.1f} D", np.array([-3.0 + w + 1.1, y, 0.0]),
                           scale=0.34, color=col, mono=True))
        self.play(FadeIn(bars))

        eq = formula(r"D_x\frac{\partial^4 w}{\partial x^4} + "
                     r"2H\frac{\partial^4 w}{\partial x^2\partial y^2} + "
                     r"D_y\frac{\partial^4 w}{\partial y^4} = q",
                     np.array([1.8, -2.55, 0.0]), scale=0.52)
        self.play(Write(eq))
        self.play(FadeIn(self.caption(
            "Material izotrop, lekin geometriya ortotrop xatti-harakat beradi")))
        self.wait(1.4)
        self.play(FadeIn(block))
