"""NM: turg'unlik va bifurkatsiya."""
from __future__ import annotations

import numpy as np
from manim import Create, FadeIn, Line, Write, VGroup, DOWN, LEFT, RIGHT, UP

from _common import (
    COMPRESS, INK, MARK, MexanikaScene, RULE, TENSION, axis_pair, curve, dot_at, formula, label,
)


class BifurcationScene(MexanikaScene):
    """Vilkasimon bifurkatsiya: bitta turg'un holat uchtaga bo'linadi."""

    subject_code = "NM-30"
    scene_title = "Turg'unlik va bifurkatsiya"

    def construct(self):
        block = self.show_title()
        O = np.array([-1.6, -1.2, 0.0])
        axes = VGroup(
            Line(O + LEFT * 3.0, O + RIGHT * 4.4, color=INK, stroke_width=2),
            Line(O + DOWN * 1.5, O + UP * 2.6, color=INK, stroke_width=2),
            formula(r"\mu", O + RIGHT * 4.6, scale=0.5),
            formula("x^*", O + UP * 2.8, scale=0.5),
        )
        self.play(Create(axes))

        sx, sy = 1.5, 1.05
        # turg'un tarmoq mu < 0 da x = 0
        stable0 = curve([O + np.array([m * sx, 0.0, 0.0]) for m in np.linspace(-2.0, 0.0, 40)],
                        color=COMPRESS, width=3)
        # mu > 0 da x = 0 turg'unligini yo'qotadi
        unstable0 = curve([O + np.array([m * sx, 0.0, 0.0]) for m in np.linspace(0.0, 2.8, 40)],
                          color=TENSION, width=2)
        up = curve([O + np.array([m * sx, np.sqrt(m) * sy, 0.0])
                    for m in np.linspace(0.0, 2.8, 80)], color=COMPRESS, width=3)
        dn = curve([O + np.array([m * sx, -np.sqrt(m) * sy, 0.0])
                    for m in np.linspace(0.0, 2.8, 80)], color=COMPRESS, width=3)

        self.play(Create(stable0), run_time=0.9)
        self.play(Create(unstable0), run_time=0.7)
        self.play(Create(up), Create(dn), run_time=1.3)
        self.play(FadeIn(dot_at(O, color=MARK, r=0.09)),
                  Write(label("bifurkatsiya nuqtasi", O + np.array([0.1, -0.55, 0.0]),
                              scale=0.34, color=MARK)))

        leg = VGroup(
            Line(np.array([-6.0, 2.4, 0.0]), np.array([-5.4, 2.4, 0.0]),
                 color=COMPRESS, stroke_width=3),
            label("turg'un", np.array([-4.7, 2.4, 0.0]), scale=0.35, color=COMPRESS),
            Line(np.array([-6.0, 1.95, 0.0]), np.array([-5.4, 1.95, 0.0]),
                 color=TENSION, stroke_width=2),
            label("noturg'un", np.array([-4.6, 1.95, 0.0]), scale=0.35, color=TENSION),
        )
        self.play(FadeIn(leg))
        eq = formula(r"\dot x = \mu x - x^3", np.array([3.0, 2.3, 0.0]), scale=0.65)
        self.play(Write(eq))
        self.play(FadeIn(self.caption(
            "Kritik qiymatdan keyin eski holat turg'unligini yo'qotadi")))
        self.wait(1.5)
        self.play(FadeIn(block))
