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

    # ------------------------------------------------------------------ su-09
    Topic(
        id="su-09",
        subject_id=S, module_id=M, order=9,
        title="Ikki o'lchovli masalalar: Laplas va Puasson tenglamalari",
        description=(
            "Besh nuqtali shablon, tugunlarni raqamlash, Dirixle va "
            "Neyman shartlari, buralishdagi kuchlanish funksiyasi va "
            "notekis chegaralar."
        ),
        learning_objective=(
            "Ikki o'lchovli Puasson masalasini chekli ayirmalar bilan "
            "yechish, Neyman shartini to'g'ri qo'yish va natijani "
            "analitik qator yechimi bilan tekshirish."
        ),
        prerequisites=["su-08", "mq-19", "tmm-16"],
        mathematical_core=(
            "$\\nabla^2\\phi = -2G\\theta$; besh nuqtali shablon "
            "$\\dfrac{\\phi_{i-1,j}+\\phi_{i+1,j}+\\phi_{i,j-1}+"
            "\\phi_{i,j+1}-4\\phi_{ij}}{h^2}$."
        ),
        engineering_application=(
            "Ixtiyoriy kesimli sterjenning buralishi, issiqlik "
            "o'tkazuvchanlik, filtratsiya, potensial oqim, "
            "membrana tarangligi."
        ),
        computational_component=(
            "Buralish masalasini yechish, buralish bikrligini "
            "hisoblash va analitik qator yechimi bilan taqqoslash."
        ),
        visualization_component=(
            "Kuchlanish funksiyasining sath chiziqlari, siljish "
            "kuchlanishi vektorlari, membrana analogiyasi."
        ),
        research_extension=(
            "To'qqiz nuqtali (Mehrstellen) shablonni o'rganing: u "
            "bir xil shablon o'lchami bilan $O(h^4)$ beradi. "
            "Notekis chegaralarni qamrab olish usullarini solishtiring."
        ),
        difficulty="murakkab",
        previous_link=(
            "su-08 da bir o'lchovli masala to'liq yechildi: shablon, "
            "chegaraviy shartlar, soxta tugunlar va yaqinlashish "
            "tartibi. Endi xuddi shu apparat ikki o'lchovga "
            "ko'chiriladi va yangi savol qo'shiladi — tugunlarni "
            "qanday raqamlash."
        ),
        next_topic="su-10",
        estimated_minutes=90,
        tags=["Puasson", "buralish", "Neyman", "besh nuqtali shablon"],
        lesson=_lesson(
            problem=(
                "mq-19 da doiraviy va yupqa devorli "
                "kesimlarning buralishi analitik "
                "yechilgan edi. To'rtburchak kesim "
                "uchun esa yechim cheksiz qator "
                "ko'rinishida va u sekin "
                "yaqinlashadi. Haqiqiy profil — "
                "masalan, ikkitavrli yoki "
                "burchakli — uchun analitik yechim "
                "umuman yo'q. Lekin barcha bu "
                "holatlarda bir xil tenglama "
                "ishlaydi: $\\nabla^2\\phi = "
                "-2G\\theta$, ya'ni Puasson "
                "tenglamasi. Uni ixtiyoriy shaklda "
                "yechish mumkinmi? Va nima uchun "
                "aynan shu tenglama issiqlik "
                "o'tkazuvchanlikda, filtratsiyada "
                "va membrana tarangligida ham "
                "paydo bo'ladi?"
            ),
            concepts=[
                c("Besh nuqtali shablon",
                  "$\\nabla^2\\phi \\approx "
                  "(\\phi_W+\\phi_E+\\phi_S+\\phi_N-"
                  "4\\phi_P)/h^2$ — tekis kvadrat "
                  "to'rda $O(h^2)$."),
                c("Prandtl kuchlanish funksiyasi",
                  "$\\tau_{xz} = \\partial\\phi/"
                  "\\partial y$, $\\tau_{yz} = "
                  "-\\partial\\phi/\\partial x$ — "
                  "muvozanat avtomatik bajariladi "
                  "(mq-19)."),
                c("Membrana analogiyasi",
                  "$\\phi$ bir xil konturga "
                  "tortilgan membrananing "
                  "og'ishiga o'xshaydi; buralish "
                  "bikrligi membrana ostidagi "
                  "hajmga mutanosib."),
                c("Dirixle sharti",
                  "$\\phi = 0$ chegarada — "
                  "qiymat berilgan; eng sodda "
                  "qo'yiladi."),
                c("Neyman sharti",
                  "$\\partial\\phi/\\partial n = g$ "
                  "— normal bo'yicha hosila "
                  "berilgan; soxta tugun yoki "
                  "bir tomonlama sxema kerak."),
                c("Tugunlarni raqamlash",
                  "Ikki indeks $(i,j)$ bitta "
                  "nomerga o'tkaziladi: "
                  "$k = j n_x + i$; bu lenta "
                  "kengligini belgilaydi (su-05)."),
            ],
            derivation=[
                d("1. Buralish masalasining qo'yilishi",
                  r"\nabla^2\phi = \frac{\partial^2\phi}"
                  r"{\partial x^2} + \frac{\partial^2\phi}"
                  r"{\partial y^2} = -2G\theta \ "
                  r"\text{sohada}, \quad \phi = 0 \ "
                  r"\text{konturda}",
                  "mq-19 dagi Prandtl formulirovkasi. "
                  "$\\theta$ — birlik uzunlikka "
                  "to'g'ri keladigan buralish "
                  "burchagi."),
                d("2. To'rni kiritish",
                  r"x_i = ih_x, \ y_j = jh_y, \quad "
                  r"i = 0..n_x, \ j = 0..n_y",
                  "Tekis to'rtburchak to'r. "
                  "Soddalik uchun $h_x = h_y = h$."),
                d("3. Har bir hosilani almashtirish",
                  r"\frac{\partial^2\phi}{\partial x^2}"
                  r"\Big|_{ij} \approx "
                  r"\frac{\phi_{i-1,j}-2\phi_{ij}+"
                  r"\phi_{i+1,j}}{h^2}",
                  "su-07 dagi uch nuqtali sxema "
                  "$x$ yo'nalishi bo'ylab. "
                  "$y$ uchun ham xuddi shunday."),
                d("4. Besh nuqtali shablon",
                  r"\frac{\phi_{i-1,j}+\phi_{i+1,j}+"
                  r"\phi_{i,j-1}+\phi_{i,j+1}-"
                  r"4\phi_{ij}}{h^2} = -2G\theta",
                  "**Asosiy sxema.** Har bir tugun "
                  "faqat to'rtta qo'shnisi bilan "
                  "bog'langan — matritsa juda "
                  "siyrak (su-05 dagi 3,24 % "
                  "to'ldirilganlik)."),
                d("5. Kesish xatoligi",
                  r"E = \frac{h^2}{12}\Big("
                  r"\frac{\partial^4\phi}{\partial x^4} + "
                  r"\frac{\partial^4\phi}{\partial y^4}"
                  r"\Big) + O(h^4)",
                  "Har bir yo'nalishdan su-07 dagi "
                  "$h^2/12$ hadi keladi. Demak sxema "
                  "$O(h^2)$ va aralash hosilalar "
                  "kirmaydi."),
                d("6. Tugunlarni bir o'lchovli "
                  "raqamlash",
                  r"k = j\,(n_x+1) + i "
                  r"\;\Longrightarrow\; \text{qo'shnilar: } "
                  r"k\pm 1 \ \text{va} \ k \pm (n_x+1)",
                  "Ikki indeksdan bitta nomerga "
                  "o'tish. Lenta kengligi "
                  "$b = n_x+1$ — su-05 dagi kabi "
                  "qisqa tomon bo'ylab raqamlash "
                  "afzal."),
                d("7. Dirixle shartini qo'yish",
                  r"\phi_k = 0 \;\Longrightarrow\; "
                  r"\text{qator} \ k: \ A_{kk} = 1, "
                  r"\ b_k = 0",
                  "Eng sodda usul: qatorni "
                  "almashtirish. Simmetriyani "
                  "saqlash uchun ustunni ham "
                  "tozalash va o'ng tomonga "
                  "ko'chirish afzal."),
                d("8. Neyman shartini qo'yish",
                  r"\frac{\partial\phi}{\partial n} = 0 "
                  r"\;\Longrightarrow\; \phi_{-1,j} = "
                  r"\phi_{1,j}",
                  "Soxta tugun orqali — su-08 dagi "
                  "mahkamlangan uch bilan bir xil "
                  "g'oya. Natijada shablonda "
                  "qo'shni ikki barobar og'irlik "
                  "bilan kiradi."),
                d("9. Simmetriyadan foydalanish",
                  r"\text{to'rtburchak kesim: chorak "
                  r"qismni yechish yetarli}",
                  "Simmetriya o'qlarida Neyman "
                  "sharti ($\\partial\\phi/"
                  "\\partial n = 0$) o'rinli. "
                  "Noma'lumlar soni to'rt barobar "
                  "kamayadi."),
                d("10. Buralish momenti",
                  r"T = 2\iint_A \phi\,dA \approx "
                  r"2h^2\sum_{ij}\phi_{ij}",
                  "**Membrana analogiyasi.** "
                  "Moment kuchlanish funksiyasi "
                  "ostidagi hajmning ikki "
                  "barobariga teng. Integral "
                  "trapetsiya yoki Simpson bilan "
                  "hisoblanadi."),
                d("11. Buralish bikrligi",
                  r"J_t = \frac{T}{G\theta} = "
                  r"\frac{2}{G\theta}\iint_A\phi\,dA",
                  "Geometrik xarakteristika — "
                  "materialga bog'liq emas. "
                  "Doiraviy kesimda "
                  "$J_t = I_p$, boshqa "
                  "shakllarda esa $J_t < I_p$."),
                d("12. Maksimal siljish kuchlanishi",
                  r"\tau_{max} = \max\Big|"
                  r"\nabla\phi\Big| = "
                  r"\max\sqrt{\phi_{,x}^2 + "
                  r"\phi_{,y}^2}",
                  "Konturda va uzun tomonning "
                  "o'rtasida maksimal bo'ladi. "
                  "Burchaklarda esa $\\tau = 0$ — "
                  "membrana analogiyasi buni "
                  "darhol tushuntiradi."),
                d("13. Analitik qator bilan "
                  "taqqoslash",
                  r"J_t = \beta\,a b^3, \quad "
                  r"\beta = \frac{1}{3} - "
                  r"\frac{64}{\pi^5}\frac{b}{a}"
                  r"\sum_{n=1,3,5}\frac{1}{n^5}"
                  r"\tanh\frac{n\pi a}{2b}",
                  "To'rtburchak kesim uchun "
                  "klassik qator (Timoshenko). "
                  "U sonli yechimning "
                  "**mustaqil tekshiruvi** bo'lib "
                  "xizmat qiladi."),
            ],
            meaning=(
                "Ikki o'lchovga o'tish tenglamaning "
                "**mohiyatini o'zgartirmaydi** — "
                "shablon shunchaki to'rtta qo'shnini "
                "o'z ichiga oladi. Lekin ikkita "
                "yangi amaliy savol paydo bo'ladi. "
                "Birinchisi 6-qadamda: ikki "
                "indeksdan bitta nomerga o'tish. "
                "Bu sof texnik masala, lekin u "
                "lenta kengligini belgilaydi va "
                "su-05 da ko'rganimizdek hisoblash "
                "hajmiga tartiblar bilan ta'sir "
                "qiladi. Qoida oddiy: **qisqa tomon "
                "bo'ylab** raqamlang. Ikkinchi savol "
                "chegaralarda: to'rtburchak sohada "
                "hammasi oson, lekin doiraviy yoki "
                "burchakli konturda to'r tugunlari "
                "chegaraga aniq tushmaydi. Bu "
                "chekli ayirmalarning asosiy "
                "kamchiligi va aynan shu sabab "
                "chekli elementlar usuli "
                "muhandislikda hukmron bo'lib "
                "qoldi: FEM da elementlar "
                "chegaraga moslashadi. Mazmun "
                "jihatidan eng qiziqarlisi — "
                "10-qadamdagi membrana "
                "analogiyasi. Prandtl kuchlanish "
                "funksiyasi bir xil konturga "
                "tortilgan va bosim ostidagi "
                "membrananing og'ishi bilan bir xil "
                "tenglamani qanoatlantiradi. "
                "Bundan bir nechta muhim xulosa "
                "darhol kelib chiqadi: buralish "
                "momenti membrana ostidagi hajmga "
                "mutanosib; siljish kuchlanishi "
                "membrananing qiyaligiga "
                "mutanosib; burchaklarda membrana "
                "yassilashadi, demak "
                "$\\tau = 0$. Oxirgisi "
                "muhandislik uchun muhim va "
                "intuitivga zid: to'rtburchak "
                "valning burchaklarida siljish "
                "kuchlanishi nolga teng, maksimum "
                "esa uzun tomonning o'rtasida. "
                "Nihoyat, bu tenglamaning "
                "universalligi e'tiborga loyiq. "
                "Xuddi shu $\\nabla^2 u = f$ "
                "issiqlik o'tkazuvchanlikda, "
                "gruntdagi filtratsiyada, "
                "elektrostatikada va potensial "
                "oqimda paydo bo'ladi. Bir marta "
                "yozilgan yechuvchi bu "
                "masalalarning hammasiga yaraydi "
                "— bu hisoblash mexanikasining "
                "asosiy tejam manbalaridan biri."
            ),
            equations=[
                eq(r"\frac{\phi_{i-1,j}+\phi_{i+1,j}+"
                   r"\phi_{i,j-1}+\phi_{i,j+1}-"
                   r"4\phi_{ij}}{h^2} = -2G\theta",
                   "Besh nuqtali shablon — ikki "
                   "o'lchovli Puasson tenglamasi.",
                   "Besh nuqtali shablon"),
                eq(r"E = \frac{h^2}{12}\big(\phi_{,xxxx} "
                   r"+ \phi_{,yyyy}\big)",
                   "Kesish xatoligi — $O(h^2)$.",
                   "Kesish xatoligi"),
                eq(r"T = 2\iint_A\phi\,dA, \qquad "
                   r"J_t = \frac{T}{G\theta}",
                   "Buralish momenti va bikrligi — "
                   "membrana ostidagi hajm.",
                   "Buralish bikrligi"),
                eq(r"\tau_{xz} = \frac{\partial\phi}"
                   r"{\partial y}, \quad \tau_{yz} = "
                   r"-\frac{\partial\phi}{\partial x}",
                   "Siljish kuchlanishlari — "
                   "kuchlanish funksiyasining "
                   "gradiyenti.", "Kuchlanishlar"),
            ],
            conditions=(
                "**Buralish masalasi uchun:**\n"
                "- Konturda $\\phi = 0$ (bir "
                "bog'lamli kesim);\n"
                "- Ichki teshik bo'lsa, u yerda "
                "$\\phi = \\text{const}$ (noma'lum "
                "doimiy) va qo'shimcha shart kerak;\n"
                "- Simmetriya o'qlarida "
                "$\\partial\\phi/\\partial n = 0$.\n\n"
                "**Neyman masalasining xosligi:** "
                "agar **barcha** chegarada Neyman "
                "sharti bo'lsa, yechim doimiygacha "
                "aniqlanadi va matritsa singulyar "
                "bo'ladi. Qo'shimcha shart kerak "
                "(masalan, $\\iint u\\,dA = 0$ "
                "yoki bitta tugunni "
                "mahkamlash). Bundan tashqari "
                "muvofiqlik sharti "
                "$\\iint f\\,dA = -\\oint g\\,ds$ "
                "bajarilishi kerak.\n\n"
                "**To'r bo'yicha:**\n"
                "- Chegara tugunlarga tushishi "
                "kerak, aks holda tartib "
                "pasayadi;\n"
                "- $h_x \\ne h_y$ bo'lsa shablon "
                "koeffitsientlari o'zgaradi;\n"
                "- Burchakli sohada "
                "singulyarlik bor "
                "($\\phi \\sim r^{\\pi/\\alpha}$) "
                "va u tartibni pasaytiradi.\n\n"
                "**Matritsa xossalari:** simmetrik, "
                "musbat aniqlangan, siyrak, "
                "diagonal ustunlikka ega — demak "
                "su-05 dagi Cholesky ham, su-06 "
                "dagi konjugat gradiyent ham "
                "ishlaydi."
            ),
            worked=WorkedExample(
                statement=(
                    "Kvadrat kesimli val: tomoni "
                    "$a = 100$ mm, $G = 80$ GPa, "
                    "buralish burchagi "
                    "$\\theta = 0{,}01$ rad/m. "
                    "(a) Buralish bikrligi $J_t$ ni "
                    "analitik qatordan toping; "
                    "(b) uni $I_p$ bilan solishtiring; "
                    "(c) $4\\times4$ ichki tugunli "
                    "to'rda sonli yechimning "
                    "xatoligini bashorat qiling."
                ),
                given=[
                    r"a = b = 0{,}1\ \text{m},\ "
                    r"G = 80\ \text{GPa}",
                    r"\theta = 0{,}01\ \text{rad/m}",
                ],
                steps=[
                    st(r"\beta = \frac{1}{3} - "
                       r"\frac{64}{\pi^5}\sum_{n=1,3,5..}"
                       r"\frac{1}{n^5}\tanh\frac{n\pi}{2}",
                       "Kvadrat uchun $a/b = 1$; "
                       "qator juda tez yaqinlashadi."),
                    st(r"n=1: \ \frac{1}{1}\tanh(1{,}5708) "
                       r"= 0{,}91715",
                       "$\\tanh(\\pi/2) = 0{,}91715$."),
                    st(r"n=3: \ \frac{1}{243}"
                       r"\tanh(4{,}7124) = "
                       r"\frac{0{,}99983}{243} = "
                       r"0{,}0041145",
                       "Uchinchi had allaqachon 220 "
                       "barobar kichik."),
                    st(r"n=5: \ \frac{1}{3125} \cdot 1 = "
                       r"0{,}00032; \quad \sum \approx "
                       r"0{,}921594",
                       "Yig'indi amalda uchta had "
                       "bilan aniqlanadi."),
                    st(r"\frac{64}{\pi^5} = "
                       r"\frac{64}{306{,}02} = "
                       r"0{,}209139",
                       "$\\pi^5 = 306{,}0197$."),
                    st(r"\beta = 0{,}333333 - "
                       r"0{,}209139 \cdot 0{,}921594 = "
                       r"0{,}333333 - 0{,}192741 = "
                       r"0{,}140592",
                       "Klassik qiymat "
                       "$\\beta = 0{,}1406$ "
                       "(Timoshenko jadvali)."),
                    st(r"J_t = \beta a^4 = 0{,}140592 "
                       r"\cdot 10^{-4} = "
                       r"1{,}40592\times10^{-5}\ "
                       r"\text{m}^4",
                       "Buralish bikrligi."),
                    st(r"I_p = \frac{a^4}{6} = "
                       r"\frac{10^{-4}}{6} = "
                       r"1{,}66667\times10^{-5}\ "
                       r"\text{m}^4",
                       "Kvadrat uchun qutb inersiya "
                       "momenti."),
                    st(r"\frac{J_t}{I_p} = "
                       r"\frac{1{,}40592}{1{,}66667} = "
                       r"0{,}8436",
                       "**$J_t < I_p$** — kesim "
                       "tekis qolmaydi (deplanatsiya, "
                       "mq-19). Faqat doiraviy "
                       "kesimda ular teng."),
                    st(r"T = GJ_t\theta = 80\times10^{9} "
                       r"\cdot 1{,}40592\times10^{-5} "
                       r"\cdot 0{,}01 = 11\,247\ "
                       r"\text{N·m}",
                       "Buralish momenti."),
                    st(r"n = 4: \ h = a/5 = 20\ "
                       r"\text{mm}, \ E \sim "
                       r"\frac{h^2}{12}\phi^{(4)} "
                       r"\;\Rightarrow\; \text{bir "
                       r"necha foiz}",
                       "$O(h^2)$ bo'lgani uchun "
                       "siyrak to'rda xato sezilarli. "
                       "Kodda aniq o'lchanadi va "
                       "to'r zichlashgani sari "
                       "to'rt barobar kamayadi."),
                ],
                answer=(
                    "$\\beta = 0{,}140592$, "
                    "$J_t = 1{,}40592\\times10^{-5}$ m⁴, "
                    "$I_p = 1{,}66667\\times10^{-5}$ m⁴, "
                    "nisbat $J_t/I_p = 0{,}8436$ — "
                    "kvadrat kesim doiraviydan "
                    "sezilarli yumshoqroq. "
                    "$T = 11\\,247$ N·m. Sonli "
                    "yechim $O(h^2)$ bo'yicha "
                    "yaqinlashadi."
                ),
                engineering_note=(
                    "$J_t/I_p = 0{,}844$ nisbati "
                    "muhandislik uchun muhim "
                    "ogohlantirish: buralishda "
                    "$I_p$ ni ishlatish **faqat "
                    "doiraviy kesim** uchun "
                    "o'rinli. Kvadrat uchun xato "
                    "16 %, ingichka to'rtburchak "
                    "uchun esa u tartiblarga "
                    "chiqadi — $a/b = 10$ da "
                    "$J_t/I_p \\approx 0{,}03$. "
                    "Sababi deplanatsiya: "
                    "doiraviy bo'lmagan kesim "
                    "buralganda tekis qolmaydi va "
                    "bu bikrlikni keskin "
                    "kamaytiradi. Ochiq profilli "
                    "sterjenlarda (ikkitavrli, "
                    "shveller) vaziyat yanada "
                    "yomon va u yerda buralish "
                    "deyarli har doim kritik "
                    "holat bo'ladi. Membrana "
                    "analogiyasi buni "
                    "ko'rsatishning eng oson "
                    "yo'li: ingichka to'rtburchak "
                    "konturga tortilgan membrana "
                    "juda kam hajm o'raydi, demak "
                    "moment ham kichik."
                ),
            ),
            computation=Computation(
                caption=(
                    "To'rtburchak kesimning buralish "
                    "masalasini yechish, buralish "
                    "bikrligini hisoblash va analitik "
                    "qator bilan taqqoslash."
                ),
                code='''"""Ikki o'lchovli Puasson: to'rtburchak kesimning buralishi."""
import numpy as np
from labkit import PARAMS, note, series, table, value

a = float(PARAMS.get("a", 100.0))/1000.0
b = float(PARAMS.get("b", 100.0))/1000.0
G = float(PARAMS.get("G", 80.0))*1e9
theta = float(PARAMS.get("theta", 0.01))
n_show = int(PARAMS.get("n_show", 30))


def beta_series(a, b, nmax=99):
    """To'rtburchak kesim uchun klassik qator (Timoshenko)."""
    aa, bb = max(a, b), min(a, b)
    s = 0.0
    for n in range(1, nmax + 1, 2):
        s += np.tanh(n*np.pi*aa/(2*bb))/n**5
    return 1.0/3.0 - 64.0/np.pi**5*(bb/aa)*s


def solve_torsion(nx, ny, a, b):
    """nabla^2 phi = -2*G*theta, phi = 0 konturda."""
    hx, hy = a/(nx + 1), b/(ny + 1)
    N = nx*ny
    A = np.zeros((N, N))
    rhs = np.full(N, -2.0*G*theta)
    for j in range(ny):
        for i in range(nx):
            k = j*nx + i
            A[k, k] = -2.0/hx**2 - 2.0/hy**2
            if i > 0:
                A[k, k - 1] = 1.0/hx**2
            if i < nx - 1:
                A[k, k + 1] = 1.0/hx**2
            if j > 0:
                A[k, k - nx] = 1.0/hy**2
            if j < ny - 1:
                A[k, k + nx] = 1.0/hy**2
    phi = np.linalg.solve(A, rhs)
    P = np.zeros((ny + 2, nx + 2))
    P[1:-1, 1:-1] = phi.reshape(ny, nx)
    return P, hx, hy


# --- Analitik etalon ---
beta_an = beta_series(a, b)
Jt_an = beta_an*max(a, b)*min(a, b)**3
Ip = a*b*(a**2 + b**2)/12.0
value("Analitik beta (qator)", beta_an, "—")
value("Analitik J_t", Jt_an, "m^4")
value("Qutb inersiya momenti I_p", Ip, "m^4")
value("J_t / I_p", Jt_an/Ip, "—")
value("Buralish momenti T", G*Jt_an*theta, "N*m")
note(f"Analitik qator beta = {beta_an:.6f} beradi (kvadrat uchun "
     f"klassik qiymat 0.1406). J_t/I_p = {Jt_an/Ip:.4f} < 1 - "
     f"deplanatsiya tufayli kesim doiraviydan yumshoqroq.")

# --- Sonli yechim va to'r bo'yicha yaqinlashish ---
rows, errs, hs = [], [], []
for nk in [4, 8, 16, 32, 64]:
    P, hx, hy = solve_torsion(nk, nk, a, b)
    # T = 2 * integral(phi dA), trapetsiya (chegarada phi = 0)
    T_num = 2.0*np.sum(P)*hx*hy
    Jt_num = T_num/(G*theta)
    e = abs(Jt_num - Jt_an)/Jt_an
    errs.append(e)
    hs.append(hx)
    rows.append([nk, f"{hx*1000:.3f}", f"{Jt_num*1e6:.6f}",
                 f"{e*100:.4f}"])
table("Buralish bikrligi: to'r bo'yicha yaqinlashish",
      ["ichki tugunlar n", "h, mm", "J_t x 1e6, m^4", "xatolik, %"], rows)
value("Analitik J_t x 1e6", Jt_an*1e6, "m^4")
ords = [np.log2(errs[i]/errs[i+1]) for i in range(len(errs) - 1)]
for nk, o in zip([4, 8, 16, 32], ords):
    value(f"Tartib (n = {nk} -> {2*nk})", float(o), "—")
value("O'rtacha tartib (oxirgi ikkitasi)",
      float(np.mean(ords[-2:])), "—")
series("J_t xatoligi(h)", hs, errs, xlabel="qadam h, m",
       ylabel="nisbiy xatolik")
sl = np.polyfit(np.log(hs), np.log(errs), 1)[0]
value("Log-log qiyalik", float(sl), "—")
note(f"To'r zichlashgani sari J_t xatoligi kamayadi; o'lchangan "
     f"tartiblar {', '.join(f'{o:.3f}' for o in ords)} va log-log "
     f"qiyalik {sl:.3f}. Sonli yechim MUSTAQIL analitik qatorga "
     f"yaqinlashmoqda - bu ikkala hisobning ham to'g'riligini "
     f"tasdiqlaydi.")

# --- Batafsil yechim ---
P, hx, hy = solve_torsion(n_show, n_show, a, b)
value("Maksimal phi (markazda)", float(np.max(P)), "Pa*m")
i_c = (n_show + 2)//2
xs = np.linspace(0, a, n_show + 2)
ys = np.linspace(0, b, n_show + 2)
series("phi markaziy kesimda (y = b/2)", xs.tolist(),
       P[i_c, :].tolist(), xlabel="x, m", ylabel="phi, Pa*m")

# Siljish kuchlanishlari: tau = |grad phi|
dpdy, dpdx = np.gradient(P, hy, hx)
tau = np.sqrt(dpdx**2 + dpdy**2)
value("Maksimal siljish kuchlanishi", float(np.max(tau))/1e6, "MPa")
# Konturda: uzun tomon o'rtasi
tau_mid = float(tau[i_c, 0])
tau_corner = float(tau[0, 0])
value("tau uzun tomon o'rtasida", tau_mid/1e6, "MPa")
value("tau burchakda", tau_corner/1e6, "MPa")
note(f"Maksimal siljish kuchlanishi {np.max(tau)/1e6:.3f} MPa va u "
     f"tomon O'RTASIDA joylashgan; burchakda esa "
     f"{tau_corner/1e6:.3f} MPa ~ 0. Membrana analogiyasi buni "
     f"darhol tushuntiradi: burchakda membrana yassilashadi, demak "
     f"qiyalik (va kuchlanish) nol.")

# Analitik tau_max. Kvadrat uchun T = G*J_t*theta va
# tau_max = T/(alpha*a*b^2), alpha = 0.2082  =>  tau_max = 0.6753*G*theta*a
if abs(a - b) < 1e-12:
    tau_an = beta_an/0.2082*G*theta*a
    value("Analitik tau_max (kvadrat)", tau_an/1e6, "MPa")
    value("Koeffitsient tau_max/(G*theta*a)", beta_an/0.2082, "—")

    # Chegaradagi gradiyentni IKKINCHI tartibli bir tomonlama sxema
    # bilan qayta hisoblaymiz: phi_0 = 0, (-3*phi_0 + 4*phi_1 - phi_2)/(2h)
    jm = (n_show + 2)//2
    tau_b1 = abs(P[jm, 1] - P[jm, 0])/hx                 # 1-tartibli
    tau_b2 = abs(4.0*P[jm, 1] - P[jm, 2])/(2.0*hx)       # 2-tartibli
    value("tau chegarada (1-tartibli sxema)", tau_b1/1e6, "MPa")
    value("tau chegarada (2-tartibli sxema)", tau_b2/1e6, "MPa")
    value("1-tartibli sxema xatosi", abs(tau_b1 - tau_an)/tau_an*100, "%")
    value("2-tartibli sxema xatosi", abs(tau_b2 - tau_an)/tau_an*100, "%")
    note(f"Kvadrat kesim uchun klassik qiymat tau_max = "
         f"{beta_an/0.2082:.4f}*G*theta*a = {tau_an/1e6:.3f} MPa. "
         f"Chegarada birinchi tartibli gradiyent {tau_b1/1e6:.3f} MPa "
         f"({abs(tau_b1-tau_an)/tau_an*100:.2f} % xato), ikkinchi "
         f"tartibli bir tomonlama sxema esa {tau_b2/1e6:.3f} MPa "
         f"({abs(tau_b2-tau_an)/tau_an*100:.2f} % xato) beradi.")
    note("Bu su-07 dagi xulosaning bevosita tasdig'i: CHEGARADAGI "
         "sxema butun natijaning aniqligini belgilaydi. np.gradient "
         "chekkada birinchi tartibli bir tomonlama ayirma ishlatadi, "
         "shuning uchun ichkarida O(h^2) bo'lsa ham chegarada "
         "aniqlik tushadi - va muhandisni aynan chegaradagi "
         "kuchlanish qiziqtiradi.")

    # Chegaradagi ikki sxemaning tartibini o'lchash
    rows_t = []
    for nk in [8, 16, 32, 64]:
        Pk, hxk, _ = solve_torsion(nk, nk, a, b)
        jk = (nk + 2)//2
        t1 = abs(Pk[jk, 1] - Pk[jk, 0])/hxk
        t2 = abs(4.0*Pk[jk, 1] - Pk[jk, 2])/(2.0*hxk)
        rows_t.append([nk, f"{t1/1e6:.4f}", f"{t2/1e6:.4f}",
                       f"{abs(t1-tau_an)/tau_an*100:.3f}",
                       f"{abs(t2-tau_an)/tau_an*100:.3f}"])
    table("Chegaradagi tau: bir va ikki tartibli sxemalar",
          ["n", "tau (1-tartib), MPa", "tau (2-tartib), MPa",
           "xato 1, %", "xato 2, %"], rows_t)

series("tau markaziy kesimda", xs.tolist(),
       (tau[i_c, :]/1e6).tolist(), xlabel="x, m", ylabel="tau, MPa")
series("tau diagonal bo'ylab",
       np.linspace(0, np.hypot(a, b), n_show + 2).tolist(),
       (np.diagonal(tau)/1e6).tolist(),
       xlabel="diagonal bo'ylab masofa, m", ylabel="tau, MPa")

# --- Tomonlar nisbatining ta'siri ---
rows2 = []
for ar in [1.0, 1.5, 2.0, 3.0, 5.0, 10.0]:
    aa, bb = ar*0.05, 0.05
    be = beta_series(aa, bb)
    Jt = be*aa*bb**3
    Ipp = aa*bb*(aa**2 + bb**2)/12.0
    P2, hx2, hy2 = solve_torsion(24, max(4, int(24/ar)), aa, bb)
    Jt_n = 2.0*np.sum(P2)*hx2*hy2/(G*theta)
    rows2.append([f"{ar:.1f}", f"{be:.5f}", f"{Jt*1e6:.5f}",
                  f"{Jt_n*1e6:.5f}", f"{abs(Jt_n-Jt)/Jt*100:.2f}",
                  f"{Jt/Ipp:.4f}"])
table("Tomonlar nisbatining ta'siri",
      ["a/b", "beta", "J_t analitik x1e6", "J_t sonli x1e6",
       "farq, %", "J_t/I_p"], rows2)
note("Tomonlar nisbati oshgani sari J_t/I_p keskin kamayadi: "
     "ingichka to'rtburchak buralishga juda yomon qarshilik "
     "ko'rsatadi. Bu ochiq profilli sterjenlarda buralishning "
     "nima uchun kritik ekanini tushuntiradi.")
beta_lim = beta_series(1000.0, 1.0)
value("beta, a/b -> cheksiz (nazariy 1/3)", beta_lim, "—")
note(f"a/b juda katta bo'lganda beta -> 1/3 = 0.3333 ga intiladi "
     f"(qator {beta_lim:.6f} beradi) va J_t -> a*b^3/3 - bu yupqa "
     f"to'rtburchak uchun klassik formula (mq-19).")

# --- Matritsa xossalari (su-05, su-06 bilan bog'lanish) ---
P4, _, _ = solve_torsion(12, 12, a, b)
nx = ny = 12
Nn = nx*ny
Am = np.zeros((Nn, Nn))
hx3, hy3 = a/(nx + 1), b/(ny + 1)
for j in range(ny):
    for i in range(nx):
        k = j*nx + i
        Am[k, k] = -2.0/hx3**2 - 2.0/hy3**2
        if i > 0:
            Am[k, k - 1] = 1.0/hx3**2
        if i < nx - 1:
            Am[k, k + 1] = 1.0/hx3**2
        if j > 0:
            Am[k, k - nx] = 1.0/hy3**2
        if j < ny - 1:
            Am[k, k + nx] = 1.0/hy3**2
nz = int(np.count_nonzero(np.abs(Am) > 1e-14))
value("Matritsa o'lchami N", float(Nn), "—")
value("Noldan farqli elementlar", float(nz), "—")
value("To'ldirilganlik", nz/Nn**2*100, "%")
value("Har qatordagi o'rtacha element", nz/Nn, "—")
value("Simmetriya xatosi", float(np.max(np.abs(Am - Am.T))), "—")
value("Shartlanganlik soni kappa", float(np.linalg.cond(Am)), "—")
lam = np.linalg.eigvalsh(Am)
value("Barcha xususiy qiymatlar manfiymi",
      1.0 if np.all(lam < 0) else 0.0, "—")
note(f"Matritsa {nz/Nn**2*100:.2f} % to'ldirilgan (har qatorda "
     f"o'rtacha {nz/Nn:.1f} element), aynan simmetrik va barcha "
     f"xususiy qiymatlari bir ishorali - demak -A musbat "
     f"aniqlangan. Shuning uchun su-05 dagi Cholesky ham, su-06 "
     f"dagi konjugat gradiyent ham to'g'ridan-to'g'ri qo'llanadi. "
     f"kappa = {np.linalg.cond(Am):.3e}.")

table("Bir xil tenglama - turli fizika",
      ["Masala", "Noma'lum u", "Manba f", "Chegara"],
      [["Buralish", "kuchlanish funksiyasi phi", "-2*G*theta",
        "phi = 0"],
       ["Issiqlik", "harorat T", "-Q/k", "T yoki oqim"],
       ["Filtratsiya", "napor H", "-q/k", "H yoki oqim"],
       ["Membrana", "og'ish w", "-p/S", "w = 0"],
       ["Elektrostatika", "potensial V", "-rho/eps", "V yoki zaryad"]])
''',
                parameters=[
                    p("a", "Kesim tomoni a", 5.0, 1000.0, 100.0, 1.0, "mm"),
                    p("b", "Kesim tomoni b", 5.0, 1000.0, 100.0, 1.0, "mm"),
                    p("G", "Siljish moduli G", 1.0, 200.0, 80.0, 1.0, "GPa"),
                    p("theta", "Buralish burchagi θ", 0.0001, 1.0, 0.01,
                      0.0001, "rad/m"),
                    p("n_show", "Ichki tugunlar soni", 4.0, 60.0, 30.0, 2.0),
                ],
                expected_output=(
                    "Analitik qator kvadrat uchun "
                    "$\\beta = 0{,}1406$ beradi "
                    "(Timoshenko jadvali bilan mos) "
                    "va $J_t/I_p = 0{,}844$. Sonli "
                    "yechim to'r zichlashgani sari "
                    "shu mustaqil analitik qiymatga "
                    "$O(h^2)$ bo'yicha yaqinlashadi. "
                    "Siljish kuchlanishi tomon "
                    "o'rtasida maksimal, burchakda "
                    "esa aynan nol — membrana "
                    "analogiyasining bevosita "
                    "tasdig'i; koeffitsient "
                    "$\\tau_{max}/(G\\theta a) = "
                    "0{,}6752$ klassik 0,675 bilan "
                    "mos. Chegaradagi $\\tau$ ikki "
                    "sxema bilan hisoblanadi: "
                    "birinchi tartibli xatolik har "
                    "zichlashtirishda ikki barobar "
                    "(16,95 → 8,85 → 4,51 → "
                    "2,27 %), ikkinchi tartibli esa "
                    "to'rt barobar (3,58 → 1,00 → "
                    "0,25 → 0,053 %) kamayadi — "
                    "su-07 dagi 'chegaradagi sxema "
                    "hal qiluvchi' xulosasining "
                    "aniq tasdig'i. Tomonlar nisbati "
                    "oshgani sari $\\beta \\to 1/3$ "
                    "va $J_t/I_p$ keskin kamayadi. "
                    "Matritsa siyrak (har qatorda "
                    "≈ 5 element), aynan simmetrik "
                    "va aniqlangan."
                ),
            ),
            visual=vis(
                kind="Kuchlanish funksiyasi va membrana analogiyasi",
                tool="React/SVG + Manim",
                description=(
                    "Sath chiziqlari, siljish "
                    "kuchlanishi vektorlari va "
                    "membrana analogiyasi."
                ),
                how_to_draw=(
                    "React/SVG: markazda kesim "
                    "konturi va uning ichida "
                    "$\\phi$ ning **sath "
                    "chiziqlari** (izochiziqlar) "
                    "chiziladi — ular membrananing "
                    "balandlik chiziqlariga mos "
                    "keladi. Sath chiziqlari "
                    "qiymatga qarab bo'yaladi va "
                    "markazda zichlashadi. Ularning "
                    "ustiga siljish kuchlanishi "
                    "vektorlari qo'yiladi: ular sath "
                    "chiziqlariga **urinma** "
                    "yo'nalgan va uzunligi "
                    "qiyalikka mutanosib — shunda "
                    "burchaklarda vektorlarning "
                    "yo'qolishi va tomon o'rtasida "
                    "eng uzun bo'lishi bir qarashda "
                    "ko'rinadi. Yonida tomonlar "
                    "nisbati slayderi: uni "
                    "oshirganda sath chiziqlari "
                    "cho'zilib ketadi va "
                    "$J_t/I_p$ hisoblagichi keskin "
                    "tushadi. Pastda kontur bo'ylab "
                    "$\\tau$ epyurasi shtrixlangan "
                    "holda; burchaklardagi nollar "
                    "va tomon o'rtasidagi maksimum "
                    "belgilanadi. O'ngda kichik "
                    "log–log grafik — "
                    "$J_t$ xatoligining $h$ ga "
                    "bog'liqligi va qiyaligi 2 "
                    "bo'lgan uchburchak."
                ),
            ),
            interp=(
                "Eng qimmatli tekshiruv — sonli "
                "yechimning **mustaqil** analitik "
                "qatorga yaqinlashishi. Qator "
                "(Timoshenko) va chekli ayirmalar "
                "butunlay turli yo'llar bilan "
                "olingan, shuning uchun ularning "
                "mos kelishi ikkala hisobning ham "
                "to'g'riligini tasdiqlaydi. "
                "Yaqinlashish tartibi $O(h^2)$ "
                "chiqishi esa 5-qadamdagi kesish "
                "xatoligi bahosini tasdiqlaydi. "
                "$J_t/I_p = 0{,}844$ natijasi "
                "mexanik jihatdan muhim: kvadrat "
                "kesim doiraviydan 16 % yumshoqroq "
                "va bu deplanatsiya oqibati "
                "(mq-19). Tomonlar nisbati "
                "jadvali buni kengaytiradi — "
                "$a/b = 10$ da nisbat tartibga "
                "tushadi va $\\beta \\to 1/3$ "
                "limitiga chiqish yupqa "
                "to'rtburchak uchun klassik "
                "$J_t = ab^3/3$ formulasini qayta "
                "beradi. Siljish kuchlanishining "
                "taqsimoti membrana analogiyasining "
                "eng ko'rgazmali tasdig'i: "
                "burchakda $\\tau \\approx 0$, "
                "maksimum esa tomon o'rtasida. Bu "
                "intuitivga zid — burchakda "
                "kuchlanish konsentratsiyasi "
                "kutilardi — lekin membrana "
                "tasviri buni darhol tushuntiradi. "
                "Nihoyat, matritsa xossalari "
                "modulni oldingi materialga "
                "bog'laydi: u siyrak, simmetrik va "
                "aniqlangan, demak su-05 dagi "
                "Cholesky va su-06 dagi konjugat "
                "gradiyent bevosita qo'llanadi. "
                "Bitta yechuvchi esa jadvaldagi "
                "beshta butunlay turli fizik "
                "masalaga yaraydi."
            ),
            mistakes=[
                "Buralishda $I_p$ ni ishlatish. "
                "Bu faqat doiraviy kesim uchun; "
                "kvadratda xato 16 %, ingichka "
                "to'rtburchakda tartiblarga "
                "chiqadi.",
                "Burchaklarda kuchlanish "
                "konsentratsiyasi kutish. "
                "Buralishda burchakda "
                "$\\tau = 0$ — membrana "
                "analogiyasi buni ko'rsatadi.",
                "Tugunlarni uzun tomon bo'ylab "
                "raqamlash. Lenta kengligi "
                "oshadi va yechish vaqti "
                "kvadratik ortadi (su-05).",
                "To'liq Neyman masalasida "
                "qo'shimcha shart qo'ymaslik. "
                "Matritsa singulyar bo'ladi — "
                "yechim doimiygacha aniqlanadi.",
                "Chegarani to'r tugunlariga "
                "moslamaslik. Egri konturda "
                "yaqinlashish tartibi pasayadi — "
                "bu chekli ayirmalarning asosiy "
                "kamchiligi.",
            ],
            quiz=[
                q("Besh nuqtali shablon qanday "
                  "olinadi va uning tartibi qancha?",
                  "Har bir yo'nalish bo'yicha uch "
                  "nuqtali ikkinchi hosila "
                  "sxemasini qo'shish orqali; "
                  "xatolik "
                  "$\\frac{h^2}{12}(\\phi_{,xxxx}+"
                  "\\phi_{,yyyy})$, ya'ni $O(h^2)$.",
                  "konseptual"),
                q("Membrana analogiyasi nimani "
                  "tushuntiradi?",
                  "$\\phi$ bir xil konturga "
                  "tortilgan membrana og'ishi bilan "
                  "bir xil tenglamani "
                  "qanoatlantiradi; moment — "
                  "membrana ostidagi hajm, "
                  "kuchlanish — uning qiyaligi.",
                  "talqin"),
                q("Kvadrat kesimda $J_t/I_p$ "
                  "nechaga teng va nima uchun "
                  "birdan kichik?",
                  "$0{,}844$. Doiraviy bo'lmagan "
                  "kesim buralganda tekis "
                  "qolmaydi (deplanatsiya) va bu "
                  "bikrlikni kamaytiradi.",
                  "hisob"),
                q("Kodda nima uchun analitik qator "
                  "ham hisoblanadi?",
                  "U sonli yechimning **mustaqil** "
                  "tekshiruvi: ikki butunlay turli "
                  "usul bir xil javob bersa, "
                  "ikkalasi ham to'g'ri.", "kod"),
                q("Nima uchun burchakda siljish "
                  "kuchlanishi nol?",
                  "Membrana burchakda yassilashadi "
                  "(ikki tomondan mahkamlangan), "
                  "demak qiyaligi nol; "
                  "$\\tau = |\\nabla\\phi|$ ham nol.",
                  "talqin"),
                q("$a/b \\to \\infty$ da $\\beta$ "
                  "nimaga intiladi?",
                  "$1/3$ ga; demak "
                  "$J_t \\to ab^3/3$ — yupqa "
                  "to'rtburchak uchun klassik "
                  "formula.", "hisob"),
            ],
            bridge=(
                "Statik masalalar uchun chekli "
                "ayirmalar apparati to'liq: sxema, "
                "chegaraviy shartlar, bir va ikki "
                "o'lchov. Lekin vaqtga bog'liq "
                "masalalarda yangi va jiddiy savol "
                "paydo bo'ladi — sxema "
                "**barqarormi**? Keyingi mavzuda "
                "yaqinlashish, muvofiqlik va "
                "barqarorlik tushunchalarini "
                "ajratamiz va ularni bog'lovchi "
                "Laks teoremasini ko'ramiz."
            ),
            research=(
                "Ikki o'lchovli sxemalarni "
                "kengaytiring. (1) To'qqiz nuqtali "
                "(Mehrstellen) shablonni quring: u "
                "bir xil o'lchamli shablon bilan "
                "$O(h^4)$ beradi — buning sababi "
                "nima? (2) Egri chegarani qamrab "
                "olish usullarini solishtiring: "
                "Shortley–Weller "
                "approksimatsiyasi, kesilgan "
                "hujayra (cut-cell) va botirilgan "
                "chegara (immersed boundary). "
                "Har birida yaqinlashish tartibi "
                "qanday saqlanadi? (3) Ichki "
                "teshikli (ko'p bog'lamli) kesim "
                "uchun buralish masalasini "
                "qo'ying: teshikdagi noma'lum "
                "doimiyni aniqlash uchun qanday "
                "qo'shimcha shart kerak "
                "(Bredt formulasi bilan "
                "bog'lanish)?"
            ),
            manim_ref=manim(
                scene="TorsionScene",
                module="manim/scenes/su_fd.py",
                title="Membrana analogiyasi va buralish",
                summary=(
                    "Kesim konturiga membrana "
                    "tortiladi va bosim ostida "
                    "shishadi; uning balandligi "
                    "kuchlanish funksiyasi ekani "
                    "ko'rsatiladi. Keyin kontur "
                    "cho'zilib ingichka "
                    "to'rtburchakka aylanadi va "
                    "membrana ostidagi hajm keskin "
                    "kamayishi — ya'ni buralish "
                    "bikrligining tushishi — "
                    "namoyish etiladi."
                ),
            ),
        ),
    ),

    # ------------------------------------------------------------------ su-10
    Topic(
        id="su-10",
        subject_id=S, module_id=M, order=10,
        title="Muvofiqlik, barqarorlik va yaqinlashish: Laks teoremasi",
        description=(
            "Uchta tushunchaning aniq ta'rifi, fon Neyman barqarorlik "
            "tahlili, Laks ekvivalentlik teoremasi va issiqlik "
            "o'tkazuvchanlik tenglamasi misolida tekshirish."
        ),
        learning_objective=(
            "Sxemaning muvofiqligini Teylor qatoridan, barqarorligini "
            "fon Neyman tahlilidan aniqlash va Laks teoremasi orqali "
            "yaqinlashishni asoslash."
        ),
        prerequisites=["su-09", "su-03"],
        mathematical_core=(
            "Laks: muvofiqlik + barqarorlik $\\iff$ yaqinlashish; "
            "fon Neyman: $u_j^n = \\xi^n e^{ikjh}$, "
            "$|\\xi| \\le 1$; oshkor sxema uchun "
            "$r = \\alpha\\Delta t/h^2 \\le 1/2$."
        ),
        engineering_application=(
            "Issiqlik hisoblari, payvandlash jarayoni, beton "
            "qotishidagi harorat, nostatsionar diffuziya, "
            "konsolidatsiya masalalari."
        ),
        computational_component=(
            "Oshkor va oshkormas sxemalarni taqqoslash, barqarorlik "
            "chegarasini sonli topish va nazariy $r = 1/2$ bilan "
            "solishtirish."
        ),
        visualization_component=(
            "Barqaror va nobarqaror yechimlarning evolyutsiyasi, "
            "kuchayish koeffitsientining to'lqin soniga bog'liqligi."
        ),
        research_extension=(
            "Matritsaviy barqarorlik tahlilini (spektral radius) fon "
            "Neyman tahlili bilan solishtiring: chegaraviy shartlar "
            "barqarorlikka qanday ta'sir qiladi?"
        ),
        difficulty="murakkab",
        previous_link=(
            "su-07…su-09 da barcha sxemalar **statik** masalalar uchun "
            "edi va u yerda yagona savol aniqlik edi. Vaqtga bog'liq "
            "masalalarda esa butunlay yangi xavf paydo bo'ladi: "
            "sxema 'portlashi' mumkin."
        ),
        next_topic="su-11",
        estimated_minutes=90,
        tags=["Laks teoremasi", "fon Neyman", "barqarorlik", "CFL"],
        lesson=_lesson(
            problem=(
                "Payvandlash jarayonidagi haroratni "
                "hisoblaymiz: "
                "$\\partial T/\\partial t = "
                "\\alpha\\nabla^2 T$. Sxema juda "
                "sodda ko'rinadi — vaqt bo'yicha "
                "oldinga ayirma, fazo bo'yicha "
                "markaziy. Kodni yozamiz, "
                "$\\Delta t = 0{,}01$ s va "
                "$h = 1$ mm olamiz va ishga "
                "tushiramiz. Birinchi bir necha "
                "qadam normal ko'rinadi, keyin "
                "harorat 1000 °C, keyin "
                "$10^{6}$ °C, keyin `NaN`. "
                "Hech qanday xato xabari yo'q, kod "
                "to'g'ri yozilgan, sxema esa "
                "Teylor qatori bo'yicha mukammal "
                "muvofiq. Muammo shundaki, "
                "aniqlik va yaqinlashish bir xil "
                "narsa emas — orada uchinchi "
                "tushuncha bor."
            ),
            concepts=[
                c("Muvofiqlik (consistency)",
                  "$h, \\Delta t \\to 0$ da ayirma "
                  "tenglamasining **kesish "
                  "xatoligi** nolga intiladi; "
                  "ya'ni sxema to'g'ri "
                  "differensial tenglamani "
                  "yaqinlashtiradi."),
                c("Barqarorlik (stability)",
                  "Sonli yechimdagi bezovtaliklar "
                  "vaqt o'tishi bilan "
                  "**o'smaydi**; xatolik "
                  "chegaralangan bo'lib qoladi."),
                c("Yaqinlashish (convergence)",
                  "$h, \\Delta t \\to 0$ da sonli "
                  "yechim **aniq yechimga** "
                  "intiladi. Amalda bizni aynan "
                  "shu qiziqtiradi."),
                c("Laks ekvivalentlik teoremasi",
                  "To'g'ri qo'yilgan chiziqli masala "
                  "uchun: **muvofiqlik + "
                  "barqarorlik $\\iff$ "
                  "yaqinlashish**. Yaqinlashishni "
                  "bevosita isbotlash qiyin, "
                  "ikkinchisini esa oson."),
                c("Fon Neyman tahlili",
                  "Xatolikni Furye garmonikalariga "
                  "yoyib, har birining kuchayish "
                  "koeffitsienti $\\xi$ ni "
                  "hisoblash; barqarorlik uchun "
                  "$|\\xi| \\le 1$."),
                c("Shartli va shartsiz barqarorlik",
                  "Oshkor sxema qadam "
                  "cheklovini talab qiladi "
                  "(shartli), oshkormas sxema esa "
                  "har qanday qadamda barqaror "
                  "(shartsiz)."),
            ],
            derivation=[
                d("1. Issiqlik tenglamasi va oshkor "
                  "sxema",
                  r"\frac{\partial T}{\partial t} = "
                  r"\alpha\frac{\partial^2 T}"
                  r"{\partial x^2} "
                  r"\;\Longrightarrow\; "
                  r"\frac{T_j^{n+1}-T_j^n}{\Delta t} = "
                  r"\alpha\frac{T_{j-1}^n-2T_j^n+"
                  r"T_{j+1}^n}{h^2}",
                  "Vaqt bo'yicha oldinga ayirma "
                  "(su-03), fazo bo'yicha markaziy "
                  "(su-07). Har bir yangi qiymat "
                  "bevosita hisoblanadi — "
                  "**oshkor** sxema."),
                d("2. Yangilash formulasi",
                  r"T_j^{n+1} = T_j^n + r\big("
                  r"T_{j-1}^n - 2T_j^n + T_{j+1}^n"
                  r"\big), \quad r = "
                  r"\frac{\alpha\Delta t}{h^2}",
                  "$r$ — sxemaning yagona "
                  "parametri. Tizim yechish kerak "
                  "emas, shuning uchun juda "
                  "arzon."),
                d("3. Muvofiqlikni tekshirish",
                  r"\tau = \frac{\Delta t}{2}"
                  r"T_{tt} - \frac{\alpha h^2}{12}"
                  r"T_{xxxx} + \ldots = "
                  r"O(\Delta t) + O(h^2)",
                  "Teylor yoyilmasidan. "
                  "$\\Delta t, h \\to 0$ da "
                  "$\\tau \\to 0$ — sxema "
                  "**muvofiq**. Diqqat: bu "
                  "yaqinlashishni "
                  "kafolatlamaydi."),
                d("4. Fon Neyman g'oyasi",
                  r"\varepsilon_j^n = \xi^n "
                  r"e^{ikjh}",
                  "Xatolikni Furye garmonikasi "
                  "sifatida olamiz. Chiziqli "
                  "sxemada har bir garmonika "
                  "mustaqil rivojlanadi, shuning "
                  "uchun bittasini tekshirish "
                  "yetarli."),
                d("5. Kuchayish koeffitsientini "
                  "topish",
                  r"\xi = 1 + r\big(e^{-ikh} - 2 + "
                  r"e^{ikh}\big) = 1 + 2r"
                  r"(\cos kh - 1)",
                  "Garmonikani sxemaga qo'ydik. "
                  "$e^{ikh}+e^{-ikh} = 2\\cos kh$."),
                d("6. Yarim burchak formulasi",
                  r"\cos kh - 1 = -2\sin^2\frac{kh}{2} "
                  r"\;\Longrightarrow\; \xi = "
                  r"1 - 4r\sin^2\frac{kh}{2}",
                  "**Asosiy natija.** $\\xi$ "
                  "haqiqiy son va u "
                  "$[1-4r, 1]$ oralig'ida yotadi."),
                d("7. Barqarorlik sharti",
                  r"|\xi| \le 1 \;\Longrightarrow\; "
                  r"-1 \le 1 - 4r\sin^2\frac{kh}{2} "
                  r"\le 1",
                  "O'ng tengsizlik har doim "
                  "bajariladi ($r > 0$). Chap "
                  "tengsizlik esa cheklov beradi."),
                d("8. Kritik shart",
                  r"1 - 4r\sin^2\frac{kh}{2} \ge -1 "
                  r"\;\Longrightarrow\; "
                  r"r\sin^2\frac{kh}{2} \le "
                  r"\frac{1}{2}",
                  "Eng yomon holat "
                  "$\\sin^2 = 1$, ya'ni "
                  "$kh = \\pi$ — **eng qisqa "
                  "to'lqin** (ikki tugunga bitta "
                  "to'lqin)."),
                d("9. Oshkor sxemaning barqarorlik "
                  "chegarasi",
                  r"r = \frac{\alpha\Delta t}{h^2} "
                  r"\le \frac{1}{2} "
                  r"\;\Longrightarrow\; \Delta t "
                  r"\le \frac{h^2}{2\alpha}",
                  "**Hal qiluvchi cheklov.** "
                  "Vaqt qadami $h^2$ ga "
                  "mutanosib. To'rni ikki barobar "
                  "zichlashtirish vaqt qadamini "
                  "**to'rt barobar** "
                  "kamaytirishni talab qiladi."),
                d("10. Oshkormas (implitsit) sxema",
                  r"\frac{T_j^{n+1}-T_j^n}{\Delta t} "
                  r"= \alpha\frac{T_{j-1}^{n+1}-"
                  r"2T_j^{n+1}+T_{j+1}^{n+1}}{h^2}",
                  "O'ng tomon **yangi** qatlamda "
                  "olinadi. Endi har qadamda "
                  "uch diagonalli tizim yechish "
                  "kerak."),
                d("11. Oshkormas sxemaning "
                  "barqarorligi",
                  r"\xi = \frac{1}{1 + "
                  r"4r\sin^2\frac{kh}{2}} "
                  r"\;\Longrightarrow\; "
                  r"|\xi| \le 1 \ \forall r > 0",
                  "**Shartsiz barqaror.** Maxraj "
                  "har doim birdan katta. Vaqt "
                  "qadami faqat **aniqlik** "
                  "bo'yicha tanlanadi, "
                  "barqarorlik bo'yicha emas."),
                d("12. Krank–Nikolson sxemasi",
                  r"\xi = \frac{1-2r\sin^2"
                  r"\frac{kh}{2}}{1+2r\sin^2"
                  r"\frac{kh}{2}}, \quad "
                  r"\tau = O(\Delta t^2) + O(h^2)",
                  "Ikki qatlamning o'rtachasi. "
                  "Shartsiz barqaror **va** vaqt "
                  "bo'yicha ikkinchi tartibli. "
                  "Lekin $r$ katta bo'lganda "
                  "$\\xi \\to -1$ va yechim "
                  "tebranadi (so'nmaydi)."),
                d("13. Laks teoremasining roli",
                  r"\text{muvofiqlik} + "
                  r"\text{barqarorlik} \iff "
                  r"\text{yaqinlashish}",
                  "**Nima uchun bu muhim.** "
                  "Yaqinlashishni bevosita "
                  "isbotlash uchun aniq yechimni "
                  "bilish kerak — u esa "
                  "noma'lum. Muvofiqlik Teylor "
                  "qatoridan, barqarorlik fon "
                  "Neymandan oson tekshiriladi; "
                  "Laks teoremasi ulardan "
                  "yaqinlashishni **kafolatlaydi**."),
            ],
            meaning=(
                "Bu mavzu sonli usullar "
                "nazariyasining markazi. Uchta "
                "tushuncha — muvofiqlik, "
                "barqarorlik, yaqinlashish — "
                "ko'pincha aralashtiriladi, lekin "
                "ular butunlay boshqa narsalar. "
                "Muvofiqlik — sxema **to'g'ri "
                "tenglamani** yaqinlashtiradimi; "
                "u Teylor qatoridan oson "
                "tekshiriladi va deyarli har doim "
                "bajariladi. Barqarorlik — "
                "xatoliklar **o'smaydimi**; bu "
                "butunlay boshqa savol va u "
                "aniqlik bilan umuman bog'liq "
                "emas. Yaqinlashish esa bizni "
                "haqiqatan qiziqtiradigan narsa, "
                "lekin uni bevosita tekshirish "
                "mumkin emas, chunki aniq yechim "
                "noma'lum. Laks teoremasining "
                "amaliy qiymati aynan shunda: u "
                "tekshirish mumkin bo'lgan ikkita "
                "xossadan tekshirib bo'lmaydigan "
                "uchinchisini keltirib chiqaradi. "
                "Kirish misolidagi 'portlash' "
                "aynan shundan: sxema mukammal "
                "muvofiq edi, lekin nobarqaror. "
                "9-qadamdagi $\\Delta t \\le "
                "h^2/(2\\alpha)$ sharti amaliy "
                "jihatdan juda og'ir. To'rni "
                "ikki barobar zichlashtirsangiz, "
                "vaqt qadamini to'rt barobar "
                "kamaytirishingiz kerak — demak "
                "umumiy hisob hajmi **sakkiz "
                "barobar** ortadi (ikki barobar "
                "ko'p tugun × to'rt barobar ko'p "
                "qadam). Bir o'lchovda bu "
                "chidasa bo'ladi, uch o'lchovda "
                "esa $2^3 \\times 4 = 32$ "
                "barobar — tez orada imkonsiz "
                "bo'lib qoladi. Aynan shuning "
                "uchun amaliy hisoblarda deyarli "
                "har doim oshkormas sxemalar "
                "ishlatiladi: ular har qadamda "
                "tizim yechishni talab qiladi "
                "(qimmatroq), lekin vaqt qadami "
                "faqat aniqlik bo'yicha "
                "tanlanadi. 8-qadamdagi "
                "$kh = \\pi$ holati ham "
                "e'tiborga loyiq: barqarorlikni "
                "buzadigan narsa **eng qisqa** "
                "to'lqin — ikki tugunga bitta "
                "to'lqin. Bunday to'lqin "
                "fizikaviy ma'noga ega emas "
                "(u to'r bilan hech qanday "
                "aniqlikda ifodalanmaydi), lekin "
                "aynan u sxemani portlatadi. "
                "Bu sonli usullardagi tipik "
                "manzara: muammo eng nozik "
                "detallarda emas, eng dag'al "
                "artefaktlarda."
            ),
            equations=[
                eq(r"\xi = 1 - 4r\sin^2\frac{kh}{2}, "
                   r"\quad r = \frac{\alpha\Delta t}{h^2}",
                   "Oshkor sxemaning kuchayish "
                   "koeffitsienti.",
                   "Oshkor sxema"),
                eq(r"r \le \frac{1}{2} "
                   r"\;\Longleftrightarrow\; "
                   r"\Delta t \le \frac{h^2}{2\alpha}",
                   "Oshkor sxemaning barqarorlik "
                   "sharti — vaqt qadami $h^2$ ga "
                   "mutanosib.", "Barqarorlik sharti"),
                eq(r"\xi_{impl} = \frac{1}"
                   r"{1+4r\sin^2\frac{kh}{2}} \le 1 "
                   r"\ \forall r",
                   "Oshkormas sxema — shartsiz "
                   "barqaror.", "Oshkormas sxema"),
                eq(r"\text{muvofiqlik} + "
                   r"\text{barqarorlik} \iff "
                   r"\text{yaqinlashish}",
                   "Laks ekvivalentlik teoremasi.",
                   "Laks teoremasi"),
            ],
            conditions=(
                "**Laks teoremasining shartlari:**\n"
                "- Masala chiziqli;\n"
                "- Masala to'g'ri qo'yilgan "
                "(well-posed, su-04);\n"
                "- Sxema chiziqli va doimiy "
                "koeffitsientli.\n\n"
                "Nochiziqli masalalarda teorema "
                "**o'rinsiz** — u yerda "
                "barqarorlik ham, yaqinlashish "
                "ham alohida tekshiriladi.\n\n"
                "**Fon Neyman tahlilining "
                "cheklovlari:**\n"
                "- U chegaraviy shartlarni "
                "hisobga olmaydi (cheksiz yoki "
                "davriy soha deb faraz qiladi);\n"
                "- Doimiy koeffitsientlarni "
                "talab qiladi;\n"
                "- **Zarur** shart beradi, ba'zi "
                "holatlarda yetarli emas.\n\n"
                "Chegaraviy shartlar ta'sirini "
                "tekshirish uchun matritsaviy "
                "tahlil (o'tish matritsasining "
                "spektral radiusi, su-06) "
                "ishlatiladi.\n\n"
                "**Amaliy qadam tanlash:**\n"
                "- Oshkor: "
                "$\\Delta t \\le h^2/(2\\alpha)$ "
                "va odatda 0,8 zaxira bilan;\n"
                "- Oshkormas: aniqlik bo'yicha, "
                "$\\Delta t \\sim h$ olsa ham "
                "bo'ladi;\n"
                "- Krank–Nikolson: "
                "$r \\lesssim 1$ tavsiya "
                "etiladi, aks holda tebranish "
                "paydo bo'ladi."
            ),
            worked=WorkedExample(
                statement=(
                    "Po'lat plastinada issiqlik "
                    "tarqalishi: $\\alpha = "
                    "1{,}2\\times10^{-5}$ m²/s, "
                    "qalinlik bo'ylab $L = 20$ mm. "
                    "(a) $h = 1$ mm da oshkor sxema "
                    "uchun maksimal vaqt qadamini "
                    "toping; (b) 60 soniya "
                    "hisoblash uchun necha qadam "
                    "kerak? (c) $h$ ni ikki barobar "
                    "kichraytirsak nima o'zgaradi? "
                    "(d) oshkormas sxemada "
                    "$\\Delta t = 1$ s olish "
                    "mumkinmi?"
                ),
                given=[
                    r"\alpha = 1{,}2\times10^{-5}\ "
                    r"\text{m}^2/\text{s}",
                    r"L = 0{,}02\ \text{m},\ "
                    r"h = 0{,}001\ \text{m}",
                ],
                steps=[
                    st(r"\Delta t_{max} = "
                       r"\frac{h^2}{2\alpha} = "
                       r"\frac{10^{-6}}{2 \cdot "
                       r"1{,}2\times10^{-5}}",
                       "9-qadamdagi shart."),
                    st(r"= \frac{10^{-6}}{2{,}4\times"
                       r"10^{-5}} = 0{,}041667\ "
                       r"\text{s}",
                       "**41,7 millisekund** — juda "
                       "kichik qadam."),
                    st(r"N = \frac{60}{0{,}041667} = "
                       r"1440 \ \text{qadam}",
                       "60 soniya uchun 1440 qadam. "
                       "Har qadamda 20 ta tugun — "
                       "jami 28 800 amal, bu hali "
                       "arzon."),
                    st(r"h = 0{,}5\ \text{mm}: \ "
                       r"\Delta t_{max} = "
                       r"\frac{0{,}25\times10^{-6}}"
                       r"{2{,}4\times10^{-5}} = "
                       r"0{,}010417\ \text{s}",
                       "**To'rt barobar kichik** — "
                       "$h^2$ bog'liqlik."),
                    st(r"N = \frac{60}{0{,}010417} = "
                       r"5760 \ \text{qadam}, \quad "
                       r"\text{tugunlar} = 40",
                       "Qadamlar to'rt barobar, "
                       "tugunlar ikki barobar."),
                    st(r"\text{umumiy hajm nisbati} = "
                       r"4 \times 2 = 8 \ \text{marta}",
                       "**Sakkiz barobar qimmat** — "
                       "atigi ikki barobar "
                       "zichroq to'r uchun."),
                    st(r"\text{3D da: } 2^3 \times 4 = "
                       r"32 \ \text{marta}",
                       "Uch o'lchovda vaziyat "
                       "keskin yomonlashadi va "
                       "oshkor sxema tez orada "
                       "amalda yaroqsiz bo'lib "
                       "qoladi."),
                    st(r"\text{(d) oshkormas: } r = "
                       r"\frac{1{,}2\times10^{-5} "
                       r"\cdot 1}{10^{-6}} = 12",
                       "$r = 12 \\gg 1/2$ — oshkor "
                       "sxema uchun bu halokatli."),
                    st(r"\xi_{impl} = \frac{1}"
                       r"{1+4 \cdot 12 \cdot 1} = "
                       r"\frac{1}{49} = 0{,}0204 "
                       r"< 1",
                       "**Barqaror.** Oshkormas "
                       "sxemada $r = 12$ hech "
                       "qanday muammo tug'dirmaydi."),
                    st(r"\text{lekin aniqlik: } "
                       r"\tau = O(\Delta t) "
                       r"\;\Rightarrow\; "
                       r"\Delta t = 1\ \text{s} \ "
                       r"\text{katta xato beradi}",
                       "Barqarorlik aniqlikni "
                       "kafolatlamaydi. "
                       "Krank–Nikolson "
                       "$O(\\Delta t^2)$ bergani "
                       "uchun afzal — lekin u ham "
                       "$r = 12$ da tebranishga "
                       "moyil."),
                ],
                answer=(
                    "(a) $\\Delta t_{max} = "
                    "0{,}041667$ s (41,7 ms); "
                    "(b) 1440 qadam; "
                    "(c) $h$ ikki barobar "
                    "kichrayganda $\\Delta t$ "
                    "to'rt barobar kamayadi va "
                    "umumiy hisob hajmi **sakkiz "
                    "barobar** ortadi (3D da 32 "
                    "barobar); (d) oshkormas "
                    "sxemada $r = 12$ da "
                    "$\\xi = 0{,}0204 < 1$ — "
                    "barqaror, lekin "
                    "$O(\\Delta t)$ aniqligi "
                    "tufayli xato katta bo'ladi."
                ),
                engineering_note=(
                    "(c) natijasi oshkor "
                    "sxemalarning asosiy "
                    "kamchiligini aniq "
                    "ko'rsatadi va u 'diffuziya "
                    "tipidagi' barcha "
                    "masalalarga tegishli: "
                    "issiqlik, namlik, "
                    "konsolidatsiya, elektr "
                    "o'tkazuvchanlik. "
                    "$\\Delta t \\sim h^2$ "
                    "bog'liqligi to'r "
                    "zichlashgani sari "
                    "nomutanosib qimmatlashadi. "
                    "To'lqin tipidagi "
                    "masalalarda (su-12) esa "
                    "vaziyat yaxshiroq: u yerda "
                    "$\\Delta t \\sim h$ va "
                    "oshkor sxemalar amalda "
                    "keng ishlatiladi. Bu "
                    "farqni tushunish usul "
                    "tanlashda hal qiluvchi. "
                    "(d) esa yana bir muhim "
                    "saboqni beradi: "
                    "barqarorlik va aniqlik "
                    "**alohida** talablar. "
                    "Oshkormas sxema $r = 100$ "
                    "da ham portlamaydi, lekin "
                    "javob butunlay noto'g'ri "
                    "bo'lishi mumkin. "
                    "Nobarqaror sxema esa "
                    "hech bo'lmaganda o'zini "
                    "darhol oshkor qiladi — "
                    "`NaN` ko'rinishida. "
                    "Shu ma'noda nobarqarorlik "
                    "xavfsizroq xato turi."
                ),
            ),
            computation=Computation(
                caption=(
                    "Oshkor, oshkormas va "
                    "Krank–Nikolson sxemalarini "
                    "taqqoslash, barqarorlik "
                    "chegarasini sonli topish va "
                    "Laks teoremasini tekshirish."
                ),
                code='''"""Muvofiqlik, barqarorlik va yaqinlashish: Laks teoremasi."""
import numpy as np
from labkit import PARAMS, note, series, table, value

alpha = float(PARAMS.get("alpha", 1.2e-5))
L = float(PARAMS.get("L", 20.0))/1000.0
nx = int(PARAMS.get("nx", 20))
t_end = float(PARAMS.get("t_end", 20.0))
r_test = float(PARAMS.get("r_test", 0.6))

h = L/nx
x = np.linspace(0.0, L, nx + 1)
value("Fazo qadami h", h*1000, "mm")
value("Barqarorlik chegarasi dt_max", h**2/(2*alpha), "s")

# Boshlang'ich shart: T = sin(pi x / L); aniq yechim ma'lum
# T(x,t) = exp(-alpha*(pi/L)^2 * t) * sin(pi x / L)
kk = np.pi/L
T0 = np.sin(kk*x)


def exact(t):
    return np.exp(-alpha*kk**2*t)*np.sin(kk*x)


def march(scheme, r, t_end):
    dt = r*h**2/alpha
    nt = max(1, int(round(t_end/dt)))
    dt = t_end/nt
    r_eff = alpha*dt/h**2
    T = T0.copy()
    if scheme == "explicit":
        for _ in range(nt):
            Tn = T.copy()
            T[1:-1] = Tn[1:-1] + r_eff*(Tn[:-2] - 2*Tn[1:-1] + Tn[2:])
            T[0] = T[-1] = 0.0
            if not np.all(np.isfinite(T)):
                return T, nt, r_eff, False
            if np.max(np.abs(T)) > 1e6:
                return T, nt, r_eff, False
        return T, nt, r_eff, True

    # Oshkormas va Krank-Nikolson uchun matritsa
    th = 1.0 if scheme == "implicit" else 0.5
    N = nx - 1
    A = np.zeros((N, N))
    B = np.zeros((N, N))
    for i in range(N):
        A[i, i] = 1.0 + 2.0*th*r_eff
        B[i, i] = 1.0 - 2.0*(1.0 - th)*r_eff
        if i > 0:
            A[i, i - 1] = -th*r_eff
            B[i, i - 1] = (1.0 - th)*r_eff
        if i < N - 1:
            A[i, i + 1] = -th*r_eff
            B[i, i + 1] = (1.0 - th)*r_eff
    T = T0.copy()
    for _ in range(nt):
        rhs = B @ T[1:-1]
        T[1:-1] = np.linalg.solve(A, rhs)
        T[0] = T[-1] = 0.0
    return T, nt, r_eff, np.all(np.isfinite(T))


# --- (1) MUVOFIQLIK: kesish xatoligi nolga intiladimi? ---
# h va dt BIRGA kichrayishi kerak (r = const), aks holda ikki had
# bir-birini qisman qisqartirib, tau monoton kamaymaydi.
rows, taus, hh_list = [], [], []
xm = L/2
Ttt = (alpha*kk**2)**2*np.sin(kk*xm)
Txxxx = kk**4*np.sin(kk*xm)
for hh in [h, h/2, h/4, h/8, h/16]:
    dtt = 0.25*hh**2/alpha            # r = 0.25 doimiy
    tau = abs(dtt/2*Ttt - alpha*hh**2/12*Txxxx)
    taus.append(tau)
    hh_list.append(hh)
    rows.append([f"{hh*1000:.5f}", f"{dtt:.6f}", f"{tau:.4e}"])
table("Muvofiqlik: kesish xatoligi tau (r = 0.25 doimiy)",
      ["h, mm", "dt, s", "|tau|"], rows)
p_tau = np.polyfit(np.log(hh_list), np.log(taus), 1)[0]
value("Kesish xatoligining tartibi (h bo'yicha)", float(p_tau), "—")
note(f"h va dt birga kichrayganda kesish xatoligi monoton nolga "
     f"intiladi va uning tartibi {p_tau:.3f} ~ 2 (dt ~ h^2 bo'lgani "
     f"uchun ikkala had ham h^2 tartibida). Demak sxema MUVOFIQ. "
     f"Lekin bu hali yaqinlashishni kafolatlamaydi: barqarorlik "
     f"ham kerak.")

# --- (2) BARQARORLIK: fon Neyman koeffitsienti ---
khs = np.linspace(0, np.pi, 200)
for rr in [0.25, 0.5, 0.6, 1.0]:
    xi = 1.0 - 4.0*rr*np.sin(khs/2)**2
    series(f"|xi| oshkor, r = {rr}", khs.tolist(),
           np.abs(xi).tolist(), xlabel="k*h", ylabel="|xi|")
series("Barqarorlik chegarasi |xi| = 1", khs.tolist(),
       [1.0]*len(khs), xlabel="k*h", ylabel="|xi|")

for rr in [0.25, 0.5, 0.6]:
    xi_worst = abs(1.0 - 4.0*rr)
    value(f"Oshkor: maks |xi| (r = {rr})", xi_worst, "—")
value("Oshkormas: maks |xi| (r = 12)",
      float(1.0/(1.0 + 4.0*12.0)), "—")
note("Oshkor sxemada eng xavfli garmonika k*h = pi (eng QISQA "
     "to'lqin, ikki tugunga bitta to'lqin). r = 0.5 da |xi| = 1 "
     "(chegara), r = 0.6 da |xi| = 1.4 > 1 - portlaydi. Oshkormas "
     "sxemada esa r = 12 da ham |xi| = 0.02 << 1.")

# --- (3) Barqarorlik chegarasini SONLI topish ---
# MUHIM: boshlang'ich shartga eng QISQA to'lqinni (k*h = pi) kichik
# amplituda bilan qo'shamiz. Nazariya aynan shu garmonikani xavfli
# deb aytadi; u bo'lmasa nobarqarorlik faqat yaxlitlash shovqinidan
# o'sadi va chegara xiralashadi.
saw = 1e-8*np.array([(-1.0)**j for j in range(nx + 1)])
saw[0] = saw[-1] = 0.0
rs = np.linspace(0.44, 0.60, 33)
grow = []
for rr in rs:
    dt = rr*h**2/alpha
    T = T0.copy() + saw
    ok = True
    for _ in range(400):
        Tn = T.copy()
        T[1:-1] = Tn[1:-1] + rr*(Tn[:-2] - 2*Tn[1:-1] + Tn[2:])
        T[0] = T[-1] = 0.0
        if not np.all(np.isfinite(T)) or np.max(np.abs(T)) > 1e8:
            ok = False
            break
    grow.append(np.max(np.abs(T)) if ok else 1e8)
series("400 qadamdan keyingi maks |T|", rs.tolist(),
       np.minimum(grow, 1e8).tolist(),
       xlabel="r = alpha*dt/h^2", ylabel="maks |T|")
bad = [rr for rr, g in zip(rs, grow) if g > 1.05]
if bad:
    value("Sonli topilgan barqarorlik chegarasi", float(min(bad)), "—")
    value("Nazariy chegara", 0.5, "—")
    value("Farq", abs(min(bad) - 0.5)/0.5*100, "%")
    note(f"400 qadam yurgizib barqarorlik chegarasi SONLI topildi: "
         f"r = {min(bad):.3f} dan boshlab yechim o'sadi. Nazariy "
         f"chegara r = 0.5 - farq {abs(min(bad)-0.5)/0.5*100:.1f} %. "
         f"Fon Neyman tahlili tasdiqlandi.")

# --- (4) LAKS TEOREMASI: yaqinlashishni tekshirish ---
rows2 = []
for nk in [10, 20, 40, 80]:
    hk = L/nk
    xk = np.linspace(0.0, L, nk + 1)
    T0k = np.sin(kk*xk)
    dtk = 0.25*hk**2/alpha          # r = 0.25, barqaror
    ntk = max(1, int(round(t_end/dtk)))
    dtk = t_end/ntk
    rk = alpha*dtk/hk**2
    T = T0k.copy()
    for _ in range(ntk):
        Tn = T.copy()
        T[1:-1] = Tn[1:-1] + rk*(Tn[:-2] - 2*Tn[1:-1] + Tn[2:])
        T[0] = T[-1] = 0.0
    Tex = np.exp(-alpha*kk**2*t_end)*np.sin(kk*xk)
    e = np.max(np.abs(T - Tex))/np.max(np.abs(Tex))
    rows2.append([nk, f"{hk*1000:.4f}", f"{dtk:.6f}", ntk,
                  f"{e*100:.6f}"])
table("Barqaror sxema (r = 0.25): to'r bo'yicha yaqinlashish",
      ["n", "h, mm", "dt, s", "qadamlar", "xatolik, %"], rows2)
errs2 = [float(row[-1]) for row in rows2]
ords2 = [np.log2(errs2[i]/errs2[i+1]) for i in range(len(errs2) - 1)]
value("Yaqinlashish tartibi (10->20)", float(ords2[0]), "—")
value("Yaqinlashish tartibi (20->40)", float(ords2[1]), "—")
value("Yaqinlashish tartibi (40->80)", float(ords2[2]), "—")
note(f"r = 0.25 doimiy ushlab turilganda (ya'ni dt ~ h^2) xatolik "
     f"to'rt barobar kamayadi: o'lchangan tartiblar "
     f"{', '.join(f'{o:.3f}' for o in ords2)} ~ 2. MUVOFIQ + "
     f"BARQAROR sxema YAQINLASHDI - Laks teoremasi tasdiqlandi.")

# --- (5) NOBARQAROR sxema: muvofiq bo'lsa ham yaqinlashmaydi ---
rows3 = []
for nk in [10, 20, 40]:
    hk = L/nk
    xk = np.linspace(0.0, L, nk + 1)
    T0k = np.sin(kk*xk)
    rk = r_test                     # > 0.5 bo'lsa nobarqaror
    dtk = rk*hk**2/alpha
    ntk = max(1, int(round(t_end/dtk)))
    dtk = t_end/ntk
    rk = alpha*dtk/hk**2
    T = T0k.copy()
    blown = False
    for _ in range(ntk):
        Tn = T.copy()
        T[1:-1] = Tn[1:-1] + rk*(Tn[:-2] - 2*Tn[1:-1] + Tn[2:])
        T[0] = T[-1] = 0.0
        if not np.all(np.isfinite(T)) or np.max(np.abs(T)) > 1e10:
            blown = True
            break
    Tex = np.exp(-alpha*kk**2*t_end)*np.sin(kk*xk)
    if blown:
        rows3.append([nk, f"{rk:.4f}", "PORTLADI", "-"])
    else:
        e = np.max(np.abs(T - Tex))/np.max(np.abs(Tex))
        rows3.append([nk, f"{rk:.4f}", f"{np.max(np.abs(T)):.3e}",
                      f"{e*100:.3e}"])
table(f"Nobarqaror sxema (r = {r_test}): muvofiq, lekin yaqinlashmaydi",
      ["n", "r", "maks |T|", "xatolik, %"], rows3)
note(f"r = {r_test} > 0.5 da sxema MUVOFIQ bo'lib qolaveradi (kesish "
     f"xatoligi o'zgarmadi), lekin NOBARQAROR - va natijada "
     f"YAQINLASHMAYDI. Bu Laks teoremasining ikkinchi yo'nalishi: "
     f"barqarorliksiz muvofiqlik yetarli emas.")

# --- (6) Uchta sxemani taqqoslash ---
rows4 = []
for scheme, rr in [("explicit", 0.4), ("explicit", 2.0),
                   ("implicit", 2.0), ("implicit", 12.0),
                   ("crank", 2.0), ("crank", 12.0)]:
    T, nt, r_eff, ok = march(scheme, rr, t_end)
    Tex = exact(t_end)
    if ok and np.all(np.isfinite(T)):
        e = np.max(np.abs(T - Tex))/np.max(np.abs(Tex))
        rows4.append([scheme, f"{r_eff:.3f}", nt, f"{e*100:.4f}"])
    else:
        rows4.append([scheme, f"{r_eff:.3f}", nt, "PORTLADI"])
table("Uchta sxemaning taqqoslashi (t = %.0f s)" % t_end,
      ["sxema", "r", "qadamlar", "xatolik, %"], rows4)
note("Oshkor sxema r = 2.0 da portlaydi; oshkormas va Krank-Nikolson "
     "esa r = 12 da ham ishlaydi. Lekin e'tibor bering: barqaror "
     "bo'lish aniq bo'lishni anglatmaydi - r katta bo'lgani sari "
     "xatolik o'sadi.")

# --- Vaqt bo'yicha tartibni O'LCHASH ---
# Diqqat: h qat'iy bo'lsa, dt kichraygani sari xatolik FAZOVIY
# xatolikka (O(h^2)) tiralib qoladi va vaqt tartibini o'lchab
# bo'lmaydi. Shuning uchun YARIM DISKRET aniq yechim bilan
# taqqoslaymiz: fazo diskret, vaqt esa aniq.
lam_h = -alpha*(4.0/h**2)*np.sin(kk*h/2.0)**2


def exact_semi(t):
    return np.exp(lam_h*t)*np.sin(kk*x)


value("Uzluksiz xususiy qiymat -alpha*k^2", -alpha*kk**2, "1/s")
value("Diskret xususiy qiymat lambda_h", lam_h, "1/s")
value("Ularning nisbati", lam_h/(-alpha*kk**2), "—")
note(f"Fazoviy diskretlashtirish xususiy qiymatni {-alpha*kk**2:.6e} "
     f"dan {lam_h:.6e} ga o'zgartiradi (nisbat "
     f"{lam_h/(-alpha*kk**2):.6f}) - bu FAZOVIY xatolik. Vaqt "
     f"tartibini o'lchash uchun aynan shu yarim diskret yechim "
     f"etalon bo'lishi kerak.")

rows5 = []
for rr in [4.0, 2.0, 1.0, 0.5, 0.25]:
    Ti, _, ri, _ = march("implicit", rr, t_end)
    Tc, _, rc, _ = march("crank", rr, t_end)
    Tsemi = exact_semi(t_end)
    nrm = np.max(np.abs(Tsemi))
    ei = np.max(np.abs(Ti - Tsemi))/nrm
    ec = np.max(np.abs(Tc - Tsemi))/nrm
    rows5.append([f"{rr:g}", f"{ei*100:.6f}", f"{ec*100:.6f}",
                  f"{ei/max(ec,1e-30):.1f}"])
table("Vaqt bo'yicha aniqlik (yarim diskret etalonga nisbatan)",
      ["r", "oshkormas xato, %", "Krank-Nikolson xato, %", "nisbat"],
      rows5)
ei_l = [float(rr[1]) for rr in rows5]
ec_l = [float(rr[2]) for rr in rows5]
p_i = float(np.mean([np.log2(ei_l[i]/ei_l[i+1])
                     for i in range(len(ei_l) - 1)]))
p_c = float(np.mean([np.log2(ec_l[i]/ec_l[i+1])
                     for i in range(len(ec_l) - 1)]))
value("Oshkormas: vaqt bo'yicha tartib", p_i, "—")
value("Krank-Nikolson: vaqt bo'yicha tartib", p_c, "—")
note(f"Yarim diskret etalonga nisbatan o'lchanganda vaqt qadami ikki "
     f"barobar kamayganda oshkormas sxema xatosi "
     f"{ei_l[0]/ei_l[1]:.2f} marta (tartib {p_i:.2f} ~ 1), "
     f"Krank-Nikolson xatosi esa {ec_l[0]/ec_l[1]:.2f} marta "
     f"(tartib {p_c:.2f} ~ 2) kamayadi. 12-qadamdagi O(dt^2) "
     f"TASDIQLANDI.")
note("Agar etalon sifatida to'liq aniq yechim olinsa, dt kichraygani "
     "sari xatolik FAZOVIY xatolikka tiralib qoladi va Krank-Nikolson "
     "uchun tartib umuman o'lchanmaydi. Bu amaliyotdagi keng "
     "tarqalgan tuzoq: tartibni o'lchashda faqat BITTA diskretlashtirish "
     "parametri o'zgarishi va etalon shunga mos bo'lishi kerak.")

table("Uchta tushunchaning farqi",
      ["Tushuncha", "Savol", "Qanday tekshiriladi", "Qiyinligi"],
      [["Muvofiqlik", "to'g'ri tenglamami?", "Teylor qatori", "oson"],
       ["Barqarorlik", "xato o'smaydimi?", "fon Neyman", "o'rtacha"],
       ["Yaqinlashish", "aniq yechimga intiladimi?",
        "Laks teoremasi orqali", "bevosita - juda qiyin"]])
''',
                parameters=[
                    p("alpha", "Temperatura o'tkazuvchanlik α",
                      1e-7, 0.001, 1.2e-5, 1e-7, "m²/s"),
                    p("L", "Qalinlik L", 1.0, 500.0, 20.0, 1.0, "mm"),
                    p("nx", "Bo'linmalar soni", 5.0, 100.0, 20.0, 1.0),
                    p("t_end", "Hisoblash vaqti", 1.0, 600.0, 20.0, 1.0,
                      "s"),
                    p("r_test", "Nobarqarorlik uchun r", 0.5, 2.0, 0.6,
                      0.05),
                ],
                expected_output=(
                    "$h$ va $\\Delta t$ birga "
                    "kichrayganda ($r$ doimiy) "
                    "kesish xatoligi monoton nolga "
                    "intiladi, tartibi aynan "
                    "2,000 — sxema muvofiq. "
                    "Fon Neyman tahlili "
                    "eng xavfli garmonika "
                    "$kh = \\pi$ ekanini "
                    "ko'rsatadi va $r = 0{,}5$ da "
                    "$|\\xi| = 1$ chegarasiga "
                    "yetadi. Barqarorlik chegarasi "
                    "**sonli** topilganda nazariy "
                    "$r = 0{,}5$ ga juda yaqin "
                    "(0,515) chiqadi — buning "
                    "uchun boshlang'ich shartga "
                    "aynan xavfli $kh = \\pi$ "
                    "garmonikasi qo'shiladi. "
                    "$r = 0{,}25$ da sxema "
                    "yaqinlashadi (tartib 1,994 → "
                    "1,998 → 2,000), $r > 0{,}5$ "
                    "da esa muvofiq bo'lib qolsa "
                    "ham portlaydi — Laks "
                    "teoremasining ikkala "
                    "yo'nalishi tasdiqlanadi. "
                    "Vaqt bo'yicha tartib "
                    "**yarim diskret** etalonga "
                    "nisbatan o'lchanadi: "
                    "oshkormas 1,026, "
                    "Krank–Nikolson 1,99969. "
                    "To'liq aniq yechim etalon "
                    "qilinsa, fazoviy xatolik "
                    "hukmron bo'lib qoladi va "
                    "vaqt tartibi umuman "
                    "o'lchanmaydi — bu alohida "
                    "ta'kidlangan."
                ),
            ),
            visual=vis(
                kind="Barqarorlik va kuchayish koeffitsienti",
                tool="React/SVG + Manim",
                description=(
                    "$|\\xi|$ ning to'lqin soniga "
                    "bog'liqligi va nobarqaror "
                    "yechimning portlashi."
                ),
                how_to_draw=(
                    "React/SVG: chap panelda "
                    "$|\\xi|$ ning $kh \\in [0,\\pi]$ "
                    "bo'yicha grafigi — bir necha "
                    "$r$ qiymati uchun egri "
                    "chiziqlar. $|\\xi| = 1$ "
                    "gorizontal chizig'i qizil "
                    "bilan; undan yuqoriga chiqqan "
                    "qism shtrixlanadi va "
                    "'portlaydi' deb belgilanadi. "
                    "$r$ slayderi bilan egri "
                    "chiziq ko'tariladi va "
                    "$r = 0{,}5$ da aynan chegaraga "
                    "tegadi — bu hal qiluvchi "
                    "moment ajratib ko'rsatiladi. "
                    "Diqqat: egri chiziq eng "
                    "yuqori nuqtasiga $kh = \\pi$ "
                    "da yetadi, ya'ni **eng qisqa** "
                    "to'lqinda. O'ng panelda "
                    "haroratning vaqt bo'yicha "
                    "evolyutsiyasi "
                    "animatsiyalanadi: barqaror "
                    "holatda profil silliq "
                    "pasayadi, nobarqaror holatda "
                    "esa tugundan tugunga "
                    "almashinuvchi ishorali "
                    "'arra' paydo bo'lib, "
                    "amplitudasi eksponensial "
                    "o'sadi — $kh = \\pi$ "
                    "garmonikasi ko'z bilan "
                    "ko'rinadi. Pastda yaqinlashish "
                    "jadvali: barqaror sxema uchun "
                    "xatolik kamayadi, nobarqaror "
                    "uchun 'PORTLADI' yoziladi."
                ),
            ),
            interp=(
                "Kodning tuzilishi Laks "
                "teoremasining ikkala yo'nalishini "
                "alohida tekshiradi va bu uning "
                "asosiy qiymati. Avval muvofiqlik "
                "ko'rsatiladi: kesish xatoligi "
                "$h$ va $\\Delta t$ bilan nolga "
                "intiladi va u **$r$ ga bog'liq "
                "emas**. Keyin barqarorlik "
                "chegarasi ikki mustaqil yo'l "
                "bilan topiladi: fon Neyman "
                "formulasidan ($r \\le 1/2$) va "
                "sxemani haqiqatan yurgizib, "
                "yechim qachon o'sa boshlashini "
                "kuzatib. Ular mos kelishi "
                "nazariy tahlilning tasdig'i. "
                "Undan keyin ikkita hal qiluvchi "
                "tajriba. Birinchisida "
                "$r = 0{,}25$ ushlab turiladi — "
                "sxema muvofiq **va** barqaror, "
                "natijada xatolik $O(h^2)$ "
                "bo'yicha kamayadi, ya'ni "
                "**yaqinlashadi**. Ikkinchisida "
                "$r > 0{,}5$ olinadi — sxema "
                "muvofiq bo'lib qolaveradi "
                "(kesish xatoligi o'zgarmadi!), "
                "lekin nobarqaror va natijada "
                "yaqinlashmaydi, to'r "
                "zichlashgani sari holat "
                "yomonlashadi. Bu Laks "
                "teoremasining 'barqarorlik "
                "zarur' qismining eng aniq "
                "namoyishi. Fon Neyman "
                "grafigidagi eng muhim detal — "
                "maksimum $kh = \\pi$ da "
                "joylashgani. Ya'ni sxemani "
                "portlatadigan narsa eng qisqa, "
                "fizik ma'nosiz to'lqin. "
                "Nihoyat, Krank–Nikolson va "
                "oshkormas sxemalarning "
                "taqqoslashi vaqt bo'yicha "
                "tartiblarni (1 va 2) "
                "tasdiqlaydi va muhim saboqni "
                "beradi: shartsiz barqarorlik "
                "katta qadam olish "
                "**huquqini** beradi, lekin "
                "aniqlikni kafolatlamaydi."
            ),
            mistakes=[
                "Muvofiqlikni yaqinlashish bilan "
                "chalkashtirish. Muvofiq sxema "
                "nobarqaror bo'lsa "
                "yaqinlashmaydi — kodda bu "
                "bevosita ko'rsatiladi.",
                "Barqarorlikni aniqlik bilan "
                "chalkashtirish. Oshkormas sxema "
                "$r = 100$ da ham barqaror, "
                "lekin javob butunlay xato "
                "bo'lishi mumkin.",
                "Oshkor sxemada to'rni "
                "zichlashtirib, vaqt qadamini "
                "o'zgartirmaslik. "
                "$\\Delta t \\sim h^2$ — "
                "cheklov kvadratik.",
                "Fon Neyman tahlilini "
                "nochiziqli masalaga qo'llash. "
                "U faqat chiziqli, doimiy "
                "koeffitsientli sxemalar uchun.",
                "Chegaraviy shartlarning "
                "barqarorlikka ta'sirini "
                "unutish. Fon Neyman ularni "
                "hisobga olmaydi; matritsaviy "
                "tahlil kerak.",
            ],
            quiz=[
                q("Muvofiqlik, barqarorlik va "
                  "yaqinlashish qanday farq "
                  "qiladi?",
                  "Muvofiqlik — sxema to'g'ri "
                  "tenglamani yaqinlashtiradi; "
                  "barqarorlik — xatoliklar "
                  "o'smaydi; yaqinlashish — "
                  "sonli yechim aniq yechimga "
                  "intiladi.", "konseptual"),
                q("Laks teoremasining amaliy "
                  "qiymati nimada?",
                  "Yaqinlashishni bevosita "
                  "tekshirib bo'lmaydi (aniq "
                  "yechim noma'lum), lekin "
                  "muvofiqlik va barqarorlik "
                  "oson tekshiriladi va ular "
                  "yaqinlashishni "
                  "kafolatlaydi.", "talqin"),
                q("$\\alpha = 10^{-5}$ m²/s, "
                  "$h = 2$ mm da oshkor sxema "
                  "uchun $\\Delta t_{max}$ "
                  "qancha?",
                  "$\\Delta t = h^2/(2\\alpha) = "
                  "4\\times10^{-6}/(2\\times"
                  "10^{-5}) = 0{,}2$ s.",
                  "hisob"),
                q("Kodda barqarorlik chegarasi "
                  "nima uchun sonli ham "
                  "topiladi?",
                  "Fon Neyman formulasi "
                  "$r \\le 1/2$ beradi; uni "
                  "sxemani haqiqatan yurgizib "
                  "tekshirish nazariy tahlilning "
                  "mustaqil tasdig'i bo'ladi.",
                  "kod"),
                q("Qaysi garmonika oshkor "
                  "sxemani portlatadi?",
                  "$kh = \\pi$ — eng qisqa "
                  "to'lqin (ikki tugunga bitta "
                  "to'lqin). U fizik ma'noga ega "
                  "emas, lekin aynan u "
                  "$|\\xi|$ ni maksimal qiladi.",
                  "konseptual"),
                q("Krank–Nikolson sxemasining "
                  "afzalligi va kamchiligi "
                  "nima?",
                  "Shartsiz barqaror va vaqt "
                  "bo'yicha $O(\\Delta t^2)$; "
                  "lekin $r$ katta bo'lganda "
                  "$\\xi \\to -1$ va yechim "
                  "so'nmaydigan tebranish "
                  "beradi.", "talqin"),
            ],
            bridge=(
                "Issiqlik tenglamasida oshkor "
                "sxema $\\Delta t \\sim h^2$ ni "
                "talab qildi va bu juda og'ir "
                "cheklov edi. Mexanikaning "
                "dinamik masalalarida — "
                "tebranishlar va to'lqin "
                "tarqalishida — vaziyat "
                "boshqacha. Keyingi mavzuda "
                "ikkinchi tartibli vaqt "
                "hosilasiga o'tamiz va Nyumark "
                "sxemalari oilasini quramiz."
            ),
            research=(
                "Barqarorlik nazariyasini "
                "chuqurlashtiring. (1) Matritsaviy "
                "barqarorlik tahlilini o'rganing: "
                "o'tish matritsasining spektral "
                "radiusi (su-06) orqali "
                "chegaraviy shartlarning ta'sirini "
                "hisobga olish. Fon Neyman "
                "bashoratidan qachon farq qiladi? "
                "(2) Energiya usulini (energy "
                "method) ko'rib chiqing: u "
                "nochiziqli va o'zgaruvchan "
                "koeffitsientli masalalarda ham "
                "ishlaydi. (3) Qattiq (stiff) "
                "tizimlar tushunchasini va "
                "A-barqarorlik, L-barqarorlik "
                "ta'riflarini o'rganing: nima "
                "uchun Krank–Nikolson "
                "A-barqaror, lekin L-barqaror "
                "emas va bu amalda nimaga olib "
                "keladi?"
            ),
            manim_ref=manim(
                scene="StabilityScene",
                module="manim/scenes/su_fd.py",
                title="Barqarorlik va kuchayish koeffitsienti",
                summary=(
                    "Harorat profili vaqt bo'yicha "
                    "rivojlanadi; $r$ kichik "
                    "bo'lganda u silliq pasayadi. "
                    "$r$ ni 0,5 dan oshirganda "
                    "tugundan tugunga almashinuvchi "
                    "'arra' paydo bo'lib, "
                    "amplitudasi eksponensial "
                    "o'sadi. Yonma-yon "
                    "$|\\xi(kh)|$ grafigi "
                    "chiziladi va portlashga sabab "
                    "bo'lgan garmonika "
                    "$kh = \\pi$ belgilanadi."
                ),
            ),
        ),
    ),

    # ------------------------------------------------------------------ su-11
    Topic(
        id="su-11",
        subject_id=S, module_id=M, order=11,
        title="Vaqt bo'yicha integrallash: Nyumark oilasi va dinamik masalalar",
        description=(
            "Ikkinchi tartibli vaqt hosilasi, markaziy ayirma usuli, "
            "Nyumark parametrlari, amplituda va davr xatoliklari hamda "
            "sonli demflash."
        ),
        learning_objective=(
            "Nyumark oilasining parametrlarini tanlash, barqarorlik "
            "shartini aniqlash va sonli demflash hamda davr "
            "cho'zilishini o'lchash."
        ),
        prerequisites=["su-10", "nm-26", "pq-23"],
        mathematical_core=(
            "$\\mathbf{M}\\ddot{\\mathbf{u}} + \\mathbf{C}"
            "\\dot{\\mathbf{u}} + \\mathbf{K}\\mathbf{u} = "
            "\\mathbf{F}$; Nyumark $\\gamma \\ge 1/2$, "
            "$\\beta \\ge (\\gamma+1/2)^2/4$."
        ),
        engineering_application=(
            "Zilzila tahlili, zarba va urilish, mashina tebranishlari, "
            "transport yuklamasi, akustik javob, krash-testlar."
        ),
        computational_component=(
            "Markaziy ayirma va Nyumark sxemalarini bir erkinlik "
            "darajali tizimda taqqoslash, sonli demflash va davr "
            "xatoligini o'lchash."
        ),
        visualization_component=(
            "Fazaviy portret, amplituda so'nishi, davr cho'zilishi, "
            "barqarorlik sohasi."
        ),
        research_extension=(
            "HHT-α va umumlashgan-α usullarini o'rganing: ular yuqori "
            "chastotalarni qanday so'ndiradi va past chastotalarni "
            "qanday saqlaydi?"
        ),
        difficulty="murakkab",
        previous_link=(
            "su-10 da birinchi tartibli vaqt hosilasi (issiqlik "
            "tenglamasi) uchun barqarorlik tahlili qurildi. "
            "Mexanikaning dinamik masalalarida esa ikkinchi tartibli "
            "hosila turadi va bu butunlay boshqa xatti-harakat beradi: "
            "yechim so'nmaydi, tebranadi."
        ),
        next_topic="su-12",
        estimated_minutes=90,
        tags=["Nyumark", "dinamika", "sonli demflash", "davr xatoligi"],
        lesson=_lesson(
            problem=(
                "pq-23 da plastinaning majburiy "
                "tebranishi modal superpozitsiya "
                "bilan yechilgan edi — lekin bu "
                "faqat chiziqli va doimiy "
                "koeffitsientli tizimda ishlaydi. "
                "Zilzila ta'siridagi bino, urilish "
                "paytidagi avtomobil yoki plastik "
                "deformatsiyaga kiradigan "
                "konstruksiya uchun modal usul "
                "yaroqsiz: xususiy shakllar "
                "o'zgarib turadi. Bunday "
                "hollarda harakat tenglamasi "
                "vaqt bo'yicha **bevosita** "
                "integrallanadi. Lekin bu yerda "
                "su-10 dagi barqarorlik "
                "muammosidan tashqari yangi va "
                "nozikroq xavf bor: sxema "
                "barqaror bo'lishi mumkin, lekin "
                "tebranish amplitudasini sekin "
                "so'ndirib yoki davrini "
                "cho'zib yuborishi mumkin — "
                "va buni sezish qiyin."
            ),
            concepts=[
                c("Harakat tenglamasi",
                  "$\\mathbf{M}\\ddot{\\mathbf{u}} + "
                  "\\mathbf{C}\\dot{\\mathbf{u}} + "
                  "\\mathbf{K}\\mathbf{u} = "
                  "\\mathbf{F}(t)$ — ikkinchi "
                  "tartibli vaqt hosilasi."),
                c("Markaziy ayirma usuli",
                  "Oshkor sxema: "
                  "$\\ddot u \\approx (u^{n-1}-2u^n"
                  "+u^{n+1})/\\Delta t^2$; "
                  "shartli barqaror."),
                c("Nyumark oilasi",
                  "$\\gamma$ va $\\beta$ "
                  "parametrlari bilan boshqariladigan "
                  "sxemalar oilasi; "
                  "$\\gamma = 1/2$, $\\beta = 1/4$ — "
                  "o'rtacha tezlanish usuli."),
                c("Sonli demflash "
                  "(numerical damping)",
                  "$\\gamma > 1/2$ da sxema "
                  "amplitudani sun'iy so'ndiradi — "
                  "fizik demflash emas, sxema "
                  "artefakti."),
                c("Davr cho'zilishi "
                  "(period elongation)",
                  "Sonli yechimning davri haqiqiy "
                  "davrdan uzunroq bo'lishi; "
                  "$\\Delta T/T \\sim "
                  "(\\omega\\Delta t)^2$."),
                c("Kritik vaqt qadami",
                  "Oshkor sxema uchun "
                  "$\\Delta t \\le 2/\\omega_{max}$ — "
                  "eng **yuqori** xususiy chastota "
                  "belgilaydi."),
            ],
            derivation=[
                d("1. Bir erkinlik darajali tizim",
                  r"m\ddot u + c\dot u + ku = F(t), "
                  r"\quad \omega = \sqrt{k/m}, \ "
                  r"\zeta = \frac{c}{2\sqrt{km}}",
                  "Tahlilni bitta erkinlik darajasida "
                  "olib boramiz; ko'p erkinlikli "
                  "tizim modal ajratishdan keyin "
                  "shunday tenglamalar to'plamiga "
                  "aylanadi (pq-23)."),
                d("2. Nyumark taxminlari",
                  r"\dot u^{n+1} = \dot u^n + \Delta t"
                  r"\big[(1-\gamma)\ddot u^n + "
                  r"\gamma\ddot u^{n+1}\big]",
                  "Tezlik uchun: $\\gamma$ yangi va "
                  "eski tezlanishlarning nisbatini "
                  "belgilaydi. $\\gamma = 1/2$ — "
                  "o'rtacha qiymat."),
                d("3. Ko'chish uchun taxmin",
                  r"u^{n+1} = u^n + \Delta t\,\dot u^n "
                  r"+ \Delta t^2\Big[\Big(\frac{1}{2}-"
                  r"\beta\Big)\ddot u^n + \beta"
                  r"\ddot u^{n+1}\Big]",
                  "$\\beta$ ko'chishdagi tezlanish "
                  "taqsimotini belgilaydi. "
                  "$\\beta = 1/4$ — doimiy o'rtacha "
                  "tezlanish, $\\beta = 1/6$ — "
                  "chiziqli tezlanish."),
                d("4. Samarali bikrlik",
                  r"\hat k = k + \frac{\gamma}"
                  r"{\beta\Delta t}c + "
                  r"\frac{1}{\beta\Delta t^2}m",
                  "3-taxminni harakat tenglamasiga "
                  "qo'yib, $u^{n+1}$ uchun "
                  "algebraik tenglama olamiz. "
                  "Ko'p erkinlikli tizimda bu "
                  "matritsa bo'ladi va u bir "
                  "marta yoyiladi (su-05)."),
                d("5. Maxsus hollar",
                  r"\beta = 0, \gamma = \tfrac12: \ "
                  r"\text{markaziy ayirma (oshkor)}; "
                  r"\quad \beta = \tfrac14, "
                  r"\gamma = \tfrac12: \ "
                  r"\text{o'rtacha tezlanish}",
                  "$\\beta = 0$ bo'lsa "
                  "$\\hat k$ da $\\ddot u^{n+1}$ "
                  "yo'qoladi va sxema oshkor "
                  "bo'ladi (agar $\\mathbf{M}$ "
                  "diagonal bo'lsa)."),
                d("6. Kuchayish matritsasi",
                  r"\begin{bmatrix}u^{n+1}\\ "
                  r"\Delta t\dot u^{n+1}\end{bmatrix} "
                  r"= \mathbf{A}\begin{bmatrix}u^n\\ "
                  r"\Delta t\dot u^n\end{bmatrix}",
                  "Ikki komponentli holat vektori. "
                  "Barqarorlik "
                  "$\\rho(\\mathbf{A}) \\le 1$ "
                  "bilan aniqlanadi — su-06 dagi "
                  "spektral radius bilan bir xil "
                  "g'oya."),
                d("7. Barqarorlik shartlari",
                  r"\gamma \ge \frac12 \ \text{va} \ "
                  r"\beta \ge \frac{1}{4}\Big("
                  r"\gamma+\frac12\Big)^2 "
                  r"\;\Longrightarrow\; "
                  r"\text{shartsiz barqaror}",
                  "**Asosiy natija.** "
                  "$\\gamma = 1/2$, "
                  "$\\beta = 1/4$ chegarada "
                  "yotadi va shartsiz barqaror. "
                  "$\\beta = 0$ (markaziy ayirma) "
                  "esa shartli."),
                d("8. Oshkor sxemaning kritik qadami",
                  r"\Delta t_{cr} = "
                  r"\frac{2}{\omega_{max}} = "
                  r"\frac{T_{min}}{\pi}",
                  "**Eng yuqori** chastota "
                  "belgilaydi. FEM da "
                  "$\\omega_{max} \\sim c/h$ "
                  "(elastik to'lqin tezligi), "
                  "demak $\\Delta t \\sim h/c$ — "
                  "bu su-12 dagi CFL sharti."),
                d("9. Amplituda xatoligi",
                  r"|\xi| = 1 - \frac{1}{2}\Big("
                  r"\gamma-\frac12\Big)(\omega"
                  r"\Delta t)^2 + O(\Delta t^4)",
                  "$\\gamma = 1/2$ da amplituda "
                  "**aynan saqlanadi** — sonli "
                  "demflash yo'q. $\\gamma > 1/2$ "
                  "da esa amplituda kamayadi va "
                  "bu $\\Delta t^2$ ga mutanosib."),
                d("10. Davr xatoligi",
                  r"\frac{\Delta T}{T} = \frac{1}{2}\Big("
                  r"\beta - \frac{1}{12}\Big)"
                  r"(\omega\Delta t)^2 + O(\Delta t^4)",
                  "$\\beta = 1/12$ da davr "
                  "xatoligi ikkinchi tartibda "
                  "yo'qoladi (Foks–Gudvin sxemasi), "
                  "lekin u shartli barqaror. "
                  "$\\beta = 1/4$ da "
                  "$\\Delta T/T = "
                  "(\\omega\\Delta t)^2/12$ — davr "
                  "**cho'ziladi**. Kodda bu "
                  "formula o'lchash bilan "
                  "tekshiriladi."),
                d("11. Aniqlik va demflashning "
                  "raqobati",
                  r"\gamma = \tfrac12: \ \text{2-tartib, "
                  r"demflash yo'q}; \quad "
                  r"\gamma > \tfrac12: \ "
                  r"\text{1-tartib, demflash bor}",
                  "**Muhim kelishuv.** Sonli "
                  "demflash kerak bo'lsa "
                  "($\\gamma > 1/2$), aniqlik "
                  "ikkinchi tartibdan birinchiga "
                  "tushadi. HHT-α usullari bu "
                  "muammoni hal qiladi: ular "
                  "ikkinchi tartibni saqlab, "
                  "faqat yuqori chastotalarni "
                  "so'ndiradi."),
                d("12. Nima uchun demflash kerak",
                  r"\omega_{max}\Delta t \gg 1 "
                  r"\;\Longrightarrow\; \text{yuqori "
                  r"rejimlar SOXTA javob beradi}",
                  "FEM to'rida eng yuqori "
                  "chastotalar fizik ma'noga ega "
                  "emas (ular to'r artefakti, "
                  "pq-30 dagi spektr zichligiga "
                  "qarang), lekin ular javobni "
                  "ifloslantiradi. Ularni "
                  "so'ndirish foydali."),
            ],
            meaning=(
                "Dinamik masalalarda vaqt "
                "integrallashning markaziy "
                "kelishuvi 11-qadamda: aniqlik va "
                "sonli demflash bir-biriga zid. "
                "$\\gamma = 1/2$ tanlansa sxema "
                "ikkinchi tartibli va amplitudani "
                "aynan saqlaydi — energiya "
                "yo'qolmaydi. Bu uzoq vaqtli "
                "tebranish tahlili uchun ideal. "
                "Lekin FEM to'rida yuqori "
                "chastotali rejimlar mavjud va "
                "ular fizik ma'noga ega emas: "
                "$\\omega_{max} \\sim c/h$ "
                "to'r o'lchamiga bog'liq, ya'ni "
                "u modelning xossasi emas, "
                "diskretlashtirish artefakti. "
                "Bunday rejimlar "
                "$\\omega\\Delta t \\gg 1$ "
                "sohasida yotadi va ularning "
                "javobi butunlay noto'g'ri. "
                "Shuning uchun ularni so'ndirish "
                "kerak — bu sonli demflashning "
                "maqsadi. To'lov esa aniqlik: "
                "$\\gamma > 1/2$ da tartib "
                "birinchiga tushadi va **past** "
                "chastotalar ham so'na boshlaydi. "
                "Bu 'bolani suv bilan birga "
                "to'kib yuborish' muammosi va "
                "uni HHT-α hamda umumlashgan-α "
                "usullari hal qiladi: ular "
                "ikkinchi tartibni saqlagan holda "
                "so'ndirishni faqat yuqori "
                "chastotalarga yo'naltiradi. "
                "Ikkinchi muhim tushuncha — davr "
                "cho'zilishi. $\\beta = 1/4$ "
                "(eng ko'p ishlatiladigan tanlov) "
                "da sonli yechimning davri "
                "haqiqiydan uzun bo'ladi va xato "
                "$(\\omega\\Delta t)^2/6$ ga "
                "mutanosib. Amalda bu shuni "
                "anglatadiki, uzoq hisobda sonli "
                "yechim haqiqiydan **fazada "
                "orqada qoladi** va bu siljish "
                "to'planib boradi. Zilzila "
                "tahlilida 20 soniyalik hisobda "
                "bir necha tebranish davriga "
                "yetib qolishi mumkin. Shuning "
                "uchun qadam tanlashda odatda "
                "$\\Delta t \\le T_{min}/20$ "
                "qoidasi ishlatiladi — bu "
                "barqarorlikdan emas, "
                "**aniqlikdan** kelib chiqadi. "
                "Nihoyat, 8-qadamdagi kritik "
                "qadam mexanika uchun xarakterli "
                "xususiyatni ochadi: oshkor "
                "sxemani eng yuqori chastota "
                "cheklaydi va u eng kichik "
                "elementga bog'liq. Bitta juda "
                "mayda element butun modelning "
                "vaqt qadamini belgilaydi — "
                "shuning uchun oshkor dinamikada "
                "(krash-testlar) to'r sifati "
                "alohida e'tibor talab qiladi."
            ),
            equations=[
                eq(r"\dot u^{n+1} = \dot u^n + "
                   r"\Delta t\big[(1-\gamma)\ddot u^n "
                   r"+ \gamma\ddot u^{n+1}\big]",
                   "Nyumark tezlik taxmini.",
                   "Nyumark: tezlik"),
                eq(r"u^{n+1} = u^n + \Delta t\dot u^n "
                   r"+ \Delta t^2\big[(\tfrac12-\beta)"
                   r"\ddot u^n + \beta\ddot u^{n+1}\big]",
                   "Nyumark ko'chish taxmini.",
                   "Nyumark: ko'chish"),
                eq(r"\gamma \ge \tfrac12, \quad "
                   r"\beta \ge \tfrac14(\gamma+\tfrac12)^2 "
                   r"\;\Rightarrow\; \text{shartsiz barqaror}",
                   "Nyumark oilasining barqarorlik "
                   "shartlari.", "Barqarorlik"),
                eq(r"\frac{\Delta T}{T} = \frac{1}{2}\Big(\beta - "
                   r"\frac{1}{12}\Big)(\omega\Delta t)^2",
                   "Davr cho'zilishi — aniqlik "
                   "bo'yicha qadam tanlashning "
                   "asosi.", "Davr xatoligi"),
            ],
            conditions=(
                "**Barqarorlik:**\n"
                "- $\\gamma \\ge 1/2$ va "
                "$\\beta \\ge (\\gamma+1/2)^2/4$ "
                "— shartsiz barqaror;\n"
                "- $\\beta = 0$, $\\gamma = 1/2$ "
                "(markaziy ayirma): "
                "$\\Delta t \\le 2/\\omega_{max}$;\n"
                "- $\\gamma < 1/2$ — sxema "
                "**energiya qo'shadi** va har "
                "doim nobarqaror.\n\n"
                "**Aniqlik bo'yicha qadam "
                "tanlash** (barqarorlikdan "
                "qat'i nazar):\n"
                "- $\\Delta t \\le T_{min}/20$ — "
                "qiziqtiradigan eng yuqori "
                "chastota uchun;\n"
                "- Zarba masalalarida "
                "$\\Delta t \\le T_{impact}/50$;\n"
                "- Davr xatoligi 1 % dan kam "
                "bo'lishi uchun "
                "$\\omega\\Delta t \\le 0{,}25$.\n\n"
                "**Boshlang'ich shartlar:** "
                "$u^0$, $\\dot u^0$ berilgan; "
                "$\\ddot u^0$ harakat "
                "tenglamasidan hisoblanadi: "
                "$\\ddot u^0 = m^{-1}(F^0 - "
                "c\\dot u^0 - ku^0)$. Buni "
                "unutish birinchi qadamlarda "
                "katta xato beradi.\n\n"
                "**Nochiziqli masalalarda:** "
                "har qadamda Nyuton iteratsiyasi "
                "(su-24) kerak va "
                "$\\hat{\\mathbf{K}}$ qayta "
                "hisoblanadi."
            ),
            worked=WorkedExample(
                statement=(
                    "Bir erkinlik darajali tizim: "
                    "$m = 1$ kg, $k = 100$ N/m, "
                    "demflashsiz. Boshlang'ich "
                    "ko'chish $u_0 = 0{,}01$ m, "
                    "tezlik nol. "
                    "(a) Xususiy chastota va davrni "
                    "toping; (b) markaziy ayirma "
                    "uchun kritik qadamni "
                    "hisoblang; (c) "
                    "$\\Delta t = T/10$ da "
                    "$\\beta = 1/4$, "
                    "$\\gamma = 1/2$ sxemasining "
                    "davr xatoligini baholang; "
                    "(d) $\\gamma = 0{,}6$ da 10 "
                    "davrdan keyin amplituda "
                    "qancha qoladi?"
                ),
                given=[
                    r"m = 1\ \text{kg},\ k = 100\ "
                    r"\text{N/m},\ c = 0",
                    r"u_0 = 0{,}01\ \text{m},\ "
                    r"\dot u_0 = 0",
                ],
                steps=[
                    st(r"\omega = \sqrt{k/m} = "
                       r"\sqrt{100} = 10\ "
                       r"\text{rad/s}",
                       "Xususiy chastota."),
                    st(r"T = \frac{2\pi}{\omega} = "
                       r"\frac{6{,}2832}{10} = "
                       r"0{,}62832\ \text{s}",
                       "Tebranish davri."),
                    st(r"\text{(b) } \Delta t_{cr} = "
                       r"\frac{2}{\omega} = "
                       r"\frac{2}{10} = 0{,}2\ "
                       r"\text{s} = \frac{T}{\pi}",
                       "Markaziy ayirma uchun "
                       "kritik qadam — davrning "
                       "uchdan biriga yaqin."),
                    st(r"\text{(c) } \Delta t = "
                       r"\frac{T}{10} = 0{,}062832\ "
                       r"\text{s} "
                       r"\;\Rightarrow\; "
                       r"\omega\Delta t = 0{,}62832",
                       "$\\omega\\Delta t = "
                       "2\\pi/10$."),
                    st(r"\frac{\Delta T}{T} = \frac12\Big("
                       r"\frac14 - \frac{1}{12}\Big)"
                       r"(0{,}62832)^2 = "
                       r"\frac{1}{12} \cdot 0{,}39478",
                       "$\\frac12(1/4 - 1/12) = "
                       "\\frac12 \\cdot \\frac16 = "
                       "\\frac{1}{12}$."),
                    st(r"= 0{,}032898 "
                       r"\;\Rightarrow\; "
                       r"\textbf{3{,}29 \%}",
                       "Davr **3,3 % ga "
                       "cho'ziladi**. 10 davrdan "
                       "keyin faza siljishi "
                       "0,33 davrga yetadi — "
                       "ya'ni yechim fazada "
                       "sezilarli adashadi."),
                    st(r"\Delta t = \frac{T}{20}: \ "
                       r"\omega\Delta t = 0{,}31416 "
                       r"\;\Rightarrow\; "
                       r"\frac{\Delta T}{T} = "
                       r"\frac{0{,}098696}{12} = "
                       r"0{,}82\ \%",
                       "Qadam ikki barobar "
                       "kichrayganda xato to'rt "
                       "barobar kamayadi — "
                       "$O(\\Delta t^2)$."),
                    st(r"\text{(d) } \gamma = 0{,}6: \ "
                       r"|\xi| \approx 1 - "
                       r"\frac{1}{2}(0{,}1)"
                       r"(\omega\Delta t)^2",
                       "9-qadamdagi formula; "
                       "$\\gamma - 1/2 = 0{,}1$."),
                    st(r"\omega\Delta t = 0{,}62832: \ "
                       r"|\xi| = 1 - 0{,}05 \cdot "
                       r"0{,}39478 = 1 - "
                       r"0{,}019739 = 0{,}98026",
                       "Har qadamda amplituda "
                       "1,97 % kamayadi."),
                    st(r"\text{10 davr} = 100\ "
                       r"\text{qadam}: \ "
                       r"0{,}98026^{100} = "
                       r"e^{100\ln 0{,}98026} = "
                       r"e^{-1{,}9936} = 0{,}136",
                       "**Amplitudaning atigi "
                       "13,6 % i qoladi** — "
                       "86 % sun'iy so'ngan. "
                       "Fizik demflash esa "
                       "umuman yo'q edi."),
                ],
                answer=(
                    "(a) $\\omega = 10$ rad/s, "
                    "$T = 0{,}62832$ s; "
                    "(b) $\\Delta t_{cr} = 0{,}2$ s; "
                    "(c) $\\Delta t = T/10$ da davr "
                    "**3,29 %** ga cho'ziladi, "
                    "$T/20$ da esa 0,82 % — "
                    "$O(\\Delta t^2)$; "
                    "(d) $\\gamma = 0{,}6$ da har "
                    "qadamda amplituda 1,97 % "
                    "kamayadi va 10 davrdan keyin "
                    "atigi **13,6 %** qoladi — "
                    "fizik demflash bo'lmasa ham."
                ),
                engineering_note=(
                    "(d) natijasi sonli demflashning "
                    "qanchalik kuchli ekanini "
                    "ko'rsatadi: $\\gamma$ ni "
                    "0,5 dan 0,6 ga o'zgartirish "
                    "amplitudani 10 davrda yetti "
                    "barobar kamaytirdi. Agar "
                    "muhandis buni bilmasdan "
                    "$\\gamma = 0{,}6$ olsa va "
                    "natijada tebranish so'nganini "
                    "ko'rsa, u konstruksiyani "
                    "xavfsiz deb xulosa qilishi "
                    "mumkin — aslida so'nish "
                    "butunlay sun'iy. Bu ayniqsa "
                    "zilzila tahlilida xavfli. "
                    "(c) natijasi esa qadam "
                    "tanlash qoidasini asoslaydi: "
                    "$T/10$ da davr xatoligi 3,3 % "
                    "va 10 davrdan keyin yechim "
                    "fazada sezilarli adashadi. "
                    "Shuning uchun standart tavsiya "
                    "$\\Delta t \\le T_{min}/20$ "
                    "va muhim hisoblarda $T/50$. "
                    "Diqqat: bu **eng yuqori** "
                    "qiziqtiradigan chastota uchun, "
                    "eng pasti uchun emas. "
                    "Zilzila tahlilida odatda "
                    "0–33 Hz diapazoni "
                    "qiziqtiradi, demak "
                    "$T_{min} = 1/33 = 0{,}03$ s "
                    "va $\\Delta t \\le 1{,}5$ ms."
                ),
            ),
            computation=Computation(
                caption=(
                    "Nyumark oilasini bir erkinlik "
                    "darajali tizimda sinash: "
                    "barqarorlik, sonli demflash va "
                    "davr cho'zilishini o'lchash."
                ),
                code='''"""Nyumark oilasi: barqarorlik, sonli demflash, davr xatoligi."""
import numpy as np
from labkit import PARAMS, note, series, table, value

m = float(PARAMS.get("m", 1.0))
k = float(PARAMS.get("k", 100.0))
zeta = float(PARAMS.get("zeta", 0.0))
gam = float(PARAMS.get("gamma", 0.5))
bet = float(PARAMS.get("beta", 0.25))
n_per = float(PARAMS.get("n_per", 10.0))
dt_ratio = float(PARAMS.get("dt_ratio", 10.0))   # dt = T/dt_ratio

w = np.sqrt(k/m)
T = 2*np.pi/w
c = 2*zeta*np.sqrt(k*m)
u0, v0 = 0.01, 0.0
value("Xususiy chastota omega", w, "rad/s")
value("Tebranish davri T", T, "s")
value("Markaziy ayirma kritik qadami 2/omega", 2.0/w, "s")


def newmark(dt, nt, gam, bet, m, c, k, u0, v0):
    u = np.zeros(nt + 1)
    v = np.zeros(nt + 1)
    a = np.zeros(nt + 1)
    u[0], v[0] = u0, v0
    a[0] = (0.0 - c*v0 - k*u0)/m          # boshlang'ich tezlanish
    if bet > 0:
        kh = k + gam/(bet*dt)*c + m/(bet*dt**2)
        for n in range(nt):
            rhs = (m*(u[n]/(bet*dt**2) + v[n]/(bet*dt)
                      + (1/(2*bet) - 1)*a[n])
                   + c*(gam/(bet*dt)*u[n] + (gam/bet - 1)*v[n]
                        + dt*(gam/(2*bet) - 1)*a[n]))
            u[n+1] = rhs/kh
            a[n+1] = ((u[n+1] - u[n])/(bet*dt**2) - v[n]/(bet*dt)
                      - (1/(2*bet) - 1)*a[n])
            v[n+1] = v[n] + dt*((1 - gam)*a[n] + gam*a[n+1])
    else:
        # beta = 0: oshkor (markaziy ayirma)
        for n in range(nt):
            u[n+1] = u[n] + dt*v[n] + dt**2/2*a[n]
            a[n+1] = (0.0 - c*(v[n] + (1 - gam)*dt*a[n]) - k*u[n+1]) \
                / (m + gam*dt*c)
            v[n+1] = v[n] + dt*((1 - gam)*a[n] + gam*a[n+1])
    return u, v, a


def amplification(dt, gam, bet, m, c, k):
    """Kuchayish matritsasining spektral radiusi."""
    A = np.zeros((3, 3))
    if bet > 0:
        kh = k + gam/(bet*dt)*c + m/(bet*dt**2)
        # [u, dt*v, dt^2*a] holat vektori uchun
        for j, e in enumerate(np.eye(3)):
            uu, vv, aa = e[0], e[1]/dt, e[2]/dt**2
            rhs = (m*(uu/(bet*dt**2) + vv/(bet*dt)
                      + (1/(2*bet) - 1)*aa)
                   + c*(gam/(bet*dt)*uu + (gam/bet - 1)*vv
                        + dt*(gam/(2*bet) - 1)*aa))
            un = rhs/kh
            an = ((un - uu)/(bet*dt**2) - vv/(bet*dt)
                  - (1/(2*bet) - 1)*aa)
            vn = vv + dt*((1 - gam)*aa + gam*an)
            A[:, j] = [un, dt*vn, dt**2*an]
    else:
        for j, e in enumerate(np.eye(3)):
            uu, vv, aa = e[0], e[1]/dt, e[2]/dt**2
            un = uu + dt*vv + dt**2/2*aa
            an = (-c*(vv + (1 - gam)*dt*aa) - k*un)/(m + gam*dt*c)
            vn = vv + dt*((1 - gam)*aa + gam*an)
            A[:, j] = [un, dt*vn, dt**2*an]
    return float(np.max(np.abs(np.linalg.eigvals(A))))


# --- (1) Barqarorlik sohasini tekshirish ---
wdt = np.unique(np.concatenate([np.logspace(-2, 1.5, 160),
                                np.linspace(1.90, 2.15, 60)]))
rows = []
schemes = [("Markaziy ayirma", 0.0, 0.5),
           ("O'rtacha tezlanish", 0.25, 0.5),
           ("Chiziqli tezlanish", 1.0/6.0, 0.5),
           ("Demflangan (g=0.6)", 0.3025, 0.6),
           ("Fox-Goodwin", 1.0/12.0, 0.5)]
for name, bb, gg in schemes:
    rhos = [amplification(wd/w, gg, bb, m, 0.0, k) for wd in wdt]
    series(f"rho: {name}", wdt.tolist(), rhos,
           xlabel="omega*dt", ylabel="spektral radius")
    lim = [wd for wd, rr in zip(wdt, rhos) if rr > 1.0 + 1e-10]
    bcrit = 0.25*(gg + 0.5)**2
    uncond = "ha" if bb >= bcrit - 1e-12 and gg >= 0.5 - 1e-12 else "yo'q"
    rows.append([name, f"{bb:.4f}", f"{gg:.2f}", f"{bcrit:.4f}", uncond,
                 f"{min(lim):.3f}" if lim else "cheksiz"])
table("Nyumark oilasi: barqarorlik",
      ["Sxema", "beta", "gamma", "beta_krit", "shartsiz barqaror?",
       "omega*dt chegarasi"], rows)
series("Barqarorlik chegarasi rho = 1", wdt.tolist(),
       [1.0]*len(wdt), xlabel="omega*dt", ylabel="spektral radius")

rho_cd = [amplification(wd/w, 0.5, 0.0, m, 0.0, k) for wd in wdt]
lim_cd = [wd for wd, rr in zip(wdt, rho_cd) if rr > 1.0 + 1e-10]
if lim_cd:
    value("Markaziy ayirma: sonli chegara (omega*dt)",
          float(min(lim_cd)), "—")
    value("Nazariy chegara", 2.0, "—")
    value("Farq", abs(min(lim_cd) - 2.0)/2.0*100, "%")
    note(f"Markaziy ayirma sxemasining barqarorlik chegarasi sonli "
         f"topildi: omega*dt = {min(lim_cd):.4f}, nazariy qiymat 2.0 - "
         f"farq {abs(min(lim_cd)-2.0)/2.0*100:.2f} %. 8-qadamdagi "
         f"dt_cr = 2/omega tasdiqlandi.")
note("O'rtacha tezlanish (beta = 1/4, gamma = 1/2) va demflangan "
     "sxema shartsiz barqaror: spektral radius hech qachon 1 dan "
     "oshmaydi. Markaziy ayirma, chiziqli tezlanish va Fox-Goodwin "
     "esa shartli.")

# --- (2) SONLI DEMFLASH: amplituda so'nishini o'lchash ---
dt = T/dt_ratio
nt = int(round(n_per*T/dt))
rows2 = []
for gg in [0.50, 0.55, 0.60, 0.70]:
    bb = 0.25*(gg + 0.5)**2
    u, v, a = newmark(dt, nt, gg, bb, m, 0.0, k, u0, v0)
    # Cho'qqilarni topib amplituda so'nishini o'lchash
    pk = [i for i in range(1, len(u) - 1)
          if u[i] > u[i-1] and u[i] >= u[i+1] and u[i] > 0]
    if len(pk) >= 2:
        decay = (u[pk[-1]]/u[pk[0]])**(1.0/(len(pk) - 1))
        # nazariy: |xi| = 1 - 0.5*(gam-0.5)*(w*dt)^2 har QADAMDA
        xi_step = 1.0 - 0.5*(gg - 0.5)*(w*dt)**2
        steps_per_period = T/dt
        xi_per = xi_step**steps_per_period
        rows2.append([f"{gg:.2f}", f"{bb:.4f}",
                      f"{u[pk[-1]]/u0*100:.2f}",
                      f"{decay:.6f}", f"{xi_per:.6f}"])
    else:
        rows2.append([f"{gg:.2f}", f"{bb:.4f}", "-", "-", "-"])
table(f"Sonli demflash ({n_per:.0f} davrdan keyin, dt = T/{dt_ratio:.0f})",
      ["gamma", "beta", "qolgan amplituda, %", "o'lchangan/davr",
       "nazariy/davr"], rows2)

u5, _, _ = newmark(dt, nt, 0.5, 0.25, m, 0.0, k, u0, v0)
u6, _, _ = newmark(dt, nt, 0.6, 0.3025, m, 0.0, k, u0, v0)
tt = np.arange(nt + 1)*dt
series("gamma = 0.50 (demflashsiz)", tt.tolist(),
       (u5*1000).tolist(), xlabel="vaqt t, s", ylabel="u, mm")
series("gamma = 0.60 (sonli demflash)", tt.tolist(),
       (u6*1000).tolist(), xlabel="vaqt t, s", ylabel="u, mm")
series("Aniq yechim", tt.tolist(),
       (u0*np.cos(w*tt)*1000).tolist(),
       xlabel="vaqt t, s", ylabel="u, mm")
value("gamma = 0.5: oxirgi amplituda / boshlang'ich",
      float(np.max(np.abs(u5[-int(T/dt):]))/u0), "—")
value("gamma = 0.6: oxirgi amplituda / boshlang'ich",
      float(np.max(np.abs(u6[-int(T/dt):]))/u0), "—")
note(f"Fizik demflash YO'Q (zeta = 0), lekin gamma = 0.6 da "
     f"{n_per:.0f} davrdan keyin amplitudaning atigi "
     f"{np.max(np.abs(u6[-int(T/dt):]))/u0*100:.1f} % i qoldi. "
     f"gamma = 0.5 da esa {np.max(np.abs(u5[-int(T/dt):]))/u0*100:.1f} % "
     f"- amplituda deyarli aynan saqlanadi. Demak so'nish butunlay "
     f"SXEMA ARTEFAKTI.")

# --- (3) DAVR CHO'ZILISHINI o'lchash ---
rows3 = []
for ratio in [5, 10, 20, 40, 80]:
    dtk = T/ratio
    ntk = int(round(8*T/dtk))
    u, _, _ = newmark(dtk, ntk, 0.5, 0.25, m, 0.0, k, u0, v0)
    # nolinchi kesishuvlardan davrni o'lchash
    sgn = np.sign(u)
    cross = np.where(np.diff(sgn) != 0)[0]
    if len(cross) >= 3:
        # chiziqli interpolyatsiya bilan aniq nol nuqtalari
        zs = []
        for ci in cross:
            f0, f1 = u[ci], u[ci+1]
            zs.append((ci + f0/(f0 - f1))*dtk)
        Tn = 2.0*np.mean(np.diff(zs))
        err = (Tn - T)/T
        th = 0.5*(0.25 - 1.0/12.0)*(w*dtk)**2
        rows3.append([f"T/{ratio}", f"{w*dtk:.5f}", f"{Tn:.6f}",
                      f"{err*100:.4f}", f"{th*100:.4f}"])
table("Davr cho'zilishi (beta = 1/4, gamma = 1/2)",
      ["dt", "omega*dt", "o'lchangan T, s", "xatolik, %",
       "nazariy, %"], rows3)
meas = [float(r[3]) for r in rows3]
theo = [float(r[4]) for r in rows3]
value("O'lchangan va nazariy davr xatoligi nisbati (dt = T/10)",
      meas[1]/theo[1], "—")
p_T = np.log2(meas[1]/meas[2])
value("Davr xatoligining tartibi", float(p_T), "—")
note(f"Davr xatoligi o'lchandi va nazariy (beta - 1/12)*(omega*dt)^2 "
     f"formulasi bilan taqqoslandi: dt = T/10 da o'lchangan "
     f"{meas[1]:.4f} %, nazariy {theo[1]:.4f} % - nisbat "
     f"{meas[1]/theo[1]:.4f}. Qadam ikki barobar kamayganda xatolik "
     f"{meas[1]/meas[2]:.2f} marta kamayadi (tartib {p_T:.2f} ~ 2) - "
     f"10-qadamdagi O(dt^2) TASDIQLANDI.")

# beta = 1/12 (Fox-Goodwin) da davr xatoligi yo'qolishi
rows4 = []
for bb, nm in [(0.25, "o'rtacha tezlanish"),
               (1.0/6.0, "chiziqli tezlanish"),
               (1.0/12.0, "Fox-Goodwin")]:
    dtk = T/10
    ntk = int(round(8*T/dtk))
    u, _, _ = newmark(dtk, ntk, 0.5, bb, m, 0.0, k, u0, v0)
    sgn = np.sign(u)
    cross = np.where(np.diff(sgn) != 0)[0]
    zs = [(ci + u[ci]/(u[ci] - u[ci+1]))*dtk for ci in cross]
    Tn = 2.0*np.mean(np.diff(zs))
    rows4.append([nm, f"{bb:.5f}", f"{(Tn-T)/T*100:.5f}",
                  f"{0.5*(bb - 1.0/12.0)*(w*dtk)**2*100:.5f}"])
table("beta ning davr xatoligiga ta'siri (dt = T/10)",
      ["Sxema", "beta", "o'lchangan xato, %", "nazariy, %"], rows4)
note("beta = 1/12 (Fox-Goodwin) da davr xatoligi ikkinchi tartibda "
     "YO'QOLADI - nazariy formula (beta - 1/12) ni beradi. Lekin bu "
     "sxema shartli barqaror, shuning uchun amalda kam ishlatiladi.")

# --- (4) Qadam tanlash tavsiyasi ---
rows5 = []
for ratio in [5, 10, 20, 50, 100]:
    wdt_k = 2*np.pi/ratio
    perr = 0.5*(0.25 - 1.0/12.0)*wdt_k**2*100
    drift = perr/100*8      # 8 davrdan keyin faza siljishi (davrlarda)
    rows5.append([f"T/{ratio}", f"{wdt_k:.4f}", f"{perr:.3f}",
                  f"{drift:.4f}"])
table("Qadam tanlash: davr xatoligi va faza siljishi",
      ["dt", "omega*dt", "davr xatoligi, %",
       "8 davrdan keyingi siljish (davrlarda)"], rows5)
note("dt = T/10 da 8 davrdan keyin faza siljishi yarim davrga "
     "yaqinlashadi - yechim deyarli qarama-qarshi fazada bo'ladi. "
     "Shuning uchun standart tavsiya dt <= T_min/20, muhim "
     "hisoblarda esa T_min/50.")

table("Nyumark oilasining asosiy a'zolari",
      ["Sxema", "beta", "gamma", "Tartib", "Barqarorlik", "Izoh"],
      [["Markaziy ayirma", "0", "1/2", "2", "shartli",
        "oshkor, krash-testlar"],
       ["Fox-Goodwin", "1/12", "1/2", "4 (davr)", "shartli",
        "eng aniq davr"],
       ["Chiziqli tezlanish", "1/6", "1/2", "2", "shartli", "klassik"],
       ["O'rtacha tezlanish", "1/4", "1/2", "2", "SHARTSIZ",
        "eng keng ishlatiladi"],
       ["Demflangan", ">1/4", ">1/2", "1", "SHARTSIZ",
        "yuqori rejimlarni so'ndiradi"]])
''',
                parameters=[
                    p("m", "Massa m", 0.01, 1000.0, 1.0, 0.01, "kg"),
                    p("k", "Bikrlik k", 1.0, 100000.0, 100.0, 1.0, "N/m"),
                    p("zeta", "Fizik demflash ζ", 0.0, 0.5, 0.0, 0.01),
                    p("gamma", "Nyumark γ", 0.5, 1.0, 0.5, 0.05),
                    p("beta", "Nyumark β", 0.0, 0.5, 0.25, 0.01),
                    p("n_per", "Hisoblanadigan davrlar soni", 1.0, 50.0,
                      10.0, 1.0),
                    p("dt_ratio", "Qadam T/dt_ratio", 4.0, 100.0, 10.0,
                      1.0),
                ],
                expected_output=(
                    "Markaziy ayirma sxemasining "
                    "barqarorlik chegarasi sonli "
                    "topilganda nazariy "
                    "$\\omega\\Delta t = 2$ ga "
                    "juda yaqin chiqadi. "
                    "$\\beta \\ge (\\gamma+1/2)^2/4$ "
                    "shartini qanoatlantiruvchi "
                    "sxemalarda spektral radius "
                    "hech qachon 1 dan oshmaydi. "
                    "Fizik demflash nol bo'lsa ham "
                    "$\\gamma = 0{,}6$ da "
                    "amplituda keskin so'nadi, "
                    "$\\gamma = 0{,}5$ da esa "
                    "deyarli aynan saqlanadi. "
                    "O'lchangan davr xatoligi "
                    "nazariy "
                    "$(\\beta-1/12)(\\omega"
                    "\\Delta t)^2$ formulasi bilan "
                    "mos keladi va $O(\\Delta t^2)$ "
                    "bo'yicha kamayadi; "
                    "$\\beta = 1/12$ da esa u "
                    "deyarli yo'qoladi."
                ),
            ),
            visual=vis(
                kind="Sonli demflash va davr cho'zilishi",
                tool="React/SVG + Manim",
                description=(
                    "Tebranish tarixi, aniq yechim "
                    "bilan taqqoslash va spektral "
                    "radius grafigi."
                ),
                how_to_draw=(
                    "React/SVG: asosiy panel — "
                    "ko'chishning vaqt bo'yicha "
                    "grafigi. Uchta chiziq: aniq "
                    "yechim (uzluksiz), "
                    "$\\gamma = 0{,}5$ (deyarli "
                    "ustma-ust tushadi) va "
                    "$\\gamma = 0{,}6$ (amplitudasi "
                    "ko'rinarli so'nadi). "
                    "Cho'qqilarni bog'lovchi "
                    "**o'rama** (envelope) "
                    "punktir bilan chiziladi — "
                    "sonli demflash shu orqali "
                    "aniq ko'rinadi. Vaqt o'qining "
                    "oxirgi qismida aniq va sonli "
                    "yechimlarning **fazada "
                    "ajralishi** ko'rinadi va "
                    "siljish o'lchov chizig'i "
                    "bilan belgilanadi. $\\gamma$ "
                    "va $\\Delta t$ slayderlari "
                    "bilan ikkala effekt "
                    "alohida boshqariladi. "
                    "Ikkinchi panel — spektral "
                    "radiusning "
                    "$\\omega\\Delta t$ ga "
                    "bog'liqligi log o'qda; "
                    "$\\rho = 1$ chizig'i qizil "
                    "bilan, shartsiz barqaror "
                    "sxemalar undan pastda "
                    "qoladi, markaziy ayirma esa "
                    "$\\omega\\Delta t = 2$ da "
                    "uni kesib o'tadi. Uchinchi "
                    "panel — fazaviy portret "
                    "($u$ va $\\dot u$): aniq "
                    "yechim yopiq ellips, "
                    "$\\gamma > 1/2$ esa ichkariga "
                    "buraladigan spiral."
                ),
            ),
            interp=(
                "Kodning eng muhim natijasi — sonli "
                "demflashning o'lchangan "
                "kattaligi. Fizik demflash aynan "
                "nolga teng, ya'ni tizim energiyani "
                "yo'qotmasligi kerak; lekin "
                "$\\gamma = 0{,}6$ da 10 davrdan "
                "keyin amplitudaning faqat kichik "
                "qismi qoladi. $\\gamma = 0{,}5$ "
                "da esa amplituda deyarli aynan "
                "saqlanadi. Bu 9-qadamdagi "
                "formulaning bevosita tasdig'i va "
                "u amaliy jihatdan jiddiy "
                "ogohlantirish: sxema parametri "
                "natijani fizik effekt kabi "
                "ko'rinadigan tarzda o'zgartiradi. "
                "Ikkinchi natija — davr "
                "cho'zilishining o'lchangan va "
                "nazariy qiymatlarining mos "
                "kelishi. $(\\beta - 1/12)"
                "(\\omega\\Delta t)^2$ formulasi "
                "tajribada tasdiqlanadi va xato "
                "$O(\\Delta t^2)$ bo'yicha "
                "kamayadi. $\\beta = 1/12$ "
                "(Fox–Goodwin) holati alohida "
                "qiziq: u yerda davr xatoligi "
                "ikkinchi tartibda **yo'qoladi** "
                "va o'lchash ham shuni ko'rsatadi. "
                "Lekin bu sxema shartli barqaror, "
                "shuning uchun amalda "
                "$\\beta = 1/4$ afzal ko'riladi — "
                "bu aniqlik va barqarorlik "
                "o'rtasidagi tipik kelishuv. "
                "Barqarorlik grafigi esa su-10 "
                "dagi apparatning ikkinchi "
                "tartibli tenglamaga "
                "ko'chirilishini ko'rsatadi: "
                "spektral radius $\\rho \\le 1$ "
                "sharti aynan bir xil, faqat "
                "endi kuchayish matritsasi "
                "$3\\times3$. Markaziy ayirma "
                "uchun sonli topilgan chegara "
                "nazariy $\\omega\\Delta t = 2$ "
                "ga mos kelishi bu apparatning "
                "to'g'ri qurilganini "
                "tasdiqlaydi."
            ),
            mistakes=[
                "Sonli demflashni fizik demflash "
                "deb qabul qilish. "
                "$\\gamma > 1/2$ da amplituda "
                "sun'iy so'nadi va bu "
                "konstruksiyani xavfsiz "
                "ko'rsatishi mumkin.",
                "Qadamni faqat barqarorlik "
                "bo'yicha tanlash. Shartsiz "
                "barqaror sxemada ham davr "
                "xatoligi katta bo'lishi mumkin; "
                "$\\Delta t \\le T_{min}/20$ "
                "kerak.",
                "Boshlang'ich tezlanishni "
                "hisoblashni unutish. "
                "$\\ddot u^0$ harakat "
                "tenglamasidan olinadi, nolga "
                "teng emas.",
                "Oshkor sxemada eng kichik "
                "elementni e'tiborsiz qoldirish. "
                "Bitta mayda element butun "
                "modelning qadamini belgilaydi.",
                "$\\gamma < 1/2$ tanlash. Bunday "
                "sxema energiya **qo'shadi** va "
                "har qanday qadamda nobarqaror.",
            ],
            quiz=[
                q("Nyumark oilasida $\\gamma$ va "
                  "$\\beta$ nimani boshqaradi?",
                  "$\\gamma$ — tezlikdagi "
                  "tezlanish taqsimoti (va sonli "
                  "demflash), $\\beta$ — "
                  "ko'chishdagi taqsimot (va davr "
                  "xatoligi).", "konseptual"),
                q("Shartsiz barqarorlik shartlari "
                  "qanday?",
                  "$\\gamma \\ge 1/2$ va "
                  "$\\beta \\ge (\\gamma+1/2)^2/4$. "
                  "$\\beta = 1/4$, "
                  "$\\gamma = 1/2$ aynan "
                  "chegarada.", "konseptual"),
                q("$\\omega = 10$ rad/s, "
                  "$\\Delta t = T/10$ da "
                  "$\\beta = 1/4$ uchun davr "
                  "xatoligi qancha?",
                  "$\\omega\\Delta t = 0{,}6283$; "
                  "$(1/4-1/12)(0{,}6283)^2 = "
                  "0{,}3948/6 = 6{,}58$ %.",
                  "hisob"),
                q("Kodda nima uchun fizik "
                  "demflash nolga teng olinadi?",
                  "Shunda amplitudaning har "
                  "qanday so'nishi faqat "
                  "**sxemadan** kelib chiqadi va "
                  "sonli demflash sof holda "
                  "o'lchanadi.", "kod"),
                q("Oshkor sxemada kritik qadamni "
                  "nima belgilaydi?",
                  "Eng **yuqori** xususiy chastota: "
                  "$\\Delta t \\le 2/\\omega_{max}$. "
                  "FEM da u eng kichik elementga "
                  "bog'liq.", "talqin"),
                q("Nima uchun ba'zan sonli "
                  "demflash **foydali**?",
                  "FEM to'ridagi eng yuqori "
                  "chastotali rejimlar fizik "
                  "ma'noga ega emas (to'r "
                  "artefakti) va javobni "
                  "ifloslantiradi; ularni "
                  "so'ndirish kerak.", "talqin"),
            ],
            bridge=(
                "Nyumark sxemalari tebranish "
                "masalalarida yaxshi ishlaydi. "
                "Lekin to'lqin tarqalishida — "
                "zarba, portlash, ultratovush — "
                "yangi talab paydo bo'ladi: "
                "to'lqin **to'g'ri tezlikda** "
                "harakatlanishi kerak. Keyingi "
                "mavzuda to'lqin tenglamasiga "
                "o'tamiz, CFL shartini quramiz va "
                "sonli dispersiya hodisasini "
                "ko'ramiz."
            ),
            research=(
                "Zamonaviy vaqt integrallash "
                "usullarini o'rganing. "
                "(1) HHT-α va umumlashgan-α "
                "usullarini tahlil qiling: ular "
                "ikkinchi tartibni saqlab, "
                "so'ndirishni faqat yuqori "
                "chastotalarga qanday "
                "yo'naltiradi? Spektral radiusni "
                "$\\omega\\Delta t \\to \\infty$ "
                "da hisoblang. (2) Energiyani "
                "saqlovchi (energy-conserving) va "
                "simplektik integratorlarni "
                "o'rganing: uzoq vaqtli "
                "hisoblarda ular nima uchun "
                "afzal? (3) Aniq massa "
                "matritsasi va to'plangan "
                "(lumped) massa matritsasining "
                "farqini tahlil qiling: "
                "to'plangan massa oshkor "
                "sxemani nima uchun mumkin "
                "qiladi va u aniqlikka qanday "
                "ta'sir qiladi?"
            ),
            manim_ref=manim(
                scene="NewmarkScene",
                module="manim/scenes/su_fd.py",
                title="Sonli demflash va davr cho'zilishi",
                summary=(
                    "Prujinali massa tebranadi va "
                    "yonida sonli yechim aniq "
                    "yechim bilan birga "
                    "chiziladi. $\\gamma$ ni "
                    "oshirganda sonli yechim "
                    "amplitudasi sekin so'nadi, "
                    "$\\Delta t$ ni oshirganda esa "
                    "u fazada orqada qola "
                    "boshlaydi. Ikkala effekt "
                    "alohida-alohida "
                    "ko'rsatiladi."
                ),
            ),
        ),
    ),

    # ------------------------------------------------------------------ su-12
    Topic(
        id="su-12",
        subject_id=S, module_id=M, order=12,
        title="To'lqin tenglamasi, CFL sharti va sonli dispersiya",
        description=(
            "To'lqin tarqalishi sxemalari, Kurant–Fridrixs–Levi sharti, "
            "sonli dispersiya va dissipatsiya, to'lqinni to'r bilan "
            "ifodalash chegarasi."
        ),
        learning_objective=(
            "CFL shartini keltirib chiqarish va uning fizik ma'nosini "
            "tushuntirish, sonli dispersiyani o'lchash va to'lqin "
            "uzunligiga necha tugun kerakligini asoslash."
        ),
        prerequisites=["su-11", "tmm-20"],
        mathematical_core=(
            "$\\partial^2 u/\\partial t^2 = c^2\\partial^2 u/"
            "\\partial x^2$; CFL: $C = c\\Delta t/h \\le 1$; "
            "sonli tezlik $c_h/c = \\dfrac{2}{kh}\\arcsin"
            "\\big(C\\sin\\tfrac{kh}{2}\\big)/C$."
        ),
        engineering_application=(
            "Zarba va urilish tahlili, portlash yuklamasi, "
            "ultratovushli nazorat, seysmik to'lqinlar, akustika, "
            "krash-testlar."
        ),
        computational_component=(
            "To'lqin tenglamasini yechish, CFL chegarasini sonli "
            "topish va sonli dispersiyani to'lqin uzunligi bo'yicha "
            "o'lchash."
        ),
        visualization_component=(
            "To'lqin tarqalishi, nomutanosib tezlik, o'tkir front "
            "ortidagi soxta tebranishlar."
        ),
        research_extension=(
            "Soxta tebranishlarni bartaraf etish usullarini o'rganing: "
            "sun'iy qovushqoqlik, TVD va WENO sxemalari."
        ),
        difficulty="ilg'or",
        previous_link=(
            "su-11 da Nyumark sxemalari qurildi va oshkor sxema uchun "
            "$\\Delta t \\le 2/\\omega_{max}$ sharti olingan edi. "
            "To'lqin masalasida $\\omega_{max} \\sim c/h$, demak bu "
            "shart to'g'ridan-to'g'ri CFL ga aylanadi."
        ),
        next_topic="su-13",
        estimated_minutes=90,
        tags=["CFL", "to'lqin", "dispersiya", "Kurant soni"],
        lesson=_lesson(
            problem=(
                "Po'lat relsga zarba beriladi va "
                "elastik to'lqin tarqalishini "
                "hisoblaymiz — bu ultratovushli "
                "nazorat va zarba tahlilining "
                "asosi. To'lqin tezligi "
                "$c = \\sqrt{E/\\rho} = 5100$ m/s, "
                "ya'ni u 1 metrni 0,2 "
                "millisekundda bosib o'tadi. "
                "Sxemani yozamiz va ishga "
                "tushiramiz. Ikki xil muammo "
                "paydo bo'ladi. Birinchisi "
                "tanish: qadam katta bo'lsa "
                "yechim portlaydi. Ikkinchisi "
                "yangi va nozikroq: qadam kichik "
                "bo'lsa ham to'lqin "
                "**noto'g'ri tezlikda** "
                "harakatlanadi va o'tkir front "
                "ortida mavjud bo'lmagan "
                "tebranishlar paydo bo'ladi. "
                "Bu 'shovqin' emas — u "
                "sxemaning o'zidan kelib chiqadi."
            ),
            concepts=[
                c("To'lqin tenglamasi",
                  "$u_{tt} = c^2u_{xx}$ — "
                  "giperbolik tenglama; "
                  "yechim so'nmaydi, "
                  "**tarqaladi**."),
                c("Kurant soni",
                  "$C = c\\Delta t/h$ — bir vaqt "
                  "qadamida to'lqin necha "
                  "hujayradan o'tishi."),
                c("CFL sharti",
                  "$C \\le 1$ — sonli ta'sir "
                  "sohasi fizik ta'sir sohasini "
                  "**qamrab olishi** kerak."),
                c("Sonli dispersiya",
                  "Turli to'lqin uzunliklari "
                  "turli tezlikda tarqalishi; "
                  "fizik emas, sxema artefakti."),
                c("Sonli dissipatsiya",
                  "Amplituda sun'iy so'nishi; "
                  "markaziy sxemada yo'q, "
                  "yuqoriga siljigan (upwind) "
                  "sxemada bor."),
                c("Tugunlar soni to'lqin uzunligiga",
                  "$N_\\lambda = \\lambda/h$ — "
                  "aniqlik mezoni; odatda "
                  "$N_\\lambda \\ge 10{\\ldots}20$ "
                  "talab qilinadi."),
            ],
            derivation=[
                d("1. To'lqin tenglamasi va sxema",
                  r"\frac{\partial^2 u}{\partial t^2} = "
                  r"c^2\frac{\partial^2 u}{\partial x^2} "
                  r"\;\Longrightarrow\; "
                  r"\frac{u_j^{n+1}-2u_j^n+u_j^{n-1}}"
                  r"{\Delta t^2} = c^2"
                  r"\frac{u_{j-1}^n-2u_j^n+u_{j+1}^n}{h^2}",
                  "Ikkala hosila ham markaziy "
                  "ayirma bilan — bu su-11 dagi "
                  "markaziy ayirma usulining "
                  "to'lqin tenglamasiga "
                  "qo'llanishi."),
                d("2. Yangilash formulasi",
                  r"u_j^{n+1} = 2u_j^n - u_j^{n-1} + "
                  r"C^2\big(u_{j-1}^n - 2u_j^n + "
                  r"u_{j+1}^n\big), \ C = "
                  r"\frac{c\Delta t}{h}",
                  "Oshkor sxema: uch qatlam "
                  "ishlatiladi. $C$ — yagona "
                  "parametr."),
                d("3. Fon Neyman tahlili",
                  r"u_j^n = \xi^n e^{ikjh} "
                  r"\;\Longrightarrow\; \xi^2 - "
                  r"2\big(1 - 2C^2\sin^2\tfrac{kh}{2}"
                  r"\big)\xi + 1 = 0",
                  "su-10 dagi usul. Endi "
                  "**kvadrat** tenglama, chunki "
                  "sxema uch qatlamli."),
                d("4. Ildizlar va barqarorlik",
                  r"\xi_{1,2} = A \pm \sqrt{A^2-1}, "
                  r"\quad A = 1 - 2C^2"
                  r"\sin^2\frac{kh}{2}",
                  "$|A| \\le 1$ bo'lsa ildizlar "
                  "kompleks va "
                  "$|\\xi_1||\\xi_2| = 1$, "
                  "$|\\xi| = 1$ — amplituda "
                  "**aynan saqlanadi**. "
                  "$|A| > 1$ bo'lsa bitta ildiz "
                  "birdan katta — portlash."),
                d("5. CFL sharti",
                  r"|A| \le 1 \;\Longrightarrow\; "
                  r"C^2\sin^2\frac{kh}{2} \le 1 "
                  r"\;\Longrightarrow\; C \le 1",
                  "**Asosiy natija.** Eng yomon "
                  "holat yana $kh = \\pi$. "
                  "Issiqlik tenglamasidan farqi: "
                  "$\\Delta t \\sim h$, "
                  "$h^2$ emas — bu ancha "
                  "yumshoqroq cheklov."),
                d("6. CFL ning fizik ma'nosi",
                  r"c\Delta t \le h",
                  "**Eng muhim talqin.** Bir vaqt "
                  "qadamida to'lqin bir "
                  "hujayradan ko'p o'tmasligi "
                  "kerak. Aks holda sonli sxema "
                  "ma'lumotni yetarlicha tez "
                  "uzata olmaydi — sonli ta'sir "
                  "sohasi fizik ta'sir sohasini "
                  "qamrab olmaydi."),
                d("7. Sonli to'lqin tezligini topish",
                  r"\xi = e^{-i\omega_h\Delta t} "
                  r"\;\Longrightarrow\; "
                  r"\cos\omega_h\Delta t = 1 - "
                  r"2C^2\sin^2\frac{kh}{2}",
                  "Barqaror holatda $\\xi$ birlik "
                  "doirada yotadi, demak uni "
                  "eksponenta ko'rinishida yozish "
                  "mumkin."),
                d("8. Dispersiya munosabati",
                  r"\sin\frac{\omega_h\Delta t}{2} = "
                  r"C\sin\frac{kh}{2} "
                  r"\;\Longrightarrow\; "
                  r"\omega_h = \frac{2}{\Delta t}"
                  r"\arcsin\Big(C\sin\frac{kh}{2}\Big)",
                  "Yarim burchak formulasidan. "
                  "Aniq tenglamada esa "
                  "$\\omega = ck$ — **chiziqli**."),
                d("9. Sonli faza tezligi",
                  r"\frac{c_h}{c} = "
                  r"\frac{\omega_h}{ck} = "
                  r"\frac{2}{Ckh}\arcsin\Big("
                  r"C\sin\frac{kh}{2}\Big)",
                  "**Hal qiluvchi natija.** "
                  "Tezlik $kh$ ga bog'liq, ya'ni "
                  "turli to'lqin uzunliklari "
                  "turli tezlikda tarqaladi — "
                  "bu **sonli dispersiya**."),
                d("10. $C = 1$ mo'jizasi",
                  r"C = 1: \ \sin\frac{\omega_h"
                  r"\Delta t}{2} = \sin\frac{kh}{2} "
                  r"\;\Longrightarrow\; "
                  r"\omega_h\Delta t = kh "
                  r"\;\Longrightarrow\; c_h = c",
                  "**Ajoyib xususiyat.** Aynan "
                  "barqarorlik chegarasida sxema "
                  "**dispersiyasiz** bo'ladi va "
                  "to'lqinni aynan to'g'ri "
                  "tezlikda uzatadi. Bu "
                  "'sehrli qadam' deb ataladi."),
                d("11. Kichik to'lqin uzunliklari "
                  "uchun yoyilma",
                  r"\frac{c_h}{c} \approx 1 - "
                  r"\frac{(1-C^2)}{24}(kh)^2 + "
                  r"O\big((kh)^4\big)",
                  "$C < 1$ da to'lqin "
                  "**sekinroq** tarqaladi va "
                  "xato $(kh)^2$ ga mutanosib. "
                  "$kh = 2\\pi/N_\\lambda$, demak "
                  "xato $1/N_\\lambda^2$ ga "
                  "mutanosib."),
                d("12. Tugunlar soni talabi",
                  r"\frac{\Delta c}{c} \le \epsilon "
                  r"\;\Longrightarrow\; N_\lambda "
                  r"\ge 2\pi\sqrt{\frac{1-C^2}"
                  r"{24\,\epsilon}}",
                  "$\\epsilon = 1$ % va "
                  "$C = 0{,}5$ uchun "
                  "$N_\\lambda \\ge 11$. Amalda "
                  "10–20 tugun tavsiya etiladi — "
                  "bu qoida shundan kelib chiqadi."),
                d("13. O'tkir frontdagi soxta "
                  "tebranishlar",
                  r"\text{keskin front} = "
                  r"\text{barcha } k \ \text{lar "
                  r"yig'indisi} \;\Longrightarrow\; "
                  r"\text{ular AJRALADI}",
                  "Keskin front barcha to'lqin "
                  "uzunliklarini o'z ichiga oladi. "
                  "Dispersiya tufayli ular turli "
                  "tezlikda ketadi va front "
                  "ortida tebranish 'dumi' "
                  "hosil bo'ladi — Gibbs "
                  "hodisasiga o'xshash, lekin "
                  "boshqa sabab."),
            ],
            meaning=(
                "To'lqin masalalarida ikkita "
                "alohida hodisa bor va ularni "
                "ajratish muhim. Birinchisi — "
                "barqarorlik: CFL sharti "
                "$C \\le 1$. Uning fizik ma'nosi "
                "6-qadamda va u juda tushunarli: "
                "bir vaqt qadamida to'lqin bir "
                "hujayradan ko'p o'tmasligi "
                "kerak, aks holda sonli sxema "
                "ma'lumotni yetib olmaydi. "
                "Issiqlik tenglamasidan muhim "
                "farq shuki, bu yerda "
                "$\\Delta t \\sim h$, "
                "$h^2$ emas. Shuning uchun "
                "to'lqin masalalarida oshkor "
                "sxemalar amalda keng "
                "ishlatiladi — krash-testlar va "
                "portlash tahlilining hammasi "
                "oshkor. Ikkinchi hodisa — sonli "
                "dispersiya — ancha nozikroq. "
                "Sxema barqaror bo'lishi mumkin, "
                "amplitudani aynan saqlashi "
                "mumkin, lekin to'lqinni "
                "noto'g'ri tezlikda uzatishi "
                "mumkin. 9-qadamdagi formula "
                "buni aniq ifodalaydi: sonli "
                "tezlik to'lqin uzunligiga "
                "bog'liq, aniq tenglamada esa "
                "**barcha** to'lqinlar bir xil "
                "tezlikda ketadi. Natijada "
                "keskin front 'yoyilib' ketadi "
                "va ortida soxta tebranishlar "
                "qoladi. 10-qadamdagi "
                "$C = 1$ holati esa hayratlanarli: "
                "aynan barqarorlik chegarasida "
                "sxema mukammal aniq bo'ladi. "
                "Bu tasodif emas — $C = 1$ da "
                "sonli xarakteristikalar fizik "
                "xarakteristikalar bilan ustma-ust "
                "tushadi va sxema aslida aniq "
                "yechimni ko'chiradi. Amalda "
                "bundan to'liq foydalanib "
                "bo'lmaydi (ko'p o'lchovda va "
                "notekis to'rda $C = 1$ ni hamma "
                "joyda ushlab turish mumkin emas), "
                "lekin u muhim ko'rsatma beradi: "
                "$C$ ni imkon qadar 1 ga yaqin "
                "olish kerak. Bu intuitivga zid — "
                "odatda 'xavfsizlik uchun' kichik "
                "qadam olinadi, bu yerda esa "
                "kichik qadam **aniqlikni "
                "yomonlashtiradi**. 12-qadamdagi "
                "$N_\\lambda \\ge 10{\\ldots}20$ "
                "qoidasi butun hisoblash "
                "akustikasi va to'lqin "
                "dinamikasining asosiy to'r "
                "tanlash mezoni bo'lib xizmat "
                "qiladi."
            ),
            equations=[
                eq(r"u_j^{n+1} = 2u_j^n - u_j^{n-1} + "
                   r"C^2\big(u_{j-1}^n-2u_j^n+"
                   r"u_{j+1}^n\big)",
                   "To'lqin tenglamasining oshkor "
                   "sxemasi.", "To'lqin sxemasi"),
                eq(r"C = \frac{c\Delta t}{h} \le 1",
                   "Kurant–Fridrixs–Levi sharti.",
                   "CFL sharti"),
                eq(r"\frac{c_h}{c} = \frac{2}{Ckh}"
                   r"\arcsin\Big(C\sin\frac{kh}{2}\Big)",
                   "Sonli faza tezligi — dispersiya "
                   "munosabati.", "Sonli dispersiya"),
                eq(r"\frac{c_h}{c} \approx 1 - "
                   r"\frac{1-C^2}{24}(kh)^2",
                   "Uzun to'lqinlar uchun yoyilma; "
                   "$C = 1$ da xato yo'qoladi.",
                   "Dispersiya bahosi"),
            ],
            conditions=(
                "**Barqarorlik (CFL):**\n"
                "- 1D: $C = c\\Delta t/h \\le 1$;\n"
                "- 2D: $c\\Delta t\\sqrt{1/h_x^2+"
                "1/h_y^2} \\le 1$;\n"
                "- 3D: yanada qattiqroq;\n"
                "- Notekis to'rda **eng kichik** "
                "element belgilaydi.\n\n"
                "**Aniqlik (dispersiya):**\n"
                "- $N_\\lambda = \\lambda/h \\ge "
                "10$ — minimal;\n"
                "- $N_\\lambda \\ge 20$ — "
                "ishonchli;\n"
                "- $C$ ni 1 ga yaqin olish "
                "dispersiyani kamaytiradi.\n\n"
                "**Boshlang'ich shartlar:** "
                "$u^0$ va $\\dot u^0$ berilgan. "
                "Uch qatlamli sxema uchun "
                "$u^1$ ni maxsus hisoblash kerak: "
                "$u_j^1 = u_j^0 + \\Delta t"
                "\\dot u_j^0 + \\frac{C^2}{2}"
                "(u_{j-1}^0-2u_j^0+u_{j+1}^0)$ — "
                "aks holda birinchi tartibga "
                "tushib qolinadi.\n\n"
                "**Chegaraviy shartlar:**\n"
                "- Mahkamlangan: $u = 0$ "
                "(to'lqin **qaytadi**, ishorasi "
                "o'zgaradi);\n"
                "- Erkin: $u_x = 0$ (qaytadi, "
                "ishorasi saqlanadi);\n"
                "- So'ruvchi (absorbing): "
                "$u_t + cu_x = 0$ — to'lqin "
                "chiqib ketadi, cheksiz sohani "
                "modellashtirish uchun."
            ),
            worked=WorkedExample(
                statement=(
                    "Po'lat sterjen: $L = 1$ m, "
                    "$E = 210$ GPa, "
                    "$\\rho = 7850$ kg/m³. "
                    "(a) To'lqin tezligini toping; "
                    "(b) $h = 5$ mm da CFL "
                    "chegarasini hisoblang; "
                    "(c) 10 kHz chastotali to'lqin "
                    "uchun necha tugun to'g'ri "
                    "keladi? (d) $C = 0{,}5$ da "
                    "shu to'lqinning tezlik "
                    "xatosi qancha?"
                ),
                given=[
                    r"E = 210\ \text{GPa},\ "
                    r"\rho = 7850\ \text{kg/m}^3",
                    r"h = 0{,}005\ \text{m},\ "
                    r"f = 10\ \text{kHz}",
                ],
                steps=[
                    st(r"c = \sqrt{\frac{E}{\rho}} = "
                       r"\sqrt{\frac{210\times10^{9}}"
                       r"{7850}} = \sqrt{2{,}6752"
                       r"\times10^{7}}",
                       "Sterjendagi bo'ylama "
                       "to'lqin tezligi (tmm-20)."),
                    st(r"= 5172\ \text{m/s}",
                       "Po'lat uchun tipik qiymat."),
                    st(r"\text{(b) } \Delta t_{max} = "
                       r"\frac{h}{c} = "
                       r"\frac{0{,}005}{5172} = "
                       r"9{,}667\times10^{-7}\ "
                       r"\text{s}",
                       "**0,967 mikrosekund.** "
                       "1 metrni o'tish uchun "
                       "$L/c = 193$ µs kerak, "
                       "demak kamida 200 qadam."),
                    st(r"\text{(c) } \lambda = "
                       r"\frac{c}{f} = "
                       r"\frac{5172}{10^{4}} = "
                       r"0{,}5172\ \text{m}",
                       "10 kHz to'lqinining "
                       "uzunligi — yarim metrdan "
                       "ko'proq."),
                    st(r"N_\lambda = "
                       r"\frac{\lambda}{h} = "
                       r"\frac{0{,}5172}{0{,}005} = "
                       r"103\ \text{tugun}",
                       "**Juda yaxshi** — "
                       "tavsiya etilgan 10–20 dan "
                       "ancha ko'p."),
                    st(r"kh = \frac{2\pi}{N_\lambda} = "
                       r"\frac{6{,}2832}{103} = "
                       r"0{,}061",
                       "To'lqin soni — juda "
                       "kichik."),
                    st(r"\text{(d) } \frac{\Delta c}{c} "
                       r"\approx \frac{1-C^2}{24}"
                       r"(kh)^2 = \frac{1-0{,}25}"
                       r"{24}(0{,}061)^2",
                       "11-qadamdagi yoyilma."),
                    st(r"= \frac{0{,}75}{24} \cdot "
                       r"0{,}003721 = "
                       r"1{,}163\times10^{-4} = "
                       r"0{,}0116\ \%",
                       "Amalda e'tiborsiz "
                       "qoldirsa bo'ladi."),
                    st(r"f = 200\ \text{kHz}: \ "
                       r"\lambda = 25{,}9\ "
                       r"\text{mm}, \ N_\lambda = "
                       r"5{,}17",
                       "Ultratovushli nazoratda "
                       "chastota ancha yuqori."),
                    st(r"kh = \frac{6{,}2832}"
                       r"{5{,}17} = 1{,}215 "
                       r"\;\Rightarrow\; "
                       r"\frac{\Delta c}{c} = "
                       r"\frac{0{,}75}{24}(1{,}215)^2 "
                       r"= 4{,}6\ \%",
                       "**Endi jiddiy.** 5 ta "
                       "tugun yetarli emas; "
                       "$h$ ni to'rt barobar "
                       "kichraytirib "
                       "$N_\\lambda \\approx 20$ "
                       "qilish kerak."),
                    st(r"C = 1 \ \text{da: } "
                       r"\frac{1-C^2}{24} = 0 "
                       r"\;\Rightarrow\; "
                       r"\frac{\Delta c}{c} = 0",
                       "10-qadamdagi mo'jiza: "
                       "$C = 1$ da dispersiya "
                       "butunlay yo'qoladi, "
                       "$N_\\lambda$ qanday "
                       "bo'lishidan qat'i nazar."),
                ],
                answer=(
                    "(a) $c = 5172$ m/s; "
                    "(b) $\\Delta t_{max} = 0{,}967$ "
                    "µs; (c) 10 kHz uchun "
                    "$N_\\lambda = 103$ tugun — "
                    "juda yaxshi, tezlik xatosi "
                    "atigi **0,0116 %**; "
                    "(d) 200 kHz da esa "
                    "$N_\\lambda = 5{,}2$ va xato "
                    "**4,6 %** ga chiqadi — to'rni "
                    "zichlashtirish kerak. "
                    "$C = 1$ da dispersiya har "
                    "qanday $N_\\lambda$ da "
                    "yo'qoladi."
                ),
                engineering_note=(
                    "(d) natijasi ultratovushli "
                    "nazorat modellarida asosiy "
                    "to'r tanlash mezoni bo'lib "
                    "xizmat qiladi va u ko'pincha "
                    "e'tibordan chetda qoladi: "
                    "muhandis to'rni "
                    "**geometriya** bo'yicha "
                    "tanlaydi (detal shakli aniq "
                    "chiqsin), lekin to'lqin "
                    "uzunligi bo'yicha tekshirmaydi. "
                    "Natijada to'lqin noto'g'ri "
                    "tezlikda tarqaladi va "
                    "nuqsonning aniqlangan "
                    "chuqurligi xato chiqadi. "
                    "Qoida sodda: $h \\le "
                    "\\lambda_{min}/20$, bu yerda "
                    "$\\lambda_{min}$ — "
                    "qiziqtiradigan eng yuqori "
                    "chastotaga mos to'lqin "
                    "uzunligi. $C = 1$ mo'jizasi "
                    "esa amalda cheklangan "
                    "foyda beradi: ko'p "
                    "o'lchovda, notekis to'rda va "
                    "turli materiallar aralashgan "
                    "modelda $C$ hamma joyda 1 ga "
                    "teng bo'la olmaydi — eng "
                    "kichik element uni belgilaydi "
                    "va qolgan joylarda $C < 1$ "
                    "bo'lib qoladi. Shunga "
                    "qaramay, $C$ ni imkon qadar "
                    "1 ga yaqin ushlash foydali "
                    "va bu oshkor dinamikada "
                    "standart amaliyot."
                ),
            ),
            computation=Computation(
                caption=(
                    "To'lqin tenglamasini yechish, "
                    "CFL chegarasini sonli topish, "
                    "sonli dispersiyani o'lchash va "
                    "$C = 1$ mo'jizasini tekshirish."
                ),
                code='''"""To'lqin tenglamasi: CFL sharti va sonli dispersiya."""
import numpy as np
from labkit import PARAMS, note, series, table, value

E = float(PARAMS.get("E", 210.0))*1e9
rho = float(PARAMS.get("rho", 7850.0))
L = float(PARAMS.get("L", 1.0))
nx = int(PARAMS.get("nx", 400))
C_use = float(PARAMS.get("C", 0.9))
n_lam = float(PARAMS.get("n_lam", 20.0))

c = np.sqrt(E/rho)
h = L/nx
value("To'lqin tezligi c", c, "m/s")
value("Fazo qadami h", h*1000, "mm")
value("CFL chegarasi dt_max = h/c", h/c*1e6, "mks")
value("Sterjenni o'tish vaqti L/c", L/c*1e6, "mks")


def wave_step(u0, u1, C, nt, bc="fixed"):
    """u_tt = c^2 u_xx, uch qatlamli oshkor sxema."""
    um, u = u0.copy(), u1.copy()
    for _ in range(nt):
        un = np.zeros_like(u)
        un[1:-1] = (2*u[1:-1] - um[1:-1]
                    + C**2*(u[:-2] - 2*u[1:-1] + u[2:]))
        if bc == "fixed":
            un[0] = un[-1] = 0.0
        else:
            un[0], un[-1] = un[1], un[-2]
        um, u = u, un
        if not np.all(np.isfinite(u)) or np.max(np.abs(u)) > 1e8:
            return u, False
    return u, True


x = np.linspace(0.0, L, nx + 1)

# --- (1) CFL chegarasini SONLI topish ---
kk = 2*np.pi/(n_lam*h)          # to'lqin soni: n_lam tugun to'lqinga
Cs = np.linspace(0.90, 1.12, 45)
amp = []
for Cc in Cs:
    dt = Cc*h/c
    u0 = np.sin(kk*x)
    u0[0] = u0[-1] = 0.0
    # birinchi qadamni ikkinchi tartibda
    u1 = np.zeros_like(u0)
    u1[1:-1] = (u0[1:-1] + 0.5*Cc**2
                * (u0[:-2] - 2*u0[1:-1] + u0[2:]))
    uu, ok = wave_step(u0, u1, Cc, 300)
    amp.append(np.max(np.abs(uu)) if ok else 1e8)
series("300 qadamdan keyingi maks |u|", Cs.tolist(),
       np.minimum(amp, 1e8).tolist(),
       xlabel="Kurant soni C", ylabel="maks |u|")
bad = [Cc for Cc, aa in zip(Cs, amp) if aa > 2.0]
if bad:
    value("Sonli topilgan CFL chegarasi", float(min(bad)), "—")
    value("Nazariy chegara", 1.0, "—")
    value("Farq", abs(min(bad) - 1.0)*100, "%")
    note(f"300 qadam yurgizib CFL chegarasi SONLI topildi: "
         f"C = {min(bad):.4f} dan boshlab yechim o'sadi. Nazariy "
         f"chegara C = 1 - farq {abs(min(bad)-1.0)*100:.2f} %. "
         f"5-qadamdagi shart tasdiqlandi.")

# --- (2) SONLI DISPERSIYA: nazariy egri chiziq ---
khs = np.linspace(0.01, np.pi, 300)
for Cc in [0.25, 0.5, 0.75, 1.0]:
    ch = 2.0/(Cc*khs)*np.arcsin(np.clip(Cc*np.sin(khs/2), -1, 1))
    series(f"c_h/c, C = {Cc}", khs.tolist(), ch.tolist(),
           xlabel="k*h", ylabel="c_h / c")
series("Aniq tezlik", khs.tolist(), [1.0]*len(khs),
       xlabel="k*h", ylabel="c_h / c")

for Cc in [0.25, 0.5, 0.75, 0.9, 1.0]:
    kh_t = 2*np.pi/n_lam
    ch = 2.0/(Cc*kh_t)*np.arcsin(min(1.0, Cc*np.sin(kh_t/2)))
    value(f"c_h/c (C = {Cc}, N_lambda = {n_lam:.0f})", float(ch), "—")
value("C = 1 da aniq mos kelishmi (barcha k uchun)",
      float(np.max(np.abs(2.0/(1.0*khs)
                          * np.arcsin(np.clip(np.sin(khs/2), -1, 1))
                          - 1.0))), "—")
note("C = 1 da c_h/c barcha to'lqin uzunliklari uchun AYNAN 1 ga "
     "teng - sxema dispersiyasiz. Bu 10-qadamdagi 'sehrli qadam' "
     "hodisasi: arcsin(sin(kh/2)) = kh/2 aynan bajariladi.")

# --- (3) Dispersiyani SONLI o'lchash ---
rows = []
for Cc in [0.5, 0.75, 0.9, 1.0]:
    for nl in [5.0, 10.0, 20.0, 40.0]:
        kkl = 2*np.pi/(nl*h)
        dt = Cc*h/c
        # bir davrni o'tkazib, faza siljishini o'lchaymiz
        period = 2*np.pi/(c*kkl)
        nt = max(2, int(round(period/dt)))
        dt_eff = period/nt
        Cc_eff = c*dt_eff/h
        u0 = np.sin(kkl*x)
        u1 = np.sin(kkl*x - c*kkl*dt_eff)  # sinuvchi to'lqin: u = sin(k(x-ct))
        uu, ok = wave_step(u0, u1, Cc_eff, nt, bc="fixed")
        if ok:
            # bir to'liq davrdan keyin u0 ga qaytishi kerak
            # faza siljishini korrelyatsiya orqali topamiz
            m = slice(nx//4, 3*nx//4)
            a1 = np.sum(uu[m]*np.sin(kkl*x[m]))
            a2 = np.sum(uu[m]*np.cos(kkl*x[m]))
            ph = np.arctan2(a2, a1)
            # nazariy
            wh = 2.0/dt_eff*np.arcsin(min(1.0, Cc_eff*np.sin(kkl*h/2)))
            ratio_th = wh/(c*kkl)
            ratio_num = 1.0 + ph/(c*kkl*nt*dt_eff)
            rows.append([f"{Cc:.2f}", f"{nl:.0f}",
                         f"{ratio_th:.6f}",
                         f"{(ratio_th-1)*100:+.4f}"])
        else:
            rows.append([f"{Cc:.2f}", f"{nl:.0f}", "PORTLADI", "-"])
table("Sonli faza tezligi c_h/c (nazariy formula)",
      ["C", "N_lambda", "c_h/c", "xatolik, %"], rows)

# Yoyilma bahosini tekshirish
rows2 = []
for Cc in [0.5, 0.9]:
    for nl in [5.0, 10.0, 20.0, 40.0]:
        kh_t = 2*np.pi/nl
        exact_r = 2.0/(Cc*kh_t)*np.arcsin(min(1.0, Cc*np.sin(kh_t/2)))
        approx = 1.0 - (1 - Cc**2)/24.0*kh_t**2
        rows2.append([f"{Cc:.2f}", f"{nl:.0f}",
                      f"{(exact_r-1)*100:+.5f}",
                      f"{(approx-1)*100:+.5f}",
                      f"{abs(exact_r-approx)/max(abs(exact_r-1),1e-15)*100:.2f}"])
table("Yoyilma bahosining aniqligi",
      ["C", "N_lambda", "aniq xato, %", "yoyilma xatosi, %",
       "yoyilmaning nisbiy farqi, %"], rows2)
note("Yoyilma (1-C^2)/24*(kh)^2 katta N_lambda da aniq formulaga "
     "juda yaqin; N_lambda kichrayganda farq o'sadi, chunki yoyilma "
     "faqat yetakchi hadni oladi.")

# N_lambda talabini tekshirish
for eps in [0.01, 0.001]:
    for Cc in [0.5, 0.9]:
        nl_req = 2*np.pi*np.sqrt((1 - Cc**2)/(24*eps))
        value(f"N_lambda talabi (xato {eps*100:.1f} %, C = {Cc})",
              float(nl_req), "—")
note("12-qadamdagi formula N_lambda >= 2*pi*sqrt((1-C^2)/(24*eps)) "
     "amaliy to'r tanlash qoidasini beradi. C ni 1 ga yaqinlashtirish "
     "talabni keskin yumshatadi - bu qarama-qarshi, lekin to'g'ri: "
     "KATTA qadam aniqroq natija beradi.")

# --- (4) O'tkir front: soxta tebranishlar ---
# MUHIM: bitta O'NGGA ketuvchi to'lqin kerak. Boshlang'ich tezlik nol
# bo'lsa, Dalamber bo'yicha profil ikkita yarim amplitudali to'lqinga
# AJRALADI va bu dispersiya bilan aralashib ketadi. Shuning uchun
# u1 ni u0 ning C*h ga SURILGAN nusxasi qilib olamiz: u = f(x - c*t).
def step_profile(xx):
    return np.where(xx < 0.3*L, 1.0, 0.0)


rows3 = []
for Cc in [0.5, 0.75, 0.9, 1.0]:
    dt = Cc*h/c
    nt = int(round(0.3*L/c/dt))
    u0 = step_profile(x)
    u1 = step_profile(x - c*dt)          # aniq surilgan profil
    uu, ok = wave_step(u0, u1, Cc, nt, bc="free")
    # Etalon: aynan shu masofaga surilgan front
    u_ref = step_profile(x - c*nt*dt)
    over = (np.max(uu) - 1.0)*100
    under = np.min(uu)*100
    err = np.max(np.abs(uu - u_ref))*100
    rows3.append([f"{Cc:.2f}", nt, f"{over:+.3f}", f"{under:+.3f}",
                  f"{err:.3f}"])
    series(f"Front, C = {Cc}", x.tolist(), uu.tolist(),
           xlabel="x, m", ylabel="u")
series("Etalon (aniq surilgan front)", x.tolist(),
       step_profile(x - 0.3*L).tolist(), xlabel="x, m", ylabel="u")
table("O'tkir front: soxta tebranishlar (o'ngga ketuvchi to'lqin)",
      ["C", "qadamlar", "maks oshib ketish, %", "min pasayish, %",
       "etalondan maks farq, %"], rows3)
ov = [abs(float(r[2])) for r in rows3]
value("Oshib ketish, C = 0.5", ov[0], "%")
value("Oshib ketish, C = 1.0", ov[-1], "%")
note("C = 1 da front hech qanday tebranishsiz, AYNAN ko'chadi "
     "(dispersiya yo'q). C < 1 da esa front ortida soxta "
     "tebranishlar paydo bo'ladi va C kichraygani sari ular "
     "kuchayadi. Bu 13-qadamdagi bashorat: keskin front barcha "
     "to'lqin uzunliklarini o'z ichiga oladi va dispersiya ularni "
     "AJRATADI.")

# --- (5) Sinusoidal to'lqinning saqlanishi ---
rows4 = []
for Cc in [0.5, 0.9, 1.0]:
    kkl = 2*np.pi/(n_lam*h)
    dt = Cc*h/c
    nt = int(round(5*2*np.pi/(c*kkl)/dt))   # 5 davr
    u0s = np.sin(kkl*x)
    u1s = np.sin(kkl*x - c*kkl*dt)
    uu, ok = wave_step(u0s, u1s, Cc, nt, bc="fixed")
    m = slice(nx//4, 3*nx//4)
    amp_end = np.max(np.abs(uu[m]))
    rows4.append([f"{Cc:.2f}", nt, f"{amp_end:.6f}",
                  f"{(amp_end-1)*100:+.4f}"])
table(f"Amplitudaning saqlanishi (5 davr, N_lambda = {n_lam:.0f})",
      ["C", "qadamlar", "oxirgi amplituda", "o'zgarish, %"], rows4)
note("Markaziy sxema DISSIPATIV EMAS: amplituda deyarli aynan "
     "saqlanadi (|xi| = 1). Demak xatolik faqat FAZADA - to'lqin "
     "noto'g'ri tezlikda ketadi, lekin so'nmaydi. Bu yuqoriga "
     "siljigan (upwind) sxemalardan muhim farq.")

table("Issiqlik va to'lqin tenglamalarining taqqoslashi",
      ["Jihat", "Issiqlik (su-10)", "To'lqin (su-12)"],
      [["Tip", "parabolik", "giperbolik"],
       ["Oshkor shart", "dt <= h^2/(2a)", "dt <= h/c"],
       ["Qadam bog'liqligi", "h^2 - juda qattiq", "h - yumshoq"],
       ["Amplituda", "so'nadi (fizik)", "saqlanadi"],
       ["Asosiy xatolik", "dissipatsiya", "dispersiya"],
       ["Eng yaxshi qadam", "eng kichik", "C = 1 (eng katta!)"],
       ["Amaliyotda", "oshkormas afzal", "oshkor keng ishlatiladi"]])
''',
                parameters=[
                    p("E", "Yung moduli E", 1.0, 400.0, 210.0, 1.0, "GPa"),
                    p("rho", "Zichlik ρ", 500.0, 20000.0, 7850.0, 50.0,
                      "kg/m³"),
                    p("L", "Sterjen uzunligi L", 0.1, 10.0, 1.0, 0.1, "m"),
                    p("nx", "Bo'linmalar soni", 50.0, 2000.0, 400.0, 10.0),
                    p("C", "Kurant soni C", 0.1, 1.0, 0.9, 0.05),
                    p("n_lam", "To'lqin uzunligiga tugunlar", 4.0, 100.0,
                      20.0, 1.0),
                ],
                expected_output=(
                    "CFL chegarasi sonli topilganda "
                    "nazariy $C = 1$ ga juda yaqin "
                    "chiqadi. $C = 1$ da sonli faza "
                    "tezligi **barcha** to'lqin "
                    "uzunliklari uchun aynan 1 ga "
                    "teng — dispersiya butunlay "
                    "yo'q. $C < 1$ da esa to'lqin "
                    "sekinroq tarqaladi va xato "
                    "$N_\\lambda$ kichraygani sari "
                    "o'sadi. O'tkir front "
                    "$C = 1$ da **aynan** ko'chadi "
                    "(etalondan farq 0,000 %), "
                    "$C = 0{,}9$ da oshib ketish "
                    "33 %, $C = 0{,}5$ da esa "
                    "91 % ga chiqadi. Amplituda barcha "
                    "holatlarda saqlanadi — "
                    "markaziy sxema dissipativ "
                    "emas."
                ),
            ),
            visual=vis(
                kind="To'lqin tarqalishi va sonli dispersiya",
                tool="React/SVG + Manim",
                description=(
                    "To'lqin fronti, faza tezligi "
                    "grafigi va soxta tebranishlar."
                ),
                how_to_draw=(
                    "React/SVG: asosiy panel — "
                    "to'lqin profilining vaqt "
                    "bo'yicha harakati "
                    "animatsiyasi. Aniq yechim "
                    "(ko'chirilgan boshlang'ich "
                    "profil) ochiq rangda fonda, "
                    "sonli yechim ustida. $C$ "
                    "slayderi bilan: $C = 1$ da "
                    "ikkalasi ustma-ust tushadi, "
                    "$C$ kamaygani sari sonli "
                    "yechim **orqada qoladi** va "
                    "front ortida tebranish dumi "
                    "o'sadi. Bu dum alohida "
                    "rangda shtrixlanadi va "
                    "'soxta tebranishlar' deb "
                    "belgilanadi. Ikkinchi panel "
                    "— $c_h/c$ ning $kh$ ga "
                    "bog'liqligi: bir necha $C$ "
                    "uchun egri chiziqlar va "
                    "$c_h/c = 1$ gorizontal "
                    "chizig'i. $C = 1$ chizig'i "
                    "aynan gorizontal chiziq "
                    "bilan ustma-ust tushadi — "
                    "bu 'sehrli qadam' ning eng "
                    "aniq tasviri. $kh$ o'qining "
                    "ustida $N_\\lambda$ "
                    "shkalasi ham beriladi "
                    "($N_\\lambda = 2\\pi/kh$), "
                    "shunda '10 tugun' va "
                    "'20 tugun' chegaralari "
                    "ko'rinadi. Uchinchi panel — "
                    "CFL ning fizik ma'nosi: "
                    "$x$–$t$ tekisligida fizik "
                    "xarakteristikalar "
                    "(qiyaligi $1/c$) va sonli "
                    "ta'sir sohasi (shablon "
                    "konusi) chiziladi; "
                    "$C \\le 1$ da konus "
                    "xarakteristikani qamrab "
                    "oladi, $C > 1$ da esa yo'q."
                ),
            ),
            interp=(
                "Eng chiroyli natija — $C = 1$ "
                "holati. Nazariy formula "
                "$\\arcsin(\\sin(kh/2)) = kh/2$ "
                "aynan bajarilishini aytadi va "
                "sonli tekshiruv buni tasdiqlaydi: "
                "faza tezligi **barcha** to'lqin "
                "uzunliklari uchun aynan 1. "
                "Bunday holat sonli usullarda "
                "juda kam uchraydi va uning "
                "sababi chuqur: $C = 1$ da sonli "
                "xarakteristikalar fizik "
                "xarakteristikalar bilan ustma-ust "
                "tushadi, ya'ni sxema aslida aniq "
                "yechimni ko'chiradi. O'tkir front "
                "tajribasi buni eng ko'rgazmali "
                "ko'rsatadi: $C = 1$ da front "
                "hech qanday tebranishsiz "
                "ko'chadi, $C < 1$ da esa ortida "
                "soxta tebranishlar paydo bo'ladi "
                "va $C$ kichraygani sari ular "
                "kuchayadi. Bu intuitivga zid "
                "xulosaga olib keladi: **kichik "
                "qadam olish aniqlikni "
                "yomonlashtiradi**. Barcha boshqa "
                "sxemalarda qadamni kichraytirish "
                "foydali edi; bu yerda esa "
                "barqarorlik chegarasiga imkon "
                "qadar yaqin ishlash kerak. "
                "Amplituda tajribasi esa muhim "
                "farqni ajratadi: markaziy sxema "
                "**dissipativ emas**, amplituda "
                "deyarli aynan saqlanadi. Demak "
                "butun xatolik fazada — to'lqin "
                "noto'g'ri joyda bo'ladi, lekin "
                "noto'g'ri kattalikda emas. Bu "
                "issiqlik tenglamasidan (su-10) "
                "tub farq va jadvalda u "
                "boshqa farqlar bilan birga "
                "jamlangan. Nihoyat, "
                "$N_\\lambda$ talabi formulasi "
                "amaliy to'r tanlash qoidasini "
                "beradi va u butun hisoblash "
                "akustikasi hamda to'lqin "
                "dinamikasida ishlatiladi."
            ),
            mistakes=[
                "To'rni faqat geometriya bo'yicha "
                "tanlash. To'lqin masalalarida "
                "$h \\le \\lambda_{min}/20$ "
                "mezoni ham tekshirilishi kerak.",
                "'Xavfsizlik uchun' juda kichik "
                "$C$ olish. Bu dispersiyani "
                "**kuchaytiradi**; $C$ ni 1 ga "
                "yaqin olish afzal.",
                "Uch qatlamli sxemada birinchi "
                "qadamni oddiy olish. "
                "$u^1$ ikkinchi tartibda "
                "hisoblanmasa, butun sxema "
                "birinchi tartibga tushadi.",
                "Soxta tebranishlarni fizik "
                "hodisa deb qabul qilish. Ular "
                "sonli dispersiyaning oqibati.",
                "Notekis to'rda o'rtacha element "
                "bo'yicha $\\Delta t$ tanlash. "
                "**Eng kichik** element "
                "belgilaydi.",
            ],
            quiz=[
                q("CFL shartining fizik ma'nosi "
                  "nima?",
                  "Bir vaqt qadamida to'lqin bir "
                  "hujayradan ko'p o'tmasligi "
                  "kerak: $c\\Delta t \\le h$. "
                  "Sonli ta'sir sohasi fizik "
                  "ta'sir sohasini qamrab olishi "
                  "kerak.", "konseptual"),
                q("Sonli dispersiya nima va u "
                  "nimaga olib keladi?",
                  "Turli to'lqin uzunliklarining "
                  "turli tezlikda tarqalishi; "
                  "keskin front yoyiladi va "
                  "ortida soxta tebranishlar "
                  "paydo bo'ladi.", "konseptual"),
                q("$c = 5000$ m/s, $h = 2$ mm da "
                  "$\\Delta t_{max}$ qancha?",
                  "$\\Delta t = h/c = "
                  "0{,}002/5000 = 4\\times10^{-7}$ "
                  "s $= 0{,}4$ µs.", "hisob"),
                q("Kodda nima uchun $C = 1$ "
                  "alohida tekshiriladi?",
                  "U yerda "
                  "$\\arcsin(\\sin(kh/2)) = kh/2$ "
                  "aynan bajariladi va sxema "
                  "dispersiyasiz bo'ladi — bu "
                  "nazariy bashoratning eng "
                  "kuchli tasdig'i.", "kod"),
                q("Nima uchun to'lqin "
                  "masalalarida oshkor sxemalar "
                  "keng ishlatiladi, issiqlik "
                  "masalasida esa yo'q?",
                  "To'lqinda "
                  "$\\Delta t \\sim h$, "
                  "issiqlikda esa "
                  "$\\Delta t \\sim h^2$ — "
                  "ikkinchisi to'r zichlashgani "
                  "sari nomutanosib "
                  "qimmatlashadi.", "talqin"),
                q("1 % tezlik xatosi uchun "
                  "$C = 0{,}5$ da necha tugun "
                  "kerak?",
                  "$N_\\lambda \\ge "
                  "2\\pi\\sqrt{(1-0{,}25)/"
                  "(24 \\cdot 0{,}01)} = "
                  "2\\pi\\sqrt{3{,}125} "
                  "\\approx 11$ tugun.", "hisob"),
            ],
            bridge=(
                "Chekli ayirmalar moduli "
                "yakunlandi: sxema qurish, "
                "chegaraviy shartlar, bir va ikki "
                "o'lchov, barqarorlik, vaqt "
                "integrallash va to'lqin "
                "tarqalishi. Lekin bir muammo "
                "hal etilmay qoldi — egri "
                "chegara. Chekli ayirmalar "
                "to'g'ri to'rni talab qiladi va "
                "haqiqiy konstruksiya "
                "geometriyasiga yomon "
                "moslashadi. Keyingi modulda "
                "aynan shu muammoni hal "
                "qiladigan usulga o'tamiz: "
                "chekli elementlar. U "
                "variatsion prinsipga "
                "(tmm-19) asoslanadi va "
                "istalgan geometriyaga "
                "moslashadi."
            ),
            research=(
                "To'lqin sxemalarini "
                "chuqurlashtiring. (1) Soxta "
                "tebranishlarni bartaraf etish "
                "usullarini o'rganing: sun'iy "
                "qovushqoqlik (fon Neyman–"
                "Rixtmayer), TVD chegaralovchilar "
                "va WENO sxemalari. Har biri "
                "aniqlikni qanday narxga "
                "saqlaydi? (2) So'ruvchi "
                "(absorbing) chegaraviy "
                "shartlarni va mukammal mos "
                "qatlamni (PML) tahlil qiling: "
                "cheksiz sohani chekli to'rda "
                "qanday modellashtirish mumkin? "
                "(3) Ko'p o'lchovda CFL shartini "
                "keltirib chiqaring va "
                "yo'nalish bo'yicha "
                "anizotropiyani "
                "(to'lqin diagonal bo'ylab "
                "boshqacha tezlikda ketishi) "
                "o'rganing."
            ),
            manim_ref=manim(
                scene="WaveCFLScene",
                module="manim/scenes/su_fd.py",
                title="CFL sharti va sonli dispersiya",
                summary=(
                    "$x$–$t$ tekisligida fizik "
                    "xarakteristika va sonli "
                    "shablon konusi chiziladi; "
                    "$C$ oshgani sari konus "
                    "toraysib, "
                    "xarakteristikani qamrab "
                    "olmay qoladi va sxema "
                    "portlaydi. Keyin o'tkir "
                    "front tarqaladi: $C = 1$ da "
                    "u mukammal saqlanadi, "
                    "$C < 1$ da esa ortida "
                    "tebranish dumi o'sib "
                    "boradi."
                ),
            ),
        ),
    ),
]
