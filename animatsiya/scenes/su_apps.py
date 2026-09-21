"""SU: chekli elementlar usulining ilovalari."""
from __future__ import annotations

import numpy as np
from scipy.linalg import eigh
from manim import Create, FadeIn, FadeOut, Line, Polygon, Write, VGroup, DOWN, LEFT, RIGHT, UP

from _common import (
    COMPRESS, INK, MARK, MexanikaScene, RULE, TENSION, axis_pair, curve, dashed, dot_at,
    formula, hatched, label, sampled, support_pin,
)


class TrussScene(MexanikaScene):
    """Ferma elementi: faqat o'qiy kuch; termik ta'sir mahkamlanganda kuch beradi."""

    subject_code = "SU-19"
    scene_title = "Ferma: kuchlar va termik ta'sir"

    def construct(self):
        block = self.show_title()
        span, h = 6.4, 1.8
        nb = 4
        bot = [np.array([-span / 2 + span * i / nb, 0.4, 0.0]) for i in range(nb + 1)]
        top = [np.array([-span / 2 + span * (i + 0.5) / nb, 0.4 + h, 0.0]) for i in range(nb)]

        bars = []
        for i in range(nb):
            bars.append((bot[i], bot[i + 1], +1.0))
        for i in range(nb - 1):
            bars.append((top[i], top[i + 1], -1.0))
        for i in range(nb):
            bars.append((bot[i], top[i], -0.6))
            bars.append((top[i], bot[i + 1], +0.6))

        self.play(Create(VGroup(*[Line(a, b, color=RULE, stroke_width=2.2)
                                  for a, b, _ in bars])), run_time=1.2)
        self.play(Create(VGroup(support_pin(bot[0]), support_pin(bot[-1]))))

        coloured = VGroup(*[Line(a, b, color=TENSION if s > 0 else COMPRESS,
                                 stroke_width=2.4 + 2.2 * abs(s))
                            for a, b, s in bars])
        self.play(Create(coloured), run_time=1.4)

        rows = VGroup(
            formula(r"\mathbf k_e = \frac{EA}{L}\begin{bmatrix} c^2 & cs & -c^2 & -cs\\"
                    r" cs & s^2 & -cs & -s^2\\ -c^2 & -cs & c^2 & cs\\"
                    r" -cs & -s^2 & cs & s^2\end{bmatrix}",
                    np.array([0.0, -1.55, 0.0]), scale=0.46),
            formula(r"\mathbf f_T = EA\,\alpha\,\Delta T\,[-c,\,-s,\,c,\,s]^T",
                    np.array([0.0, -2.55, 0.0]), scale=0.52, color=MARK),
            label("Statik aniqmas fermada isish KUCH keltiradi",
                  np.array([0.0, -3.05, 0.0]), scale=0.34, color=MARK),
        )
        for r in rows:
            self.play(Write(r), run_time=0.5)
        self.play(FadeIn(self.caption(
            "Statik aniq fermada isish faqat siljish beradi, kuch bermaydi")))
        self.wait(1.4)
        self.play(FadeIn(block))


class BeamFrameScene(MexanikaScene):
    """Ermit bazisi: to'rtta kubik funksiya."""

    subject_code = "SU-20"
    scene_title = "Ermit bazisi va moment epyurasi"

    def construct(self):
        block = self.show_title()
        O = np.array([-5.0, 1.7, 0.0])
        L = 4.4

        def N(xi):
            return np.array([
                0.25 * (1 - xi) ** 2 * (2 + xi),
                0.125 * (1 - xi) ** 2 * (1 + xi),
                0.25 * (1 + xi) ** 2 * (2 - xi),
                -0.125 * (1 + xi) ** 2 * (1 - xi)])

        cols = [TENSION, MARK, COMPRESS, RULE]
        names = ["N1 (w1)", "N2 (th1)", "N3 (w2)", "N4 (th2)"]
        base = Line(O, O + RIGHT * L, color=INK, stroke_width=1.6)
        self.play(Create(base))
        for k in range(4):
            pts = [O + np.array([(xi + 1) / 2 * L, N(xi)[k] * 1.3, 0.0])
                   for xi in np.linspace(-1, 1, 90)]
            self.play(Create(curve(pts, color=cols[k], width=2.4)), run_time=0.5)
            self.play(Write(label(names[k], np.array([0.4, 2.3 - 0.42 * k, 0.0]),
                                  scale=0.32, color=cols[k], mono=True)), run_time=0.25)

        # NAZORAT: birlikning yoyilishi sum N_i(w=1) = 1
        chk = max(abs(N(xi)[0] + N(xi)[2] - 1.0) for xi in np.linspace(-1, 1, 21))
        self.play(Write(label(f"N1 + N3 = 1 tekshiruvi: xato {chk:.1e}",
                              np.array([2.6, 2.3, 0.0]), scale=0.32, color=INK, mono=True)))

        # ramka va moment epyurasi
        A = np.array([-4.2, -2.6, 0.0]); B = np.array([-4.2, -0.6, 0.0])
        C = np.array([0.4, -0.6, 0.0]); D = np.array([0.4, -2.6, 0.0])
        frame = VGroup(Line(A, B, color=INK, stroke_width=3),
                       Line(B, C, color=INK, stroke_width=3),
                       Line(C, D, color=INK, stroke_width=3))
        self.play(Create(frame))
        ep = hatched(B, C, [0.35, -0.2, -0.75, -0.2, 0.35], n=16, scale=0.55)
        self.play(Create(ep), run_time=0.8)
        self.play(Write(label("M epyurasi", np.array([2.2, -1.1, 0.0]), scale=0.34,
                              color=RULE)))
        self.play(Write(label("k = (EI/L_rigel)/(EI/L_ustun)", np.array([2.6, -1.7, 0.0]),
                              scale=0.3, color=MARK, mono=True)))
        self.play(Write(label("portal: M = (2+3k)/(1+6k) * ...", np.array([2.6, -2.1, 0.0]),
                              scale=0.3, color=MARK, mono=True)))
        self.wait(1.3)
        self.play(FadeIn(block))


class StressConcentrationScene(MexanikaScene):
    """Kirsh yechimi: teshik chetida kuchlanish uch barobar."""

    subject_code = "SU-21"
    scene_title = "Teshik atrofidagi kuchlanish"

    def construct(self):
        block = self.show_title()
        from manim import Circle
        c = np.array([-3.0, 0.3, 0.0])
        R = 0.85
        plate = Polygon(c + np.array([-2.6, -2.0, 0]), c + np.array([2.6, -2.0, 0]),
                        c + np.array([2.6, 2.0, 0]), c + np.array([-2.6, 2.0, 0]),
                        color=RULE, stroke_width=2, fill_opacity=0.04)
        hole = Circle(radius=R, color=INK, stroke_width=2.6).move_to(c)
        self.play(Create(plate), Create(hole))
        for y in np.linspace(-1.5, 1.5, 5):
            self.add(Line(c + np.array([-3.3, y, 0]), c + np.array([-2.7, y, 0]),
                          color=COMPRESS, stroke_width=2.4))
            self.add(Line(c + np.array([2.7, y, 0]), c + np.array([3.3, y, 0]),
                          color=COMPRESS, stroke_width=2.4))
        self.play(Write(formula(r"\sigma_\infty", c + np.array([-3.7, 0.0, 0]),
                                scale=0.45, color=COMPRESS)))

        self.play(FadeIn(dot_at(c + np.array([0.0, R, 0.0]), color=TENSION, r=0.09)),
                  FadeIn(dot_at(c + np.array([0.0, -R, 0.0]), color=TENSION, r=0.09)))
        self.play(Write(label("3 sigma", c + np.array([0.75, R + 0.2, 0]), scale=0.36,
                              color=TENSION, mono=True)))
        self.play(FadeIn(dot_at(c + np.array([R, 0.0, 0.0]), color=COMPRESS, r=0.09)))
        self.play(Write(label("-1 sigma", c + np.array([R + 0.85, 0.0, 0]), scale=0.36,
                              color=COMPRESS, mono=True)))

        O = np.array([1.6, -2.0, 0.0])
        axes = axis_pair(O, x_len=4.6, y_len=4.0, x_label="r/a", y_label=r"\sigma_\theta/\sigma")
        self.play(Create(axes))

        def kirsch(t):       # theta = 90 gradus
            return 1.0 + 0.5 / t**2 + 1.5 / t**4
        pts = sampled(kirsch, 1.0, 4.0, n=160, sx=1.05, sy=1.05, origin=O)
        self.play(Create(curve(pts, color=TENSION, width=2.8)), run_time=1.0)
        self.play(Write(label("r/a = 1 da aynan 3,00", O + np.array([1.5, 3.55, 0.0]),
                              scale=0.32, color=TENSION, mono=True)))
        self.play(Write(label(f"r/a = 3 da {kirsch(3.0):.3f}", O + np.array([2.6, 1.55, 0.0]),
                              scale=0.32, color=RULE, mono=True)))

        eq = formula(r"\sigma_\theta(a,\tfrac{\pi}{2}) = 3\sigma_\infty",
                     np.array([-3.0, -2.9, 0.0]), scale=0.6)
        self.play(Write(eq))
        self.play(FadeIn(self.caption(
            "Konsentratsiya teshik O'LCHAMIGA emas, SHAKLIGA bog'liq")))
        self.wait(1.4)
        self.play(FadeIn(block))


class PlateLockingScene(MexanikaScene):
    """Yupqa plastinada to'liq integrallash javobni nolga tortadi."""

    subject_code = "SU-22"
    scene_title = "Plastina qulflanishi"

    def construct(self):
        block = self.show_title()
        O = np.array([-4.6, -2.0, 0.0])
        axes = axis_pair(O, x_len=9.2, y_len=4.2, x_label="a/h", y_label=r"w_{FEM}/w_{Navye}")
        self.play(Create(axes))

        lvl = Line(O + np.array([0.0, 3.1, 0.0]), O + np.array([8.8, 3.1, 0.0]),
                   color=RULE, stroke_width=1.8)
        self.play(Create(lvl))

        ratios = np.array([10.0, 20.0, 50.0, 100.0, 200.0, 500.0])
        full = 1.0 / (1.0 + (ratios / 48.0) ** 2)
        sri = np.array([0.986, 0.994, 0.997, 0.998, 0.998, 0.998])
        sx = 3.2
        for vals, col, name in ((full, TENSION, "to'liq integrallash"),
                                (sri, COMPRESS, "SRI")):
            pts = [O + np.array([np.log10(r) * sx - 2.6, v * 3.1, 0.0])
                   for r, v in zip(ratios, vals)]
            self.play(Create(curve(pts, color=col, width=2.8)),
                      FadeIn(VGroup(*[dot_at(p, color=col) for p in pts])), run_time=0.9)
            self.play(Write(label(name, pts[-1] + np.array([-1.4, 0.4, 0.0]),
                                  scale=0.34, color=col)), run_time=0.3)

        rows = VGroup(
            label("Qulflanish sababi: yupqa chegarada siljish energiyasi",
                  np.array([0.0, 2.65, 0.0]), scale=0.34, color=TENSION),
            label("egilish energiyasini BO'G'IB qo'yadi",
                  np.array([0.0, 2.25, 0.0]), scale=0.34, color=TENSION),
            label("Davo: siljish hadini kamaytirilgan tartibda integrallash",
                  np.array([0.0, -2.75, 0.0]), scale=0.34, color=COMPRESS),
        )
        for r in rows:
            self.play(Write(r), run_time=0.45)
        self.wait(1.3)
        self.play(FadeIn(block))


class EigenScene(MexanikaScene):
    """Tebranish va ustuvorlik — bitta xususiy qiymat masalasi."""

    subject_code = "SU-23"
    scene_title = "Tebranish va ustuvorlik birligi"

    def construct(self):
        block = self.show_title()
        left = VGroup(
            formula(r"(\mathbf K - \omega^2\mathbf M)\boldsymbol\phi = 0",
                    np.array([-3.2, 2.1, 0.0]), scale=0.62, color=COMPRESS),
            label("tebranish: M — massa matritsasi", np.array([-3.2, 1.5, 0.0]),
                  scale=0.32, color=COMPRESS),
        )
        right = VGroup(
            formula(r"(\mathbf K + \lambda\mathbf K_G)\boldsymbol\phi = 0",
                    np.array([3.2, 2.1, 0.0]), scale=0.62, color=TENSION),
            label("ustuvorlik: K_G — geometrik bikrlik", np.array([3.2, 1.5, 0.0]),
                  scale=0.32, color=TENSION),
        )
        self.play(Write(left[0])); self.play(Write(left[1]))
        self.play(Write(right[0])); self.play(Write(right[1]))
        self.play(Create(Line(np.array([-0.9, 1.85, 0.0]), np.array([0.9, 1.85, 0.0]),
                              color=RULE, stroke_width=2)))
        self.play(Write(label("bir xil algoritm", np.array([0.0, 2.2, 0.0]), scale=0.32,
                              color=RULE)))

        # HAQIQIY hisob: konsol balka chastotalari
        n = 30
        L = 1.0
        h = L / n
        nd = 2 * (n + 1)                 # n element -> n+1 tugun, tugunda 2 dof
        K = np.zeros((nd, nd))
        M = np.zeros((nd, nd))
        ke = np.array([[12, 6 * h, -12, 6 * h], [6 * h, 4 * h * h, -6 * h, 2 * h * h],
                       [-12, -6 * h, 12, -6 * h], [6 * h, 2 * h * h, -6 * h, 4 * h * h]]) / h**3
        me = np.array([[156, 22 * h, 54, -13 * h], [22 * h, 4 * h * h, 13 * h, -3 * h * h],
                       [54, 13 * h, 156, -22 * h],
                       [-13 * h, -3 * h * h, -22 * h, 4 * h * h]]) * h / 420.0
        for e in range(n):
            idx = [2 * e, 2 * e + 1, 2 * e + 2, 2 * e + 3]
            K[np.ix_(idx, idx)] += ke
            M[np.ix_(idx, idx)] += me
        free = np.arange(2, nd)          # chap uchda w = theta = 0
        # UMUMLASHGAN simmetrik masala: M^-1 K simmetrik EMAS, shuning uchun
        # eigvalsh ni unga qo'llash mumkin emas - u faqat quyi uchburchakni o'qiydi.
        w2 = eigh(K[np.ix_(free, free)], M[np.ix_(free, free)], eigvals_only=True)
        w = np.sqrt(np.abs(w2))[:3]
        exact = np.array([1.875104, 4.694091, 7.854757]) ** 2

        rows = VGroup(label("Konsol balka (n = 30 element):", np.array([0.0, 0.5, 0.0]),
                            scale=0.36, color=INK))
        for i in range(3):
            err = abs(w[i] - exact[i]) / exact[i] * 100
            rows.add(label(f"  mode {i+1}:  FEM {w[i]:9.3f}   aniq {exact[i]:9.3f}"
                           f"   xato {err:6.3f}%",
                           np.array([0.0, 0.05 - 0.42 * i, 0.0]), scale=0.32,
                           color=MARK if err < 1 else TENSION, mono=True))
        self.play(Write(rows))

        self.play(Write(label("Ikkalasida ham: eng kichik xususiy qiymat hal qiluvchi",
                              np.array([0.0, -1.6, 0.0]), scale=0.36, color=INK)))
        self.play(Write(label("HRZ jamlash massani saqlaydi va M ni maxsus qilmaydi",
                              np.array([0.0, -2.1, 0.0]), scale=0.33, color=RULE)))
        self.wait(1.4)
        self.play(FadeIn(block))


class SnapThroughScene(MexanikaScene):
    """Chegaraviy nuqtadan keyin tizim sakrab o'tadi."""

    subject_code = "SU-24"
    scene_title = "O'tib ketish hodisasi"

    def construct(self):
        block = self.show_title()
        O = np.array([-1.0, -0.4, 0.0])
        axes = VGroup(
            Line(O + LEFT * 3.2, O + RIGHT * 4.4, color=INK, stroke_width=2),
            Line(O + DOWN * 2.0, O + UP * 2.4, color=INK, stroke_width=2),
            formula("w", O + RIGHT * 4.6, scale=0.5),
            formula("P", O + UP * 2.6, scale=0.5),
        )
        self.play(Create(axes))

        # ikkita sterjenli ravoq: P(w) egri chizig'i
        b, hh, EA = 1.0, 0.18, 1.0
        L0 = float(np.hypot(b, hh))
        ws = np.linspace(-0.02, 2 * hh + 0.02, 400)

        def P(w):
            s = hh - w
            L = np.hypot(b, s)
            dL = (w * w - 2 * hh * w) / (L + L0)     # qisqarishsiz shakl
            return -2 * EA * dL / L0 * s / L

        vals = np.array([P(w) for w in ws])
        sx = 3.4 / (2 * hh)
        sy = 1.9 / max(abs(vals))
        pts = [O + np.array([w * sx, v * sy, 0.0]) for w, v in zip(ws, vals)]
        self.play(Create(curve(pts, color=TENSION, width=3)), run_time=1.6)

        imax = int(np.argmax(vals)); imin = int(np.argmin(vals))
        self.play(FadeIn(dot_at(pts[imax], color=MARK, r=0.095)),
                  FadeIn(dot_at(pts[imin], color=MARK, r=0.095)))
        self.play(Write(label("chegaraviy nuqta", pts[imax] + np.array([1.2, 0.3, 0.0]),
                              scale=0.32, color=MARK)))

        jump = Line(pts[imax], np.array([pts[imax][0] + 2.4, pts[imax][1], 0.0]),
                    color=COMPRESS, stroke_width=2.4)
        self.play(Create(jump))
        self.play(Write(label("sakrash", pts[imax] + np.array([1.4, -0.35, 0.0]),
                              scale=0.32, color=COMPRESS)))

        rows = VGroup(
            label("Kuch boshqaruvida: sakrash muqarrar", np.array([-4.2, 1.9, 0.0]),
                  scale=0.32, color=TENSION),
            label("Siljish boshqaruvida: egri to'liq kuzatiladi", np.array([-4.2, 1.5, 0.0]),
                  scale=0.32, color=COMPRESS),
            label("Yoy uzunligi usuli: har ikkalasi ham", np.array([-4.2, 1.1, 0.0]),
                  scale=0.32, color=MARK),
            formula(r"\mathbf K_T \Delta\mathbf u = \mathbf R - \mathbf F(\mathbf u)",
                    np.array([-3.0, -2.5, 0.0]), scale=0.55),
        )
        for r in rows:
            self.play(Write(r), run_time=0.45)
        self.play(FadeIn(self.caption(
            "Chegaraviy nuqtada K_T maxsus — Nyuton usuli shu yerda yiqiladi")))
        self.wait(1.4)
        self.play(FadeIn(block))
