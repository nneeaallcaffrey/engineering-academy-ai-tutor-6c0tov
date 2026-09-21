"""NM / 2-modul: Nyuton dinamikasi, bog'lanishlar va statika (nm-07 … nm-12)."""

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
M = "nm-m2"

TOPICS = [
    Topic(
        id="nm-07",
        subject_id=S,
        module_id=M,
        order=7,
        title="Nyuton qonunlari va moddiy nuqta harakatining matematik modeli",
        description=(
            "Inersial sanoq sistemasi, massa va kuch tushunchalari, harakatning "
            "ikkinchi tartibli differensial tenglamasi sifatida shakllanishi."
        ),
        learning_objective=(
            "Fizik masalani Nyutonning ikkinchi qonuni asosida differensial "
            "tenglamalar tizimiga aylantirish va uning yechimi qanday aniqlanishini "
            "tushuntirish."
        ),
        prerequisites=["nm-02", "nm-03"],
        mathematical_core=(
            "Ikkinchi tartibli ODE, Koshi masalasi, mavjudlik va yagonalik teoremasi, "
            "vektor tenglamani skalyar tizimga ajratish."
        ),
        engineering_application=(
            "Amortizator, yuk ko'tarish mexanizmi, erkin tushish va tortishish "
            "kuchidagi harakat hisobi."
        ),
        computational_component=(
            "Harakat tenglamasini `scipy.integrate.solve_ivp` bilan integrallash va "
            "analitik yechim bilan taqqoslash."
        ),
        visualization_component=(
            "Erkin jism diagrammasi (free-body diagram) va $x(t)$, $v(t)$ grafiklari."
        ),
        research_extension=(
            "Inersial sanoq sistemasi qanchalik 'inersial'? Yer aylanishining "
            "ballistik traektoriyaga ta'sirini nm-06 dagi Koriolis hadi orqali baholang."
        ),
        difficulty="asosiy",
        previous_link=(
            "Kinematika modulida harakatni tavsifladik. Endi uning sababini "
            "kiritamiz: kuch. Nyuton qonuni kinematik kattalik $\\mathbf{a}$ ni "
            "dinamik kattalik $\\mathbf{F}$ bilan bog'laydi."
        ),
        next_topic="nm-08",
        estimated_minutes=90,
        tags=["Nyuton qonunlari", "ODE", "free-body diagram"],
        lesson=Lesson(
            physical_problem=(
                "Liftni ushlab turuvchi trosda qanday kuch bo'ladi? Agar lift tekis "
                "harakatlansa — javob oddiy: yuk og'irligiga teng. Lekin lift "
                "tezlanish bilan yuqoriga ko'tarilsa, tros qo'shimcha yuk oladi. "
                "Qancha? Bu savol konstruksiyaning xavfsizlik zaxirasini belgilaydi va "
                "unga faqat dinamika javob bera oladi."
            ),
            concepts=[
                c("Inersial sanoq sistemasi", "Unda erkin jism tekis va to'g'ri chiziqli "
                  "harakatlanadi. Yer bilan bog'langan sistema ko'p masalada yetarlicha "
                  "inersial deb qabul qilinadi."),
                c("Massa (mass)", "Jismning inersiya o'lchovi — bir xil kuchda qanchalik "
                  "kam tezlanish olishini bildiradi. Skalyar, musbat, harakatga bog'liq emas."),
                c("Kuch (force)", "Jismlar o'zaro ta'sirining o'lchovi. Vektor kattalik, "
                  "SI da nyuton: $1\\text{ N} = 1\\text{ kg}\\cdot\\text{m/s}^2$."),
                c("Erkin jism diagrammasi (free-body diagram)", "Jismni bog'lanishlardan "
                  "ajratib, unga ta'sir etuvchi barcha kuchlarni ko'rsatuvchi sxema. "
                  "Dinamika masalasining birinchi va eng muhim qadami."),
                c("Koshi masalasi", "Differensial tenglama + boshlang'ich shartlar. "
                  "Nyuton tenglamasi uchun $\\mathbf{r}(0)$ va $\\mathbf{v}(0)$ berilishi "
                  "yechimni yagona qiladi."),
            ],
            derivation=[
                d("1-qadam. Ikkinchi qonunni vektor ko'rinishida yozish",
                  r"m\mathbf{a} = \sum_{i}\mathbf{F}_i \quad\Longleftrightarrow\quad "
                  r"m\frac{d^2\mathbf{r}}{dt^2} = \mathbf{F}(t, \mathbf{r}, \mathbf{v})",
                  "Kuch umumiy holda vaqtga, holatga (prujina) va tezlikka (qarshilik) "
                  "bog'liq bo'lishi mumkin. Shuning uchun bu — nochiziqli bo'lishi mumkin "
                  "bo'lgan ikkinchi tartibli ODE."),
                d("2-qadam. Skalyar tenglamalar tizimiga ajratish",
                  r"m\ddot{x} = F_x,\qquad m\ddot{y} = F_y,\qquad m\ddot{z} = F_z",
                  "Vektor tenglama fazoda 3 ta skalyar tenglamaga ajraladi. Ular "
                  "$\\mathbf{F}$ orqali o'zaro bog'langan bo'lishi mumkin."),
                d("3-qadam. Birinchi tartibli tizimga keltirish",
                  r"\frac{d}{dt}\begin{Bmatrix}\mathbf{r}\\ \mathbf{v}\end{Bmatrix} = "
                  r"\begin{Bmatrix}\mathbf{v}\\ \mathbf{F}/m\end{Bmatrix}",
                  "Sonli integrallash uchun standart shakl. 3 o'lchovli masala 6 ta "
                  "birinchi tartibli tenglamaga aylanadi — `solve_ivp` aynan shu "
                  "ko'rinishni talab qiladi (su-09)."),
                d("4-qadam. Lift masalasi uchun qo'llash",
                  r"m\ddot{y} = T - mg \;\Rightarrow\; T = m(g + \ddot{y}) = m(g+a)",
                  "Erkin jism diagrammasi: yuqoriga tros tarangligi $T$, pastga "
                  "og'irlik $mg$. Ikkinchi qonunni y o'qiga proyeksiyalaymiz."),
                d("5-qadam. Dinamiklik koeffitsientini ajratish",
                  r"T = mg\left(1 + \frac{a}{g}\right) = mg\,k_d,\qquad k_d = 1 + \frac{a}{g}",
                  "$k_d$ — dinamiklik koeffitsienti. Statik yuk $mg$ ga ko'paytiriladigan "
                  "bu koeffitsient mq-27 da zarbiy yuklanish uchun umumlashtiriladi."),
            ],
            formula_meaning=(
                "$m\\mathbf{a} = \\sum\\mathbf{F}$ tenglamasi ikki yo'nalishda o'qiladi. "
                "To'g'ri masala: kuchlar ma'lum → harakatni topamiz (integrallash). "
                "Teskari masala: harakat ma'lum → kuchni topamiz (differensiallash). "
                "Muhandislikda ikkinchisi ko'proq uchraydi: konstruksiya qanday "
                "harakatlanishi kerakligini biz belgilaymiz, u holda qanday kuch "
                "kerakligini hisoblaymiz. $k_d = 1 + a/g$ esa loyihalashning tayanch soni."
            ),
            equations=[
                eq(r"m\mathbf{a} = \sum \mathbf{F}_i", "Nyutonning ikkinchi qonuni.",
                   "Dinamikaning asosiy tenglamasi"),
                eq(r"\mathbf{F}_{12} = -\mathbf{F}_{21}", "Uchinchi qonun — ta'sir va aks ta'sir.",
                   "Uchinchi qonun"),
                eq(r"k_d = 1 + \frac{a}{g}", "Tezlanuvchi ko'tarishda dinamiklik koeffitsienti.",
                   "Dinamiklik koeffitsienti"),
            ],
            conditions=(
                "Koshi masalasi: $\\mathbf{r}(t_0) = \\mathbf{r}_0$, $\\mathbf{v}(t_0) = \\mathbf{v}_0$. "
                "Pikar teoremasiga ko'ra $\\mathbf{F}$ Lipshits shartini qanoatlantirsa, "
                "yechim mavjud va yagona. Muhandislik masalalarida bu deyarli har doim "
                "bajariladi; istisno — ishqalanish kuchi ishorasi sakrab o'zgaradigan "
                "nuqtalar (nm-12)."
            ),
            worked_example=WorkedExample(
                statement=(
                    "Lift kabinasi yuk bilan birga $m = 1200$ kg. U tinch holatdan "
                    "3 s davomida tekis tezlanib, 2,5 m/s tezlikka chiqadi, so'ng tekis "
                    "harakatlanadi, oxirida 2 s da to'xtaydi. Trosdagi kuchni har uch "
                    "bosqichda toping. Tros ruxsat etilgan kuchi 20 kN bo'lsa, zaxira "
                    "yetarlimi?"
                ),
                given=[r"m = 1200\ \text{kg}", r"v_{max} = 2{,}5\ \text{m/s}",
                       r"t_1 = 3\ \text{s},\; t_3 = 2\ \text{s}", r"[T] = 20\ \text{kN}"],
                steps=[
                    st(r"a_1 = \frac{2{,}5 - 0}{3} = 0{,}833\ \text{m/s}^2",
                       "Ko'tarilish bosqichidagi tezlanish (yuqoriga)."),
                    st(r"T_1 = m(g+a_1) = 1200(9{,}81+0{,}833) = 1200\cdot 10{,}643 = 12\,772\ \text{N}",
                       "Tezlanish bosqichi: tros og'irlikdan ko'proq kuch beradi."),
                    st(r"T_2 = mg = 1200\cdot 9{,}81 = 11\,772\ \text{N}",
                       "Tekis harakat: $a=0$, tros faqat og'irlikni ushlaydi."),
                    st(r"a_3 = \frac{0-2{,}5}{2} = -1{,}25\ \text{m/s}^2 \Rightarrow "
                       r"T_3 = 1200(9{,}81-1{,}25) = 10\,272\ \text{N}",
                       "To'xtash bosqichi: tezlanish pastga, tros yuki kamayadi."),
                    st(r"k_d = \frac{T_1}{mg} = \frac{12\,772}{11\,772} = 1{,}085",
                       "Dinamiklik koeffitsienti 1,085 — statik hisobdan 8,5 % ortiq."),
                    st(r"n = \frac{[T]}{T_{max}} = \frac{20\,000}{12\,772} = 1{,}57",
                       "Zaxira koeffitsienti."),
                ],
                answer=(
                    "$T_1 = 12{,}77$ kN, $T_2 = 11{,}77$ kN, $T_3 = 10{,}27$ kN; "
                    "$k_d = 1{,}085$; zaxira $n = 1{,}57$."
                ),
                engineering_note=(
                    "Liftlar uchun me'yoriy zaxira odatda 8–12 ga teng (favqulodda "
                    "to'xtash va tros yeyilishi hisobga olinadi), shuning uchun 1,57 "
                    "yetarli emas. Bu — mq-05 dagi ruxsat etilgan kuchlanish va zaxira "
                    "koeffitsienti mavzusiga to'g'ridan-to'g'ri o'tish nuqtasi."
                ),
            ),
            computation=Computation(
                caption=(
                    "Lift harakati: tezlanish profilini o'zgartirib, trosdagi kuch va "
                    "dinamiklik koeffitsientini kuzating."
                ),
                code='''"""Nyuton tenglamasi: lift trosidagi kuch va sonli integrallash."""
import numpy as np
from scipy.integrate import solve_ivp
from labkit import PARAMS, note, series, table, value

m = float(PARAMS.get("m", 1200.0))      # kg
a1 = float(PARAMS.get("a1", 0.833))     # tezlanish bosqichi, m/s^2
t1 = float(PARAMS.get("t1", 3.0))       # tezlanish davomiyligi, s
t2 = float(PARAMS.get("t2", 5.0))       # tekis harakat, s
g = 9.81

v_max = a1*t1
a3 = -v_max/2.0                          # 2 s da to'xtash
t3 = 2.0

def accel(t):
    """Tezlanish profili (bosqichli)."""
    if t < t1:
        return a1
    if t < t1 + t2:
        return 0.0
    if t < t1 + t2 + t3:
        return a3
    return 0.0

def rhs(t, y):
    """y = [x, v] -> dy/dt = [v, a]"""
    return [y[1], accel(t)]

t_end = t1 + t2 + t3
sol = solve_ivp(rhs, (0, t_end), [0.0, 0.0], max_step=0.01, dense_output=True)
tt = np.linspace(0, t_end, 600)
xx, vv = sol.sol(tt)
aa = np.array([accel(t) for t in tt])
T = m*(g + aa)                            # trosdagi kuch

series("Balandlik x(t)", tt.tolist(), xx.tolist(), xlabel="t, s", ylabel="x, m")
series("Tezlik v(t)", tt.tolist(), vv.tolist(), xlabel="t, s", ylabel="v, m/s")
series("Tros kuchi T(t)", tt.tolist(), (T/1000).tolist(), xlabel="t, s", ylabel="T, kN")

value("T_max", float(np.max(T)/1000), "kN")
value("T_statik", m*g/1000, "kN")
value("Dinamiklik k_d", float(np.max(T)/(m*g)), "—")
value("Ko'tarilish balandligi", float(xx[-1]), "m")
note(f"Erkin tushishda (a = -g) tros kuchi nolga tushadi — vaznsizlik holati.")

table("Bosqichlar bo'yicha",
      ["Bosqich", "a, m/s²", "T, kN"],
      [["Tezlanish", a1, float(m*(g+a1)/1000)],
       ["Tekis", 0.0, float(m*g/1000)],
       ["To'xtash", a3, float(m*(g+a3)/1000)]])
''',
                parameters=[
                    p("m", "Lift massasi m", 300.0, 3000.0, 1200.0, 50.0, "kg"),
                    p("a1", "Tezlanish a₁", 0.1, 4.0, 0.833, 0.05, "m/s²"),
                    p("t1", "Tezlanish vaqti t₁", 0.5, 10.0, 3.0, 0.5, "s"),
                    p("t2", "Tekis harakat t₂", 0.0, 20.0, 5.0, 0.5, "s"),
                ],
                expected_output="T_max ≈ 12,77 kN, T_statik = 11,77 kN, k_d ≈ 1,085",
            ),
            visualization=vis(
                "Erkin jism diagrammasi + vaqt grafiklari",
                "React/SVG",
                "Lift kabinasi to'rtburchak sifatida, yuqoriga $T$ strelkasi, pastga "
                "$mg$ strelkasi, yonida $a$ yo'nalishi; ostida $x(t)$, $v(t)$, $T(t)$ grafiklari.",
                "React/SVG: free-body diagram — eng sodda, lekin eng muhim chizma. "
                "Kuch strelkalari uzunligi kuch moduliga proporsional bo'lsin, shunda "
                "$T > mg$ ekani ko'rinib turadi. Grafiklar uchun umumiy `LinePlot` komponenti.",
            ),
            interpretation=(
                "$T(t)$ grafigi pog'onasimon: tezlanishda yuqori, tekis harakatda "
                "statik qiymatda, to'xtashda esa statikdan past. Eng muhim xulosa — "
                "harakat tezligi emas, tezlanishi konstruksiyaga yuk beradi. Lift "
                "2,5 m/s bilan yuqoriga ketayotganida ham, 10 m/s bilan ketayotganida "
                "ham tros bir xil kuch oladi, agar tezlanish nol bo'lsa."
            ),
            common_mistakes=[
                "Erkin jism diagrammasini chizmasdan tenglama yozishga urinish — "
                "kuchlarning yarmi unutiladi.",
                "Tezlanish yo'nalishini kuch yo'nalishi bilan chalkashtirish. Lift "
                "yuqoriga ketib sekinlashsa, tezlanish pastga yo'nalgan.",
                "$T = mg$ ni har doim to'g'ri deb hisoblash — bu faqat $a = 0$ da o'rinli.",
                "Inersiya kuchini erkin jism diagrammasiga qo'shib yuborish. Nyuton "
                "tenglamasida faqat real kuchlar bo'ladi (inersiya kuchi — nm-21 dagi "
                "D'Alembert usulida kiritiladi).",
                "Massani og'irlik bilan almashtirish: $m$ [kg] va $G = mg$ [N] — "
                "har xil kattaliklar.",
            ],
            quiz=[
                q("Lift yuqoriga tekis ko'tarilmoqda. Trosdagi kuch og'irlikdan katta, "
                  "kichik yoki tengmi?",
                  "Teng: $a = 0$, demak $T = mg$. Tezlik emas, tezlanish ahamiyatli.",
                  "konseptual"),
                q("Lift pastga tezlanish bilan tushmoqda ($a = 2$ m/s², pastga). "
                  "$m = 1000$ kg uchun $T$ ni toping.",
                  "$T = m(g-a) = 1000(9{,}81-2) = 7810$ N. Tros yuki kamayadi.", "hisob"),
                q("Nima uchun Nyuton tenglamasi faqat inersial sanoq sistemasida o'rinli?",
                  "Noinersial sistemada qo'shimcha (inersiya) kuchlari paydo bo'ladi — "
                  "markazdan qochma va Koriolis; ularsiz $m\\mathbf{a}=\\sum\\mathbf{F}$ buziladi.",
                  "konseptual"),
                q("Uchinchi qonun bo'yicha ot aravani tortsa, arava ham otni teng kuch "
                  "bilan tortadi. Unda nega ular harakatlanadi?",
                  "Chunki bu kuchlar turli jismlarga qo'yilgan. Otning harakatini "
                  "aniqlash uchun faqat otga qo'yilgan kuchlar (arava tortishi va "
                  "yerning ishqalanish reaksiyasi) jamlanadi.", "talqin"),
                q("Kodda `solve_ivp` uchun tenglama nima uchun birinchi tartibga keltirildi?",
                  "Chunki sonli integratorlar $y' = f(t,y)$ shaklini talab qiladi. "
                  "$y = [x, v]$ almashtirish ikkinchi tartibli tenglamani ikkita birinchi "
                  "tartibliga aylantiradi.", "kod"),
                q("Erkin tushishda ($a = -g$) tros kuchi qanday bo'ladi va bu holat nima "
                  "deb ataladi?",
                  "$T = m(g-g) = 0$ — vaznsizlik. Kabinadagi odam og'irligini his qilmaydi.",
                  "talqin"),
            ],
            bridge_to_next=(
                "Biz kuchni ma'lum deb oldik. Ammo real masalalarda kuch o'zgaruvchan "
                "bo'ladi va tenglamani integrallash kerak. Keyingi mavzuda dinamikaning "
                "to'g'ri va teskari masalalarini, integrallash texnikasini ko'ramiz."
            ),
            research_extension=(
                "Lift trosining o'zini elastik deb hisoblang (prujina, bikrligi $k$) va "
                "tizimni ikki erkinlik darajali qilib modellashtiring. Tezlanish "
                "bosqichida trosda qanday tebranish paydo bo'ladi? Dinamiklik "
                "koeffitsienti statik hisobdan qanchalik oshadi? Bu masala nm-25 va "
                "mq-27 ga to'g'ridan-to'g'ri olib boradi."
            ),
            manim=manim(
                scene="FreeBodyScene",
                module="animatsiya/scenes/nm_dynamics.py",
                title="Erkin jism diagrammasi va Nyuton tenglamasi",
                summary="Lift kabinasi bog'lanishlardan ajratiladi, kuchlar strelkalari "
                        "chiziladi va tezlanish o'zgarganda T strelkasi uzunligi o'zgaradi.",
            ),
        ),
    ),
    Topic(
        id="nm-08",
        subject_id=S,
        module_id=M,
        order=8,
        title="Dinamikaning to'g'ri va teskari masalalari: harakat tenglamasini integrallash",
        description=(
            "Kuch turiga qarab integrallash usullari: $F(t)$, $F(v)$, $F(x)$ hollari "
            "va o'zgaruvchilarni ajratish texnikasi."
        ),
        learning_objective=(
            "Kuchning qanday argumentga bog'liqligiga qarab mos integrallash "
            "strategiyasini tanlash va analitik yechimni olish."
        ),
        prerequisites=["nm-07"],
        mathematical_core=(
            "O'zgaruvchilarni ajratish, $a = v\\,dv/dx$ almashtirishi, aniqmas va "
            "aniq integral, integrallash doimiylarini boshlang'ich shartlardan topish."
        ),
        engineering_application=(
            "Reaktiv harakat, o'zgaruvchan tortishish kuchi, prujinali mexanizmlar, "
            "amortizator hisobi."
        ),
        computational_component=(
            "SymPy bilan analitik integrallash va `solve_ivp` bilan sonli yechimni "
            "taqqoslash; xatolikni baholash."
        ),
        visualization_component=(
            "Har bir kuch turi uchun $x(t)$ va $v(x)$ grafiklari; fazaviy tekislikda "
            "traektoriya."
        ),
        research_extension=(
            "Analitik yechim mavjud bo'lmagan holda (masalan, $F = -k x^3 - c v|v|$) "
            "sonli yechim yagona yo'l. Xatolik qanday nazorat qilinadi?"
        ),
        difficulty="asosiy",
        previous_link=(
            "nm-07 da tenglamani tuzdik. Endi uni yechishni o'rganamiz — va kuchning "
            "argumentiga qarab uch xil texnika kerakligini ko'ramiz."
        ),
        next_topic="nm-09",
        estimated_minutes=90,
        tags=["integrallash", "ODE", "o'zgaruvchilarni ajratish"],
        lesson=Lesson(
            physical_problem=(
                "Pnevmatik amortizator porshenini bosganda qarshilik kuchi siljishga "
                "bog'liq bo'ladi, gidravlikda esa — tezlikka. Bir xil boshlang'ich "
                "energiyada ular butunlay boshqacha to'xtash masofasini beradi. "
                "Loyihachi qaysi birini tanlashi kerak? Buning uchun har bir holda "
                "harakat tenglamasini yechish lozim — va ular turli matematik "
                "texnikani talab qiladi."
            ),
            concepts=[
                c("To'g'ri masala", "Kuchlar ma'lum → harakat qonuni topiladi. "
                  "Integrallash talab qilinadi, integrallash doimiylari boshlang'ich "
                  "shartlardan aniqlanadi."),
                c("Teskari masala", "Harakat ma'lum → kuch topiladi. Faqat "
                  "differensiallash kerak, yechim yagona va oddiy."),
                c("$F(t)$ holi", "Vaqtga bog'liq kuch. Ikki marta to'g'ridan-to'g'ri "
                  "vaqt bo'yicha integrallanadi."),
                c("$F(v)$ holi", "Tezlikka bog'liq kuch (qarshilik). "
                  "$m\\,dv/dt = F(v)$ da o'zgaruvchilar ajratiladi."),
                c("$F(x)$ holi", "Koordinataga bog'liq kuch (prujina, tortishish). "
                  "$a = v\\,dv/dx$ almashtirishi qo'llaniladi — bu energiya integraliga olib keladi."),
            ],
            derivation=[
                d("1-qadam. $F = F(t)$ holi",
                  r"m\frac{dv}{dt} = F(t) \Rightarrow v(t) = v_0 + \frac{1}{m}\int_0^t F(\tau)d\tau"
                  r"\Rightarrow x(t) = x_0 + \int_0^t v(\tau)d\tau",
                  "Eng sodda hol: ketma-ket ikki marta integrallash. Har bir integrallash "
                  "bitta doimiy beradi, ularni $v_0$ va $x_0$ aniqlaydi."),
                d("2-qadam. $F = F(v)$ holi — o'zgaruvchilarni ajratish",
                  r"m\frac{dv}{dt} = F(v) \Rightarrow \frac{m\,dv}{F(v)} = dt \Rightarrow "
                  r"t = m\int_{v_0}^{v}\frac{dv'}{F(v')}",
                  "Natijada $t(v)$ olinadi; uni teskari aylantirib $v(t)$ topiladi. "
                  "Agar teskari aylantirish qiyin bo'lsa, $v(x)$ ni topish qulayroq."),
                d("3-qadam. $F = F(v)$ holida $v(x)$ ni topish",
                  r"m\,v\frac{dv}{dx} = F(v) \Rightarrow \frac{m\,v\,dv}{F(v)} = dx",
                  "$\\frac{dv}{dt} = \\frac{dv}{dx}\\frac{dx}{dt} = v\\frac{dv}{dx}$ "
                  "almashtirishi — dinamikaning eng foydali hiylalaridan biri."),
                d("4-qadam. $F = F(x)$ holi — energiya integrali",
                  r"m\,v\frac{dv}{dx} = F(x) \Rightarrow \frac{m v^2}{2}\Big|_{v_0}^{v} = "
                  r"\int_{x_0}^{x}F(x')dx'",
                  "Chap tomon — kinetik energiya o'zgarishi, o'ng tomon — ish. Demak "
                  "$F(x)$ holida energiya teoremasi avtomatik kelib chiqadi (nm-14)."),
                d("5-qadam. Chiziqli qarshilik uchun aniq yechim",
                  r"m\dot v = -cv \Rightarrow v(t) = v_0 e^{-ct/m},\qquad "
                  r"x(t) = x_0 + \frac{mv_0}{c}\left(1-e^{-ct/m}\right)",
                  "Muhim xulosa: chiziqli qarshilikda jism hech qachon to'liq to'xtamaydi "
                  "(eksponenta nolga faqat asimptotik intiladi), lekin chekli masofa "
                  "$x_\\infty = mv_0/c$ bosib o'tadi."),
            ],
            formula_meaning=(
                "Uchta hol uchta matematik strategiyani beradi, lekin ularning fizik "
                "ma'nosi ham farq qiladi. $F(t)$ — tashqi majburlash (dvigatel, zarba). "
                "$F(v)$ — dissipatsiya: energiya yo'qoladi, harakat so'nadi. $F(x)$ — "
                "potensial: energiya saqlanadi va ikki tomonga o'tadi. Aynan shu uchinchi "
                "hol tebranishlarga olib keladi, ikkinchisi esa ularni so'ndiradi."
            ),
            equations=[
                eq(r"v\frac{dv}{dx} = \frac{F}{m}", "Vaqtni yo'qotuvchi almashtirish.",
                   "Energiya shakli"),
                eq(r"v(t) = v_0 e^{-ct/m}", "Chiziqli qarshilikdagi tezlik.", "Eksponensial so'nish"),
                eq(r"x_\infty = \frac{m v_0}{c}", "Chiziqli qarshilikda to'la bosib o'tilgan yo'l.",
                   "Chekli masofa"),
            ],
            conditions=(
                "Har bir integrallash bitta boshlang'ich shartni talab qiladi. "
                "Ikkinchi tartibli tenglama uchun $x(0)$ va $v(0)$. Agar masala "
                "'qachon to'xtaydi?' deb qo'yilsa — bu chegaraviy shart ($v = 0$) va u "
                "yechimni topgandan keyin qo'llaniladi. Chiziqli qarshilikda bunday "
                "shart chekli vaqtda bajarilmaydi — bu modelning cheklovi."
            ),
            worked_example=WorkedExample(
                statement=(
                    "Massasi $m = 25$ kg bo'lgan yuk $v_0 = 6$ m/s tezlik bilan "
                    "gorizontal yo'lda sirpanadi. Unga qarshilik kuchi ikki modelda "
                    "berilgan: (a) chiziqli $F = -cv$, $c = 15$ N·s/m; (b) kvadratik "
                    "$F = -bv^2$, $b = 2{,}5$ N·s²/m². Har ikkala holda tezlik 1 m/s ga "
                    "tushguncha bosib o'tilgan yo'lni toping."
                ),
                given=[r"m = 25\ \text{kg},\; v_0 = 6\ \text{m/s},\; v_1 = 1\ \text{m/s}",
                       r"\text{(a) } c = 15\ \text{N·s/m}", r"\text{(b) } b = 2{,}5\ \text{N·s}^2\text{/m}^2"],
                steps=[
                    st(r"\text{(a)}\; m v\frac{dv}{dx} = -cv \Rightarrow m\,dv = -c\,dx",
                       "Chiziqli holda $v$ qisqaradi — tenglama juda soddalashadi."),
                    st(r"x = \frac{m}{c}(v_0 - v_1) = \frac{25}{15}(6-1) = 1{,}667\cdot 5 = 8{,}33\ \text{m}",
                       "Chiziqli qarshilikda yo'l tezliklar farqiga proporsional."),
                    st(r"\text{(b)}\; m v\frac{dv}{dx} = -bv^2 \Rightarrow \frac{m\,dv}{v} = -b\,dx",
                       "Kvadratik holda bitta $v$ qisqaradi, logarifm paydo bo'ladi."),
                    st(r"x = \frac{m}{b}\ln\frac{v_0}{v_1} = \frac{25}{2{,}5}\ln 6 = 10\cdot 1{,}792 = 17{,}9\ \text{m}",
                       "Kvadratik qarshilikda yo'l tezliklar nisbatining logarifmiga proporsional."),
                    st(r"\text{(a) uchun } t = \frac{m}{c}\ln\frac{v_0}{v_1} = 1{,}667\cdot 1{,}792 = 2{,}99\ \text{s}",
                       "Chiziqli holda vaqt logarifmik."),
                    st(r"\text{(b) uchun } t = \frac{m}{b}\left(\frac{1}{v_1}-\frac{1}{v_0}\right) = 10(1-0{,}167) = 8{,}33\ \text{s}",
                       "Kvadratik holda vaqt teskari tezliklar farqiga proporsional."),
                ],
                answer=(
                    "(a) $x = 8{,}33$ m, $t = 2{,}99$ s; (b) $x = 17{,}9$ m, $t = 8{,}33$ s."
                ),
                engineering_note=(
                    "Kvadratik qarshilik yuqori tezlikda kuchliroq, past tezlikda esa "
                    "zaifroq. Shuning uchun u boshida tez sekinlatadi, keyin esa 'quyruq' "
                    "cho'ziladi. Amortizator loyihalashda aynan shu xossa muhim: "
                    "gidravlik amortizatorlar odatda $F \\propto v^{1{,}5...2}$ tavsifga ega."
                ),
            ),
            computation=Computation(
                caption=(
                    "Qarshilik modelini va koeffitsientini o'zgartirib, to'xtash "
                    "masofasi hamda tezlik profilini taqqoslang."
                ),
                code='''"""Uch xil kuch turi uchun harakat tenglamasini integrallash."""
import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp
from labkit import PARAMS, note, series, table, value

m = float(PARAMS.get("m", 25.0))     # kg
v0 = float(PARAMS.get("v0", 6.0))    # m/s
cc = float(PARAMS.get("c", 15.0))    # chiziqli qarshilik, N*s/m
bb = float(PARAMS.get("b", 2.5))     # kvadratik qarshilik, N*s^2/m^2
v1 = 1.0

# --- Analitik yechimlar (SymPy bilan tekshiriladi) ---
t_sym, v_sym = sp.symbols("t v", positive=True)
x_lin = m/cc*(v0 - v1)
x_quad = m/bb*sp.log(v0/v1)
value("x chiziqli (analitik)", float(x_lin), "m")
value("x kvadratik (analitik)", float(x_quad), "m")
value("t chiziqli", float(m/cc*np.log(v0/v1)), "s")
value("t kvadratik", float(m/bb*(1/v1 - 1/v0)), "s")

# --- Sonli yechim: ikkala model uchun ---
def make_rhs(kind):
    def rhs(t, y):
        x, v = y
        F = -cc*v if kind == "lin" else -bb*v*abs(v)
        return [v, F/m]
    return rhs

def stop_event(t, y):
    return y[1] - v1
stop_event.terminal = True
stop_event.direction = -1

res = {}
for kind in ("lin", "quad"):
    sol = solve_ivp(make_rhs(kind), (0, 60), [0.0, v0], events=stop_event,
                    rtol=1e-9, atol=1e-11, dense_output=True)
    res[kind] = sol
    tt = np.linspace(0, sol.t[-1], 300)
    xx, vv = sol.sol(tt)
    label = "Chiziqli F=-cv" if kind == "lin" else "Kvadratik F=-bv²"
    series(f"Tezlik: {label}", tt.tolist(), vv.tolist(), xlabel="t, s", ylabel="v, m/s")
    series(f"Yo'l: {label}", tt.tolist(), xx.tolist(), xlabel="t, s", ylabel="x, m")

err_lin = abs(res["lin"].y[0][-1] - float(x_lin))
err_quad = abs(res["quad"].y[0][-1] - float(x_quad))
note(f"Sonli va analitik farq: chiziqli {err_lin:.2e} m, kvadratik {err_quad:.2e} m")

table("Modellarni taqqoslash",
      ["Model", "x, m", "t, s"],
      [["Chiziqli", float(res["lin"].y[0][-1]), float(res["lin"].t[-1])],
       ["Kvadratik", float(res["quad"].y[0][-1]), float(res["quad"].t[-1])]])
''',
                parameters=[
                    p("m", "Massa m", 1.0, 200.0, 25.0, 1.0, "kg"),
                    p("v0", "Boshlang'ich tezlik v₀", 0.5, 30.0, 6.0, 0.5, "m/s"),
                    p("c", "Chiziqli koeffitsient c", 1.0, 100.0, 15.0, 1.0, "N·s/m"),
                    p("b", "Kvadratik koeffitsient b", 0.1, 20.0, 2.5, 0.1, "N·s²/m²"),
                ],
                expected_output="x_chiziqli = 8,33 m; x_kvadratik = 17,92 m",
            ),
            visualization=vis(
                "Ikki qarshilik modelini taqqoslash",
                "React/SVG + Matplotlib",
                "Bir grafikda ikkala modelning $v(t)$ egri chiziqlari; ikkinchi grafikda "
                "$v(x)$ — fazaviy tekislikdagi yo'l.",
                "React/SVG: ikkala chiziqni bir `LinePlot` da turli rangda ko'rsating — "
                "taqqoslash uchun eng samarali usul. Matplotlib esa hisobotlarga mos "
                "statik grafik beradi.",
            ),
            interpretation=(
                "Grafiklarda kvadratik model boshida tikroq tushadi, keyin 'quyruq' "
                "hosil qiladi; chiziqli model esa eksponensial, ya'ni bir tekis. "
                "Natijada kvadratik model 2 barobar uzoq yo'l beradi — bu loyihalash "
                "uchun hal qiluvchi farq. Sonli va analitik yechim farqi $10^{-9}$ "
                "tartibida bo'lishi kod va integrallash to'g'riligini tasdiqlaydi."
            ),
            common_mistakes=[
                "$a = dv/dt$ va $a = v\\,dv/dx$ ni chalkashtirish. Birinchisi vaqt, "
                "ikkinchisi koordinata bo'yicha integrallash uchun.",
                "$F(v)$ holda to'g'ridan-to'g'ri $\\int F\\,dt$ yozish — $F$ noma'lum "
                "$v(t)$ orqali vaqtga bog'liq, bu integral hisoblanmaydi.",
                "Kvadratik qarshilikda $v^2$ o'rniga $v|v|$ yozmaslik — teskari "
                "yo'nalishda ishora noto'g'ri chiqadi.",
                "Boshlang'ich shartlarni integrallashdan keyin emas, oldin qo'yish.",
                "Chiziqli qarshilikda 'jism $t_1$ vaqtda to'xtaydi' deb javob berish — "
                "u asimptotik to'xtaydi, aniq to'xtash vaqti yo'q.",
            ],
            quiz=[
                q("Qaysi holda $v\\,dv/dx$ almashtirishi eng foydali?",
                  "Kuch koordinataga yoki tezlikka bog'liq bo'lganda, ya'ni vaqtni "
                  "bevosita yo'qotib, $v(x)$ bog'lanishini olish kerak bo'lganda.",
                  "konseptual"),
                q("$F = F(x)$ holida integrallash qaysi fizik teoremaga olib keladi?",
                  "Kinetik energiya haqidagi teoremaga: $\\Delta(mv^2/2) = \\int F\\,dx = A$.",
                  "konseptual"),
                q("$m = 10$ kg, $F = -20v$ N, $v_0 = 5$ m/s. To'la bosib o'tiladigan "
                  "yo'lni toping.",
                  "$x_\\infty = mv_0/c = 10\\cdot 5/20 = 2{,}5$ m.", "hisob"),
                q("Kvadratik qarshilikda jism chekli vaqtda to'xtaydimi?",
                  "Yo'q, $t = (m/b)(1/v - 1/v_0)$ — $v\\to 0$ da $t\\to\\infty$. Lekin "
                  "bosib o'tiladigan yo'l ham cheksiz ($\\ln$), chiziqli modeldan farqli.",
                  "talqin"),
                q("Kodda `stop_event.terminal = True` nima qiladi?",
                  "Integrallashni hodisa (tezlik $v_1$ ga tushishi) sodir bo'lganda "
                  "to'xtatadi. Bu chegaraviy shartni sonli usulda amalga oshirish yo'li.",
                  "kod"),
                q("Nima uchun `rtol=1e-9` qo'yilgan?",
                  "Analitik yechim bilan taqqoslash uchun sonli xatolik analitik farqdan "
                  "ancha kichik bo'lishi kerak — aks holda farq usul xatoligimi yoki model "
                  "farqimi, ajratib bo'lmaydi.", "kod"),
            ],
            bridge_to_next=(
                "Qarshilik kuchi bilan tanishdik, lekin uni faqat matematik model "
                "sifatida oldik. Keyingi mavzuda real muhit qarshiligini — havo va "
                "suyuqlik qarshiligini fizik asosda ko'rib chiqamiz."
            ),
            research_extension=(
                "Aralash model $F = -cv - bv|v|$ uchun analitik yechim mavjudmi? "
                "SymPy bilan integrallashga urinib ko'ring; muvaffaqiyatsiz bo'lsa, "
                "sonli yechimni turli $c/b$ nisbatlarida tahlil qilib, qaysi rejimda "
                "qaysi had ustunligini aniqlang (o'lchamsiz son tuzing)."
            ),
        ),
    ),
    Topic(
        id="nm-09",
        subject_id=S,
        module_id=M,
        order=9,
        title="Muhit qarshiligi va o'zgaruvchan kuchlar ta'siridagi harakat",
        description=(
            "Havo va suyuqlik qarshiligi modellari, chegaraviy tezlik, ballistik "
            "traektoriyaning qarshilik bilan buzilishi."
        ),
        learning_objective=(
            "Qarshilik kuchi modelini Reynolds soniga qarab tanlash va chegaraviy "
            "tezlikni hisoblash."
        ),
        prerequisites=["nm-08"],
        mathematical_core=(
            "Nochiziqli ODE, chegaraviy (asimptotik) yechim, o'lchamsiz parametrlar, "
            "sonli integrallash."
        ),
        engineering_application=(
            "Parashyut hisobi, cho'kish tezligi, ballistika, aerodinamik yuklanish."
        ),
        computational_component=(
            "Qarshilikli ballistik traektoriyani `solve_ivp` bilan hisoblash va "
            "vakuumdagi parabola bilan taqqoslash."
        ),
        visualization_component=(
            "Traektoriyalar oilasi: qarshiliksiz parabola va turli $C_d$ dagi "
            "haqiqiy traektoriyalar."
        ),
        research_extension=(
            "Optimal otish burchagi qarshilik hisobga olinganda 45° dan qanchalik "
            "farq qiladi? Sonli optimallashtirish bilan toping."
        ),
        difficulty="asosiy",
        previous_link=(
            "nm-08 da $F(v)$ modellarini matematik jihatdan yechdik. Endi bu "
            "modellarning fizik asosini va koeffitsientlarning qayerdan olinishini "
            "ko'ramiz."
        ),
        next_topic="nm-10",
        estimated_minutes=90,
        tags=["qarshilik", "ballistika", "chegaraviy tezlik"],
        lesson=Lesson(
            physical_problem=(
                "Parashyutchi samolyotdan sakraydi. Agar qarshilik bo'lmaganida, u "
                "yerga 300 m/s dan ortiq tezlikda urilardi. Aslida esa tezligi "
                "taxminan 55 m/s da barqarorlashadi, parashyut ochilgach — 5 m/s ga "
                "tushadi. Nima uchun tezlik cheklanadi va parashyut yuzasini qanday "
                "hisoblash kerak?"
            ),
            concepts=[
                c("Qarshilik kuchi (drag)", "$F_d = \\tfrac{1}{2}\\rho C_d A v^2$ — "
                  "yuqori Reynolds sonlarida; $\\rho$ — muhit zichligi, $A$ — "
                  "midel yuzasi, $C_d$ — qarshilik koeffitsienti."),
                c("Stoks qarshiligi", "$F_d = 6\\pi\\mu R v$ — kichik Reynolds sonida "
                  "(mayda zarralar, yopishqoq suyuqlik). Tezlikka chiziqli bog'liq."),
                c("Reynolds soni (Reynolds number)", "$Re = \\rho v L/\\mu$ — inersiya "
                  "va yopishqoqlik kuchlari nisbati. Model tanlash mezoni "
                  "(tmm-29 da chuqur o'rganiladi)."),
                c("Chegaraviy tezlik (terminal velocity)", "Qarshilik og'irlikni "
                  "muvozanatlaganda o'rnatiladigan o'zgarmas tezlik: $v_t = \\sqrt{2mg/(\\rho C_d A)}$."),
                c("Ballistik koeffitsient", "$\\beta = m/(C_d A)$ — jismning qarshilikka "
                  "'qarshi turish' qobiliyati. Katta $\\beta$ — kam og'ish."),
            ],
            derivation=[
                d("1-qadam. Vertikal tushish tenglamasi",
                  r"m\frac{dv}{dt} = mg - \tfrac{1}{2}\rho C_d A v^2 = mg - k v^2,\qquad k = \tfrac{1}{2}\rho C_d A",
                  "Pastga musbat yo'nalish. Qarshilik har doim harakatga qarshi."),
                d("2-qadam. Chegaraviy tezlikni topish",
                  r"\frac{dv}{dt} = 0 \Rightarrow mg = kv_t^2 \Rightarrow "
                  r"\boxed{\,v_t = \sqrt{\frac{2mg}{\rho C_d A}}\,}",
                  "Muvozanat holati — bu tenglamaning turg'un yechimi. Har qanday "
                  "boshlang'ich tezlikdan harakat unga intiladi."),
                d("3-qadam. Tenglamani o'lchamsizlashtirish",
                  r"\frac{dv}{dt} = g\left(1 - \frac{v^2}{v_t^2}\right)",
                  "$v_t$ orqali yozilganda tenglama universal shaklga keladi: "
                  "endi u faqat bitta parametrga bog'liq."),
                d("4-qadam. Analitik yechim (tinch holatdan tushish)",
                  r"\frac{dv}{1-(v/v_t)^2} = g\,dt \Rightarrow "
                  r"v(t) = v_t\tanh\!\left(\frac{g t}{v_t}\right)",
                  "Giperbolik tangens — tezlik $v_t$ ga asimptotik intiladi. "
                  "Xarakterli vaqt $\\tau = v_t/g$."),
                d("5-qadam. Tushish balandligi",
                  r"h(t) = \frac{v_t^2}{g}\ln\cosh\!\left(\frac{gt}{v_t}\right)",
                  "$\\tanh$ ni integrallash. Katta $t$ da $h \\approx v_t t - "
                  "(v_t^2/g)\\ln 2$ — ya'ni deyarli tekis tushish."),
            ],
            formula_meaning=(
                "$v_t = \\sqrt{2mg/(\\rho C_d A)}$ formulasi to'rt loyihaviy richagni "
                "ko'rsatadi. Massa ortsa tezlik ortadi (kvadrat ildiz bilan), yuza ortsa "
                "kamayadi. Parashyut aynan $A$ ni keskin oshirish orqali ishlaydi: yuzani "
                "100 marta oshirish tezlikni 10 marta kamaytiradi. $\\tanh$ funksiyasi "
                "esa o'tish jarayonini beradi — tezlik $v_t$ ga taxminan $3\\tau$ vaqtda yetadi."
            ),
            equations=[
                eq(r"F_d = \tfrac{1}{2}\rho C_d A v^2", "Kvadratik qarshilik (yuqori Re).",
                   "Aerodinamik qarshilik"),
                eq(r"v_t = \sqrt{\frac{2mg}{\rho C_d A}}", "Chegaraviy tezlik.", "Chegaraviy tezlik"),
                eq(r"v(t) = v_t\tanh\left(\frac{gt}{v_t}\right)", "Tinch holatdan tushish qonuni.",
                   "Tushish tezligi"),
            ],
            conditions=(
                "Boshlang'ich shart: $v(0) = v_0$. Agar $v_0 > v_t$ bo'lsa, tezlik "
                "kamayib $v_t$ ga intiladi ($\\coth$ yechimi); $v_0 < v_t$ bo'lsa oshib "
                "intiladi ($\\tanh$). Model chegarasi: $\\rho$ balandlik bilan "
                "o'zgaradi (katta balandlikdan sakrashda buni hisobga olish kerak) va "
                "$C_d$ Reynolds soniga hamda jism orientatsiyasiga bog'liq."
            ),
            worked_example=WorkedExample(
                statement=(
                    "Parashyutchi (massasi ekipirovka bilan $m = 90$ kg) erkin tushish "
                    "holatida: $C_d = 1{,}0$, $A = 0{,}7$ m². Parashyut ochilgach: "
                    "$C_d = 1{,}4$, $A = 55$ m². Havo zichligi $\\rho = 1{,}22$ kg/m³. "
                    "Ikkala rejim uchun chegaraviy tezlikni va unga yetish vaqtini toping."
                ),
                given=[r"m = 90\ \text{kg},\; \rho = 1{,}22\ \text{kg/m}^3",
                       r"\text{erkin: } C_d A = 0{,}7\ \text{m}^2",
                       r"\text{parashyut: } C_d A = 77\ \text{m}^2"],
                steps=[
                    st(r"k_1 = \tfrac{1}{2}\rho C_d A = 0{,}5\cdot 1{,}22\cdot 0{,}7 = 0{,}427\ \text{kg/m}",
                       "Erkin tushish rejimidagi qarshilik koeffitsienti."),
                    st(r"v_{t1} = \sqrt{\frac{mg}{k_1}} = \sqrt{\frac{90\cdot 9{,}81}{0{,}427}} = "
                       r"\sqrt{2068} \approx 45{,}5\ \text{m/s}",
                       "Erkin tushishdagi chegaraviy tezlik ≈ 164 km/soat."),
                    st(r"\tau_1 = \frac{v_{t1}}{g} = \frac{45{,}5}{9{,}81} = 4{,}64\ \text{s}",
                       "Xarakterli vaqt; $3\\tau \\approx 14$ s da tezlik $v_t$ ning 99,5 % iga yetadi."),
                    st(r"k_2 = 0{,}5\cdot 1{,}22\cdot 77 = 46{,}97\ \text{kg/m}",
                       "Parashyut ochilgandan keyin."),
                    st(r"v_{t2} = \sqrt{\frac{90\cdot 9{,}81}{46{,}97}} = \sqrt{18{,}8} \approx 4{,}34\ \text{m/s}",
                       "Xavfsiz qo'nish tezligi (odatda 5–6 m/s dan oshmasligi kerak)."),
                    st(r"\frac{v_{t1}}{v_{t2}} = \sqrt{\frac{77}{0{,}7}} = \sqrt{110} = 10{,}5",
                       "Yuzani 110 marta oshirish tezlikni 10,5 marta kamaytirdi — "
                       "kvadrat ildiz qonuni."),
                ],
                answer=(
                    "$v_{t1} \\approx 45{,}5$ m/s ($\\tau_1 = 4{,}6$ s); "
                    "$v_{t2} \\approx 4{,}3$ m/s."
                ),
                engineering_note=(
                    "Parashyut ochilish momentida tezlik hali 45 m/s, lekin qarshilik "
                    "kuchi darhol $k_2v^2 = 46{,}97\\cdot 45{,}5^2 \\approx 97$ kN ga "
                    "sakraydi — bu og'irlikdan 110 marta katta! Shuning uchun parashyut "
                    "bosqichma-bosqich ochiladi, aks holda dinamik zarba odamni "
                    "o'ldirishi mumkin. Bu — mq-27 dagi zarbiy yuklanishning tipik misoli."
                ),
            ),
            computation=Computation(
                caption=(
                    "Ballistik traektoriya: qarshilik koeffitsienti va otish burchagini "
                    "o'zgartirib, vakuumdagi parabola bilan farqni ko'ring."
                ),
                code='''"""Muhit qarshiligi: chegaraviy tezlik va ballistik traektoriya."""
import numpy as np
from scipy.integrate import solve_ivp
from labkit import PARAMS, note, series, table, value

m = float(PARAMS.get("m", 0.145))       # jism massasi (beysbol to'pi), kg
Cd = float(PARAMS.get("Cd", 0.35))      # qarshilik koeffitsienti
A = float(PARAMS.get("A", 0.0042))      # midel yuzasi, m^2
v0 = float(PARAMS.get("v0", 45.0))      # boshlang'ich tezlik, m/s
angle = float(PARAMS.get("angle", 45.0))# otish burchagi, deg
rho, g = 1.22, 9.81

k = 0.5*rho*Cd*A
v_t = np.sqrt(m*g/k)
value("Chegaraviy tezlik v_t", v_t, "m/s")
value("Ballistik koeffitsient m/(Cd·A)", m/(Cd*A), "kg/m²")
value("Xarakterli vaqt τ", v_t/g, "s")

def rhs(t, y):
    x, yy, vx, vy = y
    v = np.hypot(vx, vy)
    return [vx, vy, -k*v*vx/m, -g - k*v*vy/m]

def ground(t, y):
    return y[1]
ground.terminal = True
ground.direction = -1

th = np.radians(angle)
sol = solve_ivp(rhs, (0, 30), [0, 0, v0*np.cos(th), v0*np.sin(th)],
                events=ground, rtol=1e-8, dense_output=True, max_step=0.01)
tt = np.linspace(0, sol.t[-1], 400)
X, Y, VX, VY = sol.sol(tt)
series("Qarshilik bilan", X.tolist(), Y.tolist(), xlabel="x, m", ylabel="y, m")

# Vakuumdagi parabola
t_vac = 2*v0*np.sin(th)/g
tv = np.linspace(0, t_vac, 400)
series("Vakuumda (parabola)", (v0*np.cos(th)*tv).tolist(),
       (v0*np.sin(th)*tv - 0.5*g*tv**2).tolist(), xlabel="x, m", ylabel="y, m")

R_real, R_vac = float(X[-1]), float(v0**2*np.sin(2*th)/g)
value("Uchish masofasi (qarshilik bilan)", R_real, "m")
value("Uchish masofasi (vakuumda)", R_vac, "m")
value("Qisqarish", 100*(1 - R_real/R_vac), "%")

# Optimal burchakni sonli izlash
best = max(((a, solve_ivp(rhs, (0, 30), [0, 0, v0*np.cos(np.radians(a)),
            v0*np.sin(np.radians(a))], events=ground, rtol=1e-7).y_events[0][0][0])
            for a in range(20, 61, 2)), key=lambda p: p[1])
note(f"Qarshilik hisobga olinganda optimal burchak ≈ {best[0]}° "
     f"(vakuumda 45°), masofa {best[1]:.1f} m")

table("Burchakka bog'liqlik", ["α, deg", "Masofa, m"],
      [[float(a), float(solve_ivp(rhs, (0, 30), [0, 0, v0*np.cos(np.radians(a)),
        v0*np.sin(np.radians(a))], events=ground, rtol=1e-7).y_events[0][0][0])]
       for a in (30, 35, 40, 45, 50)])
''',
                parameters=[
                    p("m", "Massa m", 0.01, 10.0, 0.145, 0.005, "kg"),
                    p("Cd", "Qarshilik koeff. C_d", 0.05, 1.5, 0.35, 0.05, "—"),
                    p("A", "Midel yuzasi A", 0.001, 0.5, 0.0042, 0.0005, "m²"),
                    p("v0", "Boshlang'ich tezlik v₀", 5.0, 150.0, 45.0, 1.0, "m/s"),
                    p("angle", "Otish burchagi α", 5.0, 85.0, 45.0, 1.0, "deg"),
                ],
                expected_output="v_t ≈ 34 m/s; masofa qarshilik bilan ≈ 130 m, vakuumda 206 m",
            ),
            visualization=vis(
                "Traektoriyalar oilasi",
                "React/SVG + Matplotlib",
                "Bir grafikda: vakuumdagi simmetrik parabola va qarshilikli "
                "assimetrik traektoriya (tushish shoxi tikroq).",
                "React/SVG: ikki `<path>` — biri punktir (ideal), biri to'liq (real). "
                "Assimetriya vizual jihatdan darhol ko'zga tashlanadi va bu "
                "qarshilikning asosiy sifat effekti.",
            ),
            interpretation=(
                "Qarshilikli traektoriya simmetriyasini yo'qotadi: ko'tarilish shoxi "
                "uzunroq, tushish shoxi tikroq. Uchish masofasi 35–40 % ga qisqaradi. "
                "Optimal burchak 45° dan 38–42° ga tushadi — chunki yuqori burchakda "
                "jism ko'proq vaqt havoda bo'ladi va ko'proq energiya yo'qotadi. "
                "Aynan shu sabab artilleriya jadvallarida burchaklar tajribadan olinadi."
            ),
            common_mistakes=[
                "Qarshilik kuchini $-kv^2$ deb yozish va vektorligini unutish. To'g'risi: "
                "$-k|\\mathbf{v}|\\mathbf{v}$ — modul va yo'nalish alohida.",
                "Chegaraviy tezlikni 'maksimal mumkin bo'lgan tezlik' deb tushunish. "
                "Agar $v_0 > v_t$ bo'lsa, tezlik kamayib $v_t$ ga intiladi.",
                "Stoks va kvadratik modelni Reynolds sonini tekshirmasdan tanlash.",
                "$\\rho$ ni jism zichligi deb olish. Bu — muhit zichligi.",
                "Vakuumdagi 45° qoidasini qarshilikli holga ko'chirish.",
            ],
            quiz=[
                q("Nima uchun chegaraviy tezlik massaning kvadrat ildiziga proporsional?",
                  "Chunki muvozanatda $mg = kv_t^2$, demak $v_t = \\sqrt{mg/k}$. Massa 4 "
                  "marta ortsa, tezlik 2 marta ortadi.", "konseptual"),
                q("Parashyut yuzasini 2 marta oshirsak, qo'nish tezligi qanday o'zgaradi?",
                  "$\\sqrt{2} \\approx 1{,}41$ marta kamayadi.", "hisob"),
                q("$m = 80$ kg, $C_dA = 0{,}8$ m², $\\rho = 1{,}2$ kg/m³. $v_t$ ni toping.",
                  "$v_t = \\sqrt{2\\cdot 80\\cdot 9{,}81/(1{,}2\\cdot 0{,}8)} = "
                  "\\sqrt{1635} \\approx 40{,}4$ m/s.", "hisob"),
                q("Qarshilikli traektoriya nima uchun simmetrik emas?",
                  "Ko'tarilishda qarshilik og'irlik bilan bir yo'nalishda (sekinlatadi), "
                  "tushishda esa qarama-qarshi (tezlanishni kamaytiradi). Natijada "
                  "tushish shoxi tikroq va qisqaroq.", "talqin"),
                q("Kodda `-k*v*vx/m` da nima uchun `v` (to'la tezlik) ham bor?",
                  "Chunki qarshilik $-k|\\mathbf{v}|\\mathbf{v}$: modul $|\\mathbf{v}|$ "
                  "ni komponenta $v_x$ ga ko'paytirish kerak, aks holda yo'nalish noto'g'ri.",
                  "kod"),
                q("Parashyut ochilganda qanday xavf paydo bo'ladi?",
                  "Tezlik hali yuqori bo'lgani uchun qarshilik kuchi og'irlikdan o'nlab "
                  "marta katta bo'lib ketadi — dinamik zarba. Shuning uchun ochilish "
                  "bosqichma-bosqich amalga oshiriladi.", "talqin"),
            ],
            bridge_to_next=(
                "Shu paytgacha jism erkin edi. Real konstruksiyada esa jismlar "
                "sharnir, tayanch va troslar bilan bog'langan. Keyingi mavzuda "
                "bog'lanishlar va ularning reaksiyalarini o'rganamiz."
            ),
            research_extension=(
                "Optimal otish burchagini ballistik koeffitsient $\\beta = m/(C_dA)$ "
                "ning funksiyasi sifatida hisoblang (sonli optimallashtirish). "
                "$\\alpha_{opt}(\\beta)$ bog'liqligini chizing va $\\beta\\to\\infty$ da "
                "u 45° ga intilishini tekshiring. Bu — kichik parametrli asimptotik "
                "tahlilga real kirish."
            ),
        ),
    ),
    Topic(
        id="nm-10",
        subject_id=S,
        module_id=M,
        order=10,
        title="Bog'lanishlar, reaksiya kuchlari va bog'lanishlardan ozod qilish prinsipi",
        description=(
            "Bog'lanish turlari, ularning reaksiyalari, bog'lanishlardan ozod qilish "
            "aksiomasi va hisob sxemasini tuzish metodikasi."
        ),
        learning_objective=(
            "Real tayanchni hisob sxemasidagi bog'lanish modeliga almashtirish va "
            "noma'lum reaksiyalar sonini to'g'ri aniqlash."
        ),
        prerequisites=["nm-07"],
        mathematical_core=(
            "Chiziqli tenglamalar tizimi, statik aniqlik sharti, matritsa rangi."
        ),
        engineering_application=(
            "Balka tayanchlari, ferma tugunlari, mashina detallarining mahkamlanishi, "
            "podshipniklar."
        ),
        computational_component=(
            "Reaksiyalarni chiziqli tenglamalar tizimi sifatida `numpy.linalg.solve` "
            "bilan yechish va matritsa shartlanganligini tekshirish."
        ),
        visualization_component=(
            "Bog'lanish turlari katalogi va har birining reaksiya sxemasi."
        ),
        research_extension=(
            "Statik aniqmas tizimda reaksiyalarni topish uchun nima yetishmaydi? "
            "Bu savol mq-06 da deformatsiya shartlari orqali hal qilinadi."
        ),
        difficulty="asosiy",
        previous_link=(
            "nm-07 dagi erkin jism diagrammasini chizish uchun bog'lanishlarni "
            "kuchlar bilan almashtirish kerak edi. Endi buni tizimli o'rganamiz."
        ),
        next_topic="nm-11",
        estimated_minutes=85,
        tags=["bog'lanish", "reaksiya", "hisob sxemasi"],
        lesson=Lesson(
            physical_problem=(
                "Kran balkasi ikki tayanchga o'rnatilgan: biri qo'zg'almas sharnir, "
                "ikkinchisi rolikli. Nima uchun aynan shunday? Agar ikkalasi ham "
                "qo'zg'almas bo'lsa, temperatura o'zgarganda balkada ulkan kuchlanish "
                "paydo bo'ladi. Bog'lanishni to'g'ri tanlash — konstruksiya "
                "ishonchliligining asosi."
            ),
            concepts=[
                c("Bog'lanish (constraint)", "Jism harakatini cheklovchi obyekt. "
                  "Har bir cheklangan ko'chish yo'nalishida reaksiya paydo bo'ladi."),
                c("Bog'lanishlardan ozod qilish aksiomasi", "Bog'lanishni olib tashlab, "
                  "uning o'rniga reaksiya kuchini qo'yish mumkin — jismning holati "
                  "o'zgarmaydi. Bu barcha statika hisoblarining asosi."),
                c("Silliq tayanch", "Faqat sirtga normal reaksiya: 1 ta noma'lum."),
                c("Qo'zg'almas sharnir (pin)", "Ikki yo'nalishdagi ko'chishni cheklaydi: "
                  "2 ta noma'lum ($R_x$, $R_y$), burilishga to'sqinlik qilmaydi."),
                c("Qotirish (fixed/clamped)", "Barcha ko'chish va burilishni cheklaydi: "
                  "tekislikda 3 ta noma'lum ($R_x$, $R_y$, $M$)."),
            ],
            derivation=[
                d("1-qadam. Erkinlik darajalari va bog'lanishlar balansi",
                  r"n_{\text{erkin}} = 3 \;(\text{tekislikda}),\qquad "
                  r"s = \sum(\text{cheklangan ko'chishlar})",
                  "Tekis masalada jism 3 ta erkinlik darajasiga ega ($x, y, \\varphi$). "
                  "Har bir bog'lanish ularning bir qismini cheklaydi."),
                d("2-qadam. Muvozanat tenglamalari soni",
                  r"\sum F_x = 0,\quad \sum F_y = 0,\quad \sum M_A = 0 \;\Rightarrow\; 3\ \text{tenglama}",
                  "Tekis masala uchun mustaqil muvozanat tenglamalari soni aynan 3 ta "
                  "(nm-11 da asoslanadi)."),
                d("3-qadam. Statik aniqlik sharti",
                  r"\boxed{\;s = 3 \;\Rightarrow\; \text{statik aniq};\qquad "
                  r"s > 3 \;\Rightarrow\; \text{statik aniqmas}\;}",
                  "$s < 3$ bo'lsa mexanizm — muvozanat imkonsiz. $s > 3$ bo'lsa "
                  "qo'shimcha deformatsiya shartlari kerak (mq-06)."),
                d("4-qadam. Reaksiyalarni chiziqli tizim sifatida yozish",
                  r"[A]\{R\} = \{b\},\qquad [A] \in \mathbb{R}^{3\times 3}",
                  "Muvozanat tenglamalari noma'lum reaksiyalarga nisbatan chiziqli. "
                  "$\\det[A] \\neq 0$ bo'lsa yechim yagona; $\\det[A] = 0$ — bog'lanishlar "
                  "geometrik jihatdan o'zgaruvchan (masalan, uchta reaksiya bitta nuqtada kesishadi)."),
                d("5-qadam. Balka uchun qo'llash",
                  r"\sum M_A = 0:\; R_B L - q\frac{L^2}{2} - F a = 0 \Rightarrow "
                  r"R_B = \frac{qL/2 \cdot L + Fa}{L}",
                  "Moment markazini A ga qo'yish $R_{Ax}$ va $R_{Ay}$ ni tenglamadan "
                  "chiqarib tashlaydi — bu hisobni soddalashtirishning standart usuli."),
            ],
            formula_meaning=(
                "$s = 3$ sharti — konstruksiya loyihalashning asosiy mezoni. Kam bo'lsa "
                "konstruksiya harakatlanadi (mexanizm), ko'p bo'lsa ortiqcha "
                "bog'langan: bu bir tomondan ishonchlilikni oshiradi (bitta bog'lanish "
                "buzilsa ham turadi), ikkinchi tomondan temperatura va o'tirish "
                "kuchlanishlarini keltirib chiqaradi. Rolikli tayanch aynan shu ikkinchi "
                "muammoni yechish uchun ishlatiladi."
            ),
            equations=[
                eq(r"\sum \mathbf{F} = 0,\quad \sum \mathbf{M}_A = 0", "Muvozanat shartlari.",
                   "Muvozanat"),
                eq(r"s = 3\ (\text{tekis}),\quad s = 6\ (\text{fazoviy})",
                   "Statik aniqlik shartlari.", "Statik aniqlik"),
            ],
            conditions=(
                "Bog'lanish modelini tanlash — muhandislik qarori, matematik emas. "
                "Masalan, podshipnik burilishga qisman qarshilik qiladi; uni sharnir "
                "(qarshilik yo'q) yoki qotirish (to'liq qarshilik) deb olish "
                "natijaning ikki chegarasini beradi. Real javob oralig'ida, shuning "
                "uchun ko'pincha ikkala variant ham hisoblanadi."
            ),
            worked_example=WorkedExample(
                statement=(
                    "$L = 6$ m uzunlikdagi balka A da qo'zg'almas sharnir, B da rolikli "
                    "tayanchga o'rnatilgan. Unga $q = 12$ kN/m tekis taqsimlangan yuklama "
                    "va A dan $a = 4$ m masofada $F = 30$ kN nuqtaviy kuch (pastga) "
                    "ta'sir qiladi. Tayanch reaksiyalarini toping."
                ),
                given=[r"L = 6\ \text{m},\; q = 12\ \text{kN/m}",
                       r"F = 30\ \text{kN},\; a = 4\ \text{m}"],
                steps=[
                    st(r"Q = qL = 12\cdot 6 = 72\ \text{kN}\;(\text{markazda, } x = 3\ \text{m})",
                       "Taqsimlangan yuklamani ekvivalent yig'indi kuch bilan almashtiramiz."),
                    st(r"s = 2 + 1 = 3 = 3 \Rightarrow \text{statik aniq}",
                       "Sharnir 2 ta, rolik 1 ta reaksiya beradi — masala yechiladi."),
                    st(r"\sum M_A = 0:\; R_B\cdot 6 - 72\cdot 3 - 30\cdot 4 = 0",
                       "A ga nisbatan moment — $R_{Ax}$ va $R_{Ay}$ qatnashmaydi."),
                    st(r"R_B = \frac{216 + 120}{6} = \frac{336}{6} = 56\ \text{kN}",
                       "B tayanch reaksiyasi."),
                    st(r"\sum F_y = 0:\; R_{Ay} + R_B - Q - F = 0 \Rightarrow "
                       r"R_{Ay} = 72 + 30 - 56 = 46\ \text{kN}",
                       "Vertikal proyeksiyalar."),
                    st(r"\sum F_x = 0:\; R_{Ax} = 0",
                       "Gorizontal kuchlar yo'q. Tekshirish: "
                       "$\\sum M_B = -46\\cdot 6 + 72\\cdot 3 + 30\\cdot 2 = -276+216+60 = 0$ ✓"),
                ],
                answer="$R_{Ax} = 0$; $R_{Ay} = 46$ kN; $R_B = 56$ kN.",
                engineering_note=(
                    "Tekshirishni boshqa nuqtaga nisbatan moment orqali bajarish — "
                    "majburiy amal. Agar $\\sum M_B \\neq 0$ chiqsa, hisobda xato bor. "
                    "Bu reaksiyalar mq-12 da kesuvchi kuch va eguvchi moment "
                    "epyuralarini qurish uchun boshlang'ich ma'lumot bo'ladi."
                ),
            ),
            computation=Computation(
                caption=(
                    "Balka reaksiyalari: yuklama va uning joylashuvini o'zgartirib, "
                    "reaksiyalarning qayta taqsimlanishini kuzating."
                ),
                code='''"""Statik aniq balka reaksiyalarini chiziqli tizim sifatida yechish."""
import numpy as np
from labkit import PARAMS, note, series, table, value

L = float(PARAMS.get("L", 6.0))     # balka uzunligi, m
qd = float(PARAMS.get("q", 12.0))   # taqsimlangan yuklama, kN/m
F = float(PARAMS.get("F", 30.0))    # nuqtaviy kuch, kN
a = float(PARAMS.get("a", 4.0))     # kuch koordinatasi, m

Q = qd*L                             # yig'indi taqsimlangan kuch
# Noma'lumlar: [Rax, Ray, Rb]
# 1) sum Fx = 0 : Rax = 0
# 2) sum Fy = 0 : Ray + Rb = Q + F
# 3) sum M_A = 0: Rb*L = Q*L/2 + F*a
A = np.array([[1.0, 0.0, 0.0],
              [0.0, 1.0, 1.0],
              [0.0, 0.0, L]])
b = np.array([0.0, Q + F, Q*L/2 + F*a])
R = np.linalg.solve(A, b)

value("R_Ax", R[0], "kN")
value("R_Ay", R[1], "kN")
value("R_B", R[2], "kN")
value("Matritsa shartlanganligi", float(np.linalg.cond(A)), "—")

# Tekshirish: B ga nisbatan moment
check = -R[1]*L + Q*L/2 + F*(L - a)
note(f"Tekshirish sum(M_B) = {check:.10f} kN·m (nolga teng bo'lishi kerak)")

# Kuch joylashuvining reaksiyalarga ta'siri
aa = np.linspace(0, L, 100)
Rb = (Q*L/2 + F*aa)/L
series("R_B(a)", aa.tolist(), Rb.tolist(), xlabel="Kuch koordinatasi a, m", ylabel="R_B, kN")
series("R_Ay(a)", aa.tolist(), (Q + F - Rb).tolist(),
       xlabel="Kuch koordinatasi a, m", ylabel="R_Ay, kN")

table("Chegaraviy holatlar",
      ["a, m", "R_Ay, kN", "R_B, kN"],
      [[0.0, float(Q/2 + F), float(Q/2)],
       [L/2, float(Q/2 + F/2), float(Q/2 + F/2)],
       [L, float(Q/2), float(Q/2 + F)]])
''',
                parameters=[
                    p("L", "Balka uzunligi L", 1.0, 20.0, 6.0, 0.5, "m"),
                    p("q", "Taqsimlangan yuklama q", 0.0, 50.0, 12.0, 1.0, "kN/m"),
                    p("F", "Nuqtaviy kuch F", 0.0, 200.0, 30.0, 5.0, "kN"),
                    p("a", "Kuch koordinatasi a", 0.0, 20.0, 4.0, 0.25, "m"),
                ],
                expected_output="R_Ax = 0, R_Ay = 46 kN, R_B = 56 kN",
            ),
            visualization=vis(
                "Bog'lanishlar katalogi va hisob sxemasi",
                "React/SVG",
                "Har bir bog'lanish turi uchun: real tasvir → hisob sxemasi belgisi → "
                "reaksiya strelkalari. Yonida balka sxemasi va topilgan reaksiyalar.",
                "React/SVG: bog'lanish belgilarini (sharnir — uchburchak, rolik — "
                "uchburchak + aylanalar, qotirish — shtrixlangan devor) alohida kichik "
                "komponentalar sifatida yozing va ularni balka sxemasida qayta ishlating. "
                "Bu komponentalar mq-12 dagi epyuralarda ham kerak bo'ladi.",
            ),
            interpretation=(
                "$R_B(a)$ grafigi chiziqli: kuch B ga yaqinlashgani sari B tayanch "
                "ko'proq yuk oladi. Chegaraviy holatlar jadvalida $a = 0$ da barcha "
                "nuqtaviy kuch A ga, $a = L$ da B ga tushishi ko'rinadi. Taqsimlangan "
                "yuklama esa har doim teng bo'linadi — chunki u simmetrik."
            ),
            common_mistakes=[
                "Rolikli tayanchga gorizontal reaksiya qo'yish. U faqat normal "
                "yo'nalishda reaksiya beradi.",
                "Taqsimlangan yuklamani yig'indi kuch bilan almashtirganda uning "
                "qo'yilish nuqtasini noto'g'ri olish (tekis yuklama uchun — markazda, "
                "uchburchak uchun — uchdan bir masofada).",
                "Moment markazini tasodifiy tanlash. Noma'lum reaksiyalar kesishgan "
                "nuqta tanlansa, tenglama bitta noma'lumli bo'ladi.",
                "Statik aniqlikni tekshirmasdan hisobga kirishish — statik aniqmas "
                "tizimda 3 ta tenglama yetmaydi.",
                "Tekshirish tenglamasini bajarmaslik. Bu 5 soniya vaqt oladi, lekin "
                "xatolarning yarmini topadi.",
            ],
            quiz=[
                q("Nima uchun bitta tayanch rolikli qilinadi?",
                  "Balkaning temperatura o'zgarishida erkin cho'zilishiga imkon berish "
                  "uchun. Ikkala tayanch qo'zg'almas bo'lsa, katta temperatura "
                  "kuchlanishlari paydo bo'ladi (mq-06).", "konseptual"),
                q("Tekislikda qotirish nechta noma'lum beradi va nega?",
                  "3 ta: $R_x$, $R_y$, $M$. Chunki u uchta erkinlik darajasining "
                  "hammasini (ikki ko'chish va burilish) cheklaydi.", "konseptual"),
                q("Konsol balka (bir uchi qotirilgan) statik aniqmi?",
                  "Ha: $s = 3 = 3$. Bitta qotirish uchta reaksiya beradi va uchta "
                  "muvozanat tenglamasi ularni aniqlaydi.", "hisob"),
                q("$L = 4$ m, o'rtasida $F = 20$ kN. Reaksiyalar qanday?",
                  "Simmetriya bo'yicha $R_A = R_B = 10$ kN.", "hisob"),
                q("Kodda `np.linalg.cond(A)` nima uchun chiqariladi?",
                  "Shartlanganlik soni matritsaning 'xavfsizligini' ko'rsatadi. Agar u "
                  "juda katta bo'lsa (masalan $10^{12}$), bog'lanishlar geometrik "
                  "jihatdan deyarli o'zgaruvchan va yechim ishonchsiz.", "kod"),
                q("Uchta reaksiya chizig'i bitta nuqtada kesishsa nima bo'ladi?",
                  "Shu nuqtaga nisbatan moment tenglamasi ayniyatga aylanadi — tizim "
                  "yechilmaydi, konstruksiya oniy o'zgaruvchan bo'ladi. "
                  "$\\det[A] = 0$ buni ko'rsatadi.", "talqin"),
            ],
            bridge_to_next=(
                "Reaksiyalarni topish uchun muvozanat tenglamalaridan foydalandik, "
                "lekin ularning nima uchun aynan uchtaligini asoslamadik. Keyingi "
                "mavzuda kuchlar sistemasi nazariyasini — bosh vektor va bosh momentni "
                "o'rganamiz."
            ),
            research_extension=(
                "Uch tayanchli (statik aniqmas) balkani ko'ring. Uchinchi reaksiyani "
                "parametr sifatida olib, deformatsiya shartini qo'shmasdan turib "
                "tenglamalar tizimining cheksiz ko'p yechimi borligini ko'rsating. "
                "So'ngra mq-17 da bu yechim qanday tanlanishini oldindan taxmin qiling."
            ),
        ),
    ),
    Topic(
        id="nm-11",
        subject_id=S,
        module_id=M,
        order=11,
        title="Kuchlar sistemasining muvozanati: bosh vektor, bosh moment va keltirish",
        description=(
            "Kuchlar sistemasini bir nuqtaga keltirish, bosh vektor va bosh moment, "
            "muvozanat shartlarining to'liq tizimi, ferma hisobi."
        ),
        learning_objective=(
            "Ixtiyoriy kuchlar sistemasini markazga keltirish va muvozanat "
            "shartlarini to'g'ri yozish; fermada sterjen kuchlarini topish."
        ),
        prerequisites=["nm-10"],
        mathematical_core=(
            "Vektorlar yig'indisi, momentlar yig'indisi, keltirish markazi "
            "almashtirilganda momentning o'zgarishi, chiziqli tenglamalar tizimi."
        ),
        engineering_application=(
            "Ferma konstruksiyalari (ko'prik, tom fermasi), kran, ramalar, "
            "mahkamlash birikmalari."
        ),
        computational_component=(
            "Fermaning barcha sterjen kuchlarini tugunlar usuli bilan matritsa "
            "shaklida yechish."
        ),
        visualization_component=(
            "Ferma sxemasi, sterjenlar cho'zilgan/siqilganligi rang bilan; "
            "kuchlar ko'pburchagi."
        ),
        research_extension=(
            "Ferma optimallashtirish: bir xil yuk uchun eng yengil ferma "
            "topologiyasi qanday bo'ladi?"
        ),
        difficulty="asosiy",
        previous_link=(
            "nm-10 da uchta muvozanat tenglamasini ishlatdik. Endi ularning umumiy "
            "nazariyasini — kuchlar sistemasini keltirish orqali asoslaymiz."
        ),
        next_topic="nm-12",
        estimated_minutes=90,
        tags=["statika", "ferma", "bosh moment"],
        lesson=Lesson(
            physical_problem=(
                "Ko'prik fermasi o'nlab sterjendan iborat. Yuk yuklanganda qaysi "
                "sterjen cho'ziladi, qaysi biri siqiladi? Bu farq hal qiluvchi: "
                "siqilgan sterjen ustuvorlikni yo'qotib egilishi mumkin (mq-25), "
                "cho'zilgan esa faqat mustahkamlikka hisoblanadi. Demak avval har bir "
                "sterjendagi kuchni aniq bilish kerak."
            ),
            concepts=[
                c("Bosh vektor (resultant force)", "$\\mathbf{R} = \\sum\\mathbf{F}_i$ — "
                  "keltirish markazidan bog'liq emas."),
                c("Bosh moment (resultant moment)", "$\\mathbf{M}_O = \\sum\\mathbf{r}_i\\times\\mathbf{F}_i$ "
                  "— keltirish markaziga bog'liq."),
                c("Kuchlar sistemasini keltirish", "Ixtiyoriy sistema bir kuch "
                  "($\\mathbf{R}$) va bir juftlik ($\\mathbf{M}_O$) ga keltiriladi."),
                c("Ferma (truss)", "Faqat sharnirli tugunlardan iborat sterjenli "
                  "konstruksiya; sterjenlarda faqat bo'ylama kuch bo'ladi."),
                c("Tugunlar usuli", "Har bir tugun uchun $\\sum F_x = 0$, $\\sum F_y = 0$ "
                  "yoziladi; $2n$ ta tenglama va $s + r$ ta noma'lum."),
            ],
            derivation=[
                d("1-qadam. Kuchni parallel ko'chirish (Puanso teoremasi)",
                  r"\mathbf{F}\ \text{A da} \;\equiv\; \mathbf{F}\ \text{O da} + "
                  r"\text{juftlik } \mathbf{M} = \mathbf{r}_{OA}\times\mathbf{F}",
                  "Kuchni boshqa nuqtaga ko'chirsak, qo'shimcha juftlik paydo bo'ladi. "
                  "Bu — keltirish nazariyasining asosi."),
                d("2-qadam. Butun sistemani keltirish",
                  r"\mathbf{R} = \sum_i \mathbf{F}_i,\qquad \mathbf{M}_O = \sum_i \mathbf{r}_i\times\mathbf{F}_i",
                  "Har bir kuchni O ga ko'chiramiz va hosil bo'lgan kuchlarni hamda "
                  "juftliklarni alohida jamlaymiz."),
                d("3-qadam. Markaz almashtirilganda bosh momentning o'zgarishi",
                  r"\mathbf{M}_{O'} = \mathbf{M}_O + \mathbf{r}_{O'O}\times\mathbf{R}",
                  "Agar $\\mathbf{R} = 0$ bo'lsa, bosh moment markazdan bog'liq emas — "
                  "bu juftlikning asosiy xossasi."),
                d("4-qadam. Muvozanat shartlari",
                  r"\boxed{\;\mathbf{R} = 0 \;\text{va}\; \mathbf{M}_O = 0\;}",
                  "Fazoda 6 ta skalyar tenglama, tekislikda 3 ta. Bu nm-10 dagi "
                  "shartlarning to'liq asosi."),
                d("5-qadam. Ferma tuguni uchun tenglamalar",
                  r"\sum_j N_j\cos\alpha_j + F_x = 0,\qquad \sum_j N_j\sin\alpha_j + F_y = 0",
                  "Tugundagi barcha kuchlar bitta nuqtada kesishgani uchun moment "
                  "tenglamasi ayniyat bo'ladi — faqat ikkita proyeksiya qoladi. "
                  "$N_j > 0$ — cho'zilish, $N_j < 0$ — siqilish."),
            ],
            formula_meaning=(
                "$\\mathbf{R} = 0$ jismning ilgarilanma harakatga kirmasligini, "
                "$\\mathbf{M}_O = 0$ esa burilmasligini kafolatlaydi. Fermada har bir "
                "tugunning muvozanati butun konstruksiyani bog'laydi: bitta sterjendagi "
                "kuch o'zgarsa, u qo'shni tugunlar orqali butun tizimga tarqaladi. Bu — "
                "chiziqli tenglamalar tizimining fizik ma'nosi va u su-03 dagi "
                "matritsalarni yechish usullariga bevosita olib boradi."
            ),
            equations=[
                eq(r"\mathbf{R} = \sum\mathbf{F}_i = 0", "Bosh vektor muvozanati.", "1-shart"),
                eq(r"\mathbf{M}_O = \sum\mathbf{r}_i\times\mathbf{F}_i = 0", "Bosh moment muvozanati.",
                   "2-shart"),
                eq(r"s + r = 2n", "Fermaning statik aniqlik sharti ($s$ — sterjenlar, "
                   "$r$ — reaksiyalar, $n$ — tugunlar).", "Ferma statik aniqligi"),
            ],
            conditions=(
                "Ferma modeli farazlari: tugunlar ideal sharnirli, yuk faqat tugunlarga "
                "qo'yilgan, sterjenlar og'irligi e'tiborga olinmaydi yoki tugunlarga "
                "taqsimlanadi. Real fermada tugunlar payvandlangan bo'lsa, qo'shimcha "
                "eguvchi moment paydo bo'ladi — u odatda 10–15 % ni tashkil qiladi va "
                "ikkilamchi kuchlanish deb ataladi."
            ),
            worked_example=WorkedExample(
                statement=(
                    "Oddiy uch sterjenli ferma: A(0; 0) va C(4; 0) tayanchlar, B(2; 1,5) "
                    "yuqori tugun. B tugunga vertikal pastga $F = 40$ kN kuch ta'sir "
                    "qiladi. AB, BC va AC sterjenlaridagi kuchlarni toping."
                ),
                given=[r"A(0;0),\; C(4;0),\; B(2;1{,}5)\ \text{m}", r"F = 40\ \text{kN (pastga)}"],
                steps=[
                    st(r"L_{AB} = L_{BC} = \sqrt{2^2+1{,}5^2} = 2{,}5\ \text{m},\quad "
                       r"\cos\alpha = \frac{2}{2{,}5} = 0{,}8,\; \sin\alpha = \frac{1{,}5}{2{,}5} = 0{,}6",
                       "Geometriya: sterjenlar uzunligi va yo'naltiruvchi kosinuslar."),
                    st(r"\text{B tuguni, } \sum F_x = 0:\; -N_{AB}\cdot 0{,}8 + N_{BC}\cdot 0{,}8 = 0 "
                       r"\Rightarrow N_{AB} = N_{BC}",
                       "Simmetriya natijasi tenglamadan kelib chiqdi."),
                    st(r"\sum F_y = 0:\; -N_{AB}\cdot 0{,}6 - N_{BC}\cdot 0{,}6 - 40 = 0",
                       "Sterjen kuchlari tugundan tashqariga (cho'zilish) musbat deb olindi."),
                    st(r"-1{,}2\,N_{AB} = 40 \Rightarrow N_{AB} = N_{BC} = -33{,}33\ \text{kN}",
                       "Manfiy ishora — sterjenlar siqilgan."),
                    st(r"\text{A tuguni, } \sum F_x = 0:\; N_{AB}\cdot 0{,}8 + N_{AC} = 0 "
                       r"\Rightarrow N_{AC} = 33{,}33\cdot 0{,}8 = +26{,}67\ \text{kN}",
                       "AC sterjeni cho'zilgan."),
                    st(r"\text{Tekshirish: } \sum F_y (\text{A}) = R_A + N_{AB}\cdot 0{,}6 = "
                       r"20 - 20 = 0 \;\checkmark",
                       "Simmetriya bo'yicha $R_A = R_C = 20$ kN."),
                ],
                answer=(
                    "$N_{AB} = N_{BC} = -33{,}33$ kN (siqilgan); $N_{AC} = +26{,}67$ kN "
                    "(cho'zilgan)."
                ),
                engineering_note=(
                    "Siqilgan sterjenlar (AB, BC) uchun ustuvorlik hisobi shart — ular "
                    "mustahkamlik yetarli bo'lsa ham egilib ketishi mumkin (mq-25). "
                    "Cho'zilgan AC esa faqat $\\sigma = N/A \\le [\\sigma]$ sharti bo'yicha "
                    "tekshiriladi. Shuning uchun AC ni yupqa trosdan, AB va BC ni "
                    "quvurdan qilish ratsional."
                ),
            ),
            computation=Computation(
                caption=(
                    "Ferma hisobi: tugun balandligini o'zgartirib, sterjen kuchlarining "
                    "qanday qayta taqsimlanishini ko'ring."
                ),
                code='''"""Ferma: tugunlar usulini matritsa ko'rinishida yechish."""
import numpy as np
from labkit import PARAMS, note, series, table, value

span = float(PARAMS.get("span", 4.0))    # oraliq, m
h = float(PARAMS.get("h", 1.5))          # ferma balandligi, m
F = float(PARAMS.get("F", 40.0))         # tugun yuki, kN

# Tugunlar: 0 -> A(0,0), 1 -> C(span,0), 2 -> B(span/2, h)
nodes = np.array([[0.0, 0.0], [span, 0.0], [span/2, h]])
bars = [(0, 2), (2, 1), (0, 1)]          # AB, BC, AC

def bar_dir(i, j):
    d = nodes[j] - nodes[i]
    return d/np.linalg.norm(d), float(np.linalg.norm(d))

# Noma'lumlar: N_AB, N_BC, N_AC, R_Ay, R_Cy  (R_Ax = 0 simmetriya uchun)
# Tenglamalar: A(x,y), C(x,y), B(x,y) -> 6 ta, lekin Ax ni tashlaymiz -> 5 ta
A_mat = np.zeros((5, 5)); b_vec = np.zeros(5)
rows = {"Ay": 0, "Cx": 1, "Cy": 2, "Bx": 3, "By": 4}

for k, (i, j) in enumerate(bars):
    e, _ = bar_dir(i, j)
    # i tugunida kuch +e yo'nalishida, j tugunida -e
    for node, sign in ((i, 1.0), (j, -1.0)):
        if node == 0:
            A_mat[rows["Ay"], k] += sign*e[1]
        elif node == 1:
            A_mat[rows["Cx"], k] += sign*e[0]
            A_mat[rows["Cy"], k] += sign*e[1]
        else:
            A_mat[rows["Bx"], k] += sign*e[0]
            A_mat[rows["By"], k] += sign*e[1]

A_mat[rows["Ay"], 3] = 1.0      # R_Ay
A_mat[rows["Cy"], 4] = 1.0      # R_Cy
b_vec[rows["By"]] = F           # B tugunidagi pastga yo'nalgan yuk

sol = np.linalg.solve(A_mat, b_vec)
N = sol[:3]
value("N_AB", N[0], "kN")
value("N_BC", N[1], "kN")
value("N_AC", N[2], "kN")
value("R_Ay", sol[3], "kN")
value("R_Cy", sol[4], "kN")
note("Musbat qiymat — cho'zilish, manfiy — siqilish.")

# Statik aniqlik: s + r = 2n
s, r, n = len(bars), 3, len(nodes)
note(f"Statik aniqlik: s+r = {s+r}, 2n = {2*n} -> "
     f"{'statik aniq' if s+r == 2*n else 'aniqmas yoki mexanizm'}")

# Balandlikning sterjen kuchlariga ta'siri
hh = np.linspace(0.3, 4.0, 80)
n_ab = -F/2*np.sqrt((span/2)**2 + hh**2)/hh
n_ac = F/2*(span/2)/hh
series("N_AB(h) — siqilgan raskos", hh.tolist(), n_ab.tolist(),
       xlabel="Balandlik h, m", ylabel="N, kN")
series("N_AC(h) — cho'zilgan quyi kamar", hh.tolist(), n_ac.tolist(),
       xlabel="Balandlik h, m", ylabel="N, kN")

table("Balandlikka bog'liqlik", ["h, m", "N_AB, kN", "N_AC, kN"],
      [[float(x), float(-F/2*np.sqrt((span/2)**2+x**2)/x), float(F/2*(span/2)/x)]
       for x in (0.5, 1.0, 1.5, 2.0, 3.0)])
''',
                parameters=[
                    p("span", "Oraliq", 1.0, 20.0, 4.0, 0.5, "m"),
                    p("h", "Ferma balandligi h", 0.3, 6.0, 1.5, 0.1, "m"),
                    p("F", "Tugun yuki F", 5.0, 300.0, 40.0, 5.0, "kN"),
                ],
                expected_output="N_AB = N_BC = -33,33 kN; N_AC = +26,67 kN; R = 20 kN",
            ),
            visualization=vis(
                "Ferma sxemasi va sterjen kuchlari",
                "React/SVG",
                "Tugunlar aylanalar, sterjenlar chiziqlar; cho'zilgan sterjenlar bir "
                "rangda, siqilganlar boshqa rangda; chiziq qalinligi kuch moduliga "
                "proporsional. Yonida tugun uchun kuchlar ko'pburchagi.",
                "React/SVG bu yerda eng mos: ferma — grafik struktura, uni SVG da "
                "chizish tabiiy. Rang kodlashda cho'zilish/siqilish uchun issiq/sovuq "
                "juftlikni ishlating — bu platformadagi barcha kuchlanish "
                "vizualizatsiyalarida izchil qo'llaniladi.",
            ),
            interpretation=(
                "Grafikdan asosiy muhandislik xulosasi chiqadi: ferma balandligi "
                "kamayganda sterjen kuchlari keskin (giperbolik) ortadi. $h = 0{,}5$ m "
                "da $N_{AC} = 80$ kN, $h = 2$ m da esa atigi 20 kN. Shuning uchun past "
                "fermalar material bo'yicha samarasiz — lekin balandlik konstruktiv "
                "cheklovlarga (gabarit, shamol yuki) bog'liq. Optimal $h/L \\approx 1/5...1/8$."
            ),
            common_mistakes=[
                "Sterjen kuchi ishorasini shartlashmasdan hisoblash. Standart: "
                "tugundan tashqariga yo'nalgan kuch musbat (cho'zilish).",
                "Fermada moment tenglamasini tugun uchun yozish — u ayniyatga aylanadi, "
                "chunki barcha kuchlar bitta nuqtada kesishadi.",
                "Yukni sterjen o'rtasiga qo'yish. Klassik ferma modelida yuk faqat "
                "tugunlarga qo'yiladi, aks holda sterjen egiladi.",
                "Statik aniqlik shartini ($s+r = 2n$) tekshirmaslik.",
                "Bosh momentni keltirish markazidan bog'liq emas deb hisoblash. "
                "U faqat $\\mathbf{R}=0$ bo'lgandagina markazdan bog'liq emas.",
            ],
            quiz=[
                q("Nima uchun bosh vektor keltirish markazidan bog'liq emas?",
                  "Chunki u shunchaki kuchlar vektor yig'indisi — kuchlarni ko'chirish "
                  "ularning kattaligi va yo'nalishini o'zgartirmaydi, faqat qo'shimcha "
                  "juftliklar hosil qiladi.", "konseptual"),
                q("Kuchlar sistemasi juftlikka keltirilgan bo'lsa, bu nimani bildiradi?",
                  "$\\mathbf{R} = 0$, $\\mathbf{M}_O \\neq 0$. Jism ilgarilanma "
                  "harakatlanmaydi, lekin buriladi.", "konseptual"),
                q("6 ta sterjen va 4 ta tugunli ferma, 3 ta reaksiya bilan statik aniqmi?",
                  "$s+r = 6+3 = 9$, $2n = 8$. $9 > 8$ — bir marta statik aniqmas.", "hisob"),
                q("Ferma balandligini 2 marta oshirsak, quyi kamar kuchi qanday o'zgaradi?",
                  "2 marta kamayadi, chunki $N_{AC} \\propto 1/h$.", "hisob"),
                q("Kodda `A_mat` matritsasi qanday qurilgan?",
                  "Har bir sterjen uchun birlik yo'naltiruvchi vektor hisoblanadi va "
                  "uning komponentalari mos tugun tenglamalari qatorlariga qo'yiladi. "
                  "Bu — FEM dagi yig'ish (assembly) jarayonining eng sodda ko'rinishi (su-19).",
                  "kod"),
                q("Nima uchun siqilgan va cho'zilgan sterjenlar turlicha loyihalanadi?",
                  "Cho'zilgan sterjen faqat mustahkamlikka ($\\sigma \\le [\\sigma]$), "
                  "siqilgan esa yana ustuvorlikka ham hisoblanadi — u kuchlanish "
                  "ruxsat etilganidan past bo'lsa ham egilib ketishi mumkin.", "talqin"),
            ],
            bridge_to_next=(
                "Muvozanat shartlari ideal, ishqalanishsiz bog'lanishlar uchun yozildi. "
                "Real hayotda esa ishqalanish muvozanatni saqlashda ham, buzishda ham "
                "asosiy rol o'ynaydi. Keyingi mavzu shu haqda."
            ),
            research_extension=(
                "Ferma topologiyasini optimallashtiring: berilgan yuk va oraliq uchun "
                "sterjenlar umumiy hajmini ($\\sum A_i L_i$) minimallashtiring, bunda "
                "har bir sterjen $\\sigma \\le [\\sigma]$ shartini qanoatlantirsin. "
                "`scipy.optimize` bilan $h$ ni optimallashtirib boshlang, so'ngra "
                "qo'shimcha tugun qo'shish foyda berishini tekshiring."
            ),
            manim=manim(
                scene="TrussForceScene",
                module="animatsiya/scenes/nm_statics.py",
                title="Fermada kuchlarning taqsimlanishi",
                summary="Yuk qo'yilganda sterjenlar ketma-ket rangga bo'yaladi: "
                        "cho'zilgan va siqilgan sterjenlar, tugun muvozanati ko'pburchagi.",
            ),
        ),
    ),
    Topic(
        id="nm-12",
        subject_id=S,
        module_id=M,
        order=12,
        title="Ishqalanish qonunlari va muvozanat masalalarida ishqalanishning hisobi",
        description=(
            "Quruq ishqalanish (Kulon qonuni), ishqalanish konusi, o'z-o'zidan "
            "tormozlanish, dumalash qarshiligi."
        ),
        learning_objective=(
            "Ishqalanishli muvozanat masalalarini yechish va o'z-o'zidan tormozlanish "
            "shartini aniqlash."
        ),
        prerequisites=["nm-11"],
        mathematical_core=(
            "Tengsizlik shartlari, chegaraviy muvozanat, konus ichidagi soha, "
            "sistemaning tengsizliklar bilan yechilishi."
        ),
        engineering_application=(
            "Vint birikma, tormoz, ponasimon birikma, friksion uzatma, yuk ko'tarish "
            "mexanizmlari xavfsizligi."
        ),
        computational_component=(
            "Qiya tekislikdagi jism uchun muvozanat sohasini $(\\alpha, f)$ tekisligida "
            "hisoblash va chizish."
        ),
        visualization_component=(
            "Ishqalanish konusi, muvozanat sohasi diagrammasi, vint birikma sxemasi."
        ),
        research_extension=(
            "Statik va kinetik ishqalanish farqi stick-slip tebranishini keltirib "
            "chiqaradi. Uni modellashtiring."
        ),
        difficulty="asosiy",
        previous_link=(
            "nm-10 va nm-11 da bog'lanishlarni ideal (silliq) deb oldik. Endi bu "
            "farazni olib tashlaymiz va muvozanat tenglik emas, tengsizlik bilan "
            "aniqlanishini ko'ramiz."
        ),
        next_topic="nm-13",
        estimated_minutes=90,
        tags=["ishqalanish", "Kulon qonuni", "o'z-o'zidan tormozlanish"],
        lesson=Lesson(
            physical_problem=(
                "Yuk ko'tarish vinti (domkrat) yukni ko'tarib, qo'yib yuborilganda "
                "o'zi tushib ketmasligi kerak. Bu xususiyat — o'z-o'zidan tormozlanish "
                "— faqat ishqalanish hisobiga mavjud. Agar vint qadamini oshirsak, "
                "ko'tarish osonlashadi, lekin qaysidir chegarada domkrat xavfli bo'lib "
                "qoladi. Bu chegara qayerda?"
            ),
            concepts=[
                c("Quruq ishqalanish (Coulomb friction)", "$F_{ish} \\le f N$ — "
                  "ishqalanish kuchi normal bosimga proporsional va tayanch yuzasiga "
                  "(taxminan) bog'liq emas."),
                c("Chegaraviy muvozanat", "$F_{ish} = f N$ bo'lgan holat — sirpanish "
                  "boshlanish arafasi. Undan oldin $F_{ish} < fN$ va uning qiymati "
                  "muvozanat tenglamasidan topiladi."),
                c("Ishqalanish burchagi va konusi", "$\\tan\\varphi = f$; to'la reaksiya "
                  "har doim normaldan $\\varphi$ dan katta og'maydi — shuning uchun u "
                  "konus ichida yotadi."),
                c("O'z-o'zidan tormozlanish (self-locking)", "Tashqi kuch qanchalik "
                  "katta bo'lsa ham harakat boshlanmaydigan holat: $\\alpha \\le \\varphi$."),
                c("Dumalash qarshiligi", "$M_{dum} = \\delta N$, $\\delta$ — dumalash "
                  "ishqalanish koeffitsienti (uzunlik o'lchamiga ega, mm larda)."),
            ],
            derivation=[
                d("1-qadam. Qiya tekislikdagi jismning muvozanati",
                  r"\sum F_{\parallel} = 0:\; G\sin\alpha - F_{ish} = 0;\qquad "
                  r"\sum F_{\perp} = 0:\; N - G\cos\alpha = 0",
                  "Qiya tekislik bo'ylab va unga perpendikular proyeksiyalar. "
                  "O'qlarni tekislikka bog'lash hisobni soddalashtiradi."),
                d("2-qadam. Ishqalanish shartini qo'llash",
                  r"F_{ish} = G\sin\alpha \le f N = f G\cos\alpha",
                  "Muvozanat tenglamasidan topilgan $F_{ish}$ Kulon shartini "
                  "qanoatlantirishi kerak."),
                d("3-qadam. Muvozanat sharti",
                  r"\boxed{\;\tan\alpha \le f = \tan\varphi \;\Longleftrightarrow\; \alpha \le \varphi\;}",
                  "$G$ qisqardi! Demak muvozanat jism og'irligiga umuman bog'liq emas — "
                  "faqat burchak va ishqalanish koeffitsientiga. Bu natija ko'pchilikni "
                  "hayratda qoldiradi, lekin tajribada aniq tasdiqlanadi."),
                d("4-qadam. Vint birikmaga o'tish",
                  r"\tan\alpha = \frac{P}{\pi d_2},\qquad P\ \text{— vint qadami},\; "
                  r"d_2\ \text{— o'rtacha diametr}",
                  "Vint rezbasini yoyib yuborsak — qiya tekislik hosil bo'ladi. "
                  "Rezba burchagi $\\alpha$ aynan shu formuladan aniqlanadi."),
                d("5-qadam. Vintni burash momenti",
                  r"T = \frac{F d_2}{2}\tan(\alpha + \varphi') ,\qquad \varphi' = \arctan\frac{f}{\cos(\beta/2)}",
                  "Ko'tarish uchun $(\\alpha+\\varphi')$, tushirish uchun "
                  "$(\\alpha-\\varphi')$. Ikkinchisi manfiy bo'lsa — o'z-o'zidan "
                  "tormozlanish mavjud. $\\beta$ — rezba profili burchagi (metrik uchun 60°)."),
            ],
            formula_meaning=(
                "$\\alpha \\le \\varphi$ sharti — mexanikadagi eng amaliy natijalardan "
                "biri. U shuni bildiradi: agar qiyalik burchagi ishqalanish burchagidan "
                "kichik bo'lsa, tizim o'z-o'zidan harakatga kelmaydi, yuk qanchalik og'ir "
                "bo'lishidan qat'i nazar. Domkrat, vintli mahkamlagich, konussimon "
                "birikma — barchasi shu prinsipda ishlaydi. Teskarisi ham to'g'ri: "
                "konveyer yoki tushirish qurilmasi loyihalanayotganda $\\alpha > \\varphi$ "
                "bo'lishi ta'minlanadi."
            ),
            equations=[
                eq(r"F_{ish} \le f N", "Kulon-Amonton ishqalanish qonuni.", "Ishqalanish qonuni"),
                eq(r"\tan\varphi = f", "Ishqalanish burchagi.", "Ishqalanish burchagi"),
                eq(r"\alpha \le \varphi", "O'z-o'zidan tormozlanish sharti.", "Self-locking"),
                eq(r"T = \frac{F d_2}{2}\tan(\alpha+\varphi')", "Vintni burash momenti.",
                   "Vint momenti"),
            ],
            conditions=(
                "Ishqalanish masalasi tenglamalar emas, tengsizliklar tizimi bilan "
                "yechiladi. Ikki savol farqlanadi: (1) 'muvozanat saqlanadimi?' — "
                "$F_{ish}$ ni tenglamadan topib, $fN$ bilan solishtiramiz; (2) "
                "'minimal/maksimal kuch qancha?' — chegaraviy holatni ($F_{ish} = fN$) "
                "olamiz. Ishqalanish yo'nalishi har doim mumkin bo'lgan sirpanishga "
                "qarama-qarshi — bu ishorani to'g'ri qo'yishning kaliti."
            ),
            worked_example=WorkedExample(
                statement=(
                    "Vintli domkrat: rezba trapetsiyasimon, o'rtacha diametr "
                    "$d_2 = 40$ mm, qadam $P = 6$ mm, ishqalanish koeffitsienti "
                    "$f = 0{,}12$, profil burchagi $\\beta = 30°$. Yuk $F = 50$ kN. "
                    "(a) O'z-o'zidan tormozlanadimi? (b) Ko'tarish momenti qancha? "
                    "(c) FIK ni toping."
                ),
                given=[r"d_2 = 40\ \text{mm},\; P = 6\ \text{mm}", r"f = 0{,}12,\; \beta = 30^\circ",
                       r"F = 50\ \text{kN}"],
                steps=[
                    st(r"\tan\alpha = \frac{P}{\pi d_2} = \frac{6}{\pi\cdot 40} = \frac{6}{125{,}66} = 0{,}0477 "
                       r"\Rightarrow \alpha = 2{,}73^\circ",
                       "Rezba ko'tarilish burchagi."),
                    st(r"f' = \frac{f}{\cos(\beta/2)} = \frac{0{,}12}{\cos 15^\circ} = \frac{0{,}12}{0{,}966} = 0{,}1243 "
                       r"\Rightarrow \varphi' = 7{,}08^\circ",
                       "Trapetsiyasimon rezba uchun keltirilgan ishqalanish burchagi: "
                       "profil qiyaligi normal bosimni oshiradi."),
                    st(r"\alpha = 2{,}73^\circ < \varphi' = 7{,}08^\circ \;\Rightarrow\; "
                       r"\text{o'z-o'zidan tormozlanadi} \;\checkmark",
                       "Zaxira yetarli: burchaklar nisbati 2,6 marta."),
                    st(r"T = \frac{F d_2}{2}\tan(\alpha+\varphi') = \frac{50\,000\cdot 0{,}04}{2}\tan(9{,}81^\circ)",
                       "Ko'tarish momenti formulasi."),
                    st(r"T = 1000\cdot 0{,}1729 = 172{,}9\ \text{N·m}",
                       "Burash momenti. 0,5 m dastali kalit uchun 346 N kuch kerak."),
                    st(r"\eta = \frac{\tan\alpha}{\tan(\alpha+\varphi')} = \frac{0{,}0477}{0{,}1729} = 0{,}276",
                       "FIK atigi 27,6 % — o'z-o'zidan tormozlanuvchi vintlar uchun "
                       "$\\eta < 0{,}5$ har doim o'rinli."),
                ],
                answer=(
                    "(a) Ha, $\\alpha = 2{,}73° < \\varphi' = 7{,}08°$; "
                    "(b) $T = 172{,}9$ N·m; (c) $\\eta = 27{,}6$ %."
                ),
                engineering_note=(
                    "FIK va xavfsizlik bir-biriga qarama-qarshi: $\\eta > 0{,}5$ bo'lishi "
                    "uchun $\\alpha > \\varphi'$ kerak, lekin bu o'z-o'zidan "
                    "tormozlanishni yo'qotadi. Shuning uchun yuk ko'tarish "
                    "mexanizmlarida past FIK ataylab qabul qilinadi, samaradorlik kerak "
                    "bo'lganda esa (masalan, sharikli vint uzatma) alohida tormoz o'rnatiladi."
                ),
            ),
            computation=Computation(
                caption=(
                    "Vint parametrlarini o'zgartirib, o'z-o'zidan tormozlanish chegarasi "
                    "va FIK orasidagi kompromissni tadqiq qiling."
                ),
                code='''"""Ishqalanish: qiya tekislik, vint birikma va muvozanat sohasi."""
import numpy as np
from labkit import PARAMS, note, series, table, value

d2 = float(PARAMS.get("d2", 0.040))    # o'rtacha diametr, m
P = float(PARAMS.get("P", 0.006))      # qadam, m
f = float(PARAMS.get("f", 0.12))       # ishqalanish koeffitsienti
beta = float(PARAMS.get("beta", 30.0)) # profil burchagi, deg
F = float(PARAMS.get("F", 50.0))       # yuk, kN

alpha = np.arctan(P/(np.pi*d2))
f_pr = f/np.cos(np.radians(beta)/2)
phi_pr = np.arctan(f_pr)

value("Rezba burchagi α", np.degrees(alpha), "deg")
value("Ishqalanish burchagi φ'", np.degrees(phi_pr), "deg")
value("Ko'tarish momenti T", F*1000*d2/2*np.tan(alpha+phi_pr), "N·m")
value("Tushirish momenti", F*1000*d2/2*np.tan(alpha-phi_pr), "N·m")
value("FIK η", np.tan(alpha)/np.tan(alpha+phi_pr), "—")
note("O'z-o'zidan tormozlanadi" if alpha < phi_pr else
     "DIQQAT: o'z-o'zidan tormozlanmaydi — yuk tushib ketishi mumkin!")

# Qadamning FIK va xavfsizlikka ta'siri
PP = np.linspace(0.001, 0.030, 200)
al = np.arctan(PP/(np.pi*d2))
eta = np.tan(al)/np.tan(al + phi_pr)
series("FIK η(P)", (PP*1000).tolist(), eta.tolist(), xlabel="Qadam P, mm", ylabel="η")
series("Rezba burchagi α(P)", (PP*1000).tolist(), np.degrees(al).tolist(),
       xlabel="Qadam P, mm", ylabel="α, deg")

P_crit = np.pi*d2*np.tan(phi_pr)
note(f"Kritik qadam (α = φ'): P = {P_crit*1000:.2f} mm. "
     f"Undan katta qadamda o'z-o'zidan tormozlanish yo'qoladi.")

# Qiya tekislik: muvozanat sohasi
angles = np.linspace(0, 45, 100)
f_required = np.tan(np.radians(angles))
series("Muvozanat uchun kerakli f(α)", angles.tolist(), f_required.tolist(),
       xlabel="Qiyalik burchagi α, deg", ylabel="f_min")

table("Materiallar uchun tipik qiymatlar",
      ["Juftlik", "f", "φ, deg", "Maks. qiyalik, deg"],
      [["Po'lat–po'lat (quruq)", 0.15, float(np.degrees(np.arctan(0.15))), 8.5],
       ["Po'lat–po'lat (moylangan)", 0.08, float(np.degrees(np.arctan(0.08))), 4.6],
       ["Po'lat–bronza", 0.10, float(np.degrees(np.arctan(0.10))), 5.7],
       ["Rezina–asfalt", 0.70, float(np.degrees(np.arctan(0.70))), 35.0]])
''',
                parameters=[
                    p("d2", "O'rtacha diametr d₂", 0.010, 0.120, 0.040, 0.002, "m"),
                    p("P", "Rezba qadami P", 0.001, 0.030, 0.006, 0.001, "m"),
                    p("f", "Ishqalanish koeff. f", 0.02, 0.40, 0.12, 0.01, "—"),
                    p("beta", "Profil burchagi β", 0.0, 60.0, 30.0, 5.0, "deg"),
                    p("F", "Yuk F", 1.0, 500.0, 50.0, 5.0, "kN"),
                ],
                expected_output="α = 2,73°, φ' = 7,08°, T ≈ 173 N·m, η ≈ 0,276",
            ),
            visualization=vis(
                "Ishqalanish konusi va muvozanat sohasi",
                "React/SVG",
                "Qiya tekislikdagi jism, normal reaksiya, ishqalanish kuchi va to'la "
                "reaksiya; ishqalanish konusi shtrixlangan soha sifatida. Yonida "
                "$(\\alpha, f)$ tekisligida muvozanat sohasi chegarasi $f = \\tan\\alpha$.",
                "React/SVG: ishqalanish konusi — ikki chiziq bilan chegaralangan sektor, "
                "to'la reaksiya vektori uning ichida harakatlanadi. Interaktiv slider "
                "bilan $\\alpha$ ni oshirganda vektorning konus chegarasiga yetishi "
                "va sirpanish boshlanishi ko'rsatiladi — bu tengsizlik shartining eng "
                "tushunarli geometrik talqini.",
            ),
            interpretation=(
                "FIK grafigi monoton o'sadi, lekin $P_{crit}$ nuqtasida o'z-o'zidan "
                "tormozlanish yo'qoladi. Loyihachi bu grafikda ishlash nuqtasini "
                "tanlaydi: xavfsizlik zaxirasi bilan chap tomonda (past FIK) yoki "
                "samaradorlik uchun o'ng tomonda (tormoz bilan). Jadvaldagi materiallar "
                "qiymatlari esa qanday qiyalikda konveyer yoki panduslar loyihalash "
                "mumkinligini bevosita ko'rsatadi."
            ),
            common_mistakes=[
                "$F_{ish} = fN$ ni har doim yozish. To'g'risi: $F_{ish} \\le fN$; "
                "tenglik faqat chegaraviy holatda.",
                "Ishqalanish yo'nalishini tasodifiy tanlash. U mumkin bo'lgan "
                "sirpanishga qarama-qarshi bo'lishi shart.",
                "Trapetsiyasimon rezbada $f$ ni to'g'ridan-to'g'ri ishlatish — "
                "$f' = f/\\cos(\\beta/2)$ keltirilgan koeffitsientni hisobga olish kerak.",
                "Statik va kinetik ishqalanish koeffitsientlarini farqlamaslik "
                "($f_s > f_k$ odatda 20–30 % ga).",
                "Muvozanat jism og'irligiga bog'liq deb o'ylash — qiya tekislik masalasida "
                "$G$ qisqaradi.",
            ],
            quiz=[
                q("Nima uchun qiya tekislikdagi muvozanat sharti jism og'irligiga "
                  "bog'liq emas?",
                  "Chunki ham siljituvchi kuch ($G\\sin\\alpha$), ham maksimal ishqalanish "
                  "($fG\\cos\\alpha$) $G$ ga proporsional — nisbatda u qisqaradi.",
                  "konseptual"),
                q("Ishqalanish konusi nimani anglatadi?",
                  "To'la reaksiya vektorining mumkin bo'lgan yo'nalishlari sohasini. "
                  "Vektor konus ichida bo'lsa muvozanat bor, chegarasida — sirpanish "
                  "boshlanadi.", "konseptual"),
                q("$f = 0{,}25$. Maksimal qiyalik burchagi qancha?",
                  "$\\alpha_{max} = \\arctan 0{,}25 = 14{,}0°$.", "hisob"),
                q("Vint qadamini 2 marta oshirsak, FIK va xavfsizlik qanday o'zgaradi?",
                  "$\\alpha$ taxminan 2 marta ortadi, FIK oshadi, lekin $\\alpha$ "
                  "$\\varphi'$ dan oshib ketsa o'z-o'zidan tormozlanish yo'qoladi.",
                  "talqin"),
                q("Kodda `f_pr = f/np.cos(np.radians(beta)/2)` nimani hisobga oladi?",
                  "Trapetsiyasimon rezbada normal bosim profil qiyaligi tufayli "
                  "$1/\\cos(\\beta/2)$ marta ortadi, demak ishqalanish ham shuncha ortadi.",
                  "kod"),
                q("Dumalash qarshiligi nima uchun ishqalanishdan ancha kichik?",
                  "Chunki u sirpanishdan emas, kontakt zonasidagi deformatsiyaning "
                  "assimetriyasidan kelib chiqadi: $M = \\delta N$, va $\\delta$ odatda "
                  "0,05–0,5 mm. Shuning uchun g'ildirak ixtiro qilingan.", "talqin"),
            ],
            bridge_to_next=(
                "Dinamika va statikaning asosiy apparatini o'zlashtirdik. Endi "
                "tenglamalarni har safar integrallash o'rniga umumiy qonunlardan — "
                "impuls va energiya saqlanishidan — foydalanishni o'rganamiz. Bu "
                "ko'p masalani bir necha qatorda yechish imkonini beradi."
            ),
            research_extension=(
                "Stick-slip (yopishib-sirpanish) tebranishini modellashtiring: "
                "prujina orqali tortilayotgan jism, statik ishqalanish kinetikdan "
                "katta. `solve_ivp` bilan hodisa (event) mexanizmidan foydalanib "
                "yopishish va sirpanish rejimlarini almashtiring. Bu effekt "
                "tormozlarning g'ichirlashi, mashina stanоklarining titrashi va hatto "
                "zilzila mexanizmining sodda modelidir."
            ),
        ),
    ),
]
