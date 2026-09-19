"""4-fan: Plastinalar va qobiqlar nazariyasi (kod: PQ).

Zanjirdagi o'rni: tutash muhitlar mexanikasining uch o'lchovli elastiklik
masalasini yupqa konstruksiyalar uchun ixtisoslashtiradi. Kirxhoff–Lyav
gipotezalari yordamida 3D masala 2D masalaga keltiriladi; natijada
qurilish, aviatsiya va mashinasozlikdagi eng ko'p uchraydigan element —
yupqa plastina va qobiq — uchun amaliy nazariya hosil bo'ladi.
Bu fan sonli usullar (5-fan) uchun eng boy masalalar to'plamini beradi.
"""

from __future__ import annotations

from content.curriculum.schema import Assessment, Module, Resource, Subject

from .m1_asoslar import TOPICS as _T1
from .m2_yechimlar import TOPICS as _T2
from .m3_doiraviy import TOPICS as _T3
from .m4_ustuvorlik import TOPICS as _T4
from .m5_qobiqlar import TOPICS as _T5

SUBJECT_ID = "plastinalar-qobiqlar"

MODULES = [
    Module(
        id="pq-m1", subject_id=SUBJECT_ID, order=1,
        title="Yupqa plastina modeli va asosiy tenglama",
        summary=(
            "Kirxhoff–Lyav gipotezalari, egilish kinematikasi, ichki kuch "
            "omillari, Sofi Jermen–Lagranj tenglamasi, chegaraviy shartlar "
            "va kuchlanish taqsimoti."
        ),
        outcome=(
            "Talaba plastina egilishi masalasini to'liq qo'yadi: tenglama, "
            "chegaraviy shartlar va kuchlanish hisobini bajaradi."
        ),
    ),
    Module(
        id="pq-m2", subject_id=SUBJECT_ID, order=2,
        title="To'rtburchak plastinalar: analitik va sonli yechimlar",
        summary=(
            "Navye va Levi qator yechimlari, energiya usullari (Ritz, "
            "Galerkin), chekli ayirmalar, chegaraviy shartlarning ta'siri "
            "va ortotrop plastinalar."
        ),
        outcome=(
            "Talaba bir xil masalani to'rt xil usulda yechadi va "
            "natijalarni yaqinlashish bo'yicha taqqoslaydi."
        ),
    ),
    Module(
        id="pq-m3", subject_id=SUBJECT_ID, order=3,
        title="Doiraviy plastinalar va murakkab modellar",
        summary=(
            "O'qsimmetrik va nosimmetrik doiraviy plastinalar, halqasimon "
            "plastinalar, elastik asos, qatlamli (sendvich) konstruksiyalar "
            "va fon Karman katta og'ishlari."
        ),
        outcome=(
            "Talaba silindrik koordinatalardagi masalani yechadi va "
            "geometrik nochiziqlilikning ta'sirini baholaydi."
        ),
    ),
    Module(
        id="pq-m4", subject_id=SUBJECT_ID, order=4,
        title="Plastinalarning ustuvorligi va tebranishlari",
        summary=(
            "Sirt ichidagi kuchlar, kritik yuklama masalasi, kritikdan "
            "keyingi xatti-harakat, erkin va majburiy tebranishlar, "
            "Mindlin–Reissner nazariyasi."
        ),
        outcome=(
            "Talaba plastinaning kritik yuklamasini va xususiy "
            "chastotalarini hisoblaydi hamda dinamik javobini tahlil qiladi."
        ),
    ),
    Module(
        id="pq-m5", subject_id=SUBJECT_ID, order=5,
        title="Qobiqlar nazariyasi",
        summary=(
            "Qobiq geometriyasi, membrana nazariyasi, silindrik, sferik va "
            "konus qobiqlar, chekka effekti, ustuvorlik va tebranishlar."
        ),
        outcome=(
            "Talaba aylanma qobiq uchun membrana yechimini oladi, chekka "
            "bezovtaligini baholaydi va ustuvorlikni tekshiradi."
        ),
    ),
]

TOPICS = [*_T1, *_T2, *_T3, *_T4, *_T5]

ASSESSMENTS = [
    Assessment(
        kind="oraliq", title="1-oraliq nazorat: plastina nazariyasi asoslari",
        covers="pq-01 … pq-12", weight=20,
        format=("Kirxhoff gipotezalarini qo'llash, $D\\nabla^4w = q$ "
                "tenglamasini yozish, Navye qatori bilan yechish, "
                "kuchlanishni hisoblash."),
    ),
    Assessment(
        kind="oraliq", title="2-oraliq nazorat: doiraviy plastinalar va nochiziqlilik",
        covers="pq-13 … pq-24", weight=20,
        format=("Silindrik koordinatalardagi yechim, elastik asos, "
                "kritik yuklama va xususiy chastota hisobi."),
    ),
    Assessment(
        kind="yakuniy", title="Yakuniy imtihon", covers="pq-01 … pq-30", weight=35,
        format=("A — nazariy asoslar va gipotezalar; B — plastina yoki "
                "qobiq masalasini yechish; C — natijani muhandislik "
                "nuqtai nazaridan baholash."),
    ),
    Assessment(
        kind="loyiha", title="Yakuniy loyiha: yupqa devorli konstruksiya tahlili",
        covers="pq-01 … pq-30", weight=25,
        format=("Plastina yoki qobiq elementining to'liq tahlili: egilish, "
                "kuchlanish, ustuvorlik, tebranish va sonli tekshiruv."),
    ),
]

RESOURCES = [
    Resource("Theory of Plates and Shells", "S. P. Timoshenko, S. Woinowsky-Krieger",
             "2-nashr", "asosiy",
             "Sohaning klassik va eng ko'p havola qilinadigan darsligi."),
    Resource("Theory and Analysis of Elastic Plates and Shells", "J. N. Reddy",
             "2-nashr", "asosiy",
             "Zamonaviy bayon: klassik, Mindlin va qatlamli nazariyalar."),
    Resource("Stresses in Shells", "W. Flügge", "2-nashr", "asosiy",
             "Qobiqlar nazariyasining mukammal va tizimli bayoni."),
    Resource("Пластинки и оболочки", "S. P. Timoshenko, S. Voynovskiy-Kriger",
             "—", "asosiy", "Rus tilidagi klassik tarjima; jadvallar boy."),
    Resource("Thin Plates and Shells: Theory, Analysis and Applications",
             "E. Ventsel, T. Krauthammer", "—", "asosiy",
             "Amaliy misollar va sonli usullar bilan boyitilgan zamonaviy kurs."),
    Resource("Theory of Elastic Stability", "S. P. Timoshenko, J. M. Gere",
             "2-nashr", "qoshimcha",
             "Plastina va qobiq ustuvorligi bo'limlari uchun asosiy manba."),
    Resource("Mechanics of Composite Materials", "R. M. Jones", "2-nashr",
             "qoshimcha", "Qatlamli va ortotrop plastinalar uchun."),
    Resource("Vibration of Plates (NASA SP-160)", "A. W. Leissa", "—", "qoshimcha",
             "Plastinalar tebranishining eng to'liq ma'lumotnomasi."),
    Resource("MIT 16.20 Structural Mechanics / Stanford ME 335",
             "MIT OCW, Stanford", "—", "kurs",
             "Plastina va qobiq kurslarining tuzilishi namunasi."),
]

SUBJECT = Subject(
    id=SUBJECT_ID,
    code="PQ",
    order=4,
    title="Plastinalar va qobiqlar nazariyasi",
    tagline="Yupqa konstruksiyalarning ikki o'lchovli nazariyasi",
    description=(
        "Plastina va qobiq — muhandislikdagi eng samarali konstruktiv "
        "shakllar: kam material bilan katta bikrlik beradi. Ularning "
        "nazariyasi tutash muhitlar mexanikasining uch o'lchovli "
        "masalasini asoslangan gipotezalar (Kirxhoff–Lyav) yordamida "
        "ikki o'lchovli masalaga keltirishga asoslanadi. Kurs yupqa "
        "plastinaning asosiy tenglamasidan boshlanib, analitik va sonli "
        "yechim usullari, ustuvorlik, tebranishlar orqali qobiqlar "
        "nazariyasiga olib chiqadi."
    ),
    goal=(
        "Yupqa devorli konstruksiya elementining to'liq mexanik tahlilini "
        "bajarish: model tanlash, tenglama va chegaraviy shartlarni yozish, "
        "yechish, kuchlanish, ustuvorlik va tebranishni baholash."
    ),
    prerequisites_text=(
        "Materiallar qarshiligi (egilish nazariyasi — mq-13…mq-16, "
        "ustuvorlik — mq-25) va tutash muhitlar mexanikasi (kuchlanish va "
        "deformatsiya tenzorlari — tmm-05, tmm-07; izotrop elastiklik — "
        "tmm-14; tekis masala — tmm-16; variatsion prinsiplar — tmm-19). "
        "Matematikadan: xususiy hosilali tenglamalar, Furye qatorlari, "
        "Bessel funksiyalari, xususiy qiymatlar masalasi."
    ),
    modules=MODULES,
    topics=TOPICS,
    assessments=ASSESSMENTS,
    resources=RESOURCES,
    accent="violet",
    depends_on=["materiallar-qarshiligi", "tutash-muhitlar"],
)
