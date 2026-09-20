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
]
