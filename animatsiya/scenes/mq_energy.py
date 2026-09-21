"""MQ: deformatsiya energiyasi."""
from __future__ import annotations

import numpy as np
from manim import Create, FadeIn, Line, Polygon, Write, VGroup, DOWN, LEFT, RIGHT, UP

from _common import (
    COMPRESS, INK, MARK, MexanikaScene, RULE, TENSION, axis_pair, curve, dashed, dot_at,
    formula, label,
)


class StrainEnergyScene(MexanikaScene):
    """Diagramma ostidagi yuza — to'plangan energiya."""

    subject_code = "MQ-24"
    scene_title = "Deformatsiya energiyasi"

    def construct(self):
        block = self.show_title()
        O = np.array([-4.6, -2.0, 0.0])
        axes = axis_pair(O, x_len=6.0, y_len=4.4, x_label=r"\Delta", y_label="F")
        self.play(Create(axes))

        k = 1.25
        tip = O + np.array([4.2, 4.2 * k * 0.62, 0.0])
        line = Line(O, tip, color=INK, stroke_width=3)
        self.play(Create(line))

        area = Polygon(O, tip, np.array([tip[0], O[1], 0.0]),
                       color=TENSION, stroke_width=0, fill_opacity=0.18)
        self.play(FadeIn(area))
        for i in range(1, 9):
            x = 4.2 * i / 9
            p0 = O + np.array([x, 0.0, 0.0])
            p1 = O + np.array([x, x * k * 0.62, 0.0])
            self.add(Line(p0, p1, color=TENSION, stroke_width=1.4))

        self.play(Write(label("U = F*Delta/2", O + np.array([1.5, 1.35, 0.0]),
                              scale=0.42, color=TENSION, mono=True)))
        self.play(Create(dashed(tip, np.array([O[0], tip[1], 0.0]))),
                  Create(dashed(tip, np.array([tip[0], O[1], 0.0]))))

        # Kastilyano: yuza bo'yicha hosila siljishni beradi
        note = VGroup(
            formula(r"U = \int_0^{\Delta} F\,d\Delta = \frac{F\Delta}{2}",
                    np.array([2.6, 1.4, 0.0]), scale=0.58),
            formula(r"\Delta = \frac{\partial U}{\partial F}",
                    np.array([2.6, 0.45, 0.0]), scale=0.58, color=MARK),
            formula(r"U = \int \frac{N^2}{2EA}dx + \int \frac{M^2}{2EI}dx"
                    r" + \int \frac{T^2}{2GI_p}dx",
                    np.array([0.4, -2.8, 0.0]), scale=0.55),
        )
        self.play(Write(note[0])); self.play(Write(note[1])); self.play(Write(note[2]))
        self.play(FadeIn(self.caption(
            "Kastilyano teoremasi: energiyaning kuch bo'yicha hosilasi — siljish")))
        self.wait(1.5)
        self.play(FadeIn(block))
