# Mexanika Akademiyasi

Nazariy mexanikadan hisoblash mexanikasigacha — **5 fan, 150 mavzu**,
har bir mavzuda 18 bo'limli dars va brauzerda ishga tushadigan,
sandbox'da bajariladigan Python laboratoriyasi. Butun kontent
o'zbek tilida (lotin yozuvi).

## Ishga tushirish — ikki yo'l

**1-yo'l · Docker bilan** (tavsiya etiladi):
```
docker compose up --build
```

**2-yo'l · Docker'siz** (bitta buyruq, Windows/Mac/Linux):
```
python ishga-tushir.py
```

Ikkalasida ham sayt shu manzilda ochiladi:

| | |
|---|---|
| **Sayt** | **http://localhost:7070** |
| API hujjati (Swagger) | http://localhost:7070/docs |
| Sog'liq tekshiruvi | http://localhost:7070/health |

---

## 1. Nima qilingan

| Ko'rsatkich | Qiymat |
|---|---|
| Fanlar | 5 |
| Modullar | 25 |
| Mavzular | **150** (har fanda aynan 30 ta) |
| Interaktiv laboratoriyalar | 150 |
| Interaktiv chizmalar | 314 (har mavzuda ≥ 2 ta) |
| Mustahkamlash savollari | 863 |
| Chiqarish qadamlari | 1069 |
| Manim sahnalari | 86 |
| Yakuniy loyihalar | 5 |
| Testlar | 84 backend + 49 frontend |
| Akademik audit | 18/18 tekshiruv **PASS** |

Har bir mavzuning Python hisobi **haqiqatan bajariladi**: 150/150
laboratoriya sandbox ichida xatosiz ishlaydi (o'rtacha 1,13 s,
eng sekini 7,9 s).

## 2. Arxitektura

```
                 ┌─────────────────────────────────────────┐
  brauzer  ──────▶  nginx  ──/──▶  React + TypeScript (SPA) │
                 │           ──/api──▶  FastAPI             │
                 └────────────────────────┬────────────────┘
                                          │
                             ┌────────────▼─────────────┐
                             │  SQLite (SQLAlchemy)     │
                             │  fan / modul / mavzu /   │
                             │  loyiha / manba / jurnal │
                             └────────────┬─────────────┘
                                          │
                    ┌─────────────────────▼──────────────────────┐
                    │  SANDBOX — alohida jarayon                 │
                    │  AST filtri → python -I → rlimit → tarmoq  │
                    │  yopiq → timeout → chiqish cheklangan      │
                    └────────────────────────────────────────────┘
```

**Kontent zanjiri.** Kurikulum — tipli Python `dataclass` lari
(`content/curriculum/`). Ular JSON ga eksport qilinadi, backend esa
faqat shu JSON ni o'qiydi. Ya'ni backend kurikulum kodiga bog'liq
emas va konteynerga bitta fayl ko'chiriladi.

```
content/curriculum/*.py  ──export──▶  content/generated/curriculum.json  ──seed──▶  SQLite
```

**Texnologiyalar.** Backend: FastAPI, SQLAlchemy 2, Pydantic 2,
numpy/scipy/sympy. Frontend: React 18, TypeScript 5, Vite 5,
KaTeX, Monaco (lazy). Animatsiya: Manim Community.

## 3. Kurikulum

Fanlar qat'iy pedagogik zanjirda: har biri keyingisiga tenglama beradi.

| # | Fan | Kod | Mavzular | Nima beradi |
|---|---|---|---|---|
| 1 | Nazariy mexanika | NM | 30 | muvozanat, harakat, energiya |
| 2 | Materiallar qarshiligi | MQ | 30 | kuchlanish, deformatsiya, epyura |
| 3 | Tutash muhitlar mexanikasi | TMM | 30 | tenzorlar, elastiklik, plastiklik, suyuqlik |
| 4 | Plastinalar va qobiqlar nazariyasi | PQ | 30 | ikki o'lchovli konstruksiyalar |
| 5 | Sonli usullar va hisoblash mexanikasi | SU | 30 | FEM, xatolik, V&V, samaradorlik |

Zanjir `nm-01` (moddiy nuqta muvozanati) dan boshlanib, `su-30`
(to'liq hisoblash zanjiri) da yopiladi. Fanlar orasida **32 ta**
prerequisite havolasi bor — masalan `su-30` bir vaqtda `pq-13`,
`mq-13` va `tmm-21` ga tayanadi.

**Har bir mavzu 18 bo'limdan iborat:** nom → maqsad → talab
qilinadigan bilim → oldingi mavzu bilan bog'lanish → fizik masala →
asosiy tushunchalar → qadam-baqadam chiqarish → formulalarning fizik
ma'nosi → asosiy tenglamalar → chegaraviy shartlar → yechilgan
masala → Python hisobi → vizualizatsiya → natijalarning talqini →
tipik xatolar → 5–10 savol → keyingi mavzuga ko'prik → tadqiqot
yo'nalishi.

## 4. Interaktiv chizmalar

Darsning "Vizualizatsiya" bo'limida **jonli chizma** bor: surgichni
surasiz — chizma darhol brauzerda qayta hisoblanadi va qayta chiziladi
(backendga murojaat qilinmaydi).

**150 mavzuning hammasida kamida 2 tadan, jami 300 ta chizma.** Ular ustiga
14 ta mavzuda qo'lda yozilgan maxsus vidjet ham bor (Mor doirasi, fazaviy
portret, izoparametrik element va h.k.) — jami 314 ta interaktiv chizma.

### Qanday ishlaydi

Chizma **kurikulumning o'zida** tipli `Figure` dataclass sifatida yoziladi:

```python
fig("Buralishda urinma kuchlanish radius bo'ylab",
    "τ markazda nol, chetda maksimal — chiziqli taqsimot.",
    params=[fp("T", "Burovchi moment", 50, 5000, 800, 50, "N·m"),
            fp("d", "Val diametri", 10, 120, 40, 1, "mm")],
    curves=[fc("τ(r) = Tr/I_p", "T*x*1e-3/(pi*(d*1e-3)^4/32)/1e6", "tension")],
    x=("radius r, mm", "τ, MPa"), x_min="0", x_max="d/2",
    readouts=[fr("τ_max (chetda)", "16*T/(pi*(d*1e-3)^3)/1e6", "MPa", "tension")],
    note="Markazdagi material deyarli ishlamaydi — shuning uchun quvur to'la valdan samaraliroq.")
```

`export.py` uni JSON ga chiqaradi, backend JSON ni o'zgartirmasdan uzatadi,
`frontend/src/interactive/SpecFigure.tsx` esa render qiladi. Ifodalar
`expr.ts` dagi **shunting-yard hisoblagichi** bilan baholanadi: `eval`,
`new Function` yoki shunga o'xshash hech narsa ishlatilmaydi, faqat oq
ro'yxatdagi funksiyalar (`sin`, `sqrt`, `log`, `exp`, `min`, `max`, `atan2`, …)
va shu chizmaning o'z surgichlari ko'rinadi.

### O'lchov ramkasi qanday tanlanadi

Avtomatik masshtab har surishda qayta moslashtirilsa, egri chiziq **hech
qachon qimirlamagandek** ko'rinadi: masshtab ham parametr bilan birga
o'sadi. Shuning uchun `stableFrame()` y oralig'ini bir marta —
**surgichlarning butun diapazoni bo'yicha** hisoblaydi. Agar natijada
sukutdagi egri chiziq balandlikning 12 % idan kam joy egallasa (parametr
diapazoni bir necha tartibga cho'zilgan holat), ramka sukutdagi ko'rinishga
qaytariladi.

### Nima kafolatlanadi (testlar bilan)

| Kafolat | Qayerda tekshiriladi |
|---|---|
| Har bir mavzuda ≥ 2 chizma (150/150, jami 300) | `audit.py`, `test_api.py` |
| Har bir chizmada surgich, egri chiziq, ko'rsatkich va izoh bor | `audit.py` |
| Har bir ifoda kompilyatsiya bo'ladi, sukutdagi qiymatlarda CHEKLI son beradi | `figures.test.ts` |
| Har bir surgich yo rasmni siljitadi, yo ko'rsatkichni o'zgartiradi | `frame.test.ts` |
| **Birinchi** surgich rasmni ≥ 4 piksel siljitadi (150/150 × 2) | `frame.test.ts` |
| Chizmalar API orqali uzilmasdan yetib boradi | `test_api.py` |

Chizmadagi har bir son bajarilgan hisob bilan tekshirilgan. Masalan Navye
qatorining bir hadli xatosi (+2,4 %), chekli ayirmalarning sodda balkadagi
aniq munosabati (1 + 4/(5N²)), qistirilgan chekkadagi qobiq momenti
(0,2572 pRt), Nyumark davr xatosi (Δt/T = 0,1 da +3,21 %) va sdvig
qulflanishi koeffitsienti (1 + κ(L/h)²/(2(1+ν))) — hammasi sonli hisob
bilan olingan, taxmin qilingan emas.

Mavzular ro'yxatida chizmali mavzular **◆ chizma** belgisi bilan ajratilgan.

## 5. Interaktiv laboratoriya

Har bir mavzuda parametrlar bor. Ularni surasiz → **Ishga tushirish** →
kod backend sandbox'ida bajariladi → qiymatlar, jadvallar va
grafiklar yangilanadi. Kodni tahrirlash ham mumkin.

Kod natijani `print()` bilan emas, `labkit` orqali qaytaradi:

```python
from labkit import PARAMS, note, series, table, value

a = float(PARAMS.get("a", 25.0)) * 1e-3     # interfeysdagi surgich
value("w_max", w * 1e6, "um")               # skalyar
series("Yaqinlashish", ns, errs, "n", "%")  # grafik
table("Natijalar", ["n", "xato"], rows)     # jadval
note("Izoh matni")                          # xulosa
```

## 6. Xavfsizlik — foydalanuvchi kodi qanday bajariladi

**Foydalanuvchi Python kodi asosiy jarayonda hech qachon `exec()`
qilinmaydi.** Yetti mustaqil qatlam, har biri boshqasiga tayanmaydi:

| # | Qatlam | Nima qiladi |
|---|---|---|
| 1 | `sandbox/policy.py` | AST filtri: import oq ro'yxati, `eval`/`exec`/`open`/`__import__`/`getattr` taqiqi, dunder atributlar, hajm chegarasi |
| 2 | Alohida jarayon | `python -I` — muhit o'zgaruvchilari, user site-packages va cwd e'tiborsiz |
| 3 | Resurs cheklovlari | `RLIMIT_CPU`, `RLIMIT_AS`, `RLIMIT_DATA`, `RLIMIT_NOFILE`, `RLIMIT_FSIZE=0` (fayl yozib bo'lmaydi), `RLIMIT_NPROC=0` (fork yo'q) |
| 4 | Tarmoq | `socket` butunlay ishlamaydigan holga keltiriladi |
| 5 | Fayl tizimi | bo'sh vaqtinchalik katalog, tozalangan muhit, ish tugagach o'chiriladi |
| 6 | Vaqt | devor soati bo'yicha timeout va butun **jarayonlar guruhini** `SIGKILL` |
| 7 | Chiqish | `labkit` nuqta, satr va matn hajmini cheklaydi |

Konteyner darajasida ustiga yana bir qatlam qo'yiladi
(`docker-compose.yml`): `no-new-privileges`, `cap_drop: ALL`,
`pids_limit`, `mem_limit`, `tmpfs`, root'dan tashqari foydalanuvchi.

**Tekshirilgan.** 17 ta hujum ssenariysi avtomatik testda: `os`,
`subprocess`, `socket`, `pathlib`, `shutil` import qilish, fayl
o'qish va yozish, `__import__`, `().__class__.__mro__[1].__subclasses__()`,
`eval`, `exec`, `compile`, `builtins`, `getattr`, `globals`,
`sys.exit`, nisbiy import — **hammasi bloklanadi**. Shuningdek
cheksiz sikl, xotira bombasi, fork bombasi va haddan tashqari
katta chiqish ham to'xtatiladi.

### Ishlab chiqarish uchun sandbox

Yuqoridagi arxitektura **jarayon darajasida** izolyatsiya beradi va
bu o'quv platformasi uchun yetarli. Internetga ochiq, ishonchsiz
foydalanuvchilar uchun esa **yadro darajasidagi** izolyatsiya
qo'shish kerak. Tavsiya etilgan variantlar:

1. **gVisor** (`runsc`) — sandbox konteynerini alohida runtime'da
   ishga tushirish. Eng kam o'zgarish bilan eng katta yutuq:
   ```yaml
   backend:
     runtime: runsc
   ```
2. **nsjail** yoki **bubblewrap** — har bir kod bajarilishi uchun
   alohida nom fazosi (PID, tarmoq, mount, user), seccomp-bpf filtri
   bilan. `executor.py` dagi `subprocess.Popen` chaqiruvini
   `nsjail --config ... -- python -I runner.py` ga almashtirish kifoya.
3. **Firecracker mikro-VM** yoki **Kata Containers** — har bir
   ishga tushirish uchun alohida yadro. Eng qimmat, eng xavfsiz.
4. Qo'shimcha: kodni bajaruvchi xizmatni **alohida mashinada**,
   chiquvchi tarmoqsiz, faqat ichki navbat orqali saqlash.

`executor.py` shunday yozilganki, bu o'zgarishlar faqat bitta
funksiyaga (`run_code` ichidagi jarayon ishga tushirish) tegadi —
qolgan kod o'zgarmaydi.

## 7. Ishga tushirish

### 1-yo'l · Docker

```bash
docker compose up --build
```

| Xizmat | Manzil |
|---|---|
| **Sayt** | **http://localhost:7070** |
| Swagger | http://localhost:7070/docs |
| Sog'liq | http://localhost:7070/health |
| Backend to'g'ridan-to'g'ri | http://localhost:8000 |

To'xtatish: `docker compose down` · Ma'lumot bilan ham: `docker compose down -v`

Portni o'zgartirish: `docker-compose.yml` dagi `"7070:80"` ni tahrirlang.

### 2-yo'l · Docker'siz (bitta buyruq)

Docker o'rnatilmagan bo'lsa:

```bash
pip install -r backend/requirements.txt
python ishga-tushir.py
```

Skript o'zi: kurikulum JSON ini yaratadi → frontendni yig'adi (agar
`frontend/dist` bo'lmasa, Node.js 18+ kerak) → backendni 8000-portda
ko'taradi → saytni **http://localhost:7070** da beradi va `/api`
so'rovlarini backendga uzatadi (nginx o'rniga).

```bash
python ishga-tushir.py --rebuild     # frontendni qayta yig'ish
MEXANIKA_PORT=9090 python ishga-tushir.py   # boshqa port
```

To'xtatish: `Ctrl+C`

### 3-yo'l · Dev rejim (kod ustida ishlash uchun)

Ikkita terminal kerak.

**Backend:**
```bash
python -m content.curriculum.export          # JSON ni yaratish/yangilash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

**Frontend:**
```bash
cd frontend
npm install
npm run dev                                   # http://localhost:5173
```

Bu rejimda sahifa o'zgarishlarni darhol ko'rsatadi (hot reload).

Vite `/api` ni avtomatik 8000-portga uzatadi.

### Animatsiyalar (ixtiyoriy)

Manim og'ir tizim kutubxonalariga tayanadi, shuning uchun alohida
profilda:

```bash
docker compose --profile manim run --rm manim
# yoki mahalliy manim bilan:
python -m animatsiya.render --list
python -m animatsiya.render --topic su-30
python -m animatsiya.render --all --quality yuqori
```

Havolalarni render qilmasdan tekshirish:
```bash
python -m animatsiya.verify
```

## 8. Testlar

```bash
cd backend
python -m pytest                  # 84 test, ~27 s
python -m pytest --runslow        # + 150 laboratoriyaning HAMMASINI bajarish (~3 daqiqa)

cd ../frontend
npm test                          # 49 test
```

| To'plam | Soni | Nimani tekshiradi |
|---|---|---|
| `test_sandbox.py` | 27 | 17 hujum ssenariysi, CPU/xotira/chiqish chegaralari, oq ro'yxatlarning bir xilligi |
| `test_api.py` | 23 | barcha endpointlar, 404 lar, OpenAPI, `a^4` qonuni, 300 chizma HTTP orqali |
| `test_curriculum.py` | 24 | 150 mavzuning tuzilishi, chiqarish chuqurligi, savollar, soxta matn yo'qligi |
| `test_manim_refs.py` | 6 | 87 havola, 33 fayl, 86 sinf, nom soyalanishi |
| `test_interactive.py` | 6 | registry kalitlari, har fanda ≥2 maxsus vidjet |
| frontend | 66 | Epyura, Plot, muharrir, Lab, 14 maxsus vidjet va 300 spetsifikatsiyali chizma |

Kurikulum auditi alohida:
```bash
python -m content.curriculum.audit      # 20 tekshiruv
```

## 9. Loyiha tuzilishi

```
content/curriculum/       kurikulum manbai (tipli dataclass'lar)
  schema.py               Topic, Lesson, Computation, FinalProject ...
  subjects/               5 fan x 5 modul
  figures/                300 ta interaktiv chizma spetsifikatsiyasi
  projects.py             5 yakuniy loyiha
  audit.py                20 akademik tekshiruv
  export.py               -> content/generated/curriculum.json
backend/
  app/sandbox/            policy, executor, runner, labkit
  app/routers/            subjects, topics, projects, resources, curriculum, health
  app/models.py           SQLAlchemy
  tests/                  85 test
frontend/
  src/components/         Epure, Plot, Latex, CodeEditor, Lab
  src/interactive/        SpecFigure + expr.ts + 14 maxsus vidjet + registry
  src/pages/              Dashboard, Subject, Topic, Graph, Projects, Resources, Audit
  DESIGN.md               dizayn qarorlari va ularning asosi
animatsiya/
  scenes/                 33 fayl, 86 Manim sahnasi
  render.py, verify.py
docker/                   Dockerfile'lar va nginx konfiguratsiyasi
docker-compose.yml
```

## 10. API

| Metod | Yo'l | Tavsif |
|---|---|---|
| GET | `/health` | holat, sonlar, seed |
| GET | `/health/sandbox` | sandbox haqiqiy kod bilan tekshiriladi |
| GET | `/api/subjects` | 5 fan |
| GET | `/api/subjects/{id}` | modullar, mavzular, baholash |
| GET | `/api/topics` | `?subject_id&module_id&q&limit&offset` |
| GET | `/api/topics/{id}` | to'liq 18 bo'limli dars |
| GET | `/api/topics/{id}/lab` | laboratoriya parametrlari |
| POST | `/api/topics/{id}/run` | kodni sandbox'da bajarish |
| GET | `/api/projects` · `/api/projects/{id}` | yakuniy loyihalar |
| GET | `/api/resources` | adabiyotlar |
| GET | `/api/curriculum/graph` | bog'liqlik grafi |
| GET | `/api/curriculum/audit` | akademik audit natijasi |

## 11. Dizayn

Vizual til **chizmachilik va epyura an'anasidan** olingan — bu
o'zbek/rus muhandislik ta'limida 150 yildan beri ishlatilgan til.
Epyura (bazaviy chiziqqa perpendikulyar shtrixlar bilan to'ldirilgan
diagramma) interfeysning tuzilma elementi: o'zlashtirish ko'rsatkichi,
bo'lim ajratkichlari va bog'liqlik xaritasi shu tilda quriladi.

Palitra mexanikaning ikki qutbidan olingan: **cho'zilish** (oksid
qizil) va **siqilish** (po'lat ko'k). Bu ranglar hech qachon bezak
uchun ishlatilmaydi — faqat ishorani bildiradi.

Batafsil: [`frontend/DESIGN.md`](frontend/DESIGN.md).

## 12. Ushbu muhitda tekshirilmagan narsalar

Halollik uchun aniq ro'yxat:

- **Docker tasvirlari qurilmagan.** Docker demoni ishga tushirildi,
  lekin tashkilot tarmoq siyosati Docker Hub ning blob CDN'ini
  (`production.cloudfront.docker.com`) bloklaydi, shuning uchun
  bazaviy tasvirlarni (`python:3.11-slim` va h.k.) yuklab bo'lmadi.
  Tekshirilgani: `docker compose config` sintaksisi, barcha
  `MEXANIKA_*` muhit o'zgaruvchilarining `Settings` klassiga to'g'ri
  o'tishi va — eng muhimi — **`docker/nginx.conf` ning o'zi haqiqiy
  nginx bilan 7070-portda ishlatilib**, barcha marshrutlar
  (SPA, `/api`, `/health`, `/docs`, `/static`) tekshirilgani.
  Sizning kompyuteringizda Docker Hub ochiq bo'lsa,
  `docker compose up --build` to'g'ridan-to'g'ri ishlaydi.
- **Manim sahnalari render qilinmagan.** Manim cairo/pango tizim
  kutubxonalarini talab qiladi, ular bu muhitda yo'q. Buning o'rniga
  manim API'sining stub nusxasi yozilib, **87 ta sahnaning har biri
  qurib ko'rilgan** (`construct()` bajarilgan) — bu uchta haqiqiy
  xatoni ochdi va ular tuzatildi.
- Backend va frontend esa to'liq ishga tushirilgan va brauzerda
  (Chromium) uchdan-uchgacha tekshirilgan.
