"""SU / 5-modul: Zamonaviy usullar, tekshirish va yakun (su-25 … su-30)."""

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

S = "sonli-usullar"
M = "su-m5"


def _lesson(problem, concepts, derivation, meaning, equations, conditions,
            worked, computation, visual, interp, mistakes, quiz, bridge,
            research, manim_ref=None):
    return Lesson(
        physical_problem=problem, concepts=concepts, derivation=derivation,
        formula_meaning=meaning, equations=equations, conditions=conditions,
        worked_example=worked, computation=computation, visualization=visual,
        interpretation=interp, common_mistakes=mistakes, quiz=quiz,
        bridge_to_next=bridge, research_extension=research, manim=manim_ref,
    )


TOPICS = [
    # ------------------------------------------------------------------ su-25
    Topic(
        id="su-25",
        subject_id=S, module_id=M, order=25,
        title="Differensial kvadratura usuli (DQM)",
        description=(
            "Vazn koeffitsientlari, tugun taqsimoti tanlovi, chegaraviy "
            "shartlarni qo'llash, spektral yaqinlashish va DQM ning FEM "
            "bilan taqqoslanishi."
        ),
        learning_objective=(
            "DQM vazn koeffitsientlarini qurish, uni balka va plastina "
            "masalalariga qo'llash hamda uning kuchli va zaif tomonlarini "
            "miqdoriy baholash."
        ),
        prerequisites=["su-24", "su-07", "su-23"],
        mathematical_core=(
            "$\\left.\\frac{d^mf}{dx^m}\\right|_{x_i} = "
            "\\sum_{j=1}^{N}A^{(m)}_{ij}f(x_j)$; "
            "$A_{ij} = \\frac{M(x_i)}{(x_i-x_j)M(x_j)}$; "
            "$\\mathbf{A}^{(m)} = \\mathbf{A}^m$."
        ),
        engineering_application=(
            "Plastina va qobiqlarning tebranishi hamda ustuvorligi, "
            "qatlamli kompozitlar, muntazam geometriyali masalalarda tez "
            "va juda aniq yechim."
        ),
        computational_component=(
            "Vazn koeffitsientlarini qurish va tekshirish, balka "
            "chastotalarini kam nuqta bilan topish, FEM bilan "
            "taqqoslash."
        ),
        visualization_component=(
            "Tugun taqsimotlari, spektral yaqinlashish egri chizig'i, "
            "matritsa to'ldirilishi."
        ),
        research_extension=(
            "Umumlashgan DQM (GDQ) va harmonik DQM ni o'rganing: "
            "ko'phad o'rniga boshqa bazis tanlansa nima o'zgaradi."
        ),
        difficulty="murakkab",
        previous_link=(
            "4-modulda FEM ni fermadan nochiziqli qobiqqacha qo'lladik. "
            "FEM universal, lekin har bir erkinlik darajasi uchun "
            "atigi ikkinchi tartibli aniqlik beradi. Muntazam "
            "geometriyali masalalarda bundan ancha yaxshi qilish "
            "mumkin."
        ),
        next_topic="su-26",
        estimated_minutes=85,
        tags=["DQM", "spektral usul", "vazn koeffitsientlari",
              "Chebishev-Gauss-Lobatto"],
        lesson=_lesson(
            problem=(
                "Qatlamli kompozit plastinaning "
                "tebranish chastotalari "
                "kerak — parametrik tadqiqot "
                "uchun. Qatlamlar burchagi, "
                "qalinliklar nisbati va "
                "tomonlar nisbati "
                "o'zgartirilib, **minglab** "
                "hisob bajarilishi lozim. "
                "FEM bilan har bir hisob "
                "bir necha ming erkinlik "
                "darajasini talab qiladi "
                "va butun tadqiqot "
                "soatlab davom etadi. "
                "Lekin geometriya oddiy "
                "to'rtburchak, yechim esa "
                "silliq. Shunday "
                "holatlarda o'nlab "
                "noma'lum bilan olti "
                "xonali aniqlik berishga "
                "qodir usul bormi?"
            ),
            concepts=[
                c("Differensial kvadratura "
                  "g'oyasi",
                  "Hosila barcha tugunlardagi "
                  "qiymatlarning "
                  "**chiziqli kombinatsiyasi** "
                  "sifatida ifodalanadi."),
                c("Vazn koeffitsientlari "
                  "$A_{ij}$",
                  "Lagranj bazisidan aniq "
                  "chiqariladi; ular faqat "
                  "tugun joylashuviga "
                  "bog'liq."),
                c("Yuqori tartibli hosilalar",
                  "$\\mathbf{A}^{(m)} = "
                  "\\mathbf{A}^m$ — matritsani "
                  "ko'paytirish kifoya."),
                c("Chebishev–Gauss–Lobatto "
                  "tugunlari",
                  "$x_i = \\frac{L}{2}"
                  "\\left(1 - \\cos"
                  "\\frac{\\pi i}{N-1}\\right)$ "
                  "— chekkalarda zich, Runge "
                  "hodisasini yengadi "
                  "(su-14)."),
                c("Spektral yaqinlashish",
                  "Silliq yechimda xato "
                  "$N$ bilan **eksponensial** "
                  "kamayadi — darajali "
                  "emas."),
                c("To'la matritsa narxi",
                  "DQM matritsalari zich va "
                  "yomon shartlangan; "
                  "$\\kappa \\sim N^{2m}$."),
            ],
            derivation=[
                d("1. Asosiy taxmin",
                  r"\left.\frac{df}{dx}"
                  r"\right|_{x_i} = "
                  r"\sum_{j=1}^{N}A_{ij}\,"
                  r"f(x_j)",
                  "Hosila — **global** "
                  "kombinatsiya. Chekli "
                  "ayirmalarda (su-07) faqat "
                  "qo'shni nuqtalar "
                  "qatnashardi, bu yerda "
                  "esa **hammasi**."),
                d("2. Koeffitsientlarni "
                  "aniqlash",
                  r"f(x) = \ell_k(x) "
                  r"\;\Longrightarrow\; "
                  r"A_{ik} = \ell_k'(x_i)",
                  "Har bir Lagranj bazis "
                  "funksiyasini (su-14) "
                  "qo'yib, "
                  "koeffitsientlarni "
                  "birma-bir topamiz."),
                d("3. Yopiq formula",
                  r"A_{ij} = \frac{M(x_i)}"
                  r"{(x_i - x_j)M(x_j)}, "
                  r"\quad i \ne j, \qquad "
                  r"M(x_i) = \prod_{k\ne i}"
                  r"(x_i - x_k)",
                  "**Amaliy natija.** "
                  "Iteratsiyasiz, bevosita "
                  "hisoblanadi."),
                d("4. Diagonal hadlar",
                  r"A_{ii} = -\sum_{j \ne i}"
                  r"A_{ij}",
                  "Doimiy funksiyaning "
                  "hosilasi nol bo'lishi "
                  "shartidan. **Muhim "
                  "oqibat:** "
                  "$\\mathbf{A}\\mathbf{1} = "
                  "\\mathbf{0}$, demak "
                  "$\\mathbf{A}$ "
                  "**singulyar** — bu xato "
                  "emas, fizik "
                  "zarurat."),
                d("5. Yuqori hosilalar",
                  r"\mathbf{A}^{(2)} = "
                  r"\mathbf{A}\mathbf{A}, "
                  r"\qquad \mathbf{A}^{(4)} = "
                  r"\mathbf{A}^{(2)}"
                  r"\mathbf{A}^{(2)}",
                  "Hosila operatorini "
                  "ketma-ket qo'llash. "
                  "Balka tenglamasi uchun "
                  "$\\mathbf{A}^{(4)}$ "
                  "kerak."),
                d("6. Aniqlik tartibi",
                  r"N \ \text{nuqta} \ "
                  r"\Longrightarrow\ "
                  r"(N-1)\text{-darajali "
                  r"ko'phad AYNAN}",
                  "**O'lchangan natija.** "
                  "Chekli ayirmalarda "
                  "$n$ nuqta atigi "
                  "$n-1$ tartib berardi "
                  "(su-07); bu yerda "
                  "butun bazis "
                  "ishlatiladi."),
                d("7. Tugun taqsimoti muhim",
                  r"x_i = \frac{L}{2}\left(1 - "
                  r"\cos\frac{\pi i}{N-1}"
                  r"\right)",
                  "Tekis tugunlarda katta "
                  "$N$ da Runge hodisasi "
                  "(su-14); CGL tugunlari "
                  "chekkalarda zichlashadi "
                  "va buni yengadi."),
                d("8. Balka tenglamasi",
                  r"EI\,\mathbf{A}^{(4)}"
                  r"\mathbf{w} = \rho A"
                  r"\omega^2\mathbf{w}",
                  "Xususiy qiymat masalasi "
                  "(su-23) — faqat "
                  "matritsalar boshqacha "
                  "qurilgan."),
                d("9. Chegaraviy shartlarni "
                  "qo'llash",
                  r"\text{qator almashtirish: } "
                  r"\mathbf{K}[r,:] \leftarrow "
                  r"\text{shart vektori}",
                  "**Nozik joy.** To'rtinchi "
                  "tartibli tenglamada "
                  "to'rtta shart bor, "
                  "chegara nuqtalari esa "
                  "ikkita — shuning uchun "
                  "chegaraga **qo'shni** "
                  "qatorlar ham "
                  "ishlatiladi."),
                d("10. Spektral yaqinlashish",
                  r"\|e\| \sim C\,e^{-\sigma N} "
                  r"\quad (\text{silliq } f)",
                  "**Asosiy afzallik.** "
                  "Har qo'shilgan nuqta "
                  "xatoni doimiy "
                  "koeffitsientga "
                  "**bo'ladi** — darajali "
                  "usullarda esa faqat "
                  "$h^p$ kabi kamayadi."),
                d("11. Zichlik narxi",
                  r"\text{DQM: to'la matritsa, }"
                  r" O(N^3); \quad "
                  r"\text{FEM: lentali, } "
                  r"O(nb^2)",
                  "**Cheklov.** $N$ oshgani "
                  "sari DQM matritsasi zich "
                  "qoladi (kodda 90%), FEM "
                  "esa siyraklashadi "
                  "(25%)."),
                d("12. Shartlanganlik",
                  r"\kappa \sim N^{2m} \quad "
                  r"(m - \text{hosila "
                  r"tartibi})",
                  "**O'lchangan natija.** "
                  "To'rtinchi tartibli "
                  "masalada "
                  "$\\kappa \\sim N^{8}$ — "
                  "kodda $N = 19$ da "
                  "$1{,}5\\cdot10^{8}$. Bu "
                  "$N$ ni amalda 20–30 "
                  "bilan cheklaydi."),
                d("13. Qo'llanish sohasi",
                  r"\text{muntazam geometriya} "
                  r"+ \text{silliq yechim} "
                  r"\Longrightarrow \text{DQM}",
                  "Murakkab geometriya, "
                  "singulyarlik yoki "
                  "nochiziqlik bo'lsa FEM "
                  "afzal — DQM bularni "
                  "yomon ko'taradi."),
            ],
            meaning=(
                "DQM va chekli ayirmalar "
                "orasidagi farq 1-qadamda "
                "ko'rinadi va u hal qiluvchi. "
                "Chekli ayirmalarda hosila "
                "faqat qo'shni nuqtalar "
                "orqali ifodalanadi — "
                "mahalliy yaqinlashish. "
                "DQM da esa **barcha** "
                "tugunlar qatnashadi, ya'ni "
                "yaqinlashish global. Buning "
                "bahosi 6-qadamda: $N$ nuqta "
                "$(N-1)$-darajali ko'phadni "
                "aynan differensiallaydi, "
                "holbuki chekli ayirmalarda "
                "$n$ nuqta atigi $n-1$ "
                "tartib berardi. Silliq "
                "funksiyalarda bu "
                "10-qadamdagi eksponensial "
                "yaqinlashishga olib keladi "
                "va kod buni aniq "
                "ko'rsatadi: sinusning "
                "hosilasi $N = 5$ da 43% "
                "xato bilan, $N = 21$ da esa "
                "$10^{-14}$ aniqlikda "
                "hisoblanadi. Har qo'shilgan "
                "ikki nuqta xatoni taxminan "
                "yuz barobar kamaytiradi — "
                "darajali usullarda bunday "
                "bo'lmaydi. 4-qadam "
                "kutilmagan, lekin muhim "
                "nozik nuqtani ochadi: "
                "$\\mathbf{A}$ matritsasi "
                "**singulyar**. Sababi "
                "sodda — doimiy "
                "funksiyaning hosilasi nol, "
                "demak "
                "$\\mathbf{A}\\mathbf{1} = "
                "\\mathbf{0}$. Bu xato emas "
                "va uni 'tuzatishga' "
                "urinish kerak emas; "
                "chegaraviy shartlar "
                "qo'llangandan keyin tizim "
                "yechiluvchan bo'ladi. "
                "Shuning uchun DQM kodini "
                "tekshirishda "
                "$\\mathbf{A}$ ning "
                "shartlanganligini emas, "
                "**yakuniy** tizim "
                "matritsasini o'lchash "
                "kerak. Mavzuning amaliy "
                "markazi esa 11- va "
                "12-qadamlarda. DQM "
                "matritsalari to'la va "
                "shartlanganligi "
                "$N^{2m}$ kabi o'sadi: "
                "to'rtinchi tartibli "
                "masalada $N = 19$ da u "
                "allaqachon "
                "$1{,}5\\cdot10^{8}$. "
                "Demak $N$ ni cheksiz "
                "oshirib bo'lmaydi — "
                "amalda 20–30 chegara. "
                "Ayni paytda shuncha "
                "nuqta ko'p masalalar "
                "uchun yetarlidan "
                "ortiq: kod ko'rsatadiki, "
                "13 ta nuqta balkaning "
                "birinchi uchta "
                "chastotasini besh-olti "
                "xonali aniqlikda beradi. "
                "Shunday qilib DQM ning "
                "o'rni aniq: muntazam "
                "geometriya va silliq "
                "yechim bo'lganda u "
                "raqobatsiz, murakkab "
                "geometriya yoki "
                "singulyarlik "
                "bo'lganda esa FEM "
                "afzal. Bu 'qaysi usul "
                "yaxshiroq' degan "
                "savolning noto'g'ri "
                "qo'yilganini "
                "ko'rsatadi — to'g'ri "
                "savol 'qaysi masala "
                "uchun'."
            ),
            equations=[
                eq(r"\left.\frac{d^mf}{dx^m}"
                   r"\right|_{x_i} = "
                   r"\sum_{j=1}^{N}"
                   r"A^{(m)}_{ij}f(x_j)",
                   "Differensial "
                   "kvadraturaning asosiy "
                   "taxmini.", "DQM taxmini"),
                eq(r"A_{ij} = \frac{M(x_i)}"
                   r"{(x_i-x_j)M(x_j)}, \quad "
                   r"A_{ii} = -\sum_{j\ne i}"
                   r"A_{ij}",
                   "Vazn koeffitsientlarining "
                   "yopiq formulasi.",
                   "Vazn koeffitsientlari"),
                eq(r"x_i = \frac{L}{2}\left(1 - "
                   r"\cos\frac{\pi i}{N-1}"
                   r"\right), \quad i = 0"
                   r"\dots N-1",
                   "Chebishev–Gauss–Lobatto "
                   "tugunlari.", "CGL tugunlari"),
                eq(r"\|e\| \sim e^{-\sigma N}, "
                   r"\qquad \kappa \sim N^{2m}",
                   "Spektral yaqinlashish va "
                   "uning shartlanganlik "
                   "bo'yicha narxi.",
                   "Afzallik va narx"),
            ],
            conditions=(
                "**DQM qachon mos:**\n"
                "- Geometriya muntazam "
                "(to'rtburchak, doira, "
                "halqa);\n"
                "- Yechim **silliq** — "
                "singulyarlik yo'q;\n"
                "- Koeffitsientlar uzluksiz;\n"
                "- Kam noma'lum bilan yuqori "
                "aniqlik kerak (parametrik "
                "tadqiqot).\n\n"
                "**DQM qachon mos emas:**\n"
                "- Murakkab geometriya;\n"
                "- Yorilish, burchak, "
                "kontakt — singulyarlik "
                "spektral yaqinlashishni "
                "**yo'q qiladi**;\n"
                "- Mahalliy zichlashtirish "
                "kerak bo'lsa (su-18);\n"
                "- Juda katta $N$ — "
                "shartlanganlik "
                "$N^{2m}$ kabi o'sadi.\n\n"
                "**Amaliy tavsiyalar:**\n"
                "1. Har doim CGL yoki shunga "
                "o'xshash zichlashgan "
                "tugunlardan foydalaning;\n"
                "2. $N = 11$–$21$ odatda "
                "optimal; kattaroq $N$ "
                "yaxlitlash tufayli "
                "**yomonroq** natija "
                "berishi mumkin;\n"
                "3. Faqat birinchi "
                "$\\sim N/3$ xususiy "
                "qiymatga ishoning — "
                "yuqorigilari soxta;\n"
                "4. $\\mathbf{A}$ ning "
                "singulyarligi normal; "
                "yakuniy tizimni "
                "tekshiring.\n\n"
                "**Tekshiruv:** vazn "
                "koeffitsientlarini "
                "ko'phadlarda sinab "
                "ko'ring — $N$ nuqta "
                "$(N-1)$-darajagacha "
                "aynan bo'lishi shart."
            ),
            worked=WorkedExample(
                statement=(
                    "$N = 3$ nuqtali tekis "
                    "to'rda ($x = 0,\\ L/2,\\ "
                    "L$) birinchi hosila vazn "
                    "koeffitsientlarini "
                    "toping va ular chekli "
                    "ayirmalar bilan mos "
                    "kelishini tekshiring."
                ),
                given=[
                    r"x_1 = 0,\quad x_2 = L/2, "
                    r"\quad x_3 = L",
                    r"A_{ij} = \frac{M(x_i)}"
                    r"{(x_i-x_j)M(x_j)}",
                ],
                steps=[
                    st(r"M(x_1) = (x_1-x_2)"
                       r"(x_1-x_3) = \left("
                       r"-\frac{L}{2}\right)"
                       r"(-L) = \frac{L^2}{2}",
                       "Birinchi tugun uchun."),
                    st(r"M(x_2) = \left("
                       r"\frac{L}{2}\right)"
                       r"\left(-\frac{L}{2}"
                       r"\right) = "
                       r"-\frac{L^2}{4}",
                       "O'rta tugun."),
                    st(r"M(x_3) = (L)\left("
                       r"\frac{L}{2}\right) = "
                       r"\frac{L^2}{2}",
                       "Oxirgi tugun."),
                    st(r"A_{12} = \frac{M(x_1)}"
                       r"{(x_1-x_2)M(x_2)} = "
                       r"\frac{L^2/2}{(-L/2)"
                       r"(-L^2/4)}",
                       "Formulaga qo'yamiz."),
                    st(r"= \frac{L^2/2}{L^3/8} = "
                       r"\frac{4}{L}",
                       "Soddalashtiramiz."),
                    st(r"A_{13} = \frac{L^2/2}"
                       r"{(-L)(L^2/2)} = "
                       r"-\frac{1}{L}",
                       "Uchinchi ustun."),
                    st(r"A_{11} = -(A_{12} + "
                       r"A_{13}) = -\frac{4}{L} "
                       r"+ \frac{1}{L} = "
                       r"-\frac{3}{L}",
                       "Diagonal — qator "
                       "yig'indisi noli "
                       "shartidan."),
                    st(r"\left.\frac{df}{dx}"
                       r"\right|_{x_1} = "
                       r"\frac{-3f_1 + 4f_2 - "
                       r"f_3}{L}",
                       "**Tanish formula!**"),
                    st(r"h = L/2 "
                       r"\;\Rightarrow\; "
                       r"\frac{-3f_1 + 4f_2 - "
                       r"f_3}{2h}",
                       "$h$ orqali yozsak."),
                    st(r"\text{Bu su-07 dagi "
                       r"IKKINCHI TARTIBLI "
                       r"bir tomonlama "
                       r"formula}",
                       "**Mustaqil tasdiq.** "
                       "DQM chekli "
                       "ayirmalarning "
                       "umumlashmasi ekani "
                       "shundan ko'rinadi."),
                    st(r"A_{21} = \frac{-L^2/4}"
                       r"{(L/2)(L^2/2)} = "
                       r"-\frac{1}{L}, \ "
                       r"A_{23} = \frac{1}{L}",
                       "O'rta tugun qatori."),
                    st(r"\left.\frac{df}{dx}"
                       r"\right|_{x_2} = "
                       r"\frac{f_3 - f_1}{L} = "
                       r"\frac{f_3-f_1}{2h}",
                       "**Markaziy ayirma** — "
                       "yana tanish formula."),
                ],
                answer=(
                    "$\\mathbf{A} = "
                    "\\frac{1}{L}"
                    "\\begin{bmatrix} -3 & 4 & "
                    "-1\\\\ -1 & 0 & 1\\\\ "
                    "1 & -4 & 3\\end{bmatrix}$. "
                    "Qatorlar aynan su-07 dagi "
                    "ikkinchi tartibli bir "
                    "tomonlama va markaziy "
                    "ayirma formulalari. "
                    "Ya'ni $N = 3$ da DQM "
                    "chekli ayirmalarga "
                    "**aylanadi**; farq "
                    "$N$ oshgani sari paydo "
                    "bo'ladi, chunki DQM "
                    "barcha nuqtalarni "
                    "ishlatadi."
                ),
                engineering_note=(
                    "Bu natija DQM ning "
                    "o'rnini aniq "
                    "belgilaydi: u chekli "
                    "ayirmalarning raqibi "
                    "emas, **umumlashmasi**. "
                    "$N = 3$ da ikkalasi bir "
                    "xil, lekin chekli "
                    "ayirmalarda $N$ "
                    "oshganda odatda "
                    "shablon (stencil) "
                    "kengligi qat'iy "
                    "qoldiriladi va faqat "
                    "$h$ kichrayadi — "
                    "shuning uchun tartib "
                    "$h^p$ da qotib "
                    "qoladi. DQM da esa "
                    "shablon butun sohani "
                    "qamrab oladi va "
                    "tartib $N$ bilan "
                    "birga o'sadi. "
                    "Amaliy tanlov "
                    "shundan kelib "
                    "chiqadi: yechim "
                    "silliq bo'lsa DQM "
                    "ning global shabloni "
                    "ulkan yutuq beradi; "
                    "yechimda "
                    "singulyarlik yoki "
                    "uzilish bo'lsa esa "
                    "o'sha global shablon "
                    "kamchilikka aylanadi — "
                    "bitta yomon nuqta "
                    "**barcha** "
                    "tugunlardagi "
                    "hosilani buzadi. "
                    "Chekli ayirmalar va "
                    "FEM da buzilish "
                    "mahalliy qoladi. "
                    "Shuning uchun yorilish "
                    "yoki kontakt "
                    "masalalarida DQM "
                    "deyarli "
                    "ishlatilmaydi."
                ),
            ),
            computation=Computation(
                caption=(
                    "Vazn koeffitsientlarini "
                    "qurish va tekshirish, "
                    "spektral yaqinlashishni "
                    "o'lchash, balka "
                    "chastotalarini topish va "
                    "FEM bilan taqqoslash."
                ),
                code='''"""Differensial kvadratura usuli (DQM)."""
import numpy as np
from labkit import PARAMS, note, series, table, value
from scipy.linalg import eig, eigh
from scipy.optimize import brentq

N_pts = int(PARAMS.get("N_pts", 13))
grid_kind = float(PARAMS.get("grid_kind", 1.0))   # 1 = CGL, 0 = tekis
L_b = float(PARAMS.get("L_b", 1.0))


def grid_uniform(N, L=1.0):
    return np.linspace(0.0, L, N)


def grid_cgl(N, L=1.0):
    """Chebishev-Gauss-Lobatto: chekkalarda zich."""
    return L*0.5*(1 - np.cos(np.pi*np.arange(N)/(N - 1)))


def dqm_A(x):
    """Birinchi hosila vazn koeffitsientlari."""
    N = len(x)
    A = np.zeros((N, N))
    Mv = np.array([np.prod([x[i] - x[k] for k in range(N) if k != i])
                   for i in range(N)])
    for i in range(N):
        for j in range(N):
            if i != j:
                A[i, j] = Mv[i]/((x[i] - x[j])*Mv[j])
    for i in range(N):
        A[i, i] = -np.sum([A[i, j] for j in range(N) if j != i])
    return A


# --- (0) N = 3 da DQM chekli ayirmalarga AYLANADIMI? ---
x3 = grid_uniform(3, L_b)
A3 = dqm_A(x3)*L_b
table("N = 3 da vazn matritsasi (1/L birligida)",
      ["ustun 1", "ustun 2", "ustun 3"],
      [[f"{v:+.6f}" for v in row] for row in A3])
value("A[0] qatori su-07 dagi (-3, 4, -1) ga mos farqi",
      float(np.max(np.abs(A3[0] - np.array([-3.0, 4.0, -1.0])))), "—")
value("A[1] qatori markaziy ayirma (-1, 0, 1) dan farqi",
      float(np.max(np.abs(A3[1] - np.array([-1.0, 0.0, 1.0])))), "—")
note("N = 3 da DQM vazn matritsasi AYNAN su-07 dagi chekli ayirma "
     "formulalarini beradi: birinchi qator ikkinchi tartibli bir "
     "tomonlama (-3, 4, -1)/2h, o'rta qator esa markaziy ayirma "
     "(-1, 0, 1)/2h. Demak DQM chekli ayirmalarning raqibi emas, "
     "UMUMLASHMASI: farq N oshgani sari paydo bo'ladi, chunki DQM "
     "shabloni butun sohani qamrab oladi.")

# --- (1) A SINGULYAR - bu xato emas ---
rows0 = []
for N in [5, 9, 13, 17]:
    x = grid_cgl(N, L_b)
    A = dqm_A(x)
    rows0.append([N, f"{np.max(np.abs(A @ np.ones(N))):.2e}",
                  int(np.linalg.matrix_rank(A)), N])
table("Vazn matritsasining rangi",
      ["N", "max|A @ 1|", "rang", "o'lcham"], rows0)
note("A matritsasi HAR DOIM singulyar: rangi N - 1 ga teng, chunki "
     "doimiy funksiyaning hosilasi nol, ya'ni A @ 1 = 0. Bu xato "
     "emas va uni 'tuzatish' kerak emas - chegaraviy shartlar "
     "qo'llangandan keyin tizim yechiluvchan bo'ladi. Shuning uchun "
     "DQM kodini tekshirishda A ning emas, YAKUNIY tizim "
     "matritsasining shartlanganligi o'lchanadi.")

# --- (2) KO'PHADLARDA AYNAN differensiallaydimi? ---
rows = []
for N in [5, 9, 13]:
    x = grid_cgl(N, L_b)
    A = dqm_A(x)
    A2 = A @ A
    A4 = A2 @ A2
    line = [N]
    for pdeg in [1, 2, N - 2, N - 1, N]:
        f = x**pdeg
        d1 = A @ f
        ex1 = pdeg*x**(pdeg - 1)
        denom = max(float(np.max(np.abs(ex1))), 1e-30)
        line.append(f"{float(np.max(np.abs(d1 - ex1)))/denom:.1e}")
    f6 = x**6
    d4 = A4 @ f6
    ex4 = 360.0*x**2
    line.append(f"{float(np.max(np.abs(d4 - ex4)))/float(np.max(np.abs(ex4))):.1e}")
    rows.append(line)
table("Ko'phadlarni aynan differensiallash (nisbiy xato)",
      ["N", "x^1", "x^2", "x^(N-2)", "x^(N-1)", "x^N",
       "x^6 ning 4-hosilasi"], rows)
note("N nuqta (N-1)-darajali ko'phadni AYNAN differensiallaydi "
     "(1e-15 darajasida), N-darajalisida esa xato paydo bo'ladi - "
     "bu aniq kutilgan chegara. To'rtinchi hosila uchun esa kamida "
     "N = 7 kerak: N = 5 da bazis atigi 4-darajali va x^6 ning "
     "to'rtinchi hosilasi umuman topilmaydi (xato 0.7). Bu balka "
     "masalasida N ning quyi chegarasini belgilaydi.")

# --- (3) SPEKTRAL yaqinlashish va tugun taqsimotining roli ---
rows2 = []
Ns = [5, 7, 9, 11, 13, 15, 17, 21, 25]
eu, ec = [], []
for N in Ns:
    line = [N]
    for gname, gf in [("tekis", grid_uniform), ("CGL", grid_cgl)]:
        x = gf(N, L_b)
        A = dqm_A(x)
        f = np.sin(2*np.pi*x/L_b)
        d = A @ f
        ex = 2*np.pi/L_b*np.cos(2*np.pi*x/L_b)
        e = float(np.max(np.abs(d - ex)))/float(np.max(np.abs(ex)))
        line.append(f"{e:.3e}")
        (eu if gname == "tekis" else ec).append(e)
    rows2.append(line)
table("sin(2 pi x/L) hosilasi: tugun taqsimotining ta'siri",
      ["N", "tekis tugunlar", "CGL tugunlar"], rows2)
series("Tekis tugunlar", Ns, [np.log10(max(v, 1e-18)) for v in eu],
       xlabel="N", ylabel="log10(nisbiy xato)")
series("CGL tugunlar", Ns, [np.log10(max(v, 1e-18)) for v in ec],
       xlabel="N", ylabel="log10(nisbiy xato)")
value("CGL: N = 5 dagi xato", float(ec[0]), "—")
value("CGL: N = 21 dagi xato", float(ec[Ns.index(21)]), "—")
value("Tekis: N = 21 dagi xato", float(eu[Ns.index(21)]), "—")
note("EKSPONENSIAL YAQINLASHISH. CGL tugunlarida xato N = 5 da 0.43 "
     "dan N = 21 da 1.4e-14 ga tushadi - ya'ni har qo'shilgan ikki "
     "nuqta xatoni taxminan yuz barobar kamaytiradi. Darajali "
     "usullarda (su-07, FEM) bunday bo'lmaydi: u yerda xato faqat "
     "h^p kabi kamayadi. Tekis tugunlar ham yaqinlashadi, lekin "
     "N = 21 da uch tartib yomonroq va N ortgani sari Runge hodisasi "
     "(su-14) kuchayadi. Shuning uchun DQM da CGL yoki shunga "
     "o'xshash zichlashgan tugunlar MAJBURIY.")

# --- (4) BALKA CHASTOTALARI: kam nuqta bilan yuqori aniqlik ---
def beam_dqm(N, bc, L=1.0):
    x = grid_cgl(N, L)
    A = dqm_A(x)
    A2 = A @ A
    A3 = A2 @ A
    A4 = A2 @ A2
    K = A4.astype(float).copy()
    Mm = np.eye(N)
    if bc == "ss":
        rows_bc = [(0, np.eye(N)[0]), (1, A2[0]),
                   (N - 2, A2[-1]), (N - 1, np.eye(N)[-1])]
    elif bc == "cant":
        rows_bc = [(0, np.eye(N)[0]), (1, A[0]),
                   (N - 2, A2[-1]), (N - 1, A3[-1])]
    else:      # ikki uchi mahkam
        rows_bc = [(0, np.eye(N)[0]), (1, A[0]),
                   (N - 2, A[-1]), (N - 1, np.eye(N)[-1])]
    for r, vec in rows_bc:
        K[r, :] = vec
        Mm[r, :] = 0.0
    ev = eig(K, Mm)[0]
    ev = ev[np.isfinite(ev)]
    ev = ev[np.abs(ev.imag) < 1e-6*np.maximum(np.abs(ev.real), 1e-30)].real
    ev = np.sort(ev[ev > 1e-6])
    return np.power(ev, 0.25)


bl_cant = [brentq(lambda b: np.cos(b)*np.cosh(b) + 1.0, a, b)
           for a, b in [(1.0, 2.5), (4.0, 5.5), (7.0, 8.5)]]
bl_ff = [brentq(lambda b: np.cos(b)*np.cosh(b) - 1.0, a, b)
         for a, b in [(4.0, 5.5), (7.0, 8.5), (10.0, 11.5)]]
bl_ss = [np.pi, 2*np.pi, 3*np.pi]
rows3 = []
for bc, exact, nm in [("ss", bl_ss, "sharnirli"),
                      ("cant", bl_cant, "konsol"),
                      ("ff", bl_ff, "mahkam-mahkam")]:
    for N in [9, 11, 13, 15]:
        b = beam_dqm(N, bc, L_b)[:3]
        rows3.append([nm, N] +
                     [f"{abs(b[i]/exact[i] - 1)*100:.3e}"
                      if i < len(b) else "—" for i in range(3)])
table("DQM: balka chastotalarining nisbiy xatosi, %",
      ["chegaraviy shart", "N", "1-shakl", "2-shakl", "3-shakl"], rows3)
b13 = beam_dqm(13, "ss", L_b)
value("N = 13, sharnirli: 1-shakl xatosi",
      float(abs(b13[0]/np.pi - 1)*100), "%")
value("N = 13, sharnirli: 3-shakl xatosi",
      float(abs(b13[2]/(3*np.pi) - 1)*100), "%")
note("ATIGI 13 NUQTA balkaning birinchi uchta chastotasini besh-olti "
     "xonali aniqlikda beradi va bu uchala chegaraviy shart uchun ham "
     "amal qiladi. su-23 da FEM bilan shunga yaqin aniqlik uchun "
     "16-32 element (33-66 erkinlik darajasi) kerak edi. DIQQAT: "
     "eng yuqori hisoblangan shakllar ishonchsiz - taxminan birinchi "
     "N/3 xususiy qiymatga ishonish mumkin, qolganlari soxta.")

# --- (5) DQM va FEM: BIR XIL noma'lumlar sonida ---
def fem_beam(n):
    h = L_b/n
    EI, mA = 1.0, 1.0

    def ke(Le):
        return EI/Le**3*np.array([
            [12, 6*Le, -12, 6*Le], [6*Le, 4*Le**2, -6*Le, 2*Le**2],
            [-12, -6*Le, 12, -6*Le],
            [6*Le, 2*Le**2, -6*Le, 4*Le**2]], dtype=float)

    def me(Le):
        return mA*Le/420*np.array([
            [156, 22*Le, 54, -13*Le],
            [22*Le, 4*Le**2, 13*Le, -3*Le**2],
            [54, 13*Le, 156, -22*Le],
            [-13*Le, -3*Le**2, -22*Le, 4*Le**2]], dtype=float)

    nd = 2*(n + 1)
    K = np.zeros((nd, nd))
    Mm = np.zeros((nd, nd))
    for e in range(n):
        idx = [2*e, 2*e + 1, 2*e + 2, 2*e + 3]
        K[np.ix_(idx, idx)] += ke(h)
        Mm[np.ix_(idx, idx)] += me(h)
    free = np.setdiff1d(np.arange(nd), [0, 2*n])
    w = np.sqrt(np.sort(eigh(K[np.ix_(free, free)],
                             Mm[np.ix_(free, free)], eigvals_only=True)))
    return np.power(w, 0.5), len(free)


rows4 = []
for N in [9, 11, 13, 15]:
    b = beam_dqm(N, "ss", L_b)[:3]
    rows4.append([f"DQM N={N}", N] +
                 [f"{abs(b[i]/bl_ss[i] - 1)*100:.3e}" for i in range(3)])
for n in [4, 6, 8]:
    b, nd = fem_beam(n)
    rows4.append([f"FEM n={n}", nd] +
                 [f"{abs(b[i]/bl_ss[i] - 1)*100:.3e}" for i in range(3)])
table("DQM va FEM bir xil noma'lumlar sonida (sharnirli balka, xato %)",
      ["usul", "noma'lumlar", "1-shakl", "2-shakl", "3-shakl"], rows4)
note("DQM 13 noma'lum bilan birinchi chastotani 1.9e-7% aniqlikda "
     "beradi, FEM esa 16 noma'lum bilan 8.2e-4% - ya'ni DQM kamroq "
     "noma'lum bilan to'rt ming barobar aniqroq. Lekin ustunlik "
     "shakl raqami oshgani sari kamayadi: 3-shaklda farq atigi uch "
     "barobar. Sabab - yuqori shakllar tezroq tebranadi va spektral "
     "usulning afzalligi faqat SILLIQ, kam to'lqinli yechimlarda "
     "to'liq namoyon bo'ladi.")

# --- (6) NARXI: zichlik va shartlanganlik ---
def sys_dqm(N):
    x = grid_cgl(N, L_b)
    A = dqm_A(x)
    A2 = A @ A
    K = (A2 @ A2).copy()
    for r, vec in [(0, np.eye(N)[0]), (1, A2[0]),
                   (N - 2, A2[-1]), (N - 1, np.eye(N)[-1])]:
        K[r, :] = vec
    return K


def sys_fem(n):
    h = L_b/n

    def ke(Le):
        return 1.0/Le**3*np.array([
            [12, 6*Le, -12, 6*Le], [6*Le, 4*Le**2, -6*Le, 2*Le**2],
            [-12, -6*Le, 12, -6*Le],
            [6*Le, 2*Le**2, -6*Le, 4*Le**2]], dtype=float)

    nd = 2*(n + 1)
    K = np.zeros((nd, nd))
    for e in range(n):
        idx = [2*e, 2*e + 1, 2*e + 2, 2*e + 3]
        K[np.ix_(idx, idx)] += ke(h)
    free = np.setdiff1d(np.arange(nd), [0, 2*n])
    return K[np.ix_(free, free)]


rows5 = []
cd, sz = [], []
for k in [7, 11, 15, 19, 23]:
    Kd = sys_dqm(k)
    Kf = sys_fem(max(k//2, 2))
    dens_d = np.count_nonzero(np.abs(Kd) > 1e-12)/Kd.size*100
    dens_f = np.count_nonzero(np.abs(Kf) > 1e-12)/Kf.size*100
    rows5.append([k, f"{np.linalg.cond(Kd):.2e}", f"{dens_d:.1f}",
                  Kf.shape[0], f"{np.linalg.cond(Kf):.2e}",
                  f"{dens_f:.1f}"])
    cd.append(float(np.linalg.cond(Kd)))
    sz.append(k)
table("DQM ning narxi: zichlik va shartlanganlik",
      ["N", "DQM cond", "DQM zichlik %", "FEM n", "FEM cond",
       "FEM zichlik %"], rows5)
slope = float(np.polyfit(np.log(sz), np.log(cd), 1)[0])
value("DQM shartlanganligi: cond ~ N^m, m =", slope, "—")
value("Nazariy 2m (m = 4 - hosila tartibi)", 8.0, "—")
series("DQM shartlanganligi", [np.log10(s) for s in sz],
       [np.log10(c) for c in cd], xlabel="log10(N)", ylabel="log10(cond)")
note(f"DQM ning narxi ikki tomonlama. Birinchidan, matritsa deyarli "
     f"TO'LA (N = 23 da 90%), FEM matritsasi esa N oshgani sari "
     f"siyraklashadi (25%) - demak katta masalalarda DQM xotira va "
     f"vaqt bo'yicha yutqazadi. Ikkinchidan, shartlanganlik "
     f"N^{slope:.1f} kabi o'sadi va bu nazariy N^(2m) = N^8 "
     f"bashoratiga mos keladi (m = 4 - hosila tartibi). N = 23 da "
     f"cond allaqachon 1e9 dan oshadi, shuning uchun amalda "
     f"N = 20-30 chegara bo'lib qoladi. Kattaroq N yaxlitlash "
     f"tufayli natijani YOMONLASHTIRISHI mumkin.")

table("DQM va boshqa usullarning taqqoslanishi",
      ["Jihat", "Chekli ayirmalar", "FEM", "DQM"],
      [["Shablon", "mahalliy", "mahalliy", "GLOBAL"],
       ["Yaqinlashish", "h^p (darajali)", "h^p (darajali)",
        "EKSPONENSIAL"],
       ["Matritsa", "siyrak", "siyrak/lentali", "TO'LA"],
       ["Murakkab geometriya", "qiyin", "OSON", "qiyin"],
       ["Singulyarlik", "mahalliy buzilish", "adaptivlik bilan",
        "BUTUN yechim buziladi"],
       ["Mahalliy zichlashtirish", "mumkin", "OSON", "qiyin"],
       ["Eng yaxshi soha", "sodda to'r", "universal",
        "muntazam + silliq"]])
''',
                parameters=[
                    p("N_pts", "DQM tugunlari soni", 5.0, 25.0, 13.0,
                      2.0),
                    p("grid_kind", "Tugun turi (1 = CGL, 0 = tekis)",
                      0.0, 1.0, 1.0, 1.0),
                    p("L_b", "Soha uzunligi", 0.5, 5.0, 1.0, 0.5, "m"),
                ],
                expected_output=(
                    "$N = 3$ da vazn "
                    "matritsasi aynan su-07 "
                    "dagi chekli ayirma "
                    "formulalarini beradi. "
                    "$\\mathbf{A}$ har doim "
                    "singulyar (rang "
                    "$N-1$), chunki "
                    "$\\mathbf{A}\\mathbf{1} "
                    "= \\mathbf{0}$. "
                    "$N$ nuqta "
                    "$(N-1)$-darajali "
                    "ko'phadni "
                    "$10^{-15}$ aniqlikda "
                    "differensiallaydi; "
                    "to'rtinchi hosila uchun "
                    "kamida $N = 7$ kerak. "
                    "CGL tugunlarida sinus "
                    "hosilasining xatosi "
                    "$N = 5$ da 0,43 dan "
                    "$N = 21$ da "
                    "$1{,}4\\cdot10^{-14}$ "
                    "ga tushadi — "
                    "eksponensial "
                    "yaqinlashish; tekis "
                    "tugunlar uch tartib "
                    "yomonroq. 13 nuqta "
                    "balkaning birinchi "
                    "uchta chastotasini "
                    "besh-olti xonali "
                    "aniqlikda beradi va "
                    "bir xil noma'lumlar "
                    "sonida FEM dan to'rt "
                    "ming barobar aniqroq. "
                    "Narxi: matritsa 90% "
                    "to'la va "
                    "shartlanganlik "
                    "$N^{8}$ kabi o'sadi."
                ),
            ),
            visual=vis(
                kind="DQM: tugunlar, yaqinlashish va matritsa",
                tool="React/SVG + Manim",
                description=(
                    "Tugun taqsimotlari, "
                    "spektral yaqinlashish "
                    "egri chizig'i va "
                    "matritsa to'ldirilishi."
                ),
                how_to_draw=(
                    "React/SVG: yuqori panelda "
                    "ikkita o'q yonma-yon — "
                    "tekis tugunlar va CGL "
                    "tugunlari; CGL da "
                    "nuqtalar chekkalarda "
                    "quyuqlashgani ko'rinadi "
                    "va $N$ slayderi bilan "
                    "bu farq kuchayadi. "
                    "O'rta panelda "
                    "yaqinlashish grafigi "
                    "yarim logarifmik "
                    "o'qda: DQM chizig'i "
                    "**to'g'ri chiziq** "
                    "bo'lib pastga tushadi "
                    "(eksponensial), FEM va "
                    "chekli ayirmalar "
                    "chiziqlari esa "
                    "log–log o'qda "
                    "to'g'ri bo'ladi "
                    "(darajali) — ikki "
                    "o'q turini "
                    "almashtirish tugmasi "
                    "shu farqni ochib "
                    "beradi. Pastki "
                    "panelda ikkita "
                    "matritsa xaritasi: "
                    "DQM niki deyarli "
                    "butunlay to'ldirilgan, "
                    "FEM niki esa ingichka "
                    "lenta (su-15). "
                    "Har birining ostida "
                    "shartlanganlik soni "
                    "va zichlik foizi "
                    "turadi; $N$ "
                    "oshgani sari DQM "
                    "xaritasi to'q "
                    "qolaveradi, FEM "
                    "lentasi esa "
                    "nisbatan "
                    "ingichkalashadi."
                ),
            ),
            interp=(
                "$N = 3$ tajribasi DQM ning "
                "o'rnini darhol "
                "belgilaydi: u chekli "
                "ayirmalarning raqibi emas, "
                "umumlashmasi. Vazn "
                "matritsasining qatorlari "
                "aynan su-07 dagi tanish "
                "formulalar. Farq $N$ "
                "oshgani sari paydo "
                "bo'ladi va uning "
                "manbai — shablon "
                "kengligi. Chekli "
                "ayirmalarda shablon "
                "qat'iy qoladi va faqat "
                "$h$ kichrayadi, DQM da "
                "esa shablon butun sohani "
                "qamrab oladi, shuning "
                "uchun tartib $N$ bilan "
                "birga o'sadi. Natija "
                "spektral yaqinlashish: "
                "CGL tugunlarida xato "
                "$N = 5$ dan $N = 21$ ga "
                "o'tishda 13 tartibga "
                "tushadi. Tekis "
                "tugunlarning uch tartib "
                "yomonroq bo'lishi esa "
                "su-14 dagi Runge "
                "hodisasining bevosita "
                "davomi — DQM da tugun "
                "taqsimoti tanlovi "
                "bezak emas, zarurat. "
                "Balka tajribasi amaliy "
                "kuchni ko'rsatadi: 13 "
                "nuqta uchala chegaraviy "
                "shart uchun ham birinchi "
                "uchta chastotani "
                "besh-olti xonali "
                "aniqlikda beradi, "
                "holbuki su-23 da FEM "
                "shunga yaqin natija "
                "uchun 33–66 erkinlik "
                "darajasini talab "
                "qilgandi. Bevosita "
                "taqqoslash buni "
                "raqamlashtiradi: bir "
                "xil noma'lumlar sonida "
                "DQM birinchi chastotada "
                "to'rt ming barobar "
                "aniqroq. Lekin oxirgi "
                "ikki jadval "
                "muvozanatni tiklaydi. "
                "Ustunlik shakl raqami "
                "oshgani sari kamayadi — "
                "uchinchi shaklda atigi "
                "uch barobar, chunki "
                "spektral usulning "
                "afzalligi silliq, kam "
                "to'lqinli yechimlarda "
                "to'liq namoyon bo'ladi. "
                "Va narxi jiddiy: "
                "matritsa 90% to'la, "
                "shartlanganlik esa "
                "o'lchov bo'yicha "
                "$N^{8}$ kabi o'sadi — "
                "bu nazariy "
                "$N^{2m}$ bashoratiga "
                "aniq mos keladi. "
                "Shunday qilib "
                "'qaysi usul yaxshiroq' "
                "degan savol noto'g'ri "
                "qo'yilgan: to'g'ri "
                "savol — qaysi masala "
                "uchun."
            ),
            mistakes=[
                "$\\mathbf{A}$ ning "
                "singulyarligini xato deb "
                "hisoblash. "
                "$\\mathbf{A}\\mathbf{1} = "
                "\\mathbf{0}$ fizik "
                "zarurat; yakuniy tizimni "
                "tekshiring.",
                "Tekis tugunlardan "
                "foydalanish. Katta $N$ da "
                "Runge hodisasi "
                "yaqinlashishni buzadi — "
                "CGL majburiy.",
                "$N$ ni cheksiz oshirish. "
                "$\\kappa \\sim N^{8}$, "
                "shuning uchun $N > 30$ da "
                "natija **yomonlashishi** "
                "mumkin.",
                "Barcha hisoblangan xususiy "
                "qiymatlarga ishonish. "
                "Faqat birinchi "
                "$\\sim N/3$ tasi "
                "ishonchli.",
                "Singulyarlik bor masalada "
                "DQM ishlatish. Global "
                "shablon tufayli bitta "
                "yomon nuqta butun "
                "yechimni buzadi.",
                "To'rtinchi tartibli "
                "masalada $N < 7$ olish. "
                "Bazis to'rtinchi hosilani "
                "umuman ifodalay "
                "olmaydi.",
            ],
            quiz=[
                q("DQM chekli ayirmalardan "
                  "nimasi bilan farq qiladi?",
                  "Shablon **global**: hosila "
                  "barcha tugunlardagi "
                  "qiymatlarning "
                  "kombinatsiyasi, chekli "
                  "ayirmalarda esa faqat "
                  "qo'shnilarning.",
                  "konseptual"),
                q("Nima uchun "
                  "$\\mathbf{A}$ singulyar?",
                  "Doimiy funksiyaning "
                  "hosilasi nol, demak "
                  "$\\mathbf{A}\\mathbf{1} = "
                  "\\mathbf{0}$ — rang "
                  "$N-1$. Bu diagonal "
                  "hadlarning ta'rifidan "
                  "kelib chiqadi.",
                  "konseptual"),
                q("$N = 3$ tekis to'rda "
                  "$A_{11}$ nechaga teng?",
                  "$A_{12} = 4/L$, "
                  "$A_{13} = -1/L$, demak "
                  "$A_{11} = -3/L$ — bu "
                  "su-07 dagi ikkinchi "
                  "tartibli bir tomonlama "
                  "formula.", "hisob"),
                q("Kod spektral "
                  "yaqinlashishni qanday "
                  "ko'rsatadi?",
                  "CGL tugunlarida sinus "
                  "hosilasining xatosi "
                  "$N = 5$ da 0,43 dan "
                  "$N = 21$ da "
                  "$1{,}4\\cdot10^{-14}$ ga "
                  "tushadi — 13 tartib.",
                  "kod"),
                q("DQM ning ikki asosiy "
                  "narxi nima?",
                  "Matritsa to'la (kodda 90%) "
                  "va shartlanganlik "
                  "$N^{2m}$ kabi o'sadi "
                  "(o'lchangan $N^{8}$), "
                  "shuning uchun $N$ "
                  "20–30 bilan "
                  "cheklanadi.", "kod"),
                q("Nima uchun DQM "
                  "singulyarlik bor "
                  "masalalarda yomon "
                  "ishlaydi?",
                  "Shablon global: bitta "
                  "yomon nuqta **barcha** "
                  "tugunlardagi hosilani "
                  "buzadi. FEM va chekli "
                  "ayirmalarda buzilish "
                  "mahalliy qoladi.",
                  "talqin"),
                q("DQM ning afzalligi nima "
                  "uchun yuqori shakllarda "
                  "kamayadi?",
                  "Spektral yaqinlashish "
                  "silliq, kam to'lqinli "
                  "yechimlarda to'liq "
                  "namoyon bo'ladi; yuqori "
                  "shakllar tezroq "
                  "tebranadi. Kodda "
                  "ustunlik 4000 barobardan "
                  "3 barobarga tushadi.",
                  "talqin"),
            ],
            bridge=(
                "DQM butun sohani tugunlar "
                "bilan to'ldirdi. Keyingi "
                "mavzudagi usul esa butunlay "
                "boshqacha yo'l tutadi: "
                "faqat **chegarani** "
                "diskretlashtiradi va soha "
                "ichiga umuman tegmaydi — "
                "bu o'lchamni bittaga "
                "kamaytiradi."
            ),
            research=(
                "DQM ni kengaytiring. "
                "(1) Umumlashgan DQM (GDQ) "
                "va harmonik DQM ni "
                "o'rganing: ko'phad "
                "o'rniga trigonometrik "
                "bazis tanlansa davriy "
                "masalalarda nima "
                "o'zgaradi? "
                "(2) Chegaraviy shartlarni "
                "qo'llashning turli "
                "usullarini (delta "
                "texnikasi, MMWC) "
                "taqqoslang: qaysi biri "
                "aniqroq? "
                "(3) Ko'p sohali DQM ni "
                "(multi-domain) ko'rib "
                "chiqing: u murakkab "
                "geometriya va "
                "uzilishlarni qanday "
                "hal qiladi? "
                "(4) Spektral elementlar "
                "usulini o'rganing: u "
                "FEM ning mahalliyligini "
                "spektral aniqlik bilan "
                "birlashtiradi."
            ),
            manim_ref=manim(
                scene="DQMScene",
                module="manim/scenes/su_modern.py",
                title="Global shablon va spektral yaqinlashish",
                summary=(
                    "Avval chekli ayirma "
                    "shabloni ko'rsatiladi: "
                    "bitta nuqtadagi hosila "
                    "uchun faqat uchta "
                    "qo'shni yonadi. Keyin "
                    "DQM ga o'tiladi va "
                    "**barcha** tugunlar "
                    "bir vaqtda yonadi — "
                    "global shablon. So'ng "
                    "yaqinlashish grafigi "
                    "chiziladi: DQM "
                    "chizig'i yarim "
                    "logarifmik o'qda "
                    "to'g'ri chiziq bo'lib "
                    "keskin pastga tushadi, "
                    "darajali usullar esa "
                    "yotiqroq. Oxirida "
                    "matritsa xaritalari "
                    "taqqoslanadi: DQM to'la, "
                    "FEM lentali."
                ),
            ),
        ),
    ),

    # ------------------------------------------------------------------ su-26
    Topic(
        id="su-26",
        subject_id=S, module_id=M, order=26,
        title="Chegaraviy elementlar usuli (BEM)",
        description=(
            "Fundamental yechim, chegaraviy integral tenglama, o'lcham "
            "kamayishi, diskretlashtirish va yig'ish, ichki nuqtada "
            "yechim hamda degenerat masshtab muammosi."
        ),
        learning_objective=(
            "Chegaraviy integral tenglamani qurish va yechish, BEM ning "
            "FEM dan qachon afzal ekanini asoslash va uning o'ziga xos "
            "tuzoqlarini tanib olish."
        ),
        prerequisites=["su-25", "tmm-10"],
        mathematical_core=(
            "$c_iu_i + \\int_\\Gamma q^*u\\,d\\Gamma = "
            "\\int_\\Gamma u^*q\\,d\\Gamma$; "
            "$u^* = -\\frac{1}{2\\pi}\\ln r$; "
            "$\\mathbf{H}\\mathbf{u} = \\mathbf{G}\\mathbf{q}$."
        ),
        engineering_application=(
            "Cheksiz va yarim cheksiz sohalar (tuproq, akustika), "
            "yorilish mexanikasi, elektromagnit va issiqlik masalalari, "
            "shakl optimallashtirish."
        ),
        computational_component=(
            "Chegaraviy integrallarni hisoblash, matritsalarni yig'ish, "
            "ichki nuqtada yechimni tiklash, degenerat masshtabni "
            "aniqlash."
        ),
        visualization_component=(
            "Chegaraviy diskretlashtirish, fundamental yechim, ichki "
            "nuqtadagi maydon."
        ),
        research_extension=(
            "Tez ko'p qutbli usulni (FMM) o'rganing: u BEM ning "
            "$O(N^2)$ narxini $O(N\\log N)$ ga tushiradi."
        ),
        difficulty="murakkab",
        previous_link=(
            "su-25 dagi DQM butun sohani tugunlar bilan to'ldirdi. "
            "BEM esa butunlay boshqa yo'l tutadi: faqat **chegarani** "
            "diskretlashtiradi va soha ichiga umuman tegmaydi."
        ),
        next_topic="su-27",
        estimated_minutes=90,
        tags=["BEM", "chegaraviy integral", "fundamental yechim",
              "degenerat masshtab", "cheksiz soha"],
        lesson=_lesson(
            problem=(
                "Yerto'la devoriga tuproq "
                "bosimi hisoblanmoqda. "
                "Tuproq — **cheksiz** muhit: "
                "u har tomonga cheksiz "
                "davom etadi. FEM bilan "
                "modellashtirish uchun "
                "sun'iy chegara qo'yish "
                "kerak va u yetarlicha uzoq "
                "bo'lishi lozim — natijada "
                "to'rning katta qismi "
                "hech qanday qiziqarli "
                "narsa sodir bo'lmaydigan "
                "bo'sh tuproqqa sarflanadi. "
                "Bundan tashqari sun'iy "
                "chegara to'lqinlarni "
                "qaytaradi va dinamik "
                "masalada soxta aks-sado "
                "beradi. Cheksizlikni "
                "kesmasdan, uni "
                "**aynan** hisobga oladigan "
                "usul bormi?"
            ),
            concepts=[
                c("Fundamental yechim $u^*$",
                  "Nuqtaviy manba javobi: "
                  "ikki o'lchovda "
                  "$u^* = -\\frac{1}{2\\pi}"
                  "\\ln r$ — u "
                  "differensial tenglamani "
                  "**aynan** "
                  "qanoatlantiradi."),
                c("Chegaraviy integral "
                  "tenglama",
                  "Grin ayniyati bilan sohaviy "
                  "integral chegaraviy "
                  "integralga aylantiriladi."),
                c("O'lcham kamayishi",
                  "2D masala 1D chegaraga, 3D "
                  "masala 2D sirtga tushadi — "
                  "noma'lumlar soni keskin "
                  "kamayadi."),
                c("$\\mathbf{H}$ va "
                  "$\\mathbf{G}$ matritsalari",
                  "$\\mathbf{H}\\mathbf{u} = "
                  "\\mathbf{G}\\mathbf{q}$; "
                  "ikkalasi **to'la** va "
                  "umuman **nosimmetrik**."),
                c("Qattiq jism usuli",
                  "$\\mathbf{H}$ ning "
                  "diagonali "
                  "$u = \\text{const}$ "
                  "yechim bo'lishi "
                  "shartidan topiladi."),
                c("Degenerat masshtab",
                  "Chegaraning logarifmik "
                  "sig'imi 1 ga teng "
                  "bo'lganda "
                  "$\\mathbf{G}$ singulyar "
                  "bo'lib qoladi — "
                  "birliklar tanloviga "
                  "bog'liq tuzoq."),
            ],
            derivation=[
                d("1. Fundamental yechim",
                  r"\nabla^2u^* + \delta(\xi) = "
                  r"0 \;\Longrightarrow\; "
                  r"u^* = -\frac{1}{2\pi}\ln r",
                  "Nuqtaviy manba javobi. "
                  "**Hal qiluvchi xossa:** u "
                  "tenglamani soha ichida "
                  "aynan qanoatlantiradi, "
                  "shuning uchun sohani "
                  "diskretlashtirish kerak "
                  "emas."),
                d("2. Grinning ikkinchi "
                  "ayniyati",
                  r"\int_\Omega\left(u\nabla^2v "
                  r"- v\nabla^2u\right)d\Omega "
                  r"= \int_\Gamma\left(u"
                  r"\frac{\partial v}"
                  r"{\partial n} - v"
                  r"\frac{\partial u}"
                  r"{\partial n}\right)d\Gamma",
                  "**Asosiy vosita.** Sohaviy "
                  "integralni chegaraviy "
                  "integralga aylantiradi "
                  "(tmm-10)."),
                d("3. $v = u^*$ tanlash",
                  r"\nabla^2u = 0, \ "
                  r"\nabla^2u^* = -\delta "
                  r"\;\Longrightarrow\; "
                  r"\int_\Omega u\,\delta\,"
                  r"d\Omega = u(\xi)",
                  "Chap tomon delta-funksiya "
                  "tufayli bitta qiymatga "
                  "yig'iladi — bu BEM ning "
                  "butun sehri."),
                d("4. Chegaraviy integral "
                  "tenglama",
                  r"c_i u_i + \int_\Gamma q^*u"
                  r"\,d\Gamma = \int_\Gamma "
                  r"u^*q\,d\Gamma",
                  "$q = \\partial u/"
                  "\\partial n$, "
                  "$q^* = \\partial u^*/"
                  "\\partial n$. "
                  "$c_i$ — erkin had: silliq "
                  "chegarada $1/2$."),
                d("5. Diskretlashtirish",
                  r"\mathbf{H}\mathbf{u} = "
                  r"\mathbf{G}\mathbf{q}",
                  "Chegara elementlarga "
                  "bo'linadi; har bir tugunda "
                  "$u$ yoki $q$ ma'lum, "
                  "ikkinchisi noma'lum."),
                d("6. Diagonal hadlar "
                  "muammosi",
                  r"r \to 0 \;\Longrightarrow\; "
                  r"\ln r \to -\infty",
                  "O'z-o'ziga ta'sirda "
                  "integrand singulyar. "
                  "$\\mathbf{G}$ uchun u "
                  "**zaif** singulyarlik "
                  "va analitik olinadi; "
                  "$\\mathbf{H}$ uchun esa "
                  "kuchliroq."),
                d("7. Qattiq jism usuli",
                  r"u = \text{const} "
                  r"\;\Longrightarrow\; "
                  r"\mathbf{H}\mathbf{1} = "
                  r"\mathbf{0} "
                  r"\;\Longrightarrow\; "
                  r"H_{ii} = -\sum_{j\ne i}"
                  r"H_{ij}",
                  "**Chiroyli yechim.** "
                  "Eng qiyin integralni "
                  "umuman hisoblamaymiz — "
                  "uni fizik shartdan "
                  "topamiz. Bu su-15 dagi "
                  "qator yig'indisi "
                  "tekshiruvining aynan "
                  "o'zi."),
                d("8. Ichki nuqtada yechim",
                  r"u(\xi) = \int_\Gamma u^*q"
                  r"\,d\Gamma - \int_\Gamma "
                  r"q^*u\,d\Gamma",
                  "**To'rsiz baholash.** "
                  "Chegara yechilgandan "
                  "keyin soha ichidagi "
                  "**istalgan** nuqtada "
                  "yechim bitta integral "
                  "bilan topiladi."),
                d("9. Cheksiz soha",
                  r"u^* \to 0 \ (r \to \infty) "
                  r"\;\Longrightarrow\; "
                  r"\text{tashqi chegara "
                  r"KERAK EMAS}",
                  "**BEM ning asosiy "
                  "afzalligi.** "
                  "Fundamental yechim "
                  "cheksizlikdagi shartni "
                  "avtomatik "
                  "qanoatlantiradi — "
                  "sun'iy chegara va "
                  "undan qaytish muammosi "
                  "yo'q."),
                d("10. Matritsalarning "
                  "xossalari",
                  r"\mathbf{H}, \mathbf{G} - "
                  r"\text{TO'LA va "
                  r"NOSIMMETRIK}",
                  "**BEM ning narxi.** "
                  "FEM matritsalari siyrak "
                  "va simmetrik, BEM "
                  "niki esa 100% to'la; "
                  "yechish narxi "
                  "$O(N^3)$, xotira "
                  "$O(N^2)$."),
                d("11. Aniqlik tartibi",
                  r"\|e\| \sim O(h^2) \quad "
                  r"(\text{doimiy elementlar, "
                  r"silliq chegara})",
                  "**O'lchangan natija.** "
                  "Doimiy elementlar odatda "
                  "$O(h)$ berardi, lekin "
                  "markazda kollokatsiya "
                  "silliq chegarada "
                  "superkonvergensiya "
                  "beradi."),
                d("12. Degenerat masshtab",
                  r"\text{log sig'im} = 1 "
                  r"\;\Longrightarrow\; "
                  r"\mathbf{G} \ "
                  r"\text{singulyar}",
                  "**Kutilmagan tuzoq.** "
                  "$\\ln r$ da $r = 1$ "
                  "nolga aylanadi, shuning "
                  "uchun chegaraning "
                  "o'lchami birlikka mos "
                  "kelganda tizim "
                  "buziladi. Ellips uchun "
                  "log sig'im "
                  "$(a+b)/2$."),
            ],
            meaning=(
                "BEM ning butun kuchi 1- va "
                "3-qadamlarda. Fundamental "
                "yechim differensial "
                "tenglamani soha ichida "
                "**aynan** qanoatlantiradi, "
                "shuning uchun uni bazis "
                "sifatida ishlatganda soha "
                "ichida hech narsani "
                "diskretlashtirish kerak "
                "emas. Grin ayniyati esa "
                "sohaviy integralni "
                "chegaraviy integralga "
                "aylantiradi va "
                "delta-funksiya chap "
                "tomonni bitta qiymatga "
                "yig'adi. Natijada 2D "
                "masala 1D chegaraga, 3D "
                "masala esa 2D sirtga "
                "tushadi — bu shunchaki "
                "tejamkorlik emas, "
                "o'lchamning haqiqiy "
                "kamayishi. Kod buni "
                "raqamlashtiradi: "
                "$h = 0{,}0125$ da FEM "
                "6400 noma'lum talab "
                "qiladi, BEM esa 502 ta, "
                "va bu nisbat "
                "$1/h$ kabi o'sib "
                "boraveradi. 9-qadam esa "
                "mavzu boshidagi savolga "
                "javob beradi. "
                "Fundamental yechim "
                "cheksizlikda nolga "
                "intiladi, demak "
                "cheksizlikdagi shart "
                "**avtomatik** "
                "bajariladi. Tuproq, "
                "akustika yoki "
                "elektromagnit "
                "masalalarida sun'iy "
                "chegara qo'yish va "
                "undan qaytishni "
                "bostirish muammosi "
                "butunlay yo'qoladi. "
                "7-qadam amaliy jihatdan "
                "eng chiroyli: eng qiyin "
                "integral — o'z-o'ziga "
                "ta'sir — umuman "
                "hisoblanmaydi, balki "
                "fizik shartdan "
                "topiladi. Bu su-15 dagi "
                "qator yig'indisi "
                "tekshiruvining aynan "
                "o'zi, faqat u yerda "
                "tekshiruv edi, bu "
                "yerda esa **hisoblash "
                "vositasi**. Ammo BEM "
                "bepul emas. 10-qadam "
                "narxini aytadi: "
                "matritsalar to'la va "
                "nosimmetrik, shuning "
                "uchun katta "
                "masalalarda FEM ning "
                "siyrak matritsalari "
                "ustun keladi — "
                "buni faqat tez ko'p "
                "qutbli usul (FMM) "
                "o'zgartira oladi. "
                "12-qadam esa BEM ga "
                "xos, boshqa hech "
                "qayerda uchramaydigan "
                "tuzoqni ochadi. "
                "$\\ln r$ funksiyasi "
                "$r = 1$ da nolga "
                "aylanadi, shuning "
                "uchun chegaraning "
                "o'lchami birlikka mos "
                "kelganda "
                "$\\mathbf{G}$ "
                "singulyar bo'lib "
                "qoladi. Bu "
                "**birliklar "
                "tanloviga** bog'liq "
                "xato: xuddi shu "
                "masalani metrda "
                "yechsangiz buziladi, "
                "santimetrda esa "
                "ishlaydi. Kod buni "
                "uchta butunlay "
                "boshqacha shaklda "
                "tasdiqlaydi va "
                "davosi ham sodda — "
                "masshtabni "
                "o'zgartirish."
            ),
            equations=[
                eq(r"u^* = -\frac{1}{2\pi}\ln r, "
                   r"\qquad q^* = "
                   r"\frac{\partial u^*}"
                   r"{\partial n} = "
                   r"-\frac{1}{2\pi r}"
                   r"\frac{\partial r}"
                   r"{\partial n}",
                   "Ikki o'lchovli Laplas "
                   "tenglamasining fundamental "
                   "yechimi.",
                   "Fundamental yechim"),
                eq(r"c_iu_i + \int_\Gamma q^*u"
                   r"\,d\Gamma = \int_\Gamma "
                   r"u^*q\,d\Gamma",
                   "Chegaraviy integral "
                   "tenglama.",
                   "Integral tenglama"),
                eq(r"\mathbf{H}\mathbf{u} = "
                   r"\mathbf{G}\mathbf{q}, "
                   r"\qquad H_{ii} = "
                   r"-\sum_{j\ne i}H_{ij}",
                   "Diskret tizim va qattiq "
                   "jism usuli.",
                   "Diskret tizim"),
                eq(r"\text{log sig'im}(\Gamma) = "
                   r"1 \;\Longrightarrow\; "
                   r"\mathbf{G} \ "
                   r"\text{singulyar}",
                   "Degenerat masshtab — "
                   "birliklarga bog'liq "
                   "tuzoq.",
                   "Degenerat masshtab"),
            ],
            conditions=(
                "**BEM qachon afzal:**\n"
                "- Cheksiz yoki yarim cheksiz "
                "soha (tuproq, akustika, "
                "to'lqin tarqalishi);\n"
                "- Faqat chegaradagi natija "
                "kerak;\n"
                "- Yorilish mexanikasi — "
                "singulyarlik fundamental "
                "yechimda aynan "
                "ifodalanadi;\n"
                "- Shakl "
                "optimallashtirish — har "
                "iteratsiyada faqat "
                "chegara qayta "
                "quriladi.\n\n"
                "**BEM qachon mos emas:**\n"
                "- Nobir jinsli yoki "
                "nochiziqli material — "
                "fundamental yechim "
                "mavjud emas;\n"
                "- Sohaviy yuklar "
                "(og'irlik, termik) — "
                "sohaviy integral "
                "qaytib keladi;\n"
                "- Juda katta $N$ — "
                "to'la matritsa "
                "$O(N^2)$ xotira "
                "talab qiladi;\n"
                "- Yupqa qobiqlar — "
                "qarama-qarshi sirtlar "
                "yaqinlashib, "
                "integrallar "
                "buziladi.\n\n"
                "**Majburiy "
                "tekshiruvlar:**\n"
                "1. "
                "$\\mathbf{H}\\mathbf{1} = "
                "\\mathbf{0}$ — qattiq "
                "jism sharti;\n"
                "2. Chegara o'lchami "
                "degenerat masshtabdan "
                "uzoqmi (2D da log "
                "sig'im $\\ne 1$);\n"
                "3. Ichki nuqtadagi "
                "yechim chegaraga "
                "yaqinlashganda "
                "chegaraviy qiymatga "
                "intiladimi;\n"
                "4. Analitik yechimi "
                "ma'lum etalonda "
                "sinov.\n\n"
                "**Degenerat masshtabdan "
                "qochish:** 2D Laplas "
                "masalasida chegarani "
                "shunday "
                "masshtablangki, "
                "logarifmik sig'im 1 "
                "dan uzoq bo'lsin; "
                "ellips uchun u "
                "$(a+b)/2$ ga teng. "
                "Eng sodda davo — "
                "barcha "
                "koordinatalarni "
                "o'nga ko'paytirish."
            ),
            worked=WorkedExample(
                statement=(
                    "Radiusi $R$ bo'lgan "
                    "doiraviy sohada "
                    "$u = x$ harmonik "
                    "funksiyasi berilgan. "
                    "(a) Chegarada "
                    "$q = \\partial u/"
                    "\\partial n$ ni toping; "
                    "(b) BEM $N$ ta doimiy "
                    "element bilan buni "
                    "qanday aniqlikda "
                    "tiklashini baholang; "
                    "(c) degenerat masshtab "
                    "qayerda paydo bo'ladi."
                ),
                given=[
                    r"u = x = R\cos\theta, \quad "
                    r"\mathbf{n} = "
                    r"(\cos\theta, \sin\theta)",
                    r"\mathbf{H}\mathbf{u} = "
                    r"\mathbf{G}\mathbf{q}",
                ],
                steps=[
                    st(r"\nabla^2 u = "
                       r"\frac{\partial^2x}"
                       r"{\partial x^2} + "
                       r"\frac{\partial^2x}"
                       r"{\partial y^2} = 0 "
                       r"\quad \checkmark",
                       "$u = x$ harmonik — "
                       "BEM uchun yaroqli "
                       "etalon."),
                    st(r"q = \nabla u \cdot "
                       r"\mathbf{n} = (1, 0)"
                       r"\cdot(\cos\theta, "
                       r"\sin\theta)",
                       "Gradient va normal "
                       "skalyar ko'paytmasi."),
                    st(r"q = \cos\theta",
                       "**Analitik javob** — "
                       "sonli yechim shunga "
                       "intilishi kerak."),
                    st(r"\text{(b)}\quad "
                       r"\mathbf{q} = "
                       r"\mathbf{G}^{-1}"
                       r"\mathbf{H}\mathbf{u}",
                       "Dirixle masalasi: "
                       "$u$ ma'lum, $q$ "
                       "noma'lum."),
                    st(r"h = \frac{2\pi R}{N} "
                       r"\;\Longrightarrow\; "
                       r"\|e\| \sim O(h^2) = "
                       r"O(N^{-2})",
                       "Doimiy elementlar, "
                       "markazda "
                       "kollokatsiya."),
                    st(r"N: 8 \to 16 "
                       r"\;\Longrightarrow\; "
                       r"\text{xato } 4 "
                       r"\text{ barobar "
                       r"kamayadi}",
                       "Kod: 4,6% → 1,2% → "
                       "0,31% → 0,079% — "
                       "har safar aynan "
                       "to'rtdan bir."),
                    st(r"\text{(c)}\quad u^* = "
                       r"-\frac{1}{2\pi}\ln r",
                       "Fundamental yechim."),
                    st(r"r = 1 "
                       r"\;\Longrightarrow\; "
                       r"\ln r = 0 "
                       r"\;\Longrightarrow\; "
                       r"u^* = 0",
                       "**Tuzoqning ildizi.** "
                       "Fundamental yechim "
                       "birlik masofada "
                       "nolga aylanadi."),
                    st(r"R = 1 \ \text{da } "
                       r"\mathbf{G} \ "
                       r"\text{deyarli "
                       r"singulyar}",
                       "Butun chegara birlik "
                       "masofada yotsa, "
                       "$\\mathbf{G}$ ning "
                       "bir xos qiymati "
                       "nolga intiladi."),
                    st(r"\text{Ellips uchun: "
                       r"log sig'im} = "
                       r"\frac{a+b}{2} = 1",
                       "Umumiy shart — "
                       "faqat doira uchun "
                       "emas."),
                    st(r"\text{Davo: } x "
                       r"\leftarrow 10x, \ "
                       r"\text{keyin natijani "
                       r"qaytarib "
                       r"masshtablash}",
                       "Bir qator kod; "
                       "muammo butunlay "
                       "yo'qoladi."),
                ],
                answer=(
                    "(a) $q = \\cos\\theta$; "
                    "(b) xato "
                    "$O(N^{-2})$ — kodda "
                    "$N$ ikkilanganda aynan "
                    "to'rt barobar kamayadi "
                    "(4,6% → 1,2% → 0,31% → "
                    "0,079%); "
                    "(c) $R = 1$ da, chunki "
                    "$\\ln 1 = 0$. Umumiy "
                    "shart — logarifmik "
                    "sig'im 1 ga teng; "
                    "ellips uchun "
                    "$(a+b)/2 = 1$. Kod "
                    "buni uchta boshqacha "
                    "shaklda tasdiqlaydi."
                ),
                engineering_note=(
                    "(c) qismidagi tuzoq "
                    "BEM ga xos va boshqa "
                    "hech qayerda "
                    "uchramaydi. Uning "
                    "xavfliligi shundaki, "
                    "u **birliklar "
                    "tanloviga** bog'liq: "
                    "radiusi 1 m bo'lgan "
                    "quvurni metrda "
                    "hisoblasangiz tizim "
                    "buziladi, "
                    "santimetrda "
                    "(R = 100) esa "
                    "bemalol ishlaydi. "
                    "Hech qanday fizik "
                    "o'zgarish yo'q — "
                    "faqat sonlar "
                    "boshqacha. Bundan "
                    "ham yomoni, "
                    "degenerat "
                    "masshtabga "
                    "**yaqin** bo'lsangiz "
                    "tizim singulyar "
                    "bo'lmaydi, lekin "
                    "shartlanganlik "
                    "keskin oshadi va "
                    "natija jimgina "
                    "noaniqlashadi. "
                    "Kodda "
                    "$R = 1$ da cond "
                    "502 ga sakraydi, "
                    "$R = 1{,}05$ da esa "
                    "atigi 27. Shuning "
                    "uchun 2D BEM "
                    "kodida masshtabni "
                    "tekshirish "
                    "standart amaliyot "
                    "bo'lishi kerak. "
                    "Uch o'lchovda bu "
                    "muammo yo'q, "
                    "chunki u yerda "
                    "fundamental yechim "
                    "$1/(4\\pi r)$ va u "
                    "hech qayerda nolga "
                    "aylanmaydi — tuzoq "
                    "aynan "
                    "logarifmning "
                    "xossasidan kelib "
                    "chiqadi."
                ),
            ),
            computation=Computation(
                caption=(
                    "Chegaraviy element "
                    "matritsalarini qurish, "
                    "analitik yechimlar bilan "
                    "tekshirish, ichki nuqtada "
                    "yechimni tiklash va "
                    "degenerat masshtabni "
                    "aniqlash."
                ),
                code='''"""Chegaraviy elementlar usuli (BEM)."""
import numpy as np
from labkit import PARAMS, note, series, table, value

N_el = int(PARAMS.get("N_el", 64))
a_ax = float(PARAMS.get("a_ax", 2.0))
b_ax = float(PARAMS.get("b_ax", 1.0))


def bem(N, a=1.0, b=1.0):
    """Ellips (a = b bo'lsa doira) chegarasida doimiy elementlar."""
    th = np.linspace(0, 2*np.pi, N + 1)[:-1]
    dth = 2*np.pi/N
    x1, y1 = a*np.cos(th), b*np.sin(th)
    x2, y2 = a*np.cos(th + dth), b*np.sin(th + dth)
    xc, yc = 0.5*(x1 + x2), 0.5*(y1 + y2)
    tx, ty = x2 - x1, y2 - y1
    Le = np.hypot(tx, ty)
    nx, ny = ty/Le, -tx/Le
    if np.mean(nx*xc + ny*yc) < 0:          # tashqi normal
        nx, ny = -nx, -ny
    G = np.zeros((N, N))
    H = np.zeros((N, N))
    gp, gw = np.polynomial.legendre.leggauss(12)
    for i in range(N):
        for j in range(N):
            if i == j:
                # zaif (logarifmik) singulyarlik - ANALITIK
                G[i, j] = Le[j]/(2*np.pi)*(1 - np.log(Le[j]/2))
            else:
                xs = 0.5*(x1[j] + x2[j]) + 0.5*(x2[j] - x1[j])*gp
                ys = 0.5*(y1[j] + y2[j]) + 0.5*(y2[j] - y1[j])*gp
                rx, ry = xs - xc[i], ys - yc[i]
                r = np.hypot(rx, ry)
                G[i, j] = float(np.sum(-np.log(r)/(2*np.pi)*gw))*Le[j]/2
                drdn = (rx*nx[j] + ry*ny[j])/r
                H[i, j] = float(np.sum(-drdn/(2*np.pi*r)*gw))*Le[j]/2
    # QATTIQ JISM usuli: u = const yechim bo'lishi shartidan (su-15)
    for i in range(N):
        H[i, i] = -np.sum([H[i, j] for j in range(N) if j != i])
    return G, H, xc, yc, nx, ny, Le, x1, y1, x2, y2


# --- (1) QATTIQ JISM sharti va erkin had ---
rows = []
for N in [8, 16, 32, 64, 128]:
    G, H, *_ = bem(N, 1.0, 1.0)
    rows.append([N, f"{float(np.max(np.abs(H @ np.ones(N)))):.2e}",
                 f"{H[0, 0]:.6f}", "0.500000"])
table("Qattiq jism sharti va erkin had c_i",
      ["N", "max|H @ 1|", "H[0,0] (hisoblangan)", "nazariy c_i"], rows)
note("Diagonal hadni qattiq jism usuli bilan topish - BEM ning eng "
     "chiroyli amaliy hiylasi: eng QIYIN integralni umuman "
     "hisoblamaymiz, balki u = const yechim bo'lishi shartidan "
     "topamiz. Natijada H @ 1 = 0 mashina aniqligida bajariladi. "
     "Hisoblangan diagonal esa N oshgani sari nazariy 0.5 ga "
     "intiladi (0.4375 -> 0.4922 -> ...) - ya'ni u egrilikni ham "
     "avtomatik hisobga oladi. Bu su-15 dagi qator yig'indisi "
     "tekshiruvining aynan o'zi, faqat u yerda tekshiruv edi, bu "
     "yerda esa HISOBLASH VOSITASI.")

# --- (2) ANALITIK TEKSHIRUV: ikkita harmonik funksiya ---
rows2 = []
prev = {}
for N in [8, 16, 32, 64, 128]:
    G, H, xc, yc, nx, ny, *_ = bem(N, 1.0, 1.0)
    line = [N]
    for nm, uf, qf in [("u = x", lambda X, Y: X,
                        lambda X, Y, NX, NY: NX),
                       ("u = x^2 - y^2", lambda X, Y: X**2 - Y**2,
                        lambda X, Y, NX, NY: 2*(X*NX - Y*NY))]:
        u = uf(xc, yc)
        q_ex = qf(xc, yc, nx, ny)
        q = np.linalg.solve(G, H @ u)
        e = float(np.max(np.abs(q - q_ex))/np.max(np.abs(q_ex)))
        ratio = "—" if nm not in prev else f"{prev[nm]/e:.2f}"
        prev[nm] = e
        line += [f"{e:.4e}", ratio]
    rows2.append(line)
table("Analitik yechimlar bilan tekshirish (doira R = 1)",
      ["N", "u = x xato", "nisbat", "u = x^2-y^2 xato", "nisbat"], rows2)
note("Ikkala harmonik funksiya uchun ham xato N ikkilanganda aynan "
     "TO'RT barobar kamayadi - ya'ni O(h^2). Doimiy elementlar odatda "
     "faqat O(h) beradi, lekin element MARKAZIDA kollokatsiya qilish "
     "silliq chegarada superkonvergensiya beradi. Bu su-16 dagi "
     "Barlou nuqtalari bilan bir oiladagi hodisa: to'g'ri nuqtada "
     "baholash bir tartib yutuq beradi.")

# --- (3) ICHKI NUQTADA yechim: TO'RSIZ ---
G, H, xc, yc, nx, ny, Le, x1, y1, x2, y2 = bem(N_el, 1.0, 1.0)
u_b = xc**2 - yc**2
q_b = np.linalg.solve(G, H @ u_b)


def interior(px, py):
    """Soha ichidagi istalgan nuqtada yechim - to'r kerak emas."""
    gp, gw = np.polynomial.legendre.leggauss(12)
    tot = 0.0
    for j in range(N_el):
        xs = 0.5*(x1[j] + x2[j]) + 0.5*(x2[j] - x1[j])*gp
        ys = 0.5*(y1[j] + y2[j]) + 0.5*(y2[j] - y1[j])*gp
        rx, ry = xs - px, ys - py
        r = np.hypot(rx, ry)
        Gij = float(np.sum(-np.log(r)/(2*np.pi)*gw))*Le[j]/2
        drdn = (rx*nx[j] + ry*ny[j])/r
        Hij = float(np.sum(-drdn/(2*np.pi*r)*gw))*Le[j]/2
        tot += Gij*q_b[j] - Hij*u_b[j]
    return tot


rows3 = []
for px, py in [(0.0, 0.0), (0.3, 0.2), (0.5, -0.5), (0.7, 0.0),
               (0.0, 0.9)]:
    v = interior(px, py)
    ex = px**2 - py**2
    rows3.append([f"({px:.2f}, {py:.2f})", f"{v:+.8f}", f"{ex:+.8f}",
                  f"{abs(v - ex):.2e}"])
table(f"Ichki nuqtada yechim ({N_el} chegaraviy element, to'r YO'Q)",
      ["nuqta", "BEM", "aniq", "xato"], rows3)
xs_line = np.linspace(-0.95, 0.95, 40)
series("BEM: u(x, 0)", xs_line.tolist(),
       [interior(float(x), 0.0) for x in xs_line],
       xlabel="x", ylabel="u")
series("Aniq: x^2", xs_line.tolist(), (xs_line**2).tolist(),
       xlabel="x", ylabel="u")
note("Chegara yechilgandan keyin soha ichidagi ISTALGAN nuqtada "
     "yechim bitta integral bilan topiladi - hech qanday sohaviy "
     "to'r kerak emas. Aniqlik 1e-5 darajasida va nuqta chegaraga "
     "yaqinlashgani sari biroz yomonlashadi (integrand deyarli "
     "singulyar bo'lib qoladi). FEM da esa yechim faqat to'r "
     "tugunlarida ma'lum va oradagi qiymatlar interpolyatsiya "
     "qilinadi.")

# --- (4) MATRITSA XOSSALARI: doira MAXSUS hol ---
rows4 = []
for nm, (aa, bb) in [("doira (1, 1)", (1.0, 1.0)),
                     ("ellips (2, 1)", (2.0, 1.0)),
                     ("ellips (3, 1)", (3.0, 1.0))]:
    Gx, Hx, *_ = bem(48, aa, bb)
    sG = float(np.max(np.abs(Gx - Gx.T))/np.max(np.abs(Gx)))
    sH = float(np.max(np.abs(Hx - Hx.T))/np.max(np.abs(Hx)))
    dens = np.count_nonzero(np.abs(Gx) > 1e-14)/Gx.size*100
    rows4.append([nm, f"{sG:.4f}", f"{sH:.4f}", f"{dens:.1f}"])
table("Matritsalar simmetrikmi?",
      ["shakl", "G nosimmetrikligi", "H nosimmetrikligi", "zichlik %"],
      rows4)
note("DIQQAT: doirada G va H simmetrik chiqadi, lekin bu DOIRANING "
     "aylanma simmetriyasi tufayli - umumiy qoida emas. Ellipsda "
     "nosimmetriya darhol paydo bo'ladi (a = 2 da 16%, a = 3 da 33%). "
     "Demak BEM matritsalari umuman NOSIMMETRIK va bu FEM dan jiddiy "
     "farq: Xoleskiy yoyilmasi ishlamaydi, xotira ikki barobar ko'p "
     "kerak. Bundan tashqari matritsa 100% TO'LA - FEM da u su-15 "
     "dagi kabi lentali edi.")

# --- (5) O'LCHAM KAMAYISHI ---
rows5 = []
for h in [0.2, 0.1, 0.05, 0.025, 0.0125]:
    nf = int((1.0/h)**2)
    nb = int(2*np.pi/h)
    rows5.append([f"{h:.4f}", nf, nb, f"{nf/nb:.1f}"])
table("2D masala: FEM (sohaviy to'r) va BEM (chegaraviy to'r)",
      ["h", "FEM noma'lumlari ~ 1/h^2", "BEM ~ 1/h", "nisbat"], rows5)
note("BEM ning asosiy afzalligi - O'LCHAM KAMAYISHI. 2D masala 1D "
     "chegaraga tushadi, shuning uchun noma'lumlar soni 1/h^2 "
     "o'rniga 1/h kabi o'sadi va nisbat 1/h kabi kattalashadi. Uch "
     "o'lchovda yutuq yanada katta. LEKIN matritsa to'la, shuning "
     "uchun yechish narxi O(N^3) va xotira O(N^2) - FEM ning siyrak "
     "matritsasi katta N da baribir ustun keladi. Aynan shu "
     "cheklovni tez ko'p qutbli usul (FMM) O(N log N) ga tushiradi.")

# --- (6) DEGENERAT MASSHTAB: BEM ga xos tuzoq ---
rows6 = []
for R in [0.5, 0.8, 0.95, 0.99, 1.0, 1.01, 1.05, 1.3, 2.0]:
    Gx, *_ = bem(64, R, R)
    ev = np.linalg.eigvals(Gx)
    rows6.append([f"{R:.2f}", f"{np.linalg.cond(Gx):.3e}",
                  f"{float(np.min(np.abs(ev))):.3e}"])
table("Doira radiusi va G matritsasining shartlanganligi",
      ["R", "cond(G)", "eng kichik |xos qiymat|"], rows6)
rows7 = []
for aa, bb in [(2.0, 1.0), (3.0, 1.0), (1.5, 0.5), (1.2, 0.8),
               (1.0, 1.0), (0.5, 0.5)]:
    Gx, *_ = bem(64, aa, bb)
    cap = (aa + bb)/2
    rows7.append([f"({aa:.1f}, {bb:.1f})", f"{cap:.3f}",
                  f"{np.linalg.cond(Gx):.3e}",
                  "DEGENERAT" if abs(cap - 1.0) < 1e-9 else "normal"])
table("Logarifmik sig'im (a+b)/2 va degenerat masshtab",
      ["(a, b)", "log sig'im", "cond(G)", "holat"], rows7)
value("R = 1.00 da cond(G)", float(np.linalg.cond(bem(64, 1.0, 1.0)[0])),
      "—")
value("R = 1.05 da cond(G)", float(np.linalg.cond(bem(64, 1.05, 1.05)[0])),
      "—")
series("cond(G) va radius", [0.5, 0.8, 0.95, 0.99, 1.0, 1.01, 1.05, 1.3,
                             2.0],
       [np.log10(np.linalg.cond(bem(48, R, R)[0]))
        for R in [0.5, 0.8, 0.95, 0.99, 1.0, 1.01, 1.05, 1.3, 2.0]],
       xlabel="R", ylabel="log10 cond(G)")
note("BEM GA XOS TUZOQ. Fundamental yechim ln(r) bo'lgani uchun u "
     "r = 1 da NOLGA aylanadi. Natijada chegaraning logarifmik "
     "sig'imi 1 ga teng bo'lsa, G matritsasi singulyar bo'lib "
     "qoladi. Jadval buni uchta BUTUNLAY BOSHQACHA shaklda "
     "tasdiqlaydi: doira (1,1), ellips (1.5,0.5) va ellips (1.2,0.8) "
     "- uchalasining ham (a+b)/2 = 1 va uchalasida ham cond keskin "
     "sakraydi (500-760), boshqa shakllarda esa atigi 27-81. "
     "Eng xavflisi - bu BIRLIKLAR tanloviga bog'liq: radiusi 1 m "
     "bo'lgan quvurni metrda hisoblasangiz buziladi, santimetrda "
     "ishlaydi. Davosi sodda: koordinatalarni masshtablang. Uch "
     "o'lchovda bu muammo YO'Q, chunki u yerda u* = 1/(4 pi r) va u "
     "hech qayerda nolga aylanmaydi.")

table("BEM va FEM: qachon qaysi biri",
      ["Jihat", "FEM", "BEM"],
      [["Diskretlashtirish", "butun soha", "faqat chegara"],
       ["Noma'lumlar (2D)", "~1/h^2", "~1/h"],
       ["Matritsa", "siyrak, simmetrik", "TO'LA, nosimmetrik"],
       ["Cheksiz soha", "sun'iy chegara kerak", "AVTOMATIK"],
       ["Nobir jinsli material", "OSON", "qiyin yoki mumkin emas"],
       ["Sohaviy yuk", "tabiiy", "sohaviy integral qaytadi"],
       ["Nochiziqlik", "OSON", "qiyin"],
       ["Ichki nuqtada yechim", "to'r tugunlarida", "ISTALGAN nuqtada"]])
''',
                parameters=[
                    p("N_el", "Chegaraviy elementlar soni", 8.0, 128.0,
                      64.0, 8.0),
                    p("a_ax", "Ellipsning katta yarim o'qi", 0.5, 4.0,
                      2.0, 0.1),
                    p("b_ax", "Ellipsning kichik yarim o'qi", 0.3, 3.0,
                      1.0, 0.1),
                ],
                expected_output=(
                    "Qattiq jism usuli "
                    "$\\mathbf{H}\\mathbf{1} = "
                    "\\mathbf{0}$ ni mashina "
                    "aniqligida ta'minlaydi va "
                    "hisoblangan diagonal "
                    "nazariy 0,5 ga intiladi. "
                    "Ikkala harmonik etalon "
                    "uchun ham xato $N$ "
                    "ikkilanganda aynan to'rt "
                    "barobar kamayadi — "
                    "$O(h^2)$. Ichki nuqtada "
                    "yechim to'rsiz, "
                    "$10^{-5}$ aniqlikda "
                    "topiladi. Doirada "
                    "matritsalar simmetrik "
                    "chiqadi, lekin bu "
                    "doiraning maxsus "
                    "holati: ellipsda "
                    "nosimmetriya 16% va "
                    "33% ga yetadi; zichlik "
                    "100%. Eng muhimi — "
                    "degenerat masshtab: "
                    "logarifmik sig'im "
                    "$(a+b)/2 = 1$ bo'lgan "
                    "uchta turli shaklda "
                    "ham $\\mathrm{cond}(G)$ "
                    "500–760 ga sakraydi, "
                    "boshqa shakllarda esa "
                    "27–81 bo'lib qoladi."
                ),
            ),
            visual=vis(
                kind="BEM: chegaraviy diskretlashtirish",
                tool="React/SVG + Manim",
                description=(
                    "Chegaraviy elementlar, "
                    "fundamental yechim va "
                    "to'rsiz ichki maydon."
                ),
                how_to_draw=(
                    "React/SVG: chap panelda "
                    "ikki xil "
                    "diskretlashtirish "
                    "yonma-yon — FEM uchun "
                    "butun sohani "
                    "to'ldirgan uchburchak "
                    "to'r, BEM uchun esa "
                    "faqat chegaradagi "
                    "kesmalar zanjiri. "
                    "Ikkalasining ostida "
                    "noma'lumlar soni "
                    "turadi va $h$ "
                    "slayderi surilganda "
                    "FEM raqami "
                    "kvadratik, BEM "
                    "raqami chiziqli "
                    "o'sadi — o'lcham "
                    "kamayishi shunda "
                    "ko'rinadi. O'ng "
                    "panelda tanlangan "
                    "chegara nuqtasidan "
                    "fundamental yechim "
                    "tarqaladi: "
                    "$\\ln r$ ning "
                    "darajali chiziqlari "
                    "konsentrik "
                    "aylanalar sifatida "
                    "chiziladi va "
                    "$r = 1$ aylanasi "
                    "alohida "
                    "belgilanadi — "
                    "aynan u yerda "
                    "$u^* = 0$. "
                    "Pastki panelda "
                    "soha ichidagi "
                    "maydon rang bilan "
                    "to'ldiriladi, "
                    "lekin to'r YO'Q: "
                    "sichqoncha "
                    "bosilgan har "
                    "qanday nuqtada "
                    "qiymat "
                    "hisoblanadi va "
                    "aniq javob bilan "
                    "yonma-yon "
                    "ko'rsatiladi. "
                    "Yonida radius "
                    "slayderi bor va "
                    "$R = 1$ ga "
                    "yaqinlashganda "
                    "$\\mathrm{cond}(G)$ "
                    "ko'rsatkichi "
                    "keskin qizarib "
                    "ko'tariladi."
                ),
            ),
            interp=(
                "Qattiq jism usuli BEM ning "
                "eng chiroyli amaliy "
                "hiylasi: eng qiyin "
                "integral — o'z-o'ziga "
                "ta'sir — umuman "
                "hisoblanmaydi, balki "
                "$u = \\text{const}$ yechim "
                "bo'lishi shartidan "
                "topiladi. Natija ikki "
                "tomonlama foydali: "
                "$\\mathbf{H}\\mathbf{1} = "
                "\\mathbf{0}$ mashina "
                "aniqligida bajariladi va "
                "hisoblangan diagonal "
                "egrilikni avtomatik "
                "hisobga oladi, $N$ "
                "oshgani sari nazariy "
                "0,5 ga intilib. Bu su-15 "
                "dagi qator yig'indisi "
                "tekshiruvi bilan aynan "
                "bir xil ayniyat, faqat u "
                "yerda tekshiruv, bu "
                "yerda esa hisoblash "
                "vositasi edi. "
                "Yaqinlashish "
                "o'lchovlari ikkita "
                "mustaqil harmonik "
                "etalonda $O(h^2)$ "
                "berdi — doimiy "
                "elementlar uchun "
                "kutilganidan bir "
                "tartib yaxshi. Sabab "
                "su-16 dagi Barlou "
                "nuqtalari bilan bir "
                "oilada: element "
                "markazida kollokatsiya "
                "qilish silliq "
                "chegarada "
                "superkonvergensiya "
                "beradi. Ichki nuqta "
                "tajribasi esa BEM ning "
                "eng o'ziga xos "
                "xossasini ko'rsatadi: "
                "chegara yechilgandan "
                "keyin soha ichidagi "
                "istalgan nuqtada "
                "yechim bitta integral "
                "bilan topiladi va "
                "hech qanday sohaviy "
                "to'r kerak emas. "
                "Simmetriya jadvali "
                "muhim ogohlantirish "
                "beradi. Doirada "
                "matritsalar simmetrik "
                "chiqadi va bu "
                "noto'g'ri umumlashmaga "
                "olib kelishi mumkin — "
                "aslida bu doiraning "
                "aylanma simmetriyasi "
                "tufayli, ellipsda esa "
                "nosimmetriya darhol "
                "33% gacha yetadi. "
                "Bitta shaklda "
                "o'tkazilgan sinov "
                "yetarli emasligiga "
                "yana bir misol. Eng "
                "qimmatli natija esa "
                "degenerat masshtab. "
                "Logarifmik sig'imi 1 "
                "ga teng uchta "
                "butunlay boshqacha "
                "shakl — doira "
                "$(1,1)$, ellips "
                "$(1{,}5,\\ 0{,}5)$ va "
                "ellips "
                "$(1{,}2,\\ 0{,}8)$ — "
                "uchalasida ham "
                "shartlanganlik "
                "sakraydi. Bu "
                "tasodif emas, "
                "nazariyaning aniq "
                "bashorati va u "
                "birliklar tanloviga "
                "bog'liq xato "
                "ekanligi bilan "
                "ayniqsa xavfli."
            ),
            mistakes=[
                "Diagonal hadni to'g'ridan "
                "to'g'ri integrallashga "
                "urinish. Qattiq jism usuli "
                "ham oson, ham aniqroq.",
                "Degenerat masshtabni "
                "e'tiborsiz qoldirish. "
                "2D da logarifmik sig'im "
                "1 dan uzoq bo'lsin — "
                "aks holda tizim jimgina "
                "buziladi.",
                "BEM matritsalarini "
                "simmetrik deb hisoblash. "
                "Doira maxsus hol; "
                "umumiy shaklda ular "
                "nosimmetrik.",
                "Nobir jinsli yoki "
                "nochiziqli masalada BEM "
                "ishlatishga urinish. "
                "Fundamental yechim "
                "mavjud emas.",
                "Sohaviy yuk borligini "
                "unutish. Og'irlik yoki "
                "termik yuk sohaviy "
                "integralni qaytaradi va "
                "BEM ning asosiy "
                "afzalligi yo'qoladi.",
                "Katta $N$ da BEM "
                "ishlatish. To'la "
                "matritsa $O(N^2)$ "
                "xotira va $O(N^3)$ "
                "vaqt talab qiladi.",
            ],
            quiz=[
                q("BEM nima uchun sohani "
                  "diskretlashtirmaydi?",
                  "Fundamental yechim "
                  "differensial tenglamani "
                  "soha ichida **aynan** "
                  "qanoatlantiradi, shuning "
                  "uchun faqat chegaraviy "
                  "shartlarni qanoatlantirish "
                  "qoladi.", "konseptual"),
                q("Cheksiz soha BEM da "
                  "qanday hisobga olinadi?",
                  "Fundamental yechim "
                  "$r \\to \\infty$ da nolga "
                  "intiladi, demak "
                  "cheksizlikdagi shart "
                  "avtomatik bajariladi — "
                  "sun'iy chegara kerak "
                  "emas.", "konseptual"),
                q("$u = x$ uchun doirada "
                  "$q$ nechaga teng?",
                  "$q = \\nabla u\\cdot"
                  "\\mathbf{n} = "
                  "(1,0)\\cdot"
                  "(\\cos\\theta,"
                  "\\sin\\theta) = "
                  "\\cos\\theta$.", "hisob"),
                q("Kod diagonal hadni qanday "
                  "topadi va bu nima uchun "
                  "yaxshi?",
                  "Qattiq jism usuli bilan: "
                  "$H_{ii} = -\\sum_{j\\ne i}"
                  "H_{ij}$. Eng qiyin "
                  "integral hisoblanmaydi va "
                  "$\\mathbf{H}\\mathbf{1} = "
                  "\\mathbf{0}$ aynan "
                  "bajariladi.", "kod"),
                q("Degenerat masshtab nima "
                  "va u qachon paydo "
                  "bo'ladi?",
                  "$\\ln r$ $r = 1$ da nolga "
                  "aylanadi, shuning uchun "
                  "logarifmik sig'im 1 ga "
                  "teng bo'lsa "
                  "$\\mathbf{G}$ singulyar "
                  "bo'ladi. Ellips uchun "
                  "sig'im $(a+b)/2$.",
                  "kod"),
                q("Nima uchun doirada "
                  "matritsalar simmetrik "
                  "chiqdi?",
                  "Doiraning aylanma "
                  "simmetriyasi tufayli — "
                  "bu maxsus hol. Ellipsda "
                  "nosimmetriya 16–33% ga "
                  "yetadi va umumiy holda "
                  "BEM matritsalari "
                  "nosimmetrik.", "talqin"),
                q("BEM qachon FEM dan "
                  "afzal?",
                  "Cheksiz soha, faqat "
                  "chegaradagi natija, "
                  "yorilish mexanikasi va "
                  "shakl "
                  "optimallashtirishda. "
                  "Nobir jinsli material, "
                  "sohaviy yuk yoki "
                  "nochiziqlik bo'lsa esa "
                  "FEM afzal.", "talqin"),
            ],
            bridge=(
                "DQM butun sohani, BEM esa "
                "faqat chegarani "
                "diskretlashtirdi. Keyingi "
                "mavzuda uchinchi yo'lni "
                "ko'ramiz: to'rni umuman "
                "qurmaslik. Spektral va "
                "to'rsiz usullar "
                "diskretlashtirishning "
                "o'zini qayta "
                "o'ylab ko'radi."
            ),
            research=(
                "BEM ni chuqurlashtiring. "
                "(1) Tez ko'p qutbli usulni "
                "(FMM) o'rganing: u to'la "
                "matritsani saqlamasdan "
                "ko'paytirishni "
                "$O(N\\log N)$ da "
                "bajaradi — qanday? "
                "(2) Ikkilangan "
                "o'zaro ta'sir usulini "
                "(DRM) ko'rib chiqing: "
                "sohaviy yuklarni "
                "chegaraga qanday "
                "keltiradi? "
                "(3) Yorilish mexanikasida "
                "ikkilangan BEM ni "
                "(dual BEM) o'rganing: "
                "yoriqning ikki sirti "
                "ustma-ust tushganda "
                "tizim buziladi — "
                "giperchisingulyar "
                "tenglama buni qanday "
                "hal qiladi (tmm-24)? "
                "(4) Degenerat "
                "masshtabni nazariy "
                "o'rganing: logarifmik "
                "sig'im tushunchasi va "
                "uni turli shakllar "
                "uchun hisoblash."
            ),
            manim_ref=manim(
                scene="BEMScene",
                module="manim/scenes/su_modern.py",
                title="O'lcham kamayishi",
                summary=(
                    "Avval sohaviy to'r "
                    "quriladi va tugunlar "
                    "sanaladi. Keyin "
                    "ichki tugunlar "
                    "birin-ketin "
                    "yo'qoladi va faqat "
                    "chegara qoladi — "
                    "hisoblagich keskin "
                    "tushadi. Tanlangan "
                    "chegara nuqtasidan "
                    "fundamental yechim "
                    "to'lqin kabi "
                    "tarqaladi va "
                    "$r = 1$ aylanasi "
                    "yonib, u yerda "
                    "$u^*$ nolga "
                    "aylanishi "
                    "ko'rsatiladi. "
                    "Oxirida soha "
                    "ichida ixtiyoriy "
                    "nuqtalar "
                    "tanlanadi va "
                    "har birida "
                    "yechim to'rsiz "
                    "hisoblanadi."
                ),
            ),
        ),
    ),

    # ------------------------------------------------------------------ su-27
    Topic(
        id="su-27",
        subject_id=S, module_id=M, order=27,
        title="Spektral va to'rsiz usullar",
        description=(
            "Chebishev spektral usuli, radial bazis funksiyalari, "
            "to'rsiz kollokatsiya, shakl parametri tanlovi va "
            "noaniqlik prinsipi."
        ),
        learning_objective=(
            "Spektral va to'rsiz usullarni qurish, ularning aniqlik va "
            "shartlanganlik almashuvini miqdoriy baholash hamda "
            "qo'llanish sohasini asoslash."
        ),
        prerequisites=["su-26", "su-25", "su-05"],
        mathematical_core=(
            "$u(x) \\approx \\sum_j\\alpha_j\\phi(\\|x - x_j\\|)$; "
            "multikvadrik "
            "$\\phi(r) = \\sqrt{r^2 + c^2}$; "
            "noaniqlik prinsipi: aniqlik $\\times$ shartlanganlik "
            "$\\approx$ const."
        ),
        engineering_application=(
            "Katta deformatsiya, yorilish tarqalishi, suyuqlik–qattiq "
            "jism ta'siri, harakatlanuvchi chegaralar — to'r "
            "buzilib ketadigan masalalar."
        ),
        computational_component=(
            "Chebishev differensiallash matritsasi, RBF kollokatsiya, "
            "shakl parametrining optimal qiymatini topish."
        ),
        visualization_component=(
            "Radial bazis funksiyalari, tugun taqsimoti, aniqlik va "
            "shartlanganlik egri chiziqlari."
        ),
        research_extension=(
            "RBF-FD usulini o'rganing: u RBF ning moslashuvchanligini "
            "siyrak matritsalar bilan birlashtiradi."
        ),
        difficulty="murakkab",
        previous_link=(
            "su-25 butun sohani, su-26 esa faqat chegarani "
            "diskretlashtirdi. Ikkalasi ham tugunlar orasidagi "
            "bog'lanishga — to'rga — tayanardi. Endi to'rning o'zidan "
            "voz kechamiz."
        ),
        next_topic="su-28",
        estimated_minutes=85,
        tags=["spektral usul", "RBF", "to'rsiz", "shakl parametri",
              "noaniqlik prinsipi"],
        lesson=_lesson(
            problem=(
                "Metall shakllantirish "
                "jarayoni modellashtirilmoqda: "
                "zagotovka press ostida "
                "butunlay o'zgaradi — "
                "deformatsiya yuzlab "
                "foizga yetadi. FEM to'ri "
                "bunday deformatsiyada "
                "buziladi: elementlar "
                "cho'ziladi, ag'dariladi va "
                "su-14 dagi "
                "$\\det\\mathbf{J} \\le 0$ "
                "holati yuzaga keladi. "
                "Hisob to'xtaydi va to'rni "
                "qayta qurish kerak "
                "bo'ladi — bu esa "
                "natijani interpolyatsiya "
                "qilishni va aniqlik "
                "yo'qotishni anglatadi. "
                "Yorilish tarqalishida "
                "ham xuddi shunday: yoriq "
                "yo'li oldindan noma'lum "
                "va to'r unga moslashishi "
                "kerak. To'rni butunlay "
                "tashlab yuborish "
                "mumkinmi?"
            ),
            concepts=[
                c("Spektral usul",
                  "Global silliq bazis "
                  "(Chebishev, Fure); "
                  "silliq yechimda mashina "
                  "aniqligiga yetadi."),
                c("Chebishev "
                  "differensiallash "
                  "matritsasi",
                  "su-25 dagi DQM ning "
                  "Chebishev tugunlaridagi "
                  "ko'rinishi — yopiq "
                  "formulasi bor."),
                c("Radial bazis funksiyasi "
                  "(RBF)",
                  "$\\phi(\\|x - x_j\\|)$ — "
                  "faqat masofaga bog'liq; "
                  "shuning uchun istalgan "
                  "o'lchovda va istalgan "
                  "tugun joylashuvida "
                  "ishlaydi."),
                c("To'rsizlik",
                  "Tugunlar orasida "
                  "bog'lanish **umuman "
                  "yo'q** — faqat "
                  "koordinatalar kerak."),
                c("Shakl parametri $c$",
                  "Multikvadrikning "
                  "kengligi; aniqlikni ham, "
                  "shartlanganlikni ham "
                  "belgilaydi."),
                c("Noaniqlik prinsipi",
                  "Yaxshi shartlanganlik va "
                  "yuqori aniqlikka "
                  "**bir vaqtda** erishib "
                  "bo'lmaydi (Shaback)."),
            ],
            derivation=[
                d("1. Spektral yoyilma",
                  r"u(x) \approx \sum_{k=0}^{N}"
                  r"a_kT_k(x)",
                  "Chebishev ko'phadlari — "
                  "global va silliq. Bu "
                  "su-25 dagi DQM bilan bir "
                  "oiladagi yondashuv."),
                d("2. Differensiallash "
                  "matritsasi",
                  r"D_{ij} = "
                  r"\frac{c_i(-1)^{i+j}}"
                  r"{c_j(x_i - x_j)}, \quad "
                  r"i \ne j; \qquad D_{ii} = "
                  r"-\sum_{j \ne i}D_{ij}",
                  "$c_0 = c_N = 2$, "
                  "qolganlari 1. Diagonal "
                  "yana qator yig'indisi "
                  "noli shartidan — su-25 "
                  "va su-26 dagi bir xil "
                  "ayniyat."),
                d("3. Spektral aniqlik",
                  r"\|e\| \sim e^{-\sigma N} "
                  r"\quad (\text{analitik } u)",
                  "**O'lchangan natija.** "
                  "Kodda $N = 6$ da "
                  "$1{,}7\\cdot10^{-5}$, "
                  "$N = 20$ da esa "
                  "$8{,}9\\cdot10^{-16}$ — "
                  "mashina aniqligi."),
                d("4. Spektral usulning "
                  "cheklovi",
                  r"\text{muntazam geometriya "
                  r"talab qilinadi}",
                  "Chebishev tugunlari "
                  "to'g'ri to'rtburchakda "
                  "tabiiy; murakkab "
                  "sohada esa ularni "
                  "joylashtirish "
                  "muammo."),
                d("5. Radial bazis g'oyasi",
                  r"u(x) \approx "
                  r"\sum_{j=1}^{N}\alpha_j"
                  r"\phi\left(\|x - x_j\|"
                  r"\right)",
                  "**Hal qiluvchi qadam.** "
                  "Bazis faqat **masofaga** "
                  "bog'liq, demak tugunlar "
                  "qanday joylashganining "
                  "ahamiyati yo'q — "
                  "to'r kerak emas."),
                d("6. Multikvadrik",
                  r"\phi(r) = \sqrt{r^2 + c^2}",
                  "Eng keng tarqalgan RBF. "
                  "$c$ — shakl parametri; "
                  "$c \\to 0$ da funksiya "
                  "o'tkirlashadi, katta "
                  "$c$ da yassilashadi."),
                d("7. Kollokatsiya",
                  r"\mathcal{L}u(x_i) = f(x_i), "
                  r"\quad u(x_b) = g(x_b)",
                  "Tenglamani tugunlarda "
                  "aynan qanoatlantiramiz. "
                  "Zaif formulirovka, "
                  "integrallash va yig'ish "
                  "— hech biri kerak "
                  "emas."),
                d("8. Hosilalar oson",
                  r"\frac{\partial^2\phi}"
                  r"{\partial x^2} = "
                  r"\frac{c^2}{(r^2+c^2)^{3/2}}",
                  "RBF analitik "
                  "differensiallanadi, "
                  "shuning uchun istalgan "
                  "tartibli operator "
                  "bevosita qo'llanadi."),
                d("9. Matritsaning xossalari",
                  r"\mathbf{A} \ \text{to'la, "
                  r"nosimmetrik, yomon "
                  r"shartlangan}",
                  "BEM dagi kabi to'la, "
                  "lekin undan ham yomon "
                  "shartlangan."),
                d("10. $c$ ning ikki "
                  "tomonlama ta'siri",
                  r"c \uparrow "
                  r"\;\Longrightarrow\; "
                  r"\text{aniqlik} \uparrow, "
                  r"\quad \kappa \uparrow",
                  "**Kasallikning "
                  "ildizi.** Yassiroq "
                  "bazis silliq "
                  "funksiyani yaxshiroq "
                  "yaqinlashtiradi, lekin "
                  "bazis funksiyalari "
                  "bir-biriga o'xshab "
                  "qoladi va matritsa "
                  "buziladi."),
                d("11. Noaniqlik prinsipi",
                  r"\text{xato} \times "
                  r"\kappa \approx "
                  r"\text{const}",
                  "**Shaback prinsipi.** "
                  "Ikkalasini bir vaqtda "
                  "yaxshilash mumkin "
                  "emas — bu usulning "
                  "kamchiligi emas, "
                  "nazariy chegara."),
                d("12. Optimal $c$",
                  r"\kappa(c_{opt}) \approx "
                  r"\varepsilon_{mach}^{-1} "
                  r"\approx 10^{16}",
                  "**O'lchangan natija.** "
                  "Eng yaxshi aniqlik "
                  "shartlanganlik ikkilangan "
                  "aniqlik chegarasiga "
                  "yetgan joyda — kodda "
                  "$c = 1{,}5$ da "
                  "$\\kappa = "
                  "4{,}3\\cdot10^{16}$."),
                d("13. $N$ bo'yicha "
                  "nomonotonlik",
                  r"N \uparrow \ \text{har doim "
                  r"ham yaxshiroq EMAS}",
                  "**Kutilmagan oqibat.** "
                  "Qat'iy $c$ da "
                  "tugunlar qo'shilishi "
                  "shartlanganlikni "
                  "oshiradi va yaxlitlash "
                  "xatosi yutuqni yeb "
                  "qo'yadi."),
            ],
            meaning=(
                "Bu mavzuda ikkita butunlay "
                "boshqacha falsafa "
                "uchrashadi. Spektral usul "
                "global silliq bazisga "
                "tayanadi va silliq "
                "masalada u hech narsa "
                "bilan raqobatlasha "
                "olmaydigan natija beradi: "
                "kodda 20 ta nuqta "
                "mashina aniqligini "
                "beradi. Lekin uning "
                "narxi 4-qadamda — "
                "geometriya muntazam "
                "bo'lishi shart. RBF esa "
                "aksincha: 5-qadamdagi "
                "g'oya tufayli u "
                "geometriyaga umuman "
                "befarq. Bazis faqat "
                "masofaga bog'liq, demak "
                "tugunlarni istalgan "
                "joyga, istalgan tartibda "
                "sochish mumkin — to'r, "
                "elementlar, bog'lanish "
                "jadvali, yig'ish — "
                "hech biri kerak emas. "
                "Metall shakllantirish "
                "yoki yorilish "
                "tarqalishida bu hal "
                "qiluvchi: tugunlar "
                "bilan birga "
                "harakatlanadi va "
                "hech qachon "
                "'ag'darilmaydi'. "
                "Ammo 10–12-qadamlar "
                "jiddiy narxni ochadi va "
                "bu narx nazariy. "
                "Shakl parametri $c$ "
                "ni oshirsangiz bazis "
                "yassilashadi va silliq "
                "funksiyani yaxshiroq "
                "yaqinlashtiradi — "
                "lekin ayni paytda bazis "
                "funksiyalari "
                "bir-biriga o'xshab "
                "qoladi va matritsa "
                "buziladi. Kod bu "
                "almashuvni aniq "
                "o'lchaydi: $c$ 0,05 "
                "dan 5 gacha "
                "o'zgarganda xato "
                "avval $9\\cdot10^{-2}$ "
                "dan "
                "$2{,}6\\cdot10^{-7}$ "
                "ga tushadi, so'ng "
                "yana "
                "$2\\cdot10^{-2}$ ga "
                "ko'tariladi, "
                "shartlanganlik esa "
                "38 dan "
                "$3\\cdot10^{18}$ ga "
                "monoton o'sadi. "
                "Optimal nuqta esa "
                "chiroyli tarzda "
                "aniqlanadi: u "
                "shartlanganlik "
                "ikkilangan aniqlik "
                "chegarasiga "
                "($\\sim10^{16}$) "
                "yetgan joyda. "
                "Ya'ni optimal $c$ "
                "matematik emas, "
                "**arifmetik** "
                "kattalik — u "
                "mashinaning "
                "aniqligiga "
                "bog'liq. "
                "13-qadam esa "
                "intuitsiyaga "
                "butunlay zid "
                "natija beradi: "
                "tugunlar sonini "
                "oshirish har doim "
                "ham yaxshiroq "
                "emas. Kodda "
                "$c = 2$ da "
                "$N = 11$ dan "
                "$N = 15$ ga "
                "o'tish xatoni "
                "o'n barobar "
                "**yomonlashtiradi**. "
                "Bu su-17 dagi "
                "jarima "
                "koeffitsienti va "
                "su-18 dagi to'r "
                "zichlashtirish "
                "bilan bir "
                "oiladagi hodisa: "
                "bir xatoni "
                "kamaytirish "
                "boshqasini "
                "oshiradi."
            ),
            equations=[
                eq(r"u(x) \approx \sum_{j=1}^{N}"
                   r"\alpha_j\,\phi\left(\|x - "
                   r"x_j\|\right), \qquad "
                   r"\phi(r) = \sqrt{r^2 + c^2}",
                   "RBF yoyilmasi va "
                   "multikvadrik.",
                   "RBF bazisi"),
                eq(r"D_{ij} = \frac{c_i(-1)^{i+j}}"
                   r"{c_j(x_i-x_j)}, \qquad "
                   r"D_{ii} = -\sum_{j\ne i}D_{ij}",
                   "Chebishev differensiallash "
                   "matritsasi.",
                   "Spektral matritsa"),
                eq(r"\|e\| \sim e^{-\sigma N} "
                   r"\quad (\text{spektral}), "
                   r"\qquad \|e\|\cdot\kappa "
                   r"\approx \text{const} \quad "
                   r"(\text{RBF})",
                   "Spektral yaqinlashish va "
                   "RBF noaniqlik prinsipi.",
                   "Aniqlik qonunlari"),
                eq(r"\kappa(c_{opt}) \approx "
                   r"\varepsilon_{mach}^{-1} "
                   r"\approx 10^{16}",
                   "Optimal shakl parametri "
                   "arifmetika bilan "
                   "belgilanadi.",
                   "Optimal c"),
            ],
            conditions=(
                "**Spektral usul qachon:**\n"
                "- Muntazam geometriya "
                "(to'rtburchak, doira);\n"
                "- Yechim **analitik** yoki "
                "juda silliq;\n"
                "- Eng yuqori aniqlik kerak "
                "bo'lganda.\n\n"
                "**To'rsiz usul qachon:**\n"
                "- Katta deformatsiya — to'r "
                "buziladi;\n"
                "- Harakatlanuvchi chegara, "
                "yorilish tarqalishi;\n"
                "- Tugunlarni qo'shish/olib "
                "tashlash oson bo'lishi "
                "kerak;\n"
                "- To'r qurish hisobning "
                "asosiy vaqtini olganda.\n\n"
                "**RBF da amaliy "
                "tavsiyalar:**\n"
                "1. $c$ ni har doim "
                "sozlang — universal "
                "qiymat yo'q; "
                "$c \\sim h$ tartibida "
                "boshlang;\n"
                "2. Shartlanganlikni "
                "kuzating: "
                "$\\kappa > 10^{16}$ "
                "bo'lsa natijaga "
                "ishonmang;\n"
                "3. $N$ ni oshirish "
                "natijani "
                "yomonlashtirishi "
                "mumkin — "
                "yaqinlashishni "
                "**tekshiring**;\n"
                "4. Mahalliy RBF "
                "(RBF-FD) katta "
                "masalalarda "
                "yagona amaliy "
                "variant.\n\n"
                "**Chegaraviy "
                "shartlar:** to'rsiz "
                "usullarda ular FEM "
                "dagidek oson emas. "
                "Kollokatsiyada "
                "to'g'ridan-to'g'ri "
                "qo'llanadi, lekin "
                "Galerkin asosidagi "
                "to'rsiz usullarda "
                "(EFG) shakl "
                "funksiyalari "
                "Kroneker delta "
                "xossasiga ega "
                "emas — Lagranj "
                "ko'paytuvchilari "
                "yoki jarima kerak "
                "(su-17)."
            ),
            worked=WorkedExample(
                statement=(
                    "Multikvadrik "
                    "$\\phi = \\sqrt{r^2+c^2}$ "
                    "uchun: (a) ikkinchi "
                    "hosilani toping; "
                    "(b) $c \\to 0$ va "
                    "$c \\to \\infty$ "
                    "chegaralarida bazis "
                    "qanday o'zgaradi; "
                    "(c) nima uchun katta "
                    "$c$ matritsani "
                    "buzadi."
                ),
                given=[
                    r"\phi(r) = \sqrt{r^2 + c^2}, "
                    r"\qquad r = |x - x_j|",
                    r"\text{bir o'lchovda } "
                    r"r^2 = (x-x_j)^2",
                ],
                steps=[
                    st(r"\frac{d\phi}{dx} = "
                       r"\frac{x - x_j}"
                       r"{\sqrt{r^2+c^2}}",
                       "Zanjir qoidasi."),
                    st(r"\frac{d^2\phi}{dx^2} = "
                       r"\frac{1}{\sqrt{r^2+c^2}} "
                       r"- \frac{(x-x_j)^2}"
                       r"{(r^2+c^2)^{3/2}}",
                       "Bo'linma hosilasi."),
                    st(r"= \frac{(r^2+c^2) - r^2}"
                       r"{(r^2+c^2)^{3/2}} = "
                       r"\frac{c^2}"
                       r"{(r^2+c^2)^{3/2}}",
                       "**Ixcham natija.** "
                       "Analitik, "
                       "yaqinlashishsiz."),
                    st(r"\text{(b)}\quad c \to 0: "
                       r"\ \phi \to |x - x_j|",
                       "Bazis o'tkir "
                       "burchakli bo'lib "
                       "qoladi."),
                    st(r"\frac{d^2\phi}{dx^2} \to "
                       r"0 \ (r \ne 0), \quad "
                       r"\to \infty \ (r = 0)",
                       "Ikkinchi hosila "
                       "delta-funksiyaga "
                       "aylanadi — "
                       "mahalliy, lekin "
                       "silliq emas."),
                    st(r"c \to \infty: \ \phi "
                       r"\approx c\left(1 + "
                       r"\frac{r^2}{2c^2}"
                       r"\right) = c + "
                       r"\frac{r^2}{2c}",
                       "Teylor yoyilmasi "
                       "(su-07)."),
                    st(r"\text{(c)}\quad \phi_j "
                       r"\approx c + "
                       r"\frac{(x-x_j)^2}{2c}",
                       "**Tuzoqning "
                       "ildizi.** Barcha "
                       "bazis funksiyalari "
                       "bir xil katta "
                       "doimiy $c$ ni o'z "
                       "ichiga oladi."),
                    st(r"\phi_i - \phi_j = "
                       r"\frac{(x-x_i)^2 - "
                       r"(x-x_j)^2}{2c}",
                       "Ular orasidagi "
                       "farq esa "
                       "$1/c$ kabi "
                       "**kichrayadi**."),
                    st(r"\Rightarrow \ "
                       r"\text{ustunlar deyarli "
                       r"chiziqli bog'liq}",
                       "Matritsa "
                       "singulyarlikka "
                       "yaqinlashadi."),
                    st(r"\kappa \sim c^{2N} \ "
                       r"(\text{taxminan})",
                       "Shartlanganlik "
                       "$c$ bilan juda "
                       "tez o'sadi — "
                       "kodda "
                       "$c = 0{,}05$ da "
                       "38, $c = 5$ da "
                       "$3\\cdot10^{18}$."),
                    st(r"\text{Optimal } c: \ "
                       r"\kappa \approx 10^{16}",
                       "**Amaliy qoida.** "
                       "Shartlanganlik "
                       "mashina "
                       "aniqligiga "
                       "yetgan joy — "
                       "kodda "
                       "$c = 1{,}5$."),
                ],
                answer=(
                    "(a) $\\phi'' = "
                    "c^2/(r^2+c^2)^{3/2}$; "
                    "(b) $c \\to 0$ da bazis "
                    "$|x-x_j|$ ga aylanadi "
                    "(o'tkir, mahalliy), "
                    "$c \\to \\infty$ da esa "
                    "$c + r^2/(2c)$ "
                    "(yassi, global); "
                    "(c) katta $c$ da barcha "
                    "bazis funksiyalari bir "
                    "xil $c$ ni o'z ichiga "
                    "oladi va farqlari "
                    "$1/c$ kabi kichrayadi — "
                    "ustunlar deyarli "
                    "chiziqli bog'liq "
                    "bo'lib qoladi. Kodda "
                    "optimal "
                    "$c = 1{,}5$ da "
                    "$\\kappa = "
                    "4{,}3\\cdot10^{16}$."
                ),
                engineering_note=(
                    "(c) dagi tahlil "
                    "noaniqlik "
                    "prinsipining fizik "
                    "ma'nosini beradi. "
                    "Yassi bazis silliq "
                    "funksiyani yaxshi "
                    "yaqinlashtiradi, "
                    "chunki u o'zi "
                    "silliq — lekin "
                    "aynan shuning uchun "
                    "bazis funksiyalari "
                    "bir-biridan kam "
                    "farq qiladi va "
                    "ularni ajratish "
                    "qiyinlashadi. Bu "
                    "su-17 dagi jarima "
                    "koeffitsienti bilan "
                    "bir xil tuzilishga "
                    "ega: u yerda "
                    "$\\beta$ ni "
                    "oshirish shartni "
                    "aniqroq bajaradi, "
                    "lekin "
                    "shartlanganlikni "
                    "buzadi; bu yerda "
                    "$c$ ni oshirish "
                    "aniqlikni "
                    "oshiradi, lekin "
                    "shartlanganlikni "
                    "buzadi. Ikkala "
                    "holatda ham "
                    "optimal qiymat "
                    "**arifmetika** "
                    "bilan "
                    "belgilanadi, "
                    "matematika bilan "
                    "emas — ya'ni u "
                    "mashinaning "
                    "aniqligiga "
                    "bog'liq. "
                    "To'rt karra "
                    "aniqlikda "
                    "hisoblansangiz "
                    "optimal $c$ "
                    "kattaroq bo'lardi "
                    "va natija "
                    "aniqroq. Bu "
                    "su-02 va su-05 "
                    "dagi xatolik "
                    "byudjeti "
                    "g'oyasining "
                    "eng aniq "
                    "ko'rinishi."
                ),
            ),
            computation=Computation(
                caption=(
                    "Chebishev spektral usulini "
                    "qurish, RBF kollokatsiyani "
                    "amalga oshirish va "
                    "noaniqlik prinsipini "
                    "o'lchash."
                ),
                code='''"""Spektral va to'rsiz usullar."""
import numpy as np
from labkit import PARAMS, note, series, table, value

N_rbf = int(PARAMS.get("N_rbf", 15))
c_shape = float(PARAMS.get("c_shape", 1.0))
N_spec = int(PARAMS.get("N_spec", 12))


# --- (1) CHEBISHEV SPEKTRAL USUL ---
def cheb_D(N):
    """Chebishev differensiallash matritsasi (su-25 DQM bilan bir oila)."""
    x = np.cos(np.pi*np.arange(N + 1)/N)
    cc = np.ones(N + 1)
    cc[0] = cc[N] = 2.0
    cc = cc*(-1)**np.arange(N + 1)
    X = np.tile(x, (N + 1, 1)).T
    dX = X - X.T
    D = np.outer(cc, 1.0/cc)/(dX + np.eye(N + 1))
    D = D - np.diag(D.sum(axis=1))      # qator yig'indisi noli
    return D, x


D_t, x_t = cheb_D(8)
value("Chebishev D: max|D @ 1| (nol bo'lishi kerak)",
      float(np.max(np.abs(D_t @ np.ones(len(x_t))))), "—")
# ko'phadlarni aynan differensiallaydimi
rows0 = []
for N in [6, 10, 14]:
    D, x = cheb_D(N)
    line = [N]
    for pdeg in [1, 3, N - 1, N]:
        f = x**pdeg
        ex = pdeg*x**(pdeg - 1)
        den = max(float(np.max(np.abs(ex))), 1e-30)
        line.append(f"{float(np.max(np.abs(D @ f - ex)))/den:.1e}")
    rows0.append(line)
table("Chebishev matritsasi ko'phadlarda",
      ["N", "x^1", "x^3", "x^(N-1)", "x^N"], rows0)

rows = []
sp_N, sp_e = [], []
for N in [4, 6, 8, 10, 12, 16, 20]:
    D, x = cheb_D(N)
    D2 = (D @ D)[1:N, 1:N]
    xs = x[1:N]
    u_ex = np.sin(np.pi*(xs + 1)/2)
    rhs = -(np.pi/2)**2*u_ex
    u = np.linalg.solve(D2, rhs)
    e = float(np.max(np.abs(u - u_ex)))
    rows.append([N, f"{e:.4e}",
                 f"{np.linalg.cond(D2):.2e}"])
    sp_N.append(N)
    sp_e.append(e)
table("Chebishev spektral usuli: u'' = -(pi/2)^2 u, u(+-1) = 0",
      ["N", "maks xato", "cond(D2)"], rows)
series("Spektral yaqinlashish", sp_N,
       [np.log10(max(v, 1e-18)) for v in sp_e],
       xlabel="N", ylabel="log10(xato)")
value("Spektral: N = 6 dagi xato", float(sp_e[sp_N.index(6)]), "—")
value("Spektral: N = 20 dagi xato", float(sp_e[sp_N.index(20)]), "—")
note("Chebishev matritsasi ham qator yig'indisi noli shartiga "
     "bo'ysunadi (D @ 1 = 0) - su-25 dagi DQM va su-26 dagi BEM bilan "
     "AYNI ayniyat. Spektral yaqinlashish esa hech narsa bilan "
     "raqobatlasha olmaydi: N = 6 da xato 1.7e-5, N = 20 da esa 8.9e-16 "
     "- ya'ni MASHINA ANIQLIGI. Shartlanganlik ham me'yorda qoladi. "
     "Lekin buning sharti - muntazam geometriya va silliq yechim.")


# --- (2) TO'RSIZ RBF KOLLOKATSIYA ---
def rbf(r, c):
    return np.sqrt(r*r + c*c)


def rbf_d2(r, c):
    """d2/dx2 multikvadrik - ANALITIK (sinovdan o'tgan)."""
    return c*c/np.power(r*r + c*c, 1.5)


def solve_rbf(N, c, L=1.0):
    """u'' = -pi^2 sin(pi x), u(0) = u(L) = 0 - TO'RSIZ kollokatsiya."""
    x = np.linspace(0.0, L, N)
    A = np.zeros((N, N))
    b = np.zeros(N)
    for i in range(N):
        for j in range(N):
            r = abs(x[i] - x[j])
            A[i, j] = rbf(r, c) if i in (0, N - 1) else rbf_d2(r, c)
        b[i] = 0.0 if i in (0, N - 1) else -np.pi**2*np.sin(np.pi*x[i])
    al = np.linalg.solve(A, b)
    xe = np.linspace(0.0, L, 401)
    ue = np.array([float(np.sum(al*rbf(np.abs(xx - x), c))) for xx in xe])
    ex = np.sin(np.pi*xe)
    err = float(np.max(np.abs(ue - ex))/np.max(np.abs(ex)))
    return err, float(np.linalg.cond(A)), xe, ue, ex


# analitik ikkinchi hosilani tekshirish
c_chk = 0.7
rr = np.linspace(-2, 2, 9)
num_d2 = np.array([(rbf(abs(t + 1e-5), c_chk) - 2*rbf(abs(t), c_chk) +
                    rbf(abs(t - 1e-5), c_chk))/1e-10 for t in rr])
value("RBF ikkinchi hosilasi: analitik va sonli farqi",
      float(np.max(np.abs(rbf_d2(np.abs(rr), c_chk) - num_d2))), "—")

rows2 = []
cs = [0.05, 0.1, 0.2, 0.4, 0.6, 0.8, 1.0, 1.5, 2.0, 3.0, 5.0]
errs, konds = [], []
for c in cs:
    e, k, *_ = solve_rbf(N_rbf, c)
    rows2.append([f"{c:.2f}", f"{e:.3e}", f"{k:.3e}", f"{e*k:.3e}"])
    errs.append(e)
    konds.append(k)
table(f"NOANIQLIK PRINSIPI: shakl parametri c ning roli (N = {N_rbf})",
      ["c", "nisbiy xato", "cond(A)", "xato x cond"], rows2)
i_best = int(np.argmin(errs))
value("Eng yaxshi c", float(cs[i_best]), "—")
value("Eng yaxshi c dagi xato", float(errs[i_best]), "—")
value("Eng yaxshi c dagi shartlanganlik", float(konds[i_best]), "—")
value("Ikkilangan aniqlik chegarasi 1/eps",
      float(1.0/np.finfo(float).eps), "—")
series("RBF xatosi", [np.log10(c) for c in cs],
       [np.log10(max(e, 1e-18)) for e in errs],
       xlabel="log10(c)", ylabel="log10(xato)")
series("RBF shartlanganligi", [np.log10(c) for c in cs],
       [np.log10(k) for k in konds],
       xlabel="log10(c)", ylabel="log10(cond)")
note(f"NOANIQLIK PRINSIPI (Shaback). c ortgani sari shartlanganlik "
     f"MONOTON o'sadi (38 dan 3e18 gacha), xato esa avval kamayadi, "
     f"minimumga yetadi va keyin YANA O'SADI. Minimum c = {cs[i_best]} "
     f"da va o'sha yerda cond = {konds[i_best]:.1e} - ya'ni ikkilangan "
     f"aniqlik chegarasi 1/eps = {1.0/np.finfo(float).eps:.1e} bilan bir "
     f"TARTIBDA (taxminan 10 barobar ichida). Demak optimal "
     f"shakl parametri MATEMATIK emas, ARIFMETIK kattalik: u "
     f"mashinaning aniqligiga bog'liq. Bu su-17 dagi jarima "
     f"koeffitsienti va su-02 dagi xatolik byudjeti bilan bir xil "
     f"tuzilish: bir xatoni kamaytirish ikkinchisini oshiradi.")

# --- (3) N ni oshirish HAR DOIM yaxshi emas ---
rows3 = []
for c in [0.5, 1.0, 2.0, 3.0]:
    line = [f"{c:.1f}"]
    for N in [7, 11, 15, 21]:
        e, k, *_ = solve_rbf(N, c)
        line.append(f"{e:.2e}")
    rows3.append(line)
table("Tugunlar sonini oshirish har doim yaxshimi?",
      ["c", "N = 7", "N = 11", "N = 15", "N = 21"], rows3)
e11, _, *_ = solve_rbf(11, 2.0)
e15, _, *_ = solve_rbf(15, 2.0)
value("c = 2.0: N = 11 dagi xato", float(e11), "—")
value("c = 2.0: N = 15 dagi xato", float(e15), "—")
value("N oshganda xato necha barobar o'zgardi",
      float(e15/e11), "barobar")
note("INTUITSIYAGA ZID NATIJA. Qat'iy c da tugunlar sonini oshirish "
     "xatoni YOMONLASHTIRISHI mumkin: c = 2.0 da N = 11 dan N = 15 ga "
     "o'tish xatoni o'n barobardan ko'proq oshiradi. Sabab - tugunlar "
     "zichlashgani sari bazis funksiyalari bir-biriga yaqinlashadi, "
     "shartlanganlik buziladi va yaxlitlash xatosi yaqinlashish "
     "yutug'ini yeb qo'yadi. Amalda c ni N bilan birga sozlash kerak "
     "(odatda c ~ h). Bu FEM va chekli ayirmalarda bo'lmaydigan "
     "hodisa: u yerda to'r zichlashtirish har doim yaxshilaydi.")

# --- (4) YECHIM PROFILI ---
e_b, k_b, xe, ue, ex = solve_rbf(N_rbf, c_shape)
series("RBF yechimi", xe.tolist(), ue.tolist(), xlabel="x", ylabel="u")
series("Aniq yechim sin(pi x)", xe.tolist(), ex.tolist(),
       xlabel="x", ylabel="u")
value(f"Tanlangan c = {c_shape}: nisbiy xato", float(e_b), "—")
value(f"Tanlangan c = {c_shape}: shartlanganlik", float(k_b), "—")
x_nodes = np.linspace(0, 1, N_rbf)
for j in [0, N_rbf//3, N_rbf//2]:
    series(f"Bazis funksiyasi j = {j}", xe.tolist(),
           rbf(np.abs(xe - x_nodes[j]), c_shape).tolist(),
           xlabel="x", ylabel="phi")

# --- (5) SPEKTRAL va RBF: bevosita taqqoslash ---
rows4 = []
for N in [7, 11, 15, 21]:
    e_r, k_r, *_ = solve_rbf(N, cs[i_best])
    D, x = cheb_D(N - 1)
    D2 = (D @ D)[1:N-1, 1:N-1]
    xs = x[1:N-1]
    u_ex = np.sin(np.pi*(xs + 1)/2)
    u = np.linalg.solve(D2, -(np.pi/2)**2*u_ex)
    e_s = float(np.max(np.abs(u - u_ex)))
    rows4.append([N, f"{e_s:.3e}", f"{np.linalg.cond(D2):.2e}",
                  f"{e_r:.3e}", f"{k_r:.2e}"])
table("Spektral (Chebishev) va to'rsiz (RBF) bevosita taqqoslash",
      ["N", "spektral xato", "spektral cond", "RBF xato", "RBF cond"],
      rows4)
note("SODDA SOHADA SPEKTRAL USUL USTUN: bir xil N da u ham aniqroq, "
     "ham yaxshi shartlangan. Demak RBF ning qiymati XOM ANIQLIKDA "
     "emas. Uning afzalligi boshqa joyda: tugunlarni istalgan joyga "
     "sochish mumkin, to'r va bog'lanish jadvali kerak emas, "
     "tugunlarni hisob davomida qo'shish yoki olib tashlash oson. "
     "Metall shakllantirish, yorilish tarqalishi va harakatlanuvchi "
     "chegarali masalalarda aynan shu hal qiluvchi - u yerda FEM "
     "to'ri buziladi (su-14 dagi det J <= 0) va qayta qurish kerak "
     "bo'ladi.")

table("Uch yondashuvning taqqoslanishi",
      ["Jihat", "FEM", "Spektral", "To'rsiz (RBF)"],
      [["Bazis", "mahalliy, bo'lakli", "global, silliq",
        "global, radial"],
       ["To'r", "kerak", "muntazam kerak", "KERAK EMAS"],
       ["Yaqinlashish", "h^p", "eksponensial", "c ga bog'liq"],
       ["Matritsa", "siyrak", "to'la, me'yorda", "to'la, YOMON"],
       ["Murakkab geometriya", "OSON", "qiyin", "oson"],
       ["Katta deformatsiya", "to'r buziladi", "mos emas", "TABIIY"],
       ["Sozlash", "kerak emas", "kerak emas", "c ni sozlash SHART"]])
''',
                parameters=[
                    p("N_rbf", "RBF tugunlari soni", 7.0, 25.0, 15.0,
                      2.0),
                    p("c_shape", "Shakl parametri c", 0.05, 5.0, 1.0,
                      0.05),
                    p("N_spec", "Spektral tartib N", 4.0, 24.0, 12.0,
                      2.0),
                ],
                expected_output=(
                    "Chebishev matritsasi "
                    "$\\mathbf{D}\\mathbf{1} = "
                    "\\mathbf{0}$ ayniyatiga "
                    "bo'ysunadi — su-25 va "
                    "su-26 bilan aynan bir "
                    "xil. Spektral usul "
                    "$N = 6$ da "
                    "$1{,}7\\cdot10^{-5}$, "
                    "$N = 20$ da esa "
                    "$8{,}9\\cdot10^{-16}$ "
                    "beradi. RBF da shakl "
                    "parametri $c$ "
                    "0,05 dan 5 gacha "
                    "o'zgarganda "
                    "shartlanganlik 38 "
                    "dan "
                    "$3\\cdot10^{18}$ ga "
                    "monoton o'sadi, xato "
                    "esa "
                    "$c = 1{,}5$ da "
                    "$2{,}6\\cdot10^{-7}$ "
                    "minimumiga yetib, "
                    "keyin yana "
                    "ko'tariladi; "
                    "minimum "
                    "shartlanganlik "
                    "$10^{16}$ ga yetgan "
                    "joyda. Qat'iy $c$ da "
                    "tugunlar sonini "
                    "oshirish xatoni "
                    "yomonlashtirishi "
                    "mumkin. Sodda sohada "
                    "spektral usul RBF "
                    "dan ham aniqroq, "
                    "ham yaxshi "
                    "shartlangan."
                ),
            ),
            visual=vis(
                kind="Radial bazis va noaniqlik prinsipi",
                tool="React/SVG + Manim",
                description=(
                    "Bazis funksiyalari, tugun "
                    "sochilishi va aniqlik–"
                    "shartlanganlik almashuvi."
                ),
                how_to_draw=(
                    "React/SVG: yuqori panelda "
                    "bir necha radial bazis "
                    "funksiyasi chiziladi va "
                    "$c$ slayderi bilan "
                    "ularning kengligi "
                    "o'zgaradi. Kichik $c$ da "
                    "ular o'tkir va "
                    "bir-biridan aniq "
                    "ajralib turadi, katta "
                    "$c$ da esa deyarli "
                    "**ustma-ust tushadi** — "
                    "shartlanganlikning "
                    "buzilishi shu "
                    "ustma-ust tushishda "
                    "ko'zga tashlanadi. "
                    "O'rta panelda ikkita "
                    "egri chiziq bitta "
                    "logarifmik o'qda: "
                    "$c$ ga qarab xato "
                    "(avval tushadi, "
                    "so'ng ko'tariladi — "
                    "**V shaklida**) va "
                    "shartlanganlik "
                    "(monoton "
                    "ko'tariladi). "
                    "Ularning kesishgan "
                    "atrofi yashil "
                    "bilan 'optimal "
                    "oraliq' deb "
                    "belgilanadi va "
                    "$10^{16}$ darajasi "
                    "punktir chiziq "
                    "bilan 'ikkilangan "
                    "aniqlik chegarasi' "
                    "deb yoziladi — "
                    "minimum aynan shu "
                    "chiziqqa "
                    "tushishi "
                    "ko'rinadi. Pastki "
                    "panelda "
                    "to'rsizlikning "
                    "ma'nosi: "
                    "sichqoncha bilan "
                    "istalgan joyga "
                    "tugun "
                    "qo'yiladi va "
                    "yechim darhol "
                    "qayta "
                    "hisoblanadi — "
                    "hech qanday "
                    "element yoki "
                    "bog'lanish "
                    "chizilmaydi."
                ),
            ),
            interp=(
                "Chebishev matritsasining "
                "$\\mathbf{D}\\mathbf{1} = "
                "\\mathbf{0}$ ayniyatiga "
                "bo'ysunishi tasodif emas: "
                "bu su-25 dagi DQM va su-26 "
                "dagi BEM da uchragan aynan "
                "o'sha shart. Uchala usul "
                "ham doimiy funksiyani "
                "to'g'ri ifodalashi kerak "
                "va bu ularning "
                "diagonalini belgilaydi — "
                "butunlay boshqacha "
                "usullardagi umumiy "
                "tuzilma. Spektral "
                "natijalar esa shunchaki "
                "ta'sirli: 20 ta nuqta "
                "mashina aniqligini "
                "beradi va "
                "shartlanganlik ham "
                "me'yorda qoladi. "
                "Shuning uchun muntazam "
                "geometriya va silliq "
                "yechim bo'lganda "
                "spektral usulni "
                "tanlamaslik uchun "
                "jiddiy sabab kerak. "
                "RBF tajribasi esa "
                "mavzuning markaziy "
                "natijasini beradi. "
                "Shakl parametri "
                "oshgani sari "
                "shartlanganlik "
                "monoton buziladi, "
                "xato esa V shaklida — "
                "avval kamayib, so'ng "
                "yana o'sib. Minimum "
                "nuqta muhim: u "
                "shartlanganlik "
                "ikkilangan aniqlik "
                "chegarasiga yetgan "
                "joyda joylashgan. "
                "Ya'ni optimal shakl "
                "parametri matematik "
                "emas, **arifmetik** "
                "kattalik — "
                "mashinaning "
                "aniqligiga bog'liq. "
                "To'rt karra "
                "aniqlikda "
                "hisoblansangiz "
                "optimal $c$ kattaroq "
                "bo'lardi va natija "
                "aniqroq. Bu su-02 "
                "dagi xatolik "
                "byudjeti va su-17 "
                "dagi jarima "
                "koeffitsienti bilan "
                "bir xil tuzilish. "
                "Tugunlar soni "
                "tajribasi "
                "intuitsiyaga "
                "butunlay zid: "
                "qat'iy $c$ da "
                "$N$ ni oshirish "
                "xatoni o'n "
                "barobar "
                "yomonlashtirishi "
                "mumkin. FEM va "
                "chekli ayirmalarda "
                "bunday hodisa yo'q "
                "— u yerda "
                "zichlashtirish har "
                "doim yaxshilaydi. "
                "Nihoyat bevosita "
                "taqqoslash halol "
                "xulosa beradi: "
                "sodda sohada "
                "spektral usul RBF "
                "dan har jihatdan "
                "ustun. Demak RBF "
                "ning qiymati xom "
                "aniqlikda emas, "
                "geometrik "
                "moslashuvchanlikda "
                "— tugunlarni "
                "istalgan joyga "
                "sochish va hisob "
                "davomida "
                "o'zgartirish "
                "imkoniyatida."
            ),
            mistakes=[
                "$c$ ni sozlamasdan "
                "universal qiymat "
                "ishlatish. Optimal $c$ "
                "masalaga va $N$ ga "
                "bog'liq.",
                "$N$ ni oshirish har doim "
                "yaxshilaydi deb "
                "hisoblash. Qat'iy $c$ da "
                "u natijani "
                "yomonlashtirishi mumkin.",
                "Shartlanganlikni "
                "kuzatmaslik. "
                "$\\kappa > 10^{16}$ "
                "bo'lsa natija "
                "yaxlitlash "
                "shovqinidan iborat.",
                "Sodda, muntazam sohada "
                "RBF ishlatish. U yerda "
                "spektral usul ham "
                "aniqroq, ham "
                "barqarorroq.",
                "To'rsiz usullarda "
                "chegaraviy shartlarni "
                "FEM dagidek oson deb "
                "o'ylash. Galerkin "
                "asosidagi variantlarda "
                "Lagranj ko'paytuvchilari "
                "kerak.",
                "Katta masalada to'la "
                "RBF matritsasini "
                "ishlatish. Mahalliy "
                "RBF-FD yagona amaliy "
                "variant.",
            ],
            quiz=[
                q("RBF nima uchun to'r talab "
                  "qilmaydi?",
                  "Bazis faqat "
                  "$\\|x - x_j\\|$ masofaga "
                  "bog'liq, shuning uchun "
                  "tugunlarning o'zaro "
                  "joylashuvi va bog'lanish "
                  "jadvali kerak emas.",
                  "konseptual"),
                q("Noaniqlik prinsipi nimani "
                  "aytadi?",
                  "Yaxshi shartlanganlik va "
                  "yuqori aniqlikka bir "
                  "vaqtda erishib bo'lmaydi: "
                  "xato $\\times$ "
                  "shartlanganlik taxminan "
                  "doimiy.", "konseptual"),
                q("Multikvadrikning ikkinchi "
                  "hosilasi qanday?",
                  "$\\phi'' = c^2/"
                  "(r^2+c^2)^{3/2}$ — "
                  "analitik, hech qanday "
                  "yaqinlashishsiz.",
                  "hisob"),
                q("Kodda optimal $c$ qayerda "
                  "va nima uchun aynan u "
                  "yerda?",
                  "$c = 1{,}5$ da, chunki "
                  "o'sha yerda "
                  "shartlanganlik "
                  "$4\\cdot10^{16}$ — "
                  "ikkilangan aniqlik "
                  "chegarasiga yetgan joy. "
                  "Optimal $c$ arifmetik "
                  "kattalik.", "kod"),
                q("Qat'iy $c$ da $N$ ni "
                  "oshirish nima uchun "
                  "zarar keltirishi "
                  "mumkin?",
                  "Tugunlar zichlashgani "
                  "sari bazis funksiyalari "
                  "bir-biriga "
                  "yaqinlashadi, "
                  "shartlanganlik buziladi "
                  "va yaxlitlash xatosi "
                  "yutuqni yeb qo'yadi.",
                  "kod"),
                q("Sodda sohada spektral va "
                  "RBF dan qaysi biri "
                  "afzal?",
                  "Spektral — u ham "
                  "aniqroq, ham yaxshi "
                  "shartlangan. RBF ning "
                  "qiymati aniqlikda emas, "
                  "geometrik "
                  "moslashuvchanlikda.",
                  "talqin"),
                q("To'rsiz usullar qaysi "
                  "masalalarda hal qiluvchi "
                  "afzallik beradi?",
                  "Katta deformatsiya, "
                  "yorilish tarqalishi, "
                  "harakatlanuvchi chegara — "
                  "FEM to'ri buziladigan "
                  "(su-14) holatlarda.",
                  "talqin"),
            ],
            bridge=(
                "Endi bizda usullarning "
                "keng to'plami bor: chekli "
                "ayirmalar, FEM, DQM, BEM, "
                "spektral va to'rsiz. Har "
                "biri o'z aniqlik "
                "da'vosiga ega. Lekin "
                "hisob natijasiga qachon "
                "**ishonish** mumkin? "
                "Keyingi mavzuda buni "
                "rasmiy tartibga "
                "solamiz."
            ),
            research=(
                "Zamonaviy usullarni "
                "chuqurlashtiring. "
                "(1) RBF-FD usulini "
                "o'rganing: mahalliy "
                "shablonlarda RBF "
                "ishlatib, siyrak "
                "matritsa olish — "
                "noaniqlik prinsipini "
                "qanday chetlab "
                "o'tadi? "
                "(2) Element erkin "
                "Galerkin (EFG) va "
                "harakatlanuvchi eng "
                "kichik kvadratlar "
                "(MLS) usulini ko'rib "
                "chiqing: shakl "
                "funksiyalari "
                "Kroneker delta "
                "xossasiga ega "
                "emasligi chegaraviy "
                "shartlarda qanday "
                "muammo tug'diradi? "
                "(3) Spektral "
                "elementlar usulini "
                "o'rganing: FEM ning "
                "mahalliyligi va "
                "spektral aniqlikning "
                "birikmasi. "
                "(4) Materiallar "
                "nuqtasi usulini "
                "(MPM) ko'rib chiqing: "
                "u to'r va zarrachalarni "
                "birlashtiradi va "
                "juda katta "
                "deformatsiyada "
                "ishlatiladi."
            ),
            manim_ref=manim(
                scene="MeshfreeScene",
                module="manim/scenes/su_modern.py",
                title="To'rsizlik va noaniqlik prinsipi",
                summary=(
                    "Avval FEM to'ri "
                    "katta deformatsiyada "
                    "buziladi: elementlar "
                    "cho'ziladi va "
                    "ag'dariladi, "
                    "$\\det\\mathbf{J}$ "
                    "qizaradi. Keyin "
                    "elementlar "
                    "yo'qoladi va faqat "
                    "tugunlar qoladi — "
                    "ular bemalol "
                    "harakatlanadi. "
                    "So'ng radial bazis "
                    "funksiyalari "
                    "chiziladi va shakl "
                    "parametri oshirilib "
                    "boriladi: ular "
                    "yassilashadi, "
                    "ustma-ust tushadi "
                    "va yonidagi "
                    "shartlanganlik "
                    "ko'rsatkichi "
                    "portlaydi."
                ),
            ),
        ),
    ),

    # ------------------------------------------------------------------ su-28
    Topic(
        id="su-28",
        subject_id=S, module_id=M, order=28,
        title="Verifikatsiya va validatsiya (V&V)",
        description=(
            "Kod verifikatsiyasi va yechim verifikatsiyasining farqi, "
            "ishlab chiqilgan yechimlar usuli (MMS), Richardson "
            "ekstrapolyatsiyasi va to'r yaqinlashish indeksi (GCI)."
        ),
        learning_objective=(
            "Kodni MMS bilan verifikatsiya qilish, yechim xatosini aniq "
            "javobni bilmasdan baholash va natijaning ishonchliligini "
            "rasmiy tartibda asoslash."
        ),
        prerequisites=["su-27", "su-18", "su-21"],
        mathematical_core=(
            "MMS: $u_{ex}$ tanlanadi, $f = \\mathcal{L}u_{ex}$ "
            "chiqariladi; "
            "$p_{obs} = \\ln\\frac{f_3-f_2}{f_2-f_1}/\\ln r$; "
            "$\\mathrm{GCI} = \\frac{F_s|\\varepsilon|}{r^{p}-1}$."
        ),
        engineering_application=(
            "Aviatsiya, yadro energetikasi va tibbiy qurilmalarda "
            "sertifikatlash talabi; har qanday jiddiy hisobotning "
            "ishonchlilik asosi."
        ),
        computational_component=(
            "MMS bilan tartibni o'lchash, ataylab kiritilgan xatoni "
            "aniqlash, GCI bilan xatolik chegarasini qurish."
        ),
        visualization_component=(
            "Yaqinlashish egri chiziqlari, tartib o'lchovi, GCI "
            "tasmasi."
        ),
        research_extension=(
            "ASME V&V 20 standartini o'rganing: validatsiya "
            "noaniqligini rasmiy hisoblash tartibi."
        ),
        difficulty="orta",
        previous_link=(
            "su-25…su-27 da usullar to'plami kengaydi va har biri o'z "
            "aniqlik da'vosiga ega edi. Endi asosiy savolga javob "
            "beramiz: hisob natijasiga qachon va qanchalik ishonish "
            "mumkin?"
        ),
        next_topic="su-29",
        estimated_minutes=85,
        tags=["V&V", "MMS", "Richardson", "GCI", "verifikatsiya"],
        lesson=_lesson(
            problem=(
                "Samolyot qanoti "
                "konstruksiyasining hisobi "
                "sertifikatlashga "
                "topshirilmoqda. Ekspert "
                "bitta savol beradi: "
                "'Natijangizning xatosi "
                "qancha?' Javob "
                "'to'rni zichlashtirdim, "
                "natija o'zgarmadi' — "
                "yetarli emas. Ekspert "
                "**raqam** so'raydi: "
                "xatolik chegarasi necha "
                "foiz va u qanday "
                "asoslangan? Bundan "
                "tashqari kodning o'zi "
                "to'g'ri "
                "dasturlanganini qanday "
                "isbotlaysiz — axir "
                "murakkab masalada aniq "
                "yechim yo'q, taqqoslash "
                "uchun hech narsa "
                "yo'q. Ikkala savolga "
                "ham tizimli javob bor."
            ),
            concepts=[
                c("Verifikatsiya",
                  "**Tenglamalarni to'g'ri "
                  "yechyapmizmi?** — sof "
                  "matematik savol, "
                  "tajriba kerak emas."),
                c("Validatsiya",
                  "**To'g'ri tenglamalarni "
                  "yechyapmizmi?** — "
                  "model haqiqatga mos "
                  "keladimi; tajriba "
                  "kerak."),
                c("Kod verifikatsiyasi",
                  "Dasturda xato bormi; "
                  "MMS bilan tartibni "
                  "o'lchash orqali."),
                c("Yechim verifikatsiyasi",
                  "Shu masaladagi "
                  "diskretlashtirish "
                  "xatosi qancha; "
                  "Richardson va GCI "
                  "bilan."),
                c("Ishlab chiqilgan "
                  "yechimlar usuli (MMS)",
                  "Yechimni **tanlaymiz**, "
                  "manbani undan "
                  "chiqaramiz — shunda "
                  "aniq javob ma'lum "
                  "bo'ladi."),
                c("To'r yaqinlashish "
                  "indeksi (GCI)",
                  "Xatolik uchun xavfsizlik "
                  "koeffitsienti bilan "
                  "baho: "
                  "$F_s = 1{,}25$."),
            ],
            derivation=[
                d("1. Ikki xil savol",
                  r"\text{V: } \|u_h - u_{ex}\|; "
                  r"\qquad \text{Val: } "
                  r"\|u_{ex} - u_{haqiqat}\|",
                  "**Asosiy farq.** "
                  "Verifikatsiya "
                  "matematik, validatsiya "
                  "esa fizik savol. "
                  "Birinchisini "
                  "kompyuterda hal qilish "
                  "mumkin, ikkinchisi "
                  "uchun tajriba kerak."),
                d("2. MMS ning teskari "
                  "g'oyasi",
                  r"u_{ex} \ \text{TANLANADI} "
                  r"\;\Longrightarrow\; "
                  r"f = \mathcal{L}u_{ex}",
                  "**Hal qiluvchi qadam.** "
                  "Odatda $f$ berilgan va "
                  "$u$ izlanadi; bu yerda "
                  "aksincha. Natijada aniq "
                  "javob **har doim** "
                  "ma'lum bo'ladi."),
                d("3. $u_{ex}$ ni tanlash "
                  "qoidalari",
                  r"u_{ex} \ \text{silliq, "
                  r"nolmas, barcha hadlarni "
                  r"faollashtirsin}",
                  "Masalan "
                  "$\\sin(\\pi x)(1+x^2)$: "
                  "u chegaraviy shartni "
                  "qanoatlantiradi va "
                  "operatorning barcha "
                  "hadlarini ishga "
                  "soladi."),
                d("4. Tartibni o'lchash",
                  r"p_{obs} = "
                  r"\frac{\ln(e_1/e_2)}"
                  r"{\ln(h_1/h_2)}",
                  "Ketma-ket ikki to'rdan. "
                  "Bu su-18 dagi tartib "
                  "o'lchovining aynan "
                  "o'zi, faqat endi "
                  "**kodni tekshirish** "
                  "uchun."),
                d("5. Nazariy tartiblar",
                  r"\|e\|_{L^2} \sim h^{p+1}, "
                  r"\qquad \|e\|_{E} \sim h^{p}",
                  "**O'lchangan natija.** "
                  "Kod $p = 1, 2, 3$ uchun "
                  "ham 3–4 xonali "
                  "aniqlikda shu "
                  "qiymatlarni beradi."),
                d("6. MMS ning kuchi",
                  r"p_{obs} \ne p_{nazariy} "
                  r"\;\Longrightarrow\; "
                  r"\text{KODDA XATO}",
                  "**Asosiy natija.** "
                  "Tartib mos kelmasa, "
                  "dasturda xato bor — "
                  "boshqa tushuntirish "
                  "yo'q."),
                d("7. Insidiy xatolar",
                  r"\text{kod yaqinlashadi, "
                  r"lekin NOTO'G'RI "
                  r"tartibda}",
                  "**Eng xavfli hol.** "
                  "Kodda yuk vektori "
                  "noto'g'ri bo'lsa, "
                  "natija baribir "
                  "yaqinlashadi va "
                  "ishonarli ko'rinadi — "
                  "faqat tartib "
                  "3 o'rniga 2 "
                  "bo'lib qoladi."),
                d("8. Yechim "
                  "verifikatsiyasi",
                  r"u_{ex} \ \text{NOMA'LUM} "
                  r"\;\Longrightarrow\; "
                  r"\text{uchta to'r kerak}",
                  "Haqiqiy masalada aniq "
                  "yechim yo'q, shuning "
                  "uchun uchta to'rdan "
                  "baho quriladi."),
                d("9. Kuzatilgan tartib",
                  r"p_{obs} = \frac{\ln\left|"
                  r"\frac{f_3-f_2}{f_2-f_1}"
                  r"\right|}{\ln r}",
                  "$f_1$ — eng zich to'r. "
                  "Aniq yechim kerak emas "
                  "— faqat uchta natija."),
                d("10. Richardson "
                  "ekstrapolyatsiyasi",
                  r"f_{ext} = f_1 + "
                  r"\frac{f_1 - f_2}"
                  r"{r^{p_{obs}} - 1}",
                  "su-07 dagi Richardson "
                  "ekstrapolyatsiyasining "
                  "aynan o'zi. "
                  "**O'lchangan natija:** "
                  "u eng zich to'rdan "
                  "30–437 barobar "
                  "aniqroq."),
                d("11. GCI",
                  r"\mathrm{GCI} = "
                  r"\frac{F_s\left|"
                  r"\frac{f_2-f_1}{f_1}"
                  r"\right|}{r^{p_{obs}}-1}, "
                  r"\quad F_s = 1{,}25",
                  "**Amaliy javob.** "
                  "Xavfsizlik koeffitsienti "
                  "bilan xatolik "
                  "chegarasi — ekspert "
                  "so'ragan raqam."),
                d("12. GCI ning "
                  "ishonchliligi",
                  r"\mathrm{GCI} \ge "
                  r"\text{haqiqiy xato}",
                  "**O'lchangan natija.** "
                  "Kodda beshta "
                  "holatda ham GCI "
                  "haqiqiy xatoni qamrab "
                  "oldi — $F_s = 1{,}25$ "
                  "yetarli zaxira "
                  "beradi."),
                d("13. Superkonvergensiya "
                  "tuzog'i",
                  r"\text{tugundagi } u: \ "
                  r"e \approx 0 "
                  r"\;\Longrightarrow\; "
                  r"\text{Richardson "
                  r"ISHLAMAYDI}",
                  "**Nozik joy.** su-13 "
                  "dagi nodal aniqlik "
                  "tufayli tugundagi "
                  "ko'chish xatosi "
                  "mashina noli — "
                  "ekstrapolyatsiya "
                  "shovqinni "
                  "differensiallaydi. "
                  "Qiziqish kattaligini "
                  "ehtiyotkorlik bilan "
                  "tanlang."),
                d("14. Validatsiya — "
                  "boshqa masala",
                  r"E = S - D, \qquad "
                  r"u_{val} = \sqrt{u_{num}^2 "
                  r"+ u_{inp}^2 + u_D^2}",
                  "$S$ — hisob, $D$ — "
                  "tajriba. Validatsiya "
                  "noaniqligi uchta "
                  "manbadan yig'iladi va "
                  "u **hech qachon** "
                  "nolga tushmaydi."),
            ],
            meaning=(
                "V&V ning butun tuzilishi "
                "1-qadamdagi farqqa "
                "asoslanadi va bu farq "
                "amalda doimo "
                "chalkashtiriladi. "
                "Verifikatsiya — "
                "tenglamalarni to'g'ri "
                "yechyapmizmi degan sof "
                "matematik savol; unga "
                "javob berish uchun "
                "tajriba kerak emas, "
                "faqat kompyuter kerak. "
                "Validatsiya esa "
                "to'g'ri tenglamalarni "
                "yechyapmizmi degan fizik "
                "savol va unga faqat "
                "tajriba javob beradi. "
                "su-21 dagi teshikli "
                "plastina misolida buni "
                "ko'rgan edik: to'rni "
                "zichlashtirish "
                "diskretlashtirish "
                "xatosini kamaytiradi, "
                "lekin chekli kenglik "
                "modelining xatosini "
                "emas. 2-qadamdagi MMS "
                "g'oyasi oddiy, lekin "
                "kuchli. Odatda manba "
                "berilgan va yechim "
                "izlanadi; MMS da "
                "aksincha — yechim "
                "tanlanadi va manba "
                "undan chiqariladi. "
                "Natijada aniq javob "
                "har doim ma'lum "
                "bo'ladi va uni "
                "istalgan murakkab "
                "operator uchun "
                "qurish mumkin. "
                "Shuning uchun MMS "
                "kod verifikatsiyasining "
                "oltin standarti. "
                "Uning haqiqiy "
                "qimmati esa "
                "6- va 7-qadamlarda. "
                "Kod noto'g'ri "
                "javob berib, ayni "
                "paytda ishonarli "
                "ko'rinishi mumkin — "
                "bu eng xavfli hol. "
                "Kodda ataylab "
                "kiritilgan xato "
                "aynan shunday: yuk "
                "vektori teng "
                "bo'lingan variant "
                "yaqinlashadi, "
                "natija silliq va "
                "mantiqiy, lekin "
                "tartib 3 o'rniga "
                "2. Faqat tartib "
                "o'lchovi buni "
                "ochadi — hech "
                "qanday 'ko'z bilan "
                "tekshirish' "
                "yordam bermaydi. "
                "Ikkinchi ataylab "
                "kiritilgan xato "
                "esa qo'polroq: "
                "tartib nolga "
                "tushadi va xato "
                "to'r "
                "zichlashganda "
                "umuman "
                "o'zgarmaydi. "
                "8–12-qadamlar "
                "esa ekspertning "
                "savoliga raqam "
                "bilan javob "
                "beradi. Uchta "
                "to'rdan "
                "kuzatilgan "
                "tartib, "
                "Richardson "
                "ekstrapolyatsiyasi "
                "va GCI "
                "hisoblanadi — "
                "aniq yechimni "
                "bilmasdan. "
                "Kodda GCI "
                "beshta holatda "
                "ham haqiqiy "
                "xatoni qamrab "
                "oldi. "
                "13-qadam esa "
                "muhim "
                "ogohlantirish: "
                "qiziqish "
                "kattaligini "
                "noto'g'ri "
                "tanlasangiz "
                "butun tartib "
                "yiqiladi. "
                "Tugundagi "
                "ko'chish su-13 "
                "dagi "
                "superkonvergensiya "
                "tufayli aynan "
                "to'g'ri, demak "
                "Richardson "
                "shovqinni "
                "ekstrapolyatsiya "
                "qiladi va "
                "ma'nosiz tartib "
                "beradi."
            ),
            equations=[
                eq(r"u_{ex} \ \text{tanlanadi}, "
                   r"\quad f = \mathcal{L}u_{ex} "
                   r"\;\Longrightarrow\; "
                   r"p_{obs} \overset{?}{=} "
                   r"p_{nazariy}",
                   "Ishlab chiqilgan yechimlar "
                   "usuli — kod "
                   "verifikatsiyasi.", "MMS"),
                eq(r"p_{obs} = \frac{\ln\left|"
                   r"(f_3-f_2)/(f_2-f_1)\right|}"
                   r"{\ln r}",
                   "Uchta to'rdan kuzatilgan "
                   "tartib — aniq yechim "
                   "kerak emas.",
                   "Kuzatilgan tartib"),
                eq(r"f_{ext} = f_1 + "
                   r"\frac{f_1-f_2}"
                   r"{r^{p_{obs}}-1}",
                   "Richardson "
                   "ekstrapolyatsiyasi "
                   "(su-07).", "Ekstrapolyatsiya"),
                eq(r"\mathrm{GCI} = \frac{1{,}25\,"
                   r"\left|(f_2-f_1)/f_1\right|}"
                   r"{r^{p_{obs}}-1}",
                   "To'r yaqinlashish indeksi "
                   "— hisobotga "
                   "yoziladigan raqam.",
                   "GCI"),
            ],
            conditions=(
                "**MMS uchun $u_{ex}$ "
                "tanlash:**\n"
                "1. Silliq va analitik "
                "differensiallanadigan;\n"
                "2. Operatorning **barcha** "
                "hadlarini faollashtirsin "
                "— aks holda xato "
                "yashirin qoladi;\n"
                "3. Hech bir hosilasi "
                "aynan nol bo'lmasin;\n"
                "4. Chegaraviy shartlarni "
                "qanoatlantirsin (yoki "
                "ularni ham "
                "'ishlab chiqing').\n\n"
                "**Tartib o'lchovi "
                "ishonchli bo'lishi "
                "uchun:**\n"
                "- To'rlar **asimptotik "
                "sohada** bo'lsin — "
                "dag'al to'rda tartib "
                "ma'nosiz;\n"
                "- Kamida uchta to'r;\n"
                "- Yaxlitlash xatosi "
                "diskretlashtirish "
                "xatosidan ancha kichik "
                "bo'lsin (su-02).\n\n"
                "**GCI hisobotida "
                "ko'rsatilsin:**\n"
                "1. Uchta to'rning "
                "o'lchamlari va "
                "$r$;\n"
                "2. Qiziqish kattaligi "
                "va uning uchta "
                "qiymati;\n"
                "3. $p_{obs}$ va u "
                "nazariyga mos "
                "kelishi;\n"
                "4. GCI foizda.\n\n"
                "**Qiziqish kattaligini "
                "tanlash:** "
                "superkonvergent "
                "nuqtalardan "
                "**qoching** — "
                "tugundagi ko'chish, "
                "Barlou nuqtasidagi "
                "kuchlanish. Ular "
                "haqiqiy xatoni "
                "yashiradi.\n\n"
                "**Validatsiya "
                "alohida:** "
                "verifikatsiyasiz "
                "validatsiya "
                "ma'nosiz — "
                "tajriba bilan "
                "mos kelish "
                "ikkita xatoning "
                "bir-birini "
                "qoplashi bo'lishi "
                "mumkin."
            ),
            worked=WorkedExample(
                statement=(
                    "Uchta to'rda oqim "
                    "hisoblandi: "
                    "$f_3 = 0{,}9880$ "
                    "($n = 16$), "
                    "$f_2 = 0{,}9970$ "
                    "($n = 32$), "
                    "$f_1 = 0{,}99925$ "
                    "($n = 64$). "
                    "(a) Kuzatilgan tartibni "
                    "toping; (b) Richardson "
                    "ekstrapolyatsiyasini "
                    "hisoblang; (c) GCI ni "
                    "aniqlang."
                ),
                given=[
                    r"r = 2, \quad F_s = 1{,}25",
                    r"f_1 = 0{,}99925,\ f_2 = "
                    r"0{,}9970,\ f_3 = 0{,}9880",
                ],
                steps=[
                    st(r"f_2 - f_1 = 0{,}9970 - "
                       r"0{,}99925 = -0{,}00225",
                       "Zich to'rlar farqi."),
                    st(r"f_3 - f_2 = 0{,}9880 - "
                       r"0{,}9970 = -0{,}0090",
                       "Dag'al to'rlar farqi."),
                    st(r"\frac{f_3-f_2}{f_2-f_1} = "
                       r"\frac{-0{,}0090}"
                       r"{-0{,}00225} = 4{,}00",
                       "Nisbat — u tartibni "
                       "beradi."),
                    st(r"p_{obs} = "
                       r"\frac{\ln 4{,}00}"
                       r"{\ln 2} = "
                       r"\frac{1{,}3863}"
                       r"{0{,}6931} = 2{,}00",
                       "**Ikkinchi tartib** — "
                       "$p = 2$ element "
                       "uchun oqimda "
                       "kutilgan qiymat."),
                    st(r"\text{(b)}\quad "
                       r"r^{p_{obs}} - 1 = "
                       r"2^2 - 1 = 3",
                       "Maxraj."),
                    st(r"f_{ext} = f_1 + "
                       r"\frac{f_1 - f_2}{3} = "
                       r"0{,}99925 + "
                       r"\frac{0{,}00225}{3}",
                       "Ekstrapolyatsiya "
                       "formulasi."),
                    st(r"= 0{,}99925 + "
                       r"0{,}00075 = 1{,}0000",
                       "**Aniq qiymatga "
                       "juda yaqin** — "
                       "eng zich to'rdan "
                       "ancha yaxshi."),
                    st(r"\text{(c)}\quad "
                       r"\left|\frac{f_2-f_1}"
                       r"{f_1}\right| = "
                       r"\frac{0{,}00225}"
                       r"{0{,}99925} = "
                       r"0{,}002252",
                       "Nisbiy farq."),
                    st(r"\mathrm{GCI} = "
                       r"\frac{1{,}25 \cdot "
                       r"0{,}002252}{3} = "
                       r"0{,}000938",
                       "GCI formulasi."),
                    st(r"\mathrm{GCI} = "
                       r"0{,}094\%",
                       "**Hisobotga "
                       "yoziladigan raqam.**"),
                    st(r"\text{haqiqiy xato} = "
                       r"\frac{|0{,}99925 - 1|}"
                       r"{1} = 0{,}075\%",
                       "Bu misolda aniq "
                       "javob ma'lum edi."),
                    st(r"0{,}094\% > 0{,}075\% "
                       r"\quad \checkmark",
                       "**GCI haqiqiy xatoni "
                       "qamrab oldi** — "
                       "$F_s = 1{,}25$ "
                       "zaxirasi ishladi."),
                ],
                answer=(
                    "(a) $p_{obs} = 2{,}00$ — "
                    "nazariy qiymatga mos, "
                    "demak kod va to'rlar "
                    "asimptotik sohada; "
                    "(b) $f_{ext} = "
                    "1{,}0000$; "
                    "(c) $\\mathrm{GCI} = "
                    "0{,}094\\%$ va u "
                    "haqiqiy 0,075% "
                    "xatoni qamrab oladi. "
                    "Kod bu tartibni "
                    "beshta to'rlar "
                    "uchligida ham "
                    "takrorlaydi va "
                    "GCI har safar "
                    "haqiqiy xatodan "
                    "katta chiqadi."
                ),
                engineering_note=(
                    "(a) qismidagi "
                    "tekshiruv eng ko'p "
                    "o'tkazib "
                    "yuboriladigan, "
                    "lekin eng muhim "
                    "qadam. "
                    "$p_{obs}$ nazariy "
                    "qiymatga mos "
                    "kelmasa, GCI "
                    "**ma'nosiz** — "
                    "chunki uning "
                    "butun asosi "
                    "xatoning "
                    "$Ch^p$ "
                    "ko'rinishida "
                    "bo'lishi. "
                    "Amalda "
                    "$p_{obs}$ mos "
                    "kelmasligining "
                    "uchta sababi "
                    "bor: to'rlar "
                    "hali asimptotik "
                    "sohada emas "
                    "(eng keng "
                    "tarqalgani), "
                    "kodda xato bor, "
                    "yoki qiziqish "
                    "kattaligi "
                    "superkonvergent "
                    "nuqtada "
                    "olingan. "
                    "Uchinchisi "
                    "ayniqsa "
                    "yashirin: kodda "
                    "tugundagi "
                    "ko'chishni "
                    "tanlaganimizda "
                    "xato mashina "
                    "noliga teng "
                    "chiqdi va "
                    "Richardson "
                    "shovqinni "
                    "ekstrapolyatsiya "
                    "qildi, natijada "
                    "$p_{obs}$ "
                    "manfiy va "
                    "ma'nosiz "
                    "bo'ldi. "
                    "Shuning uchun "
                    "qiziqish "
                    "kattaligini "
                    "tanlashda "
                    "ehtiyot "
                    "bo'ling: "
                    "oqim, maksimal "
                    "kuchlanish yoki "
                    "integral "
                    "kattalik — "
                    "lekin "
                    "superkonvergent "
                    "nuqtadagi "
                    "qiymat emas."
                ),
            ),
            computation=Computation(
                caption=(
                    "MMS bilan kodni "
                    "verifikatsiya qilish, "
                    "ataylab kiritilgan "
                    "xatolarni aniqlash va GCI "
                    "bilan xatolik chegarasini "
                    "qurish."
                ),
                code='''"""Verifikatsiya va validatsiya (V&V)."""
import numpy as np
from labkit import PARAMS, note, series, table, value
from numpy.polynomial.legendre import leggauss

p_ord = int(PARAMS.get("p_ord", 2))
n_base = int(PARAMS.get("n_base", 16))
x_qoi = float(PARAMS.get("x_qoi", 0.5))

EA = 1.0

# --- ISHLAB CHIQILGAN YECHIM: uni TANLAYMIZ ---
# u_ex = sin(pi x) (1 + x^2) - silliq, chegarada nol, barcha hadlar faol


def u_ex(x):
    return np.sin(np.pi*x)*(1 + x**2)


def du_ex(x):
    return np.pi*np.cos(np.pi*x)*(1 + x**2) + np.sin(np.pi*x)*2*x


def d2u_ex(x):
    return (-np.pi**2*np.sin(np.pi*x)*(1 + x**2)
            + 4*np.pi*np.cos(np.pi*x)*x + 2*np.sin(np.pi*x))


def f_src(x):
    """Manba ANIQ YECHIMDAN chiqariladi - MMS ning mohiyati."""
    return -EA*d2u_ex(x)


# manba to'g'ri chiqarilganini tekshiramiz
xt = np.linspace(0.05, 0.95, 19)
num_d2 = (u_ex(xt + 1e-5) - 2*u_ex(xt) + u_ex(xt - 1e-5))/1e-10
value("Manba tekshiruvi: analitik va sonli d2u farqi",
      float(np.max(np.abs(d2u_ex(xt) - num_d2))), "—")
value("u_ex(0) chegaraviy shart", float(u_ex(0.0)), "—")
value("u_ex(1) chegaraviy shart", float(u_ex(1.0)), "—")


def lag(xi, nd):
    m = len(nd)
    xi = np.atleast_1d(np.asarray(xi, dtype=float))
    N = np.ones((m,) + xi.shape)
    dN = np.zeros((m,) + xi.shape)
    for i in range(m):
        for j in range(m):
            if j != i:
                N[i] *= (xi - nd[j])/(nd[i] - nd[j])
        for j in range(m):
            if j != i:
                t = np.ones_like(xi)
                for k in range(m):
                    if k != i and k != j:
                        t *= (xi - nd[k])/(nd[i] - nd[k])
                dN[i] += t/(nd[i] - nd[j])
    return N, dN


def fem(n, p=2, bug="none"):
    h = 1.0/n
    nodes = np.linspace(-1.0, 1.0, p + 1)
    gx, gw = leggauss(p + 3)
    N_, dN_ = lag(gx, nodes)
    nd_ = n*p + 1
    K = np.zeros((nd_, nd_))
    F = np.zeros(nd_)
    J = h/2
    Jb = h if bug == "jac" else J          # XATO: Yakobian h/2 emas, h
    for e in range(n):
        idx = np.arange(e*p, e*p + p + 1)
        xg = e*h + h/2*(1 + gx)
        for qq in range(len(gx)):
            B = dN_[:, qq]/Jb
            K[np.ix_(idx, idx)] += EA*np.outer(B, B)*gw[qq]*J
            if bug != "load":
                F[idx] += f_src(xg[qq])*N_[:, qq]*gw[qq]*J
        if bug == "load":                  # XATO: yukni teng bo'lish
            tot = float(np.sum(f_src(xg)*gw)*J)
            F[idx] += tot/(p + 1)
    u = np.zeros(nd_)
    free = np.arange(1, nd_ - 1)
    u[free] = np.linalg.solve(K[np.ix_(free, free)], F[free])
    return u, h, nodes


def norms(n, p=2, bug="none"):
    u, h, nodes = fem(n, p, bug)
    gx2, gw2 = leggauss(p + 5)
    N2, dN2 = lag(gx2, nodes)
    J = h/2
    l2 = 0.0
    en = 0.0
    for e in range(n):
        idx = np.arange(e*p, e*p + p + 1)
        xg = e*h + h/2*(1 + gx2)
        uh = np.sum(N2*u[idx][:, None], axis=0)
        eh = np.sum((dN2/J)*u[idx][:, None], axis=0)
        l2 += float(np.sum((uh - u_ex(xg))**2*gw2)*J)
        en += EA*float(np.sum((eh - du_ex(xg))**2*gw2)*J)
    return np.sqrt(l2), np.sqrt(en)


# --- (1) KOD VERIFIKATSIYASI: tartib nazariyga mos keladimi? ---
rows = []
for p in [1, 2, 3]:
    prev = None
    for n in [4, 8, 16, 32, 64]:
        l2, en = norms(n, p)
        if prev is None:
            rows.append([p, n, f"{l2:.4e}", "—", f"{en:.4e}", "—",
                         p + 1, p])
        else:
            r1 = np.log(prev[0]/l2)/np.log(2)
            r2 = np.log(prev[1]/en)/np.log(2)
            rows.append([p, n, f"{l2:.4e}", f"{r1:.3f}", f"{en:.4e}",
                         f"{r2:.3f}", p + 1, p])
        prev = (l2, en)
table("MMS: o'lchangan tartib nazariyga mos keladimi?",
      ["p", "n", "L2 normasi", "L2 tartibi", "energiya normasi",
       "energiya tartibi", "nazariy L2", "nazariy energiya"], rows)
for p in [1, 2, 3]:
    a, _ = norms(32, p)
    b, _ = norms(64, p)
    value(f"p = {p}: o'lchangan L2 tartibi (32 -> 64)",
          float(np.log(a/b)/np.log(2)), "—")
note("KOD VERIFIKATSIYASI BAJARILDI. Uchala tartib uchun ham "
     "o'lchangan yaqinlashish tartibi nazariy qiymatga (L2 da p+1, "
     "energiyada p) uch-to'rt xonali aniqlikda mos keldi. Bu MMS "
     "ning asosiy natijasi: manba ANIQ YECHIMDAN chiqarilgani uchun "
     "aniq javob har doim ma'lum va tartibni to'g'ridan-to'g'ri "
     "o'lchash mumkin. Hech qanday tajriba yoki adabiyot qiymati "
     "kerak emas.")

# --- (2) MMS ATAYLAB KIRITILGAN XATONI TOPADIMI? ---
rows2 = []
for bug, nm in [("none", "xatosiz kod"),
                ("load", "yuk vektori teng bo'lingan"),
                ("jac", "Yakobian h/2 o'rniga h")]:
    prev = None
    line = [nm]
    rates = []
    for n in [8, 16, 32, 64, 128]:
        l2, _ = norms(n, 2, bug)
        if prev is not None:
            rates.append(np.log(prev/l2)/np.log(2))
        prev = l2
    line += [f"{r:+.3f}" for r in rates]
    rows2.append(line)
table("MMS ataylab kiritilgan xatoni topadimi? (p = 2, nazariy 3)",
      ["kod holati", "8->16", "16->32", "32->64", "64->128"], rows2)
e_clean = [norms(n, 2, "none")[0] for n in [8, 16, 32, 64, 128]]
e_load = [norms(n, 2, "load")[0] for n in [8, 16, 32, 64, 128]]
e_jac = [norms(n, 2, "jac")[0] for n in [8, 16, 32, 64, 128]]
series("Xatosiz kod", [8, 16, 32, 64, 128],
       [np.log10(v) for v in e_clean],
       xlabel="elementlar", ylabel="log10(L2 xatosi)")
series("Yuk vektori xatosi", [8, 16, 32, 64, 128],
       [np.log10(v) for v in e_load],
       xlabel="elementlar", ylabel="log10(L2 xatosi)")
series("Yakobian xatosi", [8, 16, 32, 64, 128],
       [np.log10(v) for v in e_jac],
       xlabel="elementlar", ylabel="log10(L2 xatosi)")
value("Yuk xatosi bilan: 128 elementdagi xato", float(e_load[-1]), "—")
value("Xatosiz kod: 128 elementdagi xato", float(e_clean[-1]), "—")
value("Farq necha barobar", float(e_load[-1]/e_clean[-1]), "barobar")
note("MMS NING HAQIQIY QIYMATI SHU YERDA. Yuk vektorini teng bo'lish "
     "xatosi kodni BUZMAYDI: natija baribir yaqinlashadi, silliq va "
     "mantiqiy ko'rinadi. Faqat tartib 3 o'rniga 2 bo'lib qoladi va "
     "buni faqat o'lchov ochadi - hech qanday 'ko'z bilan tekshirish' "
     "yordam bermaydi. Yakobian xatosi esa qo'polroq: tartib NOLGA "
     "tushadi va xato to'r zichlashganda umuman o'zgarmaydi. Demak "
     "tartib o'lchovi ikkala turdagi xatoni ham aniqlaydi.")

# --- (3) YECHIM VERIFIKATSIYASI: aniq javob NOMA'LUM deb ---
def qoi_flux(n, p=2, xq=0.5):
    """Oqim EA*u'(xq) - superkonvergent EMAS."""
    u, h, nodes = fem(n, p)
    e = min(int(xq/h), n - 1)
    xi = 2*(xq - e*h)/h - 1
    idx = np.arange(e*p, e*p + p + 1)
    _, dNq = lag(np.array([xi]), nodes)
    return float(EA*np.sum(dNq[:, 0]/(h/2)*u[idx]))


def qoi_disp(n, p=2):
    """Tugundagi ko'chish - SUPERKONVERGENT (su-13)."""
    u, h, nodes = fem(n, p)
    return float(u[(n*p + 1)//2])


ex_flux = du_ex(x_qoi)
value("Aniq oqim EA*u'(x)", float(ex_flux), "—")
rows3 = []
r_ref = 2.0
for n1 in [4, 8, 16, 32, 64]:
    f3, f2, f1 = (qoi_flux(n1, 2, x_qoi), qoi_flux(2*n1, 2, x_qoi),
                  qoi_flux(4*n1, 2, x_qoi))
    e21, e32 = f2 - f1, f3 - f2
    pobs = np.log(abs(e32/e21))/np.log(r_ref)
    fext = f1 + (f1 - f2)/(r_ref**pobs - 1)
    gci = 1.25*abs((f2 - f1)/f1)/(r_ref**pobs - 1)
    real = abs(f1 - ex_flux)/abs(ex_flux)
    rows3.append([f"{n1}/{2*n1}/{4*n1}", f"{pobs:.4f}", f"{fext:.8f}",
                  f"{gci*100:.4f}", f"{real*100:.5f}",
                  "HA" if gci >= real else "YO'Q"])
table("Yechim verifikatsiyasi: GCI (aniq yechim ishlatilmaydi)",
      ["to'rlar uchligi", "p_kuzatilgan", "ekstrapolyatsiya", "GCI %",
       "haqiqiy xato %", "GCI qamradimi"], rows3)
note("GCI beshta holatda ham haqiqiy xatoni QAMRAB oldi va kuzatilgan "
     "tartib nazariy 2 ga yaqinlashdi (1.81 -> 1.999). DIQQAT: bu "
     "hisobda ANIQ YECHIM UMUMAN ISHLATILMADI - faqat uchta to'rdagi "
     "natija. Aynan shuning uchun GCI haqiqiy masalalarda ishlaydi, "
     "u yerda aniq yechim yo'q. Xavfsizlik koeffitsienti Fs = 1.25 "
     "zaxira beradi, lekin u kafolat emas: asimptotik sohada "
     "bo'lmasangiz GCI ham ishonchsiz.")

rows4 = []
for n1 in [8, 16, 32]:
    f3, f2, f1 = (qoi_flux(n1, 2, x_qoi), qoi_flux(2*n1, 2, x_qoi),
                  qoi_flux(4*n1, 2, x_qoi))
    pobs = np.log(abs((f3 - f2)/(f2 - f1)))/np.log(r_ref)
    fext = f1 + (f1 - f2)/(r_ref**pobs - 1)
    e_fine = abs(f1 - ex_flux)/abs(ex_flux)
    e_ext = abs(fext - ex_flux)/abs(ex_flux)
    rows4.append([4*n1, f"{e_fine*100:.6f}", f"{e_ext*100:.6f}",
                  f"{e_fine/max(e_ext, 1e-18):.1f}"])
table("Richardson ekstrapolyatsiyasi qancha yutuq beradi?",
      ["eng zich to'r", "uning xatosi %", "ekstrapolyatsiya xatosi %",
       "necha barobar yaxshi"], rows4)
note("Richardson ekstrapolyatsiyasi eng zich to'rdan 30 dan 437 "
     "barobargacha aniqroq natija beradi - va bu BEPUL, chunki uchta "
     "hisob allaqachon bajarilgan. Bu su-07 dagi ekstrapolyatsiyaning "
     "aynan o'zi, faqat endi to'r bo'yicha.")

# --- (4) SUPERKONVERGENSIYA TUZOG'I ---
rows5 = []
for n1 in [4, 8, 16]:
    d3, d2_, d1 = (qoi_disp(n1), qoi_disp(2*n1), qoi_disp(4*n1))
    e21, e32 = d2_ - d1, d3 - d2_
    if abs(e21) < 1e-16:
        pobs_s = float("nan")
    else:
        pobs_s = np.log(abs(e32/e21) + 1e-300)/np.log(r_ref)
    rows5.append([f"{n1}/{2*n1}/{4*n1}", f"{d1:.12f}",
                  f"{abs(e21):.3e}",
                  "aniqlanmaydi" if not np.isfinite(pobs_s)
                  else f"{pobs_s:.3f}"])
table("TUZOQ: qiziqish kattaligi superkonvergent nuqtada olinsa",
      ["to'rlar uchligi", "tugundagi u", "to'rlar farqi", "p_kuzatilgan"],
      rows5)
value("Tugundagi ko'chish xatosi (n = 64)",
      float(abs(qoi_disp(64) - u_ex(x_qoi))), "—")
value("Oqim xatosi (n = 64)",
      float(abs(qoi_flux(64, 2, x_qoi) - ex_flux)), "—")
note("MUHIM TUZOQ. Tugundagi ko'chish su-13 dagi bir o'lchovli "
     "superkonvergensiya tufayli MASHINA ANIQLIGIDA to'g'ri. "
     "Natijada to'rlar orasidagi farq shovqin darajasida qoladi va "
     "Richardson ekstrapolyatsiyasi SHOVQINNI ekstrapolyatsiya "
     "qiladi - kuzatilgan tartib ma'nosiz chiqadi. Shuning uchun "
     "qiziqish kattaligini tanlashda superkonvergent nuqtalardan "
     "qochish kerak: oqim, maksimal kuchlanish yoki integral "
     "kattalik oling, tugundagi ko'chishni emas.")

table("Verifikatsiya va validatsiya: tuzilma",
      ["Bosqich", "Savol", "Vosita", "Nima kerak"],
      [["Kod verifikatsiyasi", "Dasturda xato bormi?",
        "MMS, tartib o'lchovi", "faqat kompyuter"],
       ["Yechim verifikatsiyasi", "Diskretlashtirish xatosi qancha?",
        "Richardson, GCI", "uchta to'r"],
       ["Validatsiya", "Model haqiqatga mos keladimi?",
        "tajriba bilan taqqoslash", "TAJRIBA"],
       ["Noaniqlik tahlili", "Kirish ma'lumotlari qanchalik aniq?",
        "sezgirlik, Monte-Karlo", "statistika"]])
''',
                parameters=[
                    p("p_ord", "Element tartibi", 1.0, 3.0, 2.0, 1.0),
                    p("n_base", "Boshlang'ich to'r", 4.0, 64.0, 16.0,
                      4.0),
                    p("x_qoi", "Qiziqish nuqtasi", 0.1, 0.9, 0.5, 0.05),
                ],
                expected_output=(
                    "MMS uchala element "
                    "tartibi uchun ham "
                    "o'lchangan "
                    "yaqinlashish tartibini "
                    "nazariy qiymatga "
                    "($L^2$ da $p+1$, "
                    "energiyada $p$) "
                    "uch-to'rt xonali "
                    "aniqlikda "
                    "tasdiqlaydi. Ataylab "
                    "kiritilgan yuk "
                    "vektori xatosi "
                    "kodni buzmaydi — "
                    "natija baribir "
                    "yaqinlashadi — "
                    "lekin tartib 3 "
                    "o'rniga 2 bo'lib "
                    "qoladi; Yakobian "
                    "xatosida esa tartib "
                    "nolga tushadi. "
                    "Yechim "
                    "verifikatsiyasida "
                    "kuzatilgan tartib "
                    "1,81 dan 1,999 ga "
                    "yaqinlashadi va GCI "
                    "beshta holatda ham "
                    "haqiqiy xatoni "
                    "qamrab oladi, "
                    "aniq yechim "
                    "umuman "
                    "ishlatilmagan "
                    "holda. Richardson "
                    "ekstrapolyatsiyasi "
                    "eng zich to'rdan "
                    "30–437 barobar "
                    "aniqroq. "
                    "Superkonvergent "
                    "nuqtadagi "
                    "kattalik esa "
                    "tartib o'lchovini "
                    "buzadi."
                ),
            ),
            visual=vis(
                kind="Yaqinlashish tartibi va GCI tasmasi",
                tool="React/SVG + Manim",
                description=(
                    "Log–log yaqinlashish "
                    "grafigi, tartib o'lchovi "
                    "va GCI ishonch tasmasi."
                ),
                how_to_draw=(
                    "React/SVG: asosiy panel — "
                    "log–log grafik, unda "
                    "uchta chiziq: xatosiz "
                    "kod (qiyaligi 3), yuk "
                    "vektori xatosi bilan "
                    "(qiyaligi 2) va "
                    "Yakobian xatosi bilan "
                    "(**yotiq**, qiyaligi "
                    "0). Yonida nazariy "
                    "qiyalikni ko'rsatuvchi "
                    "uchburchak "
                    "chiziladi va har bir "
                    "chiziqning "
                    "o'lchangan qiyaligi "
                    "yozib qo'yiladi. "
                    "Asosiy g'oya shu "
                    "yerda ko'rinadi: "
                    "xato chiziqlari "
                    "**parallel emas** va "
                    "aynan shu farq "
                    "xatoni ochadi. "
                    "Pastki panelda "
                    "yechim "
                    "verifikatsiyasi: "
                    "uchta to'rdagi "
                    "qiziqish kattaligi "
                    "nuqta sifatida "
                    "qo'yiladi, "
                    "Richardson "
                    "ekstrapolyatsiyasi "
                    "gorizontal chiziq "
                    "bilan, GCI esa "
                    "uning atrofidagi "
                    "**tasma** bilan "
                    "ko'rsatiladi. "
                    "Aniq qiymat "
                    "(bu sinov "
                    "masalasida "
                    "ma'lum) alohida "
                    "belgilanadi va u "
                    "tasma ichiga "
                    "tushishi "
                    "ko'rinadi. To'r "
                    "qo'shilganda "
                    "tasma torayadi. "
                    "Yon tomonda "
                    "'superkonvergent "
                    "kattalikni tanlash' "
                    "tugmasi bor: "
                    "bosilganda "
                    "nuqtalar "
                    "ustma-ust tushadi "
                    "va tasma "
                    "ma'nosiz "
                    "bo'lib qoladi."
                ),
            ),
            interp=(
                "MMS ning birinchi jadvali "
                "kod verifikatsiyasining "
                "to'liq namunasi: uchta "
                "element tartibi uchun ham "
                "o'lchangan yaqinlashish "
                "nazariy qiymatga uch-to'rt "
                "xonali aniqlikda mos "
                "keldi. Buning uchun na "
                "tajriba, na adabiyot "
                "qiymati, na boshqa kod "
                "kerak bo'ldi — faqat "
                "yechimni tanlab, manbani "
                "undan chiqarish kifoya. "
                "Ammo mavzuning eng "
                "qimmatli qismi ikkinchi "
                "jadval. Yuk vektorini "
                "teng bo'lish xatosi kodni "
                "buzmaydi: natija "
                "yaqinlashadi, silliq va "
                "mantiqiy ko'rinadi, "
                "muvozanat ham saqlanadi "
                "(su-15). Bu xatoni "
                "'natijaga qarab' aniqlash "
                "mumkin emas. Faqat tartib "
                "o'lchovi uni ochadi: 3 "
                "o'rniga 2. Yakobian xatosi "
                "esa qo'polroq va tartib "
                "nolga tushadi — xato to'r "
                "zichlashganda umuman "
                "o'zgarmaydi. Demak bitta "
                "o'lchov ikkala turdagi "
                "xatoni ham aniqlaydi va "
                "aynan shu MMS ni oltin "
                "standart qiladi. Yechim "
                "verifikatsiyasi qismida "
                "esa eng muhimi — aniq "
                "yechim **umuman "
                "ishlatilmagani**. GCI "
                "faqat uchta to'rdagi "
                "natijadan quriladi va "
                "shuning uchun haqiqiy "
                "masalalarda ham "
                "ishlaydi. Beshta "
                "holatda ham u haqiqiy "
                "xatoni qamrab oldi, "
                "kuzatilgan tartib esa "
                "1,81 dan 1,999 ga "
                "yaqinlashdi — bu "
                "to'rlar asimptotik "
                "sohaga kirganining "
                "belgisi. Richardson "
                "ekstrapolyatsiyasi "
                "qo'shimcha 30–437 "
                "barobar aniqlik "
                "beradi va bu bepul, "
                "chunki hisoblar "
                "allaqachon "
                "bajarilgan. Oxirgi "
                "jadval esa "
                "ogohlantirish. "
                "Tugundagi ko'chishni "
                "qiziqish kattaligi "
                "sifatida tanlasak, "
                "su-13 dagi "
                "superkonvergensiya "
                "tufayli xato mashina "
                "noliga teng chiqadi, "
                "to'rlar orasidagi "
                "farq shovqin "
                "darajasida qoladi va "
                "Richardson shovqinni "
                "ekstrapolyatsiya "
                "qiladi. Natijada "
                "kuzatilgan tartib "
                "ma'nosiz bo'ladi. "
                "Bu nozik, lekin "
                "amalda uchraydigan "
                "tuzoq va u "
                "kursdagi oldingi "
                "natija — "
                "superkonvergensiya — "
                "bu yerda "
                "kamchilikka "
                "aylanganini "
                "ko'rsatadi."
            ),
            mistakes=[
                "Verifikatsiya va "
                "validatsiyani "
                "adashtirish. Birinchisi "
                "matematik, ikkinchisi "
                "fizik savol.",
                "Tajriba bilan mos "
                "kelishni "
                "verifikatsiya o'rniga "
                "qabul qilish. Ikkita "
                "xato bir-birini "
                "qoplashi mumkin.",
                "$p_{obs}$ ni "
                "tekshirmasdan GCI "
                "hisoblash. Tartib mos "
                "kelmasa GCI "
                "ma'nosiz.",
                "Asimptotik sohada "
                "bo'lmagan to'rlardan "
                "tartib o'lchash. "
                "Dag'al to'rda natija "
                "ishonchsiz.",
                "Qiziqish kattaligini "
                "superkonvergent "
                "nuqtada olish. Xato "
                "yashirin qoladi va "
                "tartib buziladi.",
                "MMS uchun juda sodda "
                "$u_{ex}$ tanlash. "
                "Agar u operatorning "
                "ba'zi hadlarini "
                "faollashtirmasa, "
                "o'sha hadlardagi "
                "xato "
                "topilmaydi.",
            ],
            quiz=[
                q("Verifikatsiya va "
                  "validatsiyaning farqi "
                  "nima?",
                  "Verifikatsiya — "
                  "tenglamalarni to'g'ri "
                  "yechyapmizmi (matematik, "
                  "tajribasiz); "
                  "validatsiya — to'g'ri "
                  "tenglamalarni "
                  "yechyapmizmi (fizik, "
                  "tajriba kerak).",
                  "konseptual"),
                q("MMS ning asosiy g'oyasi "
                  "nima?",
                  "Yechim **tanlanadi**, "
                  "manba esa undan "
                  "chiqariladi — shunda "
                  "aniq javob har doim "
                  "ma'lum va tartibni "
                  "o'lchash mumkin.",
                  "konseptual"),
                q("$f_1 = 0{,}99925$, "
                  "$f_2 = 0{,}9970$, "
                  "$f_3 = 0{,}9880$, "
                  "$r = 2$. GCI nechaga "
                  "teng?",
                  "$p_{obs} = \\ln 4/"
                  "\\ln 2 = 2$; "
                  "$\\mathrm{GCI} = "
                  "1{,}25\\cdot"
                  "0{,}002252/3 = "
                  "0{,}094\\%$.", "hisob"),
                q("Kodda ataylab kiritilgan "
                  "yuk vektori xatosi "
                  "qanday namoyon "
                  "bo'ladi?",
                  "Natija baribir "
                  "yaqinlashadi va "
                  "ishonarli ko'rinadi, "
                  "lekin tartib 3 o'rniga "
                  "2 bo'lib qoladi — "
                  "faqat o'lchov buni "
                  "ochadi.", "kod"),
                q("Nima uchun tugundagi "
                  "ko'chish GCI uchun "
                  "yaroqsiz?",
                  "su-13 dagi "
                  "superkonvergensiya "
                  "tufayli xato mashina "
                  "noliga teng; Richardson "
                  "shovqinni "
                  "ekstrapolyatsiya qiladi "
                  "va tartib ma'nosiz "
                  "chiqadi.", "kod"),
                q("GCI hisoblash uchun aniq "
                  "yechim kerakmi?",
                  "Yo'q — faqat uchta "
                  "to'rdagi natija. Aynan "
                  "shuning uchun u haqiqiy "
                  "masalalarda ishlaydi.",
                  "talqin"),
                q("Richardson "
                  "ekstrapolyatsiyasi "
                  "qancha yutuq beradi?",
                  "Kodda eng zich to'rdan "
                  "30–437 barobar aniqroq, "
                  "va bu bepul — uchta "
                  "hisob allaqachon "
                  "bajarilgan.", "talqin"),
            ],
            bridge=(
                "Natijaning ishonchliligi "
                "rasmiylashtirildi. Endi "
                "oxirgi amaliy savol "
                "qoladi: bu ishonchlilikka "
                "qancha hisoblash "
                "resursi sarflanadi va "
                "uni qanday kamaytirish "
                "mumkin?"
            ),
            research=(
                "V&V ni "
                "chuqurlashtiring. "
                "(1) ASME V&V 20 "
                "standartini o'rganing: "
                "validatsiya "
                "noaniqligini "
                "$u_{val} = "
                "\\sqrt{u_{num}^2 + "
                "u_{inp}^2 + u_D^2}$ "
                "sifatida rasmiy "
                "hisoblash. "
                "(2) Chegaraviy "
                "shartlarni ham "
                "'ishlab chiqish' "
                "usulini ko'rib "
                "chiqing: "
                "$u_{ex}$ chegaraviy "
                "shartni "
                "qanoatlantirmasa "
                "nima qilish "
                "kerak? "
                "(3) Nochiziqli va "
                "vaqtga bog'liq "
                "masalalarda MMS ni "
                "o'rganing: "
                "manba endi "
                "vaqtga ham "
                "bog'liq "
                "bo'ladi. "
                "(4) Noaniqlik "
                "tarqalishini "
                "(uncertainty "
                "propagation) "
                "ko'rib chiqing: "
                "kirish "
                "ma'lumotlaridagi "
                "tarqoqlik "
                "natijaga qanday "
                "o'tadi — "
                "Monte-Karlo va "
                "polinomial xaos."
            ),
            manim_ref=manim(
                scene="VerificationScene",
                module="manim/scenes/su_modern.py",
                title="MMS va tartib o'lchovi",
                summary=(
                    "Avval MMS g'oyasi "
                    "ko'rsatiladi: yechim "
                    "tanlanadi, operator "
                    "qo'llanadi va manba "
                    "chiqadi — o'qlar "
                    "odatdagiga teskari "
                    "yo'nalishda. Keyin "
                    "log–log grafikda "
                    "uchta chiziq "
                    "chiziladi va "
                    "ularning "
                    "qiyaliklari "
                    "o'lchanadi: 3, 2 va "
                    "0. Nazariy qiyalik "
                    "uchburchagi "
                    "ustiga "
                    "qo'yilganda "
                    "faqat bittasi mos "
                    "tushadi. Oxirida "
                    "GCI tasmasi "
                    "quriladi va aniq "
                    "qiymat uning "
                    "ichiga tushishi "
                    "ko'rsatiladi."
                ),
            ),
        ),
    ),
    # ------------------------------------------------------------------ su-29
    Topic(
        id="su-29",
        subject_id=S, module_id=M, order=29,
        title="Hisoblash samaradorligi: tartiblash, xotira va usul tanlovi",
        description=(
            "Amallar sonini va xotirani baholash, tugunlarni tartiblash "
            "(RCM, AMD) va to'ldirilish, to'g'ri va iterativ usullar "
            "orasidagi tanlov, oldindan shartlash hamda o'lchangan va "
            "nazariy masshtablanishning farqi."
        ),
        learning_objective=(
            "Katta FEM tizimining narxini oldindan baholash, tartiblash "
            "va usul tanlovi orqali uni kamaytirish va tanlovni amallar "
            "hamda xotira hisobi bilan asoslash."
        ),
        prerequisites=["su-28", "su-05", "su-06", "su-15"],
        mathematical_core=(
            "Lentali yechish: $\\mathcal{O}(Nb^2)$ amal, "
            "$\\mathcal{O}(Nb)$ xotira; "
            "$b \\sim N^{1/2}$ (2D), $b \\sim N^{2/3}$ (3D). "
            "CG: $k \\le \\tfrac{1}{2}\\sqrt{\\kappa}\\,"
            "\\ln\\tfrac{2}{\\varepsilon}$, "
            "$\\kappa \\sim h^{-2}$."
        ),
        engineering_application=(
            "Sanoat FEM paketlarida yechuvchi tanlash, katta modelni "
            "mavjud xotiraga sig'dirish, parametrik tahlil va "
            "optimallashtirish uchun hisob vaqtini rejalashtirish."
        ),
        computational_component=(
            "Lenta kengligini RCM bilan kamaytirish, AMD tartiblashda "
            "to'ldirilishni o'lchash, CG iteratsiyalarini sanash, "
            "Yakobi oldindan shartlashning foydasini konstrast bo'yicha "
            "baholash va masshtablanish darajasini o'lchash."
        ),
        visualization_component=(
            "Matritsa portreti (spy) uch tartiblashda, to'ldirilish "
            "xaritasi, log-log masshtablanish grafigi nazariy qiyalik "
            "uchburchagi bilan, to'g'ri va iterativ usul narxining "
            "kesishish nuqtasi."
        ),
        research_extension=(
            "Ko'p to'rli (multigrid) usullar N ga proporsional "
            "murakkablikka erishadi va bugungi kunda eng katta 3D "
            "masalalarning asosiy yechuvchisi hisoblanadi. Tadqiqot "
            "yo'nalishlari: algebraik multigrid (AMG) ning "
            "geterogen va anizotrop masalalarga moslashuvi, domenlarga "
            "ajratish (domain decomposition) usullari va ularning "
            "parallel masshtablanishi, GPU uchun siyrak yechuvchilar, "
            "hamda matritsasiz (matrix-free) formulirovkalar — bu yerda "
            "K umuman saqlanmaydi, faqat K·v ko'paytma hisoblanadi, "
            "bu esa xotira devorini butunlay chetlab o'tadi."
        ),
        difficulty="chuqurlashtirilgan",
        previous_link=(
            "su-28 natijaning ishonchliligini rasmiylashtirdi: MMS bilan "
            "kod verifikatsiyasi, Richardson ekstrapolyatsiyasi va GCI "
            "bilan xatolik chegarasi. Lekin bu tartib to'rni bir necha "
            "marta maydalashni talab qiladi — ya'ni ishonchlilik "
            "hisoblash resursi evaziga sotib olinadi. Shu yerda tabiiy "
            "savol tug'iladi: bu resurs qanchaga tushadi va uni "
            "qanday kamaytirish mumkin? su-05 va su-06 da LU, Cholesky "
            "va CG algoritmlari alohida o'rganilgan edi, su-15 da esa "
            "yig'ish va lenta tushunchasi kiritilgan edi. Endi ular "
            "bitta muhandislik qaroriga birlashtiriladi."
        ),
        next_topic="su-30",
        estimated_minutes=100,
        tags=["samaradorlik", "tartiblash", "RCM", "AMD", "to'ldirilish",
              "oldindan shartlash", "masshtablanish"],
        lesson=_lesson(
            problem=(
                "Aviatsiya kronshteyni geksaedr elementlar bilan "
                "modellashtirilgan: 500 000 erkinlik darajasi. Muhandis "
                "uni odatdagi ish stansiyasida (32 GB operativ xotira) "
                "yechmoqchi. To'la matritsa sifatida saqlansa, K uchun "
                "$N^2 \\cdot 8 = 2{,}0$ TB kerak bo'ladi — bu mavjud "
                "xotiradan 60 baravar ko'p. Model kichraytirilsinmi, "
                "yoki boshqa yechuvchi tanlansinmi?\n\n"
                "Bu masala butun kursdagi eng amaliy savolni qo'yadi. "
                "su-13 dan su-28 gacha biz aniqlikni oshirishni "
                "o'rgandik: yuqori tartibli elementlar, adaptiv to'r, "
                "GCI bilan xatolik chegarasi. Ularning har biri N ni "
                "oshiradi. Lekin N ning o'sishi bilan narx CHIZIQLI "
                "o'smaydi: to'la yechishda u $N^3$ kabi, xotira esa "
                "$N^2$ kabi o'sadi. Shuning uchun aniqlikni oshirish "
                "muqarrar ravishda hisoblash devoriga (computational "
                "wall) urilalib qoladi.\n\n"
                "Yaxshi xabar shundaki, bu devor algoritm tanlovi bilan "
                "juda uzoqqa suriladi. Bir xil masala, bir xil "
                "kompyuter: to'la matritsa 2 TB va $8{,}3\\cdot10^{16}$ "
                "amal talab qiladi; siyrak saqlash va to'g'ri tartiblash "
                "bilan xotira 0,32 GB ga, iterativ yechuvchi bilan esa "
                "amallar $1{,}6\\cdot10^{10}$ ga tushadi. Bu amallar "
                "bo'yicha besh million baravar farq — hech qanday "
                "apparat yangilanishi bunday tezlanishni bermaydi."
            ),
            concepts=[
                c("Amallar soni (operation count, flop)",
                  "Algoritm bajaradigan ko'paytirish va qo'shishlar "
                  "soni. Odatda N ning darajasi sifatida yoziladi: "
                  "to'la LU uchun 2N^3/3, lentali uchun 2Nb^2. Bu "
                  "vaqtni to'g'ridan-to'g'ri bermaydi, lekin N "
                  "ikkilanganda vaqt necha marta oshishini beradi."),
                c("Lenta kengligi (bandwidth)",
                  "b = max|i - j|, bu yerda K_ij nolmas. Lentali "
                  "faktorizatsiya faqat lenta ichida ishlaydi, shuning "
                  "uchun narx to'g'ridan-to'g'ri b ga bog'liq. "
                  "Tuzilgan to'rda b to'rning eng qisqa kesimiga teng."),
                c("To'ldirilish (fill-in)",
                  "Faktorizatsiya davomida K da nol bo'lgan joyda "
                  "L yoki U da nolmas paydo bo'lishi. Siyrak "
                  "yechishning asosiy narxi — to'ldirilish, chunki u "
                  "ham xotirani, ham amallar sonini belgilaydi."),
                c("Tartiblash (ordering, renumbering)",
                  "Tugunlarni qayta raqamlash, ya'ni K ni P K P^T ga "
                  "almashtirish. Yechimni o'zgartirmaydi, lekin lenta "
                  "kengligini va to'ldirilishni tubdan o'zgartiradi. "
                  "RCM lentani toraytiradi, AMD to'ldirilishni "
                  "kamaytiradi."),
                c("Teskari Katxill-Makki (RCM, reverse Cuthill-McKee)",
                  "Grafni kenglik bo'yicha aylanib chiqib, tugunlarni "
                  "qatlam-qatlam raqamlaydigan evristika. Natijada "
                  "lenta kengligi to'rning kesimi tartibiga tushadi."),
                c("Minimal daraja (AMD, approximate minimum degree)",
                  "Har qadamda eng kam qo'shniga ega tugunni "
                  "chiqaradigan evristika. Lentani qaramaydi, "
                  "to'ldirilishni to'g'ridan-to'g'ri kamaytiradi va "
                  "shuning uchun RCM dan yaxshiroq natija beradi."),
                c("Uyalangan ajratish (nested dissection)",
                  "Sohani ajratuvchi (separator) bilan ikkiga bo'lib, "
                  "ajratuvchini oxirida raqamlash va buni rekursiv "
                  "takrorlash. 2D da nnz(L) ~ N log N, amallar ~ "
                  "N^{3/2}; 3D da nnz(L) ~ N^{4/3}, amallar ~ N^2."),
                c("Oldindan shartlash (preconditioning)",
                  "K u = f o'rniga M^{-1}K u = M^{-1}f yechish, bu "
                  "yerda M ni qurish arzon va M^{-1}K ning "
                  "shartlanganligi yaxshiroq. Iteratsiya soni "
                  "sqrt(kappa) ga bog'liq bo'lgani uchun kappa ni "
                  "kamaytirish to'g'ridan-to'g'ri vaqtni kamaytiradi."),
                c("Xotira devori (memory wall)",
                  "Katta masalalarda cheklovchi omil ko'pincha "
                  "amallar soni emas, balki xotira hajmi va unga "
                  "murojaat tezligi. Iterativ usullarning asosiy "
                  "ustunligi ham shu: ular K dan boshqa hech narsa "
                  "saqlamaydi."),
            ],
            derivation=[
                d("Lentali faktorizatsiyaning narxi",
                  "K_{ij} = 0,\\quad |i-j| > b \;\\Longrightarrow\; "
                  "\\text{amallar} \\approx 2Nb^2,\\quad "
                  "\\text{xotira} \\approx Nb",
                  "Gauss chiqarishning k-qadamida faqat k-ustundagi "
                  "lenta ichidagi b ta satr yangilanadi, har birida b "
                  "ta element. Demak bitta qadam ~b^2 amal, N ta qadam "
                  "~Nb^2 amal beradi (ko'paytirish va qo'shish bilan "
                  "2Nb^2). Muhim xususiyat: lentali faktorizatsiya "
                  "lentadan tashqariga hech qachon chiqmaydi, ya'ni "
                  "to'ldirilish lenta bilan chegaralangan."),
                d("Tuzilgan to'rda lenta kengligi kesim bilan belgilanadi",
                  "b = \\min(\\text{kesim})\;\\Longrightarrow\; "
                  "b \\sim N^{1/2}\\ (\\text{2D}),\\qquad "
                  "b \\sim N^{2/3}\\ (\\text{3D})",
                  "Besh nuqtali shablonda (i,j) tuguni (i,j±1) bilan "
                  "bog'langan; agar raqamlash i bo'yicha tez yursa, "
                  "bu qo'shnilarning nomeri n_x ga farq qiladi, demak "
                  "b = n_x. Shuning uchun HAR DOIM qisqa yo'nalish "
                  "bo'ylab raqamlash kerak: m×m to'rda b = m = "
                  "sqrt(N), 3D m×m×m to'rda esa butun kesim b = m^2 = "
                  "N^{2/3}. Bu oddiy qoida 16×64 to'rda amallar sonini "
                  "aynan (64/16)^2 = 16 marta o'zgartiradi."),
                d("2D va 3D uchun to'g'ri yechishning narxi",
                  "\\text{2D}: 2Nb^2 \\sim 2N\\cdot N = N^2;\\qquad "
                  "\\text{3D}: 2Nb^2 \\sim 2N\\cdot N^{4/3} = N^{7/3}",
                  "Lenta kengligini oldingi qadamdan qo'yamiz. Xotira "
                  "esa 2D da Nb ~ N^{3/2}, 3D da Nb ~ N^{5/3}. "
                  "Uyalangan ajratish bu ko'rsatkichlarni yaxshilaydi: "
                  "2D da amallar N^{3/2}, xotira N log N; 3D da "
                  "amallar N^2, xotira N^{4/3}. Ikkala holatda ham "
                  "3D 2D dan sezilarli qimmatroq — sabab geometrik: "
                  "3D da ajratuvchi yuza, 2D da esa chiziq."),
                d("CG iteratsiyalari shartlanganlik orqali",
                  "\\frac{\\|e_k\\|_A}{\\|e_0\\|_A} \\le "
                  "2\\left(\\frac{\\sqrt{\\kappa}-1}"
                  "{\\sqrt{\\kappa}+1}\\right)^{k} "
                  "\;\\Longrightarrow\; k \\le \\tfrac{1}{2}"
                  "\\sqrt{\\kappa}\\,\\ln\\frac{2}{\\varepsilon}",
                  "su-06 dagi CG bahosi. Chegaraviy masala uchun "
                  "kappa ~ h^{-2} (su-04), demak 2D da kappa ~ N va "
                  "k ~ sqrt(N) = N^{1/2}; 3D da kappa ~ N^{2/3} va "
                  "k ~ N^{1/3}. E'tibor bering: o'lchov qancha yuqori "
                  "bo'lsa, CG uchun SHUNCHA YAXSHI — bu to'g'ri "
                  "usullardagi holatning aynan teskarisi."),
                d("Kesishish: qaysi usul qachon yutadi",
                  "\\text{CG amallari} = 2\\,\\mathrm{nnz}\\cdot k "
                  "\\sim N\\cdot N^{1/2} = N^{3/2}\\ (\\text{2D}), "
                  "\\qquad N\\cdot N^{1/3} = N^{4/3}\\ (\\text{3D})",
                  "nnz ~ N, chunki har satrda qo'shnilar soni "
                  "chegaralangan. Endi taqqoslaymiz. 2D: to'g'ri "
                  "N^{3/2}, CG N^{3/2} — DARAJALAR TENG, tanlov "
                  "o'zgarmas koeffitsientlar, xotira va o'ng "
                  "tomonlar soniga qarab qilinadi (bitta "
                  "faktorizatsiya ko'p yuk holati uchun qayta "
                  "ishlatiladi). 3D: to'g'ri N^2, CG N^{4/3} — "
                  "farq N^{2/3}, ya'ni N = 10^6 da o'n ming baravar. "
                  "Xulosa qat'iy: katta 3D masalada iterativ "
                  "yechuvchi yagona amaliy yo'l."),
                d("Oldindan shartlash nimani o'zgartiradi",
                  "\\kappa(\\mathbf{M}^{-1}\\mathbf{K}) \\ll "
                  "\\kappa(\\mathbf{K}) \;\\Longrightarrow\; "
                  "k \\downarrow, \\qquad "
                  "\\mathbf{M} = \\mathrm{diag}(\\mathbf{K})\\ "
                  "(\\text{Yakobi})",
                  "Yakobi eng arzon variant: faqat diagonalga bo'lish. "
                  "Lekin u FAQAT diagonal tarqoq bo'lganda ishlaydi. "
                  "Bir jinsli materialdagi besh nuqtali shablonda "
                  "diagonal aynan o'zgarmas (hamma joyda 4), shuning "
                  "uchun unga bo'lish — o'zgarmasga ko'paytirish, "
                  "kappa esa umuman o'zgarmaydi. Hisobda bu 1,00x "
                  "tezlanish sifatida ko'rinadi. Material konstrasti "
                  "oshgan sari foyda paydo bo'ladi: 10 da 1,39x, "
                  "100 da 2,29x, 1000 da 5,89x."),
            ],
            meaning=(
                "**$2Nb^2$ — lentali yechishning narxi.** Bu ifodada N "
                "chiziqli, b esa KVADRAT ko'rinishda qatnashadi. "
                "Amaliy xulosa: masalani ikki baravar maydalashdan "
                "ko'ra, lenta kengligini ikki baravar toraytirish to'rt "
                "baravar ko'p foyda beradi. Aynan shuning uchun "
                "tartiblash — bu bepul optimallashtirish: u yechimni "
                "zarracha o'zgartirmaydi, faqat xotiradagi joylashuvni "
                "o'zgartiradi.\n\n"
                "**$b \\sim N^{1/2}$ va $b \\sim N^{2/3}$ — o'lchovning "
                "jazosi.** Lenta kengligi — to'rni ikkiga bo'luvchi "
                "eng kichik kesimdagi tugunlar soni. 2D da bu chiziq, "
                "3D da esa yuza. Yuza chiziqdan tezroq o'sadi, "
                "shuning uchun uch o'lchovli masala ikki o'lchovlidan "
                "nafaqat kattaroq, balki har bir noma'lum uchun ham "
                "qimmatroq.\n\n"
                "**$k \\le \\tfrac12\\sqrt{\\kappa}\\ln(2/\\varepsilon)$ "
                "— iterativ usulning narxi.** Bu yerda kappa ning "
                "KVADRAT ILDIZI turibdi, bu CG ning oddiy iteratsiyaga "
                "nisbatan asosiy yutug'i (su-06). Natijada CG ning "
                "narxi o'lchov oshishi bilan YAXSHILANADI: 2D da "
                "N^{1/2}, 3D da N^{1/3}. Sabab shundaki, bir xil N da "
                "3D to'r har bir yo'nalishda maydaroq emas, balki "
                "qo'polroq (m = N^{1/3}), demak h kattaroq va kappa "
                "kichikroq.\n\n"
                "**Xotira ifodalarini amallardan alohida o'qish kerak.** "
                "Ko'pincha masala amallar soni tufayli emas, xotira "
                "tufayli yechilmaydi. Kronshteyn misolida to'la "
                "matritsa 2 TB talab qiladi — bu 32 GB li mashinada "
                "ishlamaydi, amallar soni qanday bo'lishidan qat'i "
                "nazar. Iterativ usulning eng kuchli tomoni ham shu: "
                "uning xotirasi $\\mathcal{O}(N)$, ya'ni K dan tashqari "
                "faqat bir nechta vektor."
            ),
            equations=[
                eq("W_{\\text{to'la}} = \\tfrac{2}{3}N^3, \\qquad "
                   "M_{\\text{to'la}} = 8N^2\\ \\text{bayt}",
                   "To'la (zich) LU faktorizatsiyasining amallar soni "
                   "va xotirasi. Hech qanday siyraklikdan "
                   "foydalanilmaydi — bu yuqori chegara.",
                   "To'la yechishning narxi"),
                eq("W_{\\text{lenta}} \\approx 2Nb^2, \\qquad "
                   "M_{\\text{lenta}} \\approx 8Nb\\ \\text{bayt}",
                   "Lentali faktorizatsiya. b — lenta kengligi; "
                   "tartiblash aynan shu kattalikni kamaytiradi.",
                   "Lentali yechishning narxi"),
                eq("b_{\\text{2D}} \\sim N^{1/2}, \\qquad "
                   "b_{\\text{3D}} \\sim N^{2/3}",
                   "Tuzilgan to'rda lenta kengligi eng kichik kesimga "
                   "teng: 2D da chiziq, 3D da yuza.",
                   "Lenta kengligining o'lchovga bog'liqligi"),
                eq("\\text{2D}:\\ \\mathrm{nnz}(L) \\sim N\\log N, \\ "
                   "W \\sim N^{3/2}; \\qquad "
                   "\\text{3D}:\\ \\mathrm{nnz}(L) \\sim N^{4/3}, \\ "
                   "W \\sim N^{2}",
                   "Uyalangan ajratish tartiblashi uchun nazariy "
                   "baholar. AMD bu chegaraga yaqinlashadi, lekin "
                   "evristika bo'lgani uchun undan biroz yomonroq.",
                   "Uyalangan ajratishning baholari"),
                eq("\\frac{\\|\\mathbf{e}_k\\|_A}"
                   "{\\|\\mathbf{e}_0\\|_A} \\le "
                   "2\\left(\\frac{\\sqrt{\\kappa}-1}"
                   "{\\sqrt{\\kappa}+1}\\right)^{k}",
                   "CG ning yaqinlashish bahosi (su-06). Xatolik "
                   "energiya normasida o'lchanadi.",
                   "CG yaqinlashish bahosi"),
                eq("\\kappa(\\mathbf{K}) \\sim h^{-2} "
                   "\;\\Longrightarrow\; "
                   "k \\sim N^{1/2}\\ (\\text{2D}), \\quad "
                   "k \\sim N^{1/3}\\ (\\text{3D})",
                   "Chegaraviy masala matritsasining shartlanganligi "
                   "va undan kelib chiqadigan iteratsiya soni.",
                   "Iteratsiya sonining masshtablanishi"),
                eq("W_{\\text{CG}} = 2\\,\\mathrm{nnz}\\cdot k "
                   "\\sim N^{3/2}\\ (\\text{2D}), \\quad "
                   "N^{4/3}\\ (\\text{3D}), \\qquad "
                   "M_{\\text{CG}} = \\mathcal{O}(N)",
                   "Iterativ yechishning to'liq narxi. Xotira "
                   "o'lchovdan qat'i nazar chiziqli.",
                   "CG ning umumiy narxi"),
            ],
            conditions=(
                "Bu mavzuda 'chegaraviy shartlar' o'rnini ALGORITM "
                "QO'LLANISH SHARTLARI egallaydi — har bir baho faqat "
                "ma'lum farazlar ostida o'rinli.\n\n"
                "**Lentali baho uchun:** matritsa haqiqatan ham lenta "
                "tuzilishiga ega bo'lishi kerak. Bitta uzoq bog'lanish "
                "(masalan, ikki uzoq tugunni bog'laydigan MPC yoki "
                "davriy chegaraviy shart, su-17) lenta kengligini "
                "butun tizim o'lchamigacha ko'taradi va bahoni "
                "buzadi. Bunday bog'lanishlar alohida "
                "(Lagranj ko'paytuvchisi yoki chegara ajratish bilan) "
                "ishlatilishi kerak.\n\n"
                "**Cholesky uchun:** K simmetrik musbat aniq bo'lishi "
                "shart. Chegaraviy shartlar qo'yilmagan tizim "
                "qattiq jism harakatlari tufayli yarim aniq bo'ladi "
                "(su-15), nochiziqli masalada esa chegaraviy nuqtadan "
                "keyin tangensial matritsa aniqligini yo'qotadi "
                "(su-24). Ikkala holatda ham Cholesky ishlamaydi va "
                "LDL^T yoki boshqa strategiya kerak.\n\n"
                "**CG uchun:** K simmetrik musbat aniq bo'lishi shart. "
                "Nosimmetrik masalalarda (konveksiya, kontakt) "
                "GMRES yoki BiCGSTAB kerak, ularning bahosi esa "
                "sqrt(kappa) emas. Bundan tashqari CG ning "
                "to'xtatish mezoni QOLDIQ bo'yicha o'lchanadi, "
                "xatolik bo'yicha emas: ||r||/||f|| <= eps dan "
                "||e|| <= kappa*eps*||u|| kelib chiqadi, ya'ni yomon "
                "shartlangan tizimda qoldiq kichik bo'lsa ham xatolik "
                "katta bo'lishi mumkin (su-04).\n\n"
                "**Masshtablanish o'lchovi uchun:** o'lchangan daraja "
                "nazariyga faqat ASIMPTOTIK rejimda yaqinlashadi. "
                "Kichik N da kesh iyerarxiyasi va BLAS parallelligi "
                "natijani buzadi. Shuning uchun global log-log "
                "moslash emas, ketma-ket o'lchamlar orasidagi lokal "
                "qiyalik qaraladi va uning barqarorlashuvi kutiladi."
            ),
            worked=WorkedExample(
                statement=(
                    "Aviatsiya kronshteyni geksaedr elementlar bilan "
                    "modellashtirilgan: N = 500 000 erkinlik darajasi, "
                    "har bir satrda o'rtacha 81 ta nolmas (27 qo'shni "
                    "tugun × 3 erkinlik darajasi). Mavjud ish "
                    "stansiyasida 32 GB operativ xotira bor. "
                    "To'rt variant uchun xotira va amallar sonini "
                    "baholang va yechuvchini tanlang: (a) to'la "
                    "matritsa, (b) lentali, (c) siyrak + AMD "
                    "tartiblash, (d) oldindan shartlangan CG."
                ),
                given=[
                    "N = 500 000 erkinlik darajasi",
                    "Satrdagi o'rtacha nolmaslar soni: 81",
                    "Mavjud xotira: 32 GB",
                    "Haqiqiy son: 8 bayt (double)",
                    "3D uchun b ~ N^(2/3), nnz(L) ~ N^(4/3)",
                    "CG uchun k ~ c·N^(1/3), c ≈ 2,47 (o'lchangan)",
                ],
                steps=[
                    st("M_{\\text{to'la}} = 8N^2 = 8\\cdot(5\\cdot10^5)^2 "
                       "= 8 \\cdot 2{,}5\\cdot10^{11} = 2{,}0\\cdot10^{12}"
                       "\\ \\text{bayt} = 2{,}0\\ \\text{TB}",
                       "(a) To'la matritsa. 2 TB — mavjud 32 GB dan "
                       "62 baravar ko'p. Variant BEKOR QILINADI, "
                       "amallar sonini hisoblashning ham hojati yo'q. "
                       "Ma'lumot uchun: 2N^3/3 = 8,3·10^16 amal, bu "
                       "10 Gflop/s li mashinada ~100 kun."),
                    st("b \\sim N^{2/3} = (5\\cdot10^5)^{2/3} "
                       "\\approx 6300, \\qquad "
                       "M = 8Nb = 8\\cdot5\\cdot10^5\\cdot6300 "
                       "= 2{,}52\\cdot10^{10}\\ \\text{bayt} "
                       "= 25{,}2\\ \\text{GB}",
                       "(b) Lentali. 25,2 GB — 32 GB ga rasmiy "
                       "sig'adi, lekin operatsion tizim va dastur "
                       "uchun joy qolmaydi; amalda bu ishlamaydi. "
                       "Amallar: 2Nb^2 = 2·5·10^5·6300^2 = "
                       "4,0·10^13 flop, ya'ni ~1 soat. Chegaraviy "
                       "variant, ishonchsiz."),
                    st("\\mathrm{nnz}(L+U) \\sim N^{4/3} = "
                       "(5\\cdot10^5)^{4/3} \\approx 3{,}97\\cdot10^7, "
                       "\\qquad M = 8\\cdot3{,}97\\cdot10^7 "
                       "\\approx 0{,}32\\ \\text{GB}",
                       "(c) Siyrak + AMD. Atigi 0,32 GB — xotira "
                       "bo'yicha muammo YO'Q, lentaliga nisbatan 79 "
                       "baravar kam. Amallar esa 3D da ~N^2 = "
                       "2,5·10^11 flop, ya'ni ~25 sekund. Bu ishlaydigan "
                       "variant."),
                    st("\\mathrm{nnz}(K) = 81N = 4{,}05\\cdot10^7, "
                       "\\qquad M \\approx 4{,}05\\cdot10^7 \\cdot 12 "
                       "\\approx 0{,}49\\ \\text{GB}",
                       "(d) CG uchun xotira: qiymatlar (8 bayt) va "
                       "ustun indekslari (4 bayt) — satr boshiga "
                       "12 bayt, jami ~0,49 GB, ustiga bir nechta "
                       "vektor (har biri 4 MB). Xotira bo'yicha "
                       "muammo yo'q."),
                    st("k \\approx 2{,}47\\cdot N^{1/3} = "
                       "2{,}47 \\cdot 79{,}4 \\approx 196, \\qquad "
                       "W = 2\\,\\mathrm{nnz}\\cdot k = "
                       "2\\cdot4{,}05\\cdot10^7\\cdot196 "
                       "= 1{,}59\\cdot10^{10}\\ \\text{flop}",
                       "(d) CG uchun amallar. 1,6·10^10 flop — "
                       "siyrak to'g'ri usuldan 15,8 baravar kam, "
                       "ya'ni ~2 sekund. Koeffitsient c = 2,47 "
                       "quyidagi hisobda 3D Puasson uchun "
                       "o'lchangan (N = 32768 da 79 iteratsiya)."),
                    st("\\text{to'la} : \\text{CG} \\ \\text{xotira} "
                       "= \\frac{2{,}0\\cdot10^{12}}{4{,}9\\cdot10^{8}} "
                       "\\approx 4100\\times, \\qquad "
                       "\\text{to'g'ri} : \\text{CG}\\ \\text{amallar} "
                       "\\approx 15{,}8\\times",
                       "Yakuniy taqqoslash. Bir xil masala va bir xil "
                       "kompyuterda faqat saqlash formati va algoritm "
                       "tanlovi xotirani 4100 marta, amallarni esa "
                       "(to'la usulga nisbatan) besh million marta "
                       "kamaytirdi."),
                ],
                answer=(
                    "Tanlov: **oldindan shartlangan CG**. Xotira "
                    "~0,5 GB (32 GB dan juda kichik), amallar "
                    "1,6·10^10 flop (~2 sekund). Siyrak to'g'ri "
                    "usul (AMD) ham ishlaydi — 0,32 GB va ~25 sekund — "
                    "va agar KO'P YUK HOLATI yechilishi kerak bo'lsa, "
                    "aynan u afzal: faktorizatsiya bir marta "
                    "qilinadi, keyin har bir yuk uchun faqat "
                    "oldinga-orqaga yurish (~2·nnz(L) = 8·10^7 amal) "
                    "kerak. To'la va lentali variantlar bekor "
                    "qilinadi."
                ),
                engineering_note=(
                    "Bu yerda eng muhim amaliy xulosa: TANLOV BITTA "
                    "EMAS, u savolga bog'liq. Bitta statik tahlil uchun "
                    "CG aniq yutadi. Yuzta yuk holati uchun siyrak "
                    "to'g'ri usul yutadi, chunki uning qimmat qismi "
                    "(faktorizatsiya) bir marta to'lanadi. Xususiy "
                    "qiymat masalasida (su-23) ham to'g'ri usul afzal, "
                    "chunki teskari iteratsiya bir xil matritsani "
                    "qayta-qayta ishlatadi. Nochiziqli tahlilda "
                    "(su-24) esa tangensial matritsa har qadamda "
                    "o'zgaradi, demak yana iterativ usul tomonga "
                    "og'adi. Shuning uchun sanoat paketlarida "
                    "yechuvchi tanlovi foydalanuvchiga qoldiriladi — "
                    "va uni to'g'ri tanlash muhandisning vazifasi."
                ),
            ),
            computation=Computation(
                caption=(
                    "Tartiblash, to'ldirilish, oldindan shartlash va "
                    "masshtablanishni bitta hisobda o'lchash: RCM "
                    "lenta kengligini qanday tiklaydi, AMD "
                    "to'ldirilishni qancha kamaytiradi, Yakobi "
                    "qachon foyda beradi va o'lchangan daraja "
                    "nazariyga qachon yaqinlashadi."
                ),
                parameters=[
                    p("m", "To'r o'lchami (yo'nalish bo'yicha)",
                      8, 64, 20, 4, "tugun"),
                    p("dim", "Fazo o'lchovi (2 yoki 3)", 2, 3, 2, 1, ""),
                    p("seed", "Tasodifiy raqamlash urug'i", 1, 50, 1, 1, ""),
                ],
                code='''"""Hisoblash samaradorligi: tartiblash, xotira va usul tanlovi."""
import numpy as np
from scipy.sparse import coo_matrix, csc_matrix, diags, identity, kron
from scipy.sparse.csgraph import reverse_cuthill_mckee
from scipy.sparse.linalg import LinearOperator, cg, splu
from labkit import PARAMS, note, series, table, value

m = int(PARAMS.get("m", 20))
dim = int(PARAMS.get("dim", 2))
seed = int(PARAMS.get("seed", 1))
if dim == 3:                       # 3D da N = m^3 — resursni cheklaymiz
    m = min(m, 16)

# ---------------------------------------------------------------- to'r
def lap(mm, dd):
    """dd o'lchovli Puasson operatori, Dirixle chegara (su-11)."""
    T = diags([-1.0, 2.0, -1.0], [-1, 0, 1], shape=(mm, mm))
    I = identity(mm, format="csr")
    if dd == 2:
        return csc_matrix(kron(I, T) + kron(T, I))
    return csc_matrix(kron(I, kron(I, T)) + kron(I, kron(T, I))
                      + kron(T, kron(I, I)))

def het2d(mm, contrast, sd=1):
    """Heterogen material: har katakda o'z E si, yuz bo'yicha o'rtacha.

    DIQQAT: bu A = D K D emas. Diagonal masshtablash Yakobi bilan aynan
    qaytariladi va soxta tezlanish beradi; bu yerda E element darajasida
    yig'iladi, shuning uchun natija fizik ma'noga ega.
    """
    r = np.random.default_rng(sd)
    E = contrast ** r.uniform(-1.0, 1.0, size=(mm, mm))
    idx = np.arange(mm * mm).reshape(mm, mm)
    I, J, V = [], [], []
    dg = np.zeros((mm, mm))
    for sl_a, sl_b in ((np.s_[:-1, :], np.s_[1:, :]),
                       (np.s_[:, :-1], np.s_[:, 1:])):
        e = 0.5 * (E[sl_a] + E[sl_b])
        a, b, ev = idx[sl_a].ravel(), idx[sl_b].ravel(), e.ravel()
        I += [a, b]; J += [b, a]; V += [-ev, -ev]
        dg[sl_a] += e; dg[sl_b] += e
    dg[0, :] += E[0, :]; dg[-1, :] += E[-1, :]      # Dirixle tashqi yuzlar
    dg[:, 0] += E[:, 0]; dg[:, -1] += E[:, -1]
    I.append(idx.ravel()); J.append(idx.ravel()); V.append(dg.ravel())
    return csc_matrix(coo_matrix(
        (np.concatenate(V), (np.concatenate(I), np.concatenate(J))),
        shape=(mm * mm, mm * mm)))

bw = lambda A: int(np.max(np.abs(A.tocoo().row - A.tocoo().col)))
perm = lambda A, pr: csc_matrix(A[pr, :][:, pr])
g = lambda f: f.L.nnz + f.U.nnz

def n_iter(A, M=None):
    it = [0]
    cg(A, np.ones(A.shape[0]), rtol=1e-8, maxiter=50000,
       callback=lambda x: it.__setitem__(0, it[0] + 1), M=M)
    return it[0]

K = lap(m, dim)
N = K.shape[0]
value("N", N, "noma'lum")
value("nnz(K)", K.nnz, "dona")
value("Zichlik", 100.0 * K.nnz / N**2, "%")

# --- 1. Tartiblash lenta kengligini qanday o'zgartiradi -----------------
rng = np.random.default_rng(seed)
Krand = perm(K, rng.permutation(N))
Krcm = perm(Krand, reverse_cuthill_mckee(Krand, symmetric_mode=True))
rows = []
for nm, A in (("tabiiy", K), ("tasodifiy", Krand), ("RCM", Krcm)):
    b = bw(A)
    rows.append([nm, b, f"{2.0 * N * b**2:.2e}", f"{N * b * 8 / 1e6:.2f}"])
table("Lenta kengligi va lentali yechish narxi",
      ["Tartiblash", "b", "amallar ~ 2Nb^2", "xotira, MB"], rows)
value("RCM tejashi", (bw(Krand) / bw(Krcm)) ** 2, "marta")
note(
    "Tabiiy raqamlash allaqachon optimal bo'lgani uchun RCM uni "
    "yaxshilamaydi — ba'zan bir-ikki birlikka yomonlashtiradi ham. "
    "RCM ning foydasi to'r generatori bergan tartibsiz raqamlashda "
    "ko'rinadi: lenta kengligi N ga yaqin qiymatdan yana sqrt(N) "
    "atrofiga tushadi."
)

# --- 2. To'ldirilish -----------------------------------------------------
fills = {"tasodifiy": g(splu(Krand, permc_spec="NATURAL")),
         "RCM": g(splu(Krcm, permc_spec="NATURAL")),
         "AMD": g(splu(K, permc_spec="MMD_AT_PLUS_A"))}
rows = [[nm, v, f"{v / K.nnz:.1f}x", f"{v * 8 / 1e6:.2f}"]
        for nm, v in fills.items()]
rows.append(["to'la matritsa", N * N, f"{N * N / K.nnz:.1f}x",
             f"{N * N * 8 / 1e6:.2f}"])
table("Faktorizatsiyadagi to'ldirilish (fill-in)",
      ["Tartiblash", "nnz(L+U)", "K ga nisbatan", "xotira, MB"], rows)
value("AMD/RCM nisbati", fills["RCM"] / fills["AMD"], "marta")

# --- 3. Iterativ yechish -------------------------------------------------
it0 = n_iter(K)
value("CG iteratsiyalari", it0, "dona")
value("CG amallari", 2.0 * K.nnz * it0, "amal")
value("CG xotirasi", K.nnz * 8 / 1e6 + N * 4 * 8 / 1e6, "MB")

# --- 4. Yakobi oldindan shartlash qachon foyda beradi ---------------------
A1 = het2d(m, 1.0, seed)
K2 = lap(m, 2)
value("Nazorat: het(E=1) - K", float(abs(A1 - K2).max()), "-")
rows = []
for cst in (1.0, 10.0, 100.0, 1000.0):
    Ac = het2d(m, cst, seed)
    dg = Ac.diagonal()
    Mj = LinearOperator(Ac.shape, matvec=lambda x, dd=dg: x / dd)
    i1, i2 = n_iter(Ac), n_iter(Ac, Mj)
    rows.append([f"{cst:.0f}", f"{dg.max() / dg.min():.1f}", i1, i2,
                 f"{i1 / i2:.2f}x"])
table("Yakobi oldindan shartlash: material konstrastiga bog'liqlik",
      ["E_max/E_min", "diagonal farqi", "CG", "Yakobi-CG", "tezlanish"], rows)
note(
    "Bir jinsli materialda Yakobi mutlaqo foyda bermaydi (1,00x): "
    "besh nuqtali shablonning diagonali o'zgarmas, shuning uchun "
    "unga bo'lish — o'zgarmasga ko'paytirish, shartlanganlik soni esa "
    "o'zgarmaydi (su-04). Yakobi faqat diagonal tarqoq bo'lganda "
    "ishlaydi: turli material, keskin o'zgaruvchan element o'lchami "
    "yoki aralash birliklar."
)

# --- 5. Masshtablanish: o'lchangan daraja nazariyga qarshi ---------------
ms = [m // 2, m, 2 * m] if dim == 2 else [max(4, m // 2), m, min(2 * m, 24)]
Ns, its, fl = [], [], []
for mm in ms:
    A = lap(mm, dim)
    Ns.append(A.shape[0]); its.append(n_iter(A))
    fl.append(g(splu(A, permc_spec="MMD_AT_PLUS_A")))
lN = np.log(Ns)
q_it = float(np.polyfit(lN, np.log(its), 1)[0])
p_fl = float(np.polyfit(lN, np.log(fl), 1)[0])
value("CG darajasi q", q_it, "-")
value("Nazariy q", 0.5 if dim == 2 else 1.0 / 3.0, "-")
value("To'ldirilish darajasi p", p_fl, "-")
series("CG iteratsiyalari", Ns, its, "N", "iteratsiya")
series("To'ldirilish nnz(L+U)", Ns, fl, "N", "nolmas")
table("To'g'ri va iterativ usullarning o'sishi",
      ["O'lchov", "CG amallari (o'lchangan)", "To'g'ri xotira (o'lchangan)",
       "To'g'ri amallar (nazariy)", "CG xotirasi"],
      [[f"{dim}D", f"N^{1.0 + q_it:.2f}", f"N^{p_fl:.2f}",
        "N^1.50" if dim == 2 else "N^2.00", "N^1.00"]])
note(
    "Ikki o'lchovda to'g'ri va iterativ usul amallar bo'yicha deyarli "
    "teng (ikkalasi ham ~N^1.5): tanlov xotira va o'ng tomonlar soniga "
    "qarab qilinadi. Uch o'lchovda farq keskin — to'g'ri usul ~N^2, CG "
    "esa ~N^1.33. Katta 3D masalada iterativ usul yagona amaliy yo'l."
)
note(
    "O'lchangan daraja nazariyga faqat asimptotik rejimda yaqinlashadi. "
    "Kichik N da kesh va BLAS parallelligi uni pasaytiradi: to'la LU "
    "uchun 500-4000 oraliqda o'lchangan daraja 2,6-2,9, nazariy 3 emas. "
    "Shuning uchun global moslash emas, ketma-ket o'lchamlar orasidagi "
    "lokal qiyalik qaraladi."
)''',
                expected_output=(
                    "m = 20, dim = 2 (N = 400) da: tabiiy raqamlashda "
                    "lenta kengligi 20, tasodifiy raqamlashda 392, "
                    "RCM dan keyin yana 20 — ya'ni RCM amallar sonini "
                    "384 marta kamaytiradi. To'ldirilish: tasodifiy "
                    "32934, RCM 11820, AMD 7344 (to'la matritsada "
                    "160000). Nazorat tekshiruvi het(E=1) - K = 0 "
                    "aynan nolga teng. Yakobi tezlanishi konstrast "
                    "bo'yicha 1,00x / 1,39x / 2,29x / 5,89x. "
                    "CG darajasi q = 0,58 (m = 40 da 0,51), nazariy 0,5."
                ),
            ),
            visual=vis(
                kind="Matritsa portreti va masshtablanish grafiklari",
                tool="React/SVG + Matplotlib",
                description=(
                    "To'rtta bog'liq ko'rinish: (1) uchta matritsa "
                    "portreti (tabiiy, tasodifiy, RCM) yonma-yon; "
                    "(2) faktorizatsiyadan keyingi to'ldirilish "
                    "xaritasi uchta tartiblash uchun; (3) log-log "
                    "masshtablanish grafigi nazariy qiyalik "
                    "uchburchagi bilan; (4) to'g'ri va iterativ "
                    "usul narxining N bo'yicha kesishishi."
                ),
                how_to_draw=(
                    "Portret uchun nolmas elementlarning (i, j) "
                    "koordinatalarini nuqta sifatida chizish; uchta "
                    "panel bir xil o'lchamda bo'lsin, shunda "
                    "tasodifiy holatdagi 'chang bulut' va RCM dan "
                    "keyingi tor diagonal tasma keskin farq qilsin. "
                    "To'ldirilish xaritasida K ning asl nolmaslari "
                    "bir rangda, faktorizatsiya qo'shgan yangi "
                    "nolmaslar boshqa rangda ko'rsatiladi — "
                    "to'ldirilishning ma'nosi shunda darhol "
                    "ko'rinadi. Masshtablanish grafigida o'qlar "
                    "logarifmik, nuqtalar ustiga qiyaligi 1,5 va 1,0 "
                    "bo'lgan mos uchburchaklar qo'yiladi. Kesishish "
                    "grafigida ikkita chiziq (to'g'ri va CG) va "
                    "ularning kesishgan nuqtasi vertikal chiziq bilan "
                    "belgilanadi; 2D va 3D uchun alohida panel "
                    "chiziladi, shunda 2D da chiziqlar deyarli "
                    "parallel, 3D da esa keskin ajralishi ko'rinadi."
                ),
            ),
            interp=(
                "**Tartiblash bepul, lekin hal qiluvchi.** Hisobda "
                "tasodifiy raqamlash lenta kengligini 20 dan 392 ga "
                "ko'tardi — ya'ni amallar soni 384 marta oshdi, "
                "matritsaning o'zi esa umuman o'zgarmadi. RCM uni "
                "yana 20 ga tushirdi. Bu shuni anglatadiki, to'r "
                "generatori bergan tartib bilan to'g'ridan-to'g'ri "
                "yechish — bu yuzlab baravar ortiqcha ish.\n\n"
                "**Lekin RCM yaxshi tartibni yaxshilamaydi.** "
                "Tuzilgan to'rning tabiiy raqamlashi allaqachon "
                "optimal (b = 20), va RCM undan oshib keta olmaydi; "
                "cho'zinchoq to'rlarda u hatto bir-ikki birlikka "
                "yomonroq natija beradi. Bu muhim tuzatish: "
                "tartiblash — bu har doim yoqiladigan 'tezlatgich' "
                "emas, balki yomon tartibni tuzatadigan vosita.\n\n"
                "**AMD lentani emas, to'ldirilishni kamaytiradi.** "
                "Jadvalda RCM 11820, AMD esa 7344 nolmas berdi — "
                "1,6 baravar kam, garchi AMD lenta kengligi haqida "
                "umuman qayg'urmasa ham. Sabab: lenta — bu "
                "to'ldirilishning YUQORI CHEGARASI, aniq o'lchovi "
                "emas. Lentani toraytirish to'ldirilishni bilvosita "
                "kamaytiradi, AMD esa unga to'g'ridan-to'g'ri "
                "hujum qiladi va shuning uchun yutadi.\n\n"
                "**Yakobi oldindan shartlash bir jinsli masalada "
                "MUTLAQO foydasiz.** Jadvaldagi birinchi satr "
                "1,00x beradi — 36 iteratsiya oldin ham, keyin ham. "
                "Bu xato emas: besh nuqtali shablonning diagonali "
                "hamma joyda 4 ga teng, demak M = diag(K) = 4I, "
                "unga bo'lish esa shartlanganlik sonini "
                "o'zgartirmaydi (su-04). Foyda faqat diagonal "
                "tarqoq bo'lganda paydo bo'ladi, va u konstrast "
                "bilan bir tekis o'sadi: 1,39x, 2,29x, 5,89x. "
                "Amaliyotda diagonalni tarqoq qiladigan narsalar — "
                "turli material, keskin o'zgaruvchan element "
                "o'lchami va aralash birliklar (siljish va burilish "
                "bitta vektorda, su-20).\n\n"
                "**O'lchangan daraja nazariyga sekin yaqinlashadi.** "
                "m = 20 da CG darajasi q = 0,58, m = 40 da 0,51, "
                "nazariy qiymat esa 0,5. Xuddi shu hol to'la LU da "
                "ham kuzatiladi: N = 500...4000 oralig'ida o'lchangan "
                "daraja 2,6-2,9 chiqadi, nazariy 3 emas — chunki "
                "kichik matritsalar keshga sig'adi va BLAS ularni "
                "samaraliroq qayta ishlaydi. Xulosa metodologik: "
                "masshtablanishni o'lchaganda global log-log moslash "
                "aldaydi, ketma-ket o'lchamlar orasidagi lokal "
                "qiyalikka qarash kerak — bu su-28 dagi kuzatilgan "
                "tartib (p_obs) g'oyasining aynan o'zi.\n\n"
                "**O'lchov to'g'ri va iterativ usullarga TESKARI "
                "ta'sir qiladi.** To'g'ri usul uchun 3D 2D dan "
                "qimmatroq (N^2 va N^{3/2}), iterativ usul uchun esa "
                "ARZONROQ (N^{4/3} va N^{3/2}). Bu bitta geometrik "
                "sababdan kelib chiqadi: bir xil N da 3D to'r har "
                "yo'nalishda qo'polroq (m = N^{1/3}), demak h "
                "kattaroq, kappa kichikroq, iteratsiyalar kam. "
                "To'g'ri usulda esa ajratuvchi yuza bo'lgani uchun "
                "to'ldirilish tezroq o'sadi. Shu bitta kuzatish "
                "butun sanoat amaliyotini tushuntiradi: kichik 2D "
                "masalalarda to'g'ri yechuvchi standart, katta 3D "
                "masalalarda esa iterativ."
            ),
            mistakes=[
                "Tartiblash yechimni o'zgartiradi deb o'ylash. "
                "P K P^T u' = P f tizimi bir xil yechimni beradi, "
                "faqat komponentlar tartibi boshqa. Natijani qaytarib "
                "tartiblashni (u = P^T u') unutish esa — haqiqiy "
                "xato, va u sezilmay qolishi mumkin, chunki "
                "siljishlar 'ishonarli' ko'rinadi.",
                "RCM ni har doim yoqish va undan foyda kutish. "
                "Tuzilgan to'rning tabiiy raqamlashi allaqachon "
                "optimal; RCM u yerda hech narsa bermaydi va "
                "cho'zinchoq sohada natijani bir oz yomonlashtiradi. "
                "RCM ning o'rni — to'r generatori bergan tartibsiz "
                "raqamlashni tuzatish.",
                "To'ldirilishni lenta kengligi bilan tenglashtirish. "
                "Lenta — to'ldirilishning yuqori chegarasi, aniq "
                "o'lchovi emas. Shuning uchun lentani "
                "minimallashtiruvchi RCM to'ldirilishni "
                "minimallashtiruvchi AMD dan yomonroq ishlaydi "
                "(hisobda 1,6 baravar).",
                "Yakobi oldindan shartlashni 'har doim biroz "
                "yordam beradi' deb hisoblash. Bir jinsli materialda "
                "diagonal o'zgarmas, demak Yakobi — o'zgarmasga "
                "ko'paytirish va kappa umuman o'zgarmaydi (aynan "
                "1,00x). Foyda faqat diagonal tarqoq bo'lganda bor.",
                "Heterogenlikni A = D K D ko'rinishida modellashtirib, "
                "Yakobining foydasini o'lchash. Bunday matritsada "
                "Yakobi aynan D ni qaytaradi va soxta ulkan "
                "tezlanish beradi. Heterogenlik material darajasida, "
                "element matritsalari orqali kiritilishi kerak.",
                "To'g'ri usulning narxini faqat amallar soni bilan "
                "baholash. Ko'pincha masala amallar tufayli emas, "
                "XOTIRA tufayli yechilmaydi: kronshteyn misolida "
                "lentali variant amallar bo'yicha maqbul (~1 soat), "
                "lekin 25 GB talab qiladi va amalda ishlamaydi.",
                "CG ning to'xtatish mezonini xatolik deb tushunish. "
                "CG qoldiqni o'lchaydi; ||r||/||f|| <= eps dan "
                "xatolik uchun kappa marta yomonroq baho kelib "
                "chiqadi. Yomon shartlangan tizimda 'yaqinlashdi' "
                "degan xabar aniq yechimni kafolatlamaydi (su-04).",
                "O'lchangan masshtablanish darajasini global log-log "
                "moslash bilan aniqlash. Kichik N nuqtalari kesh "
                "effekti tufayli qiyalikni pasaytiradi; natijada "
                "to'la LU uchun 3 o'rniga 2,4 chiqadi va 'nazariya "
                "noto'g'ri' degan noto'g'ri xulosa qilinadi. Lokal "
                "qiyalikka qarash kerak.",
                "Faktorizatsiyani har bir yuk holati uchun qaytadan "
                "bajarish. To'g'ri usulning butun ustunligi shunda: "
                "K bir marta faktorlanadi, keyin har bir f uchun "
                "faqat oldinga-orqaga yurish (~2·nnz(L) amal) "
                "kerak. Buni sezmaslik ko'p yuklik masalada o'nlab "
                "baravar ortiqcha vaqt beradi.",
            ],
            quiz=[
                q("Lenta kengligi b ikki baravar toraytirilsa, "
                  "lentali faktorizatsiyaning amallari va xotirasi "
                  "necha marta kamayadi?",
                  "Amallar 2Nb^2 ga proporsional bo'lgani uchun "
                  "TO'RT marta kamayadi; xotira esa Nb ga "
                  "proporsional, shuning uchun IKKI marta kamayadi. "
                  "Aynan shu assimetriya tartiblashni shunday "
                  "foydali qiladi: b ni toraytirish amallarga "
                  "kvadratik ta'sir ko'rsatadi.",
                  kind="hisob",
                  options=["Amallar 2x, xotira 2x",
                           "Amallar 4x, xotira 2x",
                           "Amallar 4x, xotira 4x",
                           "Amallar 8x, xotira 4x"],
                  correct_index=1),
                q("Tuzilgan 16×64 to'rda tugunlar uzun yo'nalish "
                  "bo'ylab raqamlangan. Qisqa yo'nalishga "
                  "o'tkazilsa, lentali yechishning amallari necha "
                  "marta kamayadi?",
                  "Lenta kengligi raqamlash tez yuradigan "
                  "yo'nalishdagi tugunlar soniga teng: uzun bo'ylab "
                  "b = 64, qisqa bo'ylab b = 16. Amallar b^2 ga "
                  "proporsional, demak (64/16)^2 = 16 marta "
                  "kamayadi. Bu hisobda aynan o'lchangan.",
                  kind="hisob",
                  options=["4 marta", "8 marta", "16 marta", "64 marta"],
                  correct_index=2),
                q("Nima uchun lenta kengligini minimallashtiruvchi "
                  "RCM to'ldirilish bo'yicha AMD dan yomonroq "
                  "ishlaydi?",
                  "Chunki lenta — to'ldirilishning YUQORI CHEGARASI, "
                  "aniq o'lchovi emas. Lenta ichida ham ko'p nol "
                  "qolishi mumkin, va RCM ularni saqlashga harakat "
                  "qilmaydi. AMD esa to'ldirilishga to'g'ridan-"
                  "to'g'ri hujum qiladi: har qadamda eng kam "
                  "qo'shniga ega tugunni chiqaradi. Hisobda AMD "
                  "7344, RCM 11820 nolmas berdi — 1,6 baravar farq.",
                  kind="konseptual"),
                q("Bir jinsli materialdagi besh nuqtali Puasson "
                  "masalasida Yakobi oldindan shartlash CG "
                  "iteratsiyalarini necha marta kamaytiradi?",
                  "UMUMAN kamaytirmaydi — aynan 1,00x. Diagonal "
                  "hamma joyda 4 ga teng, demak M = 4I va "
                  "M^{-1}K = K/4. O'zgarmasga ko'paytirish "
                  "shartlanganlik sonini o'zgartirmaydi, CG esa "
                  "faqat kappa ga sezgir. Yakobi foydasi diagonal "
                  "tarqoq bo'lgandagina paydo bo'ladi.",
                  kind="konseptual",
                  options=["~1,0 marta (umuman yordam bermaydi)",
                           "~1,4 marta", "~2,3 marta",
                           "~4 marta"],
                  correct_index=0),
                q("Nima uchun uch o'lchovli masala to'g'ri usul "
                  "uchun qimmatroq, iterativ usul uchun esa "
                  "arzonroq?",
                  "Ikkalasi bitta geometrik sabab bilan "
                  "tushuntiriladi. To'g'ri usulda narx sohani "
                  "ikkiga bo'luvchi ajratuvchining kattaligiga "
                  "bog'liq: 2D da bu chiziq (~N^{1/2}), 3D da yuza "
                  "(~N^{2/3}) — 3D da tezroq o'sadi. Iterativ "
                  "usulda narx kappa ~ h^{-2} orqali to'r "
                  "qadamiga bog'liq: bir xil N da 3D to'r har "
                  "yo'nalishda QO'POLROQ (m = N^{1/3}, 2D da esa "
                  "N^{1/2}), demak h kattaroq, kappa kichikroq va "
                  "iteratsiyalar kam. Natijada to'g'ri usul "
                  "N^{3/2} → N^2 ga, CG esa N^{3/2} → N^{4/3} ga "
                  "o'tadi.",
                  kind="konseptual"),
                q("500 000 erkinlik darajali 3D modelda to'la "
                  "matritsa uchun qancha xotira kerak?",
                  "M = 8N^2 = 8·(5·10^5)^2 = 8·2,5·10^11 = "
                  "2,0·10^12 bayt = 2,0 TB. Bu odatdagi ish "
                  "stansiyasidan (32 GB) 62 baravar ko'p, shuning "
                  "uchun variant amallar sonini hisoblamasdanoq "
                  "bekor qilinadi.",
                  kind="hisob",
                  options=["2,0 GB", "25 GB", "200 GB", "2,0 TB"],
                  correct_index=3),
                q("Yuzta turli yuk holati uchun bitta konstruksiya "
                  "yechilishi kerak. Qaysi usul afzal va nima "
                  "uchun?",
                  "Siyrak TO'G'RI usul afzal. Uning qimmat qismi — "
                  "faktorizatsiya — bir marta bajariladi, keyin har "
                  "bir yuk uchun faqat oldinga-orqaga yurish kerak, "
                  "bu ~2·nnz(L) amal, ya'ni faktorizatsiyadan "
                  "yuzlab marta arzon. CG esa har bir o'ng tomon "
                  "uchun to'liq qaytadan ishlaydi, demak narx yuk "
                  "holatlari soniga to'g'ri proporsional o'sadi.",
                  kind="talqin"),
                q("Hisobda CG darajasi m = 20 da q = 0,58, m = 40 "
                  "da esa 0,51 chiqdi, nazariy qiymat 0,5. Bu "
                  "nazariyaning xatosimi?",
                  "Yo'q. Bu asimptotik rejimga sekin kirishning "
                  "belgisi: kichik N da chegaraviy effektlar va "
                  "kesh xatti-harakati o'lchovni buzadi, N ortgani "
                  "sari o'lchangan daraja nazariyga yaqinlashadi. "
                  "Shuning uchun global log-log moslash emas, "
                  "ketma-ket o'lchamlar orasidagi LOKAL qiyalik "
                  "qaralishi kerak — bu su-28 dagi kuzatilgan "
                  "tartib g'oyasining aynan o'zi.",
                  kind="talqin"),
                q("Konstruksiyaga ikkita uzoq tugunni bog'laydigan "
                  "MPC qo'shildi. Bu lentali yechuvchiga qanday "
                  "ta'sir qiladi?",
                  "Bitta uzoq bog'lanish lenta kengligini shu ikki "
                  "tugun nomerlari farqigacha, ya'ni amalda butun "
                  "tizim o'lchamigacha ko'taradi. Natijada 2Nb^2 "
                  "bahosi buziladi va lentali yechuvchi to'la "
                  "yechuvchiga aylanadi. Shuning uchun bunday "
                  "bog'lanishlar chegara ajratish yoki Lagranj "
                  "ko'paytuvchisi bilan alohida ishlanadi (su-17).",
                  kind="talqin"),
                q("To'la LU ning o'lchangan masshtablanish darajasi "
                  "N = 500...4000 oralig'ida 2,6-2,9 chiqdi, "
                  "nazariy 3 emas. Sabab nima?",
                  "Kichik matritsalar protsessor keshiga sig'adi va "
                  "BLAS ularni blokli algoritmlar bilan nisbatan "
                  "samaraliroq qayta ishlaydi; bundan tashqari "
                  "chaqiruv qo'shimcha xarajatlari kichik N da "
                  "sezilarli ulush egallaydi. Natijada vaqt N "
                  "bo'yicha nazariy N^3 dan sekinroq o'sadi. "
                  "N ortgani sari lokal qiyalik 3 ga yaqinlashadi "
                  "(o'lchovda 2,62 → 2,65 → 2,85).",
                  kind="kod"),
            ],
            bridge=(
                "Kurs endi to'liq: su-01 da sonli usulning nima "
                "uchun kerakligi qo'yilgan edi, su-29 da esa uning "
                "narxi qanday hisoblanishi va kamaytirilishi "
                "ko'rsatildi. Oralig'ida beshta fan — nazariy "
                "mexanikadan boshlab, materiallar qarshiligi, "
                "tutash muhitlar mexanikasi, plastinalar va "
                "qobiqlar nazariyasi orqali — har biri keyingisiga "
                "tenglama berib keldi. su-30 shu zanjirni yopadi: "
                "bitta real konstruksiya elementi ustida "
                "modellashtirish qarori, diskretlashtirish, "
                "yechish, xatolik baholash, validatsiya va "
                "resurs rejalashtirish bitta uzluksiz ish "
                "oqimiga birlashtiriladi — ya'ni butun kurs "
                "bitta masalada takrorlanadi."
            ),
            research=(
                "Ko'p to'rli (multigrid) usullar N ga PROPORSIONAL "
                "murakkablikka erishadi — bu chegaraviy masalalar "
                "uchun nazariy jihatdan optimal natija, chunki har "
                "bir noma'lumni hech bo'lmaganda bir marta "
                "o'qish kerak. G'oya: xatolikning silliq qismi "
                "qo'pol to'rda arzon yo'qotiladi, tebranuvchi "
                "qismi esa maydan to'rda bir necha silliqlash "
                "qadami bilan. Zamonaviy tadqiqot yo'nalishlari: "
                "algebraik multigrid (AMG) — bu yerda qo'pol "
                "darajalar geometriyadan emas, matritsaning o'zidan "
                "quriladi, bu esa tartibsiz to'r va anizotrop "
                "materiallarga yo'l ochadi; domenlarga ajratish "
                "(FETI, BDDC) usullarining parallel masshtablanishi "
                "o'n minglab yadroda; GPU uchun siyrak "
                "yechuvchilar va ularda xotira o'tkazuvchanligining "
                "hal qiluvchi roli; matritsasiz (matrix-free) "
                "formulirovkalar, bu yerda K umuman yig'ilmaydi va "
                "faqat K·v ko'paytma element darajasida hisoblanadi "
                "— yuqori tartibli elementlarda bu xotirani va "
                "vaqtni bir vaqtda tejaydi. Alohida yo'nalish — "
                "aralash aniqlik (mixed precision): "
                "faktorizatsiyani 32 bitda bajarib, natijani 64 "
                "bitli iterativ yaxshilash bilan tuzatish, bu esa "
                "zamonaviy apparatda ikki baravar tezlanish beradi "
                "(su-02 dagi yaxlitlash tahlili bevosita shu yerda "
                "ishlaydi)."
            ),
            manim_ref=manim(
                scene="OrderingAndFillIn",
                module="manim/scenes/su29_samaradorlik.py",
                title="Tartiblash, to'ldirilish va usul tanlovi",
                summary=(
                    "Sahna bir xil to'rning uchta raqamlanishini "
                    "ko'rsatadi va har biri uchun matritsa portreti "
                    "yonida quriladi: tabiiy raqamlashda tor "
                    "diagonal tasma, tasodifiy raqamlashda butun "
                    "maydonga sochilgan nuqtalar, RCM dan keyin esa "
                    "yana tasma. Keyin faktorizatsiya animatsiya "
                    "qilinadi: L va U to'lib borar ekan, yangi "
                    "paydo bo'lgan nolmaslar boshqa rangda "
                    "yonadi — to'ldirilishning ma'nosi shunda "
                    "ko'rinadi. Uchta holat uchun hisoblagich "
                    "nolmaslar sonini sanaydi va oxirida 32934 / "
                    "11820 / 7344 qiymatlari yonma-yon qoladi. "
                    "Yakunda log-log grafik chiziladi: to'g'ri va "
                    "iterativ usulning narxi 2D da deyarli "
                    "parallel, 3D ga o'tilganda esa ular keskin "
                    "ajraladi va kesishish nuqtasi chapga suriladi."
                ),
            ),
        ),
    ),
]
