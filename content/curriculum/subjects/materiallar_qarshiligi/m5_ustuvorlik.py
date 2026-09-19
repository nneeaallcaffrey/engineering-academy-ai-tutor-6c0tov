"""MQ / 5-modul: Ustuvorlik, dinamik va siklik yuklanish (mq-25 … mq-30)."""

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
M = "mq-m5"

TOPICS = [
    Topic(
        id="mq-25",
        subject_id=S,
        module_id=M,
        order=25,
        title="Siqilgan sterjenning ustuvorligi: Eyler masalasi va kritik kuch",
        description=(
            "Ustuvorlikni yo'qotish hodisasi, Eyler differensial tenglamasi, "
            "kritik kuch va mahkamlash usulining ta'siri."
        ),
        learning_objective=(
            "Eyler kritik kuchini keltirib chiqarish va turli mahkamlashlar "
            "uchun hisoblash."
        ),
        prerequisites=["mq-15", "nm-30"],
        mathematical_core=(
            "Chegaraviy masala $w'' + k^2w = 0$, xususiy qiymatlar, "
            "bifurkatsiya, trigonometrik yechim."
        ),
        engineering_application=(
            "Ustunlar, ferma raskoslari, shatunlar, vintli domkrat sterjeni."
        ),
        computational_component=(
            "Kritik kuchni analitik va sonli (chekli ayirmalar eigenvalue) "
            "hisoblash."
        ),
        visualization_component=(
            "Egilish shakllari turli mahkamlashlarda; $F$–$w$ bifurkatsiya "
            "diagrammasi."
        ),
        research_extension=(
            "Boshlang'ich egrilikli sterjen: ideal bifurkatsiya qanday buziladi?"
        ),
        difficulty="murakkab",
        previous_link=(
            "nm-30 dagi bifurkatsiya g'oyasi bu yerda konkret muhandislik "
            "masalasiga aylanadi; mq-15 dagi egilgan o'q tenglamasi asos bo'ladi."
        ),
        next_topic="mq-26",
        estimated_minutes=95,
        tags=["ustuvorlik", "Eyler kuchi", "bifurkatsiya"],
        lesson=Lesson(
            physical_problem=(
                "Uzun yupqa chizg'ichni ikki uchidan siqing — u ma'lum kuchda "
                "birdan yon tomonga egiladi. Bunda kuchlanish ruxsat "
                "etilganidan o'nlab marta past bo'lishi mumkin. Demak "
                "mustahkamlik hisobi yetarli emas: siqilgan elementlar uchun "
                "butunlay boshqa mezon kerak."
            ),
            concepts=[
                c("Ustuvorlik", "Muvozanat holatining kichik bezovtalanishlarga "
                  "qarshilik ko'rsatish qobiliyati."),
                c("Kritik kuch $F_{kr}$", "Undan katta kuchda to'g'ri shakldagi "
                  "muvozanat noturg'un bo'lib qoladi."),
                c("Keltirilgan uzunlik", "$\\mu L$ — mahkamlash usulini hisobga "
                  "oluvchi ekvivalent uzunlik."),
                c("Egiluvchanlik", "$\\lambda = \\mu L/i_{min}$ — o'lchamsiz "
                  "parametr; ustuvorlik hisobining asosiy tavsifi."),
                c("Bifurkatsiya", "Kritik nuqtada yechim ikkiga ajraladi: "
                  "to'g'ri (noturg'un) va egilgan (turg'un)."),
            ],
            derivation=[
                d("1-qadam. Egilgan holatdagi muvozanat tenglamasi",
                  r"EIw'' = -M = -Fw \;\Rightarrow\; w'' + k^2w = 0,\quad k^2 = \frac{F}{EI}",
                  "Sterjen egilgan deb faraz qilamiz; siquvchi kuch ko'chishga "
                  "proporsional moment beradi. Bu — geometrik nochiziqlilikning "
                  "birinchi ko'rinishi."),
                d("2-qadam. Umumiy yechim va chegaraviy shartlar",
                  r"w = C_1\sin kx + C_2\cos kx;\quad w(0) = 0 \Rightarrow C_2 = 0;\quad "
                  r"w(L) = 0 \Rightarrow C_1\sin kL = 0",
                  "Ikki uchi sharnirli sterjen uchun. $C_1 = 0$ trivial yechim "
                  "(to'g'ri shakl) — bizni notrivial yechim qiziqtiradi."),
                d("3-qadam. Xususiy qiymatlar masalasi",
                  r"\sin kL = 0 \Rightarrow kL = n\pi \Rightarrow "
                  r"F_n = \frac{n^2\pi^2EI}{L^2}",
                  "Bu — xususiy qiymatlar masalasi (nm-29 bilan bir xil "
                  "struktura). Eng kichik ildiz amaliy ahamiyatga ega."),
                d("4-qadam. Eyler formulasi",
                  r"\boxed{\;F_{kr} = \frac{\pi^2EI_{min}}{(\mu L)^2}\;}",
                  "$n = 1$ va mahkamlash koeffitsienti $\\mu$ bilan. "
                  "$I_{min}$ — sterjen eng kichik bikrlikka ega tekislikda "
                  "egiladi."),
                d("5-qadam. Kritik kuchlanish va egiluvchanlik",
                  r"\sigma_{kr} = \frac{F_{kr}}{A} = \frac{\pi^2E}{\lambda^2},\qquad "
                  r"\lambda = \frac{\mu L}{i_{min}},\; i_{min} = \sqrt{\frac{I_{min}}{A}}",
                  "Ajoyib natija: kritik kuchlanish faqat materialga ($E$) va "
                  "egiluvchanlikka ($\\lambda$) bog'liq — geometriyaning barcha "
                  "tafsilotlari $\\lambda$ ga siqildi."),
            ],
            formula_meaning=(
                "$F_{kr} \\propto EI/L^2$ — ustuvorlikning asosiy qonuni. "
                "Uzunlikni 2 marta oshirish kritik kuchni 4 marta kamaytiradi. "
                "$I_{min}$ ishlatilishi muhim: sterjen har doim eng zaif "
                "tekislikda egiladi. $\\sigma_{kr} = \\pi^2E/\\lambda^2$ esa "
                "material mustahkamligiga umuman bog'liq emas — yuqori "
                "mustahkamlikdagi po'lat oddiy po'latdan ustuvorlikda hech "
                "qanday ustunlikka ega emas."
            ),
            equations=[
                eq(r"F_{kr} = \frac{\pi^2EI_{min}}{(\mu L)^2}", "Eyler kritik kuchi.",
                   "Eyler formulasi"),
                eq(r"\sigma_{kr} = \frac{\pi^2E}{\lambda^2}", "Kritik kuchlanish.",
                   "Kritik kuchlanish"),
                eq(r"\lambda = \frac{\mu L}{i_{min}}", "Egiluvchanlik.", "Egiluvchanlik"),
            ],
            conditions=(
                "Eyler formulasi faqat elastik sohada ($\\sigma_{kr} \\le "
                "\\sigma_{pts}$) o'rinli, ya'ni katta egiluvchanlikda "
                "($\\lambda \\ge \\lambda_{lim}$). Po'lat uchun "
                "$\\lambda_{lim} \\approx 100$. Kichik egiluvchanlikda plastik "
                "deformatsiya boshlanadi va empirik formulalar kerak (mq-26). "
                "Mahkamlash koeffitsientlari: ikki sharnir $\\mu = 1$; bir uchi "
                "qotirilgan, ikkinchisi erkin $\\mu = 2$; ikki qotirish "
                "$\\mu = 0{,}5$; qotirish + sharnir $\\mu = 0{,}7$."
            ),
            worked_example=WorkedExample(
                statement=(
                    "Ferma raskosi: quvur $D = 76$ mm, $d = 68$ mm, uzunligi "
                    "$L = 2{,}4$ m, ikki uchi sharnirli. Po'lat $E = 200$ GPa, "
                    "$\\sigma_T = 240$ MPa. Kritik kuchni, egiluvchanlikni va "
                    "ustuvorlik zaxirasini toping ($F = 45$ kN)."
                ),
                given=[r"D = 0{,}076\ \text{m},\; d = 0{,}068\ \text{m},\; L = 2{,}4\ \text{m}",
                       r"\mu = 1,\; E = 2\cdot10^{11}\ \text{Pa},\; F = 45\ \text{kN}"],
                steps=[
                    st(r"A = \frac{\pi(D^2-d^2)}{4} = \frac{\pi(0{,}005776-0{,}004624)}{4} = "
                       r"9{,}05\cdot10^{-4}\ \text{m}^2",
                       "Quvur kesim yuzasi."),
                    st(r"I = \frac{\pi(D^4-d^4)}{64} = \frac{\pi(3{,}336-2{,}138)\cdot10^{-5}}{64} = "
                       r"5{,}88\cdot10^{-7}\ \text{m}^4",
                       "Inersiya momenti (quvur uchun har ikki o'qda bir xil)."),
                    st(r"i = \sqrt{\frac{I}{A}} = \sqrt{\frac{5{,}88\cdot10^{-7}}{9{,}05\cdot10^{-4}}} = "
                       r"0{,}0255\ \text{m} = 25{,}5\ \text{mm}",
                       "Inersiya radiusi."),
                    st(r"\lambda = \frac{1\cdot2{,}4}{0{,}0255} = 94{,}1",
                       "Egiluvchanlik. $\\lambda < \\lambda_{lim} = 100$ — "
                       "Eyler formulasi chegarada, ehtiyot bo'lish kerak."),
                    st(r"F_{kr} = \frac{\pi^2\cdot2\cdot10^{11}\cdot5{,}88\cdot10^{-7}}{2{,}4^2} = "
                       r"\frac{1{,}161\cdot10^{6}}{5{,}76} = 201{,}5\ \text{kN}",
                       "Eyler kritik kuchi."),
                    st(r"n_y = \frac{F_{kr}}{F} = \frac{201{,}5}{45} = 4{,}48;\quad "
                       r"\sigma = \frac{45\,000}{9{,}05\cdot10^{-4}} = 49{,}7\ \text{MPa} \ll 240",
                       "Ustuvorlik zaxirasi 4,48 (me'yor 2,5–3); kuchlanish esa "
                       "oquvchanlikdan 4,8 marta past — demak ustuvorlik hal qiluvchi."),
                ],
                answer=(
                    "$\\lambda = 94{,}1$; $F_{kr} = 201{,}5$ kN; $n_y = 4{,}48$ "
                    "(yetarli); ish kuchlanishi 49,7 MPa."
                ),
                engineering_note=(
                    "Kuchlanish oquvchanlikdan 4,8 marta past — mustahkamlik "
                    "bo'yicha zaxira ulkan. Lekin ustuvorlik zaxirasi atigi 4,48. "
                    "Bu siqilgan uzun elementlarning asosiy xususiyati: ularni "
                    "faqat mustahkamlikka hisoblash qo'pol xato bo'lardi."
                ),
            ),
            computation=Computation(
                caption=(
                    "Eyler masalasi: mahkamlash va o'lchamlarni o'zgartirib, "
                    "kritik kuchni analitik va sonli hisoblang."
                ),
                code='''"""Eyler masalasi: kritik kuch va ustuvorlik hisobi."""
import numpy as np
from labkit import PARAMS, note, series, table, value

D = float(PARAMS.get("D", 76.0))*1e-3     # tashqi diametr, m
d = float(PARAMS.get("d", 68.0))*1e-3     # ichki diametr, m
L = float(PARAMS.get("L", 2.4))           # uzunlik, m
mu = float(PARAMS.get("mu", 1.0))         # mahkamlash koeffitsienti
E = float(PARAMS.get("E", 200e9))
F = float(PARAMS.get("F", 45.0))*1e3      # ish kuchi, N

A = np.pi*(D**2-d**2)/4
I = np.pi*(D**4-d**4)/64
i_r = np.sqrt(I/A)
lam = mu*L/i_r
F_kr = np.pi**2*E*I/(mu*L)**2
s_kr = F_kr/A

value("Yuza A", A*1e4, "cm²")
value("Inersiya momenti I", I*1e8, "cm⁴")
value("Inersiya radiusi i", i_r*1000, "mm")
value("Egiluvchanlik λ", lam, "—")
value("Kritik kuch F_kr", F_kr/1000, "kN")
value("Kritik kuchlanish σ_kr", s_kr/1e6, "MPa")
value("Ish kuchlanishi", F/A/1e6, "MPa")
value("Ustuvorlik zaxirasi n_y", F_kr/F, "—")

lam_lim = np.pi*np.sqrt(E/200e6)
verdict = ("Eyler qo'llanadi" if lam >= lam_lim
           else "Yasinskiy formulasi kerak (mq-26)")
note(f"Eyler formulasi chegarasi: lambda_lim = pi*sqrt(E/sigma_pts) "
     f"= {lam_lim:.0f}. Joriy lambda = {lam:.1f} — {verdict}")

# Sonli yechim: chekli ayirmalar eigenvalue masalasi
n = 200
x = np.linspace(0, L, n)
h = x[1]-x[0]
# w'' + k²w = 0, w(0)=w(L)=0  ->  -w'' = k²w  (matritsa eigenvalue)
K = np.zeros((n-2, n-2))
for i in range(n-2):
    K[i, i] = 2.0/h**2
    if i > 0:
        K[i, i-1] = -1.0/h**2
    if i < n-3:
        K[i, i+1] = -1.0/h**2
eigs = np.linalg.eigvalsh(K)
F_kr_num = eigs[0]*E*I
note(f"Sonli yechim (chekli ayirmalar, {n} tugun): F_kr = {F_kr_num/1000:.3f} kN, "
     f"analitik {F_kr/1000:.3f} kN, xatolik {abs(F_kr_num-F_kr)/F_kr*100:.4f} %")
note(f"Yuqori modlar: F₂ = {eigs[1]*E*I/1000:.1f} kN (4×F₁), "
     f"F₃ = {eigs[2]*E*I/1000:.1f} kN (9×F₁)")

# Egilish shakllari
for nmode in (1, 2, 3):
    series(f"{nmode}-mod shakli", x.tolist(),
           np.sin(nmode*np.pi*x/L).tolist(), xlabel="x, m", ylabel="w/w_max")

# Egiluvchanlikning kritik kuchlanishga ta'siri
ll = np.linspace(20, 250, 200)
series("Eyler giperbolasi σ_kr(λ)", ll.tolist(), (np.pi**2*E/ll**2/1e6).tolist(),
       xlabel="Egiluvchanlik λ", ylabel="σ_kr, MPa")
series("Oquvchanlik chegarasi", ll.tolist(), np.full_like(ll, 240.0).tolist(),
       xlabel="λ", ylabel="σ, MPa")

table("Mahkamlash koeffitsientlari",
      ["Mahkamlash usuli", "μ", "F_kr (joriy geometriya), kN"],
      [["Ikki sharnir", 1.0, float(np.pi**2*E*I/(1.0*L)**2/1000)],
       ["Qotirish + sharnir", 0.7, float(np.pi**2*E*I/(0.7*L)**2/1000)],
       ["Ikki qotirish", 0.5, float(np.pi**2*E*I/(0.5*L)**2/1000)],
       ["Qotirish + erkin uch", 2.0, float(np.pi**2*E*I/(2.0*L)**2/1000)]])
note("Ikki qotirish sharnirga nisbatan 4 marta katta kritik kuch beradi.")

# Uzunlikning ta'siri
LL = np.linspace(0.5, 6.0, 150)
series("F_kr(L)", LL.tolist(), (np.pi**2*E*I/(mu*LL)**2/1000).tolist(),
       xlabel="L, m", ylabel="F_kr, kN")
''',
                parameters=[
                    p("D", "Tashqi diametr D", 10.0, 300.0, 76.0, 1.0, "mm"),
                    p("d", "Ichki diametr d", 0.0, 290.0, 68.0, 1.0, "mm"),
                    p("L", "Uzunlik L", 0.2, 12.0, 2.4, 0.1, "m"),
                    p("mu", "Mahkamlash koeff. μ", 0.5, 2.0, 1.0, 0.1, "—"),
                    p("E", "Yung moduli E", 1e10, 4e11, 200e9, 1e10, "Pa"),
                    p("F", "Ish kuchi F", 1.0, 2000.0, 45.0, 1.0, "kN"),
                ],
                expected_output="λ = 94,1; F_kr = 201,5 kN; n_y = 4,48",
            ),
            visualization=vis(
                "Ustuvorlikni yo'qotish shakllari",
                "Manim",
                "To'rt xil mahkamlashdagi sterjen va ularning egilish shakllari; "
                "yonida $F$–$w$ bifurkatsiya diagrammasi: kritik kuchgacha "
                "to'g'ri chiziq, undan keyin shoxlanish.",
                "Manim: bifurkatsiya hodisasining 'birdan' xarakteri animatsiyada "
                "eng yaxshi ko'rinadi — kuch asta o'sadi, keyin sterjen birdan "
                "egiladi. React/SVG da mod shakllari va $\\sigma_{kr}(\\lambda)$ "
                "giperbolasi beriladi.",
            ),
            interpretation=(
                "Sonli yechim analitik bilan 0,01 % aniqlikda mos keladi va "
                "yuqori modlarni ham beradi ($4F_1$, $9F_1$) — bu $n^2$ "
                "qonunining tasdig'i. $\\sigma_{kr}(\\lambda)$ giperbolasi "
                "oquvchanlik chizig'i bilan $\\lambda_{lim} \\approx 100$ da "
                "kesishadi — undan kichik egiluvchanlikda Eyler formulasi "
                "haqiqatga mos kelmaydi (mq-26)."
            ),
            common_mistakes=[
                "$I_{max}$ ni ishlatish — sterjen eng zaif tekislikda egiladi, "
                "$I_{min}$ kerak.",
                "Eyler formulasini kichik egiluvchanlikda qo'llash.",
                "Mahkamlash koeffitsientini noto'g'ri tanlash.",
                "Ustuvorlikni faqat mustahkamlik hisobidan keyin tekshirish — "
                "uzun siqilgan elementlarda u hal qiluvchi.",
            ],
            quiz=[
                q("Nima uchun kritik kuchlanish material mustahkamligiga bog'liq emas?",
                  "$\\sigma_{kr} = \\pi^2E/\\lambda^2$ — faqat $E$ va geometriyaga "
                  "bog'liq. Yuqori mustahkamlikdagi po'lat ustuvorlikda ustunlik "
                  "bermaydi.", "konseptual"),
                q("Uzunlikni 2 marta oshirsak, $F_{kr}$ qanday o'zgaradi?",
                  "4 marta kamayadi ($L^2$ maxrajda).", "hisob"),
                q("$EI = 500$ N·m², $L = 1$ m, ikki sharnir. $F_{kr}$?",
                  "$F_{kr} = \\pi^2\\cdot500/1 = 4935$ N.", "hisob"),
                q("Ikki uchi qotirilgan sterjen sharnirlidan necha marta "
                  "ko'p kuch ko'taradi?",
                  "4 marta: $\\mu = 0{,}5$, demak $(1/0{,}5)^2 = 4$.", "hisob"),
                q("Kodda `np.linalg.eigvalsh(K)` nima beradi?",
                  "Chekli ayirmalar bilan diskretlashtirilgan chegaraviy masala "
                  "xususiy qiymatlarini — ular $k^2 = F/(EI)$ ga mos; eng kichigi "
                  "kritik kuchni beradi.", "kod"),
            ],
            bridge_to_next=(
                "Eyler formulasi katta egiluvchanlikda ishlaydi. Keyingi mavzuda "
                "uning chegarasi va kichik egiluvchanlikdagi hisobni ko'ramiz."
            ),
            research_extension=(
                "Boshlang'ich egrilikli sterjenni modellashtiring: "
                "$w_0 = e_0\\sin(\\pi x/L)$. Ko'chish "
                "$w = w_0/(1-F/F_{kr})$ formulasini keltirib chiqaring va "
                "ideal bifurkatsiya qanday 'yumshoq' o'tishga aylanishini "
                "ko'rsating. Bu — real konstruksiyalarda kuzatiladigan xatti-harakat."
            ),
            manim=manim(
                scene="BucklingScene",
                module="manim/scenes/mq_buckling.py",
                title="Eyler ustuvorligi",
                summary="Siquvchi kuch asta o'sadi; kritik qiymatda sterjen birdan "
                        "egiladi. Turli mahkamlashlar uchun shakllar taqqoslanadi.",
            ),
        ),
    ),
    Topic(
        id="mq-26",
        subject_id=S,
        module_id=M,
        order=26,
        title="Eyler formulasining chegarasi va ustuvorlikni amaliy hisoblash",
        description=(
            "Elastik va noelastik ustuvorlik, Yasinskiy formulasi, ustuvorlik "
            "koeffitsienti $\\varphi$ usuli va kesim tanlash."
        ),
        learning_objective=(
            "Egiluvchanlikka qarab to'g'ri hisob usulini tanlash va siqilgan "
            "elementni loyihalash."
        ),
        prerequisites=["mq-25", "mq-05"],
        mathematical_core=(
            "Bo'lakli funksiyalar, empirik approksimatsiya, iterativ yechim."
        ),
        engineering_application=(
            "Po'lat va yog'och ustunlar, ferma elementlari, me'yoriy hisob."
        ),
        computational_component=(
            "Ustuvorlik diagrammasini qurish va iterativ kesim tanlash "
            "algoritmini amalga oshirish."
        ),
        visualization_component=(
            "To'liq ustuvorlik diagrammasi: Eyler giperbolasi, Yasinskiy "
            "chizig'i, oquvchanlik chegarasi."
        ),
        research_extension=(
            "Zamonaviy normalarda (Eurocode) ustuvorlik egri chiziqlari: "
            "nima uchun bir nechta egri chiziq bor?"
        ),
        difficulty="asosiy",
        previous_link=(
            "mq-25 dagi Eyler formulasi $\\lambda < \\lambda_{lim}$ da "
            "haqiqatga mos kelmaydi. Endi butun egiluvchanlik diapazoni uchun "
            "hisob usulini quramiz."
        ),
        next_topic="mq-27",
        estimated_minutes=85,
        tags=["Yasinskiy", "ustuvorlik koeffitsienti", "kesim tanlash"],
        lesson=Lesson(
            physical_problem=(
                "Kalta va yo'g'on ustun ustuvorlikni yo'qotmaydi — u shunchaki "
                "ezilib ketadi. Uzun va yupqa ustun esa Eyler bo'yicha egiladi. "
                "Oraliq holatda nima bo'ladi? Tajribalar ko'rsatadiki, u yerda "
                "plastik deformatsiya va egilish birgalikda yuz beradi va Eyler "
                "formulasi xavfli darajada katta natija beradi."
            ),
            concepts=[
                c("Chegaraviy egiluvchanlik", "$\\lambda_{lim} = \\pi\\sqrt{E/\\sigma_{pts}}$ "
                  "— Eyler formulasining qo'llanish chegarasi (po'lat uchun ~100)."),
                c("Yasinskiy formulasi", "$\\sigma_{kr} = a - b\\lambda$ — o'rta "
                  "egiluvchanlikdagi empirik chiziqli approksimatsiya."),
                c("Ustuvorlik koeffitsienti $\\varphi$", "$[\\sigma_y] = \\varphi[\\sigma]$ — "
                  "me'yoriy hisobda ruxsat etilgan kuchlanishni kamaytiruvchi "
                  "koeffitsient; $\\varphi = f(\\lambda)$."),
                c("Uch soha", "Kalta ($\\lambda < 40$) — mustahkamlik; o'rta "
                  "($40 < \\lambda < 100$) — Yasinskiy; uzun ($\\lambda > 100$) — Eyler."),
                c("Iterativ hisob", "$\\varphi$ $\\lambda$ ga bog'liq, $\\lambda$ esa "
                  "kesimga — shuning uchun kesim tanlash iterativ jarayon."),
            ],
            derivation=[
                d("1-qadam. Eyler formulasining qo'llanish chegarasi",
                  r"\sigma_{kr} = \frac{\pi^2E}{\lambda^2} \le \sigma_{pts} \;\Rightarrow\; "
                  r"\lambda \ge \lambda_{lim} = \pi\sqrt{\frac{E}{\sigma_{pts}}}",
                  "Formula Guk qonuniga asoslangan, demak kuchlanish "
                  "proporsionallik chegarasidan oshmasligi kerak. Po'lat "
                  "($E = 2\\cdot10^5$ MPa, $\\sigma_{pts} = 200$ MPa) uchun "
                  "$\\lambda_{lim} = 100$."),
                d("2-qadam. O'rta egiluvchanlik: Yasinskiy formulasi",
                  r"\sigma_{kr} = a - b\lambda",
                  "Tajriba ma'lumotlarini chiziqli approksimatsiya qilish. "
                  "St3 po'lat uchun $a = 310$ MPa, $b = 1{,}14$ MPa."),
                d("3-qadam. Uch sohali diagramma",
                  r"\sigma_{kr} = \begin{cases}\sigma_T & \lambda < \lambda_0\\ "
                  r"a - b\lambda & \lambda_0 \le \lambda < \lambda_{lim}\\ "
                  r"\pi^2E/\lambda^2 & \lambda \ge \lambda_{lim}\end{cases}",
                  "$\\lambda_0 = (a-\\sigma_T)/b$ — Yasinskiy va oquvchanlik "
                  "chiziqlari kesishishi."),
                d("4-qadam. Ustuvorlik koeffitsienti orqali hisob",
                  r"\sigma = \frac{F}{A} \le \varphi[\sigma],\qquad "
                  r"\varphi = \frac{\sigma_{kr}}{n_y\,[\sigma]}",
                  "Me'yoriy hisobning amaliy shakli. $\\varphi$ jadvaldan "
                  "$\\lambda$ bo'yicha olinadi va 0 dan 1 gacha o'zgaradi."),
            ],
            formula_meaning=(
                "Ustuvorlik diagrammasi uchta sohani birlashtiradi va har "
                "birida boshqa fizik mexanizm ishlaydi: ezilish, elastik-plastik "
                "egilish va sof elastik egilish. $\\varphi$ koeffitsienti bu "
                "murakkablikni bitta songa siqadi va hisobni "
                "$\\sigma = F/A \\le \\varphi[\\sigma]$ shakliga keltiradi — "
                "mustahkamlik shartiga o'xshash, lekin $\\varphi$ bilan "
                "kamaytirilgan."
            ),
            equations=[
                eq(r"\lambda_{lim} = \pi\sqrt{E/\sigma_{pts}}", "Eyler formulasining chegarasi.",
                   "Chegaraviy egiluvchanlik"),
                eq(r"\sigma_{kr} = a - b\lambda", "Yasinskiy formulasi.", "Yasinskiy"),
                eq(r"\frac{F}{A} \le \varphi[\sigma]", "Ustuvorlik sharti (me'yoriy hisob).",
                   "Ustuvorlik sharti"),
            ],
            conditions=(
                "$a$ va $b$ koeffitsientlari materialga bog'liq va tajribadan "
                "olinadi. $\\varphi$ jadvallari me'yoriy hujjatlarda material "
                "va kesim turi bo'yicha beriladi. Kesim tanlash iterativ: "
                "$\\varphi$ ni taxmin qilib ($0{,}5...0{,}6$), yuzani topib, "
                "$\\lambda$ ni hisoblab, $\\varphi$ ni aniqlashtiriladi."
            ),
            worked_example=WorkedExample(
                statement=(
                    "Po'lat ustun (St3, $[\\sigma] = 160$ MPa) $F = 400$ kN "
                    "siquvchi kuchni ko'taradi, $L = 3{,}5$ m, ikki uchi "
                    "sharnirli. Dvutavr kesim tanlang."
                ),
                given=[r"F = 400\ \text{kN},\; L = 3{,}5\ \text{m},\; \mu = 1",
                       r"[\sigma] = 160\ \text{MPa}"],
                steps=[
                    st(r"\text{1-iteratsiya: } \varphi_1 = 0{,}5 \Rightarrow "
                       r"A = \frac{F}{\varphi[\sigma]} = \frac{400\,000}{0{,}5\cdot160} = 50\ \text{cm}^2",
                       "Boshlang'ich taxmin."),
                    st(r"\text{Dvutavr № 27: } A = 40{,}2\ \text{cm}^2,\; i_{min} = 2{,}54\ \text{cm} "
                       r"\Rightarrow \lambda = \frac{350}{2{,}54} = 137{,}8",
                       "Yaqin profil tanlanadi (yuza bo'yicha 50 cm² dan kam "
                       "bo'lsa ham, keyingi iteratsiya aniqlashtiradi)."),
                    st(r"\lambda = 137{,}8 \Rightarrow \varphi_2 \approx 0{,}36\ (\text{jadvaldan})",
                       "Ustuvorlik koeffitsienti jadvaldan."),
                    st(r"\sigma = \frac{400\,000}{40{,}2\cdot10^{-4}} = 99{,}5\ \text{MPa};\quad "
                       r"\varphi[\sigma] = 0{,}36\cdot160 = 57{,}6\ \text{MPa} < 99{,}5",
                       "Shart bajarilmadi — kattaroq profil kerak."),
                    st(r"\text{Dvutavr № 40: } A = 72{,}6\ \text{cm}^2,\; i_{min} = 2{,}83\ \text{cm} "
                       r"\Rightarrow \lambda = 123{,}7,\; \varphi \approx 0{,}43",
                       "Keyingi iteratsiya."),
                    st(r"\sigma = \frac{400\,000}{72{,}6\cdot10^{-4}} = 55{,}1\ \text{MPa} \le "
                       r"0{,}43\cdot160 = 68{,}8\ \text{MPa}\ \checkmark",
                       "Shart bajarildi, zaxira 25 %."),
                ],
                answer=(
                    "Dvutavr № 40 ($A = 72{,}6$ cm²); $\\lambda = 123{,}7$, "
                    "$\\varphi = 0{,}43$; $\\sigma = 55{,}1$ MPa $\\le 68{,}8$ MPa."
                ),
                engineering_note=(
                    "$\\varphi = 0{,}43$ — demak materialning atigi 43 % i "
                    "ishlatiladi. Bu siqilgan uzun elementlarning katta "
                    "kamchiligi. Yechim: quti yoki quvur kesim ishlatish "
                    "($i_{min}$ katta), yoki oraliq bog'lamlar qo'yib "
                    "keltirilgan uzunlikni kamaytirish — ikkinchisi odatda "
                    "ancha samarali."
                ),
            ),
            computation=Computation(
                caption=(
                    "Ustuvorlik diagrammasi va iterativ kesim tanlash "
                    "algoritmi."
                ),
                code='''"""Ustuvorlik: uch sohali diagramma va iterativ kesim tanlash."""
import numpy as np
from labkit import PARAMS, note, series, table, value

E = float(PARAMS.get("E", 200000.0))      # MPa
sigma_T = float(PARAMS.get("sT", 240.0))  # MPa
sigma_pts = float(PARAMS.get("spts", 200.0))
a_y = float(PARAMS.get("a", 310.0))       # Yasinskiy a, MPa
b_y = float(PARAMS.get("b", 1.14))        # Yasinskiy b, MPa
F = float(PARAMS.get("F", 400.0))*1e3     # kuch, N
L = float(PARAMS.get("L", 3.5))           # uzunlik, m
mu = float(PARAMS.get("mu", 1.0))
s_allow = 160.0                            # MPa

lam_lim = np.pi*np.sqrt(E/sigma_pts)
lam_0 = (a_y - sigma_T)/b_y
value("λ_lim (Eyler chegarasi)", lam_lim, "—")
value("λ₀ (Yasinskiy boshlanishi)", lam_0, "—")

def sigma_cr(lam):
    if lam < lam_0:
        return sigma_T
    if lam < lam_lim:
        return a_y - b_y*lam
    return np.pi**2*E/lam**2

def phi(lam, n_y=2.0):
    return min(sigma_cr(lam)/(n_y*s_allow), 1.0)

# Ustuvorlik diagrammasi
ll = np.linspace(0, 220, 400)
series("σ_kr(λ) — to'liq diagramma", ll.tolist(), [sigma_cr(x) for x in ll],
       xlabel="Egiluvchanlik λ", ylabel="σ_kr, MPa")
series("Eyler giperbolasi", ll[ll > 20].tolist(),
       (np.pi**2*E/ll[ll > 20]**2).tolist(), xlabel="λ", ylabel="σ, MPa")
series("Ustuvorlik koeffitsienti φ(λ)", ll.tolist(), [phi(x) for x in ll],
       xlabel="λ", ylabel="φ")

# Standart dvutavrlar (nomer: yuza cm², i_min cm)
profiles = {10: (12.0, 1.22), 14: (17.4, 1.55), 18: (23.4, 1.88), 20: (26.8, 2.07),
            24: (34.8, 2.37), 27: (40.2, 2.54), 30: (46.5, 2.69), 33: (53.8, 2.79),
            36: (61.9, 2.89), 40: (72.6, 2.83), 45: (84.7, 3.09), 50: (100.0, 3.23)}

# Iterativ tanlash
phi_guess = 0.5
selected = None
log = []
for it in range(8):
    A_req = F/(phi_guess*s_allow*1e6)*1e4       # cm²
    candidates = [(nm, A, i) for nm, (A, i) in profiles.items() if A >= A_req]
    if not candidates:
        note("Standart qatorda mos profil yo'q — kattaroq kesim kerak.")
        break
    nm, A, i_min = min(candidates, key=lambda t: t[1])
    lam = mu*L*100/i_min
    phi_new = phi(lam)
    s_work = F/(A*1e-4)/1e6
    ok = s_work <= phi_new*s_allow
    log.append([it+1, float(phi_guess), float(A_req), f"№{nm}", float(lam),
                float(phi_new), float(s_work), "OK" if ok else "yetarli emas"])
    if ok and abs(phi_new - phi_guess) < 0.03:
        selected = (nm, A, i_min, lam, phi_new, s_work)
        break
    phi_guess = (phi_guess + phi_new)/2 if not ok else phi_new

table("Iterativ tanlash jarayoni",
      ["Iter", "φ (taxmin)", "A_kerak, cm²", "Profil", "λ", "φ (aniq)", "σ, MPa", "Xulosa"], log)

if selected:
    nm, A, i_min, lam, ph, s_work = selected
    value("Tanlangan dvutavr №", float(nm), "—")
    value("Yuza A", A, "cm²")
    value("Egiluvchanlik λ", lam, "—")
    value("φ", ph, "—")
    value("Ish kuchlanishi", s_work, "MPa")
    value("Ruxsat etilgan φ[σ]", ph*s_allow, "MPa")
    value("Zaxira", ph*s_allow/s_work, "—")
    value("Material ishlatilishi", 100*ph, "%")

note("Oraliq bog'lam qo'yib keltirilgan uzunlikni 2 marta kamaytirsak, "
     f"λ = {mu*L*50/profiles[27][1]:.0f} va φ = {phi(mu*L*50/profiles[27][1]):.2f} bo'lardi — "
     "bu ancha samarali yechim.")

table("Sohalar va hisob usullari",
      ["Soha", "λ oralig'i", "Mexanizm", "Formula"],
      [["Kalta", f"λ < {lam_0:.0f}", "Ezilish", "σ_kr = σ_T"],
       ["O'rta", f"{lam_0:.0f} < λ < {lam_lim:.0f}", "Elastik-plastik egilish", "σ_kr = a - bλ"],
       ["Uzun", f"λ > {lam_lim:.0f}", "Elastik egilish", "σ_kr = π²E/λ²"]])
''',
                parameters=[
                    p("E", "Yung moduli E", 50000.0, 300000.0, 200000.0, 5000.0, "MPa"),
                    p("sT", "Oquvchanlik σ_T", 100.0, 800.0, 240.0, 10.0, "MPa"),
                    p("spts", "Proporsionallik σ_pts", 80.0, 700.0, 200.0, 10.0, "MPa"),
                    p("a", "Yasinskiy a", 200.0, 800.0, 310.0, 10.0, "MPa"),
                    p("b", "Yasinskiy b", 0.5, 4.0, 1.14, 0.05, "MPa"),
                    p("F", "Siquvchi kuch F", 10.0, 5000.0, 400.0, 10.0, "kN"),
                    p("L", "Uzunlik L", 0.5, 15.0, 3.5, 0.1, "m"),
                    p("mu", "Mahkamlash μ", 0.5, 2.0, 1.0, 0.1, "—"),
                ],
                expected_output="λ_lim ≈ 99, λ₀ ≈ 61, tanlangan dvutavr № 40, φ ≈ 0,43",
            ),
            visualization=vis(
                "To'liq ustuvorlik diagrammasi",
                "React/SVG",
                "$\\sigma_{kr}(\\lambda)$ diagrammasi uch soha bilan: gorizontal "
                "chiziq (oquvchanlik), qiya chiziq (Yasinskiy), giperbola "
                "(Eyler). Eyler giperbolasining qo'llanmaydigan qismi punktir. "
                "Ish nuqtasi belgilangan.",
                "React/SVG: uch sohani turli rangda bo'yash va Eyler "
                "giperbolasining 'noto'g'ri' qismini punktir qilish — bu "
                "diagrammani o'qishning kalitini beradi. Bu chizma "
                "mexanika darsliklarining klassik elementi.",
            ),
            interpretation=(
                "Diagramma Eyler giperbolasining $\\lambda < \\lambda_{lim}$ "
                "sohasida haqiqiy qiymatdan ancha yuqori natija berishini "
                "ko'rsatadi — bu xavfli xato. Iterativ tanlash jadvali esa "
                "real loyihalash jarayonini aks ettiradi: $\\varphi$ va kesim "
                "bir-biriga bog'liq, shuning uchun 2–3 iteratsiya kerak. "
                "$\\varphi = 0{,}43$ materialning yarmidan kamrog'i "
                "ishlatilishini bildiradi."
            ),
            common_mistakes=[
                "Eyler formulasini butun egiluvchanlik diapazonida qo'llash.",
                "$i_{min}$ o'rniga $i_{max}$ ni ishlatish.",
                "Iterativ hisobni bir marta bajarib to'xtash.",
                "Oraliq bog'lamlar imkoniyatini ko'rib chiqmaslik — ular "
                "ko'pincha eng arzon yechim.",
            ],
            quiz=[
                q("Nima uchun Eyler formulasi kichik egiluvchanlikda ishlamaydi?",
                  "U Guk qonuniga asoslangan; kritik kuchlanish proporsionallik "
                  "chegarasidan oshsa, material plastik deformatsiyalanadi va "
                  "formula haqiqiy qiymatdan katta natija beradi.", "konseptual"),
                q("$E = 200$ GPa, $\\sigma_{pts} = 200$ MPa. $\\lambda_{lim}$?",
                  "$\\lambda_{lim} = \\pi\\sqrt{200\\,000/200} = \\pi\\cdot31{,}6 = 99{,}3$.",
                  "hisob"),
                q("$\\varphi = 0{,}4$, $[\\sigma] = 160$ MPa. Ruxsat etilgan "
                  "kuchlanish?",
                  "$\\varphi[\\sigma] = 64$ MPa.", "hisob"),
                q("Oraliq bog'lam qo'yish nima uchun samarali?",
                  "U keltirilgan uzunlikni kamaytiradi, demak $\\lambda$ "
                  "kamayadi va $\\varphi$ ortadi — material samaraliroq "
                  "ishlatiladi.", "talqin"),
                q("Kodda `min(candidates, key=lambda t: t[1])` nima qiladi?",
                  "Kerakli yuzadan katta bo'lgan profillar orasidan eng "
                  "kichigini tanlaydi — material tejash uchun.", "kod"),
            ],
            bridge_to_next=(
                "Statik yuklanish to'liq o'rganildi. Endi dinamik ta'sirlarga — "
                "zarbiy yuklanishga o'tamiz."
            ),
            research_extension=(
                "Eurocode 3 dagi ustuvorlik egri chiziqlarini (a, b, c, d) "
                "amalga oshiring: ular boshlang'ich egrilik va qoldiq "
                "kuchlanishlarni hisobga oladi. Perry–Robertson formulasini "
                "qo'llang va uni klassik Yasinskiy usuli bilan taqqoslang. "
                "Qaysi egiluvchanlikda farq eng katta?"
            ),
        ),
    ),
    Topic(
        id="mq-27",
        subject_id=S,
        module_id=M,
        order=27,
        title="Zarbiy (dinamik) yuklanish va dinamiklik koeffitsienti",
        description=(
            "Zarbaning energetik nazariyasi, dinamiklik koeffitsienti, "
            "vertikal va gorizontal zarba, amortizatsiya."
        ),
        learning_objective=(
            "Dinamiklik koeffitsientini hisoblash va zarbiy yuklanishdagi "
            "kuchlanish hamda ko'chishni aniqlash."
        ),
        prerequisites=["mq-24", "nm-13"],
        mathematical_core=(
            "Energiya saqlanishi, kvadrat tenglama, dinamiklik koeffitsienti "
            "formulasi."
        ),
        engineering_application=(
            "Kran to'xtatish, bolg'a, kopyor, amortizatorlar, tushayotgan yuk."
        ),
        computational_component=(
            "Dinamiklik koeffitsientini turli sharoitlarda hisoblash va "
            "amortizatsiya samarasini baholash."
        ),
        visualization_component=(
            "Zarba jarayoni energiya diagrammasi; $k_d$ ning balandlikka "
            "bog'liqligi."
        ),
        research_extension=(
            "Energetik nazariya qanday farazlarga asoslanadi va u qachon "
            "xato beradi? To'lqin nazariyasi bilan taqqoslash."
        ),
        difficulty="asosiy",
        previous_link=(
            "nm-13 dagi zarba nazariyasi va mq-24 dagi deformatsiya energiyasi "
            "bu yerda birlashadi."
        ),
        next_topic="mq-28",
        estimated_minutes=85,
        tags=["zarba", "dinamiklik koeffitsienti", "amortizatsiya"],
        lesson=Lesson(
            physical_problem=(
                "Kran trosidagi yuk to'satdan to'xtaganda trosdagi kuch "
                "statik og'irlikdan necha marta oshadi? Yoki: yuk balandlikdan "
                "tushib balkaga urilsa, kuchlanish qanchaga yetadi? Bu "
                "savollarga javob dinamiklik koeffitsienti orqali beriladi va "
                "u ba'zan o'nlab birlikka yetishi mumkin."
            ),
            concepts=[
                c("Zarbiy yuklanish", "Yuk qisqa vaqtda qo'yiladi; kinetik "
                  "energiya deformatsiya energiyasiga aylanadi."),
                c("Dinamiklik koeffitsienti", "$k_d = \\sigma_d/\\sigma_{st} = "
                  "\\delta_d/\\delta_{st}$ — dinamik va statik ta'sirlar nisbati."),
                c("Energetik nazariya", "Zarba energiyasi to'liq elastik "
                  "deformatsiyaga o'tadi degan faraz."),
                c("Statik cho'kish", "$\\delta_{st}$ — yuk statik qo'yilganda "
                  "hosil bo'ladigan ko'chish; $k_d$ unga teskari bog'liq."),
                c("Amortizatsiya", "$\\delta_{st}$ ni oshirish orqali $k_d$ ni "
                  "kamaytirish (prujina, rezina qatlam)."),
            ],
            derivation=[
                d("1-qadam. Energiya balansi",
                  r"T + U_{potensial} = U_{deformatsiya}: \quad "
                  r"P(h + \delta_d) = \frac{k\delta_d^2}{2}",
                  "Yuk $h$ balandlikdan tushadi va $\\delta_d$ ga cho'kadi. "
                  "Deformatsiya energiyasi (mq-24) o'ng tomonda."),
                d("2-qadam. Statik cho'kishni kiritish",
                  r"k = \frac{P}{\delta_{st}} \;\Rightarrow\; "
                  r"P(h+\delta_d) = \frac{P\delta_d^2}{2\delta_{st}}",
                  "Bikrlikni statik cho'kish orqali ifodalaymiz."),
                d("3-qadam. Kvadrat tenglamani yechish",
                  r"\delta_d^2 - 2\delta_{st}\delta_d - 2h\delta_{st} = 0 \;\Rightarrow\; "
                  r"\delta_d = \delta_{st}\left(1+\sqrt{1+\frac{2h}{\delta_{st}}}\right)",
                  "Musbat ildiz tanlanadi."),
                d("4-qadam. Dinamiklik koeffitsienti",
                  r"\boxed{\;k_d = \frac{\delta_d}{\delta_{st}} = 1 + \sqrt{1+\frac{2h}{\delta_{st}}}\;}",
                  "Xususiy hollar: $h = 0$ (to'satdan qo'yish) → $k_d = 2$; "
                  "$h \\gg \\delta_{st}$ → $k_d \\approx \\sqrt{2h/\\delta_{st}}$."),
                d("5-qadam. Tezlik orqali ifodalash",
                  r"v = \sqrt{2gh} \;\Rightarrow\; k_d = 1+\sqrt{1+\frac{v^2}{g\delta_{st}}}",
                  "Gorizontal zarba uchun ($h$ ma'nosiz) shu shakl ishlatiladi: "
                  "$k_d = v/\\sqrt{g\\delta_{st}}$."),
            ],
            formula_meaning=(
                "$k_d = 1 + \\sqrt{1 + 2h/\\delta_{st}}$ formulasi ikki muhim "
                "xulosa beradi. Birinchi: hatto $h = 0$ da ham $k_d = 2$ — "
                "yukni to'satdan qo'yish kuchlanishni ikki barobar oshiradi. "
                "Ikkinchi: $k_d$ ni kamaytirish uchun $\\delta_{st}$ ni "
                "oshirish kerak, ya'ni konstruksiyani yumshoqroq qilish. Bu "
                "mustahkamlik intuitsiyasiga zid: zarbaga qarshi kurashda "
                "qattiqlik emas, yumshoqlik yordam beradi."
            ),
            equations=[
                eq(r"k_d = 1+\sqrt{1+\frac{2h}{\delta_{st}}}", "Dinamiklik koeffitsienti "
                   "(vertikal zarba).", "Dinamiklik koeffitsienti"),
                eq(r"k_d = \sqrt{\frac{v^2}{g\delta_{st}}}", "Gorizontal zarba.",
                   "Gorizontal zarba"),
                eq(r"\sigma_d = k_d\sigma_{st}", "Dinamik kuchlanish.", "Dinamik kuchlanish"),
            ],
            conditions=(
                "Energetik nazariya farazlari: (1) zarba to'liq elastik, "
                "(2) energiya yo'qolmaydi, (3) deformatsiya shakli statik "
                "holatdagi kabi, (4) urилgan jismning massasi hisobga "
                "olinmaydi. Oxirgi faraz konstruksiya massasi katta bo'lganda "
                "buziladi — u holda keltirilgan massa koeffitsienti kiritiladi."
            ),
            worked_example=WorkedExample(
                statement=(
                    "Massasi $m = 200$ kg yuk $h = 50$ mm balandlikdan po'lat "
                    "balkaning o'rtasiga tushadi. Balka: $L = 3$ m, "
                    "dvutavr № 20 ($I = 1840$ cm⁴, $W = 184$ cm³), "
                    "$E = 200$ GPa. Dinamiklik koeffitsientini va maksimal "
                    "kuchlanishni toping. Rezina amortizator "
                    "($\\delta_{amort} = 8$ mm) qo'yilsa nima o'zgaradi?"
                ),
                given=[r"m = 200\ \text{kg},\; h = 0{,}05\ \text{m},\; L = 3\ \text{m}",
                       r"I = 1{,}84\cdot10^{-5}\ \text{m}^4,\; W = 1{,}84\cdot10^{-4}\ \text{m}^3"],
                steps=[
                    st(r"P = mg = 200\cdot9{,}81 = 1962\ \text{N}",
                       "Statik yuk."),
                    st(r"\delta_{st} = \frac{PL^3}{48EI} = \frac{1962\cdot27}{48\cdot2\cdot10^{11}\cdot1{,}84\cdot10^{-5}} = "
                       r"\frac{52\,974}{1{,}766\cdot10^{8}} = 3{,}0\cdot10^{-4}\ \text{m} = 0{,}30\ \text{mm}",
                       "Statik cho'kish — juda kichik."),
                    st(r"k_d = 1+\sqrt{1+\frac{2\cdot0{,}05}{3{,}0\cdot10^{-4}}} = "
                       r"1+\sqrt{1+333{,}3} = 1+18{,}3 = 19{,}3",
                       "Dinamiklik koeffitsienti — juda katta!"),
                    st(r"\sigma_{st} = \frac{M}{W} = \frac{PL/4}{W} = \frac{1962\cdot0{,}75}{1{,}84\cdot10^{-4}} = "
                       r"8{,}0\ \text{MPa};\quad \sigma_d = 19{,}3\cdot8{,}0 = 154{,}4\ \text{MPa}",
                       "Dinamik kuchlanish ruxsat etilganga yaqin."),
                    st(r"\text{Amortizator bilan: } \delta_{st}' = 0{,}30+8 = 8{,}30\ \text{mm} "
                       r"\Rightarrow k_d' = 1+\sqrt{1+\frac{100}{8{,}30}} = 1+3{,}61 = 4{,}61",
                       "Amortizator statik cho'kishni 28 marta oshirdi."),
                    st(r"\sigma_d' = 4{,}61\cdot8{,}0 = 36{,}9\ \text{MPa}",
                       "Kuchlanish 4,2 marta kamaydi!"),
                ],
                answer=(
                    "Amortizatorsiz: $k_d = 19{,}3$, $\\sigma_d = 154{,}4$ MPa; "
                    "amortizator bilan: $k_d = 4{,}61$, $\\sigma_d = 36{,}9$ MPa."
                ),
                engineering_note=(
                    "8 mm qalinlikdagi rezina qatlam kuchlanishni 4,2 marta "
                    "kamaytirdi — bu metall sarfini oshirmasdan erishilgan "
                    "natija. Aynan shu prinsip avtomobil podveskasi, mashina "
                    "fundamenti va qadoqlash materiallarida ishlatiladi: "
                    "zarbani 'yumshatish' uchun deformatsiya masofasini "
                    "oshirish kerak."
                ),
            ),
            computation=Computation(
                caption=(
                    "Zarbiy yuklanish: balandlik va amortizatsiyani o'zgartirib, "
                    "dinamiklik koeffitsientini kuzating."
                ),
                code='''"""Zarbiy yuklanish va dinamiklik koeffitsienti."""
import numpy as np
from labkit import PARAMS, note, series, table, value

m = float(PARAMS.get("m", 200.0))        # yuk massasi, kg
h = float(PARAMS.get("h", 50.0))*1e-3    # tushish balandligi, m
L = float(PARAMS.get("L", 3.0))          # balka oralig'i, m
I = float(PARAMS.get("I", 1840.0))*1e-8  # inersiya momenti, m^4
W = float(PARAMS.get("W", 184.0))*1e-6   # qarshilik momenti, m^3
E = float(PARAMS.get("E", 200e9))
d_amort = float(PARAMS.get("d_amort", 0.0))*1e-3   # amortizator cho'kishi, m
g = 9.81

P = m*g
d_st = P*L**3/(48*E*I) + d_amort
kd = 1 + np.sqrt(1 + 2*h/d_st) if d_st > 0 else np.inf
s_st = (P*L/4)/W
s_d = kd*s_st

value("Statik yuk P", P, "N")
value("Statik cho'kish δ_st", d_st*1000, "mm")
value("Dinamiklik koeffitsienti k_d", kd, "—")
value("Statik kuchlanish", s_st/1e6, "MPa")
value("Dinamik kuchlanish", s_d/1e6, "MPa")
value("Dinamik cho'kish", kd*d_st*1000, "mm")
value("Zarba tezligi", np.sqrt(2*g*h), "m/s")

# Balandlikning ta'siri
hh = np.linspace(0, 0.5, 200)
kd_arr = 1 + np.sqrt(1 + 2*hh/d_st)
series("k_d(h)", (hh*1000).tolist(), kd_arr.tolist(),
       xlabel="Tushish balandligi h, mm", ylabel="k_d")
note(f"h = 0 (to'satdan qo'yish) da ham k_d = 2 — statik hisobdan 2 marta ko'p.")

# Amortizatsiyaning ta'siri
dd = np.linspace(0, 0.05, 200)
d_base = P*L**3/(48*E*I)
kd_amort = 1 + np.sqrt(1 + 2*h/(d_base + dd))
series("k_d(amortizator qalinligi)", (dd*1000).tolist(), kd_amort.tolist(),
       xlabel="Amortizator cho'kishi, mm", ylabel="k_d")
series("σ_d(amortizator)", (dd*1000).tolist(), (kd_amort*s_st/1e6).tolist(),
       xlabel="Amortizator cho'kishi, mm", ylabel="σ_d, MPa")

# Bikrlikning paradoksal ta'siri
II = np.linspace(500e-8, 10000e-8, 150)
d_st_arr = P*L**3/(48*E*II)
kd_stiff = 1 + np.sqrt(1 + 2*h/d_st_arr)
W_arr = II/(0.1)                       # taxminiy W = I/(h/2), h≈200mm
s_d_arr = kd_stiff*(P*L/4)/W_arr/1e6
series("σ_d(inersiya momenti)", (II*1e8).tolist(), s_d_arr.tolist(),
       xlabel="I, cm⁴", ylabel="σ_d, MPa")
note("Diqqat: bikrlikni oshirish k_d ni oshiradi, lekin σ_st ni kamaytiradi — "
     "natijada σ_d kamayadi, lekin statik holatdagidek tez emas.")

table("Xarakterli hollar",
      ["Holat", "Formula", "k_d"],
      [["Statik qo'yish", "—", 1.0],
       ["To'satdan qo'yish (h=0)", "1+√1", 2.0],
       ["h = δ_st", "1+√3", 2.73],
       ["h = 10δ_st", "1+√21", 5.58],
       ["h = 100δ_st", "1+√201", 15.2],
       ["Joriy holat", f"h/δ_st = {h/d_st:.1f}", float(kd)]])

table("Zarbani kamaytirish usullari",
      ["Usul", "Ta'sir", "Amaliy misol"],
      [["Amortizator qo'yish", "δ_st ↑, k_d ↓↓", "Rezina qatlam, prujina"],
       ["Balandlikni kamaytirish", "h ↓, k_d ↓", "Yumshoq tushirish"],
       ["Konstruksiyani yumshatish", "δ_st ↑, k_d ↓", "Uzunroq/yupqaroq element"],
       ["Massani kamaytirish", "σ_st ↓", "Yengil yuk"]])
''',
                parameters=[
                    p("m", "Yuk massasi m", 1.0, 5000.0, 200.0, 10.0, "kg"),
                    p("h", "Tushish balandligi h", 0.0, 1000.0, 50.0, 5.0, "mm"),
                    p("L", "Balka oralig'i L", 0.5, 15.0, 3.0, 0.5, "m"),
                    p("I", "Inersiya momenti I", 100.0, 50000.0, 1840.0, 100.0, "cm⁴"),
                    p("W", "Qarshilik momenti W", 10.0, 5000.0, 184.0, 10.0, "cm³"),
                    p("d_amort", "Amortizator cho'kishi", 0.0, 50.0, 0.0, 1.0, "mm"),
                ],
                expected_output="δ_st = 0,30 mm, k_d = 19,3, σ_d = 154,4 MPa",
            ),
            visualization=vis(
                "Dinamiklik koeffitsienti va amortizatsiya",
                "React/SVG",
                "$k_d(h)$ egri chizig'i (kvadrat ildiz shaklida) va "
                "$k_d$(amortizator) grafigi; ikkinchisida keskin pasayish "
                "ko'rinadi. Yonida zarba jarayonining energiya diagrammasi.",
                "React/SVG: ikki grafikni yonma-yon qo'yish asosiy muhandislik "
                "xulosasini beradi — amortizatsiya balandlikni kamaytirishdan "
                "ko'ra samaraliroq. Energiya diagrammasi esa fizik mexanizmni "
                "tushuntiradi.",
            ),
            interpretation=(
                "$k_d(h)$ kvadrat ildiz shaklida o'sadi — balandlikni 4 marta "
                "oshirish $k_d$ ni taxminan 2 marta oshiradi. Amortizator "
                "grafigi esa keskin pasayadi: dastlabki bir necha millimetr "
                "eng katta samarani beradi. Bu — qadoqlash va himoya "
                "vositalarini loyihalashning asosi."
            ),
            common_mistakes=[
                "$h = 0$ da $k_d = 1$ deb o'ylash — aslida 2.",
                "$\\delta_{st}$ ni zarba joyidagi emas, boshqa nuqtadagi "
                "cho'kish deb olish.",
                "Konstruksiya massasini hisobga olmaslik (u katta bo'lsa "
                "keltirilgan massa koeffitsienti kerak).",
                "Zarbani kamaytirish uchun konstruksiyani qattiqroq qilish — "
                "bu $k_d$ ni oshiradi.",
            ],
            quiz=[
                q("Nima uchun $h = 0$ da $k_d = 2$?",
                  "Yuk to'satdan qo'yilganda u muvozanat holatidan o'tib ketadi "
                  "va tebranadi; maksimal ko'chish statikdan 2 marta katta.",
                  "konseptual"),
                q("$\\delta_{st} = 1$ mm, $h = 100$ mm. $k_d$?",
                  "$k_d = 1+\\sqrt{1+200} = 1+14{,}18 = 15{,}2$.", "hisob"),
                q("Amortizator $\\delta_{st}$ ni 10 marta oshirsa, $k_d$ qanday "
                  "o'zgaradi (katta $h$ da)?",
                  "Taxminan $\\sqrt{10} = 3{,}16$ marta kamayadi.", "hisob"),
                q("Nima uchun qattiq konstruksiya zarbaga yomonroq chidaydi?",
                  "Qattiq konstruksiyada $\\delta_{st}$ kichik, demak $k_d$ katta. "
                  "Energiya kichik masofada yutilishi kerak — kuch ortadi.",
                  "talqin"),
                q("Kodda `d_st = ... + d_amort` nima uchun qo'shiladi?",
                  "Amortizator va balka ketma-ket ulangan prujinalar kabi: "
                  "umumiy cho'kish ularning yig'indisiga teng.", "kod"),
            ],
            bridge_to_next=(
                "Bir martalik zarbani ko'rdik. Lekin ko'p konstruksiyalar "
                "millionlab marta takrorlanuvchi yuk ostida ishlaydi — "
                "keyingi mavzu charchash haqida."
            ),
            research_extension=(
                "Energetik nazariyaning chegarasini tekshiring: uni to'lqin "
                "nazariyasi bilan taqqoslang. Zarba paytida deformatsiya "
                "to'lqini sterjen bo'ylab $c = \\sqrt{E/\\rho}$ tezlikda "
                "tarqaladi. Agar zarba davomiyligi to'lqinning sterjen "
                "bo'ylab o'tish vaqtidan kichik bo'lsa, energetik nazariya "
                "xato beradi. Bu shartni miqdoriy ifodalang."
            ),
        ),
    ),
    Topic(
        id="mq-28",
        subject_id=S,
        module_id=M,
        order=28,
        title="Siklik yuklanish, charchash va chidamlilik chegarasi",
        description=(
            "Siklik yuklanish tavsiflari, Vyoler egri chizig'i, chidamlilik "
            "chegarasi, charchashga hisoblash va omillarning ta'siri."
        ),
        learning_objective=(
            "Siklik yuklangan detalni charchashga hisoblash va chidamlilik "
            "zaxirasini aniqlash."
        ),
        prerequisites=["mq-23", "mq-04"],
        mathematical_core=(
            "Sikl tavsiflari, Vyoler egri chizig'i (logarifmik), Xay "
            "diagrammasi, Palmgren–Mayner gipotezasi."
        ),
        engineering_application=(
            "Vallar, prujinalar, samolyot konstruksiyalari, ko'priklar, "
            "podshipniklar."
        ),
        computational_component=(
            "Vyoler egri chizig'ini qurish, chidamlilik zaxirasini hisoblash "
            "va yig'ilgan shikastlanishni baholash."
        ),
        visualization_component=(
            "Vyoler egri chizig'i va sikl diagrammasi; Xay diagrammasi."
        ),
        research_extension=(
            "Palmgren–Mayner gipotezasining chegaralari: o'zgaruvchan "
            "amplitudali yuklanishda shikastlanish yig'indisi."
        ),
        difficulty="murakkab",
        previous_link=(
            "mq-23 dagi val hisobida $[\\sigma]$ ni past oldik — sabab aynan "
            "charchash. Endi uni to'g'ridan-to'g'ri hisoblashni o'rganamiz."
        ),
        next_topic="mq-29",
        estimated_minutes=90,
        tags=["charchash", "Vyoler egri chizig'i", "chidamlilik"],
        lesson=Lesson(
            physical_problem=(
                "Aylanuvchi valdagi nuqta har aylanishda cho'zilishdan siqilishga "
                "o'tadi. 3000 ayl/min da bu kuniga 4,3 million sikl. Val "
                "statik mustahkamlikdan ancha past kuchlanishda ham bir necha "
                "oydan keyin sinishi mumkin. Bu — charchash va u mashina "
                "detallarining 80 % buzilishiga sabab bo'ladi."
            ),
            concepts=[
                c("Sikl tavsiflari", "$\\sigma_{max}$, $\\sigma_{min}$, "
                  "o'rtacha $\\sigma_m = (\\sigma_{max}+\\sigma_{min})/2$, "
                  "amplituda $\\sigma_a = (\\sigma_{max}-\\sigma_{min})/2$, "
                  "assimetriya $r = \\sigma_{min}/\\sigma_{max}$."),
                c("Simmetrik sikl", "$r = -1$: $\\sigma_m = 0$ — aylanuvchi "
                  "valdagi egilish uchun tipik va eng xavfli."),
                c("Vyoler egri chizig'i", "$\\sigma_a$–$N$ bog'lanishi; "
                  "$\\sigma_a^m N = \\text{const}$."),
                c("Chidamlilik chegarasi $\\sigma_{-1}$", "Cheksiz ko'p siklga "
                  "chidaydigan maksimal amplituda; po'lat uchun "
                  "$\\approx 0{,}4...0{,}5\\sigma_B$."),
                c("Ta'sir etuvchi omillar", "Kuchlanish konsentratsiyasi "
                  "$K_\\sigma$, o'lchamlar $\\varepsilon_\\sigma$, sirt sifati "
                  "$\\beta$ — ular chidamlilikni sezilarli pasaytiradi."),
            ],
            derivation=[
                d("1-qadam. Sikl tavsiflarini kiritish",
                  r"\sigma_m = \frac{\sigma_{max}+\sigma_{min}}{2},\quad "
                  r"\sigma_a = \frac{\sigma_{max}-\sigma_{min}}{2},\quad "
                  r"r = \frac{\sigma_{min}}{\sigma_{max}}",
                  "Har qanday sikl ikki parametr bilan to'liq tavsiflanadi."),
                d("2-qadam. Vyoler egri chizig'i",
                  r"\sigma_a^m N = C \;\Rightarrow\; \log\sigma_a = \frac{1}{m}(\log C - \log N)",
                  "Logarifmik koordinatalarda to'g'ri chiziq. $m = 6...12$ "
                  "(po'lat uchun odatda 9). $N > N_0 = 10^7$ da gorizontal "
                  "bo'lib qoladi — bu chidamlilik chegarasi."),
                d("3-qadam. Konstruktiv omillarni hisobga olish",
                  r"\sigma_{-1D} = \frac{\varepsilon_\sigma\,\beta}{K_\sigma}\,\sigma_{-1}",
                  "Detal uchun chidamlilik chegarasi laboratoriya namunasinikidan "
                  "2–4 marta past bo'lishi mumkin."),
                d("4-qadam. Chidamlilik zaxirasi",
                  r"\boxed{\;n_\sigma = \frac{\sigma_{-1D}}{\sigma_a + \psi_\sigma\sigma_m}\;}",
                  "$\\psi_\\sigma$ — sikl assimetriyasiga sezgirlik koeffitsienti "
                  "(po'lat uchun 0,1–0,2). Simmetrik siklda "
                  "$n_\\sigma = \\sigma_{-1D}/\\sigma_a$."),
                d("5-qadam. Yig'ilgan shikastlanish (Palmgren–Mayner)",
                  r"\sum_i\frac{n_i}{N_i} = 1 \;\Rightarrow\; \text{buzilish}",
                  "O'zgaruvchan amplitudali yuklanishda har bir daraja o'z "
                  "hissasini qo'shadi. Amalda chegara 0,3–1,5 oralig'ida "
                  "o'zgaradi."),
            ],
            formula_meaning=(
                "Charchash statik mustahkamlikdan tubdan farq qiladi: buzilish "
                "kuchlanish chegaradan oshgani uchun emas, mikroyoriqlarning "
                "asta-sekin o'sishi natijasida yuz beradi. $\\sigma_{-1} "
                "\\approx 0{,}45\\sigma_B$ — demak siklik yuklanishda "
                "materialning yarmidan kamrog'idan foydalanish mumkin. "
                "$K_\\sigma$ esa ko'rsatadiki, geometriya (galtel, teshik, "
                "shpon) charchash mustahkamligiga materialdan ko'ra ko'proq "
                "ta'sir qiladi."
            ),
            equations=[
                eq(r"\sigma_a^m N = C", "Vyoler egri chizig'i (chegaraviy chidamlilik).",
                   "Vyoler tenglamasi"),
                eq(r"\sigma_{-1D} = \frac{\varepsilon_\sigma\beta}{K_\sigma}\sigma_{-1}",
                   "Detal uchun chidamlilik chegarasi.", "Detal chidamliligi"),
                eq(r"n_\sigma = \frac{\sigma_{-1D}}{\sigma_a+\psi_\sigma\sigma_m}",
                   "Chidamlilik zaxirasi.", "Zaxira"),
                eq(r"\sum\frac{n_i}{N_i} = 1", "Palmgren–Mayner shikastlanish gipotezasi.",
                   "Shikastlanish"),
            ],
            conditions=(
                "Hisob chiziqli yig'ilish gipotezasiga asoslanadi va u "
                "taqribiy. Korroziya, yuqori temperatura va kontakt "
                "kuchlanishlar chidamlilikni keskin pasaytiradi. "
                "Mas'uliyatli detallarda (aviatsiya) hisobdan tashqari "
                "tajribaviy sinov va muntazam nazorat talab qilinadi."
            ),
            worked_example=WorkedExample(
                statement=(
                    "Val diametri $d = 45$ mm, galtel radiusi $r = 3$ mm, "
                    "keyingi diametr $D = 55$ mm. Eguvchi moment "
                    "$M = 380$ N·m (aylanuvchi val — simmetrik sikl). "
                    "Material: $\\sigma_B = 750$ MPa, $\\sigma_{-1} = 340$ MPa. "
                    "$K_\\sigma = 1{,}75$, $\\varepsilon_\\sigma = 0{,}82$, "
                    "$\\beta = 0{,}9$. Chidamlilik zaxirasini toping."
                ),
                given=[r"d = 45\ \text{mm},\; M = 380\ \text{N·m}",
                       r"\sigma_{-1} = 340\ \text{MPa},\; K_\sigma = 1{,}75,\; "
                       r"\varepsilon_\sigma = 0{,}82,\; \beta = 0{,}9"],
                steps=[
                    st(r"W = \frac{\pi d^3}{32} = \frac{\pi\cdot 9{,}1125\cdot10^{-5}}{32} = "
                       r"8{,}946\cdot10^{-6}\ \text{m}^3",
                       "Qarshilik momenti."),
                    st(r"\sigma_a = \frac{M}{W} = \frac{380}{8{,}946\cdot10^{-6}} = 42{,}5\ \text{MPa}",
                       "Aylanuvchi valda egilish kuchlanishi to'liq siklik "
                       "o'zgaradi: $\\sigma_a = \\sigma_{max}$, $\\sigma_m = 0$."),
                    st(r"\sigma_{-1D} = \frac{\varepsilon_\sigma\beta}{K_\sigma}\sigma_{-1} = "
                       r"\frac{0{,}82\cdot0{,}9}{1{,}75}\cdot340 = \frac{0{,}738}{1{,}75}\cdot340",
                       "Detal uchun chidamlilik chegarasi."),
                    st(r"\sigma_{-1D} = 0{,}4217\cdot340 = 143{,}4\ \text{MPa}",
                       "Laboratoriya qiymatidan 2,37 marta past!"),
                    st(r"n_\sigma = \frac{143{,}4}{42{,}5} = 3{,}37",
                       "Chidamlilik zaxirasi. Me'yoriy talab odatda "
                       "$[n] = 1{,}5...2{,}5$ — bajarildi."),
                    st(r"\text{Galtel radiusini } r = 5\ \text{mm ga oshirsak: } K_\sigma \approx 1{,}5 "
                       r"\Rightarrow \sigma_{-1D} = 167{,}3\ \text{MPa},\; n_\sigma = 3{,}94",
                       "Radiusni 2 mm oshirish zaxirani 17 % oshirdi — "
                       "bepul yaxshilanish."),
                ],
                answer=(
                    "$\\sigma_a = 42{,}5$ MPa; $\\sigma_{-1D} = 143{,}4$ MPa; "
                    "$n_\\sigma = 3{,}37$ (me'yordan yuqori)."
                ),
                engineering_note=(
                    "Konsentratsiya, o'lcham va sirt omillari birgalikda "
                    "chidamlilikni 2,37 marta pasaytirdi. Bu — charchash "
                    "hisobining eng muhim xulosasi: detal geometriyasi va "
                    "ishlov berish sifati materialdan ko'ra muhimroq. "
                    "Galtel radiusini oshirish, sirtni silliqlash va "
                    "yuza mustahkamlash (nagartovka) eng samarali chora."
                ),
            ),
            computation=Computation(
                caption=(
                    "Charchash hisobi: Vyoler egri chizig'i, zaxira va "
                    "yig'ilgan shikastlanishni baholang."
                ),
                code='''"""Charchash: Vyoler egri chizig'i va chidamlilik zaxirasi."""
import numpy as np
from labkit import PARAMS, note, series, table, value

d = float(PARAMS.get("d", 45.0))*1e-3     # val diametri, m
M = float(PARAMS.get("M", 380.0))         # eguvchi moment, N*m
s_B = float(PARAMS.get("sB", 750.0))      # mustahkamlik chegarasi, MPa
s_m1 = float(PARAMS.get("s_m1", 340.0))   # chidamlilik chegarasi, MPa
K_s = float(PARAMS.get("Ks", 1.75))       # konsentratsiya koeffitsienti
eps_s = float(PARAMS.get("eps", 0.82))    # o'lcham koeffitsienti
beta = float(PARAMS.get("beta", 0.9))     # sirt sifati koeffitsienti
m_w = 9.0                                  # Vyoler egri chizig'i ko'rsatkichi
N0 = 1e7                                   # bazaviy sikllar soni

W = np.pi*d**3/32
s_a = M/W/1e6
s_1D = eps_s*beta/K_s*s_m1
n_sigma = s_1D/s_a

value("Qarshilik momenti W", W*1e6, "cm³")
value("Amplituda σ_a", s_a, "MPa")
value("σ_-1 (namuna)", s_m1, "MPa")
value("σ_-1D (detal)", s_1D, "MPa")
value("Pasayish koeffitsienti", s_m1/s_1D, "marta")
value("Chidamlilik zaxirasi n_σ", n_sigma, "—")
note("Chidamlilik sharti BAJARILDI ✓" if n_sigma >= 1.5
     else "DIQQAT: chidamlilik zaxirasi yetarli emas!")
note(f"σ_-1/σ_B = {s_m1/s_B:.3f} — po'lat uchun tipik qiymat 0,4–0,5")

# Vyoler egri chizig'i
C = s_1D**m_w*N0
NN = np.logspace(3, 8, 200)
s_N = (C/NN)**(1/m_w)
s_N = np.minimum(s_N, s_B)
s_N = np.where(NN > N0, s_1D, s_N)
series("Vyoler egri chizig'i", np.log10(NN).tolist(), s_N.tolist(),
       xlabel="log₁₀(N)", ylabel="σ_a, MPa")
series("Ish nuqtasi", [np.log10(N0)], [s_a], xlabel="log₁₀(N)", ylabel="σ_a, MPa")

# Berilgan amplitudada resurs
for sa_test in (s_a, s_1D*1.2, s_1D*1.5, s_1D*2.0):
    if sa_test > s_1D:
        N_life = C/sa_test**m_w
        note(f"σ_a = {sa_test:.1f} MPa da resurs: N = {N_life:.3e} sikl "
             f"({N_life/(3000*60*24):.1f} kun, 3000 ayl/min da)")
    else:
        note(f"σ_a = {sa_test:.1f} MPa ≤ σ_-1D — cheksiz resurs")

# Galtel radiusining ta'siri
KK = np.linspace(1.0, 3.0, 100)
series("n_σ(K_σ)", KK.tolist(), (eps_s*beta/KK*s_m1/s_a).tolist(),
       xlabel="Konsentratsiya koeffitsienti K_σ", ylabel="n_σ")
note("K_σ ni 1,75 dan 1,5 ga kamaytirish (galtel radiusini oshirish) "
     f"zaxirani {(1.75/1.5-1)*100:.0f} % oshiradi.")

# Palmgren–Mayner: o'zgaruvchan amplitudali yuklanish
blocks = [(1.4*s_1D, 1e5), (1.2*s_1D, 5e5), (1.0*s_1D, 2e6), (0.8*s_1D, 1e7)]
damage = 0.0
rows = []
for sa_i, n_i in blocks:
    N_i = C/sa_i**m_w if sa_i > s_1D else np.inf
    dmg = n_i/N_i if np.isfinite(N_i) else 0.0
    damage += dmg
    rows.append([float(sa_i), float(n_i), float(N_i) if np.isfinite(N_i) else "∞", float(dmg)])
table("Yig'ilgan shikastlanish (Palmgren–Mayner)",
      ["σ_a, MPa", "n_i (sikl)", "N_i (resurs)", "n_i/N_i"], rows)
value("Umumiy shikastlanish D", damage, "—")
note(f"D = {damage:.4f}; D = 1 da buzilish kutiladi. "
     f"Qolgan resurs: {(1-damage)*100:.1f} %")

table("Chidamlilikka ta'sir etuvchi omillar",
      ["Omil", "Belgi", "Tipik qiymat", "Ta'sir"],
      [["Kuchlanish konsentratsiyasi", "K_σ", "1.2–3.0", "Pasaytiradi"],
       ["Detal o'lchami", "ε_σ", "0.6–1.0", "Pasaytiradi"],
       ["Sirt sifati", "β", "0.6–1.0", "Pasaytiradi"],
       ["Yuza mustahkamlash", "β", "1.2–2.0", "Oshiradi"],
       ["Korroziya", "β", "0.2–0.6", "Keskin pasaytiradi"]])
''',
                parameters=[
                    p("d", "Val diametri d", 10.0, 300.0, 45.0, 1.0, "mm"),
                    p("M", "Eguvchi moment M", 10.0, 20000.0, 380.0, 10.0, "N·m"),
                    p("sB", "Mustahkamlik σ_B", 200.0, 2000.0, 750.0, 10.0, "MPa"),
                    p("s_m1", "Chidamlilik σ_-1", 80.0, 900.0, 340.0, 10.0, "MPa"),
                    p("Ks", "Konsentratsiya K_σ", 1.0, 3.5, 1.75, 0.05, "—"),
                    p("eps", "O'lcham koeff. ε_σ", 0.5, 1.0, 0.82, 0.02, "—"),
                    p("beta", "Sirt koeff. β", 0.4, 2.0, 0.9, 0.05, "—"),
                ],
                expected_output="σ_a = 42,5 MPa, σ_-1D = 143,4 MPa, n_σ = 3,37",
            ),
            visualization=vis(
                "Vyoler egri chizig'i va sikl diagrammasi",
                "React/SVG",
                "Logarifmik o'qlarda Vyoler egri chizig'i; gorizontal qismi "
                "chidamlilik chegarasi. Yonida sikl diagrammasi "
                "($\\sigma$–$t$) $\\sigma_{max}$, $\\sigma_{min}$, "
                "$\\sigma_m$, $\\sigma_a$ belgilari bilan.",
                "React/SVG: logarifmik shkala majburiy (sikllar soni "
                "$10^3$–$10^8$). Ish nuqtasini egri chiziqda ko'rsatish "
                "resursni vizual baholash imkonini beradi.",
            ),
            interpretation=(
                "Vyoler egri chizig'i $N > 10^7$ da gorizontal bo'lib qoladi — "
                "bu chidamlilik chegarasi va undan past amplitudada detal "
                "cheksiz ishlaydi (po'lat uchun; alyuminiyda bunday chegara "
                "yo'q). $n_\\sigma(K_\\sigma)$ grafigi esa konstruktiv "
                "yaxshilanishning kuchini ko'rsatadi: galtel radiusini "
                "oshirish materialni almashtirishdan arzonroq va samaraliroq."
            ),
            common_mistakes=[
                "Statik mustahkamlik chegarasini charchash hisobida ishlatish.",
                "Konsentratsiya, o'lcham va sirt omillarini e'tiborsiz "
                "qoldirish — ular chidamlilikni 2–4 marta pasaytiradi.",
                "Alyuminiy uchun chidamlilik chegarasi mavjud deb hisoblash — "
                "rangli metallarda Vyoler egri chizig'i gorizontal bo'lmaydi.",
                "Simmetrik bo'lmagan siklda $\\sigma_m$ ni hisobga olmaslik.",
            ],
            quiz=[
                q("Nima uchun aylanuvchi valda sikl simmetrik?",
                  "Val aylanganda ma'lum nuqta navbat bilan cho'zilgan va "
                  "siqilgan zonaga tushadi: $\\sigma_{max} = -\\sigma_{min}$, "
                  "$\\sigma_m = 0$.", "konseptual"),
                q("$\\sigma_B = 600$ MPa. $\\sigma_{-1}$ ni baholang.",
                  "$\\sigma_{-1} \\approx 0{,}45\\sigma_B = 270$ MPa.", "hisob"),
                q("$K_\\sigma = 2$, $\\varepsilon = 0{,}8$, $\\beta = 0{,}9$, "
                  "$\\sigma_{-1} = 300$ MPa. $\\sigma_{-1D}$?",
                  "$\\sigma_{-1D} = 0{,}8\\cdot0{,}9/2\\cdot300 = 108$ MPa.", "hisob"),
                q("Nima uchun charchash buzilishi to'satdan ko'rinadi?",
                  "Mikroyoriq asta-sekin o'sadi va tashqaridan ko'rinmaydi; "
                  "kesim kritik darajada kamayganda esa qolgan qism birdan "
                  "sinadi.", "talqin"),
                q("Kodda Palmgren–Mayner yig'indisi nimani anglatadi?",
                  "Har bir yuklanish darajasi o'z resursining bir qismini "
                  "'yeydi'; yig'indi 1 ga yetganda buzilish kutiladi.", "kod"),
            ],
            bridge_to_next=(
                "Charchash hisobida konsentratsiya koeffitsienti hal qiluvchi "
                "rol o'ynadi. Keyingi mavzuda uning tabiatini batafsil "
                "ko'ramiz."
            ),
            research_extension=(
                "Rainflow (yomg'ir oqimi) algoritmini amalga oshiring: real "
                "o'lchangan kuchlanish tarixidan (tasodifiy signal) sikllarni "
                "ajratish. So'ngra Palmgren–Mayner bo'yicha shikastlanishni "
                "hisoblang. Bu — zamonaviy charchash tahlilining standart "
                "usuli (avtomobil va aviatsiya sanoatida)."
            ),
        ),
    ),
    Topic(
        id="mq-29",
        subject_id=S,
        module_id=M,
        order=29,
        title="Kuchlanish konsentratsiyasi va konstruktiv elementlarning ishonchliligi",
        description=(
            "Kuchlanish konsentratsiyasi manbalari, nazariy va effektiv "
            "koeffitsientlar, konsentratsiyani kamaytirish usullari."
        ),
        learning_objective=(
            "Kuchlanish konsentratsiyasini baholash va uni kamaytiruvchi "
            "konstruktiv yechimlarni tanlash."
        ),
        prerequisites=["mq-28", "mq-19"],
        mathematical_core=(
            "Nazariy konsentratsiya koeffitsienti, sezgirlik koeffitsienti, "
            "Kirsh yechimi (teshikli plastina)."
        ),
        engineering_application=(
            "Galtellar, teshiklar, shpon kanallari, rezbalar, payvand "
            "choklar."
        ),
        computational_component=(
            "Teshikli plastina atrofidagi kuchlanish maydonini analitik "
            "(Kirsh) hisoblash va konsentratsiyani baholash."
        ),
        visualization_component=(
            "Teshik atrofidagi kuchlanish maydoni; konsentratsiya "
            "koeffitsientining geometriyaga bog'liqligi."
        ),
        research_extension=(
            "Optimal galtel shakli: nima uchun ellipssimon o'tish "
            "doiraviydan yaxshiroq?"
        ),
        difficulty="murakkab",
        previous_link=(
            "mq-28 da $K_\\sigma$ ni jadvaldan oldik. Endi uning fizik "
            "tabiatini va analitik asosini ko'ramiz."
        ),
        next_topic="mq-30",
        estimated_minutes=85,
        tags=["konsentratsiya", "Kirsh yechimi", "galtel"],
        lesson=Lesson(
            physical_problem=(
                "Plastinada teshik ochilsa, kesim yuzasi kamayadi — bu "
                "kutilgan. Lekin teshik chekkasidagi kuchlanish o'rtacha "
                "qiymatdan 3 marta katta bo'ladi va bu kesim kamayishi bilan "
                "tushuntirilmaydi. Nima uchun? Chunki kuchlanish 'oqimi' "
                "to'siqni aylanib o'tishga majbur va u yerda 'zichlashadi'."
            ),
            concepts=[
                c("Kuchlanish konsentratsiyasi", "Geometriya keskin "
                  "o'zgaradigan joylarda kuchlanishning mahalliy ortishi."),
                c("Nazariy koeffitsient", "$K_t = \\sigma_{max}/\\sigma_{nom}$ — "
                  "elastik yechimdan olinadi, materialdan bog'liq emas."),
                c("Effektiv koeffitsient", "$K_\\sigma = \\sigma_{-1}/\\sigma_{-1D}$ — "
                  "charchash sinovlaridan; odatda $K_\\sigma < K_t$."),
                c("Sezgirlik koeffitsienti", "$q = (K_\\sigma-1)/(K_t-1)$ — "
                  "materialning konsentratsiyaga sezgirligi; plastik "
                  "materiallarda kichik."),
                c("Kirsh yechimi", "Cheksiz plastinada dumaloq teshik uchun "
                  "aniq elastik yechim: $K_t = 3$."),
            ],
            derivation=[
                d("1-qadam. Kirsh yechimi (teshikli plastina)",
                  r"\sigma_\theta(r,\theta) = \frac{\sigma}{2}\left[\left(1+\frac{a^2}{r^2}\right) - "
                  r"\left(1+\frac{3a^4}{r^4}\right)\cos2\theta\right]",
                  "Cheksiz plastina, radiusi $a$ bo'lgan teshik, bir o'qli "
                  "cho'zilish $\\sigma$. Elastiklik nazariyasidan (tmm-17)."),
                d("2-qadam. Maksimal kuchlanishni topish",
                  r"r = a,\ \theta = 90^\circ:\ \sigma_\theta = \frac{\sigma}{2}[2 - (4)(-1)] = 3\sigma "
                  r"\;\Rightarrow\; \boxed{\;K_t = 3\;}",
                  "Teshik chekkasida, yuklanishga perpendikular nuqtada. "
                  "Bu natija teshik o'lchamidan bog'liq emas!"),
                d("3-qadam. Konsentratsiyaning lokal xarakteri",
                  r"r = 3a:\ \sigma_\theta \approx 1{,}07\sigma",
                  "Teshikdan uch radius masofada kuchlanish deyarli nominal "
                  "qiymatga qaytadi — konsentratsiya juda lokal hodisa."),
                d("4-qadam. Effektiv koeffitsient va sezgirlik",
                  r"K_\sigma = 1 + q(K_t-1)",
                  "$q = 0$ (sezgir emas) — plastik material, mahalliy oqish "
                  "kuchlanishni tenglashtiradi; $q = 1$ (to'liq sezgir) — "
                  "mo'rt material. Po'lat uchun $q = 0{,}6...0{,}9$."),
            ],
            formula_meaning=(
                "$K_t = 3$ natijasi ajoyib: u teshik o'lchamiga bog'liq emas. "
                "Kichik teshik ham, katta teshik ham bir xil konsentratsiya "
                "beradi. Muhimi — o'tish radiusi: o'tkir burchak "
                "($r \\to 0$) da $K_t \\to \\infty$. Shuning uchun "
                "konstruktorlikning oltin qoidasi: o'tkir burchaklardan "
                "qoching, radiuslarni oshiring. Plastik materialda esa "
                "mahalliy oqish konsentratsiyani 'yumshatadi' — bu ularning "
                "yana bir afzalligi."
            ),
            equations=[
                eq(r"K_t = \frac{\sigma_{max}}{\sigma_{nom}}", "Nazariy konsentratsiya "
                   "koeffitsienti.", "Nazariy koeffitsient"),
                eq(r"K_t = 3\ (\text{dumaloq teshik, cho'zilish})", "Kirsh natijasi.",
                   "Kirsh yechimi"),
                eq(r"K_\sigma = 1+q(K_t-1)", "Effektiv koeffitsient.", "Effektiv koeffitsient"),
            ],
            conditions=(
                "Kirsh yechimi cheksiz plastina uchun; teshik diametri "
                "plastina kengligining 20 % idan oshsa, tuzatish kerak. "
                "Statik yuklanishda plastik material konsentratsiyaga kam "
                "sezgir (mahalliy oqish tenglashtiradi), siklik yuklanishda "
                "esa juda sezgir — shuning uchun konsentratsiya asosan "
                "charchash hisobida muhim."
            ),
            worked_example=WorkedExample(
                statement=(
                    "Plastina eni $b = 120$ mm, qalinligi $t = 10$ mm, "
                    "markazida $d = 30$ mm teshik. Cho'zuvchi kuch "
                    "$F = 90$ kN. Nominal va maksimal kuchlanishni toping. "
                    "Teshik o'rniga ikki kichik teshik ($d = 15$ mm) qo'ysak, "
                    "nima o'zgaradi?"
                ),
                given=[r"b = 0{,}12\ \text{m},\; t = 0{,}01\ \text{m},\; d = 0{,}03\ \text{m}",
                       r"F = 90\ \text{kN}"],
                steps=[
                    st(r"A_{net} = (b-d)t = (0{,}12-0{,}03)\cdot0{,}01 = 9\cdot10^{-4}\ \text{m}^2",
                       "Zaiflashgan kesim yuzasi."),
                    st(r"\sigma_{nom} = \frac{F}{A_{net}} = \frac{90\,000}{9\cdot10^{-4}} = 100\ \text{MPa}",
                       "Nominal kuchlanish (o'rtacha zaiflashgan kesimda)."),
                    st(r"d/b = 0{,}25 \Rightarrow K_t \approx 2{,}45\ (\text{jadvaldan, chekli kenglik})",
                       "Cheksiz plastinada $K_t = 3$, chekli kenglikda kamroq."),
                    st(r"\sigma_{max} = K_t\sigma_{nom} = 2{,}45\cdot100 = 245\ \text{MPa}",
                       "Teshik chekkasidagi maksimal kuchlanish."),
                    st(r"\text{Ikki teshik } d = 15: A_{net} = (0{,}12-0{,}03)\cdot0{,}01 = "
                       r"9\cdot10^{-4}\ \text{m}^2 \Rightarrow \sigma_{nom} = 100\ \text{MPa}",
                       "Zaiflashgan yuza bir xil qoldi."),
                    st(r"d/b = 0{,}125 \Rightarrow K_t \approx 2{,}7 \Rightarrow "
                       r"\sigma_{max} = 270\ \text{MPa}",
                       "Kichik teshiklar YOMONROQ: $K_t$ 3 ga yaqinlashadi. "
                       "Demak bir katta teshik ikki kichikdan afzal."),
                ],
                answer=(
                    "$\\sigma_{nom} = 100$ MPa, $\\sigma_{max} = 245$ MPa "
                    "($K_t = 2{,}45$); ikki kichik teshikda $\\sigma_{max} = 270$ MPa "
                    "— yomonroq."
                ),
                engineering_note=(
                    "Bu qarshi-intuitiv natija: teshik yuzasini bir xil "
                    "qoldirib, uni bo'lish vaziyatni yomonlashtiradi. Sabab — "
                    "chekli kenglik effekti: katta teshikda kuchlanish oqimi "
                    "kengroq sohaga taqsimlanadi. Amalda esa teshiklar "
                    "orasidagi masofa ham muhim: ular bir-biriga yaqin bo'lsa, "
                    "maydonlar qo'shilib konsentratsiya yanada oshadi."
                ),
            ),
            computation=Computation(
                caption=(
                    "Kuchlanish konsentratsiyasi: Kirsh yechimi bilan teshik "
                    "atrofidagi maydonni hisoblang."
                ),
                code='''"""Kuchlanish konsentratsiyasi: Kirsh yechimi va konstruktiv omillar."""
import numpy as np
from labkit import PARAMS, note, series, table, value

sigma = float(PARAMS.get("sigma", 100.0))   # nominal kuchlanish, MPa
a = float(PARAMS.get("a", 15.0))*1e-3       # teshik radiusi, m
b = float(PARAMS.get("b", 120.0))*1e-3      # plastina kengligi, m
r_fillet = float(PARAMS.get("r", 3.0))*1e-3 # galtel radiusi, m
D_shaft = float(PARAMS.get("D", 55.0))*1e-3 # katta diametr, m
d_shaft = float(PARAMS.get("d", 45.0))*1e-3 # kichik diametr, m
q_sens = float(PARAMS.get("q", 0.8))        # sezgirlik koeffitsienti

# Kirsh yechimi: teshik atrofida sigma_theta
def sigma_theta(r, theta):
    return sigma/2*((1+a**2/r**2) - (1+3*a**4/r**4)*np.cos(2*theta))

rr = np.linspace(a, 6*a, 300)
series("σ_θ(r) — θ=90° (maksimal)", (rr/a).tolist(),
       [sigma_theta(r, np.pi/2) for r in rr], xlabel="r/a", ylabel="σ_θ, MPa")
series("σ_θ(r) — θ=0° (minimal)", (rr/a).tolist(),
       [sigma_theta(r, 0.0) for r in rr], xlabel="r/a", ylabel="σ_θ, MPa")

value("K_t (cheksiz plastina)", sigma_theta(a, np.pi/2)/sigma, "—")
value("σ_max", sigma_theta(a, np.pi/2), "MPa")
value("σ_θ (θ=0, teshik chekkasida)", sigma_theta(a, 0.0), "MPa")
note(f"θ=0 da σ_θ = -σ = {sigma_theta(a, 0.0):.1f} MPa — siquvchi kuchlanish! "
     "Teshik atrofida ham cho'zilish, ham siqilish zonasi bor.")

for k in (2, 3, 5):
    note(f"r = {k}a da σ_θ = {sigma_theta(k*a, np.pi/2):.2f} MPa "
         f"({sigma_theta(k*a, np.pi/2)/sigma:.3f}σ) — konsentratsiya lokal.")

# Burchak bo'ylab taqsimot
th = np.linspace(0, np.pi, 200)
series("σ_θ(θ) teshik chekkasida", np.degrees(th).tolist(),
       [sigma_theta(a, t) for t in th], xlabel="θ, deg", ylabel="σ_θ, MPa")

# Chekli kenglik tuzatishi (empirik)
ratio = 2*a/b
Kt_finite = 3.0 - 3.14*ratio + 3.667*ratio**2 - 1.527*ratio**3
value("d/b nisbati", ratio, "—")
value("K_t (chekli kenglik)", Kt_finite, "—")
value("σ_max (chekli)", Kt_finite*sigma, "MPa")

# Galtel uchun konsentratsiya (val)
r_d = r_fillet/d_shaft
D_d = D_shaft/d_shaft
Kt_fillet = 1 + 0.5/np.sqrt(r_d) if r_d > 0 else np.inf
value("r/d nisbati", r_d, "—")
value("K_t (galtel, taxminiy)", Kt_fillet, "—")
value("K_σ (effektiv)", 1 + q_sens*(Kt_fillet-1), "—")

rr_f = np.linspace(0.02, 0.35, 100)
series("K_t(r/d) — galtel", rr_f.tolist(), (1 + 0.5/np.sqrt(rr_f)).tolist(),
       xlabel="r/d", ylabel="K_t")
note(f"r/d ni {r_d:.3f} dan 0,2 ga oshirish K_t ni "
     f"{Kt_fillet:.2f} dan {1+0.5/np.sqrt(0.2):.2f} ga tushiradi.")

table("Tipik konsentratsiya koeffitsientlari",
      ["Element", "Geometriya", "K_t"],
      [["Dumaloq teshik", "cheksiz plastina", 3.0],
       ["Ellips teshik (a/b=3)", "cho'zilgan", 7.0],
       ["Galtel", "r/d = 0,05", 2.2],
       ["Galtel", "r/d = 0,1", 1.8],
       ["Galtel", "r/d = 0,2", 1.5],
       ["Shpon kanali", "standart", 1.6],
       ["Rezba", "metrik", 3.0],
       ["O'tkir burchak", "r → 0", "→ ∞"]])

table("Konsentratsiyani kamaytirish usullari",
      ["Usul", "Ta'sir", "Izoh"],
      [["Radiusni oshirish", "K_t ↓↓", "Eng samarali va arzon"],
       ["Yordamchi ariqchalar", "K_t ↓", "Kuchlanish oqimini yumshatadi"],
       ["Ellipssimon o'tish", "K_t ↓", "Doiraviydan yaxshiroq"],
       ["Yuza mustahkamlash", "K_σ ↓", "Nagartovka, azotlash"],
       ["Plastik material", "q ↓", "Mahalliy oqish tenglashtiradi"]])
''',
                parameters=[
                    p("sigma", "Nominal kuchlanish σ", 10.0, 500.0, 100.0, 5.0, "MPa"),
                    p("a", "Teshik radiusi a", 1.0, 50.0, 15.0, 1.0, "mm"),
                    p("b", "Plastina kengligi b", 20.0, 500.0, 120.0, 5.0, "mm"),
                    p("r", "Galtel radiusi r", 0.5, 20.0, 3.0, 0.5, "mm"),
                    p("D", "Katta diametr D", 20.0, 300.0, 55.0, 1.0, "mm"),
                    p("d", "Kichik diametr d", 10.0, 250.0, 45.0, 1.0, "mm"),
                    p("q", "Sezgirlik q", 0.0, 1.0, 0.8, 0.05, "—"),
                ],
                expected_output="K_t = 3,0 (Kirsh), σ_max = 300 MPa, r = 3a da σ ≈ 1,07σ",
            ),
            visualization=vis(
                "Teshik atrofidagi kuchlanish maydoni",
                "React/SVG",
                "Teshikli plastina; kuchlanish darajasi rang bilan; teshik "
                "chekkasida ($\\theta = 90°$) qizil zona, $\\theta = 0$ da "
                "siqilish zonasi. Yonida $\\sigma_\\theta(r)$ grafigi.",
                "React/SVG: kuchlanish maydonini SVG to'r bilan chizish "
                "mumkin — Kirsh formulasi analitik, shuning uchun har bir "
                "nuqtada tez hisoblanadi. 'Kuchlanish oqimi' chiziqlarini "
                "qo'shish konsentratsiyaning fizik sababini tushuntiradi.",
            ),
            interpretation=(
                "$\\sigma_\\theta(r)$ grafigi konsentratsiyaning juda lokal "
                "ekanini ko'rsatadi: $r = 3a$ da kuchlanish nominal qiymatdan "
                "atigi 7 % katta. $\\theta = 0$ da esa siquvchi kuchlanish "
                "paydo bo'ladi — bu kutilmagan, lekin Kirsh yechimidan "
                "kelib chiqadi. $K_t(r/d)$ grafigi galtel radiusini "
                "oshirishning samarasini beradi: $r/d$ ni 0,05 dan 0,2 ga "
                "oshirish $K_t$ ni 1,4 marta kamaytiradi."
            ),
            common_mistakes=[
                "$\\sigma_{nom}$ ni to'liq kesim bo'yicha hisoblash — "
                "zaiflashgan kesim olinishi kerak.",
                "Statik yuklanishda plastik material uchun konsentratsiyani "
                "to'liq hisobga olish — mahalliy oqish uni yumshatadi.",
                "$K_t$ va $K_\\sigma$ ni chalkashtirish.",
                "O'tkir burchaklarni loyihada qoldirish — bu cheksiz "
                "konsentratsiya demakdir.",
            ],
            quiz=[
                q("Nima uchun $K_t = 3$ teshik o'lchamiga bog'liq emas?",
                  "Kirsh yechimida kuchlanish $a/r$ nisbatlariga bog'liq; "
                  "$r = a$ da ular birga aylanadi va o'lcham qisqaradi.",
                  "konseptual"),
                q("$\\sigma_{nom} = 80$ MPa, $K_t = 2{,}5$. $\\sigma_{max}$?",
                  "$200$ MPa.", "hisob"),
                q("Nima uchun plastik material konsentratsiyaga kam sezgir?",
                  "Mahalliy oqish kuchlanishni qayta taqsimlaydi va cho'qqini "
                  "yumshatadi — $q < 1$.", "konseptual"),
                q("Konsentratsiyani kamaytirishning eng samarali usuli?",
                  "O'tish radiusini oshirish — u arzon va $K_t$ ni sezilarli "
                  "kamaytiradi.", "talqin"),
                q("Kodda $\\theta = 0$ da nima uchun manfiy kuchlanish chiqadi?",
                  "Kirsh yechimi bo'yicha yuklanish yo'nalishidagi teshik "
                  "chekkasida siquvchi kuchlanish $-\\sigma$ paydo bo'ladi — "
                  "bu Puasson effektining natijasi.", "kod"),
            ],
            bridge_to_next=(
                "Barcha hisob turlari o'rganildi. Oxirgi mavzuda ularni "
                "birlashtirib, konstruktiv elementni to'liq loyihalash "
                "metodikasini ko'ramiz."
            ),
            research_extension=(
                "Optimal galtel shaklini toping: doiraviy o'tish o'rniga "
                "ellipssimon yoki 'kuchlanish oqimiga mos' shaklni ko'rib "
                "chiqing. Chekli elementlar bilan (yoki sonli konform "
                "akslantirishr bilan) $K_t$ ni har ikki shakl uchun hisoblang "
                "va farqni baholang. Tabiatda (daraxt shoxi, suyak) qanday "
                "shakllar uchraydi?"
            ),
        ),
    ),
    Topic(
        id="mq-30",
        subject_id=S,
        module_id=M,
        order=30,
        title="Konstruktiv elementni kompleks hisoblash va loyihalash metodikasi",
        description=(
            "Mustahkamlik, bikrlik, ustuvorlik va chidamlilik shartlarini "
            "birgalikda qanoatlantirish; to'liq loyihalash algoritmi."
        ),
        learning_objective=(
            "Real konstruktiv elementni barcha mezonlar bo'yicha hisoblab, "
            "asoslangan loyihaviy qaror qabul qilish."
        ),
        prerequisites=["mq-26", "mq-28", "mq-18"],
        mathematical_core=(
            "Ko'p mezonli optimallashtirish, cheklovlar tizimi, iterativ "
            "yechim."
        ),
        engineering_application=(
            "Har qanday mas'uliyatli konstruktiv element loyihalash; "
            "konstruktorlik hujjatlari."
        ),
        computational_component=(
            "To'liq hisob dasturi: barcha shartlarni tekshirish va hal "
            "qiluvchi mezonni aniqlash."
        ),
        visualization_component=(
            "Loyihaviy sohalar diagrammasi: har bir shart chegarasi va "
            "ruxsat etilgan soha."
        ),
        research_extension=(
            "Ko'p mezonli optimallashtirish: Pareto chegarasi va "
            "kompromiss yechimlar."
        ),
        difficulty="ilg'or",
        previous_link=(
            "Butun kurs davomida o'rganilgan barcha hisob turlari bu yerda "
            "yagona metodikaga birlashadi."
        ),
        next_topic="tmm-01",
        estimated_minutes=100,
        tags=["kompleks hisob", "loyihalash", "optimallashtirish"],
        lesson=Lesson(
            physical_problem=(
                "Kran ko'targichining balkasini loyihalash kerak. U yetarlicha "
                "mustahkam, yetarlicha bikr bo'lishi, siqilgan qismlarida "
                "ustuvorlikni yo'qotmasligi va million sikl ishlashi kerak. "
                "Bu to'rt shart turli o'lchamlarni talab qiladi. Qaysi biri "
                "hal qiluvchi va yakuniy qaror qanday qabul qilinadi?"
            ),
            concepts=[
                c("Chegaraviy holatlar", "Konstruksiya yaroqsiz bo'ladigan "
                  "holatlar: buzilish, ortiqcha deformatsiya, ustuvorlikni "
                  "yo'qotish, charchash."),
                c("Hal qiluvchi mezon", "Eng katta o'lchamni talab qiluvchi "
                  "shart; qolganlarida zaxira qoladi."),
                c("Loyihalash algoritmi", "Hisob sxemasi → ichki kuchlar → "
                  "kesim tanlash → barcha shartlarni tekshirish → optimallashtirish."),
                c("Texnologik cheklovlar", "Standart o'lchamlar, tayyorlash "
                  "usuli, montaj talablari."),
                c("Iqtisodiy mezon", "Massa, narx, ishlab chiqarish "
                  "murakkabligi — ular ham qaror qabul qilishga ta'sir qiladi."),
            ],
            derivation=[
                d("1-qadam. Shartlar tizimini yozish",
                  r"\begin{cases}\sigma_{max} \le [\sigma] & \text{(mustahkamlik)}\\ "
                  r"w_{max} \le [f] & \text{(bikrlik)}\\ "
                  r"F \le \varphi[\sigma]A & \text{(ustuvorlik)}\\ "
                  r"n_\sigma \ge [n] & \text{(chidamlilik)}\end{cases}",
                  "To'rt mustaqil shart. Har biri kesim o'lchamlariga turli "
                  "darajada bog'liq."),
                d("2-qadam. Har bir shartdan kerakli parametrni ifodalash",
                  r"W \ge \frac{M}{[\sigma]};\quad I \ge \frac{5qL^4}{384E[f]};\quad "
                  r"A \ge \frac{F}{\varphi[\sigma]};\quad W \ge \frac{M_a[n]K_\sigma}{\varepsilon\beta\sigma_{-1}}",
                  "Har bir shart o'z geometrik tavsifiga cheklov qo'yadi."),
                d("3-qadam. Hal qiluvchi mezonni aniqlash",
                  r"\text{Kesim} = \max(\text{barcha shartlardan kelib chiqadigan talablar})",
                  "Eng qattiq shart tanlanadi; qolganlarida zaxira qanchaligi "
                  "hisoblanadi."),
                d("4-qadam. Optimallashtirish va yaxlitlash",
                  r"\min A \text{ barcha shartlar bajarilganda} \to "
                  r"\text{standart qatorga yaxlitlash}",
                  "Matematik optimum standart o'lchamga yaxlitlanadi; "
                  "yakuniy tekshirish o'tkaziladi."),
            ],
            formula_meaning=(
                "Kompleks hisob loyihalashning mohiyatini ochib beradi: "
                "bu bitta formula bo'yicha hisob emas, balki bir necha "
                "cheklov orasidagi kompromiss. Tajriba shuni ko'rsatadiki, "
                "hal qiluvchi mezon element turiga bog'liq: qisqa balkalarda "
                "mustahkamlik, uzun balkalarda bikrlik, siqilgan "
                "elementlarda ustuvorlik, aylanuvchi vallarda esa "
                "chidamlilik. Tajribali konstruktor buni oldindan taxmin "
                "qiladi va hisobni shundan boshlaydi."
            ),
            equations=[
                eq(r"\sigma_{max} \le [\sigma]", "Mustahkamlik sharti.", "Mustahkamlik"),
                eq(r"w_{max} \le [f]", "Bikrlik sharti.", "Bikrlik"),
                eq(r"\sigma \le \varphi[\sigma]", "Ustuvorlik sharti.", "Ustuvorlik"),
                eq(r"n_\sigma \ge [n]", "Chidamlilik sharti.", "Chidamlilik"),
            ],
            conditions=(
                "Barcha shartlar bir vaqtda bajarilishi shart — birortasining "
                "buzilishi konstruksiyani yaroqsiz qiladi. Shartlar "
                "ustuvorligi: xavfsizlikka bog'liqlari (mustahkamlik, "
                "ustuvorlik, chidamlilik) hech qachon yon berilmaydi; "
                "bikrlik esa ba'zan foydalanish talablariga qarab "
                "yumshatilishi mumkin."
            ),
            worked_example=WorkedExample(
                statement=(
                    "Kran ko'targich balkasi: $L = 7{,}5$ m, harakatlanuvchi "
                    "yuk $P = 50$ kN (o'rtada eng xavfli), o'z og'irligi "
                    "$q = 1{,}2$ kN/m. Po'lat: $[\\sigma] = 160$ MPa, "
                    "$E = 200$ GPa, $[f] = L/500$ (kran uchun qat'iy), "
                    "$\\sigma_{-1} = 250$ MPa, $K_\\sigma = 1{,}4$, "
                    "$[n] = 1{,}6$. Dvutavr tanlang."
                ),
                given=[r"L = 7{,}5\ \text{m},\; P = 50\ \text{kN},\; q = 1{,}2\ \text{kN/m}",
                       r"[\sigma] = 160\ \text{MPa},\; [f] = 15\ \text{mm}"],
                steps=[
                    st(r"M_{max} = \frac{PL}{4} + \frac{qL^2}{8} = \frac{50\cdot7{,}5}{4} + "
                       r"\frac{1{,}2\cdot56{,}25}{8} = 93{,}75+8{,}44 = 102{,}2\ \text{kN·m}",
                       "Maksimal eguvchi moment."),
                    st(r"\text{Mustahkamlik: } W \ge \frac{102{,}2\cdot10^3}{160\cdot10^6} = "
                       r"6{,}39\cdot10^{-4}\ \text{m}^3 = 639\ \text{cm}^3",
                       "Birinchi shart."),
                    st(r"\text{Bikrlik: } I \ge \frac{PL^3}{48E[f]} + \frac{5qL^4}{384E[f]} = "
                       r"\frac{50\cdot10^3\cdot422}{48\cdot2\cdot10^{11}\cdot0{,}015} + \dots",
                       "$I \\ge 1{,}465\\cdot10^{-4} + 0{,}257\\cdot10^{-4} = "
                       "1{,}72\\cdot10^{-4}$ m⁴ $= 17\\,200$ cm⁴."),
                    st(r"\text{Chidamlilik: } \sigma_a = \frac{M_P}{W} = \frac{93{,}75\cdot10^3}{W};\ "
                       r"\sigma_{-1D} = \frac{0{,}8\cdot0{,}9}{1{,}4}\cdot250 = 128{,}6\ \text{MPa}",
                       "Harakatlanuvchi yukdan pulsatsiyalanuvchi sikl; "
                       "$W \\ge 93{,}75\\cdot10^3\\cdot1{,}6/128{,}6\\cdot10^6 = 1166$ cm³."),
                    st(r"\text{Dvutavr № 45: } W = 1231\ \text{cm}^3,\; I = 27\,696\ \text{cm}^4,\; "
                       r"A = 84{,}7\ \text{cm}^2",
                       "Barcha shartlardan eng qattig'i — chidamlilik "
                       "(1166 cm³); № 45 uni qanoatlantiradi."),
                    st(r"\text{Tekshirish: } \sigma = \frac{102{,}2\cdot10^3}{1{,}231\cdot10^{-3}} = 83{,}0\ \text{MPa} \le 160\ \checkmark;\ "
                       r"w = \frac{PL^3+\dots}{48EI} = 9{,}3\ \text{mm} \le 15\ \checkmark;\ "
                       r"n_\sigma = \frac{128{,}6}{76{,}2} = 1{,}69 \ge 1{,}6\ \checkmark",
                       "Barcha shartlar bajarildi."),
                ],
                answer=(
                    "Dvutavr № 45: $\\sigma = 83{,}0$ MPa (zaxira 1,93), "
                    "$w = 9{,}3$ mm (zaxira 1,61), $n_\\sigma = 1{,}69$ "
                    "(zaxira 1,06). Hal qiluvchi mezon — chidamlilik."
                ),
                engineering_note=(
                    "Chidamlilik hal qiluvchi bo'lib chiqdi — bu kran "
                    "balkalari uchun tipik, chunki ular millionlab sikl "
                    "ishlaydi. Mustahkamlik bo'yicha zaxira 1,93 — ya'ni "
                    "statik hisob 2 marta kichikroq kesim berardi va bu "
                    "xavfli xato bo'lardi. Aynan shuning uchun siklik "
                    "yuklangan konstruksiyalarda charchash hisobi majburiy."
                ),
            ),
            computation=Computation(
                caption=(
                    "Kompleks hisob: barcha shartlarni tekshirib, hal qiluvchi "
                    "mezonni va optimal kesimni aniqlang."
                ),
                code='''"""Kompleks loyihalash: barcha mezonlarni birgalikda tekshirish."""
import numpy as np
from labkit import PARAMS, note, series, table, value

L = float(PARAMS.get("L", 7.5))            # oraliq, m
P = float(PARAMS.get("P", 50.0))*1e3       # harakatlanuvchi yuk, N
q = float(PARAMS.get("q", 1.2))*1e3        # o'z og'irligi, N/m
s_allow = float(PARAMS.get("s_allow", 160.0))*1e6
f_div = float(PARAMS.get("f_div", 500.0))  # bikrlik me'yori L/n
s_m1 = float(PARAMS.get("s_m1", 250.0))*1e6
K_s = float(PARAMS.get("Ks", 1.4))
n_req = float(PARAMS.get("n_req", 1.6))
E = 200e9
eps_s, beta = 0.8, 0.9

M_max = P*L/4 + q*L**2/8
M_cyclic = P*L/4                            # faqat harakatlanuvchi yuk siklik
f_allow = L/f_div
s_1D = eps_s*beta/K_s*s_m1

value("M_max", M_max/1000, "kN·m")
value("Ruxsat etilgan cho'kish", f_allow*1000, "mm")
value("σ_-1D (detal)", s_1D/1e6, "MPa")

# Har bir shartdan kerakli tavsif
W_strength = M_max/s_allow
I_stiffness = (P*L**3/48 + 5*q*L**4/384)/(E*f_allow)
W_fatigue = M_cyclic*n_req/s_1D

value("W (mustahkamlikdan)", W_strength*1e6, "cm³")
value("I (bikrlikdan)", I_stiffness*1e8, "cm⁴")
value("W (chidamlilikdan)", W_fatigue*1e6, "cm³")

# Standart dvutavrlar: nomer -> (W cm³, I cm⁴, A cm²)
profiles = {
    24: (289, 3460, 34.8), 27: (371, 5010, 40.2), 30: (472, 7080, 46.5),
    33: (597, 9840, 53.8), 36: (743, 13380, 61.9), 40: (953, 19062, 72.6),
    45: (1231, 27696, 84.7), 50: (1589, 39727, 100.0), 55: (2035, 55962, 118.0),
    60: (2560, 76806, 138.0),
}

rows = []
selected = None
for nm in sorted(profiles):
    W, I, A = profiles[nm]
    W_si, I_si = W*1e-6, I*1e-8
    s_work = M_max/W_si
    w_def = (P*L**3/48 + 5*q*L**4/384)/(E*I_si)
    s_a = M_cyclic/W_si
    n_s = s_1D/s_a
    ok_str = s_work <= s_allow
    ok_stf = w_def <= f_allow
    ok_fat = n_s >= n_req
    ok_all = ok_str and ok_stf and ok_fat
    rows.append([f"№{nm}", float(A), float(s_work/1e6), float(w_def*1000),
                 float(n_s), "✓" if ok_all else "✗"])
    if ok_all and selected is None:
        selected = (nm, W, I, A, s_work, w_def, n_s)

table("Profillarni tekshirish",
      ["Profil", "A, cm²", "σ, MPa", "w, mm", "n_σ", "Barcha shartlar"], rows)

if selected:
    nm, W, I, A, s_work, w_def, n_s = selected
    value("TANLANGAN profil №", float(nm), "—")
    value("Yuza A", float(A), "cm²")
    value("Massa (1 m)", float(A*1e-4*7850), "kg/m")
    value("σ zaxirasi", float(s_allow/s_work), "—")
    value("Bikrlik zaxirasi", float(f_allow/w_def), "—")
    value("Chidamlilik zaxirasi", float(n_s/n_req), "—")
    reserves = {"Mustahkamlik": s_allow/s_work, "Bikrlik": f_allow/w_def,
                "Chidamlilik": n_s/n_req}
    critical = min(reserves, key=reserves.get)
    note(f"HAL QILUVCHI MEZON: {critical} (zaxira {reserves[critical]:.3f})")
    note("Qolgan mezonlarda zaxira: " +
         ", ".join(f"{k} {v:.2f}" for k, v in reserves.items() if k != critical))

# Oraliq uzunligining hal qiluvchi mezonga ta'siri
LL = np.linspace(3, 15, 100)
W_str = [(P*x/4 + q*x**2/8)/s_allow*1e6 for x in LL]
I_stf = [(P*x**3/48 + 5*q*x**4/384)/(E*x/f_div)*1e8 for x in LL]
W_fat = [(P*x/4)*n_req/s_1D*1e6 for x in LL]
series("W kerak (mustahkamlik)", LL.tolist(), W_str, xlabel="L, m", ylabel="W, cm³")
series("W kerak (chidamlilik)", LL.tolist(), W_fat, xlabel="L, m", ylabel="W, cm³")
series("I kerak (bikrlik)", LL.tolist(), I_stf, xlabel="L, m", ylabel="I, cm⁴")
note("Qisqa oraliqlarda chidamlilik, uzunlarida bikrlik hal qiluvchi bo'ladi.")

table("Loyihalash algoritmi",
      ["Bosqich", "Amal", "Natija"],
      [["1", "Hisob sxemasini tuzish", "Tayanchlar, yuklar"],
       ["2", "Ichki kuchlarni aniqlash", "Q, M epyuralari"],
       ["3", "Hal qiluvchi mezonni taxmin qilish", "Dastlabki kesim"],
       ["4", "Barcha shartlarni tekshirish", "Zaxiralar ro'yxati"],
       ["5", "Optimallashtirish va yaxlitlash", "Standart profil"],
       ["6", "Yakuniy tekshirish", "Konstruktorlik hujjati"]])
''',
                parameters=[
                    p("L", "Oraliq L", 2.0, 20.0, 7.5, 0.5, "m"),
                    p("P", "Harakatlanuvchi yuk P", 5.0, 500.0, 50.0, 5.0, "kN"),
                    p("q", "O'z og'irligi q", 0.1, 20.0, 1.2, 0.1, "kN/m"),
                    p("s_allow", "[σ]", 60.0, 400.0, 160.0, 10.0, "MPa"),
                    p("f_div", "Bikrlik me'yori L/n", 200.0, 1000.0, 500.0, 50.0, "—"),
                    p("s_m1", "Chidamlilik σ_-1", 100.0, 600.0, 250.0, 10.0, "MPa"),
                    p("Ks", "Konsentratsiya K_σ", 1.0, 3.0, 1.4, 0.05, "—"),
                    p("n_req", "Kerakli zaxira [n]", 1.2, 3.0, 1.6, 0.1, "—"),
                ],
                expected_output="Dvutavr № 45; hal qiluvchi mezon — chidamlilik",
            ),
            visualization=vis(
                "Loyihaviy sohalar diagrammasi",
                "React/SVG",
                "$(W, I)$ tekisligida har bir shartning chegara chizig'i; "
                "ruxsat etilgan soha (barcha shartlar bajariladigan) bo'yalgan; "
                "standart profillar nuqtalar sifatida; tanlangan profil "
                "belgilangan.",
                "React/SVG: bu diagramma loyihalashning mohiyatini — bir necha "
                "cheklov orasidagi kompromissni — bir rasmda ko'rsatadi. "
                "Standart profillarni nuqtalar bilan qo'yish esa amaliy "
                "tanlovni vizual qiladi.",
            ),
            interpretation=(
                "Oraliq uzunligiga bog'liqlik grafigi muhim qonuniyatni "
                "ko'rsatadi: qisqa oraliqlarda chidamlilik ($W \\propto L$), "
                "uzunlarida esa bikrlik ($I \\propto L^3$) hal qiluvchi. "
                "Kesish nuqtasi loyihalash strategiyasini belgilaydi. "
                "Zaxiralar ro'yxati esa qayerda material 'ortiqcha' "
                "ekanini ko'rsatadi — bu keyingi optimallashtirish uchun "
                "boshlang'ich nuqta."
            ),
            common_mistakes=[
                "Faqat mustahkamlikni tekshirib, qolgan shartlarni unutish.",
                "Hal qiluvchi mezonni oldindan taxmin qilmasdan hisobni "
                "boshlash (vaqt yo'qotish).",
                "Standart o'lchamlarga yaxlitlashdan keyin qayta "
                "tekshirmaslik.",
                "Texnologik va montaj cheklovlarini e'tiborsiz qoldirish.",
            ],
            quiz=[
                q("Nima uchun barcha shartlar bir vaqtda tekshirilishi kerak?",
                  "Ularning har biri mustaqil chegaraviy holatni tavsiflaydi; "
                  "birortasining buzilishi konstruksiyani yaroqsiz qiladi.",
                  "konseptual"),
                q("Uzun balkalarda odatda qaysi mezon hal qiluvchi?",
                  "Bikrlik, chunki $w \\propto L^4$, $\\sigma \\propto L^2$ — "
                  "cho'kish tezroq o'sadi.", "konseptual"),
                q("$W_{mustahkamlik} = 600$ cm³, $W_{chidamlilik} = 900$ cm³. "
                  "Qaysi biri hal qiluvchi?",
                  "Chidamlilik — u kattaroq kesim talab qiladi.", "hisob"),
                q("Kran balkasida nima uchun chidamlilik ko'pincha hal qiluvchi?",
                  "Kran millionlab yuklanish siklini boshdan kechiradi; "
                  "charchash chegarasi statik mustahkamlikdan ancha past.",
                  "talqin"),
                q("Kodda `min(reserves, key=reserves.get)` nima aniqlaydi?",
                  "Eng kichik zaxiraga ega mezonni — ya'ni hal qiluvchi "
                  "shartni. Uni bilish keyingi optimallashtirish yo'nalishini "
                  "ko'rsatadi.", "kod"),
            ],
            bridge_to_next=(
                "Materiallar qarshiligi kursi yakunlandi. Biz sterjenlar uchun "
                "bir o'lchovli nazariyani qurdik va u ko'p amaliy masalani "
                "yechdi. Lekin uning barcha formulalari gipotezalarga "
                "asoslangan edi. Keyingi fan — Tutash muhitlar mexanikasi — "
                "bu gipotezalarni olib tashlaydi va umumiy, uch o'lchovli "
                "nazariyani quradi. U yerda $\\sigma$ va $\\varepsilon$ "
                "tenzorlarga aylanadi, muvozanat esa differensial tenglamalar "
                "tizimiga."
            ),
            research_extension=(
                "Ko'p mezonli optimallashtirish masalasini qo'ying: massa va "
                "narxni bir vaqtda minimallashtiring (ular har doim mos "
                "kelmaydi — yupqa devorli profil yengil, lekin qimmat). "
                "Pareto chegarasini quring va unda turgan yechimlardan "
                "qaysi biri amaliy jihatdan afzal ekanini asoslang."
            ),
        ),
    ),
]
