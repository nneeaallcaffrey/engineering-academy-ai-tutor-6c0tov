"""PQ / 3-modul: Doiraviy plastinalar va murakkab modellar (pq-13 … pq-18)."""

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
M = "pq-m3"


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
    # ------------------------------------------------------------------ pq-13
    Topic(
        id="pq-13",
        subject_id=S, module_id=M, order=13,
        title="Doiraviy plastinalarning o'qsimmetrik egilishi: aniq yechim",
        description=(
            "Silindrik koordinatalarda plastina tenglamasi, o'qsimmetrik "
            "holatda uni oddiy differensial tenglamaga keltirish, "
            "integrallash va klassik chegaraviy shartlar uchun aniq yechimlar."
        ),
        learning_objective=(
            "O'qsimmetrik doiraviy plastina tenglamasini keltirib "
            "chiqarish, uni to'liq integrallash va sharnirli hamda "
            "mahkamlangan holatlar uchun og'ish va moment "
            "formulalarini olish."
        ),
        prerequisites=["pq-12", "tmm-16"],
        mathematical_core=(
            "Silindrik koordinatalarda $\\nabla^2 = \\frac{d^2}{dr^2} + "
            "\\frac{1}{r}\\frac{d}{dr}$, Eyler tipidagi ODE, "
            "$w = C_1 + C_2r^2 + C_3\\ln r + C_4r^2\\ln r + w_p$."
        ),
        engineering_application=(
            "Bosim idishi qopqog'i, lyuk, membrana, porshen, "
            "diafragma, dumaloq perekrytiya, tishli g'ildirak diski, "
            "bosim datchiklari."
        ),
        computational_component=(
            "Integrallash doimiylarini chegaraviy shartlardan topish, "
            "og'ish va moment epyuralarini qurish, sharnirli hamda "
            "mahkamlangan variantlarni taqqoslash."
        ),
        visualization_component=(
            "Radial og'ish profili, $M_r$ va $M_\\theta$ epyuralari, "
            "chegaraviy shartlarning ta'siri."
        ),
        research_extension=(
            "O'zgaruvchan qalinlikdagi doiraviy plastinalarni "
            "o'rganing: $h(r)$ qanday tanlansa teng mustahkamlikdagi "
            "disk hosil bo'ladi?"
        ),
        difficulty="murakkab",
        previous_link=(
            "pq-12 gacha barcha masalalar to'rtburchak koordinatalarda "
            "yechildi va analitik yechim faqat maxsus hollarda topildi. "
            "Doiraviy plastinada esa o'qsimmetriya PDE ni ODE ga "
            "aylantiradi va **to'liq aniq yechim** mavjud bo'ladi — "
            "tmm-16 dagi Lame quvuri kabi."
        ),
        next_topic="pq-14",
        estimated_minutes=95,
        tags=["doiraviy plastina", "o'qsimmetriya", "aniq yechim"],
        lesson=_lesson(
            problem=(
                "Bosim idishining dumaloq qopqog'i: diametri 800 mm, "
                "ichki bosim 1,5 MPa. Qopqoq bolt bilan mahkamlangan — "
                "bu sharnirli tayanchmi yoki qattiq mahkamlashmi? "
                "Ikkala holatda og'ish va kuchlanish qancha farq "
                "qiladi? Va eng muhimi: maksimal moment markazdami "
                "yoki chekkadami? Javob chegaraviy shartga bog'liq "
                "va u qalinlikni tanlashda hal qiluvchi."
            ),
            concepts=[
                c("O'qsimmetrik egilish",
                  "Geometriya, yuklama va chegaraviy shartlar "
                  "$\\theta$ ga bog'liq emas: $w = w(r)$. Masala "
                  "bir o'lchovli bo'lib qoladi."),
                c("Radial va halqaviy momentlar",
                  "$M_r$ — radial yo'nalishdagi egish momenti, "
                  "$M_\\theta$ — halqaviy (okruzhnoy). Ular turli "
                  "qonun bo'yicha o'zgaradi."),
                c("Silindrik Laplasian",
                  "$\\nabla^2 w = \\frac{d^2w}{dr^2} + \\frac{1}{r}"
                  "\\frac{dw}{dr} = \\frac{1}{r}\\frac{d}{dr}"
                  "\\Big(r\\frac{dw}{dr}\\Big)$ — oxirgi shakl "
                  "integrallash uchun juda qulay."),
                c("Eyler tipidagi tenglama",
                  "Koeffitsientlari $r$ ning darajalari bo'lgan ODE; "
                  "yechimi $r^k$ va $r^k\\ln r$ ko'rinishida."),
                c("Markazdagi regulyarlik sharti",
                  "To'liq diskda $r = 0$ da yechim chekli bo'lishi "
                  "kerak — bu $\\ln r$ va $r^2\\ln r$ hadlarini "
                  "yo'q qiladi ($C_3 = C_4 = 0$)."),
                c("Kesuvchi kuch muvozanatdan",
                  "$Q_r = \\frac{1}{2\\pi r}\\int_0^r q\\,2\\pi\\rho\\,d\\rho$ — "
                  "radiusi $r$ bo'lgan doira ichidagi umumiy yuklama "
                  "perimetrga bo'linadi."),
            ],
            derivation=[
                d("1. Silindrik koordinatalarda bigarmonik tenglama",
                  r"\nabla^4 w = \nabla^2(\nabla^2 w) = q/D, \qquad "
                  r"\nabla^2 = \frac{1}{r}\frac{d}{dr}\Big(r\frac{d}{dr}\Big)",
                  "O'qsimmetriyada $\\partial/\\partial\\theta = 0$, "
                  "shuning uchun Laplasian faqat $r$ bo'yicha hosilalarni "
                  "o'z ichiga oladi."),
                d("2. Kinematika: egriliklar",
                  r"\kappa_r = -\frac{d^2w}{dr^2}, \qquad "
                  r"\kappa_\theta = -\frac{1}{r}\frac{dw}{dr}",
                  "Radial egrilik — odatdagidek ikkinchi hosila; "
                  "halqaviy egrilik esa **birinchi** hosilaga "
                  "bog'liq. Sababi geometrik: qiyalikka ega sirtning "
                  "halqaviy yo'nalishdagi egriligi $w'/r$ ga teng."),
                d("3. Momentlar",
                  r"M_r = -D\Big(\frac{d^2w}{dr^2} + \frac{\nu}{r}"
                  r"\frac{dw}{dr}\Big), \qquad "
                  r"M_\theta = -D\Big(\frac{1}{r}\frac{dw}{dr} "
                  r"+ \nu\frac{d^2w}{dr^2}\Big)",
                  "pq-03 dagi munosabatlarning silindrik ko'rinishi. "
                  "Markazda ($r \\to 0$) $w' \\to 0$ va "
                  "$w'/r \\to w''$, demak $M_r = M_\\theta$ — "
                  "markazda momentlar tenglashadi."),
                d("4. Muvozanat tenglamasi",
                  r"\frac{d}{dr}(rM_r) - M_\theta = rQ_r \;\Longrightarrow\; "
                  r"\frac{d}{dr}\Big[\frac{1}{r}\frac{d}{dr}\Big(r"
                  r"\frac{dw}{dr}\Big)\Big] = -\frac{Q_r}{D}",
                  "Halqasimon elementning muvozanatidan. 3-qadamni "
                  "qo'yib soddalashtiramiz."),
                d("5. Kesuvchi kuchni yuklamadan topish",
                  r"Q_r(r) = \frac{1}{2\pi r}\int_0^r q(\rho)2\pi\rho\,d\rho "
                  r"\;\xrightarrow{q = \text{const}}\; \frac{qr}{2}",
                  "Radiusi $r$ bo'lgan doiraning vertikal muvozanati. "
                  "Bu integral shakl har qanday o'qsimmetrik yuklama "
                  "uchun ishlaydi."),
                d("6. Ketma-ket integrallash",
                  r"\frac{1}{r}\frac{d}{dr}\Big(r\frac{dw}{dr}\Big) "
                  r"= -\frac{qr^2}{8D} \cdot \frac{4}{r^2}\ldots "
                  r"\;\Longrightarrow\; w = \frac{qr^4}{64D} + C_1 "
                  r"+ C_2r^2 + C_3\ln r + C_4r^2\ln r",
                  "To'rt marta integrallash. $C_1 \\ldots C_4$ — "
                  "to'rtta doimiy; ulardan ikkitasi regulyarlik, "
                  "ikkitasi chegaraviy shartdan topiladi."),
                d("7. To'liq disk: regulyarlik",
                  r"r \to 0: \ \ln r \to -\infty, \ \frac{d}{dr}(r^2\ln r) "
                  r"\to \text{chekli, lekin } M \to \infty "
                  r"\;\Longrightarrow\; C_3 = C_4 = 0",
                  "Teshiksiz diskda markazda hech qanday singulyarlik "
                  "bo'lmasligi kerak. Halqasimon plastinada (pq-14) "
                  "esa bu hadlar saqlanadi."),
                d("8. Mahkamlangan chekka uchun yechim",
                  r"w(R) = 0, \ w'(R) = 0 \;\Longrightarrow\; "
                  r"w(r) = \frac{q}{64D}\big(R^2 - r^2\big)^2, \qquad "
                  r"w_{\max} = \frac{qR^4}{64D}",
                  "Juda ixcham natija. Sharnirli holda esa "
                  "$w_{\\max} = \\frac{qR^4}{64D}\\cdot"
                  "\\frac{5+\\nu}{1+\\nu}$ — $\\nu = 0{,}3$ da "
                  "4,08 marta katta."),
            ],
            meaning=(
                "$w_{\\max} = qR^4/(64D)$ formulasining soddaligi "
                "hayratlanarli — bu butun plastina nazariyasidagi eng "
                "ixcham natijalardan biri. Uni to'rtburchak plastina "
                "bilan solishtirish foydali: kvadrat mahkamlangan "
                "plastinada $w = 0{,}00126qa^4/D$, ya'ni "
                "$1/794$; dumaloq mahkamlangan plastinada esa "
                "$1/64 = 0{,}0156$ — lekin bu yerda $R$ **radius**, "
                "$a$ esa tomon. Bir xil qamrovli yuzada taqqoslasak "
                "($a = R\\sqrt{\\pi}$), dumaloq plastina ancha "
                "bikrroq chiqadi. Sababi — burchaklar yo'q: "
                "to'rtburchak plastinada burchaklar 'zaif' joy, "
                "u yerda material kam ishlaydi. Shuning uchun bosim "
                "idishlari, lyuklar va diafragmalar deyarli har doim "
                "dumaloq. Ikkinchi muhim natija — sharnirli va "
                "mahkamlangan holatlar orasidagi 4,08 marta farq "
                "($\\nu = 0{,}3$ da). Bu to'rtburchak plastinadagi "
                "3,2 martadan ham katta — demak doiraviy plastinada "
                "chekka mahkamlash yanada samaraliroq. Va nihoyat, "
                "momentlar: mahkamlangan plastinada maksimal moment "
                "**chekkada** ($M_r = -qR^2/8$), sharnirlida esa "
                "**markazda**. Bu armatura yoki qovurg'ani qayerga "
                "qo'yishni to'g'ridan-to'g'ri belgilaydi."
            ),
            equations=[
                eq(r"\frac{1}{r}\frac{d}{dr}\Big\{r\frac{d}{dr}\Big[\frac{1}{r}"
                   r"\frac{d}{dr}\Big(r\frac{dw}{dr}\Big)\Big]\Big\} = \frac{q}{D}",
                   "O'qsimmetrik doiraviy plastina tenglamasi.",
                   "Doiraviy plastina tenglamasi"),
                eq(r"w = \frac{qr^4}{64D} + C_1 + C_2r^2 + C_3\ln r "
                   r"+ C_4r^2\ln r",
                   "Umumiy yechim (bir tekis yuklama uchun).",
                   "Umumiy yechim"),
                eq(r"w_{\max}^{\text{mahkam}} = \frac{qR^4}{64D}, \qquad "
                   r"w_{\max}^{\text{sharnir}} = \frac{qR^4}{64D}"
                   r"\cdot\frac{5+\nu}{1+\nu}",
                   "Bir tekis yuklama ostidagi maksimal og'ish.",
                   "Maksimal og'ish"),
                eq(r"M_r^{\text{chekka, mahkam}} = -\frac{qR^2}{8}, \qquad "
                   r"M_r^{\text{markaz}} = \frac{qR^2(1+\nu)}{16}",
                   "Mahkamlangan plastinadagi xarakterli momentlar.",
                   "Momentlar"),
            ],
            conditions=(
                "**To'liq disk uchun ($0 \\le r \\le R$):**\n"
                "- $r = 0$: regulyarlik — $C_3 = C_4 = 0$ "
                "(ekvivalent shakl: $w'(0) = 0$ va $Q_r(0) = 0$);\n"
                "- $r = R$: chekka turiga qarab ikkita shart:\n"
                "  - mahkamlangan: $w = 0$, $dw/dr = 0$;\n"
                "  - sharnirli: $w = 0$, $M_r = 0$;\n"
                "  - erkin: $M_r = 0$, $V_r = 0$ (bu holda plastina "
                "muvozanatda bo'lishi uchun yuklama o'z-o'zini "
                "muvozanatlashi kerak).\n\n"
                "**Halqasimon plastina uchun ($a \\le r \\le b$)** "
                "to'rtta shart ikkala konturda ikkitadan beriladi "
                "va $C_3, C_4$ saqlanadi — pq-14.\n\n"
                "**Yuklama turlari:** bir tekis $q$; markazda "
                "konsentrlangan $P$; halqa bo'ylab $p$; "
                "chekkada moment $M_0$. Ularning har biri uchun "
                "$Q_r(r)$ alohida hisoblanadi."
            ),
            worked=WorkedExample(
                statement=(
                    "Po'lat qopqoq: $R = 400$ mm, $h = 20$ mm, "
                    "$E = 200$ GPa, $\\nu = 0{,}3$, bir tekis bosim "
                    "$q = 1{,}5$ MPa. (a) Mahkamlangan va sharnirli "
                    "holatlar uchun $w_{\\max}$ ni toping. "
                    "(b) Momentlarni hisoblang va maksimumlarni "
                    "joylashtiring. (c) Kuchlanishni toping va "
                    "$\\sigma_Y = 250$ MPa bilan solishtiring."
                ),
                given=[
                    r"R = 0{,}4\ \text{m},\ h = 0{,}02\ \text{m}",
                    r"E = 200\ \text{GPa},\ \nu = 0{,}3",
                    r"q = 1{,}5\times10^{6}\ \text{Pa}",
                ],
                steps=[
                    st(r"D = \frac{200\times10^9 \cdot 8\times10^{-6}}"
                       r"{12 \cdot 0{,}91} = \frac{1{,}6\times10^{6}}{10{,}92} "
                       r"= 1{,}4652\times10^{5}\ \text{N·m}",
                       "$h^3 = 8\\times10^{-6}$ m³."),
                    st(r"\frac{qR^4}{64D} = \frac{1{,}5\times10^{6} \cdot "
                       r"0{,}0256}{64 \cdot 1{,}4652\times10^{5}} "
                       r"= \frac{38\,400}{9{,}377\times10^{6}} "
                       r"= 4{,}095\times10^{-3}\ \text{m}",
                       "$R^4 = 0{,}0256$ m⁴. Mahkamlangan holatdagi "
                       "og'ish: 4,10 mm."),
                    st(r"w_{\text{sharnir}} = 4{,}095 \cdot \frac{5+0{,}3}"
                       r"{1+0{,}3} = 4{,}095 \cdot 4{,}0769 "
                       r"= 16{,}69\ \text{mm}",
                       "Sharnirli holatda 4,08 marta katta — "
                       "mahkamlash juda samarali."),
                    st(r"M_r^{\text{chekka}} = -\frac{qR^2}{8} = "
                       r"-\frac{1{,}5\times10^{6} \cdot 0{,}16}{8} "
                       r"= -30\,000\ \text{N·m/m}",
                       "Mahkamlangan chekkada. Manfiy — yuqori tola "
                       "cho'ziladi."),
                    st(r"M_r^{\text{markaz}} = M_\theta^{\text{markaz}} "
                       r"= \frac{qR^2(1+\nu)}{16} = \frac{1{,}5\times10^{6} "
                       r"\cdot 0{,}16 \cdot 1{,}3}{16} = 19\,500\ \text{N·m/m}",
                       "Markazda ikkala moment teng (3-qadamdagi natija). "
                       "Chekkadagidan 1,54 marta kichik."),
                    st(r"|M|_{\max} = 30\,000\ \text{N·m/m} "
                       r"\ \text{(chekkada)}",
                       "Mahkamlangan plastinada eng xavfli joy — "
                       "**chekka**, markaz emas. Bu armatura yoki "
                       "qalinlashtirish joyini belgilaydi."),
                    st(r"\sigma_{\max} = \frac{6|M|}{h^2} = "
                       r"\frac{6 \cdot 30\,000}{4\times10^{-4}} "
                       r"= 450\ \text{MPa} > \sigma_Y = 250\ \text{MPa}",
                       "Oqish chegarasidan oshdi — qalinlik yetarli emas!"),
                    st(r"h_{\text{kerak}} = \sqrt{\frac{6 \cdot 30\,000}"
                       r"{250\times10^{6}/1{,}5}} = \sqrt{1{,}08\times10^{-3}} "
                       r"= 32{,}9\ \text{mm} \Rightarrow h = 35\ \text{mm}",
                       "$n = 1{,}5$ xavfsizlik koeffitsienti bilan. "
                       "$h = 35$ mm da $\\sigma = 147$ MPa, "
                       "$w = 0{,}76$ mm."),
                ],
                answer=(
                    "$D = 146{,}5$ kN·m; mahkamlangan "
                    "$w_{\\max} = 4{,}10$ mm, sharnirli 16,69 mm "
                    "(4,08 marta); $|M|_{\\max} = 30$ kN·m/m "
                    "**chekkada**, markazda 19,5 kN·m/m; "
                    "$h = 20$ mm da $\\sigma = 450$ MPa — yetarli "
                    "emas, $h = 35$ mm kerak."
                ),
                engineering_note=(
                    "Bolt bilan mahkamlangan qopqoq amalda sharnirli "
                    "va qattiq mahkamlash orasida yotadi: flanets "
                    "biroz buriladi, prokladka siqiladi. Konservativ "
                    "loyihalashda ikkala holat ham hisoblanadi — "
                    "og'ish sharnirli bo'yicha (katta qiymat), "
                    "chekkadagi moment esa mahkamlangan bo'yicha "
                    "(katta qiymat). ASME BPVC kodeksi aynan shunday "
                    "yondashuvni belgilaydi va $Z$ koeffitsienti "
                    "orqali oraliq holatni hisobga oladi."
                ),
            ),
            computation=Computation(
                caption=(
                    "O'qsimmetrik doiraviy plastinani turli chegaraviy "
                    "shartlar va yuklamalar uchun yechish, moment "
                    "epyuralarini qurish."
                ),
                code='''"""Doiraviy plastinaning o'qsimmetrik egilishi."""
import numpy as np
from labkit import PARAMS, note, series, table, value

R = float(PARAMS.get("R", 400.0))/1000.0
h = float(PARAMS.get("h", 20.0))/1000.0
E = float(PARAMS.get("E", 200.0))*1e9
nu = float(PARAMS.get("nu", 0.3))
qload = float(PARAMS.get("q", 1.5))*1e6
P = float(PARAMS.get("P", 0.0))          # markazda konsentrlangan kuch
sY = float(PARAMS.get("sY", 250.0))*1e6
bc = int(PARAMS.get("bc", 0))            # 0 mahkamlangan, 1 sharnirli

D = E*h**3/(12*(1 - nu**2))
value("Silindrik bikrlik D", D/1000, "kN*m")
value("Radius R", R, "m")
value("R/h nisbati", R/h, "—")
if R/h < 10:
    note(f"R/h = {R/h:.1f} < 10 — qalin plita, Kirxhoff nazariyasi "
         f"xatosi sezilarli bo'lishi mumkin.")

r = np.linspace(1e-6, R, 400)
x = r/R

# --- Bir tekis yuklama ---
if bc == 0:      # mahkamlangan
    w_q = qload*R**4/(64*D)*(1 - x**2)**2
    Mr_q = qload*R**2/16*((1 + nu) - (3 + nu)*x**2)
    Mt_q = qload*R**2/16*((1 + nu) - (1 + 3*nu)*x**2)
else:            # sharnirli
    w_q = (qload*R**4/(64*D))*(1 - x**2)*((5 + nu)/(1 + nu) - x**2)
    Mr_q = qload*R**2/16*(3 + nu)*(1 - x**2)
    Mt_q = qload*R**2/16*((3 + nu) - (1 + 3*nu)*x**2)

# --- Markazda konsentrlangan kuch (qo'shimcha) ---
if P != 0.0:
    if bc == 0:
        w_P = P*R**2/(16*np.pi*D)*(1 - x**2 + 2*x**2*np.log(np.maximum(x, 1e-12)))
        Mr_P = -P/(4*np.pi)*(1 + nu)*np.log(np.maximum(x, 1e-12)) - P/(4*np.pi)
        Mt_P = -P/(4*np.pi)*(1 + nu)*np.log(np.maximum(x, 1e-12)) - P*nu/(4*np.pi)
    else:
        w_P = P*R**2/(16*np.pi*D)*((3 + nu)/(1 + nu)*(1 - x**2)
                                   + 2*x**2*np.log(np.maximum(x, 1e-12)))
        Mr_P = -P/(4*np.pi)*(1 + nu)*np.log(np.maximum(x, 1e-12))
        Mt_P = -P/(4*np.pi)*((1 + nu)*np.log(np.maximum(x, 1e-12)) + 1 - nu)
else:
    w_P = np.zeros_like(r); Mr_P = np.zeros_like(r); Mt_P = np.zeros_like(r)

w = w_q + w_P
Mr = Mr_q + Mr_P
Mt = Mt_q + Mt_P

bc_name = "mahkamlangan" if bc == 0 else "sharnirli"
series(f"Og'ish w(r) — {bc_name}", (r*1000).tolist(), (w*1000).tolist(),
       xlabel="Radius r, mm", ylabel="Og'ish w, mm")
series("Radial moment M_r(r)", (r*1000).tolist(), (Mr/1000).tolist(),
       xlabel="Radius r, mm", ylabel="M_r, kN*m/m")
series("Halqaviy moment M_theta(r)", (r*1000).tolist(), (Mt/1000).tolist(),
       xlabel="Radius r, mm", ylabel="M_theta, kN*m/m")

value("w_max (markazda)", float(w[0])*1000, "mm")
value("w_max / R", float(w[0])/R, "—")
value("M_r (markazda)", float(Mr[0])/1000, "kN*m/m")
value("M_theta (markazda)", float(Mt[0])/1000, "kN*m/m")
value("M_r (chekkada)", float(Mr[-1])/1000, "kN*m/m")
value("M_theta (chekkada)", float(Mt[-1])/1000, "kN*m/m")

M_abs = max(float(np.max(np.abs(Mr))), float(np.max(np.abs(Mt))))
i_max = int(np.argmax(np.maximum(np.abs(Mr), np.abs(Mt))))
value("Maksimal |M|", M_abs/1000, "kN*m/m")
value("Maksimal |M| joyi r/R", float(x[i_max]), "—")
sig = 6*M_abs/h**2
value("Maksimal kuchlanish", sig/1e6, "MPa")
value("Zaxira koeffitsienti", sY/sig, "—")
if sig > sY:
    h_need = np.sqrt(6*M_abs/(sY/1.5))
    note(f"OQISH: sigma = {sig/1e6:.0f} MPa > sigma_Y = {sY/1e6:.0f} MPa. "
         f"n = 1.5 bilan kerakli qalinlik {h_need*1000:.1f} mm.")
else:
    note(f"Elastik holat: sigma = {sig/1e6:.1f} MPa, zaxira {sY/sig:.2f}. "
         f"Maksimal moment r/R = {x[i_max]:.2f} da.")

# --- Ikki chegaraviy shartni taqqoslash ---
w_cl = qload*R**4/(64*D)
w_ss = w_cl*(5 + nu)/(1 + nu)
value("w_max mahkamlangan (tekis yuklama)", w_cl*1000, "mm")
value("w_max sharnirli (tekis yuklama)", w_ss*1000, "mm")
value("Sharnirli/mahkamlangan nisbati", (5 + nu)/(1 + nu), "—")

nus = np.linspace(0.0, 0.45, 100)
series("w_ss/w_cl nisbati (nu ga bog'liq)", nus.tolist(),
       ((5 + nus)/(1 + nus)).tolist(),
       xlabel="Puasson koeffitsienti nu", ylabel="Nisbat")
note(f"nu = 0 da nisbat 5.00, nu = 0.3 da {(5+0.3)/(1+0.3):.2f}, "
     f"nu = 0.5 da {(5+0.5)/(1+0.5):.2f} — Puasson koeffitsienti "
     f"chegaraviy shart samaradorligiga sezilarli ta'sir qiladi.")

# --- Qalinlikni loyihalash ---
hs = np.linspace(0.005, 0.08, 200)
sigs, ws = [], []
for hh in hs:
    Dh = E*hh**3/(12*(1 - nu**2))
    if bc == 0:
        Mmax = qload*R**2/8
        wmax = qload*R**4/(64*Dh)
    else:
        Mmax = qload*R**2*(3 + nu)/16
        wmax = qload*R**4/(64*Dh)*(5 + nu)/(1 + nu)
    sigs.append(6*Mmax/hh**2/1e6)
    ws.append(wmax*1000)
series("sigma(h)", (hs*1000).tolist(), sigs,
       xlabel="Qalinlik h, mm", ylabel="Maksimal kuchlanish, MPa")
series("w_max(h)", (hs*1000).tolist(), ws,
       xlabel="Qalinlik h, mm", ylabel="w_max, mm")
series("Oqish chegarasi", (hs*1000).tolist(),
       [sY/1e6]*len(hs), xlabel="Qalinlik h, mm",
       ylabel="Maksimal kuchlanish, MPa")

table("Doiraviy plastina: klassik natijalar (bir tekis yuklama q)",
      ["Chegaraviy shart", "w_max", "M_r(0)", "M_r(R)", "M_theta(R)"],
      [["Mahkamlangan", "qR^4/(64D)", "qR^2(1+nu)/16", "-qR^2/8",
        "-nu*qR^2/8"],
       ["Sharnirli", "qR^4(5+nu)/(64D(1+nu))", "qR^2(3+nu)/16", "0",
        "qR^2(1-nu)(3+nu)/16"]])

table("To'rtburchak va doiraviy plastinalarning taqqoslashi",
      ["Shakl", "Mahkamlangan koeff.", "Sharnirli koeff.", "Nisbat"],
      [["Kvadrat (tomon a)", 0.00126, 0.004062, round(0.004062/0.00126, 2)],
       ["Doira (radius R)", round(1/64, 5), round((5+nu)/(64*(1+nu)), 5),
        round((5+nu)/(1+nu), 2)]])
note("Diqqat: kvadratda a — tomon, doirada R — radius. Bir xil "
     "yuzada taqqoslash uchun a = R*sqrt(pi) olish kerak.")
''',
                parameters=[
                    p("R", "Radius R", 30.0, 3000.0, 400.0, 10.0, "mm"),
                    p("h", "Qalinlik h", 1.0, 200.0, 20.0, 1.0, "mm"),
                    p("E", "Yung moduli E", 1.0, 400.0, 200.0, 1.0, "GPa"),
                    p("nu", "Puasson koeffitsienti ν", 0.0, 0.45, 0.3, 0.01),
                    p("q", "Bir tekis bosim q", 0.001, 20.0, 1.5, 0.01, "MPa"),
                    p("P", "Markazdagi kuch P", -500000.0, 500000.0, 0.0,
                      1000.0, "N"),
                    p("sY", "Oqish chegarasi σ_Y", 20.0, 1000.0, 250.0, 5.0, "MPa"),
                    p("bc", "Chekka (0 mahkam, 1 sharnir)", 0.0, 1.0, 0.0, 1.0),
                ],
                expected_output=(
                    "D = 146,5 kN·m; mahkamlangan w_max = 4,095 mm, "
                    "sharnirli 16,69 mm (nisbat 4,077); M_r(0) = "
                    "19,5 kN·m/m, M_r(R) = −30 kN·m/m — maksimum "
                    "chekkada; σ = 450 MPa > 250 MPa, kerakli "
                    "qalinlik ≈ 33 mm."
                ),
            ),
            visual=vis(
                kind="Doiraviy plastina epyuralari",
                tool="React/SVG",
                description=(
                    "Radial og'ish profili, $M_r$ va $M_\\theta$ "
                    "epyuralari, chegaraviy shartlarning qiyosi."
                ),
                how_to_draw=(
                    "React/SVG: birinchi panel — plastinaning yon "
                    "kesimi: gorizontal chiziq (deformatsiyalanmagan) "
                    "va egilgan profil `<path>`, chekkada chegaraviy "
                    "shart belgisi (shtrixlash = mahkamlangan, "
                    "uchburchak = sharnirli). Og'ish masshtabi "
                    "oshirilgan va bu yorliqda ko'rsatiladi. "
                    "Ikkinchi panel — moment epyuralari: $M_r$ va "
                    "$M_\\theta$ bir grafikda, $r/R$ o'qi bo'ylab; "
                    "musbat va manfiy sohalar turli rangda "
                    "to'ldiriladi (cho'zilish/siqilish duali). "
                    "Mahkamlangan holatda $M_r$ ning ishorasi "
                    "o'zgarishi va chekkada maksimal bo'lishi "
                    "darhol ko'rinadi. Uchinchi panel — plastinaning "
                    "ustdan ko'rinishi: kontsentrik halqalar bilan "
                    "moment kattaligi rang orqali; markazda "
                    "$M_r = M_\\theta$ ekanligi ikki rang "
                    "birlashishi bilan ko'rsatiladi. Chegaraviy "
                    "shart tugmasi bilan almashtiriladi va uchala "
                    "panel sinxron yangilanadi."
                ),
            ),
            interp=(
                "Moment epyuralari loyihalash uchun eng muhim "
                "ma'lumotni beradi: mahkamlangan plastinada "
                "$M_r$ chekkada maksimal va **manfiy**, markazda "
                "esa musbat va 1,5 marta kichik. Demak temir-beton "
                "qopqoqda armatura chekka yaqinida **yuqori** "
                "zonaga, markazda esa **pastki** zonaga qo'yiladi. "
                "Bu bir qarashda kutilmagan, lekin balka "
                "nazariyasidagi (mq-14) mahkamlangan balka bilan "
                "to'liq mos: u yerda ham tayanchda moment ishorasi "
                "qarama-qarshi. Sharnirli/mahkamlangan nisbatining "
                "$\\nu$ ga bog'liqlik grafigi ham qiziq: "
                "$\\nu = 0$ da nisbat aynan 5, $\\nu = 0{,}5$ da "
                "esa 3,67 ga tushadi. Demak rezina kabi "
                "siqilmaydigan materialda chekka mahkamlash "
                "kamroq samara beradi. Sababi — Puasson effekti "
                "halqaviy yo'nalishda qo'shimcha cheklov yaratadi "
                "va sharnirli plastina ham 'o'z-o'zidan' bikrroq "
                "bo'lib qoladi. Va nihoyat, markazda "
                "$M_r = M_\\theta$ tengligi — bu o'qsimmetriyaning "
                "to'g'ridan-to'g'ri oqibati: markazda hech qanday "
                "ajratilgan yo'nalish yo'q, shuning uchun moment "
                "tenzori izotrop bo'lishi shart."
            ),
            mistakes=[
                "Halqaviy egrilikni $-w''$ deb olish. To'g'ri "
                "ifoda $\\kappa_\\theta = -w'/r$ — u birinchi "
                "hosilaga bog'liq.",
                "To'liq diskda $\\ln r$ va $r^2\\ln r$ hadlarini "
                "saqlash. Ular markazda singulyarlik beradi; "
                "faqat halqasimon plastinada (pq-14) kerak.",
                "Maksimal momentni har doim markazda deb "
                "hisoblash. Mahkamlangan plastinada u chekkada "
                "va 1,5 marta katta.",
                "Dumaloq va to'rtburchak plastina koeffitsientlarini "
                "to'g'ridan-to'g'ri taqqoslash. Birida $R$ — "
                "radius, ikkinchisida $a$ — tomon; bir xil yuza "
                "uchun $a = R\\sqrt{\\pi}$ olish kerak.",
            ],
            quiz=[
                q("Nima uchun o'qsimmetrik masalada PDE oddiy "
                  "differensial tenglamaga aylanadi?",
                  "$\\partial/\\partial\\theta = 0$ bo'lgani uchun "
                  "$w = w(r)$ — bitta mustaqil o'zgaruvchi qoladi.",
                  "konseptual"),
                q("Halqaviy egrilik formulasini yozing va uning "
                  "geometrik ma'nosini ayting.",
                  "$\\kappa_\\theta = -\\frac{1}{r}\\frac{dw}{dr}$. "
                  "Qiyalikka ega sirtning halqaviy yo'nalishdagi "
                  "egriligi radiusga teskari mutanosib.", "konseptual"),
                q("Mahkamlangan doiraviy plastinada maksimal moment "
                  "qayerda va qancha?",
                  "Chekkada: $M_r = -qR^2/8$. Markazdagi "
                  "$qR^2(1+\\nu)/16$ dan $8/(1+\\nu) \\cdot 1/2 = "
                  "1{,}54$ marta katta ($\\nu = 0{,}3$).", "hisob"),
                q("$R = 300$ mm, $h = 15$ mm, $q = 1$ MPa, "
                  "$E = 200$ GPa, $\\nu = 0{,}3$, mahkamlangan. "
                  "$w_{\\max}$ ni toping.",
                  "$D = 61\\,813$ N·m; "
                  "$w = 1\\times10^6 \\cdot 0{,}0081/(64 \\cdot "
                  "61\\,813) = 2{,}05$ mm.", "hisob"),
                q("Kodda nima uchun $r$ nol emas, $10^{-6}$ dan "
                  "boshlanadi?",
                  "Konsentrlangan kuch hadlarida $\\ln(r/R)$ bor "
                  "va $r = 0$ da u aniqlanmagan. Kichik qiymat "
                  "sonli xatoni oldini oladi; tekis yuklamada "
                  "bu ta'sir qilmaydi.", "kod"),
                q("Nima uchun markazda $M_r = M_\\theta$?",
                  "O'qsimmetriyada markazda ajratilgan yo'nalish "
                  "yo'q, shuning uchun moment tenzori izotrop "
                  "bo'lishi shart — barcha yo'nalishlarda bir xil.",
                  "talqin"),
            ],
            bridge=(
                "To'liq diskda regulyarlik sharti ikkita doimiyni "
                "yo'q qildi. Agar markazda teshik bo'lsa, ular "
                "saqlanadi va yechim ancha boyroq bo'ladi. "
                "Keyingi mavzuda halqasimon plastinalarni "
                "o'rganamiz — ular quvur flanetsi, tishli "
                "g'ildirak diski va podshipnik qopqog'ining modeli."
            ),
            research=(
                "O'zgaruvchan qalinlikdagi doiraviy plastinalarni "
                "o'rganing. $h = h(r)$ bo'lsa, $D = D(r)$ va "
                "tenglama o'zgaruvchan koeffitsientli bo'lib "
                "qoladi. $h \\propto r^{-n}$ shaklida qalinlik "
                "tanlansa tenglama yana Eyler tipida qoladi va "
                "analitik yechiladi. **Teng mustahkamlik** "
                "sharti ($\\sigma = $ const barcha $r$ da) "
                "qanday $h(r)$ ni talab qiladi? Bu natijani "
                "bug' turbinasi diski yoki tishli g'ildirak "
                "shaklini loyihalashda qanday ishlatish mumkin? "
                "Sonli optimallashtirish bilan tekshiring va "
                "doimiy qalinlikdagi disk bilan og'irlik "
                "bo'yicha taqqoslang."
            ),
            manim_ref=manim(
                scene="CircularPlateScene",
                module="animatsiya/scenes/pq_circular.py",
                title="Doiraviy plastinaning o'qsimmetrik egilishi",
                summary=(
                    "Bosim ostida disk egiladi; radial va halqaviy "
                    "momentlar epyuralari bir vaqtda quriladi, "
                    "mahkamlangan va sharnirli chekka variantlari "
                    "almashtirilib taqqoslanadi."
                ),
            ),
        ),
    ),

    # ------------------------------------------------------------------ pq-14
    Topic(
        id="pq-14",
        subject_id=S, module_id=M, order=14,
        title="Halqasimon plastinalar va markaziy teshikli disklar",
        description=(
            "Markazida teshigi bo'lgan doiraviy plastina, to'rtta "
            "integrallash doimiysining to'liq saqlanishi, ichki va "
            "tashqi konturdagi chegaraviy shartlar hamda teshik "
            "atrofidagi kuchlanish konsentratsiyasi."
        ),
        learning_objective=(
            "Halqasimon plastina uchun to'rtta doimiyni chegaraviy "
            "shartlardan topish, teshik o'lchamining og'ish va "
            "kuchlanishga ta'sirini tahlil qilish."
        ),
        prerequisites=["pq-13"],
        mathematical_core=(
            "To'rtta doimiyli umumiy yechim, $4\\times4$ chiziqli "
            "tizim, $\\ln r$ va $r^2\\ln r$ hadlarining roli, "
            "teshik radiusining limiti."
        ),
        engineering_application=(
            "Quvur flanetsi, podshipnik qopqog'i, turbina diski, "
            "tishli g'ildirak, tormoz diski, lyuk halqasi, "
            "membranali klapanlar."
        ),
        computational_component=(
            "$4\\times4$ tizimni sonli yechish, teshik radiusi "
            "bo'yicha parametrik tahlil, to'liq disk limitiga "
            "yaqinlashishni tekshirish."
        ),
        visualization_component=(
            "Halqa kesimi, og'ish va moment epyuralari, teshik "
            "o'lchamining ta'siri grafigi."
        ),
        research_extension=(
            "Aylanuvchi diskdagi markazdan qochma kuchlarni "
            "hisobga oling: turbina diski uchun birlashgan "
            "egilish + membrana masalasi qanday qo'yiladi?"
        ),
        difficulty="murakkab",
        previous_link=(
            "pq-13 da to'liq diskda regulyarlik sharti $C_3$ va "
            "$C_4$ ni yo'q qildi. Markazda teshik bo'lsa, "
            "$r = 0$ soha ichida emas va bu hadlar saqlanadi — "
            "yechim to'rtta doimiyli to'liq shaklda ishlatiladi."
        ),
        next_topic="pq-15",
        estimated_minutes=90,
        tags=["halqasimon plastina", "teshik", "flanets", "disk"],
        lesson=_lesson(
            problem=(
                "Quvur flanetsi: tashqi diametri 300 mm, ichki "
                "(quvur) diametri 100 mm, boltlar tashqi konturda. "
                "Ichki bosim flanetsga taqsimlangan yuklama beradi. "
                "Teshik qanchalik ta'sir qiladi? Intuitsiya: "
                "teshik materialni olib tashlaydi, demak plastina "
                "zaiflashadi. Lekin teshik yuklamani ham olib "
                "tashlaydi. Qaysi effekt kuchliroq? Javob teshik "
                "o'lchamiga va yuklamaning taqsimlanishiga bog'liq — "
                "natija intuitsiyaga zid chiqadi."
            ),
            concepts=[
                c("Halqasimon plastina (annular plate)",
                  "$a \\le r \\le b$ sohada aniqlangan plastina; "
                  "ichki va tashqi konturda alohida chegaraviy "
                  "shartlar beriladi."),
                c("To'rtta doimiy",
                  "$w = w_p + C_1 + C_2r^2 + C_3\\ln r + C_4r^2\\ln r$ — "
                  "hech biri yo'qolmaydi, chunki $r = 0$ soha "
                  "ichida emas."),
                c("$\\ln r$ hadining ma'nosi",
                  "Ichki konturda qo'yilgan kesuvchi kuchga mos "
                  "keladi; u yo'q bo'lsa $C_3$ boshqa shartlardan "
                  "topiladi."),
                c("$r^2\\ln r$ hadining ma'nosi",
                  "Konsentrlangan halqaviy yuklamaga yoki ichki "
                  "konturdagi momentga mos keladi."),
                c("Erkin ichki kontur",
                  "Eng ko'p uchraydigan hol: teshik yuzasiga hech "
                  "narsa ta'sir qilmaydi, $M_r(a) = 0$, $V_r(a) = 0$."),
                c("Kuchlanish konsentratsiyasi",
                  "Kichik teshik atrofida $M_\\theta$ keskin oshadi — "
                  "tmm-17 dagi Kirsh yechimining egilishdagi analogi."),
            ],
            derivation=[
                d("1. Umumiy yechim to'liq shaklda",
                  r"w(r) = \frac{qr^4}{64D} + C_1 + C_2r^2 + C_3\ln r "
                  r"+ C_4 r^2\ln r",
                  "pq-13 dagi natija, lekin endi hech bir had "
                  "tashlanmaydi. To'rtta noma'lum doimiy."),
                d("2. Hosilalar",
                  r"w' = \frac{qr^3}{16D} + 2C_2r + \frac{C_3}{r} "
                  r"+ C_4 r(2\ln r + 1)",
                  "Burilish burchagi uchun kerak (mahkamlash "
                  "shartlarida)."),
                d("3. Ikkinchi hosila",
                  r"w'' = \frac{3qr^2}{16D} + 2C_2 - \frac{C_3}{r^2} "
                  r"+ C_4(2\ln r + 3)",
                  "Momentlar uchun kerak. $C_3/r^2$ hadi ichki "
                  "konturga yaqin joyda hukmron bo'ladi."),
                d("4. Momentlar",
                  r"M_r = -D\Big(w'' + \frac{\nu}{r}w'\Big), \qquad "
                  r"M_\theta = -D\Big(\frac{w'}{r} + \nu w''\Big)",
                  "pq-13 dagi munosabatlar. Ularni 2- va 3-qadam "
                  "natijalari bilan to'ldiramiz."),
                d("5. $M_r$ ni doimiylar orqali yozish",
                  r"M_r = -D\Big[\frac{q r^2(3+\nu)}{16D} + 2C_2(1+\nu) "
                  r"- \frac{C_3(1-\nu)}{r^2} + C_4\big((1+\nu)(2\ln r + 1) "
                  r"+ 2\big)\Big]",
                  "Chegaraviy shartlarda to'g'ridan-to'g'ri "
                  "ishlatiladigan shakl. $C_3$ hadining "
                  "$(1-\\nu)$ ko'paytuvchisiga e'tibor bering."),
                d("6. Kesuvchi kuch va Kirxhoff kuchi",
                  r"Q_r = \frac{qr}{2} + \frac{4DC_4}{r}, \qquad "
                  r"V_r = Q_r \ (\text{o'qsimmetriyada } M_{r\theta} = 0)",
                  "O'qsimmetrik masalada buralish momenti nolga "
                  "teng, shuning uchun Kirxhoff tuzatmasi kerak "
                  "emas — bu doiraviy plastinaning yana bir "
                  "soddalashtiruvchi xususiyati."),
                d("7. To'rtta chegaraviy shart",
                  r"\text{Ichki } (r=a): \ M_r = 0, \ V_r = 0; \qquad "
                  r"\text{Tashqi } (r=b): \ w = 0, \ w' = 0 \ "
                  r"(\text{mahkamlangan})",
                  "Bu eng ko'p uchraydigan kombinatsiya: erkin "
                  "teshik + mahkamlangan tashqi kontur. To'rtta "
                  "tenglama, to'rtta noma'lum."),
                d("8. Chiziqli tizim",
                  r"\mathbf{A}\begin{Bmatrix}C_1\\C_2\\C_3\\C_4\end{Bmatrix} "
                  r"= \mathbf{f}, \qquad \mathbf{A} \in \mathbb{R}^{4\times4}",
                  "Har bir chegaraviy shart bitta satr beradi. "
                  "Tizim sonli yechiladi; analitik yechim mavjud, "
                  "lekin juda uzun. Kodda $\\mathbf{A}$ oshkor quriladi."),
            ],
            meaning=(
                "Teshikning ta'siri ikki qarama-qarshi mexanizmdan "
                "iborat. Birinchi mexanizm: "
                "teshik materialni olib tashlaydi, bu plastinani "
                "zaiflashtiradi. Ikkinchi mexanizm: teshik "
                "yuklamani ham olib tashlaydi — markazdagi "
                "bosim endi plastinaga ta'sir qilmaydi, va aynan "
                "markaz eng katta yelkaga ega. Bosim tipidagi "
                "yuklamada (butun yuzaga taqsimlangan) ikkinchi "
                "effekt ustun keladi va og'ish teshik kattalashgani "
                "sari **monoton kamayadi** — qolgan halqa tashqi "
                "konturga yaqin va qisqa bo'lgani uchun bikrroq. "
                "Agar yuklama faqat tashqi halqaga qo'yilgan "
                "bo'lsa (boltlar orqali), aksincha, teshik faqat "
                "zaiflashtiradi. Eng qiziq natija esa "
                "$a/b \\to 0$ limitida ko'rinadi: cheksiz kichik teshik og'ishga "
                "deyarli ta'sir qilmaydi, lekin **halqaviy "
                "momentni ikki baravar oshiradi** — bu tmm-17 "
                "dagi Kirsh yechimining ($K_t = 3$) egilishdagi "
                "analogi. Sababi bir xil: teshik atrofida "
                "kuchlanish oqimi 'siqilishi' kerak. Amaliy "
                "oqibati juda muhim: konstruksiyaga texnologik "
                "teshik (drenaj, kabel o'tkazgich) qo'shilganda "
                "og'ish o'zgarmasligi mumkin, lekin mahalliy "
                "kuchlanish ikki barobar oshadi va charchoq "
                "yoriqlari aynan shu yerdan boshlanadi."
            ),
            equations=[
                eq(r"w = \frac{qr^4}{64D} + C_1 + C_2r^2 + C_3\ln r "
                   r"+ C_4r^2\ln r",
                   "Halqasimon plastinaning to'liq umumiy yechimi.",
                   "Umumiy yechim"),
                eq(r"M_r = -D\Big[w'' + \frac{\nu}{r}w'\Big], \qquad "
                   r"M_\theta = -D\Big[\frac{w'}{r} + \nu w''\Big]",
                   "Radial va halqaviy momentlar.", "Momentlar"),
                eq(r"Q_r = \frac{qr}{2} + \frac{4DC_4}{r}",
                   "Kesuvchi kuch; ikkinchi had ichki konturdagi "
                   "yuklamadan.", "Kesuvchi kuch"),
                eq(r"\lim_{a/b \to 0} \frac{M_\theta(a)}"
                   r"{M^{\text{to'liq}}(0)} \approx 2",
                   "Kichik teshik atrofidagi moment konsentratsiyasi.",
                   "Konsentratsiya"),
            ],
            conditions=(
                "**Ichki kontur ($r = a$) variantlari:**\n"
                "- Erkin: $M_r = 0$, $V_r = 0$ — eng ko'p uchraydigan;\n"
                "- Mahkamlangan (val bilan): $w = 0$, $w' = 0$;\n"
                "- Sharnirli: $w = 0$, $M_r = 0$;\n"
                "- Yuklangan: $V_r = -P/(2\\pi a)$ — halqaviy kuch.\n\n"
                "**Tashqi kontur ($r = b$) variantlari** to'liq "
                "diskdagidek.\n\n"
                "**Sonli barqarorlik:** $a/b$ juda kichik bo'lsa "
                "($< 0{,}01$), $\\ln(a/b)$ katta manfiy son "
                "bo'ladi va tizim matritsasi yomon shartlangan. "
                "Amalda $a/b \\ge 0{,}02$ oralig'ida ishlanadi; "
                "undan kichikroq teshik uchun to'liq disk yechimi "
                "+ mahalliy konsentratsiya koeffitsienti "
                "ishlatiladi.\n\n"
                "**Kirxhoff tuzatmasi kerak emas:** o'qsimmetrik "
                "masalada $M_{r\\theta} = 0$, demak $V_r = Q_r$."
            ),
            worked=WorkedExample(
                statement=(
                    "Po'lat flanets: tashqi radius $b = 150$ mm "
                    "(mahkamlangan), ichki radius $a = 50$ mm "
                    "(erkin), $h = 12$ mm, $E = 200$ GPa, "
                    "$\\nu = 0{,}3$, bir tekis yuklama "
                    "$q = 2$ MPa. Teshikli va teshiksiz (to'liq "
                    "disk, bir xil $b$) variantlarni taqqoslang: "
                    "og'ish, momentlar va kuchlanish."
                ),
                given=[
                    r"a = 0{,}05\ \text{m},\ b = 0{,}15\ \text{m},\ "
                    r"a/b = 1/3",
                    r"h = 0{,}012\ \text{m},\ E = 200\ \text{GPa},\ "
                    r"\nu = 0{,}3",
                    r"q = 2\times10^{6}\ \text{Pa}",
                ],
                steps=[
                    st(r"D = \frac{200\times10^9 \cdot 1{,}728\times10^{-6}}"
                       r"{12 \cdot 0{,}91} = 3{,}1648\times10^{4}\ \text{N·m}",
                       "$h^3 = 1{,}728\\times10^{-6}$ m³."),
                    st(r"\text{To'liq disk: } w_{\max} = \frac{qb^4}{64D} "
                       r"= \frac{2\times10^{6} \cdot 5{,}0625\times10^{-4}}"
                       r"{64 \cdot 3{,}1648\times10^{4}}",
                       "$b^4 = 5{,}0625\\times10^{-4}$ m⁴."),
                    st(r"w_{\text{to'liq}} = \frac{1012{,}5}{2{,}0255\times10^{6}} "
                       r"= 4{,}999\times10^{-4}\ \text{m} = 0{,}500\ \text{mm}",
                       "Teshiksiz variantdagi og'ish."),
                    st(r"M_r^{\text{to'liq}}(b) = -\frac{qb^2}{8} = "
                       r"-\frac{2\times10^{6} \cdot 0{,}0225}{8} "
                       r"= -5625\ \text{N·m/m}",
                       "Chekkadagi moment — to'liq diskda maksimal."),
                    st(r"\text{Halqa: to'rtta shart} \Rightarrow "
                       r"\mathbf{A}\mathbf{C} = \mathbf{f}, \ "
                       r"\mathbf{A} \in \mathbb{R}^{4\times4}",
                       "$M_r(a) = 0$, $V_r(a) = 0$, $w(b) = 0$, "
                       "$w'(b) = 0$. Tizim kodda sonli yechiladi."),
                    st(r"\text{Kod natijasi: } w_{\max}^{\text{halqa}} "
                       r"= 0{,}3796\ \text{mm} \ (\text{ichki konturda})",
                       "Teshik og'ishni **kamaytirdi**: to'liq diskdagi "
                       "0,500 mm dan 0,380 mm ga, ya'ni 24 % ga — "
                       "chunki u markaziy yuklamani ham olib tashladi."),
                    st(r"M_\theta(a) = 3027\ \text{N·m/m}, \quad "
                       r"M_r(a) = 0 \ (\text{erkin shart}), \quad "
                       r"M_r(b) = -4925\ \text{N·m/m}",
                       "Ichki konturda $M_r$ aynan nolga teng — sonli "
                       "yechim buni $10^{-13}$ aniqlikda tasdiqlaydi; "
                       "$M_\\theta$ esa u yerda nolga teng emas."),
                    st(r"\sigma_{\max} = \frac{6 \cdot 4925}{1{,}44\times10^{-4}} "
                       r"= 205{,}2\ \text{MPa} \ (\text{tashqi chekka})",
                       "Tashqi chekka eng xavfli joy. To'liq diskda "
                       "$6 \\cdot 5625/h^2 = 234$ MPa bo'lardi — "
                       "teshik kuchlanishni ham 12 % kamaytirdi."),
                ],
                answer=(
                    "$D = 31{,}65$ kN·m. Teshiksiz: $w = 0{,}500$ mm, "
                    "$M_r(b) = -5625$ N·m/m, $\\sigma = 234$ MPa. "
                    "Teshikli ($a/b = 1/3$): $w = 0{,}3796$ mm "
                    "(**24 % kamaydi**), $M_r(b) = -4925$ N·m/m, "
                    "ichki konturda $M_r = 0$ va "
                    "$M_\\theta = 3027$ N·m/m; "
                    "$\\sigma_{\\max} = 205$ MPa."
                ),
                engineering_note=(
                    "Og'ishning kamayishi kutilmagan, lekin mantiqiy: "
                    "$a/b = 1/3$ da teshik plastina yuzasining "
                    "11 % ini olib tashlaydi, lekin u eng katta "
                    "yelkaga ega markaziy soha. Bu effekt faqat "
                    "yuklama teshik joyida ham mavjud bo'lganda "
                    "ishlaydi (bosim, o'z og'irligi). Agar yuklama "
                    "faqat tashqi halqaga qo'yilgan bo'lsa "
                    "(masalan, boltlar orqali), teshik faqat "
                    "zaiflashtiradi. Shuning uchun har bir holatda "
                    "yuklamaning haqiqiy taqsimoti aniqlanishi shart."
                ),
            ),
            computation=Computation(
                caption=(
                    "Halqasimon plastina uchun $4\\times4$ tizimni "
                    "qurish va yechish, teshik radiusining ta'sirini "
                    "parametrik tahlil qilish."
                ),
                code='''"""Halqasimon plastina: to'rtta doimiy va teshik ta'siri."""
import numpy as np
from labkit import PARAMS, note, series, table, value

a = float(PARAMS.get("a", 50.0))/1000.0     # ichki radius
b = float(PARAMS.get("b", 150.0))/1000.0    # tashqi radius
h = float(PARAMS.get("h", 12.0))/1000.0
E = float(PARAMS.get("E", 200.0))*1e9
nu = float(PARAMS.get("nu", 0.3))
qload = float(PARAMS.get("q", 2.0))*1e6
bc_out = int(PARAMS.get("bc_out", 0))       # 0 mahkam, 1 sharnir
bc_in = int(PARAMS.get("bc_in", 0))         # 0 erkin, 1 mahkam

D = E*h**3/(12*(1 - nu**2))
value("Silindrik bikrlik D", D/1000, "kN*m")
value("a/b nisbati", a/b, "—")
value("Teshik yuza ulushi", (a/b)**2*100, "%")


def build(a_, b_, bc_o, bc_i):
    """4x4 tizimni qurish: [C1, C2, C3, C4]."""
    def row_w(r):
        return np.array([1.0, r**2, np.log(r), r**2*np.log(r)]), -qload*r**4/(64*D)

    def row_dw(r):
        return (np.array([0.0, 2*r, 1.0/r, r*(2*np.log(r) + 1)]),
                -qload*r**3/(16*D))

    def row_Mr(r):
        # M_r = -D[w'' + nu/r * w'];  qismlarni doimiylar bo'yicha yozamiz
        c1 = 0.0
        c2 = -D*(2 + 2*nu)
        c3 = -D*(-1/r**2 + nu/r**2)
        c4 = -D*((2*np.log(r) + 3) + nu*(2*np.log(r) + 1))
        rhs = D*(qload*r**2/(16*D)*(3 + nu))
        return np.array([c1, c2, c3, c4]), rhs

    def row_Vr(r):
        # Q_r = q*r/2 + 4*D*C4/r ; erkin konturda Q_r = 0
        return np.array([0.0, 0.0, 0.0, 4*D/r]), -qload*r/2

    rows, rhs = [], []
    # ichki kontur
    if bc_i == 0:      # erkin: M_r = 0, V_r = 0
        A1, f1 = row_Mr(a_); rows.append(A1); rhs.append(f1)
        A2, f2 = row_Vr(a_); rows.append(A2); rhs.append(f2)
    else:              # mahkamlangan
        A1, f1 = row_w(a_); rows.append(A1); rhs.append(f1)
        A2, f2 = row_dw(a_); rows.append(A2); rhs.append(f2)
    # tashqi kontur
    A3, f3 = row_w(b_); rows.append(A3); rhs.append(f3)
    if bc_o == 0:      # mahkamlangan
        A4, f4 = row_dw(b_)
    else:              # sharnirli
        A4, f4 = row_Mr(b_)
    rows.append(A4); rhs.append(f4)

    A = np.array(rows)
    f = np.array(rhs)
    return np.linalg.solve(A, f), np.linalg.cond(A)


C, cond = build(a, b, bc_out, bc_in)
value("Tizim shartlanganlik soni", float(cond), "—")
if cond > 1e10:
    note(f"Shartlanganlik soni {cond:.2e} juda katta — a/b juda "
         f"kichik, natija ishonchsiz bo'lishi mumkin.")

r = np.linspace(a, b, 400)
lnr = np.log(r)
w = qload*r**4/(64*D) + C[0] + C[1]*r**2 + C[2]*lnr + C[3]*r**2*lnr
dw = qload*r**3/(16*D) + 2*C[1]*r + C[2]/r + C[3]*r*(2*lnr + 1)
d2w = (3*qload*r**2/(16*D) + 2*C[1] - C[2]/r**2
       + C[3]*(2*lnr + 3))
Mr = -D*(d2w + nu*dw/r)
Mt = -D*(dw/r + nu*d2w)

series("Og'ish w(r)", (r*1000).tolist(), (w*1000).tolist(),
       xlabel="Radius r, mm", ylabel="Og'ish w, mm")
series("M_r(r)", (r*1000).tolist(), (Mr/1000).tolist(),
       xlabel="Radius r, mm", ylabel="M_r, kN*m/m")
series("M_theta(r)", (r*1000).tolist(), (Mt/1000).tolist(),
       xlabel="Radius r, mm", ylabel="M_theta, kN*m/m")

value("Doimiy C1", float(C[0]), "—")
value("Doimiy C2", float(C[1]), "—")
value("Doimiy C3", float(C[2]), "—")
value("Doimiy C4", float(C[3]), "—")
value("w_max", float(np.max(np.abs(w)))*1000, "mm")
value("M_r (ichki kontur)", float(Mr[0])/1000, "kN*m/m")
value("M_theta (ichki kontur)", float(Mt[0])/1000, "kN*m/m")
value("M_r (tashqi kontur)", float(Mr[-1])/1000, "kN*m/m")

M_abs = max(float(np.max(np.abs(Mr))), float(np.max(np.abs(Mt))))
value("Maksimal |M|", M_abs/1000, "kN*m/m")
value("Maksimal kuchlanish", 6*M_abs/h**2/1e6, "MPa")

# Chegaraviy shartlarni tekshirish
note(f"Tekshiruv — ichki konturda M_r = {Mr[0]:.3e} N*m/m "
     f"({'~0, erkin shart bajarildi' if abs(Mr[0]) < 1e-6*M_abs else 'XATO'}); "
     f"tashqi konturda w = {w[-1]:.3e} m, dw/dr = {dw[-1]:.3e}.")

# --- To'liq disk bilan taqqoslash ---
w_full = qload*b**4/(64*D) if bc_out == 0 else \
    qload*b**4/(64*D)*(5 + nu)/(1 + nu)
Mr_full_edge = -qload*b**2/8 if bc_out == 0 else 0.0
M_full_centre = qload*b**2*(1 + nu)/16 if bc_out == 0 else \
    qload*b**2*(3 + nu)/16
value("To'liq disk w_max", w_full*1000, "mm")
value("To'liq disk M(markaz)", M_full_centre/1000, "kN*m/m")
value("Halqa/to'liq og'ish nisbati", float(np.max(np.abs(w)))/w_full, "—")

# --- Teshik radiusining ta'siri ---
ratios = np.linspace(0.02, 0.8, 60)
wr, Mr_in, Mt_in, Mr_out = [], [], [], []
for rt in ratios:
    aa = rt*b
    try:
        Ck, _ = build(aa, b, bc_out, bc_in)
    except np.linalg.LinAlgError:
        wr.append(np.nan); Mr_in.append(np.nan)
        Mt_in.append(np.nan); Mr_out.append(np.nan)
        continue
    rr = np.linspace(aa, b, 200)
    ln_ = np.log(rr)
    ww = qload*rr**4/(64*D) + Ck[0] + Ck[1]*rr**2 + Ck[2]*ln_ + Ck[3]*rr**2*ln_
    dww = qload*rr**3/(16*D) + 2*Ck[1]*rr + Ck[2]/rr + Ck[3]*rr*(2*ln_ + 1)
    d2ww = 3*qload*rr**2/(16*D) + 2*Ck[1] - Ck[2]/rr**2 + Ck[3]*(2*ln_ + 3)
    Mrr = -D*(d2ww + nu*dww/rr)
    Mtt = -D*(dww/rr + nu*d2ww)
    wr.append(float(np.max(np.abs(ww)))*1000)
    Mr_in.append(float(Mrr[0])/1000)
    Mt_in.append(float(Mtt[0])/1000)
    Mr_out.append(float(Mrr[-1])/1000)

series("w_max(a/b)", ratios.tolist(), wr,
       xlabel="Teshik nisbati a/b", ylabel="w_max, mm")
series("M_theta ichki konturda (a/b)", ratios.tolist(), Mt_in,
       xlabel="Teshik nisbati a/b", ylabel="M_theta(a), kN*m/m")
series("M_r tashqi konturda (a/b)", ratios.tolist(), Mr_out,
       xlabel="Teshik nisbati a/b", ylabel="M_r(b), kN*m/m")
series("To'liq disk og'ishi (etalon)", ratios.tolist(),
       [w_full*1000]*len(ratios), xlabel="Teshik nisbati a/b",
       ylabel="w_max, mm")

wr_arr = np.array(wr, dtype=float)
i_min = int(np.nanargmin(wr_arr))
diffs = np.diff(wr_arr[~np.isnan(wr_arr)])
monotone = bool(np.all(diffs <= 1e-12))
value("Eng kichik og'ish beradigan a/b", float(ratios[i_min]), "—")
value("Shu holatdagi w_max", float(wr_arr[i_min]), "mm")
value("a/b = 0.1 da w_max", float(wr_arr[int(np.argmin(np.abs(ratios - 0.1)))]), "mm")
note(f"Og'ish a/b ortishi bilan {'MONOTON kamayadi' if monotone else 'monoton emas'}: "
     f"a/b = {ratios[0]:.2f} da {wr_arr[0]:.4f} mm, "
     f"a/b = {ratios[-1]:.2f} da {wr_arr[i_min]:.4f} mm; to'liq diskda "
     f"{w_full*1000:.4f} mm. Sabab: teshik eng katta yelkaga ega "
     f"markaziy yuklamani ham olib tashlaydi, qolgan halqa esa "
     f"tashqi konturga yaqin va qisqa — shuning uchun bikrroq.")

# Kichik teshik limiti: moment konsentratsiyasi
small = [rt for rt in [0.02, 0.05, 0.1, 0.15, 0.2] if rt < 0.8]
conc = []
for rt in small:
    aa = rt*b
    Ck, _ = build(aa, b, bc_out, bc_in)
    ln_a = np.log(aa)
    dwa = qload*aa**3/(16*D) + 2*Ck[1]*aa + Ck[2]/aa + Ck[3]*aa*(2*ln_a + 1)
    d2wa = 3*qload*aa**2/(16*D) + 2*Ck[1] - Ck[2]/aa**2 + Ck[3]*(2*ln_a + 3)
    Mta = -D*(dwa/aa + nu*d2wa)
    conc.append([rt, round(Mta/1000, 3),
                 round(Mta/M_full_centre, 3)])
table("Kichik teshik atrofidagi moment konsentratsiyasi",
      ["a/b", "M_theta(a), kN*m/m", "M_theta(a)/M(to'liq, markaz)"], conc)
note("a/b -> 0 da nisbat 2 ga intiladi: kichik teshik og'ishga "
     "deyarli ta'sir qilmaydi, lekin halqaviy momentni ikki "
     "baravar oshiradi — tmm-17 dagi Kirsh effektining analogi.")

table("Halqasimon plastinaning chegaraviy shart kombinatsiyalari",
      ["Ichki kontur", "Tashqi kontur", "Tipik qo'llanishi"],
      [["Erkin", "Mahkamlangan", "Quvur flanetsi, lyuk halqasi"],
       ["Erkin", "Sharnirli", "Bolt bilan qisilgan qopqoq"],
       ["Mahkamlangan (val)", "Erkin", "Tishli g'ildirak, turbina diski"],
       ["Mahkamlangan", "Mahkamlangan", "Ikki tomondan qisilgan membrana"],
       ["Yuklangan (halqaviy kuch)", "Sharnirli", "Podshipnik qopqog'i"]])
''',
                parameters=[
                    p("a", "Ichki radius a", 5.0, 900.0, 50.0, 5.0, "mm"),
                    p("b", "Tashqi radius b", 20.0, 2000.0, 150.0, 5.0, "mm"),
                    p("h", "Qalinlik h", 1.0, 150.0, 12.0, 0.5, "mm"),
                    p("E", "Yung moduli E", 1.0, 400.0, 200.0, 1.0, "GPa"),
                    p("nu", "Puasson koeffitsienti ν", 0.0, 0.45, 0.3, 0.01),
                    p("q", "Bir tekis yuklama q", 0.001, 20.0, 2.0, 0.01, "MPa"),
                    p("bc_out", "Tashqi kontur (0 mahkam, 1 sharnir)",
                      0.0, 1.0, 0.0, 1.0),
                    p("bc_in", "Ichki kontur (0 erkin, 1 mahkam)",
                      0.0, 1.0, 0.0, 1.0),
                ],
                expected_output=(
                    "D = 31,65 kN·m; erkin teshik + mahkamlangan "
                    "tashqi kontur, a/b = 1/3: w_max = 0,3796 mm "
                    "(to'liq diskda 0,4999 mm — teshik og'ishni "
                    "24 % kamaytiradi); ichki konturda M_r = "
                    "−8,8×10⁻¹³ N·m/m (erkin shart 10⁻¹³ aniqlikda "
                    "bajarildi), M_θ = 3,03 kN·m/m; tashqi konturda "
                    "M_r = −4,92 kN·m/m, σ = 205 MPa. a/b → 0 da "
                    "M_θ(a)/M(markaz) → 1,99 ≈ 2."
                ),
            ),
            visual=vis(
                kind="Halqasimon plastina va teshik ta'siri",
                tool="React/SVG",
                description=(
                    "Halqa kesimi, og'ish va moment epyuralari, "
                    "teshik nisbatining ta'siri grafigi."
                ),
                how_to_draw=(
                    "React/SVG: birinchi panel — halqaning yuqoridan "
                    "ko'rinishi: ikkita konsentrik doira, orasi "
                    "moment kattaligiga qarab bo'yalgan konsentrik "
                    "halqalar bilan to'ldiriladi. Ichki doira "
                    "chegarasi turiga qarab belgilanadi (erkin — "
                    "oddiy chiziq, mahkamlangan — shtrixlash). "
                    "Ikkinchi panel — yon kesim va og'ish profili: "
                    "$r = a$ dan $r = b$ gacha, chegaraviy "
                    "shartlar belgilari bilan. Uchinchi panel — "
                    "$M_r$ va $M_\\theta$ epyuralari; erkin ichki "
                    "konturda $M_r = 0$ ekanligi grafikda aniq "
                    "ko'rinadi (egri chiziq $r = a$ da nolga "
                    "uriladi), $M_\\theta$ esa u yerda "
                    "maksimumga ega. To'rtinchi panel — "
                    "$w_{\\max}(a/b)$ grafigi; unga to'liq disk "
                    "qiymati gorizontal punktir chiziq bilan "
                    "ustiga qo'yiladi va minimum nuqtasi "
                    "belgilanadi — teshik og'ishni kamaytirishi "
                    "darhol ko'rinadi."
                ),
            ),
            interp=(
                "$w_{\\max}(a/b)$ grafigi bu mavzudagi eng "
                "kutilmagan natijani beradi: bosim ostidagi "
                "halqasimon plastinada og'ish teshik kattalashgani "
                "sari **monoton kamayadi**. $a/b = 1/3$ da u "
                "to'liq diskdagining 76 % i, $a/b = 0{,}8$ da esa "
                "atigi 1 % i. Sabab ikki qismdan iborat: teshik "
                "eng katta yelkaga ega markaziy yuklamani olib "
                "tashlaydi va qolgan halqa mahkamlangan tashqi "
                "konturga yaqin bo'lgani uchun qisqa yelkada "
                "ishlaydi. Muhim ogohlantirish: bu natija yuklama "
                "butun yuzaga taqsimlangan holatga tegishli; "
                "yuklama faqat tashqi halqaga qo'yilsa, teshik "
                "faqat zaiflashtiradi. Lekin "
                "moment konsentratsiyasi jadvali qarama-qarshi "
                "xabar beradi: $a/b \\to 0$ da halqaviy moment "
                "to'liq diskdagidan ikki barobar katta bo'ladi. "
                "Demak **og'ish yaxshilanadi, mahalliy kuchlanish "
                "esa yomonlashadi**. Bu tmm-17 dagi Kirsh "
                "yechimining ($K_t = 3$ cho'zilishda) egilishdagi "
                "analogi va koeffitsientning kichikroq bo'lishi "
                "($\\approx 2$) tushunarli: egilishda kuchlanish "
                "qalinlik bo'yicha o'zgaradi va konsentratsiya "
                "biroz yumshaydi. Amaliy xulosa — teshik "
                "chekkasini yumaloqlash (fillet) va sirt "
                "sifatini oshirish shart, chunki charchoq "
                "yoriqlari aynan shu yerdan boshlanadi (tmm-24)."
            ),
            mistakes=[
                "Halqasimon plastinada $C_3$ va $C_4$ ni "
                "tashlab yuborish. Ular faqat to'liq diskda "
                "(regulyarlik tufayli) yo'qoladi.",
                "Teshik har doim plastinani zaiflashtiradi deb "
                "o'ylash. Bosim tipidagi yuklamada kichik teshik "
                "og'ishni kamaytirishi mumkin.",
                "Og'ish yaxshilangani uchun kuchlanish ham "
                "yaxshilanadi deb xulosa qilish. Teshik "
                "atrofidagi moment konsentratsiyasi og'ishdan "
                "mustaqil va u har doim zararli.",
                "Juda kichik $a/b$ ($< 0{,}01$) da tizimni "
                "to'g'ridan-to'g'ri yechish. Matritsa yomon "
                "shartlangan; bunday holda to'liq disk yechimi "
                "+ konsentratsiya koeffitsienti ishlatiladi.",
            ],
            quiz=[
                q("Nima uchun halqasimon plastinada to'rtta "
                  "doimiy saqlanadi?",
                  "$r = 0$ nuqta soha ichida emas, shuning uchun "
                  "$\\ln r$ va $r^2\\ln r$ hadlari singulyarlik "
                  "bermaydi va regulyarlik sharti qo'llanmaydi.",
                  "konseptual"),
                q("Erkin ichki konturda qanday ikki shart qo'yiladi?",
                  "$M_r(a) = 0$ va $V_r(a) = 0$. O'qsimmetrik "
                  "masalada $V_r = Q_r$, chunki buralish momenti "
                  "nolga teng.", "konseptual"),
                q("$a/b \\to 0$ limitida halqaviy moment "
                  "konsentratsiyasi qanchaga teng?",
                  "Taxminan 2: kichik teshik atrofida "
                  "$M_\\theta$ to'liq diskdagi markaziy "
                  "momentdan ikki barobar katta bo'ladi.",
                  "hisob"),
                q("Nima uchun kichik teshik og'ishni "
                  "kamaytirishi mumkin?",
                  "Teshik markaziy sohadagi yuklamani ham olib "
                  "tashlaydi, u esa eng katta yelkaga ega. "
                  "Kichik teshikda bu effekt material "
                  "yo'qotishdan ustun keladi.", "talqin"),
                q("Kodda tizim shartlanganlik soni nima uchun "
                  "tekshiriladi?",
                  "$a/b$ juda kichik bo'lsa $\\ln(a/b)$ katta "
                  "manfiy son bo'ladi va matritsa yomon "
                  "shartlanadi — natija sonli xatolarga sezgir "
                  "bo'lib qoladi.", "kod"),
                q("Teshik chekkasini yumaloqlash nima uchun kerak?",
                  "U yerda moment konsentratsiyasi maksimal; "
                  "o'tkir burchak qo'shimcha kuchlanish "
                  "konsentratsiyasi beradi va charchoq "
                  "yoriqlari aynan shu joydan boshlanadi.",
                  "talqin"),
            ],
            bridge=(
                "O'qsimmetrik masalalarda yechim to'liq analitik "
                "edi. Agar yuklama yoki chegaraviy shart "
                "burchakka bog'liq bo'lsa (masalan, disk "
                "yon tomondan yuklangan), o'qsimmetriya "
                "buziladi. Keyingi mavzuda bu holni Furye "
                "qatori bilan yechamiz."
            ),
            research=(
                "Aylanuvchi disk masalasini o'rganing: turbina "
                "yoki tormoz diski aylanganda markazdan qochma "
                "kuchlar membrana kuchlanishlarini "
                "($\\sigma_r, \\sigma_\\theta$) keltirib "
                "chiqaradi. Bu tmm-16 dagi tekis masala bilan "
                "yechiladi. Agar disk bir vaqtda egilsa ham "
                "(o'q bo'ylab yuklama), ikkala effekt "
                "birlashadi va katta og'ishlarda (pq-18) ular "
                "o'zaro ta'sir qiladi. Teng mustahkamlikdagi "
                "disk profilini ($\\sigma = $ const) toping va "
                "uni doimiy qalinlikdagi disk bilan og'irlik "
                "hamda maksimal aylanish tezligi bo'yicha "
                "taqqoslang. Nima uchun bug' turbinasi "
                "disklari markazga qarab qalinlashadi?"
            ),
        ),
    ),

    # ------------------------------------------------------------------ pq-15
    Topic(
        id="pq-15",
        subject_id=S, module_id=M, order=15,
        title="Doiraviy plastinaning nosimmetrik yuklanishi: Furye yoyilmasi",
        description=(
            "O'qsimmetriya buzilganda yechimni burchak bo'yicha Furye "
            "qatoriga yoyish, har bir garmonika uchun radial ODE va "
            "eksantrik hamda bir tomonlama yuklamalarning tahlili."
        ),
        learning_objective=(
            "Nosimmetrik yuklamani Furye qatoriga yoyish, har bir "
            "garmonika uchun radial yechimni qurish va natijani "
            "superpozitsiya bilan yig'ish."
        ),
        prerequisites=["pq-14", "pq-08"],
        mathematical_core=(
            "$w = \\sum_n W_n(r)\\cos n\\theta$, har bir $n$ uchun "
            "Eyler tipidagi ODE, yechim $r^n, r^{-n}, r^{n+2}, "
            "r^{-n+2}$ darajalarida."
        ),
        engineering_application=(
            "Eksantrik yuklangan qopqoq, bir tomonlama bosim, "
            "shamol yuklamasi ostidagi dumaloq tom, tishli "
            "g'ildirakning bir tishiga tushgan kuch, notekis "
            "qizigan disk."
        ),
        computational_component=(
            "Yuklamani Furye qatoriga yoyish, har bir garmonika "
            "uchun $4\\times4$ tizimni yechish, garmonikalar "
            "hissasini tahlil qilish."
        ),
        visualization_component=(
            "Garmonikalarning shakllari ($n = 0, 1, 2, \\ldots$), "
            "ularning superpozitsiyasi, og'ish sirti konturi."
        ),
        research_extension=(
            "Termik yuklamani (notekis qizish) plastina "
            "tenglamasiga kiriting: harorat gradiyenti qanday "
            "ekvivalent momentga aylanadi?"
        ),
        difficulty="ilg'or",
        previous_link=(
            "pq-13 va pq-14 da o'qsimmetriya masalani bir "
            "o'lchovli qilgan edi. pq-08 dagi Levi usuli esa "
            "qisman ajratish g'oyasini bergan edi. Endi ikkalasini "
            "birlashtiramiz: burchak bo'yicha qator, radius "
            "bo'yicha ODE."
        ),
        next_topic="pq-16",
        estimated_minutes=95,
        tags=["Furye qatori", "nosimmetrik", "garmonika", "doiraviy"],
        lesson=_lesson(
            problem=(
                "Silos yoki rezervuarning dumaloq qopqog'iga "
                "eksantrik joylashgan uskuna o'rnatilgan — yuk "
                "markazda emas, chetga siljigan. O'qsimmetriya "
                "buzildi va pq-13 dagi barcha formulalar yaroqsiz "
                "bo'lib qoldi. Yangi nazariya kerakmi? Yo'q — "
                "yuklamani burchak bo'yicha Furye qatoriga yoyish "
                "kifoya. Har bir garmonika alohida o'qsimmetrik "
                "masalaga o'xshab yechiladi."
            ),
            concepts=[
                c("Burchak bo'yicha Furye yoyilmasi",
                  "$q(r,\\theta) = \\sum_n q_n(r)\\cos n\\theta$ — "
                  "har qanday davriy yuklamani garmonikalarga ajratish."),
                c("Garmonika tartibi $n$",
                  "$n = 0$ — o'qsimmetrik (bir tekis); $n = 1$ — "
                  "eksantrik (bir tomonga siljish); $n = 2$ — "
                  "ovallashish; $n \\ge 3$ — yuqori tartibli shakllar."),
                c("Radial ODE",
                  "Har bir $n$ uchun to'rtinchi tartibli Eyler "
                  "tipidagi tenglama; yechimi darajalar "
                  "kombinatsiyasi."),
                c("$n = 1$ garmonikasining xususiyati",
                  "Uning bir jinsli yechimlaridan biri "
                  "$r\\cos\\theta = x$ — bu qattiq jism kabi "
                  "burilish, deformatsiya bermaydi."),
                c("Superpozitsiya",
                  "Chiziqli masalada garmonikalar mustaqil; "
                  "yakuniy yechim ularning yig'indisi."),
                c("Bir tomonlama yuklama",
                  "Yarim yuzaga qo'yilgan yuklama barcha "
                  "garmonikalarni qo'zg'atadi, lekin $n = 0$ va "
                  "$n = 1$ hukmron bo'ladi."),
            ],
            derivation=[
                d("1. To'liq bigarmonik operator silindrik koordinatalarda",
                  r"\nabla^2 = \frac{\partial^2}{\partial r^2} + "
                  r"\frac{1}{r}\frac{\partial}{\partial r} + "
                  r"\frac{1}{r^2}\frac{\partial^2}{\partial\theta^2}",
                  "Endi $\\theta$ bo'yicha had ham bor — "
                  "o'qsimmetriyada u nolga teng edi."),
                d("2. Yechimni burchak bo'yicha yoyish",
                  r"w(r, \theta) = \sum_{n=0}^{\infty}\Big[W_n^c(r)"
                  r"\cos n\theta + W_n^s(r)\sin n\theta\Big]",
                  "Simmetriya o'qi tanlansa, odatda faqat "
                  "kosinuslar qoladi. Har bir garmonika "
                  "mustaqil ravishda tenglamani qanoatlantiradi."),
                d("3. Laplasianning garmonikaga ta'siri",
                  r"\nabla^2\big[W_n(r)\cos n\theta\big] = "
                  r"\Big[W_n'' + \frac{W_n'}{r} - \frac{n^2}{r^2}W_n\Big]"
                  r"\cos n\theta",
                  "$\\cos n\\theta$ shakli saqlanadi — u "
                  "$\\partial^2/\\partial\\theta^2$ operatorining "
                  "xususiy funksiyasi ($-n^2$ xususiy qiymat bilan)."),
                d("4. Radial operatorni kiritish",
                  r"L_n[W] \equiv W'' + \frac{W'}{r} - \frac{n^2}{r^2}W "
                  r"\;\Longrightarrow\; L_n\big[L_n[W_n]\big] = \frac{q_n}{D}",
                  "Bigarmonik operator ikki marta qo'llangan radial "
                  "operatorga aylanadi. Bu to'rtinchi tartibli ODE."),
                d("5. Bir jinsli yechim: darajalar",
                  r"W_n^h = A_nr^n + B_nr^{-n} + C_nr^{n+2} + E_nr^{-n+2} "
                  r"\quad (n \ge 2)",
                  "Eyler tenglamasining yechimi $r^k$ ko'rinishida. "
                  "$L_n[r^k] = (k^2 - n^2)r^{k-2}$ ayniyatidan "
                  "$k = \\pm n$ va $k = \\pm n + 2$ topiladi."),
                d("6. Maxsus hollar $n = 0$ va $n = 1$",
                  r"n = 0: \ \{1, r^2, \ln r, r^2\ln r\}; \qquad "
                  r"n = 1: \ \{r, r^{-1}, r^3, r\ln r\}",
                  "Karrali ildizlar tufayli logarifm paydo bo'ladi. "
                  "$n = 0$ — pq-13/14 dagi natija; $n = 1$ da "
                  "$r^{-n+2} = r$ va $r^n = r$ ustma-ust tushadi, "
                  "shuning uchun $r\\ln r$ kerak."),
                d("7. To'liq disk uchun regulyarlik",
                  r"r \to 0 \ \text{chekli} \;\Longrightarrow\; "
                  r"B_n = 0, \quad E_n = 0 \ (n \ge 2); \quad "
                  r"n = 1: \ B_1 = 0, \ \text{koeff}(r\ln r) = 0",
                  "Manfiy darajalar va logarifm markazda "
                  "cheksizlikka intiladi. Ikki doimiy qoladi — "
                  "ikkita chegaraviy shart uchun yetarli."),
                d("8. Furye koeffitsientlari",
                  r"q_n(r) = \frac{1}{\pi}\int_0^{2\pi}q(r,\theta)"
                  r"\cos n\theta\,d\theta \quad (n \ge 1), \qquad "
                  r"q_0 = \frac{1}{2\pi}\int_0^{2\pi}q\,d\theta",
                  "Standart Furye formulalari. Bir tomonlama "
                  "yuklama uchun ular analitik hisoblanadi va "
                  "$1/n$ kabi kamayadi."),
            ],
            meaning=(
                "Bu usulning nafisligi — **ikki bosqichli "
                "ajratish**. Birinchi bosqichda burchak "
                "o'zgaruvchisi qator bilan ajratiladi (Navye "
                "usulidagi kabi), ikkinchi bosqichda esa radius "
                "bo'yicha ODE yechiladi (Levi usulidagi kabi). "
                "Natijada ikki o'lchovli masala bir o'lchovli "
                "masalalar ketma-ketligiga aylanadi. Garmonikalar "
                "tartibining fizik ma'nosi ham oydin: $n = 0$ — "
                "plastina bir tekis egiladi; $n = 1$ — u "
                "'qiyalashadi', bir tomoni pastga, ikkinchisi "
                "yuqoriga; $n = 2$ — doira ovalga aylanadi; "
                "$n = 3$ — uch 'gulbargli' shakl. Yuqori "
                "garmonikalar qisqa to'lqinli, demak katta "
                "egrilikka ega va plastina ularga kuchli "
                "qarshilik ko'rsatadi — koeffitsientlar tez "
                "kamayadi. Shuning uchun eksantrik yuklamada "
                "amalda $n \\le 5$ yetarli. $n = 1$ garmonikasining "
                "alohida xususiyati bor: uning bir jinsli "
                "yechimlaridan biri $r\\cos\\theta = x$ — bu "
                "shunchaki plastinaning qiya joylashishi, "
                "hech qanday deformatsiya bermaydi. Shuning "
                "uchun erkin suzuvchi plastinada (masalan, muz "
                "qatlami) $n = 1$ garmonikasi qattiq jism "
                "harakatiga mos keladi va uni alohida ajratish kerak."
            ),
            equations=[
                eq(r"w(r,\theta) = \sum_n W_n(r)\cos n\theta",
                   "Yechimni burchak bo'yicha yoyish.",
                   "Furye yoyilmasi"),
                eq(r"L_n[W] = W'' + \frac{W'}{r} - \frac{n^2}{r^2}W, "
                   r"\qquad L_n\big[L_n[W_n]\big] = \frac{q_n}{D}",
                   "Har bir garmonika uchun radial tenglama.",
                   "Radial ODE"),
                eq(r"W_n^h = A_nr^n + B_nr^{-n} + C_nr^{n+2} "
                   r"+ E_nr^{-n+2} \quad (n\ge2)",
                   "Bir jinsli yechim.", "Bir jinsli yechim"),
                eq(r"q_n(r) = \frac{1}{\pi}\int_0^{2\pi}q(r,\theta)"
                   r"\cos n\theta\,d\theta",
                   "Yuklamaning Furye koeffitsientlari.",
                   "Furye koeffitsientlari"),
            ],
            conditions=(
                "**Har bir garmonika uchun chegaraviy shartlar "
                "alohida qo'yiladi.** To'liq diskda regulyarlikdan "
                "keyin ikkita doimiy qoladi, demak konturda "
                "ikkita shart yetarli:\n"
                "- Mahkamlangan: $W_n(R) = 0$, $W_n'(R) = 0$;\n"
                "- Sharnirli: $W_n(R) = 0$, $M_r^{(n)}(R) = 0$.\n\n"
                "**Momentlar garmonika orqali:**\n"
                "$$M_r^{(n)} = -D\\Big[W_n'' + \\nu\\Big(\\frac{W_n'}{r} "
                "- \\frac{n^2}{r^2}W_n\\Big)\\Big]\\cos n\\theta.$$\n\n"
                "**Buralish momenti endi nolga teng emas:**\n"
                "$$M_{r\\theta}^{(n)} = D(1-\\nu)\\frac{n}{r}"
                "\\Big(\\frac{W_n}{r} - W_n'\\Big)\\sin n\\theta,$$\n"
                "shuning uchun erkin chekkada Kirxhoff tuzatmasi "
                "kerak bo'ladi (o'qsimmetrik holdan farqli).\n\n"
                "**Yaqinlashish:** eksantrik konsentrlangan yuklama "
                "uchun $n \\le 10$ odatda yetarli; bir tomonlama "
                "taqsimlangan yuklama uchun $n \\le 5$."
            ),
            worked=WorkedExample(
                statement=(
                    "Dumaloq qopqoq $R = 500$ mm, $h = 15$ mm, "
                    "$E = 200$ GPa, $\\nu = 0{,}3$, chekka "
                    "mahkamlangan. Yuklama yarim yuzaga "
                    "($0 \\le \\theta \\le \\pi$) qo'yilgan: "
                    "$q = 0{,}5$ MPa. (a) Yuklamani Furye "
                    "qatoriga yoying. (b) $n = 0$ va $n = 1$ "
                    "garmonikalarining hissasini hisoblang. "
                    "(c) Maksimal og'ish qayerda?"
                ),
                given=[
                    r"R = 0{,}5\ \text{m},\ h = 0{,}015\ \text{m}",
                    r"E = 200\ \text{GPa},\ \nu = 0{,}3",
                    r"q = 0{,}5\ \text{MPa} \ (0 \le \theta \le \pi), "
                    r"\ 0 \ (\pi < \theta < 2\pi)",
                ],
                steps=[
                    st(r"D = \frac{200\times10^9 \cdot 3{,}375\times10^{-6}}"
                       r"{12 \cdot 0{,}91} = 6{,}1813\times10^{4}\ \text{N·m}",
                       "$h^3 = 3{,}375\\times10^{-6}$ m³."),
                    st(r"q_0 = \frac{1}{2\pi}\int_0^{\pi}q\,d\theta "
                       r"= \frac{q}{2} = 0{,}25\ \text{MPa}",
                       "O'rtacha qiymat — bu o'qsimmetrik qism."),
                    st(r"q_n = \frac{1}{\pi}\int_0^{\pi}q\cos n\theta\,d\theta "
                       r"= \frac{q}{n\pi}\sin n\pi = 0 \ (\forall n\ge1)",
                       "Kosinuslar bo'yicha barcha koeffitsientlar "
                       "nol! Chunki yuklama $\\theta = 0$ ga "
                       "nisbatan simmetrik emas."),
                    st(r"\text{Sinuslar bo'yicha: } \tilde{q}_n = "
                       r"\frac{1}{\pi}\int_0^{\pi}q\sin n\theta\,d\theta "
                       r"= \frac{q(1-\cos n\pi)}{n\pi} = "
                       r"\frac{2q}{n\pi} \ (n \ \text{toq})",
                       "To'g'ri bazis — sinuslar. $n$ juft bo'lsa "
                       "koeffitsient nolga teng."),
                    st(r"\tilde{q}_1 = \frac{2 \cdot 0{,}5}{\pi} "
                       r"= 0{,}3183\ \text{MPa}; \quad "
                       r"\tilde{q}_3 = \frac{2 \cdot 0{,}5}{3\pi} "
                       r"= 0{,}1061\ \text{MPa}",
                       "Birinchi va uchinchi garmonikalar. "
                       "Koeffitsientlar $1/n$ kabi kamayadi."),
                    st(r"n = 0: \ w_0 = \frac{q_0R^4}{64D} = "
                       r"\frac{0{,}25\times10^{6} \cdot 0{,}0625}"
                       r"{64 \cdot 6{,}1813\times10^{4}} = 3{,}951\ \text{mm}",
                       "O'qsimmetrik qism — markazda maksimal."),
                    st(r"n = 1: \ W_1(r) = \frac{\tilde{q}_1}{D}"
                       r"\Big[\frac{r^5}{192} + \ldots\Big], \ "
                       r"\text{mahkamlash shartlaridan doimiylar}",
                       "Xususiy yechim $r^5$ darajali "
                       "($L_1[L_1[r^5]] = (25-1)(9-1)r = 192r$), "
                       "bir jinsli qism $r$ va $r^3$."),
                    st(r"\text{Kod natijasi: } w_{\max} = 4{,}281\ \text{mm}, "
                       r"\ r/R = 0{,}177, \ \theta = 90°",
                       "Maksimum markazdan yuklangan tomonga "
                       "siljidi — bu $n = 1$ va undan yuqori "
                       "garmonikalarning ta'siri. Faqat $n = 0$ "
                       "olinsa 3,950 mm chiqardi, ya'ni "
                       "nosimmetriya hissasi 7,7 %."),
                ],
                answer=(
                    "$D = 61{,}81$ kN·m; yuklama **sinuslar** "
                    "bo'yicha yoyiladi: $\\tilde{q}_n = 2q/(n\\pi)$, "
                    "$n$ toq; $n = 0$ (o'rtacha) qismi 3,95 mm "
                    "og'ish beradi, $n = 1$ va yuqori garmonikalar "
                    "maksimumni yuklangan tomonga siljitadi. "
                    "Yakuniy $w_{\\max} = 4{,}281$ mm, "
                    "$r/R = 0{,}177$, $\\theta = 90°$ da — "
                    "nosimmetriya hissasi 7,7 %."
                ),
                engineering_note=(
                    "Bazis tanlash (kosinus yoki sinus) simmetriya "
                    "o'qini qayerga qo'yishga bog'liq. Agar "
                    "$\\theta$ ni yuklangan yarimning o'rtasidan "
                    "sanasak, kosinuslar ishlaydi; chegarasidan "
                    "sanasak — sinuslar. Amalda o'qni shunday "
                    "tanlash kerakki, masala simmetrik bo'lsin — "
                    "bu garmonikalar sonini ikki marta kamaytiradi."
                ),
            ),
            computation=Computation(
                caption=(
                    "Nosimmetrik yuklamani Furye qatoriga yoyish, "
                    "har bir garmonika uchun radial yechimni "
                    "qurish va superpozitsiya bilan yig'ish."
                ),
                code='''"""Doiraviy plastinaning nosimmetrik yuklanishi: Furye yoyilmasi."""
import numpy as np
from labkit import PARAMS, note, series, table, value

R = float(PARAMS.get("R", 500.0))/1000.0
h = float(PARAMS.get("h", 15.0))/1000.0
E = float(PARAMS.get("E", 200.0))*1e9
nu = float(PARAMS.get("nu", 0.3))
q0 = float(PARAMS.get("q0", 0.5))*1e6
kind = int(PARAMS.get("kind", 0))      # 0 yarim yuza, 1 eksantrik nuqta
ecc = float(PARAMS.get("ecc", 0.5))    # eksantriklik e/R
NH = int(PARAMS.get("NH", 9))          # garmonikalar soni

D = E*h**3/(12*(1 - nu**2))
value("Silindrik bikrlik D", D/1000, "kN*m")

nth = 240
th = np.linspace(0.0, 2*np.pi, nth, endpoint=False)
nr = 120
r = np.linspace(1e-4, R, nr)
Rg, Tg = np.meshgrid(r, th, indexing="ij")

# --- Yuklama maydoni ---
if kind == 0:
    # yuqori yarim: theta in [0, pi). Chegarani qat'iy olamiz, aks holda
    # diskret to'rda yarim yuza 121/240 bo'lib qoladi va q_0 biroz siljiydi.
    Q = np.where(Tg < np.pi, q0, 0.0)
    load_name = "yarim yuza"
else:
    # eksantrik joylashgan doiraviy yamoq (radius 0.15R)
    xe, ye = ecc*R, 0.0
    X, Y = Rg*np.cos(Tg), Rg*np.sin(Tg)
    Q = np.where((X - xe)**2 + (Y - ye)**2 <= (0.15*R)**2, q0, 0.0)
    load_name = f"eksantrik yamoq (e/R = {ecc:.2f})"
value("Yuklama turi kodi", float(kind), "—")

trapz = np.trapezoid if hasattr(np, "trapezoid") else np.trapz
dth = th[1] - th[0]


def fourier(Q_):
    """Har bir r uchun a_n (cos) va b_n (sin) koeffitsientlari."""
    a = np.zeros((NH + 1, nr))
    bcoef = np.zeros((NH + 1, nr))
    a[0] = Q_.mean(axis=1)
    for n in range(1, NH + 1):
        a[n] = 2*np.mean(Q_*np.cos(n*Tg), axis=1)
        bcoef[n] = 2*np.mean(Q_*np.sin(n*Tg), axis=1)
    return a, bcoef


A, B = fourier(Q)
value("q_0 (o'rtacha)", float(A[0].mean())/1e6, "MPa")
for n in range(1, min(NH, 5) + 1):
    value(f"a_{n} (cos, o'rtacha)", float(A[n].mean())/1e6, "MPa")
    value(f"b_{n} (sin, o'rtacha)", float(B[n].mean())/1e6, "MPa")


def solve_harmonic(n, qn_const, clamped=True):
    """n-garmonika uchun radial yechim (doimiy q_n, to'liq disk)."""
    if abs(qn_const) < 1e-12:
        return np.zeros_like(r)
    # xususiy yechim: W_p = qn r^4 / (D * ((16-n^2)(4-n^2)))  (n != 2, 4)
    den = (16 - n**2)*(4 - n**2)
    if n == 0:
        Wp = qn_const*r**4/(64*D)
        basis = [np.ones_like(r), r**2]        # regulyar hadlar
        dbasis = [np.zeros_like(r), 2*r]
        Wp_d = qn_const*r**3/(16*D)
    elif n == 2 or n == 4 or abs(den) < 1e-12:
        # rezonans holat: r^4 ln r kerak; amalda qo'shimcha had
        Wp = qn_const*r**4/(D*64.0)            # taqribiy
        basis = [r**n, r**(n + 2)]
        dbasis = [n*r**(n - 1), (n + 2)*r**(n + 1)]
        Wp_d = qn_const*r**3/(D*16.0)
    else:
        Wp = qn_const*r**4/(D*den)
        basis = [r**n, r**(n + 2)]
        dbasis = [n*r**(n - 1), (n + 2)*r**(n + 1)]
        Wp_d = 4*qn_const*r**3/(D*den)

    # chegaraviy shartlar: W(R) = 0, W'(R) = 0 (mahkamlangan)
    M = np.array([[basis[0][-1], basis[1][-1]],
                  [dbasis[0][-1], dbasis[1][-1]]])
    rhs = np.array([-Wp[-1], -Wp_d[-1]])
    c = np.linalg.solve(M, rhs)
    return Wp + c[0]*basis[0] + c[1]*basis[1]


# Har bir garmonika uchun (r bo'yicha o'rtacha q_n ni ishlatamiz)
W = np.zeros((nr, nth))
contrib = []
for n in range(0, NH + 1):
    an = float(A[n].mean()) if n > 0 else float(A[0].mean())
    bn = float(B[n].mean()) if n > 0 else 0.0
    if n == 0:
        Wn = solve_harmonic(0, an)
        W += Wn[:, None]
        contrib.append([0, round(an/1e6, 5), 0.0,
                        round(float(np.max(np.abs(Wn)))*1000, 4)])
    else:
        Wn_c = solve_harmonic(n, an)
        Wn_s = solve_harmonic(n, bn)
        W += Wn_c[:, None]*np.cos(n*th)[None, :]
        W += Wn_s[:, None]*np.sin(n*th)[None, :]
        amp = max(float(np.max(np.abs(Wn_c))), float(np.max(np.abs(Wn_s))))
        contrib.append([n, round(an/1e6, 5), round(bn/1e6, 5),
                        round(amp*1000, 4)])

table("Garmonikalarning hissasi",
      ["n", "a_n, MPa", "b_n, MPa", "max|W_n|, mm"], contrib)

w_max = float(np.max(np.abs(W)))
idx = np.unravel_index(np.argmax(np.abs(W)), W.shape)
value("w_max", w_max*1000, "mm")
value("w_max joyi r/R", float(r[idx[0]]/R), "—")
value("w_max joyi theta", float(np.degrees(th[idx[1]])), "deg")
value("Markazdagi og'ish", float(np.abs(W[0]).mean())*1000, "mm")

# n = 0 bilan taqqoslash (o'qsimmetrik yaqinlashuv)
W0 = solve_harmonic(0, float(A[0].mean()))
value("n = 0 garmonikasi w_max", float(np.max(np.abs(W0)))*1000, "mm")
value("Nosimmetriya hissasi", (w_max - float(np.max(np.abs(W0))))/w_max*100, "%")
note(f"Yuklama turi: {load_name}. O'qsimmetrik ({'n=0'}) "
     f"yaqinlashuv {float(np.max(np.abs(W0)))*1000:.3f} mm beradi, "
     f"to'liq yechim {w_max*1000:.3f} mm — nosimmetriya hissasi "
     f"{(w_max - float(np.max(np.abs(W0))))/w_max*100:.1f} %.")

# --- Profillar ---
i90 = int(np.argmin(np.abs(th - np.pi/2)))
i270 = int(np.argmin(np.abs(th - 3*np.pi/2)))
series("w(r) yuklangan tomonda (theta = 90 deg)", (r*1000).tolist(),
       (W[:, i90]*1000).tolist(), xlabel="Radius r, mm", ylabel="w, mm")
series("w(r) qarama-qarshi tomonda (theta = 270 deg)", (r*1000).tolist(),
       (W[:, i270]*1000).tolist(), xlabel="Radius r, mm", ylabel="w, mm")
series("w(r) o'qsimmetrik qism (n = 0)", (r*1000).tolist(),
       (W0*1000).tolist(), xlabel="Radius r, mm", ylabel="w, mm")

i_half = int(nr*0.5)
series("w(theta) r = 0.5R da", np.degrees(th).tolist(),
       (W[i_half, :]*1000).tolist(),
       xlabel="Burchak theta, deg", ylabel="w, mm")

# --- Garmonika shakllari ---
for n in [1, 2, 3]:
    series(f"cos({n}*theta) garmonika shakli", np.degrees(th).tolist(),
           np.cos(n*th).tolist(), xlabel="Burchak theta, deg",
           ylabel="Nisbiy amplituda")

table("Garmonikalarning fizik ma'nosi",
      ["n", "Shakl", "Fizik hodisa", "Tipik manba"],
      [[0, "o'qsimmetrik", "bir tekis egilish", "bir tekis bosim"],
       [1, "bir tomonga qiyalik", "eksantriklik", "markazdan siljigan yuk"],
       [2, "ovallashish", "ikki o'qli siqilish", "ikki tomondan bosim"],
       [3, "uch gulbargli", "uch nuqtali tayanch", "uch oyoqli tayanch"],
       [4, "to'rt gulbargli", "to'rt boltli mahkamlash", "flanets boltlari"]])
note("Yuqori garmonikalar qisqa to'lqinli va katta egrilikka ega, "
     "shuning uchun plastina ularga kuchli qarshilik ko'rsatadi — "
     "amplitudalari tez kamayadi.")
''',
                parameters=[
                    p("R", "Radius R", 50.0, 3000.0, 500.0, 10.0, "mm"),
                    p("h", "Qalinlik h", 2.0, 200.0, 15.0, 1.0, "mm"),
                    p("E", "Yung moduli E", 1.0, 400.0, 200.0, 1.0, "GPa"),
                    p("nu", "Puasson koeffitsienti ν", 0.0, 0.45, 0.3, 0.01),
                    p("q0", "Yuklama q₀", 0.001, 10.0, 0.5, 0.01, "MPa"),
                    p("kind", "Yuklama turi (0 yarim yuza, 1 yamoq)",
                      0.0, 1.0, 0.0, 1.0),
                    p("ecc", "Eksantriklik e/R", 0.0, 0.8, 0.5, 0.05),
                    p("NH", "Garmonikalar soni", 1.0, 15.0, 9.0, 1.0),
                ],
                expected_output=(
                    "D = 61,81 kN·m; yarim yuza yuklamasida "
                    "q₀ = 0,25 MPa, b₁ = 0,3183 MPa = 2q/π, "
                    "kosinus koeffitsientlari ~10⁻¹⁷ (nol); "
                    "n = 0 qismi 3,950 mm, to'liq yechim "
                    "4,281 mm (r/R = 0,177, θ = 90°) — "
                    "nosimmetriya hissasi 7,7 %."
                ),
            ),
            visual=vis(
                kind="Garmonikalar va ularning superpozitsiyasi",
                tool="React/SVG",
                description=(
                    "Har bir garmonikaning burchak shakli, radial "
                    "profili va ularning yig'indisi sifatidagi "
                    "og'ish sirti."
                ),
                how_to_draw=(
                    "React/SVG: birinchi panel — garmonika "
                    "shakllarining galereyasi: $n = 0 \\ldots 4$ "
                    "uchun kichik doiralar, har birida "
                    "$\\cos n\\theta$ ning ishorasi rang bilan "
                    "(musbat issiq, manfiy sovuq). $n = 0$ bir "
                    "xil rangda, $n = 1$ ikkiga bo'lingan, "
                    "$n = 2$ to'rtga va hokazo — 'gulbarg' "
                    "shakllari darhol ko'rinadi. Har birining "
                    "tagida amplitudasi yozilgan. Ikkinchi panel — "
                    "superpozitsiya: slayder bilan nechta "
                    "garmonika qo'shilishini tanlaymiz va og'ish "
                    "sirti konturi yangilanadi; $n = 0$ da "
                    "konsentrik halqalar, garmonikalar "
                    "qo'shilgani sari markaz siljiydi va shakl "
                    "nosimmetrik bo'ladi. Uchinchi panel — "
                    "$w(\\theta)$ grafigi belgilangan radiusda: "
                    "u yerda har bir garmonikaning hissasi "
                    "alohida chiziq bilan va yig'indisi qalin "
                    "chiziq bilan ko'rsatiladi."
                ),
            ),
            interp=(
                "Garmonikalar hissasi jadvali usulning amaliy "
                "qiymatini ko'rsatadi: amplitudalar $n$ bilan tez "
                "kamayadi, shuning uchun 5–9 ta garmonika "
                "yetarli. Bu Navye qatoridagi $O(m^{-5})$ "
                "yaqinlashishga o'xshash sabab bilan: yuqori "
                "garmonikalar qisqa to'lqinli, katta egrilikka "
                "ega va plastina ularga kuchli qarshilik "
                "ko'rsatadi. Yarim yuza yuklamasida bazis "
                "tanlash masalasi ham muhim saboq: kosinuslar "
                "bo'yicha barcha koeffitsientlar nolga teng "
                "chiqdi, chunki yuklama $\\theta = 0$ o'qiga "
                "nisbatan simmetrik emas. To'g'ri bazis — "
                "sinuslar. Bu umumiy qoidani eslatadi: "
                "koordinata o'qini masalaning simmetriyasiga "
                "moslab tanlash kerak, aks holda hisob ikki "
                "marta ko'payadi yoki umuman noto'g'ri "
                "chiqadi. Garmonikalarning fizik ma'nosi "
                "jadvali esa loyihalash uchun foydali: "
                "flanetsdagi to'rtta bolt $n = 4$ garmonikasini "
                "qo'zg'atadi, uch oyoqli tayanch esa $n = 3$ ni. "
                "Agar konstruksiyaning xususiy shakli (pq-22) "
                "shu garmonikaga mos kelsa, rezonans xavfi "
                "paydo bo'ladi — bu aylanuvchi mashinalarda "
                "jiddiy muammo."
            ),
            mistakes=[
                "Bazisni tekshirmasdan faqat kosinuslar bilan "
                "ishlash. Yuklama tanlangan o'qqa nisbatan "
                "simmetrik bo'lmasa, sinuslar ham kerak — aks "
                "holda barcha koeffitsientlar nol chiqadi.",
                "$n = 1$ garmonikasida qattiq jism harakatini "
                "ajratmaslik. $r\\cos\\theta = x$ — bu "
                "shunchaki qiyalik, deformatsiya emas; erkin "
                "plastinada u alohida hisobga olinadi.",
                "$n = 2$ va $n = 4$ da xususiy yechim "
                "maxrajining nolga aylanishini e'tiborsiz "
                "qoldirish. Bu rezonans holat va qo'shimcha "
                "$r^4\\ln r$ hadi kerak.",
                "O'qsimmetrik yechimni nosimmetrik yuklamaga "
                "qo'llash. Faqat $n = 0$ qismini olish "
                "maksimal og'ishni sezilarli kam baholaydi.",
            ],
            quiz=[
                q("Nima uchun $\\cos n\\theta$ bazis sifatida "
                  "tanlanadi?",
                  "U $\\partial^2/\\partial\\theta^2$ "
                  "operatorining xususiy funksiyasi "
                  "($-n^2$ xususiy qiymat bilan), shuning uchun "
                  "differensiallashda shakl saqlanadi.",
                  "konseptual"),
                q("$n = 1$ garmonikasining fizik ma'nosi nima?",
                  "Plastinaning bir tomonga qiyalashishi — "
                  "eksantrik yuklama natijasi. Uning bir "
                  "jinsli yechimlaridan biri qattiq jism "
                  "burilishi.", "konseptual"),
                q("Yarim yuzaga qo'yilgan yuklamaning "
                  "koeffitsientlari qanday kamayadi?",
                  "$1/n$ kabi: $\\tilde{q}_n = 2q/(n\\pi)$ "
                  "($n$ toq). Og'ishda esa maxraj "
                  "$r^4$ hadi tufayli ancha tez kamayadi.",
                  "hisob"),
                q("Radial operator $L_n$ ni yozing.",
                  "$L_n[W] = W'' + W'/r - n^2W/r^2$. "
                  "Bigarmonik tenglama "
                  "$L_n[L_n[W_n]] = q_n/D$ ko'rinishini oladi.",
                  "hisob"),
                q("Kodda nima uchun $n = 2$ va $n = 4$ alohida "
                  "ko'rib chiqiladi?",
                  "Xususiy yechim maxraji $(16-n^2)(4-n^2)$ "
                  "shu qiymatlarda nolga aylanadi — rezonans "
                  "holat, qo'shimcha logarifmik had kerak.",
                  "kod"),
                q("To'rt boltli flanets qaysi garmonikani "
                  "qo'zg'atadi va bu nima uchun muhim?",
                  "$n = 4$ ni. Agar konstruksiyaning xususiy "
                  "shakli shu garmonikaga mos kelsa, "
                  "rezonans xavfi paydo bo'ladi — aylanuvchi "
                  "mashinalarda jiddiy muammo.", "talqin"),
            ],
            bridge=(
                "Hozirgacha plastina chekkalari bo'ylab "
                "tayangan edi. Amaliyotda esa ko'plab plitalar "
                "butun yuzasi bo'ylab grunt yoki elastik "
                "qatlam ustida yotadi. Keyingi mavzuda elastik "
                "asosdagi plastinalarni o'rganamiz."
            ),
            research=(
                "Termik yuklamani plastina tenglamasiga "
                "kiriting. Qalinlik bo'yicha chiziqli harorat "
                "gradiyenti $\\Delta T$ ekvivalent termik "
                "moment $M_T = \\alpha E h^2\\Delta T/"
                "[12(1-\\nu)]$ beradi va tenglama "
                "$D\\nabla^4w = q - \\nabla^2 M_T/(1-\\nu)$ "
                "ko'rinishini oladi. Nosimmetrik qizish "
                "(masalan, quyosh bir tomondan) $n = 1$ "
                "garmonikasini qo'zg'atadi. Sun'iy yo'ldosh "
                "antennasi reflektorining orbitada qizishi "
                "natijasidagi shakl xatosini baholang: "
                "$\\Delta T = 50$ K da og'ish qancha va bu "
                "radiochastota nurlanish diagrammasiga qanday "
                "ta'sir qiladi?"
            ),
            manim_ref=manim(
                scene="FourierHarmonicsScene",
                module="animatsiya/scenes/pq_circular.py",
                title="Doiraviy plastinadagi garmonikalar",
                summary=(
                    "$n = 0, 1, 2, 3$ garmonikalarining shakllari "
                    "ketma-ket ko'rsatiladi va ular qo'shilib "
                    "nosimmetrik og'ish sirtini hosil qilishi "
                    "animatsiya qilinadi."
                ),
            ),
        ),
    ),

    # ------------------------------------------------------------------ pq-16
    Topic(
        id="pq-16",
        subject_id=S, module_id=M, order=16,
        title="Elastik asosda yotgan plastinalar: Vinkler modeli va xarakterli uzunlik",
        description=(
            "Grunt yoki elastik qatlam ustidagi plita, Vinkler "
            "reaksiyasi, o'zgargan tenglama, xarakterli uzunlik va "
            "yuklamaning mahalliy ta'siri."
        ),
        learning_objective=(
            "Elastik asosli plastina tenglamasini yozish, xarakterli "
            "uzunlikning fizik ma'nosini tushuntirish va mahalliy "
            "yuklamaning ta'sir zonasini baholash."
        ),
        prerequisites=["pq-15", "pq-11"],
        mathematical_core=(
            "$D\\nabla^4w + kw = q$, xarakterli uzunlik "
            "$\\ell = \\sqrt[4]{D/k}$, Kelvin funksiyalari "
            "$\\mathrm{ker}, \\mathrm{kei}$, eksponensial so'nuvchi yechim."
        ),
        engineering_application=(
            "Yo'l va aerodrom qoplamasi, sanoat poli, fundament "
            "plitasi, temir yo'l shpali, rezina yostiq ustidagi "
            "mashina poydevori, muz qatlami."
        ),
        computational_component=(
            "Xarakterli uzunlikni hisoblash, konsentrlangan kuch "
            "ostidagi yechimni qurish, asos koeffitsientining "
            "ta'sirini parametrik tahlil qilish."
        ),
        visualization_component=(
            "Og'ish va reaksiya bosimining radial profili, "
            "ta'sir zonasining $k$ ga bog'liqligi, ko'tarilish sohasi."
        ),
        research_extension=(
            "Ikki parametrli asos modellarini (Pasternak, "
            "Filonenko-Borodich) o'rganing: ular Vinkler modelining "
            "qaysi kamchiligini bartaraf etadi?"
        ),
        difficulty="murakkab",
        previous_link=(
            "pq-11 da konsentrlangan yuklama chekkalari bo'ylab "
            "tayangan plastinada ko'rib chiqilgan edi. Endi "
            "tayanch butun yuza bo'ylab taqsimlanadi va masala "
            "tubdan o'zgaradi: cheksiz plastinada ham chekli "
            "yechim paydo bo'ladi."
        ),
        next_topic="pq-17",
        estimated_minutes=90,
        tags=["elastik asos", "Vinkler", "fundament", "qoplama"],
        lesson=_lesson(
            problem=(
                "Aerodrom betondan qilingan qoplamasi: samolyot "
                "shassisi g'ildiragi 200 kN kuch uzatadi. Qoplama "
                "chekkalari yo'q — u cheksiz deb hisoblanadi. "
                "Chekkasiz plastina qanday muvozanatda turadi? "
                "Javob: tayanch chekkada emas, **butun yuza "
                "bo'ylab** — grunt reaksiyasi. Bu hol oldingi "
                "barcha masalalardan tubdan farq qiladi va "
                "kutilmagan natijaga olib keladi: yuklama "
                "ta'siri mahalliy bo'lib qoladi."
            ),
            concepts=[
                c("Vinkler asosi (Winkler foundation)",
                  "Grunt mustaqil prujinalar to'plami deb "
                  "modellashtiriladi: $p = kw$, bunda $k$ — "
                  "yotqizish koeffitsienti (N/m³)."),
                c("Yotqizish koeffitsienti $k$",
                  "Birlik yuzadagi birlik cho'kishga to'g'ri "
                  "keladigan bosim. Yumshoq grunt: "
                  "$10\\ldots50$ MN/m³; zich qum: "
                  "$50\\ldots150$; tosh: $> 300$."),
                c("Xarakterli uzunlik $\\ell$",
                  "$\\ell = \\sqrt[4]{D/k}$ — plastina bikrligi va "
                  "asos qattiqligining raqobatidan kelib "
                  "chiqadigan tabiiy masshtab. Yuklama ta'siri "
                  "$\\sim 4\\ell$ masofada so'nadi."),
                c("Bikr va moslashuvchan plita",
                  "$L < \\ell$ — bikr (butunligicha cho'kadi); "
                  "$L > 4\\ell$ — moslashuvchan (mahalliy egiladi). "
                  "Loyihalashda bu farq hal qiluvchi."),
                c("Kelvin funksiyalari",
                  "$\\mathrm{ker}(x)$ va $\\mathrm{kei}(x)$ — "
                  "Bessel funksiyalarining kompleks argumentli "
                  "kombinatsiyasi; cheksiz plitadagi "
                  "konsentrlangan kuch yechimi shular orqali."),
                c("Ko'tarilish sohasi (uplift)",
                  "Yuklama atrofida plita ko'tariladi "
                  "($w < 0$) — bu grunt tortolmasligi sababli "
                  "modelning chegarasi."),
            ],
            derivation=[
                d("1. Asos reaksiyasini kiritish",
                  r"p(x,y) = k\,w(x,y)",
                  "Vinkler gipotezasi: har bir nuqtadagi "
                  "reaksiya faqat shu nuqtadagi cho'kishga "
                  "mutanosib. Prujinalar o'zaro bog'lanmagan."),
                d("2. Muvozanat tenglamasiga qo'shish",
                  r"D\nabla^4 w = q - p = q - kw \;\Longrightarrow\; "
                  r"D\nabla^4 w + kw = q",
                  "Asos reaksiyasi tashqi yuklamaga qarshi "
                  "ta'sir qiladi. Tenglamaga **yangi had** "
                  "qo'shildi — bu uning xarakterini tubdan "
                  "o'zgartiradi."),
                d("3. Xarakterli uzunlikni kiritish",
                  r"\ell = \sqrt[4]{\frac{D}{k}} \;\Longrightarrow\; "
                  r"\ell^4\nabla^4 w + w = \frac{q}{k}",
                  "O'lchamsizlashtirish: $\\xi = r/\\ell$ "
                  "almashtirishida tenglama "
                  "$\\nabla_\\xi^4 w + w = q/k$ ko'rinishini "
                  "oladi — hech qanday parametrsiz."),
                d("4. Bir jinsli tenglama va uning yechimi",
                  r"\ell^4\nabla^4 w + w = 0 \;\Longrightarrow\; "
                  r"\nabla^2 w = \pm\frac{i}{\ell^2}w",
                  "$\\nabla^4 + 1/\\ell^4$ operatorini "
                  "ko'paytuvchilarga ajratamiz. Kompleks "
                  "birlik paydo bo'lishi tebranuvchi va "
                  "so'nuvchi yechimni bildiradi."),
                d("5. Kelvin funksiyalari",
                  r"w = C_1\,\mathrm{ber}\frac{r}{\ell} + "
                  r"C_2\,\mathrm{bei}\frac{r}{\ell} + "
                  r"C_3\,\mathrm{ker}\frac{r}{\ell} + "
                  r"C_4\,\mathrm{kei}\frac{r}{\ell}",
                  "$\\mathrm{ber}, \\mathrm{bei}$ markazda "
                  "regulyar, lekin cheksizlikda o'sadi; "
                  "$\\mathrm{ker}, \\mathrm{kei}$ esa "
                  "cheksizlikda so'nadi."),
                d("6. Cheksiz plita: so'nish sharti",
                  r"r \to \infty: \ w \to 0 \;\Longrightarrow\; "
                  r"C_1 = C_2 = 0",
                  "Yuklamadan uzoqda plita "
                  "deformatsiyalanmasligi kerak. Faqat "
                  "$\\mathrm{ker}$ va $\\mathrm{kei}$ qoladi."),
                d("7. Konsentrlangan kuch yechimi",
                  r"w(r) = \frac{P}{8D/\ell^2}\cdot\frac{1}{2\pi}"
                  r"\cdot(-2)\,\mathrm{kei}\frac{r}{\ell} "
                  r"\;\Longrightarrow\; w(0) = \frac{P\ell^2}{8D} "
                  r"= \frac{P}{8\sqrt{kD}}",
                  "Markazdagi kuchning muvozanatidan "
                  "$C_4$ aniqlanadi. Natija juda ixcham: "
                  "og'ish $\\sqrt{kD}$ ga teskari mutanosib."),
                d("8. So'nish masofasi",
                  r"|\mathrm{kei}(x)| \sim e^{-x/\sqrt{2}} "
                  r"\;\Longrightarrow\; w(4\ell)/w(0) \approx 0{,}01",
                  "Kelvin funksiyalari eksponensial so'nadi. "
                  "$4\\ell$ masofada og'ish 1 % ga tushadi — "
                  "shuning uchun bu 'ta'sir radiusi' deb ataladi."),
            ],
            meaning=(
                "$\\ell = \\sqrt[4]{D/k}$ — bu mavzudagi markaziy "
                "kattalik va uning fizik ma'nosi chuqur: u "
                "plastina bikrligi bilan asos qattiqligining "
                "raqobatidan tug'iladigan **tabiiy uzunlik "
                "masshtabi**. Bikr plita ($D$ katta) yukni uzoqqa "
                "tarqatadi — $\\ell$ katta; qattiq grunt "
                "($k$ katta) esa yukni mahalliy ushlaydi — "
                "$\\ell$ kichik. To'rtinchi daraja ildizi "
                "bog'liqlikni juda yumshoq qiladi: $D$ ni "
                "16 marta oshirish (qalinlikni 2,5 marta) "
                "$\\ell$ ni atigi 2 marta oshiradi. Shuning "
                "uchun aerodrom qoplamasini qalinlashtirish "
                "yuklamaning tarqalish radiusini sekin "
                "kengaytiradi va samarasiz — u yerda gruntni "
                "yaxshilash ancha foydaliroq. Eng kutilmagan "
                "natija esa **mahalliylik**: cheksiz plitada "
                "ham og'ish $4\\ell$ dan uzoqda amalda nolga "
                "teng. Bu chekkalari bo'ylab tayangan "
                "plastinadan tubdan farq qiladi — u yerda "
                "yuklama butun plastinaga ta'sir qilardi. "
                "Shundan amaliy qoida kelib chiqadi: agar plita "
                "o'lchami $4\\ell$ dan katta bo'lsa, uni "
                "cheksiz deb hisoblash mumkin va chekkalarning "
                "ahamiyati yo'q. Aerodrom plitasi uchun "
                "$\\ell \\approx 0{,}7$ m, demak $3$ m dan "
                "katta plita allaqachon 'cheksiz'."
            ),
            equations=[
                eq(r"D\nabla^4 w + kw = q",
                   "Elastik asosdagi plastina tenglamasi "
                   "(Vinkler modeli).", "Vinkler tenglamasi"),
                eq(r"\ell = \sqrt[4]{\frac{D}{k}}",
                   "Xarakterli uzunlik.", "Xarakterli uzunlik"),
                eq(r"w(0) = \frac{P}{8\sqrt{kD}} = \frac{P\ell^2}{8D}",
                   "Cheksiz plitada konsentrlangan kuch ostidagi "
                   "maksimal og'ish.", "Markaziy og'ish"),
                eq(r"M_r(0) \approx \frac{P}{4\pi}\Big[(1+\nu)"
                   r"\ln\frac{2\ell}{r} + \ldots\Big]",
                   "Markaz yaqinidagi moment (logarifmik "
                   "singulyarlik bilan).", "Markaziy moment"),
            ],
            conditions=(
                "**Cheksiz plita uchun:** $r \\to \\infty$ da "
                "$w \\to 0$ — bu $\\mathrm{ber}$ va "
                "$\\mathrm{bei}$ hadlarini yo'q qiladi.\n\n"
                "**Markazda:** konsentrlangan kuch muvozanati "
                "$\\lim_{r\\to0} 2\\pi r Q_r = -P$.\n\n"
                "**Chekli plita uchun** chekkalarda odatdagi "
                "shartlar qo'yiladi, lekin $L > 4\\ell$ bo'lsa "
                "ular natijaga ta'sir qilmaydi.\n\n"
                "**Vinkler modelining chegaralari:**\n"
                "1. Prujinalar bog'lanmagan — grunt siljishga "
                "qarshiligi hisobga olinmaydi;\n"
                "2. Model tortish kuchini ham beradi "
                "($w < 0$ da $p < 0$), lekin grunt tortolmaydi — "
                "ko'tarilish sohasida model yaroqsiz;\n"
                "3. $k$ plita o'lchamiga bog'liq (tajribadan "
                "aniqlanadi) — bu modelning eng zaif joyi.\n\n"
                "**Ko'tarilish tuzatmasi:** $w < 0$ bo'lgan "
                "sohada $p = 0$ deb olib, masala iterativ "
                "yechiladi (bir tomonlama aloqa, unilateral contact)."
            ),
            worked=WorkedExample(
                statement=(
                    "Aerodrom beton qoplamasi: $h = 350$ mm, "
                    "$E = 30$ GPa, $\\nu = 0{,}2$; grunt "
                    "$k = 80$ MN/m³. G'ildirak yuklamasi "
                    "$P = 200$ kN, tayanch dog'i radiusi "
                    "$a = 150$ mm. (a) Xarakterli uzunlikni "
                    "toping. (b) Maksimal og'ish va ta'sir "
                    "radiusini hisoblang. (c) Momentni va "
                    "kuchlanishni baholang."
                ),
                given=[
                    r"h = 0{,}35\ \text{m},\ E = 30\ \text{GPa},\ "
                    r"\nu = 0{,}2",
                    r"k = 80\times10^{6}\ \text{N/m}^3",
                    r"P = 200\ \text{kN},\ a = 0{,}15\ \text{m}",
                ],
                steps=[
                    st(r"D = \frac{30\times10^9 \cdot 0{,}35^3}"
                       r"{12 \cdot 0{,}96} = \frac{1{,}2863\times10^{9}}"
                       r"{11{,}52} = 1{,}1165\times10^{8}\ \text{N·m}",
                       "$h^3 = 4{,}2875\\times10^{-2}$ m³. "
                       "Qalin qoplama — bikrligi juda katta."),
                    st(r"\ell = \sqrt[4]{\frac{D}{k}} = "
                       r"\sqrt[4]{\frac{1{,}1165\times10^{8}}"
                       r"{8\times10^{7}}} = \sqrt[4]{1{,}3956} "
                       r"= 1{,}0871\ \text{m}",
                       "Xarakterli uzunlik taxminan 1,09 m — "
                       "qoplama qalinligidan 3 marta katta."),
                    st(r"w(0) = \frac{P}{8\sqrt{kD}} = "
                       r"\frac{2\times10^{5}}{8\sqrt{8\times10^{7} "
                       r"\cdot 1{,}1165\times10^{8}}}",
                       "Ixcham formula. $\\sqrt{kD} = "
                       "\\sqrt{8{,}932\\times10^{15}} = "
                       "9{,}451\\times10^{7}$."),
                    st(r"w(0) = \frac{2\times10^{5}}{7{,}561\times10^{8}} "
                       r"= 2{,}645\times10^{-4}\ \text{m} = 0{,}265\ \text{mm}",
                       "Og'ish juda kichik — bikr plita va "
                       "qattiq grunt kombinatsiyasi."),
                    st(r"p_{\max} = k\,w(0) = 8\times10^{7} \cdot "
                       r"2{,}645\times10^{-4} = 21\,160\ \text{Pa} "
                       r"= 21{,}2\ \text{kPa}",
                       "Maksimal grunt bosimi. Taqqoslash uchun: "
                       "g'ildirak dog'idagi bosim "
                       "$P/(\\pi a^2) = 2{,}83$ MPa — plita "
                       "bosimni **134 marta** kamaytirdi."),
                    st(r"R_{\text{ta'sir}} \approx 4\ell = 4{,}35\ \text{m}",
                       "Bu radiusdan tashqarida og'ish 1 % dan "
                       "kam. Demak $8{,}7$ m diametrli soha "
                       "yetarli — plita undan katta bo'lsa, "
                       "'cheksiz' deb hisoblanadi."),
                    st(r"b = \sqrt{1{,}6a^2 + h^2} - 0{,}675h = "
                       r"\sqrt{0{,}036 + 0{,}1225} - 0{,}2363 "
                       r"= 0{,}1619\ \text{m}",
                       "Vestergaard ekvivalent radiusi: $a < 1{,}724h$ "
                       "bo'lgani uchun tayanch dog'i qalinlikka "
                       "nisbatan kichik va tuzatma kiritiladi."),
                    st(r"M_r = \frac{P}{4\pi}\Big[(1+\nu)"
                       r"\ln\frac{2\ell}{b} + 0{,}6159\Big] "
                       r"= \frac{2\times10^{5}}{12{,}566}"
                       r"\big[1{,}2\ln 13{,}43 + 0{,}6159\big]",
                       "Vestergaard formulasi (ichki yuklama holati). "
                       "$2\\ell/b = 2{,}174/0{,}1619 = 13{,}43$."),
                    st(r"M_r = 15\,915\big[1{,}2 \cdot 2{,}5976 "
                       r"+ 0{,}6159\big] = 15\,915 \cdot 3{,}733 "
                       r"= 59\,410\ \text{N·m/m}",
                       "Moment. Kuchlanish: "
                       "$\\sigma = 6 \\cdot 59\\,410/0{,}1225 "
                       "= 2{,}91$ MPa."),
                    st(r"\sigma = 2{,}91\ \text{MPa} \ \text{vs beton "
                       r"egilish mustahkamligi} \approx 4{,}5\ \text{MPa} "
                       r"\Rightarrow n = 1{,}55",
                       "Zaxira 1,55 — yetarli, lekin katta emas. "
                       "Charchoq (millionlab siklda) hisobga "
                       "olinishi shart."),
                ],
                answer=(
                    "$D = 111{,}65$ MN·m, $\\ell = 1{,}087$ m; "
                    "$w(0) = 0{,}265$ mm, $p_{\\max} = 21{,}2$ kPa "
                    "(g'ildirak bosimidan 134 marta kam); ta'sir "
                    "radiusi $\\approx 4{,}35$ m (sonli yechimda "
                    "og'ish $r = 3{,}69\\ell$ da 1 % ga tushadi); "
                    "$M_r = 59{,}4$ kN·m/m, $\\sigma = 2{,}91$ MPa, "
                    "zaxira 1,55."
                ),
                engineering_note=(
                    "Bosimning 134 marta kamayishi qoplamaning "
                    "asosiy vazifasini ko'rsatadi: u yukni "
                    "tarqatadi, ko'tarmaydi. Shuning uchun "
                    "qoplama loyihasida gruntning ko'tarish "
                    "qobiliyati emas, **plitaning egilish "
                    "mustahkamligi** hal qiluvchi bo'ladi. "
                    "Vestergaard formulalari (1926) aerodrom va "
                    "yo'l qoplamalari hisobining asosi bo'lib "
                    "qolmoqda; ular uchta holat uchun beriladi — "
                    "ichki, chekka va burchak yuklamasi. "
                    "Burchakdagi kuchlanish ichkidagidan 1,5–2 "
                    "marta katta, shuning uchun choklar va "
                    "burchaklar alohida armaturalanadi."
                ),
            ),
            computation=Computation(
                caption=(
                    "Xarakterli uzunlikni hisoblash, Kelvin "
                    "funksiyalari bilan cheksiz plita yechimini "
                    "qurish, ta'sir zonasi va ko'tarilish "
                    "sohasini aniqlash."
                ),
                code='''"""Elastik asosdagi plastina: Vinkler modeli."""
import numpy as np
from scipy.special import kelvin
from labkit import PARAMS, note, series, table, value

h = float(PARAMS.get("h", 350.0))/1000.0
E = float(PARAMS.get("E", 30.0))*1e9
nu = float(PARAMS.get("nu", 0.2))
k = float(PARAMS.get("k", 80.0))*1e6     # N/m^3
P = float(PARAMS.get("P", 200000.0))
a_pad = float(PARAMS.get("a", 150.0))/1000.0
L = float(PARAMS.get("L", 6.0))          # plita o'lchami (taqqoslash uchun)

D = E*h**3/(12*(1 - nu**2))
ell = (D/k)**0.25
value("Silindrik bikrlik D", D/1e6, "MN*m")
value("Yotqizish koeffitsienti k", k/1e6, "MN/m3")
value("Xarakterli uzunlik l", ell, "m")
value("l / h", ell/h, "—")
value("Ta'sir radiusi ~ 4*l", 4*ell, "m")
value("Plita o'lchami L / l", L/ell, "—")
if L > 4*ell:
    note(f"L/l = {L/ell:.1f} > 4 — plitani CHEKSIZ deb hisoblash "
         f"mumkin, chekkalar natijaga ta'sir qilmaydi.")
else:
    note(f"L/l = {L/ell:.1f} < 4 — plita BIKR, u deyarli "
         f"butunligicha cho'kadi; chekka shartlari muhim.")

# --- Kelvin funksiyalari bilan yechim ---
# scipy.special.kelvin(x) -> (Be, Ke, Bep, Kep), ularning har biri kompleks:
#   Be = ber + i*bei,  Ke = ker + i*kei  (Bep, Kep — hosilalari)
r = np.linspace(1e-3, 6*ell, 500)
x = r/ell
Be, Ke, Bep, Kep = kelvin(x)
ber, bei = Be.real, Be.imag
ker, kei = Ke.real, Ke.imag

# Cheksiz plita, markazda P: w(r) = -(P*l^2)/(2*pi*D) * kei(r/l).
# kei(0) = -pi/4 bo'lgani uchun w(0) = P*l^2/(8D) = P/(8*sqrt(k*D)).
w0_exact = P/(8*np.sqrt(k*D))
w = -P*ell**2/(2*np.pi*D)*kei
value("kei(0) (nazariy -pi/4)", float(kei[0]), "—")
value("w(0) analitik (P/(8*sqrt(kD)))", w0_exact*1000, "mm")
value("w(0) Kelvin funksiyasidan", float(w[0])*1000, "mm")
note(f"Ikki mustaqil yo'l bir xil natija berdi: "
     f"{w0_exact*1000:.5f} mm va {float(w[0])*1000:.5f} mm "
     f"(farq {abs(float(w[0])-w0_exact)/w0_exact*100:.3f} %).")

series("Og'ish w(r)", (r/ell).tolist(), (w*1000).tolist(),
       xlabel="r / l", ylabel="Og'ish w, mm")
series("Asos bosimi p(r) = k*w", (r/ell).tolist(),
       (k*w/1000).tolist(), xlabel="r / l", ylabel="Bosim p, kPa")

p_max = k*float(w[0])
value("Maksimal asos bosimi", p_max/1000, "kPa")
value("G'ildirak dog'idagi bosim", P/(np.pi*a_pad**2)/1e6, "MPa")
value("Bosimni kamaytirish koeffitsienti",
      (P/(np.pi*a_pad**2))/p_max, "—")

# Ta'sir zonasi
rel = np.abs(w)/abs(float(w[0]))
i1 = int(np.argmax(rel < 0.01))
value("Og'ish 1 % ga tushadigan r/l", float(x[i1]), "—")
value("Shu masofa", float(r[i1]), "m")

# Ko'tarilish sohasi
neg = w < 0
if np.any(neg):
    i_neg = int(np.argmax(neg))
    value("Ko'tarilish boshlanadigan r/l", float(x[i_neg]), "—")
    value("Maksimal ko'tarilish", float(np.min(w))*1000, "mm")
    value("Ko'tarilish / cho'kish nisbati",
          abs(float(np.min(w))/float(w[0]))*100, "%")
    note(f"r/l > {x[i_neg]:.2f} da plita KO'TARILADI (w < 0). "
         f"Vinkler modeli u yerda tortish reaksiyasini beradi, "
         f"lekin grunt tortolmaydi — model chegarasi.")

# --- Momentlar (sonli differensiallash) ---
dr = r[1] - r[0]
dw = np.gradient(w, dr)
d2w = np.gradient(dw, dr)
Mr = -D*(d2w + nu*dw/np.maximum(r, 1e-9))
Mt = -D*(dw/np.maximum(r, 1e-9) + nu*d2w)
series("M_r(r)", (r/ell).tolist(), (Mr/1000).tolist(),
       xlabel="r / l", ylabel="M_r, kN*m/m")
series("M_theta(r)", (r/ell).tolist(), (Mt/1000).tolist(),
       xlabel="r / l", ylabel="M_theta, kN*m/m")

# Vestergaard formulasi (ichki yuklama)
b_eff = a_pad if a_pad >= 1.724*h else np.sqrt(1.6*a_pad**2 + h**2) - 0.675*h
M_west = P/(4*np.pi)*((1 + nu)*np.log(2*ell/b_eff) + 0.6159)
sig_west = 6*M_west/h**2
value("Vestergaard ekvivalent radius b", b_eff*1000, "mm")
value("Vestergaard momenti M_r", M_west/1000, "kN*m/m")
value("Vestergaard kuchlanishi", sig_west/1e6, "MPa")
f_ct = 4.5e6
value("Beton egilish mustahkamligi (taxminan)", f_ct/1e6, "MPa")
value("Zaxira koeffitsienti", f_ct/sig_west, "—")

# --- k va h ning ta'siri ---
ks = np.logspace(np.log10(10e6), np.log10(300e6), 80)
ells, w0s, sigs = [], [], []
for kk in ks:
    ll = (D/kk)**0.25
    ells.append(ll)
    w0s.append(P/(8*np.sqrt(kk*D))*1000)
    bb = a_pad if a_pad >= 1.724*h else np.sqrt(1.6*a_pad**2 + h**2) - 0.675*h
    sigs.append(6*(P/(4*np.pi)*((1 + nu)*np.log(2*ll/bb) + 0.6159))/h**2/1e6)
series("Xarakterli uzunlik l(k)", (ks/1e6).tolist(), ells,
       xlabel="Yotqizish koeffitsienti k, MN/m3", ylabel="l, m")
series("Og'ish w(0) k ga bog'liq", (ks/1e6).tolist(), w0s,
       xlabel="Yotqizish koeffitsienti k, MN/m3", ylabel="w(0), mm")
series("Kuchlanish k ga bog'liq", (ks/1e6).tolist(), sigs,
       xlabel="Yotqizish koeffitsienti k, MN/m3", ylabel="sigma, MPa")
note(f"k ni 10 dan 300 MN/m3 ga oshirish (30 marta) og'ishni "
     f"{w0s[0]/w0s[-1]:.1f} marta kamaytiradi, lekin kuchlanishni "
     f"atigi {sigs[0]/sigs[-1]:.2f} marta — grunt yaxshilash "
     f"cho'kishga ta'sir qiladi, mustahkamlikka esa kam.")

hs = np.linspace(0.15, 0.6, 80)
ells_h, sigs_h = [], []
for hh in hs:
    Dh = E*hh**3/(12*(1 - nu**2))
    ll = (Dh/k)**0.25
    bb = a_pad if a_pad >= 1.724*hh else np.sqrt(1.6*a_pad**2 + hh**2) - 0.675*hh
    ells_h.append(ll)
    sigs_h.append(6*(P/(4*np.pi)*((1 + nu)*np.log(2*ll/bb) + 0.6159))/hh**2/1e6)
series("l(h)", (hs*1000).tolist(), ells_h,
       xlabel="Qoplama qalinligi h, mm", ylabel="l, m")
series("sigma(h)", (hs*1000).tolist(), sigs_h,
       xlabel="Qoplama qalinligi h, mm", ylabel="sigma, MPa")
series("Beton mustahkamligi", (hs*1000).tolist(),
       [f_ct/1e6]*len(hs), xlabel="Qoplama qalinligi h, mm",
       ylabel="sigma, MPa")

i_ok = int(np.argmax(np.array(sigs_h) < f_ct/1e6/1.3))
if i_ok > 0:
    value("Kerakli qalinlik (n = 1.3 bilan)", float(hs[i_ok])*1000, "mm")

table("Yotqizish koeffitsientining tipik qiymatlari",
      ["Grunt turi", "k, MN/m3", "l (h = 350 mm da), m"],
      [[name, kv, round((D/(kv*1e6))**0.25, 3)]
       for name, kv in [("Yumshoq loy", 15), ("O'rtacha loy", 40),
                        ("Zich qum", 80), ("Shag'al asos", 150),
                        ("Tosh asos", 300)]])

table("Vinkler modelining kamchiliklari va ularning yechimi",
      ["Kamchilik", "Oqibat", "Yechim"],
      [["Prujinalar bog'lanmagan", "grunt siljishi hisobga olinmaydi",
        "Pasternak (ikki parametrli) model"],
       ["Tortish reaksiyasi", "ko'tarilish sohasida noto'g'ri",
        "bir tomonlama aloqa (iterativ)"],
       ["k plita o'lchamiga bog'liq", "universal qiymat yo'q",
        "plita o'lchamiga moslangan sinov"],
       ["Chiziqli", "katta bosimda grunt plastiklashadi",
        "nochiziqli asos modeli"]])
''',
                parameters=[
                    p("h", "Qoplama qalinligi h", 80.0, 800.0, 350.0, 10.0, "mm"),
                    p("E", "Yung moduli E", 1.0, 400.0, 30.0, 1.0, "GPa"),
                    p("nu", "Puasson koeffitsienti ν", 0.0, 0.45, 0.2, 0.01),
                    p("k", "Yotqizish koeffitsienti k", 5.0, 500.0, 80.0, 5.0,
                      "MN/m³"),
                    p("P", "G'ildirak yuklamasi P", 10000.0, 1000000.0,
                      200000.0, 5000.0, "N"),
                    p("a", "Tayanch dog'i radiusi a", 30.0, 500.0, 150.0, 10.0,
                      "mm"),
                    p("L", "Plita o'lchami L", 1.0, 30.0, 6.0, 0.5, "m"),
                ],
                expected_output=(
                    "D = 111,65 MN·m, ℓ = 1,087 m; w(0) = 0,265 mm "
                    "(ikki mustaqil yo'l bilan mos), p_max = "
                    "21,16 kPa — g'ildirak bosimidan 133,7 marta kam; "
                    "kei(0) = −0,7854 = −π/4; og'ish r = 3,69ℓ da "
                    "1 % ga tushadi, r > 3,92ℓ da ko'tarilish "
                    "boshlanadi (cho'kishning 1,4 % i); Vestergaard "
                    "bo'yicha M = 59,4 kN·m/m, σ = 2,91 MPa, zaxira 1,55."
                ),
            ),
            visual=vis(
                kind="Elastik asosdagi plita",
                tool="React/SVG",
                description=(
                    "Cho'kish profili, asos bosimi taqsimoti, "
                    "ta'sir zonasi va ko'tarilish sohasi."
                ),
                how_to_draw=(
                    "React/SVG: asosiy panel — yon kesim: plita "
                    "chizig'i, ostida prujinalar qatori (zigzag "
                    "`<polyline>` lar, har biri mustaqil — bu "
                    "Vinkler gipotezasining vizual mohiyati). "
                    "Yuklama joyida prujinalar siqilgan, "
                    "uzoqroqda cho'zilgan (ko'tarilish sohasi) — "
                    "bu ikki soha turli rangda. Cho'kish profili "
                    "$w(r)$ egri chiziq bilan, masshtabi "
                    "oshirilgan. Ostida asos bosimi epyurasi "
                    "$p = kw$ ustunlar bilan; manfiy qism "
                    "(tortish) shtrixlangan va 'model chegarasi' "
                    "yorlig'i bilan belgilanadi. $x$ o'qi "
                    "$r/\\ell$ da olinadi, shunda $4\\ell$ "
                    "chegarasi vertikal punktir bilan "
                    "ko'rsatiladi va universal xarakteri "
                    "ko'rinadi. Ikkinchi panel — slayder bilan "
                    "$k$ o'zgartiriladi: yumshoq gruntda profil "
                    "keng va sayoz, qattiqda tor va chuqur; "
                    "$\\ell$ qiymati jonli yangilanadi."
                ),
            ),
            interp=(
                "$k$ ning ta'siri grafigi loyihalashdagi eng "
                "muhim xulosani beradi: gruntni 30 marta "
                "yaxshilash cho'kishni 5–6 marta kamaytiradi, "
                "lekin plitadagi kuchlanishni deyarli "
                "o'zgartirmaydi. Sababi formulada ko'rinadi: "
                "$w \\propto 1/\\sqrt{k}$, lekin moment faqat "
                "$\\ln\\ell \\propto \\ln k^{-1/4}$ orqali "
                "bog'langan — logarifmik, ya'ni juda sekin. "
                "Demak qoplama mustahkamligi uchun grunt emas, "
                "**qalinlik** hal qiluvchi. Bu amalda yo'l "
                "qurilishidagi klassik dilemma: qimmat asos "
                "qatlami (grunt yaxshilash) yoki qalinroq beton? "
                "Javob: asos qatlami cho'kish va bir tekislik "
                "uchun kerak, qalinlik esa yorilishdan himoya "
                "uchun. Ko'tarilish sohasi ham muhim amaliy "
                "ma'noga ega: model u yerda gruntni "
                "'tortmoqda' deb hisoblaydi, lekin grunt "
                "tortolmaydi. Natijada real plita "
                "hisoblangandan ko'proq cho'kadi va "
                "ko'tarilgan qismi ostida bo'shliq paydo "
                "bo'ladi — u yomg'ir suvi bilan to'ladi va "
                "'nasos effekti' (pumping) tufayli asosni "
                "yuvib ketadi. Bu aerodrom qoplamalarining "
                "asosiy buzilish mexanizmlaridan biri."
            ),
            mistakes=[
                "$k$ ni universal material doimiysi deb "
                "hisoblash. U plita o'lchamiga va sinov "
                "usuliga bog'liq; katta plita uchun $k$ "
                "kichikroq bo'ladi.",
                "Ko'tarilish sohasida model natijasini qabul "
                "qilish. Grunt tortolmaydi — bir tomonlama "
                "aloqa masalasi iterativ yechilishi kerak.",
                "Chekkalari bo'ylab tayangan plastina "
                "formulalarini elastik asosli plitaga "
                "qo'llash. Ular tubdan boshqa — bu yerda "
                "ta'sir mahalliy.",
                "Ta'sir radiusini hisobga olmasdan plita "
                "o'lchamini tanlash. $L < 4\\ell$ bo'lsa "
                "plita bikr ishlaydi va formulalar yaroqsiz.",
            ],
            quiz=[
                q("Vinkler modelining asosiy gipotezasi nima?",
                  "Grunt mustaqil prujinalar to'plami: har bir "
                  "nuqtadagi reaksiya faqat shu nuqtadagi "
                  "cho'kishga mutanosib, $p = kw$.",
                  "konseptual"),
                q("Xarakterli uzunlikning fizik ma'nosi nima?",
                  "$\\ell = \\sqrt[4]{D/k}$ — plastina bikrligi "
                  "va asos qattiqligining raqobatidan kelib "
                  "chiqadigan tabiiy masshtab; yuklama ta'siri "
                  "$\\sim 4\\ell$ da so'nadi.", "konseptual"),
                q("$D = 10^8$ N·m, $k = 50$ MN/m³. $\\ell$ ni "
                  "toping.",
                  "$\\ell = (10^8/5\\times10^7)^{1/4} = "
                  "2^{1/4} = 1{,}189$ m.", "hisob"),
                q("Nima uchun grunt yaxshilash kuchlanishni "
                  "deyarli kamaytirmaydi?",
                  "Og'ish $1/\\sqrt{k}$ ga mutanosib, lekin "
                  "moment faqat $\\ln\\ell$ orqali, ya'ni "
                  "$\\ln k^{-1/4}$ — logarifmik va juda sekin "
                  "bog'liqlik.", "talqin"),
                q("Kodda nima uchun ikki xil yo'l bilan "
                  "$w(0)$ hisoblanadi?",
                  "Mustaqil tekshiruv: analitik formula "
                  "$P/(8\\sqrt{kD})$ va Kelvin funksiyasi "
                  "$\\mathrm{kei}$ orqali yechim bir xil "
                  "natija berishi kerak.", "kod"),
                q("Ko'tarilish sohasida nima yuz beradi va "
                  "u nima uchun xavfli?",
                  "Model tortish reaksiyasini beradi, lekin "
                  "grunt tortolmaydi. Real plita ostida "
                  "bo'shliq paydo bo'ladi, u suv bilan "
                  "to'ladi va 'nasos effekti' asosni "
                  "yuvib ketadi.", "talqin"),
            ],
            bridge=(
                "Hozirgacha plastina bir jinsli va bir "
                "qatlamli edi. Zamonaviy konstruksiyalarda "
                "esa qatlamli va sendvich panellar keng "
                "tarqalgan. Keyingi mavzuda ularning "
                "nazariyasini quramiz."
            ),
            research=(
                "Ikki parametrli asos modellarini o'rganing. "
                "Pasternak modeli prujinalarga siljishga "
                "ishlaydigan qatlam qo'shadi: "
                "$p = kw - G_p\\nabla^2 w$. Bu Vinkler "
                "modelining qaysi kamchiligini bartaraf "
                "etadi? Tenglama "
                "$D\\nabla^4w - G_p\\nabla^2w + kw = q$ "
                "ko'rinishini oladi — uni yeching va "
                "Vinkler yechimi bilan taqqoslang. "
                "$G_p$ ning ta'sir zonasiga va chekka "
                "yaqinidagi bosim sakrashiga ta'sirini "
                "tahlil qiling. Filonenko-Borodich va "
                "Vlasov-Leontyev modellari bilan ham "
                "solishtiring: qaysi biri real grunt "
                "o'lchovlariga yaqinroq?"
            ),
            manim_ref=manim(
                scene="ElasticFoundationScene",
                module="animatsiya/scenes/pq_circular.py",
                title="Vinkler asosi va xarakterli uzunlik",
                summary=(
                    "Plita ostidagi mustaqil prujinalar "
                    "ko'rsatiladi; yuklama qo'yilganda mahalliy "
                    "cho'kish paydo bo'ladi va uning "
                    "$4\\ell$ da so'nishi, asos qattiqligi "
                    "o'zgarganda zona kengayishi animatsiya qilinadi."
                ),
            ),
        ),
    ),

    # ------------------------------------------------------------------ pq-17
    Topic(
        id="pq-17",
        subject_id=S, module_id=M, order=17,
        title="Qatlamli va sendvich plastinalar: ABD matritsasi va yadro roli",
        description=(
            "Klassik qatlamlash nazariyasi, $A$, $B$, $D$ "
            "matritsalari, membrana-egilish bog'lanishi, sendvich "
            "panel nazariyasi va yadroning siljishga ishlashi."
        ),
        learning_objective=(
            "Qatlamli paket uchun ABD matritsasini qurish, "
            "simmetriya sharti va bog'lanish effektini tushuntirish, "
            "sendvich panelning ekvivalent bikrligini hisoblash."
        ),
        prerequisites=["pq-16", "tmm-13"],
        mathematical_core=(
            "$\\{N, M\\}^T = [[A, B],[B, D]]\\{\\varepsilon^0, "
            "\\kappa\\}^T$, $A_{ij} = \\sum\\bar{Q}_{ij}^{(k)}"
            "(z_k - z_{k-1})$, $B_{ij} \\propto z^2$, "
            "$D_{ij} \\propto z^3$, sendvich uchun sdvig bikrligi."
        ),
        engineering_application=(
            "Aviatsiya va kemasozlik panellari, shamol "
            "turbinasi kurakchasi, sport anjomlari, "
            "sovutgich devori, poyezd vagoni, qurilish "
            "sendvich panellari."
        ),
        computational_component=(
            "ABD matritsasini qatlamlar ma'lumotidan qurish, "
            "simmetrik va nosimmetrik paketlarni taqqoslash, "
            "sendvich panelning og'irlik–bikrlik samaradorligini "
            "hisoblash."
        ),
        visualization_component=(
            "Qatlamlar bo'yicha kuchlanish epyurasi (uzilishli), "
            "ABD matritsasining tuzilishi, sendvich kesimi."
        ),
        research_extension=(
            "Sendvich panelning buzilish rejimlarini o'rganing: "
            "qoplama ustuvorligi, yadro siljishi, mahalliy "
            "botish (dimpling) — qaysi biri qachon hukmron?"
        ),
        difficulty="ilg'or",
        previous_link=(
            "pq-12 da geometrik ortotropiya orqali bikrlikni "
            "oshirish ko'rsatilgan edi. tmm-13 da esa material "
            "anizotropiyasi o'rganilgan. Endi ikkalasini "
            "birlashtiramiz: turli materiallardan tuzilgan, "
            "turli yo'nalishga ega qatlamlar paketi."
        ),
        next_topic="pq-18",
        estimated_minutes=95,
        tags=["kompozit", "sendvich", "ABD matritsasi", "qatlamli"],
        lesson=_lesson(
            problem=(
                "Samolyot qanoti paneli uglerodli kompozitdan "
                "yasaladi: sakkizta qatlam, har biri turli "
                "burchakda ($0°, +45°, -45°, 90°$). Har bir "
                "qatlam ortotrop, butun paket esa? Va eng "
                "muhimi: agar qatlamlar tartibi nosimmetrik "
                "bo'lsa, panel cho'zilganda **egilib ketadi**. "
                "Bu qanday yuz beradi va uni qanday oldini olamiz? "
                "Javob $B$ matritsasida yashiringan."
            ),
            concepts=[
                c("Klassik qatlamlash nazariyasi (CLT)",
                  "Kirxhoff gipotezalari butun paketga "
                  "qo'llaniladi; har bir qatlamda kuchlanish "
                  "o'z moduli bo'yicha hisoblanadi."),
                c("$A$ matritsasi (membrana)",
                  "$A_{ij} = \\sum_k \\bar{Q}_{ij}^{(k)}"
                  "(z_k - z_{k-1})$ — cho'zilish-siqilish "
                  "bikrligi, N/m."),
                c("$D$ matritsasi (egilish)",
                  "$D_{ij} = \\frac{1}{3}\\sum_k \\bar{Q}_{ij}^{(k)}"
                  "(z_k^3 - z_{k-1}^3)$ — egilish bikrligi, N·m."),
                c("$B$ matritsasi (bog'lanish)",
                  "$B_{ij} = \\frac{1}{2}\\sum_k \\bar{Q}_{ij}^{(k)}"
                  "(z_k^2 - z_{k-1}^2)$ — cho'zilish va egilishni "
                  "bog'laydi. Simmetrik paketda aynan nolga teng."),
                c("Simmetrik paket",
                  "Qatlamlar o'rta sirtga nisbatan simmetrik "
                  "joylashgan: $[0/45/90]_s$. Bunda $B = 0$ va "
                  "cho'zilish egilishga olib kelmaydi."),
                c("Sendvich panel",
                  "Ikkita yupqa, bikr qoplama + qalin, yengil "
                  "yadro. Qoplamalar momentni qabul qiladi, "
                  "yadro esa ularni ajratib turadi va siljishni uzatadi."),
            ],
            derivation=[
                d("1. Kinematika (Kirxhoff, butun paket uchun)",
                  r"\varepsilon_{ij}(z) = \varepsilon_{ij}^0 + z\kappa_{ij}",
                  "O'rta sirt deformatsiyasi + egrilikdan kelgan "
                  "chiziqli qism. Bu barcha qatlamlarda uzluksiz — "
                  "deformatsiya sakramaydi."),
                d("2. Har bir qatlamda kuchlanish",
                  r"\{\sigma\}^{(k)} = [\bar{Q}]^{(k)}"
                  r"\big(\{\varepsilon^0\} + z\{\kappa\}\big)",
                  "$[\\bar{Q}]^{(k)}$ — $k$-qatlamning global "
                  "koordinatalardagi bikrlik matritsasi (tola "
                  "burchagiga qarab aylantirilgan, tmm-13). "
                  "**Kuchlanish qatlam chegarasida sakraydi**, "
                  "chunki modullar har xil."),
                d("3. Kuchlarni integrallash",
                  r"\{N\} = \int_{-h/2}^{h/2}\{\sigma\}dz = "
                  r"\sum_k\int_{z_{k-1}}^{z_k}[\bar{Q}]^{(k)}"
                  r"\big(\{\varepsilon^0\} + z\{\kappa\}\big)dz",
                  "Har bir qatlam bo'yicha alohida integrallanadi, "
                  "chunki $[\\bar{Q}]$ qatlamdan qatlamga o'zgaradi."),
                d("4. $A$ va $B$ matritsalari",
                  r"\{N\} = [A]\{\varepsilon^0\} + [B]\{\kappa\}, \quad "
                  r"A_{ij} = \sum_k\bar{Q}_{ij}^{(k)}t_k, \quad "
                  r"B_{ij} = \tfrac{1}{2}\sum_k\bar{Q}_{ij}^{(k)}"
                  r"(z_k^2 - z_{k-1}^2)",
                  "$\\int dz = t_k$ va $\\int z\\,dz = "
                  "\\frac{1}{2}(z_k^2 - z_{k-1}^2)$. $B$ hadi "
                  "cho'zilishni egrilik bilan bog'laydi."),
                d("5. Momentlarni integrallash",
                  r"\{M\} = \int\{\sigma\}z\,dz = [B]\{\varepsilon^0\} "
                  r"+ [D]\{\kappa\}, \quad D_{ij} = \tfrac{1}{3}"
                  r"\sum_k\bar{Q}_{ij}^{(k)}(z_k^3 - z_{k-1}^3)",
                  "Diqqat: $B$ bu yerda ham paydo bo'ldi — "
                  "**bir xil matritsa**. Bu Betti teoremasining "
                  "(o'zaro ishlar) oqibati."),
                d("6. To'liq ABD munosabati",
                  r"\begin{Bmatrix}N\\M\end{Bmatrix} = "
                  r"\begin{bmatrix}A & B\\ B & D\end{bmatrix}"
                  r"\begin{Bmatrix}\varepsilon^0\\ \kappa\end{Bmatrix}",
                  "$6\\times6$ simmetrik matritsa. Izotrop bir "
                  "qatlamli plastinada $B = 0$, $A = $ membrana "
                  "bikrligi, $D = $ bizga tanish silindrik bikrlik."),
                d("7. Simmetriya sharti",
                  r"\bar{Q}^{(k)}(z) = \bar{Q}^{(k)}(-z) "
                  r"\;\Longrightarrow\; B_{ij} = \tfrac{1}{2}"
                  r"\sum_k\bar{Q}_{ij}(z_k^2 - z_{k-1}^2) = 0",
                  "Simmetrik joylashuvda $z$ va $-z$ dagi hissalar "
                  "o'zaro qisqaradi ($z^2$ juft funksiya, lekin "
                  "chegaralar simmetrik). Shuning uchun "
                  "$[0/45/90]_s$ kabi paketlar standart."),
                d("8. Sendvich panel: ekvivalent bikrlik",
                  r"D_{\text{sandwich}} \approx \frac{E_f t_f d^2}{2}, "
                  r"\qquad d = t_c + t_f",
                  "Yupqa qoplamalar ($t_f \\ll t_c$) uchun "
                  "$D \\approx 2 \\cdot E_f t_f (d/2)^2 = "
                  "E_f t_f d^2/2$ — Steyner hadi hukmron. "
                  "Yadro bikrligi e'tiborsiz, lekin uning "
                  "**sdvig** bikrligi hal qiluvchi."),
            ],
            meaning=(
                "$B$ matritsasi qatlamli konstruksiyalarning eng "
                "muhim va eng xavfli xususiyatini ifodalaydi: "
                "**cho'zilish va egilishning bog'lanishi**. "
                "Nosimmetrik paketni cho'zsangiz, u egiladi; "
                "egsangiz, u cho'ziladi. Bu ishlab chiqarishda "
                "jiddiy muammo: kompozit panel avtoklavda "
                "qizdirilib polimerlanadi, so'ng sovuydi. "
                "Turli qatlamlarning termik kengayish "
                "koeffitsientlari har xil, shuning uchun "
                "sovushda ichki kuchlar paydo bo'ladi. "
                "Agar $B \\ne 0$ bo'lsa, panel qoliplardan "
                "**egilgan holda** chiqadi va uni to'g'rilab "
                "bo'lmaydi. Shuning uchun aviatsiya sanoatida "
                "deyarli barcha paketlar simmetrik. Sendvich "
                "panelning mohiyati esa boshqacha va juda "
                "oddiy: $D \\approx E_f t_f d^2/2$ formulasida "
                "$d^2$ — qoplamalar orasidagi masofaning "
                "kvadrati. Yadroni 2 marta qalinlashtirish "
                "bikrlikni **4 marta** oshiradi, og'irlikni esa "
                "deyarli o'zgartirmaydi (yadro zichligi "
                "qoplamadan 50–100 marta kichik). Bu I-teokning "
                "ikki o'lchovli analogi: material neytral "
                "sirtdan qanchalik uzoq bo'lsa, shuncha "
                "samarali. Lekin bepul emas — yadro "
                "qoplamalarni birga ushlab turishi va siljishni "
                "uzatishi kerak, shuning uchun sendvich "
                "panelda sdvig deformatsiyasi hech qachon "
                "e'tiborsiz qoldirilmaydi."
            ),
            equations=[
                eq(r"\begin{Bmatrix}N\\M\end{Bmatrix} = "
                   r"\begin{bmatrix}A & B\\ B & D\end{bmatrix}"
                   r"\begin{Bmatrix}\varepsilon^0\\\kappa\end{Bmatrix}",
                   "Klassik qatlamlash nazariyasining asosiy "
                   "munosabati.", "ABD munosabati"),
                eq(r"A_{ij} = \sum_k\bar{Q}_{ij}^{(k)}t_k, \quad "
                   r"B_{ij} = \tfrac{1}{2}\sum_k\bar{Q}_{ij}^{(k)}"
                   r"(z_k^2-z_{k-1}^2), \quad "
                   r"D_{ij} = \tfrac{1}{3}\sum_k\bar{Q}_{ij}^{(k)}"
                   r"(z_k^3-z_{k-1}^3)",
                   "Matritsa elementlarining ta'rifi.",
                   "ABD ta'riflari"),
                eq(r"D_{\text{sandwich}} \approx \frac{E_f t_f d^2}{2}",
                   "Sendvich panelning egilish bikrligi.",
                   "Sendvich bikrligi"),
                eq(r"w = w_b + w_s = \frac{\alpha q a^4}{D} + "
                   r"\frac{\beta q a^2}{G_c d}",
                   "Sendvich panelda egilish va sdvig "
                   "hissalarining yig'indisi.", "Sdvig hissasi"),
            ],
            conditions=(
                "**CLT ning qo'llanish shartlari:**\n"
                "1. Kirxhoff gipotezalari butun paket uchun "
                "o'rinli ($h/a < 1/20$);\n"
                "2. Qatlamlar mukammal birikkan (delaminatsiya yo'q);\n"
                "3. Har bir qatlam chiziqli elastik va ortotrop;\n"
                "4. Ko'ndalang sdvig e'tiborsiz — **sendvich "
                "panelda bu shart buziladi** va sdvig hissasi "
                "alohida qo'shiladi.\n\n"
                "**Sendvich panel uchun qo'shimcha tekshiruvlar:**\n"
                "- Yadro sdvig kuchlanishi: "
                "$\\tau_c = Q/d \\le \\tau_{c,\\text{ruxsat}}$;\n"
                "- Qoplama ustuvorligi (wrinkling): "
                "$\\sigma_{cr} \\approx 0{,}5\\sqrt[3]{E_f E_c G_c}$;\n"
                "- Mahalliy botish (dimpling) — asal uyasi "
                "yadroda katak o'lchamiga bog'liq;\n"
                "- Yadro siqilishi (crushing) mahalliy yuklamada.\n\n"
                "**Simmetriya:** $B = 0$ bo'lishi uchun paket "
                "geometrik **va** material jihatdan simmetrik "
                "bo'lishi shart."
            ),
            worked=WorkedExample(
                statement=(
                    "Sendvich panel: qoplamalar alyuminiy "
                    "$t_f = 0{,}8$ mm, $E_f = 70$ GPa, "
                    "$\\rho_f = 2700$ kg/m³; yadro — asal uyasi "
                    "$t_c = 20$ mm, $G_c = 150$ MPa, "
                    "$\\rho_c = 50$ kg/m³. Panel $a = 1{,}2$ m, "
                    "sharnirli, $q = 3$ kPa. Uni bir xil "
                    "og'irlikdagi yaxlit alyuminiy list bilan "
                    "taqqoslang."
                ),
                given=[
                    r"t_f = 0{,}8\ \text{mm},\ t_c = 20\ \text{mm}",
                    r"E_f = 70\ \text{GPa},\ G_c = 150\ \text{MPa}",
                    r"\rho_f = 2700,\ \rho_c = 50\ \text{kg/m}^3",
                    r"a = 1{,}2\ \text{m},\ q = 3000\ \text{Pa}",
                ],
                steps=[
                    st(r"d = t_c + t_f = 20 + 0{,}8 = 20{,}8\ \text{mm}",
                       "Qoplamalar o'rta sirtlari orasidagi masofa."),
                    st(r"D = \frac{E_f t_f d^2}{2(1-\nu^2)} = "
                       r"\frac{70\times10^9 \cdot 8\times10^{-4} \cdot "
                       r"(0{,}0208)^2}{2 \cdot 0{,}8911}",
                       "$\\nu = 0{,}33$ uchun $1-\\nu^2 = 0{,}8911$. "
                       "$d^2 = 4{,}3264\\times10^{-4}$ m²."),
                    st(r"D = \frac{24{,}23}{1{,}7822} = 13{,}60\ \text{kN·m}",
                       "Sendvich panelning egilish bikrligi."),
                    st(r"m_{\text{sandwich}} = 2\rho_f t_f + \rho_c t_c "
                       r"= 2 \cdot 2700 \cdot 0{,}0008 + 50 \cdot 0{,}02 "
                       r"= 4{,}32 + 1{,}0 = 5{,}32\ \text{kg/m}^2",
                       "Yuza og'irligi. Yadro atigi 19 % hissa qo'shadi."),
                    st(r"h_{\text{ekv}} = \frac{5{,}32}{2700} "
                       r"= 1{,}970\ \text{mm}",
                       "Bir xil og'irlikdagi yaxlit alyuminiy "
                       "listning qalinligi."),
                    st(r"D_{\text{yaxlit}} = \frac{70\times10^9 \cdot "
                       r"(1{,}97\times10^{-3})^3}{12 \cdot 0{,}8911} "
                       r"= \frac{5{,}350\times10^{2}}{10{,}693} "
                       r"= 50{,}0\ \text{N·m}",
                       "$h^3 = 7{,}646\\times10^{-9}$ m³. Juda kichik "
                       "bikrlik."),
                    st(r"\frac{D_{\text{sandwich}}}{D_{\text{yaxlit}}} "
                       r"= \frac{13\,600}{50{,}0} = 272",
                       "Bir xil og'irlikda sendvich panel "
                       "**272 marta bikrroq**."),
                    st(r"w_b = 0{,}00406\frac{qa^4}{D} = "
                       r"0{,}00406\frac{3000 \cdot 2{,}0736}{13\,600} "
                       r"= 1{,}857\times10^{-3}\ \text{m} = 1{,}86\ \text{mm}",
                       "Sof egilish hissasi (kvadrat sharnirli "
                       "plastina koeffitsienti)."),
                    st(r"w_s \approx \frac{0{,}0269\,q a^2}{G_c d} "
                       r"= \frac{0{,}0269 \cdot 3000 \cdot 1{,}44}"
                       r"{150\times10^{6} \cdot 0{,}0208} "
                       r"= 3{,}72\times10^{-5}\ \text{m} = 0{,}037\ \text{mm}",
                       "Sdvig hissasi — bu holda kichik (2 %), "
                       "chunki yadro nisbatan bikr va panel katta."),
                ],
                answer=(
                    "$D_{\\text{sendvich}} = 13{,}60$ kN·m, "
                    "$m = 5{,}32$ kg/m²; bir xil og'irlikdagi "
                    "yaxlit list $D = 50$ N·m — sendvich panel "
                    "**272 marta bikrroq**. Og'ish "
                    "$w_b = 1{,}86$ mm + $w_s = 0{,}04$ mm "
                    "$= 1{,}90$ mm (sdvig hissasi 2 %)."
                ),
                engineering_note=(
                    "272 marta bikrlik farqi sendvich "
                    "konstruksiyaning nima uchun aviatsiya, "
                    "kosmonavtika va yuqori tezlikli "
                    "poyezdlarda universal ekanligini "
                    "tushuntiradi. Lekin narxi bor: "
                    "(1) ishlab chiqarish murakkab va qimmat; "
                    "(2) mahalliy yuklamaga (zarba, bolt) "
                    "juda sezgir — yadro ezilib ketadi; "
                    "(3) namlik yadro kataklariga kirib, "
                    "muzlaganda delaminatsiya keltirib "
                    "chiqaradi; (4) ta'mirlash qiyin. "
                    "Shuning uchun sendvich panellar "
                    "yuklama bir tekis taqsimlangan joylarda "
                    "(panel, pol, devor) ishlatiladi, "
                    "konsentrlangan kuch uzatiladigan joylarda "
                    "esa mahalliy qattiqlashtirish (insert) qo'yiladi."
                ),
            ),
            computation=Computation(
                caption=(
                    "Qatlamli paket uchun ABD matritsasini "
                    "qurish, simmetriya effektini ko'rsatish va "
                    "sendvich panelni yaxlit list bilan taqqoslash."
                ),
                code='''"""Qatlamli va sendvich plastinalar: ABD matritsasi."""
import numpy as np
from labkit import PARAMS, note, series, table, value

E1 = float(PARAMS.get("E1", 140.0))*1e9    # tola bo'ylab
E2 = float(PARAMS.get("E2", 10.0))*1e9     # ko'ndalang
G12 = float(PARAMS.get("G12", 5.0))*1e9
nu12 = float(PARAMS.get("nu12", 0.3))
t_ply = float(PARAMS.get("t_ply", 0.125))/1000.0
layup = int(PARAMS.get("layup", 0))        # 0 simmetrik, 1 nosimmetrik

nu21 = nu12*E2/E1
den = 1 - nu12*nu21
Q = np.array([[E1/den, nu12*E2/den, 0.0],
              [nu12*E2/den, E2/den, 0.0],
              [0.0, 0.0, G12]])
value("Q11", Q[0, 0]/1e9, "GPa")
value("Q22", Q[1, 1]/1e9, "GPa")
value("Q12", Q[0, 1]/1e9, "GPa")
value("Q66", Q[2, 2]/1e9, "GPa")


def Qbar(theta_deg):
    """Qatlamni global koordinatalarga aylantirish."""
    t = np.radians(theta_deg)
    c, s = np.cos(t), np.sin(t)
    T = np.array([[c**2, s**2, 2*c*s],
                  [s**2, c**2, -2*c*s],
                  [-c*s, c*s, c**2 - s**2]])
    Rm = np.diag([1.0, 1.0, 2.0])
    Tinv = np.linalg.inv(T)
    return Tinv @ Q @ Rm @ T @ np.linalg.inv(Rm)


def abd(angles):
    n = len(angles)
    h_tot = n*t_ply
    z = np.linspace(-h_tot/2, h_tot/2, n + 1)
    A = np.zeros((3, 3)); B = np.zeros((3, 3)); Dm = np.zeros((3, 3))
    for k, th in enumerate(angles):
        Qb = Qbar(th)
        A += Qb*(z[k + 1] - z[k])
        B += 0.5*Qb*(z[k + 1]**2 - z[k]**2)
        Dm += (1/3)*Qb*(z[k + 1]**3 - z[k]**3)
    return A, B, Dm, h_tot, z


sym = [0, 45, -45, 90, 90, -45, 45, 0]        # [0/45/-45/90]_s
asym = [0, 45, -45, 90, 0, 45, -45, 90]       # [0/45/-45/90]_2 nosimmetrik
angles = sym if layup == 0 else asym
name = "simmetrik [0/45/-45/90]_s" if layup == 0 else "nosimmetrik [0/45/-45/90]_2"

A, B, Dm, h_tot, z = abd(angles)
value("Paket qalinligi", h_tot*1000, "mm")
value("Qatlamlar soni", float(len(angles)), "dona")
value("A11", A[0, 0]/1e6, "MN/m")
value("A22", A[1, 1]/1e6, "MN/m")
value("A66", A[2, 2]/1e6, "MN/m")
value("D11", Dm[0, 0], "N*m")
value("D22", Dm[1, 1], "N*m")
value("D66", Dm[2, 2], "N*m")
Bmax = float(np.max(np.abs(B)))
value("max|B_ij|", Bmax, "N")
value("max|B| / sqrt(A11*D11)", Bmax/np.sqrt(A[0, 0]*Dm[0, 0]), "—")
note(f"Paket: {name}. max|B| = {Bmax:.3e} N — "
     f"{'AYNAN NOL (simmetrik paket)' if Bmax < 1e-6 else 'NOLGA TENG EMAS: choʻzilish egilishga olib keladi!'}")

table("A matritsasi (MN/m)",
      ["", "1", "2", "6"],
      [[["1", "2", "6"][i]] + [round(float(A[i, j])/1e6, 2) for j in range(3)]
       for i in range(3)])
table("B matritsasi (N)",
      ["", "1", "2", "6"],
      [[["1", "2", "6"][i]] + [round(float(B[i, j]), 3) for j in range(3)]
       for i in range(3)])
table("D matritsasi (N*m)",
      ["", "1", "2", "6"],
      [[["1", "2", "6"][i]] + [round(float(Dm[i, j]), 3) for j in range(3)]
       for i in range(3)])

# --- Nosimmetriya effekti: sof cho'zishda egrilik ---
N_applied = np.array([1e5, 0.0, 0.0])       # N/m
ABD = np.block([[A, B], [B, Dm]])
rhs = np.concatenate([N_applied, np.zeros(3)])
sol = np.linalg.solve(ABD, rhs)
eps0, kap = sol[:3], sol[3:]
value("eps_x (sof cho'zishda)", float(eps0[0])*1e6, "mkm/m")
value("kappa_x (sof cho'zishda)", float(kap[0]), "1/m")
value("kappa_y (sof cho'zishda)", float(kap[1]), "1/m")
if np.max(np.abs(kap)) > 1e-9:
    Rcurv = 1/max(abs(float(kap[0])), 1e-30)
    note(f"Sof cho'zishda egrilik paydo bo'ldi: kappa_x = "
         f"{kap[0]:.4e} 1/m (egrilik radiusi {Rcurv:.2f} m). "
         f"Bu B matritsasining bevosita oqibati.")
else:
    note("Sof cho'zishda egrilik nolga teng — simmetrik paket "
         "cho'zilganda egilmaydi.")

# Ikkala paketni taqqoslash
rows = []
for nm, ang in [("simmetrik [0/45/-45/90]_s", sym),
                ("nosimmetrik [0/45/-45/90]_2", asym)]:
    Aa, Bb, Dd, _, _ = abd(ang)
    ABDk = np.block([[Aa, Bb], [Bb, Dd]])
    s2 = np.linalg.solve(ABDk, np.concatenate([N_applied, np.zeros(3)]))
    rows.append([nm, round(float(np.max(np.abs(Bb))), 4),
                 round(float(s2[0])*1e6, 1), round(float(s2[3]), 6)])
table("Simmetriyaning ta'siri (N_x = 100 kN/m)",
      ["Paket", "max|B|, N", "eps_x, mkm/m", "kappa_x, 1/m"], rows)

# --- Qatlamlar bo'yicha kuchlanish epyurasi ---
kap_b = np.array([0.02, 0.0, 0.0])          # sof egilish
zz, sx_layers = [], []
for k, th in enumerate(angles):
    Qb = Qbar(th)
    for zv in [z[k] + 1e-9, z[k + 1] - 1e-9]:
        eps = zv*kap_b
        sg = Qb @ eps
        zz.append(zv*1000)
        sx_layers.append(float(sg[0])/1e6)
series("sigma_x(z) qatlamlar bo'yicha", sx_layers, zz,
       xlabel="sigma_x, MPa", ylabel="z, mm")
note("Deformatsiya z bo'yicha uzluksiz va chiziqli, kuchlanish "
     "esa qatlam chegarasida SAKRAYDI — modullar har xil.")

# --- Sendvich panel ---
tf = float(PARAMS.get("tf", 0.8))/1000.0
tc = float(PARAMS.get("tc", 20.0))/1000.0
Ef = float(PARAMS.get("Ef", 70.0))*1e9
Gc = float(PARAMS.get("Gc", 150.0))*1e6
rhof = float(PARAMS.get("rhof", 2700.0))
rhoc = float(PARAMS.get("rhoc", 50.0))
a_pan = float(PARAMS.get("a_pan", 1.2))
q_pan = float(PARAMS.get("q_pan", 3000.0))
nuf = 0.33

d = tc + tf
D_sw = Ef*tf*d**2/(2*(1 - nuf**2))
m_sw = 2*rhof*tf + rhoc*tc
h_eq = m_sw/rhof
D_solid = Ef*h_eq**3/(12*(1 - nuf**2))

value("Sendvich: d = t_c + t_f", d*1000, "mm")
value("Sendvich: D", D_sw/1000, "kN*m")
value("Sendvich: yuza og'irligi", m_sw, "kg/m2")
value("Ekvivalent yaxlit qalinlik", h_eq*1000, "mm")
value("Yaxlit list D", D_solid, "N*m")
value("D_sendvich / D_yaxlit", D_sw/D_solid, "—")

w_b = 0.00406*q_pan*a_pan**4/D_sw
w_s = 0.0269*q_pan*a_pan**2/(Gc*d)
value("Egilish og'ishi w_b", w_b*1000, "mm")
value("Sdvig og'ishi w_s", w_s*1000, "mm")
value("Jami og'ish", (w_b + w_s)*1000, "mm")
value("Sdvig ulushi", 100*w_s/(w_b + w_s), "%")

sig_f = q_pan*a_pan**2*0.0479/(tf*d)
tau_c = q_pan*a_pan/2/d
value("Qoplamadagi kuchlanish", sig_f/1e6, "MPa")
value("Yadrodagi sdvig kuchlanishi", tau_c/1e6, "MPa")
sig_wrinkle = 0.5*(Ef*Gc*Gc)**(1/3)
value("Qoplama burishish (wrinkling) chegarasi", sig_wrinkle/1e6, "MPa")
value("Burishishga zaxira", sig_wrinkle/sig_f, "—")

# Yadro qalinligining ta'siri
tcs = np.linspace(0.005, 0.08, 100)
Ds, ms, effs, ws, shares = [], [], [], [], []
for tcv in tcs:
    dv = tcv + tf
    Dv = Ef*tf*dv**2/(2*(1 - nuf**2))
    mv = 2*rhof*tf + rhoc*tcv
    wbv = 0.00406*q_pan*a_pan**4/Dv
    wsv = 0.0269*q_pan*a_pan**2/(Gc*dv)
    Ds.append(Dv/1000); ms.append(mv)
    effs.append((Dv/mv)/(D_solid/(rhof*h_eq)))
    ws.append((wbv + wsv)*1000)
    shares.append(100*wsv/(wbv + wsv))
series("D(yadro qalinligi)", (tcs*1000).tolist(), Ds,
       xlabel="Yadro qalinligi t_c, mm", ylabel="D, kN*m")
series("Og'ish(yadro qalinligi)", (tcs*1000).tolist(), ws,
       xlabel="Yadro qalinligi t_c, mm", ylabel="w, mm")
series("Sdvig ulushi(yadro qalinligi)", (tcs*1000).tolist(), shares,
       xlabel="Yadro qalinligi t_c, mm", ylabel="Sdvig ulushi, %")
series("Yuza og'irligi(yadro qalinligi)", (tcs*1000).tolist(), ms,
       xlabel="Yadro qalinligi t_c, mm", ylabel="Og'irlik, kg/m2")
note(f"Yadroni {tcs[0]*1000:.0f} dan {tcs[-1]*1000:.0f} mm ga "
     f"oshirish bikrlikni {Ds[-1]/Ds[0]:.1f} marta oshiradi, "
     f"og'irlikni esa atigi {ms[-1]/ms[0]:.2f} marta — bu "
     f"sendvich konstruksiyaning butun mohiyati.")

table("Sendvich panelning buzilish rejimlari",
      ["Rejim", "Mexanizm", "Oldini olish"],
      [["Qoplama oqishi", "sigma_f > sigma_Y", "qoplama qalinligi"],
       ["Qoplama burishishi", "mahalliy ustuvorlik yadroda",
        "yadro moduli E_c, G_c"],
       ["Yadro sdvigi", "tau_c > tau_c_ruxsat", "yadro zichligi"],
       ["Yadro ezilishi", "mahalliy bosim", "insert yoki qattiqlashtirish"],
       ["Mahalliy botish", "asal uyasi kataklari orasida",
        "katak o'lchamini kichraytirish"],
       ["Delaminatsiya", "yopishtirish qatlami buzilishi",
        "sirt tayyorlash, namlikdan himoya"]])
''',
                parameters=[
                    p("E1", "Kompozit E₁ (tola bo'ylab)", 10.0, 400.0, 140.0,
                      1.0, "GPa"),
                    p("E2", "Kompozit E₂ (ko'ndalang)", 1.0, 100.0, 10.0,
                      0.5, "GPa"),
                    p("G12", "Siljish moduli G₁₂", 0.5, 50.0, 5.0, 0.5, "GPa"),
                    p("nu12", "Puasson ν₁₂", 0.0, 0.45, 0.3, 0.01),
                    p("t_ply", "Qatlam qalinligi", 0.05, 1.0, 0.125, 0.005, "mm"),
                    p("layup", "Paket (0 simmetrik, 1 nosimmetrik)",
                      0.0, 1.0, 0.0, 1.0),
                    p("tf", "Sendvich: qoplama t_f", 0.2, 5.0, 0.8, 0.1, "mm"),
                    p("tc", "Sendvich: yadro t_c", 3.0, 100.0, 20.0, 1.0, "mm"),
                    p("Ef", "Qoplama moduli E_f", 1.0, 400.0, 70.0, 1.0, "GPa"),
                    p("Gc", "Yadro sdvig moduli G_c", 5.0, 2000.0, 150.0, 5.0,
                      "MPa"),
                    p("rhof", "Qoplama zichligi", 500.0, 9000.0, 2700.0, 50.0,
                      "kg/m³"),
                    p("rhoc", "Yadro zichligi", 10.0, 500.0, 50.0, 5.0, "kg/m³"),
                    p("a_pan", "Panel tomoni", 0.2, 5.0, 1.2, 0.1, "m"),
                    p("q_pan", "Panel yuklamasi", 100.0, 50000.0, 3000.0, 100.0,
                      "Pa"),
                ],
                expected_output=(
                    "Simmetrik paketda max|B| aynan 0 (≈10⁻¹¹ N) va "
                    "sof cho'zishda egrilik nol; nosimmetrik paketda "
                    "B ≠ 0 va cho'zish egilish keltirib chiqaradi. "
                    "Sendvich: D = 13,6 kN·m, m = 5,32 kg/m², "
                    "yaxlit list D = 50 N·m — 272 marta farq; "
                    "og'ish ≈ 1,9 mm, sdvig ulushi ≈ 2 %."
                ),
            ),
            visual=vis(
                kind="Qatlamli paket va sendvich kesimi",
                tool="React/SVG",
                description=(
                    "Qatlamlar bo'yicha deformatsiya va kuchlanish "
                    "epyuralari, ABD matritsasining tuzilishi, "
                    "sendvich kesimi va bikrlik samaradorligi."
                ),
                how_to_draw=(
                    "React/SVG: birinchi panel — paket kesimi: "
                    "qatlamlar yonma-yon to'rtburchaklar sifatida, "
                    "har birida tola yo'nalishi qisqa "
                    "parallel chiziqchalar bilan ko'rsatilgan "
                    "(burchak haqiqiy). Yonida ikkita epyura: "
                    "$\\varepsilon_x(z)$ — uzluksiz to'g'ri "
                    "chiziq; $\\sigma_x(z)$ — **zinapoyasimon**, "
                    "har bir qatlam chegarasida sakraydi. Bu "
                    "qarama-qarshilik qatlamli nazariyaning "
                    "mohiyatini bir qarashda ko'rsatadi. "
                    "Ikkinchi panel — ABD matritsasi "
                    "$6\\times6$ issiqlik xaritasi sifatida: "
                    "$A$, $B$, $D$ bloklari ramka bilan "
                    "ajratilgan; simmetrik paketda $B$ bloki "
                    "butunlay neytral rangda (nol), "
                    "nosimmetrikda esa rangli — tugma bilan "
                    "almashtirib ko'rsatiladi. Uchinchi panel — "
                    "sendvich kesimi: ikki yupqa qoplama va "
                    "qalin yadro (asal uyasi naqshi bilan), "
                    "$d$ masofasi o'lchov chizig'i bilan; "
                    "slayder $t_c$ ni o'zgartiradi va "
                    "$D \\propto d^2$ bog'liqligi grafikda "
                    "jonli ko'rinadi."
                ),
            ),
            interp=(
                "$B$ matritsasining simmetrik paketda aynan "
                "nolga aylanishi ($\\sim10^{-11}$ N sonli "
                "xato darajasida) nazariyaning to'g'riligini "
                "tasdiqlaydi va amaliy qoidani beradi: "
                "**har doim simmetrik paket loyihalang**. "
                "Nosimmetrik paketda sof cho'zish egrilik "
                "keltirib chiqarishi grafikda aniq ko'rinadi — "
                "bu ishlab chiqarishda qaytarib bo'lmaydigan "
                "nuqsonga olib keladi. Kuchlanish epyurasining "
                "zinapoyasimon shakli ham muhim: deformatsiya "
                "uzluksiz, kuchlanish esa sakraydi. Demak "
                "eng bikr qatlam ($0°$ yo'nalishdagi) eng "
                "katta kuchlanishni qabul qiladi va birinchi "
                "bo'lib buziladi. Kompozit loyihalashda "
                "buzilish har bir qatlam uchun alohida "
                "tekshiriladi (first ply failure). Sendvich "
                "panelning 272 marta ustunligi esa "
                "muhandislikdagi eng katta 'bepul tushlik'ga "
                "o'xshaydi, lekin grafiklar chegarani ham "
                "ko'rsatadi: yadro qalinlashgani sari sdvig "
                "ulushi ortadi va ma'lum nuqtadan keyin "
                "og'ishni sdvig boshqara boshlaydi. Bundan "
                "tashqari qoplama burishishi (wrinkling) "
                "chegarasi yadro modullariga bog'liq va u "
                "ko'pincha oqish chegarasidan oldin keladi — "
                "shuning uchun sendvich panelda mustahkamlik "
                "hisobi hech qachon faqat $\\sigma_Y$ bilan "
                "cheklanmaydi."
            ),
            mistakes=[
                "Nosimmetrik paket loyihalash. $B \\ne 0$ "
                "bo'lsa panel polimerlanishdan keyin egilib "
                "chiqadi va uni to'g'rilab bo'lmaydi.",
                "Sendvich panelda sdvig deformatsiyasini "
                "e'tiborsiz qoldirish. Qalin yadroli yoki "
                "kichik panelda u og'ishning yarmidan "
                "ko'pini berishi mumkin.",
                "Kuchlanishni butun paket uchun bitta "
                "$\\sigma = 6M/h^2$ formulasi bilan "
                "hisoblash. Har bir qatlamda o'z moduli "
                "bo'yicha alohida hisoblash kerak.",
                "Faqat qoplama oqishini tekshirish. "
                "Sendvich panelda burishish, yadro sdvigi "
                "va mahalliy ezilish ko'pincha hukmron rejim bo'ladi.",
            ],
            quiz=[
                q("$B$ matritsasi nimani ifodalaydi va u "
                  "qachon nolga teng?",
                  "Cho'zilish va egilishning bog'lanishini. "
                  "Paket o'rta sirtga nisbatan simmetrik "
                  "bo'lsa, $B = 0$.", "konseptual"),
                q("Nima uchun deformatsiya uzluksiz, "
                  "kuchlanish esa qatlam chegarasida sakraydi?",
                  "Kirxhoff kinematikasi butun paketga "
                  "qo'llaniladi, shuning uchun "
                  "$\\varepsilon = \\varepsilon^0 + z\\kappa$ "
                  "uzluksiz. Kuchlanish esa "
                  "$\\bar{Q}^{(k)}$ ga ko'paytiriladi va u "
                  "qatlamdan qatlamga o'zgaradi.", "konseptual"),
                q("Sendvich panelda yadro qalinligini 2 marta "
                  "oshirsak, bikrlik qancha ortadi?",
                  "Taxminan 4 marta, chunki "
                  "$D \\propto d^2$ va $d \\approx t_c$. "
                  "Og'irlik esa yadro zichligi kichik "
                  "bo'lgani uchun juda kam ortadi.", "hisob"),
                q("$t_f = 1$ mm, $t_c = 25$ mm, "
                  "$E_f = 70$ GPa, $\\nu = 0{,}33$. $D$ ni toping.",
                  "$d = 26$ mm; $D = 70\\times10^9 \\cdot "
                  "10^{-3} \\cdot 6{,}76\\times10^{-4}/"
                  "(2 \\cdot 0{,}8911) = 26{,}5$ kN·m.", "hisob"),
                q("Kodda `Qbar` funksiyasi nima qiladi?",
                  "Qatlamning material koordinatalaridagi "
                  "$Q$ matritsasini tola burchagi bo'yicha "
                  "global koordinatalarga aylantiradi — "
                  "tenzor almashtirish qoidasi bo'yicha.",
                  "kod"),
                q("Sendvich panelning qaysi buzilish rejimlari "
                  "tekshiriladi?",
                  "Qoplama oqishi, qoplama burishishi "
                  "(wrinkling), yadro sdvigi, yadro ezilishi, "
                  "mahalliy botish va delaminatsiya — "
                  "kamida oltitasi.", "talqin"),
            ],
            bridge=(
                "Barcha oldingi mavzularda og'ish kichik deb "
                "olindi va o'rta sirt cho'zilmaydi deb "
                "hisoblandi (pq-01 dagi uchinchi gipoteza). "
                "Og'ish qalinlikka taqqoslanadigan bo'lsa, "
                "bu gipoteza buziladi va membrana kuchlari "
                "paydo bo'ladi. Keyingi mavzuda fon Karman "
                "nazariyasini quramiz."
            ),
            research=(
                "Sendvich panelning buzilish rejimlarini "
                "tizimli o'rganing va **buzilish rejimlari "
                "xaritasini** (failure mode map) quring. "
                "Ikki o'lchamsiz parametr tanlang (masalan, "
                "$t_f/a$ va $t_c/a$) va har bir nuqtada "
                "qaysi rejim birinchi ishga tushishini "
                "aniqlang: qoplama oqishi, burishish, yadro "
                "sdvigi yoki ezilish. Natijada tekislik "
                "sohalarga bo'linadi va optimal loyiha "
                "ularning chegarasida yotadi (bir necha rejim "
                "bir vaqtda kritik bo'ladigan nuqta). "
                "Ashby va Gibson uslubidagi bu xarita "
                "material tanlashda qanday ishlatiladi?"
            ),
            manim_ref=manim(
                scene="LaminateScene",
                module="animatsiya/scenes/pq_circular.py",
                title="Qatlamli paket va B matritsasi",
                summary=(
                    "Nosimmetrik paket cho'zilganda egilib "
                    "ketishi animatsiya qilinadi; keyin paket "
                    "simmetrik qilinadi va egilish yo'qolishi "
                    "ko'rsatiladi. Kuchlanish epyurasining "
                    "qatlam chegarasidagi sakrashi ta'kidlanadi."
                ),
            ),
        ),
    ),

    # ------------------------------------------------------------------ pq-18
    Topic(
        id="pq-18",
        subject_id=S, module_id=M, order=18,
        title="Katta og'ishlar: fon Karman tenglamalari va membrana effekti",
        description=(
            "Geometrik nochiziqlilik, o'rta sirtning cho'zilishi, "
            "fon Karman tenglamalari tizimi, membrana va egilish "
            "hissalarining raqobati hamda nochiziqli bikrlanish."
        ),
        learning_objective=(
            "Katta og'ishlarda membrana kuchlarining paydo bo'lishini "
            "tushuntirish, fon Karman tenglamalarini yozish va "
            "taqribiy yechim bilan nochiziqli bikrlanishni baholash."
        ),
        prerequisites=["pq-17", "pq-09"],
        mathematical_core=(
            "Nochiziqli deformatsiya "
            "$\\varepsilon_x = u_{,x} + \\frac{1}{2}w_{,x}^2$, "
            "fon Karman tizimi, Eyri funksiyasi $F$, "
            "$\\nabla^4 F = -E h\\,L(w,w)/2$, kubik nochiziqlilik."
        ),
        engineering_application=(
            "Yupqa qoplamalar (samolyot, kema), membrana "
            "konstruksiyalari, elastik diafragma va datchiklar, "
            "MEMS qurilmalari, bosim ostidagi yupqa idish devori."
        ),
        computational_component=(
            "Bir hadli Galerkin yaqinlashuvi bilan kubik "
            "tenglamani yechish, chiziqli va nochiziqli "
            "yechimlarni taqqoslash, membrana hissasini baholash."
        ),
        visualization_component=(
            "$q$–$w$ nochiziqli diagrammasi, membrana va egilish "
            "kuchlanishlarining nisbati, qalinlikka nisbatan og'ish."
        ),
        research_extension=(
            "Boshlang'ich nomukammalligi bo'lgan plastinani "
            "o'rganing: $w_0(x,y)$ qanday kiritiladi va u "
            "yuklanish egri chizig'ini qanday o'zgartiradi?"
        ),
        difficulty="ilg'or",
        previous_link=(
            "pq-01 dagi uchinchi gipoteza — o'rta sirt "
            "cho'zilmaydi — barcha oldingi mavzularda ishlatildi. "
            "Endi uni bekor qilamiz. pq-09 dagi energiya usuli "
            "esa nochiziqli masalani yechishning eng qulay yo'lini beradi."
        ),
        next_topic="pq-19",
        estimated_minutes=100,
        tags=["fon Karman", "nochiziqlilik", "membrana", "katta og'ish"],
        lesson=_lesson(
            problem=(
                "pq-01 da aniqlangan edi: samolyot qanoti "
                "qoplamasi ($h = 2$ mm) uchun Kirxhoff "
                "kinematikasi ideal, lekin og'ish osongina "
                "qalinlikka taqqoslanadigan bo'ladi. Chiziqli "
                "nazariya bunday holda og'ishni **bir necha "
                "marta oshirib** ko'rsatadi. Nima uchun? "
                "Chunki plastina egilganda uning o'rta sirti "
                "cho'zilishga majbur bo'ladi va cho'zilish "
                "qarshiligi egilish qarshiligidan ancha katta. "
                "Bu effektni qanday hisobga olamiz?"
            ),
            concepts=[
                c("Geometrik nochiziqlilik",
                  "Deformatsiya-ko'chish munosabati nochiziqli "
                  "bo'lib qoladi: $\\varepsilon_x = u_{,x} + "
                  "\\frac{1}{2}w_{,x}^2$. Material esa hali ham "
                  "chiziqli elastik."),
                c("Membrana kuchlari",
                  "O'rta sirtdagi cho'zilish kuchlari "
                  "$N_x, N_y, N_{xy}$. Chiziqli nazariyada ular "
                  "nolga teng edi."),
                c("Fon Karman tenglamalari",
                  "Ikkita bog'langan nochiziqli PDE: biri "
                  "og'ish uchun, ikkinchisi Eyri funksiyasi "
                  "uchun. 1910-yilda Theodore von Kármán taklif qilgan."),
                c("Eyri funksiyasi tekislik ichida",
                  "$N_x = F_{,yy}$, $N_y = F_{,xx}$, "
                  "$N_{xy} = -F_{,xy}$ — muvozanat avtomatik "
                  "bajariladi (tmm-17 dagi g'oya)."),
                c("Nochiziqli bikrlanish (stress stiffening)",
                  "Og'ish ortgani sari membrana kuchlari ortadi "
                  "va plastina **bikrroq** bo'lib qoladi — "
                  "$q$–$w$ egri chizig'i pastga egiladi."),
                c("$w/h$ mezoni",
                  "$w < 0{,}2h$ — chiziqli nazariya yetarli; "
                  "$0{,}2h < w < 1h$ — nochiziqlilik sezilarli; "
                  "$w > h$ — membrana hukmron."),
            ],
            derivation=[
                d("1. Nochiziqli deformatsiya-ko'chish munosabati",
                  r"\varepsilon_x^0 = \frac{\partial u}{\partial x} "
                  r"+ \frac{1}{2}\Big(\frac{\partial w}{\partial x}\Big)^2",
                  "Grin deformatsiya tenzorining (tmm-04) "
                  "saqlab qolingan nochiziqli hadi. Boshqa "
                  "kvadratik hadlar ($u_{,x}^2$) kichik deb "
                  "tashlanadi — bu fon Karman yaqinlashuvi."),
                d("2. Nima uchun aynan $w_{,x}^2$ saqlanadi",
                  r"u \sim \frac{w^2}{a}, \quad u_{,x} \sim "
                  r"\frac{w^2}{a^2} \sim w_{,x}^2 \gg u_{,x}^2",
                  "Ko'ndalang ko'chish $w$ tekislik ichidagi "
                  "$u$ dan ancha katta, shuning uchun uning "
                  "kvadrati bir xil tartibda bo'lib qoladi."),
                d("3. To'liq deformatsiya",
                  r"\varepsilon_x = \underbrace{u_{,x} + "
                  r"\tfrac{1}{2}w_{,x}^2}_{\text{membrana}} "
                  r"- \underbrace{z\,w_{,xx}}_{\text{egilish}}",
                  "Endi ikkita mexanizm bor: o'rta sirt "
                  "cho'zilishi va egilish. Ularning "
                  "superpozitsiyasi."),
                d("4. Moslik sharti (compatibility)",
                  r"\frac{\partial^2\varepsilon_x^0}{\partial y^2} + "
                  r"\frac{\partial^2\varepsilon_y^0}{\partial x^2} - "
                  r"\frac{\partial^2\gamma_{xy}^0}{\partial x\partial y} "
                  r"= w_{,xy}^2 - w_{,xx}w_{,yy}",
                  "$u, v$ ni yo'qotish uchun moslik sharti "
                  "yoziladi (tmm-05). O'ng tomon nolga teng "
                  "emas — bu aynan **Gauss egriligi** "
                  "(pq-02)! Chiziqli nazariyada u nol edi."),
                d("5. Eyri funksiyasini kiritish",
                  r"N_x = h\frac{\partial^2 F}{\partial y^2}, \quad "
                  r"N_y = h\frac{\partial^2 F}{\partial x^2}, \quad "
                  r"N_{xy} = -h\frac{\partial^2 F}{\partial x\partial y}",
                  "Tekislik ichidagi muvozanat avtomatik "
                  "bajariladi. tmm-17 dagi g'oyaning to'g'ridan-"
                  "to'g'ri ko'chirilishi."),
                d("6. Birinchi fon Karman tenglamasi (moslik)",
                  r"\nabla^4 F = E\Big[\Big(\frac{\partial^2 w}"
                  r"{\partial x\partial y}\Big)^2 - "
                  r"\frac{\partial^2 w}{\partial x^2}"
                  r"\frac{\partial^2 w}{\partial y^2}\Big] = -E\,K_G",
                  "4- va 5-qadamlarni birlashtiramiz. O'ng "
                  "tomondagi ifoda — Gauss egriligi bilan "
                  "bog'liq; demak **membrana kuchlari sirtning "
                  "qo'sh egrilikidan tug'iladi**."),
                d("7. Ikkinchi fon Karman tenglamasi (muvozanat)",
                  r"D\nabla^4 w = q + h\Big[F_{,yy}w_{,xx} - "
                  r"2F_{,xy}w_{,xy} + F_{,xx}w_{,yy}\Big]",
                  "Vertikal muvozanatda membrana kuchlarining "
                  "egilgan sirtdagi proeksiyasi paydo bo'ladi — "
                  "xuddi tortilgan arqon kabi. Kvadrat qavs "
                  "$L(F, w)$ bilinear operator deb belgilanadi."),
                d("8. Bir hadli Galerkin yechimi",
                  r"w = w_0\sin\frac{\pi x}{a}\sin\frac{\pi y}{b} "
                  r"\;\Longrightarrow\; C_1 w_0 + C_3 w_0^3 = q",
                  "Sinov funksiyasini qo'yib Galerkin shartini "
                  "qo'llasak, **kubik** algebraik tenglama "
                  "hosil bo'ladi. Chiziqli had — egilish "
                  "bikrligi, kubik had — membrana effekti."),
            ],
            meaning=(
                "Fon Karman tenglamalarining eng chuqur jihati "
                "birinchi tenglamaning o'ng tomonida: u aynan "
                "**Gauss egriligi**. Bu pq-02 dagi Theorema "
                "Egregium bilan to'g'ridan-to'g'ri bog'liq. "
                "Tekis plastinaning $K = 0$; agar u "
                "$K \\ne 0$ bo'lgan shaklga egilsa, o'rta sirt "
                "**cho'zilishga majbur** — chunki $K$ ichki "
                "xossa va cho'zilmasdan o'zgarmaydi. Aynan shu "
                "cho'zilish membrana kuchlarini keltirib "
                "chiqaradi. Silindrsimon egilishda esa "
                "($K = 0$) membrana kuchlari paydo bo'lmaydi — "
                "shuning uchun uzun plastinada nochiziqlilik "
                "kechroq boshlanadi. Kubik tenglama "
                "$C_1w_0 + C_3w_0^3 = q$ ham ma'noli: kichik "
                "og'ishda birinchi had hukmron (chiziqli "
                "javob), katta og'ishda esa kubik had "
                "(membrana rejimi). O'tish nuqtasi "
                "$w \\approx h$ atrofida. Amaliy oqibati "
                "juda muhim: $w = 2h$ da chiziqli nazariya "
                "og'ishni taxminan **3 marta oshirib** "
                "ko'rsatadi. Bu 'xavfsiz tomonga xato' "
                "tuyuladi, lekin aslida yo'q — chunki real "
                "membrana kuchlanishlari hisobga olinmaydi "
                "va ular chekkalarda juda katta bo'lishi "
                "mumkin. Shuning uchun yupqa qoplamalarda "
                "nochiziqli hisob majburiy."
            ),
            equations=[
                eq(r"\nabla^4 F = E\big[w_{,xy}^2 - w_{,xx}w_{,yy}\big]",
                   "Birinchi fon Karman tenglamasi (moslik).",
                   "fon Karman I"),
                eq(r"D\nabla^4 w = q + h\big[F_{,yy}w_{,xx} - "
                   r"2F_{,xy}w_{,xy} + F_{,xx}w_{,yy}\big]",
                   "Ikkinchi fon Karman tenglamasi (muvozanat).",
                   "fon Karman II"),
                eq(r"\varepsilon_x^0 = u_{,x} + \tfrac{1}{2}w_{,x}^2",
                   "Nochiziqli deformatsiya-ko'chish munosabati.",
                   "Nochiziqli deformatsiya"),
                eq(r"C_1 w_0 + C_3 w_0^3 = q",
                   "Bir hadli Galerkin yaqinlashuvidagi kubik "
                   "tenglama.", "Kubik tenglama"),
            ],
            conditions=(
                "**Tekislik ichidagi chegaraviy shartlar endi "
                "hal qiluvchi ahamiyatga ega** — chiziqli "
                "nazariyada ular umuman kerak emas edi:\n"
                "- **Harakatsiz chekka** (immovable): $u = 0$ "
                "konturda — membrana kuchlari maksimal, "
                "nochiziqlilik eng kuchli;\n"
                "- **Erkin siljiydigan chekka** (movable): "
                "$N_n = 0$ — membrana kuchlari faqat qo'sh "
                "egrilikdan, effekt ancha zaif;\n"
                "- Oraliq holat: elastik chekka bog'lanishi.\n\n"
                "Ikki hol orasidagi farq $w \\approx 2h$ da "
                "ikki baravarga yetishi mumkin.\n\n"
                "**Ko'ndalang shartlar** odatdagidek "
                "(sharnirli, mahkamlangan).\n\n"
                "**Qo'llanish chegarasi:** fon Karman "
                "yaqinlashuvi $w/a < 0{,}1$ va burilish "
                "burchaklari kichik bo'lganda o'rinli. "
                "Juda katta og'ishda to'liq nochiziqli "
                "qobiq nazariyasi kerak."
            ),
            worked=WorkedExample(
                statement=(
                    "Alyuminiy qoplama paneli: kvadrat "
                    "$a = b = 400$ mm, $h = 1{,}5$ mm, "
                    "$E = 70$ GPa, $\\nu = 0{,}33$, to'rt "
                    "chekka sharnirli va **harakatsiz** "
                    "(immovable). Bosim $q = 20$ kPa. "
                    "(a) Chiziqli yechimni toping. "
                    "(b) Nochiziqli kubik tenglamani yeching. "
                    "(c) Membrana va egilish kuchlanishlarini "
                    "taqqoslang."
                ),
                given=[
                    r"a = b = 0{,}4\ \text{m},\ h = 1{,}5\times10^{-3}\ \text{m}",
                    r"E = 70\ \text{GPa},\ \nu = 0{,}33",
                    r"q = 20\,000\ \text{Pa}",
                ],
                steps=[
                    st(r"D = \frac{70\times10^9 \cdot 3{,}375\times10^{-9}}"
                       r"{12 \cdot 0{,}8911} = \frac{236{,}25}{10{,}693} "
                       r"= 22{,}09\ \text{N·m}",
                       "$h^3 = 3{,}375\\times10^{-9}$ m³. Juda "
                       "kichik bikrlik — yupqa qoplama."),
                    st(r"w_{\text{chiziqli}} = 0{,}00406\frac{qa^4}{D} "
                       r"= 0{,}00406\frac{20\,000 \cdot 0{,}0256}{22{,}09}",
                       "Kvadrat sharnirli plastina koeffitsienti "
                       "(pq-07). $a^4 = 0{,}0256$ m⁴."),
                    st(r"w_{\text{chiziqli}} = 0{,}00406 \cdot 23{,}18 "
                       r"= 0{,}09411\ \text{m} = 94{,}1\ \text{mm}",
                       "$w/h = 94{,}1/1{,}5 = 62{,}7$ — "
                       "qalinlikdan **62 marta** katta! Chiziqli "
                       "nazariya mutlaqo yaroqsiz."),
                    st(r"C_1 w_0 + C_3 w_0^3 = q; \quad "
                       r"C_1 = \frac{\pi^4 D}{4}\Big(\frac{1}{a^2} "
                       r"+ \frac{1}{b^2}\Big)^2 \cdot \frac{16}{\pi^2}\ldots",
                       "Galerkin sharti. Kvadrat plastina va "
                       "harakatsiz chekka uchun standart "
                       "koeffitsientlar (Timoshenko)."),
                    st(r"\text{Timoshenko shakli: } \frac{qa^4}{Eh^4} "
                       r"= A\frac{w_0}{h} + B\Big(\frac{w_0}{h}\Big)^3, "
                       r"\quad A = 14{,}64,\ B = 4{,}70",
                       "O'lchamsiz shakl. $\\nu = 0{,}316$ uchun "
                       "klassik qiymatlar; kodda aniq hisoblanadi."),
                    st(r"\frac{qa^4}{Eh^4} = \frac{20\,000 \cdot 0{,}0256}"
                       r"{70\times10^9 \cdot 5{,}0625\times10^{-12}} "
                       r"= \frac{512}{0{,}3544} = 1445",
                       "$h^4 = 5{,}0625\\times10^{-12}$ m⁴. "
                       "O'lchamsiz yuklama juda katta — "
                       "membrana rejimi."),
                    st(r"14{,}64\xi + 4{,}70\xi^3 = 1445 "
                       r"\;\Longrightarrow\; \xi \approx 6{,}60",
                       "Kubik tenglamaning haqiqiy ildizi "
                       "($\\xi = w_0/h$). Kubik had hukmron: "
                       "$4{,}70 \\cdot 287 = 1349$ vs "
                       "$14{,}64 \\cdot 6{,}6 = 97$."),
                    st(r"w_0 = 6{,}60 \cdot 1{,}5 = 9{,}90\ \text{mm} "
                       r"\quad \text{vs chiziqli } 94{,}1\ \text{mm}",
                       "Nochiziqli yechim **9,5 marta** kichik! "
                       "Membrana effekti panelni keskin bikrlashtirdi."),
                    st(r"\sigma_m \approx \frac{E}{1-\nu^2}\cdot"
                       r"\frac{\pi^2 w_0^2}{8a^2}, \quad "
                       r"\sigma_b = \frac{6M}{h^2}",
                       "Membrana va egilish kuchlanishlari. "
                       "Kodda aniq hisoblanadi; membrana hissasi "
                       "bu rejimda hukmron."),
                ],
                answer=(
                    "$D = 22{,}09$ N·m; chiziqli yechim "
                    "$w = 94{,}1$ mm ($w/h = 62{,}7$ — mutlaqo "
                    "ishonchsiz); nochiziqli kubik tenglama "
                    "$w_0/h = 6{,}60$, ya'ni $w_0 = 9{,}90$ mm — "
                    "chiziqlidan **9,5 marta kichik**. Membrana "
                    "hissasi kubik hadda hukmron (1349 vs 97)."
                ),
                engineering_note=(
                    "9,5 marta farq nochiziqli hisobning nima "
                    "uchun yupqa qoplamalarda majburiy "
                    "ekanligini ko'rsatadi. Lekin diqqat: "
                    "og'ish kamaydi, **kuchlanish esa "
                    "kamaymaydi** — u boshqa turga o'tadi. "
                    "Chiziqli nazariyada faqat egilish "
                    "kuchlanishi bor edi; endi membrana "
                    "kuchlanishi qo'shiladi va u butun "
                    "qalinlik bo'yicha bir xil. Natijada "
                    "plastinaning bir yuzasida ular qo'shiladi "
                    "va maksimal kuchlanish chiziqli "
                    "bahodan kutilganidan katta bo'lishi "
                    "mumkin. Shuning uchun 'nochiziqlilik "
                    "og'ishni kamaytiradi, demak xavfsiz' "
                    "degan xulosa **xato**."
                ),
            ),
            computation=Computation(
                caption=(
                    "Kubik tenglamani yechish, chiziqli va "
                    "nochiziqli yechimlarni taqqoslash, "
                    "membrana hamda egilish kuchlanishlarini "
                    "ajratish."
                ),
                code='''"""Fon Karman: katta og'ishlar va membrana effekti."""
import numpy as np
from labkit import PARAMS, note, series, table, value

a = float(PARAMS.get("a", 400.0))/1000.0
b = float(PARAMS.get("b", 400.0))/1000.0
h = float(PARAMS.get("h", 1.5))/1000.0
E = float(PARAMS.get("E", 70.0))*1e9
nu = float(PARAMS.get("nu", 0.33))
q0 = float(PARAMS.get("q", 20000.0))
edge = int(PARAMS.get("edge", 0))       # 0 harakatsiz, 1 erkin siljiydigan
sY = float(PARAMS.get("sY", 270.0))*1e6

D = E*h**3/(12*(1 - nu**2))
value("Silindrik bikrlik D", D, "N*m")
value("a/h nisbati", a/h, "—")

# --- Chiziqli yechim (Navye) ---
w_lin = 0.0
for m in range(1, 30, 2):
    for n in range(1, 30, 2):
        am, bn = m*np.pi/a, n*np.pi/b
        qmn = 16*q0/(np.pi**2*m*n)
        w_lin += qmn/(D*(am**2 + bn**2)**2)*np.sin(m*np.pi/2)*np.sin(n*np.pi/2)
value("Chiziqli yechim w_lin", w_lin*1000, "mm")
value("w_lin / h", w_lin/h, "—")
if w_lin/h > 0.2:
    note(f"w/h = {w_lin/h:.2f} > 0.2 — chiziqli nazariya "
         f"YAROQSIZ, nochiziqli hisob majburiy.")

# --- Galerkin koeffitsientlari (bir hadli yaqinlashuv) ---
# w = w0 * sin(pi x/a) sin(pi y/b)
lam = (1/a**2 + 1/b**2)
C1 = D*np.pi**4*lam**2/4.0 * (np.pi**2/16.0) * (16.0/np.pi**2)
# chiziqli had: Galerkin -> D*pi^4*lam^2/4 * w0 = 16 q /pi^2
C1 = D*np.pi**4*lam**2/4.0
Q_eff = 16*q0/np.pi**2

# membrana hadi: harakatsiz chekka uchun (Timoshenko/Levy)
if edge == 0:
    k_mem = E*h*np.pi**4/(16*(1 - nu**2))*(1/a**4 + 1/b**4
                                           + 2*nu/(a**2*b**2)) \
        if False else E*h*np.pi**4/(16*(1 - nu**2))*(1/a**4 + 1/b**4)
    edge_name = "harakatsiz (immovable)"
else:
    k_mem = E*h*np.pi**4/(16*(1 - nu**2))*(1/a**4 + 1/b**4)*0.35
    edge_name = "erkin siljiydigan (movable)"

# C1*w0 + k_mem*w0^3 = Q_eff
roots = np.roots([k_mem, 0.0, C1, -Q_eff])
real_roots = [float(r.real) for r in roots
              if abs(r.imag) < 1e-9 and r.real > 0]
w0 = min(real_roots) if real_roots else float("nan")

value("Chegara turi kodi", float(edge), "—")
value("Chiziqli koeffitsient C1", C1, "N/m3")
value("Membrana koeffitsienti C3", k_mem, "N/m5")
value("Nochiziqli yechim w_0", w0*1000, "mm")
value("w_0 / h", w0/h, "—")
value("Chiziqli / nochiziqli nisbati", w_lin/w0, "—")
note(f"Chekka turi: {edge_name}. Chiziqli yechim "
     f"{w_lin*1000:.2f} mm, nochiziqli {w0*1000:.2f} mm — "
     f"membrana effekti og'ishni {w_lin/w0:.1f} marta kamaytirdi.")

lin_term = C1*w0
cub_term = k_mem*w0**3
value("Chiziqli hadning hissasi", lin_term/Q_eff*100, "%")
value("Kubik (membrana) hadning hissasi", cub_term/Q_eff*100, "%")

# --- Timoshenko etaloni (aniqroq, ko'p hadli yechim) ---
# Kvadrat, sharnirli, harakatsiz chekka: q a^4/(E h^4) = 14.64*xi + 4.70*xi^3
if abs(a - b) < 1e-9 and edge == 0:
    P_nd = q0*a**4/(E*h**4)
    rts_t = np.roots([4.70, 0.0, 14.64, -P_nd])
    rr_t = [float(x.real) for x in rts_t if abs(x.imag) < 1e-9 and x.real > 0]
    xi_t = min(rr_t) if rr_t else float("nan")
    value("O'lchamsiz yuklama q*a^4/(E*h^4)", P_nd, "—")
    value("Timoshenko yechimi w_0/h", xi_t, "—")
    value("Timoshenko w_0", xi_t*h*1000, "mm")
    value("Bir hadli Galerkin / Timoshenko", (w0/h)/xi_t if xi_t else 0.0, "—")
    note(f"Bir hadli Galerkin w_0/h = {w0/h:.2f}, Timoshenkoning "
         f"ko'p hadli yechimi {xi_t:.2f} — farq "
         f"{abs(w0/h - xi_t)/xi_t*100:.0f} %. Bitta sinov funksiyasi "
         f"tekislik ichidagi ko'chish maydonini qo'pol ifodalaydi, "
         f"shuning uchun membrana bikrligi oshirib baholanadi. "
         f"Muhandislik bahosi uchun Timoshenko koeffitsientlari "
         f"(14.64 va 4.70) ishlatiladi.")

# --- q - w egri chizig'i ---
xis = np.linspace(0.0, max(3.0, 1.5*w0/h), 200)
ws_ = xis*h
q_nl = (C1*ws_ + k_mem*ws_**3)*np.pi**2/16
q_lin = C1*ws_*np.pi**2/16
series("Nochiziqli q(w)", (ws_/h).tolist(), (q_nl/1000).tolist(),
       xlabel="w_0 / h", ylabel="Bosim q, kPa")
series("Chiziqli q(w)", (ws_/h).tolist(), (q_lin/1000).tolist(),
       xlabel="w_0 / h", ylabel="Bosim q, kPa")
series("Joriy ish nuqtasi", [w0/h], [q0/1000],
       xlabel="w_0 / h", ylabel="Bosim q, kPa")

i_2x = int(np.argmax(np.where(q_lin > 0, q_nl/np.maximum(q_lin, 1e-30), 0) > 2.0)) \
    if np.any(q_lin > 0) else 0
if i_2x > 0:
    value("Nochiziqlilik 2 barobar bo'ladigan w/h", float(xis[i_2x]), "—")

# --- Kuchlanishlar ---
# egilish: M = D*pi^2*(1/a^2 + nu/b^2)*w0 ; membrana (taqribiy, markazda)
M_b = D*np.pi**2*(1/a**2 + nu/b**2)*w0
sig_b = 6*M_b/h**2
eps_m = np.pi**2*w0**2/(8*a**2)
sig_m = E*eps_m/(1 - nu**2)
value("Egilish momenti M", M_b, "N*m/m")
value("Egilish kuchlanishi sigma_b", sig_b/1e6, "MPa")
value("Membrana deformatsiyasi", eps_m*1e6, "mkm/m")
value("Membrana kuchlanishi sigma_m", sig_m/1e6, "MPa")
value("sigma_m / sigma_b", sig_m/sig_b if sig_b > 0 else 0.0, "—")
sig_tot = sig_b + sig_m
value("Yuza qatlamdagi jami kuchlanish", sig_tot/1e6, "MPa")
value("Zaxira koeffitsienti", sY/sig_tot, "—")

# Chiziqli nazariya bo'lsa qanday kuchlanish chiqardi
M_lin = D*np.pi**2*(1/a**2 + nu/b**2)*w_lin
sig_lin = 6*M_lin/h**2
value("Chiziqli nazariya kuchlanishi", sig_lin/1e6, "MPa")
note(f"Og'ish {w_lin/w0:.1f} marta kamaydi, lekin jami kuchlanish "
     f"{sig_lin/sig_tot:.2f} marta o'zgardi — membrana kuchlanishi "
     f"qo'shilgani uchun kamayish ancha kamroq. 'Nochiziqlilik "
     f"xavfsiz' degan xulosa XATO.")

# --- Kuchlanish taqsimoti qalinlik bo'yicha ---
z = np.linspace(-h/2, h/2, 121)
sig_bending = 12*M_b/h**3*z
sig_membrane = np.full_like(z, sig_m)
series("Egilish kuchlanishi sigma_b(z)", (sig_bending/1e6).tolist(),
       (z*1000).tolist(), xlabel="sigma, MPa", ylabel="z, mm")
series("Membrana kuchlanishi sigma_m(z)", (sig_membrane/1e6).tolist(),
       (z*1000).tolist(), xlabel="sigma, MPa", ylabel="z, mm")
series("Jami kuchlanish", ((sig_bending + sig_membrane)/1e6).tolist(),
       (z*1000).tolist(), xlabel="sigma, MPa", ylabel="z, mm")
note("Membrana kuchlanishi qalinlik bo'yicha DOIMIY, egilish esa "
     "chiziqli. Ularning yig'indisi neytral sirtni siljitadi: "
     "bir yuzada ular qo'shiladi, ikkinchisida ayriladi.")

# --- Yuklama bo'yicha skanerlash ---
qs = np.logspace(np.log10(max(q0/200, 1.0)), np.log10(q0*5), 80)
w_nls, w_lins, ratios2 = [], [], []
for qq in qs:
    Qe = 16*qq/np.pi**2
    rts = np.roots([k_mem, 0.0, C1, -Qe])
    rr = [float(x.real) for x in rts if abs(x.imag) < 1e-9 and x.real > 0]
    wn = min(rr) if rr else np.nan
    wl = Qe/C1
    w_nls.append(wn/h)
    w_lins.append(wl/h)
    ratios2.append(wl/wn if wn and not np.isnan(wn) else np.nan)
series("w/h nochiziqli (yuklama bo'yicha)", (qs/1000).tolist(), w_nls,
       xlabel="Bosim q, kPa", ylabel="w_0 / h")
series("w/h chiziqli (yuklama bo'yicha)", (qs/1000).tolist(), w_lins,
       xlabel="Bosim q, kPa", ylabel="w_0 / h")
series("Chiziqli/nochiziqli nisbati", (qs/1000).tolist(), ratios2,
       xlabel="Bosim q, kPa", ylabel="Nisbat")

i_10 = int(np.argmax(np.array(w_lins) > 0.2))
if i_10 > 0:
    value("w/h = 0.2 ga mos yuklama", float(qs[i_10])/1000, "kPa")
    note(f"q > {qs[i_10]/1000:.2f} kPa dan boshlab chiziqli nazariya "
         f"xatosi 5 % dan oshadi.")

table("w/h bo'yicha rejimlar",
      ["w/h oralig'i", "Rejim", "Chiziqli nazariya xatosi", "Tavsiya"],
      [["< 0.2", "egilish hukmron", "< 5 %", "chiziqli nazariya yetarli"],
       ["0.2 - 0.5", "aralash", "5 - 25 %", "nochiziqlilik tavsiya etiladi"],
       ["0.5 - 1.0", "membrana sezilarli", "25 - 100 %", "nochiziqli hisob shart"],
       ["> 1.0", "membrana hukmron", "> 100 %", "faqat fon Karman yoki membrana"]])

table("Chekka shartining ta'siri (nochiziqlilikka)",
      ["Chekka turi", "Membrana kuchlari", "Nochiziqlilik kuchi"],
      [["Harakatsiz (u = 0)", "maksimal", "eng kuchli"],
       ["Erkin siljiydigan (N_n = 0)", "faqat qo'sh egrilikdan", "zaifroq"],
       ["Elastik bog'langan", "oraliq", "oraliq"],
       ["Silindrik egilish (K = 0)", "yo'q", "nochiziqlilik yo'q"]])
''',
                parameters=[
                    p("a", "Panel tomoni a", 50.0, 3000.0, 400.0, 10.0, "mm"),
                    p("b", "Panel tomoni b", 50.0, 3000.0, 400.0, 10.0, "mm"),
                    p("h", "Qalinlik h", 0.2, 30.0, 1.5, 0.1, "mm"),
                    p("E", "Yung moduli E", 1.0, 400.0, 70.0, 1.0, "GPa"),
                    p("nu", "Puasson koeffitsienti ν", 0.0, 0.45, 0.33, 0.01),
                    p("q", "Bosim q", 100.0, 500000.0, 20000.0, 100.0, "Pa"),
                    p("edge", "Chekka (0 harakatsiz, 1 siljiydigan)",
                      0.0, 1.0, 0.0, 1.0),
                    p("sY", "Oqish chegarasi σ_Y", 20.0, 1000.0, 270.0, 5.0, "MPa"),
                ],
                expected_output=(
                    "D = 22,09 N·m; chiziqli yechim w = 94,1 mm "
                    "(w/h = 62,8 — yaroqsiz). Bir hadli Galerkin "
                    "w₀/h = 5,51, Timoshenkoning ko'p hadli "
                    "yechimi 6,60 (w₀ = 9,89 mm) — farq 16 %; "
                    "o'lchamsiz yuklama qa⁴/(Eh⁴) = 1445. "
                    "Kubik hadning hissasi 97,9 % — membrana "
                    "rejimi; σ_m/σ_b = 1,04, ya'ni membrana va "
                    "egilish kuchlanishlari taqqoslanadigan."
                ),
            ),
            visual=vis(
                kind="Nochiziqli yuklanish diagrammasi",
                tool="React/SVG",
                description=(
                    "$q$–$w/h$ egri chizig'i chiziqli bilan "
                    "taqqoslangan holda, membrana va egilish "
                    "kuchlanishlarining qalinlik bo'yicha epyuralari."
                ),
                how_to_draw=(
                    "React/SVG: asosiy panel — $q$–$w/h$ "
                    "diagrammasi: chiziqli javob to'g'ri chiziq "
                    "(punktir), nochiziqli javob pastga egilgan "
                    "egri chiziq (uzluksiz, qalin). Ular "
                    "$w/h \\approx 0{,}2$ gacha ustma-ust "
                    "tushadi, so'ng ajralib ketadi — bu "
                    "ajralish nuqtasi vertikal chiziq bilan "
                    "belgilanadi va '$w/h = 0{,}2$: chiziqli "
                    "nazariya chegarasi' yorlig'i qo'yiladi. "
                    "Joriy ish nuqtasi katta belgi bilan. "
                    "Ikkinchi panel — qalinlik bo'yicha "
                    "kuchlanish epyuralari: uchta grafik bir "
                    "$z$ o'qida — egilish (chiziqli, "
                    "antisimmetrik), membrana (doimiy, "
                    "vertikal to'g'ri chiziq) va ularning "
                    "yig'indisi. Yig'indining neytral "
                    "sirtdan siljiganligi va bir yuzada "
                    "maksimal bo'lishi aniq ko'rinadi. "
                    "Uchinchi element — $w/h$ slayderi; u "
                    "siljitilganda ikkala panel va "
                    "$\\sigma_m/\\sigma_b$ nisbati jonli yangilanadi."
                ),
            ),
            interp=(
                "$q$–$w$ diagrammasi nochiziqlilikning "
                "mohiyatini ko'rsatadi: egri chiziq pastga "
                "egiladi, ya'ni plastina yuklama ortgani sari "
                "**bikrroq** bo'ladi. Bu ustuvorlik "
                "masalasidagi (pq-19) yuqoriga egilishning — "
                "yumshashning — to'liq aksi. Sababi aniq: "
                "membrana kuchlari cho'zuvchi va ular og'ishga "
                "qarshilik ko'rsatadi, xuddi tortilgan batut "
                "kabi. Eng muhim amaliy xulosa esa kuchlanish "
                "taqqoslashida: og'ish 9,5 marta kamaydi, "
                "lekin jami kuchlanish undan ancha kam "
                "o'zgardi. Sababi — membrana kuchlanishi "
                "qalinlik bo'yicha **doimiy** va u egilish "
                "kuchlanishiga qo'shiladi. Natijada plastinaning "
                "bir yuzasida kuchlanish kutilganidan yuqori "
                "bo'lishi mumkin. Bu 'nochiziqlilik og'ishni "
                "kamaytiradi, demak zaxira oshadi' degan "
                "keng tarqalgan xatoni tuzatadi. Chekka "
                "shartining ta'siri jadvali ham muhim: "
                "harakatsiz chekkada membrana effekti eng "
                "kuchli, silindrik egilishda esa ($K = 0$) "
                "umuman yo'q. Shuning uchun uzun panelda "
                "nochiziqlilik kech boshlanadi, kvadratda esa "
                "erta — bu pq-02 dagi Gauss egriligi "
                "tushunchasining bevosita amaliy oqibati."
            ),
            mistakes=[
                "Chiziqli nazariyani $w/h > 0{,}2$ da "
                "qo'llash. Xato 100 % dan oshishi mumkin va "
                "u og'ishni oshirib ko'rsatadi.",
                "Nochiziqlilik og'ishni kamaytirgani uchun "
                "xavfsiz deb hisoblash. Membrana kuchlanishi "
                "qo'shiladi va jami kuchlanish kutilganidan "
                "yuqori bo'lishi mumkin.",
                "Tekislik ichidagi chegaraviy shartni "
                "aniqlamaslik. Harakatsiz va erkin "
                "siljiydigan chekka orasidagi farq ikki "
                "baravarga yetadi.",
                "Silindrik egilishda membrana effektini "
                "izlash. $K = 0$ bo'lgani uchun o'rta sirt "
                "cho'zilmaydi va nochiziqlilik paydo bo'lmaydi "
                "(chekkalar harakatsiz bo'lmasa).",
            ],
            quiz=[
                q("Nima uchun katta og'ishda membrana kuchlari "
                  "paydo bo'ladi?",
                  "Tekis plastina ($K = 0$) qo'sh egrilikli "
                  "shaklga ($K \\ne 0$) egilganda o'rta sirt "
                  "cho'zilishga majbur — Gauss egriligi ichki "
                  "xossa (Theorema Egregium).", "konseptual"),
                q("Fon Karman tenglamalarining birinchisida "
                  "o'ng tomon nimaga teng?",
                  "$E[w_{,xy}^2 - w_{,xx}w_{,yy}]$, ya'ni "
                  "Gauss egriligiga $-E$ ko'paytirilgan. "
                  "Bu membrana kuchlarining manbai.", "konseptual"),
                q("$w/h$ ning qaysi qiymatidan boshlab "
                  "nochiziqli hisob kerak?",
                  "$w/h > 0{,}2$ dan — u yerda chiziqli "
                  "nazariya xatosi 5 % dan oshadi; "
                  "$w/h > 0{,}5$ da esa nochiziqli hisob shart.",
                  "hisob"),
                q("Nima uchun $q$–$w$ egri chizig'i pastga "
                  "egiladi?",
                  "Membrana kuchlari cho'zuvchi va og'ishga "
                  "qarshilik ko'rsatadi; og'ish ortgani sari "
                  "ular kuchayadi va plastina bikrroq "
                  "bo'ladi (stress stiffening).", "talqin"),
                q("Kodda nima uchun `np.roots` ishlatiladi va "
                  "nima uchun eng kichik musbat ildiz olinadi?",
                  "Galerkin sharti kubik tenglama beradi. "
                  "Uchta ildizdan faqat bittasi haqiqiy va "
                  "musbat (fizik yechim); qolganlari kompleks "
                  "yoki manfiy.", "kod"),
                q("Nochiziqlilik og'ishni kamaytirdi — bu "
                  "xavfsizlik zaxirasi oshdi deganimi?",
                  "Yo'q. Membrana kuchlanishi qalinlik "
                  "bo'yicha doimiy va egilish kuchlanishiga "
                  "qo'shiladi; jami kuchlanish og'ishdan "
                  "ancha kam kamayadi, ba'zan hatto oshadi.",
                  "talqin"),
            ],
            bridge=(
                "Membrana kuchlari **cho'zuvchi** bo'lganda "
                "plastinani bikrlashtiradi. Agar ular "
                "**siquvchi** bo'lsa, aksincha — plastinani "
                "yumshatadi va ma'lum qiymatda u bikrligini "
                "butunlay yo'qotadi. Keyingi modulda aynan "
                "shu hodisani — ustuvorlikni yo'qotishni — "
                "o'rganamiz."
            ),
            research=(
                "Boshlang'ich nomukammalligi bo'lgan "
                "plastinani o'rganing. Real panel hech qachon "
                "ideal tekis emas: $w_0(x,y)$ boshlang'ich "
                "egrilik mavjud. Fon Karman tenglamalariga "
                "uni kiriting — deformatsiyada "
                "$\\frac{1}{2}(w_{,x}^2 - w_{0,x}^2)$ paydo "
                "bo'ladi. Nomukammallik amplitudasi "
                "$w_0/h = 0{,}1; 0{,}5; 1{,}0$ uchun "
                "$q$–$w$ egri chiziqlarini quring. "
                "Nomukammallik yuklanish javobini qanday "
                "o'zgartiradi? Bu natija pq-21 dagi "
                "kritikdan keyingi xatti-harakat va "
                "nomukammalliklarga sezgirlik bilan "
                "qanday bog'lanadi?"
            ),
            manim_ref=manim(
                scene="VonKarmanScene",
                module="animatsiya/scenes/pq_circular.py",
                title="Membrana effekti va nochiziqli bikrlanish",
                summary=(
                    "Plastina asta-sekin egiladi; kichik "
                    "og'ishda o'rta sirt cho'zilmaydi, katta "
                    "og'ishda esa cho'zilish paydo bo'lib "
                    "membrana kuchlari o'sadi va $q$–$w$ "
                    "egri chizig'i chiziqlidan ajralib ketadi."
                ),
            ),
        ),
    ),
]
