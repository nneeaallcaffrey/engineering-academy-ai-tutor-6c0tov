"""NM: vektor algebrasi va moment."""
from __future__ import annotations

import numpy as np
from manim import (
    Arrow, Create, FadeIn, GrowArrow, Line, Polygon, Write, VGroup, ORIGIN, RIGHT, UP, DOWN, LEFT,
)

from _common import COMPRESS, INK, MARK, MexanikaScene, RULE, TENSION, dashed, dot_at, formula, label


class VectorMomentScene(MexanikaScene):
    """M = r x F: yelka uzunligi o'zgarganda moment qanday o'zgaradi."""

    subject_code = "NM-01"
    scene_title = "Vektor ko'paytma va moment"

    def construct(self):
        block = self.show_title()
        O = np.array([-3.4, -1.1, 0.0])
        pivot = dot_at(O, color=INK, r=0.07)
        pl = label("O", O + DOWN * 0.3, scale=0.4)
        self.play(FadeIn(pivot), Write(pl))

        for k, (tip, color) in enumerate([
            (O + np.array([3.6, 0.0, 0.0]), TENSION),
            (O + np.array([3.6, 1.6, 0.0]), COMPRESS),
        ]):
            r_vec = Arrow(O, tip, buff=0, color=RULE, stroke_width=3)
            r_lab = formula(r"\vec r", (O + tip) / 2 + DOWN * 0.35, scale=0.5, color=RULE)
            F = np.array([0.0, -1.7, 0.0])
            f_vec = Arrow(tip, tip + F, buff=0, color=color, stroke_width=3.4)
            f_lab = formula(r"\vec F", tip + F + DOWN * 0.24, scale=0.5, color=color)

            # yelka: O dan F ning ta'sir chizig'igacha perpendikulyar masofa
            foot = np.array([tip[0], O[1], 0.0])
            arm = dashed(O, foot)
            arm_lab = formula("d", (O + foot) / 2 + UP * 0.22, scale=0.5, color=MARK)

            self.play(GrowArrow(r_vec), Write(r_lab), run_time=0.7)
            self.play(GrowArrow(f_vec), Write(f_lab), run_time=0.7)
            self.play(Create(arm), Write(arm_lab), run_time=0.6)

            # moment yuzasi: parallelogramm |r x F|
            par = Polygon(O, tip, tip + F, O + F, color=color,
                          stroke_width=1.6, fill_opacity=0.12)
            self.play(FadeIn(par), run_time=0.6)
            m = float(abs(np.cross(tip - O, F)[2]))
            mt = label(f"|M| = {m:.2f}", np.array([2.9, 2.0 - 0.6 * k, 0.0]),
                       scale=0.42, color=color, mono=True)
            self.play(Write(mt), run_time=0.5)
            self.wait(0.6)
            if k == 0:
                self.play(*[FadeIn(x) for x in ()], run_time=0.1)
                self.remove(par, r_vec, f_vec, r_lab, f_lab, arm, arm_lab)

        eq = formula(r"\vec M = \vec r \times \vec F,\qquad |M| = |F|\,d",
                     np.array([0.0, -2.6, 0.0]), scale=0.68)
        self.play(Write(eq))
        cap = self.caption("Moment — parallelogramm yuzasi: yelka o'zgarsa, yuza ham o'zgaradi")
        self.play(FadeIn(cap))
        self.wait(1.5)
        self.play(FadeIn(block))
