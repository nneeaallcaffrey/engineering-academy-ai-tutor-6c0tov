"""TMM / 4-modul: To'lqinlar, plastiklik va reologiya (tmm-20 … tmm-24)."""

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

S = "tutash-muhitlar"
M = "tmm-m4"


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
    # ------------------------------------------------------------------ tmm-20
    Topic(
        id="tmm-20",
        subject_id=S, module_id=M, order=20,
        title="Elastik muhitda to'lqin tarqalishi: P- va S-to'lqinlar",
        description=(
            "Navye tenglamalarining dinamik holati, ko'chish maydonini "
            "potensial va solenoidal qismlarga ajratish, bo'ylama va ko'ndalang "
            "to'lqin tezliklari, sirt to'lqinlari haqida tushuncha."
        ),
        learning_objective=(
            "Dinamik Navye tenglamasidan ikkita mustaqil to'lqin tenglamasini "
            "keltirib chiqarish, $c_P$ va $c_S$ tezliklarni material doimiylari "
            "orqali hisoblash va ularning nisbatidan Puasson koeffitsientini aniqlash."
        ),
        prerequisites=["tmm-15", "nm-25"],
        mathematical_core=(
            "Gelmgols yoyilmasi $\\mathbf{u} = \\nabla\\varphi + \\nabla\\times\\boldsymbol{\\psi}$, "
            "giperbolik to'lqin tenglamasi $\\ddot{f} = c^2\\nabla^2 f$, Dalamber yechimi, "
            "dispersiya munosabati $\\omega = ck$."
        ),
        engineering_application=(
            "Ultratovushli nurayzsiz nazorat (NDT), seysmik qidiruv, zarbaviy "
            "yuklanish, akustik emissiya bilan yoriq monitoringi."
        ),
        computational_component=(
            "1D to'lqin tenglamasini aniq (explicit) markaziy-ayirmali sxema bilan "
            "yechish, CFL shartini tekshirish, $c_P/c_S$ nisbatini hisoblash."
        ),
        visualization_component=(
            "P- va S-to'lqin frontlarining animatsiyasi; zarralar harakati "
            "yo'nalishi; to'lqinning vaqt bo'yicha tarqalish diagrammasi."
        ),
        research_extension=(
            "Dispersiv to'lqinlar: qatlamli muhitda Lemb (Lamb) to'lqinlari "
            "dispersiya egri chiziqlarini quring va ularning qalinlikni "
            "o'lchashda qanday ishlatilishini tahlil qiling."
        ),
        difficulty="ilg'or",
        previous_link=(
            "tmm-19 da statik elastiklik masalasi variatsion shaklda yakunlandi. "
            "Endi inersiya hadini qaytarib, bir xil tenglamalardan dinamik "
            "hodisalarni — to'lqinlarni olamiz."
        ),
        next_topic="tmm-21",
        estimated_minutes=100,
        tags=["to'lqin", "dinamika", "elastiklik", "NDT"],
        lesson=_lesson(
            problem=(
                "Po'lat quvur devorida ichki yoriq bor-yo'qligini buzmasdan "
                "aniqlash kerak. Ultratovush datchigi devorga impuls yuboradi va "
                "qaytgan signalni qayd qiladi. Signal qancha tezlikda tarqaladi? "
                "Nega bitta impulsdan ikkita alohida qaytish keladi? Qaytish "
                "vaqtidan yoriq chuqurligini qanday hisoblash mumkin? Bu "
                "savollarga javob berish uchun elastik muhitda to'lqin "
                "tarqalishining nazariyasi kerak."
            ),
            concepts=[
                c("Bo'ylama to'lqin (P-to'lqin, longitudinal/primary wave)",
                  "Zarralar to'lqin tarqalish yo'nalishi bo'ylab tebranadi; "
                  "hajm o'zgaradi ($\\nabla\\cdot\\mathbf{u} \\neq 0$), shakl "
                  "buzilishi yo'q. Eng tez to'lqin."),
                c("Ko'ndalang to'lqin (S-to'lqin, shear/secondary wave)",
                  "Zarralar tarqalish yo'nalishiga perpendikulyar tebranadi; "
                  "hajm o'zgarmaydi ($\\nabla\\cdot\\mathbf{u} = 0$), faqat "
                  "siljish deformatsiyasi. Suyuqlikda tarqalmaydi."),
                c("Gelmgols yoyilmasi (Helmholtz decomposition)",
                  "Ixtiyoriy vektor maydonini potensialli va solenoidal "
                  "qismlarga ajratish: $\\mathbf{u} = \\nabla\\varphi + "
                  "\\nabla\\times\\boldsymbol{\\psi}$, $\\nabla\\cdot\\boldsymbol{\\psi} = 0$."),
                c("Dalamber yechimi (d'Alembert solution)",
                  "1D to'lqin tenglamasining umumiy yechimi $f(x - ct) + g(x + ct)$ — "
                  "shaklini saqlab o'ngga va chapga yuguruvchi ikki to'lqin."),
                c("CFL sharti (Courant–Friedrichs–Lewy condition)",
                  "Aniq sxemaning turg'unligi sharti $C = c\\,\\Delta t/\\Delta x \\le 1$: "
                  "sonli ma'lumot fizik to'lqindan sekin tarqalmasligi kerak."),
                c("Reley to'lqini (Rayleigh wave)",
                  "Erkin sirt bo'ylab tarqaladigan, chuqurlik bo'yicha "
                  "eksponensial so'nuvchi to'lqin; tezligi $c_R \\approx 0{,}92\\,c_S$."),
            ],
            derivation=[
                d("1. Dinamik Navye tenglamasi",
                  r"(\lambda + \mu)\nabla(\nabla\cdot\mathbf{u}) + \mu\nabla^2\mathbf{u} "
                  r"+ \rho\mathbf{b} = \rho\,\ddot{\mathbf{u}}",
                  "tmm-15 dagi statik Navye tenglamasiga inersiya hadi "
                  "$\\rho\\ddot{\\mathbf{u}}$ qo'shiladi. Hajmiy kuchni "
                  "($\\mathbf{b} = 0$) e'tiborga olmaymiz — to'lqin uzunligi "
                  "masshtabida og'irlik ahamiyatsiz."),
                d("2. Gelmgols yoyilmasini qo'llash",
                  r"\mathbf{u} = \nabla\varphi + \nabla\times\boldsymbol{\psi}, \qquad "
                  r"\nabla\cdot\boldsymbol{\psi} = 0",
                  "Ixtiyoriy silliq vektor maydonini shu ko'rinishda yozish mumkin. "
                  "$\\varphi$ — skalyar potensial (hajm o'zgarishi), "
                  "$\\boldsymbol{\\psi}$ — vektor potensial (burilish)."),
                d("3. Divergensiya va rotorning xossalari",
                  r"\nabla\cdot(\nabla\times\boldsymbol{\psi}) = 0, \qquad "
                  r"\nabla\times(\nabla\varphi) = \mathbf{0}",
                  "Bu ikki ayniyat yoyilmaning ikki qismini bir-biridan ajratish "
                  "imkonini beradi: $\\nabla\\cdot\\mathbf{u} = \\nabla^2\\varphi$, "
                  "$\\nabla\\times\\mathbf{u} = -\\nabla^2\\boldsymbol{\\psi}$."),
                d("4. Yoyilmani Navye tenglamasiga qo'yish",
                  r"\nabla\Big[(\lambda + 2\mu)\nabla^2\varphi - \rho\ddot{\varphi}\Big] "
                  r"+ \nabla\times\Big[\mu\nabla^2\boldsymbol{\psi} - \rho\ddot{\boldsymbol{\psi}}\Big] = \mathbf{0}",
                  "$\\nabla^2\\mathbf{u} = \\nabla(\\nabla\\cdot\\mathbf{u}) - "
                  "\\nabla\\times(\\nabla\\times\\mathbf{u})$ ayniyatidan foydalanib "
                  "hadlarni gradiyent va rotor ostiga yig'amiz."),
                d("5. Ikkita mustaqil to'lqin tenglamasi",
                  r"\ddot{\varphi} = c_P^2\nabla^2\varphi, \qquad "
                  r"\ddot{\boldsymbol{\psi}} = c_S^2\nabla^2\boldsymbol{\psi}",
                  "Kvadrat qavslar alohida-alohida nolga teng bo'lishi kifoya "
                  "(va umumiy holda zarur). Ikkita mustaqil to'lqin turi ajraladi — "
                  "ular bir-biridan mustaqil tarqaladi."),
                d("6. To'lqin tezliklari",
                  r"c_P = \sqrt{\frac{\lambda + 2\mu}{\rho}} = "
                  r"\sqrt{\frac{E(1-\nu)}{\rho(1+\nu)(1-2\nu)}}, \qquad "
                  r"c_S = \sqrt{\frac{\mu}{\rho}} = \sqrt{\frac{E}{2\rho(1+\nu)}}",
                  "Lame doimiylarini $E, \\nu$ orqali ifodalasak (tmm-14), "
                  "tezliklar faqat material xossalariga bog'liq bo'ladi — "
                  "chastotaga emas, ya'ni cheksiz muhitda dispersiya yo'q."),
                d("7. Tezliklar nisbatidan Puasson koeffitsienti",
                  r"\frac{c_P}{c_S} = \sqrt{\frac{2(1-\nu)}{1-2\nu}} \;\Longrightarrow\; "
                  r"\nu = \frac{(c_P/c_S)^2 - 2}{2\big[(c_P/c_S)^2 - 1\big]}",
                  "Amaliy jihatdan muhim natija: ikkita tezlikni o'lchab, "
                  "materialning $\\nu$ sini buzmasdan aniqlash mumkin. "
                  "$\\nu = 0{,}25$ uchun $c_P/c_S = \\sqrt{3} \\approx 1{,}73$."),
            ],
            meaning=(
                "$c_P = \\sqrt{(\\lambda + 2\\mu)/\\rho}$ formulasidagi surat — "
                "bir o'lchovli siqilishga qarshilik (bikrlik), maxraj — inersiya. "
                "Har qanday to'lqin tezligi shu ikki raqobatchi effektning "
                "nisbatidan kelib chiqadi: material qanchalik bikr bo'lsa, "
                "to'lqin shuncha tez; qanchalik og'ir bo'lsa, shuncha sekin. "
                "$c_S$ da faqat $\\mu$ turadi, chunki ko'ndalang to'lqinda hajm "
                "o'zgarmaydi va hajmiy bikrlik $K$ ishtirok etmaydi. Shuning uchun "
                "suyuqlikda ($\\mu = 0$) S-to'lqin umuman tarqalmaydi — Yer "
                "yadrosining suyuq ekanligi aynan shu faktdan aniqlangan. "
                "$c_P > c_S$ har doim bajariladi, chunki $\\lambda + 2\\mu > \\mu$."
            ),
            equations=[
                eq(r"\ddot{\varphi} = c_P^2\nabla^2\varphi",
                   "Bo'ylama (P) to'lqin tenglamasi.", "P-to'lqin tenglamasi"),
                eq(r"\ddot{\boldsymbol{\psi}} = c_S^2\nabla^2\boldsymbol{\psi}",
                   "Ko'ndalang (S) to'lqin tenglamasi.", "S-to'lqin tenglamasi"),
                eq(r"u(x, t) = f(x - c t) + g(x + c t)",
                   "1D Dalamber yechimi — shaklini saqlovchi ikki to'lqin.",
                   "Dalamber yechimi"),
                eq(r"Z = \rho c_P",
                   "Akustik impedans; ikki muhit chegarasida qaytish "
                   "koeffitsienti $R = (Z_2 - Z_1)/(Z_2 + Z_1)$.",
                   "Akustik impedans"),
            ],
            conditions=(
                "**Boshlang'ich shartlar:** $u(x, 0) = u_0(x)$ va "
                "$\\dot{u}(x, 0) = v_0(x)$ — to'lqin tenglamasi vaqt bo'yicha "
                "ikkinchi tartibli, shuning uchun ikkita shart kerak.\n\n"
                "**Chegaraviy shartlar:**\n"
                "- Erkin sirt: $\\sigma_{ij}n_j = 0$ — to'lqin ishorasini "
                "o'zgartirmasdan qaytadi (siljish uchun $\\partial u/\\partial x = 0$);\n"
                "- Qattiq mahkamlash: $u = 0$ — to'lqin ishorasini o'zgartirib qaytadi;\n"
                "- Yutuvchi (absorbing) chegara: $\\partial u/\\partial t \\pm "
                "c\\,\\partial u/\\partial x = 0$ — cheksiz muhitni sonli "
                "modellashda qaytishni yo'q qiladi."
            ),
            worked=WorkedExample(
                statement=(
                    "Po'lat namunada ultratovush o'lchovi $c_P = 5900$ m/s va "
                    "$c_S = 3200$ m/s berdi. Zichlik $\\rho = 7850$ kg/m³. "
                    "(a) $\\nu$, $E$ va $G$ ni toping. (b) 40 mm qalinlikdagi "
                    "plastinada P-to'lqin orqa devordan qaytib kelish vaqtini "
                    "hisoblang. (c) Agar qaytish 10,2 mks da kelsa, nuqson "
                    "qaysi chuqurlikda?"
                ),
                given=[
                    r"c_P = 5900\ \text{m/s}",
                    r"c_S = 3200\ \text{m/s}",
                    r"\rho = 7850\ \text{kg/m}^3",
                    r"h = 40\ \text{mm}",
                    r"t_{\text{def}} = 10{,}2\ \mu\text{s}",
                ],
                steps=[
                    st(r"k = c_P/c_S = 5900/3200 = 1{,}844",
                       "Tezliklar nisbati — barcha keyingi hisoblarning asosi."),
                    st(r"\nu = \frac{k^2 - 2}{2(k^2 - 1)} = \frac{3{,}400 - 2}{2(3{,}400 - 1)} "
                       r"= \frac{1{,}400}{4{,}800} = 0{,}292",
                       "Po'lat uchun kutilgan qiymat $\\approx 0{,}3$ — mos keladi."),
                    st(r"G = \mu = \rho c_S^2 = 7850 \cdot 3200^2 = 80{,}4\ \text{GPa}",
                       "Siljish moduli to'g'ridan-to'g'ri $c_S$ dan olinadi."),
                    st(r"E = 2G(1 + \nu) = 2 \cdot 80{,}4 \cdot 1{,}292 = 207{,}7\ \text{GPa}",
                       "Yung moduli — po'lat uchun klassik 205–210 GPa oralig'ida."),
                    st(r"t_{\text{orqa}} = \frac{2h}{c_P} = \frac{2 \cdot 0{,}040}{5900} "
                       r"= 13{,}56\ \mu\text{s}",
                       "To'lqin borib-qaytadi, shuning uchun yo'l $2h$."),
                    st(r"d = \frac{c_P t_{\text{def}}}{2} = \frac{5900 \cdot 10{,}2\cdot10^{-6}}{2} "
                       r"= 30{,}1\ \text{mm}",
                       "Nuqson sirtdan 30,1 mm chuqurlikda — orqa devordan oldin "
                       "kelgan signal aynan shuni bildiradi."),
                ],
                answer=(
                    "$\\nu = 0{,}292$; $G = 80{,}4$ GPa; $E = 207{,}7$ GPa; "
                    "orqa devor aks-sadosi 13,56 mks da, nuqson esa 30,1 mm chuqurlikda."
                ),
                engineering_note=(
                    "Bu — ultratovushli nazoratning (UT) butun fizik asosi. "
                    "Amalda datchik 2–10 MHz chastotada ishlaydi; to'lqin uzunligi "
                    "$\\lambda = c_P/f \\approx 1$ mm, shuning uchun taxminan "
                    "$\\lambda/2$ dan katta nuqsonlar aniqlanadi. Kichikroq "
                    "yoriqlar uchun chastota oshiriladi, lekin yutilish ham ortadi."
                ),
            ),
            computation=Computation(
                caption=(
                    "1D to'lqin tenglamasini aniq markaziy-ayirmali sxema bilan "
                    "yechish, CFL turg'unligini tekshirish va tezliklardan "
                    "material doimiylarini tiklash."
                ),
                code='''"""Elastik to'lqinlar: P/S tezliklar va 1D to'lqin tenglamasi."""
import numpy as np
from labkit import PARAMS, note, series, table, value

E = float(PARAMS.get("E", 207.0)) * 1e9        # Pa
nu = float(PARAMS.get("nu", 0.3))
rho = float(PARAMS.get("rho", 7850.0))         # kg/m^3
L = float(PARAMS.get("L", 1.0))                # sterjen uzunligi, m
cfl = float(PARAMS.get("cfl", 0.9))            # Kurant soni

lam = E*nu/((1+nu)*(1-2*nu))
mu = E/(2*(1+nu))
cP = np.sqrt((lam + 2*mu)/rho)
cS = np.sqrt(mu/rho)
c_bar = np.sqrt(E/rho)                          # ingichka sterjendagi tezlik

value("Lame lambda", lam/1e9, "GPa")
value("Lame mu = G", mu/1e9, "GPa")
value("c_P", cP, "m/s")
value("c_S", cS, "m/s")
value("c_P/c_S", cP/cS, "—")
value("Sterjen tezligi c = sqrt(E/rho)", c_bar, "m/s")

# Teskari masala: tezliklardan nu ni tiklash
k = cP/cS
nu_back = (k**2 - 2)/(2*(k**2 - 1))
note(f"Tezliklar nisbatidan tiklangan nu = {nu_back:.4f} "
     f"(kiritilgan qiymat {nu:.4f}) — teskari masala ishlaydi.")

table("Turli materiallarda to'lqin tezliklari",
      ["Material", "rho, kg/m3", "E, GPa", "nu", "c_P, m/s", "c_S, m/s"],
      [[name, r, e,  n,
        round(float(np.sqrt(e*1e9*(1-n)/(r*(1+n)*(1-2*n)))), 0),
        round(float(np.sqrt(e*1e9/(2*r*(1+n)))), 0)]
       for name, r, e, n in [
           ("Po'lat", 7850, 207.0, 0.30),
           ("Alyuminiy", 2700, 70.0, 0.33),
           ("Mis", 8960, 117.0, 0.35),
           ("Beton", 2400, 30.0, 0.20),
           ("Shisha", 2500, 70.0, 0.22)]])

# --- 1D to'lqin tenglamasi: u_tt = c^2 u_xx, aniq sxema ---
nx = 401
dx = L/(nx - 1)
x = np.linspace(0.0, L, nx)
dt = cfl*dx/c_bar
nt = int(0.6*L/c_bar/dt)

# Boshlang'ich impuls — Gauss cho'qqisi (tinch holatdan)
u_prev = np.exp(-((x - 0.25*L)/(0.03*L))**2)
u_curr = u_prev.copy()          # nol boshlang'ich tezlik
snapshots = {0: u_curr.copy()}

C2 = (c_bar*dt/dx)**2
for n in range(1, nt + 1):
    u_next = np.zeros_like(u_curr)
    u_next[1:-1] = (2*u_curr[1:-1] - u_prev[1:-1]
                    + C2*(u_curr[2:] - 2*u_curr[1:-1] + u_curr[:-2]))
    u_next[0] = 0.0             # chap chekka: qattiq mahkamlangan
    u_next[-1] = u_next[-2]     # o'ng chekka: erkin sirt
    u_prev, u_curr = u_curr, u_next
    if n in (nt//3, 2*nt//3, nt):
        snapshots[n] = u_curr.copy()

for n, snap in snapshots.items():
    series(f"u(x) t = {n*dt*1e6:.1f} mks", x.tolist(), snap.tolist(),
           xlabel="x, m", ylabel="Ko'chish (normallashtirilgan)")

amp = float(np.max(np.abs(u_curr)))
value("CFL soni", cfl, "—")
value("dt", dt*1e9, "ns")
value("Yakuniy maksimal amplituda", amp, "—")
if cfl <= 1.0:
    note(f"CFL = {cfl:.2f} <= 1 — sxema turg'un, amplituda {amp:.3f} "
         f"(boshlang'ich 1.0 atrofida saqlanishi kerak).")
else:
    note(f"CFL = {cfl:.2f} > 1 — sxema TURG'UN EMAS: amplituda {amp:.3e} "
         f"gacha portladi. Bu sonli artefakt, fizik hodisa emas.")

# Aks-sado vaqtlari (NDT uchun)
h = 0.040
value("40 mm plastinada orqa devor aks-sadosi", 2*h/cP*1e6, "mks")
value("Bir xil vaqtda S-to'lqin yo'li", 2*h/cS*1e6, "mks")
note("Bitta impulsdan ikkita aks-sado kelishining sababi shu: P- va "
     "S-to'lqinlar bir xil masofani turli vaqtda bosib o'tadi.")
''',
                parameters=[
                    p("E", "Yung moduli", 10.0, 400.0, 207.0, 1.0, "GPa"),
                    p("nu", "Puasson koeffitsienti", 0.0, 0.49, 0.3, 0.01),
                    p("rho", "Zichlik", 1000.0, 12000.0, 7850.0, 50.0, "kg/m³"),
                    p("L", "Sterjen uzunligi", 0.2, 3.0, 1.0, 0.1, "m"),
                    p("cfl", "Kurant soni C", 0.2, 1.4, 0.9, 0.05),
                ],
                expected_output=(
                    "c_P ≈ 5920 m/s, c_S ≈ 3160 m/s, c_P/c_S ≈ 1,87; tiklangan "
                    "ν = 0,300. CFL ≤ 1 da to'lqin shaklini saqlaydi, CFL > 1 da "
                    "yechim eksponensial portlaydi."
                ),
            ),
            visual=vis(
                kind="To'lqin tarqalishi va zarralar harakati",
                tool="React/SVG + Matplotlib",
                description=(
                    "P- va S-to'lqin frontlari, zarralarning tebranish yo'nalishi "
                    "va 1D to'lqinning vaqt bo'yicha kadrlari."
                ),
                how_to_draw=(
                    "React/SVG: gorizontal chiziqda teng oraliqli nuqtalar qatori "
                    "chiziladi. P-to'lqin uchun nuqtalar $x$ bo'ylab "
                    "$A\\sin(kx - \\omega t)$ ga siljiydi (zichlanish–siyraklanish "
                    "ko'rinadi), S-to'lqin uchun $y$ bo'ylab siljiydi. Vaqt "
                    "`requestAnimationFrame` bilan yuritiladi. Ikkita qator "
                    "yonma-yon chizilsa, farq darhol ko'rinadi. Sonli yechim "
                    "kadrlari `series()` natijalaridan chiziqli grafik sifatida "
                    "chiziladi — har bir kadr alohida rangda, legendada vaqt."
                ),
            ),
            interp=(
                "Sonli tajriba ikki muhim xulosa beradi. Birinchidan, CFL sharti "
                "buzilganda ($C > 1$) yechim bir necha o'nlab qadamdayoq "
                "$10^{10}$ tartibigacha portlaydi — bu material xossasi emas, "
                "balki sxemaning turg'unsizligi. Talaba grafikda buni ko'rib, "
                "sonli usullar kursiga (5-fan) tayyor bo'ladi. Ikkinchidan, "
                "$C = 1$ aynan olinganda sxema aniq Dalamber yechimini beradi "
                "(magic time step) — diskretlashtirish xatosi nolga tushadi, bu "
                "kutilmagan va chiroyli natija. Amaliy jihatdan: po'lat uchun "
                "$c_P \\approx 5900$ m/s bo'lgani uchun 40 mm devorda aks-sado "
                "13,6 mks da keladi; osilloskop ekranida undan oldinroq kelgan "
                "har qanday signal — nuqson belgisi."
            ),
            mistakes=[
                "Cheksiz muhitdagi $c_P = \\sqrt{(\\lambda + 2\\mu)/\\rho}$ ni "
                "ingichka sterjendagi $c = \\sqrt{E/\\rho}$ bilan aralashtirish. "
                "Ular har xil: sterjenda yon tomon erkin kengayadi, cheksiz "
                "muhitda esa cheklangan ($\\varepsilon_y = \\varepsilon_z = 0$).",
                "S-to'lqin suyuqlikda tarqaladi deb o'ylash. $\\mu = 0$ bo'lgani "
                "uchun $c_S = 0$ — ideal suyuqlikda ko'ndalang to'lqin yo'q.",
                "CFL shartini e'tiborsiz qoldirib, qadamni 'aniqlik uchun' "
                "kichraytirish: $\\Delta x$ ni kichraytirsangiz, $\\Delta t$ ni "
                "ham mutanosib kichraytirish shart, aks holda sxema portlaydi.",
                "Boshlang'ich shart sifatida faqat $u(x,0)$ ni berib, "
                "$\\dot{u}(x,0)$ ni unutish — natijada to'lqin bir tomonga emas, "
                "ikki tomonga teng ikkiga bo'linib ketadi (ba'zan shu kerak, "
                "lekin buni bilib qilish lozim).",
            ],
            quiz=[
                q("Nima uchun $c_P$ har doim $c_S$ dan katta?",
                  "Chunki $\\lambda + 2\\mu > \\mu$: bo'ylama to'lqin hajmiy "
                  "bikrlikka ham, siljish bikrligiga ham qarshilik ko'radi, "
                  "ko'ndalang to'lqin esa faqat siljish bikrligiga.", "konseptual"),
                q("Yer yadrosining suyuq ekanligi qanday aniqlangan?",
                  "Zilzila markazidan uzoq mintaqalarda S-to'lqinlar qayd "
                  "etilmagan — 'S-soyasi' zonasi. S-to'lqin $\\mu = 0$ bo'lgan "
                  "muhitdan o'tolmaydi, demak yadro suyuq.", "talqin"),
                q("$c_P/c_S = 2$ bo'lsa, $\\nu$ nimaga teng?",
                  "$\\nu = (4 - 2)/(2(4 - 1)) = 2/6 = 0{,}333$.", "hisob"),
                q("CFL soni $C = c\\Delta t/\\Delta x$ ning fizik ma'nosi nima?",
                  "Bir vaqt qadamida to'lqin bosib o'tgan masofaning tur "
                  "qadamiga nisbati. $C > 1$ bo'lsa, to'lqin bir qadamda "
                  "qo'shni tugundan oshib ketadi va sxema ma'lumotni "
                  "yo'qotib, turg'unsiz bo'ladi.", "kod"),
                q("Akustik impedans $Z = \\rho c$ nima uchun muhim?",
                  "Ikki muhit chegarasidan qaytish koeffitsienti $Z$ farqiga "
                  "bog'liq. Po'lat–havo chegarasida $Z$ farqi juda katta, "
                  "shuning uchun deyarli 100 % qaytadi — yoriq (havo bo'shlig'i) "
                  "shu tufayli aniq ko'rinadi.", "konseptual"),
                q("Kodda CFL ni 1,2 ga qo'ysangiz nima bo'ladi va nega?",
                  "Amplituda eksponensial o'sadi (portlaydi). Fon Neyman "
                  "tahliliga ko'ra kuchaytirish koeffitsienti moduli 1 dan "
                  "katta bo'lib qoladi — bu sonli turg'unsizlik, fizik hodisa emas.",
                  "kod"),
            ],
            bridge=(
                "Hozirgacha material chiziqli elastik deb olindi: yuk olinsa, "
                "jism to'liq tiklanadi. Lekin kuchlanish ma'lum chegaradan "
                "oshsa, qoldiq deformatsiya paydo bo'ladi. Keyingi mavzuda "
                "plastik oqishning boshlanish shartini — oqish kriteriylarini "
                "quramiz."
            ),
            research=(
                "Qatlamli plastinada tarqaluvchi Lemb (Lamb) to'lqinlarini "
                "o'rganing: ular dispersiv, ya'ni tezlik chastotaga bog'liq. "
                "Reley–Lemb dispersiya tenglamasini sonli yeching va $S_0$, "
                "$A_0$ modalar uchun $c(f h)$ egri chiziqlarini quring. Bu "
                "egri chiziqlar zamonaviy Structural Health Monitoring "
                "tizimlarida (aviatsiya paneli, quvur) qanday ishlatilishini "
                "tahlil qiling."
            ),
            manim_ref=manim(
                scene="ElasticWaveScene",
                module="animatsiya/scenes/tmm_waves.py",
                title="P- va S-to'lqinlar",
                summary=(
                    "Zarralar qatori bo'ylama to'lqinda zichlanib-siyraklanadi, "
                    "ko'ndalang to'lqinda esa ko'ndalang tebranadi; ikki front "
                    "turli tezlikda yuguradi."
                ),
            ),
        ),
    ),

    # ------------------------------------------------------------------ tmm-21
    Topic(
        id="tmm-21",
        subject_id=S, module_id=M, order=21,
        title="Plastik oqish kriteriylari: Mizes, Treska va kuchlanish fazosi geometriyasi",
        description=(
            "Oqish yuzasi tushunchasi, devyator invariantlari, Mizes va Treska "
            "kriteriylari, $\\pi$-tekislikdagi geometrik tasvir hamda "
            "gidrostatik bosimning plastiklikka ta'sirsizligi."
        ),
        learning_objective=(
            "Murakkab kuchlanish holatida plastik oqish boshlanishini $J_2$ "
            "invariant orqali aniqlash, Mizes va Treska kriteriylarini "
            "taqqoslash va ularning xavfsizlik zaxirasidagi farqini baholash."
        ),
        prerequisites=["tmm-10", "mq-22"],
        mathematical_core=(
            "Devyator $s_{ij} = \\sigma_{ij} - \\frac{1}{3}\\sigma_{kk}\\delta_{ij}$, "
            "ikkinchi invariant $J_2 = \\frac{1}{2}s_{ij}s_{ij}$, oqish yuzasi "
            "$f(\\sigma_{ij}) = 0$, $\\pi$-tekislik va gidrostatik o'q geometriyasi."
        ),
        engineering_application=(
            "Bosim ostidagi idishlar, metall shakllantirish (prokat, "
            "shtamplash), FEM paketlaridagi elastoplastik modellar, "
            "yuk ko'taruvchi konstruksiyalarning chegaraviy holati."
        ),
        computational_component=(
            "Berilgan kuchlanish tenzori uchun $\\sigma_{\\text{Mizes}}$ va "
            "$\\sigma_{\\text{Treska}}$ ni hisoblash, ikki o'lchovli "
            "kuchlanish tekisligida oqish egri chiziqlarini qurish."
        ),
        visualization_component=(
            "Mizes ellipsi va Treska olti burchagi $\\sigma_1$–$\\sigma_2$ "
            "tekisligida; $\\pi$-tekislikdagi silindr va prizma kesimi."
        ),
        research_extension=(
            "Bosimga sezgir materiallar uchun Drukker–Prager va Mor–Kulon "
            "kriteriylarini o'rganing: grunt, beton va polimerlarda oqish "
            "gidrostatik bosimga qanday bog'lanadi?"
        ),
        difficulty="murakkab",
        previous_link=(
            "tmm-10 da kuchlanish tenzorining invariantlari va devyatorga "
            "ajratish o'rganilgan edi; mq-22 da esa mustahkamlik nazariyalari "
            "bir o'lchovli tarzda berilgan edi. Endi ularni to'liq tenzor "
            "tilida umumlashtiramiz."
        ),
        next_topic="tmm-22",
        estimated_minutes=95,
        tags=["plastiklik", "Mizes", "Treska", "oqish yuzasi"],
        lesson=_lesson(
            problem=(
                "Yupqa devorli bosim idishi ichki bosim $p$ ostida ishlaydi. "
                "Devorda ikki o'qli kuchlanish holati yuzaga keladi: "
                "$\\sigma_\\theta = pR/h$ va $\\sigma_z = pR/(2h)$. Oddiy "
                "cho'zish sinovida material $\\sigma_Y = 250$ MPa da oqishni "
                "boshlaydi. Ammo bu yerda bitta emas, ikkita kuchlanish bor — "
                "qaysi biri bilan solishtiramiz? Ikki o'qli holatda oqish "
                "qachon boshlanadi? Javob uchun skalyar 'ekvivalent kuchlanish' "
                "tushunchasi va oqish yuzasi kerak."
            ),
            concepts=[
                c("Oqish yuzasi (yield surface)",
                  "Kuchlanish fazosida $f(\\sigma_{ij}) = 0$ tenglamasi bilan "
                  "berilgan yuza: ichida — elastik holat, ustida — plastik oqish "
                  "boshlanishi, tashqarisi — erishib bo'lmaydigan holat (ideal "
                  "plastiklikda)."),
                c("Ekvivalent kuchlanish (equivalent/effective stress)",
                  "Murakkab kuchlanish holatini bitta skalyar bilan almashtirish: "
                  "$\\sigma_{\\text{eq}}$ shunday tanlanadiki, oqish sharti "
                  "$\\sigma_{\\text{eq}} = \\sigma_Y$ ko'rinishida yozilsin."),
                c("Devyator (deviatoric stress)",
                  "$s_{ij} = \\sigma_{ij} - \\sigma_m\\delta_{ij}$, "
                  "$\\sigma_m = \\sigma_{kk}/3$ — kuchlanishning shakl o'zgartiruvchi "
                  "qismi; hajm o'zgartiruvchi qism ajratib tashlanadi."),
                c("$\\pi$-tekislik (deviatoric plane)",
                  "Kuchlanishning bosh o'qlari fazosida $\\sigma_1 + \\sigma_2 + "
                  "\\sigma_3 = 0$ tekisligi; gidrostatik o'qqa perpendikulyar. "
                  "Oqish kriteriysi shu tekislikda o'zining haqiqiy shaklini ko'rsatadi."),
                c("Mizes kriteriysi (von Mises criterion)",
                  "Shakl o'zgarishi energiyasi kritik qiymatga yetganda oqish "
                  "boshlanadi: $\\sqrt{3J_2} = \\sigma_Y$. Silliq, differensiallanuvchi."),
                c("Treska kriteriysi (Tresca criterion)",
                  "Maksimal urinma kuchlanish kritik qiymatga yetganda oqish "
                  "boshlanadi: $\\sigma_{\\max} - \\sigma_{\\min} = \\sigma_Y$. "
                  "Burchakli, konservativ."),
            ],
            derivation=[
                d("1. Plastiklikning gidrostatik bosimga sezgirsizligi",
                  r"f(\sigma_{ij}) = f(s_{ij}), \qquad "
                  r"s_{ij} = \sigma_{ij} - \tfrac{1}{3}\sigma_{kk}\delta_{ij}",
                  "Tajriba (Bridgman) ko'rsatadiki, metallni har tomondan bir xil "
                  "bosim bilan siqish oqishga deyarli ta'sir qilmaydi: kristall "
                  "panjarada siljish dislokatsiyalar orqali boradi, siljish esa "
                  "faqat devyatordan kelib chiqadi. Demak $f$ faqat $s_{ij}$ ga bog'liq."),
                d("2. Izotropiya: faqat devyator invariantlariga bog'liqlik",
                  r"f = f(J_2, J_3), \qquad J_2 = \tfrac{1}{2}s_{ij}s_{ij}, \qquad "
                  r"J_3 = \det(s_{ij})",
                  "Izotrop material uchun oqish sharti koordinata tizimini "
                  "tanlashga bog'liq bo'lmasligi kerak, ya'ni faqat invariantlarning "
                  "funksiyasi. $J_1 = s_{kk} = 0$ ayniyat bo'lgani uchun tushib qoladi."),
                d("3. Eng sodda taxmin: faqat $J_2$",
                  r"f = J_2 - k^2 = 0",
                  "Mizes kriteriysining mohiyati: $J_3$ ni ham tashlab yuboramiz. "
                  "Bu shakl o'zgarishi energiyasining $J_2$ ga mutanosibligi bilan "
                  "asoslanadi: $U_{\\text{shakl}} = J_2/(2\\mu)$."),
                d("4. $k$ ni bir o'qli cho'zish sinovidan aniqlash",
                  r"\sigma_1 = \sigma_Y,\ \sigma_2 = \sigma_3 = 0 \;\Rightarrow\; "
                  r"s = \operatorname{diag}\big(\tfrac{2}{3}\sigma_Y, -\tfrac{1}{3}\sigma_Y, "
                  r"-\tfrac{1}{3}\sigma_Y\big) \;\Rightarrow\; J_2 = \tfrac{1}{3}\sigma_Y^2",
                  "Kalibrlash: kriteriydagi noma'lum doimiy har doim eng sodda "
                  "sinovdan topiladi. $J_2 = \\frac{1}{2}\\left(\\frac{4}{9} + "
                  "\\frac{1}{9} + \\frac{1}{9}\\right)\\sigma_Y^2 = \\frac{1}{3}\\sigma_Y^2$."),
                d("5. Mizes ekvivalent kuchlanishi",
                  r"\sigma_{\text{eq}} = \sqrt{3J_2} = "
                  r"\sqrt{\tfrac{1}{2}\big[(\sigma_1-\sigma_2)^2 + (\sigma_2-\sigma_3)^2 "
                  r"+ (\sigma_3-\sigma_1)^2\big]}",
                  "$\\sqrt{3}$ ko'paytuvchi shunday tanlanganki, bir o'qli cho'zishda "
                  "$\\sigma_{\\text{eq}} = \\sigma_1$ bo'lsin. Endi oqish sharti "
                  "oddiy: $\\sigma_{\\text{eq}} \\ge \\sigma_Y$."),
                d("6. Umumiy komponentalar orqali ifoda",
                  r"\sigma_{\text{eq}} = \sqrt{\tfrac{1}{2}\big[(\sigma_x-\sigma_y)^2 "
                  r"+ (\sigma_y-\sigma_z)^2 + (\sigma_z-\sigma_x)^2\big] "
                  r"+ 3(\tau_{xy}^2 + \tau_{yz}^2 + \tau_{zx}^2)}",
                  "Bosh kuchlanishlarni topmasdan to'g'ridan-to'g'ri hisoblash "
                  "mumkin — FEM paketlari aynan shu formulani ishlatadi."),
                d("7. Treska kriteriysi va sof siljishdagi farq",
                  r"\text{Treska: } \tau_Y = \tfrac{1}{2}\sigma_Y; \qquad "
                  r"\text{Mizes: } \tau_Y = \tfrac{1}{\sqrt{3}}\sigma_Y \approx 0{,}577\sigma_Y",
                  "Sof siljishda ($\\sigma_1 = -\\sigma_2 = \\tau$, $\\sigma_3 = 0$) "
                  "ikki kriteriy maksimal darajada ajraladi: farq "
                  "$2/\\sqrt{3} - 1 = 15{,}5\\,\\%$. Tajribalar odatda Mizesga "
                  "yaqinroq natija beradi, Treska esa xavfsizroq tomonga xato qiladi."),
            ],
            meaning=(
                "$\\sigma_{\\text{eq}} = \\sqrt{3J_2}$ formulasining har bir hadi — "
                "bosh kuchlanishlar orasidagi **farq**. Bu tasodif emas: faqat "
                "farqlar siljish deformatsiyasini keltirib chiqaradi, teng "
                "kuchlanishlar esa jismni faqat kengaytiradi yoki siqadi. "
                "Shuning uchun okean tubidagi 100 MPa gidrostatik bosim po'lat "
                "kubni plastik deformatsiyalamaydi ($\\sigma_{\\text{eq}} = 0$), "
                "lekin 100 MPa bir o'qli cho'zish uni sezilarli yuklaydi. "
                "Geometrik tilda: Mizes oqish yuzasi — gidrostatik o'q "
                "($\\sigma_1 = \\sigma_2 = \\sigma_3$) bo'ylab cheksiz cho'zilgan "
                "**doiraviy silindr**, Treska esa shu o'q atrofida **olti "
                "burchakli prizma**. Treska prizmasi Mizes silindrining ichiga "
                "chizilgan, ya'ni Treska har doim konservativroq."
            ),
            equations=[
                eq(r"\sigma_{\text{eq}}^{\text{Mizes}} = \sqrt{3J_2} = \sigma_Y",
                   "Mizes oqish sharti.", "Mizes kriteriysi"),
                eq(r"\sigma_{\max} - \sigma_{\min} = \sigma_Y",
                   "Treska oqish sharti (bosh kuchlanishlar orqali).",
                   "Treska kriteriysi"),
                eq(r"J_2 = \tfrac{1}{2}s_{ij}s_{ij} = "
                   r"\tfrac{1}{6}\big[(\sigma_1-\sigma_2)^2 + (\sigma_2-\sigma_3)^2 "
                   r"+ (\sigma_3-\sigma_1)^2\big]",
                   "Devyatorning ikkinchi invarianti.", "J₂ invariant"),
                eq(r"n = \sigma_Y/\sigma_{\text{eq}}",
                   "Plastik oqishgacha bo'lgan xavfsizlik zaxirasi koeffitsienti.",
                   "Zaxira koeffitsienti"),
            ],
            conditions=(
                "Oqish kriteriysi chegaraviy shart emas — u **material sharti** "
                "va har bir nuqtada tekshiriladi. Elastoplastik masalada u "
                "quyidagicha ishlatiladi:\n"
                "- $f(\\sigma_{ij}) < 0$ — nuqta elastik, Guk qonuni amal qiladi;\n"
                "- $f(\\sigma_{ij}) = 0$ va $\\dot{f} = 0$ — plastik yuklanish, "
                "oqish qoidasi (tmm-22) qo'shiladi;\n"
                "- $f = 0$ va $\\dot{f} < 0$ — elastik bo'shatish (unloading).\n\n"
                "Ideal plastiklikda $f > 0$ holati mumkin emas — bu "
                "**konsistentlik sharti** deb ataladi va sonli algoritmda "
                "kuchlanishni oqish yuzasiga qaytarish (return mapping) orqali "
                "ta'minlanadi."
            ),
            worked=WorkedExample(
                statement=(
                    "Yupqa devorli silindrik bosim idishi: $R = 500$ mm, "
                    "$h = 8$ mm, ichki bosim $p = 3$ MPa. Material $\\sigma_Y = "
                    "250$ MPa. (a) Mizes va Treska bo'yicha zaxira koeffitsientini "
                    "toping. (b) Qanday bosimda oqish boshlanadi?"
                ),
                given=[
                    r"R = 500\ \text{mm},\ h = 8\ \text{mm}",
                    r"p = 3\ \text{MPa}",
                    r"\sigma_Y = 250\ \text{MPa}",
                ],
                steps=[
                    st(r"\sigma_\theta = \frac{pR}{h} = \frac{3 \cdot 500}{8} = 187{,}5\ \text{MPa}",
                       "Halqaviy (okruzhnoy) kuchlanish — eng katta komponenta."),
                    st(r"\sigma_z = \frac{pR}{2h} = 93{,}75\ \text{MPa}, \qquad "
                       r"\sigma_r \approx 0",
                       "O'q bo'ylab kuchlanish ikki marta kichik; radial kuchlanish "
                       "yupqa devorda ($-p$ dan 0 gacha) e'tiborsiz."),
                    st(r"\sigma_{\text{eq}} = \sqrt{\tfrac{1}{2}\big[(187{,}5-93{,}75)^2 "
                       r"+ (93{,}75-0)^2 + (0-187{,}5)^2\big]}",
                       "Mizes formulasiga uchala bosh kuchlanishni qo'yamiz."),
                    st(r"\sigma_{\text{eq}} = \sqrt{\tfrac{1}{2}(8789 + 8789 + 35156)} "
                       r"= \sqrt{26367} = 162{,}4\ \text{MPa}",
                       "Mizes ekvivalent kuchlanishi $\\sigma_\\theta$ dan kichik — "
                       "chunki $\\sigma_z$ qisman 'yordam beradi'."),
                    st(r"\sigma_{\text{Treska}} = \sigma_{\max} - \sigma_{\min} "
                       r"= 187{,}5 - 0 = 187{,}5\ \text{MPa}",
                       "Treska bo'yicha esa to'liq $\\sigma_\\theta$ hisobga olinadi."),
                    st(r"n_{\text{Mizes}} = \frac{250}{162{,}4} = 1{,}54; \qquad "
                       r"n_{\text{Treska}} = \frac{250}{187{,}5} = 1{,}33",
                       "Treska 13,5 % konservativroq baho beradi."),
                    st(r"p_Y^{\text{Mizes}} = 3 \cdot 1{,}54 = 4{,}62\ \text{MPa}, \qquad "
                       r"p_Y^{\text{Treska}} = 4{,}00\ \text{MPa}",
                       "Kuchlanish bosimga chiziqli bog'liq bo'lgani uchun zaxira "
                       "koeffitsientini to'g'ridan-to'g'ri bosimga ko'paytiramiz."),
                ],
                answer=(
                    "$\\sigma_{\\text{eq}}^{\\text{Mizes}} = 162{,}4$ MPa, $n = 1{,}54$; "
                    "$\\sigma^{\\text{Treska}} = 187{,}5$ MPa, $n = 1{,}33$. Oqish "
                    "Mizes bo'yicha $p = 4{,}62$ MPa, Treska bo'yicha $p = 4{,}00$ MPa da boshlanadi."
                ),
                engineering_note=(
                    "ASME Boiler & Pressure Vessel Code va EN 13445 kabi standartlar "
                    "an'anaviy ravishda Treskani (yoki uning soddalashtirilgan "
                    "shaklini) ishlatgan — konservativligi uchun. Zamonaviy FEM "
                    "tahlillarida esa Mizes standart hisoblanadi, chunki u silliq "
                    "va tajribaga yaqinroq. Farq har doim Treska foydasiga "
                    "(xavfsizroq) 0–15,5 % oralig'ida."
                ),
            ),
            computation=Computation(
                caption=(
                    "Kuchlanish tenzoridan Mizes va Treska ekvivalent "
                    "kuchlanishlarini hisoblash va ikki o'lchovli oqish "
                    "egri chiziqlarini qurish."
                ),
                code='''"""Plastik oqish kriteriylari: Mizes va Treska."""
import numpy as np
from labkit import PARAMS, note, series, table, value

sx = float(PARAMS.get("sx", 187.5))     # MPa
sy = float(PARAMS.get("sy", 93.75))
sz = float(PARAMS.get("sz", 0.0))
txy = float(PARAMS.get("txy", 0.0))
sY = float(PARAMS.get("sY", 250.0))

sigma = np.array([[sx, txy, 0.0],
                  [txy, sy, 0.0],
                  [0.0, 0.0, sz]])

# Bosh kuchlanishlar (simmetrik tenzor -> haqiqiy xususiy qiymatlar)
princ = np.sort(np.linalg.eigvalsh(sigma))[::-1]
s1, s2, s3 = [float(v) for v in princ]
value("sigma_1", s1, "MPa")
value("sigma_2", s2, "MPa")
value("sigma_3", s3, "MPa")

sm = np.trace(sigma)/3.0
dev = sigma - sm*np.eye(3)
J2 = 0.5*float(np.sum(dev*dev))
J3 = float(np.linalg.det(dev))
value("Gidrostatik qism sigma_m", float(sm), "MPa")
value("J2", J2, "MPa^2")
value("J3", J3, "MPa^3")

mises = float(np.sqrt(3*J2))
tresca = s1 - s3
value("Mizes ekvivalent kuchlanish", mises, "MPa")
value("Treska ekvivalent kuchlanish", tresca, "MPa")
value("Zaxira n (Mizes)", sY/mises if mises > 0 else float("inf"), "—")
value("Zaxira n (Treska)", sY/tresca if tresca > 0 else float("inf"), "—")
value("Treska/Mizes farqi", 100*(tresca - mises)/mises if mises > 0 else 0.0, "%")

# Ikkinchi formula bilan tekshirish (komponentalar orqali)
mises2 = np.sqrt(0.5*((sx-sy)**2 + (sy-sz)**2 + (sz-sx)**2) + 3*txy**2)
note(f"Ikki xil formula bir xil natija berdi: {mises:.3f} va {float(mises2):.3f} MPa ✓")

if mises >= sY:
    note(f"OQISH BOSHLANDI (Mizes): {mises:.1f} >= {sY:.1f} MPa.")
else:
    note(f"Elastik holat: {mises:.1f} < {sY:.1f} MPa, zaxira {sY/mises:.2f}.")

# --- sigma_1 - sigma_2 tekisligida oqish egri chiziqlari (sigma_3 = 0) ---
th = np.linspace(0, 2*np.pi, 721)
# Mizes: s1^2 - s1 s2 + s2^2 = sY^2 -> parametrik ellips
a = np.cos(th); b = np.sin(th)
r_m = sY/np.sqrt(a**2 - a*b + b**2)
series("Mizes ellipsi (sigma_1)", (r_m*a).tolist(), (r_m*b).tolist(),
       xlabel="sigma_1, MPa", ylabel="sigma_2, MPa")

# Treska: max(|s1|, |s2|, |s1 - s2|) = sY
r_t = sY/np.maximum.reduce([np.abs(a), np.abs(b), np.abs(a - b)])
series("Treska olti burchagi", (r_t*a).tolist(), (r_t*b).tolist(),
       xlabel="sigma_1, MPa", ylabel="sigma_2, MPa")

# Ish nuqtasi
series("Ish nuqtasi", [s1], [s2], xlabel="sigma_1, MPa", ylabel="sigma_2, MPa")

table("Xarakterli kuchlanish holatlarida ikki kriteriy",
      ["Holat", "sigma_1", "sigma_2", "sigma_3", "Mizes", "Treska", "Farq, %"],
      [[name, p1, p2, p3,
        round(float(np.sqrt(0.5*((p1-p2)**2 + (p2-p3)**2 + (p3-p1)**2))), 1),
        round(float(max(p1, p2, p3) - min(p1, p2, p3)), 1),
        round(100*(float(max(p1, p2, p3) - min(p1, p2, p3))
                   / float(np.sqrt(0.5*((p1-p2)**2 + (p2-p3)**2 + (p3-p1)**2))) - 1), 1)]
       for name, p1, p2, p3 in [
           ("Bir o'qli cho'zish", 250.0, 0.0, 0.0),
           ("Sof siljish", 144.3, -144.3, 0.0),
           ("Ikki o'qli teng cho'zish", 250.0, 250.0, 0.0),
           ("Bosim idishi", 187.5, 93.75, 0.0),
           ("Gidrostatik siqilish", -300.0, -300.0, -300.0 + 1e-9)]])

note("Gidrostatik holatda Mizes ~ 0: har tomonlama bir xil bosim "
     "plastik oqish keltirib chiqarmaydi.")
''',
                parameters=[
                    p("sx", "σₓ", -400.0, 400.0, 187.5, 2.5, "MPa"),
                    p("sy", "σᵧ", -400.0, 400.0, 93.75, 2.5, "MPa"),
                    p("sz", "σ_z", -400.0, 400.0, 0.0, 2.5, "MPa"),
                    p("txy", "τₓᵧ", -300.0, 300.0, 0.0, 2.5, "MPa"),
                    p("sY", "Oqish chegarasi σ_Y", 50.0, 900.0, 250.0, 5.0, "MPa"),
                ],
                expected_output=(
                    "σ_eq(Mizes) = 162,4 MPa, Treska = 187,5 MPa, farq +15,5 % emas, "
                    "balki +15,4 %; zaxira 1,54 va 1,33. Grafikda Treska olti "
                    "burchagi Mizes ellipsining ichida yotadi."
                ),
            ),
            visual=vis(
                kind="Oqish yuzasi geometriyasi",
                tool="React/SVG",
                description=(
                    "$\\sigma_1$–$\\sigma_2$ tekisligida Mizes ellipsi va Treska "
                    "olti burchagi, ish nuqtasi va zaxira vektori."
                ),
                how_to_draw=(
                    "React/SVG: `series()` dan kelgan Mizes va Treska nuqtalarini "
                    "`<polyline>` sifatida chizamiz (Mizes — uzluksiz, Treska — "
                    "punktir). Koordinata o'qlari markazda kesishadi, masshtab "
                    "$\\pm 1{,}3\\sigma_Y$. Ish nuqtasi to'ldirilgan doira; "
                    "markazdan unga qadar vektor chiziladi va uni oqish "
                    "chegarasigacha davom ettiruvchi shaffof chiziq zaxirani "
                    "ko'rsatadi. Nuqta egri chiziq ichida bo'lsa — yashil, "
                    "tashqarisida — qizil (issiq/sovuq duallik). $\\pi$-tekislik "
                    "ko'rinishi uchun alohida panel: doira (Mizes) va unga "
                    "ichki chizilgan muntazam olti burchak (Treska)."
                ),
            ),
            interp=(
                "Jadvaldagi eng muhim qator — sof siljish: Treska va Mizes "
                "orasidagi farq aynan shu yerda maksimal (15,5 %). Bu shuni "
                "anglatadiki, buralish yuklanishi ustunlik qiladigan detallarda "
                "(val, prujina) kriteriy tanlash jiddiy iqtisodiy ta'sirga ega: "
                "Treska bilan hisoblangan val diametri Mizesga qaraganda "
                "taxminan 5 % katta chiqadi. Ikki o'qli teng cho'zishda esa "
                "($\\sigma_1 = \\sigma_2$, $\\sigma_3 = 0$) ikkala kriteriy bir xil "
                "javob beradi — egri chiziqlar shu nuqtada tegib o'tadi. "
                "Gidrostatik qatorda Mizes deyarli nol chiqishi — nazariyaning "
                "eng kuchli bashorati: chuqur suv osti apparati korpusi "
                "plastik oqishdan emas, balki **ustuvorlikni yo'qotishdan** "
                "(mq-25…mq-27) buziladi."
            ),
            mistakes=[
                "Mizes ekvivalent kuchlanishini kuchlanish komponentalarining "
                "yig'indisi deb tushunish. U — farqlarning kvadratik "
                "kombinatsiyasi; $\\sigma_{\\text{eq}}$ hech qachon eng katta "
                "bosh kuchlanishdan katta bo'lolmaydi (bir o'qli holatdan tashqari, "
                "u yerda teng).",
                "$\\sigma_{\\text{eq}}$ ga ishora berish. U ta'rifi bo'yicha "
                "manfiy emas — shuning uchun cho'zish va siqishni farqlamaydi. "
                "Beton, chuyan kabi materiallar uchun bu jiddiy kamchilik.",
                "Yupqa devorli idishda $\\sigma_r = -p$ ni hisobga olmaslikni "
                "unutish emas, balki aksincha — uni qalin devorli idishda "
                "e'tiborsiz qoldirish. $R/h < 10$ bo'lsa, Lame yechimi (tmm-16) kerak.",
                "Treska kriteriysida $\\sigma_{\\max}$ va $\\sigma_{\\min}$ ni "
                "faqat nolga teng bo'lmagan kuchlanishlar orasidan tanlash. "
                "$\\sigma_3 = 0$ ham bosh kuchlanish va hisobga olinishi shart.",
            ],
            quiz=[
                q("Nima uchun plastik oqish kriteriysi gidrostatik bosimga "
                  "bog'liq emas?",
                  "Metalda plastik deformatsiya dislokatsiyalarning siljishi "
                  "orqali boradi, siljish esa faqat devyator kuchlanishdan "
                  "kelib chiqadi. Bridgman tajribalari buni tasdiqlagan.",
                  "konseptual"),
                q("$\\pi$-tekislikda Mizes va Treska qanday shaklga ega?",
                  "Mizes — doira, Treska — unga ichki chizilgan muntazam olti "
                  "burchak. Uch o'lchovda esa mos ravishda silindr va prizma.",
                  "konseptual"),
                q("Sof siljishda $\\tau = 100$ MPa. $\\sigma_Y = 250$ MPa bo'lsa, "
                  "ikkala kriteriy bo'yicha zaxirani toping.",
                  "Mizes: $\\sigma_{\\text{eq}} = \\sqrt{3}\\tau = 173{,}2$ MPa, "
                  "$n = 1{,}44$. Treska: $2\\tau = 200$ MPa, $n = 1{,}25$.",
                  "hisob"),
                q("Qaysi kriteriy konservativroq va nima uchun?",
                  "Treska, chunki uning olti burchagi Mizes doirasining ichida "
                  "yotadi — ya'ni oqish erta boshlanadi deb bashorat qiladi. "
                  "Farq 0 dan 15,5 % gacha.", "talqin"),
                q("Kodda gidrostatik holat uchun nima uchun $\\sigma_3$ ga "
                  "$10^{-9}$ qo'shilgan?",
                  "Uchala kuchlanish aynan teng bo'lsa, Mizes nolga teng bo'lib, "
                  "farq hisoblashda nolga bo'lish yuz beradi. Kichik buzilish "
                  "bu sonli muammoni oldini oladi, natijaga esa ta'sir qilmaydi.",
                  "kod"),
                q("FEM natijalarida 'von Mises stress' konturi nimani ko'rsatadi?",
                  "Har bir nuqtadagi $\\sigma_{\\text{eq}}$ ni. Uni $\\sigma_Y$ "
                  "bilan taqqoslab, plastik zona qayerda paydo bo'lishini "
                  "darhol ko'rish mumkin — shuning uchun u standart tasvir.",
                  "talqin"),
            ],
            bridge=(
                "Kriteriy oqish **qachon** boshlanishini aytadi, lekin oqish "
                "**qanday** davom etishini aytmaydi: deformatsiya qaysi "
                "yo'nalishda o'sadi, oqish chegarasi ko'tariladimi? Keyingi "
                "mavzuda oqish qoidasi va mustahkamlanish modellarini quramiz."
            ),
            research=(
                "Bosimga sezgir materiallar uchun Drukker–Prager "
                "($\\sqrt{J_2} + \\alpha I_1 = k$) va Mor–Kulon kriteriylarini "
                "o'rganing. Grunt, beton va polimerlarda $\\alpha$ parametri "
                "qanday aniqlanadi? Uch o'qli siqilish sinovi (triaxial test) "
                "ma'lumotlaridan $\\alpha$ va $k$ ni eng kichik kvadratlar "
                "usuli bilan moslashtiruvchi skript yozing va Mizes bilan "
                "taqqoslang."
            ),
            manim_ref=manim(
                scene="YieldSurfaceScene",
                module="animatsiya/scenes/tmm_plasticity.py",
                title="Mizes silindri va Treska prizmasi",
                summary=(
                    "Uch o'lchovli kuchlanish fazosida gidrostatik o'q, unga "
                    "perpendikulyar $\\pi$-tekislik va ikki oqish yuzasining "
                    "kesimi ko'rsatiladi."
                ),
            ),
        ),
    ),

    # ------------------------------------------------------------------ tmm-22
    Topic(
        id="tmm-22",
        subject_id=S, module_id=M, order=22,
        title="Elastoplastik deformatsiya: oqish qoidasi va mustahkamlanish modellari",
        description=(
            "Deformatsiyaning elastik va plastik qismlarga ajralishi, "
            "assotsiativ oqish qoidasi, izotrop va kinematik mustahkamlanish, "
            "Baushinger effekti va sonli integrallash (return mapping)."
        ),
        learning_objective=(
            "Yuklanish tarixiga bog'liq elastoplastik javobni hisoblash: "
            "qoldiq deformatsiya, oqish chegarasining o'sishi va "
            "takroriy yuklanishdagi gisterezis halqasini qurish."
        ),
        prerequisites=["tmm-21", "mq-06"],
        mathematical_core=(
            "Additiv yoyilma $\\varepsilon = \\varepsilon^e + \\varepsilon^p$, "
            "oqish qoidasi $\\dot{\\varepsilon}^p_{ij} = \\dot{\\lambda}\\,"
            "\\partial f/\\partial\\sigma_{ij}$, konsistentlik sharti "
            "$\\dot{f} = 0$, mustahkamlanish moduli $H$."
        ),
        engineering_application=(
            "Metall shakllantirish (chuqur tortish, egish), avtokerpichlash "
            "(autofrettage), seysmik yuk ostidagi konstruksiyalar, "
            "past siklli charchash (low-cycle fatigue)."
        ),
        computational_component=(
            "Bir o'lchovli elastoplastik modelni return mapping algoritmi bilan "
            "integrallash; siklik yuklanishda gisterezis halqasini qurish."
        ),
        visualization_component=(
            "$\\sigma$–$\\varepsilon$ diagrammasi yuklanish–bo'shatish "
            "tarixi bilan; oqish yuzasining kengayishi va siljishi."
        ),
        research_extension=(
            "Chaboche kombinatsiyalangan (izotrop + kinematik) mustahkamlanish "
            "modelini o'rganing va uni past siklli charchash sinovi "
            "ma'lumotlariga moslashtiring."
        ),
        difficulty="ilg'or",
        previous_link=(
            "tmm-21 da oqish **boshlanish** sharti aniqlandi. Endi oqish "
            "boshlangandan keyin nima bo'lishini — deformatsiyaning "
            "yo'nalishini va oqish chegarasining evolyutsiyasini o'rganamiz."
        ),
        next_topic="tmm-23",
        estimated_minutes=100,
        tags=["plastiklik", "mustahkamlanish", "gisterezis", "return mapping"],
        lesson=_lesson(
            problem=(
                "Po'lat sim 300 MPa gacha cho'ziladi ($\\sigma_Y = 250$ MPa), "
                "keyin yuk to'liq olinadi. Sim asl uzunligiga qaytmaydi — "
                "qoldiq cho'zilish qoladi. Endi uni siqishga o'tkazsak, "
                "oqish yana 250 MPa da boshlanadimi? Tajriba ko'rsatadiki, "
                "yo'q: siqishda oqish ancha erta, taxminan 200 MPa da "
                "boshlanadi (Baushinger effekti). Bu hodisani modellash uchun "
                "oqish chegarasi qanday evolyutsiyalanishini bilish kerak."
            ),
            concepts=[
                c("Additiv yoyilma (additive decomposition)",
                  "Kichik deformatsiyalarda $\\varepsilon_{ij} = \\varepsilon^e_{ij} "
                  "+ \\varepsilon^p_{ij}$: elastik qism qaytuvchan va Guk qonuniga "
                  "bo'ysunadi, plastik qism esa qoldiq."),
                c("Oqish qoidasi (flow rule)",
                  "Plastik deformatsiya ortishining yo'nalishini belgilaydi: "
                  "$\\dot{\\varepsilon}^p_{ij} = \\dot{\\lambda}\\,\\partial g/"
                  "\\partial\\sigma_{ij}$. Agar $g = f$ bo'lsa — assotsiativ "
                  "qoida, plastik deformatsiya oqish yuzasiga normal bo'ylab boradi."),
                c("Izotrop mustahkamlanish (isotropic hardening)",
                  "Oqish yuzasi markazini o'zgartirmasdan bir tekis kengayadi: "
                  "$\\sigma_Y = \\sigma_{Y0} + H\\varepsilon^p_{\\text{eq}}$. "
                  "Cho'zish va siqishda oqish chegarasi bir xil o'sadi."),
                c("Kinematik mustahkamlanish (kinematic hardening)",
                  "Oqish yuzasi o'lchamini saqlab, markazi $\\alpha_{ij}$ "
                  "(back stress) ga siljiydi: $f = \\sqrt{3J_2(s - \\alpha)} - "
                  "\\sigma_{Y0}$. Baushinger effektini tabiiy tushuntiradi."),
                c("Baushinger effekti (Bauschinger effect)",
                  "Bir yo'nalishda plastik deformatsiyadan keyin qarama-qarshi "
                  "yo'nalishda oqish chegarasining pasayishi."),
                c("Return mapping algoritmi",
                  "Sonli integrallash sxemasi: avval elastik prediktor "
                  "(hammasi elastik deb hisoblanadi), so'ng agar oqish yuzasidan "
                  "chiqib ketilgan bo'lsa, plastik korrektor kuchlanishni "
                  "yuzaga qaytaradi."),
            ],
            derivation=[
                d("1. Deformatsiyani ajratish va Guk qonuni",
                  r"\varepsilon = \varepsilon^e + \varepsilon^p, \qquad "
                  r"\sigma = E\,\varepsilon^e = E(\varepsilon - \varepsilon^p)",
                  "Bir o'lchovli holatda. Kuchlanish faqat elastik deformatsiyaga "
                  "bog'liq — plastik qism 'yodda saqlangan' qoldiq siljish."),
                d("2. Oqish sharti mustahkamlanish bilan",
                  r"f(\sigma, \varepsilon^p) = |\sigma - \alpha| - "
                  r"\big(\sigma_{Y0} + H_{\text{iso}}\,\bar{\varepsilon}^p\big) \le 0",
                  "$\\alpha$ — back stress (kinematik qism), "
                  "$\\bar{\\varepsilon}^p = \\int|\\dot{\\varepsilon}^p|dt$ — "
                  "yig'ilgan plastik deformatsiya (izotrop qism)."),
                d("3. Oqish qoidasi (assotsiativ)",
                  r"\dot{\varepsilon}^p = \dot{\lambda}\,\frac{\partial f}{\partial\sigma} "
                  r"= \dot{\lambda}\,\operatorname{sign}(\sigma - \alpha), \qquad \dot{\lambda} \ge 0",
                  "$\\dot{\\lambda}$ — plastik ko'paytuvchi, oqish tezligining "
                  "kattaligi. Ishorasi kuchlanish yo'nalishi bilan mos: "
                  "cho'zishda cho'ziladi."),
                d("4. Konsistentlik sharti",
                  r"\dot{f} = 0 \;\Longrightarrow\; \operatorname{sign}(\sigma-\alpha)"
                  r"(\dot{\sigma} - \dot{\alpha}) - H_{\text{iso}}\dot{\bar{\varepsilon}}^p = 0",
                  "Plastik oqish davom etayotganda kuchlanish oqish yuzasida "
                  "qolishi shart — u yuzadan chiqib ketolmaydi. Bu shart "
                  "$\\dot{\\lambda}$ ni aniqlash imkonini beradi."),
                d("5. Kinematik qism (Prager qoidasi)",
                  r"\dot{\alpha} = H_{\text{kin}}\,\dot{\varepsilon}^p",
                  "Back stress plastik deformatsiya bilan chiziqli o'sadi — "
                  "eng sodda kinematik mustahkamlanish modeli."),
                d("6. Elastoplastik tangens modul",
                  r"\dot{\sigma} = E_t\,\dot{\varepsilon}, \qquad "
                  r"E_t = \frac{E\,H}{E + H}, \qquad H = H_{\text{iso}} + H_{\text{kin}}",
                  "4- va 5-qadamlarni birlashtirib $\\dot{\\lambda}$ ni yo'qotamiz. "
                  "$H \\to \\infty$ da $E_t \\to E$ (elastik), $H = 0$ da "
                  "$E_t = 0$ (ideal plastiklik) — chegaraviy hollar to'g'ri chiqadi."),
                d("7. Return mapping (implitsit integrallash)",
                  r"\sigma^{\text{trial}} = \sigma_n + E\,\Delta\varepsilon; \qquad "
                  r"\Delta\lambda = \frac{f^{\text{trial}}}{E + H}; \qquad "
                  r"\sigma_{n+1} = \sigma^{\text{trial}} - E\,\Delta\lambda\,"
                  r"\operatorname{sign}(\sigma^{\text{trial}} - \alpha_n)",
                  "Amaliy algoritm: elastik prediktor + plastik korrektor. "
                  "$f^{\\text{trial}} \\le 0$ bo'lsa, qadam elastik va korreksiya "
                  "kerak emas. Bu sxema shartsiz turg'un va aniq (bir o'lchovli "
                  "chiziqli mustahkamlanishda xatosiz)."),
            ],
            meaning=(
                "$E_t = EH/(E + H)$ formulasi — ikkita prujinaning ketma-ket "
                "ulanishiga to'liq o'xshash: umumiy moslashuvchanlik "
                "$1/E_t = 1/E + 1/H$. Bu tasodif emas — elastik va plastik "
                "mexanizmlar ketma-ket ishlaydi: umumiy deformatsiya ikkovining "
                "yig'indisi, kuchlanish esa ikkovida bir xil. Shuning uchun "
                "eng yumshoq mexanizm jarayonni boshqaradi: po'latda "
                "$H \\approx 2$ GPa $\\ll E = 200$ GPa, demak "
                "$E_t \\approx H = 1{,}98$ GPa — oqishdan keyin material "
                "taxminan 100 marta yumshoq bo'lib qoladi. Kinematik "
                "mustahkamlanishda $\\alpha$ ning ma'nosi — 'material qaysi "
                "tomonga surilganini eslab qolishi'. Cho'zishda $\\alpha > 0$ "
                "bo'lib qoladi, shuning uchun siqishda oqishgacha yo'l "
                "qisqaradi — Baushinger effekti aynan shu."
            ),
            equations=[
                eq(r"\varepsilon = \varepsilon^e + \varepsilon^p",
                   "Deformatsiyaning additiv yoyilmasi.", "Additiv yoyilma"),
                eq(r"\dot{\varepsilon}^p_{ij} = \dot{\lambda}\,"
                   r"\frac{\partial f}{\partial \sigma_{ij}}",
                   "Assotsiativ oqish qoidasi (normal qoidasi).", "Oqish qoidasi"),
                eq(r"\sigma_Y(\bar{\varepsilon}^p) = \sigma_{Y0} + H\bar{\varepsilon}^p",
                   "Chiziqli izotrop mustahkamlanish qonuni.",
                   "Mustahkamlanish qonuni"),
                eq(r"E_t = \frac{EH}{E+H}",
                   "Elastoplastik tangens modul.", "Tangens modul"),
            ],
            conditions=(
                "**Boshlang'ich holat:** $\\varepsilon^p_0 = 0$, $\\alpha_0 = 0$, "
                "$\\bar{\\varepsilon}^p_0 = 0$ — bokira (virgin) material.\n\n"
                "**Kuhn–Takker shartlari** (yuklanish/bo'shatish mantig'i):\n"
                "$$\\dot{\\lambda} \\ge 0, \\qquad f \\le 0, \\qquad \\dot{\\lambda} f = 0.$$\n"
                "Bu uch shart birgalikda: plastik oqish faqat oqish yuzasida "
                "($f = 0$) bo'lishi mumkin, yuza ichida ($f < 0$) esa "
                "$\\dot{\\lambda} = 0$, ya'ni javob elastik.\n\n"
                "**Yuklanish tarixi** masalaning kirish ma'lumoti: plastiklikda "
                "javob yo'lga bog'liq (path-dependent), shuning uchun "
                "$\\varepsilon(t)$ butun tarixi berilishi shart — faqat oxirgi "
                "qiymat yetarli emas."
            ),
            worked=WorkedExample(
                statement=(
                    "Po'lat: $E = 200$ GPa, $\\sigma_{Y0} = 250$ MPa, chiziqli "
                    "mustahkamlanish $H = 2$ GPa (yarmi izotrop, yarmi kinematik). "
                    "Namuna $\\varepsilon = 0{,}005$ gacha cho'ziladi, so'ng yuk "
                    "to'liq olinadi. (a) Maksimal kuchlanishni toping. "
                    "(b) Qoldiq deformatsiyani hisoblang. (c) Siqishda oqish "
                    "qaysi kuchlanishda boshlanadi?"
                ),
                given=[
                    r"E = 200\ \text{GPa},\ \sigma_{Y0} = 250\ \text{MPa}",
                    r"H = H_{\text{iso}} + H_{\text{kin}} = 1 + 1 = 2\ \text{GPa}",
                    r"\varepsilon_{\max} = 0{,}005",
                ],
                steps=[
                    st(r"\varepsilon_Y = \frac{\sigma_{Y0}}{E} = \frac{250}{200000} "
                       r"= 0{,}00125",
                       "Elastik chegaraga mos deformatsiya — oqish shu yerdan boshlanadi."),
                    st(r"\Delta\varepsilon^p \approx \varepsilon_{\max} - \varepsilon_Y "
                       r"\cdot \frac{E}{E} = 0{,}005 - 0{,}00125 - \Delta\varepsilon^e_{\text{qo'sh}}",
                       "Oqishdan keyin deformatsiya ortishi elastik va plastik "
                       "qismlarga $E$ va $H$ nisbatida bo'linadi."),
                    st(r"\Delta\varepsilon^p = (\varepsilon_{\max} - \varepsilon_Y)"
                       r"\frac{E}{E + H} = 0{,}00375 \cdot \frac{200}{202} = 0{,}003713",
                       "Plastik qism — deformatsiya ortishining katta qismi, "
                       "chunki $H \\ll E$."),
                    st(r"\sigma_{\max} = \sigma_{Y0} + H\,\Delta\varepsilon^p "
                       r"= 250 + 2000 \cdot 0{,}003713 = 257{,}4\ \text{MPa}",
                       "Kuchlanish atigi 7,4 MPa ga oshdi — mustahkamlanish sekin."),
                    st(r"\varepsilon^{\text{res}} = \varepsilon_{\max} - "
                       r"\frac{\sigma_{\max}}{E} = 0{,}005 - \frac{257{,}4}{200000} "
                       r"= 0{,}005 - 0{,}001287 = 0{,}003713",
                       "Bo'shatish to'liq elastik ($E$ bo'ylab), qoldiq "
                       "deformatsiya aynan $\\Delta\\varepsilon^p$ ga teng — "
                       "nazariya o'zini tekshirdi."),
                    st(r"\alpha = H_{\text{kin}}\Delta\varepsilon^p = 1000 \cdot 0{,}003713 "
                       r"= 3{,}71\ \text{MPa}; \qquad "
                       r"\sigma_Y^{\text{iso}} = 250 + 1000 \cdot 0{,}003713 = 253{,}7\ \text{MPa}",
                       "Back stress va kengaygan oqish chegarasi alohida hisoblanadi."),
                    st(r"\sigma^{\text{siqilish}}_Y = \alpha - \sigma_Y^{\text{iso}} "
                       r"= 3{,}71 - 253{,}7 = -250{,}0\ \text{MPa}",
                       "Siqishda oqish $-250$ MPa da boshlanadi — sof izotrop "
                       "model bergan $-253{,}7$ MPa dan erta. Bu Baushinger "
                       "effektining kinematik qism tufayli yuzaga kelishi."),
                ],
                answer=(
                    "$\\sigma_{\\max} = 257{,}4$ MPa; qoldiq deformatsiya "
                    "$\\varepsilon^{\\text{res}} = 0{,}00371$ (0,371 %); siqishda "
                    "oqish $-250{,}0$ MPa da, ya'ni cho'zishdagi 257,4 MPa dan "
                    "7,4 MPa erta."
                ),
                engineering_note=(
                    "Bu hisob metall listni egish texnologiyasining asosi: "
                    "shtamp chiqarilgandan keyin list qisman 'orqaga qaytadi' "
                    "(springback), qaytish miqdori aynan elastik bo'shatish "
                    "chizig'i bilan aniqlanadi. Aniq detal olish uchun shtampni "
                    "ataylab ortiqcha burish kerak — springback compensation."
                ),
            ),
            computation=Computation(
                caption=(
                    "Bir o'lchovli elastoplastik modelni return mapping bilan "
                    "integrallash: yuklanish–bo'shatish va siklik gisterezis."
                ),
                code='''"""Elastoplastiklik: return mapping va gisterezis halqasi."""
import numpy as np
from labkit import PARAMS, note, series, table, value

E = float(PARAMS.get("E", 200.0))*1e3       # MPa
sY0 = float(PARAMS.get("sY0", 250.0))       # MPa
H_iso = float(PARAMS.get("H_iso", 1000.0))  # MPa
H_kin = float(PARAMS.get("H_kin", 1000.0))  # MPa
eps_amp = float(PARAMS.get("eps_amp", 0.005))
cycles = int(PARAMS.get("cycles", 2))

H = H_iso + H_kin
Et = E*H/(E + H)
value("Elastik chegara eps_Y", sY0/E, "—")
value("Tangens modul E_t", Et, "MPa")
value("E_t/E", Et/E, "—")


def solve(eps_path):
    """Return mapping: berilgan deformatsiya tarixi uchun kuchlanish."""
    sig = 0.0          # kuchlanish
    ep = 0.0           # plastik deformatsiya
    alpha = 0.0        # back stress (kinematik)
    ebar = 0.0         # yig'ilgan plastik deformatsiya (izotrop)
    out_s, out_ep = [], []
    for i in range(len(eps_path)):
        deps = eps_path[i] - (eps_path[i-1] if i > 0 else 0.0)
        # 1) Elastik prediktor
        sig_tr = sig + E*deps
        f_tr = abs(sig_tr - alpha) - (sY0 + H_iso*ebar)
        if f_tr <= 0.0:
            sig = sig_tr                       # elastik qadam
        else:
            # 2) Plastik korrektor
            dlam = f_tr/(E + H)
            n = np.sign(sig_tr - alpha)
            sig = sig_tr - E*dlam*n
            ep += dlam*n
            alpha += H_kin*dlam*n
            ebar += dlam
        out_s.append(sig)
        out_ep.append(ep)
    return np.array(out_s), np.array(out_ep), ebar


# --- 1) Monoton yuklanish + to'liq bo'shatish ---
n1 = 200
load = np.linspace(0.0, eps_amp, n1)
unload = np.linspace(eps_amp, 0.0, n1)
path1 = np.concatenate([load, unload])
s1, ep1, _ = solve(path1)

series("Yuklanish-bo'shatish", path1.tolist(), s1.tolist(),
       xlabel="Deformatsiya eps", ylabel="Kuchlanish sigma, MPa")
value("Maksimal kuchlanish", float(np.max(s1)), "MPa")
value("Qoldiq deformatsiya", float(ep1[-1]), "—")
value("Qoldiq deformatsiya, %", 100*float(ep1[-1]), "%")
note(f"Bo'shatishdan keyin sigma = {s1[-1]:.2f} MPa (nolga yaqin), "
     f"lekin deformatsiya {ep1[-1]*100:.3f} % bo'lib qoldi — bu plastik qoldiq.")

# --- 2) Siklik yuklanish: gisterezis halqasi ---
per = 400
quarter = np.linspace(0, eps_amp, per//4)
path2 = [0.0]
for _ in range(cycles):
    path2 += list(quarter)                                  # 0 -> +A
    path2 += list(np.linspace(eps_amp, -eps_amp, per//2))    # +A -> -A
    path2 += list(np.linspace(-eps_amp, 0.0, per//4))        # -A -> 0
path2 = np.array(path2)
s2, ep2, ebar2 = solve(path2)

series("Siklik gisterezis", path2.tolist(), s2.tolist(),
       xlabel="Deformatsiya eps", ylabel="Kuchlanish sigma, MPa")
value("Yig'ilgan plastik deformatsiya", float(ebar2), "—")
value("Oxirgi oqish chegarasi (izotrop)", sY0 + H_iso*float(ebar2), "MPa")

# Sikl boshida va oxirida cho'zish/siqish oqish chegaralari
value("Siklda tarqalgan energiya (halqa yuzasi)",
      float(abs(np.trapezoid(s2, path2))) if hasattr(np, "trapezoid")
      else float(abs(np.trapz(s2, path2))), "MPa")

table("Mustahkamlanish modellarini taqqoslash",
      ["Model", "Cho'zishda oqish", "Siqishda oqish", "Baushinger"],
      [["Ideal plastik (H=0)", sY0, -sY0, "yo'q"],
       ["Sof izotrop", round(sY0 + H*0.0037, 1), round(-(sY0 + H*0.0037), 1), "yo'q"],
       ["Sof kinematik", round(sY0 + H*0.0037, 1),
        round(-sY0 + H*0.0037, 1), "to'liq"],
       ["Aralash (50/50)", round(sY0 + H*0.0037, 1),
        round(-(sY0 + H_iso*0.0037) + H_kin*0.0037, 1), "qisman"]])

note("Kinematik modelda siqish oqish chegarasi cho'zishdagidan "
     "2*alpha ga kichik — Baushinger effekti aynan shu.")
''',
                parameters=[
                    p("E", "Yung moduli", 50.0, 400.0, 200.0, 5.0, "GPa"),
                    p("sY0", "Boshlang'ich oqish chegarasi", 50.0, 900.0, 250.0, 5.0, "MPa"),
                    p("H_iso", "Izotrop mustahkamlanish H_iso", 0.0, 10000.0, 1000.0, 50.0, "MPa"),
                    p("H_kin", "Kinematik mustahkamlanish H_kin", 0.0, 10000.0, 1000.0, 50.0, "MPa"),
                    p("eps_amp", "Deformatsiya amplitudasi", 0.001, 0.03, 0.005, 0.001),
                    p("cycles", "Sikllar soni", 1.0, 6.0, 2.0, 1.0),
                ],
                expected_output=(
                    "σ_max ≈ 257,4 MPa, qoldiq deformatsiya ≈ 0,371 %, "
                    "E_t/E ≈ 0,0099. Siklik grafikda yopiq gisterezis halqasi "
                    "ko'rinadi; H_kin = 0 qilinsa halqa simmetrik bo'lib, "
                    "Baushinger effekti yo'qoladi."
                ),
            ),
            visual=vis(
                kind="σ–ε gisterezis diagrammasi",
                tool="React/SVG",
                description=(
                    "Yuklanish, bo'shatish va siklik yuklanish traektoriyalari; "
                    "qoldiq deformatsiya va gisterezis halqasi yuzasi."
                ),
                how_to_draw=(
                    "React/SVG: `series()` nuqtalarini `<path>` sifatida chizamiz, "
                    "lekin oddiy grafikdan farqli o'laroq **yo'nalish muhim** — "
                    "shuning uchun traektoriya bo'ylab har 40-nuqtada kichik "
                    "strelka (`marker-end`) qo'yiladi. Elastik qismlar sovuq "
                    "rangda, plastik qismlar issiq rangda bo'yaladi (nuqta "
                    "orasidagi qiyalikni $E$ bilan solishtirib ajratiladi). "
                    "Qoldiq deformatsiya $x$ o'qida punktir vertikal chiziq va "
                    "yorliq bilan belgilanadi. Gisterezis halqasi ichi 10 % "
                    "shaffoflik bilan to'ldiriladi — yuza tarqalgan energiyaga "
                    "mutanosib, buni matnda ham ko'rsatamiz."
                ),
            ),
            interp=(
                "Gisterezis halqasining **yuzasi** — bir siklda issiqlikka "
                "aylangan energiya. Bu past siklli charchash (low-cycle fatigue) "
                "nazariyasining o'zagi: Koffin–Menson qonuni buzilishgacha "
                "bo'lgan sikllar sonini plastik deformatsiya amplitudasi bilan "
                "bog'laydi, $\\Delta\\varepsilon^p N_f^{0{,}5} \\approx$ const. "
                "Sonli tajribada $H_{\\text{kin}}$ ni nolga tushirsangiz, halqa "
                "tezda torayadi va material 'qotib qoladi' (shakedown) — sof "
                "izotrop model siklik yuklanishda plastik deformatsiya "
                "to'planishini noto'g'ri bashorat qiladi. Aksincha, sof "
                "kinematik model barqaror halqa beradi, lekin siklik "
                "mustahkamlanishni ko'rsatmaydi. Shuning uchun amaliyotda "
                "aralash (Chaboche) modellar ishlatiladi. $E_t/E \\approx 0{,}01$ "
                "qiymati esa muhim muhandislik xulosasini beradi: oqishdan "
                "keyin konstruksiya bikrligi deyarli yo'qoladi, shuning uchun "
                "plastik zonaning kengayishi juda tez kechadi."
            ),
            mistakes=[
                "Bo'shatish ham plastik boradi deb o'ylash. Yuk kamayganda "
                "$f < 0$ bo'lib qoladi va javob qat'iy elastik — qiyalik "
                "$E_t$ emas, aynan $E$.",
                "Qoldiq deformatsiyani $\\varepsilon_{\\max} - \\varepsilon_Y$ "
                "deb hisoblash. To'g'ri qiymat $\\varepsilon_{\\max} - "
                "\\sigma_{\\max}/E$, chunki bo'shatish yangi (kattaroq) "
                "kuchlanishdan boshlanadi.",
                "Plastiklikda superpozitsiya prinsipini qo'llash. Javob "
                "yo'lga bog'liq: A yuk + B yuk $\\neq$ (A+B) yuk. Har bir "
                "yuklanish tarixi alohida integrallanishi shart.",
                "Return mapping da $\\Delta\\lambda$ ni $f^{\\text{trial}}/E$ "
                "deb olish (mustahkamlanishni unutish). To'g'ri maxraj "
                "$E + H$, aks holda kuchlanish oqish yuzasidan tashqarida qoladi.",
            ],
            quiz=[
                q("Nima uchun bo'shatish chizig'ining qiyaligi $E$ ga teng?",
                  "Bo'shatishda $f < 0$ bo'lib qoladi, plastik oqish to'xtaydi "
                  "va $\\dot{\\varepsilon}^p = 0$. Qolgan hammasi elastik, "
                  "demak $\\dot\\sigma = E\\dot\\varepsilon$.", "konseptual"),
                q("Assotsiativ oqish qoidasining geometrik ma'nosi nima?",
                  "Plastik deformatsiya ortishi vektori oqish yuzasiga tashqi "
                  "normal bo'ylab yo'nalgan. Mizes uchun bu $\\dot{\\varepsilon}^p$ "
                  "ning devyatorga parallel bo'lishini anglatadi — plastik "
                  "hajm o'zgarmaydi.", "konseptual"),
                q("$E = 200$ GPa, $H = 2$ GPa. $E_t$ ni toping va izohlang.",
                  "$E_t = 200 \\cdot 2/202 = 1{,}98$ GPa, ya'ni $E$ ning "
                  "1 % i. Oqishdan keyin material 100 marta yumshoq.", "hisob"),
                q("Baushinger effekti qaysi mustahkamlanish turi bilan "
                  "modellashtiriladi?",
                  "Kinematik: oqish yuzasi markazi $\\alpha$ ga siljiydi, "
                  "shuning uchun qarama-qarshi tomonda oqishgacha masofa "
                  "$2\\alpha$ ga qisqaradi. Izotrop model bu effektni "
                  "umuman bera olmaydi.", "talqin"),
                q("Kodda `f_tr <= 0` sharti nimani tekshiradi?",
                  "Elastik prediktor kuchlanishi oqish yuzasi ichida qolganmi. "
                  "Agar ha — qadam to'liq elastik, korreksiya kerak emas; "
                  "agar yo'q — plastik korrektor ishga tushadi.", "kod"),
                q("Springback (orqaga qaytish) hodisasi nimadan kelib chiqadi?",
                  "Shtamp olinganda plastik deformatsiya qoladi, lekin elastik "
                  "qism qaytadi. Qaytish miqdori $\\sigma_{\\max}/E$ ga teng — "
                  "shuning uchun yuqori mustahkamlikdagi po'latda (katta "
                  "$\\sigma_Y$) springback kattaroq.", "talqin"),
            ],
            bridge=(
                "Plastiklikda javob **yo'lga** bog'liq edi, lekin **vaqtga** "
                "bog'liq emas: tezroq yuklasak ham natija bir xil. Ko'plab "
                "materiallarda (polimer, beton, biologik to'qima) esa vaqt "
                "hal qiluvchi rol o'ynaydi. Keyingi mavzuda viskoelastiklikni "
                "o'rganamiz."
            ),
            research=(
                "Chaboche kombinatsiyalangan mustahkamlanish modelini "
                "o'rganing: bir nechta nochiziqli kinematik qismlar "
                "$\\dot{\\alpha}_i = C_i\\dot{\\varepsilon}^p - "
                "\\gamma_i\\alpha_i\\dot{\\bar{\\varepsilon}}^p$ qo'shiladi. "
                "Uni return mapping sxemasiga kiriting va past siklli charchash "
                "sinovining barqaror gisterezis halqasiga eng kichik kvadratlar "
                "usuli bilan moslashtiring. $C_i$, $\\gamma_i$ parametrlarining "
                "fizik ma'nosini tahlil qiling."
            ),
            manim_ref=manim(
                scene="HardeningScene",
                module="animatsiya/scenes/tmm_plasticity.py",
                title="Oqish yuzasining evolyutsiyasi",
                summary=(
                    "Izotrop mustahkamlanishda doira kengayadi, kinematikda "
                    "esa markazi siljiydi; ikkala holat $\\sigma$–$\\varepsilon$ "
                    "diagrammasi bilan sinxron ko'rsatiladi."
                ),
            ),
        ),
    ),

    # ------------------------------------------------------------------ tmm-23
    Topic(
        id="tmm-23",
        subject_id=S, module_id=M, order=23,
        title="Viskoelastiklik: Maksvell, Kelvin–Foygt modellari va relaksatsiya",
        description=(
            "Vaqtga bog'liq material javobi: krip va relaksatsiya, reologik "
            "modellar, Bolsman superpozitsiya integrali, kompleks modul va "
            "mexanik yo'qotishlar."
        ),
        learning_objective=(
            "Reologik modeldan differensial tenglama tuzish, krip va relaksatsiya "
            "funksiyalarini analitik topish hamda garmonik yuklanishdagi "
            "yo'qotish burchagini hisoblash."
        ),
        prerequisites=["tmm-13", "nm-26"],
        mathematical_core=(
            "Chiziqli ODE $\\sigma + p_1\\dot{\\sigma} = q_0\\varepsilon + "
            "q_1\\dot{\\varepsilon}$, Bolsman integrali, Laplas almashtirishi va "
            "moslik prinsipi, kompleks modul $E^* = E' + iE''$."
        ),
        engineering_application=(
            "Polimer va kompozitlar, asfalt qoplama, beton krip, tebranish "
            "so'ndirgichlari, biologik to'qima mexanikasi, prujinali tayanchlar."
        ),
        computational_component=(
            "Maksvell va Kelvin–Foygt modellarini sonli integrallash, Prony "
            "qatori bilan umumlashtirilgan model, $E'(\\omega)$ va "
            "$\\tan\\delta(\\omega)$ egri chiziqlari."
        ),
        visualization_component=(
            "Reologik sxemalar (prujina + demfer), krip va relaksatsiya "
            "egri chiziqlari, chastota javobida yo'qotish cho'qqisi."
        ),
        research_extension=(
            "Vaqt–harorat superpozitsiya prinsipini (WLF tenglamasi) o'rganing "
            "va turli haroratdagi o'lchovlardan yagona master-egri chiziq quring."
        ),
        difficulty="murakkab",
        previous_link=(
            "tmm-22 da material javobi yo'lga bog'liq, lekin vaqtga bog'liq "
            "emas edi. Endi vaqt o'zgaruvchisini konstitutiv tenglamaga "
            "kiritamiz — bu tmm-13 dagi determinizm prinsipining to'liq "
            "shakli (hozirgi kuchlanish butun deformatsiya tarixiga bog'liq)."
        ),
        next_topic="tmm-24",
        estimated_minutes=95,
        tags=["viskoelastiklik", "krip", "relaksatsiya", "reologiya"],
        lesson=_lesson(
            problem=(
                "Polimer quvur uzatmasi bo'lt bilan mahkamlangan. Montaj paytida "
                "bo'ltga 50 kN dastlabki tortish beriladi. Olti oydan keyin "
                "o'lchov 30 kN ni ko'rsatadi — zichlash buzilib, oqish boshlangan. "
                "Bo'lt uzunligi o'zgarmagan, demak deformatsiya doimiy edi; "
                "shunga qaramay kuchlanish kamaygan. Bu hodisa — **relaksatsiya**. "
                "Metallda bunday narsa xona haroratida deyarli sezilmaydi, "
                "polimerda esa hal qiluvchi. Nega? Va uni qanday bashorat qilamiz?"
            ),
            concepts=[
                c("Krip (creep, sudralish)",
                  "Doimiy kuchlanish ostida deformatsiyaning vaqt bo'yicha "
                  "o'sishi: $\\varepsilon(t) = \\sigma_0 J(t)$, $J(t)$ — "
                  "moslashuvchanlik (creep compliance) funksiyasi."),
                c("Relaksatsiya (stress relaxation)",
                  "Doimiy deformatsiya ostida kuchlanishning vaqt bo'yicha "
                  "pasayishi: $\\sigma(t) = \\varepsilon_0 E(t)$, $E(t)$ — "
                  "relaksatsiya moduli."),
                c("Maksvell modeli (Maxwell model)",
                  "Prujina va demfer **ketma-ket**: deformatsiya qo'shiladi, "
                  "kuchlanish umumiy. Relaksatsiyani yaxshi, kripni yomon "
                  "tavsiflaydi (chegaralanmagan oqish)."),
                c("Kelvin–Foygt modeli (Kelvin–Voigt model)",
                  "Prujina va demfer **parallel**: kuchlanish qo'shiladi, "
                  "deformatsiya umumiy. Kripni yaxshi, relaksatsiyani umuman "
                  "tavsiflamaydi (oniy javob yo'q)."),
                c("Relaksatsiya vaqti (relaxation time)",
                  "$\\tau = \\eta/E$ — materialning xarakterli vaqt masshtabi. "
                  "Kuzatish vaqti $t \\ll \\tau$ bo'lsa material elastik, "
                  "$t \\gg \\tau$ bo'lsa yopishqoq ko'rinadi."),
                c("Yo'qotish burchagi (loss tangent, $\\tan\\delta$)",
                  "Garmonik yuklanishda deformatsiyaning kuchlanishdan "
                  "kechikish burchagi; $\\tan\\delta = E''/E'$ bir siklda "
                  "tarqalgan energiya ulushini o'lchaydi."),
            ],
            derivation=[
                d("1. Reologik elementlar",
                  r"\text{Prujina: } \sigma = E\varepsilon; \qquad "
                  r"\text{Demfer: } \sigma = \eta\,\dot{\varepsilon}",
                  "Ikki asosiy g'isht. Prujina energiyani saqlaydi (elastik), "
                  "demfer tarqatadi (yopishqoq). $\\eta$ — dinamik "
                  "yopishqoqlik, birligi Pa·s."),
                d("2. Maksvell modeli: ketma-ket ulanish",
                  r"\varepsilon = \varepsilon_{\text{pr}} + \varepsilon_{\text{dem}} "
                  r"\;\Rightarrow\; \dot{\varepsilon} = \frac{\dot{\sigma}}{E} "
                  r"+ \frac{\sigma}{\eta}",
                  "Ketma-ket ulanishda deformatsiyalar qo'shiladi, kuchlanish "
                  "esa ikkala elementda bir xil — xuddi ketma-ket prujinalar kabi."),
                d("3. Maksvell relaksatsiyasi",
                  r"\dot{\varepsilon} = 0 \;\Rightarrow\; \frac{\dot{\sigma}}{E} "
                  r"+ \frac{\sigma}{\eta} = 0 \;\Rightarrow\; "
                  r"\sigma(t) = \sigma_0 e^{-t/\tau}, \quad \tau = \frac{\eta}{E}",
                  "Doimiy deformatsiya ($\\dot{\\varepsilon} = 0$) qo'yib, "
                  "ajraluvchi o'zgaruvchili ODE ni yechamiz. Kuchlanish "
                  "eksponensial nolga tushadi — bo'lt masalasidagi hodisa aynan shu."),
                d("4. Kelvin–Foygt modeli: parallel ulanish",
                  r"\sigma = \sigma_{\text{pr}} + \sigma_{\text{dem}} = "
                  r"E\varepsilon + \eta\,\dot{\varepsilon}",
                  "Parallel ulanishda kuchlanishlar qo'shiladi, deformatsiya "
                  "umumiy — ikkala element bir xil cho'ziladi."),
                d("5. Kelvin–Foygt kripi",
                  r"\sigma = \sigma_0 = \text{const} \;\Rightarrow\; "
                  r"\varepsilon(t) = \frac{\sigma_0}{E}\Big(1 - e^{-t/\tau}\Big)",
                  "Birinchi tartibli chiziqli ODE ning standart yechimi. "
                  "Deformatsiya $\\sigma_0/E$ ga asimptotik intiladi — "
                  "chegaralangan krip, bu beton va polimer uchun realistik."),
                d("6. Uch parametrli standart chiziqli qattiq jism",
                  r"\sigma + p_1\dot{\sigma} = q_0\varepsilon + q_1\dot{\varepsilon}, \qquad "
                  r"E(t) = E_\infty + (E_0 - E_\infty)e^{-t/\tau}",
                  "Maksvell elementiga parallel prujina qo'shamiz. Endi model "
                  "ham oniy elastik javobni ($E_0$), ham chegaralangan "
                  "relaksatsiyani ($E_\\infty > 0$) beradi — real materialga "
                  "ancha yaqin."),
                d("7. Bolsman superpozitsiya integrali",
                  r"\sigma(t) = \int_{-\infty}^{t} E(t - s)\,\frac{d\varepsilon(s)}{ds}\,ds",
                  "Chiziqlilikdan kelib chiqadi: har bir kichik deformatsiya "
                  "ortishi mustaqil hissa qo'shadi va ular qo'shiladi. Bu "
                  "chiziqli viskoelastiklikning eng umumiy shakli — "
                  "material 'xotirasi' shu yerda."),
                d("8. Kompleks modul va yo'qotishlar",
                  r"\varepsilon = \varepsilon_0 e^{i\omega t} \;\Rightarrow\; "
                  r"E^*(\omega) = E' + iE'', \qquad "
                  r"\tan\delta = \frac{E''}{E'} = \frac{\omega\tau}{1 + \omega^2\tau^2}"
                  r"\cdot\frac{E_0 - E_\infty}{\cdots}",
                  "Garmonik yuklanishda kompleks modul kiritiladi: $E'$ — "
                  "saqlash (storage) moduli, $E''$ — yo'qotish (loss) moduli. "
                  "$\\tan\\delta$ maksimumi $\\omega\\tau \\approx 1$ da — "
                  "demfer eng samarali ishlaydigan chastota."),
            ],
            meaning=(
                "$\\tau = \\eta/E$ — butun viskoelastiklikning kaliti. U "
                "materialning ichki soati: agar tajriba $\\tau$ dan tez "
                "o'tsa, demfer 'ulgurmaydi' va material qattiq elastik "
                "ko'rinadi; agar sekin o'tsa, demfer erkin oqadi va material "
                "yopishqoq suyuqlikdek tutadi. Shuning uchun bitta polimer "
                "zarbada mo'rt sinishi, lekin uzoq yuk ostida oqib ketishi "
                "mumkin — bu qarama-qarshilik emas, bir xil $\\tau$ ning "
                "ikki tomoni. Deborah soni $De = \\tau/t_{\\text{kuzatuv}}$ "
                "aynan shu nisbatni o'lchaydi. Bo'lt masalasida: "
                "po'lat uchun xona haroratida $\\tau$ yillar bilan o'lchanadi, "
                "polimer uchun esa oylar — shuning uchun olti oyda 40 % "
                "yo'qotish yuz berdi. Relaksatsiya moduli $E(t)$ esa "
                "materialning 'unutish egri chizig'i': $E_\\infty$ — hech "
                "qachon unutilmaydigan qism (kesishgan polimer tarmog'i), "
                "$E_0 - E_\\infty$ — vaqt bilan yo'qoladigan qism."
            ),
            equations=[
                eq(r"\dot{\varepsilon} = \frac{\dot{\sigma}}{E} + \frac{\sigma}{\eta}",
                   "Maksvell modeli konstitutiv tenglamasi.", "Maksvell modeli"),
                eq(r"\sigma = E\varepsilon + \eta\dot{\varepsilon}",
                   "Kelvin–Foygt modeli konstitutiv tenglamasi.",
                   "Kelvin–Foygt modeli"),
                eq(r"\sigma(t) = \int_{0}^{t} E(t-s)\,\dot{\varepsilon}(s)\,ds",
                   "Bolsman superpozitsiya integrali (chiziqli viskoelastiklik).",
                   "Bolsman integrali"),
                eq(r"E(t) = E_\infty + \sum_{k=1}^{N} E_k e^{-t/\tau_k}",
                   "Prony qatori — umumlashtirilgan Maksvell modeli; FEM "
                   "paketlarida standart kiritish shakli.", "Prony qatori"),
            ],
            conditions=(
                "**Boshlang'ich shart:** $\\varepsilon(0^-) = 0$, "
                "$\\sigma(0^-) = 0$ — yuklanishgacha jism tinch. Zinapoyasimon "
                "(step) yuklanishda $t = 0$ da sakrash bo'ladi, shuning uchun "
                "$0^-$ va $0^+$ ni ajratish muhim: Maksvell modelida "
                "$\\varepsilon(0^+) = \\sigma_0/E$ (oniy elastik javob), "
                "Kelvin–Foygtda esa $\\varepsilon(0^+) = 0$ (oniy javob yo'q).\n\n"
                "**Yuklanish tarixi:** Bolsman integrali butun "
                "$\\varepsilon(s),\\ s \\le t$ tarixini talab qiladi. Amaliyotda "
                "$t = 0$ dan boshlanadi deb olinadi (sinov boshi).\n\n"
                "**Chegaraviy shartlar** elastik masaladagidek qoladi, lekin "
                "moslik prinsipi (correspondence principle) bo'yicha ular "
                "Laplas fazosida qo'yiladi: elastik yechimda $E \\to s\\bar{E}(s)$ "
                "almashtirish viskoelastik yechimni beradi."
            ),
            worked=WorkedExample(
                statement=(
                    "Polimer bo'lt: $E_0 = 3$ GPa, $\\eta = 4{,}7 \\times 10^{16}$ Pa·s "
                    "(Maksvell modeli). Montajda $\\sigma_0 = 50$ MPa beriladi va "
                    "deformatsiya doimiy ushlanadi. (a) Relaksatsiya vaqtini toping. "
                    "(b) 6 oydan keyin kuchlanish qancha bo'ladi? (c) 30 MPa "
                    "gacha tushishiga qancha vaqt ketadi?"
                ),
                given=[
                    r"E_0 = 3\ \text{GPa} = 3\times10^9\ \text{Pa}",
                    r"\eta = 4{,}7\times10^{16}\ \text{Pa·s}",
                    r"\sigma_0 = 50\ \text{MPa}",
                    r"t = 6\ \text{oy} = 1{,}58\times10^7\ \text{s}",
                ],
                steps=[
                    st(r"\tau = \frac{\eta}{E_0} = \frac{4{,}7\times10^{16}}{3\times10^9} "
                       r"= 1{,}567\times10^{7}\ \text{s} \approx 181\ \text{kun}",
                       "Relaksatsiya vaqti — taxminan olti oy. Demak jarayon "
                       "aynan kuzatish masshtabida kechadi."),
                    st(r"\frac{t}{\tau} = \frac{1{,}58\times10^7}{1{,}567\times10^7} = 1{,}008",
                       "O'lchamsiz vaqt birga yaqin — bu $De \\approx 1$, ya'ni "
                       "eng 'qiziq' rejim."),
                    st(r"\sigma(t) = 50\,e^{-1{,}008} = 50 \cdot 0{,}365 = 18{,}3\ \text{MPa}",
                       "Sof Maksvell modeli 18,3 MPa beradi — o'lchangan 30 MPa "
                       "dan kichik. Model to'liq relaksatsiyani bashorat qiladi."),
                    st(r"E_\infty \ne 0: \quad \sigma(t) = \sigma_\infty + "
                       r"(\sigma_0 - \sigma_\infty)e^{-t/\tau}",
                       "Real materialda qoldiq bikrlik bor. 30 MPa ni "
                       "tushuntirish uchun standart chiziqli qattiq jismga o'tamiz."),
                    st(r"30 = \sigma_\infty + (50 - \sigma_\infty)e^{-1{,}008} "
                       r"\;\Rightarrow\; \sigma_\infty = \frac{30 - 18{,}3}{1 - 0{,}365} "
                       r"= 18{,}4\ \text{MPa}",
                       "Ma'lumotdan $\\sigma_\\infty$ ni tiklaymiz: uzoq muddatda "
                       "bo'ltda 18,4 MPa qoladi."),
                    st(r"t_{30} \text{ (sof Maksvell)}: \quad "
                       r"t = -\tau\ln\frac{30}{50} = 1{,}567\times10^7 \cdot 0{,}511 "
                       r"= 8{,}0\times10^{6}\ \text{s} \approx 93\ \text{kun}",
                       "Sof Maksvell modeli bo'yicha 30 MPa ga tushish uchun "
                       "atigi 3 oy kerak — model konservativ (xavfsiz) tomonga xato qiladi."),
                ],
                answer=(
                    "$\\tau = 1{,}57\\times10^7$ s $\\approx$ 181 kun; sof Maksvell "
                    "bo'yicha 6 oyda 18,3 MPa, o'lchangan 30 MPa esa "
                    "$\\sigma_\\infty \\approx 18{,}4$ MPa li standart chiziqli "
                    "qattiq jism modeliga mos keladi; 30 MPa ga tushish "
                    "$\\approx$ 93 kun."
                ),
                engineering_note=(
                    "Polimer bo'ltli birikmalarda relaksatsiyani qoplashning "
                    "ikki yo'li bor: (1) prujinali shayba qo'yish — u katta "
                    "elastik zaxira yaratadi, shuning uchun bir xil kuch "
                    "yo'qotish nisbatan kichikroq bo'ladi; (2) davriy qayta "
                    "tortish (re-torquing) jadvalini $\\tau$ asosida belgilash. "
                    "$\\tau$ haroratga juda kuchli bog'liq (Arrenius), shuning "
                    "uchun issiq muhitda jadval bir necha marta zichlashtiriladi."
                ),
            ),
            computation=Computation(
                caption=(
                    "Maksvell, Kelvin–Foygt va standart chiziqli qattiq jism "
                    "modellarini taqqoslash: krip, relaksatsiya va chastota javobi."
                ),
                code='''"""Viskoelastiklik: Maksvell, Kelvin-Foygt va standart chiziqli qattiq jism."""
import numpy as np
from labkit import PARAMS, note, series, table, value

E0 = float(PARAMS.get("E0", 3000.0))       # MPa - oniy modul
Einf = float(PARAMS.get("Einf", 900.0))    # MPa - uzoq muddatli modul
tau = float(PARAMS.get("tau", 100.0))      # s - relaksatsiya vaqti
sig0 = float(PARAMS.get("sig0", 50.0))     # MPa - qo'yilgan kuchlanish
t_end = float(PARAMS.get("t_end", 500.0))  # s

eta = (E0 - Einf)*tau                      # MPa*s
value("Relaksatsiya vaqti tau", tau, "s")
value("Yopishqoqlik eta", eta, "MPa*s")
value("E0/Einf", E0/Einf if Einf > 0 else float("inf"), "—")

t = np.linspace(0.0, t_end, 600)

# --- Relaksatsiya: eps = const ---
E_max = E0*np.exp(-t/tau)                      # sof Maksvell
E_sls = Einf + (E0 - Einf)*np.exp(-t/tau)      # standart chiziqli qattiq jism
series("E(t) Maksvell", t.tolist(), E_max.tolist(),
       xlabel="Vaqt t, s", ylabel="Relaksatsiya moduli E(t), MPa")
series("E(t) Standart chiziqli qattiq jism", t.tolist(), E_sls.tolist(),
       xlabel="Vaqt t, s", ylabel="Relaksatsiya moduli E(t), MPa")

value("E(tau)/E(0) Maksvell", float(np.exp(-1.0)), "—")
value("E(t_end) Maksvell", float(E_max[-1]), "MPa")
value("E(t_end) SLS", float(E_sls[-1]), "MPa")

# --- Krip: sigma = const ---
eps_kv = sig0/E0*(1 - np.exp(-t/tau))          # Kelvin-Foygt
eps_mx = sig0/E0 + sig0/eta*t if eta > 0 else np.full_like(t, np.nan)  # Maksvell
series("eps(t) Kelvin-Foygt", t.tolist(), (100*eps_kv).tolist(),
       xlabel="Vaqt t, s", ylabel="Deformatsiya, %")
series("eps(t) Maksvell", t.tolist(), (100*eps_mx).tolist(),
       xlabel="Vaqt t, s", ylabel="Deformatsiya, %")
note("Kelvin-Foygt kripi chegaralangan (sigma0/E0 ga intiladi), "
     "Maksvell kripi esa cheksiz o'sadi — shuning uchun qattiq jism "
     "uchun Maksvell yolg'iz yaramaydi.")

# --- Garmonik yuklanish: kompleks modul ---
w = np.logspace(-3, 3, 400)/tau
wt = w*tau
Ep = Einf + (E0 - Einf)*wt**2/(1 + wt**2)      # saqlash moduli
Epp = (E0 - Einf)*wt/(1 + wt**2)               # yo'qotish moduli
tand = Epp/Ep

series("E'(w) saqlash moduli", w.tolist(), Ep.tolist(),
       xlabel="Chastota w, rad/s", ylabel="E', MPa")
series("E''(w) yo'qotish moduli", w.tolist(), Epp.tolist(),
       xlabel="Chastota w, rad/s", ylabel="E'', MPa")
series("tan(delta)", w.tolist(), tand.tolist(),
       xlabel="Chastota w, rad/s", ylabel="tan(delta)")

i_max = int(np.argmax(tand))
value("tan(delta) maksimumi", float(tand[i_max]), "—")
value("Maksimum chastotasi", float(w[i_max]), "rad/s")
value("w*tau maksimumda", float(w[i_max]*tau), "—")
note(f"Yo'qotish maksimumi w*tau = {w[i_max]*tau:.3f} da — nazariy "
     f"qiymat sqrt(E0/Einf) = {np.sqrt(E0/Einf):.3f}.")

# --- Bolsman integrali bilan tekshirish: chiziqli o'suvchi deformatsiya ---
rate = 1e-4          # 1/s
dt = t[1] - t[0]
deps = np.full_like(t, rate*dt)
deps[0] = 0.0
sig_num = np.array([np.sum((Einf + (E0-Einf)*np.exp(-(t[i]-t[:i+1])/tau))*deps[:i+1])
                    for i in range(len(t))])
series("sigma(t), doimiy tezlikda cho'zish", t.tolist(), sig_num.tolist(),
       xlabel="Vaqt t, s", ylabel="Kuchlanish sigma, MPa")
sig_elastic = E0*rate*t
note(f"t = {t_end:.0f} s da viskoelastik sigma = {sig_num[-1]:.2f} MPa, "
     f"sof elastik bo'lsa {sig_elastic[-1]:.2f} MPa bo'lar edi — "
     f"farq relaksatsiya hisobiga.")

table("Deborah soni va material xatti-harakati",
      ["De = tau/t_kuzatuv", "Rejim", "Misol"],
      [[">> 1", "Elastik qattiq jism", "Zarba, ultratovush"],
       ["~ 1", "Viskoelastik (maksimal yo'qotish)", "Tebranish so'ndirgich"],
       ["<< 1", "Yopishqoq suyuqlik", "Uzoq muddatli krip, asfalt oqishi"]])
''',
                parameters=[
                    p("E0", "Oniy modul E₀", 100.0, 10000.0, 3000.0, 50.0, "MPa"),
                    p("Einf", "Uzoq muddatli modul E∞", 10.0, 5000.0, 900.0, 10.0, "MPa"),
                    p("tau", "Relaksatsiya vaqti τ", 1.0, 1000.0, 100.0, 1.0, "s"),
                    p("sig0", "Qo'yilgan kuchlanish σ₀", 1.0, 200.0, 50.0, 1.0, "MPa"),
                    p("t_end", "Kuzatish vaqti", 50.0, 3000.0, 500.0, 10.0, "s"),
                ],
                expected_output=(
                    "E(τ)/E(0) = 0,368; SLS moduli 900 MPa ga intiladi; "
                    "tan δ maksimumi ωτ ≈ √(E₀/E∞) = 1,83 da, qiymati ≈ 0,58. "
                    "Kelvin–Foygt kripi 0,0167 ga to'yinadi, Maksvell kripi chiziqli o'sadi."
                ),
            ),
            visual=vis(
                kind="Reologik model va vaqt javobi",
                tool="React/SVG",
                description=(
                    "Prujina–demfer sxemalari, krip/relaksatsiya egri chiziqlari "
                    "va chastota javobidagi yo'qotish cho'qqisi."
                ),
                how_to_draw=(
                    "React/SVG: prujina zigzag `<polyline>` (6–8 tishli), demfer "
                    "esa to'rtburchak silindr + ichidagi porshen chizig'i sifatida "
                    "chiziladi. Maksvell — ikkisi bitta gorizontal chiziqda ketma-ket; "
                    "Kelvin–Foygt — ikkisi ikki parallel shoxda, chetlarida "
                    "birlashtiruvchi vertikal chiziq. Elementlar `<g>` ichida "
                    "guruhlanadi va animatsiyada cho'ziladi: prujina tishlari "
                    "orasi ochiladi, demfer porsheni siljiydi. Vaqt javobi "
                    "grafiklari uchun logarifmik $x$ o'qi kerak "
                    "($\\tau$ bir necha tartibga yoyilgan), shuning uchun "
                    "`scaleLog` ni qo'lda amalga oshiramiz: "
                    "`x => (Math.log10(v) - lo)/(hi - lo)*W`. "
                    "$\\tan\\delta$ cho'qqisiga vertikal punktir va "
                    "'$\\omega\\tau = 1$ atrofi' yorlig'i qo'yiladi."
                ),
            ),
            interp=(
                "Chastota javobi grafigi eng ko'p amaliy ma'lumot beradi. "
                "Past chastotada $E' \\to E_\\infty$ (material yumshoq, demfer "
                "erkin oqadi), yuqori chastotada $E' \\to E_0$ (material qattiq, "
                "demfer qotib qoladi), oralig'ida esa $E''$ va $\\tan\\delta$ "
                "cho'qqi beradi. Tebranish so'ndirgichini loyihalashda maqsad — "
                "shu cho'qqini konstruksiyaning ishchi chastotasiga tushirish. "
                "Aksincha, avtomobil shinasida qarama-qarshi talab bor: "
                "g'ildirakning aylanish chastotasida $\\tan\\delta$ kichik "
                "bo'lishi kerak (yonilg'i sarfi kamayadi), lekin tormozlashdagi "
                "yuqori chastotada katta bo'lishi kerak (ilashish oshadi). "
                "Bu 'magic triangle' muammosi zamonaviy rezina "
                "kompozitsiyalarini loyihalashning markaziy vazifasi. "
                "Kod Bolsman integralini to'g'ridan-to'g'ri diskret yig'indi "
                "bilan hisoblaydi — bu $O(N^2)$ operatsiya; amaliy FEM "
                "kodlarida Prony qatorining rekursiv yangilanishi ishlatiladi "
                "va murakkablik $O(N)$ ga tushadi."
            ),
            mistakes=[
                "Kelvin–Foygt modelida oniy elastik javob bor deb o'ylash. "
                "$t = 0^+$ da $\\varepsilon = 0$: demfer cheksiz katta "
                "kuchlanishni talab qiladi, shuning uchun zinapoyasimon yukda "
                "deformatsiya sekin o'sa boshlaydi.",
                "Maksvell modelini qattiq jism uchun ishlatish. Uning kripi "
                "chegarasiz o'sadi — bu suyuqliksimon xulq-atvor; qattiq jism "
                "uchun kamida standart chiziqli qattiq jism kerak.",
                "$\\tau$ ni material doimiysi deb hisoblash va haroratga "
                "bog'liqlikni unutish. $\\tau$ Arrenius yoki WLF qonuni bo'yicha "
                "haroratga eksponensial bog'liq; 10 °C o'zgarish $\\tau$ ni "
                "bir necha marta o'zgartiradi.",
                "Relaksatsiya moduli $E(t)$ va krip moslashuvchanligi $J(t)$ ni "
                "o'zaro teskari deb olish. Umumiy holda "
                "$E(t) \\ne 1/J(t)$; ular faqat Laplas fazosida "
                "$\\bar{E}(s)\\bar{J}(s) = 1/s^2$ munosabati bilan bog'langan.",
            ],
            quiz=[
                q("Doimiy deformatsiyada kuchlanish pasayishi qanday ataladi?",
                  "Relaksatsiya (stress relaxation). Doimiy kuchlanishda "
                  "deformatsiyaning o'sishi esa krip deb ataladi.", "konseptual"),
                q("Maksvell va Kelvin–Foygt modellarining asosiy farqi nimada?",
                  "Maksvellda elementlar ketma-ket (deformatsiyalar qo'shiladi) — "
                  "relaksatsiyani beradi, kripi chegarasiz. Kelvin–Foygtda "
                  "parallel (kuchlanishlar qo'shiladi) — chegaralangan kripni "
                  "beradi, relaksatsiyasi yo'q.", "konseptual"),
                q("$E_0 = 3$ GPa, $\\eta = 3\\times10^{11}$ Pa·s. $\\tau$ ni toping.",
                  "$\\tau = \\eta/E_0 = 3\\times10^{11}/3\\times10^9 = 100$ s.",
                  "hisob"),
                q("Deborah soni $De \\gg 1$ nimani anglatadi?",
                  "Material relaksatsiya vaqti kuzatish vaqtidan ancha katta — "
                  "demfer 'ulgurmaydi', material elastik qattiq jism kabi "
                  "tutadi (masalan, zarba yuklanishida).", "talqin"),
                q("$\\tan\\delta$ maksimumi qaysi chastotada bo'ladi va nega "
                  "bu muhim?",
                  "$\\omega\\tau \\approx 1$ atrofida. Bu chastotada bir siklda "
                  "eng ko'p energiya issiqlikka aylanadi, shuning uchun "
                  "so'ndirgich shu chastotaga sozlanadi.", "talqin"),
                q("Kodda Bolsman integrali qanday hisoblangan va uning "
                  "kamchiligi nima?",
                  "Har bir $t_i$ uchun butun tarix bo'yicha yig'indi olinadi — "
                  "$O(N^2)$ murakkablik. Prony qatorining rekursiv "
                  "yangilanishi bir xil natijani $O(N)$ da beradi.", "kod"),
            ],
            bridge=(
                "Endi materialning chiziqli, plastik va vaqtga bog'liq "
                "javoblari ko'rib chiqildi. Lekin konstruksiya ko'pincha "
                "material oqish chegarasiga yetmasdan ham buziladi — kichik "
                "yoriq tufayli. Keyingi mavzuda yoriqlar mexanikasi asoslarini "
                "o'rganamiz."
            ),
            research=(
                "Vaqt–harorat superpozitsiya prinsipini (time–temperature "
                "superposition) o'rganing. WLF tenglamasi "
                "$\\log a_T = -C_1(T - T_0)/(C_2 + T - T_0)$ yordamida turli "
                "haroratlarda o'lchangan $E'(\\omega)$ egri chiziqlarini "
                "gorizontal siljitib yagona master-egri chiziqqa birlashtiring. "
                "Bu usul 40 yillik xizmat muddatini bir necha kunlik "
                "yuqori haroratli sinovdan bashorat qilish imkonini qanday "
                "beradi? Sonli moslashtirish skriptini yozing."
            ),
        ),
    ),

    # ------------------------------------------------------------------ tmm-24
    Topic(
        id="tmm-24",
        subject_id=S, module_id=M, order=24,
        title="Yoriqlar mexanikasi asoslari: kuchlanish intensivligi va energetik mezon",
        description=(
            "Yoriq uchidagi singulyar kuchlanish maydoni, kuchlanish "
            "intensivligi koeffitsienti $K$, Griffit energetik mezoni, "
            "$G$–$K$ bog'lanishi va plastik zona o'lchami."
        ),
        learning_objective=(
            "Yoriqli konstruksiyaning kritik yuklanishini $K_{Ic}$ orqali "
            "hisoblash, energetik va kuchlanish yondashuvlarining "
            "ekvivalentligini ko'rsatish va chiziqli mexanikaning qo'llanish "
            "chegarasini baholash."
        ),
        prerequisites=["tmm-17", "mq-29"],
        mathematical_core=(
            "Vestergaard funksiyasi va $r^{-1/2}$ singulyarlik, asimptotik "
            "yoyilma, energiya ozod bo'lish tezligi "
            "$G = -\\partial\\Pi/\\partial a$, Irvin munosabati $G = K^2/E'$."
        ),
        engineering_application=(
            "Damage tolerance loyihalash (aviatsiya), bosim idishlari va "
            "quvurlarning xavfsizligi, yoriq o'sishini bashorat qilish "
            "(Paris qonuni), NDT natijalarini qabul qilish mezonlari."
        ),
        computational_component=(
            "$K_I$ ni geometrik koeffitsient bilan hisoblash, kritik yoriq "
            "uzunligini topish, plastik zona radiusini baholash va "
            "$K$ maydonining sonli tekshiruvi."
        ),
        visualization_component=(
            "Yoriq uchidagi kuchlanish taqsimoti $\\sigma_y(r)$, plastik zona "
            "konturi, $\\sigma_c$–$a$ loyihalash diagrammasi."
        ),
        research_extension=(
            "Elastoplastik yoriqlar mexanikasiga o'ting: $J$-integral va CTOD "
            "mezonlarini o'rganing; $J$ ning yo'ldan mustaqilligini sonli "
            "tekshiring."
        ),
        difficulty="ilg'or",
        previous_link=(
            "tmm-17 da Kirsh yechimi teshik atrofida $K_t = 3$ kuchlanish "
            "konsentratsiyasini bergan edi. Teshikni ellipsga aylantirib "
            "yassilashtirsak, $K_t \\to \\infty$ bo'ladi — klassik "
            "konsentratsiya nazariyasi buziladi. Aynan shu yerdan yoriqlar "
            "mexanikasi boshlanadi."
        ),
        next_topic="tmm-25",
        estimated_minutes=100,
        tags=["yoriq", "Griffit", "K_Ic", "buzilish"],
        lesson=_lesson(
            problem=(
                "1954-yilda ikkita de Havilland Comet reaktiv layneri havoda "
                "parchalanib ketdi. Tekshiruv ko'rsatdiki, korpus kuchlanishi "
                "materialning oqish chegarasidan ancha past bo'lgan — klassik "
                "mustahkamlik hisobi bo'yicha hammasi joyida edi. Sabab: "
                "derazacha burchagidan boshlangan mikroyoriq har bir parvozdagi "
                "bosim sikli bilan o'sib borgan va kritik uzunlikka yetganda "
                "bir zumda tarqalgan. Savol: yoriqli konstruksiya qachon "
                "buziladi? Oqish chegarasi bunga javob bermaydi — yangi "
                "material xossasi va yangi mezon kerak."
            ),
            concepts=[
                c("Kuchlanish intensivligi koeffitsienti (stress intensity factor)",
                  "$K_I = Y\\sigma\\sqrt{\\pi a}$ — yoriq uchidagi singulyar "
                  "maydonning amplitudasi. Birligi MPa·√m. Butun geometriya va "
                  "yuk ta'siri shu bitta songa yig'iladi."),
                c("Buzilish qovushqoqligi (fracture toughness, $K_{Ic}$)",
                  "Materialning yoriq tarqalishiga qarshiligini o'lchaydigan "
                  "doimiysi. Buzilish sharti: $K_I \\ge K_{Ic}$."),
                c("Griffit energetik mezoni (Griffith criterion)",
                  "Yoriq o'sishi uchun ozod bo'ladigan elastik energiya yangi "
                  "sirt yaratishga ketadigan energiyadan katta bo'lishi kerak."),
                c("Energiya ozod bo'lish tezligi (energy release rate, $G$)",
                  "$G = -\\partial\\Pi/\\partial a$ — yoriq birlik uzunlikka "
                  "o'sganda ozod bo'ladigan potensial energiya. Birligi J/m²."),
                c("Irvin munosabati (Irwin relation)",
                  "$G = K_I^2/E'$, bu yerda $E' = E$ (tekis kuchlanish) yoki "
                  "$E/(1-\\nu^2)$ (tekis deformatsiya). Ikki mustaqil "
                  "yondashuvning ekvivalentligini isbotlaydi."),
                c("Plastik zona (plastic zone)",
                  "Yoriq uchida cheksiz kuchlanish bo'lolmaydi — material "
                  "oqadi. Irvin bahosi: $r_p = \\frac{1}{2\\pi}(K_I/\\sigma_Y)^2$ "
                  "(tekis kuchlanish)."),
            ],
            derivation=[
                d("1. Ellips teshigidan yoriqqa o'tish",
                  r"\sigma_{\max} = \sigma\Big(1 + \frac{2a}{b}\Big) "
                  r"= \sigma\Big(1 + 2\sqrt{\frac{a}{\rho}}\Big) "
                  r"\;\xrightarrow{\rho \to 0}\; \infty",
                  "tmm-17 dagi Inglis yechimi. Yoriq — uchi o'tkir ($\\rho \\to 0$) "
                  "ellips. Kuchlanish cheksizlikka intiladi, demak "
                  "$\\sigma_{\\max}$ mezon sifatida yaroqsiz — boshqa kattalik kerak."),
                d("2. Yoriq uchidagi asimptotik maydon",
                  r"\sigma_{ij}(r, \theta) = \frac{K_I}{\sqrt{2\pi r}}\,f_{ij}(\theta) "
                  r"+ O(r^0)",
                  "Vestergaard/Vilyams yechimi. Muhim jihat: **burchakka "
                  "bog'liqlik $f_{ij}(\\theta)$ universal** — har qanday "
                  "geometriyada bir xil. Faqat amplituda $K_I$ farq qiladi. "
                  "Demak yoriq uchidagi butun holatni bitta son tavsiflaydi."),
                d("3. $\\theta = 0$ da kuchlanish va $K_I$ ta'rifi",
                  r"\sigma_y(r, 0) = \frac{K_I}{\sqrt{2\pi r}} \;\Longrightarrow\; "
                  r"K_I = \lim_{r\to 0}\sqrt{2\pi r}\;\sigma_y(r, 0)",
                  "$K_I$ — singulyarlikning 'kuchi'. Cheksiz plastinadagi "
                  "markaziy yoriq uchun aniq yechim $K_I = \\sigma\\sqrt{\\pi a}$."),
                d("4. Griffitning energetik balansi",
                  r"\frac{d}{da}\Big(\Pi + W_s\Big) \le 0, \qquad "
                  r"W_s = 2\gamma_s\,(2a)\cdot B",
                  "Yoriq o'sishi termodinamik jihatdan foydali bo'lsagina "
                  "sodir bo'ladi. $\\Pi$ — elastik potensial energiya "
                  "(kamayadi), $W_s$ — sirt energiyasi (ortadi), $\\gamma_s$ — "
                  "solishtirma sirt energiyasi, koeffitsient 2 — yoriqning "
                  "ikki yuzasi."),
                d("5. Ozod bo'lgan energiya (cheksiz plastina)",
                  r"\Pi(a) = \Pi_0 - \frac{\pi\sigma^2 a^2 B}{E} \;\Longrightarrow\; "
                  r"G = -\frac{1}{B}\frac{\partial\Pi}{\partial (2a)}\cdot 2 "
                  r"= \frac{\pi\sigma^2 a}{E}",
                  "Elastik energiyaning yoriq tufayli kamayishi Inglis "
                  "yechimidan olinadi. $G$ — yoriq uzunligining birlik "
                  "ortishiga to'g'ri keladigan energiya."),
                d("6. Griffit kritik kuchlanishi",
                  r"G = G_c = 2\gamma_s \;\Longrightarrow\; "
                  r"\sigma_c = \sqrt{\frac{2E\gamma_s}{\pi a}}",
                  "Kritik kuchlanish yoriq uzunligining kvadrat ildiziga "
                  "teskari mutanosib. Bu — mo'rt materiallar uchun Griffitning "
                  "1921-yildagi mashhur natijasi."),
                d("7. Irvin umumlashtirishi va $G$–$K$ bog'lanishi",
                  r"G = \frac{K_I^2}{E'}, \qquad "
                  r"E' = \begin{cases} E, & \text{tekis kuchlanish}\\ "
                  r"E/(1-\nu^2), & \text{tekis deformatsiya}\end{cases}",
                  "Tekshiramiz: $K_I = \\sigma\\sqrt{\\pi a}$ ni qo'ysak, "
                  "$G = \\sigma^2\\pi a/E$ — 5-qadamdagi natija bilan aynan "
                  "bir xil. Metallarda $G_c = 2\\gamma_s + \\gamma_p$, bunda "
                  "plastik ish $\\gamma_p$ sirt energiyasidan 1000 marta katta."),
                d("8. Plastik zona va qo'llanish chegarasi",
                  r"r_p = \frac{1}{2\pi}\Big(\frac{K_I}{\sigma_Y}\Big)^2, \qquad "
                  r"a,\ (W-a),\ B \ge 2{,}5\Big(\frac{K_{Ic}}{\sigma_Y}\Big)^2",
                  "$\\sigma_y(r_p) = \\sigma_Y$ shartidan. Chiziqli mexanika "
                  "faqat $r_p \\ll a$ bo'lganda (small scale yielding) o'rinli; "
                  "ASTM E399 standartidagi $2{,}5(K_{Ic}/\\sigma_Y)^2$ sharti "
                  "aynan shundan kelib chiqadi."),
            ],
            meaning=(
                "$K_I = Y\\sigma\\sqrt{\\pi a}$ formulasi uchta mustaqil "
                "omilni birlashtiradi: **yuk** ($\\sigma$), **nuqson o'lchami** "
                "($a$) va **geometriya** ($Y$). Uning eng chuqur ma'nosi shuki, "
                "yoriq uchi bu uchtasini alohida 'ko'rmaydi' — u faqat "
                "ularning kombinatsiyasini sezadi. Shuning uchun laboratoriyada "
                "kichik namunada o'lchangan $K_{Ic}$ real, ulkan konstruksiyaga "
                "ko'chiriladi — bu butun buzilish mexanikasining amaliy "
                "asosi. $\\sqrt{a}$ bog'liqligi ham muhim: yoriqni ikki marta "
                "uzaytirish $K_I$ ni atigi $\\sqrt{2} = 1{,}41$ marta oshiradi, "
                "shuning uchun yoriq avval sekin, oxirida esa tez o'sadi. "
                "$G = K^2/E'$ munosabati esa ikki mutlaqo turli fikrlash "
                "yo'lining — energetik (Griffit, termodinamikadan) va "
                "kuchlanish (Irvin, elastiklik nazariyasidan) — bir xil "
                "javobga olib kelishini ko'rsatadi. Fizikada bunday "
                "yo'lakchalar birikishi nazariya to'g'riligining eng ishonchli "
                "belgisi hisoblanadi."
            ),
            equations=[
                eq(r"K_I = Y\sigma\sqrt{\pi a}",
                   "Kuchlanish intensivligi koeffitsienti; $Y$ — geometrik "
                   "koeffitsient.", "K_I ta'rifi"),
                eq(r"\sigma_{ij} = \frac{K_I}{\sqrt{2\pi r}}f_{ij}(\theta)",
                   "Yoriq uchidagi asimptotik kuchlanish maydoni.",
                   "Singulyar maydon"),
                eq(r"G = -\frac{\partial \Pi}{\partial A} = \frac{K_I^2}{E'}",
                   "Energiya ozod bo'lish tezligi va Irvin munosabati.",
                   "Irvin munosabati"),
                eq(r"\frac{da}{dN} = C(\Delta K)^m",
                   "Paris qonuni — siklik yuklanishda yoriq o'sish tezligi.",
                   "Paris qonuni"),
            ],
            conditions=(
                "**Yoriq yuzalarida:** $\\sigma_{yy} = \\sigma_{xy} = 0$ — "
                "erkin sirt, yuklanmagan. Aynan shu shart singulyarlikni "
                "keltirib chiqaradi.\n\n"
                "**Cheksizlikda (yoki chegarada):** $\\sigma_{yy} \\to \\sigma$ — "
                "qo'yilgan bir tekis yuk. Chegaralangan jismda bu shart "
                "geometrik koeffitsient $Y$ ga aylanadi.\n\n"
                "**Qo'llanish shartlari (small scale yielding):**\n"
                "- $r_p \\ll a$ — plastik zona yoriq uzunligidan ancha kichik;\n"
                "- $B \\ge 2{,}5(K_{Ic}/\\sigma_Y)^2$ — qalinlik tekis "
                "deformatsiya holatini ta'minlaydi (aks holda $K_c$ qalinlikka "
                "bog'liq bo'lib qoladi);\n"
                "- Bu shartlar buzilsa, elastoplastik mezonlar ($J$-integral, "
                "CTOD) kerak bo'ladi."
            ),
            worked=WorkedExample(
                statement=(
                    "Aviatsiya alyuminiy qotishmasi 7075-T6: $\\sigma_Y = 500$ MPa, "
                    "$K_{Ic} = 24$ MPa·√m, $E = 71$ GPa. Keng panelda markaziy "
                    "yoriq ($Y = 1$), ishchi kuchlanish $\\sigma = 150$ MPa. "
                    "(a) Kritik yoriq uzunligini toping. (b) 4 mm yarim "
                    "uzunlikdagi yoriq uchun zaxirani hisoblang. (c) Plastik "
                    "zona radiusini baholang va LEFM o'rinliligini tekshiring. "
                    "(d) $G_c$ ni toping."
                ),
                given=[
                    r"\sigma_Y = 500\ \text{MPa},\ K_{Ic} = 24\ \text{MPa}\sqrt{\text{m}}",
                    r"E = 71\ \text{GPa},\ \nu = 0{,}33",
                    r"\sigma = 150\ \text{MPa},\ Y = 1",
                    r"a = 4\ \text{mm}",
                ],
                steps=[
                    st(r"a_c = \frac{1}{\pi}\Big(\frac{K_{Ic}}{Y\sigma}\Big)^2 "
                       r"= \frac{1}{\pi}\Big(\frac{24}{150}\Big)^2 = \frac{0{,}0256}{\pi} "
                       r"= 8{,}15\ \text{mm}",
                       "Kritik **yarim** uzunlik. To'liq yoriq $2a_c = 16{,}3$ mm — "
                       "ko'z bilan ko'rish mumkin bo'lgan, lekin juda kichik nuqson."),
                    st(r"K_I = 1 \cdot 150\sqrt{\pi \cdot 0{,}004} = 150 \cdot 0{,}1121 "
                       r"= 16{,}8\ \text{MPa}\sqrt{\text{m}}",
                       "Joriy holatdagi kuchlanish intensivligi koeffitsienti."),
                    st(r"n = \frac{K_{Ic}}{K_I} = \frac{24}{16{,}8} = 1{,}43",
                       "Zaxira koeffitsienti. Diqqat: $K \\propto \\sqrt{a}$ "
                       "bo'lgani uchun uzunlik bo'yicha zaxira $n^2 = 2{,}04$ — "
                       "yoriq ikki baravar uzaysa, buziladi."),
                    st(r"r_p = \frac{1}{2\pi}\Big(\frac{16{,}8}{500}\Big)^2 "
                       r"= \frac{0{,}001129}{6{,}283} = 0{,}18\ \text{mm}",
                       "Tekis kuchlanish holati uchun Irvin bahosi. "
                       "$r_p/a = 0{,}18/4 = 0{,}045$ — plastik zona yoriq "
                       "uzunligining 4,5 % i."),
                    st(r"r_p \ll a \;\checkmark; \qquad "
                       r"2{,}5\Big(\frac{24}{500}\Big)^2 = 2{,}5 \cdot 0{,}002304 "
                       r"= 5{,}8\ \text{mm}",
                       "LEFM o'rinli. ASTM sharti: qalinlik va yoriq uzunligi "
                       "5,8 mm dan katta bo'lishi kerak — $a = 4$ mm bu shartni "
                       "chegaradan biroz past bajaradi, ehtiyot bo'lish kerak."),
                    st(r"E' = \frac{E}{1-\nu^2} = \frac{71}{1 - 0{,}1089} "
                       r"= 79{,}7\ \text{GPa}; \quad "
                       r"G_c = \frac{K_{Ic}^2}{E'} = \frac{24^2}{79{,}7\times10^3} "
                       r"= 7{,}23\times10^{-3}\ \text{MPa·m} = 7{,}2\ \text{kJ/m}^2",
                       "Tekis deformatsiya uchun. Solishtirish uchun: sof "
                       "sirt energiyasi $2\\gamma_s \\approx 2$ J/m² — ya'ni "
                       "plastik ish 3600 marta ko'p energiya yutadi."),
                ],
                answer=(
                    "$a_c = 8{,}15$ mm (to'liq yoriq 16,3 mm); $K_I = 16{,}8$ "
                    "MPa·√m, zaxira $n = 1{,}43$; $r_p = 0{,}18$ mm $\\ll a$ — "
                    "LEFM o'rinli; $G_c = 7{,}2$ kJ/m²."
                ),
                engineering_note=(
                    "Aviatsiyadagi 'damage tolerance' falsafasi aynan shu "
                    "hisobga asoslangan: konstruksiya nuqsonsiz deb emas, "
                    "balki **NDT aniqlay oladigan eng kichik nuqson mavjud** "
                    "deb loyihalanadi. Keyin Paris qonuni bilan shu nuqsonning "
                    "$a_c$ gacha o'sish vaqti hisoblanadi va tekshirish "
                    "intervali shu vaqtning yarmidan kichik qilib belgilanadi — "
                    "shunda yoriq kamida ikki marta tekshiruvdan o'tadi."
                ),
            ),
            computation=Computation(
                caption=(
                    "$K_I$, kritik yoriq uzunligi, plastik zona va LEFM "
                    "qo'llanish shartlarini hisoblash; loyihalash diagrammasini qurish."
                ),
                code='''"""Yoriqlar mexanikasi: K_I, kritik yoriq va plastik zona."""
import numpy as np
from labkit import PARAMS, note, series, table, value

sig = float(PARAMS.get("sig", 150.0))      # MPa
a = float(PARAMS.get("a", 4.0))/1000.0     # m
KIc = float(PARAMS.get("KIc", 24.0))       # MPa*sqrt(m)
sY = float(PARAMS.get("sY", 500.0))        # MPa
E = float(PARAMS.get("E", 71.0))*1e3       # MPa
nu = float(PARAMS.get("nu", 0.33))
Y = float(PARAMS.get("Y", 1.0))            # geometrik koeffitsient

KI = Y*sig*np.sqrt(np.pi*a)
value("K_I", KI, "MPa*sqrt(m)")
value("K_Ic", KIc, "MPa*sqrt(m)")
value("Zaxira n = K_Ic/K_I", KIc/KI, "—")

a_c = (KIc/(Y*sig))**2/np.pi
value("Kritik yarim uzunlik a_c", a_c*1000, "mm")
value("Kritik to'liq uzunlik 2a_c", 2*a_c*1000, "mm")
value("a/a_c", a/a_c, "—")

sig_c = KIc/(Y*np.sqrt(np.pi*a))
value("Joriy yoriq uchun kritik kuchlanish", sig_c, "MPa")
value("Oqish chegarasiga nisbatan", sig_c/sY, "—")
if sig_c < sY:
    note(f"Kritik kuchlanish {sig_c:.1f} MPa < oqish chegarasi {sY:.1f} MPa: "
         f"buzilish MO'RT bo'ladi — plastik ogohlantirishsiz.")
else:
    note(f"Kritik kuchlanish {sig_c:.1f} MPa > oqish chegarasi {sY:.1f} MPa: "
         f"avval umumiy oqish boshlanadi, LEFM yaroqsiz.")

# Plastik zona (Irvin)
rp_ps = (KI/sY)**2/(2*np.pi)          # tekis kuchlanish
rp_pd = (KI/sY)**2/(6*np.pi)          # tekis deformatsiya
value("Plastik zona r_p (tekis kuchlanish)", rp_ps*1000, "mm")
value("Plastik zona r_p (tekis deformatsiya)", rp_pd*1000, "mm")
value("r_p/a", rp_ps/a, "—")

astm = 2.5*(KIc/sY)**2
value("ASTM E399 minimal o'lcham", astm*1000, "mm")
note(f"LEFM sharti: a, B >= {astm*1000:.2f} mm. Joriy a = {a*1000:.2f} mm — "
     f"{'BAJARILADI' if a >= astm else 'bajarilmaydi, elastoplastik mezon kerak'}.")

# Irvin munosabati
Ep_ps = E
Ep_pd = E/(1 - nu**2)
value("G (tekis kuchlanish)", KI**2/Ep_ps*1000, "kJ/m2")
value("G (tekis deformatsiya)", KI**2/Ep_pd*1000, "kJ/m2")
value("G_c (tekis deformatsiya)", KIc**2/Ep_pd*1000, "kJ/m2")

# --- sigma_y(r) yoriq uchi oldida ---
r = np.linspace(1e-6, 5*a, 500)
sy_sing = KI/np.sqrt(2*np.pi*r)
sy_cut = np.minimum(sy_sing, sY)          # plastik kesilish
series("sigma_y(r) singulyar yechim", (r*1000).tolist(), sy_sing.tolist(),
       xlabel="Yoriq uchidan masofa r, mm", ylabel="sigma_y, MPa")
series("sigma_y(r) plastik kesilish bilan", (r*1000).tolist(), sy_cut.tolist(),
       xlabel="Yoriq uchidan masofa r, mm", ylabel="sigma_y, MPa")
series("Oqish chegarasi", (r*1000).tolist(), np.full_like(r, sY).tolist(),
       xlabel="Yoriq uchidan masofa r, mm", ylabel="sigma_y, MPa")

# --- Loyihalash diagrammasi: sigma_c(a) ---
a_range = np.linspace(0.2, 50.0, 300)/1000.0
sc = KIc/(Y*np.sqrt(np.pi*a_range))
sc_lim = np.minimum(sc, sY)               # oqish ham chegara
series("Kritik kuchlanish sigma_c(a)", (a_range*1000).tolist(), sc_lim.tolist(),
       xlabel="Yoriq yarim uzunligi a, mm", ylabel="Kritik kuchlanish, MPa")
a_trans = (KIc/(Y*sY))**2/np.pi
value("O'tish uzunligi (mo'rt/plastik)", a_trans*1000, "mm")
note(f"a < {a_trans*1000:.2f} mm bo'lganda buzilishni oqish chegarasi "
     f"boshqaradi, undan katta yoriqlarda esa K_Ic boshqaradi.")

# --- Paris qonuni bilan qoldiq resurs ---
C, m = 1.5e-11, 3.0          # da/dN = C*(dK)^m, [mm/sikl], dK [MPa*sqrt(m)]
dsig = float(PARAMS.get("dsig", 100.0))
N, a_cur, step = 0, a, 1e-6
hist_N, hist_a = [0.0], [a*1000]
while a_cur < a_c and N < 5_000_000:
    dK = Y*dsig*np.sqrt(np.pi*a_cur)
    da = C*dK**m
    a_cur += da
    N += 1
    if N % 2000 == 0:
        hist_N.append(float(N)); hist_a.append(a_cur*1000)
hist_N.append(float(N)); hist_a.append(min(a_cur, a_c)*1000)
series("Yoriq o'sishi a(N)", hist_N, hist_a,
       xlabel="Sikllar soni N", ylabel="Yoriq yarim uzunligi a, mm")
value("Qoldiq resurs (Paris)", float(N), "sikl")
value("Tekshirish intervali (N/2)", float(N)/2, "sikl")

table("Materiallarda buzilish qovushqoqligi",
      ["Material", "sigma_Y, MPa", "K_Ic, MPa*sqrt(m)", "a_c (200 MPa da), mm"],
      [[name, sy_, kic, round(float((kic/200.0)**2/np.pi*1000), 2)]
       for name, sy_, kic in [
           ("Yumshoq po'lat", 250, 140),
           ("Yuqori mustahkam po'lat", 1500, 60),
           ("Al 7075-T6", 500, 24),
           ("Titan Ti-6Al-4V", 900, 75),
           ("Al2O3 keramika", 3000, 4),
           ("Beton", 30, 1)]])
note("Yuqori mustahkam materiallarda K_Ic past: mustahkamlik oshgani "
     "sari mo'rtlik ham oshadi — bu klassik muhandislik kompromissi.")
''',
                parameters=[
                    p("sig", "Ishchi kuchlanish σ", 10.0, 800.0, 150.0, 5.0, "MPa"),
                    p("a", "Yoriq yarim uzunligi a", 0.2, 50.0, 4.0, 0.2, "mm"),
                    p("KIc", "Buzilish qovushqoqligi K_Ic", 1.0, 200.0, 24.0, 1.0, "MPa·√m"),
                    p("sY", "Oqish chegarasi σ_Y", 30.0, 2000.0, 500.0, 10.0, "MPa"),
                    p("E", "Yung moduli", 10.0, 400.0, 71.0, 1.0, "GPa"),
                    p("nu", "Puasson koeffitsienti", 0.0, 0.49, 0.33, 0.01),
                    p("Y", "Geometrik koeffitsient Y", 0.5, 3.0, 1.0, 0.05),
                    p("dsig", "Siklik kuchlanish amplitudasi Δσ", 10.0, 400.0, 100.0, 5.0, "MPa"),
                ],
                expected_output=(
                    "K_I = 16,8 MPa·√m, zaxira 1,43; a_c = 8,15 mm; "
                    "r_p = 0,18 mm; G_c = 7,2 kJ/m². Loyihalash diagrammasida "
                    "kichik yoriqlarda σ_Y, katta yoriqlarda K_Ic chegarasi ishlaydi."
                ),
            ),
            visual=vis(
                kind="Yoriq uchi maydoni va loyihalash diagrammasi",
                tool="React/SVG + Matplotlib",
                description=(
                    "$\\sigma_y(r)$ singulyarligi, plastik kesilish, plastik zona "
                    "konturi va $\\sigma_c$–$a$ loyihalash diagrammasi."
                ),
                how_to_draw=(
                    "React/SVG: yoriq geometriyasi uchun plastina to'rtburchagi "
                    "chiziladi, markazida gorizontal qora chiziq — yoriq "
                    "($2a$ uzunlikda, uchlari biroz ochilgan linzasimon shakl). "
                    "Yoriq uchida yarim shaffof 'quloq' shakli (plastik zona) "
                    "$r_p(\\theta) = \\frac{1}{2\\pi}(K_I/\\sigma_Y)^2"
                    "\\cos^2(\\theta/2)[1 + 3\\sin^2(\\theta/2)]$ formulasi "
                    "bo'yicha `<path>` bilan chiziladi. $\\sigma_y(r)$ grafigi "
                    "alohida panelda: singulyar egri chiziq issiq rangda, "
                    "plastik kesilish gorizontal chiziq bilan, kesishgan joyi "
                    "shtrixlangan — kesilgan va qo'shilgan yuzalar teng "
                    "(Irvin korreksiyasi) ekanligi ko'rinadi. Loyihalash "
                    "diagrammasi log–log o'qlarda: $\\sigma_Y$ gorizontal "
                    "chegarasi va $K_{Ic}$ qiyaligi $-1/2$ bo'lgan chiziq "
                    "kesishadi; xavfsiz soha ostida yashil shtrixlanadi."
                ),
            ),
            interp=(
                "Materiallar jadvali eng muhim muhandislik xulosasini beradi: "
                "$\\sigma_Y$ va $K_{Ic}$ deyarli har doim **teskari** "
                "bog'langan. Yumshoq po'latda $a_c = 156$ mm — bunday yoriqni "
                "ko'rmaslik mumkin emas, shuning uchun konstruksiya "
                "'ogohlantirib' buziladi. Yuqori mustahkam po'latda esa "
                "$a_c = 28{,}6$ mm, Al 7075-T6 da atigi 4,6 mm, keramikada "
                "0,13 mm — ya'ni ko'zga ko'rinmaydigan nuqson halokatli. "
                "Aynan shuning uchun aviatsiyada materialni faqat "
                "$\\sigma_Y$ bo'yicha tanlash mumkin emas. Loyihalash "
                "diagrammasidagi o'tish uzunligi ham ma'noli: undan kichik "
                "yoriqlar amalda ahamiyatsiz (oqish avval keladi), kattalari "
                "esa hal qiluvchi. Paris qonuni bo'yicha hisoblangan qoldiq "
                "resurs va uning yarmi sifatidagi tekshirish intervali — "
                "Comet halokatidan keyin dunyo aviatsiyasi qabul qilgan "
                "'damage tolerance' falsafasining son bilan ifodalangan shakli."
            ),
            mistakes=[
                "$K_I$ (kuchlanish intensivligi koeffitsienti, MPa·√m) va "
                "$K_t$ (kuchlanish konsentratsiyasi koeffitsienti, o'lchamsiz) "
                "ni aralashtirish. Ular butunlay boshqa kattaliklar.",
                "$a$ sifatida to'liq yoriq uzunligini olish. Markaziy yoriqda "
                "$a$ — **yarim** uzunlik, chekka yoriqda esa to'liq uzunlik; "
                "$Y$ koeffitsienti ham shunga mos tanlanadi ($Y = 1{,}12$ "
                "chekka yoriq uchun).",
                "Plastik zona katta bo'lganda ham LEFM ni qo'llash. "
                "$r_p$ yoriq uzunligi bilan taqqoslanadigan bo'lsa, $K$ "
                "ma'nosini yo'qotadi va $J$-integral yoki CTOD kerak.",
                "$K_{Ic}$ ni qalinlikka bog'liq emas deb hisoblash. Yupqa "
                "namunada tekis kuchlanish hukmron bo'lib, $K_c$ sezilarli "
                "yuqori chiqadi; $K_{Ic}$ — qalin namunadagi (tekis "
                "deformatsiya) eng past, konservativ qiymat.",
            ],
            quiz=[
                q("Nima uchun yoriq uchidagi maksimal kuchlanishni buzilish "
                  "mezoni sifatida ishlatib bo'lmaydi?",
                  "Chunki chiziqli elastik yechimda u cheksizlikka intiladi "
                  "($\\sigma \\sim r^{-1/2}$) va yoriq uchining o'tkirligiga "
                  "bog'liq. $K_I$ esa chekli va o'lchanadigan kattalik.",
                  "konseptual"),
                q("$K_I$ va $G$ orasidagi bog'lanishni yozing va uning "
                  "ahamiyatini tushuntiring.",
                  "$G = K_I^2/E'$. U energetik (Griffit) va kuchlanish "
                  "(Irvin) yondashuvlarining ekvivalentligini isbotlaydi — "
                  "ikki mustaqil yo'l bir xil javob beradi.", "konseptual"),
                q("$\\sigma = 200$ MPa, $a = 5$ mm, $Y = 1$. $K_I$ ni toping.",
                  "$K_I = 200\\sqrt{\\pi \\cdot 0{,}005} = 200 \\cdot 0{,}1253 "
                  "= 25{,}1$ MPa·√m.", "hisob"),
                q("Yoriq uzunligi ikki baravar oshsa, $K_I$ necha marta ortadi?",
                  "$\\sqrt{2} \\approx 1{,}41$ marta, chunki "
                  "$K_I \\propto \\sqrt{a}$. Shuning uchun yoriq o'sishi "
                  "avval sekin, oxirida tez kechadi.", "hisob"),
                q("Nima uchun yuqori mustahkam materiallar ko'pincha "
                  "mo'rtroq bo'ladi?",
                  "$\\sigma_Y$ oshgani sari plastik deformatsiya qobiliyati "
                  "kamayadi, demak yoriq uchida yutiladigan plastik ish "
                  "$\\gamma_p$ tushadi va $K_{Ic}$ kichrayadi. Jadval buni "
                  "aniq ko'rsatadi.", "talqin"),
                q("Kodda `sy_cut = np.minimum(sy_sing, sY)` nimani modellaydi?",
                  "Plastik kesilishni: real materialda kuchlanish oqish "
                  "chegarasidan oshmaydi, singulyar yechim esa cheksizlikka "
                  "boradi. Bu Irvin korreksiyasining sodda ko'rinishi.", "kod"),
                q("Damage tolerance loyihalashda tekshirish intervali "
                  "qanday belgilanadi?",
                  "Aniqlanadigan eng kichik nuqsondan kritik uzunlikkacha "
                  "bo'lgan resursning yarmi (yoki undan kam) qilib. Shunda "
                  "yoriq kritik holatga yetguncha kamida ikki marta "
                  "tekshiruvdan o'tadi.", "talqin"),
            ],
            bridge=(
                "Qattiq jismning chiziqli, plastik, viskoelastik javobi va "
                "buzilishi to'liq ko'rib chiqildi. Endi tutash muhit "
                "nazariyasining ikkinchi katta tarmog'iga — suyuqlik va gaz "
                "mexanikasiga o'tamiz. Balans qonunlari o'zgarmaydi, faqat "
                "konstitutiv tenglama boshqacha bo'ladi."
            ),
            research=(
                "Elastoplastik yoriqlar mexanikasiga o'ting: Rays "
                "$J$-integralini "
                "$J = \\int_\\Gamma (W\\,dy - \\mathbf{T}\\cdot\\partial\\mathbf{u}/"
                "\\partial x\\,ds)$ o'rganing. Chiziqli holatda $J = G$ "
                "ekanligini isbotlang va uning **yo'ldan mustaqilligini** "
                "sonli tekshiring: yoriq uchi atrofida turli konturlar oling "
                "va integral qiymatini taqqoslang. CTOD (crack tip opening "
                "displacement) mezoni bilan bog'lanishi "
                "$J = m\\sigma_Y\\delta_t$ qanday asoslanadi?"
            ),
            manim_ref=manim(
                scene="CrackTipScene",
                module="animatsiya/scenes/tmm_fracture.py",
                title="Yoriq uchidagi kuchlanish maydoni",
                summary=(
                    "Yoriq uchi atrofida $\\sigma_y(r,\\theta)$ rangli maydon, "
                    "$r^{-1/2}$ singulyarlik va plastik zonaning 'quloq' shakli "
                    "ko'rsatiladi; yoriq uzayganda maydon qanday o'sishi animatsiya qilinadi."
                ),
            ),
        ),
    ),
]
