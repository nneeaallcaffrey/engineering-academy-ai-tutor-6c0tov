"""NM: dempfirlash, rezonans va xususiy shakllar."""
from __future__ import annotations

import numpy as np
from manim import Create, FadeIn, Line, Write, VGroup, DOWN, LEFT, RIGHT, UP

from _common import (
    COMPRESS, INK, MARK, MexanikaScene, RULE, TENSION, axis_pair, curve, dashed, dot_at,
    formula, label, sampled,
)


class DampingRegimesScene(MexanikaScene):
    """Uchta rejim: kam, kritik va ortiqcha dempfirlash."""

    subject_code = "NM-26"
    scene_title = "Dempfirlash rejimlari"

    def construct(self):
        block = self.show_title()
        O = np.array([-5.0, -0.4, 0.0])
        axes = axis_pair(O, x_len=10.0, y_len=2.4, x_label="t", y_label="x")
        base = Line(O, O + RIGHT * 9.8, color=RULE, stroke_width=1.2)
        self.play(Create(axes), Create(base))

        wn = 3.0
        cases = [(0.08, TENSION, "zeta = 0,08 — kam dempfirlash"),
                 (1.00, INK, "zeta = 1,00 — kritik"),
                 (2.20, COMPRESS, "zeta = 2,20 — ortiqcha")]
        for k, (z, col, name) in enumerate(cases):
            def x(t, z=z):
                if z < 1:
                    wd = wn * np.sqrt(1 - z**2)
                    return np.exp(-z * wn * t) * (np.cos(wd * t) + z * wn / wd * np.sin(wd * t))
                if abs(z - 1) < 1e-9:
                    return (1 + wn * t) * np.exp(-wn * t)
                r = wn * np.sqrt(z**2 - 1)
                a, b = -z * wn + r, -z * wn - r
                return (b * np.exp(a * t) - a * np.exp(b * t)) / (b - a)

            pts = sampled(x, 0.0, 6.0, n=220, sx=1.63, sy=1.7, origin=O)
            self.play(Create(curve(pts, color=col, width=2.6)), run_time=1.3)
            self.play(Write(label(name, np.array([2.3, 2.15 - 0.42 * k, 0.0]),
                                  scale=0.36, color=col, mono=True)), run_time=0.4)

        eq = formula(r"m\ddot x + c\dot x + kx = 0,\qquad "
                     r"\zeta = \frac{c}{2\sqrt{km}}",
                     np.array([-2.6, -2.5, 0.0]), scale=0.62)
        self.play(Write(eq))
        self.play(FadeIn(self.caption(
            "Kritik dempfirlash — tebranishsiz eng tez qaytish")))
        self.wait(1.5)
        self.play(FadeIn(block))


class ResonanceScene(MexanikaScene):
    """Amplituda-chastota tavsifi: zeta kamayganda cho'qqi o'sadi."""

    subject_code = "NM-27"
    scene_title = "Rezonans va AChT"

    def construct(self):
        block = self.show_title()
        O = np.array([-4.8, -2.2, 0.0])
        axes = axis_pair(O, x_len=9.4, y_len=4.6, x_label=r"\beta=\omega/\omega_n", y_label="M")
        self.play(Create(axes))

        for i, (z, col) in enumerate(((0.05, TENSION), (0.12, MARK),
                                      (0.30, COMPRESS), (0.70, RULE))):
            def M(b, z=z):
                return 1.0 / np.sqrt((1 - b**2) ** 2 + (2 * z * b) ** 2)
            pts = sampled(M, 0.02, 2.6, n=260, sx=3.4, sy=0.38, origin=O)
            self.play(Create(curve(pts, color=col, width=2.5)), run_time=0.85)
            peak = 1.0 / (2 * z * np.sqrt(1 - z**2)) if z < 0.707 else 1.0
            self.play(Write(label(f"zeta={z:.2f}  M_max={peak:.1f}",
                                  np.array([3.1, 2.1 - 0.42 * i, 0.0]),
                                  scale=0.33, color=col, mono=True)), run_time=0.35)

        res = dashed(O + np.array([3.4, 0.0, 0.0]), O + np.array([3.4, 4.3, 0.0]))
        self.play(Create(res), Write(label("beta = 1", O + np.array([3.4, 4.5, 0.0]),
                                           scale=0.35, color=INK, mono=True)))
        eq = formula(r"M = \frac{1}{\sqrt{(1-\beta^2)^2 + (2\zeta\beta)^2}}",
                     np.array([2.4, -2.75, 0.0]), scale=0.6)
        self.play(Write(eq))
        self.play(FadeIn(self.caption(
            "Rezonansda amplitudani faqat dempfirlash cheklaydi")))
        self.wait(1.5)
        self.play(FadeIn(block))


class ModeShapesScene(MexanikaScene):
    """Uch massali tizimning uchta xususiy shakli."""

    subject_code = "NM-29"
    scene_title = "Xususiy shakllar"

    def construct(self):
        block = self.show_title()

        # uch massali zanjir: K va M dan xususiy qiymat masalasi
        n = 3
        K = np.array([[2.0, -1.0, 0.0], [-1.0, 2.0, -1.0], [0.0, -1.0, 1.0]])
        w2, V = np.linalg.eigh(K)
        order = np.argsort(w2)
        cols = [TENSION, MARK, COMPRESS]

        for j, idx in enumerate(order):
            phi = V[:, idx]
            phi = phi / np.max(np.abs(phi))
            y0 = 1.85 - 1.75 * j
            base = Line(np.array([-4.6, y0, 0.0]), np.array([4.6, y0, 0.0]),
                        color=RULE, stroke_width=1.2)
            pts = [np.array([-4.6, y0, 0.0])]
            for i in range(n):
                pts.append(np.array([-4.6 + 2.3 * (i + 1), y0 + phi[i] * 0.62, 0.0]))
            shape = curve(pts, color=cols[j], width=3)
            masses = VGroup(*[dot_at(p, color=cols[j], r=0.1) for p in pts[1:]])
            freq = label(f"omega_{j+1} = {np.sqrt(w2[idx]):.3f}",
                         np.array([5.0, y0, 0.0]), scale=0.34, color=cols[j], mono=True)
            nodes = sum(1 for a, b in zip(phi[:-1], phi[1:]) if a * b < 0)
            nl = label(f"{nodes} tugun", np.array([-5.4, y0, 0.0]), scale=0.32,
                       color=RULE, mono=True)
            self.play(Create(base), Create(shape), FadeIn(masses),
                      Write(freq), Write(nl), run_time=0.95)

        eq = formula(r"(\mathbf K - \omega^2\mathbf M)\boldsymbol\phi = 0",
                     np.array([0.0, -3.0, 0.0]), scale=0.62)
        self.play(Write(eq))
        self.play(FadeIn(self.caption(
            "Chastota ortgani sari tugunlar soni bittaga ko'payadi")))
        self.wait(1.5)
        self.play(FadeIn(block))
