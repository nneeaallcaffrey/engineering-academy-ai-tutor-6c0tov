"""MQ / 2-modul: Kesim geometriyasi, siljish va buralish (mq-07 … mq-12)."""

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
M = "mq-m2"

TOPICS = [
    Topic(
        id="mq-07",
        subject_id=S,
        module_id=M,
        order=7,
        title="Kesim yuzasining geometrik tavsiflari: statik moment va og'irlik markazi",
        description=(
            "Statik moment, og'irlik markazi, murakkab kesimni bo'laklarga ajratish "
            "va markaziy o'qlar tushunchasi."
        ),
        learning_objective=(
            "Ixtiyoriy murakkab kesimning og'irlik markazini va markaziy o'qlar "
            "holatini aniqlash."
        ),
        prerequisites=["nm-16", "mq-05"],
        mathematical_core=(
            "Yuza bo'yicha integral $S_x = \\int_A y\\,dA$, additivlik, manfiy yuza usuli."
        ),
        engineering_application=(
            "Prokat profillar (dvutavr, shveller), payvand kesimlar, murakkab "
            "konstruktiv elementlar."
        ),
        computational_component=(
            "Ixtiyoriy ko'pburchak kesim uchun geometrik tavsiflarni Grin formulasi "
            "orqali hisoblash."
        ),
        visualization_component=(
            "Kesim konturi, bo'laklar va og'irlik markazi; markaziy o'qlar."
        ),
        research_extension=(
            "Ixtiyoriy kontur uchun geometrik tavsiflarni hisoblashning eng samarali "
            "algoritmi qanday? (Grin teoremasi va ko'pburchak formulalari)"
        ),
        difficulty="asosiy",
        previous_link=(
            "nm-16 da massalar markazini topdik. Kesim uchun bu aynan shu hisob, "
            "faqat massa o'rniga yuza — chunki bir jinsli plastinada ular proporsional."
        ),
        next_topic="mq-08",
        estimated_minutes=80,
        tags=["statik moment", "og'irlik markazi", "kesim geometriyasi"],
        lesson=Lesson(
            physical_problem=(
                "Dvutavr balkani yon tomonga yotqizsak, u bir necha marta ko'proq "
                "egiladi. Sabab — kesim geometriyasi. Egilishga qarshilik "
                "materialning kesimda qanday taqsimlanganiga bog'liq, va bu "
                "taqsimotni raqamlar bilan tavsiflash kerak. Birinchi qadam — "
                "markazni topish, chunki barcha keyingi hisoblar undan boshlanadi."
            ),
            concepts=[
                c("Statik moment", "$S_x = \\int_A y\\,dA$ — yuzaning $x$ o'qiga "
                  "nisbatan birinchi momenti. O'lchamligi m³."),
                c("Og'irlik markazi", "$y_C = S_x/A$ — kesim yuzasining 'markazi'. "
                  "Simmetriya o'qi bo'lsa, markaz unda yotadi."),
                c("Markaziy o'q", "Og'irlik markazidan o'tuvchi o'q. Unga nisbatan "
                  "statik moment nolga teng: $S_{x_C} = 0$."),
                c("Additivlik", "$S_x = \\sum A_iy_i$ — murakkab kesim bo'laklarga "
                  "ajratiladi."),
                c("Manfiy yuza usuli", "Teshik yoki kesib olingan qism manfiy yuza "
                  "sifatida hisobga olinadi."),
            ],
            derivation=[
                d("1-qadam. Statik moment ta'rifi",
                  r"S_x = \int_A y\,dA,\qquad S_y = \int_A z\,dA",
                  "Elementar yuzaning o'qgacha bo'lgan masofasiga ko'paytmasi "
                  "yig'indisi. Ishorasi bor: o'qning ikki tomonida qarama-qarshi."),
                d("2-qadam. Og'irlik markazi koordinatasi",
                  r"y_C = \frac{S_x}{A} = \frac{\int_A y\,dA}{\int_A dA}",
                  "Og'irlikli o'rtacha — nm-16 dagi massalar markazi bilan bir xil "
                  "struktura."),
                d("3-qadam. Markaziy o'qqa nisbatan statik moment",
                  r"S_{x_C} = \int_A(y-y_C)dA = S_x - y_CA = S_x - S_x = 0",
                  "Markaziy o'qning ta'rifiy xossasi. Bu keyingi mavzudagi Shteyner "
                  "formulasining kaliti."),
                d("4-qadam. Murakkab kesim uchun",
                  r"y_C = \frac{\sum_i A_iy_i}{\sum_i A_i},\qquad A_{teshik} < 0",
                  "Bo'laklarga ajratish har doim integrallashdan qulayroq. Standart "
                  "profillar uchun tavsiflar jadvaldan olinadi."),
            ],
            formula_meaning=(
                "Og'irlik markazi — kesimning 'muvozanat nuqtasi'. Egilishda neytral "
                "o'q aynan shu yerdan o'tadi (mq-13), cho'zilishda esa kuch shu "
                "nuqtaga qo'yilsa kesim tekis cho'ziladi. Markazni noto'g'ri topish "
                "keyingi barcha hisoblarni buzadi, shuning uchun bu — eng ko'p "
                "tekshiriladigan hisob."
            ),
            equations=[
                eq(r"S_x = \int_A y\,dA = \sum_i A_iy_i", "Statik moment.", "Statik moment"),
                eq(r"y_C = \frac{S_x}{A}", "Og'irlik markazi koordinatasi.", "Markaz"),
                eq(r"S_{x_C} = 0", "Markaziy o'qning xossasi.", "Markaziy o'q"),
            ],
            conditions=(
                "Koordinata sistemasi ixtiyoriy tanlanadi, lekin barcha bo'laklar "
                "uchun bir xil bo'lishi shart. Qulay tanlov: eng pastki yoki eng "
                "chap nuqta. Simmetriya o'qi bo'lsa, markaz unda yotadi — bu "
                "hisobni yarim marta qisqartiradi."
            ),
            worked_example=WorkedExample(
                statement=(
                    "Shvellersimon kesim: vertikal devor $10\\times 200$ mm, ikkita "
                    "gorizontal tokcha $80\\times 12$ mm (yuqori va quyi, devorning "
                    "o'ng tomoniga biriktirilgan). Og'irlik markazi koordinatalarini "
                    "chap-pastki burchakdan hisoblang."
                ),
                given=[r"\text{Devor: } 10\times200\ \text{mm}",
                       r"\text{Tokchalar: } 2\times(80\times12)\ \text{mm}"],
                steps=[
                    st(r"A_1 = 10\cdot 200 = 2000;\quad A_2 = A_3 = 80\cdot 12 = 960\ \text{mm}^2",
                       "Bo'laklar yuzalari."),
                    st(r"A = 2000 + 2\cdot 960 = 3920\ \text{mm}^2",
                       "Umumiy yuza."),
                    st(r"z_1 = 5;\quad z_2 = z_3 = 10 + 40 = 50\ \text{mm}",
                       "Bo'laklar markazlarining $z$ koordinatalari (chapdan)."),
                    st(r"y_1 = 100;\quad y_2 = 6;\quad y_3 = 194\ \text{mm}",
                       "$y$ koordinatalari (pastdan)."),
                    st(r"z_C = \frac{2000\cdot 5 + 960\cdot 50 + 960\cdot 50}{3920} = "
                       r"\frac{10\,000+96\,000}{3920} = \frac{106\,000}{3920} = 27{,}0\ \text{mm}",
                       "Gorizontal koordinata."),
                    st(r"y_C = \frac{2000\cdot100 + 960\cdot 6 + 960\cdot 194}{3920} = "
                       r"\frac{200\,000+5760+186\,240}{3920} = 100{,}0\ \text{mm}",
                       "Vertikal koordinata — simmetriya tufayli aynan o'rtada ✓"),
                ],
                answer="$A = 3920$ mm²; $z_C = 27{,}0$ mm; $y_C = 100{,}0$ mm.",
                engineering_note=(
                    "Gorizontal simmetriya $y_C = 100$ ni oldindan bashorat qilish "
                    "imkonini beradi — bu hisobni tekshirishning eng tez usuli. "
                    "$z_C = 27$ mm esa devordan sezilarli uzoqda: shuning uchun "
                    "shvellerni egishda buralish ham paydo bo'ladi (siljish markazi "
                    "masalasi)."
                ),
            ),
            computation=Computation(
                caption=(
                    "Kesim geometriyasi: bo'laklar o'lchamlarini o'zgartirib, "
                    "markaz holatini kuzating."
                ),
                code='''"""Kesim geometrik tavsiflari: statik moment va og'irlik markazi."""
import numpy as np
from labkit import PARAMS, note, series, table, value

t_web = float(PARAMS.get("t_web", 10.0))      # devor qalinligi, mm
h_web = float(PARAMS.get("h_web", 200.0))     # devor balandligi, mm
b_fl = float(PARAMS.get("b_fl", 80.0))        # tokcha eni, mm
t_fl = float(PARAMS.get("t_fl", 12.0))        # tokcha qalinligi, mm

# Bo'laklar: (yuza, z_markaz, y_markaz, nom)
parts = [
    (t_web*h_web, t_web/2, h_web/2, "Devor"),
    (b_fl*t_fl, t_web + b_fl/2, t_fl/2, "Quyi tokcha"),
    (b_fl*t_fl, t_web + b_fl/2, h_web - t_fl/2, "Yuqori tokcha"),
]

A = sum(p[0] for p in parts)
Sy = sum(p[0]*p[1] for p in parts)
Sx = sum(p[0]*p[2] for p in parts)
zC, yC = Sy/A, Sx/A

value("Umumiy yuza A", A, "mm²")
value("Statik moment S_x", Sx, "mm³")
value("Statik moment S_y", Sy, "mm³")
value("z_C", zC, "mm")
value("y_C", yC, "mm")

table("Bo'laklar", ["Bo'lak", "A, mm²", "z, mm", "y, mm", "A·z", "A·y"],
      [[p[3], float(p[0]), float(p[1]), float(p[2]), float(p[0]*p[1]), float(p[0]*p[2])]
       for p in parts])

# Markaziy o'qqa nisbatan statik moment nolga teng bo'lishi kerak
S_central = sum(p[0]*(p[2]-yC) for p in parts)
note(f"Markaziy o'qqa nisbatan S_xC = {S_central:.6f} mm³ (nol bo'lishi kerak) ✓")

# Ixtiyoriy ko'pburchak uchun Grin formulasi bilan tekshirish
def polygon_props(pts):
    """Ko'pburchak yuzasi va og'irlik markazi (Grin teoremasi)."""
    x = np.asarray([p[0] for p in pts], dtype=float)
    y = np.asarray([p[1] for p in pts], dtype=float)
    x2, y2 = np.roll(x, -1), np.roll(y, -1)
    cross = x*y2 - x2*y
    Aa = 0.5*np.sum(cross)
    cx = np.sum((x + x2)*cross)/(6*Aa)
    cy = np.sum((y + y2)*cross)/(6*Aa)
    return abs(Aa), cx, cy

contour = [(0, 0), (t_web+b_fl, 0), (t_web+b_fl, t_fl), (t_web, t_fl),
           (t_web, h_web-t_fl), (t_web+b_fl, h_web-t_fl), (t_web+b_fl, h_web),
           (0, h_web)]
A_p, z_p, y_p = polygon_props(contour)
note(f"Grin formulasi bo'yicha: A = {A_p:.1f} mm², z_C = {z_p:.3f} mm, y_C = {y_p:.3f} mm")
note(f"Bo'laklar usuli bilan farq: A {abs(A_p-A):.3f} mm², z_C {abs(z_p-zC):.4f} mm")

series("Kesim konturi", [p[0] for p in contour]+[contour[0][0]],
       [p[1] for p in contour]+[contour[0][1]], xlabel="z, mm", ylabel="y, mm")

# Tokcha kengligining markaz holatiga ta'siri
bb = np.linspace(20, 200, 100)
zc_arr = [(t_web*h_web*t_web/2 + 2*(b*t_fl)*(t_web+b/2))/(t_web*h_web + 2*b*t_fl) for b in bb]
series("z_C(tokcha kengligi)", bb.tolist(), zc_arr, xlabel="b, mm", ylabel="z_C, mm")
''',
                parameters=[
                    p("t_web", "Devor qalinligi", 4.0, 40.0, 10.0, 1.0, "mm"),
                    p("h_web", "Devor balandligi", 50.0, 600.0, 200.0, 10.0, "mm"),
                    p("b_fl", "Tokcha eni", 20.0, 250.0, 80.0, 5.0, "mm"),
                    p("t_fl", "Tokcha qalinligi", 4.0, 40.0, 12.0, 1.0, "mm"),
                ],
                expected_output="A = 3920 mm², z_C = 27,0 mm, y_C = 100,0 mm",
            ),
            visualization=vis(
                "Kesim konturi va og'irlik markazi",
                "React/SVG",
                "Kesim konturi to'ldirilgan shakl sifatida; bo'laklarga ajratish "
                "chiziqlari punktir; og'irlik markazi krest belgisi bilan; "
                "markaziy o'qlar shtrix-punktir.",
                "React/SVG: kesim — ko'pburchak, uni `<polygon>` bilan chizish "
                "tabiiy. `CrossSection` komponenti sifatida yozing: u mq-08, mq-13, "
                "mq-19 va su-21 da qayta ishlatiladi. O'qlarni mexanik chizmalar "
                "uslubida (shtrix-punktir) berish muhim.",
            ),
            interpretation=(
                "Grin formulasi va bo'laklar usuli bir xil natija beradi — bu "
                "hisobning to'g'riligini tasdiqlaydi. $z_C(b)$ grafigi ko'rsatadiki, "
                "tokchani kengaytirish markazni devordan uzoqlashtiradi va bu "
                "assimetriyani kuchaytiradi. Simmetrik kesimlarda ($y_C$) markaz "
                "avtomatik o'rtada — bu hisobni tekshirishning eng oson usuli."
            ),
            common_mistakes=[
                "Bo'laklar markazlarini turli koordinata boshlaridan o'lchash.",
                "Teshiklarni musbat yuza bilan qo'shish.",
                "Simmetriya o'qini tekshirmasdan markazni hisoblash (vaqt yo'qotish).",
                "Statik moment (mm³) va inersiya momentini (mm⁴) chalkashtirish.",
            ],
            quiz=[
                q("Markaziy o'qqa nisbatan statik moment nimaga teng va nega?",
                  "Nolga: $S_{x_C} = \\int(y-y_C)dA = S_x - y_CA = 0$, chunki "
                  "$y_C = S_x/A$.", "konseptual"),
                q("Simmetriya o'qi bo'lsa, markaz qayerda?",
                  "Simmetriya o'qida — chunki uning ikki tomonidagi statik momentlar "
                  "teng va qarama-qarshi.", "konseptual"),
                q("$A_1 = 1000$ mm² ($y_1 = 10$), $A_2 = 500$ mm² ($y_2 = 40$). $y_C$?",
                  "$y_C = (10\\,000+20\\,000)/1500 = 20$ mm.", "hisob"),
                q("Teshik bilan kesimda markaz qanday hisoblanadi?",
                  "Teshik manfiy yuza sifatida: $y_C = (A_1y_1 - A_{teshik}y_{teshik})/(A_1 - A_{teshik})$.",
                  "hisob"),
                q("Kodda `polygon_props` qaysi teoremaga asoslangan?",
                  "Grin teoremasiga: yuza integrallari kontur bo'ylab chiziqli "
                  "integralga aylantiriladi. Bu ixtiyoriy ko'pburchak uchun universal "
                  "va tez algoritm.", "kod"),
            ],
            bridge_to_next=(
                "Markaz topildi. Endi kesimning egilishga qarshiligini tavsiflovchi "
                "ikkinchi tartibli xarakteristikaga — inersiya momentiga o'tamiz."
            ),
            research_extension=(
                "Ixtiyoriy ko'pburchak kesim uchun barcha geometrik tavsiflarni "
                "(A, S, I, bosh o'qlar) Grin teoremasi asosida hisoblovchi kutubxona "
                "yozing. Uni standart prokat profillar (dvutavr, shveller) jadval "
                "qiymatlari bilan tekshiring va xatolikni baholang. Bu — FEM "
                "preprotsessorining real komponenti."
            ),
        ),
    ),
    Topic(
        id="mq-08",
        subject_id=S,
        module_id=M,
        order=8,
        title="Inersiya momentlari, o'qlarni ko'chirish va burish formulalari",
        description=(
            "O'q va qutb inersiya momentlari, markazdan qochma inersiya momenti, "
            "Shteyner formulasi, bosh o'qlar va qarshilik momenti."
        ),
        learning_objective=(
            "Murakkab kesimning inersiya momentlarini hisoblash va bosh markaziy "
            "o'qlarni aniqlash."
        ),
        prerequisites=["mq-07", "nm-17"],
        mathematical_core=(
            "Ikkinchi tartibli momentlar, Shteyner formulasi, tenzor "
            "almashtirishlari, xususiy qiymatlar masalasi."
        ),
        engineering_application=(
            "Balka kesimini tanlash, profil ratsionalligi, ustuvorlik hisobi uchun "
            "minimal inersiya momenti."
        ),
        computational_component=(
            "Inersiya tenzorini qurish, bosh o'qlarni eigenvalue orqali topish, "
            "profillarni samaradorlik bo'yicha taqqoslash."
        ),
        visualization_component=(
            "Bosh o'qlar holati va inersiya ellipsi; profillar taqqoslash diagrammasi."
        ),
        research_extension=(
            "Berilgan yuzada maksimal inersiya momentini beruvchi kesim shakli "
            "qanday? Optimallashtirish masalasi."
        ),
        difficulty="asosiy",
        previous_link=(
            "nm-17 dagi massaviy inersiya tenzori bilan bir xil matematik struktura, "
            "faqat $dm$ o'rniga $dA$. Xususiy qiymatlar masalasi ham aynan o'sha."
        ),
        next_topic="mq-09",
        estimated_minutes=90,
        tags=["inersiya momenti", "Shteyner", "bosh o'qlar"],
        lesson=Lesson(
            physical_problem=(
                "Bir xil yuzali ikki balka — to'rtburchak va dvutavr. Dvutavr 3–4 "
                "marta ko'proq yuk ko'taradi. Nima uchun? Chunki egilishga "
                "qarshilikni yuza emas, materialning neytral o'qdan uzoqligi "
                "belgilaydi. Bu 'uzoqlik' inersiya momenti orqali o'lchanadi — "
                "va aynan shu son kesim tanlashning asosiy mezoni."
            ),
            concepts=[
                c("O'q inersiya momenti", "$I_x = \\int_A y^2dA$ — har doim musbat, "
                  "o'lchamligi m⁴."),
                c("Qutb inersiya momenti", "$I_p = \\int_A\\rho^2dA = I_x + I_y$ — "
                  "buralish hisobida ishlatiladi."),
                c("Markazdan qochma inersiya momenti", "$I_{xy} = \\int_A xy\\,dA$ — "
                  "ishorasi bor; simmetriya o'qi bo'lsa nolga teng."),
                c("Shteyner formulasi", "$I_x = I_{x_C} + a^2A$ — parallel o'qqa "
                  "ko'chirish."),
                c("Qarshilik momenti", "$W_x = I_x/y_{max}$ — egilish hisobida "
                  "bevosita ishlatiladi (mq-13)."),
            ],
            derivation=[
                d("1-qadam. Ta'riflar",
                  r"I_x = \int_A y^2dA,\quad I_y = \int_A z^2dA,\quad "
                  r"I_p = \int_A\rho^2dA = I_x+I_y",
                  "$\\rho^2 = y^2+z^2$ dan qutb va o'q momentlari bog'lanishi "
                  "(perpendikular o'qlar teoremasi)."),
                d("2-qadam. Shteyner formulasini keltirib chiqarish",
                  r"I_x = \int_A(y_C+y')^2dA = y_C^2A + 2y_C\underbrace{\int y'dA}_{=0} + "
                  r"\int y'^2dA = I_{x_C} + a^2A",
                  "Markaziy o'qqa nisbatan statik moment nolga teng bo'lgani uchun "
                  "o'rta had yo'qoladi (mq-07). Xulosa: markaziy o'q minimal inersiya "
                  "momentini beradi."),
                d("3-qadam. O'qlarni burishda o'zgarish",
                  r"I_{x_1} = I_x\cos^2\alpha + I_y\sin^2\alpha - I_{xy}\sin 2\alpha",
                  "Koordinata almashtirish. Bu — nm-17 dagi tenzor almashtirishining "
                  "tekislikdagi holи va u mq-19 dagi Mor doirasi bilan bir xil."),
                d("4-qadam. Bosh o'qlar",
                  r"\tan 2\alpha_0 = \frac{2I_{xy}}{I_y - I_x},\qquad "
                  r"I_{max,min} = \frac{I_x+I_y}{2} \pm \sqrt{\left(\frac{I_x-I_y}{2}\right)^2 + I_{xy}^2}",
                  "$I_{xy} = 0$ bo'lgan o'qlar — bosh o'qlar. Ularga nisbatan "
                  "inersiya momentlari ekstremal qiymat oladi."),
            ],
            formula_meaning=(
                "$I = \\int y^2dA$ dagi kvadrat hal qiluvchi: neytral o'qdan 2 marta "
                "uzoqroq joylashgan material 4 marta ko'proq hissa qo'shadi. Shuning "
                "uchun dvutavrda material tokchalarga — eng chekka joyga — "
                "to'plangan. To'rtburchak kesim uchun $I = bh^3/12$: balandlikni 2 "
                "marta oshirish inersiya momentini 8 marta oshiradi. Bu — balkani "
                "yotqizib emas, tikka qo'yish kerakligining sababi."
            ),
            equations=[
                eq(r"I_x = \int_A y^2dA", "O'q inersiya momenti.", "Inersiya momenti"),
                eq(r"I_x = I_{x_C} + a^2A", "Shteyner (parallel o'qlar) formulasi.", "Shteyner"),
                eq(r"I_{to'rtburchak} = \frac{bh^3}{12},\quad I_{doira} = \frac{\pi d^4}{64}",
                   "Asosiy kesimlar uchun formulalar.", "Tipik kesimlar"),
                eq(r"W_x = \frac{I_x}{y_{max}}", "Qarshilik momenti.", "Qarshilik momenti"),
            ],
            conditions=(
                "Shteyner formulasi faqat markaziy o'qdan boshlanadi — ixtiyoriy ikki "
                "parallel o'q orasida to'g'ridan-to'g'ri qo'llab bo'lmaydi. "
                "Markazdan qochma moment $I_{xy}$ simmetriya o'qi bo'lsa avtomatik "
                "nolga teng, demak simmetrik kesimlarda simmetriya o'qlari bosh o'qlar "
                "bo'ladi."
            ),
            worked_example=WorkedExample(
                statement=(
                    "Tavrsimon kesim: tokcha $200\\times 20$ mm (yuqorida), devor "
                    "$20\\times 180$ mm. nm-16 da $y_C = 142{,}6$ mm topilgan edi. "
                    "Markaziy o'qqa nisbatan $I_{x_C}$ va qarshilik momentlarini "
                    "hisoblang."
                ),
                given=[r"A_1 = 4000\ \text{mm}^2\ (y_1 = 190),\; A_2 = 3600\ \text{mm}^2\ (y_2 = 90)",
                       r"y_C = 142{,}6\ \text{mm},\; A = 7600\ \text{mm}^2"],
                steps=[
                    st(r"I_{1}^{(o'z)} = \frac{200\cdot 20^3}{12} = \frac{200\cdot 8000}{12} = "
                       r"133\,333\ \text{mm}^4",
                       "Tokchaning o'z markaziy o'qiga nisbatan."),
                    st(r"a_1 = 190 - 142{,}6 = 47{,}4\ \text{mm} \Rightarrow "
                       r"I_1 = 133\,333 + 47{,}4^2\cdot 4000 = 133\,333 + 8\,985\,000",
                       "Shteyner formulasi bilan ko'chirish."),
                    st(r"I_1 = 9\,118\,333\ \text{mm}^4",
                       "Tokchaning hissasi — asosan ko'chirish hadi hisobiga."),
                    st(r"I_{2}^{(o'z)} = \frac{20\cdot 180^3}{12} = \frac{20\cdot 5\,832\,000}{12} = "
                       r"9\,720\,000\ \text{mm}^4",
                       "Devorning o'z inersiya momenti."),
                    st(r"a_2 = 142{,}6-90 = 52{,}6 \Rightarrow I_2 = 9\,720\,000 + 52{,}6^2\cdot 3600 = "
                       r"9\,720\,000 + 9\,959\,000 = 19\,679\,000\ \text{mm}^4",
                       "Devor hissasi."),
                    st(r"I_{x_C} = 9\,118\,333 + 19\,679\,000 = 28\,797\,333 \approx 2880\ \text{cm}^4;"
                       r"\quad W_{yuqori} = \frac{28\,797\,333}{57{,}4} = 501\,700\ \text{mm}^3",
                       "$W_{quyi} = 28\\,797\\,333/142{,}6 = 201\\,900$ mm³ — quyi tolalar "
                       "uchun qarshilik momenti 2,5 marta kichik."),
                ],
                answer=(
                    "$I_{x_C} = 2880$ cm⁴; $W_{yuqori} = 501{,}7$ cm³; "
                    "$W_{quyi} = 201{,}9$ cm³."
                ),
                engineering_note=(
                    "Qarshilik momentlarining farqi 2,5 marta — demak egilishda quyi "
                    "tolalar 2,5 marta ko'proq kuchlanish oladi. Tavrsimon kesim "
                    "aynan shuning uchun cho'yan kabi materiallarga mos: cho'yan "
                    "siqilishga yaxshi, cho'zilishga yomon chidaydi, shuning uchun "
                    "cho'zilgan zonaga ko'proq material qo'yiladi."
                ),
            ),
            computation=Computation(
                caption=(
                    "Inersiya momentlari: profil turini va o'lchamlarni o'zgartirib, "
                    "samaradorlikni taqqoslang."
                ),
                code='''"""Inersiya momentlari, Shteyner formulasi va bosh o'qlar."""
import numpy as np
from labkit import PARAMS, note, series, table, value

b_fl = float(PARAMS.get("b_fl", 200.0))   # tokcha eni, mm
t_fl = float(PARAMS.get("t_fl", 20.0))    # tokcha qalinligi, mm
t_web = float(PARAMS.get("t_web", 20.0))  # devor qalinligi, mm
h_web = float(PARAMS.get("h_web", 180.0)) # devor balandligi, mm

# Tavrsimon kesim: (A, y_markaz, I_o'z)
parts = [
    (b_fl*t_fl, h_web + t_fl/2, b_fl*t_fl**3/12, "Tokcha"),
    (t_web*h_web, h_web/2, t_web*h_web**3/12, "Devor"),
]
A = sum(p[0] for p in parts)
yC = sum(p[0]*p[1] for p in parts)/A
Ix = sum(p[2] + p[0]*(p[1]-yC)**2 for p in parts)
H = h_web + t_fl
W_top = Ix/(H - yC)
W_bot = Ix/yC
i_x = np.sqrt(Ix/A)

value("Yuza A", A, "mm²")
value("y_C", yC, "mm")
value("I_x", Ix/1e4, "cm⁴")
value("W (yuqori)", W_top/1000, "cm³")
value("W (quyi)", W_bot/1000, "cm³")
value("Inersiya radiusi i_x", i_x, "mm")

table("Shteyner hissalari",
      ["Bo'lak", "A, mm²", "I_o'z, cm⁴", "a, mm", "a²A, cm⁴", "Jami, cm⁴"],
      [[p[3], float(p[0]), float(p[2]/1e4), float(p[1]-yC),
        float(p[0]*(p[1]-yC)**2/1e4), float((p[2]+p[0]*(p[1]-yC)**2)/1e4)] for p in parts])

# Bir xil yuzadagi profillar samaradorligi
A_target = A
profiles = []
h_sq = np.sqrt(A_target)
profiles.append(["Kvadrat", h_sq**4/12, h_sq**3/6])
d_c = np.sqrt(4*A_target/np.pi)
profiles.append(["Doira", np.pi*d_c**4/64, np.pi*d_c**3/32])
h_r = np.sqrt(3*A_target)                       # h/b = 3
b_r = A_target/h_r
profiles.append(["To'rtburchak h/b=3", b_r*h_r**3/12, b_r*h_r**2/6])
# Dvutavr (taqribiy: 70 % tokchalarda)
h_i = 300.0
A_f = 0.35*A_target
t_w_i = 0.3*A_target/h_i
I_i = 2*A_f*(h_i/2)**2 + t_w_i*h_i**3/12
profiles.append(["Dvutavr h=300", I_i, I_i/(h_i/2)])
profiles.append(["Tavr (joriy)", Ix, min(W_top, W_bot)])

table("Bir xil yuzadagi profillar (A = %.0f mm²)" % A_target,
      ["Profil", "I, cm⁴", "W, cm³", "Samaradorlik W/W_kvadrat"],
      [[p[0], float(p[1]/1e4), float(p[2]/1000), float(p[2]/profiles[0][2])]
       for p in profiles])

# Balandlikning inersiya momentiga ta'siri (kubik qonun)
hh = np.linspace(50, 500, 200)
series("I(h) — to'rtburchak b=50 mm", hh.tolist(), (50*hh**3/12/1e4).tolist(),
       xlabel="h, mm", ylabel="I, cm⁴")
note("I ~ h³: balandlikni 2 marta oshirish I ni 8 marta oshiradi. "
     "Shuning uchun balka tikka qo'yiladi.")

# Bosh o'qlar (assimetrik kesim uchun)
Ix_t, Iy_t, Ixy_t = Ix, 4e7, 1.2e7
alpha0 = 0.5*np.arctan2(2*Ixy_t, Iy_t - Ix_t)
I_avg, I_dif = (Ix_t+Iy_t)/2, (Ix_t-Iy_t)/2
I_max = I_avg + np.hypot(I_dif, Ixy_t)
I_min = I_avg - np.hypot(I_dif, Ixy_t)
value("Bosh o'q burchagi α₀", np.degrees(alpha0), "deg")
value("I_max", I_max/1e4, "cm⁴")
value("I_min", I_min/1e4, "cm⁴")
note(f"Tekshirish: I_max + I_min = {(I_max+I_min)/1e4:.1f} cm⁴, "
     f"I_x + I_y = {(Ix_t+Iy_t)/1e4:.1f} cm⁴ — invariant ✓")
''',
                parameters=[
                    p("b_fl", "Tokcha eni", 50.0, 400.0, 200.0, 10.0, "mm"),
                    p("t_fl", "Tokcha qalinligi", 5.0, 60.0, 20.0, 1.0, "mm"),
                    p("t_web", "Devor qalinligi", 5.0, 60.0, 20.0, 1.0, "mm"),
                    p("h_web", "Devor balandligi", 50.0, 600.0, 180.0, 10.0, "mm"),
                ],
                expected_output="I_x ≈ 2880 cm⁴, W_yuqori ≈ 502 cm³, W_quyi ≈ 202 cm³",
            ),
            visualization=vis(
                "Profillarni taqqoslash va bosh o'qlar",
                "React/SVG",
                "Bir xil yuzadagi to'rt profil yonma-yon, har birining ostida $I$ va "
                "$W$ qiymatlari; ustunli diagramma samaradorlikni taqqoslaydi. "
                "Assimetrik kesim uchun bosh o'qlar burilgan holda ko'rsatiladi.",
                "React/SVG: taqqoslash diagrammasi — eng ta'sirchan pedagogik vosita. "
                "Bir xil yuzali kvadrat va dvutavrni yonma-yon ko'rsatib, $I$ "
                "qiymatlarini ustunlar bilan berish 'material qayerda bo'lishi kerak' "
                "degan g'oyani darhol yetkazadi.",
            ),
            interpretation=(
                "Profillar jadvali asosiy muhandislik xulosasini beradi: bir xil "
                "material sarfida dvutavr kvadratdan 5–8 marta ko'p qarshilik "
                "momentiga ega. $I(h)$ grafigi kubik — bu 'balandlik hukmronligi' "
                "qonuni. Bosh o'qlar hisobida esa $I_x + I_y = \\text{const}$ "
                "invarianti tekshiriladi — bu tenzor xossasi va u mq-19 dagi "
                "kuchlanish tenzorida takrorlanadi."
            ),
            common_mistakes=[
                "Shteyner formulasini markaziy bo'lmagan o'qdan boshlash.",
                "$a^2A$ hadini qo'shishni unutish — bu odatda asosiy hissa.",
                "$I$ (mm⁴) va $W$ (mm³) ni chalkashtirish.",
                "Assimetrik kesimda $W_{yuqori}$ va $W_{quyi}$ ni bir xil deb olish.",
            ],
            quiz=[
                q("Nima uchun dvutavr bir xil yuzadagi kvadratdan samaraliroq?",
                  "Chunki $I = \\int y^2dA$ da masofa kvadratga kiradi; dvutavrda "
                  "material neytral o'qdan uzoqda — tokchalarda joylashgan.",
                  "konseptual"),
                q("To'rtburchak kesim balandligini 2 marta oshirsak, $I$ va $W$ qanday "
                  "o'zgaradi?",
                  "$I$ 8 marta ($h^3$), $W$ 4 marta ($h^2$) ortadi.", "hisob"),
                q("$b = 40$ mm, $h = 120$ mm. $I_x$ va $W_x$ ni toping.",
                  "$I = 40\\cdot 120^3/12 = 5{,}76\\cdot10^6$ mm⁴; "
                  "$W = I/60 = 96\\,000$ mm³ = 96 cm³.", "hisob"),
                q("Markaziy o'q nima uchun minimal inersiya momentini beradi?",
                  "Shteyner formulasidan: $I = I_C + a^2A \\ge I_C$, chunki "
                  "$a^2A \\ge 0$.", "talqin"),
                q("Kodda $I_{max}+I_{min} = I_x+I_y$ tekshiruvi nimani ko'rsatadi?",
                  "Inersiya momentlari yig'indisi koordinata sistemasini burishda "
                  "o'zgarmaydi — bu tenzorning birinchi invarianti (nm-17, mq-19).",
                  "kod"),
            ],
            bridge_to_next=(
                "Geometrik tavsiflar tayyor. Endi ikkinchi asosiy deformatsiya "
                "turiga — siljishga o'tamiz, u buralish va egilish uchun zamin "
                "yaratadi."
            ),
            research_extension=(
                "Optimallashtirish masalasi: berilgan yuza $A$ va balandlik "
                "cheklovi $h \\le h_{max}$ da $W_x$ ni maksimallashtiruvchi "
                "dvutavr proporsiyalarini toping (tokcha eni, qalinligi, devor "
                "qalinligi). `scipy.optimize` bilan yeching va natijani standart "
                "prokat profillar bilan taqqoslang — ular optimalga qanchalik yaqin?"
            ),
        ),
    ),
    Topic(
        id="mq-09",
        subject_id=S,
        module_id=M,
        order=9,
        title="Siljish (kesilish) deformatsiyasi va siljish moduli",
        description=(
            "Toza siljish holati, siljish deformatsiyasi, Guk qonuni siljishda, "
            "elastik doimiylar orasidagi bog'lanish, birikmalar hisobi."
        ),
        learning_objective=(
            "Siljishdagi kuchlanish va deformatsiyani hisoblash, zakovkali va "
            "payvand birikmalarni loyihalash."
        ),
        prerequisites=["mq-05", "mq-02"],
        mathematical_core=(
            "$\\tau = G\\gamma$, elastik doimiylar bog'lanishi "
            "$G = E/[2(1+\\nu)]$, urinma kuchlanishlar juftligi qonuni."
        ),
        engineering_application=(
            "Zakovka, bolt, payvand chok, shpon, ponasimon birikmalar hisobi."
        ),
        computational_component=(
            "Zakovkali birikma hisobi: kesilish va ezilish shartlarini birgalikda "
            "tekshirish."
        ),
        visualization_component=(
            "Toza siljish elementi va uning deformatsiyasi; birikma sxemasi."
        ),
        research_extension=(
            "Ko'p zakovkali birikmada kuch qanday taqsimlanadi? Ideal bir xil "
            "taqsimot farazi qanchalik to'g'ri?"
        ),
        difficulty="asosiy",
        previous_link=(
            "mq-03 da normal kuchlanishni ko'rdik. Endi ikkinchi asosiy tur — "
            "urinma kuchlanish va unga mos deformatsiya."
        ),
        next_topic="mq-10",
        estimated_minutes=85,
        tags=["siljish", "kesilish", "birikma"],
        lesson=Lesson(
            physical_problem=(
                "Metall listlarni bog'lovchi zakovka ikki xil usulda buzilishi "
                "mumkin: kesilib ketishi yoki list teshigini ezib yuborishi. "
                "Qaysi biri avval sodir bo'ladi? Bu savol birikmani loyihalashda "
                "hal qiluvchi, chunki ikkala shart ham tekshirilishi va "
                "zakovkalar soni ularning eng qattiqrog'i bo'yicha tanlanishi kerak."
            ),
            concepts=[
                c("Toza siljish", "Element qirralarida faqat urinma kuchlanishlar "
                  "ta'sir qiladigan kuchlanish holati."),
                c("Siljish deformatsiyasi $\\gamma$", "To'g'ri burchakning "
                  "o'zgarishi (radianda). Odatda $10^{-3}$ tartibida."),
                c("Guk qonuni siljishda", "$\\tau = G\\gamma$; $G$ — siljish moduli, "
                  "po'lat uchun 80 GPa."),
                c("Urinma kuchlanishlar juftligi qonuni", "$\\tau_{xy} = \\tau_{yx}$ — "
                  "perpendikular maydonchalardagi urinma kuchlanishlar teng."),
                c("Ezilish kuchlanishi", "$\\sigma_{ez} = F/(d\\delta)$ — kontakt "
                  "yuzasidagi shartli kuchlanish."),
            ],
            derivation=[
                d("1-qadam. Urinma kuchlanishlar juftligi qonuni",
                  r"\sum M_z = 0:\; \tau_{xy}(dy\,dz)dx - \tau_{yx}(dx\,dz)dy = 0 "
                  r"\Rightarrow \tau_{xy} = \tau_{yx}",
                  "Elementar parallelepiped momentlari muvozanatidan. Bu — kuchlanish "
                  "tenzorining simmetrikligi (tmm-11 da umumlashtiriladi)."),
                d("2-qadam. Siljishda Guk qonuni",
                  r"\tau = G\gamma,\qquad \gamma = \frac{\Delta s}{a}",
                  "$\\gamma$ — to'g'ri burchakning o'zgarishi. Kichik burchaklarda "
                  "$\\tan\\gamma \\approx \\gamma$."),
                d("3-qadam. Elastik doimiylar bog'lanishi",
                  r"\boxed{\;G = \frac{E}{2(1+\nu)}\;}",
                  "Toza siljishni 45° burilgan o'qlarda ko'rsak, u ikki o'qli "
                  "cho'zilish-siqilishga aylanadi. Deformatsiyalarni tenglashtirish "
                  "shu bog'lanishni beradi (tmm-14 da qat'iy isbotlanadi). Po'lat "
                  "uchun $\\nu = 0{,}3$ → $G = 0{,}385E$."),
                d("4-qadam. Birikma hisobi shartlari",
                  r"\tau = \frac{F}{n\,i\,\pi d^2/4} \le [\tau];\qquad "
                  r"\sigma_{ez} = \frac{F}{n\,d\,\delta_{min}} \le [\sigma_{ez}]",
                  "$n$ — zakovkalar soni, $i$ — kesilish tekisliklari soni. "
                  "Ikkala shart ham bajarilishi kerak, zakovkalar soni qattiqrog'i "
                  "bo'yicha tanlanadi."),
            ],
            formula_meaning=(
                "$G = E/[2(1+\\nu)]$ — elastiklikning eng muhim bog'lanishlaridan "
                "biri: izotrop materialda mustaqil elastik doimiylar faqat ikkita. "
                "Birikma hisobida esa ikki shartning qaysi biri hal qiluvchi bo'lishi "
                "geometriyaga bog'liq: yupqa listlarda ezilish, qalin listlarda "
                "kesilish."
            ),
            equations=[
                eq(r"\tau = G\gamma", "Guk qonuni siljishda.", "Siljishda Guk qonuni"),
                eq(r"G = \frac{E}{2(1+\nu)}", "Elastik doimiylar bog'lanishi.", "G va E bog'lanishi"),
                eq(r"\tau_{xy} = \tau_{yx}", "Urinma kuchlanishlar juftligi qonuni.",
                   "Juftlik qonuni"),
                eq(r"\tau = \frac{F}{n i A_1} \le [\tau]", "Birikmani kesilishga hisoblash.",
                   "Kesilish sharti"),
            ],
            conditions=(
                "Birikma hisobida kuch barcha zakovkalarga bir tekis taqsimlanadi "
                "deb faraz qilinadi. Real holda chekka zakovkalar ko'proq yuk oladi "
                "(20–30 % gacha farq), lekin plastik deformatsiya bu farqni "
                "tenglashtiradi. Mo'rt materiallar va katta birikmalarda bu faraz "
                "ehtiyotkorlik bilan ishlatiladi."
            ),
            worked_example=WorkedExample(
                statement=(
                    "Ikki listni ($\\delta_1 = 10$ mm, $\\delta_2 = 12$ mm) "
                    "zakovkalar bog'laydi, $d = 16$ mm, bir kesilish tekisligi. "
                    "Uzatiladigan kuch $F = 180$ kN, $[\\tau] = 100$ MPa, "
                    "$[\\sigma_{ez}] = 240$ MPa. Zakovkalar sonini aniqlang."
                ),
                given=[r"d = 16\ \text{mm},\; i = 1,\; F = 180\ \text{kN}",
                       r"\delta_{min} = 10\ \text{mm}",
                       r"[\tau] = 100\ \text{MPa},\; [\sigma_{ez}] = 240\ \text{MPa}"],
                steps=[
                    st(r"A_1 = \frac{\pi d^2}{4} = \frac{3{,}1416\cdot 256}{4} = 201{,}1\ \text{mm}^2",
                       "Bitta zakovkaning kesilish yuzasi."),
                    st(r"n_\tau \ge \frac{F}{i A_1[\tau]} = \frac{180\,000}{1\cdot 201{,}1\cdot 100} = "
                       r"\frac{180\,000}{20\,110} = 8{,}95 \Rightarrow 9\ \text{ta}",
                       "Kesilish sharti bo'yicha."),
                    st(r"A_{ez} = d\,\delta_{min} = 16\cdot 10 = 160\ \text{mm}^2",
                       "Ezilish yuzasi — eng yupqa list bo'yicha."),
                    st(r"n_{ez} \ge \frac{F}{A_{ez}[\sigma_{ez}]} = \frac{180\,000}{160\cdot 240} = "
                       r"\frac{180\,000}{38\,400} = 4{,}69 \Rightarrow 5\ \text{ta}",
                       "Ezilish sharti bo'yicha."),
                    st(r"n = \max(9;\,5) = 9\ \text{ta}",
                       "Hal qiluvchi shart — kesilish."),
                    st(r"\tau_{haqiqiy} = \frac{180\,000}{9\cdot 201{,}1} = 99{,}5\ \text{MPa} \le 100\ \checkmark;"
                       r"\quad \sigma_{ez} = \frac{180\,000}{9\cdot 160} = 125\ \text{MPa} \le 240\ \checkmark",
                       "Ikkala shart ham bajarildi, ezilishda katta zaxira bor."),
                ],
                answer=(
                    "$n = 9$ ta zakovka (kesilish sharti hal qiluvchi); "
                    "$\\tau = 99{,}5$ MPa, $\\sigma_{ez} = 125$ MPa."
                ),
                engineering_note=(
                    "Ezilish bo'yicha zaxira 1,9 marta — demak zakovka diametrini "
                    "oshirish foydali bo'lardi: $d = 20$ mm da kesilish yuzasi "
                    "1,56 marta ortadi va 6 ta zakovka yetarli bo'ladi. Bu "
                    "birikmani ixchamlashtiradi va tayyorlashni arzonlashtiradi."
                ),
            ),
            computation=Computation(
                caption=(
                    "Zakovkali birikma: diametr va listlar qalinligini o'zgartirib, "
                    "qaysi shart hal qiluvchi ekanini aniqlang."
                ),
                code='''"""Siljish: elastik doimiylar va birikmalar hisobi."""
import numpy as np
from labkit import PARAMS, note, series, table, value

d = float(PARAMS.get("d", 16.0))          # zakovka diametri, mm
delta_min = float(PARAMS.get("delta", 10.0))  # eng yupqa list, mm
F = float(PARAMS.get("F", 180000.0))      # kuch, N
tau_allow = float(PARAMS.get("tau_allow", 100.0))    # MPa
sez_allow = float(PARAMS.get("sez_allow", 240.0))    # MPa
i_planes = float(PARAMS.get("i", 1))      # kesilish tekisliklari soni
E = 200e3                                  # MPa
nu = 0.3

G = E/(2*(1+nu))
value("Siljish moduli G", G/1000, "GPa")
value("G/E nisbati", G/E, "—")

A1 = np.pi*d**2/4
A_ez = d*delta_min
n_tau = F/(i_planes*A1*tau_allow)
n_ez = F/(A_ez*sez_allow)
n = int(np.ceil(max(n_tau, n_ez)))

value("Kesilish yuzasi A₁", A1, "mm²")
value("Ezilish yuzasi", A_ez, "mm²")
value("n (kesilishdan)", n_tau, "—")
value("n (ezilishdan)", n_ez, "—")
value("Qabul qilingan n", n, "dona")
value("τ haqiqiy", F/(n*i_planes*A1), "MPa")
value("σ_ez haqiqiy", F/(n*A_ez), "MPa")
note(f"Hal qiluvchi shart: {'KESILISH' if n_tau > n_ez else 'EZILISH'}")

# Diametrning kerakli zakovkalar soniga ta'siri
dd = np.linspace(8, 36, 100)
n_t = F/(i_planes*(np.pi*dd**2/4)*tau_allow)
n_e = F/(dd*delta_min*sez_allow)
series("n (kesilishdan)", dd.tolist(), n_t.tolist(), xlabel="d, mm", ylabel="n")
series("n (ezilishdan)", dd.tolist(), n_e.tolist(), xlabel="d, mm", ylabel="n")
cross = dd[np.argmin(np.abs(n_t - n_e))]
note(f"Ikkala shart teng bo'ladigan diametr: d ≈ {cross:.1f} mm. "
     "Undan kichik diametrda kesilish, kattaroqda ezilish hal qiluvchi.")

# Toza siljish deformatsiyasi
tau_work = F/(n*i_planes*A1)
gamma = tau_work/G
value("Siljish deformatsiyasi γ", gamma*1000, "mrad")
value("Siljish (a = 20 mm da)", gamma*20*1000, "mkm")

# Elastik doimiylar
table("Elastik doimiylar",
      ["Material", "E, GPa", "ν", "G, GPa", "G/E"],
      [[nm, Ei, ni, Ei/(2*(1+ni)), 1/(2*(1+ni))]
       for nm, Ei, ni in [("Po'lat", 200, 0.30), ("Alyuminiy", 70, 0.33),
                          ("Mis", 110, 0.34), ("Rezina", 0.01, 0.499),
                          ("Probka", 0.02, 0.0)]])
note("ν → 0,5 da G → E/3 (siqilmaydigan material, rezina); ν = 0 da G = E/2.")

table("Birikma turlari",
      ["Tur", "Kesilish tekisliklari", "Formula"],
      [["Bir kesimli zakovka", "1", "τ = F/(n·πd²/4)"],
       ["Ikki kesimli zakovka", "2", "τ = F/(2n·πd²/4)"],
       ["Burchakli payvand chok", "1", "τ = F/(0,7k·L)"],
       ["Shpon", "1", "τ = 2T/(d·b·l)"]])
''',
                parameters=[
                    p("d", "Zakovka diametri d", 6.0, 40.0, 16.0, 1.0, "mm"),
                    p("delta", "Eng yupqa list", 3.0, 40.0, 10.0, 1.0, "mm"),
                    p("F", "Kuch F", 10000.0, 1000000.0, 180000.0, 5000.0, "N"),
                    p("tau_allow", "[τ]", 30.0, 300.0, 100.0, 10.0, "MPa"),
                    p("sez_allow", "[σ_ez]", 50.0, 600.0, 240.0, 10.0, "MPa"),
                    p("i", "Kesilish tekisliklari", 1.0, 3.0, 1.0, 1.0, "dona"),
                ],
                expected_output="G = 76,9 GPa, n_kesilish = 8,95, n_ezilish = 4,69, n = 9",
            ),
            visualization=vis(
                "Toza siljish va birikma sxemasi",
                "React/SVG",
                "Chapda: kvadrat element siljishda parallelogrammga aylanadi, "
                "burchak o'zgarishi $\\gamma$ belgilangan. O'ngda: zakovkali birikma "
                "kesimi, kesilish tekisligi va ezilish zonasi ajratilgan.",
                "React/SVG: siljish deformatsiyasini bo'rttirib ko'rsatish shart "
                "($\\gamma$ real holda $10^{-3}$ rad). Birikma sxemasida kesilish va "
                "ezilish zonalarini turli rang bilan ajratish ikki shartning "
                "farqini aniq ko'rsatadi.",
            ),
            interpretation=(
                "Ikki egri chiziqning kesishishi optimal diametrni beradi: "
                "undan kichikda kesilish, kattada ezilish hal qiluvchi. Optimal "
                "nuqtada ikkala material to'liq ishlatiladi. Elastik doimiylar "
                "jadvali esa muhim chegaraviy holni ko'rsatadi: $\\nu \\to 0{,}5$ "
                "(rezina) da material amalda siqilmaydi va $G \\to E/3$."
            ),
            common_mistakes=[
                "Ezilish yuzasini $\\pi d\\delta$ deb olish — u shartli ravishda "
                "$d\\delta$ (proyeksiya) sifatida hisoblanadi.",
                "Eng yupqa emas, qalin listni ezilish hisobida ishlatish.",
                "Ikki kesimli zakovkada kesilish yuzasini ikkiga ko'paytirmaslik.",
                "$G$ ni mustaqil o'lchanadigan doimiy deb olish — izotrop materialda "
                "u $E$ va $\\nu$ orqali aniqlanadi.",
            ],
            quiz=[
                q("Nima uchun izotrop materialda faqat ikkita mustaqil elastik "
                  "doimiy bor?",
                  "Izotroplik sababli barcha yo'nalishlar teng huquqli; $G$ toza "
                  "siljishni 45° o'qlarda ko'rish orqali $E$ va $\\nu$ ga bog'lanadi.",
                  "konseptual"),
                q("$E = 200$ GPa, $\\nu = 0{,}3$. $G$ ni toping.",
                  "$G = 200/(2\\cdot1{,}3) = 76{,}9$ GPa.", "hisob"),
                q("Urinma kuchlanishlar juftligi qonuni qayerdan kelib chiqadi?",
                  "Elementar hajmning moment muvozanatidan: $\\sum M = 0$ sharti "
                  "$\\tau_{xy} = \\tau_{yx}$ ni beradi.", "konseptual"),
                q("$F = 100$ kN, $d = 20$ mm, ikki kesimli, $n = 4$. $\\tau$?",
                  "$A_1 = 314{,}2$ mm²; $\\tau = 100\\,000/(4\\cdot2\\cdot314{,}2) = 39{,}8$ MPa.",
                  "hisob"),
                q("Kodda ikki egri chiziqning kesishishi nimani anglatadi?",
                  "Kesilish va ezilish shartlari bir xil zakovkalar sonini talab "
                  "qiladigan optimal diametrni — bu yerda ikkala material to'liq "
                  "ishlatiladi.", "kod"),
            ],
            bridge_to_next=(
                "Toza siljish o'rganildi. Endi uning eng muhim amaliy ko'rinishi — "
                "valning buralishiga o'tamiz."
            ),
            research_extension=(
                "Ko'p zakovkali birikmada kuch taqsimotini modellashtiring: "
                "listlarni elastik deb hisoblab, har bir zakovkani prujina sifatida "
                "oling. Chiziqli tenglamalar tizimini yeching va chekka zakovkalar "
                "qanchalik ko'p yuk olishini aniqlang. Zakovkalar soni ortganda "
                "notekislik qanday o'zgaradi?"
            ),
        ),
    ),
    Topic(
        id="mq-10",
        subject_id=S,
        module_id=M,
        order=10,
        title="Buralish: valdagi urinma kuchlanishlar va burilish burchagi",
        description=(
            "Dumaloq valning buralishi, tekis kesimlar gipotezasi, urinma "
            "kuchlanishlar taqsimoti, buralish burchagi va bikrlik hisobi."
        ),
        learning_objective=(
            "Valdagi urinma kuchlanish va burilish burchagini hisoblash, valni "
            "mustahkamlik va bikrlik bo'yicha loyihalash."
        ),
        prerequisites=["mq-09", "mq-08"],
        mathematical_core=(
            "$\\tau = T\\rho/I_p$, differensial tenglama $d\\varphi/dx = T/(GI_p)$, "
            "integrallash."
        ),
        engineering_application=(
            "Transmissiya vallari, prujinalar, buralish tebranishlari, "
            "burg'ulash quvurlari."
        ),
        computational_component=(
            "Pog'onali val hisobi: epyuralar, kuchlanishlar va burilish burchagi."
        ),
        visualization_component=(
            "Kesim bo'ylab chiziqli $\\tau$ taqsimoti; buralgan val deformatsiyasi."
        ),
        research_extension=(
            "Nima uchun dumaloq bo'lmagan kesimlarda tekis kesimlar gipotezasi "
            "buziladi? Deplanatsiya hodisasi (tmm-18 ga ko'prik)."
        ),
        difficulty="asosiy",
        previous_link=(
            "mq-09 dagi siljish deformatsiyasi bu yerda konkret geometriyaga "
            "qo'llanadi. mq-08 dagi qutb inersiya momenti $I_p$ asosiy rol o'ynaydi."
        ),
        next_topic="mq-11",
        estimated_minutes=90,
        tags=["buralish", "val", "urinma kuchlanish"],
        lesson=Lesson(
            physical_problem=(
                "Avtomobil transmissiya vali dvigateldan g'ildiraklarga moment "
                "uzatadi. Val juda yupqa bo'lsa — buraladi va sinadi; juda qalin "
                "bo'lsa — og'ir va qimmat. Bundan tashqari val ortiqcha buralib "
                "ketmasligi kerak, aks holda boshqarish aniqligi yo'qoladi. Ikkala "
                "shartni birgalikda qanoatlantiruvchi diametr qanday topiladi?"
            ),
            concepts=[
                c("Buruvchi moment $T$", "Val o'qi atrofidagi ichki moment. "
                  "$T = 9550P/n$ (P — kW, n — ayl/min, T — N·m)."),
                c("Tekis kesimlar gipotezasi (buralishda)", "Dumaloq kesimlar tekis "
                  "qoladi va faqat o'z tekisligida buriladi. Faqat dumaloq kesim "
                  "uchun aniq o'rinli."),
                c("Qutb inersiya momenti", "$I_p = \\pi d^4/32$ — buralishga "
                  "qarshilikning geometrik o'lchovi."),
                c("Qutb qarshilik momenti", "$W_p = I_p/r = \\pi d^3/16$ — "
                  "mustahkamlik hisobida ishlatiladi."),
                c("Nisbiy burilish burchagi", "$\\theta = d\\varphi/dx = T/(GI_p)$ "
                  "[rad/m] — bikrlik mezoni."),
            ],
            derivation=[
                d("1-qadam. Kinematika: tekis kesimlar gipotezasidan",
                  r"\gamma = \rho\frac{d\varphi}{dx} = \rho\theta",
                  "Ikki qo'shni kesim $d\\varphi$ ga buriladi; radiusi $\\rho$ "
                  "bo'lgan nuqtaning siljishi $\\rho\\,d\\varphi$, deformatsiya esa "
                  "uni $dx$ ga bo'lgan nisbat. Siljish deformatsiyasi radiusga "
                  "chiziqli bog'liq."),
                d("2-qadam. Guk qonuni orqali kuchlanish",
                  r"\tau = G\gamma = G\rho\theta",
                  "Kuchlanish ham radiusga chiziqli: markazda nol, sirtda maksimal. "
                  "Bu — cho'zilishdagi bir tekis taqsimotdan tubdan farq."),
                d("3-qadam. Statik ekvivalentlikdan $\\theta$ ni topish",
                  r"T = \int_A\tau\rho\,dA = G\theta\int_A\rho^2dA = G\theta I_p "
                  r"\;\Rightarrow\; \boxed{\;\theta = \frac{T}{GI_p}\;}",
                  "$GI_p$ — buralish bikrligi. U cho'zilishdagi $EA$ ning analogi."),
                d("4-qadam. Kuchlanish formulasi",
                  r"\boxed{\;\tau = \frac{T\rho}{I_p},\qquad "
                  r"\tau_{max} = \frac{T r}{I_p} = \frac{T}{W_p}\;}",
                  "$\\theta$ ni kuchlanish ifodasiga qo'yamiz. Bu — mq-13 dagi "
                  "egilish formulasi $\\sigma = My/I$ bilan bir xil strukturaga ega."),
                d("5-qadam. Burilish burchagi",
                  r"\varphi = \int_0^L\frac{T(x)}{GI_p(x)}dx = \frac{TL}{GI_p}",
                  "Oxirgi shakl $T$ va $I_p$ o'zgarmas bo'lganda. Pog'onali valda "
                  "uchastkalar bo'yicha yig'indi."),
            ],
            formula_meaning=(
                "$\\tau = T\\rho/I_p$ formulasidagi chiziqli taqsimot muhim xulosaga "
                "olib keladi: val markazidagi material deyarli ishlamaydi. Shuning "
                "uchun quvursimon val to'la valdan ancha samarali — massaning 30 % "
                "ini olib tashlab, qarshilikning atigi 6 % i yo'qotiladi. "
                "$W_p = \\pi d^3/16$ dagi kub esa diametr ta'sirining kuchini "
                "ko'rsatadi: diametrni 20 % oshirish qarshilikni 73 % oshiradi."
            ),
            equations=[
                eq(r"\tau = \frac{T\rho}{I_p},\quad \tau_{max} = \frac{T}{W_p}",
                   "Buralishdagi urinma kuchlanish.", "Buralish formulasi"),
                eq(r"\varphi = \frac{TL}{GI_p}", "Burilish burchagi.", "Burilish burchagi"),
                eq(r"I_p = \frac{\pi d^4}{32},\quad W_p = \frac{\pi d^3}{16}",
                   "Dumaloq kesim uchun geometrik tavsiflar.", "Geometrik tavsiflar"),
                eq(r"T = 9550\frac{P}{n}", "Quvvat va aylanishlar sonidan moment "
                   "($P$ — kW, $n$ — ayl/min).", "Moment hisobi"),
            ],
            conditions=(
                "Formulalar faqat dumaloq (to'la yoki quvursimon) kesim uchun aniq. "
                "To'rtburchak va boshqa kesimlarda kesimlar tekis qolmaydi "
                "(deplanatsiya) va Sen-Venan nazariyasi kerak (tmm-18). Bikrlik "
                "sharti odatda $[\\theta] = 0{,}25...1{,}0$ deg/m; mas'uliyatli "
                "vallarda qat'iyroq."
            ),
            worked_example=WorkedExample(
                statement=(
                    "Transmissiya vali $P = 45$ kW quvvatni $n = 600$ ayl/min da "
                    "uzatadi. Material po'lat: $[\\tau] = 40$ MPa, $G = 80$ GPa, "
                    "$[\\theta] = 0{,}5$ deg/m. To'la va quvursimon "
                    "($d_{ich}/d_{tash} = 0{,}7$) val diametrlarini aniqlang va "
                    "massani taqqoslang."
                ),
                given=[r"P = 45\ \text{kW},\; n = 600\ \text{ayl/min}",
                       r"[\tau] = 40\ \text{MPa},\; G = 8\cdot10^{10}\ \text{Pa}",
                       r"[\theta] = 0{,}5\ \text{deg/m}"],
                steps=[
                    st(r"T = 9550\frac{P}{n} = 9550\cdot\frac{45}{600} = 716{,}3\ \text{N·m}",
                       "Buruvchi moment."),
                    st(r"W_p \ge \frac{T}{[\tau]} = \frac{716{,}3}{40\cdot10^6} = 1{,}79\cdot10^{-5}\ \text{m}^3 "
                       r"\Rightarrow d \ge \sqrt[3]{\frac{16\cdot 1{,}79\cdot10^{-5}}{\pi}}",
                       "Mustahkamlik shartidan."),
                    st(r"d \ge \sqrt[3]{9{,}12\cdot10^{-5}} = 0{,}0450\ \text{m} = 45{,}0\ \text{mm}",
                       "Mustahkamlik bo'yicha kerakli diametr."),
                    st(r"[\theta] = 0{,}5\frac{\pi}{180} = 8{,}73\cdot10^{-3}\ \text{rad/m};\quad "
                       r"I_p \ge \frac{T}{G[\theta]} = \frac{716{,}3}{8\cdot10^{10}\cdot 8{,}73\cdot10^{-3}}",
                       "Bikrlik shartidan."),
                    st(r"I_p \ge 1{,}025\cdot10^{-6}\ \text{m}^4 \Rightarrow "
                       r"d \ge \sqrt[4]{\frac{32\cdot 1{,}025\cdot10^{-6}}{\pi}} = 0{,}0566\ \text{m} = 56{,}6\ \text{mm}",
                       "Bikrlik bo'yicha — mustahkamlikdan 26 % katta! Hal qiluvchi shart — bikrlik."),
                    st(r"\text{Quvur: } d_t^4(1-0{,}7^4) \ge d_{to'la}^4 \Rightarrow "
                       r"d_t = \frac{56{,}6}{\sqrt[4]{0{,}7599}} = 60{,}6\ \text{mm};\quad "
                       r"\frac{m_{quvur}}{m_{to'la}} = \frac{60{,}6^2(1-0{,}49)}{56{,}6^2} = 0{,}584",
                       "Quvursimon val 42 % yengil, tashqi diametri esa atigi 7 % katta."),
                ],
                answer=(
                    "To'la val: $d = 57$ mm (bikrlik hal qiluvchi); quvursimon: "
                    "$d_{tash} = 61$ mm, $d_{ich} = 42$ mm, massa 42 % kam."
                ),
                engineering_note=(
                    "Bikrlik sharti mustahkamlikdan qattiqroq bo'lib chiqdi — bu "
                    "uzun vallar uchun tipik holat. Quvursimon val esa "
                    "materialning samarali ishlatilishini ko'rsatadi: markazdagi "
                    "kam yuklangan material olib tashlanadi. Aviatsiya va "
                    "avtosport transmissiyalarida aynan shunday vallar ishlatiladi."
                ),
            ),
            computation=Computation(
                caption=(
                    "Val hisobi: quvvat, aylanishlar soni va geometriyani o'zgartirib, "
                    "mustahkamlik va bikrlik shartlarini taqqoslang."
                ),
                code='''"""Buralish: val hisobi, epyuralar va quvursimon kesim samaradorligi."""
import numpy as np
from labkit import PARAMS, note, series, table, value

P = float(PARAMS.get("P", 45.0))            # quvvat, kW
n_rpm = float(PARAMS.get("n_rpm", 600.0))   # ayl/min
tau_allow = float(PARAMS.get("tau_allow", 40.0))*1e6   # Pa
theta_allow = float(PARAMS.get("theta_allow", 0.5))    # deg/m
alpha = float(PARAMS.get("alpha", 0.7))     # d_ich/d_tash
G = float(PARAMS.get("G", 80e9))            # Pa
L = 2.0
rho_steel = 7850.0

T = 9550*P/n_rpm
theta_rad = np.radians(theta_allow)
value("Buruvchi moment T", T, "N·m")

# Mustahkamlik sharti
Wp_req = T/tau_allow
d_strength = (16*Wp_req/np.pi)**(1/3)
# Bikrlik sharti
Ip_req = T/(G*theta_rad)
d_stiffness = (32*Ip_req/np.pi)**0.25

value("d (mustahkamlikdan)", d_strength*1000, "mm")
value("d (bikrlikdan)", d_stiffness*1000, "mm")
d = max(d_strength, d_stiffness)
value("Qabul qilingan d", d*1000, "mm")
note(f"Hal qiluvchi shart: {'BIKRLIK' if d_stiffness > d_strength else 'MUSTAHKAMLIK'}")

Ip = np.pi*d**4/32
Wp = np.pi*d**3/16
value("I_p", Ip*1e8, "cm⁴")
value("τ_max", T/Wp/1e6, "MPa")
value("θ", np.degrees(T/(G*Ip)), "deg/m")
value("φ (L=2 m)", np.degrees(T*L/(G*Ip)), "deg")

# Kesim bo'ylab kuchlanish taqsimoti
r = np.linspace(0, d/2, 100)
series("τ(ρ) — to'la val", (r*1000).tolist(), (T*r/Ip/1e6).tolist(),
       xlabel="ρ, mm", ylabel="τ, MPa")

# Quvursimon val
d_out = d/(1-alpha**4)**0.25
d_in = alpha*d_out
Ip_t = np.pi*(d_out**4 - d_in**4)/32
A_solid = np.pi*d**2/4
A_tube = np.pi*(d_out**2 - d_in**2)/4
value("Quvur d_tashqi", d_out*1000, "mm")
value("Quvur d_ichki", d_in*1000, "mm")
value("Massa nisbati (quvur/to'la)", A_tube/A_solid, "—")
value("Massa tejash", 100*(1-A_tube/A_solid), "%")

r_t = np.linspace(d_in/2, d_out/2, 60)
series("τ(ρ) — quvursimon", (r_t*1000).tolist(), (T*r_t/Ip_t/1e6).tolist(),
       xlabel="ρ, mm", ylabel="τ, MPa")

# alpha ning massa tejashga ta'siri
aa = np.linspace(0.0, 0.92, 100)
d_o = d/(1-aa**4)**0.25
mass_ratio = (d_o**2*(1-aa**2))/d**2
series("Massa nisbati(α)", aa.tolist(), mass_ratio.tolist(),
       xlabel="α = d_ich/d_tash", ylabel="m_quvur/m_to'la")
note(f"α = 0,8 da massa tejash {100*(1-mass_ratio[np.argmin(abs(aa-0.8))]):.1f} %, "
     f"lekin tashqi diametr {d/(1-0.8**4)**0.25/d:.2f} marta ortadi.")

# Pog'onali val: epyuralar
segs = [(0.8, T), (0.7, T*0.6), (0.5, T*0.6)]      # (uzunlik, moment)
x_all, T_all, phi_all = [], [], []
x0, phi0 = 0.0, 0.0
for Li, Ti in segs:
    xs = np.linspace(x0, x0+Li, 50)
    x_all += xs.tolist()
    T_all += [Ti]*50
    phi_all += (phi0 + np.degrees(Ti*(xs-x0)/(G*Ip))).tolist()
    phi0 = phi_all[-1]
    x0 += Li
series("Buruvchi moment T(x)", x_all, T_all, xlabel="x, m", ylabel="T, N·m")
series("Burilish burchagi φ(x)", x_all, phi_all, xlabel="x, m", ylabel="φ, deg")

table("Quvvat va aylanishlar soniga bog'liqlik",
      ["P, kW", "n, ayl/min", "T, N·m", "d, mm"],
      [[float(Pi), float(ni), float(9550*Pi/ni),
        float((32*(9550*Pi/ni)/(np.pi*G*theta_rad))**0.25*1000)]
       for Pi, ni in [(15, 600), (45, 600), (45, 1500), (100, 1500)]])
''',
                parameters=[
                    p("P", "Quvvat P", 1.0, 500.0, 45.0, 1.0, "kW"),
                    p("n_rpm", "Aylanishlar soni", 50.0, 6000.0, 600.0, 50.0, "ayl/min"),
                    p("tau_allow", "[τ]", 10.0, 200.0, 40.0, 5.0, "MPa"),
                    p("theta_allow", "[θ]", 0.1, 3.0, 0.5, 0.05, "deg/m"),
                    p("alpha", "α = d_ich/d_tash", 0.0, 0.92, 0.7, 0.02, "—"),
                    p("G", "Siljish moduli G", 2e10, 1.2e11, 80e9, 5e9, "Pa"),
                ],
                expected_output="T = 716,3 N·m; d_mustahkamlik = 45,0 mm; d_bikrlik = 56,6 mm",
            ),
            visualization=vis(
                "Buralishdagi kuchlanish taqsimoti",
                "Manim",
                "Val buraladi, kesimda urinma kuchlanish strelkalari radius bo'ylab "
                "chiziqli o'sadi; markazda nol. Quvursimon val bilan yonma-yon "
                "taqqoslash: kam yuklangan markaz olib tashlanadi.",
                "Manim: valning burilishi va kesim bo'ylab kuchlanish taqsimotining "
                "'o'sishi' animatsiyada juda aniq ko'rinadi. React/SVG da esa "
                "$\\tau(\\rho)$ chiziqli grafigi va to'la/quvursimon taqqoslash "
                "beriladi.",
            ),
            interpretation=(
                "$\\tau(\\rho)$ chiziqli grafigi markazdagi materialning deyarli "
                "ishlamasligini ko'rsatadi. Massa nisbati grafigi esa "
                "$\\alpha = 0{,}7...0{,}8$ oralig'ida optimal yechim borligini "
                "beradi: 40–50 % massa tejash, tashqi diametrning 7–15 % "
                "oshishi evaziga. Jadval esa aylanishlar sonining muhimligini "
                "ko'rsatadi: bir xil quvvatda 2,5 marta tez aylanuvchi val "
                "1,26 marta yupqaroq bo'lishi mumkin."
            ),
            common_mistakes=[
                "$I_p$ o'rniga $I_x$ ni ishlatish — buralishda qutb momenti kerak.",
                "$[\\theta]$ ni gradusda qoldirib, radian bilan aralashtirish.",
                "Dumaloq bo'lmagan kesimlarga ushbu formulalarni qo'llash.",
                "Faqat mustahkamlikni tekshirib, bikrlikni unutish — uzun vallarda "
                "bikrlik odatda hal qiluvchi.",
            ],
            quiz=[
                q("Nima uchun buralishda kuchlanish markazda nolga teng?",
                  "Chunki $\\gamma = \\rho\\theta$: markazda ($\\rho = 0$) siljish "
                  "deformatsiyasi yo'q, demak kuchlanish ham yo'q.", "konseptual"),
                q("Val diametrini 20 % oshirsak, $W_p$ va $I_p$ qanday o'zgaradi?",
                  "$W_p \\propto d^3$: $1{,}2^3 = 1{,}73$ marta; "
                  "$I_p \\propto d^4$: $1{,}2^4 = 2{,}07$ marta.", "hisob"),
                q("$P = 30$ kW, $n = 1000$ ayl/min. $T$ ni toping.",
                  "$T = 9550\\cdot30/1000 = 286{,}5$ N·m.", "hisob"),
                q("Nima uchun quvursimon val samaraliroq?",
                  "Markazdagi material kam kuchlangan ($\\tau \\propto \\rho$), uni "
                  "olib tashlash massani sezilarli kamaytiradi, qarshilikni esa "
                  "ozgina.", "talqin"),
                q("Kodda `d/(1-alpha**4)**0.25` formulasi qayerdan kelgan?",
                  "Quvursimon val to'la val bilan bir xil $I_p$ berishi sharti: "
                  "$d_t^4(1-\\alpha^4) = d^4$ dan $d_t$ topiladi.", "kod"),
            ],
            bridge_to_next=(
                "Statik aniq val hisoblandi. Keyingi mavzuda statik aniqmas "
                "buralish masalalari va valning to'liq loyihalash hisobini ko'ramiz."
            ),
            research_extension=(
                "Optimal val kesimini toping: berilgan $T$ va massa cheklovida "
                "$\\alpha$ ni optimallashtiring, bunda ustuvorlik (yupqa devorli "
                "quvurning lokal ustuvorligi) ham hisobga olinsin. Devor "
                "qalinligining kritik nisbatini aniqlang — undan yupqa quvur "
                "buralishda burishib ketadi (pq-25 bilan bog'liq)."
            ),
            manim=manim(
                scene="TorsionScene",
                module="manim/scenes/mq_torsion.py",
                title="Val buralishi va kuchlanish taqsimoti",
                summary="Val bosqichma-bosqich buraladi, kesimdagi urinma kuchlanish "
                        "strelkalari radius bo'ylab chiziqli o'sadi.",
            ),
        ),
    ),
    Topic(
        id="mq-11",
        subject_id=S,
        module_id=M,
        order=11,
        title="Statik aniqmas buralish masalalari va valni kompleks loyihalash",
        description=(
            "Ikki tomondan qotirilgan val, moslik sharti buralishda, "
            "ratsional kesim tanlash va buralish tebranishlariga kirish."
        ),
        learning_objective=(
            "Statik aniqmas buralish masalasini yechish va valni mustahkamlik, "
            "bikrlik hamda dinamik shartlar bo'yicha loyihalash."
        ),
        prerequisites=["mq-10", "mq-06"],
        mathematical_core=(
            "Moslik sharti $\\sum\\varphi_i = 0$, chiziqli tenglamalar tizimi, "
            "buralish tebranishlari chastotasi."
        ),
        engineering_application=(
            "Ko'p tayanchli vallar, transmissiya, buralish tebranishlari "
            "so'ndirgichlari, dvigatel tirsakli vali."
        ),
        computational_component=(
            "Statik aniqmas valni yechish va buralish tebranishlari chastotasini "
            "hisoblash."
        ),
        visualization_component=(
            "Statik aniqmas val epyuralari va burilish burchagi diagrammasi."
        ),
        research_extension=(
            "Tirsakli valning buralish tebranishlari: nima uchun dvigatelda "
            "buralish so'ndirgichi (damper) kerak?"
        ),
        difficulty="murakkab",
        previous_link=(
            "mq-06 dagi moslik sharti g'oyasi buralishga ko'chiriladi: "
            "$\\Delta L$ o'rniga $\\varphi$."
        ),
        next_topic="mq-12",
        estimated_minutes=90,
        tags=["statik aniqmas", "val", "buralish tebranishi"],
        lesson=Lesson(
            physical_problem=(
                "Val ikki tomondan qotirilgan va o'rtasiga moment qo'yilgan. "
                "Reaktiv momentlar qanday taqsimlanadi? Muvozanat tenglamasi bitta, "
                "noma'lum ikkita — yetmaydi. Yechim deformatsiyalardan keladi: "
                "valning umumiy burilishi nolga teng bo'lishi kerak. Bundan tashqari, "
                "aylanuvchi val buralish tebranishlariga tushishi mumkin — va bu "
                "rezonans dvigatel valini sindirishi mumkin."
            ),
            concepts=[
                c("Statik aniqmaslik buralishda", "Noma'lum reaktiv momentlar soni "
                  "muvozanat tenglamalari sonidan ko'p."),
                c("Moslik sharti", "$\\sum\\varphi_i = 0$ — qotirilgan uchlar orasidagi "
                  "umumiy burilish nolga teng."),
                c("Bikrliklar bo'yicha taqsimot", "Moment uchastkalarga "
                  "$GI_p/L$ ga proporsional taqsimlanadi."),
                c("Buralish tebranishlari", "Val — prujina, disklar — massalar; "
                  "$\\omega = \\sqrt{GI_p/(JL)}$."),
                c("Ratsional loyihalash", "Mustahkamlik, bikrlik va rezonansdan "
                  "qochish shartlarini birgalikda qanoatlantirish."),
            ],
            derivation=[
                d("1-qadam. Muvozanat tenglamasi",
                  r"T_A + T_B = T_0",
                  "Ikki reaktiv moment yig'indisi tashqi momentga teng. "
                  "Bitta tenglama, ikkita noma'lum — statik aniqmas."),
                d("2-qadam. Moslik sharti",
                  r"\varphi_{AB} = 0 \;\Rightarrow\; \frac{T_Aa}{GI_p} - \frac{T_Bb}{GI_p} = 0",
                  "A dan B gacha burilish burchagi nolga teng (ikkala uch qotirilgan). "
                  "Uchastkalarda momentlar turli ishorada."),
                d("3-qadam. Tizimni yechish",
                  r"T_Aa = T_Bb \;\text{va}\; T_A+T_B = T_0 \;\Rightarrow\; "
                  r"\boxed{\;T_A = T_0\frac{b}{L},\quad T_B = T_0\frac{a}{L}\;}",
                  "Moment uzoqroq uchastkaga kamroq tushadi — chunki u 'yumshoqroq'. "
                  "Bu statik aniqmas tizimlarning umumiy qonuni: yuk bikrliklarga "
                  "proporsional taqsimlanadi."),
                d("4-qadam. Buralish tebranishlari chastotasi",
                  r"J\ddot\varphi + k_T\varphi = 0,\quad k_T = \frac{GI_p}{L} "
                  r"\;\Rightarrow\; \omega = \sqrt{\frac{GI_p}{JL}}",
                  "Val — buralish prujinasi, disk — inersiya momenti $J$ bo'lgan "
                  "massa. nm-25 dagi $\\omega = \\sqrt{k/m}$ ning aylanma analogi."),
            ],
            formula_meaning=(
                "$T_A/T_B = b/a$ — statik aniqmas tizimda yuk bikrlikka proporsional "
                "taqsimlanadi degan universal qoidaning konkret ko'rinishi. "
                "Buralish tebranishi chastotasi esa dvigatel loyihalashda hal "
                "qiluvchi: agar u dvigatel garmonikalaridan biriga to'g'ri kelsa, "
                "rezonans valni sindiradi. Shuning uchun tirsakli vallarda "
                "buralish so'ndirgichlari o'rnatiladi."
            ),
            equations=[
                eq(r"T_A = T_0\frac{b}{L},\quad T_B = T_0\frac{a}{L}",
                   "Ikki tomondan qotirilgan valda reaktiv momentlar.", "Moment taqsimoti"),
                eq(r"k_T = \frac{GI_p}{L}", "Valning buralish bikrligi.", "Buralish bikrligi"),
                eq(r"\omega = \sqrt{\frac{GI_p}{JL}}", "Buralish tebranishi chastotasi.",
                   "Tebranish chastotasi"),
            ],
            conditions=(
                "Moslik sharti tayanchlarning to'liq qotirilganini nazarda tutadi. "
                "Real podshipniklar biroz burilishga ruxsat beradi — bu moment "
                "taqsimotini o'zgartiradi. Buralish tebranishlari hisobida "
                "valning o'z inersiya momenti disklarникига nisbatan kichik deb "
                "qabul qilinadi (aks holda taqsimlangan massali model kerak)."
            ),
            worked_example=WorkedExample(
                statement=(
                    "Val ikki tomondan qotirilgan, $L = 1{,}2$ m, $d = 50$ mm, "
                    "$G = 80$ GPa. A dan $a = 0{,}5$ m masofada $T_0 = 900$ N·m "
                    "moment qo'yilgan. (a) Reaktiv momentlar; (b) maksimal urinma "
                    "kuchlanish; (c) moment qo'yilgan kesimning burilish burchagi; "
                    "(d) agar B uchiga $J = 0{,}08$ kg·m² disk o'rnatilsa, buralish "
                    "tebranishi chastotasi."
                ),
                given=[r"L = 1{,}2\ \text{m},\; a = 0{,}5\ \text{m},\; b = 0{,}7\ \text{m}",
                       r"d = 0{,}05\ \text{m},\; G = 8\cdot10^{10}\ \text{Pa},\; T_0 = 900\ \text{N·m}"],
                steps=[
                    st(r"I_p = \frac{\pi d^4}{32} = \frac{3{,}1416\cdot 6{,}25\cdot10^{-6}}{32} = "
                       r"6{,}136\cdot10^{-7}\ \text{m}^4",
                       "Qutb inersiya momenti."),
                    st(r"T_A = T_0\frac{b}{L} = 900\cdot\frac{0{,}7}{1{,}2} = 525\ \text{N·m}",
                       "A tomondagi reaktiv moment."),
                    st(r"T_B = T_0\frac{a}{L} = 900\cdot\frac{0{,}5}{1{,}2} = 375\ \text{N·m}",
                       "B tomondagi. Tekshirish: $525+375 = 900$ ✓"),
                    st(r"W_p = \frac{\pi d^3}{16} = \frac{3{,}1416\cdot 1{,}25\cdot10^{-4}}{16} = "
                       r"2{,}454\cdot10^{-5}\ \text{m}^3;\quad "
                       r"\tau_{max} = \frac{525}{2{,}454\cdot10^{-5}} = 21{,}4\ \text{MPa}",
                       "Maksimal kuchlanish AC uchastkasida (moment kattaroq)."),
                    st(r"\varphi_C = \frac{T_Aa}{GI_p} = \frac{525\cdot 0{,}5}{8\cdot10^{10}\cdot 6{,}136\cdot10^{-7}} = "
                       r"\frac{262{,}5}{49\,088} = 5{,}35\cdot10^{-3}\ \text{rad} = 0{,}306^\circ",
                       "Moment qo'yilgan kesimning burilishi."),
                    st(r"k_T = \frac{GI_p}{L} = \frac{49\,088}{1{,}2} = 40\,907\ \text{N·m/rad};\quad "
                       r"\omega = \sqrt{\frac{40\,907}{0{,}08}} = 715\ \text{rad/s} = 114\ \text{Hz}",
                       "Buralish tebranishi chastotasi."),
                ],
                answer=(
                    "$T_A = 525$ N·m, $T_B = 375$ N·m; $\\tau_{max} = 21{,}4$ MPa; "
                    "$\\varphi_C = 0{,}306°$; $f = 114$ Hz."
                ),
                engineering_note=(
                    "114 Hz = 6840 ayl/min ekvivalenti. Agar dvigatel 3420 ayl/min da "
                    "ishlasa, ikkinchi garmonika (2×) aynan rezonansga to'g'ri keladi — "
                    "bu xavfli. Yechim: val bikrligini yoki disk inersiyasini "
                    "o'zgartirish, yoki buralish so'ndirgichi o'rnatish."
                ),
            ),
            computation=Computation(
                caption=(
                    "Statik aniqmas val: moment joylashuvini o'zgartirib, "
                    "taqsimotni va rezonans xavfini baholang."
                ),
                code='''"""Statik aniqmas buralish va buralish tebranishlari."""
import numpy as np
from labkit import PARAMS, note, series, table, value

L = float(PARAMS.get("L", 1.2))          # val uzunligi, m
a = float(PARAMS.get("a", 0.5))          # moment koordinatasi, m
d = float(PARAMS.get("d", 50.0))*1e-3    # diametr, m
T0 = float(PARAMS.get("T0", 900.0))      # qo'yilgan moment, N*m
G = float(PARAMS.get("G", 80e9))         # Pa
J_disk = float(PARAMS.get("J", 0.08))    # disk inersiya momenti, kg*m^2

b = L - a
Ip = np.pi*d**4/32
Wp = np.pi*d**3/16

# Moslik sharti orqali yechim
T_A = T0*b/L
T_B = T0*a/L
value("Qutb inersiya momenti I_p", Ip*1e8, "cm⁴")
value("Reaktiv moment T_A", T_A, "N·m")
value("Reaktiv moment T_B", T_B, "N·m")
note(f"Muvozanat tekshiruvi: T_A + T_B = {T_A+T_B:.3f} N·m (T₀ = {T0} N·m) ✓")

# Epyuralar
x = np.linspace(0, L, 400)
T_x = np.where(x < a, T_A, -T_B)
phi_x = np.where(x < a, T_A*x/(G*Ip), T_A*a/(G*Ip) - T_B*(x-a)/(G*Ip))
series("Buruvchi moment T(x)", x.tolist(), T_x.tolist(), xlabel="x, m", ylabel="T, N·m")
series("Burilish burchagi φ(x)", x.tolist(), np.degrees(phi_x).tolist(),
       xlabel="x, m", ylabel="φ, deg")
series("Kuchlanish τ(x)", x.tolist(), (np.abs(T_x)/Wp/1e6).tolist(),
       xlabel="x, m", ylabel="τ, MPa")

value("τ_max", float(np.max(np.abs(T_x))/Wp/1e6), "MPa")
value("φ_C (moment kesimida)", float(np.degrees(T_A*a/(G*Ip))), "deg")
note(f"Chegaraviy tekshiruv: φ(L) = {np.degrees(phi_x[-1]):.2e} deg (nol bo'lishi kerak) ✓")

# Buralish tebranishlari
k_T = G*Ip/L
omega = np.sqrt(k_T/J_disk)
f_hz = omega/(2*np.pi)
value("Buralish bikrligi k_T", k_T/1000, "kN·m/rad")
value("Xususiy chastota ω", omega, "rad/s")
value("Chastota f", f_hz, "Hz")
value("Kritik aylanish (1-garmonika)", f_hz*60, "ayl/min")

# Rezonans xaritasi: dvigatel garmonikalari
n_work = np.linspace(500, 6000, 300)
series("1-garmonika", n_work.tolist(), (n_work/60).tolist(),
       xlabel="n, ayl/min", ylabel="Chastota, Hz")
series("2-garmonika", n_work.tolist(), (2*n_work/60).tolist(),
       xlabel="n, ayl/min", ylabel="Chastota, Hz")
series("Xususiy chastota", n_work.tolist(), np.full_like(n_work, f_hz).tolist(),
       xlabel="n, ayl/min", ylabel="Chastota, Hz")
for k in (1, 2, 3):
    n_res = f_hz*60/k
    if 500 <= n_res <= 6000:
        note(f"{k}-garmonika rezonansi: n = {n_res:.0f} ayl/min — bu zonadan qochish kerak!")

# Moment joylashuvining taqsimotga ta'siri
aa = np.linspace(0.05, L-0.05, 100)
series("T_A(a)", aa.tolist(), (T0*(L-aa)/L).tolist(), xlabel="a, m", ylabel="T_A, N·m")
series("T_B(a)", aa.tolist(), (T0*aa/L).tolist(), xlabel="a, m", ylabel="T_B, N·m")

table("Statik aniq va aniqmas valni taqqoslash",
      ["Sxema", "T_max", "τ_max, MPa", "φ_max, deg"],
      [["Bir uchi qotirilgan", float(T0), float(T0/Wp/1e6), float(np.degrees(T0*a/(G*Ip)))],
       ["Ikki uchi qotirilgan", float(max(T_A, T_B)), float(max(T_A, T_B)/Wp/1e6),
        float(np.degrees(T_A*a/(G*Ip)))]])
note("Ikki tomondan qotirish maksimal momentni va burilishni sezilarli kamaytiradi — "
     "statik aniqmaslikning asosiy foydasi.")
''',
                parameters=[
                    p("L", "Val uzunligi L", 0.2, 5.0, 1.2, 0.05, "m"),
                    p("a", "Moment koordinatasi a", 0.05, 4.95, 0.5, 0.05, "m"),
                    p("d", "Val diametri d", 10.0, 200.0, 50.0, 2.0, "mm"),
                    p("T0", "Qo'yilgan moment T₀", 50.0, 10000.0, 900.0, 50.0, "N·m"),
                    p("G", "Siljish moduli G", 2e10, 1.2e11, 80e9, 5e9, "Pa"),
                    p("J", "Disk inersiya momenti", 0.001, 5.0, 0.08, 0.01, "kg·m²"),
                ],
                expected_output="T_A = 525 N·m, T_B = 375 N·m, τ_max = 21,4 MPa, f = 114 Hz",
            ),
            visualization=vis(
                "Statik aniqmas val epyuralari",
                "React/SVG",
                "Val sxemasi ikki qotirish bilan; $T(x)$ epyurasi ishora "
                "o'zgarishi bilan; $\\varphi(x)$ diagrammasi ikkala uchda nolga "
                "qaytishi ko'rsatilgan.",
                "React/SVG: $\\varphi(x)$ egri chizig'ining ikkala uchda nolga "
                "qaytishi — moslik shartining vizual isboti. Bu epyura mq-17 dagi "
                "statik aniqmas balkalar bilan bevosita taqqoslanadi.",
            ),
            interpretation=(
                "$\\varphi(x)$ diagrammasi ikkala uchda nolga qaytadi — bu moslik "
                "shartining bajarilishini tasdiqlaydi. $T_A(a)$ va $T_B(a)$ "
                "grafiklari chiziqli va qarama-qarshi: moment markazga "
                "yaqinlashganda taqsimot tenglashadi. Taqqoslash jadvali statik "
                "aniqmaslikning asosiy foydasini ko'rsatadi: maksimal moment "
                "1,7 marta kamaydi."
            ),
            common_mistakes=[
                "Moslik shartini yozmasdan momentni teng ikkiga bo'lish.",
                "Uchastkalarda moment ishorasini noto'g'ri qo'yish.",
                "Buralish tebranishi chastotasida $I_p$ (m⁴) va $J$ (kg·m²) ni "
                "chalkashtirish.",
                "Rezonansni faqat birinchi garmonika bo'yicha tekshirish — "
                "dvigatelda 2-, 3- va yuqori garmonikalar ham xavfli.",
            ],
            quiz=[
                q("Statik aniqmas valda moment nima uchun bikrliklarga proporsional "
                  "taqsimlanadi?",
                  "Moslik sharti burilishlarni tenglashtiradi; bikrroq (kaltaroq) "
                  "uchastka bir xil burilish uchun ko'proq moment talab qiladi.",
                  "konseptual"),
                q("$a = b = L/2$ bo'lsa, $T_A$ va $T_B$ qanday?",
                  "Teng: $T_A = T_B = T_0/2$ — simmetriya.", "hisob"),
                q("$k_T = 50$ kN·m/rad, $J = 0{,}1$ kg·m². Chastotani toping.",
                  "$\\omega = \\sqrt{50\\,000/0{,}1} = 707$ rad/s = 112,6 Hz.", "hisob"),
                q("Nima uchun dvigatelda buralish so'ndirgichi kerak?",
                  "Tirsakli val buralish tebranishlariga tushishi mumkin; "
                  "so'ndirgich rezonans amplitudasini cheklaydi va valni "
                  "sinishdan saqlaydi.", "talqin"),
                q("Kodda $\\varphi(L) = 0$ tekshiruvi nimani tasdiqlaydi?",
                  "Moslik shartining to'g'ri qo'llanganini: ikkala uch qotirilgan, "
                  "demak umumiy burilish nolga teng bo'lishi shart.", "kod"),
            ],
            bridge_to_next=(
                "Cho'zilish va buralish o'rganildi. Endi eng keng tarqalgan va "
                "eng murakkab deformatsiya turiga — egilishga o'tamiz. Avval uning "
                "ichki kuchlari epyuralarini qurishni o'rganamiz."
            ),
            research_extension=(
                "Ikki diskli buralish tizimini modellashtiring (dvigatel–transmissiya "
                "modeli): ikkita inersiya momenti valdan bog'langan. Xususiy "
                "chastotani toping va bitta tugun nuqtasi paydo bo'lishini "
                "ko'rsating. So'ngra buralish so'ndirgichini (qo'shimcha massa + "
                "dempfer) qo'shib, nm-27 dagi dinamik so'ndirgich prinsipini "
                "buralish tizimiga tatbiq qiling."
            ),
        ),
    ),
    Topic(
        id="mq-12",
        subject_id=S,
        module_id=M,
        order=12,
        title="Egilishda ichki kuchlar: kesuvchi kuch va eguvchi moment epyuralari",
        description=(
            "Balka turlari, kesuvchi kuch va eguvchi moment epyuralarini qurish "
            "qoidalari, differensial bog'lanishlar va tekshirish usullari."
        ),
        learning_objective=(
            "Ixtiyoriy yuklanishdagi balka uchun $Q$ va $M$ epyuralarini to'g'ri "
            "qurish va xavfli kesimni aniqlash."
        ),
        prerequisites=["mq-02", "nm-10"],
        mathematical_core=(
            "Bo'lakli funksiyalar, differensial bog'lanishlar "
            "$dQ/dx = -q$, $dM/dx = Q$, ekstremum sharti."
        ),
        engineering_application=(
            "Har qanday balka, rama, ko'prik va kran konstruksiyasi hisobining "
            "asosiy bosqichi."
        ),
        computational_component=(
            "Ixtiyoriy yuklanish uchun epyuralarni avtomatik qurish algoritmi."
        ),
        visualization_component=(
            "Balka sxemasi, $Q(x)$ va $M(x)$ epyuralari bir vertikal chiziqda."
        ),
        research_extension=(
            "Epyuralarni avtomatik quruvchi algoritm: singulyar funksiyalar "
            "(Macaulay qavslari) usuli."
        ),
        difficulty="asosiy",
        previous_link=(
            "mq-02 dagi kesim usuli va differensial bog'lanishlar bu yerda "
            "to'liq qo'llaniladi. nm-10 dagi reaksiyalar epyura qurishning "
            "boshlang'ich ma'lumoti."
        ),
        next_topic="mq-13",
        estimated_minutes=95,
        tags=["epyura", "kesuvchi kuch", "eguvchi moment"],
        lesson=Lesson(
            physical_problem=(
                "Ko'prik oralig'ining qaysi kesimida beton eng ko'p armatura talab "
                "qiladi? Javob eguvchi moment maksimal bo'lgan joyda. Lekin yuk "
                "murakkab bo'lsa (o'z og'irligi, avtomobillar, shamol), maksimum "
                "qayerda ekani ko'zga ko'rinmaydi. Epyura — bu savolga javob "
                "beruvchi universal vosita va u butun konstruksiyani bir qarashda "
                "ko'rish imkonini beradi."
            ),
            concepts=[
                c("Kesuvchi kuch $Q$", "Kesimdan chapdagi barcha vertikal kuchlar "
                  "yig'indisi. Musbat — chap qismni yuqoriga ko'taradi."),
                c("Eguvchi moment $M$", "Kesimdan chapdagi barcha kuchlarning kesimga "
                  "nisbatan momenti. Musbat — balkani pastga botiq egadi."),
                c("Differensial bog'lanishlar", "$dQ/dx = -q$, $dM/dx = Q$ — "
                  "epyuralar shaklini oldindan aytib beradi."),
                c("Xarakterli nuqtalar", "Yuklanish o'zgaradigan kesimlar: "
                  "tayanchlar, nuqtaviy kuchlar, taqsimlangan yuklama chegaralari."),
                c("Epyuralarni tekshirish qoidalari", "Nuqtaviy kuch $Q$ da sakrash, "
                  "nuqtaviy moment $M$ da sakrash; $Q = 0$ da $M$ ekstremumi."),
            ],
            derivation=[
                d("1-qadam. Elementar bo'lak muvozanati",
                  r"\sum F_y = 0:\; Q - (Q+dQ) - q\,dx = 0 \;\Rightarrow\; "
                  r"\frac{dQ}{dx} = -q",
                  "$dx$ uzunlikdagi elementar bo'lakning vertikal muvozanati."),
                d("2-qadam. Moment muvozanati",
                  r"\sum M = 0:\; M + Q\,dx - (M+dM) - q\,dx\frac{dx}{2} = 0 "
                  r"\;\Rightarrow\; \frac{dM}{dx} = Q",
                  "$dx^2$ tartibidagi had tashlab yuboriladi. Bu bog'lanish "
                  "epyuralarni qurishning asosiy vositasi."),
                d("3-qadam. Epyuralar shaklini bashorat qilish",
                  r"q = 0 \Rightarrow Q = \text{const},\; M \text{ chiziqli};\quad "
                  r"q = \text{const} \Rightarrow Q \text{ chiziqli},\; M \text{ parabola}",
                  "Integrallashning har bir bosqichi funksiya darajasini bittaga "
                  "oshiradi. Bu qoida epyurani chizishdan oldin uning shaklini "
                  "bilish imkonini beradi."),
                d("4-qadam. Ekstremum sharti",
                  r"\frac{dM}{dx} = Q = 0 \;\Rightarrow\; M \text{ ekstremumi}",
                  "Maksimal eguvchi moment $Q$ nolga teng bo'lgan yoki ishorasini "
                  "o'zgartirgan kesimda. Bu — xavfli kesimni topishning eng tez usuli."),
            ],
            formula_meaning=(
                "Epyura — konstruksiyaning 'rentgen tasviri'. $Q$ epyurasi kesimlarda "
                "qanday siljituvchi kuch, $M$ epyurasi qanday eguvchi ta'sir "
                "borligini ko'rsatadi. Differensial bog'lanishlar esa ularni "
                "bir-biri bilan qat'iy bog'laydi: $M$ epyurasi $Q$ epyurasining "
                "integrali, demak $Q$ musbat bo'lgan joyda $M$ o'sadi. Bu "
                "bog'lanishlarni bilish epyura qurishni mexanik amaldan mantiqiy "
                "jarayonga aylantiradi."
            ),
            equations=[
                eq(r"\frac{dQ}{dx} = -q(x)", "Kesuvchi kuch va yuklama bog'lanishi.",
                   "1-differensial bog'lanish"),
                eq(r"\frac{dM}{dx} = Q(x)", "Eguvchi moment va kesuvchi kuch bog'lanishi.",
                   "2-differensial bog'lanish"),
                eq(r"\frac{d^2M}{dx^2} = -q(x)", "Eguvchi momentning ikkinchi hosilasi.",
                   "Umumiy bog'lanish"),
            ],
            conditions=(
                "Epyuralar bo'lakli funksiyalar — ular xarakterli nuqtalarda "
                "uziladi. Nuqtaviy kuch $Q$ epyurasida shu kuchga teng sakrash, "
                "nuqtaviy moment $M$ epyurasida shu momentga teng sakrash beradi. "
                "Balkaning erkin uchida $Q$ va $M$ nolga teng (agar u yerda yuk "
                "bo'lmasa) — bu tekshirishning eng oson usuli."
            ),
            worked_example=WorkedExample(
                statement=(
                    "Ikki tayanchli balka $L = 6$ m: A da sharnir, B da rolik. "
                    "Butun uzunlik bo'ylab $q = 12$ kN/m tekis yuklama, A dan 4 m "
                    "da $F = 30$ kN nuqtaviy kuch (nm-10 dagi masala). $Q$ va $M$ "
                    "epyuralarini quring, $M_{max}$ va uning kesimini toping."
                ),
                given=[r"L = 6\ \text{m},\; q = 12\ \text{kN/m},\; F = 30\ \text{kN}\ (a = 4\ \text{m})",
                       r"R_A = 46\ \text{kN},\; R_B = 56\ \text{kN}\ (\text{nm-10 dan})"],
                steps=[
                    st(r"0 \le x \le 4:\; Q(x) = R_A - qx = 46 - 12x",
                       "Birinchi uchastka: $Q$ chiziqli kamayadi."),
                    st(r"Q(0) = 46\ \text{kN};\quad Q(4^-) = 46-48 = -2\ \text{kN}",
                       "$Q$ ishorani $x = 46/12 = 3{,}833$ m da o'zgartiradi — "
                       "bu yerda $M$ maksimumi."),
                    st(r"M(x) = R_Ax - \frac{qx^2}{2} = 46x - 6x^2;\quad "
                       r"M(3{,}833) = 176{,}3 - 88{,}2 = 88{,}2\ \text{kN·m}",
                       "Maksimal eguvchi moment."),
                    st(r"Q(4^+) = -2 - 30 = -32\ \text{kN}",
                       "Nuqtaviy kuch $Q$ epyurasida 30 kN sakrash beradi."),
                    st(r"4 \le x \le 6:\; Q(x) = 46 - 12x - 30;\quad Q(6) = 46-72-30 = -56\ \text{kN} = -R_B\ \checkmark",
                       "Ikkinchi uchastka. B tayanchda $Q = -R_B$ — tekshiruv bajarildi."),
                    st(r"M(4) = 46\cdot4 - 6\cdot16 = 184-96 = 88\ \text{kN·m};\quad M(6) = 0\ \checkmark",
                       "Nuqtaviy kuch kesimidagi moment va B dagi nol qiymat."),
                ],
                answer=(
                    "$M_{max} = 88{,}2$ kN·m ($x = 3{,}83$ m da); $Q_{max} = 56$ kN "
                    "(B tayanchda); $M(4) = 88$ kN·m."
                ),
                engineering_note=(
                    "$M_{max}$ va $M(4)$ deyarli teng (88,2 va 88 kN·m) — demak "
                    "xavfli zona kengaygan. Bu armaturani joylashtirishda muhim: "
                    "kuchaytirish 3,5–4,5 m oralig'ida saqlanishi kerak. "
                    "$M_{max}$ aynan $Q = 0$ nuqtasida ekani differensial "
                    "bog'lanishning amaliy tasdig'i."
                ),
            ),
            computation=Computation(
                caption=(
                    "Epyuralarni avtomatik qurish: yuklarni o'zgartirib, "
                    "$M_{max}$ va xavfli kesimni toping."
                ),
                code='''"""Egilish: Q va M epyuralarini avtomatik qurish."""
import numpy as np
from labkit import PARAMS, note, series, table, value

L = float(PARAMS.get("L", 6.0))       # oraliq, m
q = float(PARAMS.get("q", 12.0))      # tekis yuklama, kN/m
F = float(PARAMS.get("F", 30.0))      # nuqtaviy kuch, kN
a = float(PARAMS.get("a", 4.0))       # kuch koordinatasi, m
M0 = float(PARAMS.get("M0", 0.0))     # nuqtaviy moment, kN*m
x_M = float(PARAMS.get("x_M", 2.0))   # moment koordinatasi, m

# Tayanch reaksiyalari (sum M_A = 0)
R_B = (q*L*L/2 + F*a + M0)/L
R_A = q*L + F - R_B
value("R_A", R_A, "kN")
value("R_B", R_B, "kN")

x = np.linspace(0, L, 2001)
Q = R_A - q*x - F*(x > a)
Mb = R_A*x - q*x**2/2 - F*np.maximum(x-a, 0) - M0*(x > x_M)

series("Kesuvchi kuch Q(x)", x.tolist(), Q.tolist(), xlabel="x, m", ylabel="Q, kN")
series("Eguvchi moment M(x)", x.tolist(), Mb.tolist(), xlabel="x, m", ylabel="M, kN·m")

i_max = int(np.argmax(np.abs(Mb)))
value("M_max", float(Mb[i_max]), "kN·m")
value("Xavfli kesim x", float(x[i_max]), "m")
value("Q_max", float(np.max(np.abs(Q))), "kN")

# Q = 0 nuqtalarini topish (M ekstremumlari)
sign_change = np.where(np.diff(np.sign(Q)))[0]
for idx in sign_change:
    note(f"Q ishorasini x = {x[idx]:.3f} m da o'zgartiradi -> "
         f"M ekstremumi = {Mb[idx]:.2f} kN·m")

# Differensial bog'lanishlarni sonli tekshirish
dM = np.gradient(Mb, x)
err = np.max(np.abs(dM[(x > 0.05) & (x < a-0.05)] - Q[(x > 0.05) & (x < a-0.05)]))
note(f"dM/dx = Q bog'lanishi tekshiruvi: maksimal farq {err:.4f} kN "
     "(nuqtaviy kuchdan uzoqda nolga yaqin bo'lishi kerak)")

# Chegaraviy shartlar
note(f"Tekshiruv: M(0) = {Mb[0]:.4f} kN·m, M(L) = {Mb[-1]:.4f} kN·m "
     "(sharnirli tayanchlarda nol bo'lishi kerak) ✓")
note(f"Tekshiruv: Q(L) = {Q[-1]:.3f} kN, -R_B = {-R_B:.3f} kN ✓")

table("Epyuralar qoidalari",
      ["Yuklanish", "Q epyurasi", "M epyurasi"],
      [["Yuk yo'q (q=0)", "o'zgarmas", "chiziqli"],
       ["Tekis yuklama q", "chiziqli", "kvadrat parabola"],
       ["Nuqtaviy kuch F", "F ga sakrash", "sinish (burilish)"],
       ["Nuqtaviy moment M₀", "o'zgarmaydi", "M₀ ga sakrash"],
       ["Q = 0 kesimi", "—", "ekstremum"]])

# Yuklanish turlarini taqqoslash
table("Tipik sxemalar uchun M_max",
      ["Sxema", "M_max", "Qiymat (joriy L, q, F)"],
      [["Ikki tayanch + tekis yuk", "qL²/8", float(q*L**2/8)],
       ["Ikki tayanch + o'rtada F", "FL/4", float(F*L/4)],
       ["Konsol + uchida F", "FL", float(F*L)],
       ["Konsol + tekis yuk", "qL²/2", float(q*L**2/2)]])
''',
                parameters=[
                    p("L", "Oraliq L", 1.0, 20.0, 6.0, 0.5, "m"),
                    p("q", "Tekis yuklama q", 0.0, 100.0, 12.0, 1.0, "kN/m"),
                    p("F", "Nuqtaviy kuch F", 0.0, 300.0, 30.0, 5.0, "kN"),
                    p("a", "Kuch koordinatasi a", 0.0, 20.0, 4.0, 0.25, "m"),
                    p("M0", "Nuqtaviy moment M₀", -200.0, 200.0, 0.0, 10.0, "kN·m"),
                    p("x_M", "Moment koordinatasi", 0.0, 20.0, 2.0, 0.25, "m"),
                ],
                expected_output="R_A = 46 kN, R_B = 56 kN, M_max = 88,17 kN·m (x = 3,83 m)",
            ),
            visualization=vis(
                "Balka sxemasi va epyuralar",
                "React/SVG",
                "Uch panel bir vertikal o'qda: yuqorida balka sxemasi (tayanchlar, "
                "yuklar), o'rtada $Q(x)$ epyurasi, pastda $M(x)$ epyurasi. "
                "Xavfli kesim vertikal chiziq bilan barcha panellarda belgilangan.",
                "React/SVG: uch panelni bitta $x$ o'qi bo'ylab tekislash — bu "
                "mexanika chizmalarining standart formati va u epyuralar orasidagi "
                "bog'lanishni ko'rsatadi. Epyura ostidagi sohani bo'yash, musbat va "
                "manfiy qismlarni turli rangda berish an'anaviy va o'qishga qulay.",
            ),
            interpretation=(
                "$Q$ epyurasi nuqtaviy kuchda sakraydi, $M$ epyurasi esa sinadi — "
                "bu differensial bog'lanishning bevosita natijasi. $M_{max}$ aynan "
                "$Q = 0$ nuqtasida: sonli tekshiruv $dM/dx = Q$ bog'lanishining "
                "$10^{-3}$ aniqlikda bajarilishini tasdiqlaydi. Tipik sxemalar "
                "jadvali esa tez baholash uchun foydali: konsol balkada moment "
                "ikki tayanchlidagidan 8 marta katta."
            ),
            common_mistakes=[
                "Reaksiyalarni noto'g'ri topib, butun epyurani buzish — reaksiyalarni "
                "har doim ikkinchi moment tenglamasi bilan tekshiring.",
                "Nuqtaviy kuch ta'sirida $M$ epyurasida sakrash kutish — sakrash "
                "faqat $Q$ da, $M$ da esa sinish bo'ladi.",
                "$M_{max}$ ni nuqtaviy kuch ostida deb olish — u $Q = 0$ nuqtasida.",
                "Sharnirli tayanchda $M \\neq 0$ qoldirish.",
            ],
            quiz=[
                q("Nima uchun $M_{max}$ aynan $Q = 0$ kesimida bo'ladi?",
                  "$dM/dx = Q$ bo'lgani uchun $Q = 0$ ekstremum shartidir.",
                  "konseptual"),
                q("Tekis yuklamada $M$ epyurasi qanday shaklda?",
                  "Kvadrat parabola, chunki $q = \\text{const}$ → $Q$ chiziqli → "
                  "$M$ kvadratik.", "konseptual"),
                q("Ikki tayanchli balka, $L = 8$ m, o'rtasida $F = 40$ kN. $M_{max}$?",
                  "$M_{max} = FL/4 = 40\\cdot8/4 = 80$ kN·m.", "hisob"),
                q("Konsol balka, $L = 3$ m, $q = 10$ kN/m. Qotirishda $M$?",
                  "$M = qL^2/2 = 10\\cdot9/2 = 45$ kN·m.", "hisob"),
                q("Kodda `F*(x > a)` ifodasi nima qiladi?",
                  "Heaviside funksiyasi rolini bajaradi: $x > a$ bo'lganda kuchni "
                  "hisobga qo'shadi. Bu — Macaulay qavslarining sodda amalga "
                  "oshirilishi.", "kod"),
                q("Erkin uchda $Q$ va $M$ nimaga teng?",
                  "Ikkalasi ham nolga (agar u yerda yuk yoki moment qo'yilmagan "
                  "bo'lsa) — bu epyurani tekshirishning eng oson usuli.", "talqin"),
            ],
            bridge_to_next=(
                "Ichki kuchlar aniqlandi. Endi ular kesimda qanday kuchlanish hosil "
                "qilishini — egilish nazariyasining markaziy formulasini "
                "keltirib chiqaramiz."
            ),
            research_extension=(
                "Macaulay singulyar funksiyalari usulini amalga oshiring: "
                "$\\langle x-a\\rangle^n$ notatsiyasi bilan ixtiyoriy yuklanish "
                "uchun $Q(x)$, $M(x)$, $w(x)$ ni yagona analitik ifodada yozing. "
                "Bu usul epyuralarni qurishni to'liq avtomatlashtiradi va uni "
                "mq-16 dagi dastlabki parametrlar usuli bilan taqqoslang."
            ),
            manim=manim(
                scene="BeamDiagramScene",
                module="manim/scenes/mq_bending.py",
                title="Kesuvchi kuch va eguvchi moment epyuralari",
                summary="Balka bo'ylab kesim siljiydi, har bir holatda ichki kuchlar "
                        "hisoblanadi va epyuralar bosqichma-bosqich quriladi.",
            ),
        ),
    ),
]
