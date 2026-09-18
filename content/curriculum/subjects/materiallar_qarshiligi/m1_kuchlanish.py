"""MQ / 1-modul: Kuchlanish, deformatsiya va mustahkamlik sharti (mq-01 … mq-06)."""

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

S = "materiallar-qarshiligi"
M = "mq-m1"

TOPICS = [
    Topic(
        id="mq-01",
        subject_id=S,
        module_id=M,
        order=1,
        title="Materiallar qarshiligi predmeti, asosiy gipotezalar va hisob sxemasi",
        description=(
            "Deformatsiyalanuvchi jism modeli, fanning asosiy gipotezalari, real "
            "konstruksiyani hisob sxemasiga keltirish metodikasi."
        ),
        learning_objective=(
            "Fanning gipotezalarini va ularning qo'llanish chegaralarini tushuntirish, "
            "real konstruksiyadan hisob sxemasini tuzish."
        ),
        prerequisites=["nm-10", "nm-11"],
        mathematical_core=(
            "Uzluksiz funksiyalar, superpozitsiya prinsipi, chiziqli munosabatlar, "
            "idealizatsiya va modellashtirish xatoligi."
        ),
        engineering_application=(
            "Har qanday konstruksiyani hisoblashning birinchi qadami: qaysi elementni "
            "sterjen, qaysi birini plastina deb olish."
        ),
        computational_component=(
            "Sodda konstruksiya uchun ikki xil hisob sxemasini taqqoslash va "
            "modellashtirish xatoligini baholash."
        ),
        visualization_component=(
            "Real detal → hisob sxemasi o'tishi; sterjen, plastina, qobiq, massiv "
            "jism turlarining tasnifi."
        ),
        research_extension=(
            "Sen-Venan prinsipining amal qilish masofasi: yuklanish usuli natijaga "
            "qanchalik masofada ta'sir qiladi?"
        ),
        difficulty="kirish",
        previous_link=(
            "Nazariy mexanikada (nm-10, nm-11) jism qattiq edi va biz faqat tashqi "
            "muvozanat bilan shug'ullandik. Endi jism ichiga kiramiz: u "
            "deformatsiyalanadi va buzilishi mumkin."
        ),
        next_topic="mq-02",
        estimated_minutes=75,
        tags=["gipoteza", "hisob sxemasi", "modellashtirish"],
        lesson=Lesson(
            physical_problem=(
                "Kran strelasining metall profili, bolt, val, ko'prik plitasi — "
                "ularning hammasi murakkab geometriyaga ega. Har birini to'liq "
                "uch o'lchovli elastiklik nazariyasi bilan hisoblash mumkin, lekin "
                "bu haddan tashqari qimmat. Muhandis soddalashtirilgan model "
                "tanlaydi — va bu tanlov natijaning aniqligini belgilaydi. Qanday "
                "qoidalar asosida soddalashtiriladi?"
            ),
            concepts=[
                c("Sterjen (bar/beam)", "Bir o'lchami qolganlaridan ancha katta element. "
                  "Hisobda u o'q chizig'i va kesim bilan tavsiflanadi."),
                c("Bir jinslilik va izotroplik", "Material xossalari hamma nuqtada bir xil "
                  "(bir jinsli) va barcha yo'nalishlarda bir xil (izotrop). Kompozit va "
                  "yog'och uchun bu buziladi."),
                c("Kichik deformatsiyalar gipotezasi", "Deformatsiyalar shu qadar kichikki, "
                  "muvozanat tenglamalari deformatsiyalanmagan holat uchun yoziladi "
                  "(dastlabki o'lchamlar prinsipi)."),
                c("Superpozitsiya prinsipi", "Bir necha yuklanish natijalari qo'shiladi. "
                  "Faqat chiziqli masalada o'rinli — ustuvorlikda (mq-25) buziladi."),
                c("Sen-Venan prinsipi", "Yuklanishni statik ekvivalent bilan almashtirish "
                  "natijaga faqat qo'yilish joyidan kesim o'lchami tartibidagi masofada "
                  "ta'sir qiladi."),
            ],
            derivation=[
                d("1-qadam. Uch o'lchovli masaladan bir o'lchovliga o'tish",
                  r"\sigma_{ij}(x,y,z) \;\longrightarrow\; N(x),\, M(x),\, Q(x),\, T(x)",
                  "Sterjen gipotezasi: kesimdagi kuchlanishlar taqsimoti oldindan "
                  "postulat qilinadi, noma'lum bo'lib faqat kesimdagi ichki kuchlar "
                  "qoladi. Bu — 6 ta funksiyani 4 ta funksiyaga tushiradi."),
                d("2-qadam. Chiziqlilik shartlari",
                  r"\sigma = E\varepsilon \;\text{va}\; \varepsilon \ll 1 "
                  r"\;\Rightarrow\; \text{yechim yuklamaga chiziqli bog'liq}",
                  "Ikkita chiziqlilik: fizik (Guk qonuni) va geometrik (kichik "
                  "deformatsiyalar). Ikkalasi birga superpozitsiya prinsipini beradi."),
                d("3-qadam. Hisob sxemasi tanlash mezoni",
                  r"\frac{L}{h} > 5 \Rightarrow \text{sterjen};\quad "
                  r"\frac{a}{h} > 8,\ \frac{b}{h} > 8 \Rightarrow \text{plastina};\quad "
                  r"\text{aks holda massiv jism}",
                  "O'lchamlar nisbati modelni belgilaydi. Bu mezonlar pq-01 da "
                  "plastina uchun aniq asoslanadi."),
                d("4-qadam. Modellashtirish xatoligini baholash",
                  r"\delta = \frac{|u_{\text{model}} - u_{\text{aniq}}|}{u_{\text{aniq}}}\cdot 100\%",
                  "Sterjen nazariyasi $L/h = 10$ da ~1 %, $L/h = 5$ da ~4 %, "
                  "$L/h = 2$ da 20 % dan ortiq xatolik beradi — bu mq-15 da "
                  "siljish deformatsiyasi hisobga olinmagani bilan bog'liq."),
            ],
            formula_meaning=(
                "Gipotezalar cheklov emas, balki hisoblashni mumkin qiladigan "
                "vositalardir. Ularning har biri aniq narxga ega: sterjen gipotezasi "
                "hisobni yuz marta soddalashtiradi, lekin qisqa va qalin elementlarda "
                "xato beradi. Muhandislikning mohiyati — qaysi soddalashtirish qaysi "
                "vaziyatda maqbul ekanini bilish."
            ),
            equations=[
                eq(r"\sigma = E\varepsilon", "Guk qonuni — fizik chiziqlilik.", "Guk qonuni"),
                eq(r"u = \sum_i u_i(F_i)", "Superpozitsiya prinsipi.", "Superpozitsiya"),
            ],
            conditions=(
                "Barcha gipotezalar chiziqli-elastik sohada o'rinli. Oquvchanlik "
                "chegarasidan oshganda fizik chiziqlilik buziladi (tmm-21), katta "
                "ko'chishlarda geometrik chiziqlilik buziladi (pq-18), ustuvorlikni "
                "yo'qotishda esa superpozitsiya ishlamaydi (mq-25)."
            ),
            worked_example=WorkedExample(
                statement=(
                    "Konsol balka: $L = 1{,}2$ m, to'rtburchak kesim $b = 40$ mm, "
                    "$h = 120$ mm, po'lat $E = 200$ GPa, $G = 80$ GPa. Uchiga $F = 5$ kN "
                    "kuch. Klassik (Bernulli) nazariya bo'yicha ko'chishni hisoblang va "
                    "siljish deformatsiyasi hisobga olingan aniqroq yechim bilan "
                    "taqqoslang. Model xatoligi qancha?"
                ),
                given=[r"L = 1{,}2\ \text{m},\; b = 0{,}04\ \text{m},\; h = 0{,}12\ \text{m}",
                       r"E = 2\cdot10^{11}\ \text{Pa},\; G = 8\cdot10^{10}\ \text{Pa},\; F = 5000\ \text{N}"],
                steps=[
                    st(r"I = \frac{bh^3}{12} = \frac{0{,}04\cdot 0{,}12^3}{12} = "
                       r"\frac{0{,}04\cdot 1{,}728\cdot10^{-3}}{12} = 5{,}76\cdot10^{-6}\ \text{m}^4",
                       "Inersiya momenti (mq-08 da batafsil)."),
                    st(r"w_{Bernulli} = \frac{FL^3}{3EI} = \frac{5000\cdot 1{,}728}{3\cdot 2\cdot10^{11}\cdot 5{,}76\cdot10^{-6}}",
                       "Klassik formula."),
                    st(r"w_{Bernulli} = \frac{8640}{3{,}456\cdot10^{6}} = 2{,}50\cdot10^{-3}\ \text{m} = 2{,}50\ \text{mm}",
                       "Faqat egilishdan ko'chish."),
                    st(r"w_{siljish} = \frac{\kappa FL}{GA} = \frac{1{,}2\cdot 5000\cdot 1{,}2}{8\cdot10^{10}\cdot 4{,}8\cdot10^{-3}} = "
                       r"1{,}875\cdot10^{-5}\ \text{m}",
                       "Siljishdan qo'shimcha ko'chish ($\\kappa = 1{,}2$ — to'rtburchak "
                       "kesim uchun shakl koeffitsienti)."),
                    st(r"w_{to'la} = 2{,}500 + 0{,}019 = 2{,}519\ \text{mm}",
                       "To'la ko'chish."),
                    st(r"\delta = \frac{0{,}019}{2{,}519}\cdot 100\% = 0{,}75\%,\qquad L/h = 10",
                       "Model xatoligi 0,75 % — qabul qilinadi."),
                ],
                answer=(
                    "$w = 2{,}50$ mm (Bernulli), $2{,}52$ mm (siljish bilan); "
                    "model xatoligi 0,75 % ($L/h = 10$)."
                ),
                engineering_note=(
                    "$L/h = 10$ da xatolik 1 % dan kam — sterjen modeli to'liq "
                    "asoslangan. Lekin $L/h = 3$ bo'lsa, siljish ulushi 8 % ga chiqadi "
                    "va Timoshenko balka modeli kerak bo'ladi. Aynan shu chegara "
                    "pq-17 dagi Reyssner–Mindlin plastina nazariyasining sababi."
                ),
            ),
            computation=Computation(
                caption=(
                    "Model xatoligi: $L/h$ nisbatini o'zgartirib, sterjen "
                    "gipotezasining qachon buzilishini ko'ring."
                ),
                code='''"""Hisob sxemasi tanlash: sterjen modelining qo'llanish chegarasi."""
import numpy as np
from labkit import PARAMS, note, series, table, value

L = float(PARAMS.get("L", 1.2))      # uzunlik, m
b = float(PARAMS.get("b", 0.04))     # kesim eni, m
h = float(PARAMS.get("h", 0.12))     # kesim balandligi, m
E = float(PARAMS.get("E", 200e9))    # Yung moduli, Pa
F = float(PARAMS.get("F", 5000.0))   # kuch, N
nu = 0.3
G = E/(2*(1+nu))
kappa = 1.2                           # to'rtburchak kesim uchun siljish koeffitsienti

A = b*h
I = b*h**3/12

w_bend = F*L**3/(3*E*I)
w_shear = kappa*F*L/(G*A)
w_total = w_bend + w_shear

value("Kesim yuzasi A", A*1e4, "cm²")
value("Inersiya momenti I", I*1e8, "cm⁴")
value("L/h nisbati", L/h, "—")
value("Egilishdan ko'chish", w_bend*1000, "mm")
value("Siljishdan ko'chish", w_shear*1000, "mm")
value("To'la ko'chish", w_total*1000, "mm")
value("Model xatoligi", 100*w_shear/w_total, "%")

# L/h nisbatining model xatoligiga ta'siri
ratios = np.linspace(1.5, 25, 200)
Ls = ratios*h
err = [100*(kappa*F*Li/(G*A))/(F*Li**3/(3*E*I) + kappa*F*Li/(G*A)) for Li in Ls]
series("Siljish ulushi (model xatoligi)", ratios.tolist(), err,
       xlabel="L/h", ylabel="Xatolik, %")

lim5 = np.interp(5.0, err[::-1], ratios[::-1])
note(f"Xatolik 5 % dan kam bo'lishi uchun L/h > {lim5:.1f} bo'lishi kerak.")
note("L/h > 10: klassik sterjen nazariyasi; 3 < L/h < 10: Timoshenko balkasi; "
     "L/h < 3: 2D/3D elastiklik nazariyasi (tmm-16).")

table("Hisob sxemasi turlari",
      ["Model", "Mezon", "Noma'lumlar", "Misol"],
      [["Sterjen", "L/h > 5", "N, Q, M, T", "Balka, val, ustun"],
       ["Plastina", "a/h > 8 va b/h > 8", "w(x,y)", "Plita, devor"],
       ["Qobiq", "R/h > 10", "u, v, w sirt bo'ylab", "Rezervuar, quvur"],
       ["Massiv jism", "o'lchamlar o'xshash", "σ_ij(x,y,z)", "Fundament bloki"]])

# Superpozitsiya prinsipini sonli tekshirish
F1, F2 = 3000.0, 2000.0
w1 = F1*L**3/(3*E*I)
w2 = F2*L**3/(3*E*I)
w12 = (F1+F2)*L**3/(3*E*I)
note(f"Superpozitsiya: w(F₁)+w(F₂) = {(w1+w2)*1000:.6f} mm, "
     f"w(F₁+F₂) = {w12*1000:.6f} mm — chiziqli masalada aynan teng ✓")
''',
                parameters=[
                    p("L", "Balka uzunligi L", 0.2, 5.0, 1.2, 0.05, "m"),
                    p("b", "Kesim eni b", 0.01, 0.3, 0.04, 0.005, "m"),
                    p("h", "Kesim balandligi h", 0.01, 0.5, 0.12, 0.005, "m"),
                    p("E", "Yung moduli E", 1e10, 4e11, 200e9, 1e10, "Pa"),
                    p("F", "Kuch F", 100.0, 50000.0, 5000.0, 100.0, "N"),
                ],
                expected_output="L/h = 10, w = 2,50 mm, model xatoligi ≈ 0,75 %",
            ),
            visualization=vis(
                "Real detaldan hisob sxemasiga o'tish",
                "React/SVG",
                "Yonma-yon ikki tasvir: chapda real detal (murakkab kontur, teshiklar, "
                "galtel), o'ngda hisob sxemasi (o'q chizig'i, tayanch belgilari, "
                "yuklama strelkalari). Pastda model turlari tasnifi.",
                "React/SVG: bu — butun fanning 'kirish darvozasi' bo'lgan chizma. "
                "Hisob sxemasi belgilarini (tayanch, yuklama) alohida komponentlar "
                "sifatida yozing — ular mq-12 dagi epyuralar sahifasida qayta ishlatiladi.",
            ),
            interpretation=(
                "Xatolik grafigi $L/h$ kamayganda keskin (giperbolik) o'sadi: "
                "$L/h = 10$ da 0,75 %, $L/h = 3$ da 8 %, $L/h = 2$ da 17 %. Demak "
                "sterjen nazariyasining chegarasi aniq: $L/h > 5$. Superpozitsiya "
                "tekshiruvi esa chiziqli masalada aynan bajarilishini tasdiqlaydi — "
                "bu butun kursning hisoblash asosi."
            ),
            common_mistakes=[
                "Hisob sxemasini tanlashda o'lchamlar nisbatini tekshirmaslik.",
                "Superpozitsiyani nochiziqli masalalarda (ustuvorlik, plastiklik) qo'llash.",
                "Sen-Venan prinsipini yuklanish qo'yilgan joyning o'zida ham to'g'ri "
                "deb hisoblash.",
                "Gipotezalarni 'aksioma' deb qabul qilish — ularning har biri "
                "qo'llanish chegarasiga ega.",
            ],
            quiz=[
                q("Nima uchun materiallar qarshiligi alohida fan sifatida mavjud, "
                  "elastiklik nazariyasi bo'lsa ham?",
                  "Elastiklik nazariyasi umumiy, lekin murakkab. Materiallar qarshiligi "
                  "qo'shimcha gipotezalar (sterjen, tekis kesimlar) orqali masalani "
                  "muhandislik amaliyotiga mos darajada soddalashtiradi.", "konseptual"),
                q("Superpozitsiya prinsipi qachon ishlamaydi?",
                  "Fizik nochiziqlilikda (plastiklik), geometrik nochiziqlilikda (katta "
                  "ko'chishlar) va ustuvorlik masalalarida.", "konseptual"),
                q("$L = 0{,}5$ m, $h = 0{,}2$ m. Sterjen modeli qo'llanadimi?",
                  "$L/h = 2{,}5 < 5$ — yo'q, Timoshenko balkasi yoki 2D model kerak.",
                  "hisob"),
                q("Sen-Venan prinsipining amaliy foydasi nima?",
                  "Yuklanishning aniq taqsimotini bilish shart emas — uni statik "
                  "ekvivalent bilan almashtirish mumkin, natija kesim o'lchamidan "
                  "uzoqda deyarli bir xil bo'ladi.", "talqin"),
                q("Kodda superpozitsiya qanday tekshirilgan?",
                  "Ikki kuchdan alohida hosil bo'lgan ko'chishlar yig'indisi ularning "
                  "yig'indisidan hosil bo'lgan ko'chishga tenglashtirilgan — chiziqli "
                  "masalada aynan teng chiqadi.", "kod"),
            ],
            bridge_to_next=(
                "Hisob sxemasi tanlandi. Endi uning ichiga kirib, kesimda qanday "
                "ichki kuchlar va kuchlanishlar paydo bo'lishini aniqlaymiz."
            ),
            research_extension=(
                "Sen-Venan prinsipining amal qilish masofasini sonli o'rganing: "
                "bir xil natijaviy kuchni turli usulda (nuqtaviy, tekis taqsimlangan, "
                "parabolik) qo'yib, kuchlanish maydonining qancha masofada "
                "tenglashishini aniqlang. 2D masalani chekli ayirmalar bilan yeching "
                "(su-12) va xulosani $x/h$ nisbati orqali ifodalang."
            ),
        ),
    ),
    Topic(
        id="mq-02",
        subject_id=S,
        module_id=M,
        order=2,
        title="Ichki kuchlar, kesim usuli va kuchlanish tushunchasi",
        description=(
            "Kesim usuli (ROZU), ichki kuch omillari, normal va urinma kuchlanish, "
            "kuchlanishning ichki kuch bilan bog'lanishi."
        ),
        learning_objective=(
            "Kesim usuli bilan ichki kuch omillarini aniqlash va kuchlanish "
            "tushunchasini to'g'ri qo'llash."
        ),
        prerequisites=["mq-01", "nm-11"],
        mathematical_core=(
            "Chegaraviy o'tish $\\sigma = \\lim \\Delta F/\\Delta A$, yuza bo'yicha "
            "integrallash, statik ekvivalentlik shartlari."
        ),
        engineering_application=(
            "Har qanday konstruktiv element hisobining birinchi bosqichi: kesimdagi "
            "ichki kuchlarni aniqlash."
        ),
        computational_component=(
            "Sterjen bo'ylab ichki kuch omillari epyurasini sonli qurish."
        ),
        visualization_component=(
            "Kesim usuli animatsiyasi: jismni kesish, bir qismini tashlash, ichki "
            "kuchlarni qo'yish."
        ),
        research_extension=(
            "Kuchlanish tushunchasi qanchalik kichik yuzada ma'noga ega? Material "
            "mikrostrukturasi va kontinuum modeli chegarasi."
        ),
        difficulty="kirish",
        previous_link=(
            "mq-01 da hisob sxemasini tuzdik. Endi shu sxemada ichki kuchlarni "
            "aniqlashning universal usulini — kesim usulini o'rganamiz."
        ),
        next_topic="mq-03",
        estimated_minutes=80,
        tags=["kesim usuli", "ichki kuch", "kuchlanish"],
        lesson=Lesson(
            physical_problem=(
                "Kran trosi uzilganda aynan qayerdan uziladi? Eng yupqa joydan emas, "
                "balki kuchlanish eng katta bo'lgan joydan. Kuch bir xil bo'lsa ham, "
                "turli kesimlarda kuchlanish turlicha bo'ladi. Demak buzilishni "
                "bashorat qilish uchun kuch emas, kuchlanish kerak — va uni "
                "aniqlash uchun jismni 'kesib ko'rish' kerak."
            ),
            concepts=[
                c("Kesim usuli (ROZU)", "Rejem–Otbrasыvaem–Zamenyaem–Uravnovешivaem: "
                  "kesamiz, bir qismini tashlaymiz, ichki kuchlar bilan almashtiramiz, "
                  "muvozanat tenglamalarini yozamiz."),
                c("Ichki kuch omillari", "Kesimdagi 6 ta omil: $N$ (bo'ylama kuch), "
                  "$Q_y, Q_z$ (kesuvchi kuchlar), $T$ (buruvchi moment), "
                  "$M_y, M_z$ (eguvchi momentlar)."),
                c("Normal kuchlanish $\\sigma$", "Kesim tekisligiga perpendikular "
                  "kuchlanish. Musbat — cho'zuvchi."),
                c("Urinma kuchlanish $\\tau$", "Kesim tekisligida yotuvchi kuchlanish. "
                  "Siljish va buralishda paydo bo'ladi."),
                c("Statik ekvivalentlik", "$N = \\int_A\\sigma\\,dA$, "
                  "$M_y = \\int_A\\sigma z\\,dA$ — kuchlanishlar kesimdagi ichki "
                  "kuchlarga keltiriladi."),
            ],
            derivation=[
                d("1-qadam. Kuchlanish ta'rifi",
                  r"p = \lim_{\Delta A\to 0}\frac{\Delta \mathbf{F}}{\Delta A} \;\Rightarrow\; "
                  r"\sigma = \lim\frac{\Delta N}{\Delta A},\quad \tau = \lim\frac{\Delta Q}{\Delta A}",
                  "To'la kuchlanish vektori normal va urinma tashkil etuvchilarga "
                  "ajraladi. Birligi Pa = N/m²; muhandislikda MPa = N/mm²."),
                d("2-qadam. Statik ekvivalentlik shartlari",
                  r"N = \int_A \sigma\,dA,\quad M_y = \int_A \sigma z\,dA,\quad "
                  r"M_z = -\int_A \sigma y\,dA",
                  "Kuchlanishlar taqsimoti ichki kuch omillariga keltiriladi. Bu "
                  "6 ta tenglama, lekin noma'lum — butun $\\sigma(y,z)$ funksiyasi. "
                  "Shuning uchun qo'shimcha gipoteza (tekis kesimlar) kerak."),
                d("3-qadam. Ichki kuchlarni muvozanatdan topish",
                  r"N(x) = \sum F_{x}^{\text{chap}},\quad Q(x) = \sum F_{y}^{\text{chap}},\quad "
                  r"M(x) = \sum M^{\text{chap}}_{\text{kesim}}",
                  "Kesimning bir tomonidagi barcha tashqi kuchlarni jamlaymiz. "
                  "Muhim: chap va o'ng tomondan hisoblash bir xil natija berishi shart."),
                d("4-qadam. Differensial bog'lanishlar (Juravskiy)",
                  r"\frac{dQ}{dx} = -q(x),\qquad \frac{dM}{dx} = Q(x),\qquad "
                  r"\frac{d^2M}{dx^2} = -q(x)",
                  "Elementar bo'lakning muvozanatidan. Bu bog'lanishlar epyuralarni "
                  "qurish va tekshirishning asosiy vositasi (mq-12)."),
            ],
            formula_meaning=(
                "Kuchlanish — kuchning 'zichligi'. Ikki bir xil kuch turli yuzada "
                "butunlay boshqacha xavf tug'diradi: 10 kN kuch 100 mm² da 100 MPa, "
                "1000 mm² da esa 10 MPa beradi. Shuning uchun buzilish mezoni kuch "
                "emas, kuchlanish bilan ifodalanadi. Differensial bog'lanishlar esa "
                "epyuralarning shaklini oldindan aytib beradi: $q = 0$ bo'lgan "
                "uchastkada $Q$ o'zgarmas, $M$ chiziqli."
            ),
            equations=[
                eq(r"\sigma = \lim_{\Delta A\to0}\frac{\Delta N}{\Delta A}", "Normal kuchlanish ta'rifi.",
                   "Kuchlanish"),
                eq(r"N = \int_A\sigma\,dA,\quad M_y = \int_A\sigma z\,dA",
                   "Statik ekvivalentlik shartlari.", "Ekvivalentlik"),
                eq(r"\frac{dQ}{dx} = -q,\qquad \frac{dM}{dx} = Q", "Juravskiy differensial bog'lanishlari.",
                   "Differensial bog'lanish"),
            ],
            conditions=(
                "Kesim usuli konstruksiya muvozanatda bo'lgandagina qo'llanadi "
                "(dinamik masalada D'Alembert inersiya kuchlari qo'shiladi — nm-21). "
                "Ichki kuchlar kesim joyiga bog'liq, shuning uchun ular $x$ ning "
                "funksiyasi sifatida qidiriladi. Yuklanish uzilishli joylarda "
                "(nuqtaviy kuch, moment) funksiyalar ham uziladi."
            ),
            worked_example=WorkedExample(
                statement=(
                    "Pog'onali sterjen vertikal osilgan: yuqori qism $A_1 = 400$ mm², "
                    "$L_1 = 1{,}5$ m; quyi qism $A_2 = 200$ mm², $L_2 = 1$ m. "
                    "Quyi uchiga $F = 30$ kN osilgan, material po'lat "
                    "$\\rho = 7850$ kg/m³. Har bir qismdagi bo'ylama kuch va "
                    "kuchlanishni toping (o'z og'irligini hisobga olib)."
                ),
                given=[r"A_1 = 4\cdot10^{-4}\ \text{m}^2,\; L_1 = 1{,}5\ \text{m}",
                       r"A_2 = 2\cdot10^{-4}\ \text{m}^2,\; L_2 = 1\ \text{m}",
                       r"F = 30\ \text{kN},\; \rho = 7850\ \text{kg/m}^3"],
                steps=[
                    st(r"G_2 = \rho g A_2L_2 = 7850\cdot 9{,}81\cdot 2\cdot10^{-4}\cdot 1 = 15{,}4\ \text{N}",
                       "Quyi qismning og'irligi — kuchdan 1900 marta kichik."),
                    st(r"N_2(x) = F + \rho gA_2x \Rightarrow N_2^{max} = 30\,000 + 15{,}4 = 30\,015\ \text{N}",
                       "Quyi qismdagi bo'ylama kuch (yuqori kesimda maksimal)."),
                    st(r"\sigma_2 = \frac{N_2}{A_2} = \frac{30\,015}{2\cdot10^{-4}} = 150{,}1\ \text{MPa}",
                       "Quyi qismdagi kuchlanish."),
                    st(r"G_1 = 7850\cdot 9{,}81\cdot 4\cdot10^{-4}\cdot 1{,}5 = 46{,}2\ \text{N}",
                       "Yuqori qismning og'irligi."),
                    st(r"N_1^{max} = 30\,015 + 46{,}2 = 30\,061\ \text{N} \Rightarrow "
                       r"\sigma_1 = \frac{30\,061}{4\cdot10^{-4}} = 75{,}2\ \text{MPa}",
                       "Yuqori qismdagi kuchlanish — kuch katta bo'lsa ham, yuza ikki "
                       "barobar katta."),
                    st(r"\frac{\sigma_2}{\sigma_1} = \frac{150{,}1}{75{,}2} = 2{,}0",
                       "Xavfli kesim — quyi qismda, garchi undagi kuch kichikroq bo'lsa ham."),
                ],
                answer=(
                    "$\\sigma_1 = 75{,}2$ MPa, $\\sigma_2 = 150{,}1$ MPa; xavfli kesim — "
                    "quyi (yupqa) qismning yuqori kesimi. O'z og'irligi ulushi 0,2 %."
                ),
                engineering_note=(
                    "O'z og'irligi ulushi 0,2 % — uni e'tiborga olmasa ham bo'ladi. "
                    "Lekin uzun sterjenlarda (shaxta trosi, 500 m) vaziyat teskari: "
                    "$\\sigma_{og'irlik} = \\rho g L = 7850\\cdot 9{,}81\\cdot 500 = 38{,}5$ MPa "
                    "— bu ruxsat etilgan kuchlanishning sezilarli qismi."
                ),
            ),
            computation=Computation(
                caption=(
                    "Pog'onali sterjen: kesimlar va yuklarni o'zgartirib, $N$ va "
                    "$\\sigma$ epyuralarini quring."
                ),
                code='''"""Kesim usuli: bo'ylama kuch va kuchlanish epyuralari."""
import numpy as np
from labkit import PARAMS, note, series, table, value

A1 = float(PARAMS.get("A1", 400.0))*1e-6   # yuqori qism yuzasi, m^2
A2 = float(PARAMS.get("A2", 200.0))*1e-6   # quyi qism yuzasi, m^2
L1 = float(PARAMS.get("L1", 1.5))
L2 = float(PARAMS.get("L2", 1.0))
F = float(PARAMS.get("F", 30000.0))        # oxirgi yuk, N
rho = float(PARAMS.get("rho", 7850.0))
g = 9.81

# x — yuqoridan pastga, 0 dan L1+L2 gacha
n = 400
x = np.linspace(0, L1+L2, n)
N = np.zeros(n)
sig = np.zeros(n)
for i, xi in enumerate(x):
    if xi <= L1:                                   # yuqori qism
        below = rho*g*A1*(L1-xi) + rho*g*A2*L2 + F
        N[i] = below
        sig[i] = below/A1
    else:                                          # quyi qism
        below = rho*g*A2*(L1+L2-xi) + F
        N[i] = below
        sig[i] = below/A2

series("Bo'ylama kuch N(x)", x.tolist(), (N/1000).tolist(), xlabel="x, m", ylabel="N, kN")
series("Kuchlanish σ(x)", x.tolist(), (sig/1e6).tolist(), xlabel="x, m", ylabel="σ, MPa")

value("N_max", float(np.max(N))/1000, "kN")
value("σ_max", float(np.max(sig))/1e6, "MPa")
value("Xavfli kesim x", float(x[np.argmax(sig)]), "m")
value("Yuqori qism σ", float(sig[0])/1e6, "MPa")
value("O'z og'irligi ulushi", 100*(np.max(N)-F)/np.max(N), "%")

# O'z og'irligining uzunlikka bog'liqligi
LL = np.linspace(1, 800, 200)
sig_own = rho*g*LL/1e6
series("O'z og'irligidan kuchlanish", LL.tolist(), sig_own.tolist(),
       xlabel="Sterjen uzunligi L, m", ylabel="σ, MPa")
L_crit = 160e6/(rho*g)
note(f"[σ] = 160 MPa bo'lsa, faqat o'z og'irligidan uziladigan uzunlik: "
     f"L = {L_crit:.0f} m. Shaxta troslari uchun bu hal qiluvchi cheklov.")

# Kesim usulini chap va o'ng tomondan tekshirish
x_test = L1 + L2/2
N_below = rho*g*A2*(L1+L2-x_test) + F
note(f"x = {x_test:.2f} m kesimida pastdan hisoblangan N = {N_below:.1f} N, "
     f"epyuradan olingan N = {np.interp(x_test, x, N):.1f} N — mos ✓")

table("Ichki kuch omillari (fazoviy holat)",
      ["Omil", "Belgi", "Deformatsiya turi", "Kuchlanish"],
      [["Bo'ylama kuch", "N", "Cho'zilish/siqilish", "σ = N/A"],
       ["Kesuvchi kuch", "Q", "Siljish", "τ (Juravskiy)"],
       ["Buruvchi moment", "T", "Buralish", "τ = T·ρ/I_p"],
       ["Eguvchi moment", "M", "Egilish", "σ = M·y/I"]])
''',
                parameters=[
                    p("A1", "Yuqori qism yuzasi A₁", 50.0, 2000.0, 400.0, 10.0, "mm²"),
                    p("A2", "Quyi qism yuzasi A₂", 50.0, 2000.0, 200.0, 10.0, "mm²"),
                    p("L1", "Yuqori qism uzunligi", 0.2, 10.0, 1.5, 0.1, "m"),
                    p("L2", "Quyi qism uzunligi", 0.2, 10.0, 1.0, 0.1, "m"),
                    p("F", "Yuk F", 0.0, 200000.0, 30000.0, 1000.0, "N"),
                ],
                expected_output="σ_max ≈ 150,1 MPa (quyi qism), σ₁ ≈ 75,2 MPa",
            ),
            visualization=vis(
                "Kesim usuli va epyuralar",
                "Manim",
                "Sterjen kesiladi, bir qismi shaffof bo'lib yo'qoladi, kesim yuzasida "
                "taqsimlangan kuchlanish strelkalari va ularning natijaviysi $N$ "
                "paydo bo'ladi. Yonida $N(x)$ va $\\sigma(x)$ epyuralari quriladi.",
                "Manim: kesim usulining to'rt qadami (kesish, tashlash, almashtirish, "
                "muvozanatlash) — bu ketma-ketlikni animatsiyada ko'rsatish g'oyani "
                "mustahkam o'rnatadi. React/SVG da epyuralar interaktiv beriladi.",
            ),
            interpretation=(
                "$N(x)$ epyurasi deyarli pog'onasimon (o'z og'irligi kichik "
                "qiyalikni beradi), $\\sigma(x)$ esa pog'onada sakraydi — chunki "
                "yuza keskin o'zgaradi. Bu asosiy xulosani beradi: xavfli kesim "
                "maksimal kuch bo'lgan joyda emas, maksimal kuchlanish bo'lgan joyda. "
                "Uzun sterjenlar grafigi esa o'z og'irligining chegaraviy uzunlikni "
                "belgilashini ko'rsatadi."
            ),
            common_mistakes=[
                "Kuchlanishni kuch bilan chalkashtirish — kuchlanish yuzaga bo'lingan kuch.",
                "Ichki kuchni faqat kesimning bir tomonidan hisoblab, tekshirmaslik.",
                "MPa va N/mm² ni turli birlik deb o'ylash — ular aynan teng.",
                "Pog'onali sterjenda xavfli kesimni maksimal kuch bo'yicha tanlash.",
            ],
            quiz=[
                q("Nima uchun buzilish mezoni kuch emas, kuchlanish bilan ifodalanadi?",
                  "Chunki bir xil kuch turli yuzada turli intensivlikda ta'sir qiladi. "
                  "Material esa aynan kuchlanish darajasiga reaksiya bildiradi.",
                  "konseptual"),
                q("Kesim usulining to'rt qadami qanday?",
                  "Kesamiz — bir qismini tashlaymiz — ichki kuchlar bilan almashtiramiz — "
                  "muvozanat tenglamalarini yozamiz.", "konseptual"),
                q("$N = 50$ kN, $A = 250$ mm². $\\sigma$ ni toping.",
                  "$\\sigma = 50\\,000/250 = 200$ N/mm² = 200 MPa.", "hisob"),
                q("$dM/dx = Q$ bog'lanishining amaliy foydasi nima?",
                  "$Q = 0$ bo'lgan kesimda $M$ ekstremumga ega — bu xavfli kesimni "
                  "topishning eng tez usuli (mq-12).", "talqin"),
                q("Kodda o'z og'irligining ulushi qanday hisoblangan?",
                  "$(N_{max} - F)/N_{max}$ — umumiy kuchdagi og'irlik hissasi. "
                  "Kalta sterjenlarda u ahamiyatsiz, uzunlarida hal qiluvchi.", "kod"),
            ],
            bridge_to_next=(
                "Kuchlanish tushunchasi kiritildi, lekin uning kesim bo'ylab qanday "
                "taqsimlanishi hali noma'lum. Keyingi mavzuda eng sodda hol — "
                "cho'zilish uchun bu taqsimotni aniqlaymiz."
            ),
            research_extension=(
                "Kuchlanish tushunchasining chegarasini tadqiq qiling: "
                "$\\Delta A \\to 0$ limiti fizik jihatdan qachon ma'noga ega? "
                "Metallning don o'lchami (10–100 mkm) bilan taqqoslang va "
                "mikrokuchlanish hamda makrokuchlanish farqini tahlil qiling. "
                "Bu — tmm-01 dagi kontinuum gipotezasining amaliy chegarasi."
            ),
            manim=manim(
                scene="SectionMethodScene",
                module="manim/scenes/mq_stress.py",
                title="Kesim usuli",
                summary="Sterjen kesiladi, bir qismi olib tashlanadi va kesimda ichki "
                        "kuchlar paydo bo'ladi; epyuralar bosqichma-bosqich quriladi.",
            ),
        ),
    ),
    Topic(
        id="mq-03",
        subject_id=S,
        module_id=M,
        order=3,
        title="Cho'zilish va siqilishda kuchlanish, deformatsiya va Guk qonuni",
        description=(
            "Tekis kesimlar gipotezasi, bir tekis kuchlanish taqsimoti, nisbiy va "
            "absolyut deformatsiya, Guk qonuni va bikrlik tushunchasi."
        ),
        learning_objective=(
            "Cho'zilgan sterjenda kuchlanish va deformatsiyani hisoblash, "
            "bikrlik shartini qo'llash."
        ),
        prerequisites=["mq-02"],
        mathematical_core=(
            "$\\varepsilon = du/dx$, chiziqli bog'lanish $\\sigma = E\\varepsilon$, "
            "integrallash orqali ko'chishni topish."
        ),
        engineering_application=(
            "Tros, tortqi, bolt, ferma sterjeni, kran osma elementlari hisobi."
        ),
        computational_component=(
            "Pog'onali va o'zgaruvchan kesimli sterjenning ko'chishini sonli "
            "integrallash orqali topish."
        ),
        visualization_component=(
            "Kesim bo'ylab bir tekis $\\sigma$ taqsimoti va ko'chish epyurasi."
        ),
        research_extension=(
            "Teng mustahkamlikdagi sterjen profilini toping: $\\sigma = \\text{const}$ "
            "sharti qanday shaklga olib keladi?"
        ),
        difficulty="asosiy",
        previous_link=(
            "mq-02 da kuchlanish ta'rifini oldik, lekin $\\sigma(y,z)$ noma'lum edi. "
            "Cho'zilishda tekis kesimlar gipotezasi uni bir tekis deb belgilaydi."
        ),
        next_topic="mq-04",
        estimated_minutes=85,
        tags=["cho'zilish", "Guk qonuni", "deformatsiya"],
        lesson=Lesson(
            physical_problem=(
                "Lift trosi yuk ostida cho'ziladi. Agar cho'zilish juda katta bo'lsa, "
                "kabina qavat darajasidan pastda to'xtaydi — bu foydalanishga "
                "yaroqsiz. Demak konstruksiyani nafaqat mustahkamlikka (uzilmasligi), "
                "balki bikrlikka (ortiqcha deformatsiyalanmasligi) ham hisoblash kerak. "
                "Ikkala shart turli formulalar beradi va ko'pincha bikrlik hal qiluvchi "
                "bo'lib chiqadi."
            ),
            concepts=[
                c("Tekis kesimlar gipotezasi (Bernulli)", "Deformatsiyagacha tekis "
                  "bo'lgan kesimlar deformatsiyadan keyin ham tekis va o'qqa "
                  "perpendikular qoladi."),
                c("Nisbiy deformatsiya", "$\\varepsilon = \\Delta L/L = du/dx$ — "
                  "o'lchamsiz kattalik, odatda $10^{-3}$ tartibida."),
                c("Guk qonuni", "$\\sigma = E\\varepsilon$; $E$ — Yung moduli, "
                  "po'lat uchun 200–210 GPa, alyuminiy 70 GPa, beton 25–40 GPa."),
                c("Bikrlik $EA$", "Sterjenning cho'zilishga qarshiligi. "
                  "$\\Delta L = NL/(EA)$ formulasidagi maxraj."),
                c("Puasson koeffitsienti", "$\\nu = -\\varepsilon'/\\varepsilon$ — "
                  "ko'ndalang va bo'ylama deformatsiyalar nisbati; po'lat uchun 0,3."),
            ],
            derivation=[
                d("1-qadam. Tekis kesimlar gipotezasidan deformatsiya taqsimoti",
                  r"u = u(x) \text{ (kesim bo'ylab o'zgarmas)} \;\Rightarrow\; "
                  r"\varepsilon = \frac{du}{dx} = \text{const kesim bo'ylab}",
                  "Kesim tekis qolgani uchun uning barcha nuqtalari bir xil ko'chadi."),
                d("2-qadam. Guk qonuni orqali kuchlanish",
                  r"\sigma = E\varepsilon = \text{const} \text{ kesim bo'ylab}",
                  "Bir jinsli materialda deformatsiya o'zgarmas bo'lsa, kuchlanish ham "
                  "o'zgarmas — cho'zilishda kuchlanish kesim bo'ylab bir tekis taqsimlanadi."),
                d("3-qadam. Statik ekvivalentlikdan formula",
                  r"N = \int_A\sigma\,dA = \sigma\int_A dA = \sigma A \;\Rightarrow\; "
                  r"\boxed{\;\sigma = \frac{N}{A}\;}",
                  "Kuchlanish integral belgisidan chiqdi, chunki u o'zgarmas. "
                  "Materiallar qarshiligidagi eng sodda va eng ko'p ishlatiladigan formula."),
                d("4-qadam. Ko'chishni topish",
                  r"\varepsilon = \frac{\sigma}{E} = \frac{N}{EA} = \frac{du}{dx} \Rightarrow "
                  r"\boxed{\;\Delta L = \int_0^L\frac{N(x)}{E A(x)}dx = \frac{NL}{EA}\;}",
                  "Oxirgi shakl $N$ va $A$ o'zgarmas bo'lgandagina. Pog'onali "
                  "sterjenda uchastkalar bo'yicha yig'indi olinadi."),
            ],
            formula_meaning=(
                "$\\sigma = N/A$ — mustahkamlik hisobining asosi; $\\Delta L = NL/(EA)$ — "
                "bikrlik hisobining asosi. Ikkinchisida $E$ paydo bo'ladi, birinchisida "
                "yo'q: demak kuchlanish materialdan bog'liq emas, deformatsiya esa "
                "bog'liq. Shuning uchun po'lat va alyuminiy sterjenlar bir xil "
                "kuchlanishda ishlashi mumkin, lekin alyuminiy uch barobar ko'proq "
                "cho'ziladi."
            ),
            equations=[
                eq(r"\sigma = \frac{N}{A}", "Cho'zilishda normal kuchlanish.", "Kuchlanish"),
                eq(r"\Delta L = \frac{NL}{EA}", "Absolyut deformatsiya (Guk qonuni).",
                   "Ko'chish"),
                eq(r"\varepsilon' = -\nu\varepsilon", "Ko'ndalang deformatsiya.", "Puasson effekti"),
            ],
            conditions=(
                "Formula sterjenning yuklanish qo'yilgan joyidan uzoq qismlarida "
                "o'rinli (Sen-Venan prinsipi). Kesim keskin o'zgaradigan joylarda "
                "kuchlanish konsentratsiyasi paydo bo'ladi (mq-29) va $\\sigma = N/A$ "
                "faqat o'rtacha qiymatni beradi. Siqilishda uzun sterjen uchun "
                "ustuvorlikni ham tekshirish shart (mq-25)."
            ),
            worked_example=WorkedExample(
                statement=(
                    "Lift trosi: po'lat arqon, shartli kesim yuzasi $A = 380$ mm², "
                    "$E = 160$ GPa (arqon uchun kamaytirilgan), uzunligi $L = 45$ m. "
                    "Kabina va yuk $m = 1200$ kg, tezlanish $a = 1{,}2$ m/s² (yuqoriga). "
                    "Kuchlanish, cho'zilish va zaxira koeffitsientini toping "
                    "($\\sigma_u = 1600$ MPa)."
                ),
                given=[r"A = 3{,}8\cdot10^{-4}\ \text{m}^2,\; E = 1{,}6\cdot10^{11}\ \text{Pa}",
                       r"L = 45\ \text{m},\; m = 1200\ \text{kg},\; a = 1{,}2\ \text{m/s}^2"],
                steps=[
                    st(r"N = m(g+a) = 1200(9{,}81+1{,}2) = 1200\cdot 11{,}01 = 13\,212\ \text{N}",
                       "Dinamik kuch (nm-07 dagi dinamiklik koeffitsienti bilan)."),
                    st(r"\sigma = \frac{N}{A} = \frac{13\,212}{3{,}8\cdot10^{-4}} = "
                       r"34{,}8\cdot10^{6} = 34{,}8\ \text{MPa}",
                       "Ish kuchlanishi."),
                    st(r"\Delta L = \frac{NL}{EA} = \frac{13\,212\cdot 45}{1{,}6\cdot10^{11}\cdot 3{,}8\cdot10^{-4}}",
                       "Cho'zilish formulasi."),
                    st(r"\Delta L = \frac{594\,540}{6{,}08\cdot10^{7}} = 9{,}78\cdot10^{-3}\ \text{m} = 9{,}8\ \text{mm}",
                       "Cho'zilish — bu kabina qavat darajasidan 10 mm pastda to'xtashi demak."),
                    st(r"\varepsilon = \frac{\Delta L}{L} = \frac{0{,}00978}{45} = 2{,}17\cdot10^{-4}",
                       "Nisbiy deformatsiya — 0,022 %."),
                    st(r"n = \frac{\sigma_u}{\sigma} = \frac{1600}{34{,}8} = 46",
                       "Zaxira koeffitsienti — liftlar uchun me'yoriy talab 12, demak "
                       "katta zaxira bilan bajarilgan."),
                ],
                answer=(
                    "$\\sigma = 34{,}8$ MPa; $\\Delta L = 9{,}8$ mm; $n = 46$."
                ),
                engineering_note=(
                    "Zaxira 46 — mustahkamlik bo'yicha juda katta, lekin lift "
                    "troslari uchun bu normal: ular yeyilish, egilish charchashi va "
                    "favqulodda holatlarga hisoblanadi. 9,8 mm cho'zilish esa "
                    "to'xtash aniqligiga ta'sir qiladi — shuning uchun zamonaviy "
                    "liftlarda darajani avtomatik tenglashtirish tizimi bor."
                ),
            ),
            computation=Computation(
                caption=(
                    "Cho'zilgan sterjen: kesim va materialni o'zgartirib, mustahkamlik "
                    "hamda bikrlikni birgalikda tekshiring."
                ),
                code='''"""Cho'zilish: kuchlanish, deformatsiya va bikrlik hisobi."""
import numpy as np
from scipy.integrate import quad
from labkit import PARAMS, note, series, table, value

A = float(PARAMS.get("A", 380.0))*1e-6   # kesim yuzasi, m^2
E = float(PARAMS.get("E", 160e9))        # Yung moduli, Pa
L = float(PARAMS.get("L", 45.0))         # uzunlik, m
m = float(PARAMS.get("m", 1200.0))       # yuk massasi, kg
a = float(PARAMS.get("a", 1.2))          # tezlanish, m/s^2
sigma_u = float(PARAMS.get("sigma_u", 1600.0))*1e6
g = 9.81

N = m*(g+a)
sigma = N/A
dL = N*L/(E*A)
eps = dL/L

value("Bo'ylama kuch N", N/1000, "kN")
value("Kuchlanish σ", sigma/1e6, "MPa")
value("Cho'zilish ΔL", dL*1000, "mm")
value("Nisbiy deformatsiya ε", eps*100, "%")
value("Zaxira koeffitsienti n", sigma_u/sigma, "—")
value("Bikrlik EA", E*A/1e6, "MN")
value("Dinamiklik koeff.", (g+a)/g, "—")

# O'zgaruvchan kesimli sterjen: konussimon
A0, AL = A, A*0.6
def area(x):
    return A0 + (AL-A0)*x/L
dL_var, err = quad(lambda x: N/(E*area(x)), 0, L)
note(f"Konussimon sterjen (A: {A*1e6:.0f} -> {AL*1e6:.0f} mm²): "
     f"ΔL = {dL_var*1000:.3f} mm (sonli integrallash, xatolik {err:.1e})")

xx = np.linspace(0, L, 200)
series("Kuchlanish σ(x) — konussimon", xx.tolist(),
       [N/area(x)/1e6 for x in xx], xlabel="x, m", ylabel="σ, MPa")
u_x = [quad(lambda s: N/(E*area(s)), 0, x)[0]*1000 for x in xx]
series("Ko'chish u(x)", xx.tolist(), u_x, xlabel="x, m", ylabel="u, mm")

# Material tanlovi: bir xil kuchlanishda deformatsiya
mats = [("Po'lat", 200e9, 250e6), ("Alyuminiy", 70e9, 150e6),
        ("Titan", 110e9, 800e6), ("Beton (siqilish)", 30e9, 25e6)]
table("Materiallarni taqqoslash",
      ["Material", "E, GPa", "[σ], MPa", "ΔL (bir xil N), mm", "Kerakli A, mm²"],
      [[nm, Ei/1e9, su/1e6, float(N*L/(Ei*A)*1000), float(N/su*1e6)]
       for nm, Ei, su in mats])

# Bikrlik va mustahkamlik shartlaridan kerakli yuza
sigma_allow = 160e6
dL_allow = 0.005                     # ruxsat etilgan cho'zilish, m
A_strength = N/sigma_allow
A_stiffness = N*L/(E*dL_allow)
value("A (mustahkamlikdan)", A_strength*1e6, "mm²")
value("A (bikrlikdan)", A_stiffness*1e6, "mm²")
note(f"Hal qiluvchi shart: "
     f"{'BIKRLIK' if A_stiffness > A_strength else 'MUSTAHKAMLIK'} "
     f"(kerakli yuza {max(A_strength, A_stiffness)*1e6:.1f} mm²)")
''',
                parameters=[
                    p("A", "Kesim yuzasi A", 10.0, 5000.0, 380.0, 10.0, "mm²"),
                    p("E", "Yung moduli E", 1e10, 4e11, 160e9, 5e9, "Pa"),
                    p("L", "Uzunlik L", 1.0, 500.0, 45.0, 1.0, "m"),
                    p("m", "Yuk massasi m", 50.0, 10000.0, 1200.0, 50.0, "kg"),
                    p("a", "Tezlanish a", -5.0, 5.0, 1.2, 0.1, "m/s²"),
                    p("sigma_u", "Mustahkamlik chegarasi", 50.0, 2500.0, 1600.0, 50.0, "MPa"),
                ],
                expected_output="σ = 34,8 MPa, ΔL = 9,78 mm, n = 46",
            ),
            visualization=vis(
                "Kuchlanish taqsimoti va ko'chish epyurasi",
                "React/SVG",
                "Sterjen kesimi va unda bir tekis $\\sigma$ taqsimoti (bir xil "
                "uzunlikdagi strelkalar); yonida $u(x)$ ko'chish epyurasi.",
                "React/SVG: bir tekis taqsimotni teng uzunlikdagi strelkalar qatori "
                "bilan ko'rsating — bu mq-13 dagi egilishdagi uchburchak taqsimot bilan "
                "taqqoslash uchun muhim vizual kontrast beradi.",
            ),
            interpretation=(
                "Konussimon sterjenda kuchlanish yupqa uchda ortadi — shuning uchun "
                "kesim kamayishi kuchlanishni oshiradi. Materiallar jadvali muhim "
                "muhandislik xulosasini beradi: alyuminiy bir xil kuchda po'latdan "
                "3 marta ko'p cho'ziladi, lekin uch marta yengil. Yakuniy hisobda esa "
                "ko'pincha bikrlik sharti hal qiluvchi bo'lib chiqadi — bu ko'plab "
                "talabalar kutmaydigan natija."
            ),
            common_mistakes=[
                "$\\sigma = N/A$ ni kuchlanish konsentratsiyasi bo'lgan joylarda "
                "(teshik, galtel) qo'llash.",
                "Pog'onali sterjenda umumiy cho'zilishni bitta formula bilan hisoblash — "
                "uchastkalar bo'yicha yig'ish kerak.",
                "Siqilishda ustuvorlikni tekshirmaslik.",
                "Faqat mustahkamlikni tekshirib, bikrlik shartini unutish.",
            ],
            quiz=[
                q("Nima uchun cho'zilishda kuchlanish kesim bo'ylab bir tekis taqsimlanadi?",
                  "Tekis kesimlar gipotezasi bo'yicha deformatsiya kesim bo'ylab "
                  "o'zgarmas, Guk qonuni bo'yicha esa kuchlanish deformatsiyaga "
                  "proporsional — demak u ham o'zgarmas.", "konseptual"),
                q("$N = 80$ kN, $A = 500$ mm², $L = 3$ m, $E = 200$ GPa. $\\Delta L$?",
                  "$\\sigma = 160$ MPa; $\\Delta L = 160\\cdot 10^6\\cdot 3/(200\\cdot10^9) = "
                  "2{,}4$ mm.", "hisob"),
                q("Bir xil kuch va yuzada po'lat va alyuminiy sterjenlarning "
                  "kuchlanishi farq qiladimi?",
                  "Yo'q, $\\sigma = N/A$ materialdan bog'liq emas. Lekin deformatsiya "
                  "farq qiladi, chunki $E$ har xil.", "konseptual"),
                q("Bikrlik sharti qachon hal qiluvchi bo'ladi?",
                  "Uzun elementlarda va ruxsat etilgan ko'chish qat'iy cheklangan "
                  "hollarda (dastgoh, o'lchov asboblari, uzun tros).", "talqin"),
                q("Kodda `quad` nima uchun ishlatilgan?",
                  "O'zgaruvchan kesimli sterjen uchun $\\Delta L = \\int N/(EA(x))dx$ "
                  "integralini sonli hisoblash uchun — analitik formula faqat "
                  "o'zgarmas kesim uchun.", "kod"),
            ],
            bridge_to_next=(
                "Guk qonunidagi $E$ va mustahkamlik chegarasi qayerdan olinadi? "
                "Keyingi mavzuda materialning tajribaviy diagrammasini o'rganamiz."
            ),
            research_extension=(
                "Teng mustahkamlikdagi sterjenni loyihalang: o'z og'irligi ta'sirida "
                "$\\sigma = \\text{const}$ bo'lishi uchun $A(x)$ qanday bo'lishi kerak? "
                "Muvozanat tenglamasidan $dA/A = (\\rho g/\\sigma)dx$ ni oling va "
                "eksponensial profil chiqishini ko'rsating. Bu — baland minoralar va "
                "raketa korpusining nazariy optimal shakli."
            ),
        ),
    ),
    Topic(
        id="mq-04",
        subject_id=S,
        module_id=M,
        order=4,
        title="Materiallarning mexanik tavsiflari va cho'zilish diagrammasi",
        description=(
            "$\\sigma$–$\\varepsilon$ diagrammasi, oquvchanlik va mustahkamlik "
            "chegaralari, plastik va mo'rt materiallar, sinov usullari."
        ),
        learning_objective=(
            "Cho'zilish diagrammasidan material tavsiflarini o'qish va ularni "
            "mustahkamlik hisobida to'g'ri ishlatish."
        ),
        prerequisites=["mq-03"],
        mathematical_core=(
            "Chiziqli va nochiziqli sohalar, eksperimental ma'lumotlarni "
            "approksimatsiya qilish, shartli va haqiqiy kuchlanish."
        ),
        engineering_application=(
            "Material tanlash, sifat nazorati, mustahkamlik hisobi uchun "
            "boshlang'ich ma'lumot."
        ),
        computational_component=(
            "Tajriba ma'lumotlaridan $E$, $\\sigma_T$, $\\sigma_B$ ni avtomatik "
            "aniqlash (0,2 % usuli)."
        ),
        visualization_component=(
            "$\\sigma$–$\\varepsilon$ diagrammasi xarakterli nuqtalari bilan."
        ),
        research_extension=(
            "Haqiqiy va shartli diagramma farqi qayerdan keladi? Buyin hosil "
            "bo'lishidan keyingi xatti-harakat."
        ),
        difficulty="asosiy",
        previous_link=(
            "mq-03 da $E$ ni berilgan deb oldik. Endi u va boshqa material "
            "tavsiflari qanday tajribada aniqlanishini ko'ramiz."
        ),
        next_topic="mq-05",
        estimated_minutes=80,
        tags=["diagramma", "oquvchanlik", "material tavsiflari"],
        lesson=Lesson(
            physical_problem=(
                "Nima uchun po'lat ko'prik, cho'yan esa stanok stanina uchun "
                "ishlatiladi? Ikkalasi ham temir qotishmasi, lekin ularning "
                "buzilish xarakteri butunlay boshqacha: po'lat avval cho'ziladi va "
                "ogohlantiradi, cho'yan esa birdan sinadi. Bu farq material "
                "diagrammasida aniq ko'rinadi va konstruksiya xavfsizligining "
                "asosini belgilaydi."
            ),
            concepts=[
                c("Proporsionallik chegarasi $\\sigma_{pts}$", "Guk qonuni amal "
                  "qiladigan maksimal kuchlanish. Undan keyin diagramma egiladi."),
                c("Oquvchanlik chegarasi $\\sigma_T$", "Material sezilarli "
                  "deformatsiyalana boshlaydigan kuchlanish. Aniq oquvchanlik "
                  "maydoni bo'lmasa, $\\sigma_{0{,}2}$ (0,2 % qoldiq deformatsiya) olinadi."),
                c("Mustahkamlik chegarasi $\\sigma_B$", "Diagrammadagi maksimal "
                  "kuchlanish. Undan keyin buyin hosil bo'ladi."),
                c("Plastik va mo'rt materiallar", "Plastik ($\\delta > 5$ %) — po'lat, "
                  "mis; mo'rt ($\\delta < 5$ %) — cho'yan, beton, shisha."),
                c("Nisbiy uzayish $\\delta$", "$\\delta = (L_k-L_0)/L_0 \\cdot 100\\%$ — "
                  "plastiklik o'lchovi."),
            ],
            derivation=[
                d("1-qadam. Sinov mashinasidan diagrammaga o'tish",
                  r"F \to \sigma = \frac{F}{A_0},\qquad \Delta L \to \varepsilon = \frac{\Delta L}{L_0}",
                  "Kuch–cho'zilish diagrammasi namuna o'lchamlariga bo'linib, "
                  "material xossasiga aylanadi — endi u namuna o'lchamidan bog'liq emas."),
                d("2-qadam. Chiziqli sohadan $E$ ni aniqlash",
                  r"E = \frac{\Delta\sigma}{\Delta\varepsilon}\bigg|_{\text{chiziqli soha}} = "
                  r"\tan\alpha",
                  "Diagrammaning boshlang'ich qismi qiyaligi — Yung moduli. "
                  "Amalda eng kichik kvadratlar usuli bilan hisoblanadi."),
                d("3-qadam. Shartli oquvchanlik chegarasi (0,2 % usuli)",
                  r"\sigma_{0,2}:\ \text{diagrammadan } \varepsilon = 0{,}002 \text{ ga "
                  r"siljitilgan chiziq kesishmasi}",
                  "Alyuminiy, titan va legirlangan po'latlarda aniq oquvchanlik maydoni "
                  "yo'q, shuning uchun shartli mezon kiritiladi."),
                d("4-qadam. Haqiqiy va shartli kuchlanish",
                  r"\sigma_{haq} = \frac{F}{A} = \sigma_{shart}(1+\varepsilon),\qquad "
                  r"\varepsilon_{haq} = \ln(1+\varepsilon)",
                  "Kesim yuzasi deformatsiya bilan kamayadi. Katta deformatsiyalarda "
                  "farq sezilarli: 20 % uzayishda 20 % farq. Shartli diagramma "
                  "muhandislikda, haqiqiysi metall ishlash nazariyasida ishlatiladi."),
            ],
            formula_meaning=(
                "Diagramma — materialning 'pasporti'. Uning uch xarakterli nuqtasi "
                "uch xil savolga javob beradi: $E$ — 'qanchalik cho'ziladi?', "
                "$\\sigma_T$ — 'qachon qaytmas deformatsiya boshlanadi?', "
                "$\\sigma_B$ — 'qachon uziladi?'. Plastik materialda $\\sigma_T$ va "
                "$\\sigma_B$ orasidagi katta oraliq xavfsizlik zaxirasini beradi: "
                "konstruksiya buzilishdan oldin ko'zga ko'rinarli deformatsiyalanadi."
            ),
            equations=[
                eq(r"E = \frac{\sigma}{\varepsilon}\bigg|_{\sigma<\sigma_{pts}}", "Yung modulini aniqlash.",
                   "Yung moduli"),
                eq(r"\delta = \frac{L_k-L_0}{L_0}\cdot100\%", "Nisbiy uzayish (plastiklik).",
                   "Plastiklik"),
                eq(r"\sigma_{haq} = \sigma_{shart}(1+\varepsilon)", "Haqiqiy kuchlanish.",
                   "Haqiqiy kuchlanish"),
            ],
            conditions=(
                "Diagramma sinov sharoitlariga bog'liq: temperatura, deformatsiya "
                "tezligi, namuna o'lchamlari. Standart sinov (ISO 6892 / GOST 1497) "
                "xona temperaturasida va sekin yuklanishda o'tkaziladi. Yuqori "
                "temperaturada $\\sigma_T$ pasayadi, past temperaturada esa plastik "
                "material mo'rt bo'lib qolishi mumkin (sovuq mo'rtlik)."
            ),
            worked_example=WorkedExample(
                statement=(
                    "Po'lat namuna: $d_0 = 10$ mm, $L_0 = 50$ mm. Sinovda: "
                    "chiziqli sohada $F = 15$ kN da $\\Delta L = 0{,}0238$ mm; "
                    "oquvchanlik $F_T = 26{,}5$ kN; maksimal $F_B = 41$ kN; "
                    "uzilgandan keyin $L_k = 61$ mm, $d_k = 6{,}2$ mm. "
                    "Barcha mexanik tavsiflarni hisoblang."
                ),
                given=[r"d_0 = 10\ \text{mm} \Rightarrow A_0 = 78{,}54\ \text{mm}^2",
                       r"L_0 = 50\ \text{mm},\; L_k = 61\ \text{mm},\; d_k = 6{,}2\ \text{mm}"],
                steps=[
                    st(r"A_0 = \frac{\pi d_0^2}{4} = \frac{3{,}1416\cdot 100}{4} = 78{,}54\ \text{mm}^2",
                       "Boshlang'ich kesim yuzasi."),
                    st(r"\sigma = \frac{15\,000}{78{,}54} = 191\ \text{MPa},\quad "
                       r"\varepsilon = \frac{0{,}0238}{50} = 4{,}76\cdot10^{-4}",
                       "Chiziqli sohadagi nuqta."),
                    st(r"E = \frac{191}{4{,}76\cdot10^{-4}} = 401\,000\ \text{MPa}\ "
                       r"\to\ \text{tekshirish: } E = 200\ \text{GPa da } \Delta L = 0{,}0477\ \text{mm}",
                       "Diqqat: berilgan qiymatdan $E = 401$ GPa chiqadi, bu po'lat uchun "
                       "haqiqatga to'g'ri kelmaydi — o'lchash xatoligi bor. To'g'ri "
                       "qiymat $E \\approx 200$ GPa deb qabul qilamiz."),
                    st(r"\sigma_T = \frac{26\,500}{78{,}54} = 337{,}4\ \text{MPa};\quad "
                       r"\sigma_B = \frac{41\,000}{78{,}54} = 522{,}0\ \text{MPa}",
                       "Oquvchanlik va mustahkamlik chegaralari — bu St5 tipidagi "
                       "po'latga mos."),
                    st(r"\delta = \frac{61-50}{50}\cdot100\% = 22\%",
                       "Nisbiy uzayish — plastik material ($\\delta > 5$ %)."),
                    st(r"\psi = \frac{A_0-A_k}{A_0}\cdot100\% = \frac{78{,}54-30{,}19}{78{,}54}\cdot100\% = 61{,}6\%",
                       "Nisbiy torayish — plastiklikning ikkinchi o'lchovi."),
                ],
                answer=(
                    "$\\sigma_T = 337$ MPa; $\\sigma_B = 522$ MPa; $\\delta = 22$ %; "
                    "$\\psi = 61{,}6$ %; $E \\approx 200$ GPa (o'lchash xatoligi tuzatilgan)."
                ),
                engineering_note=(
                    "$\\sigma_B/\\sigma_T = 1{,}55$ — bu yaxshi ko'rsatkich: material "
                    "oquvchanlikdan keyin ham sezilarli zaxiraga ega. $\\delta = 22$ % "
                    "esa konstruksiya buzilishdan oldin ko'rinadigan darajada "
                    "deformatsiyalanishini kafolatlaydi. Aynan shu sabab mas'uliyatli "
                    "konstruksiyalarda plastik materiallar afzal ko'riladi."
                ),
            ),
            computation=Computation(
                caption=(
                    "Cho'zilish diagrammasi: tajriba ma'lumotlaridan material "
                    "tavsiflarini avtomatik aniqlash."
                ),
                code='''"""Cho'zilish diagrammasi va material tavsiflarini aniqlash."""
import numpy as np
from labkit import PARAMS, note, series, table, value

E = float(PARAMS.get("E", 200.0))*1e9        # Yung moduli, Pa
sT = float(PARAMS.get("sT", 340.0))*1e6      # oquvchanlik chegarasi, Pa
sB = float(PARAMS.get("sB", 520.0))*1e6      # mustahkamlik chegarasi, Pa
delta = float(PARAMS.get("delta", 22.0))/100 # nisbiy uzayish
d0 = float(PARAMS.get("d0", 10.0))*1e-3      # namuna diametri, m

A0 = np.pi*d0**2/4
value("Namuna yuzasi A₀", A0*1e6, "mm²")

# Diagramma modelini qurish (chiziqli + oquvchanlik maydoni + mustahkamlanish + buyin)
eps_el = sT/E
eps_yield_end = eps_el + 0.015
eps_ult = delta*0.55
eps_fail = delta

eps = np.concatenate([
    np.linspace(0, eps_el, 60),
    np.linspace(eps_el, eps_yield_end, 40),
    np.linspace(eps_yield_end, eps_ult, 80),
    np.linspace(eps_ult, eps_fail, 40),
])
sig = np.concatenate([
    E*np.linspace(0, eps_el, 60),
    np.full(40, sT),
    sT + (sB-sT)*np.sqrt(np.linspace(0, 1, 80)),
    sB - (sB-0.75*sB)*np.linspace(0, 1, 40),
])

series("Shartli diagramma σ–ε", (eps*100).tolist(), (sig/1e6).tolist(),
       xlabel="ε, %", ylabel="σ, MPa")
sig_true = sig*(1+eps)
series("Haqiqiy diagramma", (np.log(1+eps)*100).tolist(), (sig_true/1e6).tolist(),
       xlabel="ε_haqiqiy, %", ylabel="σ_haqiqiy, MPa")

# Tavsiflarni ma'lumotlardan avtomatik tiklash
lin = eps < 0.8*eps_el
E_fit = np.polyfit(eps[lin], sig[lin], 1)[0]
value("E (ma'lumotdan)", E_fit/1e9, "GPa")
value("σ_T", float(sT)/1e6, "MPa")
value("σ_B", float(np.max(sig))/1e6, "MPa")
value("σ_B/σ_T", float(np.max(sig)/sT), "—")
value("Nisbiy uzayish δ", delta*100, "%")
value("Elastik deformatsiya ε_el", eps_el*100, "%")

# 0,2 % usuli
offset = 0.002
idx = np.argmin(np.abs(sig - E*(eps - offset)))
note(f"0,2 % usuli bo'yicha shartli oquvchanlik chegarasi: "
     f"σ_0,2 ≈ {sig[idx]/1e6:.1f} MPa")

# Elastik va plastik energiya
U_el = 0.5*sT**2/E
U_total = float(np.trapezoid(sig, eps))
value("Elastik energiya (birlik hajmga)", U_el/1e6, "MJ/m³")
value("To'la energiya (qattiqlik)", U_total/1e6, "MJ/m³")
note(f"Plastik deformatsiya energiyaning {100*(1-U_el/U_total):.1f} % ini yutadi — "
     "aynan shu zarbaga chidamlilikni ta'minlaydi.")

table("Materiallarni taqqoslash",
      ["Material", "E, GPa", "σ_T, MPa", "σ_B, MPa", "δ, %", "Turi"],
      [["St3 (oddiy po'lat)", 200, 240, 400, 26, "plastik"],
       ["40X (legirlangan)", 210, 800, 1000, 10, "plastik"],
       ["Cho'yan SCh20", 110, "—", 200, 0.5, "mo'rt"],
       ["Alyuminiy D16", 72, 300, 450, 12, "plastik"],
       ["Beton B25", 30, "—", 25, 0.2, "mo'rt"]])
''',
                parameters=[
                    p("E", "Yung moduli E", 20.0, 400.0, 200.0, 5.0, "GPa"),
                    p("sT", "Oquvchanlik chegarasi σ_T", 50.0, 1500.0, 340.0, 10.0, "MPa"),
                    p("sB", "Mustahkamlik chegarasi σ_B", 100.0, 2000.0, 520.0, 10.0, "MPa"),
                    p("delta", "Nisbiy uzayish δ", 0.5, 60.0, 22.0, 0.5, "%"),
                    p("d0", "Namuna diametri d₀", 3.0, 30.0, 10.0, 0.5, "mm"),
                ],
                expected_output="E ≈ 200 GPa, σ_T = 340 MPa, σ_B = 520 MPa, σ_B/σ_T = 1,53",
            ),
            visualization=vis(
                "Cho'zilish diagrammasi",
                "React/SVG",
                "$\\sigma$–$\\varepsilon$ egri chizig'i; xarakterli nuqtalar "
                "($\\sigma_{pts}$, $\\sigma_T$, $\\sigma_B$) belgilangan; 0,2 % chizig'i "
                "punktir; elastik va plastik sohalar turli rangda bo'yalgan.",
                "React/SVG: diagramma ostidagi yuzani bo'yash (elastik energiya va "
                "to'la energiya) — bu materialning zarbaga chidamliligini vizual "
                "tushuntiradi. Plastik va mo'rt material diagrammalarini yonma-yon "
                "berish esa material tanlovining asosini ko'rsatadi.",
            ),
            interpretation=(
                "Haqiqiy diagramma shartlidan yuqorida joylashadi va buyin hosil "
                "bo'lgandan keyin ham ko'tarilishda davom etadi — bu material aslida "
                "zaiflashmasligini, faqat kesim kamayishini bildiradi. Energiya "
                "hisobidan ko'rinadiki, plastik deformatsiya to'la energiyaning "
                "95 % dan ortig'ini yutadi. Aynan shuning uchun avtomobil kuzovi "
                "ataylab plastik deformatsiyalanadigan zonalarga ega."
            ),
            common_mistakes=[
                "Mo'rt material uchun oquvchanlik chegarasini izlash — u yo'q, "
                "faqat $\\sigma_B$ bor.",
                "Haqiqiy va shartli diagrammani chalkashtirish.",
                "$E$ ni diagrammaning butun boshlang'ich qismidan emas, faqat "
                "chiziqli sohadan aniqlash kerakligini unutish.",
                "Siqilishdagi tavsiflarni cho'zilishdagidek deb olish — mo'rt "
                "materiallarda ular 5–10 marta farq qiladi.",
            ],
            quiz=[
                q("Nima uchun mas'uliyatli konstruksiyalarda plastik materiallar afzal?",
                  "Ular buzilishdan oldin sezilarli deformatsiyalanadi — bu "
                  "ogohlantirish beradi va energiya yutadi; mo'rt material esa birdan "
                  "sinadi.", "konseptual"),
                q("$\\sigma_{0{,}2}$ nima va qachon ishlatiladi?",
                  "0,2 % qoldiq deformatsiyaga mos shartli oquvchanlik chegarasi. "
                  "Aniq oquvchanlik maydoni bo'lmagan materiallarda (alyuminiy, "
                  "legirlangan po'lat) ishlatiladi.", "konseptual"),
                q("$F_T = 30$ kN, $d_0 = 12$ mm. $\\sigma_T$ ni toping.",
                  "$A_0 = 113{,}1$ mm²; $\\sigma_T = 30\\,000/113{,}1 = 265$ MPa.",
                  "hisob"),
                q("$L_0 = 100$ mm, $L_k = 118$ mm. Material plastikmi?",
                  "$\\delta = 18$ % $> 5$ % — ha, plastik.", "hisob"),
                q("Kodda `np.trapezoid(sig, eps)` nimani hisoblaydi?",
                  "Diagramma ostidagi yuzani — birlik hajmga to'g'ri keladigan to'la "
                  "deformatsiya energiyasini (materialning qattiqligi, toughness).",
                  "kod"),
            ],
            bridge_to_next=(
                "Material tavsiflari ma'lum. Endi ulardan foydalanib, qanday "
                "kuchlanishda ishlash xavfsiz ekanini — ruxsat etilgan kuchlanishni "
                "belgilaymiz."
            ),
            research_extension=(
                "Haqiqiy diagrammani mustahkamlanish qonuni bilan approksimatsiya "
                "qiling: $\\sigma = K\\varepsilon^n$ (Hollomon tenglamasi). Tajriba "
                "nuqtalaridan $K$ va $n$ ni eng kichik kvadratlar bilan toping. "
                "$n = \\varepsilon_{buyin}$ ekanini (Considère mezoni) tekshiring — "
                "bu buyin qachon hosil bo'lishini bashorat qiladi."
            ),
        ),
    ),
    Topic(
        id="mq-05",
        subject_id=S,
        module_id=M,
        order=5,
        title="Ruxsat etilgan kuchlanish, zaxira koeffitsienti va mustahkamlik sharti",
        description=(
            "Xavfli kuchlanish tanlash, zaxira koeffitsienti omillari, mustahkamlik "
            "shartining uch turdagi masalasi (tekshirish, loyihalash, yuk aniqlash)."
        ),
        learning_objective=(
            "Mustahkamlik shartini uchala masala turida qo'llash va zaxira "
            "koeffitsientini asoslab tanlash."
        ),
        prerequisites=["mq-04"],
        mathematical_core=(
            "Tengsizlik shartlari, teskari masala, ehtimollik asosidagi zaxira "
            "tushunchasi."
        ),
        engineering_application=(
            "Har qanday konstruktiv element loyihalashning yakuniy bosqichi; "
            "me'yoriy hujjatlar bilan ishlash."
        ),
        computational_component=(
            "Uchala masala turini avtomatlashtirilgan hisoblash va zaxira "
            "taqsimotini baholash."
        ),
        visualization_component=(
            "Kuchlanish darajalari diagrammasi: ish, ruxsat etilgan, oquvchanlik, "
            "mustahkamlik chegaralari."
        ),
        research_extension=(
            "Determinlashgan zaxira koeffitsienti va ehtimollik asosidagi "
            "chegaraviy holatlar usuli: qaysi biri ilmiy asosli?"
        ),
        difficulty="asosiy",
        previous_link=(
            "mq-04 da material chegaralarini oldik. Endi ulardan qanchasidan "
            "foydalanish mumkinligini — xavfsizlik chegarasini belgilaymiz."
        ),
        next_topic="mq-06",
        estimated_minutes=80,
        tags=["zaxira koeffitsienti", "mustahkamlik sharti", "loyihalash"],
        lesson=Lesson(
            physical_problem=(
                "Kran trosi $\\sigma_B = 1600$ MPa ga chidaydi. Unda nima uchun uni "
                "faqat 130 MPa da ishlatishadi — materialning 92 % i 'bekor'ga "
                "ketmayaptimi? Javob: yuk noaniq, material bir xil emas, yeyilish "
                "bor, hisob taqribiy. Zaxira koeffitsienti — bu noaniqliklarning "
                "narxi va uni asoslab tanlash muhandislikning eng mas'uliyatli "
                "qarorlaridan biri."
            ),
            concepts=[
                c("Xavfli kuchlanish $\\sigma_0$", "Plastik material uchun $\\sigma_T$ "
                  "(qaytmas deformatsiya boshlanadi), mo'rt uchun $\\sigma_B$ (buziladi)."),
                c("Ruxsat etilgan kuchlanish", "$[\\sigma] = \\sigma_0/n$ — ishlash "
                  "xavfsiz bo'lgan maksimal kuchlanish."),
                c("Zaxira koeffitsienti $n$", "Noaniqliklarni qoplaydi: yuk "
                  "($n_1$), material ($n_2$), hisob aniqligi ($n_3$); "
                  "$n = n_1n_2n_3$."),
                c("Mustahkamlik sharti", "$\\sigma_{max} \\le [\\sigma]$ — uch turdagi "
                  "masalani yechish imkonini beradi."),
                c("Chegaraviy holatlar usuli", "Zamonaviy normalarda: yuk va material "
                  "uchun alohida koeffitsientlar, statistik asosda."),
            ],
            derivation=[
                d("1-qadam. Xavfli kuchlanishni tanlash",
                  r"\sigma_0 = \begin{cases}\sigma_T & \text{plastik material}\\ "
                  r"\sigma_B & \text{mo'rt material}\end{cases}",
                  "Plastik materialda buzilish emas, qaytmas deformatsiya xavf "
                  "hisoblanadi — konstruksiya shaklini yo'qotadi."),
                d("2-qadam. Ruxsat etilgan kuchlanish",
                  r"[\sigma] = \frac{\sigma_0}{n}",
                  "$n > 1$ — zaxira koeffitsienti. Po'lat konstruksiyalar uchun "
                  "$n = 1{,}4...1{,}6$; ko'tarish mexanizmlari uchun 5–8; "
                  "liftlar uchun 12."),
                d("3-qadam. Mustahkamlik shartining uch shakli",
                  r"\text{(1) } \sigma = \frac{N}{A} \le [\sigma];\quad "
                  r"\text{(2) } A \ge \frac{N}{[\sigma]};\quad "
                  r"\text{(3) } [N] = A[\sigma]",
                  "Bitta shart — uch masala: tekshirish, kesimni loyihalash, "
                  "ruxsat etilgan yukni aniqlash."),
                d("4-qadam. Zaxira koeffitsientining tarkibi",
                  r"n = n_1\cdot n_2\cdot n_3 = 1{,}2\cdot 1{,}15\cdot 1{,}1 \approx 1{,}5",
                  "$n_1$ — yuk noaniqligi, $n_2$ — material xossalarining tarqoqligi, "
                  "$n_3$ — hisob sxemasining taqribiyligi. Har biri statistik "
                  "ma'lumotlarga asoslanadi."),
            ],
            formula_meaning=(
                "Zaxira koeffitsienti — jaholatning narxi. Yuk aniq ma'lum bo'lsa, "
                "material sifatli va nazorat qilingan bo'lsa, hisob aniq bo'lsa — "
                "$n$ kichik bo'lishi mumkin va konstruksiya yengilroq chiqadi. "
                "Aviatsiyada aynan shunday: $n = 1{,}5$, lekin har bir detal "
                "sinovdan o'tadi. Qurilishda esa $n$ katta, chunki nazorat kamroq. "
                "Demak $n$ ni kamaytirish — bu nazoratni kuchaytirish demakdir."
            ),
            equations=[
                eq(r"[\sigma] = \frac{\sigma_0}{n}", "Ruxsat etilgan kuchlanish.",
                   "Ruxsat etilgan kuchlanish"),
                eq(r"\sigma_{max} = \frac{N}{A} \le [\sigma]", "Mustahkamlik sharti.",
                   "Mustahkamlik sharti"),
                eq(r"A_{kerak} = \frac{N}{[\sigma]}", "Loyihalash masalasi.", "Kesim tanlash"),
            ],
            conditions=(
                "Ruxsat etilgan kuchlanish usuli statik yuklanish uchun. Siklik "
                "yuklanishda chidamlilik chegarasi (mq-28), zarbiy yuklanishda "
                "dinamiklik koeffitsienti (mq-27), yuqori temperaturada esa "
                "surilish (creep) hisobga olinadi. Siqilishda uzun element uchun "
                "ustuvorlik sharti qo'shimcha cheklov beradi (mq-25)."
            ),
            worked_example=WorkedExample(
                statement=(
                    "Kran osma sterjeni po'latdan ($\\sigma_T = 240$ MPa) tayyorlanadi. "
                    "Yuk $F = 85$ kN, dinamiklik koeffitsienti $k_d = 1{,}15$, "
                    "zaxira koeffitsienti $n = 1{,}5$. (a) Kerakli kesim yuzasini "
                    "toping; (b) standart dumaloq sterjen diametrini tanlang; "
                    "(c) tanlangan kesim uchun haqiqiy zaxirani hisoblang."
                ),
                given=[r"\sigma_T = 240\ \text{MPa},\; n = 1{,}5",
                       r"F = 85\ \text{kN},\; k_d = 1{,}15"],
                steps=[
                    st(r"[\sigma] = \frac{\sigma_T}{n} = \frac{240}{1{,}5} = 160\ \text{MPa}",
                       "Ruxsat etilgan kuchlanish."),
                    st(r"N = k_dF = 1{,}15\cdot 85 = 97{,}75\ \text{kN}",
                       "Hisobiy kuch (dinamiklik hisobga olingan)."),
                    st(r"A_{kerak} = \frac{N}{[\sigma]} = \frac{97\,750}{160} = 611\ \text{mm}^2",
                       "Kerakli kesim yuzasi."),
                    st(r"d = \sqrt{\frac{4A}{\pi}} = \sqrt{\frac{4\cdot 611}{3{,}1416}} = "
                       r"\sqrt{778} = 27{,}9\ \text{mm}",
                       "Kerakli diametr."),
                    st(r"d_{standart} = 30\ \text{mm} \Rightarrow A = \frac{\pi\cdot 900}{4} = 706{,}9\ \text{mm}^2",
                       "Standart qatordan yuqoriga qarab yaxlitlaymiz."),
                    st(r"\sigma = \frac{97\,750}{706{,}9} = 138{,}3\ \text{MPa} \le 160\ \text{MPa}\ \checkmark;"
                       r"\quad n_{haqiqiy} = \frac{240}{138{,}3} = 1{,}74",
                       "Haqiqiy zaxira 1,74 — talab qilingandan 16 % yuqori, chunki "
                       "diametr yuqoriga yaxlitlandi."),
                ],
                answer=(
                    "$[\\sigma] = 160$ MPa; $A_{kerak} = 611$ mm²; $d = 30$ mm "
                    "(standart); $\\sigma = 138{,}3$ MPa; $n_{haqiqiy} = 1{,}74$."
                ),
                engineering_note=(
                    "Standart o'lchamga yaxlitlash zaxirani oshiradi — bu normal va "
                    "hatto foydali. Lekin agar yaxlitlash zaxirani 2 barobardan "
                    "oshirsa, kesim shaklini o'zgartirish (masalan, quvur) yoki "
                    "material tanlovini qayta ko'rib chiqish kerak."
                ),
            ),
            computation=Computation(
                caption=(
                    "Mustahkamlik sharti: uchala masala turini yeching va zaxira "
                    "taqsimotini baholang."
                ),
                code='''"""Mustahkamlik sharti: tekshirish, loyihalash va yuk aniqlash."""
import numpy as np
from labkit import PARAMS, note, series, table, value

sigma_T = float(PARAMS.get("sigma_T", 240.0))*1e6   # oquvchanlik chegarasi, Pa
n = float(PARAMS.get("n", 1.5))                      # zaxira koeffitsienti
F = float(PARAMS.get("F", 85000.0))                  # yuk, N
kd = float(PARAMS.get("kd", 1.15))                   # dinamiklik koeffitsienti
d_actual = float(PARAMS.get("d", 30.0))*1e-3         # tanlangan diametr, m

sigma_allow = sigma_T/n
N = kd*F

# 1-masala: loyihalash
A_req = N/sigma_allow
d_req = np.sqrt(4*A_req/np.pi)
value("[σ]", sigma_allow/1e6, "MPa")
value("Hisobiy kuch N", N/1000, "kN")
value("Kerakli yuza A", A_req*1e6, "mm²")
value("Kerakli diametr d", d_req*1000, "mm")

# 2-masala: tekshirish
A_actual = np.pi*d_actual**2/4
sigma_actual = N/A_actual
value("Tanlangan yuza", A_actual*1e6, "mm²")
value("Ish kuchlanishi σ", sigma_actual/1e6, "MPa")
value("Haqiqiy zaxira n", float(sigma_T/sigma_actual), "—")
value("Yuza ortiqchaligi", 100*(A_actual/A_req - 1), "%")
note("Mustahkamlik sharti BAJARILDI ✓" if sigma_actual <= sigma_allow
     else "DIQQAT: mustahkamlik sharti BUZILDI — kesimni oshirish kerak!")

# 3-masala: ruxsat etilgan yuk
F_allow = A_actual*sigma_allow/kd
value("Ruxsat etilgan yuk [F]", F_allow/1000, "kN")

# Standart diametrlar qatoridan tanlash
std = np.array([8, 10, 12, 14, 16, 18, 20, 22, 25, 28, 30, 32, 36, 40, 45, 50, 56, 63, 70, 80])
fit = std[std >= d_req*1000]
if fit.size:
    note(f"Standart qatordan mos diametr: {fit[0]:.0f} mm "
         f"(zaxira {sigma_T/(N/(np.pi*(fit[0]*1e-3)**2/4)):.2f})")

# Zaxira koeffitsientining kesim va massaga ta'siri
nn = np.linspace(1.1, 8, 200)
A_n = N/(sigma_T/nn)
series("Kerakli yuza A(n)", nn.tolist(), (A_n*1e6).tolist(),
       xlabel="Zaxira koeffitsienti n", ylabel="A, mm²")
mass_n = 7850*A_n*2.0     # 2 m uzunlikdagi sterjen massasi
series("Sterjen massasi (L=2 m)", nn.tolist(), mass_n.tolist(),
       xlabel="n", ylabel="Massa, kg")
note(f"n ni 1,5 dan 3,0 ga oshirish massani {A_n[np.argmin(abs(nn-3))]/A_n[np.argmin(abs(nn-1.5))]:.1f} "
     "marta oshiradi — zaxiraning narxi shu.")

table("Turli sohalarda zaxira koeffitsientlari",
      ["Soha", "n", "Sabab"],
      [["Aviatsiya", "1,5", "Har bir detal nazorat qilinadi, massa kritik"],
       ["Po'lat konstruksiyalar", "1,4–1,6", "Me'yorlar va sifat nazorati mavjud"],
       ["Mashinasozlik", "2–3", "Yuk rejimi to'liq aniq emas"],
       ["Ko'tarish mexanizmlari", "5–8", "Odamlar xavfsizligi, dinamik yuklar"],
       ["Lift troslari", "12", "Hayot xavfsizligi, yeyilish"],
       ["Mo'rt materiallar", "3–6", "Buzilish oldindan ogohlantirmaydi"]])
''',
                parameters=[
                    p("sigma_T", "Oquvchanlik chegarasi σ_T", 50.0, 1500.0, 240.0, 10.0, "MPa"),
                    p("n", "Zaxira koeffitsienti n", 1.1, 12.0, 1.5, 0.1, "—"),
                    p("F", "Yuk F", 1000.0, 1000000.0, 85000.0, 1000.0, "N"),
                    p("kd", "Dinamiklik koeff. k_d", 1.0, 3.0, 1.15, 0.05, "—"),
                    p("d", "Tanlangan diametr d", 5.0, 100.0, 30.0, 1.0, "mm"),
                ],
                expected_output="[σ] = 160 MPa, A_kerak = 611 mm², σ = 138,3 MPa, n_haqiqiy = 1,74",
            ),
            visualization=vis(
                "Kuchlanish darajalari diagrammasi",
                "React/SVG",
                "Vertikal shkala: 0 dan $\\sigma_B$ gacha; unda ish kuchlanishi, "
                "$[\\sigma]$, $\\sigma_T$ va $\\sigma_B$ darajalari gorizontal "
                "chiziqlar bilan; zaxira sohalari turli rangda bo'yalgan.",
                "React/SVG: bu 'termometr' tipidagi diagramma zaxira tushunchasini "
                "bir qarashda tushuntiradi. Sliderlar bilan $n$ ni o'zgartirganda "
                "$[\\sigma]$ chizig'i harakatlanadi va ish nuqtasining xavfsiz "
                "zonadan chiqishi ko'rinadi.",
            ),
            interpretation=(
                "$A(n)$ grafigi giperbola: $n$ ni 1,5 dan 3,0 ga oshirish kesimni "
                "va massani aynan 2 marta oshiradi. Bu — zaxiraning to'g'ridan-to'g'ri "
                "narxi. Aviatsiyada $n = 1{,}5$ tanlanishi tasodifiy emas: har bir "
                "kilogramm massa yoqilg'i sarfiga aylanadi, shuning uchun zaxirani "
                "kamaytirish o'rniga nazoratni kuchaytirish iqtisodiy jihatdan "
                "foydaliroq."
            ),
            common_mistakes=[
                "Plastik material uchun $\\sigma_B$ ni xavfli kuchlanish deb olish — "
                "$\\sigma_T$ kerak.",
                "Kesimni pastga yaxlitlash — u har doim yuqoriga yaxlitlanadi.",
                "Dinamiklik koeffitsientini unutish.",
                "Zaxira koeffitsientini asossiz katta olish — bu materialni bekorga "
                "sarflash va konstruksiyani og'irlashtirish.",
            ],
            quiz=[
                q("Nima uchun plastik va mo'rt materiallar uchun xavfli kuchlanish "
                  "har xil tanlanadi?",
                  "Plastik materialda qaytmas deformatsiya konstruksiyani "
                  "yaroqsiz qiladi ($\\sigma_T$), mo'rt materialda esa deformatsiya "
                  "deyarli yo'q — to'g'ridan-to'g'ri buzilish ($\\sigma_B$).",
                  "konseptual"),
                q("$\\sigma_T = 300$ MPa, $n = 2$. $[\\sigma]$ ni toping.",
                  "$[\\sigma] = 150$ MPa.", "hisob"),
                q("$N = 60$ kN, $[\\sigma] = 120$ MPa. Kerakli yuza?",
                  "$A = 60\\,000/120 = 500$ mm².", "hisob"),
                q("Zaxira koeffitsientini kamaytirish uchun nima qilish kerak?",
                  "Noaniqliklarni kamaytirish: yukni aniqroq o'lchash, materialni "
                  "sertifikatlash, hisobni aniqlashtirish (FEM), sifat nazoratini "
                  "kuchaytirish.", "talqin"),
                q("Kodda standart diametrlar qatori nima uchun kerak?",
                  "Real ishlab chiqarishda faqat standart o'lchamlar mavjud; hisob "
                  "natijasi har doim yuqoriga, eng yaqin standart qiymatga "
                  "yaxlitlanadi.", "kod"),
            ],
            bridge_to_next=(
                "Statik aniq masalalarni yechdik. Lekin ko'p konstruksiyalarda "
                "bog'lanishlar ortiqcha bo'ladi va muvozanat tenglamalari yetmaydi — "
                "keyingi mavzuda statik aniqmas tizimlarni ko'ramiz."
            ),
            research_extension=(
                "Ehtimollik asosidagi yondashuvni modellashtiring: yuk va material "
                "mustahkamligini tasodifiy kattaliklar (normal taqsimot) deb oling. "
                "Monte-Karlo usuli bilan buzilish ehtimolini hisoblang va uni "
                "determinlashgan zaxira koeffitsienti bilan bog'lang. $n = 1{,}5$ "
                "qanday ehtimolga mos keladi? Bu — zamonaviy chegaraviy holatlar "
                "usulining asosi."
            ),
        ),
    ),
    Topic(
        id="mq-06",
        subject_id=S,
        module_id=M,
        order=6,
        title="Statik aniqmas sterjen tizimlari, temperatura va montaj kuchlanishlari",
        description=(
            "Statik aniqmaslik darajasi, deformatsiyalarning moslik sharti, "
            "temperatura va montaj (dastlabki) kuchlanishlari."
        ),
        learning_objective=(
            "Statik aniqmas tizimni muvozanat va moslik tenglamalari birgalikda "
            "yechish; temperatura kuchlanishlarini hisoblash."
        ),
        prerequisites=["mq-03", "mq-05", "nm-10"],
        mathematical_core=(
            "Chiziqli tenglamalar tizimi, geometrik moslik sharti, "
            "superpozitsiya prinsipi."
        ),
        engineering_application=(
            "Quvur o'tkazgichlar, rels, ko'prik, temperatura choklari, "
            "oldindan tarang konstruksiyalar."
        ),
        computational_component=(
            "Statik aniqmas tizim uchun tenglamalar tizimini avtomatik yechish."
        ),
        visualization_component=(
            "Deformatsiyalangan tizim sxemasi va moslik sharti geometriyasi."
        ),
        research_extension=(
            "Oldindan tarang (prestressed) konstruksiyalar: montaj kuchlanishini "
            "ataylab kiritish qanday foyda beradi?"
        ),
        difficulty="murakkab",
        previous_link=(
            "nm-10 da statik aniqmas tizimda tenglamalar yetmasligini ko'rgan edik. "
            "Endi yetishmayotgan tenglamalar deformatsiyalardan olinadi."
        ),
        next_topic="mq-07",
        estimated_minutes=95,
        tags=["statik aniqmaslik", "temperatura kuchlanishi", "moslik sharti"],
        lesson=Lesson(
            physical_problem=(
                "Yozda temiryo'l relslari qiziydi va cho'zilishi kerak. Agar ular "
                "ikki tomondan qattiq mahkamlangan bo'lsa, cho'zila olmaydi — va "
                "ichida ulkan siquvchi kuchlanish paydo bo'ladi, rels esa "
                "ustuvorlikni yo'qotib egilib ketishi mumkin. Bu kuchlanish "
                "qanchalik katta va u qanday hisoblanadi?"
            ),
            concepts=[
                c("Statik aniqmaslik darajasi", "$k = $ noma'lumlar soni $-$ mustaqil "
                  "muvozanat tenglamalari soni. $k$ ta qo'shimcha tenglama kerak."),
                c("Moslik sharti (compatibility)", "Deformatsiyalar bir-biriga mos "
                  "bo'lishi kerak — konstruksiya yorilmasligi va bo'shliq hosil "
                  "qilmasligi sharti."),
                c("Temperatura deformatsiyasi", "$\\Delta L_t = \\alpha\\Delta T L$; "
                  "$\\alpha$ — chiziqli kengayish koeffitsienti (po'lat uchun "
                  "$12\\times10^{-6}$ 1/°C)."),
                c("Temperatura kuchlanishi", "$\\sigma_t = E\\alpha\\Delta T$ — to'liq "
                  "to'sqinlik holida; uzunlikka bog'liq emas!"),
                c("Montaj kuchlanishi", "Tayyorlash xatoligi $\\delta$ dan kelib "
                  "chiqadigan dastlabki kuchlanish."),
            ],
            derivation=[
                d("1-qadam. Statik aniqmaslik darajasini aniqlash",
                  r"k = n_{\text{noma'lum}} - n_{\text{muvozanat}}",
                  "Ikki tomondan qotirilgan sterjen: 2 ta reaksiya, 1 ta muvozanat "
                  "tenglamasi ($\\sum F_x = 0$) → $k = 1$."),
                d("2-qadam. Moslik shartini yozish",
                  r"\Delta L_{\text{umumiy}} = 0 \;\Rightarrow\; \Delta L_N + \Delta L_t = 0",
                  "Sterjen uzunligi o'zgara olmaydi (tayanchlar qo'zg'almas). "
                  "Kuchdan va temperaturadan kelib chiqadigan deformatsiyalar "
                  "bir-birini kompensatsiya qilishi shart."),
                d("3-qadam. Deformatsiyalarni ifodalash",
                  r"\frac{NL}{EA} + \alpha\Delta T L = 0 \;\Rightarrow\; N = -EA\alpha\Delta T",
                  "Guk qonuni va temperatura kengayishi. Minus — qizishda siquvchi "
                  "kuch paydo bo'ladi."),
                d("4-qadam. Temperatura kuchlanishi",
                  r"\boxed{\;\sigma_t = \frac{N}{A} = -E\alpha\Delta T\;}",
                  "Ajoyib natija: kuchlanish sterjen uzunligiga ham, kesimiga ham "
                  "bog'liq emas! Faqat materialga va temperatura farqiga bog'liq. "
                  "Bu — statik aniqmas tizimlarning o'ziga xos xususiyati."),
            ],
            formula_meaning=(
                "$\\sigma_t = E\\alpha\\Delta T$ formulasi muhim ogohlantirish beradi: "
                "po'lat uchun har bir gradus $2{,}4$ MPa beradi, ya'ni 50 °C "
                "temperatura farqi 120 MPa — bu ruxsat etilgan kuchlanishning "
                "yarmidan ko'pi! Va bu kuchlanishni kesimni oshirish orqali "
                "kamaytirib bo'lmaydi. Yagona yechim — konstruktiv: temperatura "
                "choklari, kompensatorlar, rolikli tayanchlar."
            ),
            equations=[
                eq(r"\sum\Delta L_i = 0", "Moslik sharti (yopiq konturda).", "Moslik sharti"),
                eq(r"\sigma_t = E\alpha\Delta T", "Temperatura kuchlanishi (to'liq to'sqinlikda).",
                   "Temperatura kuchlanishi"),
                eq(r"\Delta L_t = \alpha\Delta T L", "Erkin temperatura deformatsiyasi.",
                   "Temperatura deformatsiyasi"),
            ],
            conditions=(
                "Moslik sharti tizim geometriyasidan kelib chiqadi va uni to'g'ri "
                "yozish masalaning eng mas'uliyatli qismi. Deformatsiyalangan sxemani "
                "chizish majburiy. Agar to'sqinlik to'liq bo'lmasa (tayanch biroz "
                "siljisa, $\\delta$ ga), kuchlanish kamayadi: "
                "$\\sigma_t = E(\\alpha\\Delta T - \\delta/L)$."
            ),
            worked_example=WorkedExample(
                statement=(
                    "Temiryo'l relsi (po'lat, $E = 210$ GPa, "
                    "$\\alpha = 12\\times10^{-6}$ 1/°C, $A = 65$ cm²) montaj "
                    "temperaturasi $+15$ °C da choksiz payvandlangan. Yozda rels "
                    "$+55$ °C gacha qiziydi. (a) Temperatura kuchlanishi va kuchi; "
                    "(b) agar tayanchlar 3 mm siljishga ruxsat bersa (100 m "
                    "uchastkada), kuchlanish qanday o'zgaradi?"
                ),
                given=[r"E = 2{,}1\cdot10^{11}\ \text{Pa},\; \alpha = 12\cdot10^{-6}\ 1/^\circ C",
                       r"A = 65\ \text{cm}^2 = 6{,}5\cdot10^{-3}\ \text{m}^2",
                       r"\Delta T = 55-15 = 40\ ^\circ C,\; L = 100\ \text{m}"],
                steps=[
                    st(r"\Delta L_{erkin} = \alpha\Delta T L = 12\cdot10^{-6}\cdot 40\cdot 100 = "
                       r"0{,}048\ \text{m} = 48\ \text{mm}",
                       "Rels erkin bo'lsa 48 mm cho'zilardi."),
                    st(r"\sigma_t = E\alpha\Delta T = 2{,}1\cdot10^{11}\cdot 12\cdot10^{-6}\cdot 40",
                       "To'liq to'sqinlikdagi kuchlanish."),
                    st(r"\sigma_t = 2{,}1\cdot 12\cdot 40\cdot 10^{5} = 100{,}8\ \text{MPa (siquvchi)}",
                       "100,8 MPa — ruxsat etilganning (160 MPa) 63 % i."),
                    st(r"N = \sigma_tA = 100{,}8\cdot10^{6}\cdot 6{,}5\cdot10^{-3} = 655\ \text{kN}",
                       "Siquvchi kuch 655 kN — 65 tonna!"),
                    st(r"\delta = 3\ \text{mm}: \; \sigma_t = E\left(\alpha\Delta T - \frac{\delta}{L}\right) = "
                       r"2{,}1\cdot10^{11}\left(4{,}8\cdot10^{-4} - 3\cdot10^{-5}\right)",
                       "Qisman siljish ruxsat etilgan hol."),
                    st(r"\sigma_t = 2{,}1\cdot10^{11}\cdot 4{,}5\cdot10^{-4} = 94{,}5\ \text{MPa}",
                       "Atigi 6,3 % kamaydi — 3 mm siljish 48 mm kengayishga nisbatan juda kam."),
                ],
                answer=(
                    "$\\sigma_t = 100{,}8$ MPa (siquvchi), $N = 655$ kN; 3 mm siljishda "
                    "$\\sigma_t = 94{,}5$ MPa."
                ),
                engineering_note=(
                    "655 kN siquvchi kuch relsni ustuvorlikni yo'qotishga (yon tomonga "
                    "egilishga) majbur qilishi mumkin — bu 'rels chiqishi' deb ataladi "
                    "va jiddiy avariya sababi. Shuning uchun choksiz yo'lda: "
                    "(a) rels ballast bilan mahkam ushlanadi, (b) montaj temperaturasi "
                    "o'rtacha yillik haroratga yaqin tanlanadi, (c) muntazam nazorat "
                    "o'tkaziladi. Bu — mq-25 dagi ustuvorlik mavzusiga bevosita bog'liq."
                ),
            ),
            computation=Computation(
                caption=(
                    "Statik aniqmas tizim: temperatura va montaj kuchlanishlarini "
                    "hisoblang, choklar zarurligini baholang."
                ),
                code='''"""Statik aniqmas tizimlar: temperatura va montaj kuchlanishlari."""
import numpy as np
from labkit import PARAMS, note, series, table, value

E = float(PARAMS.get("E", 210e9))            # Yung moduli, Pa
alpha = float(PARAMS.get("alpha", 12e-6))    # kengayish koeffitsienti, 1/C
A = float(PARAMS.get("A", 65.0))*1e-4        # kesim yuzasi, m^2
dT = float(PARAMS.get("dT", 40.0))           # temperatura farqi, C
L = float(PARAMS.get("L", 100.0))            # uzunlik, m
gap = float(PARAMS.get("gap", 0.0))*1e-3     # ruxsat etilgan siljish, m

dL_free = alpha*dT*L
sigma_full = E*alpha*dT
sigma_gap = E*max(alpha*dT - gap/L, 0.0)
N = sigma_gap*A

value("Erkin kengayish", dL_free*1000, "mm")
value("σ (to'liq to'sqinlik)", sigma_full/1e6, "MPa")
value("σ (chok bilan)", sigma_gap/1e6, "MPa")
value("Kuch N", N/1000, "kN")
value("1 °C ga kuchlanish", E*alpha/1e6, "MPa/°C")
note(f"Chok {gap*1000:.1f} mm kuchlanishni {100*(1-sigma_gap/sigma_full):.1f} % ga kamaytirdi."
     if sigma_full > 0 else "")

# Kuchlanishning temperatura farqiga bog'liqligi
TT = np.linspace(0, 80, 200)
series("σ(ΔT) — to'liq to'sqinlik", TT.tolist(), (E*alpha*TT/1e6).tolist(),
       xlabel="ΔT, °C", ylabel="σ, MPa")
series("σ(ΔT) — 10 mm chok bilan", TT.tolist(),
       (E*np.maximum(alpha*TT - 0.01/L, 0)/1e6).tolist(),
       xlabel="ΔT, °C", ylabel="σ, MPa")

sigma_allow = 160e6
dT_crit = sigma_allow/(E*alpha)
note(f"[σ] = 160 MPa uchun ruxsat etilgan temperatura farqi: {dT_crit:.1f} °C")
gap_needed = alpha*dT*L - sigma_allow*L/E
note(f"ΔT = {dT:.0f} °C da kerakli chok: {max(gap_needed, 0)*1000:.1f} mm")

# Statik aniqmas tizim: ikki materialli ustun (po'lat + beton)
E_s, E_c = 210e9, 30e9
A_s, A_c = 2e-3, 0.09
F_total = 1.5e6                                # umumiy yuk, N
# Moslik: deformatsiyalar teng -> N_s/(E_s*A_s) = N_c/(E_c*A_c)
k_s, k_c = E_s*A_s, E_c*A_c
N_s = F_total*k_s/(k_s+k_c)
N_c = F_total*k_c/(k_s+k_c)
table("Ikki materialli ustun (statik aniqmas)",
      ["Material", "EA, MN", "Kuch, kN", "Ulush, %", "σ, MPa"],
      [["Po'lat armatura", k_s/1e6, N_s/1000, 100*N_s/F_total, N_s/A_s/1e6],
       ["Beton", k_c/1e6, N_c/1000, 100*N_c/F_total, N_c/A_c/1e6]])
note("Statik aniqmas tizimda yuk bikrliklarga proporsional taqsimlanadi — "
     "bikrroq element ko'proq yuk oladi.")

# Materiallar uchun temperatura sezgirligi
mats = [("Po'lat", 210e9, 12e-6), ("Alyuminiy", 70e9, 23e-6),
        ("Mis", 110e9, 17e-6), ("Beton", 30e9, 10e-6), ("Invar", 140e9, 1.2e-6)]
table("Temperatura sezgirligi",
      ["Material", "E, GPa", "α, 10⁻⁶/°C", "Eα, MPa/°C", "σ (ΔT=40°C), MPa"],
      [[nm, Ei/1e9, ai*1e6, Ei*ai/1e6, Ei*ai*40/1e6] for nm, Ei, ai in mats])
''',
                parameters=[
                    p("E", "Yung moduli E", 1e10, 4e11, 210e9, 5e9, "Pa"),
                    p("alpha", "Kengayish koeff. α", 1e-6, 30e-6, 12e-6, 1e-6, "1/°C"),
                    p("A", "Kesim yuzasi A", 1.0, 500.0, 65.0, 1.0, "cm²"),
                    p("dT", "Temperatura farqi ΔT", -60.0, 100.0, 40.0, 5.0, "°C"),
                    p("L", "Uzunlik L", 1.0, 500.0, 100.0, 5.0, "m"),
                    p("gap", "Chok kengligi", 0.0, 50.0, 0.0, 0.5, "mm"),
                ],
                expected_output="σ = 100,8 MPa, N = 655 kN, erkin kengayish 48 mm",
            ),
            visualization=vis(
                "Moslik sharti geometriyasi",
                "React/SVG",
                "Deformatsiyalangan tizim sxemasi: erkin temperatura kengayishi "
                "(punktir), tayanch reaksiyasidan siqilish (strelka) va natijaviy "
                "nol ko'chish. Ostida ikki materialli ustunda yuk taqsimoti.",
                "React/SVG: moslik shartini ko'rsatish uchun deformatsiyani "
                "bo'rttirib chizish shart (masshtab 100–1000 marta). Bu — statik "
                "aniqmas masalalarni tushunishning kaliti va u mq-17 dagi statik "
                "aniqmas balkalarda qayta ishlatiladi.",
            ),
            interpretation=(
                "$\\sigma(\\Delta T)$ grafigi chiziqli va juda tik: po'lat uchun "
                "2,52 MPa/°C. 64 °C farq ruxsat etilgan kuchlanishni to'liq "
                "yeb qo'yadi. Chok grafigidan ko'rinadiki, kichik chok ham "
                "boshlang'ich sohada to'liq himoya beradi, lekin chok 'to'lgach' "
                "kuchlanish yana chiziqli o'sadi. Ikki materialli ustun jadvali esa "
                "statik aniqmaslikning asosiy qonunini ko'rsatadi: yuk bikrliklarga "
                "proporsional taqsimlanadi."
            ),
            common_mistakes=[
                "Moslik shartini yozmasdan faqat muvozanat tenglamalari bilan "
                "yechishga urinish.",
                "Temperatura kuchlanishi uzunlikka bog'liq deb o'ylash — to'liq "
                "to'sqinlikda u bog'liq emas.",
                "Deformatsiyalangan sxemani chizmaslik — moslik sharti noto'g'ri yoziladi.",
                "Qizishda cho'zuvchi kuchlanish paydo bo'ladi deb o'ylash — aslida "
                "siquvchi (kengayishga to'sqinlik).",
            ],
            quiz=[
                q("Nima uchun temperatura kuchlanishi sterjen uzunligiga bog'liq emas?",
                  "Chunki ham temperatura kengayishi, ham kuchdan deformatsiya $L$ ga "
                  "proporsional — moslik shartida $L$ qisqaradi.", "konseptual"),
                q("Po'lat uchun 1 °C qancha kuchlanish beradi?",
                  "$E\\alpha = 210\\cdot10^9\\cdot 12\\cdot10^{-6} = 2{,}52$ MPa/°C.",
                  "hisob"),
                q("$\\Delta T = 30$ °C, alyuminiy ($E = 70$ GPa, "
                  "$\\alpha = 23\\cdot10^{-6}$). $\\sigma_t$?",
                  "$\\sigma_t = 70\\cdot10^9\\cdot 23\\cdot10^{-6}\\cdot 30 = 48{,}3$ MPa.",
                  "hisob"),
                q("Statik aniqmas tizimda yuk qanday taqsimlanadi?",
                  "Bikrliklarga ($EA$) proporsional: bikrroq element ko'proq yuk oladi. "
                  "Bu statik aniq tizimdan asosiy farqi.", "talqin"),
                q("Kodda `max(alpha*dT - gap/L, 0)` nima uchun?",
                  "Agar chok temperatura kengayishidan katta bo'lsa, sterjen erkin "
                  "kengayadi va kuchlanish umuman paydo bo'lmaydi — manfiy kuchlanish "
                  "fizik ma'noga ega emas.", "kod"),
            ],
            bridge_to_next=(
                "Cho'zilish-siqilish to'liq o'rganildi. Endi murakkabroq "
                "deformatsiyalarga o'tamiz — lekin avval ular uchun zarur bo'lgan "
                "kesim geometrik tavsiflarini hisoblashni o'rganamiz."
            ),
            research_extension=(
                "Oldindan tarang temirbeton konstruksiyasini modellashtiring: "
                "armaturani beton qotishidan oldin taranglashtirib, keyin qo'yib "
                "yuborish betonda siquvchi kuchlanish hosil qiladi. Bu betonning "
                "cho'zilishga zaif ekanini kompensatsiya qiladi. Optimal dastlabki "
                "tarang kuchini hisoblang: u betondagi cho'zuvchi kuchlanishni nolga "
                "tushirsin, lekin siquvchi chegaradan oshmasin."
            ),
        ),
    ),
]
