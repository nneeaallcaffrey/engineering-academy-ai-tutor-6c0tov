"""TMM / 2-modul: Kuchlanish tenzori va balans qonunlari (tmm-07 … tmm-12)."""

from __future__ import annotations

from content.curriculum.schema import (
    Computation,
    Lesson,
    Topic,
    WorkedExample,
    c,
    d,
    eq,
    manim,
    p,
    q,
    st,
    vis,
)

S = "tutash-muhitlar"
M = "tmm-m2"

TOPICS = [
    Topic(
        id="tmm-07",
        subject_id=S,
        module_id=M,
        order=7,
        title="Kuchlanish vektori, Koshi teoremasi va kuchlanish tenzori",
        description=(
            "Kuchlanish vektori ta'rifi, Koshi tetraedri, kuchlanish "
            "tenzorining kelib chiqishi va maydoncha yo'nalishiga bog'liqligi."
        ),
        learning_objective=(
            "Koshi formulasini keltirib chiqarish va ixtiyoriy yo'nalishdagi "
            "maydonchadagi kuchlanishni hisoblash."
        ),
        prerequisites=["tmm-02", "mq-19"],
        mathematical_core=(
            "$t_i = \\sigma_{ij}n_j$, tetraedr muvozanati, limit o'tish, "
            "tenzor xossalari."
        ),
        engineering_application=(
            "FEM natijalarini talqin qilish, ixtiyoriy kesimdagi kuchlanish, "
            "buzilish tekisligini bashorat qilish."
        ),
        computational_component=(
            "Koshi formulasini qo'llash va turli yo'nalishlarda kuchlanish "
            "vektorini hisoblash."
        ),
        visualization_component=(
            "Koshi tetraedri va unga ta'sir etuvchi kuchlanish vektorlari."
        ),
        research_extension=(
            "Kuchlanishning boshqa o'lchovlari: Piola–Kirxgof tenzorlari "
            "katta deformatsiyalarda nima uchun kerak?"
        ),
        difficulty="murakkab",
        previous_link=(
            "mq-19 da tekis kuchlanish holatini ko'rdik. Endi uni fazoga "
            "umumlashtiramiz va kuchlanishning tenzor ekanini isbotlaymiz."
        ),
        next_topic="tmm-08",
        estimated_minutes=90,
        tags=["Koshi teoremasi", "kuchlanish tenzori", "kuchlanish vektori"],
        lesson=Lesson(
            physical_problem=(
                "Jism ichidagi nuqtada cheksiz ko'p yo'nalishdagi maydoncha "
                "o'tkazish mumkin va har birida kuchlanish har xil. Ularni "
                "hammasini saqlash imkonsiz. Koshi ajoyib natija topdi: "
                "faqat uchta o'zaro perpendikular maydonchadagi kuchlanishni "
                "bilsak, qolgan barchasi hisoblanadi."
            ),
            concepts=[
                c("Kuchlanish vektori", "$\\mathbf{t}^{(n)} = \\lim \\Delta\\mathbf{F}/\\Delta A$ — "
                  "normali $\\mathbf{n}$ bo'lgan maydonchadagi kuchlanish."),
                c("Koshi tetraedri", "Uchta koordinata tekisligi va ixtiyoriy "
                  "qiya maydoncha bilan chegaralangan elementar hajm."),
                c("Koshi formulasi", "$t_i = \\sigma_{ij}n_j$ — kuchlanish "
                  "vektorini tenzor orqali ifodalash."),
                c("Kuchlanish tenzori komponentalari", "$\\sigma_{ij}$ — "
                  "$j$ normalli maydonchadagi kuchlanishning $i$ o'qidagi "
                  "proyeksiyasi."),
                c("Normal va urinma tashkil etuvchilar", "$\\sigma_n = "
                  "\\mathbf{t}\\cdot\\mathbf{n}$, $\\tau_n = |\\mathbf{t} - "
                  "\\sigma_n\\mathbf{n}|$."),
            ],
            derivation=[
                d("1-qadam. Tetraedr muvozanati",
                  r"\mathbf{t}^{(n)}\Delta A - \mathbf{t}^{(1)}\Delta A_1 - "
                  r"\mathbf{t}^{(2)}\Delta A_2 - \mathbf{t}^{(3)}\Delta A_3 + \mathbf{b}\rho\Delta V = 0",
                  "Tetraedrga ta'sir etuvchi barcha kuchlar yig'indisi nolga "
                  "teng. $\\mathbf{b}$ — hajmiy kuch."),
                d("2-qadam. Yuzalar nisbati",
                  r"\Delta A_j = n_j\Delta A,\qquad \Delta V = \tfrac{1}{3}h\Delta A",
                  "Qiya yuzaning koordinata tekisliklariga proyeksiyasi. "
                  "Hajm esa balandlik $h$ ga proporsional."),
                d("3-qadam. Limit o'tish",
                  r"h\to0:\ \frac{\Delta V}{\Delta A} = \frac{h}{3}\to 0 "
                  r"\;\Rightarrow\; \mathbf{t}^{(n)} = \mathbf{t}^{(j)}n_j",
                  "Hajmiy kuch yuzaviy kuchga nisbatan yuqori tartibli "
                  "kichik — u yo'qoladi. Bu — Koshi isbotining kaliti."),
                d("4-qadam. Koshi formulasi",
                  r"\boxed{\;t_i = \sigma_{ij}n_j\;}",
                  "$\\sigma_{ij} = t_i^{(j)}$ deb belgilasak. Bu chiziqli "
                  "bog'lanish $\\sigma_{ij}$ ning tenzor ekanini isbotlaydi: "
                  "u vektorni vektorga chiziqli akslantiradi."),
            ],
            formula_meaning=(
                "Koshi formulasi kontinuum mexanikasining eng muhim "
                "natijalaridan biri: cheksiz ko'p maydonchadagi kuchlanish "
                "atigi 9 (simmetriya tufayli 6) ta son bilan to'liq "
                "aniqlanadi. Bu — kuchlanishning tenzor tabiati. Amaliy "
                "ma'nosi: FEM har bir tugunda 6 ta komponentani saqlaydi va "
                "ulardan istalgan kesimdagi kuchlanishni hisoblash mumkin."
            ),
            equations=[
                eq(r"t_i = \sigma_{ij}n_j", "Koshi formulasi.", "Koshi formulasi"),
                eq(r"\sigma_n = t_in_i = \sigma_{ij}n_in_j", "Normal kuchlanish.",
                   "Normal tashkil etuvchi"),
                eq(r"\tau_n = \sqrt{|\mathbf{t}|^2 - \sigma_n^2}", "Urinma kuchlanish.",
                   "Urinma tashkil etuvchi"),
            ],
            conditions=(
                "Koshi formulasi hajmiy kuchlar chekli bo'lganda o'rinli. "
                "Katta deformatsiyalarda kuchlanish qaysi holatga (boshlang'ich "
                "yoki joriy) nisbatan o'lchanishi muhim bo'lib qoladi — "
                "Koshi tenzori joriy holatga, Piola–Kirxgof tenzorlari "
                "boshlang'ich holatga nisbatan."
            ),
            worked_example=WorkedExample(
                statement=(
                    "Kuchlanish tenzori (MPa): $\\sigma_{11} = 60$, "
                    "$\\sigma_{22} = -30$, $\\sigma_{33} = 40$, "
                    "$\\sigma_{12} = 25$, $\\sigma_{13} = \\sigma_{23} = 0$. "
                    "Normali $\\mathbf{n} = (1;1;1)/\\sqrt{3}$ bo'lgan "
                    "maydonchadagi kuchlanish vektorini, normal va urinma "
                    "tashkil etuvchilarni toping."
                ),
                given=[r"\sigma = \begin{pmatrix}60&25&0\\25&-30&0\\0&0&40\end{pmatrix}\ \text{MPa}",
                       r"\mathbf{n} = \frac{1}{\sqrt3}(1;1;1)"],
                steps=[
                    st(r"n_i = 0{,}5774\ \text{har bir komponenta}",
                       "Birlik normal vektor."),
                    st(r"t_1 = \sigma_{11}n_1+\sigma_{12}n_2+\sigma_{13}n_3 = "
                       r"0{,}5774(60+25+0) = 49{,}08\ \text{MPa}",
                       "Koshi formulasi, birinchi komponenta."),
                    st(r"t_2 = 0{,}5774(25-30+0) = -2{,}89\ \text{MPa};\quad "
                       r"t_3 = 0{,}5774(0+0+40) = 23{,}09\ \text{MPa}",
                       "Qolgan komponentalar."),
                    st(r"|\mathbf{t}| = \sqrt{49{,}08^2+2{,}89^2+23{,}09^2} = "
                       r"\sqrt{2409+8{,}4+533} = 54{,}3\ \text{MPa}",
                       "To'la kuchlanish vektorining moduli."),
                    st(r"\sigma_n = \mathbf{t}\cdot\mathbf{n} = 0{,}5774(49{,}08-2{,}89+23{,}09) = "
                       r"0{,}5774\cdot69{,}28 = 40{,}0\ \text{MPa}",
                       "Normal tashkil etuvchi. Tekshirish: "
                       "$\\sigma_n = (\\sigma_{11}+\\sigma_{22}+\\sigma_{33}+2\\sigma_{12})/3 = "
                       "(60-30+40+50)/3 = 40$ ✓"),
                    st(r"\tau_n = \sqrt{54{,}3^2 - 40{,}0^2} = \sqrt{2949-1600} = "
                       r"\sqrt{1349} = 36{,}7\ \text{MPa}",
                       "Urinma tashkil etuvchi."),
                ],
                answer=(
                    "$\\mathbf{t} = (49{,}08; -2{,}89; 23{,}09)$ MPa; "
                    "$|\\mathbf{t}| = 54{,}3$ MPa; $\\sigma_n = 40{,}0$ MPa; "
                    "$\\tau_n = 36{,}7$ MPa."
                ),
                engineering_note=(
                    "Kuchlanish vektori normalga parallel emas — demak bu "
                    "maydoncha asosiy emas. Asosiy maydonchalarda "
                    "$\\mathbf{t} \\parallel \\mathbf{n}$ va $\\tau_n = 0$ "
                    "(tmm-08). Oktaedrik maydoncha ($\\mathbf{n} = (1,1,1)/\\sqrt3$) "
                    "alohida ahamiyatga ega: undagi urinma kuchlanish fon "
                    "Mizes kriteriysi bilan bevosita bog'liq."
                ),
            ),
            computation=Computation(
                caption=(
                    "Koshi formulasi: turli yo'nalishdagi maydonchalarda "
                    "kuchlanish vektorini hisoblang."
                ),
                code='''"""Koshi teoremasi: kuchlanish vektori va uning tashkil etuvchilari."""
import numpy as np
from labkit import PARAMS, note, series, table, value

s11 = float(PARAMS.get("s11", 60.0))
s22 = float(PARAMS.get("s22", -30.0))
s33 = float(PARAMS.get("s33", 40.0))
s12 = float(PARAMS.get("s12", 25.0))
s13 = float(PARAMS.get("s13", 0.0))
s23 = float(PARAMS.get("s23", 0.0))

T = np.array([[s11, s12, s13], [s12, s22, s23], [s13, s23, s33]])

def cauchy(n):
    """Koshi formulasi: t_i = sigma_ij n_j."""
    n = np.asarray(n, dtype=float)
    n = n/np.linalg.norm(n)
    t = T @ n
    sn = float(t @ n)
    tn = float(np.sqrt(max(t @ t - sn**2, 0.0)))
    return t, sn, tn

# Oktaedrik maydoncha
n_oct = np.array([1.0, 1.0, 1.0])
t_oct, sn_oct, tn_oct = cauchy(n_oct)
value("t₁", float(t_oct[0]), "MPa")
value("t₂", float(t_oct[1]), "MPa")
value("t₃", float(t_oct[2]), "MPa")
value("|t|", float(np.linalg.norm(t_oct)), "MPa")
value("σ_n (normal)", sn_oct, "MPa")
value("τ_n (urinma)", tn_oct, "MPa")
note(f"σ_n = I₁/3 = {np.trace(T)/3:.4f} MPa — oktaedrik maydonchada normal "
     "kuchlanish o'rtacha kuchlanishga teng ✓")

# Koordinata maydonchalari
rows = []
for i, nm in enumerate(["x", "y", "z"]):
    n = np.zeros(3); n[i] = 1.0
    t, sn, tn = cauchy(n)
    rows.append([f"n = {nm}", float(t[0]), float(t[1]), float(t[2]), float(sn), float(tn)])
# Asosiy maydonchalar
eigvals, eigvecs = np.linalg.eigh(T)
for i in range(3):
    t, sn, tn = cauchy(eigvecs[:, i])
    rows.append([f"Asosiy {i+1}", float(t[0]), float(t[1]), float(t[2]), float(sn), float(tn)])
rows.append(["Oktaedrik", float(t_oct[0]), float(t_oct[1]), float(t_oct[2]),
             float(sn_oct), float(tn_oct)])
table("Turli maydonchalarda kuchlanish",
      ["Maydoncha", "t₁", "t₂", "t₃", "σ_n", "τ_n"], rows)
note("Asosiy maydonchalarda τ_n ≈ 0 — bu ularning ta'rifi ✓")

# Burchakka bog'liqlik (xy tekisligida aylantirish)
angles = np.linspace(0, 180, 181)
sn_arr, tn_arr = [], []
for a in angles:
    t_rad = np.radians(a)
    n = np.array([np.cos(t_rad), np.sin(t_rad), 0.0])
    _, sn, tn = cauchy(n)
    sn_arr.append(sn); tn_arr.append(tn)
series("σ_n(α)", angles.tolist(), sn_arr, xlabel="Maydoncha burchagi, deg", ylabel="σ_n, MPa")
series("τ_n(α)", angles.tolist(), tn_arr, xlabel="Maydoncha burchagi, deg", ylabel="τ_n, MPa")
note(f"σ_n maksimumi α = {angles[int(np.argmax(sn_arr))]:.0f}° da, "
     f"τ_n maksimumi α = {angles[int(np.argmax(tn_arr))]:.0f}° da — farq 45° ✓")

# Oktaedrik urinma kuchlanish va fon Mizes
p1, p2, p3 = np.sort(eigvals)[::-1]
tau_oct = np.sqrt((p1-p2)**2 + (p2-p3)**2 + (p3-p1)**2)/3
s_mises = np.sqrt(0.5*((p1-p2)**2 + (p2-p3)**2 + (p3-p1)**2))
value("Oktaedrik τ (formula)", float(tau_oct), "MPa")
value("τ_n oktaedrik (Koshi)", tn_oct, "MPa")
value("fon Mizes σ_ekv", float(s_mises), "MPa")
note(f"σ_ekv = (3/√2)·τ_oct = {3/np.sqrt(2)*tau_oct:.3f} MPa — "
     "fon Mizes kriteriysi oktaedrik urinma kuchlanish bilan bevosita bog'liq.")

table("Koshi formulasining qo'llanilishi",
      ["Masala", "Berilgan", "Topiladi"],
      [["Kesimdagi kuchlanish", "σ_ij, n", "t, σ_n, τ_n"],
       ["Asosiy kuchlanishlar", "σ_ij", "n (τ_n = 0 sharti)"],
       ["Chegaraviy shart", "t (yuklanish)", "σ_ij chegarada"],
       ["Buzilish tekisligi", "σ_ij", "τ_n maksimal bo'lgan n"]])
''',
                parameters=[
                    p("s11", "σ₁₁", -300.0, 300.0, 60.0, 5.0, "MPa"),
                    p("s22", "σ₂₂", -300.0, 300.0, -30.0, 5.0, "MPa"),
                    p("s33", "σ₃₃", -300.0, 300.0, 40.0, 5.0, "MPa"),
                    p("s12", "σ₁₂", -200.0, 200.0, 25.0, 5.0, "MPa"),
                    p("s13", "σ₁₃", -200.0, 200.0, 0.0, 5.0, "MPa"),
                    p("s23", "σ₂₃", -200.0, 200.0, 0.0, 5.0, "MPa"),
                ],
                expected_output="t = (49,08; -2,89; 23,09) MPa, σ_n = 40,0 MPa, τ_n = 36,7 MPa",
            ),
            visualization=vis(
                "Koshi tetraedri",
                "Manim",
                "Tetraedr: uchta koordinata yuzasida $\\mathbf{t}^{(1)}$, "
                "$\\mathbf{t}^{(2)}$, $\\mathbf{t}^{(3)}$ vektorlari, qiya "
                "yuzada $\\mathbf{t}^{(n)}$; tetraedr kichrayganda hajmiy "
                "kuch yo'qolishi ko'rsatiladi.",
                "Manim: tetraedrning kichrayishi va hajmiy kuchning "
                "yo'qolishi — Koshi isbotining markaziy g'oyasi, uni "
                "animatsiyada ko'rsatish eng samarali. React/SVG da "
                "$\\sigma_n(\\alpha)$, $\\tau_n(\\alpha)$ grafiklari beriladi.",
            ),
            interpretation=(
                "Jadvalda asosiy maydonchalarda $\\tau_n \\approx 0$ — bu "
                "ularning ta'rifining sonli tasdig'i. Oktaedrik maydonchadagi "
                "normal kuchlanish esa aynan o'rtacha kuchlanishga teng va "
                "urinma kuchlanish fon Mizes kriteriysi bilan bevosita "
                "bog'liq: $\\sigma_{ekv} = \\frac{3}{\\sqrt2}\\tau_{okt}$. "
                "Bu — mq-21 dagi kriteriyning geometrik talqini."
            ),
            common_mistakes=[
                "Normal vektorni normallashtirishni unutish.",
                "Kuchlanish vektorini normal kuchlanish bilan chalkashtirish "
                "— $\\mathbf{t}$ umuman normalga parallel emas.",
                "$\\sigma_{ij}$ indekslarining ma'nosini almashtirish "
                "(birinchi — yo'nalish, ikkinchi — maydoncha normali).",
                "Koshi formulasini simmetriyasiz tenzorga qo'llash — u "
                "o'rinli, lekin simmetriya alohida isbotlanadi (tmm-11).",
            ],
            quiz=[
                q("Koshi isbotida hajmiy kuch nima uchun yo'qoladi?",
                  "Hajm $h^3$ tartibida, yuza $h^2$ tartibida kamayadi; "
                  "$h\\to0$ da ularning nisbati nolga intiladi.", "konseptual"),
                q("Nima uchun kuchlanish tenzor?",
                  "Koshi formulasi $t_i = \\sigma_{ij}n_j$ chiziqli "
                  "akslantirish — bu ikkinchi tartibli tenzorning ta'rifi.",
                  "konseptual"),
                q("$\\sigma = \\text{diag}(100, 0, 0)$, $\\mathbf{n} = (1,1,0)/\\sqrt2$. "
                  "$\\sigma_n$?",
                  "$\\sigma_n = \\sigma_{11}n_1^2 = 100\\cdot0{,}5 = 50$ MPa.",
                  "hisob"),
                q("Asosiy maydonchada $\\mathbf{t}$ va $\\mathbf{n}$ qanday "
                  "bog'langan?",
                  "$\\mathbf{t} = \\sigma\\mathbf{n}$ — ular parallel; bu "
                  "xususiy qiymatlar masalasining ta'rifi.", "talqin"),
                q("Kodda oktaedrik maydonchada $\\sigma_n = I_1/3$ nima uchun?",
                  "$\\sigma_n = \\sigma_{ij}n_in_j$; $n_i = 1/\\sqrt3$ bo'lsa "
                  "bu $\\frac{1}{3}\\sigma_{ii}$ ga aylanadi (simmetrik "
                  "tenzor uchun).", "kod"),
            ],
            bridge_to_next=(
                "Kuchlanish tenzori kiritildi. Endi uning asosiy "
                "qiymatlarini va invariantlarini batafsil o'rganamiz."
            ),
            research_extension=(
                "Piola–Kirxgof kuchlanish tenzorlarini o'rganing: katta "
                "deformatsiyalarda kuchlanish qaysi yuzaga nisbatan "
                "o'lchanadi? 1-chi va 2-chi P–K tenzorlarini Koshi tenzori "
                "bilan bog'lang va bir o'qli katta cho'zilishda ularning "
                "farqini sonli ko'rsating."
            ),
            manim=manim(
                scene="CauchyTetrahedronScene",
                module="animatsiya/scenes/tmm_stress.py",
                title="Koshi tetraedri",
                summary="Tetraedr kichrayadi, hajmiy kuch yo'qoladi va "
                        "t = σ·n formulasi kelib chiqadi.",
            ),
        ),
    ),
    Topic(
        id="tmm-08",
        subject_id=S,
        module_id=M,
        order=8,
        title="Asosiy kuchlanishlar, invariantlar va deviator ajralishi",
        description=(
            "Kuchlanish tenzorining xususiy qiymatlari, invariantlar, "
            "sferik va deviator qismlar, oktaedrik kuchlanishlar."
        ),
        learning_objective=(
            "Fazoviy kuchlanish holatida asosiy kuchlanishlarni topish va "
            "deviator invariantlarini hisoblash."
        ),
        prerequisites=["tmm-07"],
        mathematical_core=(
            "Xarakteristik tenglama $\\lambda^3 - I_1\\lambda^2 + I_2\\lambda - I_3 = 0$, "
            "deviator invariantlari $J_2$, $J_3$."
        ),
        engineering_application=(
            "Mustahkamlik kriteriylari, plastiklik nazariyasi, FEM "
            "postprotsessing (fon Mizes kuchlanishi)."
        ),
        computational_component=(
            "Xarakteristik tenglamani yechish, deviator invariantlarini "
            "hisoblash, Haigh–Westergaard fazosida tasvirlash."
        ),
        visualization_component=(
            "Asosiy kuchlanishlar fazosi, gidrostatik o'q va deviator "
            "tekisligi."
        ),
        research_extension=(
            "Lode burchagi: uchinchi invariant nima uchun ba'zi "
            "materiallarda muhim?"
        ),
        difficulty="murakkab",
        previous_link=(
            "tmm-07 da asosiy maydonchalarda $\\tau_n = 0$ ekanini ko'rdik. "
            "Endi ularni topish masalasini rasmiy qo'yamiz."
        ),
        next_topic="tmm-09",
        estimated_minutes=85,
        tags=["asosiy kuchlanishlar", "invariantlar", "deviator"],
        lesson=Lesson(
            physical_problem=(
                "FEM hisobi natijasida har bir tugunda 6 ta kuchlanish "
                "komponentasi olinadi. Lekin konstruktorga bitta son kerak: "
                "bu nuqta xavflimi? Javob invariantlarda: ular koordinata "
                "sistemasidan bog'liq emas va material xatti-harakatini "
                "bevosita belgilaydi."
            ),
            concepts=[
                c("Asosiy kuchlanishlar", "Kuchlanish tenzorining xususiy "
                  "qiymatlari $\\sigma_1 \\ge \\sigma_2 \\ge \\sigma_3$."),
                c("Asosiy invariantlar", "$I_1 = \\sigma_{kk}$, $I_2$, "
                  "$I_3 = \\det\\sigma$ — xarakteristik tenglama "
                  "koeffitsientlari."),
                c("Sferik va deviator ajralishi", "$\\sigma_{ij} = "
                  "\\sigma_m\\delta_{ij} + s_{ij}$; $\\sigma_m = I_1/3$."),
                c("Deviator invariantlari", "$J_2 = \\frac{1}{2}s_{ij}s_{ij}$, "
                  "$J_3 = \\det s$; $J_1 = 0$ har doim."),
                c("Oktaedrik kuchlanishlar", "$\\sigma_{okt} = \\sigma_m$, "
                  "$\\tau_{okt} = \\sqrt{2J_2/3}$ — plastiklik nazariyasining "
                  "asosiy kattaliklari."),
            ],
            derivation=[
                d("1-qadam. Xususiy qiymatlar masalasi",
                  r"\sigma_{ij}n_j = \lambda n_i \;\Rightarrow\; "
                  r"(\sigma_{ij}-\lambda\delta_{ij})n_j = 0",
                  "Asosiy maydoncha sharti: $\\mathbf{t} \\parallel \\mathbf{n}$. "
                  "Notrivial yechim uchun determinant nolga teng bo'lishi kerak."),
                d("2-qadam. Xarakteristik tenglama",
                  r"\lambda^3 - I_1\lambda^2 + I_2\lambda - I_3 = 0",
                  "Kubik tenglama. Simmetrik tenzor uchun uchala ildiz "
                  "haqiqiy va mos xususiy vektorlar ortogonal."),
                d("3-qadam. Deviator ajralishi",
                  r"s_{ij} = \sigma_{ij} - \tfrac{1}{3}\sigma_{kk}\delta_{ij},\qquad s_{kk} = 0",
                  "Sferik qism hajm o'zgarishiga, deviator shakl "
                  "o'zgarishiga javob beradi (mq-20)."),
                d("4-qadam. Ikkinchi deviator invarianti",
                  r"J_2 = \tfrac{1}{2}s_{ij}s_{ij} = \tfrac{1}{6}\big[(\sigma_1-\sigma_2)^2+"
                  r"(\sigma_2-\sigma_3)^2+(\sigma_3-\sigma_1)^2\big]",
                  "Bu — fon Mizes kriteriysining asosi: "
                  "$\\sigma_{ekv} = \\sqrt{3J_2}$."),
                d("5-qadam. Haigh–Westergaard koordinatalari",
                  r"\xi = \frac{I_1}{\sqrt3},\quad \rho = \sqrt{2J_2},\quad "
                  r"\cos3\theta = \frac{3\sqrt3}{2}\frac{J_3}{J_2^{3/2}}",
                  "Asosiy kuchlanishlar fazosida silindrik koordinatalar: "
                  "$\\xi$ — gidrostatik o'q bo'ylab, $\\rho$ — deviator "
                  "radiusi, $\\theta$ — Lode burchagi."),
            ],
            formula_meaning=(
                "Invariantlar kuchlanish holatining 'genetik kodi': "
                "$I_1$ hajm o'zgarishini, $J_2$ shakl o'zgarishini, $J_3$ "
                "esa deformatsiya turini (cho'zilish yoki siqilish ustunligi) "
                "tavsiflaydi. Metallarda oqish faqat $J_2$ ga bog'liq "
                "(fon Mizes), tuproq va betonda esa $I_1$ ham muhim "
                "(Mor–Kulon), kompozitlarda $J_3$ ham hisobga olinadi."
            ),
            equations=[
                eq(r"\lambda^3 - I_1\lambda^2+I_2\lambda-I_3 = 0", "Xarakteristik tenglama.",
                   "Xarakteristik tenglama"),
                eq(r"J_2 = \tfrac{1}{6}\sum(\sigma_i-\sigma_j)^2", "Ikkinchi deviator invarianti.",
                   "J₂"),
                eq(r"\sigma_{ekv}^{Mises} = \sqrt{3J_2}", "Fon Mizes ekvivalent kuchlanishi.",
                   "fon Mizes"),
                eq(r"\tau_{okt} = \sqrt{\tfrac{2}{3}J_2}", "Oktaedrik urinma kuchlanish.",
                   "Oktaedrik τ"),
            ],
            conditions=(
                "Simmetrik tenzor uchun uchala xususiy qiymat haqiqiy. "
                "Karrali qiymatlar bo'lsa (masalan, o'q simmetrik holat) "
                "xususiy vektorlar yagona emas, lekin ortogonal bazis "
                "tanlash mumkin. Gidrostatik holatda ($\\sigma_1 = \\sigma_2 = "
                "\\sigma_3$) deviator nolga teng va istalgan yo'nalish asosiy."
            ),
            worked_example=WorkedExample(
                statement=(
                    "Kuchlanish holati (MPa): $\\sigma_{11} = 120$, "
                    "$\\sigma_{22} = 60$, $\\sigma_{33} = -40$, "
                    "$\\sigma_{12} = 40$, $\\sigma_{13} = \\sigma_{23} = 0$. "
                    "Invariantlarni, asosiy kuchlanishlarni, deviatorni va "
                    "fon Mizes kuchlanishini toping."
                ),
                given=[r"\sigma = \begin{pmatrix}120&40&0\\40&60&0\\0&0&-40\end{pmatrix}"],
                steps=[
                    st(r"I_1 = 120+60-40 = 140\ \text{MPa}",
                       "Birinchi invariant."),
                    st(r"I_2 = (120)(60)+(60)(-40)+(-40)(120) - 40^2 = "
                       r"7200-2400-4800-1600 = -1600\ \text{MPa}^2",
                       "Ikkinchi invariant."),
                    st(r"I_3 = -40[(120)(60)-1600] = -40(5600) = -224\,000\ \text{MPa}^3",
                       "Determinant."),
                    st(r"\sigma_{1,2} = \frac{120+60}{2}\pm\sqrt{30^2+40^2} = 90\pm50 "
                       r"\Rightarrow \sigma_1 = 140,\; \sigma_2 = 40,\; \sigma_3 = -40",
                       "$z$ asosiy o'q bo'lgani uchun tekis masalaga keladi. "
                       "Tekshirish: $140+40-40 = 140 = I_1$ ✓"),
                    st(r"\sigma_m = \frac{140}{3} = 46{,}67;\quad "
                       r"s_1 = 93{,}33,\ s_2 = -6{,}67,\ s_3 = -86{,}67\ \text{MPa}",
                       "Deviator komponentalari. Tekshirish: "
                       "$93{,}33-6{,}67-86{,}67 \\approx 0$ ✓"),
                    st(r"J_2 = \tfrac{1}{6}[(140-40)^2+(40+40)^2+(-40-140)^2] = "
                       r"\tfrac{1}{6}[10\,000+6400+32\,400] = 8133\ \text{MPa}^2",
                       "$\\sigma_{Mises} = \\sqrt{3\\cdot8133} = 156{,}2$ MPa; "
                       "$\\tau_{okt} = \\sqrt{2\\cdot8133/3} = 73{,}6$ MPa."),
                ],
                answer=(
                    "$I_1 = 140$ MPa; $\\sigma_{1,2,3} = 140;\\ 40;\\ -40$ MPa; "
                    "$\\sigma_m = 46{,}67$ MPa; $J_2 = 8133$ MPa²; "
                    "$\\sigma_{Mises} = 156{,}2$ MPa."
                ),
                engineering_note=(
                    "Fon Mizes kuchlanishi 156,2 MPa — bu eng katta asosiy "
                    "kuchlanishdan (140 MPa) katta! Sabab: $\\sigma_3 = -40$ "
                    "MPa siqilish kuchlanishi farqni oshiradi. Bu — "
                    "murakkab kuchlanish holatining xavfliligini ko'rsatadi "
                    "va faqat $\\sigma_1$ ga qarab baholash xato ekanini "
                    "isbotlaydi."
                ),
            ),
            computation=Computation(
                caption=(
                    "Asosiy kuchlanishlar va invariantlar: kuchlanish "
                    "holatini o'zgartirib, deviator tahlilini bajaring."
                ),
                code='''"""Asosiy kuchlanishlar, invariantlar va deviator ajralishi."""
import numpy as np
from labkit import PARAMS, note, series, table, value

s11 = float(PARAMS.get("s11", 120.0))
s22 = float(PARAMS.get("s22", 60.0))
s33 = float(PARAMS.get("s33", -40.0))
s12 = float(PARAMS.get("s12", 40.0))
s13 = float(PARAMS.get("s13", 0.0))
s23 = float(PARAMS.get("s23", 0.0))

T = np.array([[s11, s12, s13], [s12, s22, s23], [s13, s23, s33]])

I1 = np.trace(T)
I2 = 0.5*(I1**2 - np.trace(T @ T))
I3 = np.linalg.det(T)
value("I₁", float(I1), "MPa")
value("I₂", float(I2), "MPa²")
value("I₃", float(I3), "MPa³")

# Xarakteristik tenglamani yechish
roots = np.roots([1.0, -I1, I2, -I3])
principals = np.sort(np.real(roots))[::-1]
eigvals, eigvecs = np.linalg.eigh(T)
for i, s in enumerate(principals):
    value(f"σ_{i+1}", float(s), "MPa")
note(f"np.roots va eigh farqi: {np.max(np.abs(np.sort(principals)-np.sort(eigvals))):.2e} MPa ✓")

table("Asosiy yo'nalishlar",
      ["Mod", "σ, MPa", "n₁", "n₂", "n₃"],
      [[i+1, float(np.sort(eigvals)[::-1][i]),
        float(eigvecs[0, np.argsort(eigvals)[::-1][i]]),
        float(eigvecs[1, np.argsort(eigvals)[::-1][i]]),
        float(eigvecs[2, np.argsort(eigvals)[::-1][i]])] for i in range(3)])

# Deviator
s_m = I1/3
S = T - s_m*np.eye(3)
J2 = 0.5*np.sum(S*S)
J3 = np.linalg.det(S)
value("σ_m (o'rtacha)", float(s_m), "MPa")
value("Deviator izi (0 bo'lishi kerak)", float(np.trace(S)), "MPa")
value("J₂", float(J2), "MPa²")
value("J₃", float(J3), "MPa³")
value("fon Mizes σ_ekv", float(np.sqrt(3*J2)), "MPa")
value("τ_oktaedrik", float(np.sqrt(2*J2/3)), "MPa")
value("τ_max (Tresk)", float((principals[0]-principals[2])/2), "MPa")
value("Tresk σ_ekv", float(principals[0]-principals[2]), "MPa")

# Haigh-Westergaard koordinatalari
xi = I1/np.sqrt(3)
rho = np.sqrt(2*J2)
cos3theta = np.clip(3*np.sqrt(3)/2*J3/max(J2**1.5, 1e-12), -1, 1)
theta_lode = np.degrees(np.arccos(cos3theta)/3)
value("ξ (gidrostatik o'q)", float(xi), "MPa")
value("ρ (deviator radiusi)", float(rho), "MPa")
value("Lode burchagi θ", float(theta_lode), "deg")
note("θ = 0°: bir o'qli cho'zilish tipi; θ = 60°: bir o'qli siqilish tipi; "
     "θ = 30°: toza siljish tipi.")

# Gidrostatik yuklanish deviatorga ta'sir qilmaydi
p_add = 100.0
T_hydro = T + p_add*np.eye(3)
S_hydro = T_hydro - (np.trace(T_hydro)/3)*np.eye(3)
note(f"Gidrostatik {p_add} MPa qo'shilgandan keyin: "
     f"I₁ = {np.trace(T_hydro):.1f} MPa (o'zgardi), "
     f"J₂ = {0.5*np.sum(S_hydro*S_hydro):.3f} MPa² (o'zgarmadi) ✓")
note("Shuning uchun metallarda gidrostatik bosim oqishga olib kelmaydi.")

# Kriteriylarni taqqoslash
table("Mustahkamlik kriteriylari (invariantlar orqali)",
      ["Kriteriy", "Formula", "Qiymat, MPa", "Bog'liqligi"],
      [["Maksimal normal", "σ₁", float(principals[0]), "I₁, I₂, I₃"],
       ["Tresk", "σ₁-σ₃", float(principals[0]-principals[2]), "J₂, J₃"],
       ["fon Mizes", "√(3J₂)", float(np.sqrt(3*J2)), "faqat J₂"],
       ["Mor–Kulon", "σ₁/[σ_c]-σ₃/[σ_s]", "—", "I₁ va J₂"]])

# Kuchlanish holatining o'zgarishi
scale = np.linspace(0, 2, 100)
series("fon Mizes (masshtablash)", scale.tolist(),
       (np.sqrt(3*J2)*scale).tolist(), xlabel="Yuklanish koeffitsienti", ylabel="σ_ekv, MPa")
series("I₁ (masshtablash)", scale.tolist(), (I1*scale).tolist(),
       xlabel="Yuklanish koeffitsienti", ylabel="I₁, MPa")
''',
                parameters=[
                    p("s11", "σ₁₁", -400.0, 400.0, 120.0, 10.0, "MPa"),
                    p("s22", "σ₂₂", -400.0, 400.0, 60.0, 10.0, "MPa"),
                    p("s33", "σ₃₃", -400.0, 400.0, -40.0, 10.0, "MPa"),
                    p("s12", "σ₁₂", -300.0, 300.0, 40.0, 10.0, "MPa"),
                    p("s13", "σ₁₃", -300.0, 300.0, 0.0, 10.0, "MPa"),
                    p("s23", "σ₂₃", -300.0, 300.0, 0.0, 10.0, "MPa"),
                ],
                expected_output="I₁ = 140 MPa, σ₁ = 140, σ₃ = -40 MPa, σ_Mises = 156,2 MPa",
            ),
            visualization=vis(
                "Asosiy kuchlanishlar fazosi",
                "React/SVG",
                "$(\\sigma_1, \\sigma_2)$ tekisligida buzilish chegaralari "
                "(fon Mizes ellipsi, Tresk olti burchagi) va joriy holat "
                "nuqtasi; alohida panelda gidrostatik o'q va deviator "
                "tekisligi sxemasi.",
                "React/SVG: mq-21 dagi diagrammani kengaytiring — endi "
                "invariantlar orqali. Gidrostatik o'q bo'ylab siljish "
                "deviatorni o'zgartirmasligini ko'rsatish — bu mavzuning "
                "asosiy g'oyasi.",
            ),
            interpretation=(
                "Gidrostatik qo'shimcha testi hal qiluvchi natija beradi: "
                "$I_1$ o'zgaradi, $J_2$ esa aynan o'zgarmaydi. Bu metallarda "
                "gidrostatik bosim plastik oqishga olib kelmasligining "
                "matematik ifodasi. Lode burchagi esa kuchlanish holatining "
                "'turini' aniqlaydi — bu ba'zi materiallar (beton, tuproq) "
                "uchun muhim, chunki ularda buzilish $J_3$ ga ham bog'liq."
            ),
            common_mistakes=[
                "$J_1 = 0$ ekanini unutish (deviator izi har doim nol).",
                "Fon Mizes kuchlanishini $\\sigma_1$ bilan taqqoslash — u "
                "kattaroq bo'lishi mumkin.",
                "Xarakteristik tenglama ildizlarini tartiblashni unutish.",
                "Karrali xususiy qiymatlarda xususiy vektorlar yagona deb "
                "hisoblash.",
            ],
            quiz=[
                q("Nima uchun metallarda gidrostatik bosim oqishga olib "
                  "kelmaydi?",
                  "Fon Mizes kriteriysi faqat $J_2$ ga bog'liq, gidrostatik "
                  "qo'shimcha esa deviatorni o'zgartirmaydi.", "konseptual"),
                q("$J_1$ nimaga teng va nega?",
                  "Nolga: deviator ta'rifi bo'yicha uning izi ayiriladi.",
                  "konseptual"),
                q("$\\sigma_{1,2,3} = (100, 0, -100)$ MPa. $\\sigma_{Mises}$?",
                  "$J_2 = \\frac{1}{6}[100^2+100^2+200^2] = 10\\,000$; "
                  "$\\sigma_{Mises} = \\sqrt{30\\,000} = 173{,}2$ MPa.", "hisob"),
                q("Lode burchagi nimani tavsiflaydi?",
                  "Kuchlanish holatining turini: cho'zilish, siqilish yoki "
                  "toza siljish tipi. Ba'zi materiallarda buzilish unga ham "
                  "bog'liq.", "talqin"),
                q("Kodda `np.roots` va `np.linalg.eigh` natijalari nima uchun "
                  "mos keladi?",
                  "Ikkalasi ham bir xil xususiy qiymatlarni topadi: birinchisi "
                  "xarakteristik tenglama ildizlari orqali, ikkinchisi to'g'ridan-"
                  "to'g'ri matritsa algoritmi bilan.", "kod"),
            ],
            bridge_to_next=(
                "Kuchlanish holatini to'liq tahlil qildik. Endi balans "
                "qonunlariga o'tamiz — massa saqlanishidan boshlab."
            ),
            research_extension=(
                "Drucker–Prager kriteriysini amalga oshiring: "
                "$\\sqrt{J_2} + \\alpha I_1 = k$. Bu kriteriy beton va "
                "tuproq uchun mo'ljallangan. $\\alpha$ parametrining "
                "buzilish sirtiga ta'sirini Haigh–Westergaard fazosida "
                "ko'rsating va fon Mizes ($\\alpha = 0$) bilan taqqoslang."
            ),
        ),
    ),
    Topic(
        id="tmm-09",
        subject_id=S,
        module_id=M,
        order=9,
        title="Massa saqlanishi va uzluksizlik tenglamasi",
        description=(
            "Massa balansi, uzluksizlik tenglamasining differensial va "
            "integral shakllari, siqilmaydigan muhit sharti."
        ),
        learning_objective=(
            "Uzluksizlik tenglamasini keltirib chiqarish va uni oqim "
            "masalalarida qo'llash."
        ),
        prerequisites=["tmm-06", "tmm-03"],
        mathematical_core=(
            "Reynolds transport teoremasi, divergensiya teoremasi, "
            "$\\partial\\rho/\\partial t + \\nabla\\cdot(\\rho\\mathbf{v}) = 0$."
        ),
        engineering_application=(
            "Quvur oqimi, nasos va kompressor hisobi, aerodinamika, "
            "CFD dasturlarining asosiy tenglamasi."
        ),
        computational_component=(
            "Uzluksizlik tenglamasini sonli tekshirish va oqim sarfini "
            "hisoblash."
        ),
        visualization_component=(
            "Oqim naychasi va sarf saqlanishi; torayuvchi quvurda tezlik "
            "o'zgarishi."
        ),
        research_extension=(
            "Siqiluvchan oqimda (Max soni > 0,3) uzluksizlik tenglamasi "
            "qanday o'zgaradi?"
        ),
        difficulty="asosiy",
        previous_link=(
            "tmm-03 dagi moddiy hosila va tmm-06 dagi tezlik maydoni "
            "endi birinchi balans qonunini yozish uchun ishlatiladi."
        ),
        next_topic="tmm-10",
        estimated_minutes=80,
        tags=["uzluksizlik tenglamasi", "massa saqlanishi", "sarf"],
        lesson=Lesson(
            physical_problem=(
                "Quvur diametri ikki marta kamaysa, suv tezligi qancha "
                "oshadi? Bu savol nasos, quvur o'tkazgich va aerodinamik "
                "kanallar loyihalashda doimiy uchraydi. Javob massa "
                "saqlanishidan kelib chiqadi — kontinuum mexanikasining "
                "birinchi balans qonunidan."
            ),
            concepts=[
                c("Nazorat hajmi", "Fazoda qo'zg'almas hajm; u orqali "
                  "modda oqib o'tadi (Eyler yondashuvi)."),
                c("Moddiy hajm", "Doimo bir xil moddiy zarralardan iborat "
                  "hajm (Lagranj yondashuvi); uning massasi o'zgarmaydi."),
                c("Reynolds transport teoremasi", "Moddiy hajm bo'yicha "
                  "integralning hosilasini nazorat hajmi orqali ifodalash."),
                c("Uzluksizlik tenglamasi", "$\\partial\\rho/\\partial t + "
                  "\\nabla\\cdot(\\rho\\mathbf{v}) = 0$ — massa balansining "
                  "differensial shakli."),
                c("Siqilmaydigan muhit", "$\\rho = \\text{const}$ → "
                  "$\\nabla\\cdot\\mathbf{v} = 0$ — hajm saqlanadi."),
            ],
            derivation=[
                d("1-qadam. Massa saqlanishi moddiy hajm uchun",
                  r"\frac{D}{Dt}\int_{V(t)}\rho\,dV = 0",
                  "Moddiy hajm doimo bir xil zarralardan iborat, demak "
                  "uning massasi o'zgarmaydi."),
                d("2-qadam. Reynolds transport teoremasi",
                  r"\frac{D}{Dt}\int_{V(t)}f\,dV = \int_{V}\frac{\partial f}{\partial t}dV + "
                  r"\oint_{S}f\,\mathbf{v}\cdot d\mathbf{S}",
                  "Moddiy hajm bo'yicha hosila = lokal o'zgarish + chegara "
                  "orqali oqim. Bu — moddiy hosilaning integral analogi."),
                d("3-qadam. Divergensiya teoremasini qo'llash",
                  r"\oint_S\rho\mathbf{v}\cdot d\mathbf{S} = \int_V\nabla\cdot(\rho\mathbf{v})\,dV "
                  r"\;\Rightarrow\; \int_V\left[\frac{\partial\rho}{\partial t}+\nabla\cdot(\rho\mathbf{v})\right]dV = 0",
                  "Sirt integralini hajm integraliga aylantiramiz."),
                d("4-qadam. Differensial shakl",
                  r"\boxed{\;\frac{\partial\rho}{\partial t} + \nabla\cdot(\rho\mathbf{v}) = 0\;}",
                  "Integral ixtiyoriy hajm uchun nolga teng bo'lgani uchun "
                  "integral osti ifodasi nolga teng."),
                d("5-qadam. Siqilmaydigan muhit va sarf",
                  r"\rho = \text{const} \Rightarrow \nabla\cdot\mathbf{v} = 0;\qquad "
                  r"Q = v_1A_1 = v_2A_2",
                  "Quvur uchun integral shakl — muhandislikda eng ko'p "
                  "ishlatiladigan natija."),
            ],
            formula_meaning=(
                "Uzluksizlik tenglamasi — eng oddiy va eng universal balans "
                "qonuni: modda yo'qolmaydi va paydo bo'lmaydi. "
                "$\\nabla\\cdot\\mathbf{v} = 0$ sharti siqilmaydigan "
                "oqimda tezlik maydoniga kuchli cheklov qo'yadi va aynan u "
                "bosimni 'noma'lum Lagranj ko'paytuvchisi' ga aylantiradi "
                "(tmm-27). Quvurdagi $v_1A_1 = v_2A_2$ esa gidravlikaning "
                "asosiy formulasidir."
            ),
            equations=[
                eq(r"\frac{\partial\rho}{\partial t}+\nabla\cdot(\rho\mathbf{v}) = 0",
                   "Uzluksizlik tenglamasi (differensial shakl).", "Uzluksizlik"),
                eq(r"\frac{D\rho}{Dt} + \rho\,\nabla\cdot\mathbf{v} = 0",
                   "Moddiy hosila orqali shakl.", "Moddiy shakl"),
                eq(r"\nabla\cdot\mathbf{v} = 0", "Siqilmaydigan muhit sharti.",
                   "Siqilmaslik"),
                eq(r"Q = v_1A_1 = v_2A_2", "Sarf saqlanishi (quvur).", "Sarf tenglamasi"),
            ],
            conditions=(
                "Siqilmaydigan faraz suyuqliklar uchun deyarli har doim, "
                "gazlar uchun esa $Ma < 0{,}3$ da o'rinli (zichlik "
                "o'zgarishi 5 % dan kam). Yuqori tezliklarda siqiluvchanlik "
                "hisobga olinishi kerak va energiya tenglamasi bilan "
                "birgalikda yechiladi."
            ),
            worked_example=WorkedExample(
                statement=(
                    "Quvur $d_1 = 100$ mm dan $d_2 = 60$ mm ga toraygan. "
                    "Kirish tezligi $v_1 = 2$ m/s, suv "
                    "($\\rho = 1000$ kg/m³). (a) Chiqish tezligi va massa "
                    "sarfi; (b) tezlanish; (c) havo oqimi uchun ($v_1 = 80$ "
                    "m/s) siqiluvchanlikni baholang."
                ),
                given=[r"d_1 = 0{,}1\ \text{m},\; d_2 = 0{,}06\ \text{m},\; v_1 = 2\ \text{m/s}"],
                steps=[
                    st(r"A_1 = \frac{\pi\cdot0{,}01}{4} = 7{,}854\cdot10^{-3}\ \text{m}^2;\quad "
                       r"A_2 = \frac{\pi\cdot0{,}0036}{4} = 2{,}827\cdot10^{-3}\ \text{m}^2",
                       "Kesim yuzalari."),
                    st(r"v_2 = v_1\frac{A_1}{A_2} = 2\cdot\frac{7{,}854}{2{,}827} = 5{,}56\ \text{m/s}",
                       "Sarf saqlanishidan. Tezlik $(d_1/d_2)^2 = 2{,}78$ "
                       "marta oshdi."),
                    st(r"Q = v_1A_1 = 2\cdot7{,}854\cdot10^{-3} = 0{,}0157\ \text{m}^3/\text{s} = 15{,}7\ \text{l/s}",
                       "Hajmiy sarf."),
                    st(r"\dot m = \rho Q = 1000\cdot0{,}0157 = 15{,}7\ \text{kg/s}",
                       "Massa sarfi."),
                    st(r"a \approx \frac{v_2^2-v_1^2}{2L} = \frac{30{,}9-4}{2\cdot0{,}3} = 44{,}8\ \text{m/s}^2 "
                       r"\ (L = 0{,}3\ \text{m torayish uzunligi})",
                       "Konvektiv tezlanish — 4,6g! Bu bosim tushishini "
                       "keltirib chiqaradi (tmm-26)."),
                    st(r"\text{Havo: } Ma = \frac{80}{340} = 0{,}235 < 0{,}3 "
                       r"\Rightarrow \text{siqilmaydigan faraz o'rinli}",
                       "Zichlik o'zgarishi $\\approx Ma^2/2 = 2{,}8$ % — "
                       "qabul qilinadi."),
                ],
                answer=(
                    "$v_2 = 5{,}56$ m/s; $Q = 15{,}7$ l/s; "
                    "$\\dot m = 15{,}7$ kg/s; $a \\approx 45$ m/s²; "
                    "havo uchun $Ma = 0{,}235$ — siqilmaydigan faraz o'rinli."
                ),
                engineering_note=(
                    "Tezlikning $(d_1/d_2)^2$ marta o'sishi — gidravlikaning "
                    "asosiy qoidasi. 45 m/s² tezlanish esa Bernulli "
                    "tenglamasi orqali bosim tushishiga aylanadi: "
                    "$\\Delta p = \\rho(v_2^2-v_1^2)/2 = 13{,}5$ kPa. Aynan "
                    "shu effekt Venturi rashodomeri va karbyuratorda "
                    "ishlatiladi."
                ),
            ),
            computation=Computation(
                caption=(
                    "Uzluksizlik tenglamasi: quvur geometriyasini o'zgartirib, "
                    "tezlik va sarf taqsimotini hisoblang."
                ),
                code='''"""Massa saqlanishi va uzluksizlik tenglamasi."""
import numpy as np
from labkit import PARAMS, note, series, table, value

d1 = float(PARAMS.get("d1", 100.0))*1e-3     # kirish diametri, m
d2 = float(PARAMS.get("d2", 60.0))*1e-3      # chiqish diametri, m
v1 = float(PARAMS.get("v1", 2.0))            # kirish tezligi, m/s
rho = float(PARAMS.get("rho", 1000.0))       # zichlik, kg/m³
L_cone = float(PARAMS.get("L_cone", 0.3))    # torayish uzunligi, m

A1 = np.pi*d1**2/4
A2 = np.pi*d2**2/4
v2 = v1*A1/A2
Q = v1*A1
m_dot = rho*Q

value("Kirish yuzasi A₁", A1*1e4, "cm²")
value("Chiqish yuzasi A₂", A2*1e4, "cm²")
value("Chiqish tezligi v₂", v2, "m/s")
value("Tezlik nisbati", v2/v1, "—")
value("Hajmiy sarf Q", Q*1000, "l/s")
value("Massa sarfi ṁ", m_dot, "kg/s")
note(f"Tekshirish: (d₁/d₂)² = {(d1/d2)**2:.4f}, v₂/v₁ = {v2/v1:.4f} ✓")

# Torayish bo'ylab tezlik va tezlanish
x = np.linspace(0, L_cone, 200)
d_x = d1 + (d2-d1)*x/L_cone
A_x = np.pi*d_x**2/4
v_x = Q/A_x
a_x = v_x*np.gradient(v_x, x)

series("Diametr d(x)", x.tolist(), (d_x*1000).tolist(), xlabel="x, m", ylabel="d, mm")
series("Tezlik v(x)", x.tolist(), v_x.tolist(), xlabel="x, m", ylabel="v, m/s")
series("Tezlanish a(x)", x.tolist(), a_x.tolist(), xlabel="x, m", ylabel="a, m/s²")
value("Maksimal tezlanish", float(np.max(a_x)), "m/s²")
value("a_max / g", float(np.max(a_x)/9.81), "—")

# Bernulli bo'yicha bosim tushishi (tmm-26 ga tayyorgarlik)
dp = rho*(v2**2 - v1**2)/2
value("Bosim tushishi Δp", dp/1000, "kPa")
value("Δp (suv ustuni)", dp/(rho*9.81), "m")

# Sarf saqlanishini sonli tekshirish
Q_x = v_x*A_x
note(f"Sarf bo'ylab o'zgarish: min {np.min(Q_x)*1000:.6f}, max {np.max(Q_x)*1000:.6f} l/s — "
     f"farq {np.ptp(Q_x)/np.mean(Q_x)*100:.2e} % (nol bo'lishi kerak) ✓")

# Divergensiya nolga tengligini tekshirish (2D oqim misolida)
nx = 60
xg = np.linspace(-1, 1, nx)
yg = np.linspace(-1, 1, nx)
X, Y = np.meshgrid(xg, yg)
U = X            # v_x = x
V = -Y           # v_y = -y  (siqilmaydigan)
divU = np.gradient(U, xg, axis=1) + np.gradient(V, yg, axis=0)
note(f"Siqilmaydigan oqim (v = (x, -y)): max|∇·v| = {np.max(np.abs(divU)):.2e} ✓")

U2 = X          # siqiluvchan misol: v = (x, y)
V2 = Y
divU2 = np.gradient(U2, xg, axis=1) + np.gradient(V2, yg, axis=0)
note(f"Siqiluvchan oqim (v = (x, y)): ∇·v = {np.median(divU2):.3f} ≠ 0 — "
     "bunday oqimda zichlik o'zgarishi shart.")

# Siqiluvchanlik mezoni
a_sound = 340.0
for v_test in (10, 50, 80, 120, 200, 300):
    Ma = v_test/a_sound
    drho = Ma**2/2*100
    verdict = ("siqilmaydigan faraz o'rinli" if Ma < 0.3
               else "siqiluvchanlik hisobga olinishi kerak")
    note(f"v = {v_test} m/s: Ma = {Ma:.3f}, d(rho)/rho = {drho:.2f} % — {verdict}")

table("Uzluksizlik tenglamasining shakllari",
      ["Shakl", "Tenglama", "Qo'llanilishi"],
      [["Umumiy", "∂ρ/∂t + ∇·(ρv) = 0", "Har qanday oqim"],
       ["Statsionar", "∇·(ρv) = 0", "Vaqtga bog'liq bo'lmagan oqim"],
       ["Siqilmaydigan", "∇·v = 0", "Suyuqlik, Ma < 0,3"],
       ["Quvur (1D)", "ρ₁v₁A₁ = ρ₂v₂A₂", "Gidravlik hisoblar"]])
''',
                parameters=[
                    p("d1", "Kirish diametri d₁", 10.0, 500.0, 100.0, 5.0, "mm"),
                    p("d2", "Chiqish diametri d₂", 5.0, 500.0, 60.0, 5.0, "mm"),
                    p("v1", "Kirish tezligi v₁", 0.1, 100.0, 2.0, 0.1, "m/s"),
                    p("rho", "Zichlik ρ", 1.0, 14000.0, 1000.0, 10.0, "kg/m³"),
                    p("L_cone", "Torayish uzunligi", 0.05, 2.0, 0.3, 0.05, "m"),
                ],
                expected_output="v₂ = 5,56 m/s, Q = 15,7 l/s, Δp = 13,5 kPa",
            ),
            visualization=vis(
                "Oqim naychasi va sarf saqlanishi",
                "React/SVG",
                "Torayuvchi quvur kesimi; oqim chiziqlari zichlashadi; "
                "tezlik strelkalari uzayadi. Ostida $v(x)$ va $a(x)$ "
                "grafiklari.",
                "React/SVG: oqim chiziqlarining zichlashishi massa "
                "saqlanishining eng aniq vizual ifodasi — chiziqlar orasi "
                "kamaysa, tezlik ortadi. Bu tasvir tmm-26 dagi Bernulli "
                "tenglamasida qayta ishlatiladi.",
            ),
            interpretation=(
                "Sarfning bo'ylama o'zgarishi $10^{-14}$ % — bu sonli "
                "hisobning to'g'riligini tasdiqlaydi. Divergensiya "
                "tekshiruvi ikki oqim uchun qarama-qarshi natija beradi: "
                "$\\mathbf{v} = (x, -y)$ siqilmaydigan, $\\mathbf{v} = (x, y)$ "
                "esa emas. Max soni jadvali esa gazlar uchun chegarani "
                "aniq beradi: 100 m/s gacha siqilmaydigan faraz qabul "
                "qilinadi."
            ),
            common_mistakes=[
                "Tezlikni diametrga teskari proporsional deb hisoblash — "
                "u yuzaga, ya'ni $d^2$ ga teskari.",
                "Siqiluvchan oqimda $\\nabla\\cdot\\mathbf{v} = 0$ ni "
                "ishlatish.",
                "Massa va hajmiy sarfni chalkashtirish.",
                "Nazorat hajmi va moddiy hajmni farqlamaslik.",
            ],
            quiz=[
                q("Quvur diametri 2 marta kamaysa, tezlik necha marta oshadi?",
                  "4 marta — yuza $d^2$ ga proporsional.", "hisob"),
                q("$\\nabla\\cdot\\mathbf{v} = 0$ nimani anglatadi?",
                  "Hajm saqlanadi — siqilmaydigan oqim. Har qanday hajmga "
                  "kirgan suyuqlik miqdori undan chiqqaniga teng.",
                  "konseptual"),
                q("$Q = 20$ l/s, $d = 50$ mm. Tezlikni toping.",
                  "$A = 1{,}963\\cdot10^{-3}$ m²; $v = 0{,}02/1{,}963\\cdot10^{-3} = "
                  "10{,}2$ m/s.", "hisob"),
                q("Gaz oqimida qachon siqiluvchanlikni hisobga olish kerak?",
                  "$Ma > 0{,}3$ da, chunki zichlik o'zgarishi 5 % dan "
                  "oshadi.", "talqin"),
                q("Kodda sarf saqlanishi qanday tekshirilgan?",
                  "$Q(x) = v(x)A(x)$ ni butun uzunlik bo'ylab hisoblab, "
                  "uning o'zgarmasligini ko'rsatish orqali.", "kod"),
            ],
            bridge_to_next=(
                "Massa balansi yozildi. Endi impuls balansiga o'tamiz — u "
                "harakat tenglamalarini beradi."
            ),
            research_extension=(
                "Siqiluvchan oqim uchun uzluksizlik tenglamasini energiya "
                "tenglamasi bilan birgalikda yeching: Laval soplosida "
                "(torayuvchi-kengayuvchi) tezlikning tovush tezligidan "
                "oshishini ko'rsating. Nima uchun tovushdan yuqori tezlikda "
                "kengayish tezlikni oshiradi?"
            ),
        ),
    ),
    Topic(
        id="tmm-10",
        subject_id=S,
        module_id=M,
        order=10,
        title="Impuls balansi va Koshi harakat tenglamalari",
        description=(
            "Impuls saqlanish qonunining kontinuumga umumlashmasi, Koshi "
            "harakat tenglamalari, muvozanat tenglamalari."
        ),
        learning_objective=(
            "Koshi harakat tenglamalarini keltirib chiqarish va ularni "
            "muvozanat masalalarida qo'llash."
        ),
        prerequisites=["tmm-09", "tmm-07", "nm-13"],
        mathematical_core=(
            "Reynolds transport teoremasi, divergensiya teoremasi, "
            "$\\rho\\frac{Dv_i}{Dt} = \\sigma_{ij,j} + \\rho b_i$."
        ),
        engineering_application=(
            "Elastiklik nazariyasi, suyuqliklar dinamikasi, FEM va CFD "
            "dasturlarining asosiy tenglamasi."
        ),
        computational_component=(
            "Berilgan kuchlanish maydonida muvozanat tenglamalarini "
            "tekshirish va hajmiy kuchlarni topish."
        ),
        visualization_component=(
            "Elementar hajm va unga ta'sir etuvchi kuchlanishlar; "
            "muvozanat sxemasi."
        ),
        research_extension=(
            "Muvozanat tenglamalari yechimi yagonami? Sen-Venan prinsipi "
            "va yechimlar oilasi."
        ),
        difficulty="murakkab",
        previous_link=(
            "nm-13 dagi impuls teoremasi endi kontinuumga umumlashtiriladi; "
            "tmm-07 dagi Koshi formulasi sirt kuchlarini ifodalash uchun "
            "ishlatiladi."
        ),
        next_topic="tmm-11",
        estimated_minutes=90,
        tags=["harakat tenglamalari", "impuls balansi", "muvozanat"],
        lesson=Lesson(
            physical_problem=(
                "Materiallar qarshiligida muvozanatni butun jism uchun "
                "yozdik: $\\sum F = 0$. Lekin jism ichidagi har bir nuqta "
                "ham muvozanatda bo'lishi kerak. Bu qanday ifodalanadi? "
                "Javob — differensial muvozanat tenglamalarida va ular "
                "butun elastiklik nazariyasi hamda gidrodinamikaning "
                "asosini tashkil qiladi."
            ),
            concepts=[
                c("Sirt kuchlari", "$\\oint_S\\mathbf{t}\\,dS$ — chegara "
                  "orqali uzatiladigan kuchlar; Koshi formulasi orqali "
                  "kuchlanish tenzoriga bog'lanadi."),
                c("Hajmiy kuchlar", "$\\int_V\\rho\\mathbf{b}\\,dV$ — "
                  "og'irlik, inersiya, magnit kuchlari."),
                c("Koshi harakat tenglamalari", "$\\rho\\frac{Dv_i}{Dt} = "
                  "\\frac{\\partial\\sigma_{ij}}{\\partial x_j} + \\rho b_i$."),
                c("Muvozanat tenglamalari", "Statik holda: "
                  "$\\sigma_{ij,j} + \\rho b_i = 0$ — 3 ta tenglama, 6 ta "
                  "noma'lum (statik aniqmaslik)."),
                c("Chegaraviy shartlar", "Kuchlanish bo'yicha: "
                  "$\\sigma_{ij}n_j = \\bar t_i$; ko'chish bo'yicha: "
                  "$u_i = \\bar u_i$."),
            ],
            derivation=[
                d("1-qadam. Impuls balansi",
                  r"\frac{D}{Dt}\int_V\rho\mathbf{v}\,dV = \oint_S\mathbf{t}\,dS + \int_V\rho\mathbf{b}\,dV",
                  "Nyutonning ikkinchi qonuni moddiy hajm uchun: impulsning "
                  "o'zgarish tezligi tashqi kuchlar yig'indisiga teng."),
                d("2-qadam. Koshi formulasini qo'llash",
                  r"\oint_S t_i\,dS = \oint_S\sigma_{ij}n_j\,dS = \int_V\frac{\partial\sigma_{ij}}{\partial x_j}dV",
                  "Divergensiya teoremasi sirt integralini hajm integraliga "
                  "aylantiradi."),
                d("3-qadam. Chap tomonni soddalashtirish",
                  r"\frac{D}{Dt}\int_V\rho v_i\,dV = \int_V\rho\frac{Dv_i}{Dt}dV",
                  "Reynolds teoremasi va uzluksizlik tenglamasi (tmm-09) "
                  "birgalikda: massa saqlanishi tufayli $\\rho\\,dV$ "
                  "o'zgarmaydi."),
                d("4-qadam. Koshi harakat tenglamalari",
                  r"\boxed{\;\rho\frac{Dv_i}{Dt} = \frac{\partial\sigma_{ij}}{\partial x_j} + \rho b_i\;}",
                  "Integral ixtiyoriy hajm uchun nolga teng, demak integral "
                  "osti ifodasi nolga teng. Bu — kontinuum mexanikasining "
                  "markaziy tenglamasi."),
                d("5-qadam. Statik hol: muvozanat tenglamalari",
                  r"\frac{\partial\sigma_{11}}{\partial x_1}+\frac{\partial\sigma_{12}}{\partial x_2}+"
                  r"\frac{\partial\sigma_{13}}{\partial x_3} + \rho b_1 = 0\quad(\text{va sikl bo'yicha})",
                  "3 ta tenglama, 6 ta noma'lum kuchlanish — masala statik "
                  "aniqmas. Yechish uchun konstitutiv tenglamalar (tmm-14) "
                  "va moslik shartlari (tmm-05) kerak."),
            ],
            formula_meaning=(
                "Koshi tenglamalari Nyutonning ikkinchi qonunining "
                "kontinuum shakli: chap tomonda inersiya, o'ngda kuchlar. "
                "$\\sigma_{ij,j}$ hadi fizik jihatdan 'kuchlanishning "
                "notekisligi' — agar kuchlanish hamma joyda bir xil bo'lsa, "
                "natijaviy kuch nolga teng. Aynan shu tenglama qattiq jism "
                "mexanikasida Navye tenglamalariga (tmm-15), suyuqliklarda "
                "esa Navye–Stoks tenglamalariga (tmm-27) aylanadi."
            ),
            equations=[
                eq(r"\rho\frac{Dv_i}{Dt} = \sigma_{ij,j} + \rho b_i", "Koshi harakat tenglamalari.",
                   "Harakat tenglamalari"),
                eq(r"\sigma_{ij,j} + \rho b_i = 0", "Muvozanat tenglamalari (statika).",
                   "Muvozanat"),
                eq(r"\sigma_{ij}n_j = \bar t_i\ \text{(S}_t\text{)},\quad u_i = \bar u_i\ \text{(S}_u\text{)}",
                   "Chegaraviy shartlar.", "Chegaraviy shartlar"),
            ],
            conditions=(
                "Chegaraviy shartlar har bir nuqtada yo kuchlanish, yo "
                "ko'chish bo'yicha berilishi kerak (ikkalasi birdan emas). "
                "Aralash shartlar ham mumkin (masalan, normal yo'nalishda "
                "ko'chish, urinma yo'nalishda kuchlanish). Yechim mavjudligi "
                "uchun tashqi kuchlar o'zaro muvozanatlashgan bo'lishi shart."
            ),
            worked_example=WorkedExample(
                statement=(
                    "Tekis kuchlanish maydoni berilgan: "
                    "$\\sigma_{11} = 3x_1^2 + 4x_1x_2 - 8x_2^2$, "
                    "$\\sigma_{22} = 2x_1^2 + x_1x_2 - 3x_2^2$, "
                    "$\\sigma_{12} = -\\frac{1}{2}x_1^2 - 6x_1x_2 - 2x_2^2$ "
                    "(MPa, koordinatalar m da). Hajmiy kuchlar nolga teng "
                    "bo'lsa, muvozanat tenglamalari bajariladimi?"
                ),
                given=[r"\sigma_{11}, \sigma_{22}, \sigma_{12}\ \text{yuqoridagi kabi};\; b_i = 0"],
                steps=[
                    st(r"\frac{\partial\sigma_{11}}{\partial x_1} = 6x_1+4x_2;\qquad "
                       r"\frac{\partial\sigma_{12}}{\partial x_2} = -6x_1-4x_2",
                       "Birinchi tenglama uchun hosilalar."),
                    st(r"\frac{\partial\sigma_{11}}{\partial x_1}+\frac{\partial\sigma_{12}}{\partial x_2} = "
                       r"(6x_1+4x_2)+(-6x_1-4x_2) = 0\ \checkmark",
                       "Birinchi muvozanat tenglamasi bajarildi."),
                    st(r"\frac{\partial\sigma_{12}}{\partial x_1} = -x_1-6x_2;\qquad "
                       r"\frac{\partial\sigma_{22}}{\partial x_2} = x_1-6x_2",
                       "Ikkinchi tenglama uchun hosilalar."),
                    st(r"\frac{\partial\sigma_{12}}{\partial x_1}+\frac{\partial\sigma_{22}}{\partial x_2} = "
                       r"(-x_1-6x_2)+(x_1-6x_2) = -12x_2 \neq 0",
                       "Ikkinchi tenglama BAJARILMADI."),
                    st(r"\rho b_2 = 12x_2\ \text{kerak}",
                       "Muvozanat uchun hajmiy kuch kerak: "
                       "$b_2 = 12x_2/\\rho$."),
                    st(r"\text{Xulosa: berilgan maydon } b_i = 0 \text{ da mumkin emas}",
                       "Bu — kuchlanish maydonini postulat qilishning "
                       "cheklovi: u muvozanat tenglamalarini "
                       "qanoatlantirishi shart."),
                ],
                answer=(
                    "Birinchi tenglama bajariladi, ikkinchisi yo'q; "
                    "muvozanat uchun $\\rho b_2 = 12x_2$ hajmiy kuch talab "
                    "qilinadi."
                ),
                engineering_note=(
                    "Bu tekshiruv — kuchlanish usulida yechish (tmm-17) "
                    "uchun majburiy qadam. Eyri kuchlanish funksiyasi aynan "
                    "shuning uchun kiritiladi: u muvozanat tenglamalarini "
                    "avtomatik qanoatlantiradi va noma'lumlar sonini "
                    "kamaytiradi."
                ),
            ),
            computation=Computation(
                caption=(
                    "Muvozanat tenglamalari: kuchlanish maydonini tekshiring "
                    "va kerakli hajmiy kuchlarni toping."
                ),
                code='''"""Koshi harakat tenglamalari va muvozanat tekshiruvi."""
import numpy as np
import sympy as sp
from labkit import PARAMS, note, series, table, value

a1 = float(PARAMS.get("a1", 3.0))
a2 = float(PARAMS.get("a2", 4.0))
a3 = float(PARAMS.get("a3", -8.0))
rho = float(PARAMS.get("rho", 7850.0))
g_acc = float(PARAMS.get("g", 0.0))

x1, x2 = sp.symbols("x1 x2")
s11 = a1*x1**2 + a2*x1*x2 + a3*x2**2
s22 = 2*x1**2 + x1*x2 - 3*x2**2
s12 = -sp.Rational(1, 2)*x1**2 - 6*x1*x2 - 2*x2**2

eq1 = sp.simplify(sp.diff(s11, x1) + sp.diff(s12, x2))
eq2 = sp.simplify(sp.diff(s12, x1) + sp.diff(s22, x2))
note(f"1-tenglama: ∂σ₁₁/∂x₁ + ∂σ₁₂/∂x₂ = {eq1}")
note(f"2-tenglama: ∂σ₁₂/∂x₁ + ∂σ₂₂/∂x₂ = {eq2}")

b1_req = sp.simplify(-eq1/rho)
b2_req = sp.simplify(-eq2/rho)
note(f"Muvozanat uchun kerakli hajmiy kuchlar: b₁ = {b1_req}, b₂ = {b2_req}")
if eq1 == 0 and eq2 == 0:
    note("Muvozanat tenglamalari HAJMIY KUCHSIZ bajariladi ✓")
else:
    note("DIQQAT: hajmiy kuchlarsiz muvozanat BAJARILMAYDI")

# Sonli tekshirish to'r ustida
n = 60
xs = np.linspace(-1, 1, n)
ys = np.linspace(-1, 1, n)
X, Y = np.meshgrid(xs, ys)
f11 = sp.lambdify((x1, x2), s11, "numpy")
f22 = sp.lambdify((x1, x2), s22, "numpy")
f12 = sp.lambdify((x1, x2), s12, "numpy")
S11 = f11(X, Y); S22 = f22(X, Y); S12 = f12(X, Y)

d11_dx = np.gradient(S11, xs, axis=1)
d12_dy = np.gradient(S12, ys, axis=0)
d12_dx = np.gradient(S12, xs, axis=1)
d22_dy = np.gradient(S22, ys, axis=0)
res1 = d11_dx + d12_dy
res2 = d12_dx + d22_dy

value("1-tenglama qoldig'i (maks)", float(np.max(np.abs(res1))), "MPa/m")
value("2-tenglama qoldig'i (maks)", float(np.max(np.abs(res2))), "MPa/m")

series("Qoldiq R₁(x₁), x₂=0", xs.tolist(), res1[n//2, :].tolist(),
       xlabel="x₁, m", ylabel="R₁, MPa/m")
series("Qoldiq R₂(x₂), x₁=0", ys.tolist(), res2[:, n//2].tolist(),
       xlabel="x₂, m", ylabel="R₂, MPa/m")

# Og'irlik ta'siridagi oddiy yechim: o'z og'irligi ostida ustun
H = 10.0
z = np.linspace(0, H, 200)
sigma_z = -rho*g_acc*(H - z)/1e6 if g_acc > 0 else np.zeros_like(z)
series("σ_zz(z) — o'z og'irligi", z.tolist(), sigma_z.tolist(),
       xlabel="z, m", ylabel="σ_zz, MPa")
if g_acc > 0:
    note(f"O'z og'irligi ostidagi ustunda: σ_zz = -ρg(H-z), "
         f"tagida {rho*g_acc*H/1e6:.4f} MPa. "
         "Muvozanat tenglamasi ∂σ_zz/∂z + ρb_z = 0 ni qanoatlantiradi ✓")

table("Koshi tenglamalarining xususiy hollari",
      ["Hol", "Tenglama", "Natija"],
      [["Statika", "σ_ij,j + ρb_i = 0", "Muvozanat tenglamalari"],
       ["Elastik jism", "σ = C:ε", "Navye tenglamalari (tmm-15)"],
       ["Ideal suyuqlik", "σ = -pI", "Eyler tenglamalari (tmm-26)"],
       ["Yopishqoq suyuqlik", "σ = -pI + 2μD", "Navye–Stoks (tmm-27)"]])

table("Noma'lumlar va tenglamalar balansi",
      ["Kattalik", "Soni", "Izoh"],
      [["Kuchlanish σ_ij", 6, "Simmetriya hisobga olingan"],
       ["Muvozanat tenglamalari", 3, "Yetarli emas!"],
       ["Ko'chish u_i", 3, "Qo'shimcha noma'lumlar"],
       ["Deformatsiya ε_ij", 6, "Kinematik bog'lanish"],
       ["Konstitutiv tenglamalar", 6, "Material xossalari"],
       ["JAMI", "15 = 15", "Masala yopiladi"]])
''',
                parameters=[
                    p("a1", "Koeffitsient a₁", -10.0, 10.0, 3.0, 0.5, "—"),
                    p("a2", "Koeffitsient a₂", -10.0, 10.0, 4.0, 0.5, "—"),
                    p("a3", "Koeffitsient a₃", -20.0, 20.0, -8.0, 0.5, "—"),
                    p("rho", "Zichlik ρ", 100.0, 20000.0, 7850.0, 100.0, "kg/m³"),
                    p("g", "Og'irlik tezlanishi", 0.0, 20.0, 0.0, 0.5, "m/s²"),
                ],
                expected_output="1-tenglama: 0 ✓; 2-tenglama: -12x₂ ≠ 0 — hajmiy kuch kerak",
            ),
            visualization=vis(
                "Elementar hajm muvozanati",
                "React/SVG",
                "Kub elementi; har bir yuzada kuchlanish komponentalari "
                "strelkalar bilan; qarama-qarshi yuzalarda kuchlanish "
                "$\\sigma + \\frac{\\partial\\sigma}{\\partial x}dx$ "
                "ko'rinishida; hajmiy kuch markazda.",
                "React/SVG: bu klassik chizma muvozanat tenglamalarining "
                "kelib chiqishini to'g'ridan-to'g'ri ko'rsatadi. "
                "Kuchlanishning ortishini ($+d\\sigma$) alohida rang bilan "
                "belgilash tushunishni osonlashtiradi.",
            ),
            interpretation=(
                "Sonli tekshiruv simvolik natijani tasdiqlaydi: birinchi "
                "qoldiq mashina aniqligida nol, ikkinchisi esa $-12x_2$ "
                "qonuni bo'yicha o'zgaradi. Noma'lumlar balansi jadvali "
                "esa elastiklik nazariyasining tuzilishini ochib beradi: "
                "15 ta noma'lum va 15 ta tenglama — masala to'liq yopiladi. "
                "Bu — tmm-15 dagi to'la masalaning asosi."
            ),
            common_mistakes=[
                "Muvozanat tenglamalarini tekshirmasdan kuchlanish maydonini "
                "postulat qilish.",
                "Hajmiy kuchni kuchlanish o'lchamligida olish "
                "($b_i$ — tezlanish o'lchamida, N/kg).",
                "Dinamik holatda inersiya hadini unutish.",
                "Chegaraviy shartlarda kuchlanish va ko'chishni bir vaqtda "
                "berish.",
            ],
            quiz=[
                q("Nima uchun muvozanat tenglamalari yetarli emas?",
                  "3 ta tenglama, 6 ta noma'lum kuchlanish — masala statik "
                  "aniqmas. Konstitutiv tenglamalar va kinematika kerak.",
                  "konseptual"),
                q("$\\sigma_{ij,j}$ hadining fizik ma'nosi nima?",
                  "Kuchlanishning notekisligi — elementar hajmga ta'sir "
                  "etuvchi natijaviy sirt kuchi.", "konseptual"),
                q("$\\sigma_{11} = kx_1$, qolganlari nol. Hajmiy kuch qancha "
                  "bo'lishi kerak?",
                  "$\\partial\\sigma_{11}/\\partial x_1 + \\rho b_1 = 0 "
                  "\\Rightarrow b_1 = -k/\\rho$.", "hisob"),
                q("Statik va dinamik tenglamalar orasidagi farq nima?",
                  "Dinamikda chap tomonda $\\rho Dv_i/Dt$ inersiya hadi bor; "
                  "statikada u nolga teng.", "talqin"),
                q("Kodda noma'lumlar balansi jadvali nimani ko'rsatadi?",
                  "Elastiklik nazariyasida 15 ta noma'lum (6 σ + 6 ε + 3 u) "
                  "va 15 ta tenglama (3 muvozanat + 6 kinematika + 6 "
                  "konstitutiv) — masala to'liq yopiladi.", "kod"),
            ],
            bridge_to_next=(
                "Impuls balansi harakat tenglamalarini berdi. Keyingi "
                "mavzuda impuls momenti balansi kuchlanish tenzorining "
                "simmetriyasini isbotlaydi."
            ),
            research_extension=(
                "Muvozanat tenglamalarini silindrik koordinatalarda yozing "
                "va qalin devorli quvur (Lame masalasi) uchun yeching. "
                "Ichki va tashqi bosim ta'sirida $\\sigma_r(r)$ va "
                "$\\sigma_\\theta(r)$ taqsimotlarini toping — bu bosimli "
                "idishlar hisobining klassik masalasi."
            ),
        ),
    ),
    Topic(
        id="tmm-11",
        subject_id=S,
        module_id=M,
        order=11,
        title="Impuls momenti balansi va kuchlanish tenzorining simmetriyasi",
        description=(
            "Impuls momenti saqlanishidan kuchlanish tenzori "
            "simmetriyasining kelib chiqishi; moment kuchlanishlari va "
            "Kosserat kontinuumi."
        ),
        learning_objective=(
            "Kuchlanish tenzori simmetriyasini isbotlash va uning "
            "qo'llanish chegaralarini tushuntirish."
        ),
        prerequisites=["tmm-10"],
        mathematical_core=(
            "Impuls momenti balansi, Levi-Civita simvoli, "
            "$\\epsilon_{ijk}\\sigma_{jk} = 0 \\Leftrightarrow "
            "\\sigma_{ij} = \\sigma_{ji}$."
        ),
        engineering_application=(
            "Barcha klassik hisoblar simmetriyaga tayanadi; mikropolyar "
            "muhitlar (g'ovakli materiallar, granulalar) uchun istisno."
        ),
        computational_component=(
            "Simmetriya buzilishining oqibatlarini modellashtirish va "
            "moment muvozanatini tekshirish."
        ),
        visualization_component=(
            "Elementar kvadratning moment muvozanati; urinma "
            "kuchlanishlar juftligi."
        ),
        research_extension=(
            "Kosserat (mikropolyar) kontinuumi: qanday materiallarda "
            "moment kuchlanishlari muhim?"
        ),
        difficulty="murakkab",
        previous_link=(
            "mq-09 da urinma kuchlanishlar juftligi qonunini elementar "
            "muvozanatdan oldik. Endi uni umumiy balans qonunidan "
            "keltirib chiqaramiz."
        ),
        next_topic="tmm-12",
        estimated_minutes=75,
        tags=["simmetriya", "impuls momenti", "Kosserat"],
        lesson=Lesson(
            physical_problem=(
                "Kuchlanish tenzorida 9 ta komponenta bor, lekin barcha "
                "darsliklar 6 ta deb yozadi. Nima uchun? Chunki tenzor "
                "simmetrik. Lekin bu shunchaki qulaylik emas — u chuqur "
                "fizik qonundan, impuls momenti saqlanishidan kelib "
                "chiqadi. Va ba'zi materiallarda bu simmetriya buziladi."
            ),
            concepts=[
                c("Impuls momenti balansi", "$\\frac{D}{Dt}\\int\\rho(\\mathbf{r}\\times\\mathbf{v})dV = "
                  "\\oint(\\mathbf{r}\\times\\mathbf{t})dS + \\int\\rho(\\mathbf{r}\\times\\mathbf{b})dV$."),
                c("Kuchlanish tenzorining simmetriyasi", "$\\sigma_{ij} = "
                  "\\sigma_{ji}$ — 9 ta komponenta 6 taga tushadi."),
                c("Urinma kuchlanishlar juftligi", "Simmetriyaning "
                  "muhandislik shakli: $\\tau_{xy} = \\tau_{yx}$."),
                c("Moment kuchlanishlari", "Kosserat kontinuumida "
                  "qo'shimcha kattalik: sirt orqali moment ham uzatiladi."),
                c("Mikropolyar muhitlar", "G'ovakli materiallar, granulalar, "
                  "suyuq kristallar — ularda simmetriya buzilishi mumkin."),
            ],
            derivation=[
                d("1-qadam. Impuls momenti balansini yozish",
                  r"\frac{D}{Dt}\int_V\rho\,\epsilon_{ijk}x_jv_k\,dV = "
                  r"\oint_S\epsilon_{ijk}x_jt_k\,dS + \int_V\rho\,\epsilon_{ijk}x_jb_k\,dV",
                  "Indeksli yozuvda. $\\epsilon_{ijk}$ vektor ko'paytmani "
                  "ifodalaydi."),
                d("2-qadam. Sirt integralini o'zgartirish",
                  r"\oint_S\epsilon_{ijk}x_j\sigma_{kl}n_l\,dS = "
                  r"\int_V\epsilon_{ijk}\frac{\partial(x_j\sigma_{kl})}{\partial x_l}dV = "
                  r"\int_V\epsilon_{ijk}(\sigma_{kj} + x_j\sigma_{kl,l})dV",
                  "Divergensiya teoremasi va ko'paytmani differensiallash; "
                  "$\\partial x_j/\\partial x_l = \\delta_{jl}$."),
                d("3-qadam. Harakat tenglamalaridan foydalanish",
                  r"\epsilon_{ijk}x_j(\sigma_{kl,l}+\rho b_k) = \epsilon_{ijk}x_j\rho\frac{Dv_k}{Dt}",
                  "tmm-10 dagi Koshi tenglamalari. Bu hadlar chap tomondagi "
                  "hadlar bilan qisqaradi."),
                d("4-qadam. Simmetriya sharti",
                  r"\int_V\epsilon_{ijk}\sigma_{kj}\,dV = 0 \;\Rightarrow\; "
                  r"\epsilon_{ijk}\sigma_{kj} = 0 \;\Rightarrow\; "
                  r"\boxed{\;\sigma_{ij} = \sigma_{ji}\;}",
                  "$\\epsilon_{ijk}$ antisimmetrik, shuning uchun uning "
                  "$\\sigma_{kj}$ bilan svertkasi nolga teng bo'lishi "
                  "tenzorning simmetrikligini talab qiladi."),
            ],
            formula_meaning=(
                "Simmetriya $\\sigma_{ij} = \\sigma_{ji}$ — impuls momenti "
                "saqlanishining bevosita natijasi. Uning amaliy ahamiyati "
                "katta: noma'lumlar soni 9 dan 6 ga tushadi, tenzor "
                "haqiqiy xususiy qiymatlarga ega bo'ladi (asosiy "
                "kuchlanishlar), Mor doirasi qurish mumkin bo'ladi. Agar "
                "muhitda taqsimlangan momentlar bo'lsa (magnit maydonidagi "
                "ferroflyuid, granulali materiallar), simmetriya buziladi "
                "va Kosserat nazariyasi kerak bo'ladi."
            ),
            equations=[
                eq(r"\epsilon_{ijk}\sigma_{jk} = 0 \iff \sigma_{ij} = \sigma_{ji}",
                   "Kuchlanish tenzorining simmetriyasi.", "Simmetriya"),
                eq(r"\tau_{xy} = \tau_{yx}", "Urinma kuchlanishlar juftligi qonuni.",
                   "Juftlik qonuni"),
            ],
            conditions=(
                "Simmetriya taqsimlangan hajmiy momentlar bo'lmagan "
                "klassik kontinuumda o'rinli. Istisnolar: magnit yoki "
                "elektr maydonidagi qutblangan muhitlar, granulali "
                "materiallar (kontakt momentlari), suyuq kristallar, "
                "mikrostrukturasi muhim bo'lgan kompozitlar."
            ),
            worked_example=WorkedExample(
                statement=(
                    "Elementar kvadrat ($dx \\times dy \\times 1$) uchun "
                    "moment muvozanatini bevosita yozing va "
                    "$\\tau_{xy} = \\tau_{yx}$ ekanini isbotlang. So'ngra "
                    "simmetriya buzilsa ($\\tau_{xy} - \\tau_{yx} = "
                    "\\Delta\\tau = 5$ MPa) elementga qanday burchak "
                    "tezlanish paydo bo'lishini baholang ($\\rho = 7850$ "
                    "kg/m³, $dx = dy = 1$ mm)."
                ),
                given=[r"dx = dy = 10^{-3}\ \text{m},\; \rho = 7850\ \text{kg/m}^3",
                       r"\Delta\tau = 5\ \text{MPa}"],
                steps=[
                    st(r"\sum M_z = \tau_{xy}(dy\cdot1)dx - \tau_{yx}(dx\cdot1)dy = "
                       r"(\tau_{xy}-\tau_{yx})dx\,dy",
                       "Ikki juft urinma kuchlanishning markazga nisbatan "
                       "momenti."),
                    st(r"J_z = \frac{\rho\,dx\,dy(dx^2+dy^2)}{12} = "
                       r"\frac{\rho\,dx\,dy\cdot2dx^2}{12}",
                       "Elementar kvadratning inersiya momenti (nm-17)."),
                    st(r"(\tau_{xy}-\tau_{yx})dx\,dy = J_z\varepsilon = "
                       r"\frac{\rho\,dx^3dy}{6}\varepsilon",
                       "Moment tenglamasi."),
                    st(r"\varepsilon = \frac{6\Delta\tau}{\rho\,dx^2} = "
                       r"\frac{6\cdot5\cdot10^6}{7850\cdot10^{-6}} = 3{,}82\cdot10^{12}\ \text{rad/s}^2",
                       "Burchak tezlanish — astronomik katta qiymat!"),
                    st(r"dx\to0:\ \varepsilon \to \infty",
                       "Element kichrayganda tezlanish cheksizlikka intiladi "
                       "— bu fizik jihatdan mumkin emas."),
                    st(r"\Rightarrow \Delta\tau = 0,\ \text{ya'ni}\ \tau_{xy} = \tau_{yx}",
                       "Yagona mumkin bo'lgan xulosa: simmetriya."),
                ],
                answer=(
                    "$\\varepsilon = 3{,}82\\cdot10^{12}$ rad/s² — fizik "
                    "jihatdan imkonsiz; demak $\\tau_{xy} = \\tau_{yx}$."
                ),
                engineering_note=(
                    "Bu isbot simmetriyaning 'kelishuv' emas, fizik zarurat "
                    "ekanini ko'rsatadi. Element kichrayganda inersiya "
                    "momenti $dx^4$ tartibida, moment esa $dx^2$ tartibida "
                    "kamayadi — shuning uchun nomutanosiblik tezlanishni "
                    "cheksizlikka olib boradi."
                ),
            ),
            computation=Computation(
                caption=(
                    "Simmetriya: moment muvozanatini tekshiring va "
                    "buzilishning oqibatlarini baholang."
                ),
                code='''"""Kuchlanish tenzori simmetriyasi va uning oqibatlari."""
import numpy as np
from labkit import PARAMS, note, series, table, value

tau_xy = float(PARAMS.get("tau_xy", 50.0))    # MPa
tau_yx = float(PARAMS.get("tau_yx", 50.0))    # MPa
rho = float(PARAMS.get("rho", 7850.0))
dx = float(PARAMS.get("dx", 1.0))*1e-3        # element o'lchami, m

d_tau = (tau_xy - tau_yx)*1e6
value("τ_xy", tau_xy, "MPa")
value("τ_yx", tau_yx, "MPa")
value("Farq Δτ", tau_xy-tau_yx, "MPa")

if abs(d_tau) < 1e-9:
    note("Simmetriya bajarilgan: τ_xy = τ_yx ✓ — tenzor simmetrik.")
    eps_ang = 0.0
else:
    eps_ang = 6*d_tau/(rho*dx**2)
    value("Burchak tezlanish ε", eps_ang, "rad/s²")
    note(f"Simmetriya buzilgan! Element {dx*1000:.2f} mm uchun burchak "
         f"tezlanish {eps_ang:.3e} rad/s² — fizik jihatdan imkonsiz.")

# Element o'lchamining ta'siri
sizes = np.logspace(-6, -2, 100)
if abs(d_tau) > 1e-9:
    eps_arr = 6*d_tau/(rho*sizes**2)
    series("Burchak tezlanish ε(dx)", (sizes*1000).tolist(), np.log10(np.abs(eps_arr)).tolist(),
           xlabel="Element o'lchami, mm", ylabel="log₁₀|ε|, rad/s²")
    note("Element kichrayganda tezlanish 1/dx² qonuni bo'yicha o'sadi — "
         "shuning uchun simmetriya buzilishi mumkin emas.")

# Simmetriya buzilishining tenzor xossalariga ta'siri
T_sym = np.array([[100.0, 50.0, 0.0], [50.0, -30.0, 0.0], [0.0, 0.0, 40.0]])
T_asym = np.array([[100.0, tau_xy, 0.0], [tau_yx, -30.0, 0.0], [0.0, 0.0, 40.0]])

ev_sym = np.linalg.eigvals(T_sym)
ev_asym = np.linalg.eigvals(T_asym)
note(f"Simmetrik tenzor xususiy qiymatlari: {np.round(np.real(ev_sym), 3)} "
     f"(mavhum qism: {np.max(np.abs(np.imag(ev_sym))):.2e})")
note(f"Asimmetrik tenzor xususiy qiymatlari: {np.round(np.real(ev_asym), 3)} "
     f"(mavhum qism: {np.max(np.abs(np.imag(ev_asym))):.3f})")
if np.max(np.abs(np.imag(ev_asym))) > 1e-9:
    note("DIQQAT: asimmetrik tenzorda kompleks xususiy qiymatlar paydo bo'ldi — "
         "asosiy kuchlanishlar tushunchasi ma'nosini yo'qotadi!")

# Simmetriyaning amaliy ahamiyati
table("Simmetriyaning oqibatlari",
      ["Xossa", "Simmetrik tenzor", "Asimmetrik tenzor"],
      [["Mustaqil komponentalar", "6", "9"],
       ["Xususiy qiymatlar", "Haqiqiy", "Kompleks bo'lishi mumkin"],
       ["Xususiy vektorlar", "Ortogonal", "Ortogonal emas"],
       ["Mor doirasi", "Qurish mumkin", "Qurib bo'lmaydi"],
       ["Asosiy kuchlanishlar", "Mavjud", "Ta'riflanmaydi"]])

# Moment muvozanatini elementar hajm uchun tekshirish
n_check = 5
rows = []
for size in np.logspace(-5, -2, n_check):
    M_surface = abs(d_tau)*size**2
    J = rho*size**4*2/12
    eps_i = M_surface/J if J > 0 else 0
    rows.append([float(size*1000), float(M_surface), float(J), float(eps_i)])
table("Element o'lchamining ta'siri",
      ["dx, mm", "Sirt momenti, N·m", "J, kg·m²", "ε, rad/s²"], rows)

table("Simmetriya buziladigan holatlar",
      ["Muhit", "Sabab", "Nazariya"],
      [["Granulali material", "Kontakt momentlari", "Kosserat"],
       ["Ferroflyuid", "Magnit momenti", "Mikropolyar"],
       ["Suyuq kristall", "Molekulyar orientatsiya", "Erikson–Lesli"],
       ["Mikrostrukturali kompozit", "O'lchamli effektlar", "Gradiyentli"],
       ["Klassik qattiq jism", "—", "Simmetrik ✓"]])
''',
                parameters=[
                    p("tau_xy", "τ_xy", -200.0, 200.0, 50.0, 5.0, "MPa"),
                    p("tau_yx", "τ_yx", -200.0, 200.0, 50.0, 5.0, "MPa"),
                    p("rho", "Zichlik ρ", 100.0, 20000.0, 7850.0, 100.0, "kg/m³"),
                    p("dx", "Element o'lchami", 0.001, 10.0, 1.0, 0.1, "mm"),
                ],
                expected_output="τ_xy = τ_yx → simmetriya ✓; farq bo'lsa ε ~ 10¹² rad/s²",
            ),
            visualization=vis(
                "Elementar kvadratning moment muvozanati",
                "React/SVG",
                "Kvadrat element; to'rt yuzasida urinma kuchlanishlar "
                "strelkalari; ular hosil qiladigan momentlar aylanma "
                "strelkalar bilan. Simmetriya buzilganda element aylanishga "
                "intilishi ko'rsatiladi.",
                "React/SVG: urinma kuchlanishlar juftligini ko'rsatish — "
                "mexanikaning eng tanilgan chizmalaridan biri. Simmetriya "
                "buzilgan holatni animatsiya bilan (element aylanadi) "
                "ko'rsatish g'oyani mustahkamlaydi.",
            ),
            interpretation=(
                "Jadval element o'lchami kichrayganda burchak tezlanishning "
                "$1/dx^2$ qonuni bo'yicha o'sishini ko'rsatadi — bu "
                "simmetriyaning muqarrarligini isbotlaydi. Asimmetrik "
                "tenzorda kompleks xususiy qiymatlar paydo bo'lishi esa "
                "asosiy kuchlanishlar tushunchasining ma'nosini yo'qotishini "
                "ko'rsatadi: butun klassik apparat simmetriyaga tayanadi."
            ),
            common_mistakes=[
                "Simmetriyani ta'rif yoki kelishuv deb hisoblash — u "
                "fizik qonundan kelib chiqadi.",
                "Kosserat kontinuumini ekzotik deb e'tiborsiz qoldirish — "
                "granulali materiallar juda keng tarqalgan.",
                "Simmetriyani deformatsiya tenzoriga ham avtomatik "
                "ko'chirish (u ta'rifi bo'yicha simmetrik).",
                "Piola–Kirxgof tenzorlarining simmetriya xossalarini "
                "Koshi tenzoriniki bilan chalkashtirish.",
            ],
            quiz=[
                q("Simmetriya qaysi fizik qonundan kelib chiqadi?",
                  "Impuls momenti saqlanish qonunidan.", "konseptual"),
                q("Simmetriya nechta mustaqil komponenta qoldiradi?",
                  "9 dan 6 taga tushiradi.", "hisob"),
                q("Nima uchun asimmetrik tenzorda asosiy kuchlanishlar "
                  "ta'riflanmaydi?",
                  "Uning xususiy qiymatlari kompleks bo'lishi mumkin va "
                  "xususiy vektorlar ortogonal bo'lmaydi.", "konseptual"),
                q("Qaysi materiallarda simmetriya buzilishi mumkin?",
                  "Granulali materiallar, ferroflyuidlar, suyuq kristallar — "
                  "ularda taqsimlangan momentlar mavjud.", "talqin"),
                q("Kodda element o'lchami kichrayganda nima sodir bo'ladi?",
                  "Burchak tezlanish $1/dx^2$ qonuni bo'yicha o'sadi va "
                  "cheksizlikka intiladi — bu simmetriyaning zaruratini "
                  "isbotlaydi.", "kod"),
            ],
            bridge_to_next=(
                "Massa va impuls balanslari yozildi. Oxirgi balans qonuni — "
                "energiya balansi va u termodinamika bilan bog'lanadi."
            ),
            research_extension=(
                "Kosserat kontinuumini o'rganing: qo'shimcha burilish "
                "erkinlik darajalari va moment kuchlanishlari kiritilsa, "
                "tenglamalar qanday o'zgaradi? G'ovakli material uchun "
                "xarakterli uzunlik parametrini kiriting va u o'lchamli "
                "effektlarni qanday tushuntirishini ko'rsating."
            ),
        ),
    ),
    Topic(
        id="tmm-12",
        subject_id=S,
        module_id=M,
        order=12,
        title="Energiya balansi va termodinamikaning ikkinchi qonuni",
        description=(
            "Energiya saqlanish qonuni kontinuumda, ichki energiya, issiqlik "
            "oqimi, entropiya va Klauzius–Dyuhem tengsizligi."
        ),
        learning_objective=(
            "Energiya balansini yozish va termodinamik cheklovlarning "
            "konstitutiv tenglamalarga ta'sirini tushuntirish."
        ),
        prerequisites=["tmm-10", "tmm-11", "nm-15"],
        mathematical_core=(
            "Energiya balansi, dissipatsiya, entropiya tengsizligi, "
            "Klauzius–Dyuhem sharti."
        ),
        engineering_application=(
            "Termoelastiklik, plastik deformatsiyada issiqlik ajralishi, "
            "viskoelastik dissipatsiya, material modellarini tekshirish."
        ),
        computational_component=(
            "Deformatsiya energiyasi va dissipatsiyani hisoblash; "
            "plastik ishning issiqlikka aylanishi."
        ),
        visualization_component=(
            "Energiya oqimlari diagrammasi: mexanik ish → ichki energiya + "
            "issiqlik."
        ),
        research_extension=(
            "Taylor–Quinney koeffitsienti: plastik ishning qancha qismi "
            "issiqlikka aylanadi?"
        ),
        difficulty="ilg'or",
        previous_link=(
            "nm-15 dagi energiya saqlanishi endi kontinuumga "
            "umumlashtiriladi va termodinamika bilan bog'lanadi."
        ),
        next_topic="tmm-13",
        estimated_minutes=85,
        tags=["energiya balansi", "entropiya", "dissipatsiya"],
        lesson=Lesson(
            physical_problem=(
                "Metall simni qayta-qayta bukib uzsak, u qiziydi. Plastik "
                "deformatsiya ishi qayerga ketadi? Taxminan 90 % i "
                "issiqlikka, 10 % i esa kristall panjaradagi nuqsonlarga "
                "(saqlangan energiya). Bu taqsimotni bashorat qilish uchun "
                "energiya balansi va termodinamika kerak."
            ),
            concepts=[
                c("Ichki energiya", "$u$ — birlik massaga to'g'ri keladigan "
                  "energiya; deformatsiya va temperaturaga bog'liq."),
                c("Kuchlanish quvvati", "$\\sigma_{ij}D_{ij}$ — birlik hajmda "
                  "mexanik ish bajarilish tezligi."),
                c("Issiqlik oqimi", "$\\mathbf{q}$ — Furye qonuni bo'yicha "
                  "$\\mathbf{q} = -k\\nabla T$."),
                c("Entropiya", "$s$ — jarayonning qaytmasligi o'lchovi; "
                  "izolyatsiyalangan tizimda kamaymaydi."),
                c("Klauzius–Dyuhem tengsizligi", "Termodinamikaning ikkinchi "
                  "qonunining kontinuum shakli; konstitutiv tenglamalarga "
                  "cheklov qo'yadi."),
            ],
            derivation=[
                d("1-qadam. Energiya balansi",
                  r"\frac{D}{Dt}\int_V\rho\left(u + \tfrac{1}{2}v^2\right)dV = "
                  r"\oint_S(\mathbf{t}\cdot\mathbf{v} - \mathbf{q}\cdot\mathbf{n})dS + "
                  r"\int_V(\rho\mathbf{b}\cdot\mathbf{v} + \rho r)dV",
                  "To'la energiya (ichki + kinetik) ning o'zgarishi = sirt "
                  "kuchlari ishi + issiqlik oqimi + hajmiy kuchlar ishi + "
                  "ichki issiqlik manbai."),
                d("2-qadam. Kinetik energiya qismini ajratish",
                  r"\rho\frac{D}{Dt}\left(\tfrac{1}{2}v^2\right) = v_i(\sigma_{ij,j}+\rho b_i)",
                  "tmm-10 dagi harakat tenglamalarini $v_i$ ga ko'paytirib "
                  "olinadi."),
                d("3-qadam. Ichki energiya balansi",
                  r"\boxed{\;\rho\frac{Du}{Dt} = \sigma_{ij}D_{ij} - \nabla\cdot\mathbf{q} + \rho r\;}",
                  "Kinetik energiyani ayirib tashlaymiz. $\\sigma_{ij}D_{ij}$ — "
                  "kuchlanish quvvati (deformatsiya tezligi bilan "
                  "svertkasi)."),
                d("4-qadam. Entropiya tengsizligi",
                  r"\rho\frac{Ds}{Dt} \ge -\nabla\cdot\left(\frac{\mathbf{q}}{T}\right) + \frac{\rho r}{T}",
                  "Termodinamikaning ikkinchi qonuni. Tenglik faqat "
                  "qaytuvchan jarayonlarda."),
                d("5-qadam. Klauzius–Dyuhem tengsizligi",
                  r"\sigma_{ij}D_{ij} - \rho\left(\frac{D\psi}{Dt} + s\frac{DT}{Dt}\right) - "
                  r"\frac{\mathbf{q}\cdot\nabla T}{T} \ge 0",
                  "$\\psi = u - Ts$ — Gelmgols erkin energiyasi. Bu "
                  "tengsizlik konstitutiv tenglamalarga qat'iy cheklov "
                  "qo'yadi (tmm-13)."),
            ],
            formula_meaning=(
                "Energiya balansi mexanika va termodinamikani bog'laydi. "
                "Klauzius–Dyuhem tengsizligi esa material modellarini "
                "'filtrlaydi': har qanday o'ylab topilgan konstitutiv "
                "tenglama fizik jihatdan haqiqiy emas — u ikkinchi qonunni "
                "buzmasligi kerak. Masalan, bu tengsizlikdan elastik "
                "materialda $\\sigma_{ij} = \\rho\\partial\\psi/\\partial "
                "\\varepsilon_{ij}$ ekani kelib chiqadi va issiqlik "
                "o'tkazuvchanlik koeffitsienti musbat bo'lishi shart."
            ),
            equations=[
                eq(r"\rho\frac{Du}{Dt} = \sigma_{ij}D_{ij} - \nabla\cdot\mathbf{q} + \rho r",
                   "Ichki energiya balansi.", "Energiya balansi"),
                eq(r"\mathcal{D} = \sigma_{ij}D_{ij} - \rho\dot\psi - \rho s\dot T \ge 0",
                   "Dissipatsiya tengsizligi.", "Dissipatsiya"),
                eq(r"\mathbf{q} = -k\nabla T", "Furye issiqlik o'tkazuvchanlik qonuni.",
                   "Furye qonuni"),
            ],
            conditions=(
                "Klauzius–Dyuhem tengsizligi har qanday termodinamik "
                "jarayonda va har qanday material uchun bajarilishi shart. "
                "Elastik materialda dissipatsiya nolga teng (qaytuvchan "
                "jarayon), plastik va viskoelastik materiallarda musbat. "
                "Issiqlik o'tkazuvchanlik koeffitsienti $k > 0$ bo'lishi "
                "ham shu tengsizlikdan kelib chiqadi."
            ),
            worked_example=WorkedExample(
                statement=(
                    "Po'lat namuna bir o'qli cho'zilishda plastik "
                    "deformatsiyalanadi: $\\sigma = 400$ MPa, "
                    "$\\varepsilon^p = 0{,}15$. Taylor–Quinney koeffitsienti "
                    "$\\beta = 0{,}9$. (a) Plastik ish; (b) issiqlikka "
                    "aylangan qism; (c) adiabatik sharoitda temperatura "
                    "ortishi ($\\rho = 7850$ kg/m³, $c = 460$ J/(kg·K))."
                ),
                given=[r"\sigma = 400\ \text{MPa},\; \varepsilon^p = 0{,}15,\; \beta = 0{,}9",
                       r"\rho = 7850\ \text{kg/m}^3,\; c = 460\ \text{J/(kg·K)}"],
                steps=[
                    st(r"W_p = \int\sigma\,d\varepsilon^p \approx \sigma\varepsilon^p = "
                       r"400\cdot10^6\cdot0{,}15 = 60\ \text{MJ/m}^3",
                       "Plastik ish (birlik hajmga); o'zgarmas kuchlanish "
                       "farazi bilan."),
                    st(r"Q = \beta W_p = 0{,}9\cdot60 = 54\ \text{MJ/m}^3",
                       "Issiqlikka aylangan qism."),
                    st(r"E_{saqlangan} = (1-\beta)W_p = 6\ \text{MJ/m}^3",
                       "Kristall panjaradagi nuqsonlarda saqlangan energiya."),
                    st(r"\Delta T = \frac{Q}{\rho c} = \frac{54\cdot10^6}{7850\cdot460} = "
                       r"\frac{54\cdot10^6}{3{,}611\cdot10^6} = 15{,}0\ \text{K}",
                       "Adiabatik temperatura ortishi."),
                    st(r"\text{Dissipatsiya: } \mathcal{D} = \beta\sigma\dot\varepsilon^p > 0\ \checkmark",
                       "Klauzius–Dyuhem tengsizligi bajariladi — plastik "
                       "oqish qaytmas jarayon."),
                    st(r"\text{Tez deformatsiyada } (\dot\varepsilon > 10^3\ \text{1/s}) "
                       r"\text{ jarayon adiabatik}",
                       "Sekin deformatsiyada issiqlik tarqaladi va "
                       "$\\Delta T$ kichik bo'ladi."),
                ],
                answer=(
                    "$W_p = 60$ MJ/m³; $Q = 54$ MJ/m³; "
                    "$E_{saqlangan} = 6$ MJ/m³; $\\Delta T = 15{,}0$ K."
                ),
                engineering_note=(
                    "15 K temperatura ortishi materialning oquvchanlik "
                    "chegarasini pasaytiradi — bu 'adiabatik yumshash' "
                    "deb ataladi va yuqori tezlikli deformatsiyalarda "
                    "(zarba, o'q ta'siri, kesish) lokalizatsiyaga "
                    "(adiabatik siljish polosalari) olib keladi. Metall "
                    "kesishda esa temperatura 800 °C ga yetishi mumkin."
                ),
            ),
            computation=Computation(
                caption=(
                    "Energiya balansi: plastik ish, dissipatsiya va "
                    "temperatura ortishini hisoblang."
                ),
                code='''"""Energiya balansi va dissipatsiya."""
import numpy as np
from labkit import PARAMS, note, series, table, value

sigma_y = float(PARAMS.get("sigma_y", 400.0))*1e6    # oquvchanlik, Pa
eps_p = float(PARAMS.get("eps_p", 0.15))             # plastik deformatsiya
beta_tq = float(PARAMS.get("beta", 0.9))             # Taylor-Quinney
rho = float(PARAMS.get("rho", 7850.0))
c_p = float(PARAMS.get("c_p", 460.0))                # solishtirma issiqlik
E_mod = float(PARAMS.get("E", 200e9))
H_mod = float(PARAMS.get("H", 2e9))                  # mustahkamlanish moduli

# Plastik ish (chiziqli mustahkamlanish bilan)
sigma_end = sigma_y + H_mod*eps_p
W_p = (sigma_y + sigma_end)/2*eps_p
Q_heat = beta_tq*W_p
E_stored = (1-beta_tq)*W_p
dT = Q_heat/(rho*c_p)

value("Yakuniy kuchlanish", sigma_end/1e6, "MPa")
value("Plastik ish W_p", W_p/1e6, "MJ/m³")
value("Issiqlik Q", Q_heat/1e6, "MJ/m³")
value("Saqlangan energiya", E_stored/1e6, "MJ/m³")
value("Temperatura ortishi ΔT", dT, "K")

# Elastik energiya (taqqoslash uchun)
W_e = sigma_y**2/(2*E_mod)
value("Elastik energiya", W_e/1e6, "MJ/m³")
value("W_p / W_e nisbati", float(W_p/W_e), "—")
note("Plastik ish elastik energiyadan ordinar darajada katta — shuning uchun "
     "plastik deformatsiya energiya yutishning samarali mexanizmi.")

# Deformatsiya bo'ylab energiya to'planishi
ee = np.linspace(0, eps_p, 200)
sig = sigma_y + H_mod*ee
W_cum = np.array([np.trapezoid(sig[:i+1], ee[:i+1]) for i in range(len(ee))])
T_cum = beta_tq*W_cum/(rho*c_p)
series("Kuchlanish σ(ε_p)", (ee*100).tolist(), (sig/1e6).tolist(),
       xlabel="ε_p, %", ylabel="σ, MPa")
series("To'plangan ish W(ε_p)", (ee*100).tolist(), (W_cum/1e6).tolist(),
       xlabel="ε_p, %", ylabel="W, MJ/m³")
series("Temperatura ΔT(ε_p)", (ee*100).tolist(), T_cum.tolist(),
       xlabel="ε_p, %", ylabel="ΔT, K")

# Dissipatsiya tengsizligini tekshirish
eps_rate = 1.0
D_plastic = beta_tq*sigma_end*eps_rate
note(f"Dissipatsiya D = {D_plastic/1e6:.3f} MW/m³ > 0 ✓ — "
     "Klauzius-Dyuhem tengsizligi bajariladi (qaytmas jarayon).")
note("Elastik deformatsiyada D = 0 (qaytuvchan jarayon).")

# Adiabatik va izotermik rejimlar
k_therm = 45.0        # issiqlik o'tkazuvchanlik, W/(m·K)
L_char = 0.001        # xarakterli o'lcham, m
alpha_th = k_therm/(rho*c_p)
t_diff = L_char**2/alpha_th
rates = np.logspace(-3, 5, 100)
t_def = 1/rates
series("Deformatsiya vaqti", np.log10(rates).tolist(), np.log10(t_def).tolist(),
       xlabel="log₁₀(deformatsiya tezligi), 1/s", ylabel="log₁₀(vaqt), s")
note(f"Issiqlik diffuziyasi vaqti (L = 1 mm): {t_diff:.4f} s. "
     f"Deformatsiya tezligi > {1/t_diff:.1f} 1/s bo'lsa jarayon adiabatik.")

# Turli materiallar uchun temperatura ortishi
table("Materiallar uchun adiabatik qizish",
      ["Material", "ρ, kg/m³", "c, J/(kg·K)", "σ_y, MPa", "ΔT (ε_p=0,15), K"],
      [[nm, r, cc, sy, float(0.9*sy*1e6*0.15/(r*cc))]
       for nm, r, cc, sy in [("Po'lat", 7850, 460, 400),
                             ("Alyuminiy", 2700, 900, 150),
                             ("Titan", 4500, 520, 800),
                             ("Mis", 8960, 385, 200)]])

table("Energiya balansi tarkibi",
      ["Had", "Ma'no", "Ishora"],
      [["σ_ij D_ij", "Mexanik quvvat", "Kiruvchi"],
       ["∇·q", "Issiqlik oqimi divergensiyasi", "Chiquvchi"],
       ["ρr", "Ichki issiqlik manbai", "Kiruvchi"],
       ["ρ Du/Dt", "Ichki energiya o'zgarishi", "To'planuvchi"]])
''',
                parameters=[
                    p("sigma_y", "Oquvchanlik σ_y", 50.0, 2000.0, 400.0, 10.0, "MPa"),
                    p("eps_p", "Plastik deformatsiya", 0.01, 1.0, 0.15, 0.01, "—"),
                    p("beta", "Taylor–Quinney β", 0.5, 1.0, 0.9, 0.05, "—"),
                    p("rho", "Zichlik ρ", 1000.0, 20000.0, 7850.0, 100.0, "kg/m³"),
                    p("c_p", "Solishtirma issiqlik", 100.0, 1500.0, 460.0, 10.0, "J/(kg·K)"),
                    p("E", "Yung moduli", 1e10, 4e11, 200e9, 1e10, "Pa"),
                    p("H", "Mustahkamlanish moduli", 0.0, 2e10, 2e9, 1e8, "Pa"),
                ],
                expected_output="W_p ≈ 62,3 MJ/m³, Q ≈ 56 MJ/m³, ΔT ≈ 15,5 K",
            ),
            visualization=vis(
                "Energiya oqimlari diagrammasi",
                "React/SVG",
                "Sankey tipidagi diagramma: mexanik ish → elastik energiya "
                "(qaytariladi) + plastik ish → issiqlik (90 %) + saqlangan "
                "energiya (10 %). Yonida $\\sigma$–$\\varepsilon$ "
                "diagrammasi va uning ostidagi yuzalar.",
                "React/SVG: energiya oqimlarini kenglikka proporsional "
                "oqimlar bilan ko'rsatish (Sankey) — taqsimotni bir "
                "qarashda tushunarli qiladi. $\\sigma$–$\\varepsilon$ "
                "diagrammasidagi yuzalarni bo'yash esa energiyaning "
                "geometrik ma'nosini beradi.",
            ),
            interpretation=(
                "Plastik ish elastik energiyadan ~150 marta katta — bu "
                "plastik deformatsiyaning energiya yutish mexanizmi "
                "sifatidagi samaradorligini ko'rsatadi (avtomobil "
                "krandiyalari, himoya konstruksiyalari). Materiallar "
                "jadvali esa alyuminiy po'latdan kam qizishini ko'rsatadi "
                "— uning solishtirma issiqligi katta. Adiabatik/izotermik "
                "chegarasi deformatsiya tezligi bilan belgilanadi."
            ),
            common_mistakes=[
                "Plastik ishning hammasi issiqlikka aylanadi deb hisoblash "
                "(aslida ~90 %).",
                "Elastik va plastik energiyani chalkashtirish — birinchisi "
                "qaytariladi.",
                "Dissipatsiya tengsizligini tekshirmasdan material modeli "
                "taklif qilish.",
                "Adiabatik va izotermik rejimlarni farqlamaslik.",
            ],
            quiz=[
                q("Klauzius–Dyuhem tengsizligi nima uchun kerak?",
                  "U konstitutiv tenglamalarga cheklov qo'yadi: har qanday "
                  "material modeli termodinamikaning ikkinchi qonunini "
                  "buzmasligi kerak.", "konseptual"),
                q("Elastik deformatsiyada dissipatsiya qancha?",
                  "Nolga teng — bu qaytuvchan jarayon.", "konseptual"),
                q("$W_p = 40$ MJ/m³, $\\beta = 0{,}9$, $\\rho c = 3{,}6$ "
                  "MJ/(m³·K). $\\Delta T$?",
                  "$\\Delta T = 0{,}9\\cdot40/3{,}6 = 10$ K.", "hisob"),
                q("Nima uchun tez deformatsiyada jarayon adiabatik?",
                  "Issiqlik tarqalishga ulgurmaydi: deformatsiya vaqti "
                  "issiqlik diffuziyasi vaqtidan kichik.", "talqin"),
                q("Kodda Taylor–Quinney koeffitsienti nimani ifodalaydi?",
                  "Plastik ishning issiqlikka aylanadigan ulushini "
                  "(odatda 0,85–0,95); qolgani kristall nuqsonlarida "
                  "saqlanadi.", "kod"),
            ],
            bridge_to_next=(
                "Uchala balans qonuni yozildi, lekin ular materialning "
                "xossalarini o'z ichiga olmaydi. Keyingi modulda "
                "konstitutiv tenglamalarga — material modellariga o'tamiz."
            ),
            research_extension=(
                "Adiabatik siljish polosalarini modellashtiring: yuqori "
                "tezlikli deformatsiyada qizish materialni yumshatadi, bu "
                "deformatsiyani lokalizatsiya qiladi va yanada ko'proq "
                "qizishga olib keladi (musbat teskari aloqa). Sodda 1D "
                "model quring va beqarorlik sharti "
                "$\\partial\\sigma/\\partial\\varepsilon \\le 0$ ni toping."
            ),
        ),
    ),
]
