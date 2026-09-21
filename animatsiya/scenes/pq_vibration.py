"""PQ: plastina tebranishlari."""
from __future__ import annotations

import numpy as np
from manim import Create, FadeIn, Line, Polygon, Write, VGroup, DOWN, LEFT, RIGHT, UP

from _common import (
    COMPRESS, INK, MARK, MexanikaScene, RULE, TENSION, axis_pair, curve, dashed, dot_at,
    formula, label, sampled,
)


class PlateModesScene(MexanikaScene):
    """Tugun chiziqlari — Xladni figuralarining o'zi."""

    subject_code = "PQ-22"
    scene_title = "Tebranish shakllari va Xladni figuralari"

    def construct(self):
        block = self.show_title()
        modes = [(1, 1), (2, 1), (2, 2), (3, 1)]
        for k, (m, n) in enumerate(modes):
            c = np.array([-4.3 + 2.85 * k, 0.5, 0.0])
            s = 1.05
            sq = Polygon(c + np.array([-s, -s, 0]), c + np.array([s, -s, 0]),
                         c + np.array([s, s, 0]), c + np.array([-s, s, 0]),
                         color=INK, stroke_width=2)
            self.play(Create(sq), run_time=0.3)

            # tugun chiziqlari: sin(m pi x) = 0 va sin(n pi y) = 0
            for i in range(1, m):
                x = -s + 2 * s * i / m
                self.add(Line(c + np.array([x, -s, 0]), c + np.array([x, s, 0]),
                              color=TENSION, stroke_width=2.6))
            for j in range(1, n):
                y = -s + 2 * s * j / n
                self.add(Line(c + np.array([-s, y, 0]), c + np.array([s, y, 0]),
                              color=TENSION, stroke_width=2.6))

            # ishora: musbat/manfiy sohalar
            for i in range(m):
                for j in range(n):
                    sgn = (-1) ** (i + j)
                    p = c + np.array([-s + 2 * s * (i + 0.5) / m,
                                      -s + 2 * s * (j + 0.5) / n, 0.0])
                    self.add(dot_at(p, color=COMPRESS if sgn > 0 else RULE, r=0.07))

            w = (m**2 + n**2)
            self.play(Write(label(f"({m},{n})", c + np.array([0.0, -s - 0.42, 0]),
                                  scale=0.38, color=INK, mono=True)),
                      Write(label(f"omega ~ {w}", c + np.array([0.0, -s - 0.8, 0]),
                                  scale=0.3, color=RULE, mono=True)), run_time=0.35)

        eq = formula(r"\omega_{mn} = \pi^2\left(\frac{m^2}{a^2} + \frac{n^2}{b^2}\right)"
                     r"\sqrt{\frac{D}{\rho h}}",
                     np.array([0.0, -2.4, 0.0]), scale=0.62)
        self.play(Write(eq))
        self.play(FadeIn(self.caption(
            "(2,1) va (1,2) kvadrat plastinada bir xil chastota beradi — karrali ildiz")))
        self.wait(1.4)
        self.play(FadeIn(block))


class ForcedVibrationScene(MexanikaScene):
    """Rezonansda amplitudani faqat demflash cheklaydi."""

    subject_code = "PQ-23"
    scene_title = "Rezonans va demflash"

    def construct(self):
        block = self.show_title()
        O = np.array([-4.8, -2.0, 0.0])
        axes = axis_pair(O, x_len=9.6, y_len=4.4, x_label=r"\omega/\omega_{11}", y_label="|w|")
        self.play(Create(axes))

        for i, (z, col) in enumerate(((0.002, TENSION), (0.02, MARK), (0.05, COMPRESS))):
            def A(b, z=z):
                return 1.0 / np.sqrt((1 - b**2) ** 2 + (2 * z * b) ** 2)
            pts = sampled(A, 0.05, 3.4, n=340, sx=2.6, sy=0.0085, origin=O)
            pts = [p for p in pts if p[1] - O[1] < 4.2]
            self.play(Create(curve(pts, color=col, width=2.4)), run_time=0.8)
            self.play(Write(label(f"zeta = {z:.3f}   kuchaytirish {1/(2*z):.0f}x",
                                  np.array([2.0, 2.35 - 0.42 * i, 0.0]), scale=0.32,
                                  color=col, mono=True)), run_time=0.3)

        for m, n in ((1, 1), (2, 1), (2, 2)):
            b = (m**2 + n**2) / 2.0
            if b * 2.6 < 9.0:
                self.play(Create(dashed(O + np.array([b * 2.6, 0.0, 0.0]),
                                        O + np.array([b * 2.6, 4.1, 0.0]))), run_time=0.25)
                self.play(Write(label(f"({m},{n})", O + np.array([b * 2.6, -0.35, 0.0]),
                                      scale=0.28, color=RULE, mono=True)), run_time=0.2)

        eq = formula(r"|w| = \frac{q/k}{\sqrt{(1-\beta^2)^2 + (2\zeta\beta)^2}}",
                     np.array([2.4, -2.75, 0.0]), scale=0.55)
        self.play(Write(eq))
        self.play(FadeIn(self.caption(
            "Rezonans cho'qqisi 1/(2 zeta) ga teng — demflash hal qiluvchi")))
        self.wait(1.4)
        self.play(FadeIn(block))


class MindlinScene(MexanikaScene):
    """Mindlinda normal burilishi mustaqil: siljish hisobga olinadi."""

    subject_code = "PQ-24"
    scene_title = "Kirxhoff va Mindlin kinematikasi"

    def construct(self):
        block = self.show_title()

        for k, (name, shear, col) in enumerate([("Kirxhoff", False, COMPRESS),
                                                ("Mindlin", True, TENSION)]):
            y0 = 1.5 - 3.0 * k
            def w(x):
                return -0.55 * np.cos(np.pi * x / 9.0) ** 2 + 0.55
            xs = np.linspace(-4.2, 4.2, 120)
            mid = curve([np.array([x, y0 - w(x), 0.0]) for x in xs], color=MARK, width=2.4)
            self.play(Create(mid), run_time=0.7)

            for x in np.linspace(-3.4, 3.4, 7):
                h = 1e-3
                slope = (w(x + h) - w(x - h)) / (2 * h)
                ang = np.arctan(slope)
                if shear:
                    ang -= 0.22                     # siljish burchagi gamma
                d = np.array([np.sin(ang), np.cos(ang), 0.0]) * 0.5
                c0 = np.array([x, y0 - w(x), 0.0])
                self.add(Line(c0 - d, c0 + d, color=col, stroke_width=2.6))
                if shear:
                    nrm = np.array([slope, 1.0, 0.0])
                    nrm = nrm / np.linalg.norm(nrm) * 0.5
                    self.add(Line(c0 - nrm, c0 + nrm, color=RULE, stroke_width=1.2))

            self.play(Write(label(name, np.array([-5.3, y0, 0.0]), scale=0.42, color=col)),
                      run_time=0.4)
            note = "normal o'rta sirtga perpendikulyar qoladi" if not shear \
                else "normal buriladi: gamma = beta + dw/dx"
            self.play(Write(label(note, np.array([0.0, y0 - 1.25, 0.0]),
                                  scale=0.32, color=RULE)), run_time=0.4)

        eq = VGroup(
            formula(r"\text{Kirxhoff: } \beta_x = -\frac{\partial w}{\partial x}",
                    np.array([3.3, 1.4, 0.0]), scale=0.5, color=COMPRESS),
            formula(r"\text{Mindlin: } \gamma_{xz} = \beta_x + "
                    r"\frac{\partial w}{\partial x} \ne 0",
                    np.array([3.1, -1.6, 0.0]), scale=0.5, color=TENSION),
        )
        self.play(Write(eq[0])); self.play(Write(eq[1]))
        self.play(FadeIn(self.caption(
            "h/a > 0,05 bo'lsa siljish deformatsiyasini e'tiborsiz qoldirib bo'lmaydi")))
        self.wait(1.4)
        self.play(FadeIn(block))
