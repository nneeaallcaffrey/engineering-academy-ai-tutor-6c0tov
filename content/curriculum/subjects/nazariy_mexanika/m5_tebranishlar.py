"""NM / 5-modul: Tebranishlar va turg'unlik (nm-25 … nm-30)."""

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
M = "nm-m5"

TOPICS = [
    Topic(
        id="nm-25",
        subject_id=S,
        module_id=M,
        order=25,
        title="Bir erkinlik darajali tizimning erkin tebranishlari",
        description=(
            "Garmonik ossillyator modeli, xususiy chastota, amplituda va faza; "
            "ekvivalent bikrlik va massa tushunchalari."
        ),
        learning_objective=(
            "Real konstruksiyani bir erkinlik darajali modelga keltirish va uning "
            "xususiy chastotasini hisoblash."
        ),
        prerequisites=["nm-22", "nm-15"],
        mathematical_core=(
            "$m\\ddot x + kx = 0$ chiziqli ODE, xarakteristik tenglama, garmonik "
            "yechim, boshlang'ich shartlar."
        ),
        engineering_application=(
            "Mashina fundamenti, vibroizolyatsiya, konsol balkaning tebranishi, "
            "rezonansdan qochish."
        ),
        computational_component=(
            "Xususiy chastotani analitik va sonli (energiya usuli) hisoblash, "
            "ekvivalent bikrlikni topish."
        ),
        visualization_component="Tebranish grafigi va fazaviy portret (ellips).",
        research_extension=(
            "Reley usuli bilan taqsimlangan massali tizimning birinchi chastotasini "
            "baholash — su-14 dagi Ritz usulining eng sodda holi."
        ),
        difficulty="asosiy",
        previous_link=(
            "nm-15 dagi potensial chuqurcha minimumi atrofidagi harakat aynan "
            "garmonik tebranishdir: $\\Pi(x) \\approx \\Pi_0 + \\tfrac{1}{2}\\Pi''x^2$."
        ),
        next_topic="nm-26",
        estimated_minutes=85,
        tags=["tebranish", "xususiy chastota", "garmonik ossillyator"],
        lesson=Lesson(
            physical_problem=(
                "Sanoat ventilyatori fundamentga o'rnatilgan. Ishga tushirishda u "
                "ma'lum aylanishlar sonida kuchli titray boshlaydi, keyin esa "
                "tinchlanadi. Bu 'xavfli tezlik' qayerdan kelib chiqadi va uni "
                "oldindan hisoblash mumkinmi? Javob — tizimning xususiy chastotasida, "
                "va uni topish uchun butun ventilyatorni bitta massa va bitta "
                "prujinaga keltirish kifoya."
            ),
            concepts=[
                c("Xususiy chastota", "$\\omega_0 = \\sqrt{k/m}$ — tizimning 'tabiiy' "
                  "tebranish chastotasi; boshlang'ich shartlarga bog'liq emas."),
                c("Ekvivalent bikrlik", "Murakkab elastik tizimni bitta prujinaga "
                  "keltirish: ketma-ket ulanishda $1/k_{ekv} = \\sum 1/k_i$, "
                  "parallel ulanishda $k_{ekv} = \\sum k_i$."),
                c("Amplituda va boshlang'ich faza", "$x(t) = A\\sin(\\omega_0 t + \\alpha)$; "
                  "$A$ va $\\alpha$ boshlang'ich shartlardan aniqlanadi."),
                c("Statik cho'kish", "$\\delta_{st} = mg/k$; undan "
                  "$\\omega_0 = \\sqrt{g/\\delta_{st}}$ — o'lchash orqali chastotani "
                  "baholashning eng tez usuli."),
            ],
            derivation=[
                d("1-qadam. Lagranj tenglamasidan harakat tenglamasi",
                  r"T = \tfrac{1}{2}m\dot x^2,\quad \Pi = \tfrac{1}{2}kx^2 \;\Rightarrow\; "
                  r"m\ddot x + kx = 0",
                  "nm-22 dagi retsept bo'yicha. Muvozanat holatidan o'lchangan $x$ da "
                  "og'irlik tenglamaga kirmaydi (u statik cho'kish bilan qisqaradi)."),
                d("2-qadam. Yechimni izlash",
                  r"x = Ce^{\lambda t} \Rightarrow (m\lambda^2+k)C = 0 \Rightarrow "
                  r"\lambda_{1,2} = \pm i\sqrt{k/m} = \pm i\omega_0",
                  "Xarakteristik tenglama sof mavhum ildizlarga ega — demak yechim "
                  "so'nmaydigan garmonik tebranish."),
                d("3-qadam. Umumiy yechim",
                  r"\boxed{\;x(t) = A\sin(\omega_0t+\alpha),\qquad \omega_0=\sqrt{k/m}\;}",
                  "$A = \\sqrt{x_0^2 + (v_0/\\omega_0)^2}$, "
                  "$\\tan\\alpha = x_0\\omega_0/v_0$ — boshlang'ich shartlardan."),
                d("4-qadam. Energiya usuli bilan tekshirish",
                  r"T_{max} = \tfrac{1}{2}m\omega_0^2A^2 = \Pi_{max} = \tfrac{1}{2}kA^2 "
                  r"\Rightarrow \omega_0^2 = k/m",
                  "Reley usulining eng sodda holi: maksimal kinetik va potensial "
                  "energiyalarni tenglashtirish. Bu usul taqsimlangan massali "
                  "tizimlarga umumlashadi."),
            ],
            formula_meaning=(
                "$\\omega_0 = \\sqrt{k/m}$ — konstruksiya dinamikasining eng muhim soni. "
                "Massani oshirish chastotani pasaytiradi, bikrlikni oshirish — ko'taradi. "
                "Vibroizolyatsiya aynan shu bilan ishlaydi: mashina chastotasidan "
                "uzoqroq $\\omega_0$ tanlanadi. $\\delta_{st}$ orqali ifodalash esa "
                "amaliy: cho'kishni o'lchab, chastotani darhol baholash mumkin."
            ),
            equations=[
                eq(r"m\ddot x + kx = 0", "Erkin tebranish tenglamasi.", "Ossillyator tenglamasi"),
                eq(r"\omega_0 = \sqrt{k/m} = \sqrt{g/\delta_{st}}", "Xususiy chastota.",
                   "Xususiy chastota"),
                eq(r"x(t) = A\sin(\omega_0 t+\alpha)", "Umumiy yechim.", "Garmonik tebranish"),
            ],
            conditions=(
                "Boshlang'ich shartlar $x(0) = x_0$, $\\dot x(0) = v_0$. Model "
                "chiziqli — ya'ni amplituda kichik va prujina Guk qonuniga bo'ysunadi "
                "deb faraz qilinadi. Katta amplitudada chastota amplitudaga bog'liq "
                "bo'lib qoladi (nm-30)."
            ),
            worked_example=WorkedExample(
                statement=(
                    "Ventilyator agregati ($m = 450$ kg) to'rtta rezina "
                    "vibroizolyatorga o'rnatilgan, har birining bikrligi "
                    "$k_1 = 180$ kN/m. (a) Tizimning xususiy chastotasi; "
                    "(b) statik cho'kish; (c) dvigatel 1450 ayl/min bilan ishlasa, "
                    "rezonans xavfi bormi?"
                ),
                given=[r"m = 450\ \text{kg},\; k_1 = 180\ \text{kN/m},\; 4\ \text{ta izolyator}",
                       r"n = 1450\ \text{ayl/min}"],
                steps=[
                    st(r"k = 4k_1 = 4\cdot 180 = 720\ \text{kN/m} = 7{,}2\cdot 10^5\ \text{N/m}",
                       "Izolyatorlar parallel ulangan — bikrliklar qo'shiladi."),
                    st(r"\omega_0 = \sqrt{\frac{7{,}2\cdot 10^5}{450}} = \sqrt{1600} = 40\ \text{rad/s}",
                       "Xususiy chastota."),
                    st(r"f_0 = \frac{\omega_0}{2\pi} = \frac{40}{6{,}283} = 6{,}37\ \text{Hz}",
                       "Texnik chastota."),
                    st(r"\delta_{st} = \frac{mg}{k} = \frac{450\cdot 9{,}81}{7{,}2\cdot10^5} = "
                       r"6{,}13\cdot 10^{-3}\ \text{m} = 6{,}13\ \text{mm}",
                       "Statik cho'kish. Tekshirish: $\\sqrt{9{,}81/0{,}00613} = 40$ rad/s ✓"),
                    st(r"f_{ish} = \frac{1450}{60} = 24{,}2\ \text{Hz},\qquad "
                       r"\frac{f_{ish}}{f_0} = \frac{24{,}2}{6{,}37} = 3{,}8",
                       "Ish chastotasi xususiydan 3,8 marta yuqori."),
                    st(r"3{,}8 > \sqrt{2} = 1{,}41 \;\Rightarrow\; \text{vibroizolyatsiya ishlaydi}",
                       "Nisbat $\\sqrt{2}$ dan katta bo'lganda uzatish koeffitsienti 1 dan "
                       "kichik bo'ladi (nm-27)."),
                ],
                answer=(
                    "$f_0 = 6{,}37$ Hz; $\\delta_{st} = 6{,}13$ mm; rezonans xavfi yo'q "
                    "($f_{ish}/f_0 = 3{,}8$), izolyatsiya samarali."
                ),
                engineering_note=(
                    "Xavf ishga tushirish/o'chirish paytida: rotor 0 dan 24,2 Hz gacha "
                    "chiqishda 6,37 Hz nuqtasidan o'tadi va qisqa vaqt rezonansga "
                    "tushadi. Shuning uchun bu zonadan tez o'tish yoki dempfirlashni "
                    "oshirish kerak (nm-26)."
                ),
            ),
            computation=Computation(
                caption=(
                    "Vibroizolyatsiya hisobi: massa va bikrlikni o'zgartirib, xususiy "
                    "chastota va rezonans zaxirasini baholang."
                ),
                code='''"""Bir erkinlik darajali tizimning erkin tebranishlari."""
import numpy as np
from scipy.integrate import solve_ivp
from labkit import PARAMS, note, series, table, value

m = float(PARAMS.get("m", 450.0))        # kg
k1 = float(PARAMS.get("k1", 180000.0))   # bitta izolyator bikrligi, N/m
n_iso = float(PARAMS.get("n_iso", 4))    # izolyatorlar soni
n_rpm = float(PARAMS.get("n_rpm", 1450)) # dvigatel aylanishi
x0 = float(PARAMS.get("x0", 0.01))       # boshlang'ich siljish, m
g = 9.81

k = n_iso*k1
w0 = np.sqrt(k/m)
f0 = w0/(2*np.pi)
delta_st = m*g/k

value("Ekvivalent bikrlik k", k/1000, "kN/m")
value("Xususiy chastota ω₀", w0, "rad/s")
value("Chastota f₀", f0, "Hz")
value("Statik cho'kish", delta_st*1000, "mm")
value("Davr T", 2*np.pi/w0, "s")
value("Ish chastotasi", n_rpm/60, "Hz")
value("Chastotalar nisbati", (n_rpm/60)/f0, "—")

note(f"√(g/δ_st) = {np.sqrt(g/delta_st):.3f} rad/s — ω₀ bilan mos ✓")
ratio = (n_rpm/60)/f0
note("Vibroizolyatsiya samarali (nisbat > √2)" if ratio > np.sqrt(2)
     else "DIQQAT: rezonans zonasiga yaqin — izolyatorlarni yumshatish kerak!")

# Sonli integrallash va analitik yechim bilan taqqoslash
def rhs(t, y):
    return [y[1], -k/m*y[0]]

sol = solve_ivp(rhs, (0, 5*2*np.pi/w0), [x0, 0.0], rtol=1e-10,
                dense_output=True, max_step=0.001)
tt = np.linspace(0, 5*2*np.pi/w0, 800)
X, V = sol.sol(tt)
X_an = x0*np.cos(w0*tt)

series("Tebranish x(t)", tt.tolist(), (X*1000).tolist(), xlabel="t, s", ylabel="x, mm")
series("Fazaviy portret", (X*1000).tolist(), V.tolist(), xlabel="x, mm", ylabel="v, m/s")
note(f"Sonli va analitik yechim farqi: {np.max(np.abs(X-X_an)):.3e} m")

# Energiya almashinuvi
T_kin = 0.5*m*V**2
Pi_pot = 0.5*k*X**2
series("Kinetik energiya", tt.tolist(), T_kin.tolist(), xlabel="t, s", ylabel="E, J")
series("Potensial energiya", tt.tolist(), Pi_pot.tolist(), xlabel="t, s", ylabel="E, J")
note(f"To'la energiya drifti: {np.ptp(T_kin+Pi_pot):.3e} J (saqlanishi kerak)")

# Izolyator bikrligining chastotaga ta'siri
kk = np.linspace(20000, 1000000, 200)
series("f₀(k)", (kk/1000).tolist(), (np.sqrt(n_iso*0+kk*n_iso/m)/(2*np.pi)).tolist(),
       xlabel="Bitta izolyator k, kN/m", ylabel="f₀, Hz")

table("Ekvivalent bikrlik qoidalari",
      ["Ulanish", "Formula", "Misol (k₁=k₂=100 kN/m)"],
      [["Parallel", "k = k₁+k₂", "200 kN/m"],
       ["Ketma-ket", "1/k = 1/k₁+1/k₂", "50 kN/m"],
       ["Konsol balka (uchida)", "k = 3EI/L³", "—"],
       ["Ikki tayanchli (o'rtada)", "k = 48EI/L³", "—"]])
''',
                parameters=[
                    p("m", "Agregat massasi m", 10.0, 5000.0, 450.0, 10.0, "kg"),
                    p("k1", "Bitta izolyator bikrligi", 5000.0, 2000000.0, 180000.0, 5000.0, "N/m"),
                    p("n_iso", "Izolyatorlar soni", 1.0, 12.0, 4.0, 1.0, "dona"),
                    p("n_rpm", "Dvigatel aylanishi", 100.0, 6000.0, 1450.0, 50.0, "ayl/min"),
                    p("x0", "Boshlang'ich siljish", 0.001, 0.05, 0.01, 0.001, "m"),
                ],
                expected_output="ω₀ = 40 rad/s, f₀ = 6,37 Hz, δ_st = 6,13 mm, nisbat = 3,80",
            ),
            visualization=vis(
                "Tebranish grafigi va fazaviy portret",
                "React/SVG",
                "$x(t)$ sinusoidasi amplituda va davr belgilari bilan; yonida "
                "fazaviy portret — ellips (so'nmaydigan tebranish).",
                "React/SVG: ikkala grafik uchun umumiy `LinePlot` komponenti yetarli. "
                "Fazaviy portretning aynan ellips ekani energiya saqlanishining "
                "geometrik ifodasi — buni nm-24 dagi portret bilan bog'lash kerak.",
            ),
            interpretation=(
                "Fazaviy portret yopiq ellips — energiya saqlanadi, tebranish "
                "so'nmaydi. Kinetik va potensial energiya grafiklari bir-birini "
                "to'ldiradi: yig'indisi o'zgarmas. $f_0(k)$ grafigi kvadrat ildiz "
                "shaklida: bikrlikni 4 marta oshirish chastotani atigi 2 marta "
                "ko'taradi — shuning uchun vibroizolyatsiyada massani oshirish "
                "ko'pincha samaraliroq."
            ),
            common_mistakes=[
                "Og'irlikni tenglamaga qo'shish — muvozanat holatidan o'lchansa u "
                "avtomatik qisqaradi.",
                "Ketma-ket va parallel ulangan prujinalarni chalkashtirish.",
                "$f$ (Hz) va $\\omega$ (rad/s) ni farqlamaslik: $\\omega = 2\\pi f$.",
                "Xususiy chastota amplitudaga bog'liq deb o'ylash — chiziqli tizimda "
                "u bog'liq emas.",
            ],
            quiz=[
                q("Nima uchun xususiy chastota boshlang'ich shartlarga bog'liq emas?",
                  "Chunki u xarakteristik tenglamadan kelib chiqadi va faqat $k$ va $m$ "
                  "ga bog'liq. Boshlang'ich shartlar faqat amplituda va fazani belgilaydi.",
                  "konseptual"),
                q("Statik cho'kish 4 mm. Xususiy chastota qancha?",
                  "$\\omega_0 = \\sqrt{9{,}81/0{,}004} = 49{,}5$ rad/s, $f_0 = 7{,}88$ Hz.",
                  "hisob"),
                q("Massani 2 marta oshirsak, chastota qanday o'zgaradi?",
                  "$\\sqrt{2} \\approx 1{,}41$ marta kamayadi.", "hisob"),
                q("Ikki prujina ketma-ket ulangan ($k_1 = k_2 = k$). Ekvivalent bikrlik?",
                  "$k_{ekv} = k/2$ — ketma-ket ulanish tizimni yumshatadi.", "hisob"),
                q("Kodda energiya drifti nima uchun tekshiriladi?",
                  "Erkin tebranishda energiya aynan saqlanishi kerak; drift sonli "
                  "integrallashning xatoligini ko'rsatadi.", "kod"),
            ],
            bridge_to_next=(
                "Real tizimda tebranish abadiy davom etmaydi — u so'nadi. Keyingi "
                "mavzuda dempfirlashni modelga kiritamiz."
            ),
            research_extension=(
                "Reley usuli bilan taqsimlangan massali konsol balkaning birinchi "
                "xususiy chastotasini baholang: $\\omega^2 = \\Pi_{max}/T^*_{max}$ "
                "nisbatini statik egilish shaklini sinov funksiyasi sifatida olib "
                "hisoblang. Aniq yechim $\\omega_1 = 3{,}516\\sqrt{EI/(\\rho AL^4)}$ "
                "bilan taqqoslang va xatolikni aniqlang."
            ),
        ),
    ),
    Topic(
        id="nm-26",
        subject_id=S,
        module_id=M,
        order=26,
        title="So'nuvchi tebranishlar: dempfirlash rejimlari va logarifmik dekrement",
        description=(
            "Yopishqoq dempfirlash, dempfirlash nisbati, uch rejim (kam, kritik va "
            "ortiqcha dempfirlangan), logarifmik dekrement va uni tajribada aniqlash."
        ),
        learning_objective=(
            "Dempfirlash darajasini aniqlash, so'nish tezligini hisoblash va "
            "tajriba ma'lumotlaridan dempfirlash nisbatini topish."
        ),
        prerequisites=["nm-25"],
        mathematical_core=(
            "$m\\ddot x + c\\dot x + kx = 0$, xarakteristik tenglama diskriminanti, "
            "kompleks ildizlar, eksponensial o'rash."
        ),
        engineering_application=(
            "Avtomobil amortizatori, bino seysmik dempferlari, o'lchov asboblari, "
            "eshik yopgich."
        ),
        computational_component=(
            "Uch rejimni taqqoslash va logarifmik dekrementdan $\\zeta$ ni tiklash."
        ),
        visualization_component="Uch rejim grafigi va so'nuvchi spiral fazaviy portret.",
        research_extension=(
            "Kulon (quruq) ishqalanishli so'nish yopishqoqdan qanday farq qiladi? "
            "Amplituda chiziqli kamayadi — buni ko'rsating."
        ),
        difficulty="asosiy",
        previous_link=(
            "nm-25 dagi modelga tezlikka proporsional qarshilik qo'shamiz — bu "
            "nm-08 dagi chiziqli qarshilik modelining tebranishlardagi ko'rinishi."
        ),
        next_topic="nm-27",
        estimated_minutes=85,
        tags=["dempfirlash", "so'nish", "logarifmik dekrement"],
        lesson=Lesson(
            physical_problem=(
                "Avtomobil g'ildiragidan o'tgach, kuzov bir-ikki marta tebranib "
                "to'xtashi kerak. Amortizator eskirsa — uzoq tebranadi (xavfsizlik "
                "yo'qoladi), juda qattiq bo'lsa — zarba to'g'ridan-to'g'ri kuzovga "
                "o'tadi. Optimal dempfirlash qanday tanlanadi?"
            ),
            concepts=[
                c("Yopishqoq dempfirlash", "$F_d = -c\\dot x$ — tezlikka proporsional "
                  "qarshilik; gidravlik amortizatorlarning asosiy modeli."),
                c("Dempfirlash nisbati", "$\\zeta = c/(2\\sqrt{km}) = c/c_{kr}$ — "
                  "o'lchamsiz parametr, rejimni belgilaydi."),
                c("Kritik dempfirlash", "$c_{kr} = 2\\sqrt{km} = 2m\\omega_0$; "
                  "$\\zeta = 1$ da tizim tebranmasdan eng tez muvozanatga qaytadi."),
                c("So'nish chastotasi", "$\\omega_d = \\omega_0\\sqrt{1-\\zeta^2}$ — "
                  "dempfirlash chastotani biroz pasaytiradi."),
                c("Logarifmik dekrement", "$\\delta = \\ln(A_n/A_{n+1}) = "
                  "2\\pi\\zeta/\\sqrt{1-\\zeta^2}$ — tajribada o'lchash mumkin bo'lgan "
                  "kattalik."),
            ],
            derivation=[
                d("1-qadam. Tenglama va xarakteristik ildizlar",
                  r"m\ddot x + c\dot x + kx = 0 \Rightarrow \lambda_{1,2} = "
                  r"-\frac{c}{2m} \pm \sqrt{\left(\frac{c}{2m}\right)^2 - \frac{k}{m}}",
                  "Diskriminant ishorasi rejimni belgilaydi."),
                d("2-qadam. O'lchamsizlashtirish",
                  r"\ddot x + 2\zeta\omega_0\dot x + \omega_0^2x = 0,\qquad "
                  r"\zeta = \frac{c}{2\sqrt{km}}",
                  "Ikkita parametr ($c$, $k$, $m$) o'rniga bitta $\\zeta$ qoldi — bu "
                  "universal tahlil imkonini beradi."),
                d("3-qadam. Kam dempfirlangan rejim ($\\zeta < 1$)",
                  r"\boxed{\;x(t) = Ae^{-\zeta\omega_0t}\sin(\omega_dt+\alpha),\quad "
                  r"\omega_d = \omega_0\sqrt{1-\zeta^2}\;}",
                  "Eksponensial o'ralgan sinusoida. Muhandislik konstruksiyalarida "
                  "$\\zeta$ odatda 0,01–0,1 — ya'ni $\\omega_d \\approx \\omega_0$."),
                d("4-qadam. Logarifmik dekrement",
                  r"\frac{A_n}{A_{n+1}} = \frac{e^{-\zeta\omega_0t_n}}{e^{-\zeta\omega_0(t_n+T_d)}} = "
                  r"e^{\zeta\omega_0T_d} \Rightarrow \delta = \zeta\omega_0T_d = "
                  r"\frac{2\pi\zeta}{\sqrt{1-\zeta^2}}",
                  "Ketma-ket amplitudalar nisbati o'zgarmas — bu tajribada "
                  "$\\zeta$ ni aniqlashning standart usuli: "
                  "$\\zeta \\approx \\delta/(2\\pi)$ kichik $\\zeta$ da."),
            ],
            formula_meaning=(
                "$\\zeta$ butun dinamikani bitta sonda jamlaydi. $\\zeta < 1$ — "
                "tebranib so'nadi (aksariyat konstruksiyalar); $\\zeta = 1$ — eng tez "
                "qaytish (o'lchov asboblari, eshik yopgichlar); $\\zeta > 1$ — sekin "
                "sudralib qaytish. Avtomobil podveskasi uchun optimal $\\zeta = 0{,}2...0{,}4$: "
                "bir-ikki tebranishda so'nadi, lekin qattiq emas."
            ),
            equations=[
                eq(r"\ddot x + 2\zeta\omega_0\dot x + \omega_0^2 x = 0",
                   "So'nuvchi tebranish tenglamasi.", "Dempfirlangan ossillyator"),
                eq(r"\zeta = \frac{c}{2\sqrt{km}}", "Dempfirlash nisbati.", "Zeta"),
                eq(r"\delta = \ln\frac{A_n}{A_{n+1}} = \frac{2\pi\zeta}{\sqrt{1-\zeta^2}}",
                   "Logarifmik dekrement.", "Dekrement"),
            ],
            conditions=(
                "Model yopishqoq (chiziqli) dempfirlashni nazarda tutadi. Real "
                "konstruksiyada so'nish materialning ichki ishqalanishi (gisterezis) "
                "va birikmalardagi quruq ishqalanishdan ham keladi — ular chiziqli "
                "emas, lekin ekvivalent yopishqoq dempfirlash bilan almashtiriladi."
            ),
            worked_example=WorkedExample(
                statement=(
                    "Avtomobil kuzovi (chorak modeli): $m = 320$ kg, prujina "
                    "$k = 22$ kN/m. Tajribada kuzov turtkidan keyin tebranganda "
                    "ketma-ket amplitudalar 40 mm va 14 mm bo'lgan. "
                    "(a) Logarifmik dekrement va $\\zeta$; (b) amortizator koeffitsienti "
                    "$c$; (c) amplituda 10 marta kamayishi uchun necha tebranish kerak?"
                ),
                given=[r"m = 320\ \text{kg},\; k = 22\,000\ \text{N/m}",
                       r"A_1 = 40\ \text{mm},\; A_2 = 14\ \text{mm}"],
                steps=[
                    st(r"\delta = \ln\frac{40}{14} = \ln 2{,}857 = 1{,}0498",
                       "Logarifmik dekrement."),
                    st(r"\zeta = \frac{\delta}{\sqrt{4\pi^2+\delta^2}} = "
                       r"\frac{1{,}0498}{\sqrt{39{,}48+1{,}102}} = \frac{1{,}0498}{6{,}370} = 0{,}1648",
                       "Aniq formula (taqribiy $\\delta/2\\pi = 0{,}167$ ham yaqin)."),
                    st(r"\omega_0 = \sqrt{\frac{22\,000}{320}} = \sqrt{68{,}75} = 8{,}29\ \text{rad/s}",
                       "Xususiy chastota ($f_0 = 1{,}32$ Hz — tipik podveska chastotasi)."),
                    st(r"c = 2\zeta\sqrt{km} = 2\cdot 0{,}1648\sqrt{22\,000\cdot 320} = "
                       r"0{,}3296\cdot 2653 = 874\ \text{N·s/m}",
                       "Amortizator koeffitsienti."),
                    st(r"\omega_d = 8{,}29\sqrt{1-0{,}0272} = 8{,}18\ \text{rad/s},\qquad "
                       r"T_d = 0{,}768\ \text{s}",
                       "So'nish chastotasi va davri."),
                    st(r"n = \frac{\ln 10}{\delta} = \frac{2{,}303}{1{,}0498} = 2{,}19 \approx 3",
                       "Amplituda 10 marta kamayishi uchun ~2,2 ta to'liq tebranish."),
                ],
                answer=(
                    "$\\delta = 1{,}05$; $\\zeta = 0{,}165$; $c = 874$ N·s/m; "
                    "amplituda 10 marta kamayishi uchun ~2,2 tebranish."
                ),
                engineering_note=(
                    "$\\zeta = 0{,}165$ biroz past — qulaylik yaxshi, lekin yo'l "
                    "ushlash uchun $\\zeta = 0{,}25...0{,}35$ afzalroq. Sport "
                    "avtomobillarda $\\zeta$ yuqoriroq (qattiq amortizator), yuk "
                    "mashinalarida pastroq. Amortizator eskirsa $c$ kamayadi va "
                    "tebranishlar cho'ziladi — bu tormoz yo'lini uzaytiradi."
                ),
            ),
            computation=Computation(
                caption=(
                    "Dempfirlash rejimlari: $\\zeta$ ni o'zgartirib, uch rejimni "
                    "taqqoslang va logarifmik dekrementni tekshiring."
                ),
                code='''"""So'nuvchi tebranishlar: uch rejim va logarifmik dekrement."""
import numpy as np
from scipy.integrate import solve_ivp
from scipy.signal import find_peaks
from labkit import PARAMS, note, series, table, value

m = float(PARAMS.get("m", 320.0))      # kg
k = float(PARAMS.get("k", 22000.0))    # N/m
zeta = float(PARAMS.get("zeta", 0.165))# dempfirlash nisbati
x0 = float(PARAMS.get("x0", 0.04))     # boshlang'ich siljish, m

w0 = np.sqrt(k/m)
c_kr = 2*np.sqrt(k*m)
c = zeta*c_kr
wd = w0*np.sqrt(abs(1-zeta**2)) if zeta < 1 else 0.0

value("ω₀", w0, "rad/s")
value("f₀", w0/(2*np.pi), "Hz")
value("Kritik dempfirlash c_kr", c_kr, "N·s/m")
value("Amortizator koeff. c", c, "N·s/m")
value("ω_d", wd, "rad/s")
value("Rejim", zeta, "ζ")
note({True: "Kam dempfirlangan (tebranib so'nadi)"}.get(zeta < 1,
     "Kritik dempfirlangan" if abs(zeta-1) < 1e-9 else "Ortiqcha dempfirlangan"))

def simulate(z, t_end=6.0):
    def rhs(t, y):
        return [y[1], -2*z*w0*y[1] - w0**2*y[0]]
    s = solve_ivp(rhs, (0, t_end), [x0, 0.0], rtol=1e-10, dense_output=True, max_step=0.002)
    tt = np.linspace(0, t_end, 1500)
    return tt, s.sol(tt)

# Uch rejimni taqqoslash
for z, label in [(zeta, f"ζ={zeta:.3f} (joriy)"), (1.0, "ζ=1 (kritik)"),
                 (2.0, "ζ=2 (ortiqcha)"), (0.02, "ζ=0,02 (kam)")]:
    tt, (X, V) = simulate(z)
    series(f"x(t): {label}", tt.tolist(), (X*1000).tolist(), xlabel="t, s", ylabel="x, mm")

# Joriy rejim uchun fazaviy portret va o'rash
tt, (X, V) = simulate(zeta)
series("Fazaviy portret (so'nuvchi spiral)", (X*1000).tolist(), V.tolist(),
       xlabel="x, mm", ylabel="v, m/s")
if zeta < 1:
    series("Eksponensial o'rash +", tt.tolist(), (x0*np.exp(-zeta*w0*tt)*1000).tolist(),
           xlabel="t, s", ylabel="x, mm")

# Logarifmik dekrementni sonli tiklash
if zeta < 1:
    peaks, _ = find_peaks(X)
    if len(peaks) >= 2:
        A = X[peaks]
        delta_num = float(np.mean(np.log(A[:-1]/A[1:])))
        zeta_rec = delta_num/np.sqrt(4*np.pi**2 + delta_num**2)
        value("δ (sonli)", delta_num, "—")
        value("δ (nazariy)", 2*np.pi*zeta/np.sqrt(1-zeta**2), "—")
        value("ζ (tiklangan)", zeta_rec, "—")
        note(f"Tiklash xatoligi: {abs(zeta_rec-zeta)/zeta*100:.3f} % — "
             "bu tajribada ζ ni aniqlashning standart usuli.")
        n10 = np.log(10)/delta_num
        value("10 marta kamayish uchun tebranishlar", n10, "dona")

table("Dempfirlash rejimlari va qo'llanilishi",
      ["ζ", "Rejim", "Tipik qo'llanilish"],
      [[0.01, "Juda kam", "Po'lat konstruksiyalar, kamertonlar"],
       [0.05, "Kam", "Ko'prik, bino (seysmik hisobda)"],
       [0.30, "O'rtacha", "Avtomobil podveskasi"],
       [1.00, "Kritik", "O'lchov asboblari, eshik yopgich"],
       [2.00, "Ortiqcha", "Og'ir eshiklar, ba'zi demferlar"]])
''',
                parameters=[
                    p("m", "Massa m", 10.0, 2000.0, 320.0, 10.0, "kg"),
                    p("k", "Bikrlik k", 1000.0, 200000.0, 22000.0, 500.0, "N/m"),
                    p("zeta", "Dempfirlash nisbati ζ", 0.0, 3.0, 0.165, 0.005, "—"),
                    p("x0", "Boshlang'ich siljish", 0.005, 0.15, 0.04, 0.005, "m"),
                ],
                expected_output="ω₀ = 8,29 rad/s, c = 874 N·s/m, δ ≈ 1,05, ζ tiklangan ≈ 0,165",
            ),
            visualization=vis(
                "Uch dempfirlash rejimi",
                "React/SVG",
                "Bir grafikda $\\zeta = 0{,}05$, $0{,}3$, $1{,}0$, $2{,}0$ uchun $x(t)$; "
                "eksponensial o'rash punktir chiziq bilan; yonida so'nuvchi spiral "
                "fazaviy portret.",
                "React/SVG: to'rt chiziqni bir grafikda ko'rsatish rejimlar farqini "
                "darhol ochib beradi. Fazaviy portretdagi spiral esa energiya "
                "yo'qolishining geometrik ifodasi — nm-25 dagi yopiq ellips bilan "
                "taqqoslash pedagogik jihatdan kuchli.",
            ),
            interpretation=(
                "$\\zeta = 0{,}02$ da tebranish o'nlab sikl davom etadi, $\\zeta = 0{,}3$ "
                "da ikki-uch siklda so'nadi, $\\zeta = 1$ da umuman tebranmaydi. "
                "$\\zeta > 1$ da qaytish sekinlashadi — demak 'ko'proq dempfirlash "
                "har doim yaxshi' degan tasavvur xato. Fazaviy portretdagi spiral "
                "markazga yaqinlashadi: energiya monoton kamayadi."
            ),
            common_mistakes=[
                "$\\omega_d$ o'rniga $\\omega_0$ ni ishlatib so'nish davrini hisoblash "
                "(kichik $\\zeta$ da farq kichik, katta $\\zeta$ da sezilarli).",
                "Logarifmik dekrementni qo'shni emas, uzoq amplitudalar orasida olish "
                "va $n$ ga bo'lishni unutish.",
                "$\\zeta > 1$ da ham tebranish bo'ladi deb o'ylash — u yerda "
                "aperiodik qaytish.",
                "Quruq ishqalanishli so'nishni eksponensial deb hisoblash — u chiziqli "
                "kamayadi.",
            ],
            quiz=[
                q("Nima uchun kritik dempfirlash eng tez qaytishni beradi?",
                  "$\\zeta < 1$ da tizim muvozanatdan o'tib ketadi va qaytadi; "
                  "$\\zeta > 1$ da esa sekin sudraladi. $\\zeta = 1$ — ikkalasining "
                  "chegarasi va eng tez.", "konseptual"),
                q("$A_1 = 20$ mm, $A_2 = 5$ mm. $\\delta$ va taqribiy $\\zeta$?",
                  "$\\delta = \\ln 4 = 1{,}386$; $\\zeta \\approx 1{,}386/6{,}283 = 0{,}22$.",
                  "hisob"),
                q("$\\zeta = 0{,}1$ da $\\omega_d$ $\\omega_0$ dan necha foiz farq qiladi?",
                  "$\\sqrt{1-0{,}01} = 0{,}995$ — atigi 0,5 %.", "hisob"),
                q("Amortizator eskirsa (c kamaysa) nima bo'ladi?",
                  "$\\zeta$ kamayadi, tebranishlar uzoqroq davom etadi, g'ildirakning "
                  "yo'l bilan kontakti buziladi — tormozlash va boshqarish yomonlashadi.",
                  "talqin"),
                q("Kodda `find_peaks` nima uchun ishlatilgan?",
                  "Ketma-ket amplitudalarni topish uchun — ulardan logarifmik dekrement "
                  "hisoblanadi va $\\zeta$ tiklanadi. Bu tajriba ma'lumotlarini qayta "
                  "ishlashning sodda modeli.", "kod"),
            ],
            bridge_to_next=(
                "Erkin tebranish so'nadi. Lekin mashina doimiy ishlaganda davriy kuch "
                "tebranishni uzluksiz qo'llab turadi. Keyingi mavzu — majburiy "
                "tebranishlar va rezonans."
            ),
            research_extension=(
                "Kulon ishqalanishli so'nishni modellashtiring: $F = -F_0\\,\\text{sign}(\\dot x)$. "
                "Amplituda har yarim siklda $2F_0/k$ ga kamayishini (chiziqli qonun) "
                "sonli ko'rsating va yopishqoq so'nish bilan taqqoslang. Qaysi model "
                "real birikmalardagi so'nishni yaxshiroq tavsiflaydi?"
            ),
            manim=manim(
                scene="DampingRegimesScene",
                module="animatsiya/scenes/nm_vibrations.py",
                title="Dempfirlash rejimlari",
                summary="Uch massa bir vaqtda qo'yib yuboriladi (ζ=0,1; 1; 2) va "
                        "ularning harakati hamda fazaviy portretlari taqqoslanadi.",
            ),
        ),
    ),
    Topic(
        id="nm-27",
        subject_id=S,
        module_id=M,
        order=27,
        title="Majburiy tebranishlar, rezonans va amplituda-chastota tavsifi",
        description=(
            "Garmonik majburlovchi kuch, barqaror rejim, dinamiklik koeffitsienti, "
            "rezonans va vibroizolyatsiya nazariyasi."
        ),
        learning_objective=(
            "Amplituda-chastota tavsifini qurish, rezonans xavfini baholash va "
            "vibroizolyatsiya samaradorligini hisoblash."
        ),
        prerequisites=["nm-26"],
        mathematical_core=(
            "Nobir jinsli ODE, xususiy va xususiy bo'lmagan yechim, kompleks "
            "amplituda usuli, uzatish funksiyasi."
        ),
        engineering_application=(
            "Mashina fundamenti, vibroizolyatsiya, dinamik so'ndirgich, "
            "seysmik hisob, rotor kritik tezligi."
        ),
        computational_component=(
            "Amplituda-chastota va faza-chastota tavsiflarini qurish, "
            "uzatish koeffitsientini hisoblash."
        ),
        visualization_component="AChT egri chiziqlari oilasi turli $\\zeta$ da.",
        research_extension=(
            "Dinamik tebranish so'ndirgichi (tuned mass damper) qanday ishlaydi? "
            "Ikki massali tizimda rezonansni yo'qotish."
        ),
        difficulty="murakkab",
        previous_link=(
            "nm-26 da erkin tebranish so'nishini ko'rdik. Endi tashqi davriy kuch "
            "qo'shamiz — va tizim o'z chastotasini emas, majburlovchi chastotani "
            "'tanlaydi'."
        ),
        next_topic="nm-28",
        estimated_minutes=95,
        tags=["rezonans", "majburiy tebranish", "vibroizolyatsiya"],
        lesson=Lesson(
            physical_problem=(
                "Muvozanatlanmagan rotor fundamentga davriy kuch beradi. "
                "Ish chastotasi xususiy chastotaga yaqinlashganda amplituda keskin "
                "ortadi — bu rezonans. Lekin undan yuqorida amplituda yana kamayadi. "
                "Demak izolyatsiya uchun tizimni yumshoq qilish kerak — bu intuitiv "
                "emas. Nima uchun shunday?"
            ),
            concepts=[
                c("Majburlovchi kuch", "$F(t) = F_0\\sin\\omega t$ — odatda "
                  "muvozanatlanmagan rotordan: $F_0 = m_ue\\omega^2$."),
                c("Barqaror rejim", "O'tish jarayoni so'ngach qoladigan tebranish; "
                  "chastotasi majburlovchi chastotaga teng."),
                c("Dinamiklik koeffitsienti", "$\\mu = A/x_{st}$ — dinamik amplitudaning "
                  "statik siljishga nisbati."),
                c("Chastotalar nisbati", "$r = \\omega/\\omega_0$ — AChT ning asosiy "
                  "argumenti."),
                c("Uzatish koeffitsienti", "$TR = F_{uzatilgan}/F_0$ — "
                  "vibroizolyatsiya samaradorligi; $r > \\sqrt{2}$ da $TR < 1$."),
            ],
            derivation=[
                d("1-qadam. Tenglama va yechim strukturasi",
                  r"m\ddot x + c\dot x + kx = F_0\sin\omega t;\qquad "
                  r"x = \underbrace{x_h}_{\text{so'nadi}} + \underbrace{x_p}_{\text{barqaror}}",
                  "Xususiy yechim $x_h$ eksponensial so'nadi, shuning uchun uzoq vaqtdan "
                  "keyin faqat $x_p$ qoladi."),
                d("2-qadam. Kompleks amplituda usuli",
                  r"x_p = \text{Im}(Xe^{i\omega t}) \Rightarrow "
                  r"(-m\omega^2 + ic\omega + k)X = F_0",
                  "Differensiallash $i\\omega$ ga ko'paytirishga aylanadi — "
                  "differensial tenglama algebraik bo'lib qoladi."),
                d("3-qadam. Amplituda-chastota tavsifi",
                  r"\boxed{\;\mu = \frac{A}{F_0/k} = \frac{1}{\sqrt{(1-r^2)^2+(2\zeta r)^2}},"
                  r"\quad r = \frac{\omega}{\omega_0}\;}",
                  "$|X|$ ni hisoblaymiz va statik siljish $F_0/k$ ga bo'lamiz. "
                  "Rezonans ($r \\to 1$) da maxraj minimal bo'ladi."),
                d("4-qadam. Rezonans amplitudasi va faza",
                  r"\mu_{max} \approx \frac{1}{2\zeta}\ (r\approx 1);\qquad "
                  r"\tan\varphi = \frac{2\zeta r}{1-r^2}",
                  "Rezonansda amplituda faqat dempfirlash bilan cheklanadi. "
                  "$\\zeta = 0{,}02$ da $\\mu = 25$ — statik siljishdan 25 marta katta! "
                  "Fazada esa $r = 1$ da aynan $90°$ kechikish."),
                d("5-qadam. Uzatish koeffitsienti",
                  r"TR = \frac{\sqrt{1+(2\zeta r)^2}}{\sqrt{(1-r^2)^2+(2\zeta r)^2}};\qquad "
                  r"TR < 1 \iff r > \sqrt{2}",
                  "Fundamentga uzatiladigan kuch prujina va dempfer orqali o'tadi. "
                  "$r = \\sqrt{2}$ — universal chegara: undan past chastotalarda "
                  "izolyatsiya kuchaytiradi, yuqorida — kamaytiradi."),
            ],
            formula_meaning=(
                "AChT egri chizig'i — konstruksiya dinamikasining 'pasporti'. Uchta "
                "soha bor: $r \\ll 1$ (kvazistatik, $\\mu \\approx 1$), $r \\approx 1$ "
                "(rezonans, $\\mu \\gg 1$) va $r \\gg 1$ (inersion, $\\mu \\to 0$). "
                "Vibroizolyatsiya uchinchi sohada ishlaydi va shuning uchun izolyator "
                "yumshoq bo'lishi kerak — bu $\\omega_0$ ni pasaytirib, $r$ ni oshiradi. "
                "$r > \\sqrt{2}$ sharti esa dempfirlashdan mustaqil universal qoida."
            ),
            equations=[
                eq(r"\mu = \frac{1}{\sqrt{(1-r^2)^2+(2\zeta r)^2}}", "Dinamiklik koeffitsienti (AChT).",
                   "AChT"),
                eq(r"\mu_{max} \approx \frac{1}{2\zeta}", "Rezonansdagi amplituda.", "Rezonans"),
                eq(r"TR = \sqrt{\frac{1+(2\zeta r)^2}{(1-r^2)^2+(2\zeta r)^2}}",
                   "Uzatish koeffitsienti.", "Vibroizolyatsiya"),
            ],
            conditions=(
                "Barqaror rejim o'tish jarayonidan keyin o'rnatiladi; uning davomiyligi "
                "$\\approx 3/(\\zeta\\omega_0)$. Ishga tushirishda tizim rezonans "
                "zonasidan o'tadi va vaqtinchalik katta amplituda oladi — bu alohida "
                "hisoblanadi. Muvozanatlanmagan rotorda $F_0 = m_ue\\omega^2$ bo'lgani "
                "uchun AChT shakli biroz o'zgaradi."
            ),
            worked_example=WorkedExample(
                statement=(
                    "Muvozanatlanmagan ventilyator: $m = 450$ kg, $k = 720$ kN/m, "
                    "$\\zeta = 0{,}08$. Rotor muvozanatsizligi $m_ue = 0{,}05$ kg·m, "
                    "ish chastotasi 1450 ayl/min. (a) Barqaror rejimdagi amplituda; "
                    "(b) fundamentga uzatiladigan kuch; (c) rezonansda amplituda "
                    "qancha bo'lardi?"
                ),
                given=[r"m = 450\ \text{kg},\; k = 7{,}2\cdot10^5\ \text{N/m},\; \zeta = 0{,}08",
                       r"m_ue = 0{,}05\ \text{kg·m},\; n = 1450\ \text{ayl/min}"],
                steps=[
                    st(r"\omega_0 = 40\ \text{rad/s},\qquad \omega = \frac{\pi\cdot 1450}{30} = 151{,}8\ \text{rad/s}",
                       "Xususiy va majburlovchi chastotalar."),
                    st(r"r = \frac{151{,}8}{40} = 3{,}80",
                       "Chastotalar nisbati — inersion sohada."),
                    st(r"F_0 = m_ue\omega^2 = 0{,}05\cdot 151{,}8^2 = 0{,}05\cdot 23\,043 = 1152\ \text{N}",
                       "Markazdan qochma majburlovchi kuch (nm-17)."),
                    st(r"\mu = \frac{1}{\sqrt{(1-14{,}44)^2+(2\cdot0{,}08\cdot3{,}8)^2}} = "
                       r"\frac{1}{\sqrt{180{,}6+0{,}37}} = \frac{1}{13{,}45} = 0{,}0743",
                       "Dinamiklik koeffitsienti — statik siljishdan 13 marta kichik."),
                    st(r"A = \mu\frac{F_0}{k} = 0{,}0743\cdot\frac{1152}{7{,}2\cdot10^5} = "
                       r"0{,}0743\cdot 1{,}6\cdot10^{-3} = 0{,}119\ \text{mm}",
                       "Barqaror amplituda — juda kichik, qabul qilinadi."),
                    st(r"TR = \sqrt{\frac{1+0{,}37}{180{,}6+0{,}37}} = \sqrt{0{,}00757} = 0{,}087;"
                       r"\quad F_{fund} = 0{,}087\cdot 1152 = 100\ \text{N}",
                       "Fundamentga kuchning atigi 8,7 % i o'tadi. Rezonansda esa "
                       "$\\mu_{max} \\approx 1/(2\\cdot 0{,}08) = 6{,}25$ bo'lardi — "
                       "amplituda 84 marta katta."),
                ],
                answer=(
                    "$A = 0{,}119$ mm; fundamentga $F = 100$ N (8,7 %); rezonansda "
                    "amplituda $\\approx 10$ mm bo'lardi."
                ),
                engineering_note=(
                    "Izolyatsiya samaradorligi 91,3 %. Lekin ishga tushirishda rotor "
                    "$r = 1$ nuqtasidan o'tadi — o'sha lahzada amplituda 10 mm gacha "
                    "chiqishi mumkin. Shuning uchun (a) bu zonadan tez o'tiladi, "
                    "(b) ishga tushirishda qo'shimcha dempfirlash qo'llaniladi."
                ),
            ),
            computation=Computation(
                caption=(
                    "AChT va uzatish koeffitsienti: dempfirlashni o'zgartirib, "
                    "rezonans cho'qqisi va izolyatsiya samaradorligini kuzating."
                ),
                code='''"""Majburiy tebranishlar: AChT, rezonans va vibroizolyatsiya."""
import numpy as np
from scipy.integrate import solve_ivp
from labkit import PARAMS, note, series, table, value

m = float(PARAMS.get("m", 450.0))
k = float(PARAMS.get("k", 720000.0))
zeta = float(PARAMS.get("zeta", 0.08))
mu_e = float(PARAMS.get("mu_e", 0.05))     # muvozanatsizlik m_u*e, kg*m
n_rpm = float(PARAMS.get("n_rpm", 1450))

w0 = np.sqrt(k/m)
w = np.pi*n_rpm/30
r = w/w0
F0 = mu_e*w**2
x_st = F0/k

def amp_factor(rr, z):
    return 1.0/np.sqrt((1-rr**2)**2 + (2*z*rr)**2)

def transmissibility(rr, z):
    return np.sqrt((1+(2*z*rr)**2)/((1-rr**2)**2 + (2*z*rr)**2))

mu = amp_factor(r, zeta)
TR = transmissibility(r, zeta)

value("ω₀", w0, "rad/s")
value("ω (ish)", w, "rad/s")
value("r = ω/ω₀", r, "—")
value("Majburlovchi kuch F₀", F0, "N")
value("Dinamiklik koeff. μ", mu, "—")
value("Amplituda A", mu*x_st*1000, "mm")
value("Uzatish koeff. TR", TR, "—")
value("Fundamentga kuch", TR*F0, "N")
value("Izolyatsiya samaradorligi", 100*(1-TR), "%")
value("μ rezonansda", 1/(2*zeta), "—")

# AChT oilasi
rr = np.linspace(0.01, 4, 500)
for z in (0.02, 0.05, zeta, 0.2, 0.5):
    series(f"AChT: ζ={z:.3f}", rr.tolist(), amp_factor(rr, z).tolist(),
           xlabel="r = ω/ω₀", ylabel="μ")
series("Faza φ(r)", rr.tolist(),
       np.degrees(np.arctan2(2*zeta*rr, 1-rr**2)).tolist(),
       xlabel="r = ω/ω₀", ylabel="φ, deg")
for z in (0.02, zeta, 0.3):
    series(f"Uzatish TR: ζ={z:.3f}", rr.tolist(), transmissibility(rr, z).tolist(),
           xlabel="r = ω/ω₀", ylabel="TR")

r_peak = np.sqrt(max(1-2*zeta**2, 0.0))
note(f"AChT maksimumi r = {r_peak:.4f} da (aniq: √(1-2ζ²)), μ_max = "
     f"{amp_factor(r_peak, zeta):.3f}")
note("TR = 1 aynan r = √2 = 1,414 da — bu dempfirlashdan mustaqil universal chegara.")

# O'tish jarayoni: ishga tushirish rezonans zonasidan o'tish
def rhs(t, y):
    w_t = w*min(t/3.0, 1.0)            # 3 s da nominal chastotaga chiqish
    F = mu_e*w_t**2*np.sin(w_t*t)
    return [y[1], (F - 2*zeta*w0*m*y[1] - k*y[0])/m]

sol = solve_ivp(rhs, (0, 8), [0, 0], rtol=1e-8, dense_output=True, max_step=0.001)
tt = np.linspace(0, 8, 3000)
X, V = sol.sol(tt)
series("Ishga tushirish x(t)", tt.tolist(), (X*1000).tolist(), xlabel="t, s", ylabel="x, mm")
note(f"Ishga tushirishdagi maksimal amplituda: {np.max(np.abs(X))*1000:.3f} mm, "
     f"barqaror rejimda esa {mu*x_st*1000:.3f} mm — "
     f"{np.max(np.abs(X))/(mu*x_st):.1f} marta katta.")

table("Chastota sohalari",
      ["Soha", "r", "μ", "Xatti-harakat"],
      [["Kvazistatik", "< 0,4", "≈ 1", "Massa kuch bilan birga harakatlanadi"],
       ["Rezonans", "≈ 1", f"{1/(2*zeta):.1f}", "Amplituda ζ bilan cheklanadi"],
       ["Inersion", "> 1,41", "< 0,5", "Izolyatsiya ishlaydi"]])
''',
                parameters=[
                    p("m", "Massa m", 10.0, 5000.0, 450.0, 10.0, "kg"),
                    p("k", "Bikrlik k", 10000.0, 5000000.0, 720000.0, 10000.0, "N/m"),
                    p("zeta", "Dempfirlash ζ", 0.005, 0.7, 0.08, 0.005, "—"),
                    p("mu_e", "Muvozanatsizlik m_u·e", 0.001, 1.0, 0.05, 0.005, "kg·m"),
                    p("n_rpm", "Ish aylanishi", 100.0, 6000.0, 1450.0, 50.0, "ayl/min"),
                ],
                expected_output="r = 3,80; μ = 0,074; A = 0,119 mm; TR = 0,087 (91,3 % izolyatsiya)",
            ),
            visualization=vis(
                "Amplituda-chastota tavsifi",
                "React/SVG",
                "Turli $\\zeta$ dagi AChT egri chiziqlari oilasi; $r = 1$ va "
                "$r = \\sqrt{2}$ vertikal chiziqlar bilan belgilangan; ostida faza "
                "grafigi va uzatish koeffitsienti.",
                "React/SVG: AChT — tebranishlar nazariyasining eng tanilgan grafigi. "
                "$\\zeta$ ni slider bilan o'zgartirganda rezonans cho'qqisining "
                "pasayishi va $r=\\sqrt{2}$ nuqtasining qimirlamasligini ko'rsatish — "
                "eng muhim pedagogik moment.",
            ),
            interpretation=(
                "Barcha AChT egri chiziqlari $r = \\sqrt{2}$ nuqtasida bir joyda "
                "kesishadi (TR grafigida) — dempfirlash bu chegarani siljitmaydi. "
                "Yuqori chastotalarda esa katta $\\zeta$ izolyatsiyani yomonlashtiradi: "
                "dempfer kuchni to'g'ridan-to'g'ri uzatadi. Shuning uchun optimal "
                "dempfirlash kompromiss: ishga tushirishda rezonansni cheklash uchun "
                "yetarli, lekin ish rejimida izolyatsiyani buzmaydigan darajada."
            ),
            common_mistakes=[
                "Rezonansni aynan $r = 1$ da deb olish — aslida maksimum "
                "$r = \\sqrt{1-2\\zeta^2}$ da, lekin kichik $\\zeta$ da farq sezilmaydi.",
                "Izolyatsiya uchun tizimni qattiqroq qilish — bu $\\omega_0$ ni "
                "oshiradi, $r$ ni kamaytiradi va vaziyatni yomonlashtiradi.",
                "O'tish jarayonini e'tiborsiz qoldirish — ishga tushirishdagi "
                "amplituda barqaror rejimdagidan o'nlab marta katta bo'lishi mumkin.",
                "Muvozanatlanmagan rotorda $F_0$ ni o'zgarmas deb olish — u "
                "$\\omega^2$ ga proporsional.",
            ],
            quiz=[
                q("Nima uchun vibroizolyator yumshoq bo'lishi kerak?",
                  "Yumshoq izolyator $\\omega_0$ ni pasaytiradi, demak $r = \\omega/\\omega_0$ "
                  "ortadi va tizim izolyatsiya ishlaydigan inersion sohaga tushadi.",
                  "konseptual"),
                q("$\\zeta = 0{,}05$ da rezonansdagi dinamiklik koeffitsienti?",
                  "$\\mu_{max} \\approx 1/(2\\cdot 0{,}05) = 10$.", "hisob"),
                q("$r = 2$, $\\zeta = 0{,}1$. $\\mu$ ni toping.",
                  "$\\mu = 1/\\sqrt{(1-4)^2+(0{,}4)^2} = 1/\\sqrt{9{,}16} = 0{,}330$.",
                  "hisob"),
                q("Rezonansda majburlovchi kuch va siljish orasidagi faza farqi?",
                  "Aynan $90°$: kuch tezlik bilan bir fazada bo'ladi va har siklda "
                  "maksimal energiya kiritadi — shuning uchun amplituda o'sadi.",
                  "talqin"),
                q("Kodda `r_peak = np.sqrt(max(1-2*zeta**2, 0))` nima uchun?",
                  "AChT maksimumining aniq o'rni. $\\zeta > 1/\\sqrt{2}$ bo'lsa "
                  "maksimum umuman yo'qoladi — shuning uchun `max(..., 0)` himoyasi.",
                  "kod"),
            ],
            bridge_to_next=(
                "Bir massali model ko'p holda yetarli. Lekin real konstruksiyada "
                "ko'p massa va ko'p chastota bor. Keyingi mavzuda ko'p erkinlik "
                "darajali tizimlarga o'tamiz — va matritsalar paydo bo'ladi."
            ),
            research_extension=(
                "Dinamik tebranish so'ndirgichini (tuned mass damper) modellashtiring: "
                "asosiy massaga kichik massa-prujina qo'shing va uni "
                "$\\omega_2 = \\omega$ ga sozlang. Asosiy massaning amplitudasi "
                "aynan nolga tushishini ko'rsating. So'ngra Den Hartog optimal sozlash "
                "formulalarini sonli tekshiring — bu Taypey 101 va boshqa "
                "osmono'parlarda ishlatiladigan real texnologiya."
            ),
            manim=manim(
                scene="ResonanceScene",
                module="animatsiya/scenes/nm_vibrations.py",
                title="Rezonans va AChT",
                summary="Majburlovchi chastota sekin oshirilganda massa amplitudasi "
                        "va AChT egri chizig'idagi ishchi nuqta bir vaqtda ko'rsatiladi.",
            ),
        ),
    ),
    Topic(
        id="nm-28",
        subject_id=S,
        module_id=M,
        order=28,
        title="Ko'p erkinlik darajali tizimlar: massa va bikrlik matritsalari",
        description=(
            "Ko'p massali tizim uchun harakat tenglamalarini matritsa ko'rinishida "
            "yozish, matritsalarni yig'ish va ularning xossalari."
        ),
        learning_objective=(
            "Ko'p erkinlik darajali tizim uchun $[M]$ va $[K]$ matritsalarini "
            "Lagranj tenglamalaridan tuzish."
        ),
        prerequisites=["nm-27", "nm-22"],
        mathematical_core=(
            "Kvadratik formalar, simmetrik musbat aniqlangan matritsalar, "
            "matritsa ko'rinishidagi ODE tizimi."
        ),
        engineering_application=(
            "Ko'p qavatli bino modeli, val-disk tizimlari, avtomobil podveskasining "
            "to'liq modeli."
        ),
        computational_component=(
            "Matritsalarni avtomatik yig'ish va tizimni sonli integrallash."
        ),
        visualization_component="Matritsa strukturasi (lentali shakl) va tizim sxemasi.",
        research_extension=(
            "Matritsalarning lentali strukturasi katta tizimlarni yechishda qanday "
            "tejamkorlik beradi? (su-03 bilan bog'lanadi)"
        ),
        difficulty="murakkab",
        previous_link=(
            "nm-22 dagi Lagranj tenglamalari har bir koordinata uchun bitta tenglama "
            "beradi. $n$ ta koordinata — $n$ ta bog'langan tenglama, ularni matritsa "
            "shaklida yozish tabiiy."
        ),
        next_topic="nm-29",
        estimated_minutes=90,
        tags=["matritsa", "ko'p erkinlik darajasi", "bikrlik matritsasi"],
        lesson=Lesson(
            physical_problem=(
                "Uch qavatli bino zilzila paytida qanday tebranadi? Har bir qavat "
                "o'z massasiga ega va qo'shni qavatlar bilan ustunlar orqali "
                "bog'langan. Bitta qavatning siljishi qolganlariga ta'sir qiladi. "
                "Bunday bog'langan tizimni tavsiflash uchun bitta tenglama yetmaydi — "
                "matritsalar kerak."
            ),
            concepts=[
                c("Massa matritsasi $[M]$", "Kinetik energiya kvadratik formasining "
                  "matritsasi: $T = \\tfrac{1}{2}\\{\\dot q\\}^T[M]\\{\\dot q\\}$. "
                  "Simmetrik va musbat aniqlangan."),
                c("Bikrlik matritsasi $[K]$", "Potensial energiya kvadratik formasining "
                  "matritsasi: $\\Pi = \\tfrac{1}{2}\\{q\\}^T[K]\\{q\\}$."),
                c("Bog'langan tenglamalar", "$K_{ij} \\neq 0$ ($i\\neq j$) bo'lsa, "
                  "koordinatalar bikrlik orqali bog'langan."),
                c("Matritsalarni yig'ish (assembly)", "Har bir element (prujina, massa) "
                  "hissasini global matritsaga qo'shish — FEM ning asosiy amali (su-19)."),
                c("Lentali struktura", "Faqat qo'shni elementlar bog'langan bo'lsa, "
                  "matritsa diagonal atrofida to'plangan bo'ladi — bu yechimni "
                  "sezilarli tezlashtiradi."),
            ],
            derivation=[
                d("1-qadam. Energiyalarni umumlashgan koordinatalarda yozish",
                  r"T = \tfrac{1}{2}\sum_i m_i\dot x_i^2,\qquad "
                  r"\Pi = \tfrac{1}{2}\sum_j k_j(\Delta_j)^2",
                  "$\\Delta_j$ — $j$-prujinaning cho'zilishi, u koordinatalar "
                  "ayirmasi orqali ifodalanadi."),
                d("2-qadam. Kvadratik forma ko'rinishiga keltirish",
                  r"T = \tfrac{1}{2}\{\dot x\}^T[M]\{\dot x\},\qquad "
                  r"\Pi = \tfrac{1}{2}\{x\}^T[K]\{x\}",
                  "Matritsa elementlari: $M_{ij} = \\partial^2T/\\partial\\dot x_i\\partial\\dot x_j$, "
                  "$K_{ij} = \\partial^2\\Pi/\\partial x_i\\partial x_j$. Ikkinchi "
                  "hosilalar simmetrik, demak matritsalar ham simmetrik."),
                d("3-qadam. Lagranj tenglamalarini qo'llash",
                  r"\frac{d}{dt}\frac{\partial L}{\partial\dot x_i} - \frac{\partial L}{\partial x_i} = 0 "
                  r"\;\Rightarrow\; \boxed{\;[M]\{\ddot x\} + [K]\{x\} = \{F(t)\}\;}",
                  "Har bir koordinata uchun Lagranj tenglamasi — matritsa ko'rinishida "
                  "bitta ixcham yozuv."),
                d("4-qadam. Uch qavatli bino uchun matritsalarni yig'ish",
                  r"[K] = \begin{pmatrix} k_1+k_2 & -k_2 & 0\\ -k_2 & k_2+k_3 & -k_3\\ "
                  r"0 & -k_3 & k_3\end{pmatrix},\qquad [M] = \text{diag}(m_1, m_2, m_3)",
                  "Har bir prujina ikkita diagonal elementga $+k$ va ikkita "
                  "diagonaldan tashqaridagiga $-k$ qo'shadi. Bu naqsh FEM da aynan "
                  "takrorlanadi."),
            ],
            formula_meaning=(
                "$[M]\\{\\ddot x\\} + [K]\\{x\\} = \\{F\\}$ — butun strukturaviy "
                "dinamikaning asosiy tenglamasi. Uch qavatli binoda ham, million "
                "erkinlik darajali FEM modelida ham shakl bir xil, faqat matritsalar "
                "o'lchami farq qiladi. $[K]$ ning lentali strukturasi esa hisoblash "
                "samaradorligining kalitidir: to'liq matritsa uchun $O(n^3)$ amal "
                "kerak bo'lsa, lentali uchun $O(nb^2)$ ($b$ — lenta kengligi)."
            ),
            equations=[
                eq(r"[M]\{\ddot x\} + [C]\{\dot x\} + [K]\{x\} = \{F(t)\}",
                   "Strukturaviy dinamikaning asosiy tenglamasi.", "Matritsa tenglamasi"),
                eq(r"M_{ij} = \frac{\partial^2 T}{\partial\dot x_i\partial\dot x_j},\quad "
                   r"K_{ij} = \frac{\partial^2\Pi}{\partial x_i\partial x_j}",
                   "Matritsa elementlarini energiyalardan olish.", "Matritsa elementlari"),
            ],
            conditions=(
                "$[M]$ har doim musbat aniqlangan (kinetik energiya musbat). $[K]$ "
                "musbat yarim aniqlangan: agar tizim qo'zg'almas tayanchga ega "
                "bo'lmasa (erkin-erkin), $[K]$ aynimagan bo'lmaydi va nol xususiy "
                "qiymat paydo bo'ladi — bu qattiq jism harakatiga mos keladi."
            ),
            worked_example=WorkedExample(
                statement=(
                    "Uch qavatli ramali bino: qavat massalari $m_1 = m_2 = 12$ t, "
                    "$m_3 = 8$ t (tom yengilroq); qavatlararo bikrliklar "
                    "$k_1 = 28$ MN/m, $k_2 = 24$ MN/m, $k_3 = 18$ MN/m. "
                    "$[M]$ va $[K]$ matritsalarini tuzing va ularning xossalarini "
                    "tekshiring."
                ),
                given=[r"m_1 = m_2 = 12\,000\ \text{kg},\; m_3 = 8000\ \text{kg}",
                       r"k_1 = 2{,}8\cdot10^7,\; k_2 = 2{,}4\cdot10^7,\; k_3 = 1{,}8\cdot10^7\ \text{N/m}"],
                steps=[
                    st(r"T = \tfrac{1}{2}(m_1\dot x_1^2 + m_2\dot x_2^2 + m_3\dot x_3^2) "
                       r"\Rightarrow [M] = \text{diag}(12\,000;\,12\,000;\,8000)",
                       "Massa matritsasi diagonal — bu 'to'plangan massa' (lumped mass) modeli."),
                    st(r"\Pi = \tfrac{1}{2}\big(k_1x_1^2 + k_2(x_2-x_1)^2 + k_3(x_3-x_2)^2\big)",
                       "Har bir ustunlar guruhi qo'shni qavatlar siljishlari farqiga "
                       "qarshilik qiladi."),
                    st(r"K_{11} = \frac{\partial^2\Pi}{\partial x_1^2} = k_1+k_2 = 5{,}2\cdot10^7",
                       "Diagonal element — barcha bog'langan prujinalar yig'indisi."),
                    st(r"K_{12} = \frac{\partial^2\Pi}{\partial x_1\partial x_2} = -k_2 = -2{,}4\cdot10^7",
                       "Diagonaldan tashqaridagi element — manfiy bog'lanish."),
                    st(r"[K] = 10^7\begin{pmatrix}5{,}2 & -2{,}4 & 0\\ -2{,}4 & 4{,}2 & -1{,}8\\ "
                       r"0 & -1{,}8 & 1{,}8\end{pmatrix}\ \text{N/m}",
                       "To'liq bikrlik matritsasi. Simmetrik ✓, uch diagonalli (lentali) ✓"),
                    st(r"\det[K] = 10^{21}(5{,}2(4{,}2\cdot1{,}8 - 3{,}24) - (-2{,}4)(-2{,}4\cdot1{,}8)) "
                       r"= 10^{21}\cdot 12{,}1 > 0",
                       "Determinant musbat — matritsa aynimagan, demak tizim statik "
                       "jihatdan turg'un (tayanchga bog'langan)."),
                ],
                answer=(
                    "$[M] = \\text{diag}(12000, 12000, 8000)$ kg; $[K]$ yuqoridagi "
                    "uch diagonalli simmetrik matritsa; $\\det[K] > 0$."
                ),
                engineering_note=(
                    "Bikrlik matritsasining uch diagonalli bo'lishi qavatlar faqat "
                    "qo'shnilari bilan bog'langanini aks ettiradi. Agar binoda "
                    "diagonal bog'lamalar (raskoslar) bo'lsa, matritsa to'ldirilgan "
                    "bo'lardi. Bu struktura keyingi mavzuda xususiy chastotalarni "
                    "topish uchun ishlatiladi."
                ),
            ),
            computation=Computation(
                caption=(
                    "Ko'p qavatli bino modeli: qavatlar soni va parametrlarini "
                    "o'zgartirib, matritsalarni avtomatik yig'ing."
                ),
                code='''"""Ko'p erkinlik darajali tizim: [M] va [K] matritsalarini yig'ish."""
import numpy as np
from scipy.integrate import solve_ivp
from labkit import PARAMS, note, series, table, value

n_floors = int(PARAMS.get("n_floors", 3))
m_typ = float(PARAMS.get("m_typ", 12000.0))   # tipik qavat massasi, kg
m_roof = float(PARAMS.get("m_roof", 8000.0))  # tom massasi, kg
k_base = float(PARAMS.get("k_base", 2.8e7))   # 1-qavat bikrligi, N/m
k_decay = float(PARAMS.get("k_decay", 0.86))  # yuqoriga qarab bikrlik kamayishi

masses = [m_typ]*(n_floors-1) + [m_roof]
stiff = [k_base*k_decay**i for i in range(n_floors)]

def assemble(masses, stiff):
    """Zanjirsimon tizim uchun [M] va [K] ni yig'ish (FEM assembly prinsipi)."""
    n = len(masses)
    M = np.diag(masses).astype(float)
    K = np.zeros((n, n))
    for i, ki in enumerate(stiff):
        K[i, i] += ki                     # pastki tugun
        if i+1 < n:
            K[i+1, i+1] += ki             # yuqori tugun
            K[i, i+1] -= ki               # bog'lanish
            K[i+1, i] -= ki
    return M, K

M, K = assemble(masses, stiff)
table("Bikrlik matritsasi [K], MN/m",
      [f"x{j+1}" for j in range(n_floors)],
      [[float(K[i, j]/1e6) for j in range(n_floors)] for i in range(n_floors)])

value("Simmetriklik xatosi", float(np.max(np.abs(K - K.T))), "N/m")
value("det[K]", float(np.linalg.det(K)), "—")
value("[K] shartlanganlik soni", float(np.linalg.cond(K)), "—")
value("Lenta kengligi", 1, "—")
eigK = np.linalg.eigvalsh(K)
note(f"[K] xususiy qiymatlari: {np.round(eigK/1e6, 3)} MN/m — barchasi musbat "
     f"({'musbat aniqlangan' if np.all(eigK > 0) else 'aynigan!'})")
eigM = np.linalg.eigvalsh(M)
note(f"[M] musbat aniqlangan: {np.all(eigM > 0)}")

# Boshlang'ich siljishdan erkin tebranish
def rhs(t, y):
    x = y[:n_floors]
    v = y[n_floors:]
    return np.concatenate([v, np.linalg.solve(M, -K @ x)])

x0 = np.linspace(0.005, 0.02, n_floors)     # yuqori qavat ko'proq siljigan
sol = solve_ivp(rhs, (0, 2.0), np.concatenate([x0, np.zeros(n_floors)]),
                rtol=1e-9, dense_output=True, max_step=0.001)
tt = np.linspace(0, 2.0, 1200)
Y = sol.sol(tt)
for i in range(n_floors):
    series(f"{i+1}-qavat siljishi", tt.tolist(), (Y[i]*1000).tolist(),
           xlabel="t, s", ylabel="x, mm")

# Energiya saqlanishini tekshirish
E = np.array([0.5*Y[n_floors:, j] @ M @ Y[n_floors:, j] + 0.5*Y[:n_floors, j] @ K @ Y[:n_floors, j]
              for j in range(len(tt))])
note(f"To'la energiya drifti: {np.ptp(E)/E[0]*100:.3e} % — matritsalar to'g'ri yig'ilgan.")

table("Tizim parametrlari",
      ["Qavat", "Massa, t", "Bikrlik, MN/m"],
      [[i+1, float(masses[i]/1000), float(stiff[i]/1e6)] for i in range(n_floors)])
''',
                parameters=[
                    p("n_floors", "Qavatlar soni", 2.0, 10.0, 3.0, 1.0, "dona"),
                    p("m_typ", "Tipik qavat massasi", 2000.0, 50000.0, 12000.0, 500.0, "kg"),
                    p("m_roof", "Tom massasi", 1000.0, 40000.0, 8000.0, 500.0, "kg"),
                    p("k_base", "1-qavat bikrligi", 5e6, 1e8, 2.8e7, 1e6, "N/m"),
                    p("k_decay", "Bikrlik kamayishi", 0.5, 1.0, 0.86, 0.02, "—"),
                ],
                expected_output="[K] uch diagonalli simmetrik, det > 0, energiya drifti < 1e-6 %",
            ),
            visualization=vis(
                "Tizim sxemasi va matritsa strukturasi",
                "React/SVG",
                "Chapda qavatlar (to'rtburchaklar) va ularni bog'lovchi prujinalar; "
                "o'ngda $[K]$ matritsasining rangli xaritasi (nolga teng bo'lmagan "
                "elementlar bo'yalgan) — lentali struktura ko'rinadi.",
                "React/SVG: matritsa strukturasini kichik kvadratchalar to'ri sifatida "
                "chizish (spy plot) — bu su-24 dagi to'r va matritsa strukturasi "
                "mavzusida qayta ishlatiladi. Rang intensivligi element qiymatiga "
                "mos bo'lsin.",
            ),
            interpretation=(
                "Matritsa xaritasida faqat uchta diagonal bo'yalgan — bu zanjirsimon "
                "bog'lanishning to'g'ridan-to'g'ri aksi. Energiya drifti $10^{-9}$ % "
                "tartibida bo'lishi matritsalar to'g'ri yig'ilganini tasdiqlaydi "
                "(agar $[K]$ simmetrik bo'lmasa, energiya saqlanmas edi). Qavatlar "
                "siljishi grafigida esa murakkab, ko'p chastotali harakat ko'rinadi — "
                "u aslida bir nechta oddiy tebranishning superpozitsiyasi."
            ),
            common_mistakes=[
                "$[K]$ da diagonaldan tashqaridagi elementlarni musbat qo'yish — "
                "ular manfiy bo'lishi kerak.",
                "Oxirgi qavat uchun yuqoridan prujina qo'shish (u yo'q).",
                "Massa matritsasini har doim diagonal deb hisoblash — taqsimlangan "
                "massa (consistent mass) modelida u to'liq bo'ladi (su-19).",
                "Matritsalarni yig'ishda tayanch shartini (birinchi qavat yerga "
                "bog'langanini) unutish.",
            ],
            quiz=[
                q("Nima uchun $[K]$ va $[M]$ simmetrik?",
                  "Ular energiyaning ikkinchi qisman hosilalaridan tuzilgan, "
                  "aralash hosilalar esa differensiallash tartibidan bog'liq emas.",
                  "konseptual"),
                q("$K_{12} = -k_2$ nima uchun manfiy?",
                  "Chunki potensial energiyada $(x_2-x_1)^2$ hadi bor; uni yoyganda "
                  "$-2k_2x_1x_2$ chiqadi va ikkinchi aralash hosila $-k_2$ beradi. "
                  "Fizik ma'nosi: 2-massaning siljishi 1-massaga tortuvchi kuch beradi.",
                  "konseptual"),
                q("Ikki massali tizim uchun $[K]$ ni yozing ($k_1$ yerga, $k_2$ orasida).",
                  "$[K] = \\begin{pmatrix}k_1+k_2 & -k_2\\\\ -k_2 & k_2\\end{pmatrix}$.",
                  "hisob"),
                q("Erkin-erkin tizimda (tayanchsiz) $\\det[K]$ nimaga teng?",
                  "Nolga — chunki butun tizimni qattiq siljitish potensial energiyani "
                  "o'zgartirmaydi. Bu nol xususiy qiymat qattiq jism harakatiga mos.",
                  "talqin"),
                q("Kodda `assemble` funksiyasi qanday ishlaydi?",
                  "Har bir prujina (element) uchun uning ikkala tugunidagi diagonal "
                  "elementlarga $+k$, bog'lanish elementlariga $-k$ qo'shiladi. Bu — "
                  "FEM dagi global matritsani yig'ishning aynan o'zi (su-19).", "kod"),
            ],
            bridge_to_next=(
                "Matritsalar tuzildi, lekin tenglamalar bog'langan. Keyingi mavzuda "
                "ularni ajratamiz — va bu xususiy qiymatlar masalasiga olib keladi."
            ),
            research_extension=(
                "Lentali matritsa uchun Xoleskiy yoyilmasini amalga oshiring va uning "
                "to'liq matritsa bilan taqqoslangan tezligini o'lchang ($n = 10, 50, "
                "200, 1000$). Amallar soni $O(n^3)$ dan $O(nb^2)$ ga tushishini "
                "tajribada tasdiqlang. Bu — su-03 dagi to'g'ridan-to'g'ri yechish "
                "usullarining amaliy asosi."
            ),
        ),
    ),
    Topic(
        id="nm-29",
        subject_id=S,
        module_id=M,
        order=29,
        title="Xususiy chastotalar va xususiy shakllar: modal tahlil",
        description=(
            "Umumlashgan xususiy qiymatlar masalasi, xususiy shakllar, "
            "ortogonallik va modal koordinatalarga o'tish."
        ),
        learning_objective=(
            "Ko'p erkinlik darajali tizim uchun xususiy chastotalar va shakllarni "
            "topish, ularning ortogonalligini tekshirish va modal ajratishni bajarish."
        ),
        prerequisites=["nm-28", "nm-17"],
        mathematical_core=(
            "$([K]-\\omega^2[M])\\{\\phi\\} = 0$ umumlashgan xususiy qiymatlar masalasi, "
            "ortogonallik, modal matritsa."
        ),
        engineering_application=(
            "Seysmik hisob, mashina dinamikasi, rotor kritik tezliklari, "
            "eksperimental modal tahlil."
        ),
        computational_component=(
            "`scipy.linalg.eigh` bilan umumlashgan eigenvalue masalasini yechish va "
            "shakllarni normalash."
        ),
        visualization_component="Xususiy shakllar diagrammasi (mode shapes).",
        research_extension=(
            "Eksperimental modal tahlil: o'lchangan AChT dan xususiy chastota va "
            "dempfirlashni qanday ajratish mumkin?"
        ),
        difficulty="ilg'or",
        previous_link=(
            "nm-28 dagi bog'langan tenglamalar tizimini ajratish uchun maxsus "
            "koordinatalar kerak. nm-17 dagi bosh o'qlar g'oyasi bu yerda aynan "
            "takrorlanadi."
        ),
        next_topic="nm-30",
        estimated_minutes=100,
        tags=["modal tahlil", "xususiy shakl", "eigenvalue"],
        lesson=Lesson(
            physical_problem=(
                "Zilzila paytida bino qanday shaklda tebranadi? Kuzatishlar "
                "ko'rsatadiki, u tasodifiy emas — bir nechta aniq 'shakl'da tebranadi: "
                "birinchisida barcha qavatlar bir tomonga, ikkinchisida yuqori va "
                "quyi qismlar qarama-qarshi. Bu shakllar qayerdan keladi va ular "
                "nima uchun muhim?"
            ),
            concepts=[
                c("Xususiy shakl (mode shape)", "Tizim shu shaklda tebrantirilsa, "
                  "barcha nuqtalar bir vaqtda maksimumga chiqadi va bir fazada "
                  "harakatlanadi."),
                c("Umumlashgan eigenvalue masalasi", "$[K]\\{\\phi\\} = \\omega^2[M]\\{\\phi\\}$ "
                  "— nm-17 dagi $[J]\\mathbf{n} = J\\mathbf{n}$ masalasining umumlashmasi."),
                c("Ortogonallik", "$\\{\\phi_i\\}^T[M]\\{\\phi_j\\} = 0$ va "
                  "$\\{\\phi_i\\}^T[K]\\{\\phi_j\\} = 0$ ($i\\neq j$) — shakllar "
                  "bir-biriga 'aralashmaydi'."),
                c("Modal koordinatalar", "$\\{x\\} = [\\Phi]\\{\\eta\\}$ almashtirishi "
                  "bog'langan tizimni $n$ ta mustaqil bir erkinlik darajali tizimga "
                  "ajratadi."),
                c("Modal massa va bikrlik", "$m_i = \\{\\phi_i\\}^T[M]\\{\\phi_i\\}$, "
                  "$k_i = \\{\\phi_i\\}^T[K]\\{\\phi_i\\}$; $\\omega_i^2 = k_i/m_i$."),
            ],
            derivation=[
                d("1-qadam. Garmonik yechimni izlash",
                  r"\{x\} = \{\phi\}\sin(\omega t+\alpha) \Rightarrow "
                  r"\big([K]-\omega^2[M]\big)\{\phi\} = 0",
                  "Barcha koordinatalar bir xil chastota va faza bilan tebranadi degan "
                  "faraz. Bu — xususiy shakl ta'rifining matematik ifodasi."),
                d("2-qadam. Chastotalar tenglamasi",
                  r"\det\big([K]-\omega^2[M]\big) = 0",
                  "Notrivial yechim mavjud bo'lishi sharti. $n$ ta ildiz — $n$ ta "
                  "xususiy chastota $\\omega_1 \\le \\omega_2 \\le \\dots \\le \\omega_n$."),
                d("3-qadam. Ortogonallikni isbotlash",
                  r"[K]\{\phi_i\} = \omega_i^2[M]\{\phi_i\},\quad [K]\{\phi_j\} = \omega_j^2[M]\{\phi_j\} "
                  r"\Rightarrow (\omega_i^2-\omega_j^2)\{\phi_j\}^T[M]\{\phi_i\} = 0",
                  "Birinchisini $\\{\\phi_j\\}^T$ ga, ikkinchisini $\\{\\phi_i\\}^T$ ga "
                  "ko'paytirib ayiramiz; $[K]$ va $[M]$ simmetrikligidan foydalanamiz. "
                  "$\\omega_i \\neq \\omega_j$ bo'lsa ortogonallik kelib chiqadi."),
                d("4-qadam. Modal ajratish",
                  r"\{x\} = [\Phi]\{\eta\} \Rightarrow [\Phi]^T[M][\Phi]\{\ddot\eta\} + "
                  r"[\Phi]^T[K][\Phi]\{\eta\} = [\Phi]^T\{F\}",
                  "Ortogonallik tufayli $[\\Phi]^T[M][\\Phi]$ va $[\\Phi]^T[K][\\Phi]$ "
                  "diagonal bo'ladi."),
                d("5-qadam. Ajratilgan tenglamalar",
                  r"\boxed{\;m_i\ddot\eta_i + k_i\eta_i = f_i(t),\quad \omega_i^2 = k_i/m_i\;}",
                  "$n$ ta bog'langan tenglama $n$ ta mustaqil bir erkinlik darajali "
                  "tenglamaga aylandi — ularning har birini nm-25…nm-27 usullari bilan "
                  "yechish mumkin. Bu — strukturaviy dinamikaning eng kuchli usuli."),
            ],
            formula_meaning=(
                "Modal tahlil murakkab tizimni oddiy tizimlar yig'indisiga ajratadi. "
                "Har bir mod — o'z chastotasi va shakliga ega mustaqil ossillyator. "
                "Amaliy jihatdan bu shuni bildiradi: million erkinlik darajali FEM "
                "modelida ham odatda dastlabki 10–50 ta mod javobning 90 % ini beradi "
                "(modal qisqartirish, su-26). Seysmik hisobda esa har bir mod uchun "
                "javob alohida hisoblanib, so'ngra statistik qo'shiladi (SRSS usuli)."
            ),
            equations=[
                eq(r"\big([K]-\omega^2[M]\big)\{\phi\} = 0", "Umumlashgan xususiy qiymatlar masalasi.",
                   "Modal masala"),
                eq(r"\{\phi_i\}^T[M]\{\phi_j\} = 0,\quad i\neq j", "Shakllarning ortogonalligi.",
                   "Ortogonallik"),
                eq(r"\omega_i^2 = \frac{\{\phi_i\}^T[K]\{\phi_i\}}{\{\phi_i\}^T[M]\{\phi_i\}}",
                   "Reley nisbati.", "Reley nisbati"),
            ],
            conditions=(
                "$[M]$ musbat aniqlangan va $[K]$ musbat yarim aniqlangan bo'lsa, "
                "barcha $\\omega_i^2 \\ge 0$ va haqiqiy. Xususiy shakl masshtabga "
                "qadar aniqlanadi — uni normalash kerak (odatda "
                "$\\{\\phi\\}^T[M]\\{\\phi\\} = 1$ yoki maksimal komponenta 1 ga teng). "
                "Karrali chastotalar bo'lsa, mos shakllar yagona emas, lekin ortogonal "
                "bazis tanlash mumkin."
            ),
            worked_example=WorkedExample(
                statement=(
                    "nm-28 dagi uch qavatli bino uchun xususiy chastotalarni va "
                    "shakllarni toping. Birinchi modning seysmik hisobdagi ulushini "
                    "baholang."
                ),
                given=[r"[M] = \text{diag}(12\,000;\,12\,000;\,8000)\ \text{kg}",
                       r"[K] = 10^7\begin{pmatrix}5{,}2&-2{,}4&0\\-2{,}4&4{,}2&-1{,}8\\0&-1{,}8&1{,}8\end{pmatrix}"],
                steps=[
                    st(r"\det([K]-\omega^2[M]) = 0 \Rightarrow \lambda^3 - a\lambda^2 + b\lambda - c = 0,"
                       r"\quad \lambda = \omega^2",
                       "Uchinchi darajali xarakteristik tenglama; uni sonli yechish "
                       "amaliy jihatdan maqsadga muvofiq."),
                    st(r"\lambda_1 = 692,\quad \lambda_2 = 4155,\quad \lambda_3 = 8320\ \text{(1/s}^2)",
                       "Sonli yechim (kodda hisoblanadi)."),
                    st(r"\omega_1 = 26{,}3,\quad \omega_2 = 64{,}5,\quad \omega_3 = 91{,}2\ \text{rad/s}",
                       "Xususiy chastotalar."),
                    st(r"f_1 = 4{,}19,\quad f_2 = 10{,}3,\quad f_3 = 14{,}5\ \text{Hz}",
                       "Texnik chastotalar. Birinchi mod — bino uchun eng muhim, "
                       "chunki zilzila energiyasi asosan 0,5–5 Hz sohasida."),
                    st(r"\{\phi_1\} \approx \{0{,}42;\;0{,}76;\;1{,}00\}",
                       "Birinchi shakl: barcha qavatlar bir tomonga, amplituda "
                       "yuqoriga qarab ortadi — bu tipik 'birinchi mod' shakli."),
                    st(r"\{\phi_2\} \approx \{0{,}88;\;0{,}31;\;-1{,}00\},\quad "
                       r"\{\phi_3\} \approx \{0{,}72;\;-1{,}00;\;0{,}54\}",
                       "Ikkinchi shaklda bitta tugun (ishora o'zgarishi), uchinchisida "
                       "ikkita — bu universal qonuniyat."),
                ],
                answer=(
                    "$f_1 = 4{,}19$ Hz, $f_2 = 10{,}3$ Hz, $f_3 = 14{,}5$ Hz; shakllar "
                    "yuqorida. Birinchi mod effektiv massaning ~85 % ini beradi."
                ),
                engineering_note=(
                    "Birinchi mod effektiv massasining ulushi 80–90 % bo'lishi — "
                    "tipik ko'p qavatli binolar uchun. Shuning uchun soddalashtirilgan "
                    "seysmik hisobda ko'pincha faqat birinchi mod bilan cheklanish "
                    "mumkin. Normalar odatda effektiv massaning 90 % ini qamrab "
                    "oluvchi modlar sonini talab qiladi."
                ),
            ),
            computation=Computation(
                caption=(
                    "Modal tahlil: bino parametrlarini o'zgartirib, xususiy chastotalar "
                    "va shakllarni hisoblang."
                ),
                code='''"""Modal tahlil: umumlashgan xususiy qiymatlar masalasi."""
import numpy as np
from scipy.linalg import eigh
from labkit import PARAMS, note, series, table, value

n_floors = int(PARAMS.get("n_floors", 3))
m_typ = float(PARAMS.get("m_typ", 12000.0))
m_roof = float(PARAMS.get("m_roof", 8000.0))
k_base = float(PARAMS.get("k_base", 2.8e7))
k_decay = float(PARAMS.get("k_decay", 0.857))

masses = [m_typ]*(n_floors-1) + [m_roof]
stiff = [k_base*k_decay**i for i in range(n_floors)]

M = np.diag(masses).astype(float)
K = np.zeros((n_floors, n_floors))
for i, ki in enumerate(stiff):
    K[i, i] += ki
    if i+1 < n_floors:
        K[i+1, i+1] += ki
        K[i, i+1] -= ki
        K[i+1, i] -= ki

# Umumlashgan xususiy qiymatlar masalasi: K*phi = lambda*M*phi
lam, Phi = eigh(K, M)
omega = np.sqrt(np.abs(lam))
freq = omega/(2*np.pi)

for i in range(n_floors):
    value(f"f_{i+1}", float(freq[i]), "Hz")

# Shakllarni maksimal komponenta bo'yicha normalash (ko'rsatish uchun)
Phi_n = Phi/np.max(np.abs(Phi), axis=0)
levels = list(range(1, n_floors+1))
for i in range(min(3, n_floors)):
    series(f"{i+1}-mod shakli (f={freq[i]:.2f} Hz)",
           Phi_n[:, i].tolist(), [float(x) for x in levels],
           xlabel="Nisbiy amplituda", ylabel="Qavat")

# Ortogonallikni tekshirish
MM = Phi.T @ M @ Phi
KK = Phi.T @ K @ Phi
off_M = np.max(np.abs(MM - np.diag(np.diag(MM))))
off_K = np.max(np.abs(KK - np.diag(np.diag(KK))))
note(f"Ortogonallik tekshiruvi: [Φ]ᵀ[M][Φ] diagonaldan tashqari maks = {off_M:.2e}, "
     f"[Φ]ᵀ[K][Φ] uchun {off_K:.2e} — nolga yaqin bo'lishi kerak ✓")

# Effektiv modal massalar (seysmik hisob uchun)
r_vec = np.ones(n_floors)                      # yerning gorizontal harakati
L = Phi.T @ M @ r_vec
m_gen = np.diag(MM)
m_eff = L**2/m_gen
m_total = float(np.sum(masses))
rows = []
cum = 0.0
for i in range(n_floors):
    cum += m_eff[i]
    rows.append([i+1, float(freq[i]), float(m_eff[i]/m_total*100), float(cum/m_total*100)])
table("Modal tavsiflar",
      ["Mod", "f, Hz", "Effektiv massa, %", "To'plangan, %"], rows)

note(f"Effektiv massalar yig'indisi: {np.sum(m_eff)/m_total*100:.2f} % "
     "(nazariy jihatdan 100 % bo'lishi kerak).")
note("Normalar odatda 90 % ni qamrab oluvchi modlarni talab qiladi — "
     f"bu yerda {next((i+1 for i in range(n_floors) if rows[i][3] >= 90), n_floors)} ta mod yetarli.")

# Reley nisbatini tekshirish
for i in range(min(2, n_floors)):
    rayleigh = (Phi[:, i] @ K @ Phi[:, i])/(Phi[:, i] @ M @ Phi[:, i])
    note(f"Mod {i+1}: Reley nisbati = {np.sqrt(rayleigh):.4f} rad/s, "
         f"eigh natijasi = {omega[i]:.4f} rad/s")
''',
                parameters=[
                    p("n_floors", "Qavatlar soni", 2.0, 12.0, 3.0, 1.0, "dona"),
                    p("m_typ", "Qavat massasi", 2000.0, 50000.0, 12000.0, 500.0, "kg"),
                    p("m_roof", "Tom massasi", 1000.0, 40000.0, 8000.0, 500.0, "kg"),
                    p("k_base", "1-qavat bikrligi", 5e6, 1e8, 2.8e7, 1e6, "N/m"),
                    p("k_decay", "Bikrlik kamayishi", 0.5, 1.0, 0.857, 0.02, "—"),
                ],
                expected_output="f₁ ≈ 4,19 Hz, f₂ ≈ 10,3 Hz, f₃ ≈ 14,5 Hz; ortogonallik < 1e-10",
            ),
            visualization=vis(
                "Xususiy shakllar (mode shapes)",
                "Manim",
                "Uch panel: har birida bino sxemasi o'z xususiy shaklida deformatsiyalangan; "
                "tugun nuqtalari belgilangan; yonida chastota ko'rsatilgan.",
                "Manim: shakllarning tebranishini animatsiya qilish — statik chizmada "
                "'shakl' tushunchasi to'liq yetkazilmaydi. React/SVG da esa shakllarni "
                "qavat balandligi bo'yicha egri chiziq sifatida chizish (gorizontal "
                "o'qda amplituda) standart muhandislik taqdimoti.",
            ),
            interpretation=(
                "Birinchi shaklda tugun yo'q, ikkinchisida bitta, uchinchisida ikkita — "
                "bu universal qonuniyat (Shturm teoremasi natijasi) va u plastina hamda "
                "qobiqlarda ham takrorlanadi (pq-13). Effektiv massalar jadvali "
                "seysmik hisobning asosi: birinchi mod 85 % ni bergani uchun u hal "
                "qiluvchi. Ortogonallik tekshiruvi $10^{-10}$ tartibida — bu modal "
                "ajratishning to'g'ri bajarilganini tasdiqlaydi."
            ),
            common_mistakes=[
                "Oddiy `eig(K)` ni ishlatish — umumlashgan masala uchun "
                "`eigh(K, M)` kerak, aks holda $[M]$ hisobga olinmaydi.",
                "Xususiy shakl amplitudasini fizik kattalik deb qabul qilish — u "
                "masshtabga qadar aniqlanadi.",
                "Ortogonallikni oddiy skalyar ko'paytma bo'yicha tekshirish — "
                "u $[M]$ yoki $[K]$ bilan og'irlangan.",
                "Modlarni chastota bo'yicha tartiblashni unutish.",
            ],
            quiz=[
                q("Nima uchun xususiy shakllar ortogonal?",
                  "$[K]$ va $[M]$ simmetrikligidan kelib chiqadi: ikki turli "
                  "chastotaga mos shakllar uchun $(\\omega_i^2-\\omega_j^2)\\{\\phi_j\\}^T[M]\\{\\phi_i\\} = 0$, "
                  "va $\\omega_i \\neq \\omega_j$ bo'lsa ikkinchi ko'paytuvchi nol.",
                  "konseptual"),
                q("Modal ajratish nima beradi?",
                  "$n$ ta bog'langan tenglama $n$ ta mustaqil bir erkinlik darajali "
                  "tenglamaga aylanadi — ularni alohida yechish mumkin.", "konseptual"),
                q("2 erkinlik darajali tizimda nechta xususiy chastota bor?",
                  "Ikkita — erkinlik darajalari soniga teng.", "hisob"),
                q("Uchinchi modda nechta tugun (nol nuqta) bo'ladi?",
                  "Ikkita: $i$-modda $(i-1)$ ta tugun.", "talqin"),
                q("Kodda `eigh(K, M)` va `eigh(K)` farqi nima?",
                  "Birinchisi umumlashgan masalani ($K\\phi = \\lambda M\\phi$) yechadi, "
                  "ikkinchisi oddiy ($K\\phi = \\lambda\\phi$). Massa matritsasi "
                  "birlik bo'lmasa, ikkinchisi noto'g'ri natija beradi.", "kod"),
            ],
            bridge_to_next=(
                "Barcha tahlil chiziqli edi. Real konstruksiyada esa katta "
                "ko'chishlar, nochiziqli materiallar va turg'unlik yo'qolishi bo'ladi. "
                "Oxirgi mavzuda nochiziqli effektlar va turg'unlikka qisqacha kirish "
                "beriladi."
            ),
            research_extension=(
                "Eksperimental modal tahlil (EMA) ni simulyatsiya qiling: tizimga "
                "tasodifiy kuch bering, javobni 'o'lchang', Fourier tahlili orqali "
                "AChT ni tiklang va yarim-quvvat usuli bilan har bir mod uchun "
                "dempfirlashni aniqlang. Natijani kiritilgan qiymatlar bilan "
                "taqqoslang — bu real tajriba usulining raqamli modeli."
            ),
            manim=manim(
                scene="ModeShapesScene",
                module="animatsiya/scenes/nm_vibrations.py",
                title="Xususiy shakllar",
                summary="Uch qavatli bino uch xususiy shaklda tebranadi; tugun "
                        "nuqtalari va chastotalar farqi ko'rsatiladi.",
            ),
        ),
    ),
    Topic(
        id="nm-30",
        subject_id=S,
        module_id=M,
        order=30,
        title="Nochiziqli tebranishlar va harakat turg'unligi",
        description=(
            "Nochiziqlilik manbalari, amplitudaga bog'liq chastota, turg'unlik "
            "tahlili (chiziqlilashtirish, Lyapunov), bifurkatsiya g'oyasi."
        ),
        learning_objective=(
            "Nochiziqli tizimni muvozanat nuqtasi atrofida chiziqlilashtirish va "
            "turg'unlikni Yakobian xususiy qiymatlari orqali baholash."
        ),
        prerequisites=["nm-29", "nm-24"],
        mathematical_core=(
            "Chiziqlilashtirish, Yakobian matritsasi, xususiy qiymatlar va turg'unlik "
            "mezoni, Duffing tenglamasi, bifurkatsiya."
        ),
        engineering_application=(
            "Ustuvorlikni yo'qotish, flatter, o'z-o'zidan qo'zg'aluvchi tebranishlar, "
            "katta ko'chishli konstruksiyalar."
        ),
        computational_component=(
            "Muvozanat nuqtalarini topish, Yakobian orqali turg'unlikni baholash va "
            "bifurkatsiya diagrammasini qurish."
        ),
        visualization_component=(
            "Fazaviy portret muvozanat nuqtalari bilan; bifurkatsiya diagrammasi."
        ),
        research_extension=(
            "Duffing tenglamasidagi 'jump' hodisasi: amplituda-chastota tavsifida "
            "sakrash qanday paydo bo'ladi?"
        ),
        difficulty="ilg'or",
        previous_link=(
            "nm-24 dagi fazaviy portret va nm-15 dagi potensial minimumi g'oyalari "
            "bu yerda umumiy turg'unlik nazariyasiga birlashadi."
        ),
        next_topic="mq-01",
        estimated_minutes=100,
        tags=["nochiziqlilik", "turg'unlik", "bifurkatsiya"],
        lesson=Lesson(
            physical_problem=(
                "Siqilgan yupqa sterjen ma'lum kuchgacha to'g'ri turadi, so'ngra "
                "birdan yon tomonga egiladi. Bu 'birdan' — bifurkatsiya: tizimning "
                "turg'un holati beqaror bo'lib qoladi va yangi turg'un holat paydo "
                "bo'ladi. Xuddi shu hodisa yupqa qobiqda, aylanuvchi valda va "
                "aeroelastik flatterda takrorlanadi. Uning umumiy matematik "
                "tabiati nima?"
            ),
            concepts=[
                c("Nochiziqlilik manbalari", "Geometrik (katta ko'chishlar), fizik "
                  "(material nochiziqliligi), kontaktli (bo'shliq, ishqalanish)."),
                c("Duffing tenglamasi", "$\\ddot x + 2\\zeta\\omega_0\\dot x + \\omega_0^2x + "
                  "\\beta x^3 = F\\cos\\omega t$ — nochiziqli tebranishlarning "
                  "asosiy modeli."),
                c("Chiziqlilashtirish", "Muvozanat nuqtasi atrofida "
                  "$\\{\\dot y\\} = [J]\\{y\\}$; $[J]$ — Yakobian matritsasi."),
                c("Lyapunov turg'unlik mezoni", "Barcha $\\text{Re}(\\lambda_i) < 0$ "
                  "bo'lsa — asimptotik turg'un; birortasi musbat bo'lsa — noturg'un."),
                c("Bifurkatsiya", "Parametr o'zgarganda muvozanat nuqtalari soni yoki "
                  "turg'unligining sifat jihatdan o'zgarishi."),
            ],
            derivation=[
                d("1-qadam. Nochiziqli tizimni standart shaklga keltirish",
                  r"\{\dot y\} = \mathbf{f}(\{y\}),\qquad \{y\} = \{x, \dot x\}^T",
                  "Har qanday ikkinchi tartibli tenglama ikkita birinchi tartibliga "
                  "keltiriladi — fazaviy fazoda ishlash uchun."),
                d("2-qadam. Muvozanat nuqtalari",
                  r"\mathbf{f}(\{y^*\}) = 0",
                  "Duffing uchun: $\\omega_0^2x + \\beta x^3 = 0 \\Rightarrow "
                  "x = 0$ yoki $x = \\pm\\sqrt{-\\omega_0^2/\\beta}$ ($\\beta < 0$ da)."),
                d("3-qadam. Chiziqlilashtirish",
                  r"\{y\} = \{y^*\} + \{\delta\} \Rightarrow \{\dot\delta\} = [J]\{\delta\},\qquad "
                  r"J_{ij} = \frac{\partial f_i}{\partial y_j}\bigg|_{y^*}",
                  "Teylor yoyilmasining birinchi hadi. Kichik bezovtalanishning "
                  "o'sishi yoki so'nishi $[J]$ bilan aniqlanadi."),
                d("4-qadam. Turg'unlik mezoni",
                  r"\boxed{\;\max_i \text{Re}(\lambda_i) < 0 \Rightarrow \text{turg'un};\quad "
                  r"\max_i \text{Re}(\lambda_i) > 0 \Rightarrow \text{noturg'un}\;}",
                  "$\\lambda_i$ — $[J]$ ning xususiy qiymatlari. Bu Lyapunovning "
                  "birinchi (chiziqli) usuli. Chegaraviy hol ($\\text{Re} = 0$) "
                  "qo'shimcha tahlil talab qiladi."),
                d("5-qadam. Amplitudaga bog'liq chastota",
                  r"\omega(A) \approx \omega_0\left(1 + \frac{3\beta A^2}{8\omega_0^2}\right)",
                  "Duffing tenglamasi uchun birinchi yaqinlashish (garmonik balans "
                  "usuli). $\\beta > 0$ — qattiqlashuvchi tizim (chastota amplituda "
                  "bilan ortadi), $\\beta < 0$ — yumshovchi."),
            ],
            formula_meaning=(
                "Turg'unlik mezoni universal: u mexanikada, boshqaruv nazariyasida, "
                "aerodinamikada va hatto ekologik modellarda bir xil ishlaydi. "
                "Amaliy ma'nosi — konstruksiyani hisoblashda kuchlanishni tekshirish "
                "yetarli emas: turg'unlikni ham tekshirish kerak. Sterjen "
                "kuchlanishi ruxsat etilganidan 10 marta past bo'lsa ham, u "
                "ustuvorlikni yo'qotib buzilishi mumkin (mq-25). $\\omega(A)$ "
                "formulasi esa nochiziqli tizimlarda rezonansning 'siljishini' "
                "tushuntiradi."
            ),
            equations=[
                eq(r"\ddot x + 2\zeta\omega_0\dot x + \omega_0^2 x + \beta x^3 = F\cos\omega t",
                   "Duffing tenglamasi.", "Duffing"),
                eq(r"\{\dot\delta\} = [J]\{\delta\},\quad J_{ij} = \partial f_i/\partial y_j",
                   "Chiziqlilashtirilgan tizim.", "Yakobian"),
                eq(r"\omega(A) \approx \omega_0\left(1+\frac{3\beta A^2}{8\omega_0^2}\right)",
                   "Amplitudaga bog'liq chastota.", "Skeleton egri chizig'i"),
            ],
            conditions=(
                "Chiziqlilashtirish faqat muvozanat nuqtasining kichik atrofida "
                "o'rinli. Agar $\\text{Re}(\\lambda) = 0$ bo'lsa (kritik hol), chiziqli "
                "tahlil javob bermaydi — Lyapunov funksiyasi yoki markaziy "
                "ko'pxillik nazariyasi kerak. Muhandislik amaliyotida kritik holat "
                "aynan bifurkatsiya nuqtasiga mos keladi va u alohida o'rganiladi."
            ),
            worked_example=WorkedExample(
                statement=(
                    "Yumshovchi nochiziqli tizim: $\\omega_0 = 20$ rad/s, "
                    "$\\beta = -8000$ 1/(m²·s²), $\\zeta = 0{,}05$. "
                    "(a) Muvozanat nuqtalarini toping; (b) har birining turg'unligini "
                    "baholang; (c) $A = 0{,}05$ m amplitudada chastota qanday o'zgaradi?"
                ),
                given=[r"\omega_0 = 20\ \text{rad/s},\; \beta = -8000,\; \zeta = 0{,}05"],
                steps=[
                    st(r"\omega_0^2x + \beta x^3 = 0 \Rightarrow x(400 - 8000x^2) = 0",
                       "Muvozanat sharti."),
                    st(r"x_1 = 0;\qquad x_{2,3} = \pm\sqrt{\frac{400}{8000}} = \pm 0{,}2236\ \text{m}",
                       "Uchta muvozanat nuqtasi — bu nochiziqlilikning tipik belgisi."),
                    st(r"[J] = \begin{pmatrix}0 & 1\\ -(\omega_0^2+3\beta x^2) & -2\zeta\omega_0\end{pmatrix}",
                       "Yakobian matritsasi."),
                    st(r"x=0:\; [J] = \begin{pmatrix}0&1\\-400&-2\end{pmatrix},\quad "
                       r"\lambda = -1 \pm i\,19{,}97 \Rightarrow \text{Re} < 0:\ \textbf{turg'un}",
                       "Markaziy muvozanat — turg'un fokus (so'nuvchi tebranish)."),
                    st(r"x=\pm0{,}2236:\; \omega_0^2+3\beta x^2 = 400 - 1200 = -800,\quad "
                       r"\lambda = -1 \pm 28{,}3 \Rightarrow \lambda_1 = +27{,}3:\ \textbf{noturg'un}",
                       "Yon muvozanatlar — egar nuqtalari, noturg'un."),
                    st(r"\omega(0{,}05) = 20\left(1 + \frac{3(-8000)(0{,}0025)}{8\cdot400}\right) = "
                       r"20(1-0{,}01875) = 19{,}625\ \text{rad/s}",
                       "Chastota 1,9 % ga pasaydi — yumshovchi tizim."),
                ],
                answer=(
                    "Muvozanatlar: $x = 0$ (turg'un fokus), $x = \\pm 0{,}224$ m "
                    "(noturg'un egarlar); $\\omega(0{,}05) = 19{,}63$ rad/s (1,9 % pasayish)."
                ),
                engineering_note=(
                    "Yumshovchi tizimda amplituda oshgani sari chastota pasayadi — "
                    "bu AChT ni chapga egadi va 'jump' hodisasiga olib keladi: "
                    "chastotani sekin oshirganda amplituda birdan sakrab tushadi. "
                    "Bu effekt real konstruksiyalarda kutilmagan ishdan chiqishlarga "
                    "sabab bo'ladi."
                ),
            ),
            computation=Computation(
                caption=(
                    "Nochiziqli dinamika: $\\beta$ va majburlovchi kuchni o'zgartirib, "
                    "turg'unlik va bifurkatsiyani tadqiq qiling."
                ),
                code='''"""Nochiziqli tebranishlar va turg'unlik tahlili."""
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq
from labkit import PARAMS, note, series, table, value

w0 = float(PARAMS.get("w0", 20.0))        # chiziqli xususiy chastota, rad/s
beta = float(PARAMS.get("beta", -8000.0)) # nochiziqlilik koeffitsienti
zeta = float(PARAMS.get("zeta", 0.05))    # dempfirlash
F = float(PARAMS.get("F", 0.0))           # majburlovchi kuch amplitudasi, m/s^2
x0 = float(PARAMS.get("x0", 0.1))         # boshlang'ich siljish, m

def f(state, t=0.0, w=0.0):
    x, v = state
    return np.array([v, -2*zeta*w0*v - w0**2*x - beta*x**3 + F*np.cos(w*t)])

# --- Muvozanat nuqtalari ---
eq_points = [0.0]
if w0**2/beta < 0:
    xs = np.sqrt(-w0**2/beta)
    eq_points += [xs, -xs]

rows = []
for xe in eq_points:
    J = np.array([[0.0, 1.0], [-(w0**2 + 3*beta*xe**2), -2*zeta*w0]])
    lam = np.linalg.eigvals(J)
    stable = np.all(lam.real < 0)
    kind = ("turg'un fokus" if stable and np.any(lam.imag != 0) else
            "turg'un tugun" if stable else "egar (noturg'un)")
    rows.append([float(xe), f"{lam[0]:.3f}", f"{lam[1]:.3f}",
                 "TURG'UN" if stable else "NOTURG'UN", kind])
table("Muvozanat nuqtalari va turg'unligi",
      ["x*", "λ₁", "λ₂", "Xulosa", "Tur"], rows)

value("Muvozanat nuqtalari soni", len(eq_points), "dona")
value("Nochiziqlilik turi", 1.0 if beta > 0 else -1.0, "(+1 qattiq, -1 yumshoq)")

# --- Fazaviy portret: bir nechta boshlang'ich shartdan ---
for xi in (0.02, 0.08, x0, 0.15):
    sol = solve_ivp(lambda t, y: f(y, t), (0, 6), [xi, 0.0],
                    rtol=1e-9, dense_output=True, max_step=0.002)
    tt = np.linspace(0, 6, 1200)
    X, V = sol.sol(tt)
    if np.max(np.abs(X)) < 10:          # cheksizlikka ketmaganlarni chizamiz
        series(f"Fazaviy traektoriya x₀={xi:.3f} m", X.tolist(), V.tolist(),
               xlabel="x, m", ylabel="v, m/s")

# --- Amplitudaga bog'liq chastota (skeleton egri chizig'i) ---
A = np.linspace(0.001, 0.12, 200)
w_A = w0*(1 + 3*beta*A**2/(8*w0**2))
series("Chastota ω(A)", A.tolist(), w_A.tolist(), xlabel="Amplituda A, m", ylabel="ω, rad/s")
value("ω(A=0,05)", float(w0*(1 + 3*beta*0.0025/(8*w0**2))), "rad/s")
note("β > 0 — qattiqlashuvchi (AChT o'ngga egiladi); β < 0 — yumshovchi (chapga).")

# --- Chastotani o'lchash: sonli tajriba ---
for amp in (0.01, 0.05, 0.09):
    sol = solve_ivp(lambda t, y: np.array([y[1], -w0**2*y[0] - beta*y[0]**3]),
                    (0, 4), [amp, 0.0], rtol=1e-11, dense_output=True, max_step=0.0005)
    tt = np.linspace(0, 4, 8000)
    X = sol.sol(tt)[0]
    zero_cross = np.where(np.diff(np.sign(X)))[0]
    if len(zero_cross) >= 3:
        T_meas = 2*(tt[zero_cross[2]] - tt[zero_cross[0]])/2
        note(f"A={amp:.3f} m: o'lchangan ω = {2*np.pi/T_meas:.3f} rad/s, "
             f"taqribiy formula: {w0*(1+3*beta*amp**2/(8*w0**2)):.3f} rad/s")

# --- Bifurkatsiya: β ning muvozanat nuqtalariga ta'siri ---
betas = np.linspace(-20000, 5000, 200)
x_eq = [np.sqrt(-w0**2/b) if b < 0 else 0.0 for b in betas]
series("Bifurkatsiya diagrammasi", betas.tolist(), x_eq,
       xlabel="β", ylabel="|x*| (yon muvozanat), m")
note("β = 0 — bifurkatsiya nuqtasi: β < 0 da ikkita qo'shimcha (noturg'un) "
     "muvozanat paydo bo'ladi. Bu — pitchfork bifurkatsiyasi.")
''',
                parameters=[
                    p("w0", "Chiziqli chastota ω₀", 1.0, 100.0, 20.0, 1.0, "rad/s"),
                    p("beta", "Nochiziqlilik β", -30000.0, 30000.0, -8000.0, 500.0, "—"),
                    p("zeta", "Dempfirlash ζ", 0.0, 0.5, 0.05, 0.01, "—"),
                    p("F", "Majburlovchi amplituda", 0.0, 50.0, 0.0, 1.0, "m/s²"),
                    p("x0", "Boshlang'ich siljish", 0.001, 0.25, 0.1, 0.005, "m"),
                ],
                expected_output="3 ta muvozanat: x=0 turg'un, x=±0,224 m noturg'un; ω(0,05) = 19,63 rad/s",
            ),
            visualization=vis(
                "Fazaviy portret va bifurkatsiya diagrammasi",
                "React/SVG",
                "Fazaviy tekislikda traektoriyalar, muvozanat nuqtalari (turg'un — "
                "to'ldirilgan doira, noturg'un — bo'sh doira), separatrisalar. "
                "Yonida bifurkatsiya diagrammasi.",
                "React/SVG: nm-24 dagi fazaviy portret komponentini kengaytiring — "
                "muvozanat nuqtalarini belgilash va turg'unlikni rang bilan "
                "ko'rsatish. Bifurkatsiya diagrammasi esa pq-15/mq-25 dagi "
                "ustuvorlik mavzularida qayta ishlatiladi.",
            ),
            interpretation=(
                "Uchta muvozanat nuqtasidan faqat markaziysi turg'un — demak tizim "
                "kichik bezovtalanishlarda unga qaytadi, lekin amplituda "
                "$0{,}224$ m dan oshsa, u 'qochib ketadi'. Bu — yumshovchi tizimning "
                "xavfi. Bifurkatsiya diagrammasi $\\beta = 0$ da sifat o'zgarishini "
                "ko'rsatadi: bitta muvozanatdan uchtaga o'tish. Aynan shunday "
                "struktura mq-25 dagi Eyler masalasida ham paydo bo'ladi, faqat "
                "u yerda parametr — siquvchi kuch."
            ),
            common_mistakes=[
                "Chiziqlilashtirilgan tahlil natijasini katta ko'chishlarga "
                "ko'chirish — u faqat muvozanat atrofida o'rinli.",
                "$\\text{Re}(\\lambda) = 0$ kritik holida chiziqli tahlildan xulosa "
                "chiqarish — u yetarli emas.",
                "Nochiziqli tizimda superpozitsiya prinsipini qo'llash — u ishlamaydi.",
                "Xususiy chastotani amplitudadan mustaqil deb hisoblash.",
            ],
            quiz=[
                q("Nima uchun nochiziqli tizimda superpozitsiya ishlamaydi?",
                  "Chunki tenglama chiziqli emas: ikki yechim yig'indisi yechim "
                  "bo'lmaydi ($(x_1+x_2)^3 \\neq x_1^3+x_2^3$).", "konseptual"),
                q("Yakobian xususiy qiymatlari $\\lambda = -2 \\pm 5i$. Turg'unlikmi?",
                  "Ha, asimptotik turg'un: haqiqiy qism manfiy. Tebranib so'nadi "
                  "(turg'un fokus).", "hisob"),
                q("Qattiqlashuvchi tizimda ($\\beta > 0$) AChT qaysi tomonga egiladi?",
                  "O'ngga: amplituda oshgani sari chastota ortadi, rezonans cho'qqisi "
                  "yuqori chastotalarga siljiydi.", "talqin"),
                q("Bifurkatsiya nima?",
                  "Parametr o'zgarganda muvozanat nuqtalari soni yoki turg'unligining "
                  "sifat jihatdan o'zgarishi. Misol: siqilgan sterjenning kritik kuchda "
                  "egilishi.", "konseptual"),
                q("Kodda `np.linalg.eigvals(J)` nima uchun `eigvalsh` emas?",
                  "Yakobian matritsasi simmetrik emas (birinchi qatori $[0, 1]$), "
                  "shuning uchun umumiy `eigvals` kerak va xususiy qiymatlar kompleks "
                  "bo'lishi mumkin.", "kod"),
            ],
            bridge_to_next=(
                "Nazariy mexanika kursi yakunlandi: harakat, kuch, energiya, "
                "tebranish va turg'unlik apparati o'zlashtirildi. Lekin butun kurs "
                "davomida jismlar qattiq deb qabul qilindi — ular deformatsiyalanmaydi. "
                "Keyingi fan — Materiallar qarshiligi — aynan shu farazni olib tashlaydi "
                "va konstruksiya ichidagi kuchlanish va deformatsiyalarni o'rganadi."
            ),
            research_extension=(
                "Duffing tenglamasining majburiy tebranishida 'jump' hodisasini "
                "tadqiq qiling: chastotani sekin oshirib, so'ngra sekin kamaytirib, "
                "amplitudaning gisterezis sirtmog'ini quring. Qaysi chastota "
                "oralig'ida uchta yechim mavjud? Ularning qaysilari turg'un? "
                "Natijani garmonik balans usuli bilan olingan analitik egri chiziq "
                "bilan taqqoslang."
            ),
            manim=manim(
                scene="BifurcationScene",
                module="animatsiya/scenes/nm_stability.py",
                title="Turg'unlik va bifurkatsiya",
                summary="Parametr o'zgarganda potensial relyef shakli o'zgaradi: bitta "
                        "chuqurchadan ikkitaga o'tish va sharchaning yangi turg'un "
                        "holatga 'sakrashi'.",
            ),
        ),
    ),
]
