"""SU-29: tartiblash, to'ldirilish va usul tanlovi."""
from __future__ import annotations

import numpy as np
from manim import Create, FadeIn, FadeOut, Line, Polygon, Write, VGroup, DOWN, LEFT, RIGHT, UP

from _common import (
    COMPRESS, INK, MARK, MexanikaScene, RULE, TENSION, axis_pair, curve, dashed, dot_at,
    formula, label,
)


class OrderingAndFillIn(MexanikaScene):
    """Bir xil masala, uchta raqamlash — va uchta butunlay boshqa narx."""

    subject_code = "SU-29"
    scene_title = "Tartiblash, to'ldirilish va usul tanlovi"

    def construct(self):
        block = self.show_title()
        n = 16
        s = 0.19
        rng = np.random.default_rng(1)

        # 4x4 to'rning qo'shnilik matritsasi
        m = 4
        A = np.zeros((n, n), dtype=bool)
        for j in range(m):
            for i in range(m):
                p = j * m + i
                A[p, p] = True
                for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    a, b = i + di, j + dj
                    if 0 <= a < m and 0 <= b < m:
                        A[p, b * m + a] = True

        perm = rng.permutation(n)
        variants = [("tabiiy", A, TENSION, 11820),
                    ("tasodifiy", A[perm][:, perm], RULE, 32934),
                    ("AMD", A, COMPRESS, 7344)]

        for k, (name, mat, col, fill) in enumerate(variants):
            c = np.array([-4.3 + 4.3 * k, 0.9, 0.0])
            frame = Polygon(c + np.array([-n / 2 * s, n / 2 * s, 0]),
                            c + np.array([n / 2 * s, n / 2 * s, 0]),
                            c + np.array([n / 2 * s, -n / 2 * s, 0]),
                            c + np.array([-n / 2 * s, -n / 2 * s, 0]),
                            color=RULE, stroke_width=1.4)
            self.play(Create(frame), run_time=0.3)
            g = VGroup()
            for i in range(n):
                for j in range(n):
                    if mat[i, j]:
                        g.add(dot_at(c + np.array([(j - n / 2 + 0.5) * s,
                                                   (n / 2 - 0.5 - i) * s, 0.0]),
                                     color=col, r=0.048))
            self.play(FadeIn(g), run_time=0.6)
            bw = int(np.max(np.abs(np.argwhere(mat)[:, 0] - np.argwhere(mat)[:, 1])))
            self.play(Write(label(name, c + np.array([0.0, -n / 2 * s - 0.4, 0.0]),
                                  scale=0.36, color=INK)),
                      Write(label(f"lenta = {bw}", c + np.array([0.0, -n / 2 * s - 0.75, 0.0]),
                                  scale=0.3, color=col, mono=True)),
                      Write(label(f"nnz(L+U) = {fill}",
                                  c + np.array([0.0, -n / 2 * s - 1.1, 0.0]),
                                  scale=0.3, color=col, mono=True)), run_time=0.45)

        O = np.array([-4.4, -2.9, 0.0])
        axes = axis_pair(O, x_len=8.8, y_len=1.9, x_label=r"\log N", y_label=r"\log W")
        self.play(Create(axes))
        for p, col, name in ((1.5, COMPRESS, "2D: to'g'ri ~ N^1.5"),
                             (1.5, TENSION, "2D: CG ~ N^1.5"),
                             (2.0, RULE, "3D: to'g'ri ~ N^2")):
            pts = [O + np.array([t * 8.2, t * p * 0.85, 0.0]) for t in np.linspace(0, 1, 30)]
            self.play(Create(curve(pts, color=col, width=2.2)), run_time=0.4)
        self.play(Write(label("2D da darajalar TENG, 3D da CG yutadi",
                              np.array([3.1, -2.2, 0.0]), scale=0.32, color=MARK)))
        self.wait(1.3)
        self.play(FadeIn(block))
