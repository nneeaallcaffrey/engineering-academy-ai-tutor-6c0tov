"""PQ: qobiqlar nazariyasi."""
from __future__ import annotations

import numpy as np
from manim import (
    Arrow, Circle, Create, FadeIn, Line, Polygon, Write, VGroup, DOWN, LEFT, RIGHT, UP,
)

from _common import (
    COMPRESS, INK, MARK, MexanikaScene, RULE, TENSION, axis_pair, curve, dashed, dot_at,
    formula, label, sampled,
)


class ShellGeometryScene(MexanikaScene):
    """Gauss egriligi sirt turini belgilaydi."""

    subject_code = "PQ-25"
    scene_title = "Gauss egriligi va sirt tasnifi"

    def construct(self):
        block = self.show_title()
        cases = [("sfera", 1.0, 1.0, "K > 0", TENSION),
                 ("silindr", 1.0, 0.0, "K = 0", MARK),
                 ("egar", 1.0, -1.0, "K < 0", COMPRESS)]
        for k, (name, k1, k2, note, col) in enumerate(cases):
            c = np.array([-4.0 + 4.0 * k, 0.6, 0.0])
            # ikkita bosh kesim
            p1 = [c + np.array([t, -k1 * 0.28 * t**2, 0.0]) for t in np.linspace(-1.3, 1.3, 50)]
            p2 = [c + np.array([t * 0.55, -k2 * 0.28 * t**2 + 0.75, 0.0])
                  for t in np.linspace(-1.9, 1.9, 50)]
            self.play(Create(curve(p1, color=col, width=2.6)),
                      Create(curve(p2, color=RULE, width=2.2)), run_time=0.6)
            self.play(Write(label(name, c + np.array([0.0, -1.35, 0.0]), scale=0.42,
                                  color=INK)),
                      Write(label(note, c + np.array([0.0, -1.78, 0.0]), scale=0.36,
                                  color=col, mono=True)), run_time=0.4)
            self.play(Write(label(f"k1={k1:+.0f}  k2={k2:+.0f}",
                                  c + np.array([0.0, -2.15, 0.0]), scale=0.3,
                                  color=RULE, mono=True)), run_time=0.3)

        eq = VGroup(
            formula(r"K = k_1 k_2 = \frac{1}{R_1 R_2}", np.array([0.0, 2.45, 0.0]), scale=0.68),
            label("K != 0 bo'lsa sirtni cho'zmasdan yoyib bo'lmaydi",
                  np.array([0.0, -2.75, 0.0]), scale=0.36, color=MARK),
        )
        self.play(Write(eq[0])); self.play(Write(eq[1]))
        self.play(FadeIn(self.caption(
            "Silindrni qog'ozdan yasash mumkin, sferani esa yo'q — K shuni aytadi")))
        self.wait(1.4)
        self.play(FadeIn(block))


class MembraneScene(MexanikaScene):
    """Laplas tenglamasi: bosim ikki egrilik orqali muvozanatlashadi."""

    subject_code = "PQ-26"
    scene_title = "Laplas tenglamasi va membrana kuchlari"

    def construct(self):
        block = self.show_title()
        c = np.array([-3.0, 0.3, 0.0])
        R = 1.6
        self.play(Create(Circle(radius=R, color=INK, stroke_width=2.8).move_to(c)))
        for a in np.linspace(0, 2 * np.pi, 13)[:-1]:
            d = np.array([np.cos(a), np.sin(a), 0.0])
            self.add(Arrow(c + d * R * 0.55, c + d * R * 0.95, buff=0,
                           color=COMPRESS, stroke_width=2))
        self.play(Write(formula("p", c + np.array([0.0, 0.0, 0.0]), scale=0.55,
                                color=COMPRESS)))
        self.play(Write(formula("N_\\theta", c + np.array([R + 0.55, 0.35, 0.0]),
                                scale=0.5, color=TENSION)))

        rows = VGroup(
            formula(r"\frac{N_1}{R_1} + \frac{N_2}{R_2} = p",
                    np.array([2.6, 1.9, 0.0]), scale=0.66, color=TENSION),
            label("sferik idish:  N = pR/2", np.array([2.6, 1.0, 0.0]),
                  scale=0.36, color=INK, mono=True),
            label("silindr:  N_theta = pR,  N_x = pR/2", np.array([2.6, 0.5, 0.0]),
                  scale=0.36, color=INK, mono=True),
            label("nisbat 2:1 — shuning uchun silindr", np.array([2.6, -0.1, 0.0]),
                  scale=0.33, color=MARK),
            label("bo'ylama chok bo'ylab yoriladi", np.array([2.6, -0.5, 0.0]),
                  scale=0.33, color=MARK),
        )
        for r in rows:
            self.play(Write(r), run_time=0.45)

        self.play(Write(label("Egilish momenti YO'Q — faqat cho'zilish",
                              np.array([0.0, -2.5, 0.0]), scale=0.4, color=TENSION)))
        self.play(FadeIn(self.caption(
            "Membrana holati eng samarali: material butun qalinligi bo'ylab ishlaydi")))
        self.wait(1.4)
        self.play(FadeIn(block))


class EdgeEffectScene(MexanikaScene):
    """Chekka effekti tez so'nadi: masshtab sqrt(Rh)."""

    subject_code = "PQ-27"
    scene_title = "Chekka effekti va so'nish masshtabi"

    def construct(self):
        block = self.show_title()
        O = np.array([-4.8, 0.2, 0.0])
        axes = axis_pair(O, x_len=9.6, y_len=2.6, x_label="x", y_label="M_x")
        self.play(Create(axes))

        for i, (beta, col, name) in enumerate(((2.2, TENSION, "yupqa: R/h = 200"),
                                               (1.2, COMPRESS, "qalin: R/h = 50"))):
            pts = []
            for x in np.linspace(0.0, 5.4, 300):
                b = beta * x
                pts.append(O + np.array([x * 1.75, 2.1 * np.exp(-b) * np.cos(b), 0.0]))
            self.play(Create(curve(pts, color=col, width=2.6)), run_time=0.9)
            L = np.pi / beta * 1.75
            self.play(Create(dashed(O + np.array([L, -1.0, 0.0]),
                                    O + np.array([L, 2.3, 0.0]))), run_time=0.3)
            self.play(Write(label(name, np.array([2.4, 2.4 - 0.45 * i, 0.0]),
                                  scale=0.34, color=col, mono=True)), run_time=0.3)

        self.play(Write(label("so'nish masshtabi ~ sqrt(R h)",
                              np.array([2.6, -1.7, 0.0]), scale=0.38, color=MARK, mono=True)))
        eq = formula(r"\ell = \frac{\pi}{\beta},\qquad "
                     r"\beta = \sqrt[4]{\frac{3(1-\nu^2)}{R^2h^2}}",
                     np.array([-2.6, -2.4, 0.0]), scale=0.58)
        self.play(Write(eq))
        self.play(FadeIn(self.caption(
            "Membrana yechimi chekkadan uzoqda o'rinli — mahalliy egilish tez so'nadi")))
        self.wait(1.4)
        self.play(FadeIn(block))


class JunctionScene(MexanikaScene):
    """Tutashuvda deformatsiyalar mos kelmaydi — moment tug'iladi."""

    subject_code = "PQ-28"
    scene_title = "Tutashuvdagi mos kelmaslik"

    def construct(self):
        block = self.show_title()
        y0 = 1.3
        cyl = VGroup(Line(np.array([-4.6, y0 + 1.1, 0]), np.array([0.0, y0 + 1.1, 0]),
                          color=INK, stroke_width=3),
                     Line(np.array([-4.6, y0 - 1.1, 0]), np.array([0.0, y0 - 1.1, 0]),
                          color=INK, stroke_width=3))
        dome = curve([np.array([1.1 * np.sin(t), y0 + 1.1 * np.cos(t), 0.0])
                      for t in np.linspace(-np.pi / 2, np.pi / 2, 80)],
                     color=INK, width=3)
        self.play(Create(cyl), Create(dome))
        self.play(Write(label("silindr", np.array([-2.6, y0 + 1.5, 0]), scale=0.36,
                              color=RULE)),
                  Write(label("sferik qopqoq", np.array([1.9, y0 + 1.2, 0]), scale=0.36,
                              color=RULE)))

        rows = VGroup(
            label("silindr:  delta = pR^2/(Eh) (1 - nu/2)", np.array([-1.6, -0.6, 0.0]),
                  scale=0.34, color=COMPRESS, mono=True),
            label("sfera:    delta = pR^2/(2Eh)(1 - nu)", np.array([-1.6, -1.05, 0.0]),
                  scale=0.34, color=TENSION, mono=True),
            label("farq != 0  ->  moslovchi kuch va moment", np.array([-1.6, -1.55, 0.0]),
                  scale=0.36, color=MARK, mono=True),
        )
        for r in rows:
            self.play(Write(r), run_time=0.45)

        self.play(FadeIn(dot_at(np.array([0.0, y0 + 1.1, 0]), color=MARK, r=0.1)),
                  FadeIn(dot_at(np.array([0.0, y0 - 1.1, 0]), color=MARK, r=0.1)))
        self.play(Create(Arrow(np.array([0.9, y0 + 1.1, 0]), np.array([0.15, y0 + 1.1, 0]),
                               buff=0, color=MARK, stroke_width=3)))
        self.play(Write(label("M_0, Q_0", np.array([1.9, y0 + 1.1, 0]), scale=0.36,
                              color=MARK, mono=True)))
        self.play(Write(label("Bu yerda membrana nazariyasi YETMAYDI",
                              np.array([0.0, -2.35, 0.0]), scale=0.4, color=TENSION)))
        self.play(FadeIn(self.caption(
            "Moslashtirish sharti: siljish va burilish ikkala tomondan teng bo'lishi kerak")))
        self.wait(1.4)
        self.play(FadeIn(block))


class ShellBucklingScene(MexanikaScene):
    """Nazariy va tajriba orasidagi tafovut — nuqsonlarga sezgirlik."""

    subject_code = "PQ-29"
    scene_title = "Qobiq ustuvorligi va nuqsonlarga sezgirlik"

    def construct(self):
        block = self.show_title()
        O = np.array([-4.4, -2.0, 0.0])
        axes = axis_pair(O, x_len=8.8, y_len=4.3, x_label=r"nuqson \ \xi", y_label=r"N/N_{cl}")
        self.play(Create(axes))

        lvl = Line(O + np.array([0.0, 3.6, 0.0]), O + np.array([8.4, 3.6, 0.0]),
                   color=RULE, stroke_width=2)
        self.play(Create(lvl), Write(label("klassik nazariya", O + np.array([5.6, 3.9, 0.0]),
                                           scale=0.34, color=RULE)))

        pts = []
        for x in np.linspace(0.0, 4.6, 220):
            rho = 1.0 / (1.0 + 2.6 * np.sqrt(x))
            pts.append(O + np.array([x * 1.8, rho * 3.6, 0.0]))
        self.play(Create(curve(pts, color=TENSION, width=3)), run_time=1.3)

        band = VGroup()
        for y in (0.20, 0.35):
            band.add(Line(O + np.array([0.0, y * 3.6, 0.0]), O + np.array([8.4, y * 3.6, 0.0]),
                          color=COMPRESS, stroke_width=1.4))
        self.play(Create(band))
        self.play(Write(label("tajriba: 0,2 ... 0,35", O + np.array([5.6, 1.05, 0.0]),
                              scale=0.34, color=COMPRESS, mono=True)))

        self.play(Write(label("Qobiq — nuqsonga ENG sezgir konstruksiya",
                              np.array([0.0, 2.55, 0.0]), scale=0.4, color=TENSION)))
        eq = formula(r"N_{cl} = \frac{Eh^2}{R\sqrt{3(1-\nu^2)}}",
                     np.array([2.6, 1.85, 0.0]), scale=0.55)
        self.play(Write(eq))
        self.play(FadeIn(self.caption(
            "Shuning uchun normalarda tajribaviy pasaytiruvchi koeffitsient qo'llaniladi")))
        self.wait(1.4)
        self.play(FadeIn(block))


class ShellVibrationScene(MexanikaScene):
    """Qobiq spektri plastinanikidan farq qiladi: minimum o'rtada."""

    subject_code = "PQ-30"
    scene_title = "Qobiq tebranish shakllari va spektr"

    def construct(self):
        block = self.show_title()
        O = np.array([-4.4, -2.0, 0.0])
        axes = axis_pair(O, x_len=8.8, y_len=4.2, x_label="n (aylana bo'yicha to'lqin)",
                         y_label=r"\omega")
        self.play(Create(axes))

        ns = np.arange(0, 13)
        # membrana qismi n bilan kamayadi, egilish qismi o'sadi
        w = np.sqrt(1.0 / (1.0 + 0.55 * ns**2) + 0.006 * ns**4)
        pts = [O + np.array([n * 0.66 + 0.3, ww * 3.0, 0.0]) for n, ww in zip(ns, w)]
        self.play(Create(curve(pts, color=TENSION, width=2.6)),
                  FadeIn(VGroup(*[dot_at(p, color=TENSION) for p in pts])), run_time=1.3)

        imin = int(np.argmin(w))
        self.play(FadeIn(dot_at(pts[imin], color=MARK, r=0.1)),
                  Write(label(f"minimum: n = {ns[imin]}", pts[imin] + np.array([0.9, -0.5, 0.0]),
                              scale=0.34, color=MARK, mono=True)))

        mem = [O + np.array([n * 0.66 + 0.3, np.sqrt(1.0 / (1.0 + 0.55 * n**2)) * 3.0, 0.0])
               for n in ns]
        ben = [O + np.array([n * 0.66 + 0.3, np.sqrt(0.006 * n**4) * 3.0, 0.0]) for n in ns]
        self.play(Create(curve(mem, color=COMPRESS, width=1.6)),
                  Create(curve(ben, color=RULE, width=1.6)))
        self.play(Write(label("membrana qismi", np.array([-1.6, 1.3, 0.0]), scale=0.3,
                              color=COMPRESS)),
                  Write(label("egilish qismi", np.array([2.6, 0.2, 0.0]), scale=0.3,
                              color=RULE)))

        self.play(Write(label("Plastinada omega n bilan monoton o'sadi, qobiqda — YO'Q",
                              np.array([0.0, 2.5, 0.0]), scale=0.38, color=TENSION)))
        self.play(FadeIn(self.caption(
            "Eng past chastota nol to'lqinli shaklda emas, o'rtadagi n da yotadi")))
        self.wait(1.4)
        self.play(FadeIn(block))
