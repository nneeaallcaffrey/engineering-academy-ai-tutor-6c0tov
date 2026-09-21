"""TMM: yoriq uchidagi kuchlanish maydoni."""
from __future__ import annotations

import numpy as np
from manim import Create, FadeIn, Line, Polygon, Write, VGroup, DOWN, LEFT, RIGHT, UP

from _common import (
    COMPRESS, INK, MARK, MexanikaScene, RULE, TENSION, axis_pair, curve, dashed, dot_at,
    formula, label, sampled,
)


class CrackTipScene(MexanikaScene):
    """1/sqrt(r) maxsusligi: chekli emas, lekin integrallanadi."""

    subject_code = "TMM-24"
    scene_title = "Yoriq uchidagi kuchlanish maydoni"

    def construct(self):
        block = self.show_title()

        plate = Polygon(np.array([-5.6, 1.9, 0.0]), np.array([-0.4, 1.9, 0.0]),
                        np.array([-0.4, -1.5, 0.0]), np.array([-5.6, -1.5, 0.0]),
                        color=RULE, stroke_width=2, fill_opacity=0.05)
        crack = Line(np.array([-5.6, 0.2, 0.0]), np.array([-2.6, 0.2, 0.0]),
                     color=INK, stroke_width=4)
        tip = dot_at(np.array([-2.6, 0.2, 0.0]), color=TENSION, r=0.09)
        self.play(Create(plate), Create(crack), FadeIn(tip))
        self.play(Write(label("yoriq uchi", np.array([-2.6, -0.2, 0.0]),
                              scale=0.34, color=TENSION)))

        for y in (1.9, -1.5):
            for x in np.linspace(-5.2, -0.8, 6):
                d = 0.45 if y > 0 else -0.45
                self.add(Line(np.array([x, y, 0.0]), np.array([x, y + d, 0.0]),
                              color=COMPRESS, stroke_width=2))
        self.play(Write(label("sigma", np.array([-3.0, 2.6, 0.0]), scale=0.4,
                              color=COMPRESS)))

        O = np.array([0.6, -1.5, 0.0])
        axes = axis_pair(O, x_len=5.2, y_len=3.9, x_label="r", y_label=r"\sigma_{yy}")
        self.play(Create(axes))

        K = 1.0
        def sig(r):
            return K / np.sqrt(2 * np.pi * max(r, 1e-4))
        pts = sampled(sig, 0.012, 1.4, n=200, sx=3.4, sy=0.42, origin=O)
        pts = [p for p in pts if p[1] - O[1] < 3.7]
        self.play(Create(curve(pts, color=TENSION, width=2.8)), run_time=1.3)

        self.play(Write(label("sigma ~ K / sqrt(2 pi r)", O + np.array([2.2, 2.9, 0.0]),
                              scale=0.36, color=TENSION, mono=True)))
        zone = dashed(O + np.array([0.42, 0.0, 0.0]), O + np.array([0.42, 3.6, 0.0]))
        self.play(Create(zone), Write(label("plastik zona", O + np.array([1.1, 3.35, 0.0]),
                                            scale=0.32, color=MARK)))

        eq = VGroup(
            formula(r"\sigma_{ij} = \frac{K_I}{\sqrt{2\pi r}}\,f_{ij}(\theta)",
                    np.array([-3.0, -2.5, 0.0]), scale=0.6),
            formula(r"K_I = Y\sigma\sqrt{\pi a}", np.array([2.6, -2.5, 0.0]), scale=0.6,
                    color=MARK),
        )
        self.play(Write(eq[0])); self.play(Write(eq[1]))
        self.play(FadeIn(self.caption(
            "Kuchlanish cheksizga intiladi, lekin energiya chekli — mezon shundan")))
        self.wait(1.5)
        self.play(FadeIn(block))
