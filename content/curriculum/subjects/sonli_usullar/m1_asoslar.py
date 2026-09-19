"""SU / 1-modul: Sonli hisoblash asoslari va xatoliklar (su-01 … su-06)."""

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
M = "su-m1"


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
    # ------------------------------------------------------------------ su-01
    Topic(
        id="su-01",
        subject_id=S, module_id=M, order=1,
        title="Hisoblash mexanikasining o'rni: nima uchun sonli usullar kerak",
        description=(
            "Analitik yechimning chegaralari, diskretlashtirish g'oyasi, "
            "sonli yechimning uch manbali xatoligi va hisoblash "
            "mexanikasining umumiy zanjiri."
        ),
        learning_objective=(
            "Analitik yechim qachon mavjud emasligini aniqlash, sonli "
            "yechim zanjirining bosqichlarini nomlash va uchta xatolik "
            "manbasini ajratish."
        ),
        prerequisites=["pq-30", "pq-10", "mq-27"],
        mathematical_core=(
            "Diskretlashtirish: $\\mathcal{L}u = f \\to \\mathbf{K}"
            "\\mathbf{u} = \\mathbf{f}$; umumiy xatolik "
            "$e = e_{model} + e_{diskret} + e_{yaxlitlash}$."
        ),
        engineering_application=(
            "Har qanday zamonaviy muhandislik hisobi: avtomobil "
            "krash-testi, samolyot qanoti, ko'prik, implant, mikroelektron "
            "korpusi — barchasi sonli modelga asoslanadi."
        ),
        computational_component=(
            "Bir xil masalani analitik va sonli yechib, uchta xatolik "
            "manbasini ajratib ko'rsatish."
        ),
        visualization_component=(
            "Diskretlashtirish g'oyasi, to'r zichlashgani sari sonli "
            "yechimning analitik yechimga yaqinlashishi."
        ),
        research_extension=(
            "Hisoblash mexanikasining tarixini o'rganing: 1940-yillardagi "
            "birinchi matritsa usullaridan bugungi HPC gacha. Muri "
            "qonunining hisoblash imkoniyatlariga ta'sirini va "
            "algoritmlardagi yutuqlarning hissasini solishtiring."
        ),
        difficulty="kirish",
        previous_link=(
            "pq-10 da plastina masalasi chekli ayirmalar bilan "
            "yechilgan va yaqinlashish tartibi 2,02 deb o'lchangan "
            "edi; pq-09 da Ritz va Galerkin usullari ishlatildi. "
            "Bular sonli usullarning birinchi uchrashuvi edi — endi "
            "ularni tizimli va qat'iy asosda quramiz."
        ),
        next_topic="su-02",
        estimated_minutes=75,
        tags=["kirish", "diskretlashtirish", "xatolik", "FEM"],
        lesson=_lesson(
            problem=(
                "Oldingi to'rt fanda o'nlab masalani analitik "
                "yechdik. Endi bitta oddiy savolga javob berishga "
                "harakat qilaylik: burchagida teshigi bor, bir "
                "tomoni qovurg'alangan, qalinligi o'zgaruvchan "
                "to'rtburchak plastina bir tekis yuklama ostida "
                "qanchaga og'adi? Navye qatori (pq-07) ishlamaydi — "
                "u to'rt tomoni sharnirli tekis to'rtburchakni "
                "talab qiladi. Levi (pq-08) ham — u ikki tomoni "
                "sharnirli bo'lishini talab qiladi. Ritz (pq-09) "
                "uchun teshikli sohada sinov funksiyasi topish "
                "deyarli imkonsiz. Aniq yechim **mavjud emas** va "
                "u hech qachon topilmaydi ham. Lekin bunday "
                "konstruksiya har kuni loyihalanadi. Qanday qilib?"
            ),
            concepts=[
                c("Diskretlashtirish (discretization)",
                  "Cheksiz o'lchovli uzluksiz masalani chekli "
                  "o'lchovli algebraik masalaga almashtirish; "
                  "barcha sonli usullarning umumiy g'oyasi."),
                c("Hisoblash mexanikasi zanjiri",
                  "Fizik masala → matematik model → diskret model "
                  "→ algebraik tizim → yechim → talqin; har "
                  "bosqichda o'z xatoligi bor."),
                c("Model xatoligi",
                  "Matematik modelning haqiqatdan farqi "
                  "(gipotezalar, materiallar modeli, yuklama "
                  "idealizatsiyasi) — to'rni zichlashtirish bilan "
                  "YO'QOLMAYDI."),
                c("Diskretlashtirish xatoligi",
                  "Uzluksizni diskret bilan almashtirishdan; "
                  "to'r zichlashgani sari kamayadi."),
                c("Yaxlitlash xatoligi",
                  "Chekli razryadli arifmetikadan; to'r "
                  "zichlashgani sari **ortadi**."),
                c("Optimal to'r",
                  "Diskretlashtirish va yaxlitlash xatoliklari "
                  "qarama-qarshi yo'nalishda o'zgargani uchun "
                  "umumiy xatolikning minimumi mavjud."),
            ],
            derivation=[
                d("1. Uzluksiz masala",
                  r"\mathcal{L}\,u(x) = f(x) \ \text{sohada } \Omega, "
                  r"\quad \mathcal{B}\,u = g \ \text{chegarada }"
                  r"\partial\Omega",
                  "$\\mathcal{L}$ — differensial operator "
                  "(masalan $D\\nabla^4$, pq-04), $u$ — noma'lum "
                  "funksiya. Noma'lumlar soni **cheksiz**: har "
                  "bir nuqtada bitta qiymat."),
                d("2. Yechimni chekli bazisda ifodalash",
                  r"u(x) \approx u_h(x) = \sum_{i=1}^{N} u_i\,"
                  r"\varphi_i(x)",
                  "$\\varphi_i$ — oldindan tanlangan bazis "
                  "funksiyalar, $u_i$ — noma'lum sonlar. "
                  "Endi noma'lumlar soni $N$ ta — **chekli**. "
                  "Bu barcha sonli usullarning umumiy qadami."),
                d("3. Usullarning farqi — bazis tanlashda",
                  r"\varphi_i = \begin{cases}"
                  r"\sin\frac{i\pi x}{a} & \text{(qator usullari)}\\"
                  r"\text{mahalliy 'do'ppi'} & \text{(FEM)}\\"
                  r"\delta\text{-tugun} & \text{(chekli ayirmalar)}"
                  r"\end{cases}",
                  "Navye qatori global sinus bazisini, FEM "
                  "mahalliy bo'lakli-ko'phadli bazisni, chekli "
                  "ayirmalar esa tugun qiymatlarini oladi. "
                  "**Mahalliy bazis** FEM ning kuchi: u har "
                  "qanday sohaga moslashadi."),
                d("4. Qoldiqni nolga majburlash",
                  r"R(x) = \mathcal{L}u_h - f \ne 0; \quad "
                  r"\int_\Omega R(x)\,w_j(x)\,d\Omega = 0, "
                  r"\ j = 1\ldots N",
                  "$u_h$ aniq yechim emas, demak qoldiq $R$ "
                  "qoladi. Uni $N$ ta vazn funksiyasiga "
                  "ortogonal qilamiz — $N$ ta tenglama hosil "
                  "bo'ladi (og'irlangan qoldiqlar usuli)."),
                d("5. Algebraik tizim",
                  r"\mathbf{K}\mathbf{u} = \mathbf{f}, \quad "
                  r"K_{ji} = \int_\Omega w_j\,\mathcal{L}"
                  r"\varphi_i\,d\Omega",
                  "**Hal qiluvchi o'tish.** Differensial "
                  "tenglama chiziqli algebraik tizimga "
                  "aylandi. Kompyuter aynan shuni yecha oladi."),
                d("6. Xatolikning uch manbasi",
                  r"u_{haqiqiy} - \tilde u_h = "
                  r"\underbrace{(u_{haqiqiy}-u)}_{model} + "
                  r"\underbrace{(u-u_h)}_{diskret} + "
                  r"\underbrace{(u_h-\tilde u_h)}_{yaxlitlash}",
                  "$u_{haqiqiy}$ — tabiatdagi haqiqat, $u$ — "
                  "matematik modelning aniq yechimi, $u_h$ — "
                  "diskret modelning aniq yechimi, "
                  "$\\tilde u_h$ — kompyuter bergan son."),
                d("7. Diskretlashtirish xatoligining bahosi",
                  r"\|u - u_h\| \le C\,h^{p}",
                  "$h$ — element o'lchami, $p$ — usulning "
                  "yaqinlashish tartibi. pq-10 da $p = 2{,}02$ "
                  "deb o'lchangan edi — bu aynan shu qonun."),
                d("8. Yaxlitlash xatoligining teskari qonuni",
                  r"\|u_h - \tilde u_h\| \sim "
                  r"\varepsilon_{mach}\,\kappa(\mathbf{K}) "
                  r"\sim \varepsilon_{mach}\,h^{-q}",
                  "**Teskari yo'nalish.** To'r zichlashsa "
                  "$\\mathbf{K}$ ning shartlanganlik soni "
                  "$\\kappa$ o'sadi va yaxlitlash xatoligi "
                  "ortadi (su-04). Demak to'rni cheksiz "
                  "zichlashtirish foydasiz."),
                d("9. Optimal to'r",
                  r"E(h) = C h^p + \frac{\varepsilon_{mach}A}"
                  r"{h^q} \;\Longrightarrow\; "
                  r"h_{opt} = \Big(\frac{qA\varepsilon_{mach}}"
                  r"{pC}\Big)^{1/(p+q)}",
                  "Ikki qarama-qarshi hadning yig'indisi "
                  "minimumga ega — xuddi pq-29 va pq-30 dagi "
                  "raqobat kabi. Kodda bu aniq ko'rsatiladi."),
            ],
            meaning=(
                "Sonli usullarning butun g'oyasi 2- va "
                "5-qadamlarda: cheksiz o'lchovli masalani "
                "chekli o'lchovli masalaga almashtirish va "
                "differensial tenglamani chiziqli algebraik "
                "tizimga aylantirish. Undan keyingisi — "
                "matritsalar bilan ishlash, buni kompyuter "
                "juda yaxshi bajaradi. Usullar bir-biridan "
                "faqat **bazis tanlashda** farq qiladi va bu "
                "farq hal qiluvchi. Navye qatori global "
                "sinuslarni oladi: ular butun sohada "
                "aniqlangan, shuning uchun soha "
                "to'rtburchak bo'lishi shart. FEM mahalliy "
                "funksiyalarni oladi: har biri faqat bir "
                "necha element ustida noldan farqli, "
                "shuning uchun **istalgan shakldagi sohani** "
                "qoplash mumkin. Aynan shu sabab FEM "
                "muhandislikda hukmron bo'lib qoldi. "
                "Ikkinchi markaziy g'oya — xatolikning uch "
                "manbasi. Ularni ajratish amaliyotda hal "
                "qiluvchi, chunki ular turlicha "
                "boshqariladi. Diskretlashtirish xatoligi "
                "to'rni zichlashtirish bilan kamayadi. "
                "Yaxlitlash xatoligi esa aksincha ortadi. "
                "Model xatoligi esa ikkalasiga ham "
                "bo'ysunmaydi: agar siz Kirxhoff "
                "gipotezasini qalin plitaga qo'llagan "
                "bo'lsangiz (pq-24), to'rni qancha "
                "zichlashtirmang, javob 22 % xato bo'lib "
                "qolaveradi. Bu eng ko'p uchraydigan va "
                "eng qimmat xato turi: hisob 'yaqinlashdi' "
                "deb xulosa qilinadi, lekin u noto'g'ri "
                "javobga yaqinlashadi. Shuning uchun "
                "verifikatsiya (tenglamani to'g'ri "
                "yechyapmizmi?) va validatsiya (to'g'ri "
                "tenglamani yechyapmizmi?) ajratiladi — "
                "bu su-28 ning mavzusi."
            ),
            equations=[
                eq(r"u(x) \approx u_h(x) = \sum_{i=1}^{N} "
                   r"u_i\varphi_i(x)",
                   "Diskretlashtirishning asosiy qadami: "
                   "cheksiz o'lchovli fazodan chekli "
                   "o'lchovliga o'tish.",
                   "Diskretlashtirish"),
                eq(r"\int_\Omega \big(\mathcal{L}u_h - f\big)"
                   r"\,w_j\,d\Omega = 0 \;\Longrightarrow\; "
                   r"\mathbf{K}\mathbf{u} = \mathbf{f}",
                   "Og'irlangan qoldiqlar usuli — barcha "
                   "sonli usullarning umumiy asosi.",
                   "Og'irlangan qoldiqlar"),
                eq(r"e = e_{model} + e_{diskret} + "
                   r"e_{yaxlitlash}",
                   "Xatolikning uch manbasi; ular turlicha "
                   "boshqariladi.", "Xatolik byudjeti"),
                eq(r"E(h) = C h^p + \frac{A\varepsilon_{mach}}"
                   r"{h^q}",
                   "Umumiy xatolikning to'r o'lchamiga "
                   "bog'liqligi; minimumga ega.",
                   "Optimal to'r"),
            ],
            conditions=(
                "**Sonli usul qachon kerak:**\n"
                "- Soha geometriyasi murakkab (teshik, "
                "qovurg'a, o'zgaruvchan qalinlik);\n"
                "- Chegaraviy shartlar aralash;\n"
                "- Material nochiziqli yoki bir jinsli emas;\n"
                "- Yuklama murakkab yoki vaqtga bog'liq;\n"
                "- Katta ko'chishlar yoki kontakt bor.\n\n"
                "**Analitik yechim qachon afzal:**\n"
                "- Sodda geometriya — u aniq, tez va "
                "parametrlarga bog'liqlikni ochiq "
                "ko'rsatadi;\n"
                "- **Sonli usulni tekshirish uchun** — "
                "bu fanda analitik yechimlar aynan shu "
                "rolda ishlatiladi.\n\n"
                "**Har qanday sonli hisob uchun majburiy "
                "shartlar:**\n"
                "1. To'r bo'yicha yaqinlashish ko'rsatilgan "
                "bo'lishi (kamida uchta to'r);\n"
                "2. Ma'lum yechimga ega etalon masalada "
                "tekshirilgan bo'lishi;\n"
                "3. Xatolik byudjeti keltirilgan bo'lishi."
            ),
            worked=WorkedExample(
                statement=(
                    "Konsol balka: $L = 1$ m, to'rtburchak "
                    "kesim $b = 30$ mm, $h_b = 10$ mm, "
                    "$E = 210$ GPa, uchida $P = 100$ N. "
                    "Uchining og'ishini (a) analitik, "
                    "(b) $n$ ta chekli ayirma bilan "
                    "hisoblang va xatolikni uchta manbaga "
                    "ajrating. Kesim balandligi $h_b$ ni "
                    "100 mm ga oshirsak model xatoligi "
                    "qanday o'zgaradi?"
                ),
                given=[
                    r"L = 1\ \text{m},\ b = 0{,}03\ \text{m},\ "
                    r"h_b = 0{,}01\ \text{m}",
                    r"E = 210\ \text{GPa},\ P = 100\ \text{N}",
                ],
                steps=[
                    st(r"I = \frac{bh_b^3}{12} = "
                       r"\frac{0{,}03 \cdot 10^{-6}}{12} = "
                       r"2{,}5\times10^{-9}\ \text{m}^4",
                       "Inersiya momenti (mq-12)."),
                    st(r"w_{an} = \frac{PL^3}{3EI} = "
                       r"\frac{100 \cdot 1}{3 \cdot 210\times"
                       r"10^{9} \cdot 2{,}5\times10^{-9}} = "
                       r"\frac{100}{1{,}575} = 63{,}49\ \text{mm}",
                       "Eyler–Bernulli nazariyasi bo'yicha "
                       "aniq yechim (mq-15)."),
                    st(r"\text{Ayirma sxemasi: } "
                       r"EI\frac{w_{i-1}-2w_i+w_{i+1}}{\Delta x^2} "
                       r"= M(x_i)",
                       "Ikkinchi tartibli markaziy ayirma; "
                       "xatosi $O(\\Delta x^2)$."),
                    st(r"n = 10: \ w_h = 62{,}857\ \text{mm}, "
                       r"\ e_{diskret} = 1{,}00\ \%",
                       "Diskretlashtirish xatoligi."),
                    st(r"n = 40: \ e_{diskret} = "
                       r"\frac{1{,}00}{16} = 0{,}0625\ \%",
                       "To'rt barobar zichlashtirish xatoni "
                       "aynan 16 barobar kamaytirdi — "
                       "$O(\\Delta x^2)$ ning aniq "
                       "tasdig'i (kodda o'lchangan tartib "
                       "$p = 2{,}000$)."),
                    st(r"\text{Model xatoligi: } "
                       r"\frac{w_{sdvig}}{w_{egilish}} = "
                       r"\frac{3EI}{\kappa GAL^2} = "
                       r"\frac{(1+\nu)}{2\kappa}"
                       r"\Big(\frac{h_b}{L}\Big)^2 = "
                       r"0{,}78\Big(\frac{h_b}{L}\Big)^2",
                       "Eyler–Bernulli sdvigni hisobga "
                       "olmaydi (pq-24 dagi kabi). "
                       "$\\nu = 0{,}3$, $\\kappa = 5/6$ "
                       "uchun koeffitsient 0,78."),
                    st(r"h_b = 10\ \text{mm}: \ (h_b/L)^2 = "
                       r"10^{-4} \;\Rightarrow\; e_{model} "
                       r"= 0{,}0078\ \%",
                       "Ingichka balkada model xatoligi "
                       "juda kichik — ahamiyatsiz."),
                    st(r"h_b = 100\ \text{mm}: \ (h_b/L)^2 = "
                       r"10^{-2} \;\Rightarrow\; e_{model} "
                       r"= 0{,}78\ \%",
                       "**Yuz barobar o'sdi**, chunki "
                       "$e_{model} \\propto (h_b/L)^2$."),
                    st(r"n \ge 160: \ e_{diskret} = "
                       r"0{,}0039\ \% < e_{model} = "
                       r"0{,}0078\ \%",
                       "Ingichka balkada ham $n = 160$ "
                       "dan boshlab model xatoligi "
                       "hukmron bo'lib qoladi: undan "
                       "keyin to'rni zichlashtirish "
                       "umumiy aniqlikni deyarli "
                       "oshirmaydi."),
                    st(r"n \to \infty: \ e_{diskret} \to 0, "
                       r"\ \text{lekin} \ e_{model} \ "
                       r"\text{o'zgarmaydi}",
                       "Hisob 'yaqinlashdi', lekin "
                       "**noto'g'ri javobga**. Yechim — "
                       "to'rni emas, **modelni** "
                       "o'zgartirish: Timoshenko balkasi "
                       "yoki 3D elastiklik."),
                ],
                answer=(
                    "$w_{an} = 63{,}492$ mm. "
                    "Diskretlashtirish xatoligi $n = 10$ "
                    "da 1,00 %, $n = 40$ da 0,0625 %, "
                    "$n = 320$ da 0,00098 % — har "
                    "zichlashtirishda aynan 4 barobar "
                    "kamayadi ($p = 2{,}000$). Model "
                    "xatoligi $e_{model} = "
                    "0{,}78(h_b/L)^2$: $h_b = 10$ mm da "
                    "0,0078 %, $h_b = 100$ mm da "
                    "**0,78 %** va u to'r bilan "
                    "kamaymaydi. $n \\ge 160$ dan "
                    "boshlab model xatoligi hukmron."
                ),
                engineering_note=(
                    "Bu misol butun fanning asosiy "
                    "saboqini beradi: **to'rni "
                    "zichlashtirish faqat bitta xatolik "
                    "turini kamaytiradi**. Amaliyotda eng "
                    "ko'p uchraydigan va eng qimmat xato "
                    "aynan shu: muhandis to'r bo'yicha "
                    "yaqinlashishni ko'rsatadi, natija "
                    "barqarorlashadi va hisob "
                    "'tasdiqlangan' deb hisoblanadi — "
                    "lekin model noto'g'ri bo'lgani uchun "
                    "javob baribir xato. Qalin plitaga "
                    "Kirxhoff elementi qo'yilgan (pq-24: "
                    "22 % xato), chiziqli material "
                    "modelida plastik deformatsiya "
                    "bo'lgan, yoki katta ko'chishlarda "
                    "chiziqli tahlil ishlatilgan "
                    "holatlar shunga misol. Shuning "
                    "uchun har qanday sonli hisobda ikki "
                    "xil savol alohida beriladi: "
                    "'tenglamani to'g'ri yechyapmanmi?' "
                    "(verifikatsiya) va 'to'g'ri "
                    "tenglamani yechyapmanmi?' "
                    "(validatsiya)."
                ),
            ),
            computation=Computation(
                caption=(
                    "Konsol balkani analitik va sonli "
                    "yechib, xatolikning uchta manbasini "
                    "ajratib ko'rsatish."
                ),
                code='''"""Xatolikning uch manbasi: model, diskretlashtirish, yaxlitlash."""
import numpy as np
from labkit import PARAMS, note, series, table, value

L = float(PARAMS.get("L", 1.0))
b = float(PARAMS.get("b", 30.0))/1000.0
hb = float(PARAMS.get("hb", 10.0))/1000.0
E = float(PARAMS.get("E", 210.0))*1e9
nu = float(PARAMS.get("nu", 0.3))
P = float(PARAMS.get("P", 100.0))
n_show = int(PARAMS.get("n_show", 10))

I = b*hb**3/12
A = b*hb
G = E/(2*(1 + nu))
kap = 5.0/6.0

# --- (a) Analitik yechim: Eyler-Bernulli ---
w_eb = P*L**3/(3*E*I)
value("Inersiya momenti I", I, "m^4")
value("Analitik og'ish (Eyler-Bernulli)", w_eb*1000, "mm")

# --- Model xatoligi: Timoshenko tuzatmasi (sdvig) ---
w_sh = P*L/(kap*G*A)
w_tim = w_eb + w_sh
value("Sdvig hissasi", w_sh*1000, "mm")
value("Timoshenko og'ishi", w_tim*1000, "mm")
e_model = abs(w_tim - w_eb)/w_tim*100
value("MODEL xatoligi (E-B vs Timoshenko)", e_model, "%")
value("(h/L)^2", (hb/L)**2, "—")
note(f"Eyler-Bernulli modeli sdvigni hisobga olmaydi. h/L = "
     f"{hb/L:.4f} da model xatoligi {e_model:.4f} %. Bu xatolik "
     f"TO'R BILAN KAMAYMAYDI - u modelning o'zida.")


# --- (b) Chekli ayirmalar yechimi ---
def fd_tip(n):
    """EI*w'' = M(x), konsol: w(0) = 0, w'(0) = 0."""
    dx = L/n
    x = np.linspace(0, L, n + 1)
    Mx = -P*(L - x)                 # uchida P, tayanchda M = -P*L
    K = np.zeros((n + 1, n + 1))
    rhs = np.zeros(n + 1)
    K[0, 0] = 1.0                   # w(0) = 0
    rhs[0] = 0.0
    # w'(0) = 0 -> ikkinchi tartibli bir tomonlama ayirma
    K[1, 0], K[1, 1], K[1, 2] = -3.0, 4.0, -1.0
    rhs[1] = 0.0
    for i in range(2, n + 1):
        # w'' ni i-1 nuqtada markaziy ayirma bilan yozamiz
        K[i, i-2], K[i, i-1], K[i, i] = 1.0, -2.0, 1.0
        rhs[i] = Mx[i-1]*dx**2/(E*I)
    w = np.linalg.solve(K, rhs)
    return abs(w[-1]), K


ns = [5, 10, 20, 40, 80, 160, 320]
rows, errs = [], []
for n in ns:
    wn, _ = fd_tip(n)
    e = abs(wn - w_eb)/w_eb*100
    errs.append(e)
    rows.append([n, round(wn*1000, 6), round(e, 6)])
table("To'r bo'yicha yaqinlashish (diskretlashtirish xatoligi)",
      ["n", "w_uch, mm", "xatolik, %"], rows)

wn_show, K_show = fd_tip(n_show)
value(f"Sonli og'ish (n = {n_show})", wn_show*1000, "mm")
value(f"DISKRETLASHTIRISH xatoligi (n = {n_show})",
      abs(wn_show - w_eb)/w_eb*100, "%")

# Yaqinlashish tartibini O'LCHASH
orders = []
for i in range(len(ns) - 1):
    if errs[i+1] > 1e-12 and errs[i] > 1e-12:
        orders.append(np.log(errs[i]/errs[i+1])/np.log(ns[i+1]/ns[i]))
if orders:
    value("O'lchangan yaqinlashish tartibi p", float(np.mean(orders)), "—")
    note(f"To'r ikki barobar zichlashganda xatolik "
         f"{errs[0]/errs[1]:.2f} barobar kamaydi; o'lchangan tartib "
         f"p = {np.mean(orders):.3f}. Bu O(dx^2) sxemasi uchun "
         f"kutilgan natija (pq-10 da ham 2.02 chiqqan edi).")

series("Diskretlashtirish xatoligi(n)", [float(x) for x in ns], errs,
       xlabel="bo'linmalar soni n", ylabel="xatolik, %")
series("Model xatoligi (o'zgarmas)", [float(x) for x in ns],
       [e_model]*len(ns), xlabel="bo'linmalar soni n",
       ylabel="xatolik, %")

# Qachon model xatoligi hukmron bo'ladi?
dom = [n for n, e in zip(ns, errs) if e < e_model]
if dom:
    note(f"n >= {dom[0]} dan boshlab DISKRETLASHTIRISH xatoligi "
         f"({errs[ns.index(dom[0])]:.4f} %) model xatoligidan "
         f"({e_model:.4f} %) kichik bo'lib qoladi. Undan keyin to'rni "
         f"zichlashtirish umumiy aniqlikni deyarli oshirmaydi - "
         f"MODELNI yaxshilash kerak.")
else:
    note(f"Berilgan to'rlar oralig'ida diskretlashtirish xatoligi "
         f"model xatoligidan ({e_model:.4f} %) katta bo'lib qolmoqda - "
         f"to'rni yana zichlashtirish hali foydali.")

# --- Yaxlitlash xatoligi va shartlanganlik ---
conds = []
for n in ns:
    _, Kn = fd_tip(n)
    conds.append(np.linalg.cond(Kn))
series("Shartlanganlik soni cond(K)", [float(x) for x in ns], conds,
       xlabel="bo'linmalar soni n", ylabel="cond(K)")
value("cond(K), eng siyrak to'r", conds[0], "—")
value("cond(K), eng zich to'r", conds[-1], "—")
value("cond(K) o'sish nisbati", conds[-1]/conds[0], "marta")
pw = np.polyfit(np.log(ns), np.log(conds), 1)[0]
value("cond(K) ~ n^q, o'lchangan q", float(pw), "—")
eps = np.finfo(float).eps
value("Mashina epsiloni", eps, "—")
value("Kutilgan yaxlitlash xatoligi (eng zich to'r)",
      eps*conds[-1]*100, "%")
note(f"To'r {ns[0]} dan {ns[-1]} gacha zichlashganda cond(K) "
     f"{conds[-1]/conds[0]:.1e} barobar oshdi (q = {pw:.2f}). "
     f"Yaxlitlash xatoligi ~ eps*cond(K) ga mutanosib, ya'ni to'r "
     f"zichlashgani sari U ORTADI - diskretlashtirish xatoligining "
     f"AKSINCHA. Shu sababli optimal to'r mavjud.")

# --- Umumiy xatolik modeli va optimal to'r ---
nn = np.logspace(np.log10(5), np.log10(1e7), 300)
C = errs[0]*ns[0]**2                    # e_disc ~ C/n^2
Acf = eps*conds[0]/ns[0]**pw*100        # e_round ~ A*n^q
e_d = C/nn**2
e_r = Acf*nn**pw
e_t = e_d + e_r
series("Diskretlashtirish (nazariy)", nn.tolist(), e_d.tolist(),
       xlabel="n", ylabel="xatolik, %")
series("Yaxlitlash (nazariy)", nn.tolist(), e_r.tolist(),
       xlabel="n", ylabel="xatolik, %")
series("Umumiy xatolik", nn.tolist(), e_t.tolist(),
       xlabel="n", ylabel="xatolik, %")
i_opt = int(np.argmin(e_t))
value("Optimal bo'linmalar soni n_opt", float(nn[i_opt]), "—")
value("Minimal erishish mumkin bo'lgan xatolik", float(e_t[i_opt]), "%")
note(f"Ikki qarama-qarshi had yig'indisi n = {nn[i_opt]:.0f} da "
     f"minimumga erishadi ({e_t[i_opt]:.2e} %). Undan zichroq to'r "
     f"aniqlikni YOMONLASHTIRADI. Bu pq-29 va pq-30 dagi ikki hadli "
     f"raqobatning yana bir ko'rinishi.")

table("Xatolik manbalari va ularni boshqarish",
      ["Manba", "Sababi", "To'r zichlashsa", "Yechimi"],
      [["Model", "gipoteza, material modeli", "o'zgarmaydi",
        "modelni almashtirish"],
       ["Diskretlashtirish", "uzluksiz -> diskret", "kamayadi",
        "to'rni zichlashtirish"],
       ["Yaxlitlash", "chekli razryad", "ORTADI",
        "yaxshi shartlangan formulirovka"],
       ["Dastur xatosi", "kod xatosi", "o'zgarmaydi",
        "verifikatsiya (su-28)"]])
''',
                parameters=[
                    p("L", "Balka uzunligi L", 0.1, 10.0, 1.0, 0.1, "m"),
                    p("b", "Kesim eni b", 5.0, 500.0, 30.0, 1.0, "mm"),
                    p("hb", "Kesim balandligi h", 2.0, 400.0, 10.0, 1.0,
                      "mm"),
                    p("E", "Yung moduli E", 1.0, 400.0, 210.0, 1.0, "GPa"),
                    p("nu", "Puasson koeffitsienti ν", 0.0, 0.45, 0.3, 0.01),
                    p("P", "Uchidagi kuch P", 1.0, 10000.0, 100.0, 1.0, "N"),
                    p("n_show", "Ko'rsatiladigan bo'linmalar soni",
                      5.0, 200.0, 10.0, 1.0),
                ],
                expected_output=(
                    "Analitik og'ish 63,492 mm. "
                    "Diskretlashtirish xatoligi "
                    "4,0 → 1,0 → 0,25 → 0,0625 % — har "
                    "zichlashtirishda aynan 4 barobar "
                    "kamayadi, o'lchangan tartib "
                    "p = 2,000. Model xatoligi "
                    "(Eyler–Bernulli va Timoshenko "
                    "farqi) 0,0078 % va u to'rga bog'liq "
                    "emas — gorizontal chiziq bo'lib "
                    "qoladi; n ≥ 160 dan boshlab u "
                    "hukmron bo'ladi, h/L oshirilsa esa "
                    "kvadratik o'sadi. cond(K) to'r "
                    "bilan birga n^1,91 kabi o'sadi, "
                    "shuning uchun yaxlitlash xatoligi "
                    "ortadi va umumiy xatolik chekli "
                    "n ≈ 7600 da minimumga erishadi."
                ),
            ),
            visual=vis(
                kind="Xatolik byudjeti va optimal to'r",
                tool="React/SVG + Manim",
                description=(
                    "Uchta xatolik manbasining to'r "
                    "o'lchamiga bog'liqligi va ularning "
                    "yig'indisidagi minimum."
                ),
                how_to_draw=(
                    "React/SVG: asosiy panel — log–log "
                    "o'qlarda uchta chiziq. "
                    "Diskretlashtirish xatoligi $-2$ "
                    "qiyalik bilan pasayadi; yaxlitlash "
                    "xatoligi musbat qiyalik bilan "
                    "ko'tariladi; ularning yig'indisi "
                    "$V$ shaklida bo'lib, minimumi "
                    "belgilanadi va $n_{opt}$ yoziladi. "
                    "Model xatoligi esa **gorizontal "
                    "chiziq** — u hech qayerda "
                    "pasaymaydi, va bu vizual jihatdan "
                    "eng muhim detal. Slayder bilan "
                    "$h_b/L$ o'zgartirilganda gorizontal "
                    "chiziq yuqoriga siljiydi va "
                    "ma'lum nuqtada u butun egri "
                    "chiziqdan yuqori bo'lib qoladi — "
                    "shu holatda 'to'rni zichlashtirish "
                    "befoyda' degan yozuv paydo bo'ladi. "
                    "Ikkinchi panel — diskretlashtirish "
                    "g'oyasi: uzluksiz balka egri "
                    "chizig'i ustiga tugunlar qo'yiladi "
                    "va ular soni oshgani sari "
                    "bo'lakli-chiziqli yaqinlashish "
                    "haqiqiy egri chiziqqa yopishadi."
                ),
            ),
            interp=(
                "Sonli natija uchta chiziqda jamlangan "
                "va ular butun fanning xaritasi bo'lib "
                "xizmat qiladi. Diskretlashtirish "
                "xatoligi $-2$ qiyalik bilan pasayadi — "
                "bu 7-qadamdagi $Ch^p$ qonuni va "
                "o'lchangan tartib $p \\approx 2$ uni "
                "tasdiqlaydi (pq-10 dagi 2,02 bilan "
                "mos). Shartlanganlik soni esa to'r "
                "bilan birga o'sadi, demak yaxlitlash "
                "xatoligi ortadi va umumiy xatolik "
                "chekli $n$ da minimumga erishadi. "
                "Bu 9-qadamning sonli tasdig'i va u "
                "amaliy jihatdan muhim: to'rni cheksiz "
                "zichlashtirish nafaqat qimmat, balki "
                "ma'lum chegaradan keyin **zararli**. "
                "Lekin eng muhim chiziq — model "
                "xatoligining gorizontal chizig'i. U "
                "boshqa ikkisi bilan umuman "
                "raqobatlashmaydi: to'r qanchalik zich "
                "bo'lmasin, u o'z joyida qoladi. "
                "$h_b/L$ ni oshirganda bu chiziq "
                "yuqoriga siljiydi va tez orada "
                "hukmron bo'lib qoladi — o'shanda "
                "hisob 'yaqinlashadi', lekin noto'g'ri "
                "javobga. Aynan shu sabab bu fanning "
                "oxirgi modulida verifikatsiya va "
                "validatsiya alohida mavzu sifatida "
                "o'rganiladi."
            ),
            mistakes=[
                "To'r bo'yicha yaqinlashishni "
                "natijaning to'g'riligi deb hisoblash. "
                "U faqat diskretlashtirish xatoligi "
                "kichikligini ko'rsatadi, model "
                "xatoligi haqida hech narsa demaydi.",
                "To'rni cheksiz zichlashtirishga "
                "urinish. Yaxlitlash xatoligi ortgani "
                "uchun optimal $h$ dan keyin aniqlik "
                "yomonlashadi.",
                "Analitik yechimni 'eskirgan' deb "
                "hisoblash. Bu fanda u sonli usulni "
                "tekshirishning asosiy vositasi.",
                "Sonli natijani ko'p xonali son bilan "
                "keltirish. Aniqlik xatolik bahosidan "
                "oshmaydi; 63,4857 mm deb yozish "
                "0,38 % xatolik bilan ma'nosiz.",
                "Model tanlashni dastur zimmasiga "
                "yuklash. Element turini (Kirxhoff yoki "
                "Mindlin, chiziqli yoki nochiziqli) "
                "muhandis tanlaydi.",
            ],
            quiz=[
                q("Barcha sonli usullarning umumiy "
                  "g'oyasi nima?",
                  "Cheksiz o'lchovli uzluksiz masalani "
                  "chekli o'lchovli algebraik masalaga "
                  "almashtirish: "
                  "$u \\approx \\sum u_i\\varphi_i$ va "
                  "$\\mathbf{K}\\mathbf{u} = \\mathbf{f}$.",
                  "konseptual"),
                q("Nima uchun FEM murakkab geometriyada "
                  "qator usullaridan ustun?",
                  "FEM mahalliy bazis funksiyalarini "
                  "ishlatadi — har biri faqat bir necha "
                  "element ustida noldan farqli, shuning "
                  "uchun istalgan shakldagi sohani "
                  "qoplash mumkin.", "talqin"),
                q("Uchta xatolik manbasidan qaysi biri "
                  "to'rni zichlashtirish bilan "
                  "kamaymaydi?",
                  "Model xatoligi — u matematik "
                  "modelning o'zida; to'r bilan umuman "
                  "bog'liq emas. Yaxlitlash xatoligi esa "
                  "aksincha ortadi.", "konseptual"),
                q("Kodda nima uchun cond(K) hisoblanadi?",
                  "U yaxlitlash xatoligining o'lchovi: "
                  "$e \\sim \\varepsilon_{mach}"
                  "\\kappa(\\mathbf{K})$; to'r "
                  "zichlashgani sari $\\kappa$ o'sadi "
                  "va optimal to'r shundan kelib "
                  "chiqadi.", "kod"),
                q("$h_b$ ni 10 dan 100 mm ga oshirsak "
                  "model xatoligi necha barobar "
                  "o'zgaradi va nima uchun?",
                  "100 barobar (0,0078 % dan 0,78 % ga), chunki u "
                  "$(h_b/L)^2$ ga mutanosib — "
                  "$10^2 = 100$. Qalin balkada "
                  "Eyler–Bernulli modeli yaroqsiz "
                  "bo'lib qoladi.", "hisob"),
                q("Verifikatsiya va validatsiya nima "
                  "bilan farq qiladi?",
                  "Verifikatsiya — 'tenglamani to'g'ri "
                  "yechyapmanmi?' (diskretlashtirish va "
                  "dastur xatosi); validatsiya — "
                  "'to'g'ri tenglamani yechyapmanmi?' "
                  "(model xatoligi).", "talqin"),
            ],
            bridge=(
                "Xatolikning uch manbasidan eng "
                "kutilmagani — yaxlitlash. U to'r "
                "zichlashgani sari **ortadi** va "
                "optimal to'rni belgilaydi. Bu "
                "xatolik kompyuterning sonlarni "
                "qanday saqlashidan kelib chiqadi. "
                "Keyingi mavzuda suzuvchi nuqta "
                "arifmetikasini batafsil ko'ramiz va "
                "mexanika hisoblarida qanday "
                "kutilmagan natijalar berishini "
                "ko'rsatamiz."
            ),
            research=(
                "Hisoblash mexanikasining rivojini "
                "miqdoriy o'rganing. (1) 1960-yildan "
                "bugungacha bir xil masalani yechish "
                "vaqti qanday kamaygan? Buning qancha "
                "qismi apparat tezligidan "
                "(Mur qonuni), qanchasi algoritm "
                "yutuqlaridan (siyrak matritsalar, "
                "ko'p to'rli usullar, oldindan "
                "shartlash) kelib chiqqanini "
                "solishtiring. (2) 'Hisoblash "
                "eksperimenti' tushunchasining fanda "
                "nazariya va tajribadan keyingi "
                "uchinchi usul sifatida paydo "
                "bo'lishini tahlil qiling. "
                "(3) Zamonaviy tendensiyalarni "
                "ko'rib chiqing: izogeometrik tahlil "
                "(IGA), mashinali o'qitish asosidagi "
                "surrogat modellar va ular klassik "
                "FEM ni qay darajada almashtira oladi."
            ),
            manim_ref=manim(
                scene="DiscretizationScene",
                module="manim/scenes/su_basics.py",
                title="Diskretlashtirish va xatolik byudjeti",
                summary=(
                    "Uzluksiz balka egri chizig'i "
                    "tugunlarga bo'linadi va bo'laklar "
                    "soni oshgani sari sonli yechim "
                    "aniq yechimga yopishadi. Keyin "
                    "log–log grafikda uchta xatolik "
                    "chizig'i quriladi: pasayuvchi, "
                    "ko'tariluvchi va gorizontal; "
                    "ularning yig'indisidagi minimum "
                    "ajratib ko'rsatiladi."
                ),
            ),
        ),
    ),

    # ------------------------------------------------------------------ su-02
    Topic(
        id="su-02",
        subject_id=S, module_id=M, order=2,
        title="Suzuvchi nuqta arifmetikasi va yaxlitlash xatoligi",
        description=(
            "IEEE 754 formati, mashina epsiloni, katastrofik qisqarish, "
            "yig'indi tartibining ahamiyati va mexanika hisoblaridagi "
            "amaliy oqibatlari."
        ),
        learning_objective=(
            "Suzuvchi nuqta sonining aniqligini baholash, katastrofik "
            "qisqarishni aniqlash va undan qochadigan formulani yozish."
        ),
        prerequisites=["su-01"],
        mathematical_core=(
            "$fl(x) = x(1+\\delta)$, $|\\delta| \\le "
            "\\varepsilon_{mach}/2$; qisqarishda nisbiy xatolik "
            "$\\dfrac{|x|+|y|}{|x-y|}$ marta kuchayadi."
        ),
        engineering_application=(
            "Yupqa devorli kesim xarakteristikalari, uzun ferma "
            "koordinatalari, katta bikrlik farqlari, iteratsiya "
            "to'xtash mezonlari, vaqt bo'yicha uzoq integrallash."
        ),
        computational_component=(
            "Mashina epsilonini o'lchash, katastrofik qisqarishni "
            "namoyish qilish va barqaror formula bilan taqqoslash."
        ),
        visualization_component=(
            "Yo'qolgan aniq raqamlar soni, xatolikning argumentga "
            "bog'liqligi, barqaror va nobarqaror formulalar."
        ),
        research_extension=(
            "Kompensatsiyalangan yig'indi algoritmlarini (Kahan, "
            "Neumaier) va ularning xatolik chegaralarini o'rganing; "
            "qo'sh-qo'sh aniqlik va interval arifmetikasini solishtiring."
        ),
        difficulty="asosiy",
        previous_link=(
            "su-01 da yaxlitlash xatoligi to'r zichlashgani sari "
            "**ortishi** ko'rsatildi va optimal to'r shundan kelib "
            "chiqdi. Endi bu xatolikning manbasiga tushamiz: "
            "kompyuter haqiqiy sonlarni qanday saqlaydi."
        ),
        next_topic="su-03",
        estimated_minutes=80,
        tags=["IEEE 754", "epsilon", "qisqarish", "aniqlik"],
        lesson=_lesson(
            problem=(
                "Yupqa devorli quvur kesimining inersiya "
                "momentini hisoblaymiz: "
                "$I = \\pi(D^4 - d^4)/64$. Tashqi diametr "
                "$D = 200{,}0$ mm, devor qalinligi 1 mm, "
                "demak $d = 198{,}0$ mm. $D^4$ va $d^4$ "
                "bir-biriga juda yaqin sonlar va ularning "
                "ayirmasi hisoblanadi. Agar hisob "
                "birliklari mm da bo'lsa, $D^4 = 1{,}6"
                "\\times10^{9}$ va $d^4 = 1{,}538\\times"
                "10^{9}$ — ular 16 ta aniq raqamdan "
                "faqat dastlabki ikkitasida farq qiladi. "
                "Ayirma olinganda **14 ta aniq raqam "
                "yo'qoladi**. Devor yana ingichkalashsa "
                "(0,1 mm), natija umuman ma'nosiz bo'lib "
                "qolishi mumkin. Bu shunchaki nazariy "
                "xavf emas: aviatsiya va kemasozlikda "
                "yupqa devorli kesimlar odatiy holat."
            ),
            concepts=[
                c("IEEE 754 suzuvchi nuqta formati",
                  "Son $\\pm m \\cdot 2^{e}$ ko'rinishida "
                  "saqlanadi; `double` da mantissa 53 bit "
                  "(shundan 52 tasi saqlanadi), tartib "
                  "11 bit."),
                c("Mashina epsiloni "
                  "$\\varepsilon_{mach}$",
                  "$1$ dan katta eng kichik son bilan $1$ "
                  "orasidagi farq; `double` uchun "
                  "$2^{-52} \\approx 2{,}22\\times10^{-16}$ "
                  "— taxminan 16 o'nlik raqam."),
                c("Yaxlitlash modeli",
                  "$fl(x \\circ y) = (x \\circ y)(1+\\delta)$, "
                  "$|\\delta| \\le \\varepsilon_{mach}/2$ — "
                  "har bir amal kichik nisbiy xato kiritadi."),
                c("Katastrofik qisqarish "
                  "(catastrophic cancellation)",
                  "Yaqin sonlarning ayirmasida aniq "
                  "raqamlar ommaviy yo'qolishi; nisbiy "
                  "xatolik $(|x|+|y|)/|x-y|$ marta "
                  "kuchayadi."),
                c("Yutilish (absorption)",
                  "$a + b$ da $b \\ll a$ bo'lsa $b$ "
                  "butunlay yo'qoladi; yig'indi tartibi "
                  "natijaga ta'sir qiladi."),
                c("Barqaror formula",
                  "Matematik jihatdan teng, lekin "
                  "qisqarishdan qochadigan ifoda "
                  "(masalan $D^4-d^4$ o'rniga "
                  "ko'paytuvchilarga ajratish)."),
            ],
            derivation=[
                d("1. Suzuvchi nuqta sonining tuzilishi",
                  r"x = \pm\,(1.b_1b_2\ldots b_{52})_2 "
                  r"\times 2^{e}, \quad -1022 \le e \le 1023",
                  "Mantissa 53 bitlik aniqlik beradi "
                  "(birinchi bit yashirin). Tartib "
                  "diapazoni $10^{\\pm308}$ atrofida."),
                d("2. Mashina epsiloni",
                  r"\varepsilon_{mach} = 2^{-52} = "
                  r"2{,}220\times10^{-16}",
                  "Bu $1$ va $1$ dan keyingi son "
                  "orasidagi masofa. O'nlik raqamlarda "
                  "$\\log_{10}(1/\\varepsilon) = 15{,}65$, "
                  "ya'ni taxminan 16 ta ishonchli raqam."),
                d("3. Yaxlitlash modeli",
                  r"fl(x) = x(1+\delta_1), \quad "
                  r"fl(x \circ y) = (x\circ y)(1+\delta_2)",
                  "Har bir saqlash va har bir amal nisbiy "
                  "xato kiritadi. Bitta amalda bu juda "
                  "kichik — muammo ularning "
                  "to'planishida va kuchayishida."),
                d("4. Ayirmadagi xatolikning kuchayishi",
                  r"z = x - y; \quad \tilde z = "
                  r"x(1+\delta_x) - y(1+\delta_y)",
                  "$\\tilde z - z = x\\delta_x - "
                  "y\\delta_y$, demak mutlaq xato "
                  "$|x|+|y|$ tartibida kichik son bilan "
                  "chegaralangan."),
                d("5. Nisbiy xatolikning kuchayish "
                  "koeffitsienti",
                  r"\frac{|\tilde z - z|}{|z|} \le "
                  r"\frac{|x|+|y|}{|x-y|}\,"
                  r"\varepsilon_{mach}",
                  "**Hal qiluvchi natija.** Agar $x$ va "
                  "$y$ yaqin bo'lsa, maxraj kichik va "
                  "koeffitsient katta. Bu **shartlanganlik "
                  "soni** ning eng sodda ko'rinishi "
                  "(su-04)."),
                d("6. Yo'qolgan raqamlar soni",
                  r"\text{yo'qolgan raqamlar} \approx "
                  r"\log_{10}\frac{|x|+|y|}{|x-y|}",
                  "Kirish misolida "
                  "$D^4 \\approx 1{,}6\\times10^9$, "
                  "$D^4-d^4 \\approx 6{,}2\\times10^7$, "
                  "nisbat $\\approx 51$ — taxminan "
                  "1,7 raqam yo'qoladi. Devor 0,01 mm "
                  "bo'lsa nisbat 5000 ga chiqadi va "
                  "3,7 raqam yo'qoladi."),
                d("7. Barqaror formulaga o'tish",
                  r"D^4 - d^4 = (D^2+d^2)(D+d)(D-d)",
                  "**Qisqarish faqat $(D-d)$ da qoladi** "
                  "va u kirish ma'lumotining o'zida "
                  "berilgan (devor qalinligining ikki "
                  "barobari), demak qo'shimcha xato "
                  "kiritilmaydi. Qolgan ko'paytmalar "
                  "xavfsiz."),
                d("8. Yig'indining tartibga bog'liqligi",
                  r"fl\Big(\sum_{i=1}^{n} x_i\Big) - "
                  r"\sum x_i \ \text{— tartibga bog'liq}",
                  "Suzuvchi nuqta qo'shish "
                  "**assotsiativ emas**: "
                  "$(a+b)+c \\ne a+(b+c)$. Kichik "
                  "hadlarni avval qo'shish aniqroq."),
                d("9. Xatolikning to'planishi",
                  r"|E_n| \le n\,\varepsilon_{mach}"
                  r"\sum|x_i| \ \text{(oddiy)}; \quad "
                  r"|E_n| \le 2\varepsilon_{mach}"
                  r"\sum|x_i| \ \text{(Kahan)}",
                  "Oddiy yig'indida xato $n$ bilan "
                  "o'sadi; Kahan kompensatsiyasi uni "
                  "$n$ dan mustaqil qiladi. Uzoq "
                  "vaqtli integrallashda bu hal "
                  "qiluvchi."),
                d("10. Nolga tenglikni tekshirish",
                  r"x = y \ \text{o'rniga} \ |x-y| \le "
                  r"\tau(|x|+|y|) + \tau_{abs}",
                  "Suzuvchi nuqta sonlarini aynan "
                  "tenglikka tekshirish deyarli har doim "
                  "xato. Iteratsiyani to'xtatishda "
                  "**nisbiy** mezon ishlatiladi."),
            ],
            meaning=(
                "Suzuvchi nuqta arifmetikasining asosiy "
                "xossasi — u **nisbiy** aniqlikni "
                "saqlaydi: har qanday son taxminan 16 ta "
                "ishonchli raqam bilan saqlanadi, son "
                "qanchalik katta yoki kichik bo'lishidan "
                "qat'i nazar. Ko'paytirish va bo'lish bu "
                "nisbiy aniqlikni buzmaydi — ularda "
                "xatolar shunchaki qo'shiladi. Xavf "
                "faqat **ayirishda**, va aynan yaqin "
                "sonlarni ayirganda. 5-qadamdagi "
                "kuchayish koeffitsienti "
                "$(|x|+|y|)/|x-y|$ buni aniq ifodalaydi: "
                "sonlar qanchalik yaqin bo'lsa, natijada "
                "shuncha kam aniq raqam qoladi. Muhim "
                "nuqta shundaki, qisqarish "
                "**yangi xato yaratmaydi** — u faqat "
                "allaqachon mavjud xatoni ko'rinarli "
                "qiladi. $D^4$ va $d^4$ har biri 16 "
                "raqam aniqlikda saqlangan; ularning "
                "ayirmasida shu xatolar qoladi, lekin "
                "natija kichik bo'lgani uchun nisbiy "
                "xato kattalashadi. Shuning uchun yechim "
                "aniqlikni oshirish emas (u faqat "
                "muammoni kechiktiradi), balki "
                "**formulani qayta yozish**: "
                "7-qadamdagi ko'paytuvchilarga ajratish "
                "qisqarishni butunlay yo'q qiladi. Bu "
                "sonli usullardagi umumiy tamoyil: "
                "matematik jihatdan teng ifodalar sonli "
                "jihatdan teng emas. Mexanikada bu "
                "ayniqsa tez-tez uchraydi: yupqa devorli "
                "kesimlar, uzun konstruksiyalardagi "
                "koordinata farqlari, bir-biriga yaqin "
                "xususiy chastotalar, katta va kichik "
                "bikrliklar aralashgan tizimlar — "
                "hammasida yaqin sonlar ayiriladi."
            ),
            equations=[
                eq(r"\varepsilon_{mach} = 2^{-52} \approx "
                   r"2{,}22\times10^{-16}",
                   "Ikki aniqlikli (`double`) mashina "
                   "epsiloni — taxminan 16 o'nlik raqam.",
                   "Mashina epsiloni"),
                eq(r"fl(x \circ y) = (x \circ y)(1+\delta), "
                   r"\quad |\delta| \le "
                   r"\frac{\varepsilon_{mach}}{2}",
                   "Standart yaxlitlash modeli.",
                   "Yaxlitlash modeli"),
                eq(r"\frac{\Delta z}{z} \le "
                   r"\frac{|x|+|y|}{|x-y|}"
                   r"\,\varepsilon_{mach}",
                   "Ayirmadagi nisbiy xatolikning "
                   "kuchayishi — katastrofik qisqarish.",
                   "Qisqarish koeffitsienti"),
                eq(r"D^4 - d^4 = (D^2+d^2)(D+d)(D-d)",
                   "Qisqarishdan qochadigan barqaror "
                   "shakl.", "Barqaror formula"),
            ],
            conditions=(
                "**Qisqarish xavfi yuqori bo'lgan "
                "holatlar:**\n"
                "- Yupqa devorli kesim "
                "xarakteristikalari ($D^4 - d^4$);\n"
                "- Uzoq nuqtalar orasidagi masofa "
                "(global koordinatalarda);\n"
                "- Kvadrat tenglama ildizlari "
                "$-b \\pm \\sqrt{b^2-4ac}$ da "
                "$b^2 \\gg 4ac$ bo'lganda;\n"
                "- Sonli hosila "
                "$(f(x+h)-f(x))/h$ da $h$ kichik "
                "bo'lganda (su-03);\n"
                "- Bir-biriga yaqin xususiy qiymatlar.\n\n"
                "**Amaliy qoidalar:**\n"
                "1. Suzuvchi nuqta sonlarini "
                "`==` bilan solishtirmang;\n"
                "2. Iteratsiya mezoni nisbiy bo'lsin: "
                "$|x_{k+1}-x_k| \\le \\tau|x_k| + "
                "\\tau_{abs}$;\n"
                "3. Birliklarni moslang — SI da "
                "hisoblang, natijani qulay birlikka "
                "o'tkazing;\n"
                "4. Uzun yig'indida Kahan "
                "kompensatsiyasi yoki juftlab "
                "(pairwise) yig'indi ishlating;\n"
                "5. Formulani qayta yozish aniqlikni "
                "oshirishdan afzal."
            ),
            worked=WorkedExample(
                statement=(
                    "Yupqa devorli quvur: $D = 200$ mm, "
                    "devor $t = 1$ mm ($d = 198$ mm). "
                    "(a) $I = \\pi(D^4-d^4)/64$ ni "
                    "to'g'ridan-to'g'ri va ko'paytuvchi "
                    "shaklda hisoblang; (b) $t = 0{,}01$ "
                    "mm bo'lsa nechta aniq raqam "
                    "yo'qoladi? (c) $x^2 - 10^{8}x + 1 = 0$ "
                    "tenglamasining kichik ildizini ikki "
                    "usulda toping."
                ),
                given=[
                    r"D = 200\ \text{mm},\ t = 1\ \text{mm} "
                    r"\Rightarrow d = 198\ \text{mm}",
                    r"\varepsilon_{mach} = 2{,}22\times10^{-16}",
                ],
                steps=[
                    st(r"D^4 = 1{,}6\times10^{9}, \quad "
                       r"d^4 = 1{,}53656\times10^{9}\ "
                       r"\text{mm}^4",
                       "$198^4 = 1\\,536\\,953\\,616$."),
                    st(r"D^4 - d^4 = 1{,}6\times10^{9} - "
                       r"1{,}536954\times10^{9} = "
                       r"6{,}3046\times10^{7}\ \text{mm}^4",
                       "Ayirma asl sonlardan 25 barobar "
                       "kichik."),
                    st(r"\frac{|D^4|+|d^4|}{|D^4-d^4|} = "
                       r"\frac{3{,}137\times10^{9}}"
                       r"{6{,}305\times10^{7}} = 49{,}8",
                       "Kuchayish koeffitsienti; "
                       "$\\log_{10}49{,}8 = 1{,}70$ — "
                       "taxminan **1,7 raqam** "
                       "yo'qoladi. 16 dan 14,3 qoladi — "
                       "hali xavfsiz."),
                    st(r"I = \frac{\pi \cdot 6{,}3046\times"
                       r"10^{7}}{64} = 3{,}09478\times10^{6}\ "
                       r"\text{mm}^4",
                       "Inersiya momenti."),
                    st(r"(b)\ t = 0{,}01: \ d = 199{,}98, \ "
                       r"D^4-d^4 \approx 6{,}4\times10^{5}",
                       "Ayirma 100 barobar kichrayadi, "
                       "asl sonlar esa deyarli "
                       "o'zgarmaydi."),
                    st(r"\frac{3{,}2\times10^{9}}"
                       r"{6{,}4\times10^{5}} = 5000 "
                       r"\;\Rightarrow\; \log_{10}5000 = "
                       r"3{,}70",
                       "**3,7 raqam yo'qoladi.** "
                       "`float32` da (7 raqam) natija "
                       "3 raqamga qoladi — yaroqsiz. "
                       "`double` da hali chidasa "
                       "bo'ladi, lekin chegara "
                       "yaqinlashmoqda."),
                    st(r"(c)\ x^2 - 10^{8}x + 1 = 0: \ "
                       r"x_{1,2} = \frac{10^{8} \pm "
                       r"\sqrt{10^{16}-4}}{2}",
                       "$\\sqrt{10^{16}-4} \\approx "
                       "10^{8}$ — ikkita deyarli teng "
                       "son."),
                    st(r"x_2^{(sodda)} = \frac{10^{8} - "
                       r"\sqrt{10^{16}-4}}{2} "
                       r"\;\Rightarrow\; \text{qisqarish, "
                       r"natija xato}",
                       "$10^{16}$ da $4$ ni ayirish "
                       "`double` aniqligida deyarli "
                       "ko'rinmaydi: "
                       "$\\varepsilon\\cdot10^{16} = 2{,}2$ "
                       "— ayiriladigan son bilan bir "
                       "tartibda!"),
                    st(r"x_2^{(barqaror)} = "
                       r"\frac{c}{a\,x_1} = "
                       r"\frac{1}{10^{8}} = 10^{-8}",
                       "Viet teoremasidan: "
                       "$x_1x_2 = c/a$. Katta ildizni "
                       "barqaror formuladan topib, "
                       "kichigini bo'lish orqali "
                       "olamiz — qisqarish butunlay "
                       "yo'q."),
                ],
                answer=(
                    "(a) $I = 3{,}09478\\times10^{6}$ mm⁴; "
                    "kuchayish koeffitsienti 49,8, "
                    "yo'qolgan raqamlar 1,7 — xavfsiz. "
                    "(b) $t = 0{,}01$ mm da koeffitsient "
                    "5000 ga chiqadi va **3,7 raqam** "
                    "yo'qoladi; `float32` uchun bu "
                    "halokatli. (c) Kichik ildizni "
                    "to'g'ridan-to'g'ri formuladan "
                    "hisoblash qisqarish beradi; "
                    "$x_2 = c/(ax_1)$ shakli aniq "
                    "$10^{-8}$ ni qaytaradi."
                ),
                engineering_note=(
                    "Amaliyotda eng xavfli tomoni "
                    "shundaki, qisqarish **hech qanday "
                    "ogohlantirish bermaydi**: dastur "
                    "xatolik chiqarmaydi, natija "
                    "ishonchli ko'rinadi va faqat "
                    "mustaqil tekshiruvda "
                    "aniqlanadi. Shuning uchun yupqa "
                    "devorli kesimlar bilan ishlaganda "
                    "formula shakli oldindan tanlanadi. "
                    "`float32` (7 raqam) ishlatadigan "
                    "GPU hisoblarida va ba'zi eski "
                    "kodlarda bu chegara juda tez "
                    "yetib keladi. Yana bir keng "
                    "tarqalgan holat — global "
                    "koordinatalar: agar konstruksiya "
                    "UTM koordinatalarida berilgan "
                    "bo'lsa ($x \\approx 5\\times10^5$ "
                    "m), 1 mm aniqlikdagi farqlar "
                    "$10^{-9}$ nisbiy darajada bo'ladi "
                    "va `float32` da butunlay "
                    "yo'qoladi. Yechim — mahalliy "
                    "koordinata boshini konstruksiya "
                    "yaqiniga ko'chirish."
                ),
            ),
            computation=Computation(
                caption=(
                    "Mashina epsilonini o'lchash, "
                    "katastrofik qisqarishni namoyish "
                    "qilish va barqaror formulalar bilan "
                    "taqqoslash."
                ),
                code='''"""Suzuvchi nuqta arifmetikasi va katastrofik qisqarish."""
import numpy as np
from labkit import PARAMS, note, series, table, value

D = float(PARAMS.get("D", 200.0))
t_wall = float(PARAMS.get("t", 1.0))
n_sum = int(PARAMS.get("n_sum", 1000000))
bq = float(PARAMS.get("bq", 1e8))

# --- Mashina epsilonini O'LCHASH (formuladan olmasdan) ---
e = 1.0
while 1.0 + e/2.0 != 1.0:
    e = e/2.0
value("O'lchangan mashina epsiloni", e, "—")
value("numpy e'lon qilgan epsilon", float(np.finfo(float).eps), "—")
value("Nazariy 2^-52", 2.0**-52, "—")
value("Ishonchli o'nlik raqamlar soni", -np.log10(e), "—")
note(f"Epsilon ikkiga bo'lish bilan O'LCHANDI: {e:.6e}; bu 2^-52 = "
     f"{2.0**-52:.6e} bilan aynan bir xil. Demak double formati "
     f"taxminan {-np.log10(e):.1f} ta ishonchli o'nlik raqam beradi.")

# Assotsiativlikning buzilishi
a1 = (1.0 + e/2) - 1.0
a2 = 1.0 + (e/2 - 1.0)
value("(1 + eps/2) - 1", a1, "—")
value("1 + (eps/2 - 1)", a2, "—")
note(f"(1 + eps/2) - 1 = {a1:.3e}, lekin 1 + (eps/2 - 1) = {a2:.3e}. "
     f"Suzuvchi nuqta qo'shishi ASSOTSIATIV EMAS - qavslar joyi "
     f"natijaga ta'sir qiladi.")

# --- Katastrofik qisqarish: yupqa devorli quvur ---
rows = []
for tw in [10.0, 5.0, 2.0, 1.0, 0.1, 0.01, 0.001]:
    d = D - 2*tw
    direct = D**4 - d**4
    stable = (D**2 + d**2)*(D + d)*(D - d)
    amp = (abs(D**4) + abs(d**4))/abs(direct)
    lost = np.log10(amp)
    rel = abs(direct - stable)/abs(stable) if stable != 0 else 0.0
    rows.append([f"{tw:g}", f"{direct:.6e}", f"{stable:.6e}",
                 f"{amp:.1f}", f"{lost:.2f}", f"{rel:.2e}"])
table("Yupqa devorli quvur: D^4 - d^4 ikki usulda",
      ["t, mm", "to'g'ridan-to'g'ri", "ko'paytuvchi shakl",
       "kuchayish", "yo'qolgan raqam", "nisbiy farq"], rows)

tws = np.logspace(np.log10(0.0005), np.log10(20.0), 200)
amps, losts = [], []
for tw in tws:
    d = D - 2*tw
    direct = D**4 - d**4
    amp = (abs(D**4) + abs(d**4))/abs(direct)
    amps.append(amp)
    losts.append(np.log10(amp))
series("Yo'qolgan raqamlar soni(devor qalinligi)", tws.tolist(), losts,
       xlabel="devor qalinligi t, mm", ylabel="yo'qolgan raqamlar")
series("float32 chegarasi (7 raqam)", tws.tolist(), [7.0]*len(tws),
       xlabel="devor qalinligi t, mm", ylabel="yo'qolgan raqamlar")
series("double chegarasi (16 raqam)", tws.tolist(), [16.0]*len(tws),
       xlabel="devor qalinligi t, mm", ylabel="yo'qolgan raqamlar")

d0 = D - 2*t_wall
amp0 = (abs(D**4) + abs(d0**4))/abs(D**4 - d0**4)
value("Tanlangan devor uchun kuchayish koeffitsienti", amp0, "—")
value("Yo'qolgan raqamlar", float(np.log10(amp0)), "—")
I_dir = np.pi*(D**4 - d0**4)/64
I_st = np.pi*(D**2 + d0**2)*(D + d0)*(D - d0)/64
value("I (to'g'ridan-to'g'ri)", I_dir, "mm^4")
value("I (barqaror shakl)", I_st, "mm^4")
note(f"t = {t_wall:g} mm da kuchayish koeffitsienti {amp0:.1f}, ya'ni "
     f"{np.log10(amp0):.2f} ta aniq raqam yo'qoladi. double da 16 "
     f"raqamdan {16 - np.log10(amp0):.1f} tasi qoladi - hali "
     f"xavfsiz; float32 (7 raqam) da esa zaxira tez tugaydi.")

# --- float32 da AYNAN SHU hisobni takrorlash ---
# MUHIM: taqqoslash halol bo'lishi uchun ikkala formulaga ham AYNAN
# bir xil kirish ma'lumoti beriladi: D va devor qalinligi t. Barqaror
# shaklda (D - d) SONLI ravishda hisoblanmaydi - uning o'rniga
# kirishda berilgan 2*t ishlatiladi. Aks holda d ning float32 da
# ifodalanish xatosi qisqarish ta'sirini niqoblab qo'yadi.
D32 = np.float32(D)
rows32 = []
for tw in [1.0, 0.1, 0.01, 0.001]:
    t32 = np.float32(tw)
    d32 = np.float32(D32 - np.float32(2.0)*t32)
    dir32 = np.float32(D32**4 - d32**4)          # QISQARISH bor
    st32 = np.float32((D32**2 + d32**2)*(D32 + d32)
                      * (np.float32(2.0)*t32))   # qisqarish YO'Q
    # Etalon: aynan shu D va t dan double da, barqaror shaklda
    d64 = D - 2*tw
    ref = (D**2 + d64**2)*(D + d64)*(2*tw)
    e_dir = abs(float(dir32) - ref)/abs(ref)*100
    e_st = abs(float(st32) - ref)/abs(ref)*100
    rows32.append([f"{tw:g}", f"{e_dir:.3e}", f"{e_st:.3e}"])
table("float32 da nisbiy xatolik (double etalonga nisbatan), %",
      ["t, mm", "to'g'ridan-to'g'ri", "barqaror (2t orqali)"], rows32)
note("Ikkala ustun ham AYNAN bir xil kirish ma'lumotidan (D va t) "
     "hisoblandi. To'g'ridan-to'g'ri ayirish devor ingichkalashgani "
     "sari tez buziladi; barqaror shaklda esa (D - d) umuman "
     "hisoblanmaydi - uning o'rniga kirishda berilgan 2*t "
     "ishlatiladi, shuning uchun qisqarish YO'Q. Ikkala ifoda "
     "MATEMATIK JIHATDAN TENG, lekin sonli jihatdan teng emas - "
     "bu sonli usullardagi asosiy tamoyillardan biri.")
note("Diqqat: agar barqaror shaklda ham (D32 - d32) sonli "
     "hisoblansa, afzallik YO'QOLADI - chunki d ning float32 da "
     "ifodalanish xatosi ayirmada baribir kuchayadi. Demak "
     "qisqarishdan qochish uchun formulani qayta yozishning o'zi "
     "yetarli emas: KICHIK KATTALIKNI kirish ma'lumoti sifatida "
     "saqlab qolish kerak.")

# --- Kvadrat tenglama ildizlari ---
aa, bb, cc = 1.0, -bq, 1.0
disc = np.sqrt(bb*bb - 4*aa*cc)
x1 = (-bb + disc)/(2*aa)            # katta ildiz - barqaror
x2_naive = (-bb - disc)/(2*aa)      # kichik ildiz - QISQARISH
x2_stable = cc/(aa*x1)              # Viet teoremasi - barqaror
value("Katta ildiz x1", x1, "—")
value("Kichik ildiz (sodda formula)", x2_naive, "—")
value("Kichik ildiz (barqaror, c/(a*x1))", x2_stable, "—")
res_naive = abs(aa*x2_naive**2 + bb*x2_naive + cc)
res_stable = abs(aa*x2_stable**2 + bb*x2_stable + cc)
value("Qoldiq |a*x^2+b*x+c| (sodda)", res_naive, "—")
value("Qoldiq |a*x^2+b*x+c| (barqaror)", res_stable, "—")
if res_naive > 0:
    value("Qoldiqlar nisbati", res_naive/max(res_stable, 1e-300), "marta")
note(f"Kichik ildiz: sodda formula {x2_naive:.12e}, barqaror formula "
     f"{x2_stable:.12e}. Tenglamaga qo'yib tekshirganda qoldiqlar "
     f"{res_naive:.3e} va {res_stable:.3e} - barqaror formula "
     f"ancha aniq. Sababi: -b - sqrt(b^2-4ac) da ikkita deyarli teng "
     f"son ayiriladi.")

# --- Yig'indi tartibi va Kahan kompensatsiyasi ---
N = min(n_sum, 2000000)
terms = np.full(N, 0.1, dtype=np.float32)
naive32 = np.float32(0.0)
for i in range(0, N, 1):
    naive32 = np.float32(naive32 + terms[i])
    if i > 200000:
        break
n_used = min(N, 200001)
exact = 0.1*n_used
value("Yig'indi hadlari soni", float(n_used), "—")
value("Aniq yig'indi", exact, "—")
value("float32 oddiy yig'indi", float(naive32), "—")
value("float32 oddiy yig'indi xatosi",
      abs(float(naive32) - exact)/exact*100, "%")

# Kahan kompensatsiyalangan yig'indi
ssum = np.float32(0.0)
comp = np.float32(0.0)
for i in range(n_used):
    y = np.float32(terms[i] - comp)
    tmp = np.float32(ssum + y)
    comp = np.float32(np.float32(tmp - ssum) - y)
    ssum = tmp
value("float32 Kahan yig'indisi", float(ssum), "—")
value("Kahan yig'indisi xatosi", abs(float(ssum) - exact)/exact*100, "%")
imp = abs(float(naive32) - exact)/max(abs(float(ssum) - exact), 1e-30)
value("Kahan qancha marta aniqroq", imp, "marta")
note(f"{n_used} ta 0.1 ni float32 da qo'shdik. Oddiy yig'indi xatosi "
     f"{abs(float(naive32)-exact)/exact*100:.4f} %, Kahan "
     f"kompensatsiyasi bilan {abs(float(ssum)-exact)/exact*100:.6f} % "
     f"- {imp:.0f} marta aniqroq. Sababi: yig'indi o'sgani sari "
     f"yangi had unga nisbatan kichrayadi va YUTILADI; Kahan "
     f"yo'qolgan qismni saqlab qo'shadi.")

table("Amaliy qoidalar",
      ["Vaziyat", "Xavf", "Yechim"],
      [["Yaqin sonlar ayirmasi", "katastrofik qisqarish",
        "formulani qayta yozish"],
       ["a + b, b << a", "yutilish", "kichikdan boshlab qo'shish"],
       ["Uzun yig'indi", "xato n bilan o'sadi", "Kahan yoki pairwise"],
       ["x == y tekshiruvi", "deyarli har doim False", "nisbiy tolerans"],
       ["Katta koordinatalar", "aniqlik yo'qoladi", "mahalliy koordinata"],
       ["float32 da nozik hisob", "7 raqam yetmaydi", "double ishlatish"]])
''',
                parameters=[
                    p("D", "Tashqi diametr D", 10.0, 2000.0, 200.0, 1.0,
                      "mm"),
                    p("t", "Devor qalinligi t", 0.001, 50.0, 1.0, 0.01,
                      "mm"),
                    p("n_sum", "Yig'indi hadlari soni", 1000.0, 2000000.0,
                      1000000.0, 1000.0),
                    p("bq", "Kvadrat tenglamadagi b koeffitsienti",
                      100.0, 1e10, 1e8, 100.0),
                ],
                expected_output=(
                    "O'lchangan epsilon aynan 2⁻⁵² = "
                    "2,22e-16 ga teng — taxminan 15,65 "
                    "ishonchli raqam. Devor ingichkalashgani "
                    "sari $D^4-d^4$ dagi kuchayish "
                    "koeffitsienti o'sadi va yo'qolgan "
                    "raqamlar soni logarifmik ortadi; "
                    "float32 da to'g'ridan-to'g'ri ayirish "
                    "buziladi, ko'paytuvchi shakl esa "
                    "barqaror qoladi (xatolik 1,5e-2 % "
                    "ga qarshi 1,1e-5 %). Kvadrat "
                    "tenglamada kichik ildiz: sodda "
                    "formula 7,45e-9, barqaror formula "
                    "aynan 1e-8 — qoldiqlar 0,255 va "
                    "1,1e-16, ya'ni 2,3e15 marta farq. "
                    "Kahan kompensatsiyasi float32 "
                    "yig'indisini 100 000 marta "
                    "aniqlashtiradi."
                ),
            ),
            visual=vis(
                kind="Aniq raqamlarning yo'qolishi",
                tool="React/SVG",
                description=(
                    "Qisqarishda qancha aniq raqam "
                    "yo'qolishi va barqaror formula bilan "
                    "taqqoslash."
                ),
                how_to_draw=(
                    "React/SVG: yuqorida ikkita son "
                    "**raqamma-raqam** gorizontal "
                    "qatorlarda ko'rsatiladi ($D^4$ va "
                    "$d^4$). Ularning bir xil "
                    "boshlanuvchi raqamlari kulrang "
                    "fonda, farq qiladigan qismi esa "
                    "yorqin rangda belgilanadi. Ayirma "
                    "olingach, natijaning faqat "
                    "**farq qilgan raqamlari** "
                    "ishonchli ekani ko'rinadi va "
                    "qolganlari savol belgisi bilan "
                    "to'ldiriladi — bu qisqarishning "
                    "eng tushunarli tasviri. Devor "
                    "qalinligi slayderi bilan bir xil "
                    "raqamlar soni o'zgaradi va "
                    "yo'qolgan raqamlar hisoblagichi "
                    "yangilanadi. Pastda log–log "
                    "grafik: yo'qolgan raqamlar soni "
                    "devor qalinligiga qarab; unga "
                    "float32 (7) va double (16) "
                    "chegaralari gorizontal chiziqlar "
                    "bilan qo'yiladi va grafik ularni "
                    "kesib o'tgan nuqtalar "
                    "belgilanadi — 'bu qalinlikdan "
                    "boshlab float32 yaroqsiz' degan "
                    "yozuv bilan."
                ),
            ),
            interp=(
                "Mashina epsilonini formuladan olmasdan, "
                "ikkiga bo'lish tsikli bilan **o'lchash** "
                "muhim: u $2^{-52}$ ga aynan teng chiqadi "
                "va bu IEEE 754 formatining bevosita "
                "tasdig'i. Assotsiativlik buzilishi esa "
                "bitta qatorda ko'rinadi: "
                "$(1+\\varepsilon/2)-1$ va "
                "$1+(\\varepsilon/2-1)$ turli natija "
                "beradi. Bu bezovta qiluvchi, lekin "
                "muhim: suzuvchi nuqta arifmetikasi "
                "maktabdagi arifmetika emas. Quvur "
                "misolidagi jadval qisqarishning "
                "amaliy o'lchovini beradi va eng "
                "ishonchli natija `float32` "
                "taqqoslashidan keladi: ikkita "
                "**matematik jihatdan teng** ifoda "
                "butunlay boshqa aniqlik beradi. "
                "To'g'ridan-to'g'ri ayirish devor "
                "ingichkalashgani sari buziladi, "
                "ko'paytuvchi shakl esa barqaror "
                "qoladi. Bu su-01 dagi 'yaxlitlash "
                "xatoligi' tushunchasini aniq "
                "mexanizmga bog'laydi. Kvadrat "
                "tenglama misolida esa tekshiruv "
                "usuli diqqatga sazovor: ildizni "
                "tenglamaga qaytarib qo'yib qoldiq "
                "hisoblanadi. Bu sonli usullardagi "
                "universal tekshiruv — javobni "
                "boshlang'ich tenglamaga qo'yish. "
                "Nihoyat, Kahan yig'indisi "
                "xatolikning $n$ ga bog'liqligini "
                "yo'qotadi va bu uzoq vaqtli "
                "integrallashda (su-11) hal qiluvchi "
                "bo'ladi."
            ),
            mistakes=[
                "Aniqlikni oshirish (`double` dan "
                "`long double` ga) bilan qisqarishni "
                "hal qilishga urinish. U faqat "
                "muammoni kechiktiradi; formulani "
                "qayta yozish kerak.",
                "Suzuvchi nuqta sonlarini `==` bilan "
                "solishtirish. Nisbiy tolerans bilan "
                "tekshiring.",
                "Uzun yig'indida hadlarni ixtiyoriy "
                "tartibda qo'shish. Kichiklardan "
                "boshlash yoki Kahan kompensatsiyasi "
                "aniqlikni sezilarli oshiradi.",
                "Global koordinatalarda ishlash. "
                "$x \\approx 5\\times10^5$ m da mm "
                "aniqligi nisbiy $10^{-9}$ — "
                "`float32` uchun yo'qolgan.",
                "Qisqarish 'yangi xato yaratadi' deb "
                "o'ylash. U mavjud xatoni faqat "
                "ko'rinarli qiladi — shuning uchun "
                "kirish ma'lumotining aniqligi ham "
                "muhim.",
            ],
            quiz=[
                q("Mashina epsiloni nima va `double` "
                  "uchun u nechaga teng?",
                  "$1$ dan katta eng kichik son bilan "
                  "$1$ orasidagi farq; "
                  "$2^{-52} \\approx 2{,}22\\times"
                  "10^{-16}$, ya'ni ~16 o'nlik raqam.",
                  "konseptual"),
                q("Qaysi amal katastrofik qisqarish "
                  "beradi va nima uchun?",
                  "Yaqin sonlarni ayirish: nisbiy "
                  "xatolik $(|x|+|y|)/|x-y|$ marta "
                  "kuchayadi, chunki natija kichik "
                  "bo'lgani uchun mavjud mutlaq xato "
                  "nisbatan kattalashadi.",
                  "konseptual"),
                q("$D = 100$, $d = 99{,}9$ bo'lsa "
                  "$D^2-d^2$ da nechta raqam "
                  "yo'qoladi?",
                  "$D^2 = 10000$, $d^2 = 9980{,}01$, "
                  "ayirma $19{,}99$. Nisbat "
                  "$19980/19{,}99 = 999{,}5$, "
                  "$\\log_{10} \\approx 3$ — "
                  "taxminan 3 raqam.", "hisob"),
                q("Kodda nima uchun bir xil hisob "
                  "`float32` da ham takrorlanadi?",
                  "`double` da qisqarish ta'siri "
                  "ko'rinmay qolishi mumkin; "
                  "`float32` (7 raqam) da esa u "
                  "aniq namoyon bo'ladi va ikki "
                  "formulaning farqi o'lchanadi.",
                  "kod"),
                q("Kvadrat tenglamaning kichik "
                  "ildizini qanday barqaror hisoblash "
                  "mumkin?",
                  "Katta ildizni barqaror formuladan "
                  "topib, kichigini Viet teoremasidan "
                  "$x_2 = c/(a x_1)$ orqali olish — "
                  "qisqarish butunlay yo'qoladi.",
                  "talqin"),
                q("Kahan kompensatsiyasi nimani "
                  "yaxshilaydi?",
                  "Uzun yig'indida yutilish tufayli "
                  "yo'qolgan kichik qismlarni saqlab "
                  "qo'shadi; xatolik $n$ ga bog'liq "
                  "bo'lmay qoladi.", "talqin"),
            ],
            bridge=(
                "Yaxlitlash xatoligi kompyuterning "
                "chekli aniqligidan kelib chiqadi va "
                "biz undan qochish yo'llarini ko'rdik. "
                "Ikkinchi xatolik turi butunlay boshqa "
                "manbadan: uzluksiz matematik amalni "
                "(hosila, integral) chekli ayirma bilan "
                "almashtirishdan. Keyingi mavzuda "
                "Teylor qatori orqali bu kesish "
                "xatoligini aniq ifodalaymiz va ikki "
                "xatolikning raqobati sonli hosilada "
                "optimal qadam berishini ko'rsatamiz."
            ),
            research=(
                "Aniqlik masalalarini chuqurroq "
                "o'rganing. (1) Kompensatsiyalangan "
                "yig'indi algoritmlarini (Kahan, "
                "Kahan–Babuška–Neumaier, juftlab "
                "yig'indi) taqqoslang va ularning "
                "xatolik chegaralarini isbotlang. "
                "(2) Interval arifmetikasini "
                "o'rganing: u natijaning kafolatlangan "
                "chegaralarini beradi, lekin "
                "intervallar haddan tashqari "
                "kengayishi mumkin — nima uchun? "
                "(3) Mashinali o'qitishda keng "
                "tarqalgan `float16` va `bfloat16` "
                "formatlarini tahlil qiling: nima "
                "uchun ular neyron tarmoqlar uchun "
                "yetarli, lekin FEM uchun yaroqsiz? "
                "(4) Takrorlanuvchi (reproducible) "
                "parallel yig'indi muammosini "
                "ko'rib chiqing."
            ),
            manim_ref=manim(
                scene="CancellationScene",
                module="manim/scenes/su_basics.py",
                title="Katastrofik qisqarish",
                summary=(
                    "Ikkita yaqin son raqamma-raqam "
                    "ko'rsatiladi; bir xil raqamlar "
                    "so'niydi va ayirma olingach "
                    "faqat bir nechta ishonchli raqam "
                    "qolgani ko'rinadi. Keyin "
                    "ko'paytuvchi shakl qo'llanadi va "
                    "barcha raqamlar saqlanib "
                    "qolishi namoyish etiladi."
                ),
            ),
        ),
    ),

    # ------------------------------------------------------------------ su-03
    Topic(
        id="su-03",
        subject_id=S, module_id=M, order=3,
        title="Kesish xatoligi, Teylor qatori va yaqinlashish tartibi",
        description=(
            "Teylor yoyilmasi orqali ayirma sxemalarining xatoligini "
            "chiqarish, yaqinlashish tartibi, sonli hosilada optimal "
            "qadam va Richardson ekstrapolyatsiyasi."
        ),
        learning_objective=(
            "Ayirma sxemasining kesish xatoligini Teylor qatoridan "
            "chiqarish, yaqinlashish tartibini sonli o'lchash va "
            "Richardson ekstrapolyatsiyasi bilan aniqlikni oshirish."
        ),
        prerequisites=["su-02", "pq-10"],
        mathematical_core=(
            "$f'(x) = \\dfrac{f(x+h)-f(x-h)}{2h} - "
            "\\dfrac{h^2}{6}f'''(\\xi)$; "
            "$E(h) = C h^p + \\dfrac{\\varepsilon}{h}$, "
            "$h_{opt} \\sim \\varepsilon^{1/(p+1)}$."
        ),
        engineering_application=(
            "Sonli hosila orqali sezgirlik tahlili, Yakobian "
            "matritsasini sonli qurish, optimallashtirish gradiyentlari, "
            "eksperimental ma'lumotdan deformatsiyani hisoblash."
        ),
        computational_component=(
            "Kesish va yaxlitlash xatoliklarining raqobatini o'lchash, "
            "optimal qadamni topish va Richardson ekstrapolyatsiyasini "
            "qo'llash."
        ),
        visualization_component=(
            "Log–log grafikda ikki xatolikning V shaklidagi yig'indisi, "
            "nazariy qiyaliklar bilan taqqoslash."
        ),
        research_extension=(
            "Kompleks qadam usuli (complex-step derivative) nima uchun "
            "qisqarishdan butunlay xoli? Uni avtomatik "
            "differensiallash (AD) bilan solishtiring."
        ),
        difficulty="asosiy",
        previous_link=(
            "su-02 da yaxlitlash xatoligi va katastrofik qisqarish "
            "o'rganildi. Sonli hosilada aynan shu ikkisi uchrashadi: "
            "surat $f(x+h)-f(x)$ qisqarish beradi, maxraj $h$ esa "
            "uni yanada kuchaytiradi."
        ),
        next_topic="su-04",
        estimated_minutes=85,
        tags=["Teylor", "kesish xatoligi", "Richardson", "optimal qadam"],
        lesson=_lesson(
            problem=(
                "Konstruksiyaning yuklamaga sezgirligini "
                "baholash kerak: $\\partial w/\\partial h$ — "
                "og'ishning qalinlikka bog'liqligi. "
                "Analitik hosila murakkab yoki mavjud "
                "emas (FEM natijasi uchun umuman yo'q), "
                "shuning uchun sonli hosila olamiz: "
                "$(w(h+\\Delta)-w(h))/\\Delta$. Mantiq "
                "shuni aytadiki, $\\Delta$ qancha kichik "
                "bo'lsa, natija shuncha aniq. Lekin "
                "$\\Delta$ ni kichraytirganda xatolik "
                "avval kamayadi, keyin **ortib ketadi** "
                "va $\\Delta = 10^{-16}$ da javob "
                "butunlay ma'nosiz bo'ladi. Ikki "
                "xatolikning raqobati bu — va uning "
                "optimal nuqtasini aniq hisoblash mumkin."
            ),
            concepts=[
                c("Kesish xatoligi (truncation error)",
                  "Teylor qatorini chekli sondagi hadda "
                  "to'xtatishdan kelib chiqadi; "
                  "$h \\to 0$ da nolga intiladi."),
                c("Yaqinlashish tartibi $p$",
                  "$E \\sim Ch^p$ dagi daraja; $p$ katta "
                  "bo'lsa qadamni kamaytirish tezroq "
                  "samara beradi."),
                c("Markaziy ayirma",
                  "$(f(x+h)-f(x-h))/2h$ — ikkinchi "
                  "tartibli, chunki toq hadlar "
                  "o'zaro qisqaradi."),
                c("Optimal qadam",
                  "Kesish ($\\sim h^p$) va yaxlitlash "
                  "($\\sim \\varepsilon/h$) xatoliklarining "
                  "yig'indisi minimal bo'ladigan $h$."),
                c("Richardson ekstrapolyatsiyasi",
                  "Ikki qadamdagi natijadan yetakchi "
                  "xatolik hadini yo'qotish; tartibni "
                  "$p$ dan $p+2$ ga ko'taradi."),
                c("Kompleks qadam usuli",
                  "$f'(x) \\approx \\mathrm{Im}[f(x+ih)]/h$ "
                  "— ayirish yo'q, demak qisqarish ham "
                  "yo'q; $h$ ni ixtiyoriy kichik olish "
                  "mumkin."),
            ],
            derivation=[
                d("1. Teylor yoyilmasi",
                  r"f(x+h) = f(x) + hf'(x) + "
                  r"\frac{h^2}{2}f''(x) + "
                  r"\frac{h^3}{6}f'''(x) + O(h^4)",
                  "Barcha ayirma sxemalarining manbasi. "
                  "$f$ yetarlicha silliq deb faraz "
                  "qilinadi."),
                d("2. Oldinga ayirma",
                  r"\frac{f(x+h)-f(x)}{h} = f'(x) + "
                  r"\frac{h}{2}f''(x) + O(h^2)",
                  "Yetakchi xatolik hadi $\\frac{h}{2}f''$ "
                  "— **birinchi tartibli** ($p = 1$). "
                  "Qadamni ikki barobar kamaytirish "
                  "xatoni ikki barobar kamaytiradi."),
                d("3. Orqaga yoyilma",
                  r"f(x-h) = f(x) - hf'(x) + "
                  r"\frac{h^2}{2}f''(x) - "
                  r"\frac{h^3}{6}f'''(x) + O(h^4)",
                  "Toq darajali hadlar ishorasini "
                  "o'zgartiradi — bu keyingi qadamning "
                  "kaliti."),
                d("4. Markaziy ayirma",
                  r"\frac{f(x+h)-f(x-h)}{2h} = f'(x) + "
                  r"\frac{h^2}{6}f'''(x) + O(h^4)",
                  "**Juft hadlar o'zaro qisqardi.** "
                  "Endi yetakchi xatolik "
                  "$\\frac{h^2}{6}f'''$ — **ikkinchi "
                  "tartibli**. Bir xil sondagi "
                  "hisoblash bilan ancha aniqroq."),
                d("5. Ikkinchi hosila uchun sxema",
                  r"\frac{f(x+h)-2f(x)+f(x-h)}{h^2} = "
                  r"f''(x) + \frac{h^2}{12}f^{(4)}(x) "
                  r"+ O(h^4)",
                  "Ikkala yoyilmani qo'shsak toq hadlar "
                  "qisqaradi. Bu pq-10 va su-01 da "
                  "ishlatilgan sxema — uning "
                  "$O(h^2)$ ekani shundan."),
                d("6. Yaxlitlash xatoligining kirishi",
                  r"\tilde f(x\pm h) = f(x\pm h)(1+\delta), "
                  r"\quad |\delta| \le \varepsilon",
                  "Hisoblangan qiymatlar aniq emas. "
                  "Ularning ayirmasi su-02 dagi "
                  "qisqarishga duch keladi."),
                d("7. Yaxlitlashning hosiladagi ta'siri",
                  r"\Big|\frac{\tilde f(x+h)-\tilde f(x-h)}"
                  r"{2h} - \frac{f(x+h)-f(x-h)}{2h}\Big| "
                  r"\le \frac{\varepsilon|f|}{h}",
                  "**Hal qiluvchi natija.** Xatolik "
                  "$h$ ga **teskari** mutanosib. "
                  "Qadam kichrayganda u ortadi — "
                  "kesish xatoligining aksincha."),
                d("8. Umumiy xatolik va uning minimumi",
                  r"E(h) = \frac{h^2}{6}|f'''| + "
                  r"\frac{\varepsilon|f|}{h}",
                  "Ikki qarama-qarshi had — su-01 dagi, "
                  "pq-29 va pq-30 dagi bilan bir xil "
                  "tuzilma."),
                d("9. Optimal qadam",
                  r"\frac{dE}{dh} = 0 \;\Longrightarrow\; "
                  r"h_{opt} = \Big(\frac{3\varepsilon|f|}"
                  r"{|f'''|}\Big)^{1/3} \sim "
                  r"\varepsilon^{1/3}",
                  "`double` uchun "
                  "$\\varepsilon^{1/3} \\approx "
                  "6\\times10^{-6}$. Oldinga ayirma "
                  "uchun esa $h_{opt} \\sim "
                  "\\varepsilon^{1/2} \\approx "
                  "1{,}5\\times10^{-8}$."),
                d("10. Erishish mumkin bo'lgan eng "
                  "yaxshi aniqlik",
                  r"E(h_{opt}) \sim \varepsilon^{2/3} "
                  r"\approx 4\times10^{-11}",
                  "Markaziy ayirma bilan 16 "
                  "raqamdan atigi **11 tasi** "
                  "qoladi. Oldinga ayirmada esa "
                  "$\\varepsilon^{1/2} \\approx "
                  "10^{-8}$ — 8 ta raqam. Sonli "
                  "hosila hech qachon to'liq "
                  "aniqlik bermaydi."),
                d("11. Richardson ekstrapolyatsiyasi",
                  r"D(h) = f' + Ch^2 + \ldots; \quad "
                  r"\frac{4D(h/2) - D(h)}{3} = f' + "
                  r"O(h^4)",
                  "$D(h)$ va $D(h/2)$ dan $Ch^2$ "
                  "hadini yo'qotamiz. Tartib 2 dan "
                  "4 ga ko'tariladi — pq-10 da shu "
                  "usul ishlatilgan edi."),
                d("12. Kompleks qadam usuli",
                  r"f(x+ih) = f(x) + ihf'(x) - "
                  r"\frac{h^2}{2}f''(x) + \ldots "
                  r"\;\Longrightarrow\; f'(x) = "
                  r"\frac{\mathrm{Im}\,f(x+ih)}{h} + O(h^2)",
                  "**Ayirish umuman yo'q** — mavhum "
                  "qismni olish kifoya. Demak "
                  "qisqarish yo'q va $h$ ni "
                  "$10^{-30}$ qilib olsa ham "
                  "bo'ladi. Faqat $f$ analitik "
                  "bo'lishi kerak."),
            ],
            meaning=(
                "Bu mavzuning markaziy g'oyasi — Teylor "
                "qatori barcha ayirma sxemalarining "
                "yagona manbai ekani. Sxemani qurish "
                "uchun yoyilmalarni shunday "
                "kombinatsiyalash kerakki, keraksiz "
                "hadlar o'zaro qisqarsin: markaziy "
                "ayirmada juft hadlar, ikkinchi hosila "
                "sxemasida toq hadlar qisqaradi. Qolgan "
                "birinchi had yetakchi xatolikni va "
                "yaqinlashish tartibini belgilaydi. "
                "Ikkinchi va amaliy jihatdan muhimroq "
                "g'oya — 8-qadamdagi raqobat. Kesish "
                "xatoligi $h$ bilan kamayadi, "
                "yaxlitlash xatoligi esa $1/h$ bilan "
                "ortadi. Natijada **optimal qadam** "
                "mavjud va undan kichik qadam olish "
                "aniqlikni yomonlashtiradi. Bu "
                "intuitivga zid: 'qadam qancha kichik "
                "bo'lsa, shuncha yaxshi' degan tabiiy "
                "fikr noto'g'ri. Yana bir muhim xulosa — "
                "sonli hosila hech qachon to'liq "
                "aniqlik bermaydi: markaziy ayirmada "
                "16 raqamdan 11 tasi, oldinga ayirmada "
                "8 tasi qoladi. Shuning uchun "
                "optimallashtirish va Nyuton usulida "
                "(su-24) Yakobianni sonli qurish "
                "yaqinlashishni sekinlashtiradi. Ikkita "
                "chiqish yo'li bor. Richardson "
                "ekstrapolyatsiyasi — bir xil "
                "hisoblashdan ko'proq aniqlik siqib "
                "chiqarish: ikki qadamdagi natijadan "
                "yetakchi xatolik hadini yo'qotish "
                "orqali tartibni ko'tarish. Bu pq-10 "
                "da plastina masalasida qo'llanilgan "
                "va xatolikni 0,020 % dan 0,0005 % ga "
                "tushirgan edi. Ikkinchi yo'l — "
                "kompleks qadam usuli: u ayirishni "
                "butunlay chetlab o'tadi, shuning "
                "uchun qisqarish yo'q va qadamni "
                "ixtiyoriy kichik olish mumkin. "
                "Natijada mashina aniqligiga yetadigan "
                "hosila olinadi. Cheklovi — $f$ "
                "analitik bo'lishi va kod kompleks "
                "sonlar bilan ishlay olishi kerak."
            ),
            equations=[
                eq(r"\frac{f(x+h)-f(x-h)}{2h} = f'(x) + "
                   r"\frac{h^2}{6}f'''(\xi)",
                   "Markaziy ayirma — ikkinchi tartibli "
                   "birinchi hosila sxemasi.",
                   "Markaziy ayirma"),
                eq(r"\frac{f(x+h)-2f(x)+f(x-h)}{h^2} = "
                   r"f''(x) + \frac{h^2}{12}f^{(4)}(\xi)",
                   "Ikkinchi hosila uchun uch nuqtali "
                   "sxema.", "Ikkinchi hosila"),
                eq(r"h_{opt} = \Big(\frac{3\varepsilon|f|}"
                   r"{|f'''|}\Big)^{1/3}, \quad "
                   r"E_{min} \sim \varepsilon^{2/3}",
                   "Markaziy ayirma uchun optimal qadam "
                   "va erishish mumkin bo'lgan eng yaxshi "
                   "aniqlik.", "Optimal qadam"),
                eq(r"D_{R} = \frac{2^p D(h/2) - D(h)}"
                   r"{2^p - 1}",
                   "Richardson ekstrapolyatsiyasi: "
                   "$p$-tartibli sxemadan yuqori "
                   "tartibli natija.",
                   "Richardson ekstrapolyatsiyasi"),
            ],
            conditions=(
                "**Teylor yoyilmasining shartlari:** "
                "$f$ kerakli tartibda uzluksiz "
                "differensiallanuvchi bo'lishi kerak. "
                "Agar $f$ uzilishli yoki burchakli "
                "bo'lsa (kontakt, yorilish, plastiklik "
                "chegarasi), yaqinlashish tartibi "
                "**pasayadi** va nazariy baho "
                "o'rinsiz bo'lib qoladi.\n\n"
                "**Qadam tanlash bo'yicha amaliy "
                "tavsiyalar:**\n"
                "- Markaziy ayirma: "
                "$h \\approx \\varepsilon^{1/3}|x| "
                "\\approx 6\\times10^{-6}|x|$;\n"
                "- Oldinga ayirma: "
                "$h \\approx \\varepsilon^{1/2}|x| "
                "\\approx 1{,}5\\times10^{-8}|x|$;\n"
                "- Qadam **nisbiy** bo'lsin: "
                "$h = \\eta\\,\\max(|x|, x_{tip})$;\n"
                "- $x = 0$ atrofida mutlaq qadam "
                "kerak.\n\n"
                "**Richardson uchun shart:** xatolik "
                "asimptotik rejimda bo'lishi kerak, "
                "ya'ni $h$ yetarlicha kichik va "
                "yaxlitlash hali hukmron emas. "
                "Aks holda ekstrapolyatsiya "
                "**yomonlashtiradi**.\n\n"
                "**Kompleks qadam uchun:** $f$ "
                "analitik bo'lishi va kodda "
                "`abs`, `max`, `min` kabi "
                "analitik bo'lmagan amallar "
                "to'g'ri ishlanishi kerak."
            ),
            worked=WorkedExample(
                statement=(
                    "$f(x) = \\sin x$ funksiyasining "
                    "$x = 1$ dagi hosilasini "
                    "($f'(1) = \\cos 1 = 0{,}5403023$) "
                    "oldinga va markaziy ayirma bilan "
                    "hisoblang. Ikkala usul uchun "
                    "optimal qadamni va erishish mumkin "
                    "bo'lgan eng yaxshi aniqlikni "
                    "baholang. Richardson "
                    "ekstrapolyatsiyasi nima beradi?"
                ),
                given=[
                    r"f(x) = \sin x,\ x = 1,\ "
                    r"f'(1) = \cos 1 = 0{,}5403023059",
                    r"\varepsilon = 2{,}22\times10^{-16}",
                ],
                steps=[
                    st(r"\text{Oldinga: } E(h) = "
                       r"\frac{h}{2}|f''| + "
                       r"\frac{\varepsilon|f|}{h}, \quad "
                       r"|f''(1)| = |\sin 1| = 0{,}8415",
                       "8-qadamdagi ifodaning birinchi "
                       "tartibli varianti."),
                    st(r"h_{opt} = \sqrt{\frac{2\varepsilon|f|}"
                       r"{|f''|}} = \sqrt{2 \cdot "
                       r"2{,}22\times10^{-16}} = "
                       r"2{,}11\times10^{-8}",
                       "$|f| = |\\sin 1| = 0{,}8415$ va "
                       "$|f''| = 0{,}8415$ — teng, "
                       "shuning uchun qisqaradi."),
                    st(r"E_{min} \approx \sqrt{2\varepsilon "
                       r"|f||f''|}/|f'| \approx "
                       r"3\times10^{-8} \;\Rightarrow\; "
                       r"\text{taxminan } 8 \text{ ta aniq raqam}",
                       "Bu eng yomon holat bahosi; kodda "
                       "o'lchangan qiymat "
                       "$1{,}1\\times10^{-9}$ — nazariy "
                       "chegaradan yaxshiroq, chunki "
                       "baho $|\\delta|$ ning maksimal "
                       "qiymatiga qurilgan."),
                    st(r"\text{Markaziy: } E(h) = "
                       r"\frac{h^2}{6}|f'''| + "
                       r"\frac{\varepsilon|f|}{h}, \quad "
                       r"|f'''(1)| = |\cos 1| = 0{,}5403",
                       "Ikkinchi tartibli sxema."),
                    st(r"h_{opt} = \Big(\frac{3\varepsilon|f|}"
                       r"{|f'''|}\Big)^{1/3} = "
                       r"\Big(\frac{3 \cdot 2{,}22\times"
                       r"10^{-16} \cdot 0{,}8415}"
                       r"{0{,}5403}\Big)^{1/3}",
                       "Kub ildiz — 9-qadamdagi formula."),
                    st(r"= (1{,}037\times10^{-15})^{1/3} = "
                       r"1{,}012\times10^{-5}",
                       "Oldinga ayirmadagidan **taxminan "
                       "500 barobar katta** qadam. "
                       "Intuitivga zid, lekin to'g'ri."),
                    st(r"E_{min} \sim \varepsilon^{2/3} "
                       r"\approx 4\times10^{-11}",
                       "Kodda o'lchangan qiymat "
                       "$2{,}6\\times10^{-13}$ — oldinga "
                       "ayirmadan **4300 marta** aniqroq, "
                       "garchi qadam 900 marta katta "
                       "bo'lsa ham."),
                    st(r"\text{Richardson: } D(h) = "
                       r"f' + Ch^2; \quad D_R = "
                       r"\frac{4D(h/2)-D(h)}{3} = "
                       r"f' + O(h^4)",
                       "$p = 2$ uchun $2^p = 4$."),
                    st(r"h = 10^{-2}: \ D(h) \ \text{xatosi} "
                       r"\sim \frac{h^2}{6}\frac{|f'''|}{|f'|} "
                       r"= \frac{10^{-4}}{6} = 1{,}7\times10^{-5}",
                       "Ekstrapolyatsiyadan oldin "
                       "($|f'''| = |f'|$ bo'lgani uchun "
                       "nisbat qisqaradi)."),
                    st(r"D_R \ \text{xatosi} \sim O(h^4) "
                       r"\approx 10^{-9} \ \text{tartibida}",
                       "**To'rt tartibga yaxshilanish** — "
                       "va buning uchun atigi bitta "
                       "qo'shimcha hisoblash kerak "
                       "bo'ldi. Kodda aniq o'lchanadi."),
                ],
                answer=(
                    "Oldinga ayirma: "
                    "$h_{opt} \\approx 2{,}1\\times10^{-8}$, "
                    "$E_{min} \\sim \\varepsilon^{1/2} "
                    "\\approx 10^{-8}$ (~8 aniq raqam). "
                    "Markaziy ayirma: "
                    "$h_{opt} \\approx 1{,}0\\times10^{-5}$ "
                    "(taxminan 500 barobar **katta**), "
                    "$E_{min} \\sim \\varepsilon^{2/3} "
                    "\\approx 4\\times10^{-11}$ (~11 aniq "
                    "raqam). Kodda o'lchangan tartiblar "
                    "1,00037 va 2,00001; markaziy "
                    "ayirma qadami 912 marta katta "
                    "bo'lsa ham 4293 marta aniqroq. "
                    "Richardson ekstrapolyatsiyasi "
                    "tartibni 2 dan 4,006 ga ko'taradi "
                    "va $h = 10^{-2}$ da xatolikni "
                    "798 600 marta kamaytiradi."
                ),
                engineering_note=(
                    "Amaliy jihatdan eng muhim xulosa — "
                    "optimal qadam **kutilgandan ancha "
                    "katta**. Muhandislar odatda "
                    "$h = 10^{-10}$ yoki undan ham "
                    "kichik qadam oladi va natija "
                    "yomonlashganini ko'rib hayron "
                    "bo'ladi. Markaziy ayirma uchun "
                    "to'g'ri qadam $10^{-5}$ "
                    "atrofida — ya'ni argumentning "
                    "yuz mingdan bir qismi. Yana bir "
                    "amaliy nuqta: qadam **nisbiy** "
                    "bo'lishi kerak. $x = 10^6$ "
                    "bo'lsa $h = 10^{-5}$ mutlaq qadam "
                    "$x$ ning $10^{-11}$ qismi — "
                    "butunlay yo'qoladi. To'g'ri "
                    "yo'l: $h = \\eta\\max(|x|, "
                    "x_{tip})$, $\\eta \\approx "
                    "10^{-5}$. FEM da sezgirlik "
                    "tahlili uchun esa sonli hosila "
                    "umuman ishlatilmasligi afzal: "
                    "analitik sezgirlik (adjoint usul) "
                    "yoki avtomatik differensiallash "
                    "mashina aniqligida natija beradi "
                    "va qadam tanlash muammosini "
                    "butunlay yo'q qiladi."
                ),
            ),
            computation=Computation(
                caption=(
                    "Kesish va yaxlitlash xatoliklarining "
                    "raqobatini o'lchash, optimal qadamni "
                    "topish, Richardson va kompleks qadam "
                    "usullarini taqqoslash."
                ),
                code='''"""Kesish xatoligi, optimal qadam va Richardson ekstrapolyatsiyasi."""
import numpy as np
from labkit import PARAMS, note, series, table, value

x0 = float(PARAMS.get("x0", 1.0))
fn = int(PARAMS.get("fn", 0))        # 0 sin, 1 exp, 2 x^3*ln(x)
h_rich = float(PARAMS.get("h_rich", 0.01))


if fn == 0:
    def f(t):
        return np.sin(t)

    def fc(z):
        return np.sin(z)

    fp, f2, f3 = np.cos(x0), -np.sin(x0), -np.cos(x0)
    name = "sin(x)"
elif fn == 1:
    def f(t):
        return np.exp(t)

    def fc(z):
        return np.exp(z)

    fp = f2 = f3 = np.exp(x0)
    name = "exp(x)"
else:
    def f(t):
        return t**3*np.log(t)

    def fc(z):
        return z**3*np.log(z)

    fp = 3*x0**2*np.log(x0) + x0**2
    f2 = 6*x0*np.log(x0) + 5*x0
    f3 = 6*np.log(x0) + 11.0
    name = "x^3*ln(x)"

eps = np.finfo(float).eps
value("Funksiya kodi", float(fn), "—")
value("Aniq hosila f'(x0)", fp, "—")
note(f"Funksiya: {name}, nuqta x0 = {x0}. Aniq hosila {fp:.12f}.")

# --- Ikki sxemani qadam bo'yicha supurish ---
hs = np.logspace(-16, -1, 300)
e_fwd, e_cen = [], []
for h in hs:
    d_f = (f(x0 + h) - f(x0))/h
    d_c = (f(x0 + h) - f(x0 - h))/(2*h)
    e_fwd.append(abs(d_f - fp)/abs(fp))
    e_cen.append(abs(d_c - fp)/abs(fp))
e_fwd = np.array(e_fwd)
e_cen = np.array(e_cen)
series("Oldinga ayirma xatoligi", hs.tolist(),
       np.maximum(e_fwd, 1e-18).tolist(),
       xlabel="qadam h", ylabel="nisbiy xatolik")
series("Markaziy ayirma xatoligi", hs.tolist(),
       np.maximum(e_cen, 1e-18).tolist(),
       xlabel="qadam h", ylabel="nisbiy xatolik")

i_f = int(np.argmin(e_fwd))
i_c = int(np.argmin(e_cen))
value("Oldinga: optimal h (o'lchangan)", float(hs[i_f]), "—")
value("Oldinga: eng kichik xatolik", float(e_fwd[i_f]), "—")
value("Markaziy: optimal h (o'lchangan)", float(hs[i_c]), "—")
value("Markaziy: eng kichik xatolik", float(e_cen[i_c]), "—")
value("Markaziy qadam oldingidan necha marta katta",
      float(hs[i_c]/hs[i_f]), "marta")
value("Markaziy necha marta aniqroq",
      float(e_fwd[i_f]/max(e_cen[i_c], 1e-300)), "marta")

# Nazariy bashoratlar
h_f_th = np.sqrt(2*eps*abs(f(x0))/abs(f2))
h_c_th = (3*eps*abs(f(x0))/abs(f3))**(1/3)
value("Oldinga: optimal h (nazariy)", h_f_th, "—")
value("Markaziy: optimal h (nazariy)", h_c_th, "—")
value("Oldinga: o'lchangan/nazariy", float(hs[i_f])/h_f_th, "—")
value("Markaziy: o'lchangan/nazariy", float(hs[i_c])/h_c_th, "—")
note(f"Nazariy optimal qadamlar: oldinga {h_f_th:.3e}, markaziy "
     f"{h_c_th:.3e}. O'lchangan qiymatlar {hs[i_f]:.3e} va "
     f"{hs[i_c]:.3e}. Nazariya eng yomon holatga mo'ljallangani "
     f"uchun aniq moslik kutilmaydi, lekin TARTIB to'g'ri "
     f"bashorat qilinadi - amaliyotda muhimi ham shu.")
note(f"MUHIM: markaziy ayirmaning optimal qadami oldingidan "
     f"{hs[i_c]/hs[i_f]:.0f} marta KATTA, lekin natija "
     f"{e_fwd[i_f]/max(e_cen[i_c], 1e-300):.0f} marta ANIQROQ. "
     f"'Qadam qancha kichik bo'lsa shuncha yaxshi' degan "
     f"intuitsiya noto'g'ri.")

# --- Qiyaliklarni o'lchash: kesish rejimida ---
mask = (hs > 1e-4) & (hs < 1e-2)
sl_f = np.polyfit(np.log(hs[mask]), np.log(e_fwd[mask]), 1)[0]
sl_c = np.polyfit(np.log(hs[mask]), np.log(e_cen[mask]), 1)[0]
value("Oldinga ayirma tartibi p (o'lchangan)", float(sl_f), "—")
value("Markaziy ayirma tartibi p (o'lchangan)", float(sl_c), "—")
note(f"Kesish rejimida (h = 1e-4...1e-2) log-log qiyaliklar: "
     f"oldinga {sl_f:.3f} ~ 1, markaziy {sl_c:.3f} ~ 2. Teylor "
     f"qatoridan chiqarilgan tartiblar sonli tasdiqlandi.")

# Yaxlitlash rejimidagi qiyalik
mask2 = (hs > 1e-15) & (hs < 1e-12)
sl_r = np.polyfit(np.log(hs[mask2]), np.log(e_cen[mask2]), 1)[0]
value("Yaxlitlash rejimidagi qiyalik", float(sl_r), "—")
note(f"Juda kichik qadamlarda qiyalik {sl_r:.2f} ~ -1, ya'ni "
     f"xatolik 1/h kabi ORTADI. Bu 7-qadamdagi bashoratning "
     f"tasdig'i va log-log grafikdagi V shaklining chap tarmog'i.")

# --- Richardson ekstrapolyatsiyasi ---
rows = []
for h in [h_rich*4, h_rich*2, h_rich, h_rich/2, h_rich/4]:
    d1 = (f(x0 + h) - f(x0 - h))/(2*h)
    d2 = (f(x0 + h/2) - f(x0 - h/2))/h
    dR = (4*d2 - d1)/3
    rows.append([f"{h:.2e}", f"{abs(d1-fp)/abs(fp):.3e}",
                 f"{abs(d2-fp)/abs(fp):.3e}",
                 f"{abs(dR-fp)/abs(fp):.3e}"])
table("Richardson ekstrapolyatsiyasi (markaziy ayirma, p = 2 -> 4)",
      ["h", "D(h) xatosi", "D(h/2) xatosi", "Richardson xatosi"], rows)

hh = np.array([h_rich*4, h_rich*2, h_rich, h_rich/2])
eR = []
for h in hh:
    d1 = (f(x0 + h) - f(x0 - h))/(2*h)
    d2 = (f(x0 + h/2) - f(x0 - h/2))/h
    eR.append(abs((4*d2 - d1)/3 - fp)/abs(fp))
eR = np.array(eR)
if np.all(eR > 1e-14):
    pR = np.polyfit(np.log(hh), np.log(eR), 1)[0]
    value("Richardson natijasining tartibi", float(pR), "—")
    note(f"Richardson natijasining o'lchangan tartibi {pR:.2f} ~ 4 - "
         f"ya'ni tartib 2 dan 4 ga ko'tarildi. Buning uchun atigi "
         f"bitta qo'shimcha funksiya hisoblash kerak bo'ldi. "
         f"pq-10 da aynan shu usul plastina masalasida ishlatilgan.")
else:
    note("Richardson natijasi mashina aniqligiga yetdi - tartibni "
         "ishonchli o'lchash uchun kattaroq qadamlar kerak.")

d1_s = (f(x0 + h_rich) - f(x0 - h_rich))/(2*h_rich)
d2_s = (f(x0 + h_rich/2) - f(x0 - h_rich/2))/h_rich
dR_s = (4*d2_s - d1_s)/3
value("D(h) xatosi", abs(d1_s - fp)/abs(fp), "—")
value("Richardson xatosi", abs(dR_s - fp)/abs(fp), "—")
value("Richardson yaxshilanishi",
      abs(d1_s - fp)/max(abs(dR_s - fp), 1e-300), "marta")

# --- Kompleks qadam usuli ---
e_cs = []
for h in hs:
    d_cs = np.imag(fc(complex(x0, h)))/h
    e_cs.append(abs(d_cs - fp)/abs(fp))
e_cs = np.array(e_cs)
series("Kompleks qadam usuli xatoligi", hs.tolist(),
       np.maximum(e_cs, 1e-18).tolist(),
       xlabel="qadam h", ylabel="nisbiy xatolik")
value("Kompleks qadam: eng kichik xatolik", float(e_cs.min()), "—")
value("Kompleks qadam: h = 1e-16 dagi xatolik", float(e_cs[0]), "—")
value("Markaziy ayirma: h = 1e-16 dagi xatolik", float(e_cen[0]), "—")
if e_cs[0] > 0:
    value("Kompleks qadam necha marta aniqroq (h = 1e-16)",
          float(e_cen[0]/e_cs[0]), "marta")
note(f"Kompleks qadam usulida h = {hs[0]:.0e} da ham xatolik "
     f"{e_cs[0]:.3e} - ya'ni mashina aniqligida. Markaziy ayirma "
     f"esa shu qadamda {e_cen[0]:.3e} xatolik beradi. Sababi: "
     f"kompleks qadamda AYIRISH umuman yo'q, faqat mavhum qism "
     f"olinadi - demak qisqarish ham yo'q va optimal qadam "
     f"muammosi butunlay yo'qoladi.")

table("Sonli hosila usullarining taqqoslashi",
      ["Usul", "Tartib", "Optimal h", "Eng yaxshi aniqlik",
       "Hisoblash narxi"],
      [["Oldinga ayirma", "1", "~eps^(1/2) = 1.5e-8", "~1e-8",
        "1 qo'shimcha"],
       ["Markaziy ayirma", "2", "~eps^(1/3) = 6e-6", "~1e-11",
        "2 qo'shimcha"],
       ["Richardson (markaziy)", "4", "~1e-3", "~1e-13",
        "4 qo'shimcha"],
       ["Kompleks qadam", "2", "ixtiyoriy kichik", "~1e-16",
        "1 kompleks"],
       ["Avtomatik diff. (AD)", "aniq", "kerak emas", "mashina aniqligi",
        "~2-3x asosiy"]])
''',
                parameters=[
                    p("x0", "Hosila olinadigan nuqta x₀", 0.1, 10.0, 1.0,
                      0.1),
                    p("fn", "Funksiya (0 sin, 1 exp, 2 x³ln x)",
                      0.0, 2.0, 0.0, 1.0),
                    p("h_rich", "Richardson uchun boshlang'ich qadam",
                      0.0001, 0.5, 0.01, 0.0001),
                ],
                expected_output=(
                    "Kesish rejimida o'lchangan qiyaliklar: "
                    "oldinga ayirma ≈ 1, markaziy ≈ 2 — "
                    "Teylor qatoridan chiqarilgan "
                    "tartiblar tasdiqlanadi. Juda kichik "
                    "qadamlarda qiyalik ≈ −1 (yaxlitlash "
                    "hukmron). Markaziy ayirmaning "
                    "optimal qadami oldingidan tartiblarga "
                    "**katta**, lekin natijasi tartiblarga "
                    "aniqroq. Richardson tartibni 2 dan "
                    "4,006 ga ko'taradi va xatolikni "
                    "798 600 marta kamaytiradi. Kompleks "
                    "qadam usuli h = 1e-16 da xatolikni "
                    "AYNAN nolga tushiradi (mashina "
                    "aniqligi), markaziy ayirma esa shu "
                    "qadamda 2,7 % xatolik beradi."
                ),
            ),
            visual=vis(
                kind="Optimal qadam va xatoliklar raqobati",
                tool="React/SVG + Manim",
                description=(
                    "Log–log grafikda kesish va "
                    "yaxlitlash xatoliklarining V "
                    "shaklidagi yig'indisi."
                ),
                how_to_draw=(
                    "React/SVG: asosiy panel — log–log "
                    "o'qlarda uchta egri chiziq "
                    "(oldinga, markaziy, kompleks qadam). "
                    "Birinchi ikkitasi xarakterli **V** "
                    "shaklida: o'ng tarmoq kesish "
                    "xatoligi (qiyalik $+1$ yoki $+2$), "
                    "chap tarmoq yaxlitlash ($-1$). "
                    "Nazariy qiyaliklar punktir "
                    "uchburchaklar bilan grafik ustiga "
                    "qo'yiladi — o'lchangan va nazariy "
                    "qiyaliklar ustma-ust tushgani "
                    "ko'rinadi. Har bir egri chiziqning "
                    "minimumi nuqta bilan belgilanib, "
                    "$h_{opt}$ qiymati yoziladi va "
                    "nazariy bashorat vertikal punktir "
                    "chiziq bilan qo'yiladi. Kompleks "
                    "qadam chizig'i esa **V shaklida "
                    "emas** — u pastda gorizontal "
                    "bo'lib cho'ziladi va bu farq "
                    "darhol ko'zga tashlanadi. "
                    "Ikkinchi panel — Richardson "
                    "jadvali ustunli diagramma "
                    "sifatida: $D(h)$, $D(h/2)$ va "
                    "$D_R$ xatoliklari log o'qda "
                    "yonma-yon, qadam kamaygani sari "
                    "$D_R$ ustuni ancha tez pasayadi."
                ),
            ),
            interp=(
                "Log–log grafikdagi ikkita qiyalik "
                "nazariyani bevosita tasdiqlaydi: "
                "kesish rejimida oldinga ayirma uchun "
                "$1$, markaziy uchun $2$ — bu 2- va "
                "4-qadamlardagi Teylor yoyilmalaridan "
                "chiqqan tartiblar. Juda kichik "
                "qadamlarda esa qiyalik $-1$ ga "
                "aylanadi va bu 7-qadamdagi "
                "$\\varepsilon/h$ bahosining tasdig'i. "
                "Ikki rejimning uchrashuvi V shaklidagi "
                "minimumni beradi. O'lchangan optimal "
                "qadam nazariy bashorat bilan bir xil "
                "tartibda chiqadi; aniq moslik "
                "kutilmaydi, chunki nazariy formula "
                "eng yomon holatga mo'ljallangan, "
                "lekin **tartib** to'g'ri bashorat "
                "qilinadi va amaliyotda muhimi shu. "
                "Eng qarama-qarshi natija shundaki, "
                "markaziy ayirmaning optimal qadami "
                "oldingidan ancha **katta**, lekin "
                "natijasi ancha **aniqroq**. Ya'ni "
                "aniqlikni oshirish uchun qadamni "
                "kichraytirish emas, **sxemani "
                "yaxshilash** kerak. Richardson "
                "ekstrapolyatsiyasi bu fikrni davom "
                "ettiradi: bir xil sxemadan bitta "
                "qo'shimcha hisoblash evaziga tartibni "
                "2 dan 4 ga ko'taradi. Nihoyat, "
                "kompleks qadam usuli butunlay boshqa "
                "manzara beradi — uning chizig'ida V "
                "shakli yo'q, chunki ayirish "
                "bajarilmaydi va qisqarish umuman "
                "paydo bo'lmaydi. Bu su-02 dagi "
                "asosiy saboqning yana bir tasdig'i: "
                "muammoni aniqlikni oshirish bilan "
                "emas, **formulani qayta qurish** "
                "bilan hal qilish kerak."
            ),
            mistakes=[
                "Qadamni imkon qadar kichik olish. "
                "Optimal qadamdan keyin xatolik "
                "$1/h$ bo'yicha **ortadi**.",
                "Mutlaq qadam ishlatish. "
                "$x = 10^6$ da $h = 10^{-5}$ "
                "butunlay yo'qoladi; qadam nisbiy "
                "bo'lishi kerak.",
                "Richardson ekstrapolyatsiyasini "
                "juda kichik qadamda qo'llash. "
                "Yaxlitlash hukmron bo'lsa u "
                "natijani **yomonlashtiradi**.",
                "Yaqinlashish tartibini silliq "
                "bo'lmagan funksiyada kutish. "
                "Uzilish yoki burchak bo'lsa tartib "
                "pasayadi.",
                "Sonli hosilani FEM sezgirlik "
                "tahlilida ishlatish. Analitik "
                "sezgirlik yoki avtomatik "
                "differensiallash tartiblarga "
                "aniqroq.",
            ],
            quiz=[
                q("Nima uchun markaziy ayirma "
                  "oldinga ayirmadan yuqori tartibli?",
                  "Teylor yoyilmalarini ayirganda "
                  "**juft** darajali hadlar o'zaro "
                  "qisqaradi va yetakchi xatolik "
                  "$h^2$ bo'lib qoladi.",
                  "konseptual"),
                q("Sonli hosilada optimal qadam nima "
                  "uchun mavjud?",
                  "Kesish xatoligi $h^p$ bilan "
                  "kamayadi, yaxlitlash xatoligi "
                  "$\\varepsilon/h$ bilan ortadi; "
                  "ikki qarama-qarshi hadning "
                  "yig'indisi minimumga ega.",
                  "konseptual"),
                q("Markaziy ayirma uchun "
                  "$h_{opt}$ ning $\\varepsilon$ ga "
                  "bog'liqligi qanday?",
                  "$h_{opt} \\sim \\varepsilon^{1/3} "
                  "\\approx 6\\times10^{-6}$; eng "
                  "yaxshi aniqlik esa "
                  "$\\varepsilon^{2/3} \\approx "
                  "4\\times10^{-11}$.", "hisob"),
                q("Kodda nima uchun qiyaliklar ikkita "
                  "turli oraliqda o'lchanadi?",
                  "Katta qadamlarda kesish rejimi "
                  "($+1$, $+2$ qiyalik), juda kichik "
                  "qadamlarda yaxlitlash rejimi "
                  "($-1$) hukmron; ular alohida "
                  "tekshiriladi.", "kod"),
                q("Richardson ekstrapolyatsiyasi "
                  "qanday ishlaydi?",
                  "$D(h)$ va $D(h/2)$ dan yetakchi "
                  "xatolik hadini algebraik "
                  "yo'qotadi: $D_R = (2^pD(h/2)-"
                  "D(h))/(2^p-1)$, tartib $p$ dan "
                  "$p+2$ ga ko'tariladi.", "talqin"),
                q("Kompleks qadam usuli nima uchun "
                  "qisqarishdan xoli?",
                  "Unda ayirish umuman yo'q — "
                  "$\\mathrm{Im}[f(x+ih)]/h$ faqat "
                  "mavhum qismni oladi; shuning "
                  "uchun $h$ ixtiyoriy kichik "
                  "bo'lishi mumkin.", "talqin"),
            ],
            bridge=(
                "Ayirmadagi xatolikning kuchayish "
                "koeffitsienti $(|x|+|y|)/|x-y|$ "
                "aslida umumiyroq tushunchaning "
                "sodda holi edi. Har qanday masala "
                "uchun kirish ma'lumotidagi xatoning "
                "natijaga qanchalik kuchayib "
                "o'tishini o'lchaydigan kattalik bor "
                "— **shartlanganlik soni**. Keyingi "
                "mavzuda uni chiziqli tizimlar uchun "
                "aniqlaymiz va nima uchun ba'zi "
                "mexanika masalalari tabiatan "
                "'qiyin' ekanini ko'rsatamiz."
            ),
            research=(
                "Differensiallash usullarini "
                "chuqurroq o'rganing. (1) Kompleks "
                "qadam usulining nazariy asosini "
                "keltirib chiqaring va uning "
                "cheklovlarini aniqlang: qaysi "
                "funksiyalarda u ishlamaydi "
                "(`abs`, `max`, taqqoslashlar)? "
                "(2) Avtomatik differensiallashning "
                "oldinga (forward) va teskari "
                "(reverse) rejimlarini solishtiring; "
                "FEM sezgirlik tahlilida qaysi biri "
                "afzal va nima uchun? (3) Yuqori "
                "tartibli ayirma sxemalarini "
                "(5 va 7 nuqtali) quring hamda "
                "ularning optimal qadami va eng "
                "yaxshi aniqligini nazariy "
                "baholang — tartib oshgani sari "
                "foyda nima uchun kamayadi?"
            ),
            manim_ref=manim(
                scene="OptimalStepScene",
                module="manim/scenes/su_basics.py",
                title="Kesish va yaxlitlash xatoliklarining raqobati",
                summary=(
                    "Qadam kamaygani sari sonli "
                    "hosila aniq qiymatga "
                    "yaqinlashadi, keyin esa "
                    "kutilmaganda undan uzoqlashib "
                    "ketadi. Log–log grafikda ikkita "
                    "tarmoq va ularning "
                    "kesishuvidagi minimum "
                    "quriladi; oxirida kompleks "
                    "qadam usuli qo'shilib, uning "
                    "chizig'i V shakliga ega "
                    "emasligi ko'rsatiladi."
                ),
            ),
        ),
    ),

    # ------------------------------------------------------------------ su-04
    Topic(
        id="su-04",
        subject_id=S, module_id=M, order=4,
        title="Shartlanganlik soni va masalaning xosligi",
        description=(
            "Shartlanganlik soni, uning mexanik ma'nosi, to'r va "
            "birliklar ta'siri, nozik masalalar va oldindan shartlash "
            "(preconditioning) g'oyasi."
        ),
        learning_objective=(
            "Chiziqli tizimning shartlanganlik sonini hisoblash, "
            "yechimdagi ishonchli raqamlar sonini baholash va "
            "shartlanganlikni yaxshilash usullarini qo'llash."
        ),
        prerequisites=["su-03", "mq-27", "pq-19"],
        mathematical_core=(
            "$\\kappa(\\mathbf{K}) = \\|\\mathbf{K}\\|\\,"
            "\\|\\mathbf{K}^{-1}\\| = "
            "\\sigma_{max}/\\sigma_{min}$; "
            "$\\dfrac{\\|\\delta u\\|}{\\|u\\|} \\le \\kappa\\,"
            "\\dfrac{\\|\\delta f\\|}{\\|f\\|}$."
        ),
        engineering_application=(
            "Yupqa qobiq elementlari, juda qattiq va juda yumshoq "
            "material aralashgan modellar, kontakt masalalari, "
            "deyarli mexanizm bo'lgan fermalar, birliklar aralashuvi."
        ),
        computational_component=(
            "Shartlanganlik sonini turli holatlarda o'lchash va "
            "yechimning aniqligiga ta'sirini ko'rsatish."
        ),
        visualization_component=(
            "Yomon shartlangan tizimning geometrik ma'nosi: deyarli "
            "parallel chiziqlar va ularning kesishuvi."
        ),
        research_extension=(
            "Oldindan shartlash (preconditioning) usullarini "
            "o'rganing: Yakobi, to'liq bo'lmagan Cholesky, ko'p "
            "to'rli usullar. FEM matritsalari uchun qaysi biri "
            "samarali?"
        ),
        difficulty="murakkab",
        previous_link=(
            "su-02 da ayirmadagi xatolikning kuchayish koeffitsienti "
            "$(|x|+|y|)/|x-y|$ chiqarilgan edi. U aslida bitta "
            "amalning shartlanganlik soni edi. Endi bu tushunchani "
            "butun chiziqli tizimga umumlashtiramiz."
        ),
        next_topic="su-05",
        estimated_minutes=85,
        tags=["shartlanganlik", "kappa", "xoslik", "preconditioning"],
        lesson=_lesson(
            problem=(
                "Ikkita ferma hisoblaymiz. Birinchisi — "
                "oddiy uchburchak ferma, sterjenlari bir "
                "xil. Ikkinchisi — deyarli yassi ferma: "
                "uchta tugun bir to'g'ri chiziqqa juda "
                "yaqin, ko'tarilish balandligi tayanchlar "
                "orasidagi masofaning mingdan biri. "
                "Ikkalasi ham statik aniqlanuvchi, "
                "ikkalasining ham yechimi mavjud va "
                "yagona. Lekin ikkinchisida yuklamani "
                "0,01 % ga o'zgartirsak, sterjendagi kuch "
                "10 % ga o'zgaradi. Hech qanday hisoblash "
                "xatosi yo'q — **masalaning o'zi shunday**. "
                "Bunday masalalarni oldindan tanib olish "
                "va ular bilan qanday ishlashni bilish "
                "kerak."
            ),
            concepts=[
                c("Shartlanganlik soni $\\kappa$",
                  "Kirish ma'lumotidagi nisbiy xatoning "
                  "yechimdagi nisbiy xatoga maksimal "
                  "kuchayish koeffitsienti; "
                  "$\\kappa = \\|\\mathbf{K}\\|\\|"
                  "\\mathbf{K}^{-1}\\|$."),
                c("Xos (well-posed) masala",
                  "Yechim mavjud, yagona va kirish "
                  "ma'lumotiga uzluksiz bog'liq "
                  "(Adamar shartlari)."),
                c("Yomon shartlangan (ill-conditioned) "
                  "masala",
                  "Xos, lekin $\\kappa$ juda katta — "
                  "kichik bezovtalik katta o'zgarish "
                  "beradi. Bu **masalaning** xossasi, "
                  "algoritmniki emas."),
                c("Nobarqaror algoritm",
                  "Yaxshi shartlangan masalada ham katta "
                  "xato beradigan algoritm — bu "
                  "**algoritmning** kamchiligi. Ikkisini "
                  "ajratish muhim."),
                c("Singulyar qiymatlar orqali ifoda",
                  "$\\kappa_2 = \\sigma_{max}/\\sigma_{min}$; "
                  "simmetrik musbat aniqlangan matritsada "
                  "$\\kappa = \\lambda_{max}/\\lambda_{min}$."),
                c("Oldindan shartlash (preconditioning)",
                  "$\\mathbf{M}^{-1}\\mathbf{K}$ ning "
                  "shartlanganligi $\\mathbf{K}$ nikidan "
                  "yaxshi bo'ladigan $\\mathbf{M}$ tanlash."),
            ],
            derivation=[
                d("1. Bezovtalangan tizim",
                  r"\mathbf{K}(\mathbf{u}+\delta\mathbf{u}) "
                  r"= \mathbf{f} + \delta\mathbf{f}",
                  "O'ng tomonda kichik xato bor (yuklama "
                  "aniq emas yoki yaxlitlangan). Yechim "
                  "qanchalik o'zgaradi?"),
                d("2. Bezovtalikning yechimga o'tishi",
                  r"\delta\mathbf{u} = \mathbf{K}^{-1}"
                  r"\delta\mathbf{f} \;\Longrightarrow\; "
                  r"\|\delta\mathbf{u}\| \le "
                  r"\|\mathbf{K}^{-1}\|\,\|\delta\mathbf{f}\|",
                  "Asosiy tizimni ayirdik. Norma "
                  "xossasidan tengsizlik."),
                d("3. Yechimning normasini baholash",
                  r"\|\mathbf{f}\| = \|\mathbf{K}\mathbf{u}\| "
                  r"\le \|\mathbf{K}\|\,\|\mathbf{u}\| "
                  r"\;\Longrightarrow\; "
                  r"\frac{1}{\|\mathbf{u}\|} \le "
                  r"\frac{\|\mathbf{K}\|}{\|\mathbf{f}\|}",
                  "Pastdan baho — nisbiy xatoni "
                  "shakllantirish uchun kerak."),
                d("4. Shartlanganlik soni",
                  r"\frac{\|\delta\mathbf{u}\|}"
                  r"{\|\mathbf{u}\|} \le "
                  r"\underbrace{\|\mathbf{K}\|\,"
                  r"\|\mathbf{K}^{-1}\|}_{\kappa}\,"
                  r"\frac{\|\delta\mathbf{f}\|}"
                  r"{\|\mathbf{f}\|}",
                  "**Asosiy natija.** $\\kappa$ — "
                  "kuchayish koeffitsienti. U su-02 "
                  "dagi $(|x|+|y|)/|x-y|$ ning "
                  "umumlashmasi."),
                d("5. Singulyar qiymatlar orqali",
                  r"\|\mathbf{K}\|_2 = \sigma_{max}, \quad "
                  r"\|\mathbf{K}^{-1}\|_2 = "
                  r"\frac{1}{\sigma_{min}} "
                  r"\;\Longrightarrow\; \kappa_2 = "
                  r"\frac{\sigma_{max}}{\sigma_{min}}",
                  "Eng katta va eng kichik "
                  "'cho'zilish' koeffitsientlarining "
                  "nisbati. $\\kappa \\ge 1$ har doim."),
                d("6. Yo'qoladigan raqamlar soni",
                  r"\text{ishonchli raqamlar} \approx "
                  r"16 - \log_{10}\kappa",
                  "$\\kappa = 10^{8}$ bo'lsa 16 raqamdan "
                  "8 tasi qoladi. $\\kappa = 10^{16}$ "
                  "bo'lsa **hech narsa qolmaydi** — "
                  "yechim ma'nosiz."),
                d("7. Mexanik ma'nosi: energiya orqali",
                  r"\kappa = \frac{\lambda_{max}}"
                  r"{\lambda_{min}} = \frac{\text{eng "
                  r"bikr deformatsiya rejimi}}"
                  r"{\text{eng yumshoq rejim}}",
                  "**Hal qiluvchi talqin.** Simmetrik "
                  "musbat aniqlangan bikrlik "
                  "matritsasida $\\lambda$ lar "
                  "deformatsiya rejimlarining "
                  "bikrliklari. $\\kappa$ katta — "
                  "demak tizimda juda bikr va juda "
                  "yumshoq rejimlar birga yashaydi."),
                d("8. Mexanikadagi manbalar",
                  r"\kappa \sim \Big(\frac{L}{h}\Big)^2, "
                  r"\quad \kappa \sim \frac{E_1}{E_2}, "
                  r"\quad \kappa \sim n^2 "
                  r"\ (\text{to'r})",
                  "Uchta asosiy manba: yupqa "
                  "konstruksiyalar (egilish va "
                  "cho'zilish bikrliklari juda farq "
                  "qiladi), materiallar farqi "
                  "(po'lat va rezina) va to'rning "
                  "zichligi (su-01 da o'lchangan "
                  "$q = 1{,}91$)."),
                d("9. Birliklarning ta'siri",
                  r"\mathbf{K} \to \mathbf{D}\mathbf{K}"
                  r"\mathbf{D} \ \text{(masshtablash)} "
                  r"\;\Longrightarrow\; \kappa \ "
                  r"\text{keskin o'zgaradi}",
                  "Ko'chish metrlarda, burilish "
                  "radianlarda o'lchansa, ularning "
                  "koeffitsientlari tartiblarga farq "
                  "qiladi. **Bu sun'iy yomon "
                  "shartlanganlik** — masshtablash "
                  "bilan bartaraf etiladi."),
                d("10. Oldindan shartlash",
                  r"\mathbf{M}^{-1}\mathbf{K}\mathbf{u} = "
                  r"\mathbf{M}^{-1}\mathbf{f}, \quad "
                  r"\kappa(\mathbf{M}^{-1}\mathbf{K}) "
                  r"\ll \kappa(\mathbf{K})",
                  "Eng sodda tanlov — Yakobi "
                  "(diagonal) shartlash: "
                  "$\\mathbf{M} = \\mathrm{diag}"
                  "(\\mathbf{K})$. U birliklar "
                  "aralashuvidan kelgan sun'iy "
                  "shartlanganlikni deyarli to'liq "
                  "yo'qotadi."),
                d("11. Qoldiq aldamchi ekani",
                  r"\|\mathbf{r}\| = \|\mathbf{f} - "
                  r"\mathbf{K}\tilde{\mathbf{u}}\| "
                  r"\ \text{kichik} \ \nRightarrow\ "
                  r"\|\tilde{\mathbf{u}} - \mathbf{u}\| "
                  r"\ \text{kichik}",
                  "**Muhim ogohlantirish.** Yomon "
                  "shartlangan tizimda qoldiq juda "
                  "kichik bo'lishi mumkin, lekin "
                  "yechim baribir xato. Chunki "
                  "$\\|\\delta u\\| \\le "
                  "\\|\\mathbf{K}^{-1}\\|\\|r\\|$ va "
                  "$\\|\\mathbf{K}^{-1}\\|$ katta."),
            ],
            meaning=(
                "Shartlanganlik soni sonli usullardagi "
                "eng muhim tushunchalardan biri, chunki "
                "u **masalaning** xossasini **algoritm** "
                "xossasidan ajratadi. Agar $\\kappa$ "
                "katta bo'lsa, hech qanday algoritm "
                "yaxshi javob bera olmaydi — bu "
                "dasturning aybi emas, masalaning "
                "tabiati. Aksincha, $\\kappa$ kichik "
                "bo'lib turib natija yomon chiqsa, "
                "algoritm nobarqaror. Bu ajratish "
                "amaliyotda hal qiluvchi: birinchi "
                "holatda modelni qayta qurish kerak, "
                "ikkinchisida algoritmni almashtirish. "
                "7-qadamdagi mexanik talqin eng "
                "foydalisi: $\\kappa$ — eng bikr va "
                "eng yumshoq deformatsiya rejimlarining "
                "bikrliklari nisbati. Yupqa qobiqda "
                "membrana bikrligi $Eh$, egilish "
                "bikrligi esa $Eh^3/12$ tartibida — "
                "ularning nisbati $(L/h)^2$ ga "
                "mutanosib. $L/h = 100$ bo'lsa "
                "$\\kappa \\sim 10^4$, ya'ni 4 ta "
                "raqam yo'qoladi. Bu qobiq elementlari "
                "nima uchun 'qiyin' ekanining aniq "
                "izohi va u pq-24 dagi sdvig "
                "qulflanishi bilan bevosita bog'liq. "
                "Amaliy jihatdan eng muhimi — 9- va "
                "11-qadamlar. Birliklardan kelgan "
                "yomon shartlanganlik **sun'iy** va "
                "uni oddiy diagonal masshtablash "
                "bilan bartaraf etish mumkin; ko'p "
                "muhandislar buni bilmay, mavjud "
                "bo'lmagan muammo bilan kurashadi. "
                "11-qadam esa ogohlantiradi: kichik "
                "qoldiq yechimning to'g'riligini "
                "kafolatlamaydi. Yomon shartlangan "
                "tizimda $\\|\\mathbf{r}\\|$ mashina "
                "aniqligida bo'lishi va yechim "
                "baribir butunlay xato bo'lishi "
                "mumkin."
            ),
            equations=[
                eq(r"\kappa(\mathbf{K}) = \|\mathbf{K}\|\,"
                   r"\|\mathbf{K}^{-1}\| = "
                   r"\frac{\sigma_{max}}{\sigma_{min}}",
                   "Shartlanganlik sonining ta'rifi va "
                   "singulyar qiymatlar orqali ifodasi.",
                   "Shartlanganlik soni"),
                eq(r"\frac{\|\delta\mathbf{u}\|}"
                   r"{\|\mathbf{u}\|} \le \kappa\,"
                   r"\frac{\|\delta\mathbf{f}\|}"
                   r"{\|\mathbf{f}\|}",
                   "Kirish xatosining yechimga "
                   "kuchayib o'tishi.",
                   "Xatolikning kuchayishi"),
                eq(r"\text{ishonchli raqamlar} \approx "
                   r"16 - \log_{10}\kappa",
                   "`double` aniqligida qancha raqam "
                   "qolishi.", "Ishonchli raqamlar"),
                eq(r"\kappa_{qobiq} \sim "
                   r"\Big(\frac{L}{h}\Big)^2",
                   "Yupqa konstruksiyalarda "
                   "shartlanganlikning geometriyaga "
                   "bog'liqligi.",
                   "Yupqa qobiq shartlanganligi"),
            ],
            conditions=(
                "**Adamar bo'yicha xoslik "
                "(well-posedness) shartlari:**\n"
                "1. Yechim **mavjud**;\n"
                "2. Yechim **yagona**;\n"
                "3. Yechim kirish ma'lumotiga "
                "**uzluksiz** bog'liq.\n\n"
                "Uchinchi shart buzilsa masala xos "
                "emas (teskari masalalar, "
                "eksperimental ma'lumotdan "
                "yuklamani tiklash). Shartlanganlik "
                "soni katta bo'lsa — masala xos, "
                "lekin **amalda** xos emasdek "
                "xatti-harakat qiladi.\n\n"
                "**$\\kappa$ ni baholash "
                "mezonlari:**\n"
                "- $\\kappa < 10^{3}$ — yaxshi;\n"
                "- $10^{3} \\ldots 10^{8}$ — odatiy "
                "FEM tizimi, e'tibor talab qiladi;\n"
                "- $10^{8} \\ldots 10^{12}$ — xavfli, "
                "natijani tekshirish shart;\n"
                "- $> 10^{14}$ — `double` da yechim "
                "ma'nosiz.\n\n"
                "**Diagnostika tartibi:** avval "
                "diagonal masshtablash qo'llang "
                "(sun'iy shartlanganlikni yo'qotadi), "
                "keyin qolgan $\\kappa$ ni baholang — "
                "u masalaning haqiqiy xossasi."
            ),
            worked=WorkedExample(
                statement=(
                    "Deyarli yassi ikki sterjenli "
                    "ferma: tayanchlar orasi "
                    "$2L = 2$ m, o'rta tugunning "
                    "ko'tarilishi $H$. Tugunga "
                    "vertikal $P = 10$ kN qo'yilgan. "
                    "$H = 500$ mm va $H = 1$ mm "
                    "holatlari uchun sterjendagi kuchni "
                    "va masalaning shartlanganligini "
                    "taqqoslang."
                ),
                given=[
                    r"L = 1\ \text{m},\ P = 10\ \text{kN}",
                    r"H_1 = 0{,}5\ \text{m},\ "
                    r"H_2 = 0{,}001\ \text{m}",
                ],
                steps=[
                    st(r"\text{Tugun muvozanati: } "
                       r"2N\sin\alpha = P, \quad "
                       r"\sin\alpha = \frac{H}"
                       r"{\sqrt{L^2+H^2}}",
                       "Ikkala sterjen simmetrik; "
                       "$\\alpha$ — sterjenning "
                       "gorizontal bilan burchagi."),
                    st(r"N = \frac{P}{2\sin\alpha} = "
                       r"\frac{P\sqrt{L^2+H^2}}{2H}",
                       "Sterjendagi kuch."),
                    st(r"H_1 = 0{,}5: \ N = "
                       r"\frac{10\sqrt{1+0{,}25}}{2 \cdot "
                       r"0{,}5} = \frac{10 \cdot 1{,}118}"
                       r"{1} = 11{,}18\ \text{kN}",
                       "Kuch yuklamaga yaqin — normal "
                       "holat."),
                    st(r"H_2 = 0{,}001: \ N = "
                       r"\frac{10\sqrt{1+10^{-6}}}"
                       r"{0{,}002} = 5000\ \text{kN}",
                       "**500 barobar katta.** Deyarli "
                       "yassi ferma yuklamani juda "
                       "katta o'q kuchlari bilan "
                       "ko'taradi."),
                    st(r"\frac{\partial N}{\partial H} "
                       r"\approx -\frac{PL}{2H^2}: \quad "
                       r"\frac{dN/N}{dH/H} = -1 "
                       r"\ (\text{kichik } H)",
                       "Sezgirlik: $H$ ning nisbiy "
                       "xatosi $N$ ga **bir barobar** "
                       "o'tadi. Bu hali yomon emas."),
                    st(r"\text{Bikrlik matritsasi: } "
                       r"k_{vert} = \frac{2EA\sin^2\alpha}"
                       r"{\ell}, \quad k_{gor} = "
                       r"\frac{2EA\cos^2\alpha}{\ell}",
                       "Tugunning vertikal va gorizontal "
                       "bikrliklari."),
                    st(r"\kappa = \frac{k_{gor}}{k_{vert}} "
                       r"= \cot^2\alpha = "
                       r"\Big(\frac{L}{H}\Big)^2",
                       "**Hal qiluvchi natija.** "
                       "Shartlanganlik soni "
                       "$(L/H)^2$ — 8-qadamdagi umumiy "
                       "qonunning aynan o'zi."),
                    st(r"H_1 = 0{,}5: \ \kappa = 2^2 = 4 "
                       r"\;\Rightarrow\; \text{ajoyib}",
                       "Deyarli hech narsa yo'qolmaydi."),
                    st(r"H_2 = 0{,}001: \ \kappa = "
                       r"1000^2 = 10^{6} "
                       r"\;\Rightarrow\; 6 \ "
                       r"\text{raqam yo'qoladi}",
                       "16 dan 10 tasi qoladi — hali "
                       "ishlaydi, lekin "
                       "$H = 10^{-5}$ m bo'lsa "
                       "$\\kappa = 10^{10}$ va faqat "
                       "6 raqam qoladi."),
                    st(r"H = 10^{-8}\ \text{m}: \ "
                       r"\kappa = 10^{16} "
                       r"\;\Rightarrow\; \text{yechim "
                       r"ma'nosiz}",
                       "Bu yerda ferma amalda "
                       "**mexanizmga** aylanadi — "
                       "matematik singulyarlikka "
                       "yaqinlashadi. Masalaning "
                       "o'zi buzilgan, algoritm "
                       "emas."),
                ],
                answer=(
                    "$H = 0{,}5$ m: $N = 11{,}18$ kN, "
                    "$\\kappa = 4$ — masala yaxshi "
                    "shartlangan. $H = 1$ mm: "
                    "$N = 5000$ kN (500 barobar katta), "
                    "$\\kappa = 10^{6}$ — 6 ta raqam "
                    "yo'qoladi. Shartlanganlik soni "
                    "$(L/H)^2$ qonuni bo'yicha o'sadi, "
                    "ya'ni geometriya yassilashgani "
                    "sari **kvadratik** yomonlashadi."
                ),
                engineering_note=(
                    "Deyarli yassi ferma — "
                    "mexanikadagi klassik yomon "
                    "shartlangan masala va u amaliyotda "
                    "tez-tez uchraydi: yassi tomlar, "
                    "kabel tizimlari, oldindan "
                    "tarang tortilgan konstruksiyalar. "
                    "Bu yerda ikkita alohida muammo "
                    "bor. Birinchisi fizik: kuch "
                    "haqiqatan ham juda katta va "
                    "konstruksiya buzilishi mumkin. "
                    "Ikkinchisi sonli: hisob "
                    "natijasiga ishonib bo'lmaydi, "
                    "chunki geometriyadagi ishlab "
                    "chiqarish dopuski (masalan "
                    "$\\pm 1$ mm) natijani ikki "
                    "barobar o'zgartirishi mumkin. "
                    "Shuning uchun bunday "
                    "konstruksiyalarda geometrik "
                    "nochiziqli tahlil (su-24) "
                    "majburiy: chiziqli yechim "
                    "nafaqat noaniq, balki fizik "
                    "jihatdan ham noto'g'ri — katta "
                    "ko'chishlarda geometriya "
                    "o'zgaradi va kuch qayta "
                    "taqsimlanadi. Yana bir amaliy "
                    "maslahat: $\\kappa$ ni FEM "
                    "hisobidan keyin **har doim** "
                    "tekshiring; ko'pchilik paketlar "
                    "uni chiqaradi yoki 'pivot ratio' "
                    "ogohlantirishini beradi."
                ),
            ),
            computation=Computation(
                caption=(
                    "Shartlanganlik sonini turli "
                    "holatlarda o'lchash: geometriya, "
                    "materiallar farqi, to'r zichligi "
                    "va birliklar."
                ),
                code='''"""Shartlanganlik soni va uning mexanikadagi manbalari."""
import numpy as np
from labkit import PARAMS, note, series, table, value

E = float(PARAMS.get("E", 210.0))*1e9
A = float(PARAMS.get("A", 1000.0))/1e6
L = float(PARAMS.get("L", 1.0))
H = float(PARAMS.get("H", 500.0))/1000.0
P = float(PARAMS.get("P", 10.0))*1e3
n_grid = int(PARAMS.get("n_grid", 40))
Erat = float(PARAMS.get("Erat", 1000.0))

# --- (1) Deyarli yassi ferma ---
def truss_K(h):
    ell = np.sqrt(L**2 + h**2)
    ca, sa = L/ell, h/ell
    k = E*A/ell
    # Tugunning 2x2 bikrlik matritsasi (ikkita simmetrik sterjen)
    return np.array([[2*k*ca**2, 0.0],
                     [0.0, 2*k*sa**2]])


Kt = truss_K(H)
kap_t = np.linalg.cond(Kt)
ell0 = np.sqrt(L**2 + H**2)
N_bar = P*ell0/(2*H)
value("Ko'tarilish H", H*1000, "mm")
value("Sterjendagi kuch N", N_bar/1000, "kN")
value("N / P nisbati", N_bar/P, "marta")
value("Shartlanganlik soni kappa", kap_t, "—")
value("Nazariy (L/H)^2", (L/H)**2, "—")
value("Yo'qoladigan raqamlar", np.log10(kap_t), "—")
note(f"H = {H*1000:.3f} mm da sterjen kuchi {N_bar/1000:.1f} kN, ya'ni "
     f"yuklamadan {N_bar/P:.1f} marta katta. Shartlanganlik soni "
     f"{kap_t:.4e}, nazariy (L/H)^2 = {(L/H)**2:.4e} - aynan mos. "
     f"Taxminan {np.log10(kap_t):.1f} ta o'nlik raqam yo'qoladi.")

Hs = np.logspace(-6, 0, 200)
kaps, forces = [], []
for h in Hs:
    kaps.append(np.linalg.cond(truss_K(h)))
    forces.append(P*np.sqrt(L**2 + h**2)/(2*h)/1000)
series("kappa(H) — ferma", (Hs*1000).tolist(), kaps,
       xlabel="ko'tarilish H, mm", ylabel="kappa")
series("Nazariy (L/H)^2", (Hs*1000).tolist(),
       [(L/h)**2 for h in Hs],
       xlabel="ko'tarilish H, mm", ylabel="kappa")
series("Sterjen kuchi N(H)", (Hs*1000).tolist(), forces,
       xlabel="ko'tarilish H, mm", ylabel="N, kN")
dev = max(abs(k - (L/h)**2)/((L/h)**2) for k, h in zip(kaps, Hs))
value("kappa va (L/H)^2 maks. farqi", dev*100, "%")

# Qaysi H da double aniqligi tugaydi?
crit = [h for h, k in zip(Hs, kaps) if k > 1e16]
if crit:
    value("double aniqligi tugaydigan H", crit[-1]*1000, "mm")
    note(f"H < {crit[-1]*1000:.4f} mm da kappa > 1e16 va double "
         f"aniqligida yechim BUTUNLAY ma'nosiz bo'ladi - ferma "
         f"amalda mexanizmga aylanadi.")
else:
    note("Berilgan H oralig'ida kappa 1e16 dan oshmadi - double "
         "aniqligi yetarli.")

# --- (2) Bezovtalikni SONLI tekshirish ---
# Kt simmetrik, shuning uchun xususiy vektorlar orqali ishlaymiz.
lam, V = np.linalg.eigh(Kt)
i_lo, i_hi = int(np.argmin(lam)), int(np.argmax(lam))

# (a) TASODIFIY yo'nalishlar: tengsizlik bajariladi, lekin kappa ga
#     odatda YETMAYDI
rng = np.random.default_rng(7)
f0 = np.array([0.0, -P])
u0 = np.linalg.solve(Kt, f0)
amp_rand = 0.0
for _ in range(400):
    dp = rng.normal(size=2)
    dp = dp/np.linalg.norm(dp)*1e-8*np.linalg.norm(f0)
    u1 = np.linalg.solve(Kt, f0 + dp)
    ri = np.linalg.norm(dp)/np.linalg.norm(f0)
    ro = np.linalg.norm(u1 - u0)/np.linalg.norm(u0)
    amp_rand = max(amp_rand, ro/ri)
value("Tasodifiy yo'nalishlarda maksimal kuchayish", amp_rand, "—")

# (b) ENG YOMON holat: f eng BIKR rejim bo'ylab, bezovtalik esa eng
#     YUMSHOQ rejim bo'ylab. Shunda nisbat aynan kappa ga teng bo'ladi.
f_w = V[:, i_hi]*P
u_w = np.linalg.solve(Kt, f_w)
df_w = V[:, i_lo]*(1e-8*P)
u_w2 = np.linalg.solve(Kt, f_w + df_w)
ri_w = np.linalg.norm(df_w)/np.linalg.norm(f_w)
ro_w = np.linalg.norm(u_w2 - u_w)/np.linalg.norm(u_w)
amp_worst = ro_w/ri_w
value("Eng yomon yo'nalishda kuchayish", amp_worst, "—")
value("Nazariy chegara kappa", kap_t, "—")
value("Eng yomon / kappa", amp_worst/kap_t, "—")
note(f"Tasodifiy 400 ta yo'nalishda kuchayish eng ko'pi bilan "
     f"{amp_rand:.4e} bo'ldi - kappa = {kap_t:.4e} dan kichik. "
     f"Lekin ENG YOMON yo'nalish maxsus qurilganda (yuklama eng bikr "
     f"rejim bo'ylab, bezovtalik eng yumshoq rejim bo'ylab) kuchayish "
     f"{amp_worst:.6e} bo'ldi, ya'ni kappa ning aynan o'zi "
     f"(nisbat {amp_worst/kap_t:.6f}). Demak 4-qadamdagi tengsizlik "
     f"ham TO'G'RI, ham QATTIQ: u erishib bo'lmaydigan baho emas.")
note("Amaliy xulosa: tasodifiy bezovtalik odatda kappa ga yetmaydi, "
     "shuning uchun 'menda hammasi yaxshi ishladi' degan tajriba "
     "kafolat bermaydi - eng yomon holat baribir mumkin.")

# --- (3) Materiallar farqi ---
rats = np.logspace(0, 8, 100)
kap_m = []
for r in rats:
    # Ketma-ket ulangan ikki prujina: k1 = 1, k2 = 1/r
    Km = np.array([[1.0 + 1.0/r, -1.0/r],
                   [-1.0/r, 1.0/r]])
    kap_m.append(np.linalg.cond(Km))
series("kappa(materiallar nisbati)", rats.tolist(), kap_m,
       xlabel="E1/E2", ylabel="kappa")
Km0 = np.array([[1.0 + 1.0/Erat, -1.0/Erat],
                [-1.0/Erat, 1.0/Erat]])
value("kappa, materiallar nisbati uchun", np.linalg.cond(Km0), "—")
note(f"Modullari {Erat:.0f} marta farq qiluvchi ikki material ketma-ket "
     f"ulanganda kappa = {np.linalg.cond(Km0):.3e}. Po'lat va rezina "
     f"(E nisbati ~1e5) birga modellashtirilganda bu jiddiy muammo.")

# --- (4) To'r zichligi ---
def laplace_K(n):
    K = np.zeros((n, n))
    for i in range(n):
        K[i, i] = 2.0
        if i > 0:
            K[i, i-1] = -1.0
        if i < n - 1:
            K[i, i+1] = -1.0
    return K*(n + 1)**2


ns = [5, 10, 20, 40, 80, 160]
kap_n = [np.linalg.cond(laplace_K(n)) for n in ns]
series("kappa(to'r zichligi)", [float(x) for x in ns], kap_n,
       xlabel="tugunlar soni n", ylabel="kappa")
pw = np.polyfit(np.log(ns), np.log(kap_n), 1)[0]
value("kappa ~ n^q, o'lchangan q", float(pw), "—")
note(f"Bir o'lchovli Laplas operatori uchun kappa ~ n^{pw:.2f}. "
     f"Nazariya n^2 beradi (eng katta xususiy qiymat ~ 4, eng "
     f"kichigi ~ (pi/n)^2). Bu su-01 dagi o'lchangan q = 1.91 bilan "
     f"mos - to'r zichlashgani sari tizim yomonlashadi.")

# --- (5) Birliklar: SUN'IY yomon shartlanganlik ---
# Balka elementi: [w1, theta1, w2, theta2], w metrda, theta radianda
le, Ib = 1.0, 1e-6
c0 = E*Ib/le**3
Kb = c0*np.array([[12, 6*le, -12, 6*le],
                  [6*le, 4*le**2, -6*le, 2*le**2],
                  [-12, -6*le, 12, -6*le],
                  [6*le, 2*le**2, -6*le, 4*le**2]])
# Mahkamlangan chap uch -> 2x2 qoladi
Kr = Kb[2:, 2:]
kap_si = np.linalg.cond(Kr)
# Endi ko'chishni MILLIMETRDA o'lchaymiz: w -> w/1000
Dsc = np.diag([1e-3, 1.0])
Kmm = Dsc @ Kr @ Dsc
kap_mm = np.linalg.cond(Kmm)
value("kappa (ko'chish metrda)", kap_si, "—")
value("kappa (ko'chish millimetrda)", kap_mm, "—")
value("Birlik almashtirish kappa ni necha marta o'zgartirdi",
      max(kap_si, kap_mm)/min(kap_si, kap_mm), "marta")

# Yakobi (diagonal) oldindan shartlash
def jacobi_cond(K):
    dg = np.sqrt(np.diag(K))
    Dm = np.diag(1.0/dg)
    return np.linalg.cond(Dm @ K @ Dm)


value("kappa (metr) Yakobi shartlashdan keyin", jacobi_cond(Kr), "—")
value("kappa (mm) Yakobi shartlashdan keyin", jacobi_cond(Kmm), "—")
note(f"Faqat BIRLIK o'zgartirildi (metr -> millimetr) va kappa "
     f"{kap_si:.3e} dan {kap_mm:.3e} ga o'zgardi - masala esa "
     f"o'zgarmadi. Bu SUN'IY yomon shartlanganlik. Yakobi (diagonal) "
     f"shartlashdan keyin ikkala holat ham "
     f"{jacobi_cond(Kr):.3e} va {jacobi_cond(Kmm):.3e} beradi - "
     f"ya'ni AYNI QIYMAT. Demak diagonal masshtablash birliklardan "
     f"kelgan sun'iy shartlanganlikni butunlay yo'qotadi.")

# --- (6) Qoldiq aldamchi ekani ---
# Yomon shartlangan tizim olamiz va yuklamani eng BIKR rejim bo'ylab
# qo'yamiz; yechimdagi xatoni esa eng YUMSHOQ rejim bo'ylab kiritamiz.
# Shunda xato katta, qoldiq esa kichik bo'ladi.
Kb2 = truss_K(1e-4)
kap_b = np.linalg.cond(Kb2)
lam_b, Vb = np.linalg.eigh(Kb2)
j_lo, j_hi = int(np.argmin(lam_b)), int(np.argmax(lam_b))

fb = Vb[:, j_hi]*P                      # yuklama eng bikr rejim bo'ylab
ub = np.linalg.solve(Kb2, fb)
u_bad = ub + Vb[:, j_lo]*(0.05*np.linalg.norm(ub))   # 5 % xato
r_bad = fb - Kb2 @ u_bad
err_rel = np.linalg.norm(u_bad - ub)/np.linalg.norm(ub)*100
res_rel = np.linalg.norm(r_bad)/np.linalg.norm(fb)*100
value("Tekshiruv tizimining kappa si", kap_b, "—")
value("Yechimdagi nisbiy xato", err_rel, "%")
value("Qoldiqning nisbiy normasi", res_rel, "%")
value("Xato qoldiqdan necha marta katta",
      err_rel/max(res_rel, 1e-300), "marta")
note(f"kappa = {kap_b:.3e} bo'lgan tizimda yechimni {err_rel:.2f} % ga "
     f"buzdik, lekin QOLDIQ atigi {res_rel:.3e} % chiqdi - ya'ni xato "
     f"qoldiqdan {err_rel/max(res_rel, 1e-300):.3e} marta katta. Bu "
     f"nisbat kappa ning o'zi bilan bir tartibda va bu tasodif emas: "
     f"||du||/||u|| <= kappa*||r||/||f||. Demak KICHIK QOLDIQ "
     f"yechimning to'g'riligini KAFOLATLAMAYDI.")
note("Amaliy xulosa: iteratsiyani faqat qoldiq bo'yicha to'xtatish "
     "yomon shartlangan tizimda xavfli. Qoldiq bilan birga kappa "
     "bahosi ham kerak yoki yechimni mustaqil tekshirish lozim.")

table("Shartlanganlikning mexanikadagi manbalari",
      ["Manba", "kappa ning o'sishi", "Misol", "Yechimi"],
      [["Yupqa geometriya", "(L/h)^2", "qobiq, yassi ferma",
        "nochiziqli tahlil"],
       ["Materiallar farqi", "E1/E2", "po'lat + rezina",
        "alohida modellar"],
       ["To'r zichligi", "n^2", "istalgan FEM",
        "ko'p to'rli usul"],
       ["Birliklar aralashuvi", "sun'iy", "w[m] + theta[rad]",
        "diagonal masshtablash"],
       ["Mexanizmga yaqinlik", "-> cheksiz", "yetarlicha "
        "mahkamlanmagan model", "chegaraviy shartni tuzatish"]])
''',
                parameters=[
                    p("E", "Yung moduli E", 1.0, 400.0, 210.0, 1.0, "GPa"),
                    p("A", "Sterjen yuzasi A", 10.0, 100000.0, 1000.0, 10.0,
                      "mm²"),
                    p("L", "Yarim oraliq L", 0.1, 20.0, 1.0, 0.1, "m"),
                    p("H", "Ko'tarilish H", 0.001, 2000.0, 500.0, 0.001,
                      "mm"),
                    p("P", "Yuklama P", 0.1, 1000.0, 10.0, 0.1, "kN"),
                    p("n_grid", "To'r tugunlari soni", 5.0, 200.0, 40.0,
                      5.0),
                    p("Erat", "Materiallar moduli nisbati E₁/E₂",
                      1.0, 100000000.0, 1000.0, 10.0),
                ],
                expected_output=(
                    "Ferma uchun o'lchangan κ nazariy "
                    "$(L/H)^2$ bilan 1e-13 % aniqlikda "
                    "mos tushadi. 400 ta tasodifiy "
                    "bezovtalikda kuchayish κ ga "
                    "yetmaydi, lekin maxsus qurilgan "
                    "eng yomon yo'nalishda (yuklama eng "
                    "bikr rejim bo'ylab, bezovtalik eng "
                    "yumshoq rejim bo'ylab) u **aynan κ** "
                    "ga teng chiqadi — tengsizlik ham "
                    "to'g'ri, ham qattiq. To'r uchun "
                    "κ ~ n^1,92 (su-01 dagi 1,91 bilan "
                    "mos). Birlikni metrdan millimetrga "
                    "o'zgartirish κ ni 69 000 marta "
                    "o'zgartiradi, lekin Yakobi "
                    "shartlashdan keyin ikkala holat ham "
                    "**ayni 13,93 qiymatini** beradi — "
                    "sun'iy shartlanganlik butunlay "
                    "yo'qoladi. Oxirgi blokda κ = 1e8 "
                    "bo'lgan tizimda yechimdagi 5 % xato "
                    "atigi 5e-8 % qoldiq beradi — xato "
                    "qoldiqdan aynan κ marta katta."
                ),
            ),
            visual=vis(
                kind="Yomon shartlanganlikning geometriyasi",
                tool="React/SVG",
                description=(
                    "Deyarli parallel chiziqlarning "
                    "kesishuvi va shartlanganlikning "
                    "manbalari."
                ),
                how_to_draw=(
                    "React/SVG: chap panelda ikkita "
                    "chiziqli tenglama tekislikda "
                    "chiziq sifatida tasvirlanadi va "
                    "ularning kesishuvi yechim. "
                    "Yaxshi shartlangan holatda "
                    "chiziqlar deyarli perpendikulyar "
                    "va kesishuv nuqtasi aniq; "
                    "slayder bilan burchakni "
                    "kichraytirganda chiziqlar "
                    "deyarli parallel bo'lib qoladi. "
                    "Har bir chiziq atrofida uning "
                    "noaniqlik yo'lagi (kirish "
                    "xatosidan) shtrixlangan tasma "
                    "sifatida chiziladi; "
                    "yo'laklarning kesishgan sohasi "
                    "yechimning noaniqlik sohasi "
                    "bo'lib, burchak kichraygani sari "
                    "u **cho'zilgan ellipsga** "
                    "aylanadi va o'lchami keskin "
                    "o'sadi. Yonida joriy $\\kappa$ "
                    "va 'yo'qolgan raqamlar' "
                    "hisoblagichi turadi. O'ng "
                    "panelda ferma chizmasi: "
                    "ko'tarilish $H$ slayderi bilan "
                    "o'zgaradi va sterjen kuchi "
                    "epyurasi hamda $\\kappa$ "
                    "grafigi bir vaqtda yangilanadi; "
                    "$(L/H)^2$ nazariy chizig'i "
                    "punktir bilan ustiga qo'yiladi."
                ),
            ),
            interp=(
                "Fermadagi o'lchangan $\\kappa$ nazariy "
                "$(L/H)^2$ bilan aynan mos tushishi "
                "7- va 8-qadamlardagi mexanik talqinni "
                "tasdiqlaydi: shartlanganlik soni "
                "haqiqatan ham eng bikr va eng yumshoq "
                "rejimlarning nisbati. Undan ham "
                "ishonchlisi — bezovtalik tajribasi: "
                "200 ta tasodifiy yo'nalishda kirish "
                "xatosining kuchayishi o'lchanadi va u "
                "hech qachon $\\kappa$ dan oshmaydi, "
                "lekin unga yetadi. Bu 4-qadamdagi "
                "tengsizlikning ham to'g'ri, ham "
                "**qattiq** (sharp) ekanini "
                "ko'rsatadi. To'r bo'yicha "
                "$\\kappa \\sim n^2$ natijasi su-01 "
                "dagi o'lchangan $q = 1{,}91$ bilan "
                "mos keladi va optimal to'rning "
                "mavjudligini yakuniy tushuntiradi. "
                "Eng amaliy natija esa birliklar "
                "tajribasida: faqat o'lchov birligi "
                "o'zgartirildi — masala mutlaqo "
                "o'zgarmadi — lekin $\\kappa$ "
                "tartiblarga siljidi. Yakobi "
                "shartlashdan keyin ikkala holat "
                "ayni qiymatni beradi, ya'ni bu "
                "shartlanganlik butunlay **sun'iy** "
                "edi. Bu FEM amaliyotidagi muhim "
                "saboq: qobiq va balka elementlarida "
                "ko'chish va burilish erkinlik "
                "darajalari aralashgani uchun sun'iy "
                "shartlanganlik deyarli har doim "
                "mavjud va diagonal masshtablash uni "
                "bepul yo'qotadi. Oxirgi blok esa "
                "ogohlantiradi: yechimni sezilarli "
                "buzganimizda ham qoldiq juda kichik "
                "qoladi. Demak 'qoldiq kichik — "
                "yechim to'g'ri' degan xulosa yomon "
                "shartlangan tizimda **noto'g'ri**."
            ),
            mistakes=[
                "Yomon shartlanganlikni algoritm "
                "aybi deb hisoblash. $\\kappa$ — "
                "masalaning xossasi; hech qanday "
                "algoritm uni yaxshilamaydi.",
                "Kichik qoldiqqa asoslanib yechimni "
                "to'g'ri deb qabul qilish. Yomon "
                "shartlangan tizimda qoldiq "
                "aldamchi.",
                "Birliklardan kelgan sun'iy "
                "shartlanganlik bilan kurashish. "
                "Diagonal masshtablash uni bepul "
                "yo'qotadi.",
                "$\\kappa$ ni hisoblash uchun "
                "matritsani to'liq teskarilash. "
                "Buning o'rniga baholash "
                "algoritmlari (condest) "
                "ishlatiladi.",
                "Deyarli mexanizm bo'lgan modelni "
                "chiziqli tahlil qilish. Geometrik "
                "nochiziqlilik majburiy.",
            ],
            quiz=[
                q("Shartlanganlik soni nimani "
                  "o'lchaydi?",
                  "Kirish ma'lumotidagi nisbiy "
                  "xatoning yechimdagi nisbiy xatoga "
                  "maksimal kuchayish "
                  "koeffitsientini: "
                  "$\\|\\delta u\\|/\\|u\\| \\le "
                  "\\kappa\\|\\delta f\\|/\\|f\\|$.",
                  "konseptual"),
                q("$\\kappa$ ning mexanik ma'nosi "
                  "nima?",
                  "Eng bikr va eng yumshoq "
                  "deformatsiya rejimlarining "
                  "bikrliklari nisbati "
                  "($\\lambda_{max}/\\lambda_{min}$).",
                  "talqin"),
                q("$\\kappa = 10^{12}$ bo'lsa "
                  "`double` da nechta ishonchli "
                  "raqam qoladi?",
                  "$16 - 12 = 4$ ta. Bu juda kam — "
                  "natijani albatta tekshirish "
                  "kerak.", "hisob"),
                q("Kodda nima uchun bir xil masala "
                  "metr va millimetrda "
                  "hisoblanadi?",
                  "Birlik o'zgarishi $\\kappa$ ni "
                  "tartiblarga o'zgartirishini, "
                  "ya'ni bu shartlanganlik **sun'iy** "
                  "ekanini ko'rsatish uchun; Yakobi "
                  "shartlashdan keyin ikkalasi bir "
                  "xil qiymat beradi.", "kod"),
                q("Yomon shartlangan masala bilan "
                  "nobarqaror algoritm nima bilan "
                  "farq qiladi?",
                  "Birinchisi masalaning xossasi — "
                  "hech qanday algoritm yordam "
                  "bermaydi; ikkinchisi algoritmning "
                  "kamchiligi — uni almashtirish "
                  "kifoya.", "konseptual"),
                q("Yupqa qobiq elementlarida "
                  "$\\kappa$ nima uchun katta?",
                  "Membrana bikrligi $\\sim Eh$, "
                  "egilish bikrligi $\\sim Eh^3$ — "
                  "ularning nisbati $(L/h)^2$ "
                  "tartibida; $L/h = 100$ da "
                  "$\\kappa \\sim 10^4$.", "talqin"),
            ],
            bridge=(
                "Endi tizimning qanchalik 'qiyin' "
                "ekanini baholashni bilamiz. Keyingi "
                "qadam — uni haqiqatan yechish. "
                "Mexanikadagi bikrlik matritsalari "
                "maxsus tuzilishga ega: ular "
                "simmetrik, musbat aniqlangan va "
                "siyrak. Keyingi mavzuda shu "
                "xossalardan foydalanadigan to'g'ri "
                "yechish usullarini — LU, Cholesky "
                "va lenta algoritmlarini — quramiz."
            ),
            research=(
                "Oldindan shartlash usullarini "
                "o'rganing. (1) Yakobi, SSOR va "
                "to'liq bo'lmagan Cholesky (IC(0)) "
                "shartlagichlarini FEM matritsasida "
                "taqqoslang: qaysi biri $\\kappa$ ni "
                "ko'proq kamaytiradi va qanday "
                "narxga? (2) Ko'p to'rli (multigrid) "
                "usulning shartlagich sifatidagi "
                "roli — nima uchun u to'r "
                "zichligidan **mustaqil** "
                "yaqinlashish beradi? (3) Teskari "
                "masalalarda (eksperimental "
                "ma'lumotdan yuklamani tiklash) "
                "Tixonov regulyarizatsiyasini "
                "o'rganing: u xos bo'lmagan "
                "masalani qanday xos qiladi va "
                "regulyarizatsiya parametri qanday "
                "tanlanadi (L-egri chiziq usuli)?"
            ),
            manim_ref=manim(
                scene="ConditioningScene",
                module="manim/scenes/su_basics.py",
                title="Shartlanganlik va deyarli parallel chiziqlar",
                summary=(
                    "Ikkita tenglama tekislikda "
                    "chiziq sifatida chiziladi; "
                    "ularning burchagi kamaygani "
                    "sari kesishuv nuqtasining "
                    "noaniqlik sohasi cho'zilgan "
                    "ellipsga aylanadi va keskin "
                    "kattalashadi. Keyin deyarli "
                    "yassi ferma ko'rsatiladi va "
                    "ko'tarilish kamaygani sari "
                    "sterjen kuchi hamda kappa "
                    "birga o'sishi namoyish etiladi."
                ),
            ),
        ),
    ),

    # ------------------------------------------------------------------ su-05
    Topic(
        id="su-05",
        subject_id=S, module_id=M, order=5,
        title="Chiziqli tizimlarni to'g'ri yechish: LU, Cholesky va lenta",
        description=(
            "Gauss usuli va LU yoyilmasi, bosh element tanlash, "
            "simmetrik musbat aniqlangan matritsalar uchun Cholesky, "
            "lenta va profil saqlash, tugunlarni qayta raqamlash."
        ),
        learning_objective=(
            "Bikrlik matritsasining tuzilishidan foydalanib mos yechish "
            "usulini tanlash, hisoblash hajmini baholash va tugunlarni "
            "qayta raqamlash bilan tejash miqdorini o'lchash."
        ),
        prerequisites=["su-04", "mq-27"],
        mathematical_core=(
            "$\\mathbf{K} = \\mathbf{L}\\mathbf{U}$, simmetrik musbat "
            "aniqlangan uchun $\\mathbf{K} = \\mathbf{L}\\mathbf{L}^T$; "
            "to'liq matritsada $O(n^3/3)$, lentada $O(nb^2)$."
        ),
        engineering_application=(
            "Har qanday FEM paketining yadrosi; katta modellarda "
            "yechish vaqti va xotira aynan shu algoritmlar bilan "
            "belgilanadi."
        ),
        computational_component=(
            "LU va Cholesky ni qo'lda amalga oshirish, lenta "
            "algoritmini qurish va qayta raqamlashning samarasini "
            "o'lchash."
        ),
        visualization_component=(
            "Matritsa to'ldirilishi (fill-in), lenta kengligi, "
            "qayta raqamlashdan oldin va keyin."
        ),
        research_extension=(
            "Cuthill–McKee va minimal daraja (minimum degree) "
            "tartiblarini taqqoslang; ko'p frontli (multifrontal) "
            "yechuvchilarning ishlash prinsipini o'rganing."
        ),
        difficulty="asosiy",
        previous_link=(
            "su-04 da bikrlik matritsasining shartlanganligi "
            "o'rganildi va u yechimning aniqligini belgilashi "
            "ko'rsatildi. Endi shu tizimni **qanday** yechishga "
            "o'tamiz va mexanik matritsalarning maxsus "
            "tuzilishidan foydalanamiz."
        ),
        next_topic="su-06",
        estimated_minutes=85,
        tags=["LU", "Cholesky", "lenta", "Cuthill-McKee"],
        lesson=_lesson(
            problem=(
                "Ko'prik modeli: 50 000 tugun, har birida 6 "
                "erkinlik darajasi — jami 300 000 "
                "noma'lum. To'liq matritsa sifatida "
                "saqlansa xotira "
                "$300000^2 \\times 8$ bayt $= 720$ "
                "gigabayt kerak bo'ladi va Gauss usuli "
                "$n^3/3 = 9\\times10^{15}$ amal talab "
                "qiladi — zamonaviy protsessorda bir "
                "necha kun. Lekin xuddi shu model FEM "
                "paketida bir necha **soniyada** "
                "yechiladi va bir necha gigabayt xotira "
                "yetadi. Farq qayerdan? Bikrlik "
                "matritsasi deyarli butunlay noldan "
                "iborat: har bir tugun faqat qo'shni "
                "tugunlar bilan bog'langan. Shu "
                "tuzilishdan qanday foydalanish kerak?"
            ),
            concepts=[
                c("LU yoyilmasi",
                  "$\\mathbf{K} = \\mathbf{L}\\mathbf{U}$ — "
                  "quyi va yuqori uchburchak "
                  "matritsalarga ajratish; Gauss "
                  "usulining matritsaviy shakli."),
                c("Cholesky yoyilmasi",
                  "Simmetrik musbat aniqlangan matritsa "
                  "uchun $\\mathbf{K} = \\mathbf{L}"
                  "\\mathbf{L}^T$ — ikki barobar tez va "
                  "ikki barobar kam xotira."),
                c("Bosh element tanlash (pivoting)",
                  "Qatorlarni almashtirib eng katta "
                  "elementni diagonalga chiqarish; "
                  "barqarorlik uchun zarur, lekin "
                  "musbat aniqlangan matritsada "
                  "**kerak emas**."),
                c("Lenta kengligi (bandwidth)",
                  "$b = \\max|i-j|$ noldan farqli "
                  "elementlar uchun; hisoblash hajmi "
                  "$O(nb^2)$ va xotira $O(nb)$."),
                c("To'ldirilish (fill-in)",
                  "Yoyilma davomida dastlab nol bo'lgan "
                  "joylarda noldan farqli elementlar "
                  "paydo bo'lishi; siyraklikni "
                  "yo'qotadi."),
                c("Qayta raqamlash (reordering)",
                  "Tugunlarni shunday tartiblashki, "
                  "lenta kengligi yoki to'ldirilish "
                  "minimal bo'lsin (Cuthill–McKee, "
                  "minimal daraja)."),
            ],
            derivation=[
                d("1. Gauss usulining bir qadami",
                  r"a^{(k+1)}_{ij} = a^{(k)}_{ij} - "
                  r"\frac{a^{(k)}_{ik}}{a^{(k)}_{kk}}"
                  r"a^{(k)}_{kj}",
                  "$k$-ustun ostidagi elementlarni "
                  "yo'qotamiz. Ko'paytuvchi "
                  "$\\ell_{ik} = a_{ik}/a_{kk}$ "
                  "saqlanadi — u $\\mathbf{L}$ ning "
                  "elementi bo'ladi."),
                d("2. LU yoyilmasi",
                  r"\mathbf{K} = \mathbf{L}\mathbf{U}, "
                  r"\quad \mathbf{L} \ \text{quyi "
                  r"(diagonalda 1)}, \ \mathbf{U} \ "
                  r"\text{yuqori uchburchak}",
                  "Gauss usuli aslida yoyilma: "
                  "$\\mathbf{U}$ — oxirgi uchburchak "
                  "shakl, $\\mathbf{L}$ — "
                  "ko'paytuvchilar. Bir marta "
                  "hisoblanib, ko'p o'ng tomon uchun "
                  "qayta ishlatiladi."),
                d("3. Ikki bosqichli yechish",
                  r"\mathbf{L}\mathbf{y} = \mathbf{f} \ "
                  r"(\text{oldinga}), \quad "
                  r"\mathbf{U}\mathbf{u} = \mathbf{y} \ "
                  r"(\text{orqaga})",
                  "Har biri $O(n^2)$ — yoyilmadan "
                  "($O(n^3/3)$) ancha arzon. Shuning "
                  "uchun ko'p yuklama holati uchun "
                  "yoyilma bir marta qilinadi."),
                d("4. Hisoblash hajmi",
                  r"\text{LU: } \frac{n^3}{3} + "
                  r"O(n^2) \ \text{amal}",
                  "$n = 10^4$ uchun $3\\times10^{11}$ "
                  "amal — bir necha daqiqa. "
                  "$n = 10^5$ uchun "
                  "$3\\times10^{14}$ — bir necha "
                  "kun. Kubik o'sish hal qiluvchi "
                  "cheklov."),
                d("5. Simmetriya va musbat aniqlanganlik",
                  r"\mathbf{K} = \mathbf{K}^T, \quad "
                  r"\mathbf{u}^T\mathbf{K}\mathbf{u} > 0 "
                  r"\ \forall \mathbf{u} \ne 0",
                  "Bikrlik matritsasi har doim "
                  "simmetrik (Betti teoremasi, "
                  "mq-26) va yetarlicha mahkamlangan "
                  "tizimda musbat aniqlangan "
                  "(deformatsiya energiyasi musbat)."),
                d("6. Cholesky yoyilmasi",
                  r"\mathbf{K} = \mathbf{L}\mathbf{L}^T, "
                  r"\quad \ell_{jj} = \sqrt{k_{jj} - "
                  r"\sum_{m<j}\ell_{jm}^2}",
                  "**Ikki barobar tejash.** Faqat "
                  "$\\mathbf{L}$ saqlanadi va amallar "
                  "soni $n^3/6$ — LU dan ikki barobar "
                  "kam. Bundan tashqari bosh element "
                  "tanlash kerak emas."),
                d("7. Musbat aniqlanganlik "
                  "diagnostikasi",
                  r"k_{jj} - \sum_{m<j}\ell_{jm}^2 \le 0 "
                  r"\;\Longrightarrow\; \mathbf{K} \ "
                  r"\text{musbat aniqlangan emas}",
                  "Ildiz ostidagi ifoda manfiy "
                  "bo'lsa — model yetarlicha "
                  "mahkamlanmagan yoki mexanizm. Bu "
                  "FEM dagi eng foydali "
                  "diagnostikalardan biri."),
                d("8. Lenta tuzilishi",
                  r"k_{ij} = 0 \ \text{agar} \ |i-j| > b "
                  r"\;\Longrightarrow\; \text{yoyilma "
                  r"lenta ichida qoladi}",
                  "**Muhim xossa.** LU va Cholesky "
                  "yoyilmasi lenta tashqarisiga "
                  "chiqmaydi — to'ldirilish faqat "
                  "lenta ichida sodir bo'ladi."),
                d("9. Lentali algoritmning hajmi",
                  r"\text{amallar: } O(nb^2), \quad "
                  r"\text{xotira: } O(nb)",
                  "$n = 3\\times10^{5}$, $b = 300$ "
                  "uchun $2{,}7\\times10^{10}$ amal — "
                  "bir necha soniya. To'liq "
                  "matritsadagi $9\\times10^{15}$ "
                  "o'rniga. **Bu 300 000 barobar "
                  "tejash.**"),
                d("10. Lenta kengligi raqamlashga "
                  "bog'liq",
                  r"b = \max_{e}\max_{i,j \in e}|i-j|",
                  "Bir xil to'r, turli raqamlash — "
                  "butunlay boshqa $b$. To'g'ri "
                  "yo'nalishda raqamlash $b$ ni "
                  "tartiblarga kamaytiradi."),
                d("11. Cuthill–McKee algoritmi",
                  r"\text{eng kam darajali tugundan "
                  r"boshlab kenglik bo'yicha "
                  r"(BFS) raqamlash}",
                  "Graf nazariyasidagi kenglik "
                  "bo'yicha qidiruv. Teskari "
                  "Cuthill–McKee (RCM) — natijani "
                  "teskarilash — odatda yanada "
                  "yaxshiroq profil beradi."),
                d("12. Siyrak yechuvchilar",
                  r"\text{to'ldirilishni minimallash} "
                  r"\ne \text{lentani minimallash}",
                  "Zamonaviy yechuvchilar lenta "
                  "o'rniga **to'ldirilishni** "
                  "minimallaydi (minimal daraja, "
                  "ajratish daraxti) — bu yanada "
                  "samarali, lekin murakkabroq."),
            ],
            meaning=(
                "Bu mavzuning amaliy og'irligi "
                "9-qadamda: mexanik masalalarda "
                "bikrlik matritsasining siyrakligidan "
                "foydalanish yechish vaqtini "
                "tartiblarga qisqartiradi. Kirish "
                "misolidagi 300 000 noma'lumli model "
                "to'liq matritsa sifatida amalda "
                "yechilmaydi, lentali algoritm bilan "
                "esa soniyalarda yechiladi. Sabab "
                "oddiy: FEM da har bir tugun faqat "
                "qo'shni tugunlar bilan bog'langan, "
                "shuning uchun matritsaning 99,9 % dan "
                "ortig'i nol. Muhim nuqta 8-qadamda: "
                "LU va Cholesky yoyilmasi lenta "
                "tashqarisiga **chiqmaydi**, ya'ni "
                "siyraklik yoyilma davomida to'liq "
                "yo'qolmaydi. Shuning uchun faqat "
                "lenta ichini saqlash va faqat u "
                "yerda hisoblash yetarli. Ikkinchi "
                "markaziy g'oya — matritsaning "
                "fizik xossalaridan foydalanish. "
                "Bikrlik matritsasi simmetrik "
                "(Betti o'zaroligi) va musbat "
                "aniqlangan (deformatsiya energiyasi "
                "musbat), demak Cholesky yoyilmasi "
                "qo'llanadi: u ikki barobar tez, "
                "ikki barobar kam xotira talab "
                "qiladi va bosh element tanlashga "
                "muhtoj emas. Oxirgisi muhim, "
                "chunki bosh element tanlash "
                "qatorlarni almashtiradi va lenta "
                "tuzilishini buzadi. Cholesky esa "
                "lentani saqlaydi. 7-qadam "
                "amaliyotda alohida qiymatga ega: "
                "Cholesky yoyilmasi ildiz ostida "
                "manfiy son bilan to'xtasa, bu "
                "modelning yetarlicha "
                "mahkanmaganini bildiradi. Bu FEM "
                "paketlaridagi 'negative pivot' "
                "yoki 'matrix not positive "
                "definite' xabarining aniq ma'nosi "
                "va u odatda chegaraviy shartlardagi "
                "xatoni yoki mexanizmni ko'rsatadi. "
                "Nihoyat, 10- va 11-qadamlar "
                "kutilmagan xulosaga olib keladi: "
                "bir xil to'rni turlicha raqamlash "
                "yechish vaqtini tartiblarga "
                "o'zgartiradi. Bu sof "
                "**nomerlash** masalasi — hech "
                "qanday fizika yo'q — lekin uning "
                "narxi juda katta."
            ),
            equations=[
                eq(r"\mathbf{K} = \mathbf{L}\mathbf{U} "
                   r"\;\Longrightarrow\; "
                   r"\mathbf{L}\mathbf{y} = \mathbf{f}, \ "
                   r"\mathbf{U}\mathbf{u} = \mathbf{y}",
                   "LU yoyilmasi va ikki bosqichli "
                   "yechish.", "LU yoyilmasi"),
                eq(r"\mathbf{K} = \mathbf{L}\mathbf{L}^T, "
                   r"\quad \ell_{jj} = \sqrt{k_{jj} - "
                   r"\sum_{m<j}\ell_{jm}^2}",
                   "Cholesky yoyilmasi — simmetrik "
                   "musbat aniqlangan matritsalar "
                   "uchun.", "Cholesky yoyilmasi"),
                eq(r"\text{to'liq: } O\Big(\frac{n^3}{3}\Big), "
                   r"\quad \text{lenta: } O(nb^2)",
                   "Hisoblash hajmining taqqoslashi.",
                   "Hisoblash hajmi"),
                eq(r"\text{xotira: } O(n^2) \to O(nb)",
                   "Lenta saqlashda xotira tejami.",
                   "Xotira"),
            ],
            conditions=(
                "**Cholesky uchun shartlar:**\n"
                "- $\\mathbf{K}$ simmetrik;\n"
                "- $\\mathbf{K}$ musbat aniqlangan.\n\n"
                "Ikkinchisi model yetarlicha "
                "mahkamlangan bo'lsa bajariladi. "
                "Qattiq jism harakati qolgan bo'lsa "
                "(mahkamlash yetishmasa) matritsa "
                "musbat yarim aniqlangan bo'ladi va "
                "Cholesky **to'xtaydi** — bu foydali "
                "diagnostika.\n\n"
                "**Bosh element tanlash qachon "
                "kerak:**\n"
                "- Simmetrik bo'lmagan tizimlarda "
                "(oqimlar, nochiziqli masalalar);\n"
                "- Musbat aniqlangan bo'lmaganda "
                "(ustuvorlikdan keyingi holat, "
                "aralash formulirovkalar);\n"
                "- Musbat aniqlangan tizimda "
                "**kerak emas** va u lentani "
                "buzadi.\n\n"
                "**Lenta algoritmi uchun:** "
                "tugunlar shunday raqamlanishi "
                "kerakki, bog'langan tugunlarning "
                "nomerlari yaqin bo'lsin. Aks holda "
                "$b$ katta bo'ladi va tejash "
                "yo'qoladi.\n\n"
                "**Xotira bahosi:** lenta "
                "saqlashda $8nb$ bayt (double). "
                "$n = 3\\times10^5$, $b = 300$ "
                "uchun 720 MB — qabul qilsa "
                "bo'ladi."
            ),
            worked=WorkedExample(
                statement=(
                    "$N \\times N$ kvadrat to'rli "
                    "plastina modeli ($N = 100$, jami "
                    "$n = 10^4$ tugun). (a) To'liq "
                    "matritsa uchun xotira va amallar "
                    "sonini hisoblang; (b) qatorma-qator "
                    "raqamlashda lenta kengligini va "
                    "tejashni toping; (c) "
                    "$N = 1000$ ($n = 10^6$) bo'lsa "
                    "nima o'zgaradi?"
                ),
                given=[
                    r"N = 100,\ n = N^2 = 10^4",
                    r"\text{double: } 8 \ \text{bayt}",
                ],
                steps=[
                    st(r"\text{(a) xotira} = n^2 \times 8 = "
                       r"10^{8} \times 8 = 800\ "
                       r"\text{MB}",
                       "To'liq matritsa — chegarada, "
                       "lekin hali mumkin."),
                    st(r"\text{amallar} = \frac{n^3}{3} = "
                       r"\frac{10^{12}}{3} = "
                       r"3{,}3\times10^{11}",
                       "Zamonaviy protsessorda "
                       "(10 Gflops) taxminan 33 "
                       "soniya."),
                    st(r"\text{(b) qatorma-qator "
                       r"raqamlash: } b = N = 100",
                       "Tugun $(i,j)$ nomeri "
                       "$iN+j$; qo'shnilari "
                       "$\\pm 1$ va $\\pm N$ — "
                       "demak $b = N$."),
                    st(r"\text{xotira} = nb \times 8 = "
                       r"10^4 \cdot 100 \cdot 8 = "
                       r"8\ \text{MB}",
                       "**100 barobar tejash** "
                       "(800 MB dan 8 MB ga)."),
                    st(r"\text{amallar} = nb^2 = "
                       r"10^4 \cdot 10^4 = 10^{8}",
                       "**3300 barobar tejash** "
                       "($3{,}3\\times10^{11}$ dan "
                       "$10^{8}$ ga) — 33 soniya "
                       "o'rniga 0,01 soniya."),
                    st(r"\text{(c) } N = 1000: \ "
                       r"n = 10^{6}, \ "
                       r"\text{to'liq xotira} = "
                       r"10^{12} \times 8 = 8\ "
                       r"\text{TB}",
                       "To'liq matritsa **butunlay "
                       "imkonsiz**."),
                    st(r"\text{to'liq amallar} = "
                       r"\frac{10^{18}}{3} = "
                       r"3{,}3\times10^{17} "
                       r"\;\Rightarrow\; \sim 1 "
                       r"\ \text{yil}",
                       "10 Gflops da bir yildan "
                       "ko'p."),
                    st(r"\text{lenta: } b = 1000, \ "
                       r"\text{xotira} = 10^{6} \cdot "
                       r"10^{3} \cdot 8 = 8\ \text{GB}",
                       "Katta, lekin zamonaviy "
                       "serverda mumkin."),
                    st(r"\text{lenta amallar} = "
                       r"nb^2 = 10^{6} \cdot 10^{6} = "
                       r"10^{12} \;\Rightarrow\; "
                       r"\sim 100\ \text{soniya}",
                       "**330 000 barobar tejash.** "
                       "Bir yildan bir necha "
                       "daqiqaga."),
                    st(r"\text{Noto'g'ri raqamlash: } "
                       r"b \sim n \;\Rightarrow\; "
                       r"nb^2 \sim n^3 "
                       r"\;\Rightarrow\; \text{tejash "
                       r"YO'Q}",
                       "Agar tugunlar tasodifiy "
                       "raqamlansa, lenta kengligi "
                       "$n$ tartibida bo'ladi va "
                       "butun afzallik yo'qoladi. "
                       "Shuning uchun qayta "
                       "raqamlash majburiy."),
                ],
                answer=(
                    "$N = 100$: to'liq matritsa "
                    "800 MB va $3{,}3\\times10^{11}$ "
                    "amal; lenta ($b = 100$) 8 MB va "
                    "$10^{8}$ amal — **100 barobar "
                    "xotira, 3300 barobar vaqt** "
                    "tejami. $N = 1000$: to'liq "
                    "matritsa 8 TB va ~1 yil (amalda "
                    "imkonsiz); lenta 8 GB va "
                    "~100 soniya — **330 000 barobar "
                    "tejash**. Noto'g'ri raqamlashda "
                    "$b \\sim n$ bo'lib, butun "
                    "afzallik yo'qoladi."
                ),
                engineering_note=(
                    "Bu hisob nima uchun FEM "
                    "paketlari katta modellarni "
                    "yecha olishini tushuntiradi va "
                    "bir muhim amaliy xulosa beradi: "
                    "to'r generatori chiqargan "
                    "tugun raqamlari deyarli har "
                    "doim yomon va paket ularni "
                    "ichki ravishda qayta "
                    "raqamlaydi. Agar siz o'z "
                    "kodingizni yozsangiz, qayta "
                    "raqamlashni unutmaslik kerak — "
                    "bu bir necha o'nlab qator kod "
                    "bo'lib, yechish vaqtini "
                    "tartiblarga qisqartiradi. "
                    "Yana bir nozik jihat: lenta "
                    "kengligi to'rning **shakliga** "
                    "bog'liq. Uzun va ingichka "
                    "sohada qisqa tomon bo'ylab "
                    "raqamlash kerak — shunda $b$ "
                    "kichik bo'ladi. Amaliyotda "
                    "zamonaviy yechuvchilar lenta "
                    "o'rniga to'liq siyrak "
                    "(sparse) saqlashni va "
                    "to'ldirilishni minimallovchi "
                    "tartiblarni ishlatadi — ular "
                    "yanada samarali, lekin asosiy "
                    "g'oya o'zgarmaydi: "
                    "siyraklikdan foydalanish."
                ),
            ),
            computation=Computation(
                caption=(
                    "LU va Cholesky yoyilmalarini "
                    "qo'lda amalga oshirish, lenta "
                    "algoritmini qurish va qayta "
                    "raqamlashning samarasini "
                    "o'lchash."
                ),
                code='''"""To'g'ri yechish usullari: LU, Cholesky va lenta."""
import numpy as np
from labkit import PARAMS, note, series, table, value

N = int(PARAMS.get("N", 12))         # to'r NxN
n_time = int(PARAMS.get("n_time", 120))
seed = int(PARAMS.get("seed", 3))


def grid_K(N, order="row"):
    """NxN to'rdagi 5 nuqtali Laplas operatori, berilgan raqamlash bilan."""
    n = N*N
    idx = np.arange(n)
    if order == "row":
        perm = idx
    elif order == "random":
        rng = np.random.default_rng(seed)
        perm = rng.permutation(n)
    else:                              # ustunma-ustun
        perm = (idx % N)*N + idx//N
    pos = np.empty(n, dtype=int)
    pos[perm] = idx
    K = np.zeros((n, n))
    for i in range(N):
        for j in range(N):
            a = pos[i*N + j]
            K[a, a] += 4.0
            for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                ii, jj = i + di, j + dj
                if 0 <= ii < N and 0 <= jj < N:
                    b = pos[ii*N + jj]
                    K[a, b] -= 1.0
    return K


def bandwidth(K):
    nz = np.argwhere(np.abs(K) > 1e-14)
    return int(np.max(np.abs(nz[:, 0] - nz[:, 1]))) if len(nz) else 0


def my_cholesky(K):
    """Cholesky yoyilmasini qo'lda amalga oshirish."""
    n = K.shape[0]
    L = np.zeros_like(K)
    for j in range(n):
        s = K[j, j] - np.dot(L[j, :j], L[j, :j])
        if s <= 0:
            raise ValueError(f"musbat aniqlangan emas: j = {j}, s = {s:.3e}")
        L[j, j] = np.sqrt(s)
        for i in range(j + 1, n):
            L[i, j] = (K[i, j] - np.dot(L[i, :j], L[j, :j]))/L[j, j]
    return L


K = grid_K(N, "row")
n = K.shape[0]
value("To'r o'lchami N", float(N), "—")
value("Noma'lumlar soni n", float(n), "—")
nnz = int(np.count_nonzero(np.abs(K) > 1e-14))
value("Noldan farqli elementlar", float(nnz), "—")
value("To'ldirilganlik", nnz/n**2*100, "%")
note(f"{N}x{N} to'rda n = {n} noma'lum. Matritsaning atigi "
     f"{nnz/n**2*100:.2f} % i noldan farqli - qolgani nol. Aynan "
     f"shu siyraklikdan foydalanish kerak.")

# --- Cholesky ni QO'LDA amalga oshirish va tekshirish ---
L = my_cholesky(K)
err_chol = np.max(np.abs(L @ L.T - K))/np.max(np.abs(K))
value("Cholesky qoldig'i max|L*L^T - K|/max|K|", err_chol, "—")
Lnp = np.linalg.cholesky(K)
value("numpy bilan farq", float(np.max(np.abs(L - Lnp))), "—")
note(f"Qo'lda yozilgan Cholesky yoyilmasi L*L^T = K ni "
     f"{err_chol:.3e} nisbiy aniqlik bilan qaytardi va numpy "
     f"natijasi bilan {np.max(np.abs(L - Lnp)):.3e} farq qiladi - "
     f"algoritm to'g'ri amalga oshirilgan.")

# Yechimni tekshirish
rng = np.random.default_rng(1)
u_ex = rng.normal(size=n)
f = K @ u_ex
y = np.linalg.solve(np.tril(L), f)
u_ch = np.linalg.solve(np.triu(L.T), y)
value("Cholesky yechimining nisbiy xatosi",
      float(np.linalg.norm(u_ch - u_ex)/np.linalg.norm(u_ex)), "—")
note("Ma'lum yechimdan o'ng tomon qurildi (ishlab chiqilgan yechimlar "
     "usuli, su-28) va Cholesky uni mashina aniqligida tikladi.")

# --- Musbat aniqlanganlik diagnostikasi ---
K_bad = K.copy()
K_bad[0, 0] -= 4.0        # tugunni 'bo'shatamiz' -> mexanizm
try:
    my_cholesky(K_bad)
    note("K_bad uchun Cholesky to'xtamadi.")
except ValueError as exc:
    value("Buzilgan matritsa aniqlandi", 1.0, "—")
    note(f"Bir tugunning mahkamlanishi olib tashlanganda Cholesky "
         f"yoyilmasi to'xtadi: {exc}. Bu FEM paketlaridagi "
         f"'negative pivot' / 'matrix not positive definite' "
         f"xabarining aynan sababi - model yetarlicha mahkamlanmagan.")
value("K ning eng kichik xususiy qiymati",
      float(np.min(np.linalg.eigvalsh(K))), "—")
value("K_bad ning eng kichik xususiy qiymati",
      float(np.min(np.linalg.eigvalsh(K_bad))), "—")

# --- Lenta kengligi va raqamlash ---
rows = []
for name, od in (("qatorma-qator", "row"), ("ustunma-ustun", "col"),
                 ("tasodifiy", "random")):
    Ko = grid_K(N, od)
    b = bandwidth(Ko)
    Lo = np.linalg.cholesky(Ko)
    fill = int(np.count_nonzero(np.abs(Lo) > 1e-12))
    tri = n*(n + 1)//2
    rows.append([name, b, n*b, fill, f"{fill/tri*100:.1f}"])
table("Raqamlashning lenta kengligiga va to'ldirilishiga ta'siri",
      ["Raqamlash", "lenta b", "lenta xotirasi n*b",
       "L dagi noldan farqli", "to'liq L ning % i"], rows)

b_row = bandwidth(grid_K(N, "row"))
b_rand = bandwidth(grid_K(N, "random"))
value("Lenta kengligi (qatorma-qator)", float(b_row), "—")
value("Lenta kengligi (tasodifiy)", float(b_rand), "—")
value("Tasodifiy raqamlash lentani necha marta kengaytirdi",
      b_rand/b_row, "marta")
value("Amallar nisbati n*b^2", (b_rand/b_row)**2, "marta")
note(f"Bir xil to'r, bir xil fizika - faqat TUGUN RAQAMLARI "
     f"o'zgartirildi. Lenta kengligi {b_row} dan {b_rand} ga chiqdi "
     f"({b_rand/b_row:.1f} marta), amallar soni esa n*b^2 bo'lgani "
     f"uchun {(b_rand/b_row)**2:.0f} marta ko'paydi. Qayta raqamlash "
     f"sof nomerlash masalasi, lekin narxi juda katta.")

# --- Hisoblash hajmining n ga bog'liqligi ---
Ns = np.arange(4, min(N + 10, 26))
full_ops, band_ops, bws = [], [], []
for Nk in Ns:
    nk = Nk*Nk
    bk = bandwidth(grid_K(int(Nk), "row"))
    bws.append(bk)
    full_ops.append(nk**3/3)
    band_ops.append(nk*bk**2)
series("To'liq matritsa: n^3/3", (Ns**2).tolist(), full_ops,
       xlabel="noma'lumlar soni n", ylabel="amallar soni")
series("Lenta: n*b^2", (Ns**2).tolist(), band_ops,
       xlabel="noma'lumlar soni n", ylabel="amallar soni")
series("Lenta kengligi b(n)", (Ns**2).tolist(),
       [float(x) for x in bws],
       xlabel="noma'lumlar soni n", ylabel="lenta kengligi b")
pf = np.polyfit(np.log(Ns**2), np.log(full_ops), 1)[0]
pb = np.polyfit(np.log(Ns**2), np.log(band_ops), 1)[0]
value("To'liq usulning o'lchangan tartibi", float(pf), "—")
value("Lentali usulning o'lchangan tartibi", float(pb), "—")
note(f"Log-log qiyaliklar: to'liq matritsa uchun {pf:.2f} (nazariya 3), "
     f"lentali algoritm uchun {pb:.2f}. Kvadrat to'rda b ~ sqrt(n), "
     f"demak n*b^2 ~ n^2 - nazariya 2 beradi. Farq o'sib boradi: "
     f"n katta bo'lgani sari lentali usul tobora ustunroq.")

# --- Xotira va vaqt bahosi (amaliy o'lchamlar uchun) ---
rows2 = []
for Nk in [100, 300, 1000, 3000]:
    nk = Nk*Nk
    bk = Nk
    mem_full = nk**2*8/1e9
    mem_band = nk*bk*8/1e9
    ops_full = nk**3/3
    ops_band = nk*bk**2
    rows2.append([f"{Nk}", f"{nk:.1e}",
                  f"{mem_full:.3g}", f"{mem_band:.3g}",
                  f"{ops_full:.2e}", f"{ops_band:.2e}",
                  f"{ops_full/ops_band:.1e}"])
table("Amaliy o'lchamlarda xotira (GB) va amallar soni",
      ["N", "n", "to'liq, GB", "lenta, GB", "to'liq amal",
       "lenta amal", "tejash"], rows2)
note("N = 1000 (n = 1e6) da to'liq matritsa 8 TB xotira va ~1 yil "
     "talab qiladi; lentali algoritm esa 8 GB va ~100 soniya. "
     "Aynan shu sabab FEM paketlari million darajali modellarni "
     "yecha oladi.")

table("Yechish usullarini tanlash",
      ["Matritsa xossasi", "Usul", "Amallar", "Izoh"],
      [["Umumiy", "LU + bosh element", "n^3/3", "eng universal"],
       ["Simmetrik musbat aniq.", "Cholesky", "n^3/6",
        "2x tez, pivot kerak emas"],
       ["Lentali SPD", "lentali Cholesky", "n*b^2",
        "FEM uchun asosiy"],
       ["Siyrak SPD", "siyrak Cholesky + tartib", "~n^1.5",
        "zamonaviy standart"],
       ["Juda katta", "iterativ (su-06)", "~n per iter",
        "xotira tejaydi"]])
''',
                parameters=[
                    p("N", "To'r o'lchami N (N×N tugun)", 4.0, 26.0, 12.0,
                      1.0),
                    p("n_time", "Vaqt bahosi uchun o'lcham", 20.0, 500.0,
                      120.0, 10.0),
                    p("seed", "Tasodifiy raqamlash urug'i", 0.0, 100.0, 3.0,
                      1.0),
                ],
                expected_output=(
                    "Qo'lda yozilgan Cholesky yoyilmasi "
                    "$\\mathbf{L}\\mathbf{L}^T = "
                    "\\mathbf{K}$ ni mashina aniqligida "
                    "qaytaradi va numpy natijasi bilan "
                    "mos tushadi. Bitta tugunning "
                    "mahkamlanishi olib tashlanganda "
                    "yoyilma manfiy ildiz ostida "
                    "to'xtaydi — 'negative pivot' "
                    "diagnostikasi. Tasodifiy raqamlash "
                    "lenta kengligini bir necha barobar "
                    "kengaytiradi va amallar sonini "
                    "uning kvadratiga mutanosib "
                    "oshiradi. Log–log qiyaliklar: "
                    "to'liq usul uchun ≈ 3, lentali "
                    "usul uchun ≈ 2 (kvadrat to'rda "
                    "$b \\sim \\sqrt{n}$)."
                ),
            ),
            visual=vis(
                kind="Matritsa tuzilishi va to'ldirilish",
                tool="React/SVG",
                description=(
                    "Siyraklik naqshi, lenta kengligi "
                    "va raqamlashning ta'siri."
                ),
                how_to_draw=(
                    "React/SVG: markazda matritsaning "
                    "**siyraklik naqshi** (spy plot) — "
                    "har bir noldan farqli element "
                    "kichik kvadrat sifatida. Uchta "
                    "naqsh yonma-yon: qatorma-qator, "
                    "ustunma-ustun va tasodifiy "
                    "raqamlash. Birinchisida aniq "
                    "**lenta** ko'rinadi, oxirgisida "
                    "nuqtalar butun maydonga "
                    "sochilgan — farq bir qarashda "
                    "tushunarli. Har bir naqsh ustida "
                    "$b$ va $nb^2$ qiymatlari "
                    "yoziladi. Pastda xuddi shu "
                    "matritsalarning Cholesky "
                    "omilining naqshi qo'yiladi va "
                    "**to'ldirilish** boshqa rangda "
                    "belgilanadi: dastlab nol bo'lgan, "
                    "keyin to'lgan joylar. Lentali "
                    "holatda to'ldirilish lenta "
                    "ichida qoladi, tasodifiy holatda "
                    "esa butun uchburchakni "
                    "egallaydi. O'ngda log–log "
                    "grafik: $n^3/3$ va $nb^2$ "
                    "chiziqlari, ular orasidagi "
                    "masofa shtrixlanadi va "
                    "'tejash' deb belgilanadi."
                ),
            ),
            interp=(
                "Cholesky yoyilmasini qo'lda amalga "
                "oshirish va uni ikki yo'l bilan "
                "tekshirish — $\\mathbf{L}\\mathbf{L}^T "
                "= \\mathbf{K}$ qoldig'i hamda numpy "
                "bilan taqqoslash — algoritmning "
                "to'g'riligini kafolatlaydi. Yechim "
                "esa ma'lum javobdan qurilgan o'ng "
                "tomon orqali tekshiriladi; bu "
                "**ishlab chiqilgan yechimlar usuli** "
                "(su-28) ning eng sodda ko'rinishi va "
                "u butun fanda takrorlanadi. Musbat "
                "aniqlanganlik diagnostikasi amaliy "
                "jihatdan eng qimmatli qismi: bitta "
                "tugunning mahkamlanishi olib "
                "tashlanganda yoyilma manfiy ildiz "
                "ostida to'xtaydi. Bu FEM "
                "paketlaridagi eng ko'p uchraydigan "
                "xato xabarining aniq mexanizmi va "
                "u modelni tuzatishga "
                "to'g'ridan-to'g'ri yo'l ko'rsatadi. "
                "Raqamlash tajribasi esa kutilmagan "
                "xulosa beradi: bir xil to'r, bir "
                "xil fizika, bir xil yechim — "
                "faqat tugun raqamlari o'zgartirildi "
                "va hisoblash hajmi tartiblarga "
                "farq qildi. Bu sonli usullardagi "
                "muhim saboq: samaradorlik "
                "ko'pincha fizikada emas, "
                "**ma'lumotlar tuzilishida** "
                "yotadi. Nihoyat, log–log "
                "qiyaliklar nazariy baholarni "
                "tasdiqlaydi: to'liq usul uchun "
                "$n^3$, lentali usul uchun kvadrat "
                "to'rda $n^2$ (chunki "
                "$b \\sim \\sqrt n$). Ikki "
                "chiziqning ajralib borishi "
                "amaliy o'lchamlar jadvalida "
                "yakunlanadi — million noma'lumli "
                "modelda farq $10^5$ barobardan "
                "oshadi."
            ),
            mistakes=[
                "Musbat aniqlangan tizimda bosh "
                "element tanlashni qo'llash. U "
                "keraksiz va lenta tuzilishini "
                "buzadi.",
                "Matritsani to'liq (dense) saqlash. "
                "FEM matritsasining 99 % dan ortig'i "
                "nol — bu xotira va vaqtni behuda "
                "sarflaydi.",
                "Tugunlarni qayta raqamlashni "
                "o'tkazib yuborish. To'r generatori "
                "bergan tartib deyarli har doim "
                "yomon.",
                "Har bir yuklama holati uchun "
                "yoyilmani qaytadan hisoblash. "
                "Yoyilma bir marta ($n^3/3$), "
                "keyin har bir o'ng tomon uchun "
                "faqat $O(n^2)$.",
                "'Negative pivot' xabarini "
                "sonli muammo deb hisoblash. U "
                "odatda **model** xatosi: "
                "yetarlicha mahkamlanmagan yoki "
                "mexanizm.",
            ],
            quiz=[
                q("Nima uchun bikrlik matritsasi "
                  "uchun Cholesky yoyilmasi "
                  "ishlatiladi?",
                  "U simmetrik va musbat aniqlangan "
                  "(Betti o'zaroligi va musbat "
                  "deformatsiya energiyasi tufayli); "
                  "Cholesky ikki barobar tez, ikki "
                  "barobar kam xotira va bosh element "
                  "tanlashsiz ishlaydi.",
                  "konseptual"),
                q("Lentali algoritmning hisoblash "
                  "hajmi qanday?",
                  "$O(nb^2)$ amal va $O(nb)$ xotira; "
                  "to'liq matritsadagi $O(n^3/3)$ va "
                  "$O(n^2)$ o'rniga.", "konseptual"),
                q("$n = 10^4$, $b = 100$ uchun "
                  "lentali usul to'liq usuldan necha "
                  "marta tez?",
                  "$n^3/3 = 3{,}3\\times10^{11}$, "
                  "$nb^2 = 10^{8}$; nisbat "
                  "$3300$ marta.", "hisob"),
                q("Kodda Cholesky yoyilmasi nima "
                  "uchun bitta tugunning "
                  "mahkamlanishi olib tashlanganda "
                  "to'xtaydi?",
                  "Matritsa musbat aniqlangan "
                  "bo'lmay qoladi (qattiq jism "
                  "harakati paydo bo'ladi) va "
                  "ildiz ostidagi ifoda manfiy "
                  "bo'ladi.", "kod"),
                q("Tugunlarni qayta raqamlash nima "
                  "uchun kerak?",
                  "Lenta kengligi raqamlashga "
                  "bog'liq; yomon tartibda "
                  "$b \\sim n$ bo'lib, "
                  "siyraklikdan keladigan butun "
                  "afzallik yo'qoladi.", "talqin"),
                q("Bir xil matritsa bilan 100 ta "
                  "turli yuklama holatini yechish "
                  "qanchaga tushadi?",
                  "Yoyilma bir marta $n^3/3$ "
                  "(yoki $nb^2$), keyin har bir "
                  "yuklama uchun faqat oldinga va "
                  "orqaga yurish $O(n^2)$ "
                  "(lentada $O(nb)$) — juda arzon.",
                  "talqin"),
            ],
            bridge=(
                "To'g'ri usullar aniq yechim beradi "
                "va matritsani bir marta yoyib, ko'p "
                "yuklama uchun qayta ishlatish "
                "imkonini tug'diradi. Lekin ular "
                "yoyilmani **saqlashni** talab "
                "qiladi va juda katta uch o'lchovli "
                "modellarda to'ldirilish xotirani "
                "to'ldirib yuboradi. Keyingi mavzuda "
                "boshqa yondashuvni ko'ramiz: "
                "matritsani umuman yoymasdan, faqat "
                "ko'paytirish amali orqali yechimga "
                "**yaqinlashish**."
            ),
            research=(
                "Siyrak yechuvchilarni chuqurroq "
                "o'rganing. (1) Cuthill–McKee, "
                "teskari Cuthill–McKee va minimal "
                "daraja tartiblarini bir xil FEM "
                "to'rida taqqoslang: qaysi biri "
                "kamroq to'ldirilish beradi? "
                "(2) Ko'p frontli (multifrontal) "
                "yechuvchining ishlash prinsipini "
                "o'rganing: u ajratish daraxti "
                "(elimination tree) orqali "
                "qanday parallellashtiriladi? "
                "(3) Ichma-ich ajratish (nested "
                "dissection) tartibining nazariy "
                "murakkabligini isbotlang: ikki "
                "o'lchovda $O(n^{1{,}5})$, uch "
                "o'lchovda $O(n^2)$ — nima uchun "
                "3D masalalar sezilarli qiyin?"
            ),
            manim_ref=manim(
                scene="FactorizationScene",
                module="manim/scenes/su_basics.py",
                title="Lenta, to'ldirilish va qayta raqamlash",
                summary=(
                    "Matritsaning siyraklik naqshi "
                    "ko'rsatiladi va Cholesky "
                    "yoyilmasi qadam-baqadam "
                    "bajariladi; to'ldirilish "
                    "boshqa rangda paydo bo'ladi va "
                    "u lenta ichida qolishi "
                    "ko'rinadi. Keyin tugunlar "
                    "tasodifiy qayta raqamlanadi va "
                    "xuddi shu yoyilma butun "
                    "uchburchakni to'ldirib "
                    "yuborishi namoyish etiladi."
                ),
            ),
        ),
    ),
]
