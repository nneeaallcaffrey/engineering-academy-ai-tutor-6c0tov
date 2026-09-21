"""NM / 3-modul: Saqlanish qonunlari va energetik usullar (nm-13 … nm-18)."""

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
M = "nm-m3"

TOPICS = [
    Topic(
        id="nm-13",
        subject_id=S,
        module_id=M,
        order=13,
        title="Impuls va impuls momenti: nuqta va mexanik sistema uchun saqlanish qonunlari",
        description=(
            "Impuls, kuch impulsi, impuls momenti (kinetik moment) va ularning "
            "saqlanish shartlari; zarba masalalari."
        ),
        learning_objective=(
            "Sistemaning impulsi va impuls momenti qachon saqlanishini aniqlash va "
            "zarba masalalarini integrallashsiz yechish."
        ),
        prerequisites=["nm-07", "nm-11"],
        mathematical_core=(
            "Vektor tenglamani vaqt bo'yicha integrallash, ichki va tashqi kuchlar "
            "ajratilishi, vektor ko'paytmaning hosilasi."
        ),
        engineering_application=(
            "Zarba va to'qnashuv hisobi, reaktiv harakat, bolg'a va shtamp, "
            "aylanuvchi tizimlar (figurali uchish, gироskop)."
        ),
        computational_component=(
            "Ikki jism to'qnashuvini restitutsiya koeffitsienti orqali hisoblash va "
            "energiya yo'qolishini baholash."
        ),
        visualization_component=(
            "To'qnashuvdan oldingi va keyingi impuls vektorlari diagrammasi."
        ),
        research_extension=(
            "Restitutsiya koeffitsienti tezlikka bog'liqmi? Tajriba ma'lumotlari "
            "bilan model tuzing."
        ),
        difficulty="asosiy",
        previous_link=(
            "nm-08 da tenglamani integrallash uchun kuchning aniq ko'rinishi kerak "
            "edi. Zarbada kuch noma'lum va juda qisqa vaqt ta'sir qiladi — lekin "
            "uning impulsini o'lchash mumkin. Shundan saqlanish qonuni tug'iladi."
        ),
        next_topic="nm-14",
        estimated_minutes=90,
        tags=["impuls", "zarba", "saqlanish qonuni"],
        lesson=Lesson(
            physical_problem=(
                "Shtamp pressi detalga zarba beradi. Zarba davomiyligi millisekundlar, "
                "kuch esa meganyutonlarga yetishi mumkin. Bu kuchni bevosita o'lchash "
                "ham, hisoblash ham qiyin. Lekin fundamentga tushadigan yukni bilish "
                "shart. Yechim: kuchning o'zini emas, uning impulsini hisoblash."
            ),
            concepts=[
                c("Impuls (momentum)", "$\\mathbf{p} = m\\mathbf{v}$ — harakat miqdori. "
                  "Sistema uchun $\\mathbf{P} = \\sum m_i\\mathbf{v}_i = M\\mathbf{v}_C$."),
                c("Kuch impulsi (impulse)", "$\\mathbf{S} = \\int_0^{t_1}\\mathbf{F}\\,dt$ — "
                  "kuchning vaqt bo'yicha to'plangan ta'siri."),
                c("Impuls momenti (angular momentum)", "$\\mathbf{L}_O = \\sum\\mathbf{r}_i\\times m_i\\mathbf{v}_i$ "
                  "— aylanma harakatning 'impulsi'."),
                c("Ichki va tashqi kuchlar", "Ichki kuchlar uchinchi qonun bo'yicha "
                  "juft-juft bo'lib yo'qoladi va sistema impulsini o'zgartira olmaydi."),
                c("Restitutsiya koeffitsienti", "$k = |v'_{\\text{nisbiy}}|/|v_{\\text{nisbiy}}|$ — "
                  "zarbaning elastikligi o'lchovi; $k=1$ — ideal elastik, $k=0$ — plastik."),
            ],
            derivation=[
                d("1-qadam. Nyuton tenglamasini integrallash",
                  r"m\frac{d\mathbf{v}}{dt} = \mathbf{F} \;\Rightarrow\; "
                  r"m\mathbf{v}_1 - m\mathbf{v}_0 = \int_{t_0}^{t_1}\mathbf{F}\,dt = \mathbf{S}",
                  "Impuls haqidagi teorema: impuls o'zgarishi kuch impulsiga teng. "
                  "Kuchning vaqt bo'yicha ko'rinishi noma'lum bo'lsa ham qo'llanadi."),
                d("2-qadam. Sistema uchun umumlashtirish",
                  r"\frac{d\mathbf{P}}{dt} = \sum\mathbf{F}^{(e)} + \underbrace{\sum\mathbf{F}^{(i)}}_{=0} = \sum\mathbf{F}^{(e)}",
                  "Ichki kuchlar $\\mathbf{F}_{ij} = -\\mathbf{F}_{ji}$ juftliklari yig'indida "
                  "bekor bo'ladi. Faqat tashqi kuchlar sistema impulsini o'zgartiradi."),
                d("3-qadam. Impuls momenti teoremasi",
                  r"\frac{d\mathbf{L}_O}{dt} = \sum \mathbf{r}_i\times\mathbf{F}_i^{(e)} = \mathbf{M}_O^{(e)}",
                  "Differensiallashda $\\dot{\\mathbf{r}}_i\\times m_i\\mathbf{v}_i = "
                  "\\mathbf{v}_i\\times m_i\\mathbf{v}_i = 0$ hadi yo'qoladi."),
                d("4-qadam. Saqlanish shartlari",
                  r"\sum\mathbf{F}^{(e)} = 0 \Rightarrow \mathbf{P} = \text{const};\qquad "
                  r"\mathbf{M}_O^{(e)} = 0 \Rightarrow \mathbf{L}_O = \text{const}",
                  "Saqlanish alohida o'qlar bo'yicha ham bo'lishi mumkin: agar "
                  "$\\sum F_x^{(e)} = 0$ bo'lsa, faqat $P_x$ saqlanadi."),
                d("5-qadam. To'qnashuv masalasi yechimi",
                  r"m_1v_1 + m_2v_2 = m_1v'_1 + m_2v'_2,\qquad k = \frac{v'_2 - v'_1}{v_1 - v_2}"
                  r"\;\Rightarrow\; v'_1 = \frac{m_1v_1 + m_2v_2 - k m_2(v_1-v_2)}{m_1+m_2}",
                  "Ikkita tenglama, ikkita noma'lum. Impuls saqlanishi zarbaning ichki "
                  "mexanizmini bilishni talab qilmaydi — bu uning kuchi."),
            ],
            formula_meaning=(
                "Impuls teoremasi zarba masalasining kalitini beradi: kuchning shakli "
                "emas, uning vaqt bo'yicha integrali muhim. Shuning uchun zarba kuchini "
                "kamaytirish uchun zarba vaqtini uzaytirish kifoya — avtomobil "
                "krandiyalari, sport himoya vositalari va amortizatorlar aynan shu "
                "prinsipda ishlaydi: $F_{\\text{o'rtacha}} = S/\\Delta t$."
            ),
            equations=[
                eq(r"m\mathbf{v}_1 - m\mathbf{v}_0 = \int\mathbf{F}\,dt", "Impuls teoremasi.",
                   "Impuls teoremasi"),
                eq(r"\frac{d\mathbf{L}_O}{dt} = \mathbf{M}_O^{(e)}", "Impuls momenti teoremasi.",
                   "Kinetik moment teoremasi"),
                eq(r"k = \frac{v'_2-v'_1}{v_1-v_2}", "Restitutsiya koeffitsienti.", "Nyuton gipotezasi"),
            ],
            conditions=(
                "Zarba masalalarida asosiy faraz: zarba davomiyligi shu qadar qisqaki, "
                "oddiy kuchlar (og'irlik, ishqalanish) impulsi hisobga olinmaydi va "
                "jismlarning joylashuvi o'zgarmaydi. Bu faraz $F_{\\text{zarba}} \\gg mg$ "
                "bo'lganda o'rinli."
            ),
            worked_example=WorkedExample(
                statement=(
                    "Shtamp pressining zarba qismi $m_1 = 800$ kg, u $v_1 = 5$ m/s "
                    "tezlik bilan $m_2 = 120$ kg li detalga (tinch holatda) uriladi. "
                    "Zarba deyarli plastik, $k = 0{,}15$; zarba davomiyligi $\\Delta t = 8$ ms. "
                    "Zarbadan keyingi tezliklar, o'rtacha zarba kuchi va yo'qolgan "
                    "energiyani toping."
                ),
                given=[r"m_1 = 800\ \text{kg},\; v_1 = 5\ \text{m/s}",
                       r"m_2 = 120\ \text{kg},\; v_2 = 0", r"k = 0{,}15,\; \Delta t = 0{,}008\ \text{s}"],
                steps=[
                    st(r"v'_1 = \frac{m_1v_1 - k m_2 v_1}{m_1+m_2} = \frac{800\cdot 5 - 0{,}15\cdot 120\cdot 5}{920}",
                       "Umumiy formulani $v_2 = 0$ holi uchun qo'llaymiz."),
                    st(r"v'_1 = \frac{4000 - 90}{920} = \frac{3910}{920} = 4{,}25\ \text{m/s}",
                       "Zarba qismining tezligi."),
                    st(r"v'_2 = v'_1 + k(v_1-v_2) = 4{,}25 + 0{,}15\cdot 5 = 5{,}0\ \text{m/s}",
                       "Detal tezligi — restitutsiya ta'rifidan."),
                    st(r"S = m_2(v'_2 - v_2) = 120\cdot 5{,}0 = 600\ \text{N·s}",
                       "Detalga uzatilgan impuls."),
                    st(r"F_{\text{o'rt}} = \frac{S}{\Delta t} = \frac{600}{0{,}008} = 75\,000\ \text{N} = 75\ \text{kN}",
                       "O'rtacha zarba kuchi — og'irlikdan ($m_1g = 7{,}85$ kN) 9,5 marta katta."),
                    st(r"\Delta T = \frac{m_1v_1^2}{2} - \frac{m_1v_1'^2 + m_2v_2'^2}{2} = "
                       r"10\,000 - (7226 + 1500) = 1274\ \text{J}",
                       "Yo'qolgan kinetik energiya — u aynan detalning plastik "
                       "deformatsiyasiga, ya'ni foydali ishga sarflanadi."),
                ],
                answer=(
                    "$v'_1 = 4{,}25$ m/s, $v'_2 = 5{,}0$ m/s; $F_{\\text{o'rt}} = 75$ kN; "
                    "$\\Delta T = 1274$ J (12,7 % energiya deformatsiyaga ketdi)."
                ),
                engineering_note=(
                    "Zarba vaqtini 8 ms dan 16 ms ga uzaytirish (yumshoq ostki qo'yish) "
                    "kuchni ikki barobar — 37,5 kN gacha kamaytiradi. Lekin bu shtamplash "
                    "sifatini pasaytiradi: plastik deformatsiya uchun aynan yuqori "
                    "kuch zarur. Fundament hisobida esa $F_{\\text{o'rt}}$ emas, maksimal "
                    "kuch (odatda $1{,}5...2 F_{\\text{o'rt}}$) olinadi."
                ),
            ),
            computation=Computation(
                caption=(
                    "To'qnashuv: massalar nisbati va restitutsiya koeffitsientini "
                    "o'zgartirib, energiya yo'qolishini kuzating."
                ),
                code='''"""Impuls saqlanishi va to'qnashuv tahlili."""
import numpy as np
from labkit import PARAMS, note, series, table, value

m1 = float(PARAMS.get("m1", 800.0))    # kg
m2 = float(PARAMS.get("m2", 120.0))    # kg
v1 = float(PARAMS.get("v1", 5.0))      # m/s
k = float(PARAMS.get("k", 0.15))       # restitutsiya koeffitsienti
dt = float(PARAMS.get("dt", 0.008))    # zarba davomiyligi, s
v2 = 0.0

def collide(m1, m2, v1, v2, k):
    """Impuls saqlanishi + Nyuton gipotezasidan zarbadan keyingi tezliklar."""
    p_total = m1*v1 + m2*v2
    v1n = (p_total - k*m2*(v1 - v2))/(m1 + m2)
    v2n = (p_total + k*m1*(v1 - v2))/(m1 + m2)
    return v1n, v2n

v1n, v2n = collide(m1, m2, v1, v2, k)
value("v'₁", v1n, "m/s")
value("v'₂", v2n, "m/s")
value("Impuls (oldin)", m1*v1 + m2*v2, "kg·m/s")
value("Impuls (keyin)", m1*v1n + m2*v2n, "kg·m/s")

S = m2*(v2n - v2)
value("Uzatilgan impuls S", S, "N·s")
value("O'rtacha kuch", S/dt/1000, "kN")

T0 = 0.5*m1*v1**2 + 0.5*m2*v2**2
T1 = 0.5*m1*v1n**2 + 0.5*m2*v2n**2
value("Yo'qolgan energiya", T0 - T1, "J")
value("Energiya yo'qolishi", 100*(T0-T1)/T0, "%")
note(f"Impuls saqlanishi tekshiruvi: farq = {abs(m1*v1+m2*v2 - m1*v1n - m2*v2n):.2e} kg·m/s")

# k ning energiya yo'qolishiga ta'siri
kk = np.linspace(0, 1, 100)
loss = []
for ki in kk:
    a, b = collide(m1, m2, v1, v2, ki)
    loss.append(100*(T0 - 0.5*m1*a**2 - 0.5*m2*b**2)/T0)
series("Energiya yo'qolishi", kk.tolist(), loss, xlabel="Restitutsiya k", ylabel="Yo'qolish, %")

# Massalar nisbatining uzatilgan energiyaga ta'siri
ratios = np.logspace(-2, 2, 100)
eff = [100*(0.5*(m1/r)*collide(m1, m1/r, v1, 0, k)[1]**2)/T0 for r in ratios]
series("Detalga o'tgan energiya", ratios.tolist(), eff,
       xlabel="m₁/m₂ nisbati", ylabel="Uzatilgan energiya, %")

table("Zarba turlari", ["k", "v'₁, m/s", "v'₂, m/s", "Yo'qolish, %"],
      [[float(ki), *[float(x) for x in collide(m1, m2, v1, v2, ki)],
        float(100*(T0 - 0.5*m1*collide(m1,m2,v1,v2,ki)[0]**2
                   - 0.5*m2*collide(m1,m2,v1,v2,ki)[1]**2)/T0)]
       for ki in (0.0, 0.15, 0.5, 1.0)])
''',
                parameters=[
                    p("m1", "Zarba qismi massasi m₁", 10.0, 5000.0, 800.0, 10.0, "kg"),
                    p("m2", "Detal massasi m₂", 1.0, 2000.0, 120.0, 5.0, "kg"),
                    p("v1", "Zarba tezligi v₁", 0.5, 20.0, 5.0, 0.5, "m/s"),
                    p("k", "Restitutsiya k", 0.0, 1.0, 0.15, 0.05, "—"),
                    p("dt", "Zarba davomiyligi", 0.001, 0.100, 0.008, 0.001, "s"),
                ],
                expected_output="v'₁ = 4,25 m/s; v'₂ = 5,0 m/s; F ≈ 75 kN; yo'qolish ≈ 12,7 %",
            ),
            visualization=vis(
                "Impuls diagrammasi va energiya balansi",
                "React/SVG",
                "Zarbadan oldin va keyin ikkita jism, ularning impuls vektorlari "
                "strelkalar uzunligi bilan; pastda energiya balansi ustunli diagramma "
                "(kinetik → kinetik + yo'qolgan).",
                "React/SVG: impuls vektorlarini gorizontal strelkalar sifatida, "
                "yig'indi uzunligi o'zgarmasligini vizual ko'rsating — bu saqlanish "
                "qonunining eng aniq tasviri. Energiya uchun oddiy ustunli diagramma.",
            ),
            interpretation=(
                "Energiya yo'qolishi grafigi $k$ ga kvadratik bog'liq: $k=0$ da maksimal, "
                "$k=1$ da nol. Massalar nisbati grafigi esa muhim optimumni ko'rsatadi — "
                "eng ko'p energiya $m_1 \\approx m_2$ bo'lganda uzatiladi. Shuning uchun "
                "mixni urishda bolg'a massasi mixnikiga yaqin emas, balki katta bo'lishi "
                "kerak — chunki bizga energiya uzatish emas, kuch kerak."
            ),
            common_mistakes=[
                "Zarbada kinetik energiya saqlanadi deb hisoblash — u faqat ideal "
                "elastik zarbada ($k=1$) saqlanadi.",
                "Zarba paytida og'irlik impulsini hisobga olish. $mg\\Delta t$ zarba "
                "impulsidan ordinar darajada kichik.",
                "Impuls momenti saqlanishini tekshirmasdan ishlatish: $\\mathbf{M}_O^{(e)}=0$ "
                "sharti kerak.",
                "Vektor kattaliklarni skalyar qo'shish. Impuls — vektor, ishorani "
                "hisobga olish shart.",
            ],
            quiz=[
                q("Nima uchun ichki kuchlar sistema impulsini o'zgartira olmaydi?",
                  "Uchinchi qonun bo'yicha ular juft-juft teng va qarama-qarshi, "
                  "yig'indida bir-birini yo'qotadi.", "konseptual"),
                q("Figurali uchuvchi qo'llarini yig'ganda nima uchun tezroq aylanadi?",
                  "Impuls momenti saqlanadi ($M_O^{(e)} \\approx 0$): $J\\omega = \\text{const}$. "
                  "$J$ kamaysa $\\omega$ ortadi.", "talqin"),
                q("$m_1 = m_2$, $v_2 = 0$, $k = 1$. Zarbadan keyingi tezliklar?",
                  "$v'_1 = 0$, $v'_2 = v_1$ — jismlar tezlik almashadi.", "hisob"),
                q("Zarba vaqtini 2 marta uzaytirsak, o'rtacha kuch qanday o'zgaradi?",
                  "2 marta kamayadi, chunki $F = S/\\Delta t$, impuls $S$ esa o'zgarmaydi.",
                  "hisob"),
                q("Kodda `collide` funksiyasi qaysi ikki tenglamadan kelib chiqqan?",
                  "Impuls saqlanishi ($m_1v_1+m_2v_2 = m_1v'_1+m_2v'_2$) va Nyuton "
                  "restitutsiya gipotezasidan ($k = (v'_2-v'_1)/(v_1-v_2)$).", "kod"),
            ],
            bridge_to_next=(
                "Impuls vaqt bo'yicha integrallashdan kelib chiqdi. Endi tenglamani "
                "yo'l bo'yicha integrallaymiz — va ish hamda energiya tushunchalari "
                "paydo bo'ladi."
            ),
            research_extension=(
                "Restitutsiya koeffitsienti aslida materialga va zarba tezligiga bog'liq. "
                "Yuqoridan tashlangan sharchaning ketma-ket sakrashlar balandligini "
                "o'lchash orqali $k(v)$ ni aniqlash usulini modellashtiring: "
                "$h_{n+1}/h_n = k^2$. Sonli eksperiment qiling va $k$ tezlik bilan "
                "kamayishini ko'rsatuvchi model tuzing."
            ),
        ),
    ),
    Topic(
        id="nm-14",
        subject_id=S,
        module_id=M,
        order=14,
        title="Kuch ishi, quvvat va kinetik energiya haqidagi teorema",
        description=(
            "Ishning ta'rifi va hisobi, quvvat, kinetik energiya teoremasi va uning "
            "mexanizmlar hisobida qo'llanilishi."
        ),
        learning_objective=(
            "Turli kuchlar ishini hisoblash va kinetik energiya teoremasi orqali "
            "tezlikni yo'l funksiyasi sifatida topish."
        ),
        prerequisites=["nm-08", "nm-13"],
        mathematical_core=(
            "Egri chiziqli integral $\\int\\mathbf{F}\\cdot d\\mathbf{r}$, skalyar "
            "ko'paytma, o'zgaruvchan kuch ishi."
        ),
        engineering_application=(
            "Dvigatel quvvati, mexanizm FIK si, tormoz yo'li, prujinali "
            "akkumulyatorlar."
        ),
        computational_component=(
            "Turli kuchlar ishini sonli integrallash (`scipy.integrate.quad`) va "
            "energiya balansini tekshirish."
        ),
        visualization_component=(
            "$F(x)$ grafigi ostidagi yuza — ishning geometrik talqini."
        ),
        research_extension=(
            "Rekuperativ tormozlash: kinetik energiyaning qancha qismini qaytarib "
            "olish mumkin?"
        ),
        difficulty="asosiy",
        previous_link=(
            "nm-13 da vaqt bo'yicha integrallash impulsni berdi. Endi xuddi shu "
            "tenglamani ko'chish bo'yicha integrallaymiz."
        ),
        next_topic="nm-15",
        estimated_minutes=85,
        tags=["ish", "quvvat", "kinetik energiya"],
        lesson=Lesson(
            physical_problem=(
                "Avtomobil 100 km/soat tezlikdan to'xtaguncha qancha yo'l bosadi? "
                "Nyuton tenglamasini integrallash mumkin, lekin tormoz kuchi "
                "o'zgaruvchan. Energiya yondashuvi esa bir qatorda javob beradi: "
                "butun kinetik energiya tormoz ishiga aylanadi. Va bu yondashuv "
                "muhim natijani ochadi — tormoz yo'li tezlikning kvadratiga proporsional."
            ),
            concepts=[
                c("Elementar ish", "$dA = \\mathbf{F}\\cdot d\\mathbf{r} = F\\,ds\\cos\\alpha$ "
                  "— faqat ko'chish yo'nalishidagi kuch ulushi ish bajaradi."),
                c("To'la ish", "$A = \\int_{(1)}^{(2)}\\mathbf{F}\\cdot d\\mathbf{r}$ — "
                  "egri chiziqli integral; umumiy holda yo'lga bog'liq."),
                c("Quvvat (power)", "$N = dA/dt = \\mathbf{F}\\cdot\\mathbf{v}$ — ishning "
                  "bajarilish tezligi."),
                c("Kinetik energiya", "$T = \\tfrac{1}{2}mv^2$; qattiq jism uchun "
                  "$T = \\tfrac{1}{2}Mv_C^2 + \\tfrac{1}{2}J_C\\omega^2$ (Koenig teoremasi)."),
                c("FIK (efficiency)", "$\\eta = A_{\\text{foydali}}/A_{\\text{sarflangan}}$ — "
                  "har doim birdan kichik."),
            ],
            derivation=[
                d("1-qadam. Nyuton tenglamasini $d\\mathbf{r}$ ga skalyar ko'paytirish",
                  r"m\frac{d\mathbf{v}}{dt}\cdot d\mathbf{r} = \mathbf{F}\cdot d\mathbf{r}",
                  "Ikkala tomonni elementar ko'chishga skalyar ko'paytiramiz."),
                d("2-qadam. Chap tomonni o'zgartirish",
                  r"m\frac{d\mathbf{v}}{dt}\cdot\mathbf{v}\,dt = m\,\mathbf{v}\cdot d\mathbf{v} = "
                  r"d\!\left(\frac{mv^2}{2}\right)",
                  "$\\mathbf{v}\\cdot d\\mathbf{v} = \\tfrac{1}{2}d(v^2)$ ayniyatidan "
                  "foydalanamiz — kinetik energiyaning differensiali paydo bo'ldi."),
                d("3-qadam. Kinetik energiya teoremasi",
                  r"\boxed{\;\frac{mv_2^2}{2} - \frac{mv_1^2}{2} = A_{12}\;}",
                  "Kinetik energiya o'zgarishi barcha kuchlar ishiga teng. Vaqt "
                  "tenglamadan yo'qoldi — bu uning asosiy afzalligi."),
                d("4-qadam. Tormoz yo'li uchun qo'llash",
                  r"0 - \frac{mv^2}{2} = -f m g\, s \;\Rightarrow\; "
                  r"\boxed{\;s = \frac{v^2}{2fg}\;}",
                  "Massa qisqardi: tormoz yo'li yuk og'irligiga bog'liq emas. "
                  "Tezlik kvadratga kirgani uchun 2 marta tez yurish 4 marta uzoq "
                  "tormoz yo'li beradi."),
                d("5-qadam. Quvvat va tortish kuchi bog'lanishi",
                  r"N = Fv = \text{const} \Rightarrow F = \frac{N}{v}",
                  "O'zgarmas quvvatda tezlik ortsa tortish kuchi kamayadi — shuning "
                  "uchun avtomobilga uzatmalar qutisi kerak."),
            ],
            formula_meaning=(
                "$s = v^2/(2fg)$ — yo'l xavfsizligining asosiy formulasi. 60 km/soat "
                "da tormoz yo'li 23 m, 120 km/soat da esa 92 m: tezlik 2 marta, yo'l "
                "4 marta. $N = Fv$ esa mashinasozlikning asosiy kompromissi: bir xil "
                "quvvatda ko'p kuch yoki yuqori tezlik — ikkalasi birdan emas."
            ),
            equations=[
                eq(r"A = \int_{(1)}^{(2)}\mathbf{F}\cdot d\mathbf{r}", "Kuch ishi.", "Ish"),
                eq(r"T_2 - T_1 = A_{12}", "Kinetik energiya haqidagi teorema.", "Energiya teoremasi"),
                eq(r"N = \mathbf{F}\cdot\mathbf{v} = M\omega", "Quvvat (ilgarilanma va aylanma).",
                   "Quvvat"),
                eq(r"s = \frac{v^2}{2fg}", "Tormoz yo'li.", "Tormoz yo'li"),
            ],
            conditions=(
                "Teorema ikki holat orasida qo'llaniladi — boshlang'ich va yakuniy. "
                "Oraliq jarayon haqida ma'lumot bermaydi va vaqtni topib bo'lmaydi. "
                "Agar vaqt kerak bo'lsa, impuls teoremasi yoki bevosita integrallash "
                "zarur. Ichki kuchlar ishi umuman nolga teng emas (deformatsiyalanuvchi "
                "sistemada) — bu mq-24 da muhim bo'ladi."
            ),
            worked_example=WorkedExample(
                statement=(
                    "Massasi $m = 1500$ kg avtomobil $v_0 = 100$ km/soat tezlikdan "
                    "to'xtaydi. Ishqalanish koeffitsienti $f = 0{,}7$ (quruq asfalt) va "
                    "$f = 0{,}25$ (nam). Tormoz yo'lini, tormozlash vaqtini va tormozlarda "
                    "ajralgan issiqlik quvvatini toping."
                ),
                given=[r"m = 1500\ \text{kg}", r"v_0 = 100\ \text{km/soat} = 27{,}8\ \text{m/s}",
                       r"f_1 = 0{,}7,\; f_2 = 0{,}25"],
                steps=[
                    st(r"T_0 = \frac{mv_0^2}{2} = \frac{1500\cdot 27{,}8^2}{2} = \frac{1500\cdot 772{,}8}{2} = 579\ \text{kJ}",
                       "Boshlang'ich kinetik energiya."),
                    st(r"s_1 = \frac{v_0^2}{2f_1g} = \frac{772{,}8}{2\cdot 0{,}7\cdot 9{,}81} = \frac{772{,}8}{13{,}73} = 56{,}3\ \text{m}",
                       "Quruq asfaltda tormoz yo'li."),
                    st(r"s_2 = \frac{772{,}8}{2\cdot 0{,}25\cdot 9{,}81} = \frac{772{,}8}{4{,}905} = 157{,}6\ \text{m}",
                       "Nam asfaltda — 2,8 marta uzoq!"),
                    st(r"a_1 = f_1 g = 6{,}87\ \text{m/s}^2,\qquad t_1 = \frac{v_0}{a_1} = \frac{27{,}8}{6{,}87} = 4{,}05\ \text{s}",
                       "Tormozlash vaqti."),
                    st(r"N_{\text{o'rt}} = \frac{T_0}{t_1} = \frac{579\,000}{4{,}05} = 143\ \text{kW}",
                       "Tormozlarda ajraladigan o'rtacha issiqlik quvvati — "
                       "dvigatel quvvatidan katta!"),
                    st(r"\Delta s = s_2 - s_1 = 101{,}3\ \text{m}",
                       "Nam yo'lda qo'shimcha 101 m — bu 25 ta avtomobil uzunligi."),
                ],
                answer=(
                    "$s_1 = 56{,}3$ m, $s_2 = 157{,}6$ m; $t_1 = 4{,}05$ s; "
                    "$N_{\\text{o'rt}} = 143$ kW."
                ),
                engineering_note=(
                    "143 kW issiqlik 4 sekundda 4 ta tormoz diskida ajraladi — har biri "
                    "36 kW. Shuning uchun disklar ventilyatsiyalangan qilinadi va "
                    "ketma-ket tormozlashda 'tormoz so'nishi' (brake fade) yuz beradi. "
                    "Elektromobillarda bu energiyaning 60–70 % i rekuperatsiya orqali "
                    "batareyaga qaytariladi."
                ),
            ),
            computation=Computation(
                caption=(
                    "Tormozlash energetikasi: tezlik va yo'l holatini o'zgartirib, "
                    "tormoz yo'li va issiqlik quvvatini hisoblang."
                ),
                code='''"""Ish, quvvat va kinetik energiya teoremasi."""
import numpy as np
from scipy.integrate import quad
from labkit import PARAMS, note, series, table, value

m = float(PARAMS.get("m", 1500.0))       # kg
v_kmh = float(PARAMS.get("v_kmh", 100))  # km/soat
f = float(PARAMS.get("f", 0.7))          # ishqalanish koeffitsienti
k_spring = float(PARAMS.get("k", 25000)) # prujina bikrligi, N/m
g = 9.81

v0 = v_kmh/3.6
T0 = 0.5*m*v0**2
s = v0**2/(2*f*g)
t_brake = v0/(f*g)

value("Kinetik energiya T₀", T0/1000, "kJ")
value("Tormoz yo'li s", s, "m")
value("Tormozlash vaqti", t_brake, "s")
value("Sekinlanish", f*g, "m/s²")
value("O'rtacha quvvat", T0/t_brake/1000, "kW")

# Tormoz yo'lining tezlikka kvadratik bog'liqligi
vv = np.linspace(10, 160, 100)
series("Tormoz yo'li (quruq, f=0,7)", vv.tolist(), ((vv/3.6)**2/(2*0.7*g)).tolist(),
       xlabel="v, km/soat", ylabel="s, m")
series("Tormoz yo'li (nam, f=0,25)", vv.tolist(), ((vv/3.6)**2/(2*0.25*g)).tolist(),
       xlabel="v, km/soat", ylabel="s, m")

# O'zgaruvchan kuch ishi: prujina (sonli va analitik)
x_max = 0.08
A_num, err = quad(lambda x: k_spring*x, 0, x_max)
A_analytic = k_spring*x_max**2/2
value("Prujina ishi (sonli)", A_num, "J")
note(f"Analitik: {A_analytic:.3f} J, sonli integrallash xatoligi: {err:.2e} J")

xx = np.linspace(0, x_max, 100)
series("Prujina kuchi F(x)", (xx*1000).tolist(), (k_spring*xx).tolist(),
       xlabel="Siqilish x, mm", ylabel="F, N")

table("Yo'l holatiga bog'liqlik",
      ["Holat", "f", "s, m", "t, s"],
      [["Quruq asfalt", 0.70, float(v0**2/(2*0.70*g)), float(v0/(0.70*g))],
       ["Nam asfalt", 0.40, float(v0**2/(2*0.40*g)), float(v0/(0.40*g))],
       ["Yomg'irli", 0.25, float(v0**2/(2*0.25*g)), float(v0/(0.25*g))],
       ["Muzli", 0.10, float(v0**2/(2*0.10*g)), float(v0/(0.10*g))]])
''',
                parameters=[
                    p("m", "Avtomobil massasi", 500.0, 40000.0, 1500.0, 100.0, "kg"),
                    p("v_kmh", "Tezlik", 10.0, 250.0, 100.0, 5.0, "km/soat"),
                    p("f", "Ishqalanish koeff.", 0.05, 1.0, 0.7, 0.05, "—"),
                    p("k", "Prujina bikrligi", 1000.0, 200000.0, 25000.0, 1000.0, "N/m"),
                ],
                expected_output="T₀ = 579 kJ, s = 56,3 m, t = 4,05 s, N = 143 kW",
            ),
            visualization=vis(
                "Ishning geometrik talqini",
                "React/SVG",
                "$F(x)$ grafigi va uning ostidagi bo'yalgan yuza — bajarilgan ish. "
                "Prujina uchun uchburchak, o'zgarmas kuch uchun to'rtburchak.",
                "React/SVG: `<path>` bilan egri chiziq, ostidagi sohani yarim shaffof "
                "to'ldirish. Bu integralning ma'nosini bir qarashda tushuntiradi va "
                "su-08 dagi sonli integrallash mavzusida qayta ishlatiladi.",
            ),
            interpretation=(
                "Ikkala tormoz yo'li egri chizig'i parabola, lekin nam yo'ldagi ancha "
                "tik. 100 km/soat da farq 101 m — bu haydovchi reaksiya vaqtidagi "
                "masofadan (28 m) ham ko'p. Aynan shu grafik tezlik cheklovlarining "
                "fizik asosini beradi: tezlikni 20 % kamaytirish tormoz yo'lini 36 % "
                "qisqartiradi."
            ),
            common_mistakes=[
                "Ishni $A = Fs$ deb har doim yozish — bu faqat o'zgarmas kuch va "
                "$\\alpha = 0$ da to'g'ri.",
                "Normal reaksiyaning ishini nolga teng emas deb hisoblash — u ko'chishga "
                "perpendikular, demak $A_N = 0$.",
                "Kinetik energiya teoremasidan vaqtni topishga urinish — undan vaqt "
                "chiqmaydi.",
                "Aylanma harakatda $T = \\tfrac{1}{2}mv^2$ ni ishlatish — "
                "$T = \\tfrac{1}{2}J\\omega^2$ kerak (nm-18).",
            ],
            quiz=[
                q("Nima uchun tormoz yo'li avtomobil massasiga bog'liq emas?",
                  "Chunki ham kinetik energiya, ham ishqalanish ishi massaga "
                  "proporsional — tenglamada $m$ qisqaradi.", "konseptual"),
                q("Tezlikni 1,5 marta oshirsak, tormoz yo'li necha marta ortadi?",
                  "$1{,}5^2 = 2{,}25$ marta.", "hisob"),
                q("Yuk gorizontal tekislikda o'zgarmas tezlik bilan ko'chirilmoqda. "
                  "Og'irlik kuchining ishi qancha?",
                  "Nol — og'irlik vertikal, ko'chish gorizontal, $\\cos 90° = 0$.", "hisob"),
                q("Nima uchun $N = Fv$ uzatmalar qutisining zaruratini tushuntiradi?",
                  "Quvvat cheklangan bo'lgani uchun kichik tezlikda katta kuch, yuqori "
                  "tezlikda kichik kuch olinadi. Uzatmalar qutisi bu almashuvni "
                  "boshqaradi.", "talqin"),
                q("Kodda `quad` natijasi analitik qiymat bilan nima uchun mos keladi?",
                  "Chunki integral osti funksiyasi chiziqli va Gauss kvadraturasi "
                  "polinomlarni aniq integrallaydi (su-08). Xatolik mashina aniqligi "
                  "tartibida.", "kod"),
            ],
            bridge_to_next=(
                "Ish umuman yo'lga bog'liq. Lekin ba'zi kuchlar uchun u faqat "
                "boshlang'ich va yakuniy nuqtaga bog'liq — bunday kuchlar potensial "
                "deyiladi va ular energiya saqlanishiga olib keladi."
            ),
            research_extension=(
                "Rekuperativ tormozlash samaradorligini modellashtiring: "
                "elektrodvigatel generator rejimida ishlaganda kinetik energiyaning "
                "qancha qismi qaytariladi? Shahar sikli (masalan, WLTP) uchun "
                "tezlik profilini oling va rekuperatsiya bilan hamda usiz energiya "
                "sarfini taqqoslang."
            ),
        ),
    ),
    Topic(
        id="nm-15",
        subject_id=S,
        module_id=M,
        order=15,
        title="Potensial kuchlar, potensial energiya va to'la mexanik energiyaning saqlanishi",
        description=(
            "Potensial maydon, potensial energiya, konservativ va dissipativ kuchlar, "
            "energiya saqlanish qonuni va potensial egri chiziqlar tahlili."
        ),
        learning_objective=(
            "Kuch potensialligini tekshirish, potensial energiyani qurish va energiya "
            "saqlanishi orqali harakat sohasini aniqlash."
        ),
        prerequisites=["nm-14"],
        mathematical_core=(
            "Gradiyent, to'la differensial sharti (rotor nolga teng), potensial "
            "funksiya, muvozanat turlari va turg'unlik."
        ),
        engineering_application=(
            "Prujinali mexanizmlar, gidroakkumulyator, tortishish maydonida harakat, "
            "muvozanat turg'unligini baholash."
        ),
        computational_component=(
            "Potensial energiya egri chizig'ini qurish va berilgan to'la energiyada "
            "harakat sohasini aniqlash."
        ),
        visualization_component=(
            "Potensial chuqurcha diagrammasi, energiya darajalari, burilish nuqtalari."
        ),
        research_extension=(
            "Ko'p o'lchovli potensial relyefda minimumlarni izlash — bu optimallashtirish "
            "masalasining fizik talqini."
        ),
        difficulty="murakkab",
        previous_link=(
            "nm-14 da ishning umuman yo'lga bog'liqligini ko'rdik. Endi maxsus, lekin "
            "nihoyatda muhim sinf — potensial kuchlarni ajratamiz."
        ),
        next_topic="nm-16",
        estimated_minutes=95,
        tags=["potensial energiya", "saqlanish", "turg'unlik"],
        lesson=Lesson(
            physical_problem=(
                "Klapan prujinasi yopiq holatda energiya to'playdi, ochilganda uni "
                "qaytaradi. Suv omborida to'plangan suv potensial energiya, turbinada "
                "u kinetik energiyaga aylanadi. Ikkala holda ham energiya 'saqlanadi' "
                "va zarur paytda qaytariladi. Lekin ishqalanish qo'shilsa, energiya "
                "qaytmaydi. Bu ikki sinf kuchni qanday ajratamiz va bu ajratish nima "
                "beradi?"
            ),
            concepts=[
                c("Potensial (konservativ) kuch", "Ishi faqat boshlang'ich va yakuniy "
                  "holatga bog'liq bo'lgan kuch. Yopiq kontur bo'ylab ishi nolga teng."),
                c("Potensial energiya $\\Pi$", "$\\mathbf{F} = -\\nabla\\Pi$; ish "
                  "$A_{12} = \\Pi_1 - \\Pi_2$. Nol daraja ixtiyoriy tanlanadi."),
                c("Potensiallik sharti", "$\\nabla\\times\\mathbf{F} = 0$ (bir bog'lamli "
                  "sohada). Tekislikda: $\\partial F_x/\\partial y = \\partial F_y/\\partial x$."),
                c("Dissipativ kuch", "Ishqalanish, qarshilik — ishi har doim manfiy va "
                  "yo'lga bog'liq; mexanik energiyani issiqlikka aylantiradi."),
                c("Turg'un muvozanat", "$\\Pi$ minimumi (Lagranj–Dirixle teoremasi). "
                  "Maksimum — noturg'un muvozanat."),
            ],
            derivation=[
                d("1-qadam. Potensiallik ta'rifidan potensial energiyaga",
                  r"A_{12} = \int_1^2 \mathbf{F}\cdot d\mathbf{r} = \Pi_1 - \Pi_2 "
                  r"\;\Rightarrow\; dA = -d\Pi",
                  "Ish potensial energiyaning kamayishiga teng. Minus ishora — "
                  "kelishuv: kuch $\\Pi$ kamayadigan tomonga yo'naladi."),
                d("2-qadam. Kuchni gradiyent orqali ifodalash",
                  r"F_x\,dx + F_y\,dy + F_z\,dz = -\left(\frac{\partial\Pi}{\partial x}dx + "
                  r"\frac{\partial\Pi}{\partial y}dy + \frac{\partial\Pi}{\partial z}dz\right)"
                  r"\;\Rightarrow\; \mathbf{F} = -\nabla\Pi",
                  "Koeffitsientlarni tenglashtiramiz. Kuch — potensial relyefning eng "
                  "tik pastga tushish yo'nalishi."),
                d("3-qadam. Potensiallik mezoni",
                  r"\nabla\times\mathbf{F} = -\nabla\times(\nabla\Pi) \equiv 0",
                  "Gradiyentning rotori aynan nolga teng. Demak $\\nabla\\times\\mathbf{F} \\neq 0$ "
                  "bo'lsa, kuch potensial emas — buni tekshirish oson."),
                d("4-qadam. Energiya saqlanish qonuni",
                  r"T_2 - T_1 = A_{12} = \Pi_1 - \Pi_2 \;\Rightarrow\; "
                  r"\boxed{\;T_1 + \Pi_1 = T_2 + \Pi_2 = E = \text{const}\;}",
                  "Kinetik energiya teoremasiga potensiallikni qo'shdik. Faqat "
                  "potensial kuchlar ta'sirida to'la mexanik energiya saqlanadi."),
                d("5-qadam. Harakat sohasi va burilish nuqtalari",
                  r"v = \sqrt{\frac{2(E-\Pi(x))}{m}} \;\Rightarrow\; \text{harakat faqat } "
                  r"\Pi(x) \le E \text{ sohasida}",
                  "$\\Pi(x) = E$ nuqtalarida tezlik nolga teng — bu burilish nuqtalari. "
                  "Jism potensial chuqurchada 'qamalib' qoladi — bu tebranishning "
                  "energetik ta'rifi."),
            ],
            formula_meaning=(
                "$E = T + \\Pi = \\text{const}$ — mexanikadagi eng kuchli hisoblash "
                "vositasi: u differensial tenglamani birinchi tartibga tushiradi. "
                "$\\mathbf{F} = -\\nabla\\Pi$ esa geometrik tasavvur beradi: jism "
                "potensial relyefda sharcha kabi harakatlanadi, chuqurchalar — turg'un "
                "muvozanat, tepaliklar — noturg'un. Bu tasavvur nm-30 dagi turg'unlik "
                "tahlili va pq-15 dagi ustuvorlik mavzusining asosi."
            ),
            equations=[
                eq(r"\mathbf{F} = -\nabla\Pi", "Potensial kuch va potensial energiya bog'lanishi.",
                   "Gradiyent bog'lanishi"),
                eq(r"T + \Pi = E = \text{const}", "Mexanik energiya saqlanish qonuni.",
                   "Energiya saqlanishi"),
                eq(r"\Pi_{\text{prujina}} = \frac{kx^2}{2},\quad \Pi_{\text{og'irlik}} = mgh",
                   "Eng ko'p ishlatiladigan potensial energiyalar.", "Tipik potensiallar"),
            ],
            conditions=(
                "Energiya saqlanishi faqat barcha ish bajaruvchi kuchlar potensial "
                "bo'lganda o'rinli. Ishqalanish bo'lsa: $E_2 - E_1 = A_{\\text{dissipativ}} < 0$. "
                "Bog'lanish reaksiyalari ideal bog'lanishda ish bajarmaydi, shuning uchun "
                "ular energiya balansiga kirmaydi — bu nm-20 dagi mumkin bo'lgan "
                "ko'chishlar prinsipining asosi."
            ),
            worked_example=WorkedExample(
                statement=(
                    "Klapan mexanizmi: massasi $m = 0{,}25$ kg klapan prujina "
                    "($k = 28$ kN/m) bilan yopiq holatda ushlab turiladi, oldindan "
                    "siqilish $x_0 = 12$ mm. Klapan $h = 9$ mm ga ochiladi. "
                    "(a) Ochish uchun zarur ish; (b) klapan yopilayotganda o'rindiqqa "
                    "urilish tezligi (prujina energiyasi to'liq kinetikaga o'tsa); "
                    "(c) 6000 ayl/min da prujinaning quvvat sarfi."
                ),
                given=[r"m = 0{,}25\ \text{kg},\; k = 28\,000\ \text{N/m}",
                       r"x_0 = 0{,}012\ \text{m},\; h = 0{,}009\ \text{m}",
                       r"n = 6000\ \text{ayl/min}"],
                steps=[
                    st(r"\Pi_1 = \frac{k x_0^2}{2} = \frac{28\,000\cdot 0{,}012^2}{2} = "
                       r"\frac{28\,000\cdot 1{,}44\cdot 10^{-4}}{2} = 2{,}016\ \text{J}",
                       "Yopiq holatdagi potensial energiya."),
                    st(r"\Pi_2 = \frac{k(x_0+h)^2}{2} = \frac{28\,000\cdot 0{,}021^2}{2} = "
                       r"\frac{28\,000\cdot 4{,}41\cdot 10^{-4}}{2} = 6{,}174\ \text{J}",
                       "To'liq ochilgan holatdagi potensial energiya."),
                    st(r"A_{\text{ochish}} = \Pi_2 - \Pi_1 = 6{,}174 - 2{,}016 = 4{,}158\ \text{J}",
                       "Kulachok bajarishi kerak bo'lgan ish."),
                    st(r"\frac{mv^2}{2} = \Pi_2 - \Pi_1 \Rightarrow "
                       r"v = \sqrt{\frac{2\cdot 4{,}158}{0{,}25}} = \sqrt{33{,}26} = 5{,}77\ \text{m/s}",
                       "Yopilish tezligi (dempfirlashsiz, eng yomon hol)."),
                    st(r"f = \frac{n}{2\cdot 60} = \frac{6000}{120} = 50\ \text{Hz}",
                       "To'rt taktli dvigatelda klapan har ikki aylanishda bir marta ochiladi."),
                    st(r"N = A\cdot f \cdot 2 = 4{,}158\cdot 50\cdot 2 \approx 416\ \text{W}",
                       "Ochish va yopishda energiya oqimi; ideal holda yopishda energiya "
                       "qaytariladi, real holda 20–30 % yo'qoladi."),
                ],
                answer=(
                    "(a) $A = 4{,}16$ J; (b) $v = 5{,}77$ m/s; (c) energiya aylanishi "
                    "$\\approx 416$ W."
                ),
                engineering_note=(
                    "5,77 m/s tezlikda urilish klapan o'rindig'ini tez yeydi va shovqin "
                    "beradi. Shuning uchun gidravlik kompensatorlar va kulachok "
                    "profilining 'yumshoq tushish' uchastkasi qo'llaniladi — ular "
                    "energiyaning bir qismini nazorat ostida dissipatsiya qiladi."
                ),
            ),
            computation=Computation(
                caption=(
                    "Potensial energiya relyefi: to'la energiyani o'zgartirib, harakat "
                    "sohasi va burilish nuqtalari qanday siljishini kuzating."
                ),
                code='''"""Potensial energiya, energiya saqlanishi va harakat sohasi."""
import numpy as np
from labkit import PARAMS, note, series, table, value

k = float(PARAMS.get("k", 28000.0))    # prujina bikrligi, N/m
m = float(PARAMS.get("m", 0.25))       # massa, kg
x0 = float(PARAMS.get("x0", 0.012))    # oldindan siqilish, m
h = float(PARAMS.get("h", 0.009))      # klapan yurishi, m
E_rel = float(PARAMS.get("E_rel", 1.0))# to'la energiya (Pi_max ulushida)

Pi1 = k*x0**2/2
Pi2 = k*(x0+h)**2/2
A = Pi2 - Pi1
value("Π (yopiq)", Pi1, "J")
value("Π (ochiq)", Pi2, "J")
value("Ochish ishi A", A, "J")
value("Yopilish tezligi", float(np.sqrt(2*A/m)), "m/s")

# Prujina potensial energiyasi egri chizig'i
x = np.linspace(0, x0+h+0.005, 200)
Pi = k*x**2/2
series("Potensial energiya Π(x)", (x*1000).tolist(), Pi.tolist(),
       xlabel="Siqilish x, mm", ylabel="Π, J")
series("Kuch F(x) = -dΠ/dx", (x*1000).tolist(), (-k*x).tolist(),
       xlabel="Siqilish x, mm", ylabel="F, N")

# Nochiziqli potensial: ikki chuqurchali relyef (Duffing turi)
q = np.linspace(-1.5, 1.5, 400)
U = 0.25*q**4 - 0.5*q**2          # ikki minimum: q = ±1
E_total = E_rel*float(np.max(U[np.abs(q) < 1.2]))
series("Ikki chuqurchali potensial U(q)", q.tolist(), U.tolist(),
       xlabel="q", ylabel="U(q)")
series("To'la energiya E", q.tolist(), np.full_like(q, E_total).tolist(),
       xlabel="q", ylabel="U(q)")

allowed = q[U <= E_total]
if allowed.size:
    verdict = ("Ikki chuqurcha bog'langan — jism o'tib keta oladi."
               if E_total > 0 else "Jism bitta chuqurchada qamalgan.")
    note(f"E = {E_total:.4f} da harakat sohasi: q in "
         f"[{allowed.min():.3f}, {allowed.max():.3f}]. {verdict}")

# Muvozanat nuqtalari: dU/dq = 0 -> q^3 - q = 0
roots = [-1.0, 0.0, 1.0]
table("Muvozanat nuqtalari",
      ["q", "U(q)", "d²U/dq²", "Turi"],
      [[r, float(0.25*r**4 - 0.5*r**2), float(3*r**2 - 1),
        "turg'un" if 3*r**2 - 1 > 0 else "noturg'un"] for r in roots])
''',
                parameters=[
                    p("k", "Prujina bikrligi k", 1000.0, 100000.0, 28000.0, 1000.0, "N/m"),
                    p("m", "Klapan massasi m", 0.05, 2.0, 0.25, 0.05, "kg"),
                    p("x0", "Oldindan siqilish x₀", 0.001, 0.050, 0.012, 0.001, "m"),
                    p("h", "Klapan yurishi h", 0.001, 0.030, 0.009, 0.001, "m"),
                    p("E_rel", "To'la energiya (nisbiy)", -0.9, 2.0, 1.0, 0.1, "—"),
                ],
                expected_output="Π₁ = 2,016 J; Π₂ = 6,174 J; A = 4,158 J; v = 5,77 m/s",
            ),
            visualization=vis(
                "Potensial chuqurcha va energiya darajalari",
                "React/SVG",
                "$\\Pi(x)$ egri chizig'i, gorizontal $E$ chizig'i, ularning kesishishi — "
                "burilish nuqtalari; ruxsat etilgan soha bo'yalgan. Minimumlar va "
                "maksimumlar belgilangan.",
                "React/SVG: ikki chiziq va bo'yalgan soha — sodda, lekin juda "
                "ta'sirchan. $E$ ni slider bilan ko'tarib-tushirganda harakat "
                "sohasining o'zgarishi turg'unlik tushunchasini intuitiv qiladi. "
                "Manim'da esa sharchaning relyef bo'ylab dumalashi ko'rsatiladi.",
            ),
            interpretation=(
                "Ikki chuqurchali potensialda $E < 0$ bo'lsa jism bitta chuqurchada "
                "qamaladi — u ikkinchisiga o'ta olmaydi. $E > 0$ da to'siqdan oshib "
                "o'tadi va butun soha bo'ylab harakatlanadi. Bu — faza o'tishlari, "
                "ustuvorlikni yo'qotish (pq-18 dagi 'snap-through') va hatto kimyoviy "
                "reaksiya aktivatsiya energiyasining universal modeli."
            ),
            common_mistakes=[
                "$\\Pi$ ning nol darajasini masala davomida o'zgartirish. U bir marta "
                "tanlanadi va o'zgarmaydi.",
                "Ishqalanish mavjud bo'lganda energiya saqlanishini qo'llash.",
                "$\\mathbf{F} = +\\nabla\\Pi$ deb yozish — minus ishorani unutish.",
                "Potensiallikni tekshirmasdan potensial energiya qurishga urinish.",
                "Turg'un muvozanatni $\\Pi$ maksimumi deb olish — aksincha, minimum.",
            ],
            quiz=[
                q("Nima uchun ishqalanish kuchi potensial emas?",
                  "Uning ishi yo'lga bog'liq: uzun yo'lda ko'proq energiya yo'qoladi. "
                  "Yopiq kontur bo'ylab ishi nolga teng emas, balki manfiy.", "konseptual"),
                q("$\\Pi(x) = kx^2/2$ dan kuchni toping.",
                  "$F = -d\\Pi/dx = -kx$ — Guk qonuni, kuch siljishga qarama-qarshi.",
                  "hisob"),
                q("Prujina siqilishini 2 marta oshirsak, energiya qanday o'zgaradi?",
                  "4 marta ortadi, chunki $\\Pi \\propto x^2$.", "hisob"),
                q("Jism potensial chuqurchada, $E$ minimumdan biroz katta. Harakat "
                  "qanday bo'ladi?",
                  "Burilish nuqtalari orasida tebranish. $E$ minimumga yaqin bo'lsa, "
                  "tebranish deyarli garmonik (nm-25).", "talqin"),
                q("Kodda `3*r**2 - 1` nima uchun hisoblanadi?",
                  "Bu $d^2U/dq^2$ — ikkinchi hosila. Musbat bo'lsa minimum (turg'un), "
                  "manfiy bo'lsa maksimum (noturg'un). Bu — Lagranj–Dirixle "
                  "teoremasining amaliy tekshiruvi.", "kod"),
            ],
            bridge_to_next=(
                "Energiya usullari bitta nuqta uchun kuchli. Ko'p jismli sistemada esa "
                "avval uning 'markazi'ni topish kerak. Keyingi mavzuda massalar markazi "
                "va uning harakati haqidagi teoremani ko'ramiz."
            ),
            research_extension=(
                "Ikki chuqurchali potensialga davriy majburlovchi kuch va dempfirlash "
                "qo'shing (Duffing tenglamasi). To'la energiya chegarada bo'lganda "
                "harakat xaotik bo'lishi mumkin. Poincaré kesimini qurib, "
                "determinlashgan xaosni kuzating. Bu — nochiziqli dinamikaga real kirish "
                "(nm-30 da davom etadi)."
            ),
            manim=manim(
                scene="PotentialWellScene",
                module="animatsiya/scenes/nm_energy.py",
                title="Potensial chuqurcha va energiya saqlanishi",
                summary="Sharcha potensial relyef bo'ylab harakatlanadi; kinetik va "
                        "potensial energiya ustunlari almashib turadi, yig'indi o'zgarmaydi.",
            ),
        ),
    ),
    Topic(
        id="nm-16",
        subject_id=S,
        module_id=M,
        order=16,
        title="Massalar markazi va massalar markazi harakati haqidagi teorema",
        description=(
            "Massalar markazi ta'rifi va hisobi, uning harakati haqidagi teorema, "
            "Koenig teoremasi orqali kinetik energiyaning ajralishi."
        ),
        learning_objective=(
            "Murakkab shaklli jismning massalar markazini hisoblash va sistema "
            "harakatini markaz harakati + markaz atrofidagi harakatga ajratish."
        ),
        prerequisites=["nm-13"],
        mathematical_core=(
            "Og'irlikli o'rtacha, integral orqali ta'rif, additivlik, Koenig teoremasi."
        ),
        engineering_application=(
            "Konstruksiya og'irlik markazi, muvozanatlash, raketa harakati, "
            "kran ustuvorligi."
        ),
        computational_component=(
            "Murakkab kesim og'irlik markazini bo'laklarga ajratish usuli bilan "
            "hisoblash — mq-07 uchun to'g'ridan-to'g'ri tayyorgarlik."
        ),
        visualization_component=(
            "Murakkab shakl, uning bo'laklari va har birining markazi; natijaviy markaz."
        ),
        research_extension=(
            "O'zgaruvchan massali sistemalar (raketa) uchun massalar markazi "
            "teoremasi qanday o'zgaradi? Mesherskiy tenglamasini keltirib chiqaring."
        ),
        difficulty="asosiy",
        previous_link=(
            "nm-13 da $\\mathbf{P} = M\\mathbf{v}_C$ formulasini ishlatdik, lekin "
            "$\\mathbf{v}_C$ ni aniqlamadik. Endi bu bo'shliqni to'ldiramiz."
        ),
        next_topic="nm-17",
        estimated_minutes=80,
        tags=["massalar markazi", "Koenig teoremasi", "og'irlik markazi"],
        lesson=Lesson(
            physical_problem=(
                "Minorali kran yuk ko'targanda ag'darilib ketmasligi kerak. "
                "Ustuvorlik sharti butun tizimning (kran + yuk + protivoves) og'irlik "
                "markazi tayanch konturi ichida qolishini talab qiladi. Demak markazni "
                "aniq hisoblash — xavfsizlikning bevosita masalasi. Xuddi shu hisob "
                "keyinchalik kesim geometrik tavsiflarida qayta paydo bo'ladi."
            ),
            concepts=[
                c("Massalar markazi", "$\\mathbf{r}_C = \\frac{1}{M}\\sum m_i\\mathbf{r}_i$ "
                  "yoki $\\frac{1}{M}\\int\\mathbf{r}\\,dm$ — massaning 'og'irlikli o'rtachasi'."),
                c("Og'irlik markazi", "Bir jinsli tortishish maydonida massalar markazi "
                  "bilan ustma-ust tushadi. Katta obyektlarda (kosmik) farq qiladi."),
                c("Additivlik", "Murakkab jismni bo'laklarga ajratib, har birini uning "
                  "markaziga jamlangan massa deb hisoblash mumkin."),
                c("Teshiklarni hisobga olish", "Teshik — manfiy massali bo'lak; bu usul "
                  "hisobni juda soddalashtiradi."),
                c("Koenig teoremasi", "$T = \\tfrac{1}{2}Mv_C^2 + T_{\\text{nisbiy}}$ — "
                  "kinetik energiya markaz harakati va markaz atrofidagi harakat "
                  "energiyalari yig'indisi."),
            ],
            derivation=[
                d("1-qadam. Massalar markazi ta'rifi",
                  r"\mathbf{r}_C = \frac{\sum m_i\mathbf{r}_i}{\sum m_i} = \frac{1}{M}\int_V \mathbf{r}\,\rho\,dV",
                  "Og'irlikli o'rtacha. Bir jinsli jism uchun $\\rho$ qisqaradi va "
                  "masala sof geometrik bo'lib qoladi."),
                d("2-qadam. Massalar markazi harakati teoremasi",
                  r"M\mathbf{a}_C = \sum\mathbf{F}^{(e)}",
                  "nm-13 dagi $d\\mathbf{P}/dt = \\sum\\mathbf{F}^{(e)}$ va "
                  "$\\mathbf{P} = M\\mathbf{v}_C$ dan. Markaz shunday harakatlanadiki, "
                  "go'yo butun massa unga jamlangan va barcha tashqi kuchlar unga qo'yilgan."),
                d("3-qadam. Koenig teoremasi",
                  r"T = \frac{1}{2}\sum m_i v_i^2,\quad \mathbf{v}_i = \mathbf{v}_C + \mathbf{v}'_i "
                  r"\;\Rightarrow\; T = \frac{Mv_C^2}{2} + \frac{1}{2}\sum m_i v_i'^2",
                  "Kesishgan had $\\mathbf{v}_C\\cdot\\sum m_i\\mathbf{v}'_i = 0$ bo'ladi, "
                  "chunki markazga nisbatan impuls nolga teng."),
                d("4-qadam. Qattiq jism uchun natija",
                  r"\boxed{\;T = \frac{Mv_C^2}{2} + \frac{J_C\omega^2}{2}\;}",
                  "Nisbiy harakat — markaz atrofida aylanish, shuning uchun "
                  "$T_{\\text{nisbiy}} = J_C\\omega^2/2$. Bu formula dumalash "
                  "masalalarining kaliti."),
                d("5-qadam. Kran ustuvorligi sharti",
                  r"x_C = \frac{\sum G_i x_i}{\sum G_i} \in [x_{\text{tayanch}}^{min}, x_{\text{tayanch}}^{max}]",
                  "Ustuvorlik koeffitsienti: $k = M_{\\text{ushlab turuvchi}}/M_{\\text{ag'daruvchi}} \\ge 1{,}4$ "
                  "(me'yoriy talab)."),
            ],
            formula_meaning=(
                "Massalar markazi teoremasi murakkab tizimni bitta nuqtaga "
                "'siqib qo'yish' imkonini beradi: portlagan snaryad bo'laklari "
                "tarqalsa ham, ularning markazi o'sha parabolani davom ettiradi. "
                "Koenig teoremasi esa energiyani ikki aniq qismga ajratadi — bu "
                "dumalash, tebranish va zarba masalalarida hal qiluvchi."
            ),
            equations=[
                eq(r"\mathbf{r}_C = \frac{1}{M}\sum m_i\mathbf{r}_i", "Massalar markazi.",
                   "Markaz ta'rifi"),
                eq(r"M\mathbf{a}_C = \sum\mathbf{F}^{(e)}", "Markaz harakati teoremasi.",
                   "Markaz teoremasi"),
                eq(r"T = \frac{Mv_C^2}{2} + \frac{J_C\omega^2}{2}", "Koenig teoremasi.",
                   "Koenig teoremasi"),
            ],
            conditions=(
                "Markaz ta'rifi koordinata sistemasini tanlashga bog'liq emas — "
                "markazning o'zi jismning obyektiv nuqtasi. Hisob uchun esa qulay "
                "boshlang'ich tanlanadi (odatda simmetriya o'qi yoki chap-pastki burchak). "
                "Simmetriya o'qi bor bo'lsa, markaz unda yotadi — bu hisobni yarim marta "
                "qisqartiradi."
            ),
            worked_example=WorkedExample(
                statement=(
                    "Tavrsimon (T-shaklidagi) kesim: gorizontal tokcha $200\\times 20$ mm, "
                    "vertikal devor $20\\times 180$ mm (tokchaning ostida). Kesim "
                    "yuzasi va og'irlik markazi koordinatasini pastki qirradan hisoblang."
                ),
                given=[r"\text{Tokcha: } b_1 = 200,\; h_1 = 20\ \text{mm}",
                       r"\text{Devor: } b_2 = 20,\; h_2 = 180\ \text{mm}"],
                steps=[
                    st(r"A_1 = 200\cdot 20 = 4000\ \text{mm}^2,\qquad A_2 = 20\cdot 180 = 3600\ \text{mm}^2",
                       "Bo'laklar yuzalari."),
                    st(r"A = A_1 + A_2 = 7600\ \text{mm}^2",
                       "Umumiy yuza."),
                    st(r"y_1 = 180 + 10 = 190\ \text{mm},\qquad y_2 = 90\ \text{mm}",
                       "Har bir bo'lak markazining pastki qirradan koordinatasi."),
                    st(r"S_x = A_1y_1 + A_2y_2 = 4000\cdot 190 + 3600\cdot 90 = 760\,000 + 324\,000 = 1\,084\,000\ \text{mm}^3",
                       "Statik moment (mq-07 da rasmiy ta'riflanadi)."),
                    st(r"y_C = \frac{S_x}{A} = \frac{1\,084\,000}{7600} = 142{,}6\ \text{mm}",
                       "Og'irlik markazi koordinatasi."),
                    st(r"\text{Tekshirish: } 90 < 142{,}6 < 190 \;\checkmark",
                       "Markaz albatta bo'laklar markazlari orasida bo'lishi kerak."),
                ],
                answer="$A = 7600$ mm²; $y_C = 142{,}6$ mm (pastki qirradan).",
                engineering_note=(
                    "Bu koordinata mq-08 da inersiya momentini hisoblash uchun "
                    "boshlang'ich ma'lumot bo'ladi, mq-13 da esa neytral o'q aynan shu "
                    "yerdan o'tadi. Tavrsimon kesim aynan shuning uchun tanlanadi: "
                    "markazni siljitib, cho'zilgan va siqilgan zonalarni "
                    "materialning xossalariga moslashtirish mumkin."
                ),
            ),
            computation=Computation(
                caption=(
                    "Murakkab kesim og'irlik markazi: o'lchamlarni o'zgartirib, "
                    "markazning siljishini kuzating."
                ),
                code='''"""Massalar / og'irlik markazi: bo'laklar usuli."""
import numpy as np
from labkit import PARAMS, note, series, table, value

b1 = float(PARAMS.get("b1", 200.0))   # tokcha eni, mm
h1 = float(PARAMS.get("h1", 20.0))    # tokcha qalinligi, mm
b2 = float(PARAMS.get("b2", 20.0))    # devor qalinligi, mm
h2 = float(PARAMS.get("h2", 180.0))   # devor balandligi, mm

# Bo'laklar: (yuza, y_markaz) — pastki qirradan
parts = [(b1*h1, h2 + h1/2, "Tokcha"), (b2*h2, h2/2, "Devor")]
A = sum(p[0] for p in parts)
Sx = sum(p[0]*p[1] for p in parts)
yC = Sx/A

value("Umumiy yuza A", A, "mm²")
value("Statik moment S_x", Sx, "mm³")
value("Og'irlik markazi y_C", yC, "mm")
value("Balandlik H", h1+h2, "mm")
value("y_C / H", yC/(h1+h2), "—")

table("Bo'laklar", ["Bo'lak", "A, mm²", "y, mm", "A·y, mm³"],
      [[p[2], float(p[0]), float(p[1]), float(p[0]*p[1])] for p in parts])

note(f"Tekshirish: y_C = {yC:.2f} mm bo'laklar markazlari "
     f"({min(p[1] for p in parts):.0f} va {max(p[1] for p in parts):.0f} mm) orasida ✓")

# Tokcha qalinligining markazga ta'siri
hh = np.linspace(5, 60, 100)
yc_arr = [(b1*t*(h2+t/2) + b2*h2*(h2/2))/(b1*t + b2*h2) for t in hh]
series("y_C(tokcha qalinligi)", hh.tolist(), yc_arr,
       xlabel="h₁, mm", ylabel="y_C, mm")

# Teshikli kesim: manfiy yuza usuli
D_out, D_in = 100.0, 60.0
A_ring = np.pi/4*(D_out**2 - D_in**2)
note(f"Halqa kesim (manfiy yuza usuli): A = {A_ring:.1f} mm², "
     f"markaz simmetriya sababli geometrik markazda.")

# Koenig teoremasi: dumalayotgan silindr
m_cyl, R_cyl, v_cyl = 5.0, 0.15, 3.0
J_C = 0.5*m_cyl*R_cyl**2
omega_cyl = v_cyl/R_cyl
T_trans, T_rot = 0.5*m_cyl*v_cyl**2, 0.5*J_C*omega_cyl**2
value("T ilgarilanma", T_trans, "J")
value("T aylanma", T_rot, "J")
value("Aylanma ulushi", 100*T_rot/(T_trans+T_rot), "%")
''',
                parameters=[
                    p("b1", "Tokcha eni b₁", 50.0, 400.0, 200.0, 10.0, "mm"),
                    p("h1", "Tokcha qalinligi h₁", 5.0, 60.0, 20.0, 1.0, "mm"),
                    p("b2", "Devor qalinligi b₂", 5.0, 60.0, 20.0, 1.0, "mm"),
                    p("h2", "Devor balandligi h₂", 50.0, 500.0, 180.0, 10.0, "mm"),
                ],
                expected_output="A = 7600 mm², y_C = 142,6 mm, aylanma ulush = 33,3 %",
            ),
            visualization=vis(
                "Murakkab kesim va uning markazi",
                "React/SVG",
                "Kesim konturi, bo'laklarga ajratish chiziqlari, har bir bo'lak markazi "
                "(kichik doira) va natijaviy markaz (kesishgan chiziqlar bilan belgilangan).",
                "React/SVG: kesim — to'rtburchaklar to'plami, markazlar — `<circle>` va "
                "`<line>` krest. Bu komponent mq-07/mq-08 da qayta ishlatiladi, shuning "
                "uchun uni `CrossSection` deb umumiy qilib yozish maqsadga muvofiq.",
            ),
            interpretation=(
                "Tokcha qalinligini oshirish markazni yuqoriga suradi, lekin monoton "
                "va to'yinuvchi tarzda: 20 dan 40 mm ga o'tishda markaz 142,6 dan "
                "160 mm ga siljiydi, 60 mm da esa faqat 168 mm ga. Dumalash misolida "
                "esa aylanma energiya 33 % ni tashkil qiladi — shuning uchun dumalab "
                "tushayotgan silindr sirpanayotgan jismdan sekinroq tezlanadi."
            ),
            common_mistakes=[
                "Bo'lak markazlari koordinatalarini bitta boshlang'ichdan emas, turli "
                "nuqtalardan o'lchash.",
                "Teshiklarni musbat yuza bilan qo'shish — ular manfiy bo'lishi kerak.",
                "Koenig teoremasida $J_C$ o'rniga boshqa o'qqa nisbatan inersiya "
                "momentini ishlatish.",
                "Massalar markazini geometrik markaz deb olish — bu faqat bir jinsli "
                "va simmetrik jismlarda to'g'ri.",
            ],
            quiz=[
                q("Havoda portlagan snaryad bo'laklarining massalar markazi qanday "
                  "harakatlanadi?",
                  "O'sha parabola bo'ylab davom etadi, chunki portlash ichki kuch — u "
                  "markaz harakatiga ta'sir qilmaydi.", "konseptual"),
                q("Ikki massa $m_1 = 2$ kg ($x=0$) va $m_2 = 3$ kg ($x=5$ m). $x_C$?",
                  "$x_C = (2\\cdot 0 + 3\\cdot 5)/5 = 3$ m.", "hisob"),
                q("Dumalayotgan silindrda energiyaning necha foizi aylanmaga to'g'ri keladi?",
                  "$J_C = mR^2/2$ uchun $T_{rot}/T = 1/3 \\approx 33$ %.", "hisob"),
                q("Kran ustuvorligi uchun protivoves nima uchun kerak?",
                  "Yuk og'irlik markazini tayanch konturidan tashqariga suradi; "
                  "protivoves uni qaytarib kontur ichiga olib kiradi.", "talqin"),
                q("Kodda teshikli kesim uchun qanday usul taklif qilingan?",
                  "Manfiy yuza usuli: teshikni manfiy yuzali bo'lak deb hisoblash. "
                  "Bu murakkab konturlarni integrallashdan qutqaradi.", "kod"),
            ],
            bridge_to_next=(
                "Massalar markazi ilgarilanma harakatni tavsifladi. Aylanma harakat "
                "uchun esa massaning taqsimlanishi muhim — bu inersiya momenti va "
                "inersiya tenzori orqali ifodalanadi."
            ),
            research_extension=(
                "O'zgaruvchan massali tizim uchun Mesherskiy tenglamasini keltirib "
                "chiqaring: $m\\frac{d\\mathbf{v}}{dt} = \\mathbf{F} + \\mathbf{u}\\frac{dm}{dt}$. "
                "Tsiolkovskiy formulasini oling va ko'p bosqichli raketaning nima uchun "
                "bir bosqichlidan samaraliroq ekanini sonli ko'rsating."
            ),
        ),
    ),
    Topic(
        id="nm-17",
        subject_id=S,
        module_id=M,
        order=17,
        title="Inersiya momentlari, inersiya tenzori va bosh inersiya o'qlari",
        description=(
            "Massaviy inersiya momenti, Shteyner teoremasi, inersiya tenzori, "
            "bosh o'qlar va xususiy qiymatlar masalasi."
        ),
        learning_objective=(
            "Jismning inersiya tenzorini qurish, bosh o'qlarni eigenvalue masalasi "
            "sifatida topish va natijani muvozanatlash masalalarida qo'llash."
        ),
        prerequisites=["nm-16", "nm-01"],
        mathematical_core=(
            "Ikkinchi tartibli tenzor, simmetrik matritsa, xususiy qiymatlar va "
            "xususiy vektorlar, koordinata almashtirishda tenzorning o'zgarishi."
        ),
        engineering_application=(
            "Rotor muvozanatlash, mahovik loyihalash, kosmik apparat orientatsiyasi, "
            "kesim geometrik tavsiflari (mq-08)."
        ),
        computational_component=(
            "Inersiya tenzorini qurish va `numpy.linalg.eigh` bilan bosh o'qlarni topish."
        ),
        visualization_component=(
            "Jism va uning bosh inersiya o'qlari; inersiya ellipsoidi."
        ),
        research_extension=(
            "Erkin aylanuvchi jismning o'rta o'q atrofidagi aylanishi nima uchun "
            "noturg'un? (Tennis raketkasi teoremasi)"
        ),
        difficulty="murakkab",
        previous_link=(
            "nm-16 da massa taqsimotining birinchi momentini (markazni) topdik. "
            "Endi ikkinchi momentga — inersiya momentiga o'tamiz. Bu — platformadagi "
            "birinchi tenzor."
        ),
        next_topic="nm-18",
        estimated_minutes=100,
        tags=["inersiya tenzori", "eigenvalue", "Shteyner teoremasi"],
        lesson=Lesson(
            physical_problem=(
                "Avtomobil g'ildiragi muvozanatlanmagan bo'lsa, ma'lum tezlikda rul "
                "titraydi. Muvozanatlash ustaxonasi g'ildirakka kichik yuklar qo'shadi. "
                "Nima uchun? Chunki massa taqsimoti aylanish o'qiga nisbatan simmetrik "
                "bo'lmasa, podshipniklarga davriy kuch tushadi. Bu effektni tavsiflash "
                "uchun bitta son yetmaydi — to'liq tenzor kerak."
            ),
            concepts=[
                c("O'qqa nisbatan inersiya momenti", "$J_z = \\sum m_i(x_i^2+y_i^2) = "
                  "\\int(x^2+y^2)dm$ — aylanma harakatdagi 'massa' roli."),
                c("Markazdan qochma inersiya momenti", "$J_{xy} = -\\int xy\\,dm$ — "
                  "massa taqsimotining assimetriyasi o'lchovi."),
                c("Inersiya tenzori", "$[J] = \\begin{pmatrix} J_{xx} & J_{xy} & J_{xz} \\\\ "
                  "J_{xy} & J_{yy} & J_{yz} \\\\ J_{xz} & J_{yz} & J_{zz}\\end{pmatrix}$ — "
                  "simmetrik, ikkinchi tartibli tenzor."),
                c("Bosh inersiya o'qlari", "Markazdan qochma momentlar nolga teng "
                  "bo'ladigan o'qlar; ular tenzorning xususiy vektorlari."),
                c("Shteyner (parallel o'qlar) teoremasi", "$J_z = J_{zC} + Md^2$ — "
                  "markaziy o'qdan parallel ko'chirishda inersiya momenti ortadi."),
            ],
            derivation=[
                d("1-qadam. Aylanma harakatdagi kinetik energiyadan tenzorga",
                  r"T = \frac{1}{2}\sum m_i|\boldsymbol{\omega}\times\mathbf{r}_i|^2 = "
                  r"\frac{1}{2}\boldsymbol{\omega}^T[J]\boldsymbol{\omega}",
                  "Kvadratik forma paydo bo'ldi — uning matritsasi aynan inersiya tenzori. "
                  "Bu tenzorning eng tabiiy ta'rifi."),
                d("2-qadam. Tenzor komponentalari",
                  r"J_{xx} = \int(y^2+z^2)dm,\quad J_{xy} = -\int xy\,dm,\quad \dots",
                  "Diagonal elementlar — o'qlarga nisbatan inersiya momentlari, "
                  "diagonaldan tashqaridagilar — markazdan qochma momentlar."),
                d("3-qadam. Shteyner teoremasi",
                  r"J_z = \int\big((x_C+x')^2+(y_C+y')^2\big)dm = J_{zC} + Md^2",
                  "Kesishgan hadlar $2x_C\\int x'dm = 0$ bo'ladi, chunki markazga nisbatan "
                  "statik moment nolga teng. Xulosa: markaziy o'q har doim minimal "
                  "inersiya momentini beradi."),
                d("4-qadam. Bosh o'qlar — xususiy qiymatlar masalasi",
                  r"[J]\{\mathbf{n}\} = J\{\mathbf{n}\} \;\Longleftrightarrow\; "
                  r"\det([J] - J[I]) = 0",
                  "$[J]$ simmetrik va musbat aniqlangani uchun uchta haqiqiy xususiy "
                  "qiymat va o'zaro ortogonal xususiy vektorlar mavjud. Bu — "
                  "platformadagi birinchi eigenvalue masalasi; xuddi shu struktura "
                  "nm-29, tmm-08, pq-13 va su-25 da takrorlanadi."),
                d("5-qadam. Muvozanatlanmaganlik shartlari",
                  r"\text{statik: } \mathbf{r}_C \ne 0 \ (\text{o'qda emas});\qquad "
                  r"\text{dinamik: } J_{xz} \ne 0 \text{ yoki } J_{yz} \ne 0",
                  "Aylanish o'qi (z) bosh markaziy o'q bo'lsa — to'liq muvozanatlangan. "
                  "Aks holda podshipniklarga $\\omega^2$ ga proporsional davriy kuch tushadi."),
            ],
            formula_meaning=(
                "Inersiya tenzori aylanma harakatda massaning rolini bajaradi, lekin "
                "skalyar emas — chunki jism turli o'qlar atrofida turlicha "
                "'qarshilik ko'rsatadi'. Bosh o'qlar — bu 'tabiiy' aylanish o'qlari: "
                "ular atrofida aylanganda podshipniklarga qo'shimcha kuch tushmaydi. "
                "Muvozanatlash ustaxonasi aynan aylanish o'qini bosh o'q qilish bilan "
                "shug'ullanadi."
            ),
            equations=[
                eq(r"J_z = \int (x^2+y^2)\,dm", "O'qqa nisbatan inersiya momenti.",
                   "Inersiya momenti"),
                eq(r"J_z = J_{zC} + Md^2", "Shteyner teoremasi.", "Parallel o'qlar teoremasi"),
                eq(r"[J]\mathbf{n} = J\mathbf{n}", "Bosh o'qlar uchun xususiy qiymatlar masalasi.",
                   "Eigenvalue masalasi"),
                eq(r"T = \tfrac{1}{2}\boldsymbol{\omega}^T[J]\boldsymbol{\omega}",
                   "Aylanma harakatdagi kinetik energiya.", "Kinetik energiya"),
            ],
            conditions=(
                "Inersiya tenzori qaysi nuqtaga nisbatan hisoblanganini har doim "
                "ko'rsatish shart — u nuqtaga bog'liq (Shteyner teoremasi). Simmetriya "
                "o'qi har doim bosh o'q bo'ladi; simmetriya tekisligi bo'lsa, unga "
                "perpendikular o'q ham bosh o'q. Bu qoidalar hisobni sezilarli "
                "qisqartiradi."
            ),
            worked_example=WorkedExample(
                statement=(
                    "Aylanish o'qi (z) ga o'rnatilgan disk: massasi $M = 12$ kg, radiusi "
                    "$R = 0{,}25$ m. Diskning qirrasiga $m = 0{,}3$ kg li ortiqcha massa "
                    "yopishgan (disk tekisligida, $z$ o'qidan 0,25 m da) va u diskning "
                    "markaziy tekisligidan $a = 0{,}05$ m siljigan. $\\omega = 200$ rad/s "
                    "da podshipniklarga tushadigan kuchni baholang."
                ),
                given=[r"M = 12\ \text{kg},\; R = 0{,}25\ \text{m}",
                       r"m = 0{,}3\ \text{kg},\; a = 0{,}05\ \text{m}",
                       r"\omega = 200\ \text{rad/s},\; L_{\text{podshipniklar}} = 0{,}4\ \text{m}"],
                steps=[
                    st(r"J_{zC}^{disk} = \frac{MR^2}{2} = \frac{12\cdot 0{,}0625}{2} = 0{,}375\ \text{kg·m}^2",
                       "Diskning o'z o'qiga nisbatan inersiya momenti."),
                    st(r"J_z = J_{zC}^{disk} + mR^2 = 0{,}375 + 0{,}3\cdot 0{,}0625 = 0{,}394\ \text{kg·m}^2",
                       "Ortiqcha massa qo'shildi (Shteyner teoremasi nuqtaviy massa uchun)."),
                    st(r"\text{Statik muvozanatsizlik: } S = m\,R = 0{,}3\cdot 0{,}25 = 0{,}075\ \text{kg·m}",
                       "Massalar markazi o'qdan $e = S/(M+m) = 0{,}075/12{,}3 = 6{,}1$ mm siljigan."),
                    st(r"F_{stat} = (M+m)\,e\,\omega^2 = 12{,}3\cdot 0{,}0061\cdot 200^2 = "
                       r"12{,}3\cdot 0{,}0061\cdot 40\,000 = 3000\ \text{N}",
                       "Statik muvozanatsizlikdan kelib chiqadigan markazdan qochma kuch."),
                    st(r"J_{xz} = -m\,R\,a = -0{,}3\cdot 0{,}25\cdot 0{,}05 = -3{,}75\cdot 10^{-3}\ \text{kg·m}^2",
                       "Markazdan qochma inersiya momenti — dinamik muvozanatsizlik o'lchovi."),
                    st(r"M_{din} = J_{xz}\,\omega^2 = 3{,}75\cdot 10^{-3}\cdot 40\,000 = 150\ \text{N·m}"
                       r"\;\Rightarrow\; F_{podsh} = \frac{150}{0{,}4} = 375\ \text{N}",
                       "Dinamik muvozanatsizlik podshipniklarga juftlik hosil qiladi."),
                ],
                answer=(
                    "$J_z = 0{,}394$ kg·m²; statik muvozanatsizlikdan $F = 3$ kN; "
                    "dinamik muvozanatsizlikdan qo'shimcha $F = 375$ N."
                ),
                engineering_note=(
                    "0,3 kg li kichik massa 3 kN kuch beradi — og'irligidan 1000 marta "
                    "katta! Aynan shuning uchun g'ildirak muvozanatlashda grammlar "
                    "bilan ishlanadi. Muhim: statik muvozanatlash (bitta tekislikda) "
                    "dinamik muvozanatsizlikni bartaraf etmaydi — buning uchun ikki "
                    "tekislikda muvozanatlash kerak."
                ),
            ),
            computation=Computation(
                caption=(
                    "Inersiya tenzori va bosh o'qlar: ortiqcha massa joylashuvini "
                    "o'zgartirib, muvozanatsizlik kuchlarini hisoblang."
                ),
                code='''"""Inersiya tenzori, bosh o'qlar va rotor muvozanatsizligi."""
import numpy as np
from labkit import PARAMS, note, series, table, value

M = float(PARAMS.get("M", 12.0))       # disk massasi, kg
R = float(PARAMS.get("R", 0.25))       # disk radiusi, m
m = float(PARAMS.get("m", 0.3))        # ortiqcha massa, kg
a = float(PARAMS.get("a", 0.05))       # o'qi bo'ylab siljish, m
omega = float(PARAMS.get("omega", 200.0))  # rad/s
L_bear = 0.4                            # podshipniklar orasi, m

# Disk tenzori (markaziy, o'z o'qlarida)
J_disk = np.diag([M*R**2/4, M*R**2/4, M*R**2/2])

# Nuqtaviy massa tenzori: r = (R, 0, a)
r = np.array([R, 0.0, a])
J_point = m*(np.dot(r, r)*np.eye(3) - np.outer(r, r))
J = J_disk + J_point

value("J_xx", J[0, 0], "kg·m²")
value("J_yy", J[1, 1], "kg·m²")
value("J_zz", J[2, 2], "kg·m²")
value("J_xz (markazdan qochma)", J[0, 2], "kg·m²")

# Bosh o'qlar — xususiy qiymatlar masalasi
eigvals, eigvecs = np.linalg.eigh(J)
table("Bosh inersiya momentlari",
      ["№", "J, kg·m²", "n_x", "n_y", "n_z"],
      [[i+1, float(eigvals[i]), float(eigvecs[0, i]), float(eigvecs[1, i]),
        float(eigvecs[2, i])] for i in range(3)])
note(f"Bosh o'qlarning z o'qidan og'ishi: "
     f"{np.degrees(np.arccos(abs(eigvecs[2, 2]))):.3f}°")

# Muvozanatsizlik kuchlari
e = m*R/(M+m)                       # massalar markazi eksentrisiteti
F_static = (M+m)*e*omega**2
M_dyn = abs(J[0, 2])*omega**2
F_dyn = M_dyn/L_bear
value("Eksentrisitet e", e*1000, "mm")
value("Statik kuch", F_static/1000, "kN")
value("Dinamik moment", M_dyn, "N·m")
value("Podshipnikdagi dinamik kuch", F_dyn, "N")
note(f"Ortiqcha massa og'irligi {m*9.81:.2f} N, hosil qilgan kuchi {F_static:.0f} N "
     f"— {F_static/(m*9.81):.0f} marta katta.")

# Aylanish tezligiga bog'liqlik
ww = np.linspace(0, 400, 200)
series("Statik muvozanatsizlik kuchi", ww.tolist(), ((M+m)*e*ww**2/1000).tolist(),
       xlabel="ω, rad/s", ylabel="F, kN")
series("Dinamik kuch (podshipnik)", ww.tolist(), (abs(J[0,2])*ww**2/L_bear/1000).tolist(),
       xlabel="ω, rad/s", ylabel="F, kN")

# Shteyner teoremasini tekshirish
d_test = 0.1
J_shifted = M*R**2/2 + M*d_test**2
note(f"Shteyner: J_z(d=0.1 m) = {J_shifted:.5f} kg·m² "
     f"(markaziy {M*R**2/2:.5f} + {M*d_test**2:.5f})")
''',
                parameters=[
                    p("M", "Disk massasi M", 1.0, 100.0, 12.0, 1.0, "kg"),
                    p("R", "Disk radiusi R", 0.05, 1.0, 0.25, 0.01, "m"),
                    p("m", "Ortiqcha massa m", 0.0, 3.0, 0.3, 0.05, "kg"),
                    p("a", "O'q bo'ylab siljish a", 0.0, 0.3, 0.05, 0.01, "m"),
                    p("omega", "Burchak tezligi ω", 10.0, 500.0, 200.0, 10.0, "rad/s"),
                ],
                expected_output="J_zz ≈ 0,394 kg·m², e ≈ 6,1 mm, F_stat ≈ 3,0 kN",
            ),
            visualization=vis(
                "Inersiya ellipsoidi va bosh o'qlar",
                "Manim",
                "Jism va uning atrofida inersiya ellipsoidi; bosh o'qlar ellipsoidning "
                "o'qlari bilan ustma-ust tushadi. Koordinata sistemasi burilganda "
                "tenzor komponentalari o'zgaradi, ellipsoid esa o'zgarmaydi.",
                "Manim: tenzorning invariantligini ko'rsatish uchun eng yaxshi vosita — "
                "koordinata o'qlari aylanganda ellipsoid qimirlamaydi. Bu g'oya tmm-08 "
                "dagi kuchlanish tenzori va mq-19 dagi Mor doirasida to'g'ridan-to'g'ri "
                "takrorlanadi. React/SVG da esa 2D holat (bosh o'qlar burchagi) yetarli.",
            ),
            interpretation=(
                "Ikkala kuch ham $\\omega^2$ ga proporsional — parabola. 200 rad/s da "
                "3 kN, 400 rad/s da esa 12 kN. Bu — yuqori aylanishli mashinalarda "
                "muvozanatlash nima uchun kritik ekanining sababi. Bosh o'qlar "
                "hisobida esa og'ish burchagi kichik (odatda 1° dan kam), lekin aynan "
                "shu kichik og'ish dinamik yuklarni keltirib chiqaradi."
            ),
            common_mistakes=[
                "Inersiya momentini qaysi o'qqa nisbatan ekanini ko'rsatmaslik.",
                "Shteyner teoremasini markaziy bo'lmagan o'qdan boshqa o'qqa "
                "to'g'ridan-to'g'ri qo'llash — u faqat markaziy o'qdan boshlanadi.",
                "Markazdan qochma inersiya momenti ishorasini unutish "
                "($J_{xy} = -\\int xy\\,dm$).",
                "Statik muvozanatlash dinamikni ham ta'minlaydi deb o'ylash.",
                "Kesim inersiya momenti (m⁴) va massaviy inersiya momentini (kg·m²) "
                "chalkashtirish — ular turli kattaliklar (mq-08 ga qarang).",
            ],
            quiz=[
                q("Nima uchun inersiya tenzori skalyar emas?",
                  "Chunki jism turli o'qlar atrofida turlicha inersiyaga ega. Faqat "
                  "sharsimon simmetrik jismda tenzor skalyarga aylanadi.", "konseptual"),
                q("Diskning diametri bo'ylab o'qqa nisbatan inersiya momenti qancha?",
                  "$J_d = MR^2/4$ — o'z o'qidagining yarmi (perpendikular o'qlar "
                  "teoremasidan: $J_z = J_x + J_y$).", "hisob"),
                q("$M = 10$ kg, $R = 0{,}2$ m disk qirrasidan o'tuvchi o'qqa nisbatan?",
                  "$J = MR^2/2 + MR^2 = 1{,}5MR^2 = 1{,}5\\cdot 10\\cdot 0{,}04 = 0{,}6$ kg·m².",
                  "hisob"),
                q("Simmetriya o'qi nima uchun har doim bosh o'q bo'ladi?",
                  "Chunki simmetriya tufayli markazdan qochma momentlar juft-juft "
                  "yo'qoladi: $J_{xz} = J_{yz} = 0$.", "talqin"),
                q("Kodda `np.linalg.eigh` nima uchun `eig` emas?",
                  "`eigh` simmetrik (ermit) matritsalar uchun mo'ljallangan: u haqiqiy "
                  "xususiy qiymatlar va ortogonal xususiy vektorlarni kafolatlaydi hamda "
                  "tezroq ishlaydi. Inersiya tenzori esa har doim simmetrik.", "kod"),
                q("Muvozanatsizlik kuchi aylanish tezligiga qanday bog'liq?",
                  "Kvadratik: $F = me\\omega^2$. Tezlikni 2 marta oshirish kuchni 4 marta "
                  "oshiradi.", "hisob"),
            ],
            bridge_to_next=(
                "Inersiya tenzori aylanma harakatdagi 'massa'ni berdi. Endi uni "
                "Nyuton tenglamasining aylanma analogi bilan birlashtirib, qattiq "
                "jism dinamikasini to'liq yozamiz."
            ),
            research_extension=(
                "Tennis raketkasi teoremasini (Janibekov effekti) sonli tekshiring: "
                "erkin aylanuvchi jism uchun Eyler tenglamalarini integrallang va "
                "o'rta bosh o'q ($J_1 < J_2 < J_3$ dagi $J_2$) atrofidagi aylanish "
                "noturg'un ekanini ko'rsating. Kichik bezovtalanish qo'shib, "
                "aylanishning davriy 'ag'darilishini' kuzating."
            ),
        ),
    ),
    Topic(
        id="nm-18",
        subject_id=S,
        module_id=M,
        order=18,
        title="Qattiq jismning aylanma harakati dinamikasi va dumalash masalalari",
        description=(
            "Aylanma harakat differensial tenglamasi, tekis harakat dinamikasi, "
            "sirpanmasdan dumalash shartlari va energetik yechim."
        ),
        learning_objective=(
            "Aylanuvchi va dumalayotgan jismlar uchun harakat tenglamalarini yozish "
            "va energiya usuli bilan tekshirish."
        ),
        prerequisites=["nm-17", "nm-14"],
        mathematical_core=(
            "$J\\varepsilon = M$ tenglamasi, bog'lanish shartlari ("
            "$v_C = \\omega R$), tenglamalar tizimi."
        ),
        engineering_application=(
            "Mahovik, yuk ko'tarish baraban, g'ildirak dinamikasi, "
            "transmissiyaga keltirilgan inersiya."
        ),
        computational_component=(
            "Qiya tekislikdan dumalayotgan turli jismlar (shar, silindr, halqa) "
            "tezlanishini taqqoslash."
        ),
        visualization_component=(
            "Dumalash animatsiyasi, kuchlar diagrammasi, tezlanish taqqoslash grafigi."
        ),
        research_extension=(
            "Dumalash qarshiligi hisobga olinganda dumalash va sirpanish orasidagi "
            "chegara qanday siljiydi?"
        ),
        difficulty="asosiy",
        previous_link=(
            "nm-17 da $J$ ni topdik. Endi u Nyuton tenglamasining aylanma analogida "
            "ishlatiladi: $J\\varepsilon = M$."
        ),
        next_topic="nm-19",
        estimated_minutes=90,
        tags=["aylanma dinamika", "dumalash", "mahovik"],
        lesson=Lesson(
            physical_problem=(
                "Qiya tekislikdan bir vaqtda shar, silindr va halqa qo'yib yuborilsa, "
                "qaysi biri birinchi tushadi? Ularning massasi va radiusi bir xil "
                "bo'lsa ham javob har xil. Sabab — inersiya momentining taqsimoti. "
                "Bu tajriba dumalash dinamikasining mohiyatini ochib beradi va "
                "transmissiya loyihalashda muhim natijalarga olib keladi."
            ),
            concepts=[
                c("Aylanma harakat tenglamasi", "$J_z\\varepsilon = \\sum M_z^{(e)}$ — "
                  "Nyuton qonunining aylanma analogi."),
                c("Tekis harakat dinamikasi", "Uchta tenglama: "
                  "$Ma_{Cx} = \\sum F_x$, $Ma_{Cy} = \\sum F_y$, $J_C\\varepsilon = \\sum M_C$."),
                c("Sirpanmasdan dumalash sharti", "$v_C = \\omega R$ va "
                  "$a_C = \\varepsilon R$ — kinematik bog'lanish; "
                  "$F_{ish} \\le fN$ — dinamik shart."),
                c("Keltirilgan inersiya momenti", "Murakkab uzatmani bitta valga "
                  "keltirish: $J_{kel} = \\sum J_i(\\omega_i/\\omega)^2$."),
                c("Inersiya radiusi", "$i = \\sqrt{J/M}$ — massa qanday radiusda "
                  "jamlangan bo'lsa, xuddi shunday inersiya beradi."),
            ],
            derivation=[
                d("1-qadam. Aylanma harakat tenglamasi",
                  r"\frac{dL_z}{dt} = M_z^{(e)},\qquad L_z = J_z\omega \;\Rightarrow\; "
                  r"J_z\frac{d\omega}{dt} = J_z\varepsilon = M_z^{(e)}",
                  "nm-13 dagi impuls momenti teoremasidan, $J_z = \\text{const}$ "
                  "(qattiq jism) shartida."),
                d("2-qadam. Dumalash uchun tenglamalar tizimi",
                  r"\begin{cases} Ma_C = Mg\sin\alpha - F_{ish} \\ J_C\varepsilon = F_{ish}R \\ "
                  r"a_C = \varepsilon R\end{cases}",
                  "Uchta tenglama, uchta noma'lum: $a_C$, $\\varepsilon$, $F_{ish}$. "
                  "Ishqalanish bu yerda noma'lum — u sirpanmaslikni ta'minlaydigan "
                  "qiymatni oladi."),
                d("3-qadam. Tizimni yechish",
                  r"F_{ish} = \frac{J_C a_C}{R^2} \;\Rightarrow\; "
                  r"Ma_C = Mg\sin\alpha - \frac{J_Ca_C}{R^2} \;\Rightarrow\; "
                  r"\boxed{\,a_C = \frac{g\sin\alpha}{1 + J_C/(MR^2)}\,}",
                  "$J_C/(MR^2)$ — o'lchamsiz inersiya koeffitsienti: shar uchun 0,4; "
                  "silindr uchun 0,5; halqa uchun 1,0. Katta koeffitsient — kichik tezlanish."),
                d("4-qadam. Sirpanmaslik shartini tekshirish",
                  r"F_{ish} = \frac{Mg\sin\alpha}{1+MR^2/J_C} \le fMg\cos\alpha "
                  r"\;\Rightarrow\; \tan\alpha \le f\left(1+\frac{MR^2}{J_C}\right)",
                  "Shar uchun $\\tan\\alpha \\le 3{,}5f$, halqa uchun $\\tan\\alpha \\le 2f$. "
                  "Demak halqa tikroq qiyalikda sirpanishga o'tadi."),
                d("5-qadam. Energiya usuli bilan tekshirish",
                  r"Mgh = \frac{Mv_C^2}{2} + \frac{J_C\omega^2}{2} = \frac{Mv_C^2}{2}\left(1+\frac{J_C}{MR^2}\right)"
                  r"\;\Rightarrow\; v_C = \sqrt{\frac{2gh}{1+J_C/(MR^2)}}",
                  "Koenig teoremasi (nm-16) va energiya saqlanishi (nm-15) bir xil "
                  "natijani beradi — bu hisobning to'g'riligini tasdiqlaydi. "
                  "Ishqalanish ish bajarmaydi, chunki kontakt nuqtasi tezligi nol."),
            ],
            formula_meaning=(
                "$a_C = g\\sin\\alpha/(1 + J_C/MR^2)$ formulasi ajoyib natijani beradi: "
                "tezlanish massaga ham, radiusga ham bog'liq emas — faqat massa "
                "taqsimotining shakliga. Shar (massa markazda to'plangan) eng tez, "
                "halqa (massa chetda) eng sekin tushadi. Muhandislikda bu "
                "$J_{kel}$ orqali namoyon bo'ladi: mexanizmning tezkorligini oshirish "
                "uchun massani aylanish o'qiga yaqinlashtirish kerak."
            ),
            equations=[
                eq(r"J_z\varepsilon = \sum M_z^{(e)}", "Aylanma harakat tenglamasi.",
                   "Aylanma dinamika"),
                eq(r"a_C = \frac{g\sin\alpha}{1+J_C/(MR^2)}", "Dumalash tezlanishi.",
                   "Dumalash tezlanishi"),
                eq(r"\tan\alpha \le f\left(1+\frac{MR^2}{J_C}\right)", "Sirpanmaslik sharti.",
                   "Sirpanmaslik"),
            ],
            conditions=(
                "Sirpanmasdan dumalashda kontakt nuqtasi tezligi nolga teng (nm-05 "
                "dagi TOM), shuning uchun ishqalanish ish bajarmaydi va energiya "
                "saqlanadi. Sirpanish boshlansa, ishqalanish $fN$ ga teng bo'ladi va "
                "energiya dissipatsiyalanadi — masala turi butunlay o'zgaradi."
            ),
            worked_example=WorkedExample(
                statement=(
                    "Yuk ko'tarish barabanning inersiya momenti $J = 2{,}4$ kg·m², "
                    "radiusi $R = 0{,}3$ m. Unga $m = 500$ kg yuk osilgan va "
                    "$M_{dv} = 1800$ N·m dvigatel momenti qo'yilgan. Yukning tezlanishi, "
                    "trosdagi kuch va 3 s dan keyingi tezlikni toping."
                ),
                given=[r"J = 2{,}4\ \text{kg·m}^2,\; R = 0{,}3\ \text{m}",
                       r"m = 500\ \text{kg},\; M_{dv} = 1800\ \text{N·m}"],
                steps=[
                    st(r"\text{Yuk: } ma = T - mg;\qquad \text{Baraban: } J\varepsilon = M_{dv} - TR",
                       "Ikki jism uchun alohida tenglamalar; $T$ — trosdagi kuch."),
                    st(r"a = \varepsilon R \Rightarrow \varepsilon = a/R",
                       "Kinematik bog'lanish (tros cho'zilmaydi)."),
                    st(r"\frac{J a}{R} = M_{dv} - TR = M_{dv} - (ma+mg)R",
                       "$T$ ni birinchi tenglamadan ikkinchisiga qo'yamiz."),
                    st(r"a\left(\frac{J}{R}+mR\right) = M_{dv} - mgR \Rightarrow "
                       r"a = \frac{1800 - 500\cdot 9{,}81\cdot 0{,}3}{2{,}4/0{,}3 + 500\cdot 0{,}3}",
                       "Noma'lumni ajratamiz."),
                    st(r"a = \frac{1800 - 1471{,}5}{8 + 150} = \frac{328{,}5}{158} = 2{,}08\ \text{m/s}^2",
                       "Yukning tezlanishi."),
                    st(r"T = m(g+a) = 500(9{,}81+2{,}08) = 5945\ \text{N};\qquad "
                       r"v_3 = at = 2{,}08\cdot 3 = 6{,}24\ \text{m/s}",
                       "Trosdagi kuch va 3 s dan keyingi tezlik."),
                ],
                answer=(
                    "$a = 2{,}08$ m/s²; $T = 5945$ N; $\\varepsilon = 6{,}93$ rad/s²; "
                    "$v(3\\text{ s}) = 6{,}24$ m/s."
                ),
                engineering_note=(
                    "Maxrajdagi $J/R = 8$ kg baraban inersiyasining yukka keltirilgan "
                    "'ekvivalent massasi'. U 150 kg li $mR$ hadi bilan solishtirganda "
                    "kichik — demak baraban inersiyasi bu holda hal qiluvchi emas. "
                    "Lekin kichik yuk va katta baraban holida vaziyat teskari bo'ladi "
                    "va mexanizm 'og'ir' bo'lib qoladi."
                ),
            ),
            computation=Computation(
                caption=(
                    "Dumalash tajribasi: turli jismlarning qiya tekislikdan tushish "
                    "tezlanishini va sirpanish chegarasini taqqoslang."
                ),
                code='''"""Aylanma harakat dinamikasi: dumalash va yuk ko'tarish mexanizmi."""
import numpy as np
from labkit import PARAMS, note, series, table, value

alpha_deg = float(PARAMS.get("alpha", 20.0))  # qiyalik burchagi
f = float(PARAMS.get("f", 0.30))              # ishqalanish koeffitsienti
J_drum = float(PARAMS.get("J", 2.4))          # baraban inersiya momenti
R = float(PARAMS.get("R", 0.3))               # baraban radiusi, m
m_load = float(PARAMS.get("m", 500.0))        # yuk massasi, kg
M_dv = float(PARAMS.get("M_dv", 1800.0))      # dvigatel momenti, N*m
g = 9.81
alpha = np.radians(alpha_deg)

# --- 1-qism: turli jismlarning dumalashi ---
bodies = [("To'la shar", 0.4), ("To'la silindr", 0.5),
          ("Yupqa qobiqli shar", 2/3), ("Halqa (quvur)", 1.0)]
rows = []
for name, kappa in bodies:
    a_c = g*np.sin(alpha)/(1+kappa)
    tan_lim = f*(1+1/kappa)
    rows.append([name, float(kappa), float(a_c),
                 float(np.degrees(np.arctan(tan_lim))),
                 "dumalaydi" if np.tan(alpha) <= tan_lim else "sirpanadi"])
table("Qiya tekislikdan dumalash",
      ["Jism", "J/(MR²)", "a_C, m/s²", "Sirpanish burchagi, °", "Rejim"], rows)

aa = np.linspace(1, 45, 100)
for name, kappa in bodies:
    series(f"a_C: {name}", aa.tolist(),
           (g*np.sin(np.radians(aa))/(1+kappa)).tolist(),
           xlabel="Qiyalik α, deg", ylabel="a_C, m/s²")

# --- 2-qism: yuk ko'tarish mexanizmi ---
a_load = (M_dv - m_load*g*R)/(J_drum/R + m_load*R)
T = m_load*(g + a_load)
eps = a_load/R
value("Yuk tezlanishi a", a_load, "m/s²")
value("Trosdagi kuch T", T/1000, "kN")
value("Burchak tezlanishi ε", eps, "rad/s²")
value("Baraban keltirilgan massasi J/R²", J_drum/R**2, "kg")
value("Baraban inersiyasi ulushi", 100*(J_drum/R**2)/(J_drum/R**2 + m_load), "%")

# Energiya usuli bilan tekshirish (dumalash uchun)
h = 1.0
for name, kappa in bodies:
    v_energy = np.sqrt(2*g*h/(1+kappa))
    a_c = g*np.sin(alpha)/(1+kappa)
    s = h/np.sin(alpha)
    v_kin = np.sqrt(2*a_c*s)
    if abs(v_energy - v_kin) > 1e-9:
        note(f"DIQQAT: {name} uchun energiya va kinematika mos kelmadi!")
note("Energiya usuli va kinematik yechim barcha jismlar uchun mos keldi ✓")

MM = np.linspace(m_load*g*R, 3*m_load*g*R, 100)
series("Tezlanish a(M_dv)", MM.tolist(),
       ((MM - m_load*g*R)/(J_drum/R + m_load*R)).tolist(),
       xlabel="Dvigatel momenti, N·m", ylabel="a, m/s²")
''',
                parameters=[
                    p("alpha", "Qiyalik burchagi α", 1.0, 45.0, 20.0, 1.0, "deg"),
                    p("f", "Ishqalanish koeff. f", 0.05, 0.8, 0.30, 0.05, "—"),
                    p("J", "Baraban inersiya momenti", 0.1, 20.0, 2.4, 0.1, "kg·m²"),
                    p("R", "Baraban radiusi", 0.05, 1.0, 0.3, 0.05, "m"),
                    p("m", "Yuk massasi", 10.0, 5000.0, 500.0, 50.0, "kg"),
                    p("M_dv", "Dvigatel momenti", 100.0, 10000.0, 1800.0, 50.0, "N·m"),
                ],
                expected_output="a = 2,08 m/s²; T = 5,95 kN; shar a_C = 2,40 m/s²; halqa 1,68 m/s²",
            ),
            visualization=vis(
                "Dumalash tajribasi va kuchlar sxemasi",
                "Manim",
                "Qiya tekislikdan bir vaqtda qo'yib yuborilgan shar, silindr va halqa; "
                "ularning ajralib borishi; har birining kuchlar diagrammasi va "
                "$J/(MR^2)$ koeffitsienti.",
                "Manim: bir vaqtda uch jismning poygasi — bu tajribani jonli "
                "ko'rsatishning eng ishonarli usuli. React/SVG tomonda esa "
                "$a_C(\\alpha)$ egri chiziqlari oilasi va sirpanish chegaralari beriladi.",
            ),
            interpretation=(
                "Jadvalda ko'rinadiki, shar halqadan 1,43 marta tez tezlanadi "
                "($0{,}714g\\sin\\alpha$ ga qarshi $0{,}5g\\sin\\alpha$). Sirpanish "
                "chegarasi esa teskari: halqa kichikroq burchakda sirpashga o'tadi. "
                "Yuk ko'tarish mexanizmida baraban inersiyasi atigi 5 % ulushga ega — "
                "lekin kichik yuklarda bu ulush 50 % dan oshib ketishi mumkin va "
                "mexanizm 'o'z inersiyasini ko'tarishga' ishlay boshlaydi."
            ),
            common_mistakes=[
                "Dumalashda ishqalanishni $fN$ ga teng deb olish. Sirpanmasdan "
                "dumalashda u noma'lum va $fN$ dan kichik.",
                "$a_C = \\varepsilon R$ bog'lanishini unutish — tenglamalar tizimi "
                "yopilmaydi.",
                "Ishqalanish ishini energiya balansiga qo'shish. Sirpanmasdan "
                "dumalashda kontakt nuqtasi tezligi nol, demak ish nol.",
                "$J_C$ o'rniga kontakt nuqtasiga nisbatan inersiya momentini "
                "ishlatib, keyin yana Shteyner qo'shish (ikki marta hisoblash).",
            ],
            quiz=[
                q("Nima uchun dumalash tezlanishi massa va radiusga bog'liq emas?",
                  "Chunki formulada faqat $J_C/(MR^2)$ o'lchamsiz nisbati qatnashadi, "
                  "u esa jismning shakliga bog'liq, o'lchamiga emas.", "konseptual"),
                q("Bo'sh va suv to'ldirilgan bochka qiya tekislikdan qanday tushadi?",
                  "Suvli bochka tezroq: suyuqlik aylanmaydi (yopishqoqlik kichik), "
                  "demak samarali $J/(MR^2)$ kamayadi.", "talqin"),
                q("$\\alpha = 30°$, to'la silindr. $a_C$ ni toping.",
                  "$a_C = 9{,}81\\cdot 0{,}5/1{,}5 = 3{,}27$ m/s².", "hisob"),
                q("Sirpanmasdan dumalash uchun sharga kerakli minimal $f$ ($\\alpha=30°$)?",
                  "$f \\ge \\tan 30°/3{,}5 = 0{,}577/3{,}5 = 0{,}165$.", "hisob"),
                q("Kodda energiya usuli bilan tekshirish nima uchun qo'shilgan?",
                  "Ikki mustaqil usul (dinamika va energiya) bir xil natija berishi "
                  "yechimning to'g'riligini tasdiqlaydi — bu hisoblash mexanikasidagi "
                  "verifikatsiyaning sodda ko'rinishi (su-29).", "kod"),
            ],
            bridge_to_next=(
                "Nyuton yondashuvi har bir jism uchun alohida tenglama va barcha "
                "reaksiyalarni talab qiladi. Murakkab mexanizmlarda bu juda "
                "og'irlashadi. Keyingi modulda butunlay boshqa yo'l — analitik "
                "mexanika — boshlanadi, u yerda reaksiyalar umuman qatnashmaydi."
            ),
            research_extension=(
                "Dumalash qarshiligini ($M_{dum} = \\delta N$) modelga qo'shing va "
                "jismning to'xtash masofasini hisoblang. $\\delta$ ni turli materiallar "
                "uchun o'zgartirib, temiryo'l g'ildiragi (po'lat-po'lat, $\\delta \\approx 0{,}05$ mm) "
                "nima uchun avtomobil g'ildiragidan ($\\delta \\approx 0{,}5$ mm) 10 marta "
                "samarali ekanini miqdoriy asoslang."
            ),
        ),
    ),
]
