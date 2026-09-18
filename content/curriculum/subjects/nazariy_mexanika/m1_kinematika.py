"""NM / 1-modul: Matematik tayanch va kinematika (nm-01 … nm-06)."""

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
M = "nm-m1"

TOPICS = [
    Topic(
        id="nm-01",
        subject_id=S,
        module_id=M,
        order=1,
        title="Vektor algebrasi va mexanikada koordinata sistemasini tanlash",
        description=(
            "Mexanikaning butun tili — vektorlar. Skalyar va vektor ko'paytma, "
            "proyeksiyalar va koordinata sistemasini maqsadga muvofiq tanlash "
            "malakasi shakllantiriladi."
        ),
        learning_objective=(
            "Vektor amallarini mexanik kattaliklar (kuch, moment, tezlik) uchun "
            "qo'llay olish va masala geometriyasiga mos koordinata sistemasini "
            "asoslab tanlash."
        ),
        prerequisites=[],
        mathematical_core=(
            "Vektor fazo, bazis, skalyar ko'paytma $\\mathbf{a}\\cdot\\mathbf{b}$, "
            "vektor ko'paytma $\\mathbf{a}\\times\\mathbf{b}$, aralash ko'paytma, "
            "ortogonal almashtirish matritsasi."
        ),
        engineering_application=(
            "Fazoviy fermada sterjen kuchlarini proyeksiyalash, bolt birikmasiga "
            "ta'sir etuvchi momentni hisoblash, kran strelasi geometriyasi."
        ),
        computational_component=(
            "NumPy bilan vektor amallari, burchak hisobi va koordinata "
            "almashtirish matritsasini qurish."
        ),
        visualization_component=(
            "3D koordinata sistemasi, vektorlar va ularning proyeksiyalari; "
            "vektor ko'paytmaning o'ng vint qoidasi."
        ),
        research_extension=(
            "Turli koordinata sistemalarida (Dekart, silindrik, sferik) bir xil "
            "masalaning shartlanganligi va yozuv ixchamligini taqqoslang: qaysi "
            "tanlov tenglamalar sonini kamaytiradi?"
        ),
        difficulty="kirish",
        previous_link=(
            "Bu kursning birinchi mavzusi. U butun platformaning notation'ini "
            "(belgilar tizimini) o'rnatadi: barcha 150 mavzuda $x, y, z$ — "
            "koordinatalar, $\\mathbf{F}$ — kuch, $\\mathbf{M}_O$ — moment."
        ),
        next_topic="nm-02",
        estimated_minutes=80,
        tags=["vektor", "koordinata", "notation"],
        lesson=Lesson(
            physical_problem=(
                "Kran strelasiga uchta trosdan kuch ta'sir qiladi. Ular fazoda turli "
                "yo'nalishlarda. Konstruktor ikki savolga javob berishi kerak: bu "
                "kuchlarning natijaviysi qanday va ular strelani mahkamlash nuqtasi "
                "atrofida qanchalik burashga urinadi? Ikkala savol ham vektor "
                "amallarisiz yechilmaydi — chunki kuch faqat kattalik emas, balki "
                "yo'nalish va ta'sir chizig'i bilan aniqlanadigan obyekt."
            ),
            concepts=[
                c("Vektor (vector)",
                  "Kattalik, yo'nalish va (mexanikada) ta'sir chizig'i bilan aniqlanuvchi "
                  "obyekt. Erkin, sirpanuvchi va bog'langan vektorlar farqlanadi: kuch — "
                  "sirpanuvchi, moment — erkin vektor."),
                c("Skalyar ko'paytma (dot product)",
                  "$\\mathbf{a}\\cdot\\mathbf{b}=|\\mathbf{a}||\\mathbf{b}|\\cos\\alpha$ — "
                  "bir vektorning ikkinchisi yo'nalishidagi proyeksiyasini beradi. Ish "
                  "hisobining asosi."),
                c("Vektor ko'paytma (cross product)",
                  "$\\mathbf{a}\\times\\mathbf{b}$ — ikkala vektorga perpendikular, moduli "
                  "ular yasagan parallelogramm yuzasiga teng vektor. Moment hisobining asosi."),
                c("O'ng vintli sistema (right-handed system)",
                  "$\\mathbf{i}\\times\\mathbf{j}=\\mathbf{k}$ shartini qanoatlantiruvchi "
                  "bazis. Platformada barcha koordinata sistemalari o'ng vintli."),
                c("Yo'naltiruvchi kosinuslar",
                  "Vektorning koordinata o'qlari bilan tashkil qilgan burchaklari "
                  "kosinuslari; ular birlik vektorning komponentalari bo'ladi."),
            ],
            derivation=[
                d("1-qadam. Vektorni bazisda yoyish",
                  r"\mathbf{F} = F_x\mathbf{i} + F_y\mathbf{j} + F_z\mathbf{k}",
                  "Har qanday vektor o'zaro ortogonal birlik vektorlar bo'yicha yagona "
                  "usulda yoyiladi. Komponentalar — proyeksiyalar: $F_x=\\mathbf{F}\\cdot\\mathbf{i}$."),
                d("2-qadam. Modul va yo'naltiruvchi kosinuslar",
                  r"|\mathbf{F}| = \sqrt{F_x^2+F_y^2+F_z^2}, \qquad "
                  r"\cos\alpha = \frac{F_x}{|\mathbf{F}|},\;\cos\beta = \frac{F_y}{|\mathbf{F}|},"
                  r"\;\cos\gamma = \frac{F_z}{|\mathbf{F}|}",
                  "Pifagor teoremasining fazoviy umumlashmasi. Yo'naltiruvchi kosinuslar "
                  "uchun $\\cos^2\\alpha+\\cos^2\\beta+\\cos^2\\gamma=1$ ayniyati o'rinli — "
                  "bu hisobni tekshirishning eng tez usuli."),
                d("3-qadam. Momentni vektor ko'paytma sifatida aniqlash",
                  r"\mathbf{M}_O = \mathbf{r}\times\mathbf{F} = "
                  r"\begin{vmatrix}\mathbf{i}&\mathbf{j}&\mathbf{k}\\ x&y&z\\ F_x&F_y&F_z\end{vmatrix}",
                  "$\\mathbf{r}$ — O nuqtadan kuch qo'yilgan nuqtaga o'tkazilgan vektor. "
                  "Determinantni yoyish momentning uchta komponentasini beradi."),
                d("4-qadam. Momentning moduli va yelka tushunchasi",
                  r"|\mathbf{M}_O| = |\mathbf{r}||\mathbf{F}|\sin\theta = F\,d,\qquad d = |\mathbf{r}|\sin\theta",
                  "$d$ — O nuqtadan kuchning ta'sir chizig'igacha bo'lgan eng qisqa masofa, "
                  "ya'ni yelka. Demak vektor ta'rif maktabdagi $M=F\\,d$ ta'rifini o'z "
                  "ichiga oladi va uni fazoga umumlashtiradi."),
                d("5-qadam. Koordinata sistemasini burish",
                  r"\{\mathbf{F}\}' = [Q]\{\mathbf{F}\},\qquad Q_{ij} = \mathbf{e}'_i\cdot\mathbf{e}_j,\qquad [Q]^{-1}=[Q]^{T}",
                  "Ortogonal matritsa $[Q]$ komponentalarni yangi bazisga o'tkazadi. "
                  "Vektorning o'zi o'zgarmaydi — faqat uning raqamli tavsifi o'zgaradi. "
                  "Aynan shu xossa keyinchalik kuchlanish tenzori uchun umumlashtiriladi (tmm-02)."),
            ],
            formula_meaning=(
                "$\\mathbf{a}\\cdot\\mathbf{b}$ — 'qanchalik bir yo'nalishda' degan savolga "
                "javob (shuning uchun ish $A=\\mathbf{F}\\cdot\\mathbf{s}$: faqat ko'chish "
                "yo'nalishidagi kuch ish bajaradi). $\\mathbf{a}\\times\\mathbf{b}$ — "
                "'qanchalik burchak ostida' degan savolga javob (shuning uchun moment "
                "$\\mathbf{r}\\times\\mathbf{F}$: kuch ta'sir chizig'i markazdan qanchalik "
                "uzoq o'tsa, burash effekti shuncha katta). Ortogonal matritsa $[Q]$ esa "
                "fizik hodisaning kuzatuvchi tanlagan o'qlarga bog'liq emasligini ifodalaydi."
            ),
            equations=[
                eq(r"\mathbf{a}\cdot\mathbf{b} = a_xb_x+a_yb_y+a_zb_z = |\mathbf{a}||\mathbf{b}|\cos\alpha",
                   "Skalyar ko'paytma — proyeksiya va ish hisobining asosi.", "Skalyar ko'paytma"),
                eq(r"\mathbf{a}\times\mathbf{b} = (a_yb_z-a_zb_y)\mathbf{i} - (a_xb_z-a_zb_x)\mathbf{j} + (a_xb_y-a_yb_x)\mathbf{k}",
                   "Vektor ko'paytma — moment va burchak tezligi hisobining asosi.", "Vektor ko'paytma"),
                eq(r"\mathbf{M}_O = \mathbf{r}\times\mathbf{F}", "Kuchning nuqtaga nisbatan momenti.",
                   "Moment ta'rifi"),
                eq(r"M_z = \mathbf{k}\cdot(\mathbf{r}\times\mathbf{F})",
                   "Kuchning o'qqa nisbatan momenti — aralash ko'paytma orqali.", "O'qqa nisbatan moment"),
            ],
            conditions=(
                "Koordinata boshi O va o'qlar yo'nalishi masala sharti emas, balki "
                "hisoblovchining tanlovi. Amaliy qoida: boshni noma'lum reaksiyalar "
                "ko'p to'planган nuqtaga qo'ying (ular momentga kirmaydi), bitta o'qni "
                "esa asosiy geometrik o'q bo'ylab yo'naltiring. Bu tanlov yechimni "
                "o'zgartirmaydi, lekin tenglamalarni sezilarli soddalashtiradi."
            ),
            worked_example=WorkedExample(
                statement=(
                    "Kran strelasining A(2; 0; 3) m nuqtasiga trosdan "
                    "$\\mathbf{F} = (-4;\\,6;\\,-12)$ kN kuch ta'sir qiladi. Koordinata "
                    "boshi O — strelaning mahkamlanish sharniri. Kuchning moduli, "
                    "yo'naltiruvchi kosinuslari, O nuqtaga nisbatan momenti va z o'qiga "
                    "nisbatan momenti topilsin."
                ),
                given=[
                    r"\mathbf{r} = (2;\,0;\,3)\ \text{m}",
                    r"\mathbf{F} = (-4;\,6;\,-12)\ \text{kN}",
                ],
                steps=[
                    st(r"|\mathbf{F}| = \sqrt{(-4)^2+6^2+(-12)^2} = \sqrt{16+36+144} = \sqrt{196} = 14\ \text{kN}",
                       "Avval kuch modulini topamiz."),
                    st(r"\cos\alpha = \frac{-4}{14} = -0{,}286,\quad \cos\beta = \frac{6}{14} = 0{,}429,\quad \cos\gamma = \frac{-12}{14} = -0{,}857",
                       "Yo'naltiruvchi kosinuslar. Tekshirish: $0{,}286^2+0{,}429^2+0{,}857^2 = 1{,}000$ ✓"),
                    st(r"\mathbf{M}_O = \begin{vmatrix}\mathbf{i}&\mathbf{j}&\mathbf{k}\\ 2&0&3\\ -4&6&-12\end{vmatrix}",
                       "Moment determinantini tuzamiz."),
                    st(r"M_x = 0\cdot(-12) - 3\cdot 6 = -18;\quad M_y = -\big(2\cdot(-12) - 3\cdot(-4)\big) = 12;\quad M_z = 2\cdot 6 - 0\cdot(-4) = 12",
                       "Determinantni yoyamiz (kN·m)."),
                    st(r"|\mathbf{M}_O| = \sqrt{18^2+12^2+12^2} = \sqrt{324+144+144} = \sqrt{612} \approx 24{,}7\ \text{kN·m}",
                       "Moment moduli."),
                    st(r"d = \frac{|\mathbf{M}_O|}{|\mathbf{F}|} = \frac{24{,}7}{14} \approx 1{,}77\ \text{m}",
                       "Kuch ta'sir chizig'ining O dan yelkasi."),
                ],
                answer=(
                    "$|\\mathbf{F}| = 14$ kN; $\\mathbf{M}_O = (-18;\\,12;\\,12)$ kN·m; "
                    "$|\\mathbf{M}_O| \\approx 24{,}7$ kN·m; $M_z = +12$ kN·m; yelka $d\\approx 1{,}77$ m."
                ),
                engineering_note=(
                    "$M_z > 0$ — strela z o'qi atrofida soat strelkasiga teskari burilishga "
                    "intiladi; aynan shu komponenta aylanish mexanizmi tormozini tanlashda "
                    "hisobga olinadi. $M_x$ manfiy — bu ag'darish momenti va u krandagi "
                    "protivoves hisobiga kiradi."
                ),
            ),
            computation=Computation(
                caption=(
                    "Vektor amallari kalkulyatori: kuch va joy vektorini o'zgartiring, "
                    "moment, yelka va yo'naltiruvchi kosinuslar qayta hisoblanadi."
                ),
                code='''"""Fazoviy kuchning momenti va geometrik tavsiflari."""
import numpy as np
from labkit import PARAMS, note, series, table, value

# --- Parametrlar (Interactive Lab sliderlaridan keladi) ---
rx = float(PARAMS.get("rx", 2.0))      # m
rz = float(PARAMS.get("rz", 3.0))      # m
Fy = float(PARAMS.get("Fy", 6.0))      # kN

r = np.array([rx, 0.0, rz])            # joy vektori, m
F = np.array([-4.0, Fy, -12.0])        # kuch vektori, kN

F_mod = np.linalg.norm(F)
M = np.cross(r, F)                     # moment, kN*m
M_mod = np.linalg.norm(M)
cosines = F / F_mod
arm = M_mod / F_mod if F_mod > 0 else 0.0

value("|F|", F_mod, "kN")
value("|M_O|", M_mod, "kN·m")
value("M_z", M[2], "kN·m")
value("Yelka d", arm, "m")

table("Yo'naltiruvchi kosinuslar",
      ["O'q", "Komponenta, kN", "cos"],
      [["x", F[0], cosines[0]], ["y", F[1], cosines[1]], ["z", F[2], cosines[2]]])

# Nazorat ayniyati: cos^2 yig'indisi 1 ga teng bo'lishi shart
note(f"Tekshirish: sum(cos^2) = {np.sum(cosines**2):.6f} (1.000000 bo'lishi kerak)")

# Yelka strelaning uzunligiga qanday bog'liq?
L = np.linspace(0.5, 6.0, 60)
arms = [np.linalg.norm(np.cross(np.array([Li, 0.0, rz]), F)) / F_mod for Li in L]
series("Yelka d(rx)", L.tolist(), arms, xlabel="rx, m", ylabel="d, m")
''',
                parameters=[
                    p("rx", "r_x — strela uzunligi", 0.5, 6.0, 2.0, 0.1, "m"),
                    p("rz", "r_z — balandlik", 0.0, 6.0, 3.0, 0.1, "m"),
                    p("Fy", "F_y — kuchning y komponentasi", -15.0, 15.0, 6.0, 0.5, "kN"),
                ],
                expected_output="|F| = 14 kN, |M_O| ≈ 24,74 kN·m, M_z = 12 kN·m, d ≈ 1,767 m",
            ),
            visualization=vis(
                "3D vektor diagrammasi va o'ng vint qoidasi",
                "React/SVG + Matplotlib",
                "O nuqtadan chiquvchi $\\mathbf{r}$, uning uchidagi $\\mathbf{F}$ va ularga "
                "perpendikular $\\mathbf{M}_O$; $\\mathbf{r}$ va $\\mathbf{F}$ yasagan "
                "parallelogramm shtrixlanadi, yelka $d$ punktir bilan ko'rsatiladi.",
                "React/SVG: izometrik proyeksiya (x→(-0,5; 0,5), y→(1; 0), z→(0; -1) "
                "birlik vektorlari) yetarli, chunki interaktiv burish shart emas. "
                "Matplotlib'da `ax.quiver` bilan haqiqiy 3D chizma; Manim'da esa o'ng "
                "vint qoidasini animatsiya qilish pedagogik jihatdan eng foydali.",
            ),
            interpretation=(
                "Natijadagi eng muhim son — yelka $d = |\\mathbf{M}_O|/|\\mathbf{F}|$. U "
                "kuchning kattaligidan mustaqil ravishda geometriyani tavsiflaydi: "
                "trosni mahkamlash nuqtasini surish orqali momentni kamaytirish mumkin, "
                "kuchni kamaytirmasdan ham. Grafikdan ko'rinadiki, $r_x$ ortganda yelka "
                "chiziqli emas, balki egri o'sadi — chunki $\\mathbf{r}$ va $\\mathbf{F}$ "
                "orasidagi burchak ham o'zgaradi."
            ),
            common_mistakes=[
                "Vektor ko'paytma tartibini almashtirib yuborish: "
                "$\\mathbf{F}\\times\\mathbf{r} = -\\mathbf{r}\\times\\mathbf{F}$ — ishora "
                "teskari bo'lib, ag'darish yo'nalishi noto'g'ri chiqadi.",
                "$\\mathbf{r}$ ni kuch qo'yilgan nuqtadan moment markaziga qarab olish "
                "(teskari yo'nalish). To'g'risi: markazdan kuch nuqtasiga.",
                "Yelkani $|\\mathbf{r}|$ deb olish. Yelka — perpendikular masofa, "
                "$d = |\\mathbf{r}|\\sin\\theta$, va u faqat $\\theta = 90°$ da $|\\mathbf{r}|$ ga teng.",
                "Kuch ta'sir chizig'i moment markazidan o'tsa ham nolga teng bo'lmagan "
                "moment kutish. Bunday holda $\\sin\\theta = 0$ va $\\mathbf{M}_O = 0$.",
                "Birliklarni aralashtirish: kN va N, m va mm. Platformada barcha hisob "
                "SI da yuritiladi, natija esa qulay birlikka keltiriladi.",
            ],
            quiz=[
                q("Nima uchun ish skalyar ko'paytma orqali, moment esa vektor ko'paytma "
                  "orqali aniqlanadi?",
                  "Ish — energiya, ya'ni skalyar kattalik va u faqat ko'chish yo'nalishidagi "
                  "kuch ulushiga bog'liq ($\\cos$). Moment esa aylanish o'qi yo'nalishiga ega "
                  "bo'lgan vektor va u kuchning perpendikular ulushiga bog'liq ($\\sin$).",
                  "konseptual"),
                q("$\\mathbf{a}\\times\\mathbf{b} = 0$, lekin $\\mathbf{a}\\neq 0$ va "
                  "$\\mathbf{b}\\neq 0$. Bundan qanday geometrik xulosa kelib chiqadi?",
                  "Vektorlar kollinear (parallel yoki antiparallel), chunki $\\sin\\theta = 0$.",
                  "konseptual"),
                q("$\\mathbf{F} = (3; -4; 0)$ N va $\\mathbf{r} = (0; 0; 2)$ m bo'lsa, "
                  "$\\mathbf{M}_O$ ni hisoblang.",
                  "$\\mathbf{M}_O = \\mathbf{r}\\times\\mathbf{F} = (0\\cdot 0 - 2\\cdot(-4);\\ "
                  "2\\cdot 3 - 0\\cdot 0;\\ 0) = (8;\\,6;\\,0)$ N·m, $|\\mathbf{M}_O| = 10$ N·m.",
                  "hisob"),
                q("Koordinata sistemasini 30° ga bursak, kuch moduli o'zgaradimi? "
                  "Komponentalari-chi?",
                  "Modul o'zgarmaydi — u invariant. Komponentalar o'zgaradi, chunki ular "
                  "bazisga bog'liq: $\\{F\\}' = [Q]\\{F\\}$, va $[Q]$ ortogonal bo'lgani uchun "
                  "$|\\{F\\}'| = |\\{F\\}|$.",
                  "konseptual"),
                q("Kod misolida `np.sum(cosines**2)` nima uchun chiqariladi?",
                  "Bu nazorat ayniyati: yo'naltiruvchi kosinuslar kvadratlari yig'indisi "
                  "aynan 1 ga teng. 1 dan farq qilsa — normalashda yoki kiritishda xato bor.",
                  "kod"),
                q("Moment markazini kuch ta'sir chizig'idagi istalgan nuqtaga ko'chirsak, "
                  "moment qanday o'zgaradi?",
                  "Nolga aylanadi, chunki bu holda $\\mathbf{r}$ va $\\mathbf{F}$ kollinear "
                  "bo'ladi. Shuning uchun moment markazini kuch chizig'ida tanlash "
                  "noma'lumlarni yo'qotishning standart usuli.",
                  "talqin"),
            ],
            bridge_to_next=(
                "Endi bizda kattaliklarni yozadigan til bor. Keyingi mavzuda bu tilni "
                "vaqtga bog'laymiz: joy vektori $\\mathbf{r}(t)$ funksiyaga aylanadi va "
                "uni differensiallash tezlik hamda tezlanishni beradi."
            ),
            research_extension=(
                "Kichik tadqiqot: fazoviy ferma tugunidagi 6–8 ta sterjen uchun kuch "
                "proyeksiyalarini avtomatik hisoblaydigan skript yozing. So'ngra "
                "koordinata o'qlarini turlicha burib, hosil bo'lgan chiziqli tenglamalar "
                "sistemasining shartlanganlik soni (condition number) qanday o'zgarishini "
                "o'lchang. Bu — su-02 dagi shartlanganlik mavzusiga real kirish nuqtasi."
            ),
            manim=manim(
                scene="VectorMomentScene",
                module="manim/scenes/nm_vectors.py",
                title="Vektor ko'paytma va moment",
                summary="r va F vektorlari, ular yasagan parallelogramm, yelka va hosil "
                        "bo'luvchi M vektori o'ng vint qoidasi bo'yicha animatsiya qilinadi.",
            ),
        ),
    ),
    Topic(
        id="nm-02",
        subject_id=S,
        module_id=M,
        order=2,
        title="Moddiy nuqta kinematikasi: joy vektori, tezlik va tezlanish",
        description=(
            "Harakatning vektor, koordinata va parametrik tavsiflari. "
            "Differensiallash orqali tezlik va tezlanishni olish."
        ),
        learning_objective=(
            "Berilgan $\\mathbf{r}(t)$ bo'yicha tezlik va tezlanishni topish, teskarisiga "
            "— tezlanishdan boshlang'ich shartlar yordamida harakat qonunini tiklash."
        ),
        prerequisites=["nm-01"],
        mathematical_core=(
            "Vektor funksiyani differensiallash, hosila geometrik ma'nosi, "
            "aniqmas integral va boshlang'ich shartlar."
        ),
        engineering_application=(
            "Manipulyator uchining traektoriyasi, avtomobil sinov siklidagi tezlanish "
            "profili, snaryad ballistikasi."
        ),
        computational_component=(
            "SymPy bilan simvolik differensiallash va NumPy bilan traektoriyani "
            "sonli qurish; sonli hosila bilan taqqoslash."
        ),
        visualization_component=(
            "Traektoriya egri chizig'i va unga urinma tezlik vektori, turli "
            "$t$ larda tezlanish vektori."
        ),
        research_extension=(
            "Traektoriyani real o'lchov (masalan, video-treking) ma'lumotlaridan "
            "tiklashda sonli differensiallash shovqinni kuchaytiradi. Silliqlash "
            "(Savitzky–Golay) filtri qanday yordam berishini tekshiring."
        ),
        difficulty="kirish",
        previous_link=(
            "nm-01 da vektorni bazisda yozishni o'rgandik. Endi uning komponentalari "
            "vaqtning funksiyasi bo'ladi: $\\mathbf{r}(t) = x(t)\\mathbf{i}+y(t)\\mathbf{j}+z(t)\\mathbf{k}$."
        ),
        next_topic="nm-03",
        estimated_minutes=85,
        tags=["kinematika", "hosila", "traektoriya"],
        lesson=Lesson(
            physical_problem=(
                "Sanoat robotining ushlagichi A nuqtadan B nuqtaga borishi kerak. "
                "Dasturchi unga vaqt bo'yicha koordinatalar beradi. Lekin muhandisni "
                "boshqa savol qiziqtiradi: shu harakatda ushlagich qanday tezlanish "
                "oladi? Chunki tezlanish $\\times$ massa = inersiya kuchi, va aynan u "
                "yukni qo'ldan chiqarib yuborishi yoki reduktorni buzishi mumkin."
            ),
            concepts=[
                c("Harakat qonuni", "Vaqtga bog'liq joy vektori $\\mathbf{r}(t)$ — "
                  "harakat haqidagi to'liq ma'lumot."),
                c("Traektoriya", "Nuqtaning fazodagi geometrik izi. Harakat qonunidan "
                  "vaqtni yo'qotish orqali olinadi."),
                c("Tezlik (velocity)", "$\\mathbf{v} = d\\mathbf{r}/dt$ — har doim "
                  "traektoriyaga urinma bo'ylab yo'nalgan."),
                c("Tezlanish (acceleration)", "$\\mathbf{a} = d\\mathbf{v}/dt = d^2\\mathbf{r}/dt^2$ "
                  "— traektoriyaning botiq tomoniga qarab yo'nalgan."),
                c("Godograf", "Tezlik vektori uchlarining geometrik o'rni; uning "
                  "urinmasi tezlanish yo'nalishini beradi."),
            ],
            derivation=[
                d("1-qadam. Tezlikni limit orqali aniqlash",
                  r"\mathbf{v}(t) = \lim_{\Delta t\to 0}\frac{\mathbf{r}(t+\Delta t)-\mathbf{r}(t)}{\Delta t} = \frac{d\mathbf{r}}{dt}",
                  "Vatar vektori $\\Delta\\mathbf{r}$ limitда urinmaga aylanadi — shuning "
                  "uchun tezlik har doim traektoriyaga urinma."),
                d("2-qadam. Dekart komponentalariga o'tish",
                  r"\mathbf{v} = \dot{x}\mathbf{i} + \dot{y}\mathbf{j} + \dot{z}\mathbf{k},\qquad "
                  r"v = \sqrt{\dot{x}^2+\dot{y}^2+\dot{z}^2}",
                  "Dekart bazisi vaqt bo'yicha o'zgarmagani uchun ($\\dot{\\mathbf{i}}=0$) "
                  "differensiallash faqat komponentalarga tegadi. Bu qulaylik egri chiziqli "
                  "koordinatalarda yo'qoladi (nm-03)."),
                d("3-qadam. Tezlanish",
                  r"\mathbf{a} = \frac{d\mathbf{v}}{dt} = \ddot{x}\mathbf{i}+\ddot{y}\mathbf{j}+\ddot{z}\mathbf{k}",
                  "Ikkinchi hosila. E'tibor bering: $|\\mathbf{a}| \\neq d|\\mathbf{v}|/dt$ — "
                  "modulning hosilasi tezlanish moduliga teng emas (aylanma harakatda "
                  "tezlik moduli o'zgarmasa ham tezlanish bor)."),
                d("4-qadam. Teskari masala: integrallash",
                  r"\mathbf{v}(t) = \mathbf{v}_0 + \int_0^t \mathbf{a}\,d\tau,\qquad "
                  r"\mathbf{r}(t) = \mathbf{r}_0 + \int_0^t \mathbf{v}\,d\tau",
                  "Ikki marta integrallash ikkita vektor integrallash doimiysini beradi — "
                  "ular boshlang'ich shartlar $\\mathbf{r}_0, \\mathbf{v}_0$ dan topiladi. "
                  "Fazoda bu 6 ta skalyar shart."),
                d("5-qadam. Tekis o'zgaruvchan harakat xususiy holi",
                  r"\mathbf{a} = \text{const} \;\Rightarrow\; \mathbf{r}(t) = \mathbf{r}_0 + \mathbf{v}_0 t + \tfrac{1}{2}\mathbf{a}t^2",
                  "Maktabdagi formula — umumiy integrallashning eng sodda holi. "
                  "Ballistika va erkin tushish shu ko'rinishda yoziladi."),
            ],
            formula_meaning=(
                "$\\mathbf{v}$ harakatning 'hozirgi yo'nalishi va shiddati'ni, "
                "$\\mathbf{a}$ esa 'bu yo'nalish va shiddat qanchalik tez o'zgarayotgani'ni "
                "bildiradi. Muhandislik uchun ikkinchisi muhimroq: Nyutonning ikkinchi "
                "qonuni bo'yicha aynan tezlanish kuchga proporsional, ya'ni konstruksiyaga "
                "tushadigan yuk tezlikdan emas, tezlanishdan kelib chiqadi."
            ),
            equations=[
                eq(r"\mathbf{v} = \dfrac{d\mathbf{r}}{dt}", "Tezlik ta'rifi.", "Tezlik"),
                eq(r"\mathbf{a} = \dfrac{d^2\mathbf{r}}{dt^2}", "Tezlanish ta'rifi.", "Tezlanish"),
                eq(r"\mathbf{r}(t) = \mathbf{r}_0 + \mathbf{v}_0 t + \tfrac{1}{2}\mathbf{a}t^2",
                   "$\\mathbf{a}=\\text{const}$ holidagi harakat qonuni.", "Tekis o'zgaruvchan harakat"),
            ],
            conditions=(
                "Kinematik masala yechimi $t=0$ dagi $\\mathbf{r}_0$ va $\\mathbf{v}_0$ "
                "bilan to'liq aniqlanadi (boshlang'ich shartlar). Agar boshlang'ich "
                "emas, balki ikki nuqtadagi holat berilsa (masalan, nishonga tegish "
                "sharti), bu chegaraviy masalaga aylanadi va yechim mavjudligi "
                "kafolatlanmaydi — bu farq su-12 da muhim bo'ladi."
            ),
            worked_example=WorkedExample(
                statement=(
                    "Manipulyator uchining harakati $x(t) = 0{,}4\\cos(2t)$ m, "
                    "$y(t) = 0{,}4\\sin(2t)$ m, $z(t) = 0{,}1t$ m qonun bilan berilgan "
                    "(vint chizig'i). $t = 1$ s uchun tezlik va tezlanish vektorlari, "
                    "ularning modullari topilsin."
                ),
                given=[r"x = 0{,}4\cos 2t,\; y = 0{,}4\sin 2t,\; z = 0{,}1t\ \text{[m, s]}", r"t = 1\ \text{s}"],
                steps=[
                    st(r"\dot{x} = -0{,}8\sin 2t,\quad \dot{y} = 0{,}8\cos 2t,\quad \dot{z} = 0{,}1",
                       "Komponentalarni differensiallaymiz."),
                    st(r"v = \sqrt{0{,}64\sin^2 2t + 0{,}64\cos^2 2t + 0{,}01} = \sqrt{0{,}65} \approx 0{,}806\ \text{m/s}",
                       "Tezlik moduli vaqtga bog'liq emas — harakat tezligi bo'yicha tekis."),
                    st(r"\ddot{x} = -1{,}6\cos 2t,\quad \ddot{y} = -1{,}6\sin 2t,\quad \ddot{z} = 0",
                       "Ikkinchi hosilalar."),
                    st(r"a = \sqrt{2{,}56\cos^2 2t + 2{,}56\sin^2 2t} = 1{,}6\ \text{m/s}^2",
                       "Tezlanish moduli ham o'zgarmas, lekin nolga teng emas!"),
                    st(r"t=1: \; \mathbf{v} = (-0{,}727;\; -0{,}333;\; 0{,}1)\ \text{m/s},\quad "
                       r"\mathbf{a} = (0{,}666;\; -1{,}455;\; 0)\ \text{m/s}^2",
                       "$\\sin 2 = 0{,}909$, $\\cos 2 = -0{,}416$ qiymatlarini qo'yamiz."),
                    st(r"\mathbf{v}\cdot\mathbf{a} = (-0{,}727)(0{,}666)+(-0{,}333)(-1{,}455)+0 \approx 0",
                       "Tezlik va tezlanish perpendikular — chunki tezlik moduli o'zgarmaydi."),
                ],
                answer=(
                    "$v \\approx 0{,}806$ m/s (o'zgarmas), $a = 1{,}6$ m/s² (o'zgarmas), "
                    "$\\mathbf{v}\\perp\\mathbf{a}$."
                ),
                engineering_note=(
                    "Tezlik moduli o'zgarmasa ham 1,6 m/s² tezlanish mavjud. 5 kg li yuk "
                    "uchun bu 8 N inersiya kuchi demakdir — ushlagich uni ushlab turishi "
                    "shart. Aynan shu sabab 'tekis harakat = kuchsiz harakat' degan "
                    "tasavvur xato."
                ),
            ),
            computation=Computation(
                caption=(
                    "Vint traektoriyasi: radius, burchak tezligi va ko'tarilish tezligini "
                    "o'zgartirib, tezlik va tezlanish profillarini kuzating."
                ),
                code='''"""Traektoriya, tezlik va tezlanish: simvolik va sonli hisob."""
import numpy as np
import sympy as sp
from labkit import PARAMS, note, series, value

R = float(PARAMS.get("R", 0.4))        # radius, m
w = float(PARAMS.get("w", 2.0))        # burchak tezligi, rad/s
vz = float(PARAMS.get("vz", 0.1))      # ko'tarilish tezligi, m/s

# --- Simvolik qism: aniq hosilalar ---
t = sp.symbols("t", positive=True)
r_sym = sp.Matrix([R*sp.cos(w*t), R*sp.sin(w*t), vz*t])
v_sym = r_sym.diff(t)
a_sym = v_sym.diff(t)
note("v(t) = " + str(sp.simplify(v_sym.T)))
note("a(t) = " + str(sp.simplify(a_sym.T)))

v_mod = sp.simplify(sp.sqrt((v_sym.T*v_sym)[0]))
a_mod = sp.simplify(sp.sqrt((a_sym.T*a_sym)[0]))
value("|v| (analitik)", float(v_mod), "m/s")
value("|a| (analitik)", float(a_mod), "m/s²")

# --- Sonli qism: traektoriya va profillar ---
tt = np.linspace(0.0, 4*np.pi/w, 400)
x = R*np.cos(w*tt); y = R*np.sin(w*tt); z = vz*tt
vx = -R*w*np.sin(w*tt); vy = R*w*np.cos(w*tt); vz_arr = np.full_like(tt, vz)
ax = -R*w**2*np.cos(w*tt); ay = -R*w**2*np.sin(w*tt)

series("Traektoriya (yuqoridan ko'rinish)", x.tolist(), y.tolist(),
       xlabel="x, m", ylabel="y, m")
series("Tezlik moduli", tt.tolist(), np.sqrt(vx**2+vy**2+vz_arr**2).tolist(),
       xlabel="t, s", ylabel="|v|, m/s")
series("Tezlanish moduli", tt.tolist(), np.sqrt(ax**2+ay**2).tolist(),
       xlabel="t, s", ylabel="|a|, m/s²")

# Sonli hosila bilan tekshirish (markaziy ayirma)
vx_num = np.gradient(x, tt)
note(f"Sonli va analitik tezlik farqi: {np.max(np.abs(vx_num - vx)):.2e} m/s")
value("v·a (ortogonallik)", float(vx[10]*ax[10] + vy[10]*ay[10]), "m²/s³")
''',
                parameters=[
                    p("R", "Vint radiusi R", 0.05, 1.5, 0.4, 0.05, "m"),
                    p("w", "Burchak tezligi ω", 0.5, 10.0, 2.0, 0.5, "rad/s"),
                    p("vz", "Ko'tarilish tezligi v_z", 0.0, 1.0, 0.1, 0.05, "m/s"),
                ],
                expected_output="|v| ≈ 0,806 m/s, |a| = 1,6 m/s², v·a ≈ 0",
            ),
            visualization=vis(
                "Traektoriya + urinma tezlik va tezlanish vektorlari",
                "React/SVG + Matplotlib",
                "Traektoriya egri chizig'i, unda harakatlanuvchi nuqta, undan chiquvchi "
                "yashil $\\mathbf{v}$ (urinma) va qizil $\\mathbf{a}$ (botiq tomonga) vektorlari.",
                "React/SVG: traektoriyani `<path>` bilan chizib, slider orqali $t$ ni "
                "boshqaring; vektorlarni `<line>` + marker-arrow bilan qo'ying. Matplotlib "
                "esa 3D vint uchun qulay (`plot3D` + `quiver`).",
            ),
            interpretation=(
                "Grafiklarda $|\\mathbf{v}|$ va $|\\mathbf{a}|$ gorizontal chiziq bo'lib "
                "chiqadi — ikkalasi ham o'zgarmas. Bu paradoks emas: tezlanish tezlik "
                "modulini emas, yo'nalishini o'zgartiradi. $\\mathbf{v}\\cdot\\mathbf{a} = 0$ "
                "ayniyati shuni tasdiqlaydi va u keyingi mavzudagi tangensial/normal "
                "ajratishning to'g'ridan-to'g'ri sababi."
            ),
            common_mistakes=[
                "$a = d|\\mathbf{v}|/dt$ deb hisoblash. To'g'risi: $\\mathbf{a} = d\\mathbf{v}/dt$, "
                "va modulning hosilasi faqat tangensial tashkil etuvchini beradi.",
                "Boshlang'ich shartlarni unutib, integrallash doimiysini tashlab ketish.",
                "Traektoriya va harakat qonunini chalkashtirish: traektoriya — geometriya, "
                "harakat qonuni — geometriya + vaqt.",
                "Burchakni gradusda qoldirish. NumPy va SymPy radianda ishlaydi.",
                "Sonli differensiallashni shovqinli ma'lumotga to'g'ridan-to'g'ri qo'llash — "
                "xatolik $1/\\Delta t$ marta kuchayadi (su-07 ga qarang).",
            ],
            quiz=[
                q("Tezlik moduli o'zgarmas bo'lsa, tezlanish albatta nolga tengmi?",
                  "Yo'q. Tezlanish yo'nalish o'zgarishidan ham paydo bo'ladi. Aylana bo'ylab "
                  "tekis harakatda $|\\mathbf{v}|=\\text{const}$, lekin $a = v^2/R \\neq 0$.",
                  "konseptual"),
                q("Nima uchun tezlik har doim traektoriyaga urinma?",
                  "Chunki $\\mathbf{v}$ — $\\Delta\\mathbf{r}$ vatar vektorining limiti, "
                  "va vatar $\\Delta t\\to 0$ da urinmaga intiladi.",
                  "konseptual"),
                q("$\\mathbf{a} = (0; -9{,}81; 0)$ m/s², $\\mathbf{v}_0 = (10; 10; 0)$ m/s, "
                  "$\\mathbf{r}_0 = 0$. Nuqta qachon eng yuqori nuqtaga chiqadi?",
                  "$v_y = 10 - 9{,}81t = 0 \\Rightarrow t \\approx 1{,}02$ s; balandlik "
                  "$y = 10\\cdot 1{,}02 - 4{,}905\\cdot 1{,}02^2 \\approx 5{,}1$ m.",
                  "hisob"),
                q("$\\mathbf{v}\\cdot\\mathbf{a} > 0$ bo'lsa harakat tezlashayaptimi yoki "
                  "sekinlashayaptimi?",
                  "Tezlashmoqda: $d|\\mathbf{v}|^2/dt = 2\\mathbf{v}\\cdot\\mathbf{a} > 0$.",
                  "talqin"),
                q("Kodda `np.gradient` natijasi analitik hosiladan nega biroz farq qiladi?",
                  "Chunki u chekli ayirmali approksimatsiya: markaziy ayirma xatoligi "
                  "$O(\\Delta t^2)$ tartibida. Qadam kichraytirilsa farq kamayadi.",
                  "kod"),
                q("Bir xil traektoriya bo'ylab ikki xil harakat qonuni bo'lishi mumkinmi?",
                  "Ha. Traektoriya — geometrik iz; u bo'ylab tez yoki sekin, tekis yoki "
                  "notekis yurish mumkin. Tezlanish esa butunlay boshqacha bo'ladi.",
                  "konseptual"),
            ],
            bridge_to_next=(
                "Dekart komponentalari universal, lekin ular harakatning geometriyasini "
                "yashiradi. Keyingi mavzuda tezlanishni traektoriyaning o'ziga bog'langan "
                "tabiiy o'qlarga — urinma va normal yo'nalishlarga — ajratamiz."
            ),
            research_extension=(
                "Video yoki sensordan olingan traektoriya ma'lumotlariga sun'iy shovqin "
                "qo'shing va tezlanishni uch usulda tiklang: (a) to'g'ridan-to'g'ri ikki "
                "marta `np.gradient`, (b) Savitzky–Golay filtri, (c) polinom bilan "
                "moslash. Xatolikni RMS bo'yicha taqqoslab, qaysi usul qaysi shovqin "
                "darajasida ustunligini aniqlang."
            ),
        ),
    ),
    Topic(
        id="nm-03",
        subject_id=S,
        module_id=M,
        order=3,
        title="Egri chiziqli harakat: tabiiy koordinatalar va tezlanishning ajralishi",
        description=(
            "Tangensial va normal tezlanish, egrilik radiusi va tabiiy uchlik. "
            "Nima uchun burilishda konstruksiya qo'shimcha yuk oladi."
        ),
        learning_objective=(
            "Tezlanishni $a_\\tau$ va $a_n$ ga ajratib, har birining fizik sababini "
            "ko'rsata olish va egrilik radiusini traektoriyadan hisoblash."
        ),
        prerequisites=["nm-02"],
        mathematical_core=(
            "Yoy uzunligi $s$, Frene uchligi ($\\boldsymbol{\\tau}, \\mathbf{n}, \\mathbf{b}$), "
            "egrilik $k = 1/\\rho$, vektor funksiyani murakkab argument bo'yicha differensiallash."
        ),
        engineering_application=(
            "Avtomobil yo'li va temiryo'l burilishlarini loyihalash, aylanma "
            "traektoriyali manipulyator, markazdan qochma kuch hisobi."
        ),
        computational_component=(
            "Diskret traektoriyadan egrilik radiusini sonli hisoblash va "
            "$a_\\tau$, $a_n$ ga ajratish."
        ),
        visualization_component=(
            "Traektoriya, urinma va bosh normal yo'nalishlari, egrilik doirasi "
            "(osculating circle) animatsiyasi."
        ),
        research_extension=(
            "Klotoida (Euler spirali) yo'l burilishlarida nega ishlatiladi? "
            "Egrilikning chiziqli o'sishi $a_n$ ni qanday 'silliqlashtirishini' "
            "sonli tahlil qiling."
        ),
        difficulty="asosiy",
        previous_link=(
            "nm-02 da $\\mathbf{v}\\cdot\\mathbf{a}=0$ holini ko'rdik. Endi umumiy holda "
            "tezlanishning qaysi qismi tezlikni o'zgartirishini, qaysi qismi yo'nalishni "
            "burishini ajratamiz."
        ),
        next_topic="nm-04",
        estimated_minutes=90,
        tags=["egrilik", "normal tezlanish", "tabiiy koordinatalar"],
        lesson=Lesson(
            physical_problem=(
                "Poyezd 200 m radiusli burilishga 90 km/soat tezlik bilan kiradi. "
                "Vagon yon tomonga siljib ketmaydi, lekin yo'lovchi devorga qarab "
                "bosilganini his qiladi, relslar esa yon kuch oladi. Bu kuch qayerdan "
                "keladi, agar poyezd tezligi umuman o'zgarmasa? Javob: tezlanishning "
                "yo'nalishni o'zgartiruvchi qismidan."
            ),
            concepts=[
                c("Yoy koordinatasi $s$", "Traektoriya bo'ylab o'lchangan masofa; "
                  "$v = ds/dt$ — algebraik tezlik."),
                c("Urinma birlik vektori $\\boldsymbol{\\tau}$", "$\\boldsymbol{\\tau} = d\\mathbf{r}/ds$ "
                  "— harakat yo'nalishini ko'rsatadi."),
                c("Bosh normal $\\mathbf{n}$", "Traektoriyaning botiq tomoniga yo'nalgan, "
                  "$\\boldsymbol{\\tau}$ ga perpendikular birlik vektor."),
                c("Egrilik radiusi $\\rho$", "Traektoriyaga berilgan nuqtada eng yaxshi "
                  "moslashuvchi doira radiusi; to'g'ri chiziq uchun $\\rho\\to\\infty$."),
                c("Tangensial va normal tezlanish", "$a_\\tau = \\dot{v}$ — tezlikning "
                  "o'zgarishi; $a_n = v^2/\\rho$ — yo'nalishning o'zgarishi."),
            ],
            derivation=[
                d("1-qadam. Tezlikni tabiiy o'qda yozish",
                  r"\mathbf{v} = v\,\boldsymbol{\tau},\qquad v = \frac{ds}{dt}",
                  "Tezlik urinma bo'ylab bo'lgani uchun uni skalyar tezlik va urinma "
                  "birlik vektor ko'paytmasi sifatida yozamiz."),
                d("2-qadam. Ko'paytmani differensiallash",
                  r"\mathbf{a} = \frac{d}{dt}(v\boldsymbol{\tau}) = \dot{v}\,\boldsymbol{\tau} + v\,\frac{d\boldsymbol{\tau}}{dt}",
                  "Ikkita had paydo bo'ldi: birinchisi tezlik modulining, ikkinchisi "
                  "yo'nalishning o'zgarishidan."),
                d("3-qadam. Frene formulasini qo'llash",
                  r"\frac{d\boldsymbol{\tau}}{dt} = \frac{d\boldsymbol{\tau}}{ds}\cdot\frac{ds}{dt} = \frac{\mathbf{n}}{\rho}\,v",
                  "Frene birinchi formulasi $d\\boldsymbol{\\tau}/ds = \\mathbf{n}/\\rho$ — "
                  "urinma vektorning yoy bo'yicha o'zgarish tezligi egrilikka teng va "
                  "bosh normal bo'ylab yo'nalgan."),
                d("4-qadam. Yakuniy ajralish",
                  r"\boxed{\;\mathbf{a} = \dot{v}\,\boldsymbol{\tau} + \frac{v^2}{\rho}\,\mathbf{n}\;}",
                  "Tezlanish har doim urinma-normal tekislikda yotadi; binormal "
                  "tashkil etuvchisi nolga teng. Bu — kinematikaning eng muhim "
                  "ajratishlaridan biri."),
                d("5-qadam. Egrilik radiusini traektoriyadan topish",
                  r"\rho = \frac{|\mathbf{v}|^3}{|\mathbf{v}\times\mathbf{a}|} = \frac{\big(\dot{x}^2+\dot{y}^2\big)^{3/2}}{|\dot{x}\ddot{y}-\dot{y}\ddot{x}|}",
                  "$\\mathbf{v}\\times\\mathbf{a} = v\\boldsymbol{\\tau}\\times(v^2/\\rho)\\mathbf{n} = "
                  "(v^3/\\rho)\\mathbf{b}$ dan kelib chiqadi. Tekislikdagi harakat uchun "
                  "o'ng tomondagi ko'rinish qulay."),
            ],
            formula_meaning=(
                "$a_\\tau$ — 'gaz va tormoz': tezlikni kattalashtiradi yoki kamaytiradi. "
                "$a_n = v^2/\\rho$ — 'rul': yo'nalishni buradi va har doim burilish "
                "markaziga qarab yo'nalgan. $v$ ning kvadrati muhandislik uchun hal "
                "qiluvchi: tezlikni ikki baravar oshirsangiz, normal tezlanish va u bilan "
                "birga relsga tushadigan yon kuch to'rt baravar ortadi."
            ),
            equations=[
                eq(r"\mathbf{a} = a_\tau\boldsymbol{\tau} + a_n\mathbf{n},\quad a_\tau = \dot v,\quad a_n = \frac{v^2}{\rho}",
                   "Tezlanishning tabiiy o'qlardagi ajralishi.", "Tabiiy ajralish"),
                eq(r"a = \sqrt{a_\tau^2 + a_n^2}", "To'la tezlanish moduli.", "To'la tezlanish"),
                eq(r"\rho = \frac{v^3}{|\mathbf{v}\times\mathbf{a}|}", "Egrilik radiusi.", "Egrilik radiusi"),
            ],
            conditions=(
                "$\\rho$ traektoriyaning geometrik xossasi — u boshlang'ich shartlarga "
                "emas, yo'lning shakliga bog'liq. To'g'ri chiziqda $a_n = 0$, aylanada "
                "$\\rho = R = \\text{const}$. Burilishga kirish joyida $\\rho$ sakrash "
                "bilan o'zgarsa, $a_n$ ham sakraydi — bu zarba yuklanishiga olib keladi "
                "va aynan shu sabab yo'l loyihalashda o'tish egri chiziqlari qo'llaniladi."
            ),
            worked_example=WorkedExample(
                statement=(
                    "Poyezd $R = 200$ m radiusli burilishdan $v_0 = 90$ km/soat tezlik "
                    "bilan o'tmoqda va bir vaqtda $a_\\tau = -0{,}5$ m/s² bilan sekinlashmoqda. "
                    "To'la tezlanishni va 60 t massali vagonga ta'sir etuvchi yon kuchni "
                    "toping."
                ),
                given=[r"R = 200\ \text{m}", r"v_0 = 90\ \text{km/soat} = 25\ \text{m/s}",
                       r"a_\tau = -0{,}5\ \text{m/s}^2", r"m = 60\ \text{t}"],
                steps=[
                    st(r"a_n = \frac{v^2}{\rho} = \frac{25^2}{200} = \frac{625}{200} = 3{,}125\ \text{m/s}^2",
                       "Normal tezlanish — burilish markaziga qarab."),
                    st(r"a = \sqrt{a_\tau^2+a_n^2} = \sqrt{0{,}25 + 9{,}766} = \sqrt{10{,}016} \approx 3{,}165\ \text{m/s}^2",
                       "To'la tezlanish moduli."),
                    st(r"\tan\varphi = \frac{|a_\tau|}{a_n} = \frac{0{,}5}{3{,}125} = 0{,}16 \Rightarrow \varphi \approx 9{,}1^\circ",
                       "Tezlanish vektori normaldan 9,1° og'gan."),
                    st(r"F_n = m\,a_n = 60\,000\cdot 3{,}125 = 187{,}5\ \text{kN}",
                       "Nyutonning ikkinchi qonuni bo'yicha relsdagi yon kuch (nm-07 da asoslanadi)."),
                    st(r"\frac{a_n}{g} = \frac{3{,}125}{9{,}81} = 0{,}319",
                       "Bu yo'lovchi uchun 0,32g yon ortiqcha yuklanish — sezilarli noqulaylik."),
                ],
                answer=(
                    "$a_n = 3{,}125$ m/s², $a = 3{,}165$ m/s², relsga yon kuch $F_n = 187{,}5$ kN "
                    "(vagon og'irligining ~32 %)."
                ),
                engineering_note=(
                    "Aynan shu sabab burilishlarda rels ko'tariladi (viraj): ko'tarilish "
                    "burchagi $\\theta$ shunday tanlanadiki, $\\tan\\theta = a_n/g$ bo'lsin — "
                    "u holda yon kuch relsga emas, poyezd og'irligining tashkil etuvchisiga "
                    "o'tadi. Bizning holda $\\theta \\approx 17{,}7^\\circ$ kerak bo'lardi, bu "
                    "juda katta — demak tezlikni cheklash lozim."
                ),
            ),
            computation=Computation(
                caption=(
                    "Burilish radiusi va tezlikni o'zgartirib, $a_n$, $a_\\tau$ va yon "
                    "ortiqcha yuklanishning o'zgarishini kuzating."
                ),
                code='''"""Egri chiziqli harakat: a_tau va a_n ga ajratish."""
import numpy as np
from labkit import PARAMS, note, series, table, value

R = float(PARAMS.get("R", 200.0))       # burilish radiusi, m
v0 = float(PARAMS.get("v0", 25.0))      # tezlik, m/s
at = float(PARAMS.get("at", -0.5))      # tangensial tezlanish, m/s^2
g = 9.81

an = v0**2 / R
a_tot = np.hypot(at, an)
value("a_n", an, "m/s²")
value("a_tau", at, "m/s²")
value("a to'la", a_tot, "m/s²")
value("Yon ortiqcha yuklanish", an/g, "g")
value("Kerakli viraj burchagi", np.degrees(np.arctan(an/g)), "deg")

# a_n ning tezlikka kvadratik bog'liqligi
v = np.linspace(5, 45, 100)
series("a_n(v)", v.tolist(), (v**2/R).tolist(), xlabel="v, m/s", ylabel="a_n, m/s²")

# Xavfsiz tezlik: a_n <= 0.1g (yo'lovchi qulayligi mezoni)
v_safe = np.sqrt(0.1*g*R)
note(f"Qulaylik mezoni a_n <= 0.1g uchun ruxsat etilgan tezlik: {v_safe:.1f} m/s "
     f"= {v_safe*3.6:.0f} km/soat")

# Sonli tekshirish: parametrik traektoriyadan rho ni tiklash
t = np.linspace(0, 2.0, 500)
x = R*np.cos(v0*t/R); y = R*np.sin(v0*t/R)
dx = np.gradient(x, t); dy = np.gradient(y, t)
ddx = np.gradient(dx, t); ddy = np.gradient(dy, t)
rho_num = (dx**2 + dy**2)**1.5 / np.abs(dx*ddy - dy*ddx)
note(f"Sonli egrilik radiusi: {np.median(rho_num):.2f} m (aniq qiymat {R:.2f} m)")

table("Turli tezliklarda burilish",
      ["v, km/soat", "a_n, m/s²", "a_n/g"],
      [[float(vi*3.6), float(vi**2/R), float(vi**2/(R*g))] for vi in (15, 20, 25, 30, 35)])
''',
                parameters=[
                    p("R", "Burilish radiusi R", 50.0, 1500.0, 200.0, 25.0, "m"),
                    p("v0", "Tezlik v", 5.0, 60.0, 25.0, 1.0, "m/s"),
                    p("at", "Tangensial tezlanish a_τ", -3.0, 3.0, -0.5, 0.1, "m/s²"),
                ],
                expected_output="a_n = 3,125 m/s², a = 3,165 m/s², viraj ≈ 17,7°",
            ),
            visualization=vis(
                "Egrilik doirasi va tezlanishning ajralishi",
                "Manim",
                "Traektoriya bo'ylab harakatlanuvchi nuqta, unga 'yopishgan' egrilik "
                "doirasi, $\\boldsymbol{\\tau}$ va $\\mathbf{n}$ o'qlari hamda "
                "$\\mathbf{a}$ ning ikki tashkil etuvchiga parallelogramm bo'yicha ajralishi.",
                "Manim bu yerda eng kuchli: egrilik doirasi radiusining traektoriya "
                "bo'ylab o'zgarishini uzluksiz animatsiya qilish React/SVG da murakkab. "
                "React tomonda esa $a_n(v)$ parabolasini interaktiv slider bilan berish "
                "yetarli.",
            ),
            interpretation=(
                "$a_n(v)$ grafigi parabola — bu muhandislik qaroriga bevosita ta'sir "
                "qiladi. Tezlikni 25 dan 35 m/s ga oshirish (40 % o'sish) normal "
                "tezlanishni 3,13 dan 6,13 m/s² gacha, ya'ni ikki baravardan ko'proq "
                "oshiradi. Shuning uchun yuqori tezlikli magistrallarda burilish radiusi "
                "kilometrlar bilan o'lchanadi."
            ),
            common_mistakes=[
                "$a_n$ ni 'markazdan qochma kuch' deb atash. $a_n$ — tezlanish va u "
                "markazga qarab yo'nalgan; markazdan qochma kuch esa faqat aylanuvchi "
                "sanoq sistemasida paydo bo'ladigan inersiya kuchi (nm-06).",
                "Tekis tezlikda $a=0$ deb hisoblash. Tekis bo'lgani $a_\\tau=0$ ni "
                "bildiradi, $a_n$ esa saqlanib qoladi.",
                "$\\rho$ ni traektoriya radiusi deb aylana bo'lmagan egri chiziqlarda ham "
                "o'zgarmas olish. $\\rho$ nuqtadan nuqtaga o'zgaradi.",
                "$a = a_\\tau + a_n$ deb skalyar qo'shish. Ular perpendikular, shuning "
                "uchun $a = \\sqrt{a_\\tau^2+a_n^2}$.",
                "Sonli egrilik hisoblashda maxrajning nolga yaqinlashishini (deyarli "
                "to'g'ri chiziqli uchastkalar) tekshirmaslik.",
            ],
            quiz=[
                q("Nima uchun tezlanishning binormal tashkil etuvchisi har doim nolga teng?",
                  "Chunki $\\mathbf{a} = \\dot v\\boldsymbol{\\tau} + (v^2/\\rho)\\mathbf{n}$ "
                  "ajralishida $\\mathbf{b}$ yo'nalishida had yo'q: tezlanish urinma va bosh "
                  "normal yotgan tekislikda (soprikashuvchi tekislikda) yotadi.",
                  "konseptual"),
                q("Avtomobil to'g'ri chiziqda tormozlamoqda. $a_n$ nimaga teng?",
                  "Nolga: $\\rho\\to\\infty$, demak $a_n = v^2/\\rho \\to 0$. Faqat $a_\\tau$ qoladi.",
                  "hisob"),
                q("$R=300$ m, $v=30$ m/s. $a_n$ ni toping va uni $g$ ulushida ifodalang.",
                  "$a_n = 900/300 = 3$ m/s² $= 0{,}306g$.", "hisob"),
                q("Tezlikni 2 marta oshirsak, xuddi shu $a_n$ ni saqlab qolish uchun "
                  "radius qanday o'zgarishi kerak?",
                  "4 marta oshishi kerak, chunki $a_n = v^2/\\rho$ da $v^2$ bor.", "talqin"),
                q("Kodda `rho_num` ning medianasi olingan, o'rtachasi emas. Nega?",
                  "Chetki nuqtalarda `np.gradient` bir tomonlama sxemaga o'tadi va xatolik "
                  "oshadi; median bunday chetlanishlarga barqaror.", "kod"),
                q("Klotoida nima uchun yo'l burilishlariga kiritiladi?",
                  "Uning egriligi yoy bo'ylab chiziqli o'zgaradi, shuning uchun $a_n$ "
                  "sakrab emas, tekis o'sadi — rulni burish ham, yon kuch ham silliq bo'ladi.",
                  "talqin"),
                q("Yo'lovchi qulayligi mezoni $a_n \\le 0{,}1g$ bo'lsa, $R = 200$ m da "
                  "maksimal tezlik qancha?",
                  "$v = \\sqrt{0{,}1\\cdot 9{,}81\\cdot 200} \\approx 14$ m/s $\\approx 50$ km/soat.",
                  "hisob"),
            ],
            bridge_to_next=(
                "Hozirgacha bitta nuqta harakatini ko'rdik. Real konstruksiya esa — "
                "o'lchamga ega jism. Keyingi mavzuda qattiq jismning harakatini "
                "ilgarilanma va aylanma tashkil etuvchilarga ajratamiz."
            ),
            research_extension=(
                "Klotoida o'tish egri chizig'ini modellashtiring: $\\kappa(s) = s/(A^2)$. "
                "Freneldan olingan integrallar orqali traektoriyani quring va aylana "
                "bilan to'g'ridan-to'g'ri ulanishga nisbatan $da_n/dt$ (jerk) ning "
                "maksimal qiymatini taqqoslang. Natijani yo'l loyihalash normalari bilan "
                "solishtiring."
            ),
            manim=manim(
                scene="CurvatureScene",
                module="manim/scenes/nm_kinematics.py",
                title="Egrilik doirasi va tezlanishning ajralishi",
                summary="Egri chiziq bo'ylab harakatlanuvchi nuqta, o'zgaruvchan egrilik "
                        "doirasi va a = a_τ·τ + a_n·n ajralishi.",
            ),
        ),
    ),
    Topic(
        id="nm-04",
        subject_id=S,
        module_id=M,
        order=4,
        title="Qattiq jism kinematikasi: ilgarilanma va aylanma harakat",
        description=(
            "Qattiq jism modeli, erkinlik darajalari, burchak tezligi vektori va "
            "aylanuvchi jism nuqtalarining tezlanishlari."
        ),
        learning_objective=(
            "Qattiq jismning ixtiyoriy nuqtasi tezligi va tezlanishini burchak "
            "tezlik/tezlanish vektorlari orqali ifodalash."
        ),
        prerequisites=["nm-01", "nm-03"],
        mathematical_core=(
            "Vektor ko'paytma, $\\boldsymbol{\\omega}$ vektori, Eyler formulasi "
            "$\\mathbf{v} = \\boldsymbol{\\omega}\\times\\mathbf{r}$, aylanish matritsasi."
        ),
        engineering_application=(
            "Val, shkiv, tishli uzatma, rotor va shpindellar kinematikasi; "
            "markazdan qochma yuklanish hisobi."
        ),
        computational_component=(
            "Aylanuvchi disk nuqtalari tezliklari maydonini NumPy bilan hisoblash "
            "va vizualizatsiya uchun vektor maydon tayyorlash."
        ),
        visualization_component=(
            "Aylanuvchi jism, $\\boldsymbol{\\omega}$ vektori o'q bo'ylab, nuqtalar "
            "tezliklarining chiziqli taqsimoti."
        ),
        research_extension=(
            "Yuqori aylanishli rotorlarda markazdan qochma kuchlanish qalinlikka "
            "qanday bog'liq? Bu savol mq-19 va pq-09 da analitik yechimga aylanadi."
        ),
        difficulty="asosiy",
        previous_link=(
            "nm-03 da nuqtaning tezlanishini ajratdik. Endi cheksiz ko'p nuqtadan "
            "iborat jismni ko'ramiz — lekin qattiqlik sharti ularning barchasini "
            "bir-biriga bog'lab, erkinlik darajalarini 6 taga tushiradi."
        ),
        next_topic="nm-05",
        estimated_minutes=90,
        tags=["qattiq jism", "burchak tezligi", "Eyler formulasi"],
        lesson=Lesson(
            physical_problem=(
                "Turbina roteri 3000 ayl/min bilan aylanadi. Uning qirrasidagi kurakcha "
                "markazdan qochma kuch ta'sirida uzilib ketishi mumkin. Buni hisoblash "
                "uchun avval kurakchaning tezlanishi kerak. Lekin rotor — cheksiz ko'p "
                "nuqta. Har biri uchun alohida $\\mathbf{r}(t)$ yozish mumkin emas; "
                "bizga butun jismni bitta vektor — $\\boldsymbol{\\omega}$ bilan "
                "tavsiflash usuli kerak."
            ),
            concepts=[
                c("Qattiq jism (rigid body)", "Istalgan ikki nuqtasi orasidagi masofa "
                  "o'zgarmaydigan model. Fazoda 6 ta erkinlik darajasiga ega: 3 ta "
                  "ilgarilanma, 3 ta aylanma."),
                c("Ilgarilanma harakat", "Jismdagi har qanday to'g'ri chiziq o'z-o'ziga "
                  "parallel qoladi. Barcha nuqtalar bir xil $\\mathbf{v}$ va $\\mathbf{a}$ ga ega."),
                c("Burchak tezligi vektori $\\boldsymbol{\\omega}$", "Moduli aylanish "
                  "tezligiga teng, yo'nalishi aylanish o'qi bo'ylab o'ng vint qoidasi "
                  "bo'yicha aniqlanadi."),
                c("Burchak tezlanishi $\\boldsymbol{\\varepsilon}$", "$\\boldsymbol{\\varepsilon} = "
                  "d\\boldsymbol{\\omega}/dt$; tezlanuvchi aylanishda $\\boldsymbol{\\omega}$ "
                  "bilan bir yo'nalishda."),
                c("Aylanma va markazga intilma tezlanish", "Nuqta tezlanishining ikki qismi: "
                  "$\\boldsymbol{\\varepsilon}\\times\\mathbf{r}$ va "
                  "$\\boldsymbol{\\omega}\\times(\\boldsymbol{\\omega}\\times\\mathbf{r})$."),
            ],
            derivation=[
                d("1-qadam. Qattiqlik shartini yozish",
                  r"|\mathbf{r}_B - \mathbf{r}_A| = \text{const} \;\Rightarrow\; "
                  r"(\mathbf{r}_B-\mathbf{r}_A)\cdot(\mathbf{v}_B-\mathbf{v}_A) = 0",
                  "Masofa kvadratini differensiallaymiz. Natija: ikki nuqta tezliklari "
                  "farqi ularni tutashtiruvchi vektorga perpendikular."),
                d("2-qadam. Perpendikularlikdan burchak tezligiga o'tish",
                  r"\mathbf{v}_B - \mathbf{v}_A = \boldsymbol{\omega}\times(\mathbf{r}_B-\mathbf{r}_A)",
                  "Berilgan vektorga perpendikular bo'lgan har qanday chiziqli "
                  "almashtirish vektor ko'paytma ko'rinishida yoziladi (antisimmetrik "
                  "tenzorning vektorga mos kelishi). $\\boldsymbol{\\omega}$ — butun jism "
                  "uchun yagona."),
                d("3-qadam. Eyler formulasi",
                  r"\boxed{\;\mathbf{v}_M = \mathbf{v}_O + \boldsymbol{\omega}\times\mathbf{r}_{OM}\;}",
                  "Qattiq jismning istalgan nuqtasi tezligi = qutb tezligi + qutb "
                  "atrofidagi aylanish tezligi. Bu — qattiq jism kinematikasining asosiy formulasi."),
                d("4-qadam. Tezlanishni olish uchun differensiallash",
                  r"\mathbf{a}_M = \mathbf{a}_O + \boldsymbol{\varepsilon}\times\mathbf{r}_{OM} + "
                  r"\boldsymbol{\omega}\times(\boldsymbol{\omega}\times\mathbf{r}_{OM})",
                  "Ko'paytmani differensiallash qoidasi va $\\dot{\\mathbf{r}}_{OM} = "
                  "\\boldsymbol{\\omega}\\times\\mathbf{r}_{OM}$ dan foydalanildi."),
                d("5-qadam. Qo'zg'almas o'q atrofida aylanish uchun soddalashtirish",
                  r"v = \omega R,\qquad a_n = \omega^2 R,\qquad a_\tau = \varepsilon R",
                  "$\\boldsymbol{\\omega}\\perp\\mathbf{R}$ bo'lgani uchun "
                  "$\\boldsymbol{\\omega}\\times(\\boldsymbol{\\omega}\\times\\mathbf{R}) = "
                  "-\\omega^2\\mathbf{R}$. Bu nm-03 dagi $a_n = v^2/\\rho$ bilan aynan mos "
                  "tushadi: $v^2/R = \\omega^2R$."),
            ],
            formula_meaning=(
                "Eyler formulasi qattiq jism harakatini ikki mustaqil qismga ajratadi: "
                "bitta nuqtaning (qutbning) ko'chishi va shu nuqta atrofidagi burilish. "
                "Qutbni istalgancha tanlash mumkin — $\\boldsymbol{\\omega}$ o'zgarmaydi, "
                "bu jismning obyektiv tavsifi. $\\omega^2 R$ esa muhandislik uchun xavf "
                "o'lchovi: aylanish tezligini ikki baravar oshirish markazdan qochma "
                "yuklanishni to'rt baravar oshiradi."
            ),
            equations=[
                eq(r"\mathbf{v}_M = \mathbf{v}_O + \boldsymbol{\omega}\times\mathbf{r}_{OM}",
                   "Eyler formulasi — tezliklar taqsimoti.", "Eyler formulasi"),
                eq(r"\mathbf{a}_M = \mathbf{a}_O + \boldsymbol{\varepsilon}\times\mathbf{r}_{OM} + \boldsymbol{\omega}\times(\boldsymbol{\omega}\times\mathbf{r}_{OM})",
                   "Rivals formulasi — tezlanishlar taqsimoti.", "Rivals formulasi"),
                eq(r"\omega = \frac{\pi n}{30}", "Ayl/min dan rad/s ga o'tish ($n$ — ayl/min).",
                   "Chastota bog'lanishi"),
            ],
            conditions=(
                "Qo'zg'almas o'q atrofida aylanishda ikkita podshipnik jismning 5 ta "
                "erkinlik darajasini bog'laydi, faqat $\\varphi(t)$ qoladi. Boshlang'ich "
                "shartlar: $\\varphi_0$ va $\\omega_0$. Agar jism erkin bo'lsa (masalan, "
                "kosmik apparat), 6 ta koordinata va 6 ta boshlang'ich tezlik kerak."
            ),
            worked_example=WorkedExample(
                statement=(
                    "Turbina roteri $n = 3000$ ayl/min bilan aylanadi, tashqi radius "
                    "$R = 0{,}6$ m. O'chirishda u 12 s davomida tekis sekinlanib to'xtaydi. "
                    "(a) Ish rejimida qirradagi nuqtaning tezligi va tezlanishi; "
                    "(b) to'xtatish paytidagi burchak tezlanishi va to'la tezlanish; "
                    "(c) 0,2 kg li kurakcha ildizidagi markazdan qochma kuch."
                ),
                given=[r"n = 3000\ \text{ayl/min}", r"R = 0{,}6\ \text{m}",
                       r"t_{\text{to'xtash}} = 12\ \text{s}", r"m_k = 0{,}2\ \text{kg}"],
                steps=[
                    st(r"\omega = \frac{\pi n}{30} = \frac{3{,}1416\cdot 3000}{30} = 314{,}16\ \text{rad/s}",
                       "Aylanish chastotasini SI ga o'tkazamiz."),
                    st(r"v = \omega R = 314{,}16\cdot 0{,}6 = 188{,}5\ \text{m/s}",
                       "Qirra tezligi — tovush tezligining yarmidan ko'proq."),
                    st(r"a_n = \omega^2 R = 314{,}16^2\cdot 0{,}6 = 98\,696\cdot 0{,}6 \approx 59\,218\ \text{m/s}^2",
                       "Markazga intilma tezlanish."),
                    st(r"\frac{a_n}{g} = \frac{59\,218}{9{,}81} \approx 6036",
                       "Bu 6000g dan ortiq — konstruksiya uchun hal qiluvchi yuk."),
                    st(r"\varepsilon = \frac{\Delta\omega}{\Delta t} = \frac{0-314{,}16}{12} = -26{,}2\ \text{rad/s}^2,"
                       r"\quad a_\tau = \varepsilon R = -15{,}7\ \text{m/s}^2",
                       "To'xtatishdagi burchak tezlanishi va tangensial tezlanish."),
                    st(r"F_c = m_k\,a_n = 0{,}2\cdot 59\,218 \approx 11{,}8\ \text{kN}",
                       "0,2 kg li kurakcha 11,8 kN — ya'ni 1,2 tonna kuch bilan tortiladi."),
                ],
                answer=(
                    "$\\omega = 314$ rad/s; $v = 188{,}5$ m/s; $a_n \\approx 59{,}2$ km/s² "
                    "($\\approx 6036g$); $\\varepsilon = -26{,}2$ rad/s²; $F_c \\approx 11{,}8$ kN."
                ),
                engineering_note=(
                    "Tangensial tezlanish (15,7 m/s²) normal tezlanishdan (59 218 m/s²) "
                    "3770 marta kichik. Shuning uchun rotor hisobida to'xtatish rejimi "
                    "emas, doimiy aylanish rejimi hal qiluvchi. Kurakcha ildizidagi "
                    "kuchlanish esa mq-03 da hisoblanadi: $\\sigma = F_c/A$."
                ),
            ),
            computation=Computation(
                caption=(
                    "Rotor kinematikasi: aylanishlar soni va radiusni o'zgartirib, "
                    "markazdan qochma yuklanishning o'sishini kuzating."
                ),
                code='''"""Aylanuvchi rotor: tezliklar maydoni va markazdan qochma yuklanish."""
import numpy as np
from labkit import PARAMS, note, series, table, value

n_rpm = float(PARAMS.get("n_rpm", 3000.0))   # ayl/min
R = float(PARAMS.get("R", 0.6))              # tashqi radius, m
m_blade = float(PARAMS.get("m_blade", 0.2))  # kurakcha massasi, kg
g = 9.81

omega = np.pi * n_rpm / 30.0
value("ω", omega, "rad/s")
value("v (qirrada)", omega*R, "m/s")
value("a_n (qirrada)", omega**2 * R, "m/s²")
value("a_n / g", omega**2 * R / g, "—")
value("F_c (kurakcha)", m_blade * omega**2 * R / 1000.0, "kN")

# Tezlik va tezlanishning radius bo'ylab chiziqli / kvadratik taqsimoti
r = np.linspace(0.0, R, 120)
series("Tezlik v(r) = ωr", r.tolist(), (omega*r).tolist(), xlabel="r, m", ylabel="v, m/s")
series("Tezlanish a_n(r) = ω²r", r.tolist(), (omega**2*r/1000).tolist(),
       xlabel="r, m", ylabel="a_n, km/s²")

# Eyler formulasini vektor ko'rinishida tekshirish
w_vec = np.array([0.0, 0.0, omega])
r_vec = np.array([R, 0.0, 0.0])
v_vec = np.cross(w_vec, r_vec)
a_vec = np.cross(w_vec, np.cross(w_vec, r_vec))
note(f"v = ω × r = {np.round(v_vec, 2)} m/s  (modul {np.linalg.norm(v_vec):.2f})")
note(f"a = ω × (ω × r) = {np.round(a_vec, 1)} m/s²  — markazga qarab yo'nalgan")

table("Aylanishlar soniga bog'liqlik",
      ["n, ayl/min", "v, m/s", "a_n/g", "F_c, kN"],
      [[float(ni), float(np.pi*ni/30*R), float((np.pi*ni/30)**2*R/g),
        float(m_blade*(np.pi*ni/30)**2*R/1000)] for ni in (1500, 3000, 6000, 12000)])
''',
                parameters=[
                    p("n_rpm", "Aylanishlar soni n", 300.0, 20000.0, 3000.0, 100.0, "ayl/min"),
                    p("R", "Tashqi radius R", 0.05, 2.0, 0.6, 0.05, "m"),
                    p("m_blade", "Kurakcha massasi", 0.01, 5.0, 0.2, 0.01, "kg"),
                ],
                expected_output="ω = 314,16 rad/s, v = 188,5 m/s, a_n/g ≈ 6036, F_c ≈ 11,8 kN",
            ),
            visualization=vis(
                "Aylanuvchi jismning tezliklar maydoni",
                "React/SVG",
                "Disk, uning markazidan chiquvchi $\\boldsymbol{\\omega}$ vektori (o'q "
                "bo'ylab), radius bo'ylab uzunligi chiziqli o'suvchi tezlik vektorlari "
                "va markazga qarab yo'nalgan $a_n$ strelkalari.",
                "React/SVG: diskni `<circle>`, tezlik vektorlarini radius bo'ylab "
                "joylashgan `<line>` massivi sifatida chizing — uzunlik $\\propto r$. "
                "Bu chiziqli taqsimotni ko'rsatishning eng aniq usuli va u keyingi "
                "mavzudagi oniy markaz g'oyasini tayyorlaydi.",
            ),
            interpretation=(
                "Tezlik grafigi — to'g'ri chiziq, tezlanish grafigi ham to'g'ri chiziq, "
                "lekin $\\omega^2$ koeffitsienti bilan. Jadvalda aylanishlar sonini 2 "
                "baravar oshirish markazdan qochma kuchni 4 baravar oshirishi ko'rinadi. "
                "Aynan shu kvadratik bog'liqlik yuqori aylanishli mashinalarda (turbina, "
                "sentrifuga, shpindel) material tanlovini belgilaydi."
            ),
            common_mistakes=[
                "$n$ (ayl/min) va $\\omega$ (rad/s) ni chalkashtirish. "
                "$\\omega = \\pi n/30$, bu 30 marta farq degani.",
                "$\\boldsymbol{\\omega}$ ni aylanish tekisligida yotadi deb tasavvur qilish. "
                "U aylanish o'qi bo'ylab, ya'ni tekislikka perpendikular.",
                "Tezlanishning markazga intilma qismida $R$ ni emas, diametrни ishlatish.",
                "Eyler formulasida $\\mathbf{r}_{OM}$ ni teskari yo'nalishda olish.",
                "Ilgarilanma harakatda ham nuqtalar turli tezlikka ega deb o'ylash — "
                "ilgarilanma harakatda barcha nuqtalar tezligi bir xil.",
            ],
            quiz=[
                q("Ilgarilanma harakat albatta to'g'ri chiziqli bo'ladimi?",
                  "Yo'q. Masalan, Ferris g'ildiragining kabinasi egri chiziq bo'ylab "
                  "harakatlanadi, lekin har doim vertikal holatda qoladi — bu ilgarilanma "
                  "harakat, chunki jismdagi har bir chiziq o'z-o'ziga parallel qoladi.",
                  "konseptual"),
                q("$\\boldsymbol{\\omega}$ vektorining yo'nalishi qanday aniqlanadi?",
                  "Aylanish o'qi bo'ylab, o'ng vint qoidasi bo'yicha: barmoqlar aylanish "
                  "yo'nalishida bukilsa, bosh barmoq $\\boldsymbol{\\omega}$ ni ko'rsatadi.",
                  "konseptual"),
                q("$n = 1500$ ayl/min, $R = 0{,}3$ m. $v$ va $a_n$ ni toping.",
                  "$\\omega = \\pi\\cdot 1500/30 = 157{,}1$ rad/s; $v = 47{,}1$ m/s; "
                  "$a_n = 157{,}1^2\\cdot 0{,}3 \\approx 7404$ m/s² $\\approx 755g$.", "hisob"),
                q("Nima uchun rotor hisobida to'xtatish rejimi emas, nominal rejim hal qiluvchi?",
                  "Chunki $a_n = \\omega^2R$ tangensial tezlanish $a_\\tau = \\varepsilon R$ dan "
                  "ordinar darajada katta: misolda 3770 marta.", "talqin"),
                q("Kodda `np.cross(w_vec, np.cross(w_vec, r_vec))` natijasi nima uchun "
                  "$-\\omega^2\\mathbf{r}$ ga teng chiqadi?",
                  "Ikki karrali vektor ko'paytma formulasi bo'yicha "
                  "$\\mathbf{a}\\times(\\mathbf{b}\\times\\mathbf{c}) = \\mathbf{b}(\\mathbf{a}\\cdot\\mathbf{c}) - "
                  "\\mathbf{c}(\\mathbf{a}\\cdot\\mathbf{b})$; $\\boldsymbol{\\omega}\\perp\\mathbf{r}$ "
                  "bo'lgani uchun birinchi had yo'qoladi.", "kod"),
                q("Qattiq jism fazoda nechta erkinlik darajasiga ega va nima uchun?",
                  "6 ta: 3 ta nuqta koordinatasi + 3 ta burilish burchagi. Qattiqlik sharti "
                  "qolgan barcha nuqtalarni bog'lab qo'yadi.", "konseptual"),
            ],
            bridge_to_next=(
                "Aylanish o'qi qo'zg'almas bo'lsa masala oddiy. Lekin shatun yoki g'ildirak "
                "kabi tekis harakatda jism ham ko'chadi, ham buriladi. Keyingi mavzuda bu "
                "murakkab harakatni bitta nuqta — oniy markaz atrofidagi aylanishga "
                "keltiramiz."
            ),
            research_extension=(
                "Aylanuvchi disk ichidagi markazdan qochma kuchlanishni hisoblang: "
                "$\\sigma_r$ va $\\sigma_\\theta$ ni radius bo'yicha integrallash orqali "
                "toping (bu mq-19 va tmm-16 ning tayyorgarligi). So'ngra teng "
                "mustahkamlikdagi disk profilini — qalinlik $h(r)$ ni shunday tanlangki, "
                "$\\sigma = \\text{const}$ bo'lsin — sonli topishga urinib ko'ring."
            ),
        ),
    ),
    Topic(
        id="nm-05",
        subject_id=S,
        module_id=M,
        order=5,
        title="Jismning tekis harakati: tezliklar taqsimoti va tezliklar oniy markazi",
        description=(
            "Tekis parallel harakat, uni ilgarilanma va aylanma harakatga ajratish, "
            "tezliklar oniy markazi (TOM) usuli."
        ),
        learning_objective=(
            "Mexanizm bo'g'inlari uchun TOM ni topib, barcha nuqtalar tezligini "
            "grafik-analitik usulda aniqlash."
        ),
        prerequisites=["nm-04"],
        mathematical_core=(
            "Eyler formulasining tekis holi, proyeksiyalar teoremasi, ikki "
            "perpendikularning kesishishi."
        ),
        engineering_application=(
            "Krivoship-shatun mexanizmi, g'ildirakning sirpanmasdan dumalashi, "
            "richagli uzatmalar tahlili."
        ),
        computational_component=(
            "Krivoship-shatun mexanizmi kinematikasini to'liq sikl bo'yicha hisoblash "
            "va porshen tezligi/tezlanishi grafigini qurish."
        ),
        visualization_component=(
            "Mexanizm animatsiyasi, TOM ning harakati (sentroida), tezlik vektorlari."
        ),
        research_extension=(
            "Krivoship-shatun mexanizmida $\\lambda = r/l$ nisbati ikkinchi tartibli "
            "garmonikaga qanday ta'sir qiladi? Fourier tahlili bilan tekshiring "
            "(su-06 va nm-27 bilan bog'lanadi)."
        ),
        difficulty="asosiy",
        previous_link=(
            "nm-04 da $\\mathbf{v}_M = \\mathbf{v}_O + \\boldsymbol{\\omega}\\times\\mathbf{r}$ "
            "formulasini oldik. Endi tekis holda shunday O nuqtani topamizki, uning "
            "tezligi nolga teng bo'lsin — shunda formula juda soddalashadi."
        ),
        next_topic="nm-06",
        estimated_minutes=90,
        tags=["tekis harakat", "oniy markaz", "mexanizm"],
        lesson=Lesson(
            physical_problem=(
                "Ichki yonuv dvigatelida porshen to'g'ri chiziq bo'ylab, krivoship esa "
                "aylana bo'ylab harakatlanadi. Ularni bog'lovchi shatun na sof "
                "ilgarilanma, na sof aylanma harakat qiladi. Porshen tezligi qanday "
                "o'zgaradi? Bu savol muhim, chunki porshenning tezlanishi inersiya "
                "kuchini, u esa shatun podshipnigidagi yukni belgilaydi."
            ),
            concepts=[
                c("Tekis parallel harakat", "Jismning barcha nuqtalari qandaydir "
                  "qo'zg'almas tekislikka parallel tekisliklarda harakatlanadi. "
                  "3 ta erkinlik darajasi: $x_A, y_A, \\varphi$."),
                c("Tezliklar oniy markazi (TOM)", "Berilgan onda tezligi nolga teng "
                  "bo'lgan nuqta. Uning atrofida jism sof aylanayotgandek ko'rinadi."),
                c("Sentroida", "TOM ning qo'zg'almas tekislikda (qo'zg'almas sentroida) "
                  "yoki jism bilan bog'liq tekislikda (harakatlanuvchi sentroida) "
                  "chizadigan chizig'i."),
                c("Proyeksiyalar teoremasi", "Kesmaning ikki uchidagi tezliklarning "
                  "kesma yo'nalishidagi proyeksiyalari teng: $v_A\\cos\\alpha = v_B\\cos\\beta$."),
                c("Sirpanmasdan dumalash", "Kontakt nuqtasi TOM bo'ladi: $v_C = 0$, "
                  "markaz tezligi esa $v_O = \\omega R$."),
            ],
            derivation=[
                d("1-qadam. Tekis holda Eyler formulasi",
                  r"\mathbf{v}_M = \mathbf{v}_A + \boldsymbol{\omega}\times\mathbf{r}_{AM},\qquad "
                  r"\boldsymbol{\omega} = \omega\mathbf{k}",
                  "Burchak tezligi tekislikka perpendikular, shuning uchun "
                  "$\\boldsymbol{\\omega}\\times\\mathbf{r}_{AM}$ vektori $\\mathbf{r}_{AM}$ ga "
                  "perpendikular va moduli $\\omega\\,|\\mathbf{r}_{AM}|$."),
                d("2-qadam. TOM mavjudligini isbotlash",
                  r"\mathbf{v}_P = 0 \;\Rightarrow\; \mathbf{v}_A = -\boldsymbol{\omega}\times\mathbf{r}_{AP}"
                  r"\;\Rightarrow\; \mathbf{r}_{AP} = \frac{\boldsymbol{\omega}\times\mathbf{v}_A}{\omega^2}",
                  "$\\omega \\neq 0$ bo'lsa, bu tenglama yagona yechimga ega — demak TOM "
                  "har doim mavjud va yagona. $\\omega = 0$ bo'lsa harakat ilgarilanma va "
                  "TOM cheksizlikka ketadi."),
                d("3-qadam. TOM orqali tezliklar taqsimoti",
                  r"\boxed{\;\mathbf{v}_M = \boldsymbol{\omega}\times\mathbf{r}_{PM},\qquad v_M = \omega\,|PM|\;}",
                  "TOM ni qutb qilib olsak, formuladan ilgarilanma had yo'qoladi. Endi "
                  "har bir nuqta tezligi TOM gacha bo'lgan masofaga proporsional va "
                  "shu masofaga perpendikular."),
                d("4-qadam. TOM ni amalda topish",
                  r"P = \big(\text{A dagi } \mathbf{v}_A \text{ ga perpendikular}\big) \cap "
                  r"\big(\text{B dagi } \mathbf{v}_B \text{ ga perpendikular}\big)",
                  "Ikki nuqta tezligi yo'nalishi ma'lum bo'lsa, ularga o'tkazilgan "
                  "perpendikularlar kesishmasi TOM ni beradi — hech qanday hisob "
                  "talab qilinmaydi."),
                d("5-qadam. Krivoship-shatun uchun porshen tezligi",
                  r"x_B = r\cos\varphi + l\sqrt{1-\lambda^2\sin^2\varphi},\quad \lambda = \frac{r}{l};"
                  r"\qquad v_B = \dot x_B \approx -r\omega\Big(\sin\varphi + \frac{\lambda}{2}\sin 2\varphi\Big)",
                  "Geometrik bog'lanishni differensiallash. Ildizni qatorga yoyish "
                  "ikkinchi garmonikani ($\\sin 2\\varphi$) ochib beradi — aynan shu had "
                  "dvigatel tebranishining ikkinchi tartibli tashkil etuvchisini yaratadi."),
            ],
            formula_meaning=(
                "TOM tushunchasi murakkab harakatni har onda sof aylanishga keltiradi: "
                "'jism shu ko'rinmas o'q atrofida aylanyapti'. $v = \\omega\\cdot|PM|$ "
                "formulasi tezliklar taqsimoti chiziqli ekanini bildiradi — TOM dan "
                "uzoqroq nuqta tezroq harakatlanadi. Krivoship formulasidagi "
                "$\\lambda\\sin 2\\varphi$ hadi esa muhandislik tili bilan aytganda "
                "ikkinchi tartibli muvozanatsizlik manbai."
            ),
            equations=[
                eq(r"v_M = \omega\,|PM|", "TOM orqali tezlik.", "TOM formulasi"),
                eq(r"\omega = \frac{v_A}{|PA|}", "Burchak tezligini bitta ma'lum tezlikdan topish.",
                   "Burchak tezligi"),
                eq(r"v_B \approx -r\omega\left(\sin\varphi + \frac{\lambda}{2}\sin 2\varphi\right)",
                   "Porshen tezligining taqribiy ifodasi ($\\lambda = r/l$).", "Porshen tezligi"),
            ],
            conditions=(
                "TOM usuli faqat tezliklar uchun ishlaydi — tezlanishlar uchun uni "
                "to'g'ridan-to'g'ri qo'llab bo'lmaydi, chunki TOM ning o'zi harakatlanadi "
                "va uning tezlanishi nolga teng emas. Tezlanishlar uchun Rivals formulasi "
                "yoki tezlanishlar oniy markazi kerak. Mexanizm hisobida chegaraviy "
                "holatlar ($\\varphi = 0$ va $180°$) alohida tekshiriladi: u yerda "
                "porshen tezligi nolga teng, tezlanish esa maksimal."
            ),
            worked_example=WorkedExample(
                statement=(
                    "Krivoship-shatun mexanizmi: $r = 60$ mm, $l = 240$ mm, krivoship "
                    "$n = 3000$ ayl/min bilan tekis aylanadi. $\\varphi = 90°$ holati uchun "
                    "porshen tezligi, shatunning burchak tezligi va porshen tezlanishi "
                    "topilsin. Porshen massasi 0,4 kg — inersiya kuchini ham baholang."
                ),
                given=[r"r = 0{,}06\ \text{m},\; l = 0{,}24\ \text{m},\; \lambda = 0{,}25",
                       r"n = 3000\ \text{ayl/min} \Rightarrow \omega = 314{,}16\ \text{rad/s}",
                       r"\varphi = 90^\circ,\; m_p = 0{,}4\ \text{kg}"],
                steps=[
                    st(r"v_A = \omega r = 314{,}16\cdot 0{,}06 = 18{,}85\ \text{m/s}",
                       "Krivoship uchining (A nuqta) tezligi — u krivoshipga perpendikular."),
                    st(r"v_B \approx -r\omega\left(\sin 90^\circ + \frac{0{,}25}{2}\sin 180^\circ\right) = -18{,}85\ \text{m/s}",
                       "$\\varphi=90°$ da ikkinchi garmonika nolga teng, porshen tezligi "
                       "maksimumga yaqin."),
                    st(r"\omega_{sh} = \frac{v_A\cos\varphi}{l\cos\beta};\quad "
                       r"\sin\beta = \lambda\sin\varphi = 0{,}25 \Rightarrow \beta = 14{,}48^\circ",
                       "Shatun burchagi geometrik bog'lanishdan."),
                    st(r"\omega_{sh} = \frac{\omega r\cos\varphi}{l\cos\beta} = \frac{314{,}16\cdot0{,}06\cdot 0}{0{,}24\cdot 0{,}968} = 0",
                       "$\\varphi = 90°$ da shatunning burchak tezligi nolga teng — bu "
                       "holatda shatun oniy ilgarilanma harakat qiladi."),
                    st(r"a_B \approx -r\omega^2(\cos\varphi + \lambda\cos 2\varphi) = "
                       r"-0{,}06\cdot 98\,696\,(0 + 0{,}25\cdot(-1)) = +1480\ \text{m/s}^2",
                       "Tezlanishni $x_B$ ni ikki marta differensiallash orqali olamiz."),
                    st(r"F_{in} = m_p\,|a_B| = 0{,}4\cdot 1480 = 592\ \text{N}",
                       "Porshenning inersiya kuchi."),
                ],
                answer=(
                    "$v_B = 18{,}85$ m/s; $\\omega_{sh} = 0$; $a_B \\approx 1480$ m/s²; "
                    "$F_{in} \\approx 592$ N."
                ),
                engineering_note=(
                    "$\\varphi = 0$ (yuqori o'lik nuqta) da tezlanish "
                    "$a_B = -r\\omega^2(1+\\lambda) = -7402$ m/s² bo'lib, inersiya kuchi "
                    "2,96 kN ga yetadi — bu $\\varphi=90°$ dagidan 5 marta katta. Aynan "
                    "o'lik nuqtalar podshipnik hisobida hal qiluvchi."
                ),
            ),
            computation=Computation(
                caption=(
                    "Krivoship-shatun mexanizmi: $\\lambda = r/l$ nisbatini o'zgartirib, "
                    "porshen tezligi va tezlanishining shakli qanday buzilishini ko'ring."
                ),
                code='''"""Krivoship-shatun mexanizmi kinematikasi (aniq va taqribiy)."""
import numpy as np
from labkit import PARAMS, note, series, table, value

r = float(PARAMS.get("r", 0.06))          # krivoship radiusi, m
l = float(PARAMS.get("l", 0.24))          # shatun uzunligi, m
n_rpm = float(PARAMS.get("n_rpm", 3000))  # ayl/min
m_p = float(PARAMS.get("m_p", 0.4))       # porshen massasi, kg

omega = np.pi*n_rpm/30.0
lam = r/l
phi = np.linspace(0, 2*np.pi, 721)

# Aniq geometrik yechim
x = r*np.cos(phi) + np.sqrt(l**2 - (r*np.sin(phi))**2)
# Aniq hosilalar (zanjir qoidasi bo'yicha)
dx = -r*np.sin(phi) - (r**2*np.sin(phi)*np.cos(phi))/np.sqrt(l**2 - (r*np.sin(phi))**2)
v_exact = omega*dx
a_exact = omega**2*np.gradient(dx, phi)

# Ikkinchi tartibgacha taqribiy yechim
v_appr = -r*omega*(np.sin(phi) + 0.5*lam*np.sin(2*phi))
a_appr = -r*omega**2*(np.cos(phi) + lam*np.cos(2*phi))

deg = np.degrees(phi)
series("Porshen tezligi (aniq)", deg.tolist(), v_exact.tolist(),
       xlabel="φ, deg", ylabel="v, m/s")
series("Porshen tezligi (taqribiy)", deg.tolist(), v_appr.tolist(),
       xlabel="φ, deg", ylabel="v, m/s")
series("Porshen tezlanishi (aniq)", deg.tolist(), (a_exact/1000).tolist(),
       xlabel="φ, deg", ylabel="a, km/s²")

value("λ = r/l", lam, "—")
value("v_max", float(np.max(np.abs(v_exact))), "m/s")
value("a (φ=0)", float(a_exact[0]), "m/s²")
value("F_inersiya (φ=0)", float(m_p*abs(a_exact[0])), "N")
note(f"Taqribiy va aniq tezlik farqining maksimumi: "
     f"{np.max(np.abs(v_exact - v_appr)):.3f} m/s "
     f"({100*np.max(np.abs(v_exact-v_appr))/np.max(np.abs(v_exact)):.2f} %)")

table("O'lik nuqtalardagi tezlanish",
      ["φ, deg", "a, m/s²", "F_in, N"],
      [[0.0, float(a_exact[0]), float(m_p*abs(a_exact[0]))],
       [180.0, float(a_exact[360]), float(m_p*abs(a_exact[360]))]])
''',
                parameters=[
                    p("r", "Krivoship radiusi r", 0.02, 0.15, 0.06, 0.005, "m"),
                    p("l", "Shatun uzunligi l", 0.10, 0.60, 0.24, 0.01, "m"),
                    p("n_rpm", "Aylanishlar soni", 500.0, 8000.0, 3000.0, 100.0, "ayl/min"),
                    p("m_p", "Porshen massasi", 0.1, 2.0, 0.4, 0.05, "kg"),
                ],
                expected_output="λ = 0,25; v_max ≈ 19,3 m/s; a(φ=0) ≈ -7402 m/s²; F_in ≈ 2961 N",
            ),
            visualization=vis(
                "Mexanizm animatsiyasi va tezliklar oniy markazi",
                "Manim",
                "Krivoship, shatun, porshen; A va B nuqtalar tezlik vektorlari; ularga "
                "o'tkazilgan perpendikularlar kesishmasi — TOM; TOM ning sikl davomida "
                "chizadigan sentroidasi.",
                "Manim: TOM cheksizlikka ketib qaytishi (φ=0 va 180° da) — bu faqat "
                "animatsiyada tushunarli bo'ladi. React/SVG tomonda esa $v(\\varphi)$ va "
                "$a(\\varphi)$ grafiklarini slider bilan berish maqsadga muvofiq.",
            ),
            interpretation=(
                "Tezlik grafigi sinusoidga o'xshaydi, lekin simmetrik emas: yuqori o'lik "
                "nuqta atrofida tezlanish moduli pastki o'lik nuqtadagidan "
                "$(1+\\lambda)/(1-\\lambda)$ marta katta. $\\lambda$ ni kamaytirish "
                "(shatunni uzaytirish) harakatni garmonikaga yaqinlashtiradi va "
                "tebranishni kamaytiradi — lekin dvigatel balandligini oshiradi. Bu — "
                "tipik muhandislik kompromissi."
            ),
            common_mistakes=[
                "TOM ni tezlanishlar uchun ham ishlatish. TOM da tezlik nolga teng, "
                "lekin tezlanish emas.",
                "Ikki nuqta tezligi parallel bo'lganda perpendikularlar kesishmasligini "
                "hisobga olmaslik — bu holda $\\omega = 0$ (oniy ilgarilanma harakat).",
                "Sirpanmasdan dumalashda kontakt nuqtasi tezligi nolga teng ekanini "
                "unutish va $v_{\\text{kontakt}} = \\omega R$ deb yozish.",
                "$\\lambda = r/l$ ni $l/r$ bilan almashtirib yuborish.",
                "Ikkinchi garmonikani tashlab, faqat $\\sin\\varphi$ bilan cheklanish — "
                "$\\lambda = 0{,}25$ da bu 12 % gacha xatolik beradi.",
            ],
            quiz=[
                q("TOM har doim jism ichida bo'ladimi?",
                  "Yo'q. U jism tashqarisida ham, hatto cheksizlikda ham bo'lishi mumkin "
                  "(ilgarilanma harakatda).", "konseptual"),
                q("G'ildirak sirpanmasdan dumalaydi, markaz tezligi $v_O = 10$ m/s, "
                  "$R = 0{,}35$ m. Eng yuqori nuqta tezligi qancha?",
                  "TOM — kontakt nuqtasi. Yuqori nuqta undan $2R$ masofada, demak "
                  "$v = \\omega\\cdot 2R = 2v_O = 20$ m/s.", "hisob"),
                q("$\\varphi = 90°$ da shatunning burchak tezligi nima uchun nolga teng?",
                  "Chunki bu holatda shatunning ikkala uchidagi tezliklar parallel bo'ladi "
                  "— oniy ilgarilanma harakat, $\\omega_{sh} = 0$.", "talqin"),
                q("Proyeksiyalar teoremasining fizik asosi nima?",
                  "Qattiqlik sharti: kesma uzunligi o'zgarmaydi, demak uchlarining "
                  "kesma bo'ylab proyeksiyalari teng bo'lishi shart.", "konseptual"),
                q("Kodda aniq va taqribiy tezlik farqi qayerda maksimal bo'ladi?",
                  "$\\varphi \\approx 90°$ va $270°$ atrofida, chunki u yerda "
                  "$\\lambda^2\\sin^2\\varphi$ hadi eng katta va qatorni ikkinchi tartibda "
                  "to'xtatish xatoligi ortadi.", "kod"),
                q("$\\lambda$ ni 0,25 dan 0,15 ga kamaytirsak, ikkinchi garmonika "
                  "amplitudasi qanday o'zgaradi?",
                  "Proporsional kamayadi: $\\lambda/2$ koeffitsienti 0,125 dan 0,075 ga "
                  "tushadi, ya'ni 40 % ga kamayadi.", "hisob"),
            ],
            bridge_to_next=(
                "Shu paytgacha barcha kuzatishlar qo'zg'almas sanoq sistemasida edi. "
                "Lekin ko'p masalada kuzatuvchining o'zi harakatlanadi — aylanuvchi "
                "platformada yurgan odam, dumalab borayotgan g'ildirakdagi nuqta. "
                "Keyingi mavzuda murakkab harakat va Koriolis effektini o'rganamiz."
            ),
            research_extension=(
                "Porshen tezlanishi $a(\\varphi)$ ni Fourier qatoriga yoying va "
                "harmonikalar amplitudalarini $\\lambda$ ning funksiyasi sifatida "
                "chizing. 1- va 2-tartibli harmonikalarni muvozanatlash uchun qanday "
                "protivoves sxemasi kerakligini tahlil qiling. Bu — dvigatel "
                "balanslash nazariyasiga kirish."
            ),
        ),
    ),
    Topic(
        id="nm-06",
        subject_id=S,
        module_id=M,
        order=6,
        title="Nuqtaning murakkab harakati: nisbiy, ko'chirma va Koriolis tezlanishi",
        description=(
            "Harakatlanuvchi sanoq sistemasida kinematika, tezliklar va "
            "tezlanishlarni qo'shish teoremalari, Koriolis tezlanishining kelib chiqishi."
        ),
        learning_objective=(
            "Harakatlanuvchi sistemadagi kuzatuvni qo'zg'almas sistemaga o'tkaza olish "
            "va Koriolis hadi qachon paydo bo'lishini aniqlash."
        ),
        prerequisites=["nm-04", "nm-05"],
        mathematical_core=(
            "Aylanuvchi bazisda differensiallash: $\\frac{d\\mathbf{A}}{dt}\\big|_{\\text{abs}} = "
            "\\frac{d\\mathbf{A}}{dt}\\big|_{\\text{rel}} + \\boldsymbol{\\omega}\\times\\mathbf{A}$."
        ),
        engineering_application=(
            "Turbina kurakchasidagi oqim, sentrifuga, gироskop, Koriolis massa "
            "rashodomeri, atmosfera va okean oqimlarining og'ishi."
        ),
        computational_component=(
            "Aylanuvchi diskda radial harakatlanuvchi nuqtaning absolyut "
            "traektoriyasini sonli qurish va tezlanish tashkil etuvchilarini ajratish."
        ),
        visualization_component=(
            "Ikki kadrda bir vaqtda: aylanuvchi sistemada to'g'ri chiziq, qo'zg'almas "
            "sistemada spiral."
        ),
        research_extension=(
            "Koriolis rashodomeri qanday ishlaydi? Naydagi suyuqlik oqimi burilish "
            "momentini qanday hosil qilishini modellashtiring."
        ),
        difficulty="murakkab",
        previous_link=(
            "nm-04 va nm-05 da jism harakatini qo'zg'almas kuzatuvchi ko'zi bilan "
            "ko'rdik. Endi kuzatuvchini jismga o'tkazamiz — va kutilmagan qo'shimcha "
            "tezlanish paydo bo'ladi."
        ),
        next_topic="nm-07",
        estimated_minutes=100,
        tags=["murakkab harakat", "Koriolis", "sanoq sistemasi"],
        lesson=Lesson(
            physical_problem=(
                "Sentrifugal nasosning aylanuvchi g'ildiragi ichida suyuqlik kanal "
                "bo'ylab markazdan chetga oqadi. Kanalning devori suyuqlikka faqat "
                "markazdan qochma effekt uchun emas, balki yana qandaydir kuch uchun "
                "ham bosim beradi — va aynan shu qo'shimcha kuch g'ildirakka moment "
                "hosil qiladi, ya'ni nasosning quvvat sarfini belgilaydi. Bu kuch "
                "qayerdan keladi?"
            ),
            concepts=[
                c("Nisbiy harakat (relative)", "Nuqtaning harakatlanuvchi sanoq "
                  "sistemasiga nisbatan harakati. $\\mathbf{v}_r$, $\\mathbf{a}_r$."),
                c("Ko'chirma harakat (transport)", "Harakatlanuvchi sistemaning "
                  "qo'zg'almasga nisbatan harakati. $\\mathbf{v}_e$ — nuqta shu onda "
                  "sistemaga 'yopishgan' bo'lsa qanday tezlikka ega bo'lardi."),
                c("Absolyut harakat", "Qo'zg'almas sistemaga nisbatan harakat: "
                  "$\\mathbf{v}_a = \\mathbf{v}_e + \\mathbf{v}_r$."),
                c("Koriolis tezlanishi", "$\\mathbf{a}_c = 2\\boldsymbol{\\omega}\\times\\mathbf{v}_r$ "
                  "— nisbiy harakat va aylanishning o'zaro ta'siridan tug'iladi."),
                c("Aylanuvchi bazisda differensiallash", "Aylanuvchi sistemadagi "
                  "vektorning absolyut hosilasi nisbiy hosila va "
                  "$\\boldsymbol{\\omega}\\times\\mathbf{A}$ yig'indisi."),
            ],
            derivation=[
                d("1-qadam. Joy vektorini ajratish",
                  r"\mathbf{r}_{abs} = \mathbf{r}_O + \mathbf{r}',\qquad "
                  r"\mathbf{r}' = x'\mathbf{i}' + y'\mathbf{j}' + z'\mathbf{k}'",
                  "$\\mathbf{r}_O$ — harakatlanuvchi sistema boshining joyi, "
                  "$\\mathbf{r}'$ — nuqtaning shu sistemadagi joyi. Muhim nuqta: "
                  "$\\mathbf{i}', \\mathbf{j}', \\mathbf{k}'$ vaqtga bog'liq!"),
                d("2-qadam. Birinchi marta differensiallash",
                  r"\mathbf{v}_{abs} = \dot{\mathbf{r}}_O + \underbrace{\dot{x}'\mathbf{i}'+\dot{y}'\mathbf{j}'+\dot{z}'\mathbf{k}'}_{\mathbf{v}_r} + "
                  r"\underbrace{x'\dot{\mathbf{i}}'+y'\dot{\mathbf{j}}'+z'\dot{\mathbf{k}}'}_{\boldsymbol{\omega}\times\mathbf{r}'}",
                  "$\\dot{\\mathbf{i}}' = \\boldsymbol{\\omega}\\times\\mathbf{i}'$ (Puasson "
                  "formulasi) — bazis vektorlari faqat buriladi, uzunligi o'zgarmaydi."),
                d("3-qadam. Tezliklarni qo'shish teoremasi",
                  r"\boxed{\;\mathbf{v}_a = \mathbf{v}_e + \mathbf{v}_r,\qquad "
                  r"\mathbf{v}_e = \mathbf{v}_O + \boldsymbol{\omega}\times\mathbf{r}'\;}",
                  "Tezliklar oddiy qo'shiladi. Bu intuitiv natija — muammo tezlanishda "
                  "boshlanadi."),
                d("4-qadam. Ikkinchi marta differensiallash",
                  r"\mathbf{a}_{abs} = \mathbf{a}_O + \boldsymbol{\varepsilon}\times\mathbf{r}' + "
                  r"\boldsymbol{\omega}\times(\boldsymbol{\omega}\times\mathbf{r}') + \mathbf{a}_r + "
                  r"2\,\boldsymbol{\omega}\times\mathbf{v}_r",
                  "$\\mathbf{v}_r$ ni differensiallashda ham $\\boldsymbol{\\omega}\\times\\mathbf{v}_r$ "
                  "chiqadi, $\\boldsymbol{\\omega}\\times\\mathbf{r}'$ ni differensiallashda ham. "
                  "Ikkalasi qo'shilib, koeffitsient 2 ni beradi."),
                d("5-qadam. Koriolis teoremasi",
                  r"\boxed{\;\mathbf{a}_a = \mathbf{a}_e + \mathbf{a}_r + \mathbf{a}_c,\qquad "
                  r"\mathbf{a}_c = 2\,\boldsymbol{\omega}\times\mathbf{v}_r\;}",
                  "Koriolis tezlanishi nolga teng bo'ladi agar: (a) $\\omega = 0$ — "
                  "ko'chirma harakat ilgarilanma; (b) $\\mathbf{v}_r = 0$ — nuqta "
                  "sistemada qo'zg'almas; (c) $\\mathbf{v}_r \\parallel \\boldsymbol{\\omega}$."),
            ],
            formula_meaning=(
                "Koriolis tezlanishi ikki sababdan tug'iladi: nisbiy harakat tufayli "
                "nuqta boshqa radiusga o'tadi va uning ko'chirma tezligi o'zgaradi "
                "($\\omega v_r$); ayni paytda aylanish nisbiy tezlik vektorini buradi "
                "($\\omega v_r$). Ikkala effekt bir xil kattalikda — shuning uchun "
                "koeffitsient aynan 2. Muhandislik ma'nosi: aylanuvchi mashinada radial "
                "oqim har doim yon kuch hosil qiladi va bu kuch quvvat sarfiga aylanadi."
            ),
            equations=[
                eq(r"\mathbf{v}_a = \mathbf{v}_e + \mathbf{v}_r", "Tezliklarni qo'shish teoremasi.",
                   "Tezliklar teoremasi"),
                eq(r"\mathbf{a}_a = \mathbf{a}_e + \mathbf{a}_r + 2\boldsymbol{\omega}\times\mathbf{v}_r",
                   "Koriolis (tezlanishlarni qo'shish) teoremasi.", "Koriolis teoremasi"),
                eq(r"a_c = 2\omega v_r \sin\alpha", "Koriolis tezlanishi moduli "
                   "($\\alpha$ — $\\boldsymbol{\\omega}$ va $\\mathbf{v}_r$ orasidagi burchak).",
                   "Koriolis moduli"),
            ],
            conditions=(
                "Harakatlanuvchi sistemani tanlash — hisoblovchining ixtiyorida, lekin "
                "to'g'ri tanlov masalani keskin soddalashtiradi. Qoida: sistemani shunday "
                "tanlangki, nisbiy harakat eng sodda (masalan, to'g'ri chiziqli) bo'lsin. "
                "Sentrifugal nasosda kanal bilan bog'langan sistema tanlanadi — u yerda "
                "suyuqlik kanal bo'ylab to'g'ri harakatlanadi."
            ),
            worked_example=WorkedExample(
                statement=(
                    "Sentrifugal nasos g'ildiragi $\\omega = 150$ rad/s bilan aylanadi. "
                    "Suyuqlik radial kanal bo'ylab $v_r = 8$ m/s tezlik bilan markazdan "
                    "chetga oqadi. Kanalning $r = 0{,}15$ m radiusidagi kesimida: (a) "
                    "ko'chirma, nisbiy va Koriolis tezlanishlari; (b) 0,5 kg/s massa "
                    "oqimidagi elementга ta'sir qiluvchi Koriolis kuchi."
                ),
                given=[r"\omega = 150\ \text{rad/s} = \text{const}", r"v_r = 8\ \text{m/s} = \text{const}",
                       r"r = 0{,}15\ \text{m}", r"\dot m = 0{,}5\ \text{kg/s}"],
                steps=[
                    st(r"a_e = \omega^2 r = 150^2\cdot 0{,}15 = 22\,500\cdot 0{,}15 = 3375\ \text{m/s}^2",
                       "Ko'chirma tezlanish — markazga qarab ($\\varepsilon = 0$ bo'lgani uchun "
                       "faqat markazga intilma qism)."),
                    st(r"a_r = \frac{dv_r}{dt} = 0",
                       "Nisbiy tezlik o'zgarmas va kanal to'g'ri — demak nisbiy tezlanish nol."),
                    st(r"a_c = 2\omega v_r\sin 90^\circ = 2\cdot 150\cdot 8 = 2400\ \text{m/s}^2",
                       "$\\boldsymbol{\\omega}$ o'q bo'ylab, $\\mathbf{v}_r$ radial — ular "
                       "perpendikular, $\\sin\\alpha = 1$."),
                    st(r"\frac{a_c}{a_e} = \frac{2400}{3375} = 0{,}71",
                       "Koriolis tezlanishi markazdan qochma effektning 71 % iga teng — "
                       "uni tashlab bo'lmaydi!"),
                    st(r"\mathbf{a}_a = \mathbf{a}_e + \mathbf{a}_c: \quad a_a = \sqrt{3375^2+2400^2} \approx 4141\ \text{m/s}^2",
                       "Ular perpendikular bo'lgani uchun geometrik qo'shiladi."),
                    st(r"F_c = \dot m \cdot 2\omega v_r \cdot \Delta t \Big|_{\text{birlik uzunlik}} "
                       r"\Rightarrow \text{elementar kuch } dF_c = 2\omega\,v_r\,dm",
                       "0,001 kg li element uchun $F_c = 0{,}001\\cdot 2400 = 2{,}4$ N; "
                       "bu kuch kanal devoriga urinma yo'nalishda tushadi va g'ildirakka "
                       "qarshilik momenti beradi."),
                ],
                answer=(
                    "$a_e = 3375$ m/s²; $a_r = 0$; $a_c = 2400$ m/s²; "
                    "$a_a \\approx 4141$ m/s². Koriolis hadi markazdan qochmaning 71 % i."
                ),
                engineering_note=(
                    "Koriolis kuchining kanal devoriga urinma yo'nalishda tushishi — "
                    "nasosning suyuqlikka energiya uzatish mexanizmi. Eyler nasos "
                    "tenglamasi ($H = u_2c_{u2}/g$) aynan shu effektdan kelib chiqadi. "
                    "Agar Koriolis hadi bo'lmaganida, sentrifugal nasos ishlamas edi."
                ),
            ),
            computation=Computation(
                caption=(
                    "Aylanuvchi kanaldagi radial oqim: absolyut traektoriya va "
                    "tezlanish tashkil etuvchilarining nisbati."
                ),
                code='''"""Murakkab harakat: aylanuvchi diskda radial harakatlanuvchi nuqta."""
import numpy as np
from labkit import PARAMS, note, series, table, value

omega = float(PARAMS.get("omega", 150.0))  # rad/s
vr = float(PARAMS.get("vr", 8.0))          # nisbiy tezlik, m/s
r0 = float(PARAMS.get("r0", 0.02))         # boshlang'ich radius, m
r_max = float(PARAMS.get("r_max", 0.15))   # chiqish radiusi, m

t_end = (r_max - r0)/vr
t = np.linspace(0, t_end, 400)
r = r0 + vr*t                 # nisbiy harakat: radius chiziqli o'sadi
phi = omega*t                 # ko'chirma harakat: burilish

# Absolyut traektoriya — Arximed spirali
X = r*np.cos(phi); Y = r*np.sin(phi)
series("Absolyut traektoriya (spiral)", X.tolist(), Y.tolist(), xlabel="x, m", ylabel="y, m")

# Tezlanish tashkil etuvchilari chiqish radiusida
a_e = omega**2*r_max
a_c = 2*omega*vr
a_r = 0.0
value("a_e (ko'chirma)", a_e, "m/s²")
value("a_c (Koriolis)", a_c, "m/s²")
value("a_r (nisbiy)", a_r, "m/s²")
value("a_c / a_e", a_c/a_e, "—")
value("a_absolyut", float(np.hypot(a_e, a_c)), "m/s²")

# Tashkil etuvchilarning radius bo'ylab o'zgarishi
rr = np.linspace(r0, r_max, 100)
series("a_e(r) — markazdan qochma", rr.tolist(), (omega**2*rr).tolist(),
       xlabel="r, m", ylabel="a, m/s²")
series("a_c(r) — Koriolis (o'zgarmas)", rr.tolist(),
       np.full_like(rr, 2*omega*vr).tolist(), xlabel="r, m", ylabel="a, m/s²")

# Qaysi radiusda ular tenglashadi?
r_eq = 2*vr/omega
note(f"a_c = a_e sharti r = 2*vr/omega = {r_eq*1000:.1f} mm da bajariladi. "
     f"Undan kichik radiusda Koriolis effekti ustun.")

table("Turli aylanish tezliklarida",
      ["ω, rad/s", "a_e, m/s²", "a_c, m/s²", "a_c/a_e"],
      [[float(w), float(w**2*r_max), float(2*w*vr), float(2*vr/(w*r_max))]
       for w in (50, 100, 150, 300)])
''',
                parameters=[
                    p("omega", "Burchak tezligi ω", 10.0, 500.0, 150.0, 10.0, "rad/s"),
                    p("vr", "Nisbiy tezlik v_r", 0.5, 30.0, 8.0, 0.5, "m/s"),
                    p("r0", "Boshlang'ich radius", 0.005, 0.10, 0.02, 0.005, "m"),
                    p("r_max", "Chiqish radiusi", 0.05, 0.50, 0.15, 0.01, "m"),
                ],
                expected_output="a_e = 3375 m/s², a_c = 2400 m/s², a_c/a_e = 0,711, spiral traektoriya",
            ),
            visualization=vis(
                "Ikki sanoq sistemasida bir harakat",
                "Manim",
                "Chapda — aylanuvchi disk bilan birga buriladigan kadr, unda nuqta "
                "to'g'ri chiziq bo'ylab yuradi; o'ngda — qo'zg'almas kadr, unda xuddi shu "
                "harakat spiral bo'lib ko'rinadi. Pastda tezlanish vektorlarining "
                "parallelogrammi.",
                "Manim bu yerda almashtirib bo'lmaydigan: ikki kadrni yonma-yon "
                "sinxron animatsiya qilish Koriolis effektini boshqa hech qanday usul "
                "bilan bu qadar aniq ko'rsatib bo'lmaydi. React/SVG da esa spiralning "
                "statik grafigi va $a_c/a_e$ nisbatining sliderli grafigi beriladi.",
            ),
            interpretation=(
                "Spiral traektoriya — nisbiy to'g'ri chiziqli harakat va aylanishning "
                "superpozitsiyasi. Muhim xulosa: $a_c$ radiusga bog'liq emas "
                "(gorizontal chiziq), $a_e$ esa chiziqli o'sadi. Demak markazga yaqin "
                "sohada Koriolis effekti ustun, chetda esa markazdan qochma. "
                "$r < 2v_r/\\omega$ shartida Koriolis hal qiluvchi — nasos g'ildiragining "
                "kirish qismida aynan shunday."
            ),
            common_mistakes=[
                "Koriolis tezlanishini 'kuch' deb atash. Bu — tezlanish; inersiya kuchi "
                "$-m\\mathbf{a}_c$ faqat harakatlanuvchi sistemada Nyuton tenglamasini "
                "saqlash uchun kiritiladi.",
                "Koeffitsient 2 ni unutish — eng keng tarqalgan hisob xatosi.",
                "$\\mathbf{v}_r$ ni absolyut tezlik bilan almashtirish. Koriolisda faqat "
                "nisbiy tezlik qatnashadi.",
                "$\\boldsymbol{\\omega} \\parallel \\mathbf{v}_r$ bo'lganda ham $a_c \\neq 0$ "
                "deb hisoblash. Vektor ko'paytma nolga teng bo'ladi.",
                "Ko'chirma tezlanishni faqat markazga intilma deb olish. Umumiy holda "
                "$\\mathbf{a}_e = \\mathbf{a}_O + \\boldsymbol{\\varepsilon}\\times\\mathbf{r}' + "
                "\\boldsymbol{\\omega}\\times(\\boldsymbol{\\omega}\\times\\mathbf{r}')$.",
            ],
            quiz=[
                q("Koriolis tezlanishidagi koeffitsient 2 qayerdan keladi?",
                  "Ikki manbadan: $\\mathbf{v}_r$ ni aylanuvchi bazisda differensiallashdan "
                  "($\\boldsymbol{\\omega}\\times\\mathbf{v}_r$) va "
                  "$\\boldsymbol{\\omega}\\times\\mathbf{r}'$ hadining "
                  "$\\dot{\\mathbf{r}}'$ qismidan ($\\boldsymbol{\\omega}\\times\\mathbf{v}_r$). "
                  "Ikkalasi bir xil, shuning uchun 2.", "konseptual"),
                q("Qaysi uchta holatda $\\mathbf{a}_c = 0$?",
                  "(1) $\\boldsymbol{\\omega}=0$ — ko'chirma harakat ilgarilanma; "
                  "(2) $\\mathbf{v}_r = 0$; (3) $\\mathbf{v}_r \\parallel \\boldsymbol{\\omega}$.",
                  "konseptual"),
                q("$\\omega = 100$ rad/s, $v_r = 5$ m/s, perpendikular. $a_c$ ni toping.",
                  "$a_c = 2\\cdot 100\\cdot 5 = 1000$ m/s².", "hisob"),
                q("Nima uchun Koriolis tezlanishi radiusga bog'liq emas?",
                  "Chunki u faqat $\\omega$ va $v_r$ ga bog'liq: $a_c = 2\\omega v_r$. "
                  "Markazdan qochma esa $\\omega^2 r$ — radiusga chiziqli bog'liq.",
                  "talqin"),
                q("Kodda hosil bo'lgan spiral qanday spiral va nega?",
                  "Arximed spirali, chunki $r = r_0 + v_r t$ va $\\varphi = \\omega t$, "
                  "demak $r$ ва $\\varphi$ chiziqli bog'langan: $r = r_0 + (v_r/\\omega)\\varphi$.",
                  "kod"),
                q("Shimoliy yarim sharda uchayotgan raketa nima uchun o'ngga og'adi?",
                  "Yer aylanishi tufayli Koriolis tezlanishi $2\\boldsymbol{\\omega}\\times\\mathbf{v}_r$ "
                  "harakatga perpendikular va shimoliy yarim sharda o'ngga yo'nalgan.",
                  "talqin"),
            ],
            bridge_to_next=(
                "Kinematika tugadi: endi biz harakatni to'liq tavsiflay olamiz. Lekin "
                "hali 'nima uchun jism aynan shunday harakatlanadi?' degan savolga javob "
                "yo'q. Keyingi modulda kuch tushunchasini kiritamiz va Nyuton qonunlari "
                "orqali dinamikaga o'tamiz."
            ),
            research_extension=(
                "Koriolis massa rashodomerini modellashtiring: U-shaklidagi nay "
                "tebranayotganda, ichidagi oqim Koriolis kuchi tufayli nayning kirish va "
                "chiqish qismlarini turli fazada tebrantiradi. Faza siljishi massa "
                "oqimiga proporsional. Sodda model quring (nayni ikki massali tizim deb "
                "olib) va faza siljishining $\\dot m$ ga chiziqli bog'liqligini "
                "tekshiring."
            ),
            manim=manim(
                scene="CoriolisScene",
                module="manim/scenes/nm_kinematics.py",
                title="Koriolis effekti: ikki kadr",
                summary="Aylanuvchi va qo'zg'almas sanoq sistemalarida bir xil harakatning "
                        "yonma-yon animatsiyasi; to'g'ri chiziq spiralga aylanadi.",
            ),
        ),
    ),
]
