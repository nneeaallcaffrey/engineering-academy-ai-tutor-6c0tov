"""MQ: val buralishi."""
from __future__ import annotations

import numpy as np
from manim import Arrow, Circle, Create, FadeIn, Line, Write, VGroup, DOWN, LEFT, RIGHT, UP

from _common import (
    COMPRESS, INK, MARK, MexanikaScene, RULE, TENSION, curve, dashed, dot_at, formula, label,
)


class TorsionScene(MexanikaScene):
    """Urinma kuchlanish radius bo'ylab chiziqli o'sadi."""

    subject_code = "MQ-10"
    scene_title = "Val buralishi va kuchlanish taqsimoti"

    def construct(self):
        block = self.show_title()

        c = np.array([-3.3, 0.2, 0.0])
        R = 1.5
        outer = Circle(radius=R, color=INK, stroke_width=2.6).move_to(c)
        self.play(Create(outer))

        # radial chiziqlar burilishi
        for a in np.linspace(0, 2 * np.pi, 9)[:-1]:
            self.add(Line(c, c + np.array([np.cos(a), np.sin(a), 0.0]) * R,
                          color=RULE, stroke_width=1.2))
        rad0 = Line(c, c + RIGHT * R, color=COMPRESS, stroke_width=3)
        phi = 0.55
        rad1 = Line(c, c + np.array([np.cos(phi), np.sin(phi), 0.0]) * R,
                    color=TENSION, stroke_width=3)
        self.play(Create(rad0))
        self.play(Create(rad1))
        self.play(Write(formula(r"\varphi", c + np.array([1.0, 0.36, 0.0]),
                                scale=0.5, color=TENSION)))

        # kuchlanish epyurasi: tau = T r / Ip
        O = np.array([1.4, -1.6, 0.0])
        ax = VGroup(Line(O, O + UP * 3.2, color=INK, stroke_width=2),
                    Line(O, O + RIGHT * 4.4, color=INK, stroke_width=2),
                    formula(r"\tau", O + RIGHT * 4.6, scale=0.5),
                    formula("r", O + UP * 3.4, scale=0.5))
        self.play(Create(ax))
        tri = curve([O, O + np.array([3.6, 3.0, 0.0])], color=TENSION, width=3)
        self.play(Create(tri))
        for k in range(1, 8):
            y = 3.0 * k / 7
            self.add(Line(O + np.array([0.0, y, 0.0]),
                          O + np.array([3.6 * k / 7, y, 0.0]),
                          color=TENSION, stroke_width=1.6))
        self.play(Write(label("tau_max = T R / Ip", O + np.array([1.1, 3.25, 0.0]),
                              scale=0.36, color=TENSION, mono=True)))
        self.play(Write(label("markazda tau = 0", O + np.array([1.5, -0.35, 0.0]),
                              scale=0.34, color=RULE, mono=True)))

        eq = formula(r"\tau = \frac{T\,r}{I_p},\qquad "
                     r"\varphi = \frac{T\,L}{G\,I_p}",
                     np.array([-3.3, -2.5, 0.0]), scale=0.62)
        self.play(Write(eq))
        self.play(FadeIn(self.caption(
            "Material markazda deyarli ishlamaydi — shuning uchun quvur samaraliroq")))
        self.wait(1.5)
        self.play(FadeIn(block))
