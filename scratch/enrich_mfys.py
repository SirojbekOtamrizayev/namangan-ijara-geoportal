import json

with open('scratch/districts_compiled.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Extra MFYs with multiple parcels for each district to make it very rich and practical
extra_mfys_by_district = {
    'pop': [
        {
            "id": "pop-chorkesar-extra",
            "name": "Chorkesar MFY",
            "area": "420 ga",
            "spec": "Urug'chilik va sabzavotchilik",
            "poorFamilies": 74,
            "parcels": [
                {
                    "id": "POP-CK-01",
                    "contourNumber": "18-kontur",
                    "farmerName": "Hasanov Jamshidbek Nuriddinovich",
                    "familyStatus": "Temir daftar",
                    "allocatedAreaHa": 0.50,
                    "contractYear": "2023 - 2033 (10 yil)",
                    "specialization": "Mosh va poliz",
                    "soil": { "type": "Qumloq bo'z tuproq", "bonitetScore": 66, "moisture": "62% (Mo'tadil)" },
                    "recommendation": { "primaryCrop": "Eksportbop Yashil Mosh", "secondaryCrop": "Kuzgi sarimsoqpiyoz" },
                    "economics": { "netProfitUzs": 34000000, "expectedYield": "3.2 tonna / ga" }
                },
                {
                    "id": "POP-CK-02",
                    "contourNumber": "19-kontur",
                    "farmerName": "Qodirova Nilufar Baxtiyorovna",
                    "familyStatus": "Ayollar daftari",
                    "allocatedAreaHa": 0.40,
                    "contractYear": "2024 - 2034 (10 yil)",
                    "specialization": "Sabzavotchilik",
                    "soil": { "type": "Qumloq tuproq", "bonitetScore": 65, "moisture": "60% (Mo'tadil)" },
                    "recommendation": { "primaryCrop": "Poliz (Qovun, Tarvuz)", "secondaryCrop": "Loviya" },
                    "economics": { "netProfitUzs": 29000000, "expectedYield": "28 tonna / ga" }
                }
            ]
        },
        {
            "id": "pop-pungon",
            "name": "Pungon MFY",
            "area": "510 ga",
            "spec": "Poliz va sarimsoqpiyoz",
            "poorFamilies": 92,
            "parcels": [
                {
                    "id": "POP-PNG-01",
                    "contourNumber": "32-kontur",
                    "farmerName": "Normatov Erkin Rustamovich",
                    "familyStatus": "Yoshlar daftari",
                    "allocatedAreaHa": 0.60,
                    "contractYear": "2023 - 2033 (10 yil)",
                    "specialization": "Sarimsoqpiyoz va poliz",
                    "soil": { "type": "Sug'oriladigan bo'z tuproq", "bonitetScore": 67, "moisture": "64% (Yaxshi)" },
                    "recommendation": { "primaryCrop": "Eksportbop Sarimsoqpiyoz", "secondaryCrop": "Takroriy mosh" },
                    "economics": { "netProfitUzs": 38500000, "expectedYield": "18 tonna / ga" }
                }
            ]
        }
    ],
    'chust': [
        {
            "id": "chust-karkidon",
            "name": "Karkidon MFY",
            "area": "420 ga",
            "spec": "Chust achchiq qalampiri va sabzi",
            "poorFamilies": 85,
            "parcels": [
                {
                    "id": "CHS-KRK-01",
                    "contourNumber": "14-kontur",
                    "farmerName": "Mamatov Botirali Fayzullayevich",
                    "familyStatus": "Temir daftar",
                    "allocatedAreaHa": 0.50,
                    "contractYear": "2023 - 2033 (10 yil)",
                    "specialization": "Achchiq qalampir",
                    "soil": { "type": "Tog'oldi bo'z tuproq", "bonitetScore": 73, "moisture": "70% (Optimal)" },
                    "recommendation": { "primaryCrop": "Chust Qalampiri", "secondaryCrop": "Kuzgi sabzi" },
                    "economics": { "netProfitUzs": 41000000, "expectedYield": "22 tonna / ga" }
                }
            ]
        },
        {
            "id": "chust-olmos",
            "name": "Olmos MFY",
            "area": "410 ga",
            "spec": "Qalampirchilik va piyoz",
            "poorFamilies": 78,
            "parcels": [
                {
                    "id": "CHS-OLM-01",
                    "contourNumber": "27-kontur",
                    "farmerName": "Yo'ldoshev Akromjon Sobirovich",
                    "familyStatus": "Kam ta'minlangan",
                    "allocatedAreaHa": 0.50,
                    "contractYear": "2024 - 2034 (10 yil)",
                    "specialization": "Qalampir va piyoz",
                    "soil": { "type": "Bo'z tuproq", "bonitetScore": 72, "moisture": "68% (Optimal)" },
                    "recommendation": { "primaryCrop": "Achchiq qalampir", "secondaryCrop": "Qizil piyoz" },
                    "economics": { "netProfitUzs": 37000000, "expectedYield": "25 tonna / ga" }
                }
            ]
        }
    ],
    'mingbuloq': [
        {
            "id": "ming-qizilqum",
            "name": "Qizilqum MFY",
            "area": "68 ga",
            "spec": "Poliz va sabzavot",
            "poorFamilies": 65,
            "parcels": [
                {
                    "id": "MNG-QZQ-01",
                    "contourNumber": "07-kontur",
                    "farmerName": "Tojiyev Ilhomjon Karimovich",
                    "familyStatus": "Temir daftar",
                    "allocatedAreaHa": 0.50,
                    "contractYear": "2023 - 2033 (10 yil)",
                    "specialization": "Gurvak qovun va poliz",
                    "soil": { "type": "Qadimgi o'tloqi tuproq", "bonitetScore": 71, "moisture": "65% (Kafolatlangan)" },
                    "recommendation": { "primaryCrop": "Gurvak qovun va tarvuz", "secondaryCrop": "Dukkakli mosh" },
                    "economics": { "netProfitUzs": 35000000, "expectedYield": "35 tonna / ga" }
                }
            ]
        },
        {
            "id": "ming-yangigulbog",
            "name": "Yangi Gulbog' MFY",
            "area": "153 ga",
            "spec": "Eksportbop poliz va sholi",
            "poorFamilies": 110,
            "parcels": [
                {
                    "id": "MNG-YGB-01",
                    "contourNumber": "21-kontur",
                    "farmerName": "Abdullayev Ravshanbek",
                    "familyStatus": "Yoshlar daftari",
                    "allocatedAreaHa": 0.50,
                    "contractYear": "2024 - 2034 (10 yil)",
                    "specialization": "Lazer sholisi va poliz",
                    "soil": { "type": "O'tloqi tuproq", "bonitetScore": 72, "moisture": "72% (Serob)" },
                    "recommendation": { "primaryCrop": "Lazer sholi", "secondaryCrop": "Takroriy mosh" },
                    "economics": { "netProfitUzs": 38000000, "expectedYield": "45 s / ga" }
                }
            ]
        }
    ],
    'toraqorgon': [
        {
            "id": "tora-axsi",
            "name": "Axsi MFY",
            "area": "410 ga",
            "spec": "Tarixiy bog'dorchilik va ertaki sabzavot",
            "poorFamilies": 82,
            "parcels": [
                {
                    "id": "TRQ-AXS-01",
                    "contourNumber": "15-kontur",
                    "farmerName": "Usmonov Sobirjon",
                    "familyStatus": "Temir daftar",
                    "allocatedAreaHa": 0.50,
                    "contractYear": "2023 - 2033 (10 yil)",
                    "specialization": "Ertapishar sabzi va pomidor",
                    "soil": { "type": "Serunum o'tloqi", "bonitetScore": 77, "moisture": "76% (Optimal)" },
                    "recommendation": { "primaryCrop": "Ertapishar sabzi", "secondaryCrop": "Kuzgi gulkaram" },
                    "economics": { "netProfitUzs": 39000000, "expectedYield": "38 tonna / ga" }
                }
            ]
        }
    ],
    'kosonsoy': [
        {
            "id": "kos-bogbon",
            "name": "Bog'bon MFY",
            "area": "380 ga",
            "spec": "Qora olxo'ri va shaftoli",
            "poorFamilies": 76,
            "parcels": [
                {
                    "id": "KSS-BGB-01",
                    "contourNumber": "09-kontur",
                    "farmerName": "Yoqubov Mansurxon",
                    "familyStatus": "Kam ta'minlangan",
                    "allocatedAreaHa": 0.50,
                    "contractYear": "2023 - 2033 (10 yil)",
                    "specialization": "Kosonsoy olxo'risi",
                    "soil": { "type": "Tog'oldi toshloq-unumdor", "bonitetScore": 70, "moisture": "66% (Buloq suvi)" },
                    "recommendation": { "primaryCrop": "Kosonsoy qora olxo'risi", "secondaryCrop": "Zira va dorivorlar" },
                    "economics": { "netProfitUzs": 43000000, "expectedYield": "24 tonna / ga" }
                }
            ]
        }
    ],
    'yangiqorgon': [
        {
            "id": "yq-poromon",
            "name": "Poromon MFY",
            "area": "390 ga",
            "spec": "Nanay elita kartoshkasi",
            "poorFamilies": 80,
            "parcels": [
                {
                    "id": "YQ-PRM-01",
                    "contourNumber": "11-kontur",
                    "farmerName": "Eshonov Alisher Muxtorovich",
                    "familyStatus": "Yoshlar daftari",
                    "allocatedAreaHa": 0.50,
                    "contractYear": "2023 - 2033 (10 yil)",
                    "specialization": "Elita urug'lik kartoshka",
                    "soil": { "type": "Tog' jigar-rang", "bonitetScore": 75, "moisture": "74% (Mo'tadil sernam)" },
                    "recommendation": { "primaryCrop": "Nanay kartoshkasi", "secondaryCrop": "Kuzgi ko'katlar" },
                    "economics": { "netProfitUzs": 46000000, "expectedYield": "34 tonna / ga" }
                }
            ]
        }
    ],
    'chortoq': [
        {
            "id": "chor-peshkorgon",
            "name": "Peshqo'rg'on MFY",
            "area": "410 ga",
            "spec": "Gilos va intensiv meva",
            "poorFamilies": 88,
            "parcels": [
                {
                    "id": "CRT-PSK-01",
                    "contourNumber": "23-kontur",
                    "farmerName": "G'oziyev Baxtiyor",
                    "familyStatus": "Temir daftar",
                    "allocatedAreaHa": 0.50,
                    "contractYear": "2023 - 2033 (10 yil)",
                    "specialization": "Gilos va qulupnay",
                    "soil": { "type": "Tog'oldi to'q bo'z", "bonitetScore": 76, "moisture": "73% (Buloq suvi)" },
                    "recommendation": { "primaryCrop": "Eksportbop Gilos", "secondaryCrop": "Remontant qulupnay" },
                    "economics": { "netProfitUzs": 48000000, "expectedYield": "26 tonna / ga" }
                }
            ]
        }
    ],
    'uychi': [
        {
            "id": "uy-yorqishloq",
            "name": "Yorqishloq MFY",
            "area": "360 ga",
            "spec": "3 mavsumli sabzavot",
            "poorFamilies": 72,
            "parcels": [
                {
                    "id": "UY-YRQ-01",
                    "contourNumber": "16-kontur",
                    "farmerName": "Sattorov Jamoliddin",
                    "familyStatus": "Temir daftar",
                    "allocatedAreaHa": 0.50,
                    "contractYear": "2023 - 2033 (10 yil)",
                    "specialization": "3 faslli poliz va sabzavot",
                    "soil": { "type": "Madaniy bo'z", "bonitetScore": 80, "moisture": "78% (Serob)" },
                    "recommendation": { "primaryCrop": "Ertaki kartoshka", "secondaryCrop": "Takroriy mosh va sholg'om" },
                    "economics": { "netProfitUzs": 42000000, "expectedYield": "45 tonna / ga" }
                }
            ]
        }
    ],
    'uchqorgon': [
        {
            "id": "uch-kujon",
            "name": "Ko'g'ay MFY",
            "area": "440 ga",
            "spec": "Anjir shaftoli va mosh",
            "poorFamilies": 84,
            "parcels": [
                {
                    "id": "UCH-KGY-01",
                    "contourNumber": "29-kontur",
                    "farmerName": "Mirzayev Farhodjon",
                    "familyStatus": "Ayollar daftari",
                    "allocatedAreaHa": 0.50,
                    "contractYear": "2024 - 2034 (10 yil)",
                    "specialization": "Anjir shaftoli",
                    "soil": { "type": "Allyuvial daryo tuprog'i", "bonitetScore": 83, "moisture": "84% (Norin daryosi)" },
                    "recommendation": { "primaryCrop": "Anjir shaftoli va gilos", "secondaryCrop": "Eksportbop mosh" },
                    "economics": { "netProfitUzs": 52000000, "expectedYield": "36 tonna / ga" }
                }
            ]
        }
    ],
    'norin': [
        {
            "id": "nor-tuda",
            "name": "To'da MFY",
            "area": "370 ga",
            "spec": "Eksportbop Qizil piyoz",
            "poorFamilies": 69,
            "parcels": [
                {
                    "id": "NOR-TUD-01",
                    "contourNumber": "19-kontur",
                    "farmerName": "Qosimov Shavkatbek",
                    "familyStatus": "Temir daftar",
                    "allocatedAreaHa": 0.50,
                    "contractYear": "2023 - 2033 (10 yil)",
                    "specialization": "Qizil piyoz",
                    "soil": { "type": "Sernam daryo qayiri", "bonitetScore": 82, "moisture": "82% (Serob)" },
                    "recommendation": { "primaryCrop": "Eksportbop Qizil piyoz", "secondaryCrop": "Kuzgi karam" },
                    "economics": { "netProfitUzs": 49000000, "expectedYield": "55 tonna / ga" }
                }
            ]
        }
    ],
    'namangan-tumani': [
        {
            "id": "namt-qoratepa",
            "name": "Qoratepa MFY",
            "area": "390 ga",
            "spec": "Erta bahorgi ko'chatchilik va baqlajon",
            "poorFamilies": 81,
            "parcels": [
                {
                    "id": "NMT-QRT-01",
                    "contourNumber": "33-kontur",
                    "farmerName": "Nazarov Rustamjon",
                    "familyStatus": "Yoshlar daftari",
                    "allocatedAreaHa": 0.45,
                    "contractYear": "2023 - 2033 (10 yil)",
                    "specialization": "Ko'chatchilik va baqlajon",
                    "soil": { "type": "O'tloqi bo'z", "bonitetScore": 79, "moisture": "76% (Optimal)" },
                    "recommendation": { "primaryCrop": "Baqlajon va bulg'ori", "secondaryCrop": "Parhez ko'katlar" },
                    "economics": { "netProfitUzs": 44000000, "expectedYield": "42 tonna / ga" }
                }
            ]
        }
    ]
}

for d_id, extra_list in extra_mfys_by_district.items():
    if d_id in data:
        data[d_id]['mfys'].extend(extra_list)

with open('scratch/districts_compiled.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Enriched dataset with extra MFYs and parcels successfully!")
for d_id, d in data.items():
    print(f" {d_id}: {len(d['mfys'])} MFYs, total parcels: {sum(len(m['parcels']) for m in d['mfys'])}")
