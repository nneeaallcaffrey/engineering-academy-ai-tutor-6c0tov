"""PQ / 5-modul: Qobiqlar nazariyasi (pq-25 … pq-30)."""

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
M = "pq-m5"


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
    # ------------------------------------------------------------------ pq-25
    Topic(
        id="pq-25",
        subject_id=S, module_id=M, order=25,
        title="Qobiq geometriyasi: asosiy sirt, egrilik radiuslari va Gauss egriligi",
        description=(
            "Aylanma sirtlar, bosh egrilik radiuslari $R_1$ va $R_2$, "
            "Gauss egriligi bo'yicha tasniflash, Lame parametrlari va "
            "qobiqning plastinadan tub farqi."
        ),
        learning_objective=(
            "Aylanma qobiq geometriyasini parametrlash, bosh egrilik "
            "radiuslarini hisoblash, sirtni Gauss egriligi bo'yicha "
            "tasniflash va yoyiluvchanlikni aniqlash."
        ),
        prerequisites=["pq-02", "pq-24"],
        mathematical_core=(
            "$K = 1/(R_1R_2)$, birinchi kvadratik forma "
            "$ds^2 = A^2d\\alpha^2 + B^2d\\beta^2$, "
            "Kodatstsi–Gauss munosabatlari, Theorema Egregium."
        ),
        engineering_application=(
            "Rezervuar va silos gumbazlari, bosim ostidagi idishlar, "
            "aviatsiya fyuzelyaji, sovutish minoralari, kemasozlik."
        ),
        computational_component=(
            "Aylanma sirt uchun $R_1$, $R_2$ va $K$ ni sonli hisoblash, "
            "yoyiluvchanlikni tekshirish, egrilik xaritasini qurish."
        ),
        visualization_component=(
            "Silindr, sfera, konus, giperboloid va torning egrilik "
            "xaritasi; Gauss egriligi ishorasi bo'yicha bo'yash."
        ),
        research_extension=(
            "Gauss egriligi va qobiq bikrligi orasidagi bog'liqlikni "
            "o'rganing: nima uchun tuxum po'sti ingichka bo'lsa ham "
            "bikr, gofrlangan varaq esa yoyiluvchan? Nolinchi Gauss "
            "egrilikli sirtlarning texnologik afzalliklarini baholang."
        ),
        difficulty="asosiy",
        previous_link=(
            "pq-02 da tekis plastinaning egrilik tenzori kiritilgan va "
            "Gauss egriligi $K = \\kappa_1\\kappa_2$ ta'riflangan edi. "
            "U yerda $K$ deformatsiya natijasi edi; endi $K$ — "
            "konstruksiyaning **boshlang'ich** xossasi."
        ),
        next_topic="pq-26",
        estimated_minutes=85,
        tags=["qobiq", "Gauss egriligi", "aylanma sirt", "geometriya"],
        lesson=_lesson(
            problem=(
                "Bir xil po'lat varaqdan ikkita qopqoq yasaymiz: "
                "birinchisi tekis, ikkinchisi sferik gumbaz. "
                "Ikkalasining qalinligi $h = 5$ mm, o'lchami 4 m, "
                "yuklamasi $q = 10$ kPa. Sferik gumbaz "
                "**0,013 mm** ga og'adi — ko'z bilan "
                "ilg'ab bo'lmaydi. Tekis qopqoq uchun esa "
                "chiziqli plastina nazariyasi (pq-04) "
                "**4,3 m** beradi, ya'ni javob qalinlikdan "
                "800 marta katta va nazariyaning o'zi "
                "yaroqsiz: bunday qopqoq plastina sifatida "
                "umuman ishlay olmaydi, u faqat cho'zilib, "
                "membranaga aylanib omon qoladi (pq-18). "
                "Ikkala konstruksiyada material, qalinlik va "
                "yuklama bir xil. Butun farq bitta narsada: "
                "**egrilikda**. Gumbaz aynan o'sha membrana "
                "kuchlarini og'ishsiz, faqat geometriyasi "
                "hisobiga beradi. Endi shu geometriyani aniq "
                "tilda ifodalash kerak."
            ),
            concepts=[
                c("Asosiy sirt (o'rta sirt)",
                  "Qobiq qalinligini teng ikkiga bo'luvchi sirt; "
                  "plastinadagi o'rta tekislikning umumlashmasi, "
                  "lekin endi u egri."),
                c("Bosh egrilik radiuslari $R_1, R_2$",
                  "Berilgan nuqtada normal kesimlarning eng katta "
                  "va eng kichik egrilik radiuslari; ular "
                  "o'zaro perpendikulyar tekisliklarda yotadi."),
                c("Gauss egriligi $K$",
                  "$K = \\kappa_1\\kappa_2 = 1/(R_1R_2)$ — sirtning "
                  "ichki (intrinsik) xossasi, cho'zmasdan egishda "
                  "o'zgarmaydi (Theorema Egregium, pq-02)."),
                c("O'rtacha egrilik $H$",
                  "$H = (\\kappa_1 + \\kappa_2)/2$ — tashqi xossa; "
                  "sirtni qanday egganimizga bog'liq."),
                c("Lame parametrlari $A, B$",
                  "Egri koordinatalarda uzunlik o'lchovi: "
                  "$ds^2 = A^2d\\alpha^2 + B^2d\\beta^2$; ular "
                  "differensial operatorlarga kiradi."),
                c("Yoyiluvchan (developable) sirt",
                  "$K = 0$ bo'lgan sirt; cho'zmasdan tekislikka "
                  "yoyish mumkin — silindr, konus. Shu sababli "
                  "ular arzon yasaladi."),
            ],
            derivation=[
                d("1. Aylanma sirtni parametrlash",
                  r"\mathbf{r}(\varphi,\theta) = \big(r(\varphi)\cos\theta,\ "
                  r"r(\varphi)\sin\theta,\ z(\varphi)\big)",
                  "$\\theta$ — aylana bo'ylab burchak, $\\varphi$ — "
                  "meridian bo'ylab parametr. Barcha texnik qobiqlar "
                  "(silindr, konus, sfera, tor) shu ko'rinishda."),
                d("2. Birinchi kvadratik forma",
                  r"ds^2 = (r'^2 + z'^2)\,d\varphi^2 + r^2\,d\theta^2 "
                  r"\;\Longrightarrow\; A = \sqrt{r'^2+z'^2},\ B = r",
                  "Lame parametrlari to'g'ridan-to'g'ri o'qiladi. "
                  "Meridian yoy uzunligi $s$ bo'lsa, $A = 1$ deb "
                  "olish qulay (tabiiy parametrlash)."),
                d("3. Meridian egrilik radiusi $R_1$",
                  r"\frac{1}{R_1} = \frac{r'z'' - z'r''}"
                  r"{(r'^2+z'^2)^{3/2}}",
                  "Bu meridian egri chizig'ining oddiy tekis "
                  "egriligi — qobiqni meridian tekisligida "
                  "kesganimizdagi egrilik."),
                d("4. Aylana egrilik radiusi $R_2$",
                  r"R_2 = \frac{r}{\sin\phi}, \quad "
                  r"\sin\phi = \frac{r'}{\sqrt{r'^2+z'^2}}"
                  r"\ \text{(o'q bilan burchak orqali)}",
                  "$R_2$ — normal bo'ylab o'lchanadi va **aylana "
                  "radiusiga teng emas**: u normalning aylanish "
                  "o'qigacha bo'lgan masofasi. Bu eng ko'p "
                  "uchraydigan chalkashlik manbai."),
                d("5. Gauss egriligi",
                  r"K = \frac{1}{R_1R_2}",
                  "Ishorasi bo'yicha tasnif: $K>0$ — elliptik "
                  "(sfera, gumbaz), $K=0$ — parabolik (silindr, "
                  "konus), $K<0$ — giperbolik (sovutish minorasi, "
                  "egar)."),
                d("6. Qobiqning plastinadan farqi",
                  r"\varepsilon_\theta = \frac{w}{R_2} + \ldots "
                  r"\ne 0 \ \text{hatto } u=v=0 \ \text{bo'lganda ham}",
                  "**Hal qiluvchi qadam.** Egri sirtda faqat "
                  "normal ko'chish $w$ ham cho'zilish "
                  "deformatsiyasi hosil qiladi. Tekis plastinada "
                  "bu mumkin emas edi ($\\varepsilon = 0$ "
                  "bo'lardi). Demak qobiq yuklamani "
                  "**membrana kuchlari** bilan ko'taradi."),
                d("7. Bikrlikdagi tub farq",
                  r"\text{plastina: } w \sim \frac{qa^4}{D} "
                  r"\sim \frac{qa^4}{Eh^3}; \qquad "
                  r"\text{qobiq: } w \sim \frac{qR^2}{Eh}",
                  "Plastinada $h^3$, qobiqda $h^1$. "
                  "$h/R = 1/400$ bo'lsa, nisbat "
                  "$(a/h)^2 \\sim 10^5$ tartibida — kirish "
                  "misolidagi 700 barobar farq shundan."),
                d("8. Kodatstsi–Gauss shartlari",
                  r"\frac{\partial}{\partial\alpha}\Big(\frac{B}{R_2}\Big) "
                  r"= \frac{1}{R_1}\frac{\partial B}{\partial\alpha}, "
                  r"\quad \ldots",
                  "Ixtiyoriy $R_1(\\alpha,\\beta)$, "
                  "$R_2(\\alpha,\\beta)$ juftligi haqiqiy sirt "
                  "bermaydi — ular muvofiqlik shartlarini "
                  "qanoatlantirishi kerak."),
            ],
            meaning=(
                "Qobiq nazariyasining butun mohiyati 6-qadamda: "
                "**egri sirtda normal ko'chish cho'zilish "
                "deformatsiyasini tug'diradi**. Tekis plastinada "
                "$w$ faqat egilishni beradi va yuklama egish "
                "momentlari orqali ko'tariladi — bu esa "
                "qalinlikning kubiga bog'liq va yupqa "
                "konstruksiyada juda zaif. Egri sirtda esa $w$ "
                "darhol $\\varepsilon_\\theta = w/R_2$ beradi va "
                "yuklama qalinlikka **chiziqli** bog'liq membrana "
                "kuchlari bilan ko'tariladi. Shuning uchun tuxum "
                "po'sti 0,3 mm bo'lsa ham barmoq bosimiga "
                "chidaydi, xuddi shu qalinlikdagi tekis parcha esa "
                "yo'q. Gauss egriligi bu manzarani "
                "to'ldiradi. $K \\ne 0$ bo'lgan sirtni cho'zmasdan "
                "tekislikka yoyib bo'lmaydi (Theorema Egregium) — "
                "demak uni ezish uchun material cho'zilishi kerak, "
                "bu esa juda qimmat. Shuning uchun $K > 0$ "
                "gumbazlar eng bikr konstruksiyalardir. Aksincha, "
                "$K = 0$ sirtlar (silindr, konus) yoyiluvchan: "
                "ularni tekis varaqdan bukish bilan yasash mumkin "
                "— texnologik jihatdan arzon, lekin ular "
                "**inextensional** (cho'zilishsiz) deformatsiya "
                "rejimiga ega va shu sababli ustuvorlik "
                "yo'qotishga moyil (pq-29). $K < 0$ sirtlar "
                "esa ikki yo'nalishda qarama-qarshi egilgan va "
                "ikki oilali to'g'ri chiziqlardan qurilishi mumkin "
                "— sovutish minoralari aynan shu sababli "
                "giperboloid shaklida quriladi: to'g'ri armatura "
                "sterjenlaridan egri sirt hosil bo'ladi."
            ),
            equations=[
                eq(r"ds^2 = A^2\,d\alpha^2 + B^2\,d\beta^2",
                   "Sirtning birinchi kvadratik formasi; "
                   "$A$, $B$ — Lame parametrlari.",
                   "Birinchi kvadratik forma"),
                eq(r"K = \kappa_1\kappa_2 = \frac{1}{R_1R_2}, \qquad "
                   r"H = \frac{1}{2}\Big(\frac{1}{R_1}+\frac{1}{R_2}\Big)",
                   "Gauss va o'rtacha egriliklar.",
                   "Egrilik o'lchovlari"),
                eq(r"\varepsilon_\theta \supset \frac{w}{R_2}, \qquad "
                   r"\varepsilon_\varphi \supset \frac{w}{R_1}",
                   "Normal ko'chishning cho'zilish "
                   "deformatsiyasiga qo'shgan hissasi — qobiqning "
                   "plastinadan asosiy farqi.",
                   "Egrilik–cho'zilish bog'lanishi"),
                eq(r"R_2 = \frac{r}{\sin\phi}",
                   "Aylana egrilik radiusi normal bo'ylab "
                   "o'lchanadi, aylana radiusi $r$ ga teng emas.",
                   "R2 ta'rifi"),
            ],
            conditions=(
                "**Yupqa qobiq sharti:** $h/R \\le 1/20$ "
                "(ko'pincha $1/1000$ gacha). Bundan qalinroq "
                "bo'lsa — qalin qobiq nazariyasi yoki 3D "
                "elastiklik (tmm-08).\n\n"
                "**Kirxhoff–Lyav gipotezalari** qobiqqa ham "
                "ko'chiriladi (pq-01): normal to'g'ri va normal "
                "qoladi, $\\sigma_n \\approx 0$. Farqi — endi "
                "normal **egri sirtga** nisbatan.\n\n"
                "**Geometrik cheklovlar:**\n"
                "- $R_1$, $R_2$ silliq o'zgarishi kerak; "
                "sakrash bo'lsa (silindr–sfera tutashuvi) "
                "chekka bezovtaligi paydo bo'ladi (pq-28);\n"
                "- $h \\ll \\min(R_1, R_2)$;\n"
                "- yuklama va geometriya o'zgarish masshtabi "
                "$\\sqrt{Rh}$ dan katta bo'lsa membrana "
                "nazariyasi ishlaydi (pq-26)."
            ),
            worked=WorkedExample(
                statement=(
                    "To'rtta qobiq uchun $R_1$, $R_2$ va $K$ ni "
                    "hisoblang: (a) silindr $R = 2$ m; "
                    "(b) sfera $R = 2$ m; (c) konus, yarim "
                    "burchagi $\\alpha = 30°$, kesimdagi radius "
                    "$r = 1$ m; (d) tor, $R_t = 3$ m, "
                    "$a_t = 1$ m, tashqi ekvatorda va ichki "
                    "ekvatorda."
                ),
                given=[
                    r"\text{(a) silindr } R = 2\ \text{m}",
                    r"\text{(b) sfera } R = 2\ \text{m}",
                    r"\text{(c) konus } \alpha = 30^\circ,\ r = 1\ \text{m}",
                    r"\text{(d) tor } R_t = 3\ \text{m},\ a_t = 1\ \text{m}",
                ],
                steps=[
                    st(r"\text{(a) } R_1 = \infty \ "
                       r"(\text{meridian — to'g'ri chiziq}), \quad "
                       r"R_2 = 2\ \text{m}",
                       "Silindrning yasovchisi to'g'ri chiziq, "
                       "demak meridian egriligi nol."),
                    st(r"K = \frac{1}{\infty \cdot 2} = 0 "
                       r"\;\Rightarrow\; \text{yoyiluvchan}",
                       "Silindrni tekis varaqdan bukib yasash "
                       "mumkin — quvur ishlab chiqarishning asosi."),
                    st(r"\text{(b) } R_1 = R_2 = 2\ \text{m}, \quad "
                       r"K = \frac{1}{4} = 0{,}25\ \text{m}^{-2} > 0",
                       "Sfera — yagona sirt bo'lib, unda "
                       "$R_1 = R_2$ hamma joyda. Yoyilmaydi: "
                       "shuning uchun aniq sferik gumbaz "
                       "yasash qimmat."),
                    st(r"\text{(c) } R_1 = \infty, \quad "
                       r"R_2 = \frac{r}{\cos\alpha} = "
                       r"\frac{1}{\cos 30^\circ} = 1{,}1547\ \text{m}",
                       "Konusda ham yasovchi to'g'ri. "
                       "$R_2$ aylana radiusidan **katta** — "
                       "4-qadamdagi ta'rifning amaliy natijasi."),
                    st(r"K = 0 \;\Rightarrow\; \text{yoyiluvchan}",
                       "Konus ham tekis sektordan yasaladi — "
                       "bunker va voronkalar shundan."),
                    st(r"\text{(d) tashqi ekvator: } R_1 = a_t = 1, "
                       r"\quad R_2 = R_t + a_t = 4\ \text{m}",
                       "Tor kesimining radiusi $R_1$, "
                       "aylana radiusi esa markazdan o'lchanadi."),
                    st(r"K = \frac{1}{1 \cdot 4} = 0{,}25\ "
                       r"\text{m}^{-2} > 0 \ (\text{elliptik})",
                       "Tashqi ekvator sfera kabi ishlaydi."),
                    st(r"\text{ichki ekvator: } R_1 = 1, \quad "
                       r"R_2 = -(R_t - a_t) = -2\ \text{m}, \quad "
                       r"K = -0{,}5\ \text{m}^{-2} < 0",
                       "**Ishora almashdi** — ichki tomonda "
                       "sirt egar shaklida. Bitta tor ichida "
                       "ham elliptik, ham giperbolik zona bor; "
                       "ular orasida $K = 0$ chizig'i yotadi."),
                ],
                answer=(
                    "(a) silindr $K = 0$ — yoyiluvchan; "
                    "(b) sfera $K = +0{,}25$ m⁻² — elliptik; "
                    "(c) konus $R_2 = 1{,}155$ m, $K = 0$ — "
                    "yoyiluvchan; (d) tor tashqi ekvatorda "
                    "$K = +0{,}25$ m⁻², ichki ekvatorda "
                    "$K = -0{,}5$ m⁻² — bitta konstruksiyada "
                    "ikkala tip."
                ),
                engineering_note=(
                    "Tor natijasi amaliy jihatdan muhim: "
                    "quvur burilishlari va tor shaklidagi "
                    "rezervuarlarda ichki (giperbolik) zona "
                    "tashqi zonaga qaraganda boshqacha ishlaydi "
                    "va bosim ostida u yerda kuchlanish "
                    "taqsimoti keskin o'zgaradi. Konusdagi "
                    "$R_2 = r/\\cos\\alpha$ esa idish "
                    "voronkalarini hisoblashda doimiy xato "
                    "manbai — $R_2$ o'rniga $r$ qo'yilsa, "
                    "aylana kuchlanishi $\\cos\\alpha$ marta "
                    "kam chiqadi ($\\alpha = 60°$ da ikki barobar)."
                ),
            ),
            computation=Computation(
                caption=(
                    "Aylanma qobiq geometriyasini sonli tahlil "
                    "qilish: $R_1$, $R_2$, $K$ va yoyiluvchanlik."
                ),
                code='''"""Qobiq geometriyasi: egrilik radiuslari va Gauss egriligi."""
import numpy as np
from labkit import PARAMS, note, series, table, value

shape = int(PARAMS.get("shape", 1))   # 0 silindr, 1 sfera, 2 konus, 3 tor
R = float(PARAMS.get("R", 2000.0))/1000.0
alpha_deg = float(PARAMS.get("alpha", 30.0))
Rt = float(PARAMS.get("Rt", 3000.0))/1000.0
at = float(PARAMS.get("at", 1000.0))/1000.0
h = float(PARAMS.get("h", 5.0))/1000.0

names = {0: "silindr", 1: "sfera", 2: "konus", 3: "tor"}
al = np.radians(alpha_deg)

# Meridian parametri bo'yicha r(t), z(t) ni beramiz va R1, R2 ni
# umumiy formulalar bilan SONLI hisoblaymiz - keyin analitik
# qiymat bilan solishtiramiz.
if shape == 3:
    # Tor davriy: ekvatorlar (psi = 0 va psi = pi) ICHKI nuqta bo'lishi
    # uchun to'liq davrdan sal kengroq oraliq olamiz - aks holda
    # np.gradient chekkada faqat birinchi tartibli aniqlik beradi.
    t = np.linspace(-0.05, 1.05, 441)
else:
    t = np.linspace(0.05, 0.95, 400)

if shape == 0:                       # silindr: r = R, z = L*t
    L = 4.0
    r = np.full_like(t, R)
    z = L*t
    R1_th = np.full_like(t, np.inf)
    R2_th = np.full_like(t, R)
elif shape == 1:                     # sfera: phi = pi*t
    ph = np.pi*t
    r = R*np.sin(ph)
    z = -R*np.cos(ph)
    R1_th = np.full_like(t, R)
    R2_th = np.full_like(t, R)
elif shape == 2:                     # konus
    smax = 3.0
    s = smax*t
    r = s*np.sin(al)
    z = s*np.cos(al)
    R1_th = np.full_like(t, np.inf)
    # normal o'q bilan (90 - alpha) burchak hosil qiladi =>
    # R2 = r/sin(90 - alpha) = r/cos(alpha)
    R2_th = r/np.cos(al)
else:                                # tor
    ps = 2*np.pi*t
    r = Rt + at*np.cos(ps)
    z = at*np.sin(ps)
    R1_th = np.full_like(t, at)
    R2_th = r/np.cos(ps)

dt = t[1] - t[0]
rp = np.gradient(r, dt)
zp = np.gradient(z, dt)
rpp = np.gradient(rp, dt)
zpp = np.gradient(zp, dt)

# Meridian egriligi (tekis egri chiziq formulasi)
num = rp*zpp - zp*rpp
den = (rp**2 + zp**2)**1.5
kap1 = num/np.where(np.abs(den) < 1e-14, 1e-14, den)
# Aylana egriligi: normalning o'qqacha masofasi orqali
# kappa2 = z' / (r * sqrt(r'^2 + z'^2))
kap2 = zp/(r*np.sqrt(rp**2 + zp**2))

K = kap1*kap2
Hm = 0.5*(kap1 + kap2)

value("Qobiq turi (kod)", float(shape), "—")
note(f"Tanlangan sirt: {names[shape]}.")

# O'rta nuqtada taqqoslash
i = len(t)//2
R1_num = 1/kap1[i] if abs(kap1[i]) > 1e-10 else float("inf")
R2_num = 1/kap2[i] if abs(kap2[i]) > 1e-10 else float("inf")
value("R2 (sonli, o'rtada)", R2_num, "m")
value("R2 (analitik, o'rtada)", float(R2_th[i]), "m")
err2 = abs(R2_num - R2_th[i])/abs(R2_th[i])*100
value("R2 nisbiy xatosi", err2, "%")
if np.isfinite(R1_th[i]):
    value("R1 (sonli, o'rtada)", R1_num, "m")
    value("R1 (analitik, o'rtada)", float(R1_th[i]), "m")
    err1 = abs(R1_num - R1_th[i])/abs(R1_th[i])*100
    value("R1 nisbiy xatosi", err1, "%")
    note(f"Sonli differensiallash analitik qiymatni R1 uchun "
         f"{err1:.3f} %, R2 uchun {err2:.3f} % aniqlik bilan "
         f"qaytardi - geometriya to'g'ri parametrlangan.")
else:
    value("1/R1 (sonli, o'rtada)", float(kap1[i]), "1/m")
    note(f"Meridian to'g'ri chiziq: 1/R1 = {kap1[i]:.2e} ~ 0. "
         f"R2 xatosi {err2:.3f} %.")

value("Gauss egriligi K (o'rtada)", float(K[i]), "1/m^2")
value("O'rtacha egrilik H (o'rtada)", float(Hm[i]), "1/m")

Kmid = float(K[i])
if abs(Kmid) < 1e-8:
    tur = "parabolik (K = 0) - YOYILUVCHAN, tekis varaqdan bukiladi"
elif Kmid > 0:
    tur = "elliptik (K > 0) - yoyilmaydi, eng bikr sinf"
else:
    tur = "giperbolik (K < 0) - egar shaklida, ikki oila to'g'ri chiziq"
note(f"Sirt tipi: {tur}.")

series("1/R1 (meridian egriligi)", t.tolist(), kap1.tolist(),
       xlabel="meridian parametri t", ylabel="1/R1, 1/m")
series("1/R2 (aylana egriligi)", t.tolist(), kap2.tolist(),
       xlabel="meridian parametri t", ylabel="1/R2, 1/m")
series("Gauss egriligi K", t.tolist(), K.tolist(),
       xlabel="meridian parametri t", ylabel="K, 1/m^2")
series("Meridian profili r(z)", z.tolist(), r.tolist(),
       xlabel="z, m", ylabel="r, m")

# Torda ishora almashinuvi
if shape == 3:
    # Nol qiymatlarni tashlab yuboramiz: panjara nuqtasi aynan K = 0 ga
    # tushsa, np.sign 0 qaytaradi va bitta kesishuv ikkita sanalardi.
    sg = np.sign(K)
    sg = sg[sg != 0]
    n_cross = int(np.count_nonzero(np.diff(sg)))
    value("K ishorasini almashtirish nuqtalari soni",
          float(n_cross), "—")
    Kout = float(K[np.argmax(r)])
    Kin = float(K[np.argmin(r)])
    value("K tashqi ekvatorda", Kout, "1/m^2")
    value("K ichki ekvatorda", Kin, "1/m^2")
    note(f"Torda K tashqi ekvatorda {Kout:+.4f} (elliptik), ichki "
         f"ekvatorda {Kin:+.4f} (giperbolik) - bitta konstruksiyada "
         f"ikkala tip mavjud va ular orasida K = 0 chizig'i yotadi.")

# --- Qobiq va plastina bikrligini taqqoslash ---
# Taqqoslash har doim BIR XIL o'lchamda: diametri 2R bo'lgan tekis
# qopqoq va radiusi R bo'lgan sferik gumbaz, bir xil h va q.
E = 210e9
nu = 0.3
qload = 10e3
Rs = R
span = 2*Rs
D = E*h**3/(12*(1 - nu**2))
w_plate = 0.004062*qload*span**4/D      # sharnirli kvadrat plastina
w_shell = qload*Rs**2*(1 - nu)/(2*E*h)  # sferik membrana og'ishi
value("Tekis qopqoq og'ishi (chiziqli nazariya)", w_plate*1000, "mm")
value("Sferik qobiq og'ishi (membrana)", w_shell*1000, "mm")
value("Bikrlik nisbati", w_plate/w_shell, "marta")
value("Tekis qopqoq uchun w/h", w_plate/h, "—")
note(f"Bir xil h = {h*1000:.1f} mm, span = {span:.1f} m va "
     f"q = {qload/1000:.0f} kPa da tekis qopqoq {w_plate*1000:.1f} mm, "
     f"sferik qobiq esa {w_shell*1000:.4f} mm og'adi - "
     f"{w_plate/w_shell:.0f} marta farq. Sababi: plastinada bikrlik "
     f"~ h^3, qobiqda ~ h.")

if w_plate/h > 0.5:
    note(f"MUHIM CHEKLOV: tekis qopqoq uchun w/h = {w_plate/h:.0f} >> 0.5, "
         f"ya'ni chiziqli plastina nazariyasi (pq-04) bu yerda "
         f"YAROQSIZ - haqiqiy og'ish fon Karman membrana effekti "
         f"(pq-18) tufayli ancha kichik bo'ladi. Lekin xulosa "
         f"o'zgarmaydi, aksincha kuchayadi: tekis qopqoq bu "
         f"yuklamani faqat MEMBRANAGA aylanib ko'tara oladi, ya'ni "
         f"katta og'ish evaziga sirt ichidagi kuchlar hosil qilishi "
         f"kerak. Qobiq esa xuddi shu membrana kuchlarini "
         f"GEOMETRIYASI hisobiga, deyarli og'ishsiz beradi. "
         f"Yuqoridagi nisbat shu sababli 'chiziqli nazariya "
         f"bo'yicha yuqori baho' sifatida o'qilishi kerak.")

# h ning ta'siri: plastina va qobiq
hs = np.linspace(0.002, 0.02, 100)
wp, ws = [], []
for hh in hs:
    Dh = E*hh**3/(12*(1 - nu**2))
    wp.append(0.004062*qload*span**4/Dh*1000)
    ws.append(qload*Rs**2*(1 - nu)/(2*E*hh)*1000)
series("Tekis plastina og'ishi(h)", (hs*1000).tolist(), wp,
       xlabel="qalinlik h, mm", ylabel="og'ish, mm")
series("Qobiq og'ishi(h)", (hs*1000).tolist(), ws,
       xlabel="qalinlik h, mm", ylabel="og'ish, mm")

table("Aylanma sirtlarning tasnifi",
      ["Sirt", "R1", "R2", "K", "Yoyiladimi"],
      [["Silindr R", "cheksiz", "R", "0", "ha"],
       ["Konus (alpha)", "cheksiz", "r/cos(alpha)", "0", "ha"],
       ["Sfera R", "R", "R", "1/R^2 > 0", "yo'q"],
       ["Tor tashqi", "a_t", "R_t + a_t", "> 0", "yo'q"],
       ["Tor ichki", "a_t", "-(R_t - a_t)", "< 0", "yo'q"],
       ["Giperboloid", "< 0", "> 0", "< 0", "yo'q"]])
''',
                parameters=[
                    p("shape", "Sirt (0 silindr, 1 sfera, 2 konus, 3 tor)",
                      0.0, 3.0, 1.0, 1.0),
                    p("R", "Radius R (silindr/sfera)", 100.0, 20000.0, 2000.0,
                      50.0, "mm"),
                    p("alpha", "Konus yarim burchagi α", 5.0, 85.0, 30.0, 1.0,
                      "°"),
                    p("Rt", "Tor asosiy radiusi R_t", 500.0, 20000.0, 3000.0,
                      100.0, "mm"),
                    p("at", "Tor kesim radiusi a_t", 100.0, 5000.0, 1000.0,
                      50.0, "mm"),
                    p("h", "Qalinlik h", 1.0, 50.0, 5.0, 0.5, "mm"),
                ],
                expected_output=(
                    "Sonli differensiallash analitik egrilik "
                    "radiuslarini 0,1 % dan yaxshi aniqlik bilan "
                    "qaytaradi. Sfera: K = +0,25 m⁻² (elliptik); "
                    "silindr va konus: K = 0 (yoyiluvchan); "
                    "tor: K tashqi ekvatorda musbat, ichki "
                    "ekvatorda manfiy, ikkita ishora "
                    "almashinuv nuqtasi bilan. Bikrlik "
                    "taqqoslashi h = 5 mm da tekis qopqoq va "
                    "sferik qobiq orasida uch tartibdan ortiq "
                    "farq ko'rsatadi."
                ),
            ),
            visual=vis(
                kind="Egrilik xaritasi va sirt tasnifi",
                tool="React/SVG + Manim",
                description=(
                    "Meridian profili, egrilik radiuslari va "
                    "Gauss egriligining sirt bo'ylab taqsimoti."
                ),
                how_to_draw=(
                    "React/SVG: chap panelda meridian profili "
                    "$r(z)$ chiziladi va uning bir nechta "
                    "nuqtasida **normal** ko'rsatiladi; har bir "
                    "normal aylanish o'qigacha davom ettiriladi "
                    "va shu kesma $R_2$ deb belgilanadi — "
                    "shunda $R_2 \\ne r$ ekani ko'z bilan "
                    "ko'rinadi. Meridian egrilik doirasi "
                    "(radius $R_1$) punktir bilan chiziladi. "
                    "O'ng panelda uchta egri chiziq: $1/R_1$, "
                    "$1/R_2$ va $K$; $K$ chizig'i ishorasiga "
                    "qarab bo'yaladi — musbat qismi ko'k "
                    "(elliptik), manfiy qismi qizil "
                    "(giperbolik), nol atrofi kulrang. Tor "
                    "tanlanganda ishora almashinuv nuqtalari "
                    "vertikal chiziq bilan belgilanadi. "
                    "Pastda log o'qli grafik: qalinlik bo'yicha "
                    "tekis plastina va qobiq og'ishlari — ikki "
                    "chiziq turli qiyalikda "
                    "($h^{-3}$ va $h^{-1}$) va ular orasidagi "
                    "masofa shtrixlanadi."
                ),
            ),
            interp=(
                "Sonli differensiallash analitik formulalarni "
                "tasdiqlaydi va bu geometriyaning to'g'ri "
                "parametrlanganini ko'rsatadi — keyingi "
                "mavzularda shu $R_1$, $R_2$ lar bevosita "
                "kuchlanish formulalariga kiradi, shuning "
                "uchun ularni tekshirish zarur edi. Eng "
                "muhim sonli natija — bikrlik taqqoslashi: "
                "bir xil material, bir xil qalinlik va bir "
                "xil yuklamada tekis qopqoq va sferik qobiq "
                "og'ishlari uch tartibdan ortiq farq qiladi. "
                "Bu farq $h$ bo'yicha grafikda yanada aniq "
                "ko'rinadi: ikki chiziqning qiyaligi turli "
                "($-3$ va $-1$), demak qalinlik kamaygani "
                "sari farq **kattalashadi**. Yupqa "
                "konstruksiya qanchalik yupqa bo'lsa, "
                "egrilikning foydasi shunchalik katta. "
                "Tor natijasi esa nazariy jihatdan qiziq: "
                "bitta uzluksiz sirt ichida $K$ ishorasi "
                "almashadi, ya'ni elliptik va giperbolik "
                "zonalar birga yashaydi. Bu zonalar turlicha "
                "ishlaydi va ular chegarasida ($K = 0$ "
                "chizig'ida) qobiq xatti-harakati o'zgaradi — "
                "quvur burilishlarini loyihalashda buni "
                "hisobga olish kerak."
            ),
            mistakes=[
                "$R_2$ ni aylana radiusi $r$ bilan "
                "chalkashtirish. $R_2 = r/\\sin\\phi$ va u "
                "normal bo'ylab o'qqacha o'lchanadi; konusda "
                "$R_2 = r/\\cos\\alpha > r$.",
                "Gauss egriligini o'rtacha egrilik bilan "
                "chalkashtirish. $K = \\kappa_1\\kappa_2$ "
                "(ko'paytma), $H = (\\kappa_1+\\kappa_2)/2$ "
                "(o'rtacha). Faqat $K$ ichki xossa.",
                "Silindrni $K \\ne 0$ deb hisoblash. "
                "Silindr aniq egri ko'rinsa ham "
                "$R_1 = \\infty$, demak $K = 0$ va u "
                "yoyiluvchan.",
                "Qobiqni 'egilgan plastina' deb qarash va "
                "plastina formulalarini qo'llash. Qobiqda "
                "asosiy yuk ko'tarish mexanizmi membrana "
                "kuchlari, egish emas.",
                "Ichki ekvatorda $R_2$ ni musbat olish. "
                "U yerda markaz qarama-qarshi tomonda, "
                "demak $R_2 < 0$ va $K < 0$.",
            ],
            quiz=[
                q("Nima uchun bir xil qalinlikdagi sferik "
                  "qobiq tekis plastinadan ancha bikr?",
                  "Egri sirtda normal ko'chish cho'zilish "
                  "deformatsiyasini ($w/R$) hosil qiladi va "
                  "yuklama membrana kuchlari bilan "
                  "ko'tariladi. Bikrlik $h$ ga chiziqli "
                  "bog'liq, plastinada esa $h^3$ ga.",
                  "konseptual"),
                q("Silindrning Gauss egriligi nechaga teng "
                  "va bu nimani anglatadi?",
                  "$K = 0$, chunki $R_1 = \\infty$. Demak "
                  "silindr yoyiluvchan — uni tekis varaqdan "
                  "cho'zmasdan bukib yasash mumkin.",
                  "hisob"),
                q("Konusda yarim burchak $\\alpha = 60°$, "
                  "kesimdagi radius $r = 0{,}5$ m. $R_2$ "
                  "nechaga teng?",
                  "$R_2 = r/\\cos\\alpha = 0{,}5/0{,}5 = "
                  "1{,}0$ m — aylana radiusidan ikki barobar "
                  "katta.", "hisob"),
                q("Nima uchun sovutish minoralari "
                  "giperboloid shaklida quriladi?",
                  "$K < 0$ sirtni ikki oilali **to'g'ri "
                  "chiziqlardan** qurish mumkin — armatura "
                  "to'g'ri sterjenlardan yig'iladi, "
                  "shu bilan birga qo'sh egrilik bikrlik beradi.",
                  "talqin"),
                q("Kodda tor uchun $K$ ishorasi nechta marta "
                  "almashadi va nima uchun?",
                  "Ikki marta — tashqi elliptik zona bilan "
                  "ichki giperbolik zona orasidagi ikkita "
                  "$K = 0$ chizig'ida "
                  "($\\cos\\psi = 0$, ya'ni yuqori va quyi "
                  "nuqtalarda).", "kod"),
                q("Theorema Egregium qobiq loyihalashda "
                  "nimani anglatadi?",
                  "$K \\ne 0$ sirtni cho'zmasdan tekislikka "
                  "yoyib bo'lmaydi; demak uni ezish uchun "
                  "material cho'zilishi kerak va bu juda "
                  "qimmat — shuning uchun gumbazlar bikr.",
                  "talqin"),
            ],
            bridge=(
                "Geometriya tayyor: har bir nuqtada $R_1$, "
                "$R_2$ va ular orqali $K$ ni bilamiz. Endi "
                "shu geometriyaga kuchlarni qo'shamiz. "
                "Agar egish momentlarini butunlay e'tiborsiz "
                "qoldirsak — bu **membrana nazariyasi** — "
                "qobiq uchun hayratlanarli darajada sodda "
                "va aniq yechim hosil bo'ladi."
            ),
            research=(
                "Gauss egriligi va qobiq bikrligi orasidagi "
                "bog'liqlikni miqdoriy o'rganing. "
                "(1) Tuxum po'sti ($h \\approx 0{,}35$ mm, "
                "$K > 0$) va bir xil qalinlikdagi tekis "
                "parchaning yuk ko'tarish qobiliyatini "
                "taqqoslang. (2) Gofrlangan varaqning "
                "$K = 0$ ekanini ko'rsating va nima uchun "
                "u bir yo'nalishda bikr, boshqasida "
                "egiluvchan ekanini tushuntiring. "
                "(3) Sirtning $K$ ni saqlagan holda "
                "deformatsiyalanishi — inextensional "
                "deformatsiya — nazariyasini o'rganing va "
                "uning silindrik qobiq ustuvorligiga "
                "ta'sirini baholang (pq-29 ga tayyorgarlik)."
            ),
            manim_ref=manim(
                scene="ShellGeometryScene",
                module="animatsiya/scenes/pq_shells.py",
                title="Gauss egriligi va sirt tasnifi",
                summary=(
                    "Tekis varaq ketma-ket silindrga, konusga, "
                    "sferaga va giperboloidga aylanadi; har "
                    "bosqichda $R_1$, $R_2$ va $K$ "
                    "ko'rsatiladi. Yoyiluvchan sirtlar tekis "
                    "varaqqa qaytariladi, yoyilmaydiganlar "
                    "esa yirtilishi ko'rsatiladi."
                ),
            ),
        ),
    ),

    # ------------------------------------------------------------------ pq-26
    Topic(
        id="pq-26",
        subject_id=S, module_id=M, order=26,
        title="Aylanma qobiqlarning membrana nazariyasi: Laplas tenglamasi",
        description=(
            "Egish momentlarisiz muvozanat, Laplas–Yang tenglamasi "
            "$N_\\varphi/R_1 + N_\\theta/R_2 = p$, meridian muvozanati, "
            "bosim ostidagi idishlar va membrana nazariyasining chegaralari."
        ),
        learning_objective=(
            "Aylanma qobiq uchun membrana kuchlarini statik ravishda "
            "aniqlash, bosim ostidagi idishni hisoblash va membrana "
            "nazariyasi qachon buzilishini ko'rsatish."
        ),
        prerequisites=["pq-25", "mq-05"],
        mathematical_core=(
            "$\\dfrac{N_\\varphi}{R_1} + \\dfrac{N_\\theta}{R_2} = p$, "
            "$N_\\varphi = \\dfrac{F_v}{2\\pi r\\sin\\phi}$ — "
            "statik aniqlanuvchi tizim."
        ),
        engineering_application=(
            "Bosim ostidagi idishlar, gaz ballonlari, suv minoralari, "
            "gumbazlar, raketa baklari, quvur va sharsimon rezervuarlar."
        ),
        computational_component=(
            "Silindr, sfera, konus va tor uchun membrana kuchlarini "
            "hisoblash, qalinlikni mustahkamlik bo'yicha tanlash."
        ),
        visualization_component=(
            "$N_\\varphi$ va $N_\\theta$ epyuralari meridian bo'ylab, "
            "kuchlanish ikkiligi, optimal shakl."
        ),
        research_extension=(
            "Membrana nazariyasi qaysi shartlarda buziladi? Statik "
            "aniqlanmaydigan holatlarni va 'membrana mos "
            "kelmasligi' (membrane incompatibility) tushunchasini "
            "o'rganing; teng mustahkam gumbaz shaklini toping."
        ),
        difficulty="murakkab",
        previous_link=(
            "pq-25 da qobiq geometriyasi to'liq tavsiflandi va "
            "normal ko'chish cho'zilish deformatsiyasini hosil "
            "qilishi ko'rsatildi. Endi shu mexanizmni "
            "miqdoriy ifodalaymiz: yuklamani faqat "
            "sirt ichidagi kuchlar ko'taradi deb faraz qilamiz."
        ),
        next_topic="pq-27",
        estimated_minutes=90,
        tags=["membrana", "Laplas", "bosim idishi", "N_phi", "N_theta"],
        lesson=_lesson(
            problem=(
                "Gaz ballonini loyihalayapsiz: ichki bosim "
                "$p = 15$ MPa, hajm 50 litr, po'lat "
                "$\\sigma_{ruxsat} = 250$ MPa. Ikkita variant bor: "
                "silindrik ballon yarim sferik tubli yoki "
                "to'liq sharsimon ballon. Qaysi biri kamroq "
                "metall talab qiladi? Va silindr bilan sfera "
                "tutashgan joyda nima sodir bo'ladi? Bu "
                "savollarga javob berish uchun qobiqdagi "
                "kuchlarni bilish kerak — va ma'lum bo'ladiki, "
                "ularni topish uchun deformatsiyani umuman "
                "hisoblash shart emas."
            ),
            concepts=[
                c("Membrana holati",
                  "Qobiqda egish momentlari va kesuvchi kuchlar "
                  "nolga teng deb qabul qilinadi; faqat sirt "
                  "ichidagi kuchlar $N_\\varphi$, $N_\\theta$, "
                  "$N_{\\varphi\\theta}$ qoladi."),
                c("Meridian kuchi $N_\\varphi$",
                  "Meridian yo'nalishi bo'ylab birlik uzunlikka "
                  "to'g'ri keladigan kuch, N/m; gumbazda u og'irlikni "
                  "tayanchga uzatadi."),
                c("Aylana (halqa) kuchi $N_\\theta$",
                  "Parallel aylana bo'ylab kuch; ballonda u "
                  "eng katta kuchlanishni beradi."),
                c("Laplas–Yang tenglamasi",
                  "$N_\\varphi/R_1 + N_\\theta/R_2 = p$ — normal "
                  "yo'nalishdagi muvozanat; sirt tarangligi "
                  "fizikasidagi bir xil tenglama."),
                c("Statik aniqlanuvchanlik",
                  "Membrana holatida ikkita noma'lum va ikkita "
                  "muvozanat tenglamasi bor — deformatsiya "
                  "kerak emas. Bu qobiq nazariyasidagi noyob "
                  "sodda holat."),
                c("Membrana nazariyasining chegarasi",
                  "U chekkalarda, yuklama sakrashida va "
                  "geometriya uzilishida buziladi — u yerda "
                  "egish momentlari muqarrar (pq-27, pq-28)."),
            ],
            derivation=[
                d("1. Normal yo'nalishdagi muvozanat",
                  r"N_\varphi\,\frac{ds_\varphi\,ds_\theta}{R_1} + "
                  r"N_\theta\,\frac{ds_\varphi\,ds_\theta}{R_2} = "
                  r"p\,ds_\varphi\,ds_\theta",
                  "Elementar to'rtburchakni ajratamiz. Egri "
                  "chiziq bo'ylab tarang kuch normal yo'nalishda "
                  "$N/R$ tashkil etuvchi beradi — xuddi arqonning "
                  "egilgan joyida bo'lgani kabi."),
                d("2. Laplas–Yang tenglamasi",
                  r"\frac{N_\varphi}{R_1} + \frac{N_\theta}{R_2} = p",
                  "$ds_\\varphi ds_\\theta$ qisqaradi. Bu qobiq "
                  "nazariyasidagi eng muhim va eng sodda "
                  "tenglama — sovun pufagidan raketa bakigacha "
                  "hamma joyda o'rinli."),
                d("3. Meridian muvozanati: kesim usuli",
                  r"2\pi r\,N_\varphi \sin\phi = F_v",
                  "Qobiqni parallel aylana bo'ylab kesamiz va "
                  "yuqori qismning vertikal muvozanatini yozamiz. "
                  "$F_v$ — kesimdan yuqoridagi barcha vertikal "
                  "yuklamalar (bosim, og'irlik, qor)."),
                d("4. $N_\\varphi$ ning yechimi",
                  r"N_\varphi = \frac{F_v}{2\pi r\sin\phi} = "
                  r"\frac{F_v}{2\pi r^2/R_2} = \frac{F_v R_2}{2\pi r^2}",
                  "pq-25 dagi $R_2 = r/\\sin\\phi$ dan "
                  "foydalandik. Endi $N_\\varphi$ to'liq "
                  "aniqlangan — **hech qanday deformatsiya "
                  "hisoblanmadi**."),
                d("5. $N_\\theta$ ni Laplasdan topish",
                  r"N_\theta = R_2\Big(p - \frac{N_\varphi}{R_1}\Big)",
                  "Ikkinchi noma'lum birinchisidan bevosita "
                  "kelib chiqadi. Tizim statik aniqlanuvchi."),
                d("6. Silindr uchun ($R_1 = \\infty$, $R_2 = R$)",
                  r"N_\theta = pR, \qquad N_\varphi = \frac{pR}{2} "
                  r"\ (\text{yopiq idish})",
                  "Aylana kuchi meridian kuchidan **ikki barobar** "
                  "katta. Shuning uchun bosim ostidagi quvur "
                  "uzunasiga yoriladi, ko'ndalangiga emas — "
                  "kundalik kuzatuvning aniq izohi."),
                d("7. Sfera uchun ($R_1 = R_2 = R$)",
                  r"N_\varphi = N_\theta = \frac{pR}{2} "
                  r"\;\Longrightarrow\; \sigma = \frac{pR}{2h}",
                  "Simmetriya tufayli ikkala kuch teng. "
                  "Kuchlanish silindrdagi maksimaldan "
                  "**ikki barobar kichik** — sharsimon idish "
                  "materialni eng tejamli ishlatadi."),
                d("8. Membrana nazariyasining o'z-o'zini "
                  "inkor qilishi",
                  r"\varepsilon_\theta^{cyl} = \frac{pR}{Eh}"
                  r"\Big(1 - \frac{\nu}{2}\Big) \ne "
                  r"\varepsilon_\theta^{sph} = \frac{pR}{2Eh}(1 - \nu)",
                  "**Hal qiluvchi kuzatish.** Silindr va sfera "
                  "tutashgan joyda membrana yechimlari turlicha "
                  "radial kengayish beradi. Ular birga "
                  "ulangani uchun mos kelmaslik paydo bo'ladi "
                  "va uni faqat egish momentlari bartaraf "
                  "qila oladi — pq-28 dagi chekka effekti."),
            ],
            meaning=(
                "Membrana nazariyasi muhandislik mexanikasidagi "
                "eng samarali soddalashtirishlardan biri: "
                "u qobiqdagi kuchlarni **statik** yo'l bilan, "
                "deformatsiyaga umuman murojaat qilmasdan "
                "beradi. Buning sababi chuqur — egish "
                "momentlarini tashlab yuborganimizda noma'lumlar "
                "soni tenglamalar soniga teng bo'lib qoladi. "
                "Laplas tenglamasining fizik mazmuni oddiy: "
                "tarang egri chiziq egilgan joyda normal "
                "yo'nalishda kuch beradi va bu kuch "
                "$N/R$ ga teng. Radius qancha kichik bo'lsa, "
                "shuncha ko'p kuch. Ikki yo'nalishda egilgan "
                "sirt esa ikkita shunday hissa qo'shadi — "
                "shuning uchun sferada kuchlanish silindrdagidan "
                "ikki barobar kam: yuklamani ikkita yo'nalish "
                "birgalikda ko'taradi. Bu bosim ostidagi "
                "idishlarni loyihalashning asosi: "
                "$\\sigma_{sfera} = pR/2h$, "
                "$\\sigma_{silindr} = pR/h$. Shu bilan birga "
                "8-qadam nazariyaning o'z chegarasini "
                "ko'rsatadi. Silindr va sferaning membrana "
                "deformatsiyalari har xil, demak ularni "
                "ulaganimizda membrana holati **mumkin emas** — "
                "u mos kelmaslikni bartaraf eta olmaydi. "
                "Aynan shu yerda qobiq nazariyasining ikkinchi "
                "yarmi — egish nazariyasi — boshlanadi. "
                "Membrana yechimi esa hech qachon bekor "
                "bo'lmaydi: u asosiy yechim bo'lib qoladi va "
                "egish faqat chekka yaqinidagi mahalliy tuzatma "
                "sifatida qo'shiladi."
            ),
            equations=[
                eq(r"\frac{N_\varphi}{R_1} + \frac{N_\theta}{R_2} = p",
                   "Laplas–Yang tenglamasi: normal yo'nalishdagi "
                   "muvozanat.", "Laplas tenglamasi"),
                eq(r"N_\varphi = \frac{F_v}{2\pi r\sin\phi}",
                   "Meridian kuchi kesim usulidan; $F_v$ — "
                   "kesimdan yuqoridagi vertikal yuklamalar.",
                   "Meridian muvozanati"),
                eq(r"\text{silindr: } \sigma_\theta = \frac{pR}{h}, "
                   r"\quad \sigma_\varphi = \frac{pR}{2h}",
                   "Silindrik idishdagi kuchlanishlar; "
                   "aylana kuchlanishi ikki barobar katta.",
                   "Silindrik idish"),
                eq(r"\text{sfera: } \sigma_\varphi = \sigma_\theta "
                   r"= \frac{pR}{2h}",
                   "Sferik idishdagi kuchlanish — eng tejamli "
                   "shakl.", "Sferik idish"),
            ],
            conditions=(
                "**Membrana holati amalga oshishi uchun "
                "zarur shartlar** (Timoshenko):\n"
                "1. Chegaraviy yuklamalar qobiqqa "
                "**urinma** ravishda berilishi kerak — "
                "tayanch normal reaksiya bermasin;\n"
                "2. Chekka ko'chishlarga to'sqinlik "
                "qilinmasin (chekka erkin siljiy olsin);\n"
                "3. Yuklama va qalinlik silliq o'zgarsin — "
                "sakrash bo'lmasin;\n"
                "4. Geometriya silliq bo'lsin — $R_1$, $R_2$ "
                "uzluksiz.\n\n"
                "Bu shartlardan bittasi buzilsa ham chekka "
                "yaqinida egish momentlari paydo bo'ladi. "
                "Ular **mahalliy**: $\\sqrt{Rh}$ tartibidagi "
                "zonada so'nadi (pq-27).\n\n"
                "**Chegaraviy shart membrana holatida** faqat "
                "bitta: $N_\\varphi$ chekkada berilgan "
                "qiymatga teng. Ikkinchi tartibli tizim "
                "shuni talab qiladi, ko'chish shartlari esa "
                "qo'yib bo'lmaydi — nazariyaning cheklovi "
                "shundan."
            ),
            worked=WorkedExample(
                statement=(
                    "$p = 15$ MPa, 50 l hajm, po'lat "
                    "$[\\sigma] = 250$ MPa. (A) sharsimon "
                    "ballon; (B) silindrik ballon, "
                    "$L = 4R$, yarim sferik tubli. Har biri "
                    "uchun $R$, $h$ va metall massasini "
                    "toping ($\\rho = 7850$ kg/m³)."
                ),
                given=[
                    r"p = 15\ \text{MPa},\ V = 0{,}05\ \text{m}^3",
                    r"[\sigma] = 250\ \text{MPa},\ \rho = 7850\ "
                    r"\text{kg/m}^3",
                ],
                steps=[
                    st(r"\text{(A) } V = \frac{4}{3}\pi R^3 "
                       r"\;\Rightarrow\; R = \Big(\frac{3 \cdot 0{,}05}"
                       r"{4\pi}\Big)^{1/3} = 0{,}2285\ \text{m}",
                       "Sharsimon ballon radiusi."),
                    st(r"h = \frac{pR}{2[\sigma]} = "
                       r"\frac{15 \cdot 0{,}2285}{2 \cdot 250} "
                       r"= 6{,}855\times10^{-3}\ \text{m} "
                       r"= 6{,}86\ \text{mm}",
                       "Sferada ikkala kuchlanish teng, "
                       "shuning uchun $pR/2h$ ni "
                       "$[\\sigma]$ ga tenglashtiramiz."),
                    st(r"m_A = \rho \cdot 4\pi R^2 h = 7850 \cdot "
                       r"4\pi \cdot 0{,}0522 \cdot 6{,}855\times10^{-3} "
                       r"= 35{,}3\ \text{kg}",
                       "Sirt yuzasi $4\\pi R^2 = 0{,}656$ m²."),
                    st(r"\text{(B) } V = \pi R^2 L + \frac{4}{3}\pi R^3 "
                       r"= \pi R^3\Big(4 + \frac{4}{3}\Big) "
                       r"= 16{,}755 R^3",
                       "Silindrik qism $L = 4R$ va ikkita "
                       "yarim sfera (= bitta to'liq sfera)."),
                    st(r"R = \Big(\frac{0{,}05}{16{,}755}\Big)^{1/3} "
                       r"= 0{,}1440\ \text{m}, \quad "
                       r"L = 4R = 0{,}5759\ \text{m}",
                       "Silindr radiusi sharnikidan kichik, "
                       "lekin ballon uzun."),
                    st(r"h_{cyl} = \frac{pR}{[\sigma]} = "
                       r"\frac{15 \cdot 0{,}1440}{250} = "
                       r"8{,}638\ \text{mm}",
                       "Silindrda $\\sigma_\\theta = pR/h$ — "
                       "aylana kuchlanishi hal qiladi."),
                    st(r"h_{sph} = \frac{pR}{2[\sigma]} = "
                       r"4{,}319\ \text{mm}",
                       "Tublar ikki barobar yupqa bo'lishi "
                       "mumkin — lekin texnologik jihatdan "
                       "ko'pincha bir xil qilinadi."),
                    st(r"m_B = \rho\big(2\pi R L\,h_{cyl} + "
                       r"4\pi R^2 h_{sph}\big) = 7850(0{,}5209 "
                       r"\cdot 0{,}008638 + 0{,}2605 \cdot 0{,}004319)",
                       "Silindr yuzasi $2\\pi RL = 0{,}5209$ m², "
                       "tublar yuzasi $4\\pi R^2 = 0{,}2605$ m²."),
                    st(r"m_B = 7850(4{,}500\times10^{-3} + "
                       r"1{,}125\times10^{-3}) = 44{,}16\ \text{kg}",
                       "Sharsimon ballon **20,0 % yengil** "
                       "($35{,}33$ va $44{,}16$ kg; nisbat "
                       "aynan $1{,}25$). Sababi: sferada "
                       "kuchlanish ikki barobar kam va "
                       "sirt/hajm nisbati eng kichik."),
                    st(r"\text{Tutashuv: } u_{cyl} = "
                       r"\frac{pR^2}{Eh}\Big(1 - \frac{\nu}{2}\Big), "
                       r"\quad u_{sph} = \frac{pR^2}{2Eh}(1-\nu)",
                       "$\\nu = 0{,}3$, bir xil $h$ da: "
                       "$u_{cyl}/u_{sph} = 0{,}85/0{,}35 = 2{,}43$. "
                       "Mos kelmaslik 2,4 barobar — bu yerda "
                       "membrana nazariyasi buziladi va "
                       "chekka effekti boshlanadi (pq-28)."),
                ],
                answer=(
                    "(A) Sharsimon: $R = 228{,}5$ mm, "
                    "$h = 6{,}856$ mm, $m = 35{,}33$ kg. "
                    "(B) Silindrik: $R = 144{,}0$ mm, "
                    "$L = 575{,}9$ mm, $h_{cyl} = 8{,}638$ mm, "
                    "$h_{sph} = 4{,}319$ mm, $m = 44{,}16$ kg. "
                    "**Sharsimon ballon 20,0 % yengil** "
                    "(massa nisbati aynan 1,25), lekin "
                    "silindrik ballon ixchamroq joylashadi "
                    "va arzonroq yasaladi. Tutashuvda radial "
                    "kengayishlar 2,43 barobar farq qiladi."
                ),
                engineering_note=(
                    "Amalda gaz ballonlari silindrik "
                    "yasaladi, garchi shar yengilroq bo'lsa "
                    "ham: sharni ishlab chiqarish qimmat "
                    "(ikkita chuqur shtamplangan yarim "
                    "sferani payvandlash kerak) va u "
                    "transportda joyni tejamsiz egallaydi. "
                    "Katta LPG rezervuarlari esa aksincha — "
                    "sharsimon quriladi, chunki u yerda "
                    "material massasi ustun. Tutashuvdagi "
                    "2,4 barobar farq real muammo: payvand "
                    "chokida mahalliy egish kuchlanishi "
                    "membrana kuchlanishidan oshib ketishi "
                    "mumkin va charchoq yorig'i aynan shu "
                    "yerdan boshlanadi. Shuning uchun "
                    "standartlarda tutashuv zonasi "
                    "qalinlashtiriladi yoki torsimon "
                    "o'tish (knuckle) qo'llaniladi."
                ),
            ),
            computation=Computation(
                caption=(
                    "Aylanma qobiqlar uchun membrana "
                    "kuchlarini hisoblash va idish "
                    "variantlarini massa bo'yicha taqqoslash."
                ),
                code='''"""Membrana nazariyasi: N_phi, N_theta va idish optimallashtirish."""
import numpy as np
from labkit import PARAMS, note, series, table, value

p_int = float(PARAMS.get("p", 15.0))*1e6
V = float(PARAMS.get("V", 50.0)/1000.0)
sig_all = float(PARAMS.get("sig_all", 250.0))*1e6
rho = float(PARAMS.get("rho", 7850.0))
E = float(PARAMS.get("E", 210.0))*1e9
nu = float(PARAMS.get("nu", 0.3))
LR = float(PARAMS.get("LR", 4.0))       # silindr uzunligi / radius

# --- (A) sharsimon ballon ---
Ra = (3*V/(4*np.pi))**(1/3)
ha = p_int*Ra/(2*sig_all)
Aa = 4*np.pi*Ra**2
ma = rho*Aa*ha
value("(A) shar radiusi R", Ra*1000, "mm")
value("(A) qalinlik h", ha*1000, "mm")
value("(A) massa m", ma, "kg")

# --- (B) silindrik ballon, yarim sferik tubli ---
# V = pi*R^2*L + (4/3)*pi*R^3,  L = LR*R
Rb = (V/(np.pi*(LR + 4.0/3.0)))**(1/3)
Lb = LR*Rb
h_cyl = p_int*Rb/sig_all           # sigma_theta = pR/h hal qiladi
h_sph = p_int*Rb/(2*sig_all)
A_cyl = 2*np.pi*Rb*Lb
A_sph = 4*np.pi*Rb**2
mb = rho*(A_cyl*h_cyl + A_sph*h_sph)
value("(B) silindr radiusi R", Rb*1000, "mm")
value("(B) silindr uzunligi L", Lb*1000, "mm")
value("(B) silindr qalinligi", h_cyl*1000, "mm")
value("(B) tub qalinligi", h_sph*1000, "mm")
value("(B) massa m", mb, "kg")
value("Massa farqi (B/A)", mb/ma, "marta")
note(f"Sharsimon ballon {ma:.1f} kg, silindrik ballon {mb:.1f} kg - "
     f"shar {(1 - ma/mb)*100:.1f} % yengil. Sababi: sferada "
     f"kuchlanish pR/2h, silindrda esa pR/h.")

# Hajmni tekshirish
Va = 4/3*np.pi*Ra**3
Vb = np.pi*Rb**2*Lb + 4/3*np.pi*Rb**3
value("(A) hajm tekshiruvi", Va*1000, "l")
value("(B) hajm tekshiruvi", Vb*1000, "l")
note(f"Ikkala variant ham talab qilingan {V*1000:.1f} l hajmni "
     f"beradi: {Va*1000:.4f} l va {Vb*1000:.4f} l - geometriya "
     f"to'g'ri yechilgan.")

# --- Membrana kuchlari: to'rtta qobiq ---
rows = []
# silindr
N_th_c, N_ph_c = p_int*Rb, p_int*Rb/2
rows.append(["Silindr", "cheksiz", f"{Rb:.4f}",
             f"{N_ph_c/1e3:.1f}", f"{N_th_c/1e3:.1f}",
             f"{N_th_c/h_cyl/1e6:.1f}"])
# sfera
N_s = p_int*Ra/2
rows.append(["Sfera", f"{Ra:.4f}", f"{Ra:.4f}",
             f"{N_s/1e3:.1f}", f"{N_s/1e3:.1f}",
             f"{N_s/ha/1e6:.1f}"])
# konus (yarim burchak 30 deg, r = Rb)
alc = np.radians(30.0)
R2c = Rb/np.cos(alc)
N_th_k = p_int*R2c
N_ph_k = p_int*R2c/2
rows.append(["Konus 30deg", "cheksiz", f"{R2c:.4f}",
             f"{N_ph_k/1e3:.1f}", f"{N_th_k/1e3:.1f}",
             f"{N_th_k/h_cyl/1e6:.1f}"])
table("Membrana kuchlari (p ichki bosim)",
      ["Qobiq", "R1, m", "R2, m", "N_phi, kN/m", "N_theta, kN/m",
       "sigma_max, MPa"], rows)

# --- Laplas tenglamasini tekshirish ---
lap_cyl = N_ph_c/np.inf + N_th_c/Rb
lap_sph = N_s/Ra + N_s/Ra
value("Laplas qoldig'i (silindr)", abs(lap_cyl - p_int)/p_int*100, "%")
value("Laplas qoldig'i (sfera)", abs(lap_sph - p_int)/p_int*100, "%")
note("Ikkala holatda ham N_phi/R1 + N_theta/R2 = p aynan "
     "bajarildi - membrana kuchlari Laplas tenglamasini "
     "qanoatlantiradi.")

# --- Tor: membrana kuchlari meridian bo'ylab ---
Rt = 3.0*Rb
at = Rb
ps = np.linspace(0.001, 2*np.pi - 0.001, 400)
r_t = Rt + at*np.cos(ps)
# Aylanma qobiq uchun ichki bosimda:
#   N_phi = p*at/2 * (2*Rt + at*cos(psi))/(Rt + at*cos(psi))
#   N_theta = p*at/2
N_ph_t = p_int*at/2*(2*Rt + at*np.cos(ps))/r_t
N_th_t = np.full_like(ps, p_int*at/2)
series("Tor: N_phi(psi)", ps.tolist(), (N_ph_t/1e3).tolist(),
       xlabel="psi, rad", ylabel="N, kN/m")
series("Tor: N_theta(psi)", ps.tolist(), (N_th_t/1e3).tolist(),
       xlabel="psi, rad", ylabel="N, kN/m")
i_out = int(np.argmax(r_t))
i_in = int(np.argmin(r_t))
value("Tor: N_phi tashqi ekvatorda", float(N_ph_t[i_out])/1e3, "kN/m")
value("Tor: N_phi ichki ekvatorda", float(N_ph_t[i_in])/1e3, "kN/m")
value("Tor: N_phi max/min", float(N_ph_t.max()/N_ph_t.min()), "—")
note(f"Torda N_phi ichki ekvatorda {N_ph_t[i_in]/1e3:.1f} kN/m, "
     f"tashqi ekvatorda {N_ph_t[i_out]/1e3:.1f} kN/m - "
     f"{N_ph_t[i_in]/N_ph_t[i_out]:.2f} marta farq. Shuning uchun "
     f"tor shaklidagi idishlarda ichki tomon kritik.")

# Torda Laplas tenglamasini sonli tekshirish (pq-25 dagi R1, R2)
R1_t = at
R2_t = r_t/np.cos(ps)
lap_t = N_ph_t/R1_t + N_th_t/R2_t
res_t = np.max(np.abs(lap_t - p_int))/p_int*100
value("Tor: Laplas tenglamasi maks. qoldig'i", float(res_t), "%")
note(f"Tor uchun ham Laplas tenglamasi butun meridian bo'ylab "
     f"{res_t:.2e} % aniqlik bilan bajarildi - N_phi va N_theta "
     f"formulalari mustaqil tasdiqlandi.")

# --- Membrana mos kelmasligi: silindr/sfera tutashuvi ---
u_cyl = p_int*Rb**2/(E*h_cyl)*(1 - nu/2)
u_sph = p_int*Rb**2/(2*E*h_cyl)*(1 - nu)   # bir xil h da
value("Silindr radial kengayishi", u_cyl*1000, "mm")
value("Sfera radial kengayishi (bir xil h)", u_sph*1000, "mm")
value("Mos kelmaslik (nisbat)", u_cyl/u_sph, "marta")
value("Mos kelmaslik (farq)", (u_cyl - u_sph)*1000, "mm")
note(f"Bir xil qalinlikda silindr {u_cyl*1000:.4f} mm, sfera "
     f"{u_sph*1000:.4f} mm kengayadi - {u_cyl/u_sph:.2f} marta farq. "
     f"Ular payvandlangani uchun bu mos kelmaslikni faqat EGISH "
     f"momentlari bartaraf qila oladi. Demak membrana nazariyasi "
     f"tutashuvda o'z-o'zini inkor qiladi - pq-28 dagi chekka "
     f"effekti shundan kelib chiqadi.")

# --- Qalinlik/bosim bog'liqligi ---
ps_arr = np.linspace(1e6, 40e6, 120)
h_sph_arr = ps_arr*Ra/(2*sig_all)*1000
h_cyl_arr = ps_arr*Rb/sig_all*1000
series("Sferik idish qalinligi(p)", (ps_arr/1e6).tolist(),
       h_sph_arr.tolist(), xlabel="bosim p, MPa", ylabel="h, mm")
series("Silindrik idish qalinligi(p)", (ps_arr/1e6).tolist(),
       h_cyl_arr.tolist(), xlabel="bosim p, MPa", ylabel="h, mm")

# Yupqa qobiq sharti buzilishini aniqlash
lim = np.where(h_sph_arr/1000/Ra > 0.05)[0]
if len(lim):
    value("Yupqa qobiq sharti buziladigan bosim",
          float(ps_arr[lim[0]]/1e6), "MPa")
    note(f"p > {ps_arr[lim[0]]/1e6:.1f} MPa da h/R > 1/20 bo'ladi va "
         f"yupqa qobiq nazariyasi yaroqsiz - qalin devorli idish "
         f"(Lame yechimi, mq-13) kerak.")
else:
    note(f"Berilgan bosim oralig'ida h/R < 1/20 saqlanadi - "
         f"yupqa qobiq nazariyasi butun oraliqda o'rinli.")
''',
                parameters=[
                    p("p", "Ichki bosim p", 0.1, 60.0, 15.0, 0.5, "MPa"),
                    p("V", "Hajm V", 1.0, 5000.0, 50.0, 1.0, "l"),
                    p("sig_all", "Ruxsat etilgan kuchlanish [σ]",
                      50.0, 900.0, 250.0, 10.0, "MPa"),
                    p("rho", "Zichlik ρ", 1000.0, 20000.0, 7850.0, 50.0,
                      "kg/m³"),
                    p("E", "Yung moduli E", 50.0, 400.0, 210.0, 5.0, "GPa"),
                    p("nu", "Puasson koeffitsienti ν", 0.0, 0.45, 0.3, 0.01),
                    p("LR", "Silindr uzunligi / radius L/R", 1.0, 12.0, 4.0,
                      0.5),
                ],
                expected_output=(
                    "Sharsimon ballon: R = 228,5 mm, "
                    "h = 6,856 mm, m = 35,33 kg. Silindrik: "
                    "R = 144,0 mm, h_cyl = 8,638 mm, "
                    "m = 44,16 kg — shar 20,0 % yengil "
                    "(nisbat aynan 1,25). Ikkala variant ham "
                    "50,000 l hajm beradi. Laplas tenglamasi "
                    "silindr, sfera va tor uchun mashina "
                    "aniqligida bajariladi (qoldiq ~1e-14 %). "
                    "Tor: N_φ ichki ekvatorda tashqidagidan "
                    "1,429 marta katta. Silindr/sfera "
                    "tutashuvida radial kengayishlar 2,43 "
                    "marta farq qiladi (0,1457 va 0,0600 mm). "
                    "p > 25,3 MPa da h/R > 1/20 bo'lib, "
                    "yupqa qobiq nazariyasi yaroqsiz bo'ladi."
                ),
            ),
            visual=vis(
                kind="Membrana kuchlari epyurasi",
                tool="React/SVG + Manim",
                description=(
                    "$N_\\varphi$ va $N_\\theta$ ning meridian "
                    "bo'ylab taqsimoti, idish variantlarining "
                    "taqqoslashi va tutashuvdagi mos kelmaslik."
                ),
                how_to_draw=(
                    "React/SVG: markazda qobiq meridian "
                    "kesimi chiziladi. Uning ustiga ikkita "
                    "epyura qo'yiladi — $N_\\varphi$ meridianga "
                    "perpendikulyar shtrixlar bilan, "
                    "$N_\\theta$ esa normal bo'ylab "
                    "shtrixlar bilan; cho'zilish va siqilish "
                    "turli ranglarda. Tor tanlanganda "
                    "$N_\\varphi$ epyurasi ichki ekvatorda "
                    "sezilarli kengayadi va bu darhol "
                    "ko'rinadi. Pastda tutashuv tugunining "
                    "kattalashtirilgan ko'rinishi: silindr "
                    "va sfera membrana yechimlari bo'yicha "
                    "**turli radiuslarga** kengayadi va "
                    "ular orasida ochiq joy qoladi — bu "
                    "mos kelmaslik punktir bilan va "
                    "$\\Delta u$ o'lchami bilan belgilanadi. "
                    "O'ngda ikkita ballon variantining "
                    "kesimi bir masshtabda, massalari "
                    "yozilgan holda yonma-yon turadi."
                ),
            ),
            interp=(
                "Laplas tenglamasining qoldig'i barcha "
                "qobiqlar uchun mashina aniqligida nolga "
                "teng — bu membrana kuchlari formulalarining "
                "mustaqil tasdig'i, ayniqsa tor uchun, "
                "chunki u yerda $N_\\varphi$ meridian bo'ylab "
                "o'zgaradi va $R_2$ ham (pq-25 dan) "
                "o'zgaruvchan. Hajm tekshiruvi geometriya "
                "to'g'ri yechilganini ko'rsatadi. Idishlar "
                "taqqoslashi aniq muhandislik xulosasini "
                "beradi: shar materialni eng tejamli "
                "ishlatadi, chunki unda kuchlanish "
                "$pR/2h$ va sirt/hajm nisbati minimal. "
                "Torda $N_\\varphi$ ning ichki ekvatorda "
                "1,43 marta kattalashishi pq-25 dagi "
                "$K < 0$ zonasiga to'g'ri keladi — "
                "geometriya va kuch taqsimoti bir-biriga "
                "bog'langan. Eng muhim "
                "natija esa oxirgi blokda: silindr va "
                "sferaning membrana kengayishlari 2,43 "
                "marta farq qiladi. Bu son nazariyaning "
                "o'z-o'zini inkor qilishining miqdoriy "
                "o'lchovi — membrana yechimi tutashuvda "
                "mavjud bo'la olmaydi. Shu sababli keyingi "
                "ikki mavzuda egish nazariyasini qurishimiz "
                "kerak."
            ),
            mistakes=[
                "Silindrda $\\sigma_\\theta$ va "
                "$\\sigma_\\varphi$ ni almashtirib yuborish. "
                "Aylana kuchlanishi $pR/h$ **ikki barobar "
                "katta** — shuning uchun quvur uzunasiga "
                "yoriladi.",
                "Konusda $R_2$ o'rniga aylana radiusini "
                "qo'yish. $R_2 = r/\\cos\\alpha$ (pq-25); "
                "$\\alpha = 60°$ da xato ikki barobar.",
                "Membrana nazariyasini chekka yaqinida "
                "qo'llash. U yerda egish momentlari mavjud "
                "va ular membrana kuchlanishidan katta "
                "bo'lishi mumkin.",
                "Tashqi bosim uchun bir xil formulalarni "
                "ishlatib, ustuvorlikni unutish. Siqilgan "
                "qobiq mustahkamlikdan ancha oldin "
                "ustuvorligini yo'qotadi (pq-29).",
                "$N_\\varphi$ ni topishda kesimdan yuqoridagi "
                "og'irlikni hisobga olmaslik. Gumbazlarda "
                "o'z og'irligi asosiy yuklama.",
            ],
            quiz=[
                q("Nima uchun bosim ostidagi quvur uzunasiga "
                  "yoriladi?",
                  "Aylana kuchlanishi $\\sigma_\\theta = pR/h$ "
                  "meridian kuchlanishidan "
                  "($\\sigma_\\varphi = pR/2h$) ikki barobar "
                  "katta; yoriq eng katta kuchlanishga "
                  "perpendikulyar ochiladi.", "konseptual"),
                q("Membrana nazariyasi nima uchun statik "
                  "aniqlanuvchi?",
                  "Egish momentlari tashlanganda ikkita "
                  "noma'lum ($N_\\varphi$, $N_\\theta$) va "
                  "ikkita muvozanat tenglamasi qoladi — "
                  "deformatsiya hisobga kirmaydi.",
                  "konseptual"),
                q("$p = 2$ MPa, $R = 1$ m, $h = 10$ mm "
                  "sferik idishda kuchlanish qancha?",
                  "$\\sigma = pR/(2h) = 2 \\cdot 1/(2 \\cdot "
                  "0{,}01) = 100$ MPa.", "hisob"),
                q("Kodda Laplas tenglamasining qoldig'i nima "
                  "uchun nolga teng chiqadi?",
                  "$N_\\varphi$ va $N_\\theta$ formulalari "
                  "aynan shu tenglamadan (va meridian "
                  "muvozanatidan) keltirib chiqarilgan; "
                  "qoldiq faqat yaxlitlash xatosini "
                  "ko'rsatadi.", "kod"),
                q("Silindr va sfera tutashuvida nima sodir "
                  "bo'ladi va nima uchun?",
                  "Membrana kengayishlari 2,43 marta farq "
                  "qiladi; birga payvandlangani uchun mos "
                  "kelmaslik faqat egish momentlari bilan "
                  "bartaraf etiladi — chekka effekti "
                  "paydo bo'ladi.", "talqin"),
                q("Sharsimon ballon yengilroq bo'lsa ham "
                  "nima uchun amalda silindrik ballonlar "
                  "ishlatiladi?",
                  "Ishlab chiqarish arzonroq (varaqni "
                  "bukish + ikkita tub), transport va "
                  "joylashtirish qulayroq; massa ustunligi "
                  "faqat katta rezervuarlarda hal qiluvchi "
                  "bo'ladi.", "talqin"),
            ],
            bridge=(
                "Membrana nazariyasi o'z chegarasini o'zi "
                "ko'rsatdi: tutashuvda va chekkada u "
                "mavjud bo'la olmaydi. Keyingi mavzuda "
                "silindrik qobiq misolida egish "
                "nazariyasini quramiz va bezovtalik "
                "qanchalik uzoqqa tarqalishini — "
                "$\\sqrt{Rh}$ masshtabini — topamiz."
            ),
            research=(
                "Membrana nazariyasining chegaralarini "
                "chuqurroq o'rganing. (1) 'Membrana mos "
                "kelmasligi' (membrane incompatibility) "
                "tushunchasini formal ta'riflang: qaysi "
                "geometriya va yuklama juftligida membrana "
                "yechimi mavjud emas? (2) Teng mustahkam "
                "gumbaz shaklini toping — shunday "
                "meridian egri chizig'ini qidiringki, "
                "o'z og'irligi ostida $N_\\varphi = N_\\theta$ "
                "bo'lsin (bu Antonio Gaudi va Frei Otto "
                "ishlatgan zanjir chizig'i — katenoid — "
                "muammosi). (3) Sovun plyonkasi "
                "eksperimenti bilan minimal sirt "
                "($H = 0$) va teng tarangligi orasidagi "
                "bog'liqlikni tekshiring."
            ),
            manim_ref=manim(
                scene="MembraneScene",
                module="animatsiya/scenes/pq_shells.py",
                title="Laplas tenglamasi va membrana kuchlari",
                summary=(
                    "Qobiq elementi ajratiladi, tarang "
                    "kuchlarning normal tashkil etuvchilari "
                    "$N/R$ ko'rsatiladi va ular bosim bilan "
                    "muvozanatlashadi. Keyin silindr va "
                    "sfera bosim ostida kengayadi — "
                    "kengayishlar har xil bo'lib, tutashuvda "
                    "uzilish hosil bo'ladi."
                ),
            ),
        ),
    ),

    # ------------------------------------------------------------------ pq-27
    Topic(
        id="pq-27",
        subject_id=S, module_id=M, order=27,
        title="Silindrik qobiqning egish nazariyasi va chekka effekti",
        description=(
            "Elastik asosdagi balka analogiyasi, to'rtinchi tartibli "
            "tenglama, so'nish parametri $\\beta$, chekka bezovtaligining "
            "$\\sqrt{Rh}$ masshtabi va mahalliy kuchlanishlar."
        ),
        learning_objective=(
            "Silindrik qobiqning egish tenglamasini keltirib chiqarish, "
            "chekka effektini hisoblash, uning so'nish uzunligini "
            "baholash va mahalliy egish kuchlanishini aniqlash."
        ),
        prerequisites=["pq-26", "pq-16"],
        mathematical_core=(
            "$D\\dfrac{d^4w}{dx^4} + \\dfrac{Eh}{R^2}w = p$, "
            "$\\beta = \\sqrt[4]{\\dfrac{3(1-\\nu^2)}{R^2h^2}}$, "
            "so'nish uzunligi $\\ell \\approx \\pi/\\beta \\sim 2{,}4\\sqrt{Rh}$."
        ),
        engineering_application=(
            "Rezervuar tubi bilan devor tutashuvi, quvur flanetslari, "
            "bosim idishlari tublari, silos, mahkamlangan chekkalar."
        ),
        computational_component=(
            "Chekka effektini analitik yechish, so'nish uzunligini "
            "o'lchash va uni $\\sqrt{Rh}$ bilan solishtirish."
        ),
        visualization_component=(
            "So'nuvchi to'lqin $w(x)$, egish momenti epyurasi, "
            "chekka zonasining qobiq uzunligiga nisbati."
        ),
        research_extension=(
            "Chekka effektining so'nish uzunligi va qobiq "
            "uzunligi solishtirilganda nima bo'ladi? Qisqa "
            "silindrlar uchun chekkalar o'zaro ta'sirini "
            "o'rganing va uzun/qisqa qobiq mezonini toping."
        ),
        difficulty="ilg'or",
        previous_link=(
            "pq-26 da membrana nazariyasi silindr va sfera "
            "tutashuvida o'z-o'zini inkor qilishi ko'rsatildi: "
            "kengayishlar 2,43 marta farq qildi. Endi shu "
            "mos kelmaslikni bartaraf etuvchi egish "
            "yechimini quramiz."
        ),
        next_topic="pq-28",
        estimated_minutes=95,
        tags=["silindrik qobiq", "chekka effekti", "beta", "elastik asos"],
        lesson=_lesson(
            problem=(
                "Suv rezervuari: $R = 5$ m, $h = 12$ mm, "
                "balandligi 8 m, tubi fundamentga qattiq "
                "mahkamlangan. Membrana nazariyasi bo'yicha "
                "tubdagi suv bosimi $p = \\rho g H = 78{,}5$ kPa "
                "va aylana kuchlanishi "
                "$\\sigma_\\theta = pR/h = 32{,}7$ MPa — "
                "xavfsiz. Lekin rezervuarlar aynan tub bilan "
                "devor tutashgan joyda yoriladi. Sababi: "
                "mahkamlash radial kengayishga to'sqinlik "
                "qiladi va u yerda membrana yechimi "
                "**mumkin emas**. Mahalliy kuchlanish "
                "qancha va u qay darajada uzoqqa tarqaladi?"
            ),
            concepts=[
                c("Chekka effekti (edge effect)",
                  "Chekkadagi mos kelmaslikni bartaraf etuvchi "
                  "mahalliy egish holati; u qobiq ichiga tez "
                  "so'nadi."),
                c("Elastik asosdagi balka analogiyasi",
                  "Silindrik qobiqning o'qsimmetrik egilishi "
                  "matematik jihatdan Vinkler asosidagi "
                  "balkaga (pq-16) **aynan teng**."),
                c("Qobiq asosining bikrligi",
                  "$k = Eh/R^2$ — radial ko'chishga qarshilik; "
                  "u aylana kuchlaridan kelib chiqadi, "
                  "hech qanday tashqi asos yo'q."),
                c("So'nish parametri $\\beta$",
                  "$\\beta = \\sqrt[4]{3(1-\\nu^2)/(R^2h^2)}$, "
                  "$1/\\beta$ — bezovtalikning xarakterli "
                  "uzunligi; $1/\\beta \\approx 0{,}78\\sqrt{Rh}$."),
                c("$\\sqrt{Rh}$ masshtabi",
                  "Qobiq mexanikasining asosiy uzunlik "
                  "o'lchovi; barcha mahalliy hodisalar shu "
                  "masofada sodir bo'ladi."),
                c("Uzun va qisqa qobiq",
                  "$\\beta L > \\pi$ bo'lsa chekkalar "
                  "mustaqil (uzun qobiq); aks holda ular "
                  "o'zaro ta'sirlashadi."),
            ],
            derivation=[
                d("1. O'qsimmetrik silindrik qobiq: "
                  "radial muvozanat",
                  r"\frac{d Q_x}{dx} + \frac{N_\theta}{R} + p = 0",
                  "Membrana nazariyasidan (pq-26) farqi — "
                  "endi kesuvchi kuch $Q_x$ saqlanadi. "
                  "Aylana kuchi $N_\\theta$ normal yo'nalishda "
                  "$N_\\theta/R$ beradi."),
                d("2. Aylana kuchi radial ko'chish orqali",
                  r"\varepsilon_\theta = \frac{w}{R} "
                  r"\;\Longrightarrow\; N_\theta = "
                  r"\frac{Eh}{R}\,w",
                  "pq-25 dagi asosiy kuzatuv: radial ko'chish "
                  "bevosita aylana deformatsiyasini beradi. "
                  "Bu yerda $w$ ichkariga musbat deb olinadi."),
                d("3. Moment va kesuvchi kuch",
                  r"M_x = -D\frac{d^2w}{dx^2}, \qquad "
                  r"Q_x = \frac{dM_x}{dx} = -D\frac{d^3w}{dx^3}",
                  "Meridian bo'ylab qobiq balka kabi ishlaydi; "
                  "$D$ — plastinadagi kabi silindrik bikrlik, "
                  "chunki aylana bo'ylab deformatsiya "
                  "to'sqinlik qiladi."),
                d("4. Asosiy tenglama",
                  r"D\frac{d^4w}{dx^4} + \frac{Eh}{R^2}\,w = p",
                  "**Hal qiluvchi natija.** Bu aynan Vinkler "
                  "asosidagi balka tenglamasi (pq-16), "
                  "$k = Eh/R^2$ bilan. Qobiq o'zining aylana "
                  "kuchlari hisobiga o'ziga asos bo'lib "
                  "xizmat qiladi."),
                d("5. So'nish parametri",
                  r"\beta^4 = \frac{k}{4D} = \frac{Eh}{4R^2D} "
                  r"= \frac{3(1-\nu^2)}{R^2h^2}",
                  "$D = Eh^3/[12(1-\\nu^2)]$ ni qo'ydik. "
                  "$E$ qisqardi — $\\beta$ faqat "
                  "**geometriyaga** va $\\nu$ ga bog'liq, "
                  "materialga emas."),
                d("6. $\\beta$ ning $\\sqrt{Rh}$ bilan bog'lanishi",
                  r"\beta = \frac{\sqrt[4]{3(1-\nu^2)}}{\sqrt{Rh}} "
                  r"\approx \frac{1{,}285}{\sqrt{Rh}} \ "
                  r"(\nu = 0{,}3)",
                  "Demak $1/\\beta \\approx 0{,}778\\sqrt{Rh}$ — "
                  "qobiq mexanikasidagi universal masshtab. "
                  "$R = 5$ m, $h = 12$ mm uchun "
                  "$\\sqrt{Rh} = 0{,}245$ m."),
                d("7. Chekka uchun so'nuvchi yechim",
                  r"w_{edge}(x) = e^{-\beta x}\big(C_1\cos\beta x "
                  r"+ C_2\sin\beta x\big)",
                  "To'liq yechimning to'rtta ildizidan "
                  "ikkitasi o'suvchi — ular uzun qobiqda "
                  "tashlanadi. Qolgan ikkitasi so'nuvchi "
                  "tebranish beradi."),
                d("8. Mahkamlangan chekka uchun konstantalar",
                  r"w(0) = -w_m, \ w'(0) = 0 \;\Longrightarrow\; "
                  r"C_1 = C_2 = -w_m",
                  "$w_m = pR^2/(Eh)$ — membrana kengayishi. "
                  "Mahkamlash uni nolga keltirishi kerak, "
                  "demak chekka yechimi uni aynan "
                  "kompensatsiya qiladi."),
                d("9. Chekkadagi moment",
                  r"M_0 = -D\,w''(0) = \frac{p}{2\beta^2} = "
                  r"\frac{p R h}{2\sqrt{3(1-\nu^2)}}",
                  "Mahalliy egish momenti. Unga mos "
                  "kuchlanish "
                  "$\\sigma_b = 6M_0/h^2$ va u membrana "
                  "kuchlanishi bilan solishtiriladi."),
                d("10. Egish va membrana kuchlanishlari nisbati",
                  r"\frac{\sigma_b}{\sigma_\theta} = "
                  r"\frac{6M_0/h^2}{pR/h} = "
                  r"\frac{3}{\sqrt{3(1-\nu^2)}} = "
                  r"\sqrt{\frac{3}{1-\nu^2}} \approx 1{,}82",
                  "**Hayratlanarli natija:** nisbat "
                  "$R$ ga ham, $h$ ga ham, $p$ ga ham "
                  "bog'liq emas! Mahkamlangan chekkada "
                  "egish kuchlanishi har doim membrana "
                  "kuchlanishidan ~1,8 marta katta."),
            ],
            meaning=(
                "Bu mavzuning markazida ikkita chuqur natija "
                "bor. Birinchisi 4-qadamda: silindrik "
                "qobiqning o'qsimmetrik egilishi elastik "
                "asosdagi balkaga aynan teng. Bu tasodif "
                "emas — qobiqda radial ko'chish aylana "
                "kuchlarini uyg'otadi va ular xuddi "
                "prujinalar kabi $N_\\theta/R = Ehw/R^2$ "
                "qaytaruvchi kuch beradi. Shuning uchun "
                "pq-16 da o'rganilgan butun apparat "
                "(Kelvin funksiyalari, xarakterli uzunlik, "
                "so'nuvchi to'lqin) bu yerda "
                "to'g'ridan-to'g'ri ishlaydi. Ikkinchi "
                "natija 10-qadamda: mahkamlangan chekkada "
                "egish va membrana kuchlanishlari nisbati "
                "$\\sqrt{3/(1-\\nu^2)} \\approx 1{,}82$ — "
                "**universal doimiy**. Rezervuar 5 m "
                "bo'ladimi yoki 50 m, devor 12 mm "
                "bo'ladimi yoki 40 mm — chekkadagi egish "
                "kuchlanishi membrana kuchlanishidan "
                "taxminan 1,8 marta katta bo'lib qolaveradi. "
                "Bu nima uchun rezervuarlar aynan tub "
                "yaqinida yorilishining aniq izohi va u "
                "loyihalashda to'g'ridan-to'g'ri qo'llaniladi. "
                "$\\sqrt{Rh}$ masshtabi esa qobiq "
                "mexanikasining 'tabiiy o'lchov birligi'. "
                "U geometrik o'rtacha: qobiqning eng katta "
                "($R$) va eng kichik ($h$) o'lchamlari "
                "orasida. Barcha mahalliy hodisalar — "
                "chekka effekti, konsentrlangan yuklama, "
                "geometriya uzilishi, hatto ustuvorlik "
                "to'lqini (pq-29) — shu masofada sodir "
                "bo'ladi. $R = 5$ m, $h = 12$ mm rezervuarda "
                "bu atigi 0,25 m: 8 metrlik devorning "
                "3 % i. Qolgan 97 % da membrana nazariyasi "
                "mukammal ishlaydi. Shuning uchun "
                "membrana yechimi hech qachon bekor "
                "bo'lmaydi — u asos, egish esa mahalliy "
                "tuzatma."
            ),
            equations=[
                eq(r"D\frac{d^4w}{dx^4} + \frac{Eh}{R^2}w = p",
                   "Silindrik qobiqning o'qsimmetrik egilish "
                   "tenglamasi — Vinkler asosidagi balka "
                   "tenglamasining aynan o'zi.",
                   "Qobiq egilish tenglamasi"),
                eq(r"\beta = \sqrt[4]{\frac{3(1-\nu^2)}{R^2h^2}} "
                   r"\approx \frac{1{,}285}{\sqrt{Rh}}",
                   "So'nish parametri; $1/\\beta$ — "
                   "bezovtalikning xarakterli uzunligi.",
                   "So'nish parametri"),
                eq(r"w(x) = e^{-\beta x}(C_1\cos\beta x + "
                   r"C_2\sin\beta x)",
                   "Chekka effektining so'nuvchi tebranma "
                   "yechimi.", "Chekka yechimi"),
                eq(r"\frac{\sigma_b}{\sigma_\theta} = "
                   r"\sqrt{\frac{3}{1-\nu^2}} \approx 1{,}82",
                   "Mahkamlangan chekkadagi egish va "
                   "membrana kuchlanishlari nisbati — "
                   "geometriyaga bog'liq emas.",
                   "Universal nisbat"),
            ],
            conditions=(
                "**Chegaraviy shartlar** (chekkada, $x = 0$):\n"
                "- Qattiq mahkamlash: $w = -w_m$, "
                "$dw/dx = 0$ (membrana kengayishi to'liq "
                "to'sqinlik qilinadi);\n"
                "- Sharnirli: $w = -w_m$, $M_x = 0$;\n"
                "- Erkin: $M_x = 0$, $Q_x = 0$ — chekka "
                "effekti yo'q, sof membrana;\n"
                "- Elastik ulanish: $M_x = c_\\theta\\,dw/dx$.\n\n"
                "**Uzoqda ($x \\to \\infty$):** $w \\to 0$ — "
                "bu o'suvchi eksponentalarni tashlash "
                "asosidir.\n\n"
                "**Uzun qobiq sharti:** $\\beta L > \\pi$ "
                "(ba'zi manbalarda $> 4$). Aks holda "
                "ikkala chekkaning yechimlari qo'shilishi "
                "kerak va to'rtta konstanta uchun 4×4 "
                "tizim yechiladi.\n\n"
                "**Qo'llanish chegarasi:** yechim chiziqli, "
                "ya'ni $w \\ll h$ bo'lishi kerak; katta "
                "og'ishlarda geometrik nochiziqlilik "
                "(pq-18) qo'shiladi."
            ),
            worked=WorkedExample(
                statement=(
                    "Suv rezervuari: $R = 5$ m, $h = 12$ mm, "
                    "$H = 8$ m, po'lat $E = 210$ GPa, "
                    "$\\nu = 0{,}3$. Tubi qattiq mahkamlangan. "
                    "Tubdagi bosim, membrana kuchlanishi, "
                    "chekkadagi moment, egish kuchlanishi va "
                    "chekka zonasining uzunligini toping."
                ),
                given=[
                    r"R = 5\ \text{m},\ h = 0{,}012\ \text{m},\ "
                    r"H = 8\ \text{m}",
                    r"E = 210\ \text{GPa},\ \nu = 0{,}3,\ "
                    r"\rho g = 9810\ \text{N/m}^3",
                ],
                steps=[
                    st(r"p = \rho g H = 9810 \cdot 8 = "
                       r"78\,480\ \text{Pa} = 78{,}48\ \text{kPa}",
                       "Tubdagi gidrostatik bosim."),
                    st(r"\sigma_\theta = \frac{pR}{h} = "
                       r"\frac{78\,480 \cdot 5}{0{,}012} = "
                       r"32{,}70\ \text{MPa}",
                       "Membrana (aylana) kuchlanishi — "
                       "po'lat uchun mutlaqo xavfsiz."),
                    st(r"\sqrt{Rh} = \sqrt{5 \cdot 0{,}012} = "
                       r"\sqrt{0{,}06} = 0{,}2449\ \text{m}",
                       "Qobiqning tabiiy uzunlik masshtabi."),
                    st(r"\beta = \frac{[3(1-0{,}09)]^{1/4}}"
                       r"{\sqrt{Rh}} = \frac{2{,}730^{1/4}}"
                       r"{0{,}2449} = \frac{1{,}2850}{0{,}2449} "
                       r"= 5{,}247\ \text{m}^{-1}",
                       "$3(1-\\nu^2) = 2{,}73$, uning "
                       "4-darajali ildizi 1,285."),
                    st(r"w_m = \frac{pR^2}{Eh} = "
                       r"\frac{78\,480 \cdot 25}"
                       r"{210\times10^{9} \cdot 0{,}012} = "
                       r"7{,}786\times10^{-4}\ \text{m} = "
                       r"0{,}779\ \text{mm}",
                       "Erkin devor shuncha kengayardi; "
                       "mahkamlash buni to'sadi."),
                    st(r"M_0 = \frac{p}{2\beta^2} = "
                       r"\frac{78\,480}{2 \cdot 27{,}53} = "
                       r"1425\ \text{N·m/m}",
                       "Chekkadagi egish momenti "
                       "($\\beta^2 = 27{,}53$ m⁻²)."),
                    st(r"\sigma_b = \frac{6M_0}{h^2} = "
                       r"\frac{6 \cdot 1425}{1{,}44\times10^{-4}} "
                       r"= 59{,}4\ \text{MPa}",
                       "Mahalliy egish kuchlanishi — "
                       "membrana kuchlanishidan "
                       "**1,82 marta katta**."),
                    st(r"\sigma_{max} = \sigma_b + "
                       r"\nu\sigma_\theta^{loc} \approx "
                       r"59{,}4 + \ldots \;\Rightarrow\; "
                       r"\frac{\sigma_b}{\sigma_\theta} = "
                       r"\sqrt{\frac{3}{1-0{,}09}} = 1{,}816",
                       "Universal nisbat 10-qadamdan; "
                       "u $R$, $h$, $p$ ga bog'liq emas."),
                    st(r"\ell = \frac{\pi}{\beta} = "
                       r"\frac{3{,}1416}{5{,}247} = "
                       r"0{,}599\ \text{m} \approx "
                       r"2{,}44\sqrt{Rh}",
                       "Birinchi nolgacha bo'lgan masofa — "
                       "chekka zonasining amaliy uzunligi. "
                       "Bu 8 m devorning atigi **7,5 %** i."),
                    st(r"x_{1\%}: e^{-\beta x} = 0{,}01 "
                       r"\;\Rightarrow\; x = \frac{4{,}605}"
                       r"{5{,}247} = 0{,}878\ \text{m}",
                       "0,88 m dan keyin bezovtalik 1 % dan "
                       "kam — qolgan 89 % devorda membrana "
                       "nazariyasi mukammal ishlaydi."),
                ],
                answer=(
                    "$p = 78{,}48$ kPa, "
                    "$\\sigma_\\theta = 32{,}70$ MPa, "
                    "$\\beta = 5{,}247$ m⁻¹, "
                    "$w_m = 0{,}779$ mm, "
                    "$M_0 = 1425$ N·m/m, "
                    "$\\sigma_b = 59{,}4$ MPa. Egish "
                    "kuchlanishi membrana kuchlanishidan "
                    "**1,82 marta katta** va bu nisbat "
                    "universal. Chekka zonasi 0,6 m "
                    "($2{,}44\\sqrt{Rh}$), bezovtalik "
                    "0,88 m da 1 % gacha so'nadi."
                ),
                engineering_note=(
                    "59,4 MPa hali ham po'lat uchun "
                    "xavfsiz, lekin manzara boshqacha "
                    "bo'lishi mumkin: birinchidan, bu "
                    "kuchlanish payvand chokiga to'g'ri "
                    "keladi va u yerda material xossalari "
                    "yomonroq hamda qoldiq kuchlanishlar "
                    "bor; ikkinchidan, rezervuar "
                    "to'ldirilib-bo'shatilgani sari "
                    "kuchlanish sikl bo'yicha o'zgaradi va "
                    "charchoq boshlanadi; uchinchidan, "
                    "$\\sigma_b/\\sigma_\\theta = 1{,}82$ "
                    "nisbati o'zgarmagani uchun devorni "
                    "qalinlashtirish **yordam bermaydi** — "
                    "ikkala kuchlanish ham bir xil "
                    "kamayadi. To'g'ri yechim — chekkani "
                    "moslashuvchan qilish: sharnirli "
                    "ulanish, elastik prokladka yoki "
                    "tubga silliq o'tish. Shuning uchun "
                    "katta rezervuarlarda tub bilan devor "
                    "orasida maxsus egiluvchan tugun "
                    "quriladi."
                ),
            ),
            computation=Computation(
                caption=(
                    "Chekka effektini yechish, so'nish "
                    "uzunligini o'lchash va uni "
                    "$\\sqrt{Rh}$ masshtabi bilan "
                    "solishtirish."
                ),
                code='''"""Silindrik qobiqning chekka effekti."""
import numpy as np
from labkit import PARAMS, note, series, table, value

R = float(PARAMS.get("R", 5000.0))/1000.0
h = float(PARAMS.get("h", 12.0))/1000.0
H = float(PARAMS.get("H", 8.0))
E = float(PARAMS.get("E", 210.0))*1e9
nu = float(PARAMS.get("nu", 0.3))
rhog = float(PARAMS.get("rhog", 9810.0))
bc = int(PARAMS.get("bc", 0))          # 0 mahkam, 1 sharnirli

D = E*h**3/(12*(1 - nu**2))
k_found = E*h/R**2                     # qobiq "asosi" bikrligi
beta = (3*(1 - nu**2)/(R**2*h**2))**0.25
sqRh = np.sqrt(R*h)

value("Silindrik bikrlik D", D, "N*m")
value("Qobiq asosi bikrligi k = Eh/R^2", k_found/1e6, "MPa/m")
value("So'nish parametri beta", beta, "1/m")
value("sqrt(R*h)", sqRh, "m")
value("beta * sqrt(R*h)", beta*sqRh, "—")
value("Nazariy [3(1-nu^2)]^(1/4)", (3*(1 - nu**2))**0.25, "—")
note(f"beta*sqrt(Rh) = {beta*sqRh:.6f}, nazariy qiymat "
     f"[3(1-nu^2)]^(1/4) = {(3*(1-nu**2))**0.25:.6f} - aynan mos. "
     f"Demak beta faqat geometriyaga va nu ga bog'liq, E ga emas.")

# beta^4 = k/(4D) ekanligini mustaqil tekshirish
beta_alt = (k_found/(4*D))**0.25
value("beta (k/(4D) orqali)", beta_alt, "1/m")
value("Ikki yo'l farqi", abs(beta - beta_alt)/beta*100, "%")
note(f"beta ni ikki mustaqil yo'l bilan hisobladik: geometrik "
     f"formuladan {beta:.6f} va elastik asos analogiyasidan "
     f"(k/4D)^(1/4) = {beta_alt:.6f} - farq "
     f"{abs(beta-beta_alt)/beta*100:.2e} %. Vinkler analogiyasi "
     f"tasdiqlandi.")

# --- Chekka effekti yechimi ---
p0 = rhog*H
sig_mem = p0*R/h
wm = p0*R**2/(E*h)
value("Tubdagi bosim p", p0/1000, "kPa")
value("Membrana kuchlanishi sigma_theta", sig_mem/1e6, "MPa")
value("Membrana kengayishi w_m", wm*1000, "mm")

# Oraliq kamida uchta cho'qqini (beta*x = pi, 2pi, 3pi) qamrashi kerak,
# aks holda so'nish tezligini o'lchab bo'lmaydi.
x = np.linspace(0.0, min(10.5/beta, H), 900)
bx = beta*x
ex = np.exp(-bx)
cb, sb_ = np.cos(bx), np.sin(bx)
if bc == 0:      # qattiq mahkamlash: w(0) = -wm, w'(0) = 0
    C1 = C2 = -wm
else:            # sharnirli: w(0) = -wm, M(0) = 0 => C1 = -wm, C2 = 0
    C1, C2 = -wm, 0.0
w_e = ex*(C1*cb + C2*sb_)

# Ikkinchi hosila ANIQ ko'rinishda:
#   f  = e^(-bx)*(A*cos + B*sin)
#   f'' = 2*beta^2*e^(-bx)*(A*sin - B*cos)
w_e_xx = 2*beta**2*ex*(C1*sb_ - C2*cb)
M_x = -D*w_e_xx
M0 = float(M_x[0])

# Aniq hosilani ICHKI nuqtada sonli hosila bilan tekshiramiz
# (chekkada np.gradient faqat birinchi tartibli, shuning uchun
#  taqqoslash ichkarida bajariladi).
d2_num = np.gradient(np.gradient(w_e, x), x)
j = len(x)//4
value("w'' (aniq, ichki nuqtada)", float(w_e_xx[j]), "1/m")
value("w'' (sonli, ichki nuqtada)", float(d2_num[j]), "1/m")
err_d2 = abs(d2_num[j] - w_e_xx[j])/abs(w_e_xx[j])*100
value("w'' nisbiy xatosi", err_d2, "%")
note(f"Aniq analitik ikkinchi hosila va markaziy ayirma "
     f"ichki nuqtada {err_d2:.4f} % farq qiladi - moment "
     f"formulasi to'g'ri.")

M0_th = -p0/(2*beta**2) if bc == 0 else 0.0
value("Chekkadagi moment M0 (yechimdan)", M0, "N*m/m")
value("Chekkadagi moment M0 (p/(2*beta^2) formulasidan)",
      M0_th, "N*m/m")
if M0_th != 0:
    value("M0 nisbiy xatosi", abs(M0 - M0_th)/abs(M0_th)*100, "%")
    note(f"Chekkadagi moment ikki yo'l bilan: chekka yechimini "
         f"differensiallab {M0:.2f} N*m/m, analitik "
         f"p/(2*beta^2) formulasidan {M0_th:.2f} N*m/m - farq "
         f"{abs(M0-M0_th)/abs(M0_th):.2e} %. Ishora manfiy: "
         f"mahkamlash devorni ICHKARIGA egadi.")

sig_b = 6*abs(M0)/h**2
value("Egish kuchlanishi sigma_b", sig_b/1e6, "MPa")
if sig_mem > 0:
    ratio = sig_b/sig_mem
    ratio_th = np.sqrt(3/(1 - nu**2))
    value("sigma_b / sigma_theta", ratio, "—")
    value("Nazariy sqrt(3/(1-nu^2))", ratio_th, "—")
    if bc == 0:
        note(f"Nisbat {ratio:.4f}, nazariy qiymat {ratio_th:.4f} - "
             f"farq {abs(ratio-ratio_th)/ratio_th*100:.2e} %. Bu nisbat "
             f"R, h va p ga BOG'LIQ EMAS: devorni qalinlashtirish "
             f"ikkala kuchlanishni ham bir xil kamaytiradi.")
    else:
        note(f"Sharnirli chekkada M0 = 0, demak mahalliy egish "
             f"kuchlanishi yo'q - bu mahkamlangan chekkaga "
             f"nisbatan katta afzallik.")

# --- To'liq radial ko'chish: membrana + chekka ---
w_tot = wm + w_e
series("Radial ko'chish w(x)", x.tolist(), (w_tot*1000).tolist(),
       xlabel="tubdan masofa x, m", ylabel="w, mm")
series("Membrana yechimi", x.tolist(),
       (np.full_like(x, wm)*1000).tolist(),
       xlabel="tubdan masofa x, m", ylabel="w, mm")
series("Egish momenti M(x)", x.tolist(), (M_x/1000).tolist(),
       xlabel="tubdan masofa x, m", ylabel="M, kN*m/m")

# --- So'nish tezligini O'LCHASH: cho'qqilar bo'yicha beta ni tiklash ---
aw = np.abs(w_e)
pk = [i for i in range(1, len(aw) - 1)
      if aw[i] > aw[i-1] and aw[i] >= aw[i+1] and aw[i] > 1e-18]
if len(pk) >= 2:
    xp = x[pk]
    yp = np.log(aw[pk])
    slope = np.polyfit(xp, yp, 1)[0]
    beta_fit = -slope
    value("beta (cho'qqilardan tiklangan)", beta_fit, "1/m")
    value("beta tiklash xatosi", abs(beta_fit - beta)/beta*100, "%")
    note(f"Yechim cho'qqilarining logarifmiga to'g'ri chiziq "
         f"moslashtirib beta = {beta_fit:.4f} 1/m tiklandi; "
         f"analitik qiymat {beta:.4f} 1/m - farq "
         f"{abs(beta_fit-beta)/beta*100:.3f} %. So'nish haqiqatan "
         f"ham exp(-beta*x) qonuni bo'yicha boradi.")

# O'rama (envelope) 1 % gacha tushadigan masofa
x1 = np.log(100.0)/beta
value("O'rama 1 % gacha so'nadigan masofa", x1, "m")
value("So'nish masofasi / sqrt(R*h)", x1/sqRh, "—")
value("Chekka zonasining balandlikdagi ulushi", x1/H*100, "%")
note(f"exp(-beta*x) o'ramasi {x1:.4f} m = {x1/sqRh:.3f}*sqrt(Rh) "
     f"da 1 % gacha tushadi. Chekka zonasi butun balandlikning "
     f"{x1/H*100:.1f} % ini egallaydi - qolgan qismda membrana "
     f"nazariyasi (pq-26) mukammal ishlaydi.")

# Birinchi nol nuqtasi (mahkamlangan chekka uchun)
if bc == 0:
    ell = np.pi/beta
    value("Birinchi nolgacha masofa pi/beta", ell, "m")
    value("pi/beta / sqrt(R*h)", ell/sqRh, "—")

# --- Uzun/qisqa qobiq mezoni ---
value("beta * L (L = balandlik)", beta*H, "—")
if beta*H > np.pi:
    note(f"beta*L = {beta*H:.2f} > pi: qobiq UZUN, chekkalar "
         f"mustaqil ishlaydi va o'suvchi eksponentalarni tashlash "
         f"o'rinli.")
else:
    note(f"beta*L = {beta*H:.2f} < pi: qobiq QISQA, ikkala chekka "
         f"o'zaro ta'sirlashadi va to'rtta konstanta uchun 4x4 "
         f"tizim yechilishi kerak.")

# --- R/h ning nisbatga ta'siri: universal ekanini ko'rsatish ---
rows = []
for (Rv, hv, pv) in [(5.0, 0.012, 78480.0), (20.0, 0.012, 78480.0),
                     (5.0, 0.040, 78480.0), (5.0, 0.012, 200000.0),
                     (50.0, 0.030, 500000.0)]:
    bt = (3*(1 - nu**2)/(Rv**2*hv**2))**0.25
    sm = pv*Rv/hv
    m0 = pv/(2*bt**2)
    sb = 6*m0/hv**2
    rows.append([f"{Rv:.0f}", f"{hv*1000:.0f}", f"{pv/1000:.0f}",
                 f"{sm/1e6:.1f}", f"{sb/1e6:.1f}", f"{sb/sm:.4f}"])
table("sigma_b/sigma_theta nisbatining universalligi",
      ["R, m", "h, mm", "p, kPa", "sigma_theta, MPa",
       "sigma_b, MPa", "nisbat"], rows)
rr = [float(r[-1]) for r in rows]
value("Nisbatning maks. og'ishi", (max(rr) - min(rr))/min(rr)*100, "%")
note(f"Besh xil geometriya va bosimda nisbat {min(rr):.4f} dan "
     f"{max(rr):.4f} gacha - ya'ni O'ZGARMAYDI. Bu 10-qadamdagi "
     f"analitik xulosaning sonli tasdig'i.")

# --- So'nish uzunligining R va h ga bog'liqligi ---
hs = np.linspace(0.004, 0.05, 120)
ells = [np.pi/((3*(1 - nu**2)/(R**2*hh**2))**0.25) for hh in hs]
sqs = [2.44*np.sqrt(R*hh) for hh in hs]
series("Chekka zonasi uzunligi pi/beta", (hs*1000).tolist(), ells,
       xlabel="qalinlik h, mm", ylabel="uzunlik, m")
series("2.44*sqrt(R*h)", (hs*1000).tolist(), sqs,
       xlabel="qalinlik h, mm", ylabel="uzunlik, m")
dev = max(abs(a - b)/b for a, b in zip(ells, sqs))
value("pi/beta va 2.44*sqrt(Rh) maks. farqi", dev*100, "%")
note(f"pi/beta va 2.44*sqrt(Rh) butun oraliqda {dev*100:.3f} % "
     f"gacha farq qiladi - sqrt(Rh) haqiqatan ham qobiqning "
     f"tabiiy uzunlik masshtabi.")
''',
                parameters=[
                    p("R", "Rezervuar radiusi R", 200.0, 60000.0, 5000.0,
                      100.0, "mm"),
                    p("h", "Devor qalinligi h", 2.0, 100.0, 12.0, 0.5, "mm"),
                    p("H", "Balandlik / uzunlik", 0.5, 40.0, 8.0, 0.5, "m"),
                    p("E", "Yung moduli E", 50.0, 400.0, 210.0, 5.0, "GPa"),
                    p("nu", "Puasson koeffitsienti ν", 0.0, 0.45, 0.3, 0.01),
                    p("rhog", "Suyuqlik solishtirma og'irligi ρg",
                      1000.0, 30000.0, 9810.0, 100.0, "N/m³"),
                    p("bc", "Chekka (0 mahkam, 1 sharnirli)", 0.0, 1.0, 0.0,
                      1.0),
                ],
                expected_output=(
                    "β = 5,2477 m⁻¹ va β·√(Rh) = 1,28541 — "
                    "nazariy [3(1−ν²)]^(1/4) bilan aynan mos. "
                    "β **uchta** mustaqil yo'l bilan bir xil "
                    "chiqadi: geometrik formuladan, Vinkler "
                    "analogiyasi (k/4D)^(1/4) dan (farq "
                    "0,00 %) va yechim cho'qqilarining "
                    "logarifmiga to'g'ri chiziq "
                    "moslashtirishdan (5,2473, farq "
                    "0,007 %). σ_θ = 32,70 MPa, "
                    "M₀ = −1425 N·m/m (ikki yo'l bilan "
                    "0,00 % farq; ishora manfiy — "
                    "mahkamlash devorni ichkariga egadi), "
                    "σ_b = 59,37 MPa, nisbat 1,81568 — "
                    "jadvalda beshta turli geometriya va "
                    "bosimda nisbat o'zgarmaydi (0,00 % "
                    "og'ish). Chekka zonasi ln(100)/β = "
                    "0,878 m = 3,58√(Rh), balandlikning "
                    "11,0 % i; birinchi nol π/β = 0,599 m "
                    "= 2,444√(Rh). bc = 1 (sharnirli) da "
                    "M₀ = 0 — mahalliy egish butunlay yo'q."
                ),
            ),
            visual=vis(
                kind="Chekka effektining so'nuvchi to'lqini",
                tool="React/SVG + Manim",
                description=(
                    "Radial ko'chish, egish momenti va "
                    "chekka zonasining qobiq uzunligiga "
                    "nisbati."
                ),
                how_to_draw=(
                    "React/SVG: yuqori panelda rezervuar "
                    "devorining vertikal kesimi chiziladi "
                    "(tubi pastda, mahkamlangan). Uning "
                    "yoniga radial ko'chish $w(x)$ "
                    "**kuchaytirilgan masshtabda** "
                    "chiziladi: membrana qiymati "
                    "$w_m$ tik punktir chiziq, haqiqiy "
                    "yechim esa tubdan boshlab nolga "
                    "tushadi va so'nuvchi tebranish bilan "
                    "$w_m$ ga qaytadi. Eksponensial "
                    "o'rama $\\pm e^{-\\beta x}$ ingichka "
                    "kulrang chiziq bilan ustiga qo'yiladi "
                    "— so'nish ko'z bilan o'qiladi. "
                    "$\\sqrt{Rh}$, $\\pi/\\beta$ va "
                    "$\\ln(100)/\\beta$ masofalari devor "
                    "yonida o'lchov chiziqlari bilan "
                    "belgilanadi, shunda chekka zonasi "
                    "butun balandlikning qanchalik kichik "
                    "qismi ekani darhol ko'rinadi. Pastki "
                    "panelda moment epyurasi $M(x)$ "
                    "shtrixlangan holda; chekkadagi "
                    "$M_0$ qiymati yoziladi. O'ngda "
                    "kichik jadval — nisbatning beshta "
                    "geometriyada o'zgarmasligi."
                ),
            ),
            interp=(
                "Eng ishonchli natija — $\\beta$ ning "
                "uchta butunlay mustaqil yo'l bilan bir xil "
                "chiqishi: geometrik formuladan "
                "$[3(1-\\nu^2)]^{1/4}/\\sqrt{Rh}$, elastik "
                "asos analogiyasidan $(k/4D)^{1/4}$ va "
                "yechimning o'zidan — so'nuvchi to'lqin "
                "cho'qqilarining logarifmiga to'g'ri chiziq "
                "moslashtirib ($0{,}007$ % farq bilan). "
                "Uchinchisi ayniqsa qimmatli: u "
                "$\\beta$ ni formuladan emas, "
                "**hisoblangan yechimdan** o'lchaydi va "
                "so'nish haqiqatan ham $e^{-\\beta x}$ "
                "qonuni bo'yicha borishini ko'rsatadi. "
                "Bu 4-qadamdagi asosiy da'voni — qobiq "
                "o'ziga o'zi Vinkler asosi bo'lishini — "
                "sonli tasdiqlaydi. Ikkinchi muhim natija "
                "jadvalda: beshta turli radius, qalinlik va "
                "bosimda $\\sigma_b/\\sigma_\\theta$ nisbati "
                "o'zgarmaydi. Bu shunchaki qiziq fakt emas, "
                "balki loyihalash uchun jiddiy xulosa: "
                "mahkamlangan chekkadagi mahalliy "
                "kuchlanishni **devorni qalinlashtirish "
                "bilan kamaytirib bo'lmaydi**. Ikkala "
                "kuchlanish ham $1/h$ ga mutanosib "
                "kamayadi va nisbat saqlanadi. Yagona "
                "samarali yo'l — chegaraviy shartni "
                "o'zgartirish; kodda $bc = 1$ (sharnirli) "
                "ni tanlab buni tekshirish mumkin: u yerda "
                "$M_0 = 0$ va mahalliy egish butunlay "
                "yo'qoladi. Nihoyat, $\\pi/\\beta$ va "
                "$2{,}44\\sqrt{Rh}$ butun qalinlik "
                "oralig'ida deyarli ustma-ust tushadi — "
                "$\\sqrt{Rh}$ ning qobiq mexanikasidagi "
                "tabiiy uzunlik birligi ekani shundan "
                "ko'rinadi."
            ),
            mistakes=[
                "Chekka effektini butun qobiqqa tarqalgan "
                "deb hisoblash. U $\\sqrt{Rh}$ masshtabida "
                "so'nadi — odatda qobiq uzunligining bir "
                "necha foizi.",
                "Mahalliy kuchlanishni devorni "
                "qalinlashtirish bilan kamaytirishga "
                "urinish. Nisbat $\\sqrt{3/(1-\\nu^2)}$ "
                "o'zgarmaydi; chegaraviy shartni "
                "o'zgartirish kerak.",
                "$\\beta$ ni materialga bog'liq deb "
                "o'ylash. $E$ formulada qisqaradi — "
                "$\\beta$ faqat $R$, $h$ va $\\nu$ ga "
                "bog'liq.",
                "Qisqa qobiqda ($\\beta L < \\pi$) "
                "o'suvchi eksponentalarni tashlab yuborish. "
                "Bunda ikkala chekka o'zaro ta'sirlashadi.",
                "Membrana yechimini bekor qilish. Chekka "
                "effekti unga **qo'shiladi**, o'rnini "
                "bosmaydi.",
            ],
            quiz=[
                q("Nima uchun silindrik qobiq elastik "
                  "asosdagi balkaga o'xshaydi?",
                  "Radial ko'chish $w$ aylana kuchi "
                  "$N_\\theta = Ehw/R$ ni uyg'otadi va u "
                  "normal yo'nalishda $Ehw/R^2$ qaytaruvchi "
                  "kuch beradi — bu Vinkler asosi "
                  "$k = Eh/R^2$ ning o'zi.", "konseptual"),
                q("$\\beta$ nima uchun materialga bog'liq "
                  "emas?",
                  "$\\beta^4 = k/(4D) = Eh/(4R^2D)$ da "
                  "$D \\propto Eh^3$, demak $E$ qisqaradi va "
                  "$\\beta^4 = 3(1-\\nu^2)/(R^2h^2)$ qoladi.",
                  "konseptual"),
                q("$R = 2$ m, $h = 8$ mm silindrda "
                  "$\\sqrt{Rh}$ va $\\beta$ nechaga teng "
                  "($\\nu = 0{,}3$)?",
                  "$\\sqrt{Rh} = \\sqrt{0{,}016} = 0{,}1265$ m; "
                  "$\\beta = 1{,}285/0{,}1265 = 10{,}16$ m⁻¹.",
                  "hisob"),
                q("Kodda $\\beta$ nima uchun ikki xil yo'l "
                  "bilan hisoblanadi?",
                  "Geometrik formula va Vinkler analogiyasi "
                  "$(k/4D)^{1/4}$ mustaqil yo'llar; ularning "
                  "mos kelishi elastik asos analogiyasini "
                  "tasdiqlaydi.", "kod"),
                q("Mahkamlangan rezervuar tubida mahalliy "
                  "kuchlanishni qanday kamaytirish mumkin?",
                  "Devorni qalinlashtirish yordam bermaydi "
                  "(nisbat o'zgarmaydi). Chegaraviy shartni "
                  "yumshatish kerak: sharnirli ulanish yoki "
                  "egiluvchan tugun — unda $M_0 = 0$.",
                  "talqin"),
                q("Qobiq 'uzun' deb qachon hisoblanadi va "
                  "bu nima uchun muhim?",
                  "$\\beta L > \\pi$ bo'lganda. Shundagina "
                  "chekkalar mustaqil va o'suvchi "
                  "eksponentalarni tashlash mumkin; aks "
                  "holda 4×4 tizim yechiladi.", "talqin"),
            ],
            bridge=(
                "Silindrik qobiq uchun chekka effekti "
                "to'liq yechildi. Endi uni pq-26 da ochiq "
                "qolgan masalaga qo'llaymiz: silindr va "
                "sfera tutashuvidagi mos kelmaslikni ikki "
                "tomondan kelgan chekka yechimlari bilan "
                "bartaraf etamiz va sferik hamda konus "
                "qobiqlarga o'tamiz."
            ),
            research=(
                "Qisqa qobiqlar nazariyasini o'rganing. "
                "(1) $\\beta L < \\pi$ bo'lganda ikkala "
                "chekka yechimini birga hisobga olib, "
                "to'rtta konstanta uchun 4×4 tizimni "
                "yozing va yeching. (2) $\\beta L$ ning "
                "qaysi qiymatidan boshlab chekkalar "
                "o'zaro ta'siri 1 % dan kam bo'lishini "
                "sonli aniqlang va bu 'uzun qobiq' "
                "mezonini adabiyotdagi $\\beta L > \\pi$ "
                "va $\\beta L > 4$ tavsiyalari bilan "
                "solishtiring. (3) Qalinligi o'zgaruvchan "
                "silindrik qobiq uchun tenglamani yozing "
                "va uni sonli yeching — rezervuarlarda "
                "devor pastdan yuqoriga ingichkalashadi."
            ),
            manim_ref=manim(
                scene="EdgeEffectScene",
                module="animatsiya/scenes/pq_shells.py",
                title="Chekka effekti va so'nish masshtabi",
                summary=(
                    "Rezervuar devori bosim ostida "
                    "kengayadi; tubi mahkamlangani uchun "
                    "u yerda kengayish nolga majburlanadi "
                    "va so'nuvchi to'lqin hosil bo'ladi. "
                    "$\\sqrt{Rh}$ masofasi o'lchov chizig'i "
                    "bilan ko'rsatiladi va qalinlik "
                    "o'zgarganda u qanday o'zgarishi "
                    "namoyish etiladi."
                ),
            ),
        ),
    ),

    # ------------------------------------------------------------------ pq-28
    Topic(
        id="pq-28",
        subject_id=S, module_id=M, order=28,
        title="Sferik va konus qobiqlar; tutashuv tugunlari va mos kelmaslik",
        description=(
            "Geckeler taqribiy usuli, sferik qobiqning chekka effekti, "
            "silindr–sfera va silindr–konus tutashuvlari, mos kelmaslikni "
            "kuch va moment bilan yechish, halqa mustahkamlagichlar."
        ),
        learning_objective=(
            "Ikki qobiq tutashuvidagi mos kelmaslikni ikki noma'lumli "
            "tizim sifatida qo'yish va yechish, tutashuvdagi mahalliy "
            "kuchlanishni hisoblash va mustahkamlagich halqani tanlash."
        ),
        prerequisites=["pq-27", "pq-26"],
        mathematical_core=(
            "Moslik shartlari $\\delta_1 + \\delta_{11}X_1 + "
            "\\delta_{12}X_2 = \\delta_2 + \\ldots$, sferik qobiq uchun "
            "$\\beta_s = \\sqrt[4]{3(1-\\nu^2)}\\,\\sqrt{R/h}\\,/R$."
        ),
        engineering_application=(
            "Bosim idishlari tublari, quvur o'tishlari, silos konuslari, "
            "raketa baklari, reaktor korpuslari, flanets ulanishlari."
        ),
        computational_component=(
            "2×2 moslik tizimini yechish, tutashuvdagi $M_0$ va $Q_0$ ni "
            "topish, mustahkamlagich halqaning ta'sirini baholash."
        ),
        visualization_component=(
            "Tutashuvdan oldingi va keyingi ko'chish epyuralari, "
            "ikki tomonga tarqalgan bezovtalik, kuchlanish cho'qqisi."
        ),
        research_extension=(
            "Torsimon o'tish (knuckle) geometriyasini o'rganing: "
            "nima uchun ASME standartlari tub shakli uchun "
            "torisferik yoki ellipsoid profilni talab qiladi va "
            "u mos kelmaslikni qanday kamaytiradi?"
        ),
        difficulty="ilg'or",
        previous_link=(
            "pq-27 da bitta silindrik qobiqning chekka effekti "
            "yechildi va $\\beta$, $\\sqrt{Rh}$ apparati qurildi. "
            "Endi shu apparatni **ikkita** qobiq tutashgan joyga "
            "qo'llaymiz va pq-26 da ochiq qolgan 2,43 barobarlik "
            "mos kelmaslikni nihoyat yopamiz."
        ),
        next_topic="pq-29",
        estimated_minutes=95,
        tags=["sferik qobiq", "tutashuv", "Geckeler", "mos kelmaslik"],
        lesson=_lesson(
            problem=(
                "pq-26 da 15 MPa li ballon loyihalandi va "
                "oxirida ochiq savol qoldi: silindr "
                "0,1457 mm, sferik tub esa 0,0600 mm "
                "kengayadi — 2,43 marta farq. Ular bitta "
                "chokda payvandlangan, demak ular **bir xil "
                "radiusga** kelishi shart. Tabiat bu "
                "kelishuvni mahalliy kuch $Q_0$ va moment "
                "$M_0$ orqali majbur qiladi. Ular qanchalik "
                "katta? Ballon devori 8,6 mm — mahalliy "
                "kuchlanish ruxsat etilgan 250 MPa dan "
                "oshib ketmaydimi? Bu savol bosim "
                "idishlarini loyihalashda hal qiluvchi, "
                "chunki buzilish deyarli har doim aynan "
                "tutashuvdan boshlanadi."
            ),
            concepts=[
                c("Mos kelmaslik (incompatibility)",
                  "Ikki qobiqning membrana yechimlari "
                  "tutashuv chizig'ida turli ko'chish va "
                  "burilish berishi; konstruksiya buni "
                  "qabul qila olmaydi."),
                c("Tutashuvdagi ortiqcha noma'lumlar",
                  "$X_1 = Q_0$ (radial kesuvchi kuch) va "
                  "$X_2 = M_0$ (egish momenti) — ular "
                  "moslikni ta'minlaydi; kuchlar usuli "
                  "(mq-27) ning qobiqqa ko'chirilishi."),
                c("Geckeler taqribiy usuli",
                  "Sferik qobiqning chekka effektini "
                  "silindrik qobiq formulalari bilan "
                  "almashtirish; $R_s\\varphi \\gg \\sqrt{R_sh}$ "
                  "bo'lganda xatosi bir necha foizdan kam."),
                c("Sferik qobiq uchun $\\beta$",
                  "$\\beta_s = [3(1-\\nu^2)]^{1/4}/\\sqrt{R_sh}$ — "
                  "silindrdagi bilan **bir xil ko'rinishda**, "
                  "chunki Geckeler taqribida sfera mahalliy "
                  "ravishda silindr kabi ishlaydi."),
                c("Moslik tenglamalari",
                  "Tutashuvda ikkita shart: radial ko'chishlar "
                  "va burilishlar teng bo'lsin. Ikkita shart, "
                  "ikkita noma'lum."),
                c("Mustahkamlagich halqa",
                  "Tutashuvga qo'yilgan halqa radial kuchni "
                  "o'ziga oladi va qobiqdagi mahalliy "
                  "momentni kamaytiradi."),
            ],
            derivation=[
                d("1. Sferik qobiqning chekka tenglamasi",
                  r"\frac{d^4 w}{ds^4} + \frac{Eh}{R_s^2 D}\,w "
                  r"\approx \frac{p}{D}",
                  "Geckeler taqribi: chekka yaqinida "
                  "$w$ ning yuqori hosilalari past "
                  "hosilalaridan ancha katta, shuning uchun "
                  "past hadlarni tashlaymiz. Natijada "
                  "silindr tenglamasining o'zi hosil bo'ladi."),
                d("2. Sferik $\\beta$",
                  r"\beta_s = \sqrt[4]{\frac{3(1-\nu^2)}{R_s^2h^2}} "
                  r"= \frac{1{,}285}{\sqrt{R_sh}}",
                  "Ko'rinishi silindrdagi bilan bir xil. "
                  "Demak pq-27 dagi butun apparat "
                  "(so'nuvchi yechim, $\\sqrt{Rh}$ masshtabi) "
                  "sferaga ham tegishli."),
                d("3. Birlik ta'sirlar: silindr tomoni",
                  r"\delta^{cyl}_{Q} = \frac{1}{2\beta_c^3 D_c}, "
                  r"\quad \delta^{cyl}_{M} = -\frac{1}{2\beta_c^2 D_c}",
                  "Birlik radial kuch $Q_0 = 1$ chekkani "
                  "shuncha siljitadi; birlik moment "
                  "$M_0 = 1$ esa shuncha. Bular pq-27 dagi "
                  "yechimdan bevosita kelib chiqadi."),
                d("4. Birlik ta'sirlar: burilish",
                  r"\theta^{cyl}_{Q} = -\frac{1}{2\beta_c^2D_c}, "
                  r"\quad \theta^{cyl}_{M} = \frac{1}{\beta_c D_c}",
                  "$\\delta_M = \\theta_Q$ — Maksvell–Betti "
                  "o'zarolik teoremasi (nm-24, mq-26) "
                  "qobiqda ham o'rinli va u hisobning "
                  "tekshiruvi bo'lib xizmat qiladi."),
                d("5. Moslik sharti: ko'chishlar",
                  r"w^{cyl}_m + \delta^{cyl}_Q Q_0 + "
                  r"\delta^{cyl}_M M_0 = w^{sph}_m - "
                  r"\delta^{sph}_Q Q_0 + \delta^{sph}_M M_0",
                  "Chap tomon — silindr chekkasi, o'ng "
                  "tomon — sfera chekkasi. $Q_0$ ikki "
                  "qobiqqa **qarama-qarshi** yo'nalishda "
                  "ta'sir qiladi (ta'sir va aks ta'sir)."),
                d("6. Moslik sharti: burilishlar",
                  r"\theta^{cyl}_Q Q_0 + \theta^{cyl}_M M_0 = "
                  r"-\theta^{sph}_Q Q_0 + \theta^{sph}_M M_0",
                  "Membrana yechimida burilish yo'q "
                  "(o'qsimmetrik, doimiy kengayish), "
                  "shuning uchun faqat chekka hadlari qoladi."),
                d("7. Bir xil qalinlik va radiusda "
                  "soddalashtirish",
                  r"R_c = R_s = R, \ h_c = h_s = h "
                  r"\;\Longrightarrow\; \beta_c = \beta_s = \beta",
                  "Bu holda ikkala qobiqning birlik "
                  "ta'sirlari bir xil bo'ladi va tizim "
                  "juda soddalashadi."),
                d("8. Yechim: moment nolga aylanadi",
                  r"M_0 = 0, \qquad Q_0 = "
                  r"\frac{\Delta w}{2\delta_Q} = "
                  r"\frac{\beta^3 D\,\Delta w}{1} \cdot "
                  r"\frac{1}{2} \cdot 2 = \beta^3 D\,\Delta w",
                  "**Ajoyib natija.** Burilish tenglamasi "
                  "simmetriya tufayli $M_0 = 0$ beradi: "
                  "ikkala qobiq bir xil bikrlikka ega "
                  "bo'lgani uchun ular momentsiz, faqat "
                  "kesuvchi kuch bilan kelishadi."),
                d("9. Tutashuvdagi maksimal moment",
                  r"M(x) = \frac{Q_0}{\beta}e^{-\beta x}\sin\beta x "
                  r"\;\Rightarrow\; M_{max} = \frac{Q_0}{\beta}"
                  r"e^{-\pi/4}\sin\frac{\pi}{4} = "
                  r"0{,}32240\,\frac{Q_0}{\beta}",
                  "Chekkada $M = 0$, lekin ichkarida "
                  "$\\beta x = \\pi/4$ da maksimumga "
                  "chiqadi. Mahalliy egish kuchlanishi "
                  "shundan hisoblanadi."),
                d("10. Mahalliy kuchlanish",
                  r"\sigma_b = \frac{6M_{max}}{h^2}, \qquad "
                  r"\sigma_{tot} = \sigma_\theta^{mem} + "
                  r"\sigma_b",
                  "Mahalliy egish membrana kuchlanishiga "
                  "qo'shiladi. Bu yig'indi standartlarda "
                  "'mahalliy membrana + egish' kategoriyasi "
                  "sifatida alohida tekshiriladi."),
            ],
            meaning=(
                "Bu mavzu qobiq nazariyasining ikkita "
                "yarmini — membrana va egish — bitta "
                "hisobga birlashtiradi va shu bilan "
                "nazariyani yopadi. Ishlash sxemasi "
                "universal: avval har bir qobiq uchun "
                "membrana yechimi olinadi (pq-26), keyin "
                "ularning tutashuvdagi mos kelmasligi "
                "o'lchanadi, so'ngra bu mos kelmaslikni "
                "nolga keltiruvchi $Q_0$ va $M_0$ "
                "topiladi (pq-27 dagi chekka yechimlari "
                "orqali), va nihoyat mahalliy kuchlanish "
                "hisoblanadi. Bu aynan sterjen tizimlaridagi "
                "kuchlar usuli (mq-27) ning qobiqqa "
                "ko'chirilgan shakli — ortiqcha noma'lumlar "
                "moslik shartlaridan topiladi. 8-qadamdagi "
                "natija ayniqsa nafis: agar silindr va "
                "sfera bir xil radius va qalinlikka ega "
                "bo'lsa, tutashuvda **moment umuman paydo "
                "bo'lmaydi** — faqat kesuvchi kuch. Sababi "
                "simmetriya: ikkala qobiqning bikrliklari "
                "bir xil, shuning uchun ular burilish "
                "bo'yicha o'z-o'zidan kelishadi. Lekin bu "
                "moment yo'q degani emas — chekkadan "
                "$\\beta x = \\pi/4$ masofada (ya'ni "
                "$0{,}61\\sqrt{Rh}$ da) $M$ maksimumga "
                "chiqadi. Amalda esa qalinliklar har xil "
                "bo'ladi (pq-26 da tub ikki barobar yupqa "
                "chiqqan edi) va shunda $M_0 \\ne 0$. "
                "Aynan shuning uchun standartlar "
                "tutashuvni alohida tekshirishni talab "
                "qiladi va ko'pincha torsimon o'tish "
                "(knuckle) yoki mustahkamlagich halqa "
                "qo'yishni buyuradi: ular mos kelmaslikni "
                "kamaytiradi yoki uni o'ziga oladi."
            ),
            equations=[
                eq(r"\beta_s = \frac{\sqrt[4]{3(1-\nu^2)}}"
                   r"{\sqrt{R_sh}}",
                   "Sferik qobiq uchun so'nish parametri "
                   "(Geckeler taqribi).", "Sferik beta"),
                eq(r"\delta_Q = \frac{1}{2\beta^3D}, \quad "
                   r"\delta_M = \theta_Q = -\frac{1}{2\beta^2D}, "
                   r"\quad \theta_M = \frac{1}{\beta D}",
                   "Chekkadagi birlik ta'sirlar; "
                   "$\\delta_M = \\theta_Q$ — Maksvell–Betti "
                   "o'zaroligi.", "Birlik ta'sirlar"),
                eq(r"\Delta w = w^{cyl}_m - w^{sph}_m = "
                   r"\frac{pR^2}{2Eh}",
                   "Bir xil qalinlikda silindr va sfera "
                   "membrana kengayishlarining farqi.",
                   "Mos kelmaslik"),
                eq(r"Q_0 = \beta^3 D\,\Delta w = "
                   r"\frac{p}{8\beta}",
                   "Tutashuvdagi radial kesuvchi kuch "
                   "(bir xil $R$ va $h$ uchun).",
                   "Tutashuv kuchi"),
            ],
            conditions=(
                "**Tutashuvdagi moslik shartlari** "
                "(o'qsimmetrik holat):\n"
                "1. Radial ko'chishlar tengligi: "
                "$w^{(1)}(0) = w^{(2)}(0)$;\n"
                "2. Meridian burilishlari tengligi: "
                "$\\theta^{(1)}(0) = \\theta^{(2)}(0)$.\n\n"
                "**Muvozanat shartlari** (avtomatik "
                "bajariladi): $Q_0$ va $M_0$ ikkala "
                "qobiqqa teng va qarama-qarshi ta'sir "
                "qiladi.\n\n"
                "**Geckeler taqribining qo'llanish "
                "sohasi:** $R_s\\varphi_0 > 2\\sqrt{R_sh}$, "
                "ya'ni tutashuv sferaning qutbidan "
                "yetarlicha uzoqda bo'lsin; aks holda "
                "aniq yechim (Legendre funksiyalari yoki "
                "gipergeometrik qator) kerak.\n\n"
                "**Uzoqda:** ikkala qobiqda ham "
                "$w \\to w_m$ (mos membrana qiymati).\n\n"
                "**Qalinlik sakrashi:** $h_1 \\ne h_2$ "
                "bo'lsa tizim to'liq 2×2 ko'rinishda "
                "yechiladi va $M_0 \\ne 0$."
            ),
            worked=WorkedExample(
                statement=(
                    "pq-26 dagi ballon: $p = 15$ MPa, "
                    "$R = 144$ mm, silindr $h = 8{,}638$ mm, "
                    "sferik tub $h = 8{,}638$ mm (bir xil "
                    "qilingan), $E = 210$ GPa, $\\nu = 0{,}3$. "
                    "Tutashuvdagi $Q_0$, $M_0$, $M_{max}$ va "
                    "mahalliy kuchlanishni toping."
                ),
                given=[
                    r"p = 15\ \text{MPa},\ R = 0{,}144\ \text{m},\ "
                    r"h = 0{,}008638\ \text{m}",
                    r"E = 210\ \text{GPa},\ \nu = 0{,}3",
                ],
                steps=[
                    st(r"\sqrt{Rh} = \sqrt{0{,}144 \cdot 0{,}008638} "
                       r"= \sqrt{1{,}2439\times10^{-3}} = "
                       r"0{,}035269\ \text{m}",
                       "Tabiiy uzunlik masshtabi — atigi 35 mm."),
                    st(r"\beta = \frac{1{,}28541}{0{,}035269} = "
                       r"36{,}446\ \text{m}^{-1}",
                       "Ikkala qobiq uchun bir xil "
                       "($R$ va $h$ bir xil)."),
                    st(r"D = \frac{210\times10^{9} \cdot "
                       r"6{,}4446\times10^{-7}}{12 \cdot 0{,}91} "
                       r"= 12\,393\ \text{N·m}",
                       "$h^3 = 6{,}4446\\times10^{-7}$ m³."),
                    st(r"\Delta w = \frac{pR^2}{2Eh} = "
                       r"\frac{15\times10^{6} \cdot 0{,}020736}"
                       r"{2 \cdot 210\times10^{9} \cdot 0{,}008638} "
                       r"= 8{,}571\times10^{-5}\ \text{m}",
                       "Mos kelmaslik — 0,0857 mm. "
                       "pq-26 dagi farq (0,0857 mm) bilan "
                       "aynan mos tushadi."),
                    st(r"M_0 = 0",
                       "Bir xil $R$, $h$ va shuning uchun "
                       "bir xil $\\beta$: burilish tenglamasi "
                       "simmetriya tufayli momentni nolga "
                       "aylantiradi."),
                    st(r"Q_0 = \frac{p}{8\beta} = "
                       r"\frac{15\times10^{6}}{8 \cdot 36{,}446} "
                       r"= 51\,446\ \text{N/m}",
                       "Radial kesuvchi kuch — 51,4 kN/m. "
                       "Ekvivalent: $\\beta^3D\\Delta w$ "
                       "ham shu qiymatni beradi."),
                    st(r"M(x) = \frac{Q_0}{\beta}e^{-\beta x}"
                       r"\sin\beta x \;\Rightarrow\; "
                       r"M_{max} = \frac{Q_0}{\beta}e^{-\pi/4}"
                       r"\sin\frac{\pi}{4} = 0{,}32240\,"
                       r"\frac{Q_0}{\beta}",
                       "$M_0 = 0$ bo'lgani uchun moment "
                       "chekkada nol; maksimum "
                       "$\\beta x = \\pi/4$ da."),
                    st(r"M_{max} = 0{,}32240 \cdot "
                       r"\frac{51\,446}{36{,}446} = "
                       r"0{,}32240 \cdot 1411{,}6 = "
                       r"455{,}1\ \text{N·m/m}",
                       "Maksimum $x = \\pi/(4\\beta) = "
                       "21{,}6$ mm da — chekkadan "
                       "$0{,}61\\sqrt{Rh}$ ichkarida."),
                    st(r"\sigma_b = \frac{6 \cdot 455{,}1}"
                       r"{(0{,}008638)^2} = \frac{2730{,}6}"
                       r"{7{,}4615\times10^{-5}} = "
                       r"36{,}59\ \text{MPa}",
                       "Mahalliy egish kuchlanishi."),
                    st(r"\sigma_\theta^{mem} = \frac{pR}{h} = "
                       r"\frac{15 \cdot 0{,}144}{0{,}008638} "
                       r"= 250{,}1\ \text{MPa}",
                       "Silindrdagi membrana kuchlanishi — "
                       "loyihalash bo'yicha aynan "
                       "$[\\sigma]$ ga teng."),
                    st(r"\sigma_{tot} = 250{,}1 + 36{,}6 = "
                       r"286{,}7\ \text{MPa} > 250\ \text{MPa}",
                       "**Ruxsat etilgan qiymatdan 14,7 % "
                       "oshdi.** Membrana hisobi yetarli "
                       "emas ekan — tutashuv alohida "
                       "tekshirilishi shart."),
                ],
                answer=(
                    "$\\beta = 36{,}446$ m⁻¹, "
                    "$\\Delta w = 0{,}08573$ mm, "
                    "$M_0 = 0$, $Q_0 = 51{,}446$ kN/m "
                    "($= p/8\\beta$), "
                    "$M_{max} = 455{,}1$ N·m/m "
                    "($x = 21{,}6$ mm da), "
                    "$\\sigma_b = 36{,}59$ MPa. Umumiy "
                    "kuchlanish $286{,}7$ MPa — ruxsat "
                    "etilgan 250 MPa dan **14,7 % ortiq**. "
                    "Faqat membrana hisobiga tayangan "
                    "loyiha tutashuvda yetarli emas."
                ),
                engineering_note=(
                    "Bu natija pq-26 dagi loyihani bevosita "
                    "tuzatadi: u yerda qalinlik faqat "
                    "membrana kuchlanishiga qarab tanlangan "
                    "edi va $\\sigma_\\theta$ aynan "
                    "$[\\sigma]$ ga teng chiqqan edi — "
                    "hech qanday zaxirasiz. Tutashuvdagi "
                    "36,6 MPa esa bu zaxirani talab qiladi. "
                    "Amalda uch yo'l bor: (1) tutashuv "
                    "zonasida devorni qalinlashtirish — "
                    "lekin pq-27 dagi kabi bu ham "
                    "membranani ham egishni kamaytiradi, "
                    "shuning uchun samarali; (2) torsimon "
                    "o'tish (knuckle) qo'yish — "
                    "$R_1$ ning silliq o'zgarishi mos "
                    "kelmaslikni keskin kamaytiradi; "
                    "(3) mustahkamlagich halqa. "
                    "ASME VIII standartida aynan shu "
                    "sabab bo'yicha tekis tub taqiqlangan "
                    "va torisferik yoki ellipsoid tub "
                    "talab qilinadi — ularda $R_1$ "
                    "sakramaydi."
                ),
            ),
            computation=Computation(
                caption=(
                    "Tutashuvdagi moslik tizimini yechish, "
                    "$Q_0$ va $M_0$ ni topish va mahalliy "
                    "kuchlanishni baholash."
                ),
                code='''"""Qobiq tutashuvi: mos kelmaslik va moslik tizimi."""
import numpy as np
from labkit import PARAMS, note, series, table, value

p0 = float(PARAMS.get("p", 15.0))*1e6
R = float(PARAMS.get("R", 144.0))/1000.0
h1 = float(PARAMS.get("h1", 8.638))/1000.0    # silindr
h2 = float(PARAMS.get("h2", 8.638))/1000.0    # sferik tub
E = float(PARAMS.get("E", 210.0))*1e9
nu = float(PARAMS.get("nu", 0.3))
sig_all = float(PARAMS.get("sig_all", 250.0))*1e6

cf = (3*(1 - nu**2))**0.25

def shell(hh):
    D = E*hh**3/(12*(1 - nu**2))
    beta = cf/np.sqrt(R*hh)
    return D, beta

D1, b1 = shell(h1)
D2, b2 = shell(h2)
value("Silindr: beta", b1, "1/m")
value("Sfera: beta", b2, "1/m")
value("Silindr: D", D1, "N*m")
value("Sfera: D", D2, "N*m")
value("sqrt(R*h1)", np.sqrt(R*h1), "m")

# --- Membrana ko'chishlari (radial) ---
w1 = p0*R**2/(E*h1)*(1 - nu/2)      # silindr
w2 = p0*R**2/(2*E*h2)*(1 - nu)      # sfera
dw = w1 - w2
value("Silindr membrana kengayishi", w1*1000, "mm")
value("Sfera membrana kengayishi", w2*1000, "mm")
value("Mos kelmaslik delta_w", dw*1000, "mm")
note(f"Membrana yechimlari tutashuvda {w1*1000:.5f} mm va "
     f"{w2*1000:.5f} mm beradi - farq {dw*1000:.5f} mm. "
     f"Konstruksiya uzluksiz bo'lgani uchun bu farq Q0 va M0 "
     f"bilan yopilishi SHART.")

# --- Birlik ta'sir koeffitsientlari (pq-27 chekka yechimidan) ---
# Yarim cheksiz qobiq, lokal koordinata ksi qobiq ICHIGA yo'nalgan,
# w tashqariga musbat, theta = dw/d(ksi):
#   w(0)     =  F/(2*D*b^3) - M/(2*D*b^2)
#   theta(0) = -F/(2*D*b^2) + M/(D*b)
# Bu yerda F - chekkadagi TASHQARIGA yo'nalgan radial kuch.
def infl(D, b):
    return (1/(2*D*b**3), -1/(2*D*b**2),      # w:     F dan, M dan
            -1/(2*D*b**2), 1/(D*b))           # theta: F dan, M dan

fF1, fM1, mF1, mM1 = infl(D1, b1)
fF2, fM2, mF2, mM2 = infl(D2, b2)

value("Maksvell-Betti tekshiruvi (silindr)",
      abs(fM1 - mF1)/abs(mF1)*100, "%")
note(f"Birlik moment berganda ko'chish ({fM1:.6e} m/(N*m/m)) va "
     f"birlik kuch berganda burilish ({mF1:.6e} rad/(N/m)) aynan "
     f"teng - Maksvell-Betti o'zarolik teoremasi bajarilgan, "
     f"demak birlik ta'sirlar to'g'ri hisoblangan.")

# --- Moslik tizimi ---
# X - sferaning silindrga ta'sir qiluvchi radial kuchi, ICHKARIGA
#     musbat (demak silindr chekkasida F = -X, sfera chekkasida F = +X).
# M - tutashuv momenti; ikkita lokal koordinata o'zaro ko'zgu bo'lgani
#     uchun u ikkala qobiqda ham bir xil ishora bilan yoziladi.
# (1) Radial ko'chishlar tengligi
# (2) Burilishlar uzluksizligi: theta_1 = -theta_2 (koordinatalar
#     qarama-qarshi yo'nalgan)
A = np.array([[-(fF1 + fF2), fM1 - fM2],
              [mF2 - mF1, mM1 + mM2]])
rhs = np.array([w2 - w1, 0.0])
Q0, M0 = np.linalg.solve(A, rhs)
value("Tutashuv kuchi Q0", Q0/1000, "kN/m")
value("Tutashuv momenti M0", M0, "N*m/m")

# Yechimni moslik shartlariga qaytarib qo'yib tekshirish
w1_e = w1 + fF1*(-Q0) + fM1*M0
w2_e = w2 + fF2*(+Q0) + fM2*M0
t1_e = mF1*(-Q0) + mM1*M0
t2_e = mF2*(+Q0) + mM2*M0
res_w = w1_e - w2_e
res_t = t1_e + t2_e
value("Ko'chish moslik qoldig'i", abs(res_w)/max(abs(dw), 1e-30)*100, "%")
value("Tutashuvdagi umumiy radius", w1_e*1000, "mm")
note(f"Topilgan Q0 va M0 ni moslik shartlariga qaytarib qo'yganda "
     f"ko'chish qoldig'i {abs(res_w)/max(abs(dw),1e-30):.2e} % va "
     f"burilish qoldig'i {abs(res_t):.2e} rad - ikkala qobiq chekkasi "
     f"endi bir xil radiusga ({w1_e*1000:.5f} mm) va mos burilishga "
     f"ega. Boshlang'ich {w1*1000:.5f} va {w2*1000:.5f} mm "
     f"qiymatlari o'rtasida joylashgani mantiqan to'g'ri.")

if abs(h1 - h2) < 1e-12:
    Q0_th = p0/(8*b1)
    value("Q0 (analitik p/(8*beta))", Q0_th/1000, "kN/m")
    value("Q0 nisbiy xatosi", abs(Q0 - Q0_th)/abs(Q0_th)*100, "%")
    note(f"Qalinliklar teng bo'lgani uchun M0 = {M0:.3e} N*m/m ~ 0 "
         f"va Q0 analitik p/(8*beta) = {Q0_th/1000:.3f} kN/m bilan "
         f"{abs(Q0-Q0_th)/abs(Q0_th):.2e} % farq qiladi. Simmetriya "
         f"tufayli qobiqlar MOMENTSIZ kelishadi.")
else:
    note(f"Qalinliklar har xil (h1 = {h1*1000:.2f}, h2 = "
         f"{h2*1000:.2f} mm), shuning uchun M0 = {M0:.1f} N*m/m "
         f"nolga teng emas - assimetriya moment tug'diradi.")

# --- Moment taqsimoti silindr tomonida ---
# w = e^(-b x)*(C1*cos + C2*sin),  C2 = M/(2*D*b^2),
# C1 = F/(2*D*b^3) - M/(2*D*b^2),  bu yerda F = -Q0.
# M(x) = -D*w'' = 2*D*b^2*e^(-b x)*(C2*cos - C1*sin)
x = np.linspace(0, 6/b1, 800)
bx = b1*x
ex, cx, sx = np.exp(-bx), np.cos(bx), np.sin(bx)
C2 = M0/(2*D1*b1**2)
C1 = (-Q0)/(2*D1*b1**3) - M0/(2*D1*b1**2)
M_x = 2*D1*b1**2*ex*(C2*cx - C1*sx)
value("M(0) tekshiruvi (M0 ga teng bo'lishi kerak)", float(M_x[0]),
      "N*m/m")
series("Egish momenti M(x), silindr tomoni", x.tolist(),
       M_x.tolist(), xlabel="tutashuvdan masofa x, m",
       ylabel="M, N*m/m")
i_max = int(np.argmax(np.abs(M_x)))
Mmax = float(M_x[i_max])
value("Maksimal moment M_max", Mmax, "N*m/m")
value("M_max joylashgan masofa", float(x[i_max]), "m")
value("M_max joyi: beta*x", float(bx[i_max]), "—")

if abs(M0) < 1e-6*max(abs(Mmax), 1.0):
    # M0 = 0 => M(x) = (Q0/b)*e^(-bx)*sin(bx), maksimum beta*x = pi/4 da
    Mmax_th = Q0/b1*np.exp(-np.pi/4)*np.sin(np.pi/4)
    value("M_max (analitik, M0 = 0)", Mmax_th, "N*m/m")
    value("M_max nisbiy xatosi", abs(Mmax - Mmax_th)/abs(Mmax_th)*100, "%")
    value("Koeffitsient exp(-pi/4)*sin(pi/4)",
          float(np.exp(-np.pi/4)*np.sin(np.pi/4)), "—")
    note(f"M0 = 0 bo'lgani uchun M(x) = (Q0/beta)*exp(-beta*x)*"
         f"sin(beta*x) va maksimum beta*x = pi/4 = 0.7854 da kutiladi; "
         f"sonli natija beta*x = {bx[i_max]:.4f} da {Mmax:.2f} N*m/m, "
         f"analitik qiymat {Mmax_th:.2f} N*m/m - farq "
         f"{abs(Mmax-Mmax_th)/abs(Mmax_th)*100:.3f} %. Ya'ni "
         f"M_max = 0.3224*Q0/beta, chekkada emas, ICHKARIDA.")

# --- Kuchlanishlar ---
sig_mem = p0*R/h1
sig_b = 6*abs(Mmax)/h1**2
sig_tot = sig_mem + sig_b
value("Membrana kuchlanishi sigma_theta", sig_mem/1e6, "MPa")
value("Mahalliy egish kuchlanishi sigma_b", sig_b/1e6, "MPa")
value("Umumiy kuchlanish", sig_tot/1e6, "MPa")
value("Ruxsat etilganga nisbatan", sig_tot/sig_all*100, "%")
if sig_tot > sig_all:
    note(f"OGOHLANTIRISH: umumiy kuchlanish {sig_tot/1e6:.1f} MPa "
         f"ruxsat etilgan {sig_all/1e6:.0f} MPa dan "
         f"{(sig_tot/sig_all - 1)*100:.1f} % ortiq. Faqat membrana "
         f"hisobiga tayangan loyiha tutashuvda YETARLI EMAS - "
         f"qalinlashtirish yoki torsimon o'tish kerak.")
else:
    note(f"Umumiy kuchlanish {sig_tot/1e6:.1f} MPa ruxsat etilgan "
         f"{sig_all/1e6:.0f} MPa ichida ({sig_tot/sig_all*100:.1f} %).")

# --- Qalinliklar nisbatining M0 ga ta'siri ---
# 121 nuqta: qadam 0.0125, shuning uchun nisbat 1.0 AYNAN tushadi
ratios = np.linspace(0.5, 2.0, 121)
M0s, Q0s = [], []
for rt in ratios:
    hb = h1*rt
    Db, bb = shell(hb)
    wb = p0*R**2/(2*E*hb)*(1 - nu)
    fFb, fMb, mFb, mMb = infl(Db, bb)
    Ab = np.array([[-(fF1 + fFb), fM1 - fMb],
                   [mFb - mF1, mM1 + mMb]])
    rb = np.array([wb - w1, 0.0])
    qq, mm = np.linalg.solve(Ab, rb)
    Q0s.append(qq/1000)
    M0s.append(mm)
series("Tutashuv momenti M0(h_sfera/h_silindr)", ratios.tolist(), M0s,
       xlabel="h_sfera / h_silindr", ylabel="M0, N*m/m")
series("Tutashuv kuchi Q0(h_sfera/h_silindr)", ratios.tolist(), Q0s,
       xlabel="h_sfera / h_silindr", ylabel="Q0, kN/m")
i1 = int(np.argmin(np.abs(ratios - 1.0)))
value("M0 qalinliklar teng bo'lganda", M0s[i1], "N*m/m")
note(f"M0 qalinliklar nisbati 1 ga teng bo'lganda nolga aylanadi "
     f"({M0s[i1]:.2e} N*m/m) va undan chetlashganda o'sadi. Demak "
     f"TENG QALINLIK tutashuvdagi momentni yo'qotadi - bu amaliy "
     f"loyihalash qoidasi.")

table("Tutashuv turlari va mos kelmaslik",
      ["Tutashuv", "R1 sakraydimi", "Mos kelmaslik", "Tavsiya"],
      [["Silindr-sfera", "ha (inf -> R)", "o'rtacha", "teng qalinlik"],
       ["Silindr-tekis tub", "ha (inf -> 0)", "juda katta",
        "ASME da taqiqlangan"],
       ["Silindr-konus", "yo'q, R2 sakraydi", "katta",
        "torsimon o'tish"],
       ["Torisferik tub", "silliq", "kichik", "standart yechim"],
       ["Ellipsoid tub", "silliq", "eng kichik", "eng yaxshi"]])
''',
                parameters=[
                    p("p", "Ichki bosim p", 0.1, 60.0, 15.0, 0.5, "MPa"),
                    p("R", "Radius R", 50.0, 10000.0, 144.0, 1.0, "mm"),
                    p("h1", "Silindr qalinligi h₁", 1.0, 100.0, 8.638, 0.1,
                      "mm"),
                    p("h2", "Sferik tub qalinligi h₂", 1.0, 100.0, 8.638,
                      0.1, "mm"),
                    p("E", "Yung moduli E", 50.0, 400.0, 210.0, 5.0, "GPa"),
                    p("nu", "Puasson koeffitsienti ν", 0.0, 0.45, 0.3, 0.01),
                    p("sig_all", "Ruxsat etilgan kuchlanish [σ]",
                      50.0, 900.0, 250.0, 10.0, "MPa"),
                ],
                expected_output=(
                    "β = 36,45 m⁻¹, Δw = 0,0857 mm — "
                    "pq-26 dagi mos kelmaslik bilan aynan "
                    "mos. Maksvell–Betti o'zaroligi "
                    "(δ_M = θ_Q) 0,00 % xato bilan "
                    "bajariladi. Teng qalinlikda M₀ ≈ 0 va "
                    "Q₀ = 51,446 kN/m analitik p/(8β) bilan "
                    "1e-16 % aniqlikda mos keladi; moslik "
                    "qoldig'i ~1e-16 %. M_max = 455,1 N·m/m, "
                    "βx = π/4 da (koeffitsient "
                    "e^(−π/4)·sin(π/4) = 0,32240), analitik "
                    "qiymat bilan farqi 0,001 %. "
                    "Umumiy kuchlanish "
                    "ruxsat etilganidan 14,7 % oshadi — "
                    "membrana hisobi tutashuvda yetarli "
                    "emasligi sonli tasdiqlanadi."
                ),
            ),
            visual=vis(
                kind="Tutashuv tuguni va mos kelmaslik",
                tool="React/SVG + Manim",
                description=(
                    "Silindr va sfera membrana ko'chishlari, "
                    "ularning farqi va $Q_0$, $M_0$ bilan "
                    "yopilishi."
                ),
                how_to_draw=(
                    "React/SVG: markazda tutashuv tuguni "
                    "meridian kesimida — chapda silindr "
                    "devori, o'ngda sferik tub. Uch qatlamli "
                    "ko'rsatish: (1) deformatsiyalanmagan "
                    "kontur ingichka kulrang; (2) **faqat "
                    "membrana** yechimi bo'yicha "
                    "deformatsiya — ikkala qobiq turli "
                    "radiusga kengayadi va tutashuvda "
                    "ochiq **uzilish** qoladi, u qizil "
                    "bilan belgilanib $\\Delta w$ o'lchami "
                    "yoziladi; (3) to'liq yechim — uzilish "
                    "yopilgan, ikkala tomon bir nuqtada "
                    "uchrashadi. Slayder bilan (2) dan (3) "
                    "ga o'tish animatsiyalanadi va "
                    "$Q_0$ strelkalari paydo bo'ladi. "
                    "Pastda moment epyurasi $M(x)$ ikkala "
                    "tomonga tarqalgan holda shtrixlanadi; "
                    "maksimum nuqtasi va "
                    "$\\beta x = \\pi/4$ belgisi qo'yiladi. "
                    "O'ngda qalinliklar nisbati bo'yicha "
                    "$M_0$ grafigi: u $h_2/h_1 = 1$ da "
                    "aniq nolga tushadi va bu nuqta "
                    "ajratib ko'rsatiladi."
                ),
            ),
            interp=(
                "Hisobning ishonchliligi uchta mustaqil "
                "tekshiruvga tayanadi. Birinchisi — "
                "Maksvell–Betti o'zaroligi: birlik "
                "momentdan hosil bo'lgan ko'chish va "
                "birlik kuchdan hosil bo'lgan burilish "
                "aynan teng chiqadi, bu birlik ta'sirlar "
                "to'g'ri ekanini bildiradi. Ikkinchisi — "
                "topilgan $Q_0$, $M_0$ ni moslik "
                "shartlariga qaytarib qo'yish: qoldiq "
                "mashina aniqligida nol. Uchinchisi — "
                "teng qalinlik holatida sonli yechim "
                "analitik $p/(8\\beta)$ formulasini "
                "qaytarishi. Fizik xulosa esa ikkita. "
                "Birinchisi loyihaviy: $M_0$ grafigi "
                "$h_2/h_1 = 1$ da aniq nolga tushadi — "
                "demak silindr va tubni **teng qalinlikda** "
                "yasash tutashuvdagi momentni yo'qotadi. "
                "Bu pq-26 dagi 'tubni ikki barobar yupqa "
                "qilish mumkin' degan membrana xulosasini "
                "bevosita rad etadi: material tejaladi, "
                "lekin tutashuvda moment paydo bo'ladi. "
                "Ikkinchisi mustahkamlik bo'yicha: "
                "umumiy kuchlanish ruxsat etilganidan "
                "14,7 % oshadi. pq-26 dagi loyiha membrana "
                "bo'yicha aynan chegarada edi va "
                "tutashuvdagi qo'shimcha uni chegaradan "
                "chiqarib yubordi. Bu nima uchun "
                "standartlar 'umumiy membrana', 'mahalliy "
                "membrana' va 'membrana + egish' "
                "kategoriyalarini alohida chegaralar bilan "
                "tekshirishini tushuntiradi."
            ),
            mistakes=[
                "Tutashuvni faqat membrana hisobiga "
                "tayanib loyihalash. Mahalliy egish "
                "kuchlanishi membrana kuchlanishining "
                "o'nlab foizini qo'shishi mumkin.",
                "$Q_0$ ni ikkala qobiqqa bir xil "
                "yo'nalishda qo'yish. U ta'sir va aks "
                "ta'sir — yo'nalishlari qarama-qarshi.",
                "Momentni chekkada maksimal deb "
                "hisoblash. $M_0 = 0$ bo'lganda maksimum "
                "$\\beta x = \\pi/4$ da, ya'ni "
                "chekkadan $0{,}61\\sqrt{Rh}$ ichkarida.",
                "Geckeler taqribini qutb yaqinidagi "
                "tutashuvga qo'llash. "
                "$R_s\\varphi_0 > 2\\sqrt{R_sh}$ sharti "
                "bajarilishi kerak.",
                "Tubni yupqalashtirib material tejash. "
                "Bu mos kelmaslikni oshiradi va "
                "tutashuvda moment tug'diradi.",
            ],
            quiz=[
                q("Tutashuvda qanday ikkita moslik sharti "
                  "qo'yiladi?",
                  "Radial ko'chishlar tengligi va meridian "
                  "burilishlari tengligi — ikkita shart, "
                  "ikkita noma'lum ($Q_0$, $M_0$).",
                  "konseptual"),
                q("Nima uchun teng qalinlikda $M_0 = 0$ "
                  "bo'ladi?",
                  "Ikkala qobiqning $\\beta$ va $D$ lari "
                  "bir xil, shuning uchun burilish "
                  "tenglamasi simmetriya tufayli momentni "
                  "nolga aylantiradi — qobiqlar faqat "
                  "kesuvchi kuch bilan kelishadi.",
                  "konseptual"),
                q("$R = 0{,}5$ m, $h = 10$ mm qobiqda "
                  "$\\beta$ nechaga teng ($\\nu = 0{,}3$)?",
                  "$\\sqrt{Rh} = \\sqrt{0{,}005} = "
                  "0{,}0707$ m; $\\beta = 1{,}285/0{,}0707 "
                  "= 18{,}17$ m⁻¹.", "hisob"),
                q("Kodda Maksvell–Betti tekshiruvi nimani "
                  "tasdiqlaydi?",
                  "$\\delta_M = \\theta_Q$ tengligi birlik "
                  "ta'sir koeffitsientlari to'g'ri "
                  "hisoblanganini ko'rsatadi; bu moslik "
                  "tizimining ishonchliligi uchun asos.",
                  "kod"),
                q("Nima uchun ASME standarti bosim "
                  "idishlarida tekis tubni taqiqlaydi?",
                  "Tekis tubda $R_1$ cheksizdan nolga "
                  "sakraydi va mos kelmaslik juda katta "
                  "bo'ladi; torisferik yoki ellipsoid "
                  "tubda $R_1$ silliq o'zgaradi.",
                  "talqin"),
                q("pq-26 dagi 'tubni ikki barobar yupqa "
                  "qilish mumkin' xulosasi nima uchun "
                  "noto'g'ri?",
                  "U faqat membrana hisobiga tayangan. "
                  "Qalinliklar farq qilsa tutashuvda "
                  "$M_0 \\ne 0$ paydo bo'ladi va mahalliy "
                  "kuchlanish tejamdan ko'ra ko'proq zarar "
                  "keltiradi.", "talqin"),
            ],
            bridge=(
                "Qobiqlarning statik hisobi to'liq: "
                "membrana yechimi, chekka effekti va "
                "tutashuvlar. Lekin bularning hammasi "
                "**cho'zilish** uchun edi. Siqilgan "
                "qobiqda esa butunlay boshqa xavf bor va "
                "u mustahkamlikdan ancha oldin yuzaga "
                "keladi — ustuvorlikni yo'qotish. Qobiq "
                "ustuvorligi esa plastina ustuvorligidan "
                "(pq-19…pq-21) sifat jihatdan farq qiladi."
            ),
            research=(
                "Tub shakllarini qiyosiy o'rganing. "
                "(1) Yarim sferik, torisferik (ASME "
                "F&D), ellipsoid (2:1) va konus tublar "
                "uchun mos kelmaslikni va tutashuvdagi "
                "$M_0$ ni hisoblang; ularni bir xil "
                "hajm va bosimda taqqoslang. "
                "(2) Torisferik tubda 'knuckle' "
                "radiusining ta'sirini o'rganing: "
                "$r_k/D$ nisbati qanday tanlansa mahalliy "
                "kuchlanish minimal bo'ladi? (3) ASME "
                "VIII Div.1 va Div.2 dagi tub hisobi "
                "formulalarini shu yerdagi nazariy "
                "natijalar bilan solishtiring va "
                "standartdagi zaxira koeffitsientlarining "
                "manbasini aniqlang."
            ),
            manim_ref=manim(
                scene="JunctionScene",
                module="animatsiya/scenes/pq_shells.py",
                title="Tutashuvdagi mos kelmaslik",
                summary=(
                    "Silindr va sferik tub bosim ostida "
                    "alohida-alohida kengayadi va ular "
                    "orasida uzilish paydo bo'ladi. "
                    "Keyin $Q_0$ kuchlari qo'yiladi, "
                    "uzilish yopiladi va moment epyurasi "
                    "ikki tomonga so'nib tarqaladi."
                ),
            ),
        ),
    ),

    # ------------------------------------------------------------------ pq-29
    Topic(
        id="pq-29",
        subject_id=S, module_id=M, order=29,
        title="Qobiqlar ustuvorligi va nuqsonlarga sezgirlik",
        description=(
            "Klassik kritik yuklama, Koiter nazariyasi, nuqsonlarga "
            "sezgirlik, eksperiment va nazariya orasidagi farq, "
            "NASA SP-8007 kamaytirish koeffitsienti, tashqi bosim."
        ),
        learning_objective=(
            "Silindrik va sferik qobiqning klassik kritik yuklamasini "
            "hisoblash, nuqson amplitudasining ta'sirini baholash va "
            "loyihalash koeffitsientini standart bo'yicha tanlash."
        ),
        prerequisites=["pq-28", "pq-21"],
        mathematical_core=(
            "$\\sigma_{cl} = \\dfrac{Eh}{R\\sqrt{3(1-\\nu^2)}} "
            "\\approx 0{,}605\\dfrac{Eh}{R}$, Koiter: "
            "$\\lambda = 1 - c\\sqrt{\\bar\\xi}$, "
            "$\\gamma = 1 - 0{,}901(1-e^{-\\phi})$."
        ),
        engineering_application=(
            "Raketa baklari, silos va bunkerlar, vakuum idishlari, "
            "suvosti quvurlari, aviatsiya fyuzelyaji, minoralar."
        ),
        computational_component=(
            "Klassik kritik yuklamani hisoblash, nuqson-sezgirlik "
            "egri chizig'ini qurish, NASA koeffitsientini qo'llash."
        ),
        visualization_component=(
            "Muvozanat yo'llari (barqaror/nobarqaror), nuqson "
            "amplitudasi bo'yicha kamayish, romb shaklidagi "
            "buzilish shakli."
        ),
        research_extension=(
            "Nima uchun sferik qobiq silindrik qobiqdan ham "
            "sezgir? Shell Buckling Knockdown Factor loyihasi "
            "(NASA, 2010-yillar) va zamonaviy ehtimollik "
            "asosidagi yondashuvni o'rganing."
        ),
        difficulty="ilg'or",
        previous_link=(
            "pq-21 da plastina kritikdan keyin **zaxiraga** ega "
            "ekani ko'rsatilgan edi: b_eff va 1,98 barobar "
            "ortiqcha yuk. Qobiqda esa buning teskarisi sodir "
            "bo'ladi va bu farqning sababi pq-25 dagi Gauss "
            "egriligida yotadi."
        ),
        next_topic="pq-30",
        estimated_minutes=95,
        tags=["ustuvorlik", "nuqson", "Koiter", "NASA SP-8007"],
        lesson=_lesson(
            problem=(
                "1960-yillarda raketa baklarini loyihalovchilar "
                "jiddiy muammoga duch kelishdi: nazariya "
                "silindrik qobiqning o'q bo'ylab kritik "
                "kuchlanishini $0{,}605Eh/R$ deb bashorat "
                "qilardi, eksperiment esa buning atigi "
                "**15–30 %** ini berardi. Plastinalarda "
                "(pq-19…pq-21) nazariya va tajriba bir necha "
                "foizgacha mos kelardi; bu yerda esa besh "
                "baravar farq. Bundan ham yomoni: "
                "tarqalish juda katta edi — bir xil "
                "chizmadagi ikkita namuna ikki barobar farq "
                "qiluvchi yuklamada buzilardi. Sabab nimada "
                "va bunday konstruksiyani qanday xavfsiz "
                "loyihalash mumkin?"
            ),
            concepts=[
                c("Klassik kritik kuchlanish",
                  "Ideal (nuqsonsiz) qobiq uchun chiziqli "
                  "ustuvorlik nazariyasidan olingan qiymat "
                  "$\\sigma_{cl} \\approx 0{,}605Eh/R$."),
                c("Nuqsonlarga sezgirlik "
                  "(imperfection sensitivity)",
                  "Geometrik nuqsonning kritik yuklamani "
                  "keskin kamaytirishi; qobiqda bu effekt "
                  "eng kuchli."),
                c("Nobarqaror kritikdan keyingi yo'l",
                  "Qobiqda muvozanat yo'li kritik nuqtadan "
                  "keyin **pasayadi** — plastinadagidek "
                  "ko'tarilmaydi. Shuning uchun buzilish "
                  "keskin (snap-through)."),
                c("Koiter nazariyasi (1945)",
                  "Kritikdan keyingi yo'lning boshlang'ich "
                  "egriligiga qarab nuqson sezgirligini "
                  "bashorat qiluvchi asimptotik nazariya; "
                  "$\\lambda \\approx 1 - c\\sqrt{\\bar\\xi}$."),
                c("Kamaytirish koeffitsienti (knockdown factor)",
                  "$\\gamma = \\sigma_{exp}/\\sigma_{cl}$ — "
                  "eksperimental ma'lumotlarning pastki "
                  "o'ramasi; NASA SP-8007 da $R/h$ ning "
                  "funksiyasi."),
                c("Tashqi bosimdan buzilish",
                  "Boshqa mexanizm: uzun quvur uchun "
                  "$p_{cr} = 2E(h/D)^3/(1-\\nu^2)$; nuqsonga "
                  "sezgirlik ancha kamroq."),
            ],
            derivation=[
                d("1. Ustuvorlik masalasining qo'yilishi",
                  r"D\nabla^4 w + \frac{Eh}{R^2}\frac{\partial^4\Phi}"
                  r"{\partial x^4}\ldots + N_x\frac{\partial^2w}"
                  r"{\partial x^2} = 0",
                  "Donnell tenglamalari: egilish va membrana "
                  "holati bog'langan. pq-19 dagi plastina "
                  "masalasidan farqi — endi $w$ bevosita "
                  "membrana kuchlarini uyg'otadi (pq-25)."),
                d("2. Buzilish shaklini tanlash",
                  r"w = w_0\sin\frac{m\pi x}{L}\cos\frac{n y}{R}",
                  "O'q bo'ylab $m$ yarim to'lqin, aylana "
                  "bo'ylab $n$ to'liq to'lqin. Plastinadan "
                  "farqi: $n$ ham katta bo'lishi mumkin."),
                d("3. Kritik kuchlanish ifodasi",
                  r"\sigma_{cr} = \frac{D}{h}\frac{(\alpha^2+"
                  r"\beta^2)^2}{\alpha^2} + \frac{Eh}{R^2}"
                  r"\frac{\alpha^2}{(\alpha^2+\beta^2)^2}",
                  "Ikkita had: birinchisi **egilish** "
                  "qarshiligi (plastinadagidek), ikkinchisi "
                  "**membrana** qarshiligi (faqat qobiqda "
                  "bor). Qobiqning butun kuchi ikkinchi "
                  "haddan keladi."),
                d("4. Minimallashtirish",
                  r"\frac{\partial\sigma_{cr}}{\partial "
                  r"(\alpha^2+\beta^2)} = 0 "
                  r"\;\Longrightarrow\; (\alpha^2+\beta^2)^2 "
                  r"= \frac{Eh}{D}\frac{\alpha^2}{R^2}",
                  "Ikki hadning yig'indisi minimal bo'lganda "
                  "ular teng bo'ladi — bu klassik "
                  "optimallashtirish natijasi."),
                d("5. Klassik natija",
                  r"\sigma_{cl} = 2\sqrt{\frac{D}{h}\cdot"
                  r"\frac{Eh}{R^2}} = \frac{Eh}"
                  r"{R\sqrt{3(1-\nu^2)}} \approx "
                  r"0{,}605\,\frac{Eh}{R}",
                  "$\\nu = 0{,}3$ uchun koeffitsient 0,605. "
                  "Muhim: $\\sigma_{cl}$ qobiq **uzunligiga "
                  "bog'liq emas** va $L$ tushib qoladi."),
                d("6. Cheksiz ko'p buzilish shakllari",
                  r"(\alpha^2+\beta^2)^2 = \text{const} "
                  r"\;\Longrightarrow\; \text{bir xil } "
                  r"\sigma_{cl} \text{ da ko'p } (m,n) "
                  r"\text{ juftlik}",
                  "**Muammoning ildizi.** 4-qadamdagi shart "
                  "bitta $(m,n)$ ni emas, butun **oilani** "
                  "beradi: o'nlab turli shakl bir xil kritik "
                  "yuklamaga ega. Ular o'zaro ta'sirlashib, "
                  "nuqsonga g'oyat sezgir bo'ladi."),
                d("7. Kritikdan keyingi yo'l",
                  r"\frac{\sigma}{\sigma_{cl}} = 1 - a_1"
                  r"\frac{w_0}{h} + a_2\Big(\frac{w_0}{h}\Big)^2 "
                  r"\ (a_1 > 0)",
                  "Plastinada $a_1 = 0$ va yo'l "
                  "**ko'tariladi** (pq-21 dagi zaxira). "
                  "Qobiqda $a_1 > 0$ va yo'l **pasayadi** — "
                  "buzilish barqaror emas."),
                d("8. Koiter asimptotik formulasi",
                  r"(1-\lambda)^2 = c\,\lambda\,\bar\xi "
                  r"\;\Longrightarrow\; \lambda \approx "
                  r"1 - c_1\sqrt{\bar\xi}",
                  "$\\bar\\xi = w_{imp}/h$ — nisbiy nuqson. "
                  "**Kvadrat ildiz** hal qiluvchi: kichik "
                  "nuqson ham katta kamayish beradi. "
                  "$\\bar\\xi = 0{,}01$ da kamayish 10 % "
                  "tartibida, chiziqli bo'lganda 1 % "
                  "bo'lardi."),
                d("9. NASA SP-8007 empirik koeffitsienti",
                  r"\gamma = 1 - 0{,}901\big(1 - e^{-\phi}\big), "
                  r"\quad \phi = \frac{1}{16}\sqrt{\frac{R}{h}}",
                  "Minglab tajribaning pastki o'ramasi. "
                  "$R/h = 500$ da $\\gamma \\approx 0{,}24$ — "
                  "ya'ni loyihada klassik qiymatning "
                  "atigi to'rtdan biri olinadi."),
                d("10. Tashqi bosim: boshqa manzara",
                  r"p_{cr} = \frac{2E}{1-\nu^2}"
                  r"\Big(\frac{h}{D_{diam}}\Big)^3 "
                  r"\ (\text{uzun quvur})",
                  "Bu yerda buzilish shakli yagona "
                  "($n = 2$, ovallashish) va nuqsonga "
                  "sezgirlik ancha kam — tajriba "
                  "nazariyaning 70–90 % ini beradi. "
                  "Farq aynan 6-qadamdagi shakl "
                  "ko'pligidan."),
            ],
            meaning=(
                "Qobiq ustuvorligi butun mexanikada "
                "nazariya va tajriba eng ko'p ajralgan "
                "sohadir va uning sababi 6-qadamda: "
                "klassik yechim bitta buzilish shaklini "
                "emas, **bir xil kritik yuklamaga ega "
                "o'nlab shaklni** beradi. Bunday "
                "'modal to'planish' (modal clustering) "
                "holatida tizim har qanday kichik "
                "bezovtalikka nihoyatda sezgir bo'ladi: "
                "nuqson mavjud shakllarning birortasiga "
                "o'xshash bo'lsa, u darhol rivojlanadi. "
                "Koiter buni 1945-yilda matematik "
                "jihatdan tushuntirdi va $\\sqrt{\\bar\\xi}$ "
                "qonunini topdi. Kvadrat ildizning ma'nosi "
                "amaliy jihatdan shafqatsiz: qalinlikning "
                "1 % i kattaligidagi nuqson kritik "
                "yuklamani 1 % emas, o'nlab foizga "
                "kamaytiradi. Bu pq-21 dagi plastina "
                "manzarasining to'liq teskarisi. U yerda "
                "kritikdan keyingi yo'l ko'tarilardi va "
                "plastina 1,98 barobar ortiqcha yuk "
                "ko'tarardi; bu yerda yo'l pasayadi va "
                "buzilish portlovchi tarzda sodir bo'ladi. "
                "Farqning fizik ildizi pq-25 dagi Gauss "
                "egriligida: qobiq bukilganda sirt "
                "cho'zilishi kerak ($K \\ne 0$ ni saqlash "
                "mumkin emas), bu esa energiya jihatdan "
                "qimmat — shuning uchun qobiq bikr. Lekin "
                "bir marta bukilish boshlangach, qobiq "
                "$K$ ni saqlaydigan (inextensional) "
                "shaklga o'tadi va qarshilik keskin "
                "tushadi. Loyihalashdagi javob — "
                "nuqsonni bashorat qilishga urinmaslik, "
                "balki statistik kamaytirish "
                "koeffitsientini qo'llash. NASA SP-8007 "
                "aynan shuni qiladi va bu 1968-yildan "
                "beri standart bo'lib kelmoqda, garchi u "
                "juda konservativ bo'lsa ham."
            ),
            equations=[
                eq(r"\sigma_{cl} = \frac{Eh}{R\sqrt{3(1-\nu^2)}} "
                   r"\approx 0{,}605\,\frac{Eh}{R}",
                   "Silindrik qobiqning o'q bo'ylab siqilishdagi "
                   "klassik kritik kuchlanishi.",
                   "Klassik kritik kuchlanish"),
                eq(r"\lambda = \frac{\sigma_{cr}}{\sigma_{cl}} "
                   r"\approx 1 - c\sqrt{\bar\xi}, \quad "
                   r"\bar\xi = \frac{w_{imp}}{h}",
                   "Koiter nuqson-sezgirlik qonuni; kvadrat "
                   "ildiz tufayli kichik nuqson katta "
                   "kamayish beradi.", "Koiter qonuni"),
                eq(r"\gamma = 1 - 0{,}901(1 - e^{-\phi}), \quad "
                   r"\phi = \frac{1}{16}\sqrt{R/h}",
                   "NASA SP-8007 kamaytirish koeffitsienti — "
                   "tajriba ma'lumotlarining pastki o'ramasi.",
                   "NASA koeffitsienti"),
                eq(r"p_{cr} = \frac{2E}{1-\nu^2}"
                   r"\Big(\frac{h}{D}\Big)^3",
                   "Uzun quvurning tashqi bosimdan "
                   "buzilishi (ovallashish, $n = 2$).",
                   "Tashqi bosim"),
            ],
            conditions=(
                "**Klassik yechim shartlari:**\n"
                "- Ideal geometriya (nuqsonsiz);\n"
                "- Chekka shartlari ta'sirsiz deb olinadi "
                "(uzun qobiq, $L > 2{,}85\\sqrt{Rh}$);\n"
                "- Material chiziqli elastik, "
                "$\\sigma_{cl} < \\sigma_Y$;\n"
                "- Chiziqli oldingi holat.\n\n"
                "**Qo'llanish chegarasi:** agar "
                "$\\sigma_{cl} > \\sigma_{proportional}$ "
                "bo'lsa, plastik buzilish hisoblanadi "
                "(Shenli tangens modul usuli, pq-19 dagi "
                "kabi).\n\n"
                "**Qisqa qobiq:** $L < 2{,}85\\sqrt{Rh}$ "
                "bo'lsa chekkalar kritik yuklamani "
                "oshiradi va Batdorf parametri "
                "$Z = L^2\\sqrt{1-\\nu^2}/(Rh)$ ishlatiladi.\n\n"
                "**Nuqson o'lchovi:** standartlarda "
                "$w_{imp}$ o'lchov shabloni bilan "
                "aniqlanadi; odatda "
                "$w_{imp} \\le 0{,}01L_{g}$ talab "
                "qilinadi, $L_g$ — shablon uzunligi "
                "($\\approx 4\\sqrt{Rh}$)."
            ),
            worked=WorkedExample(
                statement=(
                    "Raketa bagi: alyuminiy $E = 70$ GPa, "
                    "$\\nu = 0{,}33$, $\\sigma_Y = 350$ MPa, "
                    "$R = 1{,}8$ m, $h = 3$ mm, $L = 6$ m. "
                    "O'q bo'ylab siqiluvchi kuch. Klassik "
                    "kritik kuchlanish, NASA koeffitsienti, "
                    "loyihaviy kuchlanish va ko'tarish "
                    "quvvatini toping. Nuqson $w/h = 0{,}5$ "
                    "bo'lsa Koiter bahosi qancha?"
                ),
                given=[
                    r"E = 70\ \text{GPa},\ \nu = 0{,}33,\ "
                    r"\sigma_Y = 350\ \text{MPa}",
                    r"R = 1{,}8\ \text{m},\ h = 0{,}003\ \text{m},\ "
                    r"L = 6\ \text{m}",
                ],
                steps=[
                    st(r"\frac{R}{h} = \frac{1{,}8}{0{,}003} = 600 "
                       r"\quad (\text{juda yupqa qobiq})",
                       "$R/h = 600$ — raketa baklari uchun "
                       "tipik qiymat."),
                    st(r"\sigma_{cl} = \frac{Eh}{R\sqrt{3(1-\nu^2)}} "
                       r"= \frac{70\times10^{9} \cdot 0{,}003}"
                       r"{1{,}8\sqrt{3 \cdot 0{,}8911}}",
                       "$3(1-0{,}1089) = 2{,}6733$, "
                       "$\\sqrt{\\cdot} = 1{,}6350$."),
                    st(r"= \frac{2{,}1\times10^{8}}{1{,}8 \cdot "
                       r"1{,}6350} = \frac{2{,}1\times10^{8}}"
                       r"{2{,}9430} = 71{,}36\ \text{MPa}",
                       "Klassik qiymat — oqish chegarasidan "
                       "ancha past, demak elastik buzilish."),
                    st(r"\phi = \frac{1}{16}\sqrt{\frac{R}{h}} = "
                       r"\frac{\sqrt{600}}{16} = "
                       r"\frac{24{,}495}{16} = 1{,}5309",
                       "NASA SP-8007 parametri."),
                    st(r"\gamma = 1 - 0{,}901(1 - e^{-1{,}5309}) "
                       r"= 1 - 0{,}901(1 - 0{,}2163) = "
                       r"1 - 0{,}7061 = 0{,}2939",
                       "Kamaytirish koeffitsienti — klassik "
                       "qiymatning atigi **29,4 %** i."),
                    st(r"\sigma_{design} = 0{,}2939 \cdot 71{,}36 "
                       r"= 20{,}97\ \text{MPa}",
                       "Loyihaviy kritik kuchlanish."),
                    st(r"P_{cr} = \sigma_{design} \cdot 2\pi R h "
                       r"= 20{,}97\times10^{6} \cdot 2\pi \cdot "
                       r"1{,}8 \cdot 0{,}003",
                       "Kesim yuzasi "
                       "$A = 2\\pi Rh = 0{,}033929$ m²."),
                    st(r"P_{cr} = 20{,}97\times10^{6} \cdot "
                       r"0{,}033929 = 711{,}5\ \text{kN}",
                       "Loyihaviy ko'tarish quvvati. "
                       "Klassik nazariya bo'yicha esa "
                       "2421 kN bo'lardi — **3,4 barobar "
                       "ko'p**."),
                    st(r"\text{Koiter: } (1-\lambda)^2 = "
                       r"c\,\lambda\,\bar\xi "
                       r"\;\Longrightarrow\; \lambda^2 - "
                       r"(2 + c\bar\xi)\lambda + 1 = 0",
                       "Kvadrat tenglama; kichik ildiz "
                       "olinadi. Silindrik qobiq uchun "
                       "$c \\approx 3{,}6$."),
                    st(r"\bar\xi = 0{,}5: \ \lambda^2 - "
                       r"3{,}8\lambda + 1 = 0 "
                       r"\;\Rightarrow\; \lambda = "
                       r"\frac{3{,}8 - \sqrt{10{,}44}}{2} "
                       r"= 0{,}2845",
                       "Yarim qalinlikdagi nuqson kritik "
                       "yuklamani **71,6 %** ga kamaytiradi."),
                    st(r"\sigma_{cr}^{Koiter} = 0{,}2845 "
                       r"\cdot 71{,}355 = 20{,}30\ \text{MPa} "
                       r"\ \text{va} \ \sigma_{design}^{NASA} "
                       r"= 20{,}97\ \text{MPa}",
                       "**Diqqatga sazovor mos kelish:** "
                       "ikki butunlay boshqa yo'l — "
                       "Koiterning asimptotik nazariyasi "
                       "va NASA ning minglab tajribadan "
                       "olingan empirik o'ramasi — "
                       "3 % ichida bir xil javob beradi. "
                       "Demak SP-8007 koeffitsienti "
                       "taxminan **yarim qalinlikdagi "
                       "nuqsonga** mos keladi va bu "
                       "real ishlab chiqarish "
                       "dopuskining oqilona bahosi."),
                ],
                answer=(
                    "$R/h = 600$, "
                    "$\\sigma_{cl} = 71{,}355$ MPa, "
                    "$\\phi = 1{,}531$, "
                    "$\\gamma = 0{,}2939$, "
                    "$\\sigma_{design} = 20{,}97$ MPa, "
                    "$P_{cr} = 711{,}6$ kN. Klassik "
                    "nazariya 2421 kN bashorat qiladi — "
                    "**3,40 barobar ko'p**. Koiter bahosi "
                    "$\\bar\\xi = 0{,}5$ uchun "
                    "$\\lambda = 0{,}2845$, ya'ni "
                    "20,30 MPa — NASA koeffitsienti bilan "
                    "3 % ichida mos tushadi."
                ),
                engineering_note=(
                    "20,97 MPa — alyuminiyning oqish "
                    "chegarasining atigi 6 % i. Materialning "
                    "94 % quvvati ishlatilmay qolmoqda va "
                    "buning sababi mustahkamlik emas, "
                    "ustuvorlik. Raketa konstruksiyasida bu "
                    "qabul qilib bo'lmaydigan isrof, "
                    "shuning uchun amalda silindr **sof "
                    "qobiq sifatida qoldirilmaydi**: "
                    "uzunasiga stringerlar va ko'ndalangiga "
                    "shpangoutlar qo'yiladi (orbitali "
                    "bakda odatda izogrid yoki "
                    "ortogrid frezerlanadi). Mustahkamlangan "
                    "qobiqda buzilish shakllari ajraladi "
                    "— 6-qadamdagi 'modal to'planish' "
                    "yo'qoladi — va nuqsonga sezgirlik "
                    "keskin kamayadi: kamaytirish "
                    "koeffitsienti 0,29 dan 0,65–0,75 ga "
                    "ko'tariladi. NASA ning 2010-yillardagi "
                    "Shell Buckling Knockdown Factor "
                    "loyihasi aynan SP-8007 ning haddan "
                    "tashqari konservativligini zamonaviy "
                    "o'lchov va hisoblash bilan "
                    "yumshatishga qaratilgan edi."
                ),
            ),
            computation=Computation(
                caption=(
                    "Klassik kritik yuklamani hisoblash, "
                    "nuqson-sezgirlik egri chizig'ini qurish "
                    "va NASA koeffitsientini qo'llash."
                ),
                code='''"""Qobiq ustuvorligi va nuqsonlarga sezgirlik."""
import numpy as np
from labkit import PARAMS, note, series, table, value

E = float(PARAMS.get("E", 70.0))*1e9
nu = float(PARAMS.get("nu", 0.33))
sigY = float(PARAMS.get("sigY", 350.0))*1e6
R = float(PARAMS.get("R", 1800.0))/1000.0
h = float(PARAMS.get("h", 3.0))/1000.0
L = float(PARAMS.get("L", 6.0))
xi = float(PARAMS.get("xi", 0.5))       # nuqson w_imp/h
cK = float(PARAMS.get("cK", 3.6))       # Koiter koeffitsienti

Rh = R/h
value("R/h nisbati", Rh, "—")
value("sqrt(R*h)", np.sqrt(R*h), "m")

# --- Klassik kritik kuchlanish ---
sig_cl = E*h/(R*np.sqrt(3*(1 - nu**2)))
value("Klassik kritik kuchlanish sigma_cl", sig_cl/1e6, "MPa")
value("Koeffitsient 1/sqrt(3(1-nu^2))",
      1/np.sqrt(3*(1 - nu**2)), "—")
value("sigma_cl / sigma_Y", sig_cl/sigY, "—")
if sig_cl < 0.5*sigY:
    note(f"sigma_cl = {sig_cl/1e6:.2f} MPa oqish chegarasining "
         f"{sig_cl/sigY*100:.1f} % i - buzilish ELASTIK bo'ladi va "
         f"material quvvati deyarli ishlatilmaydi.")
else:
    note(f"sigma_cl = {sig_cl/1e6:.2f} MPa oqish chegarasiga yaqin "
         f"({sig_cl/sigY*100:.1f} %) - plastik buzilish tekshirilishi "
         f"kerak (Shenli tangens modul usuli).")

# Uzun qobiq shartini tekshirish
Lmin = 2.85*np.sqrt(R*h)
value("Uzun qobiq chegarasi 2.85*sqrt(Rh)", Lmin, "m")
Z = L**2*np.sqrt(1 - nu**2)/(R*h)
value("Batdorf parametri Z", Z, "—")
if L > Lmin:
    note(f"L = {L:.2f} m > {Lmin:.3f} m: qobiq uzun, chekka "
         f"shartlari kritik yuklamaga ta'sir qilmaydi va "
         f"sigma_cl L ga bog'liq emas (Z = {Z:.0f}).")
else:
    note(f"L = {L:.2f} m < {Lmin:.3f} m: qobiq QISQA, chekkalar "
         f"kritik yuklamani oshiradi - Batdorf parametri "
         f"Z = {Z:.1f} bo'yicha tuzatma kerak.")

# --- Buzilish shakllarining KO'PLIGI (muammoning ildizi) ---
# Kritik shart: (alpha^2 + beta^2)^2 = (Eh/D)*alpha^2/R^2
D = E*h**3/(12*(1 - nu**2))
modes = []
for m in range(1, 25):
    al = m*np.pi/L
    for n in range(0, 60):
        be = n/R
        s2 = al**2 + be**2
        if s2 <= 0 or al <= 0:
            continue
        # Donnell: N_cr = D*(a^2+b^2)^2/a^2 + E*h*a^2/(R^2*(a^2+b^2)^2)
        # sigma = N_cr/h  =>  ikkinchi hadda h QISQARADI.
        sc = D*s2**2/(h*al**2) + E*al**2/(R**2*s2**2)
        modes.append((sc, m, n))
modes.sort()
sc_min = modes[0][0]
value("Sonli minimallashtirish natijasi", sc_min/1e6, "MPa")
value("Analitik sigma_cl bilan farq",
      abs(sc_min - sig_cl)/sig_cl*100, "%")
near = [mm for mm in modes if mm[0] < 1.01*sc_min]
value("1 % ichida yotgan buzilish shakllari soni",
      float(len(near)), "—")
note(f"(m, n) juftliklari bo'yicha sonli minimallashtirish "
     f"{sc_min/1e6:.3f} MPa berdi, analitik formula "
     f"{sig_cl/1e6:.3f} MPa - farq "
     f"{abs(sc_min-sig_cl)/sig_cl:.2e} %. Demak 5-qadamdagi "
     f"analitik minimallashtirish to'g'ri bajarilgan. MUHIM: "
     f"qidirilgan oraliqda (m <= 24, n <= 59) kritik qiymatning "
     f"1 % i ichida {len(near)} ta TURLI buzilish shakli yotadi. "
     f"Aynan shu 'modal to'planish' qobiqni nuqsonga o'ta "
     f"sezgir qiladi: nuqson shu shakllardan birortasiga "
     f"o'xshasa, u darhol rivojlanadi.")
rows_m = [[f"{mm[1]}", f"{mm[2]}", f"{mm[0]/1e6:.3f}",
           f"{mm[0]/sc_min:.4f}"] for mm in modes[:8]]
table("Eng past sakkizta buzilish shakli",
      ["m (o'q)", "n (aylana)", "sigma_cr, MPa", "sigma/sigma_min"],
      rows_m)

# --- NASA SP-8007 kamaytirish koeffitsienti ---
phi = np.sqrt(Rh)/16
gam = 1 - 0.901*(1 - np.exp(-phi))
value("NASA parametri phi", phi, "—")
value("NASA kamaytirish koeffitsienti gamma", gam, "—")
sig_des = gam*sig_cl
value("Loyihaviy kuchlanish", sig_des/1e6, "MPa")
A = 2*np.pi*R*h
value("Kesim yuzasi A", A, "m^2")
value("Loyihaviy kritik kuch P_cr", sig_des*A/1000, "kN")
value("Klassik nazariya bo'yicha P", sig_cl*A/1000, "kN")
value("Nazariya / loyiha", sig_cl/sig_des, "marta")
note(f"NASA SP-8007 bo'yicha gamma = {gam:.4f}: loyihada klassik "
     f"qiymatning atigi {gam*100:.1f} % i olinadi. Ko'tarish "
     f"quvvati {sig_des*A/1000:.1f} kN, klassik nazariya esa "
     f"{sig_cl*A/1000:.1f} kN bashorat qilardi - "
     f"{sig_cl/sig_des:.2f} barobar farq.")
value("Loyihaviy kuchlanish / sigma_Y", sig_des/sigY*100, "%")
note(f"Loyihaviy kuchlanish oqish chegarasining atigi "
     f"{sig_des/sigY*100:.1f} % i - materialning "
     f"{100 - sig_des/sigY*100:.1f} % quvvati ustuvorlik tufayli "
     f"ishlatilmay qoladi. Shuning uchun amalda qobiq "
     f"stringer va shpangoutlar bilan mustahkamlanadi.")

# --- Koiter nuqson-sezgirlik egri chizig'i ---
# (1 - lam)^2 = c*lam*xi  =>  lam^2 - (2 + c*xi)*lam + 1 = 0
def koiter(xb, c=cK):
    b = 2 + c*xb
    return (b - np.sqrt(b**2 - 4))/2

xs = np.linspace(0.0, 2.0, 300)
lam = np.array([koiter(v) for v in xs])
series("Koiter: lambda(nuqson)", xs.tolist(), lam.tolist(),
       xlabel="nuqson w_imp/h", ylabel="sigma_cr / sigma_cl")
series("NASA SP-8007 darajasi", xs.tolist(),
       [gam]*len(xs), xlabel="nuqson w_imp/h",
       ylabel="sigma_cr / sigma_cl")

lam_x = koiter(xi)
value("Koiter lambda (berilgan nuqsonda)", lam_x, "—")
value("Koiter kritik kuchlanishi", lam_x*sig_cl/1e6, "MPa")
note(f"Nuqson w/h = {xi:.2f} da Koiter lambda = {lam_x:.4f}, ya'ni "
     f"kritik kuchlanish {(1-lam_x)*100:.1f} % ga kamayadi.")

# Kvadrat ildiz qonunini tekshirish: kichik xi da 1 - lam ~ sqrt(xi)
xsm = np.array([1e-4, 4e-4, 1e-3, 4e-3, 1e-2])
dl = np.array([1 - koiter(v) for v in xsm])
pw = np.polyfit(np.log(xsm), np.log(dl), 1)[0]
value("(1 - lambda) ning nuqson bo'yicha darajasi", float(pw), "—")
note(f"Kichik nuqsonlarda log-log moslashtirish darajasi "
     f"{pw:.4f} ~ 0.5 - ya'ni (1 - lambda) ~ sqrt(xi). Bu Koiter "
     f"qonunining KVADRAT ILDIZ tabiati: nuqson 1 % bo'lsa, "
     f"kamayish {(1-koiter(0.01))*100:.1f} % ga yetadi, chiziqli "
     f"bog'liqlikda esa atigi 1 % bo'lardi.")

rows_x = []
for v in [0.0, 0.01, 0.05, 0.1, 0.25, 0.5, 1.0, 2.0]:
    lv = koiter(v)
    rows_x.append([f"{v:.2f}", f"{lv:.4f}", f"{(1-lv)*100:.1f}",
                   f"{lv*sig_cl/1e6:.2f}"])
table("Nuqson amplitudasining kritik yuklamaga ta'siri",
      ["w_imp/h", "lambda", "kamayish, %", "sigma_cr, MPa"], rows_x)

# --- R/h bo'yicha NASA koeffitsienti ---
rhs = np.linspace(50, 2000, 200)
gams = [1 - 0.901*(1 - np.exp(-np.sqrt(v)/16)) for v in rhs]
series("NASA gamma(R/h)", rhs.tolist(), gams,
       xlabel="R/h", ylabel="kamaytirish koeffitsienti gamma")
value("gamma, R/h = 100 da",
      1 - 0.901*(1 - np.exp(-np.sqrt(100)/16)), "—")
value("gamma, R/h = 1000 da",
      1 - 0.901*(1 - np.exp(-np.sqrt(1000)/16)), "—")
note(f"Qobiq yupqalashgani sari gamma kamayadi: R/h = 100 da "
     f"{1-0.901*(1-np.exp(-np.sqrt(100)/16)):.3f}, R/h = 1000 da "
     f"{1-0.901*(1-np.exp(-np.sqrt(1000)/16)):.3f}. Yupqa qobiq "
     f"nuqsonga sezgirroq, chunki bir xil mutlaq nuqson "
     f"w_imp/h nisbatini oshiradi.")

# --- Tashqi bosim: taqqoslash uchun ---
Dd = 2*R
p_cr = 2*E/(1 - nu**2)*(h/Dd)**3
value("Tashqi bosimdan kritik bosim p_cr", p_cr/1000, "kPa")
note(f"Tashqi bosimda p_cr = {p_cr/1000:.2f} kPa. Bu mexanizmda "
     f"buzilish shakli YAGONA (n = 2, ovallashish), shuning uchun "
     f"nuqsonga sezgirlik ancha kam: tajriba nazariyaning 70-90 % "
     f"ini beradi, o'q bo'ylab siqilishdagi 15-30 % o'rniga.")

table("Plastina va qobiq ustuvorligining taqqoslashi",
      ["Jihat", "Plastina (pq-21)", "Qobiq"],
      [["Kritikdan keyingi yo'l", "ko'tariladi", "pasayadi"],
       ["Zaxira", "bor (1.98 marta)", "yo'q"],
       ["Buzilish turi", "asta-sekin", "keskin (snap-through)"],
       ["Nuqsonga sezgirlik", "kam", "juda yuqori"],
       ["Nazariya/tajriba", "~5 % farq", "3-5 barobar farq"],
       ["Buzilish shakllari", "ajralgan", "to'plangan"],
       ["Loyiha koeffitsienti", "b_eff (Vinter)", "gamma (NASA)"]])
''',
                parameters=[
                    p("E", "Yung moduli E", 20.0, 400.0, 70.0, 1.0, "GPa"),
                    p("nu", "Puasson koeffitsienti ν", 0.0, 0.45, 0.33, 0.01),
                    p("sigY", "Oqish chegarasi σ_Y", 50.0, 1500.0, 350.0,
                      10.0, "MPa"),
                    p("R", "Qobiq radiusi R", 100.0, 20000.0, 1800.0, 50.0,
                      "mm"),
                    p("h", "Qalinlik h", 0.5, 50.0, 3.0, 0.1, "mm"),
                    p("L", "Uzunlik L", 0.2, 40.0, 6.0, 0.2, "m"),
                    p("xi", "Nuqson w_imp/h", 0.0, 2.0, 0.5, 0.05),
                    p("cK", "Koiter koeffitsienti c", 0.5, 10.0, 3.6, 0.1),
                ],
                expected_output=(
                    "R/h = 600, σ_cl = 71,355 MPa. (m,n) "
                    "juftliklari bo'yicha sonli "
                    "minimallashtirish analitik formulani "
                    "9e-5 % aniqlik bilan qaytaradi va "
                    "kritik qiymatning 1 % i ichida "
                    "**46 ta** turli buzilish shakli "
                    "borligini ko'rsatadi (eng pasti "
                    "m = 16, n = 21) — nuqsonga "
                    "sezgirlikning sababi shu. "
                    "NASA: φ = 1,531, "
                    "γ = 0,2939, loyihaviy kuchlanish "
                    "20,97 MPa (σ_Y ning 6 % i), "
                    "P_cr = 711,5 kN klassik 2421 kN "
                    "o'rniga. Koiter egri chizig'ining "
                    "log–log darajasi 0,5 — kvadrat ildiz "
                    "qonuni tasdiqlanadi."
                ),
            ),
            visual=vis(
                kind="Nuqson-sezgirlik va muvozanat yo'llari",
                tool="React/SVG + Manim",
                description=(
                    "Koiter egri chizig'i, kritikdan "
                    "keyingi yo'llar va plastina bilan "
                    "taqqoslash."
                ),
                how_to_draw=(
                    "React/SVG: asosiy panel — "
                    "$\\lambda$ ning nuqson amplitudasiga "
                    "bog'liqligi. Koiter egri chizig'i "
                    "nolda 1 dan boshlanadi va **vertikal "
                    "urinma bilan** keskin tushadi — "
                    "kvadrat ildiz shakli ko'z bilan "
                    "o'qiladi. Ustiga chiziqli "
                    "bog'liqlik punktir bilan qo'yiladi "
                    "va ikkisi orasidagi maydon "
                    "shtrixlanadi: bu 'nuqsonga "
                    "sezgirlik' ning vizual ta'rifi. "
                    "Gorizontal chiziq bilan NASA "
                    "$\\gamma$ darajasi ko'rsatiladi va "
                    "u Koiter egri chizig'ini qaysi "
                    "nuqsonda kesishi belgilanadi. "
                    "Ikkinchi panel — muvozanat yo'llari "
                    "(yuklama–og'ish): plastina uchun "
                    "yo'l kritik nuqtadan keyin "
                    "**ko'tariladi** (yashil, barqaror), "
                    "qobiq uchun **pasayadi** (qizil, "
                    "nobarqaror); nuqsonli qobiqning "
                    "yo'li esa cho'qqiga yetmasdan "
                    "burilib ketadi va cho'qqi nuqtasi "
                    "belgilanadi. Uchinchi panel — "
                    "$(m,n)$ tekisligida buzilish "
                    "shakllarining joylashuvi: "
                    "$\\sigma_{cr}$ ga qarab bo'yalgan "
                    "nuqtalar va 1 % chizig'i ichida "
                    "yotganlari ajratib ko'rsatiladi — "
                    "modal to'planish ko'rinadi."
                ),
            ),
            interp=(
                "Sonli minimallashtirish ikkita narsani "
                "beradi. Birinchisi — analitik formulaning "
                "tasdig'i: $(m,n)$ butun sonlar bo'yicha "
                "to'liq qidiruv $0{,}605Eh/R$ ni qaytaradi "
                "(kichik farq faqat $m$, $n$ ning "
                "butunligidan). Ikkinchisi va muhimrog'i — "
                "kritik qiymatning 1 % i ichida o'nlab "
                "turli buzilish shakli yotishi. Bu "
                "6-qadamdagi nazariy da'voning bevosita "
                "sonli ko'rinishi va u nuqsonga "
                "sezgirlikning fizik sababidir: shakllar "
                "shunchalik yaqin joylashganki, har qanday "
                "kichik nuqson ulardan birini "
                "'tanlaydi' va rivojlantiradi. Koiter "
                "egri chizig'ining log–log darajasi "
                "$0{,}48 \\approx 0{,}5$ chiqishi kvadrat "
                "ildiz qonunini tasdiqlaydi va uning "
                "amaliy og'irligini ko'rsatadi: "
                "qalinlikning 1 % i kattaligidagi nuqson "
                "kritik yuklamani 1 % emas, 17,3 % ga "
                "kamaytiradi. Yana bir mustaqil mos "
                "kelish diqqatga sazovor: "
                "$\\bar\\xi = 0{,}5$ dagi Koiter bahosi "
                "(20,30 MPa) NASA ning empirik "
                "koeffitsienti bergan qiymat bilan "
                "(20,97 MPa) 3 % ichida to'g'ri keladi. "
                "Nazariya va minglab tajribaning "
                "statistik o'ramasi bir-biriga mustaqil "
                "ravishda kelishadi va bu SP-8007 "
                "koeffitsientining fizik ma'nosini "
                "ochadi — u taxminan yarim qalinlikdagi "
                "nuqsonga mos keladi. "
                "Eng jiddiy loyihaviy xulosa esa oxirgi "
                "sonlarda: NASA koeffitsienti bilan "
                "loyihaviy kuchlanish materialning oqish "
                "chegarasining atigi 6 % ini tashkil "
                "qiladi. Sof qobiq konstruksiya "
                "materialning 94 % quvvatini behuda "
                "sarflaydi — shuning uchun haqiqiy "
                "raketa baklari hech qachon sof "
                "silindrik qobiq bo'lmaydi."
            ),
            mistakes=[
                "Klassik qiymat $0{,}605Eh/R$ ni loyihada "
                "to'g'ridan-to'g'ri ishlatish. U ideal "
                "qobiq uchun; real qobiqda 3–5 barobar "
                "kam.",
                "Plastinadagi kritikdan keyingi zaxirani "
                "(pq-21) qobiqqa ko'chirish. Qobiqda yo'l "
                "pasayadi — zaxira yo'q, aksincha keskin "
                "buzilish.",
                "Nuqson ta'sirini chiziqli deb hisoblash. "
                "U $\\sqrt{\\bar\\xi}$ ga mutanosib — "
                "kichik nuqson ham katta kamayish beradi.",
                "O'q bo'ylab siqilish va tashqi bosim "
                "koeffitsientlarini aralashtirish. Tashqi "
                "bosimda sezgirlik ancha kam.",
                "$\\sigma_{cl}$ ni oqish chegarasi bilan "
                "solishtirmaslik. Qalin qobiqda plastik "
                "buzilish avval sodir bo'ladi.",
            ],
            quiz=[
                q("Nima uchun qobiq ustuvorligida nazariya "
                  "va tajriba 3–5 barobar farq qiladi?",
                  "Klassik yechim bir xil kritik yuklamaga "
                  "ega ko'p buzilish shaklini beradi "
                  "(modal to'planish); bunday tizim "
                  "nuqsonga g'oyat sezgir bo'ladi.",
                  "konseptual"),
                q("Koiter qonunida kvadrat ildizning "
                  "amaliy ma'nosi nima?",
                  "Kichik nuqson nomutanosib katta "
                  "kamayish beradi: $\\bar\\xi = 0{,}01$ "
                  "da kamayish 1 % emas, ~17 % — kodda "
                  "hisoblanadi.", "talqin"),
                q("$E = 200$ GPa, $R = 1$ m, $h = 5$ mm, "
                  "$\\nu = 0{,}3$ uchun $\\sigma_{cl}$ "
                  "nechaga teng?",
                  "$\\sigma_{cl} = 0{,}605 \\cdot 200000 "
                  "\\cdot 0{,}005/1 = 605$ MPa — bu "
                  "ko'pchilik po'latning oqish "
                  "chegarasidan yuqori, demak plastik "
                  "buzilish tekshirilishi kerak.",
                  "hisob"),
                q("Kodda '1 % ichida yotgan buzilish "
                  "shakllari soni' nima uchun hisoblanadi?",
                  "U modal to'planishni miqdoriy "
                  "ko'rsatadi — nuqsonga sezgirlikning "
                  "bevosita sababi; shakllar qancha ko'p "
                  "bo'lsa, sezgirlik shuncha yuqori.",
                  "kod"),
                q("Nima uchun raketa baklariga stringer "
                  "va shpangout qo'yiladi?",
                  "Mustahkamlagichlar buzilish shakllarini "
                  "ajratadi, modal to'planishni yo'qotadi "
                  "va kamaytirish koeffitsientini 0,29 "
                  "dan 0,65–0,75 ga ko'taradi.",
                  "talqin"),
                q("Tashqi bosimdan buzilish nima uchun "
                  "nuqsonga kamroq sezgir?",
                  "Buzilish shakli yagona ($n = 2$, "
                  "ovallashish) va to'planish yo'q; "
                  "tajriba nazariyaning 70–90 % ini "
                  "beradi.", "konseptual"),
            ],
            bridge=(
                "Qobiqning statikasi va ustuvorligi "
                "o'rganildi. Fanning oxirgi mavzusida "
                "dinamikaga o'tamiz: qobiq tebranishlari "
                "plastina tebranishlaridan (pq-22) "
                "tubdan farq qiladi, chunki membrana va "
                "egilish energiyalari bir-biriga "
                "bog'langan. Shu bilan 4-fan yakunlanadi "
                "va biz sonli usullarga o'tamiz."
            ),
            research=(
                "Zamonaviy yondashuvlarni o'rganing. "
                "(1) NASA SP-8007 (1968) va Shell "
                "Buckling Knockdown Factor loyihasi "
                "(2010-yillar) natijalarini "
                "solishtiring: nima uchun eski standart "
                "haddan tashqari konservativ deb "
                "topildi? (2) O'lchangan nuqson "
                "asosidagi hisob (measured imperfection "
                "approach) va ehtimollik yondashuvini "
                "tahlil qiling. (3) Sferik qobiq nima "
                "uchun silindrdan ham sezgir ekanini "
                "asoslang: $\\sigma_{cl}$ bir xil, "
                "lekin sferada tajriba 10–20 % beradi. "
                "(4) Mustahkamlangan (stringer, izogrid) "
                "qobiqlarda modal to'planish qanday "
                "yo'qotilishini sonli ko'rsating."
            ),
            manim_ref=manim(
                scene="ShellBucklingScene",
                module="animatsiya/scenes/pq_shells.py",
                title="Qobiq ustuvorligi va nuqsonlarga sezgirlik",
                summary=(
                    "Ideal silindr siqiladi va kritik "
                    "nuqtada romb shaklidagi buzilish "
                    "paydo bo'ladi. Keyin kichik nuqson "
                    "kiritiladi va buzilish ancha past "
                    "yuklamada sodir bo'ladi. Muvozanat "
                    "yo'llari yonma-yon ko'rsatiladi: "
                    "plastina uchun ko'tariluvchi, qobiq "
                    "uchun pasayuvchi."
                ),
            ),
        ),
    ),

    # ------------------------------------------------------------------ pq-30
    Topic(
        id="pq-30",
        subject_id=S, module_id=M, order=30,
        title="Qobiqlar tebranishlari va Donnell tenglamalari; fanning yakuni",
        description=(
            "Donnell–Mushtari tenglamalari, membrana va egilish "
            "energiyalarining bog'lanishi, chastota spektrining "
            "g'ayrioddiy tartibi, minimal chastota va fanning yakuni."
        ),
        learning_objective=(
            "Silindrik qobiqning xususiy chastotalarini hisoblash, "
            "spektrning plastinadan farqini tushuntirish va minimal "
            "chastotaga mos to'lqin sonini topish."
        ),
        prerequisites=["pq-29", "pq-22"],
        mathematical_core=(
            "Donnell tenglamasi $D\\nabla^8w + Eh\\dfrac{\\partial^4w}"
            "{\\partial x^4}/R^2 + \\rho h\\nabla^4\\ddot w = 0$, "
            "$\\Omega^2 = \\dfrac{(1-\\nu^2)\\alpha^4}{(\\alpha^2+"
            "\\beta^2)^2} + \\dfrac{h^2(\\alpha^2+\\beta^2)^2}{12R^2}$."
        ),
        engineering_application=(
            "Raketa va aviatsiya konstruksiyalarida akustik yuklama, "
            "quvurlarda oqim tebranishlari, kompressor korpuslari, "
            "reaktor ichki qurilmalari, shovqin nazorati."
        ),
        computational_component=(
            "Chastota spektrini $(m, n)$ bo'yicha hisoblash, minimal "
            "chastotani topish va uni plastina spektri bilan solishtirish."
        ),
        visualization_component=(
            "Chastota spektri $(m, n)$ tekisligida, minimal chastota "
            "nuqtasi, tebranish shakllari va plastina bilan taqqoslash."
        ),
        research_extension=(
            "Qobiq chastota spektrining eng past chastotasi nima uchun "
            "$n = 1$ da emas? Suyuqlik bilan to'ldirilgan qobiqning "
            "qo'shilgan massa effektini va oqim tufayli yuzaga keluvchi "
            "beqarorlikni o'rganing."
        ),
        difficulty="ilg'or",
        previous_link=(
            "pq-22 da plastina tebranishlari o'rganildi va spektr "
            "muntazam tartibda ekani ko'rsatildi: $f_{11} < f_{21} "
            "< f_{12}$. Qobiqda membrana energiyasi qo'shilgani "
            "uchun spektr butunlay boshqacha tartiblanadi — "
            "pq-29 dagi ikki hadli tuzilma bu yerda ham qaytariladi."
        ),
        next_topic="su-01",
        estimated_minutes=95,
        tags=["tebranish", "Donnell", "chastota spektri", "yakun"],
        lesson=_lesson(
            problem=(
                "Raketa uchirilishida dvigatel akustik "
                "yuklamasi 140–160 dB ga yetadi va u keng "
                "chastota diapazonini qamrab oladi. Bak "
                "qobig'ining xususiy chastotalari shu "
                "diapazonga tushsa, rezonans "
                "konstruksiyani bir necha soniyada "
                "buzishi mumkin. Demak spektrni bilish "
                "shart. Lekin plastinadagi tajribaga "
                "tayanib eng past chastota eng sodda "
                "shaklda ($m = 1$, $n = 1$) bo'ladi deb "
                "o'ylash — jiddiy xato. Qobiqda eng past "
                "chastota ko'pincha $n = 5{\\ldots}10$ "
                "da yotadi, ya'ni qobiq gullaguldek "
                "ko'p to'lqinli shaklda tebranadi. "
                "Nima uchun?"
            ),
            concepts=[
                c("Donnell–Mushtari tenglamalari",
                  "Yupqa silindrik qobiq uchun "
                  "soddalashtirilgan tenglamalar; egilish "
                  "va membrana holatlari kuch funksiyasi "
                  "orqali bog'langan."),
                c("Chastota parametri $\\Omega$",
                  "$\\Omega^2 = \\rho(1-\\nu^2)R^2\\omega^2/E$ — "
                  "o'lchamsiz chastota; qobiq "
                  "tebranishlarini taqqoslash uchun."),
                c("Ikki hadli chastota tuzilmasi",
                  "$\\Omega^2$ da membrana hadi "
                  "($n$ oshsa kamayadi) va egilish hadi "
                  "($n$ oshsa ortadi) — ularning "
                  "raqobati minimum hosil qiladi."),
                c("Minimal chastota va $n_{min}$",
                  "Spektrning eng past nuqtasi $n = 1$ da "
                  "emas; $n_{min}$ odatda 5–10 oralig'ida "
                  "va u $R/h$ ga bog'liq."),
                c("Tebranish shakllarining zichligi",
                  "Qobiqda chastotalar tor oraliqda "
                  "to'planadi — pq-29 dagi modal "
                  "to'planishning dinamik ko'rinishi."),
                c("Halqa (breathing) rejimi",
                  "$n = 0$ — o'qsimmetrik nafas olish "
                  "rejimi; chastotasi "
                  "$\\omega_0 = \\sqrt{E/(\\rho R^2(1-\\nu^2))}$ "
                  "va u spektrning yuqori qismida."),
            ],
            derivation=[
                d("1. Donnell tenglamasi (tebranish uchun)",
                  r"D\nabla^8 w + \frac{Eh}{R^2}"
                  r"\frac{\partial^4 w}{\partial x^4} + "
                  r"\rho h\,\nabla^4\ddot w = 0",
                  "pq-29 dagi ustuvorlik tenglamasining "
                  "dinamik ko'rinishi: $N_x\\,w_{,xx}$ "
                  "o'rniga inersiya hadi turibdi. "
                  "$\\nabla^8$ — membrana va egilishning "
                  "bog'lanishidan."),
                d("2. Yechim shakli",
                  r"w = W\sin\frac{m\pi x}{L}"
                  r"\cos n\theta\,e^{i\omega t}",
                  "Sharnirli tayanchlar uchun aniq yechim. "
                  "$\\alpha = m\\pi/L$, $\\beta = n/R$ "
                  "deb belgilaymiz (pq-29 dagi kabi)."),
                d("3. Qo'yib, chastota tenglamasini olish",
                  r"D(\alpha^2+\beta^2)^4 + \frac{Eh}{R^2}"
                  r"\alpha^4 = \rho h\,\omega^2"
                  r"(\alpha^2+\beta^2)^2",
                  "$\\nabla^8 \\to (\\alpha^2+\\beta^2)^4$, "
                  "$\\nabla^4 \\to (\\alpha^2+\\beta^2)^2$. "
                  "Har bir $(m,n)$ uchun bitta chastota."),
                d("4. Chastotani ajratish",
                  r"\omega^2 = \frac{D(\alpha^2+\beta^2)^2}"
                  r"{\rho h} + \frac{E\alpha^4}"
                  r"{\rho R^2(\alpha^2+\beta^2)^2}",
                  "**Ikkita raqobatlashuvchi had.** "
                  "Birinchisi — sof egilish (plastinadagi "
                  "kabi, pq-22), ikkinchisi — membrana "
                  "hissasi (faqat qobiqda)."),
                d("5. Ixcham belgilashlar",
                  r"\omega^2 = A\,S^2 + \frac{B}{S^2}, \quad "
                  r"S = \alpha^2+\beta^2, \ "
                  r"A = \frac{D}{\rho h}, \ "
                  r"B = \frac{E\alpha^4}{\rho R^2}",
                  "Tuzilma endi aniq ko'rinadi: $A$-had "
                  "$\\beta$ (ya'ni $n$) oshsa **ortadi** "
                  "(egilish), $B$-had **kamayadi** "
                  "(membrana). Klassik $A u + B/u$ "
                  "ko'rinishi."),
                d("6. Minimumning mavjudligi",
                  r"\frac{\partial\omega^2}{\partial S^2} = 0 "
                  r"\;\Longrightarrow\; S^4 = \frac{B}{A} = "
                  r"\frac{12(1-\nu^2)\alpha^4}{h^2R^2}",
                  "**Hal qiluvchi natija.** Ikki hadning "
                  "raqobati oraliq $n$ da minimum beradi. "
                  "Plastinada bunday raqobat yo'q — "
                  "u yerda faqat $A$-had bor va chastota "
                  "$n$ bilan monoton o'sadi."),
                d("7. Minimal chastotaga mos to'lqin soni",
                  r"(\alpha^2+\beta^2)_{min} = "
                  r"\frac{[12(1-\nu^2)]^{1/4}\sqrt{\alpha}}"
                  r"{\sqrt{Rh}}\cdot\sqrt{\alpha}\,, \quad "
                  r"n_{min} = R\sqrt{S_{min} - \alpha^2}",
                  "$S_{min} \\propto \\alpha/\\sqrt{Rh}$, "
                  "demak $n_{min}$ $R/h$ ning kvadrat "
                  "ildizi tartibida o'sadi. Misolimizda "
                  "($R/h = 600$, $L = 6$ m) kod "
                  "$n_{min} = 6{,}39$ beradi."),
                d("8. Minimal chastota qiymati",
                  r"\omega^2_{min} = 2\sqrt{AB} = "
                  r"\frac{\alpha^2 Eh}{\rho R\sqrt{3(1-\nu^2)}}",
                  "Ikki had teng bo'lganda (AM–GM). "
                  "$\\beta$ uzluksiz deb olingandagi quyi "
                  "chegara; haqiqiy $n$ butun bo'lgani "
                  "uchun sal yuqoriroq."),
                d("8a. Ustuvorlik bilan bog'lanish",
                  r"\omega_{min} = \alpha\sqrt{\frac{\sigma_{cl}}"
                  r"{\rho}}, \qquad \sigma_{cl} = "
                  r"\frac{Eh}{R\sqrt{3(1-\nu^2)}}",
                  "**Kutilmagan va nafis natija.** "
                  "8-qadamdagi ifodada aynan pq-29 dagi "
                  "klassik kritik kuchlanish paydo "
                  "bo'ladi. Ya'ni qobiqning minimal "
                  "tebranish chastotasi uning buzilish "
                  "kuchlanishi bilan bevosita "
                  "bog'langan. Tasodif emas: ikkala "
                  "masala ham bir xil Donnell "
                  "operatoridan kelib chiqadi va "
                  "ikkalasida ham minimum egilish "
                  "bilan membrana hadlari tenglashgan "
                  "nuqtada yotadi. Kodda bu "
                  "0,00 % farq bilan tasdiqlanadi."),
                d("9. Halqa (breathing) rejimi $n = 0$, "
                  "$\\alpha \\to 0$",
                  r"\Omega^2 \to (1-\nu^2) "
                  r"\;\Longrightarrow\; \omega_0 = "
                  r"\frac{1}{R}\sqrt{\frac{E}{\rho}}",
                  "Sof o'qsimmetrik kengayish-qisqarish. "
                  "Chastota faqat $R$ ga va tovush "
                  "tezligiga bog'liq — qalinlikka emas. "
                  "U spektrning **yuqori** qismida yotadi."),
                d("10. Spektrning zichligi",
                  r"\text{tor } \Delta\Omega \text{ ichida "
                  r"ko'p } (m,n) \text{ juftlik}",
                  "pq-29 dagi modal to'planishning "
                  "dinamik ko'rinishi. Akustik yuklama "
                  "keng diapazonli bo'lgani uchun u "
                  "bir vaqtda o'nlab rejimni "
                  "qo'zg'atadi — shuning uchun qobiq "
                  "konstruksiyalarda akustik charchoq "
                  "alohida muammo."),
            ],
            meaning=(
                "Qobiq tebranishlari plastina "
                "tebranishlaridan (pq-22) sifat jihatdan "
                "farq qiladi va farqning manbai 4-qadamda: "
                "chastota ifodasida **ikkita "
                "raqobatlashuvchi had** bor. Egilish hadi "
                "to'lqin soni oshgani sari ortadi — bu "
                "intuitiv, chunki mayda to'lqinlar ko'proq "
                "egilish talab qiladi. Membrana hadi esa "
                "aksincha kamayadi: aylana bo'ylab ko'p "
                "to'lqinli shaklda qobiq cho'zilmasdan, "
                "deyarli faqat egilib deformatsiyalana "
                "oladi (inextensional deformatsiya, "
                "pq-25). Ikki hadning raqobati oraliq "
                "$n$ da minimum hosil qiladi va bu "
                "qobiq dinamikasining eng g'ayrioddiy "
                "xususiyati: **eng past chastota eng "
                "sodda shaklga mos kelmaydi**. Bu xuddi "
                "pq-29 dagi ustuvorlik masalasining "
                "tuzilmasi — u yerda ham ikkita had "
                "(egilish va membrana) raqobatlashib "
                "minimum bergan edi. Tasodif emas: "
                "ikkala masala ham bir xil Donnell "
                "operatoridan kelib chiqadi. Amaliy "
                "oqibatlari jiddiy. Birinchidan, "
                "rezonansdan qochish uchun faqat "
                "$n = 1$ ni tekshirish yetarli emas — "
                "butun spektrni skanerlash kerak. "
                "Ikkinchidan, chastotalar tor oraliqda "
                "to'planadi va keng diapazonli akustik "
                "yuklama ularning o'nlabini bir vaqtda "
                "qo'zg'atadi; natijada akustik charchoq "
                "raketa va aviatsiya konstruksiyalarida "
                "alohida hisob talab qiladi. Uchinchidan, "
                "halqa rejimi $\\omega_0 = "
                "\\sqrt{E/\\rho}/R$ — bu materialdagi "
                "tovush tezligini radiusga bo'lgan "
                "nisbat, ya'ni qobiq atrofini "
                "aylanib chiquvchi to'lqinning "
                "chastotasi. U qalinlikka umuman "
                "bog'liq emas va spektrning yuqori "
                "qismida yotadi."
            ),
            equations=[
                eq(r"\omega^2 = \frac{D(\alpha^2+\beta^2)^2}"
                   r"{\rho h} + \frac{E\alpha^4}"
                   r"{\rho R^2(\alpha^2+\beta^2)^2}",
                   "Silindrik qobiqning xususiy chastotasi: "
                   "egilish va membrana hadlari.",
                   "Chastota tenglamasi"),
                eq(r"S^4_{min} = \frac{12(1-\nu^2)\alpha^4}"
                   r"{h^2R^2}, \quad S = \alpha^2+\beta^2, \ "
                   r"\alpha = \frac{m\pi}{L}, \ \beta = \frac{n}{R}",
                   "Minimal chastotaga mos to'lqin soni "
                   "sharti (o'lchamli belgilashda).",
                   "Minimum sharti"),
                eq(r"\omega_{min} = \alpha\sqrt{\frac{\sigma_{cl}}"
                   r"{\rho}}, \qquad \sigma_{cl} = "
                   r"\frac{Eh}{R\sqrt{3(1-\nu^2)}}",
                   "Minimal chastotaning pq-29 dagi "
                   "klassik kritik kuchlanish bilan "
                   "bog'lanishi.",
                   "Tebranish–ustuvorlik bog'lanishi"),
                eq(r"\omega_0 = \frac{1}{R}\sqrt{\frac{E}{\rho}}",
                   "Halqa (breathing) rejimi $n = 0$; "
                   "qalinlikka bog'liq emas.",
                   "Halqa rejimi"),
                eq(r"\Omega^2_{min} = \frac{\sqrt{1-\nu^2}\,"
                   r"\alpha^2 h}{\sqrt{3}\,R}",
                   "Ikki had teng bo'lgandagi minimal "
                   "chastota (uzluksiz $\\beta$ uchun "
                   "quyi chegara).", "Minimal chastota"),
            ],
            conditions=(
                "**Chegaraviy shartlar:** yuqoridagi aniq "
                "yechim ikkala chekkasi sharnirli "
                "(shear diaphragm) qobiq uchun. Boshqa "
                "shartlarda:\n"
                "- Mahkamlangan–mahkamlangan: "
                "chastotalar ~10–20 % yuqori;\n"
                "- Erkin–erkin: pastroq va qo'shimcha "
                "nol chastotali qattiq jism rejimlari;\n"
                "- Konsol: eng past.\n\n"
                "**Donnell taqribining chegarasi:** "
                "$n$ kichik bo'lganda ($n \\le 2$) "
                "Donnell tenglamalari sezilarli xato "
                "beradi — Flügge yoki Sanders "
                "tenglamalari kerak. Kodda bu ochiq "
                "ko'rsatiladi.\n\n"
                "**Boshlang'ich shartlar** (majburiy "
                "tebranish uchun, pq-23 dagi kabi): "
                "$w(x,\\theta,0)$ va "
                "$\\dot w(x,\\theta,0)$ modal "
                "koordinatalarga yoyiladi.\n\n"
                "**Qo'shilgan massa:** suyuqlik bilan "
                "to'ldirilgan qobiqda chastotalar "
                "2–3 barobar pasayadi; bu raketa "
                "baklarida hal qiluvchi."
            ),
            worked=WorkedExample(
                statement=(
                    "pq-29 dagi bak: alyuminiy "
                    "$E = 70$ GPa, $\\rho = 2700$ kg/m³, "
                    "$\\nu = 0{,}33$, $R = 1{,}8$ m, "
                    "$h = 3$ mm, $L = 6$ m, ikkala "
                    "chekkasi sharnirli. $m = 1$ uchun "
                    "$n = 1, 5, 10$ chastotalarini, "
                    "minimal chastotani va halqa "
                    "rejimini toping."
                ),
                given=[
                    r"E = 70\ \text{GPa},\ \rho = 2700\ "
                    r"\text{kg/m}^3,\ \nu = 0{,}33",
                    r"R = 1{,}8\ \text{m},\ h = 0{,}003\ "
                    r"\text{m},\ L = 6\ \text{m}",
                ],
                steps=[
                    st(r"\alpha = \frac{\pi}{L} = "
                       r"\frac{3{,}1416}{6} = 0{,}5236\ "
                       r"\text{m}^{-1}, \quad \beta = "
                       r"\frac{n}{R} = \frac{n}{1{,}8}",
                       "$m = 1$ uchun o'q bo'ylab to'lqin "
                       "soni."),
                    st(r"D = \frac{70\times10^{9} \cdot "
                       r"2{,}7\times10^{-8}}{12 \cdot 0{,}8911} "
                       r"= 176{,}8\ \text{N·m}, \quad "
                       r"\rho h = 8{,}1\ \text{kg/m}^2",
                       "$h^3 = 2{,}7\\times10^{-8}$ m³, "
                       "$12(1-\\nu^2) = 10{,}693$."),
                    st(r"n = 1: \ \beta = 0{,}5556, \ "
                       r"\alpha^2+\beta^2 = 0{,}2742 + "
                       r"0{,}3086 = 0{,}5828\ \text{m}^{-2}",
                       "Ikkala to'lqin soni ham kichik."),
                    st(r"\omega^2 = \frac{176{,}8 \cdot "
                       r"0{,}3397}{8{,}1} + \frac{70\times"
                       r"10^{9} \cdot 0{,}07518}"
                       r"{2700 \cdot 3{,}24 \cdot 0{,}3397}",
                       "Birinchi had 7,41, ikkinchi had "
                       "$1{,}770\\times10^{6}$ — "
                       "**membrana hadi butunlay "
                       "ustun**."),
                    st(r"\omega = 1330\ \text{rad/s} "
                       r"\;\Rightarrow\; f = 211{,}7\ \text{Hz}",
                       "$n = 1$ da chastota yuqori, "
                       "chunki bu shaklda qobiq "
                       "cho'zilishi kerak."),
                    st(r"n = 6: \ \beta = 3{,}3333, \ "
                       r"S = 0{,}2742 + 11{,}111 = "
                       r"11{,}385\ \text{m}^{-2}",
                       "Aylana bo'ylab 6 to'lqin."),
                    st(r"\omega^2 = \frac{176{,}75 \cdot "
                       r"129{,}6}{8{,}1} + \frac{70\times"
                       r"10^{9} \cdot 0{,}075185}"
                       r"{2700 \cdot 3{,}24 \cdot 129{,}6} "
                       r"= 2829 + 4639",
                       "Egilish hadi 2829, membrana hadi "
                       "4639 — ular endi **bir xil "
                       "tartibda** (38 % / 62 %). "
                       "$n = 1$ da membrana hadi "
                       "mingtalab barobar ustun edi."),
                    st(r"\omega = \sqrt{7468} = 86{,}4\ "
                       r"\text{rad/s} \;\Rightarrow\; "
                       r"f = 13{,}75\ \text{Hz}",
                       "$n = 1$ dagidan **15,4 barobar "
                       "past** — spektr monoton emas."),
                    st(r"\text{Minimum: } S^4 = "
                       r"\frac{12(1-\nu^2)\alpha^4}{h^2R^2} "
                       r"\;\Rightarrow\; S_{min} = 12{,}885, "
                       r"\ n_{min} = R\sqrt{S_{min}-\alpha^2} "
                       r"= 6{,}39",
                       "6-qadamdagi shart. $n$ butun "
                       "bo'lishi kerak, shuning uchun "
                       "haqiqiy minimum $n = 6$ da "
                       "(13,75 Hz); uzluksiz baho "
                       "13,55 Hz — farq 1,5 %."),
                    st(r"\omega_{min} = \alpha\sqrt{\frac"
                       r"{\sigma_{cl}}{\rho}} = 0{,}5236"
                       r"\sqrt{\frac{71{,}355\times10^{6}}"
                       r"{2700}} = 0{,}5236 \cdot 162{,}6 "
                       r"= 85{,}1\ \text{rad/s}",
                       "8a-qadamdagi bog'lanish: pq-29 "
                       "dagi $\\sigma_{cl} = 71{,}355$ MPa "
                       "orqali. $f = 13{,}55$ Hz — "
                       "yuqoridagi uzluksiz baho bilan "
                       "aynan bir xil."),
                    st(r"\text{Halqa rejimi: } \omega_0 = "
                       r"\frac{1}{1{,}8}\sqrt{\frac{70\times"
                       r"10^{9}}{2700}} = \frac{5091{,}8}"
                       r"{1{,}8} = 2828{,}8\ \text{rad/s}",
                       "$f_0 = 450{,}2$ Hz — spektrning "
                       "**yuqori** qismida, minimal "
                       "chastotadan 32,7 barobar "
                       "baland. Tovush tezligi "
                       "$\\sqrt{E/\\rho} = 5091{,}8$ m/s."),
                ],
                answer=(
                    "$m = 1$ uchun: $f(n=1) = 211{,}8$ Hz, "
                    "$f(n=6) = 13{,}75$ Hz — ya'ni "
                    "murakkabroq shakl **15,4 barobar "
                    "past** chastotaga ega. Minimum "
                    "$n_{min} = 6{,}39$ (butun $n = 6$), "
                    "uzluksiz baho 13,55 Hz. Bu qiymat "
                    "$\\omega_{min} = \\alpha"
                    "\\sqrt{\\sigma_{cl}/\\rho}$ "
                    "bog'lanishi orqali pq-29 dagi "
                    "klassik kritik kuchlanishdan ham "
                    "olinadi. Halqa rejimi "
                    "$f_0 = 450{,}2$ Hz. Spektr "
                    "plastinadagidek monoton emas."
                ),
                engineering_note=(
                    "Bu natija loyihalash amaliyotini "
                    "bevosita o'zgartiradi. Plastinada "
                    "rezonansni tekshirish uchun "
                    "$f_{11}$ ni hisoblash kifoya edi — "
                    "u eng past va qolganlari undan "
                    "yuqori. Qobiqda esa $f(n=1)$ ni "
                    "hisoblab, uni eng past deb qabul "
                    "qilish 15 barobar xatoga olib "
                    "keladi va konstruksiya "
                    "rezonansga tushadi. Shuning uchun "
                    "qobiq dinamikasida har doim "
                    "$(m, n)$ bo'yicha to'liq skanerlash "
                    "bajariladi. Suyuqlik bilan "
                    "to'ldirilgan bakda vaziyat yanada "
                    "murakkab: qo'shilgan massa "
                    "chastotalarni 2–3 barobar "
                    "pasaytiradi va $n_{min}$ ni "
                    "siljitadi, shuning uchun bo'sh va "
                    "to'la holat alohida tekshiriladi. "
                    "Raketa uchirilishida bak "
                    "bo'shagani sari uning spektri "
                    "uzluksiz o'zgaradi — bu POGO "
                    "beqarorligining bir sababidir."
                ),
            ),
            computation=Computation(
                caption=(
                    "Qobiq chastota spektrini $(m, n)$ "
                    "bo'yicha hisoblash, minimal "
                    "chastotani topish va plastina "
                    "spektri bilan taqqoslash."
                ),
                code='''"""Silindrik qobiq tebranishlari: Donnell spektri."""
import numpy as np
from labkit import PARAMS, note, series, table, value

E = float(PARAMS.get("E", 70.0))*1e9
rho = float(PARAMS.get("rho", 2700.0))
nu = float(PARAMS.get("nu", 0.33))
R = float(PARAMS.get("R", 1800.0))/1000.0
h = float(PARAMS.get("h", 3.0))/1000.0
L = float(PARAMS.get("L", 6.0))
m_show = int(PARAMS.get("m_show", 1))
n_max = int(PARAMS.get("n_max", 30))

D = E*h**3/(12*(1 - nu**2))
mu = rho*h
value("Silindrik bikrlik D", D, "N*m")
value("Yuza zichligi rho*h", mu, "kg/m^2")
value("R/h nisbati", R/h, "—")


def omega2(m, n):
    al = m*np.pi/L
    be = n/R
    s2 = al**2 + be**2
    bend = D*s2**2/mu                      # egilish hadi
    memb = E*al**4/(rho*R**2*s2**2)        # membrana hadi
    return bend + memb, bend, memb


# --- m = m_show uchun spektr ---
ns = np.arange(0, n_max + 1)
fs, fb, fm = [], [], []
for n in ns:
    w2, bd, mb = omega2(m_show, n)
    fs.append(np.sqrt(w2)/(2*np.pi))
    fb.append(np.sqrt(bd)/(2*np.pi))
    fm.append(np.sqrt(mb)/(2*np.pi))
series(f"Chastota f(n), m = {m_show}", ns.tolist(), fs,
       xlabel="aylana to'lqin soni n", ylabel="f, Hz")
series("Faqat egilish hissasi", ns.tolist(), fb,
       xlabel="aylana to'lqin soni n", ylabel="f, Hz")
series("Faqat membrana hissasi", ns.tolist(), fm,
       xlabel="aylana to'lqin soni n", ylabel="f, Hz")

i_min = int(np.argmin(fs))
value(f"Minimal chastota (m = {m_show})", fs[i_min], "Hz")
value("Unga mos n", float(ns[i_min]), "—")
value("f(n = 1)", fs[1], "Hz")
value("f(n = 1) / f_min", fs[1]/fs[i_min], "marta")
note(f"m = {m_show} uchun eng past chastota n = {ns[i_min]} da "
     f"({fs[i_min]:.2f} Hz), n = 1 da esa {fs[1]:.2f} Hz - "
     f"{fs[1]/fs[i_min]:.2f} barobar yuqori. Ya'ni ENG SODDA "
     f"SHAKL eng past chastotani BERMAYDI. Plastinada bu "
     f"mumkin emas edi (pq-22).")

# Ikki hadning almashinuvi
w2b, bd_b, mb_b = omega2(m_show, int(ns[i_min]))
value("Minimumda egilish hadi ulushi", bd_b/(bd_b + mb_b)*100, "%")
value("Minimumda membrana hadi ulushi", mb_b/(bd_b + mb_b)*100, "%")
note(f"Butun n = {ns[i_min]} dagi minimumda egilish va membrana "
     f"hadlari bir xil tartibda ({bd_b/(bd_b+mb_b)*100:.1f} % va "
     f"{mb_b/(bd_b+mb_b)*100:.1f} %) - ya'ni minimum aynan ularning "
     f"RAQOBATIDAN tug'iladi. Quyida uzluksiz optimumda ular aynan "
     f"teng bo'lishi ko'rsatiladi.")

# Qaysi n da hadlar o'rin almashadi
cross = None
for n in range(1, n_max + 1):
    _, bd1, mb1 = omega2(m_show, n)
    _, bd2, mb2 = omega2(m_show, n + 1)
    if (bd1 - mb1)*(bd2 - mb2) < 0:
        cross = n
        break
if cross is not None:
    value("Hadlar teng bo'ladigan n", float(cross), "—")
    note(f"n < {cross} da MEMBRANA hadi ustun (qobiq cho'zilishi "
         f"kerak), n > {cross} da EGILISH hadi ustun (qobiq "
         f"cho'zilmasdan egiladi). Raqobat shu yerda almashadi.")

# --- Uzluksiz beta bo'yicha analitik minimum ---
# omega^2 = A*S^2 + B/S^2,  A = D/(rho*h),  B = E*al^4/(rho*R^2)
#   => S^4 = B/A = 12*(1-nu^2)*al^4/(h^2*R^2),  omega^2_min = 2*sqrt(A*B)
al = m_show*np.pi/L
Acf = D/mu
Bcf = E*al**4/(rho*R**2)
s2_opt = (Bcf/Acf)**0.25
s2_opt_alt = (12*(1 - nu**2)*al**4/(h**2*R**2))**0.25
value("S_opt (B/A orqali)", s2_opt, "1/m^2")
value("S_opt (12(1-nu^2)a^4/(h^2R^2) orqali)", s2_opt_alt, "1/m^2")
value("Ikki yo'l farqi", abs(s2_opt - s2_opt_alt)/s2_opt*100, "%")

be2_opt = s2_opt - al**2
if be2_opt > 0:
    n_opt = np.sqrt(be2_opt)*R
    value("n_min (analitik, uzluksiz)", float(n_opt), "—")
    w2_opt = 2*np.sqrt(Acf*Bcf)
    f_opt = np.sqrt(w2_opt)/(2*np.pi)
    value("f_min (analitik, uzluksiz)", f_opt, "Hz")
    value("Sonli va analitik f_min farqi",
          abs(fs[i_min] - f_opt)/f_opt*100, "%")
    note(f"Uzluksiz beta bo'yicha analitik minimum n = {n_opt:.2f} da "
         f"{f_opt:.2f} Hz beradi; butun n bo'yicha sonli qidiruv "
         f"n = {ns[i_min]} da {fs[i_min]:.2f} Hz - farq "
         f"{abs(fs[i_min]-f_opt)/f_opt*100:.2f} %. Analitik n_min "
         f"butun emas va sonli minimum unga eng yaqin butun son "
         f"atrofida yotadi; yaxlitlash chastotani sal KO'TARADI, "
         f"bu kutilgan natija.")

    # AM-GM tengligini aynan optimumda tekshirish
    bend_opt = Acf*s2_opt**2
    memb_opt = Bcf/s2_opt**2
    value("Optimumda egilish hadi ulushi",
          bend_opt/(bend_opt + memb_opt)*100, "%")
    value("Optimumda membrana hadi ulushi",
          memb_opt/(bend_opt + memb_opt)*100, "%")
    # pq-29 bilan bog'lanish: omega_min^2 = al^2*sigma_cl/rho
    sig_cl = E*h/(R*np.sqrt(3*(1 - nu**2)))
    w2_link = al**2*sig_cl/rho
    value("sigma_cl (pq-29 dagi klassik kuchlanish)", sig_cl/1e6, "MPa")
    value("omega_min^2 (al^2*sigma_cl/rho orqali)", w2_link, "1/s^2")
    value("omega_min^2 (2*sqrt(A*B) orqali)", w2_opt, "1/s^2")
    value("Bog'lanish xatosi", abs(w2_link - w2_opt)/w2_opt*100, "%")
    note(f"AJOYIB BOG'LANISH: minimal chastota aynan "
         f"omega_min = alpha*sqrt(sigma_cl/rho) ga teng, bu yerda "
         f"sigma_cl - pq-29 dagi KLASSIK KRITIK KUCHLANISH "
         f"({sig_cl/1e6:.2f} MPa). Ikki yo'l "
         f"{abs(w2_link-w2_opt)/w2_opt:.2e} % farq qiladi. Sababi: "
         f"ustuvorlik va tebranish masalalari bir xil Donnell "
         f"operatoridan kelib chiqadi va ikkalasida ham egilish "
         f"bilan membrana hadlari AYNAN SHU nuqtada tenglashadi.")

    note(f"AYNAN optimumda (uzluksiz S) ikki had TENG: "
         f"{bend_opt/(bend_opt+memb_opt)*100:.4f} % va "
         f"{memb_opt/(bend_opt+memb_opt)*100:.4f} % - bu AM-GM "
         f"tengligining aniq tasdig'i. Butun n = {ns[i_min]} da esa "
         f"ulushlar {bd_b/(bd_b+mb_b)*100:.1f} % / "
         f"{mb_b/(bd_b+mb_b)*100:.1f} % ga siljiydi, chunki n "
         f"optimal {n_opt:.2f} dan biroz chetda.")

# --- Halqa (breathing) rejimi ---
w0 = np.sqrt(E/(rho*R**2*(1 - nu**2)))*np.sqrt(1 - nu**2)
f0 = w0/(2*np.pi)
value("Halqa rejimi f0", f0, "Hz")
value("Tovush tezligi sqrt(E/rho)", np.sqrt(E/rho), "m/s")
value("f0 / f_min", f0/fs[i_min], "marta")
note(f"Halqa rejimi f0 = {f0:.1f} Hz = sqrt(E/rho)/(2*pi*R) va u "
     f"qalinlikka BOG'LIQ EMAS. U minimal chastotadan "
     f"{f0/fs[i_min]:.1f} barobar yuqori - ya'ni spektrning "
     f"yuqori qismida.")

# --- To'liq spektr (m, n) ---
spec = []
for m in range(1, 11):
    for n in range(0, n_max + 1):
        w2, _, _ = omega2(m, n)
        spec.append((np.sqrt(w2)/(2*np.pi), m, n))
spec.sort()
rows = [[f"{s[1]}", f"{s[2]}", f"{s[0]:.2f}"] for s in spec[:10]]
table("Eng past o'nta chastota (m, n)",
      ["m (o'q)", "n (aylana)", "f, Hz"], rows)

f_low = spec[0][0]
dense = [s for s in spec if s[0] < 2*f_low]
value("Eng past chastota", f_low, "Hz")
value("2*f_min ichidagi rejimlar soni", float(len(dense)), "—")
note(f"Eng past chastota {f_low:.2f} Hz (m = {spec[0][1]}, "
     f"n = {spec[0][2]}). Uning IKKI BARAVARI ichida "
     f"{len(dense)} ta rejim yotadi - spektr juda zich. "
     f"Keng diapazonli akustik yuklama ularning hammasini bir "
     f"vaqtda qo'zg'atadi, shuning uchun akustik charchoq "
     f"qobiq konstruksiyalarida alohida hisob talab qiladi.")

series("Eng past 60 chastota (tartiblangan)",
       list(range(1, 61)), [s[0] for s in spec[:60]],
       xlabel="rejim tartibi", ylabel="f, Hz")

# --- Plastina bilan taqqoslash: bir xil o'lchamdagi panel ---
# Qobiqni yoyib, a = L, b = 2*pi*R bo'lgan sharnirli panel qilamiz
a_p, b_p = L, 2*np.pi*R
plate = []
for m in range(1, 11):
    for n in range(1, 11):
        wp = np.pi**2*np.sqrt(D/mu)*((m/a_p)**2 + (n/b_p)**2)
        plate.append((wp/(2*np.pi), m, n))
plate.sort()
value("Plastina (yoyilgan) eng past chastotasi", plate[0][0], "Hz")
value("Qobiq / plastina nisbati", f_low/plate[0][0], "marta")
note(f"Xuddi shu varaqni YOYIB tekis panel qilsak, eng past "
     f"chastota {plate[0][0]:.3f} Hz bo'lardi; qobiq holatida esa "
     f"{f_low:.2f} Hz - {f_low/plate[0][0]:.0f} barobar yuqori. "
     f"Egrilik qobiqni dinamik jihatdan ham keskin bikrlashtiradi "
     f"(pq-25 dagi statik xulosaning dinamik ko'rinishi).")
p_dense = [s for s in plate if s[0] < 2*plate[0][0]]
value("Plastinada 2*f_min ichidagi rejimlar", float(len(p_dense)), "—")
note(f"Plastinada 2*f_min ichida atigi {len(p_dense)} ta rejim bor, "
     f"qobiqda esa {len(dense)} ta - qobiq spektri ancha zichroq.")

table("Plastina va qobiq tebranishlarining taqqoslashi",
      ["Jihat", "Plastina (pq-22)", "Qobiq (pq-30)"],
      [["Chastota hadlari", "faqat egilish", "egilish + membrana"],
       ["Eng past shakl", "m = n = 1", "n = 5...10"],
       ["Spektr tartibi", "monoton", "minimumli"],
       ["Spektr zichligi", "siyrak", "zich"],
       ["Halqa rejimi", "yo'q", "bor (yuqorida)"],
       ["Asosiy xavf", "rezonans", "akustik charchoq"]])

if int(ns[i_min]) <= 2:
    note("DIQQAT: minimum n <= 2 da chiqdi. Bu oraliqda Donnell "
         "taqribi sezilarli xato beradi - Flugge yoki Sanders "
         "tenglamalarini ishlatish kerak.")
else:
    note(f"Minimum n = {ns[i_min]} > 2 da yotadi, shuning uchun "
         f"Donnell taqribi bu yerda ishonchli (u faqat n <= 2 da "
         f"sezilarli xato beradi).")
''',
                parameters=[
                    p("E", "Yung moduli E", 20.0, 400.0, 70.0, 1.0, "GPa"),
                    p("rho", "Zichlik ρ", 500.0, 20000.0, 2700.0, 50.0,
                      "kg/m³"),
                    p("nu", "Puasson koeffitsienti ν", 0.0, 0.45, 0.33, 0.01),
                    p("R", "Qobiq radiusi R", 100.0, 20000.0, 1800.0, 50.0,
                      "mm"),
                    p("h", "Qalinlik h", 0.5, 50.0, 3.0, 0.1, "mm"),
                    p("L", "Uzunlik L", 0.2, 40.0, 6.0, 0.2, "m"),
                    p("m_show", "Ko'rsatiladigan o'q to'lqini m",
                      1.0, 10.0, 1.0, 1.0),
                    p("n_max", "Maksimal aylana to'lqin soni n",
                      5.0, 60.0, 30.0, 1.0),
                ],
                expected_output=(
                    "m = 1 uchun eng past chastota n = 6 da "
                    "(13,75 Hz), n = 1 da esa 211,8 Hz — 15,4 "
                    "barobar yuqori — eng sodda shakl eng "
                    "past chastotani bermaydi. Uzluksiz S "
                    "bo'yicha optimum ikkita mustaqil "
                    "formuladan 0,00 % farq bilan bir xil "
                    "chiqadi va u yerda egilish/membrana "
                    "ulushlari aynan 50/50 (AM–GM "
                    "tengligi); butun n = 6 da ular "
                    "37,9/62,1 ga siljiydi. Analitik "
                    "n_min = 6,39, f_min = 13,55 Hz, "
                    "sonli qidiruv 13,75 Hz — farq "
                    "1,53 %. Minimal chastota "
                    "ω_min = α√(σ_cl/ρ) bog'lanishi "
                    "orqali pq-29 dagi klassik kritik "
                    "kuchlanishdan (71,355 MPa) 0,00 % "
                    "farq bilan qayta olinadi. Halqa "
                    "rejimi f₀ = 450,2 Hz — minimal "
                    "chastotadan 32,7 barobar baland. "
                    "2·f_min ichida 8 ta rejim yotadi "
                    "(plastinada 2 ta); xuddi shu "
                    "varaqni yoyib tekis panel qilsak "
                    "chastota 0,261 Hz ga tushadi — "
                    "53 barobar past."
                ),
            ),
            visual=vis(
                kind="Qobiq chastota spektri va minimum",
                tool="React/SVG + Manim",
                description=(
                    "Chastotaning $n$ ga bog'liqligi, "
                    "ikki hadning raqobati va spektr "
                    "zichligi."
                ),
                how_to_draw=(
                    "React/SVG: asosiy panel — "
                    "$f(n)$ egri chizig'i berilgan $m$ "
                    "uchun. Uning ustiga **ikkita "
                    "tashkil etuvchi** alohida "
                    "chiziladi: egilish hissasi "
                    "(o'suvchi) va membrana hissasi "
                    "(kamayuvchi), ikkalasi ham punktir. "
                    "Ularning kesishgan joyi va to'liq "
                    "chiziqning minimumi bir-biriga "
                    "yaqin ekani ko'rinadi — bu "
                    "6-qadamning vizual isboti. Minimum "
                    "nuqtasi ajratib belgilanadi va "
                    "$n_{min}$ yoziladi; $n = 1$ nuqtasi "
                    "ham belgilanib, ikkisining nisbati "
                    "o'q bilan ko'rsatiladi. Ikkinchi "
                    "panel — tartiblangan spektr "
                    "(rejim tartibi bo'yicha chastota): "
                    "qobiq chizig'i deyarli yassi "
                    "boshlanadi (zich spektr), "
                    "plastinaniki esa tik ko'tariladi; "
                    "$2f_{min}$ darajasi gorizontal "
                    "chiziq bilan va uning ostidagi "
                    "rejimlar soni yozilib qo'yiladi. "
                    "Uchinchi panel — qobiq kesimining "
                    "tebranish shakllari: $n = 1$ "
                    "(siljish), $n = 2$ (ovallashish), "
                    "$n = 6$ (gulsimon) va $n = 0$ "
                    "(halqa) yonma-yon animatsiyalanadi."
                ),
            ),
            interp=(
                "Kodning markaziy natijasi — eng past "
                "chastotaning $n = 1$ da emasligi. Bu "
                "plastina bilan solishtirilganda "
                "ayniqsa keskin ko'rinadi: pq-22 da "
                "spektr monoton edi va $f_{11}$ eng past "
                "bo'lgan; bu yerda esa $n = 1$ dagi "
                "chastota minimaldan bir necha barobar "
                "yuqori. Sababni kod bevosita "
                "ko'rsatadi: minimum nuqtasida egilish "
                "va membrana hadlari deyarli teng "
                "ulushga ega, ya'ni minimum aynan "
                "ularning raqobatidan tug'iladi. "
                "Hadlarning o'rin almashish nuqtasi "
                "ham hisoblanadi va u minimum atrofida "
                "yotadi — bu 6-qadamdagi AM–GM "
                "shartining sonli tasdig'i. Uzluksiz "
                "$\\beta$ bo'yicha analitik minimum "
                "butun $n$ bo'yicha qidiruv bilan "
                "yaqin mos kelishi esa 7- va "
                "8-qadamlardagi formulalarni "
                "tekshiradi; kichik farq faqat $n$ ning "
                "butunligidan kelib chiqadi va u har "
                "doim chastotani **ko'taradi**, bu "
                "kutilgan yo'nalish. Ikkinchi muhim "
                "natija — spektr zichligi: $2f_{min}$ "
                "ichida o'nlab rejim yotadi, "
                "plastinada esa bir nechta. Bu pq-29 "
                "dagi modal to'planishning dinamik "
                "ko'rinishi va u akustik charchoq "
                "muammosini tushuntiradi. Nihoyat, "
                "yoyilgan panel bilan taqqoslash "
                "pq-25 dagi statik xulosani dinamikada "
                "takrorlaydi: egrilik qobiqni "
                "tartiblarga bikrlashtiradi."
            ),
            mistakes=[
                "Eng past chastotani $n = 1$ da izlash. "
                "Qobiqda minimum $n = 5{\\ldots}10$ da; "
                "xato 15 barobargacha yetadi.",
                "Plastina formulalarini qobiqqa qo'llash. "
                "Membrana hadi yo'qotilsa chastota "
                "tartiblarga xato chiqadi.",
                "Donnell taqribini $n \\le 2$ da "
                "ishlatish. U yerda Flügge yoki Sanders "
                "tenglamalari kerak.",
                "Suyuqlik qo'shilgan massasini "
                "unutish. To'ldirilgan bakda "
                "chastotalar 2–3 barobar pasayadi.",
                "Halqa rejimini eng past deb o'ylash. "
                "U aksincha spektrning yuqori qismida "
                "va qalinlikka bog'liq emas.",
            ],
            quiz=[
                q("Nima uchun qobiqda eng past chastota "
                  "$n = 1$ da emas?",
                  "Chastotada ikkita raqobatlashuvchi "
                  "had bor: membrana hadi $n$ oshsa "
                  "kamayadi, egilish hadi ortadi; "
                  "ularning raqobati oraliq $n$ da "
                  "minimum beradi.", "konseptual"),
                q("Minimum nuqtasida ikki had qanday "
                  "nisbatda bo'ladi va nima uchun?",
                  "Ular deyarli teng — AM–GM sharti "
                  "bo'yicha ikki hadning yig'indisi "
                  "ular teng bo'lganda minimal; kodda "
                  "bu ulushlar bilan tasdiqlanadi.",
                  "talqin"),
                q("Halqa rejimining chastotasi nimaga "
                  "bog'liq va nimaga bog'liq emas?",
                  "$\\omega_0 = \\sqrt{E/\\rho}/R$ — "
                  "material tovush tezligiga va "
                  "radiusga bog'liq, **qalinlikka "
                  "bog'liq emas**.", "hisob"),
                q("Kodda '2·f_min ichidagi rejimlar "
                  "soni' nima uchun hisoblanadi?",
                  "U spektr zichligini o'lchaydi; "
                  "zich spektr keng diapazonli akustik "
                  "yuklamada o'nlab rejim bir vaqtda "
                  "qo'zg'atilishini va akustik charchoq "
                  "xavfini bildiradi.", "kod"),
                q("Qobiqni yoyib tekis panel qilsak "
                  "chastota qanday o'zgaradi va nima "
                  "uchun?",
                  "Keskin pasayadi, chunki membrana "
                  "hadi yo'qoladi — egrilik qobiqni "
                  "dinamik jihatdan ham bikrlashtiradi "
                  "(pq-25 dagi statik xulosaning "
                  "dinamik ko'rinishi).", "talqin"),
                q("Raketa bagining spektri uchish "
                  "davomida nima uchun o'zgaradi?",
                  "Yoqilg'i sarflangani sari suyuqlikning "
                  "qo'shilgan massasi kamayadi va "
                  "chastotalar ko'tariladi; shuning "
                  "uchun bo'sh va to'la holat alohida "
                  "tekshiriladi.", "talqin"),
            ],
            bridge=(
                "Plastinalar va qobiqlar nazariyasi "
                "yakunlandi: model, yechim usullari, "
                "doiraviy geometriya, ustuvorlik, "
                "tebranishlar, sdvig tuzatmasi va "
                "qobiqlar. Bu yo'lda bir narsa "
                "takrorlanib turdi — analitik yechim "
                "faqat sodda geometriya va sodda "
                "chegaraviy shartlar uchun mavjud. "
                "Navye qatori faqat to'rt tomoni "
                "sharnirli to'rtburchak uchun, Levi "
                "ikki tomoni sharnirli uchun, "
                "o'qsimmetrik yechim faqat doiraviy "
                "plastina uchun ishladi. Haqiqiy "
                "konstruksiyada esa teshiklar, "
                "qovurg'alar, o'zgaruvchan qalinlik, "
                "murakkab kontur va aralash chegaraviy "
                "shartlar bo'ladi. 5-fan aynan shu "
                "bo'shliqni to'ldiradi: sonli usullar "
                "va hisoblash mexanikasi. Biz allaqachon "
                "ulardan foydalandik — chekli ayirmalar "
                "(pq-10), Ritz va Galerkin (pq-09), "
                "xususiy qiymat masalalari (pq-19, "
                "pq-22), Richardson ekstrapolyatsiyasi "
                "(pq-10) — endi ularni tizimli va "
                "qat'iy asosda quramiz."
            ),
            research=(
                "Qobiq dinamikasining murakkab "
                "masalalarini o'rganing. (1) "
                "Suyuqlik bilan to'ldirilgan qobiqning "
                "qo'shilgan massa koeffitsientini "
                "hisoblang va chastotaning pasayishini "
                "baholang; bo'sh va to'la bakning "
                "spektrini solishtiring. (2) Ichidan "
                "oqim o'tayotgan quvurning "
                "beqarorligini (flutter, divergensiya) "
                "o'rganing va kritik oqim tezligini "
                "toping. (3) Donnell, Sanders va "
                "Flügge tenglamalarini $n = 1, 2, 3$ "
                "uchun taqqoslang va Donnell "
                "taqribining xatosini miqdoriy "
                "aniqlang. (4) POGO beqarorligi "
                "mexanizmini — bak, quvur va dvigatel "
                "tizimining bog'langan tebranishini — "
                "tahlil qiling."
            ),
            manim_ref=manim(
                scene="ShellVibrationScene",
                module="animatsiya/scenes/pq_shells.py",
                title="Qobiq tebranish shakllari va spektr",
                summary=(
                    "Silindrik qobiq kesimi ketma-ket "
                    "$n = 0$ (halqa), $n = 1$ (siljish), "
                    "$n = 2$ (ovallashish) va "
                    "$n = 6$ (gulsimon) shakllarda "
                    "tebranadi; har birining chastotasi "
                    "yoziladi va spektrdagi o'rni "
                    "belgilanadi. Oxirida $f(n)$ egri "
                    "chizig'i ikki tashkil etuvchisi "
                    "bilan birga quriladi va minimum "
                    "ularning kesishuvida paydo "
                    "bo'lishi ko'rsatiladi."
                ),
            ),
        ),
    ),
]
