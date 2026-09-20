# Dizayn yo'nalishi — Mexanika Akademiyasi

Bu hujjat frontend (STEP 8) uchun dizayn qarorlarini va ularning asosini
qayd qiladi. Har bir rang va shrift qarori shu yerdan olinadi.

## Mavzu va auditoriya

**Nima:** 5 fan × 30 mavzu = 150 mavzudan iborat mexanika o'quv platformasi,
ichida ishlaydigan Python laboratoriyasi bilan.
**Kim uchun:** 3–4-kurs talabalari va magistrantlar, o'zbek tilida,
uzoq o'qish seanslari (mavzu o'rtacha 90 daqiqa).
**Sahifaning bitta vazifasi:** talabani *keyingi* mavzuga olib borish —
zanjir uzilmasligi kerak.

## Nima uchun standart yechimlar emas

Uchta keng tarqalgan yo'nalish ataylab chetlab o'tildi:
krem fon + kontrast serif + terrakota; qora fon + kislotali yashil;
gazeta uslubidagi ingichka chiziqli maket. Ularning hech biri
mexanikaning o'z dunyosidan kelib chiqmaydi.

Bu platformaning vizual tili **chizmachilik va epyura an'anasidan** olinadi —
o'zbek/rus muhandislik ta'limida 150 yildan beri ishlatilgan til.

## Signature element: epyura (hatched epure)

Mexanikada har bir kattalik **epyura** sifatida chiziladi: bazaviy chiziqqa
perpendikulyar shtrixlar bilan to'ldirilgan diagramma, ishorasi esa
chiziqning qaysi tomonida yotishiga qarab beriladi. Bu dekoratsiya emas —
bu ma'lumot kodlash usuli.

Shuning uchun epyura butun interfeysning tuzilma elementi bo'ladi:

- **Progress**: fan bo'yicha o'zlashtirish epyura sifatida — tugallangan
  mavzular bazaviy chiziqdan yuqorida shtrixlangan, tugallanmaganlari past.
- **Dependency map**: bog'lanish chiziqlari epyura shtrixi bilan
  qalinlashadi — mavzu qancha ko'p narsaga asos bo'lsa, shuncha qalin.
- **Bo'lim ajratkichlari**: bitta ingichka bazaviy chiziq + qisqa shtrix qatori.
- **Lab natijalari**: musbat/manfiy qiymatlar epyura mantiqi bo'yicha
  bo'yaladi.

SVG `<pattern>` bilan real shtrix chiziladi, rasm emas.

## Ranglar

Mexanikaning o'zida ikki qutb bor: **cho'zilish va siqilish**. Bu ikkilik
150 mavzuning hammasida uchraydi (kuchlanish epyurasi, Mor doirasi,
ustuvorlik, membrana kuchlari). Palitra shundan olinadi.

```
--ink        #17191C   grafit — matn, asosiy chiziqlar (sovuq qora, qora emas)
--film       #E4E2DC   chizmachilik plyonkasi (krem emas: kulrang-issiq)
--paper      #F6F5F2   kartochka foni
--tension    #B2402E   cho'zilish — oksid qizil (chizmadagi qizil qalam)
--compress   #2B5A74   siqilish — po'lat ko'k
--rule       #9A968C   o'lchov chiziqlari, ramkalar
--mark       #D9A521   annotatsiya sarig'i — faqat joriy holat uchun
```

Qorong'i rejim: `--ink` va `--film` almashadi, `--tension`/`--compress`
yorqinligi oshiriladi (WCAG AA saqlanadi).

**Qoida:** `--tension` va `--compress` hech qachon bezak uchun
ishlatilmaydi — faqat ishora/qutbni bildiradi. Aks holda ular ma'nosini
yo'qotadi.

## Shriftlar

| Rol | Shrift | Nega |
|---|---|---|
| Display | **IBM Plex Sans Condensed** | ISO 3098 texnik yozuvining zamonaviy aksi: tor, tik, bir xil qalinlikdagi shtrix. Chizma varag'idagi sarlavha kabi o'qiladi. |
| Body | **Spectral** | Uzun o'zbek ilmiy matni uchun: `o'`, `g'` apostroflari aniq, x-balandligi katta, ekranda charchatmaydi. KaTeX bilan yaxshi turadi. |
| Data / kod | **IBM Plex Mono** | Monaco muharriri va `value()` natijalari bilan bir xil oila — lab va dars matni bir tizimda qoladi. |

Tipografik shkala (1.25 — major third), display faqat 3 o'lchamda
ishlatiladi. Sarlavhalar `letter-spacing: 0.02em` bilan —
chizmadagi yozuv kabi biroz yoyilgan.

## Nomerlash haqida

`01 / 02 / 03` kabi raqamli markerlar odatda bezak bo'ladi. Bu yerda esa
ular **haqiqiy ketma-ketlikni** bildiradi: dars 18 bo'limdan iborat va
tartib majburiy (fizik masala → model → tenglama → chegaraviy shart →
yechim → talqin). Shuning uchun nomerlash saqlanadi, lekin faqat dars
ichida — boshqa joyda emas.

## Maket

```
┌──────────────────────────────────────────────────────┐
│ MEXANIKA AKADEMIYASI        NM MQ TMM PQ SU   [◐]   │  ← title block
├────────────┬─────────────────────────────────────────┤
│            │                                         │
│  Mavzular  │   nm-17                                 │
│  ro'yxati  │   Inersiya tenzori va bosh o'qlar       │
│  (epyura   │   ────────────────────────────          │
│   progress)│   01  Fizik masala                      │
│            │   02  Asosiy tushunchalar               │
│            │   ...                                   │
│            │   12  [ Interactive Lab ]  ← Monaco     │
│            │                                         │
├────────────┴─────────────────────────────────────────┤
│ ← nm-16                                    nm-18 →   │  ← zanjir
└──────────────────────────────────────────────────────┘
```

Chap ustun — mavzular zanjiri, epyura progress bilan. O'ng tomon —
dars. Pastda zanjirning keyingi bo'g'ini har doim ko'rinadi:
sahifaning bitta vazifasi shu.

Mobil: chap ustun yig'iladi, epyura gorizontal tasmaga aylanadi.

## Animatsiya

Kam, lekin maqsadli:

- Epyura shtrixi sahifa ochilganda bazaviy chiziqdan o'sib chiqadi (250 ms).
- Lab "Run" bosilganda natija epyurasi qayta chiziladi — bu foydalanuvchiga
  hisob bajarilganini ko'rsatadi.
- Dependency map da mavzu ustiga kelganda uning butun oldingi zanjiri
  yoritiladi.

`prefers-reduced-motion` to'liq hurmat qilinadi.

## Sifat chegarasi

- 360 px kenglikdan boshlab ishlaydi, gorizontal scroll yo'q.
- Klaviatura fokusi ko'rinadi (`--mark` konturi).
- KaTeX formulalari `overflow-x: auto` ichida — uzun tenglama maketni buzmaydi.
- Kontrast: matn ≥ 4.5:1, yirik sarlavha ≥ 3:1, ikkala rejimda.
