"""SU: zamonaviy usullar va verifikatsiya."""
from __future__ import annotations

import numpy as np
from manim import Circle, Create, FadeIn, Line, Polygon, Write, VGroup, DOWN, LEFT, RIGHT, UP

from _common import (
    COMPRESS, INK, MARK, MexanikaScene, RULE, TENSION, axis_pair, curve, dashed, dot_at,
    formula, label, sampled,
)


class DQMScene(MexanikaScene):
    """DQM shabloni GLOBAL: har bir tugun hammasi bilan bog'langan."""

    subject_code = "SU-25"
    scene_title = "Global shablon va spektral yaqinlashish"

    def construct(self):
        block = self.show_title()
        n = 9
        # chap: FEM/FD mahalliy shabloni
        for k, (name, glob, col) in enumerate([("chekli ayirmalar", False, COMPRESS),
                                               ("DQM", True, TENSION)]):
            y0 = 2.0 - 1.5 * k
            xs = np.linspace(-4.4, 1.4, n)
            base = Line(np.array([-4.6, y0, 0.0]), np.array([1.6, y0, 0.0]),
                        color=RULE, stroke_width=1.2)
            self.play(Create(base), run_time=0.25)
            for x in xs:
                self.add(dot_at(np.array([x, y0, 0.0]), color=INK, r=0.06))
            c = xs[n // 2]
            targets = xs if glob else xs[n // 2 - 1:n // 2 + 2]
            for x in targets:
                if abs(x - c) < 1e-9:
                    continue
                self.add(curve([np.array([c, y0, 0.0]),
                                np.array([(c + x) / 2, y0 + 0.42, 0.0]),
                                np.array([x, y0, 0.0])], color=col, width=1.6))
            self.play(Write(label(name, np.array([3.2, y0, 0.0]), scale=0.38, color=col)),
                      Write(label(f"{len(targets)} bog'lanish", np.array([3.2, y0 - 0.38, 0.0]),
                                  scale=0.3, color=RULE, mono=True)), run_time=0.4)

        # spektral yaqinlashish grafigi
        O = np.array([-4.4, -2.5, 0.0])
        axes = axis_pair(O, x_len=8.8, y_len=2.3, x_label="N", y_label=r"\log E")
        self.play(Create(axes))
        ns = np.arange(4, 22, 2)
        alg = 1.0 / ns**2.0
        spec = np.exp(-0.75 * ns)
        for vals, col, name in ((alg, COMPRESS, "algebraik ~ N^-2"),
                                (spec, TENSION, "spektral ~ e^-cN")):
            pts = [O + np.array([(i / (len(ns) - 1)) * 8.4,
                                 (np.log10(v) + 9.0) * 0.22, 0.0])
                   for i, v in enumerate(vals)]
            self.play(Create(curve(pts, color=col, width=2.4)), run_time=0.7)
            self.play(Write(label(name, pts[-1] + np.array([-1.6, 0.35, 0.0]),
                                  scale=0.3, color=col, mono=True)), run_time=0.3)

        self.play(Write(label("A * 1 = 0  ->  diagonal qator yig'indisidan topiladi",
                              np.array([0.0, -0.35, 0.0]), scale=0.34, color=MARK, mono=True)))
        self.wait(1.3)
        self.play(FadeIn(block))


class BEMScene(MexanikaScene):
    """BEM o'lchamni bittaga kamaytiradi: faqat chegara diskretlashtiriladi."""

    subject_code = "SU-26"
    scene_title = "O'lcham kamayishi"

    def construct(self):
        block = self.show_title()
        for k, (name, interior, col) in enumerate([("FEM", True, COMPRESS),
                                                   ("BEM", False, TENSION)]):
            c = np.array([-3.2 + 6.4 * k, 0.5, 0.0])
            R = 1.7
            self.play(Create(Circle(radius=R, color=INK, stroke_width=2.4).move_to(c)),
                      run_time=0.3)
            if interior:
                cnt = 0
                for r in np.linspace(0.3, R * 0.92, 5):
                    m = max(6, int(2 * np.pi * r / 0.42))
                    for t in np.linspace(0, 2 * np.pi, m, endpoint=False):
                        self.add(dot_at(c + np.array([r * np.cos(t), r * np.sin(t), 0.0]),
                                        color=col, r=0.045))
                        cnt += 1
                cnt += 24
            else:
                cnt = 24
            for t in np.linspace(0, 2 * np.pi, 24, endpoint=False):
                self.add(dot_at(c + np.array([R * np.cos(t), R * np.sin(t), 0.0]),
                                color=col, r=0.065))
            self.play(Write(label(name, c + np.array([0.0, -2.2, 0.0]), scale=0.42,
                                  color=col)),
                      Write(label(f"~{cnt} noma'lum", c + np.array([0.0, -2.6, 0.0]),
                                  scale=0.34, color=col, mono=True)), run_time=0.4)

        rows = VGroup(
            formula(r"c\,u_i + \int_\Gamma u\,q^*\,d\Gamma = \int_\Gamma q\,u^*\,d\Gamma",
                    np.array([0.0, 2.6, 0.0]), scale=0.55),
            label("+ matritsa TO'LA va NOSIMMETRIK", np.array([0.0, -3.05, 0.0]),
                  scale=0.34, color=MARK),
            label("+ qattiq jism usuli: H_ii = -sum_{j!=i} H_ij", np.array([0.0, -3.45, 0.0]),
                  scale=0.32, color=RULE, mono=True),
        )
        for r in rows:
            self.play(Write(r), run_time=0.45)
        self.wait(1.3)
        self.play(FadeIn(block))


class MeshfreeScene(MexanikaScene):
    """Aniqlik va shartlanganlik orasidagi noaniqlik prinsipi."""

    subject_code = "SU-27"
    scene_title = "To'rsizlik va noaniqlik prinsipi"

    def construct(self):
        block = self.show_title()
        # tarqoq nuqtalar — to'r yo'q
        rng = np.random.default_rng(7)
        c = np.array([-3.4, 0.6, 0.0])
        pts = []
        for _ in range(70):
            p = rng.uniform(-1.7, 1.7, size=2)
            if np.hypot(*p) <= 1.7:
                pts.append(c + np.array([p[0], p[1], 0.0]))
        self.play(Create(Circle(radius=1.7, color=INK, stroke_width=2.2).move_to(c)))
        self.play(FadeIn(VGroup(*[dot_at(p, color=COMPRESS, r=0.055) for p in pts])),
                  run_time=0.9)
        self.play(Write(label("element yo'q — faqat nuqtalar",
                              c + np.array([0.0, -2.2, 0.0]), scale=0.36, color=COMPRESS)))

        O = np.array([0.8, -2.2, 0.0])
        axes = axis_pair(O, x_len=4.6, y_len=4.4, x_label=r"shakl parametri \epsilon",
                         y_label="log")
        self.play(Create(axes))
        eps = np.linspace(0.3, 4.0, 120)
        err = np.exp(-2.6 / eps) * 1e-2
        cond = np.exp(3.4 / eps)
        for vals, col, name in ((err, TENSION, "xato"), (cond, COMPRESS, "kappa")):
            pts2 = [O + np.array([(e - 0.3) / 3.7 * 4.2,
                                  np.clip((np.log10(v) + 6.0) * 0.32, 0.05, 4.2), 0.0])
                    for e, v in zip(eps, vals)]
            self.play(Create(curve(pts2, color=col, width=2.4)), run_time=0.8)
            self.play(Write(label(name, pts2[-1] + np.array([0.3, 0.0, 0.0]),
                                  scale=0.32, color=col, mono=True)), run_time=0.25)

        self.play(Write(label("Shaxbak: ikkalasini bir vaqtda yaxshilab bo'lmaydi",
                              np.array([0.4, 2.55, 0.0]), scale=0.36, color=MARK)))
        self.play(FadeIn(self.caption(
            "Optimal epsilon shartlanganlik 1/eps bilan bir tartibga chiqqan joyda")))
        self.wait(1.4)
        self.play(FadeIn(block))


class VerificationScene(MexanikaScene):
    """MMS: aniq yechimni TANLAYMIZ va manbani undan chiqaramiz."""

    subject_code = "SU-28"
    scene_title = "MMS va tartib o'lchovi"

    def construct(self):
        block = self.show_title()
        steps = VGroup(
            label("1.  u_ex(x) ni TANLAYMIZ", np.array([-3.4, 2.3, 0.0]), scale=0.4,
                  color=COMPRESS, mono=True),
            label("2.  f = L(u_ex) ni CHIQARAMIZ", np.array([-3.4, 1.85, 0.0]), scale=0.4,
                  color=COMPRESS, mono=True),
            label("3.  kodga f ni beramiz", np.array([-3.4, 1.4, 0.0]), scale=0.4,
                  color=COMPRESS, mono=True),
            label("4.  natijani u_ex bilan solishtiramiz", np.array([-3.4, 0.95, 0.0]),
                  scale=0.4, color=COMPRESS, mono=True),
        )
        for s in steps:
            self.play(Write(s), run_time=0.45)

        O = np.array([-4.6, -2.6, 0.0])
        axes = axis_pair(O, x_len=9.2, y_len=3.0, x_label=r"\log h", y_label=r"\log E")
        self.play(Create(axes))

        hs = np.array([1 / 4, 1 / 8, 1 / 16, 1 / 32, 1 / 64])
        for p, col, name in ((2.0, COMPRESS, "p = 2 (chiziqli)"),
                             (4.0, TENSION, "p = 4 (kubik)"),
                             (1.0, MARK, "p = 1 (XATO bor!)")):
            e = hs ** p
            pts = [O + np.array([(np.log10(h) + 1.9) * 3.6,
                                 (np.log10(v) + 7.5) * 0.35, 0.0])
                   for h, v in zip(hs, e)]
            self.play(Create(curve(pts, color=col, width=2.4)),
                      FadeIn(VGroup(*[dot_at(q, color=col, r=0.06) for q in pts])),
                      run_time=0.7)
            self.play(Write(label(name, pts[0] + np.array([0.7, 0.3, 0.0]), scale=0.3,
                                  color=col, mono=True)), run_time=0.3)

        eq = VGroup(
            formula(r"p_{obs} = \frac{\ln(E_1/E_2)}{\ln r}",
                    np.array([2.9, 0.35, 0.0]), scale=0.58),
            formula(r"\mathrm{GCI} = \frac{F_s|\varepsilon|}{r^{p}-1}",
                    np.array([2.9, -0.35, 0.0]), scale=0.58, color=MARK),
            label("p_obs nazariydan past -> kodda xato bor",
                  np.array([2.6, -1.05, 0.0]), scale=0.32, color=TENSION),
        )
        for e in eq:
            self.play(Write(e), run_time=0.5)
        self.play(FadeIn(self.caption(
            "Kuzatilgan tartib nazariyga mos kelishi — kod to'g'riligining eng kuchli dalili")))
        self.wait(1.4)
        self.play(FadeIn(block))
