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
]
