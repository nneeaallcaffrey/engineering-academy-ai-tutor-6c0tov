"""PQ: doiraviy plastinalar va kengaytmalar."""
from __future__ import annotations

import numpy as np
from manim import Circle, Create, FadeIn, FadeOut, Line, Polygon, Write, VGroup, DOWN, LEFT, RIGHT, UP

from _common import (
    COMPRESS, INK, MARK, MexanikaScene, RULE, TENSION, axis_pair, curve, dashed, dot_at,
    formula, hatched, label, load_arrows, sampled,
)


class CircularPlateScene(MexanikaScene):
    """Qisilgan va sharnirli chetlar: egilish 4 barobar farq qiladi."""

    subject_code = "PQ-13"
    scene_title = "Doiraviy plastinaning o'qsimmetrik egilishi"

    def construct(self):
        block = self.show_title()
        nu = 0.3
        for k, (name, coef, col) in enumerate([
                ("qisilgan", 1.0 / 64.0, TENSION),
                ("sharnirli", (5 + nu) / (64 * (1 + nu)), COMPRESS)]):
            y0 = 1.5 - 2.9 * k
            a = 3.4
            base = Line(np.array([-a, y0, 0.0]), np.array([a, y0, 0.0]),
                        color=RULE, stroke_width=1.2)
            self.play(Create(base), run_time=0.3)
            # shakl funksiyalari (a = 1 ga normallashgan, amplituda coef ga mos)
            amp = 1.05 * coef / (1.0 / 64.0)
            if name == "qisilgan":
                def shape(t):
                    return (1 - t**2) ** 2
            else:
                k0 = (5 + nu) / (1 + nu)
                def shape(t, k0=k0):
                    return (1 - t**2) * (k0 - t**2) / k0
            pts = [np.array([r, y0 - amp * shape((r / a)), 0.0])
                   for r in np.linspace(-a, a, 140)]
            self.play(Create(curve(pts, color=col, width=3)), run_time=0.9)
            self.play(Create(load_arrows(np.array([-a * 0.85, y0 + 0.12, 0.0]),
                                         np.array([a * 0.85, y0 + 0.12, 0.0]),
                                         n=7, length=0.45)), run_time=0.5)
            self.play(Write(label(f"{name}: w_max = {coef:.5f} q a^4 / D",
                                  np.array([0.0, y0 - 1.75, 0.0]), scale=0.34,
                                  color=col, mono=True)), run_time=0.4)

        ratio = ((5 + nu) / (64 * (1 + nu))) / (1.0 / 64.0)
        self.play(Write(label(f"nisbat = {ratio:.3f}", np.array([4.6, -0.6, 0.0]),
                              scale=0.4, color=MARK, mono=True)))
        eq = formula(r"\frac{1}{r}\frac{d}{dr}\left\{r\frac{d}{dr}\left[\frac{1}{r}"
                     r"\frac{d}{dr}\left(r\frac{dw}{dr}\right)\right]\right\} = \frac{q}{D}",
                     np.array([0.0, -3.25, 0.0]), scale=0.5)
        self.play(Write(eq))
        self.wait(1.4)
        self.play(FadeIn(block))


class FourierHarmonicsScene(MexanikaScene):
    """Nosimmetrik yuk garmonikalarga yoyiladi."""

    subject_code = "PQ-15"
    scene_title = "Doiraviy plastinadagi garmonikalar"

    def construct(self):
        block = self.show_title()
        for n in range(4):
            c = np.array([-4.2 + 2.8 * n, 0.5, 0.0])
            R = 1.15
            self.play(Create(Circle(radius=R, color=RULE, stroke_width=1.8).move_to(c)),
                      run_time=0.3)
            pts = []
            for th in np.linspace(0, 2 * np.pi, 220):
                r = R * (1.0 + 0.3 * np.cos(n * th))
                pts.append(c + np.array([r * np.cos(th), r * np.sin(th), 0.0]))
            self.play(Create(curve(pts, color=TENSION if n % 2 == 0 else COMPRESS,
                                   width=2.6)), run_time=0.6)
            # tugun diametrlari
            for j in range(n):
                a = np.pi / (2 * n) + np.pi * j / n if n else 0.0
                if n:
                    self.add(dashed(c - np.array([np.cos(a), np.sin(a), 0.0]) * R * 1.35,
                                    c + np.array([np.cos(a), np.sin(a), 0.0]) * R * 1.35))
            self.play(Write(label(f"n = {n}", c + np.array([0.0, -1.75, 0.0]),
                                  scale=0.4, color=INK, mono=True)),
                      Write(label(f"{n} tugun diametri", c + np.array([0.0, -2.1, 0.0]),
                                  scale=0.28, color=RULE)), run_time=0.35)

        eq = formula(r"w(r,\theta) = \sum_{n} \left[w_n^{c}(r)\cos n\theta "
                     r"+ w_n^{s}(r)\sin n\theta\right]",
                     np.array([0.0, -2.9, 0.0]), scale=0.55)
        self.play(Write(eq))
        self.play(FadeIn(self.caption(
            "Har bir garmonika mustaqil — masala bitta o'zgaruvchiga keladi")))
        self.wait(1.4)
        self.play(FadeIn(block))


class ElasticFoundationScene(MexanikaScene):
    """Vinkler asosi: yuk ta'siri xarakterli uzunlikda so'nadi."""

    subject_code = "PQ-16"
    scene_title = "Vinkler asosi va xarakterli uzunlik"

    def construct(self):
        block = self.show_title()
        y0 = 0.9
        plate = Line(np.array([-5.2, y0, 0.0]), np.array([5.2, y0, 0.0]),
                     color=INK, stroke_width=3.5)
        self.play(Create(plate))

        springs = VGroup()
        for x in np.linspace(-5.0, 5.0, 26):
            zz = []
            for i in range(7):
                zz.append(np.array([x + (0.11 if i % 2 else -0.11), y0 - 0.12 - 0.09 * i, 0.0]))
            springs.add(curve(zz, color=RULE, width=1.4))
        self.play(Create(springs), run_time=1.0)
        self.play(Write(label("k (Vinkler)", np.array([-4.0, -0.15, 0.0]),
                              scale=0.34, color=RULE)))

        O = np.array([0.0, -1.6, 0.0])
        for k, (beta, col) in enumerate(((0.8, COMPRESS), (1.6, TENSION))):
            pts = []
            for x in np.linspace(-5.0, 5.0, 300):
                b = beta * abs(x)
                pts.append(O + np.array([x, -1.15 * np.exp(-b) * (np.cos(b) + np.sin(b)), 0.0]))
            self.play(Create(curve(pts, color=col, width=2.6)), run_time=0.8)
            L = np.pi / beta
            self.play(Write(label(f"beta = {beta}  ->  L_c = {L:.2f}",
                                  np.array([2.9, 0.15 - 0.42 * k, 0.0]), scale=0.32,
                                  color=col, mono=True)), run_time=0.3)

        self.play(Create(Line(np.array([0.0, y0 + 0.95, 0.0]), np.array([0.0, y0 + 0.1, 0.0]),
                              color=TENSION, stroke_width=3.5)))
        self.play(Write(formula("P", np.array([0.0, y0 + 1.2, 0.0]), scale=0.5,
                                color=TENSION)))
        eq = formula(r"D\nabla^4 w + k\,w = q,\qquad "
                     r"\ell = \sqrt[4]{\frac{D}{k}}",
                     np.array([0.0, -3.1, 0.0]), scale=0.6)
        self.play(Write(eq))
        self.play(FadeIn(self.caption(
            "Yuk ta'siri butun plastinaga emas, faqat xarakterli uzunlikka tarqaladi")))
        self.wait(1.4)
        self.play(FadeIn(block))


class LaminateScene(MexanikaScene):
    """Nosimmetrik paketda B matritsasi cho'zilish va egilishni bog'laydi."""

    subject_code = "PQ-17"
    scene_title = "Qatlamli paket va B matritsasi"

    def construct(self):
        block = self.show_title()
        c = np.array([-3.4, 0.6, 0.0])
        w, h = 3.2, 0.28

        angles = [0, 45, -45, 90]
        cols = [TENSION, MARK, MARK, COMPRESS]
        for i, (a, col) in enumerate(zip(angles, cols)):
            y = c[1] + 1.2 - i * h * 1.15
            rect = Polygon(np.array([c[0] - w / 2, y, 0]), np.array([c[0] + w / 2, y, 0]),
                           np.array([c[0] + w / 2, y - h, 0]), np.array([c[0] - w / 2, y - h, 0]),
                           color=INK, stroke_width=1.6, fill_opacity=0.12)
            self.play(Create(rect), run_time=0.3)
            for t in np.linspace(-w / 2 + 0.2, w / 2 - 0.2, 9):
                d = np.array([np.cos(np.radians(a)), 0.0, 0.0]) * 0.14
                self.add(Line(np.array([c[0] + t, y - h / 2, 0]) - d,
                              np.array([c[0] + t, y - h / 2, 0]) + d,
                              color=col, stroke_width=2))
            self.play(Write(label(f"{a}°", np.array([c[0] + w / 2 + 0.5, y - h / 2, 0]),
                                  scale=0.32, color=col, mono=True)), run_time=0.25)

        mid = dashed(np.array([c[0] - w / 2 - 0.4, c[1] + 1.2 - 2 * h * 1.15, 0]),
                     np.array([c[0] + w / 2 + 0.4, c[1] + 1.2 - 2 * h * 1.15, 0]))
        self.play(Create(mid))
        self.play(Write(label("o'rta tekislik", np.array([c[0] - w / 2 - 1.15,
                                                          c[1] + 1.2 - 2 * h * 1.15, 0]),
                              scale=0.3, color=RULE)))

        mat = VGroup(
            formula(r"\begin{bmatrix}\mathbf N\\ \mathbf M\end{bmatrix} = "
                    r"\begin{bmatrix}\mathbf A & \mathbf B\\ "
                    r"\mathbf B & \mathbf D\end{bmatrix}"
                    r"\begin{bmatrix}\boldsymbol\varepsilon^0\\ \boldsymbol\kappa\end{bmatrix}",
                    np.array([3.0, 1.0, 0.0]), scale=0.62),
            label("B = 0  ->  simmetrik paket, bog'lanish yo'q",
                  np.array([3.0, -0.4, 0.0]), scale=0.33, color=COMPRESS),
            label("B != 0 ->  cho'zilish egilishni keltiradi",
                  np.array([3.0, -0.85, 0.0]), scale=0.33, color=TENSION),
        )
        self.play(Write(mat[0])); self.play(Write(mat[1])); self.play(Write(mat[2]))
        self.play(FadeIn(self.caption(
            "Nosimmetrik paket tayyorlanishdayoq qiyshayadi — bu B ning natijasi")))
        self.wait(1.4)
        self.play(FadeIn(block))


class VonKarmanScene(MexanikaScene):
    """Katta siljishda membrana kuchlari bikrlikni oshiradi."""

    subject_code = "PQ-18"
    scene_title = "Membrana effekti va nochiziqli bikrlanish"

    def construct(self):
        block = self.show_title()
        O = np.array([-4.4, -2.1, 0.0])
        axes = axis_pair(O, x_len=8.8, y_len=4.4, x_label="w/h", y_label="q")
        self.play(Create(axes))

        lin = [O + np.array([t * 2.0, t * 2.0 * 0.95, 0.0]) for t in np.linspace(0, 2.1, 60)]
        self.play(Create(curve(lin, color=RULE, width=2.2)), run_time=0.7)
        self.play(Write(label("chiziqli (Kirxhoff)", O + np.array([4.6, 4.05, 0.0]),
                              scale=0.32, color=RULE)))

        non = [O + np.array([t * 2.0, (t + 0.38 * t**3) * 2.0 * 0.95, 0.0])
               for t in np.linspace(0, 1.55, 90)]
        self.play(Create(curve(non, color=TENSION, width=3)), run_time=1.0)
        self.play(Write(label("nochiziqli (fon Karman)", O + np.array([3.0, 2.35, 0.0]),
                              scale=0.34, color=TENSION)))

        mark = dashed(O + np.array([0.4, 0.0, 0.0]), O + np.array([0.4, 4.2, 0.0]))
        self.play(Create(mark))
        self.play(Write(label("w/h = 0,2", O + np.array([0.4, -0.35, 0.0]),
                              scale=0.3, color=MARK, mono=True)))
        self.play(Write(label("bu chegaradan keyin farq sezilarli",
                              O + np.array([2.4, 0.55, 0.0]), scale=0.3, color=MARK)))

        eq = VGroup(
            formula(r"D\nabla^4 w = q + h\,L(w,F)", np.array([2.2, -2.75, 0.0]), scale=0.55),
            formula(r"\nabla^4 F = -\tfrac{E}{2}L(w,w)", np.array([2.2, -3.2, 0.0]),
                    scale=0.55, color=COMPRESS),
        )
        self.play(Write(eq[0])); self.play(Write(eq[1]))
        self.play(FadeIn(self.caption(
            "Egilish o'rta sirtni cho'zadi — cho'zilish esa qo'shimcha bikrlik beradi")))
        self.wait(1.4)
        self.play(FadeIn(block))
