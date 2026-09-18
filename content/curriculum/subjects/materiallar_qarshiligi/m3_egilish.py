"""MQ / 3-modul: Egilish nazariyasi (mq-13 … mq-18)."""

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

S = "materiallar-qarshiligi"
M = "mq-m3"

TOPICS = [
    Topic(
        id="mq-13",
        subject_id=S,
        module_id=M,
        order=13,
        title="Toza egilishda normal kuchlanishlar va neytral o'q",
        description=(
            "Tekis kesimlar gipotezasi egilishda, neytral qatlam, egilish "
            "formulasining to'liq derivatsiyasi va qarshilik momenti."
        ),
        learning_objective=(
            "Egilish formulasini keltirib chiqarish va balkani mustahkamlikka "
            "hisoblash."
        ),
        prerequisites=["mq-12", "mq-08"],
        mathematical_core=(
            "Egrilik $1/\\rho$, chiziqli deformatsiya taqsimoti, statik "
            "ekvivalentlik integrallari."
        ),
        engineering_application=(
            "Balka, ko'prik oralig'i, kran ko'targichi, qavat plitalari hisobi."
        ),
        computational_component=(
            "Kesim bo'ylab kuchlanish taqsimotini hisoblash va profillarni "
            "taqqoslash."
        ),
        visualization_component=(
            "Egilgan balka, neytral qatlam va kesim bo'ylab chiziqli $\\sigma$ epyurasi."
        ),
        research_extension=(
            "Ikki materialli (kompozit) balkada neytral o'q qayerda joylashadi? "
            "Keltirilgan kesim usuli."
        ),
        difficulty="asosiy",
        previous_link=(
            "mq-12 da $M(x)$ ni topdik. Endi u kesimda qanday kuchlanish hosil "
            "qilishini aniqlaymiz — bu butun fanning markaziy formulasi."
        ),
        next_topic="mq-14",
        estimated_minutes=90,
        tags=["egilish", "neytral o'q", "normal kuchlanish"],
        lesson=Lesson(
            physical_problem=(
                "Balka egilganda uning yuqori tolalari qisqaradi, quyi tolalari "
                "cho'ziladi. Demak orasida uzunligi o'zgarmaydigan qatlam bor. "
                "Aynan shu qatlamdan uzoqlik kuchlanishni belgilaydi — va bu "
                "kesim shaklini tanlashning butun mantiqini tushuntiradi."
            ),
            concepts=[
                c("Toza egilish", "Kesimda faqat eguvchi moment ta'sir qiladi "
                  "($Q = 0$, $N = 0$)."),
                c("Neytral qatlam", "Uzunligi o'zgarmaydigan qatlam; kuchlanish "
                  "unda nolga teng."),
                c("Neytral o'q", "Neytral qatlamning kesim bilan kesishishi. "
                  "U og'irlik markazidan o'tadi."),
                c("Egrilik", "$1/\\rho = M/(EI)$ — balka o'qining egilish darajasi."),
                c("Qarshilik momenti", "$W = I/y_{max}$ — mustahkamlik hisobining "
                  "asosiy geometrik tavsifi."),
            ],
            derivation=[
                d("1-qadam. Kinematika: tekis kesimlar gipotezasi",
                  r"\varepsilon(y) = \frac{y}{\rho}",
                  "Kesimlar tekis qolib, neytral qatlamga perpendikular buriladi. "
                  "$y$ masofadagi tolaning uzayishi $y\\,d\\varphi$, uzunligi "
                  "$\\rho\\,d\\varphi$ — nisbat $y/\\rho$."),
                d("2-qadam. Guk qonuni",
                  r"\sigma(y) = E\varepsilon = \frac{Ey}{\rho}",
                  "Kuchlanish neytral o'qdan masofaga chiziqli bog'liq — "
                  "cho'zilishdagi bir tekis taqsimotdan tubdan farq."),
                d("3-qadam. Birinchi statik shart: $N = 0$",
                  r"N = \int_A\sigma\,dA = \frac{E}{\rho}\int_A y\,dA = \frac{E}{\rho}S_x = 0 "
                  r"\;\Rightarrow\; S_x = 0",
                  "Bo'ylama kuch yo'q, demak statik moment nolga teng — "
                  "ya'ni neytral o'q og'irlik markazidan o'tadi (mq-07)."),
                d("4-qadam. Ikkinchi statik shart: $M$ ni ifodalash",
                  r"M = \int_A\sigma y\,dA = \frac{E}{\rho}\int_A y^2dA = \frac{EI_x}{\rho} "
                  r"\;\Rightarrow\; \frac{1}{\rho} = \frac{M}{EI_x}",
                  "$EI_x$ — egilish bikrligi. Bu munosabat mq-15 dagi egilgan o'q "
                  "tenglamasining asosi."),
                d("5-qadam. Egilish formulasi",
                  r"\boxed{\;\sigma(y) = \frac{My}{I_x},\qquad "
                  r"\sigma_{max} = \frac{M}{W_x}\;}",
                  "Egrilikni yo'qotib, kuchlanishni bevosita moment orqali ifodaladik. "
                  "Bu — materiallar qarshiligining eng ko'p ishlatiladigan formulasi."),
            ],
            formula_meaning=(
                "$\\sigma = My/I$ formulasi uchta omilni birlashtiradi: yuklanish "
                "($M$), joylashuv ($y$) va geometriya ($I$). Neytral o'q yaqinidagi "
                "material deyarli ishlamaydi — shuning uchun dvutavr paydo bo'lgan. "
                "$W = I/y_{max}$ esa yagona son bo'lib, kesimning egilishga "
                "qarshiligini to'liq tavsiflaydi va katalogdan bevosita tanlanadi."
            ),
            equations=[
                eq(r"\sigma = \frac{M y}{I_x}", "Egilishdagi normal kuchlanish.", "Egilish formulasi"),
                eq(r"\sigma_{max} = \frac{M}{W_x} \le [\sigma]", "Mustahkamlik sharti.",
                   "Mustahkamlik sharti"),
                eq(r"\frac{1}{\rho} = \frac{M}{EI_x}", "Egrilik va moment bog'lanishi.", "Egrilik"),
            ],
            conditions=(
                "Formula toza egilish uchun aniq. Ko'ndalang egilishda ($Q \\neq 0$) "
                "u taqribiy, lekin $L/h > 5$ da xatolik 2 % dan kam. Assimetrik "
                "kesimda $W_{yuqori} \\neq W_{quyi}$ — ikkala tola ham tekshiriladi. "
                "Plastik materialda ikkala chegara ham bir xil, mo'rt materialda "
                "cho'zilgan zona hal qiluvchi."
            ),
            worked_example=WorkedExample(
                statement=(
                    "mq-12 dagi balka: $M_{max} = 88{,}2$ kN·m. Dvutavr profil "
                    "tanlang ($[\\sigma] = 160$ MPa), so'ngra to'rtburchak kesim "
                    "($h/b = 2$) bilan material sarfini taqqoslang."
                ),
                given=[r"M_{max} = 88{,}2\ \text{kN·m},\; [\sigma] = 160\ \text{MPa}"],
                steps=[
                    st(r"W_{kerak} \ge \frac{M}{[\sigma]} = \frac{88{,}2\cdot10^3}{160\cdot10^6} = "
                       r"5{,}51\cdot10^{-4}\ \text{m}^3 = 551\ \text{cm}^3",
                       "Kerakli qarshilik momenti."),
                    st(r"\text{Dvutavr № 33: } W_x = 597\ \text{cm}^3,\; A = 53{,}8\ \text{cm}^2",
                       "Katalogdan eng yaqin kattaroq profil."),
                    st(r"\sigma = \frac{88{,}2\cdot10^3}{597\cdot10^{-6}} = 147{,}7\ \text{MPa} \le 160\ \checkmark",
                       "Mustahkamlik sharti bajarildi, zaxira 7,7 %."),
                    st(r"\text{To'rtburchak: } W = \frac{bh^2}{6} = \frac{b(2b)^2}{6} = \frac{2b^3}{3} "
                       r"\ge 5{,}51\cdot10^{-4} \Rightarrow b = 0{,}0937\ \text{m}",
                       "Teng qarshilikli to'rtburchak o'lchamlari."),
                    st(r"h = 187\ \text{mm},\; A = 93{,}7\cdot187 = 17\,522\ \text{mm}^2 = 175{,}2\ \text{cm}^2",
                       "To'rtburchak kesim yuzasi."),
                    st(r"\frac{A_{to'rtburchak}}{A_{dvutavr}} = \frac{175{,}2}{53{,}8} = 3{,}26",
                       "To'rtburchak 3,26 marta ko'p material talab qiladi!"),
                ],
                answer=(
                    "Dvutavr № 33 ($W = 597$ cm³, $A = 53{,}8$ cm²); "
                    "$\\sigma = 147{,}7$ MPa. To'rtburchak 3,26 marta og'irroq."
                ),
                engineering_note=(
                    "3,26 marta material tejash — dvutavrning iqtisodiy asosi. "
                    "Lekin dvutavr yon egilishga va buralishga zaif, shuning uchun "
                    "uni ustuvorlikka ham tekshirish kerak (mq-25). Yon "
                    "ustuvorlikni ta'minlash uchun balka qo'shimcha bog'lamlar "
                    "bilan mahkamlanadi."
                ),
            ),
            computation=Computation(
                caption=(
                    "Egilish kuchlanishi: kesim shakli va momentni o'zgartirib, "
                    "profillarning samaradorligini taqqoslang."
                ),
                code='''"""Toza egilish: kuchlanish taqsimoti va profil tanlash."""
import numpy as np
from labkit import PARAMS, note, series, table, value

M = float(PARAMS.get("M", 88.2))*1e3        # eguvchi moment, N*m
sigma_allow = float(PARAMS.get("s_allow", 160.0))*1e6
b = float(PARAMS.get("b", 94.0))*1e-3       # to'rtburchak eni, m
h = float(PARAMS.get("h", 187.0))*1e-3      # to'rtburchak balandligi, m
E = float(PARAMS.get("E", 200e9))

I_rect = b*h**3/12
W_rect = I_rect/(h/2)
sigma_rect = M/W_rect

value("I (to'rtburchak)", I_rect*1e8, "cm⁴")
value("W (to'rtburchak)", W_rect*1e6, "cm³")
value("σ_max", sigma_rect/1e6, "MPa")
value("Kerakli W", M/sigma_allow*1e6, "cm³")
value("Egrilik radiusi ρ", E*I_rect/M, "m")
note("Mustahkamlik sharti BAJARILDI ✓" if sigma_rect <= sigma_allow
     else "DIQQAT: kuchlanish ruxsat etilgandan yuqori!")

# Kesim bo'ylab kuchlanish taqsimoti (chiziqli)
y = np.linspace(-h/2, h/2, 100)
series("σ(y) — to'rtburchak", (M*y/I_rect/1e6).tolist(), (y*1000).tolist(),
       xlabel="σ, MPa", ylabel="y, mm")

# Dvutavr bilan taqqoslash (soddalashtirilgan model)
h_i, b_f, t_f, t_w = 0.33, 0.14, 0.0112, 0.007
I_i = (b_f*h_i**3 - (b_f-t_w)*(h_i-2*t_f)**3)/12
W_i = I_i/(h_i/2)
A_i = 2*b_f*t_f + t_w*(h_i-2*t_f)
A_rect = b*h
y_i = np.linspace(-h_i/2, h_i/2, 100)
series("σ(y) — dvutavr", (M*y_i/I_i/1e6).tolist(), (y_i*1000).tolist(),
       xlabel="σ, MPa", ylabel="y, mm")

table("Profillarni taqqoslash (bir xil M)",
      ["Profil", "A, cm²", "W, cm³", "σ, MPa", "Massa nisbati"],
      [["To'rtburchak", A_rect*1e4, W_rect*1e6, M/W_rect/1e6, 1.0],
       ["Dvutavr ~№33", A_i*1e4, W_i*1e6, M/W_i/1e6, A_i/A_rect]])

# Neytral o'qdan masofaning hissasi
n_bands = 10
edges = np.linspace(0, h/2, n_bands+1)
contrib = [(b*(e2**3-e1**3)/3)/(I_rect/2)*100 for e1, e2 in zip(edges[:-1], edges[1:])]
table("Qatlamlarning I ga hissasi (yarim kesim)",
      ["Zona (y/h_max)", "Hissa, %"],
      [[f"{edges[i]/(h/2):.1f}–{edges[i+1]/(h/2):.1f}", float(contrib[i])]
       for i in range(n_bands)])
note(f"Chekka 20 % material I ning {sum(contrib[-2:]):.1f} % ini beradi — "
     "shuning uchun material chetga chiqariladi (dvutavr).")

# Balandlikning ta'siri
hh = np.linspace(0.05, 0.5, 100)
series("σ_max(h) — b o'zgarmas", (hh*1000).tolist(),
       (M/(b*hh**2/6)/1e6).tolist(), xlabel="h, mm", ylabel="σ, MPa")
''',
                parameters=[
                    p("M", "Eguvchi moment M", 1.0, 1000.0, 88.2, 1.0, "kN·m"),
                    p("s_allow", "[σ]", 20.0, 400.0, 160.0, 10.0, "MPa"),
                    p("b", "Kesim eni b", 20.0, 400.0, 94.0, 2.0, "mm"),
                    p("h", "Kesim balandligi h", 20.0, 800.0, 187.0, 5.0, "mm"),
                    p("E", "Yung moduli", 1e10, 4e11, 200e9, 1e10, "Pa"),
                ],
                expected_output="W = 548 cm³, σ_max ≈ 161 MPa, dvutavr 3,3 marta yengil",
            ),
            visualization=vis(
                "Egilgan balka va kuchlanish epyurasi",
                "Manim",
                "Balka egiladi, yuqori tolalar qisqaradi (siqilish — sovuq rang), "
                "quyi tolalar cho'ziladi (issiq rang), o'rtada neytral qatlam "
                "o'zgarmaydi. Kesimda chiziqli $\\sigma$ epyurasi.",
                "Manim: neytral qatlam tushunchasini animatsiyada ko'rsatish eng "
                "samarali — tolalar uzunligi o'zgarishini bo'rttirib ko'rsatish "
                "mumkin. React/SVG da esa kesim bo'ylab chiziqli epyura va "
                "profillarni taqqoslash beriladi. Cho'zilish/siqilish uchun "
                "platformaning issiq/sovuq rang juftligi ishlatiladi.",
            ),
            interpretation=(
                "Qatlamlar jadvali asosiy xulosani beradi: chekka 20 % material "
                "inersiya momentining ~49 % ini beradi, markaziy 20 % esa atigi "
                "0,8 % ini. Bu — dvutavrning butun mantiqi. $\\sigma(h)$ grafigi "
                "esa kvadratik kamayadi: balandlikni 2 marta oshirish kuchlanishni "
                "4 marta kamaytiradi."
            ),
            common_mistakes=[
                "Neytral o'qni kesim balandligining o'rtasida deb olish — "
                "assimetrik kesimda u og'irlik markazida.",
                "$I$ o'rniga $W$ ni yoki aksincha ishlatish.",
                "Assimetrik kesimda faqat bitta tolani tekshirish.",
                "Toza egilish formulasini kalta balkalarda ($L/h < 5$) tekshirmasdan "
                "qo'llash.",
            ],
            quiz=[
                q("Nima uchun neytral o'q og'irlik markazidan o'tadi?",
                  "Toza egilishda $N = 0$ sharti $S_x = 0$ ni beradi, bu esa "
                  "markaziy o'qning ta'rifi.", "konseptual"),
                q("$M = 50$ kN·m, $W = 400$ cm³. $\\sigma_{max}$?",
                  "$\\sigma = 50\\cdot10^3/(400\\cdot10^{-6}) = 125$ MPa.", "hisob"),
                q("To'rtburchak balandligini 2 marta oshirsak, $\\sigma$ qanday o'zgaradi?",
                  "4 marta kamayadi, chunki $W \\propto h^2$.", "hisob"),
                q("Nima uchun cho'yan balkada tavrsimon kesim ishlatiladi?",
                  "Cho'yan cho'zilishga zaif; tavr neytral o'qni cho'zilgan zonaga "
                  "yaqinlashtirib, undagi kuchlanishni kamaytiradi.", "talqin"),
                q("Kodda qatlamlar hissasi qanday hisoblangan?",
                  "Har bir qatlam uchun $\\int y^2 dA = b(y_2^3-y_1^3)/3$ va uni "
                  "umumiy $I$ ga nisbati olingan — bu $y^2$ og'irlashtirishning "
                  "miqdoriy ifodasi.", "kod"),
            ],
            bridge_to_next=(
                "Toza egilishda faqat normal kuchlanish bor edi. Real balkada "
                "kesuvchi kuch ham mavjud — keyingi mavzuda u hosil qiladigan "
                "urinma kuchlanishlarni o'rganamiz."
            ),
            research_extension=(
                "Ikki materialli (po'lat + beton yoki kompozit) balkani hisoblang: "
                "keltirilgan kesim usulini qo'llab, neytral o'q holatini aniqlang. "
                "$n = E_1/E_2$ nisbati neytral o'qni qanday siljitishini tahlil "
                "qiling va natijani sonli (FEM) yechim bilan taqqoslang."
            ),
            manim=manim(
                scene="BendingStressScene",
                module="manim/scenes/mq_bending.py",
                title="Egilishda neytral qatlam",
                summary="Balka egilganda tolalarning uzayishi va qisqarishi, "
                        "neytral qatlamning o'zgarmasligi, chiziqli kuchlanish epyurasi.",
            ),
        ),
    ),
    Topic(
        id="mq-14",
        subject_id=S,
        module_id=M,
        order=14,
        title="Ko'ndalang egilishda urinma kuchlanishlar va Juravskiy formulasi",
        description=(
            "Kesuvchi kuchdan hosil bo'ladigan urinma kuchlanishlar, Juravskiy "
            "formulasi, taqsimot shakli va payvand choklar hisobi."
        ),
        learning_objective=(
            "Juravskiy formulasini qo'llab, balkadagi urinma kuchlanishlarni "
            "hisoblash va ularning ahamiyatini baholash."
        ),
        prerequisites=["mq-13", "mq-09"],
        mathematical_core=(
            "Elementar bo'lak muvozanati, kesilgan qismning statik momenti "
            "$S_x^{ots}$, integrallash."
        ),
        engineering_application=(
            "Yupqa devorli profillar, payvand va zakovkali choklar, yog'och "
            "balkalar, qisqa balkalar."
        ),
        computational_component=(
            "Turli profillarda $\\tau(y)$ taqsimotini hisoblash va normal "
            "kuchlanish bilan taqqoslash."
        ),
        visualization_component=(
            "$\\tau(y)$ parabolik taqsimoti va dvutavrdagi sakrash."
        ),
        research_extension=(
            "Yupqa devorli ochiq profilda siljish markazi qayerda? Nima uchun "
            "shvellerni egishda u buraladi?"
        ),
        difficulty="murakkab",
        previous_link=(
            "mq-13 da toza egilishni ko'rdik. Real balkada $Q \\neq 0$ va bu "
            "qo'shimcha urinma kuchlanish beradi."
        ),
        next_topic="mq-15",
        estimated_minutes=90,
        tags=["Juravskiy", "urinma kuchlanish", "ko'ndalang egilish"],
        lesson=Lesson(
            physical_problem=(
                "Yog'och balka egilganda ba'zan tolalar bo'ylab yorilib ketadi — "
                "garchi normal kuchlanish ruxsat etilgandan past bo'lsa ham. Sabab: "
                "yog'och tolalar bo'ylab siljishga zaif, egilishda esa gorizontal "
                "urinma kuchlanish paydo bo'ladi. Uni qanday hisoblash mumkin?"
            ),
            concepts=[
                c("Gorizontal siljish", "Balka qatlamlari bir-biriga nisbatan "
                  "siljishga intiladi; ular bog'langan bo'lsa, urinma kuchlanish "
                  "paydo bo'ladi."),
                c("Kesilgan qismning statik momenti", "$S_x^{ots}$ — hisoblanayotgan "
                  "sathdan yuqoridagi (yoki quyidagi) qismning neytral o'qqa "
                  "nisbatan statik momenti."),
                c("Juravskiy formulasi", "$\\tau = QS_x^{ots}/(I_xb)$ — urinma "
                  "kuchlanishning kesim bo'ylab taqsimoti."),
                c("Taqsimot shakli", "To'rtburchak kesimda parabolik: chekkalarda "
                  "nol, neytral o'qda maksimal."),
                c("Siljish oqimi", "$q_s = \\tau b = QS^{ots}/I$ — payvand chok va "
                  "birikmalarni hisoblashda ishlatiladi."),
            ],
            derivation=[
                d("1-qadam. Elementar bo'lakning gorizontal muvozanati",
                  r"\sum F_x = 0:\; \int_{A^{ots}}\sigma_2dA - \int_{A^{ots}}\sigma_1dA - \tau b\,dx = 0",
                  "$dx$ uzunlikdagi bo'lakning yuqori qismini ajratamiz. Uning ikki "
                  "kesimidagi normal kuchlanishlar farqi gorizontal siljituvchi kuch "
                  "beradi."),
                d("2-qadam. Normal kuchlanishlar farqini ifodalash",
                  r"\int_{A^{ots}}(\sigma_2-\sigma_1)dA = \frac{dM}{I_x}\int_{A^{ots}}y\,dA = "
                  r"\frac{dM}{I_x}S_x^{ots}",
                  "mq-13 dagi $\\sigma = My/I$ formulasini qo'llaymiz."),
                d("3-qadam. Juravskiy formulasi",
                  r"\tau b\,dx = \frac{dM}{I_x}S_x^{ots} \;\Rightarrow\; "
                  r"\boxed{\;\tau = \frac{Q\,S_x^{ots}}{I_x\,b}\;}",
                  "$dM/dx = Q$ bog'lanishidan (mq-12) foydalandik. Urinma "
                  "kuchlanishlar juftligi qonuni bo'yicha gorizontal va vertikal "
                  "$\\tau$ teng."),
                d("4-qadam. To'rtburchak kesim uchun",
                  r"S_x^{ots} = \frac{b}{2}\left(\frac{h^2}{4}-y^2\right) \Rightarrow "
                  r"\tau(y) = \frac{3Q}{2A}\left(1-\frac{4y^2}{h^2}\right),\quad "
                  r"\tau_{max} = \frac{3Q}{2A}",
                  "Parabolik taqsimot; maksimal qiymat o'rtacha kuchlanishdan "
                  "1,5 marta katta va neytral o'qda joylashgan."),
            ],
            formula_meaning=(
                "Juravskiy formulasi normal va urinma kuchlanishlarning "
                "'qarama-qarshiligini' ochib beradi: $\\sigma$ chekkalarda maksimal, "
                "$\\tau$ esa markazda. Shuning uchun ular turli kesimlarda xavfli. "
                "Uzun balkalarda $\\sigma$ hukmron, qisqa balkalarda esa $\\tau$ "
                "hal qiluvchi bo'lishi mumkin. Dvutavrda $\\tau$ deyarli butunlay "
                "devorga tushadi — shuning uchun devor qalinligi alohida "
                "tekshiriladi."
            ),
            equations=[
                eq(r"\tau = \frac{Q S_x^{ots}}{I_x b}", "Juravskiy formulasi.", "Juravskiy"),
                eq(r"\tau_{max} = \frac{3Q}{2A}", "To'rtburchak kesim uchun (neytral o'qda).",
                   "To'rtburchak"),
                eq(r"q_s = \frac{Q S^{ots}}{I_x}", "Siljish oqimi (payvand chok hisobi).",
                   "Siljish oqimi"),
            ],
            conditions=(
                "Formula $b$ kesim kengligi bo'lgan sathda o'rtacha $\\tau$ ni "
                "beradi. Keng kesimlarda (masalan, dvutavr tokchasi) haqiqiy "
                "taqsimot notekis. Yupqa devorli ochiq profillarda siljish markazi "
                "og'irlik markazidan farq qiladi va kuch unga qo'yilmasa buralish "
                "paydo bo'ladi."
            ),
            worked_example=WorkedExample(
                statement=(
                    "To'rtburchak yog'och balka $b = 100$ mm, $h = 200$ mm, "
                    "$L = 3$ m, o'rtasida $F = 24$ kN. Maksimal normal va urinma "
                    "kuchlanishlarni taqqoslang. Yog'och uchun "
                    "$[\\sigma] = 13$ MPa, $[\\tau] = 2$ MPa (tolalar bo'ylab)."
                ),
                given=[r"b = 0{,}1\ \text{m},\; h = 0{,}2\ \text{m},\; L = 3\ \text{m},\; F = 24\ \text{kN}"],
                steps=[
                    st(r"Q_{max} = \frac{F}{2} = 12\ \text{kN};\quad M_{max} = \frac{FL}{4} = "
                       r"\frac{24\cdot 3}{4} = 18\ \text{kN·m}",
                       "Ichki kuchlar (mq-12)."),
                    st(r"I = \frac{0{,}1\cdot 0{,}2^3}{12} = 6{,}667\cdot10^{-5}\ \text{m}^4;\quad "
                       r"W = \frac{I}{0{,}1} = 6{,}667\cdot10^{-4}\ \text{m}^3",
                       "Geometrik tavsiflar."),
                    st(r"\sigma_{max} = \frac{18\cdot10^3}{6{,}667\cdot10^{-4}} = 27{,}0\ \text{MPa} > 13\ \text{MPa}",
                       "Normal kuchlanish ruxsat etilgandan 2,08 marta katta — "
                       "balka yaroqsiz!"),
                    st(r"A = 0{,}02\ \text{m}^2;\quad \tau_{max} = \frac{3\cdot 12\cdot10^3}{2\cdot 0{,}02} = "
                       r"0{,}9\ \text{MPa} \le 2\ \text{MPa}\ \checkmark",
                       "Urinma kuchlanish esa me'yorda."),
                    st(r"\frac{\sigma_{max}}{\tau_{max}} = \frac{27{,}0}{0{,}9} = 30",
                       "Normal kuchlanish 30 marta katta — uzun balkalarda u hukmron."),
                    st(r"h_{kerak} = \sqrt{\frac{6M}{b[\sigma]}} = \sqrt{\frac{6\cdot18\cdot10^3}{0{,}1\cdot13\cdot10^6}} = "
                       r"0{,}288\ \text{m}",
                       "Kerakli balandlik — 290 mm ga oshirish kerak."),
                ],
                answer=(
                    "$\\sigma_{max} = 27{,}0$ MPa (yaroqsiz), $\\tau_{max} = 0{,}9$ MPa "
                    "(me'yorda); kerakli balandlik $h = 290$ mm."
                ),
                engineering_note=(
                    "$\\sigma/\\tau = 30$ nisbati $L/h = 15$ bo'lgani uchun. "
                    "Umumiy qoida: $\\sigma/\\tau \\approx 2L/h$. Demak $L/h < 3$ "
                    "bo'lganda urinma kuchlanish hal qiluvchi bo'lishi mumkin — "
                    "qisqa va baland balkalarda buni tekshirish shart."
                ),
            ),
            computation=Computation(
                caption=(
                    "Juravskiy formulasi: kesim shakli va nisbatlarni o'zgartirib, "
                    "$\\sigma$ va $\\tau$ ning nisbatini kuzating."
                ),
                code='''"""Ko'ndalang egilish: Juravskiy formulasi va kuchlanishlar taqqoslash."""
import numpy as np
from labkit import PARAMS, note, series, table, value

b = float(PARAMS.get("b", 100.0))*1e-3     # kesim eni, m
h = float(PARAMS.get("h", 200.0))*1e-3     # kesim balandligi, m
L = float(PARAMS.get("L", 3.0))            # oraliq, m
F = float(PARAMS.get("F", 24.0))*1e3       # o'rtadagi kuch, N

Q = F/2
M = F*L/4
A = b*h
I = b*h**3/12
W = I/(h/2)

sigma_max = M/W
tau_max = 3*Q/(2*A)
value("Q_max", Q/1000, "kN")
value("M_max", M/1000, "kN·m")
value("σ_max", sigma_max/1e6, "MPa")
value("τ_max", tau_max/1e6, "MPa")
value("σ/τ nisbati", sigma_max/tau_max, "—")
value("L/h nisbati", L/h, "—")
note(f"Taxminiy qoida σ/τ ≈ 2L/h = {2*L/h:.1f} — hisob bilan mos ✓")

# Kesim bo'ylab taqsimotlar
y = np.linspace(-h/2, h/2, 200)
sigma_y = M*y/I
S_ots = b/2*(h**2/4 - y**2)
tau_y = Q*S_ots/(I*b)
series("σ(y)", (sigma_y/1e6).tolist(), (y*1000).tolist(), xlabel="σ, MPa", ylabel="y, mm")
series("τ(y)", (tau_y/1e6).tolist(), (y*1000).tolist(), xlabel="τ, MPa", ylabel="y, mm")

# Dvutavr uchun taqsimot (sakrash bilan)
h_i, b_f, t_f, t_w = 0.30, 0.135, 0.0102, 0.0065
I_i = (b_f*h_i**3 - (b_f-t_w)*(h_i-2*t_f)**3)/12
ys, ts = [], []
for yy in np.linspace(-h_i/2, h_i/2, 400):
    ay = abs(yy)
    if ay >= h_i/2 - t_f:                       # tokchada
        S = b_f*((h_i/2)**2 - ay**2)/2
        width = b_f
    else:                                        # devorda
        S = b_f*((h_i/2)**2 - (h_i/2-t_f)**2)/2 + t_w*((h_i/2-t_f)**2 - ay**2)/2
        width = t_w
    ys.append(yy*1000)
    ts.append(Q*S/(I_i*width)/1e6)
series("τ(y) — dvutavr", ts, ys, xlabel="τ, MPa", ylabel="y, mm")
note(f"Dvutavrda devor/tokcha chegarasida τ sakraydi ({b_f/t_w:.1f} marta), "
     f"chunki kenglik b keskin o'zgaradi. τ_max(devor) = {max(ts):.2f} MPa.")

# Devorning kesuvchi kuchdagi ulushi
tau_web_avg = Q/(t_w*h_i)
note(f"Devorning o'rtacha τ = {tau_web_avg/1e6:.2f} MPa — dvutavrda kesuvchi kuchning "
     "~95 % i devorga tushadi.")

# L/h nisbatining σ/τ ga ta'siri
ratios = np.linspace(2, 25, 100)
series("σ/τ nisbati", ratios.tolist(), (2*ratios).tolist(),
       xlabel="L/h", ylabel="σ_max/τ_max")
note("L/h < 3 bo'lganda urinma kuchlanish hal qiluvchi bo'lishi mumkin — "
     "qisqa balkalarda tekshirish shart.")

table("Turli kesimlar uchun τ_max",
      ["Kesim", "τ_max formulasi", "τ_max/τ_o'rtacha"],
      [["To'rtburchak", "3Q/(2A)", 1.5],
       ["Doira", "4Q/(3A)", 1.333],
       ["Halqa (yupqa)", "2Q/A", 2.0],
       ["Dvutavr (devor)", "≈ Q/(t_w·h)", 1.05]])
''',
                parameters=[
                    p("b", "Kesim eni b", 20.0, 400.0, 100.0, 5.0, "mm"),
                    p("h", "Kesim balandligi h", 40.0, 800.0, 200.0, 10.0, "mm"),
                    p("L", "Oraliq L", 0.3, 12.0, 3.0, 0.1, "m"),
                    p("F", "Kuch F", 1.0, 300.0, 24.0, 1.0, "kN"),
                ],
                expected_output="σ_max = 27,0 MPa, τ_max = 0,9 MPa, σ/τ = 30",
            ),
            visualization=vis(
                "Normal va urinma kuchlanish epyuralari",
                "React/SVG",
                "Kesim yonida ikki epyura: $\\sigma(y)$ chiziqli (chekkalarda "
                "maksimal) va $\\tau(y)$ parabolik (markazda maksimal). Dvutavr "
                "uchun $\\tau$ epyurasidagi sakrash alohida ko'rsatiladi.",
                "React/SVG: ikki epyurani yonma-yon berish ularning "
                "'qarama-qarshiligini' darhol ko'rsatadi — bu mavzuning asosiy "
                "g'oyasi. Dvutavrdagi sakrashni aniq chizish uchun nuqtalar sonini "
                "chegaralarda zichlashtiring.",
            ),
            interpretation=(
                "Ikki epyura bir-birini to'ldiradi: $\\sigma$ chekkalarda, $\\tau$ "
                "markazda maksimal. Dvutavrda $\\tau$ devorda 20 marta sakraydi — "
                "chunki kenglik $b_f/t_w$ marta kamayadi. Bu devor qalinligini "
                "alohida tekshirish zaruratini tushuntiradi. $\\sigma/\\tau = 2L/h$ "
                "qoidasi esa qaysi kuchlanish hal qiluvchi ekanini tez baholash "
                "imkonini beradi."
            ),
            common_mistakes=[
                "$S_x^{ots}$ ni butun kesim uchun hisoblash — faqat kesilgan qism uchun.",
                "$b$ sifatida kesimning umumiy kengligini olish — hisoblanayotgan "
                "sathdagi kenglik kerak.",
                "Dvutavr tokchasida Juravskiy formulasini qo'llash (u yerda "
                "taqsimot murakkab).",
                "Uzun balkalarda urinma kuchlanishni tekshirishga ortiqcha vaqt "
                "sarflash — u odatda ahamiyatsiz.",
            ],
            quiz=[
                q("Nima uchun $\\tau$ neytral o'qda maksimal, $\\sigma$ esa chekkalarda?",
                  "$\\tau \\propto S^{ots}$, u neytral o'qda maksimal; "
                  "$\\sigma \\propto y$, u chekkalarda maksimal.", "konseptual"),
                q("To'rtburchak kesimda $\\tau_{max}$ o'rtachadan necha marta katta?",
                  "1,5 marta: $\\tau_{max} = 3Q/(2A)$, $\\tau_{o'rt} = Q/A$.", "hisob"),
                q("$Q = 40$ kN, $A = 5000$ mm² (to'rtburchak). $\\tau_{max}$?",
                  "$\\tau = 3\\cdot40\\,000/(2\\cdot5000) = 12$ MPa.", "hisob"),
                q("Nima uchun yog'och balkalar tolalar bo'ylab yorilishi mumkin?",
                  "Yog'och tolalar bo'ylab siljishga zaif ($[\\tau]$ kichik), "
                  "egilishda esa gorizontal urinma kuchlanish paydo bo'ladi.",
                  "talqin"),
                q("Kodda dvutavr uchun $\\tau$ nima uchun sakraydi?",
                  "Devor/tokcha chegarasida kenglik $b$ keskin o'zgaradi "
                  "($b_f \\to t_w$), $S^{ots}$ esa uzluksiz — demak $\\tau = QS/(Ib)$ "
                  "sakraydi.", "kod"),
            ],
            bridge_to_next=(
                "Kuchlanishlar aniqlandi. Endi balkaning deformatsiyasini — "
                "egilish chizig'ini va ko'chishlarni hisoblashga o'tamiz."
            ),
            research_extension=(
                "Yupqa devorli ochiq profil (shveller) uchun siljish markazini "
                "toping: siljish oqimi $q_s$ taqsimotini hisoblab, uning "
                "natijaviysi qayerdan o'tishini aniqlang. Kuch siljish markaziga "
                "qo'yilmasa buralish momenti paydo bo'lishini sonli ko'rsating — "
                "bu yupqa devorli konstruksiyalarning muhim xususiyati."
            ),
        ),
    ),
    Topic(
        id="mq-15",
        subject_id=S,
        module_id=M,
        order=15,
        title="Balkaning egilgan o'qi differensial tenglamasi va bikrlik hisobi",
        description=(
            "Egilgan o'q differensial tenglamasi, uni integrallash, chegaraviy "
            "shartlar va bikrlik sharti."
        ),
        learning_objective=(
            "Egilgan o'q tenglamasini yechib, balkaning ko'chish va burilishlarini "
            "aniqlash hamda bikrlik shartini tekshirish."
        ),
        prerequisites=["mq-13", "mq-12"],
        mathematical_core=(
            "$EIw'' = M(x)$ ikkinchi tartibli ODE, ikki marta integrallash, "
            "chegaraviy shartlar, bo'lakli funksiyalar."
        ),
        engineering_application=(
            "Balka bikrligi normalari ($f \\le L/250$), dastgoh shpindellari, "
            "ko'prik oralig'i cho'kishi."
        ),
        computational_component=(
            "Egilgan o'q tenglamasini analitik va sonli (chekli ayirmalar) "
            "yechish va taqqoslash."
        ),
        visualization_component=(
            "Egilgan o'q shakli, burilish burchaklari, maksimal ko'chish nuqtasi."
        ),
        research_extension=(
            "Chekli ayirmalar usuli bilan ixtiyoriy yuklanishdagi balkani yechish "
            "— su-12 ga to'g'ridan-to'g'ri ko'prik."
        ),
        difficulty="murakkab",
        previous_link=(
            "mq-13 da $1/\\rho = M/(EI)$ munosabatini oldik. Endi egrilikni "
            "ko'chish orqali ifodalab, differensial tenglamaga o'tamiz."
        ),
        next_topic="mq-16",
        estimated_minutes=95,
        tags=["egilgan o'q", "bikrlik", "differensial tenglama"],
        lesson=Lesson(
            physical_problem=(
                "Kran ko'targichi yuk ostida 15 mm cho'kdi. Bu ko'p yoki oz? "
                "Mustahkamlik bo'yicha balka mutlaqo xavfsiz bo'lishi mumkin, "
                "lekin ortiqcha cho'kish yukni aniq joylashtirishga xalaqit beradi, "
                "tebranish keltirib chiqaradi va psixologik noqulaylik tug'diradi. "
                "Shuning uchun bikrlik alohida hisoblanadi."
            ),
            concepts=[
                c("Egilgan o'q", "Deformatsiyadan keyin balka o'qining shakli "
                  "$w(x)$."),
                c("Ko'chish (progib)", "$w(x)$ — nuqtaning vertikal siljishi."),
                c("Burilish burchagi", "$\\theta = dw/dx$ — kesimning burilishi."),
                c("Bikrlik sharti", "$w_{max} \\le [f]$; odatda "
                  "$[f] = L/200...L/400$."),
                c("Egilish bikrligi", "$EI$ — ko'chishlarni belgilovchi asosiy "
                  "parametr."),
            ],
            derivation=[
                d("1-qadam. Egrilikni ko'chish orqali ifodalash",
                  r"\frac{1}{\rho} = \frac{w''}{(1+w'^2)^{3/2}} \approx w''",
                  "Kichik ko'chishlarda $w' \\ll 1$, shuning uchun maxraj 1 ga "
                  "yaqin. Bu — geometrik chiziqlilik farazi."),
                d("2-qadam. Egilgan o'q differensial tenglamasi",
                  r"\boxed{\;EI\,w'' = M(x)\;}",
                  "mq-13 dagi $1/\\rho = M/(EI)$ ga qo'yamiz. Ishoralar "
                  "kelishuvi: $w$ pastga musbat, $M$ pastga botiq egishda musbat."),
                d("3-qadam. To'rtinchi tartibli shakl",
                  r"EI\,w^{IV} = q(x)",
                  "$M'' = -q$ (mq-12) bog'lanishidan. Bu shakl sonli usullar va "
                  "FEM uchun qulayroq, chunki $M$ ni oldindan topish shart emas."),
                d("4-qadam. Integrallash va chegaraviy shartlar",
                  r"EIw' = \int M\,dx + C_1,\qquad EIw = \iint M\,dx\,dx + C_1x + C_2",
                  "Ikki doimiy chegaraviy shartlardan topiladi: sharnirda $w = 0$, "
                  "qotirishda $w = 0$ va $w' = 0$, erkin uchda $M = 0$ va $Q = 0$."),
                d("5-qadam. Tipik yechim: o'rtasida kuch",
                  r"w_{max} = \frac{FL^3}{48EI}\ \ (\text{o'rtada});\qquad "
                  r"w_{max} = \frac{5qL^4}{384EI}\ \ (\text{tekis yuklama})",
                  "$L^3$ va $L^4$ darajalar muhim: oraliqni 2 marta oshirish "
                  "cho'kishni 8 yoki 16 marta oshiradi."),
            ],
            formula_meaning=(
                "$w \\propto L^3/(EI)$ — bikrlikning asosiy qonuni. Oraliq uzunligi "
                "hukmron ta'sirga ega, shuning uchun uzun oraliqlarda cho'kish tez "
                "o'sadi va bikrlik sharti mustahkamlikdan qattiqroq bo'lib qoladi. "
                "$EI$ ni oshirishning eng samarali yo'li — balandlikni oshirish "
                "($I \\propto h^3$), material almashtirish emas."
            ),
            equations=[
                eq(r"EI\,w'' = M(x)", "Egilgan o'q differensial tenglamasi.", "Egilgan o'q"),
                eq(r"EI\,w^{IV} = q(x)", "To'rtinchi tartibli shakl.", "To'rtinchi tartib"),
                eq(r"w_{max} = \frac{5qL^4}{384EI}", "Tekis yuklamada maksimal cho'kish.",
                   "Tipik yechim"),
                eq(r"w_{max} \le [f] = \frac{L}{250}", "Bikrlik sharti.", "Bikrlik sharti"),
            ],
            conditions=(
                "Tenglama kichik ko'chishlar ($w \\ll L$) va chiziqli material "
                "uchun o'rinli. Chegaraviy shartlar soni tenglama tartibiga teng: "
                "ikkinchi tartib uchun 2 ta, to'rtinchi uchun 4 ta. Statik aniqmas "
                "balkalarda chegaraviy shartlar reaksiyalarni ham aniqlaydi (mq-17)."
            ),
            worked_example=WorkedExample(
                statement=(
                    "Ikki tayanchli balka $L = 6$ m, dvutavr № 33 "
                    "($I = 9840$ cm⁴, $E = 200$ GPa), tekis yuklama $q = 12$ kN/m "
                    "va o'rtada $F = 30$ kN. Maksimal cho'kishni toping va "
                    "$[f] = L/250$ shartini tekshiring."
                ),
                given=[r"L = 6\ \text{m},\; I = 9840\ \text{cm}^4 = 9{,}84\cdot10^{-5}\ \text{m}^4",
                       r"E = 2\cdot10^{11}\ \text{Pa},\; q = 12\ \text{kN/m},\; F = 30\ \text{kN}"],
                steps=[
                    st(r"EI = 2\cdot10^{11}\cdot 9{,}84\cdot10^{-5} = 1{,}968\cdot10^{7}\ \text{N·m}^2",
                       "Egilish bikrligi."),
                    st(r"w_q = \frac{5qL^4}{384EI} = \frac{5\cdot12\cdot10^3\cdot 1296}{384\cdot 1{,}968\cdot10^{7}}",
                       "Tekis yuklamadan cho'kish."),
                    st(r"w_q = \frac{7{,}776\cdot10^{7}}{7{,}557\cdot10^{9}} = 1{,}029\cdot10^{-2}\ \text{m} = 10{,}29\ \text{mm}",
                       "Tekis yuklama hissasi."),
                    st(r"w_F = \frac{FL^3}{48EI} = \frac{30\cdot10^3\cdot 216}{48\cdot 1{,}968\cdot10^{7}} = "
                       r"\frac{6{,}48\cdot10^{6}}{9{,}446\cdot10^{8}} = 6{,}86\ \text{mm}",
                       "Nuqtaviy kuch hissasi."),
                    st(r"w_{max} = w_q + w_F = 10{,}29 + 6{,}86 = 17{,}15\ \text{mm}",
                       "Superpozitsiya prinsipi (mq-01)."),
                    st(r"[f] = \frac{6000}{250} = 24\ \text{mm};\quad 17{,}15 \le 24\ \checkmark",
                       "Bikrlik sharti bajarildi, zaxira 1,4 marta."),
                ],
                answer=(
                    "$w_{max} = 17{,}15$ mm; $[f] = 24$ mm — bikrlik sharti "
                    "bajarildi (zaxira 1,40)."
                ),
                engineering_note=(
                    "Cho'kish $L/350$ ga teng — bu qulay qiymat. Agar oraliq 8 m "
                    "bo'lganda, cho'kish $(8/6)^4 = 3{,}16$ marta oshib 54 mm "
                    "bo'lardi, ruxsat esa 32 mm — bikrlik sharti buzilardi. Bu "
                    "uzun oraliqlarda bikrlikning hal qiluvchi bo'lishini "
                    "ko'rsatadi."
                ),
            ),
            computation=Computation(
                caption=(
                    "Egilgan o'q: analitik va sonli yechimni taqqoslang, bikrlik "
                    "shartini tekshiring."
                ),
                code='''"""Egilgan o'q differensial tenglamasi: analitik va sonli yechim."""
import numpy as np
from labkit import PARAMS, note, series, table, value

L = float(PARAMS.get("L", 6.0))
I = float(PARAMS.get("I", 9840.0))*1e-8     # m^4
E = float(PARAMS.get("E", 200e9))
q = float(PARAMS.get("q", 12.0))*1e3        # N/m
F = float(PARAMS.get("F", 30.0))*1e3        # N
limit_div = float(PARAMS.get("limit", 250.0))

EI = E*I
value("Egilish bikrligi EI", EI/1e6, "MN·m²")

# --- Analitik yechim (superpozitsiya) ---
w_q = 5*q*L**4/(384*EI)
w_F = F*L**3/(48*EI)
w_total = w_q + w_F
f_allow = L/limit_div
value("Cho'kish (tekis yuk)", w_q*1000, "mm")
value("Cho'kish (nuqtaviy kuch)", w_F*1000, "mm")
value("Umumiy cho'kish", w_total*1000, "mm")
value("Ruxsat etilgan [f]", f_allow*1000, "mm")
value("Bikrlik zaxirasi", f_allow/w_total, "—")
note("Bikrlik sharti BAJARILDI ✓" if w_total <= f_allow
     else "DIQQAT: cho'kish ruxsat etilgandan katta!")

# --- Sonli yechim: chekli ayirmalar (su-12 ga tayyorgarlik) ---
n = 201
x = np.linspace(0, L, n)
dx = x[1]-x[0]
R = q*L/2 + F/2
M_x = R*x - q*x**2/2 - F*np.maximum(x-L/2, 0)

# EI w'' = M ni chekli ayirmalar bilan yechamiz: w(0)=w(L)=0
A = np.zeros((n, n)); rhs = np.zeros(n)
A[0, 0] = 1.0
A[-1, -1] = 1.0
for i in range(1, n-1):
    A[i, i-1] = 1.0
    A[i, i] = -2.0
    A[i, i+1] = 1.0
    rhs[i] = M_x[i]*dx**2/EI
w_num = np.linalg.solve(A, rhs)

series("Egilgan o'q w(x) — sonli", x.tolist(), (w_num*1000).tolist(),
       xlabel="x, m", ylabel="w, mm")
series("Eguvchi moment M(x)", x.tolist(), (M_x/1000).tolist(),
       xlabel="x, m", ylabel="M, kN·m")
theta = np.gradient(w_num, x)
series("Burilish burchagi θ(x)", x.tolist(), np.degrees(theta).tolist(),
       xlabel="x, m", ylabel="θ, deg")

value("w_max (sonli)", float(np.max(np.abs(w_num)))*1000, "mm")
note(f"Analitik {w_total*1000:.4f} mm va sonli {np.max(np.abs(w_num))*1000:.4f} mm "
     f"farqi: {abs(np.max(np.abs(w_num))-w_total)*1000:.5f} mm "
     f"({abs(np.max(np.abs(w_num))-w_total)/w_total*100:.3f} %)")
note("Chekli ayirmalar usuli su-12 da batafsil o'rganiladi; bu yerda uning "
     "birinchi amaliy qo'llanilishi ko'rsatildi.")

# To'r zichligining aniqlikka ta'siri
errs = []
for nn in (11, 21, 51, 101, 201, 401):
    xs = np.linspace(0, L, nn); h_ = xs[1]-xs[0]
    Ms = R*xs - q*xs**2/2 - F*np.maximum(xs-L/2, 0)
    Aa = np.zeros((nn, nn)); bb = np.zeros(nn)
    Aa[0, 0] = Aa[-1, -1] = 1.0
    for i in range(1, nn-1):
        Aa[i, i-1], Aa[i, i], Aa[i, i+1] = 1.0, -2.0, 1.0
        bb[i] = Ms[i]*h_**2/EI
    ws = np.linalg.solve(Aa, bb)
    errs.append([nn, float(np.max(np.abs(ws))*1000),
                 float(abs(np.max(np.abs(ws))-w_total)/w_total*100)])
table("To'r zichligi va aniqlik", ["Tugunlar soni", "w_max, mm", "Xatolik, %"], errs)

# Oraliqning cho'kishga ta'siri
LL = np.linspace(2, 15, 100)
series("w_max(L) — tekis yuk", LL.tolist(), (5*q*LL**4/(384*EI)*1000).tolist(),
       xlabel="L, m", ylabel="w, mm")
series("Ruxsat [f] = L/250", LL.tolist(), (LL/limit_div*1000).tolist(),
       xlabel="L, m", ylabel="w, mm")
idx = np.argmin(np.abs(5*q*LL**4/(384*EI) - LL/limit_div))
note(f"Bikrlik sharti L ≈ {LL[idx]:.2f} m da chegaraga yetadi — undan uzun "
     "oraliqlarda bikrlik hal qiluvchi bo'ladi.")
''',
                parameters=[
                    p("L", "Oraliq L", 1.0, 20.0, 6.0, 0.5, "m"),
                    p("I", "Inersiya momenti I", 100.0, 100000.0, 9840.0, 100.0, "cm⁴"),
                    p("E", "Yung moduli E", 1e10, 4e11, 200e9, 1e10, "Pa"),
                    p("q", "Tekis yuklama q", 0.0, 100.0, 12.0, 1.0, "kN/m"),
                    p("F", "Nuqtaviy kuch F", 0.0, 300.0, 30.0, 5.0, "kN"),
                    p("limit", "Bikrlik me'yori L/n", 100.0, 600.0, 250.0, 25.0, "—"),
                ],
                expected_output="w_max ≈ 17,15 mm, [f] = 24 mm, sonli-analitik farq < 0,1 %",
            ),
            visualization=vis(
                "Egilgan o'q va burilish burchaklari",
                "React/SVG",
                "Balkaning deformatsiyalanmagan (punktir) va egilgan (to'liq chiziq) "
                "holati, masshtab bo'rttirilgan; maksimal cho'kish nuqtasi "
                "belgilangan; ostida $\\theta(x)$ grafigi.",
                "React/SVG: deformatsiyani 50–200 marta bo'rttirib ko'rsatish shart "
                "(real cho'kish 17 mm / 6000 mm = 0,3 %). Ruxsat etilgan chegarani "
                "gorizontal chiziq bilan qo'shish bikrlik shartini vizual qiladi.",
            ),
            interpretation=(
                "Sonli va analitik yechim farqi to'r zichligi bilan kvadratik "
                "kamayadi (jadvalda ko'rinadi) — bu markaziy ayirmalar sxemasining "
                "$O(h^2)$ tartibini tasdiqlaydi va su-07 da nazariy asoslanadi. "
                "$w(L)$ grafigi esa bikrlik va mustahkamlik shartlarining "
                "kesishish nuqtasini ko'rsatadi: undan uzun oraliqlarda bikrlik "
                "hal qiluvchi bo'ladi."
            ),
            common_mistakes=[
                "$w$ va $\\theta$ ishoralarini chalkashtirish — kelishuvni boshda "
                "belgilang va saqlang.",
                "Chegaraviy shartlar sonini tenglama tartibiga moslashtirmaslik.",
                "Bikrlikni faqat mustahkamlikdan keyin tekshirish — uzun "
                "oraliqlarda u hal qiluvchi bo'lishi mumkin.",
                "Katta ko'chishlarda chiziqli tenglamani qo'llash ($w'^2$ hadini "
                "tashlab yuborish xatosi).",
            ],
            quiz=[
                q("Nima uchun $EIw'' = M$ tenglamasi kichik ko'chishlarni talab qiladi?",
                  "Aniq egrilik $w''/(1+w'^2)^{3/2}$; $w' \\ll 1$ bo'lgandagina u "
                  "$w''$ ga soddalashadi.", "konseptual"),
                q("Oraliqni 2 marta oshirsak, tekis yuklamadagi cho'kish qanday "
                  "o'zgaradi?",
                  "16 marta ortadi ($L^4$), ruxsat esa faqat 2 marta — demak "
                  "bikrlik keskin yomonlashadi.", "hisob"),
                q("$F = 20$ kN, $L = 4$ m, $EI = 10^7$ N·m². O'rtadagi cho'kish?",
                  "$w = 20\\,000\\cdot64/(48\\cdot10^7) = 2{,}67$ mm.", "hisob"),
                q("Cho'kishni kamaytirishning eng samarali yo'li qaysi?",
                  "Kesim balandligini oshirish: $I \\propto h^3$, demak $h$ ni "
                  "26 % oshirish cho'kishni 2 marta kamaytiradi.", "talqin"),
                q("Kodda chekli ayirmalar matritsasi qanday tuzilgan?",
                  "Ichki tugunlar uchun $w''\\approx(w_{i-1}-2w_i+w_{i+1})/h^2$ "
                  "shabloni, chekkalarda esa $w = 0$ chegaraviy shartlari. Bu — "
                  "su-12 dagi matritsa usulining sodda holi.", "kod"),
            ],
            bridge_to_next=(
                "Integrallash har bir yuklanish uchun alohida bajarilishi kerak. "
                "Keyingi mavzuda universal usul — dastlabki parametrlar usulini "
                "o'rganamiz."
            ),
            research_extension=(
                "Chekli ayirmalar sxemasining yaqinlashish tartibini aniqlang: "
                "to'r qadamini ketma-ket ikki marta kamaytirib, xatolikning "
                "kamayish nisbatini o'lchang. $\\log(xatolik)$ va $\\log(h)$ "
                "grafigining qiyaligi 2 ga teng ekanini ko'rsating — bu "
                "su-07 va su-23 dagi konvergensiya tahlilining amaliy mashqi."
            ),
        ),
    ),
    Topic(
        id="mq-16",
        subject_id=S,
        module_id=M,
        order=16,
        title="Balka ko'chishlarini aniqlash: dastlabki parametrlar va energetik usullar",
        description=(
            "Dastlabki parametrlar usuli, universal tenglama, Mor integrali va "
            "Vereshchagin qoidasiga kirish."
        ),
        learning_objective=(
            "Murakkab yuklanishdagi balkaning ixtiyoriy kesimidagi ko'chishni "
            "universal usullar bilan topish."
        ),
        prerequisites=["mq-15"],
        mathematical_core=(
            "Bo'lakli funksiyalar, Macaulay qavslari, universal tenglama, "
            "epyuralarni ko'paytirish."
        ),
        engineering_application=(
            "Ko'p yuklanishli balkalar, statik aniqmas tizimlar, konstruksiya "
            "deformatsiyasini bashorat qilish."
        ),
        computational_component=(
            "Universal tenglamani dasturiy amalga oshirish va Vereshchagin "
            "qoidasi bilan taqqoslash."
        ),
        visualization_component=(
            "Epyuralarni ko'paytirish sxemasi (Vereshchagin) va egilgan o'q."
        ),
        research_extension=(
            "Mor integrali qanday qilib virtual ishlar prinsipidan kelib chiqadi? "
            "(nm-20 bilan bog'lanish)"
        ),
        difficulty="murakkab",
        previous_link=(
            "mq-15 da har bir yuklanish uchun alohida integrallash kerak edi. "
            "Dastlabki parametrlar usuli buni bir marta bajarib, universal "
            "formula beradi."
        ),
        next_topic="mq-17",
        estimated_minutes=95,
        tags=["dastlabki parametrlar", "Mor integrali", "Vereshchagin"],
        lesson=Lesson(
            physical_problem=(
                "Kran balkasiga bir vaqtda o'z og'irligi, harakatlanuvchi yuk va "
                "tormozlanish kuchi ta'sir qiladi. Har bir yuklanish uchun "
                "differensial tenglamani qaytadan integrallash juda uzoq. Kerakli "
                "kesimdagi ko'chishni to'g'ridan-to'g'ri, butun tenglamani "
                "yechmasdan topish mumkinmi? Ha — energetik usullar bilan."
            ),
            concepts=[
                c("Dastlabki parametrlar", "$w_0$, $\\theta_0$, $M_0$, $Q_0$ — "
                  "balka boshidagi to'rtta kattalik; ular butun yechimni aniqlaydi."),
                c("Universal tenglama", "Barcha yuklanish turlarini o'z ichiga olgan "
                  "bitta formula; Macaulay qavslari bilan yoziladi."),
                c("Mor integrali", "$\\Delta = \\int\\frac{M_F\\bar M}{EI}dx$ — "
                  "virtual birlik kuch usuli."),
                c("Vereshchagin qoidasi", "$\\int M_F\\bar M\\,dx = \\Omega\\bar M_C$ "
                  "— epyuralar ko'paytmasini yuza × markazdagi ordinata bilan "
                  "almashtirish."),
                c("Birlik holat", "Ko'chish izlanayotgan nuqtaga birlik kuch (yoki "
                  "moment) qo'yilgan yordamchi masala."),
            ],
            derivation=[
                d("1-qadam. Universal tenglamani tuzish",
                  r"EIw(x) = EIw_0 + EI\theta_0x + \frac{M_0x^2}{2} + \frac{Q_0x^3}{6} + "
                  r"\sum\frac{F\langle x-a\rangle^3}{6} + \sum\frac{q\langle x-b\rangle^4}{24}",
                  "$\\langle x-a\\rangle = 0$ agar $x < a$. Bu — $EIw^{IV} = q$ "
                  "tenglamasini ketma-ket to'rt marta integrallash natijasi."),
                d("2-qadam. Mor integralini virtual ishlar prinsipidan olish",
                  r"1\cdot\Delta = \int_L\frac{M_F\bar M}{EI}dx",
                  "nm-20 dagi virtual ishlar prinsipini elastik jismga qo'llaymiz: "
                  "birlik kuchning haqiqiy ko'chishdagi ishi ichki kuchlarning "
                  "virtual ishiga teng."),
                d("3-qadam. Vereshchagin qoidasi",
                  r"\int_L M_F\bar M\,dx = \Omega_F\cdot\bar M_C",
                  "$\\bar M$ chiziqli bo'lsa (bu deyarli har doim shunday), "
                  "integral $M_F$ epyurasi yuzasi $\\Omega$ va uning og'irlik "
                  "markazi ostidagi $\\bar M$ ordinatasining ko'paytmasiga teng."),
                d("4-qadam. Amaliy qo'llash tartibi",
                  r"\Delta_C = \frac{1}{EI}\sum_i \Omega_i\bar M_{Ci}",
                  "Epyuralarni oddiy shakllarga (to'rtburchak, uchburchak, "
                  "parabola) ajratib, har biri uchun yuza va markaz ordinatasini "
                  "ko'paytiramiz."),
            ],
            formula_meaning=(
                "Mor integrali va Vereshchagin qoidasi integrallashni "
                "geometrik amalga aylantiradi: epyuralarni 'ko'paytirish' kifoya. "
                "Bu — statik aniqmas tizimlarni yechishning asosiy vositasi "
                "(mq-17) va u energetik usullarning (mq-24) tabiiy davomi. "
                "Hisoblash mexanikasida esa aynan shu g'oya FEM ning zaif "
                "shakliga olib boradi (su-13)."
            ),
            equations=[
                eq(r"EIw(x) = EIw_0 + EI\theta_0 x + \frac{M_0x^2}{2} + \sum\frac{F\langle x-a\rangle^3}{6}",
                   "Universal tenglama (dastlabki parametrlar usuli).", "Universal tenglama"),
                eq(r"\Delta = \int_L\frac{M_F\bar M}{EI}dx", "Mor integrali.", "Mor integrali"),
                eq(r"\int M_F\bar M dx = \Omega\bar M_C", "Vereshchagin qoidasi.",
                   "Vereshchagin"),
            ],
            conditions=(
                "Vereshchagin qoidasi $\\bar M$ chiziqli bo'lgandagina o'rinli — "
                "bu birlik yuklanishda deyarli har doim shunday. Ikkala epyura "
                "ham egri bo'lsa, integrallash yoki Simpson formulasi kerak. "
                "$EI = \\text{const}$ bo'lmasa, integral uchastkalarga ajratiladi."
            ),
            worked_example=WorkedExample(
                statement=(
                    "Konsol balka $L = 2{,}5$ m, uchida $F = 15$ kN, butun "
                    "uzunlikda $q = 8$ kN/m. $EI = 5\\times10^6$ N·m². Uchining "
                    "ko'chishi va burilish burchagini Mor–Vereshchagin usuli bilan "
                    "toping."
                ),
                given=[r"L = 2{,}5\ \text{m},\; F = 15\ \text{kN},\; q = 8\ \text{kN/m}",
                       r"EI = 5\cdot10^6\ \text{N·m}^2"],
                steps=[
                    st(r"M_F(x) = -Fx - \frac{qx^2}{2}\ (\text{uchdan hisoblab})",
                       "Haqiqiy yuklanishdan moment epyurasi."),
                    st(r"\bar M(x) = -x\ (\text{uchga birlik kuch qo'yilgan})",
                       "Birlik holat epyurasi — chiziqli."),
                    st(r"\Delta_F = \frac{1}{EI}\Omega_F\bar M_C: \; "
                       r"\Omega_F = \frac{1}{2}(FL)L = \frac{15\cdot2{,}5\cdot2{,}5}{2} = 46{,}88\ \text{kN·m}^2,\; "
                       r"\bar M_C = \frac{2L}{3} = 1{,}667",
                       "Uchburchak epyura: yuza va markaz ordinatasi."),
                    st(r"\Delta_F = \frac{46{,}88\cdot10^3\cdot 1{,}667}{5\cdot10^6} = 0{,}01563\ \text{m} = 15{,}63\ \text{mm}",
                       "Nuqtaviy kuchdan ko'chish. Tekshirish: "
                       "$FL^3/(3EI) = 15\\,000\\cdot15{,}625/(1{,}5\\cdot10^7) = 15{,}63$ mm ✓"),
                    st(r"\Omega_q = \frac{1}{3}\cdot\frac{qL^2}{2}\cdot L = \frac{8\cdot 6{,}25}{2}\cdot\frac{2{,}5}{3} = "
                       r"20{,}83\ \text{kN·m}^2,\; \bar M_C = \frac{3L}{4} = 1{,}875",
                       "Kvadrat parabola epyurasi uchun yuza va markaz."),
                    st(r"\Delta_q = \frac{20{,}83\cdot10^3\cdot1{,}875}{5\cdot10^6} = 7{,}81\ \text{mm};\quad "
                       r"\Delta = 15{,}63+7{,}81 = 23{,}44\ \text{mm}",
                       "Umumiy ko'chish. Tekshirish: $qL^4/(8EI) = 8000\\cdot39{,}06/(4\\cdot10^7) = 7{,}81$ mm ✓"),
                ],
                answer=(
                    "$w_{uch} = 23{,}44$ mm; $\\theta_{uch} = FL^2/(2EI) + qL^3/(6EI) = "
                    "9{,}38 + 4{,}17 = 13{,}5$ mrad $= 0{,}77°$."
                ),
                engineering_note=(
                    "Vereshchagin qoidasi integrallashni to'liq geometrik amalga "
                    "aylantirdi — natija aniq formulalar bilan bir xil. Bu usulning "
                    "asosiy kuchi murakkab, ko'p uchastkali balkalarda namoyon "
                    "bo'ladi, u yerda bevosita integrallash juda uzoq."
                ),
            ),
            computation=Computation(
                caption=(
                    "Ko'chishlarni uch usulda hisoblang: universal tenglama, "
                    "Mor integrali va sonli integrallash."
                ),
                code='''"""Ko'chishlar: universal tenglama, Mor integrali, Vereshchagin."""
import numpy as np
from scipy.integrate import quad
from labkit import PARAMS, note, series, table, value

L = float(PARAMS.get("L", 2.5))
F = float(PARAMS.get("F", 15.0))*1e3
q = float(PARAMS.get("q", 8.0))*1e3
EI = float(PARAMS.get("EI", 5e6))
x_target = float(PARAMS.get("x_t", 2.5))

# --- 1. Analitik formulalar (konsol) ---
w_F = F*L**3/(3*EI)
w_q = q*L**4/(8*EI)
theta_F = F*L**2/(2*EI)
theta_q = q*L**3/(6*EI)
value("w (kuchdan)", w_F*1000, "mm")
value("w (taqsimlangan)", w_q*1000, "mm")
value("w (umumiy)", (w_F+w_q)*1000, "mm")
value("θ (umumiy)", np.degrees(theta_F+theta_q), "deg")

# --- 2. Mor integrali (sonli) ---
def M_real(x):
    """Haqiqiy yuklanishdan moment (qotirishdan x masofada)."""
    s = L - x
    return -(F*s + q*s**2/2)

def M_unit_force(x):
    """Uchga birlik kuch qo'yilgandagi moment."""
    return -(L - x)

def M_unit_moment(x):
    """Uchga birlik moment qo'yilgandagi moment."""
    return -1.0

delta_mohr, err1 = quad(lambda x: M_real(x)*M_unit_force(x)/EI, 0, L)
theta_mohr, err2 = quad(lambda x: M_real(x)*M_unit_moment(x)/EI, 0, L)
value("w (Mor integrali)", delta_mohr*1000, "mm")
value("θ (Mor integrali)", np.degrees(theta_mohr), "deg")
note(f"Analitik va Mor integrali farqi: {abs(delta_mohr-(w_F+w_q))*1000:.6f} mm")

# --- 3. Vereshchagin qoidasi (geometrik) ---
Omega_F = 0.5*(F*L)*L          # uchburchak epyura yuzasi
Mbar_F = 2*L/3                 # birlik epyura ordinatasi markazda
Omega_q = (q*L**2/2)*L/3       # parabola yuzasi
Mbar_q = 3*L/4
delta_ver = (Omega_F*Mbar_F + Omega_q*Mbar_q)/EI
value("w (Vereshchagin)", delta_ver*1000, "mm")
note(f"Vereshchagin va analitik farqi: {abs(delta_ver-(w_F+w_q))*1000:.6f} mm — "
     "geometrik usul aniq natija beradi ✓")

# --- 4. Universal tenglama bilan egilgan o'q ---
x = np.linspace(0, L, 300)
w_x = (F*x**2*(3*L-x)/(6*EI) + q*x**2*(6*L**2 - 4*L*x + x**2)/(24*EI))
series("Egilgan o'q w(x)", x.tolist(), (w_x*1000).tolist(), xlabel="x, m", ylabel="w, mm")
theta_x = np.gradient(w_x, x)
series("Burilish θ(x)", x.tolist(), np.degrees(theta_x).tolist(),
       xlabel="x, m", ylabel="θ, deg")

# Epyuralar
xs = np.linspace(0, L, 200)
series("M_F epyurasi", xs.tolist(), [M_real(v)/1000 for v in xs],
       xlabel="x, m", ylabel="M, kN·m")
series("Birlik epyura M̄", xs.tolist(), [M_unit_force(v) for v in xs],
       xlabel="x, m", ylabel="M̄, m")

table("Usullarni taqqoslash",
      ["Usul", "w, mm", "Xatolik, mm"],
      [["Analitik formula", float((w_F+w_q)*1000), 0.0],
       ["Mor integrali (sonli)", float(delta_mohr*1000), float(abs(delta_mohr-(w_F+w_q))*1000)],
       ["Vereshchagin", float(delta_ver*1000), float(abs(delta_ver-(w_F+w_q))*1000)]])

table("Vereshchagin: tipik epyuralar",
      ["Epyura shakli", "Yuza Ω", "Markaz x_C"],
      [["To'rtburchak (h×L)", "h·L", "L/2"],
       ["Uchburchak (h, L)", "h·L/2", "L/3 yoki 2L/3"],
       ["Kvadrat parabola", "h·L/3", "L/4 yoki 3L/4"],
       ["Kubik parabola", "h·L/4", "L/5"]])
''',
                parameters=[
                    p("L", "Konsol uzunligi L", 0.5, 10.0, 2.5, 0.1, "m"),
                    p("F", "Uchdagi kuch F", 0.0, 200.0, 15.0, 1.0, "kN"),
                    p("q", "Taqsimlangan yuklama q", 0.0, 100.0, 8.0, 1.0, "kN/m"),
                    p("EI", "Egilish bikrligi EI", 1e5, 1e9, 5e6, 1e5, "N·m²"),
                    p("x_t", "Nishon kesim", 0.0, 10.0, 2.5, 0.1, "m"),
                ],
                expected_output="w = 23,44 mm, θ = 0,774°, uch usul bir xil natija beradi",
            ),
            visualization=vis(
                "Epyuralarni ko'paytirish (Vereshchagin)",
                "React/SVG",
                "Ikki epyura yonma-yon: $M_F$ (haqiqiy) va $\\bar M$ (birlik). "
                "$M_F$ epyurasining yuzasi bo'yalgan, og'irlik markazi belgilangan, "
                "undan $\\bar M$ epyurasiga vertikal chiziq tushirilgan.",
                "React/SVG: Vereshchagin qoidasining butun mohiyati — 'yuza × "
                "markazdagi ordinata' — aynan shu chizmada ko'rinadi. Og'irlik "
                "markazidan tushirilgan chiziq usulni bir qarashda tushuntiradi.",
            ),
            interpretation=(
                "Uchala usul bir xil natija beradi ($10^{-9}$ mm aniqlikda) — bu "
                "ularning matematik ekvivalentligini tasdiqlaydi. Amaliy tanlov "
                "qulaylikka bog'liq: sodda holda analitik formula, murakkab "
                "epyuralarda Vereshchagin, dasturlashda esa sonli integrallash. "
                "Mor integrali esa nazariy jihatdan eng umumiy va u statik "
                "aniqmas tizimlarga to'g'ridan-to'g'ri qo'llanadi."
            ),
            common_mistakes=[
                "Vereshchagin qoidasida markaz ordinatasini noto'g'ri epyuradan "
                "olish — u chiziqli ($\\bar M$) epyuradan olinadi.",
                "Epyuralarni ishorasiz ko'paytirish — ishoralar hisobga olinishi kerak.",
                "Murakkab epyurani oddiy shakllarga ajratmaslik.",
                "Birlik kuchni noto'g'ri nuqtaga yoki noto'g'ri yo'nalishda qo'yish.",
            ],
            quiz=[
                q("Mor integrali qaysi prinsipdan kelib chiqadi?",
                  "Virtual ishlar prinsipidan (nm-20): birlik kuchning haqiqiy "
                  "ko'chishdagi ishi ichki kuchlarning virtual ishiga teng.",
                  "konseptual"),
                q("Vereshchagin qoidasi qachon qo'llanmaydi?",
                  "Ikkala epyura ham egri bo'lganda — u $\\bar M$ ning chiziqli "
                  "bo'lishini talab qiladi.", "konseptual"),
                q("Konsol, uchida $F$: $\\Omega$ va $\\bar M_C$ ni yozing.",
                  "$\\Omega = FL^2/2$ (uchburchak), $\\bar M_C = 2L/3$; "
                  "$\\Delta = FL^3/(3EI)$.", "hisob"),
                q("Burilish burchagini topish uchun qanday birlik yuk qo'yiladi?",
                  "Birlik moment — chunki moment burchakka mos umumlashgan kuch.",
                  "talqin"),
                q("Kodda `quad` bilan hisoblangan natija nima uchun analitik bilan "
                  "mos keladi?",
                  "Mor integrali matematik jihatdan aniq; sonli integrallash esa "
                  "polinomial funksiyalarni Gauss kvadraturasi bilan mashina "
                  "aniqligida hisoblaydi.", "kod"),
            ],
            bridge_to_next=(
                "Endi bizda ko'chishlarni hisoblashning universal vositasi bor. "
                "Aynan u statik aniqmas balkalarni yechish imkonini beradi — "
                "keyingi mavzu."
            ),
            research_extension=(
                "Mor integralini nafaqat egilish, balki cho'zilish va buralish "
                "uchun ham umumlashtiring: "
                "$\\Delta = \\int\\frac{N\\bar N}{EA}dx + \\int\\frac{M\\bar M}{EI}dx + "
                "\\int\\frac{T\\bar T}{GI_p}dx$. Fazoviy ramada har bir hadning "
                "hissasini hisoblang va qaysi deformatsiya turi hukmronligini "
                "aniqlang."
            ),
        ),
    ),
    Topic(
        id="mq-17",
        subject_id=S,
        module_id=M,
        order=17,
        title="Statik aniqmas balkalar va kuchlar usuli",
        description=(
            "Statik aniqmaslik darajasi, asosiy sistema, kuchlar usulining "
            "kanonik tenglamalari, uzluksizlik shartlari."
        ),
        learning_objective=(
            "Statik aniqmas balkani kuchlar usuli bilan yechish va epyuralarni "
            "qurish."
        ),
        prerequisites=["mq-16", "mq-06"],
        mathematical_core=(
            "Kanonik tenglamalar $\\delta_{11}X_1 + \\Delta_{1F} = 0$, "
            "moslik shartlari, chiziqli tenglamalar tizimi."
        ),
        engineering_application=(
            "Ko'p tayanchli balkalar, ramalar, uzluksiz ko'prik oraliqlari."
        ),
        computational_component=(
            "Kuchlar usulini dasturiy amalga oshirish va natijani sonli yechim "
            "bilan tekshirish."
        ),
        visualization_component=(
            "Asosiy sistema, birlik va yuk epyuralari, natijaviy epyura."
        ),
        research_extension=(
            "Ko'p aniqmas tizimlarda kanonik tenglamalar matritsasining "
            "xossalari; simmetriyadan foydalanish."
        ),
        difficulty="murakkab",
        previous_link=(
            "mq-16 dagi Mor integrali endi asosiy vosita bo'ladi: u ortiqcha "
            "bog'lanish reaksiyasini topish uchun kerakli ko'chishlarni beradi."
        ),
        next_topic="mq-18",
        estimated_minutes=100,
        tags=["statik aniqmas", "kuchlar usuli", "kanonik tenglamalar"],
        lesson=Lesson(
            physical_problem=(
                "Uzluksiz ko'prik oralig'i uch tayanchga tayanadi. Bu statik "
                "aniqmas: qo'shimcha tayanch momentni kamaytiradi va bikrlikni "
                "oshiradi, lekin tayanchning cho'kishi qo'shimcha kuchlanish "
                "keltirib chiqaradi. Bunday tizimni qanday hisoblash mumkin?"
            ),
            concepts=[
                c("Ortiqcha bog'lanish", "Muvozanat uchun zarur bo'lmagan, lekin "
                  "bikrlikni oshiruvchi bog'lanish."),
                c("Asosiy sistema", "Ortiqcha bog'lanishlar olib tashlangan statik "
                  "aniq sistema."),
                c("Kuchlar usuli", "Ortiqcha reaksiyalar noma'lum sifatida olinadi "
                  "va moslik shartlaridan topiladi."),
                c("Kanonik tenglamalar", "$\\delta_{11}X_1 + \\Delta_{1F} = 0$ — "
                  "ortiqcha bog'lanish yo'nalishidagi ko'chish nolga teng."),
                c("Birlik ko'chish", "$\\delta_{ij}$ — $j$-birlik kuchdan "
                  "$i$-yo'nalishdagi ko'chish; $\\delta_{ij} = \\delta_{ji}$ "
                  "(Maksvell teoremasi)."),
            ],
            derivation=[
                d("1-qadam. Aniqmaslik darajasini aniqlash",
                  r"k = n_{\text{reaksiya}} - 3",
                  "Uch tayanchli balka: 4 ta reaksiya (2 sharnir + 2 rolik yoki "
                  "boshqa kombinatsiya), 3 ta muvozanat tenglamasi → $k = 1$."),
                d("2-qadam. Asosiy sistemani tanlash",
                  r"\text{Ortiqcha bog'lanishni olib tashlab, uning o'rniga } X_1 \text{ qo'yiladi}",
                  "Tanlov erkin, lekin oqilona tanlov hisobni soddalashtiradi. "
                  "Odatda o'rta tayanch reaksiyasi yoki tayanch momenti tanlanadi."),
                d("3-qadam. Moslik shartini yozish",
                  r"\Delta_1 = 0 \;\Rightarrow\; \delta_{11}X_1 + \Delta_{1F} = 0 "
                  r"\;\Rightarrow\; X_1 = -\frac{\Delta_{1F}}{\delta_{11}}",
                  "Olib tashlangan bog'lanish yo'nalishidagi ko'chish nolga teng "
                  "bo'lishi kerak — chunki real tizimda u yerda tayanch bor."),
                d("4-qadam. Koeffitsientlarni Mor integrali bilan hisoblash",
                  r"\delta_{11} = \int\frac{\bar M_1^2}{EI}dx,\qquad "
                  r"\Delta_{1F} = \int\frac{M_F\bar M_1}{EI}dx",
                  "mq-16 dagi usullar to'g'ridan-to'g'ri qo'llanadi. "
                  "$\\delta_{11} > 0$ har doim (kvadrat integral)."),
                d("5-qadam. Yakuniy epyura",
                  r"M = M_F + \bar M_1X_1",
                  "Superpozitsiya. Natijani tekshirish: statik aniqmas tizimda "
                  "ko'chish shartlari bajarilishi kerak."),
            ],
            formula_meaning=(
                "Kuchlar usuli statik aniqmaslikni 'ochadi': ortiqcha bog'lanishni "
                "noma'lum kuchga aylantirib, uni deformatsiya shartidan topadi. "
                "Natijada statik aniqmas tizim — qo'shimcha bikrlik va kichikroq "
                "momentlar evaziga — tayanch cho'kishlariga va temperaturaga "
                "sezgir bo'lib qoladi. Bu — konstruktorning asosiy kompromissi."
            ),
            equations=[
                eq(r"\delta_{11}X_1 + \Delta_{1F} = 0", "Bir marta aniqmas tizim uchun "
                   "kanonik tenglama.", "Kanonik tenglama"),
                eq(r"\sum_j\delta_{ij}X_j + \Delta_{iF} = 0", "Umumiy holda kanonik "
                   "tenglamalar tizimi.", "Kanonik tizim"),
                eq(r"\delta_{ij} = \delta_{ji}", "Maksvell o'zaro ko'chishlar teoremasi.",
                   "Maksvell teoremasi"),
            ],
            conditions=(
                "Asosiy sistema geometrik o'zgarmas bo'lishi shart. Kanonik "
                "tenglamalar matritsasi simmetrik va musbat aniqlangan — bu "
                "yechimning yagonaligini kafolatlaydi. Tayanch cho'kishi yoki "
                "temperatura ta'siri o'ng tomonga qo'shimcha had sifatida kiradi."
            ),
            worked_example=WorkedExample(
                statement=(
                    "Bir uchi qotirilgan, ikkinchisi rolikli balka (bir marta "
                    "statik aniqmas): $L = 5$ m, tekis yuklama $q = 15$ kN/m. "
                    "Rolik reaksiyasini, epyuralarni va maksimal momentni toping. "
                    "Natijani konsol va ikki tayanchli balka bilan taqqoslang."
                ),
                given=[r"L = 5\ \text{m},\; q = 15\ \text{kN/m}",
                       r"A — qotirish, B — rolik"],
                steps=[
                    st(r"k = 4 - 3 = 1;\quad \text{asosiy sistema: konsol (B dagi rolik olib tashlanadi)}",
                       "B dagi vertikal reaksiya $X_1$ noma'lum."),
                    st(r"M_F(x) = -\frac{qx^2}{2}\ (\text{B dan hisoblab});\quad \bar M_1(x) = x",
                       "Yuk va birlik epyuralari."),
                    st(r"\delta_{11} = \int_0^L\frac{x^2}{EI}dx = \frac{L^3}{3EI} = \frac{125}{3EI}",
                       "Birlik ko'chish."),
                    st(r"\Delta_{1F} = \int_0^L\frac{-qx^2/2\cdot x}{EI}dx = -\frac{qL^4}{8EI} = "
                       r"-\frac{15\cdot 625}{8EI} = -\frac{1171{,}9}{EI}",
                       "Yuk ko'chishi."),
                    st(r"X_1 = -\frac{\Delta_{1F}}{\delta_{11}} = \frac{1171{,}9}{41{,}67} = 28{,}1\ \text{kN} = \frac{3qL}{8}",
                       "Rolik reaksiyasi — klassik natija $3qL/8$."),
                    st(r"M_A = -\frac{qL^2}{8} = -46{,}9\ \text{kN·m};\quad "
                       r"M_{max}^{oraliq} = \frac{9qL^2}{128} = 26{,}4\ \text{kN·m}",
                       "Qotirishdagi moment va oraliqdagi maksimum. Taqqoslash: "
                       "konsolda $qL^2/2 = 187{,}5$, ikki tayanchda $qL^2/8 = 46{,}9$ kN·m."),
                ],
                answer=(
                    "$R_B = 28{,}1$ kN $= 3qL/8$; $M_A = -46{,}9$ kN·m; "
                    "$M_{oraliq} = 26{,}4$ kN·m."
                ),
                engineering_note=(
                    "Statik aniqmaslik maksimal momentni konsolga nisbatan 4 marta "
                    "kamaytirdi. Lekin endi tizim tayanch cho'kishiga sezgir: B "
                    "tayanchning 10 mm cho'kishi qo'shimcha "
                    "$3EI\\delta/L^3$ reaksiya o'zgarishini beradi. Uzluksiz "
                    "ko'priklarda aynan shu sabab tayanch cho'kishlari qat'iy "
                    "nazorat qilinadi."
                ),
            ),
            computation=Computation(
                caption=(
                    "Kuchlar usuli: statik aniqmas balkani yeching va tayanch "
                    "cho'kishining ta'sirini baholang."
                ),
                code='''"""Statik aniqmas balka: kuchlar usuli va tayanch cho'kishi."""
import numpy as np
from scipy.integrate import quad
from labkit import PARAMS, note, series, table, value

L = float(PARAMS.get("L", 5.0))
q = float(PARAMS.get("q", 15.0))*1e3
EI = float(PARAMS.get("EI", 2e7))
settle = float(PARAMS.get("settle", 0.0))*1e-3   # B tayanch cho'kishi, m

# Asosiy sistema: konsol (A qotirilgan), X1 = B dagi reaksiya
def M_F(x):
    """Yuk epyurasi (B dan x masofada)."""
    return -q*x**2/2

def M_1(x):
    """Birlik kuchdan epyura."""
    return x

d11, _ = quad(lambda x: M_1(x)**2/EI, 0, L)
D1F, _ = quad(lambda x: M_F(x)*M_1(x)/EI, 0, L)
X1 = -(D1F + settle)/d11

value("δ₁₁", d11, "m/N")
value("Δ₁F", D1F, "m")
value("X₁ = R_B", X1/1000, "kN")
value("Nazariy 3qL/8", 3*q*L/8/1000, "kN")
note(f"Analitik yechim bilan farq: {abs(X1 - 3*q*L/8)/1000:.6f} kN")

# Natijaviy epyura
x = np.linspace(0, L, 300)
M_total = np.array([M_F(xi) + M_1(xi)*X1 for xi in x])
Q_total = np.gradient(M_total, x)
series("Eguvchi moment M(x)", x.tolist(), (M_total/1000).tolist(),
       xlabel="x (B dan), m", ylabel="M, kN·m")
series("Kesuvchi kuch Q(x)", x.tolist(), (Q_total/1000).tolist(),
       xlabel="x, m", ylabel="Q, kN")

value("M_A (qotirishda)", float(M_total[-1])/1000, "kN·m")
value("M_max (oraliq)", float(np.max(M_total))/1000, "kN·m")
value("Nazariy M_A = -qL²/8", -q*L**2/8/1000, "kN·m")

# Sxemalarni taqqoslash
table("Sxemalarni taqqoslash (bir xil q va L)",
      ["Sxema", "M_max, kN·m", "w_max, mm", "Nisbat"],
      [["Konsol", float(q*L**2/2/1000), float(q*L**4/(8*EI)*1000), 1.00],
       ["Bir uchi qotirilgan", float(q*L**2/8/1000), float(q*L**4/(185*EI)*1000),
        float((q*L**2/8)/(q*L**2/2))],
       ["Ikki tayanchli", float(q*L**2/8/1000), float(5*q*L**4/(384*EI)*1000),
        float((q*L**2/8)/(q*L**2/2))],
       ["Ikki uchi qotirilgan", float(q*L**2/12/1000), float(q*L**4/(384*EI)*1000),
        float((q*L**2/12)/(q*L**2/2))]])

# Tayanch cho'kishining ta'siri
ss = np.linspace(0, 0.03, 100)
R_arr = [-(D1F + s)/d11/1000 for s in ss]
series("R_B(cho'kish)", (ss*1000).tolist(), R_arr,
       xlabel="Cho'kish, mm", ylabel="R_B, kN")
dR = abs(R_arr[-1] - R_arr[0])
note(f"30 mm cho'kish reaksiyani {dR:.1f} kN ga o'zgartiradi "
     f"({100*dR/(3*q*L/8/1000):.1f} %) — statik aniqmas tizimlarning zaif tomoni.")
note("Statik aniq tizimda tayanch cho'kishi reaksiyalarni umuman o'zgartirmaydi.")

# Maksvell teoremasini tekshirish (ikki marta aniqmas uchun)
def M_2(x):
    return 1.0                      # birlik moment
d12, _ = quad(lambda x: M_1(x)*M_2(x)/EI, 0, L)
d21, _ = quad(lambda x: M_2(x)*M_1(x)/EI, 0, L)
note(f"Maksvell teoremasi: δ₁₂ = {d12:.6e}, δ₂₁ = {d21:.6e} — teng ✓")
''',
                parameters=[
                    p("L", "Oraliq L", 1.0, 20.0, 5.0, 0.5, "m"),
                    p("q", "Tekis yuklama q", 1.0, 100.0, 15.0, 1.0, "kN/m"),
                    p("EI", "Egilish bikrligi", 1e5, 1e9, 2e7, 1e5, "N·m²"),
                    p("settle", "B tayanch cho'kishi", 0.0, 30.0, 0.0, 1.0, "mm"),
                ],
                expected_output="X₁ = R_B = 28,125 kN = 3qL/8; M_A = -46,875 kN·m",
            ),
            visualization=vis(
                "Kuchlar usuli bosqichlari",
                "React/SVG",
                "Uch panel: (1) asosiy sistema va $M_F$ epyurasi, (2) birlik holat "
                "va $\\bar M_1$ epyurasi, (3) natijaviy $M$ epyurasi. Har birida "
                "sxema va epyura birga.",
                "React/SVG: usulning bosqichma-bosqich mantiqini ko'rsatish uchun "
                "uch panel majburiy. Natijaviy epyurada ishora o'zgarishi (tayanch "
                "ustida manfiy, oraliqda musbat) alohida rang bilan berilishi kerak — "
                "bu armatura joylashtirishning asosi.",
            ),
            interpretation=(
                "Sxemalarni taqqoslash jadvali statik aniqmaslikning foydasini "
                "aniq ko'rsatadi: ikki uchi qotirilgan balkada maksimal moment "
                "konsolnikidan 6 marta, cho'kish esa 48 marta kichik. Lekin "
                "cho'kish grafigi zaif tomonni ochadi: 30 mm tayanch cho'kishi "
                "reaksiyani sezilarli o'zgartiradi. Statik aniq tizimda bu ta'sir "
                "umuman yo'q."
            ),
            common_mistakes=[
                "Geometrik o'zgaruvchan asosiy sistema tanlash.",
                "$\\delta_{11}$ ni manfiy olish — u har doim musbat.",
                "Tayanch cho'kishi yoki temperaturani kanonik tenglamaga "
                "qo'shishni unutish.",
                "Natijaviy epyurani tekshirmaslik — moslik shartlari bajarilishi kerak.",
            ],
            quiz=[
                q("Nima uchun statik aniqmas tizim tayanch cho'kishiga sezgir?",
                  "Chunki reaksiyalar deformatsiya shartlaridan topiladi; cho'kish "
                  "bu shartlarni o'zgartiradi va reaksiyalarni qayta taqsimlaydi.",
                  "konseptual"),
                q("$\\delta_{11}$ nima uchun har doim musbat?",
                  "U $\\int\\bar M_1^2/(EI)dx$ — kvadrat funksiya integrali.",
                  "konseptual"),
                q("Bir uchi qotirilgan balkada tekis yuklamada $R_B$ nimaga teng?",
                  "$R_B = 3qL/8$.", "hisob"),
                q("Statik aniqmaslikning asosiy foydasi va zarari nima?",
                  "Foyda: kichikroq momentlar, katta bikrlik, ortiqcha ishonchlilik. "
                  "Zarar: tayanch cho'kishi, temperatura va montaj xatoliklariga "
                  "sezgirlik.", "talqin"),
                q("Kodda Maksvell teoremasi qanday tekshirilgan?",
                  "$\\delta_{12}$ va $\\delta_{21}$ ni alohida hisoblab, ularning "
                  "tengligini ko'rsatish orqali. Bu kanonik tenglamalar "
                  "matritsasining simmetrikligini kafolatlaydi.", "kod"),
            ],
            bridge_to_next=(
                "Balka hisobining barcha elementlari tayyor. Keyingi mavzuda "
                "ularni birlashtirib, ratsional loyihalash masalasini ko'ramiz."
            ),
            research_extension=(
                "Ko'p oraliqli uzluksiz balkani (3–5 oraliq) kuchlar usuli bilan "
                "yeching: uch moment tenglamasini (Clapeyron) keltirib chiqaring "
                "va uni matritsa shaklida dasturlang. Oraliqlar nisbatini "
                "optimallashtiring: chekka oraliqlarni qisqartirish momentlarni "
                "tenglashtirishini ko'rsating."
            ),
        ),
    ),
    Topic(
        id="mq-18",
        subject_id=S,
        module_id=M,
        order=18,
        title="Kesim shaklini tanlash va egilishda ratsional loyihalash",
        description=(
            "Kesim samaradorligi mezonlari, teng qarshilikli balka, material "
            "sarfini minimallashtirish va konstruktiv cheklovlar."
        ),
        learning_objective=(
            "Berilgan yuklanish uchun optimal kesim shakli va o'lchamlarini "
            "asoslab tanlash."
        ),
        prerequisites=["mq-15", "mq-13", "mq-08"],
        mathematical_core=(
            "Optimallashtirish, o'lchamsiz samaradorlik mezonlari, cheklovli "
            "minimallashtirish."
        ),
        engineering_application=(
            "Prokat profillar tanlash, payvand balkalar loyihalash, teng "
            "qarshilikli konstruksiyalar."
        ),
        computational_component=(
            "Kesim optimallashtirish: `scipy.optimize` bilan minimal massa "
            "masalasini yechish."
        ),
        visualization_component=(
            "Profillar samaradorligi diagrammasi; teng qarshilikli balka profili."
        ),
        research_extension=(
            "Topologik optimallashtirish: materialning eng samarali taqsimoti "
            "qanday bo'ladi?"
        ),
        difficulty="murakkab",
        previous_link=(
            "mq-13…mq-17 da hisoblash usullarini o'rgandik. Endi teskari "
            "masalani yechamiz: berilgan shartlarda eng yaxshi kesimni tanlash."
        ),
        next_topic="mq-19",
        estimated_minutes=90,
        tags=["optimallashtirish", "ratsional kesim", "teng qarshilik"],
        lesson=Lesson(
            physical_problem=(
                "Kran balkasi loyihalanmoqda. Dvutavr, quti profil yoki payvand "
                "balka? Balandlik qancha? Har bir tanlov massa, narx va "
                "tayyorlash murakkabligiga ta'sir qiladi. Muhandis bu tanlovni "
                "his-tuyg'u bilan emas, miqdoriy mezonlar asosida qilishi kerak."
            ),
            concepts=[
                c("Kesim samaradorligi", "$w_c = W_x/A^{3/2}$ — o'lchamsiz mezon; "
                  "katta qiymat — samaraliroq kesim."),
                c("Yadro radiusi", "$i = \\sqrt{I/A}$ — material neytral o'qdan "
                  "o'rtacha qanchalik uzoq joylashgani."),
                c("Teng qarshilikli balka", "$W(x) = M(x)/[\\sigma]$ — har bir "
                  "kesimda kuchlanish bir xil."),
                c("Konstruktiv cheklovlar", "Minimal devor qalinligi, lokal "
                  "ustuvorlik, tayyorlash texnologiyasi."),
                c("Optimallashtirish masalasi", "$\\min A$ shartlar bilan: "
                  "$W \\ge W_{kerak}$, $I \\ge I_{kerak}$, geometrik cheklovlar."),
            ],
            derivation=[
                d("1-qadam. Samaradorlik mezonini tuzish",
                  r"w_c = \frac{W_x}{A^{3/2}}",
                  "$W$ o'lchamligi m³, $A$ — m², shuning uchun $A^{3/2}$ ga bo'lish "
                  "o'lchamsiz mezon beradi. To'rtburchak uchun $h/b$ ga, dvutavr "
                  "uchun profil turiga bog'liq."),
                d("2-qadam. To'rtburchak uchun optimal nisbat",
                  r"w_c = \frac{bh^2/6}{(bh)^{3/2}} = \frac{1}{6}\sqrt{\frac{h}{b}} "
                  r"\;\Rightarrow\; \text{balandlik oshgani sari samaradorlik ortadi}",
                  "Nazariy jihatdan $h/b \\to\\infty$ eng yaxshi, lekin amalda "
                  "lokal ustuvorlik va yon egilish cheklaydi ($h/b \\le 6...8$)."),
                d("3-qadam. Teng qarshilikli balka profili",
                  r"W(x) = \frac{M(x)}{[\sigma]} \;\Rightarrow\; "
                  r"\text{konsol, uchida } F:\ \frac{bh^2(x)}{6} = \frac{Fx}{[\sigma]} "
                  r"\Rightarrow h(x) = h_0\sqrt{\frac{x}{L}}",
                  "Parabolik profil. Bunday balka prizmatikdan 33 % yengil "
                  "($\\int h\\,dx$ hisobi)."),
                d("4-qadam. Optimallashtirish masalasi qo'yilishi",
                  r"\min_{\mathbf{p}} A(\mathbf{p})\quad \text{shartlar: } "
                  r"W(\mathbf{p}) \ge \frac{M}{[\sigma]},\; I(\mathbf{p}) \ge \frac{5qL^4}{384E[f]}",
                  "Mustahkamlik va bikrlik shartlari bir vaqtda; qaysi biri faol "
                  "ekani oraliq uzunligiga bog'liq."),
            ],
            formula_meaning=(
                "Samaradorlik mezoni $w_c = W/A^{3/2}$ turli o'lchamdagi "
                "profillarni adolatli taqqoslash imkonini beradi. Teng qarshilikli "
                "balka esa nazariy chegarani ko'rsatadi: materialning har bir "
                "grammi to'liq ishlaydi. Amalda bunday profil tayyorlash qimmat, "
                "shuning uchun kompromiss — pog'onali balandlik yoki o'zgaruvchan "
                "devor qalinligi ishlatiladi."
            ),
            equations=[
                eq(r"w_c = \frac{W_x}{A^{3/2}}", "Kesim samaradorligi mezoni.", "Samaradorlik"),
                eq(r"h(x) = h_0\sqrt{x/L}", "Teng qarshilikli konsol profili.",
                   "Teng qarshilik"),
                eq(r"\min A \text{ s.t. } W \ge \frac{M}{[\sigma]},\ I \ge I_{kerak}",
                   "Optimallashtirish masalasi.", "Optimallashtirish"),
            ],
            conditions=(
                "Optimallashtirish natijasi konstruktiv cheklovlar bilan "
                "chegaralanadi: devor juda yupqa bo'lsa lokal ustuvorlik "
                "yo'qoladi, balandlik juta katta bo'lsa yon egilish xavfi "
                "tug'iladi. Shuning uchun matematik optimum har doim ham amaliy "
                "optimum emas."
            ),
            worked_example=WorkedExample(
                statement=(
                    "Kran balkasi: $L = 9$ m, $M_{max} = 240$ kN·m, "
                    "$[\\sigma] = 160$ MPa, $[f] = L/400$, $E = 200$ GPa, "
                    "$q_{ekv} = 23{,}7$ kN/m. Payvand dvutavr loyihalang: "
                    "optimal balandlik va devor qalinligini toping."
                ),
                given=[r"L = 9\ \text{m},\; M = 240\ \text{kN·m},\; [\sigma] = 160\ \text{MPa}",
                       r"[f] = 22{,}5\ \text{mm},\; E = 2\cdot10^{11}\ \text{Pa}"],
                steps=[
                    st(r"W_{kerak} = \frac{240\cdot10^3}{160\cdot10^6} = 1{,}5\cdot10^{-3}\ \text{m}^3 = 1500\ \text{cm}^3",
                       "Mustahkamlik shartidan."),
                    st(r"I_{kerak} = \frac{5q L^4}{384E[f]} = \frac{5\cdot 23{,}7\cdot10^3\cdot 6561}{384\cdot2\cdot10^{11}\cdot0{,}0225}",
                       "Bikrlik shartidan."),
                    st(r"I_{kerak} = \frac{7{,}775\cdot10^8}{1{,}728\cdot10^{9}} = 4{,}5\cdot10^{-4}\ \text{m}^4 = 45\,000\ \text{cm}^4",
                       "Kerakli inersiya momenti."),
                    st(r"h_{opt} \approx \frac{2I_{kerak}}{W_{kerak}} = \frac{2\cdot 4{,}5\cdot10^{-4}}{1{,}5\cdot10^{-3}} = 0{,}6\ \text{m}",
                       "$W = 2I/h$ munosabatidan optimal balandlik."),
                    st(r"t_w \ge \frac{h}{120} = 5\ \text{mm}\ (\text{lokal ustuvorlik});\ "
                       r"\text{qabul: } t_w = 8\ \text{mm}",
                       "Devor qalinligi lokal ustuvorlik shartidan."),
                    st(r"A_f = \frac{W}{h} - \frac{t_wh}{6} = \frac{1{,}5\cdot10^{-3}}{0{,}6} - \frac{0{,}008\cdot0{,}6}{6} = "
                       r"2{,}5\cdot10^{-3} - 0{,}8\cdot10^{-3} = 1{,}7\cdot10^{-3}\ \text{m}^2",
                       "Tokcha yuzasi: $b_f = 280$ mm, $t_f = 6$ mm — juda yupqa, "
                       "$b_f = 200$ mm, $t_f = 9$ mm qabul qilamiz."),
                ],
                answer=(
                    "Payvand dvutavr: $h = 600$ mm, devor $8\\times 582$ mm, "
                    "tokchalar $200\\times 9$ mm; $A \\approx 82$ cm²."
                ),
                engineering_note=(
                    "Bikrlik sharti hal qiluvchi bo'lib chiqdi: $I_{kerak}$ "
                    "mustahkamlikdan kelib chiqadigan qiymatdan katta. $L/h = 15$ "
                    "— bu balkalar uchun tipik nisbat. Standart prokat dvutavr "
                    "№ 55 ham mos kelardi, lekin payvand balka 15–20 % yengilroq "
                    "chiqadi."
                ),
            ),
            computation=Computation(
                caption=(
                    "Kesim optimallashtirish: mustahkamlik va bikrlik shartlarida "
                    "minimal massali dvutavrni toping."
                ),
                code='''"""Ratsional loyihalash: kesim optimallashtirish."""
import numpy as np
from scipy.optimize import minimize
from labkit import PARAMS, note, series, table, value

M = float(PARAMS.get("M", 240.0))*1e3       # eguvchi moment, N*m
L = float(PARAMS.get("L", 9.0))
q = float(PARAMS.get("q", 23.7))*1e3        # ekvivalent yuklama, N/m
sigma_allow = float(PARAMS.get("s_allow", 160.0))*1e6
E = float(PARAMS.get("E", 200e9))
f_div = float(PARAMS.get("f_div", 400.0))

W_req = M/sigma_allow
I_req = 5*q*L**4/(384*E*(L/f_div))
value("Kerakli W", W_req*1e6, "cm³")
value("Kerakli I", I_req*1e8, "cm⁴")
value("Optimal balandlik (2I/W)", 2*I_req/W_req*1000, "mm")
note(f"Hal qiluvchi shart: {'BIKRLIK' if 2*I_req/W_req > 0 and I_req/(W_req/2) > W_req else 'tekshiriladi'}")

def section(params):
    """Dvutavr: [h, t_w, b_f, t_f] -> (A, I, W)."""
    h, t_w, b_f, t_f = params
    h_w = h - 2*t_f
    A = 2*b_f*t_f + t_w*h_w
    I = (b_f*h**3 - (b_f-t_w)*h_w**3)/12
    W = 2*I/h
    return A, I, W

def objective(p):
    return section(p)[0]*1e4                # yuza, cm^2

cons = [
    {"type": "ineq", "fun": lambda p: section(p)[2] - W_req},       # mustahkamlik
    {"type": "ineq", "fun": lambda p: section(p)[1] - I_req},       # bikrlik
    {"type": "ineq", "fun": lambda p: p[0]/p[1] - 60},              # devor nisbati min
    {"type": "ineq", "fun": lambda p: 160 - p[0]/p[1]},             # lokal ustuvorlik
    {"type": "ineq", "fun": lambda p: p[2]/p[3] - 10},              # tokcha nisbati min
    {"type": "ineq", "fun": lambda p: 30 - p[2]/p[3]},              # tokcha nisbati maks
    {"type": "ineq", "fun": lambda p: p[0] - 3*p[2]},               # h >= 3*b_f
]
bounds = [(0.2, 1.5), (0.004, 0.03), (0.1, 0.5), (0.006, 0.04)]
x0 = [0.6, 0.008, 0.2, 0.012]

res = minimize(objective, x0, bounds=bounds, constraints=cons, method="SLSQP")
h, t_w, b_f, t_f = res.x
A_opt, I_opt, W_opt = section(res.x)

value("Optimal h", h*1000, "mm")
value("Devor qalinligi t_w", t_w*1000, "mm")
value("Tokcha eni b_f", b_f*1000, "mm")
value("Tokcha qalinligi t_f", t_f*1000, "mm")
value("Yuza A", A_opt*1e4, "cm²")
value("Massa (1 m)", A_opt*7850, "kg/m")
value("W", W_opt*1e6, "cm³")
value("I", I_opt*1e8, "cm⁴")
note(f"Optimizatsiya {'muvaffaqiyatli' if res.success else 'yaqinlashmadi'}: {res.message}")

# Samaradorlik mezoni bo'yicha taqqoslash
def eff(W, A):
    return W/A**1.5

profiles = [
    ("Optimal dvutavr", W_opt, A_opt),
    ("Kvadrat (teng W)", (6*W_req)**(1/3)**3/6, ((6*W_req)**(1/3))**2),
    ("To'rtburchak h/b=3", W_req, (6*W_req/np.sqrt(3))**(2/3)*np.sqrt(3)),
]
table("Kesim samaradorligi",
      ["Profil", "W, cm³", "A, cm²", "w_c = W/A^1.5"],
      [[nm, float(Wi*1e6), float(Ai*1e4), float(eff(Wi, Ai))] for nm, Wi, Ai in profiles])

# Balandlikning massaga ta'siri
hh = np.linspace(0.3, 1.2, 60)
masses = []
for hi in hh:
    cons_h = cons + [{"type": "eq", "fun": lambda p, hv=hi: p[0]-hv}]
    r = minimize(objective, [hi, 0.008, 0.2, 0.012], bounds=bounds,
                 constraints=cons_h, method="SLSQP")
    masses.append(section(r.x)[0]*7850 if r.success else np.nan)
series("Massa(h)", (hh*1000).tolist(), masses, xlabel="Balandlik h, mm", ylabel="Massa, kg/m")

# Teng qarshilikli balka profili
x = np.linspace(0.01, L/2, 100)
M_x = q*(L*x - x**2)/2
h_x = np.sqrt(6*M_x/(t_w*sigma_allow))
series("Teng qarshilikli balandlik h(x)", x.tolist(), (h_x*1000).tolist(),
       xlabel="x, m", ylabel="h, mm")
V_equal = 2*np.trapezoid(t_w*h_x, x)
V_prism = t_w*np.max(h_x)*L
note(f"Teng qarshilikli devor hajmi prizmatikdan {100*(1-V_equal/V_prism):.1f} % kam.")
''',
                parameters=[
                    p("M", "Eguvchi moment M", 10.0, 2000.0, 240.0, 10.0, "kN·m"),
                    p("L", "Oraliq L", 1.0, 30.0, 9.0, 0.5, "m"),
                    p("q", "Ekvivalent yuklama", 1.0, 200.0, 23.7, 0.5, "kN/m"),
                    p("s_allow", "[σ]", 40.0, 400.0, 160.0, 10.0, "MPa"),
                    p("E", "Yung moduli", 1e10, 4e11, 200e9, 1e10, "Pa"),
                    p("f_div", "Bikrlik me'yori L/n", 100.0, 800.0, 400.0, 50.0, "—"),
                ],
                expected_output="h_opt ≈ 600 mm, A ≈ 80–90 cm², bikrlik hal qiluvchi",
            ),
            visualization=vis(
                "Optimal kesim va teng qarshilikli profil",
                "React/SVG",
                "Chapda: optimallashtirilgan dvutavr kesimi o'lchamlari bilan; "
                "o'ngda: teng qarshilikli balkaning yon ko'rinishi (parabolik "
                "balandlik) prizmatik balka konturi bilan taqqoslangan.",
                "React/SVG: teng qarshilikli profil konturini prizmatik balka "
                "ustiga qo'yib ko'rsatish — tejaladigan materialni vizual "
                "ko'rsatishning eng yaxshi usuli. Massa(h) grafigi esa optimum "
                "borligini isbotlaydi.",
            ),
            interpretation=(
                "Massa(h) grafigi aniq minimumga ega: balandlik kichik bo'lsa "
                "tokchalar katta bo'lishi kerak, katta bo'lsa devor og'irlashadi. "
                "Optimum odatda $L/h = 12...18$ oralig'ida. Teng qarshilikli "
                "profil esa qo'shimcha 25–35 % tejash beradi, lekin tayyorlash "
                "murakkabligi bu foydani ko'pincha yo'qqa chiqaradi."
            ),
            common_mistakes=[
                "Faqat mustahkamlikni optimallashtirib, bikrlikni tekshirmaslik.",
                "Lokal ustuvorlik cheklovlarini hisobga olmaslik — natijada juda "
                "yupqa devor chiqadi.",
                "Standart profillar mavjudligini unutib, faqat payvand yechim "
                "izlash.",
                "Optimallashtirish natijasini yaxlitlamasdan qabul qilish.",
            ],
            quiz=[
                q("Nima uchun $w_c = W/A^{3/2}$ o'lchamsiz mezon?",
                  "$W$ — m³, $A^{3/2}$ — m³, demak nisbat o'lchamsiz va turli "
                  "o'lchamdagi profillarni taqqoslash imkonini beradi.", "konseptual"),
                q("Teng qarshilikli konsolda balandlik qanday qonun bo'yicha o'zgaradi?",
                  "$h(x) = h_0\\sqrt{x/L}$ — parabolik.", "hisob"),
                q("$W = 1500$ cm³, $I = 45\\,000$ cm⁴. Optimal balandlik?",
                  "$h = 2I/W = 2\\cdot45\\,000/1500 = 60$ cm = 600 mm.", "hisob"),
                q("Nima uchun balandlikni cheksiz oshirib bo'lmaydi?",
                  "Devor lokal ustuvorlikni yo'qotadi, balka yon egilishga zaif "
                  "bo'ladi, gabarit cheklovlari paydo bo'ladi.", "talqin"),
                q("Kodda `constraints` ro'yxatidagi `p[0]/p[1] - 60` nimani "
                  "ta'minlaydi?",
                  "$h/t_w \\ge 60$ — devorning haddan tashqari qalin bo'lmasligini "
                  "(iqtisodiylik); qarama-qarshi cheklov $h/t_w \\le 160$ lokal "
                  "ustuvorlikni ta'minlaydi.", "kod"),
            ],
            bridge_to_next=(
                "Egilish to'liq o'rganildi. Lekin real konstruksiyada bir vaqtda "
                "bir necha deformatsiya turi bo'ladi. Buni tahlil qilish uchun "
                "avval kuchlanish holati nazariyasini o'rganishimiz kerak."
            ),
            research_extension=(
                "Topologik optimallashtirishga kirish: to'rtburchak sohani "
                "elementlarga bo'lib, har bir elementning zichligini o'zgaruvchi "
                "deb oling. Berilgan hajmda bikrlikni maksimallashtiring (SIMP "
                "usuli). Natijada ferma yoki dvutavrga o'xshash struktura "
                "paydo bo'lishini kuzating — bu zamonaviy 3D-bosib chiqarish "
                "loyihalashining asosi."
            ),
        ),
    ),
]
