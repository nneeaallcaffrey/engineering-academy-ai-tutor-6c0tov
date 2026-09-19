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
                module="manim/scenes/pq_shells.py",
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
        difficulty="asosiy",
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
                module="manim/scenes/pq_shells.py",
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
                module="manim/scenes/pq_shells.py",
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
]
