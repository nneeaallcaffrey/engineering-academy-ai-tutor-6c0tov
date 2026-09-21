"""Barcha sahnalar uchun umumiy vosita va dizayn tili.

Ranglar va shtrix uslubi frontend/DESIGN.md dagi epyura tilidan olingan:
cho'zilish — oksid qizil, siqilish — po'lat ko'k, bazaviy chiziq —
grafit. Shtrix haqiqiy chiziqlar bilan chiziladi, tekstura bilan emas.
"""

from __future__ import annotations

import numpy as np
from manim import (
    BLACK, DOWN, LEFT, ORIGIN, RIGHT, UP, Arrow, Create, DashedLine, Dot,
    FadeIn, Line, MathTex, Scene, Text, VGroup, Write,
)

INK = "#17191C"
FILM = "#E4E2DC"
PAPER = "#F6F5F2"
TENSION = "#B2402E"      # cho'zilish
COMPRESS = "#2B5A74"     # siqilish
RULE = "#9A968C"
MARK = "#D9A521"

FONT = "IBM Plex Sans Condensed"
MONO = "IBM Plex Mono"


class MexanikaScene(Scene):
    """Umumiy fon va sarlavha bloki bo'lgan asosiy sahna."""

    subject_code = ""
    scene_title = ""

    def setup(self) -> None:
        self.camera.background_color = PAPER

    def title_block(self, code: str = "", title: str = "") -> VGroup:
        code = code or self.subject_code
        title = title or self.scene_title
        tag = Text(code, font=MONO, color=RULE).scale(0.35)
        head = Text(title, font=FONT, color=INK).scale(0.52)
        rule = Line(LEFT * 6.4, RIGHT * 6.4, color=RULE, stroke_width=1)
        g = VGroup(tag, head).arrange(RIGHT, buff=0.28, aligned_edge=DOWN)
        block = VGroup(g, rule).arrange(DOWN, buff=0.14, aligned_edge=LEFT)
        block.to_edge(UP, buff=0.35).to_edge(LEFT, buff=0.6)
        return block

    def caption(self, text: str) -> Text:
        t = Text(text, font=FONT, color=INK).scale(0.38)
        t.to_edge(DOWN, buff=0.4)
        return t

    def show_title(self) -> VGroup:
        block = self.title_block()
        self.play(Write(block[0]), Create(block[1]), run_time=1.0)
        return block


def hatched(base_start, base_end, values, *, positive_color=TENSION,
            negative_color=COMPRESS, n=22, scale=1.0) -> VGroup:
    """Epyura: bazaviy chiziqqa perpendikulyar shtrixlar.

    `values` — bazaviy chiziq bo'ylab normallashgan qiymatlar (n ta).
    Musbat qiymat bir tomonga, manfiy — ikkinchi tomonga shtrixlanadi.
    """
    base_start = np.asarray(base_start, dtype=float)
    base_end = np.asarray(base_end, dtype=float)
    d = base_end - base_start
    length = float(np.linalg.norm(d))
    if length == 0:
        return VGroup()
    tangent = d / length
    normal = np.array([-tangent[1], tangent[0], 0.0])

    vals = np.asarray(values, dtype=float)
    if len(vals) != n:
        vals = np.interp(np.linspace(0, 1, n), np.linspace(0, 1, len(vals)), vals)

    strokes = VGroup()
    tips = []
    for i, v in enumerate(vals):
        p0 = base_start + tangent * (length * i / (n - 1))
        p1 = p0 + normal * (v * scale)
        tips.append(p1)
        strokes.add(Line(p0, p1,
                         color=positive_color if v >= 0 else negative_color,
                         stroke_width=2))
    outline = VGroup()
    for a, b in zip(tips[:-1], tips[1:]):
        outline.add(Line(a, b, color=INK, stroke_width=2.2))
    base = Line(base_start, base_end, color=INK, stroke_width=2.6)
    return VGroup(strokes, outline, base)


def axis_pair(origin=ORIGIN, x_len=5.0, y_len=3.0, x_label="x", y_label="y") -> VGroup:
    """Oddiy ikkita o'q — chizmadagi kabi strelkali."""
    origin = np.asarray(origin, dtype=float)
    ax = Arrow(origin, origin + RIGHT * x_len, buff=0, color=INK,
               stroke_width=2, max_tip_length_to_length_ratio=0.04)
    ay = Arrow(origin, origin + UP * y_len, buff=0, color=INK,
               stroke_width=2, max_tip_length_to_length_ratio=0.06)
    lx = MathTex(x_label, color=INK).scale(0.5).next_to(ax.get_end(), DOWN, buff=0.16)
    ly = MathTex(y_label, color=INK).scale(0.5).next_to(ay.get_end(), LEFT, buff=0.16)
    return VGroup(ax, ay, lx, ly)


def curve(points, color=INK, width=2.4) -> VGroup:
    """Nuqtalar ketma-ketligidan siniq chiziq (Manim'ning plot'iga bog'liq emas)."""
    g = VGroup()
    pts = [np.asarray(p, dtype=float) for p in points]
    for a, b in zip(pts[:-1], pts[1:]):
        g.add(Line(a, b, color=color, stroke_width=width))
    return g


def sampled(f, x0, x1, n=60, sx=1.0, sy=1.0, origin=ORIGIN):
    """f(x) ni chizish uchun nuqtalarga aylantiradi."""
    origin = np.asarray(origin, dtype=float)
    xs = np.linspace(x0, x1, n)
    return [origin + np.array([x * sx, float(f(x)) * sy, 0.0]) for x in xs]


def support_pin(point, size=0.28) -> VGroup:
    """Sharnirli tayanch — uchburchak va shtrixlangan yer."""
    p = np.asarray(point, dtype=float)
    tri = VGroup(
        Line(p, p + np.array([-size, -size * 1.5, 0.0]), color=INK, stroke_width=2),
        Line(p, p + np.array([size, -size * 1.5, 0.0]), color=INK, stroke_width=2),
        Line(p + np.array([-size, -size * 1.5, 0.0]),
             p + np.array([size, -size * 1.5, 0.0]), color=INK, stroke_width=2),
    )
    ground = VGroup()
    for k in range(5):
        x = -size + 2 * size * k / 4
        a = p + np.array([x, -size * 1.5, 0.0])
        ground.add(Line(a, a + np.array([-0.12, -0.16, 0.0]), color=RULE, stroke_width=1.6))
    return VGroup(tri, ground)


def support_fixed(point, height=0.9) -> VGroup:
    """Qisilgan (mahkamlangan) uch — vertikal chiziq va shtrix."""
    p = np.asarray(point, dtype=float)
    wall = Line(p + UP * height / 2, p + DOWN * height / 2, color=INK, stroke_width=3)
    g = VGroup(wall)
    for k in range(6):
        y = -height / 2 + height * k / 5
        a = p + np.array([0.0, y, 0.0])
        g.add(Line(a, a + np.array([-0.18, -0.16, 0.0]), color=RULE, stroke_width=1.6))
    return g


def load_arrows(start, end, n=7, length=0.6, color=COMPRESS) -> VGroup:
    """Bir tekis taqsimlangan yuk — bir qator strelka."""
    start = np.asarray(start, dtype=float)
    end = np.asarray(end, dtype=float)
    g = VGroup()
    for i in range(n):
        p = start + (end - start) * i / (n - 1)
        g.add(Arrow(p + UP * length, p, buff=0, color=color, stroke_width=2.4,
                    max_tip_length_to_length_ratio=0.28))
    g.add(Line(start + UP * length, end + UP * length, color=color, stroke_width=1.6))
    return g


def label(text, at, *, scale=0.4, color=INK, mono=False) -> Text:
    t = Text(text, font=MONO if mono else FONT, color=color).scale(scale)
    t.move_to(np.asarray(at, dtype=float))
    return t


def formula(tex, at=ORIGIN, scale=0.62, color=INK) -> MathTex:
    m = MathTex(tex, color=color).scale(scale)
    m.move_to(np.asarray(at, dtype=float))
    return m


def dot_at(p, color=TENSION, r=0.055) -> Dot:
    return Dot(np.asarray(p, dtype=float), radius=r, color=color)


def dashed(a, b, color=RULE) -> DashedLine:
    return DashedLine(np.asarray(a, dtype=float), np.asarray(b, dtype=float),
                      color=color, stroke_width=1.6, dash_length=0.09)


__all__ = [
    "MexanikaScene", "hatched", "axis_pair", "curve", "sampled", "support_pin",
    "support_fixed", "load_arrows", "label", "formula", "dot_at", "dashed",
    "INK", "FILM", "PAPER", "TENSION", "COMPRESS", "RULE", "MARK", "FONT", "MONO",
    "Scene", "VGroup", "Text", "MathTex", "Line", "Arrow", "Dot", "Create",
    "Write", "FadeIn", "UP", "DOWN", "LEFT", "RIGHT", "ORIGIN", "BLACK", "np",
]
