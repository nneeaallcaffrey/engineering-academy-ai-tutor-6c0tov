"""TMM: suyuqlik mexanikasi sahnalari."""
from __future__ import annotations

import numpy as np
from manim import Arrow, Create, FadeIn, Line, Polygon, Write, VGroup, DOWN, LEFT, RIGHT, UP

from _common import (
    COMPRESS, INK, MARK, MexanikaScene, RULE, TENSION, axis_pair, curve, dashed, dot_at,
    formula, label, sampled,
)


def _erf(x: float) -> float:
    """erf ning Abramovits-Stigan yaqinlashishi (7.1.26), xatosi < 1.5e-7."""
    sign = 1.0 if x >= 0 else -1.0
    x = abs(x)
    t = 1.0 / (1.0 + 0.3275911 * x)
    y = 1.0 - (((((1.061405429 * t - 1.453152027) * t) + 1.421413741) * t
                - 0.284496736) * t + 0.254829592) * t * np.exp(-x * x)
    return sign * float(y)


class BernoulliScene(MexanikaScene):
    """Ventura: kesim torayganda tezlik o'sadi, bosim tushadi."""

    subject_code = "TMM-26"
    scene_title = "Ventura oqimi va Bernulli balansi"

    def construct(self):
        block = self.show_title()

        def half(x):
            return 1.05 - 0.55 * np.exp(-(x / 1.05) ** 2)

        xs = np.linspace(-5.0, 5.0, 160)
        yc = 0.9
        top = [np.array([x, yc + half(x), 0.0]) for x in xs]
        bot = [np.array([x, yc - half(x), 0.0]) for x in xs]
        self.play(Create(curve(top, color=INK, width=2.6)),
                  Create(curve(bot, color=INK, width=2.6)), run_time=1.3)

        for x in np.linspace(-4.4, 4.4, 12):
            v = 1.0 / half(x)
            a = Arrow(np.array([x - 0.3 * v, yc, 0.0]), np.array([x + 0.3 * v, yc, 0.0]),
                      buff=0, color=COMPRESS, stroke_width=2.2)
            self.add(a)
        self.play(Write(label("v ~ 1/A", np.array([-3.4, yc + 1.35, 0.0]),
                              scale=0.36, color=COMPRESS, mono=True)))

        O = np.array([-5.0, -2.4, 0.0])
        axes = axis_pair(O, x_len=10.0, y_len=2.2, x_label="x", y_label="p")
        self.play(Create(axes))
        p = [np.array([x, O[1] + 0.35 + 1.25 * (half(x) ** 2 - 0.25), 0.0]) for x in xs]
        self.play(Create(curve(p, color=TENSION, width=2.8)), run_time=1.1)
        self.play(FadeIn(dot_at(np.array([0.0, O[1] + 0.35 + 1.25 * (half(0.0)**2 - 0.25), 0.0]),
                                color=TENSION, r=0.08)),
                  Write(label("bosim minimal", np.array([1.5, O[1] + 0.25, 0.0]),
                              scale=0.34, color=TENSION)))

        eq = formula(r"p + \tfrac{1}{2}\rho v^2 + \rho g z = \text{const}",
                     np.array([2.4, 2.55, 0.0]), scale=0.62)
        self.play(Write(eq))
        self.play(FadeIn(self.caption(
            "Uzluksizlik tezlikni, Bernulli esa bosimni belgilaydi")))
        self.wait(1.4)
        self.play(FadeIn(block))


class NavierStokesScene(MexanikaScene):
    """Yopishqoq diffuziya: devordagi no-slip profilni shakllantiradi."""

    subject_code = "TMM-27"
    scene_title = "Yopishqoq diffuziya va no-slip"

    def construct(self):
        block = self.show_title()
        wall = np.array([-5.0, -1.9, 0.0])
        w = Line(wall, wall + RIGHT * 10.0, color=INK, stroke_width=4)
        self.play(Create(w))
        for x in np.linspace(-4.8, 4.8, 22):
            self.add(Line(np.array([x, -1.9, 0.0]), np.array([x - 0.16, -2.12, 0.0]),
                          color=RULE, stroke_width=1.4))

        H = 3.4
        for k, (t, col) in enumerate([(0.05, RULE), (0.3, COMPRESS), (1.0, TENSION)]):
            pts = []
            for y in np.linspace(0.0, H, 70):
                # Stoksning birinchi masalasi: u = U erf(y / (2 sqrt(nu t)))
                eta = y / (2.0 * np.sqrt(0.35 * t))
                u = _erf(eta)
                pts.append(np.array([-3.6 + u * 3.0, -1.9 + y, 0.0]))
            self.play(Create(curve(pts, color=col, width=2.6)), run_time=0.7)
            self.play(Write(label(f"t = {t}", np.array([pts[-1][0] + 0.55, -1.9 + H, 0.0]),
                                  scale=0.32, color=col, mono=True)), run_time=0.3)

        self.play(FadeIn(dot_at(np.array([-3.6, -1.9, 0.0]), color=INK, r=0.08)),
                  Write(label("u = 0 (no-slip)", np.array([-2.4, -1.62, 0.0]),
                              scale=0.34, color=INK)))
        eq = formula(r"\rho\frac{D\vec v}{Dt} = -\nabla p + \mu\nabla^2\vec v + \rho\vec g",
                     np.array([1.4, 2.3, 0.0]), scale=0.58)
        self.play(Write(eq))
        self.play(Write(label("qatlam qalinligi ~ sqrt(nu t)", np.array([2.6, 1.55, 0.0]),
                              scale=0.34, color=MARK, mono=True)))
        self.play(FadeIn(self.caption(
            "Yopishqoqlik impulsni devordan ichkariga DIFFUZIYA qiladi")))
        self.wait(1.4)
        self.play(FadeIn(block))


class PoiseuilleScene(MexanikaScene):
    """Parabolik profil: chekkada nol, markazda maksimum."""

    subject_code = "TMM-28"
    scene_title = "Puazeyl profilining shakllanishi"

    def construct(self):
        block = self.show_title()
        y0, R = 0.5, 1.4
        top = Line(np.array([-5.2, y0 + R, 0.0]), np.array([5.2, y0 + R, 0.0]),
                   color=INK, stroke_width=3.5)
        bot = Line(np.array([-5.2, y0 - R, 0.0]), np.array([5.2, y0 - R, 0.0]),
                   color=INK, stroke_width=3.5)
        self.play(Create(top), Create(bot))

        axis = dashed(np.array([-5.2, y0, 0.0]), np.array([5.2, y0, 0.0]))
        self.play(Create(axis))

        for x0, col, name in ((-3.4, RULE, "kirish"), (0.0, COMPRESS, "rivojlanish"),
                              (3.2, TENSION, "to'liq rivojlangan")):
            pts = []
            for y in np.linspace(-R, R, 50):
                if name == "kirish":
                    u = 1.0 if abs(y) < R * 0.85 else (R - abs(y)) / (R * 0.15)
                elif name == "rivojlanish":
                    u = 1.0 - (abs(y) / R) ** 4
                else:
                    u = 1.0 - (y / R) ** 2
                pts.append(np.array([x0 + u * 1.5, y0 + y, 0.0]))
            self.play(Create(curve(pts, color=col, width=2.6)), run_time=0.7)
            for y in np.linspace(-R * 0.9, R * 0.9, 7):
                if name == "kirish":
                    u = 1.0 if abs(y) < R * 0.85 else (R - abs(y)) / (R * 0.15)
                elif name == "rivojlanish":
                    u = 1.0 - (abs(y) / R) ** 4
                else:
                    u = 1.0 - (y / R) ** 2
                self.add(Arrow(np.array([x0, y0 + y, 0.0]),
                               np.array([x0 + u * 1.5, y0 + y, 0.0]), buff=0,
                               color=col, stroke_width=1.8))
            self.play(Write(label(name, np.array([x0 + 0.6, y0 - R - 0.42, 0.0]),
                                  scale=0.32, color=col)), run_time=0.3)

        eq = VGroup(
            formula(r"u(r) = \frac{\Delta p}{4\mu L}\left(R^2 - r^2\right)",
                    np.array([-2.4, -2.5, 0.0]), scale=0.6),
            formula(r"Q = \frac{\pi R^4 \Delta p}{8\mu L}",
                    np.array([2.8, -2.5, 0.0]), scale=0.6, color=MARK),
        )
        self.play(Write(eq[0])); self.play(Write(eq[1]))
        self.play(Write(label("u_max / u_o'rtacha = 2", np.array([0.0, 2.45, 0.0]),
                              scale=0.36, color=TENSION, mono=True)))
        self.play(FadeIn(self.caption(
            "Sarf radiusning TO'RTINCHI darajasiga proporsional — quvur diametri hal qiluvchi")))
        self.wait(1.4)
        self.play(FadeIn(block))


class BoundaryLayerScene(MexanikaScene):
    """Blazius: barcha profillar bitta o'xshashlik egrisiga tushadi."""

    subject_code = "TMM-29"
    scene_title = "Chegaraviy qatlam va o'xshashlik yechimi"

    def construct(self):
        block = self.show_title()
        plate = Line(np.array([-5.2, -0.9, 0.0]), np.array([1.2, -0.9, 0.0]),
                     color=INK, stroke_width=4)
        self.play(Create(plate))

        # qatlam qalinligi delta ~ sqrt(x)
        dpts = [np.array([x, -0.9 + 1.55 * np.sqrt(max(x + 5.2, 0.0) / 6.4), 0.0])
                for x in np.linspace(-5.2, 1.2, 100)]
        self.play(Create(curve(dpts, color=MARK, width=2.4)), run_time=1.2)
        self.play(Write(label("delta ~ sqrt(x)", np.array([-1.4, 1.15, 0.0]),
                              scale=0.36, color=MARK, mono=True)))

        for x in (-4.0, -2.2, -0.4):
            d = 1.55 * np.sqrt((x + 5.2) / 6.4)
            pts = []
            for e in np.linspace(0.0, 1.0, 40):
                u = _erf(2.0 * e)           # Blazius profiliga yaqin shakl
                pts.append(np.array([x + u * 1.0, -0.9 + e * d, 0.0]))
            self.play(Create(curve(pts, color=COMPRESS, width=2.2)), run_time=0.5)

        # o'ngda: o'xshashlik o'zgaruvchisi bo'yicha HAMMASI bitta egri
        O = np.array([2.2, -2.1, 0.0])
        axes = axis_pair(O, x_len=3.0, y_len=4.0, x_label="u/U", y_label=r"\eta")
        self.play(Create(axes))
        sim = [O + np.array([_erf(2.0 * e) * 2.6, e * 3.6, 0.0])
               for e in np.linspace(0.0, 1.0, 60)]
        self.play(Create(curve(sim, color=TENSION, width=3)), run_time=0.9)
        self.play(Write(label("uchala profil ustma-ust", O + np.array([1.2, 3.85, 0.0]),
                              scale=0.32, color=TENSION)))

        eq = formula(r"2f''' + f f'' = 0,\qquad \eta = y\sqrt{\frac{U}{\nu x}}",
                     np.array([-2.2, -2.7, 0.0]), scale=0.58)
        self.play(Write(eq))
        self.play(FadeIn(self.caption(
            "Ikki o'zgaruvchili masala bitta oddiy differensial tenglamaga keldi")))
        self.wait(1.4)
        self.play(FadeIn(block))


class TurbulenceScene(MexanikaScene):
    """Energiya kaskadi: katta uyurmalardan kichiklariga."""

    subject_code = "TMM-30"
    scene_title = "Energiya kaskadi va Reynolds o'rtachalashi"

    def construct(self):
        block = self.show_title()
        O = np.array([-4.4, -2.2, 0.0])
        axes = axis_pair(O, x_len=8.6, y_len=4.3, x_label=r"\log k", y_label=r"\log E(k)")
        self.play(Create(axes))

        pts = []
        for lk in np.linspace(0.15, 7.2, 160):
            if lk < 1.1:
                e = 3.4 + 0.5 * lk
            elif lk < 5.0:
                e = 3.95 - (5.0 / 3.0) * (lk - 1.1)     # -5/3 qonuni
            else:
                e = 3.95 - (5.0 / 3.0) * 3.9 - 3.0 * (lk - 5.0)
            pts.append(O + np.array([lk, max(e, 0.05), 0.0]))
        self.play(Create(curve(pts, color=TENSION, width=3)), run_time=1.6)

        self.play(Write(label("E(k) ~ k^(-5/3)", O + np.array([2.4, 3.05, 0.0]),
                              scale=0.4, color=TENSION, mono=True)))
        for x, name, col in ((0.6, "energiya\nkirishi", COMPRESS),
                             (3.0, "inersial\noraliq", MARK),
                             (6.2, "dissipatsiya", RULE)):
            self.play(Create(dashed(O + np.array([x, 0.0, 0.0]),
                                    O + np.array([x, 4.0, 0.0]))), run_time=0.3)
            self.play(Write(label(name.replace("\n", " "),
                                  O + np.array([x, -0.42, 0.0]), scale=0.3, color=col)),
                      run_time=0.3)

        eq = VGroup(
            formula(r"u = \bar u + u'", np.array([2.9, 2.2, 0.0]), scale=0.6),
            formula(r"-\rho\overline{u_i'u_j'}\ \text{— Reynolds kuchlanishi}",
                    np.array([2.4, 1.5, 0.0]), scale=0.48, color=COMPRESS),
        )
        self.play(Write(eq[0])); self.play(Write(eq[1]))
        self.play(FadeIn(self.caption(
            "O'rtachalash yangi noma'lum keltiradi — yopilish masalasi shundan")))
        self.wait(1.4)
        self.play(FadeIn(block))
