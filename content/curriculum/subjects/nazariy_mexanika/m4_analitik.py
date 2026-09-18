"""NM / 4-modul: Analitik mexanika (nm-19 … nm-24)."""

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

S = "nazariy-mexanika"
M = "nm-m4"

TOPICS = [
    Topic(
        id="nm-19",
        subject_id=S,
        module_id=M,
        order=19,
        title="Bog'lanishlar tasnifi, umumlashgan koordinatalar va erkinlik darajalari",
        description=(
            "Golonom va nogolonom bog'lanishlar, umumlashgan koordinatalarni tanlash, "
            "konfiguratsion fazo tushunchasi."
        ),
        learning_objective=(
            "Mexanizm uchun erkinlik darajalari sonini aniqlash va minimal sonli "
            "umumlashgan koordinatalarni tanlash."
        ),
        prerequisites=["nm-10", "nm-05"],
        mathematical_core=(
            "Bog'lanish tenglamalari $f(\\mathbf{r}, t) = 0$, implitsit funksiya, "
            "konfiguratsion fazo, o'zgaruvchilar soni va tenglamalar soni balansi."
        ),
        engineering_application=(
            "Robot manipulyator kinematikasi, mexanizmlar sinteziga kirish, "
            "ko'p jismli tizimlar (multibody) modellari."
        ),
        computational_component=(
            "Mexanizm erkinlik darajalarini Chebishev–Grubler formulasi bilan "
            "hisoblash va bog'lanish matritsasi rangini tekshirish."
        ),
        visualization_component=(
            "Mexanizm sxemasi va uning konfiguratsion fazodagi tasviri."
        ),
        research_extension=(
            "Nogolonom bog'lanish (dumalash) nima uchun erkinlik darajalari sonini "
            "kamaytirmaydi, lekin harakatni cheklaydi?"
        ),
        difficulty="murakkab",
        previous_link=(
            "nm-10 da bog'lanishlarni reaksiya kuchlari bilan almashtirdik. "
            "Analitik mexanikada esa boshqa yo'l tanlanadi: bog'lanishlarni "
            "koordinatalar tanloviga 'singdirib yuborish'."
        ),
        next_topic="nm-20",
        estimated_minutes=85,
        tags=["bog'lanish", "umumlashgan koordinata", "erkinlik darajasi"],
        lesson=Lesson(
            physical_problem=(
                "Olti bo'g'inli robot manipulyatorining holatini tavsiflash uchun "
                "nechta son kerak? Har bir bo'g'in fazoda 6 ta erkinlik darajasiga ega, "
                "demak 36 ta son? Yo'q — sharnirlar ularni bog'laydi va aslida atigi "
                "6 ta burchak yetarli. Bu 'siqish' analitik mexanikaning asosiy g'oyasi: "
                "reaksiyalar bilan ishlash o'rniga, ularni umuman paydo bo'lmaydigan "
                "koordinatalarni tanlash."
            ),
            concepts=[
                c("Golonom bog'lanish", "$f(\\mathbf{r}_1,\\dots,\\mathbf{r}_n, t) = 0$ "
                  "— faqat koordinatalarni bog'laydi. Koordinatalar sonini kamaytiradi."),
                c("Nogolonom bog'lanish", "Tezliklarni bog'laydi va integrallanmaydi "
                  "(masalan, sirpanmasdan dumalash). Erkinlik darajasini kamaytiradi, "
                  "lekin koordinatalar sonini emas."),
                c("Skleronom / reonom", "Vaqtga oshkor bog'liq bo'lmagan / bog'liq "
                  "bog'lanishlar. Reonom bog'lanishda energiya saqlanmasligi mumkin."),
                c("Umumlashgan koordinata $q_i$", "Tizim holatini to'liq aniqlovchi "
                  "mustaqil parametrlar. Ular uzunlik, burchak yoki istalgan qulay "
                  "kattalik bo'lishi mumkin."),
                c("Erkinlik darajasi", "$n = 3N - s$ (fazoda, golonom bog'lanishlar "
                  "uchun), $N$ — nuqtalar soni, $s$ — bog'lanishlar soni."),
            ],
            derivation=[
                d("1-qadam. Koordinatalar sonini sanash",
                  r"N\ \text{nuqta} \Rightarrow 3N\ \text{koordinata (fazoda)},\quad "
                  r"2N\ (\text{tekislikda})",
                  "Bog'lanishsiz tizimning konfiguratsiyasi shuncha son bilan beriladi."),
                d("2-qadam. Bog'lanish tenglamalarini yozish",
                  r"f_k(x_1,y_1,z_1,\dots,t) = 0,\qquad k = 1,\dots,s",
                  "Har bir golonom bog'lanish bitta tenglama va shu bilan bitta "
                  "erkinlik darajasini olib tashlaydi."),
                d("3-qadam. Erkinlik darajalari soni",
                  r"\boxed{\;n = 3N - s\;}",
                  "Mustaqil bog'lanishlar soni $s$ = bog'lanish matritsasining rangi. "
                  "Agar bog'lanishlar o'zaro bog'liq bo'lsa, $s$ kamayadi."),
                d("4-qadam. Umumlashgan koordinatalarga o'tish",
                  r"\mathbf{r}_i = \mathbf{r}_i(q_1, q_2, \dots, q_n, t),\qquad i = 1,\dots,N",
                  "Barcha Dekart koordinatalari $n$ ta mustaqil parametr orqali "
                  "ifodalanadi. Bog'lanishlar avtomatik bajariladi — bu ularning "
                  "reaksiyalarini hisobdan chiqarib tashlaydi."),
                d("5-qadam. Tekis mexanizmlar uchun Chebishev formulasi",
                  r"n = 3(k-1) - 2p_5 - p_4",
                  "$k$ — bo'g'inlar soni (stanina bilan), $p_5$ — bir erkinlik darajali "
                  "juftliklar (sharnir), $p_4$ — ikki erkinlik darajali juftliklar. "
                  "Krivoship-shatun: $k=4$, $p_5=4$ → $n = 9-8 = 1$ ✓"),
            ],
            formula_meaning=(
                "$n = 3N - s$ mexanikaning 'buxgalteriyasi': har bir bog'lanish bitta "
                "erkinlikni yeydi. Umumlashgan koordinatalar esa qolgan erkinliklarni "
                "eng qisqa yo'l bilan tavsiflaydi. Amaliy foyda ulkan: 36 ta "
                "koordinata va 30 ta bog'lanish o'rniga 6 ta mustaqil burchak. "
                "Bu — hisoblash hajmining kubik qisqarishi."
            ),
            equations=[
                eq(r"n = 3N - s", "Erkinlik darajalari soni (fazoda, golonom).", "Erkinlik darajasi"),
                eq(r"n = 3(k-1) - 2p_5 - p_4", "Chebishev–Grubler formulasi (tekis mexanizm).",
                   "Chebishev formulasi"),
                eq(r"\mathbf{r}_i = \mathbf{r}_i(q_1,\dots,q_n,t)", "Umumlashgan koordinatalarga o'tish.",
                   "Koordinata almashtirish"),
            ],
            conditions=(
                "Umumlashgan koordinatalarni tanlash noyagona — bir xil tizimni turli "
                "yo'llar bilan parametrlash mumkin. Yaxshi tanlov mezoni: "
                "$\\mathbf{r}_i(q)$ ifodalari sodda bo'lsin va koordinatalar butun "
                "harakat sohasida singulyar bo'lmasin (masalan, burchaklar 0 yoki "
                "$\\pi/2$ da kinematik zanjir singulyarlikka tushmasin)."
            ),
            worked_example=WorkedExample(
                statement=(
                    "Ikki bo'g'inli tekis manipulyator: uzunliklari $l_1 = 0{,}4$ m va "
                    "$l_2 = 0{,}3$ m, ikkala sharnir aylanma. (a) Erkinlik darajalari "
                    "soni; (b) uch uchining koordinatalarini umumlashgan koordinatalar "
                    "orqali yozing; (c) uch $(0{,}5;\\,0{,}2)$ nuqtaga borishi mumkinmi?"
                ),
                given=[r"l_1 = 0{,}4\ \text{m},\; l_2 = 0{,}3\ \text{m}",
                       r"q_1, q_2\ \text{— sharnir burchaklari}"],
                steps=[
                    st(r"k = 3\ (\text{stanina} + 2\ \text{bo'g'in}),\quad p_5 = 2 "
                       r"\Rightarrow n = 3(3-1) - 2\cdot 2 = 6 - 4 = 2",
                       "Chebishev formulasi: ikki erkinlik darajasi."),
                    st(r"x = l_1\cos q_1 + l_2\cos(q_1+q_2),\qquad "
                       r"y = l_1\sin q_1 + l_2\sin(q_1+q_2)",
                       "To'g'ri kinematika masalasi — har doim yagona yechimga ega."),
                    st(r"r = \sqrt{x^2+y^2} = \sqrt{0{,}5^2+0{,}2^2} = \sqrt{0{,}29} = 0{,}5385\ \text{m}",
                       "Nishondan boshlang'ichgacha masofa."),
                    st(r"|l_1 - l_2| = 0{,}1 \le r = 0{,}5385 \le l_1+l_2 = 0{,}7 \;\checkmark",
                       "Nuqta ishchi sohada — yechim mavjud."),
                    st(r"\cos q_2 = \frac{r^2 - l_1^2 - l_2^2}{2l_1l_2} = "
                       r"\frac{0{,}29 - 0{,}16 - 0{,}09}{2\cdot 0{,}12} = \frac{0{,}04}{0{,}24} = 0{,}1667",
                       "Kosinuslar teoremasi — teskari kinematika."),
                    st(r"q_2 = \pm 80{,}4^\circ,\qquad q_1 = \arctan\frac{0{,}2}{0{,}5} \mp "
                       r"\arctan\frac{l_2\sin q_2}{l_1+l_2\cos q_2}",
                       "Ikki yechim: 'tirsak yuqorida' va 'tirsak pastda' konfiguratsiyalari."),
                ],
                answer=(
                    "(a) $n = 2$; (b) yuqoridagi formulalar; (c) ha, ikkita yechim bilan: "
                    "$q_2 = +80{,}4°$ yoki $q_2 = -80{,}4°$."
                ),
                engineering_note=(
                    "Teskari kinematikaning ko'p yechimliligi — robototexnikaning asosiy "
                    "muammolaridan biri. Boshqaruv tizimi qaysi konfiguratsiyani "
                    "tanlashni hal qilishi kerak: to'siqlardan qochish, energiya sarfi "
                    "yoki singulyarlikdan uzoqlik mezonlari bo'yicha."
                ),
            ),
            computation=Computation(
                caption=(
                    "Ikki bo'g'inli manipulyator: bo'g'in uzunliklarini o'zgartirib, "
                    "ishchi sohani va teskari kinematika yechimlarini ko'ring."
                ),
                code='''"""Umumlashgan koordinatalar: manipulyator kinematikasi."""
import numpy as np
from labkit import PARAMS, note, series, table, value

l1 = float(PARAMS.get("l1", 0.4))
l2 = float(PARAMS.get("l2", 0.3))
x_t = float(PARAMS.get("x_t", 0.5))
y_t = float(PARAMS.get("y_t", 0.2))

def forward(q1, q2):
    """To'g'ri kinematika: umumlashgan koordinatalardan Dekartga."""
    x = l1*np.cos(q1) + l2*np.cos(q1+q2)
    y = l1*np.sin(q1) + l2*np.sin(q1+q2)
    return x, y

def inverse(x, y, elbow_up=True):
    """Teskari kinematika: ikki yechimdan birini qaytaradi."""
    r2 = x*x + y*y
    cos_q2 = (r2 - l1**2 - l2**2)/(2*l1*l2)
    if abs(cos_q2) > 1:
        return None
    q2 = np.arccos(cos_q2)*(1 if elbow_up else -1)
    q1 = np.arctan2(y, x) - np.arctan2(l2*np.sin(q2), l1 + l2*np.cos(q2))
    return q1, q2

# Erkinlik darajalari (Chebishev)
k, p5, p4 = 3, 2, 0
n_dof = 3*(k-1) - 2*p5 - p4
value("Erkinlik darajalari n", n_dof, "—")
value("Ishchi soha: r_min", abs(l1-l2), "m")
value("Ishchi soha: r_max", l1+l2, "m")
value("Nishongacha masofa", float(np.hypot(x_t, y_t)), "m")

sol_up = inverse(x_t, y_t, True)
sol_dn = inverse(x_t, y_t, False)
if sol_up is None:
    note("Nishon ishchi sohadan tashqarida — yechim yo'q.")
else:
    table("Teskari kinematika yechimlari",
          ["Konfiguratsiya", "q₁, deg", "q₂, deg", "Tekshirish x", "Tekshirish y"],
          [["Tirsak yuqorida", float(np.degrees(sol_up[0])), float(np.degrees(sol_up[1])),
            float(forward(*sol_up)[0]), float(forward(*sol_up)[1])],
           ["Tirsak pastda", float(np.degrees(sol_dn[0])), float(np.degrees(sol_dn[1])),
            float(forward(*sol_dn)[0]), float(forward(*sol_dn)[1])]])

# Ishchi soha chegaralari
th = np.linspace(0, 2*np.pi, 200)
series("Tashqi chegara", ((l1+l2)*np.cos(th)).tolist(), ((l1+l2)*np.sin(th)).tolist(),
       xlabel="x, m", ylabel="y, m")
series("Ichki chegara", (abs(l1-l2)*np.cos(th)).tolist(), (abs(l1-l2)*np.sin(th)).tolist(),
       xlabel="x, m", ylabel="y, m")

# Konfiguratsion fazoda traektoriya: q1 va q2 bir vaqtda o'zgaradi
tt = np.linspace(0, 1, 120)
q1_path = np.radians(10 + 60*tt)
q2_path = np.radians(80 - 100*tt)
xs, ys = forward(q1_path, q2_path)
series("Uch traektoriyasi", xs.tolist(), ys.tolist(), xlabel="x, m", ylabel="y, m")
series("Konfiguratsion fazo (q₁, q₂)", np.degrees(q1_path).tolist(),
       np.degrees(q2_path).tolist(), xlabel="q₁, deg", ylabel="q₂, deg")

# Singulyarlik: Yakobian determinanti
J_det = l1*l2*np.sin(q2_path)
note(f"Yakobian determinanti minimal moduli: {np.min(np.abs(J_det)):.5f}. "
     f"Nolga yaqin bo'lsa — singulyar konfiguratsiya (q₂ = 0 yoki 180°).")
''',
                parameters=[
                    p("l1", "1-bo'g'in uzunligi l₁", 0.1, 1.0, 0.4, 0.05, "m"),
                    p("l2", "2-bo'g'in uzunligi l₂", 0.1, 1.0, 0.3, 0.05, "m"),
                    p("x_t", "Nishon x", -1.5, 1.5, 0.5, 0.05, "m"),
                    p("y_t", "Nishon y", -1.5, 1.5, 0.2, 0.05, "m"),
                ],
                expected_output="n = 2; r_max = 0,7 m; q₂ = ±80,4°",
            ),
            visualization=vis(
                "Mexanizm va konfiguratsion fazo",
                "React/SVG",
                "Chapda manipulyator sxemasi va ishchi soha halqasi; o'ngda "
                "$(q_1, q_2)$ konfiguratsion fazosi va unda harakat traektoriyasi.",
                "React/SVG: ikki panelni yonma-yon qo'yish — fizik fazo va "
                "konfiguratsion fazo o'rtasidagi moslikni ko'rsatishning eng aniq usuli. "
                "Sliderlar bilan $q_1, q_2$ ni o'zgartirganda ikkala panelda bir vaqtda "
                "nuqta harakatlanadi.",
            ),
            interpretation=(
                "Ishchi soha — halqa: ichki radius $|l_1-l_2|$, tashqi $l_1+l_2$. "
                "Yakobian determinanti $l_1l_2\\sin q_2$ nolga aylanganda ($q_2 = 0$ "
                "yoki $180°$) manipulyator singulyar holatga tushadi: u yerda ba'zi "
                "yo'nalishlarda harakat qilish imkonsiz, sharnir tezliklari esa "
                "cheksizlikka intiladi. Bu — robot boshqaruvida qat'iy qochiladigan holat."
            ),
            common_mistakes=[
                "Bog'lanishlarning mustaqilligini tekshirmaslik — bog'liq bog'lanishlar "
                "erkinlik darajasini ikki marta kamaytirib yuboradi.",
                "Nogolonom bog'lanishni golonom deb hisoblash. Dumalash sharti "
                "integrallanmaydi va koordinatalar sonini kamaytirmaydi.",
                "Umumlashgan koordinatalarni ortiqcha tanlash — shunda ular mustaqil "
                "bo'lmaydi va Lagranj tenglamalari (nm-22) noto'g'ri chiqadi.",
                "Chebishev formulasida stanina (qo'zg'almas bo'g'in) ni sanamaslik.",
            ],
            quiz=[
                q("Golonom va nogolonom bog'lanish orasidagi asosiy farq nima?",
                  "Golonom bog'lanish koordinatalarni bog'laydi va koordinatalar sonini "
                  "kamaytiradi; nogolonom esa faqat tezliklarni bog'laydi, integrallanmaydi "
                  "va koordinatalar sonini kamaytirmaydi.", "konseptual"),
                q("Tekislikda harakatlanuvchi erkin qattiq jism nechta erkinlik "
                  "darajasiga ega?",
                  "3 ta: $x_C$, $y_C$ va burilish burchagi $\\varphi$.", "konseptual"),
                q("To'rt bo'g'inli sharnirli mexanizm ($k=4$, $p_5=4$) uchun $n$?",
                  "$n = 3(4-1) - 2\\cdot 4 = 9 - 8 = 1$. Bitta erkinlik darajasi.", "hisob"),
                q("Nima uchun umumlashgan koordinatalarda bog'lanish reaksiyalari "
                  "yo'qoladi?",
                  "Chunki koordinatalar bog'lanishlarni avtomatik qanoatlantiradi — "
                  "tizim faqat ruxsat etilgan konfiguratsiyalarda 'yashaydi', reaksiyalar "
                  "esa ish bajarmaydi.", "talqin"),
                q("Kodda `np.arctan2` nima uchun `np.arctan` o'rniga ishlatilgan?",
                  "`arctan2(y, x)` to'rt chorakni to'g'ri aniqlaydi, `arctan(y/x)` esa "
                  "faqat $(-\\pi/2, \\pi/2)$ oralig'ini beradi va ishorani yo'qotadi.",
                  "kod"),
            ],
            bridge_to_next=(
                "Koordinatalarni tanladik. Endi ularda muvozanat shartini yozish kerak "
                "— va bu Nyuton usulidan butunlay farq qiladi: kuchlar emas, "
                "mumkin bo'lgan ko'chishlardagi ish tahlil qilinadi."
            ),
            research_extension=(
                "Nogolonom bog'lanishga misol — g'ildirakli robot (unicycle modeli): "
                "$\\dot{x}\\sin\\theta - \\dot{y}\\cos\\theta = 0$. Bu bog'lanish "
                "integrallanmasligini isbotlang (Frobenius sharti) va robotning "
                "3 ta koordinataga ega bo'la turib 2 ta boshqaruv bilan istalgan "
                "nuqtaga bora olishini sonli ko'rsating."
            ),
        ),
    ),
    Topic(
        id="nm-20",
        subject_id=S,
        module_id=M,
        order=20,
        title="Mumkin bo'lgan ko'chishlar prinsipi va umumlashgan kuchlar",
        description=(
            "Virtual (mumkin bo'lgan) ko'chish, ideal bog'lanish, virtual ishlar "
            "prinsipi va umumlashgan kuch tushunchasi."
        ),
        learning_objective=(
            "Murakkab mexanizm muvozanatini reaksiyalarni hisoblamasdan, virtual "
            "ishlar prinsipi orqali topish."
        ),
        prerequisites=["nm-19", "nm-14"],
        mathematical_core=(
            "Variatsiya $\\delta$, virtual ko'chish, umumlashgan kuch "
            "$Q_j = \\sum\\mathbf{F}_i\\cdot\\partial\\mathbf{r}_i/\\partial q_j$."
        ),
        engineering_application=(
            "Press, richagli mexanizm, gidravlik uzatma kuch nisbati, "
            "konstruksiya muvozanati."
        ),
        computational_component=(
            "Umumlashgan kuchni simvolik (SymPy) hisoblash va muvozanat holatini topish."
        ),
        visualization_component=(
            "Mexanizm va uning virtual ko'chishi (kichik siljish) diagrammasi."
        ),
        research_extension=(
            "Virtual ishlar prinsipi deformatsiyalanuvchi jismga qanday "
            "umumlashtiriladi? (tmm-19 va su-13 ga ko'prik)"
        ),
        difficulty="murakkab",
        previous_link=(
            "nm-19 da mustaqil koordinatalarni tanladik. Endi muvozanat shartini "
            "aynan shu koordinatalarda yozamiz — natijada noma'lum reaksiyalar "
            "tenglamaga umuman kirmaydi."
        ),
        next_topic="nm-21",
        estimated_minutes=95,
        tags=["virtual ish", "umumlashgan kuch", "variatsion prinsip"],
        lesson=Lesson(
            physical_problem=(
                "Gidravlik pressda kichik kuch katta kuchga aylanadi. Richagli "
                "mexanizmda ham shunday. Kuch nisbatini topish uchun barcha "
                "sharnirlardagi reaksiyalarni hisoblash mumkin — lekin bu uzoq yo'l. "
                "Qisqa yo'l: energiya saqlanadi, demak kichik kuch katta yo'lda, "
                "katta kuch kichik yo'lda ish bajaradi. Bu oddiy mulohazani qat'iy "
                "matematik prinsipga aylantiramiz."
            ),
            concepts=[
                c("Virtual (mumkin bo'lgan) ko'chish $\\delta\\mathbf{r}$",
                  "Bog'lanishlar ruxsat etadigan cheksiz kichik xayoliy ko'chish. "
                  "Vaqt o'zgarmaydi ($\\delta t = 0$) — bu haqiqiy ko'chishdan farqi."),
                c("Ideal bog'lanish", "Reaksiyalarining virtual ishi nolga teng: "
                  "$\\sum\\mathbf{R}_i\\cdot\\delta\\mathbf{r}_i = 0$. Silliq sirt, "
                  "cho'zilmas tros, sharnir — barchasi ideal."),
                c("Virtual ishlar prinsipi", "Ideal bog'lanishli tizim muvozanatda "
                  "bo'lishi uchun faol kuchlarning virtual ishi nolga teng bo'lishi "
                  "zarur va yetarli."),
                c("Umumlashgan kuch $Q_j$", "$\\delta A = \\sum_j Q_j\\delta q_j$ "
                  "yoyilmasidagi koeffitsient. O'lchamligi $q_j$ ga bog'liq: burchak "
                  "uchun — moment, uzunlik uchun — kuch."),
                c("Potensial holda", "$Q_j = -\\partial\\Pi/\\partial q_j$ — umumlashgan "
                  "kuch potensial energiyaning gradiyenti."),
            ],
            derivation=[
                d("1-qadam. Muvozanatdagi har bir nuqta uchun",
                  r"\mathbf{F}_i + \mathbf{R}_i = 0 \;\Rightarrow\; "
                  r"\sum_i(\mathbf{F}_i+\mathbf{R}_i)\cdot\delta\mathbf{r}_i = 0",
                  "Har bir nuqtaning muvozanat shartini virtual ko'chishga skalyar "
                  "ko'paytirib jamlaymiz."),
                d("2-qadam. Ideal bog'lanish shartini qo'llash",
                  r"\sum_i\mathbf{R}_i\cdot\delta\mathbf{r}_i = 0 \;\Rightarrow\; "
                  r"\boxed{\;\delta A = \sum_i\mathbf{F}_i\cdot\delta\mathbf{r}_i = 0\;}",
                  "Reaksiyalar tenglamadan butunlay yo'qoldi — bu prinsipning asosiy "
                  "kuchi. Endi faqat faol kuchlar qoladi."),
                d("3-qadam. Umumlashgan koordinatalarga o'tish",
                  r"\delta\mathbf{r}_i = \sum_{j=1}^{n}\frac{\partial\mathbf{r}_i}{\partial q_j}\delta q_j "
                  r"\;\Rightarrow\; \delta A = \sum_j\underbrace{\left(\sum_i\mathbf{F}_i\cdot"
                  r"\frac{\partial\mathbf{r}_i}{\partial q_j}\right)}_{Q_j}\delta q_j",
                  "Zanjir qoidasi. Qavs ichidagi ifoda — $j$-umumlashgan kuch."),
                d("4-qadam. Muvozanat shartlari",
                  r"\delta q_j\ \text{mustaqil} \;\Rightarrow\; \boxed{\;Q_j = 0,\quad j=1,\dots,n\;}",
                  "$n$ ta tenglama, $n$ ta noma'lum — noma'lum reaksiyalar umuman "
                  "qatnashmaydi. Nyuton usulida esa ularni ham topish kerak edi."),
                d("5-qadam. Press uchun qo'llash",
                  r"\delta A = F_1\delta s_1 - F_2\delta s_2 = 0 \;\Rightarrow\; "
                  r"\frac{F_2}{F_1} = \frac{\delta s_1}{\delta s_2} = i",
                  "Kuch nisbati ko'chishlar nisbatiga teskari — 'mexanikaning oltin "
                  "qoidasi'. Ideal mexanizmda energiyada yutuq yo'q, faqat kuch va "
                  "yo'l almashadi."),
            ],
            formula_meaning=(
                "Virtual ishlar prinsipi mexanikani 'kuch balansi' tilidan 'energiya "
                "balansi' tiliga o'tkazadi. Amaliy foyda: 20 ta sharnirli mexanizmda "
                "40 ta reaksiya o'rniga bitta tenglama yoziladi. Nazariy foyda undan "
                "ham katta — bu prinsip deformatsiyalanuvchi jismlarga (tmm-19), "
                "so'ngra Ritz va chekli elementlar usuliga (su-13, su-18) "
                "to'g'ridan-to'g'ri umumlashadi. Butun hisoblash mexanikasi shu "
                "g'oyaga asoslanadi."
            ),
            equations=[
                eq(r"\sum_i\mathbf{F}_i\cdot\delta\mathbf{r}_i = 0", "Virtual ishlar prinsipi.",
                   "Virtual ishlar prinsipi"),
                eq(r"Q_j = \sum_i\mathbf{F}_i\cdot\frac{\partial\mathbf{r}_i}{\partial q_j}",
                   "Umumlashgan kuch.", "Umumlashgan kuch"),
                eq(r"Q_j = -\frac{\partial\Pi}{\partial q_j}", "Potensial kuchlar uchun.",
                   "Potensial holda"),
            ],
            conditions=(
                "Prinsip ideal bog'lanishlarni talab qiladi. Ishqalanish bo'lsa, "
                "ishqalanish kuchini faol kuchlar qatoriga kiritish kerak (chunki "
                "uning virtual ishi nolga teng emas). Bog'lanish reaksiyasini topish "
                "kerak bo'lsa, tegishli bog'lanishni olib tashlab, uni noma'lum faol "
                "kuch bilan almashtirish mumkin — shunda erkinlik darajasi bittaga ortadi."
            ),
            worked_example=WorkedExample(
                statement=(
                    "Richagli press: dastaga $F_1 = 200$ N kuch qo'yilgan, dasta "
                    "uzunligi $a = 0{,}6$ m, u sharnirdan $b = 0{,}05$ m masofadagi "
                    "shatun orqali porshenni bosadi. Dasta gorizontaldan $\\varphi = 30°$ "
                    "burchakda. Porshendagi kuchni va uzatish nisbatini toping."
                ),
                given=[r"F_1 = 200\ \text{N},\; a = 0{,}6\ \text{m},\; b = 0{,}05\ \text{m}",
                       r"\varphi = 30^\circ"],
                steps=[
                    st(r"\delta s_1 = a\,\delta\varphi",
                       "Dasta uchining virtual ko'chishi (kuch yo'nalishi bo'ylab)."),
                    st(r"\delta s_2 = b\cos\varphi\,\delta\varphi",
                       "Porshen ko'chishi — shatun geometriyasidan; $\\cos\\varphi$ "
                       "proyeksiya koeffitsienti."),
                    st(r"\delta A = F_1 a\,\delta\varphi - F_2 b\cos\varphi\,\delta\varphi = 0",
                       "Virtual ishlar prinsipi: faqat faol kuchlar."),
                    st(r"F_2 = \frac{F_1 a}{b\cos\varphi} = \frac{200\cdot 0{,}6}{0{,}05\cdot 0{,}866}",
                       "$\\delta\\varphi$ ixtiyoriy bo'lgani uchun qavs nolga teng."),
                    st(r"F_2 = \frac{120}{0{,}0433} = 2771\ \text{N}",
                       "Porshendagi kuch."),
                    st(r"i = \frac{F_2}{F_1} = 13{,}86;\qquad \varphi\to 0:\ i \to 12;\quad "
                       r"\varphi\to 90^\circ:\ i \to\infty",
                       "Uzatish nisbati burchakka bog'liq — $\\varphi$ ortganda o'sadi, "
                       "lekin porshen yurishi kamayadi."),
                ],
                answer=(
                    "$F_2 = 2771$ N; uzatish nisbati $i = 13{,}86$ ($\\varphi = 30°$ da)."
                ),
                engineering_note=(
                    "$\\varphi \\to 90°$ da kuch cheksizlikka intiladi — bu 'o'lik nuqta' "
                    "effekti va u ekssentrik presslarda ataylab ishlatiladi: shtamplash "
                    "momentida maksimal kuch kerak, yo'l esa minimal. Lekin real "
                    "mexanizmda kuch elastik deformatsiya hisobiga cheklanadi."
                ),
            ),
            computation=Computation(
                caption=(
                    "Virtual ishlar prinsipi: press geometriyasini o'zgartirib, "
                    "uzatish nisbatining burchakka bog'liqligini tadqiq qiling."
                ),
                code='''"""Virtual ishlar prinsipi va umumlashgan kuchlar (simvolik + sonli)."""
import numpy as np
import sympy as sp
from labkit import PARAMS, note, series, table, value

a = float(PARAMS.get("a", 0.6))        # dasta uzunligi, m
b = float(PARAMS.get("b", 0.05))       # krivoship radiusi, m
F1 = float(PARAMS.get("F1", 200.0))    # qo'yilgan kuch, N
phi_deg = float(PARAMS.get("phi", 30.0))

# --- Simvolik: umumlashgan kuchni hosila orqali olish ---
phi, Fa, aa, bb = sp.symbols("phi F_a a b", positive=True)
s1 = aa*phi                  # dasta uchining yo'li
s2 = bb*sp.sin(phi)          # porshen yo'li
Q_phi = Fa*sp.diff(s1, phi)  # faol kuchning umumlashgan kuchi
dS2 = sp.diff(s2, phi)
F2_sym = sp.simplify(Q_phi/dS2)
note(f"F2(phi) = {F2_sym}")

phi_r = np.radians(phi_deg)
F2 = F1*a/(b*np.cos(phi_r))
value("Porshendagi kuch F₂", F2, "N")
value("Uzatish nisbati i", F2/F1, "—")
value("Dasta ko'chishi (δφ=0,01 rad)", a*0.01*1000, "mm")
value("Porshen ko'chishi", b*np.cos(phi_r)*0.01*1000, "mm")

# Energiya balansini tekshirish
dphi = 0.01
dA1 = F1*a*dphi
dA2 = F2*b*np.cos(phi_r)*dphi
note(f"Virtual ish balansi: F₁·δs₁ = {dA1:.4f} J, F₂·δs₂ = {dA2:.4f} J, "
     f"farq = {abs(dA1-dA2):.2e} J")

# Uzatish nisbatining burchakka bog'liqligi
ph = np.linspace(1, 85, 200)
i_ratio = a/(b*np.cos(np.radians(ph)))
series("Uzatish nisbati i(φ)", ph.tolist(), i_ratio.tolist(),
       xlabel="φ, deg", ylabel="i = F₂/F₁")
series("Porshen yurishi", ph.tolist(), (b*np.cos(np.radians(ph))*1000).tolist(),
       xlabel="φ, deg", ylabel="δs₂ (δφ=1 rad), mm")

# Umumlashgan kuch potensial holda: Q = -dΠ/dq
k_spr, q_sym = sp.symbols("k q", positive=True)
Pi = k_spr*q_sym**2/2 - Fa*q_sym
Q = -sp.diff(Pi, q_sym)
q_eq = sp.solve(sp.Eq(Q, 0), q_sym)[0]
note(f"Prujinali tizim muvozanati: Q = {Q}, q_muvozanat = {q_eq}")

table("Burchakka bog'liqlik",
      ["φ, deg", "i", "F₂, N", "Porshen yurishi (δφ=0,01), mm"],
      [[float(x), float(a/(b*np.cos(np.radians(x)))),
        float(F1*a/(b*np.cos(np.radians(x)))),
        float(b*np.cos(np.radians(x))*0.01*1000)] for x in (0, 15, 30, 45, 60, 75)])
''',
                parameters=[
                    p("a", "Dasta uzunligi a", 0.1, 2.0, 0.6, 0.05, "m"),
                    p("b", "Krivoship radiusi b", 0.01, 0.3, 0.05, 0.005, "m"),
                    p("F1", "Qo'yilgan kuch F₁", 10.0, 2000.0, 200.0, 10.0, "N"),
                    p("phi", "Burchak φ", 0.0, 85.0, 30.0, 5.0, "deg"),
                ],
                expected_output="F₂ = 2771 N, i = 13,86, virtual ish balansi mos",
            ),
            visualization=vis(
                "Virtual ko'chish diagrammasi",
                "Manim",
                "Mexanizm asosiy holatida (to'q rang) va virtual ko'chgan holatida "
                "(och rang, bo'rttirilgan); $\\delta s_1$ va $\\delta s_2$ ko'chishlari "
                "o'lchamlari bilan ko'rsatilgan.",
                "Manim: virtual ko'chish tushunchasi — 'xayoliy, cheksiz kichik' — "
                "statik chizmada tushuntirish qiyin. Animatsiyada mexanizmni juda "
                "kichik burchakka burib, ko'chishlarni bo'rttirib ko'rsatish g'oyani "
                "aniq yetkazadi. React/SVG da $i(\\varphi)$ grafigi interaktiv beriladi.",
            ),
            interpretation=(
                "$i(\\varphi)$ grafigi $\\varphi \\to 90°$ da keskin ko'tariladi, "
                "porshen yurishi esa nolga tushadi. Bu — 'mexanikaning oltin qoidasi' "
                "ning miqdoriy tasdig'i: kuchda yutuq aynan yo'lda yo'qotish evaziga. "
                "Presslarni aynan shu sohada ishlatish maqsadga muvofiq, chunki "
                "shtamplashda katta kuch va kichik yurish kerak."
            ),
            common_mistakes=[
                "Virtual va haqiqiy ko'chishni chalkashtirish. Virtual ko'chishda vaqt "
                "o'zgarmaydi ($\\delta t = 0$), haqiqiyda esa o'zgaradi.",
                "Reaksiyalarni virtual ishga qo'shish — ideal bog'lanishda ular nol ish "
                "bajaradi.",
                "Ishqalanishni ideal bog'lanish deb hisoblash — u faol kuch sifatida "
                "kiritilishi kerak.",
                "$\\delta q_j$ larni mustaqil deb qabul qilish, agar koordinatalar "
                "ortiqcha tanlangan bo'lsa.",
            ],
            quiz=[
                q("Nima uchun virtual ishlar prinsipida reaksiyalar qatnashmaydi?",
                  "Ideal bog'lanish ta'rifi bo'yicha reaksiyalar virtual ko'chishga "
                  "perpendikular yoki qarama-qarshi juftlikda bo'ladi — ularning "
                  "virtual ishi nolga teng.", "konseptual"),
                q("Umumlashgan kuchning o'lchamligi nimaga bog'liq?",
                  "Mos umumlashgan koordinataga: $q$ uzunlik bo'lsa $Q$ — kuch [N], "
                  "$q$ burchak bo'lsa $Q$ — moment [N·m]. Ko'paytmasi har doim ish [J].",
                  "konseptual"),
                q("$\\Pi = kq^2/2 - Fq$. Muvozanat holati?",
                  "$Q = -d\\Pi/dq = -kq + F = 0 \\Rightarrow q = F/k$.", "hisob"),
                q("Richag uzunligini 2 marta oshirsak, uzatish nisbati qanday o'zgaradi?",
                  "2 marta ortadi, chunki $i = a/(b\\cos\\varphi)$.", "hisob"),
                q("Kodda `sp.diff(s1, phi)` nimani beradi?",
                  "$\\partial s_1/\\partial\\varphi$ — umumlashgan kuchni hisoblash uchun "
                  "zarur bo'lgan qisman hosila. Bu $Q_j$ ta'rifining bevosita amalga "
                  "oshirilishi.", "kod"),
            ],
            bridge_to_next=(
                "Virtual ishlar prinsipi statikani hal qildi. Endi uni dinamikaga "
                "kengaytirish kerak — buning uchun D'Alembert inersiya kuchini "
                "kiritadi va dinamik masalani statik ko'rinishga keltiradi."
            ),
            research_extension=(
                "Virtual ishlar prinsipini elastik sterjenga qo'llang: "
                "$\\int_0^L EI\\,w''\\,\\delta w''\\,dx = \\int_0^L q\\,\\delta w\\,dx$. "
                "Bu — mq-24 dagi Mor integrali va su-13 dagi zaif shaklning "
                "to'g'ridan-to'g'ri manbai. Sodda konsol uchun bitta sinov funksiyasi "
                "bilan taqribiy yechim oling va aniq yechim bilan taqqoslang."
            ),
        ),
    ),
    Topic(
        id="nm-21",
        subject_id=S,
        module_id=M,
        order=21,
        title="D'Alembert prinsipi va dinamik masalani statikaga keltirish",
        description=(
            "Inersiya kuchi, D'Alembert prinsipi, kinetostatika usuli va "
            "umumlashgan D'Alembert–Lagranj tenglamasi."
        ),
        learning_objective=(
            "Inersiya kuchlarini to'g'ri kiritib, dinamik masalani muvozanat "
            "masalasiga keltirish va murakkab mexanizmlarni hisoblash."
        ),
        prerequisites=["nm-20", "nm-18"],
        mathematical_core=(
            "Inersiya kuchi $-m\\mathbf{a}$, inersiya kuchlari bosh vektori va bosh "
            "momenti, D'Alembert–Lagranj umumiy tenglamasi."
        ),
        engineering_application=(
            "Tez harakatlanuvchi mexanizmlar hisobi, aylanuvchi jismlar "
            "podshipniklaridagi dinamik reaksiyalar, kran va lift dinamikasi."
        ),
        computational_component=(
            "Aylanuvchi sterjendagi inersiya kuchlari taqsimotini hisoblash va "
            "eguvchi moment epyurasini qurish."
        ),
        visualization_component=(
            "Inersiya kuchlari taqsimoti epyurasi va ekvivalent statik sxema."
        ),
        research_extension=(
            "Inersiya kuchi 'haqiqiy' kuchmi? Nyuton va D'Alembert yondashuvlarining "
            "falsafiy va amaliy farqi."
        ),
        difficulty="murakkab",
        previous_link=(
            "nm-20 dagi virtual ishlar prinsipi faqat statika uchun edi. D'Alembert "
            "g'oyasi uni dinamikaga kengaytiradi: $m\\mathbf{a}$ ni o'ng tomondan "
            "chap tomonga o'tkazib, uni 'kuch' deb atash kifoya."
        ),
        next_topic="nm-22",
        estimated_minutes=90,
        tags=["D'Alembert", "inersiya kuchi", "kinetostatika"],
        lesson=Lesson(
            physical_problem=(
                "Sentrifuga roterining sterjeni yuqori tezlikda aylanadi. Undagi "
                "eguvchi moment qanday taqsimlanadi? Statik hisobda sterjenga faqat "
                "og'irlik ta'sir qiladi va moment kichik. Lekin aylanishda har bir "
                "element markazdan qochma effekt oladi va bu effekt radius bo'ylab "
                "o'zgaradi. Bu masalani statika usullari bilan yechish mumkinmi?"
            ),
            concepts=[
                c("Inersiya kuchi", "$\\mathbf{F}^{in} = -m\\mathbf{a}$ — matematik "
                  "qulaylik uchun kiritiladigan fiktiv kuch. Real jismga qo'yilmaydi, "
                  "faqat hisob sxemasida ishlatiladi."),
                c("D'Alembert prinsipi", "Faol kuchlar, reaksiyalar va inersiya "
                  "kuchlari birgalikda muvozanatlashgan sistemani tashkil qiladi."),
                c("Kinetostatika", "Dinamik masalani statik usullar bilan yechish "
                  "metodikasi. Muhandislik hisoblarida keng qo'llaniladi."),
                c("Inersiya kuchlarining keltirilishi", "Jism uchun: "
                  "$\\mathbf{R}^{in} = -M\\mathbf{a}_C$, $\\mathbf{M}^{in}_C = -J_C\\boldsymbol{\\varepsilon}$."),
                c("D'Alembert–Lagranj tenglamasi", "$\\sum(\\mathbf{F}_i - m_i\\mathbf{a}_i)\\cdot"
                  "\\delta\\mathbf{r}_i = 0$ — dinamikaning umumiy tenglamasi."),
            ],
            derivation=[
                d("1-qadam. Nyuton tenglamasini qayta guruhlash",
                  r"m_i\mathbf{a}_i = \mathbf{F}_i + \mathbf{R}_i \;\Rightarrow\; "
                  r"\mathbf{F}_i + \mathbf{R}_i + \underbrace{(-m_i\mathbf{a}_i)}_{\mathbf{F}_i^{in}} = 0",
                  "Formal o'tkazish. Endi tenglama muvozanat shartiga o'xshaydi — "
                  "aynan shu D'Alembert g'oyasining mohiyati."),
                d("2-qadam. Jism uchun inersiya kuchlarini keltirish",
                  r"\mathbf{R}^{in} = -M\mathbf{a}_C,\qquad \mathbf{M}_C^{in} = -J_C\boldsymbol{\varepsilon}",
                  "Taqsimlangan inersiya kuchlari bosh vektor va bosh momentga "
                  "keltiriladi (nm-11 dagi keltirish nazariyasi)."),
                d("3-qadam. Aylanuvchi sterjendagi taqsimlangan inersiya kuchi",
                  r"dF^{in} = \omega^2 r\,dm = \omega^2 r\,\rho A\,dr \;\Rightarrow\; "
                  r"q^{in}(r) = \rho A\omega^2 r",
                  "Markazdan qochma inersiya kuchi radius bo'ylab chiziqli o'sadi — "
                  "uchburchak epyura."),
                d("4-qadam. Eguvchi momentni integrallash",
                  r"M(r) = \int_r^L q^{in}(\xi)(\xi - r)\,d\xi = \rho A\omega^2\left("
                  r"\frac{L^3}{6} - \frac{L^2 r}{2} + \frac{r^3}{3}\right)",
                  "Har bir elementar kuchning momentini jamlash. $r = 0$ da "
                  "$M_{max} = \\rho A\\omega^2 L^3/6$."),
                d("5-qadam. D'Alembert–Lagranj tenglamasi",
                  r"\sum_i(\mathbf{F}_i - m_i\mathbf{a}_i)\cdot\delta\mathbf{r}_i = 0 "
                  r"\;\Rightarrow\; Q_j - \sum_i m_i\mathbf{a}_i\cdot\frac{\partial\mathbf{r}_i}{\partial q_j} = 0",
                  "Virtual ishlar prinsipini inersiya kuchlariga qo'llash. Bu tenglama "
                  "keyingi mavzuda Lagranj tenglamalariga aylantiriladi."),
            ],
            formula_meaning=(
                "D'Alembert prinsipi fizik jihatdan yangi narsa qo'shmaydi — bu Nyuton "
                "tenglamasining qayta yozilishi. Lekin metodologik foydasi juda katta: "
                "butun statika apparati (epyuralar, muvozanat tenglamalari, virtual "
                "ishlar) dinamik masalalarga qo'llanadigan bo'ladi. Muhandislik "
                "hisoblarida dinamiklik koeffitsienti aynan shu yondashuvdan tug'iladi."
            ),
            equations=[
                eq(r"\mathbf{F} + \mathbf{R} + \mathbf{F}^{in} = 0", "D'Alembert prinsipi.",
                   "D'Alembert prinsipi"),
                eq(r"\mathbf{R}^{in} = -M\mathbf{a}_C,\quad \mathbf{M}^{in}_C = -J_C\boldsymbol{\varepsilon}",
                   "Inersiya kuchlarining keltirilishi.", "Keltirish"),
                eq(r"\sum_i(\mathbf{F}_i - m_i\mathbf{a}_i)\cdot\delta\mathbf{r}_i = 0",
                   "Dinamikaning umumiy tenglamasi.", "D'Alembert–Lagranj"),
            ],
            conditions=(
                "Inersiya kuchi faqat hisob sxemasida mavjud — uni erkin jism "
                "diagrammasiga qo'shish D'Alembert usulini qo'llaganda to'g'ri, lekin "
                "sof Nyuton usulida xato. Bu ikki yondashuvni aralashtirmaslik kerak. "
                "Inersiya kuchining yo'nalishi har doim tezlanishga qarama-qarshi."
            ),
            worked_example=WorkedExample(
                statement=(
                    "Sentrifuga roterining radial sterjeni: uzunlik $L = 0{,}35$ m, "
                    "kesim $A = 3\\times 10^{-4}$ m², material po'lat "
                    "($\\rho = 7850$ kg/m³). Rotor $n = 6000$ ayl/min. Ildizdagi "
                    "(o'qdagi) bo'ylama kuch va eguvchi momentni toping."
                ),
                given=[r"L = 0{,}35\ \text{m},\; A = 3\cdot 10^{-4}\ \text{m}^2",
                       r"\rho = 7850\ \text{kg/m}^3,\; n = 6000\ \text{ayl/min}"],
                steps=[
                    st(r"\omega = \frac{\pi n}{30} = \frac{\pi\cdot 6000}{30} = 628{,}3\ \text{rad/s}",
                       "Burchak tezligi."),
                    st(r"q^{in}(r) = \rho A\omega^2 r = 7850\cdot 3\cdot10^{-4}\cdot 394\,784\cdot r = "
                       r"929\,818\,r\ \text{N/m}",
                       "Taqsimlangan inersiya kuchi (r — metrda)."),
                    st(r"N(0) = \int_0^L q^{in}dr = \frac{\rho A\omega^2L^2}{2} = "
                       r"\frac{929\,818\cdot 0{,}1225}{2} = 56\,951\ \text{N}",
                       "Ildizdagi bo'ylama (markazdan qochma) kuch ≈ 57 kN."),
                    st(r"\sigma = \frac{N}{A} = \frac{56\,951}{3\cdot 10^{-4}} = 190\ \text{MPa}",
                       "Cho'zuvchi kuchlanish — po'lat uchun sezilarli, lekin qabul qilinadigan."),
                    st(r"M_{max} = \frac{\rho A\omega^2 L^3}{6}\cdot\frac{g}{\omega^2 L}\ \text{(og'irlikdan)} "
                       r"= \frac{\rho A g L^2}{2} = \frac{7850\cdot 3\cdot10^{-4}\cdot 9{,}81\cdot 0{,}1225}{2}",
                       "Eguvchi moment faqat og'irlikdan (inersiya kuchlari radial, "
                       "ular egmaydi)."),
                    st(r"M_{max} = 1{,}41\ \text{N·m} \ll N\cdot\text{ta'siri}",
                       "Xulosa: sterjen amalda faqat cho'zilishga ishlaydi. "
                       "Markazdan qochma kuch og'irlikdan "
                       "$\\omega^2L/g = 394\\,784\\cdot 0{,}35/9{,}81 = 14\\,086$ marta katta."),
                ],
                answer=(
                    "$N = 56{,}95$ kN; $\\sigma = 190$ MPa; og'irlikdan eguvchi moment "
                    "$M = 1{,}41$ N·m (e'tiborga olinmasa ham bo'ladi)."
                ),
                engineering_note=(
                    "Markazdan qochma yuklanish og'irlikdan 14 000 marta katta — shuning "
                    "uchun yuqori tezlikli rotor hisobida og'irlik umuman e'tiborga "
                    "olinmaydi. Lekin kuchlanish 190 MPa — bu nafaqat statik "
                    "mustahkamlik, balki charchash (mq-28) masalasini ham keltirib "
                    "chiqaradi, chunki rotor ishga tushish/to'xtash sikllarini boshdan "
                    "kechiradi."
                ),
            ),
            computation=Computation(
                caption=(
                    "Aylanuvchi sterjen: inersiya kuchlari taqsimoti va ichki kuchlar "
                    "epyuralarini quring."
                ),
                code='''"""D'Alembert prinsipi: aylanuvchi sterjendagi inersiya kuchlari."""
import numpy as np
from labkit import PARAMS, note, series, table, value

L = float(PARAMS.get("L", 0.35))         # sterjen uzunligi, m
A = float(PARAMS.get("A", 3e-4))         # kesim yuzasi, m^2
rho = float(PARAMS.get("rho", 7850.0))   # zichlik, kg/m^3
n_rpm = float(PARAMS.get("n_rpm", 6000)) # ayl/min
g = 9.81

omega = np.pi*n_rpm/30
r = np.linspace(0, L, 200)

# Taqsimlangan inersiya kuchi (markazdan qochma), N/m
q_in = rho*A*omega**2*r
# Bo'ylama kuch: r nuqtadan uchigacha integrallash
N = rho*A*omega**2*(L**2 - r**2)/2
sigma = N/A

series("Inersiya kuchi q(r)", r.tolist(), (q_in/1000).tolist(),
       xlabel="r, m", ylabel="q, kN/m")
series("Bo'ylama kuch N(r)", r.tolist(), (N/1000).tolist(),
       xlabel="r, m", ylabel="N, kN")
series("Kuchlanish σ(r)", r.tolist(), (sigma/1e6).tolist(),
       xlabel="r, m", ylabel="σ, MPa")

value("ω", omega, "rad/s")
value("N ildizda", float(N[0])/1000, "kN")
value("σ_max", float(sigma[0])/1e6, "MPa")
value("Massa", rho*A*L, "kg")
value("a_n uchida", omega**2*L, "m/s²")
value("a_n / g", omega**2*L/g, "—")

# Og'irlikdan eguvchi moment (taqqoslash uchun)
M_grav = rho*A*g*L**2/2
value("M (og'irlikdan)", M_grav, "N·m")
note(f"Markazdan qochma kuch og'irlikdan {omega**2*L/g:.0f} marta katta — "
     f"yuqori tezlikli rotorlarda og'irlik e'tiborga olinmaydi.")

# Aylanishlar soniga bog'liqlik
nn = np.linspace(500, 15000, 200)
sig = rho*(np.pi*nn/30)**2*L**2/2/1e6
series("σ_max(n)", nn.tolist(), sig.tolist(), xlabel="n, ayl/min", ylabel="σ_max, MPa")

sigma_allow = 250.0
n_crit = 30/np.pi*np.sqrt(2*sigma_allow*1e6/(rho*L**2))
note(f"[σ] = {sigma_allow} MPa uchun ruxsat etilgan maksimal aylanish: "
     f"{n_crit:.0f} ayl/min")

table("Aylanishlar soniga bog'liqlik", ["n, ayl/min", "σ_max, MPa", "N, kN"],
      [[float(x), float(rho*(np.pi*x/30)**2*L**2/2/1e6),
        float(rho*A*(np.pi*x/30)**2*L**2/2/1000)] for x in (3000, 6000, 9000, 12000)])
''',
                parameters=[
                    p("L", "Sterjen uzunligi L", 0.05, 1.0, 0.35, 0.05, "m"),
                    p("A", "Kesim yuzasi A", 5e-5, 2e-3, 3e-4, 5e-5, "m²"),
                    p("rho", "Zichlik ρ", 1000.0, 20000.0, 7850.0, 100.0, "kg/m³"),
                    p("n_rpm", "Aylanishlar soni", 500.0, 20000.0, 6000.0, 250.0, "ayl/min"),
                ],
                expected_output="ω = 628,3 rad/s, N = 56,95 kN, σ_max = 190 MPa",
            ),
            visualization=vis(
                "Inersiya kuchlari epyurasi",
                "React/SVG",
                "Sterjen sxemasi, unga taqsimlangan inersiya kuchi uchburchak epyurasi, "
                "ostida $N(r)$ parabolik epyurasi va $\\sigma(r)$ grafigi.",
                "React/SVG: epyura — mexanika chizmalarining klassik elementi. "
                "Taqsimlangan yuklamani strelkalar qatori bilan, ichki kuchni bo'yalgan "
                "soha bilan chizing. Bu `Epyura` komponenti mq-12 da balka uchun "
                "to'liq qayta ishlatiladi.",
            ),
            interpretation=(
                "Inersiya kuchi chiziqli, bo'ylama kuch parabolik — bu integrallashning "
                "tabiiy natijasi. Kuchlanish ildizda maksimal, uchida nol: shuning "
                "uchun rotor kurakchalari ildizga qarab qalinlashtiriladi. "
                "$\\sigma(n)$ grafigi kvadratik: aylanishni 2 marta oshirish "
                "kuchlanishni 4 marta oshiradi, demak ruxsat etilgan tezlik materialning "
                "mustahkamligi bilan qat'iy chegaralangan."
            ),
            common_mistakes=[
                "Inersiya kuchini Nyuton tenglamasidagi erkin jism diagrammasiga "
                "qo'shish — bu ikki marta hisoblash bo'ladi.",
                "Inersiya kuchining yo'nalishini tezlanish bilan bir tomonga qo'yish. "
                "U qarama-qarshi yo'naladi.",
                "Aylanuvchi jismda $J_C\\varepsilon$ momentini unutish (tekis "
                "tezlanuvchi aylanishda).",
                "Taqsimlangan inersiya kuchini o'rtacha qiymat bilan almashtirish — "
                "u chiziqli taqsimlangan, integrallash kerak.",
            ],
            quiz=[
                q("Inersiya kuchi 'haqiqiy' kuchmi?",
                  "Inersial sanoq sistemasida — yo'q, u hisob usuli. Noinersial "
                  "sistemada esa u kuzatuvchi uchun haqiqiy ta'sirga o'xshaydi. "
                  "Muhim: uning reaksiyasi (uchinchi qonun bo'yicha juftligi) yo'q.",
                  "konseptual"),
                q("D'Alembert prinsipining asosiy metodologik foydasi nima?",
                  "Statika apparatini (epyuralar, muvozanat tenglamalari, virtual "
                  "ishlar) dinamik masalalarga qo'llash imkonini beradi.", "konseptual"),
                q("$m = 5$ kg, $a = 3$ m/s². Inersiya kuchi qancha va qayerga yo'nalgan?",
                  "$F^{in} = 15$ N, tezlanishga qarama-qarshi.", "hisob"),
                q("Aylanishlar sonini 1,5 marta oshirsak, kuchlanish qanday o'zgaradi?",
                  "$1{,}5^2 = 2{,}25$ marta ortadi.", "hisob"),
                q("Kodda `N = rho*A*omega**2*(L**2 - r**2)/2` formulasi qayerdan keldi?",
                  "$N(r) = \\int_r^L \\rho A\\omega^2\\xi\\,d\\xi = \\rho A\\omega^2(L^2-r^2)/2$ "
                  "— $r$ dan uchigacha bo'lgan qismning inersiya kuchlari yig'indisi.",
                  "kod"),
            ],
            bridge_to_next=(
                "D'Alembert–Lagranj tenglamasi olindi, lekin undagi "
                "$\\sum m_i\\mathbf{a}_i\\cdot\\partial\\mathbf{r}_i/\\partial q_j$ hadi "
                "noqulay. Keyingi mavzuda uni kinetik energiya orqali qayta yozamiz — "
                "va Lagranj tenglamalari tug'iladi."
            ),
            research_extension=(
                "Teng mustahkamlikdagi aylanuvchi disk profilini toping: qalinlik "
                "$h(r)$ ni shunday tanlangki, $\\sigma = \\text{const}$ bo'lsin. "
                "Muvozanat tenglamasidan differensial tenglama chiqadi; uni yeching va "
                "eksponensial profil olinishini ko'rsating. Bu — turbina disklarining "
                "real shakli."
            ),
        ),
    ),
    Topic(
        id="nm-22",
        subject_id=S,
        module_id=M,
        order=22,
        title="Lagranj funksiyasi va ikkinchi tur Lagranj tenglamalari",
        description=(
            "Kinetik energiyani umumlashgan koordinatalarda ifodalash, Lagranj "
            "tenglamalarini keltirib chiqarish va murakkab tizimlarga qo'llash."
        ),
        learning_objective=(
            "Ixtiyoriy golonom tizim uchun Lagranj funksiyasini tuzib, harakat "
            "tenglamalarini avtomatik olish."
        ),
        prerequisites=["nm-21", "nm-15"],
        mathematical_core=(
            "Qisman hosilalar, $\\frac{d}{dt}\\frac{\\partial L}{\\partial\\dot q} - "
            "\\frac{\\partial L}{\\partial q} = 0$, kinetik energiyaning kvadratik formasi."
        ),
        engineering_application=(
            "Ko'p bo'g'inli manipulyator dinamikasi, tebranish tizimlari, "
            "avtomobil podveskasi modeli."
        ),
        computational_component=(
            "SymPy bilan Lagranj tenglamalarini avtomatik keltirib chiqarish va "
            "sonli integrallash."
        ),
        visualization_component=(
            "Ikki karrali mayatnik traektoriyasi va energiya balansi grafigi."
        ),
        research_extension=(
            "Ikki karrali mayatnik xaotik tizim. Boshlang'ich shartlarga "
            "sezgirlikni miqdoriy o'lchang (Lyapunov ko'rsatkichi)."
        ),
        difficulty="ilg'or",
        previous_link=(
            "nm-21 dagi D'Alembert–Lagranj tenglamasidagi noqulay hadni kinetik "
            "energiya orqali qayta yozamiz. Natijada harakat tenglamalarini "
            "'retsept' bo'yicha olish mumkin bo'ladi."
        ),
        next_topic="nm-23",
        estimated_minutes=110,
        tags=["Lagranj tenglamalari", "analitik mexanika", "mayatnik"],
        lesson=Lesson(
            physical_problem=(
                "Ikki bo'g'inli robot qo'lining harakat tenglamalarini Nyuton usulida "
                "yozish uchun har bir bo'g'in uchun 3 ta tenglama, sharnirlarda "
                "4 ta noma'lum reaksiya — jami 6 ta tenglama va 6 ta noma'lum kerak. "
                "Lagranj usulida esa faqat 2 ta tenglama, hech qanday reaksiyasiz. "
                "Va bu usul 6 bo'g'inli robotda ham xuddi shunday ishlaydi."
            ),
            concepts=[
                c("Lagranj funksiyasi", "$L = T - \\Pi$ — kinetik va potensial "
                  "energiyalar ayirmasi. Tizim haqidagi butun ma'lumotni saqlaydi."),
                c("Umumlashgan tezlik", "$\\dot q_j$ — umumlashgan koordinataning vaqt "
                  "bo'yicha hosilasi."),
                c("Umumlashgan impuls", "$p_j = \\partial L/\\partial\\dot q_j$ — "
                  "Lagranj funksiyasining tezlik bo'yicha hosilasi."),
                c("Kinetik energiya strukturasi", "Skleronom tizimda "
                  "$T = \\tfrac{1}{2}\\sum a_{jk}(q)\\dot q_j\\dot q_k$ — tezliklarning "
                  "kvadratik formasi; $a_{jk}$ — inersiya matritsasi."),
                c("Dissipativ funksiya", "$\\Phi = \\tfrac{1}{2}\\sum c_{jk}\\dot q_j\\dot q_k$ "
                  "— ishqalanishni hisobga olish uchun; tenglamaga "
                  "$+\\partial\\Phi/\\partial\\dot q_j$ hadi qo'shiladi."),
            ],
            derivation=[
                d("1-qadam. Tezlikni umumlashgan koordinatalarda ifodalash",
                  r"\mathbf{v}_i = \sum_j\frac{\partial\mathbf{r}_i}{\partial q_j}\dot q_j + "
                  r"\frac{\partial\mathbf{r}_i}{\partial t}",
                  "Zanjir qoidasi. Skleronom tizimda oxirgi had yo'q."),
                d("2-qadam. Asosiy ayniyatlar",
                  r"\frac{\partial\mathbf{v}_i}{\partial\dot q_j} = \frac{\partial\mathbf{r}_i}{\partial q_j},"
                  r"\qquad \frac{d}{dt}\frac{\partial\mathbf{r}_i}{\partial q_j} = \frac{\partial\mathbf{v}_i}{\partial q_j}",
                  "Ikkita 'sehrli' ayniyat — Lagranj keltirib chiqarishning kaliti. "
                  "Birinchisi nuqtalarni 'qisqartirish', ikkinchisi differensiallash "
                  "tartibini almashtirish imkonini beradi."),
                d("3-qadam. Inersiya hadini kinetik energiya orqali yozish",
                  r"\sum_i m_i\mathbf{a}_i\cdot\frac{\partial\mathbf{r}_i}{\partial q_j} = "
                  r"\frac{d}{dt}\frac{\partial T}{\partial\dot q_j} - \frac{\partial T}{\partial q_j}",
                  "Ayniyatlarni qo'llab, $T = \\tfrac{1}{2}\\sum m_iv_i^2$ orqali "
                  "ifodalaymiz. Bu — keltirib chiqarishning markaziy qadami."),
                d("4-qadam. Lagranj tenglamalari (umumiy shakl)",
                  r"\boxed{\;\frac{d}{dt}\frac{\partial T}{\partial\dot q_j} - "
                  r"\frac{\partial T}{\partial q_j} = Q_j,\quad j = 1,\dots,n\;}",
                  "nm-21 dagi D'Alembert–Lagranj tenglamasiga qo'yamiz. "
                  "Reaksiyalar yo'q, faqat umumlashgan kuchlar."),
                d("5-qadam. Potensial kuchlar uchun Lagranj funksiyasi",
                  r"Q_j = -\frac{\partial\Pi}{\partial q_j},\quad \frac{\partial\Pi}{\partial\dot q_j} = 0 "
                  r"\;\Rightarrow\; \boxed{\;\frac{d}{dt}\frac{\partial L}{\partial\dot q_j} - "
                  r"\frac{\partial L}{\partial q_j} = 0,\quad L = T-\Pi\;}",
                  "Eng ixcham shakl. Butun mexanika bitta skalyar funksiyaga siqildi."),
            ],
            formula_meaning=(
                "Lagranj tenglamalari — mexanikaning 'universal retsepti': $T$ va "
                "$\\Pi$ ni yozing, ayirmasini oling, ikkita hosila hisoblang — harakat "
                "tenglamalari tayyor. Reaksiyalar, kuchlar proyeksiyalari, koordinata "
                "o'qlarini tanlash — hech biri kerak emas. Bu yondashuv nafaqat "
                "mexanikada, balki elektrodinamika, kvant mexanikasi va nazariy "
                "fizikaning barcha sohalarida ishlaydi. Hisoblash mexanikasi uchun esa "
                "eng muhimi: $T$ va $\\Pi$ ni approksimatsiya qilish orqali FEM "
                "tenglamalari hosil bo'ladi (su-13, su-18)."
            ),
            equations=[
                eq(r"L = T - \Pi", "Lagranj funksiyasi.", "Lagranjian"),
                eq(r"\frac{d}{dt}\frac{\partial L}{\partial\dot q_j} - \frac{\partial L}{\partial q_j} = 0",
                   "Ikkinchi tur Lagranj tenglamalari (potensial kuchlar).", "Lagranj tenglamalari"),
                eq(r"\frac{d}{dt}\frac{\partial T}{\partial\dot q_j} - \frac{\partial T}{\partial q_j} "
                   r"+ \frac{\partial\Phi}{\partial\dot q_j} = Q_j",
                   "Dissipatsiya bilan umumiy shakl.", "Umumiy shakl"),
            ],
            conditions=(
                "Tenglamalar golonom bog'lanishlar va mustaqil umumlashgan "
                "koordinatalar uchun o'rinli. Boshlang'ich shartlar: $q_j(0)$ va "
                "$\\dot q_j(0)$ — jami $2n$ ta son. Nogolonom bog'lanishlar bo'lsa, "
                "Lagranj ko'paytuvchilari usuli qo'llaniladi."
            ),
            worked_example=WorkedExample(
                statement=(
                    "Arava ustidagi mayatnik (inverted pendulum ning klassik varianti): "
                    "arava massasi $M = 2$ kg gorizontal harakatlanadi ($x$), unga "
                    "uzunligi $l = 0{,}5$ m, massasi $m = 0{,}3$ kg bo'lgan mayatnik "
                    "osilgan ($\\varphi$). Lagranj tenglamalarini keltirib chiqaring."
                ),
                given=[r"M = 2\ \text{kg},\; m = 0{,}3\ \text{kg},\; l = 0{,}5\ \text{m}",
                       r"q_1 = x,\; q_2 = \varphi"],
                steps=[
                    st(r"x_m = x + l\sin\varphi,\qquad y_m = -l\cos\varphi",
                       "Mayatnik massasining koordinatalari umumlashgan koordinatalar orqali."),
                    st(r"\dot x_m = \dot x + l\dot\varphi\cos\varphi,\qquad \dot y_m = l\dot\varphi\sin\varphi",
                       "Differensiallash."),
                    st(r"T = \frac{M\dot x^2}{2} + \frac{m}{2}\left(\dot x^2 + 2l\dot x\dot\varphi\cos\varphi "
                       r"+ l^2\dot\varphi^2\right)",
                       "Kinetik energiya. Diqqat: kesishgan had "
                       "$ml\\dot x\\dot\\varphi\\cos\\varphi$ — aynan u ikki koordinatani bog'laydi."),
                    st(r"\Pi = -mgl\cos\varphi \;\Rightarrow\; L = T - \Pi",
                       "Potensial energiya (pastga musbat hisoblansa)."),
                    st(r"\frac{\partial L}{\partial\dot x} = (M+m)\dot x + ml\dot\varphi\cos\varphi "
                       r"\;\Rightarrow\; (M+m)\ddot x + ml\ddot\varphi\cos\varphi - ml\dot\varphi^2\sin\varphi = 0",
                       "Birinchi tenglama ($x$ siklik koordinata — o'ng tomon nol, "
                       "demak umumlashgan impuls saqlanadi!)."),
                    st(r"ml^2\ddot\varphi + ml\ddot x\cos\varphi + mgl\sin\varphi = 0",
                       "Ikkinchi tenglama. Kichik tebranishlarda ($\\varphi \\ll 1$) u "
                       "$\\ddot\\varphi + (g/l)\\varphi = -\\ddot x/l$ ko'rinishini oladi."),
                ],
                answer=(
                    "$(M+m)\\ddot x + ml\\ddot\\varphi\\cos\\varphi - ml\\dot\\varphi^2\\sin\\varphi = 0$; "
                    "$l\\ddot\\varphi + \\ddot x\\cos\\varphi + g\\sin\\varphi = 0$."
                ),
                engineering_note=(
                    "$x$ koordinata Lagranj funksiyasiga oshkor kirmaydi (faqat $\\dot x$ "
                    "orqali) — bu siklik koordinata va unga mos umumlashgan impuls "
                    "(gorizontal impuls) saqlanadi. Bu natijani Nyuton usulida olish "
                    "uchun alohida mulohaza kerak edi; Lagranj usulida esa u "
                    "avtomatik ko'rinadi (nm-23)."
                ),
            ),
            computation=Computation(
                caption=(
                    "Ikki karrali mayatnik: Lagranj tenglamalarini SymPy avtomatik "
                    "keltirib chiqaradi va sonli integrallaydi."
                ),
                code='''"""Lagranj tenglamalarini avtomatik keltirib chiqarish va yechish."""
import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp
from labkit import PARAMS, note, series, value

m1 = float(PARAMS.get("m1", 1.0))     # 1-mayatnik massasi, kg
m2 = float(PARAMS.get("m2", 1.0))     # 2-mayatnik massasi, kg
l1 = float(PARAMS.get("l1", 1.0))     # 1-bo'g'in uzunligi, m
l2 = float(PARAMS.get("l2", 1.0))     # 2-bo'g'in uzunligi, m
th1_0 = float(PARAMS.get("th1", 120.0))  # boshlang'ich burchak, deg
th2_0 = float(PARAMS.get("th2", 60.0))
g = 9.81

# --- Simvolik: Lagranj tenglamalarini avtomatik olish ---
t = sp.symbols("t")
q1 = sp.Function("q1")(t)
q2 = sp.Function("q2")(t)
M1, M2, L1, L2, G = sp.symbols("m1 m2 l1 l2 g", positive=True)

x1 = L1*sp.sin(q1);            y1 = -L1*sp.cos(q1)
x2 = x1 + L2*sp.sin(q2);       y2 = y1 - L2*sp.cos(q2)
v1sq = sp.diff(x1, t)**2 + sp.diff(y1, t)**2
v2sq = sp.diff(x2, t)**2 + sp.diff(y2, t)**2

T = M1*v1sq/2 + M2*v2sq/2
Pi = M1*G*y1 + M2*G*y2
Lag = sp.simplify(T - Pi)

eqs = []
for qi in (q1, q2):
    eqs.append(sp.simplify(sp.diff(sp.diff(Lag, sp.diff(qi, t)), t) - sp.diff(Lag, qi)))
note("Lagranj tenglamalari simvolik keltirib chiqarildi (2 ta ikkinchi tartibli ODE).")

# Tezlanishlarga nisbatan yechish
acc = sp.solve(eqs, [sp.diff(q1, t, 2), sp.diff(q2, t, 2)], dict=True)[0]
subs = {M1: m1, M2: m2, L1: l1, L2: l2, G: g}
f1 = sp.lambdify((q1, q2, sp.diff(q1, t), sp.diff(q2, t)),
                 acc[sp.diff(q1, t, 2)].subs(subs), "numpy")
f2 = sp.lambdify((q1, q2, sp.diff(q1, t), sp.diff(q2, t)),
                 acc[sp.diff(q2, t, 2)].subs(subs), "numpy")

def rhs(tt, y):
    a1, a2, w1, w2 = y
    return [w1, w2, float(f1(a1, a2, w1, w2)), float(f2(a1, a2, w1, w2))]

y0 = [np.radians(th1_0), np.radians(th2_0), 0.0, 0.0]
sol = solve_ivp(rhs, (0, 20), y0, rtol=1e-10, atol=1e-12, dense_output=True, max_step=0.01)
tt = np.linspace(0, 20, 2000)
a1, a2, w1, w2 = sol.sol(tt)

X2 = l1*np.sin(a1) + l2*np.sin(a2)
Y2 = -l1*np.cos(a1) - l2*np.cos(a2)
series("Ikkinchi mayatnik traektoriyasi", X2.tolist(), Y2.tolist(),
       xlabel="x, m", ylabel="y, m")
series("Burchak θ₁(t)", tt.tolist(), np.degrees(a1).tolist(), xlabel="t, s", ylabel="θ₁, deg")
series("Fazaviy portret (θ₁, ω₁)", np.degrees(a1).tolist(), w1.tolist(),
       xlabel="θ₁, deg", ylabel="ω₁, rad/s")

# Energiya saqlanishini tekshirish — sonli yechim sifati mezoni
v1s = (l1*w1)**2
v2s = (l1*w1)**2 + (l2*w2)**2 + 2*l1*l2*w1*w2*np.cos(a1-a2)
E = m1*v1s/2 + m2*v2s/2 - m1*g*l1*np.cos(a1) - m2*g*(l1*np.cos(a1)+l2*np.cos(a2))
series("To'la energiya E(t)", tt.tolist(), E.tolist(), xlabel="t, s", ylabel="E, J")
value("E boshlang'ich", float(E[0]), "J")
value("E drift (maks. farq)", float(np.max(np.abs(E-E[0]))), "J")
value("Nisbiy drift", float(np.max(np.abs(E-E[0]))/abs(E[0])*100), "%")
note("Energiya drifti kichik bo'lsa, sonli integrallash ishonchli (su-10).")

# Xaosga sezgirlik
y0b = [y0[0]+1e-6, y0[1], 0.0, 0.0]
solb = solve_ivp(rhs, (0, 20), y0b, rtol=1e-10, atol=1e-12, dense_output=True, max_step=0.01)
diff = np.abs(solb.sol(tt)[0] - a1)
series("Boshlang'ich farqning o'sishi", tt.tolist(), np.log10(diff+1e-16).tolist(),
       xlabel="t, s", ylabel="log₁₀|Δθ₁|")
note(f"10⁻⁶ rad boshlang'ich farq 20 s da {diff[-1]:.4f} rad ga yetdi — "
     f"{diff[-1]/1e-6:.0f} marta o'sish. Bu xaotik dinamikaning belgisi.")
''',
                parameters=[
                    p("m1", "1-massa m₁", 0.1, 5.0, 1.0, 0.1, "kg"),
                    p("m2", "2-massa m₂", 0.1, 5.0, 1.0, 0.1, "kg"),
                    p("l1", "1-uzunlik l₁", 0.2, 2.0, 1.0, 0.1, "m"),
                    p("l2", "2-uzunlik l₂", 0.2, 2.0, 1.0, 0.1, "m"),
                    p("th1", "Boshlang'ich θ₁", -180.0, 180.0, 120.0, 5.0, "deg"),
                    p("th2", "Boshlang'ich θ₂", -180.0, 180.0, 60.0, 5.0, "deg"),
                ],
                expected_output="Energiya drifti < 0,01 %, xaotik traektoriya, θ₁ farqi eksponensial o'sadi",
            ),
            visualization=vis(
                "Ikki karrali mayatnik va uning traektoriyasi",
                "Manim",
                "Ikki bo'g'inli mayatnik harakati, uchining qoldirgan izi (traektoriya), "
                "yonida energiya ustunlari (T va Π almashib turadi, yig'indi o'zgarmas).",
                "Manim: xaotik harakatni animatsiyada ko'rsatish — bu tushunchani "
                "yetkazishning eng ishonarli yo'li. React/SVG da esa traektoriya, "
                "fazaviy portret va ikki yaqin boshlang'ich shartning ajralishi "
                "grafiklari beriladi.",
            ),
            interpretation=(
                "Energiya drifti $10^{-8}$ J tartibida — bu sonli integrallash "
                "to'g'ri ishlayotganini tasdiqlaydi (fizik jihatdan energiya aynan "
                "saqlanishi kerak). Boshlang'ich farq grafigi esa deyarli to'g'ri "
                "chiziq (logarifmik shkalada) — bu eksponensial ajralish, ya'ni "
                "xaosning miqdoriy belgisi. Muhandislik xulosasi: bunday tizimning "
                "uzoq muddatli xatti-harakatini bashorat qilib bo'lmaydi, faqat "
                "statistik tavsiflash mumkin."
            ),
            common_mistakes=[
                "$T$ ni umumlashgan koordinatalarda emas, Dekart koordinatalarida "
                "qoldirish — tenglamalar chiqmaydi.",
                "$\\frac{d}{dt}\\frac{\\partial L}{\\partial\\dot q}$ da to'la hosilani "
                "qisman hosila bilan almashtirish. Zanjir qoidasi bo'yicha barcha "
                "$q(t)$ va $\\dot q(t)$ larni hisobga olish kerak.",
                "Dissipativ kuchlarni Lagranj funksiyasiga kiritishga urinish — ular "
                "$Q_j$ yoki $\\Phi$ orqali kiritiladi.",
                "Bog'liq koordinatalarni ishlatish (erkinlik darajasidan ko'p koordinata).",
                "Potensial energiyaning nol darajasini tenglama tuzish davomida o'zgartirish.",
            ],
            quiz=[
                q("Nima uchun Lagranj usulida bog'lanish reaksiyalari qatnashmaydi?",
                  "Chunki usul umumlashgan (mustaqil) koordinatalarda ishlaydi va "
                  "D'Alembert–Lagranj tenglamasida ideal bog'lanish reaksiyalarining "
                  "virtual ishi nolga teng.", "konseptual"),
                q("$L = T - \\Pi$ da nima uchun ayirma, yig'indi emas?",
                  "Chunki keltirib chiqarishda $Q_j = -\\partial\\Pi/\\partial q_j$ "
                  "hadi chap tomonga ko'chiriladi va $T$ dan ayiriladi. Fizik jihatdan "
                  "esa ayirma — eng kichik ta'sir prinsipidagi funksional.", "konseptual"),
                q("Oddiy mayatnik uchun ($q = \\varphi$) Lagranj tenglamasini yozing.",
                  "$T = ml^2\\dot\\varphi^2/2$, $\\Pi = -mgl\\cos\\varphi$; "
                  "$ml^2\\ddot\\varphi + mgl\\sin\\varphi = 0$, ya'ni "
                  "$\\ddot\\varphi + (g/l)\\sin\\varphi = 0$.", "hisob"),
                q("Kinetik energiya nima uchun tezliklarning kvadratik formasi?",
                  "Chunki $v_i^2$ tezliklarga kvadratik bog'liq va "
                  "$\\mathbf{v}_i = \\sum(\\partial\\mathbf{r}_i/\\partial q_j)\\dot q_j$ "
                  "chiziqli almashtirish — kvadratik forma saqlanadi.", "talqin"),
                q("Kodda energiya drifti nima uchun tekshiriladi?",
                  "Bu — sonli yechim sifatining mustaqil mezoni. Fizik jihatdan energiya "
                  "saqlanishi kerak; drift katta bo'lsa, integrallash qadami yoki usuli "
                  "noto'g'ri tanlangan.", "kod"),
            ],
            bridge_to_next=(
                "Lagranj tenglamalari harakat tenglamalarini beradi. Lekin ularni "
                "yechmasdan turib ham muhim xulosalar chiqarish mumkin — agar "
                "Lagranj funksiyasida simmetriya bo'lsa. Keyingi mavzu shu haqda."
            ),
            research_extension=(
                "Ikki karrali mayatnik uchun eng katta Lyapunov ko'rsatkichini sonli "
                "hisoblang: ikki yaqin boshlang'ich shartning ajralish tezligi "
                "$\\lambda = \\lim\\frac{1}{t}\\ln\\frac{|\\delta(t)|}{|\\delta_0|}$. "
                "Uni boshlang'ich energiyaning funksiyasi sifatida chizing va qanday "
                "energiyada tizim tartibli harakatdan xaosga o'tishini aniqlang."
            ),
            manim=manim(
                scene="DoublePendulumScene",
                module="manim/scenes/nm_lagrange.py",
                title="Ikki karrali mayatnik va xaos",
                summary="Ikki yaqin boshlang'ich shartdan boshlangan mayatniklar dastlab "
                        "birga harakatlanadi, so'ng butunlay ajralib ketadi.",
            ),
        ),
    ),
    Topic(
        id="nm-23",
        subject_id=S,
        module_id=M,
        order=23,
        title="Siklik koordinatalar, saqlanuvchi kattaliklar va simmetriya prinsipi",
        description=(
            "Siklik koordinata va umumlashgan impulsning saqlanishi, energiya "
            "integrali, Noether teoremasi g'oyasi."
        ),
        learning_objective=(
            "Lagranj funksiyasining simmetriyasidan saqlanuvchi kattaliklarni "
            "aniqlash va ular yordamida masalani soddalashtirish."
        ),
        prerequisites=["nm-22"],
        mathematical_core=(
            "Siklik koordinata sharti $\\partial L/\\partial q = 0$, birinchi "
            "integrallar, Yakobi integrali, o'zgarmaslik (invariantlik)."
        ),
        engineering_application=(
            "Sun'iy yo'ldosh orbitasi, gироskop, markazdan qochma regulyator, "
            "aylanuvchi mashinalarda saqlanuvchi kattaliklar."
        ),
        computational_component=(
            "Markaziy maydondagi harakatni saqlanuvchi kattaliklar orqali bir "
            "erkinlik darajali masalaga keltirish."
        ),
        visualization_component=(
            "Effektiv potensial egri chizig'i va orbita turlari."
        ),
        research_extension=(
            "Noether teoremasini oddiy holda isbotlang: uzluksiz simmetriya → "
            "saqlanuvchi kattalik."
        ),
        difficulty="ilg'or",
        previous_link=(
            "nm-22 dagi arava-mayatnik masalasida $x$ koordinata Lagranj funksiyasiga "
            "oshkor kirmagan edi. Bu tasodif emas — unda chuqur ma'no bor."
        ),
        next_topic="nm-24",
        estimated_minutes=95,
        tags=["siklik koordinata", "Noether", "saqlanish"],
        lesson=Lesson(
            physical_problem=(
                "Sun'iy yo'ldosh Yer atrofida elliptik orbitada harakatlanadi. Uning "
                "harakat tenglamalari nochiziqli va murakkab. Lekin Kepler yana XVII "
                "asrda yo'ldosh radius-vektori teng vaqtlarda teng yuzalarni chizishini "
                "aniqlagan. Bu qonun aslida nima? Javob: markaziy maydon aylanma "
                "simmetriyaga ega, demak impuls momenti saqlanadi — va bu masalani "
                "ikki o'lchovdan bir o'lchovga tushiradi."
            ),
            concepts=[
                c("Siklik koordinata", "$\\partial L/\\partial q_k = 0$ bo'lgan "
                  "koordinata. Unga mos umumlashgan impuls saqlanadi."),
                c("Birinchi integral", "Harakat davomida o'zgarmaydigan "
                  "$f(q, \\dot q) = \\text{const}$ funksiya. Tenglamaning tartibini "
                  "pasaytiradi."),
                c("Yakobi integrali", "$H = \\sum\\dot q_j\\frac{\\partial L}{\\partial\\dot q_j} - L$; "
                  "$\\partial L/\\partial t = 0$ bo'lsa saqlanadi. Skleronom tizimda "
                  "$H = T + \\Pi = E$."),
                c("Effektiv potensial", "$\\Pi_{eff}(r) = \\Pi(r) + \\frac{L_z^2}{2mr^2}$ — "
                  "saqlanuvchi impuls momentini potensialga 'singdirish'."),
                c("Noether teoremasi", "Har bir uzluksiz simmetriyaga bitta saqlanuvchi "
                  "kattalik mos keladi: ko'chirish → impuls, burish → impuls momenti, "
                  "vaqt siljishi → energiya."),
            ],
            derivation=[
                d("1-qadam. Siklik koordinatadan saqlanish qonuni",
                  r"\frac{\partial L}{\partial q_k} = 0 \;\Rightarrow\; "
                  r"\frac{d}{dt}\frac{\partial L}{\partial\dot q_k} = 0 \;\Rightarrow\; "
                  r"p_k = \frac{\partial L}{\partial\dot q_k} = \text{const}",
                  "Lagranj tenglamasidan bevosita. Har bir siklik koordinata bitta "
                  "birinchi integralni beradi."),
                d("2-qadam. Markaziy maydonda Lagranj funksiyasi",
                  r"L = \frac{m}{2}(\dot r^2 + r^2\dot\varphi^2) - \Pi(r)",
                  "Qutb koordinatalarida. $\\varphi$ oshkor kirmaydi — u siklik."),
                d("3-qadam. Impuls momentining saqlanishi",
                  r"p_\varphi = \frac{\partial L}{\partial\dot\varphi} = mr^2\dot\varphi = L_z = \text{const}",
                  "Bu aynan Keplerning ikkinchi qonuni: yuza tezligi "
                  "$dS/dt = r^2\\dot\\varphi/2 = L_z/(2m) = \\text{const}$."),
                d("4-qadam. Radial harakatga keltirish",
                  r"E = \frac{m\dot r^2}{2} + \frac{L_z^2}{2mr^2} + \Pi(r) = "
                  r"\frac{m\dot r^2}{2} + \Pi_{eff}(r)",
                  "$\\dot\\varphi = L_z/(mr^2)$ ni energiyaga qo'yamiz. Ikki o'lchovli "
                  "masala bir o'lchovli harakatga aylandi — bu saqlanish qonunlarining "
                  "hisoblash qudratining eng yorqin misoli."),
                d("5-qadam. Orbita turlarini aniqlash",
                  r"\Pi_{eff}(r) = -\frac{GMm}{r} + \frac{L_z^2}{2mr^2};\qquad "
                  r"E < 0 \Rightarrow \text{ellips},\; E = 0 \Rightarrow \text{parabola},\; "
                  r"E > 0 \Rightarrow \text{giperbola}",
                  "nm-15 dagi potensial chuqurcha tahlili to'g'ridan-to'g'ri qo'llanadi: "
                  "$E < 0$ bo'lsa harakat chegaralangan."),
            ],
            formula_meaning=(
                "Siklik koordinata — bu tizimning 'befarq' yo'nalishi: uni o'zgartirish "
                "fizikani o'zgartirmaydi. Va aynan shu befarqlik saqlanuvchi kattalikni "
                "yaratadi. Effektiv potensial esa saqlanuvchi kattalikni potensialga "
                "'yashirish' orqali masalani soddalashtirish texnikasi — "
                "$L_z^2/(2mr^2)$ hadi 'markazdan qochma to'siq' bo'lib, jismning "
                "markazga tushishiga to'sqinlik qiladi."
            ),
            equations=[
                eq(r"p_k = \frac{\partial L}{\partial\dot q_k} = \text{const}",
                   "Siklik koordinataga mos saqlanish qonuni.", "Umumlashgan impuls"),
                eq(r"H = \sum_j\dot q_j\frac{\partial L}{\partial\dot q_j} - L = E",
                   "Yakobi (energiya) integrali.", "Energiya integrali"),
                eq(r"\Pi_{eff}(r) = \Pi(r) + \frac{L_z^2}{2mr^2}", "Effektiv potensial.",
                   "Effektiv potensial"),
            ],
            conditions=(
                "Energiya integrali $\\partial L/\\partial t = 0$ (skleronom tizim) "
                "shartida mavjud. Reonom tizimda (vaqtga bog'liq bog'lanish) $H$ "
                "saqlanadi, lekin u to'la energiyaga teng bo'lmasligi mumkin. "
                "Dissipativ kuchlar bo'lsa, hech qanday energiya integrali yo'q."
            ),
            worked_example=WorkedExample(
                statement=(
                    "Sun'iy yo'ldosh Yer atrofida: perigey balandligi $h_p = 400$ km, "
                    "apogey $h_a = 1200$ km. Yer radiusi $R_E = 6371$ km, "
                    "$GM = 3{,}986\\times 10^{14}$ m³/s². Perigey va apogeydagi "
                    "tezliklarni saqlanish qonunlari orqali toping."
                ),
                given=[r"r_p = 6771\ \text{km},\; r_a = 7571\ \text{km}",
                       r"GM = 3{,}986\cdot 10^{14}\ \text{m}^3/\text{s}^2"],
                steps=[
                    st(r"L_z/m = r_pv_p = r_av_a \;\Rightarrow\; v_a = v_p\frac{r_p}{r_a}",
                       "Impuls momenti saqlanishi (perigey va apogeyda tezlik radiusga "
                       "perpendikular)."),
                    st(r"E/m = \frac{v_p^2}{2} - \frac{GM}{r_p} = \frac{v_a^2}{2} - \frac{GM}{r_a}",
                       "Energiya saqlanishi."),
                    st(r"\frac{v_p^2}{2}\left(1 - \frac{r_p^2}{r_a^2}\right) = GM\left(\frac{1}{r_p}-\frac{1}{r_a}\right)",
                       "$v_a$ ni yo'qotamiz."),
                    st(r"v_p = \sqrt{\frac{2GM\,r_a}{r_p(r_p+r_a)}} = "
                       r"\sqrt{\frac{2\cdot 3{,}986\cdot10^{14}\cdot 7{,}571\cdot10^6}{6{,}771\cdot10^6\cdot 1{,}4342\cdot10^7}}",
                       "Algebraik soddalashtirishdan keyin."),
                    st(r"v_p = \sqrt{6{,}215\cdot 10^7} = 7884\ \text{m/s} = 7{,}88\ \text{km/s}",
                       "Perigeydagi tezlik."),
                    st(r"v_a = 7884\cdot\frac{6771}{7571} = 7051\ \text{m/s} = 7{,}05\ \text{km/s}",
                       "Apogeydagi tezlik — 10,6 % kichik."),
                ],
                answer="$v_p = 7{,}88$ km/s; $v_a = 7{,}05$ km/s.",
                engineering_note=(
                    "Bu hisob differensial tenglamani umuman yechmasdan bajarildi — "
                    "faqat ikkita saqlanish qonuni yetarli bo'ldi. Amaliy jihatdan bu "
                    "orbital manevrlar hisobining asosi: Gomann uzatmasida ham xuddi "
                    "shu tenglamalar ishlatiladi."
                ),
            ),
            computation=Computation(
                caption=(
                    "Markaziy maydondagi harakat: impuls momenti va energiyani "
                    "o'zgartirib, orbita turini aniqlang."
                ),
                code='''"""Siklik koordinatalar, saqlanuvchi kattaliklar va effektiv potensial."""
import numpy as np
from scipy.integrate import solve_ivp
from labkit import PARAMS, note, series, table, value

GM = 3.986e14                             # m^3/s^2
h_p = float(PARAMS.get("h_p", 400.0))     # perigey balandligi, km
h_a = float(PARAMS.get("h_a", 1200.0))    # apogey balandligi, km
R_E = 6371.0

r_p = (R_E + h_p)*1000
r_a = (R_E + h_a)*1000
v_p = np.sqrt(2*GM*r_a/(r_p*(r_p+r_a)))
v_a = v_p*r_p/r_a

value("Perigey tezligi v_p", v_p/1000, "km/s")
value("Apogey tezligi v_a", v_a/1000, "km/s")
value("Solishtirma impuls momenti", v_p*r_p/1e9, "10⁹ m²/s")
E_spec = v_p**2/2 - GM/r_p
value("Solishtirma energiya", E_spec/1e6, "MJ/kg")

a_semi = (r_p+r_a)/2
T_orbit = 2*np.pi*np.sqrt(a_semi**3/GM)
value("Katta yarim o'q a", a_semi/1000, "km")
value("Orbita davri", T_orbit/60, "min")
value("Ekssentrisitet e", (r_a-r_p)/(r_a+r_p), "—")

# Effektiv potensial
Lz = v_p*r_p
r = np.linspace(0.5*r_p, 4*r_a, 600)
U_eff = -GM/r + Lz**2/(2*r**2)
series("Effektiv potensial Π_eff(r)", (r/1e6).tolist(), (U_eff/1e6).tolist(),
       xlabel="r, 10³ km", ylabel="Π_eff, MJ/kg")
series("To'la energiya E", (r/1e6).tolist(),
       np.full_like(r, E_spec/1e6).tolist(), xlabel="r, 10³ km", ylabel="MJ/kg")

r_circ = Lz**2/GM
note(f"Effektiv potensial minimumi (doiraviy orbita) r = {r_circ/1000:.0f} km")
note("E < 0 -> ellips (bog'langan orbita); E = 0 -> parabola; E > 0 -> giperbola. "
     f"Hozirgi holda E = {E_spec/1e6:.3f} MJ/kg -> "
     f"{'ellips' if E_spec < 0 else 'ochiq orbita'}")

# Sonli integrallash va saqlanuvchi kattaliklarni tekshirish
def rhs(t, y):
    x, yy, vx, vy = y
    r3 = (x*x + yy*yy)**1.5
    return [vx, vy, -GM*x/r3, -GM*yy/r3]

sol = solve_ivp(rhs, (0, 2*T_orbit), [r_p, 0, 0, v_p], rtol=1e-11, atol=1e-6,
                dense_output=True, max_step=10.0)
tt = np.linspace(0, 2*T_orbit, 2000)
X, Y, VX, VY = sol.sol(tt)
series("Orbita", (X/1e6).tolist(), (Y/1e6).tolist(), xlabel="x, 10³ km", ylabel="y, 10³ km")

Lz_num = X*VY - Y*VX
E_num = (VX**2+VY**2)/2 - GM/np.sqrt(X**2+Y**2)
note(f"L_z saqlanishi: nisbiy drift {np.ptp(Lz_num)/abs(Lz_num[0])*100:.2e} %")
note(f"E saqlanishi:   nisbiy drift {np.ptp(E_num)/abs(E_num[0])*100:.2e} %")

table("Simmetriya va saqlanish (Noether)",
      ["Simmetriya", "Saqlanuvchi kattalik", "Shart"],
      [["Fazoda ko'chirish", "Impuls P", "Π bir jinsli fazoda"],
       ["Burish", "Impuls momenti L", "Markaziy maydon"],
       ["Vaqt bo'yicha siljish", "Energiya E", "∂L/∂t = 0"]])
''',
                parameters=[
                    p("h_p", "Perigey balandligi", 200.0, 20000.0, 400.0, 50.0, "km"),
                    p("h_a", "Apogey balandligi", 200.0, 40000.0, 1200.0, 100.0, "km"),
                ],
                expected_output="v_p = 7,88 km/s; v_a = 7,05 km/s; davr ≈ 100 min; e ≈ 0,056",
            ),
            visualization=vis(
                "Effektiv potensial va orbita turlari",
                "React/SVG",
                "$\\Pi_{eff}(r)$ egri chizig'i, unda turli $E$ darajalarining "
                "gorizontal chiziqlari; har bir daraja uchun mos orbita (doira, ellips, "
                "parabola, giperbola) yonida chizilgan.",
                "React/SVG: nm-15 dagi potensial chuqurcha komponentini qayta ishlating "
                "— bu izchillikni ta'minlaydi va talabaga 'bu tanish struktura' degan "
                "signalni beradi. $E$ ni slider bilan o'zgartirganda orbita turi "
                "real vaqtda almashadi.",
            ),
            interpretation=(
                "Sonli integrallashda $L_z$ va $E$ ning drifti $10^{-10}$ % tartibida — "
                "bu saqlanish qonunlarining sonli tasdig'i va integratorning sifat "
                "mezoni. Effektiv potensial minimumi doiraviy orbitaga mos keladi; "
                "undan biroz og'ish elliptik orbitani beradi. $L_z \\to 0$ da "
                "markazdan qochma to'siq yo'qoladi va jism markazga tushadi."
            ),
            common_mistakes=[
                "Siklik koordinatani 'davriy koordinata' deb tushunish. Siklik — "
                "Lagranj funksiyasiga oshkor kirmaydigan degani.",
                "$H = E$ ni har doim to'g'ri deb hisoblash. Bu faqat skleronom "
                "tizimda va potensial tezlikka bog'liq bo'lmaganda o'rinli.",
                "Effektiv potensialda markazdan qochma hadning ishorasini "
                "noto'g'ri qo'yish — u musbat (to'siq).",
                "Impuls momenti saqlanishini markaziy bo'lmagan maydonda qo'llash.",
            ],
            quiz=[
                q("Keplerning ikkinchi qonuni qaysi saqlanish qonunining natijasi?",
                  "Impuls momentining saqlanishi: $L_z = mr^2\\dot\\varphi = \\text{const}$, "
                  "demak yuza tezligi $dS/dt = L_z/(2m)$ o'zgarmas.", "konseptual"),
                q("Noether teoremasiga ko'ra vaqt bo'yicha siljish simmetriyasi nimani beradi?",
                  "Energiyaning saqlanishini.", "konseptual"),
                q("$r_p = 7000$ km, $r_a = 10\\,000$ km. $v_a/v_p$ nisbati?",
                  "$v_a/v_p = r_p/r_a = 0{,}7$.", "hisob"),
                q("Nima uchun effektiv potensialga o'tish masalani soddalashtiradi?",
                  "Ikki o'lchovli masala bir o'lchovli radial harakatga keladi, "
                  "$\\varphi$ esa saqlanuvchi $L_z$ orqali tiklanadi.", "talqin"),
                q("Kodda `Lz_num = X*VY - Y*VX` nima?",
                  "Solishtirma impuls momenti ($\\mathbf{r}\\times\\mathbf{v}$ ning "
                  "z komponentasi). Uning o'zgarmasligi integratorning to'g'ri "
                  "ishlayotganini tasdiqlaydi.", "kod"),
            ],
            bridge_to_next=(
                "Lagranj formalizmi koordinatalar va tezliklar bilan ishlaydi. "
                "Gamilton esa tezliklar o'rniga impulslarni asosiy o'zgaruvchi qilib "
                "oladi — va bu geometrik jihatdan boyroq manzara ochadi."
            ),
            research_extension=(
                "Noether teoremasini oddiy holda isbotlang: agar $L$ "
                "$q \\to q + \\epsilon$ almashtirishda o'zgarmasa, "
                "$\\partial L/\\partial q = 0$, demak $p$ saqlanadi. So'ngra "
                "buriladigan simmetriya uchun ham xuddi shunday keltirib chiqaring va "
                "natijani ko'p zarrali sistemaga umumlashtiring."
            ),
        ),
    ),
    Topic(
        id="nm-24",
        subject_id=S,
        module_id=M,
        order=24,
        title="Gamilton funksiyasi, kanonik tenglamalar va fazaviy fazo",
        description=(
            "Lежandr almashtirish, Gamilton funksiyasi, kanonik tenglamalar, "
            "fazaviy fazo va Liuvill teoremasi g'oyasi."
        ),
        learning_objective=(
            "Lagranj formalizmidan Gamilton formalizmiga o'tish va fazaviy portret "
            "orqali harakat turlarini tahlil qilish."
        ),
        prerequisites=["nm-23"],
        mathematical_core=(
            "Лежandr almashtirishi, $2n$ ta birinchi tartibli ODE, fazaviy fazo, "
            "simplektik struktura."
        ),
        engineering_application=(
            "Nochiziqli tebranishlar tahlili, turg'unlik tadqiqoti, simplektik "
            "integratorlar (uzoq muddatli sonli hisob)."
        ),
        computational_component=(
            "Fazaviy portret qurish va simplektik integratorni oddiy Runge–Kutta "
            "bilan taqqoslash."
        ),
        visualization_component=(
            "Fazaviy portret: traektoriyalar oilasi, separatrisa, muvozanat nuqtalari."
        ),
        research_extension=(
            "Simplektik integratorlar nima uchun uzoq muddatli hisoblarda energiyani "
            "yaxshiroq saqlaydi?"
        ),
        difficulty="ilg'or",
        previous_link=(
            "nm-23 da Yakobi integrali $H$ ni kiritdik. Endi uni shunchaki saqlanuvchi "
            "kattalik emas, balki harakat tenglamalarini yozuvchi asosiy funksiya "
            "sifatida ko'ramiz."
        ),
        next_topic="nm-25",
        estimated_minutes=100,
        tags=["Gamilton", "fazaviy fazo", "kanonik tenglamalar"],
        lesson=Lesson(
            physical_problem=(
                "Mayatnik kichik tebranishda garmonik, katta amplitudada esa nochiziqli, "
                "yetarli energiyada esa umuman tebranmay aylanib ketadi. Bu uch rejimni "
                "bitta rasmda ko'rsatish mumkinmi? Ha — fazaviy fazoda. Va bu rasm "
                "nafaqat chiroyli, balki nochiziqli tizimlarni tahlil qilishning "
                "asosiy vositasidir."
            ),
            concepts=[
                c("Umumlashgan impuls", "$p_j = \\partial L/\\partial\\dot q_j$ — Gamilton "
                  "formalizmida mustaqil o'zgaruvchi."),
                c("Gamilton funksiyasi", "$H(q, p, t) = \\sum p_j\\dot q_j - L$ — "
                  "Лежandr almashtirishi natijasi. Odatda $H = T + \\Pi = E$."),
                c("Kanonik tenglamalar", "$\\dot q_j = \\partial H/\\partial p_j$, "
                  "$\\dot p_j = -\\partial H/\\partial q_j$ — $2n$ ta birinchi tartibli "
                  "tenglama."),
                c("Fazaviy fazo", "$(q_1,\\dots,q_n,p_1,\\dots,p_n)$ — $2n$ o'lchovli fazo. "
                  "Har bir nuqta tizimning to'liq holatini beradi."),
                c("Separatrisa", "Fazaviy portretda turli harakat rejimlarini "
                  "ajratuvchi traektoriya. Mayatnikda — tebranish va aylanish chegarasi."),
            ],
            derivation=[
                d("1-qadam. Лежandr almashtirish",
                  r"H(q,p,t) = \sum_j p_j\dot q_j - L(q,\dot q,t),\qquad p_j = \frac{\partial L}{\partial\dot q_j}",
                  "$\\dot q_j$ larni $p_j$ orqali ifodalab, $L$ dan $H$ ga o'tamiz. "
                  "Bu — mustaqil o'zgaruvchilarni almashtirish standart usuli "
                  "(termodinamikada ham xuddi shunday ishlatiladi)."),
                d("2-qadam. $H$ ning to'la differensiali",
                  r"dH = \sum_j\left(\dot q_j\,dp_j + p_j\,d\dot q_j\right) - "
                  r"\sum_j\left(\frac{\partial L}{\partial q_j}dq_j + \frac{\partial L}{\partial\dot q_j}d\dot q_j\right) - \frac{\partial L}{\partial t}dt",
                  "$p_j = \\partial L/\\partial\\dot q_j$ bo'lgani uchun "
                  "$d\\dot q_j$ li hadlar qisqaradi."),
                d("3-qadam. Kanonik tenglamalarni olish",
                  r"dH = \sum_j\dot q_j\,dp_j - \sum_j\dot p_j\,dq_j - \frac{\partial L}{\partial t}dt "
                  r"\;\Rightarrow\; \boxed{\;\dot q_j = \frac{\partial H}{\partial p_j},\quad "
                  r"\dot p_j = -\frac{\partial H}{\partial q_j}\;}",
                  "Lagranj tenglamasidan $\\partial L/\\partial q_j = \\dot p_j$ "
                  "ekanini qo'llab, koeffitsientlarni tenglashtiramiz."),
                d("4-qadam. Mayatnik uchun Gamiltonian",
                  r"L = \frac{ml^2\dot\varphi^2}{2} + mgl\cos\varphi,\quad p = ml^2\dot\varphi "
                  r"\;\Rightarrow\; H = \frac{p^2}{2ml^2} - mgl\cos\varphi",
                  "$\\dot\\varphi = p/(ml^2)$ ni qo'yamiz. $H$ — to'la energiya."),
                d("5-qadam. Fazaviy traektoriyalar tenglamasi",
                  r"\frac{p^2}{2ml^2} - mgl\cos\varphi = E = \text{const}",
                  "$H$ saqlanadi, demak fazaviy traektoriyalar — $H$ ning sath "
                  "chiziqlari. $E < mgl$ — yopiq egri chiziqlar (tebranish); "
                  "$E > mgl$ — ochiq (aylanish); $E = mgl$ — separatrisa."),
            ],
            formula_meaning=(
                "Kanonik tenglamalar simmetrik va go'zal: $q$ va $p$ deyarli teng "
                "huquqli. Amaliy jihatdan esa asosiy foyda — fazaviy portret. Bitta "
                "rasmda barcha mumkin bo'lgan harakatlar ko'rinadi: muvozanat nuqtalari, "
                "tebranish sohalari, separatrisalar. Bu — nochiziqli dinamikaning "
                "asosiy vositasi va nm-30 dagi turg'unlik tahlilining poydevori. "
                "Hisoblash mexanikasida esa simplektik integratorlar aynan kanonik "
                "strukturani saqlagani uchun uzoq muddatli hisoblarda ustun."
            ),
            equations=[
                eq(r"H = \sum_j p_j\dot q_j - L", "Gamilton funksiyasi (Лежandr almashtirish).",
                   "Gamiltonian"),
                eq(r"\dot q_j = \frac{\partial H}{\partial p_j},\qquad \dot p_j = -\frac{\partial H}{\partial q_j}",
                   "Kanonik (Gamilton) tenglamalari.", "Kanonik tenglamalar"),
                eq(r"H = \frac{p^2}{2ml^2} - mgl\cos\varphi", "Mayatnik Gamiltoniani.",
                   "Mayatnik"),
            ],
            conditions=(
                "Лежandr almashtirish $\\det(\\partial^2L/\\partial\\dot q_i\\partial\\dot q_j) \\neq 0$ "
                "shartini talab qiladi (Gessian aynimasligi). Mexanik tizimlarda bu "
                "inersiya matritsasining aynimasligiga teng va deyarli har doim bajariladi. "
                "$H$ saqlanishi $\\partial H/\\partial t = 0$ shartida."
            ),
            worked_example=WorkedExample(
                statement=(
                    "Matematik mayatnik: $l = 0{,}6$ m, $m = 0{,}2$ kg. "
                    "(a) Gamiltonianni yozing; (b) separatrisa energiyasini toping; "
                    "(c) $\\varphi_0 = 60°$ dan tinch holatdan qo'yib yuborilsa, "
                    "eng past nuqtadagi tezlik va impulsni hisoblang; (d) mayatnikni "
                    "aylanishga o'tkazish uchun minimal boshlang'ich tezlik."
                ),
                given=[r"l = 0{,}6\ \text{m},\; m = 0{,}2\ \text{kg},\; g = 9{,}81\ \text{m/s}^2"],
                steps=[
                    st(r"H = \frac{p^2}{2ml^2} - mgl\cos\varphi = \frac{p^2}{2\cdot 0{,}2\cdot 0{,}36} - "
                       r"0{,}2\cdot 9{,}81\cdot 0{,}6\cos\varphi",
                       "$ml^2 = 0{,}072$ kg·m²; $mgl = 1{,}177$ J."),
                    st(r"E_{sep} = H(\varphi=\pi, p=0) = +mgl = 1{,}177\ \text{J}",
                       "Separatrisa — yuqori (noturg'un) muvozanat holatidan o'tuvchi traektoriya."),
                    st(r"E_0 = -mgl\cos 60^\circ = -1{,}177\cdot 0{,}5 = -0{,}5886\ \text{J}",
                       "Boshlang'ich energiya ($p_0 = 0$)."),
                    st(r"\frac{p^2}{2ml^2} = E_0 + mgl = -0{,}5886+1{,}177 = 0{,}5886\ \text{J}",
                       "Eng past nuqtada ($\\varphi = 0$)."),
                    st(r"p = \sqrt{2\cdot 0{,}072\cdot 0{,}5886} = \sqrt{0{,}08476} = 0{,}2911\ \text{kg·m}^2/\text{s}"
                       r"\;\Rightarrow\; \dot\varphi = \frac{p}{ml^2} = 4{,}04\ \text{rad/s}",
                       "Impuls va burchak tezligi; chiziqli tezlik $v = l\\dot\\varphi = 2{,}43$ m/s."),
                    st(r"E \ge mgl \Rightarrow \frac{p_0^2}{2ml^2} - mgl \ge mgl \Rightarrow "
                       r"\dot\varphi_0 \ge 2\sqrt{g/l} = 2\sqrt{16{,}35} = 8{,}09\ \text{rad/s}",
                       "Aylanishga o'tish sharti (pastdan qo'yib yuborilganda)."),
                ],
                answer=(
                    "$E_{sep} = 1{,}177$ J; $\\dot\\varphi_{max} = 4{,}04$ rad/s "
                    "($v = 2{,}43$ m/s); aylanish uchun $\\dot\\varphi_0 \\ge 8{,}09$ rad/s."
                ),
                engineering_note=(
                    "Separatrisa energiyasi tizimning 'ag'darilish' chegarasini beradi. "
                    "Bu tushuncha pq-18 dagi 'snap-through' ustuvorlik yo'qolishida va "
                    "mq-25 dagi Eyler masalasida to'g'ridan-to'g'ri takrorlanadi: har "
                    "safar energiya to'sig'idan oshib o'tish yangi rejimga o'tishni "
                    "anglatadi."
                ),
            ),
            computation=Computation(
                caption=(
                    "Mayatnik fazaviy portreti: energiyani o'zgartirib, tebranish, "
                    "separatrisa va aylanish rejimlarini kuzating."
                ),
                code='''"""Gamilton formalizmi: fazaviy portret va simplektik integrallash."""
import numpy as np
from scipy.integrate import solve_ivp
from labkit import PARAMS, note, series, table, value

l = float(PARAMS.get("l", 0.6))       # mayatnik uzunligi, m
m = float(PARAMS.get("m", 0.2))       # massa, kg
phi0 = float(PARAMS.get("phi0", 60))  # boshlang'ich burchak, deg
g = 9.81
ml2 = m*l**2
mgl = m*g*l

def H(phi, p):
    """Gamilton funksiyasi = to'la energiya."""
    return p**2/(2*ml2) - mgl*np.cos(phi)

value("ml²", ml2, "kg·m²")
value("mgl (separatrisa energiyasi)", mgl, "J")
value("Kichik tebranish chastotasi", float(np.sqrt(g/l)), "rad/s")
value("Kichik tebranish davri", float(2*np.pi*np.sqrt(l/g)), "s")

E0 = -mgl*np.cos(np.radians(phi0))
p_max = np.sqrt(2*ml2*(E0 + mgl))
value("Boshlang'ich energiya E₀", E0, "J")
value("p_max (φ=0 da)", p_max, "kg·m²/s")
value("ω_max", p_max/ml2, "rad/s")
value("Aylanish uchun min ω₀", float(2*np.sqrt(g/l)), "rad/s")

# Fazaviy portret: turli energiyalardagi sath chiziqlari
ph = np.linspace(-np.pi, np.pi, 400)
for frac, label in [(-0.8, "Kichik tebranish"), (-0.3, "Katta tebranish"),
                    (0.0, "SEPARATRISA"), (0.5, "Aylanish")]:
    E = frac*mgl
    val = 2*ml2*(E + mgl*np.cos(ph))
    mask = val >= 0
    if mask.sum() > 3:
        series(f"{label} (E={E:.3f} J)", ph[mask].tolist(),
               np.sqrt(val[mask]).tolist(), xlabel="φ, rad", ylabel="p, kg·m²/s")

# Kanonik tenglamalarni integrallash
def canonical(t, y):
    phi, p = y
    return [p/ml2, -mgl*np.sin(phi)]     # dq/dt = dH/dp, dp/dt = -dH/dq

sol = solve_ivp(canonical, (0, 10), [np.radians(phi0), 0.0],
                rtol=1e-11, atol=1e-13, dense_output=True, max_step=0.005)
tt = np.linspace(0, 10, 2000)
PH, P = sol.sol(tt)
series("φ(t)", tt.tolist(), np.degrees(PH).tolist(), xlabel="t, s", ylabel="φ, deg")
series("Traektoriya fazaviy fazoda", PH.tolist(), P.tolist(),
       xlabel="φ, rad", ylabel="p, kg·m²/s")

E_num = H(PH, P)
note(f"Energiya drifti (RK45, rtol=1e-11): {np.ptp(E_num):.3e} J")

# Simplektik Eyler bilan taqqoslash (dag'al qadam)
dt = 0.02
n_steps = int(10/dt)
phi_s, p_s = np.radians(phi0), 0.0
E_symp, E_expl = [], []
phi_e, p_e = np.radians(phi0), 0.0
for _ in range(n_steps):
    p_s = p_s - mgl*np.sin(phi_s)*dt        # simplektik: avval p, keyin q
    phi_s = phi_s + p_s/ml2*dt
    E_symp.append(H(phi_s, p_s))
    p_new = p_e - mgl*np.sin(phi_e)*dt      # oshkora Eyler
    phi_e = phi_e + p_e/ml2*dt
    p_e = p_new
    E_expl.append(H(phi_e, p_e))

ts = np.arange(n_steps)*dt
series("Energiya: simplektik Eyler", ts.tolist(), E_symp, xlabel="t, s", ylabel="E, J")
series("Energiya: oshkora Eyler", ts.tolist(), E_expl, xlabel="t, s", ylabel="E, J")
note(f"Bir xil qadamda (dt={dt} s): simplektik drift {np.ptp(E_symp):.5f} J, "
     f"oshkora Eyler drifti {np.ptp(E_expl):.5f} J. "
     "Simplektik usul energiyani chegaralangan xatolik bilan saqlaydi.")

table("Harakat rejimlari",
      ["E/mgl", "Rejim", "Fazaviy traektoriya"],
      [[-1.0, "Turg'un muvozanat", "Nuqta (φ=0, p=0)"],
       [-0.5, "Tebranish", "Yopiq egri chiziq"],
       [1.0, "Separatrisa", "Ochiq, noturg'un nuqtaga asimptotik"],
       [2.0, "Aylanish", "Ochiq, p ishorasi o'zgarmaydi"]])
''',
                parameters=[
                    p("l", "Mayatnik uzunligi l", 0.05, 3.0, 0.6, 0.05, "m"),
                    p("m", "Massa m", 0.05, 5.0, 0.2, 0.05, "kg"),
                    p("phi0", "Boshlang'ich burchak φ₀", 1.0, 179.0, 60.0, 5.0, "deg"),
                ],
                expected_output="mgl = 1,177 J; ω_max = 4,04 rad/s; aylanish uchun ω₀ ≥ 8,09 rad/s",
            ),
            visualization=vis(
                "Fazaviy portret",
                "Manim",
                "$(\\varphi, p)$ tekisligida traektoriyalar oilasi: markazda yopiq "
                "egri chiziqlar (tebranish), chetda ochiq chiziqlar (aylanish), "
                "ularni ajratuvchi separatrisa qalin chiziq bilan. Muvozanat nuqtalari "
                "belgilangan.",
                "Manim: fazaviy portretda harakatlanuvchi nuqta bilan birga fizik "
                "mayatnikni yonma-yon ko'rsatish — bu ikki tasvir o'rtasidagi "
                "moslikni tushuntirishning eng yaxshi usuli. React/SVG da esa "
                "sath chiziqlari oilasi va energiya slideri yetarli.",
            ),
            interpretation=(
                "Fazaviy portret butun dinamikani bitta rasmda jamlaydi. Markaz "
                "($\\varphi=0$) — turg'un muvozanat, uning atrofida yopiq traektoriyalar. "
                "Egar nuqta ($\\varphi=\\pi$) — noturg'un muvozanat, undan separatrisa "
                "chiqadi. Simplektik integrator taqqoslashi esa muhim amaliy xulosani "
                "beradi: oddiy Eyler usuli energiyani sistematik oshiradi, simplektik "
                "esa uni chegaralangan doirada ushlab turadi — uzoq muddatli orbital "
                "hisoblarda bu hal qiluvchi (su-11)."
            ),
            common_mistakes=[
                "$H$ ni $L$ dagi $\\dot q$ larni qoldirgan holda yozish. Barcha "
                "$\\dot q$ lar $p$ orqali ifodalanishi shart.",
                "$H = T + \\Pi$ ni har doim to'g'ri deb hisoblash — bu skleronom "
                "tizimda va tezlikka bog'liq potensial bo'lmaganda o'rinli.",
                "Kanonik tenglamalarda minus ishorasini unutish "
                "($\\dot p = -\\partial H/\\partial q$).",
                "Fazaviy fazoni konfiguratsion fazo bilan chalkashtirish: birinchisi "
                "$2n$ o'lchovli, ikkinchisi $n$ o'lchovli.",
            ],
            quiz=[
                q("Kanonik tenglamalarning Lagranj tenglamalaridan afzalligi nima?",
                  "Ular $2n$ ta birinchi tartibli tenglama — sonli integrallash uchun "
                  "tabiiy shakl; fazaviy fazo geometriyasi tahlil uchun qulay; "
                  "simmetriyalar va saqlanuvchi kattaliklar aniq ko'rinadi.", "konseptual"),
                q("Separatrisa nima va u nima uchun muhim?",
                  "Turli sifat rejimlarini (tebranish va aylanish) ajratuvchi "
                  "traektoriya. U kritik energiyani belgilaydi — undan oshish "
                  "harakat turini keskin o'zgartiradi.", "konseptual"),
                q("$l = 1$ m mayatnikni aylanishga o'tkazish uchun minimal $\\omega_0$?",
                  "$\\omega_0 = 2\\sqrt{g/l} = 2\\sqrt{9{,}81} = 6{,}26$ rad/s.", "hisob"),
                q("Fazaviy portretdagi yopiq traektoriya nimani anglatadi?",
                  "Davriy harakatni: tizim ma'lum vaqtdan keyin bir xil holatga "
                  "qaytadi.", "talqin"),
                q("Kodda simplektik Eyler oshkoradan nimasi bilan farq qiladi?",
                  "Tartibda: simplektikda avval $p$ yangilanadi, keyin yangilangan $p$ "
                  "bilan $q$ hisoblanadi. Bu fazaviy hajmni saqlaydi va energiya "
                  "driftini chegaralaydi.", "kod"),
            ],
            bridge_to_next=(
                "Analitik mexanika apparati tayyor. Endi uni eng muhim muhandislik "
                "masalasiga — tebranishlarga qo'llaymiz. Keyingi modulda kichik "
                "tebranishlar nazariyasi boshlanadi va u to'g'ridan-to'g'ri "
                "konstruksiyalar dinamikasiga olib boradi."
            ),
            research_extension=(
                "Simplektik integratorlarni tadqiq qiling: Störmer–Verlet, "
                "leapfrog va yuqori tartibli (Yoshida) sxemalarni amalga oshiring. "
                "Har biri uchun energiya driftini integrallash vaqtining funksiyasi "
                "sifatida o'lchang va oddiy RK4 bilan taqqoslang. Nima uchun "
                "simplektik usullar 'yomonroq' lokal aniqlikka ega bo'lsa ham, "
                "uzoq muddatda ustun?"
            ),
            manim=manim(
                scene="PhaseSpaceScene",
                module="manim/scenes/nm_lagrange.py",
                title="Mayatnik fazaviy portreti",
                summary="Fizik mayatnik va uning fazaviy fazodagi tasviri yonma-yon; "
                        "energiya ortganda traektoriya separatrisadan o'tib aylanishga aylanadi.",
            ),
        ),
    ),
]
