"""1-fan: Nazariy mexanika (kod: NM).

Zanjirdagi o'rni: butun platformaning poydevori. Bu yerda shakllangan
kinematika → dinamika → saqlanish qonunlari → analitik mexanika → tebranishlar
chizig'i keyingi to'rt fanning hammasida ishlatiladi.
"""

from __future__ import annotations

from content.curriculum.schema import Assessment, Module, Resource, Subject

from .m1_kinematika import TOPICS as _T1
from .m2_dinamika import TOPICS as _T2
from .m3_saqlanish import TOPICS as _T3
from .m4_analitik import TOPICS as _T4
from .m5_tebranishlar import TOPICS as _T5

SUBJECT_ID = "nazariy-mexanika"

MODULES = [
    Module(
        id="nm-m1",
        subject_id=SUBJECT_ID,
        order=1,
        title="Matematik tayanch va kinematika",
        summary=(
            "Vektor algebrasi, koordinata sistemalari va harakatning geometrik "
            "tavsifi. Kuchlar hali kiritilmaydi — avval 'qanday harakatlanadi' "
            "savoliga javob beriladi."
        ),
        outcome=(
            "Talaba istalgan harakatni vektor funksiya sifatida yoza oladi, "
            "tezlik va tezlanishni tabiiy hamda Dekart koordinatalarida hisoblaydi."
        ),
    ),
    Module(
        id="nm-m2",
        subject_id=SUBJECT_ID,
        order=2,
        title="Nyuton dinamikasi, bog'lanishlar va statika",
        summary=(
            "Kuch–massa–tezlanish bog'lanishi, harakat differensial tenglamasi, "
            "bog'lanish reaksiyalari va muvozanat shartlari."
        ),
        outcome=(
            "Talaba mexanik tizim uchun hisob sxemasini tuzib, harakat yoki "
            "muvozanat tenglamalarini yozadi va yechadi."
        ),
    ),
    Module(
        id="nm-m3",
        subject_id=SUBJECT_ID,
        order=3,
        title="Saqlanish qonunlari va energetik usullar",
        summary=(
            "Impuls, impuls momenti, ish va energiya. Inersiya tenzori orqali "
            "qattiq jism dinamikasiga o'tish."
        ),
        outcome=(
            "Talaba masalani integrallashning o'rniga saqlanish qonuni bilan "
            "yechish mumkinligini aniqlaydi va inersiya tavsiflarini hisoblaydi."
        ),
    ),
    Module(
        id="nm-m4",
        subject_id=SUBJECT_ID,
        order=4,
        title="Analitik mexanika",
        summary=(
            "Umumlashgan koordinatalar, variatsion g'oyalar, Lagranj va Gamilton "
            "formalizmi — keyinchalik Ritz va FEM uchun zamin."
        ),
        outcome=(
            "Talaba murakkab bog'lanishli tizim uchun Lagranj tenglamalarini "
            "keltirib chiqaradi va saqlanuvchi kattaliklarni aniqlaydi."
        ),
    ),
    Module(
        id="nm-m5",
        subject_id=SUBJECT_ID,
        order=5,
        title="Tebranishlar va turg'unlik",
        summary=(
            "Bir va ko'p erkinlik darajali tizimlar, modal tahlil, nochiziqli "
            "effektlar. Bu modul plastina/qobiq dinamikasining to'g'ridan-to'g'ri "
            "kirish nuqtasi."
        ),
        outcome=(
            "Talaba xususiy chastota va shakllarni eigenvalue masalasi sifatida "
            "qo'yadi, rezonans xavfini baholaydi."
        ),
    ),
]

TOPICS = [*_T1, *_T2, *_T3, *_T4, *_T5]

ASSESSMENTS = [
    Assessment(
        kind="oraliq",
        title="1-oraliq nazorat: kinematika va Nyuton dinamikasi",
        covers="nm-01 … nm-12",
        weight=20,
        format=(
            "4 ta hisob masalasi (tezlanish tahlili, harakat DT sini integrallash, "
            "bog'lanish reaksiyasi, ishqalanishli muvozanat) + 6 ta konseptual savol."
        ),
    ),
    Assessment(
        kind="oraliq",
        title="2-oraliq nazorat: saqlanish qonunlari va analitik mexanika",
        covers="nm-13 … nm-24",
        weight=20,
        format=(
            "3 ta masala (energiya balansi, inersiya tenzori, Lagranj tenglamasini "
            "keltirib chiqarish) + 1 ta Python topshirig'i (fazaviy portret)."
        ),
    ),
    Assessment(
        kind="yakuniy",
        title="Yakuniy imtihon",
        covers="nm-01 … nm-30",
        weight=35,
        format=(
            "A qismi — nazariy derivatsiya (Lagranj yoki Gamilton tenglamalarini "
            "keltirib chiqarish); B qismi — ko'p erkinlik darajali tizimning modal "
            "tahlili; C qismi — natijani fizik talqin qilish."
        ),
    ),
    Assessment(
        kind="loyiha",
        title="Yakuniy loyiha: mexanik tizim harakatini modellashtirish",
        covers="nm-01 … nm-30",
        weight=25,
        format="Loyiha hisoboti + ishlaydigan Python kodi + grafiklar + xulosa.",
    ),
]

RESOURCES = [
    Resource(title="Теоретическая механика", author="A. A. Yablonskiy, V. M. Nikiforova",
             year="klassik", kind="asosiy",
             note="Masalalar va hisob sxemalari uchun asosiy amaliy manba."),
    Resource(title="Курс теоретической механики", author="S. M. Targ", year="klassik",
             kind="asosiy", note="Statika–kinematika–dinamika izchilligi namunasi."),
    Resource(title="Classical Mechanics", author="H. Goldstein, C. Poole, J. Safko",
             year="3-nashr", kind="asosiy",
             note="Lagranj va Gamilton formalizmi uchun asosiy darslik."),
    Resource(title="Mechanics", author="L. D. Landau, E. M. Lifshitz", year="Vol. 1",
             kind="asosiy", note="Variatsion prinsipdan boshlanadigan qisqa va chuqur bayon."),
    Resource(title="Engineering Mechanics: Dynamics", author="J. L. Meriam, L. G. Kraige",
             year="klassik", kind="qoshimcha",
             note="Muhandislik qo'llanilishlari va amaliy masalalar."),
    Resource(title="Vibration Problems in Engineering", author="S. P. Timoshenko",
             year="klassik", kind="qoshimcha",
             note="Tebranishlar moduli uchun tarixiy va amaliy asos."),
    Resource(title="Analytical Mechanics", author="L. N. Hand, J. D. Finch", year="—",
             kind="qoshimcha", note="Fazaviy fazo va kanonik formalizm bo'yicha tushunarli bayon."),
    Resource(title="MIT 8.01 / 2.003 Dynamics and Control", author="MIT OCW", year="—",
             kind="kurs", note="Kinematika va tizim dinamikasi bo'yicha kurs tuzilmasi namunasi."),
    Resource(title="Universitet 'Nazariy mexanika' tipovoy dasturi", author="Texnika oliy ta'limi",
             year="—", kind="kurs",
             note="Statika–kinematika–dinamika–analitik mexanika ketma-ketligi asos qilib olindi."),
]

SUBJECT = Subject(
    id=SUBJECT_ID,
    code="NM",
    order=1,
    title="Nazariy mexanika",
    tagline="Harakat, kuch va energiyaning matematik tili",
    description=(
        "Nazariy mexanika — mexanik harakatning umumiy qonunlarini o'rganadigan "
        "fan. Kurs vektor kinematikasidan boshlanib, Nyuton dinamikasi, saqlanish "
        "qonunlari, analitik mexanika (Lagranj va Gamilton) orqali tebranishlar "
        "nazariyasi va modal tahlilga olib chiqadi. Bu yerda o'rganilgan har bir "
        "tushuncha — muvozanat, ish, energiya, inersiya tenzori, eigenvalue "
        "masalasi — keyingi to'rtta fanda qayta ishlatiladi."
    ),
    goal=(
        "Real mexanik tizimni hisob sxemasiga keltirish, uning harakat "
        "tenglamalarini yozish, yechish va natijani fizik jihatdan talqin qilish "
        "ko'nikmasini shakllantirish."
    ),
    prerequisites_text=(
        "Maktab fizikasi va matematik analiz asoslari. Kerakli vektor algebrasi, "
        "differensial tenglamalar va chiziqli algebra elementlari kurs ichida "
        "qisqacha qaytariladi (nm-01, nm-08, nm-17, nm-28)."
    ),
    modules=MODULES,
    topics=TOPICS,
    assessments=ASSESSMENTS,
    resources=RESOURCES,
    accent="teal",
    depends_on=[],
)
