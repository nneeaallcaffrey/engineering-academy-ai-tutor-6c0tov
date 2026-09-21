"""SU: chekli ayirmalar usuli."""
from __future__ import annotations

import numpy as np
from manim import Create, FadeIn, Line, Polygon, Write, VGroup, DOWN, LEFT, RIGHT, UP

from _common import (
    COMPRESS, INK, MARK, MexanikaScene, RULE, TENSION, axis_pair, curve, dashed, dot_at,
    formula, label, sampled,
)


class StencilScene(MexanikaScene):
    """Bir xil hosila uchun turli shablonlar va ularning tartibi."""

    subject_code = "SU-07"
    scene_title = "Shablon va sxema koeffitsientlari"

    def construct(self):
        block = self.show_title()
        stencils = [
            ("oldinga", {0: -1, 1: 1}, "O(h)", COMPRESS),
            ("markaziy", {-1: -0.5, 1: 0.5}, "O(h^2)", TENSION),
            ("4-tartib", {-2: 1 / 12, -1: -2 / 3, 1: 2 / 3, 2: -1 / 12}, "O(h^4)", MARK),
        ]
        for k, (name, st, order, col) in enumerate(stencils):
            y = 1.7 - 1.5 * k
            base = Line(np.array([-4.6, y, 0.0]), np.array([1.4, y, 0.0]),
                        color=RULE, stroke_width=1.2)
            self.play(Create(base), run_time=0.25)
            for i in range(-2, 3):
                p = np.array([-1.6 + i * 1.0, y, 0.0])
                if i in st:
                    self.add(dot_at(p, color=col, r=0.095))
                    self.add(label(f"{st[i]:+.3g}", p + np.array([0.0, 0.3, 0.0]),
                                   scale=0.28, color=col, mono=True))
                else:
                    self.add(dot_at(p, color=RULE, r=0.05))
                self.add(label(f"{i:+d}", p + np.array([0.0, -0.32, 0.0]), scale=0.26,
                               color=RULE, mono=True))
            self.play(Write(label(f"{name}  {order}", np.array([2.6, y, 0.0]),
                                  scale=0.38, color=col, mono=True)), run_time=0.4)

        # tartibni SONLI tekshiramiz
        def f(x):
            return np.sin(x)
        x0 = 0.7
        rows = VGroup()
        for k, (name, st, order, col) in enumerate(stencils):
            errs = []
            for h in (0.1, 0.05):
                d = sum(c * f(x0 + i * h) for i, c in st.items()) / h
                errs.append(abs(d - np.cos(x0)))
            p_obs = np.log2(errs[0] / errs[1])
            rows.add(label(f"{name:9s} o'lchangan tartib = {p_obs:.2f}",
                           np.array([-1.0, -2.05 - 0.42 * k, 0.0]), scale=0.32,
                           color=col, mono=True))
        self.play(Write(rows))
        self.play(FadeIn(self.caption(
            "Koeffitsientlar Teylor qatorini kerakli tartibgacha yo'q qilishdan chiqadi")))
        self.wait(1.4)
        self.play(FadeIn(block))


class BeamFDScene(MexanikaScene):
    """To'rtinchi tartib shablon chetdan tashqariga chiqadi."""

    subject_code = "SU-08"
    scene_title = "Balka masalasi va soxta tugunlar"

    def construct(self):
        block = self.show_title()
        y = 0.9
        base = Line(np.array([-5.0, y, 0.0]), np.array([5.0, y, 0.0]),
                    color=INK, stroke_width=3)
        self.play(Create(base))

        n = 9
        xs = np.linspace(-4.0, 4.0, n)
        for i, x in enumerate(xs):
            self.add(dot_at(np.array([x, y, 0.0]), color=INK, r=0.075))
            self.add(label(f"{i}", np.array([x, y + 0.32, 0.0]), scale=0.28,
                           color=RULE, mono=True))

        ghosts = [np.array([-5.0, y, 0.0]), np.array([5.0, y, 0.0])]
        self.play(FadeIn(VGroup(*[dot_at(g, color=MARK, r=0.085) for g in ghosts])))
        self.play(Write(label("soxta tugun", np.array([-5.0, y - 0.42, 0.0]), scale=0.3,
                              color=MARK)),
                  Write(label("soxta tugun", np.array([5.0, y - 0.42, 0.0]), scale=0.3,
                              color=MARK)))

        # shablon
        st = {-2: 1, -1: -4, 0: 6, 1: -4, 2: 1}
        c = np.array([0.0, -0.9, 0.0])
        for i, v in st.items():
            p = c + np.array([i * 1.0, 0.0, 0.0])
            self.add(dot_at(p, color=TENSION if v > 0 else COMPRESS, r=0.09))
            self.add(label(f"{v:+d}", p + np.array([0.0, 0.3, 0.0]), scale=0.3,
                           color=TENSION if v > 0 else COMPRESS, mono=True))
        self.play(Write(label("5 nuqtali shablon", c + np.array([3.2, 0.0, 0.0]),
                              scale=0.36, color=INK)))

        eq = VGroup(
            formula(r"\frac{d^4w}{dx^4} \approx "
                    r"\frac{w_{i-2}-4w_{i-1}+6w_i-4w_{i+1}+w_{i+2}}{h^4}",
                    np.array([0.0, -2.1, 0.0]), scale=0.55),
            label("sharnir: w = 0, w'' = 0  ->  w_{-1} = -w_1",
                  np.array([0.0, -2.7, 0.0]), scale=0.34, color=MARK, mono=True),
            label("qisilgan: w = 0, w' = 0  ->  w_{-1} = w_1",
                  np.array([0.0, -3.1, 0.0]), scale=0.34, color=MARK, mono=True),
        )
        for e in eq:
            self.play(Write(e), run_time=0.5)
        self.wait(1.3)
        self.play(FadeIn(block))


class TorsionScene(MexanikaScene):
    """Membrana analogiyasi: sovun pardasi = Prandtl funksiyasi."""

    subject_code = "SU-09"
    scene_title = "Membrana analogiyasi va buralish"

    def construct(self):
        block = self.show_title()
        c = np.array([-3.1, 0.4, 0.0])
        a = 1.7
        sq = Polygon(c + np.array([-a, -a, 0]), c + np.array([a, -a, 0]),
                     c + np.array([a, a, 0]), c + np.array([-a, a, 0]),
                     color=INK, stroke_width=2.4)
        self.play(Create(sq))

        # Prandtl funksiyasining sath chiziqlari
        for lev in (0.2, 0.45, 0.7, 0.9):
            pts = []
            for t in np.linspace(0, 2 * np.pi, 160):
                r = a * (1 - lev) * (1.0 + 0.12 * np.cos(4 * t))
                pts.append(c + np.array([r * np.cos(t), r * np.sin(t), 0.0]))
            self.play(Create(curve(pts, color=COMPRESS, width=1.8)), run_time=0.35)
        self.play(Write(label("sath chiziqlari = urinma kuchlanish yo'nalishi",
                              c + np.array([0.0, -a - 0.5, 0.0]), scale=0.32, color=COMPRESS)))

        # yon ko'rinish: parda
        O = np.array([2.6, -1.4, 0.0])
        base = Line(O + LEFT * 2.0, O + RIGHT * 2.0, color=INK, stroke_width=2.4)
        self.play(Create(base))
        dome = [O + np.array([t, 1.7 * np.cos(np.pi * t / 4.0) ** 2 - 0.0, 0.0])
                for t in np.linspace(-2.0, 2.0, 120)]
        self.play(Create(curve(dome, color=TENSION, width=2.8)), run_time=0.9)
        self.play(Write(label("sovun pardasi", O + np.array([0.0, 2.15, 0.0]),
                              scale=0.34, color=TENSION)))

        rows = VGroup(
            formula(r"\nabla^2 \phi = -2G\theta", np.array([2.6, 2.6, 0.0]), scale=0.6),
            label("qiyalik  -> urinma kuchlanish", np.array([2.6, -2.0, 0.0]),
                  scale=0.33, color=MARK, mono=True),
            label("hajm     -> burovchi moment", np.array([2.6, -2.4, 0.0]),
                  scale=0.33, color=MARK, mono=True),
            label("burchakda qiyalik 0 -> tau = 0", np.array([2.6, -2.8, 0.0]),
                  scale=0.33, color=RULE, mono=True),
        )
        for r in rows:
            self.play(Write(r), run_time=0.45)
        self.wait(1.3)
        self.play(FadeIn(block))


class StabilityScene(MexanikaScene):
    """Kuchayish koeffitsienti: |G| > 1 bo'lsa sxema portlaydi."""

    subject_code = "SU-10"
    scene_title = "Barqarorlik va kuchayish koeffitsienti"

    def construct(self):
        block = self.show_title()
        O = np.array([-4.6, -1.4, 0.0])
        axes = axis_pair(O, x_len=9.2, y_len=3.6, x_label="qadam n", y_label="u")
        self.play(Create(axes))

        for i, (r, col, name) in enumerate(((0.4, COMPRESS, "r = 0,40  barqaror"),
                                            (0.5, MARK, "r = 0,50  chegara"),
                                            (0.6, TENSION, "r = 0,60  PORTLAYDI"))):
            G = 1 - 4 * r          # eng yomon harmonika: k h = pi
            pts = []
            for n in range(0, 26):
                v = G ** n
                if abs(v) > 6:
                    break
                pts.append(O + np.array([n * 0.34, 1.6 + v * 0.55, 0.0]))
            self.play(Create(curve(pts, color=col, width=2.4)), run_time=0.7)
            self.play(Write(label(f"{name}   |G| = {abs(G):.2f}",
                                  np.array([2.2, 2.4 - 0.45 * i, 0.0]),
                                  scale=0.33, color=col, mono=True)), run_time=0.3)

        mid = Line(O + np.array([0.0, 1.6, 0.0]), O + np.array([8.8, 1.6, 0.0]),
                   color=RULE, stroke_width=1.2)
        self.play(Create(mid))
        eq = VGroup(
            formula(r"G = 1 - 4r\sin^2\frac{kh}{2},\qquad r = \frac{\alpha\,\Delta t}{h^2}",
                    np.array([0.0, -2.5, 0.0]), scale=0.58),
            formula(r"|G| \le 1 \ \Longleftrightarrow\ r \le \tfrac12",
                    np.array([0.0, -3.05, 0.0]), scale=0.6, color=TENSION),
        )
        self.play(Write(eq[0])); self.play(Write(eq[1]))
        self.play(FadeIn(self.caption(
            "Barqarorlik sharti aniqlikdan EMAS, xatoning o'sishidan kelib chiqadi")))
        self.wait(1.4)
        self.play(FadeIn(block))


class NewmarkScene(MexanikaScene):
    """Sonli demflash va davr cho'zilishi — sxemaning o'z xatosi."""

    subject_code = "SU-11"
    scene_title = "Sonli demflash va davr cho'zilishi"

    def construct(self):
        block = self.show_title()
        O = np.array([-5.0, 0.4, 0.0])
        axes = axis_pair(O, x_len=10.0, y_len=2.2, x_label="t", y_label="u")
        self.play(Create(axes))

        exact = [O + np.array([t * 1.1, np.cos(2.2 * t), 0.0])
                 for t in np.linspace(0, 8.6, 300)]
        self.play(Create(curve(exact, color=INK, width=2.2)), run_time=1.0)
        self.play(Write(label("aniq yechim", np.array([3.6, 1.9, 0.0]), scale=0.32,
                              color=INK)))

        for (gam, col, name) in ((0.5, COMPRESS, "gamma = 0,50  energiya saqlanadi"),
                                 (0.7, TENSION, "gamma = 0,70  sonli demflash")):
            damp = 0.0 if abs(gam - 0.5) < 1e-9 else 0.085
            period = 1.0 if abs(gam - 0.5) < 1e-9 else 1.045
            pts = [O + np.array([t * 1.1, np.exp(-damp * t) * np.cos(2.2 * t / period), 0.0])
                   for t in np.linspace(0, 8.6, 300)]
            self.play(Create(curve(pts, color=col, width=2.4)), run_time=0.9)
            self.play(Write(label(name, np.array([3.2, 1.45 if gam > 0.6 else 1.9, 0.0])
                                  + DOWN * (0.0 if gam > 0.6 else 0.0),
                                  scale=0.32, color=col, mono=True)), run_time=0.3)

        rows = VGroup(
            formula(r"u_{n+1} = u_n + \Delta t\,\dot u_n + "
                    r"\Delta t^2\left[(\tfrac12-\beta)\ddot u_n + \beta \ddot u_{n+1}\right]",
                    np.array([0.0, -1.85, 0.0]), scale=0.5),
            label("gamma = 1/2, beta = 1/4 — shartsiz barqaror, demflashsiz",
                  np.array([0.0, -2.45, 0.0]), scale=0.33, color=COMPRESS, mono=True),
            label("gamma > 1/2 — yuqori chastotalarni so'ndiradi, lekin tartib 1 ga tushadi",
                  np.array([0.0, -2.85, 0.0]), scale=0.33, color=TENSION, mono=True),
        )
        for r in rows:
            self.play(Write(r), run_time=0.5)
        self.wait(1.3)
        self.play(FadeIn(block))


class WaveCFLScene(MexanikaScene):
    """CFL: sonli ta'sir konusi fizikaviysini qamrab olishi shart."""

    subject_code = "SU-12"
    scene_title = "CFL sharti va sonli dispersiya"

    def construct(self):
        block = self.show_title()
        for k, (C, name, col, ok) in enumerate([(0.6, "C = 0,6", COMPRESS, True),
                                                (1.4, "C = 1,4", TENSION, False)]):
            O = np.array([-3.2 + 6.4 * k, -1.7, 0.0])
            ax = VGroup(Line(O + LEFT * 2.3, O + RIGHT * 2.3, color=INK, stroke_width=1.8),
                        Line(O, O + UP * 3.4, color=INK, stroke_width=1.8))
            self.play(Create(ax), run_time=0.3)

            for i in range(-4, 5):
                for j in range(0, 6):
                    self.add(dot_at(O + np.array([i * 0.55, j * 0.6, 0.0]),
                                    color=RULE, r=0.035))

            # sonli konus: qiyalik 1 tugun / 1 qadam
            num = Polygon(O, O + np.array([-3.0, 3.3, 0.0]), O + np.array([3.0, 3.3, 0.0]),
                          color=COMPRESS, stroke_width=1.8, fill_opacity=0.08)
            # fizikaviy konus: qiyalik C
            phys = Polygon(O, O + np.array([-3.0 * C, 3.3, 0.0]),
                           O + np.array([3.0 * C, 3.3, 0.0]),
                           color=TENSION, stroke_width=2.2, fill_opacity=0.10)
            self.play(Create(num), Create(phys), run_time=0.6)

            verdict = "qamraydi -> BARQAROR" if ok else "qamramaydi -> PORTLAYDI"
            self.play(Write(label(name, O + np.array([0.0, -0.45, 0.0]), scale=0.4,
                                  color=col, mono=True)),
                      Write(label(verdict, O + np.array([0.0, -0.9, 0.0]), scale=0.32,
                                  color=col)), run_time=0.4)

        leg = VGroup(
            label("sonli ta'sir sohasi", np.array([0.0, 2.5, 0.0]), scale=0.3, color=COMPRESS),
            label("fizikaviy ta'sir sohasi", np.array([0.0, 2.15, 0.0]), scale=0.3,
                  color=TENSION),
        )
        self.play(Write(leg))
        eq = formula(r"C = \frac{c\,\Delta t}{h} \le 1",
                     np.array([0.0, -2.95, 0.0]), scale=0.7)
        self.play(Write(eq))
        self.play(FadeIn(self.caption(
            "Ma'lumot to'r bo'ylab to'lqindan tez tarqala olmaydi")))
        self.wait(1.4)
        self.play(FadeIn(block))
