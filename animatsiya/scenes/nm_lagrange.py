"""NM: ikki karrali mayatnik va fazaviy portret."""
from __future__ import annotations

import numpy as np
from manim import Circle, Create, FadeIn, Line, Write, VGroup, DOWN, LEFT, RIGHT, UP

from _common import (
    COMPRESS, INK, MARK, MexanikaScene, RULE, TENSION, axis_pair, curve, dot_at, formula, label,
)


def _double_pendulum(th1, th2, steps=1400, dt=0.004, l1=1.0, l2=1.0, m1=1.0, m2=1.0, g=9.81):
    """Lagranj tenglamalarini Runge-Kutta 4 bilan integrallaydi."""
    def rhs(s):
        a1, a2, w1, w2 = s
        d = a1 - a2
        den = 2 * m1 + m2 - m2 * np.cos(2 * d)
        dw1 = (-g * (2 * m1 + m2) * np.sin(a1) - m2 * g * np.sin(a1 - 2 * a2)
               - 2 * np.sin(d) * m2 * (w2**2 * l2 + w1**2 * l1 * np.cos(d))) / (l1 * den)
        dw2 = (2 * np.sin(d) * (w1**2 * l1 * (m1 + m2) + g * (m1 + m2) * np.cos(a1)
               + w2**2 * l2 * m2 * np.cos(d))) / (l2 * den)
        return np.array([w1, w2, dw1, dw2])

    s = np.array([th1, th2, 0.0, 0.0])
    out = []
    for _ in range(steps):
        k1 = rhs(s); k2 = rhs(s + dt / 2 * k1)
        k3 = rhs(s + dt / 2 * k2); k4 = rhs(s + dt * k3)
        s = s + dt / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
        out.append(s.copy())
    return np.array(out)


class DoublePendulumScene(MexanikaScene):
    """Boshlang'ich shartdagi arzimas farq yo'llarni ajratib yuboradi."""

    subject_code = "NM-22"
    scene_title = "Ikki karrali mayatnik va xaos"

    def construct(self):
        block = self.show_title()
        pivot = np.array([0.0, 1.9, 0.0])
        self.play(FadeIn(dot_at(pivot, color=INK, r=0.08)))

        traces = []
        for k, (d, col) in enumerate([(0.0, TENSION), (0.001, COMPRESS)]):
            sol = _double_pendulum(2.0 + d, 2.0)
            tip = []
            for a1, a2, _, _ in sol[::6]:
                p1 = pivot + np.array([np.sin(a1), -np.cos(a1), 0.0]) * 1.25
                p2 = p1 + np.array([np.sin(a2), -np.cos(a2), 0.0]) * 1.25
                tip.append(p2)
            traces.append(curve(tip, color=col, width=1.7))

            # oxirgi holatdagi sterjenlar
            a1, a2 = sol[-1][0], sol[-1][1]
            p1 = pivot + np.array([np.sin(a1), -np.cos(a1), 0.0]) * 1.25
            p2 = p1 + np.array([np.sin(a2), -np.cos(a2), 0.0]) * 1.25
            rods = VGroup(Line(pivot, p1, color=col, stroke_width=3),
                          Line(p1, p2, color=col, stroke_width=3),
                          dot_at(p1, color=col), dot_at(p2, color=col))
            self.play(Create(traces[k]), run_time=2.0)
            self.play(Create(rods), run_time=0.6)

        d_lab = label("boshlang'ich farq: 0,001 rad", np.array([0.0, -2.75, 0.0]),
                      scale=0.38, color=MARK, mono=True)
        eq = formula(r"\frac{d}{dt}\frac{\partial L}{\partial \dot q_i}"
                     r" - \frac{\partial L}{\partial q_i} = 0",
                     np.array([4.0, 1.5, 0.0]), scale=0.6)
        self.play(Write(eq), Write(d_lab))
        self.play(FadeIn(self.caption(
            "Ikkita tenglama, ikkita erkinlik darajasi — va bashorat qilib bo'lmas yo'l")))
        self.wait(1.6)
        self.play(FadeIn(block))


class PhaseSpaceScene(MexanikaScene):
    """Mayatnikning fazaviy portreti: separatrisa ikki rejimni ajratadi."""

    subject_code = "NM-24"
    scene_title = "Mayatnik fazaviy portreti"

    def construct(self):
        block = self.show_title()
        O = np.array([0.0, -0.4, 0.0])
        axes = VGroup(
            Line(O + LEFT * 5.2, O + RIGHT * 5.2, color=INK, stroke_width=2),
            Line(O + DOWN * 2.3, O + UP * 2.3, color=INK, stroke_width=2),
            formula(r"\theta", O + RIGHT * 5.4, scale=0.5),
            formula(r"\dot\theta", O + UP * 2.5, scale=0.5),
        )
        self.play(Create(axes))

        sx, sy = 1.45, 0.62
        for E, col, w in ((0.4, COMPRESS, 2.0), (1.2, COMPRESS, 2.0),
                          (2.0, TENSION, 3.0), (2.8, MARK, 2.0), (3.6, MARK, 2.0)):
            th = np.linspace(-np.pi * 1.08, np.pi * 1.08, 400)
            val = 2 * (E - (1 - np.cos(th)))
            if E < 2.0:                                  # tebranish — yopiq halqa
                ok = val >= 0
                if not ok.any():
                    continue
                t2 = th[ok]; w2 = np.sqrt(val[ok])
                up = [O + np.array([t * sx, v * sy, 0.0]) for t, v in zip(t2, w2)]
                dn = [O + np.array([t * sx, -v * sy, 0.0]) for t, v in zip(t2[::-1], w2[::-1])]
                self.play(Create(curve(up + dn + [up[0]], color=col, width=w)), run_time=0.7)
            else:                                        # aylanish — ochiq egri
                w2 = np.sqrt(np.maximum(val, 0.0))
                up = [O + np.array([t * sx, v * sy, 0.0]) for t, v in zip(th, w2)]
                dn = [O + np.array([t * sx, -v * sy, 0.0]) for t, v in zip(th, w2)]
                self.play(Create(curve(up, color=col, width=w)),
                          Create(curve(dn, color=col, width=w)), run_time=0.7)

        centre = dot_at(O, color=INK, r=0.07)
        saddle = VGroup(dot_at(O + np.array([np.pi * sx, 0, 0]), color=TENSION),
                        dot_at(O + np.array([-np.pi * sx, 0, 0]), color=TENSION))
        self.play(FadeIn(centre), FadeIn(saddle))
        self.play(Write(label("separatrisa", O + np.array([2.1, 1.5, 0.0]),
                              scale=0.38, color=TENSION)))
        self.play(FadeIn(self.caption(
            "Separatrisa ichida — tebranish, tashqarisida — to'liq aylanish")))
        self.wait(1.5)
        self.play(FadeIn(block))
