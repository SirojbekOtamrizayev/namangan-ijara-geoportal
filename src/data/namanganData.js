// Namangan viloyati 14 ta tuman va shaharlari bo'yicha aholiga ajratilgan ijara yerlar ma'lumotlar bazasi

export const NAMANGAN_CENTER = [40.9983, 71.6726];
export const DEFAULT_ZOOM = 10;

export const DISTRICTS_DATA = [
  {
    number: 1,
    id: "namangan-shahri",
    name: "Namangan shahri",
    shortName: "Namangan sh.",
    type: "shahar",
    center: [40.9983, 71.6726],
    zoom: 13,
    totalLeaseAreaHa: 1850,
    poorFamiliesCount: 1420,
    totalMFYCount: 78,
    activeContracts: 1380,
    color: "#2563eb",
    badgeColor: "from-blue-600 to-blue-500",
    description: "Viloyat ma'muriy markazi. Shahar atrofi issiqxonalari, limonariya va sabzavot-poliz ekinlari yerlari.",
    svgPath: "M 270 240 Q 320 225 350 245 Q 360 275 320 285 Q 275 280 270 240 Z",
    pinPos: { x: 310, y: 260 },
    mfys: [
      {
        id: "nam-yuksalish",
        name: "Yuksalish MFY",
        specialization: "Issiqxonachilik va Sabzavot",
        leaseAreaHa: 95,
        poorFamilies: 85,
        center: [40.9750, 71.6420],
        parcels: [
          {
            id: "NSH-YUK-01",
            contourNumber: "12-kontur",
            farmerName: "Qosimov Bobur Mirzayevich",
            familyStatus: "Temir daftar (yosh oila)",
            familyMembers: 4,
            allocatedAreaHa: 0.25,
            contractYear: "2024 - 2034 (10 yil)",
            coordinates: [40.9760, 71.6435],
            specialization: "Issiqxona sabzavotlari va rezavorlar",
            polygon: [
              [40.9750, 71.6420],
              [40.9770, 71.6425],
              [40.9765, 71.6450],
              [40.9745, 71.6445]
            ],
            soil: {
              type: "Madaniy sug'oriladigan o'tloqi tuproq",
              bonitetScore: 78,
              moisture: "75% (Yuqori namlik)",
              salinity: "Sho'rlanmagan",
              groundwaterDepth: "1.6 metr",
              waterSource: "Shahar sug'orish tizimi (Shimoliy kanal)"
            },
            recommendation: {
              primaryCrop: "Issiqxona Qulupnayi va Pomidor",
              secondaryCrop: "Ko'katlar (kashnich, ukrop, salat bargi)",
              rationale: "Shahar bozoriga juda yaqin. Yangi uzilgan sabzavot va qulupnay eng yuqori baholanadi.",
              cycleMonths: "Butun yil davomida (Issiqxona)"
            },
            economics: {
              expensesUzs: 9500000,
              expectedYield: "3.5 tonna qulupnay + 2 tonna pomidor",
              grossRevenueUzs: 58000000,
              netProfitUzs: 48500000,
              paybackMonths: 3
            }
          }
        ]
      },
      {
        id: "nam-sihatgoh",
        name: "Sihatgoh MFY",
        specialization: "Gulchilik va Limonariya",
        leaseAreaHa: 80,
        poorFamilies: 72,
        center: [40.9850, 71.6580],
        parcels: [
          {
            id: "NSH-SIH-01",
            contourNumber: "28-kontur",
            farmerName: "Valiyev Sherali Odilovich",
            familyStatus: "Ijtimoiy reyestr",
            familyMembers: 5,
            allocatedAreaHa: 0.3,
            contractYear: "2024 - 2034 (10 yil)",
            coordinates: [40.9860, 71.6590],
            specialization: "Limonariya va manzarali gulchilik",
            polygon: [
              [40.9845, 71.6570],
              [40.9870, 71.6580],
              [40.9865, 71.6610],
              [40.9840, 71.6600]
            ],
            soil: {
              type: "Gumusga boy unumdor bo'z tuproq",
              bonitetScore: 76,
              moisture: "72% (Optimal)",
              salinity: "Sho'rlanmagan",
              groundwaterDepth: "1.8 metr",
              waterSource: "Shahar ichki sug'orish arig'i"
            },
            recommendation: {
              primaryCrop: "Limon va Bodring (Issiqxonada)",
              secondaryCrop: "Rayhon va ko'katlar",
              rationale: "Mikroiqlim himoyalangan, shahar aholisi uchun har doim xaridorgir.",
              cycleMonths: "To'rt fasl davomida"
            },
            economics: {
              expensesUzs: 8200000,
              expectedYield: "4 tonna limon + 3 tonna bodring",
              grossRevenueUzs: 51000000,
              netProfitUzs: 42800000,
              paybackMonths: 3.5
            }
          }
        ]
      },
      {
        id: "nam-afsona",
        name: "Afsona MFY",
        specialization: "Erta pishar Sabzavotchilik",
        leaseAreaHa: 75,
        poorFamilies: 65,
        center: [41.0100, 71.6850],
        parcels: [
          {
            id: "NSH-AFS-01",
            contourNumber: "41-kontur",
            farmerName: "Ahmedova Sayyora Rustamovna",
            familyStatus: "Ayollar daftari",
            familyMembers: 4,
            allocatedAreaHa: 0.25,
            contractYear: "2023 - 2033 (10 yil)",
            coordinates: [41.0110, 71.6865],
            specialization: "Sabzavot va poliz ekinlari",
            polygon: [
              [41.0095, 71.6850],
              [41.0120, 71.6855],
              [41.0115, 71.6880],
              [41.0090, 71.6875]
            ],
            soil: {
              type: "O'tloqi bo'z tuproq",
              bonitetScore: 74,
              moisture: "70% (Yaxshi ta'minlangan)",
              salinity: "Sho'rlanmagan",
              groundwaterDepth: "2.0 metr",
              waterSource: "Ariq suvi"
            },
            recommendation: {
              primaryCrop: "Pomidor, Baqlajon va Bolgarskiy",
              secondaryCrop: "Kuzgi sabzi",
              rationale: "Shahar bozoriga to'g'ridan-to'g'ri topshirish orqali yuqori daromad ta'minlanadi.",
              cycleMonths: "Aprel - Noyabr"
            },
            economics: {
              expensesUzs: 6800000,
              expectedYield: "8.5 tonna sabzavotlar",
              grossRevenueUzs: 44000000,
              netProfitUzs: 37200000,
              paybackMonths: 3
            }
          }
        ]
      }
    ]
  },
  {
    number: 2,
    id: "yangi-namangan",
    name: "Yangi Namangan tumani",
    shortName: "Yangi Namangan",
    type: "tuman",
    center: [41.0250, 71.6500],
    zoom: 13,
    totalLeaseAreaHa: 1350,
    poorFamiliesCount: 1120,
    totalMFYCount: 32,
    activeContracts: 1090,
    color: "#16a34a",
    badgeColor: "from-emerald-600 to-green-500",
    description: "Yangi zamonaviy tuman. Sabzavotchilik, parhez ekinlar va ko'chatchilik agrofirmalari markazi.",
    svgPath: "M 250 190 Q 290 180 320 200 Q 300 230 260 220 Z",
    pinPos: { x: 280, y: 205 },
    mfys: [
      {
        id: "yn-mingchinor",
        name: "Mingchinor MFY",
        specialization: "Parhez sabzavotlar va Karam",
        leaseAreaHa: 85,
        poorFamilies: 78,
        center: [41.0320, 71.6410],
        parcels: [
          {
            id: "YNT-MIN-01",
            contourNumber: "19-kontur",
            farmerName: "Saidov Alisher Fayzullayevich",
            familyStatus: "Ijtimoiy himoya reyestrida (ko'p bolali)",
            familyMembers: 7,
            allocatedAreaHa: 0.3,
            contractYear: "2024 - 2034 (10 yil)",
            coordinates: [41.0335, 71.6425],
            specialization: "Gulkaram, Brokkoli va Karam",
            polygon: [
              [41.0325, 71.6410],
              [41.0345, 71.6415],
              [41.0340, 71.6440],
              [41.0320, 71.6435]
            ],
            soil: {
              type: "Tipik bo'z tuproq",
              bonitetScore: 74,
              moisture: "68% (Me'yorda)",
              salinity: "Sho'rlanmagan",
              groundwaterDepth: "2.1 metr",
              waterSource: "Ariq suvi (Nasos ko'magida)"
            },
            recommendation: {
              primaryCrop: "Gulkaram va Brokkoli",
              secondaryCrop: "Turp, Sholg'om va Ko'kat",
              rationale: "Parhez sabzavotlar bozorlarda qimmat narxda sotiladi, vegetatsiya davri qisqa.",
              cycleMonths: "Mart - Iyun, Avgust - Oktyabr"
            },
            economics: {
              expensesUzs: 4800000,
              expectedYield: "7 tonna gulkaram/brokkoli",
              grossRevenueUzs: 32000000,
              netProfitUzs: 27200000,
              paybackMonths: 3.5
            }
          }
        ]
      },
      {
        id: "yn-mehnatobod",
        name: "Mehnatobod MFY",
        specialization: "Ertapishar Qizil Sabzi",
        leaseAreaHa: 90,
        poorFamilies: 82,
        center: [41.0420, 71.6350],
        parcels: [
          {
            id: "YNT-MEH-01",
            contourNumber: "32-kontur",
            farmerName: "Normatov Bahodir Jo'rayevich",
            familyStatus: "Temir daftar",
            familyMembers: 5,
            allocatedAreaHa: 0.4,
            contractYear: "2024 - 2034 (10 yil)",
            coordinates: [41.0430, 71.6360],
            specialization: "Sabzi va Oshqovoq",
            polygon: [
              [41.0415, 71.6345],
              [41.0440, 71.6350],
              [41.0435, 71.6380],
              [41.0410, 71.6375]
            ],
            soil: {
              type: "Yengil qumloq unumdor tuproq",
              bonitetScore: 75,
              moisture: "70% (Yaxshi namlik)",
              salinity: "Sho'rlanmagan",
              groundwaterDepth: "2.0 metr",
              waterSource: "Shimoliy Farg'ona kanali tarmog'i"
            },
            recommendation: {
              primaryCrop: "Ertapishar Qizil Sabzi",
              secondaryCrop: "Mosh va Oshqovoq",
              rationale: "Qumloq tuproqda sabzi to'g'ri va shirin o'sadi, yig'ib olish oson.",
              cycleMonths: "Mart - Iyul, Avgust - Oktyabr"
            },
            economics: {
              expensesUzs: 5400000,
              expectedYield: "12 tonna sabzi + 400 kg mosh",
              grossRevenueUzs: 38000000,
              netProfitUzs: 32600000,
              paybackMonths: 3.5
            }
          }
        ]
      }
    ]
  },
  {
    number: 3,
    id: "davlatobod",
    name: "Davlatobod tumani",
    shortName: "Davlatobod",
    type: "tuman",
    center: [40.9850, 71.6250],
    zoom: 13,
    totalLeaseAreaHa: 1180,
    poorFamiliesCount: 980,
    totalMFYCount: 28,
    activeContracts: 940,
    color: "#ea580c",
    badgeColor: "from-orange-600 to-amber-500",
    description: "Namangan gullar shahrining gulchilik va issiqxona klasterlari rivojlangan tumani.",
    svgPath: "M 325 285 Q 375 280 395 320 Q 355 355 330 330 Z",
    pinPos: { x: 355, y: 315 },
    mfys: [
      {
        id: "dav-oromgoh",
        name: "Oromgoh MFY",
        specialization: "Gulchilik va Limonariya",
        leaseAreaHa: 70,
        poorFamilies: 62,
        center: [40.9890, 71.6180],
        parcels: [
          {
            id: "DAV-ORO-01",
            contourNumber: "45-kontur",
            farmerName: "Rahmonov Sanjarbek Ravshanovich",
            familyStatus: "Yoshlar daftari",
            familyMembers: 3,
            allocatedAreaHa: 0.25,
            contractYear: "2024 - 2034 (10 yil)",
            coordinates: [40.9902, 71.6195],
            specialization: "Atirgul, Lolalar va Limon",
            polygon: [
              [40.9892, 71.6180],
              [40.9912, 71.6185],
              [40.9908, 71.6210],
              [40.9888, 71.6205]
            ],
            soil: {
              type: "O'tloqi-bo'z tuproq",
              bonitetScore: 71,
              moisture: "65% (Optimal)",
              salinity: "Sho'rlanmagan",
              groundwaterDepth: "2.3 metr",
              waterSource: "Soy suvi"
            },
            recommendation: {
              primaryCrop: "Gulchilik (Atirgul va lola ko'chatlari)",
              secondaryCrop: "Limonariya (yengil issiqxona)",
              rationale: "Gullar festivali va shahar ehtiyoji uchun eng yuqori daromadli soha.",
              cycleMonths: "Butun mavsum"
            },
            economics: {
              expensesUzs: 7500000,
              expectedYield: "18 000 dona atirgul/dasta gullar",
              grossRevenueUzs: 54000000,
              netProfitUzs: 46500000,
              paybackMonths: 3
            }
          }
        ]
      },
      {
        id: "dav-yangitong",
        name: "Yangi tong MFY",
        specialization: "Bodring va Pomidor Issiqxonasi",
        leaseAreaHa: 65,
        poorFamilies: 58,
        center: [40.9810, 71.6120],
        parcels: [
          {
            id: "DAV-YAN-01",
            contourNumber: "15-kontur",
            farmerName: "Karimova Ziyoda Ergashovna",
            familyStatus: "Ayollar daftari",
            familyMembers: 4,
            allocatedAreaHa: 0.2,
            contractYear: "2024 - 2034 (10 yil)",
            coordinates: [40.9820, 71.6130],
            specialization: "Issiqxona sabzavotlari",
            polygon: [
              [40.9805, 71.6115],
              [40.9825, 71.6120],
              [40.9820, 71.6145],
              [40.9800, 71.6140]
            ],
            soil: {
              type: "Yumshoq unumdor tuproq",
              bonitetScore: 73,
              moisture: "68%",
              salinity: "Sho'rlanmagan",
              groundwaterDepth: "2.1 metr",
              waterSource: "Quvur orqali suv"
            },
            recommendation: {
              primaryCrop: "Gollandiya navli Bodring va Pomidor",
              secondaryCrop: "Ko'katlar",
              rationale: "Yuqori hosildor navlar shahar do'konlariga kunlik sotiladi.",
              cycleMonths: "Fevral - Iyun, Avgust - Dekabr"
            },
            economics: {
              expensesUzs: 6200000,
              expectedYield: "6 tonna bodring + 4 tonna pomidor",
              grossRevenueUzs: 45000000,
              netProfitUzs: 38800000,
              paybackMonths: 3
            }
          }
        ]
      }
    ]
  },
  {
    number: 4,
    id: "pop",
    name: "Pop tumani",
    shortName: "Pop",
    type: "tuman",
    center: [40.8736, 71.1092],
    zoom: 11,
    totalLeaseAreaHa: 5200,
    poorFamiliesCount: 3950,
    totalMFYCount: 48,
    activeContracts: 3840,
    color: "#7c3aed",
    badgeColor: "from-purple-600 to-indigo-500",
    description: "Viloyatning eng katta hududga ega tumani. Poliz, mosh, paxta-g'alla va adir bog'dorchiligi rivojlangan.",
    svgPath: "M 300 290 Q 340 290 330 350 Q 290 355 285 305 Z",
    pinPos: { x: 305, y: 325 },
    mfys: [
      {
        id: "pop-guzar",
        name: "G'urumsaroy MFY",
        specialization: "Poliz va Eksportbop Mosh",
        leaseAreaHa: 185,
        poorFamilies: 142,
        center: [40.8920, 71.0850],
        parcels: [
          {
            id: "POP-GUR-01",
            contourNumber: "142-kontur",
            farmerName: "Rustamov Jamshid Qodirovich",
            familyStatus: "Ijtimoiy himoya reyestrida",
            familyMembers: 5,
            allocatedAreaHa: 0.5,
            contractYear: "2024 - 2034 (10 yil)",
            coordinates: [40.8945, 71.0820],
            specialization: "Polizchilik (Tarvuz, Qovun) va Dukkakli",
            polygon: [
              [40.8935, 71.0805],
              [40.8955, 71.0810],
              [40.8950, 71.0838],
              [40.8930, 71.0832]
            ],
            soil: {
              type: "Qumloq-bo'z tuproq",
              bonitetScore: 64,
              moisture: "58% (O'rtacha namlik)",
              salinity: "Kuchsiz sho'rlangan (yuvilgan)",
              groundwaterDepth: "2.2 metr",
              waterSource: "Shimoliy Farg'ona kanali (Ariq orqali oqim suv)"
            },
            recommendation: {
              primaryCrop: "Mosh va Qovun/Tarvuz",
              secondaryCrop: "Kuzgi sarimsoqpiyoz",
              rationale: "Qumloq va quyoshli yer bo'lgani sababli ertapishar poliz ekinlari va dukkakli mosh yuqori hosil beradi.",
              cycleMonths: "Aprel - Iyul (Poliz), Avgust - Oktyabr (Mosh)"
            },
            economics: {
              expensesUzs: 6500000,
              expectedYield: "12 tonna tarvuz + 900 kg mosh",
              grossRevenueUzs: 38000000,
              netProfitUzs: 31500000,
              paybackMonths: 4
            }
          }
        ]
      },
      {
        id: "pop-chorkesar",
        name: "Chorkesar MFY",
        specialization: "Adir uzumchiligi va Bodomzor",
        leaseAreaHa: 210,
        poorFamilies: 165,
        center: [40.9450, 71.0320],
        parcels: [
          {
            id: "POP-CHO-01",
            contourNumber: "88-kontur",
            farmerName: "Tursunov Sherzod Baxtiyorovich",
            familyStatus: "Temir daftar ro'yxatida",
            familyMembers: 6,
            allocatedAreaHa: 0.5,
            contractYear: "2023 - 2033 (10 yil)",
            coordinates: [40.9460, 71.0335],
            specialization: "Kishmish uzum va No'xat",
            polygon: [
              [40.9448, 71.0315],
              [40.9472, 71.0320],
              [40.9468, 71.0355],
              [40.9442, 71.0348]
            ],
            soil: {
              type: "Adir bo'z tuprog'i, toshloq-qumloq",
              bonitetScore: 59,
              moisture: "52% (Qo'shimcha sug'orish talab etiladi)",
              salinity: "Sho'rlanmagan",
              groundwaterDepth: "4.5 metr",
              waterSource: "Tomchilatib sug'orish hovuzi (Artezian quduq)"
            },
            recommendation: {
              primaryCrop: "Uzum (Kishmish) va Bodom ko'chatlari",
              secondaryCrop: "Qator oralariga mosh va no'xat",
              rationale: "Adir relyefiga uzum va bodom eng chidamli bo'lib, tomchilatib sug'orishda juda yuqori rentabellik beradi.",
              cycleMonths: "Muntazam hosil"
            },
            economics: {
              expensesUzs: 8000000,
              expectedYield: "4 tonna uzum + 400 kg dukkakli",
              grossRevenueUzs: 45000000,
              netProfitUzs: 37000000,
              paybackMonths: 6
            }
          }
        ]
      },
      {
        id: "pop-sang",
        name: "Sang MFY",
        specialization: "Ertapishar Sabzi va Piyoz",
        leaseAreaHa: 195,
        poorFamilies: 150,
        center: [40.8520, 71.1250],
        parcels: [
          {
            id: "POP-SNG-01",
            contourNumber: "102-kontur",
            farmerName: "Qo'chqorov Alijon Valiyevich",
            familyStatus: "Ijtimoiy himoya reyestrida",
            familyMembers: 5,
            allocatedAreaHa: 0.45,
            contractYear: "2024 - 2034 (10 yil)",
            coordinates: [40.8535, 71.1265],
            specialization: "Sabzi va Qizil piyoz",
            polygon: [
              [40.8520, 71.1250],
              [40.8545, 71.1255],
              [40.8540, 71.1285],
              [40.8515, 71.1280]
            ],
            soil: {
              type: "Sug'oriladigan bo'z tuproq",
              bonitetScore: 65,
              moisture: "62% (Me'yorda)",
              salinity: "Kuchsiz yuvilgan",
              groundwaterDepth: "2.4 metr",
              waterSource: "Sirdaryo kanali"
            },
            recommendation: {
              primaryCrop: "Ertapishar Sariq va Qizil Sabzi",
              secondaryCrop: "Kuzgi piyoz",
              rationale: "Sabzi hosildorligi yuqori va saqlashga chidamli.",
              cycleMonths: "Mart - Iyul, Avgust - Oktyabr"
            },
            economics: {
              expensesUzs: 5500000,
              expectedYield: "13 tonna sabzi",
              grossRevenueUzs: 36000000,
              netProfitUzs: 30500000,
              paybackMonths: 3.5
            }
          }
        ]
      }
    ]
  },
  {
    number: 5,
    id: "chust",
    name: "Chust tumani",
    shortName: "Chust",
    type: "tuman",
    center: [41.0069, 71.2294],
    zoom: 11,
    totalLeaseAreaHa: 4100,
    poorFamiliesCount: 3250,
    totalMFYCount: 65,
    activeContracts: 3140,
    color: "#0d9488",
    badgeColor: "from-teal-600 to-cyan-500",
    description: "Mashhur Chust qalampiri, danakli mevalar, yong'oqzorlar va sabzavotchilik makoni.",
    svgPath: "M 150 170 Q 210 160 215 220 Q 185 260 145 225 Z",
    pinPos: { x: 180, y: 205 },
    mfys: [
      {
        id: "chust-ogasaroy",
        name: "O'g'asaroy MFY",
        specialization: "Chust Qalampiri va Sabzi",
        leaseAreaHa: 145,
        poorFamilies: 120,
        center: [41.0250, 71.2180],
        parcels: [
          {
            id: "CHU-OGA-01",
            contourNumber: "56-kontur",
            farmerName: "Ismoilov Otabek Shokirovich",
            familyStatus: "Kam ta'minlangan yosh oila",
            familyMembers: 4,
            allocatedAreaHa: 0.4,
            contractYear: "2024 - 2034 (10 yil)",
            coordinates: [41.0265, 71.2195],
            specialization: "Achchiq qalampir va Sabzi",
            polygon: [
              [41.0252, 71.2180],
              [41.0275, 71.2185],
              [41.0270, 71.2212],
              [41.0248, 71.2205]
            ],
            soil: {
              type: "Tipik bo'z tuproq",
              bonitetScore: 72,
              moisture: "66% (Yuqori namlik)",
              salinity: "Sho'rlanmagan",
              groundwaterDepth: "2.8 metr",
              waterSource: "Chustsoy arig'i (Kafolatlangan oqim)"
            },
            recommendation: {
              primaryCrop: "Chust achchiq qalampiri va Sabzi",
              secondaryCrop: "Kuzgi karam",
              rationale: "Tuproqda mikroelementlar boy, o'tkir ta'mli Chust qalampiri eksportbop hisoblanadi.",
              cycleMonths: "Aprel - Oktyabr"
            },
            economics: {
              expensesUzs: 5800000,
              expectedYield: "6.8 tonna qalampir + 4 tonna sabzi",
              grossRevenueUzs: 42000000,
              netProfitUzs: 36200000,
              paybackMonths: 4
            }
          }
        ]
      },
      {
        id: "chust-varzik",
        name: "Varzik MFY",
        specialization: "Tog' Olxo'risi va Kartoshka",
        leaseAreaHa: 190,
        poorFamilies: 155,
        center: [41.0820, 71.2550],
        parcels: [
          {
            id: "CHU-VAR-01",
            contourNumber: "21-kontur",
            farmerName: "Yuldasheva Dilnoza Axmedovna",
            familyStatus: "Nogironligi bor a'zosi mavjud oila",
            familyMembers: 5,
            allocatedAreaHa: 0.3,
            contractYear: "2024 - 2034 (10 yil)",
            coordinates: [41.0835, 71.2560],
            specialization: "Olxo'ri, Kartoshka va Sarimsoq",
            polygon: [
              [41.0825, 71.2545],
              [41.0845, 71.2550],
              [41.0840, 71.2575],
              [41.0820, 71.2570]
            ],
            soil: {
              type: "Unumdor tog' oldi bo'z tuprog'i",
              bonitetScore: 75,
              moisture: "70% (Optimal namlik)",
              salinity: "Sho'rlanmagan",
              groundwaterDepth: "3.2 metr",
              waterSource: "Buloq suvi va Varzik soyi"
            },
            recommendation: {
              primaryCrop: "Olxo'ri (Qora olxo'ri) va Kartoshka",
              secondaryCrop: "Sarimsoqpiyoz",
              rationale: "Quritishbop olxo'ri va erta pishar kartoshka xonadonga barqaror yuqori daromad keltiradi.",
              cycleMonths: "Mavsumiy"
            },
            economics: {
              expensesUzs: 4900000,
              expectedYield: "8 tonna kartoshka + mevalar",
              grossRevenueUzs: 36000000,
              netProfitUzs: 31100000,
              paybackMonths: 3.8
            }
          }
        ]
      },
      {
        id: "chust-gova",
        name: "G'ova MFY",
        specialization: "Dukkakli Loviya va Yong'oq",
        leaseAreaHa: 170,
        poorFamilies: 135,
        center: [41.1150, 71.2150],
        parcels: [
          {
            id: "CHU-GOV-01",
            contourNumber: "38-kontur",
            farmerName: "Mamatov Dilmurod Ikromovich",
            familyStatus: "Ijtimoiy reyestr",
            familyMembers: 6,
            allocatedAreaHa: 0.45,
            contractYear: "2023 - 2033 (10 yil)",
            coordinates: [41.1165, 71.2165],
            specialization: "Oq loviya va Dorivor o'simliklar",
            polygon: [
              [41.1150, 71.2150],
              [41.1175, 71.2155],
              [41.1170, 71.2185],
              [41.1145, 71.2180]
            ],
            soil: {
              type: "Tog' oldi qoramtir tuproq",
              bonitetScore: 71,
              moisture: "68%",
              salinity: "Sho'rlanmagan",
              groundwaterDepth: "3.5 metr",
              waterSource: "G'ovasoy chashmasi"
            },
            recommendation: {
              primaryCrop: "Eksportbop Loviya va No'xat",
              secondaryCrop: "Kuzgi sarimsoq",
              rationale: "Tog' havosi va mo'l quyosh nuri loviya donining to'liq va yirik pishishini ta'minlaydi.",
              cycleMonths: "Aprel - Sentyabr"
            },
            economics: {
              expensesUzs: 4500000,
              expectedYield: "1.4 tonna loviya + 800 kg no'xat",
              grossRevenueUzs: 34000000,
              netProfitUzs: 29500000,
              paybackMonths: 4
            }
          }
        ]
      }
    ]
  },
  {
    number: 6,
    id: "toraqorgon",
    name: "To'raqo'rg'on tumani",
    shortName: "To'raqo'rg'on",
    type: "tuman",
    center: [41.0022, 71.5125],
    zoom: 12,
    totalLeaseAreaHa: 3100,
    poorFamiliesCount: 2750,
    totalMFYCount: 52,
    activeContracts: 2650,
    color: "#db2777",
    badgeColor: "from-pink-600 to-rose-500",
    description: "Sanoat va intensiv tomorqachilik tutashgan tuman. Yiliga 3 marta sabzavot hosili olinadi.",
    svgPath: "M 160 240 Q 230 230 235 285 Q 185 305 160 265 Z",
    pinPos: { x: 195, y: 265 },
    mfys: [
      {
        id: "tora-shaxand",
        name: "Shohand MFY",
        specialization: "Ertapishar Sabzavotchilik",
        leaseAreaHa: 120,
        poorFamilies: 110,
        center: [40.9850, 71.4920],
        parcels: [
          {
            id: "TOR-SHO-01",
            contourNumber: "34-kontur",
            farmerName: "Karimov Anvar Jo'rayevich",
            familyStatus: "Ishsiz oila boshlig'i, Ijtimoiy daftarda",
            familyMembers: 5,
            allocatedAreaHa: 0.5,
            contractYear: "2024 - 2034 (10 yil)",
            coordinates: [40.9865, 71.4935],
            specialization: "Sabzavotchilik (Sabzi, Baqlajon, Karam)",
            polygon: [
              [40.9855, 71.4920],
              [40.9878, 71.4925],
              [40.9872, 71.4950],
              [40.9850, 71.4945]
            ],
            soil: {
              type: "Sug'oriladigan o'tloqi bo'z tuproq",
              bonitetScore: 76,
              moisture: "72% (Juda yaxshi ta'minlangan)",
              salinity: "Sho'rlanmagan",
              groundwaterDepth: "1.8 metr",
              waterSource: "Katta Farg'ona kanali tarmog'i"
            },
            recommendation: {
              primaryCrop: "Ertapishar Sabzi va Baqlajon",
              secondaryCrop: "Makkajo'xori (don va silos)",
              rationale: "Gumus miqdori yuqori, suv serob. Yilda 2-3 marta hosil olish imkoni mavjud.",
              cycleMonths: "Mart - Iyul, Avgust - Noyabr"
            },
            economics: {
              expensesUzs: 6200000,
              expectedYield: "15 tonna sabzi + 8 tonna silos",
              grossRevenueUzs: 41000000,
              netProfitUzs: 34800000,
              paybackMonths: 3.5
            }
          }
        ]
      },
      {
        id: "tora-yordon",
        name: "Yordon MFY",
        specialization: "Issiqxona Pomidori va Bodring",
        leaseAreaHa: 135,
        poorFamilies: 125,
        center: [41.0150, 71.5320],
        parcels: [
          {
            id: "TOR-YOR-01",
            contourNumber: "51-kontur",
            farmerName: "Sultonov Murodjon Oripovich",
            familyStatus: "Temir daftar",
            familyMembers: 5,
            allocatedAreaHa: 0.35,
            contractYear: "2024 - 2034 (10 yil)",
            coordinates: [41.0165, 71.5335],
            specialization: "Pomidor, Bodring va Shirin qalampir",
            polygon: [
              [41.0150, 71.5320],
              [41.0175, 71.5325],
              [41.0170, 71.5355],
              [41.0145, 71.5350]
            ],
            soil: {
              type: "Sergumus qora bo'z tuproq",
              bonitetScore: 78,
              moisture: "74% (A'lo namlik)",
              salinity: "Sho'rlanmagan",
              groundwaterDepth: "1.7 metr",
              waterSource: "Kosonsoy arig'i"
            },
            recommendation: {
              primaryCrop: "Yangi navli Pushti Pomidor",
              secondaryCrop: "Ko'katlar va rediska",
              rationale: "Pushti pomidorlar ichki bozorda qimmat yuradi, tez yetiladi.",
              cycleMonths: "Mart - Avgust, Sentyabr - Dekabr"
            },
            economics: {
              expensesUzs: 6900000,
              expectedYield: "11 tonna pomidor",
              grossRevenueUzs: 47000000,
              netProfitUzs: 40100000,
              paybackMonths: 3
            }
          }
        ]
      },
      {
        id: "tora-qatagon",
        name: "Qatag'on MFY",
        specialization: "Mosh va Makkajo'xori",
        leaseAreaHa: 110,
        poorFamilies: 98,
        center: [40.9950, 71.4720],
        parcels: [
          {
            id: "TOR-QAT-01",
            contourNumber: "73-kontur",
            farmerName: "Sobirova Gulchehra Ilhomovna",
            familyStatus: "Ayollar daftari",
            familyMembers: 4,
            allocatedAreaHa: 0.4,
            contractYear: "2023 - 2033 (10 yil)",
            coordinates: [40.9960, 71.4735],
            specialization: "Eksportbop mosh va poliz",
            polygon: [
              [40.9945, 71.4720],
              [40.9970, 71.4725],
              [40.9965, 71.4750],
              [40.9940, 71.4745]
            ],
            soil: {
              type: "O'tloqi bo'z tuproq",
              bonitetScore: 73,
              moisture: "70%",
              salinity: "Sho'rlanmagan",
              groundwaterDepth: "1.9 metr",
              waterSource: "Kanal tarmog'i"
            },
            recommendation: {
              primaryCrop: "Yashil Mosh va Shirin Qovun",
              secondaryCrop: "Kuzgi arpa/silos",
              rationale: "Mosh yerga tabiiy azot to'playdi, qo'shimcha mineral o'g'it talab qilmaydi.",
              cycleMonths: "May - Oktyabr"
            },
            economics: {
              expensesUzs: 4800000,
              expectedYield: "900 kg mosh + 8 tonna qovun",
              grossRevenueUzs: 35000000,
              netProfitUzs: 30200000,
              paybackMonths: 4
            }
          }
        ]
      }
    ]
  },
  {
    number: 7,
    id: "namangan-tumani",
    name: "Namangan tumani",
    shortName: "Namangan t.",
    type: "tuman",
    center: [41.0450, 71.7200],
    zoom: 11,
    totalLeaseAreaHa: 3600,
    poorFamiliesCount: 3050,
    totalMFYCount: 54,
    activeContracts: 2980,
    color: "#d97706",
    badgeColor: "from-amber-600 to-yellow-500",
    description: "Viloyat markaziga tutash. Kartoshkachilik, sabzavotchilik va ko'chatchilik agromarkazi.",
    svgPath: "M 180 80 Q 235 60 250 145 Q 200 160 175 110 Z",
    pinPos: { x: 210, y: 115 },
    mfys: [
      {
        id: "namt-toshbuloq",
        name: "Toshbuloq MFY",
        specialization: "Elita Kartoshkachilik va Piyoz",
        leaseAreaHa: 160,
        poorFamilies: 135,
        center: [41.0520, 71.7050],
        parcels: [
          {
            id: "NTM-TOS-01",
            contourNumber: "77-kontur",
            farmerName: "Bekmirzayev Ilhom Komilovich",
            familyStatus: "Ijtimoiy himoya reyestrida",
            familyMembers: 6,
            allocatedAreaHa: 0.5,
            contractYear: "2023 - 2033 (10 yil)",
            coordinates: [41.0535, 71.7065],
            specialization: "Kartoshka va Zarafshon piyozi",
            polygon: [
              [41.0522, 71.7048],
              [41.0548, 71.7055],
              [41.0542, 71.7082],
              [41.0518, 71.7075]
            ],
            soil: {
              type: "Quyuq bo'z tuproq",
              bonitetScore: 77,
              moisture: "70% (Optimal)",
              salinity: "Sho'rlanmagan",
              groundwaterDepth: "2.0 metr",
              waterSource: "Kanal suvi (Toshbuloq tarmog'i)"
            },
            recommendation: {
              primaryCrop: "Super elit kartoshka va Piyoz",
              secondaryCrop: "Kuzgi lavlagi va ko'katlar",
              rationale: "Toshbuloq yerlarining unumdorligi kartoshka uchun viloyatda eng maqbul hisoblanadi.",
              cycleMonths: "Mart - Iyun (Kartoshka), Iyul - Oktyabr (Lavlagi)"
            },
            economics: {
              expensesUzs: 7200000,
              expectedYield: "14 tonna kartoshka + 6 tonna sabzavot",
              grossRevenueUzs: 48000000,
              netProfitUzs: 40800000,
              paybackMonths: 3.5
            }
          }
        ]
      },
      {
        id: "namt-mirishkor",
        name: "Mirishkor MFY",
        specialization: "Karam va Ildizmevalar",
        leaseAreaHa: 140,
        poorFamilies: 118,
        center: [41.0650, 71.7350],
        parcels: [
          {
            id: "NTM-MIR-01",
            contourNumber: "85-kontur",
            farmerName: "Yoqubov Dilshod Mirzayevich",
            familyStatus: "Temir daftar",
            familyMembers: 5,
            allocatedAreaHa: 0.45,
            contractYear: "2024 - 2034 (10 yil)",
            coordinates: [41.0665, 71.7365],
            specialization: "Oqbosh karam va Sabzi",
            polygon: [
              [41.0650, 71.7350],
              [41.0675, 71.7355],
              [41.0670, 71.7385],
              [41.0645, 71.7380]
            ],
            soil: {
              type: "Unumdor allyuvial o'tloqi tuproq",
              bonitetScore: 76,
              moisture: "73% (Juda yaxshi)",
              salinity: "Sho'rlanmagan",
              groundwaterDepth: "1.9 metr",
              waterSource: "Mirishkor kanali"
            },
            recommendation: {
              primaryCrop: "Oqbosh Karam va Sariq Sabzi",
              secondaryCrop: "Kuzgi sarimsoq va rediska",
              rationale: "Tuproqda namlik barqaror saqlanadi, karam boshlari zich va vaznli bo'ladi.",
              cycleMonths: "Aprel - Noyabr"
            },
            economics: {
              expensesUzs: 5900000,
              expectedYield: "16 tonna karam va sabzavot",
              grossRevenueUzs: 42000000,
              netProfitUzs: 36100000,
              paybackMonths: 3.5
            }
          }
        ]
      }
    ]
  },
  {
    number: 8,
    id: "mingbuloq",
    name: "Mingbuloq tumani",
    shortName: "Mingbuloq",
    type: "tuman",
    center: [40.7681, 71.4789],
    zoom: 11,
    totalLeaseAreaHa: 5100,
    poorFamiliesCount: 3890,
    totalMFYCount: 46,
    activeContracts: 3760,
    color: "#6d28d9",
    badgeColor: "from-purple-700 to-indigo-600",
    description: "Sirdaryo qirg'og'i. Sholichilik, poliz, tarvuz va baliqchilik salohiyati yuqori hudud.",
    svgPath: "M 225 140 Q 280 130 280 190 Q 220 200 220 150 Z",
    pinPos: { x: 250, y: 165 },
    mfys: [
      {
        id: "ming-jomashoy",
        name: "Jomasho'y MFY",
        specialization: "Sholichilik va Dukkakli Mosh",
        leaseAreaHa: 230,
        poorFamilies: 180,
        center: [40.7750, 71.4650],
        parcels: [
          {
            id: "MIN-JOM-01",
            contourNumber: "105-kontur",
            farmerName: "Qambarov O'tkir Ne'matovich",
            familyStatus: "Mavsumiy band xonadon",
            familyMembers: 5,
            allocatedAreaHa: 0.6,
            contractYear: "2024 - 2034 (10 yil)",
            coordinates: [40.7765, 71.4670],
            specialization: "Lazer navli sholi va poliz",
            polygon: [
              [40.7752, 71.4652],
              [40.7778, 71.4660],
              [40.7772, 71.4690],
              [40.7748, 71.4682]
            ],
            soil: {
              type: "O'tloqi allyuvial tuproq",
              bonitetScore: 66,
              moisture: "78% (Yuqori namlik, yerosti suvi yaqin)",
              salinity: "Kuchsiz sho'rlangan",
              groundwaterDepth: "1.2 metr",
              waterSource: "Sirdaryo va zovur suvlari (doimiy suv)"
            },
            recommendation: {
              primaryCrop: "Lazer navli Sholi va Mosh",
              secondaryCrop: "Poliz (Qovun)",
              rationale: "Sizot suvlari yaqin va tuproq loyli bo'lgani sababli sholi hamda mosh juda yaxshi hosil beradi.",
              cycleMonths: "May - Oktyabr"
            },
            economics: {
              expensesUzs: 8400000,
              expectedYield: "3.8 tonna sholi (tozalangan guruch)",
              grossRevenueUzs: 49000000,
              netProfitUzs: 40600000,
              paybackMonths: 5
            }
          }
        ]
      },
      {
        id: "ming-boston",
        name: "Bo'ston MFY",
        specialization: "Gurvak Qovun va Tarvuz",
        leaseAreaHa: 200,
        poorFamilies: 155,
        center: [40.7950, 71.5050],
        parcels: [
          {
            id: "MIN-BOS-01",
            contourNumber: "119-kontur",
            farmerName: "Hamdamov Baxtiyor Rasulovich",
            familyStatus: "Temir daftar",
            familyMembers: 5,
            allocatedAreaHa: 0.5,
            contractYear: "2024 - 2034 (10 yil)",
            coordinates: [40.7960, 71.5065],
            specialization: "Polizchilik (Qovun, Tarvuz)",
            polygon: [
              [40.7945, 71.5050],
              [40.7970, 71.5055],
              [40.7965, 71.5085],
              [40.7940, 71.5080]
            ],
            soil: {
              type: "Qumloq to'qay tuprog'i",
              bonitetScore: 64,
              moisture: "72%",
              salinity: "Kuchsiz sho'rlangan",
              groundwaterDepth: "1.5 metr",
              waterSource: "Sirdaryo irmog'i"
            },
            recommendation: {
              primaryCrop: "Eksportbop Gurvak Qovun va Qora Tarvuz",
              secondaryCrop: "Dukkakli mosh",
              rationale: "Qumloq tuproqda poliz shirin pishadi, Rossiya bozoriga eksport qilish mumkin.",
              cycleMonths: "Aprel - Sentyabr"
            },
            economics: {
              expensesUzs: 6100000,
              expectedYield: "18 tonna poliz mahsulotlari",
              grossRevenueUzs: 41000000,
              netProfitUzs: 34900000,
              paybackMonths: 4
            }
          }
        ]
      }
    ]
  },
  {
    number: 9,
    id: "kosonsoy",
    name: "Kosonsoy tumani",
    shortName: "Kosonsoy",
    type: "tuman",
    center: [41.2589, 71.5492],
    zoom: 11,
    totalLeaseAreaHa: 3950,
    poorFamiliesCount: 3300,
    totalMFYCount: 58,
    activeContracts: 3210,
    color: "#15803d",
    badgeColor: "from-green-700 to-emerald-600",
    description: "Tog' va adir relyefi. Shirin olxo'ri, olma, dorivor giyohlar va dukkakli ekinlar makoni.",
    svgPath: "M 285 130 Q 330 115 345 170 Q 295 185 285 135 Z",
    pinPos: { x: 315, y: 145 },
    mfys: [
      {
        id: "kos-kushon",
        name: "Kushon MFY",
        specialization: "Kosonsoy Olxo'risi va Zira",
        leaseAreaHa: 175,
        poorFamilies: 140,
        center: [41.2650, 71.5380],
        parcels: [
          {
            id: "KOS-KUS-01",
            contourNumber: "62-kontur",
            farmerName: "Mirzayev Javlon Botirovich",
            familyStatus: "Temir daftar",
            familyMembers: 5,
            allocatedAreaHa: 0.45,
            contractYear: "2023 - 2033 (10 yil)",
            coordinates: [41.2662, 71.5395],
            specialization: "Olxo'ri, Loviya va Dorivor o'simliklar",
            polygon: [
              [41.2650, 71.5380],
              [41.2675, 71.5385],
              [41.2670, 71.5412],
              [41.2645, 71.5405]
            ],
            soil: {
              type: "Tog' oldi toshloq-bo'z tuprog'i",
              bonitetScore: 69,
              moisture: "60% (Salqin iqlim tufayli namlik yaxshi saqlanadi)",
              salinity: "Sho'rlanmagan",
              groundwaterDepth: "3.8 metr",
              waterSource: "Kosonsoy daryosi va tog' soylari"
            },
            recommendation: {
              primaryCrop: "Kosonsoy olxo'risi va Zira/Dorivor giyohlar",
              secondaryCrop: "Loviya va no'xat",
              rationale: "Tog' havosi va toza daryo suvi dorivor o'simliklar va eksportbop mevalar uchun eng yaxshi sharoit yaratadi.",
              cycleMonths: "Aprel - Oktyabr"
            },
            economics: {
              expensesUzs: 5600000,
              expectedYield: "5 tonna olxo'ri + 600 kg loviya",
              grossRevenueUzs: 39000000,
              netProfitUzs: 33400000,
              paybackMonths: 4
            }
          }
        ]
      },
      {
        id: "kos-chindovul",
        name: "Chindovul MFY",
        specialization: "Dorivor Giyohlar va Sabzavot",
        leaseAreaHa: 160,
        poorFamilies: 130,
        center: [41.2850, 71.5650],
        parcels: [
          {
            id: "KOS-CHI-01",
            contourNumber: "44-kontur",
            farmerName: "Toshmatov Omonjon G'aniyevich",
            familyStatus: "Ijtimoiy reyestr",
            familyMembers: 4,
            allocatedAreaHa: 0.4,
            contractYear: "2024 - 2034 (10 yil)",
            coordinates: [41.2865, 71.5665],
            specialization: "Zira, Qizilmiya, Sarimsoq",
            polygon: [
              [41.2850, 71.5650],
              [41.2875, 71.5655],
              [41.2870, 71.5685],
              [41.2845, 71.5680]
            ],
            soil: {
              type: "Serquyuq tog' tuprog'i",
              bonitetScore: 71,
              moisture: "62%",
              salinity: "Sho'rlanmagan",
              groundwaterDepth: "3.6 metr",
              waterSource: "Tog' bulog'i"
            },
            recommendation: {
              primaryCrop: "Zira va Tog' sarimsoqpiyozi",
              secondaryCrop: "Qizil sabzi",
              rationale: "Dorivor zira narxi yuqori (kg si 80-100 ming so'm), oz maydonda katta daromad beradi.",
              cycleMonths: "Aprel - Sentyabr"
            },
            economics: {
              expensesUzs: 5200000,
              expectedYield: "450 kg zira + 6 tonna sabzi",
              grossRevenueUzs: 41000000,
              netProfitUzs: 35800000,
              paybackMonths: 3.5
            }
          }
        ]
      }
    ]
  },
  {
    number: 10,
    id: "uychi",
    name: "Uychi tumani",
    shortName: "Uychi",
    type: "tuman",
    center: [41.0964, 71.8542],
    zoom: 11,
    totalLeaseAreaHa: 3350,
    poorFamiliesCount: 2900,
    totalMFYCount: 56,
    activeContracts: 2830,
    color: "#ea580c",
    badgeColor: "from-orange-600 to-amber-500",
    description: "Unumdor tekisliklar, intensiv ko'chatchilik va ertapishar sabzavotchilik maskani.",
    svgPath: "M 235 295 Q 280 295 270 345 Q 225 340 235 295 Z",
    pinPos: { x: 255, y: 320 },
    mfys: [
      {
        id: "uy-mashad",
        name: "Mashad MFY",
        specialization: "3 Mavsumli Sabzavotchilik",
        leaseAreaHa: 150,
        poorFamilies: 125,
        center: [41.1050, 71.8420],
        parcels: [
          {
            id: "UY-MAS-01",
            contourNumber: "48-kontur",
            farmerName: "Nazarov Shuhratbek Tolibovich",
            familyStatus: "Nogironligi bor oila a'zosi",
            familyMembers: 4,
            allocatedAreaHa: 0.35,
            contractYear: "2024 - 2034 (10 yil)",
            coordinates: [41.1065, 71.8435],
            specialization: "Ertapishar Sabzi, Karam va Mosh",
            polygon: [
              [41.1052, 71.8420],
              [41.1075, 71.8425],
              [41.1070, 71.8452],
              [41.1048, 71.8445]
            ],
            soil: {
              type: "Qadimiy sug'oriladigan o'tloqi tuproq",
              bonitetScore: 78,
              moisture: "74% (A'lo darajada)",
              salinity: "Sho'rlanmagan",
              groundwaterDepth: "1.9 metr",
              waterSource: "Norin-Farg'ona kanali tarmog'i"
            },
            recommendation: {
              primaryCrop: "Ertapishar Sabzi va Karam",
              secondaryCrop: "Mosh va Ko'katlar",
              rationale: "Uychi sabzavotkorlari tajribasi va unumdor tuproq sababli yiliga 3 marta hosil olinadi.",
              cycleMonths: "Fevral - May, Iyun - Avgust, Sentyabr - Dekabr"
            },
            economics: {
              expensesUzs: 6100000,
              expectedYield: "16 tonna sabzavotlar (3 mavsum)",
              grossRevenueUzs: 46000000,
              netProfitUzs: 39900000,
              paybackMonths: 3
            }
          }
        ]
      },
      {
        id: "uy-jiydakapa",
        name: "Jiydakapa MFY",
        specialization: "Ertapishar Kartoshka va Piyoz",
        leaseAreaHa: 130,
        poorFamilies: 110,
        center: [41.1180, 71.8650],
        parcels: [
          {
            id: "UY-JIY-01",
            contourNumber: "63-kontur",
            farmerName: "Isomiddinov Botirjon Komilovich",
            familyStatus: "Temir daftar",
            familyMembers: 5,
            allocatedAreaHa: 0.4,
            contractYear: "2024 - 2034 (10 yil)",
            coordinates: [41.1195, 71.8665],
            specialization: "Bahorgi kartoshka va piyoz",
            polygon: [
              [41.1180, 71.8650],
              [41.1205, 71.8655],
              [41.1200, 71.8685],
              [41.1175, 71.8680]
            ],
            soil: {
              type: "Yumshoq unumdor bo'z tuproq",
              bonitetScore: 76,
              moisture: "72%",
              salinity: "Sho'rlanmagan",
              groundwaterDepth: "1.8 metr",
              waterSource: "Norin kanali"
            },
            recommendation: {
              primaryCrop: "Ertapishar Kartoshka",
              secondaryCrop: "Osh lavlagi va ko'kat",
              rationale: "Plyonka ostida erta bahorda ekilib, may oyida bozorga yuqori narxda sotiladi.",
              cycleMonths: "Fevral - Iyun, Iyul - Oktyabr"
            },
            economics: {
              expensesUzs: 6400000,
              expectedYield: "12 tonna kartoshka",
              grossRevenueUzs: 43000000,
              netProfitUzs: 36600000,
              paybackMonths: 3
            }
          }
        ]
      }
    ]
  },
  {
    number: 11,
    id: "yangiqorgon",
    name: "Yangiqo'rg'on tumani",
    shortName: "Yangiqo'rg'on",
    type: "tuman",
    center: [41.1969, 71.7242],
    zoom: 11,
    totalLeaseAreaHa: 4300,
    poorFamiliesCount: 3550,
    totalMFYCount: 62,
    activeContracts: 3450,
    color: "#2563eb",
    badgeColor: "from-blue-600 to-sky-500",
    description: "Viloyatning kartoshkachilik va tog' olma-nok bog'lari bo'yicha yetakchi hududi.",
    svgPath: "M 345 220 Q 405 210 420 265 Q 365 275 350 230 Z",
    pinPos: { x: 385, y: 240 },
    mfys: [
      {
        id: "yq-nanay",
        name: "Nanay MFY",
        specialization: "Mashhur Nanay Kartoshkasi",
        leaseAreaHa: 195,
        poorFamilies: 160,
        center: [41.2350, 71.7450],
        parcels: [
          {
            id: "YQ-NAN-01",
            contourNumber: "11-kontur",
            farmerName: "Holiqov Mansurjon G'ulomovich",
            familyStatus: "Ijtimoiy reyestr (boquvchisi yo'q)",
            familyMembers: 6,
            allocatedAreaHa: 0.5,
            contractYear: "2023 - 2033 (10 yil)",
            coordinates: [41.2365, 71.7468],
            specialization: "Elita tog' kartoshkasi va Malina",
            polygon: [
              [41.2350, 71.7450],
              [41.2378, 71.7458],
              [41.2372, 71.7485],
              [41.2345, 71.7478]
            ],
            soil: {
              type: "Qora-qo'ng'ir tog' tuprog'i (Gumusga boy)",
              bonitetScore: 82,
              moisture: "76% (Tabiiy salqin va nam)",
              salinity: "Mutlaqo sho'rlanmagan",
              groundwaterDepth: "3.5 metr",
              waterSource: "Podshota soyi (Toza tog' chashmalari)"
            },
            recommendation: {
              primaryCrop: "Tog' kartoshkasi (Nanay kartoshkasi)",
              secondaryCrop: "Malina va Qulupnay",
              rationale: "Mashhur Nanay kartoshkasi O'zbekistonda eng xaridorgir hisoblanadi, kraxmalga boy va narxi baland.",
              cycleMonths: "Aprel - Sentyabr"
            },
            economics: {
              expensesUzs: 8200000,
              expectedYield: "16 tonna elita tog' kartoshkasi",
              grossRevenueUzs: 56000000,
              netProfitUzs: 47800000,
              paybackMonths: 4
            }
          }
        ]
      },
      {
        id: "yq-zarkent",
        name: "Zarkent MFY",
        specialization: "Tog' Uzumi va Olmazorlar",
        leaseAreaHa: 180,
        poorFamilies: 145,
        center: [41.2150, 71.7150],
        parcels: [
          {
            id: "YQ-ZAR-01",
            contourNumber: "29-kontur",
            farmerName: "Ergashev Tohirjon Aliyevich",
            familyStatus: "Temir daftar",
            familyMembers: 5,
            allocatedAreaHa: 0.5,
            contractYear: "2023 - 2033 (10 yil)",
            coordinates: [41.2165, 71.7165],
            specialization: "Uzum (Xusayni, Rizamat) va Olma",
            polygon: [
              [41.2150, 71.7150],
              [41.2175, 71.7155],
              [41.2170, 71.7185],
              [41.2145, 71.7180]
            ],
            soil: {
              type: "Tog' yonbag'ri unumdor tuproq",
              bonitetScore: 80,
              moisture: "71%",
              salinity: "Sho'rlanmagan",
              groundwaterDepth: "3.2 metr",
              waterSource: "Zarkent soyi"
            },
            recommendation: {
              primaryCrop: "Eksportbop Uzum va Qizil Olma",
              secondaryCrop: "Qator oralariga mosh va sarimsoq",
              rationale: "Zarkent uzumlari o'z shiraliligi va chidamliligi bilan mashhur.",
              cycleMonths: "Aprel - Oktyabr"
            },
            economics: {
              expensesUzs: 7100000,
              expectedYield: "7 tonna uzum + 4 tonna olma",
              grossRevenueUzs: 48000000,
              netProfitUzs: 40900000,
              paybackMonths: 4
            }
          }
        ]
      }
    ]
  },
  {
    number: 12,
    id: "chortoq",
    name: "Chortoq tumani",
    shortName: "Chortoq",
    type: "tuman",
    center: [41.0667, 71.8167],
    zoom: 11,
    totalLeaseAreaHa: 3250,
    poorFamiliesCount: 2800,
    totalMFYCount: 54,
    activeContracts: 2710,
    color: "#e11d48",
    badgeColor: "from-rose-600 to-pink-500",
    description: "Shifobaxsh mineral suvlari, intensiv giloszorlar va issiqxonachilik maskani.",
    svgPath: "M 360 160 Q 425 150 435 210 Q 385 220 365 170 Z",
    pinPos: { x: 395, y: 185 },
    mfys: [
      {
        id: "chor-alixon",
        name: "Alixon MFY",
        specialization: "Eksportbop Gilos va Qulupnay",
        leaseAreaHa: 160,
        poorFamilies: 130,
        center: [41.0750, 71.8250],
        parcels: [
          {
            id: "CHO-ALI-01",
            contourNumber: "93-kontur",
            farmerName: "G'aniyev Dilshodbek Ergashovich",
            familyStatus: "Yoshlar daftari ro'yxatida",
            familyMembers: 4,
            allocatedAreaHa: 0.4,
            contractYear: "2024 - 2034 (10 yil)",
            coordinates: [41.0762, 71.8265],
            specialization: "Gilos, Qulupnay va Sarimsoq",
            polygon: [
              [41.0750, 71.8250],
              [41.0772, 71.8255],
              [41.0768, 71.8282],
              [41.0745, 71.8275]
            ],
            soil: {
              type: "Tipik sug'oriladigan bo'z tuproq",
              bonitetScore: 73,
              moisture: "67%",
              salinity: "Sho'rlanmagan",
              groundwaterDepth: "2.4 metr",
              waterSource: "Chortoqsoy va artezian quduq"
            },
            recommendation: {
              primaryCrop: "Eksportbop Gilos va Qulupnay",
              secondaryCrop: "Qator oralariga sarimsoqpiyoz",
              rationale: "Chortoqning iqlimi erta pishar eksportbop gilos uchun ideal, qator oralari qo'shimcha daromad beradi.",
              cycleMonths: "Aprel - Iyun (Gilos/Qulupnay), Kuz (Sarimsoq)"
            },
            economics: {
              expensesUzs: 6500000,
              expectedYield: "3.5 tonna gilos + 2 tonna qulupnay",
              grossRevenueUzs: 52000000,
              netProfitUzs: 45500000,
              paybackMonths: 3
            }
          }
        ]
      },
      {
        id: "chor-koroskon",
        name: "Koroskon MFY",
        specialization: "Ertapishar Sabzavot va Meva",
        leaseAreaHa: 145,
        poorFamilies: 120,
        center: [41.0550, 71.8050],
        parcels: [
          {
            id: "CHO-KOR-01",
            contourNumber: "67-kontur",
            farmerName: "Ismoilova Nilufar Vohidovna",
            familyStatus: "Ijtimoiy reyestr",
            familyMembers: 4,
            allocatedAreaHa: 0.35,
            contractYear: "2024 - 2034 (10 yil)",
            coordinates: [41.0560, 71.8065],
            specialization: "Pomidor, Qalampir va Shaftoli",
            polygon: [
              [41.0545, 71.8050],
              [41.0570, 71.8055],
              [41.0565, 71.8085],
              [41.0540, 71.8080]
            ],
            soil: {
              type: "Bo'z tuproq",
              bonitetScore: 72,
              moisture: "68%",
              salinity: "Sho'rlanmagan",
              groundwaterDepth: "2.2 metr",
              waterSource: "Chortoq kanali"
            },
            recommendation: {
              primaryCrop: "Sabzavotlar (Pomidor va bolgarskiy)",
              secondaryCrop: "Kuzgi sabzi",
              rationale: "Tuproq mineral moddalarga boy bo'lgani sababli sabzavotlar erta pishadi.",
              cycleMonths: "Aprel - Noyabr"
            },
            economics: {
              expensesUzs: 5400000,
              expectedYield: "9 tonna pomidor/qalampir",
              grossRevenueUzs: 38000000,
              netProfitUzs: 32600000,
              paybackMonths: 3.5
            }
          }
        ]
      }
    ]
  },
  {
    number: 13,
    id: "uchqorgon",
    name: "Uchqo'rg'on tumani",
    shortName: "Uchqo'rg'on",
    type: "tuman",
    center: [41.1147, 72.0789],
    zoom: 11,
    totalLeaseAreaHa: 3450,
    poorFamiliesCount: 2850,
    totalMFYCount: 50,
    activeContracts: 2780,
    color: "#0284c7",
    badgeColor: "from-sky-700 to-cyan-600",
    description: "Norin daryosi bo'yida joylashgan. Baliqchilik, gilos, anjir shaftoli va sabzavotchilik rivojlangan.",
    svgPath: "M 395 105 Q 465 100 480 165 Q 425 175 405 120 Z",
    pinPos: { x: 440, y: 135 },
    mfys: [
      {
        id: "uch-qayqi",
        name: "Qayqi MFY",
        specialization: "Anjir Shaftoli va Mosh",
        leaseAreaHa: 170,
        poorFamilies: 145,
        center: [41.1250, 72.0850],
        parcels: [
          {
            id: "UCH-QAY-01",
            contourNumber: "41-kontur",
            farmerName: "Sobirov Akmalxon Tohirovich",
            familyStatus: "Temir daftar (kam ta'minlangan oila)",
            familyMembers: 5,
            allocatedAreaHa: 0.5,
            contractYear: "2024 - 2034 (10 yil)",
            coordinates: [41.1265, 72.0865],
            specialization: "Anjir shaftoli va Dukkakli mosh",
            polygon: [
              [41.1252, 72.0850],
              [41.1278, 72.0855],
              [41.1272, 72.0885],
              [41.1248, 72.0878]
            ],
            soil: {
              type: "O'tloqi-allyuvial unumdor tuproq",
              bonitetScore: 80,
              moisture: "77% (Norin daryosi hisobiga a'lo)",
              salinity: "Sho'rlanmagan",
              groundwaterDepth: "1.7 metr",
              waterSource: "Norin daryosi kanali (Kafolatlangan oqim suv)"
            },
            recommendation: {
              primaryCrop: "Shaftoli (Anjir shaftoli) va Mosh",
              secondaryCrop: "Kuzgi karam va ko'katlar",
              rationale: "Norin daryosi suvi minerallarga boy va doimiy oqadi. Shaftoli juda xaridorgir va serhosil bo'ladi.",
              cycleMonths: "May - Sentyabr"
            },
            economics: {
              expensesUzs: 7000000,
              expectedYield: "8 tonna shaftoli + 800 kg mosh",
              grossRevenueUzs: 48000000,
              netProfitUzs: 41000000,
              paybackMonths: 3.5
            }
          }
        ]
      },
      {
        id: "uch-yangiobod",
        name: "Yangiobod MFY",
        specialization: "Eksportbop Piyoz va Sabzi",
        leaseAreaHa: 155,
        poorFamilies: 130,
        center: [41.1050, 72.0550],
        parcels: [
          {
            id: "UCH-YAN-01",
            contourNumber: "55-kontur",
            farmerName: "Mavlonov Baxtiyor G'ulomovich",
            familyStatus: "Ijtimoiy reyestr",
            familyMembers: 5,
            allocatedAreaHa: 0.45,
            contractYear: "2024 - 2034 (10 yil)",
            coordinates: [41.1060, 72.0565],
            specialization: "Qizil piyoz va sabzi",
            polygon: [
              [41.1045, 72.0550],
              [41.1070, 72.0555],
              [41.1065, 72.0585],
              [41.1040, 72.0580]
            ],
            soil: {
              type: "Daryo bo'yi allyuvial tuprog'i",
              bonitetScore: 79,
              moisture: "76%",
              salinity: "Sho'rlanmagan",
              groundwaterDepth: "1.6 metr",
              waterSource: "Norin daryosi tarmog'i"
            },
            recommendation: {
              primaryCrop: "Eksportbop Zarafshon Piyozi",
              secondaryCrop: "Ertapishar sabzi",
              rationale: "Norin daryosi bo'yidagi piyoz uzoq saqlanadi va chirishga chidamli bo'ladi.",
              cycleMonths: "Mart - Iyul, Avgust - Noyabr"
            },
            economics: {
              expensesUzs: 6200000,
              expectedYield: "18 tonna piyoz + 5 tonna sabzi",
              grossRevenueUzs: 45000000,
              netProfitUzs: 38800000,
              paybackMonths: 3.5
            }
          }
        ]
      }
    ]
  },
  {
    number: 14,
    id: "norin",
    name: "Norin tumani",
    shortName: "Norin",
    type: "tuman",
    center: [40.8936, 72.0231],
    zoom: 11,
    totalLeaseAreaHa: 3650,
    poorFamiliesCount: 3150,
    totalMFYCount: 52,
    activeContracts: 3080,
    color: "#1e3a8a",
    badgeColor: "from-blue-900 to-indigo-800",
    description: "Qoradaryo va Norin tutashgan serob voha. Piyozchilik, poliz va qovun yetishtirish markazi.",
    svgPath: "M 320 60 Q 380 50 400 110 Q 345 120 325 75 Z",
    pinPos: { x: 360, y: 85 },
    mfys: [
      {
        id: "nor-haqqulobod",
        name: "Haqqulobod MFY",
        specialization: "Eksportbop Qizil Piyoz va Poliz",
        leaseAreaHa: 180,
        poorFamilies: 150,
        center: [40.9020, 72.0150],
        parcels: [
          {
            id: "NOR-HAQ-01",
            contourNumber: "118-kontur",
            farmerName: "Madaminov Farhod Rustamovich",
            familyStatus: "Ijtimoiy himoya yagona reyestri",
            familyMembers: 6,
            allocatedAreaHa: 0.5,
            contractYear: "2023 - 2033 (10 yil)",
            coordinates: [40.9035, 72.0165],
            specialization: "Qizil piyoz, Tarvuz va Mosh",
            polygon: [
              [40.9022, 72.0148],
              [40.9048, 72.0155],
              [40.9042, 72.0185],
              [40.9018, 72.0178]
            ],
            soil: {
              type: "Qalin madaniy o'tloqi tuproq",
              bonitetScore: 81,
              moisture: "76% (Yuqori namlik)",
              salinity: "Sho'rlanmagan",
              groundwaterDepth: "1.5 metr",
              waterSource: "Norin daryosi va kollektor-drenaj tarmog'i"
            },
            recommendation: {
              primaryCrop: "Eksportbop Qizil piyoz va Tarvuz",
              secondaryCrop: "Dukkakli mosh",
              rationale: "Norin piyozi o'zining chidamliligi va shirin-achchiq ta'mi bilan mashhur. Daryo bo'yida poliz shirin pishadi.",
              cycleMonths: "Mart - Iyul (Piyoz), Avgust - Oktyabr (Mosh)"
            },
            economics: {
              expensesUzs: 7800000,
              expectedYield: "22 tonna piyoz + 700 kg mosh",
              grossRevenueUzs: 53000000,
              netProfitUzs: 45200000,
              paybackMonths: 4
            }
          }
        ]
      },
      {
        id: "nor-shorariq",
        name: "Sho'rariq MFY",
        specialization: "Sabzavotchilik va Karam",
        leaseAreaHa: 165,
        poorFamilies: 135,
        center: [40.8850, 71.9950],
        parcels: [
          {
            id: "NOR-SHO-01",
            contourNumber: "92-kontur",
            farmerName: "Isroilov Dilshodbek Omonovich",
            familyStatus: "Temir daftar",
            familyMembers: 5,
            allocatedAreaHa: 0.45,
            contractYear: "2024 - 2034 (10 yil)",
            coordinates: [40.8860, 71.9965],
            specialization: "Karam, Sabzi va Oshqovoq",
            polygon: [
              [40.8845, 71.9950],
              [40.8870, 71.9955],
              [40.8865, 71.9985],
              [40.8840, 71.9980]
            ],
            soil: {
              type: "O'tloqi tuproq",
              bonitetScore: 78,
              moisture: "74%",
              salinity: "Sho'rlanmagan",
              groundwaterDepth: "1.7 metr",
              waterSource: "Sho'rariq kanali"
            },
            recommendation: {
              primaryCrop: "Oqbosh karam va Sariq sabzi",
              secondaryCrop: "Dukkakli no'xat",
              rationale: "Suv ta'minoti barqaror bo'lib, karam va sabzi yuqori hosil beradi.",
              cycleMonths: "Aprel - Noyabr"
            },
            economics: {
              expensesUzs: 5700000,
              expectedYield: "15 tonna karam va sabzi",
              grossRevenueUzs: 40000000,
              netProfitUzs: 34300000,
              paybackMonths: 3.5
            }
          }
        ]
      }
    ]
  }
];

// Ekinlar katalogi va ularning agronomik ko'rsatkichlari
export const CROPS_CATALOG = [
  {
    id: "kartoshka",
    name: "Tog' va Elita Kartoshkasi",
    suitableSoil: "Bo'z tuproq, qora-qo'ng'ir tuproq, unumdor qumloq",
    minBonitet: 65,
    optimalMoisture: "65% - 75%",
    irrigationFreq: "Har 7-10 kunda bir marta",
    avgYieldPerHa: "25 - 32 tonna/ga",
    marketPricePerKg: "4 000 - 5 500 so'm",
    avgProfitPer50Sotix: "35 - 45 mln so'm",
    bestDistricts: ["Yangiqo'rg'on", "Chortoq", "Namangan tumani", "Kosonsoy"],
    icon: "🥔"
  },
  {
    id: "sabzi",
    name: "Ertapishar Qizil va Sariq Sabzi",
    suitableSoil: "Yengil qumloq va madaniy o'tloqi tuproq",
    minBonitet: 60,
    optimalMoisture: "60% - 70%",
    irrigationFreq: "Har 5-7 kunda me'yorida",
    avgYieldPerHa: "30 - 40 tonna/ga",
    marketPricePerKg: "2 500 - 4 000 so'm",
    avgProfitPer50Sotix: "30 - 40 mln so'm",
    bestDistricts: ["Uychi", "To'raqo'rg'on", "Namangan tumani", "Norin"],
    icon: "🥕"
  },
  {
    id: "piyoz",
    name: "Eksportbop Zarafshon / Qizil Piyoz",
    suitableSoil: "O'tloqi va tipik bo'z tuproq",
    minBonitet: 68,
    optimalMoisture: "65% - 75%",
    irrigationFreq: "Har 8-10 kunda bir marta",
    avgYieldPerHa: "40 - 50 tonna/ga",
    marketPricePerKg: "2 200 - 3 500 so'm",
    avgProfitPer50Sotix: "40 - 50 mln so'm",
    bestDistricts: ["Norin", "Mingbuloq", "Pop", "Uychi"],
    icon: "🧅"
  },
  {
    id: "mosh",
    name: "Eksportbop Yashil Mosh (Dukkakli)",
    suitableSoil: "Barcha turdagi tuproqlar, qumloq va sho'rlangan yerlar",
    minBonitet: 50,
    optimalMoisture: "50% - 65% (Qurg'oqchilikka chidamli)",
    irrigationFreq: "Mavsum davomida 2-3 marta sug'orish yetarli",
    avgYieldPerHa: "1.8 - 2.5 tonna/ga",
    marketPricePerKg: "12 000 - 15 000 so'm",
    avgProfitPer50Sotix: "15 - 22 mln so'm (2-hosil sifatida)",
    bestDistricts: ["Pop", "Mingbuloq", "Chust", "Norin"],
    icon: "🌱"
  },
  {
    id: "gilos",
    name: "Eksportbop Katta Gilos / Bog'dorchilik",
    suitableSoil: "Tog' oldi toshloq va unumdor bo'z tuproq",
    minBonitet: 70,
    optimalMoisture: "60% - 70%",
    irrigationFreq: "Tomchilatib yoki ariq orqali 10 kunda bir",
    avgYieldPerHa: "8 - 14 tonna/ga",
    marketPricePerKg: "25 000 - 45 000 so'm",
    avgProfitPer50Sotix: "45 - 65 mln so'm",
    bestDistricts: ["Chortoq", "Kosonsoy", "Uchqo'rg'on", "Chust"],
    icon: "🍒"
  },
  {
    id: "sholi",
    name: "Lazer va Alanga Sholisi",
    suitableSoil: "Suv shimishi past botqoq-o'tloqi tuproq",
    minBonitet: 60,
    optimalMoisture: "85% - 95% (Doimiy suv qatlami)",
    irrigationFreq: "Doimiy suv oqimi",
    avgYieldPerHa: "6 - 7.5 tonna/ga",
    marketPricePerKg: "14 000 - 18 000 so'm",
    avgProfitPer50Sotix: "35 - 45 mln so'm",
    bestDistricts: ["Mingbuloq", "Pop (Sirdaryo bo'yi)"],
    icon: "🌾"
  }
];

// Viloyat umumiy statistikasi
export const REGION_STATS = {
  totalDistricts: 14,
  totalLeaseAreaHa: 41730,
  totalAllocatedParcels: 34500,
  totalFamiliesEmployed: 33200,
  averageFamilyNetProfitUzs: "36.4 mln so'm/yil",
  averageLandSizePerFamily: "0.45 gektar (45 sotix)",
  totalPovertyReductionRate: "78.4%",
  waterGuaranteedAreaPercentage: "92%"
};
