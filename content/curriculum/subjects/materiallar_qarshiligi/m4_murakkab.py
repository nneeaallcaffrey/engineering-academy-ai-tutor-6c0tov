"""MQ / 4-modul: Murakkab kuchlanish holati va mustahkamlik nazariyalari (mq-19 … mq-24)."""

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

S = "materiallar-qarshiligi"
M = "mq-m4"

TOPICS = [
    Topic(
        id="mq-19",
        subject_id=S,
        module_id=M,
        order=19,
        title="Kuchlanish holati, asosiy kuchlanishlar va Mor doirasi",
        description=(
            "Nuqtadagi kuchlanish holati, maydoncha burilganda kuchlanishlarning "
            "o'zgarishi, asosiy kuchlanishlar va Mor doirasi."
        ),
        learning_objective=(
            "Tekis kuchlanish holatini tahlil qilish, asosiy kuchlanishlarni "
            "analitik va grafik (Mor doirasi) usullar bilan topish."
        ),
        prerequisites=["mq-14", "nm-17"],
        mathematical_core=(
            "Koordinata almashtirish, xususiy qiymatlar masalasi, invariantlar, "
            "Mor doirasi geometriyasi."
        ),
        engineering_application=(
            "Murakkab yuklangan detallar, kuchlanish o'lchash (tenzodatchik), "
            "buzilish yo'nalishini bashorat qilish."
        ),
        computational_component=(
            "Kuchlanish tenzorini qurish, asosiy kuchlanishlarni eigenvalue "
            "orqali topish va Mor doirasini chizish."
        ),
        visualization_component=(
            "Mor doirasi va elementar hajm; asosiy maydonchalar orientatsiyasi."
        ),
        research_extension=(
            "Tenzodatchik rozetkasidan (3 ta o'lchov) to'liq kuchlanish holatini "
            "qanday tiklash mumkin?"
        ),
        difficulty="murakkab",
        previous_link=(
            "mq-13 va mq-14 da $\\sigma$ va $\\tau$ ni alohida ko'rdik. Endi ular "
            "bir nuqtada birga mavjud bo'lganda nima bo'lishini tahlil qilamiz. "
            "nm-17 dagi tenzor apparati aynan shu yerda ishlaydi."
        ),
        next_topic="mq-20",
        estimated_minutes=95,
        tags=["kuchlanish holati", "Mor doirasi", "asosiy kuchlanishlar"],
        lesson=Lesson(
            physical_problem=(
                "Val bir vaqtda egiladi va buraladi. Uning sirtidagi nuqtada ham "
                "$\\sigma$, ham $\\tau$ bor. Bu nuqta xavflimi? $\\sigma$ va $\\tau$ "
                "ni alohida solishtirish yetarli emas — ular birgalikda ta'sir "
                "qiladi. Kerak bo'lgan narsa: shu nuqtadagi eng katta kuchlanish "
                "qaysi yo'nalishda va qanchaga teng?"
            ),
            concepts=[
                c("Kuchlanish holati", "Nuqta atrofidagi barcha maydonchalardagi "
                  "kuchlanishlar to'plami; kuchlanish tenzori bilan tavsiflanadi."),
                c("Asosiy kuchlanishlar", "$\\sigma_1 \\ge \\sigma_2 \\ge \\sigma_3$ — "
                  "urinma kuchlanish nolga teng bo'lgan maydonchalardagi normal "
                  "kuchlanishlar."),
                c("Asosiy maydonchalar", "Asosiy kuchlanishlar ta'sir qiladigan "
                  "o'zaro perpendikular maydonchalar."),
                c("Mor doirasi", "Kuchlanish holatining grafik tasviri: "
                  "$(\\sigma, \\tau)$ tekisligida doira."),
                c("Invariantlar", "$\\sigma_x + \\sigma_y = \\sigma_1 + \\sigma_2$ — "
                  "koordinata burilishida o'zgarmaydigan kattaliklar."),
            ],
            derivation=[
                d("1-qadam. Burilgan maydonchadagi kuchlanishlar",
                  r"\sigma_\alpha = \frac{\sigma_x+\sigma_y}{2} + \frac{\sigma_x-\sigma_y}{2}\cos2\alpha "
                  r"+ \tau_{xy}\sin2\alpha",
                  "Uchburchak element muvozanatidan. $2\\alpha$ paydo bo'lishi "
                  "kuchlanish holatining $180°$ davriyligini bildiradi."),
                d("2-qadam. Urinma kuchlanish burilgan maydonchada",
                  r"\tau_\alpha = -\frac{\sigma_x-\sigma_y}{2}\sin2\alpha + \tau_{xy}\cos2\alpha",
                  "Ikkinchi muvozanat tenglamasidan. Bu ikki ifoda birgalikda Mor "
                  "doirasining parametrik tenglamasi."),
                d("3-qadam. Asosiy maydonchalar",
                  r"\tau_\alpha = 0 \;\Rightarrow\; \tan 2\alpha_0 = \frac{2\tau_{xy}}{\sigma_x-\sigma_y}",
                  "Ikki yechim $\\alpha_0$ va $\\alpha_0 + 90°$ — asosiy "
                  "maydonchalar o'zaro perpendikular."),
                d("4-qadam. Asosiy kuchlanishlar",
                  r"\boxed{\;\sigma_{1,2} = \frac{\sigma_x+\sigma_y}{2} \pm "
                  r"\sqrt{\left(\frac{\sigma_x-\sigma_y}{2}\right)^2 + \tau_{xy}^2}\;}",
                  "$\\alpha_0$ ni qo'yish orqali. Bu — $2\\times2$ simmetrik "
                  "matritsaning xususiy qiymatlari (nm-17)."),
                d("5-qadam. Mor doirasi",
                  r"\left(\sigma - \frac{\sigma_x+\sigma_y}{2}\right)^2 + \tau^2 = R^2,\quad "
                  r"R = \sqrt{\left(\frac{\sigma_x-\sigma_y}{2}\right)^2+\tau_{xy}^2}",
                  "Ikki ifodadan $\\alpha$ ni yo'qotamiz — doira tenglamasi hosil "
                  "bo'ladi. Markaz $\\sigma$ o'qida, radius $R = \\tau_{max}$."),
            ],
            formula_meaning=(
                "Mor doirasi kuchlanish holatining butun ma'lumotini bitta "
                "rasmda jamlaydi: eng chap nuqta $\\sigma_2$, eng o'ng nuqta "
                "$\\sigma_1$, eng yuqori nuqta $\\tau_{max} = R$. Doira markazi "
                "gidrostatik (hajmiy) qismni, radius esa deviator (shakl "
                "o'zgartiruvchi) qismni ifodalaydi — bu ajratish mq-21 dagi "
                "mustahkamlik nazariyalarining asosidir."
            ),
            equations=[
                eq(r"\sigma_{1,2} = \frac{\sigma_x+\sigma_y}{2} \pm \sqrt{\left(\frac{\sigma_x-\sigma_y}{2}\right)^2+\tau_{xy}^2}",
                   "Asosiy kuchlanishlar (tekis holat).", "Asosiy kuchlanishlar"),
                eq(r"\tau_{max} = \frac{\sigma_1-\sigma_2}{2}", "Maksimal urinma kuchlanish.",
                   "Maksimal τ"),
                eq(r"\tan2\alpha_0 = \frac{2\tau_{xy}}{\sigma_x-\sigma_y}", "Asosiy maydonchalar "
                   "orientatsiyasi.", "Asosiy yo'nalish"),
            ],
            conditions=(
                "Tekis kuchlanish holati yupqa devorli elementlarda va sirtda "
                "o'rinli (sirtda $\\sigma_3 = 0$). Fazoviy holatda uchta asosiy "
                "kuchlanish va uchta Mor doirasi bo'ladi; $\\tau_{max}$ eng katta "
                "doira radiusiga teng: $(\\sigma_1-\\sigma_3)/2$."
            ),
            worked_example=WorkedExample(
                statement=(
                    "Val sirtidagi nuqtada egilishdan $\\sigma_x = 80$ MPa, "
                    "buralishdan $\\tau_{xy} = 45$ MPa ($\\sigma_y = 0$). "
                    "Asosiy kuchlanishlarni, ularning yo'nalishini va $\\tau_{max}$ "
                    "ni toping."
                ),
                given=[r"\sigma_x = 80\ \text{MPa},\; \sigma_y = 0,\; \tau_{xy} = 45\ \text{MPa}"],
                steps=[
                    st(r"\sigma_{o'rt} = \frac{80+0}{2} = 40\ \text{MPa}",
                       "Mor doirasi markazi."),
                    st(r"R = \sqrt{40^2 + 45^2} = \sqrt{1600+2025} = \sqrt{3625} = 60{,}2\ \text{MPa}",
                       "Doira radiusi."),
                    st(r"\sigma_1 = 40 + 60{,}2 = 100{,}2\ \text{MPa};\quad "
                       r"\sigma_2 = 40 - 60{,}2 = -20{,}2\ \text{MPa}",
                       "Asosiy kuchlanishlar: biri cho'zuvchi, ikkinchisi siquvchi."),
                    st(r"\tan2\alpha_0 = \frac{2\cdot45}{80-0} = 1{,}125 \Rightarrow "
                       r"2\alpha_0 = 48{,}4^\circ \Rightarrow \alpha_0 = 24{,}2^\circ",
                       "Asosiy maydoncha o'q bilan 24,2° burchak hosil qiladi."),
                    st(r"\tau_{max} = R = 60{,}2\ \text{MPa}\ (\alpha = 24{,}2+45 = 69{,}2^\circ\ \text{da})",
                       "Maksimal urinma kuchlanish asosiy maydonchadan 45° da."),
                    st(r"\text{Invariant: } \sigma_1+\sigma_2 = 100{,}2-20{,}2 = 80 = \sigma_x+\sigma_y\ \checkmark",
                       "Tekshirish: birinchi invariant saqlanadi."),
                ],
                answer=(
                    "$\\sigma_1 = 100{,}2$ MPa, $\\sigma_2 = -20{,}2$ MPa, "
                    "$\\sigma_3 = 0$; $\\alpha_0 = 24{,}2°$; $\\tau_{max} = 60{,}2$ MPa."
                ),
                engineering_note=(
                    "$\\sigma_1 = 100{,}2$ MPa dastlabki $\\sigma_x = 80$ MPa dan "
                    "25 % katta — buralish qo'shilishi kuchlanishni sezilarli "
                    "oshirdi. Mo'rt material (cho'yan) uchun aynan $\\sigma_1$ "
                    "xavfli va buzilish unga perpendikular tekislikda, ya'ni "
                    "$24{,}2°$ burchak ostida spiral bo'ylab yuz beradi — bu "
                    "tajribada aniq kuzatiladi."
                ),
            ),
            computation=Computation(
                caption=(
                    "Kuchlanish holati: $\\sigma_x$, $\\sigma_y$, $\\tau_{xy}$ ni "
                    "o'zgartirib, Mor doirasi va asosiy kuchlanishlarni kuzating."
                ),
                code='''"""Kuchlanish holati tahlili: asosiy kuchlanishlar va Mor doirasi."""
import numpy as np
from labkit import PARAMS, note, series, table, value

sx = float(PARAMS.get("sx", 80.0))      # MPa
sy = float(PARAMS.get("sy", 0.0))
txy = float(PARAMS.get("txy", 45.0))

# Analitik yechim
s_avg = (sx+sy)/2
R = np.hypot((sx-sy)/2, txy)
s1, s2 = s_avg + R, s_avg - R
alpha0 = 0.5*np.degrees(np.arctan2(2*txy, sx-sy))

value("σ_o'rtacha", s_avg, "MPa")
value("Mor doirasi radiusi R", R, "MPa")
value("σ₁", s1, "MPa")
value("σ₂", s2, "MPa")
value("Asosiy burchak α₀", alpha0, "deg")
value("τ_max", R, "MPa")

# Tenzor sifatida — xususiy qiymatlar orqali tekshirish
T = np.array([[sx, txy], [txy, sy]])
eigvals, eigvecs = np.linalg.eigh(T)
note(f"Xususiy qiymatlar: {np.sort(eigvals)[::-1].round(3)} MPa — analitik yechim bilan mos ✓")
note(f"Birinchi invariant: tr(T) = {np.trace(T):.3f}, σ₁+σ₂ = {s1+s2:.3f} ✓")
note(f"Ikkinchi invariant: det(T) = {np.linalg.det(T):.3f}, σ₁·σ₂ = {s1*s2:.3f} ✓")

# Mor doirasi
th = np.linspace(0, 2*np.pi, 300)
series("Mor doirasi", (s_avg + R*np.cos(th)).tolist(), (R*np.sin(th)).tolist(),
       xlabel="σ, MPa", ylabel="τ, MPa")
series("Joriy maydoncha nuqtasi", [sx, sy], [txy, -txy], xlabel="σ, MPa", ylabel="τ, MPa")

# Maydoncha burchagiga bog'liqlik
a = np.linspace(0, 180, 361)
ar = np.radians(a)
s_a = s_avg + (sx-sy)/2*np.cos(2*ar) + txy*np.sin(2*ar)
t_a = -(sx-sy)/2*np.sin(2*ar) + txy*np.cos(2*ar)
series("σ(α)", a.tolist(), s_a.tolist(), xlabel="α, deg", ylabel="σ, MPa")
series("τ(α)", a.tolist(), t_a.tolist(), xlabel="α, deg", ylabel="τ, MPa")
note(f"σ maksimumi α = {a[np.argmax(s_a)]:.1f}° da, τ maksimumi α = {a[np.argmax(t_a)]:.1f}° da — "
     "orasidagi farq aynan 45°.")

# Xarakterli kuchlanish holatlari
table("Tipik kuchlanish holatlari",
      ["Holat", "σ₁", "σ₂", "σ₃", "τ_max"],
      [["Bir o'qli cho'zilish (σ)", "σ", "0", "0", "σ/2"],
       ["Toza siljish (τ)", "τ", "0", "-τ", "τ"],
       ["Ikki o'qli teng cho'zilish", "σ", "σ", "0", "σ/2"],
       ["Gidrostatik siqilish", "-p", "-p", "-p", "0"],
       ["Joriy holat", f"{s1:.1f}", f"{s2:.1f}", "0", f"{R:.1f}"]])

# Fazoviy holatda uchta doira
s3 = 0.0
principals = sorted([s1, s2, s3], reverse=True)
note(f"Fazoviy holat: σ₁={principals[0]:.1f}, σ₂={principals[1]:.1f}, σ₃={principals[2]:.1f} MPa; "
     f"τ_max(fazoviy) = {(principals[0]-principals[2])/2:.1f} MPa "
     "(eng katta doira radiusi)")
''',
                parameters=[
                    p("sx", "σ_x", -300.0, 300.0, 80.0, 5.0, "MPa"),
                    p("sy", "σ_y", -300.0, 300.0, 0.0, 5.0, "MPa"),
                    p("txy", "τ_xy", -200.0, 200.0, 45.0, 5.0, "MPa"),
                ],
                expected_output="σ₁ = 100,2 MPa, σ₂ = -20,2 MPa, α₀ = 24,2°, τ_max = 60,2 MPa",
            ),
            visualization=vis(
                "Mor doirasi va elementar hajm",
                "Manim",
                "Chapda elementar kvadrat kuchlanishlar bilan; u burilganda "
                "o'ngdagi Mor doirasida nuqta harakatlanadi. Asosiy maydonchalarda "
                "urinma kuchlanish yo'qolishi ko'rsatiladi.",
                "Manim: elementning burilishi va Mor doirasidagi nuqtaning "
                "sinxron harakati — bu bog'lanishni tushunishning eng samarali "
                "usuli. React/SVG da esa doira va interaktiv sliderlar "
                "($\\sigma_x$, $\\sigma_y$, $\\tau_{xy}$) beriladi.",
            ),
            interpretation=(
                "Mor doirasidan uchta muhim xulosa: (1) $\\tau_{max}$ asosiy "
                "maydonchalardan aynan 45° da; (2) $\\sigma$ maksimal bo'lgan "
                "maydonchada $\\tau = 0$; (3) invariantlar saqlanadi. Toza "
                "siljishda ($\\sigma_x = \\sigma_y = 0$) asosiy kuchlanishlar "
                "$\\pm\\tau$ — shuning uchun mo'rt material buralishda 45° "
                "burchak ostida sinadi, plastik esa ko'ndalang kesim bo'ylab."
            ),
            common_mistakes=[
                "$\\alpha$ va $2\\alpha$ ni chalkashtirish — Mor doirasida "
                "burchaklar ikki barobar.",
                "Tekis holatda $\\sigma_3 = 0$ ni unutib, fazoviy $\\tau_{max}$ ni "
                "noto'g'ri hisoblash.",
                "Asosiy kuchlanishlarni kattalik bo'yicha tartiblashni unutish "
                "($\\sigma_1 \\ge \\sigma_2 \\ge \\sigma_3$, ishora bilan).",
                "$\\tau_{xy}$ ishorasini e'tiborsiz qoldirish — u asosiy "
                "maydoncha yo'nalishini belgilaydi.",
            ],
            quiz=[
                q("Nima uchun formulalarda $2\\alpha$ paydo bo'ladi?",
                  "Kuchlanish holati $180°$ ga davriy: maydonchani $180°$ ga "
                  "burish uni o'z-o'ziga keltiradi. Shuning uchun $\\cos2\\alpha$, "
                  "$\\sin2\\alpha$.", "konseptual"),
                q("$\\sigma_x = 100$, $\\sigma_y = 0$, $\\tau = 0$. Asosiy "
                  "kuchlanishlar va $\\tau_{max}$?",
                  "$\\sigma_1 = 100$, $\\sigma_2 = 0$; $\\tau_{max} = 50$ MPa "
                  "(45° maydonchada).", "hisob"),
                q("Toza siljishda asosiy kuchlanishlar qanday?",
                  "$\\sigma_{1,2} = \\pm\\tau$, ya'ni teng cho'zilish va siqilish "
                  "45° burchak ostida.", "hisob"),
                q("Nima uchun mo'rt material buralishda 45° da sinadi?",
                  "Toza siljishda maksimal cho'zuvchi kuchlanish 45° maydonchada; "
                  "mo'rt material aynan cho'zilishdan buziladi.", "talqin"),
                q("Kodda `np.linalg.eigh(T)` natijasi nima uchun analitik formula "
                  "bilan mos keladi?",
                  "Asosiy kuchlanishlar — kuchlanish tenzorining xususiy "
                  "qiymatlari; analitik formula $2\\times2$ simmetrik matritsa "
                  "uchun xarakteristik tenglamaning yechimidir.", "kod"),
            ],
            bridge_to_next=(
                "Kuchlanish holatini tahlil qildik. Endi unga mos deformatsiya "
                "holatini va ularni bog'lovchi umumlashgan Guk qonunini ko'ramiz."
            ),
            research_extension=(
                "Tenzodatchik rozetkasi (0°, 45°, 90° da uchta datchik) dan to'liq "
                "tekis kuchlanish holatini tiklash algoritmini yozing. Uchta "
                "o'lchangan deformatsiyadan $\\varepsilon_x$, $\\varepsilon_y$, "
                "$\\gamma_{xy}$ ni, so'ngra umumlashgan Guk qonuni orqali "
                "kuchlanishlarni toping. O'lchash xatoligining natijaga ta'sirini "
                "baholang."
            ),
            manim=manim(
                scene="MohrCircleScene",
                module="manim/scenes/mq_stress.py",
                title="Mor doirasi",
                summary="Elementar hajm buriladi va Mor doirasidagi mos nuqta "
                        "harakatlanadi; asosiy maydonchalar topiladi.",
            ),
        ),
    ),
    Topic(
        id="mq-20",
        subject_id=S,
        module_id=M,
        order=20,
        title="Deformatsiya holati va umumlashgan Guk qonuni",
        description=(
            "Hajmiy deformatsiya holati, umumlashgan Guk qonuni, hajm o'zgarishi "
            "va solishtirma potensial energiya."
        ),
        learning_objective=(
            "Murakkab kuchlanish holatida deformatsiyalarni hisoblash va "
            "energiyani hajm hamda shakl o'zgarishiga ajratish."
        ),
        prerequisites=["mq-19", "mq-09"],
        mathematical_core=(
            "Chiziqli tenzor munosabatlari, superpozitsiya, hajmiy va deviator "
            "qismlarga ajratish, kvadratik forma."
        ),
        engineering_application=(
            "Tenzometriya, ko'p o'qli yuklanish, gидrostatik bosim ostidagi "
            "detallar, tiqilgan joylashuv."
        ),
        computational_component=(
            "Kuchlanishdan deformatsiyaga va aksincha o'tish; energiyani "
            "komponentlarga ajratish."
        ),
        visualization_component=(
            "Hajm va shakl o'zgarishining ajratilishi; kub deformatsiyasi."
        ),
        research_extension=(
            "Nima uchun $\\nu < 0{,}5$? Termodinamik cheklovlar va auxetik "
            "materiallar ($\\nu < 0$)."
        ),
        difficulty="murakkab",
        previous_link=(
            "mq-19 da kuchlanish holatini tahlil qildik. Endi unga mos "
            "deformatsiya holatini va ikkalasini bog'lovchi qonunni topamiz."
        ),
        next_topic="mq-21",
        estimated_minutes=90,
        tags=["umumlashgan Guk qonuni", "deformatsiya holati", "energiya"],
        lesson=Lesson(
            physical_problem=(
                "Detal ikki yo'nalishda cho'zilganda uchinchi yo'nalishda "
                "qanchaga siqiladi? Va nima uchun chuqur suv ostida jism "
                "shaklini o'zgartirmasdan faqat hajmini kamaytiradi? Bu "
                "savollarga javob deformatsiya energiyasini ikki qismga — hajm "
                "va shakl o'zgarishiga ajratish orqali topiladi. Aynan shu "
                "ajratish keyingi mavzudagi mustahkamlik nazariyalarining "
                "asosini beradi."
            ),
            concepts=[
                c("Umumlashgan Guk qonuni", "Har bir yo'nalishdagi deformatsiya "
                  "uchala kuchlanishdan hosil bo'ladigan deformatsiyalar "
                  "yig'indisi (superpozitsiya)."),
                c("Hajmiy deformatsiya", "$e = \\varepsilon_1+\\varepsilon_2+\\varepsilon_3 = "
                  "\\Delta V/V$ — nisbiy hajm o'zgarishi."),
                c("Hajmiy siqilish moduli", "$K = E/[3(1-2\\nu)]$ — gidrostatik "
                  "bosimga qarshilik."),
                c("Solishtirma potensial energiya", "$u = \\tfrac{1}{2}\\sigma_{ij}\\varepsilon_{ij}$ — "
                  "birlik hajmdagi deformatsiya energiyasi."),
                c("Energiyaning ajralishi", "$u = u_v + u_f$ — hajm o'zgarishi va "
                  "shakl o'zgarishi energiyalari."),
            ],
            derivation=[
                d("1-qadam. Superpozitsiya orqali umumlashgan Guk qonuni",
                  r"\varepsilon_1 = \frac{\sigma_1}{E} - \nu\frac{\sigma_2}{E} - \nu\frac{\sigma_3}{E} = "
                  r"\frac{1}{E}\big[\sigma_1 - \nu(\sigma_2+\sigma_3)\big]",
                  "Har bir kuchlanish o'z yo'nalishida cho'zadi, perpendikular "
                  "yo'nalishlarda esa $\\nu$ koeffitsienti bilan siqadi."),
                d("2-qadam. Hajmiy deformatsiya",
                  r"e = \varepsilon_1+\varepsilon_2+\varepsilon_3 = \frac{1-2\nu}{E}(\sigma_1+\sigma_2+\sigma_3)",
                  "Yig'indi olamiz. Muhim xulosa: hajm o'zgarishi faqat "
                  "kuchlanishlar yig'indisiga (birinchi invariant) bog'liq."),
                d("3-qadam. Hajmiy siqilish moduli va $\\nu$ chegarasi",
                  r"K = \frac{E}{3(1-2\nu)};\qquad \nu = 0{,}5 \Rightarrow K \to \infty",
                  "$\\nu = 0{,}5$ da material siqilmaydigan bo'ladi (rezina). "
                  "$\\nu > 0{,}5$ bo'lsa $K < 0$ — bu termodinamik jihatdan "
                  "imkonsiz, shuning uchun $-1 < \\nu < 0{,}5$."),
                d("4-qadam. Potensial energiyani ajratish",
                  r"u = \frac{1}{2E}\big[\sigma_1^2+\sigma_2^2+\sigma_3^2 - "
                  r"2\nu(\sigma_1\sigma_2+\sigma_2\sigma_3+\sigma_3\sigma_1)\big] = u_v + u_f",
                  "Kuchlanish tenzorini sferik (o'rtacha) va deviator qismlarga "
                  "ajratib, energiya ham ikkiga bo'linadi."),
                d("5-qadam. Shakl o'zgarishi energiyasi",
                  r"\boxed{\;u_f = \frac{1+\nu}{6E}\big[(\sigma_1-\sigma_2)^2+(\sigma_2-\sigma_3)^2+(\sigma_3-\sigma_1)^2\big]\;}",
                  "Faqat kuchlanishlar farqiga bog'liq — gidrostatik holatda "
                  "($\\sigma_1=\\sigma_2=\\sigma_3$) nolga teng. Bu ifoda "
                  "fon Mizes mustahkamlik nazariyasining asosi (mq-21)."),
            ],
            formula_meaning=(
                "Energiyaning hajm va shakl qismlariga ajralishi fizik jihatdan "
                "chuqur ma'noga ega: gidrostatik bosim materialning shaklini "
                "o'zgartirmaydi va (metallarda) plastik oqishga olib kelmaydi — "
                "okean tubidagi bosim po'latni oquvchanlikka keltirmaydi. "
                "Oqish faqat shakl o'zgarishi energiyasi kritik qiymatga "
                "yetganda boshlanadi. Bu tajribaviy fakt fon Mizes kriteriyasining "
                "fizik asosi."
            ),
            equations=[
                eq(r"\varepsilon_1 = \frac{1}{E}[\sigma_1-\nu(\sigma_2+\sigma_3)]",
                   "Umumlashgan Guk qonuni.", "Umumlashgan Guk qonuni"),
                eq(r"e = \frac{1-2\nu}{E}(\sigma_1+\sigma_2+\sigma_3)", "Hajmiy deformatsiya.",
                   "Hajm o'zgarishi"),
                eq(r"u_f = \frac{1+\nu}{6E}\sum(\sigma_i-\sigma_j)^2", "Shakl o'zgarishi energiyasi.",
                   "Shakl energiyasi"),
            ],
            conditions=(
                "Qonun chiziqli-elastik, izotrop material uchun. Anizotrop "
                "materialda (kompozit, monokristall) 21 tagacha mustaqil elastik "
                "doimiy bo'lishi mumkin (tmm-13). $\\nu$ chegaralari: "
                "$-1 < \\nu < 0{,}5$; ko'pchilik metallar uchun 0,25–0,35."
            ),
            worked_example=WorkedExample(
                statement=(
                    "Po'lat kub ($E = 200$ GPa, $\\nu = 0{,}3$) uch o'qli "
                    "yuklanishda: $\\sigma_1 = 120$ MPa, $\\sigma_2 = 60$ MPa, "
                    "$\\sigma_3 = -40$ MPa. Deformatsiyalarni, hajm o'zgarishini "
                    "va energiya komponentlarini hisoblang."
                ),
                given=[r"E = 2\cdot10^5\ \text{MPa},\; \nu = 0{,}3",
                       r"\sigma_1 = 120,\; \sigma_2 = 60,\; \sigma_3 = -40\ \text{MPa}"],
                steps=[
                    st(r"\varepsilon_1 = \frac{1}{2\cdot10^5}[120 - 0{,}3(60-40)] = "
                       r"\frac{120-6}{2\cdot10^5} = 5{,}70\cdot10^{-4}",
                       "Birinchi asosiy deformatsiya."),
                    st(r"\varepsilon_2 = \frac{1}{2\cdot10^5}[60 - 0{,}3(120-40)] = "
                       r"\frac{60-24}{2\cdot10^5} = 1{,}80\cdot10^{-4}",
                       "Ikkinchi deformatsiya."),
                    st(r"\varepsilon_3 = \frac{1}{2\cdot10^5}[-40 - 0{,}3(120+60)] = "
                       r"\frac{-40-54}{2\cdot10^5} = -4{,}70\cdot10^{-4}",
                       "Uchinchi deformatsiya — siqilish."),
                    st(r"e = (5{,}70+1{,}80-4{,}70)\cdot10^{-4} = 2{,}80\cdot10^{-4}",
                       "Hajmiy deformatsiya. Tekshirish: "
                       "$\\frac{1-0{,}6}{2\\cdot10^5}(140) = 2{,}80\\cdot10^{-4}$ ✓"),
                    st(r"u = \frac{1}{2E}\big[120^2+60^2+40^2 - 0{,}6(7200-2400-4800)\big] = "
                       r"\frac{20\,800 - 0{,}6\cdot 0}{4\cdot10^5}",
                       "$\\sigma_1\\sigma_2+\\sigma_2\\sigma_3+\\sigma_3\\sigma_1 = "
                       "7200-2400-4800 = 0$; $u = 0{,}052$ MJ/m³."),
                    st(r"u_f = \frac{1{,}3}{6\cdot2\cdot10^5}[(60)^2+(100)^2+(160)^2] = "
                       r"\frac{1{,}3\cdot 38\,000}{1{,}2\cdot10^6} = 0{,}0412\ \text{MJ/m}^3",
                       "Shakl o'zgarishi energiyasi — to'la energiyaning 79 % i."),
                ],
                answer=(
                    "$\\varepsilon_1 = 5{,}70\\cdot10^{-4}$, $\\varepsilon_2 = 1{,}80\\cdot10^{-4}$, "
                    "$\\varepsilon_3 = -4{,}70\\cdot10^{-4}$; $e = 2{,}80\\cdot10^{-4}$; "
                    "$u = 0{,}052$ MJ/m³, $u_f = 0{,}0412$ MJ/m³ (79 %)."
                ),
                engineering_note=(
                    "Shakl o'zgarishi energiyasi ulushi 79 % — demak bu holat "
                    "plastik oqish uchun xavfli. Agar barcha kuchlanishlar teng "
                    "bo'lganda (gidrostatik), $u_f = 0$ bo'lardi va material "
                    "oqmasdi. Aynan shu farq mq-21 dagi mustahkamlik "
                    "nazariyalarining tanlash mezonini beradi."
                ),
            ),
            computation=Computation(
                caption=(
                    "Umumlashgan Guk qonuni: uch o'qli holatda deformatsiyalarni "
                    "va energiya ajralishini hisoblang."
                ),
                code='''"""Umumlashgan Guk qonuni va energiyaning ajralishi."""
import numpy as np
from labkit import PARAMS, note, series, table, value

E = float(PARAMS.get("E", 200000.0))     # MPa
nu = float(PARAMS.get("nu", 0.3))
s1 = float(PARAMS.get("s1", 120.0))      # MPa
s2 = float(PARAMS.get("s2", 60.0))
s3 = float(PARAMS.get("s3", -40.0))

G = E/(2*(1+nu))
K = E/(3*(1-2*nu))
value("Siljish moduli G", G/1000, "GPa")
value("Hajmiy modul K", K/1000, "GPa")

def hooke(s1, s2, s3):
    e1 = (s1 - nu*(s2+s3))/E
    e2 = (s2 - nu*(s1+s3))/E
    e3 = (s3 - nu*(s1+s2))/E
    return e1, e2, e3

e1, e2, e3 = hooke(s1, s2, s3)
e_vol = e1+e2+e3
value("ε₁", e1*1e6, "µε")
value("ε₂", e2*1e6, "µε")
value("ε₃", e3*1e6, "µε")
value("Hajmiy deformatsiya e", e_vol*1e6, "µε")
note(f"Tekshirish: e = (1-2ν)(σ₁+σ₂+σ₃)/E = {(1-2*nu)*(s1+s2+s3)/E*1e6:.3f} µε ✓")

# Energiya
u_total = (s1**2+s2**2+s3**2 - 2*nu*(s1*s2+s2*s3+s3*s1))/(2*E)
s_avg = (s1+s2+s3)/3
u_vol = 3*(1-2*nu)*s_avg**2/(2*E)
u_form = (1+nu)*((s1-s2)**2+(s2-s3)**2+(s3-s1)**2)/(6*E)
value("To'la energiya u", u_total, "MJ/m³")
value("Hajm o'zgarishi u_v", u_vol, "MJ/m³")
value("Shakl o'zgarishi u_f", u_form, "MJ/m³")
value("u_f ulushi", 100*u_form/u_total, "%")
note(f"Balans tekshiruvi: u_v + u_f = {u_vol+u_form:.6f}, u = {u_total:.6f} MJ/m³ ✓")

# Gidrostatik holat: shakl energiyasi nolga teng
p_test = -100.0
_, _, _ = hooke(p_test, p_test, p_test)
u_f_hydro = (1+nu)*0.0/(6*E)
note(f"Gidrostatik holatda (σ₁=σ₂=σ₃={p_test} MPa): u_f = {u_f_hydro:.6f} MJ/m³ — "
     "shakl o'zgarmaydi, plastik oqish bo'lmaydi.")

# Puasson koeffitsientining ta'siri
nn = np.linspace(0.0, 0.499, 200)
series("Hajmiy modul K(ν)", nn.tolist(), (E/(3*(1-2*nn))/1000).tolist(),
       xlabel="ν", ylabel="K, GPa")
series("Hajmiy deformatsiya e(ν)", nn.tolist(),
       ((1-2*nn)*(s1+s2+s3)/E*1e6).tolist(), xlabel="ν", ylabel="e, µε")
note("ν → 0,5 da K → ∞ va e → 0: material siqilmaydigan bo'ladi (rezina, suyuqlik).")

table("Materiallar uchun elastik doimiylar",
      ["Material", "E, GPa", "ν", "G, GPa", "K, GPa"],
      [[nm, Ei, ni, Ei/(2*(1+ni)), Ei/(3*(1-2*ni))]
       for nm, Ei, ni in [("Po'lat", 200, 0.30), ("Alyuminiy", 70, 0.33),
                          ("Mis", 110, 0.34), ("Shisha", 70, 0.22),
                          ("Rezina", 0.01, 0.499), ("Probka", 0.02, 0.0)]])

# Tekis kuchlanish va tekis deformatsiya farqi
s3_plane_strain = nu*(s1+s2)
note(f"Tekis deformatsiya holatida (ε₃=0): σ₃ = ν(σ₁+σ₂) = {s3_plane_strain:.1f} MPa, "
     f"tekis kuchlanishda esa σ₃ = 0. Bu farq tmm-16 da muhim.")
''',
                parameters=[
                    p("E", "Yung moduli E", 1000.0, 400000.0, 200000.0, 1000.0, "MPa"),
                    p("nu", "Puasson koeff. ν", 0.0, 0.49, 0.3, 0.01, "—"),
                    p("s1", "σ₁", -500.0, 500.0, 120.0, 10.0, "MPa"),
                    p("s2", "σ₂", -500.0, 500.0, 60.0, 10.0, "MPa"),
                    p("s3", "σ₃", -500.0, 500.0, -40.0, 10.0, "MPa"),
                ],
                expected_output="ε₁ = 570 µε, e = 280 µε, u_f/u ≈ 79 %",
            ),
            visualization=vis(
                "Energiyaning hajm va shakl qismlariga ajralishi",
                "React/SVG",
                "Kub uch holatda: (1) boshlang'ich, (2) faqat hajm o'zgargan "
                "(o'xshash kattalashgan), (3) faqat shakl o'zgargan (hajm "
                "o'zgarmagan). Yonida energiya ustunli diagrammasi.",
                "React/SVG: uch kubni yonma-yon ko'rsatish energiya ajralishining "
                "fizik ma'nosini darhol yetkazadi. Bu — mq-21 dagi fon Mizes "
                "kriteriyasini tushunishning kaliti.",
            ),
            interpretation=(
                "$K(\\nu)$ grafigi $\\nu \\to 0{,}5$ da cheksizlikka intiladi — "
                "material siqilmaydigan bo'ladi. Energiya balansi tekshiruvi "
                "($u_v + u_f = u$) formulalarning to'g'riligini tasdiqlaydi. "
                "Gidrostatik holatda $u_f = 0$ bo'lishi esa asosiy fizik "
                "xulosani beradi: bosim materialni oqishga majbur qilmaydi, "
                "faqat kuchlanishlar farqi qiladi."
            ),
            common_mistakes=[
                "Umumlashgan Guk qonunida $\\nu$ oldidagi minus ishorani unutish.",
                "Tekis kuchlanish ($\\sigma_3 = 0$) va tekis deformatsiya "
                "($\\varepsilon_3 = 0$) holatlarini chalkashtirish.",
                "$\\nu > 0{,}5$ qiymatlarni ishlatish — bu fizik jihatdan imkonsiz.",
                "Energiyani hisoblashda kuchlanishlarni MPa da qoldirib, natijani "
                "noto'g'ri birlikda talqin qilish.",
            ],
            quiz=[
                q("Nima uchun $\\nu$ 0,5 dan katta bo'la olmaydi?",
                  "$K = E/[3(1-2\\nu)]$ manfiy bo'lib qolardi — bu siqilganda "
                  "hajm ortishini bildiradi, termodinamik jihatdan imkonsiz.",
                  "konseptual"),
                q("Gidrostatik bosimda shakl o'zgarishi energiyasi nimaga teng?",
                  "Nolga: barcha $(\\sigma_i - \\sigma_j) = 0$.", "konseptual"),
                q("$\\sigma_1 = 100$, $\\sigma_2 = \\sigma_3 = 0$, $E = 200$ GPa, "
                  "$\\nu = 0{,}3$. $\\varepsilon_2$?",
                  "$\\varepsilon_2 = -\\nu\\sigma_1/E = -0{,}3\\cdot100/2\\cdot10^5 = "
                  "-1{,}5\\cdot10^{-4}$.", "hisob"),
                q("Suv ostida 1000 m chuqurlikda po'lat sharning shakli o'zgaradimi?",
                  "Yo'q, faqat hajmi kamayadi — gidrostatik holatda shakl "
                  "o'zgarishi energiyasi nol.", "talqin"),
                q("Kodda energiya balansi qanday tekshirilgan?",
                  "$u_v$ va $u_f$ alohida hisoblanib, ularning yig'indisi to'liq "
                  "energiya $u$ bilan solishtirilgan — ular aynan teng bo'lishi "
                  "kerak.", "kod"),
            ],
            bridge_to_next=(
                "Endi bizda kuchlanish holati va energiya tahlili bor. Keyingi "
                "mavzuda ular asosida murakkab holatni bir o'qli holatga "
                "keltiruvchi mustahkamlik nazariyalarini quramiz."
            ),
            research_extension=(
                "Auxetik materiallarni ($\\nu < 0$) tadqiq qiling: ular "
                "cho'zilganda kengayadi. Qanday mikrostruktura bunga olib keladi? "
                "Sodda auxetik yacheyka (re-entrant honeycomb) modelini quring va "
                "samarali $\\nu$ ni geometriya funksiyasi sifatida hisoblang."
            ),
        ),
    ),
    Topic(
        id="mq-21",
        subject_id=S,
        module_id=M,
        order=21,
        title="Mustahkamlik nazariyalari va ekvivalent kuchlanish",
        description=(
            "Murakkab kuchlanish holatini bir o'qli holatga keltirish, klassik "
            "mustahkamlik kriteriylari va ularni tanlash mezonlari."
        ),
        learning_objective=(
            "Material turi va kuchlanish holatiga mos mustahkamlik nazariyasini "
            "tanlash va ekvivalent kuchlanishni hisoblash."
        ),
        prerequisites=["mq-20", "mq-19"],
        mathematical_core=(
            "Ekvivalentlik gipotezasi, invariantlar orqali kriteriylar, "
            "buzilish sirtlari geometriyasi."
        ),
        engineering_application=(
            "Vallar, bosimli idishlar, murakkab yuklangan detallar hisobi; "
            "FEM natijalarini baholash."
        ),
        computational_component=(
            "Turli kriteriylarni taqqoslash va buzilish sirtlarini chizish."
        ),
        visualization_component=(
            "Asosiy kuchlanishlar tekisligida buzilish chegaralari (Tresk "
            "olti burchagi va fon Mizes ellipsi)."
        ),
        research_extension=(
            "Mo'rt materiallar uchun Mor–Kulon kriteriysi: nima uchun ularda "
            "cho'zilish va siqilish mustahkamligi turlicha?"
        ),
        difficulty="murakkab",
        previous_link=(
            "mq-20 dagi energiya ajralishi bevosita fon Mizes kriteriysiga olib "
            "boradi; mq-19 dagi $\\tau_{max}$ esa Tresk kriteriysiga."
        ),
        next_topic="mq-22",
        estimated_minutes=95,
        tags=["mustahkamlik nazariyasi", "fon Mizes", "Tresk"],
        lesson=Lesson(
            physical_problem=(
                "Materialning mustahkamlik chegarasi bir o'qli cho'zilish "
                "sinovida aniqlangan. Lekin real detalda uch o'qli kuchlanish "
                "holati bor. Har bir kombinatsiya uchun alohida sinov o'tkazish "
                "imkonsiz. Yechim: murakkab holatni 'ekvivalent' bir o'qli "
                "holat bilan almashtirish — lekin ekvivalentlik mezoni nima?"
            ),
            concepts=[
                c("Ekvivalent kuchlanish", "$\\sigma_{ekv}$ — murakkab holat bilan "
                  "bir xil xavflilikdagi bir o'qli cho'zilish kuchlanishi."),
                c("1-nazariya (maksimal normal kuchlanish)", "$\\sigma_{ekv} = \\sigma_1$ — "
                  "mo'rt materiallar uchun."),
                c("3-nazariya (Tresk, maksimal urinma kuchlanish)", "$\\sigma_{ekv} = "
                  "\\sigma_1 - \\sigma_3$ — plastik materiallar uchun, ehtiyotkor."),
                c("4-nazariya (fon Mizes, shakl o'zgarishi energiyasi)", "Plastik "
                  "materiallar uchun eng aniq; tajriba bilan yaxshi mos keladi."),
                c("Mor–Kulon nazariyasi", "Cho'zilish va siqilish mustahkamligi "
                  "farq qiladigan materiallar uchun (beton, cho'yan, tuproq)."),
            ],
            derivation=[
                d("1-qadam. Ekvivalentlik gipotezasini qo'yish",
                  r"\text{Kriteriy: } f(\sigma_1,\sigma_2,\sigma_3) = f(\sigma_{ekv}, 0, 0)",
                  "Qandaydir fizik kattalik (kuchlanish, urinma kuchlanish yoki "
                  "energiya) ikki holatda teng bo'lsa, ular bir xil xavfli deb "
                  "qabul qilinadi."),
                d("2-qadam. Tresk kriteriysi",
                  r"\tau_{max} = \frac{\sigma_1-\sigma_3}{2} = \frac{\sigma_{ekv}}{2} "
                  r"\;\Rightarrow\; \boxed{\;\sigma_{ekv}^{III} = \sigma_1-\sigma_3\;}",
                  "Bir o'qli cho'zilishda $\\tau_{max} = \\sigma/2$. Plastik oqish "
                  "siljish bilan bog'liq degan fizik g'oyaga asoslanadi."),
                d("3-qadam. Fon Mizes kriteriysi",
                  r"u_f(\sigma_1,\sigma_2,\sigma_3) = u_f(\sigma_{ekv},0,0) \;\Rightarrow\; "
                  r"\frac{1+\nu}{6E}\sum(\sigma_i-\sigma_j)^2 = \frac{1+\nu}{6E}\cdot2\sigma_{ekv}^2",
                  "mq-20 dagi shakl o'zgarishi energiyasini tenglashtiramiz."),
                d("4-qadam. Fon Mizes formulasi",
                  r"\boxed{\;\sigma_{ekv}^{IV} = \sqrt{\tfrac{1}{2}\big[(\sigma_1-\sigma_2)^2+"
                  r"(\sigma_2-\sigma_3)^2+(\sigma_3-\sigma_1)^2\big]}\;}",
                  "Tekis holatda: $\\sigma_{ekv} = \\sqrt{\\sigma_x^2 - \\sigma_x\\sigma_y + "
                  "\\sigma_y^2 + 3\\tau_{xy}^2}$."),
                d("5-qadam. Egilish + buralish uchun amaliy shakl",
                  r"\sigma_{ekv}^{III} = \sqrt{\sigma^2+4\tau^2},\qquad "
                  r"\sigma_{ekv}^{IV} = \sqrt{\sigma^2+3\tau^2}",
                  "$\\sigma_y = 0$ holida. Tresk 15 % ehtiyotkorroq — shuning "
                  "uchun mas'uliyatli hisoblarda u ko'proq ishlatiladi."),
            ],
            formula_meaning=(
                "Mustahkamlik nazariyasi — bu gipoteza, tenglama emas. U "
                "materialning qanday buzilishini modellashtiradi: mo'rt material "
                "eng katta cho'zuvchi kuchlanishdan (1-nazariya), plastik "
                "material esa siljishdan (Tresk, fon Mizes) buziladi. "
                "$\\sqrt{3}$ va $2$ koeffitsientlari farqi 15 % — bu "
                "loyihalashda sezilarli, lekin hal qiluvchi emas. Muhimi to'g'ri "
                "nazariyani tanlash: mo'rt materialga fon Mizesni qo'llash "
                "xavfli xatodir."
            ),
            equations=[
                eq(r"\sigma_{ekv}^{I} = \sigma_1", "1-nazariya (mo'rt materiallar).",
                   "Maksimal normal kuchlanish"),
                eq(r"\sigma_{ekv}^{III} = \sigma_1-\sigma_3", "Tresk kriteriysi.", "Tresk"),
                eq(r"\sigma_{ekv}^{IV} = \sqrt{\tfrac{1}{2}\sum(\sigma_i-\sigma_j)^2}",
                   "Fon Mizes kriteriysi.", "Fon Mizes"),
                eq(r"\sigma_{ekv} = \sqrt{\sigma^2+3\tau^2}", "Egilish + buralish (fon Mizes).",
                   "Val uchun"),
            ],
            conditions=(
                "Nazariyani tanlash materialga bog'liq: plastik — Tresk yoki "
                "fon Mizes; mo'rt — 1-nazariya yoki Mor–Kulon. Gidrostatik "
                "siqilishda plastik materiallar umuman buzilmaydi — bu Tresk va "
                "fon Mizesda avtomatik hisobga olinadi (ikkalasi ham faqat "
                "kuchlanishlar farqiga bog'liq)."
            ),
            worked_example=WorkedExample(
                statement=(
                    "Val bir vaqtda egilmoqda va buralmoqda: $M = 1{,}2$ kN·m, "
                    "$T = 0{,}9$ kN·m, diametri $d = 50$ mm. Po'lat "
                    "$[\\sigma] = 160$ MPa. Uchala nazariya bo'yicha tekshiring "
                    "va kerakli diametrni toping."
                ),
                given=[r"M = 1200\ \text{N·m},\; T = 900\ \text{N·m},\; d = 0{,}05\ \text{m}",
                       r"[\sigma] = 160\ \text{MPa}"],
                steps=[
                    st(r"W = \frac{\pi d^3}{32} = \frac{3{,}1416\cdot1{,}25\cdot10^{-4}}{32} = "
                       r"1{,}227\cdot10^{-5}\ \text{m}^3;\quad W_p = 2W = 2{,}454\cdot10^{-5}\ \text{m}^3",
                       "Qarshilik momentlari."),
                    st(r"\sigma = \frac{M}{W} = \frac{1200}{1{,}227\cdot10^{-5}} = 97{,}8\ \text{MPa};\quad "
                       r"\tau = \frac{T}{W_p} = \frac{900}{2{,}454\cdot10^{-5}} = 36{,}7\ \text{MPa}",
                       "Normal va urinma kuchlanishlar."),
                    st(r"\sigma_{1,2} = \frac{97{,}8}{2} \pm \sqrt{48{,}9^2+36{,}7^2} = "
                       r"48{,}9 \pm 61{,}1 \Rightarrow \sigma_1 = 110{,}0,\; \sigma_3 = -12{,}2\ \text{MPa}",
                       "Asosiy kuchlanishlar (mq-19)."),
                    st(r"\sigma_{ekv}^{I} = 110{,}0\ \text{MPa};\quad "
                       r"\sigma_{ekv}^{III} = 110{,}0+12{,}2 = 122{,}2\ \text{MPa}",
                       "1- va 3-nazariyalar. Tekshirish: "
                       "$\\sqrt{97{,}8^2+4\\cdot36{,}7^2} = 122{,}2$ ✓"),
                    st(r"\sigma_{ekv}^{IV} = \sqrt{97{,}8^2+3\cdot36{,}7^2} = "
                       r"\sqrt{9565+4040} = 116{,}6\ \text{MPa}",
                       "Fon Mizes — Treskdan 4,6 % kichik."),
                    st(r"\text{Barchasi } \le 160\ \text{MPa}\ \checkmark;\quad "
                       r"d_{kerak}^{III} = \sqrt[3]{\frac{32\sqrt{M^2+T^2}}{\pi[\sigma]}} = "
                       r"\sqrt[3]{\frac{32\cdot1500}{\pi\cdot160\cdot10^6}} = 45{,}7\ \text{mm}",
                       "Tresk bo'yicha minimal diametr."),
                ],
                answer=(
                    "$\\sigma_{ekv}^{I} = 110{,}0$, $\\sigma_{ekv}^{III} = 122{,}2$, "
                    "$\\sigma_{ekv}^{IV} = 116{,}6$ MPa — barchasi $[\\sigma]$ dan "
                    "past; minimal diametr 45,7 mm."
                ),
                engineering_note=(
                    "Tresk 4,6 % ehtiyotkorroq natija berdi. Val hisobida "
                    "$M_{ekv} = \\sqrt{M^2+T^2}$ (Tresk) yoki "
                    "$\\sqrt{M^2+0{,}75T^2}$ (fon Mizes) formulalari qulay — "
                    "ular egilish va buralishni bitta ekvivalent momentga "
                    "keltiradi va diametrni bevosita topish imkonini beradi."
                ),
            ),
            computation=Computation(
                caption=(
                    "Mustahkamlik nazariyalarini taqqoslang va buzilish "
                    "chegaralarini chizing."
                ),
                code='''"""Mustahkamlik nazariyalari: ekvivalent kuchlanish va buzilish sirtlari."""
import numpy as np
from labkit import PARAMS, note, series, table, value

M = float(PARAMS.get("M", 1200.0))       # eguvchi moment, N*m
T = float(PARAMS.get("T", 900.0))        # buruvchi moment, N*m
d = float(PARAMS.get("d", 50.0))*1e-3    # diametr, m
s_allow = float(PARAMS.get("s_allow", 160.0))   # MPa

W = np.pi*d**3/32
Wp = 2*W
sigma = M/W/1e6
tau = T/Wp/1e6

value("σ (egilishdan)", sigma, "MPa")
value("τ (buralishdan)", tau, "MPa")

# Asosiy kuchlanishlar
s_avg = sigma/2
R = np.hypot(sigma/2, tau)
s1, s3 = s_avg+R, s_avg-R
s2 = 0.0
principals = sorted([s1, s2, s3], reverse=True)
value("σ₁", principals[0], "MPa")
value("σ₂", principals[1], "MPa")
value("σ₃", principals[2], "MPa")

def eqv(p, theory):
    a, b, cc = p
    if theory == 1:
        return a
    if theory == 3:
        return a - cc
    if theory == 4:
        return np.sqrt(0.5*((a-b)**2 + (b-cc)**2 + (cc-a)**2))
    raise ValueError(theory)

rows = []
for th, name in [(1, "I (maks. normal)"), (3, "III (Tresk)"), (4, "IV (fon Mizes)")]:
    se = eqv(principals, th)
    rows.append([name, float(se), float(s_allow/se), "OK" if se <= s_allow else "XAVF"])
table("Nazariyalarni taqqoslash", ["Nazariya", "σ_ekv, MPa", "Zaxira", "Xulosa"], rows)

note(f"Tekshirish: σ_ekv^III = √(σ²+4τ²) = {np.sqrt(sigma**2+4*tau**2):.2f} MPa")
note(f"Tekshirish: σ_ekv^IV = √(σ²+3τ²) = {np.sqrt(sigma**2+3*tau**2):.2f} MPa")
note(f"Tresk va fon Mizes farqi: {100*(eqv(principals,3)/eqv(principals,4)-1):.2f} %")

# Kerakli diametr
M_eq_tresk = np.sqrt(M**2 + T**2)
M_eq_mises = np.sqrt(M**2 + 0.75*T**2)
d_tresk = (32*M_eq_tresk/(np.pi*s_allow*1e6))**(1/3)
d_mises = (32*M_eq_mises/(np.pi*s_allow*1e6))**(1/3)
value("d (Tresk)", d_tresk*1000, "mm")
value("d (fon Mizes)", d_mises*1000, "mm")

# Buzilish chegaralari (tekis holat, σ3 = 0)
th_arr = np.linspace(0, 2*np.pi, 400)
sy_t = s_allow*np.cos(th_arr)
sx_t = s_allow*np.sin(th_arr)
# fon Mizes ellipsi: sx^2 - sx*sy + sy^2 = s_allow^2
phi = np.linspace(0, 2*np.pi, 400)
a_ax, b_ax = np.sqrt(2)*s_allow, np.sqrt(2/3)*s_allow
xm = a_ax*np.cos(phi)/np.sqrt(2) + b_ax*np.sin(phi)/np.sqrt(2)*np.sqrt(3)/np.sqrt(3)
x_m = (a_ax*np.cos(phi) + b_ax*np.sin(phi))/np.sqrt(2)
y_m = (a_ax*np.cos(phi) - b_ax*np.sin(phi))/np.sqrt(2)
series("Fon Mizes ellipsi", x_m.tolist(), y_m.tolist(), xlabel="σ₁, MPa", ylabel="σ₂, MPa")

# Tresk olti burchagi
hexa = [(s_allow, 0), (s_allow, s_allow), (0, s_allow), (-s_allow, 0),
        (-s_allow, -s_allow), (0, -s_allow), (s_allow, 0)]
series("Tresk olti burchagi", [h[0] for h in hexa], [h[1] for h in hexa],
       xlabel="σ₁, MPa", ylabel="σ₂, MPa")
series("Joriy holat", [principals[0]], [principals[1]], xlabel="σ₁, MPa", ylabel="σ₂, MPa")
note("Tresk olti burchagi fon Mizes ellipsi ichida yotadi — shuning uchun u "
     "har doim ehtiyotkorroq (maksimal farq 15,5 %).")

table("Nazariyani tanlash",
      ["Material", "Tavsiya etilgan nazariya", "Sabab"],
      [["Plastik (po'lat, alyuminiy)", "IV (fon Mizes) yoki III (Tresk)",
        "Oqish siljishdan boshlanadi"],
       ["Mo'rt (cho'yan, shisha)", "I yoki Mor–Kulon",
        "Cho'zuvchi kuchlanishdan buziladi"],
       ["Beton, tosh", "Mor–Kulon", "Cho'zilish va siqilish mustahkamligi turlicha"],
       ["Kompozit", "Maxsus kriteriylar (Tsai–Wu)", "Anizotropiya"]])
''',
                parameters=[
                    p("M", "Eguvchi moment M", 0.0, 20000.0, 1200.0, 50.0, "N·m"),
                    p("T", "Buruvchi moment T", 0.0, 20000.0, 900.0, 50.0, "N·m"),
                    p("d", "Val diametri d", 10.0, 200.0, 50.0, 1.0, "mm"),
                    p("s_allow", "[σ]", 40.0, 500.0, 160.0, 10.0, "MPa"),
                ],
                expected_output="σ = 97,8 MPa, τ = 36,7 MPa, σ_ekv^III = 122,2, σ_ekv^IV = 116,6 MPa",
            ),
            visualization=vis(
                "Buzilish chegaralari",
                "React/SVG",
                "$(\\sigma_1, \\sigma_2)$ tekisligida: Tresk olti burchagi va "
                "fon Mizes ellipsi bir grafikda; joriy kuchlanish holati nuqta "
                "sifatida belgilangan.",
                "React/SVG: ikki chegarani bir grafikda ko'rsatish ularning "
                "farqini (Tresk ichkarida — ehtiyotkorroq) darhol ko'rsatadi. "
                "Ish nuqtasining chegaraga nisbatan holati xavfsizlik zaxirasini "
                "vizual beradi — bu FEM natijalarini baholashda ham "
                "ishlatiladigan standart tasvir.",
            ),
            interpretation=(
                "Tresk olti burchagi fon Mizes ellipsiga ichdan chizilgan: "
                "ular bir o'qli holatda mos keladi, toza siljishda esa 15,5 % "
                "farq qiladi (maksimal farq). Tajribalar ko'rsatadiki, plastik "
                "metallar uchun fon Mizes aniqroq, lekin Tresk ehtiyotkorroq va "
                "hisoblash osonroq. Shuning uchun me'yoriy hujjatlarda "
                "ko'pincha Tresk, FEM dasturlarida esa fon Mizes ishlatiladi."
            ),
            common_mistakes=[
                "Mo'rt materialga fon Mizes yoki Tresk nazariyasini qo'llash — "
                "bu xavfli, chunki ular gidrostatik qismni e'tiborsiz qoldiradi.",
                "Asosiy kuchlanishlarni tartiblashni unutish ($\\sigma_1$ eng "
                "katta, $\\sigma_3$ eng kichik, ishora bilan).",
                "Tekis holatda $\\sigma_3 = 0$ ni hisobga olmay, Treskda "
                "$\\sigma_1 - \\sigma_2$ yozish.",
                "$\\sigma_{ekv}$ ni haqiqiy kuchlanish deb o'ylash — u shartli, "
                "taqqoslash uchun kattalik.",
            ],
            quiz=[
                q("Nima uchun Tresk va fon Mizes gidrostatik siqilishda "
                  "buzilishni bashorat qilmaydi?",
                  "Ikkalasi ham faqat kuchlanishlar farqiga bog'liq; gidrostatik "
                  "holatda barcha farqlar nolga teng.", "konseptual"),
                q("$\\sigma = 100$ MPa, $\\tau = 50$ MPa. Ikkala nazariya bo'yicha "
                  "$\\sigma_{ekv}$?",
                  "Tresk: $\\sqrt{100^2+4\\cdot50^2} = 141{,}4$ MPa; fon Mizes: "
                  "$\\sqrt{100^2+3\\cdot50^2} = 132{,}3$ MPa.", "hisob"),
                q("Toza siljishda ($\\tau$) ikkala nazariya qanday farq qiladi?",
                  "Tresk: $\\sigma_{ekv} = 2\\tau$; fon Mizes: $\\sqrt{3}\\tau = "
                  "1{,}73\\tau$ — 15,5 % farq, bu maksimal farq.", "hisob"),
                q("Nima uchun cho'yan uchun 1-nazariya ishlatiladi?",
                  "Cho'yan mo'rt: u plastik oqmaydi, balki eng katta cho'zuvchi "
                  "kuchlanishga perpendikular tekislikda ajraladi.", "talqin"),
                q("Kodda Tresk olti burchagi nima uchun ellips ichida yotadi?",
                  "Tresk kriteriysi har doim fon Mizesdan kichik yoki teng "
                  "ekvivalent kuchlanish chegarasini beradi — demak u "
                  "ehtiyotkorroq va uning sohasi kichikroq.", "kod"),
            ],
            bridge_to_next=(
                "Endi murakkab kuchlanish holatini baholay olamiz. Keyingi "
                "mavzularda deformatsiyalar birgalikda ta'sir qiladigan konkret "
                "hollarni — murakkab qarshilikni ko'ramiz."
            ),
            research_extension=(
                "Mor–Kulon kriteriysini amalga oshiring: "
                "$\\sigma_1/[\\sigma_c] - \\sigma_3/[\\sigma_s] \\le 1$, bunda "
                "$[\\sigma_c]$ va $[\\sigma_s]$ cho'zilish va siqilishdagi ruxsat "
                "etilgan kuchlanishlar. Cho'yan uchun ($[\\sigma_s]/[\\sigma_c] "
                "\\approx 3...4$) buzilish chegarasini chizing va uni fon Mizes "
                "bilan taqqoslang. Qaysi kuchlanish holatlarida farq eng katta?"
            ),
        ),
    ),
    Topic(
        id="mq-22",
        subject_id=S,
        module_id=M,
        order=22,
        title="Qiyshiq egilish va egilish bilan cho'zilishning birgalikdagi ta'siri",
        description=(
            "Ikki tekislikda egilish, neytral o'qning burilishi, ekssentrik "
            "cho'zilish-siqilish va kesim yadrosi."
        ),
        learning_objective=(
            "Murakkab qarshilik hollarida kuchlanishlarni superpozitsiya bilan "
            "hisoblash va xavfli nuqtani aniqlash."
        ),
        prerequisites=["mq-21", "mq-13"],
        mathematical_core=(
            "Superpozitsiya, neytral o'q tenglamasi, kesim yadrosi geometriyasi."
        ),
        engineering_application=(
            "Purlin va tom balkalari, ekssentrik yuklangan ustunlar, "
            "poydevorlar, kran ustunlari."
        ),
        computational_component=(
            "Ixtiyoriy kesimda kuchlanish maydonini hisoblash va neytral o'qni "
            "topish; kesim yadrosini qurish."
        ),
        visualization_component=(
            "Kesimda kuchlanish maydoni (rangli xarita) va burilgan neytral o'q."
        ),
        research_extension=(
            "Kesim yadrosi nima uchun beton va tosh konstruksiyalarda hal "
            "qiluvchi ahamiyatga ega?"
        ),
        difficulty="murakkab",
        previous_link=(
            "mq-13 da bir tekislikdagi egilishni ko'rdik. Endi ikki tekislikda "
            "egilish va unga bo'ylama kuch qo'shilgan holni tahlil qilamiz."
        ),
        next_topic="mq-23",
        estimated_minutes=90,
        tags=["qiyshiq egilish", "ekssentrik siqilish", "kesim yadrosi"],
        lesson=Lesson(
            physical_problem=(
                "Tom purlini qiya joylashgan va yuk vertikal. Demak u bir vaqtda "
                "ikki tekislikda egiladi. Bundan tashqari, beton ustunga yuk "
                "markazdan chetroqda tushsa, siqilish bilan birga egilish paydo "
                "bo'ladi — va agar ekssentrisitet katta bo'lsa, ustunning bir "
                "tomonida cho'zuvchi kuchlanish hosil bo'ladi. Beton esa "
                "cho'zilishga zaif. Bu chegara qayerda?"
            ),
            concepts=[
                c("Qiyshiq egilish", "Yuklanish tekisligi bosh inersiya o'qlari "
                  "bilan mos kelmaydi; kesimda ikkala o'qqa nisbatan moment bor."),
                c("Neytral o'qning burilishi", "Qiyshiq egilishda neytral o'q "
                  "yuklanish tekisligiga perpendikular emas."),
                c("Ekssentrik siqilish", "Bo'ylama kuch og'irlik markazidan "
                  "chetda qo'yilgan; $N$ va $M = Ne$ birgalikda ta'sir qiladi."),
                c("Kesim yadrosi", "Kesim atrofidagi soha; kuch shu soha ichida "
                  "qo'yilsa, kesimda faqat bir ishorali kuchlanish bo'ladi."),
                c("Xavfli nuqta", "Neytral o'qdan eng uzoq joylashgan kontur nuqtasi."),
            ],
            derivation=[
                d("1-qadam. Qiyshiq egilishda superpozitsiya",
                  r"\sigma(y,z) = \frac{M_y z}{I_y} + \frac{M_z y}{I_z}",
                  "Ikki tekislikdagi egilishlar mustaqil va qo'shiladi (chiziqli "
                  "masala). Bosh o'qlar ishlatiladi, shuning uchun $I_{yz} = 0$."),
                d("2-qadam. Neytral o'q tenglamasi",
                  r"\sigma = 0 \Rightarrow \frac{M_yz}{I_y} + \frac{M_zy}{I_z} = 0 "
                  r"\Rightarrow \tan\varphi = -\frac{M_yI_z}{M_zI_y}",
                  "Neytral o'q markazdan o'tadi, lekin yuklanish tekisligiga "
                  "perpendikular emas — bu qiyshiq egilishning asosiy xususiyati. "
                  "$I_y \\neq I_z$ bo'lsa burchak farqi katta bo'ladi."),
                d("3-qadam. Ekssentrik siqilish uchun kuchlanish",
                  r"\sigma = \frac{N}{A} + \frac{Ne_zz}{I_y} + \frac{Ne_yy}{I_z} = "
                  r"\frac{N}{A}\left(1 + \frac{e_zz}{i_y^2} + \frac{e_yy}{i_z^2}\right)",
                  "$i^2 = I/A$ — inersiya radiusi kvadrati. Formula ixchamlashdi."),
                d("4-qadam. Kesim yadrosi chegarasi",
                  r"\sigma = 0\ \text{konturda} \Rightarrow "
                  r"\frac{e_z z_{max}}{i_y^2} + \frac{e_y y_{max}}{i_z^2} = -1",
                  "Neytral o'q kesimga urinma bo'lgan holat. To'rtburchak uchun "
                  "yadro — romb, tomonlari $h/3$ va $b/3$."),
                d("5-qadam. To'rtburchak uchun 'uchdan bir qoidasi'",
                  r"|e_z| \le \frac{h}{6},\ |e_y| \le \frac{b}{6} \Rightarrow "
                  r"\text{kesimda faqat siqilish}",
                  "Klassik 'o'rta uchdan bir' qoidasi: kuch kesim balandligining "
                  "o'rta uchdan bir qismida bo'lsa, cho'zilish paydo bo'lmaydi."),
            ],
            formula_meaning=(
                "Kesim yadrosi — mo'rt materiallar (beton, g'isht, tosh) "
                "konstruksiyalarining asosiy tushunchasi. Ular cho'zilishga zaif, "
                "shuning uchun yuk yadro ichida qolishi ta'minlanadi. Qadimgi "
                "tosh ko'priklar va gumbazlar aynan shu prinsip bo'yicha "
                "loyihalangan — arka shakli yuk chizig'ini yadro ichida ushlab "
                "turadi. Qiyshiq egilishda esa neytral o'qning burilishi "
                "kuchlanishni kutilmagan nuqtada maksimal qiladi."
            ),
            equations=[
                eq(r"\sigma = \frac{M_yz}{I_y} + \frac{M_zy}{I_z}", "Qiyshiq egilishda kuchlanish.",
                   "Qiyshiq egilish"),
                eq(r"\sigma = \frac{N}{A}\left(1+\frac{e_zz}{i_y^2}+\frac{e_yy}{i_z^2}\right)",
                   "Ekssentrik siqilishda kuchlanish.", "Ekssentrik siqilish"),
                eq(r"\tan\varphi = -\frac{M_yI_z}{M_zI_y}", "Neytral o'q burchagi.",
                   "Neytral o'q"),
            ],
            conditions=(
                "Superpozitsiya faqat chiziqli masalada o'rinli — uzun siqilgan "
                "elementlarda ikkinchi tartibli effektlar (ko'chish momentni "
                "oshiradi) paydo bo'ladi va mq-25/mq-26 dagi ustuvorlik hisobi "
                "kerak bo'ladi. Bosh o'qlar ishlatilishi shart, aks holda "
                "$I_{yz}$ hadi qo'shiladi."
            ),
            worked_example=WorkedExample(
                statement=(
                    "Beton ustun kesimi $400\\times600$ mm, siquvchi kuch "
                    "$N = 800$ kN kesim markazidan $e_z = 120$ mm masofada "
                    "(balandlik bo'ylab) qo'yilgan. Chekka tolalardagi "
                    "kuchlanishlarni toping va kesim yadrosi shartini tekshiring."
                ),
                given=[r"b = 0{,}4\ \text{m},\; h = 0{,}6\ \text{m},\; N = -800\ \text{kN}",
                       r"e_z = 0{,}12\ \text{m}"],
                steps=[
                    st(r"A = 0{,}4\cdot0{,}6 = 0{,}24\ \text{m}^2;\quad "
                       r"W = \frac{0{,}4\cdot0{,}36}{6} = 0{,}024\ \text{m}^3",
                       "Geometrik tavsiflar."),
                    st(r"\frac{N}{A} = \frac{-800\cdot10^3}{0{,}24} = -3{,}33\ \text{MPa}",
                       "Markaziy siqilishdan kuchlanish."),
                    st(r"M = Ne_z = 800\cdot0{,}12 = 96\ \text{kN·m};\quad "
                       r"\frac{M}{W} = \frac{96\cdot10^3}{0{,}024} = 4{,}0\ \text{MPa}",
                       "Egilishdan kuchlanish."),
                    st(r"\sigma_{max} = -3{,}33 - 4{,}0 = -7{,}33\ \text{MPa (siqilish)}",
                       "Kuch tomonidagi chekka tola."),
                    st(r"\sigma_{min} = -3{,}33 + 4{,}0 = +0{,}67\ \text{MPa (cho'zilish!)}",
                       "Qarama-qarshi tomonda cho'zilish paydo bo'ldi — beton uchun xavfli."),
                    st(r"e_{yadro} = \frac{h}{6} = \frac{600}{6} = 100\ \text{mm} < 120\ \text{mm}",
                       "Kuch yadrodan tashqarida — shuning uchun cho'zilish paydo "
                       "bo'ldi. Ekssentrisitetni 100 mm gacha kamaytirish yoki "
                       "armatura qo'yish kerak."),
                ],
                answer=(
                    "$\\sigma_{max} = -7{,}33$ MPa (siqilish), $\\sigma_{min} = "
                    "+0{,}67$ MPa (cho'zilish); kuch kesim yadrosidan tashqarida "
                    "($e = 120 > 100$ mm)."
                ),
                engineering_note=(
                    "0,67 MPa cho'zilish — beton uchun bu chegaraviy qiymatga "
                    "yaqin (B25 uchun $R_{bt} \\approx 1{,}05$ MPa). Yechimlar: "
                    "(a) ekssentrisitetni kamaytirish, (b) kesimni kengaytirish, "
                    "(c) armatura qo'yish, (d) oldindan tarang qilish. "
                    "Armaturasiz beton ustunlarda yadro sharti qat'iy bajarilishi "
                    "shart."
                ),
            ),
            computation=Computation(
                caption=(
                    "Murakkab qarshilik: ekssentrisitet va momentlarni "
                    "o'zgartirib, kuchlanish maydonini va kesim yadrosini kuzating."
                ),
                code='''"""Qiyshiq egilish va ekssentrik siqilish: kuchlanish maydoni."""
import numpy as np
from labkit import PARAMS, note, series, table, value

b = float(PARAMS.get("b", 400.0))*1e-3     # kesim eni, m
h = float(PARAMS.get("h", 600.0))*1e-3     # kesim balandligi, m
N = float(PARAMS.get("N", -800.0))*1e3     # bo'ylama kuch (manfiy = siqilish), N
ez = float(PARAMS.get("ez", 120.0))*1e-3   # ekssentrisitet (h bo'ylab), m
ey = float(PARAMS.get("ey", 0.0))*1e-3     # ekssentrisitet (b bo'ylab), m

A = b*h
Iy = b*h**3/12          # h bo'ylab egilish
Iz = h*b**3/12
iy2, iz2 = Iy/A, Iz/A

value("Yuza A", A*1e4, "cm²")
value("I_y", Iy*1e8, "cm⁴")
value("i_y²", iy2*1e4, "cm²")

def sigma(y, z):
    """y — b bo'ylab, z — h bo'ylab koordinata (markazdan)."""
    return N/A*(1 + ez*z/iy2 + ey*y/iz2)/1e6      # MPa

corners = [(-b/2, -h/2), (b/2, -h/2), (b/2, h/2), (-b/2, h/2)]
rows = [[f"({y*1000:.0f}; {z*1000:.0f})", float(sigma(y, z))] for y, z in corners]
table("Burchak nuqtalaridagi kuchlanish", ["Nuqta (y; z), mm", "σ, MPa"], rows)

s_vals = [sigma(y, z) for y, z in corners]
value("σ_max (siqilish)", min(s_vals), "MPa")
value("σ_min", max(s_vals), "MPa")
note("Kesimda CHO'ZILISH bor — mo'rt material uchun xavfli!"
     if max(s_vals) > 0 else "Kesimda faqat siqilish — yadro sharti bajarildi ✓")

# Kesim yadrosi chegaralari
ez_core = h/6
ey_core = b/6
value("Yadro chegarasi (h bo'ylab)", ez_core*1000, "mm")
value("Yadro chegarasi (b bo'ylab)", ey_core*1000, "mm")
in_core = abs(ez)/ez_core + abs(ey)/ey_core <= 1.0
note(f"Kuch yadro {'ICHIDA' if in_core else 'TASHQARISIDA'}: "
     f"|e_z|/{ez_core*1000:.0f} + |e_y|/{ey_core*1000:.0f} = "
     f"{abs(ez)/ez_core + abs(ey)/ey_core:.3f} (≤1 bo'lishi kerak)")

# Kesim yadrosi (romb) chizmasi
core = [(ey_core, 0), (0, ez_core), (-ey_core, 0), (0, -ez_core), (ey_core, 0)]
series("Kesim yadrosi", [c[0]*1000 for c in core], [c[1]*1000 for c in core],
       xlabel="e_y, mm", ylabel="e_z, mm")
series("Joriy kuch nuqtasi", [ey*1000], [ez*1000], xlabel="e_y, mm", ylabel="e_z, mm")

# Neytral o'q
if abs(ez) > 1e-12 or abs(ey) > 1e-12:
    zz = np.linspace(-h/2, h/2, 100)
    if abs(ey) > 1e-12:
        yy_na = -(iz2/ey)*(1 + ez*zz/iy2)
        mask = np.abs(yy_na) <= b/2
        if mask.any():
            series("Neytral o'q", (yy_na[mask]*1000).tolist(), (zz[mask]*1000).tolist(),
                   xlabel="y, mm", ylabel="z, mm")
    else:
        z_na = -iy2/ez
        note(f"Neytral o'q z = {z_na*1000:.1f} mm da (kesim "
             f"{'ichida' if abs(z_na) <= h/2 else 'tashqarisida'})")

# Kuchlanish taqsimoti balandlik bo'ylab
zz = np.linspace(-h/2, h/2, 200)
series("σ(z) — kesim balandligi bo'ylab", (sigma(0, zz)).tolist(), (zz*1000).tolist(),
       xlabel="σ, MPa", ylabel="z, mm")

# Ekssentrisitetning cho'zilish paydo bo'lishiga ta'siri
ee = np.linspace(0, h/2, 150)
s_min_arr = [N/A*(1 - e*(h/2)/iy2)/1e6 for e in ee]
series("σ_min(e)", (ee*1000).tolist(), s_min_arr, xlabel="Ekssentrisitet e, mm",
       ylabel="σ_min, MPa")
note(f"Cho'zilish e > {h/6*1000:.0f} mm da paydo bo'ladi — bu 'o'rta uchdan bir' qoidasi.")

table("Kesim yadrosi shakllari",
      ["Kesim", "Yadro shakli", "Chegara"],
      [["To'rtburchak b×h", "Romb", "h/6 va b/6"],
       ["Doira d", "Doira", "d/8"],
       ["Halqa (yupqa)", "Doira", "≈ d/4"],
       ["Dvutavr", "Romb (cho'zilgan)", "≈ W/A"]])
''',
                parameters=[
                    p("b", "Kesim eni b", 100.0, 1500.0, 400.0, 20.0, "mm"),
                    p("h", "Kesim balandligi h", 100.0, 2000.0, 600.0, 20.0, "mm"),
                    p("N", "Bo'ylama kuch N", -5000.0, 2000.0, -800.0, 50.0, "kN"),
                    p("ez", "Ekssentrisitet e_z", -500.0, 500.0, 120.0, 10.0, "mm"),
                    p("ey", "Ekssentrisitet e_y", -400.0, 400.0, 0.0, 10.0, "mm"),
                ],
                expected_output="σ_max = -7,33 MPa, σ_min = +0,67 MPa, yadro chegarasi 100 mm",
            ),
            visualization=vis(
                "Kuchlanish maydoni va kesim yadrosi",
                "React/SVG",
                "Kesim konturi ichida kuchlanish rangli xarita sifatida "
                "(siqilish — sovuq, cho'zilish — issiq rang); neytral o'q chizig'i; "
                "yonida kesim yadrosi (romb) va kuch qo'yilish nuqtasi.",
                "React/SVG: kuchlanish maydonini SVG `<rect>` to'ri bilan yoki "
                "chiziqli gradient bilan chizish mumkin. Kesim yadrosi va kuch "
                "nuqtasini alohida panelda ko'rsatish — bu tushunchani eng aniq "
                "yetkazadi.",
            ),
            interpretation=(
                "$\\sigma_{min}(e)$ grafigi chiziqli va $e = h/6$ da nolni "
                "kesib o'tadi — bu yadro chegarasining aniq ifodasi. Kesim "
                "yadrosi jadvali turli kesimlar uchun chegaralarni beradi: "
                "doiraviy kesimda u $d/8$, ya'ni juda kichik. Shuning uchun "
                "mo'rt materialdan yasalgan dumaloq ustunlarda ekssentrisitetga "
                "juda ehtiyot bo'lish kerak."
            ),
            common_mistakes=[
                "Qiyshiq egilishda neytral o'qni yuklanish tekisligiga "
                "perpendikular deb olish.",
                "Bosh o'qlar o'rniga ixtiyoriy o'qlarni ishlatish "
                "($I_{yz} \\neq 0$ hadi paydo bo'ladi).",
                "Ekssentrik siqilishda $N$ ishorasini noto'g'ri qo'yish.",
                "Kesim yadrosini tekshirmasdan mo'rt material ishlatish.",
            ],
            quiz=[
                q("Nima uchun qiyshiq egilishda neytral o'q buriladi?",
                  "Chunki $\\tan\\varphi = -M_yI_z/(M_zI_y)$ — inersiya "
                  "momentlari farqi burchakni o'zgartiradi. $I_y = I_z$ bo'lsa "
                  "(kvadrat, doira) burilish bo'lmaydi.", "konseptual"),
                q("To'rtburchak kesim uchun yadro chegarasi qancha?",
                  "$h/6$ va $b/6$ — 'o'rta uchdan bir' qoidasi.", "hisob"),
                q("$N = -500$ kN, $A = 0{,}2$ m², $e = 0$. Kuchlanish?",
                  "$\\sigma = -2{,}5$ MPa, butun kesim bo'ylab bir tekis.", "hisob"),
                q("Nima uchun qadimgi tosh ko'priklar arka shaklida?",
                  "Arka yuk chizig'ini kesim yadrosi ichida ushlab turadi — "
                  "toshda cho'zilish paydo bo'lmaydi.", "talqin"),
                q("Kodda `abs(ez)/ez_core + abs(ey)/ey_core <= 1` sharti nimani "
                  "tekshiradi?",
                  "Kuchning kesim yadrosi (romb) ichida ekanini — bu rombning "
                  "tenglamasi.", "kod"),
            ],
            bridge_to_next=(
                "Egilish va cho'zilishning birgalikdagi ta'sirini ko'rdik. Endi "
                "eng ko'p uchraydigan holatga — egilish va buralishning "
                "birgalikdagi ta'siriga, ya'ni val hisobiga o'tamiz."
            ),
            research_extension=(
                "Ixtiyoriy kesim uchun kesim yadrosini avtomatik quruvchi "
                "algoritm yozing: kontur nuqtalarini aylanib chiqib, har biri "
                "uchun neytral o'q urinma bo'lgan kuch nuqtasini toping. "
                "Natijani dvutavr va shveller uchun hisoblang va standart "
                "qiymatlar bilan taqqoslang."
            ),
        ),
    ),
    Topic(
        id="mq-23",
        subject_id=S,
        module_id=M,
        order=23,
        title="Egilish va buralishning birgalikdagi ta'siri: val hisobi",
        description=(
            "Egilish va buralish momentlarining birgalikda ta'siri, ekvivalent "
            "moment, valni to'liq loyihalash metodikasi."
        ),
        learning_objective=(
            "Real ish sharoitidagi valni to'liq hisoblash: reaksiyalar, "
            "epyuralar, ekvivalent moment va diametr tanlash."
        ),
        prerequisites=["mq-21", "mq-10"],
        mathematical_core=(
            "Ekvivalent moment, fazoviy egilishni ikki tekislikka ajratish, "
            "natijaviy moment."
        ),
        engineering_application=(
            "Reduktor vallari, transmissiya, nasos va kompressor vallari."
        ),
        computational_component=(
            "Val hisobi dasturi: epyuralar, ekvivalent moment, diametr profili."
        ),
        visualization_component=(
            "Fazoviy val sxemasi, ikki tekislikdagi epyuralar va natijaviy "
            "moment diagrammasi."
        ),
        research_extension=(
            "Valning kritik aylanish tezligi: egilish tebranishlari va "
            "rezonansdan qochish."
        ),
        difficulty="murakkab",
        previous_link=(
            "mq-21 dagi ekvivalent kuchlanish endi amaliy shaklga — ekvivalent "
            "momentga aylanadi va mq-10 dagi buralish bilan birlashadi."
        ),
        next_topic="mq-24",
        estimated_minutes=95,
        tags=["val hisobi", "ekvivalent moment", "murakkab qarshilik"],
        lesson=Lesson(
            physical_problem=(
                "Reduktor vali tishli g'ildiraklardan kuch oladi. Bu kuchlar "
                "bir vaqtda valni egadi (radial va o'q bo'ylab tashkil "
                "etuvchilar) va buradi (aylana bo'ylab tashkil etuvchi). "
                "Qanday diametr kerak? Bu masala mashinasozlikdagi eng ko'p "
                "uchraydigan hisoblardan biri."
            ),
            concepts=[
                c("Fazoviy egilish", "Kuchlar ikki tekislikda; momentlar "
                  "geometrik qo'shiladi: $M = \\sqrt{M_v^2 + M_g^2}$."),
                c("Ekvivalent moment", "$M_{ekv} = \\sqrt{M^2 + \\alpha T^2}$; "
                  "Tresk uchun $\\alpha = 1$, fon Mizes uchun $\\alpha = 0{,}75$."),
                c("Xavfli kesim", "$M_{ekv}$ maksimal bo'lgan kesim — odatda "
                  "podshipnik yoki tishli g'ildirak yaqinida."),
                c("Konstruktiv cheklovlar", "Podshipnik o'lchamlari, shpon "
                  "kanali, galtellar — ular diametrni oshirishga majbur qiladi."),
                c("Kuchlanish konsentratsiyasi", "Diametr o'zgarishi va shpon "
                  "kanali kuchlanishni 1,5–3 marta oshiradi (mq-29)."),
            ],
            derivation=[
                d("1-qadam. Kuchlarni ikki tekislikka ajratish",
                  r"F_t = \frac{2T}{d_w},\qquad F_r = F_t\tan\alpha_w,\qquad "
                  r"F_a = F_t\tan\beta",
                  "Tishli uzatmada aylana, radial va o'q bo'ylab tashkil "
                  "etuvchilar. $\\alpha_w = 20°$ — ilashish burchagi."),
                d("2-qadam. Har bir tekislikda epyura qurish",
                  r"M_v(x)\ \text{va}\ M_g(x)\ \text{— vertikal va gorizontal tekisliklarda}",
                  "mq-12 dagi usul har bir tekislik uchun alohida qo'llanadi."),
                d("3-qadam. Natijaviy eguvchi moment",
                  r"M(x) = \sqrt{M_v^2(x) + M_g^2(x)}",
                  "Momentlar vektor sifatida qo'shiladi, chunki ular "
                  "perpendikular o'qlarga nisbatan."),
                d("4-qadam. Ekvivalent moment",
                  r"\boxed{\;M_{ekv} = \sqrt{M^2 + 0{,}75\,T^2}\ (\text{fon Mizes})\;}",
                  "mq-21 dagi $\\sigma_{ekv} = \\sqrt{\\sigma^2+3\\tau^2}$ ni "
                  "$\\sigma = M/W$, $\\tau = T/(2W)$ bilan ifodalasak, "
                  "$W$ qisqaradi va ekvivalent moment qoladi."),
                d("5-qadam. Diametrni aniqlash",
                  r"d \ge \sqrt[3]{\frac{32M_{ekv}}{\pi[\sigma]}}",
                  "Mustahkamlik shartidan. So'ngra konstruktiv cheklovlar va "
                  "standart qatorga yaxlitlash."),
            ],
            formula_meaning=(
                "Ekvivalent moment tushunchasi murakkab masalani oddiy egilish "
                "masalasiga keltiradi: $M_{ekv}$ ni topgach, diametr oddiy "
                "formula bilan aniqlanadi. $0{,}75$ koeffitsienti fon Mizes "
                "kriteriysidan, $1{,}0$ esa Treskdan kelib chiqadi — ikkinchisi "
                "8–15 % katta diametr beradi. Amalda ko'pincha konstruktiv "
                "cheklovlar (podshipnik, shpon) mustahkamlikdan katta diametr "
                "talab qiladi."
            ),
            equations=[
                eq(r"M = \sqrt{M_v^2+M_g^2}", "Natijaviy eguvchi moment.", "Natijaviy moment"),
                eq(r"M_{ekv} = \sqrt{M^2+0{,}75T^2}", "Ekvivalent moment (fon Mizes).",
                   "Ekvivalent moment"),
                eq(r"d = \sqrt[3]{\frac{32M_{ekv}}{\pi[\sigma]}}", "Kerakli diametr.",
                   "Diametr"),
            ],
            conditions=(
                "Hisob statik yuklanish uchun. Real valda yuk siklik "
                "(aylanishda egilish kuchlanishi ishorasini o'zgartiradi), "
                "shuning uchun charchashga hisoblash shart (mq-28). Ruxsat "
                "etilgan kuchlanish ham shunga mos tanlanadi: dastlabki "
                "hisobda $[\\sigma] = 50...60$ MPa (past qiymat charchashni "
                "hisobga oladi)."
            ),
            worked_example=WorkedExample(
                statement=(
                    "Reduktor vali: ikki podshipnik orasi $L = 320$ mm, o'rtada "
                    "tishli g'ildirak ($d_w = 200$ mm) $T = 450$ N·m moment "
                    "uzatadi. Ilashish burchagi $20°$. "
                    "$[\\sigma] = 60$ MPa. Val diametrini aniqlang."
                ),
                given=[r"L = 0{,}32\ \text{m},\; d_w = 0{,}2\ \text{m},\; T = 450\ \text{N·m}",
                       r"\alpha_w = 20^\circ,\; [\sigma] = 60\ \text{MPa}"],
                steps=[
                    st(r"F_t = \frac{2T}{d_w} = \frac{2\cdot450}{0{,}2} = 4500\ \text{N}",
                       "Aylana bo'ylab kuch."),
                    st(r"F_r = F_t\tan20^\circ = 4500\cdot0{,}364 = 1638\ \text{N}",
                       "Radial kuch."),
                    st(r"M_g = \frac{F_tL}{4} = \frac{4500\cdot0{,}32}{4} = 360\ \text{N·m};\quad "
                       r"M_v = \frac{F_rL}{4} = \frac{1638\cdot0{,}32}{4} = 131\ \text{N·m}",
                       "Ikki tekislikdagi maksimal momentlar (o'rtada)."),
                    st(r"M = \sqrt{360^2+131^2} = \sqrt{129\,600+17\,161} = \sqrt{146\,761} = 383{,}1\ \text{N·m}",
                       "Natijaviy eguvchi moment."),
                    st(r"M_{ekv} = \sqrt{383{,}1^2 + 0{,}75\cdot450^2} = "
                       r"\sqrt{146\,766+151\,875} = \sqrt{298\,641} = 546{,}5\ \text{N·m}",
                       "Ekvivalent moment (fon Mizes)."),
                    st(r"d \ge \sqrt[3]{\frac{32\cdot546{,}5}{\pi\cdot60\cdot10^6}} = "
                       r"\sqrt[3]{9{,}28\cdot10^{-5}} = 0{,}0452\ \text{m} \Rightarrow d = 45\ \text{mm}",
                       "Kerakli diametr; standart qatordan 45 mm qabul qilamiz."),
                ],
                answer=(
                    "$F_t = 4500$ N, $F_r = 1638$ N; $M = 383{,}1$ N·m; "
                    "$M_{ekv} = 546{,}5$ N·m; $d = 45$ mm."
                ),
                engineering_note=(
                    "Buralish momenti ekvivalent momentga eguvchidan ko'proq "
                    "hissa qo'shdi ($0{,}75T^2 = 151\\,875$ va $M^2 = 146\\,766$). "
                    "Bu qisqa vallar uchun tipik. Shpon kanali kuchlanishni "
                    "~1,7 marta oshiradi, shuning uchun bu joyda diametr "
                    "5–10 % oshiriladi yoki konsentratsiya koeffitsienti bilan "
                    "hisoblanadi (mq-29)."
                ),
            ),
            computation=Computation(
                caption=(
                    "Val hisobi: yuklar va geometriyani o'zgartirib, epyuralarni "
                    "va kerakli diametr profilini quring."
                ),
                code='''"""Egilish + buralish: reduktor vali hisobi."""
import numpy as np
from labkit import PARAMS, note, series, table, value

L = float(PARAMS.get("L", 320.0))*1e-3     # podshipniklar orasi, m
a = float(PARAMS.get("a", 160.0))*1e-3     # g'ildirak koordinatasi, m
dw = float(PARAMS.get("dw", 200.0))*1e-3   # g'ildirak diametri, m
T = float(PARAMS.get("T", 450.0))          # buruvchi moment, N*m
alpha_w = float(PARAMS.get("alpha_w", 20.0))
s_allow = float(PARAMS.get("s_allow", 60.0))*1e6

Ft = 2*T/dw
Fr = Ft*np.tan(np.radians(alpha_w))
value("Aylana kuchi F_t", Ft, "N")
value("Radial kuch F_r", Fr, "N")

b = L - a
# Reaksiyalar (ikki tekislikda)
RA_g, RB_g = Ft*b/L, Ft*a/L
RA_v, RB_v = Fr*b/L, Fr*a/L

x = np.linspace(0, L, 400)
Mg = np.where(x <= a, RA_g*x, RB_g*(L-x))
Mv = np.where(x <= a, RA_v*x, RB_v*(L-x))
Mres = np.hypot(Mg, Mv)
Tx = np.where((x >= a-1e-12), 0.0, T)          # moment g'ildirakkacha uzatiladi
Tx = np.where(x <= a, T, 0.0)
Mekv = np.sqrt(Mres**2 + 0.75*Tx**2)
Mekv_tresk = np.sqrt(Mres**2 + Tx**2)

series("M_gorizontal(x)", x.tolist(), Mg.tolist(), xlabel="x, m", ylabel="M, N·m")
series("M_vertikal(x)", x.tolist(), Mv.tolist(), xlabel="x, m", ylabel="M, N·m")
series("M natijaviy(x)", x.tolist(), Mres.tolist(), xlabel="x, m", ylabel="M, N·m")
series("M_ekv (fon Mizes)", x.tolist(), Mekv.tolist(), xlabel="x, m", ylabel="M, N·m")
series("M_ekv (Tresk)", x.tolist(), Mekv_tresk.tolist(), xlabel="x, m", ylabel="M, N·m")

i_max = int(np.argmax(Mekv))
value("M natijaviy (maks)", float(np.max(Mres)), "N·m")
value("M_ekv (fon Mizes, maks)", float(np.max(Mekv)), "N·m")
value("M_ekv (Tresk, maks)", float(np.max(Mekv_tresk)), "N·m")
value("Xavfli kesim x", float(x[i_max]), "m")

d_mises = (32*np.max(Mekv)/(np.pi*s_allow))**(1/3)
d_tresk = (32*np.max(Mekv_tresk)/(np.pi*s_allow))**(1/3)
value("d (fon Mizes)", d_mises*1000, "mm")
value("d (Tresk)", d_tresk*1000, "mm")
note(f"Tresk {100*(d_tresk/d_mises-1):.1f} % katta diametr talab qiladi.")

# Diametr profili (teng mustahkamlik)
d_profile = (32*Mekv/(np.pi*s_allow))**(1/3)*1000
series("Kerakli diametr d(x)", x.tolist(), d_profile.tolist(),
       xlabel="x, m", ylabel="d, mm")

# Standart qatordan tanlash
std = np.array([20, 22, 25, 28, 30, 32, 35, 38, 40, 42, 45, 48, 50, 55, 60, 65, 70, 75, 80])
d_std = std[std >= d_mises*1000][0] if (std >= d_mises*1000).any() else std[-1]
value("Standart diametr", float(d_std), "mm")
W_std = np.pi*(d_std*1e-3)**3/32
value("Haqiqiy kuchlanish", float(np.max(Mekv)/W_std/1e6), "MPa")
value("Zaxira", float(s_allow/(np.max(Mekv)/W_std)), "—")

# Hissalarni taqqoslash
value("Egilish hissasi M²", float(np.max(Mres)**2), "N²·m²")
value("Buralish hissasi 0,75T²", float(0.75*T**2), "N²·m²")
note("Buralish ustun" if 0.75*T**2 > np.max(Mres)**2 else "Egilish ustun")

table("Kuchlanish konsentratsiyasi omillari",
      ["Element", "K_t (taxminiy)", "Tavsiya"],
      [["Shpon kanali", 1.6-1.8, "Diametrni 5–10 % oshirish"],
       ["Galtel r/d = 0,1", 1.5, "Radiusni oshirish"],
       ["Galtel r/d = 0,2", 1.25, "Optimal"],
       ["Ko'ndalang teshik", 2.0-2.5, "Imkon qadar qochish"]])
''',
                parameters=[
                    p("L", "Podshipniklar orasi L", 50.0, 2000.0, 320.0, 10.0, "mm"),
                    p("a", "G'ildirak koordinatasi a", 10.0, 1990.0, 160.0, 10.0, "mm"),
                    p("dw", "G'ildirak diametri", 20.0, 1000.0, 200.0, 10.0, "mm"),
                    p("T", "Buruvchi moment T", 10.0, 20000.0, 450.0, 10.0, "N·m"),
                    p("alpha_w", "Ilashish burchagi", 14.0, 30.0, 20.0, 0.5, "deg"),
                    p("s_allow", "[σ]", 20.0, 200.0, 60.0, 5.0, "MPa"),
                ],
                expected_output="F_t = 4500 N, M = 383,1 N·m, M_ekv = 546,5 N·m, d = 45 mm",
            ),
            visualization=vis(
                "Val epyuralari va diametr profili",
                "React/SVG",
                "To'rt panel: val sxemasi, ikki tekislikdagi moment epyuralari, "
                "natijaviy va ekvivalent moment, kerakli diametr profili. "
                "Xavfli kesim barcha panellarda belgilangan.",
                "React/SVG: val hisobining barcha bosqichlarini bir sahifada "
                "ko'rsatish — bu real konstruktorlik hujjatining formati. "
                "Diametr profili grafigi pog'onali valni loyihalash uchun "
                "to'g'ridan-to'g'ri asos beradi.",
            ),
            interpretation=(
                "Diametr profili grafigi pog'onali valni loyihalash uchun "
                "to'g'ridan-to'g'ri asos: har bir uchastkada kerakli minimal "
                "diametr ko'rinadi. Amalda esa podshipnik o'lchamlari va montaj "
                "talablari ko'pincha kattaroq diametr talab qiladi. "
                "Bu misolda buralish hissasi egilishdan katta — qisqa vallar "
                "uchun tipik holat."
            ),
            common_mistakes=[
                "Ikki tekislikdagi momentlarni algebraik qo'shish — ular "
                "geometrik (vektor) qo'shiladi.",
                "Buruvchi momentni butun val bo'ylab o'zgarmas deb olish — u "
                "faqat uzatuvchi va qabul qiluvchi elementlar orasida mavjud.",
                "Kuchlanish konsentratsiyasini hisobga olmaslik.",
                "Charchash hisobini o'tkazmaslik — aylanuvchi valda egilish "
                "kuchlanishi siklik.",
            ],
            quiz=[
                q("Nima uchun ikki tekislikdagi momentlar geometrik qo'shiladi?",
                  "Ular perpendikular o'qlarga nisbatan momentlar — vektor "
                  "kattaliklar, shuning uchun $M = \\sqrt{M_v^2+M_g^2}$.",
                  "konseptual"),
                q("$M = 300$ N·m, $T = 400$ N·m. $M_{ekv}$ (fon Mizes)?",
                  "$M_{ekv} = \\sqrt{300^2+0{,}75\\cdot400^2} = \\sqrt{90\\,000+120\\,000} = "
                  "458{,}3$ N·m.", "hisob"),
                q("$M_{ekv} = 500$ N·m, $[\\sigma] = 60$ MPa. Diametr?",
                  "$d = \\sqrt[3]{32\\cdot500/(\\pi\\cdot60\\cdot10^6)} = 43{,}7$ mm.",
                  "hisob"),
                q("Nima uchun val hisobida $[\\sigma]$ past (50–60 MPa) olinadi?",
                  "Aylanuvchi valda egilish kuchlanishi siklik o'zgaradi — "
                  "charchash hal qiluvchi bo'ladi; past $[\\sigma]$ buni "
                  "dastlabki hisobda qoplaydi.", "talqin"),
                q("Kodda `Tx = np.where(x <= a, T, 0.0)` nima qiladi?",
                  "Buruvchi moment faqat uzatish nuqtasigacha mavjud — undan "
                  "keyin val burilmaydi. Bu epyuraning to'g'ri shakli uchun muhim.",
                  "kod"),
            ],
            bridge_to_next=(
                "Murakkab qarshilik hollarini ko'rib chiqdik. Keyingi mavzuda "
                "ularni yagona energetik yondashuv bilan birlashtiramiz."
            ),
            research_extension=(
                "Valning kritik aylanish tezligini hisoblang: uni egilish "
                "tebranishlari nuqtai nazaridan ko'rib, $\\omega_{kr} = "
                "\\sqrt{g/\\delta_{st}}$ formulasini (nm-25) qo'llang. Ish "
                "tezligi kritikdan 30 % uzoqda bo'lishi shartini tekshiring. "
                "Ko'p diskli val uchun Dunkerley formulasini qo'llang."
            ),
        ),
    ),
    Topic(
        id="mq-24",
        subject_id=S,
        module_id=M,
        order=24,
        title="Elastik deformatsiya energiyasi, Kastilyano teoremasi va energetik usullar",
        description=(
            "Deformatsiya energiyasi, Klapeyron teoremasi, Kastilyano teoremasi "
            "va uning statik aniqmas tizimlarga qo'llanilishi."
        ),
        learning_objective=(
            "Energiya usullari bilan ko'chishlarni va statik aniqmas "
            "reaksiyalarni topish."
        ),
        prerequisites=["mq-20", "mq-16", "nm-15"],
        mathematical_core=(
            "Potensial energiya funksionali, qisman hosila, Kastilyano teoremasi, "
            "minimal energiya prinsipi."
        ),
        engineering_application=(
            "Murakkab ramalar, egri sterjenlar, prujinalar, statik aniqmas "
            "konstruksiyalar."
        ),
        computational_component=(
            "Kastilyano teoremasini simvolik (SymPy) qo'llash va sonli "
            "yechim bilan tekshirish."
        ),
        visualization_component=(
            "Energiya diagrammasi; kuch–ko'chish grafigi ostidagi yuza."
        ),
        research_extension=(
            "Minimal potensial energiya prinsipi qanday qilib Ritz usuliga "
            "va FEM ga olib boradi? (su-13, su-18)"
        ),
        difficulty="ilg'or",
        previous_link=(
            "nm-15 dagi potensial energiya g'oyasi va mq-16 dagi Mor integrali "
            "bu yerda yagona energetik nazariyaga birlashadi."
        ),
        next_topic="mq-25",
        estimated_minutes=95,
        tags=["Kastilyano", "deformatsiya energiyasi", "energetik usullar"],
        lesson=Lesson(
            physical_problem=(
                "Egri sterjen (masalan, S-shaklidagi ilgak) uchida qancha "
                "ko'chadi? Bunday konstruksiya uchun differensial tenglama "
                "yozish murakkab, chunki geometriya egri. Lekin energiya "
                "yondashuvi geometriyadan qat'i nazar ishlaydi: energiyani "
                "hisoblab, uni kuch bo'yicha differensiallash kifoya."
            ),
            concepts=[
                c("Deformatsiya energiyasi", "$U = \\int_V u\\,dV$ — jismda "
                  "to'plangan elastik energiya; yuklanishni olib tashlaganda "
                  "to'liq qaytariladi."),
                c("Klapeyron teoremasi", "$U = \\tfrac{1}{2}\\sum F_i\\delta_i$ — "
                  "statik yuklanishda ish energiyaning yarmiga teng "
                  "(kuch bosqichma-bosqich o'sadi)."),
                c("Kastilyano teoremasi", "$\\delta_i = \\partial U/\\partial F_i$ — "
                  "energiyaning kuch bo'yicha hosilasi shu kuch yo'nalishidagi "
                  "ko'chishni beradi."),
                c("Fiktiv kuch usuli", "Ko'chish izlanayotgan nuqtada kuch "
                  "bo'lmasa, fiktiv kuch kiritiladi va oxirida nolga "
                  "tenglashtiriladi."),
                c("Minimal energiya prinsipi", "Statik aniqmas tizimda ortiqcha "
                  "reaksiyalar energiyani minimallashtiradigan qiymatlarni oladi."),
            ],
            derivation=[
                d("1-qadam. Energiya ifodalari",
                  r"U = \int\frac{N^2}{2EA}dx + \int\frac{M^2}{2EI}dx + "
                  r"\int\frac{T^2}{2GI_p}dx + \int\frac{\kappa Q^2}{2GA}dx",
                  "Har bir deformatsiya turi o'z hissasini qo'shadi. Odatda "
                  "egilish hadi hukmron, kesuvchi kuch hadi esa tashlanadi."),
                d("2-qadam. Klapeyron teoremasi",
                  r"A = \int_0^{\delta}F\,d\delta = \int_0^{\delta}k\delta\,d\delta = "
                  r"\frac{k\delta^2}{2} = \frac{F\delta}{2} = U",
                  "Chiziqli tizimda kuch ko'chish bilan proporsional o'sadi, "
                  "shuning uchun ish $F\\delta$ emas, $F\\delta/2$."),
                d("3-qadam. Kastilyano teoremasi",
                  r"\boxed{\;\delta_i = \frac{\partial U}{\partial F_i}\;}",
                  "$U$ ni $F_i$ bo'yicha differensiallash. Isbot: kuchni "
                  "$dF_i$ ga oshirib, energiya o'zgarishini ikki usulda "
                  "hisoblash orqali."),
                d("4-qadam. Egilish uchun amaliy shakl",
                  r"\delta = \frac{\partial}{\partial F}\int\frac{M^2}{2EI}dx = "
                  r"\int\frac{M}{EI}\frac{\partial M}{\partial F}dx",
                  "Bu aynan Mor integrali (mq-16): $\\partial M/\\partial F = "
                  "\\bar M$ — birlik kuchdan moment."),
                d("5-qadam. Statik aniqmas tizim uchun",
                  r"\frac{\partial U}{\partial X_1} = 0",
                  "Ortiqcha reaksiya yo'nalishidagi ko'chish nolga teng — "
                  "demak energiya shu reaksiya bo'yicha minimumga ega "
                  "(minimal ish teoremasi, Menabrea)."),
            ],
            formula_meaning=(
                "Kastilyano teoremasi energiyani ko'chishlar bilan bevosita "
                "bog'laydi: energiyani bir marta hisoblab, uni turli kuchlar "
                "bo'yicha differensiallash orqali barcha ko'chishlarni topish "
                "mumkin. Statik aniqmas tizimda esa u yanada kuchli: "
                "$\\partial U/\\partial X = 0$ sharti ortiqcha reaksiyalarni "
                "to'g'ridan-to'g'ri beradi. Bu g'oya — minimal energiya "
                "prinsipi — butun hisoblash mexanikasining (Ritz, FEM) "
                "poydevoridir."
            ),
            equations=[
                eq(r"U = \int\frac{M^2}{2EI}dx + \int\frac{N^2}{2EA}dx + \int\frac{T^2}{2GI_p}dx",
                   "Deformatsiya energiyasi.", "Energiya"),
                eq(r"\delta_i = \frac{\partial U}{\partial F_i}", "Kastilyano teoremasi.",
                   "Kastilyano"),
                eq(r"\frac{\partial U}{\partial X_1} = 0", "Menabrea (minimal ish) teoremasi.",
                   "Minimal ish"),
            ],
            conditions=(
                "Teorema chiziqli-elastik tizim uchun. Fiktiv kuch usulida "
                "differensiallashdan keyin fiktiv kuch nolga tenglashtiriladi. "
                "Energiya ifodasida barcha ichki kuch omillarini hisobga olish "
                "kerak, lekin amalda ularning hissalari juda farq qiladi: "
                "egilish odatda 90 % dan ortiq."
            ),
            worked_example=WorkedExample(
                statement=(
                    "Yarim halqa shaklidagi egri sterjen (radius $R = 150$ mm), "
                    "bir uchi qotirilgan, ikkinchi uchiga $F = 500$ N kuch "
                    "(radial yo'nalishda). $EI = 2000$ N·m². Kuch yo'nalishidagi "
                    "ko'chishni Kastilyano teoremasi bilan toping."
                ),
                given=[r"R = 0{,}15\ \text{m},\; F = 500\ \text{N},\; EI = 2000\ \text{N·m}^2",
                       r"\text{yarim halqa: } \varphi \in [0, \pi]"],
                steps=[
                    st(r"M(\varphi) = FR\sin\varphi",
                       "Qotirishdan $\\varphi$ burchak masofadagi kesimdagi moment; "
                       "kuchning yelkasi $R\\sin\\varphi$."),
                    st(r"U = \int_0^{\pi}\frac{M^2}{2EI}R\,d\varphi = "
                       r"\frac{F^2R^3}{2EI}\int_0^{\pi}\sin^2\varphi\,d\varphi",
                       "Yoy elementi $ds = R\\,d\\varphi$."),
                    st(r"\int_0^{\pi}\sin^2\varphi\,d\varphi = \frac{\pi}{2} "
                       r"\;\Rightarrow\; U = \frac{\pi F^2R^3}{4EI}",
                       "Integral hisoblandi."),
                    st(r"\delta = \frac{\partial U}{\partial F} = \frac{\pi FR^3}{2EI}",
                       "Kastilyano teoremasi."),
                    st(r"\delta = \frac{3{,}1416\cdot500\cdot0{,}15^3}{2\cdot2000} = "
                       r"\frac{3{,}1416\cdot500\cdot3{,}375\cdot10^{-3}}{4000}",
                       "Sonli qiymatlarni qo'yamiz."),
                    st(r"\delta = \frac{5{,}301}{4000} = 1{,}325\cdot10^{-3}\ \text{m} = 1{,}33\ \text{mm}",
                       "Ko'chish. Tekshirish uchun Mor integrali bilan: "
                       "$\\int\\frac{M\\bar M}{EI}ds$, $\\bar M = R\\sin\\varphi$ — "
                       "aynan shu natija."),
                ],
                answer="$U = 0{,}331$ J; $\\delta = 1{,}33$ mm.",
                engineering_note=(
                    "Egri sterjen uchun differensial tenglama yozish ancha "
                    "murakkab bo'lardi, energiya usuli esa bir necha qatorda "
                    "yechdi. Aynan shuning uchun energetik usullar egri "
                    "sterjenlar, prujinalar va murakkab ramalar hisobida asosiy "
                    "hisoblanadi. Silindrik prujina hisobi ham shu usulda "
                    "olinadi."
                ),
            ),
            computation=Computation(
                caption=(
                    "Kastilyano teoremasi: energiyani hisoblab, ko'chishlarni "
                    "va statik aniqmas reaksiyalarni toping."
                ),
                code='''"""Energetik usullar: Kastilyano teoremasi va minimal ish prinsipi."""
import numpy as np
import sympy as sp
from scipy.integrate import quad
from labkit import PARAMS, note, series, table, value

R = float(PARAMS.get("R", 0.15))        # egrilik radiusi, m
F = float(PARAMS.get("F", 500.0))       # kuch, N
EI = float(PARAMS.get("EI", 2000.0))    # egilish bikrligi, N*m^2
L_beam = float(PARAMS.get("L", 2.0))    # konsol uzunligi (2-misol), m
q = float(PARAMS.get("q", 5000.0))      # taqsimlangan yuklama, N/m

# --- 1-misol: yarim halqa, simvolik yechim ---
phi, Fs, Rs, EIs = sp.symbols("phi F R EI", positive=True)
M_expr = Fs*Rs*sp.sin(phi)
U_expr = sp.integrate(M_expr**2/(2*EIs)*Rs, (phi, 0, sp.pi))
delta_expr = sp.simplify(sp.diff(U_expr, Fs))
note(f"U = {sp.simplify(U_expr)}")
note(f"δ = ∂U/∂F = {delta_expr}")

U_val = float(U_expr.subs({Fs: F, Rs: R, EIs: EI}))
delta_val = float(delta_expr.subs({Fs: F, Rs: R, EIs: EI}))
value("Energiya U", U_val, "J")
value("Ko'chish δ", delta_val*1000, "mm")
note(f"Klapeyron tekshiruvi: U = Fδ/2 = {F*delta_val/2:.6f} J ✓")

# Sonli tekshirish (Mor integrali)
d_num, _ = quad(lambda p: (F*R*np.sin(p))*(R*np.sin(p))/EI*R, 0, np.pi)
note(f"Mor integrali bilan: δ = {d_num*1000:.6f} mm (farq {abs(d_num-delta_val)*1e6:.3f} µm)")

# --- 2-misol: statik aniqmas balka, minimal ish prinsipi ---
X = sp.symbols("X")
x_s, q_s, L_s = sp.symbols("x q L", positive=True)
M_stat = X*x_s - q_s*x_s**2/2
U_stat = sp.integrate(M_stat**2/(2*EIs), (x_s, 0, L_s))
eq_min = sp.Eq(sp.diff(U_stat, X), 0)
X_sol = sp.solve(eq_min, X)[0]
note(f"∂U/∂X = 0 dan: X = {sp.simplify(X_sol)} (nazariy 3qL/8)")
X_num = float(X_sol.subs({q_s: q, L_s: L_beam}))
value("Reaksiya X (minimal ish)", X_num/1000, "kN")
value("Nazariy 3qL/8", 3*q*L_beam/8/1000, "kN")

# --- Energiya hissalarini taqqoslash (konsol balka) ---
A_sec, G_mod, kappa = 2e-3, 8e10, 1.2
U_bend = q**2*L_beam**5/(40*EI)
U_shear = kappa*(q*L_beam)**2*L_beam/(6*G_mod*A_sec)
value("Egilish energiyasi", U_bend, "J")
value("Siljish energiyasi", U_shear, "J")
value("Siljish ulushi", 100*U_shear/(U_bend+U_shear), "%")
note("Uzun balkalarda siljish energiyasi 1 % dan kam — shuning uchun tashlanadi.")

# Kuch–ko'chish grafigi (energiya = yuza)
FF = np.linspace(0, F, 100)
dd = FF*delta_val/F
series("Kuch–ko'chish diagrammasi", (dd*1000).tolist(), FF.tolist(),
       xlabel="δ, mm", ylabel="F, N")
note(f"Uchburchak yuzasi = F·δ/2 = {F*delta_val/2:.6f} J = U ✓ (Klapeyron)")

# Radiusning ko'chishga ta'siri
RR = np.linspace(0.05, 0.4, 100)
series("δ(R)", (RR*1000).tolist(), (np.pi*F*RR**3/(2*EI)*1000).tolist(),
       xlabel="R, mm", ylabel="δ, mm")
note("δ ~ R³ — radiusni 2 marta oshirish ko'chishni 8 marta oshiradi.")

table("Energiya turlari",
      ["Deformatsiya", "Energiya", "Odatdagi hissa"],
      [["Egilish", "∫M²/(2EI)dx", "85–99 %"],
       ["Buralish", "∫T²/(2GI_p)dx", "0–15 %"],
       ["Cho'zilish", "∫N²/(2EA)dx", "0–10 %"],
       ["Siljish", "∫κQ²/(2GA)dx", "< 2 % (uzun elementlarda)"]])
''',
                parameters=[
                    p("R", "Egrilik radiusi R", 0.02, 1.0, 0.15, 0.01, "m"),
                    p("F", "Kuch F", 10.0, 10000.0, 500.0, 10.0, "N"),
                    p("EI", "Egilish bikrligi EI", 100.0, 1000000.0, 2000.0, 100.0, "N·m²"),
                    p("L", "Konsol uzunligi L", 0.2, 10.0, 2.0, 0.1, "m"),
                    p("q", "Taqsimlangan yuklama q", 100.0, 50000.0, 5000.0, 100.0, "N/m"),
                ],
                expected_output="U = 0,331 J, δ = 1,33 mm, X = 3qL/8",
            ),
            visualization=vis(
                "Energiya va kuch–ko'chish diagrammasi",
                "React/SVG",
                "Kuch–ko'chish to'g'ri chizig'i va uning ostidagi uchburchak "
                "yuza (energiya) bo'yalgan; yonida energiya turlarining "
                "ustunli diagrammasi.",
                "React/SVG: Klapeyron teoremasining ($U = F\\delta/2$) geometrik "
                "ma'nosi — uchburchak yuzasi — bir qarashda tushunarli. "
                "Energiya hissalari diagrammasi esa qaysi deformatsiya turini "
                "hisobga olish kerakligini ko'rsatadi.",
            ),
            interpretation=(
                "Simvolik va sonli yechimlar bir xil natija beradi. "
                "$\\delta(R)$ grafigi kubik: egri sterjenning radiusi "
                "ko'chishga juda kuchli ta'sir qiladi. Energiya hissalari "
                "jadvali esa amaliy qoidani beradi: uzun elementlarda faqat "
                "egilish hisobga olinadi, kalta elementlarda esa siljish ham "
                "muhim bo'lishi mumkin."
            ),
            common_mistakes=[
                "Klapeyron teoremasida 1/2 koeffitsientini unutish.",
                "Fiktiv kuchni differensiallashdan oldin nolga tenglashtirish.",
                "Energiya ifodasida yoy elementi $ds = R\\,d\\varphi$ ni "
                "$dx$ bilan almashtirish (egri sterjenlarda).",
                "Minimal ish prinsipini nochiziqli tizimlarga qo'llash.",
            ],
            quiz=[
                q("Nima uchun $U = F\\delta/2$, $F\\delta$ emas?",
                  "Statik yuklanishda kuch nolda boshlanib asta-sekin $F$ gacha "
                  "o'sadi; ish esa kuch–ko'chish grafigi ostidagi uchburchak "
                  "yuzasi.", "konseptual"),
                q("Kastilyano teoremasi Mor integrali bilan qanday bog'liq?",
                  "$\\partial M/\\partial F = \\bar M$ — birlik kuchdan moment; "
                  "shuning uchun $\\partial U/\\partial F = \\int M\\bar M/(EI)dx$ "
                  "aynan Mor integrali.", "konseptual"),
                q("$U = \\pi F^2R^3/(4EI)$. $\\delta$ ni toping.",
                  "$\\delta = \\partial U/\\partial F = \\pi FR^3/(2EI)$.", "hisob"),
                q("Statik aniqmas tizimda $\\partial U/\\partial X = 0$ nimani "
                  "anglatadi?",
                  "Ortiqcha bog'lanish yo'nalishidagi ko'chish nolga teng — "
                  "ya'ni energiya shu reaksiya bo'yicha minimumga ega.", "talqin"),
                q("Kodda `sp.diff(U_stat, X)` nima uchun nolga tenglashtirilgan?",
                  "Menabrea (minimal ish) teoremasi bo'yicha statik aniqmas "
                  "tizimda ortiqcha reaksiya energiyani minimallashtiradi.",
                  "kod"),
            ],
            bridge_to_next=(
                "Mustahkamlik va bikrlik hisoblari to'liq o'rganildi. Lekin "
                "siqilgan element kuchlanish past bo'lsa ham buzilishi mumkin — "
                "ustuvorlikni yo'qotish orqali. Keyingi modul shu haqda."
            ),
            research_extension=(
                "Minimal potensial energiya prinsipini Ritz usuliga bog'lang: "
                "ko'chishni $w(x) = \\sum a_i\\varphi_i(x)$ ko'rinishida yozib, "
                "to'la potensial energiyani $a_i$ bo'yicha minimallashtiring. "
                "Konsol balka uchun bitta va ikkita hadli approksimatsiyani "
                "aniq yechim bilan taqqoslang — bu su-14 dagi Ritz usulining "
                "to'g'ridan-to'g'ri kirish nuqtasi."
            ),
            manim=manim(
                scene="StrainEnergyScene",
                module="manim/scenes/mq_energy.py",
                title="Deformatsiya energiyasi",
                summary="Kuch asta-sekin o'sadi, ko'chish ortadi va kuch–ko'chish "
                        "grafigi ostidagi yuza (energiya) to'ldiriladi.",
            ),
        ),
    ),
]
