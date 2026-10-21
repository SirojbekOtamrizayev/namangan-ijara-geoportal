import * as XLSX from 'xlsx';

// Kirill yozuvidagi matnlarni Lotin yozuviga o'girish (O'zbek alifbosi qoidalari asosida)
export const cyrillicToLatin = (text) => {
  if (!text || typeof text !== 'string') return text || '';

  const cyrToLatMap = {
    'А': 'A', 'а': 'a',
    'Б': 'B', 'б': 'b',
    'В': 'V', 'в': 'v',
    'Г': 'G', 'г': 'g',
    'Д': 'D', 'д': 'd',
    'Е': 'E', 'е': 'e',
    'Ё': 'Yo', 'ё': 'yo',
    'Ж': 'J', 'ж': 'j',
    'З': 'Z', 'з': 'z',
    'И': 'I', 'и': 'i',
    'Й': 'Y', 'й': 'y',
    'К': 'K', 'к': 'k',
    'Л': 'L', 'л': 'l',
    'М': 'M', 'м': 'm',
    'Н': 'N', 'н': 'n',
    'О': 'O', 'о': 'o',
    'П': 'P', 'п': 'p',
    'Р': 'R', 'р': 'r',
    'С': 'S', 'с': 's',
    'Т': 'T', 'т': 't',
    'У': 'U', 'у': 'u',
    'Ф': 'F', 'ф': 'f',
    'Х': 'X', 'х': 'x',
    'Ц': 'Ts', 'ц': 'ts',
    'Ч': 'Ch', 'ч': 'ch',
    'Ш': 'Sh', 'ш': 'sh',
    'Щ': 'Sh', 'щ': 'sh',
    'Ъ': "'", 'ъ': "'",
    'Ы': 'I', 'ы': 'i',
    'Ь': '', 'ь': '',
    'Э': 'E', 'э': 'e',
    'Ю': 'Yu', 'ю': 'yu',
    'Я': 'Ya', 'я': 'ya',
    'Ў': "O'", 'ў': "o'",
    'Ғ': "G'", 'ғ': "g'",
    'Қ': 'Q', 'қ': 'q',
    'Ҳ': 'H', 'ҳ': 'h'
  };

  return text.split('').map(char => cyrToLatMap[char] !== undefined ? cyrToLatMap[char] : char).join('');
};

// Vergul bilan ajratilgan yoki nuqtali kasr sonlarni to'g'ri o'qish (masalan: "67,91" -> 67.91)
export const parseDecimalNumber = (val, defaultVal = 0) => {
  if (val === undefined || val === null || val === '') return defaultVal;
  if (typeof val === 'number') return isNaN(val) ? defaultVal : val;
  const str = String(val).replace(/\s/g, '').replace(',', '.');
  const num = parseFloat(str);
  return isNaN(num) ? defaultVal : num;
};

// Namangan 14 ta tumanlari nomlarini normallashtirish va xaritalash (Kirill va Lotin qo'llab-quvvatlanadi)
export const normalizeDistrictName = (name) => {
  if (!name) return "pop";
  // Kirill bo'lsa avval lotinga o'giramiz
  const transliterated = cyrillicToLatin(String(name));
  const lower = transliterated.toLowerCase().replace(/['`ʻ’]/g, '').trim();

  if (lower.includes("shahar") || (lower.includes("namangan") && !lower.includes("tuman") && !lower.includes("yangi"))) return "namangan-shahri";
  if (lower.includes("yangi namangan")) return "yangi-namangan";
  if (lower.includes("davlatobod")) return "davlatobod";
  if (lower.includes("pop")) return "pop";
  if (lower.includes("chust")) return "chust";
  if (lower.includes("toraqorgon") || lower.includes("tora") || lower.includes("turakurgan")) return "toraqorgon";
  if (lower.includes("namangan")) return "namangan-tumani";
  if (lower.includes("mingbuloq") || lower.includes("mingbulok")) return "mingbuloq";
  if (lower.includes("kosonsoy")) return "kosonsoy";
  if (lower.includes("uychi")) return "uychi";
  if (lower.includes("yangiqorgon") || lower.includes("yangikurgan")) return "yangiqorgon";
  if (lower.includes("chortoq") || lower.includes("chortok")) return "chortoq";
  if (lower.includes("uchqorgon") || lower.includes("uchkurgan")) return "uchqorgon";
  if (lower.includes("norin")) return "norin";

  return "pop";
};

// Namunaviy ma'lumotlar shabloni (Sample rows)
export const SAMPLE_EXCEL_ROWS = [
  {
    "Tuman": "To'raqo'rg'on tumani",
    "MFY": "Shohand MFY",
    "Xonadon egasi": "Karimov Anvar Jo'rayevich",
    "Imtiyoz toifasi": "Ijtimoiy himoya reyestrida",
    "Oila azolari": 5,
    "Maydoni (ga)": 0.5,
    "Kontur raqami": "34-kontur",
    "Ixtisoslashuvi": "Ertapishar sabzavotchilik",
    "Yer namligi": "72% (Optimal namlik)",
    "Suv taminoti": "Katta Farg'ona kanali tarmog'i",
    "Tuproq unumdorligi (ball)": 76,
    "Tuproq turi": "Sug'oriladigan o'tloqi bo'z tuproq",
    "Tavsiya sabzavotlar": "Ertapishar sabzi, baqlajon, mosh",
    "Kutiladigan sof daromad (mln som)": 34.8
  },
  {
    "Tuman": "Pop tumani",
    "MFY": "G'urumsaroy MFY",
    "Xonadon egasi": "Rustamov Jamshid Qodirovich",
    "Imtiyoz toifasi": "Boquvchisini yo'qotgan oila",
    "Oila azolari": 5,
    "Maydoni (ga)": 0.5,
    "Kontur raqami": "142-kontur",
    "Ixtisoslashuvi": "Poliz va Eksportbop mosh",
    "Yer namligi": "58% (O'rtacha namlik)",
    "Suv taminoti": "Shimoliy Farg'ona kanali",
    "Tuproq unumdorligi (ball)": 64,
    "Tuproq turi": "Qumloq-bo'z tuproq",
    "Tavsiya sabzavotlar": "Mosh, qovun, tarvuz, sarimsoq",
    "Kutiladigan sof daromad (mln som)": 31.5
  },
  {
    "Tuman": "Chust tumani",
    "MFY": "O'g'asaroy MFY",
    "Xonadon egasi": "Ismoilov Otabek Shokirovich",
    "Imtiyoz toifasi": "Temir daftar (Yosh oila)",
    "Oila azolari": 4,
    "Maydoni (ga)": 0.4,
    "Kontur raqami": "56-kontur",
    "Ixtisoslashuvi": "Chust qalampiri va sabzi",
    "Yer namligi": "66% (Yuqori namlik)",
    "Suv taminoti": "Chustsoy arig'i",
    "Tuproq unumdorligi (ball)": 72,
    "Tuproq turi": "Tipik bo'z tuproq",
    "Tavsiya sabzavotlar": "Achchiq qalampir, sabzi, karam",
    "Kutiladigan sof daromad (mln som)": 36.2
  },
  {
    "Tuman": "Yangiqo'rg'on tumani",
    "MFY": "Nanay MFY",
    "Xonadon egasi": "Holiqov Mansurjon G'ulomovich",
    "Imtiyoz toifasi": "Nogironligi bor boquvchi (Ijtimoiy reyestr)",
    "Oila azolari": 6,
    "Maydoni (ga)": 0.5,
    "Kontur raqami": "11-kontur",
    "Ixtisoslashuvi": "Elita tog' kartoshkasi",
    "Yer namligi": "76% (Tabiiy namlik)",
    "Suv taminoti": "Podshota tog' soyi",
    "Tuproq unumdorligi (ball)": 82,
    "Tuproq turi": "Qora-qo'ng'ir tog' tuprog'i",
    "Tavsiya sabzavotlar": "Nanay kartoshkasi, malina, sarimsoq",
    "Kutiladigan sof daromad (mln som)": 47.8
  },
  {
    "Tuman": "Norin tumani",
    "MFY": "Haqqulobod MFY",
    "Xonadon egasi": "Madaminov Farhod Rustamovich",
    "Imtiyoz toifasi": "Ayollar daftari (ko'p bolali)",
    "Oila azolari": 6,
    "Maydoni (ga)": 0.5,
    "Kontur raqami": "118-kontur",
    "Ixtisoslashuvi": "Eksportbop Qizil piyoz",
    "Yer namligi": "76% (Yuqori namlik)",
    "Suv taminoti": "Norin daryosi va kollektor",
    "Tuproq unumdorligi (ball)": 81,
    "Tuproq turi": "Madaniy o'tloqi tuproq",
    "Tavsiya sabzavotlar": "Qizil piyoz, tarvuz, mosh",
    "Kutiladigan sof daromad (mln som)": 45.2
  }
];

// Davlat standarti bo'yicha Lotlar taqsimoti shabloni (5 ustunli)
export const SAMPLE_LOT_ROWS = [
  { "№": 1, "Tuman": "Мингбулоқ т.", "MFY nomi": "Қизилқум", "Lotlar soni": 120, "Maydoni (ga)": "67,91" },
  { "№": 2, "Tuman": "Мингбулоқ т.", "MFY nomi": "Янги Гулбоғ", "Lotlar soni": 85, "Maydoni (ga)": "45,50" },
  { "№": 3, "Tuman": "Поп т.", "MFY nomi": "Ғурумсарой", "Lotlar soni": 140, "Maydoni (ga)": "82,30" },
  { "№": 4, "Tuman": "Чуст т.", "MFY nomi": "Ўғасарой", "Lotlar soni": 95, "Maydoni (ga)": "54,20" },
  { "№": 5, "Tuman": "Тўрақўрғон т.", "MFY nomi": "Шоҳанд", "Lotlar soni": 110, "Maydoni (ga)": "62,15" },
  { "№": 6, "Tuman": "Уйчи т.", "MFY nomi": "Гулзор", "Lotlar soni": 75, "Maydoni (ga)": "38,40" },
  { "№": 7, "Tuman": "Косонсой т.", "MFY nomi": "Обод", "Lotlar soni": 90, "Maydoni (ga)": "48,00" }
];

// Lot shablonini yuklab berish (Davlat standarti)
export const downloadLotSampleExcel = () => {
  const wb = XLSX.utils.book_new();
  const wsData = [
    ["№", "Tuman", "MFY nomi", "Lotlar soni", "Maydoni (ga)"],
    [1, "Мингбулоқ т.", "Қизилқум", 120, "67,91"],
    [2, "Мингбулоқ т.", "Янги Гулбоғ", 85, "45,50"],
    [3, "Поп т.", "Ғурумсарой", 140, "82,30"],
    [4, "Чуст т.", "Ўғасарой", 95, "54,20"],
    [5, "Тўрақўрғон т.", "Шоҳанд", 110, "62,15"],
    [6, "Уйчи т.", "Гулзор", 75, "38,40"],
    [7, "Косонсой т.", "Обод", 90, "48,00"]
  ];
  const ws = XLSX.utils.aoa_to_sheet(wsData);
  ws['!cols'] = [
    { wch: 6 },
    { wch: 22 },
    { wch: 22 },
    { wch: 15 },
    { wch: 16 }
  ];
  XLSX.utils.book_append_sheet(wb, ws, "Lotlar_Taqsimoti");
  XLSX.writeFile(wb, "Namangan_Lot_Taqsimoti_Shabloni.xlsx");
};

// Namunaviy Excel faylni yuklab berish
export const downloadSampleExcel = () => {
  const ws = XLSX.utils.json_to_sheet(SAMPLE_EXCEL_ROWS);
  const wb = XLSX.utils.book_new();
  XLSX.utils.book_append_sheet(wb, ws, "Ijara_Yer_Shablon");

  // Ustunlar kengligini chiroyli qilish
  ws['!cols'] = [
    { wch: 22 }, // Tuman
    { wch: 18 }, // MFY
    { wch: 28 }, // Xonadon egasi
    { wch: 30 }, // Imtiyoz toifasi
    { wch: 12 }, // Oila azolari
    { wch: 14 }, // Maydoni (ga)
    { wch: 15 }, // Kontur raqami
    { wch: 25 }, // Ixtisoslashuvi
    { wch: 22 }, // Yer namligi
    { wch: 28 }, // Suv taminoti
    { wch: 24 }, // Tuproq unumdorligi
    { wch: 28 }, // Tuproq turi
    { wch: 32 }, // Tavsiya sabzavotlar
    { wch: 32 }  // Sof daromad
  ];

  XLSX.writeFile(wb, "Namangan_Ijara_Yer_Shabloni.xlsx");
};

// Yuklangan Excel yoki CSV faylni o'qish va tahlil qilish (Lot formati va To'liq formatni avtomatik aniqlaydi)
export const parseUploadedExcel = async (file) => {
  return new Promise((resolve, reject) => {
    const reader = new FileReader();

    reader.onload = (e) => {
      try {
        const data = new Uint8Array(e.target.result);
        const workbook = XLSX.read(data, { type: 'array' });
        const sheetName = workbook.SheetNames[0];
        const worksheet = workbook.Sheets[sheetName];

        // 2D massiv ko'rinishida o'qib sarlavhalar va tuzilmani aniqlash
        const sheetAOA = XLSX.utils.sheet_to_json(worksheet, { header: 1, defval: "" });
        if (!sheetAOA || sheetAOA.length === 0) {
          reject(new Error("Faylda ma'lumot topilmadi yoki bo'sh!"));
          return;
        }

        // Sarlavha qaysi qatorda turganini aniqlash (1-10 qatorlar orasida qidiramiz)
        let headerRowIdx = -1;
        let isLotHeader = false;

        for (let i = 0; i < Math.min(sheetAOA.length, 10); i++) {
          const rowStr = sheetAOA[i].map(c => String(c).toLowerCase()).join(' ');
          if (
            (rowStr.includes('lot') || rowStr.includes('лот')) &&
            (rowStr.includes('tuman') || rowStr.includes('туман') || rowStr.includes('mfy') || rowStr.includes('мфй'))
          ) {
            headerRowIdx = i;
            isLotHeader = true;
            break;
          }
          if (
            (rowStr.includes('tuman') || rowStr.includes('туман')) &&
            (rowStr.includes('mfy') || rowStr.includes('мфй') || rowStr.includes('mahalla') || rowStr.includes('маҳалла'))
          ) {
            headerRowIdx = i;
            break;
          }
        }

        const rawJson = XLSX.utils.sheet_to_json(worksheet, {
          defval: "",
          range: headerRowIdx >= 0 ? headerRowIdx : 0
        });

        if (!rawJson || rawJson.length === 0) {
          reject(new Error("Faylda ma'lumotlar jadvali topilmadi!"));
          return;
        }

        // Ustun nomlarini moslashuvchan izlash yordamchisi
        const getVal = (row, possibleKeys, def = "") => {
          for (const k of Object.keys(row)) {
            const kLower = k.toLowerCase().trim();
            for (const pk of possibleKeys) {
              if (kLower.includes(pk.toLowerCase())) {
                return row[k];
              }
            }
          }
          return def;
        };

        const firstKeys = Object.keys(rawJson[0] || {}).map(k => k.toLowerCase());
        const hasLotColumn = firstKeys.some(k => k.includes('lot') || k.includes('лот'));
        const isLotFormat = isLotHeader || hasLotColumn || (firstKeys.length <= 6 && firstKeys.some(k => k.includes('maydon') || k.includes('майдон') || k.includes('ga') || k.includes('га')));

        // ===== 1-VARIANT: DAVLAT STANDARTI (LOT FORMALARI) =====
        if (isLotFormat) {
          const parsedLots = [];

          rawJson.forEach((row, index) => {
            const rowValues = Object.values(row);
            const joinedText = rowValues.join(' ').toLowerCase();

            // Bo'sh yoki yig'indi (Jami, Total) qatorlarni tashlab ketish
            if (!joinedText || joinedText.includes('jami') || joinedText.includes('жами') || joinedText.includes('итого')) {
              return;
            }

            // Tuman
            let rawDistrict = getVal(row, ["туман", "tuman", "district", "hudud", "ҳудуд"], "");
            // MFY
            let rawMfy = getVal(row, ["мфй", "mfy", "mahalla", "маҳалла", "номи", "nomi", "qishloq"], "");
            // Lotlar soni
            let rawLots = getVal(row, ["лотлар сони", "лот сони", "лотлар", "лот", "lotlar soni", "lot soni", "lotlar", "lot", "soni"], "");
            // Maydoni (ga)
            let rawArea = getVal(row, ["майдони", "майдон", "maydoni", "maydon", "ga", "га", "гектар"], "");

            // Agar sarlavha mos kelmasa indeks bo'yicha olish (№, Tuman, MFY, Lotlar, Maydoni)
            if (!rawDistrict && rowValues[1]) rawDistrict = String(rowValues[1]);
            if (!rawMfy && rowValues[2]) rawMfy = String(rowValues[2]);
            if (!rawLots && rowValues[3] !== undefined) rawLots = rowValues[3];
            if (!rawArea && rowValues[4] !== undefined) rawArea = rowValues[4];

            if (!rawDistrict && !rawMfy) return; // Noto'g'ri qator

            const districtId = normalizeDistrictName(rawDistrict || "pop");
            const cleanMfyName = cyrillicToLatin(String(rawMfy || "Yangi MFY")).trim();
            const lotsCount = parseInt(String(rawLots).replace(/\D/g, ''), 10) || 1;
            const areaHa = parseDecimalNumber(rawArea, 0.5);

            if (areaHa <= 0) return;

            parsedLots.push({
              rowId: `LOT-${Date.now()}-${index}`,
              isLotFormat: true,
              rawDistrict: String(rawDistrict),
              districtId,
              mfyName: cleanMfyName,
              rawMfyName: String(rawMfy),
              lotsCount,
              allocatedAreaHa: Math.round(areaHa * 100) / 100,
              farmerName: `${lotsCount} ta dehqon oilasi (Lotlar)`,
              privilege: "Ijtimoiy reyestr va dehqon xo'jaliklari",
              familyMembers: lotsCount * 4,
              contourNumber: `${cleanMfyName} (${lotsCount} ta lot)`,
              specialization: "Ertapishar sabzavotchilik va poliz",
              soil: {
                type: "Sug'oriladigan unumdor bo'z tuproq",
                bonitetScore: 75,
                moisture: "72% (Optimal namlik)",
                salinity: "Sho'rlanmagan",
                groundwaterDepth: "1.8 metr",
                waterSource: "Kafolatlangan oqim ariq suvi"
              },
              recommendation: {
                primaryCrop: "Ertapishar sabzi, pomidor, poliz",
                secondaryCrop: "Dukkakli mosh va ko'katlar",
                rationale: "Tuproq-iqlim sharoitida yuqori hosil va kafolatlangan daromad beradi",
                cycleMonths: "Aprel - Noyabr"
              },
              economics: {
                expensesUzs: Math.round(areaHa * 18000000),
                expectedYield: `${Math.round(areaHa * 28)} tonna`,
                grossRevenueUzs: Math.round(areaHa * 75000000),
                netProfitUzs: Math.round(areaHa * 57000000),
                paybackMonths: 4
              }
            });
          });

          if (parsedLots.length === 0) {
            reject(new Error("Lot jadvalidan yaroqli qatorlar topilmadi. Tuman, MFY, Lotlar soni va Maydoni ustunlarini tekshiring."));
            return;
          }

          resolve(parsedLots);
          return;
        }

        // ===== 2-VARIANT: TO'LIQ 14 USTUNLI SHABLON =====
        const parsedRows = rawJson.map((row, index) => {
          const rawDistrict = String(getVal(row, ["tuman", "туман", "district", "hudud", "ҳудуд"], "Pop tumani"));
          const districtId = normalizeDistrictName(rawDistrict);
          const rawMfy = String(getVal(row, ["mfy", "мфй", "mahalla", "маҳалла", "qishloq"], `Yangi MFY`));
          const mfyName = cyrillicToLatin(rawMfy).trim();
          const farmerName = String(getVal(row, ["xonadon", "хонадон", "egasi", "fio", "фио", "fish", "fuqaro", "фуқаро", "ism"], `Fuqaro #${index + 1}`));
          const privilege = String(getVal(row, ["imtiyoz", "имтиёз", "toifa", "тоифа", "daftar", "daftar", "holat", "ijtimoiy"], "Ijtimoiy himoya reyestrida"));
          const rawArea = getVal(row, ["maydon", "майдон", "gektar", "гектар", "ga", "га", "sotix"], "0.5");
          const areaHa = parseDecimalNumber(rawArea, 0.5);
          const contour = String(getVal(row, ["kontur", "контур", "raqam", "рақам", "uchastka"], `${index + 101}-kontur`));
          const spec = String(getVal(row, ["ixtisos", "ихтисос", "yonalish", "faoliyat"], "Sabzavotchilik klasteri"));
          const moisture = String(getVal(row, ["namlik", "намлик", "nam"], "70% (Optimal namlik)"));
          const water = String(getVal(row, ["suv", "сув", "manba", "kanal", "ariq"], "Kafolatlangan oqim ariq suvi"));
          const bonitet = parseInt(getVal(row, ["bonitet", "бонитет", "unumdorlik", "ball"], "72"), 10) || 72;
          const soilType = String(getVal(row, ["tuproq", "тупроқ", "turi"], "Sug'oriladigan o'tloqi bo'z tuproq"));
          const crops = String(getVal(row, ["sabzavot", "сабзавот", "ekin", "экин", "tavsiya"], "Ertapishar sabzi, pomidor, mosh"));
          const profitMln = parseDecimalNumber(getVal(row, ["daromad", "даромад", "foyda", "фойда", "tushum"], "35.0"), 35.0);
          const familyMembers = parseInt(getVal(row, ["oila", "оила", "azo", "аъзо", "kishi"], "5"), 10) || 5;

          return {
            rowId: `EXCEL-${Date.now()}-${index}`,
            isLotFormat: false,
            rawDistrict,
            districtId,
            mfyName,
            farmerName: cyrillicToLatin(farmerName),
            privilege: cyrillicToLatin(privilege),
            familyMembers,
            allocatedAreaHa: areaHa > 10 ? Math.round((areaHa / 100) * 100) / 100 : Math.round(areaHa * 100) / 100,
            contourNumber: contour.includes("kontur") ? contour : `${contour}-kontur`,
            specialization: cyrillicToLatin(spec),
            soil: {
              type: soilType,
              bonitetScore: bonitet,
              moisture: moisture.includes("%") ? moisture : `${moisture}% (Optimal namlik)`,
              salinity: "Sho'rlanmagan",
              groundwaterDepth: "1.8 metr",
              waterSource: water
            },
            recommendation: {
              primaryCrop: cyrillicToLatin(crops),
              secondaryCrop: "Dukkakli mosh va ko'katlar",
              rationale: `${soilType} va ${moisture} namlik sharoitida yuqori hosil beradi.`,
              cycleMonths: "Aprel - Noyabr"
            },
            economics: {
              expensesUzs: Math.round(profitMln * 1000000 * 0.2),
              expectedYield: `${Math.round(areaHa * 25)} tonna`,
              grossRevenueUzs: Math.round(profitMln * 1000000 * 1.25),
              netProfitUzs: Math.round(profitMln * 1000000),
              paybackMonths: 3.5
            }
          };
        });

        resolve(parsedRows);
      } catch (err) {
        reject(err);
      }
    };

    reader.onerror = (err) => reject(err);
    reader.readAsArrayBuffer(file);
  });
};

// Tumanlar drayver yo'nalishlari shablonini yuklab berish (.xlsx)
export const downloadDriverSampleExcel = () => {
  const wb = XLSX.utils.book_new();
  const wsData = [
    ["№", "Туман номи", "Драйвер йўналиши", "Туман учун танланган драйвер йўналишнинг асослантирилиши"],
    [1, "Мингбулоқ т.", "Пахта-ғалла, полизчилик ва сабзавотчилик", "Суғориладиган катта майдон, Сирдарё сув ресурси ва полизчиликка ихтисослашган деҳқонлар."],
    [2, "Поп т.", "Полизчилик, экспортбоп мош ва тутзорчилик", "Қумлоқ бўз тупроқларда мош ва қовун-тарвуз ширинлиги ҳамда экспорт салоҳияти юқори."],
    [3, "Чуст т.", "Чуст аччиқ қалампири, боғдорчилик ва сабзавот", "Тарихий қалампир бренди, тоғолди серқуёш майдонлари ва сабзавотчилик кластери."],
    [4, "Тўрақўрғон т.", "Интенсив боғдорчилик ва эртапишар сабзавот", "Катта Фарғона канали суви, унумдор бўз тупроқ ва вилоят маркази бозорига яқинлик."],
    [5, "Янгиқўрғон т.", "Элита уруғлик картошка ва тоғ мевачилиги", "Баланд тоғ иқлими, соф табиий намлик ва вируссиз уруғлик картошка етиштириш."],
    [6, "Косонсой т.", "Доривор ўсимликлар ва мева-сабзавотчилик", "Тоғолди шароити, тоза тоғ суви ва шифобахш ўсимликлар кластери."],
    [7, "Уйчи т.", "Иссиқхона сабзавотчилиги ва паррандачилик", "Аҳоли зичлиги, ихчам ерлардан интенсив 3-4 марта ҳосил олиш имконияти."],
    [8, "Чортоқ т.", "Шифобахш боғдорчилик ва гилос-ўрикчилик", "Чортоқ тоғ микроиқлими ва экспортбоп мевалар ҳосилдорлиги юқорилиги."],
    [9, "Учқўрғон т.", "Балиқчилик ва суғориладиган сабзавотчилик", "Норин дарёсининг совуқ ва тоза оқар суви интенсив балиқчилик ҳавзалари учун қулай."],
    [10, "Норин т.", "Экспортбоп қизил пиёз ва шоличилик", "Норин дарёси бўйи нам тупроқлари ва пиёз етиштириш бўйича ихтисослашган деҳқонлар."],
    [11, "Давлатобод т.", "Иссиқхона хўжаликлари ва кўкатлар", "Шаҳар марказига яқин ихчам майдонларда гидропоника ва кўкатчилик."],
    [12, "Янги Наманган т.", "Интенсив сабзавотчилик ва лимонария", "Иссиқхона ва лимон етиштириш бўйича замонавий агротехнологиялар."],
    [13, "Наманган т.", "Эртапишар сабзавот ва кўчатчилик", "Фарғона водийси бозорларини эртаки кўчат ва сабзавот билан таъминлаш маркази."],
    [14, "Наманган шаҳри", "Шаҳар атрофи иссиқхона ва агрологистика", "Маҳсулотларни саралаш, музлатгичларда сақлаш ва экспортга жўнатиш."]
  ];
  const ws = XLSX.utils.aoa_to_sheet(wsData);
  ws['!cols'] = [
    { wch: 6 },
    { wch: 20 },
    { wch: 38 },
    { wch: 65 }
  ];
  XLSX.utils.book_append_sheet(wb, ws, "Tuman_Drayverlari");
  XLSX.writeFile(wb, "Namangan_Tumanlar_Drayver_Shabloni.xlsx");
};

// Tumanlar drayver va ixtisoslashuv jadvalini o'qish (Excel)
export const parseDriverSpecializationExcel = async (file) => {
  return new Promise((resolve, reject) => {
    const reader = new FileReader();

    reader.onload = (e) => {
      try {
        const data = new Uint8Array(e.target.result);
        const workbook = XLSX.read(data, { type: 'array' });
        const sheetName = workbook.SheetNames[0];
        const worksheet = workbook.Sheets[sheetName];

        const sheetAOA = XLSX.utils.sheet_to_json(worksheet, { header: 1, defval: "" });
        if (!sheetAOA || sheetAOA.length === 0) {
          reject(new Error("Faylda ma'lumot topilmadi yoki bo'sh!"));
          return;
        }

        let headerRowIdx = 0;
        for (let i = 0; i < Math.min(sheetAOA.length, 10); i++) {
          const rowStr = sheetAOA[i].map(c => String(c).toLowerCase()).join(' ');
          if (
            (rowStr.includes('tuman') || rowStr.includes('туман')) &&
            (rowStr.includes('drayver') || rowStr.includes('драйвер') || rowStr.includes('yonalish') || rowStr.includes('йўналиш'))
          ) {
            headerRowIdx = i;
            break;
          }
        }

        const rawJson = XLSX.utils.sheet_to_json(worksheet, {
          defval: "",
          range: headerRowIdx
        });

        const getVal = (row, possibleKeys, def = "") => {
          for (const k of Object.keys(row)) {
            const kLower = k.toLowerCase().trim();
            for (const pk of possibleKeys) {
              if (kLower.includes(pk.toLowerCase())) {
                return row[k];
              }
            }
          }
          return def;
        };

        const results = [];
        rawJson.forEach((row) => {
          const rowValues = Object.values(row);
          let rawDistrict = getVal(row, ["туман", "tuman", "district", "hudud", "ҳудуд"], "");
          let rawDriver = getVal(row, ["драйвер йўналиши", "драйвер", "driver", "йўналиши", "yonalishi", "ixtisos"], "");
          let rawRationale = getVal(row, ["асослантирилиши", "асослантириш", "asoslantirish", "асос", "asos", "izoh", "tavsif"], "");

          if (!rawDistrict && rowValues[1]) rawDistrict = String(rowValues[1]);
          if (!rawDriver && rowValues[2]) rawDriver = String(rowValues[2]);
          if (!rawRationale && rowValues[3]) rawRationale = String(rowValues[3]);

          if (!rawDistrict || String(rawDistrict).toLowerCase().includes('jami') || String(rawDistrict).toLowerCase().includes('жами')) {
            return;
          }

          const districtId = normalizeDistrictName(rawDistrict);
          const cleanDriver = cyrillicToLatin(String(rawDriver || "")).trim();
          const cleanRationale = cyrillicToLatin(String(rawRationale || "")).trim();

          results.push({
            districtId,
            rawDistrict: String(rawDistrict).trim(),
            driverDirection: cleanDriver || String(rawDriver || "").trim(),
            rawDriverDirection: String(rawDriver || "").trim(),
            driverRationale: cleanRationale || String(rawRationale || "").trim(),
            rawDriverRationale: String(rawRationale || "").trim()
          });
        });

        if (results.length === 0) {
          reject(new Error("Drayver jadvalidan tumanlar topilmadi. Ustunlar sarlavhalarini tekshiring."));
          return;
        }

        resolve(results);
      } catch (err) {
        reject(err);
      }
    };

    reader.onerror = (err) => reject(err);
    reader.readAsArrayBuffer(file);
  });
};

// Barcha ma'lumotlarni Excelga eksport qilish
export const exportDataToExcel = (districts) => {
  const exportRows = [];

  districts.forEach(d => {
    d.mfys?.forEach(m => {
      m.parcels?.forEach(p => {
        exportRows.push({
          "Tuman": d.name,
          "MFY": m.name,
          "Xonadon egasi": p.farmerName,
          "Imtiyoz toifasi": p.familyStatus,
          "Oila a'zolari": p.familyMembers || 5,
          "Maydoni (ga)": p.allocatedAreaHa,
          "Kontur raqami": p.contourNumber,
          "Ixtisoslashuvi": m.specialization || p.specialization || "Sabzavotchilik",
          "Yer namligi": p.soil.moisture,
          "Suv ta'minoti": p.soil.waterSource,
          "Tuproq unumdorligi (ball)": p.soil.bonitetScore,
          "Tuproq turi": p.soil.type,
          "Tavsiya sabzavotlar": p.recommendation.primaryCrop,
          "Kutiladigan sof daromad (mln so'm)": (p.economics.netProfitUzs / 1000000).toFixed(1)
        });
      });
    });
  });

  const ws = XLSX.utils.json_to_sheet(exportRows);
  const wb = XLSX.utils.book_new();
  XLSX.utils.book_append_sheet(wb, ws, "Namangan_Ijara_Yerlar");
  XLSX.writeFile(wb, `Namangan_Ijara_Yerlar_Baza_${new Date().toISOString().slice(0, 10)}.xlsx`);
};

// =========================================================================
// SABZAVOT VA EKINLAR DAROMAD JADVALI (2-rasmdagi aynan shu Excel shablon)
// =========================================================================

export const CROPS_EXCEL_TEMPLATE = [
  {
    "№": 1,
    "Mahsulot nomi": "Sholg'om",
    "Mahalliy usulda (Navi)": "Петровская 1",
    "1 ga hosil (tonna)": 20.0,
    "1 ga daromad (so'm)": 60000000,
    "15 sotix hosil (tonna)": 3.0,
    "15 sotix daromad (so'm)": 9000000,
    "10 sotix hosil (tonna)": 2.0,
    "10 sotix daromad (so'm)": 6000000,
    "Yangi usulda (Yangi nav nomi)": "Гейша",
    "Yangi usul 1 ga hosil (tonna)": 35.0,
    "Yangi usul 1 ga daromad (so'm)": 105000000,
    "Yangi usul 15 sotix hosil (tonna)": 5.3,
    "Yangi usul 15 sotix daromad (so'm)": 15750000,
    "Yangi usul 10 sotix hosil (tonna)": 3.5,
    "Yangi usul 10 sotix daromad (so'm)": 10500000,
    "Narx (so'm/kg)": 3000
  },
  {
    "№": 2,
    "Mahsulot nomi": "Turp",
    "Mahalliy usulda (Navi)": "Дунганская 12/8",
    "1 ga hosil (tonna)": 20.0,
    "1 ga daromad (so'm)": 60000000,
    "15 sotix hosil (tonna)": 3.0,
    "15 sotix daromad (so'm)": 9000000,
    "10 sotix hosil (tonna)": 2.0,
    "10 sotix daromad (so'm)": 6000000,
    "Yangi usulda (Yangi nav nomi)": "Ризен",
    "Yangi usul 1 ga hosil (tonna)": 35.0,
    "Yangi usul 1 ga daromad (so'm)": 105000000,
    "Yangi usul 15 sotix hosil (tonna)": 5.3,
    "Yangi usul 15 sotix daromad (so'm)": 15750000,
    "Yangi usul 10 sotix hosil (tonna)": 3.5,
    "Yangi usul 10 sotix daromad (so'm)": 10500000,
    "Narx (so'm/kg)": 3000
  },
  {
    "№": 3,
    "Mahsulot nomi": "Karam",
    "Mahalliy usulda (Navi)": "Пекинская ранняя",
    "1 ga hosil (tonna)": 30.0,
    "1 ga daromad (so'm)": 90000000,
    "15 sotix hosil (tonna)": 4.5,
    "15 sotix daromad (so'm)": 13500000,
    "10 sotix hosil (tonna)": 3.0,
    "10 sotix daromad (so'm)": 9000000,
    "Yangi usulda (Yangi nav nomi)": "Мэй Куинг F1",
    "Yangi usul 1 ga hosil (tonna)": 50.0,
    "Yangi usul 1 ga daromad (so'm)": 150000000,
    "Yangi usul 15 sotix hosil (tonna)": 7.5,
    "Yangi usul 15 sotix daromad (so'm)": 22500000,
    "Yangi usul 10 sotix hosil (tonna)": 5.0,
    "Yangi usul 10 sotix daromad (so'm)": 15000000,
    "Narx (so'm/kg)": 3000
  },
  {
    "№": 4,
    "Mahsulot nomi": "Bosh karam",
    "Mahalliy usulda (Navi)": "Слава 1305",
    "1 ga hosil (tonna)": 40.0,
    "1 ga daromad (so'm)": 120000000,
    "15 sotix hosil (tonna)": 6.0,
    "15 sotix daromad (so'm)": 18000000,
    "10 sotix hosil (tonna)": 4.0,
    "10 sotix daromad (so'm)": 12000000,
    "Yangi usulda (Yangi nav nomi)": "Мегатон F1",
    "Yangi usul 1 ga hosil (tonna)": 70.0,
    "Yangi usul 1 ga daromad (so'm)": 210000000,
    "Yangi usul 15 sotix hosil (tonna)": 10.5,
    "Yangi usul 15 sotix daromad (so'm)": 31500000,
    "Yangi usul 10 sotix hosil (tonna)": 7.0,
    "Yangi usul 10 sotix daromad (so'm)": 21000000,
    "Narx (so'm/kg)": 3000
  },
  {
    "№": 5,
    "Mahsulot nomi": "Gul karam",
    "Mahalliy usulda (Navi)": "Сноуболл",
    "1 ga hosil (tonna)": 15.0,
    "1 ga daromad (so'm)": 120000000,
    "15 sotix hosil (tonna)": 2.3,
    "15 sotix daromad (so'm)": 18000000,
    "10 sotix hosil (tonna)": 1.5,
    "10 sotix daromad (so'm)": 12000000,
    "Yangi usulda (Yangi nav nomi)": "Сноу Кинг F1",
    "Yangi usul 1 ga hosil (tonna)": 28.0,
    "Yangi usul 1 ga daromad (so'm)": 224000000,
    "Yangi usul 15 sotix hosil (tonna)": 4.2,
    "Yangi usul 15 sotix daromad (so'm)": 33600000,
    "Yangi usul 10 sotix hosil (tonna)": 2.8,
    "Yangi usul 10 sotix daromad (so'm)": 22400000,
    "Narx (so'm/kg)": 8000
  },
  {
    "№": 6,
    "Mahsulot nomi": "Brokkoli",
    "Mahalliy usulda (Navi)": "Калабрезе",
    "1 ga hosil (tonna)": 8.0,
    "1 ga daromad (so'm)": 80000000,
    "15 sotix hosil (tonna)": 1.2,
    "15 sotix daromad (so'm)": 12000000,
    "10 sotix hosil (tonna)": 0.8,
    "10 sotix daromad (so'm)": 8000000,
    "Yangi usulda (Yangi nav nomi)": "Маратон F1",
    "Yangi usul 1 ga hosil (tonna)": 18.0,
    "Yangi usul 1 ga daromad (so'm)": 180000000,
    "Yangi usul 15 sotix hosil (tonna)": 2.7,
    "Yangi usul 15 sotix daromad (so'm)": 27000000,
    "Yangi usul 10 sotix hosil (tonna)": 1.8,
    "Yangi usul 10 sotix daromad (so'm)": 18000000,
    "Narx (so'm/kg)": 10000
  },
  {
    "№": 7,
    "Mahsulot nomi": "Kolrabi",
    "Mahalliy usulda (Navi)": "Венская белая 1350",
    "1 ga hosil (tonna)": 15.0,
    "1 ga daromad (so'm)": 60000000,
    "15 sotix hosil (tonna)": 2.3,
    "15 sotix daromad (so'm)": 9000000,
    "10 sotix hosil (tonna)": 1.5,
    "10 sotix daromad (so'm)": 6000000,
    "Yangi usulda (Yangi nav nomi)": "Мозарт F1",
    "Yangi usul 1 ga hosil (tonna)": 30.0,
    "Yangi usul 1 ga daromad (so'm)": 120000000,
    "Yangi usul 15 sotix hosil (tonna)": 4.5,
    "Yangi usul 15 sotix daromad (so'm)": 18000000,
    "Yangi usul 10 sotix hosil (tonna)": 3.0,
    "Yangi usul 10 sotix daromad (so'm)": 12000000,
    "Narx (so'm/kg)": 4000
  },
  {
    "№": 8,
    "Mahsulot nomi": "Baqlajon",
    "Mahalliy usulda (Navi)": "Алмаз",
    "1 ga hosil (tonna)": 25.0,
    "1 ga daromad (so'm)": 125000000,
    "15 sotix hosil (tonna)": 3.8,
    "15 sotix daromad (so'm)": 18750000,
    "10 sotix hosil (tonna)": 2.5,
    "10 sotix daromad (so'm)": 12500000,
    "Yangi usulda (Yangi nav nomi)": "Бибо F1",
    "Yangi usul 1 ga hosil (tonna)": 50.0,
    "Yangi usul 1 ga daromad (so'm)": 250000000,
    "Yangi usul 15 sotix hosil (tonna)": 7.5,
    "Yangi usul 15 sotix daromad (so'm)": 37500000,
    "Yangi usul 10 sotix hosil (tonna)": 5.0,
    "Yangi usul 10 sotix daromad (so'm)": 25000000,
    "Narx (so'm/kg)": 5000
  },
  {
    "№": 9,
    "Mahsulot nomi": "Shirin qalampir",
    "Mahalliy usulda (Navi)": "Калифорнийское чудо",
    "1 ga hosil (tonna)": 20.0,
    "1 ga daromad (so'm)": 140000000,
    "15 sotix hosil (tonna)": 3.0,
    "15 sotix daromad (so'm)": 21000000,
    "10 sotix hosil (tonna)": 2.0,
    "10 sotix daromad (so'm)": 14000000,
    "Yangi usulda (Yangi nav nomi)": "Атлант F1",
    "Yangi usul 1 ga hosil (tonna)": 45.0,
    "Yangi usul 1 ga daromad (so'm)": 315000000,
    "Yangi usul 15 sotix hosil (tonna)": 6.8,
    "Yangi usul 15 sotix daromad (so'm)": 47250000,
    "Yangi usul 10 sotix hosil (tonna)": 4.5,
    "Yangi usul 10 sotix daromad (so'm)": 31500000,
    "Narx (so'm/kg)": 7000
  },
  {
    "№": 10,
    "Mahsulot nomi": "Achchiq qalampir",
    "Mahalliy usulda (Navi)": "Астраханский 147",
    "1 ga hosil (tonna)": 8.0,
    "1 ga daromad (so'm)": 80000000,
    "15 sotix hosil (tonna)": 1.2,
    "15 sotix daromad (so'm)": 12000000,
    "10 sotix hosil (tonna)": 0.8,
    "10 sotix daromad (so'm)": 8000000,
    "Yangi usulda (Yangi nav nomi)": "Халапеньо",
    "Yangi usul 1 ga hosil (tonna)": 20.0,
    "Yangi usul 1 ga daromad (so'm)": 200000000,
    "Yangi usul 15 sotix hosil (tonna)": 3.0,
    "Yangi usul 15 sotix daromad (so'm)": 30000000,
    "Yangi usul 10 sotix hosil (tonna)": 2.0,
    "Yangi usul 10 sotix daromad (so'm)": 20000000,
    "Narx (so'm/kg)": 10000
  },
  {
    "№": 11,
    "Mahsulot nomi": "Osh lavlagi",
    "Mahalliy usulda (Navi)": "Бордо 237",
    "1 ga hosil (tonna)": 25.0,
    "1 ga daromad (so'm)": 62500000,
    "15 sotix hosil (tonna)": 3.8,
    "15 sotix daromad (so'm)": 9375000,
    "10 sotix hosil (tonna)": 2.5,
    "10 sotix daromad (so'm)": 6250000,
    "Yangi usulda (Yangi nav nomi)": "Детройт",
    "Yangi usul 1 ga hosil (tonna)": 45.0,
    "Yangi usul 1 ga daromad (so'm)": 112500000,
    "Yangi usul 15 sotix hosil (tonna)": 6.8,
    "Yangi usul 15 sotix daromad (so'm)": 16875000,
    "Yangi usul 10 sotix hosil (tonna)": 4.5,
    "Yangi usul 10 sotix daromad (so'm)": 11250000,
    "Narx (so'm/kg)": 2500
  },
  {
    "№": 12,
    "Mahsulot nomi": "Makkajo'xori",
    "Mahalliy usulda (Navi)": "Краснодарский сахарный 50",
    "1 ga hosil (tonna)": 8.0,
    "1 ga daromad (so'm)": 24000000,
    "15 sotix hosil (tonna)": 1.2,
    "15 sotix daromad (so'm)": 3600000,
    "10 sotix hosil (tonna)": 0.8,
    "10 sotix daromad (so'm)": 2400000,
    "Yangi usulda (Yangi nav nomi)": "Санденс F1",
    "Yangi usul 1 ga hosil (tonna)": 14.0,
    "Yangi usul 1 ga daromad (so'm)": 42000000,
    "Yangi usul 15 sotix hosil (tonna)": 2.1,
    "Yangi usul 15 sotix daromad (so'm)": 6300000,
    "Yangi usul 10 sotix hosil (tonna)": 1.4,
    "Yangi usul 10 sotix daromad (so'm)": 4200000,
    "Narx (so'm/kg)": 3000
  },
  {
    "№": 13,
    "Mahsulot nomi": "Kartoshka",
    "Mahalliy usulda (Navi)": "Невский",
    "1 ga hosil (tonna)": 20.0,
    "1 ga daromad (so'm)": 80000000,
    "15 sotix hosil (tonna)": 3.0,
    "15 sotix daromad (so'm)": 12000000,
    "10 sotix hosil (tonna)": 2.0,
    "10 sotix daromad (so'm)": 8000000,
    "Yangi usulda (Yangi nav nomi)": "Пикассо",
    "Yangi usul 1 ga hosil (tonna)": 40.0,
    "Yangi usul 1 ga daromad (so'm)": 160000000,
    "Yangi usul 15 sotix hosil (tonna)": 6.0,
    "Yangi usul 15 sotix daromad (so'm)": 24000000,
    "Yangi usul 10 sotix hosil (tonna)": 4.0,
    "Yangi usul 10 sotix daromad (so'm)": 16000000,
    "Narx (so'm/kg)": 4000
  },
  {
    "№": 14,
    "Mahsulot nomi": "Tarvuz",
    "Mahalliy usulda (Navi)": "Мелитопольский",
    "1 ga hosil (tonna)": 25.0,
    "1 ga daromad (so'm)": 50000000,
    "15 sotix hosil (tonna)": 3.8,
    "15 sotix daromad (so'm)": 7500000,
    "10 sotix hosil (tonna)": 2.5,
    "10 sotix daromad (so'm)": 5000000,
    "Yangi usulda (Yangi nav nomi)": "Кримсон Свит",
    "Yangi usul 1 ga hosil (tonna)": 50.0,
    "Yangi usul 1 ga daromad (so'm)": 100000000,
    "Yangi usul 15 sotix hosil (tonna)": 7.5,
    "Yangi usul 15 sotix daromad (so'm)": 15000000,
    "Yangi usul 10 sotix hosil (tonna)": 5.0,
    "Yangi usul 10 sotix daromad (so'm)": 10000000,
    "Narx (so'm/kg)": 2000
  },
  {
    "№": 15,
    "Mahsulot nomi": "Qovun",
    "Mahalliy usulda (Navi)": "Гулоби",
    "1 ga hosil (tonna)": 15.0,
    "1 ga daromad (so'm)": 60000000,
    "15 sotix hosil (tonna)": 2.3,
    "15 sotix daromad (so'm)": 9000000,
    "10 sotix hosil (tonna)": 1.5,
    "10 sotix daromad (so'm)": 6000000,
    "Yangi usulda (Yangi nav nomi)": "Ананас",
    "Yangi usul 1 ga hosil (tonna)": 30.0,
    "Yangi usul 1 ga daromad (so'm)": 120000000,
    "Yangi usul 15 sotix hosil (tonna)": 4.5,
    "Yangi usul 15 sotix daromad (so'm)": 18000000,
    "Yangi usul 10 sotix hosil (tonna)": 3.0,
    "Yangi usul 10 sotix daromad (so'm)": 12000000,
    "Narx (so'm/kg)": 4000
  },
  {
    "№": 16,
    "Mahsulot nomi": "Qovoq",
    "Mahalliy usulda (Navi)": "Мраморная",
    "1 ga hosil (tonna)": 25.0,
    "1 ga daromad (so'm)": 62500000,
    "15 sotix hosil (tonna)": 3.8,
    "15 sotix daromad (so'm)": 9375000,
    "10 sotix hosil (tonna)": 2.5,
    "10 sotix daromad (so'm)": 6250000,
    "Yangi usulda (Yangi nav nomi)": "Хоккайдо",
    "Yangi usul 1 ga hosil (tonna)": 40.0,
    "Yangi usul 1 ga daromad (so'm)": 100000000,
    "Yangi usul 15 sotix hosil (tonna)": 6.0,
    "Yangi usul 15 sotix daromad (so'm)": 15000000,
    "Yangi usul 10 sotix hosil (tonna)": 4.0,
    "Yangi usul 10 sotix daromad (so'm)": 10000000,
    "Narx (so'm/kg)": 2500
  },
  {
    "№": 17,
    "Mahsulot nomi": "Kunjut",
    "Mahalliy usulda (Navi)": "Ташкентский 122",
    "1 ga hosil (tonna)": 0.6,
    "1 ga daromad (so'm)": 12000000,
    "15 sotix hosil (tonna)": 0.1,
    "15 sotix daromad (so'm)": 1800000,
    "10 sotix hosil (tonna)": 0.1,
    "10 sotix daromad (so'm)": 1200000,
    "Yangi usulda (Yangi nav nomi)": "Yangi nav (Intensiv)",
    "Yangi usul 1 ga hosil (tonna)": 1.2,
    "Yangi usul 1 ga daromad (so'm)": 24000000,
    "Yangi usul 15 sotix hosil (tonna)": 0.2,
    "Yangi usul 15 sotix daromad (so'm)": 3600000,
    "Yangi usul 10 sotix hosil (tonna)": 0.1,
    "Yangi usul 10 sotix daromad (so'm)": 2400000,
    "Narx (so'm/kg)": 20000
  },
  {
    "№": 18,
    "Mahsulot nomi": "Kungaboqar",
    "Mahalliy usulda (Navi)": "Армавирский 3497",
    "1 ga hosil (tonna)": 2.0,
    "1 ga daromad (so'm)": 12000000,
    "15 sotix hosil (tonna)": 0.3,
    "15 sotix daromad (so'm)": 1800000,
    "10 sotix hosil (tonna)": 0.2,
    "10 sotix daromad (so'm)": 1200000,
    "Yangi usulda (Yangi nav nomi)": "Yangi nav (Intensiv)",
    "Yangi usul 1 ga hosil (tonna)": 3.5,
    "Yangi usul 1 ga daromad (so'm)": 21000000,
    "Yangi usul 15 sotix hosil (tonna)": 0.5,
    "Yangi usul 15 sotix daromad (so'm)": 3150000,
    "Yangi usul 10 sotix hosil (tonna)": 0.4,
    "Yangi usul 10 sotix daromad (so'm)": 2100000,
    "Narx (so'm/kg)": 6000
  },
  {
    "№": 19,
    "Mahsulot nomi": "No'xat",
    "Mahalliy usulda (Navi)": "Узбекский 32",
    "1 ga hosil (tonna)": 1.5,
    "1 ga daromad (so'm)": 18000000,
    "15 sotix hosil (tonna)": 0.2,
    "15 sotix daromad (so'm)": 2700000,
    "10 sotix hosil (tonna)": 0.2,
    "10 sotix daromad (so'm)": 1800000,
    "Yangi usulda (Yangi nav nomi)": "Yangi nav (Intensiv)",
    "Yangi usul 1 ga hosil (tonna)": 2.5,
    "Yangi usul 1 ga daromad (so'm)": 30000000,
    "Yangi usul 15 sotix hosil (tonna)": 0.4,
    "Yangi usul 15 sotix daromad (so'm)": 4500000,
    "Yangi usul 10 sotix hosil (tonna)": 0.3,
    "Yangi usul 10 sotix daromad (so'm)": 3000000,
    "Narx (so'm/kg)": 12000
  },
  {
    "№": 20,
    "Mahsulot nomi": "Mosh",
    "Mahalliy usulda (Navi)": "Mahalliy",
    "1 ga hosil (tonna)": 1.2,
    "1 ga daromad (so'm)": 16800000,
    "15 sotix hosil (tonna)": 0.2,
    "15 sotix daromad (so'm)": 2520000,
    "10 sotix hosil (tonna)": 0.1,
    "10 sotix daromad (so'm)": 1680000,
    "Yangi usulda (Yangi nav nomi)": "Yangi nav (Intensiv)",
    "Yangi usul 1 ga hosil (tonna)": 2.0,
    "Yangi usul 1 ga daromad (so'm)": 28000000,
    "Yangi usul 15 sotix hosil (tonna)": 0.3,
    "Yangi usul 15 sotix daromad (so'm)": 4200000,
    "Yangi usul 10 sotix hosil (tonna)": 0.2,
    "Yangi usul 10 sotix daromad (so'm)": 2800000,
    "Narx (so'm/kg)": 14000
  },
  {
    "№": 21,
    "Mahsulot nomi": "Lobiya",
    "Mahalliy usulda (Navi)": "Mahalliy",
    "1 ga hosil (tonna)": 1.5,
    "1 ga daromad (so'm)": 18000000,
    "15 sotix hosil (tonna)": 0.2,
    "15 sotix daromad (so'm)": 2700000,
    "10 sotix hosil (tonna)": 0.2,
    "10 sotix daromad (so'm)": 1800000,
    "Yangi usulda (Yangi nav nomi)": "Yangi nav (Intensiv)",
    "Yangi usul 1 ga hosil (tonna)": 2.5,
    "Yangi usul 1 ga daromad (so'm)": 30000000,
    "Yangi usul 15 sotix hosil (tonna)": 0.4,
    "Yangi usul 15 sotix daromad (so'm)": 4500000,
    "Yangi usul 10 sotix hosil (tonna)": 0.3,
    "Yangi usul 10 sotix daromad (so'm)": 3000000,
    "Narx (so'm/kg)": 12000
  },
  {
    "№": 22,
    "Mahsulot nomi": "Fasol",
    "Mahalliy usulda (Navi)": "Mahalliy",
    "1 ga hosil (tonna)": 1.5,
    "1 ga daromad (so'm)": 21000000,
    "15 sotix hosil (tonna)": 0.2,
    "15 sotix daromad (so'm)": 3150000,
    "10 sotix hosil (tonna)": 0.2,
    "10 sotix daromad (so'm)": 2100000,
    "Yangi usulda (Yangi nav nomi)": "Yangi nav (Intensiv)",
    "Yangi usul 1 ga hosil (tonna)": 2.5,
    "Yangi usul 1 ga daromad (so'm)": 35000000,
    "Yangi usul 15 sotix hosil (tonna)": 0.4,
    "Yangi usul 15 sotix daromad (so'm)": 5250000,
    "Yangi usul 10 sotix hosil (tonna)": 0.3,
    "Yangi usul 10 sotix daromad (so'm)": 3500000,
    "Narx (so'm/kg)": 14000
  },
  {
    "№": 23,
    "Mahsulot nomi": "Yeryong'oq",
    "Mahalliy usulda (Navi)": "Mahalliy",
    "1 ga hosil (tonna)": 2.5,
    "1 ga daromad (so'm)": 37500000,
    "15 sotix hosil (tonna)": 0.4,
    "15 sotix daromad (so'm)": 5625000,
    "10 sotix hosil (tonna)": 0.3,
    "10 sotix daromad (so'm)": 3750000,
    "Yangi usulda (Yangi nav nomi)": "Yangi nav (Intensiv)",
    "Yangi usul 1 ga hosil (tonna)": 4.0,
    "Yangi usul 1 ga daromad (so'm)": 60000000,
    "Yangi usul 15 sotix hosil (tonna)": 0.6,
    "Yangi usul 15 sotix daromad (so'm)": 9000000,
    "Yangi usul 10 sotix hosil (tonna)": 0.4,
    "Yangi usul 10 sotix daromad (so'm)": 6000000,
    "Narx (so'm/kg)": 15000
  },
  {
    "№": 24,
    "Mahsulot nomi": "Sholi",
    "Mahalliy usulda (Navi)": "Авангард",
    "1 ga hosil (tonna)": 5.0,
    "1 ga daromad (so'm)": 25000000,
    "15 sotix hosil (tonna)": 0.8,
    "15 sotix daromad (so'm)": 3750000,
    "10 sotix hosil (tonna)": 0.5,
    "10 sotix daromad (so'm)": 2500000,
    "Yangi usulda (Yangi nav nomi)": "Лазурный",
    "Yangi usul 1 ga hosil (tonna)": 8.0,
    "Yangi usul 1 ga daromad (so'm)": 40000000,
    "Yangi usul 15 sotix hosil (tonna)": 1.2,
    "Yangi usul 15 sotix daromad (so'm)": 6000000,
    "Yangi usul 10 sotix hosil (tonna)": 0.8,
    "Yangi usul 10 sotix daromad (so'm)": 4000000,
    "Narx (so'm/kg)": 5000
  }
];

// Sabzavotlar Excel shablonini yuklab olish
export const downloadCropsSampleExcel = () => {
  const ws = XLSX.utils.json_to_sheet(CROPS_EXCEL_TEMPLATE);
  const wb = XLSX.utils.book_new();
  XLSX.utils.book_append_sheet(wb, ws, "Ekinlar_Daromad_Jadvali");
  XLSX.writeFile(wb, "Sabzavot_va_Ekinlar_Daromad_Shabloni.xlsx");
};

// Sabzavotlar Excel faylini o'qish (parse)
export const parseUploadedCropsExcel = (file) => {
  return new Promise((resolve, reject) => {
    const reader = new FileReader();

    reader.onload = (e) => {
      try {
        const data = new Uint8Array(e.target.result);
        const workbook = XLSX.read(data, { type: 'array' });
        const firstSheetName = workbook.SheetNames[0];
        const worksheet = workbook.Sheets[firstSheetName];
        const jsonRows = XLSX.utils.sheet_to_json(worksheet);

        if (!jsonRows || jsonRows.length === 0) {
          throw new Error("Excel faylda ekinlar ma'lumoti topilmadi!");
        }

        const parsedCrops = jsonRows.map((row, index) => {
          const getVal = (keys, fallback = "") => {
            const foundKey = Object.keys(row).find(k => 
              keys.some(search => k.toLowerCase().includes(search.toLowerCase()))
            );
            return foundKey ? row[foundKey] : fallback;
          };

          const name = String(getVal(["mahsulot", "nomi", "ekin", "sabzavot"], `Ekin #${index + 1}`));
          const localVariety = String(getVal(["mahalliy usulda", "navi", "nav nomi"], "Mahalliy nav"));
          const rawYield = getVal(["hosildorlik", "1 ga hosil", "hosil"], 25);
          const localYield = typeof rawYield === 'number' ? `${rawYield} t/ga` : String(rawYield).includes('t') ? String(rawYield) : `${rawYield} t/ga`;
          
          const rawPrice = getVal(["bozor bahosi", "narx", "narxi", "som/kg"], 4000);
          const priceStr = typeof rawPrice === 'number' ? `${rawPrice.toLocaleString()} so'm/kg` : String(rawPrice).includes('so') ? String(rawPrice) : `${rawPrice} so'm/kg`;
          
          const moisture = String(getVal(["namlik", "optimal namlik"], "65% - 75%"));
          const irrigation = String(getVal(["sug'orish", "sugorish", "suv"], "Har 5-7 kunda"));
          const districts = String(getVal(["mos tumanlar", "tavsiya", "tuman"], "Pop, Mingbuloq, Chust, Namangan t."));

          const rawProfit = getVal(["kutilayotgan daromad", "sof daromad", "daromad", "foyda"], 52.5);
          let profitFormatted = "+52.5 mln so'm";
          if (typeof rawProfit === 'number') {
            if (rawProfit > 1000000) {
              profitFormatted = `+${(rawProfit / 1000000).toFixed(1)} mln so'm`;
            } else {
              profitFormatted = `+${rawProfit.toFixed(1)} mln so'm`;
            }
          } else {
            profitFormatted = String(rawProfit).startsWith('+') ? String(rawProfit) : `+${rawProfit}`;
            if (!profitFormatted.includes("so'm") && !profitFormatted.includes("som")) {
              profitFormatted += " so'm";
            }
          }

          const localRevenue = parseFloat(getVal(["1 ga daromad", "daromad"], 60000000)) || 60000000;
          const revenue15Sotix = parseFloat(getVal(["15 sotix daromad"], localRevenue * 0.15)) || (localRevenue * 0.15);
          const revenue10Sotix = parseFloat(getVal(["10 sotix daromad"], localRevenue * 0.1)) || (localRevenue * 0.1);

          const newVariety = String(getVal(["yangi usulda", "yangi nav"], "Intensiv / gibrid nav"));
          const newYieldVal = parseFloat(getVal(["yangi usul 1 ga hosil", "yangi usul hosil"], 35)) || 35;
          const newRevenue = parseFloat(getVal(["yangi usul 1 ga daromad", "yangi usul daromad"], localRevenue * 1.5)) || (localRevenue * 1.5);
          const newRev15Sotix = parseFloat(getVal(["yangi usul 15 sotix daromad"], newRevenue * 0.15)) || (newRevenue * 0.15);
          const newRev10Sotix = parseFloat(getVal(["yangi usul 10 sotix daromad"], newRevenue * 0.1)) || (newRevenue * 0.1);

          const lowerName = name.toLowerCase();
          const icon = lowerName.includes("sholg'om") || lowerName.includes("sholgom") ? "🥦" :
                       lowerName.includes("turp") ? "🥕" :
                       lowerName.includes("karam") && !lowerName.includes("brok") ? "🥬" :
                       lowerName.includes("brok") ? "🥦" :
                       lowerName.includes("kolrabi") ? "🥦" :
                       lowerName.includes("baqlajon") ? "🍆" :
                       lowerName.includes("qalampir") ? "🫑" :
                       lowerName.includes("sabzi") ? "🥕" :
                       lowerName.includes("kartoshka") ? "🥔" :
                       lowerName.includes("pomidor") ? "🍅" :
                       lowerName.includes("bodring") ? "🥒" :
                       lowerName.includes("piyoz") ? "🧅" :
                       lowerName.includes("sarimsoq") ? "🧄" :
                       lowerName.includes("makkajo") ? "🌽" :
                       lowerName.includes("tarvuz") ? "🍉" :
                       lowerName.includes("qovun") ? "🍈" :
                       lowerName.includes("sholi") ? "🌾" :
                       lowerName.includes("mosh") || lowerName.includes("noxat") || lowerName.includes("lobiya") || lowerName.includes("fasol") ? "🌱" : "🥦";

          return {
            id: `crop-${index + 1}-${Date.now()}`,
            name: name,
            localVariety: localVariety,
            avgYieldPerHa: localYield,
            localYield: localYield,
            marketPricePerKg: priceStr,
            pricePerKg: priceStr,
            optimalMoisture: moisture,
            irrigationFreq: irrigation,
            bestDistricts: districts,
            avgProfitPer50Sotix: profitFormatted,
            localRevenue: localRevenue,
            revenue15Sotix: revenue15Sotix,
            revenue10Sotix: revenue10Sotix,
            newVariety: newVariety,
            newYield: `${newYieldVal} tonna/ga`,
            newRevenue: newRevenue,
            newRev15Sotix: newRev15Sotix,
            newRev10Sotix: newRev10Sotix,
            icon: icon
          };
        });

        resolve(parsedCrops);
      } catch (err) {
        reject(err);
      }
    };

    reader.onerror = (err) => reject(err);
    reader.readAsArrayBuffer(file);
  });
};
