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
]
