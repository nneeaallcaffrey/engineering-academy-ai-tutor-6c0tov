"""SU / 4-modul: Chekli elementlar usulining ilovalari (su-19 … su-24)."""

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
M = "su-m4"


def _lesson(problem, concepts, derivation, meaning, equations, conditions,
            worked, computation, visual, interp, mistakes, quiz, bridge,
            research, manim_ref=None):
    return Lesson(
        physical_problem=problem, concepts=concepts, derivation=derivation,
        formula_meaning=meaning, equations=equations, conditions=conditions,
        worked_example=worked, computation=computation, visualization=visual,
        interpretation=interp, common_mistakes=mistakes, quiz=quiz,
        bridge_to_next=bridge, research_extension=research, manim=manim_ref,
    )


TOPICS = [
    # ------------------------------------------------------------------ su-19
    Topic(
        id="su-19",
        subject_id=S, module_id=M, order=19,
        title="Ferma va sterjen elementlari",
        description=(
            "Bir o'lchovli element global koordinatalarda, yo'naltiruvchi "
            "kosinuslar va almashtirish matritsasi, fazoviy ferma, "
            "sterjen kuchlarini tiklash va boshlang'ich (termik) "
            "deformatsiyalar."
        ),
        learning_objective=(
            "Ferma masalasini FEM bilan uchdan-uchgacha yechish va "
            "natijani statik aniqlanadigan hamda aniqlanmaydigan "
            "tizimlarda analitik yechim bilan tekshirish."
        ),
        prerequisites=["su-18", "mq-27", "nm-05"],
        mathematical_core=(
            "$\\mathbf{k} = \\frac{EA}{L}\\mathbf{T}^T\\mathbf{T}$, "
            "$\\mathbf{T} = [-c,\\,-s,\\,c,\\,s]$; "
            "$N = EA\\,\\mathbf{T}\\mathbf{u}/L - EA\\alpha\\Delta T$."
        ),
        engineering_application=(
            "Ko'prik va tom fermalari, kran strelalari, minora va antenna "
            "konstruksiyalari, fazoviy qafas tizimlari."
        ),
        computational_component=(
            "Ferma yechuvchisini qurish, sterjen kuchlarini tiklash, "
            "termik yuklarni qo'llash va statik aniqlikni tekshirish."
        ),
        visualization_component=(
            "Deformatsiyalangan shakl, sterjen kuchlari rang bilan, "
            "cho'zilish va siqilish ajratilgan holda."
        ),
        research_extension=(
            "Ferma topologiyasini optimallashtirishni o'rganing: "
            "Mishel fermalari va zamonaviy topologik "
            "optimallashtirishning bog'lanishi."
        ),
        difficulty="orta",
        previous_link=(
            "3-modulda FEM ning butun nazariy apparati qurildi. Endi uni "
            "eng sodda va eng aniq holatga qo'llaymiz: ferma. Bu yerda "
            "FEM yechimi aniq yechim bilan AYNAN mos tushadi va shu "
            "sababli u kodni tekshirish uchun ideal etalon."
        ),
        next_topic="su-20",
        estimated_minutes=80,
        tags=["ferma", "almashtirish matritsasi", "termik yuk",
              "statik aniqlanmaydigan"],
        lesson=_lesson(
            problem=(
                "Yuqori kuchlanishli elektr "
                "uzatish minorasi loyihalanmoqda: "
                "bir necha yuz sterjendan iborat "
                "fazoviy ferma. Qo'lda hisoblash "
                "mumkin emas — tugunlar usuli "
                "faqat statik aniqlanadigan "
                "tizimlarda ishlaydi, bu minora "
                "esa ko'p marta aniqlanmaydigan. "
                "Bundan tashqari qishda "
                "harorat $-40°C$ ga tushadi, "
                "yozda esa quyoshda metall "
                "$+60°C$ gacha qiziydi. "
                "Aniqlanmaydigan tizimda bu "
                "harorat farqi **tashqi yuksiz "
                "ham** sterjenlarda kuch hosil "
                "qiladi. Shu ikki masalani — "
                "aniqlanmaydiganlik va termik "
                "yuk — bitta umumiy apparat "
                "bilan qanday yechish mumkin?"
            ),
            concepts=[
                c("Ferma elementi",
                  "Faqat o'q bo'ylab kuch "
                  "uzatadigan ikki tugunli "
                  "element; tugunlar sharnirli, "
                  "moment uzatilmaydi."),
                c("Yo'naltiruvchi kosinuslar",
                  "$c = \\cos\\varphi = "
                  "\\Delta x/L$, "
                  "$s = \\sin\\varphi = "
                  "\\Delta y/L$ — elementning "
                  "fazodagi yo'nalishi."),
                c("Almashtirish matritsasi "
                  "$\\mathbf{T}$",
                  "Global tugun ko'chishlaridan "
                  "o'q bo'ylab cho'zilishni "
                  "ajratib oladi: "
                  "$\\Delta L = "
                  "\\mathbf{T}\\mathbf{u}$."),
                c("Statik aniqlanadigan tizim",
                  "Sterjen kuchlari faqat "
                  "muvozanatdan topiladi va "
                  "**kesim yuzalariga bog'liq "
                  "emas** (mq-27)."),
                c("Statik aniqlanmaydigan tizim",
                  "Kuchlar bikrliklar "
                  "nisbatiga bog'liq; "
                  "moslik sharti kerak."),
                c("Boshlang'ich deformatsiya",
                  "Termik kengayish, montaj "
                  "noaniqligi, oldindan "
                  "taranglash — "
                  "$\\varepsilon_0$ ekvivalent "
                  "tugun yuklariga "
                  "aylantiriladi."),
            ],
            derivation=[
                d("1. Mahalliy koordinatadagi "
                  "element",
                  r"\mathbf{k}_{loc} = "
                  r"\frac{EA}{L}\begin{bmatrix}"
                  r"1 & -1\\ -1 & 1\end{bmatrix}",
                  "su-15 dagi sterjen elementi. "
                  "Endi uni fazoda ixtiyoriy "
                  "burchakka burishimiz kerak."),
                d("2. Ko'chishlarning proyeksiyasi",
                  r"u_{loc} = u\cos\varphi + "
                  r"v\sin\varphi = cu + sv",
                  "Global ko'chishning o'q "
                  "bo'ylab tashkil etuvchisi. "
                  "Ko'ndalang tashkil etuvchi "
                  "cho'zilishga ta'sir qilmaydi "
                  "(kichik ko'chishlar "
                  "taxmini)."),
                d("3. Cho'zilish",
                  r"\Delta L = (cu_2 + sv_2) - "
                  r"(cu_1 + sv_1) = "
                  r"\mathbf{T}\mathbf{u}",
                  "$\\mathbf{T} = "
                  "[-c,\\ -s,\\ c,\\ s]$ — "
                  "atigi to'rtta son, va butun "
                  "geometriya shunga "
                  "to'planadi."),
                d("4. Global bikrlik matritsasi",
                  r"\mathbf{k} = \frac{EA}{L}"
                  r"\mathbf{T}^T\mathbf{T}",
                  "**Asosiy natija.** Energiya "
                  "invariant: "
                  "$U = \\frac{EA}{2L}"
                  "(\\Delta L)^2 = "
                  "\\frac{EA}{2L}"
                  "(\\mathbf{T}\\mathbf{u})^2$, "
                  "demak "
                  "$\\mathbf{k} = "
                  "\\partial^2U/"
                  "\\partial\\mathbf{u}^2$."),
                d("5. Yoyilgan ko'rinishi",
                  r"\mathbf{k} = \frac{EA}{L}"
                  r"\begin{bmatrix} c^2 & cs & "
                  r"-c^2 & -cs\\ cs & s^2 & -cs "
                  r"& -s^2\\ -c^2 & -cs & c^2 & "
                  r"cs\\ -cs & -s^2 & cs & s^2"
                  r"\end{bmatrix}",
                  "Klassik ferma element "
                  "matritsasi. Rangi 1 — bitta "
                  "element faqat bitta "
                  "deformatsiya rejimiga "
                  "qarshilik ko'rsatadi."),
                d("6. Fazoviy fermaga "
                  "kengaytirish",
                  r"\mathbf{T} = [-c_x,\,-c_y,\,"
                  r"-c_z,\,c_x,\,c_y,\,c_z]",
                  "**Hech narsa o'zgarmaydi.** "
                  "Faqat yo'naltiruvchi "
                  "kosinuslar soni uchtaga "
                  "chiqadi; "
                  "$\\mathbf{k} = "
                  "\\frac{EA}{L}"
                  "\\mathbf{T}^T\\mathbf{T}$ "
                  "formulasi aynan o'sha."),
                d("7. Sterjen kuchini tiklash",
                  r"N = EA\,\varepsilon = "
                  r"\frac{EA}{L}\mathbf{T}"
                  r"\mathbf{u}_e",
                  "Yechimdan keyin har bir "
                  "element uchun alohida. "
                  "Musbat — cho'zilish, "
                  "manfiy — siqilish."),
                d("8. Boshlang'ich deformatsiya",
                  r"N = EA\left(\varepsilon - "
                  r"\varepsilon_0\right), \qquad "
                  r"\varepsilon_0 = "
                  r"\alpha_T\Delta T",
                  "Termik kengayish "
                  "kuchlanish hosil qilmaydi "
                  "— faqat **to'sqinlik "
                  "qilingan** kengayish "
                  "qiladi."),
                d("9. Ekvivalent termik yuk",
                  r"\mathbf{f}_0 = EA"
                  r"\alpha_T\Delta T\,"
                  r"\mathbf{T}^T",
                  "**Amaliy qadam.** Termik "
                  "ta'sir oddiy tugun yukiga "
                  "aylantiriladi; yechuvchi "
                  "o'zgarmaydi. Yechimdan "
                  "keyin $N$ dan "
                  "$EA\\alpha_T\\Delta T$ "
                  "ayiriladi."),
                d("10. Statik aniqlik darajasi",
                  r"i = m + r - 2n \ "
                  r"(\text{tekis}), \qquad "
                  r"i = m + r - 3n \ "
                  r"(\text{fazoviy})",
                  "$m$ — sterjenlar, $r$ — "
                  "tayanch reaksiyalari, "
                  "$n$ — tugunlar. "
                  "$i = 0$ — aniqlanadigan, "
                  "$i > 0$ — aniqlanmaydigan."),
                d("11. Aniqlanadigan tizimning "
                  "xossasi",
                  r"i = 0 \;\Longrightarrow\; "
                  r"N \ \text{faqat "
                  r"muvozanatdan; } "
                  r"\partial N/\partial A = 0",
                  "**Muhim tekshiruv.** "
                  "Kesim yuzalarini "
                  "o'zgartirsangiz kuchlar "
                  "o'zgarmaydi. Kod buni "
                  "aynan tasdiqlaydi."),
                d("12. Aniqlanmaydigan tizimda "
                  "termik kuch",
                  r"i > 0 \;\Longrightarrow\; "
                  r"\Delta T \ \text{tashqi "
                  r"yuksiz ham } N \ne 0",
                  "**Amaliy xavf.** "
                  "Aniqlanadigan tizimda "
                  "termik yuk kuch hosil "
                  "qilmaydi (erkin "
                  "kengayadi), "
                  "aniqlanmaydiganda esa "
                  "qiladi — va u loyihaviy "
                  "yukdan katta bo'lishi "
                  "mumkin (mq-27)."),
            ],
            meaning=(
                "Bu mavzuning matematik "
                "mazmuni 4-qadamda bitta "
                "formulaga sig'adi: "
                "$\\mathbf{k} = "
                "\\frac{EA}{L}\\mathbf{T}^T"
                "\\mathbf{T}$. Butun "
                "geometriya — elementning "
                "fazodagi yo'nalishi — "
                "$\\mathbf{T}$ dagi to'rtta "
                "(fazoda oltita) songa "
                "to'planadi, fizika esa "
                "$EA/L$ ko'paytuvchisida "
                "qoladi. 6-qadam shuning "
                "uchun deyarli bepul keladi: "
                "fazoviy fermaga o'tishda "
                "formulalar umuman "
                "o'zgarmaydi, faqat "
                "$\\mathbf{T}$ uzayadi. Bu "
                "izoparametrik g'oyaning "
                "(su-14) eng sodda "
                "ko'rinishi va u dastur "
                "tuzilishini ham "
                "belgilaydi: bitta element "
                "funksiyasi ikki va uch "
                "o'lchovda ham ishlaydi. "
                "Ammo mavzuning muhandislik "
                "mazmuni 11- va 12-qadamlarda. "
                "Statik aniqlanadigan "
                "fermada sterjen kuchlari "
                "faqat muvozanatdan kelib "
                "chiqadi, demak ular "
                "kesim yuzalariga umuman "
                "bog'liq emas. Sterjenni "
                "ikki barobar "
                "qalinlashtiring — kuch "
                "o'zgarmaydi, faqat "
                "kuchlanish kamayadi. "
                "Aniqlanmaydigan tizimda "
                "esa aksincha: kuchlar "
                "bikrliklar **nisbatiga** "
                "bog'liq va bitta "
                "sterjenni qalinlashtirish "
                "unga ko'proq kuch "
                "tortadi. Bu mq-27 dagi "
                "asosiy g'oya va u bu "
                "yerda sonli tasdiqlanadi. "
                "12-qadam esa amaliyotda "
                "eng ko'p e'tibordan "
                "chetda qoladigan xavfni "
                "ko'rsatadi. Termik "
                "kengayish o'z-o'zidan "
                "kuchlanish hosil "
                "qilmaydi — faqat unga "
                "to'sqinlik qilinganda "
                "qiladi. Aniqlanadigan "
                "ferma erkin kengayadi va "
                "haroratga befarq; "
                "aniqlanmaydigan ferma "
                "esa o'zini o'zi bo'g'adi. "
                "Yuz gradusli mavsumiy "
                "farq po'latda "
                "$\\alpha_T\\Delta T = "
                "0{,}0012$ deformatsiya "
                "beradi va bu oquvchanlik "
                "chegarasidagi "
                "deformatsiyaning "
                "taxminan chorak qismi — "
                "ya'ni termik kuchlanish "
                "loyihaviy yukdan "
                "kattaroq bo'lishi "
                "mumkin."
            ),
            equations=[
                eq(r"\mathbf{k} = \frac{EA}{L}"
                   r"\mathbf{T}^T\mathbf{T}, "
                   r"\qquad \mathbf{T} = "
                   r"[-c,\ -s,\ c,\ s]",
                   "Ferma elementining global "
                   "bikrlik matritsasi.",
                   "Element matritsasi"),
                eq(r"N = \frac{EA}{L}\mathbf{T}"
                   r"\mathbf{u}_e - "
                   r"EA\,\alpha_T\Delta T",
                   "Sterjen kuchini tiklash, "
                   "termik qism ayirilgan holda.",
                   "Kuchni tiklash"),
                eq(r"\mathbf{f}_0 = "
                   r"EA\,\alpha_T\Delta T\,"
                   r"\mathbf{T}^T",
                   "Boshlang'ich "
                   "deformatsiyaning ekvivalent "
                   "tugun yuki.", "Termik yuk"),
                eq(r"i = m + r - 2n, \qquad "
                   r"i = 0 \Rightarrow "
                   r"\frac{\partial N}"
                   r"{\partial A} = 0",
                   "Statik aniqlik darajasi va "
                   "aniqlanadigan tizimning "
                   "xossasi.",
                   "Statik aniqlik"),
            ],
            conditions=(
                "**Ferma modelining "
                "taxminlari:**\n"
                "1. Tugunlar ideal sharnirli — "
                "moment uzatilmaydi;\n"
                "2. Yuklar faqat tugunlarga "
                "qo'yiladi;\n"
                "3. Sterjen o'qlari bitta "
                "nuqtada kesishadi;\n"
                "4. Ko'chishlar kichik — "
                "geometriya o'zgarmaydi "
                "(su-24 da bekor qilinadi).\n\n"
                "**Yechimdan oldin:**\n"
                "- Kinematik o'zgaruvchanlikni "
                "tekshiring: "
                "$i < 0$ bo'lsa mexanizm;\n"
                "- $i \\ge 0$ bo'lsa ham "
                "geometrik o'zgaruvchanlik "
                "bo'lishi mumkin (bir "
                "chiziqda yotgan "
                "sterjenlar) — buni "
                "$\\mathbf{K}$ ning "
                "singulyarligi ochadi "
                "(su-15).\n\n"
                "**Yechimdan keyin majburiy "
                "tekshiruvlar:**\n"
                "1. Har bir tugunda "
                "muvozanat: "
                "$\\sum N_i\\mathbf{T}_i + "
                "\\mathbf{P} = 0$;\n"
                "2. Reaksiyalar tashqi yukni "
                "muvozanatlaydi;\n"
                "3. Siqilgan sterjenlar "
                "ustuvorlikka tekshirilsin "
                "(mq-25) — ferma "
                "hisobining eng ko'p "
                "unutiladigan qismi;\n"
                "4. Termik holatda tashqi "
                "yuk bo'lmasa reaksiyalar "
                "o'z-o'zini "
                "muvozanatlashi kerak.\n\n"
                "**Nol sterjenlar:** ba'zi "
                "sterjenlarda kuch aynan "
                "nol chiqadi. Bu xato emas "
                "— ular ustuvorlikni "
                "ta'minlash uchun kerak "
                "va modeldan olib "
                "tashlanmasligi lozim."
            ),
            worked=WorkedExample(
                statement=(
                    "Uch sterjenli simmetrik "
                    "ferma: ikkita qiya sterjen "
                    "vertikaldan $\\alpha = 30°$ "
                    "burchak ostida "
                    "($A_1 = 10$ sm²), o'rtada "
                    "vertikal sterjen "
                    "($A_2 = 15$ sm²), balandlik "
                    "$L = 2$ m. Pastki tugunga "
                    "$P = 100$ kN vertikal yuk "
                    "qo'yilgan. Sterjen "
                    "kuchlarini toping."
                ),
                given=[
                    r"\alpha = 30^\circ, \quad "
                    r"L = 2\ \text{m}, \quad "
                    r"P = 100\ \text{kN}",
                    r"A_1 = 10\ \text{sm}^2, \quad "
                    r"A_2 = 15\ \text{sm}^2, \quad "
                    r"E = 2{,}1\cdot10^5\ "
                    r"\text{MPa}",
                ],
                steps=[
                    st(r"i = m + r - 2n = 3 + 6 - "
                       r"2\cdot4 = 1",
                       "**Bir marta statik "
                       "aniqlanmaydigan** — "
                       "muvozanat yetarli emas, "
                       "moslik kerak."),
                    st(r"\text{Pastki tugun } "
                       r"\delta \ \text{ga "
                       r"tushsin}",
                       "Bitta noma'lum — "
                       "simmetriya tufayli "
                       "faqat vertikal "
                       "ko'chish."),
                    st(r"\Delta L_2 = \delta, "
                       r"\qquad \Delta L_1 = "
                       r"\delta\cos\alpha",
                       "**Moslik sharti.** Qiya "
                       "sterjenning cho'zilishi "
                       "— vertikal ko'chishning "
                       "o'q bo'ylab "
                       "proyeksiyasi."),
                    st(r"L_1 = \frac{L}{\cos\alpha} "
                       r"\;\Rightarrow\; N_1 = "
                       r"\frac{EA_1\delta"
                       r"\cos\alpha}{L/\cos\alpha} "
                       r"= \frac{EA_1\delta"
                       r"\cos^2\alpha}{L}",
                       "Qiya sterjendagi kuch."),
                    st(r"N_2 = \frac{EA_2\delta}{L}",
                       "Vertikal sterjendagi "
                       "kuch."),
                    st(r"2N_1\cos\alpha + N_2 = P",
                       "**Muvozanat** pastki "
                       "tugunda (vertikal)."),
                    st(r"\frac{E\delta}{L}\left("
                       r"2A_1\cos^3\alpha + A_2"
                       r"\right) = P",
                       "Ikkalasini "
                       "birlashtiramiz."),
                    st(r"\delta = \frac{PL}"
                       r"{E\left(2A_1\cos^3\alpha "
                       r"+ A_2\right)}",
                       "Ko'chish topildi."),
                    st(r"2A_1\cos^3\alpha + A_2 = "
                       r"2(10)(0{,}6495) + 15 = "
                       r"27{,}99\ \text{sm}^2",
                       "$\\cos30° = 0{,}8660$, "
                       "$\\cos^330° = 0{,}6495$."),
                    st(r"N_2 = \frac{PA_2}"
                       r"{2A_1\cos^3\alpha + A_2} "
                       r"= \frac{100 \cdot 15}"
                       r"{27{,}99} = 53{,}59\ "
                       r"\text{kN}",
                       "**Vertikal sterjen "
                       "yukning yarmidan "
                       "ko'prog'ini oladi.**"),
                    st(r"N_1 = \frac{PA_1"
                       r"\cos^2\alpha}"
                       r"{2A_1\cos^3\alpha + A_2} "
                       r"= \frac{100 \cdot 10 "
                       r"\cdot 0{,}75}{27{,}99} = "
                       r"26{,}79\ \text{kN}",
                       "Har bir qiya sterjen."),
                    st(r"2(26{,}79)(0{,}8660) + "
                       r"53{,}59 = 46{,}41 + "
                       r"53{,}59 = 100 \ "
                       r"\checkmark",
                       "**Muvozanat "
                       "tekshiruvi bajarildi.**"),
                ],
                answer=(
                    "$N_1 = N_3 = 26{,}79$ kN "
                    "(cho'zilish), "
                    "$N_2 = 53{,}59$ kN "
                    "(cho'zilish), "
                    "$\\delta = 0{,}340$ mm. "
                    "Kod bu qiymatlarni "
                    "$10^{-14}$% aniqlikda "
                    "takrorlaydi. Diqqat: "
                    "kuchlar kesim yuzalari "
                    "**nisbatiga** bog'liq — "
                    "$A_1$ ni uch barobar "
                    "oshirsangiz $N_2$ "
                    "53,59 dan 27,79 kN ga "
                    "tushadi."
                ),
                engineering_note=(
                    "Javobdagi eng muhim "
                    "narsa — kuchlarning "
                    "kesim yuzalariga "
                    "bog'liqligi. Statik "
                    "aniqlanadigan fermada "
                    "bunday bo'lmaydi: u "
                    "yerda kuchlar faqat "
                    "geometriya va yukdan "
                    "kelib chiqadi. Bu ikki "
                    "holat orasidagi farq "
                    "loyihalashda hal "
                    "qiluvchi. "
                    "Aniqlanmaydigan "
                    "tizimda 'bu sterjen "
                    "kuchlanishi yuqori "
                    "ekan, uni "
                    "qalinlashtiraman' "
                    "degan tabiiy qaror "
                    "**teskari natija "
                    "berishi mumkin**: "
                    "qalinlashtirilgan "
                    "sterjen o'ziga ko'proq "
                    "kuch tortadi va "
                    "kuchlanish kutilgandek "
                    "kamaymaydi. To'g'ri "
                    "yo'l — iteratsiya: "
                    "kesimni o'zgartirib, "
                    "hisobni qayta "
                    "yuritish. Ikkinchi "
                    "amaliy nuqta: "
                    "hisobda barcha uchala "
                    "sterjen cho'zilgan "
                    "chiqdi, shuning uchun "
                    "ustuvorlik masalasi "
                    "yo'q. Agar yuk "
                    "yo'nalishi teskari "
                    "bo'lsa, hammasi "
                    "siqiladi va o'shanda "
                    "mq-25 dagi Eyler "
                    "kuchini tekshirish "
                    "**majburiy** bo'ladi. "
                    "Ferma hisobida eng "
                    "ko'p uchraydigan "
                    "jiddiy xato — "
                    "siqilgan sterjenlarni "
                    "faqat "
                    "mustahkamlikka "
                    "tekshirib, "
                    "ustuvorlikni "
                    "unutish."
                ),
            ),
            computation=Computation(
                caption=(
                    "Ferma yechuvchisini qurish, "
                    "analitik yechim bilan "
                    "solishtirish, statik "
                    "aniqlik ta'sirini va termik "
                    "yuklarni o'rganish."
                ),
                code='''"""Ferma va sterjen elementlari."""
import numpy as np
from labkit import PARAMS, note, series, table, value

alpha_deg = float(PARAMS.get("alpha_deg", 30.0))
A1_cm2 = float(PARAMS.get("A1_cm2", 10.0))
A2_cm2 = float(PARAMS.get("A2_cm2", 15.0))
P_kN = float(PARAMS.get("P_kN", 100.0))
dT_bar2 = float(PARAMS.get("dT_bar2", 50.0))

E = 2.1e11
alpha_T = 1.2e-5
Lv = 2.0


def truss(nodes, elems, areas, fixed, loads, dT=None):
    """Tekis yoki fazoviy ferma. nodes: (n, dim) massiv."""
    nodes = np.asarray(nodes, dtype=float)
    dim = nodes.shape[1]
    nn = len(nodes)
    ndof = dim*nn
    K = np.zeros((ndof, ndof))
    F = np.zeros(ndof)
    Ts, Ls = [], []
    for e, (i, j) in enumerate(elems):
        dvec = nodes[j] - nodes[i]
        Le = float(np.linalg.norm(dvec))
        cs = dvec/Le                      # yo'naltiruvchi kosinuslar
        T = np.concatenate([-cs, cs])     # su-19, 3-qadam
        Ts.append(T)
        Ls.append(Le)
        idx = [dim*i + k for k in range(dim)] + \\
              [dim*j + k for k in range(dim)]
        K[np.ix_(idx, idx)] += E*areas[e]/Le*np.outer(T, T)
        if dT is not None and dT[e] != 0.0:
            F[idx] += E*areas[e]*alpha_T*dT[e]*T
    for dof, val in loads.items():
        F[dof] += val
    free = np.setdiff1d(np.arange(ndof), fixed)
    u = np.zeros(ndof)
    u[free] = np.linalg.solve(K[np.ix_(free, free)], F[free])
    N = np.zeros(len(elems))
    for e, (i, j) in enumerate(elems):
        idx = [dim*i + k for k in range(dim)] + \\
              [dim*j + k for k in range(dim)]
        N[e] = E*areas[e]*(Ts[e] @ u[idx])/Ls[e]
        if dT is not None and dT[e] != 0.0:
            N[e] -= E*areas[e]*alpha_T*dT[e]
    return u, N, K @ u - F, np.array(Ls), Ts


# --- (1) Uch sterjenli aniqlanmaydigan ferma: ANALITIK tekshiruv ---
al = np.radians(alpha_deg)
A1, A2 = A1_cm2*1e-4, A2_cm2*1e-4
P = P_kN*1e3
nodes3 = np.array([[-Lv*np.tan(al), Lv], [0.0, Lv],
                   [Lv*np.tan(al), Lv], [0.0, 0.0]])
elems3 = [(0, 3), (1, 3), (2, 3)]
areas3 = [A1, A2, A1]
u3, N3, R3, L3, T3 = truss(nodes3, elems3, areas3,
                           [0, 1, 2, 3, 4, 5], {7: -P})

den = 2*A1*np.cos(al)**3 + A2
N1_ex = P*A1*np.cos(al)**2/den
N2_ex = P*A2/den
d_ex = P*Lv/(E*den)
value("N1 (qiya sterjen), sonli", float(N3[0])/1e3, "kN")
value("N1, analitik", N1_ex/1e3, "kN")
value("N1 nisbiy xato", abs(N3[0] - N1_ex)/N1_ex*100, "%")
value("N2 (vertikal sterjen), sonli", float(N3[1])/1e3, "kN")
value("N2, analitik", N2_ex/1e3, "kN")
value("N2 nisbiy xato", abs(N3[1] - N2_ex)/N2_ex*100, "%")
value("Ko'chish delta, sonli", float(-u3[7])*1e3, "mm")
value("Ko'chish delta, analitik", d_ex*1e3, "mm")
value("Tugun muvozanati: 2*N1*cos(a) + N2 - P",
      float(2*N3[0]*np.cos(al) + N3[1] - P), "N")
value("Reaksiyalar yig'indisi (y)",
      float(R3[1] + R3[3] + R3[5]), "N")
value("Statik aniqlik darajasi i = m + r - 2n",
      3 + 6 - 2*4, "—")
note(f"Uch sterjenli aniqlanmaydigan fermada FEM analitik yechimni "
     f"{abs(N3[0] - N1_ex)/N1_ex*100:.1e}% aniqlikda takrorladi. Tugun "
     f"muvozanati {abs(2*N3[0]*np.cos(al) + N3[1] - P):.1e} N gacha, "
     f"reaksiyalar esa tashqi yukni aynan muvozanatlaydi. Ferma "
     f"elementi uchun FEM yechimi AYNAN - diskretlashtirish xatosi "
     f"umuman yo'q, chunki sterjen ichida deformatsiya haqiqatan ham "
     f"doimiy va chiziqli shakl funksiyasi buni to'liq ifodalaydi.")

# --- (2) STATIK ANIQLIK: kuchlar kesim yuzasiga bog'liqmi? ---
# (a) aniqlanadigan ferma: ikki sterjen
nd2 = np.array([[0.0, 0.0], [4.0, 0.0], [2.0, 1.5]])
el2 = [(0, 2), (1, 2)]
rows = []
for mult in [1.0, 2.0, 5.0, 10.0]:
    _, Nd, _, _, _ = truss(nd2, el2, [2e-3*mult, 2e-3*mult],
                           [0, 1, 2, 3], {5: -50e3})
    rows.append(["aniqlanadigan (i = 0)", f"{mult:.0f}x",
                 f"{Nd[0]/1e3:.4f}", f"{Nd[1]/1e3:.4f}"])
for mult in [1.0, 2.0, 5.0, 10.0]:
    _, Ni, _, _, _ = truss(nodes3, elems3, [A1*mult, A2, A1*mult],
                           [0, 1, 2, 3, 4, 5], {7: -P})
    rows.append(["aniqlanmaydigan (i = 1)", f"A1 x {mult:.0f}",
                 f"{Ni[0]/1e3:.4f}", f"{Ni[1]/1e3:.4f}"])
table("Kesim yuzasi sterjen kuchlariga ta'sir qiladimi?",
      ["ferma", "yuza o'zgarishi", "N1, kN", "N2, kN"], rows)
th2 = np.arctan2(1.5, 2.0)
value("Aniqlanadigan: analitik N = -P/(2 sin(th))",
      float(-50e3/(2*np.sin(th2)))/1e3, "kN")
note("HAL QILUVCHI FARQ. Statik aniqlanadigan fermada kesim yuzasini "
     "10 barobar oshirsangiz ham sterjen kuchlari AYNAN o'zgarmaydi - "
     "ular faqat muvozanatdan kelib chiqadi. Aniqlanmaydigan fermada "
     "esa A1 ni oshirish N1 ni oshiradi va N2 ni kamaytiradi: qiya "
     "sterjenlar bikrlashib, yukning ko'proq qismini o'ziga tortadi. "
     "Bu mq-27 dagi asosiy g'oya va u loyihalashda muhim: "
     "aniqlanmaydigan tizimda elementni qalinlashtirish unga ko'proq "
     "kuch keltiradi, shuning uchun kesim tanlash ITERATIV jarayon.")

# --- (3) TERMIK yuk: aniqlanadigan va aniqlanmaydigan ---
dT3 = np.array([0.0, dT_bar2, 0.0])
u3t, N3t, R3t, _, _ = truss(nodes3, elems3, areas3,
                            [0, 1, 2, 3, 4, 5], {}, dT=dT3)
d_t_ex = alpha_T*dT_bar2*Lv*A2/(A2 + 2*A1*np.cos(al)**3)
N2_t_ex = -2*E*A1*np.cos(al)**3*alpha_T*dT_bar2*A2 / \\
    (A2 + 2*A1*np.cos(al)**3)
N1_t_ex = E*A1*d_t_ex*np.cos(al)**2/Lv
value("Termik: N2 sonli", float(N3t[1])/1e3, "kN")
value("Termik: N2 analitik", N2_t_ex/1e3, "kN")
value("Termik: N2 nisbiy xato",
      abs(N3t[1] - N2_t_ex)/abs(N2_t_ex)*100, "%")
value("Termik: N1 sonli", float(N3t[0])/1e3, "kN")
value("Termik: N1 analitik", N1_t_ex/1e3, "kN")
value("Termik: ko'chish |delta|", float(abs(u3t[7]))*1e3, "mm")
value("Termik: |delta| analitik", abs(d_t_ex)*1e3, "mm")
value("Termik muvozanat: 2*N1*cos(a) + N2",
      float(2*N3t[0]*np.cos(al) + N3t[1]), "N")
value("Termik: tayanch reaksiyalari yig'indisi (x)",
      float(sum(R3t[dof] for dof in [0, 2, 4])), "N")
value("Termik: tayanch reaksiyalari yig'indisi (y)",
      float(sum(R3t[dof] for dof in [1, 3, 5])), "N")
# aniqlanadigan fermada termik yuk
_, Nd_t, _, _, _ = truss(nd2, el2, [2e-3, 2e-3], [0, 1, 2, 3], {},
                         dT=np.array([dT_bar2, dT_bar2]))
value("Aniqlanadigan fermada termik kuch N",
      float(np.max(np.abs(Nd_t))), "N")
note(f"Aniqlanmaydigan fermada faqat bitta sterjenni {dT_bar2:.0f} "
     f"gradusga qizdirish TASHQI YUKSIZ ham {abs(N3t[1])/1e3:.1f} kN "
     f"kuch hosil qildi - bu {P_kN:.0f} kN loyihaviy yukdan kelgan "
     f"kuchning katta qismi. Kuchlar o'z-o'zini muvozanatlaydi "
     f"(2*N1*cos(a) + N2 = 0) va tayanch reaksiyalari yig'indisi nol - "
     f"ya'ni tashqi kuch yo'q, lekin ichki kuchlar bor. Statik "
     f"ANIQLANADIGAN fermada esa xuddi shunday qizdirish kuch hosil "
     f"qilmaydi: u erkin kengayadi. Termik kuchlanish faqat "
     f"TO'SQINLIK QILINGAN kengayishdan paydo bo'ladi.")

rows_t = []
for dt in [-40.0, -20.0, 0.0, 20.0, 50.0, 60.0]:
    _, Nt, _, _, _ = truss(nodes3, elems3, areas3, [0, 1, 2, 3, 4, 5],
                           {}, dT=np.array([0.0, dt, 0.0]))
    sig = Nt[1]/A2/1e6
    rows_t.append([f"{dt:+.0f}", f"{Nt[0]/1e3:+.2f}", f"{Nt[1]/1e3:+.2f}",
                   f"{sig:+.1f}"])
table("Mavsumiy harorat o'zgarishining ta'siri (tashqi yuksiz)",
      ["dT, C", "N1, kN", "N2, kN", "sigma_2, MPa"], rows_t)
series("Termik kuch N2", [-40, -20, 0, 20, 50, 60],
       [float(truss(nodes3, elems3, areas3, [0, 1, 2, 3, 4, 5], {},
                    dT=np.array([0.0, dt, 0.0]))[1][1])/1e3
        for dt in [-40, -20, 0, 20, 50, 60]],
       xlabel="dT, C", ylabel="N2, kN")

# --- (4) FAZOVIY ferma: bir xil kod, uch o'lchov ---
h_t = 6.0
base = 2.0
s3 = np.sqrt(3.0)/2.0            # aynan, 0.866 taqribiy emas
nodes_s = np.array([[base, 0.0, 0.0], [-base/2, base*s3, 0.0],
                    [-base/2, -base*s3, 0.0], [0.0, 0.0, h_t]])
elems_s = [(0, 3), (1, 3), (2, 3)]
A_s = 5e-4
Pz = -80e3
fixed_s = list(range(9))
u_s, N_s, R_s, L_s, T_s = truss(nodes_s, elems_s, [A_s]*3, fixed_s,
                                {11: Pz})
cos_t = h_t/np.sqrt(h_t**2 + base**2)
N_s_ex = Pz/(3*cos_t)
value("Fazoviy ferma: sterjen uzunligi", float(L_s[0]), "m")
value("Fazoviy ferma: N sonli", float(N_s[0])/1e3, "kN")
value("Fazoviy ferma: N analitik", N_s_ex/1e3, "kN")
value("Fazoviy ferma: nisbiy xato",
      abs(N_s[0] - N_s_ex)/abs(N_s_ex)*100, "%")
value("Fazoviy: uchta sterjen kuchi bir xilmi",
      float(np.max(N_s) - np.min(N_s)), "N")
# Muvozanat: (K u)_dof - F_dof = 0, ya'ni sum(N*T) - F = 0
value("Fazoviy: z bo'yicha muvozanat",
      float(sum(N_s[e]*T_s[e][5] for e in range(3)) - Pz), "N")
note("Fazoviy fermada element formulasi umuman o'zgarmadi - faqat "
     "yo'naltiruvchi kosinuslar uchtaga chiqdi. Bitta funksiya ikki "
     "va uch o'lchovda ham ishlaydi. Uchta simmetrik sterjendagi "
     "kuchlar mashina aniqligida teng va analitik P/(3 cos(t)) "
     "qiymatiga mos tushdi.")

# --- (5) KO'PRIK FERMASI: qo'lda hisoblab bo'lmaydigan masala ---
np_span, hgt, bay = 6, 3.0, 4.0
nd_b = []
for i in range(np_span + 1):
    nd_b.append([i*bay, 0.0])
for i in range(np_span + 1):
    nd_b.append([i*bay, hgt])
nd_b = np.array(nd_b)
top = np_span + 1
el_b = []
for i in range(np_span):
    el_b.append((i, i + 1))                 # pastki kamar
    el_b.append((top + i, top + i + 1))     # yuqori kamar
for i in range(np_span + 1):
    el_b.append((i, top + i))               # tik
for i in range(np_span):
    el_b.append((i, top + i + 1))           # diagonal
    el_b.append((i + 1, top + i))           # qarama-qarshi diagonal
A_b = [3e-3]*len(el_b)
loads_b = {2*i + 1: -40e3 for i in range(1, np_span)}
fixed_b = [0, 1, 2*np_span + 1]
u_b, N_b, R_b, L_b, T_b = truss(nd_b, el_b, A_b, fixed_b, loads_b)
m_b, r_b, n_b = len(el_b), len(fixed_b), len(nd_b)
value("Ko'prik fermasi: sterjenlar", m_b, "—")
value("Ko'prik fermasi: tugunlar", n_b, "—")
value("Statik aniqlik darajasi i", m_b + r_b - 2*n_b, "—")
value("Maks cho'zilish", float(np.max(N_b))/1e3, "kN")
value("Maks siqilish", float(np.min(N_b))/1e3, "kN")
value("Maks tugun ko'chishi", float(np.max(np.abs(u_b)))*1e3, "mm")
# HAR BIR tugunda muvozanat: sum(N*T) - F = 0
resid = np.zeros(2*n_b)
for e, (i, j) in enumerate(el_b):
    idx = [2*i, 2*i + 1, 2*j, 2*j + 1]
    resid[idx] += N_b[e]*T_b[e]
for dof, val in loads_b.items():
    resid[dof] -= val
free_b = np.setdiff1d(np.arange(2*n_b), fixed_b)
value("Erkin tugunlarda maks muvozanat qoldig'i",
      float(np.max(np.abs(resid[free_b]))), "N")
value("Reaksiyalar yig'indisi (y)",
      float(sum(R_b[dof] for dof in fixed_b if dof % 2 == 1)), "N")
value("Tashqi yuk yig'indisi", float(-sum(loads_b.values())), "N")
n_zero = int(np.sum(np.abs(N_b) < 1e-6*np.max(np.abs(N_b))))
value("Nol sterjenlar soni", n_zero, "—")
series("Sterjen kuchlari", list(range(1, len(el_b) + 1)),
       (N_b/1e3).tolist(), xlabel="element", ylabel="N, kN")
series("Nol chizig'i", list(range(1, len(el_b) + 1)),
       [0.0]*len(el_b), xlabel="element", ylabel="N, kN")
note(f"{m_b} sterjenli ko'prik fermasi {m_b + r_b - 2*n_b} marta "
     f"statik aniqlanmaydigan - tugunlar usuli bilan qo'lda yechib "
     f"bo'lmaydi. FEM esa uni bir xil apparat bilan yechadi. "
     f"Tekshiruv: HAR BIR erkin tugunda muvozanat "
     f"{np.max(np.abs(resid[free_b])):.1e} N aniqlikda bajariladi va "
     f"reaksiyalar tashqi yukni aynan muvozanatlaydi. Bu ferma "
     f"hisobining eng ishonchli tekshiruvi va uni har doim bajarish "
     f"kerak. DIQQAT: {float(np.min(N_b))/1e3:.1f} kN siqilgan "
     f"sterjen ustuvorlikka tekshirilishi SHART (mq-25) - ferma "
     f"hisobida eng ko'p unutiladigan qadam.")

table("Ferma elementining xossalari",
      ["Xossa", "Qiymat", "Sabab"],
      [["Diskretlashtirish xatosi", "AYNAN NOL",
        "deformatsiya sterjen ichida doimiy"],
       ["Element rangi", "1", "bitta deformatsiya rejimi"],
       ["Erkinlik darajasi/tugun", "2 (tekis), 3 (fazoviy)",
        "faqat ko'chish, burilish yo'q"],
       ["Aniqlanadigan tizimda N", "yuzaga bog'liq EMAS",
        "faqat muvozanatdan"],
       ["Aniqlanmaydigan tizimda N", "bikrliklar nisbatiga bog'liq",
        "moslik sharti kerak"],
       ["Termik yuk", "faqat aniqlanmaydiganda kuch beradi",
        "to'sqinlik qilingan kengayish"]])
''',
                parameters=[
                    p("alpha_deg", "Qiya sterjen burchagi", 10.0, 60.0,
                      30.0, 5.0, "°"),
                    p("A1_cm2", "Qiya sterjen kesimi", 2.0, 40.0, 10.0,
                      1.0, "sm²"),
                    p("A2_cm2", "Vertikal sterjen kesimi", 2.0, 40.0,
                      15.0, 1.0, "sm²"),
                    p("P_kN", "Tashqi yuk", 10.0, 500.0, 100.0, 10.0,
                      "kN"),
                    p("dT_bar2", "2-sterjen harorati", -60.0, 80.0, 50.0,
                      5.0, "°C"),
                ],
                expected_output=(
                    "Uch sterjenli "
                    "aniqlanmaydigan fermada "
                    "FEM analitik yechimni "
                    "$10^{-14}$% aniqlikda "
                    "takrorlaydi: "
                    "$N_1 = 26{,}79$ kN, "
                    "$N_2 = 53{,}59$ kN. "
                    "Statik aniqlanadigan "
                    "fermada kesim yuzasini "
                    "10 barobar oshirish "
                    "sterjen kuchlarini "
                    "umuman o'zgartirmaydi, "
                    "aniqlanmaydiganda esa "
                    "$N_2$ 53,59 dan "
                    "27,79 kN ga tushadi. "
                    "Bitta sterjenni 50°C "
                    "qizdirish tashqi "
                    "yuksiz 87,7 kN kuch "
                    "hosil qiladi va bu "
                    "kuchlar o'z-o'zini "
                    "muvozanatlaydi; "
                    "aniqlanadigan fermada "
                    "esa xuddi shu "
                    "qizdirish nol kuch "
                    "beradi. Fazoviy "
                    "fermada element "
                    "formulasi o'zgarmaydi "
                    "va natija analitik "
                    "$P/(3\\cos t)$ ga mos "
                    "keladi. 31 sterjenli, "
                    "olti marta "
                    "aniqlanmaydigan ko'prik "
                    "fermasida har bir erkin "
                    "tugunda muvozanat "
                    "qoldig'i $10^{-10}$ N "
                    "darajasida."
                ),
            ),
            visual=vis(
                kind="Ferma: deformatsiya va sterjen kuchlari",
                tool="React/SVG + Manim",
                description=(
                    "Deformatsiyalangan shakl va "
                    "sterjen kuchlarining rangli "
                    "xaritasi."
                ),
                how_to_draw=(
                    "React/SVG: ferma to'g'ri "
                    "chiziqlar to'plami sifatida "
                    "chiziladi. Har bir sterjen "
                    "kuchiga qarab ranglanadi — "
                    "cho'zilish va siqilish "
                    "**qarama-qarshi ranglarda**, "
                    "chiziq qalinligi esa kuch "
                    "kattaligiga proporsional. "
                    "Nol sterjenlar punktir "
                    "bilan chiziladi va "
                    "alohida sanaladi, chunki "
                    "ular xato emas. "
                    "Deformatsiyalangan shakl "
                    "ustiga shaffof qilib "
                    "qo'yiladi va "
                    "kuchaytirish koeffitsienti "
                    "slayder bilan "
                    "boshqariladi (haqiqiy "
                    "ko'chishlar ko'zga "
                    "ko'rinmaydi). Har bir "
                    "tugunni bosganda "
                    "kichik oynacha ochiladi: "
                    "unda o'sha tugunga "
                    "tutashgan sterjen "
                    "kuchlarining vektorlari "
                    "va ularning yig'indisi "
                    "ko'rsatiladi — yig'indi "
                    "nol ekani ko'rinib "
                    "turadi. Harorat "
                    "slayderi surilganda "
                    "tashqi yuk "
                    "o'zgarmasa ham "
                    "ranglar o'zgaradi: "
                    "termik kuchlarning "
                    "'yo'qdan paydo "
                    "bo'lishi' shunda "
                    "namoyon bo'ladi. "
                    "Yonida statik aniqlik "
                    "darajasi $i$ va "
                    "'aniqlanadigan/"
                    "aniqlanmaydigan' "
                    "yozuvi turadi."
                ),
            ),
            interp=(
                "Ferma elementi FEM ni "
                "tekshirish uchun ideal etalon, "
                "chunki bu yerda "
                "diskretlashtirish xatosi "
                "**aynan nol**: sterjen ichida "
                "deformatsiya haqiqatan ham "
                "doimiy va chiziqli shakl "
                "funksiyasi buni to'liq "
                "ifodalaydi. Shuning uchun "
                "$10^{-14}$% darajasidagi "
                "kelishuv kutilgan natija va "
                "undan chetlanish kodda xato "
                "borligini bildiradi. Ikkinchi "
                "tajriba mq-27 dagi asosiy "
                "g'oyani sonli tasdiqlaydi va "
                "uni loyihalash tiliga "
                "o'tkazadi: aniqlanadigan "
                "fermada kesim yuzasini o'n "
                "barobar oshirsangiz ham "
                "sterjen kuchlari o'zgarmaydi, "
                "aniqlanmaydiganda esa "
                "bikrlashtirilgan element "
                "o'ziga ko'proq kuch tortadi. "
                "Bu amaliy oqibatga ega: "
                "'kuchlanish yuqori ekan, "
                "qalinlashtiraman' degan tabiiy "
                "qaror aniqlanmaydigan "
                "tizimda kutilgan natijani "
                "bermaydi va kesim tanlash "
                "iterativ jarayonga aylanadi. "
                "Termik tajriba esa eng "
                "muhim amaliy ogohlantirishni "
                "beradi. Bitta sterjenni 50°C "
                "qizdirish tashqi yuksiz "
                "87,7 kN kuch hosil qildi — "
                "bu 100 kN loyihaviy yukdan "
                "kelgan kuchdan ham kattaroq. "
                "Ayni paytda bu kuchlar "
                "o'z-o'zini muvozanatlaydi "
                "va tayanch reaksiyalari "
                "yig'indisi nol: tashqaridan "
                "hech narsa ko'rinmaydi, "
                "ichkarida esa kuchlanish "
                "bor. Aniqlanadigan fermada "
                "xuddi shu qizdirish nol "
                "kuch beradi, chunki u erkin "
                "kengayadi. Demak termik "
                "kuchlanish materialning "
                "kengayishidan emas, balki "
                "unga **to'sqinlik "
                "qilinishidan** tug'iladi. "
                "Nihoyat ko'prik fermasi "
                "usulning kuchini "
                "ko'rsatadi: 31 sterjen, "
                "olti marta aniqlanmaydigan, "
                "qo'lda yechib bo'lmaydi — "
                "va har bir tugunda "
                "muvozanat $10^{-10}$ N "
                "aniqlikda bajariladi."
            ),
            mistakes=[
                "Siqilgan sterjenlarni faqat "
                "mustahkamlikka tekshirish. "
                "Ustuvorlik (mq-25) ferma "
                "hisobida eng ko'p "
                "unutiladigan qadam.",
                "Nol kuchli sterjenlarni "
                "modeldan olib tashlash. Ular "
                "tizimning geometrik "
                "o'zgarmasligini "
                "ta'minlaydi.",
                "Termik ta'sirni faqat "
                "kengayish deb hisoblash. "
                "Aniqlanmaydigan tizimda u "
                "loyihaviy yukdan katta kuch "
                "berishi mumkin.",
                "Yukni sterjen o'rtasiga "
                "qo'yish. Ferma elementi "
                "faqat tugun yuklarini "
                "qabul qiladi; aks holda "
                "balka elementi kerak "
                "(su-20).",
                "Aniqlanmaydigan tizimda "
                "kesimni bir marta tanlab "
                "to'xtash. Kuchlar qayta "
                "taqsimlanadi — "
                "iteratsiya kerak.",
                "Tugun muvozanatini "
                "tekshirmaslik. Bu ferma "
                "hisobining eng oson va eng "
                "ishonchli nazorati.",
            ],
            quiz=[
                q("Ferma elementining global "
                  "bikrlik matritsasi qanday "
                  "quriladi?",
                  "$\\mathbf{k} = "
                  "\\frac{EA}{L}\\mathbf{T}^T"
                  "\\mathbf{T}$, bu yerda "
                  "$\\mathbf{T} = "
                  "[-c, -s, c, s]$ — "
                  "yo'naltiruvchi "
                  "kosinuslardan tuzilgan.",
                  "konseptual"),
                q("Fazoviy fermaga o'tishda "
                  "nima o'zgaradi?",
                  "Deyarli hech narsa: faqat "
                  "$\\mathbf{T}$ olti "
                  "komponentali bo'ladi "
                  "($\\pm c_x, \\pm c_y, "
                  "\\pm c_z$). Formula aynan "
                  "o'sha qoladi.",
                  "konseptual"),
                q("Uch sterjenli fermada "
                  "($\\alpha = 30°$, "
                  "$A_1 = 10$, $A_2 = 15$ "
                  "sm²) $N_2$ nechaga teng?",
                  "$N_2 = PA_2/"
                  "(2A_1\\cos^3\\alpha + A_2) "
                  "= 100\\cdot15/27{,}99 = "
                  "53{,}59$ kN.", "hisob"),
                q("Kod statik aniqlik "
                  "ta'sirini qanday "
                  "ko'rsatadi?",
                  "Kesim yuzasini 10 barobar "
                  "oshiradi: aniqlanadigan "
                  "fermada kuchlar aynan "
                  "o'zgarmaydi, "
                  "aniqlanmaydiganda esa "
                  "$N_2$ 53,59 dan 27,79 kN "
                  "ga tushadi.", "kod"),
                q("Termik yuk qachon kuch "
                  "hosil qiladi?",
                  "Faqat kengayishga "
                  "to'sqinlik qilinganda, "
                  "ya'ni statik "
                  "aniqlanmaydigan tizimda. "
                  "Aniqlanadigan ferma erkin "
                  "kengayadi va kodda nol "
                  "kuch beradi.", "talqin"),
                q("Nima uchun ferma "
                  "masalasida FEM yechimi "
                  "aynan to'g'ri?",
                  "Sterjen ichida "
                  "deformatsiya haqiqatan "
                  "doimiy, chiziqli shakl "
                  "funksiyasi esa buni "
                  "to'liq ifodalaydi — "
                  "diskretlashtirish xatosi "
                  "yo'q.", "talqin"),
                q("Ferma hisobidan keyin "
                  "qanday tekshiruvlar "
                  "majburiy?",
                  "Har bir tugunda "
                  "muvozanat, reaksiyalarning "
                  "tashqi yukni "
                  "muvozanatlashi va siqilgan "
                  "sterjenlarning "
                  "ustuvorlikka tekshirilishi "
                  "(mq-25).", "talqin"),
            ],
            bridge=(
                "Ferma elementi faqat o'q "
                "bo'ylab kuch uzatadi, shuning "
                "uchun yuk faqat tugunlarga "
                "qo'yilishi mumkin edi. "
                "Haqiqiy konstruksiyalarda esa "
                "tugunlar payvandlangan va "
                "yuk oraliqqa tushadi. "
                "Keyingi mavzuda balka va "
                "ramka elementlarini "
                "quramiz — u yerda burilish "
                "erkinlik darajasi va "
                "Ermit shakl funksiyalari "
                "paydo bo'ladi."
            ),
            research=(
                "Ferma tahlilini "
                "kengaytiring. "
                "(1) Topologik "
                "optimallashtirishni "
                "o'rganing: berilgan yuk "
                "uchun eng yengil ferma "
                "qanday topiladi va "
                "Mishel fermalari nima "
                "uchun nazariy optimal? "
                "(2) Geometrik nochiziqlikni "
                "ko'rib chiqing: yassi "
                "fermalarda 'o'tib ketish' "
                "(snap-through) hodisasi "
                "qanday yuzaga keladi "
                "(su-24)? "
                "(3) Oldindan taranglangan "
                "kabelli tizimlarni "
                "o'rganing: kabel faqat "
                "cho'zilishga ishlaydi va "
                "bu nochiziqlik kiritadi. "
                "(4) Ferma tugunlarining "
                "haqiqiy bikrligini "
                "baholang: payvandlangan "
                "tugunlar moment uzatadi — "
                "ikkilamchi kuchlanishlar "
                "qanchalik katta?"
            ),
            manim_ref=manim(
                scene="TrussScene",
                module="manim/scenes/su_apps.py",
                title="Ferma: kuchlar va termik ta'sir",
                summary=(
                    "Uch sterjenli ferma "
                    "ko'rsatiladi va yuk "
                    "qo'yilganda "
                    "deformatsiyalanadi; "
                    "sterjenlar kuchga qarab "
                    "ranglanadi. Keyin yuk "
                    "olib tashlanadi va "
                    "o'rtadagi sterjen "
                    "qizdiriladi — ferma "
                    "yana deformatsiyalanadi "
                    "va ranglar qaytadi, "
                    "garchi tashqi kuch "
                    "yo'q bo'lsa ham. "
                    "Yonma-yon statik "
                    "aniqlanadigan ferma "
                    "qizdiriladi va u "
                    "shunchaki kengayadi — "
                    "ranglar o'zgarmaydi."
                ),
            ),
        ),
    ),

    # ------------------------------------------------------------------ su-20
    Topic(
        id="su-20",
        subject_id=S, module_id=M, order=20,
        title="Balka va ramka elementlari",
        description=(
            "Ermit shakl funksiyalari, balka elementining bikrlik "
            "matritsasi, mahkamlangan uch kuchlari, ramka elementi va "
            "ichki kuchlarni muvozanat orqali tiklash."
        ),
        learning_objective=(
            "Balka va ramka masalalarini FEM bilan yechish, ichki "
            "kuchlarni aniq tiklash va siljish deformatsiyasining "
            "qachon muhimligini baholash."
        ),
        prerequisites=["su-19", "mq-13", "mq-16"],
        mathematical_core=(
            "$C^1$ Ermit bazisi; "
            "$\\mathbf{k} = \\frac{EI}{L^3}"
            "[\\,12,\\,6L;\\ 6L,\\,4L^2\\,]$; "
            "uch kuchlari $\\mathbf{S} = \\mathbf{k}\\mathbf{u}_e - "
            "\\mathbf{f}_e$."
        ),
        engineering_application=(
            "Ko'p qavatli binolar karkasi, ko'prik ustqurmasi, kran "
            "va estakada ramkalar, quvur tizimlari."
        ),
        computational_component=(
            "Balka va ramka yechuvchisi, ichki kuch epyuralari, "
            "siljish deformatsiyasining ta'siri."
        ),
        visualization_component=(
            "Ermit shakl funksiyalari, deformatsiyalangan ramka, "
            "moment va ko'ndalang kuch epyuralari."
        ),
        research_extension=(
            "Plastik sharnirlar usulini o'rganing: ramkaning chegaraviy "
            "yuk ko'taruvchanligi va progressiv yemirilish tahlili."
        ),
        difficulty="orta",
        previous_link=(
            "su-19 dagi ferma elementi faqat o'q bo'ylab kuch uzatardi va "
            "yuk faqat tugunlarga qo'yilardi. Endi burilish erkinlik "
            "darajasini qo'shamiz — shu bilan oraliqqa tushadigan yukni "
            "va payvandlangan tugunlarni modellashtira olamiz."
        ),
        next_topic="su-21",
        estimated_minutes=90,
        tags=["Ermit funksiyalari", "balka elementi", "ramka",
              "mahkamlangan uch kuchlari", "Timoshenko"],
        lesson=_lesson(
            problem=(
                "Ko'p qavatli binoning po'lat "
                "karkasi shamol yukiga "
                "hisoblanmoqda. Ferma modeli "
                "yaramaydi: tugunlar "
                "payvandlangan va moment "
                "uzatadi, yuk esa rigellarning "
                "**oraliqiga** tushadi. "
                "Bundan tashqari hisobot "
                "uchun har bir elementning "
                "moment epyurasi kerak — "
                "ya'ni faqat ko'chish emas, "
                "ichki kuchlar ham. Lekin "
                "moment ko'chishning "
                "**ikkinchi hosilasi**, ya'ni "
                "eng kam aniq kattalik "
                "(su-17). Uni ishonchli "
                "qilib qanday olish mumkin? "
                "Va yana bir savol: qisqa, "
                "yo'g'on rigellarda siljish "
                "deformatsiyasi hisobga "
                "olinishi kerakmi?"
            ),
            concepts=[
                c("$C^1$ uzluksizlik",
                  "Balka tenglamasi to'rtinchi "
                  "tartibli, shuning uchun zaif "
                  "shaklda ikkinchi hosila "
                  "qatnashadi va bazis "
                  "**hosilasi bilan birga** "
                  "uzluksiz bo'lishi kerak."),
                c("Ermit shakl funksiyalari",
                  "Har bir tugunda ikkita "
                  "erkinlik darajasi — ko'chish "
                  "$w$ va burilish "
                  "$\\theta = w'$; to'rtta "
                  "kubik funksiya."),
                c("Mahkamlangan uch kuchlari "
                  "(fixed-end forces)",
                  "Oraliq yukning ekvivalent "
                  "tugun yuklari: "
                  "$qL/2$ va $qL^2/12$ — bu "
                  "su-15 dagi moslashgan yuk "
                  "vektorining balka "
                  "ko'rinishi."),
                c("Ramka elementi",
                  "O'q (ferma) va egilish "
                  "(balka) birlashtiriladi: "
                  "tugunda uchta erkinlik "
                  "darajasi."),
                c("Ichki kuchlarni tiklash",
                  "$\\mathbf{S} = \\mathbf{k}"
                  "\\mathbf{u}_e - \\mathbf{f}_e$ "
                  "— muvozanatga asoslangan va "
                  "**aynan** to'g'ri."),
                c("Timoshenko balkasi",
                  "Siljish deformatsiyasini "
                  "hisobga oladi; qisqa "
                  "balkalarda muhim "
                  "(pq-24 bilan bir xil "
                  "g'oya)."),
            ],
            derivation=[
                d("1. Nima uchun $C^1$ kerak",
                  r"\Pi = \int_0^L \frac{EI}{2}"
                  r"(w'')^2dx - \int_0^L qw\,dx",
                  "Energiyada **ikkinchi** "
                  "hosila bor, shuning uchun "
                  "$w'$ uzluksiz bo'lishi "
                  "shart — aks holda "
                  "$w''$ da delta-funksiya "
                  "paydo bo'lib, energiya "
                  "cheksizlashadi."),
                d("2. Erkinlik darajalarini "
                  "tanlash",
                  r"\mathbf{u}_e = \{w_1,\ "
                  r"\theta_1,\ w_2,\ "
                  r"\theta_2\}^T",
                  "**Hal qiluvchi qadam.** "
                  "Burilishni ham tugun "
                  "noma'lumi qilsak, "
                  "qo'shni elementlarda u "
                  "avtomatik mos tushadi — "
                  "$C^1$ ta'minlanadi."),
                d("3. Ermit shakl funksiyalari",
                  r"N_1 = 1 - 3\xi^2 + 2\xi^3, "
                  r"\quad N_2 = L(\xi - 2\xi^2 "
                  r"+ \xi^3)",
                  "$\\xi = x/L$. "
                  "$N_3 = 3\\xi^2 - 2\\xi^3$, "
                  "$N_4 = L(-\\xi^2 + "
                  "\\xi^3)$. To'rtta shart: "
                  "har bir funksiya o'z "
                  "erkinlik darajasida 1, "
                  "qolganlarida 0."),
                d("4. Egrilik matritsasi",
                  r"\mathbf{B} = "
                  r"\frac{d^2\mathbf{N}}{dx^2} "
                  r"= \frac{1}{L^2}"
                  r"\frac{d^2\mathbf{N}}{d\xi^2}",
                  "Ferma elementidagi "
                  "birinchi hosila o'rniga "
                  "ikkinchi hosila. "
                  "$\\mathbf{B}$ — $\\xi$ ga "
                  "chiziqli, demak egrilik "
                  "element ichida chiziqli "
                  "o'zgaradi."),
                d("5. Bikrlik matritsasi",
                  r"\mathbf{k} = \frac{EI}{L^3}"
                  r"\begin{bmatrix} 12 & 6L & "
                  r"-12 & 6L\\ 6L & 4L^2 & -6L "
                  r"& 2L^2\\ -12 & -6L & 12 & "
                  r"-6L\\ 6L & 2L^2 & -6L & "
                  r"4L^2\end{bmatrix}",
                  "Klassik balka element "
                  "matritsasi. Rangi 2 — "
                  "ikkita qattiq jism rejimi "
                  "(ko'chish va burilish)."),
                d("6. Mahkamlangan uch kuchlari",
                  r"\mathbf{f}_e = \left\{"
                  r"\frac{qL}{2},\ "
                  r"\frac{qL^2}{12},\ "
                  r"\frac{qL}{2},\ "
                  r"-\frac{qL^2}{12}"
                  r"\right\}^T",
                  "**Diqqat.** Bu su-15 dagi "
                  "$\\int\\mathbf{N}^Tq$ ning "
                  "aynan o'zi va u "
                  "$\\{qL/2,\\ 0\\}$ dan "
                  "**farq qiladi** — moment "
                  "hadlari bor."),
                d("7. Nodal aniqlik",
                  r"w_h(x_i) = w_{exact}(x_i) \ "
                  r"\text{(aynan)}",
                  "**Ajoyib xossa.** "
                  "Moslashgan yuk vektori "
                  "bilan tugun ko'chishlari "
                  "va burilishlari "
                  "**aynan** to'g'ri — "
                  "hatto bitta elementda "
                  "ham. Kod buni to'rtta "
                  "klassik masalada "
                  "tasdiqlaydi."),
                d("8. Ichki kuchlarni "
                  "tiklashning noto'g'ri "
                  "yo'li",
                  r"M = EI\,w_h'' \quad "
                  r"(\text{xato } 2-6\%)",
                  "Tabiiy ko'rinadi, lekin "
                  "$w_h''$ bo'lakli "
                  "chiziqli, aniq moment "
                  "esa parabolik — tugunda "
                  "ham xato qoladi."),
                d("9. To'g'ri yo'l: muvozanat",
                  r"\mathbf{S}_e = \mathbf{k}_e"
                  r"\mathbf{u}_e - \mathbf{f}_e",
                  "**Asosiy amaliy natija.** "
                  "Element uchi kuchlari "
                  "muvozanatdan kelib "
                  "chiqadi va tugunlarda "
                  "**aynan** to'g'ri. "
                  "Barcha FEM paketlari "
                  "shunday hisoblaydi."),
                d("10. Ramka elementi",
                  r"\mathbf{u}_e = \{u_1, w_1, "
                  r"\theta_1, u_2, w_2, "
                  r"\theta_2\}^T",
                  "O'q va egilish "
                  "**bog'lanmagan** (chiziqli "
                  "nazariyada), shuning "
                  "uchun ikkita matritsa "
                  "shunchaki birlashtiriladi."),
                d("11. Ramka elementining "
                  "almashtirilishi",
                  r"\mathbf{k}_{gl} = "
                  r"\mathbf{T}^T\mathbf{k}_{loc}"
                  r"\mathbf{T}, \quad "
                  r"\mathbf{R} = \begin{bmatrix} "
                  r"c & s & 0\\ -s & c & 0\\ "
                  r"0 & 0 & 1\end{bmatrix}",
                  "Burilish **skalyar** — u "
                  "burilishda o'zgarmaydi, "
                  "shuning uchun $\\mathbf{R}$ "
                  "ning uchinchi qatori "
                  "birlik."),
                d("12. Siljish deformatsiyasi",
                  r"\phi = \frac{12EI}"
                  r"{\kappa GAL^2}, \qquad "
                  r"\mathbf{k} \propto "
                  r"\frac{EI}{L^3(1+\phi)}",
                  "Timoshenko balkasi. "
                  "$\\phi \\sim (h/L)^2$, "
                  "demak ingichka balkada "
                  "u yo'qoladi."),
                d("13. Qachon muhim",
                  r"\frac{\Delta w}{w} \approx "
                  r"\phi \sim \left(\frac{h}{L}"
                  r"\right)^2",
                  "**O'lchangan natija.** "
                  "$L/h = 10$ da farq 0,8%, "
                  "$L/h = 2$ da esa 16%. "
                  "Ingichka balkada "
                  "Eyler–Bernulli yetarli."),
            ],
            meaning=(
                "Balka elementining butun "
                "nozikligi 1- va 2-qadamlarda. "
                "Egilish energiyasida ikkinchi "
                "hosila borligi bazisdan "
                "$C^1$ uzluksizlikni talab "
                "qiladi va bu oddiy Lagranj "
                "funksiyalari bilan "
                "erishilmaydi. Yechim "
                "chiroyli: burilishni ham "
                "tugun noma'lumi qilsak, "
                "qo'shni elementlarda u "
                "o'z-o'zidan mos tushadi. "
                "Shuning uchun balka "
                "elementida tugunga ikkita "
                "erkinlik darajasi to'g'ri "
                "keladi va bazis Ermit "
                "kubiklaridan iborat. Bu "
                "yondashuvning cheklovi ham "
                "shu yerdan kelib chiqadi: "
                "plastinalarda $C^1$ ni "
                "ta'minlash ancha qiyin "
                "(pq-24) va aynan shu sababdan "
                "plastina elementlari "
                "tarixan muammoli bo'lgan. "
                "7-qadamdagi nodal aniqlik "
                "ferma elementidagiga "
                "o'xshaydi, lekin sababi "
                "boshqacha. Ferma elementida "
                "aniq yechimning o'zi "
                "chiziqli edi; bu yerda esa "
                "taqsimlangan yuk ostida "
                "aniq yechim to'rtinchi "
                "darajali, kubik bazis uni "
                "ifodalay olmaydi — va "
                "shunga qaramay **tugun "
                "qiymatlari aynan to'g'ri** "
                "chiqadi. Bu su-13 dagi bir "
                "o'lchovli "
                "superkonvergensiyaning "
                "balka varianti va u faqat "
                "moslashgan yuk vektori "
                "bilan ishlaydi. Jamlangan "
                "vektorga o'tsangiz, bitta "
                "elementda xato darhol 33% "
                "ga chiqadi. Eng muhim "
                "amaliy dars esa 8- va "
                "9-qadamlarda. Momentni "
                "$EI\\,w_h''$ orqali olish "
                "tabiiy ko'rinadi, lekin "
                "natija tugunlarda ham "
                "xato beradi, chunki "
                "kubik bazisning ikkinchi "
                "hosilasi bo'lakli chiziqli, "
                "aniq moment esa parabolik. "
                "To'g'ri yo'l — muvozanatdan "
                "foydalanish: "
                "$\\mathbf{k}\\mathbf{u}_e - "
                "\\mathbf{f}_e$ element "
                "uchidagi haqiqiy kuchlarni "
                "beradi va ular **aynan** "
                "to'g'ri. Bu su-17 dagi "
                "kuchlanishni tiklash "
                "g'oyasining davomi: "
                "hosilani bevosita olish "
                "eng yomon variant, "
                "muvozanat yoki "
                "superkonvergent "
                "nuqtalardan tiklash esa "
                "eng yaxshisi."
            ),
            equations=[
                eq(r"N_1 = 1 - 3\xi^2 + 2\xi^3, "
                   r"\ N_2 = L(\xi - 2\xi^2 + "
                   r"\xi^3), \ \xi = x/L",
                   "Ermit shakl funksiyalari "
                   "(birinchi tugun).",
                   "Ermit bazisi"),
                eq(r"\mathbf{k} = \frac{EI}{L^3}"
                   r"\begin{bmatrix} 12 & 6L & "
                   r"-12 & 6L\\ 6L & 4L^2 & "
                   r"-6L & 2L^2\\ -12 & -6L & "
                   r"12 & -6L\\ 6L & 2L^2 & "
                   r"-6L & 4L^2\end{bmatrix}",
                   "Balka elementining bikrlik "
                   "matritsasi.",
                   "Element matritsasi"),
                eq(r"\mathbf{f}_e = \left\{"
                   r"\tfrac{qL}{2},\ "
                   r"\tfrac{qL^2}{12},\ "
                   r"\tfrac{qL}{2},\ "
                   r"-\tfrac{qL^2}{12}"
                   r"\right\}^T",
                   "Tekis taqsimlangan yukning "
                   "mahkamlangan uch kuchlari.",
                   "Ekvivalent yuk"),
                eq(r"\mathbf{S}_e = \mathbf{k}_e"
                   r"\mathbf{u}_e - \mathbf{f}_e "
                   r"\quad (\text{aynan}), "
                   r"\qquad M = EI w_h'' \quad "
                   r"(\text{taqribiy})",
                   "Ichki kuchlarni tiklashning "
                   "to'g'ri va noto'g'ri yo'li.",
                   "Kuchlarni tiklash"),
            ],
            conditions=(
                "**Balka modelining "
                "taxminlari:**\n"
                "1. Tekis kesimlar tekis "
                "qoladi va o'qqa "
                "perpendikulyar "
                "(Eyler–Bernulli);\n"
                "2. Siljish deformatsiyasi "
                "e'tiborsiz — "
                "$L/h > 10$ bo'lsa "
                "o'rinli;\n"
                "3. Ko'chishlar kichik, "
                "o'q kuchi egilishga ta'sir "
                "qilmaydi (su-23 da bekor "
                "qilinadi).\n\n"
                "**Element sonini tanlash:**\n"
                "- Tugun ko'chishlari uchun "
                "**bitta** element yetarli "
                "(nodal aniqlik);\n"
                "- Silliq epyura uchun "
                "3–5 element;\n"
                "- Yuk yoki kesim "
                "o'zgarishida albatta "
                "tugun bo'lsin;\n"
                "- Dinamikada (su-23) "
                "yuqori shakllar uchun "
                "ko'proq kerak.\n\n"
                "**Ichki kuchlarni olishda:** "
                "har doim "
                "$\\mathbf{k}\\mathbf{u}_e - "
                "\\mathbf{f}_e$ dan "
                "foydalaning; "
                "$EI\\,w''$ dan emas.\n\n"
                "**Siljish deformatsiyasi "
                "kerak bo'ladigan "
                "hollar:** qisqa va yo'g'on "
                "rigellar ($L/h < 10$), "
                "qatlamli kompozitlar "
                "(qatlamlararo siljish "
                "moduli kichik), "
                "devor-balkalar. "
                "Timoshenko elementida "
                "esa su-16 dagi siljish "
                "qulflanishi paydo "
                "bo'ladi — SRI kerak.\n\n"
                "**Ogohlantirish:** ramka "
                "elementi tugunni "
                "**nuqta** deb qaraydi. "
                "Haqiqiy tugun zonasi "
                "o'lchamga ega va bikr — "
                "buni qattiq uchlar "
                "(rigid end offsets) "
                "bilan modellashtirish "
                "mumkin."
            ),
            worked=WorkedExample(
                statement=(
                    "Uzunligi $L$ bo'lgan "
                    "konsol balka tekis "
                    "taqsimlangan $q$ yuk "
                    "ostida. **Bitta** balka "
                    "elementi bilan uch "
                    "ko'chishini toping va "
                    "analitik yechim bilan "
                    "solishtiring. Keyin "
                    "mahkamlangan uch "
                    "momentini hisoblang."
                ),
                given=[
                    r"EI = \text{const}, \quad "
                    r"q = \text{const}, \quad "
                    r"\text{bitta element}",
                    r"\text{Chap uch mahkam: } "
                    r"w_1 = \theta_1 = 0",
                ],
                steps=[
                    st(r"\mathbf{f}_e = \left\{"
                       r"\tfrac{qL}{2},\ "
                       r"\tfrac{qL^2}{12},\ "
                       r"\tfrac{qL}{2},\ "
                       r"-\tfrac{qL^2}{12}"
                       r"\right\}^T",
                       "Moslashgan yuk vektori. "
                       "Faqat 3- va "
                       "4-komponentalar "
                       "qoladi."),
                    st(r"\frac{EI}{L^3}"
                       r"\begin{bmatrix} 12 & "
                       r"-6L\\ -6L & 4L^2"
                       r"\end{bmatrix}"
                       r"\begin{Bmatrix} w_2\\ "
                       r"\theta_2\end{Bmatrix} = "
                       r"\begin{Bmatrix} "
                       r"\tfrac{qL}{2}\\ "
                       r"-\tfrac{qL^2}{12}"
                       r"\end{Bmatrix}",
                       "1- va 2-qatorlar "
                       "o'chirildi (yo'q qilish "
                       "usuli, su-17)."),
                    st(r"\det = \frac{EI}{L^3}"
                       r"\cdot\frac{EI}{L^3}"
                       r"\left(48L^2 - 36L^2"
                       r"\right) = "
                       r"\frac{12E^2I^2}{L^4}",
                       "Determinant."),
                    st(r"w_2 = \frac{L^3}{12EI}"
                       r"\left[4L^2\cdot"
                       r"\frac{qL}{2} + 6L\cdot"
                       r"\left(-\frac{qL^2}{12}"
                       r"\right)\right]\frac{1}"
                       r"{L^2}",
                       "Kramer qoidasi bilan."),
                    st(r"= \frac{L}{12EI}\left["
                       r"2qL^3 - \frac{qL^3}{2}"
                       r"\right] = "
                       r"\frac{L}{12EI}\cdot"
                       r"\frac{3qL^3}{2}",
                       "Qavs ichini "
                       "soddalashtiramiz."),
                    st(r"w_2 = \frac{qL^4}{8EI} "
                       r"\quad \checkmark",
                       "**Analitik yechim bilan "
                       "AYNAN bir xil** — "
                       "bitta element bilan!"),
                    st(r"\theta_2 = "
                       r"\frac{qL^3}{6EI} \quad "
                       r"\checkmark",
                       "Burilish ham aynan "
                       "to'g'ri."),
                    st(r"\mathbf{S}_e = "
                       r"\mathbf{k}_e\mathbf{u}_e "
                       r"- \mathbf{f}_e",
                       "Endi mahkamlangan uch "
                       "kuchlari."),
                    st(r"S_2 = \frac{EI}{L^3}"
                       r"\left(-6L\,w_2 + "
                       r"2L^2\theta_2\right) - "
                       r"\frac{qL^2}{12}",
                       "Ikkinchi komponenta — "
                       "chap uchdagi moment."),
                    st(r"= \frac{EI}{L^3}\left("
                       r"-\frac{6qL^5}{8EI} + "
                       r"\frac{2qL^5}{6EI}"
                       r"\right) - "
                       r"\frac{qL^2}{12}",
                       "Qiymatlarni "
                       "qo'yamiz."),
                    st(r"= qL^2\left(-\frac{3}{4} "
                       r"+ \frac13 - \frac{1}{12}"
                       r"\right) = qL^2\left("
                       r"\frac{-9 + 4 - 1}{12}"
                       r"\right)",
                       "Umumiy maxrajga "
                       "keltiramiz."),
                    st(r"S_2 = -\frac{qL^2}{2} "
                       r"\quad \checkmark",
                       "**Konsolning "
                       "mahkamlash momenti** — "
                       "analitik "
                       "$qL^2/2$ bilan "
                       "aynan mos."),
                ],
                answer=(
                    "$w_2 = qL^4/(8EI)$, "
                    "$\\theta_2 = qL^3/(6EI)$ — "
                    "ikkalasi ham "
                    "**bitta element** bilan "
                    "aynan to'g'ri. "
                    "Mahkamlash momenti "
                    "$|M| = qL^2/2$, u ham "
                    "aniq. Kod bu natijalarni "
                    "$10^{-14}$% aniqlikda "
                    "takrorlaydi."
                ),
                engineering_note=(
                    "Bitta element bilan "
                    "aniq javob olish "
                    "ta'sirli, lekin uni "
                    "noto'g'ri tushunmaslik "
                    "kerak. Aynan to'g'ri "
                    "bo'lgani — faqat "
                    "**tugun** qiymatlari. "
                    "Element ichida "
                    "ko'chish kubik "
                    "yaqinlashish bo'lib "
                    "qoladi, holbuki aniq "
                    "yechim to'rtinchi "
                    "darajali; moment "
                    "epyurasi esa chiziqli "
                    "chiqadi, aniqda "
                    "parabolik. Shuning "
                    "uchun epyura chizish "
                    "uchun bitta element "
                    "yetarli emas — "
                    "3–5 ta kerak. "
                    "Ikkinchi muhim nuqta: "
                    "$qL^2/12$ hadini "
                    "tushirib qoldirish "
                    "(ya'ni yukni "
                    "shunchaki ikkiga "
                    "bo'lib tugunlarga "
                    "qo'yish) bitta "
                    "elementda 33% xato "
                    "beradi. Bu xato "
                    "jimgina o'tadi, "
                    "chunki muvozanat "
                    "buzilmaydi — faqat "
                    "taqsimot noto'g'ri "
                    "(su-15). Uchinchisi: "
                    "ichki kuchlarni har "
                    "doim "
                    "$\\mathbf{k}\\mathbf{u} "
                    "- \\mathbf{f}$ dan "
                    "oling. Ko'pchilik "
                    "talaba $EI\\,w''$ ni "
                    "hisoblaydi va 2–6% "
                    "xato oladi — "
                    "hisobot uchun bu "
                    "keraksiz yo'qotish, "
                    "chunki to'g'ri usul "
                    "ham xuddi shunchalik "
                    "sodda."
                ),
            ),
            computation=Computation(
                caption=(
                    "Ermit balka elementini "
                    "klassik yechimlar bilan "
                    "tekshirish, ichki "
                    "kuchlarni ikki usulda "
                    "tiklash, ramka va siljish "
                    "deformatsiyasi."
                ),
                code='''"""Balka va ramka elementlari."""
import numpy as np
from labkit import PARAMS, note, series, table, value

n_el = int(PARAMS.get("n_el", 4))
L_b = float(PARAMS.get("L_b", 3.0))
q_kNm = float(PARAMS.get("q_kNm", 5.0))
h_col = float(PARAMS.get("h_col", 4.0))
b_beam = float(PARAMS.get("b_beam", 6.0))

E = 2.1e11
I_sec = 8e-6
A_sec = 6e-3
EI = E*I_sec
G = E/2.6
q = q_kNm*1e3


def ke_beam(EI_, Le):
    return EI_/Le**3*np.array([
        [12, 6*Le, -12, 6*Le],
        [6*Le, 4*Le*Le, -6*Le, 2*Le*Le],
        [-12, -6*Le, 12, -6*Le],
        [6*Le, 2*Le*Le, -6*Le, 4*Le*Le]], dtype=float)


def fe_udl(qq, Le):
    """Mahkamlangan uch kuchlari - su-15 dagi moslashgan yuk vektori."""
    return np.array([qq*Le/2, qq*Le*Le/12, qq*Le/2, -qq*Le*Le/12])


def beam(n, Lb, qq=0.0, P=None, bc="cantilever", lumped=False):
    h = Lb/n
    nd = 2*(n + 1)
    K = np.zeros((nd, nd))
    F = np.zeros(nd)
    for e in range(n):
        idx = [2*e, 2*e + 1, 2*e + 2, 2*e + 3]
        K[np.ix_(idx, idx)] += ke_beam(EI, h)
        F[idx] += (np.array([qq*h/2, 0.0, qq*h/2, 0.0]) if lumped
                   else fe_udl(qq, h))
    if P:
        for dof, v in P.items():
            F[dof] += v
    fixed = {"cantilever": [0, 1], "simply": [0, 2*n],
             "fixed-fixed": [0, 1, 2*n, 2*n + 1]}[bc]
    free = np.setdiff1d(np.arange(nd), fixed)
    u = np.zeros(nd)
    u[free] = np.linalg.solve(K[np.ix_(free, free)], F[free])
    return u, K, F, h


# --- (1) NODAL ANIQLIK: to'rtta klassik masala ---
P_pt = 10e3
rows = []
for n in [1, 2, 4, 8]:
    u1, _, _, _ = beam(n, L_b, P={2*n: -P_pt}, bc="cantilever")
    e1 = -P_pt*L_b**3/(3*EI)
    u2, _, _, _ = beam(n, L_b, qq=-q, bc="cantilever")
    e2 = -q*L_b**4/(8*EI)
    rows.append([n, f"{abs(u1[2*n] - e1)/abs(e1)*100:.3e}",
                 f"{abs(u2[2*n] - e2)/abs(e2)*100:.3e}"])
table("Konsol balka: bitta element ham aniq javob beradimi?",
      ["elementlar", "uchida P: xato %", "tarqalgan q: xato %"], rows)
value("Konsol + P: aniq w(L)", -P_pt*L_b**3/(3*EI), "m")
value("Konsol + q: aniq w(L)", -q*L_b**4/(8*EI), "m")

rows2 = []
for n in [2, 4, 8]:
    u3, _, _, _ = beam(n, L_b, qq=-q, bc="simply")
    e3 = -5*q*L_b**4/(384*EI)
    u4, K4, F4, _ = beam(n, L_b, qq=-q, bc="fixed-fixed")
    R4 = K4 @ u4 - F4
    e4 = q*L_b**2/12
    rows2.append([n, f"{abs(u3[n] - e3)/abs(e3)*100:.3e}",
                  f"{abs(abs(R4[1]) - e4)/e4*100:.3e}"])
table("Sharnirli va ikki uchi mahkam balka",
      ["elementlar", "sharnirli w_mid: xato %",
       "mahkam tayanch momenti: xato %"], rows2)
value("Sharnirli aniq w_mid (5qL^4/384EI)",
      -5*q*L_b**4/(384*EI), "m")
value("Mahkam tayanch momenti (qL^2/12)", q*L_b**2/12, "N*m")
note("Ermit balka elementi TO'RTTA klassik masalada ham tugun "
     "qiymatlarini mashina aniqligida beradi - hatto BITTA element "
     "bilan. Bu ferma elementidagidan boshqacha hodisa: u yerda aniq "
     "yechimning o'zi chiziqli edi, bu yerda esa tarqalgan yuk ostida "
     "aniq yechim TO'RTINCHI darajali va kubik bazis uni ifodalay "
     "olmaydi. Shunga qaramay tugun qiymatlari aynan to'g'ri - bu "
     "su-13 dagi bir o'lchovli superkonvergensiyaning balka "
     "ko'rinishi.")

# --- (2) MOSLASHGAN va JAMLANGAN yuk vektori ---
rows3 = []
ex_c = -q*L_b**4/(8*EI)
for n in [1, 2, 4, 8, 16]:
    uc, _, _, _ = beam(n, L_b, qq=-q, bc="cantilever", lumped=False)
    ul, _, _, _ = beam(n, L_b, qq=-q, bc="cantilever", lumped=True)
    rows3.append([n, f"{abs(uc[2*n] - ex_c)/abs(ex_c)*100:.3e}",
                  f"{abs(ul[2*n] - ex_c)/abs(ex_c)*100:.4f}"])
table("Moslashgan (qL^2/12 bilan) va jamlangan yuk vektori",
      ["elementlar", "moslashgan xato, %", "jamlangan xato, %"], rows3)
note("Mahkamlangan uch momentlarini (qL^2/12) tushirib qoldirish "
     "bitta elementda 33.33% xato beradi va u to'r zichlashganda "
     "aynan TO'RT barobar kamayadi - ikkinchi tartib. Muvozanat esa "
     "ikkala holatda ham buzilmaydi, shuning uchun bu xato jimgina "
     "o'tadi (su-15). Balkada u fermadagidan ancha jiddiyroq: u yerda "
     "6.25% edi, bu yerda 33%.")

# --- (3) ICHKI KUCHLARNI TIKLASH: ikki usul ---
n_m = n_el
u_m, K_m, F_m, h_m = beam(n_m, L_b, qq=-q, bc="simply")


def M_exact(x):
    return q*x*(L_b - x)/2


def M_curv(e, xi):
    """EI*w'' - 'sodda' yo'l."""
    idx = [2*e, 2*e + 1, 2*e + 2, 2*e + 3]
    d2 = np.array([6*xi/h_m**2, (3*xi - 1)/h_m,
                   -6*xi/h_m**2, (3*xi + 1)/h_m])
    return EI*float(d2 @ u_m[idx])


rows4 = []
for e in range(n_m):
    idx = [2*e, 2*e + 1, 2*e + 2, 2*e + 3]
    S = ke_beam(EI, h_m) @ u_m[idx] - fe_udl(-q, h_m)
    for x, M_eq, xi in [(e*h_m, -S[1], -1.0), ((e + 1)*h_m, S[3], 1.0)]:
        Me = M_exact(x)
        if abs(Me) < 1.0:
            continue
        Mc = M_curv(e, xi)
        rows4.append([f"{x/L_b:.3f}", f"{Me:.2f}", f"{M_eq:.2f}",
                      f"{abs(M_eq - Me)/abs(Me)*100:.2e}", f"{Mc:.2f}",
                      f"{abs(Mc - Me)/abs(Me)*100:.3f}"])
table(f"Tugunlardagi moment ({n_m} element, sharnirli balka)",
      ["x/L", "aniq M", "muvozanatdan k*u-f", "xato %",
       "EI*w'' dan", "xato %"], rows4)

xs_eq, Ms_eq, xs_cv, Ms_cv, Ms_ex = [], [], [], [], []
for e in range(n_m):
    idx = [2*e, 2*e + 1, 2*e + 2, 2*e + 3]
    S = ke_beam(EI, h_m) @ u_m[idx] - fe_udl(-q, h_m)
    xs_eq += [e*h_m, (e + 1)*h_m]
    Ms_eq += [float(-S[1]), float(S[3])]
    for xi in np.linspace(-1, 1, 9):
        x = e*h_m + h_m*(1 + xi)/2
        xs_cv.append(x)
        Ms_cv.append(M_curv(e, xi))
        Ms_ex.append(M_exact(x))
series("Aniq moment", xs_cv, Ms_ex, xlabel="x, m", ylabel="M, N*m")
series("Muvozanatdan (k*u - f)", xs_eq, Ms_eq,
       xlabel="x, m", ylabel="M, N*m")
series("EI*w'' dan", xs_cv, Ms_cv, xlabel="x, m", ylabel="M, N*m")

# Element ichida xato minimal bo'lgan nuqta - yana Barlou
xis = np.linspace(-1, 1, 401)
errs = [abs(M_curv(0, xi) - M_exact(h_m*(1 + xi)/2)) for xi in xis]
i_min = int(np.argmin(errs))
value("EI*w'' xatosi minimal bo'lgan |xi|", abs(float(xis[i_min])), "—")
value("Gauss nuqtasi 1/sqrt(3)", float(1/np.sqrt(3)), "—")
note("HAL QILUVCHI FARQ. Muvozanatdan tiklangan uch momentlari "
     "tugunlarda MASHINA ANIQLIGIDA to'g'ri, EI*w'' esa 2-6% xato "
     "beradi - va bu xato tugunlarda ham yo'qolmaydi, chunki kubik "
     "bazisning ikkinchi hosilasi bo'lakli chiziqli, aniq moment esa "
     "parabolik. Element ICHIDA esa EI*w'' xatosi |xi| = 1/sqrt(3) "
     "atrofida minimal bo'ladi: bu yana su-16 dagi Barlou nuqtasi. "
     "Xulosa: ichki kuchlarni har doim k*u - f dan oling.")

# --- (4) RAMKA elementi: burilish invariantligi ---
def ke_frame(EA_, EI_, Le):
    k = np.zeros((6, 6))
    k[0, 0] = k[3, 3] = EA_/Le
    k[0, 3] = k[3, 0] = -EA_/Le
    ix = [1, 2, 4, 5]
    k[np.ix_(ix, ix)] += ke_beam(EI_, Le)
    return k


def frame(nodes, elems, EA_, EI_, fixed, loads):
    nodes = np.asarray(nodes, dtype=float)
    nn = len(nodes)
    nd = 3*nn
    K = np.zeros((nd, nd))
    F = np.zeros(nd)
    Ts, Ls = [], []
    for (i, j) in elems:
        dx, dy = nodes[j] - nodes[i]
        Le = float(np.hypot(dx, dy))
        cc, ss = dx/Le, dy/Le
        R = np.array([[cc, ss, 0.0], [-ss, cc, 0.0], [0.0, 0.0, 1.0]])
        T = np.zeros((6, 6))
        T[:3, :3] = R
        T[3:, 3:] = R
        Ts.append(T)
        Ls.append(Le)
        idx = [3*i, 3*i + 1, 3*i + 2, 3*j, 3*j + 1, 3*j + 2]
        K[np.ix_(idx, idx)] += T.T @ ke_frame(EA_, EI_, Le) @ T
    for dof, v in loads.items():
        F[dof] += v
    free = np.setdiff1d(np.arange(nd), fixed)
    u = np.zeros(nd)
    u[free] = np.linalg.solve(K[np.ix_(free, free)], F[free])
    return u, K, F, Ts, Ls


rows5 = []
ex_rot = P_pt*L_b**3/(3*EI)
for ang in [0.0, 30.0, 45.0, 90.0, 180.0, 247.0]:
    aa = np.radians(ang)
    ndr = np.array([[0.0, 0.0], [L_b*np.cos(aa), L_b*np.sin(aa)]])
    Fx, Fy = -P_pt*np.sin(aa), P_pt*np.cos(aa)   # o'qqa perpendikulyar
    ur, _, _, _, _ = frame(ndr, [(0, 1)], E*A_sec, EI, [0, 1, 2],
                           {3: Fx, 4: Fy})
    w_perp = -ur[3]*np.sin(aa) + ur[4]*np.cos(aa)
    rows5.append([f"{ang:.0f}", f"{w_perp:.10e}",
                  f"{abs(w_perp - ex_rot)/ex_rot*100:.3e}"])
table("Ramka elementining burilishga nisbatan invariantligi",
      ["burchak, °", "ko'ndalang ko'chish, m", "aniq yechimdan xato %"],
      rows5)
note("Bir xil konsol turli burchaklarda joylashtirildi va har safar "
     "o'qqa perpendikulyar kuch qo'yildi. Ko'ndalang ko'chish barcha "
     "burchaklarda bir xil chiqdi - almashtirish matritsasi to'g'ri "
     "qurilgan. Bu ramka kodini tekshirishning eng oson va eng "
     "ishonchli usuli: natija koordinata tizimini tanlashga bog'liq "
     "bo'lmasligi SHART.")

# --- (5) PORTAL RAMKA: klassik burchak-ko'chish yechimi bilan ---
H_load = 20e3
rows6 = []
for hc, bb in [(h_col, b_beam), (3.0, 6.0), (4.0, 4.0), (5.0, 8.0)]:
    ndp = np.array([[0.0, 0.0], [0.0, hc], [bb, hc], [bb, 0.0]])
    elp = [(0, 1), (1, 2), (2, 3)]
    # o'qi cho'zilmaydigan deb olamiz - klassik formulaning sharti
    up, Kp, Fp, _, _ = frame(ndp, elp, E*A_sec*1e6, EI,
                             [0, 1, 2, 9, 10, 11], {3: H_load})
    kk = (I_sec/bb)/(I_sec/hc)
    d_ex = H_load*hc**3*(2 + 3*kk)/(12*EI*(1 + 6*kk))
    rows6.append([f"{hc:.0f}", f"{bb:.0f}", f"{kk:.4f}",
                  f"{up[3]*1e3:.6f}", f"{d_ex*1e3:.6f}",
                  f"{abs(up[3] - d_ex)/d_ex*100:.2e}"])
table("Portal ramka: yon siljish (o'qi cho'zilmaydigan holat)",
      ["h", "b", "k = (I_b/b)/(I_c/h)", "FEM, mm", "formula, mm",
       "xato %"], rows6)

ndp = np.array([[0.0, 0.0], [0.0, h_col], [b_beam, h_col],
                [b_beam, 0.0]])
elp = [(0, 1), (1, 2), (2, 3)]
up, Kp, Fp, _, _ = frame(ndp, elp, E*A_sec, EI,
                         [0, 1, 2, 9, 10, 11], {3: H_load})
Rp = Kp @ up - Fp
value("Portal: yon siljish (haqiqiy EA bilan)", float(up[3])*1e3, "mm")
value("Portal: gorizontal muvozanat",
      float(Rp[0] + Rp[9] + H_load), "N")
value("Portal: vertikal muvozanat", float(Rp[1] + Rp[10]), "N")
M_tot = (Rp[2] + Rp[11] + (ndp[3][0]*Rp[10] - ndp[3][1]*Rp[9])
         + (ndp[0][0]*Rp[1] - ndp[0][1]*Rp[0]) - ndp[1][1]*H_load)
value("Portal: moment muvozanati (koordinata boshiga)",
      float(M_tot), "N*m")
note("Klassik burchak-ko'chish formulasi delta = H h^3 (2+3k) / "
     "(12 EI (1+6k)) to'rtta turli geometriyada ham FEM bilan 1e-6% "
     "aniqlikda mos tushdi. DIQQAT: formula sterjenlar "
     "CHO'ZILMAYDIGAN deb faraz qiladi, shuning uchun taqqoslashda EA "
     "juda katta olindi. Haqiqiy EA bilan siljish biroz boshqacha "
     "chiqadi - o'q deformatsiyasi qo'shimcha moslashuvchanlik beradi. "
     "Uchala muvozanat tenglamasi ham mashina aniqligida bajariladi.")

# --- (6) SILJISH DEFORMATSIYASI: Timoshenko va Eyler-Bernulli ---
def ke_timo(EI_, GA_, Le):
    phi = 12*EI_/(GA_*Le**2)
    cf = EI_/(Le**3*(1 + phi))
    return cf*np.array([
        [12, 6*Le, -12, 6*Le],
        [6*Le, (4 + phi)*Le**2, -6*Le, (2 - phi)*Le**2],
        [-12, -6*Le, 12, -6*Le],
        [6*Le, (2 - phi)*Le**2, -6*Le, (4 + phi)*Le**2]], dtype=float)


rows7 = []
hh, bb_ = 0.2, 0.1
Ib = bb_*hh**3/12
Ab = bb_*hh
P_t = 1e3
for slend in [2, 5, 10, 20, 50, 100]:
    Lt = slend*hh
    w_eb = P_t*Lt**3/(3*E*Ib)
    Kt = ke_timo(E*Ib, (5/6)*G*Ab, Lt)
    ut = np.linalg.solve(Kt[2:, 2:], np.array([P_t, 0.0]))
    phi = 12*E*Ib/((5/6)*G*Ab*Lt**2)
    rows7.append([slend, f"{w_eb:.6e}", f"{ut[0]:.6e}",
                  f"{abs(ut[0] - w_eb)/ut[0]*100:.3f}", f"{phi:.5f}"])
table("Siljish deformatsiyasi: Eyler-Bernulli va Timoshenko",
      ["L/h", "EB ko'chish", "Timoshenko", "farq %", "phi"], rows7)
series("Siljish ulushi", [2, 5, 10, 20, 50, 100],
       [float(r[3]) for r in rows7], xlabel="L/h", ylabel="farq, %")
note("Siljish deformatsiyasining ulushi (h/L)^2 kabi kamayadi: L/h = 2 "
     "da 16.3%, L/h = 10 da 0.77%, L/h = 100 da 0.008%. Shuning uchun "
     "ingichka balkalarda Eyler-Bernulli yetarli, qisqa va yo'g'on "
     "rigellarda esa Timoshenko kerak. Bu pq-24 dagi Mindlin-Reyssner "
     "plastinasi bilan BIR XIL g'oya va u yerdagi kabi bu yerda ham "
     "siljish qulflanishi xavfi bor (su-16).")

table("Balka va ramka elementlarining xossalari",
      ["Xossa", "Ferma (su-19)", "Balka", "Ramka"],
      [["Erkinlik darajasi/tugun", "2 yoki 3", "2 (w, theta)",
        "3 (u, w, theta)"],
       ["Bazis", "chiziqli", "Ermit kubik", "chiziqli + kubik"],
       ["Uzluksizlik", "C0", "C1", "C1 (egilish)"],
       ["Tugun aniqligi", "aynan", "aynan", "aynan"],
       ["Epyura element ichida", "doimiy", "moment chiziqli",
        "moment chiziqli"],
       ["Oraliq yuk", "MUMKIN EMAS", "mahkamlangan uch kuchlari",
        "mahkamlangan uch kuchlari"]])
''',
                parameters=[
                    p("n_el", "Elementlar soni", 1.0, 20.0, 4.0, 1.0),
                    p("L_b", "Balka uzunligi", 1.0, 12.0, 3.0, 0.5, "m"),
                    p("q_kNm", "Tarqalgan yuk", 1.0, 50.0, 5.0, 1.0,
                      "kN/m"),
                    p("h_col", "Portal ramka balandligi", 2.0, 10.0, 4.0,
                      0.5, "m"),
                    p("b_beam", "Portal ramka oralig'i", 2.0, 15.0, 6.0,
                      0.5, "m"),
                ],
                expected_output=(
                    "Ermit balka elementi "
                    "to'rtta klassik masalada "
                    "ham tugun qiymatlarini "
                    "$10^{-14}$% aniqlikda "
                    "beradi — hatto bitta "
                    "element bilan. "
                    "Mahkamlangan uch "
                    "momentini "
                    "($qL^2/12$) tushirib "
                    "qoldirish bitta "
                    "elementda 33,33% xato "
                    "beradi va u to'r "
                    "zichlashganda aynan "
                    "to'rt barobar "
                    "kamayadi. Ichki "
                    "kuchlarni "
                    "$\\mathbf{k}\\mathbf{u} "
                    "- \\mathbf{f}$ dan "
                    "tiklash tugunlarda "
                    "mashina aniqligini "
                    "beradi, $EI\\,w''$ esa "
                    "2–6% xato qoldiradi; "
                    "element ichida "
                    "$EI\\,w''$ xatosi "
                    "$|\\xi| \\approx "
                    "1/\\sqrt3$ da minimal "
                    "bo'ladi. Ramka "
                    "elementi burilishga "
                    "nisbatan invariant "
                    "($10^{-11}$% "
                    "darajasida), portal "
                    "ramka esa klassik "
                    "burchak-ko'chish "
                    "formulasi bilan "
                    "to'rtta geometriyada "
                    "$10^{-6}$% aniqlikda "
                    "mos tushadi. Siljish "
                    "deformatsiyasining "
                    "ulushi $L/h = 2$ da "
                    "16,3%, $L/h = 100$ da "
                    "0,008%."
                ),
            ),
            visual=vis(
                kind="Ermit funksiyalari va ichki kuch epyuralari",
                tool="React/SVG + Manim",
                description=(
                    "Ermit shakl funksiyalari, "
                    "deformatsiyalangan ramka va "
                    "moment epyurasining ikki "
                    "usulda tiklanishi."
                ),
                how_to_draw=(
                    "React/SVG: yuqori panelda "
                    "to'rtta Ermit funksiyasi "
                    "chiziladi. Ularning "
                    "ma'nosini ko'rsatish uchun "
                    "har birining yonida "
                    "kichik balka eskizi "
                    "turadi: $N_1$ uchun chap "
                    "uch birlik ko'chgan va "
                    "**burilmagan** balka, "
                    "$N_2$ uchun chap uch "
                    "birlik burilgan va "
                    "**ko'chmagan** balka. "
                    "Shu bilan 'erkinlik "
                    "darajasi' tushunchasi "
                    "ko'rinadi. O'rta panelda "
                    "ramka chiziladi va "
                    "deformatsiyalangan shakl "
                    "kuchaytirilgan holda "
                    "ustiga qo'yiladi; "
                    "tugunlardagi burchaklar "
                    "**saqlanishi** "
                    "($C^1$) alohida "
                    "belgilanadi — ferma "
                    "modelidagi sharnirdan "
                    "farqi shunda. Pastki "
                    "panel eng muhimi: "
                    "moment epyurasi uchta "
                    "chiziq bilan — aniq "
                    "parabola, "
                    "$EI\\,w''$ dan olingan "
                    "zinapoyasimon-chiziqli "
                    "egri va muvozanatdan "
                    "olingan tugun "
                    "qiymatlari. Tugun "
                    "nuqtalarida "
                    "muvozanat qiymatlari "
                    "parabolaga **aynan** "
                    "tegib turadi, "
                    "$EI\\,w''$ egri chizig'i "
                    "esa undan ajralib "
                    "qoladi va farq "
                    "shtrixlanadi. Element "
                    "sonini oshirish "
                    "slayderi bilan "
                    "shtrixlangan soha "
                    "qisqaradi."
                ),
            ),
            interp=(
                "Birinchi jadvalning natijasi "
                "ta'sirli: bitta balka "
                "elementi ham tugun "
                "ko'chishini va burilishini "
                "aynan beradi. Lekin bu "
                "ferma elementidagidan "
                "boshqacha hodisa. U yerda "
                "aniq yechimning o'zi "
                "chiziqli edi va bazis uni "
                "to'liq ifodalardi; bu "
                "yerda esa tarqalgan yuk "
                "ostida aniq yechim "
                "to'rtinchi darajali va "
                "kubik bazis uni "
                "ifodalay olmaydi — shunga "
                "qaramay **tugun "
                "qiymatlari** aynan "
                "to'g'ri. Bu su-13 dagi "
                "superkonvergensiyaning "
                "balka varianti va u faqat "
                "moslashgan yuk vektori "
                "bilan ishlaydi: "
                "$qL^2/12$ hadini tushirib "
                "qoldirsangiz, bitta "
                "elementda xato darhol "
                "33% ga chiqadi. Fermada "
                "xuddi shu xato 6,25% edi "
                "— balkada u besh barobar "
                "jiddiyroq, chunki "
                "burilish erkinlik "
                "darajasi butunlay "
                "yuklanmay qoladi. "
                "Mavzuning eng qimmatli "
                "amaliy natijasi esa "
                "uchinchi jadvalda. "
                "Momentni "
                "$EI\\,w_h''$ orqali olish "
                "2–6% xato beradi va bu "
                "xato tugunlarda ham "
                "yo'qolmaydi. "
                "Muvozanatdan tiklangan "
                "uch kuchlari esa "
                "tugunlarda mashina "
                "aniqligida to'g'ri. Farq "
                "sababi aniq: "
                "$\\mathbf{k}\\mathbf{u}_e "
                "- \\mathbf{f}_e$ "
                "elementning haqiqiy "
                "muvozanatini ifodalaydi, "
                "$EI\\,w_h''$ esa "
                "yaqinlashtirilgan "
                "maydonning hosilasi. "
                "Element ichida esa "
                "$EI\\,w_h''$ xatosi "
                "$|\\xi| \\approx "
                "1/\\sqrt3$ da minimal — "
                "su-16 dagi Barlou "
                "nuqtasi yana paydo "
                "bo'ldi. Ramka "
                "tajribalari kodning "
                "to'g'riligini ikki "
                "mustaqil yo'ldan "
                "tasdiqlaydi: burilishga "
                "nisbatan invariantlik "
                "va klassik "
                "burchak-ko'chish "
                "formulasi bilan to'rtta "
                "geometriyadagi "
                "kelishuv. Nihoyat "
                "siljish tajribasi "
                "chegarani belgilaydi: "
                "$L/h > 10$ bo'lsa "
                "Eyler–Bernulli yetarli, "
                "aks holda Timoshenko "
                "kerak — va bu pq-24 "
                "dagi Mindlin–Reyssner "
                "plastinasi bilan bir "
                "xil g'oya."
            ),
            mistakes=[
                "Oraliq yukni shunchaki "
                "ikkiga bo'lib tugunlarga "
                "qo'yish. $qL^2/12$ moment "
                "hadlari kerak; ularsiz "
                "bitta elementda 33% xato.",
                "Momentni $EI\\,w''$ dan "
                "olish. To'g'ri yo'l — "
                "$\\mathbf{k}\\mathbf{u}_e - "
                "\\mathbf{f}_e$, u tugunlarda "
                "aynan to'g'ri.",
                "Bitta element bilan epyura "
                "chizish. Tugun qiymatlari "
                "aniq, lekin element "
                "ichidagi moment chiziqli "
                "— epyura uchun 3–5 element "
                "kerak.",
                "Ferma va ramka modelini "
                "adashtirish. Payvandlangan "
                "tugun moment uzatadi; "
                "sharnirli model uni "
                "e'tiborsiz qoldiradi.",
                "Qisqa rigellarda siljish "
                "deformatsiyasini "
                "unutish. $L/h < 10$ da "
                "farq 1% dan oshadi.",
                "Timoshenko elementini "
                "to'liq integrallash bilan "
                "ishlatish — siljish "
                "qulflanishi paydo bo'ladi "
                "(su-16).",
            ],
            quiz=[
                q("Balka elementida nima uchun "
                  "$C^1$ uzluksizlik kerak?",
                  "Egilish energiyasida "
                  "ikkinchi hosila "
                  "$(w'')^2$ qatnashadi; "
                  "$w'$ uzilsa "
                  "$w''$ da delta-funksiya "
                  "paydo bo'lib energiya "
                  "cheksizlashadi.",
                  "konseptual"),
                q("$C^1$ qanday "
                  "ta'minlanadi?",
                  "Burilish ham tugun "
                  "noma'lumi qilinadi, "
                  "shunda qo'shni "
                  "elementlarda u "
                  "avtomatik mos tushadi "
                  "— shundan Ermit "
                  "bazisi kelib chiqadi.",
                  "konseptual"),
                q("Konsol balkada bitta "
                  "element bilan $w(L)$ "
                  "nechaga teng chiqadi?",
                  "$qL^4/(8EI)$ — analitik "
                  "yechim bilan aynan bir "
                  "xil. Burilish ham aynan: "
                  "$qL^3/(6EI)$.", "hisob"),
                q("Kod momentni ikki usulda "
                  "tiklaydi. Natijalari "
                  "qanday farq qiladi?",
                  "$\\mathbf{k}\\mathbf{u} - "
                  "\\mathbf{f}$ tugunlarda "
                  "mashina aniqligida "
                  "to'g'ri, $EI\\,w''$ esa "
                  "2–6% xato beradi — "
                  "tugunlarda ham.", "kod"),
                q("Ramka kodini tekshirishning "
                  "eng oson usuli qaysi?",
                  "Burilishga nisbatan "
                  "invariantlik: bir xil "
                  "masalani turli burchaklarda "
                  "joylashtirib, natija "
                  "o'zgarmasligini tekshirish. "
                  "Kodda xato $10^{-11}$% "
                  "darajasida.", "kod"),
                q("Siljish deformatsiyasi "
                  "qachon hisobga "
                  "olinishi kerak?",
                  "$L/h < 10$ bo'lganda. "
                  "Ulush $(h/L)^2$ kabi "
                  "kamayadi: $L/h = 2$ da "
                  "16,3%, $L/h = 10$ da "
                  "0,77%, $L/h = 100$ da "
                  "0,008%.", "talqin"),
                q("Bitta element aniq javob "
                  "bersa, nega ko'proq "
                  "element kerak bo'ladi?",
                  "Aniqlik faqat tugun "
                  "qiymatlariga tegishli. "
                  "Element ichida ko'chish "
                  "kubik, moment esa "
                  "chiziqli yaqinlashish — "
                  "epyura uchun zichroq "
                  "to'r kerak.", "talqin"),
            ],
            bridge=(
                "Ferma, balka va ramka "
                "elementlari bir o'lchovli "
                "edi: ular uzun va ingichka "
                "konstruksiyalarga mos. "
                "Keyingi mavzuda ikki "
                "o'lchovga o'tamiz — tekis "
                "kuchlanish va tekis "
                "deformatsiya masalalari, "
                "CST, Q4 va Q8 elementlari "
                "hamda kuchlanish "
                "konsentratsiyasi hisobi."
            ),
            research=(
                "Sterjenli tizimlar tahlilini "
                "chuqurlashtiring. "
                "(1) Plastik sharnirlar "
                "usulini o'rganing: ramkaning "
                "chegaraviy yuk "
                "ko'taruvchanligi qanday "
                "topiladi va u chiziqli "
                "hisobdan qanchalik "
                "farq qiladi? "
                "(2) Geometrik bikrlik "
                "matritsasini ko'rib chiqing: "
                "o'q kuchi egilish bikrligini "
                "o'zgartiradi va bu "
                "ustuvorlik masalasiga olib "
                "keladi (su-23). "
                "(3) Burama-egilish "
                "(warping torsion) "
                "nazariyasini o'rganing: "
                "ochiq yupqa devorli "
                "kesimlarda ettinchi "
                "erkinlik darajasi paydo "
                "bo'ladi. "
                "(4) Qattiq uchlar (rigid "
                "end offsets) va yarim "
                "bikr tugunlarni ko'rib "
                "chiqing: haqiqiy "
                "payvandlangan tugunning "
                "bikrligi cheksiz emas."
            ),
            manim_ref=manim(
                scene="BeamFrameScene",
                module="manim/scenes/su_apps.py",
                title="Ermit bazisi va moment epyurasi",
                summary=(
                    "To'rtta Ermit funksiyasi "
                    "birin-ketin chiziladi va "
                    "har biri mos keladigan "
                    "balka deformatsiyasi "
                    "bilan ko'rsatiladi. Keyin "
                    "sharnirli balka "
                    "yuklanadi va ikkita "
                    "moment epyurasi "
                    "qo'yiladi: "
                    "$EI\\,w''$ dan olingan "
                    "siniq chiziq aniq "
                    "paraboladan ajralib "
                    "turadi, muvozanatdan "
                    "olingan tugun "
                    "nuqtalari esa "
                    "parabolaga aynan "
                    "tushadi. Oxirida "
                    "portal ramka shamol "
                    "yuki ostida "
                    "deformatsiyalanadi."
                ),
            ),
        ),
    ),

    # ------------------------------------------------------------------ su-21
    Topic(
        id="su-21",
        subject_id=S, module_id=M, order=21,
        title="Tekis masala elementlari va kuchlanish konsentratsiyasi",
        description=(
            "Tekis kuchlanish va tekis deformatsiya, doimiy "
            "deformatsiyali uchburchak (CST), Q4 va Q8 elementlari, "
            "yamoq sinovi hamda teshik atrofidagi kuchlanish "
            "konsentratsiyasini hisoblash."
        ),
        learning_objective=(
            "Tekis masala uchun element turini asoslab tanlash va "
            "kuchlanish konsentratsiyasi koeffitsientini Kirsh analitik "
            "yechimi bilan tekshirilgan holda hisoblash."
        ),
        prerequisites=["su-20", "tmm-17", "tmm-13"],
        mathematical_core=(
            "$\\boldsymbol\\varepsilon = \\mathbf{B}\\mathbf{u}$, "
            "$\\mathbf{k} = \\int\\mathbf{B}^T\\mathbf{D}\\mathbf{B}"
            "\\,t\\,dA$; Kirsh: $\\sigma_\\theta(r) = "
            "\\frac{\\sigma}{2}\\left(2 + \\frac{a^2}{r^2} + "
            "\\frac{3a^4}{r^4}\\right)$."
        ),
        engineering_application=(
            "Teshik va galtellar atrofidagi kuchlanish konsentratsiyasi, "
            "plastina va devor konstruksiyalari, tishli g'ildirak tishi "
            "asosi, charchoq hisobining boshlang'ich nuqtasi."
        ),
        computational_component=(
            "Yamoq sinovi, uch element turini taqqoslash, teshikli "
            "plastinada $K_t$ ni ikki bosqichli yaqinlashish bilan "
            "aniqlash."
        ),
        visualization_component=(
            "Kuchlanish maydonining rangli xaritasi, teshik atrofidagi "
            "konsentratsiya va uning radial so'nishi."
        ),
        research_extension=(
            "Kuchlanish konsentratsiyasi va charchoq bog'liqligini "
            "o'rganing: nima uchun $K_f < K_t$ va o'lchamning ta'siri "
            "qanday."
        ),
        difficulty="murakkab",
        previous_link=(
            "su-19 va su-20 dagi elementlar bir o'lchovli edi — ular "
            "uzun va ingichka konstruksiyalarga mos. Teshik atrofidagi "
            "kuchlanish maydoni esa mohiyatan ikki o'lchovli va uni "
            "sterjen modeli bilan umuman ifodalab bo'lmaydi."
        ),
        next_topic="su-22",
        estimated_minutes=95,
        tags=["tekis kuchlanish", "CST", "Q4", "Q8", "Kirsh masalasi",
              "yamoq sinovi"],
        lesson=_lesson(
            problem=(
                "Samolyot qanotining "
                "qoplamasida texnologik "
                "teshiklar bor: zambaraklar, "
                "lyuklar, kabel o'tkazgichlari. "
                "Har bir teshik atrofida "
                "kuchlanish o'sadi va "
                "charchoq yorig'i aynan "
                "shu yerdan boshlanadi. "
                "Nominal kuchlanish "
                "100 MPa bo'lsa, teshik "
                "chekkasida nechchi bo'ladi? "
                "tmm-17 dagi Kirsh yechimi "
                "cheksiz plastina uchun "
                "$K_t = 3$ beradi, lekin "
                "haqiqiy qoplama chekli "
                "kenglikda, teshiklar bir "
                "biriga yaqin va shakli "
                "har doim ham doira emas. "
                "Bunday holatda ishonchli "
                "javobni qanday olish va "
                "unga qanday ishonish "
                "mumkin?"
            ),
            concepts=[
                c("Tekis kuchlanish "
                  "(plane stress)",
                  "Yupqa plastina, tekislikka "
                  "perpendikulyar kuchlanish "
                  "nol: "
                  "$\\sigma_z = 0$ (tmm-13)."),
                c("Tekis deformatsiya "
                  "(plane strain)",
                  "Uzun jism, o'q bo'ylab "
                  "deformatsiya nol: "
                  "$\\varepsilon_z = 0$; "
                  "to'g'on, tunnel, quvur."),
                c("CST — doimiy deformatsiyali "
                  "uchburchak",
                  "Eng sodda element; "
                  "deformatsiya element ichida "
                  "**doimiy**, shuning uchun "
                  "juda sekin yaqinlashadi."),
                c("Q4 va Q8",
                  "To'rt va sakkiz tugunli "
                  "to'rtburchaklar; Q8 "
                  "serendipiti — markaziy "
                  "tuguni yo'q."),
                c("Yamoq sinovi (patch test)",
                  "Element doimiy deformatsiya "
                  "maydonini **aynan** "
                  "tiklashi kerak — "
                  "yaqinlashishning zaruriy "
                  "sharti (su-14)."),
                c("Kuchlanish konsentratsiyasi "
                  "koeffitsienti $K_t$",
                  "$K_t = \\sigma_{max}/"
                  "\\sigma_{nom}$; doiraviy "
                  "teshik uchun cheksiz "
                  "plastinada aynan 3."),
            ],
            derivation=[
                d("1. Tekis holat "
                  "taxminlari",
                  r"\text{tekis kuchlanish: } "
                  r"\sigma_z = \tau_{xz} = "
                  r"\tau_{yz} = 0",
                  "Yupqa plastinada "
                  "qalinlik bo'ylab "
                  "kuchlanish rivojlana "
                  "olmaydi. Tekis "
                  "deformatsiyada esa "
                  "$\\varepsilon_z = 0$ va "
                  "$\\sigma_z = "
                  "\\nu(\\sigma_x + "
                  "\\sigma_y) \\ne 0$."),
                d("2. Material matritsasi",
                  r"\mathbf{D}_{\sigma} = "
                  r"\frac{E}{1-\nu^2}"
                  r"\begin{bmatrix} 1 & \nu & "
                  r"0\\ \nu & 1 & 0\\ 0 & 0 & "
                  r"\frac{1-\nu}{2}"
                  r"\end{bmatrix}",
                  "Tekis deformatsiya uchun "
                  "$E \\to E/(1-\\nu^2)$, "
                  "$\\nu \\to \\nu/(1-\\nu)$ "
                  "almashtirish yetarli — "
                  "bitta kod ikkalasiga "
                  "yaraydi."),
                d("3. Deformatsiya matritsasi",
                  r"\boldsymbol\varepsilon = "
                  r"\{\varepsilon_x, "
                  r"\varepsilon_y, "
                  r"\gamma_{xy}\}^T = "
                  r"\mathbf{B}\mathbf{u}",
                  "$\\mathbf{B}$ ning "
                  "qatorlari shakl "
                  "funksiyalarining "
                  "$x$ va $y$ bo'yicha "
                  "hosilalaridan tuziladi "
                  "(su-14)."),
                d("4. CST ning "
                  "deformatsiyasi",
                  r"\mathbf{B} = "
                  r"\frac{1}{2A}\begin{bmatrix} "
                  r"b_1 & 0 & b_2 & 0 & b_3 & 0"
                  r"\\ 0 & c_1 & 0 & c_2 & 0 & "
                  r"c_3\\ c_1 & b_1 & c_2 & b_2 "
                  r"& c_3 & b_3\end{bmatrix}",
                  "**Muhim kuzatuv.** "
                  "$b_i$ va $c_i$ faqat "
                  "koordinatalardan iborat, "
                  "demak $\\mathbf{B}$ "
                  "**doimiy** — deformatsiya "
                  "element ichida "
                  "o'zgarmaydi."),
                d("5. CST ning "
                  "cheklovi",
                  r"\varepsilon = "
                  r"\text{const} \ "
                  r"\Longrightarrow\ "
                  r"\text{egilishni "
                  r"ifodalash uchun ko'p "
                  r"element kerak}",
                  "Egilishda deformatsiya "
                  "chiziqli o'zgarishi "
                  "kerak, CST esa bo'lakli "
                  "doimiy beradi — bu "
                  "su-16 dagi qulflanishning "
                  "eng qo'pol ko'rinishi."),
                d("6. Element matritsasi",
                  r"\mathbf{k} = "
                  r"\int_A \mathbf{B}^T"
                  r"\mathbf{D}\mathbf{B}\,t\,dA "
                  r"= \mathbf{B}^T\mathbf{D}"
                  r"\mathbf{B}\,tA \ "
                  r"(\text{CST uchun})",
                  "CST da integral aynan "
                  "olinadi, chunki "
                  "integrand doimiy. Q4 va "
                  "Q8 uchun Gauss "
                  "kvadraturasi kerak "
                  "(su-16)."),
                d("7. Yamoq sinovi",
                  r"u = a_0 + a_1x + a_2y "
                  r"\;\Longrightarrow\; "
                  r"\boldsymbol\varepsilon_h = "
                  r"\boldsymbol\varepsilon \ "
                  r"\text{(aynan)}",
                  "**Majburiy tekshiruv.** "
                  "Har qanday yangi element "
                  "uchun birinchi bajariladigan "
                  "test; bajarilmasa element "
                  "yaqinlashmaydi."),
                d("8. Kirsh yechimi",
                  r"\sigma_\theta(r,\theta) = "
                  r"\frac{\sigma}{2}\left[\left("
                  r"1 + \frac{a^2}{r^2}\right) - "
                  r"\left(1 + \frac{3a^4}{r^4}"
                  r"\right)\cos2\theta\right]",
                  "tmm-17 dagi aniq yechim. "
                  "$\\theta = 90°$, $r = a$ "
                  "da $\\sigma_\\theta = "
                  "3\\sigma$."),
                d("9. Konsentratsiyaning "
                  "so'nishi",
                  r"\sigma_\theta(r, 90^\circ) = "
                  r"\frac{\sigma}{2}\left(2 + "
                  r"\frac{a^2}{r^2} + "
                  r"\frac{3a^4}{r^4}\right)",
                  "**Amaliy muhim natija.** "
                  "$r = 3a$ da "
                  "$\\sigma_\\theta = "
                  "1{,}07\\sigma$ — "
                  "konsentratsiya juda tez "
                  "so'nadi. Sen-Venan "
                  "prinsipining (tmm-14) "
                  "aniq ko'rinishi."),
                d("10. Teshik chekkasidagi "
                  "siqilish",
                  r"\sigma_\theta(a, 0^\circ) = "
                  r"\frac{\sigma}{2}(2 - 4) = "
                  r"-\sigma",
                  "**Mustaqil tekshiruv.** "
                  "Yuk yo'nalishi bo'ylab "
                  "teshik chekkasida "
                  "**siqilish** paydo "
                  "bo'ladi — sonli yechimni "
                  "tekshirishning ikkinchi "
                  "nuqtasi."),
                d("11. Chekli kenglik ta'siri",
                  r"K_t^{chekli} > K_t^{\infty} "
                  r"= 3",
                  "Kirsh yechimi cheksiz "
                  "plastina uchun. Chekli "
                  "kenglikda material kamroq "
                  "va $K_t$ **oshadi** — kod "
                  "buni $W/a = 5$ da 3,35 "
                  "sifatida ko'rsatadi."),
                d("12. Ikki xil xatolik",
                  r"\text{xato} = "
                  r"\underbrace{\text{to'r}}"
                  r"_{\text{diskretlashtirish}} "
                  r"+ \underbrace{W/a}"
                  r"_{\text{model}}",
                  "**Hal qiluvchi ajratish.** "
                  "To'rni zichlashtirish "
                  "birinchisini kamaytiradi, "
                  "ikkinchisini esa **yo'q** "
                  "— buning uchun sohani "
                  "kattalashtirish kerak. "
                  "Bu su-29 dagi V&V "
                  "ning asosi."),
            ],
            meaning=(
                "4- va 5-qadamlar CST "
                "elementining taqdirini "
                "belgilaydi. Uning "
                "deformatsiya matritsasi "
                "doimiy, demak element "
                "ichida deformatsiya "
                "o'zgara olmaydi. Egilishda "
                "esa deformatsiya "
                "balandlik bo'ylab chiziqli "
                "o'zgarishi kerak, shuning "
                "uchun CST buni faqat "
                "bo'lakli doimiy zinapoya "
                "bilan yaqinlashtiradi. "
                "Kod buni shafqatsiz "
                "ko'rsatadi: CST 576 "
                "erkinlik darajasi bilan "
                "javobning atigi 87% ini "
                "beradi, Q8 esa 40 "
                "erkinlik darajasi bilan "
                "97% ini. Farq o'n to'rt "
                "barobar kamroq noma'lum "
                "bilan ancha yaxshi "
                "natija. Shuning uchun "
                "zamonaviy paketlarda CST "
                "deyarli ishlatilmaydi — "
                "u faqat to'r "
                "generatorining murakkab "
                "geometriyani to'ldirishi "
                "uchun zaxira sifatida "
                "qoladi. Mavzuning "
                "muhandislik markazi esa "
                "9- va 12-qadamlarda. "
                "9-qadam tinchlantiradi: "
                "konsentratsiya juda tez "
                "so'nadi — teshikdan uch "
                "radius narida kuchlanish "
                "nominaldan atigi 7% "
                "yuqori. Demak "
                "teshiklar bir-biridan "
                "yetarlicha uzoq bo'lsa, "
                "ular mustaqil ishlaydi "
                "va har birini alohida "
                "hisoblash mumkin. Bu "
                "Sen-Venan prinsipining "
                "(tmm-14) miqdoriy "
                "ifodasi. 12-qadam esa "
                "butun kursning eng muhim "
                "uslubiy g'oyalaridan "
                "birini kiritadi: sonli "
                "natijaning xatosi ikki "
                "manbadan keladi va ular "
                "**har xil davolanadi**. "
                "To'r qo'pol bo'lsa — uni "
                "zichlashtiring. Lekin "
                "modelning o'zi noto'g'ri "
                "bo'lsa (bu yerda: chekli "
                "sohani cheksiz deb "
                "hisoblash), to'rni qancha "
                "zichlashtirmang, javob "
                "noto'g'ri qiymatga "
                "yaqinlashadi. Kod buni "
                "aniq ko'rsatadi: "
                "$W/a = 5$ da to'r "
                "zichlashganda "
                "$K_t$ 3 ga emas, 3,35 ga "
                "intiladi. Bu xato emas — "
                "bu o'sha geometriya uchun "
                "to'g'ri javob. Xato "
                "bo'lardi, agar biz uni "
                "cheksiz plastinaning "
                "javobi deb "
                "e'lon qilsak."
            ),
            equations=[
                eq(r"\mathbf{k} = \int_A "
                   r"\mathbf{B}^T\mathbf{D}"
                   r"\mathbf{B}\,t\,dA, \qquad "
                   r"\mathbf{D}_\sigma = "
                   r"\frac{E}{1-\nu^2}\begin{bmatrix} "
                   r"1 & \nu & 0\\ \nu & 1 & 0\\ "
                   r"0 & 0 & \frac{1-\nu}{2}"
                   r"\end{bmatrix}",
                   "Tekis masala elementining "
                   "matritsasi va tekis "
                   "kuchlanish uchun material "
                   "matritsasi.",
                   "Element matritsasi"),
                eq(r"\sigma_\theta(r,\theta) = "
                   r"\frac{\sigma}{2}\left[\left("
                   r"1 + \frac{a^2}{r^2}\right) - "
                   r"\left(1 + \frac{3a^4}{r^4}"
                   r"\right)\cos 2\theta\right]",
                   "Kirsh yechimi — sonli "
                   "natijani tekshirish uchun "
                   "etalon (tmm-17).",
                   "Kirsh yechimi"),
                eq(r"\sigma_\theta(a, 90^\circ) = "
                   r"3\sigma, \qquad "
                   r"\sigma_\theta(a, 0^\circ) = "
                   r"-\sigma",
                   "Teshik chekkasidagi ikkita "
                   "mustaqil tekshiruv "
                   "nuqtasi.",
                   "Tekshiruv nuqtalari"),
                eq(r"\text{xato} = "
                   r"\text{diskretlashtirish}(h) "
                   r"+ \text{model}(W/a)",
                   "Ikki xil xatolik manbai; "
                   "ular har xil davolanadi.",
                   "Xatolik manbalari"),
            ],
            conditions=(
                "**Qaysi tekis holat:**\n"
                "- Qalinlik boshqa "
                "o'lchamlardan ancha kichik → "
                "tekis kuchlanish;\n"
                "- Jism o'q bo'ylab uzun va "
                "uchlari to'sqinlik qilingan → "
                "tekis deformatsiya;\n"
                "- Noto'g'ri tanlash "
                "$\\nu$ ta'siri orqali "
                "sezilarli xato beradi, "
                "ayniqsa $\\nu \\to 0{,}5$ "
                "da (su-16).\n\n"
                "**Element tanlash:**\n"
                "- Egilish ustun → Q8 yoki "
                "yuqori tartib;\n"
                "- Q4 → faqat zich to'r "
                "bilan yoki SRI bilan "
                "(su-16);\n"
                "- CST → faqat "
                "to'ldiruvchi sifatida; "
                "asosiy element sifatida "
                "**tavsiya etilmaydi**.\n\n"
                "**Konsentratsiya "
                "hisobida:**\n"
                "1. Teshik chekkasida "
                "kamida 8–12 element "
                "chorak aylana bo'ylab;\n"
                "2. $W/a \\ge 10$ — "
                "cheksiz plastina bilan "
                "solishtirish uchun;\n"
                "3. To'r bo'yicha "
                "yaqinlashishni "
                "**ko'rsating** — bitta "
                "hisob yetarli emas "
                "(su-18);\n"
                "4. Kuchlanishni Gauss "
                "nuqtalaridan tiklang "
                "(su-17).\n\n"
                "**Ogohlantirish:** o'tkir "
                "burchakda (galtelsiz) "
                "aniq kuchlanish "
                "**cheksiz** va $K_t$ "
                "ma'nosini yo'qotadi. "
                "U yerda yorilish "
                "mexanikasi parametrlari "
                "(tmm-24) yoki plastiklik "
                "kerak."
            ),
            worked=WorkedExample(
                statement=(
                    "Kengligi $2W = 200$ mm "
                    "bo'lgan plastinada "
                    "diametri $2a = 20$ mm "
                    "teshik bor. Plastina "
                    "$\\sigma = 100$ MPa "
                    "tortilgan. (a) Teshik "
                    "chekkasidagi maksimal "
                    "kuchlanishni toping; "
                    "(b) teshikdan qaysi "
                    "masofada kuchlanish "
                    "nominaldan 5% dan kam "
                    "farq qiladi; (c) "
                    "$\\theta = 0$ da "
                    "kuchlanish qanday."
                ),
                given=[
                    r"a = 10\ \text{mm}, \quad "
                    r"W = 100\ \text{mm}, \quad "
                    r"\sigma = 100\ \text{MPa}",
                    r"\sigma_\theta(r,90^\circ) = "
                    r"\frac{\sigma}{2}\left(2 + "
                    r"\frac{a^2}{r^2} + "
                    r"\frac{3a^4}{r^4}\right)",
                ],
                steps=[
                    st(r"W/a = 100/10 = 10",
                       "Nisbat yetarlicha katta — "
                       "cheksiz plastina "
                       "taxmini o'rinli."),
                    st(r"r = a: \quad "
                       r"\sigma_\theta = "
                       r"\frac{\sigma}{2}"
                       r"\left(2 + 1 + 3\right) "
                       r"= 3\sigma",
                       "**$K_t = 3$** — "
                       "klassik natija."),
                    st(r"\sigma_{max} = 3 \cdot "
                       r"100 = 300\ \text{MPa}",
                       "Maksimal kuchlanish."),
                    st(r"\text{(b)}\quad "
                       r"\frac{\sigma_\theta}"
                       r"{\sigma} = 1{,}05 "
                       r"\;\Rightarrow\; "
                       r"\frac12\left(2 + "
                       r"\rho^{-2} + 3\rho^{-4}"
                       r"\right) = 1{,}05",
                       "$\\rho = r/a$ "
                       "belgilaymiz."),
                    st(r"\rho^{-2} + 3\rho^{-4} = "
                       r"0{,}10",
                       "Tenglamani "
                       "soddalashtiramiz."),
                    st(r"t = \rho^{-2}: \quad "
                       r"3t^2 + t - 0{,}10 = 0",
                       "Kvadrat tenglama."),
                    st(r"t = \frac{-1 + "
                       r"\sqrt{1 + 1{,}2}}{6} = "
                       r"\frac{-1 + 1{,}4832}{6} "
                       r"= 0{,}08054",
                       "Musbat ildiz."),
                    st(r"\rho = 1/\sqrt{0{,}08054} "
                       r"= 3{,}524",
                       "**$r \\approx 3{,}5a$** — "
                       "ya'ni teshikdan "
                       "35 mm narida."),
                    st(r"\text{(c)}\quad "
                       r"\sigma_\theta(a,0) = "
                       r"\frac{\sigma}{2}\left[2 - "
                       r"4\right] = -\sigma",
                       "$\\cos 0 = 1$ qo'yib."),
                    st(r"\sigma_\theta(a,0) = "
                       r"-100\ \text{MPa}",
                       "**Siqilish** — yuk "
                       "yo'nalishi bo'ylab "
                       "teshik chekkasida."),
                    st(r"\Delta\sigma = 300 - "
                       r"(-100) = 400\ "
                       r"\text{MPa}",
                       "Teshik chekkasi bo'ylab "
                       "kuchlanish o'zgarish "
                       "oralig'i — charchoq "
                       "uchun aynan shu "
                       "muhim."),
                ],
                answer=(
                    "(a) "
                    "$\\sigma_{max} = 300$ MPa "
                    "($K_t = 3$); "
                    "(b) $r \\approx 3{,}5a = "
                    "35$ mm da kuchlanish "
                    "nominaldan 5% dan kam "
                    "farq qiladi; "
                    "(c) $\\theta = 0$ da "
                    "$\\sigma_\\theta = "
                    "-100$ MPa (siqilish). "
                    "Kod bu uchala qiymatni "
                    "ham 0,3–0,7% aniqlikda "
                    "takrorlaydi."
                ),
                engineering_note=(
                    "(b) javobidagi "
                    "$3{,}5a$ amaliyotda "
                    "juda foydali qoida. "
                    "Teshiklar bir-biridan "
                    "yetti radiusdan "
                    "ko'proq uzoqlikda "
                    "bo'lsa, ular "
                    "bir-biriga deyarli "
                    "ta'sir qilmaydi va har "
                    "birini alohida "
                    "hisoblash mumkin. "
                    "Yaqinroq bo'lsa "
                    "ta'sirlar qo'shiladi "
                    "va $K_t$ oshadi. "
                    "Xuddi shu qoida to'r "
                    "qurishda ham kerak: "
                    "model chegarasini "
                    "teshikdan kamida "
                    "besh-o'n radius "
                    "narida joylashtiring, "
                    "aks holda chegaraviy "
                    "shart natijani "
                    "buzadi. (c) javobi "
                    "esa charchoq "
                    "nuqtai nazaridan "
                    "muhimroq bo'lishi "
                    "mumkin. Teshik "
                    "chekkasi bo'ylab "
                    "kuchlanish "
                    "$+300$ dan $-100$ MPa "
                    "gacha o'zgaradi, ya'ni "
                    "oraliq 400 MPa. "
                    "Takroriy yuklamada "
                    "aynan shu oraliq "
                    "yorilish "
                    "boshlanishini "
                    "belgilaydi. Nihoyat "
                    "eng muhim amaliy "
                    "ogohlantirish: "
                    "$K_t = 3$ faqat "
                    "**doiraviy** teshik "
                    "uchun. Ellips uchun "
                    "$K_t = 1 + 2b/a$ va "
                    "u cho'zilgan teshikda "
                    "tez o'sadi; o'tkir "
                    "burchakda esa "
                    "cheksizlashadi. "
                    "Shuning uchun "
                    "aviatsiyada barcha "
                    "teshiklar doiraviy "
                    "va chekkalari "
                    "silliqlangan."
                ),
            ),
            computation=Computation(
                caption=(
                    "Yamoq sinovi, uch element "
                    "turini taqqoslash va "
                    "teshikli plastinada $K_t$ "
                    "ni Kirsh yechimi bilan "
                    "tekshirish."
                ),
                code='''"""Tekis masala elementlari va kuchlanish konsentratsiyasi."""
import numpy as np
from labkit import PARAMS, note, series, table, value

W_over_a = float(PARAMS.get("W_over_a", 20.0))
n_ring = int(PARAMS.get("n_ring", 20))
grade = float(PARAMS.get("grade", 3.0))
nu = float(PARAMS.get("nu", 0.3))

E = 2.1e11
a_hole = 0.01
sig_inf = 1e6


def Dmat(nu_, mode):
    if mode == "stress":
        return E/(1 - nu_**2)*np.array([[1, nu_, 0], [nu_, 1, 0],
                                        [0, 0, (1 - nu_)/2]])
    return E/((1 + nu_)*(1 - 2*nu_))*np.array(
        [[1 - nu_, nu_, 0], [nu_, 1 - nu_, 0], [0, 0, (1 - 2*nu_)/2]])


def shp_q4(xi, eta):
    xn = np.array([-1, 1, 1, -1.])
    yn = np.array([-1, -1, 1, 1.])
    N = 0.25*(1 + xi*xn)*(1 + eta*yn)
    dN = np.vstack([0.25*xn*(1 + eta*yn), 0.25*(1 + xi*xn)*yn])
    return N, dN


def shp_q8(xi, eta):
    xn = np.array([-1, 1, 1, -1, 0, 1, 0, -1.])
    yn = np.array([-1, -1, 1, 1, -1, 0, 1, 0.])
    N = np.zeros(8)
    dN = np.zeros((2, 8))
    for i in range(4):
        N[i] = 0.25*(1 + xi*xn[i])*(1 + eta*yn[i])*(xi*xn[i] + eta*yn[i] - 1)
        dN[0, i] = 0.25*xn[i]*(1 + eta*yn[i])*(2*xi*xn[i] + eta*yn[i])
        dN[1, i] = 0.25*(1 + xi*xn[i])*yn[i]*(xi*xn[i] + 2*eta*yn[i])
    for i in (4, 6):
        N[i] = 0.5*(1 - xi**2)*(1 + eta*yn[i])
        dN[0, i] = -xi*(1 + eta*yn[i])
        dN[1, i] = 0.5*(1 - xi**2)*yn[i]
    for i in (5, 7):
        N[i] = 0.5*(1 + xi*xn[i])*(1 - eta**2)
        dN[0, i] = 0.5*xn[i]*(1 - eta**2)
        dN[1, i] = -(1 + xi*xn[i])*eta
    return N, dN


def Bmat(shp, xi, eta, xy):
    N, dN = shp(xi, eta)
    J = dN @ xy
    dNx = np.linalg.solve(J, dN)
    n = len(xy)
    B = np.zeros((3, 2*n))
    B[0, 0::2] = dNx[0]
    B[1, 1::2] = dNx[1]
    B[2, 0::2] = dNx[1]
    B[2, 1::2] = dNx[0]
    return B, float(np.linalg.det(J)), N


def ke_quad(xy, D, shp, ngp, t=1.0):
    n = len(xy)
    k = np.zeros((2*n, 2*n))
    g, w = np.polynomial.legendre.leggauss(ngp)
    for aa in range(ngp):
        for bb in range(ngp):
            B, dJ, _ = Bmat(shp, g[aa], g[bb], xy)
            k += B.T @ D @ B*dJ*w[aa]*w[bb]*t
    return k


def cst(xy, D, t=1.0):
    (x1, y1), (x2, y2), (x3, y3) = xy
    A = 0.5*((x2 - x1)*(y3 - y1) - (x3 - x1)*(y2 - y1))
    b = np.array([y2 - y3, y3 - y1, y1 - y2])
    c = np.array([x3 - x2, x1 - x3, x2 - x1])
    B = np.zeros((3, 6))
    B[0, 0::2] = b/(2*A)
    B[1, 1::2] = c/(2*A)
    B[2, 0::2] = c/(2*A)
    B[2, 1::2] = b/(2*A)
    return B.T @ D @ B*A*t, B, A


# --- (1) YAMOQ SINOVI: doimiy deformatsiya aynan tiklanadimi? ---
D0 = Dmat(nu, "stress")
a0, b0, c0 = 0.01, 2e-4, 1e-4
d0, e0, f0 = -0.02, 3e-4, -1.5e-4
eps_ref = np.array([b0, f0, c0 + e0])
rows = []
for name, shp, xy, ngp in [
        ("Q4", shp_q4, np.array([[0, 0], [2, 0], [2.3, 2.1], [0.2, 1.8]],
                                float), 2),
        ("Q8", shp_q8, np.array([[0, 0], [2, 0], [2, 2], [0, 2],
                                 [1.1, 0.1], [2.1, 1.0], [0.9, 2.1],
                                 [-0.1, 1.0]], float), 3)]:
    n = len(xy)
    uu = np.zeros(2*n)
    for i in range(n):
        uu[2*i] = a0 + b0*xy[i, 0] + c0*xy[i, 1]
        uu[2*i + 1] = d0 + e0*xy[i, 0] + f0*xy[i, 1]
    g, w = np.polynomial.legendre.leggauss(ngp)
    err = 0.0
    for aa in range(ngp):
        for bb in range(ngp):
            B, _, _ = Bmat(shp, g[aa], g[bb], xy)
            err = max(err, float(np.max(np.abs(B @ uu - eps_ref))))
    kk = ke_quad(xy, D0, shp, ngp)
    ev = np.linalg.eigvalsh(kk)
    rows.append([name, f"{err:.3e}", int(np.sum(ev < 1e-8*ev.max())), 3])
xy_t = np.array([[0, 0], [2, 0.3], [0.7, 2.]], float)
uu = np.zeros(6)
for i in range(3):
    uu[2*i] = a0 + b0*xy_t[i, 0] + c0*xy_t[i, 1]
    uu[2*i + 1] = d0 + e0*xy_t[i, 0] + f0*xy_t[i, 1]
kk, Bc, Ac = cst(xy_t, D0)
ev = np.linalg.eigvalsh(kk)
rows.insert(0, ["CST", f"{float(np.max(np.abs(Bc @ uu - eps_ref))):.3e}",
                int(np.sum(ev < 1e-8*ev.max())), 3])
table("Yamoq sinovi: doimiy deformatsiya maydoni",
      ["element", "deformatsiya xatosi", "nol rejimlar",
       "kutilgan (qattiq jism)"], rows)
note("Uchala element ham yamoq sinovidan MASHINA ANIQLIGIDA o'tdi va "
     "har birida aynan uchta qattiq jism rejimi bor (ikkita ko'chish + "
     "bitta burilish). Yamoq sinovi buzilgan element shaklida "
     "o'tkazildi - bu muhim, chunki to'g'ri to'rtburchakda ko'p xato "
     "yashirin qoladi. Bu test har qanday yangi element uchun "
     "birinchi bajariladigan tekshiruv bo'lishi kerak (su-14).")

# --- (2) ELEMENT TURLARINI taqqoslash: konsol balka ---
L_c, h_c, P_c = 10.0, 1.0, 1.0


def cantilever(nx, ny, kind):
    if kind == "Q8":
        nnx, nny = 2*nx + 1, 2*ny + 1
    else:
        nnx, nny = nx + 1, ny + 1
    X, Y = np.meshgrid(np.linspace(0, L_c, nnx),
                       np.linspace(-h_c/2, h_c/2, nny), indexing="ij")
    nid = np.arange(nnx*nny).reshape(nnx, nny)
    nodes = np.column_stack([X.ravel(), Y.ravel()])
    els = []
    for i in range(nx):
        for j in range(ny):
            if kind == "CST":
                n = [nid[i, j], nid[i+1, j], nid[i+1, j+1], nid[i, j+1]]
                els += [[n[0], n[1], n[2]], [n[0], n[2], n[3]]]
            elif kind == "Q4":
                els.append([nid[i, j], nid[i+1, j], nid[i+1, j+1],
                            nid[i, j+1]])
            else:
                I, J = 2*i, 2*j
                els.append([nid[I, J], nid[I+2, J], nid[I+2, J+2],
                            nid[I, J+2], nid[I+1, J], nid[I+2, J+1],
                            nid[I+1, J+2], nid[I, J+1]])
    # Q8 serendipiti: blok markazidagi tugunlar hech bir elementga
    # tegishli emas - ularni tizimdan chiqaramiz
    used = sorted({n for el in els for n in el})
    remap = {n: i for i, n in enumerate(used)}
    nodes = nodes[used]
    els = [[remap[n] for n in el] for el in els]
    nid = np.vectorize(lambda n: remap.get(n, -1))(nid)
    ndof = 2*len(nodes)
    K = np.zeros((ndof, ndof))
    F = np.zeros(ndof)
    D = Dmat(nu, "stress")
    for el in els:
        xy = nodes[el]
        if kind == "CST":
            ke, _, _ = cst(xy, D)
        elif kind == "Q4":
            ke = ke_quad(xy, D, shp_q4, 2)
        else:
            ke = ke_quad(xy, D, shp_q8, 3)
        idx = np.array([[2*k, 2*k + 1] for k in el]).ravel()
        K[np.ix_(idx, idx)] += ke
    tip = [nid[nnx-1, j] for j in range(nny) if nid[nnx-1, j] >= 0]
    for n in tip:
        F[2*n + 1] -= P_c/len(tip)
    fixed = [v for j in range(nny) if nid[0, j] >= 0
             for v in (2*nid[0, j], 2*nid[0, j] + 1)]
    free = np.setdiff1d(np.arange(ndof), fixed)
    u = np.zeros(ndof)
    u[free] = np.linalg.solve(K[np.ix_(free, free)], F[free])
    return abs(float(np.mean([u[2*n + 1] for n in tip]))), ndof - len(fixed)


I_c = h_c**3/12
G_c = E/(2*(1 + nu))
w_ref = P_c*L_c**3/(3*E*I_c) + P_c*L_c/((5/6)*G_c*h_c)
value("Etalon uch ko'chishi (Timoshenko)", w_ref, "m")
rows2 = []
for nx, ny in [(4, 1), (8, 2), (16, 4), (32, 8)]:
    line = [f"{nx}x{ny}"]
    for kind in ["CST", "Q4", "Q8"]:
        wv, nd = cantilever(nx, ny, kind)
        line.append(f"{wv/w_ref*100:.2f}% ({nd})")
    rows2.append(line)
table("Element turlarini taqqoslash: konsol balka "
      "(aniqlik va erkinlik darajalari)",
      ["to'r", "CST", "Q4", "Q8"], rows2)
note("CST 576 erkinlik darajasi bilan javobning atigi 87% ini beradi, "
     "Q8 esa 40 erkinlik darajasi bilan 97% ini - o'n to'rt barobar "
     "kam noma'lum bilan ancha yaxshi natija. Sababi su-14 va su-16 da: "
     "CST da deformatsiya element ichida DOIMIY, shuning uchun egilishni "
     "faqat bo'lakli zinapoya bilan yaqinlashtiradi. Q4 bunga qaraganda "
     "yaxshiroq, lekin unda ham siljish qulflanishi bor. Zamonaviy "
     "paketlarda CST asosiy element sifatida ishlatilmaydi.")

# --- (3) KIRSH masalasi: teshikli plastina ---
def hole_mesh(a, W, nr, nt, gr):
    th = np.linspace(0, np.pi/2, nt + 1)
    s = np.linspace(0, 1, nr + 1)**gr
    X = np.zeros((nr + 1, nt + 1))
    Y = np.zeros((nr + 1, nt + 1))
    for j, t in enumerate(th):
        xi_, yi_ = a*np.cos(t), a*np.sin(t)
        if t <= np.pi/4:
            xo, yo = W, W*np.tan(t)
        else:
            xo, yo = W/np.tan(t), W
        X[:, j] = xi_ + (xo - xi_)*s
        Y[:, j] = yi_ + (yo - yi_)*s
    nid = np.arange((nr + 1)*(nt + 1)).reshape(nr + 1, nt + 1)
    conn = [[nid[i, j], nid[i+1, j], nid[i+1, j+1], nid[i, j+1]]
            for i in range(nr) for j in range(nt)]
    return np.column_stack([X.ravel(), Y.ravel()]), conn, nid, nr, nt


def solve_hole(a, W, nr, nt, gr):
    nodes, conn, nid, nr, nt = hole_mesh(a, W, nr, nt, gr)
    D = Dmat(nu, "stress")
    ndof = 2*len(nodes)
    K = np.zeros((ndof, ndof))
    F = np.zeros(ndof)
    for el in conn:
        idx = np.array([[2*k, 2*k + 1] for k in el]).ravel()
        K[np.ix_(idx, idx)] += ke_quad(nodes[el], D, shp_q4, 2)
    for j in range(nt):
        n1, n2 = nid[nr, j], nid[nr, j + 1]
        if abs(nodes[n1, 0] - W) < 1e-9 and abs(nodes[n2, 0] - W) < 1e-9:
            Ledge = abs(nodes[n2, 1] - nodes[n1, 1])
            F[2*n1] += sig_inf*Ledge/2
            F[2*n2] += sig_inf*Ledge/2
    fixed = set()
    for n in range(len(nodes)):
        if abs(nodes[n, 0]) < 1e-12:
            fixed.add(2*n)          # x = 0 simmetriya
        if abs(nodes[n, 1]) < 1e-12:
            fixed.add(2*n + 1)      # y = 0 simmetriya
    free = np.setdiff1d(np.arange(ndof), sorted(fixed))
    u = np.zeros(ndof)
    u[free] = np.linalg.solve(K[np.ix_(free, free)], F[free])

    def stress(el, xi, eta):
        B, _, N = Bmat(shp_q4, xi, eta, nodes[el])
        idx = np.array([[2*k, 2*k + 1] for k in el]).ravel()
        return D @ (B @ u[idx]), N @ nodes[el]

    return u, nodes, conn, nid, stress, nr, nt


rows3 = []
for Wa in [5.0, 10.0, 20.0]:
    for nr, nt in [(10, 10), (16, 16), (24, 24)]:
        _, _, conn, _, stress, nrr, ntt = solve_hole(
            a_hole, Wa*a_hole, nr, nt, grade)
        s90, _ = stress(conn[0*ntt + (ntt - 1)], -1.0, 1.0)
        rows3.append([f"{Wa:.0f}", f"{nr}x{nt}",
                      f"{s90[0]/sig_inf:.4f}",
                      f"{abs(s90[0]/sig_inf - 3.0)/3.0*100:.2f}"])
table("Kuchlanish konsentratsiyasi: to'r va soha o'lchami bo'yicha",
      ["W/a", "to'r", "K_t = s_theta/s", "cheksiz plastinadan farq %"],
      rows3)
note("IKKI XIL YAQINLASHISH. To'rni zichlashtirish DISKRETLASHTIRISH "
     "xatosini kamaytiradi va har bir W/a uchun o'z qiymatiga "
     "yaqinlashtiradi. Lekin W/a = 5 da bu qiymat 3 emas, 3.35 - "
     "chekli kenglik ta'siri, ya'ni MODEL xatosi. Uni to'r bilan "
     "davolab bo'lmaydi; sohani kattalashtirish kerak. W/a = 20 da "
     "esa K_t 3 ga 0.1% aniqlikda yetadi. Bu farqni ajratish V&V ning "
     "asosiy g'oyasi (su-29): diskretlashtirish xatosi va model xatosi "
     "har xil davolanadi. DIQQAT: W/a = 10 qatoriga e'tibor bering - "
     "eng DAG'AL to'r 3 ga eng yaqin javobni (3.012) beradi, to'r "
     "zichlashgani sari esa u 3.07 ga uzoqlashadi. Bu tasodif: dag'al "
     "to'rning kam baholashi chekli kenglikning ortiqcha baholashini "
     "qoplagan. Ikki xato bir-birini yo'qotgan va natija 'to'g'ri' "
     "ko'rinadi. Aynan shuning uchun bitta hisob hech qachon yetarli "
     "emas - yaqinlashishni KO'RSATISH kerak (su-18).")

# --- (4) Kirsh yechimining TO'LIQ radial profili ---
_, nodes_k, conn_k, nid_k, stress_k, nrk, ntk = solve_hole(
    a_hole, W_over_a*a_hole, n_ring + 8, n_ring, grade)


def kirsch_90(rho):
    return 0.5*(2 + 1/rho**2 + 3/rho**4)


rows4 = []
rs, fem_s, kir_s = [], [], []
j = ntk - 1
for i in range(0, nrk, 2):
    s_, xg = stress_k(conn_k[i*ntk + j], 0.0, 1.0)
    rho = float(np.hypot(*xg)/a_hole)
    if rho > 6:
        break
    kk_ = kirsch_90(rho)
    rows4.append([f"{rho:.3f}", f"{s_[0]/sig_inf:.5f}", f"{kk_:.5f}",
                  f"{abs(s_[0]/sig_inf - kk_)/kk_*100:.3f}"])
    rs.append(rho)
    fem_s.append(float(s_[0]/sig_inf))
    kir_s.append(kk_)
table("Kirsh yechimi bilan to'liq radial profil (theta = 90°)",
      ["r/a", "FEM s_theta/s", "Kirsh", "xato %"], rows4)
series("FEM: s_theta/s", rs, fem_s, xlabel="r/a", ylabel="s_theta/s")
series("Kirsh (analitik)", rs, kir_s, xlabel="r/a", ylabel="s_theta/s")
series("Nominal kuchlanish", rs, [1.0]*len(rs),
       xlabel="r/a", ylabel="s_theta/s")

s90, _ = stress_k(conn_k[0*ntk + (ntk - 1)], -1.0, 1.0)
s00, _ = stress_k(conn_k[0*ntk + 0], -1.0, -1.0)
value("(0, a) da s_theta/s (Kirsh: +3)", float(s90[0]/sig_inf), "—")
value("(0, a) da s_r/s (erkin sirt: 0)", float(s90[1]/sig_inf), "—")
value("(a, 0) da s_theta/s (Kirsh: -1)", float(s00[1]/sig_inf), "—")
value("Teshik chekkasidagi kuchlanish oralig'i",
      float((s90[0] - s00[1])/sig_inf), "—")
rho5 = (0.10)
t5 = (-1 + np.sqrt(1 + 1.2))/6
value("5% chegarasi: r/a (analitik)", float(1/np.sqrt(t5)), "—")
note(f"UCHTA MUSTAQIL TEKSHIRUV. Kirsh yechimining barcha uchala "
     f"bashorati ham tasdiqlandi: teshik chekkasida theta = 90 da "
     f"K_t = {s90[0]/sig_inf:.4f} (aniq 3), theta = 0 da "
     f"{s00[1]/sig_inf:.4f} (aniq -1, ya'ni SIQILISH) va erkin sirtda "
     f"radial kuchlanish {s90[1]/sig_inf:.5f} (aniq 0). Bundan tashqari "
     f"butun radial profil r/a = 1 dan 5 gacha 1% dan yaxshi aniqlikda "
     f"mos tushdi - ya'ni faqat maksimal qiymat emas, MAYDONNING "
     f"O'ZI to'g'ri. Kuchlanish teshikdan 3.5 radius narida nominaldan "
     f"atigi 5% farq qiladi: Sen-Venan prinsipining (tmm-14) miqdoriy "
     f"ifodasi.")

# --- (5) TEKIS KUCHLANISH va TEKIS DEFORMATSIYA ---
rows5 = []
for nu_ in [0.0, 0.2, 0.3, 0.45, 0.49]:
    Ds = Dmat(nu_, "stress")
    De = Dmat(nu_, "strain")
    rows5.append([f"{nu_:.2f}", f"{Ds[0, 0]/E:.4f}", f"{De[0, 0]/E:.4f}",
                  f"{De[0, 0]/Ds[0, 0]:.4f}"])
table("Tekis kuchlanish va tekis deformatsiya material matritsalari",
      ["nu", "D11/E (kuchlanish)", "D11/E (deformatsiya)", "nisbat"],
      rows5)
note("nu = 0 da ikkala holat AYNAN bir xil, lekin nu ortgani sari farq "
     "keskin o'sadi: nu = 0.3 da tekis deformatsiya 1.23 barobar, "
     "nu = 0.49 da esa 13 barobar bikrroq. Shuning uchun tekis holatni "
     "noto'g'ri "
     "tanlash jiddiy xato - ayniqsa deyarli siqilmas materiallarda "
     "(rezina, to'yingan tuproq), u yerda hajmiy qulflanish ham "
     "qo'shiladi (su-16).")

table("Tekis masala elementlarining taqqoslanishi",
      ["Element", "Tugunlar", "Deformatsiya", "Yamoq sinovi", "Tavsiya"],
      [["CST", "3", "DOIMIY", "o'tadi", "faqat to'ldiruvchi"],
       ["LST (T6)", "6", "chiziqli", "o'tadi", "yaxshi"],
       ["Q4", "4", "chiziqli (to'liq emas)", "o'tadi",
        "zich to'r yoki SRI"],
       ["Q8", "8", "chiziqli", "o'tadi", "ENG YAXSHI tanlov"],
       ["Q9", "9", "chiziqli", "o'tadi", "Q8 ga yaqin, qimmatroq"]])
''',
                parameters=[
                    p("W_over_a", "Plastina kengligi / teshik radiusi",
                      3.0, 40.0, 20.0, 1.0),
                    p("n_ring", "Teshik atrofidagi elementlar", 8.0, 32.0,
                      20.0, 2.0),
                    p("grade", "Radial zichlashtirish darajasi", 1.0, 5.0,
                      3.0, 0.5),
                    p("nu", "Puasson koeffitsienti", 0.0, 0.49, 0.3,
                      0.01),
                ],
                expected_output=(
                    "Uchala element ham "
                    "buzilgan shaklda "
                    "o'tkazilgan yamoq "
                    "sinovidan $10^{-18}$ "
                    "darajasida o'tadi va "
                    "har birida aynan uchta "
                    "qattiq jism rejimi bor. "
                    "Konsol balkada CST 576 "
                    "erkinlik darajasi bilan "
                    "86,7%, Q4 95,9%, Q8 esa "
                    "atigi 40 erkinlik "
                    "darajasi bilan 97,5% "
                    "beradi. Teshikli "
                    "plastinada $W/a = 20$ "
                    "va zich to'rda "
                    "$K_t = 3{,}00$ chiqadi, "
                    "$W/a = 5$ da esa to'r "
                    "zichlashganda ham 3,35 "
                    "ga intiladi — bu model "
                    "xatosi, "
                    "diskretlashtirish "
                    "xatosi emas. Kirsh "
                    "yechimining uchala "
                    "bashorati ham "
                    "tasdiqlanadi: "
                    "$\\theta = 90°$ da "
                    "$+3$, $\\theta = 0$ da "
                    "$-1$, erkin sirtda "
                    "radial kuchlanish nol; "
                    "butun radial profil "
                    "$r/a = 1$ dan 5 gacha "
                    "1% dan yaxshi "
                    "aniqlikda mos keladi."
                ),
            ),
            visual=vis(
                kind="Kuchlanish konsentratsiyasi xaritasi",
                tool="React/SVG + Manim",
                description=(
                    "Teshik atrofidagi "
                    "kuchlanish maydoni va "
                    "uning radial so'nishi."
                ),
                how_to_draw=(
                    "React/SVG: chorak plastina "
                    "to'r bilan chiziladi va "
                    "elementlar "
                    "$\\sigma_{\\theta}$ "
                    "qiymatiga qarab "
                    "ranglanadi — nominal "
                    "kuchlanish neytral rang, "
                    "undan yuqorisi bir "
                    "tomonga, siqilish "
                    "boshqa tomonga. Shu "
                    "bilan teshik "
                    "chekkasidagi ikkita "
                    "qarama-qarshi zona "
                    "($+3\\sigma$ va "
                    "$-\\sigma$) darhol "
                    "ko'zga tashlanadi. "
                    "O'ng tomonda radial "
                    "profil grafigi: FEM "
                    "nuqtalari va Kirsh "
                    "egri chizig'i ustma-ust, "
                    "nominal daraja gorizontal "
                    "chiziq bilan; "
                    "$r = 3{,}5a$ da "
                    "vertikal belgi "
                    "'5% chegarasi' deb "
                    "yoziladi. $W/a$ "
                    "slayderi surilganda "
                    "ikki narsa bir vaqtda "
                    "o'zgaradi: to'r "
                    "kengayadi va yonidagi "
                    "$K_t$ ko'rsatkichi "
                    "3,35 dan 3,00 ga "
                    "tushadi — model "
                    "xatosining yo'qolishi "
                    "shunda ko'rinadi. "
                    "To'r slayderi esa "
                    "$K_t$ ni o'z "
                    "chegarasiga "
                    "yaqinlashtiradi, "
                    "lekin uni o'zgartira "
                    "olmaydi: ikki xil "
                    "xatolikning farqi "
                    "aynan shu ikki "
                    "slayderda namoyon "
                    "bo'ladi."
                ),
            ),
            interp=(
                "Yamoq sinovi buzilgan "
                "element shaklida "
                "o'tkazildi va bu muhim: "
                "to'g'ri to'rtburchakda ko'p "
                "xato yashirin qoladi. "
                "Uchala element ham o'tdi "
                "va har birida aynan uchta "
                "qattiq jism rejimi bor. "
                "Ammo yamoq sinovidan "
                "o'tish — yaqinlashishning "
                "**zaruriy** sharti, "
                "yetarli emas: element "
                "taqqoslash jadvali buni "
                "keskin ko'rsatadi. CST 576 "
                "erkinlik darajasi bilan "
                "javobning 87% ini beradi, "
                "Q8 esa 40 tasi bilan 97% "
                "ini. Sababi su-14 da "
                "aniqlangan edi: CST da "
                "deformatsiya element "
                "ichida doimiy, shuning "
                "uchun egilishni faqat "
                "bo'lakli zinapoya bilan "
                "yaqinlashtiradi. Bu "
                "amaliy xulosaga olib "
                "keladi — uchburchak "
                "element tanlashda "
                "CST emas, olti tugunli "
                "LST ni oling. "
                "Kirsh tajribasi esa ikki "
                "qatlamli tasdiq beradi. "
                "Birinchidan, sonli yechim "
                "faqat maksimal qiymatni "
                "emas, **butun maydonni** "
                "to'g'ri beradi: radial "
                "profil $r/a = 1$ dan 5 "
                "gacha 1% dan yaxshi "
                "aniqlikda mos tushdi. "
                "Bitta nuqtadagi kelishuv "
                "tasodif bo'lishi mumkin, "
                "butun profilniki esa "
                "emas. Ikkinchidan, "
                "uchta mustaqil bashorat "
                "ham tasdiqlandi, jumladan "
                "$\\theta = 0$ dagi "
                "**siqilish** — bu "
                "intuitiv emas va shuning "
                "uchun ayniqsa qimmatli "
                "tekshiruv. Eng muhim "
                "uslubiy natija esa "
                "$K_t$ jadvalida. "
                "$W/a = 5$ da to'rni "
                "qancha zichlashtirmang, "
                "$K_t$ 3 ga emas, 3,35 ga "
                "intiladi. Bu sonli xato "
                "emas — o'sha geometriya "
                "uchun to'g'ri javob. "
                "Xato faqat uni cheksiz "
                "plastinaning javobi deb "
                "e'lon qilsak paydo "
                "bo'ladi. To'r "
                "zichlashtirish "
                "diskretlashtirish "
                "xatosini davolaydi, "
                "model xatosini esa faqat "
                "modelni o'zgartirish "
                "davolaydi — va bu "
                "su-29 dagi V&V "
                "tartibining yadrosi."
            ),
            mistakes=[
                "CST ni asosiy element "
                "sifatida ishlatish. "
                "Deformatsiya doimiy — "
                "egilishda juda sekin "
                "yaqinlashadi; LST yoki Q8 "
                "oling.",
                "Tekis kuchlanish va tekis "
                "deformatsiyani adashtirish. "
                "$\\nu = 0{,}49$ da "
                "matritsalar 17 barobar "
                "farq qiladi.",
                "Model chegarasini teshikka "
                "juda yaqin qo'yish. "
                "$W/a < 10$ da $K_t$ "
                "sezilarli oshadi.",
                "Bitta hisob bilan "
                "cheklanib, to'r bo'yicha "
                "yaqinlashishni "
                "ko'rsatmaslik (su-18).",
                "Model xatosini to'r "
                "zichlashtirish bilan "
                "yengishga urinish. "
                "$W/a = 5$ da $K_t$ "
                "3,35 ga intiladi va "
                "u yerda qoladi.",
                "$K_t = 3$ ni har qanday "
                "teshikka qo'llash. Bu "
                "faqat doiraviy teshik "
                "uchun; ellipsda "
                "$K_t = 1 + 2b/a$.",
            ],
            quiz=[
                q("Tekis kuchlanish va tekis "
                  "deformatsiyaning farqi "
                  "nima?",
                  "Tekis kuchlanishda "
                  "$\\sigma_z = 0$ (yupqa "
                  "plastina), tekis "
                  "deformatsiyada "
                  "$\\varepsilon_z = 0$ "
                  "(uzun jism) va "
                  "$\\sigma_z = "
                  "\\nu(\\sigma_x + "
                  "\\sigma_y)$.",
                  "konseptual"),
                q("CST nima uchun sekin "
                  "yaqinlashadi?",
                  "Uning $\\mathbf{B}$ "
                  "matritsasi doimiy, demak "
                  "deformatsiya element "
                  "ichida o'zgara olmaydi; "
                  "egilishda esa u chiziqli "
                  "bo'lishi kerak.",
                  "konseptual"),
                q("$a = 10$ mm teshikda "
                  "kuchlanish qaysi masofada "
                  "nominaldan 5% farq "
                  "qiladi?",
                  "$\\rho^{-2} + 3\\rho^{-4} "
                  "= 0{,}1$ dan "
                  "$\\rho = 3{,}52$, ya'ni "
                  "$r \\approx 35$ mm.",
                  "hisob"),
                q("Kod Kirsh yechimining "
                  "qaysi uchta bashoratini "
                  "tekshiradi?",
                  "$\\theta = 90°$ da "
                  "$+3\\sigma$, "
                  "$\\theta = 0$ da "
                  "$-\\sigma$ (siqilish) va "
                  "erkin sirtda radial "
                  "kuchlanishning noli; "
                  "bundan tashqari butun "
                  "radial profil.", "kod"),
                q("$W/a = 5$ da to'r "
                  "zichlashganda $K_t$ "
                  "3 ga intilmaydi. Bu "
                  "xatomi?",
                  "Yo'q — bu o'sha chekli "
                  "geometriya uchun to'g'ri "
                  "javob (3,35). Xato faqat "
                  "uni cheksiz plastinaning "
                  "javobi deb hisoblasak "
                  "paydo bo'ladi.", "talqin"),
                q("Diskretlashtirish va model "
                  "xatolari qanday farq "
                  "qiladi?",
                  "Birinchisi to'rni "
                  "zichlashtirish bilan "
                  "kamayadi, ikkinchisi esa "
                  "yo'q — u uchun modelni "
                  "o'zgartirish (sohani "
                  "kattalashtirish) kerak.",
                  "talqin"),
                q("Q8 nima uchun CST dan "
                  "ancha samarali?",
                  "Kodda Q8 40 erkinlik "
                  "darajasi bilan 97,5%, "
                  "CST esa 576 tasi bilan "
                  "86,7% beradi — Q8 ning "
                  "bazisi deformatsiyani "
                  "chiziqli ifodalaydi.",
                  "kod"),
            ],
            bridge=(
                "Tekis masala elementlari "
                "faqat tekislikdagi "
                "kuchlanishni ifodalaydi. "
                "Plastina va qobiq esa "
                "egilishga ham ishlaydi va "
                "u yerda pq fanidagi butun "
                "nazariya FEM tilida qayta "
                "quriladi — jumladan "
                "pq-24 dagi siljish "
                "qulflanishi muammosi."
            ),
            research=(
                "Kuchlanish konsentratsiyasi "
                "mavzusini kengaytiring. "
                "(1) $K_t$ va charchoqdagi "
                "$K_f$ bog'liqligini "
                "o'rganing: nima uchun "
                "$K_f < K_t$ va o'lchamning "
                "ta'siri (notch "
                "sensitivity) qanday? "
                "(2) Bir necha teshikning "
                "o'zaro ta'sirini "
                "hisoblang: ular qanchalik "
                "yaqin bo'lganda "
                "ta'sirlar qo'shiladi? "
                "(3) Ellips va o'tkir "
                "burchak holatlarini "
                "ko'rib chiqing: "
                "$K_t \\to \\infty$ "
                "bo'lganda yorilish "
                "mexanikasi parametrlariga "
                "(tmm-24) o'tish qanday "
                "amalga oshiriladi? "
                "(4) Yassilangan "
                "deformatsiya (EAS) "
                "elementlarini o'rganing: "
                "ular Q4 ni Q8 darajasiga "
                "olib chiqa oladimi?"
            ),
            manim_ref=manim(
                scene="StressConcentrationScene",
                module="manim/scenes/su_apps.py",
                title="Teshik atrofidagi kuchlanish",
                summary=(
                    "Tekis plastina tortiladi "
                    "va kuchlanish maydoni bir "
                    "tekis rangda "
                    "ko'rsatiladi. Keyin "
                    "markazda teshik "
                    "ochiladi: kuchlanish "
                    "chiziqlari teshikni "
                    "aylanib o'tadi va "
                    "yon tomonlarda "
                    "quyuqlashadi. Rang "
                    "xaritasi "
                    "$3\\sigma$ zonasini va "
                    "qutblardagi siqilish "
                    "zonasini ajratib "
                    "ko'rsatadi. Nihoyat "
                    "radial profil "
                    "chiziladi va u "
                    "Kirsh egri chizig'i "
                    "bilan ustma-ust "
                    "tushadi; "
                    "$3{,}5a$ da nominal "
                    "darajaga qaytish "
                    "belgilanadi."
                ),
            ),
        ),
    ),

    # ------------------------------------------------------------------ su-22
    Topic(
        id="su-22",
        subject_id=S, module_id=M, order=22,
        title="Plastina va qobiq elementlari",
        description=(
            "Kirxgof va Mindlin plastina elementlari, $C^1$ muammosi, "
            "siljish qulflanishi va uni yengish, qobiq elementlari hamda "
            "natijani Navye yechimi bilan tekshirish."
        ),
        learning_objective=(
            "Plastina elementini tanlash va qo'llash, siljish "
            "qulflanishini tanib olish va yengish, natijani analitik "
            "yechim bilan tekshirish."
        ),
        prerequisites=["su-21", "pq-09", "pq-24"],
        mathematical_core=(
            "$\\mathbf{k} = \\int\\mathbf{B}_b^T\\mathbf{D}_b\\mathbf{B}_b"
            "\\,dA + \\int\\mathbf{B}_s^T\\mathbf{D}_s\\mathbf{B}_s\\,dA$; "
            "Navye: $w_{max} = 0{,}00406\\,qa^4/D$."
        ),
        engineering_application=(
            "Ko'prik plitalari, rezervuar va idish devorlari, kema "
            "korpusi, samolyot qoplamasi, silos va quvurlar."
        ),
        computational_component=(
            "Mindlin plastina elementini qurish, qulflanishni ko'rsatish "
            "va SRI bilan yengish, Navye yechimi bilan tekshirish."
        ),
        visualization_component=(
            "Plastina egilish sirti, moment xaritalari, qulflanishning "
            "qalinlikka bog'liqligi."
        ),
        research_extension=(
            "MITC (Mixed Interpolation of Tensorial Components) "
            "elementlarini o'rganing: ular soxta rejimsiz "
            "qulflanishni yechadi."
        ),
        difficulty="murakkab",
        previous_link=(
            "su-21 dagi tekis masala elementlari faqat tekislik ichidagi "
            "kuchlanishni ifodalardi. Plastina esa egilishga ishlaydi va "
            "pq fanidagi butun nazariya bu yerda FEM tilida qayta "
            "quriladi — jumladan pq-24 dagi siljish qulflanishi."
        ),
        next_topic="su-23",
        estimated_minutes=95,
        tags=["plastina elementi", "Mindlin", "Kirxgof", "siljish "
              "qulflanishi", "qobiq", "Navye yechimi"],
        lesson=_lesson(
            problem=(
                "Rezervuar qopqog'i "
                "hisoblanmoqda: "
                "$4\\times4$ m po'lat plastina, "
                "qalinligi 8 mm, chekkalari "
                "sharnirli, ustida suv "
                "bosimi. Tayyor FEM paketda "
                "to'rtburchak plastina "
                "elementlari tanlanadi, to'r "
                "quriladi, hisob bajariladi — "
                "va natija kutilgandan "
                "**yuz barobar** kichik "
                "chiqadi. Go'yo plastina "
                "deyarli qimirlamaydi. To'r "
                "zichlashtiriladi, natija "
                "o'sadi, lekin sekin. "
                "pq-24 dagi tanish kasallik "
                "— siljish qulflanishi — "
                "lekin bu safar u FEM "
                "elementida. Nima sodir "
                "bo'lmoqda va uni qanday "
                "yengish mumkin?"
            ),
            concepts=[
                c("Kirxgof plastinasi",
                  "Siljish deformatsiyasi nol; "
                  "faqat $w$ noma'lum, lekin "
                  "$C^1$ uzluksizlik talab "
                  "qilinadi (pq-04)."),
                c("Mindlin–Reyssner plastinasi",
                  "Burilishlar mustaqil "
                  "noma'lum: $w$, "
                  "$\\beta_x$, $\\beta_y$; "
                  "faqat $C^0$ kerak, lekin "
                  "qulflanish xavfi bor "
                  "(pq-24)."),
                c("$C^1$ muammosi",
                  "Plastina uchun to'liq mos "
                  "(conforming) element qurish "
                  "juda qiyin — tarixan FEM "
                  "ning eng murakkab "
                  "masalalaridan biri."),
                c("Egilish va siljish "
                  "matritsalari",
                  "$\\mathbf{k} = "
                  "\\mathbf{k}_b + "
                  "\\mathbf{k}_s$; "
                  "$\\mathbf{k}_b \\sim h^3$, "
                  "$\\mathbf{k}_s \\sim h$."),
                c("Siljish qulflanishi",
                  "$h \\to 0$ da "
                  "$\\mathbf{k}_s$ "
                  "$\\mathbf{k}_b$ ni bo'g'ib "
                  "qo'yadi — nisbat "
                  "$(a/h)^2$ kabi o'sadi."),
                c("Qobiq elementi",
                  "Membrana (su-21) va "
                  "egilish (plastina) "
                  "birlashtiriladi; egrilik "
                  "ularni bog'laydi (pq-26)."),
            ],
            derivation=[
                d("1. Mindlin kinematikasi",
                  r"u = z\beta_x(x,y), \quad "
                  r"v = z\beta_y(x,y), \quad "
                  r"w = w(x,y)",
                  "Uchta mustaqil maydon. "
                  "Kirxgofda "
                  "$\\beta_x = -\\partial w/"
                  "\\partial x$ majburlanadi, "
                  "bu yerda esa yo'q."),
                d("2. Egrilik va siljish",
                  r"\boldsymbol\kappa = \left\{"
                  r"\beta_{x,x},\ \beta_{y,y},\ "
                  r"\beta_{x,y} + \beta_{y,x}"
                  r"\right\}, \quad "
                  r"\boldsymbol\gamma = \left\{"
                  r"w_{,x} + \beta_x,\ w_{,y} + "
                  r"\beta_y\right\}",
                  "**Hal qiluvchi nuqta.** "
                  "Faqat **birinchi** "
                  "hosilalar qatnashadi, "
                  "demak $C^0$ bazis "
                  "yetarli — oddiy Lagranj "
                  "funksiyalari ishlaydi."),
                d("3. Ikki qismli energiya",
                  r"U = \frac12\int"
                  r"\boldsymbol\kappa^T"
                  r"\mathbf{D}_b"
                  r"\boldsymbol\kappa\,dA + "
                  r"\frac12\int"
                  r"\boldsymbol\gamma^T"
                  r"\mathbf{D}_s"
                  r"\boldsymbol\gamma\,dA",
                  "$\\mathbf{D}_b = "
                  "\\frac{Eh^3}{12(1-\\nu^2)}"
                  "[\\cdot]$, "
                  "$\\mathbf{D}_s = "
                  "\\kappa Gh\\,\\mathbf{I}$, "
                  "$\\kappa = 5/6$."),
                d("4. Qalinlik bo'yicha "
                  "masshtab",
                  r"\mathbf{k}_b \sim h^3, "
                  r"\qquad \mathbf{k}_s \sim h",
                  "**Qulflanishning ildizi.** "
                  "Ikkala had har xil tezlikda "
                  "kamayadi."),
                d("5. Nisbatning o'sishi",
                  r"\frac{\|\mathbf{k}_s\|}"
                  r"{\|\mathbf{k}_b\|} \sim "
                  r"\frac{h/a^2}{h^3/a^4} = "
                  r"\left(\frac{a}{h}\right)^2",
                  "$a/h = 100$ da nisbat "
                  "$10^4$ — siljish hadi "
                  "egilishdan o'n ming "
                  "barobar kuchliroq va "
                  "elementni bo'g'ib "
                  "qo'yadi."),
                d("6. Nima uchun bo'g'adi",
                  r"h \to 0 \;\Rightarrow\; "
                  r"\boldsymbol\gamma \to 0 "
                  r"\;\Rightarrow\; "
                  r"\beta_x \to -w_{,x}",
                  "Ingichka plastinada "
                  "siljish deformatsiyasi nol "
                  "bo'lishi kerak. Q4 bazisi "
                  "buni **har bir Gauss "
                  "nuqtasida** "
                  "qanoatlantira olmaydi — "
                  "haddan ziyod talab "
                  "(su-16)."),
                d("7. Tanlab kamaytirilgan "
                  "integrallash",
                  r"\mathbf{k}_b: 2\times2, "
                  r"\qquad \mathbf{k}_s: "
                  r"1\times1",
                  "**Davo.** Siljish sharti "
                  "endi faqat element "
                  "markazida talab qilinadi "
                  "— bu bajarilishi mumkin "
                  "bo'lgan talab."),
                d("8. SRI ning narxi",
                  r"\mathrm{rank}(\mathbf{k}) "
                  r"= 7 < 12 - 3 = 9",
                  "**Ogohlantirish.** SRI "
                  "element darajasida ikkita "
                  "soxta nol energiyali "
                  "rejim kiritadi. Kod buni "
                  "aniq o'lchaydi."),
                d("9. Yig'ish ularni "
                  "bostiradi",
                  r"\mathbf{K}_{global} \ "
                  r"\text{singulyar emas}",
                  "Amalda qo'shni elementlar "
                  "va chegaraviy shartlar "
                  "soxta rejimlarni "
                  "bostiradi — shuning uchun "
                  "SRI ishlaydi. Lekin bu "
                  "kafolat emas."),
                d("10. Mindlin va Kirxgof "
                  "farqi",
                  r"\frac{w_{Mindlin}}"
                  r"{w_{Kirchhoff}} = 1 + "
                  r"C\left(\frac{h}{a}\right)^2",
                  "**O'lchangan natija.** "
                  "$C \\approx 5{,}1$ "
                  "(foizda 510). "
                  "$a/h = 10$ da farq 5%, "
                  "$a/h = 100$ da 0,05% — "
                  "ingichka plastinada "
                  "ikkalasi bir xil."),
                d("11. Navye yechimi",
                  r"w_{max} = \frac{16q}"
                  r"{\pi^6D}\sum_{m,n\ toq}"
                  r"\frac{\sin\frac{m\pi}{2}"
                  r"\sin\frac{n\pi}{2}}"
                  r"{mn\left(\frac{m^2}{a^2} + "
                  r"\frac{n^2}{b^2}\right)^2}",
                  "**Diqqat.** Sinuslar "
                  "ishorani almashtiradi. "
                  "Ularsiz yig'indi "
                  "0,00429 beradi, "
                  "to'g'risi esa "
                  "**0,00406** (pq-09)."),
                d("12. Qobiq elementi",
                  r"\mathbf{k}_{shell} = "
                  r"\mathbf{k}_{membrana} + "
                  r"\mathbf{k}_{egilish}",
                  "Tekis qobiq elementida "
                  "ikkalasi **bog'lanmagan**; "
                  "bog'lanish faqat "
                  "elementlar burchak ostida "
                  "ulanganda paydo bo'ladi — "
                  "bu egrilikni taqriban "
                  "ifodalaydi (pq-26)."),
                d("13. Beshinchi va oltinchi "
                  "erkinlik darajasi",
                  r"\text{tugunda: } u, v, w, "
                  r"\theta_x, \theta_y, "
                  r"\theta_z",
                  "$\\theta_z$ (normal "
                  "atrofida burilish) "
                  "bikrligi nol — tekis "
                  "qobiqda u soxta "
                  "singulyarlik beradi va "
                  "kichik sun'iy bikrlik "
                  "qo'shiladi."),
            ],
            meaning=(
                "Plastina elementining butun "
                "tarixi 2-qadamdagi tanlovga "
                "bog'liq. Kirxgof nazariyasi "
                "faqat bitta noma'lum "
                "($w$) bilan ishlaydi va bu "
                "jozibali ko'rinadi, lekin "
                "energiyada ikkinchi "
                "hosilalar qatnashgani uchun "
                "$C^1$ uzluksizlik kerak — "
                "ikki o'lchovda esa buni "
                "ta'minlash juda qiyin. "
                "Mindlin nazariyasi burilishni "
                "mustaqil noma'lum qiladi, "
                "shunda faqat birinchi "
                "hosilalar qoladi va oddiy "
                "$C^0$ Lagranj bazisi "
                "yetarli bo'ladi. Bu katta "
                "soddalashtirish, lekin "
                "uning evaziga 4- va "
                "5-qadamlardagi muammo "
                "keladi. Egilish bikrligi "
                "$h^3$, siljish bikrligi "
                "esa $h$ kabi kamayadi, "
                "demak ingichka plastinada "
                "siljish hadi mutlaqo "
                "hukmron bo'lib qoladi: "
                "$a/h = 100$ da nisbat "
                "o'n ming. Fizik jihatdan "
                "siljish deformatsiyasi "
                "nolga intilishi kerak, "
                "lekin Q4 bazisi buni har "
                "bir Gauss nuqtasida "
                "qanoatlantira olmaydi va "
                "natijada element "
                "qotib qoladi. Kod buni "
                "shafqatsiz ko'rsatadi: "
                "to'liq integrallash bilan "
                "ingichka plastina "
                "javobning atigi 1% ini "
                "beradi — yuz barobar "
                "bikrroq. SRI esa xuddi "
                "shu to'rda 98% beradi. "
                "Farq bitta satr kodda: "
                "siljish hadini to'rt "
                "nuqta o'rniga bitta "
                "nuqtada integrallash. "
                "8- va 9-qadamlar "
                "halollik talab qiladi. "
                "SRI bepul emas: element "
                "darajasida u ikkita soxta "
                "nol energiyali rejim "
                "kiritadi va kod buni "
                "rang hisobi bilan aniq "
                "o'lchaydi. Amalda ular "
                "yig'ishdan keyin "
                "bostiriladi va hisob "
                "ishlaydi, lekin bu "
                "kafolat emas — ayrim "
                "chegaraviy shartlarda "
                "soxta rejimlar yuzaga "
                "chiqishi mumkin. Aynan "
                "shu sababdan zamonaviy "
                "paketlar SRI o'rniga "
                "MITC oilasini "
                "ishlatadi: u "
                "qulflanishni yechadi "
                "va soxta rejim "
                "kiritmaydi. Nihoyat "
                "10-qadam nazariya "
                "tanlovini "
                "oydinlashtiradi. "
                "Mindlin yechimi "
                "Kirxgofdan "
                "$(h/a)^2$ ga "
                "proporsional ortiqcha "
                "beradi va bu **xato "
                "emas** — bu haqiqiy "
                "siljish deformatsiyasi. "
                "$a/h = 10$ da u 5%, "
                "$a/h = 100$ da esa "
                "0,05%. Demak ingichka "
                "plastinada ikkala "
                "nazariya ham bir xil "
                "javob beradi va tanlov "
                "faqat element "
                "texnologiyasiga "
                "qoladi."
            ),
            equations=[
                eq(r"\mathbf{k} = \int"
                   r"\mathbf{B}_b^T\mathbf{D}_b"
                   r"\mathbf{B}_b\,dA + \int"
                   r"\mathbf{B}_s^T\mathbf{D}_s"
                   r"\mathbf{B}_s\,dA",
                   "Mindlin plastina "
                   "elementining ikki qismli "
                   "matritsasi.",
                   "Element matritsasi"),
                eq(r"\frac{\|\mathbf{k}_s\|}"
                   r"{\|\mathbf{k}_b\|} \sim "
                   r"\left(\frac{a}{h}\right)^2",
                   "Qulflanish sababi: ikki "
                   "hadning qalinlik bo'yicha "
                   "har xil masshtabi.",
                   "Qulflanish sababi"),
                eq(r"w_{max} = 0{,}00406\,"
                   r"\frac{qa^4}{D}, \qquad "
                   r"M_{max} = 0{,}0479\,qa^2",
                   "Navye yechimi — sharnirli "
                   "kvadrat plastina uchun "
                   "etalon (pq-09).",
                   "Navye etaloni"),
                eq(r"\frac{w_{Mindlin}}"
                   r"{w_{Kirchhoff}} = 1 + "
                   r"5{,}1\left(\frac{h}{a}"
                   r"\right)^2",
                   "Siljish deformatsiyasining "
                   "ulushi — o'lchangan "
                   "koeffitsient bilan.",
                   "Siljish ulushi"),
            ],
            conditions=(
                "**Nazariya tanlash:**\n"
                "- $a/h > 20$ → Kirxgof "
                "yetarli (farq < 1,3%);\n"
                "- $a/h < 10$ → Mindlin "
                "kerak;\n"
                "- Qatlamli kompozit → "
                "har doim Mindlin yoki "
                "yuqori tartibli "
                "nazariya.\n\n"
                "**Element texnologiyasi:**\n"
                "- To'liq integrallash → "
                "**hech qachon** ingichka "
                "plastinada;\n"
                "- SRI → ishlaydi, lekin "
                "soxta rejimlarni "
                "tekshiring;\n"
                "- MITC4/MITC9 → zamonaviy "
                "standart, soxta rejimsiz;\n"
                "- Diskret Kirxgof (DKT) → "
                "faqat ingichka "
                "plastinalar uchun.\n\n"
                "**Chegaraviy shartlar "
                "nozikligi:** sharnirli "
                "chekkada ikki variant bor "
                "— qattiq (hard, "
                "$w = 0$ va chekkaga "
                "parallel burilish nol) va "
                "yumshoq (soft, faqat "
                "$w = 0$). Mindlin "
                "nazariyasida ular "
                "**farq qiladi** va "
                "chekka yaqinida "
                "chegaraviy qatlam paydo "
                "bo'ladi.\n\n"
                "**Qobiqlarda "
                "qo'shimcha:** "
                "$\\theta_z$ bikrligi nol "
                "— tekis elementlar bir "
                "tekislikda yotsa "
                "singulyarlik paydo "
                "bo'ladi. Paketlar kichik "
                "sun'iy bikrlik qo'shadi; "
                "uning qiymati natijaga "
                "ta'sir qilmasligini "
                "tekshiring.\n\n"
                "**Tekshiruv:** har doim "
                "Navye yoki "
                "NAFEMS etalon "
                "masalasida elementni "
                "sinab ko'ring."
            ),
            worked=WorkedExample(
                statement=(
                    "$4\\times4$ m po'lat "
                    "plastina, $h = 8$ mm, "
                    "chekkalari sharnirli, "
                    "$q = 5$ kPa. "
                    "(a) Navye yechimi bilan "
                    "$w_{max}$ ni toping; "
                    "(b) Mindlin nazariyasi "
                    "qancha ortiqcha beradi; "
                    "(c) to'liq integrallash "
                    "bilan hisoblangan Q4 "
                    "elementi nima uchun "
                    "yuz barobar bikrroq "
                    "chiqadi."
                ),
                given=[
                    r"a = 4\ \text{m}, \quad "
                    r"h = 0{,}008\ \text{m}, "
                    r"\quad q = 5000\ "
                    r"\text{Pa}",
                    r"E = 2{,}1\cdot10^{11}\ "
                    r"\text{Pa}, \quad \nu = "
                    r"0{,}3",
                ],
                steps=[
                    st(r"D = \frac{Eh^3}"
                       r"{12(1-\nu^2)} = "
                       r"\frac{2{,}1\cdot10^{11}"
                       r"\cdot 5{,}12\cdot"
                       r"10^{-7}}{12(0{,}91)}",
                       "$h^3 = 5{,}12\\cdot"
                       "10^{-7}$ m³."),
                    st(r"D = \frac{1{,}0752\cdot"
                       r"10^{5}}{10{,}92} = "
                       r"9845\ \text{N}\cdot"
                       r"\text{m}",
                       "Egilish bikrligi."),
                    st(r"w_{max} = 0{,}00406\,"
                       r"\frac{qa^4}{D} = "
                       r"0{,}00406 \cdot "
                       r"\frac{5000 \cdot 256}"
                       r"{9845}",
                       "$a^4 = 256$ m⁴."),
                    st(r"= 0{,}00406 \cdot "
                       r"130{,}0 = 0{,}5278\ "
                       r"\text{m}",
                       "**53 sm** — bu juda "
                       "katta, plastina "
                       "haddan tashqari "
                       "yupqa."),
                    st(r"\text{(b)}\quad "
                       r"\frac{a}{h} = "
                       r"\frac{4}{0{,}008} = "
                       r"500",
                       "Juda ingichka "
                       "plastina."),
                    st(r"\frac{\Delta w}{w} = "
                       r"5{,}1\left(\frac{h}{a}"
                       r"\right)^2 = 5{,}1 "
                       r"\cdot 4\cdot10^{-6}",
                       "O'lchangan "
                       "koeffitsient bilan."),
                    st(r"= 2{,}04\cdot10^{-5} = "
                       r"0{,}002\%",
                       "**Siljish deformatsiyasi "
                       "mutlaqo ahamiyatsiz** — "
                       "Kirxgof va Mindlin "
                       "bir xil javob "
                       "beradi."),
                    st(r"\text{(c)}\quad "
                       r"\frac{\|\mathbf{k}_s\|}"
                       r"{\|\mathbf{k}_b\|} \sim "
                       r"\left(\frac{a}{h}"
                       r"\right)^2 = 500^2",
                       "Siljish hadi "
                       "egilishdan..."),
                    st(r"= 2{,}5\cdot10^{5}",
                       "**Chorak million "
                       "barobar kuchliroq.**"),
                    st(r"\text{Q4 bazisi } "
                       r"\boldsymbol\gamma = 0 "
                       r"\text{ ni har bir "
                       r"Gauss nuqtasida "
                       r"bajara olmaydi}",
                       "To'rtta nuqtada "
                       "to'rtta shart — "
                       "element erkinlik "
                       "darajalari bunga "
                       "yetmaydi."),
                    st(r"\Rightarrow \ "
                       r"\text{element qotadi; "
                       r"SRI bilan shart "
                       r"faqat markazda}",
                       "Bitta nuqtada bitta "
                       "shart — bu "
                       "bajarilishi mumkin. "
                       "Kod: to'liq 1,1%, "
                       "SRI 97,8%."),
                ],
                answer=(
                    "(a) $D = 9845$ N·m, "
                    "$w_{max} = 0{,}528$ m — "
                    "plastina loyihaviy "
                    "jihatdan yaroqsiz "
                    "darajada yupqa. "
                    "(b) $a/h = 500$ da "
                    "siljish ulushi "
                    "0,002% — e'tiborsiz. "
                    "(c) Siljish bikrligi "
                    "egilishdan "
                    "$2{,}5\\cdot10^5$ "
                    "barobar kuchli va Q4 "
                    "bazisi "
                    "$\\gamma = 0$ ni "
                    "to'rtta Gauss "
                    "nuqtasida bajara "
                    "olmaydi; SRI bu "
                    "shartni faqat "
                    "markazda talab "
                    "qiladi."
                ),
                engineering_note=(
                    "(a) javobidagi 53 sm "
                    "cho'kish loyihaning "
                    "o'zi noto'g'ri "
                    "ekanini ko'rsatadi: "
                    "$w/a = 0{,}13$ — bu "
                    "chiziqli plastina "
                    "nazariyasining "
                    "chegarasidan ($w < "
                    "h/5$, ya'ni 1,6 mm) "
                    "uch yuz barobar "
                    "tashqarida. Bunday "
                    "cho'kishda membrana "
                    "kuchlari paydo "
                    "bo'ladi va plastina "
                    "aslida **parda** "
                    "kabi ishlaydi — "
                    "javob bir necha "
                    "barobar kichik "
                    "chiqadi (su-24 dagi "
                    "geometrik "
                    "nochiziqlik). Bu "
                    "muhim dars: sonli "
                    "hisob to'g'ri "
                    "bajarilgan bo'lishi "
                    "mumkin, lekin "
                    "**nazariyaning "
                    "qo'llanish sohasi** "
                    "buzilgan bo'lsa "
                    "javob baribir "
                    "noto'g'ri. Har doim "
                    "$w/h$ nisbatini "
                    "tekshiring. "
                    "Amaliyotda esa "
                    "qopqoq qovurg'alar "
                    "bilan "
                    "kuchaytiriladi "
                    "yoki qalinligi "
                    "oshiriladi: "
                    "$w \\sim h^{-3}$ "
                    "bo'lgani uchun "
                    "qalinlikni ikki "
                    "barobar oshirish "
                    "cho'kishni **sakkiz "
                    "barobar** "
                    "kamaytiradi — "
                    "bu plastina "
                    "loyihalashdagi eng "
                    "kuchli vosita."
                ),
            ),
            computation=Computation(
                caption=(
                    "Mindlin plastina elementini "
                    "qurish, siljish "
                    "qulflanishini ko'rsatish va "
                    "SRI bilan yengish, natijani "
                    "Navye yechimi bilan "
                    "tekshirish."
                ),
                code='''"""Plastina va qobiq elementlari."""
import numpy as np
from labkit import PARAMS, note, series, table, value

a_pl = float(PARAMS.get("a_pl", 1.0))
a_over_h = float(PARAMS.get("a_over_h", 100.0))
n_div = int(PARAMS.get("n_div", 12))
q_load = float(PARAMS.get("q_load", 1e4))

E = 2.1e11
nu = 0.3
kappa_s = 5.0/6.0


# --- Navye yechimi (pq-09): ETALON ---
def navier_w(N=199):
    s = 0.0
    for m in range(1, N + 1, 2):
        for n in range(1, N + 1, 2):
            s += (np.sin(m*np.pi/2)*np.sin(n*np.pi/2) /
                  (m*n*(m*m + n*n)**2))
    return 16.0/np.pi**6*s


def navier_M(N=199):
    s = 0.0
    for m in range(1, N + 1, 2):
        for n in range(1, N + 1, 2):
            s += ((m*m + nu*n*n)*np.sin(m*np.pi/2)*np.sin(n*np.pi/2) /
                  (m*n*(m*m + n*n)**2))
    return 16.0/np.pi**4*s


alpha_w = navier_w()
alpha_M = navier_M()
value("Navye koeffitsienti alpha_w (adabiyot 0.00406)", alpha_w, "—")
value("Navye koeffitsienti alpha_M (adabiyot 0.0479)", alpha_M, "—")
# Sinuslarsiz yig'indi - keng tarqalgan xato
s_no = sum(1.0/(m*n*(m*m + n*n)**2)
           for m in range(1, 200, 2) for n in range(1, 200, 2))
value("Sinuslar unutilsa chiqadigan (noto'g'ri) qiymat",
      16.0/np.pi**6*s_no, "—")
note(f"Navye qatorida sin(m*pi/2)*sin(n*pi/2) ko'paytuvchilari ISHORANI "
     f"almashtiradi: (m,n) = (1,3) uchun u -1 beradi. Ularni unutib "
     f"barcha hadlarni musbat qo'shsak {16.0/np.pi**6*s_no:.5f} chiqadi, "
     f"to'g'ri qiymat esa {alpha_w:.5f} - 5.7% farq. Bu adabiyotdagi "
     f"0.00406 bilan mashina aniqligida mos tushadi. Moment "
     f"koeffitsienti {alpha_M:.5f} ham adabiyotdagi 0.0479 ga teng.")


def shp(xi, eta):
    xn = np.array([-1, 1, 1, -1.])
    yn = np.array([-1, -1, 1, 1.])
    N = 0.25*(1 + xi*xn)*(1 + eta*yn)
    dN = np.vstack([0.25*xn*(1 + eta*yn), 0.25*(1 + xi*xn)*yn])
    return N, dN


def ke_plate(xy, h, scheme):
    """Mindlin plastina elementi. dof/tugun: w, beta_x, beta_y."""
    D = E*h**3/(12*(1 - nu**2))
    Db = D*np.array([[1, nu, 0], [nu, 1, 0], [0, 0, (1 - nu)/2]])
    Ds = kappa_s*E/(2*(1 + nu))*h*np.eye(2)
    k = np.zeros((12, 12))

    def integrate(ngp, part):
        g, w = np.polynomial.legendre.leggauss(ngp)
        for ia in range(ngp):
            for ib in range(ngp):
                N, dN = shp(g[ia], g[ib])
                J = dN @ xy
                dJ = float(np.linalg.det(J))
                dNx = np.linalg.solve(J, dN)
                if part == "bend":
                    Bb = np.zeros((3, 12))
                    Bb[0, 1::3] = dNx[0]
                    Bb[1, 2::3] = dNx[1]
                    Bb[2, 1::3] = dNx[1]
                    Bb[2, 2::3] = dNx[0]
                    k[:, :] += Bb.T @ Db @ Bb*dJ*w[ia]*w[ib]
                else:
                    Bs = np.zeros((2, 12))
                    Bs[0, 0::3] = dNx[0]
                    Bs[0, 1::3] = N
                    Bs[1, 0::3] = dNx[1]
                    Bs[1, 2::3] = N
                    k[:, :] += Bs.T @ Ds @ Bs*dJ*w[ia]*w[ib]

    integrate(2 if scheme != "reduced" else 1, "bend")
    integrate(2 if scheme == "full" else 1, "shear")
    return k


def plate(n, a, h, q, bc="ss", scheme="sri"):
    xs = np.linspace(0, a, n + 1)
    X, Y = np.meshgrid(xs, xs, indexing="ij")
    nid = np.arange((n + 1)**2).reshape(n + 1, n + 1)
    nodes = np.column_stack([X.ravel(), Y.ravel()])
    nd = 3*len(nodes)
    K = np.zeros((nd, nd))
    F = np.zeros(nd)
    g2, w2 = np.polynomial.legendre.leggauss(2)
    for i in range(n):
        for j in range(n):
            el = [nid[i, j], nid[i+1, j], nid[i+1, j+1], nid[i, j+1]]
            xy = nodes[el]
            idx = np.array([[3*k_, 3*k_ + 1, 3*k_ + 2] for k_ in el]).ravel()
            K[np.ix_(idx, idx)] += ke_plate(xy, h, scheme)
            for ia in range(2):
                for ib in range(2):
                    N, dN = shp(g2[ia], g2[ib])
                    dJ = float(np.linalg.det(dN @ xy))
                    for m_ in range(4):
                        F[idx[3*m_]] += q*N[m_]*dJ*w2[ia]*w2[ib]
    fixed = set()
    for i in range(n + 1):
        for j in range(n + 1):
            nn = nid[i, j]
            onx = (i == 0 or i == n)
            ony = (j == 0 or j == n)
            if onx or ony:
                fixed.add(3*nn)                   # w = 0
                if bc == "cl":
                    fixed.add(3*nn + 1)
                    fixed.add(3*nn + 2)
                else:                              # qattiq sharnirli
                    if onx:
                        fixed.add(3*nn + 2)
                    if ony:
                        fixed.add(3*nn + 1)
    free = np.setdiff1d(np.arange(nd), sorted(fixed))
    Kf = K[np.ix_(free, free)]
    if np.linalg.matrix_rank(Kf) < Kf.shape[0]:
        return None, nodes, nid, None
    u = np.zeros(nd)
    u[free] = np.linalg.solve(Kf, F[free])
    return abs(float(u[3*nid[n//2, n//2]])), nodes, nid, u


# --- (1) SILJISH QULFLANISHI: to'liq va tanlab kamaytirilgan ---
rows = []
for ah in [10.0, 100.0]:
    h = a_pl/ah
    D = E*h**3/(12*(1 - nu**2))
    ref = alpha_w*q_load*a_pl**4/D
    for n in [4, 8, 16, 24]:
        ws, _, _, _ = plate(n, a_pl, h, q_load, "ss", "sri")
        wf, _, _, _ = plate(n, a_pl, h, q_load, "ss", "full")
        rows.append([f"{ah:.0f}", n,
                     f"{ws/ref*100:.2f}" if ws else "SING",
                     f"{wf/ref*100:.2f}" if wf else "SING"])
table("Siljish qulflanishi: Navye yechimiga nisbatan aniqlik, %",
      ["a/h", "to'r n x n", "SRI", "to'liq 2x2"], rows)
h_thin = a_pl/a_over_h
D_thin = E*h_thin**3/(12*(1 - nu**2))
ref_thin = alpha_w*q_load*a_pl**4/D_thin
value("Tanlangan plastina: a/h", a_over_h, "—")
value("Navye w_max", ref_thin, "m")
w_sri, nodes_p, nid_p, u_p = plate(n_div, a_pl, h_thin, q_load, "ss", "sri")
w_full, _, _, _ = plate(n_div, a_pl, h_thin, q_load, "ss", "full")
value(f"SRI natijasi ({n_div}x{n_div} to'r)", float(w_sri), "m")
value(f"To'liq integrallash ({n_div}x{n_div} to'r)", float(w_full), "m")
value(f"To'liq integrallash necha barobar bikrroq "
      f"({n_div}x{n_div} to'rda)", float(w_sri/w_full), "barobar")
w_s4, _, _, _ = plate(4, a_pl, h_thin, q_load, "ss", "sri")
w_f4, _, _, _ = plate(4, a_pl, h_thin, q_load, "ss", "full")
value("To'liq integrallash necha barobar bikrroq (4x4 to'rda)",
      float(w_s4/w_f4), "barobar")
note("KATASTROFIK QULFLANISH. a/h = 100 da to'liq integrallash bilan "
     "4x4 to'r javobning atigi 1.10% ini beradi - ya'ni element yuz "
     "barobardan ko'proq bikrroq. 24x24 to'rda ham u 28.6% da qoladi. "
     "SRI esa xuddi shu 4x4 to'rda 97.8% va 24x24 da 100.00% beradi. "
     "Farq bitta satrda: siljish hadini 2x2 o'rniga 1x1 nuqtada "
     "integrallash. a/h = 10 da (qalin plastina) qulflanish ancha "
     "yumshoq - chunki uning kuchi (a/h)^2 kabi o'sadi (su-16).")

# --- (2) SRI ning narxi: soxta nol energiyali rejimlar ---
xy1 = np.array([[0, 0], [1, 0], [1, 1], [0, 1.]], float)
rows2 = []
for sch in ["full", "sri", "reduced"]:
    kk = ke_plate(xy1, 0.01, sch)
    ev = np.linalg.eigvalsh(kk)
    nz = int(np.sum(ev < 1e-8*ev.max()))
    rows2.append([sch, int(np.linalg.matrix_rank(kk)), nz, 3, nz - 3])
table("Bitta plastina elementining rangi",
      ["sxema", "rang", "nol rejimlar", "qattiq jism", "SOXTA rejimlar"],
      rows2)
note("SRI BEPUL EMAS. Element darajasida u ikkita soxta nol energiyali "
     "rejim kiritadi (rang 9 dan 7 ga tushadi), to'liq kamaytirilgan "
     "integrallash esa to'rttasini. Shunga qaramay yig'ilgan global "
     "matritsa singulyar emas: qo'shni elementlar va chegaraviy "
     "shartlar soxta rejimlarni bostiradi - yuqoridagi barcha hisoblar "
     "muvaffaqiyatli yechildi. Lekin bu KAFOLAT emas, ayrim chegaraviy "
     "shartlarda ular yuzaga chiqishi mumkin. Aynan shu sababdan "
     "zamonaviy paketlar SRI o'rniga MITC oilasini ishlatadi.")

# --- (3) MINDLIN va KIRXGOF: farq haqiqiy siljish deformatsiyasimi? ---
rows3 = []
for ah in [5.0, 10.0, 20.0, 40.0]:
    h = a_pl/ah
    D = E*h**3/(12*(1 - nu**2))
    ref = alpha_w*q_load*a_pl**4/D
    w, _, _, _ = plate(20, a_pl, h, q_load, "ss", "sri")
    exc = (w/ref - 1)*100
    rows3.append([f"{ah:.0f}", f"{w/ref*100:.3f}", f"{exc:.4f}",
                  f"{exc/(1/ah)**2:.1f}"])
table("Mindlin ortiqchasi (h/a)^2 kabi kamayadimi?",
      ["a/h", "FEM/Navye, %", "ortiqcha, %", "ortiqcha/(h/a)^2"], rows3)
note("Ortiqcha/(h/a)^2 ustuni a/h = 5, 10, 20 uchun deyarli DOIMIY "
     "(518, 512, 488) - demak farq aynan (h/a)^2 kabi kamayadi va bu "
     "HAQIQIY siljish deformatsiyasi, sonli xato emas. Koeffitsient "
     "taxminan 5.1 (foizda 510). a/h = 40 da nisbat pasayadi, chunki "
     "u yerda qoldiq diskretlashtirish xatosidan kichik bo'lib qoladi "
     "- ya'ni test o'z sezgirlik chegarasiga yetdi. Bu su-20 dagi "
     "Timoshenko balkasi bilan bir xil qonuniyat.")
series("Mindlin ortiqchasi", [5, 10, 20, 40],
       [float(r[2]) for r in rows3], xlabel="a/h", ylabel="ortiqcha, %")

# --- (4) MAHKAMLANGAN plastina: ikkinchi etalon ---
rows4 = []
h_c = a_pl/100.0
D_c = E*h_c**3/(12*(1 - nu**2))
for n in [8, 16, 24, 32]:
    w, _, _, _ = plate(n, a_pl, h_c, q_load, "cl", "sri")
    coef = w*D_c/(q_load*a_pl**4)
    rows4.append([n, f"{coef:.6f}", f"{abs(coef - 0.00126)/0.00126*100:.2f}"])
table("Mahkamlangan kvadrat plastina (adabiyot: 0.00126 q a^4 / D)",
      ["to'r n x n", "w D / (q a^4)", "adabiyotdan farq %"], rows4)
value("Sharnirli / mahkamlangan cho'kish nisbati",
      float(alpha_w/0.00126), "—")
note("Mahkamlangan plastina uchun ikkinchi mustaqil etalon ham 0.5% "
     "aniqlikda takrorlandi. Sharnirli plastina mahkamlanganidan 3.2 "
     "barobar ko'proq cho'kadi - chekka mahkamlash plastinada juda "
     "kuchli ta'sirga ega. Bu ikkita turli chegaraviy shart bilan "
     "o'tkazilgan tekshiruv element kodining to'g'riligiga ishonchni "
     "sezilarli oshiradi.")

# --- (5) Egilish sirti va moment ---
if u_p is not None:
    mid = n_div//2
    xs_line = [float(nodes_p[nid_p[i, mid], 0]) for i in range(n_div + 1)]
    ws_line = [float(abs(u_p[3*nid_p[i, mid]])) for i in range(n_div + 1)]
    series("FEM: w(x, a/2)", xs_line, ws_line, xlabel="x, m",
           ylabel="w, m")
    ex_line = []
    for x in xs_line:
        s = 0.0
        for m in range(1, 60, 2):
            for n_ in range(1, 60, 2):
                s += (np.sin(m*np.pi*x/a_pl)*np.sin(n_*np.pi/2) /
                      (m*n_*(m*m + n_*n_)**2))
        ex_line.append(16*q_load*a_pl**4/(np.pi**6*D_thin)*s)
    series("Navye: w(x, a/2)", xs_line, ex_line, xlabel="x, m",
           ylabel="w, m")
    err_line = max(abs(f - e) for f, e in zip(ws_line, ex_line))
    value("Butun kesim bo'ylab maks farq",
          float(err_line/max(ex_line)*100), "%")

table("Plastina elementlarining taqqoslanishi",
      ["Element", "Nazariya", "Uzluksizlik", "Qulflanish", "Soxta rejim"],
      [["ACM / MZC", "Kirxgof", "C1 emas (mos emas)", "yo'q",
        "yo'q"],
       ["DKT", "Kirxgof", "diskret C1", "yo'q", "yo'q"],
       ["Q4 to'liq", "Mindlin", "C0", "KATASTROFIK", "yo'q"],
       ["Q4 + SRI", "Mindlin", "C0", "yo'q", "2 ta"],
       ["MITC4", "Mindlin", "C0", "yo'q", "YO'Q (eng yaxshi)"]])
''',
                parameters=[
                    p("a_pl", "Plastina tomoni", 0.5, 10.0, 1.0, 0.5, "m"),
                    p("a_over_h", "Nisbiy ingichkalik a/h", 5.0, 200.0,
                      100.0, 5.0),
                    p("n_div", "To'r bo'linishi", 4.0, 24.0, 12.0, 2.0),
                    p("q_load", "Tarqalgan yuk", 1e3, 1e5, 1e4, 1e3,
                      "Pa"),
                ],
                expected_output=(
                    "Navye qatori "
                    "$\\alpha_w = 0{,}004062$ "
                    "va "
                    "$\\alpha_M = 0{,}047886$ "
                    "beradi — adabiyotdagi "
                    "0,00406 va 0,0479 bilan "
                    "aynan mos; sinus "
                    "ko'paytuvchilari "
                    "unutilsa 0,004293 "
                    "chiqadi (5,7% xato). "
                    "$a/h = 100$ da to'liq "
                    "integrallash $4\\times4$ "
                    "to'rda javobning atigi "
                    "1,10% ini, $24\\times24$ "
                    "da 28,6% ini beradi; "
                    "SRI esa 97,8% va "
                    "100,00%. Element "
                    "darajasida SRI ikkita, "
                    "to'liq kamaytirilgan "
                    "integrallash esa "
                    "to'rtta soxta nol "
                    "rejim kiritadi, lekin "
                    "yig'ilgan matritsa "
                    "singulyar emas. "
                    "Mindlin ortiqchasi "
                    "aynan $(h/a)^2$ kabi "
                    "kamayadi (koeffitsient "
                    "$\\approx 5{,}1$), "
                    "ya'ni u haqiqiy "
                    "siljish deformatsiyasi. "
                    "Mahkamlangan plastina "
                    "uchun ikkinchi etalon "
                    "0,00126 ham 0,5% "
                    "aniqlikda "
                    "takrorlanadi."
                ),
            ),
            visual=vis(
                kind="Plastina egilishi va qulflanish",
                tool="React/SVG + Manim",
                description=(
                    "Egilish sirti, moment "
                    "xaritalari va "
                    "qulflanishning "
                    "qalinlikka bog'liqligi."
                ),
                how_to_draw=(
                    "React/SVG: markazda "
                    "plastina yuqoridan "
                    "ko'rinishda to'r bilan "
                    "chiziladi va "
                    "$w(x,y)$ qiymati rang "
                    "bilan beriladi; "
                    "chekkalari nolda "
                    "bo'lgani uchun markazga "
                    "qarab quyuqlashadi. "
                    "Yonida kesim "
                    "bo'ylab profil grafigi: "
                    "FEM nuqtalari va Navye "
                    "egri chizig'i ustma-ust. "
                    "Eng muhimi — pastdagi "
                    "ikki panel yonma-yon: "
                    "bir xil to'r, bir xil "
                    "yuk, faqat "
                    "integrallash sxemasi "
                    "boshqacha. Chapda SRI "
                    "bilan normal egilgan "
                    "plastina, o'ngda esa "
                    "to'liq integrallash "
                    "bilan deyarli tekis "
                    "qolgan plastina; "
                    "ikkalasining tagida "
                    "foiz ko'rsatkichi "
                    "(97,8% va 1,1%). "
                    "$a/h$ slayderi "
                    "surilganda o'ng "
                    "paneldagi plastina "
                    "asta-sekin "
                    "'tirilib' boradi — "
                    "qulflanishning "
                    "qalinlikka "
                    "bog'liqligi shunda "
                    "ko'rinadi. Uchinchi "
                    "panelda element "
                    "darajasidagi soxta "
                    "rejimlar "
                    "animatsiya bilan "
                    "ko'rsatiladi: "
                    "element "
                    "deformatsiyalanadi, "
                    "lekin energiya "
                    "ko'rsatkichi nolda "
                    "qoladi."
                ),
            ),
            interp=(
                "Navye qatoridagi sinus "
                "ko'paytuvchilari kichik "
                "detal ko'rinadi, lekin "
                "ularsiz yig'indi 5,7% "
                "noto'g'ri chiqadi — va bu "
                "xato jimgina o'tadi, "
                "chunki natija hali ham "
                "'ishonarli' ko'rinadi. "
                "Etalon qiymatni o'zi "
                "hisoblaganda ana shunday "
                "tuzoqlar bor, shuning "
                "uchun uni adabiyotdagi "
                "qiymat bilan "
                "solishtirish shart. "
                "Asosiy natija esa "
                "qulflanish jadvalida va "
                "u pq-24 dagi nazariyani "
                "sonli tasdiqlaydi. "
                "$a/h = 100$ da to'liq "
                "integrallash bilan "
                "element yuz barobardan "
                "ko'proq bikrroq: "
                "$4\\times4$ to'r "
                "javobning 1,1% ini "
                "beradi. Muhimi — bu "
                "to'r qo'polligidan "
                "emas: $24\\times24$ "
                "to'rda ham u 28,6% da "
                "qoladi, ya'ni "
                "zichlashtirish "
                "kasallikni "
                "davolamaydi (su-16 "
                "dagi xulosa "
                "takrorlanadi). "
                "SRI esa eng dag'al "
                "to'rda ham 97,8% "
                "beradi. Farq bitta "
                "satrda va bu FEM "
                "dasturlashdagi eng "
                "katta samaradorlik "
                "farqlaridan biri. "
                "Ammo uchinchi jadval "
                "halollik talab "
                "qiladi: SRI bepul "
                "emas. Element "
                "darajasida u ikkita "
                "soxta nol energiyali "
                "rejim kiritadi. "
                "Amalda yig'ish va "
                "chegaraviy shartlar "
                "ularni bostiradi — "
                "barcha hisoblar "
                "muvaffaqiyatli "
                "yechildi — lekin bu "
                "kafolat emas va "
                "aynan shu sababdan "
                "zamonaviy paketlar "
                "MITC oilasini "
                "ishlatadi. To'rtinchi "
                "jadval esa nazariya "
                "tanloviga aniqlik "
                "kiritadi. Mindlin "
                "yechimining Kirxgofdan "
                "ortiqchasi aynan "
                "$(h/a)^2$ kabi "
                "kamayadi va "
                "koeffitsient uchta "
                "qalinlikda deyarli "
                "doimiy — demak bu "
                "haqiqiy siljish "
                "deformatsiyasi, sonli "
                "xato emas. "
                "$a/h = 40$ da nisbat "
                "buzila boshlaydi, "
                "chunki qoldiq "
                "diskretlashtirish "
                "xatosidan kichik "
                "bo'lib qoladi — "
                "testning sezgirlik "
                "chegarasi shu yerda. "
                "Buni tan olish ham "
                "o'lchov madaniyatining "
                "qismi."
            ),
            mistakes=[
                "Ingichka plastinada "
                "to'liq integrallashni "
                "ishlatish. Element yuz "
                "barobar bikrroq bo'ladi "
                "va to'r zichlashtirish "
                "yordam bermaydi.",
                "Navye qatorida sinus "
                "ko'paytuvchilarini "
                "unutish. Natija 5,7% "
                "noto'g'ri chiqadi va "
                "ishonarli ko'rinadi.",
                "SRI ni soxta rejimlarni "
                "tekshirmasdan ishlatish. "
                "Element darajasida "
                "ikkita soxta rejim bor.",
                "Sharnirli chekkaning "
                "qattiq va yumshoq "
                "variantlarini "
                "adashtirish. Mindlin "
                "nazariyasida ular farq "
                "qiladi.",
                "$w/h$ nisbatini "
                "tekshirmaslik. "
                "$w > h/5$ bo'lsa "
                "chiziqli plastina "
                "nazariyasi "
                "qo'llanmaydi (su-24).",
                "Tekis qobiq elementlarida "
                "$\\theta_z$ "
                "singulyarligini "
                "e'tiborsiz qoldirish.",
            ],
            quiz=[
                q("Mindlin nazariyasi "
                  "Kirxgofdan nimasi bilan "
                  "qulayroq?",
                  "Faqat birinchi hosilalar "
                  "qatnashadi, demak $C^0$ "
                  "bazis yetarli; Kirxgof "
                  "esa ikki o'lchovda "
                  "ta'minlash qiyin bo'lgan "
                  "$C^1$ ni talab qiladi.",
                  "konseptual"),
                q("Siljish qulflanishining "
                  "sababi nima?",
                  "$\\mathbf{k}_b \\sim h^3$, "
                  "$\\mathbf{k}_s \\sim h$ — "
                  "nisbat $(a/h)^2$ kabi "
                  "o'sadi va ingichka "
                  "plastinada siljish hadi "
                  "elementni bo'g'ib "
                  "qo'yadi.", "konseptual"),
                q("$a = 4$ m, $h = 8$ mm "
                  "plastinada siljish "
                  "deformatsiyasining "
                  "ulushi qancha?",
                  "$5{,}1(h/a)^2 = "
                  "5{,}1 \\cdot 4\\cdot"
                  "10^{-6} = 0{,}002\\%$ — "
                  "mutlaqo ahamiyatsiz.",
                  "hisob"),
                q("Kodda to'liq va tanlab "
                  "kamaytirilgan "
                  "integrallash qanday farq "
                  "beradi?",
                  "$a/h = 100$, $4\\times4$ "
                  "to'rda to'liq 1,10%, SRI "
                  "97,8%; $24\\times24$ da "
                  "28,6% va 100,00% — "
                  "zichlashtirish "
                  "qulflanishni "
                  "davolamaydi.", "kod"),
                q("SRI ning yashirin narxi "
                  "nima va u nima uchun "
                  "amalda ishlaydi?",
                  "Element darajasida ikkita "
                  "soxta nol rejim kiritadi "
                  "(rang 9 dan 7 ga), lekin "
                  "yig'ish va chegaraviy "
                  "shartlar ularni "
                  "bostiradi.", "kod"),
                q("Mindlin ortiqchasi sonli "
                  "xatomi yoki fizik "
                  "hodisami? Qanday "
                  "tekshiriladi?",
                  "Fizik — u aynan "
                  "$(h/a)^2$ kabi kamayadi "
                  "va koeffitsient uchta "
                  "qalinlikda doimiy "
                  "(518, 512, 488).",
                  "talqin"),
                q("Plastina cho'kishini "
                  "kamaytirishning eng "
                  "kuchli usuli qaysi?",
                  "Qalinlikni oshirish: "
                  "$w \\sim h^{-3}$, demak "
                  "qalinlikni ikki barobar "
                  "oshirish cho'kishni "
                  "sakkiz barobar "
                  "kamaytiradi.", "talqin"),
            ],
            bridge=(
                "Shu paytgacha barcha "
                "masalalar statik va "
                "chiziqli edi: "
                "$\\mathbf{K}\\mathbf{u} = "
                "\\mathbf{F}$. Keyingi "
                "mavzuda xususiy qiymat "
                "masalalariga o'tamiz — "
                "tebranish chastotalari va "
                "ustuvorlik kuchlari. "
                "U yerda massa va geometrik "
                "bikrlik matritsalari "
                "paydo bo'ladi."
            ),
            research=(
                "Plastina va qobiq "
                "elementlarini "
                "chuqurlashtiring. "
                "(1) MITC4 elementini "
                "o'rganing: siljish "
                "deformatsiyasi alohida "
                "nuqtalarda "
                "interpolyatsiya "
                "qilinadi — bu "
                "qulflanishni qanday "
                "yechadi va nima uchun "
                "soxta rejim "
                "kiritmaydi? "
                "(2) Diskret Kirxgof "
                "uchburchagini (DKT) "
                "ko'rib chiqing: u "
                "siljishni aynan nolga "
                "tenglashtiradi. "
                "(3) Egri qobiq "
                "elementlarini va "
                "membrana "
                "qulflanishini "
                "o'rganing (pq-26): u "
                "siljish "
                "qulflanishidan "
                "qanday farq qiladi? "
                "(4) Qatlamli "
                "kompozitlar uchun "
                "yuqori tartibli "
                "siljish nazariyalarini "
                "(HSDT) ko'rib "
                "chiqing."
            ),
            manim_ref=manim(
                scene="PlateLockingScene",
                module="manim/scenes/su_apps.py",
                title="Plastina qulflanishi",
                summary=(
                    "Ikkita bir xil plastina "
                    "yonma-yon turadi va "
                    "bir xil yuk bilan "
                    "yuklanadi. Chapdagisi "
                    "(SRI) normal egiladi, "
                    "o'ngdagisi (to'liq "
                    "integrallash) deyarli "
                    "qimirlamaydi. "
                    "Qalinlik slayderi "
                    "ko'tarilganda o'ngdagi "
                    "plastina asta-sekin "
                    "chapdagiga "
                    "yetib oladi — "
                    "qulflanish "
                    "yo'qoladi. Oxirida "
                    "bitta element "
                    "ajratib olinadi va "
                    "uning soxta nol "
                    "energiyali rejimi "
                    "ko'rsatiladi."
                ),
            ),
        ),
    ),
]
