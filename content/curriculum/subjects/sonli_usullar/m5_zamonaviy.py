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
]
