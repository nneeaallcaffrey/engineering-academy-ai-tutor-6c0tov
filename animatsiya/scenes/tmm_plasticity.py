"""TMM: oqish yuzalari va mustahkamlanish."""
from __future__ import annotations

import numpy as np
from manim import Create, FadeIn, FadeOut, Line, Polygon, Write, VGroup, DOWN, LEFT, RIGHT, UP

from _common import (
    COMPRESS, INK, MARK, MexanikaScene, RULE, TENSION, axis_pair, curve, dashed, dot_at,
    formula, label,
)


def _mises_ellipse(sy, n=180):
    """Tekis kuchlanishda Mizes: s1^2 - s1 s2 + s2^2 = sy^2."""
    th = np.linspace(0, 2 * np.pi, n)
    # parametrik: aylananing 45 gradusga burilgan va cho'zilgan ko'rinishi
    a = sy * np.sqrt(2.0)
    b = sy * np.sqrt(2.0 / 3.0)
    x = a * np.cos(th) / np.sqrt(2) - b * np.sin(th) / np.sqrt(2)
    y = a * np.cos(th) / np.sqrt(2) + b * np.sin(th) / np.sqrt(2)
    return x, y


class YieldSurfaceScene(MexanikaScene):
    """Mizes ellipsi va Treska olti burchagi — ikkalasi ham bir o'qda mos."""

    subject_code = "TMM-21"
    scene_title = "Mizes silindri va Treska prizmasi"

    def construct(self):
        block = self.show_title()
        O = np.array([0.0, -0.3, 0.0])
        sy = 1.0
        s = 1.7
        axes = VGroup(
            Line(O + LEFT * 3.4, O + RIGHT * 3.4, color=INK, stroke_width=2),
            Line(O + DOWN * 2.3, O + UP * 2.3, color=INK, stroke_width=2),
            formula(r"\sigma_1", O + RIGHT * 3.6, scale=0.5),
            formula(r"\sigma_2", O + UP * 2.5, scale=0.5),
        )
        self.play(Create(axes))

        x, y = _mises_ellipse(sy)
        mises = curve([O + np.array([xi * s, yi * s, 0.0]) for xi, yi in zip(x, y)],
                      color=TENSION, width=2.8)
        self.play(Create(mises), run_time=1.4)

        hexa = [(1, 0), (1, 1), (0, 1), (-1, 0), (-1, -1), (0, -1)]
        tre = curve([O + np.array([a * sy * s, b * sy * s, 0.0]) for a, b in hexa + [hexa[0]]],
                    color=COMPRESS, width=2.4)
        self.play(Create(tre), run_time=1.0)

        pts = VGroup(*[dot_at(O + np.array([a * sy * s, b * sy * s, 0.0]), color=MARK)
                       for a, b in hexa])
        self.play(FadeIn(pts))

        leg = VGroup(
            label("Mizes (silindr)", np.array([-4.6, 1.9, 0.0]), scale=0.36, color=TENSION),
            label("Treska (prizma)", np.array([-4.6, 1.5, 0.0]), scale=0.36, color=COMPRESS),
            label("6 nuqtada ustma-ust", np.array([-4.6, 1.1, 0.0]), scale=0.32, color=MARK),
            label("sof siljishda farq 15,5%", np.array([-4.6, 0.7, 0.0]),
                  scale=0.32, color=RULE, mono=True),
        )
        self.play(Write(leg))
        eq = formula(r"\sigma_{vM} = \sqrt{\sigma_1^2 - \sigma_1\sigma_2 + \sigma_2^2}"
                     r" = \sigma_y",
                     np.array([2.6, -2.75, 0.0]), scale=0.55)
        self.play(Write(eq))
        self.play(FadeIn(self.caption(
            "Treska har doim konservativroq: uning yuzasi Mizes ichida yotadi")))
        self.wait(1.5)
        self.play(FadeIn(block))


class HardeningScene(MexanikaScene):
    """Izotrop yuza kengayadi, kinematik — siljiydi."""

    subject_code = "TMM-22"
    scene_title = "Oqish yuzasining evolyutsiyasi"

    def construct(self):
        block = self.show_title()
        s = 1.15
        for j, (name, col, cx) in enumerate([("izotrop", TENSION, -3.1),
                                             ("kinematik", COMPRESS, 3.1)]):
            O = np.array([cx, -0.2, 0.0])
            axes = VGroup(
                Line(O + LEFT * 2.5, O + RIGHT * 2.5, color=INK, stroke_width=1.8),
                Line(O + DOWN * 1.9, O + UP * 1.9, color=INK, stroke_width=1.8),
            )
            self.play(Create(axes), run_time=0.4)
            self.play(Write(label(name + " mustahkamlanish",
                                  O + np.array([0.0, 2.25, 0.0]), scale=0.4, color=col)),
                      run_time=0.4)

            for k, sy in enumerate((0.7, 1.0, 1.3)):
                if name == "izotrop":
                    # yuza KENGAYADI, markaz joyida qoladi
                    x, y = _mises_ellipse(sy)
                    shift = np.zeros(3)
                else:
                    # yuza o'lchamini SAQLAYDI, markaz siljiydi
                    x, y = _mises_ellipse(0.7)
                    shift = np.array([0.30 * k, 0.30 * k, 0.0])
                e = curve([O + shift + np.array([xi * s, yi * s, 0.0])
                           for xi, yi in zip(x, y)],
                          color=col if k == 2 else RULE, width=2.6 if k == 2 else 1.8)
                self.play(Create(e), run_time=0.55)

        note = VGroup(
            label("o'lcham o'sadi, markaz qo'zg'almaydi", np.array([-3.1, -2.45, 0.0]),
                  scale=0.32, color=TENSION),
            label("o'lcham o'zgarmaydi, markaz siljiydi", np.array([3.1, -2.45, 0.0]),
                  scale=0.32, color=COMPRESS),
            label("Baushinger effekti faqat kinematik modelda chiqadi",
                  np.array([0.0, -2.95, 0.0]), scale=0.34, color=MARK),
        )
        self.play(Write(note))
        self.wait(1.5)
        self.play(FadeIn(block))
