"""5-fan: Sonli usullar va hisoblash mexanikasi (kod: SU).

Zanjirdagi o'rni: oldingi to'rt fan mexanika masalalarini qo'yishni va
analitik yechishni o'rgatdi. Lekin analitik yechim faqat sodda geometriya
va sodda chegaraviy shartlar uchun mavjud: Navye qatori to'rt tomoni
sharnirli to'rtburchak uchun, Levi ikki tomoni sharnirli uchun,
o'qsimmetrik yechim faqat doiraviy plastina uchun ishladi. Haqiqiy
konstruksiyada teshiklar, qovurg'alar, o'zgaruvchan qalinlik va aralash
chegaraviy shartlar bo'ladi. Bu fan shu bo'shliqni to'ldiradi va kursni
yopadi: oldingi fanlardagi har bir tenglama bu yerda sonli yechiladi,
har bir analitik natija esa sonli yechimning tekshiruvi (verifikatsiya)
sifatida ishlatiladi.
"""

from __future__ import annotations

from content.curriculum.schema import Assessment, Module, Resource, Subject

from .m1_asoslar import TOPICS as _T1
from .m2_chekli_ayirmalar import TOPICS as _T2
from .m3_fem_asoslari import TOPICS as _T3
from .m4_fem_ilovalari import TOPICS as _T4
from .m5_zamonaviy import TOPICS as _T5

SUBJECT_ID = "sonli-usullar"

MODULES = [
    Module(
        id="su-m1", subject_id=SUBJECT_ID, order=1,
        title="Sonli hisoblash asoslari va xatoliklar",
        summary=(
            "Sonli usullarning o'rni, suzuvchi nuqta arifmetikasi, "
            "yaxlitlash va kesish xatoliklari, shartlanganlik soni, "
            "chiziqli tizimlarni to'g'ri va iterativ yechish."
        ),
        outcome=(
            "Talaba sonli natijaning xatoligini manbalarga ajratadi, "
            "shartlanganlikni baholaydi va mos yechish usulini tanlaydi."
        ),
    ),
    Module(
        id="su-m2", subject_id=SUBJECT_ID, order=2,
        title="Chekli ayirmalar usuli",
        summary=(
            "Ayirma sxemalari va yaqinlashish tartibi, bir va ikki "
            "o'lchovli chegaraviy masalalar, barqarorlik va yaqinlashish, "
            "vaqt bo'yicha integrallash, to'lqin tarqalishi."
        ),
        outcome=(
            "Talaba differensial tenglamani ayirma sxemasiga o'tkazadi, "
            "barqarorlik shartini aniqlaydi va yaqinlashish tartibini "
            "sonli o'lchaydi."
        ),
    ),
    Module(
        id="su-m3", subject_id=SUBJECT_ID, order=3,
        title="Chekli elementlar usulining asoslari",
        summary=(
            "Variatsion asos va zaif formulirovka, shakl funksiyalari, "
            "izoparametrik almashtirish, element matritsalari va yig'ish, "
            "sonli integrallash, xatolik baholash va adaptivlik."
        ),
        outcome=(
            "Talaba FEM ni nazariy asosidan boshlab quradi va bir "
            "o'lchovli masala uchun to'liq dasturini yozadi."
        ),
    ),
    Module(
        id="su-m4", subject_id=SUBJECT_ID, order=4,
        title="Chekli elementlar usulining ilovalari",
        summary=(
            "Ferma, balka va ramka elementlari, tekis masala elementlari, "
            "plastina va qobiq elementlari, xususiy qiymat masalalari, "
            "nochiziqli tahlil."
        ),
        outcome=(
            "Talaba oldingi to'rt fandagi masalalarni FEM bilan yechadi "
            "va natijani analitik yechim bilan tekshiradi."
        ),
    ),
    Module(
        id="su-m5", subject_id=SUBJECT_ID, order=5,
        title="Zamonaviy usullar, tekshirish va yakun",
        summary=(
            "Differensial kvadratura (DQM), chegaraviy elementlar (BEM), "
            "spektral usullar, verifikatsiya va validatsiya, hisoblash "
            "samaradorligi va kursning yakuniy integratsiyasi."
        ),
        outcome=(
            "Talaba usul tanlashni asoslaydi, natijani V&V tartibida "
            "tekshiradi va hisoblash zanjirini uchdan-uchgacha quradi."
        ),
    ),
]

TOPICS = [*_T1, *_T2, *_T3, *_T4, *_T5]

ASSESSMENTS = [
    Assessment(
        kind="oraliq", title="1-oraliq nazorat: xatoliklar va chekli ayirmalar",
        covers="su-01 … su-12", weight=20,
        format=("Xatolik manbalarini ajratish, shartlanganlikni baholash, "
                "ayirma sxemasi qurish, barqarorlik shartini chiqarish va "
                "yaqinlashish tartibini sonli o'lchash."),
    ),
    Assessment(
        kind="oraliq", title="2-oraliq nazorat: chekli elementlar usuli",
        covers="su-13 … su-24", weight=20,
        format=("Zaif formulirovkani yozish, element matritsasini "
                "hisoblash, tizimni yig'ish va yechish, natijani analitik "
                "yechim bilan taqqoslash."),
    ),
    Assessment(
        kind="yakuniy", title="Yakuniy imtihon", covers="su-01 … su-30",
        weight=35,
        format=("A — usulning nazariy asosi va xatolik tahlili; "
                "B — masalani sonli yechish; C — natijaning "
                "ishonchliligini V&V tartibida asoslash."),
    ),
    Assessment(
        kind="loyiha",
        title="Yakuniy loyiha: to'liq hisoblash zanjiri",
        covers="su-01 … su-30", weight=25,
        format=("Haqiqiy konstruksiya elementi uchun model qurish, sonli "
                "yechish, to'r bo'yicha yaqinlashishni ko'rsatish, "
                "analitik yoki eksperimental ma'lumot bilan validatsiya "
                "qilish va xatolik byudjetini keltirish."),
    ),
]

RESOURCES = [
    Resource("The Finite Element Method: Its Basis and Fundamentals",
             "O. C. Zienkiewicz, R. L. Taylor, J. Z. Zhu", "7-nashr",
             "asosiy",
             "FEM ning eng nufuzli va to'liq darsligi."),
    Resource("An Introduction to the Finite Element Method", "J. N. Reddy",
             "4-nashr", "asosiy",
             "Variatsion asosdan boshlangan aniq va o'qishli bayon."),
    Resource("The Finite Element Method: Linear Static and Dynamic Finite "
             "Element Analysis", "T. J. R. Hughes", "—", "asosiy",
             "Matematik jihatdan qat'iy; barqarorlik va yaqinlashish tahlili."),
    Resource("Concepts and Applications of Finite Element Analysis",
             "R. D. Cook, D. S. Malkus, M. E. Plesha, R. J. Witt",
             "4-nashr", "asosiy",
             "Amaliy muhandislik nuqtai nazari; qulflanish va element "
             "sifatiga alohida e'tibor."),
    Resource("Numerical Recipes: The Art of Scientific Computing",
             "W. H. Press va b.", "3-nashr", "asosiy",
             "Sonli usullarning amaliy algoritmlari va ularning tuzoqlari."),
    Resource("Accuracy and Stability of Numerical Algorithms",
             "N. J. Higham", "2-nashr", "qoshimcha",
             "Suzuvchi nuqta arifmetikasi va shartlanganlik bo'yicha "
             "eng chuqur manba."),
    Resource("Finite Difference Methods for Ordinary and Partial "
             "Differential Equations", "R. J. LeVeque", "—", "asosiy",
             "Barqarorlik, yaqinlashish va Laks teoremasining aniq bayoni."),
    Resource("Differential Quadrature and Its Application in Engineering",
             "C. W. Bert, M. Malik / C. Shu", "—", "qoshimcha",
             "DQM usulining asosiy manbasi."),
    Resource("Verification and Validation in Scientific Computing",
             "W. L. Oberkampf, C. J. Roy", "—", "asosiy",
             "V&V, ishlab chiqilgan yechimlar usuli (MMS) va noaniqlik "
             "tahlilining standart manbasi."),
    Resource("MIT 2.092 / 16.920, Stanford ME 335, NAFEMS Benchmarks",
             "MIT OCW, Stanford, NAFEMS", "—", "kurs",
             "Hisoblash mexanikasi kurslari va sanoat etalon masalalari."),
]

SUBJECT = Subject(
    id=SUBJECT_ID,
    code="SU",
    order=5,
    title="Sonli usullar va hisoblash mexanikasi",
    tagline="Analitik yechim mavjud bo'lmaganda mexanikani hisoblash",
    description=(
        "Oldingi to'rt fan mexanika masalalarini qo'yish va analitik "
        "yechishni o'rgatdi, lekin analitik yechim faqat sodda geometriya "
        "va sodda chegaraviy shartlar uchun mavjud. Bu fan har qanday "
        "geometriya va yuklama uchun ishlaydigan sonli apparatni quradi: "
        "xatolik nazariyasidan boshlab, chekli ayirmalar va chekli "
        "elementlar usullari orqali zamonaviy usullar va natijani "
        "tekshirish tartibiga olib chiqadi. Fanning o'ziga xosligi "
        "shundaki, har bir sonli natija oldingi fanlardagi analitik "
        "yechim bilan solishtirib tekshiriladi — shu sababli u butun "
        "kursning yakunlovchi bo'g'ini bo'lib xizmat qiladi."
    ),
    goal=(
        "Mexanika masalasini sonli yechish zanjirini uchdan-uchgacha "
        "qurish: model tanlash, diskretlashtirish, yechish, xatolikni "
        "baholash va natijani verifikatsiya hamda validatsiya qilish."
    ),
    prerequisites_text=(
        "Barcha oldingi to'rt fan. Xususan: nazariy mexanikadan harakat "
        "tenglamalari va variatsion prinsiplar (nm-21…nm-24), "
        "tebranishlar (nm-26…nm-29); materiallar qarshiligidan egilish va "
        "ustuvorlik (mq-13…mq-16, mq-25), statik aniqlanmaydigan tizimlar "
        "(mq-27); tutash muhitlar mexanikasidan tenzorlar, balans "
        "tenglamalari va variatsion prinsiplar (tmm-05, tmm-10, tmm-19); "
        "plastinalar va qobiqlardan asosiy tenglama, yechim usullari, "
        "ustuvorlik va tebranishlar (pq-04, pq-09, pq-10, pq-19, pq-22). "
        "Matematikadan: chiziqli algebra, Teylor qatori, xususiy hosilali "
        "tenglamalar, xususiy qiymatlar masalasi. Dasturlashdan: Python "
        "va NumPy asoslari."
    ),
    modules=MODULES,
    topics=TOPICS,
    assessments=ASSESSMENTS,
    resources=RESOURCES,
    accent="amber",
    depends_on=[
        "nazariy-mexanika",
        "materiallar-qarshiligi",
        "tutash-muhitlar",
        "plastinalar-qobiqlar",
    ],
)
