"""TMM: Koshi tetraedri."""
from __future__ import annotations

import numpy as np
from manim import Arrow, Create, FadeIn, Line, Polygon, Write, VGroup, DOWN, LEFT, RIGHT, UP

from _common import (
    COMPRESS, INK, MARK, MexanikaScene, RULE, TENSION, dashed, dot_at, formula, label,
)


class CauchyTetrahedronScene(MexanikaScene):
    """Uch yuzdagi kuchlanish to'rtinchi yuzdagisini belgilaydi."""

    subject_code = "TMM-07"
    scene_title = "Koshi tetraedri"

    def construct(self):
        block = self.show_title()

        # izometrik proyeksiya
        O = np.array([-1.2, -1.5, 0.0])
        ex = np.array([2.6, -0.85, 0.0])
        ey = np.array([2.5, 1.0, 0.0])
        ez = np.array([0.0, 2.7, 0.0])
        A, B, C = O + ex, O + ey, O + ez

        edges = VGroup(
            Line(O, A, color=RULE, stroke_width=2), Line(O, B, color=RULE, stroke_width=2),
            Line(O, C, color=RULE, stroke_width=2),
            Line(A, B, color=INK, stroke_width=2.4), Line(B, C, color=INK, stroke_width=2.4),
            Line(A, C, color=INK, stroke_width=2.4),
        )
        self.play(Create(edges), run_time=1.3)
        face = Polygon(A, B, C, color=MARK, stroke_width=2, fill_opacity=0.14)
        self.play(FadeIn(face))

        lbl = VGroup(label("x", A + np.array([0.24, -0.2, 0.0]), scale=0.4),
                     label("y", B + np.array([0.26, 0.05, 0.0]), scale=0.4),
                     label("z", C + np.array([-0.05, 0.26, 0.0]), scale=0.4))
        self.play(Write(lbl))

        centre = (A + B + C) / 3
        n = Arrow(centre, centre + np.array([0.95, 0.72, 0.0]), buff=0,
                  color=MARK, stroke_width=3.2)
        t = Arrow(centre, centre + np.array([1.25, 0.15, 0.0]), buff=0,
                  color=TENSION, stroke_width=3.4)
        self.play(Create(n), Create(t))
        self.play(Write(formula(r"\vec n", centre + np.array([1.15, 0.92, 0.0]),
                                scale=0.5, color=MARK)),
                  Write(formula(r"\vec t^{(n)}", centre + np.array([1.7, 0.1, 0.0]),
                                scale=0.5, color=TENSION)))

        for p, col, name in ((O + ex * 0.5 + ey * 0.12, COMPRESS, r"\sigma_{xx}"),
                             (O + ey * 0.5 + ez * 0.1, COMPRESS, r"\sigma_{yy}"),
                             (O + ez * 0.5 + ex * 0.1, COMPRESS, r"\sigma_{zz}")):
            self.play(Create(Arrow(p, p + np.array([-0.62, -0.28, 0.0]), buff=0,
                                   color=col, stroke_width=2.4)), run_time=0.3)

        eq = VGroup(
            formula(r"t^{(n)}_i = \sigma_{ij} n_j", np.array([3.6, 1.1, 0.0]), scale=0.68),
            formula(r"\sum \vec F = 0 \ \Rightarrow\ "
                    r"\vec t^{(n)}dA = \sum \vec t^{(k)}dA_k",
                    np.array([3.0, 0.2, 0.0]), scale=0.5),
        )
        self.play(Write(eq[0])); self.play(Write(eq[1]))
        self.play(FadeIn(self.caption(
            "Tetraedr kichrayganda hajmiy kuchlar yuza kuchlariga nisbatan yo'qoladi")))
        self.wait(1.5)
        self.play(FadeIn(block))
