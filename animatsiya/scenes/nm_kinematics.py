"""NM: egrilik doirasi va Koriolis effekti."""
from __future__ import annotations

import numpy as np
from manim import Arrow, Circle, Create, FadeIn, FadeOut, Write, VGroup, DOWN, LEFT, RIGHT, UP

from _common import (
    COMPRESS, INK, MARK, MexanikaScene, RULE, TENSION, curve, dashed, dot_at, formula, label,
)


class CurvatureScene(MexanikaScene):
    """Tezlanish urinma va normal tashkil etuvchilarga ajraladi."""

    subject_code = "NM-03"
    scene_title = "Egrilik doirasi va tezlanishning ajralishi"

    def construct(self):
        block = self.show_title()

        def path(t):
            return np.array([t, 0.55 * np.sin(1.1 * t) - 0.3, 0.0])

        pts = [path(t) for t in np.linspace(-4.6, 4.6, 160)]
        trail = curve(pts, color=RULE, width=2.4)
        self.play(Create(trail), run_time=1.6)

        for t0 in (-2.2, 0.35, 2.4):
            p = path(t0)
            h = 1e-4
            d1 = (path(t0 + h) - path(t0 - h)) / (2 * h)
            d2 = (path(t0 + h) - 2 * path(t0) + path(t0 - h)) / h**2
            speed = float(np.linalg.norm(d1))
            tang = d1 / speed
            # normal tashkil etuvchi: d2 dan urinma qismini ayiramiz
            a_n = d2 - float(np.dot(d2, tang)) * tang
            kappa = float(np.linalg.norm(np.cross(d1, d2))) / speed**3
            rho = 1.0 / kappa if kappa > 1e-9 else 50.0
            nrm = a_n / (np.linalg.norm(a_n) + 1e-12)

            centre = p + nrm * rho
            osc = Circle(radius=rho, color=MARK, stroke_width=1.8).move_to(centre)
            mark = dot_at(p, color=INK, r=0.06)
            vt = Arrow(p, p + tang * 1.15, buff=0, color=COMPRESS, stroke_width=3)
            vn = Arrow(p, p + nrm * min(1.15, 2.4 / rho + 0.35), buff=0,
                       color=TENSION, stroke_width=3)
            rad = dashed(p, centre)
            txt = label(f"rho = {rho:.2f}", p + nrm * 0.1 + RIGHT * 1.4, scale=0.36,
                        color=MARK, mono=True)

            self.play(FadeIn(mark), Create(osc), Create(rad), run_time=0.8)
            self.play(Create(vt), Create(vn), Write(txt), run_time=0.8)
            self.wait(0.7)
            self.play(FadeOut(VGroup(osc, rad, vt, vn, txt, mark)), run_time=0.5)

        eq = formula(r"\vec a = \dot v\,\vec\tau + \frac{v^2}{\rho}\,\vec n",
                     np.array([0.0, -2.7, 0.0]), scale=0.75)
        self.play(Write(eq))
        self.play(FadeIn(self.caption(
            "Urinma tashkil etuvchi tezlikni, normal esa yo'nalishni o'zgartiradi")))
        self.wait(1.4)
        self.play(FadeIn(block))


class CoriolisScene(MexanikaScene):
    """Bir xil harakat ikki kadrda: inersial va aylanuvchi."""

    subject_code = "NM-06"
    scene_title = "Koriolis effekti: ikki kadr"

    def construct(self):
        block = self.show_title()
        om = 0.9
        T = np.linspace(0.0, 2.6, 120)

        # inersial kadrda — to'g'ri chiziq
        left_c = np.array([-3.3, -0.3, 0.0])
        right_c = np.array([3.3, -0.3, 0.0])
        disc_l = Circle(radius=2.0, color=RULE, stroke_width=1.6).move_to(left_c)
        disc_r = Circle(radius=2.0, color=RULE, stroke_width=1.6).move_to(right_c)
        t1 = label("Inersial kadr", left_c + UP * 2.35, scale=0.42)
        t2 = label("Aylanuvchi kadr", right_c + UP * 2.35, scale=0.42)
        self.play(Create(disc_l), Create(disc_r), Write(t1), Write(t2))

        straight = [left_c + np.array([0.0, -1.85 + 1.45 * t, 0.0]) for t in T]
        spiral = []
        for t in T:
            r = -1.85 + 1.45 * t
            a = -om * t
            spiral.append(right_c + np.array([r * np.sin(a), r * np.cos(a), 0.0]))

        self.play(Create(curve(straight, color=COMPRESS, width=3)),
                  Create(curve(spiral, color=TENSION, width=3)), run_time=2.2)

        eq = formula(r"\vec a_{abs} = \vec a_{rel} + \vec a_{tr} "
                     r"+ 2\,\vec\omega\times\vec v_{rel}",
                     np.array([0.0, -2.75, 0.0]), scale=0.68)
        self.play(Write(eq))
        self.play(FadeIn(self.caption(
            "Bir xil harakat: inersial kadrda to'g'ri, aylanuvchi kadrda egri")))
        self.wait(1.5)
        self.play(FadeIn(block))
