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
]
