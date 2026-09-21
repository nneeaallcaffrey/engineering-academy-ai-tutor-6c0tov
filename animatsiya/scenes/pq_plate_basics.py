"""PQ: yupqa plastina nazariyasining asoslari."""
from __future__ import annotations

import numpy as np
from manim import Arrow, Create, FadeIn, FadeOut, Line, Polygon, Write, VGroup, DOWN, LEFT, RIGHT, UP

from _common import (
    COMPRESS, INK, MARK, MexanikaScene, RULE, TENSION, curve, dashed, dot_at, formula, hatched,
    label, load_arrows,
)


class KirchhoffHypothesisScene(MexanikaScene):
    """Deformatsiyadan keyin ham normal o'rta sirtga perpendikulyar qoladi."""

    subject_code = "PQ-01"
    scene_title = "Kirxhoff gipotezasi: normal normal qoladi"

    def construct(self):
        block = self.show_title()

        # deformatsiyalanmagan holat
        y0 = 1.9
        mid = Line(np.array([-5.0, y0, 0.0]), np.array([5.0, y0, 0.0]),
                   color=MARK, stroke_width=2.4)
        top = Line(np.array([-5.0, y0 + 0.4, 0.0]), np.array([5.0, y0 + 0.4, 0.0]),
                   color=INK, stroke_width=2)
        bot = Line(np.array([-5.0, y0 - 0.4, 0.0]), np.array([5.0, y0 - 0.4, 0.0]),
                   color=INK, stroke_width=2)
        self.play(Create(top), Create(mid), Create(bot))
        norms = VGroup(*[Line(np.array([x, y0 + 0.4, 0.0]), np.array([x, y0 - 0.4, 0.0]),
                              color=COMPRESS, stroke_width=2)
                         for x in np.linspace(-4.2, 4.2, 9)])
        self.play(Create(norms))
        self.play(Write(label("deformatsiyadan oldin", np.array([0.0, y0 + 0.85, 0.0]),
                              scale=0.36, color=RULE)))

        # deformatsiyalangan holat
        y1 = -1.1
        def w(x):
            return -0.75 * np.cos(np.pi * x / 10.0) ** 2 + 0.75

        xs = np.linspace(-5.0, 5.0, 140)
        midd = curve([np.array([x, y1 - w(x), 0.0]) for x in xs], color=MARK, width=2.6)
        self.play(Create(midd), run_time=1.0)

        for x in np.linspace(-4.2, 4.2, 9):
            h = 1e-3
            slope = (w(x + h) - w(x - h)) / (2 * h)
            # normal: o'rta sirtga perpendikulyar, burchagi -dw/dx
            n = np.array([slope, 1.0, 0.0])
            n = n / np.linalg.norm(n)
            c = np.array([x, y1 - w(x), 0.0])
            self.add(Line(c + n * 0.4, c - n * 0.4, color=COMPRESS, stroke_width=2))
        topd = curve([np.array([x, y1 - w(x), 0.0]) +
                      _normal(w, x) * 0.4 for x in xs], color=INK, width=2)
        botd = curve([np.array([x, y1 - w(x), 0.0]) -
                      _normal(w, x) * 0.4 for x in xs], color=INK, width=2)
        self.play(Create(topd), Create(botd), run_time=0.9)
        self.play(Write(label("deformatsiyadan keyin", np.array([0.0, y1 - 1.55, 0.0]),
                              scale=0.36, color=RULE)))

        eq = VGroup(
            formula(r"u = -z\frac{\partial w}{\partial x},\quad "
                    r"v = -z\frac{\partial w}{\partial y}",
                    np.array([0.0, -2.55, 0.0]), scale=0.62),
            formula(r"\gamma_{xz} = \gamma_{yz} = 0",
                    np.array([0.0, -3.05, 0.0]), scale=0.55, color=TENSION),
        )
        self.play(Write(eq[0])); self.play(Write(eq[1]))
        self.play(FadeIn(self.caption(
            "Siljish deformatsiyasi nolga tenglanadi — uch o'lchovli masala ikkiga tushadi")))
        self.wait(1.4)
        self.play(FadeIn(block))


def _normal(w, x, h=1e-3):
    slope = (w(x + h) - w(x - h)) / (2 * h)
    n = np.array([slope, 1.0, 0.0])
    return n / np.linalg.norm(n)


class PlateMomentsScene(MexanikaScene):
    """Element qirralaridagi beshta ichki kuch omili."""

    subject_code = "PQ-03"
    scene_title = "Plastina elementidagi ichki kuch omillari"

    def construct(self):
        block = self.show_title()
        c = np.array([-1.2, 0.1, 0.0])
        a = 1.5
        sq = Polygon(c + np.array([-a, -a, 0]), c + np.array([a, -a, 0]),
                     c + np.array([a, a, 0]), c + np.array([-a, a, 0]),
                     color=INK, stroke_width=2.4, fill_opacity=0.06)
        self.play(Create(sq))
        self.play(Write(label("dx", c + np.array([0.0, -a - 0.32, 0.0]), scale=0.36)),
                  Write(label("dy", c + np.array([-a - 0.36, 0.0, 0.0]), scale=0.36)))

        items = [
            (c + np.array([a, 0.3, 0]), RIGHT * 0.9, r"M_x", TENSION),
            (c + np.array([0.3, a, 0]), UP * 0.9, r"M_y", TENSION),
            (c + np.array([a, -0.5, 0]), RIGHT * 0.75, r"M_{xy}", MARK),
            (c + np.array([a, 0.9, 0]), DOWN * 0.8, r"Q_x", COMPRESS),
            (c + np.array([-0.55, a, 0]), DOWN * 0.8, r"Q_y", COMPRESS),
        ]
        for k, (p, d, name, col) in enumerate(items):
            self.play(Create(Arrow(p, p + d, buff=0, color=col, stroke_width=2.8)),
                      run_time=0.35)
            self.play(Write(formula(name, p + d * 1.35, scale=0.5, color=col)), run_time=0.3)

        eq = VGroup(
            formula(r"M_x = -D\left(\frac{\partial^2 w}{\partial x^2} + "
                    r"\nu\frac{\partial^2 w}{\partial y^2}\right)",
                    np.array([3.3, 1.7, 0.0]), scale=0.52),
            formula(r"M_{xy} = -D(1-\nu)\frac{\partial^2 w}{\partial x \partial y}",
                    np.array([3.3, 0.8, 0.0]), scale=0.52, color=MARK),
            formula(r"Q_x = \frac{\partial M_x}{\partial x} + "
                    r"\frac{\partial M_{xy}}{\partial y}",
                    np.array([3.3, -0.1, 0.0]), scale=0.52, color=COMPRESS),
            formula(r"D = \frac{Eh^3}{12(1-\nu^2)}",
                    np.array([3.3, -1.0, 0.0]), scale=0.56, color=INK),
        )
        for e in eq:
            self.play(Write(e), run_time=0.5)
        self.play(FadeIn(self.caption(
            "Beshta omil, lekin mustaqil noma'lum bitta: w(x, y)")))
        self.wait(1.4)
        self.play(FadeIn(block))


class PlateEquationScene(MexanikaScene):
    """Muvozanat + geometriya + Guk = bigarmonik tenglama."""

    subject_code = "PQ-04"
    scene_title = "Bigarmonik tenglamaning keltirib chiqarilishi"

    def construct(self):
        block = self.show_title()
        steps = [
            (r"\frac{\partial Q_x}{\partial x} + \frac{\partial Q_y}{\partial y} + q = 0",
             "muvozanat", COMPRESS),
            (r"Q_x = \frac{\partial M_x}{\partial x} + \frac{\partial M_{xy}}{\partial y}",
             "kesuvchi kuch — momentlar orqali", RULE),
            (r"M_x = -D\left(w_{,xx} + \nu w_{,yy}\right)",
             "moment — egrilik orqali (Guk)", MARK),
            (r"D\left(\frac{\partial^4 w}{\partial x^4} + "
             r"2\frac{\partial^4 w}{\partial x^2\partial y^2} + "
             r"\frac{\partial^4 w}{\partial y^4}\right) = q",
             "birlashtirilgan natija", TENSION),
        ]
        y = 2.1
        for tex, note, col in steps:
            f = formula(tex, np.array([-0.4, y, 0.0]), scale=0.62, color=col)
            n = label(note, np.array([-0.4, y - 0.52, 0.0]), scale=0.32, color=RULE)
            self.play(Write(f), run_time=0.9)
            self.play(Write(n), run_time=0.4)
            if col is not TENSION:
                self.play(Create(Line(np.array([-0.4, y - 0.78, 0.0]),
                                      np.array([-0.4, y - 1.05, 0.0]),
                                      color=RULE, stroke_width=1.6)), run_time=0.25)
            y -= 1.35

        final = formula(r"D\nabla^4 w = q", np.array([3.9, -1.6, 0.0]), scale=0.95,
                        color=TENSION)
        self.play(Write(final))
        self.play(Write(label("Sofi Jermen - Lagranj tenglamasi",
                              np.array([3.9, -2.25, 0.0]), scale=0.34, color=RULE)))
        self.play(FadeIn(self.caption(
            "To'rtinchi tartib: shuning uchun har chekkada IKKITA shart kerak")))
        self.wait(1.5)
        self.play(FadeIn(block))


class KirchhoffShearScene(MexanikaScene):
    """Uchta shartni ikkiga siqish burchakda reaksiya paydo qiladi."""

    subject_code = "PQ-05"
    scene_title = "Kirxhoff kesuvchi kuchi va burchak reaksiyasi"

    def construct(self):
        block = self.show_title()
        c = np.array([-2.2, 0.2, 0.0])
        a = 2.0
        plate = Polygon(c + np.array([-a, -a, 0]), c + np.array([a, -a, 0]),
                        c + np.array([a, a, 0]), c + np.array([-a, a, 0]),
                        color=INK, stroke_width=2.6, fill_opacity=0.05)
        self.play(Create(plate))

        edge = c + np.array([a, 0.0, 0.0])
        self.play(Create(Arrow(edge + RIGHT * 0.9, edge, buff=0, color=COMPRESS,
                               stroke_width=3)),
                  Write(formula("Q_x", edge + RIGHT * 1.25, scale=0.48, color=COMPRESS)))
        self.play(Create(Arrow(edge + np.array([0.55, 0.75, 0]),
                               edge + np.array([0.55, 0.05, 0]), buff=0, color=MARK,
                               stroke_width=2.6)),
                  Write(formula("M_{xy}", edge + np.array([1.15, 0.75, 0]),
                                scale=0.44, color=MARK)))

        arrow = Arrow(np.array([0.4, 0.2, 0.0]), np.array([1.5, 0.2, 0.0]), buff=0,
                      color=RULE, stroke_width=2.4)
        self.play(Create(arrow))
        eq = formula(r"V_x = Q_x + \frac{\partial M_{xy}}{\partial y}",
                     np.array([3.6, 0.9, 0.0]), scale=0.6, color=TENSION)
        self.play(Write(eq))

        corner = c + np.array([a, a, 0.0])
        self.play(FadeIn(dot_at(corner, color=TENSION, r=0.1)))
        self.play(Create(Arrow(corner + np.array([0.75, 0.75, 0]), corner, buff=0,
                               color=TENSION, stroke_width=3.4)))
        self.play(Write(formula(r"R = 2M_{xy}", corner + np.array([1.35, 0.95, 0]),
                                scale=0.5, color=TENSION)))
        self.play(Write(label("burchakni ushlab turadigan kuch",
                              np.array([3.4, -0.6, 0.0]), scale=0.34, color=TENSION)))
        self.play(Write(label("Aks holda burchak ko'tariladi",
                              np.array([3.4, -1.1, 0.0]), scale=0.32, color=RULE)))
        self.play(FadeIn(self.caption(
            "Uchta chegaraviy shartni ikkiga siqish — bu Kirxhoffning kelishuvi")))
        self.wait(1.5)
        self.play(FadeIn(block))
