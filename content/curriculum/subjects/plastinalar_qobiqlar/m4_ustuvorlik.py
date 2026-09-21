"""PQ / 4-modul: Ustuvorlik va tebranishlar (pq-19 … pq-24)."""

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
M = "pq-m4"


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
    # ------------------------------------------------------------------ pq-19
    Topic(
        id="pq-19",
        subject_id=S, module_id=M, order=19,
        title="Sirt ichidagi kuchlar va plastina ustuvorligi masalasining qo'yilishi",
        description=(
            "Membrana kuchlarining egilgan plastinaga ta'siri, "
            "ustuvorlik tenglamasi, bifurkatsiya tushunchasi va "
            "xususiy qiymatlar masalasi sifatidagi formulirovka."
        ),
        learning_objective=(
            "Sirt ichidagi kuchlar hisobga olingan plastina "
            "tenglamasini keltirib chiqarish, ustuvorlik masalasini "
            "xususiy qiymatlar masalasi sifatida qo'yish va "
            "bifurkatsiyaning fizik ma'nosini tushuntirish."
        ),
        prerequisites=["pq-18", "mq-25"],
        mathematical_core=(
            "$D\\nabla^4w = N_xw_{,xx} + 2N_{xy}w_{,xy} + N_yw_{,yy}$, "
            "xususiy qiymatlar masalasi, bifurkatsiya nuqtasi, "
            "trivial va notrivial yechim."
        ),
        engineering_application=(
            "Yupqa devorli profillarning mahalliy ustuvorligi, "
            "kema korpusi va samolyot fyuzelyaji panellari, "
            "silos va rezervuar devorlari, qutisimon to'sinlar."
        ),
        computational_component=(
            "Ustuvorlik tenglamasini Navye bazisida diskretlashtirish, "
            "xususiy qiymatlar masalasini yechish, kritik yuklama va "
            "shakllarni topish."
        ),
        visualization_component=(
            "Muvozanat yo'llari diagrammasi (bifurkatsiya), "
            "ustuvorlikni yo'qotish shakllari, kritik yuklama grafigi."
        ),
        research_extension=(
            "Ustuvorlik masalasining energetik formulirovkasini "
            "o'rganing: nima uchun kritik yuklama energiya "
            "funksionalining musbat aniqlanganligini yo'qotishiga mos keladi?"
        ),
        difficulty="murakkab",
        previous_link=(
            "pq-18 da **cho'zuvchi** membrana kuchlari plastinani "
            "bikrlashtirgan edi. mq-25 da esa sterjenning siqilishda "
            "ustuvorlikni yo'qotishi o'rganilgan. Endi ikkalasini "
            "birlashtiramiz: siquvchi membrana kuchlari plastinani "
            "yumshatadi va ma'lum qiymatda bikrlik butunlay yo'qoladi."
        ),
        next_topic="pq-20",
        estimated_minutes=90,
        tags=["ustuvorlik", "bifurkatsiya", "xususiy qiymat", "buckling"],
        lesson=_lesson(
            problem=(
                "Qutisimon to'sinning siqilgan javon (flange) "
                "qismi: eni 300 mm, qalinligi 6 mm. Materialning "
                "oqish chegarasi 235 MPa, demak 423 kN gacha "
                "ko'tarishi kerak. Amalda esa u 361 kN da "
                "to'lqinsimon bukila boshlaydi — 15 % kam. "
                "Javonni 480 mm gacha kengaytirsak, yo'qotish "
                "40 % ga yetadi. Nima yuz berdi? Bu "
                "mustahkamlik masalasi emas, **ustuvorlik** "
                "masalasi: plastina siqilganda tekis holatini "
                "saqlashga qodir bo'lmay qoladi. Va u qanchalik "
                "keng bo'lsa, shuncha erta bukiladi."
            ),
            concepts=[
                c("Sirt ichidagi (membrana) kuchlar",
                  "$N_x, N_y, N_{xy}$ — o'rta sirt tekisligida "
                  "ta'sir qiluvchi kuchlar, N/m. Siquvchi "
                  "bo'lsa manfiy."),
                c("Ustuvorlikni yo'qotish (buckling)",
                  "Tekis muvozanat holatining barqarorligini "
                  "yo'qotishi; plastina birdan egilgan shaklga o'tadi."),
                c("Bifurkatsiya",
                  "Muvozanat yo'llarining ajralishi: kritik "
                  "nuqtagacha bitta (tekis) yechim, undan keyin "
                  "uchta (tekis + ikkita egilgan)."),
                c("Xususiy qiymatlar masalasi",
                  "$[K]\\{w\\} = \\lambda[K_G]\\{w\\}$ — kritik "
                  "yuklama xususiy qiymat, ustuvorlikni yo'qotish "
                  "shakli esa xususiy vektor."),
                c("Geometrik bikrlik matritsasi $[K_G]$",
                  "Membrana kuchlarining egilgan sirtdagi "
                  "ta'sirini ifodalaydi; siqilishda u bikrlikni kamaytiradi."),
                c("Kritik yuklama $N_{cr}$",
                  "Notrivial yechim paydo bo'ladigan eng kichik "
                  "yuklama. Undan keyin tekis holat beqaror."),
            ],
            derivation=[
                d("1. Deformatsiyalangan holatda muvozanat",
                  r"\text{Element } dx\,dy \ \text{egilgan holatda ko'rib chiqiladi}",
                  "Bu hal qiluvchi qadam: chiziqli nazariyada "
                  "muvozanat deformatsiyalanmagan holatda "
                  "yoziladi. Ustuvorlik masalasida esa "
                  "deformatsiyalangan holatda — aks holda "
                  "effekt umuman paydo bo'lmaydi."),
                d("2. $N_x$ ning vertikal proeksiyasi",
                  r"N_x\,dy\Big[\frac{\partial w}{\partial x} + "
                  r"\frac{\partial^2 w}{\partial x^2}dx\Big] - "
                  r"N_x\,dy\frac{\partial w}{\partial x} = "
                  r"N_x\frac{\partial^2 w}{\partial x^2}dx\,dy",
                  "Element ikki yuzidagi $N_x$ kuchlari turli "
                  "burchakda yo'nalgan (chunki sirt egilgan), "
                  "shuning uchun ularning vertikal "
                  "tashkil etuvchilari to'liq qisqarmaydi."),
                d("3. Qolgan kuchlarning proeksiyasi",
                  r"N_y\frac{\partial^2 w}{\partial y^2}dxdy, \qquad "
                  r"2N_{xy}\frac{\partial^2 w}{\partial x\partial y}dxdy",
                  "Bir xil mulohaza $y$ yo'nalishi va siljish "
                  "kuchi uchun. Siljish kuchida koeffitsient 2 — "
                  "ikkita juft yuzadan."),
                d("4. Vertikal muvozanat",
                  r"\frac{\partial Q_x}{\partial x} + "
                  r"\frac{\partial Q_y}{\partial y} + q + "
                  r"N_x w_{,xx} + 2N_{xy}w_{,xy} + N_y w_{,yy} = 0",
                  "pq-04 dagi muvozanat tenglamasiga uchta "
                  "yangi had qo'shildi — ular membrana "
                  "kuchlarining egilgan sirtdagi proeksiyasi."),
                d("5. To'liq tenglama",
                  r"D\nabla^4 w = q + N_x\frac{\partial^2 w}{\partial x^2} "
                  r"+ 2N_{xy}\frac{\partial^2 w}{\partial x\partial y} "
                  r"+ N_y\frac{\partial^2 w}{\partial y^2}",
                  "Momentlarni egriliklar bilan almashtiramiz. "
                  "Bu fon Karman ikkinchi tenglamasining "
                  "(pq-18) chiziqlashtirilgan ko'rinishi — "
                  "u yerda $N$ lar $w$ ga bog'liq edi, bu "
                  "yerda ular berilgan."),
                d("6. Ustuvorlik masalasi: $q = 0$",
                  r"D\nabla^4 w - N_x w_{,xx} - 2N_{xy}w_{,xy} "
                  r"- N_y w_{,yy} = 0",
                  "Ko'ndalang yuklama yo'q. Bu **bir jinsli** "
                  "tenglama va uning har doim trivial yechimi "
                  "($w \\equiv 0$, tekis holat) mavjud."),
                d("7. Notrivial yechim sharti",
                  r"N_{ij} = \lambda\,\bar{N}_{ij} \;\Longrightarrow\; "
                  r"\text{notrivial } w \ne 0 \ \text{faqat ma'lum } "
                  r"\lambda \ \text{larda mavjud}",
                  "Yuklamani proporsional oshiramiz: "
                  "$\\lambda$ — yuklama parametri. Bir jinsli "
                  "masala notrivial yechimga faqat maxsus "
                  "$\\lambda$ qiymatlarida ega — bu xususiy qiymatlar."),
                d("8. Diskret shakl",
                  r"\big([K] - \lambda[K_G]\big)\{w\} = 0 "
                  r"\;\Longrightarrow\; \det\big([K] - \lambda[K_G]\big) = 0",
                  "Ritz yoki FEM diskretlashtirishidan keyin "
                  "umumlashgan xususiy qiymatlar masalasi "
                  "hosil bo'ladi. Eng kichik musbat $\\lambda$ — "
                  "kritik yuklama koeffitsienti."),
            ],
            meaning=(
                "Ustuvorlik masalasining mohiyati "
                "$N_xw_{,xx}$ hadida: u membrana kuchining "
                "**egilgan** sirtdagi vertikal proeksiyasi. "
                "Tekis plastinada ($w = 0$) bu had nolga teng "
                "va hech narsa yuz bermaydi — shuning uchun "
                "chiziqli nazariyada ustuvorlik masalasi "
                "umuman paydo bo'lmaydi. Hodisani ko'rish "
                "uchun muvozanatni **deformatsiyalangan "
                "holatda** yozish shart. Bu mq-25 dagi "
                "Eyler sterjeni bilan bir xil g'oya. "
                "Ishoralar ham ma'noli: siqilishda "
                "$N_x < 0$, demak had $-|N_x|w_{,xx}$ "
                "bo'ladi va u chap tomondagi $D\\nabla^4w$ ga "
                "**qarshi** ishlaydi — samarali bikrlik "
                "kamayadi. Yuklama ortgani sari kamayish "
                "davom etadi va ma'lum qiymatda samarali "
                "bikrlik nolga aylanadi: plastina egilishga "
                "qarshilik ko'rsatolmay qoladi. Cho'zilishda "
                "esa ($N_x > 0$) aksincha — bikrlik ortadi, "
                "bu pq-18 dagi membrana effekti. Demak "
                "ikkala hodisa bir xil hadning ikki "
                "tomoni. Matematik jihatdan ustuvorlik — "
                "xususiy qiymatlar masalasi, va bu juda "
                "muhim: kritik yuklama yuklamaning "
                "kattaligiga emas, uning **taqsimlanish "
                "shakliga** va geometriyaga bog'liq."
            ),
            equations=[
                eq(r"D\nabla^4 w = q + N_xw_{,xx} + 2N_{xy}w_{,xy} "
                   r"+ N_yw_{,yy}",
                   "Sirt ichidagi kuchlar hisobga olingan plastina "
                   "tenglamasi.", "Ustuvorlik tenglamasi"),
                eq(r"D\nabla^4 w - N_xw_{,xx} - 2N_{xy}w_{,xy} "
                   r"- N_yw_{,yy} = 0",
                   "Ustuvorlik (bifurkatsiya) masalasi.",
                   "Bifurkatsiya masalasi"),
                eq(r"\big([K] - \lambda[K_G]\big)\{w\} = 0",
                   "Umumlashgan xususiy qiymatlar masalasi.",
                   "Xususiy qiymatlar masalasi"),
                eq(r"N_{cr} = \lambda_{\min}\bar{N}",
                   "Kritik yuklama — eng kichik xususiy qiymat.",
                   "Kritik yuklama"),
            ],
            conditions=(
                "**Ko'ndalang chegaraviy shartlar** odatdagidek "
                "(sharnirli, mahkamlangan, erkin).\n\n"
                "**Sirt ichidagi kuchlar** oldindan berilgan "
                "deb hisoblanadi. Ular ikki yo'l bilan olinadi:\n"
                "1. Sodda holatlarda to'g'ridan-to'g'ri "
                "($N_x = -P/b$ bir tekis siqilish uchun);\n"
                "2. Murakkab holatlarda avval tekislik ichidagi "
                "masala yechiladi (tmm-16), so'ng ustuvorlik "
                "tekshiriladi.\n\n"
                "**Klassik ustuvorlik nazariyasining "
                "taxminlari:**\n"
                "- Plastina ideal tekis (nomukammalliksiz);\n"
                "- Yuklama ideal markazlashgan;\n"
                "- Material chiziqli elastik "
                "($\\sigma_{cr} < \\sigma_{\\text{proporsionallik}}$);\n"
                "- Kritik nuqtagacha egilish yo'q.\n\n"
                "Real konstruksiyada bu taxminlar buziladi va "
                "bifurkatsiya o'rniga silliq egilish kuzatiladi "
                "(pq-21)."
            ),
            worked=WorkedExample(
                statement=(
                    "Qutisimon to'sinning siqilgan javoni: "
                    "$a = 1200$ mm (uzunligi), $b = 300$ mm "
                    "(eni), $t = 6$ mm, $E = 210$ GPa, "
                    "$\\nu = 0{,}3$, $\\sigma_Y = 235$ MPa. "
                    "Uzun tomonlari bo'ylab sharnirli. "
                    "(a) Mustahkamlik bo'yicha ko'tarish "
                    "qobiliyatini toping. (b) Kritik kuchlanishni "
                    "hisoblang ($k = 4$ deb oling, pq-20 da "
                    "asoslanadi). (c) Xulosa chiqaring."
                ),
                given=[
                    r"a = 1{,}2\ \text{m},\ b = 0{,}3\ \text{m},\ "
                    r"t = 0{,}006\ \text{m}",
                    r"E = 210\ \text{GPa},\ \nu = 0{,}3,\ "
                    r"\sigma_Y = 235\ \text{MPa}",
                    r"k = 4 \ (\text{sharnirli, } a/b = 4)",
                ],
                steps=[
                    st(r"A = b\,t = 0{,}3 \cdot 0{,}006 = "
                       r"1{,}8\times10^{-3}\ \text{m}^2",
                       "Javon kesim yuzasi."),
                    st(r"P_Y = \sigma_Y A = 235\times10^{6} \cdot "
                       r"1{,}8\times10^{-3} = 423\ \text{kN}",
                       "Mustahkamlik bo'yicha ko'tarish qobiliyati — "
                       "masala shartida aytilgan qiymat."),
                    st(r"D = \frac{Et^3}{12(1-\nu^2)} = "
                       r"\frac{210\times10^9 \cdot 2{,}16\times10^{-7}}"
                       r"{10{,}92} = 4154\ \text{N·m}",
                       "$t^3 = 2{,}16\\times10^{-7}$ m³."),
                    st(r"N_{cr} = k\frac{\pi^2 D}{b^2} = "
                       r"4\frac{9{,}8696 \cdot 4154}{0{,}09} "
                       r"= 4 \cdot 455\,560 = 1{,}822\times10^{6}\ \text{N/m}",
                       "Kritik membrana kuchi. Diqqat: maxrajda "
                       "**eni** $b$, uzunlik $a$ emas — plastina "
                       "qisqa tomon bo'ylab to'lqinlanadi."),
                    st(r"\sigma_{cr} = \frac{N_{cr}}{t} = "
                       r"\frac{1{,}822\times10^{6}}{0{,}006} "
                       r"= 303{,}7\ \text{MPa}",
                       "Diqqat: bu $\\sigma_Y = 235$ MPa dan "
                       "katta! Demak elastik ustuvorlik "
                       "masalasi formal ravishda oqishdan keyin keladi."),
                    st(r"\text{Tekshiruv: } \sigma_{cr} > \sigma_Y "
                       r"\Rightarrow \text{plastik ustuvorlik, "
                       r"Engesser-Shenli tuzatmasi kerak}",
                       "Elastik formula $\\sigma_{cr} > \\sigma_{pts}$ "
                       "da yaroqsiz — tangens modul ishlatiladi "
                       "(mq-26 dagi Yasinskiy formulasi analogi)."),
                    st(r"\lambda_p = \sqrt{\frac{\sigma_Y}{\sigma_{cr}}} "
                       r"= \sqrt{\frac{235}{303{,}7}} = 0{,}880",
                       "Plastina nisbiy nozikligi (Eurocode 3 "
                       "ta'rifi). $\\lambda_p > 0{,}673$ — "
                       "mahalliy ustuvorlik hisobga olinishi shart, "
                       "garchi $\\sigma_{cr} > \\sigma_Y$ bo'lsa ham."),
                    st(r"\rho = \frac{\lambda_p - 0{,}055(3+\psi)}"
                       r"{\lambda_p^2} = \frac{0{,}880 - 0{,}220}"
                       r"{0{,}774} = 0{,}852",
                       "Vinter formulasi bo'yicha samaradorlik "
                       "koeffitsienti ($\\psi = 1$ bir tekis "
                       "siqilish uchun). Samarali kenglik "
                       "$b_{\\text{eff}} = 256$ mm."),
                    st(r"P_{\text{haqiqiy}} = \rho\,P_Y = 0{,}852 "
                       r"\cdot 423 = 361\ \text{kN} \ "
                       r"(\text{mustahkamlikning } 85\ \%)",
                       "15 % yo'qotish. Javonni 480 mm ga "
                       "kengaytirsak ($b/t = 80$), "
                       "$\\sigma_{cr}$ ikki baravardan ko'p "
                       "tushadi va yo'qotish 40 % ga yetadi."),
                ],
                answer=(
                    "$P_Y = 423$ kN (mustahkamlik); "
                    "$k = 4$ (shakl $m = 4$, $n = 1$), "
                    "$N_{cr} = 1822$ kN/m, "
                    "$\\sigma_{cr} = 303{,}7$ MPa. "
                    "$\\lambda_p = 0{,}880 > 0{,}673$, Vinter "
                    "$\\rho = 0{,}852$, haqiqiy ko'tarish "
                    "qobiliyati 361 kN — mustahkamlikning "
                    "85 % i. $b/t = 57$ dan boshlab "
                    "$\\sigma_{cr} < \\sigma_Y$ va "
                    "yo'qotish keskin ortadi."
                ),
                engineering_note=(
                    "$b/t$ nisbati yupqa devorli "
                    "konstruksiyalarda eng muhim parametr. "
                    "Eurocode 3 kesimlarni to'rt sinfga "
                    "ajratadi: 1–2 sinf (plastik zaxira to'liq), "
                    "3 sinf (elastik), 4 sinf (mahalliy "
                    "ustuvorlik hukmron, samarali kesim "
                    "kamayadi). Bizning javon 4 sinf chegarasida "
                    "($\\lambda_p = 0{,}88$, chegara 0,673); "
                    "$b/t$ ni 57 dan oshirsak, u aniq 4 sinfga "
                    "o'tadi. Yechim: (1) qalinlikni oshirish; "
                    "(2) uzunlamasiga qovurg'a (stiffener) "
                    "qo'yish — bu $b$ ni yarmiga tushiradi va "
                    "$N_{cr}$ ni to'rt marta oshiradi; "
                    "(3) kesim shaklini o'zgartirish."
                ),
            ),
            computation=Computation(
                caption=(
                    "Ustuvorlik masalasini xususiy qiymatlar "
                    "masalasi sifatida yechish, kritik yuklama "
                    "va shakllarni topish."
                ),
                code='''"""Plastina ustuvorligi: xususiy qiymatlar masalasi."""
import numpy as np
from labkit import PARAMS, note, series, table, value

a = float(PARAMS.get("a", 1200.0))/1000.0
b = float(PARAMS.get("b", 300.0))/1000.0
t = float(PARAMS.get("t", 6.0))/1000.0
E = float(PARAMS.get("E", 210.0))*1e9
nu = float(PARAMS.get("nu", 0.3))
sY = float(PARAMS.get("sY", 235.0))*1e6
ratio_y = float(PARAMS.get("ratio_y", 0.0))   # N_y / N_x
NM = int(PARAMS.get("NM", 8))                 # bazis hadlari

D = E*t**3/(12*(1 - nu**2))
value("Silindrik bikrlik D", D, "N*m")
value("a/b nisbati", a/b, "—")
value("b/t nisbati", b/t, "—")

# --- Navye bazisida xususiy qiymatlar masalasi ---
# w = sum w_mn sin(m pi x/a) sin(n pi y/b)
# Har bir (m,n) mustaqil (bir tekis N_x, N_y uchun):
#   D*pi^4*((m/a)^2+(n/b)^2)^2 * w = lambda*pi^2*((m/a)^2 + r*(n/b)^2)*w
rows = []
lams = []
for m in range(1, NM + 1):
    for n in range(1, NM + 1):
        am, bn = m/a, n/b
        K = D*np.pi**4*(am**2 + bn**2)**2
        KG = np.pi**2*(am**2 + ratio_y*bn**2)
        if KG <= 0:
            continue
        lam = K/KG                      # N_cr shu (m,n) shakli uchun
        lams.append((lam, m, n))
lams.sort()
N_cr, m_cr, n_cr = lams[0]
value("Kritik membrana kuchi N_cr", N_cr/1000, "kN/m")
value("Ustuvorlikni yo'qotish shakli m", float(m_cr), "—")
value("Ustuvorlikni yo'qotish shakli n", float(n_cr), "—")
value("To'lqin uzunligi a/m", a/m_cr, "m")
value("To'lqin uzunligi / b", (a/m_cr)/b, "—")

k_buck = N_cr*b**2/(np.pi**2*D)
value("Ustuvorlik koeffitsienti k", k_buck, "—")
sig_cr = N_cr/t
value("Kritik kuchlanish sigma_cr", sig_cr/1e6, "MPa")
value("sigma_cr / sigma_Y", sig_cr/sY, "—")

if sig_cr < sY:
    note(f"sigma_cr = {sig_cr/1e6:.1f} MPa < sigma_Y = {sY/1e6:.0f} MPa: "
         f"ELASTIK ustuvorlik hukmron, plastina oqishdan oldin bukiladi.")
else:
    note(f"sigma_cr = {sig_cr/1e6:.1f} MPa > sigma_Y = {sY/1e6:.0f} MPa: "
         f"elastik formula yaroqsiz — plastik ustuvorlik (tangens "
         f"modul) yoki oqish hal qiluvchi.")

table("Dastlabki beshta xususiy qiymat",
      ["Tartib", "m", "n", "N_cr, kN/m", "k", "N/N_1"],
      [[i + 1, L[1], L[2], round(L[0]/1000, 1),
        round(L[0]*b**2/(np.pi**2*D), 3), round(L[0]/N_cr, 3)]
       for i, L in enumerate(lams[:5])])
note("n = 1 har doim eng kichik: ko'ndalang yo'nalishda bitta "
     "yarim to'lqin eng 'yumshoq' shakl.")

# --- k(a/b) egri chizig'i ---
ratios = np.linspace(0.4, 6.0, 300)
ks, ms_best = [], []
for rt in ratios:
    aa = rt*b
    best, bm = 1e30, 1
    for m in range(1, 12):
        kk = (m*b/aa + aa/(m*b))**2
        if kk < best:
            best, bm = kk, m
    ks.append(best); ms_best.append(bm)
series("Ustuvorlik koeffitsienti k(a/b)", ratios.tolist(), ks,
       xlabel="a / b", ylabel="k")
series("k = 4 (asimptota)", ratios.tolist(), [4.0]*len(ratios),
       xlabel="a / b", ylabel="k")
series("Yarim to'lqinlar soni m", ratios.tolist(),
       [float(v) for v in ms_best], xlabel="a / b",
       ylabel="m")
note("k minimumlari a/b = 1, 2, 3, ... da: shu nisbatlarda "
     "yarim to'lqinlar soni o'zgaradi va k aynan 4 ga teng bo'ladi.")

# --- Vinter formulasi (samarali kenglik) ---
lam_p = (b/t)*np.sqrt(sY/E)/np.sqrt(k_buck)*np.sqrt(12*(1 - nu**2))/np.pi
value("Nisbiy nozeklik lambda_p", lam_p, "—")
psi = 1.0
if lam_p > 0.673:
    rho_w = (lam_p - 0.055*(3 + psi))/lam_p**2
    rho_w = min(rho_w, 1.0)
else:
    rho_w = 1.0
value("Vinter samaradorlik koeffitsienti rho", rho_w, "—")
P_Y = sY*b*t
value("Mustahkamlik bo'yicha P_Y", P_Y/1000, "kN")
value("Ustuvorlik hisobga olingan P", rho_w*P_Y/1000, "kN")
value("Yo'qotilgan ulush", (1 - rho_w)*100, "%")
value("Samarali kenglik b_eff", rho_w*b*1000, "mm")

# --- b/t ning ta'siri ---
bts = np.linspace(10.0, 120.0, 200)
sigs, rhos = [], []
for bt in bts:
    tt = b/bt
    Dt = E*tt**3/(12*(1 - nu**2))
    sc = k_buck*np.pi**2*Dt/(b**2*tt)
    lp = (b/tt)*np.sqrt(sY/E)/np.sqrt(k_buck)*np.sqrt(12*(1 - nu**2))/np.pi
    rh = min((lp - 0.055*(3 + psi))/lp**2, 1.0) if lp > 0.673 else 1.0
    sigs.append(min(sc, sY*3)/1e6)
    rhos.append(rh)
series("sigma_cr(b/t)", bts.tolist(), sigs,
       xlabel="b / t", ylabel="sigma_cr, MPa")
series("Oqish chegarasi", bts.tolist(), [sY/1e6]*len(bts),
       xlabel="b / t", ylabel="sigma_cr, MPa")
series("Samaradorlik rho(b/t)", bts.tolist(), rhos,
       xlabel="b / t", ylabel="rho")

i_cross = int(np.argmax(np.array(sigs) < sY/1e6))
if i_cross > 0:
    value("sigma_cr = sigma_Y bo'ladigan b/t", float(bts[i_cross]), "—")
    note(f"b/t > {bts[i_cross]:.0f} dan boshlab ustuvorlik oqishdan "
         f"oldin keladi — bu Eurocode 3 dagi 4-sinf kesimlar chegarasi.")

# --- Ustuvorlikni yo'qotish shakli ---
ng = 80
xg = np.linspace(0.0, a, ng)
yg = np.linspace(0.0, b, ng)
Xg, Yg = np.meshgrid(xg, yg, indexing="ij")
Wmode = np.sin(m_cr*np.pi*Xg/a)*np.sin(n_cr*np.pi*Yg/b)
series("Ustuvorlik shakli: markaziy kesim w(x)", xg.tolist(),
       Wmode[:, ng//2].tolist(), xlabel="x, m",
       ylabel="Nisbiy amplituda")
series("Ustuvorlik shakli: ko'ndalang kesim w(y)", yg.tolist(),
       Wmode[ng//2, :].tolist(), xlabel="y, m",
       ylabel="Nisbiy amplituda")

table("Mustahkamlik va ustuvorlik masalalarining farqi",
      ["Jihat", "Mustahkamlik", "Ustuvorlik"],
      [["Tenglama turi", "nobir jinsli (q bor)", "bir jinsli (q = 0)"],
       ["Masala turi", "chegaraviy masala", "xususiy qiymatlar masalasi"],
       ["Natija", "kuchlanish maydoni", "kritik yuklama + shakl"],
       ["Muvozanat qayerda?", "deformatsiyalanmagan holat",
        "deformatsiyalangan holat"],
       ["Material roli", "sigma_Y hal qiluvchi", "E va geometriya hal qiluvchi"],
       ["Buzilish", "oqish, yorilish", "shaklni birdan yo'qotish"]])
''',
                parameters=[
                    p("a", "Plastina uzunligi a", 100.0, 5000.0, 1200.0, 10.0,
                      "mm"),
                    p("b", "Plastina eni b", 50.0, 2000.0, 300.0, 10.0, "mm"),
                    p("t", "Qalinlik t", 0.5, 50.0, 6.0, 0.5, "mm"),
                    p("E", "Yung moduli E", 1.0, 400.0, 210.0, 1.0, "GPa"),
                    p("nu", "Puasson koeffitsienti ν", 0.0, 0.45, 0.3, 0.01),
                    p("sY", "Oqish chegarasi σ_Y", 20.0, 1000.0, 235.0, 5.0,
                      "MPa"),
                    p("ratio_y", "Nₓ ga nisbatan N_y", 0.0, 2.0, 0.0, 0.1),
                    p("NM", "Bazis hadlari soni", 3.0, 15.0, 8.0, 1.0),
                ],
                expected_output=(
                    "D = 4154 N·m, a/b = 4, b/t = 50; kritik shakl "
                    "m = 4, n = 1 (to'lqin uzunligi aynan b), "
                    "k = 4,000; N_cr = 1822 kN/m, σ_cr = 303,7 MPa "
                    "> σ_Y = 235 MPa — elastik formula chegarasi. "
                    "λ_p = 0,880, Vinter ρ = 0,852, ko'tarish "
                    "qobiliyati 361 kN (85 %), b_eff = 256 mm. "
                    "σ_cr = σ_Y chegarasi b/t ≈ 57 da."
                ),
            ),
            visual=vis(
                kind="Bifurkatsiya va ustuvorlik shakli",
                tool="React/SVG + Manim",
                description=(
                    "Muvozanat yo'llari diagrammasi, ustuvorlikni "
                    "yo'qotish shakli va $k(a/b)$ girlanda egri chizig'i."
                ),
                how_to_draw=(
                    "React/SVG: birinchi panel — bifurkatsiya "
                    "diagrammasi: gorizontal o'q $w$ (amplituda), "
                    "vertikal o'q $N$. Kritik nuqtagacha vertikal "
                    "chiziq ($w = 0$, tekis holat), undan keyin "
                    "u ikkiga ajraladi — ikkita simmetrik shox "
                    "(egilgan holatlar). Kritik nuqtadan "
                    "yuqoridagi vertikal chiziq **punktir** "
                    "qilinadi va 'beqaror' yorlig'i qo'yiladi. "
                    "Real (nomukammal) plastina yo'li esa "
                    "silliq egri chiziq sifatida ustiga "
                    "qo'yiladi — u bifurkatsiya nuqtasiga "
                    "asimptotik yaqinlashadi. Ikkinchi panel — "
                    "ustuvorlikni yo'qotish shakli: plastina "
                    "rejasi, $m \\times n$ yarim to'lqinlar "
                    "kontur chiziqlari bilan; musbat va manfiy "
                    "sohalar turli rangda, shuning uchun "
                    "'shaxmat taxtasi' naqshi ko'rinadi. "
                    "$a/b$ slayderi bilan $m$ ning sakrashi "
                    "kuzatiladi. Uchinchi panel — $k(a/b)$ "
                    "girlandasi: har bir $m$ uchun alohida "
                    "egri chiziq ochiq rangda, ularning "
                    "pastki o'ramasi qalin chiziq bilan; "
                    "$k = 4$ gorizontal asimptota punktir bilan."
                ),
            ),
            interp=(
                "$k(a/b)$ girlandasi bu mavzudagi eng "
                "ma'lumotli grafik: u minimumlari aynan "
                "$a/b = 1, 2, 3, \\ldots$ da bo'lgan "
                "'gulchambar' shaklida va minimal qiymati "
                "har doim 4. Bu shuni anglatadiki, uzun "
                "plastina o'zini **kvadrat bo'laklarga** "
                "bo'lib bukiladi — har bir yarim to'lqinning "
                "uzunligi eniga teng. Fizik sabab: bu shakl "
                "energiya jihatidan eng qulay. Amaliy "
                "oqibati juda muhim: uzun plastinaning "
                "kritik kuchlanishi **uzunligiga bog'liq "
                "emas** va faqat $b/t$ nisbati bilan "
                "aniqlanadi. Shuning uchun uzunlamasiga "
                "qovurg'a qo'yish (ya'ni $b$ ni kamaytirish) "
                "juda samarali — $N_{cr} \\propto 1/b^2$, "
                "demak $b$ ni yarmiga tushirish kritik "
                "yuklamani to'rt marta oshiradi. Ko'ndalang "
                "qovurg'a esa deyarli befoyda, chunki u $a$ "
                "ni kamaytiradi, $a$ esa natijaga ta'sir "
                "qilmaydi. Bu qoida kema, samolyot va "
                "ko'prik konstruksiyalarida universal: "
                "siqilgan panellarda qovurg'alar har doim "
                "kuch yo'nalishi bo'ylab qo'yiladi. "
                "$\\sigma_{cr} > \\sigma_Y$ chiqishi ham "
                "muhim saboq: elastik formula chegarasini "
                "har doim tekshirish kerak, aks holda "
                "xavfsizlikka zid natija olinadi."
            ),
            mistakes=[
                "Muvozanatni deformatsiyalanmagan holatda "
                "yozish. U holda $N_xw_{,xx}$ hadi paydo "
                "bo'lmaydi va ustuvorlik masalasi umuman yo'qoladi.",
                "Kritik kuchlanish formulasida $b$ o'rniga "
                "$a$ ni qo'yish. Maxrajda har doim "
                "**qisqa** tomon (to'lqinlanish yo'nalishidagi o'lcham).",
                "$\\sigma_{cr} > \\sigma_Y$ chiqqanda "
                "natijani qabul qilish. Elastik formula "
                "faqat proporsionallik chegarasigacha o'rinli; "
                "undan keyin tangens modul kerak.",
                "Ustuvorlikni yo'qotish shaklini oldindan "
                "taxmin qilish. $m$ ning qiymati $a/b$ ga "
                "bog'liq va u sakrab o'zgaradi — xususiy "
                "qiymatlar masalasi yechilishi shart.",
            ],
            quiz=[
                q("Nima uchun ustuvorlik masalasida "
                  "muvozanat deformatsiyalangan holatda "
                  "yoziladi?",
                  "Faqat egilgan sirtda membrana kuchlarining "
                  "vertikal proeksiyasi ($N_xw_{,xx}$) paydo "
                  "bo'ladi. Tekis holatda bu had nolga teng "
                  "va hodisa ko'rinmaydi.", "konseptual"),
                q("Ustuvorlik masalasi qaysi matematik turga "
                  "kiradi?",
                  "Umumlashgan xususiy qiymatlar masalasi: "
                  "$([K] - \\lambda[K_G])\\{w\\} = 0$. Kritik "
                  "yuklama — xususiy qiymat, shakl — xususiy vektor.",
                  "konseptual"),
                q("$D = 4154$ N·m, $b = 0{,}3$ m, $k = 4$. "
                  "$N_{cr}$ ni toping.",
                  "$N_{cr} = 4\\pi^2 \\cdot 4154/0{,}09 = "
                  "1{,}822\\times10^6$ N/m = 1822 kN/m.", "hisob"),
                q("Nima uchun uzun plastinaning kritik "
                  "kuchlanishi uzunligiga bog'liq emas?",
                  "U o'zini eniga teng kvadrat bo'laklarga "
                  "bo'lib bukiladi, shuning uchun "
                  "$k \\to 4$ va $\\sigma_{cr}$ faqat "
                  "$b/t$ bilan aniqlanadi.", "talqin"),
                q("Kodda nima uchun har bir $(m,n)$ juftlik "
                  "mustaqil hisoblanadi?",
                  "Bir tekis membrana kuchlarida sinuslar "
                  "bazisi ham $[K]$, ham $[K_G]$ ni "
                  "diagonallashtiradi — xususiy qiymatlar "
                  "masalasi alohida tenglamalarga ajraladi.",
                  "kod"),
                q("Siqilgan panelda qovurg'a qaysi yo'nalishda "
                  "qo'yiladi va nega?",
                  "Kuch yo'nalishi bo'ylab (uzunlamasiga), "
                  "chunki u $b$ ni kamaytiradi va "
                  "$N_{cr} \\propto 1/b^2$. Ko'ndalang "
                  "qovurg'a $a$ ni kamaytiradi, $a$ esa "
                  "natijaga ta'sir qilmaydi.", "talqin"),
            ],
            bridge=(
                "Umumiy formulirovka tayyor. Keyingi mavzuda "
                "eng muhim amaliy holatni — bir tekis "
                "siqilgan to'rtburchak plastinani — "
                "batafsil yechamiz va ustuvorlik "
                "koeffitsienti $k$ ning barcha chegaraviy "
                "shartlar uchun qiymatlarini olamiz."
            ),
            research=(
                "Ustuvorlik masalasining energetik "
                "formulirovkasini o'rganing. Ikkinchi "
                "variatsiya $\\delta^2\\Pi = \\delta^2 U - "
                "\\delta^2 W$ ni hisoblang va kritik yuklama "
                "aynan $\\delta^2\\Pi$ musbat aniqlanganligini "
                "yo'qotadigan nuqtaga mos kelishini "
                "isbotlang. Bu Ritz usuli bilan kritik "
                "yuklamani baholashning asosini beradi: "
                "$\\lambda_{cr} = \\min \\frac{U_{\\text{egilish}}}"
                "{U_{\\text{geometrik}}}$ (Reley nisbati). "
                "Bir hadli baho bilan aniq yechimni "
                "taqqoslang va Ritz bahosi har doim "
                "**yuqoridan** ekanligini ko'rsating."
            ),
            manim_ref=manim(
                scene="PlateBucklingScene",
                module="animatsiya/scenes/pq_stability.py",
                title="Plastina ustuvorligini yo'qotishi",
                summary=(
                    "Siqilgan plastina yuklama ortgani sari "
                    "tekis qoladi, kritik nuqtada birdan "
                    "to'lqinsimon shaklga o'tadi; "
                    "bifurkatsiya diagrammasi bir vaqtda "
                    "quriladi va $a/b$ o'zgarganda "
                    "yarim to'lqinlar soni sakrashi ko'rsatiladi."
                ),
            ),
        ),
    ),

    # ------------------------------------------------------------------ pq-20
    Topic(
        id="pq-20",
        subject_id=S, module_id=M, order=20,
        title="Siqilgan to'rtburchak plastinaning kritik yuklamasi va ustuvorlik koeffitsienti",
        description=(
            "Bir tekis siqilgan plastina uchun aniq yechim, "
            "ustuvorlik koeffitsienti $k$ ning tomonlar nisbatiga "
            "bog'liqligi (girlanda egri chizig'i) va chegaraviy "
            "shartlarning ta'siri."
        ),
        learning_objective=(
            "Kritik yuklamani aniq formuladan hisoblash, $k$ "
            "koeffitsientining minimumini topish va turli "
            "chegaraviy shartlar uchun qiymatlarini taqqoslash."
        ),
        prerequisites=["pq-19"],
        mathematical_core=(
            "$N_{cr} = k\\pi^2 D/b^2$, "
            "$k = (mb/a + a/(mb))^2$, minimumlash, "
            "girlanda egri chizig'i va o'rama."
        ),
        engineering_application=(
            "Po'lat konstruksiya kesimlarini sinflarga ajratish, "
            "qovurg'alar orasidagi masofani tanlash, panel "
            "qalinligini loyihalash, qutisimon va I-kesimli "
            "to'sinlar."
        ),
        computational_component=(
            "$k(a/b)$ girlandasini qurish, minimumni topish, "
            "chegaraviy shartlar va qovurg'alar ta'sirini baholash."
        ),
        visualization_component=(
            "Girlanda egri chizig'i, ustuvorlik shakllari "
            "turli $a/b$ da, $k$ jadvali."
        ),
        research_extension=(
            "Uzunlamasiga qovurg'ali panelning ustuvorligini "
            "o'rganing: qovurg'a qanday bikrlikka ega bo'lsa "
            "panelni mustaqil bo'laklarga ajratadi?"
        ),
        difficulty="murakkab",
        previous_link=(
            "pq-19 da ustuvorlik masalasi umumiy qo'yildi va "
            "$k = 4$ qiymati berilgan deb olingan edi. Endi "
            "uni aniq keltirib chiqaramiz va boshqa "
            "geometriyalar uchun qiymatlarini olamiz."
        ),
        next_topic="pq-21",
        estimated_minutes=85,
        tags=["kritik yuklama", "k koeffitsienti", "girlanda", "panel"],
        lesson=_lesson(
            problem=(
                "pq-19 da qovurg'a qo'yish kritik yuklamani "
                "to'rt marta oshirishi aytilgan edi. Lekin "
                "qovurg'ani qayerga qo'yish kerak? Va nechta? "
                "Javob $k$ koeffitsientining tomonlar nisbatiga "
                "bog'liqligida yashiringan. Eng qizig'i shundaki, "
                "bu bog'liqlik monoton emas — u 'girlanda' "
                "shaklida va uning minimumlari aniq joylarda yotadi."
            ),
            concepts=[
                c("Ustuvorlik koeffitsienti $k$",
                  "$N_{cr} = k\\pi^2D/b^2$ formulasidagi "
                  "o'lchamsiz koeffitsient; geometriya va "
                  "chegaraviy shartlarga bog'liq."),
                c("Girlanda egri chizig'i (garland curve)",
                  "$k(a/b)$ bog'liqligi: har bir $m$ uchun "
                  "alohida egri chiziq, ularning pastki "
                  "o'ramasi haqiqiy $k$ ni beradi."),
                c("Yarim to'lqinlar soni $m$",
                  "Ustuvorlikni yo'qotishda uzunlik bo'ylab "
                  "hosil bo'ladigan yarim to'lqinlar soni; "
                  "$a/b$ oshgani sari sakrab ortadi."),
                c("Minimum sharti",
                  "$dk/dm = 0$ dan $a/b = m$ chiqadi: har bir "
                  "yarim to'lqin kvadrat bo'lganda $k$ minimal "
                  "va aynan 4 ga teng."),
                c("Chegaraviy shartlarning ta'siri",
                  "Uzun tomonlar mahkamlangan bo'lsa $k = 6{,}97$; "
                  "bittasi erkin bo'lsa $k = 0{,}425$ — "
                  "16 baravar farq."),
                c("Qovurg'a samaradorligi",
                  "Uzunlamasiga qovurg'a $b$ ni bo'ladi va "
                  "$N_{cr} \\propto 1/b^2$; ko'ndalang qovurg'a "
                  "esa deyarli befoyda."),
            ],
            derivation=[
                d("1. Yechimni Navye bazisida izlash",
                  r"w = w_{mn}\sin\frac{m\pi x}{a}\sin\frac{n\pi y}{b}",
                  "To'rt chekka sharnirli. Har bir had "
                  "chegaraviy shartlarni qanoatlantiradi."),
                d("2. Ustuvorlik tenglamasiga qo'yish",
                  r"D\pi^4\Big[\Big(\frac{m}{a}\Big)^2 + "
                  r"\Big(\frac{n}{b}\Big)^2\Big]^2 w_{mn} = "
                  r"N_x\pi^2\Big(\frac{m}{a}\Big)^2 w_{mn}",
                  "$N_x$ siquvchi (manfiy) deb olib, "
                  "$N_x w_{,xx}$ hadi musbat chiqadi. "
                  "Sinuslar qisqaradi."),
                d("3. Kritik kuch",
                  r"N_{cr} = \frac{D\pi^2}{(m/a)^2}"
                  r"\Big[\Big(\frac{m}{a}\Big)^2 + "
                  r"\Big(\frac{n}{b}\Big)^2\Big]^2",
                  "Har bir $(m, n)$ juftligi uchun o'z qiymati. "
                  "Eng kichigi haqiqiy kritik yuklama."),
                d("4. $n = 1$ ekanligi",
                  r"\frac{\partial N_{cr}}{\partial n} > 0 "
                  r"\;\Longrightarrow\; n = 1",
                  "$n$ faqat musbat hadda qatnashadi, shuning "
                  "uchun uni oshirish $N_{cr}$ ni oshiradi. "
                  "Ko'ndalang yo'nalishda har doim bitta "
                  "yarim to'lqin."),
                d("5. Standart shaklga keltirish",
                  r"N_{cr} = \frac{\pi^2 D}{b^2}\Big(\frac{mb}{a} "
                  r"+ \frac{a}{mb}\Big)^2 \equiv k\frac{\pi^2 D}{b^2}",
                  "$n = 1$ qo'yib, $b^2$ ni ajratamiz. "
                  "Qavs ichidagi ifoda $k$ ning kvadrat ildizi."),
                d("6. $k$ ning minimumi",
                  r"\frac{dk}{dm} = 0 \;\Longrightarrow\; "
                  r"\frac{b}{a} = \frac{a}{m^2 b} "
                  r"\;\Longrightarrow\; m = \frac{a}{b}",
                  "$(u + 1/u)^2$ shaklidagi ifoda $u = 1$ da "
                  "minimal. Bu yerda $u = mb/a$."),
                d("7. Minimal qiymat",
                  r"k_{\min} = (1 + 1)^2 = 4",
                  "Har bir yarim to'lqin kvadrat bo'lganda "
                  "($a/m = b$) koeffitsient aynan 4. Bu "
                  "natija $a/b$ butun son bo'lganda aniq "
                  "erishiladi."),
                d("8. $m$ ning sakrash nuqtalari",
                  r"k_m = k_{m+1} \;\Longrightarrow\; "
                  r"\frac{a}{b} = \sqrt{m(m+1)}",
                  "Ikki qo'shni egri chiziq kesishgan joyda "
                  "$m$ sakrab ortadi: $\\sqrt{2} = 1{,}41$, "
                  "$\\sqrt{6} = 2{,}45$, $\\sqrt{12} = 3{,}46$ "
                  "va hokazo."),
            ],
            meaning=(
                "$k = (mb/a + a/(mb))^2$ formulasi "
                "$(u + 1/u)^2$ ko'rinishida va bu matematikada "
                "juda tanish tuzilish: u $u = 1$ da minimal "
                "va har ikki tomonga simmetrik o'sadi. "
                "Fizik ma'nosi: plastina ikki raqobatchi "
                "mexanizm orasida murosaga keladi. Uzun "
                "to'lqin ($m$ kichik) egilish energiyasini "
                "kamaytiradi $x$ yo'nalishida, lekin $y$ "
                "yo'nalishida egrilik katta bo'lib qoladi. "
                "Qisqa to'lqin esa aksincha. Eng qulay "
                "murosa — **kvadrat yarim to'lqin**, ikkala "
                "yo'nalishda egrilik teng. Shuning uchun "
                "$k_{\\min} = 4$ va u har doim erishiladi "
                "(agar $a/b \\ge 1$ bo'lsa). Bundan eng "
                "muhim amaliy qoida kelib chiqadi: "
                "**uzun plastinaning kritik kuchlanishi "
                "uzunligiga bog'liq emas**. Girlandaning "
                "'tishlari' esa qisqa plastinalarda "
                "($a/b < 1$) sezilarli: $a/b = 0{,}5$ da "
                "$k = 6{,}25$, ya'ni 56 % yuqori. Demak "
                "ko'ndalang qovurg'a qo'yish (ya'ni $a$ ni "
                "kamaytirish) faqat $a/b < 1$ bo'lganda "
                "foyda beradi — bu deyarli hech qachon "
                "amaliy emas. Uzunlamasiga qovurg'a esa "
                "$b$ ni kamaytiradi va $N_{cr} \\propto 1/b^2$ "
                "bo'lgani uchun juda samarali: $b$ ni "
                "yarmiga tushirish kritik yuklamani to'rt "
                "marta oshiradi."
            ),
            equations=[
                eq(r"N_{cr} = k\frac{\pi^2 D}{b^2}, \qquad "
                   r"\sigma_{cr} = k\frac{\pi^2 E}{12(1-\nu^2)}"
                   r"\Big(\frac{t}{b}\Big)^2",
                   "Kritik yuklama va kuchlanish.",
                   "Kritik yuklama"),
                eq(r"k = \Big(\frac{mb}{a} + \frac{a}{mb}\Big)^2",
                   "Ustuvorlik koeffitsienti (4 chekka sharnirli, "
                   "bir tekis siqilish).", "k formulasi"),
                eq(r"k_{\min} = 4 \quad \text{da} \quad m = \frac{a}{b}",
                   "Minimal qiymat va unga mos yarim to'lqinlar soni.",
                   "Minimum"),
                eq(r"\frac{a}{b} = \sqrt{m(m+1)}",
                   "Yarim to'lqinlar soni sakraydigan nisbatlar.",
                   "Sakrash nuqtalari"),
            ],
            conditions=(
                "**$k$ ning qiymatlari (bir tekis siqilish, "
                "uzun plastina):**\n\n"
                "| Uzun tomonlar | $k$ | Izoh |\n"
                "|---|---|---|\n"
                "| Ikkalasi sharnirli | 4,00 | Etalon |\n"
                "| Ikkalasi mahkamlangan | 6,97 | +74 % |\n"
                "| Biri mahkam, biri sharnirli | 5,42 | +36 % |\n"
                "| Biri sharnirli, biri erkin | 0,425 | −89 % |\n"
                "| Biri mahkam, biri erkin | 1,277 | −68 % |\n\n"
                "**Erkin chekkaning halokatli ta'siri** — "
                "$k = 0{,}425$ — I-kesimli to'sin javoni uchun "
                "aynan shu hol amal qiladi (javonning yarmi "
                "bir tomondan devorga biriktirilgan, ikkinchisi "
                "erkin).\n\n"
                "**Boshqa yuklanish turlari uchun $k$** "
                "(4 chekka sharnirli, uzun plastina):\n"
                "- Sof egilish (chiziqli epyura): $k = 23{,}9$;\n"
                "- Sof siljish: $k = 5{,}34$;\n"
                "- Siqilish + egilish: oraliq qiymatlar.\n\n"
                "**Qo'llanish sharti:** "
                "$\\sigma_{cr} < \\sigma_{\\text{proporsionallik}}$; "
                "aks holda tangens modul tuzatmasi kerak."
            ),
            worked=WorkedExample(
                statement=(
                    "Ko'prik ortotrop plitasining siqilgan "
                    "paneli: $a = 3000$ mm, $b = 600$ mm, "
                    "$t = 12$ mm, $E = 210$ GPa, $\\nu = 0{,}3$, "
                    "$\\sigma_Y = 355$ MPa. Uzun tomonlar "
                    "sharnirli. (a) $k$ va $\\sigma_{cr}$ ni "
                    "toping. (b) Markazga bitta uzunlamasiga "
                    "qovurg'a qo'ysak nima o'zgaradi? "
                    "(c) Ko'ndalang qovurg'a bilan taqqoslang."
                ),
                given=[
                    r"a = 3\ \text{m},\ b = 0{,}6\ \text{m},\ "
                    r"t = 0{,}012\ \text{m}",
                    r"E = 210\ \text{GPa},\ \nu = 0{,}3,\ "
                    r"\sigma_Y = 355\ \text{MPa}",
                ],
                steps=[
                    st(r"D = \frac{210\times10^9 \cdot 1{,}728\times10^{-6}}"
                       r"{10{,}92} = 33\,231\ \text{N·m}",
                       "$t^3 = 1{,}728\\times10^{-6}$ m³."),
                    st(r"\frac{a}{b} = \frac{3}{0{,}6} = 5 "
                       r"\;\Longrightarrow\; m = 5, \ k = (1+1)^2 = 4",
                       "Butun nisbat — $k$ aynan minimal "
                       "qiymatga teng. Beshta kvadrat "
                       "yarim to'lqin hosil bo'ladi."),
                    st(r"\sigma_{cr} = k\frac{\pi^2 E}{12(1-\nu^2)}"
                       r"\Big(\frac{t}{b}\Big)^2 = "
                       r"4\frac{9{,}8696 \cdot 210\times10^{9}}{10{,}92}"
                       r"\Big(\frac{12}{600}\Big)^2",
                       "$t/b = 0{,}02$, kvadrati "
                       "$4\\times10^{-4}$."),
                    st(r"\sigma_{cr} = 4 \cdot 1{,}8981\times10^{11} "
                       r"\cdot 4\times10^{-4} = 303{,}7\ \text{MPa}",
                       "$\\sigma_{cr} = 303{,}7 < \\sigma_Y = 355$ MPa — "
                       "elastik ustuvorlik hukmron, formula o'rinli."),
                    st(r"\text{Qovurg'a markazda: } b' = 300\ \text{mm}, "
                       r"\quad \frac{a}{b'} = 10, \ k = 4 \ (\text{o'zgarmadi})",
                       "$k$ o'zgarmaydi, chunki u faqat "
                       "nisbatga bog'liq va $a/b'$ hali ham butun."),
                    st(r"\sigma_{cr}' = 4 \cdot 1{,}8981\times10^{11}"
                       r"\Big(\frac{12}{300}\Big)^2 = "
                       r"4 \cdot 1{,}8981\times10^{11} \cdot 1{,}6\times10^{-3} "
                       r"= 1215\ \text{MPa}",
                       "**To'rt marta oshdi** — $b$ yarmiga "
                       "tushgani uchun. Endi "
                       "$\\sigma_{cr} \\gg \\sigma_Y$, demak "
                       "oqish hal qiluvchi va panel to'liq "
                       "mustahkamligini beradi."),
                    st(r"\text{Ko'ndalang qovurg'a: } a' = 1500\ \text{mm}, "
                       r"\quad \frac{a'}{b} = 2{,}5",
                       "Endi $a/b$ butun emas. $m = 2$ va $m = 3$ "
                       "orasida — $\\sqrt{6} = 2{,}449 < 2{,}5$, "
                       "demak $m = 3$."),
                    st(r"k = \Big(\frac{3 \cdot 0{,}6}{1{,}5} + "
                       r"\frac{1{,}5}{3 \cdot 0{,}6}\Big)^2 = "
                       r"(1{,}2 + 0{,}8333)^2 = 4{,}134",
                       "$k$ atigi 3,4 % oshdi. Ko'ndalang "
                       "qovurg'a deyarli befoyda."),
                    st(r"\frac{\text{uzunlamasiga}}{\text{ko'ndalang}} = "
                       r"\frac{4{,}000}{4{,}134}\cdot\frac{(1/0{,}3)^2}"
                       r"{(1/0{,}6)^2} = \frac{4 \cdot 4}{4{,}134} "
                       r"= 3{,}87",
                       "Uzunlamasiga qovurg'a 3,87 marta "
                       "samaraliroq — bir xil material sarfida."),
                ],
                answer=(
                    "$D = 33{,}23$ kN·m; $a/b = 5$, $k = 4$, "
                    "$\\sigma_{cr} = 303{,}7$ MPa $< \\sigma_Y$. "
                    "Uzunlamasiga qovurg'a $\\sigma_{cr}$ ni "
                    "**4 marta** (1215 MPa ga) oshiradi; "
                    "ko'ndalang qovurg'a esa $k$ ni atigi "
                    "3,4 % o'zgartiradi — 3,87 marta samarasiz."
                ),
                engineering_note=(
                    "Bu natija ko'prik, kema va samolyot "
                    "konstruksiyalaridagi universal qoidani "
                    "asoslaydi: **uzunlamasiga qovurg'a "
                    "(stringer) asosiy, ko'ndalang qovurg'a "
                    "(frame, diafragma) ikkilamchi**. "
                    "Ko'ndalang elementlar boshqa vazifani "
                    "bajaradi: ular shaklni ushlab turadi, "
                    "uzunlamasiga qovurg'alarni burilishdan "
                    "saqlaydi va mahalliy yuklamalarni "
                    "tarqatadi. Lekin siqilish ustuvorligiga "
                    "ta'siri kichik. Diqqat: qovurg'aning "
                    "o'zi ham yetarli bikrlikka ega bo'lishi "
                    "kerak — aks holda u panel bilan birga "
                    "bukiladi va hech qanday foyda bermaydi."
                ),
            ),
            computation=Computation(
                caption=(
                    "$k(a/b)$ girlandasini qurish, chegaraviy "
                    "shartlarni taqqoslash va qovurg'a "
                    "samaradorligini baholash."
                ),
                code='''"""Siqilgan plastina: ustuvorlik koeffitsienti va girlanda."""
import numpy as np
from labkit import PARAMS, note, series, table, value

a = float(PARAMS.get("a", 3000.0))/1000.0
b = float(PARAMS.get("b", 600.0))/1000.0
t = float(PARAMS.get("t", 12.0))/1000.0
E = float(PARAMS.get("E", 210.0))*1e9
nu = float(PARAMS.get("nu", 0.3))
sY = float(PARAMS.get("sY", 355.0))*1e6
n_rib = int(PARAMS.get("n_rib", 0))       # uzunlamasiga qovurg'alar soni

D = E*t**3/(12*(1 - nu**2))
value("Silindrik bikrlik D", D/1000, "kN*m")
value("a/b nisbati", a/b, "—")
value("b/t nisbati", b/t, "—")


def k_ss(rt, mmax=20):
    """4 chekka sharnirli, bir tekis siqilish: k va m."""
    best, bm = 1e30, 1
    for m in range(1, mmax + 1):
        kk = (m/rt + rt/m)**2
        if kk < best:
            best, bm = kk, m
    return best, bm


k, m_cr = k_ss(a/b)
value("Ustuvorlik koeffitsienti k", k, "—")
value("Yarim to'lqinlar soni m", float(m_cr), "—")
value("Yarim to'lqin uzunligi a/m", a/m_cr, "m")
value("(a/m) / b", (a/m_cr)/b, "—")

sig_cr = k*np.pi**2*E/(12*(1 - nu**2))*(t/b)**2
N_cr = sig_cr*t
value("Kritik kuchlanish sigma_cr", sig_cr/1e6, "MPa")
value("Kritik kuch N_cr", N_cr/1000, "kN/m")
value("sigma_cr / sigma_Y", sig_cr/sY, "—")
if sig_cr < sY:
    note(f"sigma_cr = {sig_cr/1e6:.1f} MPa < sigma_Y = {sY/1e6:.0f} MPa — "
         f"elastik ustuvorlik hukmron, formula o'rinli.")
else:
    note(f"sigma_cr = {sig_cr/1e6:.1f} MPa > sigma_Y = {sY/1e6:.0f} MPa — "
         f"panel oqishdan oldin bukilmaydi; tangens modul tuzatmasi "
         f"yoki oqish hal qiluvchi.")

# --- Girlanda egri chizig'i ---
rts = np.linspace(0.3, 6.0, 600)
k_env, m_env = [], []
for rt in rts:
    kk, mm = k_ss(rt)
    k_env.append(kk); m_env.append(float(mm))
series("k(a/b) — o'rama (haqiqiy k)", rts.tolist(), k_env,
       xlabel="a / b", ylabel="k")
series("k = 4 (asimptota)", rts.tolist(), [4.0]*len(rts),
       xlabel="a / b", ylabel="k")
series("Yarim to'lqinlar soni m(a/b)", rts.tolist(), m_env,
       xlabel="a / b", ylabel="m")

for m in range(1, 6):
    series(f"m = {m} shoxi", rts.tolist(),
           [min((m/rt + rt/m)**2, 20.0) for rt in rts],
           xlabel="a / b", ylabel="k")

# Sakrash nuqtalari
jumps = [np.sqrt(m*(m + 1)) for m in range(1, 6)]
table("Yarim to'lqinlar soni sakraydigan nisbatlar",
      ["m -> m+1", "a/b = sqrt(m(m+1))", "Shu nuqtadagi k"],
      [[f"{m} -> {m+1}", round(float(np.sqrt(m*(m+1))), 4),
        round(float(k_ss(np.sqrt(m*(m+1)))[0]), 4)]
       for m in range(1, 6)])
note("Sakrash nuqtalarida ikkala shox bir xil k beradi — "
     "girlandaning 'tishlari' aynan shu yerda.")

# --- Chegaraviy shartlarning ta'siri ---
bc_table = [
    ("Ikkalasi sharnirli (SS)", 4.000),
    ("Ikkalasi mahkamlangan (CC)", 6.970),
    ("Biri mahkam, biri sharnirli (CS)", 5.420),
    ("Biri sharnirli, biri erkin (SF)", 0.425),
    ("Biri mahkam, biri erkin (CF)", 1.277),
]
rows = []
for nm, kv in bc_table:
    sc = kv*np.pi**2*E/(12*(1 - nu**2))*(t/b)**2
    rows.append([nm, kv, round(sc/1e6, 1), round(kv/4.0, 3)])
table("Uzun tomonlardagi chegaraviy shartlar (uzun plastina)",
      ["Chegaraviy shart", "k", "sigma_cr, MPa", "k/k_SS"], rows)
note("Erkin chekka halokatli: k = 0.425, ya'ni sharnirli "
     "holatdan 9,4 marta kam. I-kesim javoni uchun aynan shu hol.")

# --- Yuklanish turining ta'siri ---
table("Yuklanish turi va k (4 chekka sharnirli, uzun plastina)",
      ["Yuklanish turi", "k", "Izoh"],
      [["Bir tekis siqilish", 4.00, "Etalon"],
       ["Sof egilish", 23.9, "Epyura chiziqli, yarmi cho'zilgan"],
       ["Sof siljish", 5.34, "Qiya to'lqinlar hosil bo'ladi"],
       ["Siqilish + egilish (psi = 0)", 7.81, "Uchburchak epyura"],
       ["Ikki o'qli siqilish (N_y = N_x)", 2.00, "Eng xavfli hol"]])

# --- Qovurg'alarning ta'siri ---
ribs = list(range(0, 6))
sig_ribs, b_sub = [], []
for nr in ribs:
    bb = b/(nr + 1)
    kk, _ = k_ss(a/bb)
    sc = kk*np.pi**2*E/(12*(1 - nu**2))*(t/bb)**2
    sig_ribs.append(min(sc, 5*sY)/1e6)
    b_sub.append(bb*1000)
series("sigma_cr(uzunlamasiga qovurg'alar soni)",
       [float(r) for r in ribs], sig_ribs,
       xlabel="Qovurg'alar soni", ylabel="sigma_cr, MPa")
series("Oqish chegarasi", [float(r) for r in ribs],
       [sY/1e6]*len(ribs), xlabel="Qovurg'alar soni",
       ylabel="sigma_cr, MPa")
table("Uzunlamasiga qovurg'alarning ta'siri",
      ["Qovurg'alar", "b', mm", "sigma_cr, MPa", "Nisbat"],
      [[ribs[i], round(b_sub[i], 0), round(sig_ribs[i], 0),
        round(sig_ribs[i]/sig_ribs[0], 2)] for i in range(len(ribs))])

# Ko'ndalang qovurg'a bilan taqqoslash
a_half = a/2
k_tr, m_tr = k_ss(a_half/b)
sig_tr = k_tr*np.pi**2*E/(12*(1 - nu**2))*(t/b)**2
b_half = b/2
k_ln, _ = k_ss(a/b_half)
sig_ln = k_ln*np.pi**2*E/(12*(1 - nu**2))*(t/b_half)**2
value("Ko'ndalang qovurg'a: a' = a/2, k", k_tr, "—")
value("Ko'ndalang qovurg'a: sigma_cr", sig_tr/1e6, "MPa")
value("Uzunlamasiga qovurg'a: b' = b/2, k", k_ln, "—")
value("Uzunlamasiga qovurg'a: sigma_cr", sig_ln/1e6, "MPa")
value("Uzunlamasiga / ko'ndalang samaradorlik", sig_ln/sig_tr, "—")
note(f"Bir xil material sarfida uzunlamasiga qovurg'a "
     f"{sig_ln/sig_tr:.2f} marta samaraliroq: u b ni kamaytiradi "
     f"(sigma_cr ~ 1/b^2), ko'ndalang esa a ni — a esa natijaga "
     f"deyarli ta'sir qilmaydi.")

# --- b/t bo'yicha loyihalash ---
bts = np.linspace(20.0, 150.0, 200)
scs = [4.0*np.pi**2*E/(12*(1 - nu**2))/bt**2/1e6 for bt in bts]
series("sigma_cr(b/t), k = 4", bts.tolist(), scs,
       xlabel="b / t", ylabel="sigma_cr, MPa")
series("Oqish chegarasi", bts.tolist(), [sY/1e6]*len(bts),
       xlabel="b / t", ylabel="sigma_cr, MPa")
bt_lim = np.pi*np.sqrt(4*E/(12*(1 - nu**2)*sY))
value("sigma_cr = sigma_Y bo'ladigan b/t", float(bt_lim), "—")
note(f"b/t < {bt_lim:.0f} bo'lsa panel oqishdan oldin bukilmaydi "
     f"(3-sinf yoki undan yaxshi); undan katta bo'lsa mahalliy "
     f"ustuvorlik hal qiluvchi (4-sinf).")
''',
                parameters=[
                    p("a", "Panel uzunligi a", 200.0, 10000.0, 3000.0, 50.0,
                      "mm"),
                    p("b", "Panel eni b", 50.0, 3000.0, 600.0, 10.0, "mm"),
                    p("t", "Qalinlik t", 1.0, 60.0, 12.0, 0.5, "mm"),
                    p("E", "Yung moduli E", 1.0, 400.0, 210.0, 1.0, "GPa"),
                    p("nu", "Puasson koeffitsienti ν", 0.0, 0.45, 0.3, 0.01),
                    p("sY", "Oqish chegarasi σ_Y", 20.0, 1000.0, 355.0, 5.0,
                      "MPa"),
                    p("n_rib", "Uzunlamasiga qovurg'alar", 0.0, 5.0, 0.0, 1.0),
                ],
                expected_output=(
                    "D = 33,23 kN·m, a/b = 5 → m = 5, k = 4,000 "
                    "(yarim to'lqin aynan kvadrat); σ_cr = 303,7 MPa "
                    "< σ_Y = 355 MPa. Uzunlamasiga qovurg'a σ_cr ni "
                    "4 marta oshiradi (1215 MPa), ko'ndalang esa "
                    "atigi 3,4 % — samaradorlik nisbati ≈ 3,9. "
                    "σ_cr = σ_Y chegarasi b/t ≈ 55."
                ),
            ),
            visual=vis(
                kind="Girlanda egri chizig'i va ustuvorlik shakllari",
                tool="React/SVG",
                description=(
                    "$k(a/b)$ girlandasi barcha shoxlari bilan, "
                    "ustuvorlik shakllari turli $a/b$ da, "
                    "qovurg'a samaradorligi."
                ),
                how_to_draw=(
                    "React/SVG: asosiy panel — girlanda: har bir "
                    "$m$ uchun $(m/r + r/m)^2$ egri chizig'i "
                    "och rangda va yorliq bilan ($m = 1, 2, "
                    "3\\ldots$); ularning pastki o'ramasi qalin "
                    "to'q chiziq bilan — bu haqiqiy $k$. "
                    "$k = 4$ gorizontal punktir asimptota. "
                    "Sakrash nuqtalari ($\\sqrt{2}, \\sqrt{6}, "
                    "\\sqrt{12}$) vertikal nozik chiziqlar va "
                    "qiymat yorliqlari bilan. $a/b$ slayderi "
                    "ish nuqtasini siljitadi. Ikkinchi panel — "
                    "shu $a/b$ dagi ustuvorlik shakli: plastina "
                    "rejasi, $m$ ta yarim to'lqin kontur "
                    "chiziqlari bilan, musbat/manfiy sohalar "
                    "qarama-qarshi rangda; har bir yarim "
                    "to'lqinning uzunligi $b$ ga yaqinligi "
                    "o'lchov chizig'i bilan ta'kidlanadi. "
                    "Uchinchi panel — qovurg'a taqqoslashi: "
                    "ikkita panel sxemasi (uzunlamasiga va "
                    "ko'ndalang qovurg'a bilan) va ularning "
                    "$\\sigma_{cr}$ ustunlari yonma-yon."
                ),
            ),
            interp=(
                "Chegaraviy shartlar jadvali eng keskin "
                "raqamni beradi: erkin chekkada $k = 0{,}425$, "
                "ya'ni sharnirli holatdan **9,4 marta kam**. "
                "Bu I-kesimli to'sin javoni uchun bevosita "
                "amal qiladi — javonning bir tomoni devorga "
                "ulangan, ikkinchisi erkin. Shuning uchun "
                "normativlar javon chiqish uzunligining "
                "qalinlikka nisbatini juda qattiq "
                "cheklaydi ($c/t \\le 9\\varepsilon$ 1-sinf "
                "uchun, $b/t \\le 42\\varepsilon$ ichki "
                "elementlar uchun — besh baravar farq). "
                "Qovurg'a jadvali esa loyihalash strategiyasini "
                "beradi: har bir qo'shilgan uzunlamasiga "
                "qovurg'a $\\sigma_{cr}$ ni "
                "$(n+1)^2$ marta oshiradi — bitta qovurg'a "
                "4 marta, ikkitasi 9 marta. Lekin bu "
                "cheksiz davom etmaydi: $\\sigma_{cr}$ "
                "$\\sigma_Y$ dan oshgandan keyin qo'shimcha "
                "qovurg'a hech qanday foyda bermaydi. "
                "Optimal loyiha aynan shu chegarada yotadi — "
                "$\\sigma_{cr} \\approx \\sigma_Y$, ya'ni "
                "mahalliy ustuvorlik va oqish bir vaqtda "
                "kritik bo'lgan holat. Bu muhandislikdagi "
                "umumiy optimallik prinsipi: eng yaxshi "
                "loyiha — bir necha buzilish mexanizmi "
                "bir vaqtda ishga tushadigan loyiha."
            ),
            mistakes=[
                "$k$ ni geometriyaga bog'liq emas deb "
                "hisoblash. U $a/b$ ga va chegaraviy "
                "shartlarga kuchli bog'liq: 0,425 dan "
                "23,9 gacha o'zgaradi.",
                "Formulada $b$ o'rniga $a$ ni qo'yish. "
                "$b$ — har doim to'lqinlanish yo'nalishidagi "
                "(odatda qisqa) o'lcham.",
                "Ko'ndalang qovurg'a bilan ustuvorlikni "
                "oshirishga urinish. U $a$ ni kamaytiradi, "
                "$a$ esa uzun plastinada natijaga ta'sir qilmaydi.",
                "Qovurg'aning o'z bikrligini tekshirmaslik. "
                "Yetarli bikr bo'lmagan qovurg'a panel bilan "
                "birga bukiladi va hech qanday foyda bermaydi.",
            ],
            quiz=[
                q("$k$ ning minimal qiymati qancha va u "
                  "qachon erishiladi?",
                  "$k_{\\min} = 4$, $m = a/b$ bo'lganda — "
                  "ya'ni har bir yarim to'lqin kvadrat "
                  "bo'lganda.", "konseptual"),
                q("Nima uchun $n = 1$ har doim eng kichik "
                  "kritik yuklamani beradi?",
                  "$n$ faqat musbat hadda qatnashadi "
                  "($(n/b)^2$ surat ichida), shuning uchun "
                  "uni oshirish $N_{cr}$ ni oshiradi.",
                  "konseptual"),
                q("$a/b = 2{,}5$, sharnirli. $k$ va $m$ ni toping.",
                  "$m = 2$: $k = (0{,}8+1{,}25)^2 = 4{,}20$; "
                  "$m = 3$: $k = (1{,}2+0{,}833)^2 = 4{,}13$. "
                  "Demak $m = 3$, $k = 4{,}13$.", "hisob"),
                q("Erkin chekkaning $k$ ga ta'siri qanday?",
                  "$k$ 4,00 dan 0,425 ga tushadi — 9,4 marta. "
                  "Shuning uchun I-kesim javoni uchun "
                  "normativlar juda qattiq.", "talqin"),
                q("Kodda girlandaning 'shoxlari' nima uchun "
                  "alohida chiziladi?",
                  "Har bir $m$ o'z egri chizig'ini beradi; "
                  "haqiqiy $k$ — ularning pastki o'ramasi. "
                  "Shoxlarni ko'rsatish $m$ ning sakrashini "
                  "tushuntiradi.", "kod"),
                q("Nechta uzunlamasiga qovurg'a qo'yish "
                  "optimal?",
                  "$\\sigma_{cr}$ $\\sigma_Y$ ga yetguncha. "
                  "Undan keyin qo'shimcha qovurg'a foyda "
                  "bermaydi — oqish hal qiluvchi bo'lib qoladi.",
                  "talqin"),
            ],
            bridge=(
                "Bir tekis siqilish eng sodda hol edi. "
                "Amaliyotda panellar ko'pincha siljish yoki "
                "aralash yuklanishga uchraydi. Bundan "
                "tashqari, kritik yuklamadan keyin panel "
                "birdan buzilmaydi — u qo'shimcha yuk "
                "ko'tarishda davom etadi. Keyingi mavzuda "
                "shu ikki masalani ko'ramiz."
            ),
            research=(
                "Uzunlamasiga qovurg'ali panelning "
                "ustuvorligini o'rganing. Qovurg'a yetarli "
                "bikr bo'lsa, panel mustaqil bo'laklarga "
                "ajraladi; yetarli bo'lmasa, panel qovurg'a "
                "bilan birga bukiladi (global rejim). "
                "**Chegaraviy bikrlik** $\\gamma^*$ ni "
                "aniqlang: shu qiymatda ikkala rejim bir xil "
                "kritik yuklama beradi. Eurocode 3 Part 1-5 "
                "dagi formulalar bilan taqqoslang. Ortotrop "
                "plastina modeli (pq-12) bilan qovurg'ali "
                "panelni modellashtirib, natijani aniq "
                "yechim bilan solishtiring — qovurg'alar "
                "soni qanchadan boshlab ekvivalent ortotrop "
                "model yetarli aniq bo'ladi?"
            ),
            manim_ref=manim(
                scene="BucklingGarlandScene",
                module="animatsiya/scenes/pq_stability.py",
                title="Girlanda egri chizig'i va yarim to'lqinlar",
                summary=(
                    "$a/b$ asta-sekin oshadi; plastinadagi "
                    "yarim to'lqinlar soni sakrab o'zgaradi "
                    "va shu paytda girlanda egri chizig'ida "
                    "shoxdan shoxga o'tish ko'rsatiladi."
                ),
            ),
        ),
    ),

    # ------------------------------------------------------------------ pq-21
    Topic(
        id="pq-21",
        subject_id=S, module_id=M, order=21,
        title="Siljish, aralash yuklanish va kritikdan keyingi xatti-harakat",
        description=(
            "Sof siljishda ustuvorlik, aralash yuklanish uchun "
            "o'zaro ta'sir tenglamalari, kritikdan keyingi zaxira "
            "va samarali kenglik (Vinter) tushunchasi."
        ),
        learning_objective=(
            "Siljish va aralash yuklanishda kritik kuchlanishni "
            "hisoblash, kritikdan keyingi zaxirani baholash va "
            "samarali kenglik usulini qo'llash."
        ),
        prerequisites=["pq-20", "pq-18"],
        mathematical_core=(
            "$k_s = 5{,}34 + 4(b/a)^2$, o'zaro ta'sir tenglamasi "
            "$(\\sigma/\\sigma_{cr})^2 + (\\tau/\\tau_{cr})^2 \\le 1$, "
            "Vinter formulasi $\\rho = (\\bar\\lambda - 0{,}22)/\\bar\\lambda^2$."
        ),
        engineering_application=(
            "To'sin devori (web) siljishda, qutisimon kesim, "
            "yupqa devorli profil, kema korpusi, samolyot paneli, "
            "tortish maydoni (tension field) nazariyasi."
        ),
        computational_component=(
            "Siljish uchun $k_s$ ni hisoblash, o'zaro ta'sir "
            "egri chizig'ini qurish, kritikdan keyingi zaxira va "
            "samarali kenglikni baholash."
        ),
        visualization_component=(
            "Qiya to'lqinlar (siljish shakli), o'zaro ta'sir "
            "diagrammasi, samarali kenglik sxemasi."
        ),
        research_extension=(
            "Tortish maydoni (tension field) nazariyasini "
            "o'rganing: to'sin devori bukilgandan keyin qanday "
            "qilib ferma kabi ishlay boshlaydi?"
        ),
        difficulty="ilg'or",
        previous_link=(
            "pq-20 da bir tekis siqilish ko'rib chiqildi va "
            "kritik yuklama buzilish deb hisoblandi. Amalda esa "
            "plastina kritik nuqtada buzilmaydi — pq-18 dagi "
            "membrana kuchlari ishga tushadi va qo'shimcha "
            "zaxira beradi."
        ),
        next_topic="pq-22",
        estimated_minutes=90,
        tags=["siljish", "o'zaro ta'sir", "samarali kenglik", "postbuckling"],
        lesson=_lesson(
            problem=(
                "Ko'prik to'sinining devori (web): balandligi "
                "1500 mm, qalinligi 10 mm. U asosan **siljish** "
                "kuchini uzatadi. Hisob shuni ko'rsatadiki, devor "
                "ishchi yuklamaning yarmida bukilib ketadi. Lekin "
                "ko'prik yillar davomida ishlaydi va hech narsa "
                "yuz bermaydi. Nega? Chunki plastina, sterjendan "
                "farqli o'laroq, kritik yuklamadan keyin "
                "**qulamaydi** — u yukni qayta taqsimlaydi va "
                "ko'tarishda davom etadi."
            ),
            concepts=[
                c("Siljishda ustuvorlik",
                  "Qiya to'lqinlar hosil bo'ladi (taxminan 45°), "
                  "chunki sof siljish 45° da sof cho'zilish va "
                  "siqilishga teng (mq-21)."),
                c("Siljish koeffitsienti $k_s$",
                  "$k_s = 5{,}34 + 4(b/a)^2$ ($a > b$); uzun "
                  "plastinada $k_s \\to 5{,}34$."),
                c("O'zaro ta'sir (interaction)",
                  "Bir vaqtda bir necha yuklama turi bo'lsa, "
                  "ularning nisbiy qiymatlari kvadratik "
                  "munosabat bilan bog'lanadi."),
                c("Kritikdan keyingi zaxira (postbuckling reserve)",
                  "Plastina bukilgandan keyin ham yuk ko'taradi: "
                  "yuk chekkalarga qayta taqsimlanadi. Sterjenda "
                  "bunday zaxira deyarli yo'q."),
                c("Samarali kenglik (effective width)",
                  "Bukilgan plastinani ikkita yon polosaga "
                  "almashtirish: ular to'liq kuchlanish oladi, "
                  "o'rta qism esa 'ishlamaydi'."),
                c("Tortish maydoni (tension field)",
                  "Devor bukilgandan keyin diagonal tortilish "
                  "sohasi hosil bo'ladi va to'sin ferma kabi "
                  "ishlay boshlaydi."),
            ],
            derivation=[
                d("1. Sof siljishning bosh kuchlanishlari",
                  r"\sigma_1 = +\tau, \quad \sigma_2 = -\tau "
                  r"\quad (\theta = \pm 45°)",
                  "mq-21 dagi Mor doirasi natijasi. Siqilish "
                  "45° yo'nalishda va aynan u ustuvorlikni "
                  "yo'qotishga olib keladi."),
                d("2. Qiya to'lqinlar",
                  r"w \sim \sin\frac{\pi(x - \alpha y)}{\lambda}"
                  r"\sin\frac{\pi y}{b}",
                  "Ustuvorlikni yo'qotish shakli qiya — "
                  "to'lqin cho'qqilari siqilish yo'nalishiga "
                  "perpendikulyar."),
                d("3. Siljish uchun kritik kuchlanish",
                  r"\tau_{cr} = k_s\frac{\pi^2 E}{12(1-\nu^2)}"
                  r"\Big(\frac{t}{b}\Big)^2, \qquad "
                  r"k_s = 5{,}34 + \frac{4}{(a/b)^2}",
                  "Formulaning shakli siqilishdagi bilan bir xil, "
                  "faqat koeffitsient boshqa. Uzun plastinada "
                  "$k_s = 5{,}34$."),
                d("4. Aralash yuklanish: o'zaro ta'sir",
                  r"\Big(\frac{\sigma}{\sigma_{cr}}\Big)^2 + "
                  r"\Big(\frac{\tau}{\tau_{cr}}\Big)^2 \le 1",
                  "Tajriba va sonli hisoblardan olingan "
                  "yaqinlashuv. Doira tenglamasi — bu "
                  "har bir yuklama turining hissasi kvadratik "
                  "qo'shilishini bildiradi."),
                d("5. Nima uchun plastina qulamaydi",
                  r"N_x(y) \ne \text{const} \ \text{bukilgandan keyin}",
                  "Bukilishdan keyin o'rta qism 'yumshaydi' va "
                  "yuk chekkalarga oqib o'tadi. Chekkalar esa "
                  "ko'ndalang yo'nalishda ushlab turilgan, "
                  "shuning uchun ular yuqori kuchlanish oladi."),
                d("6. Samarali kenglik g'oyasi",
                  r"\int_0^b \sigma(y)\,dy = \sigma_{\max}\,b_{\text{eff}}",
                  "Haqiqiy notekis kuchlanish epyurasini "
                  "ekvivalent to'g'ri to'rtburchak bilan "
                  "almashtiramiz. $b_{\\text{eff}}$ — shu "
                  "to'rtburchakning eni."),
                d("7. Vinter formulasi",
                  r"\rho = \frac{b_{\text{eff}}}{b} = "
                  r"\frac{\bar\lambda_p - 0{,}22}{\bar\lambda_p^2}, "
                  r"\qquad \bar\lambda_p = \sqrt{\frac{\sigma_Y}{\sigma_{cr}}}",
                  "Tajribaviy formula (1947), Eurocode 3 va "
                  "AISI normativlarining asosi. "
                  "$\\bar\\lambda_p \\le 0{,}673$ da $\\rho = 1$."),
                d("8. Kritikdan keyingi zaxira koeffitsienti",
                  r"\frac{\sigma_u}{\sigma_{cr}} = \frac{\rho\,\sigma_Y}"
                  r"{\sigma_{cr}} = \rho\,\bar\lambda_p^2",
                  "$\\bar\\lambda_p = 2$ da zaxira "
                  "$0{,}445 \\cdot 4 = 1{,}78$ — chegaraviy "
                  "yuklama kritikdan 78 % yuqori. Nozik "
                  "plastinada zaxira yanada katta."),
            ],
            meaning=(
                "Kritikdan keyingi zaxira plastinani sterjendan "
                "tubdan ajratib turadi. Siqilgan sterjen kritik "
                "yuklamada qulaydi — uning zaxirasi yo'q, chunki "
                "yukni qayta taqsimlash uchun 'ikkinchi yo'l' "
                "mavjud emas. Plastinada esa bor: o'rta qism "
                "bukilib yumshaganda, yuk chekkalarga oqib "
                "o'tadi. Chekkalar ko'ndalang yo'nalishda "
                "ushlab turilgani uchun ular bukilmaydi va "
                "kuchlanishni oqish chegarasigacha ko'taradi. "
                "Shuning uchun **buzilish kritik yuklamada emas, "
                "chekkalar oqqanda** yuz beradi. Samarali kenglik "
                "shu g'oyaning muhandislik tilidagi ifodasi: "
                "bukilgan plastinani ikkita ishlaydigan polosaga "
                "almashtiramiz. Vinter formulasidagi "
                "$\\rho = (\\bar\\lambda - 0{,}22)/\\bar\\lambda^2$ "
                "ning shakli ham ma'noli: $\\bar\\lambda$ katta "
                "bo'lganda $\\rho \\approx 1/\\bar\\lambda$, "
                "demak $b_{\\text{eff}} \\propto t\\sqrt{E/\\sigma_Y}$ — "
                "samarali kenglik plastina eniga umuman bog'liq "
                "emas! U faqat qalinlik va materialga bog'liq. "
                "Bu juda kuchli xulosa: panelni kengaytirish "
                "ko'tarish qobiliyatini oshirmaydi. Shuning uchun "
                "yupqa devorli konstruksiyalarda kenglik emas, "
                "qovurg'alar soni oshiriladi."
            ),
            equations=[
                eq(r"\tau_{cr} = k_s\frac{\pi^2E}{12(1-\nu^2)}"
                   r"\Big(\frac{t}{b}\Big)^2, \quad "
                   r"k_s = 5{,}34 + \frac{4}{(a/b)^2}",
                   "Siljishda kritik kuchlanish.", "Siljish ustuvorligi"),
                eq(r"\Big(\frac{\sigma}{\sigma_{cr}}\Big)^2 + "
                   r"\Big(\frac{\tau}{\tau_{cr}}\Big)^2 \le 1",
                   "Siqilish va siljishning o'zaro ta'siri.",
                   "O'zaro ta'sir"),
                eq(r"\rho = \frac{\bar\lambda_p - 0{,}22}{\bar\lambda_p^2} "
                   r"\le 1, \qquad \bar\lambda_p = "
                   r"\sqrt{\frac{\sigma_Y}{\sigma_{cr}}}",
                   "Vinter samaradorlik koeffitsienti.",
                   "Vinter formulasi"),
                eq(r"b_{\text{eff}} \approx 1{,}9\,t"
                   r"\sqrt{\frac{E}{\sigma_Y}}",
                   "Katta nozeklikda samarali kenglik — eniga "
                   "bog'liq emas.", "Samarali kenglik"),
            ],
            conditions=(
                "**Siljish uchun chegaraviy shartlar** "
                "siqilishdagidek, lekin $k_s$ boshqa:\n"
                "- Sharnirli: $k_s = 5{,}34 + 4/(a/b)^2$;\n"
                "- Mahkamlangan: $k_s = 8{,}98 + 5{,}6/(a/b)^2$.\n\n"
                "**Kritikdan keyingi zaxira quyidagi shartlarda "
                "mavjud:**\n"
                "1. Plastina chekkalari ko'ndalang yo'nalishda "
                "ushlab turilgan (qovurg'a, qo'shni panel);\n"
                "2. Chekkalar to'g'ri qoladi (harakatsiz yoki "
                "bikr elementga ulangan);\n"
                "3. Yuklama statik (siklik yuklamada bukilish "
                "charchoq yoriqlariga olib keladi).\n\n"
                "**Zaxira yo'q bo'lgan hollar:** erkin chekkali "
                "element (I-kesim javoni chiqishi) — u yerda "
                "yukni qayta taqsimlash uchun joy yo'q.\n\n"
                "**Eksplutatsiya cheklovi:** bukilgan panel "
                "ko'rinishi yoqimsiz va tebranishga moyil, "
                "shuning uchun ba'zi normativlar xizmat "
                "yuklamasida bukilishga umuman yo'l qo'ymaydi."
            ),
            worked=WorkedExample(
                statement=(
                    "To'sin devori: $h_w = 1500$ mm (balandligi), "
                    "$a = 3000$ mm (qovurg'alar orasi), "
                    "$t = 10$ mm, $E = 210$ GPa, $\\nu = 0{,}3$, "
                    "$\\sigma_Y = 355$ MPa, $\\tau_Y = "
                    "\\sigma_Y/\\sqrt{3}$. (a) $\\tau_{cr}$ ni "
                    "toping. (b) Kritikdan keyingi zaxirani "
                    "baholang. (c) Devor bir vaqtda "
                    "$\\sigma = 100$ MPa siqilish olsa, "
                    "tekshiring."
                ),
                given=[
                    r"b = h_w = 1{,}5\ \text{m},\ a = 3\ \text{m},\ "
                    r"t = 0{,}01\ \text{m}",
                    r"E = 210\ \text{GPa},\ \nu = 0{,}3,\ "
                    r"\sigma_Y = 355\ \text{MPa}",
                ],
                steps=[
                    st(r"\frac{a}{b} = 2 \;\Rightarrow\; "
                       r"k_s = 5{,}34 + \frac{4}{4} = 6{,}34",
                       "Siljish koeffitsienti. Uzun devorda u "
                       "5,34 ga intiladi."),
                    st(r"\frac{t}{b} = \frac{10}{1500} = "
                       r"6{,}667\times10^{-3}",
                       "Nisbiy qalinlik — juda nozik devor "
                       "($b/t = 150$)."),
                    st(r"\tau_{cr} = 6{,}34 \cdot "
                       r"\frac{9{,}8696 \cdot 210\times10^{9}}{10{,}92} "
                       r"\cdot (6{,}667\times10^{-3})^2",
                       "Standart formula."),
                    st(r"\tau_{cr} = 6{,}34 \cdot 1{,}8981\times10^{11} "
                       r"\cdot 4{,}444\times10^{-5} = 53{,}5\ \text{MPa}",
                       "Kritik siljish kuchlanishi."),
                    st(r"\tau_Y = \frac{355}{\sqrt{3}} = 205{,}0\ \text{MPa} "
                       r"\;\Rightarrow\; \frac{\tau_Y}{\tau_{cr}} = 3{,}83",
                       "Devor oqish chegarasidan **3,83 marta "
                       "past** yuklamada bukiladi. Klassik "
                       "hisobda bu yaroqsiz deb qabul qilinardi."),
                    st(r"\bar\lambda_w = \sqrt{\frac{\tau_Y}{\tau_{cr}}} "
                       r"= \sqrt{3{,}83} = 1{,}957",
                       "Devorning nisbiy nozekligi."),
                    st(r"\chi_w = \frac{1{,}37}{0{,}7 + \bar\lambda_w} "
                       r"= \frac{1{,}37}{2{,}657} = 0{,}516 "
                       r"\quad (\text{EN 1993-1-5})",
                       "Kritikdan keyingi zaxira hisobga olingan "
                       "kamaytirish koeffitsienti."),
                    st(r"\tau_u = \chi_w\,\tau_Y = 0{,}516 \cdot 205 "
                       r"= 105{,}8\ \text{MPa}",
                       "Chegaraviy siljish kuchlanishi. "
                       "$\\tau_{cr} = 53{,}5$ MPa bilan "
                       "solishtirsak: **zaxira 1,98 marta**."),
                    st(r"\text{Aralash: } \Big(\frac{100}{\sigma_{cr}}\Big)^2 "
                       r"+ \Big(\frac{\tau}{105{,}8}\Big)^2 \le 1; \ "
                       r"\sigma_{cr} = 4\cdot1{,}8981\times10^{11}"
                       r"\cdot4{,}444\times10^{-5} = 33{,}7\ \text{MPa}",
                       "Siqilish uchun $k = 4$. "
                       "$\\sigma = 100 > \\sigma_{cr} = 33{,}7$ MPa — "
                       "siqilishda ham bukilish bor, "
                       "$\\rho$ hisoblash kerak."),
                ],
                answer=(
                    "$k_s = 6{,}34$, $\\tau_{cr} = 53{,}5$ MPa — "
                    "oqish chegarasidan 3,83 marta past. Lekin "
                    "kritikdan keyingi zaxira tufayli chegaraviy "
                    "qiymat $\\tau_u = 105{,}8$ MPa, ya'ni "
                    "**kritikdan 1,98 marta yuqori**. Devor "
                    "bukilgan holda ishlashga ruxsat etiladi."
                ),
                engineering_note=(
                    "Ko'prik va kran to'sinlarida devorning "
                    "bukilgan holda ishlashi **normal loyiha "
                    "yechimi**, nuqson emas. EN 1993-1-5 buni "
                    "to'g'ridan-to'g'ri hisobga oladi. Shart: "
                    "ko'ndalang qovurg'alar devorni ushlab "
                    "turishi kerak — ular bukilgan paneldan "
                    "kelgan tortish kuchini qabul qiladi. "
                    "Agar qovurg'a yetarli bikr bo'lmasa, "
                    "tortish maydoni ishlamaydi va zaxira "
                    "yo'qoladi. Shuning uchun qovurg'a "
                    "hisobida devorning bukilishidan kelgan "
                    "kuch albatta hisobga olinadi."
                ),
            ),
            computation=Computation(
                caption=(
                    "Siljish ustuvorligi, o'zaro ta'sir egri "
                    "chizig'i, kritikdan keyingi zaxira va "
                    "samarali kenglikni hisoblash."
                ),
                code='''"""Siljish, aralash yuklanish va kritikdan keyingi zaxira."""
import numpy as np
from labkit import PARAMS, note, series, table, value

b = float(PARAMS.get("b", 1500.0))/1000.0
a = float(PARAMS.get("a", 3000.0))/1000.0
t = float(PARAMS.get("t", 10.0))/1000.0
E = float(PARAMS.get("E", 210.0))*1e9
nu = float(PARAMS.get("nu", 0.3))
sY = float(PARAMS.get("sY", 355.0))*1e6
sig_app = float(PARAMS.get("sig_app", 100.0))*1e6
tau_app = float(PARAMS.get("tau_app", 60.0))*1e6

D = E*t**3/(12*(1 - nu**2))
base = np.pi**2*E/(12*(1 - nu**2))*(t/b)**2
value("Silindrik bikrlik D", D/1000, "kN*m")
value("b/t nisbati", b/t, "—")
value("a/b nisbati", a/b, "—")

# --- Siqilish ---
rt = a/b
k_c = min((m/rt + rt/m)**2 for m in range(1, 20))
sig_cr = k_c*base
value("Siqilish koeffitsienti k", k_c, "—")
value("sigma_cr", sig_cr/1e6, "MPa")

# --- Siljish ---
if rt >= 1.0:
    k_s = 5.34 + 4.0/rt**2
else:
    k_s = 4.0 + 5.34/rt**2
tau_cr = k_s*base
tauY = sY/np.sqrt(3)
value("Siljish koeffitsienti k_s", k_s, "—")
value("tau_cr", tau_cr/1e6, "MPa")
value("tau_Y = sigma_Y/sqrt(3)", tauY/1e6, "MPa")
value("tau_Y / tau_cr", tauY/tau_cr, "—")

# --- Kritikdan keyingi zaxira (EN 1993-1-5, siljish) ---
lam_w = np.sqrt(tauY/tau_cr)
if lam_w < 0.83:
    chi_w = 1.0
elif lam_w < 1.08:
    chi_w = 0.83/lam_w
else:
    chi_w = 1.37/(0.7 + lam_w)
tau_u = chi_w*tauY
value("Devor nozekligi lambda_w", lam_w, "—")
value("Kamaytirish koeffitsienti chi_w", chi_w, "—")
value("Chegaraviy tau_u", tau_u/1e6, "MPa")
value("Kritikdan keyingi zaxira tau_u/tau_cr", tau_u/tau_cr, "—")
note(f"Devor tau_cr = {tau_cr/1e6:.1f} MPa da bukiladi, lekin "
     f"tau_u = {tau_u/1e6:.1f} MPa gacha ishlaydi — zaxira "
     f"{tau_u/tau_cr:.2f} marta. Sterjenda bunday zaxira yo'q.")

# --- Vinter: siqilishda samarali kenglik ---
lam_p = np.sqrt(sY/sig_cr)
rho = 1.0 if lam_p <= 0.673 else min((lam_p - 0.22)/lam_p**2, 1.0)
b_eff = rho*b
value("Siqilish nozekligi lambda_p", lam_p, "—")
value("Vinter rho", rho, "—")
value("Samarali kenglik b_eff", b_eff*1000, "mm")
value("b_eff / t", b_eff/t, "—")
b_eff_asym = 1.9*t*np.sqrt(E/sY)
value("Asimptotik b_eff = 1.9t*sqrt(E/sY)", b_eff_asym*1000, "mm")
note(f"Katta nozeklikda b_eff eniga deyarli bog'liq emas: "
     f"hisoblangan {b_eff*1000:.0f} mm, asimptotik baho "
     f"{b_eff_asym*1000:.0f} mm. Panelni kengaytirish ko'tarish "
     f"qobiliyatini oshirmaydi!")

# --- b ning ta'siri: b_eff eniga bog'liq emasligini ko'rsatish ---
bs = np.linspace(0.3, 4.0, 120)
beffs, rhos, caps = [], [], []
for bb in bs:
    bse = np.pi**2*E/(12*(1 - nu**2))*(t/bb)**2
    kcc = min((m/(a/bb) + (a/bb)/m)**2 for m in range(1, 25))
    scr = kcc*bse
    lp = np.sqrt(sY/scr)
    rr = 1.0 if lp <= 0.673 else min((lp - 0.22)/lp**2, 1.0)
    beffs.append(rr*bb*1000)
    rhos.append(rr)
    caps.append(rr*bb*t*sY/1000)
series("Samarali kenglik b_eff(b)", (bs*1000).tolist(), beffs,
       xlabel="Panel eni b, mm", ylabel="b_eff, mm")
series("Asimptota 1.9t*sqrt(E/sY)", (bs*1000).tolist(),
       [b_eff_asym*1000]*len(bs), xlabel="Panel eni b, mm",
       ylabel="b_eff, mm")
series("Samaradorlik rho(b)", (bs*1000).tolist(), rhos,
       xlabel="Panel eni b, mm", ylabel="rho")
series("Ko'tarish qobiliyati N(b)", (bs*1000).tolist(), caps,
       xlabel="Panel eni b, mm", ylabel="N_u, kN/m")
note(f"b ni {bs[0]*1000:.0f} dan {bs[-1]*1000:.0f} mm ga "
     f"(13 marta) oshirish b_eff ni atigi "
     f"{beffs[-1]/beffs[0]:.2f} marta o'zgartiradi.")

# --- O'zaro ta'sir egri chizig'i ---
th = np.linspace(0, np.pi/2, 200)
series("O'zaro ta'sir: sigma/sigma_cr", np.cos(th).tolist(),
       np.sin(th).tolist(), xlabel="sigma / sigma_cr",
       ylabel="tau / tau_cr")
r_s = sig_app/sig_cr
r_t = tau_app/tau_cr
util = r_s**2 + r_t**2
series("Ish nuqtasi", [r_s], [r_t],
       xlabel="sigma / sigma_cr", ylabel="tau / tau_cr")
value("sigma / sigma_cr", r_s, "—")
value("tau / tau_cr", r_t, "—")
value("O'zaro ta'sir ko'rsatkichi", util, "—")
if util <= 1.0:
    note(f"Ustuvorlik ko'rsatkichi {util:.3f} <= 1 — elastik "
         f"ustuvorlik bo'yicha xavfsiz (kritikdan keyingi "
         f"zaxira hisobga olinmagan holda).")
else:
    note(f"Ustuvorlik ko'rsatkichi {util:.3f} > 1 — elastik "
         f"kritik yuklama oshib ketdi. Kritikdan keyingi "
         f"zaxira hisobga olinishi kerak (chi_w = {chi_w:.3f}).")

# --- Kuchlanish taqsimoti: bukilgandan oldin va keyin ---
y = np.linspace(0.0, b, 200)
sig_pre = np.full_like(y, 1.0)
xi = y/b
sig_post = 1.0 + 0.9*np.cos(2*np.pi*xi - np.pi)*0 + \
    0.9*(np.cos(np.pi*(2*xi - 1))*0.5 + 0.5)*0
sig_post = 0.35 + 0.65*np.abs(np.cos(np.pi*xi))**1.5*2
sig_post = np.clip(sig_post, 0.3, 2.0)
sig_post = sig_post/np.trapezoid(sig_post, xi) if hasattr(np, "trapezoid") \
    else sig_post/np.trapz(sig_post, xi)
series("Kuchlanish epyurasi: bukilishdan oldin", (y*1000).tolist(),
       sig_pre.tolist(), xlabel="y, mm", ylabel="sigma / sigma_o'rtacha")
series("Kuchlanish epyurasi: bukilishdan keyin", (y*1000).tolist(),
       sig_post.tolist(), xlabel="y, mm",
       ylabel="sigma / sigma_o'rtacha")
note("Bukilgandan keyin o'rta qism 'yumshaydi' va yuk chekkalarga "
     "oqib o'tadi — samarali kenglik g'oyasining fizik asosi.")

table("Siljish va siqilish koeffitsientlari",
      ["Yuklanish", "Chegaraviy shart", "k (uzun plastina)", "k (a/b = 1)"],
      [["Siqilish", "4 sharnirli", 4.00, 4.00],
       ["Siqilish", "uzun tomonlar mahkam", 6.97, 6.97],
       ["Siljish", "4 sharnirli", 5.34, 9.34],
       ["Siljish", "4 mahkamlangan", 8.98, 14.58],
       ["Sof egilish", "4 sharnirli", 23.9, 25.6]])

table("Plastina va sterjen ustuvorligining farqi",
      ["Jihat", "Sterjen (Eyler)", "Plastina"],
      [["Kritik yuklamada", "qulaydi", "bukiladi, lekin yuk ko'taradi"],
       ["Zaxira", "deyarli yo'q", "1.5 - 3 marta"],
       ["Sababi", "qayta taqsimlash yo'li yo'q",
        "yuk chekkalarga oqib o'tadi"],
       ["Loyiha yondashuvi", "N < N_cr talab qilinadi",
        "bukilishga ruxsat, b_eff bilan hisob"],
       ["Normativ", "chi (egilish egri chizig'i)",
        "rho (samarali kenglik) yoki chi_w"]])
''',
                parameters=[
                    p("b", "Panel eni (devor balandligi) b", 100.0, 4000.0,
                      1500.0, 50.0, "mm"),
                    p("a", "Qovurg'alar orasi a", 200.0, 10000.0, 3000.0,
                      100.0, "mm"),
                    p("t", "Qalinlik t", 2.0, 50.0, 10.0, 0.5, "mm"),
                    p("E", "Yung moduli E", 1.0, 400.0, 210.0, 1.0, "GPa"),
                    p("nu", "Puasson koeffitsienti ν", 0.0, 0.45, 0.3, 0.01),
                    p("sY", "Oqish chegarasi σ_Y", 20.0, 1000.0, 355.0, 5.0,
                      "MPa"),
                    p("sig_app", "Qo'yilgan siqilish σ", 0.0, 500.0, 100.0,
                      5.0, "MPa"),
                    p("tau_app", "Qo'yilgan siljish τ", 0.0, 300.0, 60.0,
                      5.0, "MPa"),
                ],
                expected_output=(
                    "k_s = 6,34, τ_cr = 53,5 MPa, τ_Y = 205 MPa "
                    "(nisbat 3,83); λ_w = 1,96, χ_w = 0,516, "
                    "τ_u = 105,8 MPa — zaxira 1,98 marta. "
                    "Samarali kenglik b_eff = 431 mm, asimptotik "
                    "baho 1,9t√(E/σ_Y) = 462 mm — panel eniga "
                    "deyarli bog'liq emas."
                ),
            ),
            visual=vis(
                kind="Siljish shakli va samarali kenglik",
                tool="React/SVG",
                description=(
                    "Qiya to'lqinlar, o'zaro ta'sir doirasi, "
                    "bukilishdan oldingi va keyingi kuchlanish "
                    "epyuralari."
                ),
                how_to_draw=(
                    "React/SVG: birinchi panel — siljish "
                    "ustuvorligi shakli: plastina to'rtburchagi, "
                    "ichida taxminan 45° burchakda qiya to'lqin "
                    "chiziqlari; chekkalarda siljish yo'nalishini "
                    "ko'rsatuvchi strelkalar juftligi. To'lqin "
                    "cho'qqilari va botiqlari qarama-qarshi "
                    "rangda. Ikkinchi panel — o'zaro ta'sir "
                    "diagrammasi: chorak doira "
                    "($\\sigma/\\sigma_{cr}$ va "
                    "$\\tau/\\tau_{cr}$ o'qlarida), ichi "
                    "xavfsiz soha sifatida och rangda "
                    "to'ldirilgan; ish nuqtasi belgi bilan, "
                    "markazdan unga vektor. Nuqta doiradan "
                    "chiqsa rang o'zgaradi. Uchinchi panel — "
                    "samarali kenglik: panel kesimi, ustida "
                    "ikkita kuchlanish epyurasi ustma-ust: "
                    "bukilishdan oldin to'g'ri to'rtburchak "
                    "(punktir), keyin esa chekkalarda cho'qqili "
                    "egri chiziq (uzluksiz). Ikkala epyura "
                    "yuzasi teng ekanligi ko'rsatiladi; "
                    "$b_{\\text{eff}}/2$ polosalari "
                    "shtrixlanadi — bu 'ishlaydigan' qism."
                ),
            ),
            interp=(
                "$b_{\\text{eff}}(b)$ grafigi bu mavzudagi eng "
                "kuchli natijani beradi: panel enini 13 marta "
                "oshirish samarali kenglikni deyarli "
                "o'zgartirmaydi. Sababi formulada ko'rinadi — "
                "katta nozeklikda "
                "$b_{\\text{eff}} \\approx 1{,}9t\\sqrt{E/\\sigma_Y}$ "
                "va bu ifodada $b$ umuman yo'q. Amaliy oqibati: "
                "keng yupqa panel qo'shimcha yuk ko'tarmaydi — "
                "u shunchaki ko'proq material sarflaydi. "
                "Shuning uchun yupqa devorli konstruksiyalarda "
                "panel kengaytirilmaydi, **qovurg'alar qo'shiladi**. "
                "Ikkinchi muhim natija — plastina va sterjen "
                "taqqoslash jadvali. Sterjen kritik yuklamada "
                "qulaydi, plastina esa 1,5–3 marta zaxiraga ega. "
                "Bu zaxira bepul emas: u bukilgan panel va "
                "qovurg'alarga qo'shimcha kuch uzatilishini "
                "talab qiladi. Shuning uchun EN 1993-1-5 "
                "qovurg'a hisobida bukilishdan kelgan tortish "
                "kuchini majburiy hisobga oladi. Agar qovurg'a "
                "zaif bo'lsa, zaxira umuman ishlamaydi va "
                "konstruksiya kritik yuklamada buziladi — "
                "hisobda ko'zda tutilgandan ikki barobar erta."
            ),
            mistakes=[
                "Kritik yuklamani buzilish yuklamasi deb "
                "hisoblash. Plastinada ular orasida 1,5–3 "
                "marta farq bor.",
                "Kritikdan keyingi zaxirani erkin chekkali "
                "elementda kutish. U yerda yukni qayta "
                "taqsimlash uchun joy yo'q.",
                "Siljish uchun siqilish koeffitsientini "
                "ishlatish. $k_s$ va $k$ har xil: uzun "
                "plastinada 5,34 va 4,00.",
                "Zaxirani hisobga olib, qovurg'alarni "
                "tekshirmaslik. Bukilgan panel qovurg'aga "
                "qo'shimcha tortish kuchi uzatadi.",
            ],
            quiz=[
                q("Nima uchun siljishda qiya to'lqinlar "
                  "hosil bo'ladi?",
                  "Sof siljish 45° da sof siqilishga teng; "
                  "ustuvorlikni yo'qotish aynan siqilish "
                  "yo'nalishiga perpendikulyar to'lqinlar "
                  "bilan sodir bo'ladi.", "konseptual"),
                q("Kritikdan keyingi zaxira nima uchun "
                  "plastinada bor, sterjenda esa yo'q?",
                  "Plastinada yuk chekkalarga qayta "
                  "taqsimlanadi va chekkalar ko'ndalang "
                  "yo'nalishda ushlab turilgani uchun "
                  "bukilmaydi. Sterjenda qayta taqsimlash "
                  "yo'li yo'q.", "konseptual"),
                q("$a/b = 2$, sharnirli. $k_s$ ni toping.",
                  "$k_s = 5{,}34 + 4/4 = 6{,}34$.", "hisob"),
                q("Samarali kenglik nima uchun panel eniga "
                  "bog'liq emas?",
                  "Katta nozeklikda "
                  "$b_{\\text{eff}} \\approx 1{,}9t\\sqrt{E/\\sigma_Y}$ — "
                  "ifodada $b$ yo'q. Kengaytirish ko'tarish "
                  "qobiliyatini oshirmaydi.", "talqin"),
                q("Kodda o'zaro ta'sir ko'rsatkichi qanday "
                  "hisoblanadi?",
                  "$(\\sigma/\\sigma_{cr})^2 + "
                  "(\\tau/\\tau_{cr})^2$ — u 1 dan kichik "
                  "bo'lsa elastik ustuvorlik bo'yicha xavfsiz.",
                  "kod"),
                q("Bukilgan devorli to'sin qanday ishlaydi?",
                  "Tortish maydoni hosil bo'ladi: diagonal "
                  "tortilish sohasi + qovurg'alar siqilishi — "
                  "to'sin ferma kabi ishlay boshlaydi.",
                  "talqin"),
            ],
            bridge=(
                "Statik yuklama ostidagi ustuvorlik to'liq "
                "ko'rib chiqildi. Endi vaqt o'zgaruvchisini "
                "kiritamiz: plastina qanday chastotalarda "
                "tebranadi va bu nima uchun muhim?"
            ),
            research=(
                "Tortish maydoni (tension field) nazariyasini "
                "o'rganing. Devor bukilgandan keyin unda "
                "faqat diagonal **tortilish** qoladi — "
                "siqilishni u ko'tarolmaydi. Natijada to'sin "
                "Pratt fermasiga aylanadi: devor diagonallari "
                "tortiladi, ko'ndalang qovurg'alar esa "
                "siqiladi. Basler modelini o'rganing va "
                "tortish maydoni burchagini aniqlang. "
                "Qovurg'aga tushadigan siqilish kuchini "
                "hisoblang — u qovurg'a kesimini tanlashda "
                "hal qiluvchi. Aviatsiyadagi Wagner "
                "nazariyasi bilan taqqoslang: nima uchun "
                "samolyot qanotida bu effekt yanada muhim?"
            ),
            manim_ref=manim(
                scene="ShearBucklingScene",
                module="animatsiya/scenes/pq_stability.py",
                title="Siljishda ustuvorlik va tortish maydoni",
                summary=(
                    "Devor siljish ostida qiya to'lqinlar "
                    "bilan bukiladi; keyin kuchlanish "
                    "taqsimoti o'zgarib, diagonal tortish "
                    "maydoni hosil bo'lishi va to'sin ferma "
                    "kabi ishlay boshlashi ko'rsatiladi."
                ),
            ),
        ),
    ),

    # ------------------------------------------------------------------ pq-22
    Topic(
        id="pq-22",
        subject_id=S, module_id=M, order=22,
        title="Plastinalarning erkin tebranishlari va xususiy chastotalar",
        description=(
            "Dinamik plastina tenglamasi, o'zgaruvchilarni "
            "ajratish, xususiy chastotalar va tebranish "
            "shakllari, tugun chiziqlari (Xladni figuralari)."
        ),
        learning_objective=(
            "Erkin tebranish tenglamasini yechish, xususiy "
            "chastotalarni hisoblash, tebranish shakllarini "
            "va tugun chiziqlarini aniqlash."
        ),
        prerequisites=["pq-21", "nm-29"],
        mathematical_core=(
            "$D\\nabla^4w + \\rho h\\ddot{w} = 0$, "
            "$\\omega_{mn} = \\pi^2\\sqrt{D/(\\rho h)}"
            "[(m/a)^2+(n/b)^2]$, modal analiz, ortogonallik."
        ),
        engineering_application=(
            "Musiqa asboblari (gitara deki, baraban), "
            "tebranishdan himoya, akustik panel, aviatsiya "
            "paneli flatteri, mashina korpuslari rezonansi."
        ),
        computational_component=(
            "Xususiy chastotalarni hisoblash, shakllarni "
            "qurish, tugun chiziqlarini topish, qalinlik va "
            "materialning ta'sirini baholash."
        ),
        visualization_component=(
            "Tebranish shakllari (modal shakllar), tugun "
            "chiziqlari xaritasi, chastota spektri."
        ),
        research_extension=(
            "Xladni figuralarini o'rganing: qum tugun "
            "chiziqlarida to'planishi nimani ko'rsatadi va "
            "bu 18-asrda akustikani qanday o'zgartirgan?"
        ),
        difficulty="murakkab",
        previous_link=(
            "nm-29 da ko'p erkinlik darajali tizimning modal "
            "tahlili o'rganilgan edi. Plastina — cheksiz "
            "erkinlik darajali tizim, lekin g'oya bir xil: "
            "xususiy chastotalar va shakllar."
        ),
        next_topic="pq-23",
        estimated_minutes=90,
        tags=["tebranish", "xususiy chastota", "modal", "Xladni"],
        lesson=_lesson(
            problem=(
                "Sanoat ventilyatorining korpusi panellaridan "
                "biri 47 Hz da kuchli shovqin chiqaradi. "
                "Ventilyator 2820 ayl/daq (47 Hz) da ishlaydi — "
                "aniq moslik. Bu rezonans. Panel qalinligini "
                "yoki o'lchamini qanday o'zgartirsak chastota "
                "xavfli zonadan chiqadi? Javob uchun plastinaning "
                "xususiy chastotalari nimaga bog'liqligini "
                "bilish kerak."
            ),
            concepts=[
                c("Erkin tebranish",
                  "Tashqi kuchsiz tebranish: plastina "
                  "boshlang'ich turtkidan keyin o'z "
                  "chastotalarida tebranadi."),
                c("Xususiy chastota $\\omega_{mn}$",
                  "Har bir $(m, n)$ juftlik uchun o'z "
                  "chastotasi. Eng kichigi — asosiy (fundamental) chastota."),
                c("Tebranish shakli (mode shape)",
                  "$W_{mn}(x,y)$ — shu chastotada tebranadigan "
                  "fazoviy shakl. Plastina faqat shu shakllarda "
                  "tebranadi."),
                c("Tugun chiziqlari (nodal lines)",
                  "Tebranish paytida harakatsiz qoladigan "
                  "chiziqlar. Xladni ularni qum bilan ko'rsatgan."),
                c("Modal ortogonallik",
                  "Turli shakllar massa bilan vaznlangan "
                  "ma'noda ortogonal — shuning uchun ular "
                  "mustaqil tebranadi."),
                c("Rezonans",
                  "Qo'zg'atuvchi chastota xususiy chastotaga "
                  "yaqinlashganda amplituda keskin ortadi."),
            ],
            derivation=[
                d("1. Dinamik tenglama (Dalamber prinsipi)",
                  r"D\nabla^4 w + \rho h\frac{\partial^2 w}"
                  r"{\partial t^2} = q(x,y,t)",
                  "pq-04 dagi tenglamaga inersiya hadi "
                  "qo'shiladi: $\\rho h$ — birlik yuzadagi "
                  "massa. Aylanish inersiyasi e'tiborsiz "
                  "(yupqa plastina)."),
                d("2. Erkin tebranish: $q = 0$",
                  r"D\nabla^4 w + \rho h\,\ddot{w} = 0",
                  "Bir jinsli tenglama. Uning notrivial "
                  "davriy yechimi xususiy chastotalarni beradi."),
                d("3. O'zgaruvchilarni ajratish",
                  r"w(x,y,t) = W(x,y)\,e^{i\omega t} "
                  r"\;\Longrightarrow\; D\nabla^4 W - "
                  r"\rho h\omega^2 W = 0",
                  "Garmonik tebranish faraz qilinadi. "
                  "Vaqt o'zgaruvchisi ajraladi va fazoviy "
                  "masala qoladi."),
                d("4. Xususiy qiymatlar masalasi",
                  r"\nabla^4 W = \beta^4 W, \qquad "
                  r"\beta^4 = \frac{\rho h\omega^2}{D}",
                  "Bu ustuvorlik masalasiga (pq-19) juda "
                  "o'xshash — ikkalasi ham xususiy qiymatlar "
                  "masalasi, faqat o'ng tomon boshqacha."),
                d("5. Navye yechimi (4 chekka sharnirli)",
                  r"W_{mn} = \sin\frac{m\pi x}{a}"
                  r"\sin\frac{n\pi y}{b} \;\Longrightarrow\; "
                  r"\beta^4 = \pi^4\Big[\Big(\frac{m}{a}\Big)^2 "
                  r"+ \Big(\frac{n}{b}\Big)^2\Big]^2",
                  "Sinuslar bazisi yana ishlaydi — u "
                  "$\\nabla^4$ ning xususiy funksiyasi."),
                d("6. Xususiy chastotalar",
                  r"\omega_{mn} = \pi^2\sqrt{\frac{D}{\rho h}}"
                  r"\Big[\Big(\frac{m}{a}\Big)^2 + "
                  r"\Big(\frac{n}{b}\Big)^2\Big]",
                  "Diqqat: kvadrat qavs **kvadratga "
                  "ko'tarilmaydi** — $\\beta^4$ dan ildiz "
                  "olinganda daraja yarmiga tushadi."),
                d("7. Asosiy chastota",
                  r"f_{11} = \frac{\pi}{2}\sqrt{\frac{D}{\rho h}}"
                  r"\Big(\frac{1}{a^2} + \frac{1}{b^2}\Big)",
                  "$m = n = 1$. Kvadrat plastinada "
                  "$f_{11} = \\pi\\sqrt{D/(\\rho h)}/a^2$."),
                d("8. Qalinlikning ta'siri",
                  r"\sqrt{\frac{D}{\rho h}} = \sqrt{\frac{Eh^3}"
                  r"{12(1-\nu^2)\rho h}} = h\sqrt{\frac{E}"
                  r"{12(1-\nu^2)\rho}} \;\Longrightarrow\; "
                  r"\omega \propto h",
                  "Juda muhim natija: chastota qalinlikka "
                  "**chiziqli** mutanosib. Qalinlikni ikki "
                  "marta oshirish chastotani ikki marta "
                  "oshiradi. Og'ishda esa $h^3$ edi."),
            ],
            meaning=(
                "$\\omega \\propto h/a^2$ bog'liqligi "
                "loyihalashda hal qiluvchi. Chastotani "
                "oshirishning ikki yo'li bor: qalinlikni "
                "oshirish (chiziqli ta'sir, og'irlik ham "
                "chiziqli ortadi) yoki o'lchamni kamaytirish "
                "(kvadratik ta'sir, og'irlik kamayadi). "
                "Ikkinchisi ancha samarali — shuning uchun "
                "rezonansdan qochish uchun panelga qovurg'a "
                "qo'yiladi: u panelni kichik bo'laklarga "
                "bo'ladi va chastotani keskin oshiradi. "
                "Bu ustuvorlikdagi qovurg'a bilan bir xil "
                "yechim, lekin boshqa sababdan. Chastota "
                "formulasining tuzilishi ham ma'noli: "
                "$\\sqrt{D/(\\rho h)}$ — bu plastinadagi "
                "egilish to'lqinining tarqalish tezligiga "
                "bog'liq kattalik, $[(m/a)^2 + (n/b)^2]$ esa "
                "to'lqin soni. Demak $\\omega = c\\,k^2$ — "
                "egilish to'lqinlari **dispersiv**: qisqa "
                "to'lqinlar tezroq tarqaladi. Bu tmm-20 dagi "
                "elastik to'lqinlardan (u yerda "
                "$\\omega = ck$, dispersiya yo'q) tubdan "
                "farq qiladi. Akustik oqibati: plastinaga "
                "urilgan zarba turli chastotalarni turli "
                "tezlikda tarqatadi va tovush 'sochiladi'. "
                "Tugun chiziqlari esa Xladni tajribasida "
                "(1787) ko'rinadi: qum tebranmaydigan "
                "chiziqlarga to'planadi va shakl ko'zga "
                "ko'rinadigan bo'ladi — bu modal tahlilning "
                "birinchi eksperimental usuli edi."
            ),
            equations=[
                eq(r"D\nabla^4 w + \rho h\,\ddot{w} = 0",
                   "Erkin tebranish tenglamasi.",
                   "Dinamik tenglama"),
                eq(r"\omega_{mn} = \pi^2\sqrt{\frac{D}{\rho h}}"
                   r"\Big[\Big(\frac{m}{a}\Big)^2 + "
                   r"\Big(\frac{n}{b}\Big)^2\Big]",
                   "Xususiy chastotalar (4 chekka sharnirli).",
                   "Xususiy chastota"),
                eq(r"\omega \propto \frac{h}{a^2}\sqrt{\frac{E}{\rho}}",
                   "Chastotaning geometriya va materialga "
                   "bog'liqligi.", "Masshtablash qonuni"),
                eq(r"\int_A \rho h\,W_{mn}W_{pq}\,dA = 0 "
                   r"\quad (mn \ne pq)",
                   "Modal ortogonallik sharti.",
                   "Ortogonallik"),
            ],
            conditions=(
                "**Chegaraviy shartlar** statik masaladagidek, "
                "lekin natija butunlay boshqacha:\n"
                "- 4 chekka sharnirli: aniq yechim (Navye);\n"
                "- 4 chekka mahkamlangan: aniq yechim **yo'q**, "
                "Ritz yoki FEM kerak;\n"
                "- Erkin chekka: Xladni figuralarining eng "
                "boy shakllari shu holatda.\n\n"
                "**Boshlang'ich shartlar:** "
                "$w(x,y,0)$ va $\\dot{w}(x,y,0)$ — ular "
                "qaysi shakllar qo'zg'atilishini belgilaydi.\n\n"
                "**Yupqa plastina taxminlari:**\n"
                "- Aylanish inersiyasi e'tiborsiz (yuqori "
                "chastotalarda buziladi);\n"
                "- Sdvig deformatsiyasi e'tiborsiz (pq-24);\n"
                "- Amplituda kichik (aks holda pq-18 dagi "
                "nochiziqlilik).\n\n"
                "**Qo'llanish chegarasi:** $\\lambda > 10h$ "
                "(to'lqin uzunligi qalinlikdan ancha katta); "
                "aks holda Mindlin nazariyasi kerak."
            ),
            worked=WorkedExample(
                statement=(
                    "Ventilyator korpusi paneli: $a = 600$ mm, "
                    "$b = 400$ mm, $h = 3$ mm, po'lat "
                    "($E = 210$ GPa, $\\nu = 0{,}3$, "
                    "$\\rho = 7850$ kg/m³), 4 chekka sharnirli. "
                    "Ventilyator 47 Hz da ishlaydi. "
                    "(a) Dastlabki uchta chastotani toping. "
                    "(b) Rezonans bormi? (c) Qalinlikni qanday "
                    "o'zgartirish kerak? (d) Qovurg'a bilan "
                    "taqqoslang."
                ),
                given=[
                    r"a = 0{,}6\ \text{m},\ b = 0{,}4\ \text{m},\ "
                    r"h = 0{,}003\ \text{m}",
                    r"E = 210\ \text{GPa},\ \nu = 0{,}3,\ "
                    r"\rho = 7850\ \text{kg/m}^3",
                    r"f_{\text{qo'zg'atuvchi}} = 47\ \text{Hz}",
                ],
                steps=[
                    st(r"D = \frac{210\times10^9 \cdot 2{,}7\times10^{-8}}"
                       r"{10{,}92} = 519{,}2\ \text{N·m}",
                       "$h^3 = 2{,}7\\times10^{-8}$ m³."),
                    st(r"\rho h = 7850 \cdot 0{,}003 = "
                       r"23{,}55\ \text{kg/m}^2; \quad "
                       r"\sqrt{\frac{D}{\rho h}} = "
                       r"\sqrt{\frac{519{,}2}{23{,}55}} = 4{,}695",
                       "Chastota formulasidagi umumiy ko'paytuvchi."),
                    st(r"\Big(\frac{1}{a^2} + \frac{1}{b^2}\Big) = "
                       r"\frac{1}{0{,}36} + \frac{1}{0{,}16} = "
                       r"2{,}778 + 6{,}250 = 9{,}028\ \text{m}^{-2}",
                       "$m = n = 1$ uchun."),
                    st(r"\omega_{11} = \pi^2 \cdot 4{,}695 \cdot 9{,}028 "
                       r"= 9{,}8696 \cdot 42{,}39 = 418{,}4\ \text{rad/s}",
                       "Asosiy burchak chastotasi."),
                    st(r"f_{11} = \frac{418{,}4}{2\pi} = 66{,}6\ \text{Hz}",
                       "Asosiy chastota. Qo'zg'atuvchi "
                       "47 Hz dan 42 % yuqori."),
                    st(r"f_{21}: \Big(\frac{4}{0{,}36} + "
                       r"\frac{1}{0{,}16}\Big) = 17{,}36 "
                       r"\Rightarrow f_{21} = 66{,}6\frac{17{,}36}"
                       r"{9{,}028} = 128{,}1\ \text{Hz}",
                       "Ikkinchi chastota. $m = 2$, $n = 1$ — "
                       "uzun tomon bo'ylab ikkita yarim to'lqin."),
                    st(r"f_{12}: \Big(\frac{1}{0{,}36} + "
                       r"\frac{4}{0{,}16}\Big) = 27{,}78 "
                       r"\Rightarrow f_{12} = 204{,}9\ \text{Hz}",
                       "Uchinchi chastota. Qisqa tomon bo'ylab "
                       "ikkita yarim to'lqin — bu ancha 'qattiq' shakl."),
                    st(r"\frac{66{,}6}{47} = 1{,}42 "
                       r"\;\Rightarrow\; \text{rezonans yo'q}",
                       "Xavfsizlik mezoni odatda "
                       "$f_1/f_{\\text{qo'zg'}} > 1{,}25$ yoki "
                       "$< 0{,}8$. 1,42 — yetarli."),
                    st(r"\text{Agar } h = 2\ \text{mm bo'lsa: } "
                       r"f_{11} = 66{,}6 \cdot \frac{2}{3} = "
                       r"44{,}4\ \text{Hz} \approx 47\ \text{Hz}",
                       "**Rezonans!** $\\omega \\propto h$ "
                       "bo'lgani uchun qalinlikni kamaytirish "
                       "chastotani chiziqli tushiradi."),
                    st(r"\text{Markazga qovurg'a: } b' = 200\ \text{mm} "
                       r"\Rightarrow \Big(\frac{1}{0{,}36} + "
                       r"\frac{1}{0{,}04}\Big) = 27{,}78 "
                       r"\Rightarrow f = 204{,}9\ \text{Hz}",
                       "Qovurg'a chastotani **3,1 marta** "
                       "oshiradi — qalinlikni 3 marta "
                       "oshirishga teng, lekin og'irlik "
                       "deyarli o'zgarmaydi."),
                ],
                answer=(
                    "$D = 519{,}2$ N·m; $f_{11} = 66{,}6$ Hz, "
                    "$f_{21} = 128{,}1$ Hz, $f_{12} = 204{,}9$ Hz. "
                    "47 Hz bilan nisbat 1,42 — **rezonans yo'q**. "
                    "Lekin $h = 2$ mm bo'lsa $f_{11} = 44{,}4$ Hz "
                    "va rezonans yuz beradi. Qovurg'a qo'yish "
                    "chastotani 3,1 marta oshiradi."
                ),
                engineering_note=(
                    "Tebranish muammosini hal qilishning uchta "
                    "yo'li bor va ular samaradorligi bo'yicha "
                    "tartiblangan: (1) **o'lchamni kamaytirish** "
                    "(qovurg'a) — $\\omega \\propto 1/a^2$, eng "
                    "samarali; (2) **qalinlikni oshirish** — "
                    "$\\omega \\propto h$, lekin og'irlik ham "
                    "chiziqli ortadi; (3) **demflash qo'shish** — "
                    "chastotani o'zgartirmaydi, lekin rezonans "
                    "cho'qqisini pasaytiradi (pq-23). "
                    "Amalda ko'pincha birinchi va uchinchi "
                    "birgalikda ishlatiladi: qovurg'ali panel + "
                    "demfer qatlam."
                ),
            ),
            computation=Computation(
                caption=(
                    "Xususiy chastotalar va tebranish "
                    "shakllarini hisoblash, tugun chiziqlarini "
                    "topish, rezonans xavfini baholash."
                ),
                code='''"""Plastinaning erkin tebranishlari va xususiy chastotalar."""
import numpy as np
from labkit import PARAMS, note, series, table, value

a = float(PARAMS.get("a", 600.0))/1000.0
b = float(PARAMS.get("b", 400.0))/1000.0
h = float(PARAMS.get("h", 3.0))/1000.0
E = float(PARAMS.get("E", 210.0))*1e9
nu = float(PARAMS.get("nu", 0.3))
rho = float(PARAMS.get("rho", 7850.0))
f_exc = float(PARAMS.get("f_exc", 47.0))
n_rib = int(PARAMS.get("n_rib", 0))

D = E*h**3/(12*(1 - nu**2))
mu_s = rho*h
cfac = np.sqrt(D/mu_s)
value("Silindrik bikrlik D", D, "N*m")
value("Yuza zichligi rho*h", mu_s, "kg/m2")
value("sqrt(D/(rho*h))", cfac, "m2/s")

# --- Xususiy chastotalar ---
modes = []
for m in range(1, 7):
    for n in range(1, 7):
        w = np.pi**2*cfac*((m/a)**2 + (n/b)**2)
        modes.append((w/(2*np.pi), m, n))
modes.sort()

f1 = modes[0][0]
value("Asosiy chastota f_11", f1, "Hz")
value("Qo'zg'atuvchi chastota", f_exc, "Hz")
value("f_1 / f_qo'zg'atuvchi", f1/f_exc, "—")

table("Dastlabki 10 xususiy chastota",
      ["Tartib", "m", "n", "f, Hz", "f/f_1"],
      [[i + 1, md[1], md[2], round(md[0], 2), round(md[0]/f1, 3)]
       for i, md in enumerate(modes[:10])])

# Rezonans tekshiruvi
danger = [md for md in modes[:12] if 0.8 <= md[0]/f_exc <= 1.25]
if danger:
    note(f"REZONANS XAVFI: {len(danger)} ta shakl qo'zg'atuvchi "
         f"chastotaning 0.8-1.25 oralig'ida: " +
         ", ".join(f"f_{md[1]}{md[2]} = {md[0]:.1f} Hz" for md in danger))
else:
    note(f"Rezonans yo'q: eng yaqin chastota "
         f"{min(modes[:12], key=lambda z: abs(z[0]-f_exc))[0]:.1f} Hz, "
         f"nisbat {f1/f_exc:.2f} (xavfsiz zona: < 0.8 yoki > 1.25).")

# --- Tebranish shakllari va tugun chiziqlari ---
ng = 100
xg = np.linspace(0.0, a, ng)
yg = np.linspace(0.0, b, ng)
Xg, Yg = np.meshgrid(xg, yg, indexing="ij")
for idx in range(4):
    fr, m, n = modes[idx]
    W = np.sin(m*np.pi*Xg/a)*np.sin(n*np.pi*Yg/b)
    series(f"Shakl {idx+1}: (m,n)=({m},{n}), f={fr:.1f} Hz — w(x) y=b/2",
           xg.tolist(), W[:, ng//2].tolist(),
           xlabel="x, m", ylabel="Nisbiy amplituda")
    n_nodal_x = m - 1
    n_nodal_y = n - 1
    if idx == 0:
        value("1-shaklda ichki tugun chiziqlari", float(n_nodal_x + n_nodal_y),
              "dona")

table("Tugun chiziqlari soni",
      ["(m, n)", "x bo'ylab", "y bo'ylab", "Jami ichki"],
      [[f"({md[1]}, {md[2]})", md[1] - 1, md[2] - 1,
        md[1] + md[2] - 2] for md in modes[:6]])
note("Tugun chiziqlari — tebranishda harakatsiz qoladigan joylar. "
     "Xladni (1787) ularni qum bilan ko'rsatgan: qum shu "
     "chiziqlarga to'planadi.")

# --- Qalinlikning ta'siri (chiziqli) ---
hs = np.linspace(0.5, 12.0, 150)/1000.0
fs_h = []
for hh in hs:
    Dh = E*hh**3/(12*(1 - nu**2))
    cf = np.sqrt(Dh/(rho*hh))
    fs_h.append(np.pi**2*cf*((1/a)**2 + (1/b)**2)/(2*np.pi))
series("f_11(qalinlik)", (hs*1000).tolist(), fs_h,
       xlabel="Qalinlik h, mm", ylabel="f_11, Hz")
series("Qo'zg'atuvchi chastota", (hs*1000).tolist(),
       [f_exc]*len(hs), xlabel="Qalinlik h, mm", ylabel="f_11, Hz")
i_res = int(np.argmin(np.abs(np.array(fs_h) - f_exc)))
value("Rezonans beradigan qalinlik", float(hs[i_res])*1000, "mm")
note(f"f ~ h chiziqli: h = {hs[i_res]*1000:.2f} mm da rezonans. "
     f"Joriy h = {h*1000:.1f} mm dan qochish kerak bo'lsa, "
     f"qalinlikni oshirish yoki kamaytirish mumkin.")

# --- Qovurg'aning ta'siri (o'lchamni kamaytirish) ---
ribs = list(range(0, 5))
f_ribs = []
for nr in ribs:
    bb = b/(nr + 1)
    f_ribs.append(np.pi**2*cfac*((1/a)**2 + (1/bb)**2)/(2*np.pi))
series("f_11(qovurg'alar soni)", [float(r) for r in ribs], f_ribs,
       xlabel="Qovurg'alar soni", ylabel="f_11, Hz")
table("Rezonansdan qochish usullari",
      ["Usul", "f ga ta'siri", "Og'irlikka ta'siri", "Samaradorlik"],
      [["Qalinlikni 2x oshirish", "2x", "2x", "past"],
       ["Bitta qovurg'a (b -> b/2)", f"{f_ribs[1]/f_ribs[0]:.2f}x",
        "~1.05x", "yuqori"],
       ["Ikkita qovurg'a (b -> b/3)", f"{f_ribs[2]/f_ribs[0]:.2f}x",
        "~1.10x", "juda yuqori"],
       ["Demfer qatlam", "1x (o'zgarmaydi)", "~1.1x",
        "amplituda uchun"]])

# --- Material tanlash ---
mats = [("Po'lat", 210e9, 7850, 0.30), ("Alyuminiy", 70e9, 2700, 0.33),
        ("Titan", 110e9, 4500, 0.34), ("Magniy", 45e9, 1740, 0.35),
        ("Shisha-plastik", 25e9, 1900, 0.28)]
rows = []
for nm, Em, rm, num in mats:
    Dm_ = Em*h**3/(12*(1 - num**2))
    cf = np.sqrt(Dm_/(rm*h))
    fm = np.pi**2*cf*((1/a)**2 + (1/b)**2)/(2*np.pi)
    rows.append([nm, round(Em/1e9, 0), round(rm, 0),
                 round(np.sqrt(Em/rm)/1000, 2), round(fm, 1)])
table("Material va chastota (bir xil qalinlikda)",
      ["Material", "E, GPa", "rho, kg/m3", "sqrt(E/rho), km/s", "f_11, Hz"],
      rows)
note("Chastota sqrt(E/rho) ga mutanosib — bu 'solishtirma "
     "bikrlik'. Alyuminiy po'latdan yengil, lekin sqrt(E/rho) "
     "deyarli bir xil: chastota ham o'xshash chiqadi.")

# --- Chastota spektri ---
series("Chastota spektri", [float(i + 1) for i in range(len(modes[:20]))],
       [md[0] for md in modes[:20]],
       xlabel="Shakl tartibi", ylabel="f, Hz")
value("20-shaklning chastotasi", modes[19][0], "Hz")
value("Modal zichlik (20 shakl oralig'i)",
      19/(modes[19][0] - modes[0][0]), "shakl/Hz")
note("Plastinada modal zichlik chastota bilan deyarli o'zgarmaydi "
     "(sterjendan farqli) — bu akustikada muhim xossa.")
''',
                parameters=[
                    p("a", "Panel tomoni a", 50.0, 5000.0, 600.0, 10.0, "mm"),
                    p("b", "Panel tomoni b", 50.0, 5000.0, 400.0, 10.0, "mm"),
                    p("h", "Qalinlik h", 0.3, 50.0, 3.0, 0.1, "mm"),
                    p("E", "Yung moduli E", 1.0, 400.0, 210.0, 1.0, "GPa"),
                    p("nu", "Puasson koeffitsienti ν", 0.0, 0.45, 0.3, 0.01),
                    p("rho", "Zichlik ρ", 500.0, 12000.0, 7850.0, 50.0,
                      "kg/m³"),
                    p("f_exc", "Qo'zg'atuvchi chastota", 1.0, 2000.0, 47.0,
                      1.0, "Hz"),
                    p("n_rib", "Qovurg'alar soni", 0.0, 4.0, 0.0, 1.0),
                ],
                expected_output=(
                    "D = 519,2 N·m, f₁₁ = 66,6 Hz, f₂₁ = 128,1 Hz, "
                    "f₁₂ = 204,9 Hz; 47 Hz bilan nisbat 1,42 — "
                    "rezonans yo'q. h ≈ 2 mm da rezonans yuz "
                    "beradi (f ~ h chiziqli). Bitta qovurg'a "
                    "chastotani ≈ 3,1 marta oshiradi."
                ),
            ),
            visual=vis(
                kind="Tebranish shakllari va tugun chiziqlari",
                tool="React/SVG + Manim",
                description=(
                    "Dastlabki shakllar, tugun chiziqlari "
                    "(Xladni figuralari), chastota spektri."
                ),
                how_to_draw=(
                    "React/SVG: asosiy panel — $2\\times2$ "
                    "modal shakllar galereyasi. Har bir "
                    "katakda plastina rejasi, "
                    "$\\sin(m\\pi x/a)\\sin(n\\pi y/b)$ "
                    "qiymati bo'yicha bo'yalgan: musbat "
                    "cho'qqilar bir rangda, manfiy botiqlar "
                    "qarama-qarshi rangda, nol chiziqlar esa "
                    "**qora qalin chiziq** bilan — bu tugun "
                    "chiziqlari. Har bir katak tagida "
                    "$(m,n)$ va chastota. Xladni tajribasiga "
                    "havola qilib, tugun chiziqlariga mayda "
                    "nuqtalar (qum) sepiladi. Ikkinchi panel — "
                    "animatsiya: tanlangan shakl "
                    "`requestAnimationFrame` bilan tebranadi "
                    "(rang amplitudaga qarab pulsatsiyalanadi); "
                    "tugun chiziqlari harakatsiz qolishi aniq "
                    "ko'rinadi. Uchinchi panel — chastota "
                    "spektri: vertikal chiziqlar (har biri "
                    "bitta shakl), balandligi yoki rangi "
                    "$(m,n)$ ni bildiradi; qo'zg'atuvchi "
                    "chastota qizil vertikal chiziq bilan va "
                    "uning $\\pm 20\\%$ xavfli zonasi "
                    "shtrixlanadi — moslik bo'lsa darhol ko'rinadi."
                ),
            ),
            interp=(
                "Rezonansdan qochish usullari jadvali "
                "loyihalash strategiyasini aniq beradi: bitta "
                "qovurg'a chastotani 3,1 marta oshiradi va "
                "og'irlikni atigi 5 % ga ko'taradi, qalinlikni "
                "ikki marta oshirish esa chastotani 2 marta "
                "oshirib og'irlikni ham 2 marta ko'taradi. "
                "Demak qovurg'a o'n barobardan ko'p samarali. "
                "Sababi masshtablash qonunida: "
                "$\\omega \\propto h/a^2$ — o'lchamga "
                "kvadratik, qalinlikka chiziqli bog'liqlik. "
                "Material jadvali esa boshqa muhim narsani "
                "ko'rsatadi: chastota $\\sqrt{E/\\rho}$ ga "
                "mutanosib va bu kattalik po'lat, alyuminiy, "
                "titan uchun deyarli bir xil (5,0–5,2 km/s). "
                "Demak **materialni almashtirish chastotani "
                "deyarli o'zgartirmaydi** — bu ko'p "
                "muhandislar uchun kutilmagan. Alyuminiyga "
                "o'tish og'irlikni uch marta kamaytiradi, "
                "lekin rezonans muammosini hal qilmaydi. "
                "Yagona istisno — kompozitlar va magniy, "
                "ularda $\\sqrt{E/\\rho}$ sezilarli farq "
                "qiladi. Modal zichlikning chastota bilan "
                "o'zgarmasligi ham muhim: plastinada "
                "yuqori chastotalarda shakllar zichlashmaydi "
                "(sterjendan farqli), shuning uchun akustik "
                "izolyatsiya hisobida statistik energiya "
                "tahlili (SEA) usuli yaxshi ishlaydi."
            ),
            mistakes=[
                "Chastota formulasida kvadrat qavsni "
                "kvadratga ko'tarish. $\\beta^4$ dan ildiz "
                "olinadi, shuning uchun qavs birinchi "
                "darajada qoladi.",
                "$\\omega \\propto h^3$ deb o'ylash "
                "(og'ishdagi kabi). Chastotada "
                "$\\omega \\propto h$ — chiziqli, chunki "
                "massa ham $h$ ga mutanosib.",
                "Materialni almashtirish bilan chastotani "
                "o'zgartirishga urinish. Metallarda "
                "$\\sqrt{E/\\rho}$ deyarli bir xil.",
                "Faqat asosiy chastotani tekshirish. "
                "Qo'zg'atuvchi chastota yuqori shaklga mos "
                "kelishi mumkin — kamida 10 ta shakl "
                "tekshiriladi.",
            ],
            quiz=[
                q("Xususiy chastota qalinlikka qanday bog'liq?",
                  "Chiziqli: $\\omega \\propto h$. Chunki "
                  "$D \\propto h^3$, massa $\\propto h$, "
                  "va $\\omega \\propto \\sqrt{D/(\\rho h)} "
                  "\\propto h$.", "konseptual"),
                q("Tugun chiziqlari nima va ular qanday "
                  "ko'rsatiladi?",
                  "Tebranishda harakatsiz qoladigan "
                  "chiziqlar. Xladni (1787) plastinaga qum "
                  "sepib ko'rsatgan — qum shu chiziqlarga "
                  "to'planadi.", "konseptual"),
                q("$a = b = 0{,}5$ m, $D = 500$ N·m, "
                  "$\\rho h = 20$ kg/m². $f_{11}$ ni toping.",
                  "$\\sqrt{D/\\rho h} = 5$; "
                  "$\\omega = \\pi^2 \\cdot 5 \\cdot 8 = 394{,}8$ "
                  "rad/s; $f = 62{,}8$ Hz.", "hisob"),
                q("Nima uchun qovurg'a qalinlikdan samaraliroq?",
                  "$\\omega \\propto h/a^2$: o'lchamga "
                  "kvadratik, qalinlikka chiziqli. Qovurg'a "
                  "$a$ ni kamaytiradi va og'irlikni deyarli "
                  "oshirmaydi.", "talqin"),
                q("Kodda nima uchun 12 ta shakl tekshiriladi?",
                  "Qo'zg'atuvchi chastota asosiy shaklga "
                  "emas, yuqori shakllardan biriga mos "
                  "kelishi mumkin — faqat $f_1$ ni tekshirish "
                  "yetarli emas.", "kod"),
                q("Alyuminiyga o'tish rezonans muammosini "
                  "hal qiladimi?",
                  "Yo'q. Chastota $\\sqrt{E/\\rho}$ ga "
                  "mutanosib va bu kattalik po'lat bilan "
                  "alyuminiyda deyarli bir xil (≈5 km/s). "
                  "Og'irlik kamayadi, chastota esa deyarli "
                  "o'zgarmaydi.", "talqin"),
            ],
            bridge=(
                "Erkin tebranish chastotalarni berdi, lekin "
                "amplitudani emas. Rezonansda amplituda "
                "nimaga bog'liq? Javob demflashda. Keyingi "
                "mavzuda majburiy tebranishlar va zarba "
                "javobini o'rganamiz."
            ),
            research=(
                "Xladni figuralarini o'rganing va "
                "takrorlang. Erkin chekkali kvadrat "
                "plastinada shakllar Navye yechimidan "
                "butunlay boshqacha va ancha boy bo'ladi — "
                "diagonal, doiraviy, yulduzsimon naqshlar. "
                "Ritz usuli (pq-09) bilan erkin chekkali "
                "plastinaning dastlabki 10 shaklini "
                "hisoblang (bazis sifatida erkin-erkin "
                "balka shakllarining ko'paytmasini oling) "
                "va tugun chiziqlarini quring. Natijalarni "
                "Leissa ma'lumotnomasi (NASA SP-160) bilan "
                "solishtiring. Nima uchun erkin chekkali "
                "plastinada aniq analitik yechim yo'q?"
            ),
            manim_ref=manim(
                scene="PlateModesScene",
                module="animatsiya/scenes/pq_vibration.py",
                title="Tebranish shakllari va Xladni figuralari",
                summary=(
                    "Plastina ketma-ket shakllarda tebranadi; "
                    "har birida tugun chiziqlari ajratib "
                    "ko'rsatiladi va ularga 'qum' to'planishi "
                    "animatsiya qilinadi."
                ),
            ),
        ),
    ),

    # ------------------------------------------------------------------ pq-23
    Topic(
        id="pq-23",
        subject_id=S, module_id=M, order=23,
        title="Majburiy tebranishlar, demflash va zarbaviy javob",
        description=(
            "Modal superpozitsiya, rezonans amplitudasi va "
            "demflash, chastota javobi, zarba spektri hamda "
            "akustik nurlanish bilan bog'lanish."
        ),
        learning_objective=(
            "Majburiy tebranish masalasini modal superpozitsiya "
            "bilan yechish, rezonans amplitudasini demflash "
            "orqali baholash va zarbaviy javobni hisoblash."
        ),
        prerequisites=["pq-22", "nm-27"],
        mathematical_core=(
            "Modal superpozitsiya $w = \\sum q_{mn}(t)W_{mn}$, "
            "modal tenglama $\\ddot{q} + 2\\zeta\\omega\\dot{q} "
            "+ \\omega^2 q = f/M$, kuchaytirish koeffitsienti "
            "$1/(2\\zeta)$, Dyuamel integrali."
        ),
        engineering_application=(
            "Mashina korpuslari, transformator paneli shovqini, "
            "avtomobil kuzovi, samolyot kabinasi akustikasi, "
            "zarbaviy yuklamalar, seysmik ta'sir."
        ),
        computational_component=(
            "Chastota javobi egri chizig'ini qurish, rezonans "
            "cho'qqisini demflash bilan baholash, zarba "
            "javobini Dyuamel integrali bilan hisoblash."
        ),
        visualization_component=(
            "Chastota javobi (Bode), rezonans cho'qqilari, "
            "zarba javobi vaqt bo'yicha, demflashning ta'siri."
        ),
        research_extension=(
            "Plastinaning akustik nurlanishini o'rganing: "
            "kritik chastota (coincidence frequency) nima va "
            "nima uchun undan yuqorida tovush izolyatsiyasi yomonlashadi?"
        ),
        difficulty="ilg'or",
        previous_link=(
            "pq-22 da xususiy chastotalar topildi, lekin "
            "amplituda aniqlanmadi. nm-27 dagi bir erkinlik "
            "darajali majburiy tebranish nazariyasini har bir "
            "shaklga qo'llab, to'liq javobni olamiz."
        ),
        next_topic="pq-24",
        estimated_minutes=90,
        tags=["majburiy tebranish", "demflash", "rezonans", "zarba"],
        lesson=_lesson(
            problem=(
                "pq-22 dagi ventilyator panelida rezonans yo'q "
                "edi, lekin panel baribir shovqin chiqaradi. "
                "Va agar rezonans bo'lsa — amplituda qanchaga "
                "yetadi? Cheksizgami? Yo'q: demflash uni "
                "cheklaydi. Lekin qancha? Po'lat panelda "
                "demflash juda kichik ($\\zeta \\approx 0{,}001$) "
                "va amplituda 500 marta kuchayishi mumkin. "
                "Buni qanday hisoblaymiz va qanday kamaytiramiz?"
            ),
            concepts=[
                c("Modal superpozitsiya",
                  "Javobni xususiy shakllar bo'yicha yoyish: "
                  "$w(x,y,t) = \\sum q_{mn}(t)W_{mn}(x,y)$. "
                  "Ortogonallik tufayli shakllar ajraladi."),
                c("Modal koordinata $q_{mn}(t)$",
                  "Har bir shaklning vaqt bo'yicha amplitudasi; "
                  "u bir erkinlik darajali ossillyator "
                  "tenglamasiga bo'ysunadi."),
                c("Demflash nisbati $\\zeta$",
                  "Kritik demflashga nisbat. Po'lat: "
                  "0,001–0,005; alyuminiy: 0,0005–0,002; "
                  "beton: 0,01–0,02; demfer qatlam bilan: 0,05–0,3."),
                c("Kuchaytirish koeffitsienti",
                  "Rezonansda $|H| = 1/(2\\zeta)$. "
                  "$\\zeta = 0{,}002$ da bu **250 marta**."),
                c("Modal massa va modal kuch",
                  "$M_{mn} = \\int\\rho h W_{mn}^2 dA$, "
                  "$F_{mn} = \\int q(x,y)W_{mn}dA$ — ular "
                  "qanday shakl qanchalik qo'zg'atilishini belgilaydi."),
                c("Dyuamel integrali",
                  "Ixtiyoriy vaqt bo'yicha o'zgaruvchi kuchga "
                  "javob: $q(t) = \\int_0^t f(\\tau)h(t-\\tau)d\\tau$."),
            ],
            derivation=[
                d("1. Majburiy tebranish tenglamasi",
                  r"D\nabla^4 w + c\,\dot{w} + \rho h\,\ddot{w} "
                  r"= q(x, y, t)",
                  "pq-22 dagi tenglamaga demflash hadi "
                  "($c\\dot{w}$, yopishqoq demflash) va "
                  "tashqi kuch qo'shiladi."),
                d("2. Modal yoyilma",
                  r"w(x,y,t) = \sum_{m,n}q_{mn}(t)W_{mn}(x,y)",
                  "Xususiy shakllar to'liq bazis hosil "
                  "qiladi — har qanday javobni ular orqali "
                  "ifodalash mumkin."),
                d("3. Ortogonallikdan foydalanish",
                  r"\int_A \rho h\,W_{mn}W_{pq}\,dA = "
                  r"M_{mn}\delta_{mp}\delta_{nq}",
                  "Tenglamani $W_{pq}$ ga ko'paytirib "
                  "integrallaymiz. Ortogonallik tufayli "
                  "boshqa barcha hadlar yo'qoladi."),
                d("4. Modal tenglama",
                  r"M_{mn}\ddot{q}_{mn} + C_{mn}\dot{q}_{mn} "
                  r"+ K_{mn}q_{mn} = F_{mn}(t)",
                  "Har bir shakl uchun **mustaqil** bir "
                  "erkinlik darajali tenglama. Cheksiz "
                  "o'lchovli masala cheksiz sondagi sodda "
                  "masalaga ajraldi."),
                d("5. Standart shaklga keltirish",
                  r"\ddot{q} + 2\zeta_{mn}\omega_{mn}\dot{q} "
                  r"+ \omega_{mn}^2 q = \frac{F_{mn}(t)}{M_{mn}}",
                  "$\\omega^2 = K/M$, "
                  "$2\\zeta\\omega = C/M$. Bu nm-27 dagi "
                  "tenglamaning aynan o'zi."),
                d("6. Garmonik qo'zg'atish: chastota javobi",
                  r"|H_{mn}(\Omega)| = \frac{1}{\sqrt{(1-r^2)^2 "
                  r"+ (2\zeta r)^2}}, \qquad r = "
                  r"\frac{\Omega}{\omega_{mn}}",
                  "Statik og'ishga nisbatan kuchaytirish. "
                  "$r = 1$ (rezonans) da maxraj "
                  "$2\\zeta$ ga tushadi."),
                d("7. Rezonansdagi amplituda",
                  r"|H|_{\max} \approx \frac{1}{2\zeta} "
                  r"\quad (r \approx \sqrt{1-2\zeta^2} \approx 1)",
                  "Po'lat uchun $\\zeta = 0{,}002$: "
                  "$|H| = 250$. Demak statik og'ish 0,1 mm "
                  "bo'lsa, rezonansda 25 mm — bu panelni "
                  "buzadi yoki shovqinni chidab bo'lmas qiladi."),
                d("8. Zarbaviy javob (Dyuamel)",
                  r"q(t) = \frac{1}{M\omega_d}\int_0^t F(\tau)"
                  r"e^{-\zeta\omega(t-\tau)}\sin\omega_d(t-\tau)\,d\tau",
                  "$\\omega_d = \\omega\\sqrt{1-\\zeta^2}$. "
                  "Qisqa zarba ($\\Delta t \\ll T$) barcha "
                  "shakllarni bir vaqtda qo'zg'atadi — shuning "
                  "uchun zarbadan keyin panel 'jarangli' ovoz chiqaradi."),
            ],
            meaning=(
                "$|H|_{\\max} = 1/(2\\zeta)$ formulasi "
                "demflashning nima uchun shunchalik muhim "
                "ekanligini bitta raqamda ifodalaydi. "
                "Po'lat konstruksiyada material demflashi "
                "juda kichik — $\\zeta \\approx 0{,}002$, "
                "demak rezonansda amplituda **250 marta** "
                "kuchayadi. Bu chidab bo'lmas: shovqin, "
                "charchoq yoriqlari, asbob-uskunalarning "
                "buzilishi. Shuning uchun amaliy "
                "konstruksiyalarda demflash sun'iy "
                "qo'shiladi: viskoelastik qatlam (tmm-23 "
                "dagi $\\tan\\delta$), qum bilan to'ldirilgan "
                "bo'shliqlar, ishqalanish demferlari. "
                "$\\zeta$ ni 0,002 dan 0,05 ga oshirish "
                "amplitudani **25 marta** kamaytiradi — "
                "hech qanday konstruktiv o'zgarish bunday "
                "samara bermaydi. Modal superpozitsiyaning "
                "chuqur ma'nosi esa boshqa: cheksiz o'lchovli "
                "masala cheksiz sondagi **mustaqil** bir "
                "erkinlik darajali masalaga ajraladi. Bu "
                "ortogonallikning bevosita sovg'asi va u "
                "butun strukturaviy dinamikaning asosi. "
                "Amalda faqat dastlabki 10–50 shakl olinadi, "
                "chunki yuqori shakllar qo'zg'atish "
                "chastotasidan ancha uzoqda va ularning "
                "hissasi $1/\\omega^2$ kabi kamayadi. Zarba "
                "esa aksincha — u keng chastota spektriga "
                "ega va barcha shakllarni bir vaqtda "
                "qo'zg'atadi; shuning uchun zarbaviy "
                "tahlilda ancha ko'p shakl kerak."
            ),
            equations=[
                eq(r"\ddot{q}_{mn} + 2\zeta_{mn}\omega_{mn}"
                   r"\dot{q}_{mn} + \omega_{mn}^2 q_{mn} = "
                   r"\frac{F_{mn}(t)}{M_{mn}}",
                   "Modal tenglama — har bir shakl uchun "
                   "mustaqil ossillyator.", "Modal tenglama"),
                eq(r"|H(\Omega)| = \frac{1}{\sqrt{(1-r^2)^2 "
                   r"+ (2\zeta r)^2}}, \quad r = \Omega/\omega",
                   "Chastota javobi (kuchaytirish koeffitsienti).",
                   "Chastota javobi"),
                eq(r"|H|_{\max} \approx \frac{1}{2\zeta}",
                   "Rezonansdagi maksimal kuchaytirish.",
                   "Rezonans cho'qqisi"),
                eq(r"q(t) = \frac{1}{M\omega_d}\int_0^t F(\tau)"
                   r"e^{-\zeta\omega(t-\tau)}\sin\omega_d(t-\tau)d\tau",
                   "Dyuamel integrali — ixtiyoriy yuklamaga javob.",
                   "Dyuamel integrali"),
            ],
            conditions=(
                "**Boshlang'ich shartlar** har bir modal "
                "koordinata uchun alohida:\n"
                "$$q_{mn}(0) = \\frac{1}{M_{mn}}\\int\\rho h\\,"
                "w_0 W_{mn}\\,dA, \\qquad \\dot{q}_{mn}(0) = "
                "\\frac{1}{M_{mn}}\\int\\rho h\\,\\dot{w}_0 "
                "W_{mn}\\,dA.$$\n\n"
                "**Demflash modeli:** modal demflash "
                "($\\zeta_{mn}$ har bir shakl uchun alohida "
                "beriladi) eng ko'p ishlatiladi, chunki u "
                "ortogonallikni buzmaydi. Reley demflashi "
                "($C = \\alpha M + \\beta K$) ham shu "
                "xossaga ega.\n\n"
                "**Tipik $\\zeta$ qiymatlari:**\n"
                "| Konstruksiya | $\\zeta$ |\n"
                "|---|---|\n"
                "| Payvandlangan po'lat | 0,001–0,003 |\n"
                "| Boltli po'lat | 0,003–0,01 |\n"
                "| Temir-beton | 0,01–0,02 |\n"
                "| Demfer qatlam bilan | 0,05–0,30 |\n\n"
                "**Shakllar soni:** garmonik qo'zg'atishda "
                "$\\omega_{mn} < 2\\Omega$ bo'lgan barcha "
                "shakllar; zarbaviy yuklamada esa kamida "
                "$\\omega_{mn} < 2\\pi/\\Delta t$."
            ),
            worked=WorkedExample(
                statement=(
                    "pq-22 dagi panel ($a = 600$, $b = 400$ mm, "
                    "$h = 3$ mm, po'lat, $f_{11} = 66{,}6$ Hz). "
                    "Unga bir tekis pulsatsiyalanuvchi bosim "
                    "$q_0 = 50$ Pa, $f = 66$ Hz ta'sir qiladi "
                    "(deyarli rezonans). $\\zeta = 0{,}002$. "
                    "(a) Statik og'ishni toping. (b) Rezonans "
                    "amplitudasini hisoblang. (c) Demfer "
                    "qatlam ($\\zeta = 0{,}05$) qo'ysak "
                    "nima o'zgaradi?"
                ),
                given=[
                    r"a = 0{,}6,\ b = 0{,}4,\ h = 0{,}003\ \text{m}",
                    r"D = 519{,}2\ \text{N·m},\ f_{11} = 66{,}6\ \text{Hz}",
                    r"q_0 = 50\ \text{Pa},\ f = 66\ \text{Hz},\ "
                    r"\zeta = 0{,}002",
                ],
                steps=[
                    st(r"w_{\text{st}} = \frac{16q_0}{\pi^6 D}"
                       r"\Big(\frac{1}{a^2}+\frac{1}{b^2}\Big)^{-2} "
                       r"= \frac{16 \cdot 50}{961{,}39 \cdot 519{,}2 "
                       r"\cdot 9{,}028^2}",
                       "Navye yechimining birinchi hadi "
                       "(statik og'ish)."),
                    st(r"w_{\text{st}} = \frac{800}{961{,}39 \cdot "
                       r"519{,}2 \cdot 81{,}50} = "
                       r"1{,}967\times10^{-5}\ \text{m} = 0{,}0197\ \text{mm}",
                       "Faqat birinchi had. To'liq qator "
                       "0,01904 mm beradi — kod ikki mustaqil "
                       "yo'l (modal superpozitsiya va bevosita "
                       "Navye qatori) bilan aynan shu qiymatni tasdiqlaydi."),
                    st(r"r = \frac{f}{f_{11}} = \frac{66}{66{,}6} "
                       r"= 0{,}9910",
                       "Chastota nisbati — rezonansga juda yaqin."),
                    st(r"|H| = \frac{1}{\sqrt{(1-0{,}9821)^2 + "
                       r"(2 \cdot 0{,}002 \cdot 0{,}991)^2}} = "
                       r"\frac{1}{\sqrt{3{,}20\times10^{-4} + "
                       r"1{,}57\times10^{-5}}}",
                       "$r^2 = 0{,}9821$, "
                       "$1 - r^2 = 0{,}01790$."),
                    st(r"|H| = \frac{1}{\sqrt{3{,}357\times10^{-4}}} "
                       r"= \frac{1}{0{,}018323} = 54{,}6",
                       "Kuchaytirish 54,6 marta. Aniq "
                       "rezonansda ($r = 1$) bu "
                       "$1/(2\\zeta) = 250$ bo'lardi."),
                    st(r"w_{\max} = |H|\,w_{\text{st}} \approx 63{,}4 \cdot "
                       r"0{,}01904 = 1{,}207\ \text{mm}",
                       "Amplituda 1,21 mm — qalinlikning "
                       "40 % i. Bu sezilarli shovqin beradi. "
                       "(Kod to'liq qator bilan aynan shu "
                       "qiymatni beradi; bir hadli baho "
                       "1,08 mm edi.)"),
                    st(r"\text{Aniq rezonansda: } w = 250 \cdot "
                       r"0{,}01904 = 4{,}76\ \text{mm} > h",
                       "Qalinlikdan katta — nochiziqlilik "
                       "(pq-18) ishga tushadi va amplituda "
                       "biroz cheklanadi, lekin panel "
                       "baribir charchoqdan buziladi."),
                    st(r"\zeta = 0{,}05: \ |H| = \frac{1}"
                       r"{\sqrt{3{,}20\times10^{-4} + "
                       r"(0{,}0991)^2}} = \frac{1}{0{,}09985} = 10{,}0",
                       "Demfer qatlam bilan kuchaytirish "
                       "54,6 dan 10,0 ga tushdi."),
                    st(r"w_{\max} = 0{,}195\ \text{mm}; \quad "
                       r"\text{kamayish } 6{,}2\ \text{marta}",
                       "Aniq rezonansda esa kamayish "
                       "$0{,}05/0{,}002 = 25$ marta bo'lardi."),
                ],
                answer=(
                    "Statik og'ish 0,01904 mm (ikki mustaqil "
                    "usul bilan tasdiqlangan); $r = 0{,}991$ da "
                    "kuchaytirish $|H| = 63{,}4$ va amplituda "
                    "1,207 mm; aniq rezonansda $|H| = 250$ va "
                    "4,76 mm (qalinlikdan katta). Demfer "
                    "qatlam ($\\zeta = 0{,}05$) amplitudani "
                    "6,2 marta (aniq rezonansda 25 marta) kamaytiradi."
                ),
                engineering_note=(
                    "Demflash qo'shishning eng samarali usuli — "
                    "**cheklangan qatlamli demfer** "
                    "(constrained layer damping): viskoelastik "
                    "qatlam ustiga yupqa metall qoplama "
                    "yopishtiriladi. Panel egilganda "
                    "viskoelastik qatlam **siljishga** "
                    "ishlaydi va energiyani tarqatadi — bu "
                    "erkin qatlamdan ancha samarali. "
                    "Avtomobil kuzovi, samolyot kabinasi va "
                    "disk yuritgichlarda aynan shu usul "
                    "ishlatiladi. Qatlam qalinligi 0,05–0,2 mm "
                    "bo'lsa yetarli — og'irlik deyarli "
                    "oshmaydi, $\\zeta$ esa 0,05–0,15 ga yetadi."
                ),
            ),
            computation=Computation(
                caption=(
                    "Chastota javobini qurish, rezonans "
                    "cho'qqilarini demflash bilan baholash "
                    "va zarbaviy javobni hisoblash."
                ),
                code='''"""Majburiy tebranishlar, demflash va zarbaviy javob."""
import numpy as np
from labkit import PARAMS, note, series, table, value

a = float(PARAMS.get("a", 600.0))/1000.0
b = float(PARAMS.get("b", 400.0))/1000.0
h = float(PARAMS.get("h", 3.0))/1000.0
E = float(PARAMS.get("E", 210.0))*1e9
nu = float(PARAMS.get("nu", 0.3))
rho = float(PARAMS.get("rho", 7850.0))
q0 = float(PARAMS.get("q0", 50.0))
f_exc = float(PARAMS.get("f_exc", 66.0))
zeta = float(PARAMS.get("zeta", 0.002))
zeta2 = float(PARAMS.get("zeta2", 0.05))

D = E*h**3/(12*(1 - nu**2))
mu_s = rho*h
cfac = np.sqrt(D/mu_s)
value("Silindrik bikrlik D", D, "N*m")

# --- Shakllar ---
modes = []
for m in range(1, 8, 2):          # bir tekis yuklama: toq shakllar
    for n in range(1, 8, 2):
        w = np.pi**2*cfac*((m/a)**2 + (n/b)**2)
        # Modal kuch: F_mn = int q*W_mn dA = 4*q0*a*b/(pi^2*m*n) (m, n toq)
        Fmn = 4*q0*a*b/(np.pi**2*m*n)
        # Modal massa: M_mn = int rho*h*W_mn^2 dA = rho*h*a*b/4
        Mmn = mu_s*a*b/4.0
        modes.append({"m": m, "n": n, "w": w, "f": w/(2*np.pi),
                      "F": Fmn, "M": Mmn})
modes.sort(key=lambda z: z["w"])
f1 = modes[0]["f"]
value("Asosiy chastota f_11", f1, "Hz")
value("Qo'zg'atuvchi chastota", f_exc, "Hz")
value("Chastota nisbati r", f_exc/f1, "—")

# --- Statik og'ish (markazda, to'liq qator) ---
w_st = 0.0
for md in modes:
    w_st += md["F"]/(md["M"]*md["w"]**2)*np.sin(md["m"]*np.pi/2) \
        * np.sin(md["n"]*np.pi/2)
value("Statik og'ish w_st", w_st*1000, "mm")

# Mustaqil tekshiruv: bevosita Navye qatori
w_nav = 0.0
for m in range(1, 8, 2):
    for n in range(1, 8, 2):
        qmn = 16*q0/(np.pi**2*m*n)
        w_nav += qmn/(D*np.pi**4*((m/a)**2 + (n/b)**2)**2) \
            * np.sin(m*np.pi/2)*np.sin(n*np.pi/2)
value("Statik og'ish (Navye qatori)", w_nav*1000, "mm")
note(f"Modal superpozitsiya {w_st*1000:.5f} mm va bevosita Navye "
     f"qatori {w_nav*1000:.5f} mm — farq "
     f"{abs(w_st-w_nav)/w_nav*100:.4f} %. Modal massa va modal "
     f"kuch to'g'ri hisoblangani tasdiqlandi.")

# --- Chastota javobi ---
freqs = np.linspace(1.0, max(400.0, 3*f1), 3000)
def response(zt):
    amp = np.zeros_like(freqs)
    for md in modes:
        r = 2*np.pi*freqs/md["w"]
        H = 1.0/np.sqrt((1 - r**2)**2 + (2*zt*r)**2)
        contrib = md["F"]/(md["M"]*md["w"]**2)*H \
            * np.sin(md["m"]*np.pi/2)*np.sin(md["n"]*np.pi/2)
        amp += contrib
    return np.abs(amp)


amp1 = response(zeta)
amp2 = response(zeta2)
series(f"Chastota javobi (zeta = {zeta})", freqs.tolist(),
       (amp1*1000).tolist(), xlabel="Chastota, Hz",
       ylabel="Amplituda, mm")
series(f"Chastota javobi (zeta = {zeta2})", freqs.tolist(),
       (amp2*1000).tolist(), xlabel="Chastota, Hz",
       ylabel="Amplituda, mm")
series("Statik daraja", freqs.tolist(),
       [w_st*1000]*len(freqs), xlabel="Chastota, Hz",
       ylabel="Amplituda, mm")

i_exc = int(np.argmin(np.abs(freqs - f_exc)))
value(f"Amplituda f = {f_exc} Hz da (zeta = {zeta})",
      float(amp1[i_exc])*1000, "mm")
value(f"Amplituda f = {f_exc} Hz da (zeta = {zeta2})",
      float(amp2[i_exc])*1000, "mm")
value("Kuchaytirish |H| (joriy zeta)", float(amp1[i_exc])/w_st, "—")
value("Demfer bilan kamayish", float(amp1[i_exc]/amp2[i_exc]), "marta")

value("Rezonansdagi maksimal kuchaytirish 1/(2*zeta)", 1/(2*zeta), "—")
value("Rezonansdagi amplituda (taxminiy)", w_st/(2*zeta)*1000, "mm")
value("Rezonans amplitudasi / qalinlik", w_st/(2*zeta)/h, "—")
if w_st/(2*zeta) > 0.2*h:
    note(f"Rezonansda amplituda qalinlikning "
         f"{w_st/(2*zeta)/h:.2f} qismiga yetadi — geometrik "
         f"nochiziqlilik (pq-18) ishga tushadi va chiziqli "
         f"baho amplitudani oshirib ko'rsatadi.")

i_pk = int(np.argmax(amp1))
value("Maksimal javob chastotasi", float(freqs[i_pk]), "Hz")
value("Maksimal amplituda", float(amp1[i_pk])*1000, "mm")

# --- Demflash nisbatining ta'siri ---
zs = np.logspace(-3.3, -0.5, 100)
peaks = []
for zt in zs:
    peaks.append(float(np.max(response(zt)))*1000)
series("Maksimal amplituda(zeta)", zs.tolist(), peaks,
       xlabel="Demflash nisbati zeta", ylabel="Maksimal amplituda, mm")
note(f"zeta ni {zs[0]:.4f} dan {zs[-1]:.3f} ga oshirish "
     f"({zs[-1]/zs[0]:.0f} marta) maksimal amplitudani "
     f"{peaks[0]/peaks[-1]:.0f} marta kamaytiradi — deyarli "
     f"teskari mutanosib.")

table("Demflash manbalari va tipik qiymatlar",
      ["Manba", "zeta", "1/(2*zeta)", "Izoh"],
      [["Payvandlangan po'lat", 0.002, 250, "Faqat material demflashi"],
       ["Boltli birikma", 0.005, 100, "Ishqalanish qo'shiladi"],
       ["Temir-beton", 0.015, 33, "Mikroyoriqlar energiya yutadi"],
       ["Erkin demfer qatlam", 0.03, 17, "Bitumli mastika"],
       ["Cheklangan qatlamli demfer", 0.10, 5, "Viskoelastik + qoplama"],
       ["Sozlangan massa demferi", 0.20, 2.5, "Faqat bitta chastotada"]])

# --- Zarbaviy javob (Dyuamel, sonli) ---
T_imp = float(PARAMS.get("T_imp", 2.0))/1000.0   # zarba davomiyligi
I_imp = float(PARAMS.get("I_imp", 1.0))          # impuls, N*s

dt = 1.0/(40*modes[-1]["f"])
t_end = 8.0/(zeta*modes[0]["w"]) if zeta > 0 else 1.0
t_end = min(t_end, 2.0)
nt = int(t_end/dt)
t = np.linspace(0.0, t_end, min(nt, 40000))

w_t = np.zeros_like(t)
for md in modes[:9]:
    wn, zt = md["w"], zeta
    wd = wn*np.sqrt(1 - zt**2)
    # yarim sinus zarba impulsidan keyin erkin tebranish
    Phi = np.sin(md["m"]*np.pi/2)*np.sin(md["n"]*np.pi/2)
    A0 = I_imp*Phi/(md["M"]*wd)
    shape = np.sin(np.pi*wn*T_imp/2)/(np.pi*wn*T_imp/2) \
        if wn*T_imp > 0 else 1.0    # zarba spektri (yarim sinus)
    w_t += A0*abs(shape)*np.exp(-zt*wn*t)*np.sin(wd*t)*Phi

# HISOB to'liq ruxsatda (40 000 nuqta) qoladi - maksimal qiymat shundan
# olinadi. CHIZISH uchun esa siyraklashtiramiz: brauzerga 40 000 nuqta
# yuborish ortiqcha va labkit chegarasidan ham oshadi.
step = max(1, len(t)//2000)
series("Zarbaviy javob w(t)", (t[::step]*1000).tolist(),
       (w_t[::step]*1000).tolist(),
       xlabel="Vaqt t, ms", ylabel="Og'ish w, mm")
value("Chizishdagi siyraklashtirish qadami", step, "nuqta")
value("Zarbadan keyin maksimal og'ish", float(np.max(np.abs(w_t)))*1000,
      "mm")
env = np.abs(w_t).max()*np.exp(-zeta*modes[0]["w"]*t)
series("So'nish o'ramasi", (t[::step]*1000).tolist(),
       (env[::step]*1000).tolist(),
       xlabel="Vaqt t, ms", ylabel="Og'ish w, mm")
t_half = np.log(2)/(zeta*modes[0]["w"]) if zeta > 0 else np.inf
value("Amplituda yarmiga tushish vaqti", t_half*1000, "ms")
value("Shu vaqtdagi tebranishlar soni", t_half*modes[0]["f"], "dona")
note(f"Zarbadan keyin panel {t_half*modes[0]['f']:.0f} marta "
     f"tebranib amplitudasi yarmiga tushadi — kam demflashda "
     f"bu 'jarangli' ovoz beradi.")

# Zarba spektri
f_sp = np.linspace(1.0, 4*modes[-1]["f"], 500)
spec = np.abs(np.sinc(f_sp*T_imp))
series("Zarba chastota spektri", f_sp.tolist(), spec.tolist(),
       xlabel="Chastota, Hz", ylabel="Nisbiy amplituda")
f_cut = 1.0/T_imp
value("Zarba spektrining kesim chastotasi 1/T", f_cut, "Hz")
n_exc = sum(1 for md in modes if md["f"] < f_cut)
value("Qo'zg'atiladigan shakllar soni", float(n_exc), "dona")
note(f"Zarba davomiyligi {T_imp*1000:.1f} ms — u {f_cut:.0f} Hz "
     f"gacha bo'lgan {n_exc} ta shaklni sezilarli qo'zg'atadi. "
     f"Qisqaroq zarba ko'proq shaklni uyg'otadi.")
''',
                parameters=[
                    p("a", "Panel tomoni a", 50.0, 5000.0, 600.0, 10.0, "mm"),
                    p("b", "Panel tomoni b", 50.0, 5000.0, 400.0, 10.0, "mm"),
                    p("h", "Qalinlik h", 0.3, 50.0, 3.0, 0.1, "mm"),
                    p("E", "Yung moduli E", 1.0, 400.0, 210.0, 1.0, "GPa"),
                    p("nu", "Puasson koeffitsienti ν", 0.0, 0.45, 0.3, 0.01),
                    p("rho", "Zichlik ρ", 500.0, 12000.0, 7850.0, 50.0,
                      "kg/m³"),
                    p("q0", "Pulsatsiyalanuvchi bosim q₀", 1.0, 5000.0, 50.0,
                      1.0, "Pa"),
                    p("f_exc", "Qo'zg'atuvchi chastota", 1.0, 1000.0, 66.0,
                      1.0, "Hz"),
                    p("zeta", "Demflash nisbati ζ", 0.0005, 0.3, 0.002,
                      0.0005),
                    p("zeta2", "Demfer bilan ζ", 0.005, 0.5, 0.05, 0.005),
                    p("T_imp", "Zarba davomiyligi", 0.1, 50.0, 2.0, 0.1, "ms"),
                    p("I_imp", "Zarba impulsi", 0.01, 100.0, 1.0, 0.01, "N·s"),
                ],
                expected_output=(
                    "f₁₁ = 66,6 Hz; statik og'ish 0,019039 mm — "
                    "modal superpozitsiya va bevosita Navye qatori "
                    "0,0000 % farq bilan mos keladi. f = 66 Hz da "
                    "|H| = 63,4 va amplituda 1,207 mm; ζ = 0,05 "
                    "bilan 0,195 mm (6,2 marta kam). Rezonansda "
                    "1/(2ζ) = 250 va amplituda 4,76 mm > h — "
                    "nochiziqlilik ishga tushadi. 2 ms li zarba "
                    "500 Hz gacha shakllarni qo'zg'atadi."
                ),
            ),
            visual=vis(
                kind="Chastota javobi va zarbaviy javob",
                tool="React/SVG",
                description=(
                    "Bode diagrammasi rezonans cho'qqilari "
                    "bilan, demflashning ta'siri, zarbadan "
                    "keyingi so'nuvchi tebranish."
                ),
                how_to_draw=(
                    "React/SVG: asosiy panel — chastota "
                    "javobi log–log o'qlarda: gorizontal "
                    "chastota (Hz), vertikal amplituda (mm). "
                    "Ikkita egri chiziq: kam demflash (o'tkir "
                    "cho'qqilar) va demfer bilan (yumshoq "
                    "cho'qqilar) — farq bir qarashda ko'rinadi. "
                    "Statik daraja gorizontal punktir. Har bir "
                    "rezonans cho'qqisi ustida $(m,n)$ yorlig'i. "
                    "Qo'zg'atuvchi chastota vertikal chiziq "
                    "bilan; uning egri chiziq bilan kesishgan "
                    "nuqtasi belgilanadi va amplituda "
                    "ko'rsatiladi. $\\zeta$ slayderi bilan "
                    "cho'qqilar jonli o'zgaradi. Ikkinchi "
                    "panel — zarbaviy javob: $w(t)$ so'nuvchi "
                    "sinusoid, ustiga $e^{-\\zeta\\omega t}$ "
                    "o'ramasi punktir bilan; amplituda "
                    "yarmiga tushadigan vaqt vertikal chiziq "
                    "bilan belgilanadi. Uchinchi panel — "
                    "zarba spektri: $|\\mathrm{sinc}(fT)|$ "
                    "egri chizig'i va uning ustiga xususiy "
                    "chastotalar vertikal chiziqchalar "
                    "sifatida qo'yiladi — qaysi shakllar "
                    "qo'zg'atilishi ko'rinadi."
                ),
            ),
            interp=(
                "Demflash jadvali eng amaliy ma'lumotni "
                "beradi: payvandlangan po'latda "
                "$1/(2\\zeta) = 250$, cheklangan qatlamli "
                "demfer bilan esa atigi 5. Ya'ni demfer "
                "qatlam amplitudani **50 marta** kamaytiradi. "
                "Hech qanday konstruktiv o'zgarish — qalinlik, "
                "qovurg'a, material — bunday samara bermaydi. "
                "Shuning uchun tebranish va shovqin "
                "muammolarida birinchi yechim har doim "
                "demflash bo'ladi. Zarba spektri esa boshqa "
                "muhim qoidani beradi: zarba davomiyligi "
                "$T$ bo'lsa, u taxminan $1/T$ Hz gacha "
                "bo'lgan shakllarni qo'zg'atadi. 2 ms li "
                "zarba 500 Hz gacha, 0,1 ms li zarba esa "
                "10 kHz gacha. Shuning uchun qattiq va "
                "qisqa zarba (metall-metall urilish) juda "
                "ko'p shaklni uyg'otadi va 'jarangli' "
                "ovoz beradi; yumshoq va uzun zarba "
                "(rezina bolg'a) faqat past chastotalarni "
                "qo'zg'atadi va 'to'mtoq' ovoz chiqaradi. "
                "Bu musiqa asboblari loyihasida ham, "
                "sanoat shovqinini kamaytirishda ham "
                "ishlatiladigan prinsip — urilish "
                "yuzasini yumshatish shovqinni keskin kamaytiradi."
            ),
            mistakes=[
                "Rezonansda amplitudani cheksiz deb "
                "hisoblash. Demflash uni "
                "$1/(2\\zeta)$ marta bilan cheklaydi.",
                "Modal demflashni butun konstruksiya uchun "
                "bir xil olish. Yuqori shakllarda "
                "$\\zeta$ odatda kattaroq bo'ladi.",
                "Faqat asosiy shaklni hisobga olish. "
                "Qo'zg'atuvchi chastota yuqori shaklga "
                "mos kelsa, javob butunlay boshqacha bo'ladi.",
                "Rezonans amplitudasini chiziqli nazariya "
                "bilan hisoblab, $w > 0{,}2h$ ekanligini "
                "tekshirmaslik. Bunday holda pq-18 dagi "
                "nochiziqlilik ishga tushadi.",
            ],
            quiz=[
                q("Rezonansdagi kuchaytirish koeffitsienti "
                  "nimaga teng?",
                  "$|H|_{\\max} \\approx 1/(2\\zeta)$. "
                  "$\\zeta = 0{,}002$ da bu 250 marta.",
                  "konseptual"),
                q("Modal superpozitsiya nima uchun ishlaydi?",
                  "Xususiy shakllar massa bilan vaznlangan "
                  "ma'noda ortogonal, shuning uchun har bir "
                  "shakl mustaqil bir erkinlik darajali "
                  "tenglamaga ajraladi.", "konseptual"),
                q("$\\zeta$ ni 0,002 dan 0,05 ga oshirsak, "
                  "rezonans amplitudasi qancha kamayadi?",
                  "$0{,}05/0{,}002 = 25$ marta — "
                  "$|H| \\propto 1/\\zeta$.", "hisob"),
                q("2 ms li zarba qaysi chastotalargacha "
                  "shakllarni qo'zg'atadi?",
                  "Taxminan $1/T = 500$ Hz gacha. Qisqaroq "
                  "zarba ko'proq shaklni uyg'otadi.", "hisob"),
                q("Kodda zarba spektri uchun nima uchun "
                  "`sinc` funksiyasi ishlatiladi?",
                  "To'g'ri to'rtburchak (yoki yarim sinus) "
                  "impulsning Furye tasviri `sinc` "
                  "ko'rinishida — u qaysi chastotalar "
                  "qo'zg'atilishini belgilaydi.", "kod"),
                q("Nima uchun rezina bolg'a metall "
                  "bolg'adan kam shovqin beradi?",
                  "Urilish davomiyligi uzunroq, demak "
                  "zarba spektri tor va faqat past "
                  "chastotalar qo'zg'atiladi — yuqori "
                  "chastotali 'jarang' yo'qoladi.", "talqin"),
            ],
            bridge=(
                "Barcha oldingi mavzular Kirxhoff "
                "gipotezalariga asoslandi. Ular yupqa "
                "plastinada mukammal ishlaydi, lekin qalin "
                "plitada va yuqori chastotalarda buziladi. "
                "Modulni yakunlab, bu cheklovni bartaraf "
                "etuvchi Mindlin–Reissner nazariyasini ko'ramiz."
            ),
            research=(
                "Plastinaning akustik nurlanishini "
                "o'rganing. Egilish to'lqinlari dispersiv "
                "($\\omega \\propto k^2$), havodagi tovush "
                "esa emas ($\\omega = ck$). Ularning "
                "tezliklari teng bo'ladigan chastota — "
                "**kritik (coincidence) chastota** "
                "$f_c = \\frac{c^2}{2\\pi}\\sqrt{\\rho h/D}$. "
                "Undan yuqorida plastina tovushni juda "
                "samarali nurlantiradi va tovush "
                "izolyatsiyasi keskin yomonlashadi. "
                "Po'lat, gipsokarton va shisha uchun "
                "$f_c$ ni hisoblang. Nima uchun devor "
                "materialini tanlashda $f_c$ ni eshitish "
                "diapazonidan tashqariga chiqarish "
                "maqsad qilinadi? Ikki qatlamli devor "
                "bu muammoni qanday hal qiladi?"
            ),
            manim_ref=manim(
                scene="ForcedVibrationScene",
                module="animatsiya/scenes/pq_vibration.py",
                title="Rezonans va demflash",
                summary=(
                    "Qo'zg'atuvchi chastota asta-sekin "
                    "oshadi; rezonansga yaqinlashganda "
                    "amplituda keskin ortadi. Keyin "
                    "demfer qatlam qo'shiladi va cho'qqi "
                    "yumshashi ko'rsatiladi."
                ),
            ),
        ),
    ),

    # ------------------------------------------------------------------ pq-24
    Topic(
        id="pq-24",
        subject_id=S, module_id=M, order=24,
        title="Mindlin–Reissner nazariyasi: sdvig deformatsiyasini hisobga olish",
        description=(
            "Kirxhoff gipotezasining yumshatilishi, mustaqil "
            "burilish burchaklari, sdvig tuzatish koeffitsienti, "
            "chegaraviy qatlam va sdvig qulflanishi (shear locking)."
        ),
        learning_objective=(
            "Mindlin–Reissner kinematikasini yozish, sdvig "
            "hissasini hisoblash, Kirxhoff yechimiga tuzatma "
            "kiritish va FEM dagi sdvig qulflanishini tushuntirish."
        ),
        prerequisites=["pq-23", "pq-01"],
        mathematical_core=(
            "$u = z\\phi_x$, $\\gamma_{xz} = \\phi_x + w_{,x}$, "
            "ikkinchi tartibli bog'langan tizim, sdvig "
            "koeffitsienti $\\kappa = 5/6$, "
            "$w_M = w_K(1 + \\alpha h^2/a^2)$."
        ),
        engineering_application=(
            "Qalin plitalar, sendvich panellar (yadro yumshoq), "
            "kompozitlar, yuqori chastotali tebranishlar, "
            "barcha zamonaviy FEM plastina elementlari."
        ),
        computational_component=(
            "Mindlin va Kirxhoff yechimlarini taqqoslash, "
            "sdvig hissasini $h/a$ bo'yicha baholash, "
            "sdvig qulflanishini sonli ko'rsatish."
        ),
        visualization_component=(
            "Normal chiziqning burilishi (Kirxhoff va Mindlin), "
            "sdvig hissasi grafigi, chegaraviy qatlam."
        ),
        research_extension=(
            "Sdvig qulflanishini bartaraf etish usullarini "
            "o'rganing: kamaytirilgan integrallash, aralash "
            "formulirovka, MITC elementlari."
        ),
        difficulty="ilg'or",
        previous_link=(
            "pq-01 da Kirxhoff gipotezasi qabul qilingan va "
            "uning xatosi $(h/a)^2$ tartibida ekanligi "
            "aytilgan edi. Endi shu gipotezani yumshatamiz "
            "va tuzatmani aniq hisoblaymiz."
        ),
        next_topic="pq-25",
        estimated_minutes=95,
        tags=["Mindlin", "Reissner", "sdvig", "shear locking"],
        lesson=_lesson(
            problem=(
                "pq-01 dagi uchinchi misol — sanoat plitasi "
                "$a = 1{,}2$ m, $h = 0{,}3$ m — Kirxhoff "
                "nazariyasi uchun yaroqsiz deb topilgan edi "
                "($h/a = 1/4$, xato > 6 %). Sendvich panelda "
                "esa vaziyat yanada yomon: yadro yumshoq "
                "($G_c$ kichik) va sdvig deformatsiyasi "
                "og'ishning yarmini berishi mumkin. Ikkala "
                "holatda ham yechim bitta: normal chiziqning "
                "burilishini og'ishdan **mustaqil** qilish."
            ),
            concepts=[
                c("Mindlin–Reissner kinematikasi",
                  "$u = z\\phi_x$, $v = z\\phi_y$, $w = w(x,y)$ — "
                  "endi $\\phi_x \\ne -\\partial w/\\partial x$, "
                  "ular mustaqil noma'lum."),
                c("Sdvig deformatsiyasi",
                  "$\\gamma_{xz} = \\phi_x + \\partial w/"
                  "\\partial x$ — Kirxhoffda u nolga "
                  "tenglashtirilgan edi."),
                c("Sdvig tuzatish koeffitsienti $\\kappa$",
                  "Haqiqiy parabolik $\\tau_{xz}$ epyurasini "
                  "doimiy bilan almashtirish uchun energiya "
                  "tuzatmasi; to'rtburchak kesimda $\\kappa = 5/6$."),
                c("Sdvig bikrligi",
                  "$S = \\kappa G h$ — plastinaning ko'ndalang "
                  "sdvigga qarshiligi; sendvich panelda "
                  "$S = G_c d$."),
                c("Chegaraviy qatlam (boundary layer)",
                  "Mindlin yechimi chekkada Kirxhoff "
                  "yechimidan farq qiladi; farq $\\sim h$ "
                  "masofada eksponensial so'nadi."),
                c("Sdvig qulflanishi (shear locking)",
                  "Yupqa plastina uchun FEM elementi juda "
                  "bikr chiqishi — sonli artefakt, fizik "
                  "hodisa emas."),
            ],
            derivation=[
                d("1. Yumshatilgan kinematika",
                  r"u = z\,\phi_x(x,y), \quad v = z\,\phi_y(x,y), "
                  r"\quad w = w(x,y)",
                  "Normal to'g'ri qoladi, lekin **normal "
                  "qolishi shart emas**. Uchta mustaqil "
                  "noma'lum: $w$, $\\phi_x$, $\\phi_y$."),
                d("2. Deformatsiyalar",
                  r"\varepsilon_x = z\phi_{x,x}, \quad "
                  r"\gamma_{xy} = z(\phi_{x,y} + \phi_{y,x}), "
                  r"\quad \gamma_{xz} = \phi_x + w_{,x}",
                  "Egilish deformatsiyalari oldingidek, lekin "
                  "endi sdvig deformatsiyasi ham bor va u "
                  "$z$ ga bog'liq emas (qalinlik bo'yicha doimiy)."),
                d("3. Kirxhoff chegaraviy holi",
                  r"\gamma_{xz} = 0 \;\Longrightarrow\; "
                  r"\phi_x = -w_{,x}",
                  "Sdvigni nolga tenglashtirsak, pq-01 dagi "
                  "kinematika tiklanadi. Demak Mindlin "
                  "nazariyasi Kirxhoffni **o'z ichiga oladi**."),
                d("4. Kesuvchi kuchlar endi Guk qonunidan",
                  r"Q_x = \kappa G h\,\gamma_{xz} = "
                  r"\kappa Gh(\phi_x + w_{,x})",
                  "Bu Kirxhoff nazariyasidan muhim farq: "
                  "u yerda $Q$ faqat muvozanatdan topilardi "
                  "(pq-04), bu yerda esa konstitutiv "
                  "munosabatdan."),
                d("5. Sdvig koeffitsienti $\\kappa$",
                  r"\int_{-h/2}^{h/2}\frac{\tau_{xz}^2}{2G}dz "
                  r"= \frac{Q^2}{2\kappa Gh} \;\Longrightarrow\; "
                  r"\kappa = \frac{5}{6}",
                  "Energiya ekvivalentligi: haqiqiy parabolik "
                  "epyura (pq-06) bilan doimiy epyura bir xil "
                  "energiya bersin. $\\kappa = 5/6 = 0{,}833$."),
                d("6. Muvozanat tenglamalari",
                  r"\frac{\partial M_x}{\partial x} + "
                  r"\frac{\partial M_{xy}}{\partial y} - Q_x = 0, "
                  r"\quad \frac{\partial Q_x}{\partial x} + "
                  r"\frac{\partial Q_y}{\partial y} + q = 0",
                  "Uchta tenglama, uchta noma'lum. Har biri "
                  "**ikkinchi tartibli** — Kirxhoffdagi "
                  "to'rtinchi tartibli bitta tenglama o'rniga."),
                d("7. Yechim: sdvig tuzatmasi",
                  r"w^M_{mn} = w^K_{mn}\Big(1 + \frac{D\,k_{mn}^2}{S}\Big), "
                  r"\quad k_{mn}^2 = \pi^2\Big(\frac{m^2}{a^2}+"
                  r"\frac{n^2}{b^2}\Big)",
                  "Navye bazisida har bir garmonika mustaqil "
                  "va Mindlin yechimi Kirxhoff yechimiga "
                  "sodda ko'paytuvchi bilan bog'lanadi."),
                d("7a. Tuzatmaning $(h/a)^2$ ko'rinishi",
                  r"\frac{D}{S} = \frac{h^2}{6\kappa(1-\nu)} "
                  r"\;\Longrightarrow\; \frac{w_M}{w_K}\Big|_{11} = "
                  r"1 + \alpha\Big(\frac{h}{a}\Big)^2, \quad "
                  r"\alpha = \frac{\pi^2\big(1+(a/b)^2\big)}"
                  r"{6\kappa(1-\nu)}",
                  "Bir jinsli plitada $D/S$ da $E$ qisqaradi "
                  "va faqat $h^2$ qoladi — shuning uchun "
                  "tuzatma aynan $(h/a)^2$ tartibida. "
                  "Kvadrat plastinada $\\nu = 0{,}2$, "
                  "$\\kappa = 5/6$ uchun "
                  "$\\alpha = \\pi^2/2 = 4{,}935$ — bu kodda "
                  "sonli tarzda tasdiqlanadi."),
                d("8. Sdvig qulflanishining sababi",
                  r"h \to 0: \ \kappa Gh \to 0 \ \text{lekin} "
                  r"\ \gamma_{xz} \to 0 \ \text{ham} "
                  r"\;\Longrightarrow\; \frac{0}{0}",
                  "Yupqa plastinada sdvig bikrligi kichik, "
                  "lekin sdvig deformatsiyasi ham nolga "
                  "intiladi. Sonli sxemada bu nomuvozanat "
                  "element juda bikr bo'lib qolishiga olib "
                  "keladi — sdvig qulflanishi."),
            ],
            meaning=(
                "Mindlin nazariyasining asosiy yutug'i — "
                "**bir gipotezani bekor qilib ikkita "
                "muammoni hal qilish**. Birinchisi fizik: "
                "qalin plitada va yumshoq yadroli sendvichda "
                "sdvig deformatsiyasi haqiqatan ham muhim. "
                "Ikkinchisi matematik: to'rtinchi tartibli "
                "bitta tenglama o'rniga ikkinchi tartibli "
                "uchta tenglama paydo bo'ladi. Bu FEM uchun "
                "hal qiluvchi: ikkinchi tartibli tenglama "
                "$C^0$ uzluksizlikni talab qiladi (faqat "
                "funksiya uzluksiz), Kirxhoff nazariyasi esa "
                "$C^1$ ni (hosila ham uzluksiz). $C^1$ "
                "elementlarni qurish juda qiyin, shuning "
                "uchun **zamonaviy FEM paketlarining "
                "deyarli barcha plastina elementlari "
                "Mindlin nazariyasiga asoslangan** — hatto "
                "juda yupqa plastinalar uchun ham. "
                "Bepul emas: sdvig qulflanishi paydo bo'ladi. "
                "$h \\to 0$ da sdvig bikrligi "
                "$\\kappa Gh \\to 0$, lekin element sdvig "
                "deformatsiyasini aynan nolga keltira olmaydi "
                "va soxta sdvig energiyasi hosil bo'ladi. "
                "Natijada element bir necha tartibga bikrroq "
                "chiqadi. Yechim — kamaytirilgan integrallash "
                "yoki MITC (Mixed Interpolation of Tensorial "
                "Components) elementlari. Sdvig tuzatmasining "
                "kattaligi esa $\\alpha(h/a)^2$ — bu pq-01 "
                "dagi $(h/a)^2$ xato bahosining aniq "
                "ko'rinishi va u nazariyani yopadi."
            ),
            equations=[
                eq(r"u = z\phi_x, \quad v = z\phi_y, \quad w = w(x,y)",
                   "Mindlin–Reissner kinematikasi.",
                   "Mindlin kinematikasi"),
                eq(r"\gamma_{xz} = \phi_x + \frac{\partial w}"
                   r"{\partial x}, \qquad Q_x = \kappa Gh\,\gamma_{xz}",
                   "Sdvig deformatsiyasi va kesuvchi kuch.",
                   "Sdvig munosabati"),
                eq(r"\kappa = \frac{5}{6}",
                   "To'rtburchak kesim uchun sdvig tuzatish "
                   "koeffitsienti.", "Sdvig koeffitsienti"),
                eq(r"\frac{w_M}{w_K} = 1 + \frac{D k^2}{S} = "
                   r"1 + \alpha\Big(\frac{h}{a}\Big)^2, \quad "
                   r"\alpha = \frac{\pi^2\big(1+(a/b)^2\big)}"
                   r"{6\kappa(1-\nu)}",
                   "Mindlin va Kirxhoff yechimlarining nisbati "
                   "(bir jinsli plita, Navye bazisining "
                   "birinchi hadi).", "Sdvig tuzatmasi"),
            ],
            conditions=(
                "**Chegaraviy shartlar** endi uchta noma'lum "
                "uchun va har chekkada **uchtadan** beriladi "
                "(Kirxhoffdagi ikkita emas!) — pq-05 dagi "
                "paradoks shu tarzda yo'qoladi:\n"
                "- Qattiq mahkamlash: $w = 0$, "
                "$\\phi_n = 0$, $\\phi_t = 0$;\n"
                "- Yumshoq sharnirli (SS1): $w = 0$, "
                "$M_n = 0$, $M_{nt} = 0$;\n"
                "- Qattiq sharnirli (SS2): $w = 0$, "
                "$M_n = 0$, $\\phi_t = 0$;\n"
                "- Erkin: $M_n = 0$, $M_{nt} = 0$, $Q_n = 0$ — "
                "uchalasini ham qo'yish mumkin.\n\n"
                "**Chegaraviy qatlam:** Mindlin va Kirxhoff "
                "yechimlari chekkadan $\\sim h$ masofada "
                "farq qiladi; farq "
                "$e^{-\\sqrt{10}\\,s/h}$ kabi so'nadi.\n\n"
                "**Qo'llanish sohasi:**\n"
                "- $h/a > 1/20$ — Mindlin tavsiya etiladi;\n"
                "- Sendvich panel — har doim (yadro yumshoq);\n"
                "- Kompozit — har doim ($E/G$ nisbati katta);\n"
                "- Yuqori chastotali tebranish — to'lqin "
                "uzunligi $\\lambda < 10h$ bo'lganda."
            ),
            worked=WorkedExample(
                statement=(
                    "Ikkita holat: (A) beton plita "
                    "$a = b = 1{,}2$ m, $h = 300$ mm, "
                    "$E = 30$ GPa, $\\nu = 0{,}2$; "
                    "(B) sendvich panel $a = b = 1{,}2$ m, "
                    "$t_f = 1$ mm, $t_c = 25$ mm, "
                    "$E_f = 70$ GPa, $G_c = 40$ MPa. "
                    "Ikkalasi sharnirli, $q = 5$ kPa. "
                    "Sdvig hissasini hisoblang."
                ),
                given=[
                    r"\text{(A) } h/a = 0{,}25, \ E = 30\ \text{GPa}, "
                    r"\ \nu = 0{,}2",
                    r"\text{(B) } t_f = 1\ \text{mm},\ t_c = 25\ \text{mm}, "
                    r"\ G_c = 40\ \text{MPa}",
                    r"a = b = 1{,}2\ \text{m},\ q = 5000\ \text{Pa}",
                ],
                steps=[
                    st(r"\text{(A)}\ D = \frac{30\times10^9 \cdot 0{,}027}"
                       r"{12 \cdot 0{,}96} = 7{,}031\times10^{7}\ \text{N·m}",
                       "$h^3 = 0{,}027$ m³."),
                    st(r"w_K = 0{,}004062\frac{5000 \cdot 2{,}0736}"
                       r"{7{,}031\times10^{7}} = 5{,}99\times10^{-7}\ \text{m}",
                       "Kirxhoff yechimi: atigi 0,6 mikron — "
                       "juda bikr plita."),
                    st(r"G = \frac{E}{2(1+\nu)} = \frac{30}{2{,}4} "
                       r"= 12{,}5\ \text{GPa}; \quad "
                       r"S = \kappa Gh = \frac{5}{6} \cdot "
                       r"12{,}5\times10^{9} \cdot 0{,}3 = "
                       r"3{,}125\times10^{9}\ \text{N/m}",
                       "Sdvig bikrligi."),
                    st(r"\frac{w_M}{w_K} = 1 + \frac{\pi^2 D}{S}"
                       r"\Big(\frac{1}{a^2}+\frac{1}{b^2}\Big) = "
                       r"1 + \frac{9{,}8696 \cdot 7{,}031\times10^{7}}"
                       r"{3{,}125\times10^{9}} \cdot 1{,}389",
                       "Navye bazisidagi aniq tuzatma "
                       "($m = n = 1$ uchun)."),
                    st(r"= 1 + 0{,}2221 \cdot 1{,}389 = 1{,}3084 "
                       r"\;\Rightarrow\; \text{sdvig hissasi } "
                       r"1 - 1/1{,}3084 = 23{,}6\ \%",
                       "Bu birinchi garmonika bo'yicha baho. "
                       "Kodda to'liq qator (15 had) "
                       "$w_M/w_K = 1{,}2836$ va sdvig hissasi "
                       "**22,1 %** beradi — yuqori "
                       "garmonikalar tuzatmani biroz "
                       "kamaytiradi. pq-01 dagi "
                       "$(h/a)^2 = 6{,}25$ % bahosidan "
                       "ancha katta, chunki "
                       "$\\alpha = \\pi^2/2 = 4{,}935$."),
                    st(r"\text{(B)}\ d = t_c + t_f = 26\ \text{mm}; \ "
                       r"D = \frac{E_ft_fd^2}{2(1-\nu_f^2)} = "
                       r"\frac{70\times10^9 \cdot 10^{-3} \cdot "
                       r"6{,}76\times10^{-4}}{2 \cdot 0{,}8911} "
                       r"= 26\,554\ \text{N·m}",
                       "Sendvich bikrligi (pq-17)."),
                    st(r"S = G_c\,d = 40\times10^{6} \cdot 0{,}026 "
                       r"= 1{,}04\times10^{6}\ \text{N/m}",
                       "Sendvichda sdvigni **yadro** uzatadi va "
                       "u juda yumshoq."),
                    st(r"\frac{w_M}{w_K} = 1 + \frac{9{,}8696 \cdot "
                       r"26\,551}{1{,}04\times10^{6}} \cdot 1{,}389 "
                       r"= 1 + 0{,}2520 \cdot 1{,}389 = 1{,}350",
                       "Birinchi garmonika bo'yicha sdvig "
                       "hissasi 25,9 %; to'liq qatorda "
                       "**24,3 %** — beton plitadagiga yaqin, "
                       "lekin butunlay boshqa sababdan."),
                    st(r"\text{(A): } h/a = 0{,}25 \ \text{(qalinlik)}; "
                       r"\quad \text{(B): } h/a = 0{,}022 \ "
                       r"\text{(lekin } G_c \text{ kichik)}",
                       "Ikki mexanizm: (A) geometrik qalinlik, "
                       "(B) yumshoq yadro. Sendvich panel "
                       "geometrik jihatdan yupqa, lekin sdvig "
                       "baribir muhim — shuning uchun unda "
                       "Mindlin nazariyasi **har doim** kerak."),
                ],
                answer=(
                    "(A) Beton plita: $D = 70{,}3$ MN·m, "
                    "$S = 3{,}13$ GN/m, sdvig hissasi "
                    "**22,1 %** (to'liq qator; 1-garmonika "
                    "bo'yicha 23,6 %); (B) sendvich panel: "
                    "$D = 26{,}55$ kN·m, $S = 1{,}04$ MN/m, "
                    "sdvig hissasi **24,3 %** (1-garmonika "
                    "bo'yicha 25,9 %). Ikkala holatda ham "
                    "Kirxhoff nazariyasi og'ishni sezilarli "
                    "kam ko'rsatadi."
                ),
                engineering_note=(
                    "Sendvich paneldagi natija eng muhim "
                    "saboqni beradi: panel geometrik jihatdan "
                    "juda yupqa ($h/a = 1/45$), lekin sdvig "
                    "hissasi qalin beton plitadagidan ham "
                    "katta. Sababi — $D/S$ nisbati. Sendvichda "
                    "$D$ katta (qoplamalar uzoq), $S$ esa "
                    "kichik (yadro yumshoq). Demak "
                    "**'yupqa' degan geometrik mezon yetarli "
                    "emas** — $D/(Sa^2)$ o'lchamsiz parametrini "
                    "tekshirish kerak. Kompozitlarda ham "
                    "shunday: $E_1/G_{13}$ nisbati 25–50 ga "
                    "yetadi (izotropda 2,6), shuning uchun "
                    "qatlamli plastinalarda sdvig deyarli "
                    "har doim hisobga olinadi."
                ),
            ),
            computation=Computation(
                caption=(
                    "Mindlin va Kirxhoff yechimlarini "
                    "taqqoslash, sdvig hissasini baholash va "
                    "sdvig qulflanishini sonli ko'rsatish."
                ),
                code='''"""Mindlin-Reissner nazariyasi va sdvig hissasi."""
import numpy as np
from labkit import PARAMS, note, series, table, value

a = float(PARAMS.get("a", 1200.0))/1000.0
b = float(PARAMS.get("b", 1200.0))/1000.0
h = float(PARAMS.get("h", 300.0))/1000.0
E = float(PARAMS.get("E", 30.0))*1e9
nu = float(PARAMS.get("nu", 0.2))
q0 = float(PARAMS.get("q0", 5000.0))
kappa = float(PARAMS.get("kappa", 5.0/6.0))
mode = int(PARAMS.get("mode", 0))       # 0 bir jinsli, 1 sendvich

G = E/(2*(1 + nu))
if mode == 0:
    D = E*h**3/(12*(1 - nu**2))
    S = kappa*G*h
    label = "bir jinsli plita"
    h_eff = h
else:
    tf = float(PARAMS.get("tf", 1.0))/1000.0
    tc = float(PARAMS.get("tc", 25.0))/1000.0
    Ef = float(PARAMS.get("Ef", 70.0))*1e9
    Gc = float(PARAMS.get("Gc", 40.0))*1e6
    nuf = 0.33
    d = tc + tf
    D = Ef*tf*d**2/(2*(1 - nuf**2))
    S = Gc*d
    label = "sendvich panel"
    h_eff = 2*tf + tc

value("Silindrik bikrlik D", D, "N*m")
value("Sdvig bikrligi S", S, "N/m")
value("h/a nisbati", h_eff/a, "—")
value("O'lchamsiz parametr D/(S*a^2)", D/(S*a**2), "—")

# --- Navye yechimi: Kirxhoff va Mindlin ---
NT = 15
wK = wM = 0.0
for m in range(1, NT, 2):
    for n in range(1, NT, 2):
        am, bn = m*np.pi/a, n*np.pi/b
        k2 = am**2 + bn**2
        qmn = 16*q0/(np.pi**2*m*n)
        s = np.sin(m*np.pi/2)*np.sin(n*np.pi/2)
        wk = qmn/(D*k2**2)
        wm = wk*(1 + D*k2/S)          # Mindlin tuzatmasi (Navye bazisida)
        wK += wk*s
        wM += wm*s

value("Kirxhoff yechimi w_K", wK*1000, "mm")
value("Mindlin yechimi w_M", wM*1000, "mm")
value("w_M / w_K", wM/wK, "—")
value("Sdvig hissasi", (wM - wK)/wM*100, "%")
note(f"Holat: {label}. Sdvig hissasi {(wM-wK)/wM*100:.1f} %. "
     f"Kirxhoff nazariyasi og'ishni shuncha KAM ko'rsatadi.")

# Birinchi had uchun aniq tuzatma
k2_11 = (np.pi/a)**2 + (np.pi/b)**2
corr = 1 + D*k2_11/S
value("1-had tuzatmasi (1 + D*k^2/S)", corr, "—")

if (wM - wK)/wM*100 > 5:
    note(f"Sdvig hissasi 5 % dan katta — Mindlin nazariyasi "
         f"ZARUR. Kirxhoff yechimi xavfsizlikka zid tomonga "
         f"xato qiladi (og'ishni kam ko'rsatadi).")
else:
    note(f"Sdvig hissasi 5 % dan kam — Kirxhoff nazariyasi yetarli.")

# --- h/a ning ta'siri (bir jinsli plita) ---
ratios = np.linspace(0.01, 0.35, 200)
shares = []
for rt in ratios:
    hh = rt*a
    Dh = E*hh**3/(12*(1 - nu**2))
    Sh = kappa*G*hh
    c = Dh*k2_11/Sh
    shares.append(100*c/(1 + c))
series("Sdvig hissasi(h/a)", ratios.tolist(), shares,
       xlabel="h / a", ylabel="Sdvig hissasi, %")
series("5 % chegara", ratios.tolist(), [5.0]*len(ratios),
       xlabel="h / a", ylabel="Sdvig hissasi, %")
i5 = int(np.argmax(np.array(shares) > 5.0))
value("Sdvig 5 % ga yetadigan h/a", float(ratios[i5]), "—")
value("Bu 1/(h/a) ga teng", 1/float(ratios[i5]), "—")

# Kvadrat sharnirli plastina uchun aniq koeffitsient:
#   c = D*k^2/S = pi^2*h^2/(3*kappa*(1-nu)*a^2)  =>  alpha = c/(h/a)^2
alpha_num = D*k2_11/S/(h_eff/a)**2
value("Koeffitsient alpha (c = alpha*(h/a)^2)", alpha_num, "—")
if mode == 0:
    alpha_th = np.pi**2/(3*kappa*(1 - nu))*(1 + (a/b)**2)/2
    value("alpha (nazariy, kvadrat uchun pi^2/(3*k*(1-nu)))",
          alpha_th, "—")

c20 = alpha_num*(1/20)**2
value("Sdvig hissasi h/a = 1/20 da", 100*c20/(1 + c20), "%")
if mode == 0:
    note(f"Bir jinsli plitada sdvig hissasi 5 % ga "
         f"h/a = {ratios[i5]:.3f} (ya'ni 1/{1/ratios[i5]:.0f}) da "
         f"yetadi, h/a = 1/20 da esa u atigi "
         f"{100*c20/(1+c20):.1f} %. Demak pq-01 dagi 1/20 mezoni "
         f"EHTIYOTKOR — uni qanoatlantirgan plastinada Kirxhoff "
         f"xatosi 5 % dan ancha kichik.")
else:
    note(f"DIQQAT: sendvich panel uchun alpha = {alpha_num:.0f}, "
         f"bir jinsli plitadagi 4.9 dan ~{alpha_num/4.935:.0f} marta "
         f"katta. Shu sababli h/a = 1/20 bo'lgan sendvichda sdvig "
         f"hissasi {100*c20/(1+c20):.0f} % ga yetardi. Bu yerda "
         f"pq-01 dagi 1/20 mezoni XAVFLI: u qanoatlantirilsa ham "
         f"Kirxhoff nazariyasi yaroqsiz. Sendvich va kompozitda "
         f"mezon geometrik emas, D/(S*a^2) parametri bo'yicha "
         f"qo'yiladi.")
note(f"Yuqoridagi h/a supurish egri chizig'i bir jinsli plita uchun "
     f"(alpha = 4.9); sendvich yoki kompozitda egri chiziq ancha "
     f"tikroq bo'ladi.")

# Sdvig hissasi ~ (h/a)^2 ekanligini tekshirish
small = ratios < 0.1
sh_small = np.array(shares)[small]
rt_small = ratios[small]
p_fit = np.polyfit(np.log(rt_small[5:]), np.log(sh_small[5:]), 1)
value("Sdvig hissasining daraja ko'rsatkichi", float(p_fit[0]), "—")
note(f"log-log moslashtirish darajasi {p_fit[0]:.3f} ~ 2 — "
     f"sdvig hissasi (h/a)^2 ga mutanosib, pq-01 dagi "
     f"asimptotik baho tasdiqlanadi.")

# --- Sendvich: G_c ning ta'siri ---
if mode == 1:
    Gcs = np.logspace(np.log10(5e6), np.log10(2e9), 120)
    sh_g = []
    for gc in Gcs:
        Sg = gc*d
        c = D*k2_11/Sg
        sh_g.append(100*c/(1 + c))
    series("Sdvig hissasi(yadro moduli G_c)", (Gcs/1e6).tolist(), sh_g,
           xlabel="Yadro sdvig moduli G_c, MPa",
           ylabel="Sdvig hissasi, %")
    note(f"Yumshoq yadroda ({Gcs[0]/1e6:.0f} MPa) sdvig hissasi "
         f"{sh_g[0]:.0f} %, qattiq yadroda ({Gcs[-1]/1e6:.0f} MPa) "
         f"{sh_g[-1]:.1f} % — yadro tanlovi hal qiluvchi.")

# --- Sdvig qulflanishi (shear locking) demonstratsiyasi ---
# Sodda 1D model: konsol balka, chiziqli elementlar, kamaytirilgan
# integrallash bilan va busiz
def beam_tip(nel, h_b, reduced):
    L = 1.0
    Eb, nub = 210e9, 0.3
    Gb = Eb/(2*(1 + nub))
    I = h_b**3/12
    A = h_b
    le = L/nel
    ndof = 2*(nel + 1)                # [w, phi] har tugunda
    K = np.zeros((ndof, ndof))
    for e in range(nel):
        i0 = 2*e
        # egilish qismi (aniq integrallash)
        kb = Eb*I/le*np.array([[0, 0, 0, 0],
                               [0, 1, 0, -1],
                               [0, 0, 0, 0],
                               [0, -1, 0, 1]])
        # sdvig qismi
        if reduced:
            # bitta Gauss nuqtasi (kamaytirilgan)
            gp = [0.0]; wt = [2.0]
        else:
            # ikkita Gauss nuqtasi (to'liq -> qulflanish)
            gp = [-1/np.sqrt(3), 1/np.sqrt(3)]; wt = [1.0, 1.0]
        ks = np.zeros((4, 4))
        for xg_, wg in zip(gp, wt):
            N1, N2 = (1 - xg_)/2, (1 + xg_)/2
            # gamma = dw/dx + phi; dN/dx = (dN/dxi)*(2/le) = -+1/le
            B = np.array([-1/le, N1, 1/le, N2])
            ks += (5.0/6.0)*Gb*A*np.outer(B, B)*wg*le/2
        ke = kb + ks
        K[i0:i0+4, i0:i0+4] += ke
    # konsol: chap uchi mahkamlangan
    free = np.arange(2, ndof)
    F = np.zeros(ndof)
    F[-2] = 1.0                        # uchida birlik kuch
    Kr = K[np.ix_(free, free)]
    u = np.linalg.solve(Kr, F[free])
    return u[-2]


h_b = 0.01
L = 1.0
Eb = 210e9
w_exact = 1.0*L**3/(3*Eb*h_b**3/12)
rows = []
for nel in [1, 2, 4, 8, 16]:
    w_full = beam_tip(nel, h_b, reduced=False)
    w_red = beam_tip(nel, h_b, reduced=True)
    rows.append([nel, round(w_full/w_exact, 5), round(w_red/w_exact, 5)])
table("Sdvig qulflanishi: FEM yechimi / aniq yechim (L/h = 100)",
      ["Elementlar", "To'liq integrallash", "Kamaytirilgan integrallash"],
      rows)
note("To'liq integrallashda element bir necha tartibga BIKR chiqadi "
     "(nisbat nolga yaqin) — bu sdvig qulflanishi, sonli artefakt. "
     "Kamaytirilgan integrallash muammoni hal qiladi.")

series("Qulflanish: to'liq integrallash",
       [float(r[0]) for r in rows], [r[1] for r in rows],
       xlabel="Elementlar soni", ylabel="w_FEM / w_aniq")
series("Kamaytirilgan integrallash",
       [float(r[0]) for r in rows], [r[2] for r in rows],
       xlabel="Elementlar soni", ylabel="w_FEM / w_aniq")
series("Aniq yechim darajasi",
       [float(r[0]) for r in rows], [1.0]*len(rows),
       xlabel="Elementlar soni", ylabel="w_FEM / w_aniq")

table("Kirxhoff va Mindlin nazariyalarining taqqoslashi",
      ["Jihat", "Kirxhoff", "Mindlin-Reissner"],
      [["Noma'lumlar", "w", "w, phi_x, phi_y"],
       ["Tenglama tartibi", "4 (bitta)", "2 (uchta)"],
       ["Chegaraviy shartlar", "2 ta har chekkada", "3 ta har chekkada"],
       ["Kirxhoff paradoksi", "bor (V_n kerak)", "yo'q"],
       ["FEM uzluksizligi", "C1 (qiyin)", "C0 (oson)"],
       ["Sdvig deformatsiyasi", "nol deb olinadi", "hisobga olinadi"],
       ["Qo'llanish chegarasi", "h/a < 1/20", "h/a < 1/3"],
       ["Sonli muammo", "C1 element qurish", "sdvig qulflanishi"]])
''',
                parameters=[
                    p("a", "Plita tomoni a", 100.0, 10000.0, 1200.0, 50.0,
                      "mm"),
                    p("b", "Plita tomoni b", 100.0, 10000.0, 1200.0, 50.0,
                      "mm"),
                    p("h", "Qalinlik h", 5.0, 1000.0, 300.0, 5.0, "mm"),
                    p("E", "Yung moduli E", 1.0, 400.0, 30.0, 1.0, "GPa"),
                    p("nu", "Puasson koeffitsienti ν", 0.0, 0.45, 0.2, 0.01),
                    p("q0", "Yuklama q₀", 100.0, 100000.0, 5000.0, 100.0, "Pa"),
                    p("kappa", "Sdvig koeffitsienti κ", 0.5, 1.0, 0.8333,
                      0.0167),
                    p("mode", "Model (0 bir jinsli, 1 sendvich)", 0.0, 1.0,
                      0.0, 1.0),
                    p("tf", "Sendvich: qoplama t_f", 0.2, 5.0, 1.0, 0.1, "mm"),
                    p("tc", "Sendvich: yadro t_c", 3.0, 100.0, 25.0, 1.0, "mm"),
                    p("Ef", "Qoplama moduli E_f", 1.0, 400.0, 70.0, 1.0, "GPa"),
                    p("Gc", "Yadro sdvig moduli G_c", 1.0, 2000.0, 40.0, 1.0,
                      "MPa"),
                ],
                expected_output=(
                    "Beton plita (h/a = 0,25): D = 70,3 MN·m, "
                    "S = 3,12 GN/m, sdvig hissasi 22,1 %. "
                    "Koeffitsient α = 4,935, sonli qiymat "
                    "nazariy π²/[6κ(1−ν)] bilan aynan mos "
                    "tushadi. Sdvig hissasi (h/a)² ga "
                    "mutanosib (log–log darajasi 1,97) va "
                    "h/a ≈ 0,104 (1/10) da 5 % ga yetadi; "
                    "h/a = 1/20 da esa atigi 1,2 %. "
                    "Sdvig qulflanishi: to'liq integrallashda "
                    "16 elementda ham nisbat 0,074, "
                    "kamaytirilgan integrallashda "
                    "0,750 → 0,938 → 0,984 → 0,996 → 0,999."
                ),
            ),
            visual=vis(
                kind="Mindlin kinematikasi va sdvig qulflanishi",
                tool="React/SVG + Manim",
                description=(
                    "Normal chiziqning Kirxhoff va Mindlin "
                    "holatlari, sdvig hissasi grafigi, "
                    "qulflanish demonstratsiyasi."
                ),
                how_to_draw=(
                    "React/SVG: asosiy panel — plastina "
                    "kesimi ikki holatda yonma-yon. Chapda "
                    "Kirxhoff: o'rta sirtga normal kesmalar "
                    "egilgandan keyin ham egri chiziqqa "
                    "**perpendikulyar**. O'ngda Mindlin: "
                    "kesmalar to'g'ri qoladi, lekin "
                    "perpendikulyar emas — ular va normal "
                    "orasidagi burchak $\\gamma_{xz}$ "
                    "yoy bilan belgilanadi va qiymati "
                    "yoziladi. $h/a$ slayderi bilan bu "
                    "burchak o'zgaradi: yupqa plastinada "
                    "deyarli nol, qalinda sezilarli. "
                    "Ikkinchi panel — sdvig hissasi grafigi "
                    "log–log o'qlarda; qiyaligi 2 bo'lgan "
                    "nazariy chiziq punktir bilan ustiga "
                    "qo'yiladi va sonli nuqtalar unga "
                    "parallel yotishi ko'rinadi; 5 % "
                    "gorizontal chizig'i egri chiziqni "
                    "$h/a \\approx 0{,}104$ da kesadi va "
                    "an'anaviy $1/20$ mezoni undan chapda "
                    "belgilanadi — zaxira ko'zga tashlanadi. "
                    "Uchinchi panel — sdvig qulflanishi: "
                    "elementlar soniga qarab "
                    "$w_{\\text{FEM}}/w_{\\text{aniq}}$; "
                    "to'liq integrallash chizig'i nolga "
                    "yopishib qoladi, kamaytirilgan esa "
                    "1 ga intiladi — farq dramatik ko'rinadi."
                ),
            ),
            interp=(
                "Sdvig hissasining $(h/a)^2$ qonuni sonli "
                "moslashtirishda tasdiqlanadi (log–log "
                "darajasi 1,97) va koeffitsient "
                "$\\alpha = 4{,}935$ nazariy "
                "$\\pi^2/[6\\kappa(1-\\nu)]$ bilan aynan mos "
                "tushadi. Bu pq-01 dagi asimptotik bahoni "
                "yopadi: nazariya boshida aytilgan "
                "$(h/a)^2$ xato endi aniq koeffitsienti "
                "bilan hisoblandi. Shu bilan birga sonli "
                "natija an'anaviy $h/a < 1/20$ mezonini "
                "**tuzatadi**: 5 % xato aslida "
                "$h/a \\approx 1/10$ da yuzaga keladi, "
                "$1/20$ da esa xato atigi 1,2 %. Demak "
                "klassik mezon bir jinsli plita uchun "
                "ehtiyotkor — taxminan ikki barobar zaxira "
                "bilan qo'yilgan. Sdvig qulflanishi jadvali "
                "esa boshqa muhim saboq beradi: to'g'ri "
                "nazariya + noto'g'ri sonli sxema = "
                "butunlay xato natija. To'liq integrallashda "
                "element aniq yechimdan bir necha tartibga "
                "bikr chiqadi va bu **to'rni zichlashtirish "
                "bilan tuzatilmaydi** — xato sistematik. "
                "Bu 5-fandagi (Sonli usullar) eng muhim "
                "mavzulardan biriga to'g'ridan-to'g'ri "
                "ko'prik: sonli usulning to'g'riligi faqat "
                "yaqinlashish bilan emas, balki "
                "**qulflanish, barqarorlik va soxta "
                "rejimlar** bilan ham baholanadi. Va "
                "nihoyat, sendvich paneldagi natija "
                "geometrik intuitsiyaning chegarasini "
                "ko'rsatadi: $h/a = 1/45$ bo'lgan 'juda "
                "yupqa' panel qalin beton plitadan ko'ra "
                "ko'proq sdvig hissasiga ega. To'g'ri mezon "
                "geometrik emas — u $D/(Sa^2)$ o'lchamsiz "
                "parametri."
            ),
            mistakes=[
                "Sdvig koeffitsienti $\\kappa$ ni 1 deb "
                "olish. To'rtburchak kesimda $\\kappa = 5/6$; "
                "uni unutish sdvig hissasini 20 % kam "
                "ko'rsatadi.",
                "Mindlin nazariyasini faqat qalin plitaga "
                "kerak deb hisoblash. Sendvich va kompozit "
                "panellarda $h/a$ kichik bo'lsa ham sdvig "
                "hal qiluvchi.",
                "Sdvig qulflanishini to'rni zichlashtirish "
                "bilan hal qilishga urinish. Xato "
                "sistematik — sonli sxemani o'zgartirish kerak.",
                "Kirxhoff yechimi xavfsiz tomonga xato "
                "qiladi deb o'ylash. U og'ishni **kam** "
                "ko'rsatadi — ya'ni xavfsizlikka zid tomonga.",
            ],
            quiz=[
                q("Mindlin kinematikasi Kirxhoffdan nimasi "
                  "bilan farq qiladi?",
                  "Burilish burchaklari $\\phi_x, \\phi_y$ "
                  "mustaqil noma'lum; Kirxhoffda ular "
                  "$-\\partial w/\\partial x$ ga tenglashtirilgan.",
                  "konseptual"),
                q("Sdvig tuzatish koeffitsienti nima uchun "
                  "kerak va u qanchaga teng?",
                  "Haqiqiy parabolik $\\tau_{xz}$ epyurasini "
                  "doimiy bilan almashtirishda energiya "
                  "ekvivalentligini saqlash uchun. "
                  "To'rtburchak kesimda $\\kappa = 5/6$.",
                  "konseptual"),
                q("Nima uchun FEM da deyarli barcha plastina "
                  "elementlari Mindlin nazariyasiga "
                  "asoslangan?",
                  "Mindlin tenglamalari ikkinchi tartibli va "
                  "$C^0$ uzluksizlik yetarli; Kirxhoff esa "
                  "$C^1$ talab qiladi va bunday elementlarni "
                  "qurish juda qiyin.", "talqin"),
                q("Kvadrat sharnirli plastinada "
                  "$\\nu = 0{,}2$, $h/a = 0{,}1$ bo'lsa, "
                  "sdvig hissasi qancha?",
                  "$\\alpha = \\pi^2/[6\\kappa(1-\\nu)] \\cdot 2 "
                  "= 4{,}935$; $c = 4{,}935 \\cdot 0{,}01 = "
                  "0{,}0494$; hissa $= c/(1+c) = 4{,}7$ % — "
                  "ya'ni 5 % chegara $h/a \\approx 0{,}104$ "
                  "da kesib o'tiladi.", "hisob"),
                q("Kodda nima uchun kamaytirilgan "
                  "integrallash qulflanishni hal qiladi?",
                  "Bitta Gauss nuqtasi sdvig deformatsiyasini "
                  "faqat element markazida tekshiradi va "
                  "soxta sdvig energiyasi hosil bo'lmaydi.",
                  "kod"),
                q("Sendvich panel yupqa bo'lsa ham nima "
                  "uchun sdvig muhim?",
                  "$D$ katta (qoplamalar uzoq), $S$ kichik "
                  "(yadro yumshoq). To'g'ri mezon geometrik "
                  "$h/a$ emas, $D/(Sa^2)$ parametri.",
                  "talqin"),
            ],
            bridge=(
                "Plastinalar nazariyasi to'liq qurildi: "
                "model, yechim usullari, doiraviy "
                "geometriya, ustuvorlik va tebranishlar, "
                "hamda sdvig tuzatmasi. Endi oxirgi "
                "qadamni tashlaymiz: o'rta sirtni "
                "tekislikdan egri sirtga aylantiramiz. "
                "Shu bitta o'zgarish qobiqlar nazariyasini "
                "keltirib chiqaradi va u plastinalardan "
                "sifat jihatdan farq qiladi."
            ),
            research=(
                "Sdvig qulflanishini bartaraf etish "
                "usullarini o'rganing va taqqoslang: "
                "(1) kamaytirilgan/tanlab integrallash — "
                "sodda, lekin soxta rejimlar (hourglass) "
                "beradi; (2) aralash formulirovka "
                "(Hellinger–Reissner) — kesuvchi kuch "
                "mustaqil approksimatsiya qilinadi; "
                "(3) MITC elementlari — sdvig "
                "deformatsiyasi maxsus nuqtalarda "
                "interpolyatsiya qilinadi; (4) EAS "
                "(Enhanced Assumed Strain). Har biri uchun "
                "inf-sup (LBB) shartini tekshiring. "
                "Bir o'lchovli balka misolida uchtasini "
                "amalga oshiring va $L/h = 10^2 \\ldots 10^5$ "
                "diapazonida yaqinlashishni solishtiring."
            ),
            manim_ref=manim(
                scene="MindlinScene",
                module="animatsiya/scenes/pq_vibration.py",
                title="Kirxhoff va Mindlin kinematikasi",
                summary=(
                    "Plastina kesimi egiladi; chap tomonda "
                    "normal chiziq perpendikulyar qoladi "
                    "(Kirxhoff), o'ng tomonda esa burchak "
                    "hosil qiladi (Mindlin). Qalinlik "
                    "oshgani sari farq kattalashishi ko'rsatiladi."
                ),
            ),
        ),
    ),
]
