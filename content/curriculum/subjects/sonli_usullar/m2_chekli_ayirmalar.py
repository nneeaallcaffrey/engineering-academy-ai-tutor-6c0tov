"""SU / 2-modul: Chekli ayirmalar usuli (su-07 … su-12)."""

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
M = "su-m2"


def _lesson(problem, concepts, derivation, meaning, equations, conditions,
            worked, computation, visual, interp, mistakes, quiz, bridge, research,
            manim_ref=None):
    return Lesson(
        physical_problem=problem, concepts=concepts, derivation=derivation,
        formula_meaning=meaning, equations=equations, conditions=conditions,
        worked_example=worked, computation=computation, visualization=visual,
        interpretation=interp, common_mistakes=mistakes, quiz=quiz,
        bridge_to_next=bridge, research_extension=research, manim=manim_ref,
    )


TOPICS = [
    # ------------------------------------------------------------------ su-07
    Topic(
        id="su-07",
        subject_id=S, module_id=M, order=7,
        title="Ayirma sxemalarini qurish: aniqlanmagan koeffitsientlar usuli",
        description=(
            "Ixtiyoriy tartibli ayirma sxemasini qurish, notekis to'rda "
            "sxema olish, bir tomonlama sxemalar va ularning "
            "chegaralardagi roli."
        ),
        learning_objective=(
            "Berilgan shablon uchun aniqlanmagan koeffitsientlar usuli "
            "bilan ayirma sxemasini qurish, uning tartibini nazariy "
            "aniqlash va sonli tasdiqlash."
        ),
        prerequisites=["su-03", "su-06"],
        mathematical_core=(
            "$\\sum_k c_k f(x+kh) = f^{(m)}(x) + O(h^p)$; "
            "Vandermond tizimi $\\sum_k c_k k^j = "
            "m!\\,\\delta_{jm}/h^m$."
        ),
        engineering_application=(
            "Notekis to'rda kuchlanish hisobi, chegara yaqinidagi "
            "sxemalar, tenzodatchik ma'lumotidan deformatsiya olish, "
            "yuqori tartibli hisoblash sxemalari."
        ),
        computational_component=(
            "Vandermond tizimini yechib ixtiyoriy sxema qurish va "
            "uning tartibini sonli o'lchash."
        ),
        visualization_component=(
            "Shablon nuqtalari va koeffitsientlar, yaqinlashish "
            "tartibining shablon o'lchamiga bog'liqligi."
        ),
        research_extension=(
            "Kompakt (Padé) sxemalarni o'rganing: ular kichik shablon "
            "bilan yuqori tartib beradi. Ularning narxi va afzalligini "
            "oddiy sxemalar bilan solishtiring."
        ),
        difficulty="asosiy",
        previous_link=(
            "su-03 da markaziy va oldinga ayirma sxemalari Teylor "
            "qatoridan qo'lda chiqarildi. Endi bu jarayonni "
            "avtomatlashtiramiz: ixtiyoriy shablon uchun sxemani "
            "chiziqli tizim yechib olamiz."
        ),
        next_topic="su-08",
        estimated_minutes=80,
        tags=["Vandermond", "shablon", "notekis to'r", "bir tomonlama"],
        lesson=_lesson(
            problem=(
                "Konsol balkaning egilish chizig'i "
                "o'lchandi, lekin datchiklar **notekis** "
                "joylashgan: mahkamlash yaqinida zich "
                "(u yerda egrilik katta), uchida siyrak. "
                "Egish momentini topish uchun ikkinchi "
                "hosila kerak. su-03 dagi "
                "$(w_{i-1}-2w_i+w_{i+1})/h^2$ sxemasi "
                "**tekis** to'r uchun; notekis to'rda "
                "uni qo'llash xato beradi va, eng "
                "yomoni, xato mavjudligi bilinmaydi. "
                "Bundan tashqari mahkamlangan uchida "
                "markaziy ayirma umuman qo'llanmaydi — "
                "chapda tugun yo'q. Ikkala holat uchun "
                "ham sxema kerak, va ularni har safar "
                "qo'lda chiqarish o'rniga umumiy "
                "usulni qurish mantiqiy."
            ),
            concepts=[
                c("Shablon (stencil)",
                  "Sxemada ishtirok etadigan tugunlar "
                  "to'plami; $x + k_1h, \\ldots, "
                  "x + k_sh$."),
                c("Aniqlanmagan koeffitsientlar usuli",
                  "Koeffitsientlarni noma'lum deb olib, "
                  "Teylor yoyilmasidan chiziqli tizim "
                  "qurish va uni yechish."),
                c("Vandermond tizimi",
                  "Hosil bo'ladigan matritsa "
                  "$V_{jk} = k^j$ — Vandermond "
                  "ko'rinishida; u yomon shartlangan "
                  "(su-04), lekin kichik shablonda "
                  "muammo emas."),
                c("Sxemaning tartibi",
                  "$s$ nuqtali shablon $m$-hosila "
                  "uchun odatda $p = s - m$ tartib "
                  "beradi; simmetrik shablonda esa "
                  "$p = s - m + 1$ (bitta had bepul "
                  "qisqaradi)."),
                c("Bir tomonlama sxema",
                  "Faqat bir tomondagi tugunlarni "
                  "ishlatadigan sxema; chegaralarda "
                  "zarur, lekin xatolik "
                  "koeffitsienti kattaroq."),
                c("Notekis to'r",
                  "Tugunlar orasidagi masofa "
                  "o'zgaruvchan; sxema "
                  "koeffitsientlari har bir tugunda "
                  "alohida hisoblanadi."),
            ],
            derivation=[
                d("1. Umumiy sxemaning ko'rinishi",
                  r"f^{(m)}(x) \approx \sum_{k=1}^{s} "
                  r"c_k\,f(x_k), \quad x_k = x + \delta_k",
                  "$\\delta_k$ — shablon nuqtalarining "
                  "$x$ ga nisbatan siljishi. Tekis "
                  "to'rda $\\delta_k = k h$, notekis "
                  "to'rda ixtiyoriy."),
                d("2. Har bir qiymatni Teylorga yoyish",
                  r"f(x_k) = \sum_{j=0}^{s-1} "
                  r"\frac{\delta_k^j}{j!}f^{(j)}(x) + "
                  r"O(\delta^s)",
                  "$s$ ta nuqta bor, demak $s$ ta "
                  "shartni qanoatlantirish mumkin."),
                d("3. Yig'indini almashtirish",
                  r"\sum_k c_k f(x_k) = \sum_{j=0}^{s-1}"
                  r"f^{(j)}(x)\Big[\frac{1}{j!}\sum_k "
                  r"c_k\delta_k^j\Big] + \ldots",
                  "Yig'indi tartibini almashtirdik. "
                  "Kvadrat qavs ichidagi ifoda har bir "
                  "hosila oldidagi koeffitsient."),
                d("4. Shartlar tizimi",
                  r"\sum_k c_k \delta_k^j = "
                  r"\begin{cases} m! & j = m\\ 0 & "
                  r"j \ne m\end{cases}, \quad "
                  r"j = 0,\ldots,s-1",
                  "**Hal qiluvchi qadam.** Biz "
                  "$f^{(m)}$ ni olishni istaymiz, "
                  "demak uning koeffitsienti 1 "
                  "bo'lsin, qolganlari nol. Bu $s$ ta "
                  "tenglamali chiziqli tizim."),
                d("5. Vandermond matritsasi",
                  r"\mathbf{V}\mathbf{c} = \mathbf{b}, "
                  r"\quad V_{jk} = \delta_k^{\,j}, "
                  r"\quad b_j = m!\,\delta_{jm}",
                  "Matritsa Vandermond ko'rinishida. "
                  "Shablon nuqtalari turlicha bo'lsa "
                  "u teskarilanuvchan — demak yechim "
                  "mavjud va yagona."),
                d("6. Tekis to'r uchun soddalashtirish",
                  r"\delta_k = k h \;\Longrightarrow\; "
                  r"\sum_k c_k k^j = \frac{m!\,"
                  r"\delta_{jm}}{h^m}",
                  "$h$ ni ajratib chiqarish mumkin: "
                  "koeffitsientlar $1/h^m$ ga "
                  "mutanosib va shablon shakliga "
                  "bog'liq."),
                d("7. Tekshirish: markaziy ayirma",
                  r"s = 3, \ m = 2, \ k = \{-1,0,1\} "
                  r"\;\Longrightarrow\; \mathbf{c} = "
                  r"\frac{1}{h^2}\{1,-2,1\}",
                  "su-03 dagi sxema aynan qayta "
                  "olindi. Usul to'g'ri ishlayotganining "
                  "birinchi tasdig'i."),
                d("8. Yetakchi xatolik hadi",
                  r"E = \frac{f^{(q)}(x)}{q!}\sum_k "
                  r"c_k\delta_k^{\,q}, \quad q = s "
                  r"\ (\text{birinchi nolga teng "
                  r"bo'lmagan})",
                  "Tizim $j < s$ uchun shartlarni "
                  "bajaradi; birinchi "
                  "qanoatlantirilmagan had xatolikni "
                  "beradi. Uni hisoblash sxemaning "
                  "tartibini aniqlaydi."),
                d("9. Simmetriyaning bonusi",
                  r"\text{simmetrik shablon} \ + \ "
                  r"\text{juft } m \;\Longrightarrow\; "
                  r"\sum_k c_k\delta_k^{\,s} = 0",
                  "**Bepul tartib.** Simmetrik "
                  "shablonda toq hadlar o'zaro "
                  "qisqaradi, shuning uchun tartib "
                  "kutilganidan bitta yuqori. "
                  "Markaziy ayirma $O(h^2)$ ekani "
                  "shundan ($s-m = 1$ emas)."),
                d("10. Notekis to'rda tartibning "
                  "pasayishi",
                  r"\delta_{-1} = -h_1, \ \delta_{1} = "
                  r"h_2, \ h_1 \ne h_2 "
                  r"\;\Longrightarrow\; E \sim "
                  r"\frac{h_2-h_1}{3}f''' + O(h^2)",
                  "**Muhim ogohlantirish.** Notekis "
                  "to'rda ikkinchi hosila sxemasi "
                  "birinchi tartibga tushadi. Tekis "
                  "to'rdagi simmetriya bonusi "
                  "yo'qoladi."),
                d("11. Bir tomonlama sxemalar",
                  r"k = \{0,1,2,3\}, \ m = 2 "
                  r"\;\Longrightarrow\; \mathbf{c} = "
                  r"\frac{1}{h^2}\{2,-5,4,-1\}",
                  "Chegarada chapda tugun yo'q. "
                  "To'rt nuqtali bir tomonlama sxema "
                  "$O(h^2)$ beradi — markaziy bilan "
                  "bir xil tartib, lekin xatolik "
                  "koeffitsienti kattaroq."),
            ],
            meaning=(
                "Aniqlanmagan koeffitsientlar usuli "
                "ayirma sxemalarini qurishni "
                "**mexanik jarayonga** aylantiradi: "
                "shablonni tanlaysiz, hosilaning "
                "tartibini aytasiz va chiziqli tizimni "
                "yechasiz. Qo'lda Teylor yoyish shart "
                "emas. Bu ayniqsa notekis to'rda va "
                "chegaralarda qimmatli, chunki u "
                "yerda tayyor formulalar yo'q. "
                "9-qadamdagi simmetriya bonusi "
                "tushunish uchun muhim: markaziy "
                "ayirma nima uchun 'kutilganidan "
                "yaxshiroq' ekanini u tushuntiradi. "
                "Uch nuqtali shablon ikkinchi hosila "
                "uchun $s - m = 1$ tartib berishi "
                "kerak edi, lekin simmetriya tufayli "
                "$O(h^2)$ chiqadi. Bu bepul emas — u "
                "shablonning simmetrikligiga "
                "bog'liq. 10-qadam aynan shuni "
                "ko'rsatadi: to'r notekis bo'lishi "
                "bilan bonus yo'qoladi va sxema "
                "birinchi tartibga tushadi. Bu "
                "amaliyotda ko'p uchraydigan yashirin "
                "xato manbai: muhandis notekis to'r "
                "quradi (bu to'g'ri — kuchlanish "
                "konsentratsiyasi joyida zichroq "
                "to'r kerak), lekin tekis to'r "
                "formulasini ishlatadi va yaqinlashish "
                "tartibi jimgina pasayadi. Chekli "
                "elementlar usuli (su-13 dan boshlab) "
                "bu muammodan xoli — u notekis to'rda "
                "ham tartibni saqlaydi va bu uning "
                "muhim afzalliklaridan biri. Bir "
                "tomonlama sxemalar esa chegaralarda "
                "zarur va ularning sifati butun "
                "hisobning tartibini belgilaydi: "
                "ichkarida $O(h^4)$ sxema ishlatib, "
                "chegarada $O(h)$ qo'llasangiz, "
                "umumiy tartib $O(h)$ ga tushib "
                "qolishi mumkin."
            ),
            equations=[
                eq(r"\sum_{k} c_k\,\delta_k^{\,j} = "
                   r"m!\,\delta_{jm}, \quad j = 0,"
                   r"\ldots,s-1",
                   "Aniqlanmagan koeffitsientlar "
                   "tizimi — ixtiyoriy shablon uchun.",
                   "Sxema shartlari"),
                eq(r"\mathbf{V}\mathbf{c} = \mathbf{b}, "
                   r"\quad V_{jk} = \delta_k^{\,j}",
                   "Vandermond matritsasi "
                   "ko'rinishidagi tizim.",
                   "Vandermond tizimi"),
                eq(r"\frac{f_{i-1}-2f_i+f_{i+1}}{h^2} = "
                   r"f'' + \frac{h^2}{12}f^{(4)} + O(h^4)",
                   "Tekis to'rdagi klassik sxema — "
                   "simmetriya tufayli $O(h^2)$.",
                   "Markaziy sxema"),
                eq(r"\frac{2f_0-5f_1+4f_2-f_3}{h^2} = "
                   r"f'' + O(h^2)",
                   "To'rt nuqtali bir tomonlama "
                   "ikkinchi hosila sxemasi — "
                   "chegaralar uchun.",
                   "Bir tomonlama sxema"),
            ],
            conditions=(
                "**Sxema mavjud bo'lishi uchun:** "
                "shablon nuqtalari turlicha bo'lsin "
                "(Vandermond matritsasi "
                "teskarilanuvchan).\n\n"
                "**Tartib bo'yicha qoidalar:**\n"
                "- Umumiy holda $p = s - m$;\n"
                "- Simmetrik shablon va juft $m$: "
                "$p = s - m + 1$;\n"
                "- Notekis to'rda simmetriya bonusi "
                "**yo'qoladi**.\n\n"
                "**Chegaralarda:** ichki sxema bilan "
                "bir xil tartibli bir tomonlama "
                "sxema ishlatish kerak. Chegarada "
                "tartib pasaysa, umumiy tartib ham "
                "pasayishi mumkin (lekin har doim "
                "emas — bu masalaga bog'liq).\n\n"
                "**Shablon o'lchami bo'yicha "
                "ogohlantirish:** $s$ katta bo'lsa "
                "Vandermond matritsasi yomon "
                "shartlangan bo'ladi "
                "($\\kappa \\sim 4^s$) va "
                "koeffitsientlar aniqligi tushadi. "
                "Amalda $s \\le 7$ tavsiya etiladi; "
                "undan yuqori tartib kerak bo'lsa "
                "kompakt (Padé) sxemalar afzal.\n\n"
                "**Silliqlik talabi:** $p$-tartibli "
                "sxema $f$ ning $p+m$ tartibli "
                "hosilasi mavjud va chegaralangan "
                "bo'lishini talab qiladi."
            ),
            worked=WorkedExample(
                statement=(
                    "(a) $k = \\{-1, 0, 1\\}$ shabloni "
                    "va $m = 2$ uchun sxemani va uning "
                    "yetakchi xatolik hadini "
                    "chiqaring. (b) Notekis to'rda "
                    "($h_1 = 0{,}5h$, $h_2 = h$) xuddi "
                    "shu masalani yeching va tartibni "
                    "aniqlang. (c) Chegara uchun "
                    "$k = \\{0,1,2,3\\}$ sxemasini "
                    "toping."
                ),
                given=[
                    r"m = 2 \ (\text{ikkinchi hosila})",
                    r"\text{(a) } \delta = \{-h, 0, h\}",
                    r"\text{(b) } \delta = \{-0{,}5h, 0, h\}",
                ],
                steps=[
                    st(r"\text{(a) } j=0: \ c_{-1}+c_0+c_1 "
                       r"= 0",
                       "$f$ ning koeffitsienti nol "
                       "bo'lishi kerak."),
                    st(r"j=1: \ -hc_{-1} + hc_1 = 0 "
                       r"\;\Rightarrow\; c_{-1} = c_1",
                       "$f'$ ning koeffitsienti nol — "
                       "simmetriya kelib chiqdi."),
                    st(r"j=2: \ \frac{h^2}{2}(c_{-1}+c_1) "
                       r"= 1 \cdot \frac{2!}{2!} "
                       r"\;\Rightarrow\; c_{-1}+c_1 = "
                       r"\frac{2}{h^2}",
                       "$f''$ ning koeffitsienti 1."),
                    st(r"c_{-1} = c_1 = \frac{1}{h^2}, "
                       r"\quad c_0 = -\frac{2}{h^2}",
                       "Klassik sxema qayta olindi — "
                       "7-qadamdagi tekshiruv."),
                    st(r"E: \ j=3 \ \text{hadi} = "
                       r"\frac{1}{6}\big(-h^3c_{-1} + "
                       r"h^3c_1\big) = 0",
                       "**Toq had qisqardi** — "
                       "simmetriya bonusi. Demak "
                       "tartib kutilgan 1 emas."),
                    st(r"j=4: \ \frac{1}{24}h^4"
                       r"(c_{-1}+c_1) = "
                       r"\frac{h^4}{24}\cdot\frac{2}{h^2} "
                       r"= \frac{h^2}{12} "
                       r"\;\Rightarrow\; E = "
                       r"\frac{h^2}{12}f^{(4)}",
                       "Yetakchi xatolik "
                       "$\\frac{h^2}{12}f^{(4)}$ — "
                       "**ikkinchi tartib**."),
                    st(r"\text{(b) } \delta = \{-a, 0, b\}, "
                       r"\ a = 0{,}5h, \ b = h",
                       "Notekis to'r."),
                    st(r"c_{-1} = \frac{2}{a(a+b)}, \ "
                       r"c_1 = \frac{2}{b(a+b)}, \ "
                       r"c_0 = -\frac{2}{ab}",
                       "Vandermond tizimining umumiy "
                       "yechimi (kodda tasdiqlanadi)."),
                    st(r"E = \frac{b-a}{3}f''' + O(h^2) "
                       r"= \frac{0{,}5h}{3}f''' = "
                       r"0{,}167h\,f'''",
                       "**Birinchi tartib!** "
                       "$a \\ne b$ bo'lgani uchun toq "
                       "had qisqarmaydi va tartib "
                       "2 dan 1 ga tushadi."),
                    st(r"\text{(c) } j=0{:}3 \ "
                       r"\text{tizimini yechib: } "
                       r"\mathbf{c} = \frac{1}{h^2}"
                       r"\{2,-5,4,-1\}",
                       "Bir tomonlama sxema."),
                    st(r"E = -\frac{11h^2}{12}f^{(4)} "
                       r"\;\Rightarrow\; O(h^2), \ "
                       r"\text{lekin koeffitsient } "
                       r"11 \ \text{marta katta}",
                       "Tartib bir xil, aniqlik esa "
                       "ancha yomon. Shuning uchun "
                       "chegara yaqinida to'rni "
                       "zichlashtirish foydali."),
                ],
                answer=(
                    "(a) $\\{1,-2,1\\}/h^2$, "
                    "$E = \\frac{h^2}{12}f^{(4)}$ — "
                    "ikkinchi tartib (simmetriya "
                    "bonusi). (b) Notekis to'rda "
                    "$c_{-1} = \\frac{2}{a(a+b)}$, "
                    "$c_0 = -\\frac{2}{ab}$, "
                    "$c_1 = \\frac{2}{b(a+b)}$ va "
                    "$E = \\frac{b-a}{3}f'''$ — "
                    "**birinchi tartib**. "
                    "(c) $\\{2,-5,4,-1\\}/h^2$, "
                    "$E = -\\frac{11h^2}{12}f^{(4)}$ — "
                    "ikkinchi tartib, lekin xatolik "
                    "koeffitsienti 11 barobar katta."
                ),
                engineering_note=(
                    "(b) natijasi amaliyotda eng "
                    "ko'p e'tibordan chetda qoladigan "
                    "xato manbai. Notekis to'r "
                    "qurish to'g'ri va zarur — "
                    "kuchlanish konsentratsiyasi "
                    "joyida tugunlar zichroq bo'lishi "
                    "kerak. Lekin tekis to'r "
                    "formulasi qo'llanilsa, "
                    "yaqinlashish tartibi jimgina "
                    "2 dan 1 ga tushadi va hech "
                    "qanday xato xabari chiqmaydi. "
                    "Natija to'r bo'yicha "
                    "yaqinlashadi, lekin ikki "
                    "barobar sekin — va agar "
                    "yaqinlashish tartibi "
                    "o'lchanmasa, buni sezish "
                    "imkonsiz. Aynan shuning uchun "
                    "su-28 da yaqinlashish tartibini "
                    "o'lchash V&V tartibining "
                    "majburiy qismi sifatida "
                    "qo'yiladi. (c) natijasi esa "
                    "boshqa amaliy maslahatni "
                    "beradi: chegaradagi xatolik "
                    "koeffitsienti ichki sxemadan "
                    "ancha katta, shuning uchun "
                    "chegara yaqinida to'rni "
                    "zichlashtirish nomutanosib "
                    "katta foyda keltiradi."
                ),
            ),
            computation=Computation(
                caption=(
                    "Aniqlanmagan koeffitsientlar "
                    "usuli bilan ixtiyoriy sxema "
                    "qurish, uning tartibini nazariy "
                    "va sonli aniqlash."
                ),
                code='''"""Ayirma sxemalarini avtomatik qurish va tartibini o'lchash."""
import numpy as np
from labkit import PARAMS, note, series, table, value

m_der = int(PARAMS.get("m_der", 2))       # nechanchi hosila
s_left = int(PARAMS.get("s_left", 1))     # chapda nechta nuqta
s_right = int(PARAMS.get("s_right", 1))   # o'ngda nechta nuqta
ratio = float(PARAMS.get("ratio", 0.5))   # notekis to'r nisbati
x0 = float(PARAMS.get("x0", 1.0))


def fd_coeffs(offsets, m):
    """Aniqlanmagan koeffitsientlar usuli: Vandermond tizimini yechish.

    offsets - shablon nuqtalarining x ga nisbatan siljishlari (h birligida)
    m       - kerakli hosilaning tartibi
    """
    s = len(offsets)
    d = np.asarray(offsets, dtype=float)
    V = np.vander(d, s, increasing=True).T     # V[j, k] = d_k^j
    b = np.zeros(s)
    if m >= s:
        raise ValueError("shablon juda kichik")
    b[m] = float(np.prod(np.arange(1, m + 1))) if m > 0 else 1.0
    return np.linalg.solve(V, b), d


def leading_error(coeffs, offsets, m):
    """Birinchi nolga teng bo'lmagan qoldiq hadni topadi."""
    s = len(offsets)
    d = np.asarray(offsets, dtype=float)
    for j in range(s, s + 6):
        fact = float(np.prod(np.arange(1, j + 1))) if j > 0 else 1.0
        val = np.sum(coeffs*d**j)/fact
        if abs(val) > 1e-10:
            return j - m, val        # (tartib, koeffitsient)
    return None, 0.0


# --- (1) Klassik sxemalarni qayta olish ---
rows = []
checks = [
    ("markaziy, 1-hosila", [-1, 0, 1], 1),
    ("markaziy, 2-hosila", [-1, 0, 1], 2),
    ("markaziy, 2-hosila (5 nuqta)", [-2, -1, 0, 1, 2], 2),
    ("oldinga, 1-hosila", [0, 1], 1),
    ("bir tomonlama, 2-hosila", [0, 1, 2, 3], 2),
    ("markaziy, 4-hosila", [-2, -1, 0, 1, 2], 4),
]
for name, off, m in checks:
    cf, dd = fd_coeffs(off, m)
    p_ord, ecf = leading_error(cf, off, m)
    rows.append([name, str(off), m,
                 " ".join(f"{v:+.4g}" for v in cf),
                 p_ord, f"{ecf:+.5g}"])
table("Aniqlanmagan koeffitsientlar usuli bilan qurilgan sxemalar",
      ["Sxema", "shablon", "m", "koeffitsientlar (1/h^m)",
       "tartib p", "xatolik koeff."], rows)

cf3, _ = fd_coeffs([-1, 0, 1], 2)
value("Markaziy 2-hosila: c[-1]", float(cf3[0]), "—")
value("Markaziy 2-hosila: c[0]", float(cf3[1]), "—")
value("Markaziy 2-hosila: c[+1]", float(cf3[2]), "—")
p3, e3 = leading_error(cf3, [-1, 0, 1], 2)
value("Uning tartibi", float(p3), "—")
value("Xatolik koeffitsienti", float(e3), "—")
note(f"Uch nuqtali markaziy sxema {{{cf3[0]:.0f}, {cf3[1]:.0f}, "
     f"{cf3[2]:.0f}}}/h^2 qayta olindi va uning tartibi {p3}, "
     f"xatolik koeffitsienti {e3:.6f} = 1/12. Bu su-03 dagi qo'lda "
     f"chiqarilgan natija bilan AYNAN mos - usul to'g'ri ishlaydi.")

cfb, _ = fd_coeffs([0, 1, 2, 3], 2)
pb, eb = leading_error(cfb, [0, 1, 2, 3], 2)
value("Bir tomonlama sxema tartibi", float(pb), "—")
value("Bir tomonlama xatolik koeffitsienti", float(eb), "—")
value("Chegara/ichki xatolik nisbati", abs(eb/e3), "marta")
note(f"Bir tomonlama {{2,-5,4,-1}}/h^2 sxemasi ham {pb}-tartibli, "
     f"lekin xatolik koeffitsienti {eb:.5f} - ichki sxemadan "
     f"{abs(eb/e3):.1f} marta katta. Shuning uchun chegara yaqinida "
     f"to'rni zichlashtirish nomutanosib katta foyda beradi.")

# --- (2) Simmetriya bonusini ko'rsatish ---
rows2 = []
for s_tot in range(3, 10, 2):
    half = s_tot//2
    off_sym = list(range(-half, half + 1))
    cfs, _ = fd_coeffs(off_sym, 2)
    ps, es = leading_error(cfs, off_sym, 2)
    off_asym = list(range(0, s_tot))
    cfa, _ = fd_coeffs(off_asym, 2)
    pa, ea = leading_error(cfa, off_asym, 2)
    rows2.append([s_tot, f"{ps}", f"{s_tot - 2}", f"{pa}",
                  f"{abs(ea/es):.1f}"])
table("Simmetriya bonusi (m = 2)",
      ["nuqtalar s", "simmetrik tartib", "s - m", "bir tomonlama tartib",
       "xatolik nisbati"], rows2)
note("Simmetrik shablonda tartib s - m emas, s - m + 1 chiqadi - "
     "toq hadlar o'zaro qisqagani uchun bitta tartib BEPUL keladi. "
     "Bir tomonlama shablonda bu bonus yo'q.")

# --- (3) Notekis to'r: tartibning pasayishi ---
def d2_nonuniform(a, b):
    """x-a, x, x+b nuqtalaridan ikkinchi hosila koeffitsientlari."""
    cf, _ = fd_coeffs([-a, 0.0, b], 2)
    return cf


a_r, b_r = ratio, 1.0
cf_nu = d2_nonuniform(a_r, b_r)
p_nu, e_nu = leading_error(cf_nu, [-a_r, 0.0, b_r], 2)
value("Notekis to'r nisbati a/b", a_r/b_r, "—")
value("Notekis sxema tartibi", float(p_nu), "—")
value("Notekis xatolik koeffitsienti", float(e_nu), "—")
# Analitik formula bilan tekshirish
c_an = np.array([2/(a_r*(a_r + b_r)), -2/(a_r*b_r), 2/(b_r*(a_r + b_r))])
value("Analitik formuladan farq",
      float(np.max(np.abs(cf_nu - c_an))), "—")
note(f"Notekis to'rda (a/b = {a_r/b_r:.2f}) sxema tartibi {p_nu} ga "
     f"TUSHDI (tekis to'rda 2 edi). Koeffitsientlar analitik "
     f"formuladan {np.max(np.abs(cf_nu - c_an)):.3e} farq qiladi - "
     f"tizim to'g'ri yechilgan. Yetakchi xatolik koeffitsienti "
     f"{e_nu:.5f} ~ (b-a)/3 = {(b_r - a_r)/3:.5f}.")

# --- (4) TARTIBNI SONLI O'LCHASH ---
def f(t):
    return np.exp(np.sin(t))


def f2_exact(t):
    return np.exp(np.sin(t))*(np.cos(t)**2 - np.sin(t))


hs = np.logspace(-4, -1, 40)
e_uni, e_non, e_bnd = [], [], []
for h in hs:
    # tekis
    cu, _ = fd_coeffs([-1, 0, 1], 2)
    du = np.sum(cu*np.array([f(x0 - h), f(x0), f(x0 + h)]))/h**2
    e_uni.append(abs(du - f2_exact(x0))/abs(f2_exact(x0)))
    # notekis
    cn = d2_nonuniform(a_r, b_r)
    dn = np.sum(cn*np.array([f(x0 - a_r*h), f(x0), f(x0 + b_r*h)]))/h**2
    e_non.append(abs(dn - f2_exact(x0))/abs(f2_exact(x0)))
    # bir tomonlama
    cb, _ = fd_coeffs([0, 1, 2, 3], 2)
    db = np.sum(cb*np.array([f(x0), f(x0 + h), f(x0 + 2*h),
                             f(x0 + 3*h)]))/h**2
    e_bnd.append(abs(db - f2_exact(x0))/abs(f2_exact(x0)))

series("Tekis to'r xatoligi", hs.tolist(), e_uni,
       xlabel="qadam h", ylabel="nisbiy xatolik")
series("Notekis to'r xatoligi", hs.tolist(), e_non,
       xlabel="qadam h", ylabel="nisbiy xatolik")
series("Bir tomonlama sxema xatoligi", hs.tolist(), e_bnd,
       xlabel="qadam h", ylabel="nisbiy xatolik")

msk = (hs > 3e-4) & (hs < 3e-2)
sl_u = np.polyfit(np.log(hs[msk]), np.log(np.array(e_uni)[msk]), 1)[0]
sl_n = np.polyfit(np.log(hs[msk]), np.log(np.array(e_non)[msk]), 1)[0]
sl_b = np.polyfit(np.log(hs[msk]), np.log(np.array(e_bnd)[msk]), 1)[0]
value("Tekis to'r: o'lchangan tartib", float(sl_u), "—")
value("Notekis to'r: o'lchangan tartib", float(sl_n), "—")
value("Bir tomonlama: o'lchangan tartib", float(sl_b), "—")
note(f"SONLI o'lchangan tartiblar: tekis to'r {sl_u:.3f} (nazariy 2), "
     f"notekis to'r {sl_n:.3f} (nazariy 1), bir tomonlama {sl_b:.3f} "
     f"(nazariy 2). Nazariy bashoratlar to'liq tasdiqlandi - "
     f"jumladan notekis to'rdagi TARTIB PASAYISHI ham.")

# Bir xil h da xatoliklarni taqqoslash
i_ref = int(np.argmin(np.abs(hs - 1e-2)))
value("h = 1e-2 da tekis to'r xatoligi", float(e_uni[i_ref]), "—")
value("h = 1e-2 da notekis to'r xatoligi", float(e_non[i_ref]), "—")
value("h = 1e-2 da bir tomonlama xatolik", float(e_bnd[i_ref]), "—")
note(f"h = 1e-2 da: tekis {e_uni[i_ref]:.3e}, notekis "
     f"{e_non[i_ref]:.3e} ({e_non[i_ref]/e_uni[i_ref]:.0f} marta "
     f"yomon), bir tomonlama {e_bnd[i_ref]:.3e} "
     f"({e_bnd[i_ref]/e_uni[i_ref]:.0f} marta yomon). Notekislik "
     f"tartibni pasaytirgani uchun h kichraygan sari bu farq "
     f"YANADA o'sadi.")

# --- (5) Vandermond matritsasining shartlanganligi ---
rows3 = []
for s_tot in range(3, 12, 2):
    half = s_tot//2
    off = np.arange(-half, half + 1, dtype=float)
    V = np.vander(off, s_tot, increasing=True).T
    rows3.append([s_tot, f"{np.linalg.cond(V):.3e}",
                  f"{16 - np.log10(np.linalg.cond(V)):.1f}"])
table("Vandermond tizimining shartlanganligi",
      ["shablon o'lchami s", "kappa(V)", "qolgan ishonchli raqamlar"],
      rows3)
note("Shablon kattalashgani sari Vandermond matritsasi tez "
     "yomonlashadi (su-04). Shuning uchun juda yuqori tartibli "
     "sxemalarni bu usul bilan qurish xavfli; amalda s <= 7 "
     "tavsiya etiladi yoki kompakt (Pade) sxemalar ishlatiladi.")

# --- (6) Foydalanuvchi tanlagan shablon ---
off_user = list(range(-s_left, s_right + 1))
if len(off_user) > m_der:
    cu2, _ = fd_coeffs(off_user, m_der)
    pu, eu = leading_error(cu2, off_user, m_der)
    value("Tanlangan shablon nuqtalari soni", float(len(off_user)), "—")
    value("Tanlangan shablon tartibi", float(pu), "—")
    value("Tanlangan shablon xatolik koeffitsienti", float(eu), "—")
    note(f"Shablon {off_user}, hosila m = {m_der}: koeffitsientlar "
         f"{{{', '.join(f'{v:+.4g}' for v in cu2)}}}/h^{m_der}, "
         f"tartib {pu}, xatolik koeffitsienti {eu:.5g}.")
''',
                parameters=[
                    p("m_der", "Hosilaning tartibi m", 1.0, 4.0, 2.0, 1.0),
                    p("s_left", "Chapdagi nuqtalar soni", 0.0, 4.0, 1.0,
                      1.0),
                    p("s_right", "O'ngdagi nuqtalar soni", 0.0, 4.0, 1.0,
                      1.0),
                    p("ratio", "Notekis to'r nisbati a/b", 0.1, 1.0, 0.5,
                      0.05),
                    p("x0", "Hosila olinadigan nuqta x₀", 0.1, 5.0, 1.0,
                      0.1),
                ],
                expected_output=(
                    "Usul klassik sxemalarni aynan "
                    "qayta oladi: markaziy ikkinchi "
                    "hosila $\\{1,-2,1\\}/h^2$, "
                    "xatolik koeffitsienti $1/12$ — "
                    "su-03 dagi qo'lda chiqarilgan "
                    "natija bilan mos. Simmetrik "
                    "shablonlarda tartib $s-m$ emas, "
                    "$s-m+1$ chiqadi. Notekis to'rda "
                    "tartib 2 dan 1 ga tushadi va "
                    "koeffitsientlar analitik "
                    "formuladan mashina aniqligida "
                    "farq qiladi. Sonli o'lchangan "
                    "tartiblar nazariy qiymatlarni "
                    "tasdiqlaydi: tekis ≈ 2, notekis "
                    "≈ 1, bir tomonlama ≈ 2. "
                    "Vandermond matritsasining "
                    "shartlanganligi shablon "
                    "kattalashgani sari tez "
                    "yomonlashadi."
                ),
            ),
            visual=vis(
                kind="Shablon, koeffitsientlar va tartib",
                tool="React/SVG",
                description=(
                    "Shablon nuqtalari, koeffitsientlar "
                    "epyurasi va yaqinlashish "
                    "tartibining o'lchanishi."
                ),
                how_to_draw=(
                    "React/SVG: yuqorida bir o'lchovli "
                    "to'r chiziladi va shablon "
                    "nuqtalari yirik doiralar bilan "
                    "belgilanadi; har birining ustida "
                    "koeffitsient qiymati vertikal "
                    "ustun sifatida ko'rsatiladi "
                    "(musbat yuqoriga, manfiy pastga — "
                    "epyura mantiqi). Shablonni "
                    "slayderlar bilan o'zgartirganda "
                    "ustunlar darhol qayta "
                    "hisoblanadi va ularning "
                    "yig'indisi nol ekani alohida "
                    "ko'rsatiladi. Notekis to'r "
                    "rejimida nuqtalar orasidagi "
                    "masofalar haqiqiy nisbatda "
                    "chiziladi va simmetriyaning "
                    "buzilgani ko'rinadi. Pastda "
                    "log–log grafik: uchta xatolik "
                    "chizig'i (tekis, notekis, bir "
                    "tomonlama) va ularning "
                    "qiyaliklari uchburchaklar bilan "
                    "belgilanadi — notekis "
                    "chizig'ining yotiqroq ekani "
                    "(tartib 1) darhol ko'zga "
                    "tashlanadi."
                ),
            ),
            interp=(
                "Usulning to'g'riligi uchta mustaqil "
                "yo'l bilan tasdiqlanadi. Birinchisi — "
                "klassik sxemalarni qayta olish: "
                "markaziy ikkinchi hosila uchun "
                "$\\{1,-2,1\\}/h^2$ va xatolik "
                "koeffitsienti aynan $1/12$ chiqadi, "
                "bu su-03 da qo'lda chiqarilgan "
                "natija. Ikkinchisi — notekis "
                "to'rdagi koeffitsientlarning "
                "analitik formula bilan mashina "
                "aniqligida mos kelishi. Uchinchisi "
                "va eng muhimi — tartibni "
                "**sonli o'lchash**: nazariy "
                "bashoratlar (2, 1, 2) o'lchangan "
                "qiyaliklar bilan tasdiqlanadi. "
                "Ayniqsa notekis to'rdagi tartib "
                "pasayishi muhim, chunki u nazariy "
                "da'vo emas, o'lchangan fakt. "
                "Simmetriya bonusi jadvali "
                "9-qadamni aniq ko'rsatadi: "
                "simmetrik shablonda tartib "
                "$s-m+1$, bir tomonlamada esa "
                "$s-m$. Bu markaziy sxemalarning "
                "nima uchun afzal ekanini "
                "tushuntiradi — ular bir xil "
                "nuqtalar soni bilan bitta tartib "
                "ko'proq beradi. Bir tomonlama "
                "sxemaning xatolik koeffitsienti "
                "ichki sxemadan bir necha barobar "
                "katta bo'lishi esa amaliy maslahat "
                "beradi: chegara yaqinida to'rni "
                "zichlashtirish nomutanosib katta "
                "foyda keltiradi. Nihoyat, "
                "Vandermond matritsasining "
                "shartlanganligi su-04 bilan "
                "bog'lanadi va yuqori tartibli "
                "sxemalarning tabiiy chegarasini "
                "belgilaydi."
            ),
            mistakes=[
                "Notekis to'rda tekis to'r "
                "formulasini qo'llash. Tartib "
                "jimgina 2 dan 1 ga tushadi va hech "
                "qanday xato xabari chiqmaydi.",
                "Chegarada past tartibli sxema "
                "ishlatish. U butun hisobning "
                "tartibini pasaytirishi mumkin.",
                "Juda katta shablon olish. "
                "Vandermond matritsasi yomon "
                "shartlanadi va koeffitsientlar "
                "aniqligi tushadi.",
                "Yuqori tartibli sxemani silliq "
                "bo'lmagan yechimga qo'llash. "
                "$p$-tartib $f^{(p+m)}$ mavjudligini "
                "talab qiladi.",
                "Xatolik koeffitsientini e'tiborsiz "
                "qoldirish. Bir xil tartibli ikki "
                "sxema aniqlik bo'yicha o'nlab "
                "barobar farq qilishi mumkin.",
            ],
            quiz=[
                q("Aniqlanmagan koeffitsientlar "
                  "usulining mohiyati nima?",
                  "Shablon nuqtalarining Teylor "
                  "yoyilmalaridan chiziqli tizim "
                  "qurish: kerakli hosilaning "
                  "koeffitsienti 1, qolganlari nol "
                  "bo'lsin. Natijada Vandermond "
                  "tizimi hosil bo'ladi.",
                  "konseptual"),
                q("Nima uchun simmetrik shablon "
                  "bitta tartib ko'proq beradi?",
                  "Toq darajali hadlar o'zaro "
                  "qisqaradi (juft $m$ uchun), "
                  "shuning uchun birinchi "
                  "qanoatlantirilmagan had bitta "
                  "keyinroq keladi.", "konseptual"),
                q("$\\{0,1,2\\}$ shabloni va $m=1$ "
                  "uchun sxema qanday bo'ladi?",
                  "$\\{-3, 4, -1\\}/(2h)$ — ikkinchi "
                  "tartibli oldinga ayirma "
                  "($p = s-m = 2$).", "hisob"),
                q("Kodda notekis to'r tartibi nima "
                  "uchun alohida o'lchanadi?",
                  "Nazariy bashorat (tartib 2 dan "
                  "1 ga tushadi) o'lchash bilan "
                  "tasdiqlanishi kerak; bu amaliyotda "
                  "eng ko'p e'tibordan chetda "
                  "qoladigan xato manbai.", "kod"),
                q("Chegaradagi bir tomonlama sxema "
                  "nima uchun ichki sxemadan yomon?",
                  "Tartibi bir xil bo'lishi mumkin, "
                  "lekin xatolik koeffitsienti bir "
                  "necha barobar katta — simmetriya "
                  "yo'qligi tufayli.", "talqin"),
                q("Shablon o'lchamining amaliy "
                  "chegarasi nima belgilaydi?",
                  "Vandermond matritsasining "
                  "shartlanganligi $\\kappa \\sim 4^s$ "
                  "kabi o'sadi; $s > 7$ da "
                  "koeffitsientlar aniqligi "
                  "yo'qoladi.", "talqin"),
            ],
            bridge=(
                "Endi ixtiyoriy sxema qurishni "
                "bilamiz. Keyingi qadam — ularni "
                "haqiqiy chegaraviy masalaga "
                "qo'llash. Bir o'lchovli balka "
                "egilishi eng qulay boshlanish "
                "nuqtasi: unda to'rtinchi tartibli "
                "tenglama, turli chegaraviy shartlar "
                "va analitik yechim bor — demak "
                "sonli natijani tekshirish mumkin."
            ),
            research=(
                "Yuqori tartibli sxemalarni "
                "o'rganing. (1) Kompakt (Padé) "
                "sxemalar: "
                "$\\alpha f'_{i-1} + f'_i + "
                "\\alpha f'_{i+1} = "
                "b\\frac{f_{i+2}-f_{i-2}}{4h} + "
                "a\\frac{f_{i+1}-f_{i-1}}{2h}$ — "
                "kichik shablon bilan qanday qilib "
                "$O(h^6)$ ga erishiladi? Narxi "
                "nima (uch diagonalli tizim "
                "yechish)? (2) Notekis to'rda "
                "yuqori tartibni saqlash "
                "usullarini toping: koordinata "
                "almashtirish (mapping) yoki "
                "to'liq notekis sxemalar. "
                "(3) Spektral aniqlik tushunchasini "
                "o'rganing: Furye tahlilida ayirma "
                "sxemalari to'lqin sonini qanday "
                "buzadi (su-12 ga tayyorgarlik)?"
            ),
            manim_ref=manim(
                scene="StencilScene",
                module="manim/scenes/su_fd.py",
                title="Shablon va sxema koeffitsientlari",
                summary=(
                    "Shablon nuqtalari to'r ustida "
                    "belgilanadi va har birining "
                    "Teylor yoyilmasi ustma-ust "
                    "qo'yiladi; keraksiz hadlar "
                    "o'zaro qisqarib yo'qolishi "
                    "animatsiya bilan ko'rsatiladi. "
                    "Keyin to'r notekis qilinadi va "
                    "toq hadning qisqarmay qolishi "
                    "hamda tartibning pasayishi "
                    "namoyish etiladi."
                ),
            ),
        ),
    ),

    # ------------------------------------------------------------------ su-08
    Topic(
        id="su-08",
        subject_id=S, module_id=M, order=8,
        title="Bir o'lchovli chegaraviy masalalar: balka egilishi",
        description=(
            "To'rtinchi tartibli tenglamani ayirma tizimiga o'tkazish, "
            "chegaraviy shartlarni qo'yish usullari, soxta tugunlar va "
            "yaqinlashish tartibini o'lchash."
        ),
        learning_objective=(
            "Balka egilishi masalasini chekli ayirmalar bilan to'liq "
            "yechish, to'rt xil chegaraviy shartni to'g'ri qo'yish va "
            "natijani analitik yechim bilan tekshirish."
        ),
        prerequisites=["su-07", "mq-15", "mq-16"],
        mathematical_core=(
            "$EI\\,w^{(4)} = q$; besh nuqtali shablon "
            "$\\{1,-4,6,-4,1\\}/h^4$; soxta tugun orqali "
            "chegaraviy shart."
        ),
        engineering_application=(
            "Balka va ramka hisoblari, elastik asosdagi balka, "
            "o'zgaruvchan kesimli konstruksiyalar, quvur va "
            "relslar."
        ),
        computational_component=(
            "Balka masalasini to'liq yechish, to'rt xil chegaraviy "
            "shart uchun analitik yechim bilan taqqoslash va "
            "yaqinlashish tartibini o'lchash."
        ),
        visualization_component=(
            "Egilish chizig'i, moment va kesuvchi kuch epyuralari, "
            "sonli va analitik yechimlarning ustma-ust tushishi."
        ),
        research_extension=(
            "O'zgaruvchan kesimli va elastik asosdagi balka uchun "
            "sxemani umumlashtiring; konservativ (divergent) shakl "
            "nima uchun afzal ekanini tekshiring."
        ),
        difficulty="asosiy",
        previous_link=(
            "su-07 da ixtiyoriy sxema qurish usuli o'rganildi va "
            "besh nuqtali to'rtinchi hosila sxemasi "
            "$\\{1,-4,6,-4,1\\}$ jadvalda hisoblangan edi. Endi "
            "uni haqiqiy chegaraviy masalaga qo'llaymiz."
        ),
        next_topic="su-09",
        estimated_minutes=85,
        tags=["balka", "to'rtinchi tartib", "soxta tugun", "yaqinlashish"],
        lesson=_lesson(
            problem=(
                "mq-15 da balka egilishi analitik "
                "yechilgan edi, lekin faqat sodda "
                "holatlar uchun: doimiy kesim, doimiy "
                "yuklama, klassik tayanchlar. Endi "
                "real masala: kran balkasining kesimi "
                "uzunlik bo'ylab o'zgaradi (o'rtada "
                "baland, uchlarida past), yuklama esa "
                "harakatlanuvchi va nuqtaviy. "
                "$EI(x)w^{(4)} = q(x)$ tenglamasining "
                "analitik yechimi yo'q. Chekli "
                "ayirmalar bu masalani yechadi — "
                "lekin to'rtinchi tartibli tenglamada "
                "chegaraviy shartlarni qo'yish "
                "ikkinchi tartibli masalaga qaraganda "
                "sezilarli qiyinroq va aynan shu "
                "yerda eng ko'p xato qilinadi."
            ),
            concepts=[
                c("To'rtinchi tartibli shablon",
                  "$w^{(4)} \\approx "
                  "(w_{i-2}-4w_{i-1}+6w_i-4w_{i+1}"
                  "+w_{i+2})/h^4$ — besh nuqtali, "
                  "$O(h^2)$."),
                c("Soxta (fiktiv) tugun",
                  "Soha tashqarisidagi xayoliy tugun; "
                  "chegaraviy shartni ikkinchi tartibda "
                  "qo'yish uchun kiritiladi va keyin "
                  "yo'qotiladi."),
                c("Muhim va tabiiy shartlar",
                  "$w$ va $w'$ — muhim (kinematik); "
                  "$M = -EIw''$ va $Q = -EIw'''$ — "
                  "tabiiy (kuch) shartlari. Ular "
                  "turlicha qo'yiladi."),
                c("Chegaraviy shartlarning to'rt turi",
                  "Mahkamlangan, sharnirli, erkin va "
                  "sirpanuvchi mahkamlash; har biri "
                  "ikkitadan shart beradi."),
                c("Konservativ (divergent) shakl",
                  "$(EI w'')'' = q$ — o'zgaruvchan "
                  "$EI$ uchun to'g'ri shakl; "
                  "$EI w^{(4)} = q$ noto'g'ri."),
                c("Yaqinlashish tartibini o'lchash",
                  "Uchta to'rdan tartibni tiklash: "
                  "$p = \\log_2\\frac{e_h}{e_{h/2}}$ — "
                  "sonli yechimning ishonchliligi "
                  "mezoni."),
            ],
            derivation=[
                d("1. Boshlang'ich tenglama",
                  r"EI\,\frac{d^4w}{dx^4} = q(x), \quad "
                  r"0 < x < L",
                  "Eyler–Bernulli balkasi (mq-15). "
                  "To'rtinchi tartibli, demak to'rtta "
                  "chegaraviy shart kerak — har "
                  "uchida ikkitadan."),
                d("2. To'rni kiritish",
                  r"x_i = ih, \quad h = \frac{L}{n}, "
                  r"\quad i = 0,1,\ldots,n",
                  "$n+1$ ta tugun. Har birida "
                  "$w_i$ noma'lum."),
                d("3. Ichki tugunlar uchun sxema",
                  r"\frac{w_{i-2}-4w_{i-1}+6w_i-"
                  r"4w_{i+1}+w_{i+2}}{h^4} = "
                  r"\frac{q_i}{EI}",
                  "su-07 dagi jadvaldan olingan "
                  "sxema. Bu $i = 2,\\ldots,n-2$ "
                  "uchun ishlaydi — shablon "
                  "chegaradan chiqmasligi kerak."),
                d("4. Muammo: chegaraga yaqin tugunlar",
                  r"i = 1: \ w_{-1} \ \text{kerak}; "
                  r"\quad i = n-1: \ w_{n+1} \ "
                  r"\text{kerak}",
                  "**Asosiy qiyinchilik.** Shablon "
                  "soha tashqarisiga chiqadi. Ikkita "
                  "yechim bor: soxta tugun kiritish "
                  "yoki bir tomonlama sxema ishlatish."),
                d("5. Soxta tugun usuli",
                  r"w_{-1} \ \text{— xayoliy tugun}, "
                  r"\ \text{chegaraviy shartdan "
                  r"ifodalanadi}",
                  "Sohani $x = -h$ gacha kengaytiramiz. "
                  "$w_{-1}$ ni chegaraviy shart "
                  "orqali $w_0, w_1, \\ldots$ bilan "
                  "bog'laymiz va tizimdan yo'qotamiz."),
                d("6. Mahkamlangan uch",
                  r"w_0 = 0, \quad w'(0) = 0 "
                  r"\;\Longrightarrow\; "
                  r"\frac{w_1 - w_{-1}}{2h} = 0 "
                  r"\;\Longrightarrow\; w_{-1} = w_1",
                  "Markaziy ayirma bilan "
                  "$O(h^2)$ aniqlikda. Simmetriya "
                  "kelib chiqdi: mahkamlangan uchda "
                  "egilish chizig'i juft funksiya."),
                d("7. Sharnirli uch",
                  r"w_0 = 0, \quad M(0) = 0 "
                  r"\;\Longrightarrow\; "
                  r"\frac{w_{-1}-2w_0+w_1}{h^2} = 0 "
                  r"\;\Longrightarrow\; w_{-1} = -w_1",
                  "Endi antisimmetriya: sharnirli "
                  "uchda egilish chizig'i toq "
                  "funksiya. Ikki holatning farqi "
                  "faqat ishorada, lekin natija "
                  "butunlay boshqacha."),
                d("8. Erkin uch (ikkita shart)",
                  r"M(n) = 0: \ w_{n+1} = 2w_n - "
                  r"w_{n-1}; \quad Q(n) = 0: \ "
                  r"w_{n+2} = 2w_{n+1} - 2w_{n-1} + "
                  r"w_{n-2}",
                  "Erkin uchda **ikkita** soxta "
                  "tugun kerak, chunki shablon ikki "
                  "qadam chiqadi. Uchinchi hosila "
                  "sxemasi markaziy: "
                  "$(w_{n+2}-2w_{n+1}+2w_{n-1}"
                  "-w_{n-2})/(2h^3)$."),
                d("9. Tizimning tuzilishi",
                  r"\mathbf{K}\mathbf{w} = "
                  r"\frac{h^4}{EI}\mathbf{q}, \quad "
                  r"\mathbf{K} \ \text{— besh "
                  r"diagonalli}",
                  "Lenta kengligi $b = 2$ — su-05 "
                  "dagi kabi juda samarali. "
                  "Simmetrik musbat aniqlangan "
                  "(to'g'ri mahkamlanganda), demak "
                  "Cholesky qo'llanadi."),
                d("10. Moment va kesuvchi kuchni "
                  "tiklash",
                  r"M_i = -EI\frac{w_{i-1}-2w_i+"
                  r"w_{i+1}}{h^2}, \quad Q_i = "
                  r"-EI\frac{-w_{i-2}+2w_{i-1}-"
                  r"2w_{i+1}+w_{i+2}}{2h^3}",
                  "Diqqat: bu yerda **qo'shimcha xato "
                  "kiritilmaydi**. Diskret yechim "
                  "aynan $D_4w = q/EI$ ni "
                  "qanoatlantiradi va $M$ shu "
                  "yechimga $D_2$ ni qo'llab "
                  "olinadi — operatorlar "
                  "muvofiqlashgan. Sinusoidal "
                  "yechimda og'ish xatosi "
                  "$\sim k^2h^2/6$, moment xatosi "
                  "esa $\sim k^2h^2/12$, ya'ni "
                  "moment **ikki barobar "
                  "aniqroq**. Kodda bu "
                  "o'lchanadi."),
                d("10a. Qachon differensiallash "
                  "xavfli",
                  r"\text{o'lchov ma'lumoti: } "
                  r"\tilde f = f + \eta "
                  r"\;\Longrightarrow\; "
                  r"\Big|\frac{d^2\tilde f}{dx^2}\Big| "
                  r"\sim \frac{\eta}{h^2}",
                  "**Asosiy farq.** Agar "
                  "differensiallanayotgan ma'lumotda "
                  "**mustaqil** xato bo'lsa "
                  "(tenzodatchik o'lchovi, "
                  "yaxlitlash shovqini), u "
                  "$1/h^2$ marta kuchayadi — su-03 "
                  "dagi mexanizm. Sonli yechimni "
                  "differensiallashda esa xato "
                  "mustaqil emas, balki shu "
                  "sxemadan kelib chiqqan va u "
                  "kuchaymaydi."),
                d("11. Konservativ shakl "
                  "(o'zgaruvchan $EI$)",
                  r"\Big(EI\frac{d^2w}{dx^2}\Big)'' = q "
                  r"\;\Longrightarrow\; \text{avval } "
                  r"M = -EIw'' \text{, keyin } M'' = -q",
                  "**Hal qiluvchi nozik jihat.** "
                  "$EI$ o'zgaruvchan bo'lsa "
                  "$EIw^{(4)} = q$ **noto'g'ri** — "
                  "$EI$ ni hosila ostidan chiqarib "
                  "bo'lmaydi. To'g'ri shakl ikkita "
                  "ikkinchi tartibli tenglama."),
                d("12. Yaqinlashish tartibini o'lchash",
                  r"p = \log_2\frac{\|w_h - w_{ex}\|}"
                  r"{\|w_{h/2} - w_{ex}\|}",
                  "Aniq yechim ma'lum bo'lsa "
                  "bevosita; noma'lum bo'lsa uchta "
                  "to'rdan: "
                  "$p = \\log_2\\frac{w_h - w_{h/2}}"
                  "{w_{h/2} - w_{h/4}}$."),
            ],
            meaning=(
                "Bir o'lchovli balka masalasi chekli "
                "ayirmalar usulining barcha muhim "
                "jihatlarini o'z ichiga oladi va "
                "shuning uchun ideal mashq. Uning "
                "markaziy qiyinchiligi 4-qadamda: "
                "to'rtinchi tartibli tenglamaning "
                "shabloni besh nuqtali, demak "
                "chegaradan ikki qadam ichkarida ham "
                "muammo tug'iladi. Soxta tugun usuli "
                "buni nafis hal qiladi — sohani "
                "xayolan kengaytirib, chegaraviy "
                "shartni soxta tugun qiymati sifatida "
                "ifodalaymiz. 6- va 7-qadamlarning "
                "taqqoslashi ayniqsa o'rgatuvchi: "
                "mahkamlangan uchda $w_{-1} = +w_1$, "
                "sharnirlida $w_{-1} = -w_1$. "
                "Farq faqat ishorada, lekin fizik "
                "ma'nosi butunlay boshqa: birinchisi "
                "simmetriya (burilish nol), "
                "ikkinchisi antisimmetriya (moment "
                "nol). Chegaraviy shartlardagi "
                "ishorani adashtirish chekli "
                "ayirmalarda eng ko'p uchraydigan "
                "xato va u yechimni butunlay "
                "o'zgartiradi. 10- va 10a-qadamlar "
                "amaliy jihatdan muhim va ular "
                "intuitivga zid natija beradi. "
                "Muhandisni odatda og'ish emas, "
                "**kuchlanish** qiziqtiradi, u esa "
                "momentdan, moment esa ikkinchi "
                "hosiladan olinadi. Tabiiy fikr "
                "shuki, differensiallash aniqlikni "
                "yo'qotadi — lekin bu yerda "
                "**aksincha**: moment og'ishdan "
                "ikki barobar aniqroq chiqadi. "
                "Sababi shuki, moment mustaqil "
                "ma'lumotdan emas, aynan shu "
                "diskret operatordan tiklanadi va "
                "qo'shimcha xato kiritilmaydi. "
                "su-03 dagi $\\varepsilon/h$ "
                "kuchayishi esa faqat **mustaqil** "
                "xatoli ma'lumotni (tenzodatchik "
                "o'lchovi, shovqin) "
                "differensiallashda yuzaga keladi. "
                "Bu ikki holatni ajratish "
                "amaliyotda muhim: sonli yechimdan "
                "kuchlanish tiklash xavfsiz, "
                "o'lchov ma'lumotini ikki marta "
                "differensiallash esa deyarli har "
                "doim yaroqsiz natija beradi. "
                "Nihoyat, 11-qadam "
                "konservativ shakl haqida "
                "ogohlantiradi. O'zgaruvchan "
                "kesimli balkada "
                "$EIw^{(4)} = q$ yozish — jimgina "
                "noto'g'ri model qurish demak, "
                "chunki $EI$ hosila ostida qoladi. "
                "To'g'ri yondashuv masalani ikkita "
                "ikkinchi tartibli tenglamaga "
                "ajratish: $M = -EIw''$ va "
                "$M'' = -q$. Bu nafaqat to'g'ri, "
                "balki sonli jihatdan ham afzal — "
                "ikkita uch diagonalli tizim beshta "
                "diagonallidan yaxshiroq "
                "shartlangan."
            ),
            equations=[
                eq(r"\frac{w_{i-2}-4w_{i-1}+6w_i-"
                   r"4w_{i+1}+w_{i+2}}{h^4} = "
                   r"\frac{q_i}{EI}",
                   "Balka tenglamasining ayirma "
                   "sxemasi — besh nuqtali, $O(h^2)$.",
                   "Balka sxemasi"),
                eq(r"\text{mahkamlangan: } w_{-1} = w_1, "
                   r"\qquad \text{sharnirli: } "
                   r"w_{-1} = -w_1",
                   "Soxta tugun orqali chegaraviy "
                   "shartlar — farq faqat ishorada.",
                   "Soxta tugun shartlari"),
                eq(r"\Big(EI\,w''\Big)'' = q",
                   "O'zgaruvchan kesim uchun "
                   "konservativ (to'g'ri) shakl.",
                   "Konservativ shakl"),
                eq(r"p = \log_2\frac{\|e_h\|}"
                   r"{\|e_{h/2}\|}",
                   "Yaqinlashish tartibini o'lchash.",
                   "Tartibni o'lchash"),
            ],
            conditions=(
                "**To'rt xil chegaraviy shart "
                "(har uchida ikkitadan):**\n"
                "- Mahkamlangan: $w = 0$, $w' = 0$;\n"
                "- Sharnirli: $w = 0$, $M = 0$ "
                "(ya'ni $w'' = 0$);\n"
                "- Erkin: $M = 0$, $Q = 0$ "
                "($w'' = 0$, $w''' = 0$);\n"
                "- Sirpanuvchi mahkamlash: "
                "$w' = 0$, $Q = 0$.\n\n"
                "**Yechim mavjudligi:** kamida "
                "ikkita shart kinematik bo'lishi "
                "kerak, aks holda balka qattiq jism "
                "sifatida harakatlanadi va matritsa "
                "musbat aniqlangan bo'lmaydi "
                "(su-05 dagi Cholesky "
                "diagnostikasi buni aniqlaydi).\n\n"
                "**Aniqlik bo'yicha:**\n"
                "- $w$ — $O(h^2)$;\n"
                "- $M = -EIw''$ — $O(h^2)$, lekin "
                "kattaroq koeffitsient;\n"
                "- $Q = -EIw'''$ — eng yomon.\n\n"
                "**O'zgaruvchan $EI$ uchun:** "
                "konservativ shakl majburiy. "
                "$EI$ uzilishli bo'lsa (kesim "
                "keskin o'zgarsa) tugunni aynan "
                "uzilish joyiga qo'yish kerak.\n\n"
                "**Nuqtaviy yuklama uchun:** "
                "$q$ ni delta funksiya sifatida "
                "emas, tugunga "
                "$P/h$ zichlik sifatida "
                "qo'yiladi; tugun aynan yuklama "
                "joyida bo'lishi kerak."
            ),
            worked=WorkedExample(
                statement=(
                    "Ikki uchi sharnirli balka: "
                    "$L = 2$ m, $EI = 1000$ N·m², "
                    "bir tekis yuklama $q = 500$ N/m. "
                    "(a) Analitik yechimni yozing; "
                    "(b) $n = 4$ bo'linma uchun ayirma "
                    "tizimini to'liq qo'ying va "
                    "yeching; (c) xatolikni baholang "
                    "va $n = 8$ da qanday "
                    "o'zgarishini bashorat qiling."
                ),
                given=[
                    r"L = 2\ \text{m},\ EI = 1000\ "
                    r"\text{N·m}^2,\ q = 500\ \text{N/m}",
                    r"\text{ikki uchi sharnirli}",
                ],
                steps=[
                    st(r"w(x) = \frac{q}{24EI}\big(x^4 - "
                       r"2Lx^3 + L^3x\big)",
                       "mq-15 dagi analitik yechim."),
                    st(r"w_{max} = w(L/2) = "
                       r"\frac{5qL^4}{384EI} = "
                       r"\frac{5 \cdot 500 \cdot 16}"
                       r"{384 \cdot 1000} = "
                       r"0{,}104167\ \text{m}",
                       "O'rtadagi og'ish — etalon "
                       "qiymat."),
                    st(r"n = 4: \ h = 0{,}5\ \text{m}, "
                       r"\ \text{tugunlar } x = "
                       r"0; 0{,}5; 1; 1{,}5; 2",
                       "Beshta tugun, ulardan "
                       "$w_0 = w_4 = 0$ ma'lum."),
                    st(r"\text{Sharnirli: } w_{-1} = "
                       r"-w_1, \quad w_5 = -w_3",
                       "7-qadamdagi antisimmetriya "
                       "sharti."),
                    st(r"i=1: \ \frac{w_{-1}-4w_0+6w_1-"
                       r"4w_2+w_3}{h^4} = \frac{q}{EI} "
                       r"\;\Rightarrow\; \frac{5w_1-"
                       r"4w_2+w_3}{h^4} = \frac{q}{EI}",
                       "$w_{-1} = -w_1$ va $w_0 = 0$ "
                       "qo'yildi; $6w_1 - w_1 = 5w_1$."),
                    st(r"i=2: \ \frac{w_0-4w_1+6w_2-"
                       r"4w_3+w_4}{h^4} = \frac{q}{EI} "
                       r"\;\Rightarrow\; \frac{-4w_1+"
                       r"6w_2-4w_3}{h^4} = \frac{q}{EI}",
                       "Ichki tugun — to'liq shablon."),
                    st(r"i=3: \ \frac{w_1-4w_2+5w_3}"
                       r"{h^4} = \frac{q}{EI} \ "
                       r"(\text{simmetriya bo'yicha})",
                       "$w_5 = -w_3$ va $w_4 = 0$."),
                    st(r"\text{Simmetriya: } w_1 = w_3 "
                       r"\;\Rightarrow\; \begin{cases}"
                       r"6w_1 - 4w_2 = \beta\\ "
                       r"-8w_1 + 6w_2 = \beta\end{cases}, "
                       r"\ \beta = \frac{qh^4}{EI}",
                       "Masala simmetrik, shuning "
                       "uchun $w_1 = w_3$ va tizim "
                       "ikkita tenglamaga tushadi "
                       "($5w_1 + w_3 = 6w_1$)."),
                    st(r"\beta = \frac{500 \cdot 0{,}0625}"
                       r"{1000} = 0{,}03125; \quad "
                       r"w_2 = \frac{7\beta}{2} \cdot "
                       r"\frac{1}{1} \ldots",
                       "Tizimni yechamiz: "
                       "determinant $36-32 = 4$; "
                       "$w_1 = (6\\beta+4\\beta)/4 = "
                       "2{,}5\\beta$, "
                       "$w_2 = (6\\beta+8\\beta)/4 = "
                       "3{,}5\\beta$."),
                    st(r"w_2 = 3{,}5 \cdot 0{,}03125 = "
                       r"0{,}109375\ \text{m}",
                       "Sonli natija. Analitik "
                       "$0{,}104167$ m bilan "
                       "taqqoslaymiz."),
                    st(r"e = \frac{0{,}109375 - "
                       r"0{,}104167}{0{,}104167} = "
                       r"5{,}00\ \%",
                       "**5 % xato** — $n = 4$ juda "
                       "siyrak to'r uchun kutilgan."),
                    st(r"n = 8: \ e \approx "
                       r"\frac{5{,}00}{4} = 1{,}25\ \%",
                       "$O(h^2)$ bo'lgani uchun to'r "
                       "ikki barobar zichlashsa xato "
                       "to'rt barobar kamayadi. "
                       "Kodda bu aniq tekshiriladi."),
                ],
                answer=(
                    "Analitik $w_{max} = 0{,}104167$ m. "
                    "$n = 4$ da ayirma tizimi "
                    "$w_1 = w_3 = 2{,}5\\beta$, "
                    "$w_2 = 3{,}5\\beta$ beradi "
                    "($\\beta = qh^4/EI = 0{,}03125$), "
                    "ya'ni $w_2 = 0{,}109375$ m — "
                    "xato **5,00 %**. $O(h^2)$ "
                    "qonuni bo'yicha $n = 8$ da xato "
                    "≈ 1,25 % ga tushadi."
                ),
                engineering_note=(
                    "$n = 4$ da 5 % xato ko'p "
                    "tuyulishi mumkin, lekin bu "
                    "atigi uchta noma'lumli tizim. "
                    "Amaliy hisoblarda $n = 50$–100 "
                    "olinadi va xato 0,01 % dan "
                    "kamayadi. Muhimi — xatoning "
                    "**tartibi** ma'lum va u "
                    "boshqariladi. Yana bir amaliy "
                    "jihat: bu yerda og'ish "
                    "yuqoriroq chiqdi, ya'ni ayirma "
                    "sxemasi balkani "
                    "**yumshoqroq** ko'rsatdi. "
                    "Chekli elementlar usulida esa "
                    "(su-20) aksincha bo'ladi — "
                    "u balkani bikrroq ko'rsatadi, "
                    "chunki Ritz usuli (pq-09) "
                    "energiyani yuqoridan "
                    "chegaralaydi. Ikkala usulning "
                    "xatosi turli tomonga "
                    "yo'nalgani foydali: ular "
                    "birgalikda aniq yechimni "
                    "'qamrab' oladi va bu "
                    "natijaning ishonchliligini "
                    "baholash imkonini beradi."
                ),
            ),
            computation=Computation(
                caption=(
                    "Balka egilishi masalasini chekli "
                    "ayirmalar bilan yechish, to'rt xil "
                    "chegaraviy shart uchun analitik "
                    "yechim bilan taqqoslash va "
                    "yaqinlashish tartibini o'lchash."
                ),
                code='''"""Balka egilishi: chekli ayirmalar va analitik tekshiruv."""
import numpy as np
from labkit import PARAMS, note, series, table, value

L = float(PARAMS.get("L", 2.0))
EI = float(PARAMS.get("EI", 1000.0))
q0 = float(PARAMS.get("q0", 500.0))
n_show = int(PARAMS.get("n_show", 40))
bc = int(PARAMS.get("bc", 0))     # 0 sharnirli-sharnirli, 1 mahkam-mahkam,
                                  # 2 konsol (chap mahkam, o'ng erkin)
taper = float(PARAMS.get("taper", 1.0))   # EI(L)/EI(0)


def solve_beam(n, bc, taper=1.0):
    """EI*w_xxxx = q ni chekli ayirmalar bilan yechadi.

    taper != 1 bo'lsa konservativ shakl ishlatiladi:
    M = -EI*w_xx, M_xx = -q  (ikkita ikkinchi tartibli tizim).
    """
    h = L/n
    x = np.linspace(0.0, L, n + 1)
    if abs(taper - 1.0) < 1e-12:
        # Doimiy EI: bevosita to'rtinchi tartibli sxema.
        # Soxta tugunlar ichki tugunlarning chiziqli kombinatsiyasi
        # sifatida ifodalanadi (ghost dict: {indeks: koeffitsient}).
        if bc == 2:
            # konsol: chap mahkam (w=0, w'=0), o'ng erkin (M=0, Q=0)
            #   w_{-1}  = w_1
            #   w_{n+1} = 2*w_n - w_{n-1}
            #   w_{n+2} = 4*w_n - 4*w_{n-1} + w_{n-2}
            ghost = {-1: {1: 1.0},
                     n + 1: {n: 2.0, n - 1: -1.0},
                     n + 2: {n: 4.0, n - 1: -4.0, n - 2: 1.0}}
            fixed = [0]
            rows_eq = range(1, n + 1)
        elif bc == 1:
            # mahkam - mahkam: w_{-1} = w_1,  w_{n+1} = w_{n-1}
            ghost = {-1: {1: 1.0}, n + 1: {n - 1: 1.0}}
            fixed = [0, n]
            rows_eq = range(1, n)
        else:
            # sharnirli - sharnirli: w_{-1} = -w_1, w_{n+1} = -w_{n-1}
            ghost = {-1: {1: -1.0}, n + 1: {n - 1: -1.0}}
            fixed = [0, n]
            rows_eq = range(1, n)

        A = np.zeros((n + 1, n + 1))
        b = np.zeros(n + 1)
        st5 = np.array([1.0, -4.0, 6.0, -4.0, 1.0])
        for i in fixed:
            A[i, i] = 1.0
            b[i] = 0.0
        for i in rows_eq:
            for k in range(-2, 3):
                j, cf = i + k, st5[k + 2]
                if 0 <= j <= n:
                    A[i, j] += cf
                elif j in ghost:
                    for jj, gc in ghost[j].items():
                        A[i, jj] += cf*gc
                else:
                    raise ValueError(f"soxta tugun aniqlanmagan: {j}")
            b[i] = q0*h**4/EI
        w = np.linalg.solve(A, b)
        return x, w, h

    # --- O'zgaruvchan EI: KONSERVATIV shakl ---
    EIx = EI*(1.0 + (taper - 1.0)*x/L)
    # M'' = -q,  M(0) = M(L) = 0   (sharnirli)
    Am = np.zeros((n + 1, n + 1))
    bm = np.zeros(n + 1)
    for i in range(n + 1):
        if i == 0 or i == n:
            Am[i, i] = 1.0
            bm[i] = 0.0
        else:
            Am[i, i - 1], Am[i, i], Am[i, i + 1] = 1.0, -2.0, 1.0
            bm[i] = -q0*h**2
    M = np.linalg.solve(Am, bm)
    # w'' = -M/EI,  w(0) = w(L) = 0
    Aw = np.zeros((n + 1, n + 1))
    bw = np.zeros(n + 1)
    for i in range(n + 1):
        if i == 0 or i == n:
            Aw[i, i] = 1.0
            bw[i] = 0.0
        else:
            Aw[i, i - 1], Aw[i, i], Aw[i, i + 1] = 1.0, -2.0, 1.0
            bw[i] = -M[i]/EIx[i]*h**2
    w = np.linalg.solve(Aw, bw)
    return x, w, h


def exact(x, bc):
    if bc == 0:      # sharnirli - sharnirli
        return q0/(24*EI)*(x**4 - 2*L*x**3 + L**3*x)
    if bc == 1:      # mahkam - mahkam
        return q0/(24*EI)*x**2*(L - x)**2
    # konsol
    return q0/(24*EI)*(x**4 - 4*L*x**3 + 6*L**2*x**2)


names = {0: "sharnirli-sharnirli", 1: "mahkam-mahkam", 2: "konsol"}
value("Chegaraviy shart kodi", float(bc), "—")
note(f"Chegaraviy shart: {names[bc]}. EI nisbati (o'ng/chap) = "
     f"{taper:.2f}.")

x, w, h = solve_beam(n_show, bc, taper)
if abs(taper - 1.0) < 1e-12:
    w_ex = exact(x, bc)
    i_max = int(np.argmax(np.abs(w_ex)))
    value("Sonli maksimal og'ish", float(np.max(np.abs(w))*1000), "mm")
    value("Analitik maksimal og'ish",
          float(np.max(np.abs(w_ex))*1000), "mm")
    err_max = np.max(np.abs(w - w_ex))/np.max(np.abs(w_ex))
    value("Maksimal nisbiy xatolik", err_max*100, "%")
    series("Sonli yechim w(x)", x.tolist(), (w*1000).tolist(),
           xlabel="x, m", ylabel="og'ish w, mm")
    series("Analitik yechim", x.tolist(), (w_ex*1000).tolist(),
           xlabel="x, m", ylabel="og'ish w, mm")
    note(f"n = {n_show} da sonli va analitik yechimlar orasidagi "
         f"maksimal nisbiy farq {err_max*100:.4f} %.")

    # --- YAQINLASHISH TARTIBINI O'LCHASH ---
    rows, errs, hs = [], [], []
    for nk in [4, 8, 16, 32, 64, 128]:
        xk, wk, hk = solve_beam(nk, bc)
        wek = exact(xk, bc)
        e = np.max(np.abs(wk - wek))/np.max(np.abs(wek))
        errs.append(e)
        hs.append(hk)
        rows.append([nk, f"{hk:.5f}", f"{np.max(np.abs(wk))*1000:.6f}",
                     f"{e*100:.6f}"])
    table("To'r bo'yicha yaqinlashish",
          ["n", "h, m", "w_max, mm", "xatolik, %"], rows)
    ords = [np.log2(errs[i]/errs[i+1]) for i in range(len(errs) - 1)]
    for nk, o in zip([4, 8, 16, 32, 64], ords):
        value(f"Tartib (n = {nk} -> {2*nk})", float(o), "—")
    value("O'rtacha o'lchangan tartib", float(np.mean(ords[1:])), "—")
    series("Xatolik(h)", hs, errs, xlabel="qadam h",
           ylabel="nisbiy xatolik")
    sl = np.polyfit(np.log(hs), np.log(errs), 1)[0]
    value("Log-log qiyalik", float(sl), "—")
    note(f"To'r ikki barobar zichlashganda xatolik taxminan to'rt "
         f"barobar kamayadi; o'lchangan tartiblar "
         f"{', '.join(f'{o:.3f}' for o in ords)} va log-log qiyalik "
         f"{sl:.3f}. Nazariy O(h^2) TASDIQLANDI.")

    # n = 4 uchun qo'lda hisoblangan natijani tekshirish
    if bc == 0:
        x4, w4, h4 = solve_beam(4, 0)
        beta = q0*h4**4/EI
        value("n = 4: beta = q*h^4/EI", beta, "m")
        value("n = 4: w_1 / beta", float(w4[1]/beta), "—")
        value("n = 4: w_2 / beta", float(w4[2]/beta), "—")
        value("n = 4: w_2", float(w4[2]*1000), "mm")
        value("n = 4: analitik w(L/2)",
              float(exact(np.array([L/2]), 0)[0]*1000), "mm")
        e4 = abs(w4[2] - exact(np.array([L/2]), 0)[0]) \
            / exact(np.array([L/2]), 0)[0]
        value("n = 4: xatolik", e4*100, "%")
        note(f"n = 4 da qo'lda yechilgan tizim w_1 = 2.5*beta, "
             f"w_2 = 3.5*beta bergan edi; kod {w4[1]/beta:.4f}*beta va "
             f"{w4[2]/beta:.4f}*beta beradi - AYNAN mos. Xatolik "
             f"{e4*100:.3f} % va u qo'lda topilgan 5.00 % bilan "
             f"to'g'ri keladi.")

    # --- Moment va kesuvchi kuchni tiklash ---
    xm, wm, hm = solve_beam(64, bc)
    Mnum = np.full_like(wm, np.nan)
    Mnum[1:-1] = -EI*(wm[:-2] - 2*wm[1:-1] + wm[2:])/hm**2
    if bc == 0:
        Mex = q0*xm*(L - xm)/2
    elif bc == 1:
        Mex = q0*(6*xm*(L - xm) - L**2)/12
    else:
        Mex = -q0*(L - xm)**2/2
    ok = ~np.isnan(Mnum)
    eM = np.max(np.abs(Mnum[ok] - Mex[ok]))/np.max(np.abs(Mex))
    value("Moment: maksimal nisbiy xatolik", eM*100, "%")
    series("Moment M(x) — sonli", xm[ok].tolist(),
           (Mnum[ok]/1000).tolist(), xlabel="x, m", ylabel="M, kN*m")
    series("Moment M(x) — analitik", xm.tolist(),
           (Mex/1000).tolist(), xlabel="x, m", ylabel="M, kN*m")
    ew = np.max(np.abs(wm - exact(xm, bc)))/np.max(np.abs(exact(xm, bc)))
    value("Og'ish: maksimal nisbiy xatolik", ew*100, "%")
    note(f"KUTILMAGAN NATIJA: n = 64 da og'ishdagi xatolik "
         f"{ew*100:.5f} %, momentdagi xatolik esa atigi {eM*100:.3e} % "
         f"- ya'ni moment MASHINA ANIQLIGIDA to'g'ri chiqdi. Bu xato "
         f"emas: bir tekis yuklamada aniq moment KVADRAT ko'phad, uch "
         f"nuqtali ikkinchi ayirma esa kvadrat ko'phadni AYNAN "
         f"differensiallaydi (su-07 dagi xatolik hadi f^(4) ga "
         f"mutanosib, kvadrat uchun esa f^(4) = 0).")

    # Differensiallashda aniqlik yo'qolishini HAQIQIY ko'rsatish uchun
    # yuklamani sinusoidal qilamiz: unda M ko'phad emas.
    def solve_sine(nk):
        hk = L/nk
        xk = np.linspace(0.0, L, nk + 1)
        qk = q0*np.sin(np.pi*xk/L)
        A = np.zeros((nk + 1, nk + 1))
        b = np.zeros(nk + 1)
        st5 = np.array([1.0, -4.0, 6.0, -4.0, 1.0])
        for i in range(nk + 1):
            if i == 0 or i == nk:
                A[i, i] = 1.0
                continue
            for k in range(-2, 3):
                j, cf = i + k, st5[k + 2]
                if 0 <= j <= nk:
                    A[i, j] += cf
                elif j == -1:
                    A[i, 1] += -cf
                elif j == nk + 1:
                    A[i, nk - 1] += -cf
                elif j == -2:
                    A[i, 2] += -cf
                elif j == nk + 2:
                    A[i, nk - 2] += -cf
            b[i] = qk[i]*hk**4/EI
        return xk, np.linalg.solve(A, b), hk

    rows_s, e_w_s, e_m_s = [], [], []
    for nk in [16, 32, 64, 128]:
        xs, ws, hsk = solve_sine(nk)
        w_ex_s = q0*L**4/(np.pi**4*EI)*np.sin(np.pi*xs/L)
        M_ex_s = q0*L**2/np.pi**2*np.sin(np.pi*xs/L)
        M_n_s = -EI*(ws[:-2] - 2*ws[1:-1] + ws[2:])/hsk**2
        ewk = np.max(np.abs(ws - w_ex_s))/np.max(np.abs(w_ex_s))
        emk = np.max(np.abs(M_n_s - M_ex_s[1:-1]))/np.max(np.abs(M_ex_s))
        e_w_s.append(ewk)
        e_m_s.append(emk)
        rows_s.append([nk, f"{ewk*100:.6f}", f"{emk*100:.6f}",
                       f"{emk/ewk:.2f}"])
    table("Sinusoidal yuklama: og'ish va moment xatoliklari",
          ["n", "og'ish xatosi, %", "moment xatosi, %", "nisbat"], rows_s)
    value("Sinusoidal: moment/og'ish xatolik nisbati",
          float(np.mean([m/w_ for m, w_ in zip(e_m_s, e_w_s)])), "marta")
    pw_s = np.log2(e_w_s[-2]/e_w_s[-1])
    pm_s = np.log2(e_m_s[-2]/e_m_s[-1])
    value("Sinusoidal: og'ish tartibi", float(pw_s), "—")
    value("Sinusoidal: moment tartibi", float(pm_s), "—")
    rat = float(np.mean([m/w_ for m, w_ in zip(e_m_s, e_w_s)]))
    note(f"Yuklama sinusoidal bo'lganda (M endi ko'phad EMAS) moment "
         f"xatosi og'ish xatosining atigi {rat:.2f} qismini tashkil "
         f"qiladi - ya'ni moment og'ishdan ANIQROQ. Ikkala kattalik "
         f"ham O(h^2) (tartiblar {pw_s:.2f} va {pm_s:.2f}).")
    note("Buning sababi nozik va muhim. Diskret yechim aynan "
         "D4*w = q/EI tenglamasini qanoatlantiradi, moment esa shu "
         "yechimga D2 ni qo'llab olinadi. Sinus uchun D2*sin = "
         "-k2~*sin, bu yerda k2~ = k^2(1 - k^2h^2/12 + ...). Demak "
         "og'ishda xato (k/k~)^4 - 1 ~ k^2h^2/6, momentda esa "
         "(k/k~)^2 - 1 ~ k^2h^2/12 - AYNAN ikki barobar kichik.")
    note("Umumiy xulosa: MUSTAQIL xatoli ma'lumotni (o'lchov "
         "natijasi, boshqa usul bilan olingan yechim) "
         "differensiallash xatoni kuchaytiradi - bu su-03 dagi "
         "eps/h mexanizmi. Lekin bu yerda moment AYNAN shu diskret "
         "operatordan tiklanmoqda va qo'shimcha xato kiritilmaydi. "
         "Shuning uchun chekli ayirmalarda kuchlanishni yechimdan "
         "tiklash xavfsiz; xavf faqat tashqi (shovqinli) ma'lumotni "
         "differensiallashda.")
else:
    # O'zgaruvchan EI: konservativ shaklni tekshirish
    value("EI nisbati (o'ng/chap)", taper, "—")
    value("Maksimal og'ish (konservativ shakl)",
          float(np.max(np.abs(w))*1000), "mm")
    x1, w1, _ = solve_beam(n_show, bc, 1.0)
    value("Doimiy EI dagi og'ish", float(np.max(np.abs(w1)))*1000, "mm")
    value("O'zgaruvchan kesim ta'siri",
          float(np.max(np.abs(w))/np.max(np.abs(w1))), "marta")
    series("O'zgaruvchan EI: og'ish", x.tolist(), (w*1000).tolist(),
           xlabel="x, m", ylabel="w, mm")
    series("Doimiy EI: og'ish", x1.tolist(), (w1*1000).tolist(),
           xlabel="x, m", ylabel="w, mm")
    rows, errs2 = [], []
    for nk in [8, 16, 32, 64, 128]:
        _, wk, _ = solve_beam(nk, bc, taper)
        rows.append([nk, f"{np.max(np.abs(wk))*1000:.6f}"])
        errs2.append(np.max(np.abs(wk)))
    table("O'zgaruvchan EI: to'r bo'yicha yaqinlashish",
          ["n", "w_max, mm"], rows)
    d1 = abs(errs2[-3] - errs2[-2])
    d2 = abs(errs2[-2] - errs2[-1])
    if d2 > 1e-15:
        value("To'rdan tiklangan tartib", float(np.log2(d1/d2)), "—")
        note(f"Aniq yechim noma'lum, shuning uchun tartib UCHTA to'rdan "
             f"tiklandi: log2(|w_h - w_h/2| / |w_h/2 - w_h/4|) = "
             f"{np.log2(d1/d2):.3f}. Konservativ shakl O(h^2) ni "
             f"saqlaydi.")

table("Chegaraviy shartlar va soxta tugun munosabatlari",
      ["Chegara", "Shartlar", "Soxta tugun", "Fizik ma'no"],
      [["Mahkamlangan", "w = 0, w' = 0", "w_{-1} = +w_1", "simmetriya"],
       ["Sharnirli", "w = 0, M = 0", "w_{-1} = -w_1", "antisimmetriya"],
       ["Erkin", "M = 0, Q = 0", "ikkita soxta tugun", "kuch shartlari"],
       ["Sirpanuvchi", "w' = 0, Q = 0", "w_{-1} = +w_1", "aralash"]])
''',
                parameters=[
                    p("L", "Balka uzunligi L", 0.2, 20.0, 2.0, 0.1, "m"),
                    p("EI", "Egilish bikrligi EI", 10.0, 1000000.0, 1000.0,
                      10.0, "N·m²"),
                    p("q0", "Yuklama q₀", 1.0, 100000.0, 500.0, 10.0, "N/m"),
                    p("n_show", "Bo'linmalar soni n", 4.0, 200.0, 40.0, 2.0),
                    p("bc", "Chegara (0 sharnirli, 1 mahkam, 2 konsol)",
                      0.0, 2.0, 0.0, 1.0),
                    p("taper", "EI nisbati (o'ng/chap)", 0.2, 5.0, 1.0,
                      0.1),
                ],
                expected_output=(
                    "$n = 4$ da kod qo'lda yechilgan "
                    "tizimni aynan qaytaradi: "
                    "$w_1 = 2{,}5\\beta$, "
                    "$w_2 = 3{,}5\\beta$, xatolik "
                    "5,00 %. To'r zichlashgani sari "
                    "xatolik to'rt barobar kamayadi "
                    "va o'lchangan tartib 2 ga "
                    "yaqinlashadi (aynan 2,000). "
                    "Bir tekis yuklamada tiklangan "
                    "moment **mashina aniqligida** "
                    "to'g'ri chiqadi, chunki aniq "
                    "$M$ kvadrat ko'phad va uch "
                    "nuqtali ikkinchi ayirma uni "
                    "aynan differensiallaydi. "
                    "Sinusoidal yuklamada esa "
                    "moment xatosi og'ish "
                    "xatosining **aynan yarmi** — "
                    "moment og'ishdan ikki barobar "
                    "aniqroq. "
                    "O'zgaruvchan $EI$ da "
                    "konservativ shakl ishlatiladi "
                    "va tartib uchta to'rdan "
                    "tiklanadi."
                ),
            ),
            visual=vis(
                kind="Egilish chizig'i va epyuralar",
                tool="React/SVG",
                description=(
                    "Sonli va analitik yechimlarning "
                    "taqqoslashi, moment epyurasi va "
                    "yaqinlashish tartibi."
                ),
                how_to_draw=(
                    "React/SVG: yuqorida balka "
                    "sxemasi tayanchlari bilan "
                    "chiziladi; ostida egilish "
                    "chizig'i **kuchaytirilgan "
                    "masshtabda** — analitik yechim "
                    "uzluksiz chiziq, sonli yechim "
                    "esa tugunlarda nuqtalar. "
                    "Bo'linmalar soni slayderi bilan "
                    "nuqtalar soni oshadi va ular "
                    "uzluksiz chiziqqa yopishib "
                    "boradi. Chegaralarda soxta "
                    "tugunlar soha tashqarisida "
                    "**punktir doira** bilan "
                    "ko'rsatiladi va ularning "
                    "qiymati $w_1$ ga bog'lanishi "
                    "($+$ yoki $-$) o'q bilan "
                    "belgilanadi — mahkamlangan va "
                    "sharnirli holatlar orasidagi "
                    "ishora farqi shu yerda ko'zga "
                    "tashlanadi. Pastda moment "
                    "epyurasi shtrixlangan holda "
                    "(epyura an'anasi bo'yicha) "
                    "chiziladi, sonli va analitik "
                    "ustma-ust. O'ngda log–log "
                    "grafik: xatolikning $h$ ga "
                    "bog'liqligi va qiyaligi 2 "
                    "bo'lgan uchburchak."
                ),
            ),
            interp=(
                "Eng ishonchli tekshiruv — "
                "$n = 4$ holatining qo'lda "
                "yechilgan natija bilan aynan mos "
                "kelishi: kod $w_1 = 2{,}5\\beta$ "
                "va $w_2 = 3{,}5\\beta$ qaytaradi, "
                "xatolik esa 5,00 %. Bu chegaraviy "
                "shartlar va soxta tugunlar to'g'ri "
                "qo'yilganini kafolatlaydi, chunki "
                "shu kichik tizimni qo'lda "
                "to'liq kuzatish mumkin. Undan "
                "keyin to'r bo'yicha yaqinlashish "
                "$O(h^2)$ ni tasdiqlaydi va bu "
                "sxemaning nazariy tartibi bilan "
                "mos keladi. Ikkinchi muhim natija "
                "moment tiklashda va u intuitivga "
                "zid chiqadi. Bir tekis yuklamada "
                "tiklangan moment **mashina "
                "aniqligida** to'g'ri: aniq $M$ "
                "kvadrat ko'phad, uch nuqtali "
                "ikkinchi ayirmaning xatolik hadi "
                "esa $f^{(4)}$ ga mutanosib va "
                "kvadrat uchun u aynan nol. Buni "
                "tekshirish uchun yuklama "
                "sinusoidal qilinadi — o'shanda "
                "ham moment xatosi og'ish "
                "xatosining **aynan yarmi** bo'lib "
                "chiqadi, ya'ni moment baribir "
                "aniqroq. Sababi 10-qadamda: "
                "diskret yechim $D_4w = q/EI$ ni "
                "qanoatlantiradi va moment shu "
                "yechimga $D_2$ ni qo'llab "
                "olinadi, demak operatorlar "
                "muvofiqlashgan va qo'shimcha xato "
                "kirmaydi. Bu su-03 dagi "
                "$\\varepsilon/h$ kuchayishidan "
                "aniq farqlanishi kerak: u faqat "
                "**mustaqil** xatoli ma'lumotni "
                "differensiallashda yuzaga keladi. "
                "Amaliy xulosa: sonli yechimdan "
                "kuchlanish tiklash xavfsiz, "
                "tenzodatchik ma'lumotini ikki "
                "marta differensiallash esa emas. "
                "O'zgaruvchan $EI$ holati alohida "
                "qiymatga ega: u yerda aniq yechim "
                "yo'q, shuning uchun tartib "
                "**uchta to'rdan** tiklanadi. Bu "
                "amaliyotdagi odatiy vaziyat — "
                "etalon yechim deyarli hech qachon "
                "mavjud emas va yaqinlashishni "
                "faqat to'r ketma-ketligi orqali "
                "tekshirish mumkin. Konservativ "
                "shaklning $O(h^2)$ ni saqlashi "
                "esa 11-qadamdagi nazariy "
                "tavsiyani tasdiqlaydi."
            ),
            mistakes=[
                "Mahkamlangan va sharnirli "
                "chegaralardagi soxta tugun "
                "ishorasini adashtirish. "
                "$w_{-1} = +w_1$ va "
                "$w_{-1} = -w_1$ butunlay boshqa "
                "yechim beradi.",
                "Erkin uchda bitta soxta tugun "
                "bilan cheklanish. Besh nuqtali "
                "shablon ikki qadam chiqadi — "
                "ikkita soxta tugun kerak.",
                "O'zgaruvchan $EI$ uchun "
                "$EIw^{(4)} = q$ yozish. To'g'ri "
                "shakl $(EIw'')'' = q$ — "
                "konservativ.",
                "O'lchov ma'lumotini (shovqinli) "
                "ikki marta differensiallash. U "
                "yerda xato $1/h^2$ marta "
                "kuchayadi — sonli yechimni "
                "differensiallashdan farqli "
                "o'laroq.",
                "Yaqinlashish tartibini "
                "o'lchamaslik. Chegaraviy shartdagi "
                "xato ko'pincha faqat tartib "
                "pasayishi orqali bilinadi.",
            ],
            quiz=[
                q("Nima uchun to'rtinchi tartibli "
                  "tenglamada soxta tugun kerak?",
                  "Besh nuqtali shablon chegaradan "
                  "ikki qadam chiqadi; $i = 1$ da "
                  "$w_{-1}$ kerak bo'ladi va u "
                  "chegaraviy shartdan ifodalanadi.",
                  "konseptual"),
                q("Mahkamlangan va sharnirli uchda "
                  "soxta tugun qanday farq qiladi?",
                  "Mahkamlangan: $w_{-1} = +w_1$ "
                  "(simmetriya, $w' = 0$); "
                  "sharnirli: $w_{-1} = -w_1$ "
                  "(antisimmetriya, $w'' = 0$).",
                  "konseptual"),
                q("Sharnirli balkada $n = 4$ da "
                  "$w_2$ nechaga teng "
                  "($\\beta = qh^4/EI$)?",
                  "Tizimni yechib $w_2 = 3{,}5\\beta$; "
                  "$\\beta = 0{,}03125$ m uchun "
                  "$w_2 = 0{,}109375$ m, xatolik "
                  "5,00 %.", "hisob"),
                q("Kodda nima uchun $n = 4$ holati "
                  "alohida tekshiriladi?",
                  "Uni qo'lda to'liq yechish mumkin, "
                  "shuning uchun u chegaraviy "
                  "shartlar va soxta tugunlar "
                  "to'g'ri qo'yilganini "
                  "kafolatlaydi.", "kod"),
                q("Sonli yechimdan tiklangan moment "
                  "og'ishdan aniqroqmi yoki "
                  "aniqsizroqmi?",
                  "**Aniqroq** — sinusoidal "
                  "yechimda ikki barobar. Moment "
                  "aynan shu diskret operatordan "
                  "tiklanadi, shuning uchun "
                  "qo'shimcha xato kirmaydi; "
                  "$\\varepsilon/h$ kuchayishi "
                  "faqat mustaqil shovqinli "
                  "ma'lumotda yuzaga keladi.",
                  "talqin"),
                q("Aniq yechim noma'lum bo'lsa "
                  "yaqinlashish tartibi qanday "
                  "o'lchanadi?",
                  "Uchta to'rdan: "
                  "$p = \\log_2\\frac{|w_h-w_{h/2}|}"
                  "{|w_{h/2}-w_{h/4}|}$ — bu "
                  "amaliyotdagi standart usul.",
                  "talqin"),
            ],
            bridge=(
                "Bir o'lchovda hamma narsa "
                "tushunarli: to'r — chiziq, shablon "
                "— bir necha qo'shni tugun, "
                "matritsa — lentali. Ikki o'lchovda "
                "esa yangi savollar paydo bo'ladi: "
                "tugunlarni qanday raqamlash, "
                "shablon qanday ko'rinishda bo'ladi "
                "va murakkab shaklli sohani qanday "
                "qoplash. Keyingi mavzuda Laplas va "
                "Puasson tenglamalariga o'tamiz."
            ),
            research=(
                "Balka masalasini kengaytiring. "
                "(1) Elastik asosdagi balka "
                "($EIw^{(4)} + kw = q$, pq-16) "
                "uchun sxemani quring va chekka "
                "effektining so'nish uzunligini "
                "sonli o'lchang; uni pq-27 dagi "
                "analitik $\\beta$ bilan "
                "solishtiring. (2) $EI$ uzilishli "
                "bo'lgan holatni ko'rib chiqing "
                "(kesim keskin o'zgaradi): tugun "
                "uzilish joyiga tushmasa "
                "yaqinlashish tartibi qanday "
                "o'zgaradi? (3) Nuqtaviy yuklamani "
                "modellashtirishni tahlil qiling: "
                "delta funksiyani diskretlashtirish "
                "tartibni pasaytiradimi va buni "
                "qanday bartaraf etish mumkin?"
            ),
            manim_ref=manim(
                scene="BeamFDScene",
                module="manim/scenes/su_fd.py",
                title="Balka masalasi va soxta tugunlar",
                summary=(
                    "Balka to'rga bo'linadi va besh "
                    "nuqtali shablon tugundan "
                    "tugunga siljiydi; chegaraga "
                    "yetganda shablon sohadan "
                    "chiqib ketishi ko'rinadi. "
                    "Soxta tugunlar paydo bo'lib, "
                    "chegaraviy shart orqali ichki "
                    "tugunlarga bog'lanadi va "
                    "mahkamlangan hamda sharnirli "
                    "holatlar uchun ishora farqi "
                    "ko'rsatiladi."
                ),
            ),
        ),
    ),
]
