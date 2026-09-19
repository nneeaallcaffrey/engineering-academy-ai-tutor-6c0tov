"""TMM / 3-modul: Konstitutiv munosabatlar va elastiklik (tmm-13 … tmm-19)."""

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
M = "tmm-m3"


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
    Topic(
        id="tmm-13",
        subject_id=S, module_id=M, order=13,
        title="Konstitutiv tenglamalar prinsiplari va material simmetriyasi",
        description=(
            "Material tenglamalarini qurish prinsiplari (determinizm, lokallik, "
            "obyektivlik), anizotropiya turlari va elastik doimiylar soni."
        ),
        learning_objective=(
            "Konstitutiv tenglamalarga qo'yiladigan talablarni sanab berish va "
            "material simmetriyasi mustaqil doimiylar sonini qanday kamaytirishini "
            "ko'rsatish."
        ),
        prerequisites=["tmm-12", "tmm-08"],
        mathematical_core=(
            "To'rtinchi tartibli elastiklik tenzori $C_{ijkl}$, simmetriya "
            "shartlari, Voygt notatsiyasi, material simmetriya guruhlari."
        ),
        engineering_application=(
            "Kompozit materiallar, yog'och, monokristallar, to'qimalar; material "
            "sinovlari rejasini tuzish."
        ),
        computational_component=(
            "Turli simmetriyadagi bikrlik matritsalarini qurish va mustaqil "
            "doimiylar sonini tekshirish."
        ),
        visualization_component=(
            "Bikrlik matritsasining tuzilishi turli simmetriyalarda (nolga teng "
            "bo'lmagan elementlar xaritasi)."
        ),
        research_extension=(
            "Kompozit materialning effektiv elastik doimiylarini "
            "mikrostrukturadan hisoblash (gomogenizatsiya)."
        ),
        difficulty="murakkab",
        previous_link=(
            "tmm-10 da 15 ta noma'lum va 9 ta tenglama bor edi. Yetishmayotgan "
            "6 ta tenglama — material tenglamalari. Ular qanday qurilishi kerak?"
        ),
        next_topic="tmm-14",
        estimated_minutes=85,
        tags=["konstitutiv tenglama", "anizotropiya", "elastiklik tenzori"],
        lesson=_lesson(
            problem=(
                "Balans qonunlari har qanday material uchun bir xil: po'lat ham, "
                "suv ham, rezina ham ularga bo'ysunadi. Demak materiallar "
                "orasidagi farq boshqa joyda — konstitutiv tenglamalarda. "
                "Lekin ularni ixtiyoriy tanlab bo'lmaydi: ular bir necha "
                "fundamental prinsipga bo'ysunishi kerak."
            ),
            concepts=[
                c("Determinizm prinsipi", "Joriy kuchlanish deformatsiya tarixi "
                  "bilan to'liq aniqlanadi."),
                c("Lokallik prinsipi", "Nuqtadagi kuchlanish faqat shu nuqta "
                  "atrofidagi deformatsiyaga bog'liq."),
                c("Moddiy obyektivlik", "Konstitutiv tenglama kuzatuvchining "
                  "harakatidan bog'liq bo'lmasligi kerak."),
                c("Elastiklik tenzori", "$\\sigma_{ij} = C_{ijkl}\\varepsilon_{kl}$; "
                  "81 ta komponenta, simmetriyalar tufayli 21 taga tushadi."),
                c("Voygt notatsiyasi", "Tenzorlarni 6 elementli vektor, "
                  "$C$ ni $6\\times6$ matritsa sifatida yozish."),
            ],
            derivation=[
                d("1-qadam. Umumiy chiziqli bog'lanish",
                  r"\sigma_{ij} = C_{ijkl}\varepsilon_{kl},\qquad C_{ijkl}\in\mathbb{R}^{81}",
                  "Eng umumiy chiziqli munosabat: har bir kuchlanish "
                  "komponentasi barcha deformatsiya komponentalariga bog'liq."),
                d("2-qadam. Kuchlanish va deformatsiya simmetriyasidan",
                  r"C_{ijkl} = C_{jikl} = C_{ijlk} \Rightarrow 81 \to 36",
                  "$\\sigma_{ij}$ va $\\varepsilon_{kl}$ simmetrik bo'lgani uchun."),
                d("3-qadam. Energiya mavjudligidan",
                  r"C_{ijkl} = \frac{\partial^2 W}{\partial\varepsilon_{ij}\partial\varepsilon_{kl}} "
                  r"\Rightarrow C_{ijkl} = C_{klij} \Rightarrow 36 \to 21",
                  "Deformatsiya energiyasi $W$ mavjud bo'lsa (giperelastik "
                  "material), aralash hosilalar tartibi ahamiyatsiz."),
                d("4-qadam. Material simmetriyasidan qo'shimcha qisqarish",
                  r"21 \to 13\ (\text{monoklinik}) \to 9\ (\text{ortotrop}) \to "
                  r"5\ (\text{transversal izotrop}) \to 2\ (\text{izotrop})",
                  "Har bir simmetriya tekisligi qo'shimcha cheklov qo'yadi. "
                  "Izotrop materialda faqat 2 ta mustaqil doimiy qoladi — "
                  "$E$ va $\\nu$ (yoki $\\lambda$ va $\\mu$)."),
            ],
            meaning=(
                "Konstitutiv tenglamalar mexanikaning 'material qismi': balans "
                "qonunlari universal, material tenglamalari esa aniq moddaga "
                "xos. Simmetriya tahlili amaliy jihatdan juda muhim: izotrop "
                "material uchun 2 ta sinov yetarli, ortotrop kompozit uchun esa "
                "9 ta mustaqil doimiy o'lchash kerak — bu sinov dasturini "
                "butunlay o'zgartiradi."
            ),
            equations=[
                eq(r"\sigma_{ij} = C_{ijkl}\varepsilon_{kl}", "Umumlashgan Guk qonuni.",
                   "Konstitutiv tenglama"),
                eq(r"C_{ijkl} = C_{klij} = C_{jikl} = C_{ijlk}", "Simmetriya shartlari.",
                   "Simmetriyalar"),
                eq(r"W = \tfrac{1}{2}C_{ijkl}\varepsilon_{ij}\varepsilon_{kl}",
                   "Deformatsiya energiyasi zichligi.", "Energiya"),
            ],
            conditions=(
                "Chiziqli bog'lanish kichik deformatsiyalarda o'rinli. "
                "$C_{ijkl}$ musbat aniqlangan bo'lishi kerak (energiya musbat) — "
                "bu elastik doimiylarga cheklov qo'yadi, masalan izotrop "
                "materialda $-1 < \\nu < 0{,}5$ va $E > 0$."
            ),
            worked=WorkedExample(
                statement=(
                    "Bir yo'nalishli uglerod-epoksid kompozit (transversal "
                    "izotrop): $E_1 = 140$ GPa (tola bo'ylab), $E_2 = E_3 = 10$ "
                    "GPa, $\\nu_{12} = 0{,}3$, $G_{12} = 5$ GPa, "
                    "$\\nu_{23} = 0{,}45$. Mustaqil doimiylar sonini tekshiring "
                    "va $\\nu_{21}$ ni toping."
                ),
                given=[r"E_1 = 140,\ E_2 = E_3 = 10\ \text{GPa};\ \nu_{12}=0{,}3;\ "
                       r"G_{12}=5\ \text{GPa};\ \nu_{23}=0{,}45"],
                steps=[
                    st(r"\text{Transversal izotrop: } E_1, E_2, \nu_{12}, G_{12}, \nu_{23} "
                       r"\Rightarrow 5\ \text{ta mustaqil doimiy}",
                       "$G_{23} = E_2/[2(1+\\nu_{23})]$ mustaqil emas."),
                    st(r"\frac{\nu_{21}}{E_2} = \frac{\nu_{12}}{E_1} \Rightarrow "
                       r"\nu_{21} = \nu_{12}\frac{E_2}{E_1} = 0{,}3\cdot\frac{10}{140}",
                       "Maksvell–Betti simmetriyasidan (bikrlik matritsasi "
                       "simmetrik)."),
                    st(r"\nu_{21} = 0{,}0214",
                       "Juda kichik — tola yo'nalishida cho'zilsa, ko'ndalang "
                       "torayish katta; ko'ndalang cho'zilsa, bo'ylama torayish "
                       "juda kichik."),
                    st(r"G_{23} = \frac{E_2}{2(1+\nu_{23})} = \frac{10}{2\cdot1{,}45} = 3{,}45\ \text{GPa}",
                       "Izotropiya tekisligida odatdagi bog'lanish o'rinli."),
                    st(r"\frac{E_1}{E_2} = 14 \Rightarrow \text{kuchli anizotropiya}",
                       "Po'latda bu nisbat 1 ga teng (izotrop)."),
                ],
                answer=("5 ta mustaqil doimiy; $\\nu_{21} = 0{,}0214$; "
                        "$G_{23} = 3{,}45$ GPa; anizotropiya darajasi $E_1/E_2 = 14$."),
                engineering_note=(
                    "$\\nu_{12} \\neq \\nu_{21}$ — anizotrop materialning "
                    "muhim xususiyati. Faqat $\\nu_{12}/E_1 = \\nu_{21}/E_2$ "
                    "nisbati saqlanadi. Bu kompozit konstruksiyalarni "
                    "loyihalashda ko'p xatolarga sabab bo'ladi."
                ),
            ),
            computation=Computation(
                caption="Material simmetriyasi: bikrlik matritsalarini quring va taqqoslang.",
                code='''"""Konstitutiv tenglamalar: material simmetriyasi va elastik doimiylar."""
import numpy as np
from labkit import PARAMS, note, series, table, value

E1 = float(PARAMS.get("E1", 140.0))      # GPa
E2 = float(PARAMS.get("E2", 10.0))
nu12 = float(PARAMS.get("nu12", 0.3))
G12 = float(PARAMS.get("G12", 5.0))
nu23 = float(PARAMS.get("nu23", 0.45))

nu21 = nu12*E2/E1
G23 = E2/(2*(1+nu23))
value("ν₂₁", nu21, "—")
value("G₂₃", G23, "GPa")
value("Anizotropiya E₁/E₂", E1/E2, "—")
note(f"Maksvell simmetriyasi: ν₁₂/E₁ = {nu12/E1:.6f} = ν₂₁/E₂ = {nu21/E2:.6f} ✓")

# Moslashuvchanlik matritsasi (transversal izotrop, Voygt)
S = np.zeros((6, 6))
S[0, 0] = 1/E1; S[1, 1] = S[2, 2] = 1/E2
S[0, 1] = S[1, 0] = S[0, 2] = S[2, 0] = -nu12/E1
S[1, 2] = S[2, 1] = -nu23/E2
S[3, 3] = 1/G23; S[4, 4] = S[5, 5] = 1/G12
C = np.linalg.inv(S)

table("Bikrlik matritsasi C (GPa)",
      ["", "1", "2", "3", "4", "5", "6"],
      [[f"{i+1}"] + [float(round(C[i, j], 2)) for j in range(6)] for i in range(6)])

nonzero = int(np.sum(np.abs(C) > 1e-9))
value("Nolga teng bo'lmagan elementlar", nonzero, "dona")
value("Simmetriya xatosi", float(np.max(np.abs(C - C.T))), "GPa")
eigC = np.linalg.eigvalsh(C)
note(f"C xususiy qiymatlari: {np.round(eigC, 2)} — "
     f"{'musbat aniqlangan ✓' if np.all(eigC > 0) else 'MUSBAT ANIQLANMAGAN — fizik jihatdan xato!'}")

table("Material simmetriyasi va mustaqil doimiylar",
      ["Simmetriya turi", "Mustaqil doimiylar", "Misol"],
      [["Anizotrop (triklinik)", 21, "Kristall (eng past simmetriya)"],
       ["Monoklinik", 13, "Ba'zi minerallar"],
       ["Ortotrop", 9, "Yog'och, to'qima kompozit"],
       ["Transversal izotrop", 5, "Bir yo'nalishli kompozit"],
       ["Kubik", 3, "Metall monokristall"],
       ["Izotrop", 2, "Po'lat, alyuminiy (polikristall)"]])

# Anizotropiyaning bikrlikka ta'siri: burchakka bog'liq E
angles = np.linspace(0, 90, 91)
E_theta = []
for a in angles:
    t = np.radians(a)
    c4, s4 = np.cos(t)**4, np.sin(t)**4
    cs = np.cos(t)**2*np.sin(t)**2
    inv_E = c4/E1 + s4/E2 + cs*(1/G12 - 2*nu12/E1)
    E_theta.append(1/inv_E)
series("E(θ) — tola burchagiga bog'liq", angles.tolist(), E_theta,
       xlabel="Tola burchagi θ, deg", ylabel="E, GPa")
note(f"θ = 0°: E = {E_theta[0]:.1f} GPa; θ = 45°: E = {E_theta[45]:.1f} GPa; "
     f"θ = 90°: E = {E_theta[90]:.1f} GPa — anizotropiya juda kuchli.")

# Izotrop hol bilan taqqoslash
E_iso, nu_iso = 200.0, 0.3
lam = E_iso*nu_iso/((1+nu_iso)*(1-2*nu_iso))
mu = E_iso/(2*(1+nu_iso))
value("Lame λ (po'lat)", lam, "GPa")
value("Lame μ = G (po'lat)", mu, "GPa")
''',
                parameters=[
                    p("E1", "E₁ (tola bo'ylab)", 10.0, 400.0, 140.0, 5.0, "GPa"),
                    p("E2", "E₂ (ko'ndalang)", 1.0, 100.0, 10.0, 1.0, "GPa"),
                    p("nu12", "ν₁₂", 0.0, 0.49, 0.3, 0.01, "—"),
                    p("G12", "G₁₂", 0.5, 50.0, 5.0, 0.5, "GPa"),
                    p("nu23", "ν₂₃", 0.0, 0.49, 0.45, 0.01, "—"),
                ],
                expected_output="ν₂₁ = 0,0214; G₂₃ = 3,45 GPa; C musbat aniqlangan",
            ),
            visual=vis(
                "Bikrlik matritsasining tuzilishi",
                "React/SVG",
                "$6\\times6$ matritsa to'ri; nolga teng bo'lmagan elementlar "
                "bo'yalgan, qiymati rang intensivligi bilan. Turli simmetriya "
                "turlari uchun naqshlar yonma-yon.",
                "React/SVG: matritsa strukturasini kvadratchalar to'ri bilan "
                "ko'rsatish (spy plot) — simmetriya turlari orasidagi farqni "
                "bir qarashda ochib beradi.",
            ),
            interp=(
                "$E(\\theta)$ grafigi anizotropiyaning amaliy oqibatini "
                "ko'rsatadi: tola yo'nalishidan $45°$ og'ishda bikrlik 10 "
                "marta kamayadi. Bu kompozit konstruksiyalarni loyihalashda "
                "qatlamlar yo'nalishini tanlashning asosi. Matritsa musbat "
                "aniqlanganligi esa material doimiylarining fizik jihatdan "
                "to'g'riligini tasdiqlaydi."
            ),
            mistakes=[
                "$\\nu_{12} = \\nu_{21}$ deb hisoblash — anizotrop materialda "
                "ular farq qiladi.",
                "Voygt notatsiyasida siljish deformatsiyalari uchun "
                "koeffitsient 2 ni unutish.",
                "Bikrlik matritsasining musbat aniqlanganligini tekshirmaslik.",
                "Kompozit uchun izotrop formulalarni qo'llash.",
            ],
            quiz=[
                q("Nima uchun $C_{ijkl}$ da 81 emas, 21 ta mustaqil komponenta bor?",
                  "Kuchlanish va deformatsiya simmetriyasi 36 taga, energiya "
                  "mavjudligi esa 21 taga tushiradi.", "konseptual"),
                q("Izotrop materialda nechta mustaqil doimiy bor?",
                  "2 ta: $E$ va $\\nu$ (yoki Lame konstantalari $\\lambda$, $\\mu$).",
                  "konseptual"),
                q("$E_1 = 100$ GPa, $E_2 = 8$ GPa, $\\nu_{12} = 0{,}28$. "
                  "$\\nu_{21}$?",
                  "$\\nu_{21} = 0{,}28\\cdot8/100 = 0{,}0224$.", "hisob"),
                q("Moddiy obyektivlik prinsipi nimani talab qiladi?",
                  "Konstitutiv tenglama kuzatuvchining harakatidan bog'liq "
                  "bo'lmasligini — masalan, qattiq burilish kuchlanish hosil "
                  "qilmasligi kerak.", "talqin"),
                q("Kodda $E(\\theta)$ formulasi nimani ko'rsatadi?",
                  "Anizotrop materialda bikrlik yo'nalishga bog'liq; "
                  "kompozitda tola burchagi hal qiluvchi.", "kod"),
            ],
            bridge=(
                "Umumiy prinsiplar aniqlandi. Endi eng muhim xususiy holga — "
                "chiziqli izotrop elastiklikka o'tamiz."
            ),
            research=(
                "Gomogenizatsiya usulini qo'llang: tola va matritsadan iborat "
                "kompozitning effektiv $E_1$, $E_2$ ni aralashmalar qoidasi "
                "(Voygt va Reuss chegaralari) bilan hisoblang va ularni "
                "tajriba ma'lumotlari bilan taqqoslang. Halpin–Tsai "
                "formulasi nima uchun aniqroq?"
            ),
        ),
    ),
    Topic(
        id="tmm-14",
        subject_id=S, module_id=M, order=14,
        title="Chiziqli izotrop elastiklik: Lame konstantalari va muhandislik doimiylari",
        description=(
            "Izotrop materialning konstitutiv tenglamasi, Lame konstantalari, "
            "ular bilan $E$, $\\nu$, $G$, $K$ orasidagi bog'lanishlar."
        ),
        learning_objective=(
            "Izotrop Guk qonunini tenzor shaklida yozish va elastik doimiylar "
            "orasida erkin o'tish."
        ),
        prerequisites=["tmm-13", "mq-20"],
        mathematical_core=(
            "$\\sigma_{ij} = \\lambda\\varepsilon_{kk}\\delta_{ij} + "
            "2\\mu\\varepsilon_{ij}$, teskari munosabat, doimiylar bog'lanishi."
        ),
        engineering_application=(
            "Barcha metall konstruksiyalar hisobi, FEM material modeli, "
            "elastik doimiylarni tajribada aniqlash."
        ),
        computational_component=(
            "Doimiylar orasida o'tish kalkulyatori va Guk qonunini tenzor "
            "shaklida qo'llash."
        ),
        visualization_component=(
            "Elastik doimiylar orasidagi bog'lanishlar xaritasi; $\\nu$ ning "
            "ta'siri."
        ),
        research_extension=(
            "Elastik doimiylarni ultratovush usuli bilan o'lchash: to'lqin "
            "tezliklari orqali $E$ va $\\nu$ ni aniqlash."
        ),
        difficulty="asosiy",
        previous_link=(
            "tmm-13 dagi 21 ta doimiy izotropiya sharti bilan 2 taga tushdi. "
            "Endi bu ikki doimiyni turli shakllarda yozishni o'rganamiz."
        ),
        next_topic="tmm-15",
        estimated_minutes=80,
        tags=["izotrop elastiklik", "Lame konstantalari", "Guk qonuni"],
        lesson=_lesson(
            problem=(
                "FEM dasturiga material kiritishda ba'zan $E$ va $\\nu$, ba'zan "
                "$\\lambda$ va $\\mu$, ba'zan $K$ va $G$ so'raladi. Ular bir xil "
                "materialni tavsiflaydi, lekin turli kombinatsiyalarda. Qaysi "
                "birini qachon ishlatish kerak va ular qanday bog'langan?"
            ),
            concepts=[
                c("Lame konstantalari", "$\\lambda$ va $\\mu$ — tenzor "
                  "yozuvida eng qulay juftlik; $\\mu = G$ siljish moduli."),
                c("Muhandislik doimiylari", "$E$ (Yung moduli) va $\\nu$ "
                  "(Puasson koeffitsienti) — tajribada bevosita o'lchanadi."),
                c("Hajmiy modul", "$K = \\lambda + \\frac{2}{3}\\mu$ — "
                  "gidrostatik siqilishga qarshilik."),
                c("Tenzor shaklidagi Guk qonuni", "$\\sigma_{ij} = "
                  "\\lambda\\varepsilon_{kk}\\delta_{ij} + 2\\mu\\varepsilon_{ij}$."),
                c("Doimiylar chegaralari", "$E > 0$, $G > 0$, $K > 0$ "
                  "$\\Rightarrow -1 < \\nu < 0{,}5$."),
            ],
            derivation=[
                d("1-qadam. Izotropiyadan eng umumiy shakl",
                  r"C_{ijkl} = \lambda\delta_{ij}\delta_{kl} + \mu(\delta_{ik}\delta_{jl}+\delta_{il}\delta_{jk})",
                  "Izotrop to'rtinchi tartibli tenzor faqat $\\delta_{ij}$ "
                  "orqali qurilishi mumkin — bu ikkita mustaqil doimiy beradi."),
                d("2-qadam. Guk qonunining tenzor shakli",
                  r"\boxed{\;\sigma_{ij} = \lambda\varepsilon_{kk}\delta_{ij} + 2\mu\varepsilon_{ij}\;}",
                  "$C_{ijkl}\\varepsilon_{kl}$ ni yozib chiqamiz. Birinchi had "
                  "hajmiy, ikkinchisi to'liq deformatsiyaga proporsional."),
                d("3-qadam. Izni olib, $K$ ni topish",
                  r"\sigma_{kk} = (3\lambda+2\mu)\varepsilon_{kk} \Rightarrow "
                  r"K = \frac{\sigma_{kk}/3}{\varepsilon_{kk}} = \lambda+\tfrac{2}{3}\mu",
                  "Gidrostatik holatda hajmiy modul."),
                d("4-qadam. Muhandislik doimiylariga o'tish",
                  r"E = \frac{\mu(3\lambda+2\mu)}{\lambda+\mu},\qquad "
                  r"\nu = \frac{\lambda}{2(\lambda+\mu)}",
                  "Bir o'qli cho'zilish sharti ($\\sigma_{22}=\\sigma_{33}=0$) "
                  "dan olinadi."),
                d("5-qadam. Teskari munosabat",
                  r"\varepsilon_{ij} = \frac{1+\nu}{E}\sigma_{ij} - \frac{\nu}{E}\sigma_{kk}\delta_{ij}",
                  "Guk qonunini deformatsiyaga nisbatan yechish — mq-20 dagi "
                  "umumlashgan Guk qonunining tenzor shakli."),
            ],
            meaning=(
                "Lame konstantalari matematik jihatdan qulay ($\\sigma$ va "
                "$\\varepsilon$ orasidagi bog'lanish eng sodda), muhandislik "
                "doimiylari esa fizik jihatdan tushunarli va bevosita "
                "o'lchanadi. $K$ va $G$ juftligi esa eng fizik: ular hajm va "
                "shakl o'zgarishiga alohida javob beradi. $\\nu \\to 0{,}5$ da "
                "$\\lambda \\to \\infty$ — bu siqilmaydigan materialda sonli "
                "muammolar (locking) keltirib chiqaradi (su-22)."
            ),
            equations=[
                eq(r"\sigma_{ij} = \lambda\varepsilon_{kk}\delta_{ij}+2\mu\varepsilon_{ij}",
                   "Izotrop Guk qonuni (tenzor shakli).", "Guk qonuni"),
                eq(r"\lambda = \frac{E\nu}{(1+\nu)(1-2\nu)},\quad \mu = G = \frac{E}{2(1+\nu)}",
                   "Lame konstantalari.", "Lame"),
                eq(r"K = \frac{E}{3(1-2\nu)}", "Hajmiy modul.", "Hajmiy modul"),
            ],
            conditions=(
                "Musbat aniqlanganlik: $\\mu > 0$ va $K > 0$, bu "
                "$-1 < \\nu < 0{,}5$ va $E > 0$ ni beradi. $\\nu = 0{,}5$ "
                "chegaraviy hol: material siqilmaydi, $\\lambda \\to \\infty$ "
                "va standart FEM formulirovkasi buziladi — maxsus elementlar "
                "kerak."
            ),
            worked=WorkedExample(
                statement=(
                    "Po'lat: $E = 200$ GPa, $\\nu = 0{,}3$. (a) Lame "
                    "konstantalari, $G$ va $K$ ni toping; (b) deformatsiya "
                    "holati $\\varepsilon_{11} = 10^{-3}$, "
                    "$\\varepsilon_{22} = -3\\cdot10^{-4}$, "
                    "$\\varepsilon_{33} = -3\\cdot10^{-4}$, "
                    "$\\varepsilon_{12} = 2\\cdot10^{-4}$ bo'lsa, kuchlanishlarni "
                    "hisoblang."
                ),
                given=[r"E = 200\ \text{GPa},\ \nu = 0{,}3"],
                steps=[
                    st(r"\mu = G = \frac{200}{2(1{,}3)} = 76{,}92\ \text{GPa}",
                       "Siljish moduli."),
                    st(r"\lambda = \frac{200\cdot0{,}3}{1{,}3\cdot0{,}4} = \frac{60}{0{,}52} = "
                       r"115{,}4\ \text{GPa}",
                       "Birinchi Lame konstantasi."),
                    st(r"K = \frac{200}{3(0{,}4)} = 166{,}7\ \text{GPa}",
                       "Hajmiy modul. Tekshirish: "
                       "$\\lambda + \\frac{2}{3}\\mu = 115{,}4+51{,}3 = 166{,}7$ ✓"),
                    st(r"\varepsilon_{kk} = 10^{-3}-3\cdot10^{-4}-3\cdot10^{-4} = 4\cdot10^{-4}",
                       "Hajmiy deformatsiya."),
                    st(r"\sigma_{11} = \lambda\varepsilon_{kk}+2\mu\varepsilon_{11} = "
                       r"115{,}4\cdot10^9\cdot4\cdot10^{-4} + 2\cdot76{,}92\cdot10^9\cdot10^{-3}",
                       "$= 46{,}15 + 153{,}85 = 200{,}0$ MPa."),
                    st(r"\sigma_{12} = 2\mu\varepsilon_{12} = 2\cdot76{,}92\cdot10^9\cdot2\cdot10^{-4} = "
                       r"30{,}77\ \text{MPa}",
                       "Siljish kuchlanishi. $\\sigma_{22} = \\sigma_{33} = "
                       "46{,}15 - 46{,}15 = 0$ MPa — bir o'qli holat."),
                ],
                answer=(
                    "$\\lambda = 115{,}4$ GPa, $\\mu = G = 76{,}92$ GPa, "
                    "$K = 166{,}7$ GPa; $\\sigma_{11} = 200$ MPa, "
                    "$\\sigma_{22} = \\sigma_{33} = 0$, $\\sigma_{12} = 30{,}77$ MPa."
                ),
                engineering_note=(
                    "$\\sigma_{22} = \\sigma_{33} = 0$ chiqishi tasodifiy emas: "
                    "berilgan deformatsiyalar aynan bir o'qli cho'zilishga mos "
                    "($\\varepsilon_{22} = -\\nu\\varepsilon_{11}$). Bu — Guk "
                    "qonunini tekshirishning yaxshi usuli."
                ),
            ),
            computation=Computation(
                caption="Elastik doimiylar kalkulyatori va tenzor Guk qonuni.",
                code='''"""Izotrop elastiklik: Lame konstantalari va Guk qonuni."""
import numpy as np
from labkit import PARAMS, note, series, table, value

E = float(PARAMS.get("E", 200.0))        # GPa
nu = float(PARAMS.get("nu", 0.3))
e11 = float(PARAMS.get("e11", 1000.0))*1e-6   # µε -> ε
e22 = float(PARAMS.get("e22", -300.0))*1e-6
e12 = float(PARAMS.get("e12", 200.0))*1e-6

mu = E/(2*(1+nu))
lam = E*nu/((1+nu)*(1-2*nu))
K = E/(3*(1-2*nu))
value("μ = G", mu, "GPa")
value("λ", lam, "GPa")
value("K", K, "GPa")
note(f"Tekshirish: λ + 2μ/3 = {lam + 2*mu/3:.4f} GPa = K ✓")

# Guk qonuni tenzor shaklida
eps = np.array([[e11, e12, 0.0], [e12, e22, 0.0], [0.0, 0.0, e22]])
tr_eps = np.trace(eps)
sig = lam*tr_eps*np.eye(3) + 2*mu*eps       # GPa
table("Kuchlanish tenzori (MPa)",
      ["", "1", "2", "3"],
      [[f"{i+1}"] + [float(round(sig[i, j]*1000, 3)) for j in range(3)] for i in range(3)])

value("σ₁₁", float(sig[0, 0]*1000), "MPa")
value("σ₂₂", float(sig[1, 1]*1000), "MPa")
value("σ₁₂", float(sig[0, 1]*1000), "MPa")
value("Hajmiy deformatsiya", tr_eps*1e6, "µε")
value("O'rtacha kuchlanish", float(np.trace(sig)/3*1000), "MPa")

# Teskari tekshirish
eps_back = (1+nu)/E*sig - nu/E*np.trace(sig)*np.eye(3)
note(f"Teskari Guk qonuni tekshiruvi: maksimal farq "
     f"{np.max(np.abs(eps_back - eps))*1e6:.4f} µε ✓")

# Doimiylar orasidagi o'tish jadvali
table("Elastik doimiylar o'zaro bog'lanishi",
      ["Berilgan", "E", "ν", "G", "K", "λ"],
      [["E, ν", E, nu, float(mu), float(K), float(lam)],
       ["G, K", float(9*K*mu/(3*K+mu)), float((3*K-2*mu)/(2*(3*K+mu))),
        float(mu), float(K), float(K-2*mu/3)],
       ["λ, μ", float(mu*(3*lam+2*mu)/(lam+mu)), float(lam/(2*(lam+mu))),
        float(mu), float(lam+2*mu/3), float(lam)]])

# Puasson koeffitsientining ta'siri
nn = np.linspace(0.0, 0.499, 200)
series("λ(ν)", nn.tolist(), (E*nn/((1+nn)*(1-2*nn))).tolist(), xlabel="ν", ylabel="λ, GPa")
series("K(ν)", nn.tolist(), (E/(3*(1-2*nn))).tolist(), xlabel="ν", ylabel="K, GPa")
series("G(ν)", nn.tolist(), (E/(2*(1+nn))).tolist(), xlabel="ν", ylabel="G, GPa")
note("ν → 0,5 da λ va K cheksizlikka intiladi — siqilmaydigan material. "
     "Bu FEM da 'volumetric locking' muammosini keltirib chiqaradi (su-22).")

# To'lqin tezliklari orqali doimiylarni aniqlash (tmm-20 ga tayyorgarlik)
rho = 7850.0
c_L = np.sqrt((lam + 2*mu)*1e9/rho)
c_T = np.sqrt(mu*1e9/rho)
value("Bo'ylama to'lqin tezligi c_L", c_L, "m/s")
value("Ko'ndalang to'lqin tezligi c_T", c_T, "m/s")
value("c_L/c_T nisbati", c_L/c_T, "—")
nu_from_waves = (c_L**2 - 2*c_T**2)/(2*(c_L**2 - c_T**2))
note(f"To'lqin tezliklaridan tiklangan ν = {nu_from_waves:.4f} (haqiqiy {nu}) — "
     "ultratovush usulining asosi.")

table("Materiallar uchun elastik doimiylar",
      ["Material", "E, GPa", "ν", "G, GPa", "K, GPa"],
      [[nm, Ei, ni, Ei/(2*(1+ni)), Ei/(3*(1-2*ni))]
       for nm, Ei, ni in [("Po'lat", 200, 0.30), ("Alyuminiy", 70, 0.33),
                          ("Titan", 110, 0.34), ("Shisha", 70, 0.22),
                          ("Beton", 30, 0.20), ("Rezina", 0.01, 0.499)]])
''',
                parameters=[
                    p("E", "Yung moduli E", 0.001, 500.0, 200.0, 1.0, "GPa"),
                    p("nu", "Puasson koeff. ν", -0.5, 0.499, 0.3, 0.01, "—"),
                    p("e11", "ε₁₁", -5000.0, 5000.0, 1000.0, 50.0, "µε"),
                    p("e22", "ε₂₂", -5000.0, 5000.0, -300.0, 50.0, "µε"),
                    p("e12", "ε₁₂", -2000.0, 2000.0, 200.0, 50.0, "µε"),
                ],
                expected_output="λ = 115,4 GPa, μ = 76,92 GPa, K = 166,7 GPa, σ₁₁ = 200 MPa",
            ),
            visual=vis(
                "Elastik doimiylar bog'lanishlari",
                "React/SVG",
                "$\\lambda(\\nu)$, $K(\\nu)$, $G(\\nu)$ egri chiziqlari bir "
                "grafikda; $\\nu \\to 0{,}5$ da ikkitasining cheksizlikka "
                "intilishi ko'rsatilgan.",
                "React/SVG: uch egri chiziqni bir grafikda berish "
                "doimiylarning turli xatti-harakatini ochib beradi — $G$ "
                "chekli qoladi, $\\lambda$ va $K$ portlaydi.",
            ),
            interp=(
                "$\\nu \\to 0{,}5$ da $\\lambda$ va $K$ cheksizlikka "
                "intiladi — bu siqilmaydigan materialning matematik "
                "belgisi va FEM da 'volumetric locking' muammosining "
                "manbai. To'lqin tezliklaridan $\\nu$ ni tiklash esa "
                "ultratovush nazoratining asosi: materialni buzmasdan "
                "elastik doimiylarni o'lchash mumkin."
            ),
            mistakes=[
                "$\\lambda$ va $\\mu$ ni $E$ va $\\nu$ bilan chalkashtirish.",
                "Tenzor Guk qonunida $\\varepsilon_{kk}$ o'rniga "
                "$\\varepsilon_{ij}$ ni qo'yish.",
                "Siljish uchun $\\sigma_{12} = \\mu\\gamma_{12} = 2\\mu\\varepsilon_{12}$ "
                "da koeffitsientni chalkashtirish.",
                "$\\nu > 0{,}5$ qiymatlarni ishlatish.",
            ],
            quiz=[
                q("Nima uchun izotrop materialda faqat 2 ta mustaqil doimiy bor?",
                  "Izotrop to'rtinchi tartibli tenzor faqat $\\delta_{ij}$ "
                  "kombinatsiyalaridan qurilishi mumkin — bu ikkita "
                  "koeffitsient beradi.", "konseptual"),
                q("$E = 70$ GPa, $\\nu = 0{,}33$. $G$ ni toping.",
                  "$G = 70/(2\\cdot1{,}33) = 26{,}3$ GPa.", "hisob"),
                q("$\\nu = 0{,}5$ da $K$ nimaga teng?",
                  "Cheksizlikka intiladi — material siqilmaydi.", "hisob"),
                q("Qaysi doimiylar juftligi fizik jihatdan eng tabiiy?",
                  "$K$ va $G$ — ular hajm va shakl o'zgarishiga alohida "
                  "javob beradi; bu ajratish plastiklik nazariyasida ham "
                  "ishlatiladi.", "talqin"),
                q("Kodda to'lqin tezliklaridan $\\nu$ qanday tiklangan?",
                  "$c_L$ va $c_T$ nisbati orqali: "
                  "$\\nu = (c_L^2-2c_T^2)/[2(c_L^2-c_T^2)]$ — bu ultratovush "
                  "nazoratining asosiy formulasi.", "kod"),
            ],
            bridge=(
                "Material tenglamalari tayyor. Endi ularni balans qonunlari "
                "bilan birlashtirib, elastiklik nazariyasining to'la "
                "masalasini qo'yamiz."
            ),
            research=(
                "Ultratovush usuli bilan elastik doimiylarni aniqlashni "
                "modellashtiring: bo'ylama va ko'ndalang to'lqin tezliklarini "
                "'o'lchab', ulardan $E$, $\\nu$, $G$ ni tiklang. O'lchash "
                "xatoligining (±1 %) natijaga ta'sirini baholang — qaysi "
                "doimiy eng sezgir?"
            ),
        ),
    ),
    Topic(
        id="tmm-15",
        subject_id=S, module_id=M, order=15,
        title="Elastiklik nazariyasining to'la masalasi va Navye tenglamalari",
        description=(
            "15 ta tenglama va 15 ta noma'lum, ko'chish usuli (Navye "
            "tenglamalari), kuchlanish usuli (Beltrami–Mitchell), yechimning "
            "yagonaligi."
        ),
        learning_objective=(
            "Elastiklik masalasini to'liq qo'yish va ko'chish usulida "
            "Navye tenglamalarini keltirib chiqarish."
        ),
        prerequisites=["tmm-14", "tmm-10", "tmm-05"],
        mathematical_core=(
            "Elliptik PDE tizimi, Navye tenglamalari "
            "$\\mu\\nabla^2\\mathbf{u} + (\\lambda+\\mu)\\nabla(\\nabla\\cdot\\mathbf{u}) + "
            "\\rho\\mathbf{b} = 0$."
        ),
        engineering_application=(
            "FEM ning nazariy asosi, analitik yechimlar, chegaraviy "
            "masalalarni qo'yish."
        ),
        computational_component=(
            "Navye tenglamalarini sodda sohada chekli ayirmalar bilan yechish."
        ),
        visualization_component=(
            "Masala tuzilmasi sxemasi: tenglamalar va noma'lumlar bog'lanishi."
        ),
        research_extension=(
            "Yechimning yagonaligi (Kirxgof teoremasi): nima uchun elastiklik "
            "masalasi yagona yechimga ega?"
        ),
        difficulty="ilg'or",
        previous_link=(
            "tmm-10 da 3 ta muvozanat, tmm-05 da 6 ta kinematik, tmm-14 da "
            "6 ta konstitutiv tenglama oldik. Endi ularni birlashtiramiz."
        ),
        next_topic="tmm-16",
        estimated_minutes=90,
        tags=["Navye tenglamalari", "to'la masala", "chegaraviy masala"],
        lesson=_lesson(
            problem=(
                "Murakkab shaklli detalda kuchlanish taqsimotini topish kerak. "
                "Materiallar qarshiligi formulalari bu yerda ishlamaydi. "
                "Elastiklik nazariyasi umumiy masalani qo'yadi: 15 ta tenglama, "
                "15 ta noma'lum. Ularni qanday yechish mumkin va yechim "
                "yagonami?"
            ),
            concepts=[
                c("To'la masala", "3 muvozanat + 6 kinematik + 6 konstitutiv = "
                  "15 tenglama; noma'lumlar: 3 ko'chish + 6 deformatsiya + "
                  "6 kuchlanish."),
                c("Ko'chish usuli", "Barcha noma'lumlarni $u_i$ orqali "
                  "ifodalash — 3 ta tenglama (Navye) qoladi."),
                c("Kuchlanish usuli", "Kuchlanishlarni asosiy noma'lum qilish; "
                  "moslik shartlari kerak (Beltrami–Mitchell)."),
                c("Chegaraviy masala turlari", "1-tur (ko'chish berilgan), "
                  "2-tur (kuchlanish berilgan), aralash."),
                c("Yechimning yagonaligi", "Kirxgof teoremasi: chegaraviy "
                  "shartlar to'g'ri qo'yilsa, yechim yagona (qattiq harakatga "
                  "qadar)."),
            ],
            derivation=[
                d("1-qadam. Kinematikani Guk qonuniga qo'yish",
                  r"\sigma_{ij} = \lambda u_{k,k}\delta_{ij} + \mu(u_{i,j}+u_{j,i})",
                  "$\\varepsilon_{ij} = \\frac{1}{2}(u_{i,j}+u_{j,i})$ ni "
                  "tmm-14 dagi Guk qonuniga qo'yamiz."),
                d("2-qadam. Muvozanat tenglamalariga qo'yish",
                  r"\frac{\partial}{\partial x_j}\big[\lambda u_{k,k}\delta_{ij}+\mu(u_{i,j}+u_{j,i})\big] + \rho b_i = 0",
                  "tmm-10 dagi $\\sigma_{ij,j}+\\rho b_i = 0$ ga qo'yamiz."),
                d("3-qadam. Navye tenglamalari",
                  r"\boxed{\;\mu\nabla^2u_i + (\lambda+\mu)\frac{\partial}{\partial x_i}(\nabla\cdot\mathbf{u}) + \rho b_i = 0\;}",
                  "Hosilalarni guruhlab olamiz. 3 ta ikkinchi tartibli "
                  "elliptik PDE — noma'lumlar soni 15 dan 3 ga tushdi."),
                d("4-qadam. Chegaraviy shartlar",
                  r"u_i = \bar u_i\ \text{on}\ S_u;\qquad "
                  r"\sigma_{ij}n_j = \bar t_i\ \text{on}\ S_t",
                  "Har bir chegara nuqtasida uchta shart (har bir yo'nalish "
                  "uchun bittadan) berilishi kerak."),
                d("5-qadam. Yechimning yagonaligi",
                  r"\text{Ikki yechim farqi } \Delta u_i \Rightarrow "
                  r"\int_V C_{ijkl}\Delta\varepsilon_{ij}\Delta\varepsilon_{kl}\,dV = 0 "
                  r"\Rightarrow \Delta\varepsilon_{ij} = 0",
                  "Energiya musbat aniqlangani uchun farq faqat qattiq "
                  "harakat bo'lishi mumkin. Bu — Kirxgof yagonalik "
                  "teoremasi."),
            ],
            meaning=(
                "Navye tenglamalari elastiklik nazariyasining 'asosiy "
                "tenglamalari': ular Nyuton qonuni, Guk qonuni va "
                "kinematikani bitta ifodaga birlashtiradi. Ularni analitik "
                "yechish faqat sodda geometriyalarda mumkin — shuning uchun "
                "FEM paydo bo'ldi. Yagonalik teoremasi esa hisoblash uchun "
                "hal qiluvchi: agar biror yo'l bilan yechim topilsa, u "
                "yagona to'g'ri yechim."
            ),
            equations=[
                eq(r"\mu\nabla^2\mathbf{u}+(\lambda+\mu)\nabla(\nabla\cdot\mathbf{u})+\rho\mathbf{b} = 0",
                   "Navye tenglamalari (ko'chish usuli).", "Navye tenglamalari"),
                eq(r"\nabla^2\sigma_{ij}+\frac{1}{1+\nu}\sigma_{kk,ij} = -\dots",
                   "Beltrami–Mitchell tenglamalari (kuchlanish usuli).",
                   "Beltrami–Mitchell"),
            ],
            conditions=(
                "Chegara $S = S_u \\cup S_t$ va $S_u \\cap S_t = \\emptyset$ "
                "(har bir nuqtada har bir yo'nalish uchun bitta shart). "
                "$S_u = \\emptyset$ bo'lsa (faqat kuchlanish berilgan), "
                "tashqi kuchlar muvozanatlashgan bo'lishi va yechim qattiq "
                "harakatga qadar aniqlanishi kerak."
            ),
            worked=WorkedExample(
                statement=(
                    "O'z og'irligi ostidagi vertikal ustun (1D masala): "
                    "$u = u(z)$, $b_z = -g$. Navye tenglamasini yeching, "
                    "chegaraviy shartlar: $u(0) = 0$ (tagida qotirilgan), "
                    "$\\sigma_{zz}(H) = 0$ (yuqorisi erkin). "
                    "$H = 50$ m, $E = 30$ GPa (beton), "
                    "$\\rho = 2400$ kg/m³."
                ),
                given=[r"H = 50\ \text{m},\ E = 30\ \text{GPa},\ \rho = 2400\ \text{kg/m}^3"],
                steps=[
                    st(r"1D: \ (\lambda+2\mu)\frac{d^2u}{dz^2} - \rho g = 0",
                       "Bir o'lchovli holda Navye tenglamasi. Yon "
                       "deformatsiya cheklangan bo'lsa $(\\lambda+2\\mu)$, "
                       "erkin bo'lsa $E$ ishlatiladi; bu yerda $E$ olamiz."),
                    st(r"E\frac{d^2u}{dz^2} = \rho g \Rightarrow "
                       r"\frac{du}{dz} = \frac{\rho g z}{E} + C_1",
                       "Birinchi integrallash."),
                    st(r"\sigma_{zz}(H) = E\frac{du}{dz}\bigg|_H = 0 \Rightarrow "
                       r"C_1 = -\frac{\rho g H}{E}",
                       "Yuqori chegara sharti."),
                    st(r"u(z) = \frac{\rho g}{E}\left(\frac{z^2}{2} - Hz\right) + C_2;\quad "
                       r"u(0) = 0 \Rightarrow C_2 = 0",
                       "Ikkinchi integrallash va pastki shart."),
                    st(r"u(H) = \frac{\rho g}{E}\left(\frac{H^2}{2}-H^2\right) = -\frac{\rho gH^2}{2E}",
                       "$= -\\frac{2400\\cdot9{,}81\\cdot2500}{2\\cdot3\\cdot10^{10}} = "
                       "-9{,}81\\cdot10^{-4}$ m $= -0{,}98$ mm."),
                    st(r"\sigma_{zz}(0) = E\left(\frac{\rho g\cdot 0}{E}-\frac{\rho gH}{E}\right) = "
                       r"-\rho gH = -1{,}177\ \text{MPa}",
                       "Tagidagi siquvchi kuchlanish."),
                ],
                answer=(
                    "$u(H) = -0{,}98$ mm (cho'kish); "
                    "$\\sigma_{zz}(0) = -1{,}177$ MPa (siqilish)."
                ),
                engineering_note=(
                    "1 mm cho'kish 50 m balandlikda — juda kichik. Lekin "
                    "kuchlanish 1,18 MPa beton uchun sezilarli emas, "
                    "shuning uchun baland betondan qurilgan minoralarda "
                    "hal qiluvchi mezon o'z og'irligi emas, shamol va "
                    "ustuvorlikdir."
                ),
            ),
            computation=Computation(
                caption="Navye tenglamalarini 1D va 2D sohada sonli yechish.",
                code='''"""Elastiklik nazariyasining to'la masalasi: Navye tenglamalari."""
import numpy as np
from labkit import PARAMS, note, series, table, value

H = float(PARAMS.get("H", 50.0))         # balandlik, m
E = float(PARAMS.get("E", 30e9))         # Pa
rho = float(PARAMS.get("rho", 2400.0))   # kg/m³
nu = float(PARAMS.get("nu", 0.2))
n = int(PARAMS.get("n", 200))            # to'r tugunlari
g = 9.81

mu = E/(2*(1+nu))
lam = E*nu/((1+nu)*(1-2*nu))
value("λ", lam/1e9, "GPa")
value("μ", mu/1e9, "GPa")

# Analitik yechim
z = np.linspace(0, H, n)
u_exact = rho*g/E*(z**2/2 - H*z)
sig_exact = E*(rho*g*z/E - rho*g*H/E)
series("Ko'chish u(z) — analitik", z.tolist(), (u_exact*1000).tolist(),
       xlabel="z, m", ylabel="u, mm")
series("Kuchlanish σ(z) — analitik", z.tolist(), (sig_exact/1e6).tolist(),
       xlabel="z, m", ylabel="σ_zz, MPa")
value("u(H) analitik", float(u_exact[-1]*1000), "mm")
value("σ(0) analitik", float(sig_exact[0]/1e6), "MPa")

# Sonli yechim: chekli ayirmalar
h = z[1]-z[0]
A = np.zeros((n, n)); b = np.zeros(n)
A[0, 0] = 1.0                               # u(0) = 0
for i in range(1, n-1):
    A[i, i-1] = 1.0; A[i, i] = -2.0; A[i, i+1] = 1.0
    b[i] = rho*g*h**2/E
A[-1, -1] = 1.0/h; A[-1, -2] = -1.0/h       # du/dz(H) = 0
b[-1] = 0.0
u_num = np.linalg.solve(A, b)
series("Ko'chish u(z) — sonli", z.tolist(), (u_num*1000).tolist(),
       xlabel="z, m", ylabel="u, mm")
err = np.max(np.abs(u_num - u_exact))
value("Sonli-analitik farq", float(err*1000), "mm")
note(f"Nisbiy xatolik: {err/max(abs(u_exact.min()), 1e-12)*100:.4f} % "
     f"({n} tugun, h = {h:.3f} m)")

# To'r zichligining aniqlikka ta'siri
errs = []
for nn in (21, 41, 81, 161, 321):
    zz = np.linspace(0, H, nn); hh = zz[1]-zz[0]
    Aa = np.zeros((nn, nn)); bb = np.zeros(nn)
    Aa[0, 0] = 1.0
    for i in range(1, nn-1):
        Aa[i, i-1], Aa[i, i], Aa[i, i+1] = 1.0, -2.0, 1.0
        bb[i] = rho*g*hh**2/E
    Aa[-1, -1], Aa[-1, -2] = 1.0/hh, -1.0/hh
    uu = np.linalg.solve(Aa, bb)
    ue = rho*g/E*(zz**2/2 - H*zz)
    errs.append([nn, float(hh), float(np.max(np.abs(uu-ue))*1000)])
table("To'r zichligi va xatolik", ["Tugunlar", "h, m", "Xatolik, mm"], errs)

# Masala tuzilmasi
table("Elastiklik nazariyasining to'la masalasi",
      ["Guruh", "Tenglamalar", "Soni", "Noma'lumlar"],
      [["Muvozanat", "σ_ij,j + ρb_i = 0", 3, "σ_ij (6)"],
       ["Kinematika", "ε_ij = (u_i,j+u_j,i)/2", 6, "ε_ij (6), u_i (3)"],
       ["Konstitutiv", "σ_ij = λε_kk δ_ij + 2με_ij", 6, "—"],
       ["JAMI", "", 15, "15"]])

table("Yechish usullari",
      ["Usul", "Asosiy noma'lum", "Tenglamalar", "Qo'shimcha shart"],
      [["Ko'chish (Navye)", "u_i (3)", "3 ta PDE", "Moslik avtomatik"],
       ["Kuchlanish (B–M)", "σ_ij (6)", "6 ta PDE", "Moslik shartlari kerak"],
       ["Aralash", "u va σ", "—", "Gibrid FEM formulirovkasi"]])

# Navye tenglamasining 2D versiyasi uchun operator matritsasi
note("2D holda Navye tenglamalari: "
     "μ∇²u + (λ+μ)∂/∂x(∂u/∂x + ∂v/∂y) + ρb_x = 0 va shunga o'xshash v uchun. "
     "Bu tizim FEM da diskretlashtiriladi (su-21).")
''',
                parameters=[
                    p("H", "Balandlik H", 1.0, 300.0, 50.0, 5.0, "m"),
                    p("E", "Yung moduli E", 1e9, 4e11, 30e9, 1e9, "Pa"),
                    p("rho", "Zichlik ρ", 500.0, 10000.0, 2400.0, 100.0, "kg/m³"),
                    p("nu", "Puasson koeff. ν", 0.0, 0.49, 0.2, 0.01, "—"),
                    p("n", "To'r tugunlari", 21.0, 500.0, 200.0, 10.0, "dona"),
                ],
                expected_output="u(H) = -0,98 mm, σ(0) = -1,177 MPa, sonli xatolik < 0,01 %",
            ),
            visual=vis(
                "Masala tuzilmasi va yechim",
                "React/SVG",
                "Sxema: 15 ta tenglama va 15 ta noma'lum bloklari, ular "
                "orasidagi bog'lanishlar strelkalar bilan; ko'chish usulida "
                "qisqarish ko'rsatilgan. Yonida $u(z)$ va $\\sigma(z)$ "
                "grafiklari.",
                "React/SVG: masala tuzilmasi diagrammasi elastiklik "
                "nazariyasining mantiqiy skeletini ko'rsatadi — bu "
                "talabalar uchun eng qiyin tushuniladigan jihat.",
            ),
            interp=(
                "Sonli va analitik yechim mos keladi, xatolik to'r zichligi "
                "bilan $h^2$ qonuni bo'yicha kamayadi. Masala tuzilmasi "
                "jadvali esa elastiklik nazariyasining mantiqini ochib "
                "beradi: ko'chish usuli noma'lumlar sonini 15 dan 3 ga "
                "tushiradi va aynan shu sabab FEM da u ustun."
            ),
            mistakes=[
                "Chegaraviy shartlarni har bir yo'nalish uchun alohida "
                "qo'ymaslik.",
                "Faqat kuchlanish berilgan masalada tashqi kuchlar "
                "muvozanatini tekshirmaslik.",
                "Kuchlanish usulida moslik shartlarini unutish.",
                "1D masalada $E$ va $(\\lambda+2\\mu)$ ni chalkashtirish "
                "(yon deformatsiya erkinmi yoki cheklanganmi).",
            ],
            quiz=[
                q("Nima uchun ko'chish usuli FEM da ustun?",
                  "Noma'lumlar soni 15 dan 3 ga tushadi va moslik shartlari "
                  "avtomatik bajariladi.", "konseptual"),
                q("Elastiklik masalasida nechta tenglama va noma'lum bor?",
                  "15 tadan: 3 muvozanat + 6 kinematik + 6 konstitutiv; "
                  "noma'lumlar 3 ko'chish + 6 deformatsiya + 6 kuchlanish.",
                  "konseptual"),
                q("Faqat kuchlanish berilgan masalada yechim qanday aniqlanadi?",
                  "Qattiq harakatga qadar — ko'chishlar ixtiyoriy qattiq "
                  "siljish va burilishga qadar aniqlanadi.", "talqin"),
                q("$\\rho gH$ formulasi nimani beradi?",
                  "O'z og'irligidan tagdagi kuchlanishni; u balandlikka "
                  "chiziqli bog'liq.", "hisob"),
                q("Kodda to'r zichligi xatolikka qanday ta'sir qiladi?",
                  "Xatolik $h^2$ qonuni bo'yicha kamayadi — markaziy "
                  "ayirmalar sxemasining ikkinchi tartibi (su-07).", "kod"),
            ],
            bridge=(
                "Umumiy masala qo'yildi. Endi uning eng muhim xususiy "
                "holiga — tekis masalalarga o'tamiz."
            ),
            research=(
                "Kirxgof yagonalik teoremasini isbotlang: ikki yechim "
                "farqi uchun energiya integralini yozing va u nolga teng "
                "bo'lishidan deformatsiyalar tengligini keltirib chiqaring. "
                "Nima uchun ko'chishlar qattiq harakatga qadar aniqlanadi?"
            ),
        ),
    ),
    Topic(
        id="tmm-16",
        subject_id=S, module_id=M, order=16,
        title="Tekis kuchlanish va tekis deformatsiya masalalari",
        description=(
            "Ikki o'lchovli soddalashtirish shartlari, tekis kuchlanish va "
            "tekis deformatsiya farqi, qalin devorli quvur (Lame) masalasi."
        ),
        learning_objective=(
            "Masalani tekis holga keltirish shartlarini aniqlash va "
            "o'qsimmetrik masalani analitik yechish."
        ),
        prerequisites=["tmm-15", "mq-20"],
        mathematical_core=(
            "2D soddalashtirish, silindrik koordinatalar, Eyler tipidagi ODE, "
            "Lame yechimi."
        ),
        engineering_application=(
            "Bosimli idishlar, quvurlar, tiqilgan joylashuvlar, plitalar, "
            "tunel va shaxta qoplamalari."
        ),
        computational_component=(
            "Lame formulalarini hisoblash va qalin/yupqa devorli quvur "
            "yechimlarini taqqoslash."
        ),
        visualization_component=(
            "Quvur kesimida $\\sigma_r$ va $\\sigma_\\theta$ taqsimoti."
        ),
        research_extension=(
            "Ko'p qatlamli (avtofretaj qilingan) quvurlar: dastlabki "
            "kuchlanish qanday foyda beradi?"
        ),
        difficulty="murakkab",
        previous_link=(
            "tmm-15 dagi umumiy masala 3D da murakkab. Ko'p amaliy holatda "
            "uni 2D ga keltirish mumkin — bu sezilarli soddalashtirish beradi."
        ),
        next_topic="tmm-17",
        estimated_minutes=90,
        tags=["tekis masala", "Lame yechimi", "bosimli idish"],
        lesson=_lesson(
            problem=(
                "Yuqori bosimli gidravlik quvur devori qalin bo'lishi kerak. "
                "Lekin qalin devorda kuchlanish bir tekis taqsimlanmaydi: "
                "ichki sirtda u eng katta. Yupqa devorli formula "
                "($\\sigma = pr/t$) bu yerda katta xatolik beradi. Aniq "
                "yechim qanday?"
            ),
            concepts=[
                c("Tekis kuchlanish", "$\\sigma_{33} = \\sigma_{13} = "
                  "\\sigma_{23} = 0$ — yupqa plastina, tekisligida yuklangan."),
                c("Tekis deformatsiya", "$\\varepsilon_{33} = \\varepsilon_{13} = "
                  "\\varepsilon_{23} = 0$ — uzun jism, o'q bo'ylab cheklangan."),
                c("Ikki holatning bog'lanishi", "Formulalar bir xil, faqat "
                  "elastik doimiylar almashtiriladi: $E \\to E/(1-\\nu^2)$, "
                  "$\\nu \\to \\nu/(1-\\nu)$."),
                c("O'qsimmetrik masala", "Barcha kattaliklar faqat $r$ ga "
                  "bog'liq; masala ODE ga keladi."),
                c("Lame yechimi", "Qalin devorli quvur uchun aniq analitik "
                  "yechim."),
            ],
            derivation=[
                d("1-qadam. O'qsimmetrik muvozanat tenglamasi",
                  r"\frac{d\sigma_r}{dr} + \frac{\sigma_r - \sigma_\theta}{r} = 0",
                  "Silindrik koordinatalarda muvozanat (tmm-10). "
                  "$\\sigma_r - \\sigma_\\theta$ hadi egrilik tufayli paydo bo'ladi."),
                d("2-qadam. Ko'chish orqali ifodalash",
                  r"\varepsilon_r = \frac{du}{dr},\quad \varepsilon_\theta = \frac{u}{r} "
                  r"\Rightarrow \frac{d^2u}{dr^2}+\frac{1}{r}\frac{du}{dr}-\frac{u}{r^2} = 0",
                  "Guk qonuni va kinematikani muvozanatga qo'yamiz. Bu — "
                  "Eyler tipidagi ODE."),
                d("3-qadam. Umumiy yechim",
                  r"u(r) = C_1r + \frac{C_2}{r}",
                  "Eyler tenglamasining yechimi. Ikki doimiy ikkita "
                  "chegaraviy shartdan topiladi."),
                d("4-qadam. Lame formulalari",
                  r"\boxed{\;\sigma_r = \frac{p_ia^2-p_bb^2}{b^2-a^2} - "
                  r"\frac{(p_i-p_b)a^2b^2}{(b^2-a^2)r^2},\quad "
                  r"\sigma_\theta = \frac{p_ia^2-p_bb^2}{b^2-a^2} + "
                  r"\frac{(p_i-p_b)a^2b^2}{(b^2-a^2)r^2}\;}",
                  "Chegaraviy shartlar: $\\sigma_r(a) = -p_i$, "
                  "$\\sigma_r(b) = -p_b$."),
                d("5-qadam. Muhim xossalar",
                  r"\sigma_r + \sigma_\theta = \text{const};\qquad "
                  r"\sigma_\theta^{max} = \sigma_\theta(a) = p_i\frac{b^2+a^2}{b^2-a^2}",
                  "Kuchlanishlar yig'indisi radiusdan bog'liq emas. "
                  "Maksimal halqaviy kuchlanish ichki sirtda."),
            ],
            meaning=(
                "Lame yechimi bosimli idishlar hisobining asosi. Eng muhim "
                "xulosa: devorni qalinlashtirish cheksiz foyda bermaydi — "
                "$b \\to \\infty$ da $\\sigma_\\theta(a) \\to p_i$, ya'ni "
                "ichki bosimdan kam bo'lmaydi. Demak juda yuqori bosimlarda "
                "oddiy quvur yetarli emas va ko'p qatlamli yoki avtofretaj "
                "qilingan konstruksiyalar kerak."
            ),
            equations=[
                eq(r"\frac{d\sigma_r}{dr}+\frac{\sigma_r-\sigma_\theta}{r} = 0",
                   "O'qsimmetrik muvozanat tenglamasi.", "Muvozanat"),
                eq(r"\sigma_\theta(a) = p_i\frac{b^2+a^2}{b^2-a^2}",
                   "Ichki sirtdagi maksimal halqaviy kuchlanish.", "Lame"),
                eq(r"\sigma_\theta^{yupqa} = \frac{p_ir_m}{t}", "Yupqa devorli taqribiy formula.",
                   "Yupqa devor"),
            ],
            conditions=(
                "Tekis kuchlanish: $t/L < 0{,}1$ (yupqa plastina). Tekis "
                "deformatsiya: uzun jism ($L/D > 5$) yoki o'q bo'ylab "
                "harakat cheklangan. Lame yechimi elastik sohada; ichki "
                "sirt oqishga o'tsa, elastik-plastik hisob kerak."
            ),
            worked=WorkedExample(
                statement=(
                    "Gidravlik quvur: ichki radius $a = 40$ mm, tashqi "
                    "$b = 60$ mm, ichki bosim $p_i = 60$ MPa, tashqi "
                    "$p_b = 0$. (a) $\\sigma_r$ va $\\sigma_\\theta$ "
                    "taqsimotini toping; (b) yupqa devorli formula bilan "
                    "taqqoslang; (c) fon Mizes kuchlanishini hisoblang."
                ),
                given=[r"a = 0{,}04\ \text{m},\ b = 0{,}06\ \text{m},\ p_i = 60\ \text{MPa}"],
                steps=[
                    st(r"\frac{b^2}{a^2} = \frac{3600}{1600} = 2{,}25;\quad "
                       r"b^2-a^2 = 2000\ \text{mm}^2",
                       "Geometrik nisbatlar."),
                    st(r"\sigma_\theta(a) = 60\cdot\frac{3600+1600}{3600-1600} = "
                       r"60\cdot\frac{5200}{2000} = 156\ \text{MPa}",
                       "Ichki sirtdagi halqaviy kuchlanish."),
                    st(r"\sigma_\theta(b) = 60\cdot\frac{2a^2}{b^2-a^2} = "
                       r"60\cdot\frac{3200}{2000} = 96\ \text{MPa}",
                       "Tashqi sirtdagi — 38 % kichik."),
                    st(r"\sigma_r(a) = -60\ \text{MPa};\quad \sigma_r(b) = 0",
                       "Radial kuchlanish chegaraviy shartlardan."),
                    st(r"\text{Yupqa devor: } \sigma = \frac{p_ir_m}{t} = "
                       r"\frac{60\cdot50}{20} = 150\ \text{MPa}",
                       "$r_m = 50$ mm, $t = 20$ mm. Xatolik: "
                       "$(156-150)/156 = 3{,}8$ %."),
                    st(r"\sigma_{Mises}(a) = \sqrt{\tfrac{1}{2}[(156+60)^2+(60)^2+(156)^2]} = "
                       r"\sqrt{\tfrac{1}{2}(46656+3600+24336)} = 193{,}3\ \text{MPa}",
                       "$\\sigma_z = 0$ (ochiq quvur) deb olindi."),
                ],
                answer=(
                    "$\\sigma_\\theta(a) = 156$ MPa, $\\sigma_\\theta(b) = 96$ MPa; "
                    "yupqa devorli formula 150 MPa (3,8 % xatolik); "
                    "$\\sigma_{Mises}(a) = 193{,}3$ MPa."
                ),
                engineering_note=(
                    "$b/a = 1{,}5$ da yupqa devorli formula atigi 3,8 % "
                    "xatolik beradi — u ko'p hollarda yetarli. Lekin "
                    "$b/a = 2$ da xatolik 15 % ga, $b/a = 3$ da 40 % ga "
                    "yetadi. Amaliy qoida: $t/r_m < 0{,}1$ da yupqa devorli "
                    "formula, aks holda Lame yechimi."
                ),
            ),
            computation=Computation(
                caption="Qalin devorli quvur: Lame yechimi va yupqa devorli taqqoslash.",
                code='''"""Tekis masalalar: qalin devorli quvur (Lame yechimi)."""
import numpy as np
from labkit import PARAMS, note, series, table, value

a = float(PARAMS.get("a", 40.0))*1e-3     # ichki radius, m
b = float(PARAMS.get("b", 60.0))*1e-3     # tashqi radius, m
p_i = float(PARAMS.get("p_i", 60.0))*1e6  # ichki bosim, Pa
p_b = float(PARAMS.get("p_b", 0.0))*1e6   # tashqi bosim, Pa
E = float(PARAMS.get("E", 200e9))
nu = float(PARAMS.get("nu", 0.3))

r = np.linspace(a, b, 300)
A_c = (p_i*a**2 - p_b*b**2)/(b**2 - a**2)
B_c = (p_i - p_b)*a**2*b**2/(b**2 - a**2)
sig_r = A_c - B_c/r**2
sig_t = A_c + B_c/r**2

series("σ_r(r)", (r*1000).tolist(), (sig_r/1e6).tolist(), xlabel="r, mm", ylabel="σ_r, MPa")
series("σ_θ(r)", (r*1000).tolist(), (sig_t/1e6).tolist(), xlabel="r, mm", ylabel="σ_θ, MPa")
series("σ_r + σ_θ", (r*1000).tolist(), ((sig_r+sig_t)/1e6).tolist(),
       xlabel="r, mm", ylabel="σ, MPa")

value("σ_θ (ichki sirt)", float(sig_t[0]/1e6), "MPa")
value("σ_θ (tashqi sirt)", float(sig_t[-1]/1e6), "MPa")
value("σ_r (ichki sirt)", float(sig_r[0]/1e6), "MPa")
value("Notekislik σ_θ(a)/σ_θ(b)", float(sig_t[0]/sig_t[-1]), "—")
note(f"σ_r + σ_θ = {(sig_r[0]+sig_t[0])/1e6:.4f} MPa — radiusdan bog'liq emas ✓")

# Yupqa devorli taqqoslash
t_w = b - a
r_m = (a+b)/2
sig_thin = p_i*r_m/t_w
value("σ (yupqa devorli formula)", sig_thin/1e6, "MPa")
value("Xatolik", float(abs(sig_t[0]-sig_thin)/sig_t[0]*100), "%")
value("t/r_m nisbati", t_w/r_m, "—")

# b/a nisbatining ta'siri
ratios = np.linspace(1.05, 4.0, 100)
sig_exact = [p_i*(x**2+1)/(x**2-1)/1e6 for x in ratios]
sig_approx = [p_i*((x+1)/2)/(x-1)/1e6 for x in ratios]
series("σ_θ(a) — aniq (Lame)", ratios.tolist(), sig_exact, xlabel="b/a", ylabel="σ_θ, MPa")
series("σ_θ — yupqa devorli", ratios.tolist(), sig_approx, xlabel="b/a", ylabel="σ_θ, MPa")
err_arr = [abs(e-ap)/e*100 for e, ap in zip(sig_exact, sig_approx)]
series("Yupqa devorli formula xatoligi", ratios.tolist(), err_arr,
       xlabel="b/a", ylabel="Xatolik, %")

# Devor qalinligining samarasi
note(f"b → ∞ da σ_θ(a) → p_i = {p_i/1e6:.1f} MPa — devorni qalinlashtirish "
     "cheksiz foyda bermaydi!")
for br in (1.5, 2.0, 3.0, 5.0, 10.0):
    st_val = p_i*(br**2+1)/(br**2-1)/1e6
    note(f"b/a = {br}: σ_θ(a) = {st_val:.2f} MPa "
         f"({st_val/(p_i/1e6):.2f}·p_i)")

# fon Mizes kuchlanishi
sig_z = 0.0                                    # ochiq quvur
sm = np.sqrt(0.5*((sig_t-sig_r)**2 + (sig_r-sig_z)**2 + (sig_z-sig_t)**2))
series("fon Mizes σ_ekv(r)", (r*1000).tolist(), (sm/1e6).tolist(),
       xlabel="r, mm", ylabel="σ_ekv, MPa")
value("σ_Mises (ichki sirt)", float(sm[0]/1e6), "MPa")

# Tekis kuchlanish va tekis deformatsiya farqi
E_ps, nu_ps = E, nu                                     # tekis kuchlanish
E_pe, nu_pe = E/(1-nu**2), nu/(1-nu)                    # tekis deformatsiya
table("Tekis kuchlanish va tekis deformatsiya",
      ["Holat", "Shart", "E_samarali, GPa", "ν_samarali"],
      [["Tekis kuchlanish", "σ₃₃ = 0", E_ps/1e9, nu_ps],
       ["Tekis deformatsiya", "ε₃₃ = 0", E_pe/1e9, nu_pe]])
note(f"Tekis deformatsiyada σ_zz = ν(σ_r+σ_θ) = {nu*(sig_r[0]+sig_t[0])/1e6:.2f} MPa "
     "— ochiq quvurdan farqli.")
''',
                parameters=[
                    p("a", "Ichki radius a", 5.0, 500.0, 40.0, 1.0, "mm"),
                    p("b", "Tashqi radius b", 6.0, 800.0, 60.0, 1.0, "mm"),
                    p("p_i", "Ichki bosim p_i", 0.0, 500.0, 60.0, 5.0, "MPa"),
                    p("p_b", "Tashqi bosim p_b", 0.0, 200.0, 0.0, 5.0, "MPa"),
                    p("E", "Yung moduli", 1e10, 4e11, 200e9, 1e10, "Pa"),
                    p("nu", "Puasson koeff.", 0.0, 0.49, 0.3, 0.01, "—"),
                ],
                expected_output="σ_θ(a) = 156 MPa, σ_θ(b) = 96 MPa, yupqa devorli xatolik 3,8 %",
            ),
            visual=vis(
                "Quvur kesimida kuchlanish taqsimoti",
                "React/SVG",
                "Quvur kesimi (ikki konsentrik doira); ichkaridan tashqariga "
                "$\\sigma_\\theta$ rangli xarita; yonida $\\sigma_r(r)$ va "
                "$\\sigma_\\theta(r)$ grafiklari.",
                "React/SVG: halqasimon kesimda rangli taqsimot — bosimli "
                "idishlar hisobining standart tasviri. Ichki sirtdagi "
                "maksimumni aniq ko'rsatish muhim.",
            ),
            interp=(
                "$\\sigma_r + \\sigma_\\theta$ o'zgarmasligi Lame "
                "yechimining muhim xossasi va uni tekshirish usuli. "
                "$b/a$ grafigi esa asosiy muhandislik xulosasini beradi: "
                "$b/a > 3$ dan keyin devorni qalinlashtirish deyarli foyda "
                "bermaydi, chunki $\\sigma_\\theta(a)$ $p_i$ ga asimptotik "
                "yaqinlashadi. Juda yuqori bosimlarda avtofretaj yoki "
                "ko'p qatlamli konstruksiya kerak."
            ),
            mistakes=[
                "Qalin devorli quvurda yupqa devorli formulani tekshirmasdan "
                "ishlatish.",
                "Tekis kuchlanish va tekis deformatsiya holatlarini "
                "chalkashtirish.",
                "Ichki bosim ishorasini noto'g'ri qo'yish "
                "($\\sigma_r(a) = -p_i$).",
                "Yopiq quvurda o'q bo'ylab kuchlanishni unutish "
                "($\\sigma_z = p_ia^2/(b^2-a^2)$).",
            ],
            quiz=[
                q("Nima uchun $\\sigma_\\theta$ ichki sirtda maksimal?",
                  "Lame formulasidagi $1/r^2$ hadi ichki radiusda eng "
                  "katta qiymatga ega.", "konseptual"),
                q("Tekis kuchlanish va tekis deformatsiya farqi nima?",
                  "Birinchisida $\\sigma_{33} = 0$ (yupqa plastina), "
                  "ikkinchisida $\\varepsilon_{33} = 0$ (uzun jism).",
                  "konseptual"),
                q("$b/a = 2$, $p_i = 50$ MPa. $\\sigma_\\theta(a)$?",
                  "$\\sigma_\\theta = 50(4+1)/(4-1) = 83{,}3$ MPa.", "hisob"),
                q("Devorni cheksiz qalinlashtirsak, $\\sigma_\\theta(a)$ "
                  "nimaga intiladi?",
                  "$p_i$ ga — ichki bosimdan kam bo'lmaydi. Shuning uchun "
                  "juda yuqori bosimlarda boshqa yechim kerak.", "talqin"),
                q("Kodda $\\sigma_r+\\sigma_\\theta$ nima uchun tekshiriladi?",
                  "Lame yechimida bu yig'indi radiusdan bog'liq emas — "
                  "hisobning to'g'riligini tasdiqlovchi invariant.", "kod"),
            ],
            bridge=(
                "O'qsimmetrik masalani yechdik. Umumiy tekis masalalar "
                "uchun esa maxsus vosita — Eyri kuchlanish funksiyasi kerak."
            ),
            research=(
                "Avtofretaj jarayonini modellashtiring: quvurni yuqori "
                "bosim bilan qisman plastik deformatsiyalash, so'ngra "
                "bosimni olib tashlash. Natijada ichki sirtda qoldiq "
                "siquvchi kuchlanish paydo bo'ladi. Ish bosimida "
                "kuchlanish qanchaga kamayishini hisoblang."
            ),
        ),
    ),
    Topic(
        id="tmm-17",
        subject_id=S, module_id=M, order=17,
        title="Eyri kuchlanish funksiyasi va tekis masalalarning yechimlari",
        description=(
            "Kuchlanish funksiyasi g'oyasi, bigarmonik tenglama, polinomial "
            "yechimlar va Kirsh masalasi."
        ),
        learning_objective=(
            "Eyri funksiyasini qo'llab tekis masalalarni yechish va "
            "konsentratsiya effektini analitik olish."
        ),
        prerequisites=["tmm-16", "mq-29"],
        mathematical_core=(
            "Bigarmonik tenglama $\\nabla^4\\varphi = 0$, polinomial va "
            "trigonometrik yechimlar, silindrik koordinatalar."
        ),
        engineering_application=(
            "Kuchlanish konsentratsiyasi, tirqishli va teshikli elementlar, "
            "kontakt masalalari."
        ),
        computational_component=(
            "Kirsh yechimini hisoblash va bigarmonik tenglamani sonli yechish."
        ),
        visualization_component=(
            "Teshik atrofidagi kuchlanish maydoni; kuchlanish oqimi chiziqlari."
        ),
        research_extension=(
            "Kompleks potensiallar usuli (Muskhelishvili): ixtiyoriy "
            "shakldagi teshik uchun yechim."
        ),
        difficulty="ilg'or",
        previous_link=(
            "mq-29 da $K_t = 3$ natijasini jadvaldan oldik. Endi uni "
            "analitik keltirib chiqaramiz."
        ),
        next_topic="tmm-18",
        estimated_minutes=90,
        tags=["Eyri funksiyasi", "bigarmonik tenglama", "Kirsh masalasi"],
        lesson=_lesson(
            problem=(
                "Teshikli plastinada kuchlanish 3 marta ortadi — bu tajribada "
                "ma'lum. Lekin nima uchun aynan 3? Va boshqa shakldagi "
                "teshiklar uchun qancha? Bu savollarga javob berish uchun "
                "tekis masalani analitik yechish usuli kerak."
            ),
            concepts=[
                c("Eyri kuchlanish funksiyasi", "$\\sigma_{xx} = "
                  "\\partial^2\\varphi/\\partial y^2$, $\\sigma_{yy} = "
                  "\\partial^2\\varphi/\\partial x^2$, $\\sigma_{xy} = "
                  "-\\partial^2\\varphi/\\partial x\\partial y$."),
                c("Muvozanatning avtomatik bajarilishi", "Bunday ta'rifda "
                  "muvozanat tenglamalari aynan qanoatlantiriladi."),
                c("Bigarmonik tenglama", "$\\nabla^4\\varphi = 0$ — moslik "
                  "shartidan kelib chiqadi."),
                c("Polinomial yechimlar", "Past darajali polinomlar sodda "
                  "masalalarni (toza egilish, siljish) beradi."),
                c("Kirsh masalasi", "Teshikli plastinaning aniq yechimi; "
                  "$K_t = 3$ natijasini beradi."),
            ],
            derivation=[
                d("1-qadam. Kuchlanish funksiyasini kiritish",
                  r"\sigma_{xx} = \varphi_{,yy},\quad \sigma_{yy} = \varphi_{,xx},\quad "
                  r"\sigma_{xy} = -\varphi_{,xy}",
                  "Hajmiy kuchlar yo'q deb olamiz. Muvozanat tenglamasi: "
                  "$\\varphi_{,yyx} - \\varphi_{,xyy} = 0$ — aynan bajariladi."),
                d("2-qadam. Moslik shartini qo'llash",
                  r"\varepsilon_{xx,yy}+\varepsilon_{yy,xx} = 2\varepsilon_{xy,xy}",
                  "tmm-05 dagi moslik sharti. Guk qonuni orqali "
                  "kuchlanishlarga o'tkazamiz."),
                d("3-qadam. Bigarmonik tenglama",
                  r"\boxed{\;\nabla^4\varphi = \frac{\partial^4\varphi}{\partial x^4}+"
                  r"2\frac{\partial^4\varphi}{\partial x^2\partial y^2}+"
                  r"\frac{\partial^4\varphi}{\partial y^4} = 0\;}",
                  "Butun tekis masala bitta to'rtinchi tartibli PDE ga "
                  "keldi — bu Eyri usulining asosiy yutug'i."),
                d("4-qadam. Kirsh masalasi uchun yechim",
                  r"\varphi = \frac{\sigma}{4}\left[r^2 - a^2\ln r - \left(r^2 - "
                  r"\frac{2a^2r^2 - a^4}{r^2}\right)\cos2\theta\right]",
                  "Silindrik koordinatalarda; chegaraviy shartlar: teshik "
                  "sirti erkin, cheksizlikda bir o'qli cho'zilish."),
                d("5-qadam. Konsentratsiya koeffitsienti",
                  r"\sigma_\theta(a, \pi/2) = \frac{\sigma}{2}[2+2] = 3\sigma "
                  r"\;\Rightarrow\; K_t = 3",
                  "Teshik chekkasida, yuklanishga perpendikular nuqtada. "
                  "Teshik o'lchamidan bog'liq emas."),
            ],
            meaning=(
                "Eyri funksiyasi tekis masalani 6 ta noma'lumdan bitta "
                "funksiyaga keltiradi va muvozanatni avtomatik "
                "qanoatlantiradi. Bigarmonik tenglama esa klassik "
                "matematik fizikada yaxshi o'rganilgan — shuning uchun "
                "ko'p analitik yechimlar mavjud. Kirsh yechimi ularning eng "
                "mashhuri va u konsentratsiya nazariyasining poydevori."
            ),
            equations=[
                eq(r"\nabla^4\varphi = 0", "Bigarmonik tenglama.", "Bigarmonik tenglama"),
                eq(r"\sigma_\theta = \frac{\sigma}{2}\left[\left(1+\frac{a^2}{r^2}\right)-"
                   r"\left(1+\frac{3a^4}{r^4}\right)\cos2\theta\right]",
                   "Kirsh yechimi (halqaviy kuchlanish).", "Kirsh yechimi"),
                eq(r"K_t = 3", "Dumaloq teshik uchun konsentratsiya koeffitsienti.",
                   "Konsentratsiya"),
            ],
            conditions=(
                "Eyri usuli hajmiy kuchlar bo'lmaganda (yoki ular potensialga "
                "ega bo'lganda) qo'llanadi. Kirsh yechimi cheksiz plastina "
                "uchun; chekli kenglikda tuzatish kerak. Yechim faqat "
                "elastik sohada o'rinli — teshik chekkasida oqish boshlansa, "
                "kuchlanish qayta taqsimlanadi."
            ),
            worked=WorkedExample(
                statement=(
                    "Cheksiz plastina bir o'qli $\\sigma = 100$ MPa bilan "
                    "cho'zilgan, radiusi $a = 10$ mm teshik bor. "
                    "(a) $\\theta = 90°$ va $\\theta = 0$ da teshik "
                    "chekkasidagi kuchlanish; (b) $r = 2a$, $3a$ da "
                    "kuchlanish; (c) ikki o'qli cho'zilishda ($\\sigma_x = "
                    "\\sigma_y = \\sigma$) $K_t$ qancha?"
                ),
                given=[r"\sigma = 100\ \text{MPa},\ a = 10\ \text{mm}"],
                steps=[
                    st(r"r = a,\ \theta = 90^\circ:\ \sigma_\theta = \frac{\sigma}{2}[2-4(-1)] = 3\sigma = "
                       r"300\ \text{MPa}",
                       "$\\cos 180° = -1$; maksimal konsentratsiya."),
                    st(r"r = a,\ \theta = 0:\ \sigma_\theta = \frac{\sigma}{2}[2-4(1)] = -\sigma = "
                       r"-100\ \text{MPa}",
                       "Siquvchi kuchlanish! Bu — Kirsh yechimining "
                       "kutilmagan natijasi."),
                    st(r"r = 2a,\ \theta = 90^\circ:\ \sigma_\theta = \frac{\sigma}{2}\left[(1+0{,}25)+"
                       r"(1+3/16)\right] = \frac{\sigma}{2}(2{,}4375) = 1{,}22\sigma",
                       "$= 122$ MPa — konsentratsiya tez so'nadi."),
                    st(r"r = 3a:\ \sigma_\theta \approx 1{,}07\sigma = 107\ \text{MPa}",
                       "Nominal qiymatdan atigi 7 % katta."),
                    st(r"\text{Ikki o'qli: superpozitsiya } \Rightarrow "
                       r"\sigma_\theta(a) = 3\sigma - \sigma = 2\sigma",
                       "Ikkinchi yo'nalishdagi cho'zilish teshik chekkasida "
                       "$-\\sigma$ beradi."),
                    st(r"K_t^{2-o'qli} = 2",
                       "Ikki o'qli holatda konsentratsiya kamroq — bu "
                       "bosimli idishlardagi teshiklar uchun muhim."),
                ],
                answer=(
                    "$\\sigma_\\theta(a, 90°) = 300$ MPa ($K_t = 3$); "
                    "$\\sigma_\\theta(a, 0) = -100$ MPa (siqilish); "
                    "$r = 3a$ da 107 MPa; ikki o'qli holatda $K_t = 2$."
                ),
                engineering_note=(
                    "Ikki o'qli cho'zilishda $K_t = 2$ — bu bosimli "
                    "idishlardagi lyuk va teshiklar uchun muhim: u yerda "
                    "kuchlanish holati taxminan ikki o'qli "
                    "($\\sigma_\\theta = 2\\sigma_z$), shuning uchun "
                    "konsentratsiya 3 dan kam."
                ),
            ),
            computation=Computation(
                caption="Kirsh yechimi: teshik atrofidagi kuchlanish maydonini hisoblang.",
                code='''"""Eyri kuchlanish funksiyasi va Kirsh masalasi."""
import numpy as np
from labkit import PARAMS, note, series, table, value

sigma = float(PARAMS.get("sigma", 100.0))     # MPa, x bo'ylab
sigma_y = float(PARAMS.get("sigma_y", 0.0))   # MPa, y bo'ylab
a = float(PARAMS.get("a", 10.0))*1e-3         # teshik radiusi, m
r_max = float(PARAMS.get("r_max", 5.0))       # tahlil radiusi (a birligida)

def kirsch(r, theta, s_x, s_y):
    """Kirsh yechimi (ikki o'qli holat, superpozitsiya)."""
    ar2 = (a/r)**2
    ar4 = (a/r)**4
    # x bo'ylab cho'zilish
    sr_x = s_x/2*((1-ar2) + (1 - 4*ar2 + 3*ar4)*np.cos(2*theta))
    st_x = s_x/2*((1+ar2) - (1 + 3*ar4)*np.cos(2*theta))
    srt_x = -s_x/2*(1 + 2*ar2 - 3*ar4)*np.sin(2*theta)
    # y bo'ylab cho'zilish (theta -> theta + 90°)
    th2 = theta + np.pi/2
    sr_y = s_y/2*((1-ar2) + (1 - 4*ar2 + 3*ar4)*np.cos(2*th2))
    st_y = s_y/2*((1+ar2) - (1 + 3*ar4)*np.cos(2*th2))
    srt_y = -s_y/2*(1 + 2*ar2 - 3*ar4)*np.sin(2*th2)
    return sr_x+sr_y, st_x+st_y, srt_x+srt_y

# Teshik chekkasida burchak bo'ylab
th = np.linspace(0, np.pi, 181)
_, st_edge, _ = kirsch(a, th, sigma, sigma_y)
series("σ_θ(θ) teshik chekkasida", np.degrees(th).tolist(), st_edge.tolist(),
       xlabel="θ, deg", ylabel="σ_θ, MPa")
value("σ_θ (θ=90°)", float(st_edge[90]), "MPa")
value("σ_θ (θ=0°)", float(st_edge[0]), "MPa")
value("K_t", float(st_edge[90]/sigma) if sigma != 0 else 0.0, "—")

# Radius bo'ylab so'nish
rr = np.linspace(a, r_max*a, 300)
_, st_r90, _ = kirsch(rr, np.pi/2, sigma, sigma_y)
sr_r90, _, _ = kirsch(rr, np.pi/2, sigma, sigma_y)
series("σ_θ(r), θ=90°", (rr/a).tolist(), st_r90.tolist(), xlabel="r/a", ylabel="σ_θ, MPa")
series("σ_r(r), θ=90°", (rr/a).tolist(), sr_r90.tolist(), xlabel="r/a", ylabel="σ_r, MPa")

rows = []
for k in (1, 1.5, 2, 3, 5):
    _, s_t, _ = kirsch(k*a, np.pi/2, sigma, sigma_y)
    rows.append([float(k), float(s_t), float(s_t/sigma) if sigma else 0.0])
table("Konsentratsiyaning so'nishi", ["r/a", "σ_θ, MPa", "σ_θ/σ"], rows)
note("Konsentratsiya juda lokal: r = 3a da nominal qiymatdan atigi 7 % katta.")

# Chegaraviy shartlarni tekshirish
sr_edge, _, srt_edge = kirsch(a*1.0001, th, sigma, sigma_y)
note(f"Teshik sirtida σ_r = {np.max(np.abs(sr_edge)):.4f} MPa, "
     f"σ_rθ = {np.max(np.abs(srt_edge)):.4f} MPa (nol bo'lishi kerak) ✓")

# Turli yuklanish holatlari
table("Turli yuklanishda K_t",
      ["Yuklanish", "σ_x", "σ_y", "K_t", "Izoh"],
      [["Bir o'qli", 1.0, 0.0, 3.0, "Klassik Kirsh natijasi"],
       ["Ikki o'qli teng", 1.0, 1.0, 2.0, "Bosimli idish (sferik)"],
       ["Ikki o'qli (2:1)", 2.0, 1.0, 2.5, "Silindrik idish"],
       ["Toza siljish", 1.0, -1.0, 4.0, "Eng katta konsentratsiya"]])

# Bigarmonik tenglamani sonli tekshirish (polinomial yechim)
import numpy.polynomial.polynomial as P
note("Polinomial Eyri funksiyasi φ = ax³ + bx²y + cxy² + dy³ har doim "
     "bigarmonik (4-tartibli hosilalar nol). 4-darajali polinomlar uchun "
     "koeffitsientlarga cheklov paydo bo'ladi.")

# Ellips teshik uchun umumlashma
for ab_ratio in (0.5, 1.0, 2.0, 3.0, 5.0):
    Kt_ellipse = 1 + 2*ab_ratio
    note(f"Ellips teshik (a/b = {ab_ratio}): K_t = 1 + 2a/b = {Kt_ellipse:.1f}")
note("a/b → ∞ (yoriq) da K_t → ∞ — bu yoriqlar mexanikasining "
     "boshlang'ich nuqtasi (tmm-24).")
''',
                parameters=[
                    p("sigma", "σ_x (cho'zilish)", -300.0, 300.0, 100.0, 10.0, "MPa"),
                    p("sigma_y", "σ_y (cho'zilish)", -300.0, 300.0, 0.0, 10.0, "MPa"),
                    p("a", "Teshik radiusi a", 1.0, 100.0, 10.0, 1.0, "mm"),
                    p("r_max", "Tahlil radiusi (a birligida)", 2.0, 20.0, 5.0, 0.5, "—"),
                ],
                expected_output="σ_θ(90°) = 300 MPa, K_t = 3; σ_θ(0°) = -100 MPa",
            ),
            visual=vis(
                "Teshik atrofidagi kuchlanish maydoni",
                "React/SVG",
                "Teshikli plastina; $\\sigma_\\theta$ rangli xarita; teshik "
                "chekkasida qizil (konsentratsiya) va ko'k (siqilish) "
                "zonalari. Kuchlanish oqimi chiziqlari teshikni aylanib "
                "o'tadi.",
                "React/SVG: Kirsh yechimi analitik, shuning uchun har bir "
                "nuqtada tez hisoblanadi — rangli xarita SVG to'ri bilan "
                "chizilishi mumkin. Kuchlanish oqimi chiziqlari "
                "konsentratsiyaning fizik sababini tushuntiradi.",
            ),
            interp=(
                "$\\theta = 0$ da siquvchi kuchlanish ($-\\sigma$) paydo "
                "bo'lishi Kirsh yechimining kutilmagan, lekin tajribada "
                "tasdiqlangan natijasi. Turli yuklanish jadvali esa muhim "
                "amaliy xulosani beradi: toza siljishda $K_t = 4$ — eng "
                "xavfli holat. Ellips teshik formulasi $K_t = 1+2a/b$ esa "
                "yoriqlar mexanikasiga ko'prik: $b \\to 0$ da "
                "$K_t \\to \\infty$."
            ),
            mistakes=[
                "Kirsh yechimini chekli kenglikdagi plastinaga tuzatishsiz "
                "qo'llash.",
                "Konsentratsiyani teshik o'lchamiga bog'liq deb o'ylash.",
                "$\\theta = 0$ dagi siquvchi kuchlanishni e'tiborsiz "
                "qoldirish (siklik yuklanishda u muhim).",
                "Eyri funksiyasini hajmiy kuchlar mavjud bo'lganda "
                "o'zgartirishsiz ishlatish.",
            ],
            quiz=[
                q("Nima uchun Eyri funksiyasi muvozanatni avtomatik "
                  "qanoatlantiradi?",
                  "Kuchlanishlar ikkinchi hosilalar orqali ta'riflangani "
                  "uchun muvozanat tenglamalari aralash hosilalar "
                  "tengligiga keladi va aynan bajariladi.", "konseptual"),
                q("Bigarmonik tenglama qayerdan kelib chiqadi?",
                  "Moslik shartidan: deformatsiyalar uzluksiz ko'chishdan "
                  "kelib chiqishi kerak.", "konseptual"),
                q("Ikki o'qli teng cho'zilishda $K_t$ qancha?",
                  "2 — superpozitsiya bo'yicha $3\\sigma - \\sigma = 2\\sigma$.",
                  "hisob"),
                q("Ellips teshik ($a/b = 4$) uchun $K_t$?",
                  "$K_t = 1+2\\cdot4 = 9$.", "hisob"),
                q("Kodda chegaraviy shartlar qanday tekshirilgan?",
                  "Teshik sirtida $\\sigma_r$ va $\\sigma_{r\\theta}$ nolga "
                  "tengligini ko'rsatish orqali — bu yechimning to'g'riligini "
                  "tasdiqlaydi.", "kod"),
            ],
            bridge=(
                "Tekis masalalarni yechdik. Endi uch o'lchovli klassik "
                "masalaga — Sen-Venan buralishiga o'tamiz."
            ),
            research=(
                "Muskhelishvili kompleks potensiallar usulini o'rganing: "
                "$\\varphi(z)$ va $\\psi(z)$ analitik funksiyalari orqali "
                "tekis masala yechiladi. Konform akslantirish yordamida "
                "ixtiyoriy shakldagi teshik uchun yechim olish mumkin. "
                "Kvadrat teshik uchun $K_t$ ni hisoblang."
            ),
        ),
    ),
    Topic(
        id="tmm-18",
        subject_id=S, module_id=M, order=18,
        title="Sen-Venan buralish masalasi va membrana analogiyasi",
        description=(
            "Dumaloq bo'lmagan kesimlarning buralishi, deplanatsiya, "
            "buralish funksiyasi va Prandtl membrana analogiyasi."
        ),
        learning_objective=(
            "Ixtiyoriy kesimning buralish bikrligini aniqlash va membrana "
            "analogiyasini qo'llash."
        ),
        prerequisites=["tmm-17", "mq-10"],
        mathematical_core=(
            "Puasson tenglamasi $\\nabla^2\\Psi = -2G\\theta$, buralish "
            "funksiyasi, membrana analogiyasi."
        ),
        engineering_application=(
            "To'rtburchak va profil kesimli vallar, yupqa devorli profillar, "
            "aviatsiya konstruksiyalari."
        ),
        computational_component=(
            "Puasson tenglamasini chekli ayirmalar bilan yechib, buralish "
            "bikrligini hisoblash."
        ),
        visualization_component=(
            "Prandtl funksiyasining sath chiziqlari; membrana analogiyasi."
        ),
        research_extension=(
            "Yupqa devorli yopiq va ochiq profillarning buralish bikrligi "
            "nima uchun 100 marta farq qiladi?"
        ),
        difficulty="ilg'or",
        previous_link=(
            "mq-10 da dumaloq val uchun aniq yechim oldik. Dumaloq bo'lmagan "
            "kesimda tekis kesimlar gipotezasi buziladi — endi uni to'g'ri "
            "hal qilamiz."
        ),
        next_topic="tmm-19",
        estimated_minutes=85,
        tags=["Sen-Venan buralishi", "deplanatsiya", "membrana analogiyasi"],
        lesson=_lesson(
            problem=(
                "To'rtburchak kesimli valni buraganimizda uning kesimlari "
                "tekis qolmaydi — ular 'qiyshayadi' (deplanatsiya). Shuning "
                "uchun $\\tau = T\\rho/I_p$ formulasi ishlamaydi. Bunday "
                "kesimlar uchun bikrlik va kuchlanishni qanday hisoblash mumkin?"
            ),
            concepts=[
                c("Deplanatsiya", "Kesimning o'z tekisligidan chiqishi; "
                  "dumaloq kesimda yo'q, boshqa barcha kesimlarda bor."),
                c("Buralish funksiyasi", "$u_z = \\theta\\psi(x,y)$ — "
                  "deplanatsiyani tavsiflovchi funksiya."),
                c("Prandtl kuchlanish funksiyasi", "$\\tau_{zx} = "
                  "\\partial\\Psi/\\partial y$, $\\tau_{zy} = "
                  "-\\partial\\Psi/\\partial x$."),
                c("Puasson tenglamasi", "$\\nabla^2\\Psi = -2G\\theta$ — "
                  "buralish masalasining asosiy tenglamasi."),
                c("Membrana analogiyasi", "Prandtl funksiyasi bosim ostidagi "
                  "membrana cho'kishiga o'xshaydi — bu intuitiv baholash "
                  "imkonini beradi."),
            ],
            derivation=[
                d("1-qadam. Sen-Venan gipotezasi",
                  r"u_x = -\theta zy,\quad u_y = \theta zx,\quad u_z = \theta\psi(x,y)",
                  "Kesim burilади va deplanatsiyalanadi, lekin shakli "
                  "o'zgarmaydi."),
                d("2-qadam. Kuchlanishlar",
                  r"\tau_{zx} = G\theta\left(\frac{\partial\psi}{\partial x}-y\right),\quad "
                  r"\tau_{zy} = G\theta\left(\frac{\partial\psi}{\partial y}+x\right)",
                  "Kinematikadan va Guk qonunidan. Qolgan kuchlanishlar nolga teng."),
                d("3-qadam. Prandtl funksiyasini kiritish",
                  r"\tau_{zx} = \frac{\partial\Psi}{\partial y},\quad "
                  r"\tau_{zy} = -\frac{\partial\Psi}{\partial x} \Rightarrow "
                  r"\boxed{\;\nabla^2\Psi = -2G\theta\;}",
                  "Muvozanat avtomatik bajariladi; moslik sharti Puasson "
                  "tenglamasini beradi."),
                d("4-qadam. Chegaraviy shart va moment",
                  r"\Psi = 0\ \text{konturda};\qquad T = 2\int_A\Psi\,dA",
                  "Kontur erkin (kuchlanishsiz). Buruvchi moment — "
                  "$\\Psi$ ostidagi hajmning ikki barobari."),
                d("5-qadam. Membrana analogiyasi",
                  r"\nabla^2 w = -\frac{p}{S} \quad\longleftrightarrow\quad \nabla^2\Psi = -2G\theta",
                  "Bir xil tenglama: $\\Psi \\leftrightarrow w$ (membrana "
                  "cho'kishi), $2G\\theta \\leftrightarrow p/S$. Demak "
                  "membrananing shakli kuchlanish taqsimotini beradi: "
                  "eng tik qiyalik — eng katta kuchlanish."),
            ],
            meaning=(
                "Membrana analogiyasi muhandislik intuitsiyasi uchun "
                "ajoyib vosita: kesim shaklini tasavvur qilib, ustiga "
                "membrana tortilgan va bosim berilgan deb o'ylash kifoya. "
                "Membrana eng ko'p ko'tarilgan joy — eng katta $\\Psi$, "
                "eng tik qiyalik — eng katta kuchlanish. Bu darhol "
                "tushuntiradi: nima uchun o'tkir burchaklarda kuchlanish "
                "nolga teng (membrana u yerda tekis) va nima uchun yupqa "
                "ochiq profil buralishga juda zaif (membrana ko'tarila olmaydi)."
            ),
            equations=[
                eq(r"\nabla^2\Psi = -2G\theta", "Buralish masalasining asosiy tenglamasi.",
                   "Puasson tenglamasi"),
                eq(r"T = 2\int_A\Psi\,dA", "Buruvchi moment.", "Moment"),
                eq(r"I_t = \beta\,b\,h^3", "To'rtburchak kesim uchun buralish "
                   "inersiya momenti ($\\beta$ — jadval koeffitsienti).",
                   "To'rtburchak kesim"),
            ],
            conditions=(
                "Sen-Venan yechimi erkin deplanatsiya sharti bilan o'rinli. "
                "Agar deplanatsiya cheklangan bo'lsa (masalan, uchi "
                "qotirilgan profil), qo'shimcha normal kuchlanishlar paydo "
                "bo'ladi — bu cheklangan buralish (Vlasov nazariyasi)."
            ),
            worked=WorkedExample(
                statement=(
                    "To'rtburchak kesimli val: $b = 60$ mm, $h = 30$ mm, "
                    "$G = 80$ GPa, $T = 500$ N·m. (a) Buralish bikrligi va "
                    "burilish burchagini toping ($L = 1$ m); (b) maksimal "
                    "kuchlanish qayerda va qancha; (c) bir xil yuzali "
                    "dumaloq val bilan taqqoslang."
                ),
                given=[r"b = 60\ \text{mm},\ h = 30\ \text{mm},\ G = 80\ \text{GPa},\ T = 500\ \text{N·m}"],
                steps=[
                    st(r"\frac{b}{h} = 2 \Rightarrow \beta = 0{,}229,\ \alpha = 0{,}246\ "
                       r"(\text{jadvaldan})",
                       "To'rtburchak kesim koeffitsientlari."),
                    st(r"I_t = \beta bh^3 = 0{,}229\cdot60\cdot27\,000 = 371\,000\ \text{mm}^4",
                       "Buralish inersiya momenti."),
                    st(r"\theta = \frac{T}{GI_t} = \frac{500}{80\cdot10^9\cdot3{,}71\cdot10^{-7}} = "
                       r"0{,}01685\ \text{rad/m} = 0{,}966\ \text{deg/m}",
                       "Nisbiy burilish burchagi."),
                    st(r"\tau_{max} = \frac{T}{\alpha bh^2} = \frac{500}{0{,}246\cdot0{,}06\cdot0{,}0009} = "
                       r"37{,}6\ \text{MPa}",
                       "Maksimal kuchlanish — uzun tomonning o'rtasida "
                       "(membrana analogiyasi: eng tik qiyalik)."),
                    st(r"\text{Dumaloq, teng yuza: } A = 1800\ \text{mm}^2 \Rightarrow "
                       r"d = 47{,}9\ \text{mm};\ I_p = 517\,000\ \text{mm}^4",
                       "Bir xil material sarfi bilan."),
                    st(r"\frac{I_t}{I_p} = \frac{371}{517} = 0{,}72",
                       "To'rtburchak kesim dumaloqdan 28 % zaifroq — "
                       "buralishda dumaloq kesim optimal."),
                ],
                answer=(
                    "$I_t = 371\\,000$ mm⁴; $\\theta = 0{,}966$ deg/m; "
                    "$\\tau_{max} = 37{,}6$ MPa (uzun tomon o'rtasida); "
                    "dumaloq kesimdan 28 % zaifroq."
                ),
                engineering_note=(
                    "Burchaklardagi kuchlanish nolga teng — bu membrana "
                    "analogiyasidan darhol ko'rinadi. Shuning uchun "
                    "buralishda ishlaydigan detallarda o'tkir burchaklar "
                    "kuchlanish nuqtai nazaridan xavfli emas (egilishdan "
                    "farqli)."
                ),
            ),
            computation=Computation(
                caption="Buralish masalasi: Puasson tenglamasini sonli yeching.",
                code='''"""Sen-Venan buralishi: Prandtl funksiyasi va membrana analogiyasi."""
import numpy as np
from labkit import PARAMS, note, series, table, value

b = float(PARAMS.get("b", 60.0))*1e-3     # kesim eni, m
h = float(PARAMS.get("h", 30.0))*1e-3     # kesim balandligi, m
G = float(PARAMS.get("G", 80e9))          # Pa
T = float(PARAMS.get("T", 500.0))         # N*m
n = int(PARAMS.get("n", 60))              # to'r zichligi

# Puasson tenglamasini chekli ayirmalar bilan yechish: ∇²Ψ = -2Gθ, Ψ=0 konturda
# Birlik θ = 1 uchun yechamiz, keyin masshtablaymiz
nx, ny = n, max(int(n*h/b), 10)
dx, dy = b/(nx-1), h/(ny-1)
N = (nx-2)*(ny-2)
A = np.zeros((N, N)); rhs = np.full(N, -2*G*1.0)

def idx(i, j):
    return (j-1)*(nx-2) + (i-1)

for j in range(1, ny-1):
    for i in range(1, nx-1):
        k = idx(i, j)
        A[k, k] = -2/dx**2 - 2/dy**2
        if i > 1:
            A[k, idx(i-1, j)] = 1/dx**2
        if i < nx-2:
            A[k, idx(i+1, j)] = 1/dx**2
        if j > 1:
            A[k, idx(i, j-1)] = 1/dy**2
        if j < ny-2:
            A[k, idx(i, j+1)] = 1/dy**2

psi_int = np.linalg.solve(A, rhs)
Psi = np.zeros((ny, nx))
for j in range(1, ny-1):
    for i in range(1, nx-1):
        Psi[j, i] = psi_int[idx(i, j)]

# Buralish inersiya momenti: T = 2∫Ψ dA (θ=1 uchun)
It_num = 2*np.sum(Psi)*dx*dy/G
value("I_t (sonli)", It_num*1e12, "mm⁴")

# Analitik (jadval) qiymat
ratio = b/h
beta_tab = {1.0: 0.141, 1.5: 0.196, 2.0: 0.229, 3.0: 0.263, 4.0: 0.281,
            6.0: 0.299, 10.0: 0.312}
keys = sorted(beta_tab)
beta = np.interp(ratio, keys, [beta_tab[k] for k in keys])
alpha = np.interp(ratio, keys, [0.208, 0.231, 0.246, 0.267, 0.282, 0.299, 0.312])
It_tab = beta*b*h**3
value("I_t (jadval)", It_tab*1e12, "mm⁴")
value("Farq", float(abs(It_num-It_tab)/It_tab*100), "%")

theta = T/(G*It_tab)
value("Nisbiy burilish θ", np.degrees(theta), "deg/m")
tau_max = T/(alpha*b*h**2)
value("τ_max", tau_max/1e6, "MPa")

# Prandtl funksiyasi profillari (membrana shakli)
Psi_scaled = Psi*theta
mid_j = ny//2
series("Ψ(x) — o'rta kesim", (np.linspace(0, b, nx)*1000).tolist(),
       (Psi_scaled[mid_j, :]/1e6).tolist(), xlabel="x, mm", ylabel="Ψ, MPa·m")
mid_i = nx//2
series("Ψ(y) — o'rta kesim", (np.linspace(0, h, ny)*1000).tolist(),
       (Psi_scaled[:, mid_i]/1e6).tolist(), xlabel="y, mm", ylabel="Ψ, MPa·m")

# Kuchlanish: τ = |∇Ψ|
tau_x = np.gradient(Psi_scaled, dy, axis=0)
tau_y = -np.gradient(Psi_scaled, dx, axis=1)
tau_mag = np.hypot(tau_x, tau_y)
value("τ_max (sonli)", float(np.max(tau_mag))/1e6, "MPa")
note("Maksimal kuchlanish uzun tomonning o'rtasida — membrana analogiyasi "
     "bo'yicha u yerda qiyalik eng tik.")
note(f"Burchaklardagi kuchlanish: {tau_mag[1, 1]/1e6:.3f} MPa (nolga yaqin) ✓")

# Dumaloq kesim bilan taqqoslash (teng yuza)
A_rect = b*h
d_eq = np.sqrt(4*A_rect/np.pi)
Ip_circ = np.pi*d_eq**4/32
table("Kesimlarni taqqoslash (teng yuza)",
      ["Kesim", "I_t, mm⁴", "Nisbat", "τ_max, MPa"],
      [["To'rtburchak", float(It_tab*1e12), 1.0, float(tau_max/1e6)],
       ["Dumaloq", float(Ip_circ*1e12), float(Ip_circ/It_tab),
        float(T/(np.pi*d_eq**3/16)/1e6)]])

# Yupqa devorli profillar
t_thin = 0.005
b_thin = 0.2
It_open = b_thin*t_thin**3/3
A_closed = b_thin*b_thin
It_closed = 4*A_closed**2*t_thin/(4*b_thin)
note(f"Yupqa ochiq profil: I_t = {It_open*1e12:.1f} mm⁴; "
     f"yopiq profil: I_t = {It_closed*1e12:.1f} mm⁴ — "
     f"{It_closed/It_open:.0f} marta katta!")
note("Shuning uchun buralishga ishlaydigan konstruksiyalarda yopiq "
     "(quti) profillar ishlatiladi.")
''',
                parameters=[
                    p("b", "Kesim eni b", 10.0, 300.0, 60.0, 5.0, "mm"),
                    p("h", "Kesim balandligi h", 5.0, 300.0, 30.0, 5.0, "mm"),
                    p("G", "Siljish moduli G", 2e10, 1.2e11, 80e9, 5e9, "Pa"),
                    p("T", "Buruvchi moment T", 10.0, 10000.0, 500.0, 50.0, "N·m"),
                    p("n", "To'r zichligi", 20.0, 100.0, 60.0, 5.0, "dona"),
                ],
                expected_output="I_t ≈ 371 000 mm⁴, θ ≈ 0,97 deg/m, τ_max ≈ 37,6 MPa",
            ),
            visual=vis(
                "Prandtl funksiyasi va membrana analogiyasi",
                "Manim",
                "Kesim konturi ustiga tortilgan membrana; bosim ostida u "
                "ko'tariladi. Sath chiziqlari kuchlanish yo'nalishini, "
                "qiyalik esa kattaligini beradi.",
                "Manim: membrananing 3D shaklini ko'rsatish analogiyani "
                "to'liq ochib beradi. React/SVG da esa sath chiziqlari "
                "(kontur grafigi) va kuchlanish vektorlari beriladi.",
            ),
            interp=(
                "Sonli yechim jadval qiymatlari bilan mos keladi. Membrana "
                "analogiyasi natijalarni tushuntiradi: burchaklarda "
                "kuchlanish nol (membrana tekis), uzun tomon o'rtasida "
                "maksimal (eng tik qiyalik). Ochiq va yopiq profil "
                "taqqoslashi esa eng muhim amaliy xulosani beradi: yopiq "
                "profil buralishga yuzlab marta bikrroq."
            ),
            mistakes=[
                "Dumaloq bo'lmagan kesimga $I_p$ ni ishlatish — "
                "$I_t \\neq I_p$.",
                "Maksimal kuchlanishni burchakda deb o'ylash — u uzun "
                "tomon o'rtasida.",
                "Ochiq va yopiq yupqa devorli profillarni bir xil deb "
                "hisoblash.",
                "Cheklangan deplanatsiya holatida Sen-Venan yechimini "
                "qo'llash.",
            ],
            quiz=[
                q("Nima uchun dumaloq kesimda deplanatsiya yo'q?",
                  "Simmetriya tufayli: buralish funksiyasi "
                  "$\\psi = \\text{const}$ va kesim tekis qoladi.",
                  "konseptual"),
                q("Membrana analogiyasida kuchlanish nimaga mos keladi?",
                  "Membrana sirtining qiyaligiga: $\\tau = |\\nabla\\Psi|$.",
                  "konseptual"),
                q("To'rtburchak kesim ($b/h = 2$) uchun $I_t = \\beta bh^3$, "
                  "$\\beta = 0{,}229$. $b = 40$, $h = 20$ mm. $I_t$?",
                  "$I_t = 0{,}229\\cdot40\\cdot8000 = 73\\,280$ mm⁴.", "hisob"),
                q("Nima uchun yopiq profil ochiqdan ko'p marta bikrroq?",
                  "Yopiq profilda kuchlanish oqimi kontur bo'ylab "
                  "aylanadi (Bredt formulasi), ochiqda esa devor "
                  "qalinligi bo'ylab almashadi va samarasiz.", "talqin"),
                q("Kodda burchaklardagi kuchlanish nima uchun nolga yaqin?",
                  "Membrana analogiyasi bo'yicha burchakda membrana "
                  "deyarli tekis — qiyalik nolga teng.", "kod"),
            ],
            bridge=(
                "Klassik masalalarni yechdik. Endi elastiklik nazariyasining "
                "energetik formulirovkasiga o'tamiz — u sonli usullarning "
                "asosi bo'ladi."
            ),
            research=(
                "Yupqa devorli yopiq profil uchun Bredt formulasini "
                "keltirib chiqaring: $\\tau = T/(2A_m t)$, "
                "$I_t = 4A_m^2/\\oint(ds/t)$. Ochiq va yopiq profillarning "
                "bikrligini bir xil material sarfida taqqoslang va nisbatni "
                "$b/t$ orqali ifodalang."
            ),
        ),
    ),
    Topic(
        id="tmm-19",
        subject_id=S, module_id=M, order=19,
        title="Variatsion prinsiplar: mumkin bo'lgan ko'chishlar va minimal energiya",
        description=(
            "Virtual ishlar prinsipining kontinuumga umumlashmasi, minimal "
            "potensial energiya prinsipi, Lagranj va Kastilyano prinsiplari."
        ),
        learning_objective=(
            "Elastiklik masalasining variatsion formulirovkasini yozish va "
            "uning differensial formulirovka bilan ekvivalentligini ko'rsatish."
        ),
        prerequisites=["tmm-15", "mq-24", "nm-20"],
        mathematical_core=(
            "Funksional, variatsiya, Eyler–Lagranj tenglamalari, zaif shakl, "
            "minimal energiya prinsipi."
        ),
        engineering_application=(
            "Ritz usuli, chekli elementlar usuli — butun hisoblash "
            "mexanikasining nazariy asosi."
        ),
        computational_component=(
            "Ritz usuli bilan taqribiy yechim qurish va aniq yechim bilan "
            "taqqoslash."
        ),
        visualization_component=(
            "Potensial energiya funksionali va uning minimumi; taqribiy "
            "yechimlarning yaqinlashishi."
        ),
        research_extension=(
            "Aralash (Hellinger–Reissner) variatsion prinsiplari: nima uchun "
            "ular ba'zi FEM formulirovkalarida afzal?"
        ),
        difficulty="ilg'or",
        previous_link=(
            "nm-20 dagi virtual ishlar prinsipi va mq-24 dagi Kastilyano "
            "teoremasi endi kontinuumga umumlashtiriladi va su-13, su-18 "
            "uchun to'g'ridan-to'g'ri asos bo'ladi."
        ),
        next_topic="tmm-20",
        estimated_minutes=95,
        tags=["variatsion prinsip", "zaif shakl", "Ritz usuli"],
        lesson=_lesson(
            problem=(
                "Navye tenglamalarini murakkab sohada analitik yechib "
                "bo'lmaydi. Lekin boshqa yo'l bor: to'g'ri yechim potensial "
                "energiyani minimallashtiradi. Demak energiyani taqribiy "
                "funksiyalar orasidan minimallashtirib, yaxshi yaqinlashish "
                "olish mumkin. Bu — butun hisoblash mexanikasining g'oyasi."
            ),
            concepts=[
                c("Mumkin bo'lgan ko'chishlar", "Chegaraviy shartlarni "
                  "qanoatlantiruvchi va uzluksiz ixtiyoriy ko'chish maydoni."),
                c("Virtual ishlar prinsipi", "$\\int_V\\sigma_{ij}\\delta\\varepsilon_{ij}dV = "
                  "\\int_V\\rho b_i\\delta u_idV + \\int_{S_t}\\bar t_i\\delta u_idS$."),
                c("To'la potensial energiya", "$\\Pi = U - W$; $U$ — "
                  "deformatsiya energiyasi, $W$ — tashqi kuchlar ishi."),
                c("Minimal potensial energiya prinsipi", "Haqiqiy ko'chish "
                  "maydoni $\\Pi$ ni minimallashtiradi."),
                c("Zaif (variatsion) shakl", "Differensial tenglamaning "
                  "integral ekvivalenti; FEM shundan quriladi."),
            ],
            derivation=[
                d("1-qadam. Virtual ishlar prinsipi",
                  r"\int_V\sigma_{ij}\delta\varepsilon_{ij}\,dV = "
                  r"\int_V\rho b_i\delta u_i\,dV + \int_{S_t}\bar t_i\delta u_i\,dS",
                  "Muvozanat tenglamalarini $\\delta u_i$ ga ko'paytirib "
                  "integrallash va bo'laklab integrallash orqali olinadi."),
                d("2-qadam. To'la potensial energiya",
                  r"\Pi[\mathbf{u}] = \underbrace{\tfrac{1}{2}\int_VC_{ijkl}\varepsilon_{ij}\varepsilon_{kl}dV}_{U} - "
                  r"\underbrace{\int_V\rho b_iu_idV - \int_{S_t}\bar t_iu_idS}_{W}",
                  "Elastik materialda virtual ish funksional variatsiyasiga "
                  "aylanadi."),
                d("3-qadam. Minimal energiya prinsipi",
                  r"\delta\Pi = 0 \iff \text{muvozanat tenglamalari va kuch chegaraviy shartlari}",
                  "Variatsiyani nolga tenglashtirish Eyler–Lagranj "
                  "tenglamalarini beradi — ular aynan Navye tenglamalari."),
                d("4-qadam. Minimum ekanini isbotlash",
                  r"\Pi[\mathbf{u}+\delta\mathbf{u}] - \Pi[\mathbf{u}] = "
                  r"\tfrac{1}{2}\int_VC_{ijkl}\delta\varepsilon_{ij}\delta\varepsilon_{kl}dV > 0",
                  "$C_{ijkl}$ musbat aniqlangani uchun ikkinchi variatsiya "
                  "musbat — demak bu haqiqiy minimum."),
                d("5-qadam. Ritz usuli",
                  r"\mathbf{u} \approx \sum_ia_i\boldsymbol{\varphi}_i \Rightarrow "
                  r"\frac{\partial\Pi}{\partial a_i} = 0 \Rightarrow [K]\{a\} = \{F\}",
                  "Cheksiz o'lchovli minimallashtirish chekli o'lchovliga "
                  "keltiriladi. FEM — bu Ritz usuli, bunda "
                  "$\\boldsymbol{\\varphi}_i$ bo'lakli funksiyalar."),
            ],
            meaning=(
                "Variatsion prinsip differensial tenglamani ekvivalent "
                "minimallashtirish masalasiga aylantiradi. Bu uch katta "
                "afzallik beradi: (1) taqribiy yechim qurish tabiiy "
                "bo'ladi; (2) chegaraviy shartlarning bir qismi avtomatik "
                "bajariladi (tabiiy shartlar); (3) hosil bo'lgan matritsa "
                "simmetrik va musbat aniqlangan. Aynan shu sabab FEM "
                "variatsion asosga qurilgan."
            ),
            equations=[
                eq(r"\delta\Pi = 0", "Minimal potensial energiya prinsipi.",
                   "Variatsion prinsip"),
                eq(r"\Pi = \tfrac{1}{2}\int_V\sigma_{ij}\varepsilon_{ij}dV - \int_V\rho b_iu_idV - "
                   r"\int_{S_t}\bar t_iu_idS", "To'la potensial energiya.", "Funksional"),
                eq(r"[K]\{a\} = \{F\}", "Ritz usuli natijasi.", "Ritz tizimi"),
            ],
            conditions=(
                "Sinov funksiyalari geometrik (muhim) chegaraviy shartlarni "
                "qanoatlantirishi shart; kuch (tabiiy) shartlari esa "
                "avtomatik bajariladi. Funksiyalar to'la sistema tashkil "
                "qilishi kerak — aks holda yechim aniq yechimga "
                "yaqinlashmaydi."
            ),
            worked=WorkedExample(
                statement=(
                    "Konsol balka ($L$, $EI$, uchida $F$) uchun Ritz usuli "
                    "bilan taqribiy yechim quring: (a) bitta had "
                    "$w = a_1x^2$; (b) ikki had $w = a_1x^2 + a_2x^3$. "
                    "Aniq yechim $w_{max} = FL^3/(3EI)$ bilan taqqoslang."
                ),
                given=[r"w(0) = 0,\ w'(0) = 0\ (\text{geometrik shartlar})"],
                steps=[
                    st(r"\Pi = \frac{EI}{2}\int_0^L(w'')^2dx - Fw(L)",
                       "Konsol balka uchun to'la potensial energiya."),
                    st(r"w = a_1x^2:\ w'' = 2a_1 \Rightarrow "
                       r"\Pi = \frac{EI}{2}\cdot4a_1^2L - Fa_1L^2",
                       "Bitta hadli approksimatsiya."),
                    st(r"\frac{d\Pi}{da_1} = 4EIa_1L - FL^2 = 0 \Rightarrow "
                       r"a_1 = \frac{FL}{4EI};\quad w(L) = \frac{FL^3}{4EI}",
                       "Xatolik: $(1/3 - 1/4)/(1/3) = 25$ %."),
                    st(r"w = a_1x^2+a_2x^3:\ w'' = 2a_1+6a_2x",
                       "Ikki hadli approksimatsiya."),
                    st(r"\Pi = \frac{EI}{2}\int_0^L(2a_1+6a_2x)^2dx - F(a_1L^2+a_2L^3)",
                       "$= EI(2a_1^2L + 6a_1a_2L^2 + 6a_2^2L^3) - "
                       "F(a_1L^2+a_2L^3)$."),
                    st(r"\frac{\partial\Pi}{\partial a_1} = 0,\ \frac{\partial\Pi}{\partial a_2} = 0 "
                       r"\Rightarrow a_1 = \frac{FL}{2EI},\ a_2 = -\frac{F}{6EI}",
                       "$w(L) = FL^3/(2EI) - FL^3/(6EI) = FL^3/(3EI)$ — "
                       "AYNAN aniq yechim!"),
                ],
                answer=(
                    "Bitta had: $w(L) = FL^3/(4EI)$ (25 % xatolik); "
                    "ikki had: $w(L) = FL^3/(3EI)$ — aniq yechim."
                ),
                engineering_note=(
                    "Ikki hadli approksimatsiya aniq yechimni berdi, chunki "
                    "konsol balkaning aniq yechimi kubik polinom. Bu — Ritz "
                    "usulining muhim xossasi: agar sinov funksiyalari aniq "
                    "yechimni o'z ichiga olsa, usul uni topadi. FEM da ham "
                    "shunday: chiziqli element chiziqli yechimni aniq beradi."
                ),
            ),
            computation=Computation(
                caption="Ritz usuli: taqribiy yechimlarning aniq yechimga yaqinlashishi.",
                code='''"""Variatsion prinsiplar va Ritz usuli."""
import numpy as np
import sympy as sp
from labkit import PARAMS, note, series, table, value

L = float(PARAMS.get("L", 2.0))
EI = float(PARAMS.get("EI", 1e6))
F = float(PARAMS.get("F", 1000.0))
q = float(PARAMS.get("q", 0.0))          # taqsimlangan yuklama
n_terms = int(PARAMS.get("n_terms", 3))

x, Ls = sp.symbols("x L", positive=True)
w_exact_expr = F*x**2*(3*Ls - x)/(6*EI) + q*x**2*(6*Ls**2 - 4*Ls*x + x**2)/(24*EI)
w_exact = sp.lambdify(x, w_exact_expr.subs(Ls, L), "numpy")
w_tip_exact = float(w_exact_expr.subs({x: L, Ls: L}))
value("Aniq yechim w(L)", w_tip_exact*1000, "mm")

# Ritz usuli: w = sum a_i x^(i+1), i = 1..n  (geometrik shartlar w(0)=w'(0)=0)
results = []
for n in range(1, n_terms+1):
    a = sp.symbols(f"a1:{n+1}")
    w_trial = sum(a[i]*x**(i+2) for i in range(n))
    w2 = sp.diff(w_trial, x, 2)
    Pi = EI/2*sp.integrate(w2**2, (x, 0, L)) - F*w_trial.subs(x, L) \
         - q*sp.integrate(w_trial, (x, 0, L))
    eqs = [sp.diff(Pi, ai) for ai in a]
    sol = sp.solve(eqs, a, dict=True)[0]
    w_ritz = w_trial.subs(sol)
    w_tip = float(w_ritz.subs(x, L))
    err = abs(w_tip - w_tip_exact)/abs(w_tip_exact)*100
    results.append([n, float(w_tip*1000), float(err)])
    xs = np.linspace(0, L, 100)
    f_ritz = sp.lambdify(x, w_ritz, "numpy")
    series(f"Ritz, {n} had", xs.tolist(), (np.asarray(f_ritz(xs), dtype=float)*1000).tolist(),
           xlabel="x, m", ylabel="w, mm")

xs = np.linspace(0, L, 100)
series("Aniq yechim", xs.tolist(), (np.asarray(w_exact(xs), dtype=float)*1000).tolist(),
       xlabel="x, m", ylabel="w, mm")

table("Ritz usulining yaqinlashishi",
      ["Hadlar soni", "w(L), mm", "Xatolik, %"], results)
note("Ikki had kifoya: konsol balkaning aniq yechimi kubik polinom, "
     "shuning uchun x² va x³ hadlari uni to'liq ifodalaydi.")

# Potensial energiya funksionali
a1_range = np.linspace(0, 2*F*L/(2*EI), 100)
Pi_vals = [EI/2*4*aa**2*L - F*aa*L**2 for aa in a1_range]
series("Π(a₁) — bitta hadli approksimatsiya", a1_range.tolist(), Pi_vals,
       xlabel="a₁", ylabel="Π, J")
a1_opt = F*L/(4*EI)
value("Optimal a₁", a1_opt, "1/m")
value("Π minimal qiymati", float(EI/2*4*a1_opt**2*L - F*a1_opt*L**2), "J")
note("Funksional aniq minimumga ega — bu minimal potensial energiya "
     "prinsipining sonli tasdig'i.")

# Energiya balansi
U_exact = F**2*L**3/(6*EI)
W_exact = F*w_tip_exact
note(f"Deformatsiya energiyasi U = {U_exact:.6f} J; tashqi ish W = {W_exact:.6f} J; "
     f"U = W/2 ✓ (Klapeyron teoremasi)")
value("Π (aniq yechimda)", float(U_exact - W_exact), "J")

table("Variatsion prinsiplar",
      ["Prinsip", "Funksional", "Noma'lum", "Chegaraviy shart"],
      [["Lagranj (minimal Π)", "Π = U - W", "Ko'chishlar", "Geometrik"],
       ["Kastilyano (minimal Π*)", "Π* = U* - W*", "Kuchlanishlar", "Statik"],
       ["Hellinger–Reissner", "Aralash", "u va σ", "Ikkalasi"],
       ["Hu–Washizu", "Uch maydonli", "u, σ, ε", "Barchasi"]])
note("FEM ning standart formulirovkasi Lagranj prinsipiga asoslangan; "
     "aralash prinsiplar siqilmaydigan materiallar uchun afzal (su-22).")
''',
                parameters=[
                    p("L", "Balka uzunligi L", 0.5, 10.0, 2.0, 0.1, "m"),
                    p("EI", "Egilish bikrligi EI", 1e4, 1e9, 1e6, 1e4, "N·m²"),
                    p("F", "Uchdagi kuch F", 10.0, 100000.0, 1000.0, 50.0, "N"),
                    p("q", "Taqsimlangan yuklama", 0.0, 10000.0, 0.0, 100.0, "N/m"),
                    p("n_terms", "Ritz hadlari soni", 1.0, 5.0, 3.0, 1.0, "dona"),
                ],
                expected_output="1 had: 25 % xatolik; 2 had: aniq yechim (0 %)",
            ),
            visual=vis(
                "Potensial energiya funksionali va yaqinlashish",
                "React/SVG",
                "Chapda $\\Pi(a_1)$ parabolasi va uning minimumi; o'ngda "
                "turli hadlar sonidagi taqribiy yechimlar va aniq yechim "
                "bir grafikda.",
                "React/SVG: funksionalning minimumga ega ekanini ko'rsatish "
                "variatsion prinsipning mohiyatini ochib beradi. "
                "Yaqinlashish grafigi esa Ritz usulining kuchini "
                "namoyish qiladi.",
            ),
            interp=(
                "Bitta had 25 % xatolik beradi, ikkitasi esa aniq yechimni "
                "beradi — chunki aniq yechim kubik polinom va u sinov "
                "funksiyalar fazosida yotadi. Bu Ritz usulining asosiy "
                "xossasi va FEM ning ishonchliligining sababi. "
                "$\\Pi(a_1)$ parabolasining aniq minimumi esa minimal "
                "energiya prinsipining vizual tasdig'i."
            ),
            mistakes=[
                "Sinov funksiyalarini geometrik chegaraviy shartlarni "
                "qanoatlantirmaydigan qilib tanlash.",
                "Kuch (tabiiy) chegaraviy shartlarini ham majburan "
                "qo'yishga urinish.",
                "Funksionalda tashqi ish ishorasini noto'g'ri qo'yish "
                "($\\Pi = U - W$).",
                "To'la bo'lmagan funksiyalar sistemasini ishlatish — "
                "yechim yaqinlashmaydi.",
            ],
            quiz=[
                q("Nima uchun variatsion formulirovka FEM uchun afzal?",
                  "Taqribiy yechim qurish tabiiy, tabiiy chegaraviy "
                  "shartlar avtomatik bajariladi, matritsa simmetrik va "
                  "musbat aniqlangan chiqadi.", "konseptual"),
                q("Qaysi chegaraviy shartlar majburiy qo'yilishi kerak?",
                  "Geometrik (muhim) shartlar — ko'chish bo'yicha; kuch "
                  "shartlari avtomatik bajariladi.", "konseptual"),
                q("Konsol balka uchun $\\Pi$ ni yozing.",
                  "$\\Pi = \\frac{EI}{2}\\int_0^L(w'')^2dx - Fw(L)$.", "hisob"),
                q("Nima uchun ikki hadli Ritz aniq yechimni berdi?",
                  "Konsol balkaning aniq yechimi kubik polinom va u "
                  "$x^2$, $x^3$ bazisda to'liq ifodalanadi.", "talqin"),
                q("Kodda $U = W/2$ tekshiruvi nimani tasdiqlaydi?",
                  "Klapeyron teoremasini: chiziqli elastik tizimda "
                  "deformatsiya energiyasi tashqi ishning yarmiga teng.",
                  "kod"),
            ],
            bridge=(
                "Elastiklik nazariyasi to'liq qurildi — differensial va "
                "variatsion formulirovkalarda. Keyingi modulda dinamik "
                "hodisalar va nochiziqli material xatti-harakatiga o'tamiz."
            ),
            research=(
                "Aralash variatsion prinsiplarni (Hellinger–Reissner) "
                "o'rganing: ko'chish va kuchlanish mustaqil approksimatsiya "
                "qilinadi. Bu siqilmaydigan materiallarda (rezina, "
                "$\\nu \\to 0{,}5$) 'volumetric locking' muammosini qanday "
                "hal qiladi? Sodda 1D misolda ikkala formulirovkani "
                "taqqoslang."
            ),
            manim_ref=manim(
                scene="VariationalScene",
                module="manim/scenes/tmm_variational.py",
                title="Minimal potensial energiya prinsipi",
                summary="Turli mumkin bo'lgan ko'chish maydonlari sinab "
                        "ko'riladi; haqiqiy yechim energiyani minimallashtiradi.",
            ),
        ),
    ),
]
