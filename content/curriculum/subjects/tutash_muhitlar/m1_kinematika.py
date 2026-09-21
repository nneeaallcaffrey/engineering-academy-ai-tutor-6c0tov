"""TMM / 1-modul: Kontinuum modeli va deformatsiya kinematikasi (tmm-01 … tmm-06)."""

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

S = "tutash-muhitlar"
M = "tmm-m1"

TOPICS = [
    Topic(
        id="tmm-01",
        subject_id=S,
        module_id=M,
        order=1,
        title="Tutash muhit gipotezasi va kontinuum modelining chegaralari",
        description=(
            "Moddaning diskret tuzilishidan uzluksiz modelga o'tish, "
            "elementar hajm tushunchasi va modelning qo'llanish chegaralari."
        ),
        learning_objective=(
            "Kontinuum gipotezasining mohiyatini va uning qachon buzilishini "
            "tushuntirish; Knudsen sonini baholash."
        ),
        prerequisites=["mq-01", "mq-02"],
        mathematical_core=(
            "Limit o'tish, o'rtachalash hajmi, uzluksiz va differensiallanuvchi "
            "maydonlar, Knudsen soni."
        ),
        engineering_application=(
            "Materiallar modellashtirish chegaralari, mikro/nano tizimlar, "
            "siyrak gaz dinamikasi, g'ovakli muhitlar."
        ),
        computational_component=(
            "Elementar hajm o'lchamining o'rtacha zichlik tebranishiga "
            "ta'sirini modellashtirish."
        ),
        visualization_component=(
            "Diskret zarralar → o'rtachalash hajmi → uzluksiz maydon o'tishi."
        ),
        research_extension=(
            "Nanoquvurlar va yupqa plyonkalarda kontinuum modeli qachon "
            "buziladi? O'lchamli effektlar."
        ),
        difficulty="kirish",
        previous_link=(
            "mq-02 da kuchlanishni $\\lim \\Delta F/\\Delta A$ deb ta'rifladik. "
            "Bu limit qanchalik kichik yuzada ma'noga ega? Javob aynan shu "
            "mavzuda."
        ),
        next_topic="tmm-02",
        estimated_minutes=70,
        tags=["kontinuum", "gipoteza", "Knudsen soni"],
        lesson=Lesson(
            physical_problem=(
                "Po'lat donlar o'lchami 10–100 mkm. Agar kuchlanishni 1 mkm "
                "yuzada o'lchasak, natija donning qayeriga tushganiga qarab "
                "keskin o'zgaradi. Lekin 1 mm yuzada u barqaror. Demak "
                "'nuqtadagi kuchlanish' tushunchasi shartli — u ma'lum "
                "o'lcham oralig'ida ma'noga ega. Bu oraliq qayerda?"
            ),
            concepts=[
                c("Tutash muhit gipotezasi", "Modda fazoni uzluksiz to'ldiradi "
                  "deb qabul qilinadi; barcha maydonlar uzluksiz va "
                  "differensiallanuvchi."),
                c("Elementar hajm (RVE)", "Statistik jihatdan vakil bo'lgan "
                  "hajm: mikrostruktura o'lchamidan katta, konstruksiya "
                  "o'lchamidan kichik."),
                c("Moddiy nuqta", "Kontinuumdagi nuqta — matematik nuqta emas, "
                  "balki ko'p zarrani o'z ichiga olgan elementar hajm."),
                c("Knudsen soni", "$Kn = \\ell/L$ — erkin yugurish yo'lining "
                  "xarakterli o'lchamga nisbati; $Kn < 0{,}01$ da kontinuum "
                  "o'rinli."),
                c("Masshtablar ajralishi", "$d_{mikro} \\ll L_{RVE} \\ll L_{makro}$ — "
                  "kontinuum modelining asosiy sharti."),
            ],
            derivation=[
                d("1-qadam. Zichlikni o'rtachalash orqali aniqlash",
                  r"\rho(\mathbf{x}) = \lim_{\Delta V\to\Delta V^*}\frac{\Delta m}{\Delta V}",
                  "Limit nolga emas, $\\Delta V^*$ — elementar hajmga intiladi. "
                  "Bu matematik limitdan farq va aynan shu farq kontinuum "
                  "modelining mohiyati."),
                d("2-qadam. Uch masshtab sohasini ajratish",
                  r"\Delta V \ll \Delta V^*:\ \text{tebranish katta};\quad "
                  r"\Delta V \approx \Delta V^*:\ \text{barqaror};\quad "
                  r"\Delta V \gg \Delta V^*:\ \text{makroskopik o'zgarish}",
                  "O'rtacha qiymat grafigida barqaror 'plato' bo'lishi kerak — "
                  "bu kontinuum modelining qo'llanish sharti."),
                d("3-qadam. Knudsen soni orqali mezon",
                  r"Kn = \frac{\ell}{L} < 0{,}01 \;\Rightarrow\; \text{kontinuum o'rinli}",
                  "Gazlar uchun $\\ell$ — molekulaning erkin yugurish yo'li "
                  "(havo uchun 68 nm); qattiq jismlar uchun — don o'lchami "
                  "yoki atomlararo masofa."),
                d("4-qadam. Maydonlarning uzluksizligi",
                  r"\rho(\mathbf{x}, t),\; \mathbf{v}(\mathbf{x},t),\; "
                  r"\sigma_{ij}(\mathbf{x},t) \in C^1",
                  "Barcha maydonlar uzluksiz differensiallanuvchi deb qabul "
                  "qilinadi — bu differensial tenglamalar yozish imkonini "
                  "beradi. Uzilishlar (zarba to'lqini, yoriq) alohida "
                  "ko'riladi."),
            ],
            formula_meaning=(
                "Kontinuum gipotezasi — bu soddalashtirish emas, balki "
                "masshtablarni ajratish. U $10^{23}$ ta molekula o'rniga "
                "bir nechta maydon funksiyasi bilan ishlash imkonini beradi. "
                "Narxi: mikrostruktura effektlari yo'qoladi va ular "
                "konstitutiv tenglamalarga (tmm-13) 'yashiriladi'. "
                "Knudsen soni esa chegarani aniq belgilaydi: mikroelektronika, "
                "vakuum texnikasi va nanotexnologiyada kontinuum modeli "
                "ishlamaydi."
            ),
            equations=[
                eq(r"\rho = \lim_{\Delta V\to\Delta V^*}\frac{\Delta m}{\Delta V}",
                   "Zichlikning kontinuum ta'rifi.", "Zichlik"),
                eq(r"Kn = \frac{\ell}{L}", "Knudsen soni.", "Knudsen soni"),
                eq(r"d_{mikro} \ll L_{RVE} \ll L_{makro}", "Masshtablar ajralishi sharti.",
                   "Masshtablar"),
            ],
            conditions=(
                "Kontinuum modeli $Kn < 0{,}01$ da to'liq o'rinli, "
                "$0{,}01 < Kn < 0{,}1$ da sirpanish shartlari bilan tuzatiladi, "
                "$Kn > 0{,}1$ da esa kinetik nazariya (Bolsman tenglamasi) "
                "kerak. Qattiq jismlarda: detal o'lchami don o'lchamidan "
                "kamida 10–20 marta katta bo'lishi kerak."
            ),
            worked_example=WorkedExample(
                statement=(
                    "(a) Havo uchun normal sharoitda ($\\ell = 68$ nm) "
                    "$D = 1$ mm li quvurda va $D = 100$ nm li nanokanalda "
                    "Knudsen sonini hisoblang. (b) Po'lat detal ($d_{don} = "
                    "50$ mkm) uchun minimal ishonchli o'lcham qancha?"
                ),
                given=[r"\ell_{havo} = 68\ \text{nm},\; D_1 = 10^{-3}\ \text{m},\; "
                       r"D_2 = 10^{-7}\ \text{m}",
                       r"d_{don} = 5\cdot10^{-5}\ \text{m}"],
                steps=[
                    st(r"Kn_1 = \frac{68\cdot10^{-9}}{10^{-3}} = 6{,}8\cdot10^{-5} \ll 0{,}01",
                       "Oddiy quvurda kontinuum modeli to'liq o'rinli."),
                    st(r"Kn_2 = \frac{68\cdot10^{-9}}{10^{-7}} = 0{,}68 > 0{,}1",
                       "Nanokanalda kontinuum modeli ishlamaydi — molekulyar "
                       "dinamika yoki kinetik nazariya kerak."),
                    st(r"L_{RVE} \ge 10\,d_{don} = 0{,}5\ \text{mm}",
                       "Elementar hajm kamida 10 ta donni o'z ichiga olishi kerak."),
                    st(r"L_{detal} \ge 10\,L_{RVE} = 5\ \text{mm}",
                       "Detal RVE dan kamida 10 marta katta bo'lishi kerak."),
                    st(r"\text{Xulosa: } L_{detal} \ge 5\ \text{mm}",
                       "Undan kichik detallarda (mikromexanika) don chegaralari "
                       "va kristallografik orientatsiya hisobga olinishi kerak."),
                ],
                answer=(
                    "$Kn_1 = 6{,}8\\cdot10^{-5}$ (kontinuum o'rinli); "
                    "$Kn_2 = 0{,}68$ (o'rinli emas); po'lat detal uchun "
                    "minimal o'lcham $\\approx 5$ mm."
                ),
                engineering_note=(
                    "MEMS (mikroelektromexanik tizimlar) va nanotexnologiyada "
                    "bu chegaralar hal qiluvchi. Mikrobalkalarning bikrligi "
                    "kontinuum nazariyasi bashorat qilganidan farq qiladi — "
                    "bu 'o'lchamli effekt' deb ataladi va gradiyentli "
                    "elastiklik nazariyalari bilan modellashtiriladi."
                ),
            ),
            computation=Computation(
                caption=(
                    "Kontinuum gipotezasi: o'rtachalash hajmini o'zgartirib, "
                    "zichlik tebranishini kuzating."
                ),
                code='''"""Kontinuum gipotezasi: o'rtachalash va Knudsen soni."""
import numpy as np
from labkit import PARAMS, note, series, table, value

d_particle = float(PARAMS.get("d_particle", 50.0))*1e-6   # zarra o'lchami, m
L_domain = float(PARAMS.get("L_domain", 5.0))*1e-3        # soha o'lchami, m
mfp = float(PARAMS.get("mfp", 68.0))*1e-9                 # erkin yugurish yo'li, m
L_char = float(PARAMS.get("L_char", 1.0))*1e-3            # xarakterli o'lcham, m
rho_true = 7850.0

Kn = mfp/L_char
value("Knudsen soni Kn", Kn, "—")
regime = ("Kontinuum" if Kn < 0.01 else
          "Sirpanish rejimi" if Kn < 0.1 else
          "O'tish rejimi" if Kn < 10 else "Erkin molekulyar")
note(f"Oqim rejimi: {regime}")

# Tasodifiy zarralar bilan o'rtachalash tajribasi
rng = np.random.default_rng(42)
n_particles = 20000
pts = rng.random((n_particles, 2))*L_domain
m_particle = rho_true*L_domain**2/n_particles

sizes = np.logspace(np.log10(d_particle/2), np.log10(L_domain/2), 40)
means, stds = [], []
for s in sizes:
    samples = []
    for _ in range(40):
        x0 = rng.random()*(L_domain - s)
        y0 = rng.random()*(L_domain - s)
        inside = np.sum((pts[:, 0] >= x0) & (pts[:, 0] < x0+s) &
                        (pts[:, 1] >= y0) & (pts[:, 1] < y0+s))
        samples.append(inside*m_particle/s**2)
    means.append(float(np.mean(samples)))
    stds.append(float(np.std(samples)/max(np.mean(samples), 1e-12)*100))

series("O'rtacha zichlik", (sizes*1e3).tolist(), means,
       xlabel="O'rtachalash hajmi, mm", ylabel="ρ, kg/m³")
series("Nisbiy tebranish", (sizes*1e3).tolist(), stds,
       xlabel="O'rtachalash hajmi, mm", ylabel="Tarqoqlik, %")

idx = next((i for i, s in enumerate(stds) if s < 5.0), len(stds)-1)
value("RVE o'lchami (tarqoqlik < 5 %)", float(sizes[idx]*1e3), "mm")
value("RVE / zarra o'lchami", float(sizes[idx]/d_particle), "—")
note("Kichik hajmda tarqoqlik katta (diskret ta'sir), katta hajmda barqaror — "
     "bu 'plato' kontinuum modelining qo'llanish sohasi.")

table("Knudsen soni bo'yicha rejimlar",
      ["Kn", "Rejim", "Model", "Misol"],
      [["< 0,01", "Kontinuum", "Navye–Stoks", "Oddiy quvur oqimi"],
       ["0,01–0,1", "Sirpanish", "N–S + sirpanish sharti", "Mikrokanal"],
       ["0,1–10", "O'tish", "Kinetik nazariya", "Nanokanal, vakuum"],
       ["> 10", "Erkin molekulyar", "Molekulyar dinamika", "Kosmos, yuqori vakuum"]])

table("Masshtablar ajralishi",
      ["Daraja", "Xarakterli o'lcham", "Model"],
      [["Atom", "10⁻¹⁰ m", "Kvant mexanikasi"],
       ["Mikrostruktura (don)", "10⁻⁵ m", "Kristall plastiklik"],
       ["RVE", "10⁻⁴…10⁻³ m", "Kontinuum (effektiv xossalar)"],
       ["Detal", "10⁻²…10⁰ m", "Kontinuum mexanikasi"],
       ["Konstruksiya", "10⁰…10² m", "Konstruksiya mexanikasi"]])
''',
                parameters=[
                    p("d_particle", "Zarra/don o'lchami", 1.0, 500.0, 50.0, 5.0, "µm"),
                    p("L_domain", "Soha o'lchami", 0.5, 50.0, 5.0, 0.5, "mm"),
                    p("mfp", "Erkin yugurish yo'li", 1.0, 1000.0, 68.0, 1.0, "nm"),
                    p("L_char", "Xarakterli o'lcham", 0.0001, 100.0, 1.0, 0.01, "mm"),
                ],
                expected_output="Kn = 6,8e-5 (kontinuum), RVE ≈ 0,5–1 mm",
            ),
            visualization=vis(
                "Diskret zarralardan uzluksiz maydonga o'tish",
                "React/SVG",
                "Uch panel: (1) tasodifiy zarralar to'plami, (2) ular ustiga "
                "turli o'lchamdagi o'rtachalash kvadratlari, (3) hosil bo'lgan "
                "uzluksiz zichlik maydoni. Ostida $\\rho(\\Delta V)$ grafigi.",
                "React/SVG: zarralarni `<circle>` bilan, o'rtachalash "
                "kvadratlarini `<rect>` bilan chizish. 'Plato' ni grafikda "
                "ko'rsatish — kontinuum gipotezasining eng aniq isboti.",
            ),
            interpretation=(
                "Tarqoqlik grafigi aniq 'plato' ko'rsatadi: kichik hajmda "
                "tebranish 30–50 %, RVE dan katta hajmda esa 5 % dan kam. "
                "Aynan shu barqaror soha kontinuum modelining yashash joyi. "
                "Knudsen jadvali esa gazlar uchun chegaralarni beradi — "
                "nanokanallarda Navye–Stoks tenglamalari umuman ishlamaydi."
            ),
            common_mistakes=[
                "Kontinuum limitini matematik limit ($\\Delta V \\to 0$) deb "
                "tushunish.",
                "Mikromexanika masalalarida kontinuum modelini tekshirmasdan "
                "qo'llash.",
                "Knudsen sonini hisoblashda noto'g'ri xarakterli o'lcham olish.",
                "RVE tushunchasini geometrik emas, statistik ekanini unutish.",
            ],
            quiz=[
                q("Nima uchun kontinuum limiti $\\Delta V \\to 0$ emas?",
                  "Juda kichik hajmda diskret zarralar soni kam bo'lib, o'rtacha "
                  "qiymat keskin tebranadi. Limit elementar (vakil) hajmga "
                  "intiladi.", "konseptual"),
                q("$Kn = 0{,}5$. Qaysi model kerak?",
                  "O'tish rejimi — kinetik nazariya yoki DSMC usuli; "
                  "Navye–Stoks ishlamaydi.", "hisob"),
                q("Don o'lchami 100 mkm. Minimal ishonchli detal o'lchami?",
                  "RVE $\\ge 1$ mm, detal $\\ge 10$ mm.", "hisob"),
                q("Kontinuum modelida mikrostruktura qayerga 'yashiriladi'?",
                  "Konstitutiv tenglamalarga: $E$, $\\nu$, oquvchanlik chegarasi "
                  "— bularning hammasi mikrostrukturaning o'rtachalangan "
                  "natijasi.", "talqin"),
                q("Kodda nima uchun tarqoqlik foizda hisoblangan?",
                  "Nisbiy tarqoqlik o'rtacha qiymatdan mustaqil mezon beradi "
                  "va RVE o'lchamini aniqlash uchun qulay (masalan, < 5 % "
                  "sharti).", "kod"),
            ],
            bridge_to_next=(
                "Kontinuum modeli qabul qilindi. Endi uning tili — tenzor "
                "apparatini o'zlashtiramiz."
            ),
            research_extension=(
                "Kompozit material uchun RVE o'lchamini sonli aniqlang: "
                "tasodifiy joylashgan tolalar bilan sohani generatsiya qilib, "
                "turli o'lchamdagi bo'laklarda effektiv $E$ ni hisoblang. "
                "Tarqoqlik 5 % dan kam bo'ladigan o'lchamni toping va uni "
                "tola diametriga nisbatan ifodalang."
            ),
        ),
    ),
    Topic(
        id="tmm-02",
        subject_id=S,
        module_id=M,
        order=2,
        title="Tenzor hisobi asoslari: indeksli yozuv va koordinata almashtirishlari",
        description=(
            "Skalyar, vektor va tenzorlar, indeksli (Eynshteyn) yozuv, "
            "koordinata almashtirishda tenzorning o'zgarishi, invariantlar."
        ),
        learning_objective=(
            "Indeksli yozuvda amallar bajarish va tenzorlarni koordinata "
            "almashtirishda to'g'ri qayta hisoblash."
        ),
        prerequisites=["tmm-01", "nm-17", "mq-19"],
        mathematical_core=(
            "Eynshteyn yig'indi qoidasi, Kroneker deltasi, Levi-Civita "
            "simvoli, ortogonal almashtirish, invariantlar."
        ),
        engineering_application=(
            "Barcha kontinuum mexanikasi hisoblarining tili; FEM dasturlari "
            "ichki mantiqining asosi."
        ),
        computational_component=(
            "Tenzor amallarini NumPy bilan bajarish, koordinata "
            "almashtirishni tekshirish, invariantlarni hisoblash."
        ),
        visualization_component=(
            "Tenzorning burilgan koordinatalarda o'zgarishi; invariantlarning "
            "o'zgarmasligi."
        ),
        research_extension=(
            "Egri chiziqli koordinatalarda (silindrik, sferik) tenzor "
            "komponentalari qanday o'zgaradi? Kristoffel simvollari."
        ),
        difficulty="asosiy",
        previous_link=(
            "nm-17 dagi inersiya tenzori va mq-19 dagi Mor doirasi bir xil "
            "matematik strukturaga ega edi. Endi bu strukturani umumiy "
            "shaklda o'rganamiz."
        ),
        next_topic="tmm-03",
        estimated_minutes=85,
        tags=["tenzor", "indeksli yozuv", "invariant"],
        lesson=Lesson(
            physical_problem=(
                "Kuchlanish holati koordinata sistemasidan bog'liq emas, "
                "lekin uning komponentalari bog'liq. Qanday qilib bir xil "
                "fizik holatni turli koordinatalarda bir xil deb tanib "
                "olamiz? Javob: tenzor tushunchasida va uning invariantlarida. "
                "Bu apparat butun kontinuum mexanikasining tili."
            ),
            concepts=[
                c("Tenzor tartibi", "0 — skalyar (temperatura), 1 — vektor "
                  "(tezlik), 2 — matritsa ko'rinishida (kuchlanish), 4 — "
                  "elastiklik tenzori."),
                c("Eynshteyn yig'indi qoidasi", "Takrorlanuvchi indeks bo'yicha "
                  "yig'indi olinadi: $a_ib_i = \\sum_i a_ib_i$."),
                c("Kroneker deltasi", "$\\delta_{ij} = 1$ ($i=j$), $0$ ($i\\neq j$) — "
                  "birlik tenzor."),
                c("Levi-Civita simvoli", "$\\epsilon_{ijk}$ — vektor ko'paytmani "
                  "indeksli yozishda ishlatiladi: "
                  "$(\\mathbf{a}\\times\\mathbf{b})_i = \\epsilon_{ijk}a_jb_k$."),
                c("Invariantlar", "Koordinata almashtirishda o'zgarmaydigan "
                  "kombinatsiyalar: $I_1 = \\sigma_{ii}$, $I_2$, $I_3 = \\det\\sigma$."),
            ],
            derivation=[
                d("1-qadam. Tenzorning almashtirish qoidasi orqali ta'rifi",
                  r"\sigma'_{ij} = Q_{ik}Q_{jl}\sigma_{kl},\qquad Q_{ij} = \mathbf{e}'_i\cdot\mathbf{e}_j",
                  "Ikkinchi tartibli tenzor har bir indeks bo'yicha vektor "
                  "kabi almashadi. Bu — tenzorning haqiqiy ta'rifi (matritsa "
                  "bo'lish yetarli emas)."),
                d("2-qadam. Birinchi invariant",
                  r"I_1 = \sigma'_{ii} = Q_{ik}Q_{il}\sigma_{kl} = \delta_{kl}\sigma_{kl} = \sigma_{kk}",
                  "$[Q]$ ortogonal bo'lgani uchun $Q_{ik}Q_{il} = \\delta_{kl}$. "
                  "Iz (trace) invariant."),
                d("3-qadam. Uchta asosiy invariant",
                  r"I_1 = \sigma_{ii},\quad I_2 = \tfrac{1}{2}(\sigma_{ii}\sigma_{jj} - \sigma_{ij}\sigma_{ij}),"
                  r"\quad I_3 = \det(\sigma_{ij})",
                  "Ular xarakteristik tenglama koeffitsientlari: "
                  "$\\lambda^3 - I_1\\lambda^2 + I_2\\lambda - I_3 = 0$."),
                d("4-qadam. Sferik va deviator qismlarga ajratish",
                  r"\sigma_{ij} = \underbrace{\tfrac{1}{3}\sigma_{kk}\delta_{ij}}_{\text{sferik}} + "
                  r"\underbrace{s_{ij}}_{\text{deviator}},\qquad s_{ii} = 0",
                  "Sferik qism hajm o'zgarishiga, deviator shakl o'zgarishiga "
                  "javob beradi (mq-20). Bu ajratish plastiklik nazariyasida "
                  "hal qiluvchi (tmm-21)."),
            ],
            formula_meaning=(
                "Indeksli yozuv ixchamlik uchun emas, aniqlik uchun kerak: "
                "$\\sigma'_{ij} = Q_{ik}Q_{jl}\\sigma_{kl}$ formulasi tenzorning "
                "fizik mohiyatini — koordinatalardan mustaqilligini — "
                "matematik jihatdan qat'iy ifodalaydi. Invariantlar esa shu "
                "mustaqillikning konkret ko'rinishi: ular fizik holatni "
                "koordinatalarga bog'liq bo'lmagan holda tavsiflaydi va aynan "
                "shuning uchun mustahkamlik kriteriylari (mq-21, tmm-21) "
                "ularga asoslanadi."
            ),
            equations=[
                eq(r"\sigma'_{ij} = Q_{ik}Q_{jl}\sigma_{kl}", "Tenzorning almashtirish qoidasi.",
                   "Almashtirish"),
                eq(r"I_1 = \sigma_{kk},\quad I_3 = \det\sigma", "Asosiy invariantlar.",
                   "Invariantlar"),
                eq(r"\sigma_{ij} = \tfrac{1}{3}\sigma_{kk}\delta_{ij} + s_{ij}",
                   "Sferik va deviator qismlarga ajratish.", "Ajratish"),
            ],
            conditions=(
                "Almashtirish qoidasi ortogonal (Dekart) koordinatalar uchun. "
                "Egri chiziqli koordinatalarda ko'variant va kontrvariant "
                "komponentalar farqlanadi va Kristoffel simvollari paydo "
                "bo'ladi. Muhandislik hisoblarida odatda Dekart yoki "
                "silindrik koordinatalar yetarli."
            ),
            worked_example=WorkedExample(
                statement=(
                    "Kuchlanish tenzori (MPa): "
                    "$\\sigma = \\begin{pmatrix}100 & 40 & 0\\\\ 40 & -20 & 0\\\\ "
                    "0 & 0 & 60\\end{pmatrix}$. (a) Invariantlarni toping; "
                    "(b) asosiy kuchlanishlarni hisoblang; (c) z o'qi atrofida "
                    "$30°$ ga burib, komponentalarni qayta hisoblang va "
                    "invariantlar saqlanishini tekshiring."
                ),
                given=[r"\sigma_{11}=100,\ \sigma_{22}=-20,\ \sigma_{33}=60,\ \sigma_{12}=40\ \text{MPa}"],
                steps=[
                    st(r"I_1 = 100-20+60 = 140\ \text{MPa}",
                       "Birinchi invariant — diagonal yig'indisi."),
                    st(r"I_2 = (100)(-20)+(-20)(60)+(60)(100) - 40^2 = "
                       r"-2000-1200+6000-1600 = 1200\ \text{MPa}^2",
                       "Ikkinchi invariant."),
                    st(r"I_3 = 60\big[(100)(-20)-40^2\big] = 60(-3600) = -216\,000\ \text{MPa}^3",
                       "Determinant (z o'qi asosiy o'q bo'lgani uchun oson)."),
                    st(r"\lambda^3 - 140\lambda^2 + 1200\lambda + 216\,000 = 0",
                       "Xarakteristik tenglama."),
                    st(r"\sigma_1 = 113{,}0;\quad \sigma_2 = 60{,}0;\quad \sigma_3 = -33{,}0\ \text{MPa}",
                       "Ildizlar. Tekshirish: "
                       "$113{,}0+60{,}0-33{,}0 = 140{,}0 = I_1$ ✓"),
                    st(r"30^\circ\ \text{burilishda: } \sigma'_{11} = 100\cos^2 30 + (-20)\sin^2 30 + "
                       r"2(40)\sin30\cos30 = 75-5+34{,}64 = 104{,}64",
                       "Yangi komponenta; $I_1' = 104{,}64 + 15{,}36 + 60 = 140$ ✓ — "
                       "invariant saqlandi."),
                ],
                answer=(
                    "$I_1 = 140$ MPa, $I_2 = 1200$ MPa², $I_3 = -216\\,000$ MPa³; "
                    "$\\sigma_{1,2,3} = 113{,}0;\\ 60{,}0;\\ -33{,}0$ MPa; "
                    "burilishda invariantlar saqlanadi."
                ),
                engineering_note=(
                    "Invariantlarning saqlanishi — hisobni tekshirishning eng "
                    "ishonchli usuli. FEM dasturlari natijalarini tekshirishda "
                    "ham shu prinsip ishlatiladi: fon Mizes kuchlanishi "
                    "invariantlar orqali ifodalanadi va koordinata "
                    "sistemasidan bog'liq emas."
                ),
            ),
            computation=Computation(
                caption=(
                    "Tenzor amallari: koordinata almashtirish, invariantlar va "
                    "asosiy qiymatlar."
                ),
                code='''"""Tenzor hisobi: almashtirish, invariantlar, asosiy qiymatlar."""
import numpy as np
from labkit import PARAMS, note, series, table, value

s11 = float(PARAMS.get("s11", 100.0))
s22 = float(PARAMS.get("s22", -20.0))
s33 = float(PARAMS.get("s33", 60.0))
s12 = float(PARAMS.get("s12", 40.0))
angle = float(PARAMS.get("angle", 30.0))

T = np.array([[s11, s12, 0.0], [s12, s22, 0.0], [0.0, 0.0, s33]])

def invariants(A):
    I1 = np.trace(A)
    I2 = 0.5*(np.trace(A)**2 - np.trace(A @ A))
    I3 = np.linalg.det(A)
    return I1, I2, I3

I1, I2, I3 = invariants(T)
value("I₁ (iz)", I1, "MPa")
value("I₂", I2, "MPa²")
value("I₃ (determinant)", I3, "MPa³")

eigvals, eigvecs = np.linalg.eigh(T)
principals = np.sort(eigvals)[::-1]
for i, s in enumerate(principals):
    value(f"σ_{i+1}", float(s), "MPa")
note(f"Tekshirish: Σσ_i = {np.sum(principals):.6f}, I₁ = {I1:.6f} ✓")
note(f"Tekshirish: Πσ_i = {np.prod(principals):.3f}, I₃ = {I3:.3f} ✓")

# Koordinata almashtirish (z o'qi atrofida burish)
th = np.radians(angle)
Q = np.array([[np.cos(th), np.sin(th), 0.0],
              [-np.sin(th), np.cos(th), 0.0],
              [0.0, 0.0, 1.0]])
T_rot = Q @ T @ Q.T
table("Burilgan koordinatalarda tenzor (MPa)",
      ["", "1", "2", "3"],
      [[f"{i+1}", float(T_rot[i, 0]), float(T_rot[i, 1]), float(T_rot[i, 2])]
       for i in range(3)])

I1r, I2r, I3r = invariants(T_rot)
note(f"Invariantlar burilishdan keyin: I₁ = {I1r:.6f}, I₂ = {I2r:.6f}, I₃ = {I3r:.3f}")
note(f"Farq: ΔI₁ = {abs(I1r-I1):.2e}, ΔI₂ = {abs(I2r-I2):.2e}, ΔI₃ = {abs(I3r-I3):.2e} — "
     "invariantlar saqlanadi ✓")

# Burchakka bog'liqlik
aa = np.linspace(0, 180, 181)
s11_arr, s12_arr, I1_arr = [], [], []
for a in aa:
    t = np.radians(a)
    Qa = np.array([[np.cos(t), np.sin(t), 0], [-np.sin(t), np.cos(t), 0], [0, 0, 1]])
    Ta = Qa @ T @ Qa.T
    s11_arr.append(float(Ta[0, 0]))
    s12_arr.append(float(Ta[0, 1]))
    I1_arr.append(float(np.trace(Ta)))
series("σ'₁₁(α)", aa.tolist(), s11_arr, xlabel="Burilish burchagi, deg", ylabel="σ, MPa")
series("σ'₁₂(α)", aa.tolist(), s12_arr, xlabel="Burilish burchagi, deg", ylabel="τ, MPa")
series("I₁(α) — invariant", aa.tolist(), I1_arr, xlabel="Burilish burchagi, deg", ylabel="I₁, MPa")

# Sferik va deviator qismlar
s_mean = I1/3
T_sph = s_mean*np.eye(3)
T_dev = T - T_sph
value("O'rtacha kuchlanish σ_m", s_mean, "MPa")
value("Deviator izi (0 bo'lishi kerak)", float(np.trace(T_dev)), "MPa")
J2 = 0.5*np.sum(T_dev*T_dev)
value("J₂ (deviator 2-invarianti)", J2, "MPa²")
value("fon Mizes σ_ekv = √(3J₂)", float(np.sqrt(3*J2)), "MPa")

# Indeksli yozuv namunalari
delta = np.eye(3)
note(f"δ_ii = {np.trace(delta):.0f} (3 ga teng)")
eps = np.zeros((3, 3, 3))
eps[0, 1, 2] = eps[1, 2, 0] = eps[2, 0, 1] = 1
eps[0, 2, 1] = eps[2, 1, 0] = eps[1, 0, 2] = -1
a_v, b_v = np.array([1.0, 2.0, 3.0]), np.array([4.0, 5.0, 6.0])
cross_idx = np.einsum("ijk,j,k->i", eps, a_v, b_v)
note(f"ε_ijk a_j b_k = {cross_idx} , np.cross = {np.cross(a_v, b_v)} — mos ✓")

table("Tenzor tartiblari",
      ["Tartib", "Komponentalar soni", "Misol"],
      [[0, 1, "Temperatura, zichlik"],
       [1, 3, "Tezlik, kuch"],
       [2, 9, "Kuchlanish, deformatsiya"],
       [4, 81, "Elastiklik tenzori C_ijkl"]])
''',
                parameters=[
                    p("s11", "σ₁₁", -300.0, 300.0, 100.0, 5.0, "MPa"),
                    p("s22", "σ₂₂", -300.0, 300.0, -20.0, 5.0, "MPa"),
                    p("s33", "σ₃₃", -300.0, 300.0, 60.0, 5.0, "MPa"),
                    p("s12", "σ₁₂", -200.0, 200.0, 40.0, 5.0, "MPa"),
                    p("angle", "Burilish burchagi", 0.0, 180.0, 30.0, 5.0, "deg"),
                ],
                expected_output="I₁ = 140 MPa, σ₁ = 113,0 MPa, invariantlar saqlanadi",
            ),
            visualization=vis(
                "Tenzor komponentalarining burilishda o'zgarishi",
                "React/SVG",
                "$\\sigma'_{11}(\\alpha)$ va $\\sigma'_{12}(\\alpha)$ sinusoidal "
                "egri chiziqlari; ularning ostida $I_1(\\alpha)$ — gorizontal "
                "to'g'ri chiziq (invariant).",
                "React/SVG: invariantning gorizontal chiziq bo'lishi — "
                "tenzor tushunchasining eng aniq vizual isboti. "
                "Komponentalar tebranadi, invariant esa qimirlamaydi.",
            ),
            interpretation=(
                "Grafiklarda komponentalar $180°$ davr bilan o'zgaradi, "
                "invariant esa mutlaqo o'zgarmaydi — bu tenzor tushunchasining "
                "mohiyati. Deviator izining nolga tengligi va "
                "$\\sqrt{3J_2}$ ning fon Mizes kuchlanishiga tengligi esa "
                "mq-21 dagi kriteriyning invariant tabiatini tasdiqlaydi."
            ),
            common_mistakes=[
                "Har qanday $3\\times3$ matritsani tenzor deb hisoblash — "
                "tenzor almashtirish qoidasiga bo'ysunishi kerak.",
                "Eynshteyn yig'indi qoidasida erkin va bog'langan indekslarni "
                "chalkashtirish.",
                "$Q$ matritsasini transponirlashda xato qilish "
                "($\\sigma' = Q\\sigma Q^T$).",
                "Invariantlarni faqat asosiy o'qlarda hisoblash mumkin deb "
                "o'ylash — ular istalgan koordinatalarda bir xil.",
            ],
            quiz=[
                q("Nima uchun invariantlar muhim?",
                  "Ular koordinata sistemasidan bog'liq emas, demak fizik "
                  "holatni obyektiv tavsiflaydi. Mustahkamlik kriteriylari "
                  "aynan ularga asoslanadi.", "konseptual"),
                q("Eynshteyn yozuvida $a_{ii}$ nimani anglatadi?",
                  "$\\sum_i a_{ii} = a_{11}+a_{22}+a_{33}$ — matritsaning izi.",
                  "konseptual"),
                q("$\\sigma_{ij} = \\text{diag}(100, 50, -30)$. $I_1$ va "
                  "$\\sigma_m$ ni toping.",
                  "$I_1 = 120$ MPa; $\\sigma_m = 40$ MPa.", "hisob"),
                q("Deviator tenzorning izi nimaga teng va nega?",
                  "Nolga: $s_{ii} = \\sigma_{ii} - \\frac{1}{3}\\sigma_{kk}\\delta_{ii} = "
                  "\\sigma_{ii} - \\sigma_{kk} = 0$ (chunki $\\delta_{ii} = 3$).",
                  "hisob"),
                q("Kodda `np.einsum('ijk,j,k->i', eps, a, b)` nima hisoblaydi?",
                  "Levi-Civita simvoli orqali vektor ko'paytmani — bu indeksli "
                  "yozuvning to'g'ridan-to'g'ri amalga oshirilishi.", "kod"),
            ],
            bridge_to_next=(
                "Tenzor apparati tayyor. Endi uni harakatni tavsiflashga "
                "qo'llaymiz: deformatsiya kinematikasi."
            ),
            research_extension=(
                "Silindrik koordinatalarda kuchlanish tenzorining "
                "komponentalarini hisoblang va Dekart koordinatalardan "
                "o'tish matritsasini quring. Quvur (bosimli idish) masalasida "
                "$\\sigma_{rr}$, $\\sigma_{\\theta\\theta}$, $\\sigma_{zz}$ "
                "komponentalarini toping — bu tmm-16 da qo'llaniladi."
            ),
            manim=manim(
                scene="TensorTransformScene",
                module="animatsiya/scenes/tmm_tensor.py",
                title="Tenzorning koordinata almashtirishda o'zgarishi",
                summary="Koordinata o'qlari buriladi, tenzor komponentalari "
                        "o'zgaradi, lekin invariantlar va asosiy o'qlar o'zgarmaydi.",
            ),
        ),
    ),
    Topic(
        id="tmm-03",
        subject_id=S,
        module_id=M,
        order=3,
        title="Deformatsiya kinematikasi: Lagranj va Eyler tavsiflari",
        description=(
            "Moddiy va fazoviy koordinatalar, harakat funksiyasi, moddiy "
            "hosila, Lagranj va Eyler yondashuvlarining farqi."
        ),
        learning_objective=(
            "Ikki tavsif o'rtasida o'tish va moddiy hosilani to'g'ri "
            "hisoblash."
        ),
        prerequisites=["tmm-02", "nm-06"],
        mathematical_core=(
            "Harakat funksiyasi $\\mathbf{x} = \\chi(\\mathbf{X}, t)$, "
            "moddiy hosila $D/Dt = \\partial/\\partial t + "
            "\\mathbf{v}\\cdot\\nabla$, Yakobian."
        ),
        engineering_application=(
            "Qattiq jism mexanikasida Lagranj, suyuqliklar mexanikasida "
            "Eyler tavsifi; FEM va CFD dasturlarining asosi."
        ),
        computational_component=(
            "Berilgan tezlik maydonida zarra traektoriyasini va oqim "
            "chiziqlarini hisoblash."
        ),
        visualization_component=(
            "Traektoriyalar va oqim chiziqlari; ularning statsionar va "
            "nostatsionar oqimda farqi."
        ),
        research_extension=(
            "ALE (Arbitrary Lagrangian–Eulerian) usuli: nima uchun "
            "suyuqlik–konstruksiya o'zaro ta'sirida kerak?"
        ),
        difficulty="murakkab",
        previous_link=(
            "nm-06 dagi nisbiy va absolyut harakat g'oyasi bu yerda "
            "kontinuumga umumlashtiriladi: endi cheksiz ko'p moddiy nuqta bor."
        ),
        next_topic="tmm-04",
        estimated_minutes=85,
        tags=["Lagranj", "Eyler", "moddiy hosila"],
        lesson=Lesson(
            physical_problem=(
                "Daryodagi suv oqimini qanday tavsiflash kerak? Ikki yo'l bor: "
                "(a) bir tomchini kuzatib borish — u qayerga boradi, tezligi "
                "qanday o'zgaradi; (b) qirg'oqdagi bir nuqtada turib, undan "
                "o'tayotgan suvning tezligini o'lchash. Ikkala tavsif ham "
                "to'g'ri, lekin ular turli tenglamalarga olib keladi."
            ),
            concepts=[
                c("Lagranj tavsifi", "Moddiy nuqtani kuzatib borish: "
                  "$\\mathbf{x} = \\chi(\\mathbf{X}, t)$; $\\mathbf{X}$ — "
                  "boshlang'ich holat (moddiy koordinata)."),
                c("Eyler tavsifi", "Fazodagi qo'zg'almas nuqtada kuzatish: "
                  "$\\mathbf{v} = \\mathbf{v}(\\mathbf{x}, t)$."),
                c("Moddiy (to'la) hosila", "$\\frac{D}{Dt} = \\frac{\\partial}{\\partial t} + "
                  "\\mathbf{v}\\cdot\\nabla$ — moddiy nuqtani kuzatib "
                  "borgandagi o'zgarish tezligi."),
                c("Konvektiv had", "$\\mathbf{v}\\cdot\\nabla$ — nuqta boshqa "
                  "joyga ko'chgani uchun o'zgarish; nochiziqlilikning manbai."),
                c("Traektoriya va oqim chizig'i", "Birinchisi — bitta zarra "
                  "yo'li, ikkinchisi — berilgan onda tezlikka urinma chiziq; "
                  "statsionar oqimda ular ustma-ust tushadi."),
            ],
            derivation=[
                d("1-qadam. Harakat funksiyasi",
                  r"\mathbf{x} = \chi(\mathbf{X}, t),\qquad \mathbf{X} = \chi(\mathbf{X}, 0)",
                  "Har bir moddiy nuqta o'z 'nomi' $\\mathbf{X}$ ga ega va "
                  "vaqt o'tishi bilan $\\mathbf{x}$ holatga ko'chadi."),
                d("2-qadam. Tezlik ikki tavsifda",
                  r"\mathbf{v}(\mathbf{X},t) = \frac{\partial\chi}{\partial t}\bigg|_{\mathbf{X}} "
                  r"\quad\text{(Lagranj)};\qquad \mathbf{v} = \mathbf{v}(\mathbf{x},t)\quad\text{(Eyler)}",
                  "Lagranjda $\\mathbf{X}$ qotirilgan, Eylerda $\\mathbf{x}$."),
                d("3-qadam. Moddiy hosila",
                  r"\frac{Df}{Dt} = \frac{\partial f}{\partial t} + "
                  r"\frac{\partial f}{\partial x_i}\frac{dx_i}{dt} = "
                  r"\boxed{\;\frac{\partial f}{\partial t} + v_i\frac{\partial f}{\partial x_i}\;}",
                  "Zanjir qoidasi. Birinchi had — lokal o'zgarish, ikkinchisi — "
                  "konvektiv (ko'chish tufayli)."),
                d("4-qadam. Tezlanish Eyler tavsifida",
                  r"\mathbf{a} = \frac{D\mathbf{v}}{Dt} = \frac{\partial\mathbf{v}}{\partial t} + "
                  r"(\mathbf{v}\cdot\nabla)\mathbf{v}",
                  "Ikkinchi had kvadratik — bu Navye–Stoks tenglamalarining "
                  "nochiziqliligi va turbulentlikning matematik manbai (tmm-30)."),
            ],
            formula_meaning=(
                "Moddiy hosiladagi konvektiv had barcha qiyinchiliklarning "
                "manbai: u nochiziqli va aynan u turbulentlikni keltirib "
                "chiqaradi. Fizik ma'nosi oddiy: statsionar oqimda ham "
                "($\\partial\\mathbf{v}/\\partial t = 0$) zarra tezlanishi "
                "mumkin, chunki u tezligi boshqa bo'lgan joyga ko'chadi — "
                "masalan, torayuvchi quvurda."
            ),
            equations=[
                eq(r"\frac{Df}{Dt} = \frac{\partial f}{\partial t} + v_i\frac{\partial f}{\partial x_i}",
                   "Moddiy (to'la) hosila.", "Moddiy hosila"),
                eq(r"\mathbf{a} = \frac{\partial\mathbf{v}}{\partial t} + (\mathbf{v}\cdot\nabla)\mathbf{v}",
                   "Eyler tavsifida tezlanish.", "Tezlanish"),
                eq(r"J = \det\left(\frac{\partial x_i}{\partial X_j}\right) > 0",
                   "Yakobian — hajm o'zgarishi va harakatning fizik "
                   "mumkinligi sharti.", "Yakobian"),
            ],
            conditions=(
                "Harakat funksiyasi uzluksiz, differensiallanuvchi va "
                "o'zaro bir qiymatli bo'lishi kerak ($J > 0$) — bu modda "
                "o'z-o'ziga kirib ketmasligini bildiradi. Qattiq jism "
                "mexanikasida Lagranj tavsifi tabiiy (deformatsiya "
                "boshlang'ich holatdan o'lchanadi), suyuqliklarda esa Eyler "
                "(zarralarni kuzatish amaliy emas)."
            ),
            worked_example=WorkedExample(
                statement=(
                    "Statsionar oqim tezlik maydoni: $v_x = k x$, "
                    "$v_y = -k y$ ($k = 2$ 1/s) — bu to'siqqa urilayotgan "
                    "oqim modeli. (a) Zarra traektoriyasini toping; "
                    "(b) $(1; 1)$ nuqtadagi tezlanishni hisoblang; "
                    "(c) nima uchun statsionar oqimda tezlanish nolga teng emas?"
                ),
                given=[r"v_x = kx,\; v_y = -ky,\; k = 2\ \text{s}^{-1}",
                       r"\text{boshlang'ich: } (x_0, y_0) = (0{,}5;\ 2)"],
                steps=[
                    st(r"\frac{dx}{dt} = kx \Rightarrow x = x_0e^{kt};\qquad "
                       r"\frac{dy}{dt} = -ky \Rightarrow y = y_0e^{-kt}",
                       "Lagranj tavsifi: traektoriya tenglamalari."),
                    st(r"xy = x_0y_0 = \text{const} \Rightarrow \text{giperbola}",
                       "Vaqtni yo'qotib, traektoriya shaklini olamiz."),
                    st(r"a_x = \frac{\partial v_x}{\partial t} + v_x\frac{\partial v_x}{\partial x} + "
                       r"v_y\frac{\partial v_x}{\partial y} = 0 + (kx)(k) + 0 = k^2x",
                       "Moddiy hosila: lokal had nol (statsionar), konvektiv "
                       "had qoladi."),
                    st(r"a_y = 0 + 0 + (-ky)(-k) = k^2y",
                       "Xuddi shunday."),
                    st(r"(1;1)\ \text{da}: a_x = 4\cdot1 = 4;\quad a_y = 4\ \text{m/s}^2",
                       "Tezlanish vektori $(4; 4)$ m/s², moduli 5,66 m/s²."),
                    st(r"\text{Sabab: } \partial\mathbf{v}/\partial t = 0,\ \text{lekin } "
                       r"(\mathbf{v}\cdot\nabla)\mathbf{v} \neq 0",
                       "Zarra tezroq oqim sohasiga ko'chadi — bu konvektiv "
                       "tezlanish."),
                ],
                answer=(
                    "Traektoriya — giperbola $xy = \\text{const}$; "
                    "$\\mathbf{a}(1;1) = (4; 4)$ m/s²; tezlanish konvektiv "
                    "haddan kelib chiqadi."
                ),
                engineering_note=(
                    "Bu — quvur toraygan joyda bosim tushishining sababi "
                    "(Bernulli tenglamasi, tmm-26). Suyuqlik tezlashadi, "
                    "demak unga kuch kerak, demak bosim farqi paydo bo'ladi. "
                    "Statsionar oqimda ham tezlanish mavjudligi — "
                    "gidrodinamikaning eng muhim va eng ko'p chalkashtiriladigan "
                    "nuqtasi."
                ),
            ),
            computation=Computation(
                caption=(
                    "Lagranj va Eyler tavsiflari: traektoriyalar, oqim "
                    "chiziqlari va konvektiv tezlanish."
                ),
                code='''"""Deformatsiya kinematikasi: Lagranj va Eyler tavsiflari."""
import numpy as np
from scipy.integrate import solve_ivp
from labkit import PARAMS, note, series, table, value

k = float(PARAMS.get("k", 2.0))          # oqim intensivligi, 1/s
x0 = float(PARAMS.get("x0", 0.5))        # boshlang'ich holat
y0 = float(PARAMS.get("y0", 2.0))
t_end = float(PARAMS.get("t_end", 1.0))  # kuzatish vaqti, s
unsteady = float(PARAMS.get("unsteady", 0.0))   # nostatsionarlik amplitudasi

def velocity(t, pos):
    x, y = pos
    amp = 1.0 + unsteady*np.sin(2*np.pi*t)
    return [k*x*amp, -k*y*amp]

# Lagranj: traektoriya
sol = solve_ivp(velocity, (0, t_end), [x0, y0], rtol=1e-10, dense_output=True, max_step=0.001)
tt = np.linspace(0, t_end, 400)
X, Y = sol.sol(tt)
series("Zarra traektoriyasi", X.tolist(), Y.tolist(), xlabel="x, m", ylabel="y, m")
series("x(t)", tt.tolist(), X.tolist(), xlabel="t, s", ylabel="x, m")
series("y(t)", tt.tolist(), Y.tolist(), xlabel="t, s", ylabel="y, m")

value("Yakuniy x", float(X[-1]), "m")
value("Yakuniy y", float(Y[-1]), "m")
value("xy ko'paytma (boshda)", x0*y0, "m²")
value("xy ko'paytma (oxirda)", float(X[-1]*Y[-1]), "m²")
if unsteady == 0:
    note("Statsionar oqimda xy = const — traektoriya giperbola ✓")

# Eyler: tezlanish maydoni (moddiy hosila)
def acceleration(x, y):
    """a = (v·∇)v statsionar holda."""
    return k**2*x, k**2*y

xp, yp = 1.0, 1.0
ax, ay = acceleration(xp, yp)
value(f"a_x ({xp}, {yp})", ax, "m/s²")
value(f"a_y ({xp}, {yp})", ay, "m/s²")
value("Tezlanish moduli", float(np.hypot(ax, ay)), "m/s²")
note("Statsionar oqimda ∂v/∂t = 0, lekin konvektiv had (v·∇)v ≠ 0 — "
     "shuning uchun tezlanish mavjud.")

# Oqim chiziqlari (statsionar holda traektoriya bilan ustma-ust tushadi)
for c_val in (0.25, 0.5, 1.0, 2.0):
    xs = np.linspace(0.1, 4.0, 100)
    series(f"Oqim chizig'i xy={c_val}", xs.tolist(), (c_val/xs).tolist(),
           xlabel="x, m", ylabel="y, m")

# Tezlik va tezlanish maydonlari (to'r nuqtalarida)
grid = np.linspace(0.2, 2.0, 5)
rows = []
for xg in grid:
    for yg in grid[:3]:
        vx, vy = k*xg, -k*yg
        agx, agy = acceleration(xg, yg)
        rows.append([float(xg), float(yg), float(vx), float(vy),
                     float(np.hypot(agx, agy))])
table("Tezlik va tezlanish maydoni",
      ["x, m", "y, m", "v_x, m/s", "v_y, m/s", "|a|, m/s²"], rows[:10])

# Yakobian: hajm o'zgarishi
J = np.exp(k*tt)*np.exp(-k*tt)
note(f"Yakobian J = det(∂x/∂X) = {J[0]:.6f} (o'zgarmas) — "
     "bu oqim siqilmaydigan (hajm saqlanadi).")

# Moddiy hosilani sonli tekshirish
def f_field(x, y):
    """Skalyar maydon: temperatura T = x² + y²."""
    return x**2 + y**2

T_along = f_field(X, Y)
DT_Dt_num = np.gradient(T_along, tt)
DT_Dt_analytic = 2*X*(k*X) + 2*Y*(-k*Y)
note(f"Moddiy hosila tekshiruvi: maksimal farq "
     f"{np.max(np.abs(DT_Dt_num - DT_Dt_analytic)):.2e}")
series("Zarra bo'ylab T(t)", tt.tolist(), T_along.tolist(), xlabel="t, s", ylabel="T")

table("Ikki tavsifni taqqoslash",
      ["Xususiyat", "Lagranj", "Eyler"],
      [["O'zgaruvchi", "X (moddiy)", "x (fazoviy)"],
       ["Kuzatish", "Zarrani kuzatib borish", "Qo'zg'almas nuqtada"],
       ["Qo'llanilishi", "Qattiq jism, FEM", "Suyuqlik, CFD"],
       ["Tezlanish", "∂v/∂t|_X", "∂v/∂t + (v·∇)v"],
       ["Afzalligi", "Deformatsiya tabiiy", "Chegara qo'zg'almas"]])
''',
                parameters=[
                    p("k", "Oqim intensivligi k", 0.1, 10.0, 2.0, 0.1, "1/s"),
                    p("x0", "Boshlang'ich x₀", 0.05, 4.0, 0.5, 0.05, "m"),
                    p("y0", "Boshlang'ich y₀", 0.05, 4.0, 2.0, 0.05, "m"),
                    p("t_end", "Kuzatish vaqti", 0.1, 3.0, 1.0, 0.1, "s"),
                    p("unsteady", "Nostatsionarlik", 0.0, 1.0, 0.0, 0.1, "—"),
                ],
                expected_output="Traektoriya giperbola (xy = 1), a(1,1) = (4; 4) m/s²",
            ),
            visualization=vis(
                "Traektoriyalar va oqim chiziqlari",
                "React/SVG",
                "Tezlik maydoni strelkalar bilan; bir nechta oqim chizig'i "
                "(giperbolalar); harakatlanuvchi zarra va uning izi. "
                "Nostatsionar holatda traektoriya oqim chizig'idan ajraladi.",
                "React/SVG: tezlik maydonini to'r nuqtalarida strelkalar "
                "bilan chizish (quiver plot). Statsionar va nostatsionar "
                "holatlarni almashtirish orqali traektoriya va oqim "
                "chizig'ining farqini ko'rsatish — bu mavzuning kaliti.",
            ),
            interpretation=(
                "Statsionar oqimda $xy = \\text{const}$ saqlanadi va "
                "traektoriya aynan oqim chizig'i bilan ustma-ust tushadi. "
                "Nostatsionarlik qo'shilganda ular ajraladi. Moddiy hosilani "
                "sonli tekshirish esa $D/Dt$ formulasining to'g'riligini "
                "tasdiqlaydi. Yakobianning o'zgarmasligi oqimning "
                "siqilmaydigan ekanini bildiradi — bu tmm-09 da uzluksizlik "
                "tenglamasiga olib boradi."
            ),
            common_mistakes=[
                "Statsionar oqimda tezlanish nolga teng deb o'ylash.",
                "Traektoriya va oqim chizig'ini har doim bir xil deb "
                "hisoblash — bu faqat statsionar oqimda to'g'ri.",
                "Moddiy hosilada konvektiv hadni unutish.",
                "Lagranj va Eyler o'zgaruvchilarini aralashtirish.",
            ],
            quiz=[
                q("Nima uchun statsionar oqimda ham tezlanish bo'lishi mumkin?",
                  "Zarra tezligi boshqa bo'lgan joyga ko'chadi — konvektiv "
                  "tezlanish $(\\mathbf{v}\\cdot\\nabla)\\mathbf{v} \\neq 0$.",
                  "konseptual"),
                q("Qattiq jism mexanikasida qaysi tavsif qulay va nega?",
                  "Lagranj — deformatsiya boshlang'ich holatdan o'lchanadi va "
                  "har bir moddiy nuqtani kuzatish tabiiy.", "konseptual"),
                q("$v_x = 3x$, $v_y = 0$. $x = 2$ da $a_x$?",
                  "$a_x = v_x\\partial v_x/\\partial x = 3x\\cdot3 = 9x = 18$ m/s².",
                  "hisob"),
                q("Yakobian $J < 0$ bo'lsa nima demak?",
                  "Harakat fizik jihatdan mumkin emas — modda o'z-o'ziga kirib "
                  "ketadi yoki aks etadi.", "talqin"),
                q("Kodda moddiy hosila qanday tekshirilgan?",
                  "Zarra traektoriyasi bo'ylab $T(t)$ ni sonli "
                  "differensiallash va uni analitik formula "
                  "$\\partial T/\\partial t + v\\cdot\\nabla T$ bilan "
                  "taqqoslash orqali.", "kod"),
            ],
            bridge_to_next=(
                "Harakatni tavsifladik. Endi deformatsiyani miqdoriy "
                "o'lchaydigan asosiy obyektga — deformatsiya gradiyentiga "
                "o'tamiz."
            ),
            research_extension=(
                "ALE (Arbitrary Lagrangian–Eulerian) formulirovkasini "
                "o'rganing: to'r suyuqlik bilan ham, konstruksiya bilan ham "
                "harakatlanmaydi, balki alohida qonun bo'yicha siljiydi. "
                "Bu suyuqlik–konstruksiya o'zaro ta'siri (FSI) masalalarida "
                "qanday muammoni hal qiladi? Sodda 1D misolda amalga oshiring."
            ),
        ),
    ),
    Topic(
        id="tmm-04",
        subject_id=S,
        module_id=M,
        order=4,
        title="Deformatsiya gradiyenti va polar dekompozitsiya",
        description=(
            "Deformatsiya gradiyenti tenzori, cho'zilish va burilishga "
            "ajratish, Koshi–Grin tenzorlari."
        ),
        learning_objective=(
            "Deformatsiya gradiyentini hisoblash va uni sof cho'zilish hamda "
            "qattiq burilish qismlariga ajratish."
        ),
        prerequisites=["tmm-03"],
        mathematical_core=(
            "$F_{iJ} = \\partial x_i/\\partial X_J$, polar dekompozitsiya "
            "$F = RU = VR$, Koshi–Grin tenzorlari $C = F^TF$."
        ),
        engineering_application=(
            "Katta deformatsiyalar (rezina, metall ishlash), geometrik "
            "nochiziqli FEM, biomexanika."
        ),
        computational_component=(
            "Deformatsiya gradiyentini hisoblash va SVD orqali polar "
            "dekompozitsiyani bajarish."
        ),
        visualization_component=(
            "Birlik kvadratning deformatsiyasi: cho'zilish + burilish "
            "ajratilishi."
        ),
        research_extension=(
            "Nima uchun katta deformatsiyalarda chiziqli deformatsiya "
            "tenzori xato beradi? Qattiq burilish testi."
        ),
        difficulty="murakkab",
        previous_link=(
            "tmm-03 dagi harakat funksiyasi $\\chi(\\mathbf{X},t)$ ning "
            "gradiyenti aynan deformatsiya haqidagi butun ma'lumotni saqlaydi."
        ),
        next_topic="tmm-05",
        estimated_minutes=90,
        tags=["deformatsiya gradiyenti", "polar dekompozitsiya", "katta deformatsiya"],
        lesson=Lesson(
            physical_problem=(
                "Jismni $90°$ ga bursak, u deformatsiyalanmaydi — lekin "
                "ko'chishlar katta. Chiziqli deformatsiya tenzori bu holatda "
                "nolga teng bo'lmagan 'soxta deformatsiya' beradi. Demak "
                "katta ko'chishlarda deformatsiyani burilishdan ajratish "
                "kerak. Buni qanday qilish mumkin?"
            ),
            concepts=[
                c("Deformatsiya gradiyenti", "$F_{iJ} = \\partial x_i/\\partial X_J$ — "
                  "boshlang'ich va joriy holatlarni bog'lovchi tenzor; "
                  "$d\\mathbf{x} = F\\,d\\mathbf{X}$."),
                c("Polar dekompozitsiya", "$F = RU = VR$; $R$ — ortogonal "
                  "(burilish), $U$, $V$ — simmetrik musbat aniqlangan "
                  "(cho'zilish)."),
                c("O'ng Koshi–Grin tenzori", "$C = F^TF = U^2$ — burilishdan "
                  "mustaqil deformatsiya o'lchovi."),
                c("Grin–Lagranj deformatsiya tenzori", "$E = \\frac{1}{2}(C - I)$ — "
                  "qattiq burilishda aynan nolga teng."),
                c("Cho'zilish darajalari", "$U$ ning xususiy qiymatlari — "
                  "bosh cho'zilishlar $\\lambda_i$."),
            ],
            derivation=[
                d("1-qadam. Deformatsiya gradiyentini kiritish",
                  r"dx_i = \frac{\partial x_i}{\partial X_J}dX_J = F_{iJ}dX_J",
                  "Boshlang'ich holatdagi cheksiz kichik vektor joriy "
                  "holatga chiziqli akslantiriladi."),
                d("2-qadam. Uzunlik o'zgarishi",
                  r"ds^2 = dx_idx_i = F_{iJ}F_{iK}dX_JdX_K = C_{JK}dX_JdX_K,\quad C = F^TF",
                  "$C$ — o'ng Koshi–Grin tenzori. U burilishdan mustaqil, "
                  "chunki $R^TR = I$."),
                d("3-qadam. Grin–Lagranj deformatsiya tenzori",
                  r"ds^2 - dS^2 = (C_{JK}-\delta_{JK})dX_JdX_K = 2E_{JK}dX_JdX_K "
                  r"\;\Rightarrow\; \boxed{\;E = \tfrac{1}{2}(F^TF - I)\;}",
                  "Uzunlik kvadratlari farqi. Qattiq burilishda $F = R$, "
                  "$F^TF = I$, demak $E = 0$ — aynan kerakli xossa."),
                d("4-qadam. Polar dekompozitsiya",
                  r"F = RU: \quad U = \sqrt{C},\quad R = FU^{-1}",
                  "Har qanday aynimagan $F$ yagona usulda burilish va "
                  "cho'zilishga ajraladi. Amalda SVD orqali hisoblanadi: "
                  "$F = W\\Sigma V^T \\Rightarrow R = WV^T$, $U = V\\Sigma V^T$."),
                d("5-qadam. Kichik deformatsiyalarga o'tish",
                  r"F = I + \nabla\mathbf{u} \Rightarrow E = \tfrac{1}{2}(\nabla\mathbf{u} + "
                  r"\nabla\mathbf{u}^T + \nabla\mathbf{u}^T\nabla\mathbf{u}) \approx \varepsilon",
                  "Kvadratik hadni tashlasak, chiziqli deformatsiya tenzori "
                  "qoladi (tmm-05). Bu faqat $|\\nabla\\mathbf{u}| \\ll 1$ da o'rinli."),
            ],
            formula_meaning=(
                "Polar dekompozitsiya deformatsiyaning fizik mohiyatini "
                "ochadi: har qanday deformatsiya — bu avval sof cho'zilish, "
                "keyin qattiq burilish (yoki teskari tartibda). Grin–Lagranj "
                "tenzori esa burilishga 'ko'r' — u faqat haqiqiy "
                "deformatsiyani o'lchaydi. Aynan shuning uchun katta "
                "ko'chishli masalalarda (rezina, metall shtamplash, "
                "biologik to'qimalar) u ishlatiladi."
            ),
            equations=[
                eq(r"F_{iJ} = \frac{\partial x_i}{\partial X_J}", "Deformatsiya gradiyenti.",
                   "Deformatsiya gradiyenti"),
                eq(r"E = \tfrac{1}{2}(F^TF - I)", "Grin–Lagranj deformatsiya tenzori.",
                   "Grin–Lagranj"),
                eq(r"F = RU = VR", "Polar dekompozitsiya.", "Polar dekompozitsiya"),
            ],
            conditions=(
                "$\\det F > 0$ — modda o'z-o'ziga kirib ketmasligi sharti. "
                "$\\det F = 1$ — siqilmaydigan deformatsiya (rezina, plastik "
                "oqish). Kichik deformatsiyalar nazariyasi "
                "$|\\nabla\\mathbf{u}| < 0{,}01$ da 1 % xatolik beradi, "
                "$0{,}1$ da esa 10 % gacha."
            ),
            worked_example=WorkedExample(
                statement=(
                    "Tekis deformatsiya: $x_1 = 1{,}2X_1 + 0{,}3X_2$, "
                    "$x_2 = 0{,}9X_2$, $x_3 = X_3$. (a) $F$ ni yozing; "
                    "(b) $\\det F$ va hajm o'zgarishini toping; (c) $E$ ni "
                    "hisoblang; (d) polar dekompozitsiya orqali burilish "
                    "burchagini aniqlang."
                ),
                given=[r"x_1 = 1{,}2X_1+0{,}3X_2,\; x_2 = 0{,}9X_2,\; x_3 = X_3"],
                steps=[
                    st(r"F = \begin{pmatrix}1{,}2 & 0{,}3 & 0\\ 0 & 0{,}9 & 0\\ 0&0&1\end{pmatrix}",
                       "Qisman hosilalar matritsasi."),
                    st(r"\det F = 1{,}2\cdot0{,}9\cdot1 = 1{,}08",
                       "Hajm 8 % ga ortgan."),
                    st(r"C = F^TF = \begin{pmatrix}1{,}44 & 0{,}36 & 0\\ "
                       r"0{,}36 & 0{,}90 & 0\\ 0&0&1\end{pmatrix}",
                       "$C_{11} = 1{,}2^2 = 1{,}44$; $C_{12} = 1{,}2\\cdot0{,}3 = 0{,}36$; "
                       "$C_{22} = 0{,}3^2+0{,}9^2 = 0{,}90$."),
                    st(r"E = \tfrac{1}{2}(C-I) = \begin{pmatrix}0{,}220 & 0{,}180 & 0\\ "
                       r"0{,}180 & -0{,}050 & 0\\ 0&0&0\end{pmatrix}",
                       "Grin–Lagranj deformatsiya tenzori."),
                    st(r"\text{Chiziqli tenzor: } \varepsilon_{11} = 0{,}2;\ \varepsilon_{22} = -0{,}1;\ "
                       r"\varepsilon_{12} = 0{,}15",
                       "Taqqoslash: $E_{11} = 0{,}22$ va $\\varepsilon_{11} = 0{,}20$ — "
                       "10 % farq, chunki deformatsiya katta."),
                    st(r"\text{SVD: } R \approx \begin{pmatrix}0{,}993 & 0{,}122\\ "
                       r"-0{,}122 & 0{,}993\end{pmatrix} \Rightarrow \theta \approx -7{,}0^\circ",
                       "Polar dekompozitsiya burilish burchagini beradi."),
                ],
                answer=(
                    "$\\det F = 1{,}08$ (hajm +8 %); $E_{11} = 0{,}22$, "
                    "$E_{22} = -0{,}05$, $E_{12} = 0{,}18$; burilish "
                    "$\\theta \\approx -7{,}0°$."
                ),
                engineering_note=(
                    "Chiziqli va Grin–Lagranj tenzorlari 10 % farq qildi — "
                    "bu 20 % deformatsiyada kutilgan natija. Metall "
                    "shtamplashda deformatsiya 50–100 % ga yetadi va u yerda "
                    "chiziqli nazariya umuman ishlamaydi. Rezina va biologik "
                    "to'qimalarda ham shunday."
                ),
            ),
            computation=Computation(
                caption=(
                    "Deformatsiya gradiyenti: polar dekompozitsiya va "
                    "chiziqli nazariya bilan taqqoslash."
                ),
                code='''"""Deformatsiya gradiyenti va polar dekompozitsiya."""
import numpy as np
from labkit import PARAMS, note, series, table, value

F11 = float(PARAMS.get("F11", 1.2))
F12 = float(PARAMS.get("F12", 0.3))
F21 = float(PARAMS.get("F21", 0.0))
F22 = float(PARAMS.get("F22", 0.9))

F = np.array([[F11, F12, 0.0], [F21, F22, 0.0], [0.0, 0.0, 1.0]])
J = np.linalg.det(F)
value("det F (hajm nisbati)", J, "—")
value("Hajm o'zgarishi", (J-1)*100, "%")
note("DIQQAT: det F ≤ 0 — fizik jihatdan mumkin emas!" if J <= 0 else
     "det F > 0 ✓ (harakat fizik jihatdan mumkin)")

C = F.T @ F
E_gl = 0.5*(C - np.eye(3))
grad_u = F - np.eye(3)
eps_lin = 0.5*(grad_u + grad_u.T)

table("Deformatsiya tenzorlarini taqqoslash",
      ["Komponenta", "Grin–Lagranj E", "Chiziqli ε", "Farq, %"],
      [[f"{i+1}{j+1}", float(E_gl[i, j]), float(eps_lin[i, j]),
        float(abs(E_gl[i, j]-eps_lin[i, j])/max(abs(E_gl[i, j]), 1e-12)*100)]
       for i in range(2) for j in range(2)])

# Polar dekompozitsiya (SVD orqali)
W, S, Vt = np.linalg.svd(F)
R = W @ Vt
U = Vt.T @ np.diag(S) @ Vt
V = W @ np.diag(S) @ W.T
theta = np.degrees(np.arctan2(R[1, 0], R[0, 0]))

value("Burilish burchagi θ", theta, "deg")
value("Bosh cho'zilish λ₁", float(S[0]), "—")
value("Bosh cho'zilish λ₂", float(S[1]), "—")
note(f"Tekshirish: ||F - RU|| = {np.linalg.norm(F - R @ U):.2e} ✓")
note(f"R ortogonalligi: ||RᵀR - I|| = {np.linalg.norm(R.T @ R - np.eye(3)):.2e} ✓")

# Birlik kvadratning deformatsiyasi
square = np.array([[0, 0], [1, 0], [1, 1], [0, 1], [0, 0]], dtype=float)
deformed = (F[:2, :2] @ square.T).T
rotated_only = (R[:2, :2] @ square.T).T
stretched_only = (U[:2, :2] @ square.T).T

series("Boshlang'ich kvadrat", square[:, 0].tolist(), square[:, 1].tolist(),
       xlabel="x", ylabel="y")
series("Deformatsiyalangan (F)", deformed[:, 0].tolist(), deformed[:, 1].tolist(),
       xlabel="x", ylabel="y")
series("Faqat cho'zilish (U)", stretched_only[:, 0].tolist(), stretched_only[:, 1].tolist(),
       xlabel="x", ylabel="y")
series("Faqat burilish (R)", rotated_only[:, 0].tolist(), rotated_only[:, 1].tolist(),
       xlabel="x", ylabel="y")

# Qattiq burilish testi: chiziqli tenzor xato beradi
for ang in (5, 15, 30, 45, 90):
    t = np.radians(ang)
    R_test = np.array([[np.cos(t), -np.sin(t), 0], [np.sin(t), np.cos(t), 0], [0, 0, 1]])
    E_test = 0.5*(R_test.T @ R_test - np.eye(3))
    gu = R_test - np.eye(3)
    eps_test = 0.5*(gu + gu.T)
    note(f"{ang}° qattiq burilish: ||E_GL|| = {np.linalg.norm(E_test):.2e} (nol ✓), "
         f"||ε_chiziqli|| = {np.linalg.norm(eps_test):.4f} (SOXTA deformatsiya!)")

# Deformatsiya darajasining xatolikka ta'siri
lams = np.linspace(1.0, 1.5, 100)
err = [abs(0.5*(l**2-1) - (l-1))/max(0.5*(l**2-1), 1e-12)*100 for l in lams]
series("Chiziqli nazariya xatoligi", ((lams-1)*100).tolist(), err,
       xlabel="Deformatsiya, %", ylabel="Xatolik, %")
note("Deformatsiya 5 % da xatolik ~2,5 %, 20 % da ~10 %, 50 % da ~25 % — "
     "shuning uchun katta deformatsiyalarda chiziqli nazariya yaroqsiz.")
''',
                parameters=[
                    p("F11", "F₁₁", 0.3, 3.0, 1.2, 0.05, "—"),
                    p("F12", "F₁₂", -1.0, 1.0, 0.3, 0.05, "—"),
                    p("F21", "F₂₁", -1.0, 1.0, 0.0, 0.05, "—"),
                    p("F22", "F₂₂", 0.3, 3.0, 0.9, 0.05, "—"),
                ],
                expected_output="det F = 1,08; E₁₁ = 0,22; θ ≈ -7,0°; qattiq burilishda E = 0",
            ),
            visualization=vis(
                "Deformatsiyaning cho'zilish va burilishga ajralishi",
                "Manim",
                "Birlik kvadrat: avval cho'ziladi (ellipsga aylanadi), "
                "so'ngra buriladi. Yakuniy shakl $F$ ta'sirida hosil "
                "bo'lgan shakl bilan ustma-ust tushadi.",
                "Manim: polar dekompozitsiyaning ikki bosqichli animatsiyasi "
                "($U$ keyin $R$) — bu tushunchani tasvirlashning eng aniq "
                "usuli. React/SVG da to'rt shaklni yonma-yon ko'rsatish "
                "yetarli.",
            ),
            interpretation=(
                "Qattiq burilish testi hal qiluvchi natija beradi: $90°$ "
                "burilishda Grin–Lagranj tenzori aynan nolga teng, chiziqli "
                "tenzor esa katta 'soxta deformatsiya' ko'rsatadi. Xatolik "
                "grafigi esa chegarani aniq beradi: 5 % deformatsiyada 2,5 % "
                "xatolik qabul qilinadi, 20 % da esa 10 % — bu ko'p hollarda "
                "yaroqsiz."
            ),
            common_mistakes=[
                "Katta ko'chishlarda chiziqli deformatsiya tenzorini "
                "ishlatish.",
                "$\\det F < 0$ holatni tekshirmaslik.",
                "$C = F^TF$ va $B = FF^T$ ni chalkashtirish (o'ng va chap "
                "Koshi–Grin tenzorlari).",
                "Polar dekompozitsiyada $R$ va $U$ tartibini almashtirish "
                "($F = RU \\neq UR$).",
            ],
            quiz=[
                q("Nima uchun Grin–Lagranj tenzori qattiq burilishda nolga teng?",
                  "$F = R$ bo'lsa $F^TF = R^TR = I$, demak "
                  "$E = \\frac{1}{2}(I-I) = 0$.", "konseptual"),
                q("$\\det F = 1$ nimani anglatadi?",
                  "Hajm o'zgarmaydi — siqilmaydigan deformatsiya (rezina, "
                  "plastik oqish).", "konseptual"),
                q("$F = \\text{diag}(1{,}5;\\ 1;\\ 1)$. $E_{11}$ ni toping.",
                  "$E_{11} = (1{,}5^2-1)/2 = 0{,}625$; chiziqli nazariyada "
                  "0,5 — 25 % farq.", "hisob"),
                q("Polar dekompozitsiyaning fizik ma'nosi nima?",
                  "Har qanday deformatsiya sof cho'zilish va qattiq "
                  "burilishning ketma-ketligi sifatida ifodalanadi.",
                  "talqin"),
                q("Kodda SVD nima uchun ishlatilgan?",
                  "$F = W\\Sigma V^T$ dan $R = WV^T$ (burilish) va "
                  "$U = V\\Sigma V^T$ (cho'zilish) to'g'ridan-to'g'ri "
                  "olinadi — bu polar dekompozitsiyaning sonli barqaror "
                  "usuli.", "kod"),
            ],
            bridge_to_next=(
                "Umumiy nazariya qurildi. Endi muhandislik amaliyotidagi "
                "asosiy holga — kichik deformatsiyalarga o'tamiz."
            ),
            research_extension=(
                "Hiperelastik material modelini (neo-Hooke: "
                "$W = \\frac{\\mu}{2}(I_1 - 3)$) amalga oshiring va rezina "
                "namunaning bir o'qli cho'zilishini hisoblang. Natijani "
                "tajriba ma'lumotlari bilan taqqoslang va chiziqli Guk "
                "qonuni qaysi deformatsiyagacha to'g'ri ekanini aniqlang."
            ),
        ),
    ),
    Topic(
        id="tmm-05",
        subject_id=S,
        module_id=M,
        order=5,
        title="Chiziqli deformatsiya tenzori, asosiy deformatsiyalar va moslik shartlari",
        description=(
            "Kichik deformatsiyalar nazariyasi, deformatsiya tenzorining "
            "komponentalari va fizik ma'nosi, Sen-Venan moslik shartlari."
        ),
        learning_objective=(
            "Ko'chish maydonidan deformatsiya tenzorini hisoblash, asosiy "
            "deformatsiyalarni topish va moslik shartlarini tekshirish."
        ),
        prerequisites=["tmm-04", "mq-20"],
        mathematical_core=(
            "$\\varepsilon_{ij} = \\frac{1}{2}(u_{i,j}+u_{j,i})$, xususiy "
            "qiymatlar, moslik shartlari (ikkinchi tartibli PDE)."
        ),
        engineering_application=(
            "Tenzometriya, FEM natijalarini talqin qilish, deformatsiya "
            "maydonini o'lchash (DIC)."
        ),
        computational_component=(
            "Ko'chish maydonidan deformatsiyani sonli hisoblash va moslik "
            "shartlarini tekshirish."
        ),
        visualization_component=(
            "Deformatsiya maydoni rangli xarita; bosh deformatsiya "
            "yo'nalishlari."
        ),
        research_extension=(
            "Raqamli tasvir korrelyatsiyasi (DIC) usuli: tajribada "
            "deformatsiya maydonini qanday o'lchash mumkin?"
        ),
        difficulty="asosiy",
        previous_link=(
            "tmm-04 dagi Grin–Lagranj tenzorining kvadratik hadini tashlab, "
            "muhandislik amaliyotining asosiy vositasini olamiz."
        ),
        next_topic="tmm-06",
        estimated_minutes=85,
        tags=["deformatsiya tenzori", "moslik sharti", "tenzometriya"],
        lesson=Lesson(
            physical_problem=(
                "Tenzodatchiklar bilan detal sirtida uchta yo'nalishda "
                "deformatsiya o'lchandi. Undan to'liq deformatsiya holatini "
                "va kuchlanishlarni qanday tiklash mumkin? Va teskari savol: "
                "ixtiyoriy uchta funksiya deformatsiya maydoni bo'la oladimi? "
                "Yo'q — ular moslik shartlarini qanoatlantirishi kerak."
            ),
            concepts=[
                c("Chiziqli deformatsiya tenzori", "$\\varepsilon_{ij} = "
                  "\\frac{1}{2}(\\partial u_i/\\partial x_j + \\partial u_j/\\partial x_i)$."),
                c("Diagonal komponentalar", "$\\varepsilon_{11}$ — $x$ "
                  "yo'nalishidagi nisbiy uzayish."),
                c("Diagonaldan tashqaridagilar", "$\\gamma_{12} = 2\\varepsilon_{12}$ — "
                  "to'g'ri burchakning o'zgarishi (muhandislik siljish "
                  "deformatsiyasi)."),
                c("Burilish tenzori", "$\\omega_{ij} = \\frac{1}{2}(u_{i,j}-u_{j,i})$ — "
                  "antisimmetrik qism, qattiq burilishni tavsiflaydi."),
                c("Moslik shartlari", "Deformatsiya maydonidan uzluksiz "
                  "ko'chish maydonini tiklash imkonini beruvchi shartlar."),
            ],
            derivation=[
                d("1-qadam. Ko'chish gradiyentini ajratish",
                  r"\frac{\partial u_i}{\partial x_j} = \underbrace{\tfrac{1}{2}(u_{i,j}+u_{j,i})}_{\varepsilon_{ij}} + "
                  r"\underbrace{\tfrac{1}{2}(u_{i,j}-u_{j,i})}_{\omega_{ij}}",
                  "Har qanday tenzor simmetrik va antisimmetrik qismlarga "
                  "ajraladi. Simmetrik qism deformatsiya, antisimmetrik — "
                  "qattiq burilish."),
                d("2-qadam. Diagonal komponentaning fizik ma'nosi",
                  r"\varepsilon_{11} = \frac{\partial u_1}{\partial x_1} = "
                  r"\lim\frac{\Delta l - \Delta x}{\Delta x}",
                  "$x$ o'qi bo'ylab kesmaning nisbiy uzayishi."),
                d("3-qadam. Siljish deformatsiyasi",
                  r"\gamma_{12} = 2\varepsilon_{12} = \frac{\partial u_1}{\partial x_2}+\frac{\partial u_2}{\partial x_1}",
                  "Dastlab to'g'ri bo'lgan burchakning kamayishi. "
                  "Koeffitsient 2 — muhandislik va tenzor ta'riflari farqi, "
                  "bu ko'p xatolarning manbai."),
                d("4-qadam. Moslik shartlari (Sen-Venan)",
                  r"\varepsilon_{ij,kl} + \varepsilon_{kl,ij} - \varepsilon_{ik,jl} - \varepsilon_{jl,ik} = 0",
                  "6 ta deformatsiya komponentasi 3 ta ko'chishdan hosil "
                  "bo'ladi — demak ular mustaqil emas. Tekislikda bitta "
                  "shart qoladi: "
                  "$\\varepsilon_{11,22}+\\varepsilon_{22,11} = 2\\varepsilon_{12,12}$."),
            ],
            formula_meaning=(
                "Deformatsiya tenzori ko'chish maydonining 'foydali' qismini "
                "ajratib oladi: qattiq burilish materialda kuchlanish hosil "
                "qilmaydi, faqat deformatsiya qiladi. Moslik shartlari esa "
                "chuqurroq g'oyani ifodalaydi: deformatsiya maydoni ixtiyoriy "
                "bo'la olmaydi, chunki u uzluksiz jismdan kelib chiqishi "
                "kerak. Bu shartlar kuchlanish usulida yechish (tmm-17) uchun "
                "hal qiluvchi."
            ),
            equations=[
                eq(r"\varepsilon_{ij} = \tfrac{1}{2}(u_{i,j}+u_{j,i})",
                   "Chiziqli deformatsiya tenzori.", "Deformatsiya tenzori"),
                eq(r"\gamma_{12} = 2\varepsilon_{12}", "Muhandislik siljish deformatsiyasi.",
                   "Siljish deformatsiyasi"),
                eq(r"\varepsilon_{11,22}+\varepsilon_{22,11} = 2\varepsilon_{12,12}",
                   "Tekis holda moslik sharti.", "Moslik sharti"),
            ],
            conditions=(
                "Chiziqli nazariya $|\\varepsilon| \\ll 1$ va "
                "$|\\omega| \\ll 1$ shartlarida o'rinli. Moslik shartlari "
                "bir bog'lamli sohada yetarli; teshikli (ko'p bog'lamli) "
                "sohada qo'shimcha integral shartlar kerak."
            ),
            worked_example=WorkedExample(
                statement=(
                    "Ko'chish maydoni: $u_1 = a(x_1^2 + x_2^2)$, "
                    "$u_2 = 2ax_1x_2$, $u_3 = 0$, $a = 10^{-4}$ 1/mm. "
                    "(a) Deformatsiya tenzorini toping; (b) $(10; 5)$ mm "
                    "nuqtada asosiy deformatsiyalarni hisoblang; "
                    "(c) moslik shartini tekshiring."
                ),
                given=[r"u_1 = a(x_1^2+x_2^2),\; u_2 = 2ax_1x_2,\; a = 10^{-4}\ \text{mm}^{-1}"],
                steps=[
                    st(r"\varepsilon_{11} = \frac{\partial u_1}{\partial x_1} = 2ax_1;\quad "
                       r"\varepsilon_{22} = \frac{\partial u_2}{\partial x_2} = 2ax_1",
                       "Diagonal komponentalar teng chiqdi."),
                    st(r"\varepsilon_{12} = \tfrac{1}{2}\left(\frac{\partial u_1}{\partial x_2}+"
                       r"\frac{\partial u_2}{\partial x_1}\right) = \tfrac{1}{2}(2ax_2 + 2ax_2) = 2ax_2",
                       "Siljish deformatsiyasi."),
                    st(r"(10;5): \varepsilon_{11} = \varepsilon_{22} = 2\cdot10^{-4}\cdot10 = 2\cdot10^{-3};"
                       r"\quad \varepsilon_{12} = 2\cdot10^{-4}\cdot5 = 10^{-3}",
                       "Sonli qiymatlar."),
                    st(r"\varepsilon_{1,2} = \frac{\varepsilon_{11}+\varepsilon_{22}}{2} \pm "
                       r"\sqrt{\left(\frac{\varepsilon_{11}-\varepsilon_{22}}{2}\right)^2+\varepsilon_{12}^2} = "
                       r"2\cdot10^{-3} \pm 10^{-3}",
                       "Asosiy deformatsiyalar: $3\\cdot10^{-3}$ va $10^{-3}$."),
                    st(r"\tan2\alpha = \frac{2\varepsilon_{12}}{\varepsilon_{11}-\varepsilon_{22}} = "
                       r"\frac{2\cdot10^{-3}}{0} \to \infty \Rightarrow \alpha = 45^\circ",
                       "Asosiy o'qlar $45°$ burchakda."),
                    st(r"\text{Moslik: } \varepsilon_{11,22} = 0;\ \varepsilon_{22,11} = 0;\ "
                       r"2\varepsilon_{12,12} = 2\cdot0 = 0 \Rightarrow 0+0 = 0\ \checkmark",
                       "Shart bajarildi — bu haqiqiy deformatsiya maydoni."),
                ],
                answer=(
                    "$\\varepsilon_{11} = \\varepsilon_{22} = 2ax_1$, "
                    "$\\varepsilon_{12} = 2ax_2$; $(10;5)$ da asosiy "
                    "deformatsiyalar $3\\cdot10^{-3}$ va $10^{-3}$, "
                    "$\\alpha = 45°$; moslik sharti bajarildi."
                ),
                engineering_note=(
                    "Moslik shartining bajarilishi bu maydon haqiqatan "
                    "uzluksiz ko'chishdan kelib chiqqanini tasdiqlaydi. "
                    "FEM da ko'chish usuli ishlatilganda moslik avtomatik "
                    "bajariladi; kuchlanish usulida esa uni alohida "
                    "ta'minlash kerak — bu uning asosiy qiyinchiligi."
                ),
            ),
            computation=Computation(
                caption=(
                    "Deformatsiya maydoni: ko'chishlardan deformatsiyani "
                    "hisoblang va moslik shartini tekshiring."
                ),
                code='''"""Chiziqli deformatsiya tenzori va moslik shartlari."""
import numpy as np
import sympy as sp
from labkit import PARAMS, note, series, table, value

a_coef = float(PARAMS.get("a", 1e-4))     # ko'chish maydoni koeffitsienti, 1/mm
x_p = float(PARAMS.get("x_p", 10.0))      # tekshirish nuqtasi, mm
y_p = float(PARAMS.get("y_p", 5.0))
L_dom = float(PARAMS.get("L", 20.0))      # soha o'lchami, mm

# Simvolik hisob
x1, x2, a = sp.symbols("x1 x2 a")
u1 = a*(x1**2 + x2**2)
u2 = 2*a*x1*x2

e11 = sp.diff(u1, x1)
e22 = sp.diff(u2, x2)
e12 = sp.Rational(1, 2)*(sp.diff(u1, x2) + sp.diff(u2, x1))
w12 = sp.Rational(1, 2)*(sp.diff(u2, x1) - sp.diff(u1, x2))

note(f"ε₁₁ = {e11}, ε₂₂ = {e22}, ε₁₂ = {sp.simplify(e12)}, ω₁₂ = {sp.simplify(w12)}")

subs = {a: a_coef, x1: x_p, x2: y_p}
E11 = float(e11.subs(subs)); E22 = float(e22.subs(subs)); E12 = float(e12.subs(subs))
value("ε₁₁", E11*1e6, "µε")
value("ε₂₂", E22*1e6, "µε")
value("ε₁₂", E12*1e6, "µε")
value("γ₁₂ (muhandislik)", 2*E12*1e6, "µε")
value("Hajmiy deformatsiya e", (E11+E22)*1e6, "µε")

# Asosiy deformatsiyalar
T_eps = np.array([[E11, E12], [E12, E22]])
eig, vecs = np.linalg.eigh(T_eps)
value("ε₁ (asosiy)", float(max(eig))*1e6, "µε")
value("ε₂ (asosiy)", float(min(eig))*1e6, "µε")
alpha = 0.5*np.degrees(np.arctan2(2*E12, E11-E22))
value("Asosiy o'q burchagi", alpha, "deg")
value("γ_max", float(max(eig)-min(eig))*1e6, "µε")

# Moslik sharti (simvolik)
compat = sp.simplify(sp.diff(e11, x2, 2) + sp.diff(e22, x1, 2) - 2*sp.diff(e12, x1, x2))
note(f"Moslik sharti: ε₁₁,₂₂ + ε₂₂,₁₁ - 2ε₁₂,₁₂ = {compat}")
note("Moslik sharti BAJARILDI ✓" if compat == 0 else
     "DIQQAT: moslik sharti buzilgan — bu maydon uzluksiz ko'chishdan kelib chiqmaydi!")

# Buzilgan maydon misoli
e11_bad = a*x2**2
e22_bad = a*x1**2
e12_bad = sp.Integer(0)
compat_bad = sp.simplify(sp.diff(e11_bad, x2, 2) + sp.diff(e22_bad, x1, 2)
                         - 2*sp.diff(e12_bad, x1, x2))
note(f"Buzilgan misol (ε₁₁ = ax₂², ε₂₂ = ax₁², ε₁₂ = 0): shart = {compat_bad} ≠ 0 — "
     "bunday deformatsiya maydoni mavjud emas.")

# Maydon bo'ylab taqsimot
xx = np.linspace(0, L_dom, 100)
series("ε₁₁(x₁) — y=5 mm", xx.tolist(), (2*a_coef*xx*1e6).tolist(),
       xlabel="x₁, mm", ylabel="ε₁₁, µε")
yy = np.linspace(0, L_dom, 100)
series("ε₁₂(x₂) — x=10 mm", yy.tolist(), (2*a_coef*yy*1e6).tolist(),
       xlabel="x₂, mm", ylabel="ε₁₂, µε")

# Tenzorozetka: uchta o'lchovdan deformatsiya holatini tiklash
def rosette(e_0, e_45, e_90):
    """0°/45°/90° rozetkadan ε₁₁, ε₂₂, γ₁₂ ni tiklash."""
    return e_0, e_90, 2*e_45 - e_0 - e_90

e0 = E11
e45 = (E11+E22)/2 + E12
e90 = E22
r11, r22, g12 = rosette(e0, e45, e90)
table("Tenzorozetka bilan tiklash",
      ["Kattalik", "Haqiqiy, µε", "Tiklangan, µε", "Farq"],
      [["ε₁₁", E11*1e6, r11*1e6, abs(E11-r11)*1e6],
       ["ε₂₂", E22*1e6, r22*1e6, abs(E22-r22)*1e6],
       ["γ₁₂", 2*E12*1e6, g12*1e6, abs(2*E12-g12)*1e6]])
note("Uchta o'lchov tekis deformatsiya holatini to'liq aniqlaydi — "
     "bu tenzometriyaning asosi.")

table("Deformatsiya tenzori komponentalarining ma'nosi",
      ["Komponenta", "Fizik ma'no", "Birlik"],
      [["ε₁₁, ε₂₂, ε₃₃", "O'qlar bo'ylab nisbiy uzayish", "—"],
       ["γ₁₂ = 2ε₁₂", "To'g'ri burchakning o'zgarishi", "rad"],
       ["e = ε_kk", "Nisbiy hajm o'zgarishi", "—"],
       ["ω_ij", "Qattiq burilish (deformatsiya emas)", "rad"]])
''',
                parameters=[
                    p("a", "Maydon koeffitsienti a", 1e-6, 1e-3, 1e-4, 1e-5, "1/mm"),
                    p("x_p", "Tekshirish nuqtasi x", 0.0, 50.0, 10.0, 1.0, "mm"),
                    p("y_p", "Tekshirish nuqtasi y", 0.0, 50.0, 5.0, 1.0, "mm"),
                    p("L", "Soha o'lchami", 5.0, 100.0, 20.0, 5.0, "mm"),
                ],
                expected_output="ε₁₁ = 2000 µε, ε₁₂ = 1000 µε, moslik sharti bajarildi",
            ),
            visualization=vis(
                "Deformatsiya maydoni va asosiy yo'nalishlar",
                "React/SVG",
                "Sohada deformatsiya darajasi rangli xarita sifatida; "
                "tanlangan nuqtalarda asosiy deformatsiya yo'nalishlari "
                "kesishgan chiziqlar bilan (krest belgilari).",
                "React/SVG: rangli xarita uchun SVG to'r; asosiy "
                "yo'nalishlarni krestlar bilan ko'rsatish — bu FEM "
                "postprotsessorlarining standart tasviri va u tajriba "
                "(DIC) natijalari bilan bevosita taqqoslanadi.",
            ),
            interpretation=(
                "Moslik sharti tekshiruvi ikki misolda qarama-qarshi natija "
                "beradi: birinchi maydon haqiqiy, ikkinchisi esa mavjud "
                "bo'la olmaydi. Tenzorozetka jadvali esa amaliy jihatdan "
                "muhim: uchta o'lchov tekis deformatsiya holatini to'liq "
                "aniqlaydi va undan umumlashgan Guk qonuni orqali "
                "kuchlanishlar tiklanadi (mq-20)."
            ),
            common_mistakes=[
                "$\\gamma_{12}$ va $\\varepsilon_{12}$ ni chalkashtirish "
                "(koeffitsient 2).",
                "Qattiq burilishni deformatsiya deb hisoblash.",
                "Moslik shartlarini tekshirmasdan deformatsiya maydonini "
                "postulat qilish.",
                "Deformatsiyani $\\mu\\varepsilon$ ($10^{-6}$) va "
                "$\\%$ birliklarida chalkashtirish.",
            ],
            quiz=[
                q("Nima uchun ko'chish gradiyenti simmetrik va antisimmetrik "
                  "qismlarga ajratiladi?",
                  "Simmetrik qism (deformatsiya) kuchlanish hosil qiladi, "
                  "antisimmetrik (burilish) esa yo'q — ular fizik jihatdan "
                  "turli.", "konseptual"),
                q("$\\gamma_{12} = 0{,}002$. $\\varepsilon_{12}$ nimaga teng?",
                  "$0{,}001$ — tenzor komponentasi muhandislik "
                  "deformatsiyasining yarmi.", "hisob"),
                q("Moslik shartlari nima uchun kerak?",
                  "6 ta deformatsiya komponentasi 3 ta ko'chish funksiyasidan "
                  "hosil bo'ladi — demak ular mustaqil emas va o'zaro "
                  "bog'lanishlarni qanoatlantirishi kerak.", "konseptual"),
                q("$u_1 = cx_2$, $u_2 = -cx_1$. Bu deformatsiyami?",
                  "Yo'q — $\\varepsilon_{ij} = 0$, faqat qattiq burilish "
                  "($\\omega_{12} = -c$).", "hisob"),
                q("Kodda buzilgan maydon misoli nimani ko'rsatadi?",
                  "Ixtiyoriy tanlangan deformatsiya funksiyalari moslik "
                  "shartini qanoatlantirmasligi mumkin — bunday maydon "
                  "uzluksiz jismda mavjud bo'la olmaydi.", "kod"),
            ],
            bridge_to_next=(
                "Deformatsiya statik holatda o'rganildi. Suyuqliklar uchun "
                "esa deformatsiya emas, uning tezligi muhim — keyingi mavzu."
            ),
            research_extension=(
                "Raqamli tasvir korrelyatsiyasi (DIC) usulini "
                "modellashtiring: deformatsiyalangan sirtning ikki "
                "tasviridan ko'chish maydonini tiklang (korrelyatsiya "
                "orqali), so'ngra sonli differensiallash bilan deformatsiya "
                "maydonini hisoblang. Shovqinning natijaga ta'sirini "
                "baholang va silliqlash usullarini taqqoslang."
            ),
        ),
    ),
    Topic(
        id="tmm-06",
        subject_id=S,
        module_id=M,
        order=6,
        title="Tezliklar maydoni, deformatsiya tezligi va vorteks tenzori",
        description=(
            "Tezlik gradiyenti, deformatsiya tezligi tenzori, vorteks "
            "(aylanma) tenzori va sirkulyatsiya."
        ),
        learning_objective=(
            "Tezlik maydonidan deformatsiya tezligi va vorteksni ajratish "
            "hamda oqim xarakterini aniqlash."
        ),
        prerequisites=["tmm-05", "tmm-03"],
        mathematical_core=(
            "Tezlik gradiyenti $L_{ij} = \\partial v_i/\\partial x_j$, "
            "$D = \\frac{1}{2}(L+L^T)$, $W = \\frac{1}{2}(L-L^T)$, vorteks "
            "$\\boldsymbol{\\omega} = \\nabla\\times\\mathbf{v}$."
        ),
        engineering_application=(
            "Suyuqlik oqimlari tahlili, qorishtirish jarayonlari, "
            "aerodinamika, turbulentlik tuzilmasi."
        ),
        computational_component=(
            "Tezlik maydonidan $D$ va $W$ tenzorlarini hisoblash, vorteks "
            "maydonini qurish."
        ),
        visualization_component=(
            "Vorteks maydoni rangli xarita; deformatsiya va aylanish "
            "zonalari."
        ),
        research_extension=(
            "Q-kriteriysi va λ₂-kriteriysi: turbulent oqimda vorteks "
            "tuzilmalarini qanday ajratish mumkin?"
        ),
        difficulty="murakkab",
        previous_link=(
            "tmm-05 dagi deformatsiya tenzori statik holat uchun edi. "
            "Suyuqliklarda deformatsiyaning o'zi emas, uning tezligi "
            "kuchlanishni belgilaydi."
        ),
        next_topic="tmm-07",
        estimated_minutes=85,
        tags=["deformatsiya tezligi", "vorteks", "sirkulyatsiya"],
        lesson=Lesson(
            physical_problem=(
                "Daryodagi suv aylanma hosil qiladi. Aylanma ichidagi suv "
                "bo'lagi aylanadimi yoki faqat ko'chadimi? Bu farq muhim: "
                "aylanish yopishqoqlik kuchlarini keltirib chiqaradi, sof "
                "ko'chish esa yo'q. Tezlik maydonini deformatsiya va "
                "aylanishga ajratish bu savolga javob beradi."
            ),
            concepts=[
                c("Tezlik gradiyenti", "$L_{ij} = \\partial v_i/\\partial x_j$ — "
                  "tezlik maydonining fazoviy o'zgarishi."),
                c("Deformatsiya tezligi tenzori", "$D_{ij} = \\frac{1}{2}(L_{ij}+L_{ji})$ — "
                  "simmetrik qism; suyuqlikda kuchlanishni belgilaydi."),
                c("Vorteks (aylanma) tenzori", "$W_{ij} = \\frac{1}{2}(L_{ij}-L_{ji})$ — "
                  "antisimmetrik qism; suyuqlik elementining qattiq aylanishi."),
                c("Vorteks vektori", "$\\boldsymbol{\\omega} = \\nabla\\times\\mathbf{v}$; "
                  "$\\boldsymbol{\\omega} = 0$ — potensial (aylanmas) oqim."),
                c("Sirkulyatsiya", "$\\Gamma = \\oint\\mathbf{v}\\cdot d\\mathbf{l}$ — "
                  "yopiq kontur bo'ylab; ko'taruvchi kuch bilan bevosita "
                  "bog'liq (Jukovskiy teoremasi)."),
            ],
            derivation=[
                d("1-qadam. Tezlik gradiyentini ajratish",
                  r"L_{ij} = \frac{\partial v_i}{\partial x_j} = D_{ij} + W_{ij}",
                  "tmm-05 dagi bilan bir xil struktura, lekin ko'chish "
                  "o'rniga tezlik."),
                d("2-qadam. Deformatsiya tezligining fizik ma'nosi",
                  r"D_{11} = \frac{\partial v_1}{\partial x_1} = \frac{1}{l}\frac{dl}{dt}",
                  "Kesmaning nisbiy uzayish tezligi. Suyuqlikda aynan bu "
                  "kattalik yopishqoq kuchlanishni belgilaydi (tmm-27)."),
                d("3-qadam. Vorteks tenzori va vorteks vektori",
                  r"W_{ij} = -\tfrac{1}{2}\epsilon_{ijk}\omega_k,\qquad "
                  r"\boldsymbol{\omega} = \nabla\times\mathbf{v}",
                  "Antisimmetrik tenzor vektorga mos keladi. "
                  "$\\boldsymbol{\\omega}$ — suyuqlik elementining burchak "
                  "tezligining ikki barobari."),
                d("4-qadam. Sirkulyatsiya va Stoks teoremasi",
                  r"\Gamma = \oint_C\mathbf{v}\cdot d\mathbf{l} = \int_S(\nabla\times\mathbf{v})\cdot d\mathbf{S} = "
                  r"\int_S\boldsymbol{\omega}\cdot d\mathbf{S}",
                  "Sirkulyatsiya kontur ichidagi vorteks oqimiga teng. "
                  "Potensial oqimda $\\Gamma = 0$ (agar kontur ichida "
                  "singulyarlik bo'lmasa)."),
            ],
            formula_meaning=(
                "Deformatsiya tezligi va vorteksga ajratish oqimning ikki "
                "xil 'harakat' turini farqlaydi: birinchisi suyuqlik "
                "elementining shaklini o'zgartiradi (va yopishqoqlik "
                "tufayli energiya yo'qotadi), ikkinchisi uni qattiq jism "
                "kabi buradi (energiya yo'qotmaydi). Aerodinamikada "
                "sirkulyatsiya hal qiluvchi: qanotning ko'taruvchi kuchi "
                "$L = \\rho v\\Gamma$ (Jukovskiy) — sirkulyatsiyasiz "
                "ko'tarilish yo'q."
            ),
            equations=[
                eq(r"D_{ij} = \tfrac{1}{2}\left(\frac{\partial v_i}{\partial x_j}+\frac{\partial v_j}{\partial x_i}\right)",
                   "Deformatsiya tezligi tenzori.", "Deformatsiya tezligi"),
                eq(r"\boldsymbol{\omega} = \nabla\times\mathbf{v}", "Vorteks vektori.", "Vorteks"),
                eq(r"\Gamma = \oint_C\mathbf{v}\cdot d\mathbf{l}", "Sirkulyatsiya.",
                   "Sirkulyatsiya"),
            ],
            conditions=(
                "Potensial oqim ($\\boldsymbol{\\omega} = 0$) da tezlik "
                "potensial funksiya gradiyenti sifatida ifodalanadi: "
                "$\\mathbf{v} = \\nabla\\varphi$ — bu masalani sezilarli "
                "soddalashtiradi. Real yopishqoq oqimda chegara qatlamida "
                "vorteks hosil bo'ladi va potensial nazariya faqat undan "
                "tashqarida o'rinli."
            ),
            worked_example=WorkedExample(
                statement=(
                    "Ikki oqim: (a) qattiq jism kabi aylanish "
                    "$v_\\theta = \\Omega r$; (b) potensial aylanma "
                    "$v_\\theta = \\Gamma_0/(2\\pi r)$. Har biri uchun "
                    "vorteks va sirkulyatsiyani hisoblang. Qaysi biri "
                    "suyuqlik elementini buradi?"
                ),
                given=[r"\text{(a) } v_\theta = \Omega r,\ \Omega = 2\ \text{s}^{-1}",
                       r"\text{(b) } v_\theta = \frac{\Gamma_0}{2\pi r},\ \Gamma_0 = 4\ \text{m}^2/\text{s}"],
                steps=[
                    st(r"\text{(a) } \omega_z = \frac{1}{r}\frac{\partial(rv_\theta)}{\partial r} = "
                       r"\frac{1}{r}\frac{\partial(\Omega r^2)}{\partial r} = 2\Omega = 4\ \text{s}^{-1}",
                       "Qattiq jism aylanishida vorteks hamma joyda "
                       "o'zgarmas va nolga teng emas."),
                    st(r"\Gamma_{(a)} = \oint v_\theta\,dl = \Omega R\cdot2\pi R = 2\pi\Omega R^2",
                       "$R = 1$ m uchun $\\Gamma = 12{,}57$ m²/s; radius "
                       "bilan o'sadi."),
                    st(r"\text{(b) } \omega_z = \frac{1}{r}\frac{\partial}{\partial r}\left(r\cdot\frac{\Gamma_0}{2\pi r}\right) = "
                       r"\frac{1}{r}\frac{\partial}{\partial r}\left(\frac{\Gamma_0}{2\pi}\right) = 0",
                       "Potensial aylanmada vorteks NOLGA teng (markazdan "
                       "tashqarida) — bu paradoksal, lekin to'g'ri."),
                    st(r"\Gamma_{(b)} = \frac{\Gamma_0}{2\pi R}\cdot2\pi R = \Gamma_0 = 4\ \text{m}^2/\text{s}",
                       "Sirkulyatsiya radiusdan bog'liq emas va nolga teng "
                       "emas — chunki markazda singulyarlik bor."),
                    st(r"\text{(a): element buriladi; (b): element burilmaydi, "
                       r"faqat ko'chadi va deformatsiyalanadi}",
                       "Potensial aylanmada suyuqlik elementi o'z "
                       "orientatsiyasini saqlaydi — bu Stoks teoremasining "
                       "ta'sirchan namoyishi."),
                ],
                answer=(
                    "(a) $\\omega_z = 2\\Omega = 4$ 1/s, $\\Gamma = 2\\pi\\Omega R^2$; "
                    "(b) $\\omega_z = 0$, $\\Gamma = \\Gamma_0 = 4$ m²/s "
                    "(markazdagi singulyarlik hisobiga)."
                ),
                engineering_note=(
                    "Potensial aylanma real aylanmalarning (bo'ron, "
                    "vannadagi suv) tashqi qismini yaxshi tavsiflaydi; "
                    "markazda esa yopishqoqlik tufayli qattiq jism kabi "
                    "aylanadigan yadro hosil bo'ladi (Rankine aylanmasi). "
                    "Aerodinamikada sirkulyatsiya ko'taruvchi kuchni "
                    "belgilaydi: $L = \\rho v_\\infty\\Gamma$."
                ),
            ),
            computation=Computation(
                caption=(
                    "Tezlik maydoni tahlili: deformatsiya tezligi, vorteks "
                    "va sirkulyatsiyani hisoblang."
                ),
                code='''"""Tezlik gradiyenti: deformatsiya tezligi va vorteks."""
import numpy as np
from labkit import PARAMS, note, series, table, value

Omega = float(PARAMS.get("Omega", 2.0))      # qattiq aylanish, 1/s
Gamma0 = float(PARAMS.get("Gamma0", 4.0))    # potensial aylanma, m²/s
r_core = float(PARAMS.get("r_core", 0.3))    # Rankine yadro radiusi, m
R_max = float(PARAMS.get("R_max", 2.0))      # tahlil radiusi, m
shear = float(PARAMS.get("shear", 0.0))      # sof siljish oqimi qo'shimchasi

r = np.linspace(0.01, R_max, 300)

# Uch xil oqim
v_solid = Omega*r
v_potential = Gamma0/(2*np.pi*r)
v_rankine = np.where(r <= r_core, Gamma0*r/(2*np.pi*r_core**2), Gamma0/(2*np.pi*r))

series("Qattiq aylanish v(r)", r.tolist(), v_solid.tolist(), xlabel="r, m", ylabel="v_θ, m/s")
series("Potensial aylanma v(r)", r.tolist(), np.minimum(v_potential, 10).tolist(),
       xlabel="r, m", ylabel="v_θ, m/s")
series("Rankine aylanmasi v(r)", r.tolist(), v_rankine.tolist(),
       xlabel="r, m", ylabel="v_θ, m/s")

# Vorteks: omega_z = (1/r) d(r*v_theta)/dr
def vorticity(rr, vv):
    return np.gradient(rr*vv, rr)/rr

series("Vorteks: qattiq aylanish", r.tolist(), vorticity(r, v_solid).tolist(),
       xlabel="r, m", ylabel="ω_z, 1/s")
series("Vorteks: potensial", r.tolist(), vorticity(r, v_potential).tolist(),
       xlabel="r, m", ylabel="ω_z, 1/s")
series("Vorteks: Rankine", r.tolist(), vorticity(r, v_rankine).tolist(),
       xlabel="r, m", ylabel="ω_z, 1/s")

value("ω (qattiq aylanish)", float(np.median(vorticity(r, v_solid))), "1/s")
value("ω (potensial, r>0)", float(np.median(vorticity(r, v_potential))), "1/s")
note("Potensial aylanmada vorteks nolga teng — suyuqlik elementi burilmaydi, "
     "faqat deformatsiyalanadi. Bu Stoks teoremasining natijasi.")

# Sirkulyatsiya
for R_test in (0.5, 1.0, 1.5):
    G_solid = Omega*R_test*2*np.pi*R_test
    G_pot = Gamma0
    note(f"R = {R_test} m: Γ(qattiq) = {G_solid:.3f} m²/s, "
         f"Γ(potensial) = {G_pot:.3f} m²/s (radiusdan bog'liq emas)")

# Dekart koordinatalarda tezlik gradiyenti tahlili
def analyze(L):
    D = 0.5*(L + L.T)
    W = 0.5*(L - L.T)
    omega_z = L[1, 0] - L[0, 1]
    Q = 0.5*(np.sum(W*W) - np.sum(D*D))
    return D, W, omega_z, Q

flows = {
    "Sof siljish (v=γy, 0)": np.array([[0.0, 1.0], [0.0, 0.0]]),
    "Sof deformatsiya (kx, -ky)": np.array([[1.0, 0.0], [0.0, -1.0]]),
    "Qattiq aylanish": np.array([[0.0, -1.0], [1.0, 0.0]]),
    "Aralash": np.array([[1.0, 1.0], [0.0, -1.0]]),
}
rows = []
for name, L in flows.items():
    D, W, wz, Q = analyze(L)
    rows.append([name, float(np.linalg.norm(D)), float(np.linalg.norm(W)),
                 float(wz), float(Q),
                 "aylanma" if Q > 0 else ("deformatsiya" if Q < 0 else "muvozanat")])
table("Oqim turlarini tasniflash",
      ["Oqim", "||D||", "||W||", "ω_z", "Q-kriteriy", "Xarakter"], rows)
note("Q > 0: aylanish ustun (vorteks yadrosi); Q < 0: deformatsiya ustun. "
     "Bu — turbulent oqimda vorteks tuzilmalarini ajratish mezoni.")

table("Deformatsiya tezligi va vorteksni taqqoslash",
      ["Xususiyat", "D (deformatsiya tezligi)", "W (vorteks)"],
      [["Simmetriya", "Simmetrik", "Antisimmetrik"],
       ["Fizik ma'no", "Shakl o'zgarishi tezligi", "Qattiq aylanish"],
       ["Yopishqoq kuchlanish", "Hosil qiladi", "Hosil qilmaydi"],
       ["Energiya dissipatsiyasi", "Bor", "Yo'q"],
       ["Komponentalar soni (3D)", "6", "3 (vektorga ekvivalent)"]])
''',
                parameters=[
                    p("Omega", "Aylanish tezligi Ω", 0.1, 20.0, 2.0, 0.1, "1/s"),
                    p("Gamma0", "Sirkulyatsiya Γ₀", 0.5, 50.0, 4.0, 0.5, "m²/s"),
                    p("r_core", "Rankine yadro radiusi", 0.05, 1.5, 0.3, 0.05, "m"),
                    p("R_max", "Tahlil radiusi", 0.5, 10.0, 2.0, 0.5, "m"),
                    p("shear", "Siljish qo'shimchasi", 0.0, 5.0, 0.0, 0.5, "1/s"),
                ],
                expected_output="ω(qattiq) = 4 1/s, ω(potensial) = 0, Γ(potensial) = 4 m²/s",
            ),
            visualization=vis(
                "Vorteks maydoni va oqim turlari",
                "React/SVG + Matplotlib",
                "Tezlik maydoni strelkalar bilan; vorteks darajasi rangli "
                "fon sifatida. Uch xil oqim (qattiq aylanish, potensial "
                "aylanma, Rankine) yonma-yon.",
                "React/SVG: vorteks maydonini rangli fon, tezlikni strelkalar "
                "bilan berish — CFD postprotsessorlarining standart tasviri. "
                "Suyuqlik elementining orientatsiyasini kichik krest bilan "
                "belgilash potensial oqimdagi 'burilmaslikni' ko'rsatadi.",
            ),
            interpretation=(
                "Uch oqim taqqoslashi asosiy xulosani beradi: potensial "
                "aylanmada tezlik katta, lekin vorteks nol — suyuqlik "
                "elementi burilmaydi. Rankine modeli esa real aylanmani "
                "yaxshi tavsiflaydi: markazda qattiq aylanish, tashqarida "
                "potensial. Q-kriteriysi jadvali turbulent oqimda vorteks "
                "tuzilmalarini avtomatik ajratish imkonini beradi — bu "
                "zamonaviy CFD tahlilining standart vositasi."
            ),
            common_mistakes=[
                "Aylanma harakatni har doim vorteks bor deb hisoblash — "
                "potensial aylanmada u nolga teng.",
                "Vorteks vektorini burchak tezligi bilan tenglashtirish "
                "($\\boldsymbol{\\omega} = 2\\boldsymbol{\\Omega}$).",
                "Sirkulyatsiyani hisoblashda kontur yo'nalishini "
                "e'tiborsiz qoldirish.",
                "Deformatsiya tezligi va deformatsiyani chalkashtirish "
                "(birinchisining birligi 1/s).",
            ],
            quiz=[
                q("Nima uchun potensial aylanmada vorteks nolga teng?",
                  "$v_\\theta \\propto 1/r$ bo'lgani uchun $rv_\\theta = "
                  "\\text{const}$ va uning hosilasi nol. Fizik jihatdan: "
                  "element cho'ziladi, lekin burilmaydi.", "konseptual"),
                q("Suyuqlikda kuchlanishni $D$ mi yoki $W$ mi belgilaydi?",
                  "$D$ — deformatsiya tezligi. Qattiq aylanishda kuchlanish "
                  "hosil bo'lmaydi.", "konseptual"),
                q("$\\Omega = 5$ 1/s qattiq aylanish. $\\omega_z$?",
                  "$\\omega_z = 2\\Omega = 10$ 1/s.", "hisob"),
                q("Sirkulyatsiya ko'taruvchi kuch bilan qanday bog'liq?",
                  "Jukovskiy teoremasi: $L = \\rho v_\\infty\\Gamma$ — "
                  "sirkulyatsiyasiz ko'tarilish bo'lmaydi.", "talqin"),
                q("Kodda Q-kriteriysi nimani ko'rsatadi?",
                  "$Q = \\frac{1}{2}(||W||^2 - ||D||^2)$; $Q > 0$ bo'lsa "
                  "aylanish deformatsiyadan ustun — bu vorteks yadrosining "
                  "belgisi.", "kod"),
            ],
            bridge_to_next=(
                "Kinematika to'liq o'rganildi: deformatsiya va uning "
                "tezligi. Endi ularni keltirib chiqaruvchi sababga — "
                "kuchlanishga o'tamiz."
            ),
            research_extension=(
                "Turbulent oqimda vorteks tuzilmalarini ajratish "
                "kriteriylarini taqqoslang: Q-kriteriysi, $\\lambda_2$ "
                "kriteriysi va $\\Delta$-kriteriysi. Sodda oqim maydonida "
                "(masalan, ikki aylanma) ularning natijalarini hisoblang "
                "va qaysi biri vorteks chegarasini aniqroq belgilashini "
                "tahlil qiling."
            ),
        ),
    ),
]
