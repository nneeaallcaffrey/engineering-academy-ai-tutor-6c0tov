"""SU-30: to'liq hisoblash zanjiri."""
from __future__ import annotations

import numpy as np
from manim import Create, FadeIn, FadeOut, Line, Polygon, Write, VGroup, DOWN, LEFT, RIGHT, UP

from _common import (
    COMPRESS, INK, MARK, MexanikaScene, RULE, TENSION, axis_pair, curve, dashed, dot_at,
    formula, label,
)


class FullChain(MexanikaScene):
    """Beshta fan bitta membranada birlashadi."""

    subject_code = "SU-30"
    scene_title = "To'liq hisoblash zanjiri"

    def construct(self):
        block = self.show_title()

        links = [
            ("NM", r"\sum \vec F = 0", "nazorat = 0", COMPRESS),
            ("MQ", r"\sigma = \frac{6M}{h^2}", "162,76 MPa", TENSION),
            ("TMM", r"\sigma_{vM}", "144,67 MPa", MARK),
            ("PQ", r"D\nabla^4 w = p", "91,8353 mkm", TENSION),
            ("SU", r"\mathbf{K}\mathbf{u} = \mathbf{f}", "xato 1,7e-4 %", COMPRESS),
        ]
        boxes = VGroup()
        for k, (code, tex, val, col) in enumerate(links):
            c = np.array([-5.0 + 2.5 * k, 1.5, 0.0])
            box = Polygon(c + np.array([-1.05, 0.75, 0]), c + np.array([1.05, 0.75, 0]),
                          c + np.array([1.05, -0.75, 0]), c + np.array([-1.05, -0.75, 0]),
                          color=col, stroke_width=2, fill_opacity=0.06)
            self.play(Create(box), run_time=0.35)
            self.play(Write(label(code, c + np.array([0.0, 0.5, 0.0]), scale=0.36,
                                  color=col, mono=True)), run_time=0.2)
            self.play(Write(formula(tex, c + np.array([0.0, 0.0, 0.0]), scale=0.42,
                                    color=INK)), run_time=0.35)
            self.play(Write(label(val, c + np.array([0.0, -0.5, 0.0]), scale=0.3,
                                  color=col, mono=True)), run_time=0.2)
            boxes.add(box)
            if k:
                self.play(Create(Line(c + np.array([-1.45, 0.0, 0]),
                                      c + np.array([-1.1, 0.0, 0]),
                                      color=RULE, stroke_width=2.4)), run_time=0.15)

        # membrana va to'r yaqinlashishi
        O = np.array([-3.4, -1.6, 0.0])
        base = Line(O + LEFT * 1.9, O + RIGHT * 1.9, color=RULE, stroke_width=1.2)
        self.play(Create(base))
        shape = [O + np.array([r, -0.75 * (1 - (r / 1.9) ** 2) ** 2, 0.0])
                 for r in np.linspace(-1.9, 1.9, 120)]
        self.play(Create(curve(shape, color=INK, width=2.6)), run_time=0.8)
        for n in (4, 8):
            xs = np.linspace(-1.9, 1.9, n + 1)
            self.play(FadeIn(VGroup(*[
                dot_at(O + np.array([x, -0.75 * (1 - (x / 1.9) ** 2) ** 2, 0.0]),
                       color=TENSION, r=0.055) for x in xs])), run_time=0.45)
        self.play(Write(label("FEM aniq yechimga yopishadi",
                              O + np.array([0.0, -1.35, 0.0]), scale=0.32, color=TENSION)))

        # validatsiya paneli
        checks = [("h/a = 0,048 < 0,05", True), ("w/h = 0,077 < 0,2", True),
                  ("zaxira 2,45 > 1,5", True), ("siljish 1,05% < 5%", True)]
        for k, (txt, ok) in enumerate(checks):
            p = np.array([1.6, -0.9 - 0.45 * k, 0.0])
            self.add(Polygon(p + np.array([-0.16, 0.13, 0]), p + np.array([0.02, 0.13, 0]),
                             p + np.array([0.02, -0.13, 0]), p + np.array([-0.16, -0.13, 0]),
                             color=COMPRESS if ok else TENSION,
                             stroke_width=1.6, fill_opacity=0.8))
            self.play(Write(label(txt, p + np.array([1.5, 0.0, 0.0]), scale=0.32,
                                  color=INK, mono=True)), run_time=0.3)
        self.play(Write(label("FARAZLAR VALIDATSIYASI", np.array([2.9, -0.4, 0.0]),
                              scale=0.34, color=INK)))

        self.play(Write(label("Sonli yechim benuqson bo'lsa ham, farazlar buzilsa natija yaroqsiz",
                              np.array([0.0, -3.2, 0.0]), scale=0.36, color=TENSION)))
        self.wait(1.6)
        self.play(FadeIn(block))
