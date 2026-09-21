"""TMM: elastik to'lqinlar."""
from __future__ import annotations

import numpy as np
from manim import Create, FadeIn, Line, Write, VGroup, DOWN, LEFT, RIGHT, UP

from _common import (
    COMPRESS, INK, MARK, MexanikaScene, RULE, TENSION, curve, dot_at, formula, label,
)


class ElasticWaveScene(MexanikaScene):
    """P-to'lqin bo'ylama, S-to'lqin ko'ndalang; P doim tezroq."""

    subject_code = "TMM-20"
    scene_title = "P- va S-to'lqinlar"

    def construct(self):
        block = self.show_title()
        E, nu, rho = 210e9, 0.3, 7850.0
        lam = E * nu / ((1 + nu) * (1 - 2 * nu))
        mu = E / (2 * (1 + nu))
        cp = float(np.sqrt((lam + 2 * mu) / rho))
        cs = float(np.sqrt(mu / rho))

        # P-to'lqin: zarralar siqilish yo'nalishida
        yP = 1.5
        base = Line(np.array([-5.4, yP, 0.0]), np.array([5.4, yP, 0.0]),
                    color=RULE, stroke_width=1.2)
        self.play(Create(base))
        dots = VGroup()
        for i in range(46):
            x = -5.2 + 10.4 * i / 45
            d = 0.34 * np.sin(2.2 * x)
            dots.add(dot_at(np.array([x + d, yP, 0.0]), color=TENSION, r=0.055))
        self.play(FadeIn(dots), run_time=1.0)
        self.play(Write(label("P-to'lqin — bo'ylama (siqilish)",
                              np.array([-1.6, yP + 0.62, 0.0]), scale=0.38, color=TENSION)))

        # S-to'lqin
        yS = -0.7
        base2 = Line(np.array([-5.4, yS, 0.0]), np.array([5.4, yS, 0.0]),
                     color=RULE, stroke_width=1.2)
        self.play(Create(base2))
        wave = curve([np.array([x, yS + 0.45 * np.sin(2.2 * x), 0.0])
                      for x in np.linspace(-5.2, 5.2, 200)], color=COMPRESS, width=2.6)
        dots2 = VGroup()
        for i in range(46):
            x = -5.2 + 10.4 * i / 45
            dots2.add(dot_at(np.array([x, yS + 0.45 * np.sin(2.2 * x), 0.0]),
                             color=COMPRESS, r=0.05))
        self.play(Create(wave), FadeIn(dots2), run_time=1.2)
        self.play(Write(label("S-to'lqin — ko'ndalang (siljish)",
                              np.array([-1.5, yS - 0.85, 0.0]), scale=0.38, color=COMPRESS)))

        vals = VGroup(
            label(f"c_P = {cp:.0f} m/s", np.array([3.4, -2.05, 0.0]), scale=0.36,
                  color=TENSION, mono=True),
            label(f"c_S = {cs:.0f} m/s", np.array([3.4, -2.45, 0.0]), scale=0.36,
                  color=COMPRESS, mono=True),
            label(f"c_P / c_S = {cp/cs:.3f}", np.array([3.4, -2.85, 0.0]), scale=0.36,
                  color=MARK, mono=True),
        )
        self.play(Write(vals))
        eq = formula(r"c_P=\sqrt{\frac{\lambda+2\mu}{\rho}},\quad "
                     r"c_S=\sqrt{\frac{\mu}{\rho}}",
                     np.array([-2.4, -2.5, 0.0]), scale=0.6)
        self.play(Write(eq))
        self.play(FadeIn(self.caption(
            "Suyuqlikda mu = 0 — shuning uchun S-to'lqin umuman tarqalmaydi")))
        self.wait(1.5)
        self.play(FadeIn(block))
