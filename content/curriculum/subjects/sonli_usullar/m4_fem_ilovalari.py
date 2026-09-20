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
]
