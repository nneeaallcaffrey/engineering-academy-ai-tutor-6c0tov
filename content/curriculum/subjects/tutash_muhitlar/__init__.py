"""3-fan: Tutash muhitlar mexanikasi (kod: TMM).

Zanjirdagi o'rni: materiallar qarshiligidagi bir o'lchovli gipotezalarni
olib tashlaydi va uch o'lchovli, tenzor tilidagi umumiy nazariyani quradi.
Bu fan plastinalar/qobiqlar nazariyasi (4-fan) va hisoblash mexanikasi
(5-fan) uchun matematik poydevor beradi.
"""

from __future__ import annotations

from content.curriculum.schema import Assessment, Module, Resource, Subject

from .m1_kinematika import TOPICS as _T1
from .m2_balans import TOPICS as _T2
from .m3_elastiklik import TOPICS as _T3
from .m4_plastiklik import TOPICS as _T4
from .m5_suyuqlik import TOPICS as _T5

SUBJECT_ID = "tutash-muhitlar"

MODULES = [
    Module(
        id="tmm-m1", subject_id=SUBJECT_ID, order=1,
        title="Kontinuum modeli va deformatsiya kinematikasi",
        summary=(
            "Tutash muhit gipotezasi, tenzor apparati, Lagranj va Eyler "
            "tavsiflari, deformatsiya gradiyenti va deformatsiya tenzorlari."
        ),
        outcome=(
            "Talaba ixtiyoriy ko'chish maydonidan deformatsiya tenzorini "
            "hisoblaydi va uni fizik jihatdan talqin qiladi."
        ),
    ),
    Module(
        id="tmm-m2", subject_id=SUBJECT_ID, order=2,
        title="Kuchlanish tenzori va balans qonunlari",
        summary=(
            "Koshi teoremasi, kuchlanish tenzori va invariantlari, massa, "
            "impuls, impuls momenti va energiya balansi."
        ),
        outcome=(
            "Talaba kontinuum uchun harakat tenglamalarini yozadi va "
            "kuchlanish holatini to'liq tahlil qiladi."
        ),
    ),
    Module(
        id="tmm-m3", subject_id=SUBJECT_ID, order=3,
        title="Konstitutiv munosabatlar va elastiklik nazariyasi",
        summary=(
            "Material tenglamalari prinsiplari, chiziqli izotrop elastiklik, "
            "Navye tenglamalari, tekis masalalar va variatsion prinsiplar."
        ),
        outcome=(
            "Talaba elastiklik nazariyasining to'la masalasini qo'yadi va "
            "klassik yechimlarni (Eyri funksiyasi, Sen-Venan buralishi) tahlil qiladi."
        ),
    ),
    Module(
        id="tmm-m4", subject_id=SUBJECT_ID, order=4,
        title="To'lqinlar, plastiklik va reologiya",
        summary=(
            "Elastik to'lqinlar, plastik oqish kriteriylari, mustahkamlanish, "
            "viskoelastiklik va yoriqlar mexanikasi asoslari."
        ),
        outcome=(
            "Talaba nochiziqli material xatti-harakatini modellashtiradi va "
            "buzilish mexanikasi tushunchalarini qo'llaydi."
        ),
    ),
    Module(
        id="tmm-m5", subject_id=SUBJECT_ID, order=5,
        title="Suyuqlik va gaz mexanikasi",
        summary=(
            "Gidrostatika, Eyler va Navye–Stoks tenglamalari, analitik oqim "
            "yechimlari, o'xshashlik nazariyasi va turbulentlik asoslari."
        ),
        outcome=(
            "Talaba oqim masalasini qo'yadi, o'lchamsiz sonlar orqali rejimni "
            "aniqlaydi va sodda holatlarda analitik yechim oladi."
        ),
    ),
]

TOPICS = [*_T1, *_T2, *_T3, *_T4, *_T5]

ASSESSMENTS = [
    Assessment(
        kind="oraliq", title="1-oraliq nazorat: kinematika va balans qonunlari",
        covers="tmm-01 … tmm-12", weight=20,
        format=("Tenzor hisobi masalalari, deformatsiya tenzorini hisoblash, "
                "Koshi teoremasini qo'llash, muvozanat tenglamalarini tekshirish."),
    ),
    Assessment(
        kind="oraliq", title="2-oraliq nazorat: elastiklik nazariyasi",
        covers="tmm-13 … tmm-19", weight=20,
        format=("Navye tenglamalarini yozish, tekis masalani Eyri funksiyasi "
                "bilan yechish, variatsion formulirovka."),
    ),
    Assessment(
        kind="yakuniy", title="Yakuniy imtihon", covers="tmm-01 … tmm-30", weight=35,
        format=("A — tenzor apparati va balans qonunlari; B — elastiklik yoki "
                "suyuqlik masalasini yechish; C — natijani fizik talqin qilish."),
    ),
    Assessment(
        kind="loyiha", title="Yakuniy loyiha: elastik jism yoki oqim uchun matematik model",
        covers="tmm-01 … tmm-30", weight=25,
        format="To'liq model: tenglamalar, chegaraviy shartlar, sonli yechim, tahlil.",
    ),
]

RESOURCES = [
    Resource("Механика сплошной среды", "L. I. Sedov", "Vol. 1–2", "asosiy",
             "Klassik va eng to'liq rus tilidagi bayon."),
    Resource("Continuum Mechanics", "A. J. M. Spencer", "—", "asosiy",
             "Ixcham va tushunarli kirish; tenzor apparati yaxshi bayon qilingan."),
    Resource("Theory of Elasticity", "S. P. Timoshenko, J. N. Goodier", "3-nashr",
             "asosiy", "Elastiklik nazariyasining klassik darsligi."),
    Resource("A First Course in Continuum Mechanics", "Y. C. Fung", "—", "asosiy",
             "Muhandislik nuqtai nazaridan yozilgan kirish kursi."),
    Resource("Fluid Mechanics", "F. M. White", "—", "asosiy",
             "Suyuqliklar mexanikasi bo'limi uchun asosiy manba."),
    Resource("Теория упругости", "V. Novatskiy", "—", "qoshimcha",
             "Elastiklik nazariyasi va to'lqinlar bo'yicha chuqur bayon."),
    Resource("Introduction to Fracture Mechanics", "T. L. Anderson", "—", "qoshimcha",
             "Yoriqlar mexanikasi bo'limi uchun."),
    Resource("An Introduction to Fluid Dynamics", "G. K. Batchelor", "—", "qoshimcha",
             "Suyuqlik dinamikasining nazariy asoslari."),
    Resource("MIT 2.25 Advanced Fluid Mechanics / 16.20 Structural Mechanics",
             "MIT OCW", "—", "kurs",
             "Kontinuum mexanikasi kurslarining tuzilishi namunasi."),
]

SUBJECT = Subject(
    id=SUBJECT_ID,
    code="TMM",
    order=3,
    title="Tutash muhitlar mexanikasi",
    tagline="Deformatsiyalanuvchi jism va suyuqlikning umumiy nazariyasi",
    description=(
        "Tutash muhitlar mexanikasi qattiq jism, suyuqlik va gazning "
        "deformatsiyasi hamda harakatini yagona matematik apparat bilan "
        "tavsiflaydi. Materiallar qarshiligida qabul qilingan gipotezalar "
        "(tekis kesimlar, sterjen modeli) bu yerda olib tashlanadi: "
        "kuchlanish va deformatsiya tenzorlarga aylanadi, muvozanat esa "
        "differensial tenglamalar tizimiga. Kurs kinematikadan boshlanib, "
        "balans qonunlari va konstitutiv munosabatlar orqali elastiklik, "
        "plastiklik va suyuqliklar mexanikasiga olib chiqadi."
    ),
    goal=(
        "Deformatsiyalanuvchi muhit uchun to'liq matematik model qurish: "
        "kinematika, balans qonunlari va material tenglamalarini birlashtirib, "
        "chegaraviy masalani qo'yish va yechish."
    ),
    prerequisites_text=(
        "Nazariy mexanika (tenzor tushunchasi — nm-17, balans qonunlari — nm-13) "
        "va materiallar qarshiligi (kuchlanish, deformatsiya, Guk qonuni — "
        "mq-03, mq-19, mq-20). Matematikadan: xususiy hosilalar, vektor tahlili "
        "(divergensiya, rotor, gradiyent), xususiy qiymatlar masalasi, PDE asoslari."
    ),
    modules=MODULES,
    topics=TOPICS,
    assessments=ASSESSMENTS,
    resources=RESOURCES,
    accent="indigo",
    depends_on=["nazariy-mexanika", "materiallar-qarshiligi"],
)
