"""MQ: kesim usuli va Mor doirasi."""
from __future__ import annotations

import numpy as np
from manim import Arrow, Circle, Create, FadeIn, FadeOut, Line, Polygon, Write, VGroup, DOWN, LEFT, RIGHT, UP

from _common import (
    COMPRESS, INK, MARK, MexanikaScene, RULE, TENSION, dashed, dot_at, formula, hatched, label,
)


class SectionMethodScene(MexanikaScene):
    """Jismni kesamiz — ichki kuchlar tashqi bo'lib chiqadi."""

    subject_code = "MQ-02"
    scene_title = "Kesim usuli"

    def construct(self):
        block = self.show_title()
        A = np.array([-4.5, 0.4, 0.0])
        B = np.array([4.5, 0.4, 0.0])
        bar = Polygon(A + UP * 0.34, B + UP * 0.34, B + DOWN * 0.34, A + DOWN * 0.34,
                      color=INK, stroke_width=2.4, fill_opacity=0.08)
        f1 = Arrow(A + LEFT * 1.3, A, buff=0, color=TENSION, stroke_width=3.4)
        f2 = Arrow(B + RIGHT * 1.3, B, buff=0, color=TENSION, stroke_width=3.4)
        self.play(Create(bar), Create(f1), Create(f2))
        self.play(Write(formula("F", A + LEFT * 1.6, scale=0.55, color=TENSION)),
                  Write(formula("F", B + RIGHT * 1.6, scale=0.55, color=TENSION)))
        self.wait(0.5)

        cut = dashed(np.array([0.4, 1.2, 0.0]), np.array([0.4, -1.2, 0.0]))
        self.play(Create(cut))
        self.play(Write(label("kesim m-m", np.array([0.4, 1.45, 0.0]), scale=0.38, color=MARK)))
        self.wait(0.4)

        left = Polygon(A + UP * 0.34, np.array([0.1, 0.74, 0.0]), np.array([0.1, 0.06, 0.0]),
                       A + DOWN * 0.34, color=INK, stroke_width=2.4, fill_opacity=0.08)
        right = Polygon(np.array([0.7, 0.74, 0.0]), B + UP * 0.34, B + DOWN * 0.34,
                        np.array([0.7, 0.06, 0.0]), color=INK, stroke_width=2.4, fill_opacity=0.08)
        self.play(FadeOut(bar), FadeIn(left), FadeIn(right), run_time=0.8)

        nl = Arrow(np.array([0.1, 0.4, 0.0]), np.array([1.3, 0.4, 0.0]), buff=0,
                   color=COMPRESS, stroke_width=3.4)
        nr = Arrow(np.array([0.7, 0.4, 0.0]), np.array([-0.5, 0.4, 0.0]), buff=0,
                   color=COMPRESS, stroke_width=3.4)
        self.play(Create(nl), Create(nr))
        self.play(Write(formula("N", np.array([1.55, 0.4, 0.0]), scale=0.55, color=COMPRESS)),
                  Write(formula("N", np.array([-0.8, 0.4, 0.0]), scale=0.55, color=COMPRESS)))

        ep = hatched(np.array([-4.5, -2.1, 0.0]), np.array([4.5, -2.1, 0.0]),
                     [1.0] * 12, n=20, scale=0.7)
        self.play(Create(ep), run_time=1.0)
        self.play(Write(label("N epyurasi", np.array([-5.2, -1.7, 0.0]), scale=0.36,
                              color=RULE, mono=True)))
        eq = formula(r"N = F,\qquad \sigma = \frac{N}{A}",
                     np.array([0.0, -3.0, 0.0]), scale=0.65)
        self.play(Write(eq))
        self.play(FadeIn(self.caption(
            "Ichki kuch — kesimning ikki tomoni bir-biriga ta'sir qiladigan kuch")))
        self.wait(1.4)
        self.play(FadeIn(block))


class MohrCircleScene(MexanikaScene):
    """Mor doirasi: kesim burilganda kuchlanishlar qanday o'zgaradi."""

    subject_code = "MQ-19"
    scene_title = "Mor doirasi"

    def construct(self):
        block = self.show_title()
        sx, sy, txy = 120.0, 40.0, 50.0
        c = (sx + sy) / 2
        r = float(np.hypot((sx - sy) / 2, txy))
        s1, s2 = c + r, c - r
        scale = 0.028
        O = np.array([0.6, -0.5, 0.0])

        axes = VGroup(
            Line(O + LEFT * 5.4, O + RIGHT * 4.6, color=INK, stroke_width=2),
            Line(O + DOWN * 2.1, O + UP * 2.4, color=INK, stroke_width=2),
            formula(r"\sigma", O + RIGHT * 4.8, scale=0.5),
            formula(r"\tau", O + UP * 2.6, scale=0.5),
        )
        self.play(Create(axes))

        centre = O + np.array([c * scale, 0.0, 0.0])
        circ = Circle(radius=r * scale, color=INK, stroke_width=2.6).move_to(centre)
        self.play(Create(circ), FadeIn(dot_at(centre, color=RULE)))

        px = O + np.array([sx * scale, txy * scale, 0.0])
        py = O + np.array([sy * scale, -txy * scale, 0.0])
        diam = Line(px, py, color=MARK, stroke_width=2.4)
        self.play(FadeIn(dot_at(px, color=TENSION)), FadeIn(dot_at(py, color=COMPRESS)),
                  Create(diam))
        self.play(Write(label("X", px + UP * 0.28, scale=0.38, color=TENSION)),
                  Write(label("Y", py + DOWN * 0.28, scale=0.38, color=COMPRESS)))

        p1 = O + np.array([s1 * scale, 0.0, 0.0])
        p2 = O + np.array([s2 * scale, 0.0, 0.0])
        self.play(FadeIn(dot_at(p1, color=TENSION, r=0.08)),
                  FadeIn(dot_at(p2, color=COMPRESS, r=0.08)))
        self.play(Write(label(f"sigma_1 = {s1:.1f}", p1 + DOWN * 0.34, scale=0.34,
                              color=TENSION, mono=True)),
                  Write(label(f"sigma_2 = {s2:.1f}", p2 + DOWN * 0.34, scale=0.34,
                              color=COMPRESS, mono=True)))
        tmax = O + np.array([c * scale, r * scale, 0.0])
        self.play(FadeIn(dot_at(tmax, color=MARK, r=0.08)),
                  Write(label(f"tau_max = {r:.1f}", tmax + UP * 0.3, scale=0.34,
                              color=MARK, mono=True)))

        eq = formula(r"\sigma_{1,2} = \frac{\sigma_x+\sigma_y}{2} \pm "
                     r"\sqrt{\left(\frac{\sigma_x-\sigma_y}{2}\right)^2 + \tau_{xy}^2}",
                     np.array([0.0, -2.75, 0.0]), scale=0.58)
        self.play(Write(eq))
        self.play(FadeIn(self.caption(
            "Kesim 2x burchakka burilsa, nuqta doira bo'ylab shuncha buriladi")))
        self.wait(1.5)
        self.play(FadeIn(block))
