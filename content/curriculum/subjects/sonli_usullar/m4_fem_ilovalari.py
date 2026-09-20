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
        difficulty="murakkab",
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
        difficulty="murakkab",
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

    # ------------------------------------------------------------------ su-23
    Topic(
        id="su-23",
        subject_id=S, module_id=M, order=23,
        title="Xususiy qiymat masalalari: tebranish va ustuvorlik",
        description=(
            "Massa matritsasi, erkin tebranish chastotalari va shakllari, "
            "geometrik bikrlik matritsasi, ustuvorlik yuklari hamda "
            "xususiy qiymatlarni sonli topish usullari."
        ),
        learning_objective=(
            "Tebranish va ustuvorlik masalalarini umumlashgan xususiy "
            "qiymat masalasi sifatida qo'yish, yechish va natijani "
            "analitik yechim bilan tekshirish."
        ),
        prerequisites=["su-22", "nm-26", "mq-25"],
        mathematical_core=(
            "$(\\mathbf{K} - \\omega^2\\mathbf{M})\\boldsymbol\\phi = "
            "\\mathbf{0}$; "
            "$(\\mathbf{K} - \\lambda\\mathbf{K}_G)"
            "\\boldsymbol\\phi = \\mathbf{0}$; "
            "$P_{cr} = \\pi^2EI/(KL)^2$."
        ),
        engineering_application=(
            "Bino va ko'priklarning seysmik hisobi, mashina "
            "rezonansdan qochish, ustun va qobiq ustuvorligi, "
            "shamol tufayli tebranishlar."
        ),
        computational_component=(
            "Massa va geometrik bikrlik matritsalarini qurish, xususiy "
            "qiymatlarni topish va ikki tomonlama chegara olish."
        ),
        visualization_component=(
            "Tebranish shakllari, ustuvorlik shakllari, "
            "chastotalarning to'r bilan yaqinlashishi."
        ),
        research_extension=(
            "Lanshos va blokli subfazo iteratsiyasi usullarini "
            "o'rganing: katta tizimlarda faqat bir necha xususiy "
            "qiymat qanday topiladi."
        ),
        difficulty="murakkab",
        previous_link=(
            "Shu paytgacha barcha masalalar "
            "$\\mathbf{K}\\mathbf{u} = \\mathbf{F}$ ko'rinishida edi — "
            "berilgan yukka berilgan javob. Endi savol o'zgaradi: "
            "konstruksiya **qanday chastotalarda** tebranadi va "
            "**qanday yukda** ustuvorligini yo'qotadi?"
        ),
        next_topic="su-24",
        estimated_minutes=95,
        tags=["xususiy qiymat", "massa matritsasi", "tebranish shakli",
              "geometrik bikrlik", "ustuvorlik", "Eyler kuchi"],
        lesson=_lesson(
            problem=(
                "Sanoat binosida yangi "
                "kompressor o'rnatilmoqda: "
                "aylanish chastotasi "
                "1480 ayl/min, ya'ni 24,7 Hz. "
                "Pol plitasining xususiy "
                "chastotasi shunga yaqin "
                "bo'lsa rezonans yuzaga "
                "keladi va tebranish "
                "amplitudasi bir necha "
                "barobar o'sadi — "
                "konstruksiya charchoqdan "
                "buziladi. Ayni paytda "
                "binoning po'lat ustunlari "
                "tom yukini ko'taradi va "
                "ularning ustuvorligi "
                "tekshirilishi kerak. "
                "Ikkala savol ham birinchi "
                "qarashda butunlay "
                "boshqacha, lekin "
                "matematik jihatdan ular "
                "**bir xil** masala. "
                "Qanday qilib?"
            ),
            concepts=[
                c("Umumlashgan xususiy qiymat "
                  "masalasi",
                  "$\\mathbf{A}\\boldsymbol\\phi "
                  "= \\lambda\\mathbf{B}"
                  "\\boldsymbol\\phi$ — "
                  "tebranish va ustuvorlik "
                  "ikkalasi ham shu "
                  "ko'rinishda."),
                c("Moslashgan massa matritsasi",
                  "$\\mathbf{M} = \\int\\rho"
                  "\\mathbf{N}^T\\mathbf{N}"
                  "\\,dV$ — bikrlik matritsasi "
                  "bilan **bir xil** shakl "
                  "funksiyalaridan."),
                c("Jamlangan massa matritsasi",
                  "Diagonal; hisob arzon, "
                  "lekin aniqlik past. "
                  "HRZ sxemasi to'liq massani "
                  "saqlaydi."),
                c("Tebranish shakli "
                  "(mode shape)",
                  "$\\boldsymbol\\phi_i$ — "
                  "konstruksiyaning o'ziga xos "
                  "deformatsiya shakli; "
                  "ular ortogonal (nm-28)."),
                c("Geometrik bikrlik matritsasi",
                  "$\\mathbf{K}_G$ — o'q kuchi "
                  "tufayli bikrlikning "
                  "o'zgarishi; siquvchi kuch "
                  "uni **kamaytiradi**."),
                c("Ustuvorlik yuki",
                  "$\\mathbf{K}$ va "
                  "$\\lambda\\mathbf{K}_G$ "
                  "teng bo'lgan yuk — "
                  "effektiv bikrlik nolga "
                  "aylanadi (mq-25)."),
            ],
            derivation=[
                d("1. Harakat tenglamasi",
                  r"\mathbf{M}\ddot{\mathbf{u}} "
                  r"+ \mathbf{K}\mathbf{u} = "
                  r"\mathbf{0}",
                  "Erkin tebranish (so'nishsiz). "
                  "nm-26 dagi tenglamaning "
                  "ko'p erkinlik darajali "
                  "ko'rinishi."),
                d("2. Garmonik yechim taxmini",
                  r"\mathbf{u}(t) = "
                  r"\boldsymbol\phi\,"
                  r"e^{i\omega t}",
                  "Shakl vaqtdan mustaqil, "
                  "faqat amplitudasi "
                  "o'zgaradi — bu "
                  "o'zgaruvchilarni "
                  "ajratishning natijasi."),
                d("3. Xususiy qiymat masalasi",
                  r"\left(\mathbf{K} - "
                  r"\omega^2\mathbf{M}\right)"
                  r"\boldsymbol\phi = \mathbf{0}",
                  "**Asosiy natija.** "
                  "Notrivial yechim faqat "
                  "determinant nol "
                  "bo'lganda mavjud."),
                d("4. Moslashgan massa "
                  "matritsasi",
                  r"\mathbf{M}_e = \int_0^L "
                  r"\rho A\,\mathbf{N}^T"
                  r"\mathbf{N}\,dx",
                  "Bikrlik matritsasi bilan "
                  "bir xil Ermit "
                  "funksiyalaridan (su-20) — "
                  "shuning uchun "
                  "'moslashgan'."),
                d("5. Balka uchun natija",
                  r"\mathbf{M}_e = "
                  r"\frac{\rho AL}{420}"
                  r"\begin{bmatrix} 156 & 22L & "
                  r"54 & -13L\\ 22L & 4L^2 & "
                  r"13L & -3L^2\\ 54 & 13L & "
                  r"156 & -22L\\ -13L & -3L^2 & "
                  r"-22L & 4L^2\end{bmatrix}",
                  "Diagonal bo'lmagan hadlar "
                  "bor — massa erkinlik "
                  "darajalarini "
                  "**bog'laydi**."),
                d("6. Umumiy massa tekshiruvi",
                  r"\sum_i\sum_j M_{ij}\Big|_{"
                  r"\text{ko'chish}} = "
                  r"\rho A L_{jami}",
                  "**Majburiy tekshiruv.** "
                  "Qattiq jism ko'chishida "
                  "kinetik energiya "
                  "$\\frac12\\rho A L v^2$ "
                  "bo'lishi shart."),
                d("7. Jamlangan massa (HRZ)",
                  r"\mathbf{M}_e = \rho AL\,"
                  r"\mathrm{diag}\left(\tfrac12, "
                  r"\tfrac{L^2}{78}, \tfrac12, "
                  r"\tfrac{L^2}{78}\right)",
                  "Diagonal hadlar "
                  "masshtablanadi, to'liq "
                  "massa saqlanadi. "
                  "Burilish inersiyasi "
                  "nolga tenglashtirilsa "
                  "matritsa **singulyar** "
                  "bo'ladi."),
                d("8. Ikki tomonlama chegara",
                  r"\omega_{lump} \le "
                  r"\omega_{aniq} \le "
                  r"\omega_{cons}",
                  "**Amaliy jihatdan qimmatli.** "
                  "Moslashgan massa "
                  "chastotani oshirib, "
                  "jamlangan esa "
                  "kamaytirib beradi — "
                  "ikkalasini hisoblab "
                  "aniq javobni "
                  "**qamrab olish** "
                  "mumkin."),
                d("9. O'q kuchining ta'siri",
                  r"\Pi = \frac12\int EI"
                  r"(w'')^2dx - \frac{P}{2}"
                  r"\int (w')^2dx",
                  "Siquvchi kuch "
                  "potensial energiyani "
                  "**kamaytiradi** — "
                  "ikkinchi had manfiy "
                  "ishora bilan kiradi."),
                d("10. Geometrik bikrlik "
                  "matritsasi",
                  r"\mathbf{K}_G = "
                  r"\frac{1}{30L}"
                  r"\begin{bmatrix} 36 & 3L & "
                  r"-36 & 3L\\ 3L & 4L^2 & -3L "
                  r"& -L^2\\ -36 & -3L & 36 & "
                  r"-3L\\ 3L & -L^2 & -3L & "
                  r"4L^2\end{bmatrix}",
                  "$\\int(w')^2dx$ dan kelib "
                  "chiqadi. U **kuchdan "
                  "mustaqil** — kuch "
                  "ko'paytuvchi sifatida "
                  "ajratiladi."),
                d("11. Ustuvorlik masalasi",
                  r"\left(\mathbf{K} - \lambda"
                  r"\mathbf{K}_G\right)"
                  r"\boldsymbol\phi = \mathbf{0}",
                  "**Bir xil struktura.** "
                  "$\\lambda$ — kritik yuk. "
                  "Tebranishdagi "
                  "$\\mathbf{M}$ o'rnida "
                  "endi $\\mathbf{K}_G$ "
                  "turadi."),
                d("12. Effektiv uzunlik",
                  r"P_{cr} = \frac{\pi^2EI}"
                  r"{(KL)^2}",
                  "$K$ — chegaraviy shartga "
                  "bog'liq: sharnirli 1, "
                  "konsol 2, ikki uchi "
                  "mahkam 0,5, "
                  "mahkam–sharnirli "
                  "$\\pi/4{,}4934 = "
                  "0{,}69916$ (mq-25)."),
                d("13. Nima uchun yuqoridan "
                  "yaqinlashadi",
                  r"\text{FEM bikrroq} "
                  r"\;\Longrightarrow\; "
                  r"\omega_h \ge \omega, \quad "
                  r"P_{cr}^h \ge P_{cr}",
                  "Diskretlashtirish "
                  "harakatni cheklaydi, "
                  "demak tizim bikrroq "
                  "bo'ladi — bu su-13 dagi "
                  "energiya quyi chegarasi "
                  "prinsipining "
                  "oqibati."),
                d("14. Yuqori shakllar "
                  "yomonroq",
                  r"\text{xato} \sim "
                  r"\left(\frac{\omega_i h}{c}"
                  r"\right)^{2p}",
                  "**Amaliy qoida.** "
                  "$i$-shaklni ishonchli "
                  "olish uchun to'lqin "
                  "uzunligiga kamida "
                  "5–10 element kerak; "
                  "birinchi shakl uchun "
                  "yetarli to'r "
                  "o'ninchisi uchun "
                  "yaramaydi."),
            ],
            meaning=(
                "Bu mavzuning eng chiroyli "
                "g'oyasi 3- va 11-qadamlarni "
                "yonma-yon qo'yishda. "
                "Tebranish va ustuvorlik "
                "fizik jihatdan butunlay "
                "boshqacha hodisalar — "
                "biri vaqt bo'yicha "
                "tebranish, ikkinchisi "
                "statik muvozanatning "
                "yo'qolishi — lekin "
                "matematik jihatdan "
                "ikkalasi ham bitta "
                "umumlashgan xususiy qiymat "
                "masalasi. Faqat ikkinchi "
                "matritsa almashadi: "
                "tebranishda "
                "$\\mathbf{M}$, "
                "ustuvorlikda "
                "$\\mathbf{K}_G$. Demak "
                "bitta yechuvchi kod "
                "ikkala masalani ham "
                "hal qiladi va bu FEM "
                "paketlarining ichki "
                "tuzilishida aynan shunday "
                "amalga oshirilgan. "
                "9- va 10-qadamlar "
                "ustuvorlikning mohiyatini "
                "ochadi. Siquvchi o'q kuchi "
                "potensial energiyaga "
                "**manfiy** hissa qo'shadi: "
                "u egilishni "
                "qarshilik ko'rsatish "
                "o'rniga rag'batlantiradi. "
                "Yuk ortgani sari effektiv "
                "bikrlik "
                "$\\mathbf{K} - \\lambda"
                "\\mathbf{K}_G$ kamayadi va "
                "qaysidir nuqtada nolga "
                "aylanadi — o'sha nuqtada "
                "konstruksiya "
                "cheksiz kichik "
                "bezovtalanishdan katta "
                "ko'chish oladi. Bu "
                "ustuvorlikning FEM "
                "tilidagi ta'rifi. "
                "8-qadam esa amaliyotda "
                "kam ishlatiladigan, "
                "lekin juda qimmatli "
                "vositani beradi. "
                "Moslashgan massa "
                "chastotani yuqoridan, "
                "jamlangan massa esa "
                "pastdan baholaydi. "
                "Ikkalasini hisoblasangiz, "
                "aniq javob ular orasida "
                "**kafolatlangan** — "
                "ya'ni bitta hisobdan "
                "xatolik bahosini ham "
                "olasiz. Kod buni aniq "
                "ko'rsatadi: dag'al "
                "to'rda ikkita baho "
                "88% va 100,05% beradi, "
                "demak aniq javob shu "
                "oraliqda. 13-qadam "
                "nima uchun yuqoridan "
                "yaqinlashishni "
                "tushuntiradi va u "
                "su-13 dagi energiya "
                "prinsipiga bog'lanadi: "
                "diskretlashtirish "
                "harakat erkinligini "
                "cheklaydi, cheklangan "
                "tizim esa bikrroq "
                "bo'ladi. Nihoyat "
                "14-qadam eng ko'p "
                "xatoga sabab "
                "bo'ladigan amaliy "
                "nuqtani belgilaydi: "
                "birinchi chastota "
                "uchun yetarli to'r "
                "o'ninchisi uchun "
                "butunlay yaramaydi. "
                "Seysmik hisobda esa "
                "aynan yuqori shakllar "
                "kerak bo'ladi."
            ),
            equations=[
                eq(r"\left(\mathbf{K} - "
                   r"\omega^2\mathbf{M}\right)"
                   r"\boldsymbol\phi = \mathbf{0}",
                   "Erkin tebranish masalasi.",
                   "Tebranish"),
                eq(r"\left(\mathbf{K} - \lambda"
                   r"\mathbf{K}_G\right)"
                   r"\boldsymbol\phi = \mathbf{0}",
                   "Ustuvorlik masalasi — bir "
                   "xil struktura, boshqa "
                   "matritsa.", "Ustuvorlik"),
                eq(r"\mathbf{M}_e = "
                   r"\frac{\rho AL}{420}"
                   r"\begin{bmatrix} 156 & 22L & "
                   r"54 & -13L\\ 22L & 4L^2 & "
                   r"13L & -3L^2\\ 54 & 13L & "
                   r"156 & -22L\\ -13L & -3L^2 "
                   r"& -22L & 4L^2\end{bmatrix}",
                   "Balka elementining "
                   "moslashgan massa "
                   "matritsasi.",
                   "Massa matritsasi"),
                eq(r"\omega_{lump} \le "
                   r"\omega_{aniq} \le "
                   r"\omega_{cons}",
                   "Ikki massa matritsasi "
                   "aniq chastotani qamrab "
                   "oladi.",
                   "Ikki tomonlama chegara"),
            ],
            conditions=(
                "**Yechishdan oldin:**\n"
                "- $\\mathbf{K}$ va "
                "$\\mathbf{M}$ simmetrik va "
                "musbat aniq bo'lsin "
                "(chegaraviy shartlardan "
                "keyin);\n"
                "- Umumiy massa tekshiruvi "
                "bajarilsin;\n"
                "- Ustuvorlikda "
                "$\\mathbf{K}_G$ **musbat "
                "aniq emas** — u ishorasi "
                "aralash, shuning uchun "
                "manfiy xususiy qiymatlar "
                "ham chiqadi (teskari "
                "yo'nalishdagi yuk).\n\n"
                "**To'r tanlash:**\n"
                "- $i$-shakl uchun kamida "
                "$5i$–$10i$ element;\n"
                "- Birinchi 10 shakl kerak "
                "bo'lsa, birinchisi uchun "
                "yetarli to'rdan 10 barobar "
                "zichroq kerak;\n"
                "- Jamlangan massada "
                "burilish inersiyasi "
                "nolga tenglashtirilmasin "
                "— matritsa singulyar "
                "bo'ladi.\n\n"
                "**Rezonansdan qochish:** "
                "ishchi chastota xususiy "
                "chastotadan kamida 20–25% "
                "uzoq bo'lsin; "
                "$0{,}8 < \\omega_{ish}/"
                "\\omega_1 < 1{,}25$ "
                "oralig'idan qoching.\n\n"
                "**Ustuvorlik hisobining "
                "cheklovi:** chiziqli "
                "ustuvorlik tahlili "
                "**ideal** "
                "konstruksiya uchun "
                "yuqori baho beradi. "
                "Haqiqiy nuqsonlar "
                "(boshlang'ich egrilik, "
                "eksentrisitet) kritik "
                "yukni sezilarli "
                "kamaytiradi — "
                "ayniqsa qobiqlarda "
                "(pq-29), u yerda "
                "farq besh barobargacha "
                "boradi. Aniq javob "
                "uchun nochiziqli "
                "tahlil kerak (su-24)."
            ),
            worked=WorkedExample(
                statement=(
                    "Po'lat konsol balka: "
                    "$L = 3$ m, "
                    "$I = 8\\cdot10^{-6}$ m⁴, "
                    "$A = 6\\cdot10^{-3}$ m², "
                    "$\\rho = 7850$ kg/m³. "
                    "(a) Birinchi xususiy "
                    "chastotani toping; "
                    "(b) kompressor 24,7 Hz "
                    "da ishlasa, rezonans "
                    "xavfi bormi; "
                    "(c) xuddi shu ustun "
                    "siqilsa, Eyler kuchi "
                    "nechaga teng."
                ),
                given=[
                    r"L = 3\ \text{m}, \quad EI = "
                    r"2{,}1\cdot10^{11}\cdot"
                    r"8\cdot10^{-6} = 1{,}68"
                    r"\cdot10^{6}\ \text{N}"
                    r"\cdot\text{m}^2",
                    r"\rho A = 7850 \cdot "
                    r"6\cdot10^{-3} = 47{,}1\ "
                    r"\text{kg/m}",
                ],
                steps=[
                    st(r"\omega_1 = (\beta_1L)^2"
                       r"\sqrt{\frac{EI}{\rho A "
                       r"L^4}}",
                       "Konsol balka uchun "
                       "klassik formula."),
                    st(r"\cos\beta\cosh\beta + 1 = "
                       r"0 \;\Rightarrow\; "
                       r"\beta_1L = 1{,}875104",
                       "**Transsendent tenglama** "
                       "— kod uni sonli "
                       "yechadi, hech qanday "
                       "yaxlitlangan doimiy "
                       "ishlatilmaydi."),
                    st(r"\frac{EI}{\rho AL^4} = "
                       r"\frac{1{,}68\cdot10^6}"
                       r"{47{,}1 \cdot 81} = "
                       r"440{,}3",
                       "$L^4 = 81$ m⁴."),
                    st(r"\sqrt{440{,}3} = 20{,}98",
                       "Kvadrat ildiz."),
                    st(r"\omega_1 = "
                       r"(1{,}875104)^2 \cdot "
                       r"20{,}98 = 3{,}5160 "
                       r"\cdot 20{,}98",
                       "$(\\beta_1L)^2 = "
                       "3{,}5160$."),
                    st(r"\omega_1 = 73{,}78\ "
                       r"\text{rad/s}",
                       "Burchak chastotasi."),
                    st(r"f_1 = \frac{\omega_1}"
                       r"{2\pi} = "
                       r"\frac{73{,}78}{6{,}283} "
                       r"= 11{,}74\ \text{Hz}",
                       "**Birinchi xususiy "
                       "chastota.**"),
                    st(r"\text{(b)}\quad "
                       r"\frac{f_{ish}}{f_1} = "
                       r"\frac{24{,}7}{11{,}74} = "
                       r"2{,}10",
                       "Nisbat."),
                    st(r"2{,}10 > 1{,}25 "
                       r"\;\Rightarrow\; "
                       r"\text{xavfsiz}",
                       "Ishchi chastota "
                       "birinchi shakldan "
                       "ancha yuqori. "
                       "**Lekin** ikkinchi "
                       "shaklni tekshirish "
                       "kerak."),
                    st(r"f_2 = \left(\frac{4{,}6941}"
                       r"{1{,}8751}\right)^2 "
                       r"f_1 = 6{,}267 \cdot "
                       r"11{,}74 = 73{,}6\ "
                       r"\text{Hz}",
                       "Ikkinchi chastota "
                       "ancha uzoq — "
                       "**xavfsiz**."),
                    st(r"\text{(c)}\quad P_{cr} = "
                       r"\frac{\pi^2EI}{(2L)^2} = "
                       r"\frac{9{,}8696 \cdot "
                       r"1{,}68\cdot10^6}{36}",
                       "Konsol uchun "
                       "$K = 2$."),
                    st(r"P_{cr} = 460{,}6\ "
                       r"\text{kN}",
                       "**Eyler kuchi.** Kod "
                       "buni to'rtta "
                       "chegaraviy shart "
                       "uchun ham "
                       "$10^{-4}$% "
                       "aniqlikda "
                       "takrorlaydi."),
                ],
                answer=(
                    "(a) $f_1 = 11{,}74$ Hz; "
                    "(b) ishchi chastota "
                    "$24{,}7$ Hz birinchi "
                    "shakldan 2,1 barobar, "
                    "ikkinchisidan esa 3 "
                    "barobar uzoq — "
                    "rezonans xavfi yo'q; "
                    "(c) $P_{cr} = 460{,}6$ kN "
                    "($K = 2$)."
                ),
                engineering_note=(
                    "(b) javobida ikkinchi "
                    "shaklni ham "
                    "tekshirganimizga "
                    "e'tibor bering. Faqat "
                    "birinchi chastotani "
                    "ko'rib 'xavfsiz' deb "
                    "xulosa chiqarish keng "
                    "tarqalgan xato: "
                    "ishchi chastota "
                    "birinchisidan yuqori "
                    "bo'lsa, u ikkinchi "
                    "yoki uchinchisiga "
                    "tushib qolishi "
                    "mumkin. Qoida: "
                    "ishchi chastotadan "
                    "yuqoridagi birinchi "
                    "xususiy chastotagacha "
                    "barcha shakllarni "
                    "tekshiring. "
                    "Ikkinchi muhim nuqta "
                    "(c) ga tegishli. "
                    "$P_{cr} = 460$ kN — "
                    "bu **ideal** ustun "
                    "uchun. Haqiqiy "
                    "ustunda boshlang'ich "
                    "egrilik va "
                    "eksentrisitet bor, "
                    "shuning uchun "
                    "me'yorlar bu "
                    "qiymatni "
                    "kamaytiruvchi "
                    "koeffitsient bilan "
                    "ishlatadi. Qobiqlarda "
                    "esa farq keskin: "
                    "pq-29 da ko'rganimizdek, "
                    "nuqsonlarga sezgirlik "
                    "tufayli haqiqiy "
                    "kritik yuk nazariy "
                    "qiymatning beshdan "
                    "bir qismigacha "
                    "tushishi mumkin. "
                    "Shuning uchun "
                    "chiziqli ustuvorlik "
                    "tahlili — bu "
                    "**boshlang'ich "
                    "baho**, yakuniy "
                    "javob emas."
                ),
            ),
            computation=Computation(
                caption=(
                    "Massa va geometrik bikrlik "
                    "matritsalarini qurish, "
                    "chastota va ustuvorlik "
                    "yuklarini topish, "
                    "natijani analitik yechim "
                    "bilan tekshirish."
                ),
                code='''"""Xususiy qiymat masalalari: tebranish va ustuvorlik."""
import numpy as np
from labkit import PARAMS, note, series, table, value
from scipy.linalg import eigh
from scipy.optimize import brentq

n_el = int(PARAMS.get("n_el", 8))
L_b = float(PARAMS.get("L_b", 3.0))
I_sec = float(PARAMS.get("I_sec", 8e-6))
A_sec = float(PARAMS.get("A_sec", 6e-3))

E = 2.1e11
rho = 7850.0
EI = E*I_sec
mA = rho*A_sec


def ke(Le):
    return EI/Le**3*np.array([
        [12, 6*Le, -12, 6*Le],
        [6*Le, 4*Le**2, -6*Le, 2*Le**2],
        [-12, -6*Le, 12, -6*Le],
        [6*Le, 2*Le**2, -6*Le, 4*Le**2]], dtype=float)


def me_consistent(Le):
    return mA*Le/420*np.array([
        [156, 22*Le, 54, -13*Le],
        [22*Le, 4*Le**2, 13*Le, -3*Le**2],
        [54, 13*Le, 156, -22*Le],
        [-13*Le, -3*Le**2, -22*Le, 4*Le**2]], dtype=float)


def me_hrz(Le):
    """HRZ jamlash: diagonal, to'liq massa saqlanadi."""
    return mA*Le*np.diag([0.5, Le**2/78, 0.5, Le**2/78])


def kg(Le):
    """Geometrik bikrlik - birlik siquvchi kuch uchun."""
    return 1.0/(30*Le)*np.array([
        [36, 3*Le, -36, 3*Le],
        [3*Le, 4*Le**2, -3*Le, -Le**2],
        [-36, -3*Le, 36, -3*Le],
        [3*Le, -Le**2, -3*Le, 4*Le**2]], dtype=float)


BC = {"cant": lambda n: [0, 1],
      "ss": lambda n: [0, 2*n],
      "ff": lambda n: [0, 1, 2*n, 2*n + 1],
      "fp": lambda n: [0, 1, 2*n]}


def assemble(n, mass, bc):
    h = L_b/n
    nd = 2*(n + 1)
    K = np.zeros((nd, nd))
    M = np.zeros((nd, nd))
    G = np.zeros((nd, nd))
    for e in range(n):
        idx = [2*e, 2*e + 1, 2*e + 2, 2*e + 3]
        K[np.ix_(idx, idx)] += ke(h)
        G[np.ix_(idx, idx)] += kg(h)
        M[np.ix_(idx, idx)] += (me_consistent(h) if mass == "cons"
                                else me_hrz(h))
    fx = BC[bc](n)
    free = np.setdiff1d(np.arange(nd), fx)
    return (K[np.ix_(free, free)], M[np.ix_(free, free)],
            G[np.ix_(free, free)], K, M, G)


# --- (0) MASSA MATRITSASINING TEKSHIRUVI ---
_, _, _, _, M_full, _ = assemble(n_el, "cons", "cant")
_, _, _, _, M_hrz, _ = assemble(n_el, "hrz", "cant")
ones_tr = np.zeros(2*(n_el + 1))
ones_tr[0::2] = 1.0            # qattiq jism ko'chishi
value("Moslashgan massa: 1^T M 1 (ko'chish)",
      float(ones_tr @ M_full @ ones_tr), "kg")
value("HRZ massa: 1^T M 1 (ko'chish)",
      float(ones_tr @ M_hrz @ ones_tr), "kg")
value("Haqiqiy massa rho*A*L", mA*L_b, "kg")
note("Ikkala massa matritsasi ham qattiq jism ko'chishida to'liq "
     "massani AYNAN beradi - bu massa matritsasining birinchi va eng "
     "muhim tekshiruvi. Agar bu bajarilmasa, barcha chastotalar "
     "noto'g'ri chiqadi va xato jimgina o'tadi.")

# --- (1) ANALITIK ETALONLAR: transsendent tenglamalarni YECHAMIZ ---
def roots_cant(k):
    f = lambda b: np.cos(b)*np.cosh(b) + 1.0
    out = []
    lo = 1.0
    while len(out) < k:
        hi = lo + 0.25
        while f(lo)*f(hi) > 0 and hi < 40:
            lo, hi = hi, hi + 0.25
        if hi >= 40:
            break
        out.append(brentq(f, lo, hi))
        lo = hi
    return out


bl = roots_cant(4)
value("Konsol: beta_1 L (cos*cosh + 1 = 0)", bl[0], "—")
value("Konsol: beta_2 L", bl[1], "—")
value("Konsol: beta_3 L", bl[2], "—")
w_exact = [(b**2)*np.sqrt(EI/(mA*L_b**4)) for b in bl]
value("Aniq omega_1", w_exact[0], "rad/s")
value("Aniq f_1", w_exact[0]/(2*np.pi), "Hz")
value("Aniq f_2", w_exact[1]/(2*np.pi), "Hz")

# --- (2) CHASTOTALAR: moslashgan va jamlangan massa ---
rows = []
for n in [2, 4, 8, 16, 32]:
    line = [n]
    for mass in ["cons", "hrz"]:
        K, M, _, _, _, _ = assemble(n, mass, "cant")
        w = np.sqrt(np.sort(eigh(K, M, eigvals_only=True))[:3])
        line += [f"{w[i]/w_exact[i]*100:.4f}" for i in range(3)]
    rows.append(line)
table("Konsol balka chastotalari, aniq qiymatga nisbatan %",
      ["elementlar", "cons f1", "cons f2", "cons f3",
       "HRZ f1", "HRZ f2", "HRZ f3"], rows)
K4, M4, _, _, _, _ = assemble(4, "cons", "cant")
Kh, Mh, _, _, _, _ = assemble(4, "hrz", "cant")
w_c = np.sqrt(np.sort(eigh(K4, M4, eigvals_only=True))[0])
w_h = np.sqrt(np.sort(eigh(Kh, Mh, eigvals_only=True))[0])
value("4 element, moslashgan massa: f1", float(w_c/(2*np.pi)), "Hz")
value("4 element, HRZ massa: f1", float(w_h/(2*np.pi)), "Hz")
value("Aniq f1 shu oraliqdami (1 = ha)",
      float(1.0 if w_h <= w_exact[0] <= w_c else 0.0), "—")
value("Oraliq kengligi", float((w_c - w_h)/w_exact[0]*100), "%")
note("IKKI TOMONLAMA CHEGARA. Moslashgan massa chastotani har doim "
     "YUQORIDAN (100.048%, 100.849%, 121.8%), HRZ jamlangan massa esa "
     "PASTDAN (88.7%, 71.2%, 94.0%) baholaydi. Demak aniq javob ikkisi "
     "orasida KAFOLATLANGAN. Bu amalda kam ishlatiladigan, lekin juda "
     "qimmatli vosita: ikkita hisob bilan nafaqat javobni, balki "
     "xatolik chegarasini ham olasiz. Yuqoridan yaqinlashish "
     "tasodifiy emas - diskretlashtirish harakat erkinligini "
     "cheklaydi, cheklangan tizim esa bikrroq bo'ladi (su-13).")

series("Moslashgan massa: f1 xatosi", [2, 4, 8, 16, 32],
       [float(r[1]) for r in rows], xlabel="elementlar",
       ylabel="aniqlik, %")
series("HRZ massa: f1 xatosi", [2, 4, 8, 16, 32],
       [float(r[4]) for r in rows], xlabel="elementlar",
       ylabel="aniqlik, %")
series("Aniq qiymat", [2, 4, 8, 16, 32], [100.0]*5,
       xlabel="elementlar", ylabel="aniqlik, %")

# --- (3) YUQORI SHAKLLAR yomonroq yaqinlashadi ---
rows2 = []
bl8 = roots_cant(6)
w_ex8 = [(b**2)*np.sqrt(EI/(mA*L_b**4)) for b in bl8]
for n in [4, 8, 16, 32]:
    K, M, _, _, _, _ = assemble(n, "cons", "cant")
    w = np.sqrt(np.sort(eigh(K, M, eigvals_only=True)))
    line = [n] + [f"{(w[i]/w_ex8[i] - 1)*100:.4f}"
                  for i in range(min(5, len(w)))]
    rows2.append(line)
table("Yuqori shakllar qanchalik yomonroq (xato, %)",
      ["elementlar", "1-shakl", "2-shakl", "3-shakl", "4-shakl",
       "5-shakl"], rows2)
note("Bir xil to'rda yuqori shakllar ANCHA yomonroq: 8 elementda "
     "1-shakl xatosi 0.0002%, 5-shakl xatosi esa 0.5786% - ya'ni 2900 "
     "barobar katta. 4 elementda farq undan ham keskin: 0.0033% ga "
     "qarshi 14.1%. Sabab - yuqori shakl qisqaroq to'lqin uzunligiga "
     "ega va "
     "uni ifodalash uchun ko'proq element kerak. Amaliy qoida: "
     "i-shaklni ishonchli olish uchun kamida 5i...10i element. Seysmik "
     "hisobda aynan yuqori shakllar kerak bo'ladi, shuning uchun bu "
     "qoidani e'tiborsiz qoldirib bo'lmaydi.")

# --- (4) TEBRANISH SHAKLLARI va ORTOGONALLIK ---
K, M, _, _, _, _ = assemble(n_el, "cons", "cant")
ev, phi = eigh(K, M)
w_num = np.sqrt(ev)
# M-ortogonallik: phi_i^T M phi_j = delta_ij (normallashtirilgan)
Gram = phi[:, :4].T @ M @ phi[:, :4]
value("Shakllarning M-ortogonalligi: maks diagonaldan tashqari",
      float(np.max(np.abs(Gram - np.diag(np.diag(Gram))))), "—")
Gram_K = phi[:, :4].T @ K @ phi[:, :4]
# K-Gram diagonalida omega^2 turadi (katta sonlar), shuning uchun
# nisbiy o'lchovda baholaymiz
value("Shakllarning K-ortogonalligi: nisbiy maks (diagonaldan tashqari)",
      float(np.max(np.abs(Gram_K - np.diag(np.diag(Gram_K)))) /
            np.max(np.abs(np.diag(Gram_K)))), "—")
value("Reley nisbati phi^T K phi / phi^T M phi (1-shakl)",
      float((phi[:, 0] @ K @ phi[:, 0])/(phi[:, 0] @ M @ phi[:, 0])),
      "rad^2/s^2")
value("omega_1^2 (xususiy qiymatdan)", float(ev[0]), "rad^2/s^2")
xs = np.linspace(0, L_b, n_el + 1)
for k_ in range(3):
    shape = np.concatenate([[0.0], phi[0::2, k_]])
    shape = shape/np.max(np.abs(shape))
    series(f"{k_+1}-tebranish shakli", xs.tolist(), shape.tolist(),
           xlabel="x, m", ylabel="normallashgan w")
note("Tebranish shakllari M va K bo'yicha ham ORTOGONAL - "
     "diagonaldan tashqari hadlar mashina noliga teng (nm-28). "
     "Bu modal superpozitsiyaning asosi: dinamik masala "
     "bog'lanmagan bir erkinlik darajali tenglamalarga ajraladi. "
     "Reley nisbati esa xususiy qiymat bilan aynan mos tushdi - "
     "bu xususiy vektorning to'g'ri hisoblanganini tasdiqlaydi.")

# --- (5) USTUVORLIK: to'rtta chegaraviy shart ---
u_fp = brentq(lambda x: np.tan(x) - x, np.pi + 1e-6, 1.5*np.pi - 1e-6)
K_fp = np.pi/u_fp
value("Mahkam-sharnirli: tan(u) = u ildizi", float(u_fp), "—")
value("Mahkam-sharnirli effektiv uzunlik K", float(K_fp), "—")
rows3 = []
for bc, Kf, nm in [("ss", 1.0, "sharnirli-sharnirli"),
                   ("cant", 2.0, "konsol"),
                   ("ff", 0.5, "mahkam-mahkam"),
                   ("fp", K_fp, "mahkam-sharnirli")]:
    P_ex = np.pi**2*EI/(Kf*L_b)**2
    line = [nm, f"{Kf:.5f}", f"{P_ex/1e3:.3f}"]
    for n in [2, 4, 8, 16]:
        K_, _, G_, _, _, _ = assemble(n, "cons", bc)
        evg = eigh(K_, G_, eigvals_only=True)
        lam = float(np.min(evg[evg > 1e-9]))
        line.append(f"{lam/P_ex*100:.4f}")
    rows3.append(line)
table("Ustuvorlik: P_cr = pi^2 EI/(KL)^2 ga nisbatan aniqlik, %",
      ["chegaraviy shart", "K", "aniq P_cr, kN", "n=2", "n=4", "n=8",
       "n=16"], rows3)
note("To'rtta chegaraviy shart uchun ham FEM Eyler kuchini 16 element "
     "bilan 0.02% dan yaxshi aniqlikda takrorladi va HAR DOIM "
     "YUQORIDAN yaqinlashdi - tebranishdagi kabi. Effektiv uzunlik "
     "koeffitsientlari qo'lda yozilmadi: mahkam-sharnirli holat uchun "
     "K = pi/u, bu yerda u - tan(u) = u tenglamasining ildizi, kod "
     "tomonidan sonli topildi. Shu bilan 'adabiyotdagi 0.699' "
     "yaxlitlanishi xatolik manbai bo'lib qolmaydi.")

# Ustuvorlik shakli
K_, _, G_, _, _, _ = assemble(n_el, "cons", "ss")
evg, phig = eigh(K_, G_)
i0 = int(np.argmin(np.where(evg > 1e-9, evg, np.inf)))
sh = np.concatenate([[0.0], phig[0::2, i0], [0.0]])
sh = sh/np.max(np.abs(sh))
series("Ustuvorlik shakli (sharnirli ustun)",
       np.linspace(0, L_b, len(sh)).tolist(), sh.tolist(),
       xlabel="x, m", ylabel="normallashgan w")
series("Aniq sin(pi x/L)", np.linspace(0, L_b, len(sh)).tolist(),
       np.sin(np.pi*np.linspace(0, L_b, len(sh))/L_b).tolist(),
       xlabel="x, m", ylabel="normallashgan w")

# --- (6) O'Q KUCHI CHASTOTAGA TA'SIRI ---
rows4 = []
K_, M_, G_, _, _, _ = assemble(16, "cons", "ss")
P_euler = np.pi**2*EI/L_b**2
for frac in [0.0, 0.25, 0.5, 0.75, 0.9, 0.99]:
    Keff = K_ - frac*P_euler*G_
    ev_ = eigh(Keff, M_, eigvals_only=True)
    w1 = np.sqrt(max(ev_[0], 0.0))
    w0 = np.sqrt(eigh(K_, M_, eigvals_only=True)[0])
    rows4.append([f"{frac:.2f}", f"{w1/w0:.5f}",
                  f"{np.sqrt(1 - frac):.5f}",
                  f"{abs(w1/w0 - np.sqrt(1-frac))*100:.4f}"])
table("Siquvchi kuch chastotani qanday kamaytiradi",
      ["P/P_cr", "omega/omega_0 (FEM)", "sqrt(1 - P/P_cr)", "farq %"],
      rows4)
series("Chastota va siquvchi kuch", [0, 0.25, 0.5, 0.75, 0.9, 0.99],
       [float(r[1]) for r in rows4], xlabel="P/P_cr",
       ylabel="omega/omega_0")
note("CHIROYLI BOG'LANISH. Siquvchi kuch ostida birinchi chastota "
     "sqrt(1 - P/P_cr) qonuni bo'yicha kamayadi va FEM buni 0.01% "
     "aniqlikda takrorladi. P -> P_cr da chastota NOLGA intiladi - "
     "ya'ni ustuvorlikni yo'qotish 'chastotasi nolga teng tebranish' "
     "sifatida talqin qilinadi. Bu tebranish va ustuvorlik bir xil "
     "matematik masala ekanining eng aniq fizik ifodasi. Amalda bu "
     "usul bilan ustunning haqiqiy kritik yukini buzmasdan o'lchash "
     "mumkin: bir necha yuk darajasida chastotani o'lchab, "
     "ekstrapolyatsiya qilinadi (Sautvell usuli).")

table("Tebranish va ustuvorlik: bir xil matematika",
      ["Jihat", "Tebranish", "Ustuvorlik"],
      [["Masala", "(K - w^2 M) phi = 0", "(K - lambda K_G) phi = 0"],
       ["Ikkinchi matritsa", "M (massa)", "K_G (geometrik)"],
       ["Xususiy qiymat", "w^2 (chastota kvadrati)", "lambda (kritik yuk)"],
       ["Xususiy vektor", "tebranish shakli", "ustuvorlik shakli"],
       ["M / K_G musbat aniqmi", "HA", "YO'Q (ishorasi aralash)"],
       ["Yaqinlashish", "yuqoridan", "yuqoridan"],
       ["Amaliy cheklov", "yuqori shakllar yomon",
        "nuqsonlarga sezgirlik (pq-29)"]])
''',
                parameters=[
                    p("n_el", "Elementlar soni", 2.0, 32.0, 8.0, 1.0),
                    p("L_b", "Balka uzunligi", 1.0, 12.0, 3.0, 0.5, "m"),
                    p("I_sec", "Inersiya momenti", 1e-6, 1e-4, 8e-6,
                      1e-6, "m⁴"),
                    p("A_sec", "Kesim yuzasi", 1e-3, 2e-2, 6e-3, 1e-3,
                      "m²"),
                ],
                expected_output=(
                    "Ikkala massa matritsasi "
                    "ham qattiq jism "
                    "ko'chishida to'liq "
                    "massani aynan beradi. "
                    "Moslashgan massa "
                    "chastotalarni yuqoridan "
                    "(100,048%, 100,849%, "
                    "121,8% ikki elementda), "
                    "HRZ jamlangan massa esa "
                    "pastdan (88,7%, 71,2%, "
                    "94,0%) baholaydi — aniq "
                    "javob ular orasida "
                    "kafolatlangan. Yuqori "
                    "shakllar sezilarli "
                    "yomonroq yaqinlashadi. "
                    "Tebranish shakllari "
                    "$\\mathbf{M}$ va "
                    "$\\mathbf{K}$ bo'yicha "
                    "mashina aniqligida "
                    "ortogonal, Reley "
                    "nisbati xususiy qiymat "
                    "bilan aynan mos "
                    "tushadi. To'rtta "
                    "chegaraviy shart uchun "
                    "ham Eyler kuchi 16 "
                    "element bilan 0,02% dan "
                    "yaxshi aniqlikda "
                    "chiqadi; "
                    "mahkam–sharnirli "
                    "holatning $K$ "
                    "koeffitsienti "
                    "$\\tan u = u$ "
                    "tenglamasidan sonli "
                    "topiladi. Siquvchi "
                    "kuch ostida chastota "
                    "$\\sqrt{1 - P/P_{cr}}$ "
                    "qonuni bo'yicha "
                    "kamayadi (0,01% "
                    "aniqlikda) va "
                    "$P \\to P_{cr}$ da "
                    "nolga intiladi."
                ),
            ),
            visual=vis(
                kind="Tebranish va ustuvorlik shakllari",
                tool="React/SVG + Manim",
                description=(
                    "Tebranish shakllari, "
                    "ustuvorlik shakli va "
                    "chastotaning siquvchi "
                    "kuchga bog'liqligi."
                ),
                how_to_draw=(
                    "React/SVG: yuqori panelda "
                    "balka chiziladi va tanlangan "
                    "tebranish shakli "
                    "animatsiya bilan "
                    "tebranadi; shakl "
                    "raqamini tanlash "
                    "tugmalari yonida "
                    "chastota qiymati "
                    "turadi. Tugunlar "
                    "(shakl nolga tegadigan "
                    "nuqtalar) alohida "
                    "belgilanadi va "
                    "ularning soni shakl "
                    "raqami bilan "
                    "o'sishi ko'rinadi. "
                    "O'rta panelda ikkita "
                    "yaqinlashish egri "
                    "chizig'i: moslashgan "
                    "massa 100% dan "
                    "**yuqorida**, "
                    "jamlangan massa "
                    "**pastda**, orasidagi "
                    "soha 'aniq javob shu "
                    "yerda' deb "
                    "shtrixlanadi — "
                    "element soni "
                    "oshgani sari "
                    "shtrixlangan tasma "
                    "torayadi. Pastki "
                    "panelda eng qiziq "
                    "tajriba: ustun "
                    "asta-sekin "
                    "siqiladi va uning "
                    "tebranish "
                    "animatsiyasi "
                    "**sekinlashadi**; "
                    "yonidagi grafik "
                    "$\\omega/\\omega_0$ "
                    "ni $P/P_{cr}$ ga "
                    "qarab chizadi va "
                    "u $\\sqrt{1-P/P_{cr}}$ "
                    "egri chizig'i bilan "
                    "ustma-ust tushadi. "
                    "$P \\to P_{cr}$ da "
                    "tebranish butunlay "
                    "to'xtaydi va balka "
                    "ustuvorlik shakliga "
                    "o'tib ketadi — "
                    "ikki hodisaning "
                    "birligi shu "
                    "lahzada "
                    "ko'rinadi."
                ),
            ),
            interp=(
                "Massa matritsasining "
                "tekshiruvi eng oddiy, "
                "lekin eng muhim qadam: "
                "qattiq jism ko'chishida "
                "u to'liq massani aynan "
                "berishi shart. Bu "
                "bajarilmasa barcha "
                "chastotalar noto'g'ri "
                "chiqadi va xato jimgina "
                "o'tadi, chunki natija "
                "hali ham ishonarli "
                "ko'rinadi. Asosiy "
                "natija esa ikki "
                "tomonlama chegarada. "
                "Moslashgan massa "
                "chastotani har doim "
                "yuqoridan, jamlangan "
                "massa esa pastdan "
                "baholaydi — demak "
                "ikkita hisob bilan "
                "aniq javobni qamrab "
                "olish mumkin. Bu "
                "amalda kam "
                "ishlatiladi, lekin "
                "bepul xatolik bahosini "
                "beradi va shuning uchun "
                "qimmatli. Yuqoridan "
                "yaqinlashish tasodifiy "
                "emas: diskretlashtirish "
                "harakat erkinligini "
                "cheklaydi, cheklangan "
                "tizim esa bikrroq "
                "bo'ladi — bu su-13 dagi "
                "energiya prinsipining "
                "bevosita oqibati va u "
                "ustuvorlikda ham "
                "takrorlanadi. Yuqori "
                "shakllar jadvali eng "
                "ko'p e'tibordan chetda "
                "qoladigan amaliy "
                "nuqtani ko'rsatadi: "
                "bir xil to'rda birinchi "
                "shakl xatosi 0,0002%, "
                "beshinchisiniki esa "
                "minglab barobar katta. "
                "Seysmik hisobda aynan "
                "yuqori shakllar kerak "
                "bo'ladi, shuning uchun "
                "'birinchi chastota "
                "to'g'ri chiqdi, demak "
                "to'r yetarli' degan "
                "xulosa xavfli. Eng "
                "chiroyli natija esa "
                "oxirgi tajribada. "
                "Siquvchi kuch ostida "
                "birinchi chastota "
                "$\\sqrt{1 - P/P_{cr}}$ "
                "qonuni bo'yicha "
                "kamayadi va FEM buni "
                "0,01% aniqlikda "
                "takrorlaydi. "
                "$P \\to P_{cr}$ da "
                "chastota nolga "
                "intiladi — ya'ni "
                "ustuvorlikni yo'qotish "
                "'chastotasi nol "
                "bo'lgan tebranish' "
                "sifatida talqin "
                "qilinadi. Shu bilan "
                "mavzu boshida qo'yilgan "
                "savol — nima uchun "
                "tebranish va ustuvorlik "
                "bitta masala — fizik "
                "javob oladi. Amalda bu "
                "bog'lanish Sautvell "
                "usulining asosi: "
                "ustunning kritik yukini "
                "uni buzmasdan, faqat "
                "chastota o'lchash "
                "orqali aniqlash "
                "mumkin."
            ),
            mistakes=[
                "Faqat birinchi chastotani "
                "tekshirish. Ishchi chastota "
                "ikkinchi yoki uchinchi "
                "shaklga tushib qolishi "
                "mumkin.",
                "Birinchi shakl uchun "
                "yetarli to'rni yuqori "
                "shakllar uchun ham "
                "yetarli deb hisoblash. "
                "$i$-shaklga $5i$–$10i$ "
                "element kerak.",
                "Jamlangan massada burilish "
                "inersiyasini nolga "
                "tenglashtirish. Matritsa "
                "singulyar bo'ladi va "
                "yechuvchi ishlamaydi.",
                "Massa matritsasining "
                "umumiy massasini "
                "tekshirmaslik — bu bir "
                "qator kod va u jiddiy "
                "xatolarni ochadi.",
                "Chiziqli ustuvorlik "
                "yukini yakuniy javob deb "
                "qabul qilish. Nuqsonlar "
                "uni sezilarli kamaytiradi, "
                "qobiqlarda besh barobargacha "
                "(pq-29).",
                "$\\mathbf{K}_G$ ni musbat "
                "aniq deb hisoblash. Uning "
                "ishorasi aralash va "
                "manfiy xususiy qiymatlar "
                "ham chiqadi.",
            ],
            quiz=[
                q("Tebranish va ustuvorlik "
                  "masalalari matematik "
                  "jihatdan nima bilan "
                  "bir xil?",
                  "Ikkalasi ham umumlashgan "
                  "xususiy qiymat masalasi; "
                  "faqat ikkinchi matritsa "
                  "almashadi — "
                  "$\\mathbf{M}$ o'rniga "
                  "$\\mathbf{K}_G$.",
                  "konseptual"),
                q("Nima uchun FEM "
                  "chastotalarni yuqoridan "
                  "baholaydi?",
                  "Diskretlashtirish harakat "
                  "erkinligini cheklaydi, "
                  "cheklangan tizim esa "
                  "bikrroq — bu su-13 dagi "
                  "energiya prinsipining "
                  "oqibati.", "konseptual"),
                q("$L = 3$ m konsol balkaning "
                  "birinchi chastotasi "
                  "qanday topiladi?",
                  "$\\omega_1 = "
                  "(1{,}8751)^2"
                  "\\sqrt{EI/(\\rho AL^4)} = "
                  "73{,}78$ rad/s, ya'ni "
                  "$f_1 = 11{,}74$ Hz.",
                  "hisob"),
                q("Kod ikki massa matritsasi "
                  "bilan qanday foydali "
                  "natija beradi?",
                  "Moslashgan yuqoridan, HRZ "
                  "pastdan baholaydi, demak "
                  "aniq javob ular orasida "
                  "kafolatlangan — bepul "
                  "xatolik bahosi.", "kod"),
                q("Siquvchi kuch chastotani "
                  "qanday o'zgartiradi?",
                  "$\\omega/\\omega_0 = "
                  "\\sqrt{1 - P/P_{cr}}$; "
                  "kod buni 0,01% aniqlikda "
                  "tasdiqlaydi va "
                  "$P \\to P_{cr}$ da "
                  "chastota nolga "
                  "intiladi.", "kod"),
                q("Effektiv uzunlik "
                  "koeffitsienti $K$ nimaga "
                  "bog'liq va "
                  "mahkam–sharnirli holatda "
                  "u qanday topiladi?",
                  "Chegaraviy shartga. "
                  "Mahkam–sharnirlida "
                  "$K = \\pi/u$, bu yerda "
                  "$u$ — $\\tan u = u$ "
                  "tenglamasining ildizi "
                  "($u = 4{,}4934$, "
                  "$K = 0{,}69916$).",
                  "talqin"),
                q("Chiziqli ustuvorlik "
                  "tahlilining asosiy "
                  "cheklovi nima?",
                  "U ideal konstruksiya "
                  "uchun yuqori baho "
                  "beradi; nuqsonlar "
                  "kritik yukni "
                  "kamaytiradi — "
                  "qobiqlarda besh "
                  "barobargacha (pq-29). "
                  "Aniq javob uchun "
                  "nochiziqli tahlil "
                  "kerak.", "talqin"),
            ],
            bridge=(
                "Xususiy qiymat masalalari "
                "ham chiziqli edi. Lekin "
                "ustuvorlikda ko'rganimizdek, "
                "haqiqiy javob nuqsonlarga "
                "va katta ko'chishlarga "
                "bog'liq. Keyingi mavzuda "
                "chiziqlilik taxminini "
                "butunlay bekor qilamiz: "
                "geometrik va fizik "
                "nochiziqlik, iterativ "
                "yechish usullari va "
                "'o'tib ketish' hodisasi."
            ),
            research=(
                "Xususiy qiymat "
                "hisoblarini "
                "chuqurlashtiring. "
                "(1) Lanshos va blokli "
                "subfazo iteratsiyasi "
                "usullarini o'rganing: "
                "million erkinlik "
                "darajali tizimdan "
                "faqat birinchi 50 "
                "shaklni qanday olish "
                "mumkin? "
                "(2) Shturm ketma-ketligi "
                "tekshiruvini ko'rib "
                "chiqing: berilgan "
                "oraliqda nechta xususiy "
                "qiymat borligini "
                "ularni hisoblamasdan "
                "aniqlash. "
                "(3) Modal massa va "
                "ishtirok "
                "koeffitsientlarini "
                "o'rganing: seysmik "
                "hisobda nechta shakl "
                "kerakligini qanday "
                "aniqlash (odatda "
                "modal massaning 90% i "
                "qamralsin)? "
                "(4) Sautvell grafigini "
                "va nuqsonli ustunning "
                "haqiqiy "
                "xatti-harakatini "
                "ko'rib chiqing."
            ),
            manim_ref=manim(
                scene="EigenScene",
                module="manim/scenes/su_apps.py",
                title="Tebranish va ustuvorlik birligi",
                summary=(
                    "Konsol balkaning "
                    "birinchi uchta "
                    "tebranish shakli "
                    "ketma-ket "
                    "animatsiya qilinadi "
                    "va tugunlar soni "
                    "o'sishi ko'rsatiladi. "
                    "Keyin sharnirli "
                    "ustun asta-sekin "
                    "siqiladi: uning "
                    "tebranishi "
                    "sekinlashadi, "
                    "chastota grafigi "
                    "$\\sqrt{1-P/P_{cr}}$ "
                    "egri chizig'i "
                    "bo'ylab tushadi va "
                    "kritik yukda "
                    "tebranish to'xtab, "
                    "ustun yon tomonga "
                    "egilib ketadi."
                ),
            ),
        ),
    ),

    # ------------------------------------------------------------------ su-24
    Topic(
        id="su-24",
        subject_id=S, module_id=M, order=24,
        title="Nochiziqli tahlil",
        description=(
            "Geometrik va fizik nochiziqlik, urinma bikrlik matritsasi, "
            "Nyuton–Rafson va uning o'zgartirilgan varianti, yuk va "
            "siljish nazorati, o'tib ketish hodisasi hamda "
            "elastoplastik qaytarish algoritmi."
        ),
        learning_objective=(
            "Nochiziqli masalani iterativ yechish, yaqinlashish tartibini "
            "o'lchash, chegaraviy nuqtadan o'ta oladigan usulni tanlash "
            "va natijani analitik yechim bilan tekshirish."
        ),
        prerequisites=["su-23", "su-02", "mq-08"],
        mathematical_core=(
            "$\\mathbf{K}_T\\Delta\\mathbf{u} = "
            "-\\mathbf{R}(\\mathbf{u})$; "
            "Nyuton kvadratik, o'zgartirilgani chiziqli; "
            "$\\sigma = \\sigma^{tr} - E\\Delta\\gamma\\,"
            "\\mathrm{sign}(\\sigma^{tr})$."
        ),
        engineering_application=(
            "Yassi qobiq va gumbazlarning o'tib ketishi, metall "
            "shakllantirish, avariya (crash) hisobi, chegaraviy yuk "
            "ko'taruvchanlik, katta ko'chishli konstruksiyalar."
        ),
        computational_component=(
            "Urinma bikrlikni qurish, Nyuton iteratsiyasini o'lchash, "
            "o'tib ketishni siljish nazorati bilan bosib o'tish, "
            "qaytarish algoritmini tekshirish."
        ),
        visualization_component=(
            "Yuk–ko'chish yo'li, chegaraviy nuqtalar, iteratsiyaning "
            "yaqinlashishi, kuchlanish–deformatsiya sikli."
        ),
        research_extension=(
            "Riks yoy uzunligi usulini o'rganing: u siljish nazorati "
            "ham yetarli bo'lmagan holatlarda ishlaydi."
        ),
        difficulty="murakkab",
        previous_link=(
            "su-23 da chiziqli ustuvorlik tahlili ideal konstruksiya "
            "uchun yuqori baho berishini ko'rdik. Haqiqiy javob esa "
            "katta ko'chishlarga va material oqishiga bog'liq — "
            "chiziqlilik taxminini butunlay bekor qilish vaqti keldi."
        ),
        next_topic="su-25",
        estimated_minutes=100,
        tags=["nochiziqlik", "Nyuton-Rafson", "o'tib ketish",
              "urinma bikrlik", "plastiklik", "qaytarish algoritmi"],
        lesson=_lesson(
            problem=(
                "Yassi gumbazli tom "
                "loyihalanmoqda: ko'tarilishi "
                "oralig'iga nisbatan juda "
                "kichik. Chiziqli hisob "
                "bemalol ishlaydi va yuk "
                "ko'taruvchanlik yetarli "
                "chiqadi. Lekin qorli qishda "
                "shunga o'xshash "
                "konstruksiyalar birdan, "
                "hech qanday ogohlantirishsiz "
                "**ichkariga o'pirilib "
                "tushadi** — go'yo ular "
                "ag'darilib ketadi. Yuk "
                "yemirilish kuchidan ancha "
                "kichik, material esa "
                "oqmagan. Chiziqli hisob bu "
                "hodisani umuman ko'rsata "
                "olmaydi, chunki u "
                "geometriyani "
                "o'zgarmas deb hisoblaydi. "
                "Aynan shu o'zgarish esa "
                "butun masalaning "
                "mohiyati."
            ),
            concepts=[
                c("Geometrik nochiziqlik",
                  "Muvozanat **deformatsiyalangan** "
                  "holatda yoziladi; katta "
                  "ko'chishlarda geometriya "
                  "o'zgaradi."),
                c("Fizik nochiziqlik",
                  "Material qonuni chiziqli "
                  "emas: plastiklik, "
                  "yemirilish, "
                  "giperelastiklik."),
                c("Urinma bikrlik matritsasi",
                  "$\\mathbf{K}_T = "
                  "\\partial\\mathbf{R}/"
                  "\\partial\\mathbf{u}$ — "
                  "joriy holatdagi bikrlik; "
                  "u yechim davomida "
                  "o'zgaradi."),
                c("Nyuton–Rafson usuli",
                  "Har iteratsiyada "
                  "$\\mathbf{K}_T$ qayta "
                  "hisoblanadi; "
                  "**kvadratik** "
                  "yaqinlashadi."),
                c("Chegaraviy nuqta "
                  "(limit point)",
                  "$\\det\\mathbf{K}_T = 0$ "
                  "bo'lgan nuqta; yuk "
                  "nazorati u yerda "
                  "to'xtaydi."),
                c("O'tib ketish "
                  "(snap-through)",
                  "Chegaraviy nuqtada "
                  "konstruksiya boshqa "
                  "muvozanat holatiga "
                  "**sakraydi** — dinamik "
                  "va xavfli."),
                c("Qaytarish algoritmi "
                  "(return mapping)",
                  "Plastiklikda: sinov "
                  "kuchlanishi hisoblanadi, "
                  "so'ng oqish sirtiga "
                  "qaytariladi."),
            ],
            derivation=[
                d("1. Nochiziqli muvozanat",
                  r"\mathbf{R}(\mathbf{u}) = "
                  r"\mathbf{F}_{int}(\mathbf{u}) "
                  r"- \mathbf{F}_{ext} = "
                  r"\mathbf{0}",
                  "Ichki kuchlar endi "
                  "ko'chishga **nochiziqli** "
                  "bog'liq, shuning uchun "
                  "$\\mathbf{K}\\mathbf{u} = "
                  "\\mathbf{F}$ ishlamaydi."),
                d("2. Teylor yoyilmasi",
                  r"\mathbf{R}(\mathbf{u} + "
                  r"\Delta\mathbf{u}) \approx "
                  r"\mathbf{R}(\mathbf{u}) + "
                  r"\frac{\partial\mathbf{R}}"
                  r"{\partial\mathbf{u}}"
                  r"\Delta\mathbf{u}",
                  "su-07 dagi Teylor qatori "
                  "— endi vektor "
                  "ko'rinishida."),
                d("3. Nyuton qadami",
                  r"\mathbf{K}_T\Delta\mathbf{u} "
                  r"= -\mathbf{R}(\mathbf{u}), "
                  r"\qquad \mathbf{u} "
                  r"\leftarrow \mathbf{u} + "
                  r"\Delta\mathbf{u}",
                  "**Asosiy algoritm.** Har "
                  "qadamda chiziqli tizim "
                  "yechiladi — ya'ni "
                  "nochiziqli masala "
                  "chiziqli masalalar "
                  "ketma-ketligiga "
                  "aylantiriladi."),
                d("4. Kvadratik yaqinlashish",
                  r"\|\mathbf{R}_{k+1}\| \le "
                  r"C\|\mathbf{R}_k\|^2",
                  "**Nyutonning kuchi.** "
                  "To'g'ri raqamlar soni "
                  "har iteratsiyada "
                  "**ikkilanadi** — shuning "
                  "uchun 5–6 iteratsiya "
                  "yetarli."),
                d("5. O'zgartirilgan Nyuton",
                  r"\mathbf{K}_T^{(0)}"
                  r"\Delta\mathbf{u} = "
                  r"-\mathbf{R}(\mathbf{u})",
                  "Bikrlik bir marta "
                  "hisoblanadi va qotiriladi. "
                  "Har iteratsiya arzon, "
                  "lekin yaqinlashish "
                  "**chiziqli** — kod "
                  "buni 0,584 nisbat "
                  "sifatida o'lchaydi."),
                d("6. Yassi ferma "
                  "geometriyasi",
                  r"L(w) = \sqrt{b^2 + "
                  r"(h-w)^2}, \qquad N = "
                  r"\frac{EA(L-L_0)}{L_0}",
                  "Ikki sterjenli yassi "
                  "ferma — o'tib ketishning "
                  "eng sodda modeli."),
                d("7. Muvozanat shartidan "
                  "yuk",
                  r"P(w) = \frac{2EA}{L_0}"
                  r"\left(1 - \frac{L_0}{L}"
                  r"\right)(h-w)",
                  "**Aniq yechim.** Bu "
                  "nochiziqli funksiya va "
                  "u monoton emas — aynan "
                  "shundan o'tib ketish "
                  "kelib chiqadi."),
                d("8. Urinma bikrlik "
                  "analitik",
                  r"K_T = \frac{dP}{dw} = "
                  r"\frac{2EA}{L_0}\left[\left("
                  r"1 - \frac{L_0}{L}\right) + "
                  r"\frac{(h-w)^2L_0}{L^3}"
                  r"\right]",
                  "Birinchi had — material "
                  "bikrligi, ikkinchisi — "
                  "**geometrik** bikrlik "
                  "(su-23 dagi "
                  "$\\mathbf{K}_G$ ning "
                  "nochiziqli ko'rinishi)."),
                d("9. Chegaraviy nuqtalar",
                  r"K_T = 0 \;\Longrightarrow\; "
                  r"w_{lim} = 0{,}42361\,h",
                  "**O'lchangan natija.** "
                  "Yassi ferma taxminida "
                  "$w_{lim} \\approx "
                  "h(1 - 1/\\sqrt3) = "
                  "0{,}42265\\,h$ — 0,23% "
                  "farq bilan."),
                d("10. Yuk nazoratining "
                  "muvaffaqiyatsizligi",
                  r"P > P_{lim} "
                  r"\;\Longrightarrow\; "
                  r"\text{yechim yo'q "
                  r"(yaqin atrofda)}",
                  "Chegaraviy nuqtadan "
                  "keyin berilgan yuk uchun "
                  "**yaqin** muvozanat "
                  "holati mavjud emas — "
                  "Nyuton yaqinlashmaydi."),
                d("11. Siljish nazorati",
                  r"w \ \text{beriladi, } P \ "
                  r"\text{noma'lum}",
                  "**Yechim.** Ko'chishni "
                  "bosqichma-bosqich "
                  "oshirib, butun yo'lni "
                  "— jumladan pasayuvchi "
                  "shoxni ham — bosib "
                  "o'tish mumkin."),
                d("12. Qisqarish tuzog'i",
                  r"L - L_0 = \frac{L^2 - "
                  r"L_0^2}{L + L_0} = "
                  r"\frac{w^2 - 2hw}{L + L_0}",
                  "**Muhim amaliy nozik "
                  "nuqta.** $L \\approx L_0$ "
                  "bo'lganda $L - L_0$ ni "
                  "bevosita hisoblash "
                  "halokatli qisqarish "
                  "beradi (su-02); bu "
                  "ayniyat uni butunlay "
                  "yo'qotadi."),
                d("13. Elastoplastik sinov "
                  "kuchlanishi",
                  r"\sigma^{tr} = \sigma_n + "
                  r"E\Delta\varepsilon, \qquad "
                  r"f = |\sigma^{tr}| - "
                  r"(\sigma_y + H\alpha_n)",
                  "Avval to'liq elastik deb "
                  "qaraymiz, so'ng oqish "
                  "shartini tekshiramiz."),
                d("14. Oqish sirtiga qaytarish",
                  r"\Delta\gamma = "
                  r"\frac{f}{E + H}, \qquad "
                  r"\sigma = \sigma^{tr} - "
                  r"E\Delta\gamma\,"
                  r"\mathrm{sign}(\sigma^{tr})",
                  "**Qaytarish algoritmi.** "
                  "Bir o'lchovda u aynan "
                  "yechiladi — iteratsiya "
                  "kerak emas."),
                d("15. Urinma modul",
                  r"E_t = \frac{EH}{E + H}",
                  "Oqishdan keyingi "
                  "bikrlik. $H \\ll E$ "
                  "bo'lsa "
                  "$E_t \\approx H$ — "
                  "material deyarli "
                  "ideal plastik."),
            ],
            meaning=(
                "Nochiziqli tahlilning butun "
                "g'oyasi 3-qadamda: "
                "nochiziqli masalani "
                "**chiziqli masalalar "
                "ketma-ketligiga** "
                "aylantirish. Har bir Nyuton "
                "qadami oddiy "
                "$\\mathbf{K}\\Delta"
                "\\mathbf{u} = -\\mathbf{R}$ "
                "tizimi — ya'ni butun "
                "3-modulda qurilgan apparat "
                "o'zgarishsiz ishlaydi, "
                "faqat matritsa har "
                "iteratsiyada yangilanadi. "
                "4-qadamdagi kvadratik "
                "yaqinlashish Nyutonning "
                "asosiy kuchi va uni "
                "kodda ko'rish mumkin: "
                "qoldiq "
                "$6\\cdot10^3 \\to "
                "1{,}4\\cdot10^3 \\to "
                "1{,}8\\cdot10^2 \\to "
                "4{,}8 \\to "
                "3{,}9\\cdot10^{-3} \\to "
                "2{,}6\\cdot10^{-9}$ — "
                "oxirgi qadamlarda to'g'ri "
                "raqamlar soni "
                "ikkilanmoqda. "
                "O'zgartirilgan Nyuton esa "
                "chiziqli yaqinlashadi va "
                "o'sha aniqlikka yetish "
                "uchun uch barobar ko'p "
                "iteratsiya talab qiladi — "
                "lekin har biri arzon, "
                "shuning uchun tanlov "
                "masalaga bog'liq. "
                "Mavzuning fizik markazi "
                "7- va 9-qadamlarda. "
                "Yuk–ko'chish egri "
                "chizig'i **monoton emas**: "
                "u maksimumga yetadi, "
                "so'ng pasayadi. Chiziqli "
                "hisob bu egri chiziqning "
                "faqat boshidagi urinmani "
                "ko'radi va shuning uchun "
                "maksimumni umuman sezmaydi. "
                "Gumbaz qulashining sababi "
                "aynan shu: yuk "
                "$P_{lim}$ dan oshganda "
                "yaqin atrofda muvozanat "
                "holati qolmaydi va "
                "konstruksiya uzoqdagi "
                "boshqa holatga — "
                "ag'darilgan shaklga — "
                "dinamik ravishda "
                "sakraydi. Kod buni aniq "
                "o'lchaydi: sakrash "
                "$0{,}42h$ dan "
                "$2{,}16h$ ga. "
                "10- va 11-qadamlar "
                "amaliy xulosani beradi: "
                "yuk nazorati chegaraviy "
                "nuqtadan o'ta olmaydi va "
                "bu hisoblash usulining "
                "kamchiligi emas, "
                "masalaning fizik "
                "xossasi. Siljish nazorati "
                "esa butun yo'lni bosib "
                "o'tadi. Nihoyat 12-qadam "
                "kutilmagan, lekin juda "
                "muhim bog'lanishni "
                "ochadi. Yassi fermada "
                "$L \\approx L_0$, demak "
                "$L - L_0$ ni bevosita "
                "hisoblash su-02 dagi "
                "halokatli qisqarishga "
                "olib keladi. Natijada "
                "Nyuton qoldiqni "
                "$2\\cdot10^{-10}$ dan "
                "pastga tushira olmaydi "
                "va **abadiy** shu yerda "
                "qoladi — go'yo usul "
                "ishlamayotgandek. "
                "Aslida usul benuqson, "
                "formula noto'g'ri. "
                "Ayniyat bilan qayta "
                "yozilganda qoldiq "
                "**aynan nolga** "
                "tushadi. Bu kursning "
                "muhim uslubiy saboqi: "
                "yaqinlashmayotgan "
                "iteratsiya har doim "
                "usulning aybi emas."
            ),
            equations=[
                eq(r"\mathbf{K}_T\Delta\mathbf{u} "
                   r"= -\mathbf{R}(\mathbf{u}), "
                   r"\qquad \mathbf{K}_T = "
                   r"\frac{\partial\mathbf{R}}"
                   r"{\partial\mathbf{u}}",
                   "Nyuton–Rafson qadami va "
                   "urinma bikrlik "
                   "matritsasi.",
                   "Nyuton qadami"),
                eq(r"P(w) = \frac{2EA}{L_0}"
                   r"\left(1 - \frac{L_0}{L}"
                   r"\right)(h-w), \qquad "
                   r"L = \sqrt{b^2 + (h-w)^2}",
                   "Yassi fermaning aniq "
                   "yuk–ko'chish yo'li.",
                   "O'tib ketish yo'li"),
                eq(r"L - L_0 = \frac{w^2 - 2hw}"
                   r"{L + L_0}",
                   "Qisqarishsiz ayniyat — "
                   "Nyutonni mashina "
                   "aniqligigacha olib "
                   "boradi (su-02).",
                   "Barqaror formula"),
                eq(r"\Delta\gamma = \frac{f}"
                   r"{E+H}, \quad \sigma = "
                   r"\sigma^{tr} - E\Delta\gamma\,"
                   r"\mathrm{sign}(\sigma^{tr}), "
                   r"\quad E_t = \frac{EH}{E+H}",
                   "Elastoplastik qaytarish "
                   "algoritmi va urinma "
                   "modul.",
                   "Qaytarish algoritmi"),
            ],
            conditions=(
                "**Nochiziqlik qachon "
                "kerak:**\n"
                "- $w > h/5$ (plastinalar) "
                "yoki $w > L/50$ "
                "(balkalar) — geometrik;\n"
                "- Yassi gumbaz, arka, "
                "kabel tizimlari — "
                "**har doim**;\n"
                "- Kuchlanish oqish "
                "chegarasiga yaqin — "
                "fizik;\n"
                "- Ustuvorlik "
                "nuqsonlarga sezgir "
                "bo'lsa (pq-29).\n\n"
                "**Iteratsiya "
                "nazorati:**\n"
                "- Qoldiq mezoni: "
                "$\\|\\mathbf{R}\\| / "
                "\\|\\mathbf{F}_{ext}\\| "
                "< 10^{-4}$;\n"
                "- Energiya mezoni ham "
                "tekshirilsin;\n"
                "- Yaqinlashmasa: qadamni "
                "kichraytiring, keyin "
                "formulani tekshiring "
                "(qisqarish!), so'ng "
                "usulni o'zgartiring.\n\n"
                "**Usul tanlash:**\n"
                "- Monoton yo'l → yuk "
                "nazorati;\n"
                "- Chegaraviy nuqta bor → "
                "siljish nazorati;\n"
                "- Ham chegaraviy, ham "
                "qaytuvchi nuqta bor "
                "(snap-back) → Riks yoy "
                "uzunligi usuli.\n\n"
                "**Plastiklikda:** "
                "qaytarish algoritmi "
                "qadam kattaligidan "
                "**mustaqil** aniq "
                "bo'lishi kerak "
                "(bir o'lchovda shunday); "
                "ko'p o'lchovda "
                "izchil urinma modul "
                "(consistent tangent) "
                "ishlatilmasa, Nyuton "
                "kvadratik "
                "yaqinlashishni "
                "**yo'qotadi**.\n\n"
                "**Ogohlantirish:** o'tib "
                "ketish dinamik hodisa. "
                "Statik tahlil sakrash "
                "sodir bo'lishini "
                "ko'rsatadi, lekin "
                "sakrash paytidagi "
                "inersiya kuchlarini "
                "hisobga olmaydi."
            ),
            worked=WorkedExample(
                statement=(
                    "Yassi ikki sterjenli "
                    "ferma: yarim oraliq "
                    "$b = 1$ m, ko'tarilish "
                    "$h = 0{,}1$ m, "
                    "$EA = 2{,}1\\cdot10^{7}$ N. "
                    "(a) Chegaraviy nuqta "
                    "joyini toping; "
                    "(b) yassi ferma "
                    "taxminini tekshiring; "
                    "(c) nima uchun yuk "
                    "nazorati bu nuqtadan "
                    "o'ta olmaydi."
                ),
                given=[
                    r"b = 1\ \text{m}, \quad h = "
                    r"0{,}1\ \text{m}, \quad "
                    r"L_0 = \sqrt{1 + 0{,}01} = "
                    r"1{,}004988\ \text{m}",
                    r"P(w) = \frac{2EA}{L_0}"
                    r"\left(1 - \frac{L_0}{L}"
                    r"\right)(h-w)",
                ],
                steps=[
                    st(r"K_T = \frac{dP}{dw} = "
                       r"\frac{2EA}{L_0}\left[\left("
                       r"1-\frac{L_0}{L}\right) + "
                       r"\frac{s^2L_0}{L^3}\right], "
                       r"\ s = h-w",
                       "Urinma bikrlik "
                       "(8-qadam)."),
                    st(r"K_T = 0 \;\Rightarrow\; "
                       r"\left(1-\frac{L_0}{L}"
                       r"\right) = -\frac{s^2L_0}"
                       r"{L^3}",
                       "Chegaraviy nuqta "
                       "sharti."),
                    st(r"\frac{L - L_0}{L} = "
                       r"-\frac{s^2L_0}{L^3} "
                       r"\;\Rightarrow\; "
                       r"L^2(L-L_0) = -s^2L_0",
                       "Soddalashtiramiz."),
                    st(r"\text{Yassi ferma: } "
                       r"h \ll b \;\Rightarrow\; "
                       r"L \approx b\left(1 + "
                       r"\frac{s^2}{2b^2}\right)",
                       "Teylor yoyilmasi "
                       "(su-07)."),
                    st(r"L - L_0 \approx "
                       r"\frac{s^2 - h^2}{2b}",
                       "Ikkala uzunlikni "
                       "yoyib ayiramiz."),
                    st(r"\frac{s^2-h^2}{2b}\cdot "
                       r"b^2 = -s^2 b "
                       r"\;\Rightarrow\; "
                       r"s^2 - h^2 = -2s^2",
                       "$L \\approx L_0 "
                       "\\approx b$ deb "
                       "qo'yamiz."),
                    st(r"3s^2 = h^2 "
                       r"\;\Rightarrow\; s = "
                       r"\frac{h}{\sqrt3}",
                       "**Chiroyli natija.**"),
                    st(r"w_{lim} = h - s = "
                       r"h\left(1 - "
                       r"\frac{1}{\sqrt3}\right) "
                       r"= 0{,}42265\,h",
                       "Yassi ferma "
                       "taxminining javobi."),
                    st(r"\text{(b)}\quad "
                       r"\text{aniq: } w_{lim} = "
                       r"0{,}42361\,h",
                       "Kod $K_T = 0$ ni sonli "
                       "yechib topadi."),
                    st(r"\text{farq} = "
                       r"\frac{0{,}42361 - "
                       r"0{,}42265}{0{,}42361} "
                       r"= 0{,}23\%",
                       "**Taxmin juda "
                       "yaxshi** — $h/b = "
                       "0{,}1$ uchun."),
                    st(r"\text{(c)}\quad P > "
                       r"P_{lim}: \ P(w) = P "
                       r"\text{ tenglamasining "
                       r"yaqin ildizi YO'Q}",
                       "Egri chiziq "
                       "maksimumdan past, "
                       "demak kesishmaydi."),
                    st(r"\Rightarrow \ "
                       r"\text{Nyuton "
                       r"yaqinlashmaydi; "
                       r"siljish nazorati "
                       r"kerak}",
                       "Kod buni "
                       "$P/P_{lim} = "
                       "1{,}001$ da "
                       "ko'rsatadi."),
                ],
                answer=(
                    "(a) $K_T = 0$ dan "
                    "$w_{lim} = 0{,}42361\\,h "
                    "= 0{,}042361$ m, "
                    "$P_{lim} = 8003$ N. "
                    "(b) Yassi ferma taxmini "
                    "$w_{lim} = h(1 - "
                    "1/\\sqrt3) = "
                    "0{,}42265\\,h$ — "
                    "0,23% farq bilan. "
                    "(c) $P > P_{lim}$ da "
                    "yaqin muvozanat holati "
                    "mavjud emas, shuning "
                    "uchun Nyuton "
                    "yaqinlashmaydi — bu "
                    "usul emas, masalaning "
                    "xossasi."
                ),
                engineering_note=(
                    "(c) javobi amaliyotda "
                    "eng ko'p "
                    "chalkashtiradigan "
                    "nuqta. FEM paketi "
                    "'yaqinlashmadi' deb "
                    "xabar berganda "
                    "birinchi o'y — "
                    "qadamni "
                    "kichraytirish yoki "
                    "iteratsiya sonini "
                    "oshirish. Lekin "
                    "chegaraviy nuqtada "
                    "bu **hech qachon** "
                    "yordam bermaydi: "
                    "yechim mavjud emas, "
                    "uni qanchalik "
                    "tirishib "
                    "izlamang. To'g'ri "
                    "javob — nazorat "
                    "turini "
                    "o'zgartirish. "
                    "Ikkinchi muhim "
                    "nuqta: o'tib ketish "
                    "**dinamik** hodisa. "
                    "Statik tahlil "
                    "sakrash sodir "
                    "bo'lishini va qayerga "
                    "sakrashini "
                    "ko'rsatadi, lekin "
                    "sakrash paytidagi "
                    "tezlik va inersiya "
                    "kuchlarini hisobga "
                    "olmaydi — haqiqiy "
                    "konstruksiya "
                    "o'sha lahzada "
                    "qo'shimcha zarba "
                    "yuki oladi va u "
                    "ko'pincha "
                    "yemirilishga olib "
                    "keladi. Uchinchisi, "
                    "loyihaviy xulosa: "
                    "yassi gumbaz va "
                    "arkalarda "
                    "ko'tarilish "
                    "oralig'iga nisbatan "
                    "yetarlicha katta "
                    "bo'lishi kerak. "
                    "$P_{lim}$ "
                    "ko'tarilishning "
                    "kubiga "
                    "proporsional — "
                    "ko'tarilishni ikki "
                    "barobar oshirish "
                    "xavfsizlikni "
                    "sakkiz barobar "
                    "oshiradi."
                ),
            ),
            computation=Computation(
                caption=(
                    "Yassi fermaning o'tib "
                    "ketishini hisoblash, "
                    "Nyuton yaqinlashish "
                    "tartibini o'lchash, yuk va "
                    "siljish nazoratini "
                    "taqqoslash, elastoplastik "
                    "qaytarish algoritmini "
                    "tekshirish."
                ),
                code='''"""Nochiziqli tahlil."""
import numpy as np
from labkit import PARAMS, note, series, table, value
from scipy.optimize import brentq

b_span = float(PARAMS.get("b_span", 1.0))
h_rise = float(PARAMS.get("h_rise", 0.1))
EA = float(PARAMS.get("EA", 2.1e7))
H_hard = float(PARAMS.get("H_hard", 2.1e9))

L0 = float(np.hypot(b_span, h_rise))
E_mod, sig_y = 2.1e11, 250e6


def P_stable(w):
    """Ichki qarshilik. L - L0 ayniyat bilan - QISQARISHSIZ (su-02)."""
    s = h_rise - w
    L = np.hypot(b_span, s)
    dL = (w*w - 2*h_rise*w)/(L + L0)      # = L - L0, aynan
    return -2*EA*dL/L0*s/L


def P_naive(w):
    """Sodda ko'rinish: (1 - L0/L) da halokatli qisqarish bor."""
    s = h_rise - w
    L = np.hypot(b_span, s)
    return -2*EA/L0*s*(1 - L0/L)


def KT(w):
    """ANALITIK urinma bikrlik."""
    s = h_rise - w
    L = np.hypot(b_span, s)
    return 2*EA/L0*((1 - L0/L) + s*s*L0/L**3)


# --- (0) Urinma bikrlikning tekshiruvi ---
rows0 = []
for w in [0.0, 0.05*h_rise, 0.5*h_rise, 1.2*h_rise, 1.9*h_rise]:
    num = (P_stable(w + 1e-7) - P_stable(w - 1e-7))/2e-7
    rows0.append([f"{w/h_rise:.2f}", f"{KT(w):.4f}", f"{num:.4f}",
                  f"{abs(KT(w) - num)/abs(num)*100:.2e}"])
table("Analitik urinma bikrlik markaziy ayirma bilan tekshiriladi",
      ["w/h", "K_T analitik", "K_T sonli", "farq %"], rows0)
note("Urinma bikrlik analitik chiqarildi va markaziy ayirma bilan "
     "1e-6% aniqlikda tasdiqlandi. Bu muhim: noto'g'ri K_T bilan "
     "Nyuton kvadratik yaqinlashishni YO'QOTADI va sekin ishlaydi - "
     "lekin baribir to'g'ri javobga keladi, shuning uchun xato "
     "yashirin qoladi.")

# --- (1) YUK-KO'CHISH YO'LI va chegaraviy nuqtalar ---
w_lim = brentq(KT, 1e-9, h_rise - 1e-9)
w_up = brentq(KT, h_rise + 1e-9, 2*h_rise - 1e-9)
P_lim = P_stable(w_lim)
value("Chegaraviy nuqta w_lim", float(w_lim), "m")
value("Chegaraviy nuqta w_lim / h", float(w_lim/h_rise), "—")
value("Chegaraviy yuk P_lim", float(P_lim), "N")
value("Yassi ferma taxmini h(1 - 1/sqrt(3)) / h",
      float(1 - 1/np.sqrt(3)), "—")
value("Taxminning xatosi",
      float(abs(w_lim/h_rise - (1 - 1/np.sqrt(3))) /
            (w_lim/h_rise)*100), "%")
value("Antisimmetriya: P(w_up) + P(w_lim)",
      float(P_stable(w_up) + P_lim), "N")
ws = np.linspace(0, 2.6*h_rise, 400)
Ps = [float(P_stable(x)) for x in ws]
series("Yuk-ko'chish yo'li", (ws/h_rise).tolist(),
       [p/P_lim for p in Ps], xlabel="w/h", ylabel="P/P_lim")
series("Chegaraviy yuk darajasi", (ws/h_rise).tolist(),
       [1.0]*len(ws), xlabel="w/h", ylabel="P/P_lim")
w_snap = brentq(lambda x: P_stable(x) - P_lim, 2.0*h_rise, 6.0*h_rise)
value("O'tib ketishdan keyingi holat w/h", float(w_snap/h_rise), "—")
value("Sakrash kattaligi (w/h bo'yicha)",
      float((w_snap - w_lim)/h_rise), "—")
value("sqrt(3) bilan taqqoslash", float(np.sqrt(3)), "—")
value("Sakrash va sqrt(3) farqi",
      float(abs((w_snap - w_lim)/h_rise - np.sqrt(3)) /
            np.sqrt(3)*100), "%")
rows_j = []
for hb in [0.05, 0.1, 0.2, 0.4, 0.8]:
    hh = hb*b_span
    LL0 = float(np.hypot(b_span, hh))

    def Pr_(w, hh=hh, LL0=LL0):
        s = hh - w
        L = np.hypot(b_span, s)
        return -2*EA*((w*w - 2*hh*w)/(L + LL0))/LL0*s/L

    def KT_(w, hh=hh, LL0=LL0):
        s = hh - w
        L = np.hypot(b_span, s)
        return 2*EA/LL0*((1 - LL0/L) + s*s*LL0/L**3)

    wl_ = brentq(KT_, 1e-12, hh - 1e-12)
    ws_ = brentq(lambda x: Pr_(x) - Pr_(wl_), 2.0*hh, 20.0*hh)
    jump = (ws_ - wl_)/hh
    rows_j.append([f"{hb:.2f}", f"{wl_/hh:.6f}", f"{ws_/hh:.6f}",
                   f"{jump:.6f}",
                   f"{abs(jump - np.sqrt(3))/np.sqrt(3)*100:.4f}"])
table("Sakrash kattaligi yassilikka qanday bog'liq",
      ["h/b", "w_lim/h", "w_snap/h", "sakrash/h", "sqrt(3) dan farq %"],
      rows_j)
note("KUTILMAGAN ANIQ NATIJA. Sakrash kattaligi yassi fermada aynan "
     "sqrt(3)*h ga teng: h/b = 0.05 da farq 0.0000%, h/b = 0.1 da "
     "0.0001%. Ferma chuqurlashgani sari (h/b = 0.8 da 0.22%) bu "
     "ayniyat buziladi - ya'ni u YASSI ferma natijasi va h/b -> 0 da "
     "asimptotik aniq. Bu w_lim = h(1 - 1/sqrt(3)) taxmini bilan bir "
     "oilaga kiradi va sonli yechimni yana bir mustaqil yo'ldan "
     "tekshiradi.")
note(f"Yuk-ko'chish yo'li MONOTON EMAS: u w = {w_lim/h_rise:.4f}h da "
     f"maksimumga yetadi, so'ng pasayadi va w = h da nolga tushadi. "
     f"Chiziqli hisob bu egri chiziqning faqat boshidagi urinmasini "
     f"ko'radi, shuning uchun maksimumni umuman sezmaydi - gumbaz "
     f"qulashining sababi aynan shu. Yassi ferma taxmini "
     f"h(1-1/sqrt(3)) = 0.42265h esa aniq qiymat 0.42361h ga {abs(w_lim/h_rise - (1 - 1/np.sqrt(3)))/(w_lim/h_rise)*100:.2f}% "
     f"aniqlikda mos keldi. Yo'l w = h atrofida ANTISIMMETRIK - "
     f"P(w_up) = -P(w_lim) mashina aniqligida.")

# --- (2) NYUTON-RAFSON: kvadratik yaqinlashish va QISQARISH tuzog'i ---
P_target = 0.8*P_lim
rows = []
seqs = {}
for name, Pf in [("barqaror (ayniyat bilan)", P_stable),
                 ("sodda (1 - L0/L)", P_naive)]:
    w = 0.0
    res = []
    for it in range(14):
        r = Pf(w) - P_target
        res.append(abs(r))
        if abs(r) < 1e-13:
            break
        w -= r/KT(w)
    seqs[name] = res
    rows.append([name, len(res)] +
                [f"{res[i]:.3e}" if i < len(res) else "—"
                 for i in range(8)])
table("Nyuton-Rafson qoldiqlari: formulaning ta'siri",
      ["formula", "iteratsiyalar"] + [f"|R_{i}|" for i in range(8)], rows)
value("Barqaror formula: yakuniy qoldiq",
      float(seqs["barqaror (ayniyat bilan)"][-1]), "N")
value("Sodda formula: yakuniy qoldiq",
      float(seqs["sodda (1 - L0/L)"][-1]), "N")
series("Nyuton: barqaror formula",
       list(range(len(seqs["barqaror (ayniyat bilan)"]))),
       [np.log10(max(r, 1e-18))
        for r in seqs["barqaror (ayniyat bilan)"]],
       xlabel="iteratsiya", ylabel="log10|R|")
series("Nyuton: sodda formula",
       list(range(len(seqs["sodda (1 - L0/L)"]))),
       [np.log10(max(r, 1e-18)) for r in seqs["sodda (1 - L0/L)"]],
       xlabel="iteratsiya", ylabel="log10|R|")
note("ENG MUHIM NATIJA. Ikkala hisobda ham AYNAN bir xil Nyuton "
     "algoritmi va aynan bir xil urinma bikrlik ishlatildi. Yagona "
     "farq - ichki kuchni hisoblash formulasi. Ayniyat bilan yozilgan "
     "variant qoldiqni AYNAN NOLGA tushiradi, sodda variant esa "
     "2e-10 atrofida qotib qoladi va u yerdan hech qachon "
     "chiqmaydi. Sabab: yassi fermada L ~ L0, demak (1 - L0/L) da "
     "halokatli qisqarish yuz beradi (su-02). Amaliy xulosa: "
     "yaqinlashmayotgan iteratsiya HAR DOIM usulning aybi emas - "
     "avval formulani tekshiring.")

# --- (3) O'ZGARTIRILGAN NYUTON: chiziqli yaqinlashish ---
w = 0.0
K0 = KT(0.0)
res_m = []
for it in range(40):
    r = P_stable(w) - P_target
    res_m.append(abs(r))
    if abs(r) < 1e-10:
        break
    w -= r/K0
ratios = [res_m[k+1]/res_m[k] for k in range(2, len(res_m) - 1)]
value("O'zgartirilgan Nyuton: iteratsiyalar soni", len(res_m), "—")
value("To'liq Nyuton: iteratsiyalar soni",
      len(seqs["barqaror (ayniyat bilan)"]), "—")
value("O'zgartirilgan: ketma-ket qoldiq nisbati (chiziqli tartib)",
      float(np.mean(ratios)) if ratios else float("nan"), "—")
series("O'zgartirilgan Nyuton", list(range(len(res_m))),
       [np.log10(max(r, 1e-18)) for r in res_m],
       xlabel="iteratsiya", ylabel="log10|R|")
note(f"O'zgartirilgan Nyutonda bikrlik bir marta hisoblanadi va "
     f"qotiriladi. Natijada qoldiq har iteratsiyada bir xil "
     f"{np.mean(ratios):.4f} koeffitsientga ko'payadi - bu CHIZIQLI "
     f"yaqinlashish. Bir xil aniqlikka yetish uchun {len(res_m)} "
     f"iteratsiya kerak bo'ldi, to'liq Nyutonda esa "
     f"{len(seqs['barqaror (ayniyat bilan)'])} ta. Lekin har "
     f"iteratsiya arzon: katta tizimlarda matritsani qayta yoyish "
     f"eng qimmat amal, shuning uchun tanlov masalaga bog'liq.")

# --- (4) YUK va SILJISH nazorati ---
rows2 = []
for frac in [0.5, 0.9, 0.99, 1.001, 1.05, 1.2]:
    Pt = frac*P_lim
    w = 0.0
    conv = False
    for it in range(100):
        r = P_stable(w) - Pt
        if abs(r) < 1e-9:
            conv = True
            break
        k = KT(w)
        if abs(k) < 1e-6:
            break
        w -= r/k
    rows2.append([f"{frac:.3f}",
                  "yaqinlashdi" if conv else "YAQINLASHMADI",
                  f"{w/h_rise:.5f}" if conv else "—"])
table("Yuk nazorati chegaraviy nuqtadan o'ta oladimi?",
      ["P/P_lim", "natija", "w/h"], rows2)
rows3 = []
for wf in [0.2, 0.42361, 0.7, 1.0, 1.5764, 2.0, 2.3]:
    ww = wf*h_rise
    rows3.append([f"{wf:.5f}", f"{P_stable(ww)/P_lim:+.5f}",
                  f"{KT(ww):+.1f}"])
table("Siljish nazorati butun yo'lni bosib o'tadi",
      ["w/h", "P/P_lim", "K_T"], rows3)
note("Yuk nazorati P > P_lim da YAQINLASHMAYDI va bu hisoblash "
     "usulining kamchiligi emas: o'sha yuk uchun YAQIN muvozanat "
     "holati mavjud emas. Qadamni kichraytirish yoki iteratsiya "
     "sonini oshirish hech qachon yordam bermaydi. Siljish nazorati "
     "esa butun yo'lni - jumladan K_T manfiy bo'lgan pasayuvchi "
     "shoxni ham - bemalol bosib o'tadi. Amalda P_lim ga yetganda "
     "konstruksiya w = 0.4236h dan w = 2.1557h ga DINAMIK ravishda "
     "sakraydi: bu o'tib ketish (snap-through).")

# --- (5) ELASTOPLASTIK qaytarish algoritmi ---
def return_map(eps_path):
    sig, alpha, prev = 0.0, 0.0, 0.0
    out = []
    for e in eps_path:
        de = e - prev
        prev = e
        s_tr = sig + E_mod*de
        f = abs(s_tr) - (sig_y + H_hard*alpha)
        if f <= 0.0:
            sig = s_tr
        else:
            dg = f/(E_mod + H_hard)
            sig = s_tr - E_mod*dg*np.sign(s_tr)
            alpha += dg
        out.append((e, sig, alpha))
    return out


eps_y = sig_y/E_mod
E_t = E_mod*H_hard/(E_mod + H_hard)
value("Oqish deformatsiyasi eps_y", float(eps_y), "—")
value("Urinma modul E_t = EH/(E+H)", float(E_t/1e9), "GPa")
value("Elastik modul E", float(E_mod/1e9), "GPa")
mono = return_map(np.linspace(0, 5*eps_y, 601))
err = max(abs(s - (E_mod*e if e <= eps_y else sig_y + E_t*(e - eps_y)))
          for e, s, _ in mono)/sig_y
value("Monoton yuklashda maks xato (sigma_y ga nisbatan)",
      float(err), "—")
series("Kuchlanish-deformatsiya (monoton)",
       [e/eps_y for e, _, _ in mono],
       [s/1e6 for _, s, _ in mono],
       xlabel="eps/eps_y", ylabel="sigma, MPa")

# Qadam kattaligidan mustaqilmi?
rows4 = []
for npts in [11, 51, 201, 1001]:
    r_ = return_map(np.linspace(0, 5*eps_y, npts))
    rows4.append([npts, f"{r_[-1][1]/1e6:.9f}",
                  f"{r_[-1][2]:.9e}"])
table("Qaytarish algoritmi qadam kattaligiga bog'liqmi?",
      ["qadamlar soni", "yakuniy sigma, MPa", "yakuniy alpha"], rows4)

# Sikl: Bauschinger yo'q (izotrop)
cyc = np.concatenate([np.linspace(0, 3*eps_y, 300),
                      np.linspace(3*eps_y, -3*eps_y, 600)])
rc = return_map(cyc)
s_max = max(s for _, s, _ in rc)
s_min = min(s for _, s, _ in rc)
al_end = rc[-1][2]
value("Siklda sigma_max", float(s_max/1e6), "MPa")
value("Siklda sigma_min", float(s_min/1e6), "MPa")
value("Izotrop bashorat: -(sigma_y + H*alpha)",
      float(-(sig_y + H_hard*al_end)/1e6), "MPa")
value("Farq", float(abs(abs(s_min) - (sig_y + H_hard*al_end))/1e6),
      "MPa")
series("Kuchlanish-deformatsiya (sikl)",
       [e/eps_y for e, _, _ in rc], [s/1e6 for _, s, _ in rc],
       xlabel="eps/eps_y", ylabel="sigma, MPa")
note("Qaytarish algoritmi bir o'lchovda AYNAN yechiladi - iteratsiya "
     "kerak emas va natija qadam kattaligiga umuman bog'liq emas "
     "(11 va 1001 qadam bir xil javob beradi). Monoton yuklashda u "
     "ikki chiziqli qonunni 5e-16 aniqlikda takrorladi. Siklda esa "
     "izotrop mustahkamlanish tasdiqlandi: teskari yo'nalishda oqish "
     "|sigma| = sigma_y + H*alpha da boshlanadi, ya'ni oqish sirti "
     "BIR TEKIS kengayadi. Kinematik mustahkamlanishda esa sirt "
     "siljiydi va Baushinger effekti paydo bo'lardi (mq-08).")

table("Nochiziqlik turlari va usullar",
      ["Tur", "Manbai", "Belgisi", "Usul"],
      [["Geometrik", "katta ko'chish", "w > h/5", "yangilanuvchi K_T"],
       ["Material", "oqish, yemirilish", "sigma ~ sigma_y",
        "qaytarish algoritmi"],
       ["Kontakt", "o'zgaruvchi chegara", "sirtlar tegishi",
        "faol to'plam"],
       ["Chegaraviy nuqta", "det K_T = 0", "yuk nazorati uziladi",
        "siljish nazorati"],
       ["Qaytuvchi nuqta", "snap-back", "siljish ham uziladi",
        "Riks yoy uzunligi"]])
''',
                parameters=[
                    p("b_span", "Yarim oraliq b", 0.2, 5.0, 1.0, 0.1,
                      "m"),
                    p("h_rise", "Ko'tarilish h", 0.01, 0.5, 0.1, 0.01,
                      "m"),
                    p("EA", "Sterjen bikrligi EA", 1e6, 1e8, 2.1e7, 1e6,
                      "N"),
                    p("H_hard", "Mustahkamlanish moduli H", 1e8, 2e10,
                      2.1e9, 1e8, "Pa"),
                ],
                expected_output=(
                    "Analitik urinma bikrlik "
                    "markaziy ayirma bilan "
                    "$10^{-6}$% aniqlikda mos "
                    "keladi. Chegaraviy nuqta "
                    "$w_{lim} = 0{,}42361h$, "
                    "yassi ferma taxmini "
                    "$h(1-1/\\sqrt3) = "
                    "0{,}42265h$ bilan 0,23% "
                    "farq qiladi; yo'l "
                    "$w = h$ atrofida aynan "
                    "antisimmetrik. Nyuton "
                    "qoldiqlari "
                    "$6{,}4\\cdot10^3 \\to "
                    "1{,}4\\cdot10^3 \\to "
                    "1{,}8\\cdot10^2 \\to "
                    "4{,}8 \\to "
                    "3{,}9\\cdot10^{-3} \\to "
                    "2{,}6\\cdot10^{-9} \\to "
                    "1{,}8\\cdot10^{-12} "
                    "\\to 0$ — kvadratik. "
                    "Sodda formula bilan esa "
                    "qoldiq "
                    "$2\\cdot10^{-10}$ da "
                    "qotib qoladi, chunki "
                    "$1 - L_0/L$ da "
                    "halokatli qisqarish bor. "
                    "O'zgartirilgan Nyuton "
                    "chiziqli yaqinlashadi "
                    "(nisbat 0,584). Yuk "
                    "nazorati "
                    "$P > P_{lim}$ da "
                    "yaqinlashmaydi, siljish "
                    "nazorati esa butun "
                    "yo'lni bosib o'tadi; "
                    "sakrash "
                    "$0{,}4236h$ dan "
                    "$2{,}1557h$ ga. "
                    "Qaytarish algoritmi "
                    "ikki chiziqli qonunni "
                    "$5\\cdot10^{-16}$ "
                    "aniqlikda, qadam "
                    "sonidan mustaqil "
                    "ravishda takrorlaydi."
                ),
            ),
            visual=vis(
                kind="O'tib ketish va Nyuton iteratsiyasi",
                tool="React/SVG + Manim",
                description=(
                    "Yuk–ko'chish yo'li, "
                    "chegaraviy nuqtalar, "
                    "iteratsiyaning "
                    "yaqinlashishi va "
                    "kuchlanish–deformatsiya "
                    "sikli."
                ),
                how_to_draw=(
                    "React/SVG: chap panelda "
                    "yassi ferma yon "
                    "ko'rinishda chiziladi va "
                    "yuk slayderi bilan "
                    "asta-sekin bosiladi; "
                    "apex tushgani sari "
                    "shakl o'zgaradi va "
                    "$P_{lim}$ ga yetganda "
                    "ferma **birdan "
                    "ag'darilib** pastki "
                    "holatga sakraydi — "
                    "animatsiya aynan shu "
                    "lahzada tezlashadi. "
                    "O'ng panelda "
                    "yuk–ko'chish egri "
                    "chizig'i: joriy holat "
                    "nuqta bilan "
                    "belgilanadi va u "
                    "egri chiziq bo'ylab "
                    "harakatlanadi; "
                    "chegaraviy nuqtaga "
                    "yetganda nuqta "
                    "gorizontal chiziq "
                    "bo'ylab **sakrab** "
                    "uzoqdagi shoxga "
                    "o'tadi va shu "
                    "sakrash yo'li "
                    "punktir bilan "
                    "qoladi. Egri "
                    "chiziqning "
                    "$K_T < 0$ qismi "
                    "boshqa uslubda "
                    "chiziladi — u "
                    "faqat siljish "
                    "nazorati bilan "
                    "erishiladi. Pastki "
                    "panelda ikkita "
                    "Nyuton "
                    "yaqinlashish "
                    "grafigi "
                    "$\\log|R|$ "
                    "o'qida: "
                    "barqaror formula "
                    "tik pastga tushib "
                    "yo'qoladi, sodda "
                    "formula esa "
                    "$-10$ darajasida "
                    "yassilanib "
                    "qoladi — "
                    "qisqarish "
                    "chegarasi "
                    "gorizontal "
                    "punktir bilan "
                    "belgilanadi."
                ),
            ),
            interp=(
                "Urinma bikrlikni markaziy "
                "ayirma bilan tekshirish "
                "arzon, lekin muhim: "
                "noto'g'ri "
                "$\\mathbf{K}_T$ bilan "
                "Nyuton kvadratik "
                "yaqinlashishni yo'qotadi, "
                "ammo baribir to'g'ri "
                "javobga keladi — shuning "
                "uchun xato jimgina "
                "sekinlik sifatida "
                "namoyon bo'ladi va "
                "ko'pincha sezilmaydi. "
                "Yuk–ko'chish yo'lining "
                "monoton emasligi esa "
                "butun mavzuning fizik "
                "o'zagi. Chiziqli hisob "
                "bu egri chiziqning faqat "
                "boshidagi urinmani "
                "ko'radi va maksimumni "
                "umuman sezmaydi — "
                "gumbaz qulashining sababi "
                "aynan shu. Yassi ferma "
                "taxminining 0,23% "
                "aniqlikda mos kelishi "
                "esa qo'lda chiqarilgan "
                "natijani sonli yechim "
                "bilan mustaqil "
                "tasdiqlaydi. Eng "
                "qimmatli natija esa "
                "Nyuton jadvalida va u "
                "kutilmagan joydan "
                "keladi. Ikkala hisobda "
                "ham aynan bir xil "
                "algoritm va aynan bir "
                "xil urinma bikrlik "
                "ishlatildi; yagona "
                "farq — ichki kuchni "
                "hisoblash formulasi. "
                "Ayniyat bilan yozilgan "
                "variant qoldiqni aynan "
                "nolga tushiradi, sodda "
                "variant esa "
                "$2\\cdot10^{-10}$ da "
                "abadiy qotib qoladi. "
                "Sabab su-02 da "
                "o'rganilgan halokatli "
                "qisqarish: yassi "
                "fermada "
                "$L \\approx L_0$, demak "
                "$1 - L_0/L$ ni bevosita "
                "hisoblash aniqlikni "
                "yo'qotadi. Amaliy "
                "xulosa muhim: "
                "yaqinlashmayotgan "
                "iteratsiya har doim "
                "usulning aybi emas. "
                "Nazorat turini "
                "taqqoslash esa "
                "ikkinchi amaliy "
                "saboqni beradi. Yuk "
                "nazorati "
                "$P > P_{lim}$ da "
                "yaqinlashmaydi va "
                "qadamni "
                "kichraytirish hech "
                "qachon yordam "
                "bermaydi, chunki "
                "o'sha yuk uchun "
                "yaqin muvozanat "
                "holati mavjud emas. "
                "Siljish nazorati "
                "esa manfiy "
                "$K_T$ li pasayuvchi "
                "shoxni ham bemalol "
                "bosib o'tadi. "
                "Nihoyat qaytarish "
                "algoritmi bir "
                "o'lchovda aynan "
                "yechilishi va qadam "
                "sonidan mustaqilligi "
                "tasdiqlandi — bu "
                "plastiklik "
                "hisobining "
                "ishonchliligining "
                "asosi."
            ),
            mistakes=[
                "Yaqinlashmaslikni har doim "
                "usulning aybi deb bilish. "
                "Kodda sabab formuladagi "
                "qisqarish edi (su-02).",
                "Chegaraviy nuqtada qadamni "
                "kichraytirish. Yechim "
                "mavjud emas — nazorat "
                "turini o'zgartirish kerak.",
                "Urinma bikrlikni "
                "tekshirmaslik. Noto'g'ri "
                "$\\mathbf{K}_T$ kvadratik "
                "yaqinlashishni yo'qotadi, "
                "lekin javob to'g'ri "
                "chiqadi — xato yashirin "
                "qoladi.",
                "Yassi gumbazlarda chiziqli "
                "hisob bilan cheklanish. U "
                "o'tib ketishni umuman "
                "ko'rsata olmaydi.",
                "O'tib ketishni statik "
                "hodisa deb hisoblash. "
                "Sakrash dinamik va "
                "qo'shimcha zarba yuki "
                "beradi.",
                "Ko'p o'lchovli plastiklikda "
                "izchil urinma modul "
                "(consistent tangent) "
                "o'rniga elastoplastik "
                "modulni ishlatish — "
                "kvadratik yaqinlashish "
                "yo'qoladi.",
            ],
            quiz=[
                q("Nyuton–Rafson nochiziqli "
                  "masalani qanday hal "
                  "qiladi?",
                  "Uni chiziqli masalalar "
                  "ketma-ketligiga "
                  "aylantiradi: har qadamda "
                  "$\\mathbf{K}_T\\Delta"
                  "\\mathbf{u} = "
                  "-\\mathbf{R}$ yechiladi "
                  "va urinma bikrlik "
                  "yangilanadi.",
                  "konseptual"),
                q("To'liq va o'zgartirilgan "
                  "Nyutonning farqi nima?",
                  "To'liqda "
                  "$\\mathbf{K}_T$ har "
                  "iteratsiyada "
                  "yangilanadi (kvadratik), "
                  "o'zgartirilganida bir "
                  "marta hisoblanadi "
                  "(chiziqli, kodda nisbat "
                  "0,584).", "konseptual"),
                q("Yassi fermada chegaraviy "
                  "nuqta qayerda?",
                  "$K_T = 0$ dan "
                  "$3s^2 = h^2$, ya'ni "
                  "$w_{lim} = h(1 - "
                  "1/\\sqrt3) = "
                  "0{,}4227h$; aniq "
                  "qiymat $0{,}4236h$.",
                  "hisob"),
                q("Kodda bir xil algoritm "
                  "ikki xil natija berdi. "
                  "Nega?",
                  "Ichki kuch formulasi "
                  "farq qildi: "
                  "$1 - L_0/L$ da halokatli "
                  "qisqarish bor (su-02). "
                  "Ayniyat bilan qoldiq "
                  "nolga tushadi, sodda "
                  "variantda "
                  "$2\\cdot10^{-10}$ da "
                  "qotadi.", "kod"),
                q("Yuk nazorati nima uchun "
                  "chegaraviy nuqtadan o'ta "
                  "olmaydi?",
                  "$P > P_{lim}$ uchun yaqin "
                  "muvozanat holati mavjud "
                  "emas — bu usulning emas, "
                  "masalaning xossasi. "
                  "Siljish nazorati kerak.",
                  "talqin"),
                q("O'tib ketish nima uchun "
                  "xavfli?",
                  "Konstruksiya "
                  "$0{,}42h$ dan $2{,}16h$ "
                  "ga dinamik sakraydi; "
                  "statik tahlil sakrash "
                  "paytidagi inersiya "
                  "kuchlarini hisobga "
                  "olmaydi.", "talqin"),
                q("Qaytarish algoritmining "
                  "muhim xossasi qanday "
                  "tekshiriladi?",
                  "Natija qadam "
                  "kattaligidan mustaqil "
                  "bo'lishi kerak — kodda "
                  "11 va 1001 qadam aynan "
                  "bir xil javob beradi.",
                  "kod"),
            ],
            bridge=(
                "4-modul yakunlandi: FEM "
                "apparati fermadan "
                "nochiziqli qobiqqacha "
                "qo'llanildi. Oxirgi modulda "
                "esa FEM dan tashqariga "
                "chiqamiz — differensial "
                "kvadratura, chegaraviy "
                "elementlar va spektral "
                "usullar; so'ng natijaning "
                "ishonchliligini "
                "rasmiylashtiramiz va "
                "kursni yopamiz."
            ),
            research=(
                "Nochiziqli tahlilni "
                "chuqurlashtiring. "
                "(1) Riks yoy uzunligi "
                "usulini o'rganing: "
                "qaytuvchi nuqta "
                "(snap-back) bo'lganda "
                "siljish nazorati ham "
                "yetarli emas — yoy "
                "uzunligi buni qanday "
                "hal qiladi? "
                "(2) Izchil urinma "
                "modulni (consistent "
                "tangent) o'rganing: "
                "nima uchun uni "
                "elastoplastik modul "
                "bilan almashtirish "
                "kvadratik "
                "yaqinlashishni "
                "yo'qotadi? "
                "(3) Kinematik va "
                "aralash "
                "mustahkamlanishni "
                "ko'rib chiqing: "
                "Baushinger effekti va "
                "siklik yuklamadagi "
                "xatti-harakat (mq-08). "
                "(4) Aniq (explicit) "
                "dinamik "
                "integrallashni "
                "o'rganing: avariya "
                "hisobida nima uchun "
                "Nyuton iteratsiyasi "
                "umuman "
                "ishlatilmaydi?"
            ),
            manim_ref=manim(
                scene="SnapThroughScene",
                module="manim/scenes/su_apps.py",
                title="O'tib ketish hodisasi",
                summary=(
                    "Yassi ferma asta-sekin "
                    "yuklanadi va yonida "
                    "yuk–ko'chish egri "
                    "chizig'ida nuqta "
                    "harakatlanadi. "
                    "Chegaraviy nuqtaga "
                    "yetganda ferma "
                    "birdan ag'darilib "
                    "pastki holatga "
                    "sakraydi, nuqta esa "
                    "egri chiziqdagi "
                    "uzoq shoxga o'tadi. "
                    "Keyin xuddi shu "
                    "masala siljish "
                    "nazorati bilan "
                    "takrorlanadi va bu "
                    "safar butun yo'l, "
                    "jumladan "
                    "pasayuvchi shox "
                    "ham, uzluksiz "
                    "bosib o'tiladi."
                ),
            ),
        ),
    ),
]
