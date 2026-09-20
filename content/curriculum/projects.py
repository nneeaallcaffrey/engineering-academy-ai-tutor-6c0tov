"""Har bir fan uchun yakuniy loyiha (23-talab).

Har bir loyihaning `starter_code` i — sandbox'da ishlaydigan HAQIQIY kod:
u aniq yechim yoki mustaqil etalon bilan o'zini tekshiradi va talaba
uni kengaytirishi uchun asos bo'ladi.
"""

from __future__ import annotations

from content.curriculum.schema import FinalProject, ProjectStage, p

_S = ProjectStage

PROJECTS: list[FinalProject] = [
    FinalProject(
        id="proj-nm",
        subject_id="nazariy-mexanika",
        title="Krivoship-polzun mexanizmini tahlil qilish va muvozanatlash",
        problem_statement=(
            "Ichki yonuv dvigateli yoki kompressorning krivoship-polzun "
            "mexanizmi berilgan. Uning kinematikasini aniq (yaqinlashishsiz) "
            "hisoblang, inersiya kuchlarini toping va ularning ramaga "
            "uzatiladigan qoldig'ini muvozanatlash orqali kamaytiring. "
            "Asosiy savol: qarama-qarshi massalar bilan birinchi tartibli "
            "inersiya kuchini to'liq yo'qotish mumkinmi, va bunda ko'ndalang "
            "yo'nalishda nima paydo bo'ladi?"
        ),
        stages=[
            _S("1. Kinematika",
               "Polzunning siljishi, tezligi va tezlanishini burchak "
               "bo'yicha aniq ifodalar bilan hisoblang. Natijani sonli "
               "differensiallash bilan tekshiring va chetki nuqtalarda "
               "klassik -r*om^2*(1+lambda) va r*om^2*(1-lambda) "
               "qiymatlari bilan solishtiring."),
            _S("2. Taqribiy qatorni baholash",
               "a ~ -r*om^2*(cos th + lambda*cos 2th) taqribini aniq "
               "yechim bilan taqqoslang va lambda = r/L ning turli "
               "qiymatlarida xatolikni o'lchang. Qaysi lambda dan "
               "boshlab taqrib yaroqsiz bo'ladi?"),
            _S("3. Massalarni keltirish",
               "Shatun massasini ikki nuqtaga (krivoship barmog'i va "
               "polzun) statik ekvivalent tarzda keltiring. Keltirish "
               "shartlarini (massa, statik moment) yozing va inersiya "
               "momenti bo'yicha xatolikni baholang."),
            _S("4. Inersiya kuchlari va moment",
               "Birinchi va ikkinchi tartibli inersiya kuchlarini "
               "ajrating, ramaga uzatiladigan yig'indi kuchni va "
               "ag'daruvchi momentni bir tsikl davomida hisoblang."),
            _S("5. Muvozanatlash",
               "Krivoshipga qarama-qarshi massa qo'ying va uning "
               "qiymatini optimallashtiring. Qoldiq kuchning "
               "gorizontal va vertikal tashkil etuvchilarini "
               "taqqoslang — to'liq muvozanatlash nima uchun "
               "imkonsizligini ko'rsating."),
            _S("6. Xulosa va tavsiya",
               "Tanlangan muvozanatlash darajasini asoslang va "
               "qoldiq tebranishning chastota tarkibini keltiring."),
        ],
        deliverables=[
            "Kinematik va dinamik grafiklar (x, v, a, F, M) bir tsikl uchun",
            "Aniq va taqribiy yechimning xatolik tahlili",
            "Muvozanatlash massasining optimal qiymati va asoslash",
            "Qoldiq kuchning godografi (gorizontal-vertikal tekislikda)",
            "2-3 sahifalik hisobot: farazlar, natijalar, tavsiya",
        ],
        starter_code='''"""NM loyihasi: krivoship-polzun mexanizmining kinematikasi va dinamikasi."""
import numpy as np
from labkit import PARAMS, note, series, table, value

r = float(PARAMS.get("r", 60.0))*1e-3          # krivoship radiusi, mm -> m
L = float(PARAMS.get("L", 240.0))*1e-3         # shatun uzunligi
n_rpm = float(PARAMS.get("n_rpm", 1500.0))     # aylanish chastotasi
m_p = float(PARAMS.get("m_p", 0.45))           # polzun massasi, kg

lam = r/L
om = 2*np.pi*n_rpm/60.0
value("Nisbat lambda = r/L", lam, "-")
value("Burchak tezligi", om, "rad/s")

th = np.linspace(0.0, 2*np.pi, 721)
# ANIQ kinematika (yaqinlashishsiz)
s = np.sqrt(L**2 - (r*np.sin(th))**2)
x = r*np.cos(th) + s
# ANIQ hosilalar: s' va s'' ni qo'lda chiqaramiz
ds = -(r**2/2)*np.sin(2*th)/s                     # ds/dth
dx = -r*np.sin(th) + ds                           # dx/dth
d2s = -(r**2/2)*(2*np.cos(2*th)*s - np.sin(2*th)*ds)/s**2
d2x = -r*np.cos(th) + d2s                         # d2x/dth2
v = om*dx
a = om**2*d2x

# NAZORAT: analitik hosilani sonli hosila bilan solishtiramiz
dth = th[1] - th[0]
v_num = om*np.gradient(x, dth)
# chetki nuqtalarda np.gradient bir tomonlama - ichki nuqtalarni olamiz
value("Hosila nazorati (v)",
      float(np.max(np.abs(v[1:-1] - v_num[1:-1]))/np.max(np.abs(v))*100), "%")
# NAZORAT: chetki nuqtalarda klassik formulalar
value("a(0) nazorati: -r om^2 (1+lam)",
      float(abs(a[0] + r*om**2*(1 + lam))), "m/s^2")
value("a(180) nazorati: r om^2 (1-lam)",
      float(abs(a[360] - r*om**2*(1 - lam))), "m/s^2")

value("Yurish (2r)", (x.max()-x.min())*1e3, "mm")
value("Yurish nazorati 2r", 2*r*1e3, "mm")

# taqribiy qator: a ~ -r om^2 (cos th + lambda cos 2th)
a_appr = -r*om**2*(np.cos(th) + lam*np.cos(2*th))
value("Taqribiy qator xatosi", float(np.max(np.abs(a-a_appr))/np.max(np.abs(a))*100), "%")

F_in = m_p*a                                    # inersiya kuchi
M_t = F_in*(-v/om)                              # quvvat balansidan moment
value("Maks tezlik", float(np.max(np.abs(v))), "m/s")
value("Maks tezlanish", float(np.max(np.abs(a))), "m/s^2")
value("Maks inersiya kuchi", float(np.max(np.abs(F_in))), "N")
value("Maks moment", float(np.max(np.abs(M_t))), "N*m")
series("Siljish x(th)", th, x*1e3, "th, rad", "x, mm")
series("Tezlanish a(th)", th, a, "th, rad", "a, m/s^2")
table("Xarakterli holatlar",
      ["th, deg", "x, mm", "v, m/s", "a, m/s^2"],
      [[int(np.degrees(th[i])), f"{x[i]*1e3:.2f}", f"{v[i]:.2f}", f"{a[i]:.1f}"]
       for i in (0, 90, 180, 270, 360, 540)])
note("Bu boshlang'ich kod aniq kinematikani beradi. Loyihada uni "
     "kengaytiring: shatun massasini ikki nuqtaga keltirish, "
     "birinchi va ikkinchi tartibli muvozanatlash, teskari "
     "massalar bilan qoldiq kuchni kamaytirish.")''',
        evaluation=[
            "Kinematika aniq ifodalar bilan chiqarilgan va tekshirilgan (20%)",
            "Massalarni keltirish to'g'ri va uning cheklovi ko'rsatilgan (15%)",
            "Inersiya kuchlari tartiblarga ajratilgan (20%)",
            "Muvozanatlash optimallashtirilgan va cheklovi tushuntirilgan (25%)",
            "Hisobot aniq, grafiklar o'qiladigan, xulosa asoslangan (20%)",
        ],
        parameters=[
            p("r", "Krivoship radiusi", 20.0, 120.0, 60.0, 5.0, "mm"),
            p("L", "Shatun uzunligi", 100.0, 500.0, 240.0, 10.0, "mm"),
            p("n_rpm", "Aylanishlar soni", 300.0, 4000.0, 1500.0, 100.0, "ayl/min"),
            p("m_p", "Polzun massasi", 0.1, 3.0, 0.45, 0.05, "kg"),
        ],
    ),
    FinalProject(
        id="proj-mq",
        subject_id="materiallar-qarshiligi",
        title="Egilish va buralish ostidagi uzatma valini loyihalash",
        problem_statement=(
            "Reduktorning uzatma vali berilgan quvvatni berilgan "
            "aylanishlar sonida uzatadi. Valning diametrini "
            "mustahkamlik bo'yicha tanlang, salqilikni tekshiring va "
            "shponka o'yig'idagi kuchlanish konsentratsiyasini hisobga "
            "oling. Asosiy savol: uchinchi va to'rtinchi mustahkamlik "
            "nazariyalari qancha farq qiladi va qaysi biri tanlanishi "
            "kerak?"
        ),
        stages=[
            _S("1. Yuklarni aniqlash",
               "Quvvat va aylanishlar sonidan burovchi momentni, undan "
               "esa tishli ilashishdagi aylanma va radial kuchlarni "
               "toping. Muvozanat shartini alohida tekshiring."),
            _S("2. Ichki kuchlar epyuralari",
               "Kesuvchi kuch, eguvchi moment va burovchi moment "
               "epyuralarini ikki tekislikda quring, xavfli kesimni "
               "aniqlang."),
            _S("3. Mustahkamlik bo'yicha diametr",
               "Uchinchi (Treska) va to'rtinchi (Mizes) nazariyalar "
               "bo'yicha ekvivalent momentni hisoblang va diametrni "
               "toping. Farqni foizda keltiring va tanlovni asoslang."),
            _S("4. Bikrlik tekshiruvi",
               "Salqilikni va tayanchlardagi burilish burchagini "
               "hisoblang, ularni podshipnik va tishli uzatma uchun "
               "ruxsat etilgan qiymatlar bilan taqqoslang."),
            _S("5. Konsentratsiya va charchoq",
               "Shponka o'yig'i va galtel uchun konsentratsiya "
               "koeffitsientini qo'llang, siklik yuk ostidagi charchoq "
               "zaxirasini baholang."),
            _S("6. Yakuniy kesim va xulosa",
               "Standart diametrga yaxlitlang, barcha tekshiruvlarni "
               "jadvalga jamlang va yakuniy zaxira koeffitsientini "
               "keltiring."),
        ],
        deliverables=[
            "Ichki kuchlar epyuralari (ikki tekislikda) va xavfli kesim",
            "Ikki nazariya bo'yicha diametrlar va ularning taqqoslanishi",
            "Bikrlik va charchoq tekshiruvlari",
            "Yakuniy kesim chizmasi va zaxira koeffitsientlari jadvali",
            "2-3 sahifalik hisobot",
        ],
        starter_code='''"""MQ loyihasi: egilish va buralish ostidagi valni loyihalash."""
import numpy as np
from labkit import PARAMS, note, series, table, value

P_kw = float(PARAMS.get("P_kw", 15.0))         # uzatilayotgan quvvat, kW
n_rpm = float(PARAMS.get("n_rpm", 720.0))      # aylanishlar soni
L = float(PARAMS.get("L", 600.0))*1e-3         # tayanchlar orasi, mm -> m
D_g = float(PARAMS.get("D_g", 200.0))*1e-3     # tishli g'ildirak diametri
sig_all = float(PARAMS.get("sig_all", 60.0))*1e6   # ruxsat etilgan kuchlanish

om = 2*np.pi*n_rpm/60.0
T = P_kw*1e3/om                                 # burovchi moment, N*m
value("Burchak tezligi", om, "rad/s")
value("Burovchi moment T", T, "N*m")
value("T nazorati (9550 P/n)", 9550.0*P_kw/n_rpm, "N*m")

F_t = 2*T/D_g                                   # aylanma kuch
F_r = F_t*np.tan(np.radians(20.0))              # radial kuch (20 grad ilashish)
F = np.hypot(F_t, F_r)
value("Aylanma kuch Ft", F_t, "N")
value("Radial kuch Fr", F_r, "N")
value("To'liq kuch F", F, "N")

# g'ildirak o'rtada: M_max = F L / 4
M = F*L/4.0
value("Eguvchi moment M", M, "N*m")
# muvozanat nazorati: reaksiyalar yig'indisi
R = F/2.0
value("Muvozanat nazorati", abs(2*R - F), "N")

# Ekvivalent moment: 3-nazariya (Treska) va 4-nazariya (Mizes)
M_t3 = np.hypot(M, T)
M_t4 = np.sqrt(M**2 + 0.75*T**2)
value("M_ekv (3-nazariya)", M_t3, "N*m")
value("M_ekv (4-nazariya)", M_t4, "N*m")
value("Nazariyalar farqi", (M_t3 - M_t4)/M_t4*100, "%")

d3 = (32*M_t3/(np.pi*sig_all))**(1/3)
d4 = (32*M_t4/(np.pi*sig_all))**(1/3)
value("d (3-nazariya)", d3*1e3, "mm")
value("d (4-nazariya)", d4*1e3, "mm")
d = np.ceil(d4*1e3/5)*5*1e-3                    # 5 mm ga yaxlitlash
value("Tanlangan d", d*1e3, "mm")

W = np.pi*d**3/32.0
sig = M_t4/W
value("Haqiqiy kuchlanish", sig/1e6, "MPa")
value("Zaxira koeffitsienti", sig_all/sig, "-")
# NAZORAT: I = int y^2 dA ni kesim bo'yicha sonli integrallash bilan
yy = np.linspace(-d/2, d/2, 20001)
b_y = 2*np.sqrt(np.maximum((d/2)**2 - yy**2, 0.0))      # doira kengligi
I_num = np.trapezoid(yy**2*b_y, yy)
value("I nazorati (sonli/analitik)", I_num/(np.pi*d**4/64.0), "-")

E = 210e9
I = np.pi*d**4/64.0
f_max = F*L**3/(48*E*I)
value("Maks salqilik", f_max*1e3, "mm")
value("Salqilik / L", f_max/L*1000, "‰")
table("Nazariyalar taqqoslash",
      ["Nazariya", "M_ekv, N*m", "d_hisob, mm"],
      [["3 (Treska)", f"{M_t3:.1f}", f"{d3*1e3:.2f}"],
       ["4 (Mizes)", f"{M_t4:.1f}", f"{d4*1e3:.2f}"]])
dd = np.linspace(0.6*d, 1.6*d, 60)
series("Kuchlanish d bo'yicha", dd*1e3, M_t4/(np.pi*dd**3/32)/1e6, "d, mm", "sigma, MPa")
note("Boshqi kod g'ildirak o'rtada joylashgan sodda holatni beradi. "
     "Loyihada uni kengaytiring: ikki g'ildirak, ikki tekislikdagi "
     "egilish, shponka o'yig'ining konsentratsiyasi, charchoqqa "
     "hisob va podshipnik resursini baholash.")''',
        evaluation=[
            "Yuklar to'g'ri aniqlangan va muvozanat tekshirilgan (15%)",
            "Epyuralar to'g'ri va xavfli kesim asoslangan (20%)",
            "Ikki nazariya taqqoslangan, tanlov asoslangan (25%)",
            "Bikrlik va charchoq tekshiruvlari bajarilgan (20%)",
            "Hisobot va chizma sifati (20%)",
        ],
        parameters=[
            p("P_kw", "Uzatilayotgan quvvat", 1.0, 100.0, 15.0, 1.0, "kW"),
            p("n_rpm", "Aylanishlar soni", 100.0, 3000.0, 720.0, 10.0, "ayl/min"),
            p("L", "Tayanchlar orasi", 200.0, 1500.0, 600.0, 50.0, "mm"),
            p("D_g", "Tishli g'ildirak diametri", 50.0, 500.0, 200.0, 10.0, "mm"),
            p("sig_all", "Ruxsat etilgan kuchlanish", 30.0, 150.0, 60.0, 5.0, "MPa"),
        ],
    ),
    FinalProject(
        id="proj-tmm",
        subject_id="tutash-muhitlar",
        title="Yuqori bosimli qalin devorli quvurni tahlil qilish va avtofretaj",
        problem_statement=(
            "Gidravlik presning yuqori bosimli quvuri qalin devorli "
            "silindr sifatida ishlaydi. Elastik holatdagi kuchlanish "
            "taqsimotini Lame yechimi bilan toping, oqishning "
            "boshlanish bosimini va to'liq plastik holatga mos "
            "chegaraviy bosimni aniqlang. Asosiy savol: avtofretaj "
            "(oldindan plastik deformatsiyalash) ish bosimini qancha "
            "oshirishga imkon beradi va buning narxi nima?"
        ),
        stages=[
            _S("1. Elastik yechim",
               "Lame formulalari bilan sigma_r, sigma_theta va "
               "sigma_z ni toping. Chegaraviy shartlarni "
               "(sigma_r(a) = -p_i, sigma_r(b) = -p_o) va "
               "sigma_r + sigma_theta = const invariantini alohida "
               "tekshiring."),
            _S("2. Oqishning boshlanishi",
               "von Mizes mezoni bo'yicha eng xavfli nuqtani "
               "aniqlang (u ichki yuzada bo'lishini ko'rsating) va "
               "p_y bosimini toping. Natijani Treska mezoni bilan "
               "taqqoslang."),
            _S("3. Elastoplastik holat",
               "Plastik zona radiusi c ni bosimga bog'liq ravishda "
               "toping, elastik va plastik sohalardagi kuchlanishlarni "
               "birlashtiring va uzluksizlikni tekshiring."),
            _S("4. Chegaraviy bosim",
               "To'liq plastik holatdagi chegaraviy bosimni hisoblang "
               "va uning p_y ga nisbatini devor nisbati b/a bo'yicha "
               "grafikda keltiring."),
            _S("5. Avtofretaj",
               "Yuklab-bo'shatish siklini modellashtiring, qoldiq "
               "kuchlanishni toping va yangi (oshirilgan) ish bosimini "
               "aniqlang. Teskari oqish xavfini tekshiring."),
            _S("6. Loyihaviy xulosa",
               "Devor nisbatini optimallashtiring: massa va ish "
               "bosimi orasidagi kompromissni grafik bilan asoslang."),
        ],
        deliverables=[
            "Kuchlanish epyuralari (elastik va elastoplastik holatlar)",
            "p_y va p_lim qiymatlari, b/a bo'yicha bog'liqlik grafigi",
            "Avtofretajdan keyingi qoldiq kuchlanish taqsimoti",
            "Ish bosimining oshishi va uning miqdoriy asoslanishi",
            "2-3 sahifalik hisobot",
        ],
        starter_code='''"""TMM loyihasi: qalin devorli quvurning elastik va plastik holati."""
import numpy as np
from labkit import PARAMS, note, series, table, value

a = float(PARAMS.get("a", 50.0))*1e-3          # ichki radius
b = float(PARAMS.get("b", 100.0))*1e-3         # tashqi radius
p_i = float(PARAMS.get("p_i", 80.0))*1e6       # ichki bosim
sig_y = float(PARAMS.get("sig_y", 420.0))*1e6  # oqish chegarasi
p_o = 0.0

k = b/a
value("Devor nisbati b/a", k, "-")
r = np.linspace(a, b, 400)

# --- Lame yechimi ------------------------------------------------------
A = (p_i*a**2 - p_o*b**2)/(b**2 - a**2)
B = (p_i - p_o)*a**2*b**2/(b**2 - a**2)
sig_r = A - B/r**2
sig_t = A + B/r**2
sig_z = A                                       # yopiq uchli quvur

# NAZORAT: chegaraviy shartlar
value("ChSh nazorati sigma_r(a) = -p_i", abs(sig_r[0] + p_i)/p_i*100, "%")
value("ChSh nazorati sigma_r(b) = 0", abs(sig_r[-1])/p_i*100, "%")
# NAZORAT: sigma_r + sigma_t = 2A = const (Lame invarianti)
value("Lame invarianti tarqalishi",
      float(np.max(np.abs(sig_r + sig_t - 2*A))/abs(2*A)*100), "%")

value("sigma_t ichkarida", sig_t[0]/1e6, "MPa")
value("sigma_t tashqarida", sig_t[-1]/1e6, "MPa")
value("sigma_t nisbati (ich/tash)", sig_t[0]/sig_t[-1], "-")

# --- von Mizes va oqish boshlanishi ------------------------------------
sv = np.sqrt(0.5*((sig_r-sig_t)**2 + (sig_t-sig_z)**2 + (sig_z-sig_r)**2))
value("von Mizes ichkarida", sv[0]/1e6, "MPa")
value("Zaxira koeffitsienti", sig_y/sv[0], "-")
# oqish ichki yuzada boshlanadi: p_y = sig_y (b^2-a^2)/(sqrt(3) b^2)
p_y = sig_y*(b**2 - a**2)/(np.sqrt(3)*b**2)
value("Oqish boshlanish bosimi p_y", p_y/1e6, "MPa")
# NAZORAT: p_i = p_y da von Mizes aynan sig_y bo'lishi kerak
Bv = p_y*a**2*b**2/(b**2-a**2); Av = p_y*a**2/(b**2-a**2)
sv_chk = np.sqrt(3)*Bv/a**2
value("p_y nazorati (sv/sig_y)", sv_chk/sig_y, "-")

# --- To'liq plastik holat ----------------------------------------------
p_lim = 2*sig_y/np.sqrt(3)*np.log(k)
value("Chegaraviy bosim p_lim", p_lim/1e6, "MPa")
value("p_lim / p_y", p_lim/p_y, "-")

series("sigma_r(r)", r*1e3, sig_r/1e6, "r, mm", "sigma_r, MPa")
series("sigma_t(r)", r*1e3, sig_t/1e6, "r, mm", "sigma_theta, MPa")
series("von Mizes(r)", r*1e3, sv/1e6, "r, mm", "sigma_vM, MPa")
table("Kuchlanishlar taqsimoti",
      ["r, mm", "sigma_r, MPa", "sigma_theta, MPa", "von Mizes, MPa"],
      [[f"{r[i]*1e3:.1f}", f"{sig_r[i]/1e6:.1f}", f"{sig_t[i]/1e6:.1f}",
        f"{sv[i]/1e6:.1f}"] for i in (0, 100, 200, 300, 399)])
note("Boshlang'ich kod elastik Lame yechimini va oqish chegaralarini "
     "beradi. Loyihada uni kengaytiring: elastoplastik radiusni "
     "topish, avtofretaj (oldindan plastik deformatsiyalash) orqali "
     "qoldiq kuchlanish hosil qilish va uning ish bosimini qancha "
     "oshirishini miqdoriy baholash.")''',
        evaluation=[
            "Lame yechimi to'g'ri va chegaraviy shartlar tekshirilgan (20%)",
            "Oqish mezoni to'g'ri qo'llanilgan, mezonlar taqqoslangan (20%)",
            "Elastoplastik yechim uzluksiz va asoslangan (25%)",
            "Avtofretaj tahlili to'liq, teskari oqish tekshirilgan (20%)",
            "Hisobot va grafiklar sifati (15%)",
        ],
        parameters=[
            p("a", "Ichki radius", 10.0, 200.0, 50.0, 5.0, "mm"),
            p("b", "Tashqi radius", 20.0, 400.0, 100.0, 5.0, "mm"),
            p("p_i", "Ichki bosim", 10.0, 400.0, 80.0, 10.0, "MPa"),
            p("sig_y", "Oqish chegarasi", 200.0, 1200.0, 420.0, 20.0, "MPa"),
        ],
    ),
    FinalProject(
        id="proj-pq",
        subject_id="plastinalar-qobiqlar",
        title="Qovurg'ali panelni loyihalash va massa bo'yicha optimallashtirish",
        problem_statement=(
            "Kema yoki samolyot korpusining to'rtburchak paneli bir "
            "tekis bosim ostida ishlaydi. Silliq qoplama talab "
            "qilingan bikrlikni juda katta massa evaziga beradi. "
            "Panelni qovurg'alar bilan kuchaytiring va ekvivalent "
            "ortotrop model bilan hisoblang. Asosiy savol: bir xil "
            "salqilikda qovurg'ali panel silliq qoplamadan qancha "
            "yengil va bu yutuq qanday chegaralangan?"
        ),
        stages=[
            _S("1. Silliq qoplama",
               "Navye qatori bilan SSSS plastinaning salqiligi va "
               "momentini toping. Markazdagi sin(m*pi/2)sin(n*pi/2) "
               "ishora ko'paytuvchilarini TUSHIRIB QOLDIRMANG va "
               "natijani kvadrat plastina uchun ma'lum 0,00406 "
               "koeffitsienti bilan tekshiring."),
            _S("2. Qovurg'ali kesimning geometriyasi",
               "Qoplama va qovurg'aning qo'shma kesimi uchun neytral "
               "o'qni va inersiya momentini toping. Qoplamaning "
               "ishtirok etuvchi kengligi (effective width) "
               "tushunchasini qo'llang."),
            _S("3. Ekvivalent ortotrop model",
               "Dx, Dy va aralash had H ni hisoblang, ortotrop Navye "
               "yechimini quring va silliq qoplama bilan "
               "taqqoslang."),
            _S("4. Massa bo'yicha optimallashtirish",
               "Qovurg'alar soni, balandligi va qalinligini "
               "o'zgartirib, berilgan salqilik chegarasida eng yengil "
               "variantni toping."),
            _S("5. Mahalliy tekshiruvlar",
               "Qovurg'alar orasidagi qoplamaning mahalliy egilishini "
               "va qovurg'aning mahalliy ustuvorligini tekshiring — "
               "ekvivalent model bularni ko'rsatmaydi."),
            _S("6. Tekshirish va xulosa",
               "Natijani chekli elementlar bilan mustaqil tekshiring "
               "va ekvivalent modelning xatoligini baholang."),
        ],
        deliverables=[
            "Silliq va qovurg'ali panel uchun salqilik va kuchlanish",
            "Ekvivalent bikrliklarning chiqarilishi",
            "Massa-salqilik optimallashtirish grafigi",
            "Mahalliy ustuvorlik va mahalliy egilish tekshiruvlari",
            "FEM bilan tekshirish natijasi va xatolik bahosi",
            "3-4 sahifalik hisobot",
        ],
        starter_code='''"""PQ loyihasi: qovurg'ali to'rtburchak panelni loyihalash."""
import numpy as np
from labkit import PARAMS, note, series, table, value

a = float(PARAMS.get("a", 1.2))                # panel tomoni, m
b = float(PARAMS.get("b", 1.2))
h = float(PARAMS.get("h", 6.0))*1e-3           # qoplama qalinligi
q = float(PARAMS.get("q", 5.0))*1e3            # bir tekis yuk, kPa -> Pa
n_rib = int(PARAMS.get("n_rib", 3))            # qovurg'alar soni
E, nu, rho = 210e9, 0.3, 7850.0

D = E*h**3/(12*(1 - nu**2))
value("Silliq qoplama D", D, "N*m")

# --- Navye qatori (su-22 dagi tuzoq: ishora ko'paytuvchilari) ----------
M_ODD = 41
def navier(A, B, Dx, Dy=None, H=None):
    """SSSS plastina, bir tekis yuk. Dy, H berilmasa - izotrop."""
    Dy = Dx if Dy is None else Dy
    H = Dx if H is None else H
    w = 0.0; mx = 0.0
    for m in range(1, M_ODD, 2):
        for n in range(1, M_ODD, 2):
            # markazda sin(m pi/2) sin(n pi/2) - TUSHIRIB QOLDIRMANG
            sg = (-1)**((m-1)//2)*(-1)**((n-1)//2)
            den = Dx*(m/A)**4 + 2*H*(m/A)**2*(n/B)**2 + Dy*(n/B)**4
            w += sg/(m*n*den)
            mx += sg*(Dx*(m/A)**2 + nu*Dy*(n/B)**2)/(m*n*den)
    return 16*q/np.pi**6*w, 16*q/np.pi**4*mx

w_pl, M_pl = navier(a, b, D)
value("w_max silliq", w_pl*1e3, "mm")
value("Moment silliq", M_pl, "N*m/m")
# NAZORAT: kvadrat SSSS uchun ma'lum koeffitsient 0,00406
value("Koeffitsient w D/(q a^4)", w_pl*D/(q*a**4), "-")
value("Adabiyotdagi qiymat", 0.00406, "-")
value("Koeffitsient xatosi", abs(w_pl*D/(q*a**4) - 0.00406)/0.00406*100, "%")
sig_pl = 6*M_pl/h**2
value("Kuchlanish silliq", sig_pl/1e6, "MPa")

# --- Qovurg'ali panel: ekvivalent ortotrop bikrliklar ------------------
h_r = float(PARAMS.get("h_r", 40.0))*1e-3      # qovurg'a balandligi
t_r = float(PARAMS.get("t_r", 5.0))*1e-3       # qovurg'a qalinligi
s_r = b/(n_rib + 1)                            # qovurg'alar qadami
# qo'shma kesimning neytral o'qi va inersiya momenti (birlik kenglikka)
A_p, A_r = h*s_r, h_r*t_r
y_p, y_r = 0.0, (h + h_r)/2
y_c = (A_p*y_p + A_r*y_r)/(A_p + A_r)
I_c = (s_r*h**3/12 + A_p*(y_c - y_p)**2
       + t_r*h_r**3/12 + A_r*(y_r - y_c)**2)
Dx = E*I_c/s_r                                 # qovurg'a yo'nalishi bo'yicha
Dy = D                                          # ko'ndalang yo'nalish
H = np.sqrt(Dx*Dy)*0 + (nu*np.sqrt(Dx*Dy) + (1 - nu)*D)   # aralash had
value("Qovurg'a qadami", s_r*1e3, "mm")
value("Neytral o'q y_c", y_c*1e3, "mm")
value("Dx (qovurg'ali)", Dx, "N*m")
value("Dx / D", Dx/D, "marta")

w_rib, M_rib = navier(a, b, Dx, Dy, H)
value("w_max qovurg'ali", w_rib*1e3, "mm")
value("Salqilik kamayishi", w_pl/w_rib, "marta")

# --- Massa taqqoslash: teng bikrlikdagi silliq qoplama -----------------
h_eq = (12*(1 - nu**2)*Dx/E)**(1/3)
m_rib = rho*(h*a*b + n_rib*a*h_r*t_r)
m_eq = rho*h_eq*a*b
value("Teng bikrlikdagi qalinlik", h_eq*1e3, "mm")
value("Qovurg'ali panel massasi", m_rib, "kg")
value("Silliq ekvivalent massasi", m_eq, "kg")
value("Massa yutug'i", m_eq/m_rib, "marta")

def Dx_of(k):
    """k ta qovurg'a uchun bo'ylama bikrlik (birlik kenglikka)."""
    sp = b/(k + 1)
    Ap, Ar = h*sp, h_r*t_r
    yc = Ar*(h + h_r)/2/(Ap + Ar)
    Ic = (sp*h**3/12 + Ap*yc**2
          + t_r*h_r**3/12 + Ar*((h + h_r)/2 - yc)**2)
    return E*Ic/sp

# NAZORAT: Dx_of(n_rib) yuqorida qo'lda hisoblangan Dx bilan mos kelsinmi
value("Dx_of nazorati", Dx_of(n_rib)/Dx, "-")
ks = list(range(1, 9))
series("Qovurg'alar soni bo'yicha salqilik", ks,
       [navier(a, b, Dx_of(k), D, D)[0]*1e3 for k in ks],
       "qovurg'alar soni", "w_max, mm")
table("Silliq va qovurg'ali panel",
      ["Variant", "w_max, mm", "Massa, kg"],
      [["Silliq qoplama", f"{w_pl*1e3:.3f}", f"{rho*h*a*b:.2f}"],
       [f"Qovurg'ali (n={n_rib})", f"{w_rib*1e3:.3f}", f"{m_rib:.2f}"],
       ["Teng bikrlikdagi silliq", f"{w_rib*1e3:.3f}", f"{m_eq:.2f}"]])
note("Boshlang'ich kod ekvivalent ortotrop model beradi. Loyihada uni "
     "kengaytiring: qovurg'alarning lokal ustuvorligi, qoplamaning "
     "qovurg'alar orasidagi mahalliy egilishi, ikki yo'nalishli "
     "qovurg'alash va natijani chekli elementlar bilan tekshirish.")''',
        evaluation=[
            "Navye yechimi to'g'ri va etalon bilan tekshirilgan (20%)",
            "Ekvivalent bikrliklar to'g'ri chiqarilgan (20%)",
            "Optimallashtirish asoslangan va chegaralar ko'rsatilgan (20%)",
            "Mahalliy tekshiruvlar bajarilgan (20%)",
            "FEM tekshiruvi va hisobot sifati (20%)",
        ],
        parameters=[
            p("a", "Panel tomoni a", 0.5, 3.0, 1.2, 0.1, "m"),
            p("b", "Panel tomoni b", 0.5, 3.0, 1.2, 0.1, "m"),
            p("h", "Qoplama qalinligi", 2.0, 20.0, 6.0, 0.5, "mm"),
            p("q", "Bir tekis yuk", 1.0, 50.0, 5.0, 1.0, "kPa"),
            p("n_rib", "Qovurg'alar soni", 1, 8, 3, 1, "dona"),
            p("h_r", "Qovurg'a balandligi", 10.0, 120.0, 40.0, 5.0, "mm"),
            p("t_r", "Qovurg'a qalinligi", 2.0, 15.0, 5.0, 0.5, "mm"),
        ],
    ),
    FinalProject(
        id="proj-su",
        subject_id="sonli-usullar",
        title="To'liq hisoblash zanjiri: modeldan ishonchlilik chegarasigacha",
        problem_statement=(
            "O'zingiz tanlagan konstruksiya elementi uchun to'liq "
            "hisoblash zanjirini quring: modellashtirish qarorini "
            "asoslashdan boshlab, natijani xatolik chegarasi bilan "
            "keltirishgacha. Bu loyiha butun kursning yakuni — unda "
            "beshta fanning hammasi ishlatiladi. Asosiy talab: "
            "yakuniy natija bitta son emas, balki asoslangan "
            "ishonchlilik oralig'i bo'lishi kerak."
        ),
        stages=[
            _S("1. Modellashtirish qarori",
               "Konstruksiyani tanlang va qaysi nazariya "
               "qo'llanilishini asoslang (sterjen, balka, plastina, "
               "qobiq yoki 3D). Farazlarni aniq ro'yxat qilib "
               "yozing."),
            _S("2. Etalon yechim",
               "Analitik yechim, soddalashtirilgan model yoki yuqori "
               "aniqlikdagi kvadratura bilan mustaqil etalon quring. "
               "Etalonning o'zini ham tekshiring (masalan, "
               "kvadratura tugunlari sonini oshirib)."),
            _S("3. Sonli yechim",
               "FEM (yoki mos usul) bilan yeching. Element turini, "
               "integrallash tartibini va chegaraviy shartlarni "
               "qo'llash usulini asoslang."),
            _S("4. Yaqinlashish va kuzatilgan tartib",
               "Kamida uchta to'rda hisoblang, kuzatilgan tartib "
               "p_obs ni o'lchang va uni nazariy tartib bilan "
               "taqqoslang. Mos kelmasa — sababini toping."),
            _S("5. Richardson va GCI",
               "Richardson ekstrapolyatsiyasi bilan to'rdan mustaqil "
               "qiymatni baholang va GCI bilan xatolik chegarasini "
               "quring. GCI haqiqiy xatoni qoplaganini tekshiring."),
            _S("6. Validatsiya va farazlarni tekshirish",
               "Barcha model farazlarini natijaga qaytarib "
               "solishtiring (yupqalik, kichik siljish, elastiklik). "
               "Biror shart buzilgan bo'lsa — buni ochiq ayting va "
               "modelni tuzating."),
            _S("7. Resurs rejasi",
               "Masalani o'n marta maydalash uchun qancha xotira va "
               "vaqt kerakligini baholang; to'g'ri va iterativ "
               "yechuvchi orasidagi tanlovni asoslang."),
        ],
        deliverables=[
            "Modellashtirish qarori va farazlar ro'yxati",
            "Mustaqil etalon va uning o'z tekshiruvi",
            "Yaqinlashish jadvali va kuzatilgan tartib p_obs",
            "Richardson ekstrapolyatsiyasi va GCI chegarasi",
            "Farazlar validatsiyasi jadvali (har biri OK/BUZILDI)",
            "Resurs bahosi va yechuvchi tanlovi",
            "4-5 sahifalik hisobot: yakuniy natija xatolik chegarasi bilan",
        ],
        starter_code='''"""SU loyihasi: to'liq hisoblash zanjiri - FEM, yaqinlashish, GCI."""
import numpy as np
from labkit import PARAMS, note, series, table, value
from numpy.polynomial.legendre import leggauss

L = float(PARAMS.get("L", 2.0))                # konsol uzunligi, m
P = float(PARAMS.get("P", 5.0))*1e3            # uchdagi kuch, kN -> N
taper = float(PARAMS.get("taper", 0.6))        # EI(L)/EI(0)
b0 = float(PARAMS.get("b0", 80.0))*1e-3        # ildizdagi kengligi
h0 = float(PARAMS.get("h0", 160.0))*1e-3       # ildizdagi balandligi
E = 210e9

I0 = b0*h0**3/12.0
EI = lambda x: E*I0*(1.0 - (1.0 - taper)*x/L)   # chiziqli o'zgaruvchan
value("EI ildizda", E*I0, "N*m^2")
value("EI uchida", EI(L), "N*m^2")

# --- ETALON: birlik yuk usuli bilan aniq integral ----------------------
# w(L) = P * int_0^L (L-x)^2 / EI(x) dx  -- yuqori aniqlikdagi kvadratura
def ref(ng):
    gx, gw = leggauss(ng)
    x = L/2*(1 + gx)
    return P*float(np.sum((L - x)**2/EI(x)*gw)*L/2)
w_ref = ref(60)
value("Etalon w(L)", w_ref*1e3, "mm")
value("Etalon nazorati (40 vs 60 tugun)", abs(ref(40) - w_ref)/w_ref*100, "%")

# --- FEM: Ermit balka elementi (su-20) ---------------------------------
def fem(n):
    xs = np.linspace(0.0, L, n + 1)
    K = np.zeros((2*(n+1), 2*(n+1))); F = np.zeros(2*(n+1))
    gx, gw = leggauss(4)
    for e in range(n):
        x1, Le = xs[e], xs[e+1] - xs[e]
        idx = [2*e, 2*e+1, 2*e+2, 2*e+3]
        ke = np.zeros((4, 4))
        for xi, wq in zip(gx, gw):
            xx = x1 + Le/2*(1 + xi)
            # Ermit shakl funksiyalarining ikkinchi hosilasi
            d2N = np.array([1.5*xi, Le/8*(6*xi - 2),
                            -1.5*xi, Le/8*(6*xi + 2)])*(2/Le)**2
            ke += EI(xx)*np.outer(d2N, d2N)*wq*(Le/2)
        K[np.ix_(idx, idx)] += ke
    F[2*n] = P                                  # uchdagi ko'ndalang kuch
    free = np.arange(2, 2*(n+1))                # ildizda w = th = 0
    u = np.zeros(2*(n+1))
    u[free] = np.linalg.solve(K[np.ix_(free, free)], F[free])
    return u[2*n]

ns = [2, 4, 8, 16, 32]
ws = [fem(n) for n in ns]
errs = [abs(w - w_ref)/w_ref*100 for w in ws]
table("To'r bo'yicha yaqinlashish",
      ["elementlar", "w(L), mm", "xato, %"],
      [[n, f"{w*1e3:.6f}", f"{e:.3e}"] for n, w, e in zip(ns, ws, errs)])
series("Yaqinlashish", ns, errs, "elementlar", "xato, %")

# --- Kuzatilgan tartib va Richardson (su-28) ---------------------------
f1, f2, f3 = ws[-3], ws[-2], ws[-1]
p_obs = np.log(abs((f2 - f1)/(f3 - f2)))/np.log(2.0)
value("Kuzatilgan tartib p_obs", p_obs, "-")
w_rich = f3 + (f3 - f2)/(2**p_obs - 1)
value("Richardson ekstrapolyatsiyasi", w_rich*1e3, "mm")
value("Richardson xatosi etalonga", abs(w_rich - w_ref)/w_ref*100, "%")
gci = 1.25*abs((f3 - f2)/f3)/(2**p_obs - 1)*100
value("GCI (F_s = 1,25)", gci, "%")
value("Haqiqiy xato (eng mayda to'r)", errs[-1], "%")
value("GCI haqiqiy xatoni qopladimi", 1.0 if gci >= errs[-1] else 0.0, "1=ha")

# --- Resurs bahosi (su-29) ---------------------------------------------
for n in (32, 320, 3200):
    N = 2*(n + 1)
    value(f"n={n}: erkinlik darajasi", N, "-")
value("Lentali amallar (n=3200)", 2.0*2*3201*4**2, "amal")
note("Boshlang'ich kod zanjirning barcha bo'g'inlarini beradi: aniq "
     "etalon, FEM, yaqinlashish tartibi, Richardson va GCI. Loyihada "
     "uni o'z konstruksiyangizga ko'chiring: geometriya va yuklarni "
     "almashtiring, model farazlarini tekshiring va natijani "
     "xatolik chegarasi bilan keltiring.")''',
        evaluation=[
            "Modellashtirish qarori asoslangan, farazlar aniq (15%)",
            "Etalon mustaqil va o'zi tekshirilgan (15%)",
            "Sonli yechim to'g'ri, tanlovlar asoslangan (20%)",
            "p_obs o'lchangan va nazariy qiymat bilan izohlangan (20%)",
            "GCI qurilgan va farazlar validatsiyasi bajarilgan (20%)",
            "Resurs rejasi va hisobot sifati (10%)",
        ],
        parameters=[
            p("L", "Konsol uzunligi", 0.5, 6.0, 2.0, 0.1, "m"),
            p("P", "Uchdagi kuch", 0.5, 50.0, 5.0, 0.5, "kN"),
            p("taper", "Kesim toraytirish EI(L)/EI(0)", 0.2, 1.0, 0.6, 0.05, "-"),
            p("b0", "Ildizdagi kengligi", 30.0, 200.0, 80.0, 5.0, "mm"),
            p("h0", "Ildizdagi balandligi", 60.0, 400.0, 160.0, 10.0, "mm"),
        ],
    ),
]
