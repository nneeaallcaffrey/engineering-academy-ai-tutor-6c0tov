"""MQ: egilish epyuralari va neytral qatlam."""
from __future__ import annotations

import numpy as np
from manim import Arrow, Create, FadeIn, Line, Polygon, Write, VGroup, DOWN, LEFT, RIGHT, UP

from _common import (
    COMPRESS, INK, MARK, MexanikaScene, RULE, TENSION, curve, dashed, dot_at, formula, hatched,
    label, load_arrows, support_pin,
)


class BeamDiagramScene(MexanikaScene):
    """Q va M epyuralari bir vaqtda quriladi: dM/dx = Q."""

    subject_code = "MQ-12"
    scene_title = "Kesuvchi kuch va eguvchi moment epyuralari"

    def construct(self):
        block = self.show_title()
        L = 8.0
        A = np.array([-4.0, 1.8, 0.0])
        B = np.array([4.0, 1.8, 0.0])
        beam = Line(A, B, color=INK, stroke_width=5)
        self.play(Create(beam), Create(VGroup(support_pin(A), support_pin(B))))
        self.play(Create(load_arrows(A, B, n=9, length=0.55)))
        self.play(Write(label("q", np.array([0.0, 2.6, 0.0]), scale=0.42, color=COMPRESS)))

        q = 1.0
        xs = np.linspace(0.0, 1.0, 22)
        Q = [q * L * (0.5 - x) for x in xs]
        M = [q * L * L * x * (1 - x) / 2 for x in xs]

        qmax = max(abs(v) for v in Q)
        mmax = max(M)
        epQ = hatched(np.array([-4.0, -0.15, 0.0]), np.array([4.0, -0.15, 0.0]),
                      [v / qmax for v in Q], n=22, scale=0.85)
        self.play(Create(epQ), run_time=1.2)
        self.play(Write(label("Q", np.array([-4.6, -0.15, 0.0]), scale=0.45)),
                  Write(label("qL/2", np.array([-4.0, 0.95, 0.0]), scale=0.32,
                              color=TENSION, mono=True)))

        epM = hatched(np.array([-4.0, -2.4, 0.0]), np.array([4.0, -2.4, 0.0]),
                      [v / mmax for v in M], n=22, scale=0.9)
        self.play(Create(epM), run_time=1.2)
        self.play(Write(label("M", np.array([-4.6, -2.4, 0.0]), scale=0.45)),
                  Write(label("qL^2/8", np.array([0.0, -1.25, 0.0]), scale=0.34,
                              color=TENSION, mono=True)))

        mark = dashed(np.array([0.0, -0.15, 0.0]), np.array([0.0, -2.4, 0.0]))
        self.play(Create(mark))
        self.play(Write(label("Q = 0 -> M maksimal", np.array([1.9, -1.35, 0.0]),
                              scale=0.34, color=MARK, mono=True)))
        eq = formula(r"\frac{dM}{dx} = Q,\qquad \frac{dQ}{dx} = -q",
                     np.array([0.0, -3.2, 0.0]), scale=0.6)
        self.play(Write(eq))
        self.wait(1.4)
        self.play(FadeIn(block))


class BendingStressScene(MexanikaScene):
    """Neytral qatlam: yuqorisi siqiladi, pasti cho'ziladi."""

    subject_code = "MQ-13"
    scene_title = "Egilishda neytral qatlam"

    def construct(self):
        block = self.show_title()

        # egilgan balka bo'lagi
        c = np.array([-3.0, 0.2, 0.0])
        R = 4.2
        for k, (off, col, w) in enumerate([(0.62, COMPRESS, 2.4), (0.0, MARK, 3.0),
                                           (-0.62, TENSION, 2.4)]):
            pts = [c + np.array([(R + off) * np.sin(a), (R + off) * np.cos(a) - R, 0.0])
                   for a in np.linspace(-0.42, 0.42, 60)]
            self.play(Create(curve(pts, color=col, width=w)), run_time=0.6)
        self.play(Write(label("siqilish", c + np.array([2.1, 0.95, 0.0]), scale=0.36,
                              color=COMPRESS)),
                  Write(label("neytral qatlam", c + np.array([2.4, 0.15, 0.0]), scale=0.36,
                              color=MARK)),
                  Write(label("cho'zilish", c + np.array([2.1, -0.75, 0.0]), scale=0.36,
                              color=TENSION)))

        # kesim va kuchlanish epyurasi
        base = np.array([2.6, 0.2, 0.0])
        h = 1.5
        sec = Polygon(base + np.array([-0.45, h, 0.0]), base + np.array([0.45, h, 0.0]),
                      base + np.array([0.45, -h, 0.0]), base + np.array([-0.45, -h, 0.0]),
                      color=INK, stroke_width=2.4, fill_opacity=0.07)
        self.play(Create(sec))
        axis = dashed(base + LEFT * 0.9, base + RIGHT * 3.6)
        self.play(Create(axis))

        ep = hatched(base + np.array([1.0, h, 0.0]), base + np.array([1.0, -h, 0.0]),
                     list(np.linspace(-1.0, 1.0, 18)), n=18, scale=1.25)
        self.play(Create(ep), run_time=1.0)
        self.play(Write(label("sigma", base + np.array([2.6, 0.55, 0.0]), scale=0.4)))
        self.play(Write(label("y", base + np.array([-0.05, 1.75, 0.0]), scale=0.38)))

        eq = formula(r"\sigma = \frac{M\,y}{I},\qquad \int_A y\,dA = 0",
                     np.array([0.0, -2.6, 0.0]), scale=0.66)
        self.play(Write(eq))
        self.play(FadeIn(self.caption(
            "Neytral o'q og'irlik markazidan o'tadi — shuning uchun statik moment nol")))
        self.wait(1.5)
        self.play(FadeIn(block))
