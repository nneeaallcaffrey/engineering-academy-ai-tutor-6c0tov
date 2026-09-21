"""TMM: tenzorning koordinata almashtirishdagi xatti-harakati."""
from __future__ import annotations

import numpy as np
from manim import Arrow, Create, FadeIn, FadeOut, Line, Write, VGroup, DOWN, LEFT, RIGHT, UP

from _common import (
    COMPRESS, INK, MARK, MexanikaScene, RULE, TENSION, curve, dot_at, formula, label,
)


class TensorTransformScene(MexanikaScene):
    """Komponentalar o'zgaradi, invariantlar o'zgarmaydi."""

    subject_code = "TMM-02"
    scene_title = "Tenzorning koordinata almashtirishda o'zgarishi"

    def construct(self):
        block = self.show_title()
        S = np.array([[120.0, 50.0], [50.0, 40.0]])
        c = np.array([-3.2, -0.1, 0.0])

        sq = VGroup(*[Line(c + np.array(a), c + np.array(b), color=INK, stroke_width=2)
                      for a, b in (((-1.1, -1.1, 0), (1.1, -1.1, 0)),
                                   ((1.1, -1.1, 0), (1.1, 1.1, 0)),
                                   ((1.1, 1.1, 0), (-1.1, 1.1, 0)),
                                   ((-1.1, 1.1, 0), (-1.1, -1.1, 0)))])
        self.play(Create(sq))

        inv1 = np.trace(S)
        inv2 = float(np.linalg.det(S))
        vals = np.linalg.eigvalsh(S)

        rows = VGroup()
        for k, th_deg in enumerate((0.0, 20.0, 45.0, 31.7)):
            th = np.radians(th_deg)
            Q = np.array([[np.cos(th), np.sin(th)], [-np.sin(th), np.cos(th)]])
            Sp = Q @ S @ Q.T
            axes = VGroup(
                Arrow(c, c + np.array([np.cos(th), np.sin(th), 0.0]) * 1.7, buff=0,
                      color=TENSION, stroke_width=3),
                Arrow(c, c + np.array([-np.sin(th), np.cos(th), 0.0]) * 1.7, buff=0,
                      color=COMPRESS, stroke_width=3),
            )
            txt = label(
                f"th={th_deg:4.1f}  s11={Sp[0,0]:6.1f}  s22={Sp[1,1]:6.1f}  s12={Sp[0,1]:6.1f}",
                np.array([2.4, 1.6 - 0.5 * k, 0.0]), scale=0.32,
                color=MARK if abs(Sp[0, 1]) < 0.5 else INK, mono=True)
            self.play(Create(axes), Write(txt), run_time=0.8)
            rows.add(txt)
            if k < 3:
                self.play(FadeOut(axes), run_time=0.25)

        inv = VGroup(
            label(f"I1 = s11 + s22 = {inv1:.1f}  (o'zgarmaydi)",
                  np.array([1.4, -1.35, 0.0]), scale=0.34, color=TENSION, mono=True),
            label(f"I2 = det = {inv2:.1f}  (o'zgarmaydi)",
                  np.array([1.4, -1.75, 0.0]), scale=0.34, color=TENSION, mono=True),
            label(f"bosh qiymatlar: {vals[1]:.1f}, {vals[0]:.1f}",
                  np.array([1.4, -2.15, 0.0]), scale=0.34, color=COMPRESS, mono=True),
        )
        self.play(Write(inv))
        eq = formula(r"\sigma'_{ij} = Q_{ik}Q_{jl}\sigma_{kl}",
                     np.array([-3.2, -2.55, 0.0]), scale=0.62)
        self.play(Write(eq))
        self.play(FadeIn(self.caption(
            "31,7 gradusda siljish nolga aylanadi — bu bosh o'qlar")))
        self.wait(1.5)
        self.play(FadeIn(block))
