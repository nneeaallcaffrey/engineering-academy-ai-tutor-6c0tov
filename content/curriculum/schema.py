"""Kurrikulum ma'lumot modeli (single source of truth).

Bu modul platformaning butun o'quv mazmuni uchun tipli (typed) sxemani beradi.
Mazmun Python dataclass'lari ko'rinishida yoziladi, so'ngra `export.py` orqali
`content/generated/curriculum.json` fayliga eksport qilinadi. Backend faqat
shu JSON bilan ishlaydi — ya'ni kontent qatlami backend'dan mustaqil.

Yangi mavzu qo'shish tartibi:
  1. Tegishli `s?_*.py` faylida `topic(...)` chaqiruvini qo'shing.
  2. `python -m content.curriculum.export` ni ishga tushiring.
  3. `pytest content/tests` — akademik audit avtomatik tekshiradi.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
from typing import Any, Literal

# ---------------------------------------------------------------------------
# Yagona notation (27-talab): barcha 150 mavzuda bir xil belgilar ishlatiladi.
# ---------------------------------------------------------------------------

NOTATION: list[dict[str, str]] = [
    {"symbol": r"x, y, z", "meaning": "Dekart koordinatalari", "unit": "m"},
    {"symbol": r"t", "meaning": "Vaqt", "unit": "s"},
    {"symbol": r"\mathbf{r}", "meaning": "Joy (radius) vektori", "unit": "m"},
    {"symbol": r"\mathbf{v}", "meaning": "Tezlik vektori", "unit": "m/s"},
    {"symbol": r"\mathbf{a}", "meaning": "Tezlanish vektori", "unit": "m/s²"},
    {"symbol": r"m", "meaning": "Massa", "unit": "kg"},
    {"symbol": r"\mathbf{F}", "meaning": "Kuch vektori", "unit": "N"},
    {"symbol": r"\mathbf{M}_O", "meaning": "O nuqtaga nisbatan moment", "unit": "N·m"},
    {"symbol": r"\omega", "meaning": "Burchak tezligi / chastota", "unit": "rad/s"},
    {"symbol": r"J, I", "meaning": "Inersiya momenti (massaviy / yuza)", "unit": "kg·m², m⁴"},
    {"symbol": r"u, v, w", "meaning": "Ko'chish komponentalari (displacement)", "unit": "m"},
    {"symbol": r"\sigma_{ij}", "meaning": "Kuchlanish tenzori (stress tensor)", "unit": "Pa"},
    {"symbol": r"\varepsilon_{ij}", "meaning": "Deformatsiya tenzori (strain tensor)", "unit": "—"},
    {"symbol": r"\tau", "meaning": "Urinma (siljish) kuchlanish", "unit": "Pa"},
    {"symbol": r"\gamma", "meaning": "Siljish deformatsiyasi", "unit": "—"},
    {"symbol": r"E", "meaning": "Yung moduli (Young's modulus)", "unit": "Pa"},
    {"symbol": r"G", "meaning": "Siljish moduli (shear modulus)", "unit": "Pa"},
    {"symbol": r"\nu", "meaning": "Puasson koeffitsienti (Poisson's ratio)", "unit": "—"},
    {"symbol": r"\lambda, \mu", "meaning": "Lame konstantalari", "unit": "Pa"},
    {"symbol": r"\rho", "meaning": "Zichlik", "unit": "kg/m³"},
    {"symbol": r"D", "meaning": "Plastina silindrik bikrligi", "unit": "N·m"},
    {"symbol": r"h", "meaning": "Plastina/qobiq qalinligi", "unit": "m"},
    {"symbol": r"q", "meaning": "Taqsimlangan yuklama", "unit": "N/m yoki Pa"},
    {"symbol": r"\mathbf{K}, \mathbf{M}", "meaning": "Bikrlik va massa matritsalari", "unit": "N/m, kg"},
    {"symbol": r"\nabla", "meaning": "Nabla operatori", "unit": "1/m"},
    {"symbol": r"\delta", "meaning": "Variatsiya belgisi", "unit": "—"},
]

SIGN_CONVENTION = (
    "Koordinatalar o'ng vintli (right-handed) sistemada. Cho'zuvchi normal kuchlanish "
    "musbat, siquvchi manfiy. Balkada pastga yo'nalgan yuklama musbat, egilish "
    "w(x) pastga musbat. Momentlar o'ng vint qoidasi bo'yicha musbat. Barcha "
    "hisoblarda SI birliklari ishlatiladi."
)

Difficulty = Literal["kirish", "asosiy", "murakkab", "ilg'or"]


# ---------------------------------------------------------------------------
# Dars kontenti bloklari
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class Concept:
    """Asosiy tushuncha va uning ta'rifi."""

    term: str
    definition: str


@dataclass(frozen=True)
class DerivationStep:
    """Derivatsiyaning bitta qadami: boshlang'ich → almashtirish → natija."""

    title: str
    latex: str
    explanation: str


@dataclass(frozen=True)
class Equation:
    """Mavzuning asosiy (governing) tenglamasi."""

    latex: str
    description: str
    name: str = ""


@dataclass(frozen=True)
class SolutionStep:
    latex: str
    text: str


@dataclass(frozen=True)
class WorkedExample:
    """Yechilgan muhandislik masalasi."""

    statement: str
    given: list[str]
    steps: list[SolutionStep]
    answer: str
    engineering_note: str = ""


@dataclass(frozen=True)
class QuizItem:
    """Mustahkamlash savoli. `options` bo'lsa — test, bo'lmasa — ochiq savol."""

    question: str
    answer: str
    options: list[str] = field(default_factory=list)
    correct_index: int = -1
    kind: Literal["konseptual", "hisob", "kod", "talqin"] = "konseptual"


@dataclass(frozen=True)
class LabParameter:
    """Interactive Lab'dagi boshqariladigan parametr."""

    key: str
    label: str
    minimum: float
    maximum: float
    default: float
    step: float
    unit: str = ""

    def __post_init__(self) -> None:  # pragma: no cover - sanity guard
        if not self.minimum <= self.default <= self.maximum:
            raise ValueError(f"'{self.key}' default qiymati [min, max] oralig'ida emas")
        if self.step <= 0:
            raise ValueError(f"'{self.key}' step musbat bo'lishi kerak")


@dataclass(frozen=True)
class Computation:
    """Sandbox'da ishga tushadigan Python hisobi.

    `code` ichida `PARAMS` global lug'ati mavjud deb hisoblanadi (labkit beradi),
    shuning uchun kod ham mustaqil, ham Interactive Lab rejimida ishlaydi.
    """

    caption: str
    code: str
    parameters: list[LabParameter] = field(default_factory=list)
    expected_output: str = ""

    @property
    def is_lab(self) -> bool:
        return bool(self.parameters)


@dataclass(frozen=True)
class Visualization:
    """Vizualizatsiya spetsifikatsiyasi — nima chiziladi va qaysi vosita bilan."""

    kind: str
    tool: Literal["React/SVG", "Canvas", "Matplotlib", "Manim",
                  "React/SVG + Matplotlib", "React/SVG + Manim"]
    description: str
    how_to_draw: str


@dataclass(frozen=True)
class ManimRef:
    """Manim sahnasiga havola (manim/scenes/ ichidagi real Scene klassi)."""

    scene: str
    module: str
    title: str
    summary: str


@dataclass(frozen=True)
class Lesson:
    """9-talabdagi 18 bo'limli dars strukturasi.

    1-4 bo'limlar (nom, maqsad, prerequisite, oldingi mavzu bilan bog'lanish)
    `Topic` darajasida saqlanadi, qolgani shu yerda.
    """

    physical_problem: str  # 5
    concepts: list[Concept]  # 6
    derivation: list[DerivationStep]  # 7
    formula_meaning: str  # 8
    equations: list[Equation]  # 9
    conditions: str  # 10
    worked_example: WorkedExample  # 11
    computation: Computation  # 12
    visualization: Visualization  # 13
    interpretation: str  # 14
    common_mistakes: list[str]  # 15
    quiz: list[QuizItem]  # 16
    bridge_to_next: str  # 17
    research_extension: str  # 18
    manim: ManimRef | None = None


@dataclass(frozen=True)
class Topic:
    """29-talabdagi majburiy maydonlar + to'liq dars kontenti."""

    id: str
    subject_id: str
    module_id: str
    order: int
    title: str
    description: str
    learning_objective: str
    prerequisites: list[str]
    mathematical_core: str
    engineering_application: str
    computational_component: str
    visualization_component: str
    research_extension: str
    lesson: Lesson
    difficulty: Difficulty = "asosiy"
    previous_link: str = ""
    next_topic: str | None = None
    estimated_minutes: int = 90
    tags: list[str] = field(default_factory=list)


@dataclass(frozen=True)
class Module:
    id: str
    subject_id: str
    order: int
    title: str
    summary: str
    outcome: str


@dataclass(frozen=True)
class Assessment:
    """24-talab: oraliq nazoratlar, yakuniy imtihon, loyiha."""

    kind: Literal["oraliq", "yakuniy", "loyiha"]
    title: str
    covers: str
    weight: int
    format: str


@dataclass(frozen=True)
class ProjectStage:
    name: str
    detail: str


@dataclass(frozen=True)
class FinalProject:
    """23-talab: har bir fan uchun to'liq pipeline'li yakuniy loyiha."""

    id: str
    subject_id: str
    title: str
    problem_statement: str
    stages: list[ProjectStage]
    deliverables: list[str]
    starter_code: str
    evaluation: list[str]
    parameters: list[LabParameter] = field(default_factory=list)


@dataclass(frozen=True)
class Resource:
    title: str
    author: str
    year: str
    kind: Literal["asosiy", "qoshimcha", "kurs"]
    note: str


@dataclass(frozen=True)
class Subject:
    id: str
    code: str
    order: int
    title: str
    tagline: str
    description: str
    goal: str
    prerequisites_text: str
    modules: list[Module]
    topics: list[Topic]
    assessments: list[Assessment]
    resources: list[Resource]
    accent: str
    depends_on: list[str] = field(default_factory=list)

    @property
    def topic_count(self) -> int:
        return len(self.topics)


# ---------------------------------------------------------------------------
# Qisqa yozuv uchun yordamchi funksiyalar (authoring helpers)
# ---------------------------------------------------------------------------


def c(term: str, definition: str) -> Concept:
    return Concept(term=term, definition=definition)


def d(title: str, latex: str, explanation: str) -> DerivationStep:
    return DerivationStep(title=title, latex=latex, explanation=explanation)


def eq(latex: str, description: str, name: str = "") -> Equation:
    return Equation(latex=latex, description=description, name=name)


def st(latex: str, text: str) -> SolutionStep:
    return SolutionStep(latex=latex, text=text)


def q(question: str, answer: str, kind: str = "konseptual", options: list[str] | None = None,
      correct_index: int = -1) -> QuizItem:
    return QuizItem(
        question=question,
        answer=answer,
        options=options or [],
        correct_index=correct_index,
        kind=kind,  # type: ignore[arg-type]
    )


def p(key: str, label: str, minimum: float, maximum: float, default: float, step: float,
      unit: str = "") -> LabParameter:
    return LabParameter(
        key=key, label=label, minimum=minimum, maximum=maximum,
        default=default, step=step, unit=unit,
    )


def vis(kind: str, tool: str, description: str, how_to_draw: str) -> Visualization:
    return Visualization(
        kind=kind, tool=tool,  # type: ignore[arg-type]
        description=description, how_to_draw=how_to_draw,
    )


def manim(scene: str, module: str, title: str, summary: str) -> ManimRef:
    return ManimRef(scene=scene, module=module, title=title, summary=summary)


def to_dict(obj: Any) -> Any:
    """Dataclass daraxtini JSON-ga mos dict'ga aylantiradi."""
    return asdict(obj)
