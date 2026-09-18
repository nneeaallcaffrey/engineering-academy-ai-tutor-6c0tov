"""2-fan: Materiallar qarshiligi (kod: MQ).

Zanjirdagi o'rni: nazariy mexanikadagi qattiq jism farazini olib tashlaydi.
Endi jism deformatsiyalanadi va uning ichida kuchlanish paydo bo'ladi.
Bu fan tutash muhitlar mexanikasining bir o'lchovli, muhandislik varianti
sifatida qaraladi — tmm-07 da bir xil tushunchalar tenzor tilida umumlashtiriladi.
"""

from __future__ import annotations

from content.curriculum.schema import Assessment, Module, Resource, Subject

from .m1_kuchlanish import TOPICS as _T1
from .m2_geometriya import TOPICS as _T2
from .m3_egilish import TOPICS as _T3
from .m4_murakkab import TOPICS as _T4
from .m5_ustuvorlik import TOPICS as _T5

SUBJECT_ID = "materiallar-qarshiligi"

MODULES = [
    Module(
        id="mq-m1", subject_id=SUBJECT_ID, order=1,
        title="Kuchlanish, deformatsiya va mustahkamlik sharti",
        summary=(
            "Kesim usuli, kuchlanish va deformatsiya tushunchalari, Guk qonuni, "
            "material tavsiflari va mustahkamlik hisobining mantiqi."
        ),
        outcome=(
            "Talaba sterjenli konstruksiyada kuchlanishni hisoblab, mustahkamlik "
            "shartini tekshiradi va kesimni tanlaydi."
        ),
    ),
    Module(
        id="mq-m2", subject_id=SUBJECT_ID, order=2,
        title="Kesim geometriyasi, siljish va buralish",
        summary=(
            "Kesimning geometrik tavsiflari (statik moment, inersiya momenti), "
            "siljish deformatsiyasi va valning buralish hisobi."
        ),
        outcome=(
            "Talaba ixtiyoriy kesimning geometrik tavsiflarini hisoblaydi va "
            "valni mustahkamlik hamda bikrlik bo'yicha loyihalaydi."
        ),
    ),
    Module(
        id="mq-m3", subject_id=SUBJECT_ID, order=3,
        title="Egilish nazariyasi",
        summary=(
            "Ichki kuchlar epyuralari, toza va ko'ndalang egilish, egilgan o'q "
            "differensial tenglamasi, ko'chishlarni aniqlash va ratsional loyihalash."
        ),
        outcome=(
            "Talaba balkani to'liq hisoblaydi: epyuralar, kuchlanishlar, ko'chishlar "
            "va kesim tanlovi."
        ),
    ),
    Module(
        id="mq-m4", subject_id=SUBJECT_ID, order=4,
        title="Murakkab kuchlanish holati va mustahkamlik nazariyalari",
        summary=(
            "Kuchlanish holati tahlili, Mor doirasi, umumlashgan Guk qonuni, "
            "mustahkamlik kriteriylari va murakkab qarshilik hollari."
        ),
        outcome=(
            "Talaba fazoviy kuchlanish holatini tahlil qilib, mos mustahkamlik "
            "nazariyasi bo'yicha ekvivalent kuchlanishni hisoblaydi."
        ),
    ),
    Module(
        id="mq-m5", subject_id=SUBJECT_ID, order=5,
        title="Ustuvorlik, dinamik va siklik yuklanish",
        summary=(
            "Eyler masalasi va ustuvorlik hisobi, zarbiy yuklanish, charchash "
            "va kuchlanish konsentratsiyasi; kompleks loyihalash."
        ),
        outcome=(
            "Talaba konstruktiv elementni mustahkamlik, bikrlik, ustuvorlik va "
            "chidamlilik bo'yicha birgalikda hisoblaydi."
        ),
    ),
]

TOPICS = [*_T1, *_T2, *_T3, *_T4, *_T5]

ASSESSMENTS = [
    Assessment(
        kind="oraliq", title="1-oraliq nazorat: cho'zilish, buralish, geometrik tavsiflar",
        covers="mq-01 … mq-11", weight=20,
        format=("3 ta hisob masalasi (statik aniqmas sterjen tizimi, kesim geometrik "
                "tavsiflari, val hisobi) + epyura qurish topshirig'i."),
    ),
    Assessment(
        kind="oraliq", title="2-oraliq nazorat: egilish va kuchlanish holati",
        covers="mq-12 … mq-24", weight=20,
        format=("Balkaning to'liq hisobi (epyuralar, kuchlanish, ko'chish) + Mor "
                "doirasi va mustahkamlik nazariyasi bo'yicha masala."),
    ),
    Assessment(
        kind="yakuniy", title="Yakuniy imtihon", covers="mq-01 … mq-30", weight=35,
        format=("A — nazariy derivatsiya (egilish formulasi yoki Eyler kuchi); "
                "B — murakkab qarshilikdagi val hisobi; C — ustuvorlik va charchash "
                "tekshiruvi."),
    ),
    Assessment(
        kind="loyiha", title="Yakuniy loyiha: konstruktiv elementni to'liq hisoblash",
        covers="mq-01 … mq-30", weight=25,
        format="Hisob-kitob hisoboti + Python kodi + epyuralar + kesim tanlovi asosi.",
    ),
]

RESOURCES = [
    Resource("Сопротивление материалов", "N. M. Belyaev", "klassik", "asosiy",
             "Klassik bayon va masalalar to'plami — kursning tayanch manbai."),
    Resource("Сопротивление материалов", "V. I. Feodosyev", "klassik", "asosiy",
             "Chuqur fizik talqin va nostandart masalalar."),
    Resource("Mechanics of Materials", "F. P. Beer, E. R. Johnston", "—", "asosiy",
             "Zamonaviy muhandislik bayoni, ko'p sonli amaliy misollar."),
    Resource("Strength of Materials", "S. P. Timoshenko", "Part I–II", "asosiy",
             "Nazariy asoslar va tarixiy derivatsiyalar."),
    Resource("Mechanics of Materials", "J. M. Gere, B. J. Goodno", "—", "qoshimcha",
             "Kesim tavsiflari va ustuvorlik bo'limlari uchun qulay."),
    Resource("Сборник задач по сопротивлению материалов", "A. V. Darkov (tahr.)", "—",
             "qoshimcha", "Amaliy mashg'ulotlar uchun masalalar bazasi."),
    Resource("Roark's Formulas for Stress and Strain", "W. C. Young, R. G. Budynas", "—",
             "qoshimcha", "Muhandislik amaliyotidagi tayyor formulalar ma'lumotnomasi."),
    Resource("MIT 2.001 Mechanics and Materials I", "MIT OCW", "—", "kurs",
             "Kuchlanish–deformatsiya–konstruksiya ketma-ketligi namunasi."),
    Resource("Universitet 'Materiallar qarshiligi' tipovoy dasturi", "Texnika oliy ta'limi",
             "—", "kurs", "Cho'zilish → buralish → egilish → murakkab qarshilik → "
             "ustuvorlik ketma-ketligi asos qilib olindi."),
]

SUBJECT = Subject(
    id=SUBJECT_ID,
    code="MQ",
    order=2,
    title="Materiallar qarshiligi",
    tagline="Konstruksiya ichidagi kuchlanish, deformatsiya va mustahkamlik",
    description=(
        "Materiallar qarshiligi konstruktiv elementlarning mustahkamligi, bikrligi "
        "va ustuvorligini hisoblash usullarini o'rganadi. Nazariy mexanikada jism "
        "qattiq deb qabul qilingan edi; bu yerda u deformatsiyalanadi va ichida "
        "kuchlanish paydo bo'ladi. Kurs cho'zilishdan boshlab, buralish va egilish "
        "orqali murakkab kuchlanish holati, ustuvorlik va charchash masalalariga "
        "olib chiqadi."
    ),
    goal=(
        "Real konstruktiv elementni hisob sxemasiga keltirish, undagi ichki kuchlar "
        "va kuchlanishlarni aniqlash hamda mustahkamlik, bikrlik va ustuvorlik "
        "shartlarini birgalikda ta'minlaydigan o'lchamlarni tanlash."
    ),
    prerequisites_text=(
        "Nazariy mexanika (muvozanat tenglamalari, epyura tushunchasi, inersiya "
        "momenti) — nm-10, nm-11, nm-16, nm-17. Matematikadan: integral hisob, "
        "oddiy differensial tenglamalar, chiziqli algebra elementlari."
    ),
    modules=MODULES,
    topics=TOPICS,
    assessments=ASSESSMENTS,
    resources=RESOURCES,
    accent="amber",
    depends_on=["nazariy-mexanika"],
)
