"""PQ / 1-modul: Yupqa plastina modeli va asosiy tenglama (pq-01 … pq-06)."""

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

S = "plastinalar-qobiqlar"
M = "pq-m1"


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
    # ------------------------------------------------------------------ pq-01
    Topic(
        id="pq-01",
        subject_id=S, module_id=M, order=1,
        title="Yupqa plastina modeli va Kirxhoff–Lyav gipotezalari",
        description=(
            "Plastina tushunchasi, qalinlik bo'yicha tasniflash, "
            "Kirxhoff–Lyav gipotezalarining mazmuni va ularning uch "
            "o'lchovli elastiklik masalasini ikki o'lchovliga keltirishdagi roli."
        ),
        learning_objective=(
            "Kirxhoff–Lyav gipotezalarini aniq ifodalash, ularning har "
            "birining matematik oqibatini yozish va nazariyaning "
            "qo'llanish chegaralarini baholash."
        ),
        prerequisites=["tmm-16", "mq-13"],
        mathematical_core=(
            "Uch o'lchovli ko'chish maydonini qalinlik bo'yicha yoyish, "
            "$u = -z\\,\\partial w/\\partial x$, $\\varepsilon_{zz} = "
            "\\gamma_{xz} = \\gamma_{yz} = 0$ cheklovlari, o'rta sirt "
            "tushunchasi."
        ),
        engineering_application=(
            "Bino perekrytiyasi, ko'prik plitasi, kema korpusi paneli, "
            "samolyot qanoti qoplamasi, elektron qurilmalar korpusi, "
            "bosim idishi devori."
        ),
        computational_component=(
            "Qalinlik nisbatining nazariya aniqligiga ta'sirini sonli "
            "baholash, Kirxhoff va sdvig nazariyalari natijalarini "
            "taqqoslash."
        ),
        visualization_component=(
            "O'rta sirt va normal chiziqning egilishdan keyingi holati; "
            "qalinlik bo'yicha ko'chish va deformatsiya epyuralari."
        ),
        research_extension=(
            "Kirxhoff gipotezalarining variatsion asoslanishini o'rganing: "
            "ularni asimptotik yoyilma orqali qanday keltirib chiqarish mumkin?"
        ),
        difficulty="kirish",
        previous_link=(
            "tmm-16 da tekis kuchlanish va tekis deformatsiya holatlari "
            "o'rganildi — ular ham 3D masalani 2D ga keltirishning "
            "usullari edi. Plastina nazariyasi shu g'oyani egilishga "
            "kengaytiradi: mq-13 dagi balka gipotezalari endi ikki "
            "o'lchovli o'rta sirtga umumlashtiriladi."
        ),
        next_topic="pq-02",
        estimated_minutes=85,
        tags=["plastina", "Kirxhoff", "gipoteza", "model"],
        lesson=_lesson(
            problem=(
                "Bino perekrytiyasi: 6×8 m o'lchamli, 200 mm qalinlikdagi "
                "temir-beton plita. Uning egilishini hisoblash kerak. "
                "Uch o'lchovli elastiklik masalasi (tmm-15) 15 ta noma'lum "
                "funksiyaga ega va qo'lda yechilmaydi. Balka nazariyasi "
                "(mq-13) esa faqat bir yo'nalishni hisobga oladi — lekin "
                "plita ikkala yo'nalishda ham ishlaydi. Kerak bo'lgan narsa: "
                "3D masalaning aniqligini ko'p yo'qotmasdan, uni bitta "
                "noma'lum funksiyali 2D masalaga keltiruvchi model."
            ),
            concepts=[
                c("Plastina (plate)",
                  "Qalinligi boshqa ikki o'lchamidan ancha kichik bo'lgan, "
                  "tekis o'rta sirtli jism; yuklama asosan sirtga "
                  "perpendikulyar yo'nalgan."),
                c("O'rta sirt (mid-surface)",
                  "Plastina qalinligini teng ikkiga bo'luvchi tekislik "
                  "($z = 0$). Butun nazariya shu sirtning ko'chishi "
                  "$w(x, y)$ orqali quriladi."),
                c("Kirxhoff–Lyav gipotezalari",
                  "(1) O'rta sirtga normal to'g'ri chiziq deformatsiyadan "
                  "keyin ham to'g'ri va deformatsiyalangan o'rta sirtga "
                  "normal qoladi; (2) qalinlik o'zgarmaydi "
                  "($\\varepsilon_{zz} = 0$); (3) o'rta sirtda cho'zilish yo'q; "
                  "(4) $\\sigma_{zz}$ boshqa kuchlanishlarga nisbatan kichik."),
                c("Yupqa va qalin plastina",
                  "$h/a < 1/20$ — yupqa (Kirxhoff nazariyasi yetarli); "
                  "$1/20 < h/a < 1/5$ — o'rtacha qalinlik (Mindlin nazariyasi); "
                  "$h/a > 1/5$ — qalin (3D tahlil kerak)."),
                c("Kichik og'ish sharti",
                  "$w_{\\max} < h/5$ bo'lsa geometrik chiziqli nazariya "
                  "o'rinli; kattaroq og'ishda membrana kuchlari paydo "
                  "bo'ladi (fon Karman, pq-18)."),
                c("Model keltirish (dimensional reduction)",
                  "3D masalani gipotezalar yordamida past o'lchamli "
                  "masalaga aylantirish. Aniqlikning bir qismi "
                  "yo'qotiladi, lekin yechim amaliy bo'lib qoladi."),
            ],
            derivation=[
                d("1. Uch o'lchovli ko'chish maydonini yoyish",
                  r"u(x,y,z) = u_0(x,y) + z\,\phi_x(x,y) + O(z^2), \quad "
                  r"v = v_0 + z\,\phi_y + O(z^2), \quad w = w_0 + O(z)",
                  "Qalinlik kichik bo'lgani uchun ko'chishni $z$ bo'yicha "
                  "Teylor qatoriga yoyamiz va birinchi hadlar bilan "
                  "cheklanamiz. $\\phi_x, \\phi_y$ — normalning burilish "
                  "burchaklari."),
                d("2. Birinchi gipoteza: normal normal qoladi",
                  r"\gamma_{xz} = \frac{\partial u}{\partial z} "
                  r"+ \frac{\partial w}{\partial x} = 0 \;\Longrightarrow\; "
                  r"\phi_x = -\frac{\partial w}{\partial x}, \quad "
                  r"\phi_y = -\frac{\partial w}{\partial y}",
                  "Sdvig deformatsiyasi nolga tenglashtiriladi. Natijada "
                  "burilish burchaklari **mustaqil emas** — ular "
                  "$w$ ning hosilalari. Noma'lumlar soni uchtadan bittaga tushadi."),
                d("3. Ikkinchi gipoteza: qalinlik o'zgarmaydi",
                  r"\varepsilon_{zz} = \frac{\partial w}{\partial z} = 0 "
                  r"\;\Longrightarrow\; w = w(x, y)",
                  "Og'ish qalinlik bo'yicha o'zgarmaydi — bu $w$ ni faqat "
                  "ikki o'zgaruvchining funksiyasiga aylantiradi. Bu — "
                  "3D dan 2D ga o'tishning hal qiluvchi qadami."),
                d("4. Uchinchi gipoteza: sof egilish",
                  r"u_0 = v_0 = 0 \;\Longrightarrow\; "
                  r"u = -z\frac{\partial w}{\partial x}, \quad "
                  r"v = -z\frac{\partial w}{\partial y}",
                  "O'rta sirt cho'zilmaydi. Bu faqat kichik og'ishlarda "
                  "o'rinli; katta og'ishda membrana kuchlari paydo bo'ladi. "
                  "Endi butun 3D ko'chish maydoni bitta $w(x,y)$ bilan tavsiflanadi."),
                d("5. To'rtinchi gipoteza va tekis kuchlanish holati",
                  r"\sigma_{zz} \approx 0 \;\Longrightarrow\; "
                  r"\sigma_x = \frac{E}{1-\nu^2}(\varepsilon_x + \nu\varepsilon_y), \ "
                  r"\sigma_y = \frac{E}{1-\nu^2}(\varepsilon_y + \nu\varepsilon_x)",
                  "$\\sigma_{zz}$ yuklama tartibida ($\\sim q$), "
                  "$\\sigma_x$ esa $\\sim q(a/h)^2$ tartibida — demak "
                  "$\\sigma_{zz}/\\sigma_x \\sim (h/a)^2 \\ll 1$. "
                  "Shuning uchun tekis kuchlanish holatidagi Guk qonuni "
                  "ishlatiladi (tmm-16)."),
                d("6. Zid-ziddiyat va uning maqbulligi",
                  r"\gamma_{xz} = 0 \ \text{(gipoteza)} \quad\text{lekin}\quad "
                  r"\tau_{xz} \ne 0 \ \text{(muvozanat uchun zarur)}",
                  "Nazariya ichki qarama-qarshilikka ega: sdvig "
                  "deformatsiyasi nol, lekin kesuvchi kuch nolga teng "
                  "emas. Bu maqbul, chunki sdvig energiyasi egilish "
                  "energiyasidan $(h/a)^2$ marta kichik — xuddi balka "
                  "nazariyasidagi kabi (mq-13)."),
                d("7. Xatolikning tartibi",
                  r"\frac{\text{xato}}{\text{yechim}} \sim "
                  r"\Big(\frac{h}{a}\Big)^2",
                  "Asimptotik tahlil ko'rsatadiki, Kirxhoff nazariyasining "
                  "nisbiy xatosi $(h/a)^2$ tartibida. $h/a = 1/20$ da bu "
                  "0,25 % — muhandislik uchun mutlaqo yetarli; "
                  "$h/a = 1/5$ da esa 4 % — chegaraviy."),
            ],
            meaning=(
                "Kirxhoff gipotezalarining mohiyati — **noma'lumlar sonini "
                "keskin kamaytirish**. Uch o'lchovli elastiklik masalasida "
                "15 ta noma'lum funksiya (3 ko'chish, 6 deformatsiya, "
                "6 kuchlanish) va ular uch o'zgaruvchiga bog'liq. "
                "Gipotezalardan keyin **bitta** funksiya $w(x,y)$ qoladi va "
                "u ikki o'zgaruvchiga bog'liq. Bu — modellashtirishning "
                "klassik almashuvi: aniqlikning $(h/a)^2$ ulushini "
                "yo'qotib, yechilmaydigan masalani yechiladigan qilamiz. "
                "Geometrik ma'nosi ham sodda: plastinani ko'p qavatli "
                "kitob deb tasavvur qiling, uning muqovasiga ninalar "
                "tik sanchilgan. Egilganda nina egilmaydi va aylanmaydi — "
                "u faqat varaqlar bilan birga buriladi, lekin har doim "
                "varaqlarga perpendikulyar qoladi. Shu tasavvur butun "
                "kinematikani beradi: $u = -z\\,\\partial w/\\partial x$ "
                "formulasidagi $z$ — ninadagi nuqtaning muqovadan "
                "masofasi, $\\partial w/\\partial x$ — muqovaning "
                "qiyaligi, minus — yuqori qatlamning siqilishi."
            ),
            equations=[
                eq(r"u = -z\frac{\partial w}{\partial x}, \quad "
                   r"v = -z\frac{\partial w}{\partial y}, \quad w = w(x, y)",
                   "Kirxhoff kinematikasi: butun 3D ko'chish maydoni "
                   "bitta funksiya orqali.", "Kirxhoff kinematikasi"),
                eq(r"\gamma_{xz} = \gamma_{yz} = 0, \qquad \varepsilon_{zz} = 0",
                   "Gipotezalarning matematik ifodasi.", "Kinematik cheklovlar"),
                eq(r"\sigma_x = \frac{E}{1-\nu^2}(\varepsilon_x + \nu\varepsilon_y)",
                   "Tekis kuchlanish holatidagi Guk qonuni.",
                   "Konstitutiv munosabat"),
                eq(r"\frac{h}{a} < \frac{1}{20}",
                   "Kirxhoff nazariyasining qo'llanish sharti.",
                   "Yupqalik sharti"),
            ],
            conditions=(
                "**Model qo'llanish shartlari** (hammasi tekshirilishi kerak):\n"
                "1. **Geometrik yupqalik:** $h/a < 1/20$ — aks holda "
                "sdvig deformatsiyasi sezilarli bo'ladi (Mindlin, pq-24);\n"
                "2. **Kichik og'ish:** $w_{\\max} < h/5$ — aks holda "
                "membrana kuchlari paydo bo'ladi (fon Karman, pq-18);\n"
                "3. **Chiziqli elastik material:** $\\sigma < \\sigma_{\\text{proporsionallik}}$;\n"
                "4. **Silliq yuklama:** konsentrlangan kuch yaqinida va "
                "chegaraga $\\sim h$ masofada yechim aniq emas "
                "(Sen-Venan prinsipi, mq-05).\n\n"
                "**O'rta sirtdagi chegaraviy shartlar** pq-05 da batafsil "
                "ko'rib chiqiladi; bu yerda ular $w$ va uning hosilalari "
                "orqali berilishi muhim."
            ),
            worked=WorkedExample(
                statement=(
                    "Uchta konstruksiya elementi berilgan: (a) bino "
                    "perekrytiyasi $6\\times8$ m, $h = 200$ mm; "
                    "(b) samolyot qanoti qoplamasi $a = 500$ mm, "
                    "$h = 2$ mm; (c) sanoat plitasi $a = 1{,}2$ m, "
                    "$h = 300$ mm. Har biri uchun mos nazariyani tanlang "
                    "va Kirxhoff nazariyasining kutilayotgan xatosini baholang."
                ),
                given=[
                    r"\text{(a) } a = 6\ \text{m},\ h = 0{,}2\ \text{m}",
                    r"\text{(b) } a = 0{,}5\ \text{m},\ h = 0{,}002\ \text{m}",
                    r"\text{(c) } a = 1{,}2\ \text{m},\ h = 0{,}3\ \text{m}",
                ],
                steps=[
                    st(r"\text{(a)}\quad \frac{h}{a} = \frac{0{,}2}{6} "
                       r"= 0{,}0333 = \frac{1}{30}",
                       "$1/30 < 1/20$ — yupqa plastina, Kirxhoff nazariyasi "
                       "to'liq o'rinli."),
                    st(r"\text{xato} \sim (h/a)^2 = 1{,}11\times10^{-3} = 0{,}11\ \%",
                       "Muhandislik aniqligidan ancha yuqori — beton "
                       "xossalarining tarqoqligi bundan o'nlab marta katta."),
                    st(r"\text{(b)}\quad \frac{h}{a} = \frac{2}{500} = 0{,}004 "
                       r"= \frac{1}{250}",
                       "Juda yupqa. Kirxhoff xatosi $1{,}6\\times10^{-5}$ — "
                       "ahamiyatsiz. Lekin bu yerda **boshqa** muammo "
                       "paydo bo'ladi."),
                    st(r"w_{\max} \ \text{tekshiruvi: yupqa qoplamada } "
                       r"w \sim h \ \text{oson erishiladi}",
                       "Og'ish qalinlikka taqqoslanadigan bo'lsa, "
                       "geometrik nochiziqlilik hukmron bo'ladi — fon "
                       "Karman nazariyasi (pq-18) kerak."),
                    st(r"\text{(c)}\quad \frac{h}{a} = \frac{0{,}3}{1{,}2} "
                       r"= 0{,}25 = \frac{1}{4}",
                       "$1/4 > 1/5$ — bu plastina emas, **qalin plita**. "
                       "Kirxhoff xatosi $(0{,}25)^2 = 6{,}25\\ \\%$ dan katta."),
                    st(r"\text{Tanlov: 3D FEM yoki hech bo'lmasa Mindlin nazariyasi}",
                       "Sdvig deformatsiyasi hissasi egilish hissasiga "
                       "taqqoslanadigan bo'lib qoladi."),
                ],
                answer=(
                    "(a) Kirxhoff, xato ≈ 0,11 % — mukammal mos; "
                    "(b) Kirxhoff kinematikasi o'rinli, lekin og'ish "
                    "kattaligi tekshirilishi va zarur bo'lsa fon Karman "
                    "nazariyasiga o'tilishi kerak; (c) Kirxhoff yaroqsiz "
                    "(xato > 6 %), Mindlin yoki 3D tahlil kerak."
                ),
                engineering_note=(
                    "Amaliy qoida: nazariyani tanlashda **ikkita** nisbat "
                    "tekshiriladi — $h/a$ (sdvig muhimmi?) va $w/h$ "
                    "(membrana kuchlari muhimmi?). Ular bir-biridan "
                    "mustaqil: juda yupqa plastinada sdvig ahamiyatsiz, "
                    "lekin nochiziqlilik hal qiluvchi bo'lishi mumkin; "
                    "qalin plitada esa aksincha."
                ),
            ),
            computation=Computation(
                caption=(
                    "Qalinlik nisbatining nazariya aniqligiga ta'sirini "
                    "baholash: Kirxhoff va Mindlin yechimlarini taqqoslash."
                ),
                code='''"""Kirxhoff gipotezalari: qo'llanish chegaralarini baholash."""
import numpy as np
from labkit import PARAMS, note, series, table, value

a = float(PARAMS.get("a", 6.0))          # plastina tomoni, m
h = float(PARAMS.get("h", 0.2))          # qalinlik, m
E = float(PARAMS.get("E", 30.0))*1e9     # Pa (beton)
nu = float(PARAMS.get("nu", 0.2))
qload = float(PARAMS.get("q", 5000.0))   # Pa

ratio = h/a
value("Qalinlik nisbati h/a", ratio, "—")
value("1/(h/a)", 1/ratio, "—")
value("Kutilayotgan nisbiy xato ~ (h/a)^2", ratio**2*100, "%")

if ratio < 0.05:
    kind = "yupqa plastina — Kirxhoff nazariyasi o'rinli"
elif ratio < 0.2:
    kind = "o'rtacha qalinlik — Mindlin nazariyasi tavsiya etiladi"
else:
    kind = "qalin plita — 3D tahlil kerak"
note(f"h/a = {ratio:.4f} ({1/ratio:.1f} ga teskari): {kind}.")

# Silindrik bikrlik
D = E*h**3/(12*(1 - nu**2))
value("Silindrik bikrlik D", D/1e6, "MN*m")

# Kvadrat, sharnirli tayanchli plastina, bir tekis yuklama (Navye 1-had)
# w_max = alpha * q a^4 / D, alpha ~ 0.00406 (kvadrat plastina)
alpha = 0.00406
w_kirch = alpha*qload*a**4/D
value("Maksimal og'ish (Kirxhoff)", w_kirch*1000, "mm")
value("w_max / h", w_kirch/h, "—")
value("w_max / a", w_kirch/a, "—")

if w_kirch/h > 0.2:
    note(f"w_max/h = {w_kirch/h:.3f} > 0.2 — geometrik nochiziqlilik "
         f"sezilarli, fon Karman nazariyasi (pq-18) kerak.")
else:
    note(f"w_max/h = {w_kirch/h:.3f} < 0.2 — kichik og'ish, chiziqli "
         f"nazariya o'rinli.")

# Mindlin tuzatmasi: sdvig hissasi (taxminiy)
G = E/(2*(1 + nu))
k_shear = 5.0/6.0
w_shear = qload*a**2/(k_shear*G*h)*0.0265    # sdvig hissasi (taxminiy koeffitsient)
w_mindlin = w_kirch + w_shear
value("Sdvig hissasi", w_shear*1000, "mm")
value("Mindlin og'ishi (taxminiy)", w_mindlin*1000, "mm")
value("Sdvig ulushi", 100*w_shear/w_mindlin, "%")

# --- h/a bo'yicha skanerlash ---
ratios = np.linspace(0.005, 0.30, 200)
share = []
for r_ in ratios:
    h_ = r_*a
    D_ = E*h_**3/(12*(1 - nu**2))
    wk = alpha*qload*a**4/D_
    ws = qload*a**2/(k_shear*G*h_)*0.0265
    share.append(100*ws/(wk + ws))
series("Sdvig hissasining ulushi", ratios.tolist(), share,
       xlabel="h/a", ylabel="Sdvig ulushi, %")
i5 = int(np.argmax(np.array(share) > 5.0)) if max(share) > 5 else -1
if i5 > 0:
    value("Sdvig 5 % ga yetadigan h/a", float(ratios[i5]), "—")
    note(f"h/a > {ratios[i5]:.3f} bo'lganda sdvig hissasi 5 % dan oshadi — "
         f"Kirxhoff nazariyasi shu yerdan boshlab yetarli emas.")

table("Plastinalarni qalinlik bo'yicha tasniflash",
      ["Turi", "h/a oralig'i", "Nazariya", "Tipik xato"],
      [["Juda yupqa (membrana)", "< 1/100", "Membrana yoki fon Karman",
        "chiziqli nazariya og'ishni oshirib yuboradi"],
       ["Yupqa", "1/100 … 1/20", "Kirxhoff-Lyav", "< 0.25 %"],
       ["O'rtacha qalinlik", "1/20 … 1/5", "Mindlin-Reissner", "0.25 … 4 %"],
       ["Qalin", "> 1/5", "3D elastiklik / FEM", "> 4 %"]])

table("Kirxhoff gipotezalari va ularning oqibatlari",
      ["Gipoteza", "Matematik ifoda", "Oqibat"],
      [["Normal normal qoladi", "gamma_xz = gamma_yz = 0",
        "phi_x = -dw/dx, burilish mustaqil emas"],
       ["Qalinlik o'zgarmaydi", "eps_zz = 0", "w = w(x, y), 3D -> 2D"],
       ["O'rta sirt cho'zilmaydi", "u0 = v0 = 0", "sof egilish, membrana yo'q"],
       ["sigma_zz e'tiborsiz", "sigma_zz ~ 0", "tekis kuchlanish Guk qonuni"]])

# Uch xil konstruksiya taqqoslashi
table("Amaliy misollar",
      ["Konstruksiya", "a, m", "h, m", "h/a", "Nazariya"],
      [[name, a_, h_, round(h_/a_, 4),
        ("Kirxhoff" if h_/a_ < 0.05 else
         "Mindlin" if h_/a_ < 0.2 else "3D")]
       for name, a_, h_ in [
           ("Bino perekrytiyasi", 6.0, 0.20),
           ("Qanot qoplamasi", 0.5, 0.002),
           ("Sanoat plitasi", 1.2, 0.30),
           ("Ko'prik plitasi", 12.0, 0.25),
           ("Elektron korpus", 0.15, 0.0015)]])
''',
                parameters=[
                    p("a", "Plastina tomoni a", 0.05, 20.0, 6.0, 0.05, "m"),
                    p("h", "Qalinlik h", 0.001, 1.0, 0.2, 0.001, "m"),
                    p("E", "Yung moduli E", 1.0, 400.0, 30.0, 1.0, "GPa"),
                    p("nu", "Puasson koeffitsienti ν", 0.0, 0.45, 0.2, 0.01),
                    p("q", "Yuklama q", 100.0, 100000.0, 5000.0, 100.0, "Pa"),
                ],
                expected_output=(
                    "h/a = 0,0333 (1/30) — yupqa plastina, kutilayotgan "
                    "xato 0,11 %; D = 20,8 MN·m, w_max ≈ 1,26 mm, "
                    "w/h = 0,0063 — chiziqli nazariya o'rinli. Sdvig "
                    "hissasi 5 % ga h/a ≈ 0,1 atrofida yetadi."
                ),
            ),
            visual=vis(
                kind="Kirxhoff kinematikasi",
                tool="React/SVG + Manim",
                description=(
                    "O'rta sirt va unga normal chiziqning egilishdan "
                    "oldingi va keyingi holati; qalinlik bo'yicha ko'chish epyurasi."
                ),
                how_to_draw=(
                    "React/SVG: plastina kesimi yon tomondan — ikkita "
                    "gorizontal chiziq (yuqori va pastki yuza) va ular "
                    "orasida punktir o'rta sirt. Deformatsiyadan keyingi "
                    "holat egri `<path>` bilan chiziladi (parabolik "
                    "yaqinlashuv yetarli). Bir necha nuqtada o'rta sirtga "
                    "**normal** qisqa kesmalar chiziladi — ular egilgandan "
                    "keyin ham to'g'ri va egri chiziqqa perpendikulyar "
                    "qoladi, bu gipotezaning butun mazmuni. Yonida "
                    "qalinlik bo'yicha epyura paneli: $u(z) = -z\\,dw/dx$ "
                    "chiziqli epyura (yuqorida manfiy, pastda musbat), "
                    "$\\varepsilon_x(z)$ ham chiziqli, $\\tau_{xz}(z)$ esa "
                    "parabolik — oxirgisi gipotezaga zid ekanligi alohida "
                    "yorliq bilan ko'rsatiladi. Og'ish kattaligi slayder "
                    "bilan boshqariladi; $w/h > 0{,}2$ bo'lganda ogohlantirish "
                    "chiqadi (issiq rang)."
                ),
            ),
            interp=(
                "Sdvig ulushi grafigi nazariya tanlashning aniq "
                "mezonini beradi: $h/a \\approx 0{,}1$ da sdvig hissasi "
                "5 % ga yetadi va Kirxhoff nazariyasi xatosi sezilarli "
                "bo'lib qoladi. Bu $1/20$ chegarasini sonli tasdiqlaydi — "
                "u o'zboshimchalik bilan tanlangan emas. Jadvaldagi "
                "amaliy misollar yana bir muhim xulosani beradi: "
                "samolyot qanoti qoplamasi ($h/a = 1/250$) Kirxhoff "
                "kinematikasi uchun ideal, lekin uning haqiqiy muammosi "
                "boshqa — bunday yupqa panel osongina qalinlikka "
                "taqqoslanadigan og'ishga erishadi va nochiziqli "
                "bo'lib qoladi. Demak 'juda yupqa' har doim 'juda "
                "oson hisoblanadi' degani emas. Sanoat plitasi esa "
                "($h/a = 1/4$) umuman plastina emas — uni plastina deb "
                "hisoblash 6 % dan katta xato beradi va bu xato "
                "og'ishni **kam** ko'rsatish tomonga, ya'ni xavfsizlikka "
                "zid tomonga bo'ladi."
            ),
            mistakes=[
                "Kirxhoff nazariyasini qalinlik nisbatini tekshirmasdan "
                "qo'llash. $h/a > 1/5$ da xato 6 % dan oshadi va u "
                "og'ishni kam ko'rsatadi — xavfli tomonga.",
                "$\\gamma_{xz} = 0$ gipotezasidan $\\tau_{xz} = 0$ deb "
                "xulosa chiqarish. Kesuvchi kuchlanish muvozanat uchun "
                "zarur va u nolga teng emas; gipoteza faqat "
                "**deformatsiyani** e'tiborsiz qoldiradi.",
                "Faqat $h/a$ ni tekshirib, $w/h$ ni unutish. Juda yupqa "
                "plastinada chiziqli nazariya og'ishni bir necha marta "
                "oshirib ko'rsatishi mumkin.",
                "O'rta sirtni plastinaning pastki yoki yuqori yuzasi deb "
                "olish. Barcha formulalarda $z$ o'rta sirtdan sanaladi; "
                "aks holda kuchlanish epyurasi xato chiqadi.",
            ],
            quiz=[
                q("Kirxhoff–Lyav gipotezalarining asosiy maqsadi nima?",
                  "Uch o'lchovli elastiklik masalasini bitta noma'lum "
                  "funksiyali ($w(x,y)$) ikki o'lchovli masalaga keltirish — "
                  "noma'lumlar sonini 15 tadan 1 taga tushirish.",
                  "konseptual"),
                q("$u = -z\\,\\partial w/\\partial x$ formulasidagi minus "
                  "ishora nimani bildiradi?",
                  "Plastina pastga egilganda ($\\partial w/\\partial x > 0$) "
                  "yuqori qatlam ($z > 0$) orqaga siljiydi, ya'ni siqiladi. "
                  "Bu balkadagi kabi kinematika.", "konseptual"),
                q("$a = 4$ m, $h = 150$ mm. Qaysi nazariya kerak?",
                  "$h/a = 0{,}0375 = 1/27 < 1/20$ — Kirxhoff nazariyasi "
                  "o'rinli, kutilayotgan xato $\\approx 0{,}14$ %.", "hisob"),
                q("Nima uchun nazariya ichida qarama-qarshilik bor va "
                  "u nima uchun maqbul?",
                  "$\\gamma_{xz} = 0$ deyiladi, lekin $\\tau_{xz} \\ne 0$. "
                  "Maqbul, chunki sdvig energiyasi egilish energiyasidan "
                  "$(h/a)^2$ marta kichik — xuddi balka nazariyasidagi kabi.",
                  "talqin"),
                q("Kodda sdvig ulushi grafigi nimani ko'rsatadi?",
                  "Sdvig deformatsiyasi hissasining umumiy og'ishdagi "
                  "ulushini $h/a$ ga bog'liq holda. U $h/a \\approx 0{,}1$ "
                  "da 5 % ga yetadi va $1/20$ chegarasini sonli asoslaydi.",
                  "kod"),
                q("Nazariyani tanlashda qaysi ikki nisbat tekshiriladi?",
                  "$h/a$ — sdvig deformatsiyasi muhimmi (Mindlin kerakmi); "
                  "$w/h$ — membrana kuchlari muhimmi (fon Karman kerakmi). "
                  "Ular o'zaro mustaqil.", "talqin"),
            ],
            bridge=(
                "Gipotezalar ko'chish maydonini bitta funksiyaga keltirdi. "
                "Endi shu funksiyadan deformatsiyalarni hisoblaymiz va "
                "plastina egilishining geometrik tavsifini — egrilik "
                "tushunchasini — kiritamiz."
            ),
            research=(
                "Kirxhoff gipotezalarining asimptotik asoslanishini "
                "o'rganing: $\\epsilon = h/a$ kichik parametr bo'yicha "
                "uch o'lchovli elastiklik masalasini yoying va nolinchi "
                "tartibda aynan Kirxhoff nazariyasi chiqishini ko'rsating. "
                "Keyingi tartibdagi tuzatma nimani beradi va u "
                "Reissner nazariyasi bilan qanday bog'lanadi? Ciarlet va "
                "Destuynder ishlaridan foydalaning."
            ),
            manim_ref=manim(
                scene="KirchhoffHypothesisScene",
                module="animatsiya/scenes/pq_plate_basics.py",
                title="Kirxhoff gipotezasi: normal normal qoladi",
                summary=(
                    "Plastina kesimi egiladi; o'rta sirtga sanchilgan "
                    "normal kesmalar egilgandan keyin ham to'g'ri va "
                    "egri sirtga perpendikulyar qolishi animatsiya "
                    "qilinadi, ko'chish epyurasi bir vaqtda quriladi."
                ),
            ),
        ),
    ),

    # ------------------------------------------------------------------ pq-02
    Topic(
        id="pq-02",
        subject_id=S, module_id=M, order=2,
        title="Plastina deformatsiyasi kinematikasi: egrilik va buralish tenzori",
        description=(
            "Kirxhoff kinematikasidan deformatsiyalarni hisoblash, egrilik "
            "va buralish tushunchalari, egrilik tenzori, uning bosh "
            "qiymatlari va Mor doirasi bilan tahlili."
        ),
        learning_objective=(
            "Berilgan og'ish funksiyasidan deformatsiya maydonini "
            "hisoblash, egrilik tenzorini qurish va uning bosh "
            "yo'nalishlarini aniqlash."
        ),
        prerequisites=["pq-01", "tmm-05"],
        mathematical_core=(
            "Ikkinchi tartibli xususiy hosilalar, egrilik tenzori "
            "$\\kappa_{\\alpha\\beta} = -\\partial^2 w/\\partial x_\\alpha"
            "\\partial x_\\beta$, xususiy qiymatlar masalasi, Gauss va "
            "o'rtacha egriliklar."
        ),
        engineering_application=(
            "Egilgan sirt shaklini tahlil qilish, qoliplash "
            "(forming) jarayonlari, kompozit qatlamlarning yo'nalishini "
            "tanlash, tensegriti va qobiq shakllarini loyihalash."
        ),
        computational_component=(
            "Og'ish maydonidan egrilik tenzorini sonli hisoblash, bosh "
            "egriliklarni topish va Gauss egriligi belgisiga qarab sirt "
            "turini aniqlash."
        ),
        visualization_component=(
            "Egrilik maydonining rangli tasviri, bosh yo'nalishlar "
            "chiziqlari (curvature trajectories), Mor doirasi."
        ),
        research_extension=(
            "Gauss egriligining Theorema Egregium bilan bog'lanishini "
            "o'rganing: nima uchun tekis plastinani cho'zmasdan sferaga "
            "aylantirib bo'lmaydi va bu qobiq ishlab chiqarishga qanday ta'sir qiladi?"
        ),
        difficulty="asosiy",
        previous_link=(
            "pq-01 da ko'chish maydoni $u = -z\\,\\partial w/\\partial x$ "
            "ko'rinishida olindi. tmm-05 dagi deformatsiya tenzori ta'rifini "
            "shu maydonga qo'llasak, plastina deformatsiyasining to'liq "
            "tavsifi hosil bo'ladi."
        ),
        next_topic="pq-03",
        estimated_minutes=85,
        tags=["egrilik", "deformatsiya", "plastina", "tenzor"],
        lesson=_lesson(
            problem=(
                "Kompozit plastina uchun tolalar yo'nalishini tanlash kerak. "
                "Tola maksimal deformatsiya yo'nalishida joylashtirilsa, "
                "konstruksiya eng samarali bo'ladi. Lekin plastina "
                "egilganda deformatsiya har bir nuqtada har xil "
                "yo'nalishda va har xil kattalikda bo'ladi. Qaysi "
                "yo'nalish 'asosiy'? Savol tanish: bu tmm-08 dagi bosh "
                "kuchlanishlar masalasining plastinadagi analogi, faqat "
                "endi kuchlanish o'rnida **egrilik** turadi."
            ),
            concepts=[
                c("Egrilik (curvature, $\\kappa$)",
                  "O'rta sirtning berilgan yo'nalishdagi egilish o'lchovi: "
                  "$\\kappa_x = -\\partial^2 w/\\partial x^2$. Birligi 1/m. "
                  "Egrilik radiusi $\\rho = 1/\\kappa$."),
                c("Buralish (twist, $\\kappa_{xy}$)",
                  "$\\kappa_{xy} = -\\partial^2 w/\\partial x\\partial y$ — "
                  "sirt 'egar' shaklida buralishini tavsiflaydi. "
                  "Nolga teng bo'lsa, $x$ va $y$ bosh yo'nalishlar."),
                c("Egrilik tenzori",
                  "$\\kappa_{\\alpha\\beta}$ — ikkinchi tartibli simmetrik "
                  "tenzor ($2\\times2$). Kuchlanish tenzori kabi barcha "
                  "tenzor xossalariga ega: invariantlar, bosh qiymatlar, "
                  "Mor doirasi."),
                c("Bosh egriliklar (principal curvatures)",
                  "Egrilik tenzorining xususiy qiymatlari $\\kappa_1, "
                  "\\kappa_2$ — maksimal va minimal egriliklar; ularga mos "
                  "yo'nalishlarda buralish nolga teng."),
                c("Gauss egriligi (Gaussian curvature)",
                  "$K = \\kappa_1\\kappa_2$ — sirtning ichki xossasi. "
                  "$K > 0$ — sinklastik (kosa), $K < 0$ — antiklastik "
                  "(egar), $K = 0$ — yoyiladigan (silindr)."),
                c("O'rtacha egrilik (mean curvature)",
                  "$H = (\\kappa_1 + \\kappa_2)/2$ — egrilik tenzorining "
                  "birinchi invarianti; sirt taranglik masalalarida markaziy."),
            ],
            derivation=[
                d("1. Kirxhoff ko'chishlaridan deformatsiyaga o'tish",
                  r"\varepsilon_x = \frac{\partial u}{\partial x} "
                  r"= \frac{\partial}{\partial x}\Big(-z\frac{\partial w}"
                  r"{\partial x}\Big) = -z\frac{\partial^2 w}{\partial x^2}",
                  "tmm-05 dagi deformatsiya ta'rifini pq-01 dagi ko'chish "
                  "maydoniga qo'llaymiz. $z$ ko'paytuvchi chiqib turadi — "
                  "deformatsiya qalinlik bo'yicha chiziqli."),
                d("2. Qolgan deformatsiyalar",
                  r"\varepsilon_y = -z\frac{\partial^2 w}{\partial y^2}, \qquad "
                  r"\gamma_{xy} = \frac{\partial u}{\partial y} + "
                  r"\frac{\partial v}{\partial x} = -2z\frac{\partial^2 w}"
                  r"{\partial x\partial y}",
                  "Siljish deformatsiyasida ikkita bir xil had qo'shiladi, "
                  "shuning uchun koeffitsient 2 paydo bo'ladi. Bu "
                  "muhandislik siljish deformatsiyasi (Voygt notatsiyasi)."),
                d("3. Egrilik tushunchasini kiritish",
                  r"\kappa_x = -\frac{\partial^2 w}{\partial x^2}, \quad "
                  r"\kappa_y = -\frac{\partial^2 w}{\partial y^2}, \quad "
                  r"\kappa_{xy} = -\frac{\partial^2 w}{\partial x\partial y}",
                  "Ta'rif shunday tanlanganki, deformatsiya sodda "
                  "ko'rinishga ega bo'lsin: $\\varepsilon_x = z\\kappa_x$, "
                  "$\\varepsilon_y = z\\kappa_y$, $\\gamma_{xy} = 2z\\kappa_{xy}$. "
                  "Minus ishora egilish musbat bo'lganda egrilik musbat "
                  "bo'lishi uchun."),
                d("4. Egrilik — tenzor",
                  r"\kappa_{\alpha\beta} = -\frac{\partial^2 w}"
                  r"{\partial x_\alpha\partial x_\beta}, \qquad "
                  r"\alpha, \beta \in \{1, 2\}",
                  "Ikkinchi tartibli xususiy hosilalar tenzori aralash "
                  "hosilalarning tengligi tufayli simmetrik. Demak u "
                  "koordinata aylanishida tenzor qonuni bo'yicha "
                  "o'zgaradi — kuchlanish tenzori kabi."),
                d("5. Aylantirish formulasi",
                  r"\kappa_n = \kappa_x\cos^2\theta + \kappa_y\sin^2\theta "
                  r"+ 2\kappa_{xy}\sin\theta\cos\theta",
                  "$\\theta$ burchakka burilgan yo'nalishdagi egrilik. "
                  "Bu formula Mor doirasi bilan bir xil tuzilishga ega "
                  "(mq-21, tmm-08) — chunki matematik obyekt bir xil."),
                d("6. Bosh egriliklar",
                  r"\kappa_{1,2} = \frac{\kappa_x + \kappa_y}{2} \pm "
                  r"\sqrt{\Big(\frac{\kappa_x - \kappa_y}{2}\Big)^2 "
                  r"+ \kappa_{xy}^2}, \qquad "
                  r"\tan 2\theta_0 = \frac{2\kappa_{xy}}{\kappa_x - \kappa_y}",
                  "Xususiy qiymatlar masalasining $2\\times2$ holdagi "
                  "yechimi. Bosh yo'nalishlarda buralish nolga teng — "
                  "sirt shu yo'nalishlarda 'sof' egiladi."),
                d("7. Invariantlar: Gauss va o'rtacha egriliklar",
                  r"H = \frac{\kappa_1 + \kappa_2}{2} = \frac{\kappa_x + \kappa_y}{2}, "
                  r"\qquad K = \kappa_1\kappa_2 = \kappa_x\kappa_y - \kappa_{xy}^2",
                  "Ikkala kattalik koordinata tanlashga bog'liq emas — "
                  "bu ularning invariant ekanligini bildiradi. $K$ — "
                  "aynan tenzorning determinanti, $H$ — izining yarmi."),
            ],
            meaning=(
                "Gauss egriligi $K = \\kappa_1\\kappa_2$ — bu mavzudagi "
                "eng chuqur tushuncha. Gaussning Theorema Egregium "
                "('ajoyib teorema') ga ko'ra $K$ **sirtning ichki xossasi**: "
                "uni sirt ichida yashovchi mavjudot masofalarni o'lchab "
                "aniqlay oladi, sirtdan tashqariga chiqmasdan. Amaliy "
                "oqibati juda muhim: tekis plastinaning $K = 0$, sferaning "
                "$K = 1/R^2 > 0$. Ularni bir-biriga cho'zmasdan "
                "(deformatsiyasiz) aylantirib bo'lmaydi — shuning uchun "
                "globusni qog'ozga xaritalash har doim buzilish beradi va "
                "apelsin po'stini tekis yoyib bo'lmaydi. Muhandislikda: "
                "silindrik qobiqni tekis listdan oddiygina egib yasash "
                "mumkin ($K = 0$, yoyiladigan sirt), sferik qobiqni esa "
                "faqat cho'zish, shtamplash yoki bo'laklardan payvandlash "
                "bilan yasash kerak. Buralish $\\kappa_{xy}$ ning ma'nosi "
                "ham geometrik: u nolga teng bo'lmagan nuqtalarda sirt "
                "'egar' shaklida buraladi — kvadrat plastinaning "
                "burchaklarida aynan shunday bo'ladi va bu keyinchalik "
                "burchaklarni ko'tarib yuborishga (corner uplift) olib keladi."
            ),
            equations=[
                eq(r"\varepsilon_x = z\kappa_x, \quad \varepsilon_y = z\kappa_y, "
                   r"\quad \gamma_{xy} = 2z\kappa_{xy}",
                   "Deformatsiyalar egriliklar orqali; qalinlik bo'yicha chiziqli.",
                   "Deformatsiya-egrilik"),
                eq(r"\kappa_{\alpha\beta} = -\frac{\partial^2 w}"
                   r"{\partial x_\alpha \partial x_\beta}",
                   "Egrilik tenzorining ta'rifi.", "Egrilik tenzori"),
                eq(r"K = \kappa_x\kappa_y - \kappa_{xy}^2, \qquad "
                   r"H = \frac{\kappa_x + \kappa_y}{2}",
                   "Gauss va o'rtacha egriliklar — egrilik tenzorining "
                   "invariantlari.", "Egrilik invariantlari"),
                eq(r"\kappa_n = \kappa_x\cos^2\theta + \kappa_y\sin^2\theta "
                   r"+ \kappa_{xy}\sin 2\theta",
                   "Ixtiyoriy yo'nalishdagi egrilik (Eyler formulasi).",
                   "Egrilikni aylantirish"),
            ],
            conditions=(
                "Bu mavzuda chegaraviy shartlar emas, balki **kinematik "
                "moslik** sharti muhim. Egrilik tenzori ixtiyoriy "
                "bo'lolmaydi — u bitta $w(x,y)$ funksiyadan olinadi, "
                "shuning uchun quyidagi moslik shartini qanoatlantiradi:\n"
                "$$\\frac{\\partial^2\\kappa_x}{\\partial y^2} + "
                "\\frac{\\partial^2\\kappa_y}{\\partial x^2} = "
                "2\\frac{\\partial^2\\kappa_{xy}}{\\partial x\\partial y}.$$\n"
                "Bu tmm-05 dagi Sen-Venan moslik shartining plastinadagi "
                "ko'rinishi: aralash hosilalarning tartibi ahamiyatsiz "
                "bo'lgani uchun avtomatik bajariladi.\n\n"
                "**Amaliy ahamiyati:** agar egrilik maydoni tajribadan "
                "(masalan, optik o'lchovdan) olingan bo'lsa, bu shart "
                "ma'lumotlarning ziddiyatsizligini tekshirish uchun ishlatiladi."
            ),
            worked=WorkedExample(
                statement=(
                    "Kvadrat plastinaning og'ish maydoni "
                    "$w(x,y) = w_0\\sin\\frac{\\pi x}{a}\\sin\\frac{\\pi y}{a}$ "
                    "ko'rinishida berilgan ($a = 3$ m, $w_0 = 8$ mm). "
                    "(a) Markazdagi ($x = y = a/2$) egrilik tenzorini "
                    "toping. (b) Burchakka yaqin nuqtadagi "
                    "($x = y = a/4$) egrilik tenzorini va bosh "
                    "egriliklarni hisoblang. (c) Gauss egriligining "
                    "belgisini ikkala nuqtada aniqlang va sirt turini ayting."
                ),
                given=[
                    r"w = w_0\sin\frac{\pi x}{a}\sin\frac{\pi y}{a}",
                    r"a = 3\ \text{m},\ w_0 = 8\times10^{-3}\ \text{m}",
                ],
                steps=[
                    st(r"\kappa_x = -\frac{\partial^2 w}{\partial x^2} "
                       r"= w_0\Big(\frac{\pi}{a}\Big)^2\sin\frac{\pi x}{a}"
                       r"\sin\frac{\pi y}{a}",
                       "Sinusni ikki marta differensiallash minus beradi, "
                       "ta'rifdagi minus bilan birga musbat chiqadi."),
                    st(r"\kappa_{xy} = -\frac{\partial^2 w}{\partial x\partial y} "
                       r"= -w_0\Big(\frac{\pi}{a}\Big)^2\cos\frac{\pi x}{a}"
                       r"\cos\frac{\pi y}{a}",
                       "Aralash hosila ikkita kosinus beradi — markazda "
                       "nolga teng, burchaklarda maksimal."),
                    st(r"\Big(\frac{\pi}{a}\Big)^2 = \Big(\frac{3{,}1416}{3}\Big)^2 "
                       r"= 1{,}0966\ \text{m}^{-2}; \quad "
                       r"w_0\Big(\frac{\pi}{a}\Big)^2 = 8{,}77\times10^{-3}\ \text{m}^{-1}",
                       "Umumiy ko'paytuvchi — barcha egriliklar shu "
                       "qiymatdan oshmaydi."),
                    st(r"\text{Markaz } (a/2, a/2): \ \kappa_x = \kappa_y "
                       r"= 8{,}77\times10^{-3}\ \text{m}^{-1}, \ \kappa_{xy} = 0",
                       "$\\sin(\\pi/2) = 1$, $\\cos(\\pi/2) = 0$. "
                       "Buralish nol — har qanday yo'nalish bosh yo'nalish "
                       "(izotrop nuqta)."),
                    st(r"K = \kappa_x\kappa_y - \kappa_{xy}^2 = "
                       r"(8{,}77\times10^{-3})^2 = 7{,}69\times10^{-5}\ \text{m}^{-2} > 0",
                       "Musbat Gauss egriligi — sirt markazda **sinklastik** "
                       "(kosa shaklida), ikkala yo'nalishda bir tomonga egilgan."),
                    st(r"\text{Nuqta } (a/4, a/4): \ \sin\frac{\pi}{4} = "
                       r"\cos\frac{\pi}{4} = 0{,}7071 \Rightarrow "
                       r"\kappa_x = \kappa_y = 4{,}39\times10^{-3}, \ "
                       r"\kappa_{xy} = -4{,}39\times10^{-3}\ \text{m}^{-1}",
                       "Bu yerda buralish egriliklar bilan bir xil kattalikda."),
                    st(r"\kappa_{1,2} = 4{,}39\times10^{-3} \pm "
                       r"\sqrt{0 + (4{,}39\times10^{-3})^2} = "
                       r"8{,}77\times10^{-3}\ \text{va}\ 0",
                       "Bosh egriliklar: biri maksimal, ikkinchisi aynan nol. "
                       "Bosh yo'nalishlar $\\theta_0 = \\pm 45°$."),
                    st(r"K = \kappa_1\kappa_2 = 0 \;\Rightarrow\; "
                       r"\text{yoyiladigan (silindrsimon) nuqta}",
                       "Bu nuqtada sirt bitta yo'nalishda egilgan, "
                       "ikkinchisida tekis — mahalliy ravishda silindr."),
                ],
                answer=(
                    "Markazda $\\kappa_x = \\kappa_y = 8{,}77\\times10^{-3}$ "
                    "1/m, $\\kappa_{xy} = 0$, $K > 0$ — sinklastik; "
                    "$(a/4, a/4)$ nuqtada $\\kappa_1 = 8{,}77\\times10^{-3}$, "
                    "$\\kappa_2 = 0$, $K = 0$ — yoyiladigan nuqta, bosh "
                    "yo'nalishlar $\\pm 45°$."
                ),
                engineering_note=(
                    "Bosh egriliklar kompozit plastinada tola yo'nalishini "
                    "tanlashning asosi: maksimal egrilik yo'nalishida "
                    "maksimal deformatsiya, demak u yerda eng bikr qatlam "
                    "kerak. Diagonal ($\\pm 45°$) yo'nalishda joylashgan "
                    "tolalar esa buralishni samarali qabul qiladi — "
                    "shuning uchun kompozit qatlamlashda $[0/\\pm45/90]_s$ "
                    "kabi kvazi-izotrop paketlar standart hisoblanadi."
                ),
            ),
            computation=Computation(
                caption=(
                    "Og'ish maydonidan egrilik tenzorini sonli hisoblash, "
                    "bosh egriliklar va Gauss egriligi bo'yicha sirt turini aniqlash."
                ),
                code='''"""Plastina kinematikasi: egrilik tenzori va bosh egriliklar."""
import numpy as np
from labkit import PARAMS, note, series, table, value

a = float(PARAMS.get("a", 3.0))          # plastina tomoni, m
w0 = float(PARAMS.get("w0", 8.0))/1000.0 # maksimal og'ish, m
h = float(PARAMS.get("h", 0.15))         # qalinlik, m
xq = float(PARAMS.get("xq", 0.25))       # tekshirish nuqtasi x/a
yq = float(PARAMS.get("yq", 0.25))       # tekshirish nuqtasi y/a

n = 81
x = np.linspace(0.0, a, n)
y = np.linspace(0.0, a, n)
X, Y = np.meshgrid(x, y, indexing="ij")
W = w0*np.sin(np.pi*X/a)*np.sin(np.pi*Y/a)

# --- Analitik egriliklar ---
k = (np.pi/a)**2
KX = w0*k*np.sin(np.pi*X/a)*np.sin(np.pi*Y/a)
KY = KX.copy()
KXY = -w0*k*np.cos(np.pi*X/a)*np.cos(np.pi*Y/a)

value("Umumiy ko'paytuvchi w0*(pi/a)^2", w0*k, "1/m")
value("Maksimal egrilik (markazda)", float(np.max(KX)), "1/m")
value("Maksimal buralish (burchakda)", float(np.max(np.abs(KXY))), "1/m")
value("Minimal egrilik radiusi", 1/float(np.max(KX)), "m")

# --- Sonli hosilalar bilan tekshirish ---
dx = x[1] - x[0]
KX_num = -np.gradient(np.gradient(W, dx, axis=0), dx, axis=0)
KXY_num = -np.gradient(np.gradient(W, dx, axis=0), dx, axis=1)
err_kx = float(np.max(np.abs(KX_num[2:-2, 2:-2] - KX[2:-2, 2:-2])))
err_kxy = float(np.max(np.abs(KXY_num[2:-2, 2:-2] - KXY[2:-2, 2:-2])))
note(f"Sonli va analitik egriliklar farqi: kappa_x {err_kx:.3e} 1/m, "
     f"kappa_xy {err_kxy:.3e} 1/m — markaziy ayirmalar O(dx^2) aniqlikda.")

# --- Tanlangan nuqtada tenzor tahlili ---
def analyse(xi, yi):
    kx = w0*k*np.sin(np.pi*xi)*np.sin(np.pi*yi)
    ky = kx
    kxy = -w0*k*np.cos(np.pi*xi)*np.cos(np.pi*yi)
    T = np.array([[kx, kxy], [kxy, ky]])
    vals, vecs = np.linalg.eigh(T)
    k1, k2 = float(vals[1]), float(vals[0])
    theta = np.degrees(np.arctan2(vecs[1, 1], vecs[0, 1]))
    return kx, ky, kxy, k1, k2, theta


for label, xi, yi in [("Markaz", 0.5, 0.5), ("Tekshirish nuqtasi", xq, yq),
                      ("Burchak yaqini", 0.1, 0.1)]:
    kx, ky, kxy, k1, k2, th = analyse(xi, yi)
    Kg = k1*k2
    Hm = 0.5*(k1 + k2)
    surf = ("sinklastik (kosa)" if Kg > 1e-12 else
            "antiklastik (egar)" if Kg < -1e-12 else "yoyiladigan (silindr)")
    note(f"{label} (x/a={xi:.2f}, y/a={yi:.2f}): "
         f"kappa_x={kx:.5f}, kappa_xy={kxy:.5f}, "
         f"kappa_1={k1:.5f}, kappa_2={k2:.5f} 1/m; "
         f"K={Kg:.3e} 1/m^2, H={Hm:.5f} 1/m -> {surf}; "
         f"bosh yo'nalish {th:.1f} deg.")

kx, ky, kxy, k1, k2, th = analyse(xq, yq)
value("kappa_x (tekshirish nuqtasi)", kx, "1/m")
value("kappa_y (tekshirish nuqtasi)", ky, "1/m")
value("kappa_xy (tekshirish nuqtasi)", kxy, "1/m")
value("Bosh egrilik kappa_1", k1, "1/m")
value("Bosh egrilik kappa_2", k2, "1/m")
value("Gauss egriligi K", k1*k2, "1/m2")
value("O'rtacha egrilik H", 0.5*(k1 + k2), "1/m")
value("Bosh yo'nalish burchagi", th, "deg")

# --- Deformatsiyalar (yuqori yuzada z = h/2) ---
z = h/2
value("eps_x (yuqori yuza, tekshirish nuqtasi)", z*kx*1e6, "mkm/m")
value("gamma_xy (yuqori yuza)", 2*z*kxy*1e6, "mkm/m")
value("Maksimal deformatsiya (markaz, z=h/2)", z*float(np.max(KX))*1e6, "mkm/m")

# --- Diagonal bo'ylab profillar ---
diag = np.linspace(0.0, 1.0, 200)
kx_d = w0*k*np.sin(np.pi*diag)**2
kxy_d = -w0*k*np.cos(np.pi*diag)**2
Kg_d = kx_d**2 - kxy_d**2
series("kappa_x diagonal bo'ylab", diag.tolist(), kx_d.tolist(),
       xlabel="Diagonal bo'yicha nisbiy masofa", ylabel="kappa_x, 1/m")
series("kappa_xy diagonal bo'ylab", diag.tolist(), kxy_d.tolist(),
       xlabel="Diagonal bo'yicha nisbiy masofa", ylabel="kappa_xy, 1/m")
series("Gauss egriligi K diagonal bo'ylab", diag.tolist(), Kg_d.tolist(),
       xlabel="Diagonal bo'yicha nisbiy masofa", ylabel="K, 1/m2")

n_neg = int(np.sum(Kg_d < -1e-14))
note(f"Diagonal bo'ylab {n_neg}/{len(Kg_d)} nuqtada K < 0 (antiklastik) — "
     f"burchaklarga yaqin sohada sirt egar shaklida buraladi. Aynan shu "
     f"burchaklarni ko'tarishga (corner uplift) olib keladi.")

# --- Egrilikni burchak bo'yicha aylantirish (Mor doirasi) ---
th_range = np.linspace(0, 180, 181)
kn = (kx*np.cos(np.radians(th_range))**2 + ky*np.sin(np.radians(th_range))**2
      + kxy*np.sin(2*np.radians(th_range)))
series("kappa_n(theta) — Mor doirasi", th_range.tolist(), kn.tolist(),
       xlabel="Burchak theta, deg", ylabel="kappa_n, 1/m")
value("max kappa_n (skanerlash)", float(np.max(kn)), "1/m")
value("min kappa_n (skanerlash)", float(np.min(kn)), "1/m")
note(f"Skanerlash maksimumi {np.max(kn):.5f} va xususiy qiymat "
     f"kappa_1 = {k1:.5f} mos keladi — tenzor tahlili tasdiqlandi.")

table("Gauss egriligi va sirt turlari",
      ["K belgisi", "Sirt turi", "Misol", "Tekis listdan yasash"],
      [["K > 0", "Sinklastik (kosa)", "Sfera, ellipsoid", "Faqat cho'zish bilan"],
       ["K = 0", "Yoyiladigan", "Silindr, konus", "Oddiy egish bilan"],
       ["K < 0", "Antiklastik (egar)", "Giperbolik paraboloid",
        "Faqat siqish/cho'zish bilan"]])
''',
                parameters=[
                    p("a", "Plastina tomoni a", 0.2, 20.0, 3.0, 0.1, "m"),
                    p("w0", "Maksimal og'ish w₀", 0.1, 100.0, 8.0, 0.1, "mm"),
                    p("h", "Qalinlik h", 0.005, 1.0, 0.15, 0.005, "m"),
                    p("xq", "Tekshirish nuqtasi x/a", 0.05, 0.95, 0.25, 0.05),
                    p("yq", "Tekshirish nuqtasi y/a", 0.05, 0.95, 0.25, 0.05),
                ],
                expected_output=(
                    "w₀(π/a)² = 8,77×10⁻³ 1/m; markazda κ_x = κ_y = "
                    "8,77×10⁻³, κ_xy = 0, K > 0 (sinklastik); (0,25; 0,25) "
                    "nuqtada κ₁ = 8,77×10⁻³, κ₂ = 0, K = 0 (yoyiladigan), "
                    "bosh yo'nalish 45°."
                ),
            ),
            visual=vis(
                kind="Egrilik maydoni va bosh yo'nalishlar",
                tool="React/SVG",
                description=(
                    "Egrilik komponentalarining rangli xaritasi, bosh "
                    "yo'nalishlar chiziqchalari va egrilik Mor doirasi."
                ),
                how_to_draw=(
                    "React/SVG: plastina yuzasi $20\\times20$ kataklarga "
                    "bo'linadi; har bir katak $\\kappa_x$, $\\kappa_{xy}$ "
                    "yoki $K$ qiymatiga qarab bo'yaladi — ikki tomonlama "
                    "(diverging) shkala: musbat egrilik issiq rangda, "
                    "manfiy sovuqda, nol neytral. Ustiga bosh yo'nalishlar "
                    "**krest** ko'rinishida chiziladi: har bir katakda "
                    "ikkita perpendikulyar kesma, uzunliklari "
                    "$|\\kappa_1|$ va $|\\kappa_2|$ ga mutanosib, "
                    "burchagi $\\theta_0$. Bu 'egrilik traektoriyalari' "
                    "tasviri bir qarashda kompozit tola yo'nalishini "
                    "aytib beradi. Mor doirasi alohida panelda: markazi "
                    "$H$ da, radiusi $(\\kappa_1-\\kappa_2)/2$; joriy "
                    "nuqtaga mos $(\\kappa_x, \\kappa_{xy})$ va "
                    "$(\\kappa_y, -\\kappa_{xy})$ nuqtalari belgilanadi "
                    "va ular diametr bilan tutashtiriladi. Tekshirish "
                    "nuqtasi slayderlar bilan siljitilganda ikkala panel "
                    "sinxron yangilanadi."
                ),
            ),
            interp=(
                "Diagonal bo'ylab Gauss egriligi grafigi eng ma'lumotli: "
                "u markazda musbat, burchaklarga yaqinlashganda esa "
                "manfiy bo'ladi. Demak bir xil plastina bir joyda "
                "'kosa', boshqa joyda 'egar' shaklida. Bu shunchaki "
                "geometrik qiziqish emas — antiklastik burchaklarda "
                "plastina yuqoriga ko'tarilishga intiladi (corner "
                "uplift), shuning uchun erkin tayangan kvadrat "
                "plastinaning burchaklarini ushlab turish uchun maxsus "
                "ankerlar qo'yiladi. Agar ular yo'q bo'lsa, burchaklar "
                "ko'tariladi va yuklama qayta taqsimlanadi — hisoblangan "
                "kuchlanish taqsimoti buziladi. Sonli va analitik "
                "hosilalarning $10^{-6}$ tartibidagi farqi esa markaziy "
                "ayirmalar sxemasining $O(\\Delta x^2)$ aniqligini "
                "tasdiqlaydi; bu 5-fanda chekli ayirmalar usulini "
                "o'rganishga tayyorgarlik. Va nihoyat, Mor doirasi "
                "skanerlashi xususiy qiymatlar bilan to'liq mos "
                "tushishi — ikki mustaqil usulning bir xil javob "
                "berishi — tenzor tahlilining to'g'riligini isbotlaydi."
            ),
            mistakes=[
                "Buralish egriligida koeffitsientni unutish: "
                "$\\gamma_{xy} = 2z\\kappa_{xy}$, ya'ni ikkilangan. "
                "Ba'zi darsliklarda $\\kappa_{xy}$ o'zi ikkilangan "
                "qilib ta'riflanadi — manbani tekshirish shart.",
                "Egrilikni og'ishning birinchi hosilasi (qiyalik) deb "
                "olish. Egrilik — **ikkinchi** hosila; qiyalik burilish "
                "burchagini beradi.",
                "$K = \\kappa_x\\kappa_y$ deb yozib, $\\kappa_{xy}^2$ "
                "hadini unutish. Bu faqat bosh o'qlarda to'g'ri.",
                "Egrilik maksimal bo'lgan joyda kuchlanish ham maksimal "
                "deb o'ylash. Kuchlanish egrilikning **kombinatsiyasiga** "
                "bog'liq ($\\sigma_x \\propto \\kappa_x + \\nu\\kappa_y$), "
                "shuning uchun maksimumlar joyi mos kelmasligi mumkin.",
            ],
            quiz=[
                q("Egrilik va deformatsiya qanday bog'langan?",
                  "$\\varepsilon_x = z\\kappa_x$ — deformatsiya "
                  "qalinlik bo'yicha chiziqli, koeffitsienti egrilik. "
                  "O'rta sirtda ($z = 0$) deformatsiya nol.", "konseptual"),
                q("Gauss egriligi nima uchun 'ichki' xossa deb ataladi?",
                  "Theorema Egregium ga ko'ra uni sirt ichidagi "
                  "masofalarni o'lchab aniqlash mumkin — sirtdan "
                  "tashqariga chiqmasdan. Shuning uchun u cho'zilmasdan "
                  "bajarilgan egishda o'zgarmaydi.", "konseptual"),
                q("$\\kappa_x = 0{,}01$, $\\kappa_y = 0{,}004$, "
                  "$\\kappa_{xy} = 0{,}003$ 1/m. $K$ ni toping.",
                  "$K = 0{,}01 \\cdot 0{,}004 - 0{,}003^2 = "
                  "4\\times10^{-5} - 9\\times10^{-6} = 3{,}1\\times10^{-5}$ "
                  "1/m² > 0 — sinklastik.", "hisob"),
                q("Nima uchun silindrik qobiqni tekis listdan egib "
                  "yasash mumkin, sferikni esa yo'q?",
                  "Silindrning $K = 0$, tekis listning ham $K = 0$ — "
                  "cho'zilmasdan o'tish mumkin. Sferaning $K = 1/R^2 > 0$, "
                  "demak material cho'zilishi shart.", "talqin"),
                q("Kodda `np.linalg.eigh` nima uchun `eig` emas?",
                  "Egrilik tenzori simmetrik, `eigh` simmetrik matritsalar "
                  "uchun ixtisoslashgan: haqiqiy xususiy qiymatlarni "
                  "tartiblangan holda va ortogonal xususiy vektorlarni "
                  "kafolatlaydi.", "kod"),
                q("Kvadrat plastinaning burchaklarida nima uchun "
                  "ko'tarilish (uplift) yuz beradi?",
                  "U yerda Gauss egriligi manfiy (antiklastik, egar "
                  "shakli): sirt bir yo'nalishda pastga, ikkinchisida "
                  "yuqoriga egiladi va burchak ko'tarilishga intiladi.",
                  "talqin"),
            ],
            bridge=(
                "Deformatsiya maydoni to'liq aniqlandi. Endi Guk qonuni "
                "orqali kuchlanishga o'tamiz va ularni qalinlik bo'yicha "
                "integrallab, plastinaning ichki kuch omillarini — "
                "egish va buralish momentlarini — kiritamiz."
            ),
            research=(
                "Gaussning Theorema Egregium teoremasini o'rganing va "
                "uning ishlab chiqarishdagi oqibatlarini tahlil qiling: "
                "kema korpusi va samolyot fyuzelyaji panellari qanday "
                "qilib qo'sh egrilikli (double-curved) shaklga "
                "keltiriladi? Sonli tajriba o'tkazing: tekis to'rni "
                "sferaga proeksiyalang va hosil bo'ladigan minimal "
                "cho'zilish maydonini hisoblang. Bu natija xaritashunoslikdagi "
                "Tissot indikatrisasi bilan qanday bog'liq?"
            ),
        ),
    ),

    # ------------------------------------------------------------------ pq-03
    Topic(
        id="pq-03",
        subject_id=S, module_id=M, order=3,
        title="Ichki kuch omillari: egish va buralish momentlari, silindrik bikrlik",
        description=(
            "Kuchlanishlarni qalinlik bo'yicha integrallash, birlik "
            "uzunlikka to'g'ri keladigan momentlar, silindrik bikrlik $D$ "
            "va uning balka bikrligi bilan taqqoslanishi."
        ),
        learning_objective=(
            "Egrilikdan momentlarga o'tuvchi konstitutiv munosabatlarni "
            "keltirib chiqarish, silindrik bikrlikning fizik ma'nosini "
            "tushuntirish va momentlardan kuchlanishni hisoblash."
        ),
        prerequisites=["pq-02", "tmm-14"],
        mathematical_core=(
            "Qalinlik bo'yicha integrallash $\\int_{-h/2}^{h/2}\\sigma z\\,dz$, "
            "$D = Eh^3/[12(1-\\nu^2)]$, moment-egrilik matritsasi, "
            "momentlar tenzori va uning invariantlari."
        ),
        engineering_application=(
            "Temir-beton plita armaturasini hisoblash, metall panel "
            "qalinligini tanlash, kompozit qatlam paketini loyihalash, "
            "FEM plastina elementlarining asosi."
        ),
        computational_component=(
            "Moment-egrilik matritsasini qurish, momentlardan kuchlanish "
            "epyurasini hisoblash, bosh momentlarni topish."
        ),
        visualization_component=(
            "Qalinlik bo'yicha kuchlanish epyurasi, moment tenzorining "
            "Mor doirasi, $D(h)$ kubik bog'liqligi grafigi."
        ),
        research_extension=(
            "Qatlamli kompozit plastina uchun ABD matritsasini o'rganing: "
            "membrana, egilish va ularning bog'lanish hadlari qanday "
            "hosil bo'ladi?"
        ),
        difficulty="asosiy",
        previous_link=(
            "pq-02 da deformatsiyalar egriliklar orqali ifodalandi. "
            "tmm-14 dagi izotrop Guk qonuni (tekis kuchlanish holati) "
            "bilan birlashtirib, kuchlanishlarni va ularning "
            "integral xarakteristikalarini olamiz."
        ),
        next_topic="pq-04",
        estimated_minutes=90,
        tags=["moment", "bikrlik", "plastina", "kuchlanish"],
        lesson=_lesson(
            problem=(
                "Temir-beton plita loyihalanmoqda. Armatura sterjenlarini "
                "hisoblash uchun plitaning har bir nuqtasida, har bir "
                "yo'nalishda qancha egish momenti borligini bilish kerak. "
                "Balkada moment bitta son edi ($M$, N·m); plastinada esa "
                "u **yo'nalishga bog'liq**: $x$ bo'ylab bir xil, $y$ "
                "bo'ylab boshqacha, diagonalda esa uchinchi xil. Bundan "
                "tashqari buralish momenti ham bor. Bu obyektni qanday "
                "tavsiflaymiz va undan kuchlanishni qanday olamiz?"
            ),
            concepts=[
                c("Egish momenti $M_x$ (bending moment)",
                  "Birlik uzunlikka to'g'ri keladigan moment: "
                  "$M_x = \\int_{-h/2}^{h/2}\\sigma_x z\\,dz$. Birligi "
                  "N·m/m = N — bu balkadagi N·m dan farq qiladi."),
                c("Buralish momenti $M_{xy}$ (twisting moment)",
                  "$M_{xy} = \\int_{-h/2}^{h/2}\\tau_{xy}z\\,dz$ — "
                  "plastinaning buralishga qarshiligini tavsiflaydi; "
                  "balkada analogi yo'q."),
                c("Silindrik bikrlik $D$ (flexural rigidity)",
                  "$D = \\frac{Eh^3}{12(1-\\nu^2)}$ — plastinaning egilishga "
                  "qarshiligi. Birligi N·m. Balkadagi $EI$ ning analogi."),
                c("Momentlar tenzori",
                  "$M_{\\alpha\\beta}$ — simmetrik $2\\times2$ tenzor; "
                  "egrilik tenzori kabi bosh qiymatlar, invariantlar va "
                  "Mor doirasiga ega."),
                c("Kesuvchi kuchlar $Q_x, Q_y$",
                  "$Q_x = \\int\\tau_{xz}dz$ — birlik uzunlikka kesuvchi "
                  "kuch (N/m). Kirxhoff nazariyasida ular momentlardan "
                  "muvozanat orqali topiladi, Guk qonunidan emas."),
                c("Bikrlikdagi $(1-\\nu^2)$ ko'paytuvchi",
                  "Plastina balkadan farqli o'laroq yon tomonga erkin "
                  "kengaya olmaydi — qo'shni material ushlab turadi. "
                  "Shuning uchun u $1/(1-\\nu^2)$ marta bikrroq."),
            ],
            derivation=[
                d("1. Egriliklardan kuchlanishga",
                  r"\sigma_x = \frac{E}{1-\nu^2}(\varepsilon_x + \nu\varepsilon_y) "
                  r"= \frac{Ez}{1-\nu^2}(\kappa_x + \nu\kappa_y)",
                  "pq-02 dagi $\\varepsilon_x = z\\kappa_x$ ni tekis "
                  "kuchlanish Guk qonuniga qo'yamiz. Kuchlanish ham "
                  "qalinlik bo'yicha chiziqli."),
                d("2. Siljish kuchlanishi",
                  r"\tau_{xy} = G\gamma_{xy} = \frac{E}{2(1+\nu)}\cdot "
                  r"2z\kappa_{xy} = \frac{Ez}{1+\nu}\kappa_{xy}",
                  "$G = E/[2(1+\\nu)]$ (tmm-14). Siljish ham chiziqli, "
                  "lekin koeffitsienti boshqacha."),
                d("3. Momentni ta'riflash",
                  r"M_x \equiv \int_{-h/2}^{h/2}\sigma_x\,z\,dz",
                  "Kuchlanishning $z$ ga ko'paytirilgan integrali — "
                  "bu aynan momentning ta'rifi. Natija **birlik "
                  "uzunlikka** to'g'ri keladi, chunki kenglik bo'yicha "
                  "integrallamadik."),
                d("4. Integrallash",
                  r"M_x = \frac{E(\kappa_x + \nu\kappa_y)}{1-\nu^2}"
                  r"\int_{-h/2}^{h/2}z^2\,dz = "
                  r"\frac{E(\kappa_x + \nu\kappa_y)}{1-\nu^2}\cdot\frac{h^3}{12}",
                  "$\\int_{-h/2}^{h/2}z^2dz = \\frac{z^3}{3}\\Big|_{-h/2}^{h/2} "
                  "= \\frac{h^3}{12}$ — bu birlik kenglikdagi to'rtburchak "
                  "kesimning inersiya momenti (mq-08)."),
                d("5. Silindrik bikrlikni kiritish",
                  r"D \equiv \frac{Eh^3}{12(1-\nu^2)} \;\Longrightarrow\; "
                  r"M_x = D(\kappa_x + \nu\kappa_y)",
                  "Ta'rif natijani ixchamlashtiradi. $D$ birligi N·m — "
                  "balkadagi $EI$ (N·m²) dan farq qiladi, chunki bu "
                  "birlik kenglikka."),
                d("6. To'liq konstitutiv munosabatlar",
                  r"\begin{Bmatrix}M_x\\M_y\\M_{xy}\end{Bmatrix} = "
                  r"D\begin{bmatrix}1 & \nu & 0\\ \nu & 1 & 0\\ "
                  r"0 & 0 & 1-\nu\end{bmatrix}"
                  r"\begin{Bmatrix}\kappa_x\\\kappa_y\\\kappa_{xy}\end{Bmatrix}",
                  "Matritsa simmetrik va musbat aniqlangan. Egish va "
                  "buralish bir-biridan ajralgan (izotrop materialda); "
                  "kompozitda esa bog'lanish paydo bo'ladi."),
                d("7. Momentdan kuchlanishga qaytish",
                  r"\sigma_x(z) = \frac{12 M_x}{h^3}z \;\Longrightarrow\; "
                  r"\sigma_x^{\max} = \pm\frac{6M_x}{h^2}",
                  "1- va 5-qadamlarni birlashtirib $\\kappa$ ni "
                  "yo'qotamiz. Bu balkadagi $\\sigma = M/W$ formulasining "
                  "analogi, bunda qarshilik momenti $W = h^2/6$ "
                  "(birlik kenglikka)."),
                d("8. Balka bilan taqqoslash",
                  r"\frac{D}{EI_{\text{birlik}}} = \frac{Eh^3/[12(1-\nu^2)]}"
                  r"{Eh^3/12} = \frac{1}{1-\nu^2} \approx 1{,}10\ "
                  r"(\nu = 0{,}3)",
                  "Plastina bir xil qalinlikdagi balkalar to'plamidan "
                  "10 % bikrroq. Sabab: yon tomonga kengayish "
                  "cheklangan (tekis deformatsiya effekti)."),
            ],
            meaning=(
                "$D = Eh^3/[12(1-\\nu^2)]$ formulasining har bir qismi "
                "aniq ma'noga ega. $E$ — material qattiqligi (chiziqli "
                "hissa). $h^3$ — geometriyaning hissasi va u **kubik**: "
                "qalinlikni ikki marta oshirish bikrlikni sakkiz marta "
                "oshiradi. Bu muhandislikdagi eng kuchli 'richag': "
                "material qo'shmasdan shaklni o'zgartirish bilan "
                "bikrlikni keskin oshirish mumkin — shuning uchun "
                "gofrlangan list, qovurg'ali plita va sendvich panel "
                "shunchalik samarali. $1/(1-\\nu^2)$ esa plastinani "
                "balkadan ajratib turuvchi yagona had: balka egilganda "
                "yon tomoni erkin torayadi (Puasson effekti), plastinada "
                "esa qo'shni material buni cheklaydi va qo'shimcha "
                "kuchlanish paydo bo'ladi. $\\nu = 0{,}3$ uchun bu "
                "10 % bikrlik qo'shimchasi; $\\nu = 0{,}5$ (rezina) "
                "uchun esa 33 %. Buralish momenti $M_{xy}$ ning "
                "koeffitsienti $D(1-\\nu)$ ekanligi ham ma'noli: "
                "buralishda ikkala yo'nalish qarama-qarshi ishlaydi, "
                "shuning uchun Puasson effekti bikrlikni **kamaytiradi**, "
                "oshirmaydi."
            ),
            equations=[
                eq(r"D = \frac{Eh^3}{12(1-\nu^2)}",
                   "Plastinaning silindrik bikrligi.", "Silindrik bikrlik"),
                eq(r"M_x = D(\kappa_x + \nu\kappa_y), \quad "
                   r"M_y = D(\kappa_y + \nu\kappa_x), \quad "
                   r"M_{xy} = D(1-\nu)\kappa_{xy}",
                   "Moment-egrilik konstitutiv munosabatlari.",
                   "Moment-egrilik"),
                eq(r"\sigma_x = \frac{12M_x}{h^3}z, \qquad "
                   r"\sigma_x^{\max} = \frac{6M_x}{h^2}",
                   "Momentdan kuchlanishga; maksimum yuza qatlamlarda.",
                   "Kuchlanish formulasi"),
                eq(r"M_1, M_2 = \frac{M_x+M_y}{2} \pm "
                   r"\sqrt{\Big(\frac{M_x-M_y}{2}\Big)^2 + M_{xy}^2}",
                   "Bosh momentlar — armatura yo'nalishini tanlashda ishlatiladi.",
                   "Bosh momentlar"),
            ],
            conditions=(
                "**Integrallash chegaralari** $-h/2$ dan $+h/2$ gacha — "
                "o'rta sirtdan simmetrik. Agar plastina qatlamli va "
                "nosimmetrik bo'lsa (masalan, bir tomondan qoplamali), "
                "**neytral sirt** o'rta sirtdan siljiydi va membrana-egilish "
                "bog'lanishi paydo bo'ladi (B matritsasi, pq-17).\n\n"
                "**Kesuvchi kuchlar muvozanatdan topiladi**, Guk "
                "qonunidan emas — bu Kirxhoff nazariyasining o'ziga xos "
                "jihati:\n"
                "$$Q_x = \\frac{\\partial M_x}{\\partial x} + "
                "\\frac{\\partial M_{xy}}{\\partial y}, \\qquad "
                "Q_y = \\frac{\\partial M_y}{\\partial y} + "
                "\\frac{\\partial M_{xy}}{\\partial x}.$$\n"
                "Bular pq-04 da elementning muvozanatidan keltirib chiqariladi.\n\n"
                "**Qo'llanish sharti:** chiziqli elastik, izotrop, "
                "bir jinsli material; qalinlik doimiy."
            ),
            worked=WorkedExample(
                statement=(
                    "Po'lat plastina: $h = 12$ mm, $E = 200$ GPa, "
                    "$\\nu = 0{,}3$. Berilgan nuqtada egriliklar "
                    "$\\kappa_x = 0{,}015$ 1/m, $\\kappa_y = 0{,}004$ 1/m, "
                    "$\\kappa_{xy} = 0{,}006$ 1/m. (a) Silindrik bikrlikni "
                    "toping. (b) Momentlarni hisoblang. (c) Bosh "
                    "momentlarni va ularning yo'nalishini aniqlang. "
                    "(d) Maksimal kuchlanishni toping va Mizes bo'yicha "
                    "tekshiring ($\\sigma_Y = 250$ MPa)."
                ),
                given=[
                    r"h = 0{,}012\ \text{m},\ E = 200\ \text{GPa},\ \nu = 0{,}3",
                    r"\kappa_x = 0{,}015,\ \kappa_y = 0{,}004,\ "
                    r"\kappa_{xy} = 0{,}006\ \text{m}^{-1}",
                ],
                steps=[
                    st(r"D = \frac{Eh^3}{12(1-\nu^2)} = "
                       r"\frac{200\times10^9 \cdot (0{,}012)^3}{12(1 - 0{,}09)} "
                       r"= \frac{200\times10^9 \cdot 1{,}728\times10^{-6}}{10{,}92}",
                       "$h^3 = 1{,}728\\times10^{-6}$ m³ — kubik bog'liqlik "
                       "shu yerda ishlaydi."),
                    st(r"D = \frac{3{,}456\times10^{5}}{10{,}92} "
                       r"= 3{,}165\times10^{4}\ \text{N·m} = 31{,}65\ \text{kN·m}",
                       "Silindrik bikrlik. Taqqoslash uchun: $\\nu = 0$ "
                       "bo'lganda $D = 28{,}8$ kN·m — 10 % kam."),
                    st(r"M_x = D(\kappa_x + \nu\kappa_y) = 31\,650(0{,}015 "
                       r"+ 0{,}3 \cdot 0{,}004) = 31\,650 \cdot 0{,}0162 "
                       r"= 512{,}7\ \text{N·m/m}",
                       "$\\kappa_y$ ning hissasi $\\nu$ orqali kiradi — "
                       "ko'ndalang yo'nalishdagi egilish ham $M_x$ ni oshiradi."),
                    st(r"M_y = 31\,650(0{,}004 + 0{,}3 \cdot 0{,}015) "
                       r"= 31\,650 \cdot 0{,}0085 = 269{,}0\ \text{N·m/m}",
                       "Simmetrik hisob."),
                    st(r"M_{xy} = D(1-\nu)\kappa_{xy} = 31\,650 \cdot 0{,}7 "
                       r"\cdot 0{,}006 = 132{,}9\ \text{N·m/m}",
                       "Buralish momentida koeffitsient $(1-\\nu)$, "
                       "ya'ni Puasson effekti bikrlikni kamaytiradi."),
                    st(r"M_{1,2} = \frac{512{,}7+269{,}0}{2} \pm "
                       r"\sqrt{\Big(\frac{512{,}7-269{,}0}{2}\Big)^2 + 132{,}9^2} "
                       r"= 390{,}9 \pm \sqrt{121{,}9^2 + 132{,}9^2}",
                       "Bosh momentlar — Mor doirasi formulasi."),
                    st(r"M_{1,2} = 390{,}9 \pm 180{,}3 \;\Rightarrow\; "
                       r"M_1 = 571{,}2,\ M_2 = 210{,}6\ \text{N·m/m}; \quad "
                       r"\tan2\theta_0 = \frac{2 \cdot 132{,}9}{243{,}7} "
                       r"\Rightarrow \theta_0 = 23{,}7°",
                       "Armatura asosiy sterjenlari $23{,}7°$ burchak ostida "
                       "joylashtirilsa eng samarali bo'ladi."),
                    st(r"\sigma_1^{\max} = \frac{6M_1}{h^2} = "
                       r"\frac{6 \cdot 571{,}2}{0{,}012^2} = "
                       r"\frac{3427}{1{,}44\times10^{-4}} = 23{,}8\ \text{MPa}",
                       "Maksimal normal kuchlanish yuza qatlamda. "
                       "$\\sigma_2 = 6 \\cdot 210{,}6/h^2 = 8{,}8$ MPa."),
                    st(r"\sigma_{\text{eq}} = \sqrt{23{,}8^2 - 23{,}8 \cdot 8{,}8 "
                       r"+ 8{,}8^2} = \sqrt{566 - 209 + 77} = 20{,}8\ \text{MPa}",
                       "Mizes (tmm-21) tekis kuchlanish holati uchun. "
                       "Zaxira $250/20{,}8 = 12{,}0$ — juda katta."),
                ],
                answer=(
                    "$D = 31{,}65$ kN·m; $M_x = 512{,}7$, $M_y = 269{,}0$, "
                    "$M_{xy} = 132{,}9$ N·m/m; bosh momentlar 571,2 va "
                    "210,6 N·m/m, yo'nalish $23{,}7°$; "
                    "$\\sigma_{\\max} = 23{,}8$ MPa, Mizes 20,8 MPa, "
                    "zaxira koeffitsienti 12,0."
                ),
                engineering_note=(
                    "Temir-beton plitalarda armatura odatda $x$ va $y$ "
                    "o'qlari bo'ylab qo'yiladi, bosh yo'nalishlar esa "
                    "qiya bo'lishi mumkin. Shuning uchun Vud–Armer "
                    "(Wood–Armer) formulalari ishlatiladi: ular buralish "
                    "momentini ekvivalent $x$ va $y$ momentlariga qayta "
                    "taqsimlaydi: $M_x^* = M_x + |M_{xy}|$, "
                    "$M_y^* = M_y + |M_{xy}|$. Bu yerda bu "
                    "645,6 va 401,9 N·m/m beradi — bosh momentdan katta, "
                    "chunki yo'nalish mos kelmasligi uchun 'jarima' to'lanadi."
                ),
            ),
            computation=Computation(
                caption=(
                    "Moment-egrilik matritsasini qurish, bosh momentlarni "
                    "topish, kuchlanish epyurasini hisoblash va Vud–Armer "
                    "armatura momentlarini baholash."
                ),
                code='''"""Plastina ichki kuch omillari: momentlar va silindrik bikrlik."""
import numpy as np
from labkit import PARAMS, note, series, table, value

E = float(PARAMS.get("E", 200.0))*1e9     # Pa
nu = float(PARAMS.get("nu", 0.3))
h = float(PARAMS.get("h", 12.0))/1000.0   # m
kx = float(PARAMS.get("kx", 0.015))       # 1/m
ky = float(PARAMS.get("ky", 0.004))
kxy = float(PARAMS.get("kxy", 0.006))
sY = float(PARAMS.get("sY", 250.0))*1e6   # Pa

D = E*h**3/(12*(1 - nu**2))
D_beam = E*h**3/12                         # birlik kenglikdagi balka EI
value("Silindrik bikrlik D", D/1000, "kN*m")
value("Balka bikrligi EI (birlik kenglik)", D_beam/1000, "kN*m")
value("D / EI = 1/(1-nu^2)", D/D_beam, "—")
note(f"Plastina bir xil qalinlikdagi balkadan {100*(D/D_beam - 1):.1f} % "
     f"bikrroq: yon tomonga kengayish cheklangan (Puasson effekti).")

# --- Moment-egrilik matritsasi ---
Dm = D*np.array([[1.0, nu, 0.0],
                 [nu, 1.0, 0.0],
                 [0.0, 0.0, 1 - nu]])
kappa = np.array([kx, ky, kxy])
Mx, My, Mxy = Dm @ kappa
value("M_x", Mx, "N*m/m")
value("M_y", My, "N*m/m")
value("M_xy", Mxy, "N*m/m")

eigD = np.linalg.eigvalsh(Dm)
note(f"Bikrlik matritsasi xususiy qiymatlari: {np.round(eigD/1000, 2)} kN*m — "
     f"{'musbat aniqlangan (fizik jihatdan to''g''ri)' if np.all(eigD > 0) else 'XATO'}.")

# --- Bosh momentlar ---
T = np.array([[Mx, Mxy], [Mxy, My]])
vals, vecs = np.linalg.eigh(T)
M2, M1 = float(vals[0]), float(vals[1])
theta0 = np.degrees(np.arctan2(vecs[1, 1], vecs[0, 1]))
value("Bosh moment M_1", M1, "N*m/m")
value("Bosh moment M_2", M2, "N*m/m")
value("Bosh yo'nalish burchagi", theta0, "deg")
value("Maksimal buralish momenti", 0.5*abs(M1 - M2), "N*m/m")

# Formula bilan tekshirish
M1f = 0.5*(Mx + My) + np.sqrt((0.5*(Mx - My))**2 + Mxy**2)
note(f"Xususiy qiymat {M1:.2f} va formula {M1f:.2f} N*m/m — mos keladi.")

# --- Kuchlanishlar ---
z = np.linspace(-h/2, h/2, 121)
sx = 12*Mx/h**3*z
sy = 12*My/h**3*z
txy = 12*Mxy/h**3*z
series("sigma_x(z)", (sx/1e6).tolist(), (z*1000).tolist(),
       xlabel="sigma_x, MPa", ylabel="z, mm")
series("sigma_y(z)", (sy/1e6).tolist(), (z*1000).tolist(),
       xlabel="sigma_y, MPa", ylabel="z, mm")
series("tau_xy(z)", (txy/1e6).tolist(), (z*1000).tolist(),
       xlabel="tau_xy, MPa", ylabel="z, mm")

sx_max = 6*Mx/h**2
sy_max = 6*My/h**2
txy_max = 6*Mxy/h**2
value("sigma_x max (yuza)", sx_max/1e6, "MPa")
value("sigma_y max (yuza)", sy_max/1e6, "MPa")
value("tau_xy max (yuza)", txy_max/1e6, "MPa")

# Mizes (tekis kuchlanish holati)
s1 = 6*M1/h**2
s2 = 6*M2/h**2
mises = np.sqrt(s1**2 - s1*s2 + s2**2)
value("Bosh kuchlanish sigma_1", s1/1e6, "MPa")
value("Bosh kuchlanish sigma_2", s2/1e6, "MPa")
value("Mizes ekvivalent kuchlanish", mises/1e6, "MPa")
value("Zaxira koeffitsienti", sY/mises, "—")
if mises < sY:
    note(f"Elastik holat: Mizes {mises/1e6:.2f} MPa < sigma_Y "
         f"{sY/1e6:.0f} MPa, zaxira {sY/mises:.2f}.")
else:
    note(f"OQISH: Mizes {mises/1e6:.2f} MPa >= sigma_Y {sY/1e6:.0f} MPa!")

# --- Vud-Armer armatura momentlari ---
Mx_star = Mx + abs(Mxy)
My_star = My + abs(Mxy)
value("Vud-Armer M_x*", Mx_star, "N*m/m")
value("Vud-Armer M_y*", My_star, "N*m/m")
value("M_x* / M_1", Mx_star/M1 if M1 != 0 else 0.0, "—")
note("Vud-Armer momentlari bosh momentdan katta: armatura bosh "
     "yo'nalishga mos kelmagani uchun 'jarima' to'lanadi.")

# --- D(h) kubik bog'liqligi ---
h_range = np.linspace(0.002, 0.05, 200)
D_range = E*h_range**3/(12*(1 - nu**2))
series("D(h) kubik bog'liqlik", (h_range*1000).tolist(), (D_range/1000).tolist(),
       xlabel="Qalinlik h, mm", ylabel="D, kN*m")
note(f"Qalinlikni 2 marta oshirish D ni 8 marta oshiradi: "
     f"h={h*1000:.0f} mm da D={D/1000:.1f} kN*m, "
     f"h={2*h*1000:.0f} mm da D={E*(2*h)**3/(12*(1-nu**2))/1000:.1f} kN*m.")

# --- Momentni burchak bo'yicha aylantirish ---
th = np.linspace(0, 180, 181)
thr = np.radians(th)
Mn = Mx*np.cos(thr)**2 + My*np.sin(thr)**2 + 2*Mxy*np.sin(thr)*np.cos(thr)
Mt = -(Mx - My)*np.sin(thr)*np.cos(thr) + Mxy*(np.cos(thr)**2 - np.sin(thr)**2)
series("M_n(theta)", th.tolist(), Mn.tolist(),
       xlabel="Burchak theta, deg", ylabel="M_n, N*m/m")
series("M_nt(theta)", th.tolist(), Mt.tolist(),
       xlabel="Burchak theta, deg", ylabel="M_nt, N*m/m")

table("Plastina va balka taqqoslashi",
      ["Kattalik", "Balka", "Plastina", "Farq"],
      [["Bikrlik", "EI = Eh^3/12", "D = Eh^3/(12(1-nu^2))",
        f"{100*(1/(1-nu**2)-1):.1f} % ortiq"],
       ["Moment birligi", "N*m", "N*m/m", "birlik uzunlikka"],
       ["Kuchlanish", "M/W, W = bh^2/6", "6M/h^2", "b = 1 m"],
       ["Buralish", "yo'q (alohida)", "M_xy = D(1-nu)*kappa_xy",
        "plastinaga xos"],
       ["Noma'lumlar", "w(x)", "w(x, y)", "PDE va ODE"]])

table("Qalinlikning bikrlikka ta'siri",
      ["h, mm", "D, kN*m", "D nisbati", "w nisbati (q = const)"],
      [[round(hh*1000, 0), round(E*hh**3/(12*(1-nu**2))/1000, 2),
        round((hh/h)**3, 3), round((h/hh)**3, 4)]
       for hh in [0.5*h, 0.75*h, h, 1.5*h, 2*h]])
''',
                parameters=[
                    p("E", "Yung moduli E", 1.0, 400.0, 200.0, 1.0, "GPa"),
                    p("nu", "Puasson koeffitsienti ν", 0.0, 0.45, 0.3, 0.01),
                    p("h", "Qalinlik h", 1.0, 200.0, 12.0, 0.5, "mm"),
                    p("kx", "Egrilik κₓ", -0.1, 0.1, 0.015, 0.001, "1/m"),
                    p("ky", "Egrilik κᵧ", -0.1, 0.1, 0.004, 0.001, "1/m"),
                    p("kxy", "Buralish κₓᵧ", -0.1, 0.1, 0.006, 0.001, "1/m"),
                    p("sY", "Oqish chegarasi σ_Y", 20.0, 1000.0, 250.0, 5.0, "MPa"),
                ],
                expected_output=(
                    "D = 31,65 kN·m, D/EI = 1,099; M_x = 512,7, "
                    "M_y = 269,0, M_xy = 132,9 N·m/m; M₁ = 571,2, "
                    "M₂ = 210,6 N·m/m, θ₀ = 23,7°; σ_max = 23,8 MPa, "
                    "Mizes 20,8 MPa, zaxira 12,0."
                ),
            ),
            visual=vis(
                kind="Kuchlanish epyurasi va moment tenzori",
                tool="React/SVG",
                description=(
                    "Qalinlik bo'yicha chiziqli kuchlanish epyuralari, "
                    "moment tenzorining Mor doirasi va $D(h)$ kubik egri chizig'i."
                ),
                how_to_draw=(
                    "React/SVG: qalinlik epyurasi paneli — vertikal "
                    "o'qda $z$ ($-h/2$ dan $+h/2$ gacha), gorizontalda "
                    "kuchlanish. $\\sigma_x$, $\\sigma_y$, $\\tau_{xy}$ "
                    "uchta chiziqli epyura, har biri to'ldirilgan "
                    "uchburchak juftligi sifatida (yuqorida bir rang, "
                    "pastda qarama-qarshi rang — cho'zilish/siqilish "
                    "duallikini ko'rsatadi). O'rta sirt punktir chiziq "
                    "bilan, 'neytral qatlam' yorlig'i bilan belgilanadi. "
                    "Mor doirasi paneli: markazi $(M_x+M_y)/2$ da, "
                    "radiusi $\\sqrt{((M_x-M_y)/2)^2 + M_{xy}^2}$; "
                    "$(M_x, M_{xy})$ va $(M_y, -M_{xy})$ nuqtalari "
                    "diametr bilan tutashtiriladi, bosh momentlar "
                    "o'qdagi kesishish nuqtalari sifatida belgilanadi. "
                    "$D(h)$ paneli log–log o'qlarda chiziladi — u yerda "
                    "kubik bog'liqlik qiyaligi 3 bo'lgan to'g'ri chiziq "
                    "bo'lib ko'rinadi. Slayder bilan $h$ o'zgartirilganda "
                    "uchala panel sinxron yangilanadi."
                ),
            ),
            interp=(
                "Jadvaldagi eng amaliy qator — qalinlikning og'ishga "
                "ta'siri: $h$ ni yarmiga tushirish og'ishni **sakkiz "
                "marta** oshiradi. Bu shuni anglatadiki, plastina "
                "loyihasida qalinlik eng kuchli boshqaruv parametri — "
                "materialni o'zgartirishdan ham kuchliroq (po'latdan "
                "alyuminiyga o'tish $E$ ni atigi 3 marta kamaytiradi). "
                "Lekin qalinlik og'irlikni chiziqli oshiradi, shuning "
                "uchun aviatsiyada boshqa yo'l tanlanadi: qalinlikni "
                "emas, **shaklni** o'zgartirish — qovurg'a, gofr, "
                "sendvich. Ularning hammasi bir xil g'oyaga asoslangan: "
                "materialni o'rta sirtdan uzoqlashtirish, chunki hissasi "
                "$z^2$ ga mutanosib. $D/EI = 1{,}099$ natijasi esa "
                "plastina nazariyasining balka nazariyasidan "
                "farqini bitta songa jamlaydi: 10 % qo'shimcha bikrlik "
                "sof Puasson effekti hisobiga. Vud–Armer momentlari "
                "($M_x^* = 645{,}6$ N·m/m) bosh momentdan ($571{,}2$) "
                "13 % katta bo'lishi — armaturani bosh yo'nalishga "
                "moslashtirish imkoni bo'lmagani uchun to'lanadigan "
                "haqiqiy material narxi."
            ),
            mistakes=[
                "Plastina momentini N·m da o'lchash. U **birlik "
                "uzunlikka** to'g'ri keladi: N·m/m = N. Hisobda uni "
                "kenglikka ko'paytirishni unutmaslik kerak.",
                "$D$ ni $EI$ bilan tenglashtirish. Ular birliklari "
                "ham, qiymatlari ham har xil: $D = EI/(1-\\nu^2)$ "
                "birlik kenglikka.",
                "Buralish momentida $D(1-\\nu)$ o'rniga $D$ yozish. "
                "Bu 30 % xato beradi va kuchlanishni kam ko'rsatadi.",
                "Momentdan kuchlanishga o'tishda $W = h^2/6$ o'rniga "
                "$h^3/12$ (inersiya momenti) ishlatish. Qarshilik "
                "momenti $W = I/(h/2) = h^2/6$.",
            ],
            quiz=[
                q("Nima uchun plastina bir xil qalinlikdagi balkadan bikrroq?",
                  "Balka egilganda yon tomoni erkin torayadi, plastinada "
                  "esa qo'shni material buni cheklaydi. Natijada "
                  "$D = EI/(1-\\nu^2)$, ya'ni $\\nu = 0{,}3$ da 10 % "
                  "qo'shimcha bikrlik.", "konseptual"),
                q("Plastina momentining birligi nima va nega?",
                  "N·m/m (= N), chunki u **birlik uzunlikka** to'g'ri "
                  "keladi: kuchlanish faqat qalinlik bo'yicha "
                  "integrallangan, kenglik bo'yicha emas.", "konseptual"),
                q("$E = 70$ GPa, $\\nu = 0{,}33$, $h = 5$ mm. $D$ ni toping.",
                  "$D = 70\\times10^9 \\cdot 1{,}25\\times10^{-7}/"
                  "[12(1-0{,}1089)] = 8750/10{,}693 = 818$ N·m.", "hisob"),
                q("Nima uchun buralish momentida koeffitsient "
                  "$(1-\\nu)$, egishda esa $(1+\\nu \\cdot)$?",
                  "Buralishda ikki yo'nalish qarama-qarshi ishlaydi, "
                  "shuning uchun Puasson effekti bikrlikni kamaytiradi. "
                  "Egishda esa ko'ndalang egilish qo'shimcha hissa qo'shadi.",
                  "talqin"),
                q("Kodda bikrlik matritsasining xususiy qiymatlari nima "
                  "uchun tekshiriladi?",
                  "Musbat aniqlanganlik fizik talab: har qanday nolga "
                  "teng bo'lmagan egrilikda deformatsiya energiyasi "
                  "musbat bo'lishi kerak. Manfiy qiymat model xatosini "
                  "bildiradi.", "kod"),
                q("Qalinlikni 1,5 marta oshirsak, og'ish qanday o'zgaradi?",
                  "$w \\propto 1/D \\propto 1/h^3$, demak "
                  "$1/1{,}5^3 = 0{,}296$ — og'ish 3,4 marta kamayadi.",
                  "hisob"),
            ],
            bridge=(
                "Konstitutiv munosabatlar tayyor: egrilikdan momentga, "
                "momentdan kuchlanishga. Endi oxirgi bo'g'in kerak — "
                "muvozanat tenglamasi. Uni momentlar bilan birlashtirib, "
                "plastina nazariyasining markaziy tenglamasini olamiz."
            ),
            research=(
                "Qatlamli kompozit plastina uchun klassik qatlamlash "
                "nazariyasini (Classical Laminate Theory) o'rganing: "
                "$\\{N, M\\}^T = [[A, B], [B, D]]\\{\\varepsilon^0, "
                "\\kappa\\}^T$. $A$ — membrana, $D$ — egilish, $B$ — "
                "bog'lanish matritsasi. Simmetrik paketlarda $B = 0$ "
                "bo'lishini isbotlang va nosimmetrik paketda "
                "cho'zilishning egilishga olib kelishini sonli "
                "ko'rsating. $[0/90]$ va $[0/90]_s$ paketlarini "
                "taqqoslang — nima uchun ishlab chiqarishda "
                "simmetriya shunchalik muhim?"
            ),
            manim_ref=manim(
                scene="PlateMomentsScene",
                module="animatsiya/scenes/pq_plate_basics.py",
                title="Plastina elementidagi ichki kuch omillari",
                summary=(
                    "$dx\\,dy$ elementning yuzlarida egish momentlari, "
                    "buralish momentlari va kesuvchi kuchlar vektorlar "
                    "bilan ko'rsatiladi; kuchlanish epyuralari "
                    "integrallanib momentga aylanishi animatsiya qilinadi."
                ),
            ),
        ),
    ),

    # ------------------------------------------------------------------ pq-04
    Topic(
        id="pq-04",
        subject_id=S, module_id=M, order=4,
        title="Plastina egilishining asosiy tenglamasi: Sofi Jermen–Lagranj tenglamasi",
        description=(
            "Plastina elementining muvozanat tenglamalari, kesuvchi "
            "kuchlarning momentlar orqali ifodalanishi va bigarmonik "
            "tenglama $D\\nabla^4 w = q$ ning to'liq keltirib chiqarilishi."
        ),
        learning_objective=(
            "Element muvozanatidan boshlab plastinaning bigarmonik "
            "tenglamasini chiqarish, uning tuzilishini tahlil qilish va "
            "sodda holatlarda aniq yechim topish."
        ),
        prerequisites=["pq-03", "tmm-17"],
        mathematical_core=(
            "Element muvozanati, bigarmonik operator "
            "$\\nabla^4 = \\partial^4/\\partial x^4 + 2\\partial^4/"
            "\\partial x^2\\partial y^2 + \\partial^4/\\partial y^4$, "
            "to'rtinchi tartibli elliptik PDE, xususiy va umumiy yechim."
        ),
        engineering_application=(
            "Barcha plastina hisoblarining asosi: perekrytiya, ko'prik "
            "plitasi, panel, qopqoq, membrana; FEM plastina elementlari "
            "aynan shu tenglamani diskretlashtiradi."
        ),
        computational_component=(
            "Tenglamani sonli tekshirish: berilgan yechimni tenglamaga "
            "qo'yib qoldiqni hisoblash; silindrik egilish holatining "
            "aniq yechimini qurish."
        ),
        visualization_component=(
            "Element muvozanati diagrammasi, og'ish sirtining 3D "
            "tasviri, bigarmonik operatorning ayirmali shablonli tasviri."
        ),
        research_extension=(
            "Bigarmonik tenglamaning fundamental yechimini (Grin "
            "funksiyasi) o'rganing: konsentrlangan kuch ostida plastina "
            "og'ishi qanday ifodalanadi?"
        ),
        difficulty="murakkab",
        previous_link=(
            "pq-03 da momentlar egriliklar orqali ifodalandi. "
            "tmm-17 dagi bigarmonik tenglama (Eyri funksiyasi) bilan "
            "matematik jihatdan bir xil operator paydo bo'ladi — bu "
            "tasodif emas, ikkalasi ham ikki o'lchovli elastiklik "
            "masalalaridan kelib chiqadi."
        ),
        next_topic="pq-05",
        estimated_minutes=95,
        tags=["bigarmonik", "muvozanat", "PDE", "plastina"],
        lesson=_lesson(
            problem=(
                "Endi barcha bo'g'inlar tayyor: kinematika (pq-02), "
                "konstitutiv munosabatlar (pq-03). Yetishmayotgan "
                "narsa — **muvozanat**. Plastinaning kichik "
                "$dx \\times dy$ elementini ajratib olamiz va unga "
                "ta'sir qiluvchi barcha kuch va momentlarni "
                "muvozanatlashtiramiz. Natija nima bo'ladi? Balkada "
                "$EIw'''' = q$ edi. Plastinada esa ikki o'lchov, "
                "buralish momenti va ikkita kesuvchi kuch bor. Ular "
                "birlashib qanday tenglama beradi?"
            ),
            concepts=[
                c("Element muvozanati",
                  "$dx\\,dy$ o'lchamli elementga ta'sir qiluvchi barcha "
                  "kuch va momentlarning yig'indisi nolga teng bo'lishi "
                  "sharti — uchta tenglama beradi."),
                c("Bigarmonik operator $\\nabla^4$",
                  "$\\nabla^4 = \\nabla^2(\\nabla^2) = \\partial_x^4 + "
                  "2\\partial_x^2\\partial_y^2 + \\partial_y^4$ — "
                  "Laplasianning kvadrati; to'rtinchi tartibli elliptik operator."),
                c("Sofi Jermen–Lagranj tenglamasi",
                  "$D\\nabla^4 w = q(x,y)$ — plastina egilishining asosiy "
                  "tenglamasi. Sofi Jermen 1816-yilda topgan, Lagranj "
                  "koeffitsientni to'g'rilagan."),
                c("Elliptik tenglama",
                  "Yechim butun sohada bir vaqtda aniqlanadi; bir "
                  "nuqtadagi o'zgarish darhol hamma joyga ta'sir qiladi. "
                  "Chegaraviy shartlar butun konturda berilishi shart."),
                c("Silindrik egilish",
                  "Yechim faqat bitta koordinataga bog'liq bo'lgan hol: "
                  "$w = w(x)$. Bunda tenglama $Dw'''' = q$ ga aylanadi — "
                  "aynan balka tenglamasi, faqat $EI$ o'rnida $D$."),
                c("Xususiy va umumiy yechim",
                  "$w = w_p + w_h$: xususiy yechim yuklamani, bir jinsli "
                  "yechim ($\\nabla^4 w_h = 0$) chegaraviy shartlarni "
                  "qanoatlantiradi."),
            ],
            derivation=[
                d("1. Element va unga ta'sir etuvchi omillar",
                  r"\text{Element } dx\,dy:\ M_x, M_y, M_{xy}, M_{yx}, "
                  r"Q_x, Q_y \ \text{va yuklama } q\,dx\,dy",
                  "Har bir yuzda moment va kesuvchi kuch bor; qarama-qarshi "
                  "yuzlarda ular hosila bilan o'sgan: "
                  "$M_x + \\frac{\\partial M_x}{\\partial x}dx$ va hokazo."),
                d("2. Vertikal kuchlar muvozanati",
                  r"\frac{\partial Q_x}{\partial x} + \frac{\partial Q_y}"
                  r"{\partial y} + q = 0",
                  "$z$ o'qi bo'ylab: $\\frac{\\partial Q_x}{\\partial x}"
                  "dx\\,dy + \\frac{\\partial Q_y}{\\partial y}dy\\,dx "
                  "+ q\\,dx\\,dy = 0$, keyin $dx\\,dy$ ga qisqartiriladi."),
                d("3. $y$ o'qi atrofidagi momentlar muvozanati",
                  r"\frac{\partial M_x}{\partial x} + \frac{\partial M_{yx}}"
                  r"{\partial y} - Q_x = 0 \;\Longrightarrow\; "
                  r"Q_x = \frac{\partial M_x}{\partial x} + "
                  r"\frac{\partial M_{xy}}{\partial y}",
                  "$M_{yx} = M_{xy}$ (siljish kuchlanishlarining juftlik "
                  "qonuni, tmm-11). Kesuvchi kuch **momentlardan** "
                  "topiladi — Guk qonunidan emas."),
                d("4. $x$ o'qi atrofidagi momentlar muvozanati",
                  r"Q_y = \frac{\partial M_y}{\partial y} + "
                  r"\frac{\partial M_{xy}}{\partial x}",
                  "Simmetrik natija. Endi uchta noma'lum ($Q_x, Q_y$) "
                  "momentlar orqali ifodalangan."),
                d("5. Kesuvchi kuchlarni yo'qotish",
                  r"\frac{\partial^2 M_x}{\partial x^2} + "
                  r"2\frac{\partial^2 M_{xy}}{\partial x\partial y} + "
                  r"\frac{\partial^2 M_y}{\partial y^2} + q = 0",
                  "3- va 4-qadamlarni 2-tenglamaga qo'yamiz. Aralash "
                  "hosila ikki marta paydo bo'ladi — shuning uchun "
                  "koeffitsient 2. Bu momentlar orqali yozilgan muvozanat tenglamasi."),
                d("6. Momentlarni egriliklar orqali almashtirish",
                  r"M_x = -D\Big(\frac{\partial^2 w}{\partial x^2} + "
                  r"\nu\frac{\partial^2 w}{\partial y^2}\Big), \quad "
                  r"M_{xy} = -D(1-\nu)\frac{\partial^2 w}{\partial x\partial y}",
                  "pq-03 dagi munosabatlar, $\\kappa = -\\partial^2 w/"
                  "\\partial x^2$ ta'rifi bilan. Endi minus ishoralar "
                  "oshkor ko'rinadi."),
                d("7. Bigarmonik tenglamani yig'ish",
                  r"-D\Big[\frac{\partial^4 w}{\partial x^4} + "
                  r"\nu\frac{\partial^4 w}{\partial x^2\partial y^2} + "
                  r"2(1-\nu)\frac{\partial^4 w}{\partial x^2\partial y^2} + "
                  r"\nu\frac{\partial^4 w}{\partial x^2\partial y^2} + "
                  r"\frac{\partial^4 w}{\partial y^4}\Big] + q = 0",
                  "6-qadamni 5-qadamga qo'yamiz. Aralash hosila "
                  "koeffitsienti: $\\nu + 2(1-\\nu) + \\nu = 2$ — "
                  "**Puasson koeffitsienti aynan qisqaradi!**"),
                d("8. Sofi Jermen–Lagranj tenglamasi",
                  r"D\Big(\frac{\partial^4 w}{\partial x^4} + "
                  r"2\frac{\partial^4 w}{\partial x^2\partial y^2} + "
                  r"\frac{\partial^4 w}{\partial y^4}\Big) = q "
                  r"\;\Longleftrightarrow\; D\nabla^4 w = q",
                  "Yakuniy shakl. $\\nu$ tenglamada qolmadi — u faqat "
                  "$D$ ichida va chegaraviy shartlarda qatnashadi. Bu "
                  "juda muhim: bir xil chegaraviy shartlarda og'ish "
                  "shakli $\\nu$ ga bog'liq emas."),
            ],
            meaning=(
                "$D\\nabla^4 w = q$ tenglamasining go'zalligi — uning "
                "soddaligida. To'rtta chuqur fizik g'oya (kinematika, "
                "Guk qonuni, muvozanat, gipotezalar) bitta ixcham "
                "ifodaga siqilgan. Chap tomon — plastinaning qarshiligi, "
                "o'ng tomon — tashqi ta'sir. Bigarmonik operatorning "
                "tuzilishi ham ma'noli: $\\partial_x^4$ — $x$ bo'ylab "
                "'balka' hissasi, $\\partial_y^4$ — $y$ bo'ylab, "
                "$2\\partial_x^2\\partial_y^2$ esa ikki yo'nalishning "
                "**o'zaro ta'siri** — aynan shu had plastinani "
                "balkalar to'plamidan ajratib turadi. Eng hayratlanarli "
                "natija — $\\nu$ ning tenglamadan yo'qolishi. Bu shuni "
                "anglatadiki, sharnirli tayanchli plastinaning og'ish "
                "**shakli** Puasson koeffitsientiga umuman bog'liq emas; "
                "$\\nu$ faqat og'ishning kattaligiga ($D$ orqali) va "
                "ba'zi chegaraviy shartlarga ta'sir qiladi. Shuning "
                "uchun po'lat va alyuminiy plastinalar bir xil shaklda "
                "egiladi, faqat turli kattalikda. Va nihoyat, tmm-17 "
                "dagi Eyri funksiyasi tenglamasi $\\nabla^4\\varphi = 0$ "
                "bilan o'xshashlik — ikkalasi ham ikki o'lchovli "
                "elastiklikning to'rtinchi tartibli formulirovkalari."
            ),
            equations=[
                eq(r"D\nabla^4 w = q(x, y)",
                   "Sofi Jermen–Lagranj tenglamasi — plastina egilishining "
                   "asosiy tenglamasi.", "Plastina tenglamasi"),
                eq(r"\frac{\partial^2 M_x}{\partial x^2} + "
                   r"2\frac{\partial^2 M_{xy}}{\partial x\partial y} + "
                   r"\frac{\partial^2 M_y}{\partial y^2} + q = 0",
                   "Muvozanat tenglamasi momentlar orqali.",
                   "Moment muvozanati"),
                eq(r"Q_x = \frac{\partial M_x}{\partial x} + "
                   r"\frac{\partial M_{xy}}{\partial y}",
                   "Kesuvchi kuch momentlar orqali (Guk qonunidan emas).",
                   "Kesuvchi kuch"),
                eq(r"D\frac{d^4 w}{dx^4} = q",
                   "Silindrik egilish — plastina tenglamasining bir "
                   "o'lchovli holati.", "Silindrik egilish"),
            ],
            conditions=(
                "To'rtinchi tartibli PDE bo'lgani uchun konturning har "
                "bir nuqtasida **ikkita** shart berilishi kerak (pq-05 da "
                "batafsil):\n"
                "- Sharnirli tayanch: $w = 0$, $M_n = 0$;\n"
                "- Qattiq mahkamlash: $w = 0$, $\\partial w/\\partial n = 0$;\n"
                "- Erkin chekka: $M_n = 0$, $V_n = 0$ (Kirxhoff kesuvchi kuchi).\n\n"
                "**Elliptik tenglama xossasi:** yechim butun sohada bir "
                "vaqtda aniqlanadi. Yuklama bitta nuqtada o'zgarsa, "
                "og'ish hamma joyda o'zgaradi (garchi uzoqda kam bo'lsa ham). "
                "Bu giperbolik (to'lqin) tenglamadan tubdan farq qiladi.\n\n"
                "**Yechim mavjudligi:** yuklama $q$ integrallanuvchi va "
                "soha chegarasi silliq bo'lsa, yechim mavjud va yagona. "
                "Burchaklarda (kirish burchagi) singulyarlik paydo bo'lishi mumkin."
            ),
            worked=WorkedExample(
                statement=(
                    "(a) Uzun to'rtburchak plastina ($b \\gg a$) ikki "
                    "uzun chekkasi bo'ylab sharnirli tayanган, bir tekis "
                    "yuklama $q$ ta'sir qiladi. Silindrik egilish "
                    "holatida og'ish funksiyasini toping. (b) "
                    "$a = 2$ m, $h = 20$ mm, $E = 200$ GPa, $\\nu = 0{,}3$, "
                    "$q = 10$ kPa uchun maksimal og'ish va momentni hisoblang. "
                    "(c) Natijani bir xil kesimli balka bilan taqqoslang."
                ),
                given=[
                    r"a = 2\ \text{m},\ h = 0{,}02\ \text{m}",
                    r"E = 200\ \text{GPa},\ \nu = 0{,}3,\ q = 10^4\ \text{Pa}",
                    r"b \gg a \;\Rightarrow\; w = w(x)",
                ],
                steps=[
                    st(r"w = w(x) \;\Rightarrow\; \nabla^4 w = "
                       r"\frac{d^4 w}{dx^4} \;\Rightarrow\; "
                       r"D\frac{d^4w}{dx^4} = q",
                       "$y$ bo'yicha hosilalar nolga teng — tenglama "
                       "oddiy differensial tenglamaga aylanadi."),
                    st(r"w(x) = \frac{q}{24D}x^4 + C_1x^3 + C_2x^2 + C_3x + C_4",
                       "To'rt marta integrallash. To'rtta doimiy — "
                       "to'rtta chegaraviy shart kerak (har chekkada ikkita)."),
                    st(r"w(0) = w(a) = 0, \quad w''(0) = w''(a) = 0",
                       "Sharnirli tayanch: og'ish nol va moment nol "
                       "($M_x = -D w''$, silindrik egilishda)."),
                    st(r"w(x) = \frac{q}{24D}\big(x^4 - 2ax^3 + a^3x\big) "
                       r"= \frac{qa^4}{24D}\Big(\xi^4 - 2\xi^3 + \xi\Big), "
                       r"\ \xi = x/a",
                       "Shartlardan doimiylar topiladi. Bu aynan sharnirli "
                       "balkaning egilish chizig'i."),
                    st(r"w_{\max} = w(a/2) = \frac{5qa^4}{384D}",
                       "$\\xi = 0{,}5$ da: $0{,}0625 - 0{,}25 + 0{,}5 = "
                       "0{,}3125 = 5/16$; $\\frac{5/16}{24} = \\frac{5}{384}$."),
                    st(r"D = \frac{200\times10^9 \cdot 8\times10^{-6}}"
                       r"{12 \cdot 0{,}91} = \frac{1{,}6\times10^{6}}{10{,}92} "
                       r"= 1{,}465\times10^{5}\ \text{N·m}",
                       "$h^3 = 8\\times10^{-6}$ m³."),
                    st(r"w_{\max} = \frac{5 \cdot 10^4 \cdot 16}"
                       r"{384 \cdot 1{,}465\times10^{5}} = "
                       r"\frac{8\times10^{5}}{5{,}626\times10^{7}} "
                       r"= 1{,}422\times10^{-2}\ \text{m} = 14{,}2\ \text{mm}",
                       "$a^4 = 16$ m⁴. Og'ish $a/141$ — qurilish normasi "
                       "odatda $a/250$ talab qiladi, demak bu plastina yupqa."),
                    st(r"M_{\max} = \frac{qa^2}{8} = \frac{10^4 \cdot 4}{8} "
                       r"= 5000\ \text{N·m/m}; \quad "
                       r"\sigma_{\max} = \frac{6M}{h^2} = "
                       r"\frac{30\,000}{4\times10^{-4}} = 75\ \text{MPa}",
                       "Moment balkadagi bilan bir xil, chunki silindrik "
                       "egilishda ikkinchi yo'nalish ishlamaydi."),
                    st(r"\frac{w_{\text{plastina}}}{w_{\text{balka}}} = "
                       r"\frac{EI}{D} = 1 - \nu^2 = 0{,}91",
                       "Plastina balkadan 9 % kam egiladi — aynan "
                       "$(1-\\nu^2)$ ko'paytuvchi tufayli (pq-03)."),
                ],
                answer=(
                    "$w(x) = \\frac{q}{24D}(x^4 - 2ax^3 + a^3x)$, "
                    "$w_{\\max} = 5qa^4/(384D) = 14{,}2$ mm; "
                    "$M_{\\max} = qa^2/8 = 5000$ N·m/m, "
                    "$\\sigma_{\\max} = 75$ MPa. Plastina bir xil "
                    "kesimli balkadan 9 % kam egiladi."
                ),
                engineering_note=(
                    "Silindrik egilish — plastina hisobidagi eng muhim "
                    "**tekshirish holati**. Har qanday sonli yechim "
                    "(FEM, chekli ayirmalar) avval shu holatda "
                    "sinaladi, chunki aniq yechim ma'lum. Bundan "
                    "tashqari, u xavfsiz tomonga taxmin beradi: "
                    "$b/a > 3$ bo'lgan plastinada haqiqiy og'ish "
                    "silindrik egilishdagidan kichik, chunki qisqa "
                    "yo'nalish ham qisman ishlaydi."
                ),
            ),
            computation=Computation(
                caption=(
                    "Bigarmonik tenglamani sonli tekshirish, silindrik "
                    "egilish aniq yechimi va Navye qatori bilan taqqoslash."
                ),
                code='''"""Sofi Jermen-Lagranj tenglamasi: D*nabla^4 w = q."""
import numpy as np
from labkit import PARAMS, note, series, table, value

a = float(PARAMS.get("a", 2.0))           # plastina tomoni x bo'yicha, m
b = float(PARAMS.get("b", 6.0))           # y bo'yicha, m
h = float(PARAMS.get("h", 20.0))/1000.0   # qalinlik, m
E = float(PARAMS.get("E", 200.0))*1e9     # Pa
nu = float(PARAMS.get("nu", 0.3))
qload = float(PARAMS.get("q", 10000.0))   # Pa

D = E*h**3/(12*(1 - nu**2))
value("Silindrik bikrlik D", D/1000, "kN*m")
value("Tomonlar nisbati b/a", b/a, "—")

# --- 1) Silindrik egilish (aniq yechim) ---
x = np.linspace(0.0, a, 300)
xi = x/a
w_cyl = qload*a**4/(24*D)*(xi**4 - 2*xi**3 + xi)
w_max_cyl = 5*qload*a**4/(384*D)
series("Silindrik egilish w(x)", x.tolist(), (w_cyl*1000).tolist(),
       xlabel="x, m", ylabel="Og'ish w, mm")
value("w_max (silindrik, analitik)", w_max_cyl*1000, "mm")
value("w_max (yechimdan)", float(np.max(w_cyl))*1000, "mm")
value("w_max / a", w_max_cyl/a, "—")
value("a / w_max", a/w_max_cyl, "—")
value("w_max / h", w_max_cyl/h, "—")

M_max = qload*a**2/8
value("M_max (silindrik)", M_max, "N*m/m")
value("sigma_max", 6*M_max/h**2/1e6, "MPa")

w_beam = 5*qload*a**4/(384*(E*h**3/12))
value("Balka og'ishi (birlik kenglik)", w_beam*1000, "mm")
value("Plastina / balka nisbati", w_max_cyl/w_beam, "—")
note(f"Plastina balkadan {100*(1 - w_max_cyl/w_beam):.1f} % kam egiladi — "
     f"aynan (1 - nu^2) = {1-nu**2:.3f} ko'paytuvchi tufayli.")

# --- 2) Tenglamani sonli tekshirish: qoldiqni hisoblash ---
n = 161
xs = np.linspace(0.0, a, n)
dx = xs[1] - xs[0]
w_num = qload*a**4/(24*D)*((xs/a)**4 - 2*(xs/a)**3 + (xs/a))
# to'rtinchi hosila markaziy ayirma bilan
w4 = np.zeros(n)
w4[2:-2] = (w_num[4:] - 4*w_num[3:-1] + 6*w_num[2:-2]
            - 4*w_num[1:-3] + w_num[:-4])/dx**4
resid = D*w4[2:-2] - qload
value("Maksimal qoldiq |D*w_xxxx - q|", float(np.max(np.abs(resid))), "Pa")
value("Nisbiy qoldiq", float(np.max(np.abs(resid)))/qload*100, "%")
note(f"Aniq yechim tenglamani {float(np.max(np.abs(resid)))/qload*100:.2e} % "
     f"aniqlikda qanoatlantiradi — bu sonli differensiallash xatosi, "
     f"yechim xatosi emas.")

# --- 3) Navye qatori bilan to'liq 2D yechim ---
N = 30
Xg = np.linspace(0.0, a, 61)
Yg = np.linspace(0.0, b, 61)
XX, YY = np.meshgrid(Xg, Yg, indexing="ij")
W2 = np.zeros_like(XX)
for m in range(1, 2*N, 2):
    for k in range(1, 2*N, 2):
        qmn = 16*qload/(np.pi**2*m*k)
        denom = D*np.pi**4*((m/a)**2 + (k/b)**2)**2
        W2 += qmn/denom*np.sin(m*np.pi*XX/a)*np.sin(k*np.pi*YY/b)

w_max_2d = float(np.max(W2))
value("w_max (2D Navye, b/a = %.1f)" % (b/a), w_max_2d*1000, "mm")
value("2D / silindrik nisbati", w_max_2d/w_max_cyl, "—")
note(f"b/a = {b/a:.1f} da 2D yechim silindrik egilishning "
     f"{100*w_max_2d/w_max_cyl:.1f} % ini beradi — qisqa yo'nalish "
     f"yukning bir qismini oladi, shuning uchun og'ish kamroq.")

mid = W2[:, W2.shape[1]//2]
series("w(x) markaziy kesim (2D)", Xg.tolist(), (mid*1000).tolist(),
       xlabel="x, m", ylabel="Og'ish w, mm")
series("w(x) silindrik egilish", x.tolist(), (w_cyl*1000).tolist(),
       xlabel="x, m", ylabel="Og'ish w, mm")

# --- 4) b/a nisbatining ta'siri ---
ratios = np.linspace(1.0, 5.0, 25)
wr = []
for r_ in ratios:
    bb = r_*a
    s = 0.0
    for m in range(1, 2*N, 2):
        for k in range(1, 2*N, 2):
            qmn = 16*qload/(np.pi**2*m*k)
            denom = D*np.pi**4*((m/a)**2 + (k/bb)**2)**2
            s += qmn/denom*np.sin(m*np.pi/2)*np.sin(k*np.pi/2)
    wr.append(s/w_max_cyl)
series("w_max(b/a) / w_silindrik", ratios.tolist(), wr,
       xlabel="Tomonlar nisbati b/a", ylabel="Nisbat")
value("Nisbat b/a = 1 da", wr[0], "—")
value("Nisbat b/a = 5 da", wr[-1], "—")
note(f"b/a = 1 (kvadrat) da og'ish silindrik holatning "
     f"{100*wr[0]:.1f} % i; b/a -> katta bo'lganda 100 % ga intiladi.")

table("Bigarmonik operatorning hadlari",
      ["Had", "Fizik ma'nosi", "Silindrik egilishda"],
      [["d4w/dx4", "x yo'nalishidagi egilish qarshiligi", "yagona qoladi"],
       ["2*d4w/dx2dy2", "ikki yo'nalishning o'zaro ta'siri", "nolga teng"],
       ["d4w/dy4", "y yo'nalishidagi egilish qarshiligi", "nolga teng"]])

table("Plastina va balka tenglamalarining taqqoslashi",
      ["Jihat", "Balka", "Plastina"],
      [["Tenglama", "EI*w_xxxx = q", "D*nabla^4 w = q"],
       ["Tartib", "4 (ODE)", "4 (PDE)"],
       ["Noma'lum", "w(x)", "w(x, y)"],
       ["Chegaraviy shart", "2 ta har uchida", "2 ta konturning har nuqtasida"],
       ["nu roli", "yo'q", "faqat D ichida va chegaraviy shartlarda"]])
''',
                parameters=[
                    p("a", "Plastina tomoni a", 0.2, 20.0, 2.0, 0.1, "m"),
                    p("b", "Plastina tomoni b", 0.2, 40.0, 6.0, 0.1, "m"),
                    p("h", "Qalinlik h", 1.0, 300.0, 20.0, 1.0, "mm"),
                    p("E", "Yung moduli E", 1.0, 400.0, 200.0, 1.0, "GPa"),
                    p("nu", "Puasson koeffitsienti ν", 0.0, 0.45, 0.3, 0.01),
                    p("q", "Yuklama q", 100.0, 200000.0, 10000.0, 100.0, "Pa"),
                ],
                expected_output=(
                    "D = 146,5 kN·m; silindrik w_max = 14,2 mm, "
                    "M_max = 5000 N·m/m, σ_max = 75 MPa; qoldiq "
                    "< 10⁻³ %; b/a = 3 da 2D yechim silindrikning "
                    "≈ 96 % i, kvadratda ≈ 32 % i."
                ),
            ),
            visual=vis(
                kind="Element muvozanati va og'ish sirti",
                tool="React/SVG + Manim",
                description=(
                    "Plastina elementidagi kuch va momentlar, og'ish "
                    "sirtining kontur tasviri va $b/a$ ning ta'siri."
                ),
                how_to_draw=(
                    "React/SVG: element muvozanati paneli — "
                    "$dx \\times dy$ to'rtburchak izometrik proeksiyada "
                    "chiziladi. Har bir yuzda: egish momenti ikki "
                    "boshli strelka (aylanish), buralish momenti "
                    "boshqa rangdagi ikki boshli strelka, kesuvchi "
                    "kuch to'g'ri strelka. Qarama-qarshi yuzlarda "
                    "qiymatlar $+\\partial(\\cdot)/\\partial x\\,dx$ "
                    "bilan yozilgan yorliqlar. Og'ish sirti paneli: "
                    "$w(x,y)$ kontur chiziqlari (10–12 daraja) "
                    "ketma-ket rang bilan; ustiga to'rtta chekka "
                    "chegaraviy sharti belgilanadi (sharnirli — "
                    "uchburchak tayanch belgisi). Uchinchi panel: "
                    "$b/a$ slayderi bilan boshqariladigan grafik — "
                    "og'ishning silindrik holatga nisbati; $b/a \\to "
                    "\\infty$ da 1 ga intilishi ko'rinadi. Barcha "
                    "kontur chizishda `d3-contour` o'rniga sodda "
                    "marching-squares implementatsiyasi ishlatiladi "
                    "(tashqi kutubxonasiz)."
                ),
            ),
            interp=(
                "$b/a$ grafigi plastina va balka farqini eng aniq "
                "ko'rsatadi: kvadrat plastinada ($b/a = 1$) og'ish "
                "silindrik egilishdagining atigi 32 % i. Demak ikkinchi "
                "yo'nalish yukning **uchdan ikki qismini** oladi — "
                "plastina bir yo'nalishli balkadan uch baravar samaraliroq. "
                "Bu temir-beton qurilishdagi muhim qaror: kvadratga yaqin "
                "plita ikki yo'nalishli armaturalanadi va material tejaladi; "
                "$b/a > 3$ bo'lganda esa qisqa yo'nalish deyarli butun "
                "yukni oladi va bir yo'nalishli plita sifatida hisoblash "
                "mumkin (grafik $b/a = 3$ da 96 % ni ko'rsatadi, xatosi "
                "4 %). Sonli qoldiq tekshiruvi ($< 10^{-3}$ %) esa "
                "boshqa maqsadga xizmat qiladi: u bizning aniq "
                "yechimimiz haqiqatan ham tenglamani qanoatlantirishini "
                "mustaqil tasdiqlaydi. Bu — har qanday sonli kodni "
                "ishonchli qilishning birinchi qoidasi: aniq yechimi "
                "ma'lum masalada tekshirish (method of manufactured "
                "solutions), va u 5-fanda tizimli o'rganiladi."
            ),
            mistakes=[
                "Aralash hosila hadidagi koeffitsient 2 ni unutish. "
                "$\\nabla^4 = \\partial_x^4 + 2\\partial_x^2\\partial_y^2 "
                "+ \\partial_y^4$ — bu Laplasianning kvadrati, shuning "
                "uchun o'rta had ikkilangan.",
                "Kesuvchi kuchni Guk qonunidan topishga urinish. "
                "Kirxhoff nazariyasida $\\gamma_{xz} = 0$, demak "
                "$Q = G\\gamma = 0$ chiqadi — bu xato. $Q$ faqat "
                "muvozanatdan topiladi.",
                "$\\nu$ tenglamada qolgan deb o'ylash. U aynan "
                "qisqaradi; $\\nu$ faqat $D$ da va erkin chekka "
                "shartlarida qatnashadi.",
                "Bir jinsli yechimni unutib, faqat xususiy yechim bilan "
                "cheklanish. $w_p = qx^4/(24D)$ o'zi chegaraviy "
                "shartlarni qanoatlantirmaydi — to'rtta doimiy zarur.",
            ],
            quiz=[
                q("Sofi Jermen–Lagranj tenglamasini yozing va hadlarini "
                  "izohlang.",
                  "$D\\nabla^4 w = q$. Chap tomon — plastinaning egilish "
                  "qarshiligi, o'ng tomon — taqsimlangan yuklama. "
                  "$\\nabla^4$ ichidagi aralash had ikki yo'nalishning "
                  "o'zaro ta'sirini ifodalaydi.", "konseptual"),
                q("Nima uchun Puasson koeffitsienti tenglamadan yo'qoladi?",
                  "Aralash hosila koeffitsientlari yig'indisi "
                  "$\\nu + 2(1-\\nu) + \\nu = 2$ bo'ladi — $\\nu$ aynan "
                  "qisqaradi. U faqat $D$ ichida va chegaraviy "
                  "shartlarda qoladi.", "konseptual"),
                q("Silindrik egilishda tenglama qanday shaklga keladi?",
                  "$Dw'''' = q$ — aynan balka tenglamasi, faqat $EI$ "
                  "o'rnida $D$. Og'ish $(1-\\nu^2)$ marta kam chiqadi.",
                  "hisob"),
                q("Kesuvchi kuch $Q_x$ qanday topiladi?",
                  "Moment muvozanatidan: $Q_x = \\partial M_x/\\partial x "
                  "+ \\partial M_{xy}/\\partial y$. Guk qonunidan emas, "
                  "chunki Kirxhoff nazariyasida sdvig deformatsiyasi nol.",
                  "konseptual"),
                q("Kodda qoldiq $|Dw'''' - q|$ nima uchun hisoblanadi?",
                  "Yechimning to'g'riligini mustaqil tekshirish uchun: "
                  "aniq yechim tenglamani qanoatlantirishi kerak. "
                  "Qolgan farq — sonli differensiallash xatosi.", "kod"),
                q("$b/a = 1$ da og'ish nima uchun silindrik holatdan "
                  "uch marta kichik?",
                  "Kvadrat plastinada ikkala yo'nalish ham yukni "
                  "qabul qiladi; silindrik egilishda esa faqat bittasi "
                  "ishlaydi. Ikki yo'nalishli ishlash samaradorlikni "
                  "keskin oshiradi.", "talqin"),
            ],
            bridge=(
                "Tenglama tayyor, lekin uni yechish uchun chegaraviy "
                "shartlar kerak. Plastinada bu masala balkadagidan "
                "ancha nozik: erkin chekkada uchta tabiiy shart "
                "paydo bo'ladi, lekin to'rtinchi tartibli tenglama "
                "faqat ikkitasini qabul qila oladi. Kirxhoff bu "
                "paradoksni qanday hal qilgan?"
            ),
            research=(
                "Bigarmonik tenglamaning fundamental yechimini "
                "o'rganing: cheksiz plastinada konsentrlangan kuch $P$ "
                "ostida $w = \\frac{P r^2\\ln r}{8\\pi D}$. Uni "
                "$D\\nabla^4 w = P\\delta(\\mathbf{x})$ tenglamasiga "
                "qo'yib tekshiring (umumlashgan funksiyalar ma'nosida). "
                "Nima uchun og'ish chekli, lekin moment "
                "logarifmik singulyarlikka ega? Bu natija FEM da "
                "konsentrlangan kuch qo'yilganda tur zichlashtirilganda "
                "kuchlanishning yaqinlashmasligini qanday tushuntiradi?"
            ),
            manim_ref=manim(
                scene="PlateEquationScene",
                module="animatsiya/scenes/pq_plate_basics.py",
                title="Bigarmonik tenglamaning keltirib chiqarilishi",
                summary=(
                    "Element muvozanatidan boshlab kesuvchi kuchlar "
                    "yo'qotiladi, momentlar egriliklar bilan "
                    "almashtiriladi va Puasson koeffitsientining "
                    "qisqarishi bosqichma-bosqich ko'rsatiladi."
                ),
            ),
        ),
    ),

    # ------------------------------------------------------------------ pq-05
    Topic(
        id="pq-05",
        subject_id=S, module_id=M, order=5,
        title="Chegaraviy shartlar va Kirxhoff kesuvchi kuchi; burchak reaksiyasi",
        description=(
            "Plastina chekkalaridagi chegaraviy shartlar turlari, erkin "
            "chekkadagi uch shart paradoksi, Kirxhoffning ekvivalent "
            "kesuvchi kuchi va burchaklardagi konsentrlangan reaksiya."
        ),
        learning_objective=(
            "Har bir chekka turi uchun to'g'ri chegaraviy shartlarni "
            "yozish, Kirxhoff kesuvchi kuchini variatsion yo'l bilan "
            "asoslash va burchak reaksiyasini hisoblash."
        ),
        prerequisites=["pq-04", "tmm-19"],
        mathematical_core=(
            "Variatsion formulirovka, chegaraviy had bo'ylab integrallash, "
            "$V_n = Q_n + \\partial M_{nt}/\\partial t$, burchakdagi "
            "sakrash $R = 2M_{xy}$."
        ),
        engineering_application=(
            "Erkin tayangan plitalarning burchaklarini ankerlash, "
            "konstruksiya tayanchlarini loyihalash, FEM da chegaraviy "
            "shartlarni to'g'ri qo'yish."
        ),
        computational_component=(
            "Turli chegaraviy shartlarda og'ish va momentlarni "
            "taqqoslash, burchak reaksiyasini hisoblash, "
            "$V_n$ va $Q_n$ farqini ko'rsatish."
        ),
        visualization_component=(
            "Chegaraviy shartlar sxemalari, burchakdagi buralish "
            "momentining ekvivalent kuchlar juftligiga aylanishi."
        ),
        research_extension=(
            "Reissner–Mindlin nazariyasida chegaraviy shartlar "
            "paradoksi yo'qolishini o'rganing: nima uchun u yerda uchta "
            "shartni ham qo'yish mumkin?"
        ),
        difficulty="murakkab",
        previous_link=(
            "pq-04 dagi to'rtinchi tartibli tenglama konturning har "
            "nuqtasida ikkita shart talab qiladi. tmm-19 dagi variatsion "
            "prinsip esa tabiiy chegaraviy shartlarni avtomatik beradi — "
            "aynan shu apparat erkin chekka paradoksini hal qiladi."
        ),
        next_topic="pq-06",
        estimated_minutes=90,
        tags=["chegaraviy shart", "Kirxhoff", "burchak", "variatsion"],
        lesson=_lesson(
            problem=(
                "Erkin chekkada uchta narsa nolga teng bo'lishi kerak "
                "ko'rinadi: egish momenti $M_n$, buralish momenti "
                "$M_{nt}$ va kesuvchi kuch $Q_n$ — chunki chekkaga hech "
                "narsa ta'sir qilmayapti. Lekin to'rtinchi tartibli "
                "tenglama har nuqtada faqat **ikkita** shartni qabul "
                "qiladi. Uchtasini qo'ysak, masala ortiqcha aniqlangan "
                "va yechim mavjud bo'lmaydi. Poisson 1829-yilda shu "
                "paradoksga duch keldi; Kirxhoff 1850-yilda uni hal "
                "qildi. Qanday?"
            ),
            concepts=[
                c("Sharnirli tayanch (simply supported)",
                  "$w = 0$, $M_n = 0$ — chekka ko'chmaydi, lekin erkin "
                  "buriladi. Eng ko'p uchraydigan ideallashtirish."),
                c("Qattiq mahkamlash (clamped/fixed)",
                  "$w = 0$, $\\partial w/\\partial n = 0$ — chekka "
                  "ko'chmaydi va burilmaydi. Eng bikr shart."),
                c("Erkin chekka (free edge)",
                  "$M_n = 0$, $V_n = 0$ — hech qanday cheklov yo'q. "
                  "Aynan shu yerda Kirxhoff paradoksi paydo bo'ladi."),
                c("Kirxhoff ekvivalent kesuvchi kuchi $V_n$",
                  "$V_n = Q_n + \\frac{\\partial M_{nt}}{\\partial t}$ — "
                  "kesuvchi kuch va buralish momentining o'zgarishini "
                  "birlashtiruvchi kattalik. Aynan u nolga tenglashtiriladi."),
                c("Burchak reaksiyasi",
                  "Ikki erkin (yoki sharnirli) chekka kesishgan "
                  "burchakda konsentrlangan reaksiya $R = 2M_{xy}$ "
                  "paydo bo'ladi — buralish momentining sakrashi natijasi."),
                c("Tabiiy va muhim chegaraviy shartlar",
                  "Muhim (essential): $w$, $\\partial w/\\partial n$ — "
                  "oldindan qo'yiladi. Tabiiy (natural): $M_n$, $V_n$ — "
                  "variatsion prinsipdan o'z-o'zidan chiqadi."),
            ],
            derivation=[
                d("1. Variatsion formulirovka",
                  r"\Pi = \frac{D}{2}\int_A\Big[(\nabla^2 w)^2 - 2(1-\nu)"
                  r"\big(w_{,xx}w_{,yy} - w_{,xy}^2\big)\Big]dA - \int_A qw\,dA",
                  "tmm-19 dagi minimal potensial energiya prinsipi. "
                  "Ikkinchi had — Gauss egriligi integrali; u "
                  "chegaraviy hadlarga ta'sir qiladi, tenglamaga esa yo'q."),
                d("2. Variatsiyani olish va ikki marta bo'laklab integrallash",
                  r"\delta\Pi = \int_A (D\nabla^4 w - q)\,\delta w\,dA "
                  r"+ \oint_\Gamma [\text{chegaraviy hadlar}]\,ds = 0",
                  "Sohaviy had nolga tenglashib tenglamani beradi "
                  "(pq-04). Chegaraviy hadlar esa qanday shartlar "
                  "qo'yilishi kerakligini aytadi."),
                d("3. Chegaraviy hadlarning tuzilishi",
                  r"\oint_\Gamma\Big[-Q_n\,\delta w + M_n\,\delta\frac{\partial w}"
                  r"{\partial n} + M_{nt}\,\delta\frac{\partial w}{\partial t}\Big]ds",
                  "Uchta had, uchta variatsiya. Lekin "
                  "$\\delta(\\partial w/\\partial t)$ mustaqil emas — "
                  "u chekka bo'ylab $\\delta w$ ning hosilasi!"),
                d("4. Uchinchi hadni bo'laklab integrallash",
                  r"\oint_\Gamma M_{nt}\frac{\partial(\delta w)}{\partial t}ds "
                  r"= \big[M_{nt}\delta w\big]_{\text{burchaklar}} - "
                  r"\oint_\Gamma \frac{\partial M_{nt}}{\partial t}\delta w\,ds",
                  "Bu — hal qiluvchi qadam. Buralish momenti hadi "
                  "ikkiga bo'linadi: burchaklardagi konsentrlangan had "
                  "va chekka bo'ylab taqsimlangan had."),
                d("5. Kirxhoff kesuvchi kuchining paydo bo'lishi",
                  r"\oint_\Gamma\Big[-\underbrace{\Big(Q_n + \frac{\partial M_{nt}}"
                  r"{\partial t}\Big)}_{V_n}\delta w + M_n\,\delta\frac{\partial w}"
                  r"{\partial n}\Big]ds + \big[M_{nt}\delta w\big]_{\text{burch}} = 0",
                  "Endi faqat **ikkita** mustaqil variatsiya qoldi: "
                  "$\\delta w$ va $\\delta(\\partial w/\\partial n)$. "
                  "Paradoks hal bo'ldi — uchta shart ikkitaga birlashdi."),
                d("6. Erkin chekka shartlari",
                  r"M_n = 0 \quad\text{va}\quad V_n = Q_n + "
                  r"\frac{\partial M_{nt}}{\partial t} = 0",
                  "$\\delta w$ va $\\delta(\\partial w/\\partial n)$ "
                  "ixtiyoriy bo'lgani uchun ularning koeffitsientlari "
                  "nolga teng bo'lishi kerak."),
                d("7. Burchak reaksiyasi",
                  r"R = \big[M_{nt}\big]_{\text{sakrash}} = 2M_{xy}\Big|_{\text{burchak}}",
                  "Burchakda ikki chekka kesishadi va $M_{nt}$ ishorasi "
                  "o'zgaradi. Sakrash $M_{xy} - (-M_{xy}) = 2M_{xy}$ — "
                  "bu konsentrlangan kuch sifatida namoyon bo'ladi."),
                d("8. $V_n$ ni og'ish orqali ifodalash",
                  r"V_x = -D\Big[\frac{\partial^3 w}{\partial x^3} + "
                  r"(2-\nu)\frac{\partial^3 w}{\partial x\partial y^2}\Big]",
                  "$Q_x$ va $\\partial M_{xy}/\\partial y$ ni og'ish "
                  "orqali yozib qo'shamiz. Koeffitsient $(2-\\nu)$ — "
                  "aynan Kirxhoff birlashmasining izi."),
            ],
            meaning=(
                "Kirxhoffning g'oyasi fizik jihatdan juda nafis. "
                "Buralish momenti $M_{nt}$ chekka bo'ylab taqsimlangan. "
                "Uni har bir kichik $ds$ uzunlikda ekvivalent **kuchlar "
                "juftligiga** almashtiramiz: $M_{nt}$ kattalikdagi "
                "moment = $M_{nt}/ds$ kattalikdagi ikki qarama-qarshi "
                "vertikal kuch, $ds$ masofada. Qo'shni elementlarda bu "
                "kuchlar qisman o'zaro qisqaradi va qolgan farq "
                "$\\partial M_{nt}/\\partial t$ ga teng bo'ladi — u "
                "taqsimlangan kesuvchi kuch kabi ta'sir qiladi. "
                "Burchakda esa qisqarish uchun juft yo'q: u yerda "
                "kuch to'liq qoladi va konsentrlangan reaksiya beradi. "
                "Bu shunchaki matematik hiyla emas — **o'lchanadigan "
                "fizik hodisa**. Erkin tayangan kvadrat plastinaning "
                "burchaklarini ushlab turmasa, ular haqiqatan ham "
                "ko'tariladi, chunki $R = 2M_{xy}$ reaksiya pastga "
                "yo'nalgan bo'lishi kerak edi. Shuning uchun temir-beton "
                "plitalarda burchaklar maxsus ankerlanadi va u yerga "
                "qo'shimcha armatura qo'yiladi. Sen-Venan prinsipi "
                "(mq-05) esa almashtirishning maqbulligini kafolatlaydi: "
                "chekkadan $\\sim h$ masofada yechim to'g'ri bo'ladi, "
                "chekkaning o'zida esa mahalliy farq qoladi."
            ),
            equations=[
                eq(r"V_n = Q_n + \frac{\partial M_{nt}}{\partial t}",
                   "Kirxhoffning ekvivalent kesuvchi kuchi.",
                   "Kirxhoff kesuvchi kuchi"),
                eq(r"V_x = -D\Big[\frac{\partial^3 w}{\partial x^3} + "
                   r"(2-\nu)\frac{\partial^3 w}{\partial x\partial y^2}\Big]",
                   "$V_x$ og'ish orqali.", "V_x ifodasi"),
                eq(r"R_{\text{burchak}} = 2M_{xy} = -2D(1-\nu)"
                   r"\frac{\partial^2 w}{\partial x\partial y}",
                   "Burchakdagi konsentrlangan reaksiya.",
                   "Burchak reaksiyasi"),
                eq(r"\text{Sharnirli: } w = 0,\ \frac{\partial^2 w}"
                   r"{\partial n^2} = 0",
                   "Sharnirli tayanchning og'ish orqali ifodasi "
                   "(to'g'ri chekkada).", "Sharnirli shart"),
            ],
            conditions=(
                "**Chegaraviy shartlar jadvali** ($x = $ const chekka uchun):\n\n"
                "| Chekka turi | 1-shart | 2-shart |\n"
                "|---|---|---|\n"
                "| Qattiq mahkamlash | $w = 0$ | $\\partial w/\\partial x = 0$ |\n"
                "| Sharnirli tayanch | $w = 0$ | $M_x = 0$ |\n"
                "| Erkin chekka | $M_x = 0$ | $V_x = 0$ |\n"
                "| Elastik tayanch | $V_x = -k w$ | $M_x = -c\\,\\partial w/\\partial x$ |\n\n"
                "**Sharnirli shartning soddalashishi:** to'g'ri chekkada "
                "$w = 0$ butun chekka bo'ylab, demak $\\partial^2 w/"
                "\\partial y^2 = 0$ ham. $M_x = -D(w_{,xx} + \\nu w_{,yy}) "
                "= 0$ dan $w_{,xx} = 0$ chiqadi. Shuning uchun "
                "$w = 0$, $\\nabla^2 w = 0$ deb yozish mumkin — bu "
                "Navye yechimini (pq-07) ancha soddalashtiradi.\n\n"
                "**Burchak shartlari:** ikki erkin yoki ikki sharnirli "
                "chekka kesishgan burchakda $R = 2M_{xy}$ reaksiya "
                "paydo bo'ladi. Agar burchak erkin bo'lsa (ushlab "
                "turilmagan), $M_{xy} = 0$ sharti qo'yiladi."
            ),
            worked=WorkedExample(
                statement=(
                    "Kvadrat plastina ($a = b = 4$ m, $h = 150$ mm, "
                    "$E = 30$ GPa, $\\nu = 0{,}2$) to'rt chekkasi bo'ylab "
                    "sharnirli tayangan, bir tekis yuklama $q = 6$ kPa. "
                    "Navye yechimining birinchi hadini ishlatib: "
                    "(a) $w_{\\max}$ ni toping; (b) burchakdagi $M_{xy}$ "
                    "va reaksiya $R$ ni hisoblang; (c) reaksiyaning "
                    "yo'nalishini va uning muhandislik oqibatini izohlang."
                ),
                given=[
                    r"a = b = 4\ \text{m},\ h = 0{,}15\ \text{m}",
                    r"E = 30\ \text{GPa},\ \nu = 0{,}2,\ q = 6000\ \text{Pa}",
                ],
                steps=[
                    st(r"D = \frac{30\times10^9 \cdot 0{,}15^3}{12(1-0{,}04)} "
                       r"= \frac{1{,}0125\times10^{8}}{11{,}52} "
                       r"= 8{,}789\times10^{6}\ \text{N·m}",
                       "$h^3 = 3{,}375\\times10^{-3}$ m³. $D = 8{,}79$ MN·m."),
                    st(r"w_{11} = \frac{16q}{\pi^6 D}\cdot\frac{1}"
                       r"{\big(1/a^2 + 1/b^2\big)^2}",
                       "Navye qatorining birinchi hadi ($m = k = 1$); "
                       "to'liq yechim pq-07 da."),
                    st(r"\Big(\frac{1}{16} + \frac{1}{16}\Big)^2 = "
                       r"(0{,}125)^2 = 0{,}015625; \quad \pi^6 = 961{,}39",
                       "Kvadrat plastina uchun maxraj."),
                    st(r"w_{\max} \approx \frac{16 \cdot 6000}"
                       r"{961{,}39 \cdot 8{,}789\times10^{6} \cdot 0{,}015625} "
                       r"= \frac{96\,000}{1{,}3204\times10^{8}} "
                       r"= 7{,}27\times10^{-4}\ \text{m} = 0{,}727\ \text{mm}",
                       "Birinchi had. To'liq qator 0,725 mm beradi — "
                       "birinchi had 99,7 % aniqlik beradi."),
                    st(r"w = w_{11}\sin\frac{\pi x}{a}\sin\frac{\pi y}{a} "
                       r"\;\Rightarrow\; \frac{\partial^2 w}{\partial x\partial y} "
                       r"= w_{11}\frac{\pi^2}{a^2}\cos\frac{\pi x}{a}"
                       r"\cos\frac{\pi y}{a}",
                       "Aralash hosila — burchakda ($x = y = 0$) kosinuslar "
                       "birga teng, ya'ni maksimal."),
                    st(r"\frac{\partial^2 w}{\partial x\partial y}\Big|_{(0,0)} "
                       r"= 7{,}27\times10^{-4}\cdot\frac{9{,}8696}{16} "
                       r"= 4{,}485\times10^{-4}\ \text{m}^{-1}",
                       "$\\pi^2/a^2 = 9{,}8696/16 = 0{,}61685$ 1/m²."),
                    st(r"M_{xy} = -D(1-\nu)\frac{\partial^2 w}{\partial x\partial y} "
                       r"= -8{,}789\times10^{6} \cdot 0{,}8 \cdot "
                       r"4{,}485\times10^{-4} = -3153\ \text{N·m/m}",
                       "Buralish momenti burchakda maksimal."),
                    st(r"R = 2M_{xy} = -6306\ \text{N} \approx -6{,}31\ \text{kN}",
                       "Manfiy — reaksiya **pastga** yo'nalgan, ya'ni "
                       "tayanch plastinani pastga tortib turishi kerak. "
                       "Agar ushlab turilmasa, burchak ko'tariladi."),
                ],
                answer=(
                    "$D = 8{,}79$ MN·m, $w_{\\max} \\approx 0{,}73$ mm; "
                    "burchakda $M_{xy} = -3153$ N·m/m, konsentrlangan "
                    "reaksiya $R = -6{,}31$ kN (pastga). Burchaklar "
                    "ushlab turilmasa ko'tariladi."
                ),
                engineering_note=(
                    "6,31 kN — plastinaning umumiy og'irligining "
                    "($6 \\cdot 16 = 96$ kN) 6,6 % i, lekin u bitta "
                    "nuqtaga to'plangan. Temir-beton plitalarda bu "
                    "reaksiya burchak armaturasi bilan qabul qilinadi: "
                    "plita burchagiga yuqori va pastki zonalarda "
                    "diagonal to'r qo'yiladi. Metall panellarda esa "
                    "burchak boltlari yoki payvand qo'yiladi. Eng "
                    "xavfli xato — burchakni umuman ushlamaslik: "
                    "u holda plita burchagi ko'tariladi, yuklama "
                    "qayta taqsimlanadi va markazdagi moment "
                    "hisoblangandan 15–20 % katta bo'lib ketadi."
                ),
            ),
            computation=Computation(
                caption=(
                    "Turli chegaraviy shartlarda og'ishni taqqoslash, "
                    "burchak reaksiyasini hisoblash va $V_n$ bilan $Q_n$ "
                    "farqini ko'rsatish."
                ),
                code='''"""Plastina chegaraviy shartlari va Kirxhoff kesuvchi kuchi."""
import numpy as np
from labkit import PARAMS, note, series, table, value

a = float(PARAMS.get("a", 4.0))
b = float(PARAMS.get("b", 4.0))
h = float(PARAMS.get("h", 150.0))/1000.0
E = float(PARAMS.get("E", 30.0))*1e9
nu = float(PARAMS.get("nu", 0.2))
qload = float(PARAMS.get("q", 6000.0))

D = E*h**3/(12*(1 - nu**2))
value("Silindrik bikrlik D", D/1e6, "MN*m")

# --- Navye yechimi (sharnirli, to'liq qator) ---
N = 40
def navier_w(X, Y, nterms=N):
    W = np.zeros_like(X)
    for m in range(1, 2*nterms, 2):
        for k in range(1, 2*nterms, 2):
            qmn = 16*qload/(np.pi**2*m*k)
            den = D*np.pi**4*((m/a)**2 + (k/b)**2)**2
            W += qmn/den*np.sin(m*np.pi*X/a)*np.sin(k*np.pi*Y/b)
    return W


ng = 81
xg = np.linspace(0.0, a, ng)
yg = np.linspace(0.0, b, ng)
XX, YY = np.meshgrid(xg, yg, indexing="ij")
W = navier_w(XX, YY)
w_max = float(np.max(W))
value("w_max (to'liq Navye qatori)", w_max*1000, "mm")

# Birinchi had bilan taqqoslash
w11 = 16*qload/(np.pi**6*D*(1/a**2 + 1/b**2)**2)
value("w_max (faqat 1-had)", w11*1000, "mm")
value("1-had aniqligi", 100*w11/w_max, "%")

# --- Burchak buralish momenti va reaksiya (1-had bo'yicha) ---
wxy_corner = w11*np.pi**2/(a*b)
Mxy_corner = -D*(1 - nu)*wxy_corner
R_corner = 2*Mxy_corner
value("d2w/dxdy burchakda", wxy_corner, "1/m")
value("M_xy burchakda", Mxy_corner, "N*m/m")
value("Burchak reaksiyasi R = 2*M_xy", R_corner/1000, "kN")
value("Plastina umumiy og'irligi q*a*b", qload*a*b/1000, "kN")
value("R / (q*a*b)", abs(R_corner)/(qload*a*b)*100, "%")
if R_corner < 0:
    note(f"R = {R_corner/1000:.2f} kN < 0: reaksiya PASTGA yo'nalgan — "
         f"tayanch plastina burchagini ushlab turishi kerak, aks holda "
         f"burchak ko'tariladi (corner uplift).")

# --- V_n va Q_n farqi chekka bo'ylab ---
# x = 0 chekkasi uchun, 1-had yaqinlashuvi
y = np.linspace(0.0, b, 200)
kx, ky = np.pi/a, np.pi/b
# w = w11 sin(kx x) sin(ky y)
# Q_x = -D d/dx (nabla^2 w);  V_x = -D [w_xxx + (2-nu) w_xyy]
Qx = -D*w11*(-kx*(kx**2 + ky**2))*np.sin(ky*y)      # x = 0 da cos = 1
Vx = -D*w11*(-kx**3 - (2 - nu)*kx*ky**2)*np.sin(ky*y)
series("Q_x(y) chekkada", y.tolist(), (Qx/1000).tolist(),
       xlabel="y, m", ylabel="Kesuvchi kuch, kN/m")
series("V_x(y) Kirxhoff kuchi", y.tolist(), (Vx/1000).tolist(),
       xlabel="y, m", ylabel="Kesuvchi kuch, kN/m")
value("max Q_x", float(np.max(np.abs(Qx)))/1000, "kN/m")
value("max V_x (Kirxhoff)", float(np.max(np.abs(Vx)))/1000, "kN/m")
value("V_x / Q_x nisbati", float(np.max(np.abs(Vx)))/float(np.max(np.abs(Qx))), "—")
note(f"Kirxhoff kuchi Q dan {100*(float(np.max(np.abs(Vx)))/float(np.max(np.abs(Qx))) - 1):.1f} % "
     f"katta: buralish momentining hissasi qo'shilgan.")

# Umumiy reaksiya balansi tekshiruvi
trapz = np.trapezoid if hasattr(np, "trapezoid") else np.trapz
R_edges = 4*float(trapz(Vx, y))            # to'rt chekka
R_corners = 4*R_corner                      # to'rt burchak
value("Chekkalardagi reaksiya (jami)", R_edges/1000, "kN")
value("Burchaklardagi reaksiya (jami)", R_corners/1000, "kN")
value("Jami reaksiya", (R_edges + R_corners)/1000, "kN")
value("Tashqi yuklama", qload*a*b/1000, "kN")
bal = abs(R_edges + R_corners - qload*a*b)/(qload*a*b)*100
note(f"Muvozanat xatosi {bal:.1f} % — 1-had yaqinlashuvidan kelib chiqadi "
     f"(to'liq qator bilan nolga intiladi).")

# --- Turli chegaraviy shartlarda og'ish koeffitsientlari ---
table("Kvadrat plastina: chegaraviy shartlarning ta'siri",
      ["Chegaraviy shart", "alpha (w = alpha*q*a^4/D)", "Nisbat", "Izoh"],
      [["4 chekka sharnirli", 0.004062, 1.000, "Standart holat"],
       ["4 chekka mahkamlangan", 0.001260, 0.310, "3.2 marta bikrroq"],
       ["2 sharnirli, 2 mahkamlangan", 0.002080, 0.512, "Oraliq"],
       ["3 sharnirli, 1 erkin", 0.008700, 2.142, "Erkin chekka yumshatadi"],
       ["2 qarama-qarshi sharnirli, 2 erkin", 0.013020, 3.205,
        "Silindrik egilishga yaqin"]])

for name, alpha in [("4 sharnirli", 0.004062), ("4 mahkamlangan", 0.001260),
                    ("3 sharnirli + 1 erkin", 0.008700)]:
    value(f"w_max ({name})", alpha*qload*a**4/D*1000, "mm")

table("Chegaraviy shartlar turlari (x = const chekka)",
      ["Turi", "1-shart", "2-shart", "Burchak reaksiyasi"],
      [["Qattiq mahkamlash", "w = 0", "dw/dx = 0", "yo'q"],
       ["Sharnirli tayanch", "w = 0", "M_x = 0", "R = 2*M_xy"],
       ["Erkin chekka", "M_x = 0", "V_x = 0", "M_xy = 0 sharti"],
       ["Elastik tayanch", "V_x = -k*w", "M_x = -c*dw/dx", "k, c ga bog'liq"]])

# --- Qalinlikni o'zgartirib burchak reaksiyasini kuzatish ---
h_range = np.linspace(0.05, 0.4, 100)
R_h = []
for hh in h_range:
    Dh = E*hh**3/(12*(1 - nu**2))
    w11h = 16*qload/(np.pi**6*Dh*(1/a**2 + 1/b**2)**2)
    R_h.append(abs(2*(-Dh*(1-nu)*w11h*np.pi**2/(a*b)))/1000)
series("Burchak reaksiyasi R(h)", (h_range*1000).tolist(), R_h,
       xlabel="Qalinlik h, mm", ylabel="|R|, kN")
note(f"Burchak reaksiyasi qalinlikka deyarli bog'liq emas "
     f"({min(R_h):.2f} … {max(R_h):.2f} kN): D ham, w ham h^3 ga "
     f"bog'liq va ular qisqaradi. Demak yupqa plastinada ham "
     f"burchakni ankerlash shart.")
''',
                parameters=[
                    p("a", "Plastina tomoni a", 0.5, 20.0, 4.0, 0.1, "m"),
                    p("b", "Plastina tomoni b", 0.5, 20.0, 4.0, 0.1, "m"),
                    p("h", "Qalinlik h", 20.0, 500.0, 150.0, 5.0, "mm"),
                    p("E", "Yung moduli E", 1.0, 400.0, 30.0, 1.0, "GPa"),
                    p("nu", "Puasson koeffitsienti ν", 0.0, 0.45, 0.2, 0.01),
                    p("q", "Yuklama q", 500.0, 100000.0, 6000.0, 100.0, "Pa"),
                ],
                expected_output=(
                    "D = 8,79 MN·m, w_max ≈ 0,725 mm (1-had 100,3 %); "
                    "burchakda M_xy ≈ −3153 N·m/m, R ≈ −6,3 kN (og'irlikning "
                    "6,6 %); V_x Q_x dan ≈ 45 % katta; burchak reaksiyasi "
                    "qalinlikka deyarli bog'liq emas."
                ),
            ),
            visual=vis(
                kind="Chegaraviy shartlar va burchak reaksiyasi",
                tool="React/SVG",
                description=(
                    "Chekka turlarining sxematik belgilari, buralish "
                    "momentining kuchlar juftligiga aylanishi va "
                    "burchakdagi qoldiq kuch."
                ),
                how_to_draw=(
                    "React/SVG: eng muhim panel — Kirxhoff "
                    "almashtirishining tushuntirilishi. Chekka bo'ylab "
                    "ketma-ket $ds$ bo'laklar chiziladi; har birida "
                    "buralish momenti ikki qarama-qarshi vertikal "
                    "strelka (yuqoriga va pastga) bilan almashtiriladi. "
                    "Qo'shni bo'laklarning qarama-qarshi strelkalari "
                    "ustma-ust tushadi va ular shaffof qilib "
                    "ko'rsatiladi (qisqargan). Qolgan farq — "
                    "$\\partial M_{nt}/\\partial t$ — to'q rangda. "
                    "Oxirgi bo'lakda (burchakda) juft yo'q: u yerda "
                    "strelka to'liq qoladi va $R = 2M_{xy}$ yorlig'i "
                    "bilan belgilanadi. Bu animatsiyani slayder bilan "
                    "boshqarish mumkin: $ds$ kichrayganda qisqarish "
                    "to'liqroq bo'ladi. Ikkinchi panel — plastina "
                    "rejasi, to'rt chekkada chegaraviy shart belgilari "
                    "(uchburchak tayanch = sharnirli, shtrixlangan "
                    "chiziq = mahkamlangan, belgisiz = erkin), "
                    "burchaklarda reaksiya strelkalari. Har bir chekka "
                    "bosilganda turi o'zgaradi va og'ish qiymati "
                    "yangilanadi."
                ),
            ),
            interp=(
                "Chegaraviy shartlar jadvali loyihalashdagi eng katta "
                "'richag'ni ko'rsatadi: to'rt chekkani mahkamlash "
                "og'ishni 3,2 marta kamaytiradi. Bu qalinlikni "
                "$3{,}2^{1/3} = 1{,}47$ marta oshirishga teng — lekin "
                "material qo'shmasdan. Shuning uchun metall "
                "konstruksiyalarda panel chekkalarini payvandlash "
                "(bolt bilan biriktirishdan ko'ra) bikrlikni sezilarli "
                "oshiradi. Aksincha, bitta chekkani erkin qoldirish "
                "og'ishni ikki baravardan ko'p oshiradi — shuning uchun "
                "balkon plitalari va konsol kozirkalar alohida "
                "e'tibor talab qiladi. Burchak reaksiyasining "
                "qalinlikka bog'liq emasligi esa kutilmagan va muhim "
                "natija: $D \\propto h^3$ va $w \\propto 1/h^3$, "
                "ko'paytmada ular qisqaradi. Demak yupqa alyuminiy "
                "panelda ham, qalin beton plitada ham burchakni "
                "ushlash bir xil darajada zarur. $V_x$ ning $Q_x$ dan "
                "45 % katta chiqishi — Kirxhoff almashtirishining "
                "kattaligini ko'rsatadi; agar loyihalashda oddiy "
                "$Q_x$ ishlatilsa, tayanch reaksiyasi sezilarli kam "
                "baholanadi."
            ),
            mistakes=[
                "Erkin chekkada uchta shart ($M_n = M_{nt} = Q_n = 0$) "
                "qo'yish. To'rtinchi tartibli tenglama faqat ikkitasini "
                "qabul qiladi; uchinchisi Kirxhoff birlashmasi orqali "
                "hisobga olinadi.",
                "Burchak reaksiyasini unutish. Sharnirli tayangan "
                "plastinada u har doim mavjud va ko'pincha pastga "
                "yo'nalgan — ankerlash shart.",
                "Sharnirli chekkada $\\partial^2 w/\\partial x^2 = 0$ "
                "o'rniga $\\nabla^2 w = 0$ ni to'g'ri bo'lmagan joyda "
                "ishlatish. Ular faqat to'g'ri chekkada ekvivalent; "
                "egri konturda emas.",
                "$V_n$ o'rniga $Q_n$ ni tayanch reaksiyasi sifatida "
                "olish. Haqiqiy reaksiya $V_n$ ga teng va u 30–50 % "
                "katta bo'lishi mumkin.",
            ],
            quiz=[
                q("Kirxhoff paradoksi nimadan iborat va u qanday hal qilingan?",
                  "Erkin chekkada uchta shart tabiiy ko'rinadi, lekin "
                  "to'rtinchi tartibli tenglama ikkitasini qabul "
                  "qiladi. Kirxhoff buralish momentini ekvivalent "
                  "kesuvchi kuchga qo'shib, $V_n = Q_n + \\partial "
                  "M_{nt}/\\partial t$ ni kiritdi.", "konseptual"),
                q("Burchak reaksiyasi qayerdan paydo bo'ladi?",
                  "Buralish momentini kuchlar juftligiga almashtirganda "
                  "qo'shni elementlarda ular qisqaradi, burchakda esa "
                  "juft yo'q — kuch to'liq qoladi: $R = 2M_{xy}$.",
                  "konseptual"),
                q("Sharnirli tayangan to'g'ri chekkada nima uchun "
                  "$\\nabla^2 w = 0$ deb yozish mumkin?",
                  "$w = 0$ butun chekka bo'ylab, demak $w_{,yy} = 0$. "
                  "$M_x = -D(w_{,xx} + \\nu w_{,yy}) = 0$ dan "
                  "$w_{,xx} = 0$, ya'ni $\\nabla^2 w = 0$.", "hisob"),
                q("To'rt chekkani mahkamlash og'ishni qancha kamaytiradi?",
                  "Kvadrat plastinada $\\alpha$ 0,004062 dan 0,001260 "
                  "ga tushadi — 3,2 marta. Bu qalinlikni 1,47 marta "
                  "oshirishga teng.", "hisob"),
                q("Kodda nima uchun burchak reaksiyasi $h$ ga deyarli "
                  "bog'liq emas?",
                  "$R \\propto D \\cdot w_{11}$, $D \\propto h^3$ va "
                  "$w_{11} \\propto 1/D \\propto 1/h^3$ — ular "
                  "qisqaradi. Demak reaksiya faqat yuklama va "
                  "geometriyaga bog'liq.", "kod"),
                q("Erkin tayangan plita burchagi ankerlanmasa nima bo'ladi?",
                  "Burchak ko'tariladi, yuklama qayta taqsimlanadi va "
                  "markazdagi moment hisoblangandan 15–20 % katta "
                  "bo'lib ketadi — konstruksiya xavfsizlik zaxirasini "
                  "yo'qotadi.", "talqin"),
            ],
            bridge=(
                "Tenglama va chegaraviy shartlar to'liq qo'yildi. "
                "Modulni yakunlash uchun teskari yo'lni bosib o'tamiz: "
                "topilgan og'ishdan momentlarga, momentlardan "
                "kuchlanishlarga qaytib, mustahkamlikni tekshiramiz."
            ),
            research=(
                "Reissner–Mindlin nazariyasida chegaraviy shartlar "
                "paradoksi yo'qolishini o'rganing. U yerda burilish "
                "burchaklari $\\phi_x, \\phi_y$ mustaqil noma'lum, "
                "shuning uchun tenglamalar tizimi ikkinchi tartibli "
                "va har chekkada uchta shart qo'yish mumkin. "
                "Kirxhoff yechimi Mindlin yechimining $h \\to 0$ "
                "dagi limiti ekanligini sonli ko'rsating va chekka "
                "yaqinidagi chegaraviy qatlam (boundary layer) "
                "hodisasini tahlil qiling: uning qalinligi $\\sim h$ "
                "ekanligini tasdiqlang."
            ),
            manim_ref=manim(
                scene="KirchhoffShearScene",
                module="animatsiya/scenes/pq_plate_basics.py",
                title="Kirxhoff kesuvchi kuchi va burchak reaksiyasi",
                summary=(
                    "Chekka bo'ylab buralish momentlari kuchlar "
                    "juftligiga aylanadi, qo'shni juftlar o'zaro "
                    "qisqaradi va burchakda qoldiq konsentrlangan "
                    "kuch $2M_{xy}$ paydo bo'lishi animatsiya qilinadi."
                ),
            ),
        ),
    ),

    # ------------------------------------------------------------------ pq-06
    Topic(
        id="pq-06",
        subject_id=S, module_id=M, order=6,
        title="Plastinadagi kuchlanish holati va mustahkamlik tekshiruvi",
        description=(
            "Momentlardan kuchlanishlarga qaytish, qalinlik bo'yicha "
            "taqsimot, kesuvchi kuchlanishning parabolik epyurasi, "
            "Mizes bo'yicha mustahkamlik va deformatsiya cheklovi."
        ),
        learning_objective=(
            "Plastinaning ixtiyoriy nuqtasidagi to'liq kuchlanish "
            "holatini aniqlash, mustahkamlik va bikrlik shartlarini "
            "tekshirish hamda qalinlikni loyihalash."
        ),
        prerequisites=["pq-05", "tmm-21"],
        mathematical_core=(
            "$\\sigma = 12Mz/h^3$, $\\tau_{xz} = \\frac{3Q}{2h}"
            "\\big(1 - 4z^2/h^2\\big)$, Mizes kriteriysi tekis "
            "kuchlanish holatida, og'ish cheklovi $w \\le a/L$."
        ),
        engineering_application=(
            "Plita qalinligini tanlash, temir-beton armaturasini "
            "hisoblash, metall panelning ruxsat etilgan yuklamasini "
            "aniqlash, normativ tekshiruvlar (SNiP, Eurocode)."
        ),
        computational_component=(
            "Kuchlanish maydonini hisoblash, Mizes kuchlanishining "
            "maksimumini topish, qalinlikni iterativ loyihalash."
        ),
        visualization_component=(
            "Mizes kuchlanishi konturi, qalinlik bo'yicha uch epyura, "
            "qalinlik–yuklama loyihalash diagrammasi."
        ),
        research_extension=(
            "Plastinalarning chegaraviy (limit) tahlilini o'rganing: "
            "oqish chiziqlari nazariyasi (yield line theory) plastik "
            "buzilish yuklamasini qanday beradi?"
        ),
        difficulty="asosiy",
        previous_link=(
            "pq-05 gacha bo'lgan mavzular og'ish maydonini topish "
            "yo'lini qurdi. Endi teskari yo'l: $w \\to \\kappa \\to "
            "M \\to \\sigma$. tmm-21 dagi Mizes kriteriysi bilan "
            "mustahkamlikni tekshiramiz."
        ),
        next_topic="pq-07",
        estimated_minutes=85,
        tags=["kuchlanish", "mustahkamlik", "Mizes", "loyihalash"],
        lesson=_lesson(
            problem=(
                "Sanoat binosi perekrytiyasi uchun po'lat plita "
                "tanlanmoqda. Yuklama, o'lchamlar va material ma'lum. "
                "Qalinlikni qanday tanlaymiz? Ikkita mustaqil talab "
                "bor: (1) **mustahkamlik** — kuchlanish oqish "
                "chegarasidan past bo'lishi; (2) **bikrlik** — og'ish "
                "normativ chegaradan (masalan, $a/250$) kichik "
                "bo'lishi. Qaysi biri hal qiluvchi? Javob geometriyaga "
                "bog'liq va ko'pincha kutilganidan farq qiladi."
            ),
            concepts=[
                c("Normal kuchlanishlar taqsimoti",
                  "$\\sigma_x = 12M_x z/h^3$ — qalinlik bo'yicha "
                  "chiziqli, yuza qatlamlarda maksimal, o'rta sirtda nol."),
                c("Kesuvchi kuchlanish epyurasi",
                  "$\\tau_{xz} = \\frac{3Q_x}{2h}\\big(1 - \\frac{4z^2}"
                  "{h^2}\\big)$ — parabolik, o'rta sirtda maksimal, "
                  "yuzalarda nol. Muvozanatdan topiladi."),
                c("Kuchlanishlar tartibi",
                  "$\\sigma \\sim q(a/h)^2$, $\\tau_{xz} \\sim q(a/h)$, "
                  "$\\sigma_z \\sim q$. Demak "
                  "$\\sigma : \\tau : \\sigma_z = (a/h)^2 : (a/h) : 1$ — "
                  "yupqa plastinada normal kuchlanish hukmron."),
                c("Bikrlik sharti (serviceability)",
                  "$w_{\\max} \\le a/L$, bunda $L = 200\\ldots400$ "
                  "normativga bog'liq. Ko'pincha mustahkamlikdan oldin bajariladi."),
                c("Loyihalash mezoni",
                  "Qalinlik ikkala shartdan kattarog'i bo'yicha "
                  "tanlanadi: $h = \\max(h_{\\text{mustahkamlik}}, "
                  "h_{\\text{bikrlik}})$."),
                c("Hukmron mezon",
                  "$\\sigma \\propto 1/h^2$, $w \\propto 1/h^3$ — "
                  "demak qalinlik oshganda og'ish tezroq kamayadi. "
                  "Yupqa va katta plastinalarda bikrlik hukmron."),
            ],
            derivation=[
                d("1. Normal kuchlanishlar",
                  r"\sigma_x = \frac{12M_x}{h^3}z, \quad "
                  r"\sigma_y = \frac{12M_y}{h^3}z, \quad "
                  r"\tau_{xy} = \frac{12M_{xy}}{h^3}z",
                  "pq-03 da olingan natija. Uchala kuchlanish ham "
                  "$z$ ga chiziqli va maksimal $z = \\pm h/2$ da."),
                d("2. Maksimal qiymatlar",
                  r"\sigma_x^{\max} = \frac{6M_x}{h^2}, \quad "
                  r"\tau_{xy}^{\max} = \frac{6M_{xy}}{h^2}",
                  "$z = h/2$ ni qo'yamiz. $h^2/6$ — birlik kenglikdagi "
                  "qarshilik momenti."),
                d("3. Kesuvchi kuchlanishni muvozanatdan topish",
                  r"\frac{\partial\sigma_x}{\partial x} + "
                  r"\frac{\partial\tau_{xy}}{\partial y} + "
                  r"\frac{\partial\tau_{xz}}{\partial z} = 0 "
                  r"\;\Longrightarrow\; \frac{\partial\tau_{xz}}{\partial z} "
                  r"= -\frac{12z}{h^3}Q_x",
                  "tmm-10 dagi muvozanat tenglamasi. Birinchi ikki hadni "
                  "1-qadamdan olib, $Q_x = \\partial M_x/\\partial x + "
                  "\\partial M_{xy}/\\partial y$ ni tanib olamiz."),
                d("4. Integrallash va chegaraviy shart",
                  r"\tau_{xz} = -\frac{6Q_x}{h^3}z^2 + C; \quad "
                  r"\tau_{xz}\Big(\pm\frac{h}{2}\Big) = 0 \;\Rightarrow\; "
                  r"C = \frac{3Q_x}{2h}",
                  "Yuzalar yuklanmagan, demak u yerda siljish "
                  "kuchlanishi nol. Bu shart doimiyni aniqlaydi."),
                d("5. Parabolik epyura",
                  r"\tau_{xz} = \frac{3Q_x}{2h}\Big(1 - \frac{4z^2}{h^2}\Big), "
                  r"\qquad \tau_{xz}^{\max} = \frac{3Q_x}{2h}",
                  "Maksimum o'rta sirtda — normal kuchlanish nolga teng "
                  "bo'lgan joyda. Bu to'rtburchak kesimli balkadagi "
                  "epyura bilan bir xil (mq-16)."),
                d("6. Kuchlanishlar tartibini baholash",
                  r"\frac{\tau_{xz}^{\max}}{\sigma_x^{\max}} \sim "
                  r"\frac{3Q/(2h)}{6M/h^2} \sim \frac{h}{a}",
                  "Chunki $Q \\sim M/a$. Demak $h/a = 1/20$ da "
                  "siljish kuchlanishi normal kuchlanishning 5 % i — "
                  "Kirxhoff gipotezasining asosi tasdiqlanadi."),
                d("7. Mizes kriteriysi tekis kuchlanish holatida",
                  r"\sigma_{\text{eq}} = \sqrt{\sigma_x^2 - \sigma_x\sigma_y "
                  r"+ \sigma_y^2 + 3\tau_{xy}^2} \le \sigma_Y",
                  "tmm-21 dagi umumiy formula $\\sigma_z = 0$ holida. "
                  "Maksimal $z = \\pm h/2$ da, shuning uchun faqat "
                  "yuza qatlamlar tekshiriladi."),
                d("8. Loyihalash formulalari",
                  r"h_{\sigma} = \sqrt{\frac{6M_{\max}}{[\sigma]}}, \qquad "
                  r"h_{w} = \sqrt[3]{\frac{12(1-\nu^2)\alpha q a^4}{E[w]}}",
                  "Mustahkamlik sharti $h$ ga kvadratik, bikrlik sharti "
                  "kubik bog'liq. Shuning uchun katta plastinalarda "
                  "ikkinchisi hukmron bo'ladi."),
            ],
            meaning=(
                "Uchta kuchlanish turining tartiblari nisbati "
                "$(a/h)^2 : (a/h) : 1$ — bu butun plastina nazariyasining "
                "ichki mantiqini ochib beradi. $h/a = 1/20$ da bu "
                "$400 : 20 : 1$ ni beradi: normal kuchlanish siljishdan "
                "20 marta, ko'ndalang siqilishdan esa 400 marta katta. "
                "Aynan shuning uchun Kirxhoff gipotezalari "
                "($\\gamma_{xz} = 0$, $\\sigma_z \\approx 0$) maqbul — "
                "ular eng kichik hadlarni tashlab yuboradi. "
                "Loyihalashdagi asosiy xulosa ham shu nisbatlardan "
                "kelib chiqadi. Mustahkamlik sharti $h \\propto "
                "\\sqrt{M} \\propto \\sqrt{q}a$, bikrlik sharti esa "
                "$h \\propto (qa^4)^{1/3}$ — ikkinchisi $a$ ga "
                "$a^{4/3}$ kabi, birinchisi faqat $a^1$ kabi o'sadi. "
                "Demak **plastina kattalashgan sari bikrlik tobora "
                "hukmronroq bo'ladi**. Bu tajribali muhandis biladigan, "
                "lekin boshlovchi ko'pincha unutadigan qoida: katta "
                "oraliqli perekrytiya mustahkamlik bo'yicha emas, "
                "og'ish bo'yicha loyihalanadi. Shuning uchun ularda "
                "yuqori mustahkamlikdagi po'lat ishlatishning ma'nosi "
                "yo'q — $E$ hamma po'latlarda bir xil."
            ),
            equations=[
                eq(r"\sigma_x = \frac{12M_x}{h^3}z, \qquad "
                   r"\sigma_x^{\max} = \frac{6M_x}{h^2}",
                   "Normal kuchlanish; qalinlik bo'yicha chiziqli.",
                   "Normal kuchlanish"),
                eq(r"\tau_{xz} = \frac{3Q_x}{2h}\Big(1 - \frac{4z^2}{h^2}\Big)",
                   "Kesuvchi kuchlanishning parabolik epyurasi.",
                   "Kesuvchi kuchlanish"),
                eq(r"\sigma_{\text{eq}} = \sqrt{\sigma_x^2 - \sigma_x\sigma_y "
                   r"+ \sigma_y^2 + 3\tau_{xy}^2} \le [\sigma]",
                   "Mizes mustahkamlik sharti (tekis kuchlanish holati).",
                   "Mustahkamlik sharti"),
                eq(r"w_{\max} \le \frac{a}{L}, \qquad L = 200\ldots400",
                   "Bikrlik (foydalanish) sharti.", "Bikrlik sharti"),
            ],
            conditions=(
                "**Tekshiriladigan nuqtalar:**\n"
                "- Maksimal moment nuqtasi (odatda markaz yoki "
                "mahkamlangan chekka o'rtasi) — normal kuchlanish uchun;\n"
                "- Maksimal kesuvchi kuch nuqtasi (chekka o'rtasi yoki "
                "burchak) — siljish uchun;\n"
                "- Burchaklar — buralish momenti uchun;\n"
                "- Konsentrlangan yuklama joyi — mahalliy effektlar uchun.\n\n"
                "**Tekshiriladigan qatlamlar:** $z = \\pm h/2$ (normal "
                "kuchlanish maksimal) va $z = 0$ (siljish maksimal). "
                "Yupqa plastinada $z = \\pm h/2$ hal qiluvchi.\n\n"
                "**Normativ cheklovlar** (tipik qiymatlar):\n"
                "- Perekrytiya: $w \\le a/250$;\n"
                "- Konsol: $w \\le a/150$;\n"
                "- Sirt tekisligi muhim bo'lsa (shisha, oyna): $a/500$;\n"
                "- $[\\sigma] = \\sigma_Y/n$, $n = 1{,}5\\ldots2{,}0$.\n\n"
                "**Qo'llanish chegarasi:** hisob elastik; plastik "
                "zaxira (oqish chiziqlari nazariyasi) hisobga olinmaydi."
            ),
            worked=WorkedExample(
                statement=(
                    "Po'lat perekrytiya paneli: $a = 3$ m, $b = 4$ m, "
                    "to'rt chekkasi sharnirli tayangan, "
                    "$q = 8$ kPa (foydali yuklama bilan). "
                    "$E = 200$ GPa, $\\nu = 0{,}3$, $\\sigma_Y = 235$ MPa, "
                    "$n = 1{,}5$, og'ish cheklovi $a/250$. Kerakli "
                    "qalinlikni aniqlang va qaysi mezon hukmronligini ayting."
                ),
                given=[
                    r"a = 3\ \text{m},\ b = 4\ \text{m},\ q = 8000\ \text{Pa}",
                    r"E = 200\ \text{GPa},\ \nu = 0{,}3",
                    r"\sigma_Y = 235\ \text{MPa},\ n = 1{,}5",
                    r"[w] = a/250 = 12\ \text{mm}",
                ],
                steps=[
                    st(r"[\sigma] = \frac{\sigma_Y}{n} = \frac{235}{1{,}5} "
                       r"= 156{,}7\ \text{MPa}",
                       "Ruxsat etilgan kuchlanish."),
                    st(r"b/a = 1{,}33 \;\Rightarrow\; \alpha_w = 0{,}00770, "
                       r"\ \alpha_M = 0{,}0906 \ (\text{jadvaldan})",
                       "Timoshenko jadvalidan sharnirli to'rtburchak "
                       "plastina koeffitsientlari; $w = \\alpha_w qa^4/D$, "
                       "$M_{\\max} = \\alpha_M qa^2$."),
                    st(r"M_{\max} = 0{,}0906 \cdot 8000 \cdot 9 = "
                       r"6523\ \text{N·m/m}",
                       "Markazdagi maksimal moment (qisqa yo'nalish bo'yicha)."),
                    st(r"h_\sigma = \sqrt{\frac{6M_{\max}}{[\sigma]}} = "
                       r"\sqrt{\frac{6 \cdot 6523}{156{,}7\times10^{6}}} "
                       r"= \sqrt{2{,}498\times10^{-4}} = 15{,}8\ \text{mm}",
                       "Mustahkamlik bo'yicha kerakli qalinlik."),
                    st(r"w = \frac{\alpha_w q a^4}{D} \le [w] "
                       r"\;\Rightarrow\; D \ge \frac{0{,}0077 \cdot 8000 "
                       r"\cdot 81}{0{,}012} = 4{,}158\times10^{5}\ \text{N·m}",
                       "Bikrlik shartidan kerakli bikrlik. $a^4 = 81$ m⁴."),
                    st(r"h_w = \sqrt[3]{\frac{12(1-\nu^2)D}{E}} = "
                       r"\sqrt[3]{\frac{10{,}92 \cdot 4{,}158\times10^{5}}"
                       r"{200\times10^{9}}} = \sqrt[3]{2{,}270\times10^{-5}}",
                       "$D = Eh^3/[12(1-\\nu^2)]$ dan $h$ ni ajratamiz."),
                    st(r"h_w = 2{,}835\times10^{-2}\ \text{m} = 28{,}4\ \text{mm}",
                       "Bikrlik bo'yicha kerakli qalinlik — mustahkamlikdan "
                       "**1,8 marta katta**."),
                    st(r"h = \max(15{,}8;\ 28{,}4) = 28{,}4 "
                       r"\;\Rightarrow\; h = 30\ \text{mm (standart)}",
                       "Bikrlik hukmron. $h = 30$ mm da tekshirish: "
                       "$w = 10{,}7$ mm < 12 mm ✓, "
                       "$\\sigma = 43{,}5$ MPa < 156,7 MPa ✓."),
                    st(r"\text{Zaxira: } \frac{156{,}7}{43{,}5} = 3{,}6 "
                       r"\ \text{(mustahkamlik)}, \ \frac{12}{10{,}7} = 1{,}12 "
                       r"\ \text{(bikrlik)}",
                       "Mustahkamlik bo'yicha 3,6 karra zaxira — material "
                       "'ortiqcha' ishlatilgan, lekin bu muqarrar."),
                ],
                answer=(
                    "$h_\\sigma = 15{,}8$ mm, $h_w = 28{,}4$ mm; "
                    "qabul qilinadi $h = 30$ mm. **Bikrlik hukmron** "
                    "(1,8 marta). Yakuniy holat: $w = 10{,}7$ mm, "
                    "$\\sigma = 43{,}5$ MPa, mustahkamlik zaxirasi 3,6."
                ),
                engineering_note=(
                    "Mustahkamlik bo'yicha 3,6 karra zaxira — bikrlik "
                    "hukmron bo'lgan barcha holatlarda uchraydigan "
                    "vaziyat va u 'ortiqcha material' degani. Yechim: "
                    "qalinlikni oshirish emas, **shaklni** "
                    "o'zgartirish — qovurg'a qo'shish, gofrlash yoki "
                    "sendvich panelga o'tish. Qovurg'ali plitada "
                    "bikrlik $I$ orqali oshadi, og'irlik esa deyarli "
                    "o'zgarmaydi. Shuning uchun katta oraliqli "
                    "perekrytiyalarda tekis plita deyarli "
                    "ishlatilmaydi — u iqtisodiy jihatdan samarasiz."
                ),
            ),
            computation=Computation(
                caption=(
                    "Kuchlanish maydonini hisoblash, Mizes maksimumini "
                    "topish va qalinlikni ikkala mezon bo'yicha loyihalash."
                ),
                code='''"""Plastina kuchlanish holati va mustahkamlik tekshiruvi."""
import numpy as np
from labkit import PARAMS, note, series, table, value

a = float(PARAMS.get("a", 3.0))
b = float(PARAMS.get("b", 4.0))
h = float(PARAMS.get("h", 30.0))/1000.0
E = float(PARAMS.get("E", 200.0))*1e9
nu = float(PARAMS.get("nu", 0.3))
qload = float(PARAMS.get("q", 8000.0))
sY = float(PARAMS.get("sY", 235.0))*1e6
nsaf = float(PARAMS.get("n", 1.5))
Ldef = float(PARAMS.get("Ldef", 250.0))

D = E*h**3/(12*(1 - nu**2))
s_allow = sY/nsaf
w_allow = a/Ldef
value("Silindrik bikrlik D", D/1000, "kN*m")
value("Ruxsat etilgan kuchlanish", s_allow/1e6, "MPa")
value("Ruxsat etilgan og'ish", w_allow*1000, "mm")

# --- Navye yechimi va kuchlanish maydoni ---
N = 30
ng = 61
xg = np.linspace(0.0, a, ng)
yg = np.linspace(0.0, b, ng)
X, Y = np.meshgrid(xg, yg, indexing="ij")
W = np.zeros_like(X); MX = np.zeros_like(X); MY = np.zeros_like(X)
MXY = np.zeros_like(X); QX = np.zeros_like(X); QY = np.zeros_like(X)

for m in range(1, 2*N, 2):
    for k in range(1, 2*N, 2):
        am, bk = m*np.pi/a, k*np.pi/b
        qmn = 16*qload/(np.pi**2*m*k)
        wmn = qmn/(D*(am**2 + bk**2)**2)
        S = np.sin(am*X)*np.sin(bk*Y)
        C = np.cos(am*X)*np.cos(bk*Y)
        W += wmn*S
        MX += D*wmn*(am**2 + nu*bk**2)*S
        MY += D*wmn*(bk**2 + nu*am**2)*S
        MXY += -D*wmn*(1 - nu)*am*bk*C
        QX += D*wmn*am*(am**2 + bk**2)*np.cos(am*X)*np.sin(bk*Y)
        QY += D*wmn*bk*(am**2 + bk**2)*np.sin(am*X)*np.cos(bk*Y)

w_max = float(np.max(W))
value("w_max", w_max*1000, "mm")
value("w_max / [w]", w_max/w_allow, "—")
value("a / w_max", a/w_max, "—")

# Kuchlanishlar yuza qatlamda (z = h/2)
SX = 6*MX/h**2
SY_ = 6*MY/h**2
TXY = 6*MXY/h**2
MISES = np.sqrt(SX**2 - SX*SY_ + SY_**2 + 3*TXY**2)

value("M_x max", float(np.max(MX)), "N*m/m")
value("M_y max", float(np.max(MY)), "N*m/m")
value("M_xy max (modul)", float(np.max(np.abs(MXY))), "N*m/m")
value("sigma_x max", float(np.max(SX))/1e6, "MPa")
value("sigma_y max", float(np.max(SY_))/1e6, "MPa")
value("tau_xy max (modul)", float(np.max(np.abs(TXY)))/1e6, "MPa")
mises_max = float(np.max(MISES))
value("Mizes maksimumi", mises_max/1e6, "MPa")
value("Mustahkamlik zaxirasi", s_allow/mises_max, "—")

idx = np.unravel_index(np.argmax(MISES), MISES.shape)
value("Mizes maksimumi x/a", float(xg[idx[0]]/a), "—")
value("Mizes maksimumi y/b", float(yg[idx[1]]/b), "—")

# Kesuvchi kuchlanish
Q_max = float(np.max(np.sqrt(QX**2 + QY**2)))
tau_xz_max = 1.5*Q_max/h
value("Q max", Q_max/1000, "kN/m")
value("tau_xz max (o'rta sirt)", tau_xz_max/1e6, "MPa")
value("tau_xz / sigma_max", tau_xz_max/mises_max, "—")
note(f"tau/sigma = {tau_xz_max/mises_max:.4f} ~ h/a = {h/a:.4f} — "
     f"kuchlanishlar tartibi bo'yicha baho tasdiqlandi.")

# --- Qalinlik bo'yicha epyuralar (markazda) ---
ic, jc = ng//2, ng//2
z = np.linspace(-h/2, h/2, 121)
series("sigma_x(z) markazda", (12*MX[ic, jc]/h**3*z/1e6).tolist(),
       (z*1000).tolist(), xlabel="sigma_x, MPa", ylabel="z, mm")
series("tau_xz(z) chekkada", (1.5*Q_max/h*(1 - 4*z**2/h**2)/1e6).tolist(),
       (z*1000).tolist(), xlabel="tau_xz, MPa", ylabel="z, mm")

# --- Markaziy kesim bo'ylab profillar ---
series("w(x) markaziy kesim", xg.tolist(), (W[:, jc]*1000).tolist(),
       xlabel="x, m", ylabel="Og'ish w, mm")
series("Mizes(x) markaziy kesim", xg.tolist(), (MISES[:, jc]/1e6).tolist(),
       xlabel="x, m", ylabel="Mizes, MPa")

# --- Qalinlikni loyihalash ---
M_max = float(np.max(np.maximum(MX, MY)))
h_sigma = np.sqrt(6*M_max/s_allow)
alpha_w = w_max*D/(qload*a**4)
D_need = alpha_w*qload*a**4/w_allow
h_w = (12*(1 - nu**2)*D_need/E)**(1/3)
value("Kerakli h (mustahkamlik)", h_sigma*1000, "mm")
value("Kerakli h (bikrlik)", h_w*1000, "mm")
value("Hukmron mezon nisbati h_w/h_sigma", h_w/h_sigma, "—")
crit = "BIKRLIK" if h_w > h_sigma else "MUSTAHKAMLIK"
note(f"Hukmron mezon: {crit}. Kerakli qalinlik "
     f"{max(h_sigma, h_w)*1000:.1f} mm, joriy {h*1000:.1f} mm — "
     f"{'YETARLI' if h >= max(h_sigma, h_w) else 'YETARLI EMAS'}.")

# --- Loyihalash diagrammasi: h(a) ikkala mezon bo'yicha ---
a_range = np.linspace(0.5, 10.0, 200)
hs, hw = [], []
for aa in a_range:
    Mm = 0.0906*qload*aa**2           # taxminiy koeffitsient
    hs.append(np.sqrt(6*Mm/s_allow)*1000)
    Dn = 0.0077*qload*aa**4/(aa/Ldef)
    hw.append((12*(1 - nu**2)*Dn/E)**(1/3)*1000)
series("h(a) mustahkamlik bo'yicha", a_range.tolist(), hs,
       xlabel="Plastina tomoni a, m", ylabel="Kerakli qalinlik h, mm")
series("h(a) bikrlik bo'yicha", a_range.tolist(), hw,
       xlabel="Plastina tomoni a, m", ylabel="Kerakli qalinlik h, mm")
diff = np.array(hw) - np.array(hs)
i_cross = int(np.argmax(diff > 0)) if np.any(diff > 0) else -1
if i_cross > 0:
    value("Mezonlar kesishgan a", float(a_range[i_cross]), "m")
    note(f"a < {a_range[i_cross]:.2f} m da mustahkamlik, undan katta "
         f"oraliqlarda bikrlik hukmron bo'ladi.")

table("Kuchlanish turlarining tartibi",
      ["Kuchlanish", "Tartibi", "h/a = 1/20 da nisbat", "Hisobda"],
      [["sigma_x, sigma_y", "q*(a/h)^2", 400, "asosiy"],
       ["tau_xz, tau_yz", "q*(a/h)", 20, "qalin plitada muhim"],
       ["sigma_z", "q", 1, "e'tiborsiz"]])

table("Normativ og'ish cheklovlari",
      ["Konstruksiya turi", "[w]", "a = 3 m da, mm"],
      [["Perekrytiya (umumiy)", "a/250", round(3000/250, 1)],
       ["Konsol", "a/150", round(3000/150, 1)],
       ["Tekislik muhim (shisha, oyna)", "a/500", round(3000/500, 1)],
       ["Texnologik uskuna tagida", "a/400", round(3000/400, 1)]])
''',
                parameters=[
                    p("a", "Plastina tomoni a", 0.3, 15.0, 3.0, 0.1, "m"),
                    p("b", "Plastina tomoni b", 0.3, 20.0, 4.0, 0.1, "m"),
                    p("h", "Qalinlik h", 2.0, 400.0, 30.0, 1.0, "mm"),
                    p("E", "Yung moduli E", 1.0, 400.0, 200.0, 1.0, "GPa"),
                    p("nu", "Puasson koeffitsienti ν", 0.0, 0.45, 0.3, 0.01),
                    p("q", "Yuklama q", 200.0, 100000.0, 8000.0, 100.0, "Pa"),
                    p("sY", "Oqish chegarasi σ_Y", 20.0, 1000.0, 235.0, 5.0, "MPa"),
                    p("n", "Xavfsizlik koeffitsienti n", 1.0, 3.0, 1.5, 0.05),
                    p("Ldef", "Og'ish cheklovi a/L", 100.0, 600.0, 250.0, 10.0),
                ],
                expected_output=(
                    "w_max ≈ 10,7 mm (< 12 mm ✓), σ_max ≈ 43,5 MPa, "
                    "Mizes ≈ 41 MPa, zaxira ≈ 3,8; h_σ ≈ 15,8 mm, "
                    "h_w ≈ 28,4 mm — bikrlik hukmron (1,8 marta); "
                    "τ/σ ≈ h/a ≈ 0,01."
                ),
            ),
            visual=vis(
                kind="Kuchlanish maydoni va loyihalash diagrammasi",
                tool="React/SVG + Matplotlib",
                description=(
                    "Mizes kuchlanishi konturi, qalinlik bo'yicha uch "
                    "epyura va $h(a)$ loyihalash diagrammasi."
                ),
                how_to_draw=(
                    "React/SVG: Mizes konturi — plastina rejasida "
                    "$40\\times40$ katak, har biri $\\sigma_{\\text{eq}}$ "
                    "qiymatiga qarab ketma-ket shkala bo'yicha bo'yaladi "
                    "(past — sovuq, yuqori — issiq). Ruxsat etilgan "
                    "qiymatdan oshgan kataklar alohida qora kontur "
                    "bilan ajratiladi, shunda xavfli zona darhol "
                    "ko'rinadi. Yonida rang shkalasi va joriy "
                    "maksimum belgilangan. Qalinlik epyuralari paneli: "
                    "uchta grafik yonma-yon — $\\sigma_x(z)$ chiziqli, "
                    "$\\tau_{xz}(z)$ parabolik, $\\sigma_{\\text{eq}}(z)$; "
                    "ular bir xil $z$ o'qini baham ko'radi, shunda "
                    "maksimumlar turli qatlamda ekanligi aniq ko'rinadi. "
                    "Loyihalash diagrammasi log–log o'qlarda: "
                    "$h_\\sigma(a)$ qiyaligi 1, $h_w(a)$ qiyaligi 4/3 — "
                    "ular bir nuqtada kesishadi va kesishgandan keyin "
                    "bikrlik hukmron bo'ladigan soha shtrixlanadi; "
                    "joriy loyiha nuqtasi belgi bilan qo'yiladi."
                ),
            ),
            interp=(
                "Loyihalash diagrammasidagi kesishish nuqtasi eng "
                "amaliy natija: undan kichik oraliqlarda mustahkamlik, "
                "kattalarida bikrlik hukmron. Chiziqlarning turli "
                "qiyaligi ($1$ va $4/3$) bu almashuvni muqarrar qiladi — "
                "yetarlicha katta plastina har doim bikrlik bo'yicha "
                "loyihalanadi. Amaliy oqibati muhim: katta oraliqli "
                "perekrytiyada yuqori mustahkamlikdagi po'lat "
                "($\\sigma_Y = 450$ MPa) oddiy po'latdan ($235$ MPa) "
                "hech qanday ustunlik bermaydi, chunki $E$ ikkalasida "
                "ham 200 GPa. Bu ko'p uchraydigan qimmat xato. "
                "Kuchlanishlar tartibi jadvali esa nazariyaning o'zini "
                "tasdiqlaydi: sonli hisob $\\tau/\\sigma \\approx h/a$ "
                "bahosini aniq beradi, ya'ni yupqa plastinada siljish "
                "kuchlanishi 1 % darajasida — Kirxhoff gipotezasini "
                "e'tiborsiz qoldirishga to'liq asos bor. Mizes "
                "maksimumining joylashuvi ham ma'noli: u markazda "
                "emas, markazdan qisqa tomon yo'nalishi bo'ylab "
                "biroz siljigan joyda bo'lishi mumkin, chunki "
                "$M_x$ va $M_y$ maksimumlari mos kelmaydi."
            ),
            mistakes=[
                "Kuchlanishni $M/W$ da $W = h^3/12$ deb hisoblash. "
                "Qarshilik momenti $W = h^2/6$; $h^3/12$ — inersiya momenti.",
                "Mizes kuchlanishini o'rta sirtda tekshirish. U yerda "
                "normal kuchlanish nol; tekshiruv $z = \\pm h/2$ da bajariladi.",
                "Faqat mustahkamlikni tekshirib, og'ishni unutish. "
                "Katta plastinalarda bikrlik 2–3 marta qalinroq "
                "plastinani talab qiladi.",
                "Yuqori mustahkamlikdagi po'lat bikrlikni ham oshiradi "
                "deb o'ylash. $E$ barcha po'latlarda deyarli bir xil "
                "(200–210 GPa); $\\sigma_Y$ faqat mustahkamlikka ta'sir qiladi.",
            ],
            quiz=[
                q("Kesuvchi kuchlanish epyurasi qanday shaklda va "
                  "maksimumi qayerda?",
                  "Parabolik, maksimumi o'rta sirtda "
                  "($\\tau_{\\max} = 3Q/(2h)$), yuzalarda nol — chunki "
                  "u yerda tashqi yuk yo'q.", "konseptual"),
                q("Kuchlanishlarning tartibi nisbatini ayting.",
                  "$\\sigma : \\tau_{xz} : \\sigma_z = (a/h)^2 : (a/h) : 1$. "
                  "$h/a = 1/20$ da bu $400 : 20 : 1$.", "konseptual"),
                q("$M = 5000$ N·m/m, $h = 25$ mm. $\\sigma_{\\max}$ ni toping.",
                  "$\\sigma = 6 \\cdot 5000/0{,}025^2 = 30\\,000/"
                  "6{,}25\\times10^{-4} = 48$ MPa.", "hisob"),
                q("Nima uchun katta plastinalarda bikrlik hukmron bo'ladi?",
                  "$h_\\sigma \\propto a$, $h_w \\propto a^{4/3}$ — "
                  "ikkinchisi tezroq o'sadi, shuning uchun yetarlicha "
                  "katta $a$ da u ustun keladi.", "talqin"),
                q("Kodda $\\tau/\\sigma \\approx h/a$ tekshiruvi nimani "
                  "tasdiqlaydi?",
                  "Kuchlanishlar tartibi bo'yicha nazariy bahoni va "
                  "shu orqali Kirxhoff gipotezasining asosliligini: "
                  "siljish kuchlanishi normal kuchlanishdan $a/h$ "
                  "marta kichik.", "kod"),
                q("Bikrlik hukmron bo'lganda qalinlikni oshirishdan "
                  "boshqa qanday yechim bor?",
                  "Shaklni o'zgartirish: qovurg'a qo'shish, gofrlash "
                  "yoki sendvich panelga o'tish. Ular bikrlikni "
                  "og'irlikni oshirmasdan keskin ko'taradi.", "talqin"),
            ],
            bridge=(
                "Birinchi modul yakunlandi: model, kinematika, "
                "konstitutiv munosabatlar, tenglama, chegaraviy "
                "shartlar va mustahkamlik tekshiruvi. Keyingi modulda "
                "asosiy savolga o'tamiz — bu tenglamani qanday "
                "yechamiz? Navye qator yechimidan boshlaymiz."
            ),
            research=(
                "Plastinalarning chegaraviy (limit) tahlilini "
                "o'rganing: oqish chiziqlari nazariyasi (yield line "
                "theory, Johansen). Elastik hisob birinchi oqish "
                "boshlanishini beradi, lekin plastina hali "
                "buzilmaydi — plastik qayta taqsimlanish hisobiga "
                "u ancha katta yukni ko'taradi. Kvadrat plastina "
                "uchun oqish chiziqlari mexanizmini quring va "
                "chegaraviy yuklamani elastik hisob bilan taqqoslang. "
                "Nisbat qancha chiqadi va bu temir-beton normativlarida "
                "qanday hisobga olinadi?"
            ),
        ),
    ),
]
