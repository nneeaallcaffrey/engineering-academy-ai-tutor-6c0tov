"""PQ: plastina ustuvorligi."""
from __future__ import annotations

import numpy as np
from manim import Arrow, Create, FadeIn, Line, Polygon, Write, VGroup, DOWN, LEFT, RIGHT, UP

from _common import (
    COMPRESS, INK, MARK, MexanikaScene, RULE, TENSION, axis_pair, curve, dashed, dot_at,
    formula, label,
)


class PlateBucklingScene(MexanikaScene):
    """Plastina sterjendan farqli — ustuvorlikdan keyin ham yuk ko'taradi."""

    subject_code = "PQ-19"
    scene_title = "Plastina ustuvorligini yo'qotishi"

    def construct(self):
        block = self.show_title()
        c = np.array([-3.0, 0.6, 0.0])
        a, b = 2.4, 1.6
        plate = Polygon(c + np.array([-a, -b, 0]), c + np.array([a, -b, 0]),
                        c + np.array([a, b, 0]), c + np.array([-a, b, 0]),
                        color=INK, stroke_width=2.4, fill_opacity=0.05)
        self.play(Create(plate))
        for y in np.linspace(-b * 0.8, b * 0.8, 5):
            self.add(Arrow(c + np.array([-a - 0.75, y, 0]), c + np.array([-a - 0.08, y, 0]),
                           buff=0, color=COMPRESS, stroke_width=2.4))
            self.add(Arrow(c + np.array([a + 0.75, y, 0]), c + np.array([a + 0.08, y, 0]),
                           buff=0, color=COMPRESS, stroke_width=2.4))
        self.play(Write(formula("N_x", c + np.array([-a - 1.15, 0, 0]), scale=0.5,
                                color=COMPRESS)))

        for j in range(3):
            m = j + 1
            pts = []
            for t in np.linspace(0, 1, 80):
                pts.append(c + np.array([-a + 2 * a * t,
                                         0.5 * np.sin(m * np.pi * t) * np.sin(np.pi * 0.5),
                                         0.0]))
            self.play(Create(curve(pts, color=[TENSION, MARK, RULE][j],
                                   width=3 - 0.5 * j)), run_time=0.55)

        O = np.array([2.6, -2.0, 0.0])
        axes = axis_pair(O, x_len=3.4, y_len=4.0, x_label="w/h", y_label="N")
        self.play(Create(axes))
        cr = Line(O + np.array([0.0, 2.0, 0.0]), O + np.array([3.0, 2.0, 0.0]),
                  color=RULE, stroke_width=1.8)
        self.play(Create(cr), Write(label("N_cr", O + np.array([3.2, 2.0, 0.0]),
                                          scale=0.34, color=RULE, mono=True)))
        post = [O + np.array([t * 2.6, 2.0 + 1.35 * np.sqrt(max(t, 0.0)), 0.0])
                for t in np.linspace(0, 1.15, 60)]
        self.play(Create(curve(post, color=TENSION, width=2.8)), run_time=0.9)
        self.play(Write(label("ustuvorlikdan keyingi zaxira",
                              O + np.array([1.5, 3.85, 0.0]), scale=0.3, color=TENSION)))

        eq = formula(r"N_{cr} = k\,\frac{\pi^2 D}{b^2}", np.array([-3.0, -2.5, 0.0]),
                     scale=0.66)
        self.play(Write(eq))
        self.play(FadeIn(self.caption(
            "Sterjen ustuvorlikni yo'qotsa qulaydi, plastina esa yuk ko'tarishda davom etadi")))
        self.wait(1.4)
        self.play(FadeIn(block))


class BucklingGarlandScene(MexanikaScene):
    """k(alpha) girlandasi: minimumlar butun nisbatlarda."""

    subject_code = "PQ-20"
    scene_title = "Girlanda egri chizig'i va yarim to'lqinlar"

    def construct(self):
        block = self.show_title()
        O = np.array([-4.8, -1.9, 0.0])
        axes = axis_pair(O, x_len=9.6, y_len=4.2, x_label=r"\alpha = a/b", y_label="k")
        self.play(Create(axes))

        sx, sy = 1.75, 0.58
        for m in range(1, 6):
            xs = np.linspace(0.45, 5.3, 300)
            ks = (m / xs + xs / m) ** 2
            pts = [O + np.array([x * sx, k * sy, 0.0])
                   for x, k in zip(xs, ks) if k < 7.2]
            if pts:
                self.play(Create(curve(pts, color=RULE, width=1.6)), run_time=0.45)

        # pastki o'ram — haqiqiy kritik qiymat
        xs = np.linspace(0.45, 5.3, 400)
        env = [min((m / x + x / m) ** 2 for m in range(1, 8)) for x in xs]
        pts = [O + np.array([x * sx, e * sy, 0.0]) for x, e in zip(xs, env) if e < 7.2]
        self.play(Create(curve(pts, color=TENSION, width=3)), run_time=1.2)

        for m in range(1, 5):
            x = float(m)
            self.play(FadeIn(dot_at(O + np.array([x * sx, 4.0 * sy, 0.0]),
                                    color=MARK, r=0.075)), run_time=0.2)
            self.play(Write(label(f"m={m}", O + np.array([x * sx, 4.0 * sy - 0.42, 0.0]),
                                  scale=0.3, color=MARK, mono=True)), run_time=0.2)

        self.play(Write(label("k_min = 4,0", O + np.array([7.2, 4.0 * sy + 0.3, 0.0]),
                              scale=0.36, color=TENSION, mono=True)))
        eq = formula(r"k = \left(\frac{m}{\alpha} + \frac{\alpha}{m}\right)^2",
                     np.array([2.6, 2.5, 0.0]), scale=0.66)
        self.play(Write(eq))
        self.play(FadeIn(self.caption(
            "Uzun plastina yarim to'lqinlarga bo'linadi va k doim 4 ga yaqin qoladi")))
        self.wait(1.4)
        self.play(FadeIn(block))


class ShearBucklingScene(MexanikaScene):
    """Siljishda to'lqinlar qiyshiq; keyin tortish maydoni paydo bo'ladi."""

    subject_code = "PQ-21"
    scene_title = "Siljishda ustuvorlik va tortish maydoni"

    def construct(self):
        block = self.show_title()
        c = np.array([-2.8, 0.4, 0.0])
        a, b = 2.7, 1.7
        plate = Polygon(c + np.array([-a, -b, 0]), c + np.array([a, -b, 0]),
                        c + np.array([a, b, 0]), c + np.array([-a, b, 0]),
                        color=INK, stroke_width=2.4, fill_opacity=0.05)
        self.play(Create(plate))

        for (p0, p1) in ((c + np.array([-a, b, 0]), c + np.array([a, b, 0])),
                         (c + np.array([a, -b, 0]), c + np.array([-a, -b, 0]))):
            self.add(Arrow(p0, p1, buff=0, color=COMPRESS, stroke_width=3))
        self.play(Write(formula(r"\tau", c + np.array([0.0, b + 0.45, 0]), scale=0.5,
                                color=COMPRESS)))

        for k in range(-3, 4):
            off = k * 0.85
            pts = [c + np.array([t, t + off, 0.0]) for t in np.linspace(-a, a, 40)]
            pts = [p for p in pts if abs(p[1] - c[1]) <= b]
            if len(pts) > 1:
                self.play(Create(curve(pts, color=TENSION, width=2.0)), run_time=0.22)
        self.play(Write(label("45° qiyshiq to'lqinlar", c + np.array([0.0, -b - 0.45, 0]),
                              scale=0.34, color=TENSION)))

        info = VGroup(
            formula(r"\tau_{cr} = k_s\frac{\pi^2 D}{b^2 h}", np.array([2.9, 1.5, 0.0]),
                    scale=0.6),
            label("k_s = 9,34  (uzun panel, sharnirli)", np.array([2.9, 0.85, 0.0]),
                  scale=0.32, color=RULE, mono=True),
            label("tortish maydoni: ustuvorlikdan keyin", np.array([2.9, 0.25, 0.0]),
                  scale=0.32, color=MARK),
            label("panel diagonal ferma kabi ishlaydi", np.array([2.9, -0.2, 0.0]),
                  scale=0.32, color=MARK),
        )
        for x in info:
            self.play(Write(x), run_time=0.45)
        self.play(FadeIn(self.caption(
            "Cho'zilish diagonali ish qiladi, siqilish diagonali esa qiyshayadi")))
        self.wait(1.4)
        self.play(FadeIn(block))
