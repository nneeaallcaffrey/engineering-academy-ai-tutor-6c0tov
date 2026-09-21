"""TMM: minimal potensial energiya prinsipi."""
from __future__ import annotations

import numpy as np
from manim import Create, FadeIn, Line, Write, VGroup, DOWN, LEFT, RIGHT, UP

from _common import (
    COMPRESS, INK, MARK, MexanikaScene, RULE, TENSION, axis_pair, curve, dashed, dot_at,
    formula, label, sampled,
)


class VariationalScene(MexanikaScene):
    """Haqiqiy yechim — energiyani minimallashtiradigan funksiya."""

    subject_code = "TMM-19"
    scene_title = "Minimal potensial energiya prinsipi"

    def construct(self):
        block = self.show_title()

        # chapda: sinov funksiyalari
        A = np.array([-5.6, 1.4, 0.0])
        B = np.array([-0.6, 1.4, 0.0])
        base = Line(A, B, color=RULE, stroke_width=1.6)
        self.play(Create(base))

        exact = [A + np.array([5.0 * t, -1.1 * np.sin(np.pi * t), 0.0])
                 for t in np.linspace(0, 1, 90)]
        trials = []
        for a, col in ((0.55, COMPRESS), (1.45, MARK)):
            trials.append([A + np.array([5.0 * t, -1.1 * a * (t - t * t) * 4, 0.0])
                           for t in np.linspace(0, 1, 90)])
        self.play(Create(curve(trials[0], color=COMPRESS, width=2)),
                  Create(curve(trials[1], color=MARK, width=2)), run_time=1.0)
        self.play(Create(curve(exact, color=TENSION, width=3)), run_time=0.9)
        self.play(Write(label("haqiqiy yechim", A + np.array([2.4, -1.75, 0.0]),
                              scale=0.34, color=TENSION)))

        # o'ngda: energiya funksionali
        O = np.array([1.4, -1.9, 0.0])
        axes = axis_pair(O, x_len=4.6, y_len=4.0, x_label="a", y_label=r"\Pi")
        self.play(Create(axes))

        def Pi(a):
            return 1.35 * (a - 1.0) ** 2 + 0.55
        pts = sampled(Pi, 0.0, 2.2, n=120, sx=1.9, sy=1.05, origin=O)
        self.play(Create(curve(pts, color=INK, width=2.8)), run_time=1.0)

        mn = O + np.array([1.0 * 1.9, Pi(1.0) * 1.05, 0.0])
        self.play(FadeIn(dot_at(mn, color=TENSION, r=0.09)),
                  Create(dashed(mn, np.array([mn[0], O[1], 0.0]))))
        self.play(Write(label("minimum", mn + np.array([0.9, 0.25, 0.0]),
                              scale=0.36, color=TENSION)))

        eq = VGroup(
            formula(r"\Pi = U - W", np.array([0.0, 2.55, 0.0]), scale=0.68),
            formula(r"\delta \Pi = 0", np.array([3.2, 2.55, 0.0]), scale=0.68, color=TENSION),
            formula(r"\Pi(\text{sinov}) \ge \Pi(\text{haqiqiy})",
                    np.array([0.0, -3.1, 0.0]), scale=0.58),
        )
        self.play(Write(eq[0])); self.play(Write(eq[1])); self.play(Write(eq[2]))
        self.play(FadeIn(self.caption(
            "Har qanday mos sinov funksiyasi energiyani YUQORIDAN baholaydi")))
        self.wait(1.5)
        self.play(FadeIn(block))
