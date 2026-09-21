"""NM: erkin jism diagrammasi."""
from __future__ import annotations

import numpy as np
from manim import Arrow, Create, FadeIn, FadeOut, Line, Polygon, Write, VGroup, DOWN, LEFT, RIGHT, UP

from _common import COMPRESS, INK, MARK, MexanikaScene, RULE, TENSION, dashed, formula, label


class FreeBodyScene(MexanikaScene):
    """Jismni ajratamiz, bog'lanishlarni reaksiya bilan almashtiramiz."""

    subject_code = "NM-07"
    scene_title = "Erkin jism diagrammasi va Nyuton tenglamasi"

    def construct(self):
        block = self.show_title()
        alpha = 24 * np.pi / 180

        # qiya tekislik
        A = np.array([-4.6, -2.0, 0.0])
        B = np.array([2.4, -2.0, 0.0])
        C = B + np.array([0.0, float(np.tan(alpha)) * 7.0, 0.0]) * 0.0
        top = A + np.array([7.0 * np.cos(alpha), 7.0 * np.sin(alpha), 0.0])
        incline = Polygon(A, B, top, color=RULE, stroke_width=2, fill_opacity=0.07)
        self.play(Create(incline))

        centre = A + np.array([3.4 * np.cos(alpha), 3.4 * np.sin(alpha), 0.0]) \
            + np.array([-np.sin(alpha), np.cos(alpha), 0.0]) * 0.42
        box = Polygon(*[centre + np.array([dx * np.cos(alpha) - dy * np.sin(alpha),
                                           dx * np.sin(alpha) + dy * np.cos(alpha), 0.0])
                        for dx, dy in ((-0.42, -0.42), (0.42, -0.42), (0.42, 0.42), (-0.42, 0.42))],
                     color=INK, stroke_width=2.4, fill_opacity=0.1)
        self.play(Create(box))
        self.wait(0.4)

        self.play(FadeOut(incline), run_time=0.8)      # jismni AJRATAMIZ

        n_dir = np.array([-np.sin(alpha), np.cos(alpha), 0.0])
        t_dir = np.array([np.cos(alpha), np.sin(alpha), 0.0])
        forces = [
            (np.array([0.0, -1.7, 0.0]), "mg", COMPRESS),
            (n_dir * 1.55, "N", TENSION),
            (-t_dir * 0.95, "f", MARK),
        ]
        for vec, name, col in forces:
            a = Arrow(centre, centre + vec, buff=0, color=col, stroke_width=3.4)
            t = formula(name, centre + vec * 1.22, scale=0.55, color=col)
            self.play(Create(a), Write(t), run_time=0.7)

        ax = dashed(centre - t_dir * 1.9, centre + t_dir * 1.9)
        an = dashed(centre - n_dir * 0.5, centre + n_dir * 2.1)
        self.play(Create(ax), Create(an))

        eqs = VGroup(
            formula(r"\sum F_t = mg\sin\alpha - f = m\,a", np.array([0.0, 1.55, 0.0]), scale=0.6),
            formula(r"\sum F_n = N - mg\cos\alpha = 0", np.array([0.0, 0.95, 0.0]), scale=0.6),
        )
        self.play(Write(eqs))
        self.play(FadeIn(self.caption(
            "Bog'lanish olib tashlanadi va uning o'rniga reaksiya qo'yiladi")))
        self.wait(1.5)
        self.play(FadeIn(block))
