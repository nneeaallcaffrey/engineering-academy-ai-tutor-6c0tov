"""TMM / 5-modul: Suyuqlik va gaz mexanikasi (tmm-25 … tmm-30)."""

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
M = "tmm-m5"


def _lesson(problem, concepts, derivation, meaning, equations, conditions,
            worked, computation, visual, interp, mistakes, quiz, bridge, research,
            manim_ref=None):
    return Lesson(
        physical_problem=problem, concepts=concepts, derivation=derivation,
        formula_meaning=meaning, equations=equations, conditions=conditions,
        worked_example=worked, computation=computation, visualization=visual,
        interpretation=interp, common_mistakes=mistakes, quiz=quiz,
        bridge_to_next=bridge, research_extension=research, manim=manim_ref,
    )


TOPICS = [
    # ------------------------------------------------------------------ tmm-25
    Topic(
        id="tmm-25",
        subject_id=S, module_id=M, order=25,
        title="Gidrostatika: bosim maydoni, Paskal qonuni va suzish barqarorligi",
        description=(
            "Tinch turgan suyuqlikda kuchlanish tenzorining izotropligi, "
            "gidrostatik bosim taqsimoti, devorlarga ta'sir kuchi hamda "
            "Arximed qonuni va suzish barqarorligi (metasentr)."
        ),
        learning_objective=(
            "Koshi harakat tenglamasidan gidrostatika tenglamasini keltirib "
            "chiqarish, tekis va egri devorlarga ta'sir kuchini integrallash "
            "hamda suzuvchi jismning barqarorligini metasentrik balandlik "
            "orqali baholash."
        ),
        prerequisites=["tmm-10", "tmm-08"],
        mathematical_core=(
            "$\\nabla p = \\rho\\mathbf{g}$, yuza integrali "
            "$F = \\int_A p\\,dA$, kuch qo'yilish markazi "
            "$y_c = I_{xx}/(y_G A)$, metasentrik balandlik $GM = I/V - BG$."
        ),
        engineering_application=(
            "To'g'on va shlyuz devorlari, suv ombori, kema va suzuvchi "
            "platformalar, manometr va gidravlik press, rezervuar loyihasi."
        ),
        computational_component=(
            "Bosim epyurasini hisoblash, devorga ta'sir kuchi va uning "
            "qo'yilish nuqtasini sonli integrallash, ag'darish momenti tahlili."
        ),
        visualization_component=(
            "Uchburchak bosim epyurasi, natijaviy kuch vektori va uning "
            "qo'yilish nuqtasi; suzuvchi jismning og'ish diagrammasi."
        ),
        research_extension=(
            "Tezlanuvchi idishdagi suyuqlik (rigid body motion) masalasini "
            "o'rganing: bir tekis tezlanish va aylanishda erkin sirt shakli "
            "qanday o'zgaradi?"
        ),
        difficulty="asosiy",
        previous_link=(
            "tmm-24 da qattiq jism mexanikasi yakunlandi. Endi bir xil balans "
            "qonunlarini (tmm-09, tmm-10) suyuqlikka qo'llaymiz — faqat "
            "konstitutiv tenglama o'zgaradi. Eng sodda hol — tinch turgan "
            "suyuqlik, ya'ni gidrostatika."
        ),
        next_topic="tmm-26",
        estimated_minutes=85,
        tags=["gidrostatika", "bosim", "Arximed", "suyuqlik"],
        lesson=_lesson(
            problem=(
                "Suv omborining to'g'on devori 12 m chuqurlikdagi suvni "
                "ushlab turadi. Devorga qancha kuch ta'sir qiladi va u qaysi "
                "balandlikda qo'yilgan deb hisoblash kerak? Ikkinchi savol "
                "birinchisidan ham muhim: agar kuchni noto'g'ri balandlikka "
                "qo'ysak, ag'darish momenti xato hisoblanadi va to'g'on "
                "asosidan ag'darilib ketishi mumkin. Javob uchun bosimning "
                "chuqurlik bo'yicha taqsimotini bilish kerak."
            ),
            concepts=[
                c("Gidrostatik bosim (hydrostatic pressure)",
                  "Tinch turgan suyuqlikda kuchlanish tenzori izotrop: "
                  "$\\sigma_{ij} = -p\\delta_{ij}$. Urinma kuchlanish yo'q, "
                  "chunki $\\mu\\dot{\\gamma} = 0$."),
                c("Paskal qonuni (Pascal's law)",
                  "Berilgan nuqtada bosim yo'nalishga bog'liq emas; yopiq "
                  "idishda bosim o'zgarishi butun hajmga bir xil uzatiladi — "
                  "gidravlik pressning asosi."),
                c("Bosim markazi (centre of pressure)",
                  "Taqsimlangan bosimning natijaviy kuchi qo'yiladigan nuqta. "
                  "U og'irlik markazidan har doim pastroqda yotadi."),
                c("Arximed qonuni (Archimedes' principle)",
                  "Suzuvchi jismga ta'sir qiluvchi ko'taruvchi kuch siqib "
                  "chiqarilgan suyuqlik og'irligiga teng: "
                  "$F_A = \\rho g V_{\\text{botgan}}$."),
                c("Metasentr (metacentre)",
                  "Kema og'ganda ko'taruvchi kuch chizig'i simmetriya o'qini "
                  "kesib o'tadigan nuqta. $GM > 0$ bo'lsa suzish barqaror."),
                c("Manometrik va absolyut bosim",
                  "Manometrik bosim atmosfera bosimidan sanaladi; "
                  "$p_{\\text{abs}} = p_{\\text{atm}} + p_{\\text{man}}$. "
                  "Kuch hisobida odatda manometrik bosim ishlatiladi, chunki "
                  "atmosfera devorning ikkala tomoniga ta'sir qiladi."),
            ],
            derivation=[
                d("1. Koshi tenglamasidan boshlash",
                  r"\rho\frac{D\mathbf{v}}{Dt} = \nabla\cdot\boldsymbol{\sigma} "
                  r"+ \rho\mathbf{b}",
                  "tmm-10 dagi umumiy harakat tenglamasi. Gidrostatikada "
                  "$\\mathbf{v} = 0$, demak chap tomon nolga teng."),
                d("2. Tinch suyuqlikda kuchlanish tenzori",
                  r"\sigma_{ij} = -p\,\delta_{ij}",
                  "Suyuqlik ta'rifi bo'yicha ixtiyoriy kichik urinma "
                  "kuchlanishga qarshilik ko'rsatolmaydi — u oqib ketadi. "
                  "Tinch holatda urinma kuchlanish nolga teng bo'lishi shart, "
                  "demak tenzor sferik. Minus ishora — bosim siquvchi."),
                d("3. Divergensiyani hisoblash",
                  r"(\nabla\cdot\boldsymbol{\sigma})_i = "
                  r"\frac{\partial\sigma_{ij}}{\partial x_j} "
                  r"= -\frac{\partial p}{\partial x_j}\delta_{ij} "
                  r"= -\frac{\partial p}{\partial x_i}",
                  "Kronekker deltasi indeksni 'yutadi'. Natijada tenzor "
                  "divergensiyasi oddiy gradiyentga aylanadi."),
                d("4. Gidrostatika asosiy tenglamasi",
                  r"\nabla p = \rho\,\mathbf{b} = \rho\,\mathbf{g}",
                  "Bosim gradiyenti hajmiy kuch bilan muvozanatlashadi. "
                  "Vektor tenglama — uchta skalyar tenglamaga teng."),
                d("5. Vertikal o'q bo'yicha integrallash",
                  r"\frac{\partial p}{\partial x} = \frac{\partial p}{\partial y} = 0, "
                  r"\quad \frac{dp}{dz} = -\rho g \;\Longrightarrow\; "
                  r"p = p_0 + \rho g h",
                  "$z$ yuqoriga yo'nalgan, $h = -z$ — chuqurlik. Gorizontal "
                  "hosilalar nol: **bir xil chuqurlikda bosim bir xil** — "
                  "bu ulangan idishlar qonuni."),
                d("6. Tekis devorga natijaviy kuch",
                  r"F = \int_A p\,dA = \rho g\int_A y\sin\alpha\,dA "
                  r"= \rho g\,y_G\sin\alpha\,A = p_G A",
                  "$y_G$ — og'irlik markazining qiya o'q bo'yicha koordinatasi. "
                  "Natija sodda: kuch og'irlik markazidagi bosim ko'paytiriladi "
                  "yuzaga."),
                d("7. Bosim markazi (kuch qo'yilish nuqtasi)",
                  r"y_{cp} = \frac{\int_A y\,p\,dA}{\int_A p\,dA} "
                  r"= y_G + \frac{I_{xx,G}}{y_G A}",
                  "Moment tengligi shartidan. $I_{xx,G}$ — og'irlik markaziga "
                  "nisbatan yuza inersiya momenti (mq-08 da o'rganilgan). "
                  "Qo'shimcha had har doim musbat — bosim markazi pastroqda."),
                d("8. Suzish barqarorligi: metasentrik balandlik",
                  r"GM = \frac{I_{\text{wl}}}{V} - BG",
                  "$I_{\\text{wl}}$ — suv chizig'i yuzasining inersiya momenti, "
                  "$V$ — botgan hajm, $BG$ — ko'taruvchi kuch markazidan "
                  "og'irlik markazigacha masofa. $GM > 0$ — og'ish momenti "
                  "tiklovchi, ya'ni barqaror."),
            ],
            meaning=(
                "$p = p_0 + \\rho g h$ formulasining hayratlanarli jihati — "
                "unda idish shakli yo'q. 1 sm diametrli naycha ham, ulkan ko'l "
                "ham bir xil chuqurlikda bir xil bosim beradi. Bu 'gidrostatik "
                "paradoks' aslida paradoks emas: devorlar qiya bo'lsa, ularning "
                "reaksiyasi vertikal tashkil etuvchiga ega bo'ladi va balansni "
                "ta'minlaydi. $y_{cp} = y_G + I_{xx,G}/(y_G A)$ formulasi esa "
                "muhandislik uchun hal qiluvchi: bosim chiziqli o'sgani uchun "
                "uning 'og'irlik markazi' yuzaning og'irlik markazidan pastda "
                "yotadi. Vertikal to'rtburchak devor uchun "
                "$I_{xx,G} = bh^3/12$, $y_G = h/2$, $A = bh$ bo'lib, "
                "$y_{cp} = h/2 + h/6 = 2h/3$ — kuch har doim yuqoridan uchdan "
                "ikki chuqurlikda qo'yiladi. Metasentrik balandlikdagi "
                "$I_{\\text{wl}}/V$ hadi kemaning kengligiga kubik bog'liq: "
                "shuning uchun keng, yassi kema (barja) barqaror, tor va "
                "chuqur kema esa ag'darilishga moyil."
            ),
            equations=[
                eq(r"\nabla p = \rho\mathbf{g}",
                   "Gidrostatikaning asosiy differensial tenglamasi.",
                   "Gidrostatika tenglamasi"),
                eq(r"p = p_0 + \rho g h",
                   "Bir jinsli suyuqlikda bosimning chuqurlik bo'yicha taqsimoti.",
                   "Gidrostatik bosim"),
                eq(r"F = p_G A, \qquad y_{cp} = y_G + \frac{I_{xx,G}}{y_G A}",
                   "Tekis devorga natijaviy kuch va uning qo'yilish nuqtasi.",
                   "Devorga kuch"),
                eq(r"GM = \frac{I_{\text{wl}}}{V} - BG",
                   "Metasentrik balandlik — suzish barqarorligi mezoni.",
                   "Metasentrik balandlik"),
            ],
            conditions=(
                "**Erkin sirtda:** $p = p_{\\text{atm}}$ (yoki manometrik "
                "shkalada $p = 0$). Bu gidrostatika tenglamasini integrallash "
                "uchun zarur bo'lgan yagona shart.\n\n"
                "**Ikki suyuqlik chegarasida:** bosim uzluksiz, "
                "$p_1 = p_2$ — manometr hisobining asosi.\n\n"
                "**Qattiq devorda:** suyuqlik faqat normal kuchlanish uzatadi, "
                "$\\mathbf{t} = -p\\,\\mathbf{n}$.\n\n"
                "**Qo'llanish sharti:** $\\mathbf{v} = 0$ yoki suyuqlik qattiq "
                "jism kabi harakatlanadi (rigid body motion); bu holda "
                "$\\nabla p = \\rho(\\mathbf{g} - \\mathbf{a})$ va tezlanish "
                "hisobga olinadi."
            ),
            worked=WorkedExample(
                statement=(
                    "To'g'onning vertikal devori 12 m chuqurlikdagi suvni "
                    "ushlaydi, devor kengligi 1 m (birlik kenglikka hisob). "
                    "$\\rho = 1000$ kg/m³. (a) Devorga ta'sir qiluvchi "
                    "natijaviy kuchni toping. (b) Bosim markazini aniqlang. "
                    "(c) Asosga nisbatan ag'darish momentini hisoblang."
                ),
                given=[
                    r"h = 12\ \text{m},\ b = 1\ \text{m}",
                    r"\rho = 1000\ \text{kg/m}^3,\ g = 9{,}81\ \text{m/s}^2",
                ],
                steps=[
                    st(r"p_{\max} = \rho g h = 1000 \cdot 9{,}81 \cdot 12 "
                       r"= 117{,}7\ \text{kPa}",
                       "Tubdagi maksimal manometrik bosim. Epyura uchburchak: "
                       "yuqorida nol, pastda maksimal."),
                    st(r"y_G = \frac{h}{2} = 6\ \text{m}, \qquad "
                       r"p_G = \rho g y_G = 58{,}86\ \text{kPa}",
                       "Og'irlik markazi o'rtada, undagi bosim maksimalning yarmi."),
                    st(r"F = p_G A = 58\,860 \cdot (12 \cdot 1) = 706{,}3\ \text{kN}",
                       "Birlik kenglikka 706 kN — taxminan 72 tonna kuch."),
                    st(r"I_{xx,G} = \frac{bh^3}{12} = \frac{1 \cdot 12^3}{12} "
                       r"= 144\ \text{m}^4",
                       "Yuza inersiya momenti (mq-08)."),
                    st(r"y_{cp} = y_G + \frac{I_{xx,G}}{y_G A} = 6 + "
                       r"\frac{144}{6 \cdot 12} = 6 + 2 = 8\ \text{m}",
                       "Sirtdan 8 m, ya'ni $2h/3$ — kutilgan natija. Kuch "
                       "og'irlik markazidan 2 m pastda qo'yiladi."),
                    st(r"a = h - y_{cp} = 12 - 8 = 4\ \text{m}",
                       "Kuchning asosdan balandligi — ag'darish momenti uchun yelka."),
                    st(r"M_{\text{ag'darish}} = F \cdot a = 706{,}3 \cdot 4 "
                       r"= 2825\ \text{kN·m/m}",
                       "Agar kuchni xato ravishda o'rtaga (6 m) qo'ysak, "
                       "moment $706{,}3 \\cdot 6 = 4238$ kN·m bo'lardi — "
                       "50 % ortiqcha, ya'ni xato xavfsiz tomonga emas."),
                ],
                answer=(
                    "$F = 706{,}3$ kN/m; bosim markazi sirtdan 8 m "
                    "(= $2h/3$) chuqurlikda; asosga nisbatan ag'darish "
                    "momenti 2825 kN·m/m."
                ),
                engineering_note=(
                    "Amalda to'g'on hisobiga yana ikkita muhim yuk qo'shiladi: "
                    "(1) **ko'tarish bosimi** (uplift) — asos ostidan sizib "
                    "kiruvchi suv to'g'onni yuqoriga itaradi va ishqalanish "
                    "qarshiligini kamaytiradi; (2) **loyqa bosimi** — vaqt "
                    "o'tishi bilan to'planadigan cho'kindi suvdan zichroq. "
                    "Ikkalasi ham ag'darish va sirpanish tekshiruvida hal "
                    "qiluvchi bo'lishi mumkin."
                ),
            ),
            computation=Computation(
                caption=(
                    "Bosim epyurasi, devorga ta'sir kuchi va bosim markazini "
                    "sonli integrallash; suzish barqarorligini tekshirish."
                ),
                code='''"""Gidrostatika: bosim epyurasi, devor kuchi va suzish barqarorligi."""
import numpy as np
from labkit import PARAMS, note, series, table, value

h = float(PARAMS.get("h", 12.0))         # suv chuqurligi, m
b = float(PARAMS.get("b", 1.0))          # devor kengligi, m
rho = float(PARAMS.get("rho", 1000.0))   # kg/m^3
alpha = float(PARAMS.get("alpha", 90.0)) # devor qiyaligi, deg
g = 9.81

# --- Bosim epyurasi ---
z = np.linspace(0.0, h, 300)             # sirtdan chuqurlik
pres = rho*g*z                           # Pa
series("Bosim epyurasi p(z)", (pres/1000).tolist(), (-z).tolist(),
       xlabel="Manometrik bosim p, kPa", ylabel="Chuqurlik (sirtdan), m")
value("Maksimal bosim (tubda)", float(pres[-1])/1000, "kPa")
value("O'rtacha bosim", float(np.mean(pres))/1000, "kPa")

# --- Analitik formula ---
a_rad = np.radians(alpha)
L = h/np.sin(a_rad)                      # devorning qiya uzunligi
A = L*b
yG = L/2                                 # qiya o'q bo'ylab og'irlik markazi
pG = rho*g*(yG*np.sin(a_rad))
F_analytic = pG*A
Ixx = b*L**3/12
ycp = yG + Ixx/(yG*A)

value("Devor qiya uzunligi L", L, "m")
value("Natijaviy kuch F (analitik)", F_analytic/1000, "kN")
value("Bosim markazi y_cp (qiya o'q bo'yicha)", ycp, "m")
value("Bosim markazi chuqurligi", ycp*np.sin(a_rad), "m")
value("y_cp / L", ycp/L, "—")

# --- Sonli integrallash bilan tekshirish ---
s = np.linspace(0.0, L, 4001)            # qiya o'q bo'ylab
p_s = rho*g*s*np.sin(a_rad)
trapz = np.trapezoid if hasattr(np, "trapezoid") else np.trapz
F_num = float(trapz(p_s, s))*b
M_num = float(trapz(p_s*s, s))*b
ycp_num = M_num/F_num
note(f"Analitik F = {F_analytic/1000:.2f} kN, sonli F = {F_num/1000:.2f} kN; "
     f"nisbiy farq {abs(F_num-F_analytic)/F_analytic*100:.4f} % — integrallash to'g'ri.")
note(f"Analitik y_cp = {ycp:.4f} m, sonli y_cp = {ycp_num:.4f} m.")

# --- Ag'darish momenti ---
arm = L - ycp
value("Kuch yelkasi (asosdan)", arm, "m")
value("Ag'darish momenti", F_analytic*arm/1000, "kN*m")
value("Xato hisob (kuch o'rtada) momenti", F_analytic*(L - yG)/1000, "kN*m")
value("Xato ulushi", 100*((L-yG)/arm - 1), "%")

table("Turli devor shakllari uchun bosim markazi",
      ["Shakl", "y_cp / h", "Izoh"],
      [["Vertikal to'rtburchak", round(2/3, 4), "Klassik natija 2h/3"],
       ["Uchburchak (uchi yuqorida)", round(3/4, 4), "Yuza pastda to'plangan"],
       ["Uchburchak (uchi pastda)", round(1/2, 4), "Yuza yuqorida to'plangan"],
       ["Doira (markazi h/2 da)", round(0.5 + (1/16)/(0.5*np.pi/4)*0, 4),
        "y_G + I/(y_G A), I = pi R^4/4"]])

# --- Arximed qonuni va suzish barqarorligi ---
Lb = float(PARAMS.get("Lb", 20.0))       # kema uzunligi, m
Bb = float(PARAMS.get("Bb", 6.0))        # kema kengligi, m
T = float(PARAMS.get("T", 1.5))          # cho'kish (draft), m
KG = float(PARAMS.get("KG", 2.5))        # og'irlik markazi tubdan, m

V = Lb*Bb*T
disp = rho*V
KB = T/2                                  # to'rtburchak kesim uchun
I_wl = Lb*Bb**3/12
BM = I_wl/V
GM = KB + BM - KG
value("Botgan hajm V", V, "m3")
value("Suv sig'imi (displacement)", disp/1000, "t")
value("BM = I_wl/V", BM, "m")
value("Metasentrik balandlik GM", GM, "m")
if GM > 0:
    note(f"GM = {GM:.3f} m > 0 — suzish BARQAROR. "
         f"GM juda katta bo'lsa (> B/10 = {Bb/10:.2f} m) kema tez va "
         f"noqulay chayqaladi.")
else:
    note(f"GM = {GM:.3f} m <= 0 — suzish BEQAROR, kema ag'dariladi.")

# Tiklovchi moment egri chizig'i (kichik burchaklar uchun)
theta = np.linspace(0, 20, 100)
GZ = GM*np.sin(np.radians(theta))
series("Tiklovchi yelka GZ(theta)", theta.tolist(), GZ.tolist(),
       xlabel="Og'ish burchagi theta, deg", ylabel="GZ, m")
value("Tiklovchi moment 10 deg da", disp*g*GM*np.sin(np.radians(10))/1000, "kN*m")
''',
                parameters=[
                    p("h", "Suv chuqurligi h", 1.0, 60.0, 12.0, 0.5, "m"),
                    p("b", "Devor kengligi b", 0.5, 20.0, 1.0, 0.5, "m"),
                    p("rho", "Suyuqlik zichligi ρ", 600.0, 1400.0, 1000.0, 10.0, "kg/m³"),
                    p("alpha", "Devor qiyaligi α", 20.0, 90.0, 90.0, 5.0, "deg"),
                    p("Lb", "Kema uzunligi", 5.0, 100.0, 20.0, 1.0, "m"),
                    p("Bb", "Kema kengligi", 1.0, 30.0, 6.0, 0.5, "m"),
                    p("T", "Cho'kish T", 0.3, 10.0, 1.5, 0.1, "m"),
                    p("KG", "Og'irlik markazi KG", 0.5, 15.0, 2.5, 0.1, "m"),
                ],
                expected_output=(
                    "F = 706,3 kN, y_cp = 8,0 m (= 2h/3), ag'darish momenti "
                    "2825 kN·m; xato hisob 50 % ortiqcha. Kema uchun "
                    "GM = 1,25 m > 0 — barqaror."
                ),
            ),
            visual=vis(
                kind="Bosim epyurasi va suzish barqarorligi",
                tool="React/SVG",
                description=(
                    "Uchburchak bosim epyurasi, natijaviy kuch vektori, "
                    "bosim markazi hamda og'gan kemadagi tiklovchi juftlik."
                ),
                how_to_draw=(
                    "React/SVG: devor vertikal to'g'ri chiziq, chapida suv "
                    "sathi gorizontal chiziq bilan (to'lqinli `<path>` bilan "
                    "bezatiladi). Epyura — devordan chapga qarab o'sib boruvchi "
                    "uchburchak `<polygon>`, ichida har 1/6 chuqurlikda "
                    "gorizontal strelkalar (uzunligi $p(z)$ ga mutanosib). "
                    "Natijaviy kuch — qalin strelka, aniq $2h/3$ chuqurlikda; "
                    "yonida $F$ va $y_{cp}$ yorliqlari. Suzish panelida kema "
                    "kesimi $\\theta$ burchakka burilgan `<g transform=\"rotate\">` "
                    "ichida; $G$ (og'irlik markazi) va $B$ (ko'taruvchi kuch "
                    "markazi) nuqtalari, ulardan yuqoriga va pastga vertikal "
                    "vektorlar, ular orasidagi $GZ$ yelkasi o'lchov chizig'i "
                    "bilan belgilanadi. $\\theta$ slayder bilan boshqariladi."
                ),
            ),
            interp=(
                "Sonli integrallash analitik formulani 0,001 % dan yaxshi "
                "aniqlikda tasdiqlaydi — bu kodning to'g'riligini isbotlaydi "
                "va keyingi, analitik yechimi bo'lmagan masalalarga ishonch "
                "beradi. Eng muhim amaliy xulosa ag'darish momenti qatorida: "
                "kuchni og'irlik markaziga qo'yish 50 % xato beradi, lekin "
                "bu **xavfsizlik zaxirasini kamaytiradigan** emas, balki "
                "oshiradigan tomonga — shuning uchun ko'pincha sezilmay "
                "qoladi va konstruksiyani ortiqcha qimmatlashtiradi. "
                "Metasentrik balandlik hisobida $BM = I_{\\text{wl}}/V$ "
                "kenglikka **kubik** bog'liq: kemani 10 % kengaytirish "
                "$GM$ ni 33 % oshiradi. Lekin bu bepul emas — juda katta "
                "$GM$ chayqalish davrini qisqartiradi va yo'lovchilar uchun "
                "noqulay, yuk uchun esa xavfli bo'ladi. Kema loyihasi aynan "
                "shu ikki talab orasidagi murosadan iborat."
            ),
            mistakes=[
                "Natijaviy kuchni yuzaning og'irlik markaziga qo'yish. "
                "Bosim chiziqli o'sgani uchun kuch markazi pastroqda: "
                "vertikal to'rtburchak uchun $2h/3$, og'irlik markazi esa $h/2$.",
                "Bosimni idish shakliga yoki suyuqlik hajmiga bog'liq deb "
                "hisoblash. $p = \\rho g h$ da faqat chuqurlik bor — "
                "gidrostatik paradoks.",
                "Absolyut va manometrik bosimni aralashtirish. Devorga kuch "
                "hisoblashda manometrik bosim ishlatiladi, chunki atmosfera "
                "ikkala tomondan bir xil ta'sir qiladi va o'zaro qisqaradi.",
                "Suzish barqarorligini $G$ va $B$ nuqtalarining o'zaro "
                "joylashuvi bilan baholash. $G$ nuqta $B$ dan yuqorida "
                "bo'lishi mumkin va suzish baribir barqaror bo'ladi — muhimi "
                "$GM = KB + BM - KG > 0$.",
            ],
            quiz=[
                q("Nima uchun tinch turgan suyuqlikda urinma kuchlanish yo'q?",
                  "Suyuqlik ta'rifi bo'yicha ixtiyoriy kichik urinma "
                  "kuchlanish ostida uzluksiz deformatsiyalanadi (oqadi). "
                  "Muvozanat faqat $\\tau = 0$ da mumkin.", "konseptual"),
                q("Vertikal to'rtburchak devorda bosim markazi qayerda?",
                  "Sirtdan $2h/3$ chuqurlikda, ya'ni tubdan $h/3$ "
                  "balandlikda — uchburchak epyuraning og'irlik markazi.",
                  "hisob"),
                q("15 m chuqurlikda manometrik bosim qancha?",
                  "$p = 1000 \\cdot 9{,}81 \\cdot 15 = 147{,}2$ kPa "
                  "($\\approx 1{,}45$ atm).", "hisob"),
                q("Gidrostatik paradoks nima va u qanday tushuntiriladi?",
                  "Turli shakldagi idishlarda bir xil chuqurlikda tubga "
                  "bosim bir xil, suyuqlik og'irligi esa har xil. Sabab: "
                  "qiya devorlar reaksiyasining vertikal tashkil etuvchisi "
                  "farqni qoplaydi.", "talqin"),
                q("$GM > 0$ sharti nimani kafolatlaydi?",
                  "Og'ish paytida yuzaga keladigan moment tiklovchi bo'lishini, "
                  "ya'ni suzish barqarorligini. $GM < 0$ da moment og'ishni "
                  "kuchaytiradi va kema ag'dariladi.", "konseptual"),
                q("Kodda sonli va analitik kuch nima uchun taqqoslanadi?",
                  "Bu — verifikatsiya: aniq yechimi ma'lum masalada sonli "
                  "usulni tekshirish. Farq $10^{-4}$ % darajasida bo'lsa, "
                  "integrallash sxemasi to'g'ri ishlaydi degan ishonch paydo bo'ladi.",
                  "kod"),
            ],
            bridge=(
                "Tinch suyuqlikda faqat bosim bor edi. Endi suyuqlikni "
                "harakatga keltiramiz: inersiya hadi paydo bo'ladi va "
                "Koshi tenglamasi Eyler tenglamalariga aylanadi. Ular "
                "Bernulli integrali orqali muhandislikdagi eng ko'p "
                "ishlatiladigan formulaga olib keladi."
            ),
            research=(
                "Tezlanuvchi idishdagi suyuqlikni (rigid body motion) "
                "o'rganing: $\\nabla p = \\rho(\\mathbf{g} - \\mathbf{a})$. "
                "Gorizontal tezlanishda erkin sirt qiya tekislikka, doimiy "
                "burchak tezlik bilan aylanishda esa paraboloidga aylanishini "
                "isbotlang. Aylanuvchi idishdagi sirt tenglamasi "
                "$z = \\omega^2 r^2/(2g)$ ni chiqaring va uni teleskop "
                "oynalarini quyishda (spin casting) qanday ishlatilishini "
                "tahlil qiling."
            ),
        ),
    ),

    # ------------------------------------------------------------------ tmm-26
    Topic(
        id="tmm-26",
        subject_id=S, module_id=M, order=26,
        title="Ideal suyuqlik dinamikasi: Eyler tenglamalari va Bernulli integrali",
        description=(
            "Yopishqoqligi e'tiborsiz suyuqlik uchun harakat tenglamalari, "
            "oqim chizig'i bo'ylab Bernulli integrali, uning energetik "
            "talqini va amaliy qo'llanishlari (Ventura, Pito, Torrichelli)."
        ),
        learning_objective=(
            "Koshi tenglamasidan Eyler tenglamalarini olish, ularni oqim "
            "chizig'i bo'ylab integrallab Bernulli tenglamasini chiqarish "
            "va uni uzluksizlik tenglamasi bilan birga oqim masalalarini "
            "yechishda qo'llash."
        ),
        prerequisites=["tmm-25", "tmm-09"],
        mathematical_core=(
            "Moddiy hosila $D\\mathbf{v}/Dt = \\partial_t\\mathbf{v} + "
            "(\\mathbf{v}\\cdot\\nabla)\\mathbf{v}$, Lamb–Gromeka shakli, "
            "chiziq bo'ylab integrallash, potensial oqim va "
            "$\\nabla^2\\varphi = 0$."
        ),
        engineering_application=(
            "Ventura rasxodomeri, Pito naychasi bilan tezlik o'lchash, "
            "sifon va rezervuardan oqib chiqish, nasos va turbina "
            "balansi, qanot ko'taruvchi kuchining sodda tushuntirishi."
        ),
        computational_component=(
            "Ventura quvurida bosim va tezlik taqsimotini hisoblash, "
            "Torrichelli formulasi bo'yicha rezervuar bo'shalish vaqtini "
            "sonli integrallash, kavitatsiya xavfini tekshirish."
        ),
        visualization_component=(
            "Oqim chiziqlari va Ventura kesimidagi tezlik/bosim grafiklari; "
            "energiya chizig'i (EGL) va pyezometrik chiziq (HGL)."
        ),
        research_extension=(
            "Bernulli tenglamasining nostatsionar umumlashmasini "
            "($\\partial\\varphi/\\partial t$ hadi bilan) o'rganing va uni "
            "suv bolg'asi (water hammer) hodisasiga qo'llang."
        ),
        difficulty="murakkab",
        previous_link=(
            "tmm-25 da $\\mathbf{v} = 0$ edi va faqat bosim bilan og'irlik "
            "muvozanatlashardi. Endi inersiya hadini qaytaramiz: shu bitta "
            "qadam gidrostatikani gidrodinamikaga aylantiradi."
        ),
        next_topic="tmm-27",
        estimated_minutes=95,
        tags=["Eyler", "Bernulli", "oqim", "Ventura"],
        lesson=_lesson(
            problem=(
                "Quvurdagi suv sarfini o'lchash kerak, lekin oqimni to'xtatib "
                "hisoblagich o'rnatish mumkin emas. Yechim: quvurga torayuvchi "
                "qism (Ventura) kiritiladi va ikki kesimda bosim o'lchanadi. "
                "Tor kesimda bosim pasayadi — nega? Va bosim farqidan sarfni "
                "qanday hisoblaymiz? Eng muhimi: torayish juda kuchli bo'lsa, "
                "bosim suvning to'yingan bug' bosimidan pastga tushib, "
                "kavitatsiya boshlanadi va quvur yemiriladi. Bu chegarani "
                "qanday topamiz?"
            ),
            concepts=[
                c("Ideal suyuqlik (ideal/inviscid fluid)",
                  "Yopishqoqligi nolga teng deb olinadigan model: "
                  "$\\sigma_{ij} = -p\\delta_{ij}$ harakatda ham. Devordan "
                  "uzoqda, oqim tez va yo'l qisqa bo'lganda yaxshi ishlaydi."),
                c("Eyler tenglamalari (Euler equations)",
                  "Ideal suyuqlikning harakat tenglamalari: "
                  "$\\rho\\,D\\mathbf{v}/Dt = -\\nabla p + \\rho\\mathbf{g}$."),
                c("Oqim chizig'i (streamline)",
                  "Har bir nuqtada tezlik vektoriga urinma bo'lgan chiziq. "
                  "Statsionar oqimda zarra traektoriyasi bilan ustma-ust tushadi."),
                c("Bernulli integrali",
                  "$p + \\frac{1}{2}\\rho v^2 + \\rho gz = \\text{const}$ — "
                  "oqim chizig'i bo'ylab mexanik energiyaning saqlanishi."),
                c("To'xtash bosimi (stagnation pressure)",
                  "$p_0 = p + \\frac{1}{2}\\rho v^2$ — oqim to'liq to'xtaganda "
                  "hosil bo'ladigan bosim; Pito naychasi shuni o'lchaydi."),
                c("Kavitatsiya (cavitation)",
                  "Bosim to'yingan bug' bosimidan pastga tushganda suyuqlik "
                  "ichida bug' pufakchalari hosil bo'lishi; ular yemirilganda "
                  "metall sirtni yemiradi."),
            ],
            derivation=[
                d("1. Koshi tenglamasi ideal suyuqlik uchun",
                  r"\rho\frac{D\mathbf{v}}{Dt} = -\nabla p + \rho\mathbf{g}",
                  "tmm-10 dagi umumiy tenglamaga $\\sigma_{ij} = -p\\delta_{ij}$ "
                  "ni qo'yamiz. Bu Eyler tenglamalari — 1757-yil."),
                d("2. Moddiy hosilani yoyish",
                  r"\frac{D\mathbf{v}}{Dt} = \frac{\partial\mathbf{v}}{\partial t} "
                  r"+ (\mathbf{v}\cdot\nabla)\mathbf{v}",
                  "tmm-03 dagi Eyler tavsifi. Ikkinchi had — konvektiv "
                  "tezlanish, u nochiziqli va gidrodinamikaning butun "
                  "murakkabligi manbai."),
                d("3. Lamb–Gromeka almashtirishi",
                  r"(\mathbf{v}\cdot\nabla)\mathbf{v} = "
                  r"\nabla\Big(\frac{v^2}{2}\Big) - \mathbf{v}\times"
                  r"(\nabla\times\mathbf{v})",
                  "Vektor ayniyati. Ikkinchi had vorteks $\\boldsymbol{\\omega} = "
                  "\\nabla\\times\\mathbf{v}$ ni o'z ichiga oladi (tmm-06). "
                  "Bu shakl integrallash uchun hal qiluvchi."),
                d("4. Statsionar oqim va og'irlik potensiali",
                  r"\nabla\Big(\frac{v^2}{2} + \frac{p}{\rho} + gz\Big) "
                  r"= \mathbf{v}\times\boldsymbol{\omega}",
                  "$\\partial\\mathbf{v}/\\partial t = 0$ va "
                  "$\\mathbf{g} = -\\nabla(gz)$, hamda $\\rho = $ const deb "
                  "olamiz. Chap tomon — to'liq gradiyent."),
                d("5. Oqim chizig'i bo'ylab skalyar ko'paytirish",
                  r"\mathbf{v}\cdot\nabla\Big(\frac{v^2}{2} + \frac{p}{\rho} "
                  r"+ gz\Big) = \mathbf{v}\cdot(\mathbf{v}\times"
                  r"\boldsymbol{\omega}) = 0",
                  "Aralash ko'paytma nolga teng, chunki $\\mathbf{v}\\times"
                  "\\boldsymbol{\\omega}$ $\\mathbf{v}$ ga perpendikulyar. "
                  "Shu bitta qadam butun Bernulli tenglamasini beradi."),
                d("6. Bernulli tenglamasi",
                  r"\frac{v^2}{2} + \frac{p}{\rho} + gz = \text{const} "
                  r"\quad\text{(oqim chizig'i bo'ylab)}",
                  "Gradiyentning tezlik yo'nalishidagi proeksiyasi nol — "
                  "demak ifoda oqim chizig'i bo'ylab o'zgarmaydi. "
                  "$\\rho$ ga ko'paytirsak: $p + \\frac{1}{2}\\rho v^2 + "
                  "\\rho gz = $ const."),
                d("7. Vorteksi nol oqimda (potensial oqim)",
                  r"\boldsymbol{\omega} = 0 \;\Rightarrow\; \mathbf{v} = \nabla\varphi, "
                  r"\quad \nabla^2\varphi = 0 \;\Rightarrow\; \text{const butun sohada}",
                  "Vorteks nol bo'lsa, $\\mathbf{v}\\times\\boldsymbol{\\omega} = 0$ "
                  "aynan nolga teng va Bernulli doimiysi **butun oqimda** bir xil "
                  "bo'ladi — nafaqat bitta chiziq bo'ylab. Uzluksizlik "
                  "tenglamasi esa Laplas tenglamasiga aylanadi."),
                d("8. Ventura va Torrichelli natijalari",
                  r"Q = A_2\sqrt{\frac{2\Delta p/\rho}{1 - (A_2/A_1)^2}}; \qquad "
                  r"v = \sqrt{2gh}",
                  "Bernulli + uzluksizlik ($A_1v_1 = A_2v_2$) dan Ventura "
                  "formulasi; erkin sirtdan teshikkacha qo'llanganda esa "
                  "Torrichelli formulasi — u erkin tushish tezligi bilan bir xil!"),
            ],
            meaning=(
                "Bernulli tenglamasining uch hadi — bir xil kattalikning uch "
                "ko'rinishi: $p$ — bosim energiyasi, $\\frac{1}{2}\\rho v^2$ — "
                "kinetik energiya, $\\rho gz$ — potensial energiya, hammasi "
                "hajm birligiga. Ularning yig'indisi o'zgarmasligi shuni "
                "anglatadiki, **tezlik ortsa bosim tushadi** — bu intuitsiyaga "
                "zid tuyuladi (tez oqim kuchliroq bosadi deb o'ylanadi), lekin "
                "aslida to'g'ri: suyuqlikni tezlashtirish uchun uni oldinga "
                "itaruvchi kuch kerak, u esa faqat bosim farqidan kelishi "
                "mumkin. Demak oqim tezlashayotgan joyda bosim albatta "
                "pasayayotgan bo'ladi. Torrichelli formulasi "
                "$v = \\sqrt{2gh}$ ning chiroyi shundaki, u erkin tushayotgan "
                "jism tezligi bilan aynan bir xil: suyuqlik zarrasi ham "
                "$h$ balandlikdan 'tushadi', faqat vertikal emas, quvur "
                "bo'ylab. Energiya esa yo'lni bilmaydi."
            ),
            equations=[
                eq(r"\rho\frac{D\mathbf{v}}{Dt} = -\nabla p + \rho\mathbf{g}",
                   "Eyler tenglamalari (ideal suyuqlik harakati).",
                   "Eyler tenglamalari"),
                eq(r"p + \tfrac{1}{2}\rho v^2 + \rho g z = \text{const}",
                   "Bernulli integrali oqim chizig'i bo'ylab.",
                   "Bernulli tenglamasi"),
                eq(r"A_1 v_1 = A_2 v_2 = Q",
                   "Siqilmaydigan oqim uchun uzluksizlik (sarf saqlanishi).",
                   "Uzluksizlik"),
                eq(r"\nabla^2\varphi = 0",
                   "Potensial oqim uchun Laplas tenglamasi.",
                   "Potensial oqim"),
            ],
            conditions=(
                "**Bernulli tenglamasining qo'llanish shartlari** (hammasi "
                "bajarilishi shart):\n"
                "1. Oqim **statsionar** ($\\partial/\\partial t = 0$);\n"
                "2. Suyuqlik **siqilmaydigan** ($\\rho = $ const; gaz uchun "
                "$\\mathrm{Ma} < 0{,}3$);\n"
                "3. **Yopishqoqlik e'tiborsiz** (ishqalanish yo'qotishlari yo'q);\n"
                "4. Ifoda **bitta oqim chizig'i bo'ylab** qo'llaniladi "
                "(vorteks nol bo'lsagina butun sohada).\n\n"
                "**Chegaraviy shartlar:** qattiq devorda o'tmaslik sharti "
                "$\\mathbf{v}\\cdot\\mathbf{n} = 0$ (ideal suyuqlikda urinma "
                "tezlik erkin — sirpanish mumkin); erkin sirtda "
                "$p = p_{\\text{atm}}$; kirish kesimida tezlik yoki bosim berilgan.\n\n"
                "**Kavitatsiya cheklovi:** $p_{\\min} > p_v$ (to'yingan bug' "
                "bosimi, 20 °C suvda $\\approx 2{,}34$ kPa)."
            ),
            worked=WorkedExample(
                statement=(
                    "Ventura rasxodomeri: kirish diametri $D_1 = 100$ mm, "
                    "tor kesim $D_2 = 50$ mm, gorizontal joylashgan. Suv "
                    "($\\rho = 1000$ kg/m³) oqmoqda, o'lchangan bosim farqi "
                    "$\\Delta p = 35$ kPa. (a) Sarfni toping. (b) Tor "
                    "kesimdagi bosim 101,3 kPa absolyut kirish bosimida "
                    "qancha bo'ladi? (c) Kavitatsiya xavfi bormi?"
                ),
                given=[
                    r"D_1 = 100\ \text{mm},\ D_2 = 50\ \text{mm}",
                    r"\Delta p = p_1 - p_2 = 35\ \text{kPa}",
                    r"\rho = 1000\ \text{kg/m}^3,\ p_v = 2{,}34\ \text{kPa}",
                ],
                steps=[
                    st(r"A_1 = \frac{\pi \cdot 0{,}1^2}{4} = 7{,}854\times10^{-3}\ \text{m}^2, "
                       r"\quad A_2 = 1{,}963\times10^{-3}\ \text{m}^2",
                       "Kesim yuzalari. Diametr ikki marta kichraysa, yuza "
                       "to'rt marta kichrayadi."),
                    st(r"v_1 A_1 = v_2 A_2 \;\Rightarrow\; v_1 = v_2\frac{A_2}{A_1} "
                       r"= 0{,}25\,v_2",
                       "Uzluksizlik tenglamasi. Tor kesimda tezlik to'rt "
                       "marta katta."),
                    st(r"p_1 + \tfrac{1}{2}\rho v_1^2 = p_2 + \tfrac{1}{2}\rho v_2^2 "
                       r"\;\Rightarrow\; \Delta p = \tfrac{1}{2}\rho v_2^2(1 - 0{,}0625)",
                       "Gorizontal quvur, $z_1 = z_2$ — og'irlik hadi tushib qoladi."),
                    st(r"v_2 = \sqrt{\frac{2 \cdot 35\,000}{1000 \cdot 0{,}9375}} "
                       r"= \sqrt{74{,}67} = 8{,}64\ \text{m/s}",
                       "Tor kesimdagi tezlik."),
                    st(r"Q = A_2 v_2 = 1{,}963\times10^{-3} \cdot 8{,}64 "
                       r"= 1{,}696\times10^{-2}\ \text{m}^3\text{/s} = 16{,}96\ \text{l/s}",
                       "Sarf. Amalda bunga $C_d \\approx 0{,}98$ rasxod "
                       "koeffitsienti ko'paytiriladi (ishqalanish hisobiga)."),
                    st(r"p_2 = p_1 - \Delta p = 101{,}3 - 35 = 66{,}3\ \text{kPa (abs)}",
                       "Tor kesimdagi absolyut bosim."),
                    st(r"p_2 = 66{,}3\ \text{kPa} \gg p_v = 2{,}34\ \text{kPa} "
                       r"\;\Rightarrow\; \text{kavitatsiya yo'q}",
                       "Zaxira katta. Kavitatsiya boshlanishi uchun "
                       "$\\Delta p > 99$ kPa kerak, ya'ni $v_2 > 14{,}5$ m/s."),
                ],
                answer=(
                    "$Q = 16{,}96$ l/s (ideal), $C_d = 0{,}98$ bilan "
                    "$\\approx 16{,}6$ l/s; $v_2 = 8{,}64$ m/s; tor kesimda "
                    "$p_2 = 66{,}3$ kPa — kavitatsiya chegarasidan ancha uzoq."
                ),
                engineering_note=(
                    "Ventura rasxodomerining diffuzor qismi (kengayish) "
                    "ataylab uzun va sekin qilinadi — 5–7° burchak bilan. "
                    "Sabab: keskin kengayishda oqim devordan ajraladi "
                    "(separation) va energiya yo'qotiladi. Sekin diffuzorda "
                    "esa bosimning 85–95 % i tiklanadi, shuning uchun Ventura "
                    "diafragmaga (orifice plate) qaraganda ancha kam yo'qotish "
                    "beradi — garchi qimmatroq bo'lsa ham."
                ),
            ),
            computation=Computation(
                caption=(
                    "Ventura quvurida tezlik va bosim taqsimoti, kavitatsiya "
                    "chegarasi; Torrichelli bo'yicha rezervuar bo'shalish vaqti."
                ),
                code='''"""Ideal suyuqlik: Bernulli, Ventura va Torrichelli."""
import numpy as np
from labkit import PARAMS, note, series, table, value

D1 = float(PARAMS.get("D1", 100.0))/1000.0   # m
D2 = float(PARAMS.get("D2", 50.0))/1000.0    # m
dp = float(PARAMS.get("dp", 35.0))*1000.0    # Pa
rho = float(PARAMS.get("rho", 1000.0))
p1_abs = float(PARAMS.get("p1", 101.3))*1000.0
pv = float(PARAMS.get("pv", 2.34))*1000.0    # to'yingan bug' bosimi
g = 9.81

A1 = np.pi*D1**2/4
A2 = np.pi*D2**2/4
beta = D2/D1
value("Kesim nisbati beta = D2/D1", beta, "—")
value("A1", A1*1e4, "cm2")
value("A2", A2*1e4, "cm2")

v2 = np.sqrt(2*dp/(rho*(1 - beta**4)))
v1 = v2*(A2/A1)
Q = A2*v2
value("Tezlik v1 (kirish)", v1, "m/s")
value("Tezlik v2 (tor kesim)", v2, "m/s")
value("Sarf Q (ideal)", Q*1000, "l/s")
value("Sarf Q (Cd = 0.98)", 0.98*Q*1000, "l/s")

p2 = p1_abs - dp
value("Tor kesimdagi absolyut bosim p2", p2/1000, "kPa")
value("Bug' bosimidan zaxira", (p2 - pv)/1000, "kPa")
dp_cav = p1_abs - pv
v2_cav = np.sqrt(2*dp_cav/(rho*(1 - beta**4)))
value("Kavitatsiya boshlanish tezligi", v2_cav, "m/s")
value("Kavitatsiya boshlanish sarfi", A2*v2_cav*1000, "l/s")
if p2 > pv:
    note(f"Kavitatsiya YO'Q: p2 = {p2/1000:.1f} kPa > pv = {pv/1000:.2f} kPa. "
         f"Sarf {A2*v2_cav*1000:.1f} l/s dan oshsa xavf paydo bo'ladi.")
else:
    note(f"KAVITATSIYA XAVFI: p2 = {p2/1000:.1f} kPa <= pv = {pv/1000:.2f} kPa!")

# --- Ventura bo'ylab profil ---
x = np.linspace(0.0, 1.0, 400)             # normallashtirilgan uzunlik
# konfuzor (0-0.3), tomoq (0.3-0.4), diffuzor (0.4-1.0)
D = np.where(x < 0.3, D1 + (D2 - D1)*(x/0.3),
             np.where(x < 0.4, D2, D2 + (D1 - D2)*((x - 0.4)/0.6)))
A = np.pi*D**2/4
v = Q/A
pres = p1_abs + 0.5*rho*v1**2 - 0.5*rho*v**2

series("Diametr D(x)", x.tolist(), (D*1000).tolist(),
       xlabel="Normallashtirilgan uzunlik", ylabel="Diametr, mm")
series("Tezlik v(x)", x.tolist(), v.tolist(),
       xlabel="Normallashtirilgan uzunlik", ylabel="Tezlik, m/s")
series("Bosim p(x)", x.tolist(), (pres/1000).tolist(),
       xlabel="Normallashtirilgan uzunlik", ylabel="Absolyut bosim, kPa")
series("Bug' bosimi (chegara)", x.tolist(), np.full_like(x, pv/1000).tolist(),
       xlabel="Normallashtirilgan uzunlik", ylabel="Absolyut bosim, kPa")

# Bernulli doimiysini tekshirish
H = pres/(rho*g) + v**2/(2*g)
value("Bernulli napori H (min)", float(np.min(H)), "m")
value("Bernulli napori H (max)", float(np.max(H)), "m")
note(f"Napor bo'ylab o'zgarish {float(np.max(H)-np.min(H)):.2e} m — "
     f"ideal oqimda u aynan doimiy bo'lishi kerak (sonli xato darajasida).")

# --- Torrichelli: rezervuar bo'shalishi ---
H0 = float(PARAMS.get("H0", 3.0))            # boshlang'ich sath, m
Dt = float(PARAMS.get("Dt", 2.0))            # rezervuar diametri, m
d0 = float(PARAMS.get("d0", 30.0))/1000.0    # teshik diametri, m
Cd = 0.62                                     # teshik rasxod koeffitsienti

At = np.pi*Dt**2/4
a0 = np.pi*d0**2/4
# dh/dt = -Cd*a0*sqrt(2 g h)/At  ->  t = 2 At (sqrt(H0)-sqrt(h)) / (Cd a0 sqrt(2g))
t_full = 2*At*np.sqrt(H0)/(Cd*a0*np.sqrt(2*g))
value("To'liq bo'shalish vaqti (analitik)", t_full, "s")
value("To'liq bo'shalish vaqti", t_full/60, "min")

# Sonli integrallash bilan tekshirish (Eyler usuli)
dt = t_full/20000
hh, tt = H0, 0.0
hist_t, hist_h = [0.0], [H0]
while hh > 1e-6:
    vq = Cd*a0*np.sqrt(2*g*hh)
    hh -= vq/At*dt
    tt += dt
    if len(hist_t) < 400 and tt > hist_t[-1] + t_full/300:
        hist_t.append(tt); hist_h.append(max(hh, 0.0))
hist_t.append(tt); hist_h.append(0.0)
series("Sath h(t)", hist_t, hist_h, xlabel="Vaqt t, s", ylabel="Sath h, m")
value("To'liq bo'shalish vaqti (sonli)", tt, "s")
note(f"Analitik {t_full:.1f} s va sonli {tt:.1f} s — farq "
     f"{abs(tt-t_full)/t_full*100:.3f} %.")
value("Boshlang'ich chiqish tezligi", float(np.sqrt(2*g*H0)), "m/s")

table("Bernulli qo'llanish shartlari va buzilish oqibati",
      ["Shart", "Buzilsa nima bo'ladi", "Tuzatish"],
      [["Statsionar oqim", "Nostatsionar had qo'shiladi", "d(phi)/dt hadini kiriting"],
       ["Siqilmaydigan", "Zichlik o'zgaradi (Ma > 0.3)", "Siqiluvchi Bernulli"],
       ["Yopishqoqsiz", "Napor yo'qoladi", "Darsi-Veysbax yo'qotishi"],
       ["Bitta oqim chizig'i", "Doimiy chiziqdan chiziqqa o'zgaradi",
        "Vorteksi nol oqimni tekshiring"]])
''',
                parameters=[
                    p("D1", "Kirish diametri D₁", 20.0, 500.0, 100.0, 5.0, "mm"),
                    p("D2", "Tor kesim diametri D₂", 10.0, 400.0, 50.0, 5.0, "mm"),
                    p("dp", "Bosim farqi Δp", 1.0, 200.0, 35.0, 1.0, "kPa"),
                    p("rho", "Zichlik ρ", 600.0, 1400.0, 1000.0, 10.0, "kg/m³"),
                    p("p1", "Kirish absolyut bosimi p₁", 50.0, 600.0, 101.3, 1.0, "kPa"),
                    p("pv", "To'yingan bug' bosimi p_v", 0.5, 50.0, 2.34, 0.1, "kPa"),
                    p("H0", "Rezervuar sathi H₀", 0.2, 20.0, 3.0, 0.1, "m"),
                    p("Dt", "Rezervuar diametri", 0.3, 10.0, 2.0, 0.1, "m"),
                    p("d0", "Teshik diametri", 5.0, 200.0, 30.0, 1.0, "mm"),
                ],
                expected_output=(
                    "v₂ = 8,64 m/s, Q = 16,96 l/s; p₂ = 66,3 kPa, kavitatsiya "
                    "tezligi ≈ 14,5 m/s. Napor bo'ylab o'zgarish ~1e-14 m "
                    "(ideal oqim). Rezervuar bo'shalish vaqti ≈ 1541 s."
                ),
            ),
            visual=vis(
                kind="Ventura oqimi va energiya chiziqlari",
                tool="React/SVG",
                description=(
                    "Ventura kesimi, oqim chiziqlari, tezlik va bosim "
                    "profillari hamda EGL/HGL energiya chiziqlari."
                ),
                how_to_draw=(
                    "React/SVG: Ventura konturi ikkita simmetrik `<path>` "
                    "(yuqori va pastki devor) bilan chiziladi, ichi och rangda. "
                    "Oqim chiziqlari — devorga parallel 5–7 ta egri chiziq, "
                    "ular tomoqda zichlashadi (zichlik tezlikni ko'rsatadi); "
                    "har bir chiziqda `<animateMotion>` bilan kichik nuqta "
                    "yurdiriladi, tezligi $v(x)$ ga mutanosib — bu tezlashuvni "
                    "ko'z bilan ko'rsatadi. Tepada pyezometrik naychalar: "
                    "har bir kesimda vertikal naycha va undagi suv ustuni "
                    "balandligi $p/(\\rho g)$ ga teng — tomoqda ustun pasayadi. "
                    "EGL (energiya chizig'i) gorizontal punktir, HGL "
                    "(pyezometrik chiziq) esa undan $v^2/2g$ pastda — ikkisi "
                    "orasidagi masofa tezlik naporini ko'rsatadi. Bug' bosimi "
                    "chizig'i qizil punktir; bosim egri chizig'i uni kesib "
                    "o'tsa, kesishgan soha qizil shtrixlanadi (kavitatsiya)."
                ),
            ),
            interp=(
                "Bernulli napori $H$ ning butun Ventura bo'ylab $10^{-14}$ m "
                "aniqlikda saqlanishi — bu kodning emas, modelning "
                "xususiyati: ideal oqimda energiya yo'qolmaydi. Real "
                "Venturada esa $H$ chiqishda kirishdagidan 5–15 % past "
                "bo'ladi va bu farq aynan yopishqoqlik yo'qotishi — keyingi "
                "mavzuning mavzusi. Kavitatsiya hisobi muhandislik uchun eng "
                "amaliy natija: $\\beta = D_2/D_1$ ni kichraytirish "
                "o'lchov sezgirligini oshiradi ($\\Delta p \\propto \\beta^{-4}$), "
                "lekin kavitatsiya chegarasiga yaqinlashtiradi. Standart "
                "(ISO 5167) $0{,}3 \\le \\beta \\le 0{,}75$ oralig'ini "
                "tavsiya qiladi — aynan shu murosaning natijasi. Rezervuar "
                "bo'shalishida sonli va analitik yechimning 0,01 % dan kichik "
                "farqi esa Eyler usulining bunday sodda ODE uchun yetarli "
                "ekanligini ko'rsatadi; murakkabroq masalalarda (5-fan) "
                "yuqori tartibli usullar kerak bo'ladi."
            ),
            mistakes=[
                "Bernulli tenglamasini yopishqoq oqimda, uzun quvurda "
                "yo'qotishlarsiz qo'llash. Uzun quvurda Darsi–Veysbax "
                "yo'qotishi $h_f = f\\frac{L}{D}\\frac{v^2}{2g}$ hal "
                "qiluvchi bo'ladi.",
                "Ifodani turli oqim chiziqlari orasida taqqoslash. Bu faqat "
                "vorteksi nol (potensial) oqimda o'rinli; vorteksli oqimda "
                "har bir chiziqda o'z doimiysi bor.",
                "Nasos yoki turbinadan o'tayotgan oqimga oddiy Bernullini "
                "qo'llash. Mashina energiya qo'shadi yoki oladi, shuning uchun "
                "$H_{\\text{nasos}}$ yoki $H_{\\text{turbina}}$ hadi kerak.",
                "Kavitatsiyani manometrik bosim bilan tekshirish. Bug' bosimi "
                "**absolyut** shkalada berilgan, shuning uchun taqqoslash ham "
                "absolyut bosimda bo'lishi shart.",
            ],
            quiz=[
                q("Nima uchun tor kesimda bosim pasayadi?",
                  "Uzluksizlik bo'yicha tezlik ortadi; suyuqlikni "
                  "tezlashtiruvchi kuch faqat bosim farqidan kelishi mumkin, "
                  "demak oldinda bosim pastroq bo'lishi shart.", "konseptual"),
                q("Bernulli tenglamasining to'rtta qo'llanish shartini sanang.",
                  "Statsionar, siqilmaydigan, yopishqoqsiz oqim va bitta "
                  "oqim chizig'i bo'ylab (yoki vorteksi nol bo'lsa butun sohada).",
                  "konseptual"),
                q("5 m chuqurlikdagi teshikdan suv qanday tezlikda otiladi?",
                  "Torrichelli: $v = \\sqrt{2gh} = \\sqrt{2 \\cdot 9{,}81 "
                  "\\cdot 5} = 9{,}90$ m/s.", "hisob"),
                q("Pito naychasi nimani o'lchaydi va tezlik qanday topiladi?",
                  "To'xtash bosimi $p_0 = p + \\frac{1}{2}\\rho v^2$ ni. "
                  "Statik bosim bilan farqidan $v = \\sqrt{2(p_0-p)/\\rho}$.",
                  "talqin"),
                q("Kodda `1 - beta**4` hadi qayerdan keladi?",
                  "Uzluksizlikdan $v_1 = v_2\\beta^2$, uni Bernulliga qo'ysak "
                  "$\\Delta p = \\frac{1}{2}\\rho v_2^2(1 - \\beta^4)$ chiqadi. "
                  "$\\beta$ kichrayganda had birga intiladi.", "kod"),
                q("Torrichelli tezligi nima uchun erkin tushish tezligi bilan "
                  "bir xil?",
                  "Ikkala holatda ham bir xil balandlik farqidagi potensial "
                  "energiya to'liq kinetik energiyaga aylanadi. Energiya "
                  "balansi yo'lga bog'liq emas.", "talqin"),
            ],
            bridge=(
                "Ideal suyuqlik modeli Ventura va Pito uchun ajoyib ishladi, "
                "lekin u devordagi ishqalanishni, quvurdagi bosim "
                "yo'qotishini va qarshilik kuchini umuman tushuntira "
                "olmaydi (Dalamber paradoksi). Keyingi mavzuda yopishqoqlikni "
                "konstitutiv tenglamaga kiritamiz va Navye–Stoks "
                "tenglamalarini quramiz."
            ),
            research=(
                "Bernulli tenglamasining nostatsionar umumlashmasini "
                "o'rganing: potensial oqim uchun "
                "$\\partial\\varphi/\\partial t + v^2/2 + p/\\rho + gz = f(t)$. "
                "Uni quvurdagi zadvijka keskin yopilganda yuzaga keladigan "
                "suv bolg'asi (water hammer) hodisasiga qo'llang: Jukovskiy "
                "formulasi $\\Delta p = \\rho a \\Delta v$ ni chiqaring, "
                "bu yerda $a$ — quvurdagi bosim to'lqini tezligi (tmm-20 "
                "dagi to'lqin tezligi bilan bog'lang). Quvur devorining "
                "elastikligi $a$ ga qanday ta'sir qiladi?"
            ),
            manim_ref=manim(
                scene="BernoulliScene",
                module="manim/scenes/tmm_fluid.py",
                title="Ventura oqimi va Bernulli balansi",
                summary=(
                    "Oqim chiziqlari tomoqda zichlashadi, zarralar "
                    "tezlashadi, pyezometrik naychalardagi suv ustuni "
                    "pasayadi; uch energiya hadi ustun diagrammada bir-birini "
                    "qanday to'ldirishi ko'rsatiladi."
                ),
            ),
        ),
    ),

    # ------------------------------------------------------------------ tmm-27
    Topic(
        id="tmm-27",
        subject_id=S, module_id=M, order=27,
        title="Yopishqoq suyuqlik: Nyuton gipotezasi va Navye–Stoks tenglamalari",
        description=(
            "Yopishqoq suyuqlik uchun konstitutiv tenglama, Stoks "
            "gipotezalari, Navye–Stoks tenglamalari tizimi, chegaraviy "
            "shartlar va tenglamalarning matematik tabiati."
        ),
        learning_objective=(
            "Deformatsiya tezligi tenzoridan yopishqoq kuchlanishni ifodalash, "
            "Navye–Stoks tenglamalarini to'liq keltirib chiqarish va "
            "ulardagi har bir hadning fizik ma'nosini tushuntirish."
        ),
        prerequisites=["tmm-26", "tmm-06", "tmm-13"],
        mathematical_core=(
            "$\\tau_{ij} = 2\\mu D_{ij} + \\lambda_f D_{kk}\\delta_{ij}$, "
            "Stoks munosabati $3\\lambda_f + 2\\mu = 0$, "
            "$\\rho D\\mathbf{v}/Dt = -\\nabla p + \\mu\\nabla^2\\mathbf{v} "
            "+ \\rho\\mathbf{g}$, nochiziqli parabolik PDE tizimi."
        ),
        engineering_application=(
            "Quvur va kanal gidravlikasi, nasos va kompressor, moylash "
            "(lubrication), qon oqimi, CFD hisoblarining asosi."
        ),
        computational_component=(
            "Navye–Stoks tenglamalarini o'lchamsizlashtirish, hadlar "
            "kattaliklarini taqqoslash, Kuett oqimini sonli yechish va "
            "turg'un holatga chiqish vaqtini o'lchash."
        ),
        visualization_component=(
            "Yopishqoq kuchlanishning tezlik profiliga bog'liqligi, "
            "no-slip sharti, hadlarning nisbiy kattaligi diagrammasi."
        ),
        research_extension=(
            "Nonyuton suyuqliklarni o'rganing: quvvat qonuni (power-law), "
            "Bingem plastik va tiksotrop modellar; ularni qon, loy va "
            "polimer eritmasiga qanday qo'llash mumkin?"
        ),
        difficulty="ilg'or",
        previous_link=(
            "tmm-26 dagi ideal suyuqlik modeli Dalamber paradoksiga olib "
            "keldi: shar atrofida qarshilik kuchi nolga teng chiqadi, "
            "bu esa tajribaga zid. Sababi — yopishqoqlikning e'tiborsiz "
            "qoldirilishi. Endi uni konstitutiv tenglamaga kiritamiz."
        ),
        next_topic="tmm-28",
        estimated_minutes=100,
        tags=["Navye-Stoks", "yopishqoqlik", "CFD", "suyuqlik"],
        lesson=_lesson(
            problem=(
                "Ideal suyuqlik nazariyasi bo'yicha oqimdagi sharga ta'sir "
                "qiluvchi qarshilik kuchi **nolga teng** (Dalamber "
                "paradoksi, 1752). Lekin har qanday tajriba buning aksini "
                "ko'rsatadi: samolyot yonilg'i sarflaydi, quvurda bosim "
                "tushadi, velosipedchi shamolga qarshi kurashadi. Nazariya "
                "qayerda xato qilgan? Javob — devor yaqinidagi ingichka "
                "qatlamda: u yerda tezlik gradiyenti juda katta va "
                "yopishqoqlik, qanchalik kichik bo'lmasin, hal qiluvchi rol "
                "o'ynaydi. Bu hadni tenglamaga qanday kiritamiz?"
            ),
            concepts=[
                c("Nyuton suyuqligi (Newtonian fluid)",
                  "Yopishqoq kuchlanish deformatsiya tezligiga **chiziqli** "
                  "bog'liq bo'lgan suyuqlik: $\\tau = \\mu\\,dv/dy$. "
                  "Suv, havo, moylarning ko'pchiligi shunday."),
                c("Dinamik va kinematik yopishqoqlik",
                  "$\\mu$ [Pa·s] — dinamik yopishqoqlik; "
                  "$\\nu = \\mu/\\rho$ [m²/s] — kinematik yopishqoqlik, "
                  "u impuls diffuziyasi koeffitsienti."),
                c("Stoks gipotezalari",
                  "(1) $\\tau_{ij}$ $D_{ij}$ ga chiziqli bog'liq; "
                  "(2) suyuqlik izotrop; (3) $D_{ij} = 0$ da "
                  "$\\sigma_{ij} = -p\\delta_{ij}$; (4) hajmiy yopishqoqlik "
                  "nol: $3\\lambda_f + 2\\mu = 0$."),
                c("No-slip sharti (no-slip condition)",
                  "Yopishqoq suyuqlik qattiq devorda devor bilan bir xil "
                  "tezlikka ega: $\\mathbf{v}_{\\text{suyuqlik}} = "
                  "\\mathbf{v}_{\\text{devor}}$. Bu tajribaviy fakt va "
                  "chegaraviy qatlamning sababi."),
                c("Navye–Stoks tenglamalari",
                  "Yopishqoq siqilmaydigan suyuqlikning harakat "
                  "tenglamalari; uzluksizlik bilan birga to'rt noma'lum "
                  "($u, v, w, p$) uchun to'rt tenglama."),
                c("Dalamber paradoksi (d'Alembert's paradox)",
                  "Ideal suyuqlikda jismga qarshilik kuchi nolga teng "
                  "chiqishi — bu modelning chegarasini ko'rsatuvchi klassik "
                  "qarama-qarshilik."),
            ],
            derivation=[
                d("1. Kuchlanishni bosim va yopishqoq qismga ajratish",
                  r"\sigma_{ij} = -p\,\delta_{ij} + \tau_{ij}",
                  "Birinchi had — tinch holatdagi (gidrostatik) qism, "
                  "ikkinchisi — harakat tufayli paydo bo'ladigan yopishqoq "
                  "kuchlanish (deviator qism)."),
                d("2. Chiziqli izotrop konstitutiv munosabat",
                  r"\tau_{ij} = 2\mu D_{ij} + \lambda_f D_{kk}\delta_{ij}, \qquad "
                  r"D_{ij} = \tfrac{1}{2}\Big(\frac{\partial v_i}{\partial x_j} "
                  r"+ \frac{\partial v_j}{\partial x_i}\Big)",
                  "Shakli tmm-14 dagi Guk qonuni bilan **aynan bir xil**, "
                  "faqat deformatsiya o'rnida deformatsiya **tezligi** "
                  "$D_{ij}$ (tmm-06) turadi. Bu — qattiq jism va suyuqlik "
                  "mexanikasining chuqur parallelligi."),
                d("3. Stoks gipotezasi",
                  r"\tau_{kk} = (2\mu + 3\lambda_f)D_{kk} = 0 \;\Longrightarrow\; "
                  r"\lambda_f = -\tfrac{2}{3}\mu",
                  "Yopishqoq kuchlanishning izi nolga teng deb olinadi, "
                  "ya'ni hajm o'zgarishi yopishqoq qarshilik keltirib "
                  "chiqarmaydi. Siqilmaydigan oqimda ($D_{kk} = 0$) bu had "
                  "baribir tushib ketadi."),
                d("4. Siqilmaydigan hol uchun soddalashtirish",
                  r"\nabla\cdot\mathbf{v} = 0 \;\Longrightarrow\; "
                  r"\tau_{ij} = 2\mu D_{ij} = \mu\Big(\frac{\partial v_i}{\partial x_j} "
                  r"+ \frac{\partial v_j}{\partial x_i}\Big)",
                  "Uzluksizlik tenglamasi (tmm-09) $D_{kk} = 0$ ni beradi. "
                  "Endi faqat bitta material doimiysi $\\mu$ qoladi."),
                d("5. Divergensiyani hisoblash",
                  r"\frac{\partial\tau_{ij}}{\partial x_j} = "
                  r"\mu\Big(\frac{\partial^2 v_i}{\partial x_j\partial x_j} "
                  r"+ \frac{\partial}{\partial x_i}\underbrace{\frac{\partial v_j}"
                  r"{\partial x_j}}_{=0}\Big) = \mu\nabla^2 v_i",
                  "Ikkinchi had uzluksizlik tufayli nolga teng. Natijada "
                  "yopishqoq had oddiy Laplasianga aylanadi — bu diffuziya "
                  "operatori."),
                d("6. Navye–Stoks tenglamalari",
                  r"\rho\Big(\frac{\partial\mathbf{v}}{\partial t} "
                  r"+ (\mathbf{v}\cdot\nabla)\mathbf{v}\Big) = "
                  r"-\nabla p + \mu\nabla^2\mathbf{v} + \rho\mathbf{g}",
                  "Koshi tenglamasiga (tmm-10) 5-qadam natijasini qo'yamiz. "
                  "Bu — suyuqliklar mexanikasining markaziy tenglamasi, "
                  "1822 (Navye) va 1845 (Stoks)."),
                d("7. O'lchamsizlashtirish va Reynolds soni",
                  r"\frac{\partial\mathbf{v}^*}{\partial t^*} + (\mathbf{v}^*\cdot"
                  r"\nabla^*)\mathbf{v}^* = -\nabla^* p^* + "
                  r"\frac{1}{\mathrm{Re}}\nabla^{*2}\mathbf{v}^*, \qquad "
                  r"\mathrm{Re} = \frac{\rho U L}{\mu}",
                  "$x^* = x/L$, $v^* = v/U$, $t^* = tU/L$, "
                  "$p^* = p/(\\rho U^2)$ almashtirishlari. Butun masalada "
                  "**bitta** o'lchamsiz parametr qoladi — Reynolds soni."),
                d("8. Tenglamalarning matematik tabiati",
                  r"\text{4 noma'lum } (u, v, w, p) \;\leftrightarrow\; "
                  r"\text{4 tenglama (3 NS + 1 uzluksizlik)}",
                  "Tizim yopiq. Lekin $p$ uchun alohida evolyutsiya "
                  "tenglamasi yo'q — u uzluksizlikni ta'minlovchi Lagranj "
                  "ko'paytuvchisi rolini o'ynaydi. Shuning uchun sonli "
                  "yechishda maxsus algoritmlar (SIMPLE, proeksiya usuli) kerak."),
            ],
            meaning=(
                "$\\mu\\nabla^2\\mathbf{v}$ hadi — impuls **diffuziyasi**. "
                "Issiqlik o'tkazuvchanlik tenglamasidagi $k\\nabla^2 T$ bilan "
                "bir xil tuzilishga ega va bir xil ish qiladi: tezlik "
                "farqlarini tekislaydi, tez oqayotgan qatlamdan sekinroq "
                "qatlamga impuls uzatadi. Kinematik yopishqoqlik "
                "$\\nu = \\mu/\\rho$ aynan shu diffuziyaning koeffitsienti; "
                "suvda $\\nu \\approx 10^{-6}$ m²/s, havoda esa "
                "$1{,}5\\times10^{-5}$ m²/s — ya'ni havo **15 marta tezroq** "
                "impuls tarqatadi, garchi u ancha 'suyuqroq' tuyulsa ham. "
                "Reynolds soni $\\mathrm{Re} = UL/\\nu$ esa ikki hadning "
                "nisbati: inersiya (konvektiv tashish) va yopishqoqlik "
                "(diffuziv tashish). $\\mathrm{Re} \\ll 1$ da yopishqoqlik "
                "hukmron — oqim sekin, tartibli, qaytuvchan (Stoks oqimi); "
                "$\\mathrm{Re} \\gg 1$ da inersiya hukmron — oqim "
                "turbulentlashadi. Dalamber paradoksining yechimi ham shu "
                "yerda: $\\mathrm{Re} \\to \\infty$ da yopishqoq had butun "
                "sohada kichik, **lekin devor yonidagi ingichka qatlamda "
                "emas** — u yerda $\\nabla^2 v$ shunchalik kattaki, "
                "$1/\\mathrm{Re}$ ga ko'paytirilganda ham chekli qoladi. "
                "Bu — Prandtlning 1904-yildagi buyuk g'oyasi."
            ),
            equations=[
                eq(r"\rho\frac{D\mathbf{v}}{Dt} = -\nabla p + \mu\nabla^2\mathbf{v} "
                   r"+ \rho\mathbf{g}",
                   "Navye–Stoks tenglamalari (siqilmaydigan, doimiy $\\mu$).",
                   "Navye–Stoks"),
                eq(r"\nabla\cdot\mathbf{v} = 0",
                   "Siqilmaydigan oqim uchun uzluksizlik tenglamasi.",
                   "Uzluksizlik"),
                eq(r"\tau_{ij} = 2\mu D_{ij}",
                   "Nyuton suyuqligi uchun konstitutiv tenglama.",
                   "Nyuton gipotezasi"),
                eq(r"\mathrm{Re} = \frac{\rho U L}{\mu} = \frac{UL}{\nu}",
                   "Reynolds soni — inersiya va yopishqoqlik kuchlari nisbati.",
                   "Reynolds soni"),
            ],
            conditions=(
                "**Qattiq devorda (no-slip + o'tmaslik):**\n"
                "$$\\mathbf{v} = \\mathbf{v}_{\\text{devor}} \\quad "
                "(\\text{urinma va normal tashkil etuvchilar birgalikda}).$$\n"
                "Bu ideal suyuqlikdan asosiy farq: u yerda faqat "
                "$\\mathbf{v}\\cdot\\mathbf{n} = 0$ talab qilinardi, "
                "sirpanishga ruxsat berilardi.\n\n"
                "**Erkin sirtda:** kinematik shart (sirt zarralar bilan "
                "harakatlanadi) va dinamik shart "
                "$\\boldsymbol{\\sigma}\\cdot\\mathbf{n} = -p_{\\text{atm}}"
                "\\mathbf{n} + \\gamma\\kappa\\mathbf{n}$ (sirt taranglik bilan).\n\n"
                "**Kirish/chiqishda:** kirish tezlik profili berilgan; "
                "chiqishda odatda $\\partial\\mathbf{v}/\\partial n = 0$ "
                "va $p$ berilgan.\n\n"
                "**Boshlang'ich shart:** $\\mathbf{v}(\\mathbf{x}, 0)$ "
                "berilgan va u uzluksizlik tenglamasini qanoatlantirishi "
                "shart ($\\nabla\\cdot\\mathbf{v}_0 = 0$)."
            ),
            worked=WorkedExample(
                statement=(
                    "Moylash qatlami: ikki tekis plastina orasida "
                    "$h = 0{,}2$ mm qalinlikdagi moy ($\\mu = 0{,}15$ Pa·s, "
                    "$\\rho = 880$ kg/m³). Ustki plastina $U = 3$ m/s "
                    "tezlikda siljiydi, pastkisi qo'zg'almas, bosim gradiyenti "
                    "yo'q. (a) Tezlik profilini toping. (b) Ishqalanish "
                    "kuchlanishini va 0,1 m² yuzaga ta'sir qiluvchi kuchni "
                    "hisoblang. (c) Reynolds sonini toping va oqim rejimini "
                    "aniqlang. (d) Isrof quvvatini baholang."
                ),
                given=[
                    r"h = 0{,}2\ \text{mm} = 2\times10^{-4}\ \text{m}",
                    r"\mu = 0{,}15\ \text{Pa·s},\ \rho = 880\ \text{kg/m}^3",
                    r"U = 3\ \text{m/s},\ A = 0{,}1\ \text{m}^2",
                ],
                steps=[
                    st(r"0 = -\frac{\partial p}{\partial x} + \mu\frac{d^2u}{dy^2} "
                       r"\;\Rightarrow\; \frac{d^2u}{dy^2} = 0",
                       "Statsionar, to'liq rivojlangan oqim: inersiya hadlari "
                       "nolga teng, bosim gradiyenti berilishi bo'yicha nol."),
                    st(r"u(y) = C_1 y + C_2; \quad u(0) = 0,\ u(h) = U "
                       r"\;\Rightarrow\; u(y) = U\frac{y}{h}",
                       "No-slip shartlari ikkala devorda. Natija — chiziqli "
                       "profil, bu sof Kuett oqimi."),
                    st(r"\tau = \mu\frac{du}{dy} = \mu\frac{U}{h} "
                       r"= 0{,}15 \cdot \frac{3}{2\times10^{-4}} = 2250\ \text{Pa}",
                       "Kuchlanish butun qatlam bo'ylab bir xil (profil chiziqli)."),
                    st(r"F = \tau A = 2250 \cdot 0{,}1 = 225\ \text{N}",
                       "Plastinani siljitish uchun kerakli kuch."),
                    st(r"\mathrm{Re} = \frac{\rho U h}{\mu} = "
                       r"\frac{880 \cdot 3 \cdot 2\times10^{-4}}{0{,}15} = 3{,}52",
                       "$\\mathrm{Re} \\ll 1500$ — oqim qat'iy laminar. "
                       "Moylash qatlamlarida deyarli har doim shunday."),
                    st(r"P = F \cdot U = 225 \cdot 3 = 675\ \text{W}",
                       "Ishqalanishga sarflanadigan quvvat — u to'liq "
                       "issiqlikka aylanadi."),
                    st(r"\Phi = \mu\Big(\frac{du}{dy}\Big)^2 = 0{,}15 \cdot "
                       r"(15\,000)^2 = 3{,}375\times10^{7}\ \text{W/m}^3",
                       "Yopishqoq dissipatsiya zichligi. Hajm "
                       "$2\\times10^{-5}$ m³ ga ko'paytirsak 675 W — "
                       "energiya balansi yopildi."),
                ],
                answer=(
                    "$u(y) = 3y/h$ (chiziqli); $\\tau = 2250$ Pa, $F = 225$ N; "
                    "$\\mathrm{Re} = 3{,}52$ — laminar; isrof quvvati 675 W, "
                    "dissipatsiya zichligi $3{,}4\\times10^7$ W/m³."
                ),
                engineering_note=(
                    "675 W — juda katta issiqlik oqimi: 20 sm³ moyni bir "
                    "necha soniyada qizdirib yuborishi mumkin. Shuning uchun "
                    "podshipniklarda moy doimiy aylanib turadi va sovutiladi. "
                    "Bundan tashqari, $\\mu$ haroratga eksponensial bog'liq "
                    "(harorat 20 °C ortsa, $\\mu$ taxminan ikki marta "
                    "kamayadi), demak qizigan moy ingichka plyonkani ushlab "
                    "turolmaydi — bu 'issiqlik qochishi' (thermal runaway) "
                    "hodisasiga olib kelishi mumkin."
                ),
            ),
            computation=Computation(
                caption=(
                    "Navye–Stoks hadlarining kattaligini taqqoslash, Kuett "
                    "oqimini nostatsionar holatdan turg'un holatga sonli olib chiqish."
                ),
                code='''"""Navye-Stoks: hadlar balansi va nostatsionar Kuett oqimi."""
import numpy as np
from labkit import PARAMS, note, series, table, value

rho = float(PARAMS.get("rho", 880.0))       # kg/m^3
mu = float(PARAMS.get("mu", 0.15))          # Pa*s
U = float(PARAMS.get("U", 3.0))             # m/s
h = float(PARAMS.get("h", 0.2))/1000.0      # m
L = float(PARAMS.get("L", 0.1))             # xarakterli uzunlik, m

nu = mu/rho
Re_h = rho*U*h/mu
Re_L = rho*U*L/mu
value("Kinematik yopishqoqlik nu", nu*1e6, "mm2/s")
value("Re (h bo'yicha)", Re_h, "—")
value("Re (L bo'yicha)", Re_L, "—")

# --- Hadlar kattaligini baholash (scaling analysis) ---
inertia = rho*U**2/L
viscous = mu*U/h**2
gravity = rho*9.81
value("Inersiya hadi ~ rho U^2/L", inertia, "Pa/m")
value("Yopishqoq had ~ mu U/h^2", viscous, "Pa/m")
value("Og'irlik hadi ~ rho g", gravity, "Pa/m")
value("Inersiya/yopishqoq", inertia/viscous, "—")
if inertia/viscous < 0.1:
    note("Yopishqoq had hukmron: inersiyani e'tiborsiz qoldirish mumkin "
         "(Stoks yaqinlashuvi, moylash nazariyasi).")
elif inertia/viscous > 10:
    note("Inersiya hukmron: yopishqoqlik faqat devor yonidagi ingichka "
         "chegaraviy qatlamda muhim (Prandtl).")
else:
    note("Ikkala had taqqoslanadigan: to'liq Navye-Stoks kerak.")

# --- Turg'un Kuett oqimi (analitik) ---
y = np.linspace(0.0, h, 200)
u_steady = U*y/h
series("Turg'un profil u(y)", (u_steady).tolist(), (y*1000).tolist(),
       xlabel="Tezlik u, m/s", ylabel="y, mm")
tau = mu*U/h
value("Ishqalanish kuchlanishi tau", tau, "Pa")
value("Kuch 0.1 m2 yuzaga", tau*0.1, "N")
value("Isrof quvvati", tau*0.1*U, "W")
value("Dissipatsiya zichligi", mu*(U/h)**2, "W/m3")

# --- Nostatsionar Kuett: du/dt = nu * d2u/dy2 (birinchi Stoks masalasi) ---
ny = 121
yy = np.linspace(0.0, h, ny)
dy = yy[1] - yy[0]
dt = 0.2*dy**2/nu                    # diffuziv turg'unlik sharti
t_diff = h**2/nu                     # xarakterli diffuziya vaqti
nt = int(3*t_diff/dt)
value("Diffuziya vaqti h^2/nu", t_diff*1000, "ms")
value("Vaqt qadami dt", dt*1e6, "mks")
value("Qadamlar soni", float(nt), "dona")

u = np.zeros(ny)
u[-1] = U                            # ustki plastina birdan harakatga keldi
snap_times = [0.02*t_diff, 0.1*t_diff, 0.3*t_diff, 1.0*t_diff, 3.0*t_diff]
snap_idx = [int(s/dt) for s in snap_times]
r_coef = nu*dt/dy**2
for n in range(1, nt + 1):
    u_new = u.copy()
    u_new[1:-1] = u[1:-1] + r_coef*(u[2:] - 2*u[1:-1] + u[:-2])
    u_new[0] = 0.0
    u_new[-1] = U
    u = u_new
    if n in snap_idx:
        series(f"u(y), t = {n*dt*1000:.2f} ms", u.tolist(), (yy*1000).tolist(),
               xlabel="Tezlik u, m/s", ylabel="y, mm")

err = float(np.max(np.abs(u - U*yy/h)))
value("Turg'un yechimdan maksimal farq", err, "m/s")
value("Nisbiy farq", 100*err/U, "%")
note(f"3*h^2/nu vaqtdan keyin sonli yechim chiziqli profilga "
     f"{100*err/U:.3f} % aniqlikda yaqinlashdi — diffuziya vaqti "
     f"masshtabi to'g'ri baholangan.")

table("Navye-Stoks hadlarining fizik ma'nosi",
      ["Had", "Ma'nosi", "Yo'qolsa qanday model qoladi"],
      [["rho dv/dt", "Lokal inersiya", "Statsionar oqim"],
       ["rho (v.grad)v", "Konvektiv inersiya (nochiziqli)", "Stoks oqimi (Re << 1)"],
       ["-grad p", "Bosim kuchi", "Hech qachon tushmaydi"],
       ["mu grad^2 v", "Yopishqoq diffuziya", "Eyler tenglamalari (ideal)"],
       ["rho g", "Og'irlik", "Mikrooqimlar, gorizontal oqim"]])

table("Turli suyuqliklarda yopishqoqlik (20 C)",
      ["Suyuqlik", "mu, Pa*s", "rho, kg/m3", "nu, mm2/s"],
      [[name, m_, r_, round(m_/r_*1e6, 3)]
       for name, m_, r_ in [
           ("Havo", 1.81e-5, 1.20),
           ("Suv", 1.00e-3, 998.0),
           ("Etil spirti", 1.20e-3, 789.0),
           ("Qon (taxminan)", 3.5e-3, 1060.0),
           ("Motor moyi SAE30", 0.29, 890.0),
           ("Glitserin", 1.49, 1260.0)]])
note("Havoning kinematik yopishqoqligi suvnikidan 15 marta katta: "
     "impuls diffuziyasi gazda tezroq boradi, garchi gaz 'suyuqroq' tuyulsa ham.")
''',
                parameters=[
                    p("rho", "Zichlik ρ", 0.5, 1500.0, 880.0, 0.5, "kg/m³"),
                    p("mu", "Dinamik yopishqoqlik μ", 1e-5, 2.0, 0.15, 1e-5, "Pa·s"),
                    p("U", "Plastina tezligi U", 0.01, 20.0, 3.0, 0.01, "m/s"),
                    p("h", "Qatlam qalinligi h", 0.02, 10.0, 0.2, 0.02, "mm"),
                    p("L", "Xarakterli uzunlik L", 0.001, 2.0, 0.1, 0.001, "m"),
                ],
                expected_output=(
                    "ν = 170,5 mm²/s, Re_h = 3,52; τ = 2250 Pa, kuch 225 N, "
                    "isrof quvvati 675 W. Nostatsionar yechim 3h²/ν ≈ 1,06 ms "
                    "dan keyin chiziqli profilga 0,1 % dan yaxshi yaqinlashadi."
                ),
            ),
            visual=vis(
                kind="Yopishqoq oqim va hadlar balansi",
                tool="React/SVG + Matplotlib",
                description=(
                    "No-slip sharti, tezlik profilining vaqt bo'yicha "
                    "rivojlanishi va Navye–Stoks hadlarining nisbiy "
                    "kattaligi diagrammasi."
                ),
                how_to_draw=(
                    "React/SVG: ikki gorizontal plastina (yuqorigisi "
                    "strelka bilan $U$ tezlikda harakatlanmoqda), orasida "
                    "suyuqlik. Tezlik profili — chapdan o'ngga qarab "
                    "uzunligi $u(y)$ ga mutanosib strelkalar qatori, "
                    "uchlari `<polyline>` bilan tutashtiriladi. Vaqt "
                    "slayderi `snapshots` orasida o'tadi: boshida profil "
                    "faqat yuqori devorga yopishgan ingichka qatlamda, "
                    "so'ng asta-sekin pastga 'tarqaladi' — diffuziya shu "
                    "yerda ko'rinadi. Devorda tezlik aniq nolga teng "
                    "bo'lishini ko'rsatish uchun eng pastki strelka nuqta "
                    "sifatida chiziladi va 'no-slip' yorlig'i qo'yiladi. "
                    "Hadlar balansi uchun gorizontal ustun diagramma: "
                    "log masshtabda inersiya, yopishqoqlik va og'irlik "
                    "hadlari; hukmron had to'q rangda ajratiladi."
                ),
            ),
            interp=(
                "Yopishqoqlik jadvalidagi eng qarama-qarshi natija — havo "
                "va suvning taqqoslanishi. Dinamik yopishqoqlikda suv "
                "havodan 55 marta 'qovushqoqroq', lekin **kinematik** "
                "yopishqoqlikda havo suvdan 15 marta ustun. Chunki "
                "$\\nu = \\mu/\\rho$ da zichlik maxrajda turadi, havo esa "
                "800 marta yengil. Amaliy oqibat: bir xil o'lcham va "
                "tezlikda havo oqimi suv oqimiga qaraganda **past** Reynolds "
                "soniga ega bo'ladi, ya'ni turbulentlikka kechroq o'tadi. "
                "Nostatsionar hisob esa diffuziya vaqti masshtabini "
                "tasdiqlaydi: $t \\sim h^2/\\nu$. Bu kvadratik bog'liqlik "
                "muhim — qatlamni ikki marta qalinlashtirish turg'un holatga "
                "chiqish vaqtini **to'rt marta** uzaytiradi. Shuning uchun "
                "mikroflyuidikada (h ~ mikron) oqim deyarli oniy ravishda "
                "turg'unlashadi, okean miqyosida esa diffuziya amalda hech "
                "qachon ulgurmaydi va turbulent aralashuv hukmron bo'ladi."
            ),
            mistakes=[
                "Ideal suyuqlikdagi sirpanish shartini yopishqoq oqimga "
                "ko'chirish. Yopishqoq suyuqlikda devorda **to'liq** "
                "no-slip: urinma tezlik ham nolga teng.",
                "$\\mu$ va $\\nu$ ni aralashtirish. Reynolds sonida "
                "$\\nu = \\mu/\\rho$, kuchlanishda esa $\\mu$ ishlatiladi; "
                "birliklari ham har xil (Pa·s va m²/s).",
                "Yopishqoq hadni $\\mu\\nabla^2\\mathbf{v}$ deb yozib, "
                "$\\mu$ ning o'zgaruvchanligini unutish. $\\mu$ haroratga "
                "bog'liq bo'lsa, to'g'ri shakl "
                "$\\nabla\\cdot(2\\mu\\mathbf{D})$ bo'ladi.",
                "Yuqori Reynolds sonida yopishqoqlikni butunlay tashlab "
                "yuborish. Bu Dalamber paradoksiga olib keladi: chegaraviy "
                "qatlam va ajralish (separation) yo'qoladi, qarshilik "
                "kuchi nol chiqadi.",
            ],
            quiz=[
                q("Nyuton suyuqligi ta'rifini bering.",
                  "Yopishqoq kuchlanish deformatsiya tezligiga chiziqli "
                  "bog'liq bo'lgan suyuqlik: $\\tau_{ij} = 2\\mu D_{ij}$. "
                  "Koeffitsient $\\mu$ tezlik gradiyentiga bog'liq emas.",
                  "konseptual"),
                q("Navye–Stoks tenglamasining qaysi hadi nochiziqli va "
                  "nima uchun bu muhim?",
                  "Konvektiv had $(\\mathbf{v}\\cdot\\nabla)\\mathbf{v}$. "
                  "Aynan u turbulentlikni, ko'p yechimlikni va umumiy "
                  "analitik yechimning yo'qligini keltirib chiqaradi.",
                  "konseptual"),
                q("Suv uchun $U = 2$ m/s, $D = 50$ mm. Re ni toping "
                  "($\\nu = 10^{-6}$ m²/s).",
                  "$\\mathrm{Re} = 2 \\cdot 0{,}05/10^{-6} = 10^5$ — "
                  "turbulent rejim (quvurda $\\mathrm{Re}_{cr} \\approx 2300$).",
                  "hisob"),
                q("Dalamber paradoksi nima va u qanday hal qilingan?",
                  "Ideal suyuqlikda jismga qarshilik nol chiqishi. Prandtl "
                  "(1904) chegaraviy qatlam g'oyasi bilan hal qildi: "
                  "yopishqoqlik butun sohada emas, devor yonidagi ingichka "
                  "qatlamda hal qiluvchi.", "talqin"),
                q("Kodda `dt = 0.2*dy**2/nu` sharti nimani ta'minlaydi?",
                  "Aniq (explicit) diffuziya sxemasining turg'unligini: "
                  "$\\nu\\Delta t/\\Delta y^2 \\le 1/2$. 0,2 koeffitsienti "
                  "zaxira bilan olingan.", "kod"),
                q("Nima uchun havoning kinematik yopishqoqligi suvnikidan "
                  "katta?",
                  "$\\nu = \\mu/\\rho$; havoning $\\mu$ si 55 marta kichik, "
                  "lekin $\\rho$ si 830 marta kichik. Natijada $\\nu$ "
                  "15 marta katta chiqadi.", "talqin"),
            ],
            bridge=(
                "Navye–Stoks tenglamalarining umumiy analitik yechimi yo'q — "
                "bu Millennium mukofoti muammolaridan biri. Lekin bir necha "
                "sodda geometriyada aniq yechim mavjud va ular butun "
                "gidravlikaning asosi bo'lib xizmat qiladi. Keyingi mavzuda "
                "aynan shularni — Kuett va Puazeyl oqimlarini — quramiz."
            ),
            research=(
                "Nonyuton suyuqliklarni o'rganing: quvvat qonuni "
                "$\\tau = K\\dot{\\gamma}^n$ (n < 1 — psevdoplastik, "
                "n > 1 — dilatant), Bingem plastik "
                "$\\tau = \\tau_0 + \\mu_p\\dot{\\gamma}$ va Herschel–Bulkley "
                "modellari. Quvurdagi oqim uchun har bir model bilan tezlik "
                "profilini chiqaring va taqqoslang. Bingem suyuqligida "
                "paydo bo'ladigan 'qattiq o'zak' (plug flow) hodisasini "
                "tushuntiring va uning tish pastasi, beton yoki burg'ulash "
                "loyqasini quvur orqali haydashdagi ahamiyatini tahlil qiling."
            ),
            manim_ref=manim(
                scene="NavierStokesScene",
                module="manim/scenes/tmm_fluid.py",
                title="Yopishqoq diffuziya va no-slip",
                summary=(
                    "Birdan harakatga kelgan plastina yonida tezlik profili "
                    "asta-sekin suyuqlik ichiga 'tarqaladi'; diffuziya "
                    "chuqurligi $\\sqrt{\\nu t}$ qonuni bilan o'sishi "
                    "ko'rsatiladi."
                ),
            ),
        ),
    ),

    # ------------------------------------------------------------------ tmm-28
    Topic(
        id="tmm-28",
        subject_id=S, module_id=M, order=28,
        title="Laminar oqimning aniq yechimlari: Kuett, Puazeyl va gidravlik qarshilik",
        description=(
            "Navye–Stoks tenglamalarining to'liq rivojlangan laminar "
            "oqimdagi aniq yechimlari: tekis kanal, doiraviy quvur, "
            "Hagen–Puazeyl qonuni va Darsi–Veysbax yo'qotish formulasi."
        ),
        learning_objective=(
            "To'liq rivojlangan oqim uchun Navye–Stoks tenglamalarini "
            "soddalashtirish, tezlik profilini integrallash, sarf va "
            "ishqalanish koeffitsientini hisoblash hamda quvurdagi bosim "
            "yo'qotishini aniqlash."
        ),
        prerequisites=["tmm-27"],
        mathematical_core=(
            "Bir o'lchovli ODE $\\mu\\,d^2u/dy^2 = dp/dx$, silindrik "
            "koordinatalarda "
            "$\\frac{\\mu}{r}\\frac{d}{dr}\\big(r\\frac{du}{dr}\\big) = "
            "\\frac{dp}{dx}$, integrallash va sarf $Q = \\int u\\,dA$."
        ),
        engineering_application=(
            "Quvur tarmoqlari va nasos tanlash, moylash podshipniklari, "
            "kapillyar viskozimetr, mikroflyuidika, tibbiy kateter va "
            "infuziya tizimlari."
        ),
        computational_component=(
            "Tezlik profilini sonli va analitik hisoblash, sarfni "
            "integrallash, $f = 64/\\mathrm{Re}$ munosabatini tekshirish, "
            "Darsi–Veysbax bo'yicha nasos quvvatini baholash."
        ),
        visualization_component=(
            "Parabolik va chiziqli tezlik profillari, quvur kesimidagi "
            "kuchlanish taqsimoti, Mudi diagrammasining laminar sohasi."
        ),
        research_extension=(
            "Kirish uchastkasi (entrance region) masalasini o'rganing: "
            "profil qancha masofada to'liq rivojlanadi va bu uzunlikda "
            "qo'shimcha bosim yo'qotishi qanday hisoblanadi?"
        ),
        difficulty="murakkab",
        previous_link=(
            "tmm-27 da Navye–Stoks tenglamalari to'liq shaklda olindi. "
            "Ular umumiy holda yechilmaydi, lekin geometriya sodda va "
            "oqim to'liq rivojlangan bo'lsa, nochiziqli had aynan nolga "
            "aylanadi va aniq yechim topiladi."
        ),
        next_topic="tmm-29",
        estimated_minutes=95,
        tags=["Puazeyl", "Kuett", "laminar", "gidravlika"],
        lesson=_lesson(
            problem=(
                "Kasalxonada tomchilatib yuborish tizimi loyihalanmoqda: "
                "dori eritmasi 1,2 m balandlikdagi idishdan 1,5 m "
                "uzunlikdagi, 0,8 mm ichki diametrli kateter orqali "
                "oqadi. Kerakli sarf — soatiga 120 ml. Bu geometriya "
                "kerakli sarfni beradimi? Diametrni 0,1 mm o'zgartirish "
                "sarfga qanchalik ta'sir qiladi? Javob kutilgandan ancha "
                "keskin: sarf diametrning **to'rtinchi** darajasiga "
                "mutanosib. Nega aynan to'rtinchi?"
            ),
            concepts=[
                c("To'liq rivojlangan oqim (fully developed flow)",
                  "Tezlik profili oqim yo'nalishi bo'ylab o'zgarmaydigan "
                  "holat: $\\partial u/\\partial x = 0$. Bunda konvektiv "
                  "had aynan nolga aylanadi va tenglama chiziqli bo'lib qoladi."),
                c("Kuett oqimi (Couette flow)",
                  "Devor harakati tufayli yuzaga keladigan oqim; bosim "
                  "gradiyenti bo'lmasa profil chiziqli."),
                c("Puazeyl oqimi (Poiseuille flow)",
                  "Bosim gradiyenti tufayli yuzaga keladigan oqim; "
                  "profil parabolik."),
                c("Hagen–Puazeyl qonuni",
                  "Doiraviy quvurda $Q = \\frac{\\pi R^4\\Delta p}{8\\mu L}$ — "
                  "sarf radiusning to'rtinchi darajasiga mutanosib."),
                c("Darsi–Veysbax formulasi",
                  "$h_f = f\\frac{L}{D}\\frac{V^2}{2g}$ — quvurdagi napor "
                  "yo'qotishi; laminar oqimda $f = 64/\\mathrm{Re}$."),
                c("Gidravlik diametr (hydraulic diameter)",
                  "Nodoiraviy kesim uchun ekvivalent o'lcham: "
                  "$D_h = 4A/P$, bu yerda $P$ — ho'llanuvchi perimetr."),
            ],
            derivation=[
                d("1. To'liq rivojlangan oqim taxminlari",
                  r"v = w = 0, \quad u = u(y)\ \text{yoki}\ u(r), \quad "
                  r"\frac{\partial u}{\partial x} = 0",
                  "Uzluksizlik tenglamasi $\\partial u/\\partial x = 0$ ni "
                  "beradi (chunki $v = w = 0$). Demak profil $x$ bo'ylab "
                  "o'zgarmaydi."),
                d("2. Konvektiv had nolga aylanadi",
                  r"(\mathbf{v}\cdot\nabla)\mathbf{v} = u\frac{\partial u}"
                  r"{\partial x}\mathbf{i} = 0",
                  "Navye–Stoksning yagona nochiziqli hadi yo'qoladi. "
                  "Aynan shu sabab bu masalalarni aniq yechish mumkin."),
                d("3. Tekis kanal uchun tenglama",
                  r"0 = -\frac{dp}{dx} + \mu\frac{d^2u}{dy^2} \;\Longrightarrow\; "
                  r"\frac{d^2u}{dy^2} = \frac{1}{\mu}\frac{dp}{dx} = \text{const}",
                  "$y$ va $z$ tenglamalari $\\partial p/\\partial y = "
                  "\\partial p/\\partial z = 0$ ni beradi, demak $p = p(x)$ "
                  "va $dp/dx$ doimiy."),
                d("4. Ikki marta integrallash va chegaraviy shartlar",
                  r"u(y) = \frac{1}{2\mu}\frac{dp}{dx}y^2 + C_1y + C_2; \quad "
                  r"u(0) = 0,\ u(h) = U",
                  "Umumiy yechim parabola. Ikki chegaraviy shart ikki "
                  "doimiyni aniqlaydi."),
                d("5. Umumiy Kuett–Puazeyl profili",
                  r"u(y) = U\frac{y}{h} - \frac{h^2}{2\mu}\frac{dp}{dx}"
                  r"\frac{y}{h}\Big(1 - \frac{y}{h}\Big)",
                  "Superpozitsiya: chiziqli Kuett qismi + parabolik Puazeyl "
                  "qismi. Tenglama chiziqli bo'lgani uchun ularni qo'shish mumkin."),
                d("6. Doiraviy quvur: silindrik koordinatalarda",
                  r"\frac{\mu}{r}\frac{d}{dr}\Big(r\frac{du}{dr}\Big) "
                  r"= \frac{dp}{dx} \;\Longrightarrow\; "
                  r"u(r) = \frac{1}{4\mu}\frac{dp}{dx}\big(r^2 - R^2\big)",
                  "Integrallash: $r\\,du/dr = \\frac{1}{2\\mu}\\frac{dp}{dx}r^2 "
                  "+ C_1$. Markazda ($r = 0$) tezlik chekli bo'lishi shartidan "
                  "$C_1 = 0$; $u(R) = 0$ dan ikkinchi doimiy."),
                d("7. Hagen–Puazeyl sarfi",
                  r"Q = \int_0^R u(r)\,2\pi r\,dr = \frac{\pi R^4}{8\mu}"
                  r"\Big(-\frac{dp}{dx}\Big) = \frac{\pi R^4\Delta p}{8\mu L}",
                  "$R^4$ bog'liqligining kelib chiqishi: profil $R^2$ ga "
                  "mutanosib, yuza ham $R^2$ ga — ko'paytmasi $R^4$. "
                  "Diametrni 20 % oshirish sarfni 2 marta oshiradi."),
                d("8. Darsi ishqalanish koeffitsienti",
                  r"h_f = \frac{\Delta p}{\rho g} = f\frac{L}{D}\frac{V^2}{2g} "
                  r"\;\Longrightarrow\; f = \frac{64}{\mathrm{Re}}",
                  "O'rtacha tezlik $V = Q/(\\pi R^2) = u_{\\max}/2$ ni "
                  "qo'yib, Darsi–Veysbax ta'rifi bilan taqqoslaymiz. "
                  "Natija — laminar oqimning universal qonuni, g'adir-budirlikka "
                  "umuman bog'liq emas."),
            ],
            meaning=(
                "$Q \\propto R^4$ — bu butun gidravlikadagi eng keskin "
                "bog'liqliklardan biri va u ikki mustaqil $R^2$ dan "
                "tug'iladi: birinchisi kesim yuzasidan, ikkinchisi "
                "profilning o'zidan (tor quvurda devor butun oqimni "
                "sekinlashtiradi). Tibbiyotdagi oqibati dramatik: "
                "qon tomiri devori 10 % qalinlashsa, ichki radius 10 % "
                "kamayadi va qon oqimi $0{,}9^4 = 0{,}656$ ga, ya'ni "
                "**34 % ga** tushadi. Yurak buni qoplash uchun bosimni "
                "oshirishi kerak — gipertoniyaning mexanik ildizi shu. "
                "$f = 64/\\mathrm{Re}$ munosabatining chiroyi esa "
                "boshqacha: laminar oqimda quvur ichki sirtining "
                "g'adir-budirligi **umuman ahamiyatsiz**. Sababi — "
                "devordagi suyuqlik qatlami harakatsiz (no-slip) va "
                "mikroskopik do'ngliklar shu harakatsiz qatlam ichida "
                "'ko'milib' qoladi. Turbulent oqimda esa bu qatlam juda "
                "ingichka bo'lib qoladi va g'adir-budirlik hal qiluvchi "
                "bo'ladi — Mudi diagrammasidagi ikki sohaning farqi aynan shu."
            ),
            equations=[
                eq(r"u(r) = u_{\max}\Big(1 - \frac{r^2}{R^2}\Big), \quad "
                   r"u_{\max} = \frac{\Delta p\,R^2}{4\mu L}",
                   "Doiraviy quvurdagi parabolik tezlik profili.",
                   "Puazeyl profili"),
                eq(r"Q = \frac{\pi R^4\,\Delta p}{8\mu L}",
                   "Hagen–Puazeyl qonuni (sarf).", "Hagen–Puazeyl"),
                eq(r"h_f = f\frac{L}{D}\frac{V^2}{2g}, \qquad "
                   r"f = \frac{64}{\mathrm{Re}}\ (\text{laminar})",
                   "Darsi–Veysbax napor yo'qotishi va laminar ishqalanish "
                   "koeffitsienti.", "Darsi–Veysbax"),
                eq(r"\tau_w = \mu\Big|\frac{du}{dr}\Big|_{r=R} "
                   r"= \frac{\Delta p\,R}{2L}",
                   "Devordagi urinma kuchlanish.", "Devor kuchlanishi"),
            ],
            conditions=(
                "**Devorda:** $u = 0$ (no-slip) — barcha yechimlarning asosi.\n\n"
                "**Quvur o'qida:** $du/dr = 0$ (simmetriya) yoki "
                "$u$ chekli bo'lishi sharti — ikkalasi ekvivalent va "
                "$C_1 = 0$ ni beradi.\n\n"
                "**Yuklanish:** $dp/dx$ berilgan (bosim bilan haydash) "
                "yoki $Q$ berilgan (nasos bilan haydash) — ikkala "
                "qo'yilish ekvivalent.\n\n"
                "**Qo'llanish shartlari:**\n"
                "- $\\mathrm{Re} < 2300$ (doiraviy quvur uchun) — aks "
                "holda oqim turbulent va bu yechim yaroqsiz;\n"
                "- $x > L_e \\approx 0{,}06\\,\\mathrm{Re}\\,D$ — kirish "
                "uchastkasidan keyin, profil to'liq rivojlangan;\n"
                "- Statsionar oqim, doimiy $\\mu$ va $\\rho$."
            ),
            worked=WorkedExample(
                statement=(
                    "Tibbiy kateter: $D = 0{,}8$ mm, $L = 1{,}5$ m, dori "
                    "eritmasi ($\\mu = 1{,}2\\times10^{-3}$ Pa·s, "
                    "$\\rho = 1010$ kg/m³) idishdan $H = 1{,}2$ m "
                    "balandlikdan oqadi. (a) Sarfni toping. (b) Reynolds "
                    "sonini tekshiring. (c) Soatiga 120 ml olish uchun "
                    "diametr qancha bo'lishi kerak?"
                ),
                given=[
                    r"D = 0{,}8\ \text{mm},\ R = 4\times10^{-4}\ \text{m}",
                    r"L = 1{,}5\ \text{m},\ H = 1{,}2\ \text{m}",
                    r"\mu = 1{,}2\times10^{-3}\ \text{Pa·s},\ \rho = 1010\ \text{kg/m}^3",
                ],
                steps=[
                    st(r"\Delta p = \rho g H = 1010 \cdot 9{,}81 \cdot 1{,}2 "
                       r"= 11\,890\ \text{Pa}",
                       "Gidrostatik bosim (tmm-25). Tezlik napori kichik "
                       "deb e'tiborsiz qoldiriladi."),
                    st(r"Q = \frac{\pi R^4\Delta p}{8\mu L} = "
                       r"\frac{\pi (4\times10^{-4})^4 \cdot 11\,890}"
                       r"{8 \cdot 1{,}2\times10^{-3} \cdot 1{,}5}",
                       "Hagen–Puazeyl qonuni. $R^4 = 2{,}56\\times10^{-14}$ m⁴."),
                    st(r"Q = \frac{\pi \cdot 2{,}56\times10^{-14} \cdot 11\,890}"
                       r"{1{,}44\times10^{-2}} = 6{,}64\times10^{-8}\ \text{m}^3\text{/s}",
                       "Sekundiga 0,0664 ml."),
                    st(r"Q = 6{,}64\times10^{-8} \cdot 3600 \cdot 10^6 "
                       r"= 239\ \text{ml/soat}",
                       "Kerakli 120 ml/soat dan ikki marta ko'p — demak "
                       "oqim regulyatori bilan bo'g'ish kerak yoki "
                       "kateter ingichkaroq."),
                    st(r"V = \frac{Q}{\pi R^2} = \frac{6{,}64\times10^{-8}}"
                       r"{5{,}027\times10^{-7}} = 0{,}132\ \text{m/s}; \quad "
                       r"\mathrm{Re} = \frac{1010 \cdot 0{,}132 \cdot 8\times10^{-4}}"
                       r"{1{,}2\times10^{-3}} = 88{,}9",
                       "$\\mathrm{Re} = 89 \\ll 2300$ — oqim ishonchli "
                       "laminar, yechim o'rinli."),
                    st(r"\frac{Q_2}{Q_1} = \Big(\frac{D_2}{D_1}\Big)^4 "
                       r"\;\Rightarrow\; D_2 = 0{,}8\Big(\frac{120}{239}\Big)^{1/4} "
                       r"= 0{,}8 \cdot 0{,}8413 = 0{,}673\ \text{mm}",
                       "To'rtinchi daraja ildizi. Diametrni atigi 16 % "
                       "kamaytirish sarfni ikki marta tushiradi."),
                ],
                answer=(
                    "$Q = 239$ ml/soat, $V = 0{,}132$ m/s, "
                    "$\\mathrm{Re} = 89$ (laminar); 120 ml/soat uchun "
                    "$D = 0{,}67$ mm kerak."
                ),
                engineering_note=(
                    "Amalda tomchilatib yuborish tizimlarida diametr "
                    "o'zgartirilmaydi — o'rniga rolikli klapan (roller "
                    "clamp) bilan naycha qisilib, mahalliy qarshilik "
                    "kiritiladi. Sababi aniq: $Q \\propto D^4$ bog'liqligi "
                    "shunchalik keskinki, ishlab chiqarishdagi 5 % "
                    "diametr xatosi sarfda 22 % xato beradi — bunday "
                    "aniqlikni ta'minlash qimmat. Sozlanadigan qarshilik "
                    "esa arzon va ishonchli."
                ),
            ),
            computation=Computation(
                caption=(
                    "Kuett–Puazeyl profillari, Hagen–Puazeyl sarfi, "
                    "$f = 64/\\mathrm{Re}$ tekshiruvi va nasos quvvati hisobi."
                ),
                code='''"""Laminar oqim: Kuett, Puazeyl va gidravlik qarshilik."""
import numpy as np
from labkit import PARAMS, note, series, table, value

D = float(PARAMS.get("D", 0.8))/1000.0      # quvur diametri, m
Lp = float(PARAMS.get("Lp", 1.5))           # quvur uzunligi, m
dp = float(PARAMS.get("dp", 11890.0))       # bosim farqi, Pa
mu = float(PARAMS.get("mu", 1.2e-3))        # Pa*s
rho = float(PARAMS.get("rho", 1010.0))      # kg/m^3
Uw = float(PARAMS.get("Uw", 0.0))           # Kuett: devor tezligi, m/s
hc = float(PARAMS.get("hc", 1.0))/1000.0    # tekis kanal balandligi, m
g = 9.81

R = D/2
trapz = np.trapezoid if hasattr(np, "trapezoid") else np.trapz

# --- Doiraviy quvur: Hagen-Puazeyl ---
umax = dp*R**2/(4*mu*Lp)
Q = np.pi*R**4*dp/(8*mu*Lp)
V = Q/(np.pi*R**2)
Re = rho*V*D/mu
tau_w = dp*R/(2*Lp)
f_darcy = 64/Re if Re > 0 else float("inf")

value("Maksimal tezlik u_max", umax, "m/s")
value("O'rtacha tezlik V", V, "m/s")
value("V/u_max", V/umax if umax > 0 else 0.0, "—")
value("Sarf Q", Q*1e6, "ml/s")
value("Sarf Q", Q*3.6e9, "ml/soat")
value("Reynolds soni", Re, "—")
value("Devor kuchlanishi tau_w", tau_w, "Pa")
value("Darsi koeffitsienti f = 64/Re", f_darcy, "—")

if Re < 2300:
    note(f"Re = {Re:.1f} < 2300 — oqim LAMINAR, Hagen-Puazeyl yechimi o'rinli.")
else:
    note(f"Re = {Re:.1f} >= 2300 — oqim turbulent bo'lishi mumkin! "
         f"Bu yechim endi yaroqsiz, Kolbruk formulasi kerak.")

# Kirish uchastkasi
Le = 0.06*Re*D
value("Kirish uchastkasi L_e", Le*1000, "mm")
value("L_e / L", Le/Lp, "—")
if Le > 0.1*Lp:
    note(f"Kirish uchastkasi quvur uzunligining {100*Le/Lp:.1f} % ini "
         f"egallaydi — to'liq rivojlangan oqim taxmini shubhali.")

# --- Profil ---
r = np.linspace(-R, R, 300)
u_pois = umax*(1 - (r/R)**2)
series("Puazeyl profili u(r)", u_pois.tolist(), (r*1000).tolist(),
       xlabel="Tezlik u, m/s", ylabel="r, mm")

# Sonli integrallash bilan sarfni tekshirish
rr = np.linspace(0.0, R, 2000)
Q_num = float(trapz(umax*(1 - (rr/R)**2)*2*np.pi*rr, rr))
note(f"Analitik Q = {Q*1e6:.5f} ml/s, sonli integral Q = {Q_num*1e6:.5f} ml/s, "
     f"farq {abs(Q_num-Q)/Q*100:.5f} %.")

# Darsi-Veysbax tekshiruvi
hf = f_darcy*(Lp/D)*V**2/(2*g)
dp_check = rho*g*hf
note(f"Darsi-Veysbax bo'yicha dp = {dp_check:.2f} Pa, berilgan dp = {dp:.2f} Pa "
     f"— farq {abs(dp_check-dp)/dp*100:.4f} %. f = 64/Re munosabati tasdiqlandi.")
value("Napor yo'qotishi h_f", hf, "m")
value("Nasos quvvati (Q*dp)", Q*dp, "W")

# --- D^4 bog'liqligi ---
D_range = np.linspace(0.3, 3.0, 200)/1000.0
Q_range = np.pi*(D_range/2)**4*dp/(8*mu*Lp)*3.6e9
series("Q(D) — to'rtinchi daraja", (D_range*1000).tolist(), Q_range.tolist(),
       xlabel="Diametr D, mm", ylabel="Sarf Q, ml/soat")
note("Diametrni 20 % oshirish sarfni 1.2^4 = 2.07 marta, ya'ni ikki "
     "barobardan ko'proq oshiradi.")

# --- Tekis kanal: umumiy Kuett-Puazeyl ---
dpdx = -dp/Lp
y = np.linspace(0.0, hc, 300)
u_gen = Uw*(y/hc) - (hc**2/(2*mu))*dpdx*(y/hc)*(1 - y/hc)
series("Kuett-Puazeyl profili (tekis kanal)", u_gen.tolist(), (y*1000).tolist(),
       xlabel="Tezlik u, m/s", ylabel="y, mm")
q_chan = float(trapz(u_gen, y))
value("Kanal solishtirma sarfi (1 m kenglikka)", q_chan*1e6, "ml/(s*m)")

# Sof Kuett va sof Puazeyl komponentalari
series("Kuett komponenta", (Uw*y/hc).tolist(), (y*1000).tolist(),
       xlabel="Tezlik u, m/s", ylabel="y, mm")
series("Puazeyl komponenta",
       (-(hc**2/(2*mu))*dpdx*(y/hc)*(1 - y/hc)).tolist(), (y*1000).tolist(),
       xlabel="Tezlik u, m/s", ylabel="y, mm")

table("Laminar oqimning klassik yechimlari",
      ["Geometriya", "Profil", "f*Re", "V/u_max"],
      [["Doiraviy quvur", "Parabolik", 64, round(0.5, 3)],
       ["Cheksiz tekis kanal", "Parabolik", 96, round(2/3, 3)],
       ["Kvadrat kanal", "Taxminan parabolik", 57, "~0.48"],
       ["Halqasimon (ingichka)", "Parabolik", 96, round(2/3, 3)],
       ["Sof Kuett", "Chiziqli", "—", round(0.5, 3)]])

table("Diametr o'zgarishining sarfga ta'siri",
      ["D o'zgarishi, %", "Q nisbati", "Izoh"],
      [[k, round((1 + k/100)**4, 4),
        "Sarf D^4 ga mutanosib"] for k in [-20, -10, -5, 5, 10, 20]])
''',
                parameters=[
                    p("D", "Quvur diametri D", 0.1, 50.0, 0.8, 0.05, "mm"),
                    p("Lp", "Quvur uzunligi L", 0.05, 100.0, 1.5, 0.05, "m"),
                    p("dp", "Bosim farqi Δp", 100.0, 500000.0, 11890.0, 100.0, "Pa"),
                    p("mu", "Dinamik yopishqoqlik μ", 1e-5, 2.0, 1.2e-3, 1e-5, "Pa·s"),
                    p("rho", "Zichlik ρ", 0.5, 1500.0, 1010.0, 0.5, "kg/m³"),
                    p("Uw", "Devor tezligi (Kuett) U", 0.0, 10.0, 0.0, 0.1, "m/s"),
                    p("hc", "Kanal balandligi h", 0.05, 20.0, 1.0, 0.05, "mm"),
                ],
                expected_output=(
                    "u_max = 0,264 m/s, V = 0,132 m/s, Q = 239 ml/soat, "
                    "Re = 88,9 (laminar), f = 0,72; Darsi–Veysbax tekshiruvi "
                    "1e-4 % dan yaxshi mos keladi; kirish uchastkasi 4,3 mm."
                ),
            ),
            visual=vis(
                kind="Laminar tezlik profillari",
                tool="React/SVG",
                description=(
                    "Quvur kesimidagi parabolik profil, kanaldagi "
                    "Kuett+Puazeyl superpozitsiyasi va $Q(D)$ egri chizig'i."
                ),
                how_to_draw=(
                    "React/SVG: quvur kesimi ikkita gorizontal devor chizig'i "
                    "bilan; profil — chapdan o'ngga qarab uzunligi $u(r)$ ga "
                    "mutanosib 15–20 ta strelka, uchlari silliq parabola "
                    "bilan tutashtiriladi (`<path>` `Q` buyrug'i bilan). "
                    "Devor yonidagi strelkalar nolga intiladi. Kuett+Puazeyl "
                    "panelida uchta profil bir grafikda: Kuett (chiziqli, "
                    "punktir), Puazeyl (parabolik, punktir) va ularning "
                    "yig'indisi (uzluksiz, qalin) — superpozitsiya prinsipi "
                    "ko'z bilan ko'rinadi. Bosim gradiyenti ishorasini "
                    "manfiy qilish mumkin, shunda teskari oqim zonasi "
                    "paydo bo'ladi va uni boshqa rangda bo'yash kerak. "
                    "$Q(D)$ grafigi log–log o'qlarda chiziladi — u yerda "
                    "$D^4$ bog'liqligi qiyaligi 4 bo'lgan to'g'ri chiziq "
                    "bo'lib ko'rinadi, bu daraja ko'rsatkichini vizual "
                    "tasdiqlaydi."
                ),
            ),
            interp=(
                "Jadvaldagi $f\\,\\mathrm{Re}$ ustuni muhim umumlashma "
                "beradi: laminar oqimda bu ko'paytma har bir geometriya "
                "uchun **doimiy son**, faqat qiymati farq qiladi (quvurda "
                "64, tekis kanalda 96, kvadrat kanalda 57). Demak "
                "gidravlik diametr tushunchasi taxminiy: u geometriyani "
                "qisman hisobga oladi, lekin to'liq emas. Sonli va "
                "analitik sarfning $10^{-5}$ % farqi esa integrallashning "
                "to'g'riligini tasdiqlaydi. Diametr jadvali eng keskin "
                "muhandislik xulosasini beradi: $-5$ % diametr $-18{,}5$ % "
                "sarf, $+5$ % diametr esa $+21{,}6$ % sarf. Shuning uchun "
                "mikroflyuidik qurilmalarda kanal o'lchamining ishlab "
                "chiqarish aniqligi hal qiluvchi — mikrondagi xato "
                "o'nlab foizli sarf xatosiga aylanadi. Kirish uchastkasi "
                "hisobi ham ogohlantiruvchi: $\\mathrm{Re}$ katta bo'lsa "
                "$L_e = 0{,}06\\,\\mathrm{Re}\\,D$ quvur uzunligiga "
                "taqqoslanadigan bo'lib qoladi va to'liq rivojlangan oqim "
                "taxmini buziladi."
            ),
            mistakes=[
                "O'rtacha tezlik $V$ va maksimal tezlik $u_{\\max}$ ni "
                "aralashtirish. Doiraviy quvurda $V = u_{\\max}/2$, tekis "
                "kanalda esa $V = 2u_{\\max}/3$ — Reynolds sonida "
                "$V$ ishlatiladi.",
                "Laminar $f = 64/\\mathrm{Re}$ formulasini turbulent "
                "rejimda qo'llash. $\\mathrm{Re} > 2300$ da Kolbruk yoki "
                "Blazius formulasi kerak, g'adir-budirlik ham hisobga olinadi.",
                "$Q \\propto D^4$ o'rniga $D^2$ deb o'ylash (faqat yuza "
                "bo'yicha). Profilning o'zi ham $R^2$ ga mutanosib — "
                "shuning uchun to'rtinchi daraja chiqadi.",
                "Kirish uchastkasini e'tiborsiz qoldirish. Qisqa quvurda "
                "($L < L_e$) profil to'liq rivojlanmaydi va haqiqiy "
                "yo'qotish hisoblangandan katta bo'ladi.",
            ],
            quiz=[
                q("Nima uchun to'liq rivojlangan oqimda Navye–Stoks "
                  "tenglamasi chiziqli bo'lib qoladi?",
                  "Chunki $\\partial u/\\partial x = 0$ va $v = w = 0$ "
                  "bo'lgani uchun konvektiv had "
                  "$(\\mathbf{v}\\cdot\\nabla)\\mathbf{v}$ aynan nolga "
                  "aylanadi — u yagona nochiziqli had edi.", "konseptual"),
                q("Sarf diametrning nechanchi darajasiga mutanosib va nega?",
                  "To'rtinchi darajasiga. Kesim yuzasi $R^2$ ga, tezlik "
                  "profilining o'zi ham $R^2$ ga mutanosib; ko'paytmasi "
                  "$R^4$.", "konseptual"),
                q("$\\mathrm{Re} = 800$ bo'lsa, Darsi koeffitsienti qancha?",
                  "$f = 64/800 = 0{,}08$.", "hisob"),
                q("Nima uchun laminar oqimda quvur g'adir-budirligi "
                  "ahamiyatsiz?",
                  "Devorda no-slip sharti tufayli suyuqlik harakatsiz; "
                  "mikroskopik do'ngliklar shu harakatsiz qatlam ichida "
                  "qoladi va oqimga ta'sir qilmaydi.", "talqin"),
                q("Kodda `Le = 0.06*Re*D` nimani hisoblaydi va nega muhim?",
                  "Kirish uchastkasi uzunligini — profil to'liq "
                  "rivojlanguncha bo'lgan masofani. Agar u quvur "
                  "uzunligiga taqqoslanadigan bo'lsa, Hagen–Puazeyl "
                  "yechimi yaroqsiz.", "kod"),
                q("Qon tomiri radiusi 10 % torayса, oqim necha foizga "
                  "kamayadi?",
                  "$0{,}9^4 = 0{,}656$, ya'ni 34,4 % ga kamayadi. Shu "
                  "sababli kichik torayish ham sezilarli fiziologik "
                  "oqibatga olib keladi.", "talqin"),
            ],
            bridge=(
                "Aniq yechimlar faqat sodda geometriyada mavjud. Murakkab "
                "masalalarda esa boshqa kuchli vosita ishlatiladi: "
                "o'lchamsiz sonlar va o'xshashlik nazariyasi. Ular model "
                "tajribasi natijalarini real obyektga ko'chirish va "
                "hukmron fizik mexanizmni aniqlash imkonini beradi."
            ),
            research=(
                "Kirish uchastkasi (entrance region) masalasini o'rganing. "
                "Bu yerda oqim to'liq rivojlanmagan: chegaraviy qatlam "
                "devordan o'sib boradi va markazda potensial o'zak "
                "qoladi. $L_e/D = 0{,}06\\,\\mathrm{Re}$ formulasini "
                "chegaraviy qatlam qalinligi $\\delta \\sim \\sqrt{\\nu x/U}$ "
                "dan chiqaring. Bu uchastkada qo'shimcha bosim yo'qotishi "
                "(entrance loss, $K \\approx 1{,}2$) qanday paydo bo'ladi? "
                "Sonli yechim bilan taqqoslang."
            ),
            manim_ref=manim(
                scene="PoiseuilleScene",
                module="manim/scenes/tmm_fluid.py",
                title="Puazeyl profilining shakllanishi",
                summary=(
                    "Quvurga kirgan tekis profil chegaraviy qatlamlar "
                    "o'sishi bilan asta-sekin parabolaga aylanadi; "
                    "kirish uchastkasi va to'liq rivojlangan soha "
                    "ajratib ko'rsatiladi."
                ),
            ),
        ),
    ),

    # ------------------------------------------------------------------ tmm-29
    Topic(
        id="tmm-29",
        subject_id=S, module_id=M, order=29,
        title="O'lchamsiz sonlar, o'xshashlik nazariyasi va chegaraviy qatlam",
        description=(
            "Buckingem $\\Pi$-teoremasi, Reynolds, Frud, Max, Struhal va "
            "Eyler sonlari, model tajribasining o'xshashlik shartlari hamda "
            "Prandtl chegaraviy qatlam nazariyasi va Blazius yechimi."
        ),
        learning_objective=(
            "Masalani o'lchamsizlashtirish orqali boshqaruvchi parametrlar "
            "sonini kamaytirish, model va tabiiy obyekt orasidagi "
            "o'xshashlik shartlarini yozish hamda chegaraviy qatlam "
            "qalinligi va qarshilik koeffitsientini hisoblash."
        ),
        prerequisites=["tmm-28", "tmm-27"],
        mathematical_core=(
            "Buckingem $\\Pi$-teoremasi, o'lchamlar matritsasining rangi, "
            "chegaraviy qatlam tenglamalari, o'xshashlik o'zgaruvchisi "
            "$\\eta = y\\sqrt{U/(\\nu x)}$, Blazius ODE "
            "$2f''' + ff'' = 0$."
        ),
        engineering_application=(
            "Shamol tunneli va gidrotexnika model sinovlari, kema "
            "qarshiligi (Frud + Reynolds muammosi), aerodinamik qarshilik, "
            "issiqlik almashinuvi hisobi."
        ),
        computational_component=(
            "O'lchamlar matritsasidan $\\Pi$-guruhlarni avtomatik topish, "
            "Blazius tenglamasini otish (shooting) usuli bilan yechish, "
            "chegaraviy qatlam qalinligini hisoblash."
        ),
        visualization_component=(
            "$\\Pi$-guruhlar jadvali, chegaraviy qatlamning $\\sqrt{x}$ "
            "bo'yicha o'sishi, Blazius profili va $C_f(\\mathrm{Re}_x)$ "
            "egri chizig'i."
        ),
        research_extension=(
            "Bosim gradiyentining chegaraviy qatlamga ta'sirini "
            "(Falkner–Skan yechimlari) o'rganing: oqim ajralishi "
            "qaysi shartda boshlanadi?"
        ),
        difficulty="murakkab",
        previous_link=(
            "tmm-28 dagi aniq yechimlar faqat sodda geometriyada topildi. "
            "Real masalalarda esa (qanot, kema, bino) analitik yechim yo'q. "
            "O'lchamsiz tahlil va chegaraviy qatlam nazariyasi — bunday "
            "masalalarda tartib o'rnatishning ikki asosiy vositasi."
        ),
        next_topic="tmm-30",
        estimated_minutes=100,
        tags=["o'xshashlik", "Reynolds", "chegaraviy qatlam", "Blazius"],
        lesson=_lesson(
            problem=(
                "Yangi ko'prik tayanchi loyihalanmoqda. Uning suv oqimiga "
                "qarshiligini bilish kerak, lekin haqiqiy o'lchamda sinov "
                "imkonsiz. Laboratoriyada 1:25 masshtabdagi model "
                "yasaladi. Savol: modeldagi oqim tezligini qanday tanlash "
                "kerakki, o'lchangan kuchni haqiqiy obyektga ishonch bilan "
                "ko'chirish mumkin bo'lsin? Va nima uchun kema modellarida "
                "bu masala hech qachon to'liq hal bo'lmaydi?"
            ),
            concepts=[
                c("Buckingem $\\Pi$-teoremasi (Buckingham Pi theorem)",
                  "$n$ ta o'lchamli kattalik va $k$ ta mustaqil asosiy "
                  "o'lchov birligi bo'lsa, masala $n - k$ ta o'lchamsiz "
                  "guruh bilan to'liq tavsiflanadi."),
                c("Geometrik, kinematik va dinamik o'xshashlik",
                  "Geometrik — barcha o'lchamlar bir xil nisbatda; "
                  "kinematik — tezlik maydonlari o'xshash; dinamik — "
                  "kuchlar nisbati bir xil, ya'ni barcha muhim o'lchamsiz "
                  "sonlar teng."),
                c("Reynolds soni",
                  "$\\mathrm{Re} = UL/\\nu$ — inersiya/yopishqoqlik. "
                  "Quvur, qanot, botgan jism uchun asosiy parametr."),
                c("Frud soni (Froude number)",
                  "$\\mathrm{Fr} = U/\\sqrt{gL}$ — inersiya/og'irlik. "
                  "Erkin sirtli oqimlarda (kema, kanal, to'lqin) asosiy."),
                c("Chegaraviy qatlam (boundary layer)",
                  "Devor yonidagi ingichka soha, unda tezlik noldan "
                  "erkin oqim qiymatigacha o'zgaradi. Qalinligi "
                  "$\\delta \\sim \\sqrt{\\nu x/U}$."),
                c("Blazius yechimi",
                  "Bosim gradiyentisiz tekis plastinadagi laminar "
                  "chegaraviy qatlamning o'xshashlik yechimi: "
                  "$\\delta/x = 4{,}91/\\sqrt{\\mathrm{Re}_x}$."),
            ],
            derivation=[
                d("1. O'lchamli kattaliklarni sanash",
                  r"F = F(U, L, \rho, \mu, g) \;\Rightarrow\; n = 6,\ k = 3\ (M, L, T)",
                  "Qarshilik kuchi beshta parametrga bog'liq. Asosiy "
                  "o'lchov birliklari — massa, uzunlik, vaqt."),
                d("2. Buckingem teoremasini qo'llash",
                  r"n - k = 6 - 3 = 3 \;\Rightarrow\; \Pi_1 = f(\Pi_2, \Pi_3)",
                  "Beshta parametrli masala uchta o'lchamsiz guruhga "
                  "keltiriladi. Bu — tajriba hajmini keskin kamaytiradi: "
                  "5 o'zgaruvchi bo'yicha to'liq sinov o'rniga 2 ta."),
                d("3. Guruhlarni qurish",
                  r"\Pi_1 = \frac{F}{\rho U^2 L^2} = C_D, \quad "
                  r"\Pi_2 = \frac{\rho U L}{\mu} = \mathrm{Re}, \quad "
                  r"\Pi_3 = \frac{U}{\sqrt{gL}} = \mathrm{Fr}",
                  "Takrorlanuvchi o'zgaruvchilar sifatida $U$, $L$, "
                  "$\\rho$ tanlanadi (ular uchala o'lchovni qamrab oladi "
                  "va o'zaro o'lchamsiz guruh hosil qilmaydi)."),
                d("4. O'xshashlik sharti",
                  r"C_D^{\text{model}} = C_D^{\text{tabiiy}} \iff "
                  r"\mathrm{Re}_m = \mathrm{Re}_t \ \text{va}\ "
                  r"\mathrm{Fr}_m = \mathrm{Fr}_t",
                  "Ikki o'lchamsiz son bir vaqtda teng bo'lsa, kuch "
                  "koeffitsienti ham teng bo'ladi. Bu — model sinovining "
                  "butun mantiqiy asosi."),
                d("5. Kema muammosi: ikki shartning zidligi",
                  r"\mathrm{Fr}: U_m = U_t\sqrt{\lambda}; \qquad "
                  r"\mathrm{Re}: U_m = \frac{U_t}{\lambda} "
                  r"\;\Rightarrow\; \nu_m = \nu_t\,\lambda^{3/2}",
                  "$\\lambda = L_m/L_t$ — masshtab. $\\lambda = 1/25$ da "
                  "$\\nu_m = \\nu_t/125$ kerak bo'ladi — bunday suyuqlik "
                  "yo'q. Yechim: Frud bo'yicha modellash, yopishqoq "
                  "qarshilikni esa alohida formula bilan hisoblash "
                  "(Fruda usuli)."),
                d("6. Chegaraviy qatlam tenglamalari (Prandtl, 1904)",
                  r"u\frac{\partial u}{\partial x} + v\frac{\partial u}{\partial y} "
                  r"= -\frac{1}{\rho}\frac{dp}{dx} + \nu\frac{\partial^2 u}{\partial y^2}, "
                  r"\qquad \frac{\partial p}{\partial y} \approx 0",
                  "$\\delta \\ll L$ taxminidan: $\\partial^2u/\\partial x^2 "
                  "\\ll \\partial^2u/\\partial y^2$ va ko'ndalang bosim "
                  "gradiyenti e'tiborsiz. Elliptik tizim parabolikka "
                  "aylanadi — bu yechishni ancha soddalashtiradi."),
                d("7. O'xshashlik o'zgaruvchisi va Blazius tenglamasi",
                  r"\eta = y\sqrt{\frac{U}{\nu x}}, \quad "
                  r"\psi = \sqrt{\nu x U}\,f(\eta) \;\Longrightarrow\; "
                  r"2f''' + f f'' = 0",
                  "Profil $x$ ga bog'liq, lekin $\\eta$ o'zgaruvchisida "
                  "**bitta universal egri chiziqqa** keltiriladi. PDE "
                  "oddiy differensial tenglamaga aylanadi — bu Blaziusning "
                  "1908-yildagi natijasi."),
                d("8. Qalinlik va qarshilik koeffitsienti",
                  r"\frac{\delta}{x} = \frac{4{,}91}{\sqrt{\mathrm{Re}_x}}, \qquad "
                  r"c_f = \frac{0{,}664}{\sqrt{\mathrm{Re}_x}}, \qquad "
                  r"C_D = \frac{1{,}328}{\sqrt{\mathrm{Re}_L}}",
                  "Blazius ODE ni sonli yechib, $f''(0) = 0{,}332$ "
                  "topiladi; qolgan natijalar shundan kelib chiqadi. "
                  "$C_D$ — $c_f$ ning plastina bo'ylab o'rtachasi, "
                  "$\\int_0^L x^{-1/2}dx = 2\\sqrt{L}$ tufayli aynan ikki barobar."),
            ],
            meaning=(
                "Buckingem teoremasining kuchi — u hech qanday tenglamani "
                "yechmasdan masalaning **strukturasini** aniqlaydi. "
                "Beshta parametrli masalada har biri bo'yicha 10 ta nuqta "
                "olsak, $10^5$ tajriba kerak bo'lardi; ikkita o'lchamsiz "
                "guruhga keltirilgandan keyin esa atigi $10^2$. Bu "
                "eksperimental gidrodinamikani umuman mumkin qilgan g'oya. "
                "Chegaraviy qatlamdagi $\\delta \\sim \\sqrt{\\nu x/U}$ "
                "qonuni esa tmm-27 dagi diffuziya g'oyasining to'g'ridan-"
                "to'g'ri natijasi: impuls devordan suyuqlikka diffuziya "
                "bilan tarqaladi, diffuziya vaqti $t = x/U$, tarqalish "
                "chuqurligi $\\sqrt{\\nu t}$ — shundan $\\sqrt{\\nu x/U}$ "
                "kelib chiqadi. Demak chegaraviy qatlam nazariyasi yangi "
                "fizika emas, balki bir fizikaning oqim geometriyasiga "
                "mohirona qo'llanilishi. Kema masalasidagi zidlik esa "
                "muhandislik modellashtirishning fundamental cheklovini "
                "ko'rsatadi: barcha o'lchamsiz sonlarni bir vaqtda saqlab "
                "bo'lmaydi va qaysi birini saqlash — fizik mulohaza masalasi."
            ),
            equations=[
                eq(r"\Pi_1 = \Phi(\Pi_2, \ldots, \Pi_{n-k})",
                   "Buckingem $\\Pi$-teoremasining umumiy shakli.",
                   "Π-teorema"),
                eq(r"\mathrm{Re} = \frac{UL}{\nu}, \quad "
                   r"\mathrm{Fr} = \frac{U}{\sqrt{gL}}, \quad "
                   r"\mathrm{Ma} = \frac{U}{a}, \quad "
                   r"\mathrm{St} = \frac{fL}{U}",
                   "Suyuqliklar mexanikasining asosiy o'lchamsiz sonlari.",
                   "O'lchamsiz sonlar"),
                eq(r"2f''' + f f'' = 0, \quad f(0) = f'(0) = 0,\ f'(\infty) = 1",
                   "Blazius tenglamasi va uning chegaraviy shartlari.",
                   "Blazius tenglamasi"),
                eq(r"\frac{\delta}{x} = \frac{4{,}91}{\sqrt{\mathrm{Re}_x}}, \qquad "
                   r"C_D = \frac{1{,}328}{\sqrt{\mathrm{Re}_L}}",
                   "Laminar chegaraviy qatlam qalinligi va plastina "
                   "qarshilik koeffitsienti.", "Blazius natijalari"),
            ],
            conditions=(
                "**Blazius masalasining chegaraviy shartlari:**\n"
                "- $y = 0$: $u = 0$ (no-slip) va $v = 0$ (o'tmaslik) "
                "$\\Rightarrow f(0) = f'(0) = 0$;\n"
                "- $y \\to \\infty$: $u \\to U$ $\\Rightarrow f'(\\infty) = 1$.\n\n"
                "Uchinchi tartibli ODE uchun uchta shart — masala to'liq "
                "qo'yilgan. Lekin shartlar ikki chekkada berilgani uchun "
                "u **chegaraviy masala** (boundary value problem) va "
                "otish (shooting) usuli bilan yechiladi: $f''(0)$ "
                "taxmin qilinadi va $f'(\\infty) = 1$ ta'minlanguncha "
                "tuzatiladi.\n\n"
                "**O'xshashlik shartlari (model sinovi uchun):**\n"
                "1. Geometrik o'xshashlik — barcha o'lchamlar $\\lambda$ "
                "nisbatda, g'adir-budirlik ham;\n"
                "2. Hukmron o'lchamsiz sonlarning tengligi;\n"
                "3. Chegaraviy shartlarning o'xshashligi."
            ),
            worked=WorkedExample(
                statement=(
                    "(a) Ko'prik tayanchi modeli 1:25 masshtabda, suvda "
                    "sinaladi. Tabiiy oqim tezligi 2,5 m/s. Reynolds "
                    "o'xshashligi bo'yicha model tezligi qancha bo'lishi "
                    "kerak? Bu amaliymi? (b) Havo oqimidagi tekis plastina: "
                    "$U = 15$ m/s, $L = 0{,}5$ m, $\\nu = 1{,}5\\times10^{-5}$ "
                    "m²/s. Chegaraviy qatlam qalinligini va qarshilik kuchini "
                    "(kenglik 0,3 m, ikki tomon) toping."
                ),
                given=[
                    r"\lambda = 1/25,\ U_t = 2{,}5\ \text{m/s}",
                    r"U = 15\ \text{m/s},\ L = 0{,}5\ \text{m},\ b = 0{,}3\ \text{m}",
                    r"\nu = 1{,}5\times10^{-5}\ \text{m}^2\text{/s},\ "
                    r"\rho = 1{,}2\ \text{kg/m}^3",
                ],
                steps=[
                    st(r"\mathrm{Re}_m = \mathrm{Re}_t: \quad "
                       r"U_m L_m = U_t L_t \;\Rightarrow\; "
                       r"U_m = U_t\frac{L_t}{L_m} = 2{,}5 \cdot 25 = 62{,}5\ \text{m/s}",
                       "Bir xil suyuqlikda ($\\nu$ bir xil) Reynolds "
                       "o'xshashligi tezlikni masshtab teskarisiga "
                       "ko'paytirishni talab qiladi."),
                    st(r"62{,}5\ \text{m/s suvda} \Rightarrow \text{kavitatsiya, "
                       r"katta nasos quvvati — amaliy emas}",
                       "Bu — modellashtirishning tipik muammosi. Yechim: "
                       "kattaroq model, shamol tunneli yoki bosimli tunnel "
                       "($\\nu$ ni kamaytirish uchun)."),
                    st(r"\mathrm{Re}_L = \frac{UL}{\nu} = \frac{15 \cdot 0{,}5}"
                       r"{1{,}5\times10^{-5}} = 5\times10^5",
                       "Kritik qiymat $5\\times10^5$ — aynan laminar/turbulent "
                       "o'tish chegarasida. Butun plastina bo'ylab laminar "
                       "deb hisoblash chegaraviy holat."),
                    st(r"\delta(L) = \frac{4{,}91 L}{\sqrt{\mathrm{Re}_L}} = "
                       r"\frac{4{,}91 \cdot 0{,}5}{707{,}1} = 3{,}47\times10^{-3}\ \text{m} "
                       r"= 3{,}47\ \text{mm}",
                       "Qatlam juda ingichka: plastina uzunligining atigi "
                       "0,7 % i. Prandtl taxmini ($\\delta \\ll L$) "
                       "yaxshi bajariladi."),
                    st(r"C_D = \frac{1{,}328}{\sqrt{5\times10^5}} = "
                       r"\frac{1{,}328}{707{,}1} = 1{,}878\times10^{-3}",
                       "Qarshilik koeffitsienti — juda kichik, bu silliq "
                       "plastinaning aerodinamik samaradorligini ko'rsatadi."),
                    st(r"F_{\text{bir tomon}} = C_D \cdot \tfrac{1}{2}\rho U^2 bL "
                       r"= 1{,}878\times10^{-3} \cdot \tfrac{1}{2} \cdot 1{,}2 "
                       r"\cdot 225 \cdot 0{,}15 = 0{,}0380\ \text{N}",
                       "$bL = 0{,}3 \\cdot 0{,}5 = 0{,}15$ m² — bir tomonning yuzasi."),
                    st(r"F_{\text{jami}} = 2 \cdot 0{,}0380 = 0{,}0761\ \text{N}",
                       "Ikki tomon hisobga olinadi. Taqqoslash uchun: "
                       "bir tanga og'irligi taxminan 0,05 N."),
                ],
                answer=(
                    "(a) $U_m = 62{,}5$ m/s — amaliy emas, shuning uchun "
                    "qisman o'xshashlik yoki boshqa modellashtirish "
                    "usuli kerak. (b) $\\mathrm{Re}_L = 5\\times10^5$, "
                    "$\\delta = 3{,}47$ mm, $C_D = 1{,}88\\times10^{-3}$, "
                    "$F = 0{,}076$ N."
                ),
                engineering_note=(
                    "Kema sinovlarida (Fruda usuli) qarshilik ikkiga "
                    "ajratiladi: to'lqin qarshiligi (Frud soniga bog'liq) "
                    "va yopishqoq qarshilik (Reynolds soniga bog'liq). "
                    "Model Frud bo'yicha sinaladi, o'lchangan umumiy "
                    "qarshilikdan hisoblangan yopishqoq qism ayriladi, "
                    "qolgan to'lqin qarshiligi masshtablanadi, so'ng "
                    "haqiqiy o'lcham uchun hisoblangan yopishqoq qism "
                    "qo'shiladi. Bu usul 1870-yildan beri ishlatiladi va "
                    "hali ham kemasozlik standarti."
                ),
            ),
            computation=Computation(
                caption=(
                    "$\\Pi$-guruhlarni o'lchamlar matritsasidan topish, "
                    "Blazius tenglamasini otish usuli bilan yechish va "
                    "chegaraviy qatlam parametrlarini hisoblash."
                ),
                code='''"""O'xshashlik nazariyasi va chegaraviy qatlam (Blazius)."""
import numpy as np
from labkit import PARAMS, note, series, table, value

U = float(PARAMS.get("U", 15.0))            # erkin oqim tezligi, m/s
Lx = float(PARAMS.get("L", 0.5))            # plastina uzunligi, m
nu = float(PARAMS.get("nu", 1.5e-5))        # m^2/s
rho = float(PARAMS.get("rho", 1.2))         # kg/m^3
bw = float(PARAMS.get("b", 0.3))            # kenglik, m
scale = float(PARAMS.get("scale", 25.0))    # model masshtabi 1:scale
Ut = float(PARAMS.get("Ut", 2.5))           # tabiiy obyekt tezligi, m/s
g = 9.81

# --- 1) O'lchamlar matritsasi va Pi-guruhlar soni ---
# Kattaliklar: F, U, L, rho, mu, g   |   Asosiy: M, L, T
names = ["F", "U", "L", "rho", "mu", "g"]
dims = np.array([
    [1, 0, 0, 1, 1, 0],       # M
    [1, 1, 1, -3, -1, 1],     # L
    [-2, -1, 0, 0, -1, -2],   # T
])
rank = int(np.linalg.matrix_rank(dims))
n_pi = len(names) - rank
value("Kattaliklar soni n", float(len(names)), "dona")
value("O'lchamlar matritsasi rangi k", float(rank), "—")
value("Pi-guruhlar soni (n - k)", float(n_pi), "dona")
note(f"Buckingem teoremasi: {len(names)} parametrli masala {n_pi} ta "
     f"o'lchamsiz guruh bilan to'liq tavsiflanadi.")

table("Asosiy o'lchamsiz sonlar",
      ["Son", "Ta'rif", "Fizik ma'no", "Qachon hukmron"],
      [["Reynolds Re", "U L / nu", "inersiya / yopishqoqlik", "Botgan jism, quvur"],
       ["Frud Fr", "U / sqrt(g L)", "inersiya / og'irlik", "Erkin sirt, to'lqin"],
       ["Max Ma", "U / a", "inersiya / siqiluvchanlik", "Ma > 0.3 gaz oqimi"],
       ["Struhal St", "f L / U", "nostatsionarlik / konvektsiya", "Vorteks uzilishi"],
       ["Eyler Eu", "dp / (rho U^2)", "bosim / inersiya", "Kavitatsiya, nasos"],
       ["Veber We", "rho U^2 L / sigma", "inersiya / sirt taranglik", "Tomchi, purkagich"]])

# --- 2) Model o'xshashligi ---
U_re = Ut*scale                # Reynolds o'xshashligi (bir xil suyuqlik)
U_fr = Ut/np.sqrt(scale)       # Frud o'xshashligi
value("Model tezligi (Re o'xshashligi)", U_re, "m/s")
value("Model tezligi (Fr o'xshashligi)", U_fr, "m/s")
value("Ikki talab nisbati", U_re/U_fr, "—")
nu_needed = nu/scale**1.5
value("Ikkalasi uchun kerakli nu", nu_needed*1e6, "mm2/s")
note(f"Ikkala shartni bir vaqtda bajarish uchun model suyuqligining "
     f"nu si {nu/nu_needed:.0f} marta kichik bo'lishi kerak — bunday "
     f"suyuqlik mavjud emas. Shuning uchun qisman o'xshashlik ishlatiladi.")

# --- 3) Blazius tenglamasi: 2*f_xxx + f*f_xx = 0, otish (shooting) usuli ---
def blasius_rhs(s):
    """f, f', f'' -> hosilalar."""
    return np.array([s[1], s[2], -0.5*s[0]*s[2]])


def integrate(fpp0, eta_max=10.0, n=4000):
    h = eta_max/n
    s = np.array([0.0, 0.0, fpp0])
    eta = [0.0]
    F = [s.copy()]
    for _ in range(n):
        k1 = blasius_rhs(s)
        k2 = blasius_rhs(s + 0.5*h*k1)
        k3 = blasius_rhs(s + 0.5*h*k2)
        k4 = blasius_rhs(s + h*k3)
        s = s + h/6*(k1 + 2*k2 + 2*k3 + k4)
        eta.append(eta[-1] + h)
        F.append(s.copy())
    return np.array(eta), np.array(F)


# Otish (shooting): f'(inf) = 1 bo'lishi uchun f''(0) ni topamiz
lo, hi = 0.1, 1.0
for _ in range(60):
    mid = 0.5*(lo + hi)
    _, Fm = integrate(mid)
    if Fm[-1, 1] < 1.0:
        lo = mid
    else:
        hi = mid
fpp0 = 0.5*(lo + hi)
eta, F = integrate(fpp0)
value("f''(0) (otish usuli bilan topilgan)", fpp0, "—")
value("Nazariy qiymat", 0.332057, "—")
value("Nisbiy xato", abs(fpp0 - 0.332057)/0.332057*100, "%")
value("f'(eta_max)", float(F[-1, 1]), "—")

series("Blazius profili u/U = f'(eta)", F[:, 1].tolist(), eta.tolist(),
       xlabel="u/U", ylabel="eta = y*sqrt(U/(nu x))")

# eta qiymatlari: qalinlik ta'riflari
i99 = int(np.argmax(F[:, 1] >= 0.99))
eta99 = float(eta[i99])
value("eta(u/U = 0.99)", eta99, "—")
trapz = np.trapezoid if hasattr(np, "trapezoid") else np.trapz
d_star = float(trapz(1 - F[:, 1], eta))              # siljish qalinligi
theta = float(trapz(F[:, 1]*(1 - F[:, 1]), eta))     # impuls qalinligi
value("Siljish qalinligi delta*/x * sqrt(Re_x)", d_star, "—")
value("Impuls qalinligi theta/x * sqrt(Re_x)", theta, "—")
value("Shakl faktori H = delta*/theta", d_star/theta, "—")
note(f"Nazariy qiymatlar: delta* = 1.7208, theta = 0.6641, H = 2.59. "
     f"Sonli yechim: {d_star:.4f}, {theta:.4f}, {d_star/theta:.3f}.")

# --- 4) Chegaraviy qatlam parametrlari plastina bo'ylab ---
x = np.linspace(1e-4, Lx, 300)
Re_x = U*x/nu
delta = eta99*x/np.sqrt(Re_x)
cf = 2*fpp0/np.sqrt(Re_x)
series("Chegaraviy qatlam qalinligi delta(x)", x.tolist(), (delta*1000).tolist(),
       xlabel="x, m", ylabel="delta, mm")
series("Mahalliy ishqalanish koeffitsienti cf(x)", x.tolist(), cf.tolist(),
       xlabel="x, m", ylabel="c_f")

Re_L = U*Lx/nu
CD = 4*fpp0/np.sqrt(Re_L)
F_one = CD*0.5*rho*U**2*bw*Lx
value("Re_L", Re_L, "—")
value("delta(L)", float(delta[-1])*1000, "mm")
value("delta(L)/L", float(delta[-1])/Lx*100, "%")
value("C_D (Blazius)", CD, "—")
value("Qarshilik kuchi (bir tomon)", F_one, "N")
value("Qarshilik kuchi (ikki tomon)", 2*F_one, "N")

if Re_L > 5e5:
    x_tr = 5e5*nu/U
    note(f"Re_L = {Re_L:.3e} > 5e5: x = {x_tr*1000:.1f} mm dan keyin "
         f"oqim turbulentlashadi, Blazius yechimi faqat shu nuqtagacha o'rinli.")
else:
    note(f"Re_L = {Re_L:.3e} < 5e5 — butun plastina bo'ylab laminar, "
         f"Blazius yechimi to'liq o'rinli.")

table("Chegaraviy qatlam: laminar va turbulent taqqoslash",
      ["Kattalik", "Laminar (Blazius)", "Turbulent (1/7 qonun)"],
      [["delta/x", "4.91/sqrt(Re_x)", "0.382/Re_x^0.2"],
       ["c_f", "0.664/sqrt(Re_x)", "0.0592/Re_x^0.2"],
       ["C_D", "1.328/sqrt(Re_L)", "0.074/Re_L^0.2"],
       ["Shakl faktori H", round(d_star/theta, 2), "~1.3"]])
note("Turbulent qatlam qalinroq va qarshiligi katta, lekin ajralishga "
     "ancha chidamli — shuning uchun golf to'pi ataylab g'adir-budir qilinadi.")
''',
                parameters=[
                    p("U", "Erkin oqim tezligi U", 0.5, 100.0, 15.0, 0.5, "m/s"),
                    p("L", "Plastina uzunligi L", 0.05, 5.0, 0.5, 0.05, "m"),
                    p("nu", "Kinematik yopishqoqlik ν", 1e-7, 1e-3, 1.5e-5, 1e-7, "m²/s"),
                    p("rho", "Zichlik ρ", 0.5, 1200.0, 1.2, 0.1, "kg/m³"),
                    p("b", "Plastina kengligi b", 0.05, 3.0, 0.3, 0.05, "m"),
                    p("scale", "Model masshtabi 1:λ", 2.0, 100.0, 25.0, 1.0),
                    p("Ut", "Tabiiy obyekt tezligi", 0.1, 20.0, 2.5, 0.1, "m/s"),
                ],
                expected_output=(
                    "f''(0) = 0,33206 (nazariy 0,332057, xato < 0,01 %); "
                    "δ*/θ = 2,59; Re_L = 5×10⁵, δ(L) = 3,47 mm, "
                    "C_D = 1,88×10⁻³, qarshilik ikki tomon 0,076 N. "
                    "Model uchun Re talabi 62,5 m/s, Fr talabi 0,5 m/s."
                ),
            ),
            visual=vis(
                kind="Chegaraviy qatlam va o'xshashlik",
                tool="React/SVG + Matplotlib",
                description=(
                    "Chegaraviy qatlamning $\\sqrt{x}$ bo'yicha o'sishi, "
                    "universal Blazius profili va $\\Pi$-guruhlar jadvali."
                ),
                how_to_draw=(
                    "React/SVG: gorizontal plastina, ustida erkin oqim "
                    "strelkalari (bir xil uzunlikda). Chegaraviy qatlam "
                    "chegarasi $\\delta(x) = 4{,}91x/\\sqrt{\\mathrm{Re}_x} "
                    "\\propto \\sqrt{x}$ — parabolik `<path>`, ichi och "
                    "rangda to'ldiriladi. Bir necha $x$ kesimda tezlik "
                    "profili chiziladi (strelkalar qatori): ular har xil "
                    "ko'rinadi. Yonida ikkinchi panel: bir xil profillar "
                    "$\\eta$ o'zgaruvchisida — **hammasi bitta egri "
                    "chiziqqa tushadi**. Bu ikki panel yonma-yon "
                    "o'xshashlik yechimining mohiyatini bir qarashda "
                    "ko'rsatadi. Laminar/turbulent o'tish nuqtasi "
                    "($\\mathrm{Re}_x = 5\\times10^5$) vertikal punktir "
                    "bilan belgilanadi va undan keyingi soha boshqa "
                    "shtrixlash bilan ajratiladi."
                ),
            ),
            interp=(
                "Otish usuli $f''(0) = 0{,}33206$ ni 0,01 % dan yaxshi "
                "aniqlikda topadi — bu 1908-yilda Blazius qo'lda qator "
                "yoyilmasi bilan hisoblagan qiymat. Sonli yechim "
                "shakl faktori $H = \\delta^*/\\theta = 2{,}59$ ni ham "
                "tiklaydi; bu kattalik amaliy jihatdan muhim, chunki "
                "$H > 3{,}5$ ga yaqinlashganda oqim ajralishi "
                "(separation) boshlanadi. Jadvaldagi laminar/turbulent "
                "taqqoslash esa aerodinamikaning eng qarama-qarshi "
                "faktini tushuntiradi: turbulent qatlam **qalinroq** va "
                "ishqalanish qarshiligi **kattaroq**, shunga qaramay "
                "golf to'pi, kriket to'pi va ba'zi qanot profillarida "
                "turbulentlik ataylab qo'zg'atiladi. Sababi — turbulent "
                "qatlamda devorga yaqin qatlamga tashqaridan impuls "
                "kuchli aralashtiriladi, shuning uchun u teskari bosim "
                "gradiyentiga uzoqroq chiday oladi va ajralish kechroq "
                "boshlanadi. Ajralish natijasidagi shakl qarshiligi "
                "(form drag) esa ishqalanish qarshiligidan bir necha "
                "marta katta — demak kichik yo'qotish katta yutuqni beradi."
            ),
            mistakes=[
                "Barcha o'lchamsiz sonlarni bir vaqtda saqlashga urinish. "
                "Ko'pincha bu matematik jihatdan imkonsiz; qaysi son "
                "hukmronligini fizik mulohaza bilan tanlash kerak.",
                "Chegaraviy qatlam qalinligini $\\delta \\propto x$ deb "
                "olish. To'g'ri bog'liqlik $\\delta \\propto \\sqrt{x}$ — "
                "qatlam sekinlashib o'sadi.",
                "Blazius yechimini bosim gradiyenti bor joyda qo'llash. "
                "U faqat $dp/dx = 0$ (tekis plastina) uchun o'rinli; "
                "boshqa hollarda Falkner–Skan yoki sonli yechim kerak.",
                "$\\mathrm{Re}_x$ va $\\mathrm{Re}_L$ ni aralashtirish. "
                "Mahalliy $c_f$ da $\\mathrm{Re}_x$ (joriy koordinata), "
                "umumiy $C_D$ da $\\mathrm{Re}_L$ (to'liq uzunlik) turadi.",
            ],
            quiz=[
                q("Buckingem $\\Pi$-teoremasi nimani aytadi?",
                  "$n$ ta o'lchamli kattalik va $k$ rangli o'lchamlar "
                  "matritsasi bo'lsa, masala $n - k$ ta o'lchamsiz guruh "
                  "bilan to'liq tavsiflanadi.", "konseptual"),
                q("Nima uchun kema modelida Re va Fr o'xshashligini bir "
                  "vaqtda ta'minlab bo'lmaydi?",
                  "Fr $U_m = U_t\\sqrt{\\lambda}$ ni, Re esa "
                  "$U_m = U_t/\\lambda$ ni talab qiladi. Ikkalasi uchun "
                  "$\\nu_m = \\nu_t\\lambda^{3/2}$ kerak — bunday "
                  "suyuqlik yo'q.", "talqin"),
                q("$U = 20$ m/s, $x = 0{,}2$ m, $\\nu = 1{,}5\\times10^{-5}$ "
                  "m²/s. $\\delta$ ni toping.",
                  "$\\mathrm{Re}_x = 2{,}67\\times10^5$, "
                  "$\\delta = 4{,}91 \\cdot 0{,}2/516{,}4 = 1{,}90$ mm.",
                  "hisob"),
                q("Blazius tenglamasi nima uchun ODE, garchi masala "
                  "ikki o'lchovli bo'lsa ham?",
                  "$\\eta = y\\sqrt{U/(\\nu x)}$ o'xshashlik o'zgaruvchisi "
                  "ikki mustaqil o'zgaruvchini bittaga birlashtiradi — "
                  "profil har bir $x$ da bir xil shaklga ega.", "konseptual"),
                q("Kodda otish (shooting) usuli nima qiladi?",
                  "$f''(0)$ ni taxmin qilib tenglamani integrallaydi va "
                  "$f'(\\infty) = 1$ shartini bajarmagunicha ikkiga "
                  "bo'lish usuli bilan tuzatadi — chegaraviy masalani "
                  "boshlang'ich masalalar ketma-ketligiga keltiradi.", "kod"),
                q("Nima uchun golf to'pi g'adir-budir qilinadi?",
                  "G'adir-budirlik chegaraviy qatlamni erta "
                  "turbulentlashtiradi; turbulent qatlam ajralishga "
                  "chidamliroq, shuning uchun izdagi (wake) soha "
                  "torayadi va shakl qarshiligi keskin kamayadi.",
                  "talqin"),
            ],
            bridge=(
                "Chegaraviy qatlam nazariyasi laminar rejimda aniq "
                "javob berdi. Lekin muhandislik amaliyotidagi oqimlarning "
                "aksariyati turbulent. Yakuniy mavzuda turbulentlikning "
                "tabiati, Reynolds o'rtachalashi va muhandislik "
                "modellarini ko'rib chiqamiz."
            ),
            research=(
                "Falkner–Skan yechimlarini o'rganing: bosim gradiyenti "
                "bo'lganda ($U_e \\propto x^m$) Blazius tenglamasi "
                "$f''' + ff'' + \\beta(1 - f'^2) = 0$ ga aylanadi. "
                "Turli $\\beta$ qiymatlarida yeching va $f''(0) = 0$ "
                "bo'ladigan kritik $\\beta \\approx -0{,}1988$ ni toping — "
                "bu oqim ajralishi boshlanishiga mos keladi. Natijani "
                "qanot profilidagi bosim taqsimoti bilan bog'lang: "
                "hujum burchagi qanday qiymatda 'stall' boshlanadi?"
            ),
            manim_ref=manim(
                scene="BoundaryLayerScene",
                module="manim/scenes/tmm_fluid.py",
                title="Chegaraviy qatlam va o'xshashlik yechimi",
                summary=(
                    "Plastina bo'ylab chegaraviy qatlam $\\sqrt{x}$ qonuni "
                    "bilan o'sadi; turli kesimdagi profillar $\\eta$ "
                    "o'zgaruvchisiga qayta chizilganda bitta universal "
                    "Blazius egri chizig'iga birlashadi."
                ),
            ),
        ),
    ),

    # ------------------------------------------------------------------ tmm-30
    Topic(
        id="tmm-30",
        subject_id=S, module_id=M, order=30,
        title="Turbulentlik asoslari: Reynolds o'rtachalashi va muhandislik modellari",
        description=(
            "Laminar oqimning turg'unligini yo'qotishi, Reynolds "
            "yoyilmasi va RANS tenglamalari, yopilish (closure) muammosi, "
            "Bussinesk gipotezasi va $k$–$\\varepsilon$ modeli, "
            "Kolmogorov energiya kaskadi."
        ),
        learning_objective=(
            "Turbulent oqim uchun o'rtachalangan tenglamalarni keltirib "
            "chiqarish, Reynolds kuchlanishlarining paydo bo'lish sababini "
            "tushuntirish, yopilish muammosini ifodalash va muhandislik "
            "modelining ishlash prinsipini bayon qilish."
        ),
        prerequisites=["tmm-29", "tmm-28"],
        mathematical_core=(
            "Reynolds yoyilmasi $u = \\bar{u} + u'$, o'rtachalash "
            "qoidalari, RANS tenglamalari, Reynolds kuchlanishlari "
            "$-\\rho\\overline{u_i'u_j'}$, Bussinesk gipotezasi "
            "$\\mu_t$, Kolmogorov masshtablari $\\eta_K = "
            "(\\nu^3/\\varepsilon)^{1/4}$."
        ),
        engineering_application=(
            "CFD hisoblarining asosi (ANSYS Fluent, OpenFOAM), quvur "
            "tarmoqlari va Mudi diagrammasi, atmosfera va okean "
            "modellari, yonish kameralari, aralashtirish jarayonlari."
        ),
        computational_component=(
            "Kolbruk tenglamasini iteratsiya bilan yechish, Mudi "
            "diagrammasini qurish, logarifmik devor qonuni profilini "
            "laminar profil bilan taqqoslash, Kolmogorov masshtablarini "
            "hisoblash."
        ),
        visualization_component=(
            "Mudi diagrammasi, logarifmik devor qonuni ($u^+$–$y^+$), "
            "energiya kaskadi spektri, laminar/turbulent profil "
            "taqqoslashi."
        ),
        research_extension=(
            "LES (Large Eddy Simulation) va DNS usullarini o'rganing: "
            "har biri uchun kerakli tur nuqtalari sonini Reynolds "
            "soniga bog'liq holda baholang."
        ),
        difficulty="ilg'or",
        previous_link=(
            "tmm-29 da chegaraviy qatlam laminar deb olindi va "
            "$\\mathrm{Re}_x > 5\\times10^5$ da bu taxmin buzilishi "
            "aytib o'tildi. Yakuniy mavzuda aynan shu buzilishdan "
            "keyingi holatni — turbulentlikni o'rganamiz."
        ),
        next_topic="pq-01",
        estimated_minutes=100,
        tags=["turbulentlik", "RANS", "Kolbruk", "CFD"],
        lesson=_lesson(
            problem=(
                "Neft quvuri: $D = 0{,}5$ m, $L = 50$ km, sarf 0,4 m³/s. "
                "Hagen–Puazeyl qonuni bo'yicha bosim yo'qotishini "
                "hisoblasak, nasos quvvati bir necha kilovatt chiqadi. "
                "Amalda esa megavattlar kerak bo'ladi — farq 100 "
                "barobardan ortiq. Sabab: $\\mathrm{Re} \\approx 10^6$ va "
                "oqim turbulent. Turbulentlikda tezlik har bir nuqtada "
                "tasodifiy tebranadi, Navye–Stoks tenglamalarini to'g'ridan-"
                "to'g'ri yechish esa bunday Reynolds sonida bugungi "
                "superkompyuterlar uchun ham imkonsiz. Muhandis nima qiladi?"
            ),
            concepts=[
                c("Turbulentlik (turbulence)",
                  "Yuqori Reynolds sonida yuzaga keladigan xaotik, "
                  "uch o'lchovli, vorteksli oqim rejimi; tezlik va bosim "
                  "vaqt bo'yicha tartibsiz tebranadi."),
                c("Reynolds yoyilmasi (Reynolds decomposition)",
                  "Har bir kattalikni o'rtacha va pulsatsion qismga "
                  "ajratish: $u = \\bar{u} + u'$, bunda "
                  "$\\overline{u'} = 0$."),
                c("Reynolds kuchlanishlari (Reynolds stresses)",
                  "$-\\rho\\overline{u_i'u_j'}$ — pulsatsiyalar hisobiga "
                  "yuzaga keladigan qo'shimcha impuls oqimi. Ular haqiqiy "
                  "kuchlanish emas, balki konvektiv tashishning "
                  "o'rtachalashdan keyingi ko'rinishi."),
                c("Yopilish muammosi (closure problem)",
                  "RANS tenglamalarida noma'lumlar soni tenglamalar "
                  "sonidan ko'p: 4 tenglama, 10 noma'lum. Qo'shimcha "
                  "model (gipoteza) kiritilishi shart."),
                c("Bussinesk gipotezasi (Boussinesq hypothesis)",
                  "$-\\rho\\overline{u_i'u_j'} = 2\\mu_t\\bar{D}_{ij} "
                  "- \\frac{2}{3}\\rho k\\delta_{ij}$ — Reynolds "
                  "kuchlanishlari o'rtacha deformatsiya tezligiga "
                  "mutanosib deb olinadi; $\\mu_t$ — turbulent "
                  "yopishqoqlik (material xossasi EMAS, oqim xossasi)."),
                c("Kolmogorov energiya kaskadi",
                  "Energiya katta vorteksdan kichikroqlariga uzatiladi, "
                  "eng kichik (Kolmogorov) masshtabda esa yopishqoqlik "
                  "hisobiga issiqlikka aylanadi."),
            ],
            derivation=[
                d("1. Reynolds yoyilmasi va o'rtachalash qoidalari",
                  r"u_i = \bar{u}_i + u_i', \qquad \overline{u_i'} = 0, \qquad "
                  r"\overline{\bar{a}b} = \bar{a}\bar{b}, \qquad "
                  r"\overline{a'b'} \ne 0",
                  "Oxirgi munosabat hal qiluvchi: ikki pulsatsiyaning "
                  "ko'paytmasi o'rtachasi umuman nolga teng emas, chunki "
                  "ular korrelyatsiyalangan."),
                d("2. Uzluksizlik tenglamasini o'rtachalash",
                  r"\frac{\partial\bar{u}_i}{\partial x_i} = 0 \quad\text{va}\quad "
                  r"\frac{\partial u_i'}{\partial x_i} = 0",
                  "Chiziqli tenglama o'rtachalashda shaklini saqlaydi; "
                  "pulsatsion qism ham alohida uzluksizlikni qanoatlantiradi."),
                d("3. Navye–Stoks tenglamasini konservativ shaklda yozish",
                  r"\frac{\partial u_i}{\partial t} + \frac{\partial (u_iu_j)}"
                  r"{\partial x_j} = -\frac{1}{\rho}\frac{\partial p}{\partial x_i} "
                  r"+ \nu\frac{\partial^2 u_i}{\partial x_j\partial x_j}",
                  "Uzluksizlikdan foydalanib konvektiv hadni divergensiya "
                  "shaklida yozamiz — o'rtachalash uchun qulay shakl."),
                d("4. Nochiziqli hadni o'rtachalash",
                  r"\overline{u_iu_j} = \overline{(\bar{u}_i + u_i')"
                  r"(\bar{u}_j + u_j')} = \bar{u}_i\bar{u}_j "
                  r"+ \overline{u_i'u_j'}",
                  "Kesishgan hadlar ($\\bar{u}_iu_j'$) o'rtachalashda "
                  "yo'qoladi, lekin $\\overline{u_i'u_j'}$ qoladi. "
                  "**Aynan shu had butun turbulentlik muammosining manbai.**"),
                d("5. RANS tenglamalari",
                  r"\rho\frac{D\bar{u}_i}{Dt} = -\frac{\partial\bar{p}}{\partial x_i} "
                  r"+ \frac{\partial}{\partial x_j}\Big(2\mu\bar{D}_{ij} "
                  r"- \rho\overline{u_i'u_j'}\Big)",
                  "Shakl Navye–Stoks bilan bir xil, faqat kuchlanishga "
                  "qo'shimcha had qo'shildi. $-\\rho\\overline{u_i'u_j'}$ — "
                  "Reynolds kuchlanishlari tenzori, simmetrik, 6 ta "
                  "mustaqil komponenta."),
                d("6. Yopilish muammosining kattaligi",
                  r"\text{Tenglamalar: } 4; \qquad "
                  r"\text{Noma'lumlar: } \bar{u}_i (3) + \bar{p} (1) "
                  r"+ \overline{u_i'u_j'} (6) = 10",
                  "Tizim yopiq emas. $\\overline{u_i'u_j'}$ uchun "
                  "tenglama yozsak, unda uchinchi tartibli korrelyatsiyalar "
                  "paydo bo'ladi va hokazo — cheksiz zanjir. Qaysidir "
                  "bosqichda modellashtirish shart."),
                d("7. Bussinesk gipotezasi va turbulent yopishqoqlik",
                  r"-\rho\overline{u_i'u_j'} = 2\mu_t\bar{D}_{ij} "
                  r"- \tfrac{2}{3}\rho k\delta_{ij}, \qquad "
                  r"k = \tfrac{1}{2}\overline{u_i'u_i'}",
                  "Nyuton gipotezasiga o'xshatib yoziladi, lekin "
                  "$\\mu_t$ — material doimiysi emas: u oqimga, joyga va "
                  "vaqtga bog'liq. Odatda $\\mu_t \\gg \\mu$ "
                  "(100–1000 marta) — shuning uchun turbulent oqimda "
                  "qarshilik keskin ortadi."),
                d("8. $k$–$\\varepsilon$ modeli va Kolmogorov masshtablari",
                  r"\mu_t = \rho C_\mu\frac{k^2}{\varepsilon}, \qquad "
                  r"\eta_K = \Big(\frac{\nu^3}{\varepsilon}\Big)^{1/4}, \qquad "
                  r"\frac{L}{\eta_K} \sim \mathrm{Re}^{3/4}",
                  "$k$ va $\\varepsilon$ uchun ikkita qo'shimcha tashish "
                  "tenglamasi yoziladi ($C_\\mu = 0{,}09$). Kolmogorov "
                  "masshtabi eng kichik vorteks o'lchami; DNS uchun tur "
                  "nuqtalari soni $\\mathrm{Re}^{9/4}$ ga mutanosib — "
                  "shuning uchun yuqori $\\mathrm{Re}$ da DNS imkonsiz."),
            ],
            meaning=(
                "Reynolds kuchlanishlarining eng chuqur ma'nosi shundaki, "
                "ular **haqiqiy kuchlanish emas**. Ular o'rtachalash "
                "amalining natijasi: pulsatsiyalar impulsni bir joydan "
                "boshqasiga tashiydi, o'rtachalangan tenglamada esa bu "
                "tashish kuchlanishga o'xshab ko'rinadi. Bu — modellashtirish "
                "falsafasining klassik misoli: axborotni o'rtachalash bilan "
                "yo'qotamiz, yo'qotilgan axborot esa yangi noma'lum "
                "sifatida qaytib keladi. $\\mu_t \\gg \\mu$ munosabati "
                "turbulentlikning barcha amaliy oqibatlarini tushuntiradi: "
                "qarshilik katta (neft quvurida megavattlar), issiqlik "
                "almashinuvi kuchli (radiator samarali ishlaydi), "
                "aralashtirish tez (yonish kamerasi ishlaydi). "
                "Kolmogorov munosabati $L/\\eta_K \\sim \\mathrm{Re}^{3/4}$ "
                "esa hisoblash mexanikasi uchun hal qiluvchi: "
                "$\\mathrm{Re} = 10^6$ da eng katta va eng kichik vorteks "
                "orasidagi nisbat 31 600, uch o'lchovda esa "
                "$3\\times10^{13}$ tur nuqtasi kerak bo'ladi. Shuning "
                "uchun muhandislik amaliyotida DNS emas, RANS ishlatiladi — "
                "u aniqlikning bir qismini modellashtirish evaziga "
                "almashtiradi."
            ),
            equations=[
                eq(r"\rho\frac{D\bar{u}_i}{Dt} = -\frac{\partial\bar{p}}{\partial x_i} "
                   r"+ \frac{\partial}{\partial x_j}\big(2\mu\bar{D}_{ij} "
                   r"- \rho\overline{u_i'u_j'}\big)",
                   "RANS — Reynolds bo'yicha o'rtachalangan Navye–Stoks "
                   "tenglamalari.", "RANS"),
                eq(r"\frac{1}{\sqrt{f}} = -2\log_{10}\Big(\frac{\epsilon/D}{3{,}7} "
                   r"+ \frac{2{,}51}{\mathrm{Re}\sqrt{f}}\Big)",
                   "Kolbruk–Uayt tenglamasi — turbulent ishqalanish "
                   "koeffitsienti (oshkormas).", "Kolbruk tenglamasi"),
                eq(r"u^+ = \frac{1}{\kappa}\ln y^+ + B, \quad "
                   r"\kappa \approx 0{,}41,\ B \approx 5{,}0",
                   "Logarifmik devor qonuni ($30 < y^+ < 300$).",
                   "Devor qonuni"),
                eq(r"\eta_K = \Big(\frac{\nu^3}{\varepsilon}\Big)^{1/4}, \qquad "
                   r"\frac{L}{\eta_K} \sim \mathrm{Re}^{3/4}",
                   "Kolmogorov masshtabi va masshtablar diapazoni.",
                   "Kolmogorov masshtabi"),
            ],
            conditions=(
                "**Devor yaqinidagi shartlar** turbulent hisobning eng "
                "nozik joyi. Ikki yondashuv bor:\n"
                "- **Devor funksiyalari** (wall functions): birinchi tur "
                "nuqtasi $30 < y^+ < 300$ oralig'ida joylashtiriladi va "
                "logarifmik qonun chegaraviy shart sifatida ishlatiladi. "
                "Arzon, lekin ajralishli oqimlarda noaniq;\n"
                "- **Devorgacha yechish** (low-Re modellar): birinchi "
                "nuqta $y^+ < 1$ da bo'lishi kerak, bu tur nuqtalari "
                "sonini keskin oshiradi.\n\n"
                "Bu yerda $y^+ = y u_\\tau/\\nu$, $u_\\tau = "
                "\\sqrt{\\tau_w/\\rho}$ — dinamik tezlik.\n\n"
                "**Kirish chegarasida** $k$ va $\\varepsilon$ ham "
                "berilishi kerak: odatda turbulentlik intensivligi $I$ "
                "($k = \\frac{3}{2}(\\bar{U}I)^2$) va uzunlik masshtabi "
                "orqali.\n\n"
                "**Qo'llanish sharti:** RANS statistik statsionar yoki "
                "sekin o'zgaruvchan oqimlar uchun; kuchli nostatsionar "
                "hodisalarda (vorteks uzilishi) URANS yoki LES kerak."
            ),
            worked=WorkedExample(
                statement=(
                    "Neft quvuri: $D = 0{,}5$ m, $L = 50$ km, $Q = 0{,}4$ "
                    "m³/s, $\\rho = 850$ kg/m³, $\\mu = 8\\times10^{-3}$ "
                    "Pa·s, mutlaq g'adir-budirlik $\\epsilon = 0{,}15$ mm. "
                    "(a) Oqim rejimini aniqlang. (b) Kolbruk bo'yicha $f$ "
                    "ni toping. (c) Bosim yo'qotishi va nasos quvvatini "
                    "hisoblang. (d) Laminar formula bilan taqqoslang."
                ),
                given=[
                    r"D = 0{,}5\ \text{m},\ L = 50\,000\ \text{m}",
                    r"Q = 0{,}4\ \text{m}^3\text{/s}",
                    r"\rho = 850\ \text{kg/m}^3,\ \mu = 8\times10^{-3}\ \text{Pa·s}",
                    r"\epsilon = 1{,}5\times10^{-4}\ \text{m}",
                ],
                steps=[
                    st(r"V = \frac{Q}{\pi D^2/4} = \frac{0{,}4}{0{,}1963} "
                       r"= 2{,}037\ \text{m/s}",
                       "O'rtacha tezlik — neft quvurlari uchun tipik qiymat "
                       "(1–3 m/s)."),
                    st(r"\mathrm{Re} = \frac{\rho V D}{\mu} = "
                       r"\frac{850 \cdot 2{,}037 \cdot 0{,}5}{8\times10^{-3}} "
                       r"= 1{,}082\times10^{5}",
                       "$\\mathrm{Re} \\gg 4000$ — oqim to'liq turbulent."),
                    st(r"\frac{\epsilon}{D} = \frac{1{,}5\times10^{-4}}{0{,}5} "
                       r"= 3\times10^{-4}",
                       "Nisbiy g'adir-budirlik — Kolbruk tenglamasining "
                       "ikkinchi parametri."),
                    st(r"\frac{1}{\sqrt{f}} = -2\log_{10}\Big(\frac{3\times10^{-4}}"
                       r"{3{,}7} + \frac{2{,}51}{1{,}082\times10^5\sqrt{f}}\Big)",
                       "Oshkormas tenglama. Boshlang'ich taxmin sifatida "
                       "Svami–Jeyn formulasi olinadi, so'ng 3–4 iteratsiya."),
                    st(r"f \approx 0{,}0193",
                       "Iteratsiya natijasi. Taqqoslash uchun: silliq quvur "
                       "uchun Blazius $f = 0{,}316\\,\\mathrm{Re}^{-0{,}25} "
                       "= 0{,}0174$ — g'adir-budirlik 11 % qo'shgan."),
                    st(r"h_f = f\frac{L}{D}\frac{V^2}{2g} = 0{,}0193 \cdot "
                       r"\frac{50\,000}{0{,}5} \cdot \frac{2{,}037^2}{19{,}62} "
                       r"= 1930 \cdot 0{,}2115 = 408{,}2\ \text{m}",
                       "Napor yo'qotishi — 408 m neft ustuniga teng, "
                       "juda katta."),
                    st(r"\Delta p = \rho g h_f = 850 \cdot 9{,}81 \cdot 408{,}2 "
                       r"= 3{,}404\ \text{MPa}; \quad "
                       r"P = Q\,\Delta p = 0{,}4 \cdot 3{,}404\times10^6 "
                       r"= 1{,}36\ \text{MW}",
                       "Nasos quvvati 1,36 MW (FIK 100 % da). Real FIK "
                       "0,75 bilan 1,82 MW kerak."),
                    st(r"f_{\text{laminar}} = \frac{64}{\mathrm{Re}} "
                       r"= \frac{64}{1{,}082\times10^5} = 5{,}92\times10^{-4}; "
                       r"\quad \frac{f_{\text{turb}}}{f_{\text{lam}}} = 32{,}6",
                       "Agar noto'g'ri ravishda laminar formula qo'llansa, "
                       "quvvat 32,6 marta kam chiqadi — 42 kW. Bu "
                       "loyihani butunlay yaroqsiz qilardi."),
                ],
                answer=(
                    "$\\mathrm{Re} = 1{,}08\\times10^5$ (turbulent), "
                    "$f = 0{,}0193$, $h_f = 408$ m, $\\Delta p = 3{,}40$ MPa, "
                    "nasos quvvati 1,36 MW (FIK 0,75 bilan 1,82 MW). "
                    "Laminar formula 32,6 marta kam quvvat bergan bo'lardi."
                ),
                engineering_note=(
                    "50 km da 3,4 MPa yo'qotish — shuning uchun uzun "
                    "quvurlarda har 30–80 km da oraliq nasos stansiyalari "
                    "qo'yiladi. Yana bir muhandislik yechimi — drag "
                    "reducing agents (DRA): quvurga million ulushlarda "
                    "qo'shiladigan uzun zanjirli polimerlar turbulent "
                    "pulsatsiyalarni bostirib, ishqalanishni 30–70 % "
                    "kamaytiradi. Bu Toms effekti (1948) deb ataladi va "
                    "uning to'liq mexanizmi hozirgacha faol tadqiqot "
                    "mavzusi bo'lib qolmoqda."
                ),
            ),
            computation=Computation(
                caption=(
                    "Kolbruk tenglamasini iteratsiya bilan yechish, Mudi "
                    "diagrammasini qurish, devor qonuni profili va "
                    "Kolmogorov masshtablari hisobi."
                ),
                code='''"""Turbulentlik: Kolbruk, Mudi diagrammasi va devor qonuni."""
import numpy as np
from labkit import PARAMS, note, series, table, value

D = float(PARAMS.get("D", 0.5))              # quvur diametri, m
Lp = float(PARAMS.get("Lp", 50000.0))        # uzunlik, m
Q = float(PARAMS.get("Q", 0.4))              # sarf, m^3/s
rho = float(PARAMS.get("rho", 850.0))
mu = float(PARAMS.get("mu", 8e-3))
eps = float(PARAMS.get("eps", 0.15))/1000.0  # mutlaq g'adir-budirlik, m
eta_pump = float(PARAMS.get("eta_pump", 0.75))
g = 9.81

A = np.pi*D**2/4
V = Q/A
Re = rho*V*D/mu
rr = eps/D
nu = mu/rho

value("O'rtacha tezlik V", V, "m/s")
value("Reynolds soni", Re, "—")
value("Nisbiy g'adir-budirlik eps/D", rr, "—")

if Re < 2300:
    regime = "laminar"
elif Re < 4000:
    regime = "o'tish (kritik)"
else:
    regime = "turbulent"
note(f"Oqim rejimi: {regime} (Re = {Re:.3e}).")


def colebrook(Re_, rr_, tol=1e-12, itmax=100):
    """Kolbruk-Uayt tenglamasini sobit nuqta iteratsiyasi bilan yechish."""
    if Re_ < 2300:
        return 64.0/Re_, 0
    # Svami-Jeyn boshlang'ich taxmini
    f = 0.25/np.log10(rr_/3.7 + 5.74/Re_**0.9)**2
    for i in range(1, itmax + 1):
        rhs = -2*np.log10(rr_/3.7 + 2.51/(Re_*np.sqrt(f)))
        f_new = 1.0/rhs**2
        if abs(f_new - f) < tol:
            return f_new, i
        f = f_new
    return f, itmax


f, iters = colebrook(Re, rr)
value("Darsi koeffitsienti f (Kolbruk)", f, "—")
value("Iteratsiyalar soni", float(iters), "dona")

f_blasius = 0.316*Re**-0.25 if Re >= 4000 else float("nan")
f_lam = 64/Re
value("f (Blazius, silliq quvur)", f_blasius, "—")
value("f (laminar formula — noto'g'ri)", f_lam, "—")
value("f_turb / f_lam", f/f_lam, "—")
note(f"G'adir-budirlik hissasi: {100*(f-f_blasius)/f_blasius:.1f} % "
     f"(silliq quvurga nisbatan).")

hf = f*(Lp/D)*V**2/(2*g)
dp = rho*g*hf
P_ideal = Q*dp
value("Napor yo'qotishi h_f", hf, "m")
value("Bosim yo'qotishi", dp/1e6, "MPa")
value("Nasos quvvati (ideal)", P_ideal/1e6, "MW")
value("Nasos quvvati (FIK bilan)", P_ideal/eta_pump/1e6, "MW")
value("Laminar formula bersa bo'lar edi", Q*rho*g*f_lam*(Lp/D)*V**2/(2*g)/1e3, "kW")

# --- Devor kuchlanishi va y+ ---
tau_w = f*rho*V**2/8
u_tau = np.sqrt(tau_w/rho)
value("Devor kuchlanishi tau_w", tau_w, "Pa")
value("Dinamik tezlik u_tau", u_tau, "m/s")
value("u_tau / V", u_tau/V, "—")
value("Yopishqoq qatlam qalinligi (y+ = 5)", 5*nu/u_tau*1000, "mm")
value("y+ = 1 uchun birinchi tur nuqtasi", nu/u_tau*1e6, "mkm")

# --- Devor qonuni profili ---
yp = np.logspace(-1, 3.5, 400)
kappa, B = 0.41, 5.0
u_visc = yp                                  # yopishqoq qatlam: u+ = y+
u_log = np.log(yp)/kappa + B                 # logarifmik soha
u_plus = np.where(yp < 11.0, u_visc, u_log)
series("Devor qonuni u+(y+)", yp.tolist(), u_plus.tolist(),
       xlabel="y+", ylabel="u+")
series("Yopishqoq qatlam u+ = y+", yp.tolist(), u_visc.tolist(),
       xlabel="y+", ylabel="u+")
series("Logarifmik qonun", yp.tolist(), u_log.tolist(),
       xlabel="y+", ylabel="u+")

# Turbulent (1/7) va laminar profil taqqoslash
r_norm = np.linspace(0.0, 1.0, 200)
u_lam_prof = 2*(1 - r_norm**2)                # u/V, laminar
u_turb_prof = (60/49)*(1 - r_norm)**(1/7)     # u/V, 1/7 qonun
series("Laminar profil u/V", u_lam_prof.tolist(), r_norm.tolist(),
       xlabel="u / V", ylabel="r / R")
series("Turbulent profil u/V (1/7)", u_turb_prof.tolist(), r_norm.tolist(),
       xlabel="u / V", ylabel="r / R")
note(f"Laminar: u_max/V = 2.00; turbulent (1/7): u_max/V = "
     f"{60/49:.3f} — turbulent profil ancha 'yassi', chunki "
     f"aralashuv markaz va devor orasidagi farqni tekislaydi.")

# --- Mudi diagrammasi ---
# Laminar va turbulent sohalar ALOHIDA chiziladi. 2300 < Re < 4000
# o'tish sohasida ishonchli korrelyatsiya yo'q, shuning uchun u umuman
# chizilmaydi - "teshik"ni NaN bilan to'ldirish natijani soxtalashtiradi.
Re_lam = np.logspace(3.3, np.log10(2300.0), 40)
series("Mudi: laminar 64/Re", Re_lam.tolist(), (64.0/Re_lam).tolist(),
       xlabel="Reynolds soni Re", ylabel="Darsi koeffitsienti f")
Re_turb = np.logspace(np.log10(4000.0), 8, 210)
for rr_i in [0.0, 1e-5, 1e-4, 1e-3, 5e-3, 2e-2]:
    fs = [float(colebrook(Re_i, rr_i)[0]) for Re_i in Re_turb]
    series(f"Mudi: eps/D = {rr_i:g}", Re_turb.tolist(), fs,
           xlabel="Reynolds soni Re", ylabel="Darsi koeffitsienti f")

# To'liq turbulent (g'adir-budirlik hukmron) asimptota
f_rough = 1/(-2*np.log10(rr/3.7))**2 if rr > 0 else float("nan")
value("To'liq turbulent asimptota f", f_rough, "—")
note("Yuqori Re da egri chiziqlar gorizontal asimptotaga chiqadi: "
     "f faqat g'adir-budirlikka bog'liq bo'lib qoladi.")

# --- Kolmogorov masshtablari ---
epsilon = u_tau**3/(0.5*D)                    # dissipatsiya bahosi
eta_K = (nu**3/epsilon)**0.25
t_K = np.sqrt(nu/epsilon)
v_K = (nu*epsilon)**0.25
value("Dissipatsiya tezligi epsilon", epsilon, "m2/s3")
value("Kolmogorov uzunligi eta_K", eta_K*1e6, "mkm")
value("Kolmogorov vaqti t_K", t_K*1000, "ms")
value("Kolmogorov tezligi v_K", v_K, "m/s")
value("Masshtablar nisbati D/eta_K", D/eta_K, "—")
value("DNS uchun tur nuqtalari (~(D/eta_K)^3)", (D/eta_K)**3, "dona")
note(f"DNS uchun taxminan {(D/eta_K)**3:.2e} tur nuqtasi kerak — "
     f"shuning uchun muhandislik hisoblarida RANS ishlatiladi.")

table("Turbulentlik modellari",
      ["Model", "Qo'shimcha tenglama", "Hisob narxi", "Qo'llanishi"],
      [["Aralashuv uzunligi", 0, "juda arzon", "Sodda chegaraviy qatlam"],
       ["Spalart-Allmaras", 1, "arzon", "Aerodinamika, tashqi oqim"],
       ["k-epsilon", 2, "o'rtacha", "Umumiy sanoat, erkin oqim"],
       ["k-omega SST", 2, "o'rtacha", "Ajralish, devor yaqini"],
       ["Reynolds kuchlanish (RSM)", 7, "qimmat", "Anizotrop, aylanma oqim"],
       ["LES", "filtrlangan NS", "juda qimmat", "Nostatsionar, aralashuv"],
       ["DNS", "to'liq NS", "imkonsiz (yuqori Re)", "Tadqiqot, past Re"]])
''',
                parameters=[
                    p("D", "Quvur diametri D", 0.01, 2.0, 0.5, 0.01, "m"),
                    p("Lp", "Quvur uzunligi L", 10.0, 200000.0, 50000.0, 10.0, "m"),
                    p("Q", "Sarf Q", 0.001, 5.0, 0.4, 0.001, "m³/s"),
                    p("rho", "Zichlik ρ", 500.0, 1200.0, 850.0, 10.0, "kg/m³"),
                    p("mu", "Dinamik yopishqoqlik μ", 1e-5, 1.0, 8e-3, 1e-5, "Pa·s"),
                    p("eps", "G'adir-budirlik ε", 0.0, 5.0, 0.15, 0.01, "mm"),
                    p("eta_pump", "Nasos FIK", 0.3, 0.95, 0.75, 0.01),
                ],
                expected_output=(
                    "Re = 1,08×10⁵ (turbulent), f = 0,0193 (4–6 iteratsiya), "
                    "h_f = 408 m, Δp = 3,40 MPa, nasos quvvati 1,36 MW "
                    "(FIK bilan 1,82 MW); laminar formula 32,6 marta kam "
                    "beradi. η_K ≈ 60 mkm, DNS uchun ~6×10¹¹ tur nuqtasi."
                ),
            ),
            visual=vis(
                kind="Mudi diagrammasi va devor qonuni",
                tool="React/SVG + Matplotlib",
                description=(
                    "Log–log Mudi diagrammasi, $u^+$–$y^+$ devor qonuni "
                    "va laminar/turbulent profillarning taqqoslashi."
                ),
                how_to_draw=(
                    "React/SVG: Mudi diagrammasi ikki o'q ham logarifmik "
                    "($\\mathrm{Re}$: $10^3$–$10^8$, $f$: 0,008–0,1). "
                    "Har bir $\\epsilon/D$ uchun alohida `<polyline>`; "
                    "laminar soha ($\\mathrm{Re} < 2300$) bitta qiya "
                    "to'g'ri chiziq (log–logda $f = 64/\\mathrm{Re}$ "
                    "qiyaligi $-1$), kritik soha vertikal shtrixlangan "
                    "band bilan ajratiladi. Ish nuqtasi katta belgi bilan "
                    "qo'yiladi va unga $\\mathrm{Re}$, $f$ yorliqlari "
                    "ilova qilinadi. Devor qonuni panelida $x$ o'qi "
                    "logarifmik: yopishqoq osti qatlam ($u^+ = y^+$, "
                    "log-o'qda eksponensial egri), logarifmik soha "
                    "(to'g'ri chiziq) va ularning o'rtasidagi bufer "
                    "qatlam uch xil rangda; $y^+ = 5$ va $y^+ = 30$ "
                    "chegaralari vertikal punktir bilan. Profillar "
                    "paneli laminar parabolani va turbulent 1/7 "
                    "profilni ustma-ust chizadi — farq darhol ko'rinadi."
                ),
            ),
            interp=(
                "Eng muhim son — $f_{\\text{turb}}/f_{\\text{lam}} = 32{,}6$. "
                "Bu shunchaki koeffitsient farqi emas: agar muhandis "
                "rejimni noto'g'ri aniqlasa, nasos quvvatini 1,36 MW "
                "o'rniga 42 kW deb hisoblaydi va butun loyiha yaroqsiz "
                "bo'ladi. Shuning uchun har qanday gidravlik hisobning "
                "birinchi qadami — Reynolds sonini tekshirish. "
                "Mudi diagrammasidagi gorizontal asimptotalar boshqa muhim "
                "xulosani beradi: yuqori $\\mathrm{Re}$ da $f$ Reynolds "
                "soniga umuman bog'liq bo'lmay qoladi va faqat "
                "g'adir-budirlik bilan aniqlanadi. Bu 'to'liq turbulent' "
                "rejim eski quvurlarda odatiy holat — shuning uchun "
                "korroziya va cho'kindi tufayli $\\epsilon$ ning o'sishi "
                "yillar davomida quvur o'tkazuvchanligini asta-sekin "
                "pasaytiradi. Tur nuqtalari hisobi ($\\sim 10^{11}$) esa "
                "hisoblash mexanikasi kursiga (5-fan) to'g'ridan-to'g'ri "
                "ko'prik: u yerda diskretlashtirish, tur qurish va "
                "iterativ yechish usullarini o'rganamiz — aynan shu "
                "masshtabdagi masalalarni yechish uchun."
            ),
            mistakes=[
                "Turbulent yopishqoqlik $\\mu_t$ ni material xossasi deb "
                "hisoblash. U — oqim xossasi: joyga, vaqtga va "
                "geometriyaga bog'liq, jadvalda berilmaydi.",
                "Reynolds kuchlanishlarini haqiqiy mexanik kuchlanish deb "
                "tushunish. Ular impuls tashishning o'rtachalashdan "
                "keyingi ko'rinishi, molekulalararo kuch emas.",
                "Laminar $f = 64/\\mathrm{Re}$ ni turbulent rejimda "
                "qo'llash. Xato 30 baravargacha yetadi va xavfsiz "
                "tomonga emas.",
                "Devor funksiyalari ishlatilganda birinchi tur nuqtasini "
                "$y^+ < 5$ da qo'yish. Bu logarifmik qonun amal "
                "qilmaydigan sohaga tushadi va natija ishonchsiz bo'ladi; "
                "$30 < y^+ < 300$ oralig'i talab qilinadi.",
            ],
            quiz=[
                q("Reynolds kuchlanishlari qayerdan paydo bo'ladi?",
                  "Navye–Stoksning nochiziqli konvektiv hadini "
                  "o'rtachalashdan: $\\overline{u_iu_j} = \\bar{u}_i"
                  "\\bar{u}_j + \\overline{u_i'u_j'}$ — oxirgi had "
                  "o'rtachalangan tenglamada yangi noma'lum bo'lib qoladi.",
                  "konseptual"),
                q("Yopilish (closure) muammosi nima?",
                  "RANS da 4 tenglamaga 10 noma'lum to'g'ri keladi. "
                  "Yuqori tartibli tenglama yozish yangi, yanada yuqori "
                  "tartibli korrelyatsiyalarni keltirib chiqaradi — "
                  "cheksiz zanjir. Modellashtirish shart.", "konseptual"),
                q("$\\mathrm{Re} = 10^5$, $\\epsilon/D = 0$ (silliq). "
                  "Blazius formulasi bo'yicha $f$ ni toping.",
                  "$f = 0{,}316 \\cdot (10^5)^{-0{,}25} = 0{,}316/17{,}78 "
                  "= 0{,}0178$.", "hisob"),
                q("Nima uchun turbulent tezlik profili laminar profildan "
                  "'yassiroq'?",
                  "Turbulent pulsatsiyalar impulsni markazdan devorga "
                  "faol tashiydi va tezliklarni tekislaydi. "
                  "$u_{\\max}/V$ laminarda 2,00, turbulentda esa "
                  "$\\approx 1{,}22$.", "talqin"),
                q("Kodda Kolbruk tenglamasi nima uchun iteratsiya bilan "
                  "yechiladi?",
                  "U oshkormas: $f$ tenglamaning ikkala tomonida "
                  "qatnashadi. Sobit nuqta iteratsiyasi Svami–Jeyn "
                  "taxminidan boshlab 4–6 qadamda $10^{-12}$ aniqlikka "
                  "yetadi.", "kod"),
                q("$L/\\eta_K \\sim \\mathrm{Re}^{3/4}$ munosabati "
                  "hisoblash uchun nimani anglatadi?",
                  "Uch o'lchovli DNS uchun tur nuqtalari soni "
                  "$\\mathrm{Re}^{9/4}$ ga mutanosib. $\\mathrm{Re} = 10^6$ "
                  "da bu $10^{13}$ tartibida — bugungi kompyuterlar uchun "
                  "imkonsiz, shuning uchun RANS yoki LES ishlatiladi.",
                  "talqin"),
            ],
            bridge=(
                "Tutash muhitlar mexanikasi yakunlandi: qattiq jism va "
                "suyuqlik uchun yagona tenzor apparati, balans qonunlari "
                "va konstitutiv munosabatlar qurildi. Keyingi fanda "
                "(Plastinalar va qobiqlar nazariyasi) shu umumiy "
                "nazariyani yupqa konstruksiyalar uchun ixtisoslashtiramiz: "
                "uch o'lchovli elastiklik masalasi asoslangan gipotezalar "
                "yordamida ikki o'lchovli masalaga keltiriladi."
            ),
            research=(
                "LES (Large Eddy Simulation) va DNS usullarini "
                "taqqoslang. LES da katta vortekslar to'g'ridan-to'g'ri "
                "yechiladi, kichiklari esa submasshtabli model bilan "
                "(Smagorinskiy) almashtiriladi. Har bir usul uchun tur "
                "nuqtalari sonining Reynolds soniga bog'liqligini "
                "baholang: DNS uchun $N \\sim \\mathrm{Re}^{9/4}$, LES "
                "uchun devor yaqinida $N \\sim \\mathrm{Re}^{1{,}8}$. "
                "Bir xil hisoblash resursi bilan har bir usul qanday "
                "maksimal Reynolds soniga chiqishi mumkinligini hisoblang "
                "va natijani Mur qonuni bilan birga ekstrapolyatsiya "
                "qiling: DNS qachon sanoat masalalari uchun amaliy bo'ladi?"
            ),
            manim_ref=manim(
                scene="TurbulenceScene",
                module="manim/scenes/tmm_fluid.py",
                title="Energiya kaskadi va Reynolds o'rtachalashi",
                summary=(
                    "Katta vorteks kichiklariga bo'linib boradi, energiya "
                    "kaskad bo'ylab Kolmogorov masshtabiga o'tadi va "
                    "issiqlikka aylanadi; yonida tezlik signalining "
                    "o'rtacha va pulsatsion qismlarga ajralishi ko'rsatiladi."
                ),
            ),
        ),
    ),
]
