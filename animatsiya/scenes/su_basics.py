"""SU: sonli hisoblash asoslari."""
from __future__ import annotations

import numpy as np
from manim import Create, FadeIn, FadeOut, Line, Polygon, Write, VGroup, DOWN, LEFT, RIGHT, UP

from _common import (
    COMPRESS, INK, MARK, MexanikaScene, RULE, TENSION, axis_pair, curve, dashed, dot_at,
    formula, label, sampled,
)


class DiscretizationScene(MexanikaScene):
    """Uzluksiz masala chekli sonli noma'lumga almashadi."""

    subject_code = "SU-01"
    scene_title = "Diskretlashtirish va xatolik byudjeti"

    def construct(self):
        block = self.show_title()
        O = np.array([-5.0, 0.9, 0.0])

        def f(x):
            return 0.9 * np.sin(np.pi * x / 4.6) * (1 - 0.18 * x)
        exact = sampled(f, 0.0, 9.2, n=220, sx=1.0, sy=1.0, origin=O)
        self.play(Create(curve(exact, color=INK, width=2.8)), run_time=1.2)
        self.play(Write(label("uzluksiz yechim u(x)", O + np.array([6.0, 1.3, 0.0]),
                              scale=0.34, color=INK)))

        for n, col in ((4, TENSION), (8, COMPRESS)):
            xs = np.linspace(0.0, 9.2, n + 1)
            pts = [O + np.array([x, f(x), 0.0]) for x in xs]
            self.play(Create(curve(pts, color=col, width=2.2)),
                      FadeIn(VGroup(*[dot_at(p, color=col) for p in pts])), run_time=0.8)
            self.play(Write(label(f"n = {n}", O + np.array([9.6, f(9.2) - 0.35 * (n == 8), 0.0]),
                                  scale=0.32, color=col, mono=True)), run_time=0.3)

        rows = VGroup(
            label("XATOLIK BYUDJETI", np.array([-3.4, -1.5, 0.0]), scale=0.38, color=INK),
            label("model xatosi      — to'r maydalansa ham QOLADI",
                  np.array([-3.4, -1.95, 0.0]), scale=0.32, color=TENSION, mono=True),
            label("diskretlashtirish — h -> 0 da nolga intiladi",
                  np.array([-3.4, -2.35, 0.0]), scale=0.32, color=COMPRESS, mono=True),
            label("yaxlitlash        — h -> 0 da O'SADI",
                  np.array([-3.4, -2.75, 0.0]), scale=0.32, color=MARK, mono=True),
        )
        for r in rows:
            self.play(Write(r), run_time=0.4)
        self.play(FadeIn(self.caption(
            "To'rni cheksiz maydalash yordam bermaydi — uchala manba birga qaraladi")))
        self.wait(1.4)
        self.play(FadeIn(block))


class CancellationScene(MexanikaScene):
    """Yaqin sonlarni ayirish ma'noli raqamlarni yo'q qiladi."""

    subject_code = "SU-02"
    scene_title = "Katastrofik qisqarish"

    def construct(self):
        block = self.show_title()
        a, b = 1.0000001, 1.0000000
        rows = [
            ("a = 1,0000001", INK), ("b = 1,0000000", INK),
            ("a - b = 0,0000001", TENSION),
            ("8 ta ma'noli raqamdan 1 tasi qoldi", MARK),
        ]
        y = 2.0
        for txt, col in rows:
            self.play(Write(label(txt, np.array([-3.2, y, 0.0]), scale=0.42,
                                  color=col, mono=True)), run_time=0.5)
            y -= 0.62

        # amaliy misol: kvadrat tenglama
        A, B, C = 1.0, 1e8, 1.0
        naive = (-B + np.sqrt(B * B - 4 * A * C)) / (2 * A)
        stable = (2 * C) / (-B - np.sqrt(B * B - 4 * A * C))
        cmp_rows = VGroup(
            label("x^2 + 1e8 x + 1 = 0", np.array([2.6, 1.9, 0.0]), scale=0.4,
                  color=INK, mono=True),
            label(f"oddiy formula: {naive:.6e}", np.array([2.6, 1.35, 0.0]), scale=0.34,
                  color=TENSION, mono=True),
            label(f"barqaror shakl: {stable:.6e}", np.array([2.6, 0.9, 0.0]), scale=0.34,
                  color=COMPRESS, mono=True),
            label(f"nisbiy xato: {abs(naive-stable)/abs(stable)*100:.1f}%",
                  np.array([2.6, 0.45, 0.0]), scale=0.34, color=MARK, mono=True),
        )
        for r in cmp_rows:
            self.play(Write(r), run_time=0.45)

        eq = formula(r"x_1 = \frac{-b+\sqrt{b^2-4ac}}{2a} \ \longrightarrow\ "
                     r"x_1 = \frac{2c}{-b-\sqrt{b^2-4ac}}",
                     np.array([0.0, -1.9, 0.0]), scale=0.55)
        self.play(Write(eq))
        self.play(Write(label("Ayni matematika, boshqa arifmetika",
                              np.array([0.0, -2.5, 0.0]), scale=0.38, color=TENSION)))
        self.wait(1.4)
        self.play(FadeIn(block))


class OptimalStepScene(MexanikaScene):
    """Kesish va yaxlitlash xatolari qarama-qarshi yo'nalishda."""

    subject_code = "SU-03"
    scene_title = "Kesish va yaxlitlash xatoliklarining raqobati"

    def construct(self):
        block = self.show_title()
        O = np.array([-4.6, -2.1, 0.0])
        axes = axis_pair(O, x_len=9.2, y_len=4.4, x_label=r"\log h", y_label=r"\log E")
        self.play(Create(axes))

        eps = 2.2e-16
        hs = np.logspace(-11, -1, 200)
        trunc = hs / 2.0
        roundo = 2 * eps / hs
        total = trunc + roundo

        def lg(v):
            return (np.log10(v) + 14.0) * 0.30
        sx = 0.78
        cut = [O + np.array([(np.log10(h) + 11.2) * sx, lg(t), 0.0]) for h, t in zip(hs, trunc)]
        rnd = [O + np.array([(np.log10(h) + 11.2) * sx, lg(t), 0.0]) for h, t in zip(hs, roundo)]
        tot = [O + np.array([(np.log10(h) + 11.2) * sx, lg(t), 0.0]) for h, t in zip(hs, total)]

        self.play(Create(curve(cut, color=COMPRESS, width=2.2)), run_time=0.7)
        self.play(Write(label("kesish ~ h", np.array([2.2, 1.35, 0.0]), scale=0.33,
                              color=COMPRESS, mono=True)))
        self.play(Create(curve(rnd, color=MARK, width=2.2)), run_time=0.7)
        self.play(Write(label("yaxlitlash ~ eps/h", np.array([-2.6, 1.35, 0.0]),
                              scale=0.33, color=MARK, mono=True)))
        self.play(Create(curve(tot, color=TENSION, width=3)), run_time=1.0)

        h_opt = float(np.sqrt(4 * eps))
        i = int(np.argmin(total))
        self.play(FadeIn(dot_at(tot[i], color=TENSION, r=0.1)),
                  Create(dashed(tot[i], np.array([tot[i][0], O[1], 0.0]))))
        self.play(Write(label(f"h_opt ~ sqrt(eps) = {h_opt:.1e}",
                              tot[i] + np.array([1.9, 0.5, 0.0]), scale=0.34,
                              color=TENSION, mono=True)))

        eq = formula(r"E(h) \approx \frac{h}{2}|f''| + \frac{2\varepsilon}{h}",
                     np.array([2.6, -2.7, 0.0]), scale=0.58)
        self.play(Write(eq))
        self.play(FadeIn(self.caption(
            "Qadamni cheksiz kichraytirish aniqlikni YOMONLASHTIRADI")))
        self.wait(1.4)
        self.play(FadeIn(block))


class ConditioningScene(MexanikaScene):
    """Deyarli parallel chiziqlar: kichik o'zgarish yechimni uchiradi."""

    subject_code = "SU-04"
    scene_title = "Shartlanganlik va deyarli parallel chiziqlar"

    def construct(self):
        block = self.show_title()
        for k, (m2, name, col) in enumerate([(0.55, "yaxshi shartlangan", COMPRESS),
                                             (1.02, "yomon shartlangan", TENSION)]):
            O = np.array([-3.2 + 6.4 * k, -0.4, 0.0])
            ax = VGroup(Line(O + LEFT * 2.2, O + RIGHT * 2.4, color=INK, stroke_width=1.8),
                        Line(O + DOWN * 1.6, O + UP * 2.2, color=INK, stroke_width=1.8))
            self.play(Create(ax), run_time=0.35)

            l1 = curve([O + np.array([t, 1.0 * t + 0.35, 0.0]) for t in (-2.0, 2.2)],
                       color=INK, width=2.4)
            l2 = curve([O + np.array([t, m2 * t - 0.25, 0.0]) for t in (-2.0, 2.2)],
                       color=col, width=2.4)
            self.play(Create(l1), Create(l2), run_time=0.5)

            A = np.array([[1.0, -1.0], [m2, -1.0]])
            kappa = float(np.linalg.cond(A))
            xs = (0.35 + 0.25) / (m2 - 1.0) if abs(m2 - 1.0) > 1e-9 else 0.0
            if abs(xs) < 2.1:
                self.play(FadeIn(dot_at(O + np.array([xs, 1.0 * xs + 0.35, 0.0]),
                                        color=MARK, r=0.09)), run_time=0.3)

            # buzilgan tizim
            l2p = curve([O + np.array([t, (m2 * 1.02) * t - 0.25, 0.0]) for t in (-2.0, 2.2)],
                        color=RULE, width=1.6)
            self.play(Create(l2p), run_time=0.35)

            self.play(Write(label(name, O + np.array([0.0, -2.0, 0.0]), scale=0.36,
                                  color=col)),
                      Write(label(f"kappa = {kappa:.1f}", O + np.array([0.0, -2.42, 0.0]),
                                  scale=0.34, color=col, mono=True)), run_time=0.4)

        eq = formula(r"\frac{\|\delta x\|}{\|x\|} \le "
                     r"\kappa(\mathbf A)\frac{\|\delta b\|}{\|b\|}",
                     np.array([0.0, 2.45, 0.0]), scale=0.66)
        self.play(Write(eq))
        self.play(FadeIn(self.caption(
            "Kappa — masalaning o'z xossasi, algoritmniki emas")))
        self.wait(1.4)
        self.play(FadeIn(block))


class FactorizationScene(MexanikaScene):
    """Qayta raqamlash lentani toraytiradi va to'ldirilishni kamaytiradi."""

    subject_code = "SU-05"
    scene_title = "Lenta, to'ldirilish va qayta raqamlash"

    def construct(self):
        block = self.show_title()
        rng = np.random.default_rng(3)
        n = 14
        s = 0.28

        def draw(mat, centre, col, title):
            g = VGroup()
            for i in range(n):
                for j in range(n):
                    if mat[i, j]:
                        p = centre + np.array([(j - n / 2) * s, (n / 2 - i) * s, 0.0])
                        g.add(dot_at(p, color=col, r=0.072))
            frame = Polygon(centre + np.array([-n / 2 * s, n / 2 * s, 0]),
                            centre + np.array([n / 2 * s, n / 2 * s, 0]),
                            centre + np.array([n / 2 * s, -n / 2 * s, 0]),
                            centre + np.array([-n / 2 * s, -n / 2 * s, 0]),
                            color=RULE, stroke_width=1.4)
            lab = label(title, centre + np.array([0.0, -n / 2 * s - 0.45, 0.0]),
                        scale=0.34, color=INK)
            cnt = label(f"lenta = {_bw(mat)}", centre + np.array([0.0, -n / 2 * s - 0.82, 0.0]),
                        scale=0.3, color=col, mono=True)
            return VGroup(frame, g, lab, cnt)

        # tabiiy (uch diagonalli) va tasodifiy raqamlash
        base = np.zeros((n, n), dtype=bool)
        for i in range(n):
            base[i, i] = True
            if i: base[i, i - 1] = base[i - 1, i] = True
        perm = rng.permutation(n)
        shuffled = base[perm][:, perm]

        self.play(Create(draw(shuffled, np.array([-3.4, 0.4, 0.0]), TENSION,
                              "to'r generatori bergan tartib")), run_time=1.2)
        self.play(Create(draw(base, np.array([3.4, 0.4, 0.0]), COMPRESS,
                              "RCM dan keyin")), run_time=1.2)

        eq = formula(r"\text{amallar} \approx 2Nb^2,\qquad "
                     r"\text{xotira} \approx Nb",
                     np.array([0.0, -2.75, 0.0]), scale=0.6)
        self.play(Write(eq))
        self.play(Write(label("b kvadrat ko'rinishda kiradi — shuning uchun tartiblash arzon yutuq",
                              np.array([0.0, -3.25, 0.0]), scale=0.34, color=MARK)))
        self.wait(1.4)
        self.play(FadeIn(block))


def _bw(mat) -> int:
    idx = np.argwhere(mat)
    return int(np.max(np.abs(idx[:, 0] - idx[:, 1]))) if len(idx) else 0


class IterativeScene(MexanikaScene):
    """Yakobi, Gauss-Zeydel va CG ning yaqinlashishi."""

    subject_code = "SU-06"
    scene_title = "Iterativ yechuvchilarning yaqinlashishi"

    def construct(self):
        block = self.show_title()
        O = np.array([-4.6, -2.2, 0.0])
        axes = axis_pair(O, x_len=9.2, y_len=4.4, x_label="iteratsiya", y_label=r"\log\|r\|")
        self.play(Create(axes))

        # haqiqiy hisob: uch diagonalli tizim
        n = 40
        A = np.diag(2.0 * np.ones(n)) + np.diag(-np.ones(n - 1), 1) + np.diag(-np.ones(n - 1), -1)
        b = np.ones(n)
        D = np.diag(np.diag(A))
        L = np.tril(A, -1)
        U = np.triu(A, 1)

        def resid(x):
            return float(np.linalg.norm(b - A @ x))

        hist = {}
        # Yakobi
        x = np.zeros(n); h = [resid(x)]
        for _ in range(60):
            x = np.linalg.solve(D, b - (L + U) @ x); h.append(resid(x))
        hist["Yakobi"] = (h, RULE)
        # Gauss-Zeydel
        x = np.zeros(n); h = [resid(x)]
        for _ in range(60):
            x = np.linalg.solve(D + L, b - U @ x); h.append(resid(x))
        hist["Gauss-Zeydel"] = (h, COMPRESS)
        # CG
        x = np.zeros(n); r = b - A @ x; p = r.copy(); h = [resid(x)]
        rr = float(r @ r)
        for _ in range(60):
            # CG aniq arifmetikada n qadamda TUGAYDI; to'xtatish mezonisiz
            # keyingi qadamda p @ Ap = 0 bo'lib, nolga bo'linish chiqadi.
            if np.sqrt(rr) <= 1e-12 * np.linalg.norm(b):
                break
            Ap = A @ p
            al = rr / float(p @ Ap)
            x = x + al * p
            r = r - al * Ap
            rr_new = float(r @ r)
            p = r + (rr_new / rr) * p
            rr = rr_new
            h.append(resid(x))
        hist["CG"] = (h, TENSION)

        for k, (name, (h, col)) in enumerate(hist.items()):
            pts = []
            for i, v in enumerate(h):
                if v <= 0:
                    break
                y = (np.log10(v) + 14.0) * 0.28
                pts.append(O + np.array([i * 0.145, max(y, 0.05), 0.0]))
            self.play(Create(curve(pts, color=col, width=2.6)), run_time=0.8)
            self.play(Write(label(f"{name}: {len(pts)} iteratsiya",
                                  np.array([2.4, 2.4 - 0.45 * k, 0.0]), scale=0.33,
                                  color=col, mono=True)), run_time=0.3)

        eq = formula(r"k \le \tfrac{1}{2}\sqrt{\kappa}\,\ln\frac{2}{\varepsilon}",
                     np.array([2.6, -2.85, 0.0]), scale=0.6, color=TENSION)
        self.play(Write(eq))
        self.play(FadeIn(self.caption(
            "CG kappa ning KVADRAT ILDIZIGA bog'liq — asosiy yutug'i shu")))
        self.wait(1.4)
        self.play(FadeIn(block))
