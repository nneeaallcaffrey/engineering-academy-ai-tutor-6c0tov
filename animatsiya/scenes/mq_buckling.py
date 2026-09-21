"""MQ: Eyler ustuvorligi."""
from __future__ import annotations

import numpy as np
from manim import Arrow, Create, FadeIn, Line, Write, VGroup, DOWN, LEFT, RIGHT, UP

from _common import (
    COMPRESS, INK, MARK, MexanikaScene, RULE, TENSION, axis_pair, curve, dashed, dot_at,
    formula, label, sampled,
)


class BucklingScene(MexanikaScene):
    """Kritik kuchdan keyin to'g'ri shakl turg'unligini yo'qotadi."""

    subject_code = "MQ-25"
    scene_title = "Eyler ustuvorligi"

    def construct(self):
        block = self.show_title()

        H = 3.1
        for i, (mu, name, col) in enumerate([(1.0, "sharnir-sharnir", TENSION),
                                             (0.7, "sharnir-qisilgan", MARK),
                                             (0.5, "qisilgan-qisilgan", COMPRESS),
                                             (2.0, "konsol", RULE)]):
            x0 = -5.2 + 2.1 * i
            base = np.array([x0, -1.9, 0.0])
            amp = 0.34
            pts = []
            for t in np.linspace(0.0, 1.0, 80):
                # mu ga mos yarim to'lqin shakli
                y = base[1] + H * t
                d = amp * np.sin(np.pi * t / mu) if mu >= 1.0 else \
                    amp * (1 - np.cos(2 * np.pi * t)) / 2 * np.sign(np.sin(np.pi * t))
                pts.append(np.array([x0 + d, y, 0.0]))
            self.play(Create(curve(pts, color=col, width=3)), run_time=0.7)
            self.play(Create(Arrow(np.array([x0, base[1] + H + 0.95, 0.0]),
                                   np.array([x0, base[1] + H + 0.12, 0.0]),
                                   buff=0, color=col, stroke_width=3)), run_time=0.3)
            self.play(Write(label(f"mu = {mu}", np.array([x0, -2.25, 0.0]),
                                  scale=0.34, color=col, mono=True)),
                      Write(label(name, np.array([x0, -2.6, 0.0]), scale=0.28, color=RULE)),
                      run_time=0.35)

        eq = formula(r"P_{cr} = \frac{\pi^2 EI}{(\mu L)^2},\qquad "
                     r"\lambda = \frac{\mu L}{i}",
                     np.array([0.0, 2.35, 0.0]), scale=0.68)
        self.play(Write(eq))
        self.play(FadeIn(self.caption(
            "Mahkamlash usuli keltirilgan uzunlikni, u esa kritik kuchni belgilaydi")))
        self.wait(1.5)
        self.play(FadeIn(block))
