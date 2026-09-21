"""NM: potensial chuqurcha va energiya saqlanishi."""
from __future__ import annotations

import numpy as np
from manim import Create, FadeIn, Line, Write, VGroup, DOWN, LEFT, RIGHT, UP

from _common import (
    COMPRESS, INK, MARK, MexanikaScene, RULE, TENSION, axis_pair, curve, dashed, dot_at,
    formula, label, sampled,
)


class PotentialWellScene(MexanikaScene):
    """To'liq energiya chizig'i harakat sohasini kesib beradi."""

    subject_code = "NM-15"
    scene_title = "Potensial chuqurcha va energiya saqlanishi"

    def construct(self):
        block = self.show_title()
        O = np.array([-4.8, -2.1, 0.0])
        axes = axis_pair(O, x_len=9.4, y_len=4.5, x_label="x", y_label="U(x)")
        self.play(Create(axes))

        def U(x):
            return 0.55 * (0.25 * x**4 - 1.6 * x**2 + 2.6)

        pts = sampled(U, -2.9, 2.9, n=140, sx=1.5, sy=0.62,
                      origin=O + np.array([4.35, 0.15, 0.0]))
        well = curve(pts, color=INK, width=2.8)
        self.play(Create(well), run_time=1.6)

        for E, col in ((0.62, TENSION), (1.55, COMPRESS)):
            y = O[1] + 0.15 + E * 0.62
            lvl = Line(np.array([O[0] + 0.1, y, 0.0]), np.array([O[0] + 9.1, y, 0.0]),
                       color=col, stroke_width=2.4)
            tl = label(f"E = {E:.2f}", np.array([O[0] + 9.2, y, 0.0]), scale=0.36, color=col)

            # burilish nuqtalari: U(x) = E
            xs = np.linspace(-2.9, 2.9, 2000)
            sign = np.sign(U(xs) - E)
            roots = [xs[i] for i in range(len(xs) - 1) if sign[i] != sign[i + 1]]
            marks = VGroup(*[
                dot_at(O + np.array([4.35 + r * 1.5, 0.15 + U(r) * 0.62, 0.0]), color=col)
                for r in roots])
            self.play(Create(lvl), Write(tl), FadeIn(marks), run_time=0.9)
            if roots:
                note = label(f"{len(roots)} ta burilish nuqtasi",
                             np.array([O[0] + 2.4, y + 0.3, 0.0]), scale=0.33,
                             color=col, mono=True)
                self.play(Write(note), run_time=0.5)
            self.wait(0.5)

        eq = formula(r"E = T + U = \text{const},\qquad F = -\frac{dU}{dx}",
                     np.array([0.0, 2.55, 0.0]), scale=0.68)
        self.play(Write(eq))
        self.play(FadeIn(self.caption(
            "Past energiyada harakat bitta chuqurchada qamalgan, yuqorida — erkin")))
        self.wait(1.5)
        self.play(FadeIn(block))
