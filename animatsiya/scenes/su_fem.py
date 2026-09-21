"""SU: chekli elementlar usulining asoslari."""
from __future__ import annotations

import numpy as np
from manim import Create, FadeIn, FadeOut, Line, Polygon, Write, VGroup, DOWN, LEFT, RIGHT, UP

from _common import (
    COMPRESS, INK, MARK, MexanikaScene, RULE, TENSION, axis_pair, curve, dashed, dot_at,
    formula, label, sampled,
)


class WeakFormScene(MexanikaScene):
    """Kuchli shakldan zaifga: bir marta integrallash tartibni tushiradi."""

    subject_code = "SU-13"
    scene_title = "Zaif formulirovka va bazis funksiyalari"

    def construct(self):
        block = self.show_title()
        steps = [
            (r"-\frac{d}{dx}\left(EA\frac{du}{dx}\right) = f", "kuchli shakl", COMPRESS),
            (r"-\int_0^L v\,\frac{d}{dx}\left(EA\frac{du}{dx}\right)dx = \int_0^L v f\,dx",
             "sinov funksiyasiga ko'paytiramiz", RULE),
            (r"\int_0^L EA\frac{du}{dx}\frac{dv}{dx}dx = \int_0^L v f\,dx + [\,\cdot\,]_0^L",
             "bo'laklab integrallash", MARK),
        ]
        y = 2.2
        for tex, note, col in steps:
            self.play(Write(formula(tex, np.array([0.0, y, 0.0]), scale=0.56, color=col)),
                      run_time=0.9)
            self.play(Write(label(note, np.array([0.0, y - 0.45, 0.0]), scale=0.3,
                                  color=RULE)), run_time=0.35)
            y -= 1.15

        self.play(Write(label("u ikki marta emas, BIR marta differensiallanadi",
                              np.array([0.0, -0.9, 0.0]), scale=0.38, color=TENSION)))

        # bazis funksiyalari
        O = np.array([-4.6, -2.7, 0.0])
        base = Line(O, O + RIGHT * 9.2, color=INK, stroke_width=2)
        self.play(Create(base))
        h = 1.53
        for i in range(1, 6):
            xc = i * h
            pts = [O + np.array([xc - h, 0.0, 0.0]), O + np.array([xc, 1.0, 0.0]),
                   O + np.array([xc + h, 0.0, 0.0])]
            col = TENSION if i == 3 else RULE
            self.play(Create(curve(pts, color=col, width=2.6 if i == 3 else 1.6)),
                      run_time=0.3)
        for i in range(0, 7):
            self.add(dot_at(O + np.array([i * h, 0.0, 0.0]), color=INK, r=0.06))
        self.play(Write(label("shlyapa funksiyalari: qo'shni elementlardagina nolmas",
                              O + np.array([4.6, -0.5, 0.0]), scale=0.32, color=RULE)))
        self.wait(1.3)
        self.play(FadeIn(block))


class IsoparametricScene(MexanikaScene):
    """Ideal kvadrat haqiqiy elementga akslantiriladi; Yakobian nazorat qiladi."""

    subject_code = "SU-14"
    scene_title = "Izoparametrik almashtirish"

    def construct(self):
        block = self.show_title()
        c1 = np.array([-3.4, 0.3, 0.0])
        s = 1.25
        ref = Polygon(c1 + np.array([-s, -s, 0]), c1 + np.array([s, -s, 0]),
                      c1 + np.array([s, s, 0]), c1 + np.array([-s, s, 0]),
                      color=COMPRESS, stroke_width=2.6, fill_opacity=0.06)
        self.play(Create(ref))
        self.play(Write(label("ideal element", c1 + np.array([0.0, -1.85, 0.0]),
                              scale=0.36, color=COMPRESS)),
                  Write(formula(r"(\xi,\eta)", c1 + np.array([0.0, 1.75, 0.0]),
                                scale=0.5, color=COMPRESS)))

        c2 = np.array([2.6, 0.3, 0.0])
        nodes = [c2 + np.array([-1.5, -1.1, 0]), c2 + np.array([1.7, -1.4, 0]),
                 c2 + np.array([1.2, 1.5, 0]), c2 + np.array([-1.7, 0.9, 0])]
        real = Polygon(*nodes, color=TENSION, stroke_width=2.6, fill_opacity=0.06)
        self.play(Create(real))
        self.play(Write(label("haqiqiy element", c2 + np.array([0.0, -2.05, 0.0]),
                              scale=0.36, color=TENSION)),
                  Write(formula("(x,y)", c2 + np.array([0.0, 2.05, 0.0]),
                                scale=0.5, color=TENSION)))

        arrow = curve([np.array([-1.7, 0.3, 0.0]), np.array([0.5, 0.3, 0.0])],
                      color=RULE, width=2.4)
        self.play(Create(arrow))
        self.play(Write(formula(r"x = \sum N_i(\xi,\eta)\,x_i",
                                np.array([-0.6, 0.85, 0.0]), scale=0.46, color=RULE)))

        # Yakobian aniqlovchisi — haqiqatan hisoblanadi
        xy = np.array([[n[0] - c2[0], n[1] - c2[1]] for n in nodes])
        dets = []
        for xi, eta in ((-0.577, -0.577), (0.577, -0.577), (0.577, 0.577), (-0.577, 0.577)):
            dN = 0.25 * np.array([
                [-(1 - eta), -(1 - xi)], [(1 - eta), -(1 + xi)],
                [(1 + eta), (1 + xi)], [-(1 + eta), (1 - xi)]])
            J = dN.T @ xy
            dets.append(float(np.linalg.det(J)))
        rows = VGroup(
            label("Gauss nuqtalarida det J:", np.array([0.0, -2.75, 0.0]),
                  scale=0.34, color=INK),
            label("  ".join(f"{d:.3f}" for d in dets), np.array([0.0, -3.15, 0.0]),
                  scale=0.34, color=MARK if min(dets) > 0 else TENSION, mono=True),
        )
        self.play(Write(rows))
        self.play(Write(label("det J > 0 — akslantirish teskarilanadi",
                              np.array([0.0, 2.15, 0.0]), scale=0.36, color=MARK)))
        self.wait(1.3)
        self.play(FadeIn(block))


class AssemblyScene(MexanikaScene):
    """Element matritsalari global matritsaga QO'SHILADI."""

    subject_code = "SU-15"
    scene_title = "Global tizimni yig'ish"

    def construct(self):
        block = self.show_title()
        n = 5
        s = 0.62
        c = np.array([2.8, 0.3, 0.0])

        # global matritsa katakchalari
        cells = {}
        for i in range(n):
            for j in range(n):
                p = c + np.array([(j - n / 2 + 0.5) * s, (n / 2 - 0.5 - i) * s, 0.0])
                cells[(i, j)] = p
                self.add(Polygon(p + np.array([-s / 2, -s / 2, 0]),
                                 p + np.array([s / 2, -s / 2, 0]),
                                 p + np.array([s / 2, s / 2, 0]),
                                 p + np.array([-s / 2, s / 2, 0]),
                                 color=RULE, stroke_width=0.9))
        self.play(FadeIn(VGroup()), run_time=0.3)
        self.play(Write(label("global K", c + np.array([0.0, n / 2 * s + 0.45, 0.0]),
                              scale=0.4, color=INK)))

        # sterjenlar va ularning hissasi
        y0 = 2.0
        bar = Line(np.array([-6.0, y0, 0.0]), np.array([-1.2, y0, 0.0]),
                   color=INK, stroke_width=3)
        self.play(Create(bar))
        xs = np.linspace(-6.0, -1.2, n)
        for i, x in enumerate(xs):
            self.add(dot_at(np.array([x, y0, 0.0]), color=INK, r=0.07))
            self.add(label(f"{i}", np.array([x, y0 + 0.3, 0.0]), scale=0.28,
                           color=RULE, mono=True))

        for e in range(n - 1):
            hl = VGroup(*[Polygon(cells[(i, j)] + np.array([-s / 2, -s / 2, 0]),
                                  cells[(i, j)] + np.array([s / 2, -s / 2, 0]),
                                  cells[(i, j)] + np.array([s / 2, s / 2, 0]),
                                  cells[(i, j)] + np.array([-s / 2, s / 2, 0]),
                                  color=TENSION, stroke_width=2, fill_opacity=0.18)
                          for i in (e, e + 1) for j in (e, e + 1)])
            seg = Line(np.array([xs[e], y0, 0.0]), np.array([xs[e + 1], y0, 0.0]),
                       color=TENSION, stroke_width=5)
            self.play(Create(seg), FadeIn(hl), run_time=0.5)
            self.play(FadeOut(hl), run_time=0.25)

        rows = VGroup(
            formula(r"\mathbf K = \sum_e \mathbf L_e^T \mathbf k_e \mathbf L_e",
                    np.array([-3.6, 0.5, 0.0]), scale=0.6),
            label("qo'shni elementlar diagonalda USTMA-UST tushadi",
                  np.array([-3.6, -0.25, 0.0]), scale=0.32, color=TENSION),
            label("K simmetrik, siyrak va lentali chiqadi",
                  np.array([-3.6, -0.7, 0.0]), scale=0.32, color=COMPRESS),
            label("chegaraviy shartsiz K MAXSUS (qattiq jism harakati)",
                  np.array([-3.6, -1.15, 0.0]), scale=0.32, color=MARK),
        )
        for r in rows:
            self.play(Write(r), run_time=0.45)
        self.wait(1.3)
        self.play(FadeIn(block))


class LockingScene(MexanikaScene):
    """Qulflanish va soat mexanizmi — ikki qarama-qarshi xavf."""

    subject_code = "SU-16"
    scene_title = "Qulflanish va soat mexanizmi"

    def construct(self):
        block = self.show_title()
        O = np.array([-4.6, -2.0, 0.0])
        axes = axis_pair(O, x_len=9.2, y_len=4.2, x_label="L/h", y_label=r"w_{FEM}/w_{aniq}")
        self.play(Create(axes))

        lvl = Line(O + np.array([0.0, 3.0, 0.0]), O + np.array([8.8, 3.0, 0.0]),
                   color=RULE, stroke_width=1.8)
        self.play(Create(lvl), Write(label("1,0", O + np.array([9.0, 3.0, 0.0]),
                                           scale=0.32, color=RULE, mono=True)))

        rs = np.linspace(2.0, 100.0, 200)
        full = 1.0 / (1.0 + (rs / 26.0) ** 2)
        sri = np.ones_like(rs) * 0.995
        self.play(Create(curve([O + np.array([np.log10(r) * 4.2 - 1.1, f * 3.0, 0.0])
                                for r, f in zip(rs, full)], color=TENSION, width=2.8)),
                  run_time=1.1)
        self.play(Write(label("to'liq integrallash — QULFLANADI",
                              np.array([2.2, 0.55, 0.0]), scale=0.34, color=TENSION)))
        self.play(Create(curve([O + np.array([np.log10(r) * 4.2 - 1.1, f * 3.0, 0.0])
                                for r, f in zip(rs, sri)], color=COMPRESS, width=2.8)),
                  run_time=0.9)
        self.play(Write(label("tanlab kamaytirilgan (SRI) — to'g'ri",
                              np.array([2.4, 3.35, 0.0]), scale=0.34, color=COMPRESS)))

        # soat mexanizmi shakli
        c = np.array([3.4, 1.4, 0.0])
        s = 0.55
        sq = Polygon(c + np.array([-s, -s, 0]), c + np.array([s, -s, 0]),
                     c + np.array([s, s, 0]), c + np.array([-s, s, 0]),
                     color=RULE, stroke_width=1.6)
        hg = Polygon(c + np.array([-s * 1.35, -s * 0.65, 0]),
                     c + np.array([s * 0.65, -s * 1.35, 0]),
                     c + np.array([s * 1.35, s * 0.65, 0]),
                     c + np.array([-s * 0.65, s * 1.35, 0]),
                     color=MARK, stroke_width=2.2)
        self.play(Create(sq), Create(hg))
        self.play(Write(label("soat mexanizmi:", c + np.array([0.0, 1.15, 0.0]),
                              scale=0.3, color=MARK)),
                  Write(label("energiyasiz shakl", c + np.array([0.0, -1.15, 0.0]),
                              scale=0.3, color=MARK)))

        self.play(Write(label("To'liq: qulflanish   |   To'liq kamaytirilgan: soat mexanizmi",
                              np.array([0.0, -2.7, 0.0]), scale=0.36, color=INK)))
        self.play(FadeIn(self.caption(
            "SRI ikkala xavf orasidan o'tadi: egilish to'liq, siljish kamaytirilgan")))
        self.wait(1.4)
        self.play(FadeIn(block))


class BoundaryRecoveryScene(MexanikaScene):
    """Kuchlanish tugunlarda emas, Barlou nuqtalarida aniqroq."""

    subject_code = "SU-17"
    scene_title = "Chegaraviy shartlar va kuchlanishni tiklash"

    def construct(self):
        block = self.show_title()
        O = np.array([-4.8, 0.2, 0.0])
        axes = axis_pair(O, x_len=9.6, y_len=2.6, x_label="x", y_label=r"\sigma")
        self.play(Create(axes))

        def exact(x):
            return 1.6 * (1.0 - x / 9.2)
        pts = sampled(exact, 0.0, 9.2, n=140, sx=1.0, sy=1.0, origin=O)
        self.play(Create(curve(pts, color=INK, width=2.6)), run_time=0.9)
        self.play(Write(label("aniq kuchlanish", O + np.array([6.2, 1.15, 0.0]),
                              scale=0.32, color=INK)))

        n = 4
        h = 9.2 / n
        for e in range(n):
            x0, x1 = e * h, (e + 1) * h
            xm = 0.5 * (x0 + x1)
            val = exact(xm)
            self.add(Line(O + np.array([x0, val, 0.0]), O + np.array([x1, val, 0.0]),
                          color=TENSION, stroke_width=3))
            self.add(dot_at(O + np.array([xm, val, 0.0]), color=MARK, r=0.085))
        self.play(FadeIn(VGroup()), run_time=0.3)
        self.play(Write(label("element bo'yicha o'zgarmas (sakrash bor)",
                              O + np.array([3.0, -0.7, 0.0]), scale=0.32, color=TENSION)),
                  Write(label("Barlou nuqtalari — o'rtada, super aniq",
                              O + np.array([3.2, -1.15, 0.0]), scale=0.32, color=MARK)))

        rows = VGroup(
            label("CHEGARAVIY SHARTNI QO'YISH", np.array([-2.6, -2.05, 0.0]),
                  scale=0.36, color=INK),
            label("chiqarib tashlash — aniq, lekin tartib buziladi",
                  np.array([-2.6, -2.45, 0.0]), scale=0.31, color=RULE, mono=True),
            label("jarima (penalty)  — sodda, kappa yomonlashadi",
                  np.array([-2.6, -2.8, 0.0]), scale=0.31, color=RULE, mono=True),
            label("Lagranj            — aniq, tizim kattalashadi",
                  np.array([-2.6, -3.15, 0.0]), scale=0.31, color=RULE, mono=True),
        )
        for r in rows:
            self.play(Write(r), run_time=0.4)
        self.wait(1.3)
        self.play(FadeIn(block))


class AdaptiveMeshScene(MexanikaScene):
    """Xatolik ko'rsatkichi to'rni o'zi maydalaydigan joyni tanlaydi."""

    subject_code = "SU-18"
    scene_title = "Adaptiv to'rning rivojlanishi"

    def construct(self):
        block = self.show_title()

        # uchta bosqich: to'r maxsuslik atrofida quyuqlashadi
        for k in range(3):
            y0 = 2.0 - 1.55 * k
            base = Line(np.array([-4.8, y0, 0.0]), np.array([3.2, y0, 0.0]),
                        color=INK, stroke_width=2)
            self.play(Create(base), run_time=0.25)

            # x = 0 (chap chet) da maxsuslik: elementlar u yerda maydalanadi
            edges = [0.0]
            n = 6 * (k + 1)
            for i in range(1, n + 1):
                edges.append((i / n) ** (1.0 + 0.9 * k))
            for e in edges:
                x = -4.8 + 8.0 * e
                self.add(Line(np.array([x, y0 - 0.22, 0.0]), np.array([x, y0 + 0.22, 0.0]),
                              color=TENSION if e < 0.25 else RULE, stroke_width=2))
            self.play(Write(label(f"{k+1}-bosqich: {n} element",
                                  np.array([4.4, y0, 0.0]), scale=0.34,
                                  color=INK, mono=True)), run_time=0.35)

        self.play(FadeIn(dot_at(np.array([-4.8, 2.0, 0.0]), color=MARK, r=0.1)),
                  Write(label("maxsuslik", np.array([-4.8, 2.45, 0.0]), scale=0.32,
                              color=MARK)))

        rows = VGroup(
            formula(r"\eta_e = \|\sigma^* - \sigma^h\|_{E,e}",
                    np.array([-1.6, -1.55, 0.0]), scale=0.58, color=COMPRESS),
            label("Zenkevich-Chju ko'rsatkichi: silliqlangan va xom yechim farqi",
                  np.array([-1.0, -2.05, 0.0]), scale=0.32, color=RULE),
            label("Dorfler belgilashi: eng katta hissa beruvchi elementlar tanlanadi",
                  np.array([-1.0, -2.45, 0.0]), scale=0.32, color=MARK),
            label("Bir tekis maydalash maxsuslikda tartibni TIKLAMAYDI",
                  np.array([-1.0, -2.9, 0.0]), scale=0.34, color=TENSION),
        )
        for r in rows:
            self.play(Write(r), run_time=0.45)
        self.wait(1.3)
        self.play(FadeIn(block))
