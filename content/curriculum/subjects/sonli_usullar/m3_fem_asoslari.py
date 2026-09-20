"""SU / 3-modul: Chekli elementlar usulining asoslari (su-13 … su-18)."""

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

S = "sonli-usullar"
M = "su-m3"


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
    # ------------------------------------------------------------------ su-13
    Topic(
        id="su-13",
        subject_id=S, module_id=M, order=13,
        title="Chekli elementlar usulining variatsion asosi va zaif formulirovka",
        description=(
            "Kuchli va zaif formulirovkalarning farqi, Galerkin usuli, "
            "minimal potensial energiya prinsipi va FEM ning chekli "
            "ayirmalardan afzalligi."
        ),
        learning_objective=(
            "Differensial tenglamadan zaif formulirovkani keltirib "
            "chiqarish, Galerkin diskretlashtirishini qo'llash va "
            "natijaning minimal energiya prinsipiga tengligini ko'rsatish."
        ),
        prerequisites=["su-12", "tmm-19", "pq-09"],
        mathematical_core=(
            "Zaif shakl: $\\int_0^L EA\\,u'v'\\,dx = "
            "\\int_0^L f v\\,dx + [\\bar{N}v]_0^L$; "
            "Galerkin: $v = \\varphi_i$, "
            "$\\Pi = \\tfrac12\\mathbf{u}^T\\mathbf{K}\\mathbf{u} - "
            "\\mathbf{u}^T\\mathbf{f}$."
        ),
        engineering_application=(
            "Har qanday zamonaviy muhandislik hisobi: konstruksiya "
            "tahlili, issiqlik, oqim, elektromagnetizm — hammasi "
            "shu asosga quriladi."
        ),
        computational_component=(
            "Zaif formulirovkani sonli amalga oshirish, uchta usulni "
            "(FEM, Ritz, chekli ayirmalar) bir masalada taqqoslash."
        ),
        visualization_component=(
            "Sinov funksiyalari, qoldiqning ortogonalligi, energiya "
            "funksionalining minimumi."
        ),
        research_extension=(
            "Petrov–Galerkin usullarini o'rganing: sinov va vazn "
            "funksiyalari turlicha bo'lganda nima o'zgaradi va bu "
            "konvektiv masalalarda nima uchun zarur?"
        ),
        difficulty="ilg'or",
        previous_link=(
            "su-07…su-12 da chekli ayirmalar usuli to'liq qurildi va "
            "uning asosiy kamchiligi aniqlandi: u to'g'ri to'rni "
            "talab qiladi va egri chegaraga yomon moslashadi. pq-09 "
            "da esa Ritz va Galerkin usullari ishlatilgan edi — endi "
            "ularni tizimli asosda quramiz."
        ),
        next_topic="su-14",
        estimated_minutes=95,
        tags=["FEM", "zaif formulirovka", "Galerkin", "variatsion"],
        lesson=_lesson(
            problem=(
                "su-01 dagi savolga qaytamiz: "
                "burchagida teshigi bor, "
                "qovurg'alangan, qalinligi "
                "o'zgaruvchan plastina. Chekli "
                "ayirmalar uni yecha olmadi — to'r "
                "to'g'ri bo'lishi kerak edi. "
                "Ammo muammo chuqurroq. "
                "$D\\nabla^4w = q$ tenglamasi "
                "$w$ ning **to'rtinchi** hosilasini "
                "talab qiladi, ya'ni yechim juda "
                "silliq bo'lishi kerak. Qovurg'a "
                "yoki qalinlik sakragan joyda esa "
                "yechim shunchalik silliq emas — "
                "u yerda ikkinchi hosila uzilishli. "
                "Demak tenglamaning o'zi bunday "
                "yechimni **qabul qilmaydi**. "
                "Tenglamani qayta yozish kerak — "
                "shunday qilib, u kamroq silliqlik "
                "talab qilsin va shu bilan birga "
                "bir xil fizikani ifodalasin."
            ),
            concepts=[
                c("Kuchli formulirovka "
                  "(strong form)",
                  "Differensial tenglamaning o'zi; "
                  "yechimdan yuqori tartibli "
                  "hosilalar mavjudligini talab "
                  "qiladi."),
                c("Zaif formulirovka (weak form)",
                  "Tenglamani sinov funksiyasiga "
                  "ko'paytirib integrallash va "
                  "bo'laklab integrallash orqali "
                  "hosila tartibini **pasaytirish**."),
                c("Sinov funksiyasi (test function)",
                  "$v$ — ixtiyoriy, lekin muhim "
                  "chegaraviy shartlarda nolga "
                  "teng funksiya; virtual "
                  "ko'chishning matematik "
                  "ifodasi (tmm-19)."),
                c("Galerkin usuli",
                  "Sinov funksiyalari sifatida "
                  "yechim bazisining o'zini "
                  "olish: $v = \\varphi_i$. "
                  "Natijada simmetrik matritsa "
                  "hosil bo'ladi."),
                c("Muhim va tabiiy chegaraviy "
                  "shartlar",
                  "Muhim (Dirixle) — bazisga "
                  "kiritiladi; tabiiy (Neyman) — "
                  "zaif shaklda **o'z-o'zidan** "
                  "paydo bo'ladi."),
                c("Minimal potensial energiya",
                  "Simmetrik musbat aniqlangan "
                  "masalada Galerkin yechimi "
                  "$\\Pi$ ni minimallashtiradi — "
                  "Ritz usuli bilan aynan "
                  "ustma-ust tushadi."),
            ],
            derivation=[
                d("1. Kuchli formulirovka",
                  r"-\frac{d}{dx}\Big(EA\frac{du}{dx}\Big) "
                  r"= f(x), \quad 0 < x < L",
                  "Sterjenning cho'zilishi. "
                  "$u$ ning **ikkinchi** hosilasi "
                  "talab qilinadi; $EA$ uzilishli "
                  "bo'lsa bu shart buziladi."),
                d("2. Sinov funksiyasiga ko'paytirish",
                  r"-\int_0^L \frac{d}{dx}\Big(EA"
                  r"\frac{du}{dx}\Big)v\,dx = "
                  r"\int_0^L f v\,dx \quad \forall v",
                  "$v$ — ixtiyoriy funksiya. Agar "
                  "bu **barcha** $v$ uchun "
                  "bajarilsa, kuchli formulirovka "
                  "ham bajariladi."),
                d("3. Bo'laklab integrallash",
                  r"\int_0^L EA\,u'v'\,dx - "
                  r"\Big[EA\,u'v\Big]_0^L = "
                  r"\int_0^L f v\,dx",
                  "**Hal qiluvchi qadam.** Hosila "
                  "$u$ dan $v$ ga 'o'tkazildi'. "
                  "Endi $u$ dan faqat **birinchi** "
                  "hosila talab qilinadi."),
                d("4. Tabiiy chegaraviy shartning "
                  "paydo bo'lishi",
                  r"EA\,u'\Big|_L = \bar N "
                  r"\;\Longrightarrow\; "
                  r"\Big[EA u'v\Big]_0^L = "
                  r"\bar N v(L)",
                  "Chegara hadida aynan "
                  "**kuch** turadi. Demak kuch "
                  "sharti zaif shaklga "
                  "o'z-o'zidan kiradi — uni "
                  "alohida qo'yish kerak emas. "
                  "Shuning uchun u **tabiiy** "
                  "deb ataladi."),
                d("5. Zaif formulirovka",
                  r"\text{Topilsin } u \in V: \quad "
                  r"\int_0^L EA\,u'v'\,dx = "
                  r"\int_0^L f v\,dx + \bar N v(L) "
                  r"\quad \forall v \in V_0",
                  "$V$ — muhim shartni "
                  "qanoatlantiruvchi funksiyalar, "
                  "$V_0$ — u yerda nolga teng "
                  "bo'lganlari. Bu **virtual "
                  "ishlar prinsipi** (tmm-19) "
                  "ning aynan o'zi."),
                d("6. Silliqlik talabining "
                  "pasayishi",
                  r"\text{kuchli: } u \in C^2; "
                  r"\quad \text{zaif: } u \in H^1 "
                  r"\ (u' \ \text{kvadrat bilan "
                  r"integrallanuvchi})",
                  "**Asosiy yutuq.** Zaif shakl "
                  "bo'lakli-chiziqli funksiyalarni "
                  "qabul qiladi — ularning "
                  "hosilasi uzilishli, lekin "
                  "integrallanadi. Aynan shu FEM "
                  "ni mumkin qiladi."),
                d("7. Galerkin diskretlashtirishi",
                  r"u_h = \sum_j u_j\varphi_j, "
                  r"\quad v = \varphi_i "
                  r"\;\Longrightarrow\; "
                  r"\sum_j\Big(\int_0^L EA\,"
                  r"\varphi_i'\varphi_j'dx\Big)u_j "
                  r"= \int_0^L f\varphi_i dx + \ldots",
                  "Sinov funksiyalari sifatida "
                  "bazisning o'zi olinadi. "
                  "$N$ ta $i$ uchun $N$ ta "
                  "tenglama."),
                d("8. Algebraik tizim",
                  r"\mathbf{K}\mathbf{u} = "
                  r"\mathbf{f}, \quad K_{ij} = "
                  r"\int_0^L EA\,\varphi_i'"
                  r"\varphi_j'\,dx",
                  "**$\\mathbf{K}$ simmetrik** — "
                  "chunki $\\varphi_i'\\varphi_j'$ "
                  "indekslar bo'yicha simmetrik. "
                  "Bu Galerkin tanlovining "
                  "bevosita natijasi (su-05 dagi "
                  "Cholesky shundan)."),
                d("9. Energiya funksionali bilan "
                  "bog'lanish",
                  r"\Pi(u) = \frac12\int_0^L "
                  r"EA(u')^2dx - \int_0^L fu\,dx "
                  r"- \bar N u(L)",
                  "Potensial energiya (tmm-19). "
                  "Uning birinchi variatsiyasi "
                  "$\\delta\\Pi = 0$ aynan "
                  "5-qadamdagi zaif shaklni "
                  "beradi."),
                d("10. Diskret energiya va minimum",
                  r"\Pi_h = \frac12\mathbf{u}^T"
                  r"\mathbf{K}\mathbf{u} - "
                  r"\mathbf{u}^T\mathbf{f} "
                  r"\;\Longrightarrow\; "
                  r"\frac{\partial\Pi_h}"
                  r"{\partial\mathbf{u}} = 0 "
                  r"\;\Longrightarrow\; "
                  r"\mathbf{K}\mathbf{u} = \mathbf{f}",
                  "**Ikki yo'l bir joyga olib "
                  "keladi.** Galerkin (qoldiqni "
                  "ortogonallash) va Ritz "
                  "(energiyani minimallash) "
                  "simmetrik masalada aynan bir "
                  "xil tizimni beradi."),
                d("11. Eng yaxshi yaqinlashish "
                  "xossasi",
                  r"\|u - u_h\|_E = \min_{v_h \in "
                  r"V_h}\|u - v_h\|_E",
                  "**Galerkin ortogonalligi.** "
                  "FEM yechimi berilgan bazisda "
                  "energiya normasi bo'yicha "
                  "**eng yaxshi** yaqinlashish. "
                  "Chekli ayirmalarda bunday "
                  "kafolat yo'q."),
                d("12. Energiyaning quyidan "
                  "chegaralanishi",
                  r"\Pi_h \ge \Pi_{exact} "
                  r"\;\Longrightarrow\; "
                  r"\text{FEM konstruksiyani "
                  r"BIKRROQ ko'rsatadi}",
                  "Diskret fazo haqiqiy fazoning "
                  "qism fazosi, demak minimum "
                  "kattaroq. Amalda: FEM "
                  "og'ishni **kam** ko'rsatadi — "
                  "su-08 dagi chekli ayirmalarning "
                  "aksincha."),
            ],
            meaning=(
                "Zaif formulirovkaning butun "
                "mohiyati 3- va 6-qadamlarda: "
                "bo'laklab integrallash hosilani "
                "noma'lumdan sinov funksiyasiga "
                "o'tkazadi va shu bilan yechimga "
                "qo'yilgan silliqlik talabini "
                "**pasaytiradi**. Kuchli shakl "
                "ikkinchi hosilani talab qilardi; "
                "zaif shakl faqat birinchisini. "
                "Bu shunchaki texnik qulaylik "
                "emas — u butun usulni mumkin "
                "qiladi. Bo'lakli-chiziqli "
                "funksiya (uchburchak 'do'ppi') "
                "ning ikkinchi hosilasi mavjud "
                "emas, birinchisi esa bo'lakli "
                "doimiy va bemalol "
                "integrallanadi. Shuning uchun "
                "FEM bazisi mahalliy va sodda "
                "bo'lishi mumkin — va aynan "
                "mahalliylik uni istalgan "
                "geometriyaga moslashtiradi. "
                "Ikkinchi chuqur natija "
                "4-qadamda: kuch chegaraviy "
                "sharti zaif shaklga "
                "**o'z-o'zidan** kiradi. Chekli "
                "ayirmalarda kuch shartini "
                "qo'yish alohida ish edi (su-08 "
                "dagi soxta tugunlar); bu yerda "
                "u bo'laklab integrallashning "
                "chegara hadi sifatida tabiiy "
                "paydo bo'ladi. Faqat ko'chish "
                "sharti majburan qo'yiladi. Bu "
                "ajratish — muhim va tabiiy "
                "shartlar — FEM ning eng "
                "chiroyli tomonlaridan biri. "
                "10-qadam esa ikkita butunlay "
                "boshqa g'oyani birlashtiradi: "
                "Galerkin qoldiqni sinov "
                "funksiyalariga ortogonal "
                "qiladi, Ritz esa energiyani "
                "minimallaydi. Simmetrik "
                "masalada ular aynan bir xil "
                "tizimni beradi va bu tasodif "
                "emas — energiyaning "
                "variatsiyasi aynan zaif shakl. "
                "Shundan 11- va 12-qadamlardagi "
                "kuchli natijalar kelib chiqadi: "
                "FEM yechimi berilgan bazisda "
                "**eng yaxshi** va u har doim "
                "bir tomonga — bikrroq tomonga "
                "— xato qiladi. Chekli "
                "ayirmalarda bunday kafolatlar "
                "yo'q: su-08 da ular balkani "
                "yumshoqroq ko'rsatgan edi. "
                "Ikkala usulning xatosi turli "
                "tomonga yo'nalgani esa "
                "foydali: ular birgalikda aniq "
                "yechimni qamrab oladi."
            ),
            equations=[
                eq(r"\int_0^L EA\,u'v'\,dx = "
                   r"\int_0^L fv\,dx + \bar N v(L) "
                   r"\quad \forall v \in V_0",
                   "Zaif formulirovka — virtual "
                   "ishlar prinsipining aynan "
                   "o'zi.", "Zaif shakl"),
                eq(r"K_{ij} = \int_0^L EA\,"
                   r"\varphi_i'\varphi_j'\,dx = K_{ji}",
                   "Galerkin matritsasi — "
                   "simmetrik.", "Bikrlik matritsasi"),
                eq(r"\Pi_h = \tfrac12\mathbf{u}^T"
                   r"\mathbf{K}\mathbf{u} - "
                   r"\mathbf{u}^T\mathbf{f}",
                   "Diskret potensial energiya; "
                   "uning minimumi "
                   "$\\mathbf{K}\\mathbf{u} = "
                   "\\mathbf{f}$ ni beradi.",
                   "Diskret energiya"),
                eq(r"\|u-u_h\|_E = \min_{v_h}"
                   r"\|u-v_h\|_E, \qquad \Pi_h \ge \Pi",
                   "Eng yaxshi yaqinlashish va "
                   "energiyaning quyidan "
                   "chegaralanishi.",
                   "Galerkin xossalari"),
            ],
            conditions=(
                "**Zaif formulirovka uchun "
                "talablar:**\n"
                "- $u \\in H^1$: $u$ va $u'$ "
                "kvadrat bilan integrallanuvchi;\n"
                "- $v \\in V_0$: sinov funksiyasi "
                "**muhim** shartlarda nolga teng;\n"
                "- $EA > 0$ va chegaralangan.\n\n"
                "**Chegaraviy shartlarning "
                "tasnifi:**\n"
                "- **Muhim (essential, Dirixle):** "
                "$u = \\bar u$ — bazisga "
                "majburan kiritiladi, sinov "
                "funksiyasi u yerda nol;\n"
                "- **Tabiiy (natural, Neyman):** "
                "$EAu' = \\bar N$ — zaif shaklda "
                "o'z-o'zidan paydo bo'ladi, "
                "hech narsa qilish kerak emas.\n\n"
                "**Yechim mavjudligi (Laks–"
                "Milgram):** bilinear shakl "
                "chegaralangan va majburiy "
                "(coercive) bo'lsa, yechim "
                "mavjud va yagona. Mexanikada "
                "bu konstruksiya yetarlicha "
                "mahkamlangan degani.\n\n"
                "**Galerkin uchun:** sinov va "
                "yechim fazolari bir xil. "
                "Turlicha bo'lsa — "
                "Petrov–Galerkin (konvektiv "
                "masalalarda zarur).\n\n"
                "**Simmetriya:** operator "
                "o'z-o'ziga qo'shma bo'lsa "
                "$\\mathbf{K}$ simmetrik va "
                "energiya minimumi mavjud. "
                "Konvektiv had bo'lsa "
                "simmetriya yo'qoladi."
            ),
            worked=WorkedExample(
                statement=(
                    "Sterjen: $L = 1$ m, "
                    "$EA = 1000$ N, bir tekis "
                    "yuklama $f = 100$ N/m, chap "
                    "uchi mahkamlangan, o'ng uchi "
                    "erkin. (a) Aniq yechimni "
                    "toping; (b) bitta chiziqli "
                    "element bilan FEM yechimini "
                    "qo'lda hisoblang; (c) "
                    "ikkita element bilan "
                    "takrorlang; (d) energiyani "
                    "taqqoslang."
                ),
                given=[
                    r"L = 1\ \text{m},\ EA = 1000\ "
                    r"\text{N},\ f = 100\ \text{N/m}",
                    r"u(0) = 0,\ N(L) = 0",
                ],
                steps=[
                    st(r"-EAu'' = f \;\Rightarrow\; "
                       r"u = \frac{f}{EA}\Big(Lx - "
                       r"\frac{x^2}{2}\Big)",
                       "Ikki marta integrallab, "
                       "shartlarni qo'ydik."),
                    st(r"u(L) = \frac{fL^2}{2EA} = "
                       r"\frac{100 \cdot 1}{2000} = "
                       r"0{,}05\ \text{m}",
                       "Uchining aniq ko'chishi."),
                    st(r"\Pi_{exact} = -\frac{1}{2}"
                       r"\int_0^L fu\,dx = "
                       r"-\frac{f^2L^3}{6EA} = "
                       r"-\frac{10^4}{6000} = "
                       r"-1{,}6667\ \text{J}",
                       "Aniq yechimda "
                       "$\\Pi = -\\frac12\\int fu$ "
                       "(Klapeyron teoremasi)."),
                    st(r"\text{(b) 1 element: } "
                       r"\varphi_1 = \frac{x}{L}, "
                       r"\quad \varphi_1' = "
                       r"\frac{1}{L}",
                       "Yagona erkin tugun — o'ng "
                       "uch. Chapda $u = 0$."),
                    st(r"K_{11} = \int_0^L EA"
                       r"\Big(\frac1L\Big)^2dx = "
                       r"\frac{EA}{L} = 1000",
                       "Bikrlik."),
                    st(r"f_1 = \int_0^L f\frac{x}{L}dx "
                       r"= \frac{fL}{2} = 50",
                       "Ekvivalent tugun kuchi — "
                       "yuklamaning yarmi."),
                    st(r"u_1 = \frac{50}{1000} = "
                       r"0{,}05\ \text{m}",
                       "**Aniq yechim bilan bir "
                       "xil!** Tugunda FEM aniq "
                       "javob berdi — bu "
                       "superkonvergensiya "
                       "hodisasi."),
                    st(r"\Pi_h = \frac12 K_{11}u_1^2 "
                       r"- f_1u_1 = \frac12(1000)"
                       r"(0{,}0025) - 50(0{,}05)",
                       "Diskret energiya."),
                    st(r"= 1{,}25 - 2{,}5 = "
                       r"-1{,}25\ \text{J} > "
                       r"-1{,}6667\ \text{J}",
                       "**$\\Pi_h > \\Pi_{exact}$** "
                       "— 12-qadamdagi bashorat "
                       "tasdiqlandi. FEM energiyani "
                       "to'liq ushlay olmadi."),
                    st(r"\text{(c) 2 element: } "
                       r"\mathbf{K} = \frac{EA}{h}"
                       r"\begin{bmatrix}2 & -1\\ "
                       r"-1 & 1\end{bmatrix}, \ "
                       r"h = 0{,}5",
                       "Ikkita erkin tugun "
                       "($x = 0{,}5$ va $x = 1$); "
                       "$EA/h = 2000$."),
                    st(r"\mathbf{f} = \begin{bmatrix}"
                       r"fh\\ fh/2\end{bmatrix} = "
                       r"\begin{bmatrix}50\\ "
                       r"25\end{bmatrix}",
                       "O'rta tugun ikkita "
                       "elementdan yarimtadan "
                       "oladi, oxirgisi bittadan."),
                    st(r"u_1 = 0{,}0375, \ u_2 = "
                       r"0{,}05 \;\Rightarrow\; "
                       r"\Pi_h = -1{,}5625\ \text{J}",
                       "Aniq qiymatlar: "
                       "$u(0{,}5) = 0{,}0375$ — "
                       "yana **aynan** to'g'ri. "
                       "Energiya esa "
                       "$-1{,}6667$ ga yaqinlashdi."),
                ],
                answer=(
                    "Aniq: $u(L) = 0{,}05$ m, "
                    "$\\Pi = -1{,}6667$ J. "
                    "1 element: $u_1 = 0{,}05$ m "
                    "(tugunda **aniq**), "
                    "$\\Pi_h = -1{,}25$ J. "
                    "2 element: tugun qiymatlari "
                    "yana aniq, "
                    "$\\Pi_h = -1{,}5625$ J. "
                    "Energiya har doim "
                    "$\\Pi_{exact}$ dan "
                    "**katta** va to'r "
                    "zichlashgani sari unga "
                    "quyidan yaqinlashadi."
                ),
                engineering_note=(
                    "Tugunlardagi qiymatlarning "
                    "aynan aniq chiqishi tasodif "
                    "emas — bu bir o'lchovli "
                    "masalalarda chiziqli "
                    "elementlar uchun ma'lum "
                    "natija (superkonvergensiya). "
                    "Uning sababi shundaki, "
                    "chiziqli elementlarning "
                    "ta'sir funksiyasi aynan "
                    "diskret Grin funksiyasiga "
                    "mos keladi. Lekin bu "
                    "**faqat tugunlarda** "
                    "o'rinli: element ichida "
                    "yechim chiziqli, aniq "
                    "yechim esa kvadratik, "
                    "demak u yerda xato bor. "
                    "Kuchlanish esa yanada "
                    "yomonroq: u element ichida "
                    "**doimiy**, aniq yechimda "
                    "esa chiziqli. Shuning uchun "
                    "FEM natijalarini o'qishda "
                    "tugun ko'chishlariga "
                    "ishonish mumkin, "
                    "kuchlanishlarga esa "
                    "ehtiyotkorlik bilan "
                    "qarash kerak — bu su-17 "
                    "dagi kuchlanishni tiklash "
                    "mavzusiga olib keladi. "
                    "Energiyaning quyidan "
                    "chegaralanishi esa amaliy "
                    "vosita: agar ikki xil to'rda "
                    "hisoblab energiyalarni "
                    "solishtirsangiz, ularning "
                    "farqi xatolikning bahosini "
                    "beradi va aniq yechim har "
                    "doim ikkalasidan ham "
                    "pastda yotadi."
                ),
            ),
            computation=Computation(
                caption=(
                    "Zaif formulirovkani amalga "
                    "oshirish, FEM ni chekli "
                    "ayirmalar va Ritz usullari "
                    "bilan taqqoslash, "
                    "energiyaning chegaralanishini "
                    "tekshirish."
                ),
                code='''"""FEM ning variatsion asosi: zaif shakl, Galerkin, energiya."""
import numpy as np
from labkit import PARAMS, note, series, table, value

L = float(PARAMS.get("L", 1.0))
EA = float(PARAMS.get("EA", 1000.0))
f0 = float(PARAMS.get("f0", 100.0))
n_show = int(PARAMS.get("n_show", 8))
load_type = int(PARAMS.get("load_type", 0))   # 0 doimiy, 1 chiziqli


def load(x):
    return f0*np.ones_like(x) if load_type == 0 else f0*x/L


def exact_u(x):
    if load_type == 0:
        return f0/EA*(L*x - x**2/2)
    return f0/(EA*L)*(L**2*x/2 - x**3/6)


def exact_strain(x):
    if load_type == 0:
        return f0/EA*(L - x)
    return f0/(EA*L)*(L**2/2 - x**2/2)


def exact_energy():
    # Pi = -1/2 * int(f*u) dx  (Klapeyron)
    xg = np.linspace(0, L, 20001)
    return -0.5*np.trapezoid(load(xg)*exact_u(xg), xg)


def fem_bar(n):
    """Chiziqli elementlar bilan sterjen; chap uch mahkamlangan."""
    h = L/n
    xn = np.linspace(0.0, L, n + 1)
    K = np.zeros((n + 1, n + 1))
    F = np.zeros(n + 1)
    ke = EA/h*np.array([[1.0, -1.0], [-1.0, 1.0]])
    for e in range(n):
        K[e:e+2, e:e+2] += ke
        # Ekvivalent tugun kuchlari: int(f * N_i) dx, 2 nuqtali Gauss
        gp = np.array([-1/np.sqrt(3), 1/np.sqrt(3)])
        for g in gp:
            N = np.array([(1 - g)/2, (1 + g)/2])
            xg = xn[e] + (1 + g)/2*h
            F[e:e+2] += load(np.array([xg]))[0]*N*(h/2)
    # Muhim shart: u(0) = 0
    Kr, Fr = K[1:, 1:], F[1:]
    ur = np.linalg.solve(Kr, Fr)
    u = np.concatenate([[0.0], ur])
    Pi = 0.5*u @ (K @ u) - u @ F
    return xn, u, K, F, Pi


def fd_bar(n):
    """Chekli ayirmalar: -EA*u'' = f, u(0) = 0, EA*u'(L) = 0."""
    h = L/n
    xn = np.linspace(0.0, L, n + 1)
    A = np.zeros((n + 1, n + 1))
    b = np.zeros(n + 1)
    A[0, 0] = 1.0
    for i in range(1, n):
        A[i, i-1], A[i, i], A[i, i+1] = -1.0, 2.0, -1.0
        b[i] = load(np.array([xn[i]]))[0]*h**2/EA
    # o'ng uch: soxta tugun orqali u'(L) = 0 -> u_{n+1} = u_{n-1}
    A[n, n-1], A[n, n] = -2.0, 2.0
    b[n] = load(np.array([xn[n]]))[0]*h**2/EA
    return xn, np.linalg.solve(A, b)


def ritz_poly(m):
    """Ritz usuli: global ko'phad bazis phi_j = x^j, j = 1..m."""
    Kr = np.zeros((m, m))
    Fr = np.zeros(m)
    xg = np.linspace(0, L, 4001)
    for i in range(m):
        for j in range(m):
            Kr[i, j] = np.trapezoid(EA*(i+1)*xg**i*(j+1)*xg**j, xg)
        Fr[i] = np.trapezoid(load(xg)*xg**(i+1), xg)
    a = np.linalg.solve(Kr, Fr)
    return a, 0.5*a @ (Kr @ a) - a @ Fr


Pi_ex = exact_energy()
value("Aniq uch ko'chishi u(L)", float(exact_u(np.array([L]))[0]), "m")
value("Aniq potensial energiya", Pi_ex, "J")

# --- (1) Bitta element: qo'lda hisob bilan tekshirish ---
xn1, u1, K1, F1, Pi1 = fem_bar(1)
value("1 element: K_11", float(K1[1, 1]), "N/m")
value("1 element: f_1", float(F1[1]), "N")
value("1 element: u_1", float(u1[1]), "m")
value("1 element: energiya", Pi1, "J")
value("1 element: uch ko'chishi xatosi",
      abs(u1[1] - exact_u(np.array([L]))[0])
      / exact_u(np.array([L]))[0]*100, "%")
note(f"Bitta element bilan K_11 = {K1[1,1]:.1f} N/m, ekvivalent tugun "
     f"kuchi {F1[1]:.1f} N va u_1 = {u1[1]:.6f} m. Aniq yechim "
     f"{exact_u(np.array([L]))[0]:.6f} m - TUGUNDA aynan mos "
     f"(superkonvergensiya). Qo'lda hisoblangan qiymatlar bilan "
     f"ham bir xil.")

# --- (2) ENERGIYANING QUYIDAN CHEGARALANISHI ---
rows, Pis, ns = [], [], []
for nk in [1, 2, 4, 8, 16, 32, 64]:
    xk, uk, Kk, Fk, Pik = fem_bar(nk)
    ue = exact_u(xk)
    e_u = np.max(np.abs(uk - ue))/np.max(np.abs(ue))
    Pis.append(Pik)
    ns.append(nk)
    rows.append([nk, f"{uk[-1]:.8f}", f"{e_u*100:.3e}", f"{Pik:.8f}",
                 f"{(Pik - Pi_ex):.3e}"])
table("FEM: to'r bo'yicha yaqinlashish va energiya",
      ["elementlar", "u(L)", "tugun xatosi, %", "Pi_h",
       "Pi_h - Pi_aniq"], rows)
above = all(pp >= Pi_ex - 1e-12 for pp in Pis)
value("Pi_h har doim Pi_aniq dan kattami", 1.0 if above else 0.0, "—")
value("Pi_h monoton kamayadimi",
      1.0 if all(Pis[i] >= Pis[i+1] - 1e-12
                 for i in range(len(Pis)-1)) else 0.0, "—")
series("Pi_h(elementlar soni)", [float(x) for x in ns], Pis,
       xlabel="elementlar soni", ylabel="Pi_h, J")
series("Aniq energiya", [float(x) for x in ns],
       [Pi_ex]*len(ns), xlabel="elementlar soni", ylabel="Pi_h, J")
note(f"Barcha to'rlarda Pi_h >= Pi_aniq = {Pi_ex:.6f} J va u to'r "
     f"zichlashgani sari MONOTON kamayib aniq qiymatga QUYIDAN "
     f"yaqinlashadi. Bu 12-qadamdagi nazariy bashoratning aniq "
     f"tasdig'i: diskret fazo haqiqiy fazoning qism fazosi, demak "
     f"minimum kattaroq bo'lishi SHART.")

# Energiya xatoligining tartibi
eP = [abs(pp - Pi_ex) for pp in Pis]
ordP = [np.log2(eP[i]/eP[i+1]) for i in range(len(eP) - 1)
        if eP[i+1] > 1e-14]
if ordP:
    value("Energiya xatoligining tartibi", float(np.mean(ordP[-3:])), "—")
    note(f"Energiya xatoligi to'r ikki barobar zichlashganda "
         f"{eP[-4]/eP[-3]:.2f} marta kamayadi (tartib "
         f"{np.mean(ordP[-3:]):.3f} ~ 2). Energiya normasidagi "
         f"xatolik O(h) bo'lgani uchun energiyaning o'zi O(h^2) - "
         f"bu klassik natija.")

# --- (3) FEM va CHEKLI AYIRMALAR: xato QAY TOMONGA? ---
# Diqqat: DOIMIY yuklamada aniq yechim KVADRAT ko'phad va uni
# ikkala usul ham aynan tiklaydi. Farqni ko'rish uchun CHIZIQLI
# yuklamani ham qo'shamiz - unda aniq yechim kubik bo'ladi.
_lt_saved = load_type
rows2 = []
for lt in [0, 1]:
    load_type = lt
    for nk in [2, 4, 8, 16]:
        xk, uk, _, _, _ = fem_bar(nk)
        xd, ud = fd_bar(nk)
        ue = exact_u(xk)
        e_fem = (uk[-1] - ue[-1])/ue[-1]*100
        e_fd = (ud[-1] - ue[-1])/ue[-1]*100
        rows2.append(["doimiy" if lt == 0 else "chiziqli", nk,
                      f"{e_fem:+.6f}", f"{e_fd:+.6f}"])
load_type = _lt_saved
table("FEM va chekli ayirmalar: uch ko'chishidagi xato, %",
      ["yuklama", "elementlar", "FEM xato, %", "CHA xato, %"], rows2)

load_type = 1
xk4, uk4, _, _, _ = fem_bar(4)
xd4, ud4 = fd_bar(4)
ue4 = exact_u(xk4)
e_fem4 = (uk4[-1] - ue4[-1])/ue4[-1]*100
e_fd4 = (ud4[-1] - ue4[-1])/ue4[-1]*100
load_type = _lt_saved
value("Chiziqli yuklama, 4 element: FEM xato", e_fem4, "%")
value("Chiziqli yuklama, 4 element: CHA xato", e_fd4, "%")
note(f"DOIMIY yuklamada ikkala usul ham aynan aniq: yechim kvadrat "
     f"ko'phad va uni ham uch nuqtali ikkinchi ayirma, ham chiziqli "
     f"element to'liq tiklaydi. CHIZIQLI yuklamada esa (yechim kubik) "
     f"ularning yo'llari ajraladi: 4 element bilan FEM xatosi "
     f"{e_fem4:+.2e} % - ya'ni HALI HAM aynan nol, chekli ayirmalar "
     f"xatosi esa {e_fd4:+.5f} %.")
note("Bu bir o'lchovli superkonvergensiyaning kuchli ko'rinishi: "
     "chiziqli elementlar TUGUNLARDA ixtiyoriy yuklama uchun aniq "
     "yechim beradi, chunki ularning ta'sir funksiyasi aynan diskret "
     "Grin funksiyasiga mos keladi. Chekli ayirmalarda bunday xossa "
     "yo'q - u faqat yechim sxema aniq tiklaydigan ko'phad bo'lganda "
     "aniq chiqadi.")
note("DIQQAT: bu tugun qiymatlariga tegishli. Element ICHIDA va "
     "ayniqsa kuchlanishda FEM ham xato qiladi (yuqoriga qarang), "
     "va energiya bo'yicha u har doim BIR TOMONGA xato qiladi: "
     "Pi_h >= Pi_aniq, ya'ni konstruksiya bikrroq ko'rinadi. "
     "Bu ikki o'lchovli masalalarda ko'chishda ham namoyon bo'ladi "
     "- u yerda superkonvergensiya yo'q.")

# --- (4) Element ichidagi xatolik: ko'chish va kuchlanish ---
xk, uk, _, _, _ = fem_bar(n_show)
h = L/n_show
xf = np.linspace(0, L, 601)
# FEM yechimini element ichida chiziqli interpolyatsiya qilamiz
u_fem = np.interp(xf, xk, uk)
u_ex = exact_u(xf)
# Kuchlanish: element ichida DOIMIY
eps_fem = np.zeros_like(xf)
for e in range(n_show):
    m = (xf >= xk[e]) & (xf <= xk[e+1])
    eps_fem[m] = (uk[e+1] - uk[e])/h
eps_ex = exact_strain(xf)
series("Ko'chish: FEM", xf.tolist(), (u_fem*1000).tolist(),
       xlabel="x, m", ylabel="u, mm")
series("Ko'chish: aniq", xf.tolist(), (u_ex*1000).tolist(),
       xlabel="x, m", ylabel="u, mm")
series("Deformatsiya: FEM (bo'lakli doimiy)", xf.tolist(),
       (eps_fem*1e6).tolist(), xlabel="x, m", ylabel="eps x 1e6")
series("Deformatsiya: aniq", xf.tolist(), (eps_ex*1e6).tolist(),
       xlabel="x, m", ylabel="eps x 1e6")
value("Ko'chishdagi maks xatolik (element ichida)",
      float(np.max(np.abs(u_fem - u_ex))/np.max(np.abs(u_ex))*100), "%")
value("Deformatsiyadagi maks xatolik",
      float(np.max(np.abs(eps_fem - eps_ex))/np.max(np.abs(eps_ex))*100),
      "%")
value("Tugunlardagi maks xatolik",
      float(np.max(np.abs(uk - exact_u(xk)))
            / np.max(np.abs(exact_u(xk)))*100), "%")
note(f"Tugunlarda xatolik amalda nol, element ICHIDA esa "
     f"{np.max(np.abs(u_fem-u_ex))/np.max(np.abs(u_ex))*100:.4f} %, "
     f"deformatsiyada (va demak kuchlanishda) "
     f"{np.max(np.abs(eps_fem-eps_ex))/np.max(np.abs(eps_ex))*100:.2f} % "
     f"ga chiqadi. Sababi: chiziqli element ichida deformatsiya "
     f"DOIMIY, aniq yechimda esa chiziqli. Shuning uchun FEM da "
     f"ko'chishga ishonish mumkin, kuchlanishni esa tiklash kerak "
     f"(su-17).")

# Element markazida kuchlanish ANIQ bo'lishini tekshirish
xm = (xk[:-1] + xk[1:])/2
eps_mid = (uk[1:] - uk[:-1])/h
err_mid = np.max(np.abs(eps_mid - exact_strain(xm))
                 / np.max(np.abs(exact_strain(xm))))
value("Element MARKAZIDAGI deformatsiya xatosi", float(err_mid*100), "%")
note(f"Element markazida deformatsiya xatosi atigi {err_mid*100:.3e} % - "
     f"ya'ni AYNAN aniq. Bu superkonvergensiya nuqtalari hodisasi: "
     f"chiziqli elementda deformatsiya element markazida aniq bo'ladi. "
     f"su-16 dagi Gauss nuqtalari aynan shu joylarga to'g'ri keladi.")

# --- (5) GALERKIN va RITZ bir xil natija beradimi? ---
rows3 = []
for mm in [1, 2, 3, 4]:
    a, Pi_r = ritz_poly(mm)
    u_r = sum(a[j]*L**(j+1) for j in range(mm))
    rows3.append([mm, f"{u_r:.8f}", f"{Pi_r:.8f}",
                  f"{(Pi_r - Pi_ex):.3e}"])
table("Ritz usuli (global ko'phad bazis)",
      ["hadlar soni", "u(L)", "Pi", "Pi - Pi_aniq"], rows3)
a2, Pi_r2 = ritz_poly(2)
note(f"Ritz usulida ham Pi >= Pi_aniq. IKKI HADLI ko'phad bazis "
     f"aniq yechimni AYNAN tiklaydi, chunki doimiy yuklamada aniq "
     f"yechim kvadratik ko'phad va u shu bazisda yotadi: "
     f"Pi - Pi_aniq = {Pi_r2 - Pi_ex:.3e}. Bazis aniq yechimni o'z "
     f"ichiga olsa, Ritz usuli uni AYNAN topadi.")
note("Galerkin (qoldiqni ortogonallash) va Ritz (energiyani "
     "minimallash) simmetrik masalada AYNAN bir xil tizimni beradi - "
     "10-qadamdagi da'vo. Farq faqat bazisda: FEM mahalliy "
     "funksiyalarni, Ritz esa global ko'phadlarni oladi.")

# --- (6) Qoldiqning ortogonalligini tekshirish ---
xk8, uk8, K8, F8, _ = fem_bar(8)
r8 = F8 - K8 @ uk8
# Tayanch reaksiyasi: (K u)_0 = F_0 + R  =>  R = (K u)_0 - F_0 = -r8[0]
R_sup = float((K8 @ uk8)[0] - F8[0])
value("Qoldiqning normasi (erkin tugunlarda)",
      float(np.linalg.norm(r8[1:])), "N")
value("Tayanch reaksiyasi R", R_sup, "N")
value("Umumiy tashqi yuklama", float(np.sum(F8)), "N")
value("Muvozanat qoldig'i R + sum(F)", float(R_sup + np.sum(F8)), "N")
note(f"Erkin tugunlarda qoldiq {np.linalg.norm(r8[1:]):.3e} N - ya'ni "
     f"nol: Galerkin sharti bajarilgan. Mahkamlangan tugunda esa "
     f"qoldiq TAYANCH REAKSIYASINI beradi: R = {R_sup:.4f} N. U "
     f"umumiy tashqi yuklama {np.sum(F8):.4f} N ni aynan "
     f"muvozanatlaydi: R + sum(F) = {R_sup + np.sum(F8):.3e} N. "
     f"Demak FEM global muvozanatni MASHINA ANIQLIGIDA saqlaydi.")

table("Kuchli va zaif formulirovkalarning taqqoslashi",
      ["Jihat", "Kuchli shakl", "Zaif shakl"],
      [["Hosila tartibi", "2 (yoki 4)", "1 (yoki 2)"],
       ["Silliqlik talabi", "u in C^2", "u in H^1"],
       ["Kuch sharti", "alohida qo'yiladi", "O'Z-O'ZIDAN kiradi"],
       ["Ko'chish sharti", "alohida", "bazisga kiritiladi"],
       ["Bazis", "global yoki to'r", "MAHALLIY bo'lishi mumkin"],
       ["Geometriya", "to'g'ri to'r kerak", "istalgan shakl"],
       ["Matritsa", "simmetrik emas ham", "Galerkinda simmetrik"]])
''',
                parameters=[
                    p("L", "Sterjen uzunligi L", 0.1, 10.0, 1.0, 0.1, "m"),
                    p("EA", "Bo'ylama bikrlik EA", 10.0, 1000000.0, 1000.0,
                      10.0, "N"),
                    p("f0", "Yuklama zichligi f₀", 1.0, 10000.0, 100.0, 1.0,
                      "N/m"),
                    p("n_show", "Elementlar soni", 2.0, 64.0, 8.0, 1.0),
                    p("load_type", "Yuklama (0 doimiy, 1 chiziqli)",
                      0.0, 1.0, 0.0, 1.0),
                ],
                expected_output=(
                    "Bitta element bilan "
                    "$K_{11} = 1000$ N/m, "
                    "$f_1 = 50$ N va "
                    "$u_1 = 0{,}05$ m — aniq "
                    "yechim bilan **aynan** mos "
                    "(superkonvergensiya). "
                    "$\\Pi_h$ barcha to'rlarda "
                    "$\\Pi_{aniq}$ dan katta va "
                    "monoton kamayib unga "
                    "quyidan yaqinlashadi, "
                    "xatolik $O(h^2)$. "
                    "Tugunlarda xatolik amalda "
                    "nol, element ichida esa "
                    "noldan farqli; "
                    "deformatsiya xatosi ancha "
                    "katta, lekin element "
                    "**markazida** u aynan "
                    "nolga teng. Erkin "
                    "tugunlardagi qoldiq nol "
                    "(Galerkin sharti), "
                    "mahkamlangan tugundagisi "
                    "esa tayanch reaksiyasini "
                    "beradi (−100 N) va umumiy "
                    "yuklamani mashina aniqligida "
                    "muvozanatlaydi. Doimiy "
                    "yuklamada FEM ham, chekli "
                    "ayirmalar ham aniq; "
                    "chiziqli yuklamada esa FEM "
                    "tugunlarda hali ham aynan "
                    "aniq, chekli ayirmalar xatosi "
                    "3,125 % ga chiqadi."
                ),
            ),
            visual=vis(
                kind="Zaif formulirovka va energiya minimumi",
                tool="React/SVG + Manim",
                description=(
                    "Sinov funksiyalari, FEM "
                    "yechimi va energiya "
                    "funksionalining minimumi."
                ),
                how_to_draw=(
                    "React/SVG: yuqorida sterjen "
                    "va uning ostida ikkita "
                    "chiziq — aniq yechim "
                    "(silliq parabola) va FEM "
                    "yechimi (bo'lakli-chiziqli "
                    "siniq chiziq). Tugunlar "
                    "yirik nuqtalar bilan "
                    "belgilanadi va ular aniq "
                    "chiziq ustida **aynan** "
                    "yotgani ko'rinadi — "
                    "superkonvergensiya shu "
                    "tarzda ko'z bilan "
                    "o'qiladi. Element ichida "
                    "esa ikki chiziq ajraladi "
                    "va orasidagi maydon "
                    "shtrixlanadi. Ostida "
                    "deformatsiya epyurasi: "
                    "aniq yechim chiziqli "
                    "pasayuvchi, FEM esa "
                    "**pog'onali** (bo'lakli "
                    "doimiy); har bir "
                    "pog'onaning o'rtasi aniq "
                    "chiziqni kesib o'tgani "
                    "belgilanadi — bu "
                    "superkonvergensiya "
                    "nuqtalari. Ikkinchi panel — "
                    "energiya: gorizontal o'qda "
                    "elementlar soni, vertikalda "
                    "$\\Pi_h$; nuqtalar yuqoridan "
                    "pastga tushib "
                    "$\\Pi_{aniq}$ gorizontal "
                    "chizig'iga yaqinlashadi, "
                    "lekin uni **hech qachon "
                    "kesib o'tmaydi** — bu "
                    "quyidan chegaralanishning "
                    "vizual isboti. Uchinchi "
                    "panel — bitta 'do'ppi' "
                    "bazis funksiyasi "
                    "$\\varphi_i$ va uning "
                    "hosilasi: birinchisi "
                    "uzluksiz, ikkinchisi "
                    "uzilishli — zaif "
                    "shaklning nima uchun "
                    "kerakligi shu yerda "
                    "ko'rinadi."
                ),
            ),
            interp=(
                "Kodning eng kuchli natijasi — "
                "energiyaning quyidan "
                "chegaralanishi. Barcha to'rlarda "
                "$\\Pi_h \\ge \\Pi_{aniq}$ va u "
                "monoton kamayib aniq qiymatga "
                "yaqinlashadi, lekin uni hech "
                "qachon kesib o'tmaydi. Bu "
                "12-qadamdagi nazariy da'voning "
                "aniq tasdig'i va u FEM ning "
                "eng qimmatli xossalaridan biri: "
                "usul har doim **bir tomonga** "
                "xato qiladi, demak natija "
                "ishonchli chegara beradi. "
                "Chekli ayirmalarda bunday "
                "kafolat yo'q. Ikkinchi natija "
                "— superkonvergensiya: tugun "
                "qiymatlari aynan aniq chiqadi. "
                "Bu bir o'lchovli masalalarga "
                "xos va uni umumlashtirib "
                "bo'lmaydi, lekin u muhim "
                "ogohlantirish bilan keladi: "
                "element **ichida** xato bor va "
                "deformatsiyada u ancha katta. "
                "Shuning uchun FEM natijalarini "
                "o'qishda ko'chish va kuchlanish "
                "turlicha ishonch darajasiga "
                "ega. Element markazidagi "
                "deformatsiyaning aynan aniq "
                "chiqishi esa alohida qimmatli: "
                "bu superkonvergensiya "
                "nuqtalari va ular su-16 dagi "
                "Gauss integrallash nuqtalari "
                "bilan ustma-ust tushadi. "
                "Shuning uchun FEM paketlari "
                "kuchlanishni aynan Gauss "
                "nuqtalarida hisoblab, keyin "
                "tugunlarga ekstrapolyatsiya "
                "qiladi. Nihoyat, qoldiq "
                "tekshiruvi ikki narsani "
                "ko'rsatadi: erkin tugunlarda "
                "u nol (Galerkin sharti), "
                "mahkamlangan tugunda esa u "
                "**reaksiya** bo'lib chiqadi "
                "va umumiy yuklamani aynan "
                "muvozanatlaydi. Ya'ni FEM "
                "muvozanatni global miqyosda "
                "aynan saqlaydi — bu usulning "
                "fizik ishonchliligining muhim "
                "belgisi."
            ),
            mistakes=[
                "Zaif formulirovkani 'taqribiy' "
                "deb hisoblash. U kuchli shaklga "
                "**ekvivalent** (silliq yechim "
                "uchun); taqribiylik faqat "
                "diskretlashtirishdan keladi.",
                "Kuch chegaraviy shartini "
                "alohida qo'yish. U zaif shaklda "
                "o'z-o'zidan paydo bo'ladi; "
                "majburan qo'yish ikki marta "
                "hisoblashga olib keladi.",
                "Sinov funksiyasini muhim "
                "chegarada noldan farqli olish. "
                "$v \\in V_0$ sharti buziladi va "
                "tizim noto'g'ri chiqadi.",
                "Kuchlanishni tugunlarda "
                "bevosita o'qish. Chiziqli "
                "elementda u element ichida "
                "doimiy; Gauss nuqtalarida "
                "hisoblab ekstrapolyatsiya "
                "qilish kerak.",
                "FEM ni 'aniqroq chekli "
                "ayirmalar' deb qarash. Ular "
                "turli asosga ega: FEM "
                "variatsion, chekli ayirmalar "
                "esa Teylor qatoriga tayanadi.",
            ],
            quiz=[
                q("Zaif formulirovkaning asosiy "
                  "yutug'i nima?",
                  "Bo'laklab integrallash "
                  "hosilani sinov funksiyasiga "
                  "o'tkazadi va yechimga "
                  "qo'yilgan silliqlik talabini "
                  "pasaytiradi — shu sababli "
                  "bo'lakli-chiziqli bazis "
                  "ishlatish mumkin.",
                  "konseptual"),
                q("Muhim va tabiiy chegaraviy "
                  "shartlar nima bilan farq "
                  "qiladi?",
                  "Muhim (ko'chish) bazisga "
                  "majburan kiritiladi; tabiiy "
                  "(kuch) zaif shaklda "
                  "bo'laklab integrallashning "
                  "chegara hadi sifatida "
                  "o'z-o'zidan paydo bo'ladi.",
                  "konseptual"),
                q("Bitta chiziqli element bilan "
                  "$EA = 1000$ N, $L = 1$ m, "
                  "$f = 100$ N/m uchun $u(L)$ "
                  "qancha?",
                  "$K_{11} = EA/L = 1000$, "
                  "$f_1 = fL/2 = 50$, "
                  "$u_1 = 0{,}05$ m — aniq "
                  "yechim bilan bir xil.",
                  "hisob"),
                q("Kodda nima uchun $\\Pi_h$ "
                  "ning $\\Pi_{aniq}$ dan "
                  "kattaligi tekshiriladi?",
                  "Diskret fazo haqiqiy fazoning "
                  "qism fazosi, demak minimum "
                  "kattaroq bo'lishi shart. Bu "
                  "FEM ning bir tomonga xato "
                  "qilishini kafolatlaydi.",
                  "kod"),
                q("Nima uchun FEM konstruksiyani "
                  "bikrroq ko'rsatadi?",
                  "U energiyani quyidan "
                  "chegaralaydi: diskret fazoda "
                  "erishish mumkin bo'lgan "
                  "minimal energiya haqiqiy "
                  "minimumdan katta, demak "
                  "og'ish kamroq chiqadi.",
                  "talqin"),
                q("Galerkin va Ritz usullari "
                  "qanday bog'langan?",
                  "Simmetrik musbat aniqlangan "
                  "masalada ular **aynan bir "
                  "xil** tizimni beradi: "
                  "energiyaning variatsiyasi "
                  "aynan zaif shakl.", "talqin"),
            ],
            bridge=(
                "Zaif formulirovka bazisning "
                "mahalliy bo'lishiga ruxsat "
                "berdi, lekin biz hali faqat eng "
                "sodda 'do'ppi' funksiyalarni "
                "ishlatdik. Keyingi mavzuda shakl "
                "funksiyalarini tizimli quramiz: "
                "yuqori tartibli elementlar, "
                "ikki va uch o'lchovli elementlar "
                "hamda izoparametrik "
                "almashtirish — aynan u FEM ni "
                "istalgan egri geometriyaga "
                "moslashtiradi."
            ),
            research=(
                "Variatsion asoslarni "
                "chuqurlashtiring. "
                "(1) Petrov–Galerkin usullarini "
                "o'rganing: sinov va vazn "
                "funksiyalari turlicha "
                "bo'lganda matritsa simmetriyasi "
                "yo'qoladi — konvektiv "
                "masalalarda (SUPG) bu nima "
                "uchun zarur? (2) Aralash "
                "(mixed) formulirovkalarni "
                "tahlil qiling: siqilmaydigan "
                "materiallarda ko'chish va "
                "bosim alohida noma'lum "
                "sifatida olinadi; inf-sup "
                "(LBB) sharti nima va u nima "
                "uchun zarur? (3) Laks–Milgram "
                "teoremasini va uning "
                "mexanikadagi ma'nosini "
                "o'rganing: majburiylik "
                "(coercivity) konstruksiyaning "
                "yetarlicha mahkamlanganiga "
                "qanday bog'langan?"
            ),
            manim_ref=manim(
                scene="WeakFormScene",
                module="manim/scenes/su_fem.py",
                title="Zaif formulirovka va bazis funksiyalari",
                summary=(
                    "Kuchli shakldagi tenglama "
                    "sinov funksiyasiga "
                    "ko'paytiriladi va bo'laklab "
                    "integrallash animatsiyasi "
                    "ko'rsatiladi: hosila "
                    "belgisi $u$ dan $v$ ga "
                    "'sakraydi' va chegara hadi "
                    "ajralib chiqadi. Keyin "
                    "bo'lakli-chiziqli bazis "
                    "funksiyalari qo'yiladi va "
                    "ularning yig'indisi aniq "
                    "yechimga yaqinlashishi "
                    "namoyish etiladi."
                ),
            ),
        ),
    ),

    # ------------------------------------------------------------------ su-14
    Topic(
        id="su-14",
        subject_id=S, module_id=M, order=14,
        title="Shakl funksiyalari va izoparametrik elementlar",
        description=(
            "Lagranj shakl funksiyalari, to'liqlik va moslik talablari, "
            "tabiiy koordinatalar, izoparametrik almashtirish va Yakobian "
            "matritsasi."
        ),
        learning_objective=(
            "Ixtiyoriy tartibli shakl funksiyalarini qurish, ularning "
            "yaqinlashish talablarini tekshirish va izoparametrik "
            "almashtirish orqali egri elementni qurish."
        ),
        prerequisites=["su-13"],
        mathematical_core=(
            "$N_i(\\xi_j) = \\delta_{ij}$, $\\sum_i N_i = 1$; "
            "izoparametrik: $x = \\sum N_i x_i$, "
            "$J = \\partial x/\\partial\\xi$, "
            "$\\mathbf{B} = \\mathbf{J}^{-1}\\partial\\mathbf{N}/"
            "\\partial\\boldsymbol\\xi$."
        ),
        engineering_application=(
            "Egri chegarali detallar, galtellar, teshiklar atrofidagi "
            "to'r, qobiq elementlari — barcha zamonaviy FEM "
            "paketlarining asosi."
        ),
        computational_component=(
            "Shakl funksiyalarini qurish va tekshirish, Yakobianning "
            "buzilishini o'lchash, element sifatining natijaga "
            "ta'sirini baholash."
        ),
        visualization_component=(
            "Shakl funksiyalarining grafigi, izoparametrik "
            "almashtirish, buzilgan elementdagi Yakobian xaritasi."
        ),
        research_extension=(
            "Ierarxik (p-tipdagi) shakl funksiyalarini o'rganing: "
            "ular tartibni oshirishda oldingi bazisni saqlaydi — "
            "bu adaptivlikda nima uchun afzal?"
        ),
        difficulty="murakkab",
        previous_link=(
            "su-13 da zaif formulirovka bazisning mahalliy va "
            "bo'lakli-ko'phad bo'lishiga ruxsat berdi. Endi shu "
            "bazisni tizimli quramiz va uni egri geometriyaga "
            "moslashtiramiz — aynan shu FEM ni chekli ayirmalardan "
            "ustun qiladi."
        ),
        next_topic="su-15",
        estimated_minutes=90,
        tags=["shakl funksiyasi", "izoparametrik", "Yakobian", "Lagranj"],
        lesson=_lesson(
            problem=(
                "Kuchlanish konsentratsiyasini "
                "hisoblash kerak: plastinadagi "
                "doiraviy teshik atrofida "
                "(tmm-17 dagi Kirsh masalasi). "
                "Teshik chegarasi — aylana. "
                "To'g'ri chiziqli elementlar bilan "
                "uni qoplasak, chegara ko'pburchak "
                "bo'lib qoladi va har bir "
                "burchakda soxta kuchlanish "
                "konsentratsiyasi paydo bo'ladi — "
                "aynan biz o'lchamoqchi bo'lgan "
                "kattalik buziladi. To'rni "
                "zichlashtirish yordam beradi, "
                "lekin sekin: xato "
                "$O(h)$ bo'lib qoladi. Kerak "
                "bo'lgan narsa — chegarasi "
                "**egri** bo'lgan element. Uni "
                "qanday qurish mumkin va ayni "
                "paytda integrallashni qanday "
                "sodda saqlash mumkin?"
            ),
            concepts=[
                c("Shakl funksiyasi $N_i$",
                  "$N_i(\\xi_j) = \\delta_{ij}$ — "
                  "o'z tugunida 1, qolganlarida 0; "
                  "tugun qiymatini element ichiga "
                  "interpolyatsiya qiladi."),
                c("To'liqlik (completeness)",
                  "$\\sum_i N_i = 1$ va bazis "
                  "chiziqli ko'phadlarni aynan "
                  "ifodalay olishi kerak — qattiq "
                  "jism harakati va doimiy "
                  "deformatsiya uchun."),
                c("Moslik (compatibility, $C^0$)",
                  "Qo'shni elementlar chegarasida "
                  "ko'chish uzluksiz bo'lishi "
                  "kerak; aks holda 'yoriq' "
                  "paydo bo'ladi."),
                c("Tabiiy koordinatalar $\\xi$",
                  "Etalon element "
                  "$[-1, 1]$ da aniqlanadi; "
                  "barcha elementlar bir xil "
                  "formuladan olinadi."),
                c("Izoparametrik almashtirish",
                  "Geometriya **va** ko'chish bir "
                  "xil shakl funksiyalari bilan "
                  "ifodalanadi: "
                  "$x = \\sum N_ix_i$, "
                  "$u = \\sum N_iu_i$."),
                c("Yakobian $J$",
                  "$J = \\partial x/\\partial\\xi$ — "
                  "etalon va haqiqiy element "
                  "orasidagi cho'zilish; "
                  "$\\det J > 0$ bo'lishi shart."),
            ],
            derivation=[
                d("1. Lagranj shakl funksiyalari",
                  r"N_i(\xi) = \prod_{j \ne i}"
                  r"\frac{\xi - \xi_j}{\xi_i - \xi_j}",
                  "Klassik interpolyatsiya "
                  "ko'phadlari. Ular avtomatik "
                  "ravishda "
                  "$N_i(\\xi_j) = \\delta_{ij}$ "
                  "shartini qanoatlantiradi."),
                d("2. Chiziqli element (2 tugun)",
                  r"N_1 = \frac{1-\xi}{2}, \quad "
                  r"N_2 = \frac{1+\xi}{2}, \quad "
                  r"\xi \in [-1, 1]",
                  "Eng sodda element. "
                  "$N_1 + N_2 = 1$ — to'liqlik "
                  "sharti bajarilgan."),
                d("3. Kvadratik element (3 tugun)",
                  r"N_1 = \frac{\xi(\xi-1)}{2}, \ "
                  r"N_2 = 1-\xi^2, \ "
                  r"N_3 = \frac{\xi(\xi+1)}{2}",
                  "O'rta tugun qo'shildi. Endi "
                  "element ichida ko'chish "
                  "kvadratik, deformatsiya esa "
                  "chiziqli — su-13 dagi asosiy "
                  "kamchilik yumshatiladi."),
                d("4. To'liqlik shartining ma'nosi",
                  r"u = a + bx \;\Longrightarrow\; "
                  r"\text{bazis uni AYNAN "
                  r"ifodalashi kerak}",
                  "**Zarur shart.** $a$ — qattiq "
                  "jism ko'chishi (deformatsiyasiz), "
                  "$bx$ — doimiy deformatsiya. "
                  "Agar element bularni aynan "
                  "ifodalay olmasa, to'r "
                  "zichlashganda ham "
                  "yaqinlashmaydi."),
                d("5. Yig'indi sharti",
                  r"\sum_i N_i(\xi) = 1 \quad "
                  r"\forall \xi",
                  "Qattiq jism ko'chishi "
                  "$u = a$ uchun: "
                  "$u_h = \\sum N_i a = "
                  "a\\sum N_i = a$ — faqat "
                  "yig'indi 1 bo'lsa. Bu eng "
                  "sodda, lekin eng muhim "
                  "tekshiruv."),
                d("6. Izoparametrik g'oya",
                  r"x(\xi) = \sum_i N_i(\xi)x_i, "
                  r"\qquad u(\xi) = \sum_i "
                  r"N_i(\xi)u_i",
                  "**Hal qiluvchi qadam.** Bir "
                  "xil funksiyalar ikkala vazifani "
                  "bajaradi. Kvadratik shakl "
                  "funksiyalari bilan element "
                  "chegarasi **parabola** bo'ladi "
                  "— egri chegara shundan."),
                d("7. Yakobian",
                  r"J = \frac{dx}{d\xi} = \sum_i "
                  r"\frac{dN_i}{d\xi}x_i",
                  "Etalon elementdan haqiqiy "
                  "elementga o'tishdagi cho'zilish. "
                  "Chiziqli elementda "
                  "$J = h/2$ — doimiy."),
                d("8. Hosilalarni almashtirish",
                  r"\frac{dN_i}{dx} = "
                  r"\frac{dN_i}{d\xi}\cdot"
                  r"\frac{d\xi}{dx} = "
                  r"\frac{1}{J}\frac{dN_i}{d\xi}",
                  "Deformatsiya matritsasi "
                  "$\\mathbf{B}$ aynan shu "
                  "hosilalardan quriladi. "
                  "$J$ nolga teng bo'lsa — "
                  "falokat."),
                d("9. Integrallashning "
                  "almashtirilishi",
                  r"\int_{x_1}^{x_2}(\cdot)\,dx = "
                  r"\int_{-1}^{1}(\cdot)\,J\,d\xi",
                  "**Katta qulaylik.** Barcha "
                  "integrallar bir xil "
                  "$[-1,1]$ oralig'ida "
                  "hisoblanadi — Gauss "
                  "kvadraturasi (su-16) shundan "
                  "kelib chiqadi."),
                d("10. Ikki o'lchovli element",
                  r"N_i(\xi,\eta) = \frac14"
                  r"(1+\xi\xi_i)(1+\eta\eta_i), "
                  r"\quad i = 1..4",
                  "To'rt tugunli element (Q4). "
                  "Bir o'lchovli funksiyalarning "
                  "ko'paytmasi — 'tenzor "
                  "ko'paytma' bazis."),
                d("11. Ikki o'lchovli Yakobian",
                  r"\mathbf{J} = \begin{bmatrix}"
                  r"\partial x/\partial\xi & "
                  r"\partial y/\partial\xi\\ "
                  r"\partial x/\partial\eta & "
                  r"\partial y/\partial\eta"
                  r"\end{bmatrix}, \quad "
                  r"dA = \det\mathbf{J}\,d\xi\,d\eta",
                  "$2\\times2$ matritsa. "
                  "$\\det\\mathbf{J}$ — yuza "
                  "nisbati."),
                d("12. Element sifatining mezoni",
                  r"\det\mathbf{J} > 0 \ \text{hamma "
                  r"joyda}; \quad \frac{\max\det"
                  r"\mathbf{J}}{\min\det\mathbf{J}} "
                  r"\ \text{kichik bo'lsin}",
                  "**Amaliy mezon.** "
                  "$\\det\\mathbf{J} \\le 0$ "
                  "bo'lsa element 'ag'darilgan' "
                  "va hisob ma'nosiz. Nisbat "
                  "katta bo'lsa element cho'zilgan "
                  "va aniqlik tushadi."),
                d("13. Q4 elementning cheklovi",
                  r"u = \alpha_0 + \alpha_1\xi + "
                  r"\alpha_2\eta + \alpha_3\xi\eta",
                  "Q4 bazisi to'liq kvadratik "
                  "emas: unda $\\xi^2$ va "
                  "$\\eta^2$ yo'q, lekin "
                  "$\\xi\\eta$ bor. Shuning uchun "
                  "u sof egilishni yomon "
                  "ifodalaydi — bu su-16 dagi "
                  "qulflanish muammosining "
                  "manbasi."),
            ],
            meaning=(
                "Izoparametrik g'oya 6-qadamda va "
                "u FEM ning muhandislikdagi "
                "hukmronligini tushuntiradi. "
                "Fikr sodda: geometriyani ham, "
                "noma'lum maydonni ham "
                "**bir xil** funksiyalar bilan "
                "ifodalash. Natijada kvadratik "
                "shakl funksiyalari bilan element "
                "chegarasi parabolaga aylanadi va "
                "aylanani ancha yaxshi "
                "yaqinlashtiradi. Teshik atrofida "
                "endi soxta burchaklar yo'q. "
                "Bundan ham muhimi — 9-qadamdagi "
                "qulaylik: barcha integrallar "
                "etalon elementda, bir xil "
                "$[-1,1]$ oralig'ida hisoblanadi. "
                "Element qanchalik egri va "
                "buzilgan bo'lmasin, kod bir xil "
                "qoladi; butun geometrik "
                "murakkablik Yakobianga "
                "to'planadi. Bu dasturlash "
                "nuqtai nazaridan hal qiluvchi: "
                "bitta element kodi million "
                "turli shakldagi elementga "
                "yaraydi. To'liqlik va moslik "
                "shartlari (4- va 5-qadamlar) "
                "esa yaqinlashishning "
                "kafolatidir. Ular intuitiv: "
                "element kamida qattiq jism "
                "harakatini va doimiy "
                "deformatsiyani aynan ifodalay "
                "olishi kerak. Agar shunday "
                "bo'lmasa, to'rni qancha "
                "zichlashtirmang, yechim aniq "
                "javobga yaqinlashmaydi — chunki "
                "eng sodda holatni ham to'g'ri "
                "bera olmaydi. "
                "$\\sum N_i = 1$ tekshiruvi bir "
                "qator kod, lekin u butun "
                "elementning yaroqliligini "
                "aniqlaydi va har qanday yangi "
                "element yozilganda birinchi "
                "bajariladigan test bo'lishi "
                "kerak. Yakobian esa amaliy "
                "jihatdan eng ko'p muammo "
                "keltiradigan joy. "
                "$\\det\\mathbf{J} \\le 0$ — "
                "element ag'darilgan degani va "
                "bu to'r generatori xatosining "
                "eng keng tarqalgan ko'rinishi. "
                "FEM paketlari buni tekshiradi "
                "va 'distorted element' "
                "ogohlantirishini beradi. Nihoyat "
                "13-qadam muhim ogohlantirish: "
                "Q4 elementning bazisi to'liq "
                "kvadratik emas. U sof egilishni "
                "ifodalay olmaydi va bu keyingi "
                "mavzudagi qulflanish "
                "muammosining ildizi."
            ),
            equations=[
                eq(r"N_i(\xi_j) = \delta_{ij}, \qquad "
                   r"\sum_i N_i(\xi) = 1",
                   "Shakl funksiyalarining "
                   "asosiy xossalari.",
                   "Shakl funksiyalari"),
                eq(r"x = \sum_i N_i(\xi)\,x_i, \qquad "
                   r"u = \sum_i N_i(\xi)\,u_i",
                   "Izoparametrik almashtirish — "
                   "geometriya va maydon bir xil "
                   "bazisda.", "Izoparametrik"),
                eq(r"\frac{dN_i}{dx} = "
                   r"\frac{1}{J}\frac{dN_i}{d\xi}, "
                   r"\qquad \int_{x_1}^{x_2}dx = "
                   r"\int_{-1}^{1}J\,d\xi",
                   "Yakobian orqali hosila va "
                   "integralning almashtirilishi.",
                   "Yakobian almashtirish"),
                eq(r"\det\mathbf{J} > 0 \ "
                   r"\text{hamma joyda}",
                   "Element yaroqliligining "
                   "majburiy sharti.",
                   "Element sifati"),
            ],
            conditions=(
                "**Yaqinlashish uchun zarur "
                "shartlar:**\n"
                "1. **To'liqlik:** element "
                "qattiq jism harakatini va "
                "doimiy deformatsiyani aynan "
                "ifodalay olsin "
                "($\\sum N_i = 1$ va chiziqli "
                "hadlar bazisda);\n"
                "2. **Moslik ($C^0$):** "
                "elementlar chegarasida ko'chish "
                "uzluksiz. Plastina "
                "elementlarida $C^1$ kerak — "
                "bu ancha qiyin (pq-24).\n\n"
                "**Yakobian bo'yicha:**\n"
                "- $\\det\\mathbf{J} > 0$ barcha "
                "integrallash nuqtalarida — "
                "majburiy;\n"
                "- $\\max/\\min$ nisbati < 5–10 "
                "— tavsiya;\n"
                "- Burchak 45°–135° oralig'ida;\n"
                "- Tomonlar nisbati (aspect "
                "ratio) < 5 (kuchlanish uchun), "
                "< 20 (ko'chish uchun).\n\n"
                "**O'rta tugun joylashuvi:** "
                "kvadratik elementda o'rta "
                "tugun chekkaning o'rtasidan "
                "chorak uzunlikdan ko'p "
                "siljimasin, aks holda element "
                "ichida $\\det\\mathbf{J}$ "
                "ishorasini o'zgartiradi.\n\n"
                "**Maxsus hol:** chorak nuqtali "
                "(quarter-point) element — o'rta "
                "tugun ataylab chorakka "
                "siljitiladi va "
                "$1/\\sqrt{r}$ singulyarligi "
                "hosil qilinadi; yorilish "
                "mexanikasida ishlatiladi "
                "(tmm-24)."
            ),
            worked=WorkedExample(
                statement=(
                    "(a) Uch tugunli kvadratik "
                    "elementning shakl "
                    "funksiyalarini yozing va "
                    "$\\sum N_i = 1$ ni "
                    "tekshiring; (b) tugunlari "
                    "$x = \\{0, 0{,}5, 2\\}$ "
                    "bo'lgan element uchun "
                    "Yakobianni toping va "
                    "yaroqliligini baholang; "
                    "(c) o'rta tugun qayerdan "
                    "boshlab elementni "
                    "buzadi?"
                ),
                given=[
                    r"N_1 = \tfrac{\xi(\xi-1)}{2}, \ "
                    r"N_2 = 1-\xi^2, \ "
                    r"N_3 = \tfrac{\xi(\xi+1)}{2}",
                    r"x_1 = 0,\ x_2 = 0{,}5,\ x_3 = 2",
                ],
                steps=[
                    st(r"\sum N_i = \frac{\xi^2-\xi}{2} "
                       r"+ 1 - \xi^2 + "
                       r"\frac{\xi^2+\xi}{2}",
                       "Uchta hadni qo'shamiz."),
                    st(r"= \frac{\xi^2-\xi+\xi^2+\xi}{2} "
                       r"+ 1 - \xi^2 = \xi^2 + 1 - "
                       r"\xi^2 = 1 \quad \checkmark",
                       "**To'liqlik sharti "
                       "bajarildi** — har qanday "
                       "$\\xi$ uchun."),
                    st(r"N_1(-1) = \frac{(-1)(-2)}{2} "
                       r"= 1, \ N_2(-1) = 0, \ "
                       r"N_3(-1) = 0 \quad \checkmark",
                       "$\\delta_{ij}$ xossasi "
                       "birinchi tugunda "
                       "tekshirildi."),
                    st(r"\text{(b) } \frac{dN_1}{d\xi} "
                       r"= \xi - \tfrac12, \ "
                       r"\frac{dN_2}{d\xi} = -2\xi, \ "
                       r"\frac{dN_3}{d\xi} = "
                       r"\xi + \tfrac12",
                       "Hosilalar."),
                    st(r"J(\xi) = \sum\frac{dN_i}"
                       r"{d\xi}x_i = 0 + "
                       r"(-2\xi)(0{,}5) + "
                       r"(\xi+\tfrac12)(2)",
                       "$x_1 = 0$ bo'lgani uchun "
                       "birinchi had tushdi."),
                    st(r"= -\xi + 2\xi + 1 = "
                       r"\xi + 1",
                       "Yakobian $\\xi$ ga "
                       "**chiziqli** bog'liq — "
                       "o'rta tugun markazda "
                       "emasligi shundan."),
                    st(r"J(-1) = 0, \quad J(0) = 1, "
                       r"\quad J(+1) = 2",
                       "**$J(-1) = 0$** — element "
                       "chap uchida "
                       "singulyar! Bu chegaraviy "
                       "holat."),
                    st(r"\text{(c) o'rta tugun } "
                       r"x_2 = \alpha \cdot 2: \ "
                       r"J = \sum\frac{dN_i}{d\xi}x_i "
                       r"= (\xi+\tfrac12)(2) - "
                       r"2\xi\alpha \cdot 2",
                       "Umumiy holat: $x_3 = 2$ "
                       "qat'iy, $x_2 = 2\\alpha$."),
                    st(r"J = 2\xi + 1 - 4\alpha\xi = "
                       r"1 + 2\xi(1 - 2\alpha)",
                       "$\\alpha = 1/2$ (markaz) "
                       "bo'lsa $J = 1$ — doimiy va "
                       "ideal."),
                    st(r"J(-1) = 1 - 2(1-2\alpha) = "
                       r"4\alpha - 1 > 0 "
                       r"\;\Rightarrow\; \alpha > "
                       r"\frac14",
                       "**Chorak qoidasi.** O'rta "
                       "tugun chekkaning chorak "
                       "nuqtasidan tashqariga "
                       "chiqsa, $J$ ishorasini "
                       "o'zgartiradi."),
                    st(r"\text{Shu masalada } "
                       r"\alpha = \frac{0{,}5}{2} = "
                       r"\frac14 \;\Rightarrow\; "
                       r"J(-1) = 0",
                       "Element aynan chegarada — "
                       "bu **chorak nuqtali "
                       "element** va u yorilish "
                       "mexanikasida ataylab "
                       "ishlatiladi: "
                       "$1/\\sqrt{r}$ "
                       "singulyarligini hosil "
                       "qiladi (tmm-24)."),
                ],
                answer=(
                    "(a) $\\sum N_i = 1$ aynan "
                    "bajariladi va "
                    "$N_i(\\xi_j) = \\delta_{ij}$ "
                    "ham. (b) $J(\\xi) = \\xi + 1$: "
                    "$J(-1) = 0$, $J(0) = 1$, "
                    "$J(1) = 2$ — element chap "
                    "uchida singulyar. (c) O'rta "
                    "tugun chekkaning "
                    "**chorak nuqtasidan** "
                    "tashqariga chiqsa "
                    "($\\alpha < 1/4$) Yakobian "
                    "ishorasini o'zgartiradi. "
                    "Berilgan element aynan shu "
                    "chegarada — bu ataylab "
                    "qurilgan chorak nuqtali "
                    "element."
                ),
                engineering_note=(
                    "Chorak qoidasi FEM "
                    "amaliyotidagi eng aniq "
                    "sonli mezonlardan biri va "
                    "to'r generatorlari uni "
                    "tekshiradi. Odatda u "
                    "cheklov sifatida qaraladi: "
                    "o'rta tugunni chorakdan "
                    "nariga siljitmang. Lekin "
                    "yorilish mexanikasida u "
                    "**imkoniyat**: o'rta tugunni "
                    "ataylab aynan chorak "
                    "nuqtaga qo'yib, "
                    "$1/\\sqrt{r}$ "
                    "singulyarligini hosil "
                    "qilish mumkin. Bu aynan "
                    "yorilish uchida kutilgan "
                    "kuchlanish maydoni "
                    "(tmm-24 dagi $K_I$), "
                    "shuning uchun bunday "
                    "element yorilish uchini "
                    "juda samarali "
                    "modellashtiradi — to'rni "
                    "zichlashtirmasdan. Bu "
                    "izoparametrik g'oyaning "
                    "kutilmagan foydasi: "
                    "geometriyani buzish orqali "
                    "kerakli matematik "
                    "xatti-harakatni qurish "
                    "mumkin. Amaliy jihatdan "
                    "esa yana bir maslahat: FEM "
                    "hisobidan keyin element "
                    "sifati hisobotini "
                    "albatta ko'ring. "
                    "$\\det\\mathbf{J}$ nolga "
                    "yaqin elementlar "
                    "kuchlanish natijalarini "
                    "buzadi va ular odatda "
                    "murakkab geometriyaning "
                    "o'tkir burchaklarida "
                    "to'planadi."
                ),
            ),
            computation=Computation(
                caption=(
                    "Shakl funksiyalarini qurish "
                    "va tekshirish, Yakobianni "
                    "hisoblash, element "
                    "buzilishining aniqlikka "
                    "ta'sirini o'lchash."
                ),
                code='''"""Shakl funksiyalari va izoparametrik elementlar."""
import numpy as np
from labkit import PARAMS, note, series, table, value

p_ord = int(PARAMS.get("p_ord", 2))       # element tartibi
alpha = float(PARAMS.get("alpha", 0.5))   # o'rta tugun joyi (0..1)
skew = float(PARAMS.get("skew", 0.0))     # Q4 tugunini ichkariga tortish
L_el = float(PARAMS.get("L_el", 2.0))


def lagrange_N(xi, nodes):
    """Lagranj shakl funksiyalari va ularning hosilalari."""
    n = len(nodes)
    xi = np.asarray(xi, dtype=float)
    N = np.ones((n,) + xi.shape)
    dN = np.zeros((n,) + xi.shape)
    for i in range(n):
        for j in range(n):
            if j == i:
                continue
            N[i] *= (xi - nodes[j])/(nodes[i] - nodes[j])
        # hosila: ko'paytma qoidasi bo'yicha yig'indi
        for j in range(n):
            if j == i:
                continue
            term = np.ones_like(xi)
            for k in range(n):
                if k == i or k == j:
                    continue
                term *= (xi - nodes[k])/(nodes[i] - nodes[k])
            dN[i] += term/(nodes[i] - nodes[j])
    return N, dN


# --- (1) Shakl funksiyalarini qurish va TEKSHIRISH ---
rows = []
for order in [1, 2, 3, 4]:
    nodes = np.linspace(-1.0, 1.0, order + 1)
    xi = np.linspace(-1.0, 1.0, 501)
    N, dN = lagrange_N(xi, nodes)
    # (a) delta xossasi
    Nn, _ = lagrange_N(nodes, nodes)
    delta_err = np.max(np.abs(Nn - np.eye(order + 1)))
    # (b) birlik yig'indi
    sum_err = np.max(np.abs(np.sum(N, axis=0) - 1.0))
    # (c) hosilalar yig'indisi nol
    dsum_err = np.max(np.abs(np.sum(dN, axis=0)))
    # (d) chiziqli funksiyani aynan tiklash
    lin = np.sum(N*nodes[:, None], axis=0) - xi
    lin_err = np.max(np.abs(lin))
    rows.append([order, order + 1, f"{delta_err:.2e}", f"{sum_err:.2e}",
                 f"{dsum_err:.2e}", f"{lin_err:.2e}"])
table("Shakl funksiyalarining tekshiruvi",
      ["tartib p", "tugunlar", "delta xossasi", "sum(N) - 1",
       "sum(dN)", "chiziqli tiklash"], rows)
note("Barcha tartiblar uchun to'rtta shart ham mashina aniqligida "
     "bajarildi: N_i(xi_j) = delta_ij, sum(N) = 1, sum(dN) = 0 va "
     "chiziqli funksiya AYNAN tiklanadi. Oxirgi ikkitasi to'liqlik "
     "shartining bevosita ifodasi - qattiq jism harakati va doimiy "
     "deformatsiya to'g'ri ifodalanadi.")

nodes_p = np.linspace(-1.0, 1.0, p_ord + 1)
xi_plot = np.linspace(-1.0, 1.0, 301)
Np, dNp = lagrange_N(xi_plot, nodes_p)
for i in range(p_ord + 1):
    series(f"N_{i+1} (p = {p_ord})", xi_plot.tolist(), Np[i].tolist(),
           xlabel="tabiiy koordinata xi", ylabel="N")
series("sum(N_i)", xi_plot.tolist(), np.sum(Np, axis=0).tolist(),
       xlabel="tabiiy koordinata xi", ylabel="N")

# Yuqori tartibli elementlarda Runge hodisasi
rows2 = []
for order in [2, 4, 8, 16, 24, 32]:
    nodes_u = np.linspace(-1.0, 1.0, order + 1)
    xi = np.linspace(-1.0, 1.0, 2001)
    Nu, _ = lagrange_N(xi, nodes_u)
    # Runge funksiyasi
    fr = 1.0/(1.0 + 25.0*xi**2)
    fn = 1.0/(1.0 + 25.0*nodes_u**2)
    interp = np.sum(Nu*fn[:, None], axis=0)
    err_u = np.max(np.abs(interp - fr))
    # Chebishev tugunlari
    nodes_c = np.cos(np.pi*np.arange(order + 1)/order)
    Nc, _ = lagrange_N(xi, nodes_c)
    fc = 1.0/(1.0 + 25.0*nodes_c**2)
    interp_c = np.sum(Nc*fc[:, None], axis=0)
    err_c = np.max(np.abs(interp_c - fr))
    rows2.append([order, f"{err_u:.4f}", f"{err_c:.5f}"])
table("Runge hodisasi: tekis va Chebishev tugunlari",
      ["tartib", "tekis tugunlar xatosi", "Chebishev xatosi"], rows2)
note("Kichik tartiblarda (p <= 4) ikkala joylashuv ham bir xil, lekin "
     "p >= 8 dan boshlab yo'llar keskin ajraladi: tekis tugunlarda xato "
     "PORTLAYDI (p = 32 da 5059 ga yetadi - Runge hodisasi), Chebishev "
     "tugunlarida esa bir tekis kamayadi (0.0016). Shuning uchun yuqori "
     "tartibli elementlarda tugunlar tekis emas, Gauss-Lobatto "
     "nuqtalariga joylashtiriladi.")

# --- (2) YAKOBIAN: bir o'lchovli kvadratik element ---
x_nodes = np.array([0.0, alpha*L_el, L_el])
nodes3 = np.array([-1.0, 0.0, 1.0])
xi = np.linspace(-1.0, 1.0, 401)
N3, dN3 = lagrange_N(xi, nodes3)
J = np.sum(dN3*x_nodes[:, None], axis=0)
series("Yakobian J(xi)", xi.tolist(), J.tolist(),
       xlabel="xi", ylabel="J")
series("J = 0 chegarasi", xi.tolist(), [0.0]*len(xi),
       xlabel="xi", ylabel="J")
value("O'rta tugun nisbiy joyi alpha", alpha, "—")
value("J(-1)", float(J[0]), "—")
value("J(0)", float(J[len(J)//2]), "—")
value("J(+1)", float(J[-1]), "—")
value("min J", float(np.min(J)), "—")
value("max/min J nisbati",
      float(np.max(J)/np.min(J)) if np.min(J) > 1e-12 else float("inf"),
      "—")
# Analitik: J = L/2 * (1 + 2*xi*(1 - 2*alpha))
J_an = L_el/2*(1 + 2*xi*(1 - 2*alpha))
value("Analitik formuladan maks farq",
      float(np.max(np.abs(J - J_an))), "—")
note(f"Yakobian J(xi) = (L/2)*(1 + 2*xi*(1-2*alpha)) analitik "
     f"formulasi bilan {np.max(np.abs(J - J_an)):.2e} farq qiladi. "
     f"alpha = {alpha:.3f} da J(-1) = {J[0]:.4f}.")

rows3 = []
for al in [0.50, 0.40, 0.30, 0.25, 0.20, 0.15]:
    xn = np.array([0.0, al*L_el, L_el])
    Jk = np.sum(dN3*xn[:, None], axis=0)
    ok = "ha" if np.min(Jk) > 1e-12 else "YO'Q"
    rows3.append([f"{al:.2f}", f"{np.min(Jk):+.4f}", f"{np.max(Jk):.4f}",
                  ok])
table("O'rta tugun joyining Yakobianga ta'siri",
      ["alpha", "min J", "max J", "yaroqlimi?"], rows3)
note("alpha = 0.25 (CHORAK NUQTA) da min J aynan nolga aylanadi va "
     "undan kichik qiymatlarda MANFIY bo'ladi - element ag'dariladi. "
     "Bu FEM dagi 'o'rta tugun chorakdan nariga chiqmasin' "
     "qoidasining aniq manbai.")

# --- (2b) CHORAK NUQTALI element 1/sqrt(r) ni HOSIL QILADIMI? ---
# Mustaqil tekshiruv: alpha = 1/4 da geometriya x = (L/4)(1+xi)^2 bo'ladi,
# demak (1+xi) ~ sqrt(x) va deformatsiya 1/sqrt(x) kabi singulyar bo'ladi.
xi_q = np.linspace(-0.999, 1.0, 2000)
Nq, dNq = lagrange_N(xi_q, nodes3)
u_nod = np.array([0.0, 0.5, 1.0])          # ixtiyoriy tugun ko'chishlari

xq_qp = np.sum(Nq*np.array([0.0, L_el/4, L_el])[:, None], axis=0)
Jq_qp = np.sum(dNq*np.array([0.0, L_el/4, L_el])[:, None], axis=0)
eps_qp = np.sum(dNq*u_nod[:, None], axis=0)/Jq_qp
value("x(xi) va (L/4)(1+xi)^2 farqi",
      float(np.max(np.abs(xq_qp - (L_el/4)*(1 + xi_q)**2))), "m")
slope = float(np.polyfit(np.log(xq_qp[:400]),
                         np.log(np.abs(eps_qp[:400])), 1)[0])
value("Chorak nuqtali element: log-log qiyaligi", slope, "—")
value("eps*sqrt(x) ning o'zgarishi (maks - min)",
      float(np.max(eps_qp*np.sqrt(xq_qp)) -
            np.min(eps_qp*np.sqrt(xq_qp))), "—")

xq_md = np.sum(Nq*np.array([0.0, L_el/2, L_el])[:, None], axis=0)
Jq_md = np.sum(dNq*np.array([0.0, L_el/2, L_el])[:, None], axis=0)
eps_md = np.sum(dNq*u_nod[:, None], axis=0)/Jq_md
value("Markaziy tugunli element: eps o'zgarishi",
      float(np.max(eps_md) - np.min(eps_md)), "—")
series("Deformatsiya: chorak nuqtali", xq_qp.tolist(), eps_qp.tolist(),
       xlabel="x, m", ylabel="eps")
series("Deformatsiya: markaziy tugunli", xq_md.tolist(), eps_md.tolist(),
       xlabel="x, m", ylabel="eps")
note(f"Chorak nuqtali elementda deformatsiya log-log o'lchovda "
     f"{slope:.4f} qiyalikka ega - ya'ni AYNAN 1/sqrt(x). "
     f"eps*sqrt(x) ko'paytmasi butun element bo'ylab "
     f"{np.max(eps_qp*np.sqrt(xq_qp)) - np.min(eps_qp*np.sqrt(xq_qp)):.2e} "
     f"gacha aniqlikda doimiy. Aynan shu tmm-24 dagi yorilish uchidagi "
     f"kuchlanish maydoni. O'rta tugun markazda bo'lsa (alpha = 0.5) "
     f"xuddi shu tugun qiymatlari deformatsiyani DOIMIY beradi. Demak "
     f"geometriyani buzish orqali kerakli matematik xatti-harakat "
     f"hosil qilindi.")

# --- (3) IKKI O'LCHOVLI Q4 element va uning buzilishi ---
def q4_shape(xi, eta):
    xn = np.array([-1.0, 1.0, 1.0, -1.0])
    yn = np.array([-1.0, -1.0, 1.0, 1.0])
    N = 0.25*(1 + xi*xn[:, None, None])*(1 + eta*yn[:, None, None])
    dNx = 0.25*xn[:, None, None]*(1 + eta*yn[:, None, None])
    dNe = 0.25*(1 + xi*xn[:, None, None])*yn[:, None, None]
    return N, dNx, dNe


g = np.linspace(-1, 1, 61)
XI, ETA = np.meshgrid(g, g, indexing="ij")
N4, dN4x, dN4e = q4_shape(XI, ETA)
value("Q4: sum(N) dan maks chetlanish",
      float(np.max(np.abs(np.sum(N4, axis=0) - 1.0))), "—")


def q4_detJ(xc, yc, dx, de):
    Jxx = np.sum(dx*xc[:, None, None], axis=0)
    Jxy = np.sum(dx*yc[:, None, None], axis=0)
    Jyx = np.sum(de*xc[:, None, None], axis=0)
    Jyy = np.sum(de*yc[:, None, None], axis=0)
    return Jxx*Jyy - Jxy*Jyx


# Yuzani 2x2 Gauss bilan hisoblaymiz - Q4 uchun AYNAN
gx2, gw2 = np.polynomial.legendre.leggauss(2)
GX, GE = np.meshgrid(gx2, gx2, indexing="ij")
_, dg4x, dg4e = q4_shape(GX, GE)


def q4_area(xc, yc):
    return float(np.sum(q4_detJ(xc, yc, dg4x, dg4e)*np.outer(gw2, gw2)))


def shoelace(xc, yc):
    return 0.5*abs(sum(xc[i]*yc[(i + 1) % 4] - xc[(i + 1) % 4]*yc[i]
                       for i in range(4)))


# (a) Trapetsiya: uchinchi tugun o'ngga suriladi - det J o'zgaruvchan,
#     lekin hamma joyda musbat
rows4 = []
for sk in [0.0, 0.5, 1.0, 2.0, 4.0]:
    xc = np.array([0.0, 1.0, 1.0 + sk, 0.0])
    yc = np.array([0.0, 0.0, 1.0, 1.0])
    dJ = q4_detJ(xc, yc, dN4x, dN4e)
    rows4.append([f"{sk:.1f}", f"{np.min(dJ):+.5f}", f"{np.max(dJ):.5f}",
                  f"{np.max(dJ)/np.min(dJ):.2f}",
                  f"{q4_area(xc, yc):.6f}", f"{shoelace(xc, yc):.6f}"])
table("Q4: trapetsiyaga cho'zilish (det J musbat qoladi)",
      ["surilish", "min det J", "max det J", "nisbat",
       "Gauss yuzasi", "aniq yuza"], rows4)
note("Trapetsiyada det(J) endi DOIMIY emas va max/min nisbati "
     "surilish bilan chiziqli o'sadi. Yuza esa 2x2 Gauss bilan "
     "mashina aniqligida aynan chiqadi - Q4 uchun ikki nuqtali "
     "kvadratura yetarli (su-16 da asoslanadi).")

# (b) Uchinchi tugunni ICHKARIGA tortamiz - element botiq bo'ladi
rows5b = []
for sk in [0.0, 0.3, 0.5, 0.6, 0.9, 1.1]:
    xc = np.array([0.0, 1.0, 1.0 - sk, 0.0])
    yc = np.array([0.0, 0.0, 1.0 - sk, 1.0])
    dJ = q4_detJ(xc, yc, dN4x, dN4e)
    # geometrik mezon: tugun 2-4 diagonalidan o'tganmi?
    # diagonal: x + y = 1; tugun 3: 2(1-sk)
    d3 = 2*(1.0 - sk) - 1.0
    rows5b.append([f"{sk:.1f}", f"{np.min(dJ):+.5f}", f"{d3:+.4f}",
                   f"{q4_area(xc, yc):+.5f}",
                   "ha" if np.min(dJ) > 1e-12 else "YO'Q"])
table("Q4: uchinchi tugunni ichkariga tortish (ag'darilish)",
      ["tortish", "min det J", "diagonaldan masofa", "Gauss yuzasi",
       "yaroqlimi?"], rows5b)
note("MUSTAQIL TEKSHIRUV. Yakobian bo'yicha element tortish 0.5 da "
     "ag'dariladi (min det J = 0.25 - 0.5*s, nol nuqtasi s = 0.5). "
     "Geometrik mezon esa boshqa yo'ldan boradi: uchinchi tugun 2- va "
     "4-tugunlarni tutashtirgan diagonaldan o'tganda to'rtburchak "
     "BOTIQ bo'ladi, ya'ni 2(1-s) = 1 dan s = 0.5. Ikki mustaqil "
     "mezon bir xil chegarani berdi - det J botiqlikni aynan "
     "aniqlaydi. s > 1 da yuza manfiy: element o'z ustiga o'raladi.")

xc = np.array([0.0, 1.0, 1.0 - skew, 0.0])
yc = np.array([0.0, 0.0, 1.0 - skew, 1.0])
detJ = q4_detJ(xc, yc, dN4x, dN4e)
value("Q4: min det(J)", float(np.min(detJ)), "—")
value("Q4: max/min det(J) nisbati",
      float(np.max(detJ)/np.min(detJ)) if np.min(detJ) > 1e-12
      else float("inf"), "—")
value("Q4: yuza (2x2 Gauss)", q4_area(xc, yc), "m^2")
value("Q4: yuza (aniq, Gauss formulasi)",
      float(shoelace(xc, yc)), "m^2")
series("det(J) diagonal bo'ylab", g.tolist(),
       np.diagonal(detJ).tolist(), xlabel="xi = eta", ylabel="det J")

# --- (4) TO'LIQLIK: patch test ---
# Har bir element chiziqli maydonni AYNAN tiklashi kerak
rows5 = []
for order in [1, 2, 3]:
    nodes_t = np.linspace(-1.0, 1.0, order + 1)
    xi_t = np.linspace(-1.0, 1.0, 101)
    Nt, dNt = lagrange_N(xi_t, nodes_t)
    xe = np.array([0.0, L_el])
    # element geometriyasi: tekis taqsimlangan tugunlar
    xg_n = np.linspace(0.0, L_el, order + 1)
    xg = np.sum(Nt*xg_n[:, None], axis=0)
    Jt = np.sum(dNt*xg_n[:, None], axis=0)
    for test, fn in [("doimiy (a)", lambda t: 3.0*np.ones_like(t)),
                     ("chiziqli (a+bx)", lambda t: 3.0 + 2.0*t),
                     ("kvadratik (x^2)", lambda t: t**2)]:
        un = fn(xg_n)
        uh = np.sum(Nt*un[:, None], axis=0)
        err = np.max(np.abs(uh - fn(xg)))
        rows5.append([order, test, f"{err:.3e}"])
table("Patch test: element qaysi maydonlarni AYNAN tiklaydi",
      ["tartib p", "sinov maydoni", "xatolik"], rows5)
note("Har qanday tartibdagi element doimiy va chiziqli maydonni "
     "AYNAN tiklaydi - to'liqlik sharti bajarilgan. Kvadratik "
     "maydonni esa faqat p >= 2 aynan tiklaydi; p = 1 da xato "
     "qoladi. Bu yaqinlashish tartibini belgilaydi: p-tartibli "
     "element O(h^(p+1)) ko'chish aniqligini beradi.")

# --- (5) Element tartibining aniqlikka ta'siri ---
# u'' = -f ni turli tartibli elementlar bilan yechamiz
def fem_order(n_el, p):
    """p-tartibli elementlar bilan sterjen masalasi."""
    EA_, f_, Lb = 1000.0, 100.0, 1.0
    nodes_e = np.linspace(-1.0, 1.0, p + 1)
    ndof = n_el*p + 1
    K = np.zeros((ndof, ndof))
    F = np.zeros(ndof)
    he = Lb/n_el
    # Gauss nuqtalari (p+1 nuqta - aniq integrallash uchun yetarli)
    ng = p + 1
    gx, gw = np.polynomial.legendre.leggauss(ng)
    Ng, dNg = lagrange_N(gx, nodes_e)
    for e in range(n_el):
        idx = np.arange(e*p, e*p + p + 1)
        Je = he/2
        ke = np.zeros((p + 1, p + 1))
        fe = np.zeros(p + 1)
        for q_ in range(ng):
            B = dNg[:, q_]/Je
            ke += EA_*np.outer(B, B)*gw[q_]*Je
            fe += f_*Ng[:, q_]*gw[q_]*Je
        K[np.ix_(idx, idx)] += ke
        F[idx] += fe
    Kr, Fr = K[1:, 1:], F[1:]
    u = np.concatenate([[0.0], np.linalg.solve(Kr, Fr)])
    return u[-1], ndof - 1


rows6 = []
u_ex_tip = 100.0*1.0**2/(2*1000.0)
for p in [1, 2, 3]:
    for n_el in [1, 2, 4, 8]:
        ut, ndof = fem_order(n_el, p)
        rows6.append([p, n_el, ndof, f"{ut:.10f}",
                      f"{abs(ut-u_ex_tip)/u_ex_tip*100:.3e}"])
table("Element tartibi va aniqlik (uch ko'chishi)",
      ["p", "elementlar", "erkinlik darajalari", "u(L)", "xato, %"],
      rows6)
value("Aniq u(L)", u_ex_tip, "m")
note("Bu masalada barcha tartiblar tugunda aniq yechimni beradi "
     "(1D superkonvergensiya, su-13). Yuqori tartibli elementlarning "
     "afzalligi element ICHIDA va kuchlanishda namoyon bo'ladi - "
     "keyingi jadvalga qarang.")

# Element ichidagi aniqlik: deformatsiya
rows7 = []
for p in [1, 2, 3]:
    n_el = 4
    EA_, f_, Lb = 1000.0, 100.0, 1.0
    nodes_e = np.linspace(-1.0, 1.0, p + 1)
    he = Lb/n_el
    ut, _ = fem_order(n_el, p)
    # to'liq yechimni qayta qurish
    ng = p + 1
    gx, gw = np.polynomial.legendre.leggauss(ng)
    ndof = n_el*p + 1
    K = np.zeros((ndof, ndof))
    F = np.zeros(ndof)
    Ng, dNg = lagrange_N(gx, nodes_e)
    for e in range(n_el):
        idx = np.arange(e*p, e*p + p + 1)
        Je = he/2
        for q_ in range(ng):
            B = dNg[:, q_]/Je
            K[np.ix_(idx, idx)] += EA_*np.outer(B, B)*gw[q_]*Je
            F[idx] += f_*Ng[:, q_]*gw[q_]*Je
    u = np.concatenate([[0.0], np.linalg.solve(K[1:, 1:], F[1:])])
    # deformatsiyani element ichida bir necha nuqtada baholaymiz
    xs_all, eps_all, eps_ex_all = [], [], []
    xi_s = np.linspace(-1, 1, 21)
    Ns, dNs = lagrange_N(xi_s, nodes_e)
    for e in range(n_el):
        idx = np.arange(e*p, e*p + p + 1)
        Je = he/2
        xe_loc = np.linspace(e*he, (e+1)*he, p + 1)
        xs = np.sum(Ns*xe_loc[:, None], axis=0)
        eps = np.sum((dNs/Je)*u[idx][:, None], axis=0)
        xs_all.extend(xs)
        eps_all.extend(eps)
        eps_ex_all.extend(f_/EA_*(Lb - xs))
    eps_all = np.array(eps_all)
    eps_ex_all = np.array(eps_ex_all)
    err_eps = np.max(np.abs(eps_all - eps_ex_all))/np.max(np.abs(eps_ex_all))
    rows7.append([p, n_el, n_el*p + 1, f"{err_eps*100:.4e}"])
    series(f"Deformatsiya, p = {p}", list(xs_all),
           (eps_all*1e6).tolist(), xlabel="x, m", ylabel="eps x 1e6")
table("Element ICHIDAGI deformatsiya xatosi (4 element)",
      ["p", "elementlar", "erkinlik darajalari", "maks xato, %"], rows7)
note("Element ichidagi deformatsiya xatosi tartib oshgani sari "
     "keskin kamayadi: p = 1 da deformatsiya bo'lakli DOIMIY, "
     "p = 2 da chiziqli. Bu masalada aniq deformatsiya chiziqli, "
     "shuning uchun p = 2 uni AYNAN tiklaydi. Erkinlik darajalari "
     "soni esa atigi ikki barobar oshdi - yuqori tartibli "
     "elementlarning afzalligi shunda.")

table("Element turlari va ularning xossalari",
      ["Element", "Tugunlar", "Ko'chish", "Deformatsiya", "Chegara"],
      [["Chiziqli (L2)", "2", "chiziqli", "DOIMIY", "to'g'ri"],
       ["Kvadratik (L3)", "3", "kvadratik", "chiziqli", "PARABOLA"],
       ["Kubik (L4)", "4", "kubik", "kvadratik", "kubik egri"],
       ["Q4 (2D)", "4", "bichiziqli", "chiziqli", "to'g'ri"],
       ["Q8 (2D)", "8", "kvadratik", "chiziqli", "PARABOLA"],
       ["Chorak nuqtali", "3", "kvadratik", "1/sqrt(r)", "singulyar"]])
''',
                parameters=[
                    p("p_ord", "Element tartibi p", 1.0, 4.0, 2.0, 1.0),
                    p("alpha", "O'rta tugun nisbiy joyi", 0.1, 0.9, 0.5,
                      0.05),
                    p("skew", "Q4: uchinchi tugunni ichkariga tortish",
                      0.0, 1.2, 0.0, 0.05),
                    p("L_el", "Element uzunligi", 0.1, 10.0, 2.0, 0.1, "m"),
                ],
                expected_output=(
                    "Barcha tartiblar uchun "
                    "$N_i(\\xi_j) = \\delta_{ij}$, "
                    "$\\sum N_i = 1$, "
                    "$\\sum dN_i = 0$ va chiziqli "
                    "funksiyaning aynan tiklanishi "
                    "mashina aniqligida "
                    "bajariladi. Runge sinovida "
                    "$p \\le 4$ da farq yo'q, "
                    "lekin $p = 32$ da tekis "
                    "tugunlar xatosi 5059 ga "
                    "chiqadi, Chebishev esa "
                    "0,0016 ga tushadi. O'rta "
                    "tugun $\\alpha = 0{,}25$ "
                    "(chorak nuqta) da "
                    "$\\min J = 0$ va undan "
                    "kichik qiymatlarda manfiy. "
                    "Shu nuqtada deformatsiyaning "
                    "log-log qiyaligi aynan "
                    "$-0{,}5$ — ya'ni "
                    "$1/\\sqrt{x}$ singulyarligi "
                    "hosil bo'ladi. Q4 "
                    "elementda tortish 0,5 ga "
                    "yetganda $\\det J$ nolga "
                    "aylanadi va bu tugunning "
                    "diagonaldan o'tish nuqtasi "
                    "bilan aynan mos tushadi; "
                    "yuza $2\\times2$ Gauss "
                    "bilan aynan chiqadi. Patch "
                    "test barcha elementlar "
                    "doimiy va chiziqli maydonni "
                    "aynan tiklashini, kvadratik "
                    "maydonni esa faqat "
                    "$p \\ge 2$ tiklashini "
                    "ko'rsatadi; element ichidagi "
                    "deformatsiya xatosi "
                    "$p = 1$ da 12,5%, "
                    "$p = 2$ da esa nolga teng."
                ),
            ),
            visual=vis(
                kind="Shakl funksiyalari va izoparametrik almashtirish",
                tool="React/SVG + Manim",
                description=(
                    "Shakl funksiyalarining "
                    "grafigi, etalon va haqiqiy "
                    "element, Yakobian xaritasi."
                ),
                how_to_draw=(
                    "React/SVG: yuqori chap panelda "
                    "shakl funksiyalari "
                    "$N_i(\\xi)$ chiziladi; har "
                    "biri o'z tugunida aynan 1 ga "
                    "yetib, qolganlarida nolga "
                    "tushishi nuqtalar bilan "
                    "belgilanadi. Ularning ustiga "
                    "$\\sum N_i$ chizig'i "
                    "qo'yiladi va u **aynan 1** "
                    "bo'lgan gorizontal chiziq "
                    "ekani ko'rinadi — to'liqlik "
                    "shartining eng aniq tasviri. "
                    "Tartib slayderi bilan "
                    "funksiyalar soni o'zgaradi. "
                    "O'ng panelda izoparametrik "
                    "almashtirish: chapda etalon "
                    "kvadrat "
                    "$[-1,1]\\times[-1,1]$ "
                    "to'r chiziqlari bilan, "
                    "o'ngda esa uning haqiqiy "
                    "elementga aylangani — to'r "
                    "chiziqlari egri bo'lib "
                    "qoladi. Tugunlarni sichqoncha "
                    "bilan sudrab element "
                    "buziladi va **det J "
                    "xaritasi** rang bilan "
                    "ko'rsatiladi: yashildan "
                    "qizilga, manfiy sohalar esa "
                    "qora shtrix bilan "
                    "'ag'darilgan' deb "
                    "belgilanadi. Pastda "
                    "bir o'lchovli $J(\\xi)$ "
                    "grafigi va $J = 0$ chizig'i; "
                    "o'rta tugun slayderi "
                    "$\\alpha = 0{,}25$ ga "
                    "yetganda $J$ chap uchida "
                    "aynan nolga tegadi va bu "
                    "moment alohida "
                    "ta'kidlanadi."
                ),
            ),
            interp=(
                "Shakl funksiyalarining to'rtta "
                "xossasi mashina aniqligida "
                "tekshiriladi va bu har qanday "
                "yangi element uchun birinchi "
                "bajariladigan test bo'lishi "
                "kerak. Ayniqsa $\\sum N_i = 1$ "
                "va chiziqli funksiyaning aynan "
                "tiklanishi muhim: ular "
                "to'liqlik shartining bevosita "
                "ifodasi va ularsiz element "
                "yaqinlashmaydi. Runge hodisasi "
                "jadvali esa kutilmagan "
                "ogohlantirish beradi: tekis "
                "tugunlarda tartib oshgani sari "
                "interpolyatsiya xatosi "
                "**o'sadi**. Shuning uchun "
                "yuqori tartibli elementlarda "
                "tugunlar tekis emas, "
                "Gauss–Lobatto nuqtalariga "
                "joylashtiriladi — bu "
                "amaliyotda ko'pincha "
                "e'tibordan chetda qoladi. "
                "Yakobian tajribasi eng aniq "
                "sonli natijani beradi: "
                "$\\alpha = 0{,}25$ da "
                "$\\min J$ aynan nolga aylanadi. "
                "Bu 'o'rta tugun chorakdan "
                "nariga chiqmasin' qoidasining "
                "manbai va uning aniq chegarasi. "
                "Chorak nuqtali element sinovi "
                "esa buni kutilmagan tomondan "
                "ko'rsatadi: o'sha nuqtada "
                "deformatsiyaning log-log "
                "qiyaligi aynan $-0{,}5$ va "
                "$\\varepsilon\\sqrt{x}$ "
                "ko'paytmasi butun element "
                "bo'ylab $4\\cdot10^{-14}$ "
                "gacha aniqlikda doimiy — "
                "ya'ni $1/\\sqrt{x}$ "
                "singulyarligi **aynan** hosil "
                "bo'ldi. Xuddi shu tugun "
                "qiymatlari bilan o'rta tugun "
                "markazda bo'lsa, deformatsiya "
                "doimiy chiqadi. Demak bir xil "
                "shakl funksiyalari va bir xil "
                "tugun qiymatlari, faqat "
                "geometriya boshqacha — natija "
                "esa tubdan farq qiladi. "
                "Q4 tajribasi ikki o'lchovga "
                "ko'chiradi va u yerda mustaqil "
                "tekshiruv o'rnatildi: "
                "Yakobian bo'yicha "
                "ag'darilish chegarasi "
                "$s = 0{,}5$ "
                "($\\min\\det J = 0{,}25 - "
                "0{,}5s$) va sof geometrik "
                "mezon — tugunning qarshi "
                "diagonaldan o'tishi — bir xil "
                "qiymatni berdi. Ya'ni "
                "$\\det J$ to'rtburchakning "
                "botiq bo'lishini aynan "
                "aniqlaydi; bu 'element "
                "sifati' tekshiruvining "
                "matematik asosi. Yuza esa "
                "$2\\times2$ Gauss bilan "
                "mashina aniqligida chiqdi — "
                "Q4 uchun to'rt nuqta yetarli "
                "ekanining bevosita isboti. "
                "Nihoyat, "
                "element tartibi tajribasi "
                "muhim xulosaga olib keladi: "
                "ko'chishda barcha tartiblar "
                "tugunda aniq (1D "
                "superkonvergensiya), lekin "
                "element **ichidagi** "
                "deformatsiyada farq keskin. "
                "$p = 2$ bu masalada "
                "deformatsiyani aynan tiklaydi, "
                "$p = 1$ esa bo'lakli doimiy "
                "beradi. Erkinlik darajalari "
                "soni atigi ikki barobar "
                "oshgani hisobga olinsa, yuqori "
                "tartibli elementlarning "
                "samaradorligi ayon bo'ladi."
            ),
            mistakes=[
                "$\\sum N_i = 1$ ni "
                "tekshirmaslik. Bu bir qator "
                "kod, lekin u butun elementning "
                "yaroqliligini aniqlaydi.",
                "O'rta tugunni chorak "
                "nuqtasidan nariga siljitish. "
                "$\\det J$ ishorasini "
                "o'zgartiradi va element "
                "ag'dariladi.",
                "Yuqori tartibli elementda "
                "tugunlarni tekis joylashtirish. "
                "Runge hodisasi tufayli aniqlik "
                "tushadi; Gauss–Lobatto "
                "nuqtalari kerak.",
                "Q4 elementni sof egilish "
                "masalasida ishlatish. Uning "
                "bazisi to'liq kvadratik emas — "
                "qulflanish paydo bo'ladi "
                "(su-16).",
                "$\\det J$ hisobotini "
                "e'tiborsiz qoldirish. Buzilgan "
                "elementlar kuchlanish "
                "natijalarini jimgina buzadi.",
            ],
            quiz=[
                q("Shakl funksiyalarining ikkita "
                  "asosiy xossasi qanday?",
                  "$N_i(\\xi_j) = \\delta_{ij}$ "
                  "(o'z tugunida 1, qolganlarida "
                  "0) va $\\sum_i N_i = 1$ "
                  "(to'liqlik).", "konseptual"),
                q("Izoparametrik almashtirishning "
                  "mohiyati nima?",
                  "Geometriya va noma'lum maydon "
                  "**bir xil** shakl funksiyalari "
                  "bilan ifodalanadi; natijada "
                  "kvadratik elementning "
                  "chegarasi parabola bo'ladi.",
                  "konseptual"),
                q("Uch tugunli element "
                  "$x = \\{0, 0{,}5, 2\\}$ uchun "
                  "$J(-1)$ nechaga teng?",
                  "$J = \\xi + 1$, demak "
                  "$J(-1) = 0$ — element chap "
                  "uchida singulyar (chorak "
                  "nuqtali element).", "hisob"),
                q("Kodda nima uchun Runge "
                  "hodisasi tekshiriladi?",
                  "Tekis tugunlarda tartib "
                  "oshgani sari interpolyatsiya "
                  "xatosi o'sishini ko'rsatish "
                  "uchun; bu yuqori tartibli "
                  "elementlarda tugun "
                  "joylashuvi muhimligini "
                  "asoslaydi.", "kod"),
                q("Patch test nimani tekshiradi "
                  "va u nima uchun muhim?",
                  "Element doimiy va chiziqli "
                  "maydonni aynan tiklay "
                  "oladimi — ya'ni to'liqlik "
                  "shartini. Bu bajarilmasa "
                  "to'r zichlashganda ham "
                  "yaqinlashish yo'q.", "talqin"),
                q("$\\det\\mathbf{J} \\le 0$ nima "
                  "degani va u qachon yuzaga "
                  "keladi?",
                  "Element ag'darilgan — etalon "
                  "va haqiqiy element orasidagi "
                  "moslik buzilgan. Odatda "
                  "o'rta tugun juda siljiganda "
                  "yoki to'rt burchakli element "
                  "botiq bo'lganda.", "talqin"),
                q("Kod Q4 elementning ag'darilish "
                  "chegarasini ikki mustaqil "
                  "yo'l bilan topadi. Ular "
                  "qanday va natija qanday?",
                  "Birinchisi — $\\min\\det J$ "
                  "ning nolga aylanishi, "
                  "ikkinchisi — tugunning qarshi "
                  "diagonaldan o'tishi (sof "
                  "geometrik mezon). Ikkalasi "
                  "ham $s = 0{,}5$ ni beradi, "
                  "demak $\\det J$ botiqlikni "
                  "aynan aniqlaydi.", "kod"),
                q("Chorak nuqtali elementda "
                  "deformatsiya nima uchun "
                  "$1/\\sqrt{x}$ kabi o'zgaradi?",
                  "$\\alpha = 1/4$ da geometriya "
                  "$x = (L/4)(1+\\xi)^2$ bo'ladi, "
                  "ya'ni $1+\\xi \\propto "
                  "\\sqrt{x}$. Deformatsiya "
                  "$\\varepsilon = "
                  "(du/d\\xi)/J$ va "
                  "$J \\propto (1+\\xi)$, demak "
                  "$\\varepsilon \\propto "
                  "1/\\sqrt{x}$ — kod buni "
                  "log-log qiyaligi $-0{,}5$ "
                  "bilan tasdiqlaydi.", "hisob"),
            ],
            bridge=(
                "Shakl funksiyalari va "
                "izoparametrik almashtirish "
                "tayyor. Endi ularni bikrlik "
                "matritsasini qurishda "
                "ishlatamiz. Bu yerda ikkita "
                "yangi savol paydo bo'ladi: "
                "element integrallarini qanday "
                "hisoblash va alohida element "
                "matritsalarini global tizimga "
                "qanday yig'ish."
            ),
            research=(
                "Element texnologiyasini "
                "chuqurlashtiring. "
                "(1) Ierarxik (p-tipdagi) shakl "
                "funksiyalarini o'rganing: ular "
                "tartibni oshirishda oldingi "
                "bazisni saqlaydi, shuning uchun "
                "matritsaning bir qismi qayta "
                "hisoblanmaydi — adaptivlikda "
                "(su-18) bu qanday "
                "ishlatiladi? (2) Serendipiti "
                "(Q8) va Lagranj (Q9) "
                "elementlarini taqqoslang: "
                "markaziy tugunning bo'lishi "
                "aniqlikka va samaradorlikka "
                "qanday ta'sir qiladi? "
                "(3) Uchburchak elementlar "
                "uchun maydon koordinatalarini "
                "(area coordinates) o'rganing "
                "va ularning to'rtburchak "
                "elementlardan afzalligini "
                "murakkab geometriyada "
                "baholang. (4) NURBS asosidagi "
                "izogeometrik tahlilni (IGA) "
                "ko'rib chiqing: u CAD "
                "geometriyasini AYNAN "
                "ishlatadi — bu izoparametrik "
                "g'oyaning tabiiy davomi."
            ),
            manim_ref=manim(
                scene="IsoparametricScene",
                module="manim/scenes/su_fem.py",
                title="Izoparametrik almashtirish",
                summary=(
                    "Etalon kvadrat "
                    "$[-1,1]^2$ to'r chiziqlari "
                    "bilan ko'rsatiladi va "
                    "asta-sekin haqiqiy "
                    "elementga aylanadi: to'r "
                    "chiziqlari egriladi, "
                    "chegara parabolaga aylanadi. "
                    "Keyin tugun siljitilib "
                    "element buziladi va "
                    "$\\det J$ xaritasi qizarib "
                    "boradi; chorak nuqtada u "
                    "nolga tegadi va undan "
                    "keyin element o'z ustiga "
                    "o'ralib qoladi."
                ),
            ),
        ),
    ),

    # ------------------------------------------------------------------ su-15
    Topic(
        id="su-15",
        subject_id=S, module_id=M, order=15,
        title="Element matritsalari va global tizimni yig'ish",
        description=(
            "Element bikrlik matritsasi va moslashgan yuk vektori, "
            "yig'ish (assembly) algoritmi, global matritsaning xossalari, "
            "lenta kengligi va tugunlarni raqamlash."
        ),
        learning_objective=(
            "Element matritsalarini hisoblash, ularni global tizimga "
            "yig'ish va natijaviy matritsaning to'rtta majburiy xossasini "
            "tekshirish; raqamlashning yechish narxiga ta'sirini baholash."
        ),
        prerequisites=["su-14"],
        mathematical_core=(
            "$\\mathbf{k}^e = \\int_{\\Omega_e}\\mathbf{B}^T\\mathbf{D}"
            "\\mathbf{B}\\,d\\Omega$, "
            "$\\mathbf{f}^e = \\int_{\\Omega_e}\\mathbf{N}^T b\\,d\\Omega$; "
            "$\\mathbf{K} = \\sum_e \\mathbf{A}_e^T\\mathbf{k}^e"
            "\\mathbf{A}_e$; "
            "$\\mathbf{K} = \\mathbf{K}^T \\ge 0$, "
            "$\\mathbf{K}\\mathbf{r} = \\mathbf{0}$ qattiq jism uchun."
        ),
        engineering_application=(
            "Har qanday FEM dasturining yadrosi; raqamlash tanlovi katta "
            "modelning yechish vaqtini o'nlab marta o'zgartiradi."
        ),
        computational_component=(
            "Element matritsalarini qurish, yig'ish, xossalarni "
            "tekshirish, lenta kengligini o'lchash va qayta raqamlash."
        ),
        visualization_component=(
            "Yig'ish jarayonining animatsiyasi, matritsa to'ldirilish "
            "xaritasi, lenta kengligining raqamlashga bog'liqligi."
        ),
        research_extension=(
            "Frontal va ko'p frontli (multifrontal) yechish usullarini "
            "o'rganing: ular yig'ish va yechishni birlashtiradi — bu "
            "xotira talabini qanday kamaytiradi?"
        ),
        difficulty="orta",
        previous_link=(
            "su-14 da shakl funksiyalari va izoparametrik almashtirish "
            "tayyor bo'ldi. Endi ular bilan element integrallarini "
            "hisoblaymiz va alohida elementlarni bitta global tizimga "
            "bog'laymiz — bu FEM dasturining yadrosi."
        ),
        next_topic="su-16",
        estimated_minutes=85,
        tags=["bikrlik matritsasi", "assembly", "lenta kengligi",
              "moslashgan yuk"],
        lesson=_lesson(
            problem=(
                "Ko'prik fermasining hisobi "
                "10 000 tugundan iborat. Har bir "
                "element o'z bikrlik "
                "matritsasiga ega, lekin ular "
                "umumiy tugunlar orqali bir "
                "biriga bog'langan. Bu "
                "bog'lanishni qanday tizimli "
                "yozish mumkin? Bundan ham "
                "muhimi — natijaviy "
                "$20\\,000\\times20\\,000$ "
                "matritsa to'la saqlansa "
                "3,2 GB xotira talab qiladi va "
                "yechish bir necha soat davom "
                "etadi. Lekin har bir tugun "
                "faqat qo'shnilari bilan "
                "bog'langan, demak matritsaning "
                "99,9% i nol. Bu bo'shlikni "
                "qanday ishlatish kerak va u "
                "nimaga bog'liq?"
            ),
            concepts=[
                c("Element bikrlik matritsasi",
                  "$\\mathbf{k}^e = \\int "
                  "\\mathbf{B}^T\\mathbf{D}"
                  "\\mathbf{B}\\,d\\Omega$ — "
                  "elementning o'z ichidagi "
                  "kuch–ko'chish bog'lanishi."),
                c("Moslashgan yuk vektori "
                  "(consistent load vector)",
                  "$\\mathbf{f}^e = \\int "
                  "\\mathbf{N}^T b\\,d\\Omega$ — "
                  "taqsimlangan yukning "
                  "tugunlarga **energiya "
                  "jihatdan ekvivalent** "
                  "keltirilishi."),
                c("Yig'ish (assembly)",
                  "Element matritsalarini global "
                  "tizimga qo'shish; umumiy "
                  "tugunlarda hissalar "
                  "**qo'shiladi**."),
                c("Bog'lanish jadvali "
                  "(connectivity)",
                  "Har bir elementning qaysi "
                  "global tugunlarga tegishli "
                  "ekanini ko'rsatadi — yig'ish "
                  "uchun yagona zarur "
                  "ma'lumot."),
                c("Qattiq jism rejimi "
                  "(rigid body mode)",
                  "Deformatsiyasiz ko'chish; "
                  "$\\mathbf{K}\\mathbf{r} = "
                  "\\mathbf{0}$, shuning uchun "
                  "chegaraviy shartlarsiz "
                  "$\\mathbf{K}$ singulyar."),
                c("Lenta kengligi (bandwidth)",
                  "$b = \\max|i - j|$ nolmas "
                  "elementlar uchun; yechish "
                  "narxi $\\sim n b^2$ — "
                  "raqamlashga to'g'ridan-to'g'ri "
                  "bog'liq."),
            ],
            derivation=[
                d("1. Zaif shakldan element "
                  "integraliga",
                  r"\int_\Omega \mathbf{B}^T"
                  r"\mathbf{D}\mathbf{B}\,d\Omega"
                  r"\;\mathbf{u} = \int_\Omega "
                  r"\mathbf{N}^T b\,d\Omega + "
                  r"\int_{\Gamma_t}\mathbf{N}^T"
                  r"\bar{t}\,d\Gamma",
                  "su-13 dagi zaif formulirovka "
                  "matritsa ko'rinishida. "
                  "$\\mathbf{B}$ — deformatsiya "
                  "matritsasi, $\\mathbf{D}$ — "
                  "material matritsasi "
                  "(tmm-12)."),
                d("2. Integralning elementlar "
                  "bo'yicha bo'linishi",
                  r"\int_\Omega(\cdot)\,d\Omega = "
                  r"\sum_{e=1}^{n_{el}}"
                  r"\int_{\Omega_e}(\cdot)\,"
                  r"d\Omega",
                  "**Hal qiluvchi qadam.** "
                  "Integral additiv, shuning "
                  "uchun uni element bo'yicha "
                  "bo'lish mumkin. Yig'ishning "
                  "butun asosi shu."),
                d("3. Element bikrlik matritsasi",
                  r"k^e_{ij} = \int_{-1}^{1} "
                  r"EA\,\frac{1}{J}"
                  r"\frac{dN_i}{d\xi}\cdot"
                  r"\frac{1}{J}\frac{dN_j}{d\xi}"
                  r"\;J\,d\xi",
                  "su-14 dagi almashtirish bilan. "
                  "Chiziqli elementda "
                  "$J = h/2$ va integral oson "
                  "olinadi."),
                d("4. Chiziqli element matritsasi",
                  r"\mathbf{k}^e = \frac{EA}{h}"
                  r"\begin{bmatrix} 1 & -1\\ "
                  r"-1 & 1\end{bmatrix}",
                  "Eng mashhur element "
                  "matritsasi. Uning qatorlari "
                  "yig'indisi nol — bu tasodif "
                  "emas."),
                d("5. Kvadratik element "
                  "matritsasi",
                  r"\mathbf{k}^e = \frac{EA}{3h}"
                  r"\begin{bmatrix} 7 & -8 & 1\\ "
                  r"-8 & 16 & -8\\ 1 & -8 & 7"
                  r"\end{bmatrix}",
                  "O'rta tugun eng katta "
                  "diagonal hadga ega — u "
                  "ikkala chetga ham "
                  "bog'langan."),
                d("6. Moslashgan yuk vektori",
                  r"f^e_i = \int_{-1}^{1} "
                  r"N_i\,q\,J\,d\xi",
                  "**Diqqat.** Bu taqsimlangan "
                  "yukni tugunlarga 'teng "
                  "bo'lish' emas, balki "
                  "energiya jihatdan ekvivalent "
                  "keltirishdir."),
                d("7. Kvadratik element uchun "
                  "moslashgan yuk",
                  r"\mathbf{f}^e = qh\left\{"
                  r"\tfrac16,\ \tfrac23,\ "
                  r"\tfrac16\right\}^T",
                  "**Kutilmagan natija.** "
                  "Intuitiv javob "
                  "$\\{1/3, 1/3, 1/3\\}$ "
                  "**noto'g'ri**: o'rta tugun "
                  "yukning to'rtdan uchini "
                  "oladi, chetlar esa atigi "
                  "oltidan birini."),
                d("8. Yig'ish operatori",
                  r"\mathbf{K} = \sum_e "
                  r"\mathbf{A}_e^T\,\mathbf{k}^e"
                  r"\,\mathbf{A}_e, \qquad "
                  r"\mathbf{F} = \sum_e "
                  r"\mathbf{A}_e^T\mathbf{f}^e",
                  "$\\mathbf{A}_e$ — "
                  "joylashtirish "
                  "(localization) matritsasi: "
                  "global vektordan element "
                  "erkinlik darajalarini "
                  "ajratib oladi. Amalda u "
                  "hech qachon qurilmaydi — "
                  "indekslar bilan "
                  "almashtiriladi."),
                d("9. Amaliy yig'ish algoritmi",
                  r"\mathbf{K}[\mathrm{idx}_e,"
                  r"\mathrm{idx}_e]\;"
                  r"\mathrel{+}=\;\mathbf{k}^e",
                  "Butun FEM yadrosi shu bir "
                  "qatorda. `idx_e` — "
                  "elementning global tugun "
                  "raqamlari."),
                d("10. Simmetriya",
                  r"k^e_{ij} = \int B_iD B_j = "
                  r"\int B_jD B_i = k^e_{ji} "
                  r"\;\Rightarrow\; \mathbf{K} = "
                  r"\mathbf{K}^T",
                  "$\\mathbf{D}$ simmetrik "
                  "bo'lgani uchun (tmm-12 dagi "
                  "Grin elastikligi). Simmetriya "
                  "yig'ishda saqlanadi."),
                d("11. Qattiq jism rejimi va "
                  "singulyarlik",
                  r"\mathbf{u} = \mathbf{1} "
                  r"\;\Rightarrow\; "
                  r"\boldsymbol\varepsilon = 0 "
                  r"\;\Rightarrow\; "
                  r"\mathbf{K}\mathbf{1} = "
                  r"\mathbf{0}",
                  "**Muhim xulosa.** Barcha "
                  "tugunlar bir xil siljisa "
                  "deformatsiya yo'q, demak "
                  "kuch ham yo'q. Bu "
                  "$\\mathbf{K}$ ning qator "
                  "yig'indilari nol ekanini "
                  "beradi — eng oson va eng "
                  "kuchli tekshiruv."),
                d("12. Musbat yarim aniqlik",
                  r"\mathbf{u}^T\mathbf{K}"
                  r"\mathbf{u} = 2U \ge 0",
                  "Kvadratik shakl — ikkilangan "
                  "deformatsiya energiyasi, u "
                  "hech qachon manfiy emas. "
                  "Nol faqat qattiq jism "
                  "rejimlarida."),
                d("13. Lenta kengligi",
                  r"b = \max_e\left(\max_i "
                  r"\mathrm{idx}_e^i - \min_i "
                  r"\mathrm{idx}_e^i\right) + 1",
                  "Nolmas hadlar faqat "
                  "diagonal atrofidagi "
                  "lentada. Bu **butunlay** "
                  "raqamlashga bog'liq — "
                  "fizikaga emas."),
                d("14. Yechish narxi",
                  r"\text{to'la: } O(n^3), \qquad "
                  r"\text{lentali: } O(n b^2)",
                  "**Amaliy xulosa.** "
                  "$n = 10^5$, $b = 100$ uchun "
                  "$nb^2 = 10^9$, "
                  "$n^3 = 10^{15}$ — million "
                  "marta farq. Raqamlash "
                  "tanlovi shuning uchun "
                  "muhim."),
            ],
            meaning=(
                "Butun yig'ish g'oyasi 2-qadamda: "
                "integral additiv. Shuning uchun "
                "global matritsani element "
                "hissalarining oddiy yig'indisi "
                "sifatida qurish mumkin va har "
                "bir element qolganlaridan "
                "mustaqil hisoblanadi. Amalda bu "
                "9-qadamdagi bitta qatorga "
                "qisqaradi va aynan shu qator "
                "FEM dasturining yadrosi. "
                "Matematik jihatdan 8-qadamdagi "
                "$\\mathbf{A}_e$ matritsasi "
                "chiroyli, lekin dasturda u "
                "hech qachon qurilmaydi — "
                "indeks massivi bilan "
                "almashtiriladi, chunki "
                "$\\mathbf{A}_e$ deyarli "
                "butunlay nollardan iborat. "
                "7-qadam esa eng ko'p xatoga "
                "sabab bo'ladigan joy. "
                "Taqsimlangan yukni tugunlarga "
                "'teng bo'lish' tabiiy "
                "ko'rinadi, lekin bu "
                "**noto'g'ri**. To'g'ri javob "
                "$\\int N_i q\\,dx$ va u "
                "kvadratik elementda "
                "$\\{1/6,\\ 2/3,\\ 1/6\\}$ "
                "beradi — o'rta tugun yukning "
                "to'rtdan uchini oladi. Sabab "
                "aniq: $N_2 = 1-\\xi^2$ "
                "element bo'ylab eng katta "
                "yuzaga ega, chet "
                "funksiyalari esa manfiy "
                "qismga ham ega. Faqat "
                "moslashgan vektor zaif "
                "formulirovkani aynan "
                "qanoatlantiradi va shuning "
                "uchun u tugunlardagi "
                "superkonvergensiyani saqlaydi. "
                "11-qadam amaliyotda eng "
                "foydali tekshiruvni beradi. "
                "Qattiq jism harakati "
                "deformatsiya bermaydi, demak "
                "$\\mathbf{K}\\mathbf{1} = "
                "\\mathbf{0}$: matritsaning "
                "har bir qator yig'indisi "
                "nol bo'lishi shart. Bu bir "
                "qator kod va u yig'ishdagi "
                "xatolarning katta qismini "
                "darhol ochadi — indeks "
                "xatosi, ishora xatosi, "
                "tushib qolgan element. "
                "Nihoyat 13- va 14-qadamlar "
                "muhandislik jihatdan hal "
                "qiluvchi. Lenta kengligi "
                "fizikaga emas, faqat tugun "
                "raqamlashga bog'liq: bir xil "
                "masala, bir xil to'r, "
                "boshqacha raqamlash — va "
                "yechish vaqti yuz marta "
                "farq qiladi. Bu 'bepul' "
                "tezlanish va shuning uchun "
                "barcha jiddiy paketlar "
                "avtomatik qayta raqamlashni "
                "bajaradi."
            ),
            equations=[
                eq(r"\mathbf{k}^e = \int_{\Omega_e}"
                   r"\mathbf{B}^T\mathbf{D}"
                   r"\mathbf{B}\,d\Omega, \qquad "
                   r"\mathbf{f}^e = \int_{\Omega_e}"
                   r"\mathbf{N}^T b\,d\Omega",
                   "Element bikrlik matritsasi va "
                   "moslashgan yuk vektori.",
                   "Element matritsalari"),
                eq(r"\mathbf{K}[\mathrm{idx}_e,"
                   r"\mathrm{idx}_e] "
                   r"\mathrel{+}= \mathbf{k}^e, "
                   r"\qquad \mathbf{F}"
                   r"[\mathrm{idx}_e] "
                   r"\mathrel{+}= \mathbf{f}^e",
                   "Yig'ish algoritmi — FEM "
                   "dasturining yadrosi.",
                   "Assembly"),
                eq(r"\mathbf{K} = \mathbf{K}^T, "
                   r"\quad \mathbf{u}^T\mathbf{K}"
                   r"\mathbf{u} \ge 0, \quad "
                   r"\mathbf{K}\mathbf{r} = "
                   r"\mathbf{0}",
                   "Global matritsaning majburiy "
                   "xossalari; oxirgisi qattiq "
                   "jism rejimlari uchun.",
                   "K ning xossalari"),
                eq(r"\text{narx} \sim n b^2, "
                   r"\qquad b = \max_e"
                   r"(\max\mathrm{idx}_e - "
                   r"\min\mathrm{idx}_e) + 1",
                   "Lentali yechishning narxi va "
                   "lenta kengligi.",
                   "Yechish narxi"),
            ],
            conditions=(
                "**Yig'ishdan keyin majburiy "
                "tekshiruvlar:**\n"
                "1. $\\mathbf{K} = \\mathbf{K}^T$ "
                "— simmetriya "
                "(mashina aniqligida);\n"
                "2. Har bir qator yig'indisi nol "
                "— qattiq jism rejimi;\n"
                "3. $\\mathrm{rank}(\\mathbf{K}) = "
                "n - n_{rb}$, bu yerda "
                "$n_{rb}$ — qattiq jism "
                "rejimlari soni (1D da 1, "
                "tekis masalada 3, fazoda 6);\n"
                "4. Diagonal hadlar musbat: "
                "$K_{ii} > 0$;\n"
                "5. $\\sum_i F_i$ = to'liq "
                "tashqi yuk — yuk vektorining "
                "tekshiruvi.\n\n"
                "**Chegaraviy shartlargacha:** "
                "$\\mathbf{K}$ **singulyar** "
                "bo'lishi SHART. Agar u "
                "singulyar bo'lmasa, demak "
                "yig'ishda xato bor yoki "
                "bikrlik qo'shib yuborilgan.\n\n"
                "**Xotira:** lentali saqlash "
                "$n\\times b$, profil (skyline) "
                "undan ham kam, siyrak "
                "(sparse) format eng kam. "
                "$10^5$ tugunda to'la saqlash "
                "mumkin emas.\n\n"
                "**Raqamlash:** Kathill–Makki "
                "teskari usuli (Reverse "
                "Cuthill–McKee, RCM) — "
                "standart evristika; u "
                "optimalni kafolatlamaydi, "
                "lekin tasodifiy raqamlashdan "
                "o'n barobar yaxshi natija "
                "beradi."
            ),
            worked=WorkedExample(
                statement=(
                    "Kvadratik (uch tugunli) "
                    "sterjen elementi uchun: "
                    "(a) bikrlik matritsasining "
                    "$k_{11}$ va $k_{12}$ "
                    "hadlarini integrallab "
                    "toping; (b) doimiy "
                    "$q$ yuk uchun moslashgan "
                    "yuk vektorini hisoblang; "
                    "(c) ikkita shunday elementni "
                    "yig'ing va umumiy tugundagi "
                    "hissani ko'rsating."
                ),
                given=[
                    r"N_1 = \tfrac{\xi(\xi-1)}{2}, \ "
                    r"N_2 = 1-\xi^2, \ "
                    r"N_3 = \tfrac{\xi(\xi+1)}{2}",
                    r"J = h/2, \quad B_i = "
                    r"\tfrac{2}{h}\tfrac{dN_i}{d\xi}",
                ],
                steps=[
                    st(r"\frac{dN_1}{d\xi} = "
                       r"\xi - \tfrac12, \quad "
                       r"\frac{dN_2}{d\xi} = -2\xi",
                       "Hosilalar (su-14 dan)."),
                    st(r"k_{11} = \int_{-1}^{1}EA"
                       r"\left(\tfrac{2}{h}\right)^2"
                       r"\left(\xi-\tfrac12\right)^2"
                       r"\frac{h}{2}d\xi = "
                       r"\frac{2EA}{h}\int_{-1}^{1}"
                       r"\left(\xi-\tfrac12\right)^2"
                       r"d\xi",
                       "Yakobianlar qisqardi: "
                       "$(2/h)^2\\cdot(h/2) = "
                       "2/h$."),
                    st(r"\int_{-1}^{1}\left(\xi^2 - "
                       r"\xi + \tfrac14\right)d\xi = "
                       r"\tfrac23 - 0 + \tfrac12 = "
                       r"\tfrac76",
                       "Toq had nolga integrallanadi."),
                    st(r"k_{11} = \frac{2EA}{h}\cdot"
                       r"\frac76 = \frac{7EA}{3h}",
                       "**Birinchi had topildi.**"),
                    st(r"k_{12} = \frac{2EA}{h}"
                       r"\int_{-1}^{1}\left(\xi-"
                       r"\tfrac12\right)(-2\xi)d\xi "
                       r"= \frac{2EA}{h}\int_{-1}^{1}"
                       r"\left(-2\xi^2+\xi\right)d\xi",
                       "Ikkinchi had."),
                    st(r"= \frac{2EA}{h}\left(-\tfrac43"
                       r"\right) = -\frac{8EA}{3h}",
                       "Shunday qilib "
                       "$\\mathbf{k}^e = "
                       "\\frac{EA}{3h}"
                       "[[7,-8,1],[-8,16,-8],"
                       "[1,-8,7]]$."),
                    st(r"\text{(b) } f_2 = "
                       r"\int_{-1}^{1}q(1-\xi^2)"
                       r"\frac{h}{2}d\xi = "
                       r"\frac{qh}{2}\left(2 - "
                       r"\tfrac23\right) = "
                       r"\frac{2qh}{3}",
                       "**O'rta tugun** yukning "
                       "to'rtdan uchini oladi."),
                    st(r"f_1 = \int_{-1}^{1}q\,"
                       r"\frac{\xi(\xi-1)}{2}"
                       r"\frac{h}{2}d\xi = "
                       r"\frac{qh}{4}\left(\tfrac23"
                       r"\right) = \frac{qh}{6}",
                       "Chet tugunlar atigi "
                       "oltidan bir."),
                    st(r"\sum f_i = \frac{qh}{6} + "
                       r"\frac{2qh}{3} + "
                       r"\frac{qh}{6} = qh \quad "
                       r"\checkmark",
                       "**Tekshiruv:** yig'indi "
                       "to'liq yukka teng — "
                       "muvozanat saqlanadi."),
                    st(r"\text{(c) tugunlar: } "
                       r"\{1,2,3\} \text{ va } "
                       r"\{3,4,5\}",
                       "Ikkinchi elementning "
                       "birinchi tuguni — "
                       "birinchisining oxirgisi."),
                    st(r"K_{33} = k^{(1)}_{33} + "
                       r"k^{(2)}_{11} = "
                       r"\frac{7EA}{3h} + "
                       r"\frac{7EA}{3h} = "
                       r"\frac{14EA}{3h}",
                       "**Umumiy tugunda "
                       "hissalar qo'shiladi** — "
                       "yig'ishning butun "
                       "mohiyati shu."),
                    st(r"F_3 = \frac{qh}{6} + "
                       r"\frac{qh}{6} = "
                       r"\frac{qh}{3}",
                       "Yuk vektorida ham "
                       "xuddi shunday."),
                ],
                answer=(
                    "(a) $k_{11} = 7EA/3h$, "
                    "$k_{12} = -8EA/3h$; to'liq "
                    "matritsa "
                    "$\\frac{EA}{3h}"
                    "[[7,-8,1],[-8,16,-8],"
                    "[1,-8,7]]$. "
                    "(b) $\\mathbf{f}^e = "
                    "qh\\{1/6,\\ 2/3,\\ 1/6\\}$ "
                    "— yig'indisi $qh$ ga teng, "
                    "lekin taqsimot teng emas. "
                    "(c) Umumiy tugunda ikkala "
                    "elementning hissalari "
                    "qo'shiladi: "
                    "$K_{33} = 14EA/3h$, "
                    "$F_3 = qh/3$."
                ),
                engineering_note=(
                    "(b) qismidagi natija — bu "
                    "mavzudagi eng ko'p xatoga "
                    "sabab bo'ladigan joy. "
                    "Taqsimlangan yukni uchta "
                    "tugunga teng bo'lish "
                    "($1/3$ har biriga) tabiiy "
                    "ko'rinadi va ko'p talaba "
                    "shunday qiladi, lekin bu "
                    "noto'g'ri. To'g'ri javob "
                    "$\\{1/6, 2/3, 1/6\\}$ va "
                    "farq katta: o'rta tugun "
                    "ikki barobar ko'p, chet "
                    "tugunlar esa ikki barobar "
                    "kam oladi. Bundan ham "
                    "g'alati ko'rinadigan hol — "
                    "kubik elementda chet "
                    "tugunlar $1/8$, ichki "
                    "tugunlar $3/8$ oladi. "
                    "Hatto **manfiy** hadlar "
                    "ham bo'lishi mumkin: "
                    "Ermit (balka) elementida "
                    "burchak erkinlik "
                    "darajalariga mos keladigan "
                    "yuk hadlari moment "
                    "ko'rinishida chiqadi va "
                    "ishorasi qarama-qarshi "
                    "bo'ladi. Bu xato jimgina "
                    "o'tadi: hisob ishlaydi, "
                    "natija ishonarli "
                    "ko'rinadi, faqat noto'g'ri. "
                    "Yagona ishonchli usul — "
                    "har doim "
                    "$\\int\\mathbf{N}^Tq$ ni "
                    "hisoblash va yig'indini "
                    "to'liq yuk bilan "
                    "solishtirish."
                ),
            ),
            computation=Computation(
                caption=(
                    "Element matritsalarini qurish, "
                    "yig'ish, to'rtta majburiy "
                    "xossani tekshirish va "
                    "raqamlashning yechish narxiga "
                    "ta'sirini o'lchash."
                ),
                code='''"""Element matritsalari va global tizimni yig'ish."""
from collections import deque

import numpy as np
from labkit import PARAMS, note, series, table, value

n_el = int(PARAMS.get("n_el", 6))
p_ord = int(PARAMS.get("p_ord", 1))
nx_g = int(PARAMS.get("nx_g", 5))
ny_g = int(PARAMS.get("ny_g", 21))

EA = 1000.0
L = 1.0
q0 = 100.0


def lagrange_N(xi, nodes):
    n = len(nodes)
    xi = np.asarray(xi, dtype=float)
    N = np.ones((n,) + xi.shape)
    dN = np.zeros((n,) + xi.shape)
    for i in range(n):
        for j in range(n):
            if j == i:
                continue
            N[i] *= (xi - nodes[j])/(nodes[i] - nodes[j])
        for j in range(n):
            if j == i:
                continue
            term = np.ones_like(xi)
            for k in range(n):
                if k == i or k == j:
                    continue
                term *= (xi - nodes[k])/(nodes[i] - nodes[k])
            dN[i] += term/(nodes[i] - nodes[j])
    return N, dN


def elem_matrices(p, h, q):
    """p-tartibli sterjen elementining k va f matritsalari."""
    nodes = np.linspace(-1.0, 1.0, p + 1)
    gx, gw = np.polynomial.legendre.leggauss(p + 2)
    N, dN = lagrange_N(gx, nodes)
    J = h/2
    ke = np.zeros((p + 1, p + 1))
    fe = np.zeros(p + 1)
    for g_ in range(len(gx)):
        B = dN[:, g_]/J
        ke += EA*np.outer(B, B)*gw[g_]*J
        fe += q*N[:, g_]*gw[g_]*J
    return ke, fe


# --- (1) Element matritsalari: klassik natijalar ---
h1 = L/n_el
den = {1: 1, 2: 3, 3: 40}      # har bir tartibning tabiiy maxraji
for p in [1, 2, 3]:
    ke, fe = elem_matrices(p, h1, q0)
    kk = ke*den[p]*h1/EA
    rows_k = [[f"{v:.4f}" for v in row] for row in kk]
    table(f"Bikrlik matritsasi, p = {p} — EA/({den[p]}h) birligida",
          [f"ustun {i+1}" for i in range(p + 1)], rows_k)
    table(f"Moslashgan yuk vektori, p = {p} (q*h birligida)",
          [f"tugun {i+1}" for i in range(p + 1)],
          [[f"{v:.6f}" for v in fe/(q0*h1)]])
    value(f"p = {p}: yuk yig'indisi / (q*h)",
          float(np.sum(fe)/(q0*h1)), "—")
    value(f"p = {p}: matritsa butun sonlardan chetlanishi",
          float(np.max(np.abs(kk - np.round(kk)))), "—")

ke2, fe2 = elem_matrices(2, h1, q0)
value("k11*3h/EA (kutilgan 7)", float(ke2[0, 0]*3*h1/EA), "—")
value("k12*3h/EA (kutilgan -8)", float(ke2[0, 1]*3*h1/EA), "—")
value("k22*3h/EA (kutilgan 16)", float(ke2[1, 1]*3*h1/EA), "—")
note("Kvadratik element matritsasi klassik (EA/3h)*[[7,-8,1],[-8,16,-8],"
     "[1,-8,7]] qiymatini mashina aniqligida takrorladi. Moslashgan yuk "
     "vektori esa {1/6, 2/3, 1/6} - INTUITIV {1/3, 1/3, 1/3} EMAS. "
     "Kubik elementda {1/8, 3/8, 3/8, 1/8}. Barcha holatlarda yig'indi "
     "aynan q*h ga teng: muvozanat saqlanadi, taqsimot esa teng emas.")

# --- (2) Yig'ish va MAJBURIY tekshiruvlar ---
def assemble(n, p, q=q0, order=None):
    h = L/n
    ke, fe = elem_matrices(p, h, q)
    ndof = n*p + 1
    K = np.zeros((ndof, ndof))
    F = np.zeros(ndof)
    els = range(n) if order is None else order
    for e in els:
        idx = np.arange(e*p, e*p + p + 1)
        K[np.ix_(idx, idx)] += ke          # FEM yadrosi: shu bir qator
        F[idx] += fe
    return K, F


K, F = assemble(n_el, p_ord)
ndof = n_el*p_ord + 1
value("Erkinlik darajalari soni", ndof, "—")
value("1) Simmetriya: max|K - K^T|", float(np.max(np.abs(K - K.T))), "N/m")
value("2) Qattiq jism: max|K @ 1|",
      float(np.max(np.abs(K @ np.ones(ndof)))), "N")
value("3) Rangi", int(np.linalg.matrix_rank(K)), "—")
value("3) Kutilgan rang (n - 1)", ndof - 1, "—")
ev = np.linalg.eigvalsh(K)
value("4) Eng kichik xos qiymat", float(ev[0]), "N/m")
value("4) Keyingi xos qiymat", float(ev[1]), "N/m")
value("5) Yuk yig'indisi", float(np.sum(F)), "N")
value("5) Aniq to'liq yuk (q*L)", q0*L, "N")
value("Diagonal hadlarning minimumi", float(np.min(np.diag(K))), "N/m")
gap = np.log10(ev[1]/max(abs(ev[0]), 1e-300))
value("Xos qiymatlar orasidagi uzilish (o'nlik tartib)", float(gap), "—")
note(f"Beshta majburiy tekshiruv ham bajarildi. Eng kichik xos qiymat "
     f"mashina noliga teng, keyingisi esa undan {gap:.0f} o'nlik tartib "
     f"katta - demak singulyarlik ANIQ bitta qattiq jism rejimidan "
     f"keladi, sonli shovqindan emas. Bu farqni ko'rish muhim: agar "
     f"ikkinchi xos qiymat ham kichik bo'lsa, modelda mahkamlanmagan "
     f"mexanizm bor. Chegaraviy shartlargacha K singulyar bo'lishi "
     f"SHART; agar u teskarilanuvchi bo'lsa, yig'ishda xato bor.")

# Yig'ish tartibidan mustaqillik
rng = np.random.default_rng(7)
Kr, Fr = assemble(n_el, p_ord, order=rng.permutation(n_el))
value("Yig'ish tartibidan mustaqillik: max|dK|",
      float(np.max(np.abs(K - Kr))), "N/m")
value("Yig'ish tartibidan mustaqillik: max|dF|",
      float(np.max(np.abs(F - Fr))), "N")

# Energiya tekshiruvi: u^T K u = 2U
# Deformatsiya energiyasini element bo'ylab Gauss bilan integrallaymiz -
# bu istalgan p uchun to'g'ri (nuqtalar ayirmasi faqat p = 1 da ishlaydi)
u = np.concatenate([[0.0], np.linalg.solve(K[1:, 1:], F[1:])])
U_mat = 0.5*float(u @ K @ u)

h_e = L/n_el
nodes_e = np.linspace(-1.0, 1.0, p_ord + 1)
gx_e, gw_e = np.polynomial.legendre.leggauss(p_ord + 2)
_, dNe_ = lagrange_N(gx_e, nodes_e)
U_int = 0.0
for e in range(n_el):
    idx = np.arange(e*p_ord, e*p_ord + p_ord + 1)
    eps_g = np.sum((dNe_/(h_e/2))*u[idx][:, None], axis=0)
    U_int += 0.5*EA*float(np.sum(eps_g**2*gw_e)*(h_e/2))
U_exact = 0.5*q0**2*L**3/(3*EA)     # analitik: eps = q0(L-x)/EA
value("Energiya: 0.5*u^T K u", U_mat, "J")
value("Energiya: 0.5*EA*int(eps^2) dx", U_int, "J")
value("Energiya nisbiy farqi",
      abs(U_mat - U_int)/abs(U_int)*100, "%")
value("Energiya: aniq yechim", U_exact, "J")
value("Diskret energiya aniqdan oshib ketdimi",
      float(U_mat - U_exact), "J")
note(f"Deformatsiya energiyasi ikki mustaqil yo'ldan hisoblandi: "
     f"matritsa kvadratik shakli va deformatsiya maydonining bevosita "
     f"integrali. Ular ustma-ust tushdi - demak yig'ilgan K haqiqatan "
     f"ham zaif formulirovkadagi energiya operatorini ifodalaydi. "
     f"Bundan tashqari diskret energiya aniq qiymatdan OSHMADI "
     f"(farq {U_mat - U_exact:+.3e} J) - su-13 dagi quyi chegara "
     f"xossasi yig'ishdan keyin ham saqlanadi.")

xg_n = np.linspace(0.0, L, ndof)
series("Ko'chish u(x)", xg_n.tolist(), (u*1e3).tolist(),
       xlabel="x, m", ylabel="u, mm")

# --- (3) MOSLASHGAN va JAMLANGAN yuk vektori ---
# Chiziqli o'zgaruvchi yuk q(x) = q0*x/L uchun
def assemble_lin(n, lumped):
    h = L/n
    ke, _ = elem_matrices(1, h, 0.0)
    K = np.zeros((n + 1, n + 1))
    F = np.zeros(n + 1)
    gx, gw = np.polynomial.legendre.leggauss(3)
    for e in range(n):
        x1, x2 = e*h, (e + 1)*h
        K[e:e+2, e:e+2] += ke
        if lumped:
            Q = q0*((x1 + x2)/2)/L*h        # element markazidagi yuk
            F[e:e+2] += np.array([Q/2, Q/2])
        else:
            xg = (x1 + x2)/2 + gx*h/2
            N1 = (x2 - xg)/h
            N2 = (xg - x1)/h
            qg = q0*xg/L
            F[e] += float(np.sum(N1*qg*gw)*h/2)
            F[e+1] += float(np.sum(N2*qg*gw)*h/2)
    return K, F


def u_exact(x):
    return q0/(EA*L)*(L**2*x/2 - x**3/6)


rows_l = []
for n in [2, 4, 8, 16, 32]:
    Kc, Fc = assemble_lin(n, False)
    uc = np.concatenate([[0.0], np.linalg.solve(Kc[1:, 1:], Fc[1:])])
    Kl, Fl = assemble_lin(n, True)
    ul = np.concatenate([[0.0], np.linalg.solve(Kl[1:, 1:], Fl[1:])])
    xs = np.linspace(0.0, L, n + 1)
    ex = u_exact(xs)
    ec = np.max(np.abs(uc - ex))/np.max(ex)*100
    el_ = np.max(np.abs(ul - ex))/np.max(ex)*100
    rows_l.append([n, f"{ec:.3e}", f"{el_:.6f}",
                   f"{np.sum(Fc):.4f}", f"{np.sum(Fl):.4f}"])
table("Moslashgan va jamlangan yuk vektori (q = q0*x/L)",
      ["elementlar", "moslashgan xato, %", "jamlangan xato, %",
       "sum F moslashgan", "sum F jamlangan"], rows_l)
note("MUHIM NATIJA. Moslashgan yuk vektori tugunlarda AYNAN yechim "
     "beradi (xato 1e-14 darajasida) - ya'ni su-13 dagi bir o'lchovli "
     "superkonvergensiya saqlanadi. Jamlangan (lumped) vektor esa uni "
     "BUZADI: xato 6.25% dan boshlanib, to'r zichlashganda aynan to'rt "
     "barobar kamayadi (ikkinchi tartib). Ikkala vektorning yig'indisi "
     "bir xil - demak muvozanat ikkalasida ham saqlanadi, farq faqat "
     "taqsimotda. Bu jamlangan vektorning xatosi nima uchun jimgina "
     "o'tishini tushuntiradi.")

# --- (4) LENTA KENGLIGI va qayta raqamlash ---
def grid_mesh(nx, ny, direction):
    """nx x ny tugunli to'r, Q4 elementlar."""
    idx = np.zeros((nx, ny), dtype=int)
    k = 0
    if direction == "x":
        for j in range(ny):
            for i in range(nx):
                idx[i, j] = k
                k += 1
    else:
        for i in range(nx):
            for j in range(ny):
                idx[i, j] = k
                k += 1
    conn = []
    for i in range(nx - 1):
        for j in range(ny - 1):
            conn.append([idx[i, j], idx[i+1, j], idx[i+1, j+1], idx[i, j+1]])
    return np.array(conn), nx*ny


def half_bw(conn):
    return int(max(e.max() - e.min() for e in conn)) + 1


def adjacency(conn, n):
    adj = [set() for _ in range(n)]
    for e in conn:
        for a in e:
            for b in e:
                if a != b:
                    adj[a].add(b)
    return [sorted(s) for s in adj]


def rcm(conn, n):
    """Teskari Kathill-Makki qayta raqamlash."""
    adj = adjacency(conn, n)
    deg = [len(a) for a in adj]
    seen = [False]*n
    order = []
    while len(order) < n:
        start = min((i for i in range(n) if not seen[i]),
                    key=lambda i: deg[i])
        Q = deque([start])
        seen[start] = True
        while Q:
            v = Q.popleft()
            order.append(v)
            for w in sorted(adj[v], key=lambda w: deg[w]):
                if not seen[w]:
                    seen[w] = True
                    Q.append(w)
    perm = np.array(order[::-1])
    inv = np.zeros(n, dtype=int)
    inv[perm] = np.arange(n)
    return inv


conn_x, n_nod = grid_mesh(nx_g, ny_g, "x")
conn_y, _ = grid_mesh(nx_g, ny_g, "y")
rng2 = np.random.default_rng(0)
conn_r = rng2.permutation(n_nod)[conn_y]
inv_rcm = rcm(conn_r, n_nod)
conn_rcm = inv_rcm[conn_r]

rows_b = []
for name, cn in [("qisqa yo'nalish bo'yicha", conn_x),
                 ("uzun yo'nalish bo'yicha", conn_y),
                 ("tasodifiy", conn_r),
                 ("tasodifiy + RCM", conn_rcm)]:
    b = half_bw(cn)
    rows_b.append([name, b, n_nod*b*b,
                   f"{n_nod*b*b/(n_nod*half_bw(conn_x)**2):.1f}x"])
table(f"Lenta kengligi va yechish narxi ({nx_g} x {ny_g} to'r, "
      f"{n_nod} tugun)",
      ["raqamlash", "yarim lenta b", "narx ~ n*b^2", "eng yaxshiga nisbatan"],
      rows_b)
value("Tugunlar soni", n_nod, "—")
value("Eng yaxshi lenta kengligi", half_bw(conn_x), "—")
value("Tasodifiy raqamlashda lenta kengligi", half_bw(conn_r), "—")
value("RCM dan keyin lenta kengligi", half_bw(conn_rcm), "—")
value("RCM ning foydasi", half_bw(conn_r)/half_bw(conn_rcm), "barobar")
note(f"Bir xil masala, bir xil to'r, bir xil fizika - faqat tugun "
     f"raqamlari boshqacha. Tasodifiy raqamlashda lenta kengligi "
     f"{half_bw(conn_r)} (deyarli to'la matritsa), qisqa yo'nalish "
     f"bo'yicha esa {half_bw(conn_x)}. Narx nisbati "
     f"{n_nod*half_bw(conn_r)**2/(n_nod*half_bw(conn_x)**2):.0f} "
     f"barobar. RCM tasodifiy raqamlashni "
     f"{half_bw(conn_r)/half_bw(conn_rcm):.0f} barobar yaxshiladi, "
     f"lekin optimalga ({half_bw(conn_x)}) yetmadi - u evristika, "
     f"kafolat emas.")

# Matritsaning to'ldirilish xaritasi
def sparsity_profile(conn, n):
    prof = np.zeros(n, dtype=int)
    for e in conn:
        for a in e:
            prof[a] = max(prof[a], a - int(e.min()))
    return prof


series("Profil: qisqa yo'nalish", list(range(n_nod)),
       sparsity_profile(conn_x, n_nod).tolist(),
       xlabel="tugun raqami", ylabel="profil balandligi")
series("Profil: tasodifiy", list(range(n_nod)),
       sparsity_profile(conn_r, n_nod).tolist(),
       xlabel="tugun raqami", ylabel="profil balandligi")
series("Profil: RCM", list(range(n_nod)),
       sparsity_profile(conn_rcm, n_nod).tolist(),
       xlabel="tugun raqami", ylabel="profil balandligi")

# Xotira taqqoslash
rows_m = []
for n_ in [1_000, 10_000, 100_000]:
    b_ = int(2*np.sqrt(n_))
    rows_m.append([n_, f"{n_*n_*8/1e9:.3f}", f"{n_*b_*8/1e6:.2f}", b_,
                   f"{n_**3/1e9:.1f}", f"{n_*b_*b_/1e9:.4f}"])
table("To'la va lentali saqlashning taqqoslanishi (2D to'r, b ~ 2*sqrt(n))",
      ["n", "to'la xotira, GB", "lentali xotira, MB", "b",
       "to'la amallar, mlrd", "lentali amallar, mlrd"], rows_m)
note("100 000 erkinlik darajasida to'la matritsa 80 GB talab qiladi va "
     "amalda saqlab bo'lmaydi; lentali saqlash esa atigi 506 MB. Amallar "
     "soni bo'yicha farq undan ham katta. Aynan shu sabab FEM "
     "paketlari hech qachon to'la matritsa bilan ishlamaydi.")
''',
                parameters=[
                    p("n_el", "Elementlar soni", 2.0, 40.0, 6.0, 1.0),
                    p("p_ord", "Element tartibi", 1.0, 3.0, 1.0, 1.0),
                    p("nx_g", "To'r: qisqa yo'nalish", 3.0, 15.0, 5.0, 1.0),
                    p("ny_g", "To'r: uzun yo'nalish", 5.0, 40.0, 21.0, 1.0),
                ],
                expected_output=(
                    "Kvadratik element matritsasi "
                    "klassik "
                    "$\\frac{EA}{3h}"
                    "[[7,-8,1],[-8,16,-8],"
                    "[1,-8,7]]$ ni aynan "
                    "takrorlaydi, moslashgan yuk "
                    "vektori esa "
                    "$\\{1/6, 2/3, 1/6\\}$ "
                    "beradi. Yig'ishdan keyin "
                    "beshta tekshiruv ham "
                    "bajariladi: simmetriya va "
                    "qattiq jism rejimi aynan "
                    "nol, rang $n-1$, eng kichik "
                    "xos qiymat mashina noli, "
                    "yuk yig'indisi $qL$ ga "
                    "teng. Yig'ish tartibi "
                    "natijaga umuman ta'sir "
                    "qilmaydi. Moslashgan yuk "
                    "vektori tugunlarda aynan "
                    "yechim beradi, jamlangan "
                    "esa 6,25% dan boshlanib "
                    "ikkinchi tartibda "
                    "kamayadigan xato "
                    "kiritadi. Lenta kengligi "
                    "raqamlashga qarab 7 dan "
                    "104 gacha o'zgaradi — "
                    "yechish narxida 221 "
                    "barobar farq; RCM uni "
                    "10 barobar yaxshilaydi."
                ),
            ),
            visual=vis(
                kind="Yig'ish jarayoni va matritsa to'ldirilishi",
                tool="React/SVG + Manim",
                description=(
                    "Element matritsalarining "
                    "global tizimga "
                    "joylashtirilishi va lenta "
                    "kengligining raqamlashga "
                    "bog'liqligi."
                ),
                how_to_draw=(
                    "React/SVG: chap panelda "
                    "sterjen elementlarga "
                    "bo'lingan holda "
                    "ko'rsatiladi, o'ng panelda "
                    "esa global matritsa "
                    "katakchalar to'ri sifatida. "
                    "'Keyingi element' tugmasi "
                    "bosilganda tanlangan "
                    "element yonib turadi va "
                    "uning $(p+1)^2$ ta hissasi "
                    "matritsadagi mos "
                    "katakchalarga **qo'shiladi** "
                    "— umumiy tugundagi "
                    "katakcha ikki marta "
                    "yonganda uning rangi "
                    "to'qlashadi va yon "
                    "tomonda $K_{33} = "
                    "k^{(1)}_{33} + k^{(2)}_{11}$ "
                    "yozuvi chiqadi. Pastki "
                    "panelda ikki o'lchovli "
                    "to'rning nol bo'lmagan "
                    "hadlari xaritasi: uchta "
                    "variant yonma-yon — "
                    "tartibli raqamlash (ingichka "
                    "lenta), tasodifiy (butun "
                    "maydon bo'ylab sochilgan "
                    "nuqtalar) va RCM dan keyin "
                    "(yana ingichka lenta). Har "
                    "birining ostida $b$ va "
                    "$nb^2$ qiymatlari; "
                    "tasodifiy variantda narx "
                    "ko'rsatkichi qizil rangda. "
                    "'RCM qo'lla' tugmasi "
                    "nuqtalarni animatsiya bilan "
                    "lentaga yig'adi."
                ),
            ),
            interp=(
                "Element matritsalari klassik "
                "qiymatlarni mashina aniqligida "
                "takrorladi va bu kodning "
                "to'g'riligining birinchi "
                "dalili. Moslashgan yuk "
                "vektorining "
                "$\\{1/6, 2/3, 1/6\\}$ "
                "natijasi esa intuitiv "
                "kutilmagan, lekin uning "
                "yig'indisi aynan $qh$ ga teng: "
                "muvozanat saqlanadi, taqsimot "
                "esa teng emas. Yig'ishdan "
                "keyingi beshta tekshiruv ham "
                "aynan bajarildi. Ulardan eng "
                "nozigi — xos qiymatlar: eng "
                "kichigi mashina noli, "
                "keyingisi esa undan 15 tartib "
                "katta. Bu farq muhim, chunki u "
                "singulyarlikning **aniq bitta** "
                "qattiq jism rejimidan "
                "kelayotganini ko'rsatadi; agar "
                "ikkinchi xos qiymat ham kichik "
                "bo'lsa, demak modelda "
                "mahkamlanmagan mexanizm bor. "
                "Yig'ish tartibidan mustaqillik "
                "aynan nol chiqdi — bu "
                "parallellashtirish uchun "
                "nazariy asos. Energiya "
                "tekshiruvi yana bir mustaqil "
                "tasdiq beradi: "
                "$\\tfrac12\\mathbf{u}^T"
                "\\mathbf{K}\\mathbf{u}$ va "
                "deformatsiya maydonining "
                "bevosita integrali ustma-ust "
                "tushdi, va diskret energiya "
                "aniq qiymatdan oshmadi — "
                "su-13 dagi quyi chegara "
                "xossasi yig'ishdan keyin ham "
                "kuchda. $p = 1$ da farq "
                "$-0{,}0116$ J, $p \\ge 2$ da "
                "esa nol, chunki bu masalaning "
                "aniq yechimi kvadratik va "
                "kvadratik element uni to'liq "
                "ifodalaydi. Eng muhim "
                "amaliy natija esa uchinchi "
                "tajribada: moslashgan yuk "
                "vektori tugunlarda aynan "
                "yechim beradi, ya'ni su-13 "
                "dagi superkonvergensiyani "
                "saqlaydi, jamlangan vektor "
                "esa uni buzadi va 6,25% dan "
                "boshlanadigan, ikkinchi "
                "tartibda kamayadigan xato "
                "kiritadi. Ikkala vektorning "
                "yig'indisi bir xil, shuning "
                "uchun muvozanat tekshiruvi "
                "bu xatoni **ushlamaydi** — "
                "u jimgina o'tadi va natija "
                "ishonarli ko'rinadi. "
                "To'rtinchi tajriba esa "
                "muhandislik jihatdan eng "
                "qimmatli xulosani beradi: "
                "bir xil masala, bir xil to'r, "
                "bir xil fizika — faqat tugun "
                "raqamlari boshqacha, va "
                "yechish narxi 221 barobar "
                "farq qiladi. RCM tasodifiy "
                "raqamlashni 10 barobar "
                "yaxshilaydi, lekin optimalga "
                "yetmaydi — u evristika, "
                "kafolat emas, va buni "
                "bilish kerak."
            ),
            mistakes=[
                "Taqsimlangan yukni tugunlarga "
                "teng bo'lish. To'g'ri yo'l — "
                "$\\int\\mathbf{N}^Tq$; "
                "kvadratik elementda "
                "$\\{1/6, 2/3, 1/6\\}$, "
                "$\\{1/3,1/3,1/3\\}$ emas.",
                "Chegaraviy shartlargacha "
                "$\\mathbf{K}$ ning "
                "singulyarligini xato deb "
                "hisoblash. Aksincha — u "
                "singulyar bo'lishi **shart**.",
                "Qator yig'indisi tekshiruvini "
                "o'tkazib yuborish. Bu bir "
                "qator kod yig'ishdagi "
                "xatolarning katta qismini "
                "darhol ochadi.",
                "Tugunlarni ixtiyoriy "
                "raqamlash. Lenta kengligi "
                "shundan o'nlab marta o'sadi "
                "va yechish vaqti yuz barobar "
                "uzayadi.",
                "Faqat yuk yig'indisini "
                "tekshirish bilan "
                "cheklanish. Jamlangan yuk "
                "vektori bu tekshiruvdan "
                "o'tadi, lekin noto'g'ri "
                "taqsimot beradi.",
            ],
            quiz=[
                q("Yig'ishning matematik asosi "
                  "nima?",
                  "Integralning additivligi: "
                  "$\\int_\\Omega = \\sum_e "
                  "\\int_{\\Omega_e}$ — shuning "
                  "uchun global matritsa element "
                  "hissalarining yig'indisi.",
                  "konseptual"),
                q("Kvadratik element uchun doimiy "
                  "$q$ yukning moslashgan "
                  "vektori qanday va nega "
                  "$\\{1/3,1/3,1/3\\}$ emas?",
                  "$qh\\{1/6, 2/3, 1/6\\}$. "
                  "Sababi $\\int N_i q$: "
                  "$N_2 = 1-\\xi^2$ eng katta "
                  "yuzaga ega, chet "
                  "funksiyalari esa manfiy "
                  "qismga ham ega.", "hisob"),
                q("Chegaraviy shartlargacha "
                  "$\\mathbf{K}$ nima uchun "
                  "singulyar?",
                  "Qattiq jism harakati "
                  "deformatsiya bermaydi: "
                  "$\\mathbf{K}\\mathbf{1} = "
                  "\\mathbf{0}$. 1D da bitta, "
                  "tekis masalada uchta, fazoda "
                  "oltita nol xos qiymat.",
                  "konseptual"),
                q("Kod yig'ishdan keyin qaysi "
                  "beshta tekshiruvni bajaradi?",
                  "Simmetriya, qator "
                  "yig'indisining noli, rang "
                  "$n-1$ ga tengligi, eng "
                  "kichik xos qiymatning "
                  "noliga yaqinligi va yuk "
                  "yig'indisining to'liq yukka "
                  "tengligi.", "kod"),
                q("Moslashgan va jamlangan yuk "
                  "vektorlari orasidagi farq "
                  "natijada qanday ko'rinadi?",
                  "Moslashgan vektor tugunlarda "
                  "aynan yechim beradi "
                  "(superkonvergensiya "
                  "saqlanadi), jamlangan esa "
                  "6,25% dan boshlanib "
                  "$O(h^2)$ kamayadigan xato "
                  "kiritadi; yig'indi ikkalasida "
                  "bir xil.", "talqin"),
                q("Lenta kengligi nimaga bog'liq "
                  "va u nima uchun muhim?",
                  "Faqat tugun raqamlashga, "
                  "fizikaga emas. Yechish "
                  "narxi $\\sim nb^2$, shuning "
                  "uchun bir xil masalada "
                  "raqamlash tanlovi yuz "
                  "barobar farq berishi "
                  "mumkin.", "talqin"),
                q("RCM nima qiladi va u "
                  "optimalni kafolatlaydimi?",
                  "Graf bo'ylab kengligiga "
                  "qidirish bilan tugunlarni "
                  "qayta raqamlab lenta "
                  "kengligini kamaytiradi. "
                  "Kafolatlamaydi: kodda u "
                  "tasodifiy raqamlashni "
                  "10 barobar yaxshiladi, "
                  "lekin optimal 7 o'rniga "
                  "10 berdi.", "kod"),
            ],
            bridge=(
                "Element matritsalarini qurish "
                "va yig'ish tayyor, lekin biz "
                "integrallarni Gauss "
                "kvadraturasi bilan hisobladik "
                "va necha nuqta kerakligini "
                "asoslamadik. Keyingi mavzuda "
                "shu savolga javob beramiz — "
                "va kutilmagan narsa aniqlanadi: "
                "ba'zan integralni **kamroq** "
                "nuqta bilan hisoblash "
                "natijani yaxshilaydi."
            ),
            research=(
                "Yig'ish va saqlashni "
                "chuqurlashtiring. "
                "(1) Frontal va ko'p frontli "
                "(multifrontal) usullarni "
                "o'rganing: ular yig'ish va "
                "yechishni birlashtiradi va "
                "global matritsani hech qachon "
                "to'liq qurmaydi — bu xotira "
                "talabini qanday kamaytiradi? "
                "(2) Siyrak matritsalarning "
                "CSR va skyline formatlarini "
                "taqqoslang: qaysi biri "
                "to'g'ri yechuvchiga, qaysi "
                "biri iterativ yechuvchiga "
                "mos? (3) To'ldirilish "
                "(fill-in) hodisasini "
                "o'rganing: LU yoyilishida "
                "nol hadlar nolmas bo'ladi — "
                "minimal daraja (minimum "
                "degree) va ichki ajratish "
                "(nested dissection) buni "
                "qanday kamaytiradi? "
                "(4) Element matritsalarini "
                "parallel hisoblash va "
                "yig'ishdagi poyga holatini "
                "(race condition) ko'rib "
                "chiqing: rang berish "
                "(colouring) yondashuvi "
                "qanday ishlaydi?"
            ),
            manim_ref=manim(
                scene="AssemblyScene",
                module="manim/scenes/su_fem.py",
                title="Global tizimni yig'ish",
                summary=(
                    "To'rt elementli sterjen "
                    "ko'rsatiladi va element "
                    "matritsalari birin-ketin "
                    "global matritsaga "
                    "'uchib boradi'. Umumiy "
                    "tugunlarda katakchalar "
                    "ustma-ust tushadi va "
                    "qiymatlar qo'shilib "
                    "boradi. Oxirida "
                    "matritsaning qator "
                    "yig'indilari hisoblanadi "
                    "va barchasi nol chiqadi — "
                    "qattiq jism rejimining "
                    "ko'rinishi."
                ),
            ),
        ),
    ),
]
