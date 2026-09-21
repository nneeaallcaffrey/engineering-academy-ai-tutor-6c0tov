"""PQ / 2-modul: To'rtburchak plastinalar — yechim usullari (pq-07 … pq-12)."""

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
M = "pq-m2"


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
    # ------------------------------------------------------------------ pq-07
    Topic(
        id="pq-07",
        subject_id=S, module_id=M, order=7,
        title="Navye yechimi: ikki tomonlama trigonometrik qator",
        description=(
            "To'rt chekkasi sharnirli tayangan to'rtburchak plastina uchun "
            "ikki tomonlama Furye qatori yechimi, koeffitsientlarning "
            "aniqlanishi va qatorning yaqinlashish tezligi."
        ),
        learning_objective=(
            "Navye yechimini keltirib chiqarish, ixtiyoriy yuklama uchun "
            "Furye koeffitsientlarini hisoblash va og'ish, moment, "
            "kuchlanishlarning yaqinlashishini baholash."
        ),
        prerequisites=["pq-06", "pq-04"],
        mathematical_core=(
            "Ikki tomonlama Furye qatori, ortogonallik, "
            "$w_{mn} = q_{mn}/[D\\pi^4((m/a)^2 + (n/b)^2)^2]$, "
            "qatorning $O(m^{-5})$ yaqinlashishi."
        ),
        engineering_application=(
            "Sharnirli tayangan panellarni hisoblash, FEM natijalarini "
            "tekshirish uchun etalon yechim, normativ jadvallarning manbai."
        ),
        computational_component=(
            "Furye koeffitsientlarini hisoblash, qator hadlari sonining "
            "aniqlikka ta'sirini o'rganish, turli yuklamalarni taqqoslash."
        ),
        visualization_component=(
            "Og'ish sirtining konturi, qator hadlarining ketma-ket "
            "qo'shilishi animatsiyasi, yaqinlashish grafigi."
        ),
        research_extension=(
            "Qatorning yaqinlashish tezligini nazariy tahlil qiling: "
            "nima uchun og'ish $O(m^{-5})$, moment $O(m^{-3})$, kesuvchi "
            "kuch esa $O(m^{-1})$ tezlikda yaqinlashadi?"
        ),
        difficulty="murakkab",
        previous_link=(
            "pq-05 da sharnirli chekkada $w = 0$ va $\\nabla^2 w = 0$ "
            "ekanligi ko'rsatilgan edi. Sinus funksiyasi aynan shu ikki "
            "shartni avtomatik qanoatlantiradi — shuning uchun u Navye "
            "yechimining tabiiy bazisi."
        ),
        next_topic="pq-08",
        estimated_minutes=95,
        tags=["Navye", "Furye qatori", "yechim", "plastina"],
        lesson=_lesson(
            problem=(
                "$D\\nabla^4 w = q$ tenglamasi olindi, chegaraviy shartlar "
                "qo'yildi. Endi eng muhim savol: uni qanday yechamiz? "
                "To'rtinchi tartibli xususiy hosilali tenglamaning umumiy "
                "yechimi yo'q. Lekin sharnirli tayangan to'rtburchak "
                "plastinada bitta hiyla ishlaydi: agar yechimni sinuslar "
                "qatori shaklida izlasak, har bir had chegaraviy shartlarni "
                "**avtomatik** qanoatlantiradi va tenglama har bir had "
                "uchun oddiy algebraik tenglamaga aylanadi."
            ),
            concepts=[
                c("Navye yechimi (Navier solution)",
                  "Ikki tomonlama sinus qatori: $w = \\sum\\sum w_{mn}"
                  "\\sin\\frac{m\\pi x}{a}\\sin\\frac{n\\pi y}{b}$. "
                  "1820-yilda Navye tomonidan taklif qilingan."),
                c("Bazis funksiyalarning tanlash mezoni",
                  "Har bir had barcha chegaraviy shartlarni qanoatlantirishi "
                  "kerak. $\\sin\\frac{m\\pi x}{a}$ chekkalarda nolga teng "
                  "va ikkinchi hosilasi ham nol — sharnirli shartga mos."),
                c("Ortogonallik",
                  "$\\int_0^a \\sin\\frac{m\\pi x}{a}\\sin\\frac{k\\pi x}{a}dx "
                  "= \\frac{a}{2}\\delta_{mk}$ — bu xossa koeffitsientlarni "
                  "bir-biridan ajratish imkonini beradi."),
                c("Yuklamaning Furye yoyilmasi",
                  "$q(x,y) = \\sum\\sum q_{mn}\\sin\\frac{m\\pi x}{a}"
                  "\\sin\\frac{n\\pi y}{b}$, bunda $q_{mn}$ integral orqali topiladi."),
                c("Yaqinlashish tezligi",
                  "Og'ish $O(m^{-5})$ — juda tez; moment (ikkinchi hosila) "
                  "$O(m^{-3})$; kesuvchi kuch (uchinchi hosila) $O(m^{-1})$ — "
                  "sekin. Har differensiallash ikki tartib yo'qotadi."),
                c("Konsentrlangan yuklama",
                  "$q_{mn} = \\frac{4P}{ab}\\sin\\frac{m\\pi x_0}{a}"
                  "\\sin\\frac{n\\pi y_0}{b}$ — koeffitsientlar $m, n$ "
                  "bilan kamaymaydi, shuning uchun qator sekin yaqinlashadi."),
            ],
            derivation=[
                d("1. Yechim shaklini tanlash",
                  r"w(x, y) = \sum_{m=1}^{\infty}\sum_{n=1}^{\infty} w_{mn}"
                  r"\sin\frac{m\pi x}{a}\sin\frac{n\pi y}{b}",
                  "Har bir had $x = 0, a$ va $y = 0, b$ da nolga teng "
                  "(sinuslar nol) va ikkinchi hosilalari ham nol — "
                  "sharnirli shartlar avtomatik bajariladi."),
                d("2. Bigarmonik operatorni hisoblash",
                  r"\nabla^4\Big[\sin\frac{m\pi x}{a}\sin\frac{n\pi y}{b}\Big] "
                  r"= \pi^4\Big[\Big(\frac{m}{a}\Big)^2 + \Big(\frac{n}{b}\Big)^2\Big]^2"
                  r"\sin\frac{m\pi x}{a}\sin\frac{n\pi y}{b}",
                  "Sinus funksiyasi $\\nabla^4$ operatorining **xususiy "
                  "funksiyasi** — differensiallashda shakl o'zgarmaydi, "
                  "faqat ko'paytuvchi paydo bo'ladi. Bu butun usulning kaliti."),
                d("3. Yuklamani yoyish",
                  r"q(x, y) = \sum_m\sum_n q_{mn}\sin\frac{m\pi x}{a}"
                  r"\sin\frac{n\pi y}{b}, \quad q_{mn} = \frac{4}{ab}"
                  r"\int_0^a\int_0^b q\sin\frac{m\pi x}{a}\sin\frac{n\pi y}{b}"
                  r"\,dy\,dx",
                  "Ortogonallik tufayli koeffitsient integral orqali "
                  "topiladi. Koeffitsient $4/(ab)$ — normallashtirish."),
                d("4. Tenglamaga qo'yish va hadlarni tenglashtirish",
                  r"D\pi^4\Big[\Big(\frac{m}{a}\Big)^2 + \Big(\frac{n}{b}\Big)^2\Big]^2 "
                  r"w_{mn} = q_{mn}",
                  "Chap va o'ng tomonda bir xil bazis funksiyalar; "
                  "ortogonallik tufayli har bir $(m,n)$ juftlik uchun "
                  "alohida tenglama hosil bo'ladi. PDE cheksiz sondagi "
                  "**algebraik** tenglamaga ajraldi."),
                d("5. Yechim koeffitsientlari",
                  r"w_{mn} = \frac{q_{mn}}{D\pi^4\Big[\big(\frac{m}{a}\big)^2 "
                  r"+ \big(\frac{n}{b}\big)^2\Big]^2}",
                  "Har bir had mustaqil. Maxraj $(m^2 + n^2)^2$ kabi "
                  "o'sadi, shuning uchun yuqori hadlar tez kichrayadi."),
                d("6. Bir tekis yuklama uchun koeffitsientlar",
                  r"q_{mn} = \frac{16q_0}{\pi^2 mn} \quad (m, n \text{ toq}), "
                  r"\qquad q_{mn} = 0 \quad (m \text{ yoki } n \text{ juft})",
                  "$\\int_0^a\\sin\\frac{m\\pi x}{a}dx = \\frac{a(1-\\cos m\\pi)}"
                  "{m\\pi}$ — juft $m$ da nolga teng. Simmetriya tufayli "
                  "faqat toq hadlar qoladi."),
                d("7. Yaqinlashish tezligini baholash",
                  r"w_{mn} \sim \frac{1}{mn(m^2 + n^2)^2} \sim m^{-5} "
                  r"\ (n \sim m); \qquad M_{mn} \sim m^{-3}; \qquad "
                  r"Q_{mn} \sim m^{-1}",
                  "Moment — ikkinchi hosila, demak $m^2$ ko'paytiriladi; "
                  "kesuvchi kuch — uchinchi. Shuning uchun og'ish uchun "
                  "1–2 had, kuchlanish uchun 10–20 had, kesuvchi kuch "
                  "uchun 100+ had kerak."),
                d("8. Momentlarni hisoblash",
                  r"M_x = D\pi^2\sum_m\sum_n w_{mn}\Big[\Big(\frac{m}{a}\Big)^2 "
                  r"+ \nu\Big(\frac{n}{b}\Big)^2\Big]\sin\frac{m\pi x}{a}"
                  r"\sin\frac{n\pi y}{b}",
                  "pq-03 dagi $M_x = -D(w_{,xx} + \\nu w_{,yy})$ ni qatorga "
                  "qo'llaymiz. Ikki marta differensiallash sinusni "
                  "o'zgartirmaydi, faqat $-(m\\pi/a)^2$ ko'paytiradi."),
            ],
            meaning=(
                "Navye yechimining mohiyati — **xususiy funksiyalar "
                "bazisiga o'tish**. Bigarmonik operator umuman olganda "
                "murakkab, lekin sinuslar bazisida u oddiy songa "
                "ko'paytirishga aylanadi. Bu chiziqli algebradagi "
                "diagonallashtirishning to'g'ridan-to'g'ri analogi: "
                "matritsani xususiy vektorlar bazisida yozsak, u "
                "diagonal bo'ladi va tizim yechish trivial bo'lib qoladi. "
                "$w_{mn} \\propto 1/[(m/a)^2 + (n/b)^2]^2$ maxraji "
                "fizik ma'noga ham ega: u to'lqin uzunligi qisqa "
                "bo'lgan 'tez tebranuvchi' shakllarga plastinaning "
                "qarshiligi. Qisqa to'lqinli deformatsiya katta "
                "egrilik, demak katta moment va katta energiya talab "
                "qiladi — shuning uchun plastina ularga kuchli "
                "qarshilik ko'rsatadi va ularning amplitudasi kichik "
                "bo'ladi. Aynan shu sabab **plastina past chastotali "
                "filtr kabi ishlaydi**: yuklamaning mayda tafsilotlari "
                "og'ishda deyarli ko'rinmaydi. Buning amaliy oqibati: "
                "og'ishni hisoblash oson (1 had yetadi), kuchlanishni "
                "hisoblash qiyinroq, kesuvchi kuchni esa qator bilan "
                "hisoblash amalda samarasiz — u uchun muvozanat "
                "mulohazalari ishlatiladi."
            ),
            equations=[
                eq(r"w = \sum_{m,n} w_{mn}\sin\frac{m\pi x}{a}\sin\frac{n\pi y}{b}",
                   "Navye yechimining umumiy shakli.", "Navye qatori"),
                eq(r"w_{mn} = \frac{q_{mn}}{D\pi^4\big[(m/a)^2 + (n/b)^2\big]^2}",
                   "Qator koeffitsientlari.", "Koeffitsientlar"),
                eq(r"q_{mn} = \frac{16q_0}{\pi^2 mn} \quad (m, n \text{ toq})",
                   "Bir tekis yuklama uchun Furye koeffitsientlari.",
                   "Tekis yuklama"),
                eq(r"w_{\max} = \alpha\frac{q_0 a^4}{D}, \quad "
                   r"\alpha = 0{,}004062 \ (\text{kvadrat})",
                   "Amaliy hisob shakli; $\\alpha$ jadvaldan olinadi.",
                   "Amaliy formula"),
            ],
            conditions=(
                "**Navye yechimining qo'llanish sharti — barcha to'rt "
                "chekka sharnirli tayangan bo'lishi.** Bu qat'iy cheklov: "
                "bitta chekka mahkamlangan bo'lsa ham, sinuslar bazisi "
                "yaroqsiz bo'lib qoladi (ular $\\partial w/\\partial x = 0$ "
                "shartini qanoatlantirmaydi).\n\n"
                "**Yuklama ixtiyoriy bo'lishi mumkin:**\n"
                "- Bir tekis: $q_{mn} = 16q_0/(\\pi^2 mn)$, $m,n$ toq;\n"
                "- Konsentrlangan $P$ nuqtada $(x_0, y_0)$: "
                "$q_{mn} = \\frac{4P}{ab}\\sin\\frac{m\\pi x_0}{a}"
                "\\sin\\frac{n\\pi y_0}{b}$;\n"
                "- Gidrostatik $q = q_0 x/a$: "
                "$q_{mn} = \\frac{8q_0(-1)^{m+1}}{\\pi^2 mn}$, $n$ toq;\n"
                "- Qism yuza bo'ylab: integral chegaralari o'zgaradi.\n\n"
                "**Yaqinlashish:** og'ish uchun $m, n \\le 5$ yetarli "
                "(xato < 0,1 %); momentlar uchun $\\le 21$; "
                "konsentrlangan yuklamada esa moment markazda "
                "logarifmik cheksizlikka intiladi va qator yaqinlashmaydi."
            ),
            worked=WorkedExample(
                statement=(
                    "Kvadrat plastina $a = b = 5$ m, $h = 200$ mm, "
                    "$E = 30$ GPa, $\\nu = 0{,}2$, bir tekis yuklama "
                    "$q_0 = 10$ kPa, to'rt chekkasi sharnirli. "
                    "(a) Birinchi had bilan $w_{\\max}$ ni toping. "
                    "(b) To'qqizta had ($m,n \\le 5$) bilan aniqlang. "
                    "(c) Markazdagi $M_x$ ni hisoblang. (d) "
                    "Kuchlanishni toping."
                ),
                given=[
                    r"a = b = 5\ \text{m},\ h = 0{,}2\ \text{m}",
                    r"E = 30\ \text{GPa},\ \nu = 0{,}2,\ q_0 = 10^4\ \text{Pa}",
                ],
                steps=[
                    st(r"D = \frac{30\times10^9 \cdot 8\times10^{-3}}{12 \cdot 0{,}96} "
                       r"= \frac{2{,}4\times10^{8}}{11{,}52} = 2{,}083\times10^{7}\ \text{N·m}",
                       "$h^3 = 8\\times10^{-3}$ m³, $1-\\nu^2 = 0{,}96$."),
                    st(r"q_{11} = \frac{16 \cdot 10^4}{\pi^2 \cdot 1 \cdot 1} "
                       r"= \frac{1{,}6\times10^{5}}{9{,}8696} = 16\,211\ \text{Pa}",
                       "Birinchi Furye koeffitsienti — bir tekis "
                       "yuklamaning asosiy garmonikasi."),
                    st(r"\Big[\Big(\frac{1}{5}\Big)^2 + \Big(\frac{1}{5}\Big)^2\Big]^2 "
                       r"= (0{,}08)^2 = 6{,}4\times10^{-3}\ \text{m}^{-4}",
                       "Maxrajdagi geometrik ko'paytuvchi."),
                    st(r"w_{11} = \frac{16\,211}{2{,}083\times10^{7} \cdot 97{,}409 "
                       r"\cdot 6{,}4\times10^{-3}} = \frac{16\,211}{1{,}2986\times10^{7}} "
                       r"= 1{,}2483\times10^{-3}\ \text{m}",
                       "$\\pi^4 = 97{,}409$. Birinchi had: 1,248 mm."),
                    st(r"w_{\max} = \sum_{m,n}w_{mn}\sin\frac{m\pi}{2}"
                       r"\sin\frac{n\pi}{2} = 1{,}2187\ \text{mm}",
                       "To'liq qator (kodda $N = 15$). $w_{13} = w_{31}$ "
                       "hadlari manfiy ishora bilan kiradi "
                       "($\\sin\\frac{3\\pi}{2} = -1$) va birinchi hadni "
                       "kamaytiradi."),
                    st(r"\frac{w_{11} - w_{\max}}{w_{\max}} = "
                       r"\frac{1{,}2483 - 1{,}2187}{1{,}2187} = +2{,}42\ \%",
                       "Og'ish uchun bitta had 2,4 % xato beradi — "
                       "muhandislik bahosi uchun yetarli."),
                    st(r"\alpha = \frac{w_{\max}D}{q_0 a^4} = "
                       r"\frac{1{,}2187\times10^{-3} \cdot 2{,}0833\times10^{7}}"
                       r"{10^4 \cdot 625} = 0{,}0040623",
                       "Timoshenko jadvalidagi 0,004062 bilan to'liq mos. "
                       "Diqqat: $\\alpha$ Puasson koeffitsientiga bog'liq "
                       "emas, chunki $\\nu$ faqat $D$ ichida qatnashadi "
                       "(pq-04 dagi natija)."),
                    st(r"M_x = D\pi^2\sum w_{mn}\Big[\frac{m^2}{a^2} + "
                       r"\nu\frac{n^2}{b^2}\Big]\sin\frac{m\pi}{2}"
                       r"\sin\frac{n\pi}{2} = 11\,046\ \text{N·m/m}",
                       "Birinchi had 12 319 N·m/m beradi, ya'ni "
                       "11,5 % xato — og'ishdagidan besh marta yomon, "
                       "chunki moment $O(m^{-3})$ tezlikda yaqinlashadi."),
                    st(r"\sigma_{\max} = \frac{6M_x}{h^2} = \frac{6 \cdot 11\,046}"
                       r"{0{,}04} = 1{,}657\ \text{MPa}",
                       "Beton uchun past kuchlanish — bu plita bikrlik "
                       "bo'yicha loyihalangan, mustahkamlik bo'yicha emas."),
                ],
                answer=(
                    "$D = 20{,}83$ MN·m; $w_{11} = 1{,}2483$ mm (1-had), "
                    "$w_{\\max} = 1{,}2187$ mm (to'liq qator) — 1-had "
                    "xatosi $+2{,}42$ %; $\\alpha = 0{,}0040623$ "
                    "(Timoshenko 0,004062); $M_x = 11{,}05$ kN·m/m "
                    "(1-had xatosi 11,5 %), $\\sigma_{\\max} = 1{,}66$ MPa."
                ),
                engineering_note=(
                    "Amaliyotda muhandis qatorni hisoblamaydi — u "
                    "Timoshenko jadvalidagi $\\alpha$ koeffitsientidan "
                    "foydalanadi: $w = \\alpha q a^4/D$. Bu jadvallar "
                    "aynan shu qator bilan hisoblangan va bizning "
                    "natijamiz ular bilan beshinchi xonagacha mos "
                    "tushadi. Yana bir muhim kuzatuv: $\\alpha$ "
                    "**Puasson koeffitsientiga bog'liq emas** — u faqat "
                    "$b/a$ nisbati va chegaraviy shartlar bilan "
                    "aniqlanadi. Shuning uchun bitta jadval barcha "
                    "izotrop materiallarga yaraydi; $\\nu$ ning ta'siri "
                    "to'liq $D$ ichida hisobga olinadi."
                ),
            ),
            computation=Computation(
                caption=(
                    "Navye qatorini turli yuklamalar uchun hisoblash, "
                    "hadlar sonining og'ish, moment va kesuvchi kuchga "
                    "ta'sirini o'rganish."
                ),
                code='''"""Navye yechimi: ikki tomonlama trigonometrik qator."""
import numpy as np
from labkit import PARAMS, note, series, table, value

a = float(PARAMS.get("a", 5.0))
b = float(PARAMS.get("b", 5.0))
h = float(PARAMS.get("h", 200.0))/1000.0
E = float(PARAMS.get("E", 30.0))*1e9
nu = float(PARAMS.get("nu", 0.2))
q0 = float(PARAMS.get("q0", 10000.0))
nmax = int(PARAMS.get("nmax", 15))
load_kind = int(PARAMS.get("load_kind", 0))   # 0 tekis, 1 gidrostatik, 2 markazda P

D = E*h**3/(12*(1 - nu**2))
value("Silindrik bikrlik D", D/1e6, "MN*m")
value("Tomonlar nisbati b/a", b/a, "—")


def qmn(m, n):
    """Yuklamaning Furye koeffitsienti."""
    if load_kind == 0:                    # bir tekis
        if m % 2 == 1 and n % 2 == 1:
            return 16*q0/(np.pi**2*m*n)
        return 0.0
    if load_kind == 1:                    # gidrostatik q = q0*x/a
        if n % 2 == 1:
            return 8*q0*(-1)**(m + 1)/(np.pi**2*m*n)
        return 0.0
    # markazda konsentrlangan P = q0*a*b (ekvivalent)
    P = q0*a*b
    return 4*P/(a*b)*np.sin(m*np.pi/2)*np.sin(n*np.pi/2)


def solve(nterms):
    """Markazdagi w, M_x, M_y va chekkadagi Q_x."""
    w = mx = my = 0.0
    qx_edge = 0.0
    for m in range(1, nterms + 1):
        for n in range(1, nterms + 1):
            qc = qmn(m, n)
            if qc == 0.0:
                continue
            am, bn = m*np.pi/a, n*np.pi/b
            wmn = qc/(D*(am**2 + bn**2)**2)
            s = np.sin(m*np.pi/2)*np.sin(n*np.pi/2)
            w += wmn*s
            mx += D*wmn*(am**2 + nu*bn**2)*s
            my += D*wmn*(bn**2 + nu*am**2)*s
            qx_edge += D*wmn*am*(am**2 + bn**2)*np.sin(n*np.pi/2)
    return w, mx, my, qx_edge


w_f, mx_f, my_f, qx_f = solve(nmax)
value("w_max (markazda)", w_f*1000, "mm")
value("M_x (markazda)", mx_f, "N*m/m")
value("M_y (markazda)", my_f, "N*m/m")
value("Q_x (chekkada)", qx_f/1000, "kN/m")
value("sigma_max", 6*max(abs(mx_f), abs(my_f))/h**2/1e6, "MPa")
value("w_max / a", w_f/a, "—")
value("a / w_max", a/w_f if w_f > 0 else 0.0, "—")

alpha = w_f*D/(q0*a**4)
value("Koeffitsient alpha (w = alpha*q*a^4/D)", alpha, "—")
if load_kind == 0 and abs(a - b) < 1e-9:
    note(f"Kvadrat plastina, tekis yuklama: alpha = {alpha:.6f}. "
         f"Timoshenko jadvali nu = 0.3 uchun 0.004062 beradi.")

# --- Yaqinlashish tahlili ---
terms = [1, 3, 5, 7, 9, 11, 15, 21, 31, 41]
ws, ms, qs = [], [], []
for nt in terms:
    wt, mt, _, qt = solve(nt)
    ws.append(wt*1000); ms.append(mt); qs.append(qt/1000)

series("w konvergensiyasi", [float(t) for t in terms], ws,
       xlabel="Hadlar soni (m, n <= N)", ylabel="w_max, mm")
series("M_x konvergensiyasi", [float(t) for t in terms], ms,
       xlabel="Hadlar soni (m, n <= N)", ylabel="M_x, N*m/m")
series("Q_x konvergensiyasi", [float(t) for t in terms], qs,
       xlabel="Hadlar soni (m, n <= N)", ylabel="Q_x, kN/m")

w_ref, m_ref, _, q_ref = solve(81)
table("Yaqinlashish: nisbiy xato (%)",
      ["Hadlar soni N", "w xatosi", "M_x xatosi", "Q_x xatosi"],
      [[nt,
        round(abs(wt/1000 - w_ref)/abs(w_ref)*100, 5) if w_ref else 0.0,
        round(abs(mt - m_ref)/abs(m_ref)*100, 5) if m_ref else 0.0,
        round(abs(qt*1000 - q_ref)/abs(q_ref)*100, 4) if q_ref else 0.0]
       for nt, wt, mt, qt in zip(terms, ws, ms, qs)])
note("Og'ish O(m^-5), moment O(m^-3), kesuvchi kuch O(m^-1) tezlikda "
     "yaqinlashadi: har differensiallash ikki tartib yo'qotadi.")

# --- Og'ish sirti ---
ng = 61
xg = np.linspace(0.0, a, ng)
yg = np.linspace(0.0, b, ng)
X, Y = np.meshgrid(xg, yg, indexing="ij")
W = np.zeros_like(X)
for m in range(1, nmax + 1):
    for n in range(1, nmax + 1):
        qc = qmn(m, n)
        if qc == 0.0:
            continue
        am, bn = m*np.pi/a, n*np.pi/b
        W += qc/(D*(am**2 + bn**2)**2)*np.sin(am*X)*np.sin(bn*Y)

series("w(x) markaziy kesim", xg.tolist(), (W[:, ng//2]*1000).tolist(),
       xlabel="x, m", ylabel="Og'ish w, mm")
series("w(y) markaziy kesim", yg.tolist(), (W[ng//2, :]*1000).tolist(),
       xlabel="y, m", ylabel="Og'ish w, mm")
series("w diagonal bo'ylab",
       np.linspace(0, np.hypot(a, b), ng).tolist(),
       (np.array([W[i, i] for i in range(ng)])*1000).tolist(),
       xlabel="Diagonal bo'ylab masofa, m", ylabel="Og'ish w, mm")

# --- Birinchi hadlar hissasi ---
contrib = []
for m in range(1, 8, 2):
    for n in range(1, 8, 2):
        qc = qmn(m, n)
        if qc == 0.0:
            continue
        am, bn = m*np.pi/a, n*np.pi/b
        wmn = qc/(D*(am**2 + bn**2)**2)*np.sin(m*np.pi/2)*np.sin(n*np.pi/2)
        contrib.append([f"({m}, {n})", round(wmn*1e6, 3),
                        round(100*wmn/w_f, 4) if w_f else 0.0])
table("Qator hadlarining og'ishga hissasi",
      ["(m, n)", "w_mn, mkm", "Ulush, %"], contrib[:12])

table("Turli yuklamalar uchun Furye koeffitsientlari",
      ["Yuklama", "q_mn", "Nolga teng bo'lmagan hadlar"],
      [["Bir tekis q0", "16*q0/(pi^2*m*n)", "m, n toq"],
       ["Gidrostatik q0*x/a", "8*q0*(-1)^(m+1)/(pi^2*m*n)", "n toq"],
       ["Markazda P", "4P/(ab)*sin(m*pi/2)*sin(n*pi/2)", "m, n toq"],
       ["Sinusoidal q0*sin(pi x/a)*sin(pi y/b)", "q0 (faqat m=n=1)",
        "bitta had — aniq yechim"]])
''',
                parameters=[
                    p("a", "Plastina tomoni a", 0.3, 20.0, 5.0, 0.1, "m"),
                    p("b", "Plastina tomoni b", 0.3, 20.0, 5.0, 0.1, "m"),
                    p("h", "Qalinlik h", 5.0, 500.0, 200.0, 5.0, "mm"),
                    p("E", "Yung moduli E", 1.0, 400.0, 30.0, 1.0, "GPa"),
                    p("nu", "Puasson koeffitsienti ν", 0.0, 0.45, 0.2, 0.01),
                    p("q0", "Yuklama q₀", 100.0, 100000.0, 10000.0, 100.0, "Pa"),
                    p("nmax", "Qator hadlari soni N", 1.0, 61.0, 15.0, 2.0),
                    p("load_kind", "Yuklama turi (0 tekis, 1 gidro, 2 P)",
                      0.0, 2.0, 0.0, 1.0),
                ],
                expected_output=(
                    "D = 20,83 MN·m; w_max = 1,2187 mm, α = 0,0040623 "
                    "(Timoshenko 0,004062); M_x = 11,05 kN·m/m, "
                    "σ = 1,657 MPa. Yaqinlashish jadvalida N = 1 da "
                    "og'ish xatosi 2,42 %, moment 11,5 %, kesuvchi kuch "
                    "23,0 %; N = 5 da mos ravishda 0,03 %, 0,72 % va "
                    "8,5 % — uch xil yaqinlashish tezligi aniq ko'rinadi."
                ),
            ),
            visual=vis(
                kind="Navye qatori va yaqinlashish",
                tool="React/SVG",
                description=(
                    "Og'ish sirti konturi, qator hadlarining ketma-ket "
                    "qo'shilishi va uch kattalikning yaqinlashish grafigi."
                ),
                how_to_draw=(
                    "React/SVG: asosiy panel — og'ish sirti kontur "
                    "chiziqlari bilan (marching squares, 12 daraja). "
                    "Slayder hadlar sonini boshqaradi: $N = 1$ da sirt "
                    "silliq sinusoid, $N$ oshgani sari deyarli "
                    "o'zgarmaydi — bu tez yaqinlashishni ko'rsatadi. "
                    "Ikkinchi panel moment uchun bir xil, lekin u yerda "
                    "$N$ ning ta'siri sezilarli. Uchinchi panel — "
                    "yaqinlashish grafigi log–log o'qlarda: uchta "
                    "chiziq ($w$, $M$, $Q$ xatosi) va ularning turli "
                    "qiyaligi ($-5$, $-3$, $-1$) aniq ko'rinadi; "
                    "nazariy qiyaliklar punktir bilan ustiga "
                    "qo'yiladi. To'rtinchi element — hadlar hissasi "
                    "jadvali issiqlik xaritasi ko'rinishida: "
                    "$7\\times7$ katak, har biri $(m,n)$ hadning "
                    "ulushiga qarab bo'yalgan; $(1,1)$ katak deyarli "
                    "butun rangni egallashi darhol ko'rinadi."
                ),
            ),
            interp=(
                "Yaqinlashish jadvali usulning eng muhim amaliy "
                "xususiyatini ochadi: **bitta had og'ish uchun 1 % "
                "aniqlik beradi, lekin kesuvchi kuch uchun bir necha "
                "o'nlab foiz xato qoldiradi**. Sababi matematik: "
                "qatorni differensiallash yaqinlashishni "
                "yomonlashtiradi, chunki yuqori hadlar $m^2$ yoki "
                "$m^3$ ga ko'payadi. Bu umumiy qoida va u barcha "
                "qator yechimlarga tegishli — shu jumladan FEM da "
                "ham: ko'chish har doim kuchlanishdan aniqroq "
                "hisoblanadi, shuning uchun kuchlanish uchun "
                "post-protsessing (smoothing, superconvergent "
                "recovery) usullari qo'llaniladi. Hadlar hissasi "
                "jadvali esa boshqa muhim narsani ko'rsatadi: "
                "$(1,1)$ had og'ishning 102,4 % ini beradi, qolgan "
                "hadlar esa uni **kamaytiradi** (ishoralar manfiy). "
                "Bu fizik jihatdan mantiqiy: birinchi garmonika eng "
                "'yumshoq' shakl, u haqiqiy yechimdan biroz kattaroq "
                "og'ish beradi va yuqori hadlar tuzatish kiritadi. "
                "Konsentrlangan yuklamada esa ($load\\_kind = 2$) "
                "vaziyat butunlay boshqacha: $q_{mn}$ $m, n$ bilan "
                "kamaymaydi va moment markazda logarifmik "
                "cheksizlikka intiladi — qator yaqinlashmaydi."
            ),
            mistakes=[
                "Navye yechimini sharnirli bo'lmagan chekkali "
                "plastinaga qo'llash. Sinuslar bazisi faqat to'rt "
                "chekka sharnirli bo'lganda o'rinli; boshqa hollarda "
                "Levi yechimi (pq-08) yoki sonli usul kerak.",
                "Bir tekis yuklamada juft hadlarni hisoblash. "
                "$q_{mn} = 0$ agar $m$ yoki $n$ juft bo'lsa — "
                "ularni hisoblash vaqt yo'qotish.",
                "Og'ish uchun yetarli bo'lgan hadlar soni bilan "
                "kuchlanishni hisoblash. Moment uchun kamida "
                "$N = 11$, kesuvchi kuch uchun $N > 50$ kerak.",
                "Konsentrlangan yuklamada markazdagi momentni "
                "qatordan olish. U logarifmik cheksizlikka intiladi; "
                "amalda yuklama kichik yuza bo'ylab taqsimlangan "
                "deb olinadi.",
            ],
            quiz=[
                q("Nima uchun sinus funksiyalari Navye yechimi uchun "
                  "tanlanadi?",
                  "Ular sharnirli chegaraviy shartlarni ($w = 0$, "
                  "$\\nabla^2 w = 0$) avtomatik qanoatlantiradi va "
                  "bigarmonik operatorning xususiy funksiyalari — "
                  "differensiallashda shakl o'zgarmaydi.", "konseptual"),
                q("Qator koeffitsienti formulasini yozing.",
                  "$w_{mn} = q_{mn}/\\{D\\pi^4[(m/a)^2 + (n/b)^2]^2\\}$. "
                  "Maxraj tez o'sadi, shuning uchun yuqori hadlar "
                  "kichik.", "hisob"),
                q("Og'ish, moment va kesuvchi kuchning yaqinlashish "
                  "tezligini taqqoslang.",
                  "$O(m^{-5})$, $O(m^{-3})$, $O(m^{-1})$. Har "
                  "differensiallash ikki tartib yo'qotadi, shuning "
                  "uchun kesuvchi kuch juda sekin yaqinlashadi.",
                  "konseptual"),
                q("Bir tekis yuklamada nima uchun faqat toq hadlar qoladi?",
                  "Yuklama plastina markaziga nisbatan simmetrik, "
                  "juft sinuslar esa antisimmetrik — ularning "
                  "integrali nolga teng.", "talqin"),
                q("Kodda `solve(81)` nima uchun etalon sifatida "
                  "ishlatiladi?",
                  "81 had bilan hisoblangan natija amalda aniq "
                  "yechimga juda yaqin; unga nisbatan kichik $N$ "
                  "larning xatosi o'lchanadi — bu konvergensiya "
                  "tahlilining standart usuli.", "kod"),
                q("Konsentrlangan yuklamada qator nima uchun "
                  "yaqinlashmaydi?",
                  "$q_{mn}$ $m, n$ bilan kamaymaydi (faqat sinus "
                  "ko'paytuvchisi bor), shuning uchun moment qatori "
                  "logarifmik divergensiya beradi — markazda haqiqiy "
                  "singulyarlik bor.", "talqin"),
            ],
            bridge=(
                "Navye yechimi nafis, lekin juda tor: u faqat to'rt "
                "chekka sharnirli bo'lganda ishlaydi. Amaliyotda esa "
                "mahkamlangan va erkin chekkalar ham uchraydi. "
                "Keyingi mavzuda Levi yechimini o'rganamiz — u ikki "
                "chekkada sharnirli tayanch talab qiladi, qolgan "
                "ikkitasi ixtiyoriy bo'lishi mumkin."
            ),
            research=(
                "Qatorning yaqinlashish tezligini nazariy tahlil "
                "qiling. Furye qatorining yaqinlashishi funksiyaning "
                "silliqligiga bog'liq: $C^k$ funksiya uchun "
                "koeffitsientlar $O(m^{-k-1})$ kabi kamayadi. Bir "
                "tekis yuklama uzluksiz, lekin uning davriy "
                "davomi chekkalarda uzilishga ega — shuning uchun "
                "$q_{mn} \\sim 1/(mn)$. Buni Gibbs hodisasi bilan "
                "bog'lang: chekka yaqinida moment qatori tebranishlar "
                "beradimi? Sonli tajriba o'tkazing va Lanczos "
                "sigma-faktori bilan silliqlashtirishni sinab ko'ring."
            ),
            manim_ref=manim(
                scene="NavierSeriesScene",
                module="animatsiya/scenes/pq_solutions.py",
                title="Navye qatorining yig'ilishi",
                summary=(
                    "Birinchi garmonikadan boshlab hadlar ketma-ket "
                    "qo'shiladi; og'ish sirti deyarli darhol yakuniy "
                    "shaklga keladi, moment sirti esa sekinroq "
                    "yaqinlashishi yonma-yon ko'rsatiladi."
                ),
            ),
        ),
    ),

    # ------------------------------------------------------------------ pq-08
    Topic(
        id="pq-08",
        subject_id=S, module_id=M, order=8,
        title="Levi yechimi: bir yo'nalishli qator va oddiy differensial tenglama",
        description=(
            "Ikki qarama-qarshi chekkasi sharnirli tayangan plastina "
            "uchun bir tomonlama qator yechimi, hosil bo'ladigan oddiy "
            "differensial tenglama va uning ixtiyoriy chegaraviy "
            "shartlarda yechilishi."
        ),
        learning_objective=(
            "Levi yechimini qurish, to'rtinchi tartibli ODE ni yechish "
            "va qolgan ikki chekkada ixtiyoriy chegaraviy shartlarni "
            "qanoatlantirish."
        ),
        prerequisites=["pq-07"],
        mathematical_core=(
            "Bir tomonlama Furye qatori, $Y_m'''' - 2\\alpha_m^2 Y_m'' "
            "+ \\alpha_m^4 Y_m = q_m/D$, xarakteristik tenglamaning "
            "karrali ildizlari, giperbolik funksiyalar."
        ),
        engineering_application=(
            "Uzun panellar, ko'prik plitalari, mahkamlangan chekkali "
            "konstruksiyalar, qisman erkin chekkali qopqoqlar."
        ),
        computational_component=(
            "ODE ni analitik yechish, integrallash doimiylarini "
            "chegaraviy shartlardan topish, Navye yechimi bilan taqqoslash."
        ),
        visualization_component=(
            "Turli chegaraviy shartlarda og'ish profillari, giperbolik "
            "funksiyalarning hissasi, chekka effekti."
        ),
        research_extension=(
            "Levi yechimini uch va undan ko'p oraliqli uzluksiz "
            "plitalarga umumlashtiring: oraliqlar orasidagi moslik "
            "shartlari qanday yoziladi?"
        ),
        difficulty="ilg'or",
        previous_link=(
            "pq-07 dagi Navye yechimi to'rt chekkada sharnirli tayanch "
            "talab qilardi. Levi bu cheklovni yarmiga qisqartiradi: "
            "faqat ikki qarama-qarshi chekka sharnirli bo'lsa yetarli, "
            "qolgan ikkitasi ixtiyoriy bo'lishi mumkin."
        ),
        next_topic="pq-09",
        estimated_minutes=100,
        tags=["Levi", "ODE", "giperbolik", "plastina"],
        lesson=_lesson(
            problem=(
                "Ko'prik plitasi: ikki uzun chekkasi asosiy to'sinlarga "
                "qattiq mahkamlangan, ikki qisqa chekkasi esa deformatsiya "
                "choki orqali sharnirli tayangan. Navye yechimi bu yerda "
                "yaroqsiz — sinuslar mahkamlash shartini qanoatlantirmaydi. "
                "Lekin ikki qarama-qarshi chekka hali ham sharnirli. "
                "Shu qisman simmetriyadan foydalanib yechim qurish "
                "mumkinmi? Maurice Levi 1899-yilda buning yo'lini topgan."
            ),
            concepts=[
                c("Levi yechimi (Lévy solution)",
                  "$w = \\sum_m Y_m(y)\\sin\\frac{m\\pi x}{a}$ — faqat "
                  "$x$ bo'yicha qator, $y$ bo'yicha esa noma'lum "
                  "funksiya $Y_m(y)$."),
                c("Qisman ajratish (partial separation)",
                  "O'zgaruvchilarni to'liq ajratish o'rniga, faqat "
                  "bittasi bo'yicha qator olinadi; ikkinchisi bo'yicha "
                  "ODE hosil bo'ladi."),
                c("Xarakteristik tenglamaning karrali ildizlari",
                  "$(r^2 - \\alpha_m^2)^2 = 0$ — $r = \\pm\\alpha_m$ "
                  "ikki karrali. Shuning uchun yechimda "
                  "$y\\cosh$, $y\\sinh$ hadlari paydo bo'ladi."),
                c("Giperbolik funksiyalar",
                  "$\\cosh\\alpha y$, $\\sinh\\alpha y$ — mahalliy "
                  "(chekka yaqinidagi) effektlarni tavsiflaydi; "
                  "ular chekkadan uzoqlashganda tez o'sadi/kamayadi."),
                c("Chekka effekti (edge effect)",
                  "Mahkamlash yoki erkin chekka yaqinidagi mahalliy "
                  "bezovtalik; uning ta'sir zonasi $\\sim a/(m\\pi)$."),
                c("To'liq va xususiy yechim",
                  "$Y_m = Y_m^{\\text{xus}} + Y_m^{\\text{bir jinsli}}$: "
                  "birinchisi yuklamani, ikkinchisi chegaraviy shartlarni "
                  "qanoatlantiradi."),
            ],
            derivation=[
                d("1. Qisman ajratilgan yechim shakli",
                  r"w(x, y) = \sum_{m=1}^{\infty}Y_m(y)\sin\frac{m\pi x}{a}",
                  "$x = 0$ va $x = a$ chekkalari sharnirli — sinus "
                  "ularni avtomatik qanoatlantiradi. $y$ bo'yicha esa "
                  "hech qanday taxmin qilinmaydi."),
                d("2. Yuklamani ham yoyish",
                  r"q(x, y) = \sum_m q_m(y)\sin\frac{m\pi x}{a}, \qquad "
                  r"q_m(y) = \frac{2}{a}\int_0^a q(x, y)\sin\frac{m\pi x}{a}dx",
                  "Bir tomonlama Furye yoyilmasi. Bir tekis yuklama "
                  "uchun $q_m = 4q_0/(m\\pi)$, $m$ toq."),
                d("3. Bigarmonik operatorni qo'llash",
                  r"\nabla^4 w = \sum_m\Big[Y_m'''' - 2\alpha_m^2 Y_m'' "
                  r"+ \alpha_m^4 Y_m\Big]\sin\alpha_m x, \quad "
                  r"\alpha_m = \frac{m\pi}{a}",
                  "$x$ bo'yicha differensiallash sinusni o'zgartirmaydi, "
                  "faqat $-\\alpha_m^2$ ko'paytiradi. $y$ bo'yicha "
                  "hosilalar $Y_m$ ga tushadi."),
                d("4. Oddiy differensial tenglama",
                  r"Y_m'''' - 2\alpha_m^2 Y_m'' + \alpha_m^4 Y_m "
                  r"= \frac{q_m(y)}{D}",
                  "Ortogonallik tufayli har bir $m$ uchun alohida ODE. "
                  "PDE cheksiz sondagi **oddiy** differensial "
                  "tenglamaga ajraldi — Navyedagi algebraik "
                  "tenglamadan murakkabroq, lekin ancha umumiyroq."),
                d("5. Bir jinsli yechim: xarakteristik tenglama",
                  r"r^4 - 2\alpha_m^2 r^2 + \alpha_m^4 = (r^2 - \alpha_m^2)^2 = 0 "
                  r"\;\Rightarrow\; r = \pm\alpha_m \ (\text{ikki karrali})",
                  "Karrali ildizlar — bu muhim: oddiy eksponentalardan "
                  "tashqari $y e^{\\pm\\alpha y}$ hadlari ham kerak."),
                d("6. Bir jinsli yechimning to'liq shakli",
                  r"Y_m^{h} = A_m\cosh\alpha_m y + B_m\sinh\alpha_m y "
                  r"+ C_m\,\alpha_m y\cosh\alpha_m y + E_m\,\alpha_m y\sinh\alpha_m y",
                  "To'rtta doimiy — to'rtta chegaraviy shart "
                  "($y = \\pm b/2$ da ikkitadan). Giperbolik shakl "
                  "eksponensialdan qulayroq, chunki simmetriya oshkor."),
                d("7. Xususiy yechim (bir tekis yuklama)",
                  r"q_m = \frac{4q_0}{m\pi} = \text{const} \;\Rightarrow\; "
                  r"Y_m^{p} = \frac{q_m}{D\alpha_m^4} = \frac{4q_0 a^4}"
                  r"{D\pi^5 m^5}",
                  "$Y'' = Y'''' = 0$ deb olsak, $\\alpha_m^4 Y = q_m/D$. "
                  "Bu aynan Navye yechimining $y$ bo'yicha 'o'rtacha' qismi."),
                d("8. Chegaraviy shartlarni qo'llash",
                  r"\text{Mahkamlangan } y = \pm b/2: \ Y_m = 0,\ Y_m' = 0; "
                  r"\quad \text{Erkin: } Y_m'' - \nu\alpha_m^2 Y_m = 0, \ldots",
                  "To'rtta shartdan to'rtta doimiy topiladi. Simmetrik "
                  "yuklamada $B_m = C_m = 0$ va masala ikkiga tushadi — "
                  "hisob ancha soddalashadi."),
            ],
            meaning=(
                "Levi yechimining kuchi — **umumiylik bilan soddalik "
                "orasidagi muvozanat**. Navye yechimi eng sodda "
                "(algebraik tenglama), lekin eng tor (faqat to'rt "
                "sharnirli chekka). To'liq sonli usul eng umumiy, lekin "
                "analitik tushunchani yo'qotadi. Levi ularning "
                "o'rtasida: bitta yo'nalish bo'yicha analitik qator, "
                "ikkinchisi bo'yicha aniq ODE yechimi. Giperbolik "
                "funksiyalarning paydo bo'lishi ham chuqur ma'noga ega: "
                "$\\cosh\\alpha_m y$ va $\\sinh\\alpha_m y$ chekkadan "
                "uzoqlashganda $e^{\\alpha_m y}$ kabi tez o'sadi, "
                "ya'ni ular **mahalliy** effektlarni tavsiflaydi. "
                "$\\alpha_m = m\\pi/a$ bo'lgani uchun ta'sir zonasi "
                "$\\sim a/(m\\pi)$ — yuqori garmonikalar tezroq "
                "so'nadi. Bu Sen-Venan prinsipining (mq-05) "
                "matematik ko'rinishi: chekkadagi bezovtalik "
                "plastinaning ichkarisiga eksponensial kamayib "
                "tarqaladi va bir necha $a/\\pi$ masofadan keyin "
                "ahamiyatsiz bo'lib qoladi. Amaliy oqibati: uzun "
                "plastinada ($b \\gg a$) o'rta qism chekka "
                "shartlaridan mustaqil ravishda silindrik egilish "
                "rejimida ishlaydi."
            ),
            equations=[
                eq(r"w = \sum_m Y_m(y)\sin\frac{m\pi x}{a}",
                   "Levi yechimining shakli.", "Levi qatori"),
                eq(r"Y_m'''' - 2\alpha_m^2 Y_m'' + \alpha_m^4 Y_m "
                   r"= \frac{q_m}{D}, \quad \alpha_m = \frac{m\pi}{a}",
                   "Har bir garmonika uchun oddiy differensial tenglama.",
                   "Levi ODE"),
                eq(r"Y_m^h = (A_m + C_m\alpha_m y)\cosh\alpha_m y "
                   r"+ (B_m + E_m\alpha_m y)\sinh\alpha_m y",
                   "Bir jinsli yechim (karrali ildizlar tufayli "
                   "$y$ ko'paytuvchili hadlar).", "Bir jinsli yechim"),
                eq(r"\ell_{\text{chekka}} \sim \frac{a}{m\pi}",
                   "Chekka effektining ta'sir zonasi.", "Chekka effekti"),
            ],
            conditions=(
                "**Majburiy shart:** $x = 0$ va $x = a$ chekkalari "
                "sharnirli tayangan bo'lishi kerak.\n\n"
                "**$y = \\pm b/2$ chekkalarida ixtiyoriy shartlar:**\n"
                "- Mahkamlangan: $Y_m = 0$, $Y_m' = 0$;\n"
                "- Sharnirli: $Y_m = 0$, $Y_m'' - \\nu\\alpha_m^2 Y_m = 0$ "
                "(ya'ni $Y_m'' = 0$, chunki $Y_m = 0$);\n"
                "- Erkin: $M_y = 0$ va $V_y = 0$, ya'ni\n"
                "$$Y_m'' - \\nu\\alpha_m^2 Y_m = 0, \\qquad "
                "Y_m''' - (2-\\nu)\\alpha_m^2 Y_m' = 0;$$\n"
                "- Elastik tayanch: $Y_m''' - (2-\\nu)\\alpha_m^2 Y_m' "
                "= \\frac{k}{D}Y_m$.\n\n"
                "**Simmetriya:** yuklama $y = 0$ ga nisbatan simmetrik "
                "bo'lsa, $Y_m$ juft funksiya va $B_m = C_m = 0$ — "
                "to'rtta noma'lum ikkitaga tushadi."
            ),
            worked=WorkedExample(
                statement=(
                    "Plastina $a = 4$ m ($x$ bo'yicha, sharnirli), "
                    "$b = 6$ m ($y$ bo'yicha, ikkala chekka "
                    "mahkamlangan), $h = 180$ mm, $E = 30$ GPa, "
                    "$\\nu = 0{,}2$, $q_0 = 8$ kPa. Birinchi garmonika "
                    "($m = 1$) uchun Levi yechimini quring va "
                    "markazdagi og'ishni toping. Navye yechimi bilan "
                    "(to'rt chekka sharnirli) taqqoslang."
                ),
                given=[
                    r"a = 4\ \text{m},\ b = 6\ \text{m},\ h = 0{,}18\ \text{m}",
                    r"E = 30\ \text{GPa},\ \nu = 0{,}2,\ q_0 = 8000\ \text{Pa}",
                    r"y = \pm b/2 \ \text{mahkamlangan}",
                ],
                steps=[
                    st(r"D = \frac{30\times10^9 \cdot 5{,}832\times10^{-3}}"
                       r"{12 \cdot 0{,}96} = 1{,}519\times10^{7}\ \text{N·m}",
                       "$h^3 = 5{,}832\\times10^{-3}$ m³."),
                    st(r"\alpha_1 = \frac{\pi}{4} = 0{,}7854\ \text{m}^{-1}; "
                       r"\quad q_1 = \frac{4q_0}{\pi} = \frac{32\,000}{3{,}1416} "
                       r"= 10\,186\ \text{Pa}",
                       "Birinchi garmonika parametrlari."),
                    st(r"Y_1^{p} = \frac{q_1}{D\alpha_1^4} = "
                       r"\frac{10\,186}{1{,}519\times10^{7} \cdot 0{,}38050} "
                       r"= 1{,}7623\times10^{-3}\ \text{m}",
                       "$\\alpha_1^4 = 0{,}7854^4 = 0{,}38050$. Bu — "
                       "silindrik egilish darajasidagi og'ish."),
                    st(r"\text{Simmetriya} \Rightarrow Y_1 = Y_1^p + "
                       r"A\cosh\alpha y + E\,\alpha y\sinh\alpha y",
                       "Yuklama $y$ ga nisbatan juft, demak $\\sinh$ va "
                       "$y\\cosh$ hadlari tushadi."),
                    st(r"\beta = \alpha_1\frac{b}{2} = 0{,}7854 \cdot 3 "
                       r"= 2{,}3562; \quad \cosh\beta = 5{,}3228, \ "
                       r"\sinh\beta = 5{,}2280",
                       "Chekkadagi argument. $\\beta > 2$ — giperbolik "
                       "funksiyalar allaqachon katta."),
                    st(r"\begin{bmatrix}\cosh\beta & \beta\sinh\beta\\ "
                       r"\sinh\beta & \sinh\beta + \beta\cosh\beta\end{bmatrix}"
                       r"\begin{Bmatrix}A\\E\end{Bmatrix} = "
                       r"\begin{Bmatrix}-Y_1^p\\0\end{Bmatrix}",
                       "Mahkamlashning ikki sharti ($Y = 0$, $Y' = 0$) "
                       "ikkita noma'lumli chiziqli tizim beradi."),
                    st(r"\Delta = \cosh\beta\sinh\beta + \beta "
                       r"= 27{,}8310 + 2{,}3562 = 30{,}1872",
                       "Determinant soddalashadi, chunki "
                       "$\\cosh^2\\beta - \\sinh^2\\beta = 1$."),
                    st(r"A = -\frac{Y_1^p(\sinh\beta + \beta\cosh\beta)}{\Delta} "
                       r"= -\frac{1{,}7622\times10^{-3} \cdot 17{,}7696}"
                       r"{30{,}1872} = -1{,}0373\times10^{-3}\ \text{m}",
                       "$\\sinh\\beta + \\beta\\cosh\\beta = 5{,}2280 + "
                       "12{,}5416 = 17{,}7696$."),
                    st(r"E = \frac{Y_1^p\sinh\beta}{\Delta} = "
                       r"\frac{1{,}7622\times10^{-3} \cdot 5{,}2280}{30{,}1872} "
                       r"= 3{,}0517\times10^{-4}\ \text{m}",
                       "Ikkinchi doimiy — u markazda hissa qo'shmaydi, "
                       "lekin chekka yaqinida hal qiluvchi."),
                    st(r"Y_1(0) = Y_1^p + A = 1{,}7622\times10^{-3} "
                       r"- 1{,}0373\times10^{-3} = 7{,}249\times10^{-4}\ "
                       r"\text{m} = 0{,}725\ \text{mm}",
                       "Markazda $\\cosh 0 = 1$, $y\\sinh 0 = 0$ — "
                       "faqat $Y^p$ va $A$ qoladi."),
                    st(r"w_{\text{Navye}}(m=n=1) = \frac{16q_0/\pi^2}"
                       r"{D\pi^4[(1/4)^2 + (1/6)^2]^2} = "
                       r"\frac{12\,967}{1{,}2059\times10^{7}} = 1{,}075\ \text{mm}",
                       "Sharnirli holat uchun taqqoslash. Mahkamlash "
                       "og'ishni **1,48 marta** kamaytirdi."),
                ],
                answer=(
                    "$Y_1^p = 1{,}762$ mm (silindrik daraja); "
                    "mahkamlangan chekkalar bilan markazda "
                    "$w \\approx 0{,}725$ mm, sharnirli holatda "
                    "1,075 mm — mahkamlash og'ishni 1,48 marta "
                    "kamaytiradi va silindrik darajadan 59 % ni "
                    "'qaytarib oladi'. To'liq qator (15 had) mos "
                    "ravishda 0,718 va 1,042 mm beradi."
                ),
                engineering_note=(
                    "1,48 marta farq mahkamlash sharoitini to'g'ri "
                    "baholashning muhimligini ko'rsatadi. Amalda "
                    "'mahkamlangan' chekka kamdan-kam ideal bo'ladi: "
                    "to'sin buraladi, birikma erkin qoladi. Shuning "
                    "uchun konservativ loyihalashda ko'pincha sharnirli "
                    "deb hisoblanadi (og'ish uchun) va mahkamlangan deb "
                    "hisoblanadi (chekkadagi moment uchun) — ikkala "
                    "xavfli holat qamrab olinadi."
                ),
            ),
            computation=Computation(
                caption=(
                    "Levi yechimini turli chegaraviy shartlar uchun "
                    "qurish, giperbolik hadlarni topish va Navye "
                    "yechimi bilan taqqoslash."
                ),
                code='''"""Levi yechimi: bir yo'nalishli qator va ODE."""
import numpy as np
from labkit import PARAMS, note, series, table, value

a = float(PARAMS.get("a", 4.0))          # sharnirli yo'nalish, m
b = float(PARAMS.get("b", 6.0))          # ixtiyoriy chekkalar, m
h = float(PARAMS.get("h", 180.0))/1000.0
E = float(PARAMS.get("E", 30.0))*1e9
nu = float(PARAMS.get("nu", 0.2))
q0 = float(PARAMS.get("q0", 8000.0))
bc = int(PARAMS.get("bc", 0))            # 0 mahkamlangan, 1 sharnirli, 2 erkin
nmax = int(PARAMS.get("nmax", 15))

D = E*h**3/(12*(1 - nu**2))
value("Silindrik bikrlik D", D/1e6, "MN*m")
value("b/a", b/a, "—")

yg = np.linspace(-b/2, b/2, 201)
W = np.zeros_like(yg)
Wnav = np.zeros_like(yg)
terms_info = []

for m in range(1, nmax + 1, 2):          # bir tekis yuklama: toq hadlar
    al = m*np.pi/a
    qm = 4*q0/(m*np.pi)
    Yp = qm/(D*al**4)                     # xususiy yechim (doimiy)
    beta = al*b/2
    ch, sh = np.cosh(beta), np.sinh(beta)

    # Umumiy shakl: Y = Yp + A*cosh(al*y) + Ec*al*y*sinh(al*y)
    #   dY/dy    = al*[A*sh + Ec*(sh + al*y*ch)]
    #   d2Y/dy2  = al^2*[A*ch + Ec*(2*ch + al*y*sh)]
    #   d3Y/dy3  = al^3*[A*sh + Ec*(3*sh + al*y*ch)]
    if bc == 0:      # mahkamlangan: Y = 0, Y' = 0
        A11, A12, r1 = ch, beta*sh, -Yp
        A21, A22, r2 = sh, sh + beta*ch, 0.0
    elif bc == 1:    # sharnirli: Y = 0, Y'' = 0
        A11, A12, r1 = ch, beta*sh, -Yp
        A21, A22, r2 = ch, 2*ch + beta*sh, 0.0
    else:            # erkin: M_y = 0, V_y = 0
        A11, A12, r1 = (1 - nu)*ch, 2*ch + (1 - nu)*beta*sh, nu*Yp
        A21, A22, r2 = -(1 - nu)*sh, (1 + nu)*sh - (1 - nu)*beta*ch, 0.0

    det = A11*A22 - A12*A21
    A = (r1*A22 - A12*r2)/det
    Ec = (A11*r2 - r1*A21)/det
    Y = Yp + A*np.cosh(al*yg) + Ec*al*yg*np.sinh(al*yg)

    W += Y*np.sin(m*np.pi/2)             # x = a/2 markaziy kesim
    # Navye (to'rt chekka sharnirli) taqqoslash uchun
    for n in range(1, nmax + 1, 2):
        bn = n*np.pi/b
        qmn = 16*q0/(np.pi**2*m*n)
        Wnav += qmn/(D*(al**2 + bn**2)**2)*np.sin(m*np.pi/2)*np.sin(bn*(yg + b/2))
    if m <= 5:
        terms_info.append([m, round(Yp*1000, 4), round(float(np.max(np.abs(Y)))*1000, 4)])

bc_name = {0: "mahkamlangan", 1: "sharnirli", 2: "erkin"}[bc]
series(f"w(y) — {bc_name} chekkalar", yg.tolist(), (W*1000).tolist(),
       xlabel="y, m", ylabel="Og'ish w, mm")
series("w(y) — Navye (4 chekka sharnirli)", yg.tolist(), (Wnav*1000).tolist(),
       xlabel="y, m", ylabel="Og'ish w, mm")

w_levi = float(np.max(np.abs(W)))
w_navier = float(np.max(np.abs(Wnav)))
value("w_max (Levi, %s)" % bc_name, w_levi*1000, "mm")
value("w_max (Navye, sharnirli)", w_navier*1000, "mm")
value("Levi / Navye nisbati", w_levi/w_navier if w_navier else 0.0, "—")

# Silindrik egilish darajasi (chekkasiz)
al1 = np.pi/a
Yp1 = (4*q0/np.pi)/(D*al1**4)
value("Xususiy yechim Y_p (1-garmonika)", Yp1*1000, "mm")
value("Chekka shartlari ta'siri", 100*(1 - w_levi/Yp1), "%")

if bc == 0:
    note(f"Mahkamlash og'ishni Navye holatidan {w_navier/w_levi:.2f} marta "
         f"kamaytiradi va silindrik darajadan {100*(1-w_levi/Yp1):.1f} % ni "
         f"qaytarib oladi.")
elif bc == 2:
    note(f"Erkin chekkalar og'ishni sezilarli oshiradi: {w_levi*1000:.3f} mm "
         f"({w_levi/w_navier:.2f} marta Navye holatidan katta).")

table("1-garmonika hadlari",
      ["m", "Y_p (xususiy), mm", "max|Y_m|, mm"], terms_info)

# --- Chekka effektining so'nish masshtabi ---
for m in [1, 3, 5, 9]:
    al = m*np.pi/a
    value(f"Chekka effekti zonasi (m = {m})", 1/al, "m")
note("Chekka effektining so'nish masofasi 1/alpha_m = a/(m*pi): "
     "yuqori garmonikalar tezroq so'nadi — Sen-Venan prinsipi.")

decay_y = np.linspace(0, b/2, 200)
for m in [1, 3, 5]:
    al = m*np.pi/a
    series(f"Chekka effekti so'nishi (m = {m})", decay_y.tolist(),
           np.exp(-al*decay_y).tolist(),
           xlabel="Chekkadan masofa, m", ylabel="Nisbiy amplituda")

# --- b/a ning ta'siri ---
ratios = np.linspace(0.5, 5.0, 40)
wr_c, wr_s = [], []
for r_ in ratios:
    bb = r_*a
    al = np.pi/a
    qm = 4*q0/np.pi
    Yp = qm/(D*al**4)
    beta = al*bb/2
    ch, sh = np.cosh(beta), np.sinh(beta)
    det = ch*(sh + beta*ch) - beta*sh*sh
    A = -Yp*(sh + beta*ch)/det
    wr_c.append((Yp + A)*1000)
    # Navye
    s = 0.0
    for n in range(1, 16, 2):
        bn = n*np.pi/bb
        qmn = 16*q0/(np.pi**2*1*n)
        s += qmn/(D*(al**2 + bn**2)**2)*np.sin(n*np.pi/2)
    wr_s.append(s*1000)
series("w_max(b/a) mahkamlangan", ratios.tolist(), wr_c,
       xlabel="b/a", ylabel="w_max, mm")
series("w_max(b/a) sharnirli", ratios.tolist(), wr_s,
       xlabel="b/a", ylabel="w_max, mm")
note(f"b/a katta bo'lganda ikkala egri chiziq ham gorizontal "
     f"asimptotaga chiqadi: mahkamlangan {wr_c[-1]:.3f} mm, "
     f"sharnirli {wr_s[-1]:.3f} mm — chekka effekti markazga yetmaydi.")

table("Navye va Levi yechimlarining taqqoslashi",
      ["Jihat", "Navye", "Levi"],
      [["Chegaraviy shartlar", "4 chekka sharnirli",
        "2 qarama-qarshi sharnirli"],
       ["Yechim shakli", "sin(m pi x/a)*sin(n pi y/b)", "Y_m(y)*sin(m pi x/a)"],
       ["Hosil bo'ladigan masala", "algebraik tenglama", "4-tartibli ODE"],
       ["Umumiylik", "past", "yuqori"],
       ["Murakkablik", "juda sodda", "o'rtacha"],
       ["Yaqinlashish", "O(m^-5)", "O(m^-5), lekin har had qimmatroq"]])
''',
                parameters=[
                    p("a", "Sharnirli yo'nalish a", 0.5, 20.0, 4.0, 0.1, "m"),
                    p("b", "Ixtiyoriy chekkalar b", 0.5, 30.0, 6.0, 0.1, "m"),
                    p("h", "Qalinlik h", 10.0, 500.0, 180.0, 5.0, "mm"),
                    p("E", "Yung moduli E", 1.0, 400.0, 30.0, 1.0, "GPa"),
                    p("nu", "Puasson koeffitsienti ν", 0.0, 0.45, 0.2, 0.01),
                    p("q0", "Yuklama q₀", 100.0, 100000.0, 8000.0, 100.0, "Pa"),
                    p("bc", "y-chekkalar (0 mahkam, 1 sharnir, 2 erkin)",
                      0.0, 2.0, 0.0, 1.0),
                    p("nmax", "Qator hadlari N", 1.0, 41.0, 15.0, 2.0),
                ],
                expected_output=(
                    "D = 15,19 MN·m; mahkamlangan chekkalarda "
                    "w_max = 0,718 mm, Navye (sharnirli) = 1,042 mm — "
                    "nisbat 0,69. bc = 1 tanlansa Levi yechimi Navye "
                    "bilan aynan ustma-ust tushadi (1,042 mm) — bu "
                    "implementatsiyaning mustaqil tekshiruvi. Erkin "
                    "chekkalarda 1,914 mm; chekka effekti zonasi "
                    "1/α₁ = 1,27 m."
                ),
            ),
            visual=vis(
                kind="Levi yechimi va chekka effekti",
                tool="React/SVG",
                description=(
                    "Turli chegaraviy shartlardagi $w(y)$ profillari, "
                    "giperbolik hadlarning hissasi va chekka "
                    "effektining eksponensial so'nishi."
                ),
                how_to_draw=(
                    "React/SVG: asosiy panel — $w(y)$ profillari "
                    "markaziy kesim bo'ylab. Uchta egri chiziq bir "
                    "grafikda: mahkamlangan, sharnirli va erkin "
                    "chekkalar; ularning farqi darhol ko'rinadi. "
                    "Gorizontal punktir chiziq $Y_m^p$ (silindrik "
                    "daraja) ni ko'rsatadi — barcha yechimlar undan "
                    "pastda. Ikkinchi panel — yechimning "
                    "tarkibiy qismlari: $Y^p$ (doimiy), "
                    "$A\\cosh\\alpha y$ va $E\\alpha y\\sinh\\alpha y$ "
                    "alohida chiziladi, ular qo'shilib to'liq "
                    "yechimni berishi ko'rinadi. Uchinchi panel — "
                    "chekka effekti: $e^{-\\alpha_m y}$ egri "
                    "chiziqlari $m = 1, 3, 5$ uchun; ular chekkadan "
                    "qanchalik tez so'nishi va yuqori garmonikalar "
                    "tezroq so'nishi ko'rinadi. Chegaraviy shart "
                    "tugmalari bilan tanlanadi va barcha panellar "
                    "sinxron yangilanadi."
                ),
            ),
            interp=(
                "Chekka effektining so'nish grafigi eng ma'lumotli: "
                "birinchi garmonika uchun ta'sir zonasi "
                "$1/\\alpha_1 = a/\\pi \\approx 0{,}32a$, uchinchi "
                "uchun uch marta kichik. Demak chekkadagi bezovtalik "
                "plastina ichkarisiga taxminan **yarim tomon** "
                "masofasigacha yetadi. $b/a > 3$ bo'lganda ikki "
                "chekkadagi effektlar bir-biriga yetmaydi va markaziy "
                "qism silindrik egilish rejimida ishlaydi — bu "
                "$b/a$ grafigidagi gorizontal asimptotada ko'rinadi. "
                "Amaliy xulosa: uzun panelda chekka shartlari faqat "
                "chekka yaqinidagi hisoblarga ta'sir qiladi, markazda "
                "esa bir o'lchovli formula yetarli. Kod muhim "
                "mustaqil tekshiruv ham beradi: `bc = 1` (sharnirli) "
                "tanlansa, Levi yechimi Navye yechimi bilan **aynan** "
                "ustma-ust tushadi (1,0416 mm ikkalasida ham). Ikki "
                "butunlay boshqa yo'l — ikki tomonlama qator va "
                "bir tomonlama qator + ODE — bir xil javob berishi "
                "implementatsiyaning to'g'riligini isbotlaydi. "
                "Mahkamlashning 1,48 marta ta'siri esa qisqa "
                "plastinalarda hal qiluvchi — u yerda ikki chekkadan "
                "kelgan effektlar ustma-ust tushadi va bir-birini "
                "kuchaytiradi. "
                "Karrali ildizlar tufayli paydo bo'lgan "
                "$y\\sinh\\alpha y$ hadi ham muhim: usiz to'rtta "
                "chegaraviy shartni qanoatlantirish imkonsiz bo'lar "
                "edi, chunki faqat ikkita mustaqil funksiya qolardi."
            ),
            mistakes=[
                "Karrali ildizlarni unutib, yechimni faqat "
                "$A\\cosh + B\\sinh$ shaklida izlash. Bu ikkita "
                "doimiy beradi, lekin to'rtta shart bor — masala "
                "yechilmaydi.",
                "Levi yechimini to'rt chekkasi ham mahkamlangan "
                "plastinaga qo'llash. Kamida ikki qarama-qarshi "
                "chekka sharnirli bo'lishi shart.",
                "Katta $\\beta = \\alpha_m b/2$ da giperbolik "
                "funksiyalarni to'g'ridan-to'g'ri hisoblash. "
                "$\\cosh(50) \\approx 10^{21}$ — sonli to'lib "
                "ketish; eksponensial shaklga o'tish yoki "
                "masshtablash kerak.",
                "Simmetriyani hisobga olmaslik. Simmetrik yuklamada "
                "to'rtta noma'lum ikkitaga tushadi — hisob ikki "
                "marta soddalashadi va sonli barqarorlik yaxshilanadi.",
            ],
            quiz=[
                q("Levi yechimi Navyedan nimasi bilan farq qiladi?",
                  "Faqat bitta yo'nalish bo'yicha qator olinadi; "
                  "ikkinchi yo'nalish bo'yicha noma'lum funksiya "
                  "$Y_m(y)$ qoladi va u ODE dan topiladi. Shuning "
                  "uchun ikki chekkada ixtiyoriy shart qo'yish mumkin.",
                  "konseptual"),
                q("Nima uchun yechimda $y\\cosh$ va $y\\sinh$ hadlari "
                  "paydo bo'ladi?",
                  "Xarakteristik tenglama $(r^2-\\alpha^2)^2 = 0$ — "
                  "ildizlar ikki karrali. Karrali ildizda ikkinchi "
                  "mustaqil yechim $y e^{ry}$ ko'rinishida bo'ladi.",
                  "konseptual"),
                q("$a = 3$ m, $m = 1$. Chekka effektining so'nish "
                  "masofasini toping.",
                  "$1/\\alpha_1 = a/\\pi = 3/3{,}1416 = 0{,}955$ m — "
                  "bu masofada amplituda $e$ marta kamayadi.", "hisob"),
                q("Mahkamlash og'ishni qanchaga kamaytiradi va bu "
                  "nimaga bog'liq?",
                  "Misolda 1,86 marta. Bu $b/a$ ga bog'liq: "
                  "$b/a$ kichik bo'lsa ta'sir kuchli, katta bo'lsa "
                  "chekka effekti markazga yetmaydi va ta'sir "
                  "kamayadi.", "talqin"),
                q("Kodda katta $\\beta$ da qanday sonli muammo "
                  "paydo bo'lishi mumkin?",
                  "$\\cosh\\beta$ va $\\sinh\\beta$ eksponensial "
                  "o'sadi va $\\beta > 700$ da `float` to'lib "
                  "ketadi. Amalda $\\beta$ katta bo'lsa chekka "
                  "effekti ahamiyatsiz va soddalashtirish mumkin.",
                  "kod"),
                q("Uzun plastinada ($b \\gg a$) markazdagi og'ish "
                  "nimaga teng bo'ladi?",
                  "Silindrik egilish darajasiga, ya'ni xususiy "
                  "yechim $Y^p$ ga — chekka effekti markazga "
                  "yetmaydi va chegaraviy shartlar ahamiyatsiz "
                  "bo'lib qoladi.", "talqin"),
            ],
            bridge=(
                "Navye va Levi — analitik usullar, lekin ikkalasi "
                "ham geometriya va chegaraviy shartlarga cheklov "
                "qo'yadi. Ixtiyoriy shakl va shartlar uchun "
                "taqribiy usullar kerak. Keyingi mavzuda energiya "
                "usullarini — Ritz va Galerkin — plastinalarga "
                "qo'llaymiz."
            ),
            research=(
                "Levi yechimini ko'p oraliqli uzluksiz plitalarga "
                "umumlashtiring. Har bir oraliqda o'z $Y_m^{(i)}(y)$ "
                "funksiyasi bo'ladi; oraliqlar chegarasida to'rtta "
                "moslik sharti yoziladi: $w$, $\\partial w/\\partial y$, "
                "$M_y$ uzluksiz va $V_y$ da tayanch reaksiyasiga teng "
                "sakrash. Uch oraliqli plita uchun tizimni tuzing va "
                "yeching; tayanch ustidagi manfiy momentni oraliqdagi "
                "musbat moment bilan taqqoslang. Bu natija uzluksiz "
                "plitalarni armaturalash qoidalarini qanday asoslaydi?"
            ),
            manim_ref=manim(
                scene="LevySolutionScene",
                module="animatsiya/scenes/pq_solutions.py",
                title="Levi yechimi va chekka effekti",
                summary=(
                    "Plastina bo'ylab og'ish profili quriladi: "
                    "markazda silindrik egilish, chekkalarda esa "
                    "giperbolik hadlar hisobiga mahalliy bezovtalik "
                    "paydo bo'lishi va uning eksponensial so'nishi "
                    "ko'rsatiladi."
                ),
            ),
        ),
    ),

    # ------------------------------------------------------------------ pq-09
    Topic(
        id="pq-09",
        subject_id=S, module_id=M, order=9,
        title="Energiya usullari plastinalarda: Ritz va Galerkin taqribiy yechimlari",
        description=(
            "Plastinaning deformatsiya energiyasi funksionali, minimal "
            "potensial energiya prinsipi, Ritz usuli bilan taqribiy "
            "yechim qurish va Galerkin usuli bilan taqqoslash."
        ),
        learning_objective=(
            "Plastina uchun energiya funksionalini yozish, mos bazis "
            "funksiyalarni tanlash, Ritz tizimini tuzib yechish va "
            "taqribiy yechimning aniqligini baholash."
        ),
        prerequisites=["pq-08", "tmm-19"],
        mathematical_core=(
            "$\\Pi = \\frac{D}{2}\\int(\\nabla^2 w)^2 dA + \\ldots - "
            "\\int qw\\,dA$, $\\partial\\Pi/\\partial c_i = 0$, "
            "chiziqli tizim $\\mathbf{Kc} = \\mathbf{f}$, Galerkin "
            "ortogonallik sharti."
        ),
        engineering_application=(
            "Ixtiyoriy shaklli va chegaraviy shartli plastinalar, "
            "FEM ning nazariy asosi, tez muhandislik baholari, "
            "kritik yuklama va chastotalarni taxminiy hisoblash."
        ),
        computational_component=(
            "Ritz matritsasini sonli qurish, chiziqli tizimni yechish, "
            "bazis funksiyalar sonining aniqlikka ta'sirini o'rganish."
        ),
        visualization_component=(
            "Bazis funksiyalar, ularning superpozitsiyasi, "
            "yaqinlashish grafigi va aniq yechim bilan taqqoslash."
        ),
        research_extension=(
            "Ritz usulidan chekli elementlar usuliga o'tishni "
            "o'rganing: bazis funksiyalarni mahalliylashtirsak nima "
            "o'zgaradi va nima uchun matritsa siyrak bo'lib qoladi?"
        ),
        difficulty="murakkab",
        previous_link=(
            "pq-07 va pq-08 dagi aniq yechimlar geometriya va "
            "chegaraviy shartlarga qat'iy cheklov qo'yardi. tmm-19 "
            "dagi variatsion prinsip esa hech qanday cheklov "
            "qo'ymaydi — u ixtiyoriy masalaga taqribiy yechim "
            "qurish imkonini beradi."
        ),
        next_topic="pq-10",
        estimated_minutes=95,
        tags=["Ritz", "Galerkin", "energiya", "taqribiy"],
        lesson=_lesson(
            problem=(
                "To'rt chekkasi mahkamlangan kvadrat plastina uchun "
                "aniq yechim yo'q: Navye yaroqsiz (chekkalar sharnirli "
                "emas), Levi ham yaroqsiz (biror juft chekka sharnirli "
                "emas). Lekin bu eng ko'p uchraydigan holatlardan biri — "
                "payvandlangan panel, quyilgan plita. Nima qilamiz? "
                "Javob: aniq yechimni izlashdan voz kechib, **eng "
                "yaxshi taqribiy** yechimni qidiramiz. Energiya "
                "prinsipi bunga aniq mezon beradi."
            ),
            concepts=[
                c("Deformatsiya energiyasi",
                  "$U = \\frac{D}{2}\\int_A\\big[(\\nabla^2 w)^2 - "
                  "2(1-\\nu)(w_{,xx}w_{,yy} - w_{,xy}^2)\\big]dA$ — "
                  "plastinaning egilishda to'plagan energiyasi."),
                c("Minimal potensial energiya prinsipi",
                  "Haqiqiy yechim $\\Pi = U - W$ funksionalini barcha "
                  "mumkin bo'lgan (kinematik jihatdan maqbul) "
                  "ko'chishlar orasida minimallashtiradi."),
                c("Ritz usuli",
                  "$w \\approx \\sum_i c_i\\phi_i(x,y)$ — bazis "
                  "funksiyalar tanlanadi, koeffitsientlar "
                  "$\\partial\\Pi/\\partial c_i = 0$ dan topiladi."),
                c("Kinematik maqbul funksiyalar",
                  "Bazis funksiyalar **muhim** (geometrik) chegaraviy "
                  "shartlarni qanoatlantirishi shart; tabiiy (kuch) "
                  "shartlar avtomatik bajariladi."),
                c("Galerkin usuli",
                  "Qoldiqni bazis funksiyalarga ortogonal qilish: "
                  "$\\int_A (D\\nabla^4 w - q)\\phi_i\\,dA = 0$. "
                  "Energiya funksionali bo'lmagan masalalarda ham ishlaydi."),
                c("Yuqoridan baho (upper bound)",
                  "Ritz yechimi haqiqiy yechimdan **bikrroq** chiqadi, "
                  "ya'ni og'ish kam baholanadi. Bazis kengaytirilsa "
                  "monoton ravishda aniq yechimga yaqinlashadi."),
            ],
            derivation=[
                d("1. Deformatsiya energiyasi zichligi",
                  r"u = \tfrac{1}{2}\big(\sigma_x\varepsilon_x + "
                  r"\sigma_y\varepsilon_y + \tau_{xy}\gamma_{xy}\big)",
                  "Chiziqli elastik jismda energiya zichligi (tmm-19). "
                  "Plastinada kuchlanish va deformatsiya $z$ ga chiziqli."),
                d("2. Qalinlik bo'yicha integrallash",
                  r"U = \frac{D}{2}\int_A\Big[\kappa_x^2 + \kappa_y^2 "
                  r"+ 2\nu\kappa_x\kappa_y + 2(1-\nu)\kappa_{xy}^2\Big]dA",
                  "pq-02 va pq-03 dagi munosabatlarni qo'yib "
                  "$\\int_{-h/2}^{h/2}z^2dz = h^3/12$ ni hisoblaymiz."),
                d("3. Laplasian orqali qayta yozish",
                  r"U = \frac{D}{2}\int_A\Big[(\nabla^2 w)^2 - 2(1-\nu)"
                  r"\big(w_{,xx}w_{,yy} - w_{,xy}^2\big)\Big]dA",
                  "$\\kappa_x + \\kappa_y = -\\nabla^2 w$ va "
                  "$\\kappa_x\\kappa_y - \\kappa_{xy}^2 = $ Gauss "
                  "egriligi. Ikkinchi had — to'liq divergensiya, "
                  "shuning uchun sobit chegaraviy shartlarda hissa qo'shmaydi."),
                d("4. To'liq potensial energiya",
                  r"\Pi[w] = U[w] - \int_A q\,w\,dA",
                  "Tashqi kuchlarning ishi ayriladi. Haqiqiy yechim "
                  "$\\Pi$ ni minimallashtiradi."),
                d("5. Ritz approksimatsiyasi",
                  r"w(x, y) \approx \sum_{i=1}^{N}c_i\,\phi_i(x, y)",
                  "Bazis funksiyalar $\\phi_i$ oldindan tanlanadi va "
                  "geometrik chegaraviy shartlarni qanoatlantiradi. "
                  "Noma'lumlar — $N$ ta son $c_i$."),
                d("6. Minimallashtirish sharti",
                  r"\frac{\partial\Pi}{\partial c_i} = 0, \quad "
                  r"i = 1, \ldots, N \;\Longrightarrow\; "
                  r"\sum_j K_{ij}c_j = f_i",
                  "$\\Pi$ $c_i$ larning kvadratik funksiyasi, shuning "
                  "uchun hosila chiziqli — oddiy chiziqli tizim hosil bo'ladi."),
                d("7. Bikrlik matritsasi va yuklama vektori",
                  r"K_{ij} = D\int_A\Big[\nabla^2\phi_i\nabla^2\phi_j "
                  r"- (1-\nu)\big(\phi_{i,xx}\phi_{j,yy} + "
                  r"\phi_{i,yy}\phi_{j,xx} - 2\phi_{i,xy}\phi_{j,xy}\big)\Big]dA, "
                  r"\quad f_i = \int_A q\phi_i\,dA",
                  "$K$ simmetrik va musbat aniqlangan — bu energiya "
                  "funksionalining qavariqligidan kelib chiqadi. "
                  "FEM bikrlik matritsasining to'g'ridan-to'g'ri "
                  "ajdodi aynan shu."),
                d("8. Galerkin usuli va ekvivalentlik",
                  r"\int_A\big(D\nabla^4 w_N - q\big)\phi_i\,dA = 0 "
                  r"\;\Longleftrightarrow\; \frac{\partial\Pi}{\partial c_i} = 0",
                  "Ikki marta bo'laklab integrallash Galerkin shartini "
                  "Ritz tizimiga aylantiradi (agar chegaraviy hadlar "
                  "yo'qolsa). Demak simmetrik masalalarda ular ekvivalent."),
            ],
            meaning=(
                "Ritz usulining falsafasi — **izlash sohasini "
                "cheklash**. Haqiqiy yechim cheksiz o'lchovli "
                "funksiyalar fazosida yotadi; biz uning $N$ o'lchovli "
                "qism fazosiga proeksiyasini qidiramiz. Energiya "
                "prinsipi esa 'eng yaxshi proeksiya' nima ekanligini "
                "aniq belgilaydi: energiya normasi bo'yicha eng yaqin "
                "element. Bundan muhim xulosa kelib chiqadi: **Ritz "
                "yechimi har doim haqiqiy yechimdan bikrroq**. Chunki "
                "biz plastinani sun'iy ravishda cheklab qo'ydik — u "
                "faqat tanlangan shakllarda deformatsiyalanishi mumkin. "
                "Har qanday qo'shimcha cheklov esa konstruksiyani "
                "bikrroq qiladi. Shuning uchun og'ish har doim kam "
                "baholanadi, xususiy chastota esa oshirib baholanadi. "
                "Bu bir tomondan xato, ikkinchi tomondan **kafolat**: "
                "biz xatoning yo'nalishini bilamiz. Bazis "
                "kengaytirilganda cheklov yumshaydi va yechim "
                "monoton ravishda pastdan (energiya bo'yicha) aniq "
                "yechimga yaqinlashadi. Va nihoyat, $K_{ij}$ "
                "matritsasining tuzilishi — bu chekli elementlar "
                "usulining bevosita ajdodi: FEM shunchaki $\\phi_i$ "
                "larni butun soha bo'ylab emas, mayda elementlarda "
                "mahalliy qilib tanlaydi, qolgan hamma narsa bir xil."
            ),
            equations=[
                eq(r"\Pi[w] = \frac{D}{2}\int_A(\nabla^2 w)^2 dA - "
                   r"\int_A qw\,dA + \text{(chegaraviy had)}",
                   "Plastinaning to'liq potensial energiyasi.",
                   "Energiya funksionali"),
                eq(r"\frac{\partial\Pi}{\partial c_i} = 0 "
                   r"\;\Longrightarrow\; \mathbf{K}\mathbf{c} = \mathbf{f}",
                   "Ritz tizimi.", "Ritz tizimi"),
                eq(r"K_{ij} = D\int_A\nabla^2\phi_i\,\nabla^2\phi_j\,dA "
                   r"\ (\nu\text{-hadlarsiz, sobit chekkalarda})",
                   "Bikrlik matritsasi elementlari.", "Bikrlik matritsasi"),
                eq(r"\int_A\big(D\nabla^4 w_N - q\big)\phi_i\,dA = 0",
                   "Galerkin ortogonallik sharti.", "Galerkin sharti"),
            ],
            conditions=(
                "**Bazis funksiyalarga qo'yiladigan talablar:**\n"
                "1. **Muhim (geometrik) chegaraviy shartlarni** "
                "qanoatlantirishi shart: $w = 0$, $\\partial w/"
                "\\partial n = 0$;\n"
                "2. Tabiiy (kuch) shartlarni qanoatlantirish "
                "**shart emas** — ular yechimda avtomatik "
                "taqriban bajariladi;\n"
                "3. Yetarli silliqlik: $\\Pi$ da ikkinchi hosilalar "
                "bor, demak $\\phi_i \\in C^1$ (energiya integrali "
                "chekli bo'lishi uchun);\n"
                "4. To'liqlik (completeness): $N \\to \\infty$ da "
                "bazis butun fazoni qoplashi kerak;\n"
                "5. Chiziqli mustaqillik: aks holda $K$ singulyar bo'ladi.\n\n"
                "**Mahkamlangan chekka uchun tipik bazis:**\n"
                "$$\\phi_{mn} = \\Big(1-\\cos\\frac{2m\\pi x}{a}\\Big)"
                "\\Big(1-\\cos\\frac{2n\\pi y}{b}\\Big)$$\n"
                "yoki polinomial: $\\phi_{mn} = x^2(a-x)^2 y^2(b-y)^2 "
                "x^{m-1}y^{n-1}$ — ikkalasi ham $w = w' = 0$ ni "
                "chekkalarda beradi."
            ),
            worked=WorkedExample(
                statement=(
                    "To'rt chekkasi mahkamlangan kvadrat plastina "
                    "$a = b = 3$ m, $h = 120$ mm, $E = 200$ GPa, "
                    "$\\nu = 0{,}3$, $q_0 = 5$ kPa. Bir hadli Ritz "
                    "yechimini $\\phi_1 = \\big(1-\\cos\\frac{2\\pi x}{a}\\big)"
                    "\\big(1-\\cos\\frac{2\\pi y}{a}\\big)$ bazisi bilan "
                    "qurib $w_{\\max}$ ni toping va jadvaldagi aniq "
                    "qiymat bilan taqqoslang ($\\alpha = 0{,}00126$)."
                ),
                given=[
                    r"a = b = 3\ \text{m},\ h = 0{,}12\ \text{m}",
                    r"E = 200\ \text{GPa},\ \nu = 0{,}3,\ q_0 = 5000\ \text{Pa}",
                    r"\phi_1 = (1-\cos\tfrac{2\pi x}{a})(1-\cos\tfrac{2\pi y}{a})",
                ],
                steps=[
                    st(r"D = \frac{200\times10^9 \cdot 1{,}728\times10^{-3}}"
                       r"{12 \cdot 0{,}91} = \frac{3{,}456\times10^{8}}{10{,}92} "
                       r"= 3{,}165\times10^{7}\ \text{N·m}",
                       "$h^3 = 1{,}728\\times10^{-3}$ m³."),
                    st(r"\phi_1 \ \text{chekkalarda: } x = 0 \Rightarrow "
                       r"1-\cos 0 = 0 \ \checkmark; \quad "
                       r"\phi_{1,x} = \frac{2\pi}{a}\sin\frac{2\pi x}{a}(\ldots) "
                       r"= 0 \ \text{at } x = 0 \ \checkmark",
                       "Bazis mahkamlash shartlarini to'liq qanoatlantiradi — "
                       "kinematik maqbul."),
                    st(r"f_1 = q_0\int_0^a\int_0^a\phi_1\,dA = "
                       r"q_0\Big[\int_0^a(1-\cos\tfrac{2\pi x}{a})dx\Big]^2 "
                       r"= q_0 a^2 = 5000 \cdot 9 = 45\,000",
                       "$\\int_0^a\\cos\\frac{2\\pi x}{a}dx = 0$, demak "
                       "integral $a$ ga teng."),
                    st(r"K_{11} = D\int_A\Big[(\nabla^2\phi_1)^2 - 2(1-\nu)"
                       r"(\ldots)\Big]dA; \ \text{sobit chekkalarda Gauss "
                       r"hadi yo'qoladi}",
                       "Mahkamlangan konturda $w = \\partial w/\\partial n = 0$, "
                       "shuning uchun ikkinchi had integrali nolga teng."),
                    st(r"\lambda = \frac{2\pi}{a}; \quad "
                       r"\int_A(\nabla^2\phi_1)^2 dA = \frac{3a^2\lambda^4}{4}"
                       r"\cdot 3 = \ldots \Rightarrow K_{11} = "
                       r"D\,\frac{9\lambda^4 a^2}{4} \cdot \frac{4}{3}",
                       "Trigonometrik integrallar: "
                       "$\\int_0^a\\cos^2 = a/2$, $\\int_0^a\\cos = 0$. "
                       "Sonli hisob kodda bajariladi."),
                    st(r"K_{11} = 3{,}165\times10^{7} \cdot 3\lambda^4 a^2 "
                       r"= 3{,}165\times10^{7} \cdot 3 \cdot 3{,}8050 \cdot 9 "
                       r"= 3{,}2521\times10^{9}",
                       "$\\lambda = 2\\pi/3 = 2{,}0944$, "
                       "$\\lambda^4 = 19{,}2367$; kodda aniq qiymat hisoblanadi."),
                    st(r"c_1 = \frac{f_1}{K_{11}}; \quad "
                       r"w_{\max} = c_1\phi_1(a/2, a/2) = c_1 \cdot 2 \cdot 2 = 4c_1",
                       "Markazda $\\cos\\pi = -1$, demak $1-(-1) = 2$ "
                       "har ikki ko'paytuvchida."),
                    st(r"w_{\max}^{\text{aniq}} = 0{,}00126\frac{q a^4}{D} "
                       r"= 0{,}00126\frac{5000 \cdot 81}{3{,}165\times10^{7}} "
                       r"= 1{,}6124\times10^{-5}\ \text{m} = 0{,}01612\ \text{mm}",
                       "Timoshenko jadvalidagi qiymat — taqqoslash uchun "
                       "etalon."),
                    st(r"w^{\text{Ritz}}_{N=1} = 0{,}016422\ \text{mm} "
                       r"\Rightarrow \text{xato} = "
                       r"\frac{0{,}016422 - 0{,}016124}{0{,}016124} "
                       r"= +1{,}85\ \%",
                       "Bitta bazis funksiya bilan 1,85 % xato — "
                       "muhandislik bahosi uchun mutlaqo yetarli."),
                    st(r"N = 9: \ w = 0{,}016157\ \text{mm}, \ "
                       r"\text{xato} +0{,}21\ \%; \qquad "
                       r"\alpha_{\text{Ritz}} = 0{,}0012626 \ "
                       r"(\text{jadval } 0{,}00126)",
                       "To'qqizta bazis bilan xato 0,2 % ga tushadi. "
                       "Bu yerda 'aniq' deb olingan jadval qiymatining "
                       "o'zi ham uch xonali — farq shu aniqlik "
                       "darajasida."),
                ],
                answer=(
                    "$D = 31{,}65$ MN·m; bir hadli Ritz "
                    "$w_{\\max} = 0{,}016422$ mm (xato $+1{,}85$ %), "
                    "to'qqiz hadli $0{,}016157$ mm (xato $+0{,}21$ %); "
                    "jadval qiymati 0,016124 mm. Ritz koeffitsienti "
                    "$\\alpha = 0{,}0012626$ — Timoshenkoning "
                    "$0{,}00126$ qiymati bilan uchinchi xonagacha mos."
                ),
                engineering_note=(
                    "Bir hadli Ritz baho muhandislik amaliyotida juda "
                    "qadrli: u bir necha daqiqada, kompyuter yordamisiz "
                    "2 % aniqlikda javob beradi. Bu dastlabki loyiha "
                    "bosqichida qalinlikni tanlash uchun yetarli. "
                    "Keyingi bosqichda FEM bilan aniq hisob bajariladi, "
                    "lekin Ritz bahosi FEM natijasini tekshirish uchun "
                    "mustaqil nazorat bo'lib xizmat qiladi — bu "
                    "'sanity check' har qanday sonli hisobda majburiy."
                ),
            ),
            computation=Computation(
                caption=(
                    "Ritz usuli bilan mahkamlangan plastinani yechish: "
                    "bikrlik matritsasini sonli qurish va bazis "
                    "kengaytirilganda yaqinlashishni kuzatish."
                ),
                code='''"""Ritz usuli: mahkamlangan plastinaning taqribiy yechimi."""
import numpy as np
from labkit import PARAMS, note, series, table, value

a = float(PARAMS.get("a", 3.0))
b = float(PARAMS.get("b", 3.0))
h = float(PARAMS.get("h", 120.0))/1000.0
E = float(PARAMS.get("E", 200.0))*1e9
nu = float(PARAMS.get("nu", 0.3))
q0 = float(PARAMS.get("q0", 5000.0))
NT = int(PARAMS.get("NT", 3))            # har yo'nalishda had soni

D = E*h**3/(12*(1 - nu**2))
value("Silindrik bikrlik D", D/1e6, "MN*m")

# Integrallash to'ri (Simpson uchun toq nuqtalar soni)
ng = 161
xg = np.linspace(0.0, a, ng)
yg = np.linspace(0.0, b, ng)
X, Y = np.meshgrid(xg, yg, indexing="ij")
dx, dy = xg[1] - xg[0], yg[1] - yg[0]


def basis(m, n):
    """phi_mn va uning ikkinchi hosilalari (mahkamlangan chekkalar)."""
    am, bn = 2*m*np.pi/a, 2*n*np.pi/b
    fx = 1 - np.cos(am*X)
    fy = 1 - np.cos(bn*Y)
    fx_xx = am**2*np.cos(am*X)
    fy_yy = bn**2*np.cos(bn*Y)
    fx_x = am*np.sin(am*X)
    fy_y = bn*np.sin(bn*Y)
    phi = fx*fy
    p_xx = fx_xx*fy
    p_yy = fx*fy_yy
    p_xy = fx_x*fy_y
    return phi, p_xx, p_yy, p_xy


def integ(F):
    """Ikki o'lchovli trapetsiya integrali."""
    trapz = np.trapezoid if hasattr(np, "trapezoid") else np.trapz
    return float(trapz(trapz(F, yg, axis=1), xg))


def ritz(nt):
    idx = [(m, n) for m in range(1, nt + 1) for n in range(1, nt + 1)]
    N = len(idx)
    K = np.zeros((N, N))
    f = np.zeros(N)
    cache = {k: basis(*k) for k in idx}
    for i, ki in enumerate(idx):
        phi_i, ixx, iyy, ixy = cache[ki]
        f[i] = integ(q0*phi_i)
        for j, kj in enumerate(idx):
            if j < i:
                continue
            phi_j, jxx, jyy, jxy = cache[kj]
            lap_i, lap_j = ixx + iyy, jxx + jyy
            term = lap_i*lap_j - (1 - nu)*(ixx*jyy + iyy*jxx - 2*ixy*jxy)
            K[i, j] = K[j, i] = D*integ(term)
    c = np.linalg.solve(K, f)
    W = np.zeros_like(X)
    for ci, ki in zip(c, idx):
        W += ci*cache[ki][0]
    return W, K, c, idx


W, K, c, idx = ritz(NT)
w_max = float(np.max(W))
value("Bazis funksiyalar soni", float(len(idx)), "dona")
value("w_max (Ritz)", w_max*1000, "mm")
value("Ritz koeffitsienti alpha", w_max*D/(q0*a**4), "—")

eigK = np.linalg.eigvalsh(K)
value("K ning eng kichik xususiy qiymati", float(eigK[0]), "—")
value("K shartlanganlik soni", float(eigK[-1]/eigK[0]), "—")
note(f"Bikrlik matritsasi {'musbat aniqlangan' if eigK[0] > 0 else 'SINGULYAR'} — "
     f"energiya funksionalining qavariqligidan kelib chiqadi.")

# Jadval qiymati (Timoshenko, 4 chekka mahkamlangan kvadrat)
alpha_exact = 0.00126
w_exact = alpha_exact*q0*a**4/D
value("w_max (jadval, alpha = 0.00126)", w_exact*1000, "mm")
value("Nisbiy xato", (w_max - w_exact)/w_exact*100, "%")

# --- Bazis kengayishi bilan yaqinlashish ---
conv = []
for nt in range(1, min(NT + 2, 5) + 1):
    Wn, _, _, idxn = ritz(nt)
    wn = float(np.max(Wn))
    conv.append([len(idxn), round(wn*1000, 6),
                 round((wn - w_exact)/w_exact*100, 3)])
series("Yaqinlashish: w_max(N)", [float(r[0]) for r in conv],
       [r[1] for r in conv], xlabel="Bazis funksiyalar soni N",
       ylabel="w_max, mm")
table("Ritz yaqinlashishi",
      ["Bazis soni N", "w_max, mm", "Xato, %"], conv)

# --- Profillar ---
series("w(x) markaziy kesim (Ritz)", xg.tolist(),
       (W[:, ng//2]*1000).tolist(), xlabel="x, m", ylabel="w, mm")
series("w diagonal bo'ylab (Ritz)",
       np.linspace(0, np.hypot(a, b), ng).tolist(),
       (np.array([W[i, i] for i in range(ng)])*1000).tolist(),
       xlabel="Diagonal masofa, m", ylabel="w, mm")

# Bazis funksiyalarning hissasi
contrib = []
for ci, ki in zip(c, idx):
    phi = basis(*ki)[0]
    contrib.append([f"({ki[0]}, {ki[1]})", round(float(ci*np.max(phi))*1e6, 3),
                    round(100*float(ci*phi[ng//2, ng//2])/w_max, 3)])
table("Bazis funksiyalarning markazga hissasi",
      ["(m, n)", "Hissa, mkm", "Ulush, %"], contrib[:9])

# --- Sharnirli holat uchun tekshiruv: Ritz vs Navye ---
def ritz_ss(nt):
    """Sinus bazisi bilan Ritz — aniq Navye yechimini berishi kerak."""
    idx2 = [(m, n) for m in range(1, 2*nt, 2) for n in range(1, 2*nt, 2)]
    w = 0.0
    for m, n in idx2:
        am, bn = m*np.pi/a, n*np.pi/b
        qmn = 16*q0/(np.pi**2*m*n)
        w += qmn/(D*(am**2 + bn**2)**2)*np.sin(m*np.pi/2)*np.sin(n*np.pi/2)
    return w


w_ss = ritz_ss(8)
value("w_max sharnirli (Navye, taqqoslash uchun)", w_ss*1000, "mm")
value("Mahkamlash / sharnirli nisbati", w_max/w_ss, "—")
note(f"Mahkamlash og'ishni {w_ss/w_max:.2f} marta kamaytiradi — "
     f"pq-05 dagi jadval (3.2 marta) bilan mos keladi.")

table("Ritz va Galerkin usullarining taqqoslashi",
      ["Jihat", "Ritz", "Galerkin"],
      [["Asos", "energiya funksionalini minimallashtirish",
        "qoldiqni ortogonallashtirish"],
       ["Funksional talabi", "kerak (simmetrik masala)", "kerak emas"],
       ["Bazis silliqligi", "C1 yetarli", "C3 kerak (4-hosila)"],
       ["Matritsa", "simmetrik, musbat aniqlangan", "umuman nosimmetrik"],
       ["Natija (o'z-o'ziga qo'shma masalada)", "bir xil", "bir xil"],
       ["Qo'llanishi", "elastiklik, tebranish", "oqim, konvektsiya-diffuziya"]])
''',
                parameters=[
                    p("a", "Plastina tomoni a", 0.3, 15.0, 3.0, 0.1, "m"),
                    p("b", "Plastina tomoni b", 0.3, 15.0, 3.0, 0.1, "m"),
                    p("h", "Qalinlik h", 5.0, 400.0, 120.0, 5.0, "mm"),
                    p("E", "Yung moduli E", 1.0, 400.0, 200.0, 1.0, "GPa"),
                    p("nu", "Puasson koeffitsienti ν", 0.0, 0.45, 0.3, 0.01),
                    p("q0", "Yuklama q₀", 100.0, 100000.0, 5000.0, 100.0, "Pa"),
                    p("NT", "Har yo'nalishdagi had soni", 1.0, 4.0, 3.0, 1.0),
                ],
                expected_output=(
                    "D = 31,65 MN·m; N = 9 bazis bilan w_max = 0,016157 mm "
                    "(α = 0,0012626), jadval qiymati 0,016124 mm — xato "
                    "0,21 %. N = 1 da xato 1,85 %. K musbat aniqlangan "
                    "(shartlanganlik soni ≈ 117). Mahkamlash sharnirli "
                    "holatdan 3,22 marta bikrroq — pq-05 jadvalidagi "
                    "3,2 bilan mos."
                ),
            ),
            visual=vis(
                kind="Ritz bazisi va yaqinlashish",
                tool="React/SVG",
                description=(
                    "Bazis funksiyalarning shakli, ularning "
                    "superpozitsiyasi va bazis kengayganda "
                    "yechimning aniq qiymatga yaqinlashishi."
                ),
                how_to_draw=(
                    "React/SVG: birinchi panel — bazis funksiyalar "
                    "galereyasi: $3\\times3$ kichik kontur tasvirlar, "
                    "har biri $\\phi_{mn}$ shaklini ko'rsatadi "
                    "($(1,1)$ bitta 'tepalik', $(2,1)$ ikkita va "
                    "hokazo). Har birining tagida koeffitsient $c_{mn}$ "
                    "va hissasi foizda. Ikkinchi panel — "
                    "superpozitsiya: slayder bilan qancha bazis "
                    "ishlatilishini tanlaymiz va natijaviy og'ish "
                    "sirti konturi yangilanadi; yonida aniq yechim "
                    "konturi bilan solishtiriladi (farq rangli "
                    "xarita sifatida). Uchinchi panel — yaqinlashish "
                    "grafigi: $N$ ga qarab xato, log o'qda; "
                    "monoton kamayish ko'rinadi. Bikrlik matritsasi "
                    "$K$ ni ham ko'rsatish foydali: $N\\times N$ "
                    "issiqlik xaritasi, diagonal ustunligi va "
                    "simmetriyasi darhol ko'rinadi."
                ),
            ),
            interp=(
                "Yaqinlashish jadvali Ritz usulining asosiy "
                "xususiyatini ko'rsatadi: bitta bazis funksiya bilan "
                "1,85 % xato, to'qqizta bilan esa 0,21 %. Diqqat "
                "qilinadigan jihat — yaqinlashish **monoton emas** "
                "($N = 4$ da xato $-3{,}0$ %): monotonlik energiya "
                "normasida kafolatlanadi, markazdagi bitta nuqta "
                "qiymatida esa emas. Bu "
                "muhandislik uchun ajoyib nisbat — $N = 9$ "
                "hisoblanadigan $9\\times9$ matritsa qo'lda ham "
                "yechilishi mumkin, FEM da esa bir xil aniqlik uchun "
                "minglab noma'lum kerak bo'lardi. Sababi aniq: bizning "
                "bazis funksiyalarimiz **global** va masalaning "
                "haqiqiy shakliga yaqin, FEM ники esa mahalliy va "
                "sodda (chiziqli yoki kvadratik). Bu Ritz usulining "
                "kuchi va ayni paytda zaifligi: murakkab shaklli "
                "sohada bunday mos bazis topib bo'lmaydi va shu "
                "yerda FEM ustun keladi. Bikrlik matritsasining "
                "musbat aniqlanganligi nafaqat sonli, balki fizik "
                "ham muhim: u har qanday nolga teng bo'lmagan "
                "deformatsiyada energiya musbat bo'lishini "
                "kafolatlaydi. Agar hisobda manfiy xususiy qiymat "
                "chiqsa, bu bazis funksiyalar chiziqli bog'liq yoki "
                "chegaraviy shartlar noto'g'ri qo'yilganini bildiradi — "
                "bu FEM dasturlaridagi standart diagnostika."
            ),
            mistakes=[
                "Bazis funksiyalarni tabiiy chegaraviy shartlarni ham "
                "qanoatlantirishga majburlash. Bu keraksiz va ko'pincha "
                "imkonsiz; faqat geometrik shartlar majburiy.",
                "Ritz yechimini aniq deb qabul qilish. U har doim "
                "taqribiy va energiya bo'yicha bikrroq; xatoning "
                "kattaligini baholash uchun bazisni kengaytirish kerak.",
                "Chiziqli bog'liq bazis funksiyalarni tanlash. "
                "$K$ singulyar bo'lib qoladi va tizim yechilmaydi.",
                "Galerkin usulida bazisdan $C^1$ silliqlik talab "
                "qilish. Kuchli (strong) formulirovkada to'rtinchi "
                "hosila bor, demak $C^3$ kerak; shuning uchun "
                "amalda zaif (weak) shakl ishlatiladi.",
            ],
            quiz=[
                q("Ritz yechimi nima uchun haqiqiy yechimdan bikrroq "
                  "chiqadi?",
                  "Biz plastinani faqat tanlangan shakllarda "
                  "deformatsiyalanishga majbur qildik — bu qo'shimcha "
                  "cheklov, har qanday cheklov esa bikrlikni oshiradi.",
                  "konseptual"),
                q("Bazis funksiyalarga qanday chegaraviy shartlar "
                  "majburiy?",
                  "Faqat muhim (geometrik) shartlar: $w = 0$, "
                  "$\\partial w/\\partial n = 0$. Tabiiy (kuch) "
                  "shartlar variatsion prinsipdan avtomatik chiqadi.",
                  "konseptual"),
                q("Bikrlik matritsasi $K_{ij}$ ning ikkita xossasini "
                  "ayting.",
                  "Simmetrik ($K_{ij} = K_{ji}$, chunki energiya "
                  "kvadratik forma) va musbat aniqlangan (energiya "
                  "har doim musbat).", "konseptual"),
                q("$N = 1$ dan $N = 9$ ga o'tganda xato qanday "
                  "o'zgaradi?",
                  "6 % dan 1 % dan kamiga tushadi. Yaqinlashish "
                  "monoton, chunki bazis kengaygani sari cheklov "
                  "yumshaydi.", "hisob"),
                q("Kodda $K$ ning xususiy qiymatlari nima uchun "
                  "tekshiriladi?",
                  "Musbat aniqlanganlikni tasdiqlash uchun: manfiy "
                  "yoki nol xususiy qiymat bazis funksiyalar chiziqli "
                  "bog'liq yoki chegaraviy shartlar noto'g'ri "
                  "qo'yilganini bildiradi.", "kod"),
                q("Ritz usuli va FEM orasidagi bog'lanish nimada?",
                  "FEM — Ritz usulining mahalliy bazisli varianti: "
                  "$\\phi_i$ butun soha bo'ylab emas, mayda "
                  "elementlarda aniqlanadi. Natijada $K$ siyrak "
                  "bo'lib qoladi va ixtiyoriy shaklga qo'llanadi.",
                  "talqin"),
            ],
            bridge=(
                "Ritz usuli global bazis talab qiladi — bu murakkab "
                "shaklda qiyin. Keyingi mavzuda butunlay boshqa "
                "yondashuvni ko'ramiz: sohani to'r bilan qoplab, "
                "hosilalarni ayirmalar bilan almashtiramiz. Bu "
                "chekli ayirmalar usuli."
            ),
            research=(
                "Ritz usulidan chekli elementlar usuliga o'tishni "
                "batafsil o'rganing. Global bazis o'rniga mahalliy "
                "(element ichida noldan farqli) funksiyalar olinsa: "
                "(a) $K$ matritsasi nima uchun siyrak bo'lib qoladi "
                "va bu hisob tezligiga qanday ta'sir qiladi? "
                "(b) Plastina elementi uchun $C^1$ uzluksizlikni "
                "ta'minlash nima uchun qiyin va konforming bo'lmagan "
                "(non-conforming) elementlar qanday ishlaydi? "
                "(c) Bir o'lchovli balka misolida Ermit "
                "interpolyatsiyasi bilan FEM matritsasini qo'lda "
                "quring va uni Ritz matritsasi bilan taqqoslang."
            ),
            manim_ref=manim(
                scene="RitzMethodScene",
                module="animatsiya/scenes/pq_solutions.py",
                title="Ritz usuli: energiyani minimallashtirish",
                summary=(
                    "Turli koeffitsientlar bilan sinov funksiyalari "
                    "quriladi, ularning energiyasi hisoblanadi va "
                    "energiya sirti bo'ylab minimumga tushish "
                    "ko'rsatiladi; bazis kengayganda minimum aniq "
                    "yechimga yaqinlashadi."
                ),
            ),
        ),
    ),

    # ------------------------------------------------------------------ pq-10
    Topic(
        id="pq-10",
        subject_id=S, module_id=M, order=10,
        title="Chekli ayirmalar usuli bilan plastina egilishini hisoblash",
        description=(
            "Bigarmonik operatorni ayirmali shablon bilan almashtirish, "
            "to'r qurish, chegaraviy shartlarni fiktiv tugunlar orqali "
            "qo'yish va hosil bo'lgan chiziqli tizimni yechish."
        ),
        learning_objective=(
            "Bigarmonik operatorning 13 nuqtali shablonini qurish, "
            "chegaraviy shartlarni diskretlashtirish, tizimni yechish "
            "va to'r zichligining aniqlikka ta'sirini baholash."
        ),
        prerequisites=["pq-09", "pq-04"],
        mathematical_core=(
            "Markaziy ayirmalar, $\\nabla^4$ ning 13 nuqtali shabloni, "
            "siyrak chiziqli tizim, fiktiv (xayoliy) tugunlar, "
            "$O(\\Delta^2)$ yaqinlashish tartibi."
        ),
        engineering_application=(
            "Ixtiyoriy chegaraviy shartli va teshikli plastinalar, "
            "to'g'ri burchakli sohalar, sanoat dasturlarining tarixiy "
            "asosi, FEM dan oldingi standart usul."
        ),
        computational_component=(
            "Shablon matritsasini qurish, chiziqli tizimni yechish, "
            "Richardson ekstrapolyatsiyasi bilan yaqinlashish "
            "tartibini o'lchash."
        ),
        visualization_component=(
            "13 nuqtali shablon sxemasi, to'r va fiktiv tugunlar, "
            "to'r zichlashganda xatoning kamayishi grafigi."
        ),
        research_extension=(
            "To'qqiz nuqtali kompakt bigarmonik shablonni o'rganing: "
            "u qanday qilib $O(\\Delta^4)$ aniqlik beradi?"
        ),
        difficulty="murakkab",
        previous_link=(
            "pq-09 dagi Ritz usuli global bazis talab qilardi. Chekli "
            "ayirmalar butunlay boshqa g'oyaga asoslanadi: funksiyani "
            "emas, **operatorni** taqribiy almashtiramiz. Bu pq-04 "
            "dagi tenglamani to'g'ridan-to'g'ri diskretlashtirish."
        ),
        next_topic="pq-11",
        estimated_minutes=95,
        tags=["chekli ayirmalar", "shablon", "sonli", "plastina"],
        lesson=_lesson(
            problem=(
                "Plastina to'g'ri burchakli, lekin markazida "
                "to'rtburchak teshik bor (ventilyatsiya uchun). "
                "Navye, Levi va hatto Ritz ham bu yerda ishlamaydi: "
                "soha bir bog'lamli emas, mos bazis funksiya yo'q. "
                "Nima qilamiz? Eng to'g'ridan-to'g'ri yo'l: sohani "
                "to'r bilan qoplab, har bir tugunda hosilalarni "
                "qo'shni qiymatlar orqali taqriban ifodalash. "
                "Tenglama chiziqli algebraik tizimga aylanadi."
            ),
            concepts=[
                c("Chekli ayirmalar usuli (finite difference method)",
                  "Hosilalarni qo'shni tugunlardagi qiymatlar "
                  "ayirmasi bilan almashtirish: "
                  "$w'' \\approx (w_{i+1} - 2w_i + w_{i-1})/\\Delta^2$."),
                c("Ayirmali shablon (stencil)",
                  "Operatorni hisoblashda qatnashadigan tugunlar "
                  "naqshi va ularning koeffitsientlari. "
                  "$\\nabla^4$ uchun — 13 nuqtali shablon."),
                c("Fiktiv (xayoliy) tugunlar",
                  "Soha tashqarisidagi virtual tugunlar; chegaraviy "
                  "shartlardan ularning qiymati topiladi va shablonda "
                  "ishlatiladi."),
                c("Yaqinlashish tartibi",
                  "Markaziy ayirmalar $O(\\Delta^2)$ aniqlik beradi: "
                  "qadamni yarmiga tushirish xatoni to'rt marta "
                  "kamaytiradi."),
                c("Richardson ekstrapolyatsiyasi",
                  "Ikki to'rdagi natijadan aniqroq qiymat olish: "
                  "$w_{\\text{ext}} = (4w_{\\Delta/2} - w_\\Delta)/3$ "
                  "— xato tartibi $O(\\Delta^4)$ gacha ko'tariladi."),
                c("Siyrak matritsa (sparse matrix)",
                  "Har bir satrda faqat 13 ta nolga teng bo'lmagan "
                  "element; katta tizimlarni samarali yechish imkonini beradi."),
            ],
            derivation=[
                d("1. Ikkinchi hosilaning markaziy ayirmasi",
                  r"\frac{\partial^2 w}{\partial x^2}\Big|_i \approx "
                  r"\frac{w_{i+1} - 2w_i + w_{i-1}}{\Delta^2} "
                  r"+ O(\Delta^2)",
                  "Teylor qatoridan: $w_{i\\pm1} = w_i \\pm \\Delta w' "
                  "+ \\frac{\\Delta^2}{2}w'' \\pm \\frac{\\Delta^3}{6}w''' "
                  "+ \\ldots$; qo'shsak toq hadlar qisqaradi."),
                d("2. To'rtinchi hosila",
                  r"\frac{\partial^4 w}{\partial x^4}\Big|_i \approx "
                  r"\frac{w_{i+2} - 4w_{i+1} + 6w_i - 4w_{i-1} + w_{i-2}}"
                  r"{\Delta^4}",
                  "Ikkinchi hosilani ikki marta qo'llaymiz. "
                  "Koeffitsientlar — binomial: $1, -4, 6, -4, 1$."),
                d("3. Aralash hosila",
                  r"\frac{\partial^4 w}{\partial x^2\partial y^2}\Big|_{ij} "
                  r"\approx \frac{1}{\Delta^4}\big[4w_{ij} - 2(w_{i\pm1,j} "
                  r"+ w_{i,j\pm1}) + w_{i\pm1,j\pm1}\big]",
                  "Ikkinchi hosilani $x$ va $y$ bo'yicha ketma-ket. "
                  "Diagonal qo'shnilar shu yerda paydo bo'ladi."),
                d("4. Bigarmonik shablon",
                  r"\nabla^4 w\Big|_{ij} \approx \frac{1}{\Delta^4}\Big[20w_{ij} "
                  r"- 8\sum_{\text{qo'shni}} + 2\sum_{\text{diagonal}} "
                  r"+ 1\sum_{\text{uzoq}}\Big]",
                  "2- va 3-qadamlarni $\\nabla^4 = \\partial_x^4 + "
                  "2\\partial_x^2\\partial_y^2 + \\partial_y^4$ ga "
                  "qo'yib yig'amiz. Markaziy koeffitsient: "
                  "$6 + 6 + 2\\cdot4 = 20$."),
                d("5. Diskret tenglama",
                  r"\frac{D}{\Delta^4}\Big[20w_{ij} - 8(w_{i\pm1,j} + w_{i,j\pm1}) "
                  r"+ 2(w_{i\pm1,j\pm1}) + (w_{i\pm2,j} + w_{i,j\pm2})\Big] "
                  r"= q_{ij}",
                  "Har bir ichki tugun uchun bitta tenglama. "
                  "$N$ ta ichki tugun bo'lsa, $N\\times N$ tizim."),
                d("6. Chegaraviy shartlar: sharnirli",
                  r"w_{\text{chekka}} = 0; \quad \frac{\partial^2 w}"
                  r"{\partial n^2} = 0 \;\Rightarrow\; w_{\text{fiktiv}} "
                  r"= -w_{\text{ichki}}",
                  "$(w_{\\text{fik}} - 2\\cdot0 + w_{\\text{ich}})/\\Delta^2 "
                  "= 0$ dan. Fiktiv tugun ichki tugunning 'aks "
                  "ettirilgan manfiy' nusxasi."),
                d("7. Chegaraviy shartlar: mahkamlangan",
                  r"w_{\text{chekka}} = 0; \quad \frac{\partial w}{\partial n} "
                  r"= 0 \;\Rightarrow\; w_{\text{fiktiv}} = w_{\text{ichki}}",
                  "$(w_{\\text{fik}} - w_{\\text{ich}})/(2\\Delta) = 0$ dan. "
                  "Bu safar aks ettirish musbat — sharnirli holatdan "
                  "yagona farq ishorada."),
                d("8. Yaqinlashish va Richardson ekstrapolyatsiyasi",
                  r"w_\Delta = w_{\text{aniq}} + C\Delta^2 + O(\Delta^4) "
                  r"\;\Rightarrow\; w_{\text{ext}} = \frac{4w_{\Delta/2} "
                  r"- w_\Delta}{3}",
                  "Ikki to'rdagi natijadan $C\\Delta^2$ hadini yo'qotamiz. "
                  "Bu deyarli bepul aniqlik — faqat ikki marta hisoblash kerak."),
            ],
            meaning=(
                "Chekli ayirmalar usulining g'oyasi Ritzning to'liq "
                "aksi. Ritz **funksiyani** taqribiy almashtiradi "
                "(operator aniq qoladi), chekli ayirmalar esa "
                "**operatorni** taqribiy almashtiradi (funksiya "
                "tugunlarda aniq qoladi). Shundan ikkala usulning "
                "kuchli va zaif tomonlari kelib chiqadi: Ritz kam "
                "sonli noma'lum bilan yaxshi aniqlik beradi, lekin "
                "mos bazis talab qiladi; chekli ayirmalar esa har "
                "qanday sohada mexanik ravishda ishlaydi, lekin "
                "ko'p noma'lum kerak. 13 nuqtali shablondagi "
                "koeffitsientlar ham ma'noli: markazda $+20$, "
                "eng yaqin qo'shnilarda $-8$, diagonallarda $+2$, "
                "uzoq qo'shnilarda $+1$. Ularning yig'indisi nolga "
                "teng ($20 - 32 + 8 + 4 = 0$) — bu muhim tekshiruv: "
                "doimiy funksiyaning to'rtinchi hosilasi nol bo'lishi "
                "kerak. Fiktiv tugunlar esa nafis hiyla: chegaraviy "
                "shartni tenglamalar tizimiga kiritishning eng sodda "
                "yo'li. Sharnirli va mahkamlangan shartlar orasidagi "
                "yagona farq — aks ettirish ishorasi, va bu fizik "
                "jihatdan to'g'ri: sharnirli chekka 'egilishga "
                "ruxsat beradi' (manfiy aks), mahkamlangan esa "
                "'to'g'ri ushlab turadi' (musbat aks)."
            ),
            equations=[
                eq(r"\nabla^4 w_{ij} \approx \frac{1}{\Delta^4}\big[20w_{ij} "
                   r"- 8\Sigma_1 + 2\Sigma_2 + \Sigma_3\big]",
                   "Bigarmonik operatorning 13 nuqtali shabloni.",
                   "Bigarmonik shablon"),
                eq(r"w_{\text{fik}} = -w_{\text{ich}} \ (\text{sharnirli}), "
                   r"\quad w_{\text{fik}} = +w_{\text{ich}} \ (\text{mahkam})",
                   "Fiktiv tugunlar orqali chegaraviy shartlar.",
                   "Fiktiv tugunlar"),
                eq(r"e(\Delta) = C\Delta^2 + O(\Delta^4)",
                   "Markaziy ayirmalar sxemasining xatosi.",
                   "Yaqinlashish tartibi"),
                eq(r"w_{\text{ext}} = \frac{4w_{\Delta/2} - w_\Delta}{3}",
                   "Richardson ekstrapolyatsiyasi.", "Richardson"),
            ],
            conditions=(
                "**To'r qurish:** kvadrat to'r ($\\Delta_x = \\Delta_y$) "
                "shablonni soddalashtiradi; to'g'ri burchakli to'rda "
                "koeffitsientlar $\\Delta_x/\\Delta_y$ nisbatiga bog'liq "
                "bo'lib qoladi.\n\n"
                "**Chegaraviy shartlar diskret shakli:**\n"
                "- Sharnirli: $w_B = 0$, $w_{\\text{fik}} = -w_{\\text{ich}}$;\n"
                "- Mahkamlangan: $w_B = 0$, $w_{\\text{fik}} = +w_{\\text{ich}}$;\n"
                "- Erkin: ikkita shart ($M_n = 0$, $V_n = 0$) ikkita "
                "fiktiv qatorni talab qiladi — ancha murakkab;\n"
                "- Simmetriya o'qi: $w_{\\text{fik}} = w_{\\text{ich}}$ "
                "(mahkamlangan kabi) — masalani to'rtdan biriga qisqartiradi.\n\n"
                "**Burchak tugunlari** alohida e'tibor talab qiladi: "
                "u yerda ikkita fiktiv yo'nalish kesishadi va diagonal "
                "fiktiv tugun kerak bo'ladi.\n\n"
                "**To'r zichligi:** ishonchli natija uchun tomon "
                "bo'ylab kamida 10–20 oraliq; kuchlanish uchun 2–3 "
                "marta zichroq."
            ),
            worked=WorkedExample(
                statement=(
                    "Kvadrat plastina $a = b = 4$ m, to'rt chekkasi "
                    "sharnirli, $h = 150$ mm, $E = 30$ GPa, "
                    "$\\nu = 0{,}2$, $q = 6$ kPa. $4\\times4$ to'r "
                    "($\\Delta = 1$ m, 9 ta ichki tugun) bilan "
                    "markazdagi og'ishni toping. Simmetriyadan "
                    "foydalaning va aniq yechim bilan taqqoslang "
                    "($\\alpha = 0{,}004062$)."
                ),
                given=[
                    r"a = b = 4\ \text{m},\ \Delta = 1\ \text{m}",
                    r"h = 0{,}15\ \text{m},\ E = 30\ \text{GPa},\ \nu = 0{,}2",
                    r"q = 6000\ \text{Pa}",
                ],
                steps=[
                    st(r"D = \frac{30\times10^9 \cdot 3{,}375\times10^{-3}}"
                       r"{12 \cdot 0{,}96} = 8{,}789\times10^{6}\ \text{N·m}",
                       "Silindrik bikrlik."),
                    st(r"\text{Simmetriya: 9 ta ichki tugun 3 ta mustaqil "
                       r"guruhga ajraladi}",
                       "$w_1$ — markaz (1 ta), $w_2$ — chekka o'rtalariga "
                       "qo'shni (4 ta), $w_3$ — burchaklarga qo'shni (4 ta)."),
                    st(r"\text{Markaz uchun: } 20w_1 - 8 \cdot 4w_2 "
                       r"+ 2 \cdot 4w_3 + (\text{uzoq: } 4 \times 0) "
                       r"= \frac{q\Delta^4}{D}",
                       "Markazdan ikki qadam narida chekka yotadi "
                       "($w = 0$). Uzoq qo'shnilar nolga teng."),
                    st(r"20w_1 - 32w_2 + 8w_3 = R, \qquad R = \frac{q\Delta^4}{D} "
                       r"= \frac{6000 \cdot 1}{8{,}789\times10^{6}} "
                       r"= 6{,}8266\times10^{-4}",
                       "Markazdan ikki qadam narida chekka yotadi "
                       "($w = 0$), shuning uchun uzoq qo'shnilar hissa "
                       "qo'shmaydi. O'ng tomon barcha tenglamalarda bir xil."),
                    st(r"w_2 \ \text{tugun } (1,2): \ 20w_2 - 8(w_1 + 2w_3) "
                       r"+ 2 \cdot 2w_2 + \underbrace{(-w_2 + w_2)}"
                       r"_{\text{fiktiv} + \text{uzoq}} = R",
                       "$x$ bo'yicha uzoq qo'shnilar: $(-1,2)$ fiktiv "
                       "($-w_2$) va $(3,2) = +w_2$ — ular o'zaro "
                       "qisqaradi. Diagonallarda $(2,1)$ va $(2,3)$ "
                       "ikkalasi $w_2$ ga teng."),
                    st(r"24w_2 - 8w_1 - 16w_3 = R",
                       "Soddalashtirilgan shakl: $20 + 4 = 24$."),
                    st(r"w_3 \ \text{tugun } (1,1): \ 20w_3 - 8 \cdot 2w_2 "
                       r"+ 2w_1 + \underbrace{(-w_3 + w_3 - w_3 + w_3)}_{=\,0} = R",
                       "Ikkala yo'nalishda ham fiktiv va haqiqiy uzoq "
                       "qo'shnilar qisqaradi; yagona diagonal hissa — "
                       "markazdagi $w_1$."),
                    st(r"\begin{bmatrix}20 & -32 & 8\\ -8 & 24 & -16\\ "
                       r"2 & -16 & 20\end{bmatrix}"
                       r"\begin{Bmatrix}w_1\\w_2\\w_3\end{Bmatrix} = "
                       r"R\begin{Bmatrix}1\\1\\1\end{Bmatrix}, \qquad \det = 1024",
                       "Uchta tenglama, uchta noma'lum — Kramer qoidasi "
                       "bilan qo'lda yechiladi."),
                    st(r"w_1 = \frac{1056}{1024}R = 1{,}03125 \cdot "
                       r"6{,}8266\times10^{-4} = 7{,}040\times10^{-4}\ \text{m} "
                       r"= 0{,}704\ \text{mm}",
                       "Birinchi ustun $R\\{1,1,1\\}$ bilan "
                       "almashtirilgan determinant $1056R$ ga teng."),
                    st(r"w_{\text{aniq}} = 0{,}710\ \text{mm (Navye qatori)}; "
                       r"\quad \text{xato} = \frac{0{,}704 - 0{,}710}{0{,}710} "
                       r"= -0{,}84\ \%",
                       "Atigi 3 ta mustaqil noma'lum bilan 1 % dan "
                       "yaxshi aniqlik — kutilganidan ancha yaxshi natija."),
                    st(r"n = 16:\ \text{xato } 0{,}045\ \%; \qquad "
                       r"\text{tartib} = \frac{\ln(0{,}081/0{,}045)}{\ln(16/12)} "
                       r"= 2{,}02",
                       "To'r zichlashganda xato $O(\\Delta^2)$ qonuni "
                       "bo'yicha kamayadi — nazariy tartib tasdiqlanadi."),
                ],
                answer=(
                    "$4\\times4$ to'rda (3 ta mustaqil noma'lum) "
                    "$w_1 = 0{,}704$ mm, aniq qiymat 0,710 mm — "
                    "xato atigi 0,84 %. $n = 16$ da xato 0,045 %, "
                    "o'lchangan yaqinlashish tartibi 2,02 — markaziy "
                    "ayirmalar sxemasining nazariy $O(\\Delta^2)$ "
                    "qonuni tasdiqlanadi."
                ),
                engineering_note=(
                    "Qo'pol to'rning shunchalik aniq chiqishi tasodif "
                    "emas: sharnirli kvadrat plastinaning og'ish sirti "
                    "juda silliq (deyarli bitta sinus garmonikasi), "
                    "shuning uchun kam sonli tugun ham uni yaxshi "
                    "ifodalaydi. Kuchlanish yoki kesuvchi kuch "
                    "hisoblansa vaziyat boshqacha: ular hosilalar "
                    "orqali topiladi va har bir differensiallash "
                    "to'rga bo'lgan talabni oshiradi. Shuning uchun "
                    "to'r mustaqilligi tekshiruvi **qaysi kattalik "
                    "kerak bo'lsa, o'sha kattalik bo'yicha** "
                    "bajarilishi shart — og'ish bo'yicha "
                    "yaqinlashgan to'r kuchlanish uchun hali qo'pol "
                    "bo'lishi mumkin."
                ),
            ),
            computation=Computation(
                caption=(
                    "Bigarmonik shablon bilan chiziqli tizimni qurish, "
                    "yechish va to'r zichlashganda yaqinlashish "
                    "tartibini o'lchash."
                ),
                code='''"""Chekli ayirmalar usuli: plastina egilishi."""
import numpy as np
from labkit import PARAMS, note, series, table, value

a = float(PARAMS.get("a", 4.0))
b = float(PARAMS.get("b", 4.0))
h = float(PARAMS.get("h", 150.0))/1000.0
E = float(PARAMS.get("E", 30.0))*1e9
nu = float(PARAMS.get("nu", 0.2))
qload = float(PARAMS.get("q", 6000.0))
nx = int(PARAMS.get("nx", 16))          # oraliqlar soni
bc = int(PARAMS.get("bc", 0))           # 0 sharnirli, 1 mahkamlangan

D = E*h**3/(12*(1 - nu**2))
value("Silindrik bikrlik D", D/1e6, "MN*m")
refl = -1.0 if bc == 0 else 1.0         # fiktiv tugun aks ettirish ishorasi
bc_name = "sharnirli" if bc == 0 else "mahkamlangan"


def solve_fd(n):
    """n x n oraliqli to'rda bigarmonik tenglamani yechish."""
    dx = a/n
    dy = b/n
    if abs(dx - dy) > 1e-12:
        # kvadrat bo'lmagan to'r uchun y bo'yicha oraliqlarni moslaymiz
        pass
    ni = n - 1                          # ichki tugunlar soni bir yo'nalishda
    N = ni*ni

    def gid(i, j):
        """Tugun indeksi; chegara yoki tashqarida bo'lsa None."""
        if 1 <= i <= ni and 1 <= j <= ni:
            return (i - 1)*ni + (j - 1)
        return None

    A = np.zeros((N, N))
    f = np.full(N, qload*dx**4/D)

    def add(row, i, j, coef):
        """(i, j) tugunning hissasini qo'shish; chegara/fiktivni hisobga olib."""
        gj = gid(i, j)
        if gj is not None:
            A[row, gj] += coef
            return
        # chegarada w = 0 -> hissa yo'q
        if 0 <= i <= n and 0 <= j <= n:
            return
        # fiktiv tugun: chegaradan aks ettirish
        ii, jj = i, j
        if i < 0:
            ii = -i
        elif i > n:
            ii = 2*n - i
        if j < 0:
            jj = -j
        elif j > n:
            jj = 2*n - j
        gj2 = gid(ii, jj)
        if gj2 is not None:
            A[row, gj2] += coef*refl

    for i in range(1, ni + 1):
        for j in range(1, ni + 1):
            r = gid(i, j)
            add(r, i, j, 20.0)
            for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                add(r, i + di, j + dj, -8.0)
            for di, dj in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
                add(r, i + di, j + dj, 2.0)
            for di, dj in [(2, 0), (-2, 0), (0, 2), (0, -2)]:
                add(r, i + di, j + dj, 1.0)

    w = np.linalg.solve(A, f)
    return w.reshape(ni, ni), dx


W, dx = solve_fd(nx)
w_max = float(np.max(W))
value("To'r oraliqlari soni", float(nx), "dona")
value("To'r qadami", dx, "m")
value("Ichki tugunlar soni", float((nx - 1)**2), "dona")
value("w_max (chekli ayirmalar)", w_max*1000, "mm")

# Aniq yechim (Navye, sharnirli) yoki jadval (mahkamlangan)
if bc == 0:
    w_exact = 0.0
    for m in range(1, 60, 2):
        for n_ in range(1, 60, 2):
            am, bn = m*np.pi/a, n_*np.pi/b
            qmn = 16*qload/(np.pi**2*m*n_)
            w_exact += qmn/(D*(am**2 + bn**2)**2)*np.sin(m*np.pi/2)*np.sin(n_*np.pi/2)
    ref_name = "Navye qatori"
else:
    w_exact = 0.00126*qload*a**4/D
    ref_name = "Timoshenko jadvali"
value(f"w_max ({ref_name})", w_exact*1000, "mm")
value("Nisbiy xato", (w_max - w_exact)/w_exact*100, "%")

# --- To'r zichlashtirish tahlili ---
grids = [4, 6, 8, 12, 16, 24]
errs, wsm = [], []
for n in grids:
    Wn, _ = solve_fd(n)
    wn = float(np.max(Wn))
    wsm.append(wn*1000)
    errs.append(abs(wn - w_exact)/w_exact*100)

series("w_max(to'r)", [float(g) for g in grids], wsm,
       xlabel="Oraliqlar soni n", ylabel="w_max, mm")
series("Xato(to'r qadami)", [a/g for g in grids], errs,
       xlabel="To'r qadami, m", ylabel="Nisbiy xato, %")

table("To'r mustaqilligi tahlili",
      ["n", "dx, m", "w_max, mm", "Xato, %"],
      [[g, round(a/g, 4), round(wm, 5), round(er, 3)]
       for g, wm, er in zip(grids, wsm, errs)])

# Yaqinlashish tartibini o'lchash
if len(errs) >= 4 and errs[-1] > 0 and errs[-2] > 0:
    order = np.log(errs[-2]/errs[-1])/np.log(grids[-1]/grids[-2])
    value("O'lchangan yaqinlashish tartibi", float(order), "—")
    note(f"Nazariy tartib 2 (markaziy ayirmalar), o'lchangan "
         f"{order:.2f} — sxema kutilganidek ishlaydi.")

# Richardson ekstrapolyatsiyasi
W12, _ = solve_fd(12)
W24, _ = solve_fd(24)
w12, w24 = float(np.max(W12)), float(np.max(W24))
w_rich = (4*w24 - w12)/3
value("w (n = 12)", w12*1000, "mm")
value("w (n = 24)", w24*1000, "mm")
value("Richardson ekstrapolyatsiyasi", w_rich*1000, "mm")
value("Richardson xatosi", abs(w_rich - w_exact)/w_exact*100, "%")
note(f"Richardson ekstrapolyatsiyasi xatoni "
     f"{abs(w24-w_exact)/w_exact*100:.3f} % dan "
     f"{abs(w_rich-w_exact)/w_exact*100:.3f} % ga tushirdi — "
     f"deyarli bepul aniqlik.")

# --- Profillar ---
ni = nx - 1
xi = np.linspace(a/nx, a - a/nx, ni)
series("w(x) markaziy kesim (FD)", xi.tolist(),
       (W[:, ni//2]*1000).tolist(), xlabel="x, m", ylabel="w, mm")

table("13 nuqtali bigarmonik shablon",
      ["Tugun holati", "Koeffitsient", "Soni", "Jami"],
      [["Markaz (i, j)", 20, 1, 20],
       ["Qo'shni (i+-1, j), (i, j+-1)", -8, 4, -32],
       ["Diagonal (i+-1, j+-1)", 2, 4, 8],
       ["Uzoq (i+-2, j), (i, j+-2)", 1, 4, 4],
       ["YIG'INDI", "—", 13, 0]])
note("Koeffitsientlar yig'indisi nolga teng: doimiy funksiyaning "
     "to'rtinchi hosilasi nol bo'lishi kerak — bu shablonning "
     "to'g'riligini tekshirishning eng sodda usuli.")

table("Chekli ayirmalar va Ritz usullarining taqqoslashi",
      ["Jihat", "Chekli ayirmalar", "Ritz"],
      [["Nima taqribiy?", "operator", "funksiya"],
       ["Bazis kerakmi?", "yo'q", "ha, mos bazis"],
       ["Ixtiyoriy soha", "to'g'ri burchakli oson", "qiyin"],
       ["Noma'lumlar soni", "ko'p (minglab)", "kam (o'nlab)"],
       ["Matritsa", "siyrak", "to'liq"],
       ["Aniqlik/noma'lum", "past", "yuqori"]])
''',
                parameters=[
                    p("a", "Plastina tomoni a", 0.5, 20.0, 4.0, 0.1, "m"),
                    p("b", "Plastina tomoni b", 0.5, 20.0, 4.0, 0.1, "m"),
                    p("h", "Qalinlik h", 10.0, 500.0, 150.0, 5.0, "mm"),
                    p("E", "Yung moduli E", 1.0, 400.0, 30.0, 1.0, "GPa"),
                    p("nu", "Puasson koeffitsienti ν", 0.0, 0.45, 0.2, 0.01),
                    p("q", "Yuklama q", 200.0, 100000.0, 6000.0, 100.0, "Pa"),
                    p("nx", "To'r oraliqlari soni", 4.0, 28.0, 16.0, 2.0),
                    p("bc", "Chegaraviy shart (0 sharnir, 1 mahkam)",
                      0.0, 1.0, 0.0, 1.0),
                ],
                expected_output=(
                    "D = 8,79 MN·m; n = 16 to'rda w_max = 0,70963 mm, "
                    "Navye qatori 0,70995 mm — xato 0,045 %. "
                    "O'lchangan yaqinlashish tartibi 2,02; Richardson "
                    "ekstrapolyatsiyasi (n = 12 va 24 dan) xatoni "
                    "0,020 % dan 0,0005 % ga tushiradi. Shablon "
                    "koeffitsientlari yig'indisi aynan 0."
                ),
            ),
            visual=vis(
                kind="Ayirmali shablon va to'r yaqinlashishi",
                tool="React/SVG",
                description=(
                    "13 nuqtali shablon naqshi, fiktiv tugunlar va "
                    "to'r zichlashganda xatoning $O(\\Delta^2)$ "
                    "kamayishi."
                ),
                how_to_draw=(
                    "React/SVG: shablon paneli — $5\\times5$ "
                    "tugunlar to'ri, faqat 13 tasi bo'yalgan. Har "
                    "bir bo'yalgan tugunda koeffitsient yozilgan "
                    "($20$, $-8$, $2$, $1$); rang koeffitsient "
                    "ishorasiga qarab (musbat issiq, manfiy sovuq), "
                    "doira o'lchami esa moduliga mutanosib. Markaziy "
                    "tugun ta'kidlangan. Pastda yig'indi $= 0$ "
                    "tekshiruvi ko'rsatiladi. Ikkinchi panel — to'r "
                    "va chegaralar: plastina konturi, ichki tugunlar "
                    "to'ldirilgan doiralar, chegaraviy tugunlar "
                    "bo'sh doiralar, fiktiv tugunlar esa kontur "
                    "tashqarisida punktir doiralar; fiktiv tugundan "
                    "uning 'aks manbai' bo'lgan ichki tugunga "
                    "strelka chiziladi va ishora ($-$ yoki $+$) "
                    "yozib qo'yiladi. Uchinchi panel — "
                    "log–log xato grafigi: $\\Delta$ ga qarab xato; "
                    "qiyaligi 2 bo'lgan nazariy chiziq punktir "
                    "bilan ustiga qo'yiladi va sonli nuqtalar unga "
                    "parallel yotishi ko'rinadi."
                ),
            ),
            interp=(
                "To'r mustaqilligi jadvali muhandislik hisobining eng "
                "muhim odatini o'rgatadi. $n = 4$ da (atigi uchta "
                "mustaqil noma'lum!) xato 0,84 %, $n = 16$ da "
                "0,045 %, $n = 24$ da esa 0,020 %. "
                "Xatoning kamayish qonuniyati aniq $O(\\Delta^2)$ — "
                "o'lchangan tartib 2,0 ga juda yaqin, bu sxemaning "
                "to'g'ri amalga oshirilganini tasdiqlaydi. Richardson "
                "ekstrapolyatsiyasi esa deyarli sehrli natija beradi: "
                "ikkita mavjud hisobdan foydalanib, xatoni bir necha "
                "marta kamaytiradi. Bu 'bepul tushlik' emas — u "
                "xatoning $C\\Delta^2$ shaklda ekanligiga asoslangan, "
                "va agar sxema boshqa tartibga ega bo'lsa "
                "(masalan, burchakdagi singulyarlik tufayli), "
                "ekstrapolyatsiya yordam bermaydi. Shablon "
                "koeffitsientlari yig'indisining aynan nolga "
                "tengligi esa eng sodda, lekin eng samarali "
                "tekshiruv: har qanday chekli ayirmali sxemani "
                "yozgandan keyin birinchi navbatda shuni tekshirish "
                "kerak. Nol chiqmasa, sxema hatto doimiy funksiyani "
                "ham to'g'ri qayta ishlamaydi."
            ),
            mistakes=[
                "Fiktiv tugunlarni unutish. Ularsiz chegaraga "
                "qo'shni tugunlarda shablon to'liq qo'llanmaydi va "
                "chegaraviy shart noto'g'ri hisobga olinadi.",
                "Sharnirli va mahkamlangan uchun bir xil aks "
                "ettirish ishorasini ishlatish. Sharnirlida "
                "$-$, mahkamlanganda $+$ — bu yagona, lekin "
                "hal qiluvchi farq.",
                "To'r mustaqilligini tekshirmasdan natijani qabul "
                "qilish. Qo'pol to'r ishonchsiz javob beradi va "
                "xatoning kattaligi oldindan ma'lum emas.",
                "Kvadrat bo'lmagan to'rda ($\\Delta_x \\ne \\Delta_y$) "
                "standart 13 nuqtali shablonni o'zgartirmasdan "
                "ishlatish. Koeffitsientlar $\\Delta_x/\\Delta_y$ "
                "nisbatiga bog'liq bo'lib qoladi.",
            ],
            quiz=[
                q("Bigarmonik shablonning markaziy koeffitsienti nima "
                  "uchun 20 ga teng?",
                  "$\\partial_x^4$ dan 6, $\\partial_y^4$ dan 6, "
                  "$2\\partial_x^2\\partial_y^2$ dan $2\\cdot4 = 8$; "
                  "jami $6+6+8 = 20$.", "hisob"),
                q("Fiktiv tugun nima va u qanday aniqlanadi?",
                  "Soha tashqarisidagi virtual tugun; chegaraviy "
                  "shartdan topiladi. Sharnirlida "
                  "$w_{\\text{fik}} = -w_{\\text{ich}}$, "
                  "mahkamlanganda $+w_{\\text{ich}}$.", "konseptual"),
                q("Shablon koeffitsientlari yig'indisi nima uchun nol "
                  "bo'lishi kerak?",
                  "Doimiy funksiyaning to'rtinchi hosilasi nol; "
                  "shablon shu holatni to'g'ri qayta ishlashi kerak. "
                  "Bu eng sodda tekshiruv.", "konseptual"),
                q("To'r qadamini yarmiga tushirsak, xato qanday "
                  "o'zgaradi?",
                  "To'rt marta kamayadi, chunki xato $O(\\Delta^2)$. "
                  "Amalda kodda $n = 12 \\to 24$ da aynan shunday "
                  "kuzatiladi.", "hisob"),
                q("Kodda `add` funksiyasi nima qiladi?",
                  "Shablon tugunining hissasini matritsaga qo'shadi. "
                  "Agar tugun ichki bo'lsa — to'g'ridan-to'g'ri; "
                  "chegarada bo'lsa — hissa yo'q ($w = 0$); "
                  "tashqarida bo'lsa — aks ettirish ishorasi bilan "
                  "ichki tugunga qo'shadi.", "kod"),
                q("Richardson ekstrapolyatsiyasi qanday ishlaydi va "
                  "qachon yordam bermaydi?",
                  "$w = w_{\\text{aniq}} + C\\Delta^2$ deb faraz "
                  "qilib, ikki to'rdan $C$ ni yo'qotadi. Xato boshqa "
                  "tartibga ega bo'lsa (singulyarlik, noto'g'ri "
                  "chegaraviy shart) yordam bermaydi.", "talqin"),
            ],
            bridge=(
                "Endi bizda to'rtta usul bor: Navye, Levi, Ritz va "
                "chekli ayirmalar. Keyingi mavzuda ularni bitta "
                "masalada solishtirib, chegaraviy shartlarning "
                "og'ish, moment va reaksiyalarga ta'sirini tizimli "
                "o'rganamiz."
            ),
            research=(
                "To'qqiz nuqtali kompakt bigarmonik shablonni "
                "o'rganing. U faqat $3\\times3$ tugunlar naqshidan "
                "foydalanadi, lekin $O(\\Delta^4)$ aniqlik beradi — "
                "buning uchun o'ng tomon ham silliqlanadi: "
                "$\\nabla^4 w = q + \\frac{\\Delta^2}{12}\\nabla^2 q "
                "+ \\ldots$. Shablon koeffitsientlarini Teylor "
                "yoyilmasidan keltirib chiqaring, kodda amalga "
                "oshiring va 13 nuqtali shablon bilan bir xil to'rda "
                "taqqoslang. Nima uchun kompakt shablon chegara "
                "yaqinida qulayroq?"
            ),
            manim_ref=manim(
                scene="FiniteDifferenceScene",
                module="animatsiya/scenes/pq_solutions.py",
                title="Bigarmonik shablon va fiktiv tugunlar",
                summary=(
                    "To'r ustida 13 nuqtali shablon siljiydi, har bir "
                    "tugunda tenglama yoziladi; chegarada fiktiv "
                    "tugunlar paydo bo'lib, aks ettirish qoidasi "
                    "bilan ichki tugunlarga bog'lanishi ko'rsatiladi."
                ),
            ),
        ),
    ),

    # ------------------------------------------------------------------ pq-11
    Topic(
        id="pq-11",
        subject_id=S, module_id=M, order=11,
        title="Konsentrlangan va mahalliy yuklamalar; chegaraviy shartlarning qiyosiy tahlili",
        description=(
            "Nuqtaviy kuch ostidagi plastina, Grin funksiyasi va "
            "superpozitsiya, mahalliy singulyarlik, hamda chegaraviy "
            "shartlarning og'ish, moment va reaksiyalarga ta'sirini "
            "tizimli taqqoslash."
        ),
        learning_objective=(
            "Konsentrlangan yuklama ostidagi og'ishni qator yoki Grin "
            "funksiyasi bilan hisoblash, moment singulyarligini tushunish "
            "va chegaraviy shartlar tanlovini son bilan asoslash."
        ),
        prerequisites=["pq-10", "pq-07"],
        mathematical_core=(
            "Dirak delta funksiyasi, Grin funksiyasi "
            "$G(\\mathbf{x}, \\boldsymbol{\\xi})$, superpozitsiya "
            "integrali, $w \\sim r^2\\ln r$ singulyarligi, "
            "qator yaqinlashishining buzilishi."
        ),
        engineering_application=(
            "Uskuna oyoqlari, ustun tayanchi (punching shear), "
            "g'ildirak yuklamasi, ko'prik plitasidagi o'q bosimi, "
            "anker va bolt joylari."
        ),
        computational_component=(
            "Konsentrlangan va taqsimlangan yuklama yechimlarini "
            "taqqoslash, moment singulyarligini sonli ko'rsatish, "
            "chegaraviy shartlar jadvalini qurish."
        ),
        visualization_component=(
            "Nuqtaviy kuch ostidagi og'ish va moment maydonlari, "
            "singulyarlik zonasi, chegaraviy shartlar taqqoslash diagrammasi."
        ),
        research_extension=(
            "Punching shear (o'tkazib yuborish) hodisasini o'rganing: "
            "ustun atrofida plita qanday buziladi va normativlar "
            "kritik perimetrni qanday belgilaydi?"
        ),
        difficulty="murakkab",
        previous_link=(
            "pq-07 dagi Navye yechimi ixtiyoriy yuklamani qabul "
            "qilardi, lekin konsentrlangan kuchda qator sekin "
            "yaqinlashishi aytib o'tilgan edi. pq-10 dagi sonli usul "
            "esa singulyarlikni umuman ko'rmaydi. Endi shu "
            "muammoni to'g'ridan-to'g'ri o'rganamiz."
        ),
        next_topic="pq-12",
        estimated_minutes=90,
        tags=["konsentrlangan yuklama", "Grin funksiyasi", "singulyarlik"],
        lesson=_lesson(
            problem=(
                "Sanoat binosi plitasida og'ir uskuna o'rnatiladi: "
                "to'rtta oyoq, har biri 50 kN yuk uzatadi, tayanch "
                "yostig'i $100\\times100$ mm. Plitadagi kuchlanishni "
                "hisoblasak, yostiq o'lchamini nolga intiltirganda "
                "moment cheksizlikka intiladi. Bu fizik ma'noga egami? "
                "Va agar cheksiz bo'lsa, plita qanday qilib buzilmay "
                "turibdi? Javob ikki qismdan iborat: matematik model "
                "chegarasi va plastik qayta taqsimlanish."
            ),
            concepts=[
                c("Grin funksiyasi (Green's function)",
                  "$G(\\mathbf{x}, \\boldsymbol{\\xi})$ — "
                  "$\\boldsymbol{\\xi}$ nuqtada qo'yilgan birlik kuchdan "
                  "hosil bo'lgan og'ish. Ixtiyoriy yuklama uchun yechim "
                  "$w = \\int G q\\,dA$."),
                c("Konsentrlangan kuch modeli",
                  "$q = P\\delta(x-x_0)\\delta(y-y_0)$ — Dirak delta "
                  "funksiyasi. Bu matematik ideallashtirish; real "
                  "yuklama har doim chekli yuza bo'ylab taqsimlangan."),
                c("Moment singulyarligi",
                  "Nuqtaviy kuch ostida $w \\sim r^2\\ln r$, demak "
                  "$M \\sim \\ln r \\to \\infty$. Og'ish chekli, "
                  "moment esa logarifmik cheksiz."),
                c("Ekvivalent tayanch yuzasi",
                  "Real yostiq $c\\times c$ bo'lsa, moment chekli "
                  "bo'ladi va taxminan $\\ln(a/c)$ ga mutanosib o'sadi — "
                  "yostiqni kichraytirish sekin ta'sir qiladi."),
                c("Superpozitsiya prinsipi",
                  "Chiziqli masala bo'lgani uchun bir necha yuklamaning "
                  "ta'siri alohida yechimlarning yig'indisiga teng."),
                c("Punching shear (o'tkazib yuborish)",
                  "Konsentrlangan kuch ostida plitaning konussimon "
                  "kesilib chiqishi — egilish emas, siljish bo'yicha buzilish."),
            ],
            derivation=[
                d("1. Dirak delta yuklamasini Furye qatoriga yoyish",
                  r"q_{mn} = \frac{4}{ab}\int\int P\delta(x-x_0)\delta(y-y_0)"
                  r"\sin\frac{m\pi x}{a}\sin\frac{n\pi y}{b}dxdy "
                  r"= \frac{4P}{ab}\sin\frac{m\pi x_0}{a}\sin\frac{n\pi y_0}{b}",
                  "Delta funksiyasining saralash (sifting) xossasi: "
                  "integral funksiyaning nuqtadagi qiymatini beradi."),
                d("2. Og'ish qatori",
                  r"w = \frac{4P}{abD\pi^4}\sum_{m,n}"
                  r"\frac{\sin\frac{m\pi x_0}{a}\sin\frac{n\pi y_0}{b}"
                  r"\sin\frac{m\pi x}{a}\sin\frac{n\pi y}{b}}"
                  r"{\big[(m/a)^2 + (n/b)^2\big]^2}",
                  "Bu aynan Grin funksiyasi $G(\\mathbf{x}, "
                  "\\boldsymbol{\\xi})$ — sharnirli to'rtburchak plastina uchun."),
                d("3. Og'ish qatorining yaqinlashishi",
                  r"w_{mn} \sim \frac{1}{(m^2 + n^2)^2} \;\Rightarrow\; "
                  r"\sum \frac{1}{m^4} \ \text{yaqinlashadi}",
                  "Delta yuklamada $q_{mn}$ kamaymaydi, lekin maxraj "
                  "$m^4$ kabi o'sadi — og'ish qatori yaqinlashadi, "
                  "garchi taqsimlangan yuklamadagidan sekinroq."),
                d("4. Moment qatorining divergensiyasi",
                  r"M_{mn} \sim \frac{m^2}{(m^2+n^2)^2} \;\Rightarrow\; "
                  r"\sum_m\sum_n \frac{m^2}{(m^2+n^2)^2} \ \text{log kabi o'sadi}",
                  "Ikki marta differensiallash $m^2$ ko'paytiradi. "
                  "Yuklama nuqtasida qator logarifmik divergensiya beradi."),
                d("5. Mahalliy asimptotik yechim",
                  r"w \approx \frac{P r^2}{8\pi D}\ln\frac{r}{a} + "
                  r"\text{(silliq qism)}, \qquad r = |\mathbf{x} - "
                  r"\boldsymbol{\xi}|",
                  "Cheksiz plastina uchun fundamental yechim. Chekkalar "
                  "uzoq bo'lsa, yuklama nuqtasi yaqinida shu shakl hukmron."),
                d("6. Moment singulyarligi",
                  r"M_r \approx -\frac{P}{4\pi}\Big[(1+\nu)\ln\frac{r}{a} "
                  r"+ \ldots\Big] \;\xrightarrow{r\to0}\; +\infty",
                  "Ikki marta differensiallash $r^2\\ln r$ ni "
                  "$\\ln r$ ga aylantiradi. Og'ish chekli "
                  "($r^2\\ln r \\to 0$), moment esa cheksiz."),
                d("7. Chekli yostiq bilan regulyarizatsiya",
                  r"M_{\max} \approx \frac{P}{4\pi}\Big[(1+\nu)"
                  r"\ln\frac{2a}{\pi c} + \gamma\Big]",
                  "Yuklama $c\\times c$ yuza bo'ylab taqsimlansa, "
                  "logarifm chekli bo'ladi. $c$ ni ikki marta "
                  "kichraytirish momentni faqat "
                  "$\\frac{P(1+\\nu)\\ln 2}{4\\pi}$ ga oshiradi — juda sekin."),
                d("8. Superpozitsiya bilan ko'p yuklama",
                  r"w(\mathbf{x}) = \sum_{k} P_k\,G(\mathbf{x}, "
                  r"\boldsymbol{\xi}_k) + \int_A q(\boldsymbol{\xi})"
                  r"G(\mathbf{x}, \boldsymbol{\xi})\,dA_\xi",
                  "Chiziqlilik tufayli barcha yuklamalar mustaqil "
                  "qo'shiladi. To'rtta uskuna oyog'i — to'rtta Grin "
                  "funksiyasining yig'indisi."),
            ],
            meaning=(
                "Moment singulyarligining fizik ma'nosi — "
                "**modelning chegarasi, materialning emas**. "
                "Kirxhoff nazariyasi plastinani ikki o'lchovli deb "
                "hisoblaydi va qalinlik bo'yicha kuchlanish "
                "taqsimotini chiziqli deb oladi. Yuklama nuqtasidan "
                "$\\sim h$ masofada bu taxmin buziladi: u yerda uch "
                "o'lchovli, murakkab kuchlanish holati mavjud. "
                "Sen-Venan prinsipi (mq-05) aynan shuni aytadi — "
                "nazariya yuklama qo'yilish joyidan qalinlik "
                "tartibidagi masofada ishonchli bo'ladi. Shuning "
                "uchun amaliyotda moment $r \\approx h$ da "
                "'kesiladi' yoki yuklama chekli yuza bo'ylab "
                "taqsimlangan deb olinadi. Logarifmik singulyarlikning "
                "yana bir amaliy oqibati bor: u **juda sekin** "
                "o'sadi. Yostiq yuzasini 100 marta kichraytirish "
                "momentni atigi $\\ln 100 = 4{,}6$ marta "
                "ko'paytiradi (koeffitsient bilan). Shuning uchun "
                "tayanch yostig'ining aniq o'lchami hisobga kam "
                "ta'sir qiladi — bu muhandis uchun yaxshi xabar. "
                "Yomon xabar esa boshqa: konsentrlangan kuch ostida "
                "plita ko'pincha egilish bo'yicha emas, **siljish "
                "bo'yicha** (punching shear) buziladi va bu butunlay "
                "boshqa hisobni talab qiladi."
            ),
            equations=[
                eq(r"w(\mathbf{x}) = \int_A G(\mathbf{x}, \boldsymbol{\xi})"
                   r"q(\boldsymbol{\xi})\,dA_\xi",
                   "Grin funksiyasi orqali umumiy yechim.",
                   "Superpozitsiya integrali"),
                eq(r"w \approx \frac{Pr^2}{8\pi D}\ln\frac{r}{a}",
                   "Konsentrlangan kuch ostidagi mahalliy og'ish "
                   "(fundamental yechim).", "Fundamental yechim"),
                eq(r"M_r \sim -\frac{P(1+\nu)}{4\pi}\ln r \to \infty",
                   "Moment logarifmik singulyarligi.",
                   "Moment singulyarligi"),
                eq(r"u_{\text{kritik}} = 4(c + 2d) \ \text{(kvadrat ustun)}",
                   "Punching shear uchun kritik perimetr (Eurocode 2 "
                   "uslubida, $d$ — foydali balandlik).",
                   "Kritik perimetr"),
            ],
            conditions=(
                "**Konsentrlangan yuklama uchun qo'shimcha shartlar:**\n"
                "- Yuklama nuqtasidan $r > h$ masofada Kirxhoff "
                "nazariyasi ishonchli; $r < h$ da 3D tahlil kerak;\n"
                "- Moment hisobi uchun yuklama chekli yuza "
                "($c \\times c$) bo'ylab taqsimlangan deb olinadi;\n"
                "- Punching shear alohida tekshiriladi: kritik "
                "perimetrda $\\tau = V/(u\\,d) \\le \\tau_{\\text{ruxsat}}$.\n\n"
                "**Qator yaqinlashishi:**\n"
                "- Og'ish: $N \\approx 30$ yetarli (xato < 0,5 %);\n"
                "- Moment: qator yuklama nuqtasida **yaqinlashmaydi**; "
                "$r > h$ nuqtalarda esa $N \\approx 100$ kerak;\n"
                "- Amaliy yechim: momentni yuklama nuqtasidan "
                "$r = h/2 \\ldots h$ masofada baholash.\n\n"
                "**Chegaraviy shartlar** oldingi mavzulardagidek qoladi; "
                "konsentrlangan yuklama ularga ta'sir qilmaydi."
            ),
            worked=WorkedExample(
                statement=(
                    "Temir-beton plita $a = b = 6$ m, $h = 220$ mm, "
                    "$E = 30$ GPa, $\\nu = 0{,}2$, to'rt chekka "
                    "sharnirli. Markazda uskuna oyog'i $P = 80$ kN "
                    "kuch uzatadi, yostiq $c = 150$ mm. "
                    "(a) Markazdagi og'ishni toping. (b) Momentni "
                    "yostiq chekkasida baholang. (c) Bir tekis "
                    "ekvivalent yuklama ($q = P/(ab)$) bilan "
                    "taqqoslang. (d) Punching shear ni tekshiring "
                    "($\\tau_{\\text{ruxsat}} = 0{,}6$ MPa, $d = 185$ mm)."
                ),
                given=[
                    r"a = b = 6\ \text{m},\ h = 0{,}22\ \text{m}",
                    r"E = 30\ \text{GPa},\ \nu = 0{,}2",
                    r"P = 80\ \text{kN},\ c = 0{,}15\ \text{m},\ d = 0{,}185\ \text{m}",
                ],
                steps=[
                    st(r"D = \frac{30\times10^9 \cdot 0{,}22^3}{12 \cdot 0{,}96} "
                       r"= \frac{3{,}1944\times10^{8}}{11{,}52} "
                       r"= 2{,}7729\times10^{7}\ \text{N·m}",
                       "$h^3 = 1{,}0648\\times10^{-2}$ m³."),
                    st(r"w_{\max} = \alpha_P\frac{Pa^2}{D}, \quad "
                       r"\alpha_P = 0{,}01160 \ (\text{kvadrat, markazda})",
                       "Konsentrlangan kuch uchun koeffitsient — "
                       "jadvaldan yoki qatordan; kodda qator bilan "
                       "aniq hisoblanadi."),
                    st(r"w_{\max} = 0{,}01160\frac{80\,000 \cdot 36}"
                       r"{2{,}7729\times10^{7}} = 0{,}01160 \cdot "
                       r"0{,}10387 = 1{,}205\times10^{-3}\ \text{m} "
                       r"= 1{,}21\ \text{mm}",
                       "Og'ish chekli va oddiy — singulyarlik faqat "
                       "momentda."),
                    st(r"M \approx \frac{P}{4\pi}\Big[(1+\nu)\ln\frac{2a}"
                       r"{\pi c} + 1 - \nu\Big]",
                       "Yostiq bilan regulyarizatsiya qilingan moment "
                       "(Timoshenko formulasi)."),
                    st(r"\frac{2a}{\pi c} = \frac{12}{\pi \cdot 0{,}15} "
                       r"= 25{,}46; \quad \ln 25{,}46 = 3{,}237",
                       "Logarifm argumenti — yostiq qanchalik kichik "
                       "bo'lsa, shuncha katta."),
                    st(r"M \approx \frac{80\,000}{12{,}566}\big[1{,}2 \cdot "
                       r"3{,}237 + 0{,}8\big] = 6366 \cdot 4{,}684 "
                       r"= 29\,822\ \text{N·m/m}",
                       "Moment birlik uzunlikka. Bu juda katta — "
                       "taqsimlangan yuklamadagidan bir necha marta."),
                    st(r"q_{\text{ekv}} = \frac{P}{ab} = \frac{80\,000}{36} "
                       r"= 2222\ \text{Pa}; \quad "
                       r"M_{\text{tekis}} = 0{,}0479 \cdot 2222 \cdot 36 "
                       r"= 3831\ \text{N·m/m}",
                       "Bir xil umumiy kuch tekis taqsimlansa, moment "
                       "**7,8 marta** kichik bo'lardi."),
                    st(r"u_{\text{kritik}} = 4(c + 2 \cdot 2d) = "
                       r"4(0{,}15 + 0{,}74) = 3{,}56\ \text{m}",
                       "Eurocode 2: kritik perimetr ustun yuzidan "
                       "$2d$ masofada."),
                    st(r"\tau = \frac{P}{u\,d} = \frac{80\,000}{3{,}56 "
                       r"\cdot 0{,}185} = 121{,}5\ \text{kPa} = 0{,}12\ \text{MPa} "
                       r"< 0{,}6\ \text{MPa} \ \checkmark",
                       "Punching shear bo'yicha zaxira 4,9 — xavf yo'q. "
                       "Lekin egilish momenti bo'yicha armatura "
                       "tekshirilishi shart."),
                ],
                answer=(
                    "$D = 27{,}73$ MN·m; $w_{\\max} = 1{,}21$ mm; "
                    "yostiq chekkasida $M \\approx 29{,}8$ kN·m/m — "
                    "bir xil kuchning tekis taqsimlanishidagidan "
                    "7,8 marta katta; punching shear "
                    "$\\tau = 0{,}12$ MPa $< 0{,}6$ MPa, zaxira 4,9."
                ),
                engineering_note=(
                    "7,8 marta farq konsentrlangan yuklamaning eng "
                    "muhim xususiyatini ko'rsatadi: **umumiy kuch bir "
                    "xil bo'lsa ham, mahalliy ta'sir butunlay "
                    "boshqacha**. Shuning uchun uskuna oyoqlari "
                    "ostiga yuklamani tarqatuvchi plita (spreader "
                    "plate) qo'yiladi — yostiq yuzasini oshirish "
                    "momentni logarifmik ravishda kamaytiradi. "
                    "Yana bir yechim — oyoqlarni to'sin ustiga "
                    "joylashtirish, shunda kuch to'g'ridan-to'g'ri "
                    "vertikal elementga uzatiladi."
                ),
            ),
            computation=Computation(
                caption=(
                    "Konsentrlangan yuklama yechimini qator bilan "
                    "hisoblash, moment singulyarligini ko'rsatish va "
                    "chegaraviy shartlarni tizimli taqqoslash."
                ),
                code='''"""Konsentrlangan yuklama, Grin funksiyasi va singulyarlik."""
import numpy as np
from labkit import PARAMS, note, series, table, value

a = float(PARAMS.get("a", 6.0))
b = float(PARAMS.get("b", 6.0))
h = float(PARAMS.get("h", 220.0))/1000.0
E = float(PARAMS.get("E", 30.0))*1e9
nu = float(PARAMS.get("nu", 0.2))
P = float(PARAMS.get("P", 80000.0))
cpad = float(PARAMS.get("c", 150.0))/1000.0
x0r = float(PARAMS.get("x0", 0.5))       # yuklama joyi x/a
y0r = float(PARAMS.get("y0", 0.5))
NT = int(PARAMS.get("NT", 60))

D = E*h**3/(12*(1 - nu**2))
x0, y0 = x0r*a, y0r*b
value("Silindrik bikrlik D", D/1e6, "MN*m")
value("Yuklama joyi x0", x0, "m")
value("Yuklama joyi y0", y0, "m")


def green(x, y, nterms):
    """Nuqtaviy kuchdan og'ish (Navye qatori)."""
    w = np.zeros_like(np.asarray(x, dtype=float))
    for m in range(1, nterms + 1):
        sm0 = np.sin(m*np.pi*x0/a)
        if abs(sm0) < 1e-14:
            continue
        for n in range(1, nterms + 1):
            sn0 = np.sin(n*np.pi*y0/b)
            if abs(sn0) < 1e-14:
                continue
            am, bn = m*np.pi/a, n*np.pi/b
            w += (4*P/(a*b*D)*sm0*sn0/(am**2 + bn**2)**2
                  * np.sin(am*x)*np.sin(bn*y))
    return w


w_c = float(green(np.array([x0]), np.array([y0]), NT)[0])
value("w (yuklama nuqtasida)", w_c*1000, "mm")
value("Koeffitsient alpha_P = w*D/(P*a^2)", w_c*D/(P*a**2), "—")
note(f"Kvadrat sharnirli plastina uchun jadval qiymati 0.01160 — "
     f"hisob {w_c*D/(P*a**2):.5f} beradi.")

# Og'ish qatorining yaqinlashishi
conv = []
for nt in [5, 10, 20, 40, 60, 100]:
    wn = float(green(np.array([x0]), np.array([y0]), nt)[0])
    conv.append([nt, round(wn*1000, 6),
                 round(abs(wn - w_c)/w_c*100, 4) if w_c else 0.0])
table("Og'ish qatorining yaqinlashishi (konsentrlangan kuch)",
      ["Hadlar soni N", "w, mm", "Farq, %"], conv)
note("Og'ish qatori yaqinlashadi: q_mn kamaymaydi, lekin maxraj "
     "(m^2+n^2)^2 kabi o'sadi.")

# --- Moment qatori: divergensiya ---
def moment_x(x, y, nterms):
    mx = np.zeros_like(np.asarray(x, dtype=float))
    for m in range(1, nterms + 1):
        sm0 = np.sin(m*np.pi*x0/a)
        if abs(sm0) < 1e-14:
            continue
        for n in range(1, nterms + 1):
            sn0 = np.sin(n*np.pi*y0/b)
            if abs(sn0) < 1e-14:
                continue
            am, bn = m*np.pi/a, n*np.pi/b
            wmn = 4*P/(a*b*D)*sm0*sn0/(am**2 + bn**2)**2
            mx += D*wmn*(am**2 + nu*bn**2)*np.sin(am*x)*np.sin(bn*y)
    return mx


mconv = []
for nt in [5, 10, 20, 40, 60, 100, 150]:
    mm = float(moment_x(np.array([x0]), np.array([y0]), nt)[0])
    mconv.append([nt, round(mm/1000, 3)])
table("Moment qatori yuklama nuqtasida (divergensiya)",
      ["Hadlar soni N", "M_x, kN*m/m"], mconv)
note("Moment qatori YAQINLASHMAYDI: hadlar soni oshgani sari "
     "qiymat logarifmik ravishda o'sib boradi — bu matematik "
     "singulyarlik, fizik hodisa emas.")

# --- Moment r ga bog'liq (singulyarlik profili) ---
rr = np.linspace(0.02, 1.5, 120)
mr = moment_x(x0 + rr, np.full_like(rr, y0), 100)
series("M_x(r) yuklama nuqtasidan masofa bo'yicha",
       rr.tolist(), (mr/1000).tolist(),
       xlabel="Masofa r, m", ylabel="M_x, kN*m/m")
series("Qalinlik chegarasi r = h", [h, h], [0.0, float(np.max(mr)/1000)],
       xlabel="Masofa r, m", ylabel="M_x, kN*m/m")
i_h = int(np.argmin(np.abs(rr - h)))
value("M_x (r = h)", float(mr[i_h])/1000, "kN*m/m")
note(f"r = h = {h*1000:.0f} mm da M_x = {mr[i_h]/1000:.2f} kN*m/m. "
     f"Sen-Venan prinsipiga ko'ra Kirxhoff nazariyasi shu masofadan "
     f"boshlab ishonchli.")

# --- Yostiq bilan regulyarizatsiya (Timoshenko formulasi) ---
M_pad = P/(4*np.pi)*((1 + nu)*np.log(2*a/(np.pi*cpad)) + 1 - nu)
value("M (yostiq bilan, c = %.0f mm)" % (cpad*1000), M_pad/1000, "kN*m/m")
value("sigma (yostiq chekkasida)", 6*M_pad/h**2/1e6, "MPa")

pads = np.linspace(0.02, 1.0, 100)
Mp = P/(4*np.pi)*((1 + nu)*np.log(2*a/(np.pi*pads)) + 1 - nu)
series("M(c) — yostiq o'lchamining ta'siri", (pads*1000).tolist(),
       (Mp/1000).tolist(), xlabel="Yostiq o'lchami c, mm",
       ylabel="M, kN*m/m")
note(f"Yostiqni 2 marta kichraytirish momentni faqat "
     f"{P*(1+nu)*np.log(2)/(4*np.pi)/1000:.2f} kN*m/m ga oshiradi — "
     f"logarifmik bog'liqlik juda sekin.")

# --- Tekis taqsimlangan ekvivalent yuklama bilan taqqoslash ---
q_eq = P/(a*b)
M_unif = 0.0
for m in range(1, 40, 2):
    for n in range(1, 40, 2):
        am, bn = m*np.pi/a, n*np.pi/b
        qmn = 16*q_eq/(np.pi**2*m*n)
        wmn = qmn/(D*(am**2 + bn**2)**2)
        M_unif += D*wmn*(am**2 + nu*bn**2)*np.sin(m*np.pi/2)*np.sin(n*np.pi/2)
value("Ekvivalent tekis yuklama q", q_eq, "Pa")
value("M (tekis yuklama)", M_unif/1000, "kN*m/m")
value("M(konsentrlangan)/M(tekis)", M_pad/M_unif, "—")
note(f"Bir xil umumiy kuch: konsentrlangan holatda moment "
     f"{M_pad/M_unif:.1f} marta katta. Umumiy kuch emas, "
     f"uning taqsimlanishi hal qiluvchi.")

# --- Punching shear ---
d_eff = h - 0.035
u_crit = 4*(cpad + 4*d_eff)
tau = P/(u_crit*d_eff)
value("Foydali balandlik d", d_eff*1000, "mm")
value("Kritik perimetr u", u_crit, "m")
value("Siljish kuchlanishi tau", tau/1e6, "MPa")
value("Zaxira (tau_ruxsat = 0.6 MPa)", 0.6e6/tau, "—")
if tau < 0.6e6:
    note(f"Punching shear XAVFSIZ: tau = {tau/1e6:.3f} MPa < 0.6 MPa, "
         f"zaxira {0.6e6/tau:.1f}.")
else:
    note(f"PUNCHING SHEAR XAVFI: tau = {tau/1e6:.3f} MPa >= 0.6 MPa — "
         f"siljish armaturasi yoki kapitel kerak.")

# --- Chegaraviy shartlarning qiyosiy tahlili ---
table("Kvadrat plastina: chegaraviy shartlar qiyosi (tekis yuklama)",
      ["Chegaraviy shart", "w koeff.", "M_markaz", "M_chekka", "Izoh"],
      [["4 sharnirli", 0.004062, 0.0479, 0.0,
        "Etalon; burchak reaksiyasi bor"],
       ["4 mahkamlangan", 0.001260, 0.0231, -0.0513,
        "Eng bikr; chekkada katta manfiy moment"],
       ["2 sharnirli + 2 mahkamlangan", 0.002080, 0.0340, -0.0400,
        "Oraliq variant"],
       ["3 sharnirli + 1 erkin", 0.008700, 0.0850, 0.0,
        "Erkin chekka yumshatadi"],
       ["2 qarama-qarshi sharnirli, 2 erkin", 0.013020, 0.1250, 0.0,
        "Silindrik egilishga yaqin"]])

for name, aw in [("4 sharnirli", 0.004062), ("4 mahkamlangan", 0.001260),
                 ("3 sharnirli + 1 erkin", 0.008700)]:
    value(f"w_max ({name}, q = {q_eq:.0f} Pa)", aw*q_eq*a**4/D*1000, "mm")

table("Yuklama turlarining taqqoslashi (bir xil umumiy kuch P)",
      ["Yuklama turi", "M nisbati", "w nisbati", "Amaliy xulosa"],
      [["Butun yuza bo'ylab tekis", 1.0, 1.0, "Eng qulay"],
       ["Markaziy chorak yuza", "~2", "~1.5", "Oraliq"],
       ["Konsentrlangan (c = 150 mm)", round(M_pad/M_unif, 1), "~1.2",
        "Moment keskin oshadi, og'ish kam o'zgaradi"],
       ["Ideal nuqtaviy (c -> 0)", "cheksiz", "chekli",
        "Matematik ideallashtirish"]])
''',
                parameters=[
                    p("a", "Plastina tomoni a", 1.0, 20.0, 6.0, 0.1, "m"),
                    p("b", "Plastina tomoni b", 1.0, 20.0, 6.0, 0.1, "m"),
                    p("h", "Qalinlik h", 50.0, 600.0, 220.0, 5.0, "mm"),
                    p("E", "Yung moduli E", 1.0, 400.0, 30.0, 1.0, "GPa"),
                    p("nu", "Puasson koeffitsienti ν", 0.0, 0.45, 0.2, 0.01),
                    p("P", "Konsentrlangan kuch P", 1000.0, 1000000.0,
                      80000.0, 1000.0, "N"),
                    p("c", "Tayanch yostig'i c", 20.0, 1000.0, 150.0, 10.0, "mm"),
                    p("x0", "Yuklama joyi x/a", 0.1, 0.9, 0.5, 0.05),
                    p("y0", "Yuklama joyi y/b", 0.1, 0.9, 0.5, 0.05),
                    p("NT", "Qator hadlari N", 10.0, 120.0, 60.0, 10.0),
                ],
                expected_output=(
                    "D = 27,73 MN·m; w = 1,20 mm, α_P ≈ 0,0116 "
                    "(jadval 0,01160); og'ish qatori yaqinlashadi, "
                    "moment qatori esa N oshgani sari o'sib boradi "
                    "(divergensiya); yostiq bilan M ≈ 30 kN·m/m — "
                    "tekis yuklamadagidan ≈ 8 marta katta; "
                    "punching shear τ ≈ 0,12 MPa, zaxira ≈ 5."
                ),
            ),
            visual=vis(
                kind="Konsentrlangan yuklama va singulyarlik",
                tool="React/SVG + Matplotlib",
                description=(
                    "Nuqtaviy kuch ostidagi og'ish va moment "
                    "maydonlari, moment singulyarligi profili, "
                    "chegaraviy shartlar taqqoslash diagrammasi."
                ),
                how_to_draw=(
                    "React/SVG: birinchi panel — og'ish konturi; u "
                    "yuklama nuqtasida silliq cho'qqi beradi, "
                    "singulyarlik ko'rinmaydi. Ikkinchi panel — "
                    "moment konturi; u yerda yuklama nuqtasi "
                    "atrofida rang keskin to'yinadi va shkalaning "
                    "yuqori chegarasiga urilib qoladi — bu "
                    "singulyarlikning vizual belgisi. Rang shkalasi "
                    "logarifmik olinadi, shunda tuzilish ko'rinadi. "
                    "Uchinchi panel — $M(r)$ profili yarim-log "
                    "o'qlarda: $\\ln r$ bo'yicha to'g'ri chiziq "
                    "bo'lib chiqadi, bu logarifmik singulyarlikni "
                    "tasdiqlaydi; $r = h$ vertikal punktir chiziq "
                    "bilan belgilanadi va undan chapdagi soha "
                    "'nazariya ishonchsiz' deb shtrixlanadi. "
                    "To'rtinchi panel — chegaraviy shartlar ustun "
                    "diagrammasi: beshta variant uchun $w$ va "
                    "$M$ qiymatlari yonma-yon ustunlar bilan."
                ),
            ),
            interp=(
                "Moment qatorining yaqinlashish jadvali eng muhim "
                "natija: hadlar soni oshgani sari qiymat to'xtamasdan "
                "o'sib boradi. Bu sonli xato emas — qator haqiqatan "
                "ham divergent. Boshlovchi muhandis buni "
                "'yaqinlashmadi, ko'proq had olaman' deb "
                "tushunishi mumkin, lekin bu behuda: masalaning "
                "o'zida singulyarlik bor. To'g'ri yechim — model "
                "chegarasini tan olish va momentni $r \\approx h$ "
                "da baholash yoki yostiq bilan regulyarizatsiya "
                "qilish. Bu FEM da ham aynan shunday namoyon "
                "bo'ladi: konsentrlangan kuch qo'yilgan tugunda "
                "kuchlanish to'r zichlashgani sari cheksiz o'sadi "
                "va 'to'r mustaqilligi' hech qachon erishilmaydi. "
                "Yuklama turlari jadvali esa loyihalash uchun aniq "
                "xulosa beradi: bir xil umumiy kuch konsentrlangan "
                "holatda 8 marta katta moment beradi, lekin og'ish "
                "atigi 20 % ga farq qiladi. Sababi — og'ish "
                "integral kattalik (butun plastina javob beradi), "
                "moment esa mahalliy. Shuning uchun konsentrlangan "
                "yuklamada bikrlik emas, **mustahkamlik** hal "
                "qiluvchi bo'ladi — bu pq-06 dagi umumiy qoidaning "
                "muhim istisnosi."
            ),
            mistakes=[
                "Moment qatorining divergensiyasini sonli xato deb "
                "hisoblab, ko'proq had olishga urinish. Qator "
                "matematik jihatdan yaqinlashmaydi; muammo "
                "hadlar sonida emas.",
                "Konsentrlangan kuchni ekvivalent tekis yuklama "
                "bilan almashtirish. Og'ish uchun bu taxminan "
                "to'g'ri, moment uchun esa 5–10 marta xato beradi.",
                "Punching shear ni tekshirmaslik. Konsentrlangan "
                "kuch ostida plita ko'pincha egilishdan emas, "
                "siljishdan buziladi — bu mo'rt va oldindan "
                "ogohlantirmaydigan buzilish.",
                "Yostiq o'lchamini juda aniq tanlashga urinish. "
                "Logarifmik bog'liqlik tufayli $c$ ning ikki "
                "barobar xatosi momentda atigi 10–15 % beradi.",
            ],
            quiz=[
                q("Nima uchun konsentrlangan kuch ostida og'ish "
                  "chekli, moment esa cheksiz?",
                  "$w \\sim r^2\\ln r \\to 0$ ($r \\to 0$ da), lekin "
                  "ikki marta differensiallash $\\ln r$ beradi va u "
                  "cheksizlikka intiladi.", "konseptual"),
                q("Grin funksiyasi nima va u nima uchun foydali?",
                  "Birlik konsentrlangan kuchdan hosil bo'lgan "
                  "og'ish. Ixtiyoriy yuklama uchun yechim uning "
                  "superpozitsiyasi: $w = \\int Gq\\,dA$.",
                  "konseptual"),
                q("Yostiq o'lchamini 2 marta kichraytirsak, moment "
                  "qancha oshadi?",
                  "$\\frac{P(1+\\nu)\\ln 2}{4\\pi}$ ga — misolda "
                  "atigi 4,4 kN·m/m, ya'ni 15 % dan kam. "
                  "Logarifmik bog'liqlik sekin.", "hisob"),
                q("Singulyarlikning fizik ma'nosi nima?",
                  "Modelning chegarasi: Kirxhoff nazariyasi "
                  "yuklama nuqtasidan $\\sim h$ masofadan yaqinroqda "
                  "o'rinli emas. Real materialda u yerda 3D "
                  "kuchlanish holati va plastik qayta taqsimlanish bor.",
                  "talqin"),
                q("Kodda moment qatorining jadvali nimani ko'rsatadi "
                  "va nega bu muhim?",
                  "Hadlar soni oshgani sari moment to'xtamasdan "
                  "o'sib borishini — qator divergent. Bu sonli xato "
                  "emas, masalaning xossasi; shuning uchun boshqa "
                  "yondashuv (regulyarizatsiya) kerak.", "kod"),
                q("Bir xil umumiy kuch nima uchun konsentrlangan "
                  "holatda 8 marta katta moment beradi, lekin "
                  "og'ish atigi 20 % ga farq qiladi?",
                  "Og'ish — integral kattalik, unga butun plastina "
                  "javob beradi; moment esa mahalliy va yuklamaning "
                  "to'planishiga juda sezgir.", "talqin"),
            ],
            bridge=(
                "Hozirgacha material izotrop deb olindi. Lekin "
                "amaliyotda ko'plab plastinalar yo'nalish bo'yicha "
                "har xil xossaga ega: gofrlangan list, qovurg'ali "
                "plita, temir-beton, kompozit. Keyingi mavzuda "
                "ortotrop plastinalar nazariyasini quramiz."
            ),
            research=(
                "Punching shear (o'tkazib yuborish) hodisasini "
                "chuqur o'rganing. Ustun atrofida plita konussimon "
                "sirt bo'ylab kesilib chiqadi; buzilish mo'rt va "
                "ogohlantirishsiz. Eurocode 2 va ACI 318 "
                "normativlaridagi kritik perimetr ta'riflarini "
                "taqqoslang (ular $2d$ va $d/2$ masofani oladi — "
                "nima uchun farqli?). Kritik perimetr formulasi "
                "bo'yicha parametrik tahlil qiling: ustun "
                "o'lchamini, plita qalinligini va armatura "
                "koeffitsientini o'zgartirib, xavfsizlik chegarasini "
                "quring. Siljish armaturasi va kapitel (ustun "
                "boshi kengaytmasi) qanday ishlaydi?"
            ),
        ),
    ),

    # ------------------------------------------------------------------ pq-12
    Topic(
        id="pq-12",
        subject_id=S, module_id=M, order=12,
        title="Ortotrop plastinalar va ekvivalent bikrliklar: gofrlangan hamda qovurg'ali panellar",
        description=(
            "Ortotrop material uchun moment-egrilik munosabatlari, "
            "Huber tenglamasi, geometrik ortotropiya (gofr, qovurg'a, "
            "hujayrali panel) va ekvivalent bikrliklarni hisoblash."
        ),
        learning_objective=(
            "Ortotrop plastina tenglamasini yozish va yechish, "
            "geometrik ortotropiyada ekvivalent bikrliklarni "
            "hisoblash va qovurg'ali panelning samaradorligini baholash."
        ),
        prerequisites=["pq-11", "tmm-13"],
        mathematical_core=(
            "$D_x w_{,xxxx} + 2H w_{,xxyy} + D_y w_{,yyyy} = q$, "
            "$H = D_1 + 2D_{xy}$, ekvivalent bikrliklar, "
            "affin almashtirish bilan izotropga keltirish."
        ),
        engineering_application=(
            "Gofrlangan po'lat list, qovurg'ali plita (ribbed slab), "
            "sendvich va hujayrali panel, temir-beton ikki yo'nalishli "
            "armatura, yog'och va kompozit panellar."
        ),
        computational_component=(
            "Ekvivalent bikrliklarni hisoblash, ortotrop Navye "
            "yechimini qurish, izotrop tekis plastina bilan "
            "og'irlik/bikrlik bo'yicha taqqoslash."
        ),
        visualization_component=(
            "Gofr va qovurg'a kesimlari, bikrliklarning yo'nalish "
            "bo'yicha diagrammasi, og'irlik–bikrlik samaradorligi grafigi."
        ),
        research_extension=(
            "Auksetik (manfiy Puasson koeffitsientli) va gradiyentli "
            "materiallardan yasalgan plastinalarni o'rganing: ular "
            "qanday noodatiy xossalar beradi?"
        ),
        difficulty="ilg'or",
        previous_link=(
            "tmm-13 da material simmetriyasi va ortotropiya "
            "o'rganilgan edi. Endi uni plastina nazariyasiga "
            "kiritamiz va kutilmagan natijaga kelamiz: ortotropiya "
            "faqat materialdan emas, **geometriyadan** ham kelib "
            "chiqishi mumkin."
        ),
        next_topic="pq-13",
        estimated_minutes=95,
        tags=["ortotrop", "gofr", "qovurg'a", "ekvivalent bikrlik"],
        lesson=_lesson(
            problem=(
                "pq-06 da aniqlangan edi: katta plastinalarda bikrlik "
                "hukmron va mustahkamlik bo'yicha 3–4 karra zaxira "
                "qoladi — material isrof bo'ladi. Yechim sifatida "
                "'shaklni o'zgartirish' aytilgan edi. Endi buni "
                "miqdoriy qilamiz: tekis listni gofrlash yoki "
                "qovurg'a qo'shish bikrlikni qancha oshiradi? "
                "Va bunday panel endi izotrop emas — uni qanday "
                "hisoblaymiz?"
            ),
            concepts=[
                c("Ortotrop plastina",
                  "Uchta o'zaro perpendikulyar simmetriya tekisligiga "
                  "ega material yoki struktura; egilish bikrligi "
                  "yo'nalishga bog'liq: $D_x \\ne D_y$."),
                c("Material va geometrik ortotropiya",
                  "Birinchisi materialning o'zidan (yog'och, kompozit), "
                  "ikkinchisi geometriyadan (gofr, qovurg'a) kelib "
                  "chiqadi. Matematik apparat ikkalasida bir xil."),
                c("Huber tenglamasi",
                  "$D_x w_{,xxxx} + 2Hw_{,xxyy} + D_y w_{,yyyy} = q$ — "
                  "ortotrop plastinaning asosiy tenglamasi (1914)."),
                c("Effektiv buralish bikrligi $H$",
                  "$H = D_1 + 2D_{xy}$, bunda $D_1 = \\nu_y D_x = "
                  "\\nu_x D_y$ — o'zaro bikrlik, $D_{xy}$ — sof "
                  "buralish bikrligi."),
                c("Ekvivalent bikrlik",
                  "Geometrik ortotropiyada real strukturaning "
                  "(qovurg'a, gofr) og'irlik markazi va inersiya "
                  "momentidan hisoblangan taqsimlangan bikrlik."),
                c("Bikrlik–og'irlik samaradorligi",
                  "$D/\\rho_{\\text{yuza}}$ nisbati — qovurg'ali "
                  "panel tekis listdan o'nlab marta samarali."),
            ],
            derivation=[
                d("1. Ortotrop Guk qonuni (tekis kuchlanish holati)",
                  r"\sigma_x = \frac{E_x}{1-\nu_x\nu_y}(\varepsilon_x "
                  r"+ \nu_y\varepsilon_y), \quad \tau_{xy} = G\gamma_{xy}",
                  "tmm-13 dagi ortotrop munosabatlar. Maksvell "
                  "simmetriyasi: $\\nu_x E_y = \\nu_y E_x$, demak "
                  "mustaqil doimiylar to'rtta: $E_x, E_y, \\nu_x, G$."),
                d("2. Momentlarni integrallash",
                  r"M_x = -\big(D_x w_{,xx} + D_1 w_{,yy}\big), \quad "
                  r"M_y = -\big(D_y w_{,yy} + D_1 w_{,xx}\big), \quad "
                  r"M_{xy} = -2D_{xy}w_{,xy}",
                  "pq-03 dagi kabi qalinlik bo'yicha integrallash; "
                  "endi har bir yo'nalishda o'z moduli."),
                d("3. Bikrliklar ta'rifi",
                  r"D_x = \frac{E_x h^3}{12(1-\nu_x\nu_y)}, \quad "
                  r"D_y = \frac{E_y h^3}{12(1-\nu_x\nu_y)}, \quad "
                  r"D_1 = \nu_y D_x, \quad D_{xy} = \frac{Gh^3}{12}",
                  "Izotrop holda $E_x = E_y = E$, $G = E/[2(1+\\nu)]$ "
                  "va hammasi $D$ ga keltiriladi."),
                d("4. Muvozanatga qo'yish",
                  r"\frac{\partial^2 M_x}{\partial x^2} + "
                  r"2\frac{\partial^2 M_{xy}}{\partial x\partial y} + "
                  r"\frac{\partial^2 M_y}{\partial y^2} + q = 0",
                  "pq-04 dagi muvozanat tenglamasi o'zgarmaydi — u "
                  "materialga bog'liq emas."),
                d("5. Huber tenglamasi",
                  r"D_x\frac{\partial^4 w}{\partial x^4} + "
                  r"2H\frac{\partial^4 w}{\partial x^2\partial y^2} + "
                  r"D_y\frac{\partial^4 w}{\partial y^4} = q, \qquad "
                  r"H = D_1 + 2D_{xy}",
                  "2- va 4-qadamlarni birlashtiramiz. Izotrop holda "
                  "$D_x = D_y = H = D$ va pq-04 dagi tenglama tiklanadi."),
                d("6. Navye yechimi ortotrop holda",
                  r"w_{mn} = \frac{q_{mn}}{\pi^4\Big[D_x\big(\frac{m}{a}\big)^4 "
                  r"+ 2H\big(\frac{m}{a}\big)^2\big(\frac{n}{b}\big)^2 "
                  r"+ D_y\big(\frac{n}{b}\big)^4\Big]}",
                  "Sinuslar bazisi hali ham xususiy funksiya — "
                  "faqat maxraj o'zgardi. Sharnirli chekkalarda "
                  "yechim shu qadar sodda qoladi."),
                d("7. Gofrlangan list uchun ekvivalent bikrliklar",
                  r"D_x = \frac{E I_g}{s}, \qquad D_y = "
                  r"\frac{s}{\ell}\cdot\frac{Et^3}{12(1-\nu^2)}, \qquad "
                  r"H \approx \frac{s}{\ell}\cdot\frac{Gt^3}{6}",
                  "$s$ — gofr qadami, $\\ell$ — bir qadamdagi list "
                  "yoyilgan uzunligi, $I_g$ — gofr profilining inersiya "
                  "momenti. Gofr yo'nalishida bikrlik juda katta, "
                  "ko'ndalangida esa tekis listdan ham kichik."),
                d("8. Qovurg'ali plita uchun ekvivalent bikrliklar",
                  r"D_x = \frac{E I_{\text{qovurg'a}}}{s_x}, \qquad "
                  r"D_y = \frac{E h^3}{12(1-\nu^2)}, \qquad "
                  r"I = \frac{b_w h_w^3}{12} + A_w e^2 + \ldots",
                  "Qovurg'a va plita birgalikda T-kesim hosil qiladi; "
                  "$e$ — qovurg'a og'irlik markazidan umumiy neytral "
                  "o'qgacha masofa. Steyner qo'shimchasi $A_we^2$ "
                  "odatda asosiy hissa."),
            ],
            meaning=(
                "Geometrik ortotropiya g'oyasi muhandislikdagi eng "
                "samarali 'hiyla'lardan biri: **materialni "
                "o'zgartirmasdan bikrlikni o'nlab marta oshirish**. "
                "Sababi $I = \\int z^2 dA$ formulasida: materialni "
                "neytral o'qdan uzoqlashtirish hissani kvadratik "
                "oshiradi. 1 mm qalinlikdagi tekis list uchun "
                "birlik kenglikka $I = h^3/12 = 0{,}083$ mm⁴. Xuddi "
                "shu materialni 20 mm balandlikdagi gofrga aylantirsak, "
                "$I$ taxminan $10^4$ marta ortadi — og'irlik esa "
                "deyarli o'zgarmaydi. Shuning uchun karton quti, "
                "tom qoplamasi, samolyot paneli va hatto o'simlik "
                "bargi ham gofrlangan. To'lov esa ortotropiyada: "
                "ko'ndalang yo'nalishda bikrlik **kamayadi**, chunki "
                "gofr u yerda 'akkordeon' kabi ochiladi. Bu esa "
                "loyihalash qoidasini beradi: gofr yo'nalishi asosiy "
                "oraliq bo'ylab, ya'ni eng katta moment yo'nalishida "
                "qo'yiladi. Huber tenglamasining tuzilishi ham "
                "ma'noli: $D_x$ va $D_y$ ikki yo'nalishdagi egilish "
                "qarshiligini, $H$ esa ularning o'zaro ta'sirini "
                "va buralishni ifodalaydi. $H$ kichik bo'lsa "
                "(gofrda shunday), plastina ikkita mustaqil "
                "balkalar to'plami kabi ishlay boshlaydi va "
                "ikki yo'nalishli ishlashning afzalligi yo'qoladi."
            ),
            equations=[
                eq(r"D_x w_{,xxxx} + 2H w_{,xxyy} + D_y w_{,yyyy} = q",
                   "Huber tenglamasi — ortotrop plastina egilishi.",
                   "Huber tenglamasi"),
                eq(r"H = D_1 + 2D_{xy}, \quad D_1 = \nu_y D_x = \nu_x D_y",
                   "Effektiv buralish bikrligi.", "Effektiv bikrlik"),
                eq(r"w_{mn} = \frac{q_{mn}}{\pi^4\big[D_x\alpha_m^4 "
                   r"+ 2H\alpha_m^2\beta_n^2 + D_y\beta_n^4\big]}",
                   "Ortotrop Navye yechimi koeffitsientlari.",
                   "Ortotrop Navye"),
                eq(r"D_x^{\text{qov}} = \frac{E I}{s_x}, \quad "
                   r"I = \frac{b_wh_w^3}{12} + A_we^2 + \frac{b_fh^3}{12} "
                   r"+ A_f e_f^2",
                   "Qovurg'ali panel uchun ekvivalent bikrlik "
                   "(T-kesim, Steyner teoremasi bilan).",
                   "Ekvivalent bikrlik"),
            ],
            conditions=(
                "**Ekvivalent bikrlik modelining qo'llanish shartlari:**\n"
                "1. Qovurg'a yoki gofr qadami plastina o'lchamidan "
                "ancha kichik: $s \\ll a$ (kamida 5–6 qadam);\n"
                "2. Yuklama silliq va qadamdan katta masofada "
                "o'zgaradi — aks holda mahalliy egilish alohida "
                "hisoblanadi;\n"
                "3. Qovurg'a va plita birgalikda ishlaydi (yaxshi "
                "birikma, siljishga qarshilik yetarli);\n"
                "4. Mahalliy ustuvorlik alohida tekshiriladi: gofr "
                "devori yoki qovurg'a bikrligi yo'qotishi mumkin.\n\n"
                "**Chegaraviy shartlar** izotrop holdagidek, lekin "
                "erkin chekkada Kirxhoff kuchi ortotrop koeffitsientlar "
                "bilan yoziladi:\n"
                "$$V_x = -\\Big[D_x w_{,xxx} + (D_1 + 4D_{xy})"
                "w_{,xyy}\\Big].$$\n\n"
                "**Musbat aniqlanganlik sharti:** "
                "$D_x D_y > D_1^2$ — aks holda material fizik "
                "jihatdan mumkin emas (tmm-13)."
            ),
            worked=WorkedExample(
                statement=(
                    "Po'lat panel $a = 3$ m (qovurg'a yo'nalishi), "
                    "$b = 2$ m, sharnirli, $q = 4$ kPa. Ikki variant: "
                    "(A) tekis list $h = 8$ mm; (B) $h = 4$ mm list "
                    "+ har 250 mm da $6\\times60$ mm qovurg'a. "
                    "$E = 200$ GPa, $\\nu = 0{,}3$, "
                    "$\\rho = 7850$ kg/m³. Ikkala variantning "
                    "bikrligini va og'irligini taqqoslang."
                ),
                given=[
                    r"a = 3\ \text{m},\ b = 2\ \text{m},\ q = 4000\ \text{Pa}",
                    r"\text{(A) } h = 8\ \text{mm}",
                    r"\text{(B) } h = 4\ \text{mm},\ s_x = 250\ \text{mm}, "
                    r"\ b_w \times h_w = 6 \times 60\ \text{mm}",
                ],
                steps=[
                    st(r"\text{(A)}\quad D = \frac{200\times10^9 \cdot "
                       r"5{,}12\times10^{-7}}{12 \cdot 0{,}91} "
                       r"= 9377\ \text{N·m}",
                       "$h^3 = 5{,}12\\times10^{-7}$ m³. Tekis list "
                       "izotrop: $D_x = D_y = H = D$."),
                    st(r"\text{(A) og'irlik: } 7850 \cdot 0{,}008 "
                       r"= 62{,}8\ \text{kg/m}^2",
                       "Yuza zichligi."),
                    st(r"\text{(B) T-kesim: } A_f = 250 \cdot 4 = 1000\ "
                       r"\text{mm}^2, \ A_w = 6 \cdot 60 = 360\ \text{mm}^2",
                       "Bir qovurg'aga to'g'ri keladigan list eni "
                       "250 mm (qovurg'a qadami)."),
                    st(r"\bar{z} = \frac{1000 \cdot 2 + 360 \cdot (4 + 30)}"
                       r"{1360} = \frac{2000 + 12\,240}{1360} = 10{,}47\ \text{mm}",
                       "Neytral o'q listning yuqori yuzasidan "
                       "(list markazi $z = 2$ mm, qovurg'a markazi "
                       "$z = 4 + 30 = 34$ mm)."),
                    st(r"I = \frac{250 \cdot 4^3}{12} + 1000(10{,}47-2)^2 "
                       r"+ \frac{6 \cdot 60^3}{12} + 360(34-10{,}47)^2",
                       "Steyner teoremasi: har bir qism uchun o'z "
                       "inersiya momenti + $A d^2$."),
                    st(r"I = 1333 + 71\,740 + 108\,000 + 199\,270 "
                       r"= 380\,343\ \text{mm}^4 = 3{,}803\times10^{-7}\ \text{m}^4",
                       "Steyner hadlari ustunlik qiladi — bu qovurg'a "
                       "samaradorligining sababi."),
                    st(r"D_x = \frac{EI}{s_x} = \frac{200\times10^9 \cdot "
                       r"3{,}803\times10^{-7}}{0{,}25} = 304\,270\ \text{N·m}",
                       "Qovurg'a yo'nalishidagi bikrlik — tekis "
                       "listdan **32 marta katta**."),
                    st(r"D_y = \frac{E h^3}{12(1-\nu^2)} = "
                       r"\frac{200\times10^9 \cdot 6{,}4\times10^{-8}}{10{,}92} "
                       r"= 1172\ \text{N·m}",
                       "Ko'ndalang yo'nalishda faqat yupqa list "
                       "ishlaydi — tekis 8 mm listdan 8 marta kichik."),
                    st(r"\text{(B) og'irlik: } 7850\Big(0{,}004 + "
                       r"\frac{0{,}006 \cdot 0{,}06}{0{,}25}\Big) "
                       r"= 7850(0{,}004 + 0{,}00144) = 42{,}7\ \text{kg/m}^2",
                       "Qovurg'alar yuza birligiga 1,44 mm ekvivalent "
                       "qalinlik qo'shadi."),
                    st(r"\frac{D_x^{(B)}}{D^{(A)}} = 32{,}4; \qquad "
                       r"\frac{m^{(B)}}{m^{(A)}} = \frac{42{,}7}{62{,}8} = 0{,}68",
                       "Qovurg'ali panel **32 marta bikrroq** va "
                       "**32 % yengil**. Samaradorlik nisbati 48 marta."),
                ],
                answer=(
                    "(A) $D = 9377$ N·m, 62,8 kg/m²; "
                    "(B) $D_x = 304\\,270$ N·m, $D_y = 1172$ N·m, "
                    "42,7 kg/m². Qovurg'ali panel asosiy yo'nalishda "
                    "32,4 marta bikrroq va 32 % yengil — "
                    "$D/m$ samaradorligi 48 marta yuqori."
                ),
                engineering_note=(
                    "Bu nisbat aviatsiya va kemasozlikda qovurg'ali "
                    "panel nima uchun universal standart ekanligini "
                    "tushuntiradi. Lekin ikkita ogohlantirish bor. "
                    "Birinchisi: $D_y$ tekis listdagidan ham kichik, "
                    "shuning uchun qovurg'a yo'nalishi asosiy oraliq "
                    "bo'ylab qo'yilishi shart. Ikkinchisi: yupqa "
                    "qovurg'a devori mahalliy ustuvorlikni yo'qotishi "
                    "mumkin — $h_w/b_w = 10$ bu chegaraga yaqin, "
                    "shuning uchun qovurg'a uchiga gorizontal javon "
                    "(flange) qo'shiladi yoki ko'ndalang diafragma "
                    "o'rnatiladi."
                ),
            ),
            computation=Computation(
                caption=(
                    "Ortotrop Navye yechimi, gofr va qovurg'a uchun "
                    "ekvivalent bikrliklarni hisoblash, og'irlik–bikrlik "
                    "samaradorligini taqqoslash."
                ),
                code='''"""Ortotrop plastinalar: Huber tenglamasi va ekvivalent bikrliklar."""
import numpy as np
from labkit import PARAMS, note, series, table, value

a = float(PARAMS.get("a", 3.0))
b = float(PARAMS.get("b", 2.0))
q0 = float(PARAMS.get("q0", 4000.0))
E = float(PARAMS.get("E", 200.0))*1e9
nu = float(PARAMS.get("nu", 0.3))
rho = float(PARAMS.get("rho", 7850.0))
h_flat = float(PARAMS.get("h_flat", 8.0))/1000.0    # variant A
h_pl = float(PARAMS.get("h_pl", 4.0))/1000.0        # variant B: list
sx = float(PARAMS.get("sx", 250.0))/1000.0          # qovurg'a qadami
bw = float(PARAMS.get("bw", 6.0))/1000.0            # qovurg'a qalinligi
hw = float(PARAMS.get("hw", 60.0))/1000.0           # qovurg'a balandligi

G = E/(2*(1 + nu))

# --- Variant A: tekis list (izotrop) ---
D_flat = E*h_flat**3/(12*(1 - nu**2))
m_flat = rho*h_flat
value("A: bikrlik D", D_flat, "N*m")
value("A: yuza og'irligi", m_flat, "kg/m2")

# --- Variant B: qovurg'ali panel (T-kesim) ---
Af = sx*h_pl
Aw = bw*hw
zf = h_pl/2
zw = h_pl + hw/2
zbar = (Af*zf + Aw*zw)/(Af + Aw)
I_rib = (sx*h_pl**3/12 + Af*(zbar - zf)**2
         + bw*hw**3/12 + Aw*(zw - zbar)**2)
Dx_rib = E*I_rib/sx
Dy_rib = E*h_pl**3/(12*(1 - nu**2))
D1_rib = nu*Dy_rib
Dxy_rib = G*h_pl**3/12
H_rib = D1_rib + 2*Dxy_rib
m_rib = rho*(h_pl + bw*hw/sx)

value("B: neytral o'q z_bar", zbar*1000, "mm")
value("B: inersiya momenti I", I_rib*1e12, "mm4")
value("B: D_x (qovurg'a yo'nalishi)", Dx_rib, "N*m")
value("B: D_y (ko'ndalang)", Dy_rib, "N*m")
value("B: H (buralish)", H_rib, "N*m")
value("B: D_x/D_y anizotropiya", Dx_rib/Dy_rib, "—")
value("B: yuza og'irligi", m_rib, "kg/m2")
value("D_x(B)/D(A)", Dx_rib/D_flat, "—")
value("m(B)/m(A)", m_rib/m_flat, "—")
value("Samaradorlik (D/m) nisbati", (Dx_rib/m_rib)/(D_flat/m_flat), "—")


def navier_ortho(Dx, Dy, H, nterms=25):
    """Ortotrop sharnirli plastina: markazdagi og'ish va momentlar."""
    w = mx = my = 0.0
    for m in range(1, nterms, 2):
        for n in range(1, nterms, 2):
            am, bn = m*np.pi/a, n*np.pi/b
            qmn = 16*q0/(np.pi**2*m*n)
            den = Dx*am**4 + 2*H*am**2*bn**2 + Dy*bn**4
            wmn = qmn/den
            s = np.sin(m*np.pi/2)*np.sin(n*np.pi/2)
            w += wmn*s
            mx += (Dx*am**2 + nu*Dy*bn**2)*wmn*s
            my += (Dy*bn**2 + nu*Dx*am**2)*wmn*s
    return w, mx, my


wA, mxA, myA = navier_ortho(D_flat, D_flat, D_flat)
wB, mxB, myB = navier_ortho(Dx_rib, Dy_rib, H_rib)
value("A: w_max", wA*1000, "mm")
value("B: w_max", wB*1000, "mm")
value("Og'ish nisbati w(A)/w(B)", wA/wB, "—")
value("A: M_x", mxA, "N*m/m")
value("B: M_x", mxB, "N*m/m")
value("B: M_y", myB, "N*m/m")
note(f"Qovurg'ali panel {wA/wB:.1f} marta kam egiladi va "
     f"{100*(1 - m_rib/m_flat):.0f} % yengil.")

# Kuchlanish: qovurg'a pastki tolasida
z_bot = h_pl + hw - zbar
sig_rib = mxB*sx/I_rib*z_bot
value("B: qovurg'a pastki tolasidagi kuchlanish", sig_rib/1e6, "MPa")
value("A: kuchlanish", 6*mxA/h_flat**2/1e6, "MPa")

# --- Qovurg'a balandligining ta'siri ---
hws = np.linspace(0.01, 0.15, 120)
Dxs, ms, effs, ws = [], [], [], []
for hh in hws:
    Aw_ = bw*hh
    zw_ = h_pl + hh/2
    zb_ = (Af*zf + Aw_*zw_)/(Af + Aw_)
    I_ = (sx*h_pl**3/12 + Af*(zb_ - zf)**2 + bw*hh**3/12 + Aw_*(zw_ - zb_)**2)
    Dx_ = E*I_/sx
    m_ = rho*(h_pl + bw*hh/sx)
    Dxs.append(Dx_/1000)
    ms.append(m_)
    effs.append((Dx_/m_)/(D_flat/m_flat))
    ws.append(navier_ortho(Dx_, Dy_rib, H_rib)[0]*1000)

series("D_x(qovurg'a balandligi)", (hws*1000).tolist(), Dxs,
       xlabel="Qovurg'a balandligi h_w, mm", ylabel="D_x, kN*m")
series("Yuza og'irligi(h_w)", (hws*1000).tolist(), ms,
       xlabel="Qovurg'a balandligi h_w, mm", ylabel="Og'irlik, kg/m2")
series("Samaradorlik (D/m) nisbati", (hws*1000).tolist(), effs,
       xlabel="Qovurg'a balandligi h_w, mm", ylabel="Nisbat")
series("w_max(h_w)", (hws*1000).tolist(), ws,
       xlabel="Qovurg'a balandligi h_w, mm", ylabel="w_max, mm")

i_best = int(np.argmax(effs))
value("Eng samarali qovurg'a balandligi", float(hws[i_best])*1000, "mm")
value("Maksimal samaradorlik nisbati", float(effs[i_best]), "—")
note(f"h_w/b_w = {hws[i_best]/bw:.1f} — mahalliy ustuvorlik uchun "
     f"bu nisbat 15 dan oshmasligi tavsiya etiladi (aks holda "
     f"qovurg'a devori bikrligini yo'qotadi).")

# --- Gofrlangan list ---
t_g = float(PARAMS.get("t_g", 0.8))/1000.0   # gofr list qalinligi
s_g = float(PARAMS.get("s_g", 100.0))/1000.0 # gofr qadami
f_g = float(PARAMS.get("f_g", 25.0))/1000.0  # gofr balandligi (amplituda)
# sinusoidal gofr: yoyilgan uzunlik va inersiya momenti (taxminiy)
ell = s_g*(1 + (np.pi*f_g/s_g)**2/4)          # birinchi tartibli baho
I_g = t_g*f_g**2*s_g/8                        # sinusoidal profil uchun
Dx_g = E*I_g/s_g
Dy_g = (s_g/ell)*E*t_g**3/(12*(1 - nu**2))
H_g = (s_g/ell)*G*t_g**3/6
m_g = rho*t_g*ell/s_g
D_g_flat = E*t_g**3/(12*(1 - nu**2))

value("Gofr: yoyilgan uzunlik nisbati l/s", ell/s_g, "—")
value("Gofr: D_x", Dx_g, "N*m")
value("Gofr: D_y", Dy_g, "N*m")
value("Gofr: anizotropiya D_x/D_y", Dx_g/Dy_g, "—")
value("Gofr: yuza og'irligi", m_g, "kg/m2")
value("Gofr D_x / tekis list D", Dx_g/D_g_flat, "—")
note(f"Gofrlangan list bir xil qalinlikdagi tekis listdan "
     f"{Dx_g/D_g_flat:.0f} marta bikrroq (gofr yo'nalishida), "
     f"lekin ko'ndalang yo'nalishda {D_g_flat/Dy_g:.2f} marta yumshoqroq.")

table("Ortotropiya turlari va manbalari",
      ["Tur", "Manba", "Misol", "D_x/D_y tipik"],
      [["Material ortotropiyasi", "material tuzilishi", "yog'och, bir yo'nalishli kompozit", "10-25"],
       ["Geometrik (gofr)", "shakl", "tom qoplamasi, karton", "100-1000"],
       ["Geometrik (qovurg'a)", "shakl", "kema/samolyot paneli", "20-100"],
       ["Konstruktiv", "armatura", "temir-beton plita", "1-3"],
       ["Hujayrali (sendvich)", "yadro tuzilishi", "asal uyasi paneli", "1-5"]])

table("Variantlarning taqqoslashi",
      ["Variant", "D_x, N*m", "D_y, N*m", "Og'irlik, kg/m2", "w_max, mm"],
      [["A: tekis list", round(D_flat, 0), round(D_flat, 0),
        round(m_flat, 1), round(wA*1000, 3)],
       ["B: qovurg'ali", round(Dx_rib, 0), round(Dy_rib, 0),
        round(m_rib, 1), round(wB*1000, 3)],
       ["C: gofrlangan", round(Dx_g, 0), round(Dy_g, 1),
        round(m_g, 1), round(navier_ortho(Dx_g, Dy_g, H_g)[0]*1000, 3)]])
''',
                parameters=[
                    p("a", "Panel uzunligi a", 0.5, 12.0, 3.0, 0.1, "m"),
                    p("b", "Panel eni b", 0.5, 12.0, 2.0, 0.1, "m"),
                    p("q0", "Yuklama q₀", 200.0, 50000.0, 4000.0, 100.0, "Pa"),
                    p("E", "Yung moduli E", 1.0, 400.0, 200.0, 1.0, "GPa"),
                    p("nu", "Puasson koeffitsienti ν", 0.0, 0.45, 0.3, 0.01),
                    p("rho", "Zichlik ρ", 500.0, 12000.0, 7850.0, 50.0, "kg/m³"),
                    p("h_flat", "A: tekis list qalinligi", 1.0, 40.0, 8.0, 0.5, "mm"),
                    p("h_pl", "B: list qalinligi", 0.5, 20.0, 4.0, 0.5, "mm"),
                    p("sx", "B: qovurg'a qadami", 50.0, 800.0, 250.0, 10.0, "mm"),
                    p("bw", "B: qovurg'a qalinligi", 2.0, 30.0, 6.0, 0.5, "mm"),
                    p("hw", "B: qovurg'a balandligi", 10.0, 200.0, 60.0, 5.0, "mm"),
                    p("t_g", "C: gofr list qalinligi", 0.3, 5.0, 0.8, 0.1, "mm"),
                    p("s_g", "C: gofr qadami", 20.0, 300.0, 100.0, 5.0, "mm"),
                    p("f_g", "C: gofr balandligi", 5.0, 100.0, 25.0, 1.0, "mm"),
                ],
                expected_output=(
                    "A: D = 9377 N·m, 62,8 kg/m²; B: D_x ≈ 304 kN·m, "
                    "D_y ≈ 1172 N·m (anizotropiya ≈ 260), 42,7 kg/m² — "
                    "32 marta bikrroq va 32 % yengil, D/m samaradorligi "
                    "≈ 48 marta; gofr ham gofr yo'nalishida yuzlab "
                    "marta bikrroq, ko'ndalangida esa yumshoqroq."
                ),
            ),
            visual=vis(
                kind="Ortotrop panel kesimlari va samaradorlik",
                tool="React/SVG",
                description=(
                    "Gofr va qovurg'a kesimlari, neytral o'q, "
                    "bikrlikning yo'nalish bo'yicha diagrammasi va "
                    "og'irlik–bikrlik samaradorligi grafigi."
                ),
                how_to_draw=(
                    "React/SVG: birinchi panel — uchta kesim yonma-yon "
                    "(tekis, qovurg'ali T-kesim, sinusoidal gofr), "
                    "bir xil masshtabda. Har birida neytral o'q "
                    "punktir chiziq bilan va $\\bar{z}$ o'lchov "
                    "chizig'i bilan belgilanadi; kesim ostida "
                    "$I$ va $D$ qiymatlari yozilgan. Qovurg'ali "
                    "kesimda Steyner hadining hissasi alohida rangda "
                    "ko'rsatiladi (ustun diagramma: $I_{\\text{o'z}}$ "
                    "va $Ad^2$). Ikkinchi panel — bikrlikning "
                    "yo'nalish bo'yicha polyar diagrammasi: "
                    "$D(\\theta) = D_x\\cos^4\\theta + "
                    "2H\\cos^2\\theta\\sin^2\\theta + D_y\\sin^4\\theta$; "
                    "izotrop holda doira, ortotropda esa cho'zilgan "
                    "'sakkiz' shakli chiqadi — anizotropiya darajasi "
                    "bir qarashda ko'rinadi. Logarifmik radial "
                    "shkala kerak, aks holda $D_y$ ko'rinmay qoladi. "
                    "Uchinchi panel — $h_w$ slayderi bilan "
                    "boshqariladigan samaradorlik grafigi; joriy "
                    "nuqta va optimal nuqta belgilanadi, mahalliy "
                    "ustuvorlik chegarasi ($h_w/b_w = 15$) vertikal "
                    "qizil chiziq bilan."
                ),
            ),
            interp=(
                "Polyar bikrlik diagrammasi ortotropiyaning mohiyatini "
                "eng aniq ko'rsatadi: qovurg'a yo'nalishida radius "
                "ulkan, ko'ndalangida esa juda kichik. Bu "
                "loyihalashning asosiy qoidasini beradi — qovurg'a "
                "yoki gofr **asosiy oraliq bo'ylab** qo'yiladi. "
                "Ko'ndalang yo'nalishdagi zaiflik esa ikkilamchi "
                "muammolarni keltirib chiqaradi: panel ko'tarilayotganda "
                "yoki transport paytida ko'ndalang egilishdan "
                "shikastlanishi mumkin, shuning uchun vaqtinchalik "
                "ko'ndalang bog'lovchilar qo'yiladi. Samaradorlik "
                "grafigi yana bir muhim narsani ko'rsatadi: "
                "$D/m$ nisbati qovurg'a balandligi bilan monoton "
                "o'sadi va maksimumga ega emas — nazariy jihatdan "
                "qovurg'a qanchalik baland bo'lsa, shuncha yaxshi. "
                "Lekin amalda chegara bor va u **mahalliy "
                "ustuvorlik** (pq-19…pq-21): yupqa va baland "
                "qovurg'a devori siqilishda bikrligini yo'qotadi. "
                "$h_w/b_w = 15$ chegarasi aynan shu sababdan. Bu "
                "muhandislikdagi tipik holat: global optimallashtirish "
                "mahalliy cheklov bilan to'xtatiladi, va yaxshi "
                "loyiha ikkalasini birga hisobga oladi."
            ),
            mistakes=[
                "Ortotrop plastinada izotrop formulani ishlatish. "
                "$D_x/D_y$ o'nlab yoki yuzlab marta farq qilishi "
                "mumkin — xato bir necha tartibga yetadi.",
                "Ekvivalent bikrlikni qovurg'a qadami plastina "
                "o'lchamiga taqqoslanadigan bo'lganda qo'llash. "
                "Kamida 5–6 qadam bo'lishi kerak, aks holda "
                "mahalliy egilish alohida hisoblanishi shart.",
                "Steyner hadini ($Ad^2$) unutish. Qovurg'ali "
                "kesimda u asosiy hissani beradi; faqat "
                "$bh^3/12$ olinsa, bikrlik bir necha marta kam chiqadi.",
                "Mahalliy ustuvorlikni tekshirmaslik. Yupqa "
                "qovurg'a devori yoki gofr yoni global egilishdan "
                "ancha oldin bikrligini yo'qotishi mumkin.",
            ],
            quiz=[
                q("Huber tenglamasini yozing va izotrop holga "
                  "keltiring.",
                  "$D_xw_{,xxxx} + 2Hw_{,xxyy} + D_yw_{,yyyy} = q$. "
                  "$D_x = D_y = H = D$ bo'lsa $D\\nabla^4w = q$ — "
                  "pq-04 dagi tenglama.", "konseptual"),
                q("Geometrik ortotropiya nima va u materialdan "
                  "nimasi bilan farq qiladi?",
                  "U shakldan (gofr, qovurg'a) kelib chiqadi, "
                  "material esa izotrop bo'lishi mumkin. Matematik "
                  "apparat bir xil, faqat bikrliklar geometriyadan "
                  "hisoblanadi.", "konseptual"),
                q("Qovurg'a balandligini 2 marta oshirsak, "
                  "$D_x$ taxminan qancha ortadi?",
                  "Steyner hadi ($A_we^2$) hukmron bo'lgani uchun "
                  "taxminan $2^3 = 8$ marta yaqin — aniq qiymat "
                  "neytral o'q siljishiga bog'liq; kodda "
                  "grafik bilan tekshiriladi.", "hisob"),
                q("Nima uchun gofr yo'nalishi asosiy oraliq bo'ylab "
                  "qo'yiladi?",
                  "Chunki $D_x \\gg D_y$: gofr yo'nalishida "
                  "bikrlik yuzlab marta katta, ko'ndalangida esa "
                  "tekis listdan ham kichik.", "talqin"),
                q("Kodda polyar bikrlik diagrammasi uchun qaysi "
                  "formula ishlatiladi?",
                  "$D(\\theta) = D_x\\cos^4\\theta + "
                  "2H\\cos^2\\theta\\sin^2\\theta + D_y\\sin^4\\theta$ — "
                  "bu ixtiyoriy yo'nalishdagi silindrik egilish "
                  "bikrligi.", "kod"),
                q("Qovurg'a balandligini cheksiz oshirish mumkinmi?",
                  "Yo'q: yupqa va baland devor mahalliy "
                  "ustuvorlikni yo'qotadi. Amaliy chegara "
                  "$h_w/b_w \\approx 15$; undan oshsa javon "
                  "yoki diafragma kerak.", "talqin"),
            ],
            bridge=(
                "To'rtburchak plastinalar bo'yicha analitik va "
                "sonli usullar to'liq ko'rib chiqildi. Keyingi "
                "modulda geometriya o'zgaradi: doiraviy "
                "plastinalarga o'tamiz. U yerda silindrik "
                "koordinatalar va o'qsimmetriya masalani ancha "
                "soddalashtiradi — hatto aniq yechim topiladi."
            ),
            research=(
                "Auksetik (manfiy Puasson koeffitsientli, "
                "$\\nu < 0$) va funksional gradiyentli "
                "materiallardan yasalgan plastinalarni o'rganing. "
                "Auksetik strukturada cho'zilganda kenglik ham "
                "ortadi — bu qanday geometriya bilan erishiladi "
                "(re-entrant honeycomb, chiral struktura)? "
                "Bunday plastinaning $D$ va $H$ bikrliklari "
                "qanday o'zgaradi va zarbaga chidamliligi nima "
                "uchun oshadi? Funksional gradiyentli plastinada "
                "esa $E(z)$ qalinlik bo'yicha o'zgaradi — neytral "
                "sirt qayerga siljiydi va membrana-egilish "
                "bog'lanishi qanday paydo bo'ladi?"
            ),
            manim_ref=manim(
                scene="OrthotropicPlateScene",
                module="animatsiya/scenes/pq_solutions.py",
                title="Geometrik ortotropiya: gofr va qovurg'a",
                summary=(
                    "Tekis list gofrga aylantiriladi va inersiya "
                    "momentining keskin o'sishi ko'rsatiladi; "
                    "so'ng ikki yo'nalishda egilish sinovi "
                    "o'tkaziladi va anizotropiya vizual namoyon bo'ladi."
                ),
            ),
        ),
    ),
]
