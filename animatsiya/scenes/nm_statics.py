"""NM: fermada kuchlarning taqsimlanishi."""
from __future__ import annotations

import numpy as np
from manim import Create, FadeIn, Line, Write, VGroup, DOWN, RIGHT, UP

from _common import (
    COMPRESS, INK, MexanikaScene, RULE, TENSION, dot_at, formula, label, support_pin,
)


class TrussForceScene(MexanikaScene):
    """Har bir sterjen cho'zilish yoki siqilishda ekani rang bilan ko'rsatiladi."""

    subject_code = "NM-11"
    scene_title = "Fermada kuchlarning taqsimlanishi"

    def construct(self):
        block = self.show_title()

        span, h = 6.0, 1.7
        n_bay = 3
        bot = [np.array([-span / 2 + span * i / n_bay, -1.0, 0.0]) for i in range(n_bay + 1)]
        top = [np.array([-span / 2 + span * (i + 0.5) / n_bay, -1.0 + h, 0.0])
               for i in range(n_bay)]

        bars = []
        for i in range(n_bay):
            bars.append((bot[i], bot[i + 1], +1))         # pastki pister — cho'ziladi
        for i in range(n_bay - 1):
            bars.append((top[i], top[i + 1], -1))         # yuqorigi — siqiladi
        for i in range(n_bay):
            bars.append((bot[i], top[i], -1))
            bars.append((top[i], bot[i + 1], -1))

        nodes = VGroup(*[dot_at(p, color=INK, r=0.06) for p in bot + top])
        frame = VGroup(*[Line(a, b, color=RULE, stroke_width=2.5) for a, b, _ in bars])
        self.play(Create(frame), FadeIn(nodes), run_time=1.6)

        sup = VGroup(support_pin(bot[0]), support_pin(bot[-1]))
        self.play(Create(sup))

        # yuk: o'rtadagi yuqori tugunga
        p_load = top[n_bay // 2]
        arrow = Line(p_load + UP * 1.2, p_load, color=COMPRESS, stroke_width=3.5)
        self.play(Create(arrow), Write(label("P", p_load + UP * 1.35, scale=0.45,
                                             color=COMPRESS)))

        coloured = VGroup()
        for a, b, sgn in bars:
            coloured.add(Line(a, b, color=TENSION if sgn > 0 else COMPRESS,
                              stroke_width=4.4 if sgn > 0 else 3.4))
        self.play(Create(coloured), run_time=1.8)

        leg = VGroup(
            Line(np.array([-5.6, -2.55, 0.0]), np.array([-5.0, -2.55, 0.0]),
                 color=TENSION, stroke_width=4.4),
            label("cho'zilish", np.array([-4.1, -2.55, 0.0]), scale=0.36, color=TENSION),
            Line(np.array([-2.9, -2.55, 0.0]), np.array([-2.3, -2.55, 0.0]),
                 color=COMPRESS, stroke_width=3.4),
            label("siqilish", np.array([-1.5, -2.55, 0.0]), scale=0.36, color=COMPRESS),
        )
        self.play(FadeIn(leg))
        eq = formula(r"\sum \vec F = 0 \ \text{(har bir tugunda)}",
                     np.array([2.6, -2.55, 0.0]), scale=0.55)
        self.play(Write(eq))
        self.play(FadeIn(self.caption(
            "Pastki pister cho'ziladi, ravoq va tirgaklar siqiladi")))
        self.wait(1.5)
        self.play(FadeIn(block))
