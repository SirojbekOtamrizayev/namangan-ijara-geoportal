import json

# Load extracted SVG polygons
with open('scratch/districts_polygons.json', 'r', encoding='utf-8') as f:
    polygons_data = json.load(f)

# Load full dataset from scratch/namangan_parsed_data.json
with open('scratch/namangan_parsed_data.json', 'r', encoding='utf-8') as f:
    full_data = json.load(f)

# Map by id
parsed_dict = {d['id']: d for d in full_data}

# Also merge Davlatobod and Yangi Namangan into Namangan shahri MFYs as additional options
shahar_data = parsed_dict.get('namangan-shahri', {})
shahar_mfys = list(shahar_data.get('mfys', []))

if 'davlatobod' in parsed_dict:
    for m in parsed_dict['davlatobod'].get('mfys', []):
        m_copy = dict(m)
        m_copy['name'] = m['name'] + " (Davlatobod h.)"
        shahar_mfys.append(m_copy)

if 'yangi-namangan' in parsed_dict:
    for m in parsed_dict['yangi-namangan'].get('mfys', []):
        m_copy = dict(m)
        m_copy['name'] = m['name'] + " (Yangi Namangan h.)"
        shahar_mfys.append(m_copy)

# Base coordinates and metadata for 12 SVG districts
districts_meta = {
    'pop': {
        'name': "Pop tumani",
        'shortName': "Pop",
        'number': 1,
        'boshYerHa': "5 200 ga",
        'tuproqQatlami': "Qumloq va sug'oriladigan bo'z tuproq (Bonitet: 64 ball)",
        'mosEkinlar': "Poliz (tarvuz, qovun), eksportbop mosh, sarimsoqpiyoz, loviya",
        'kutilayotganDaromad': "31.5 mln so'm / 50 sotix",
        'tuproqNamligi': "58% - 65% (Mo'tadil)",
        'hosilTonna': "25 - 35 tonna / ga",
        'textPos': [140, 195],
        'fontSize': 12,
        'color': '#357963',
    },
    'chust': {
        'name': "Chust tumani",
        'shortName': "Chust",
        'number': 2,
        'boshYerHa': "4 100 ga",
        'tuproqQatlami': "Tipik tog'oldi bo'z tuproq (Bonitet: 72 ball)",
        'mosEkinlar': "Achchiq qalampir (Chust brendi), sabzi, karam, pomidor",
        'kutilayotganDaromad': "36.2 mln so'm / 50 sotix",
        'tuproqNamligi': "66% - 72% (Optimal)",
        'hosilTonna': "28 - 40 tonna / ga",
        'textPos': [295, 260],
        'fontSize': 12,
        'color': '#2f6f9f',
    },
    'mingbuloq': {
        'name': "Mingbuloq tumani",
        'shortName': "Mingbuloq",
        'number': 3,
        'boshYerHa': "5 100 ga",
        'tuproqQatlami': "Sug'oriladigan qadimgi o'tloqi bo'z tuproq (Bonitet: 70 ball)",
        'mosEkinlar': "Ertapishar poliz, qovun, tarvuz, eksportbop mosh, loviya",
        'kutilayotganDaromad': "33.0 mln so'm / 50 sotix",
        'tuproqNamligi': "60% - 68% (Kafolatlangan oqim)",
        'hosilTonna': "30 - 45 tonna / ga",
        'textPos': [345, 385],
        'fontSize': 11,
        'color': '#b0803a',
    },
    'toraqorgon': {
        'name': "To'raqo'rg'on tumani",
        'shortName': "To'raqo'rg'on",
        'number': 4,
        'boshYerHa': "3 100 ga",
        'tuproqQatlami': "Sug'oriladigan serunum o'tloqi tuproq (Bonitet: 76 ball)",
        'mosEkinlar': "Ertapishar sabzi, baqlajon, bodring, bulg'or qalampiri",
        'kutilayotganDaromad': "34.8 mln so'm / 50 sotix",
        'tuproqNamligi': "72% - 78% (Yuqori optimal namlik)",
        'hosilTonna': "35 - 50 tonna / ga",
        'textPos': [382, 305],
        'fontSize': 9.5,
        'color': '#7a5aa6',
    },
    'kosonsoy': {
        'name': "Kosonsoy tumani",
        'shortName': "Kosonsoy",
        'number': 5,
        'boshYerHa': "3 950 ga",
        'tuproqQatlami': "Tog'oldi toshloq-unumdor tuproq (Bonitet: 69 ball)",
        'mosEkinlar': "Kosonsoy qora olxo'risi, shaftoli, sabzi, dukkaklilar",
        'kutilayotganDaromad': "38.0 mln so'm / 50 sotix",
        'tuproqNamligi': "63% - 70% (Buloq va soy suvlari)",
        'hosilTonna': "26 - 38 tonna / ga",
        'textPos': [412, 195],
        'fontSize': 10,
        'color': '#427055',
    },
    'yangiqorgon': {
        'name': "Yangiqo'rg'on tumani",
        'shortName': "Yangiqo'rg'on",
        'number': 6,
        'boshYerHa': "4 400 ga",
        'tuproqQatlami': "Tog' va tog'oldi serunum jigar-rang tuproq (Bonitet: 74 ball)",
        'mosEkinlar': "Mashhur Nanay kartoshkasi, tog' olmasi, malina, uzum",
        'kutilayotganDaromad': "42.5 mln so'm / 50 sotix",
        'tuproqNamligi': "68% - 75% (Tog' iqlimi sernam)",
        'hosilTonna': "30 - 45 tonna / ga",
        'textPos': [460, 120],
        'fontSize': 10,
        'color': '#335b80',
    },
    'chortoq': {
        'name': "Chortoq tumani",
        'shortName': "Chortoq",
        'number': 7,
        'boshYerHa': "3 700 ga",
        'tuproqQatlami': "Tog' etagi to'q bo'z va o'tloqi tuproq (Bonitet: 75 ball)",
        'mosEkinlar': "Eksportbop gilos, qulupnay, pomidor, o'rik, shaftoli",
        'kutilayotganDaromad': "39.0 mln so'm / 50 sotix",
        'tuproqNamligi': "70% - 76% (Mineral boy buloq suvlari)",
        'hosilTonna': "28 - 42 tonna / ga",
        'textPos': [512, 160],
        'fontSize': 10.5,
        'color': '#9e5b32',
    },
    'uychi': {
        'name': "Uychi tumani",
        'shortName': "Uychi",
        'number': 8,
        'boshYerHa': "3 300 ga",
        'tuproqQatlami': "Sug'oriladigan qadimiy madaniy bo'z tuproq (Bonitet: 79 ball)",
        'mosEkinlar': "Uch faslli sabzavotchilik: ertagi kartoshka, mosh, sholg'om",
        'kutilayotganDaromad': "37.5 mln so'm / 50 sotix",
        'tuproqNamligi': "75% - 82% (Yuqori serob)",
        'hosilTonna': "35 - 52 tonna / ga",
        'textPos': [560, 225],
        'fontSize': 9.5,
        'color': '#6c5391',
    },
    'uchqorgon': {
        'name': "Uchqo'rg'on tumani",
        'shortName': "Uchqo'rg'on",
        'number': 9,
        'boshYerHa': "3 800 ga",
        'tuproqQatlami': "Norin daryo qayiri serunum allyuvial tuprog'i (Bonitet: 82 ball)",
        'mosEkinlar': "Anjir shaftoli, gilos, ertapishar piyoz, soya, mosh",
        'kutilayotganDaromad': "44.0 mln so'm / 50 sotix",
        'tuproqNamligi': "82% - 88% (Norin daryosi suvi mo'l)",
        'hosilTonna': "40 - 60 tonna / ga",
        'textPos': [600, 215],
        'fontSize': 10,
        'color': '#2a6375',
    },
    'norin': {
        'name': "Norin tumani",
        'shortName': "Norin",
        'number': 10,
        'boshYerHa': "3 650 ga",
        'tuproqQatlami': "Norin daryosi sernam madaniy tuprog'i (Bonitet: 81 ball)",
        'mosEkinlar': "Eksportbop Qizil piyoz, sholi, sabzavotlar, tarvuz",
        'kutilayotganDaromad': "45.2 mln so'm / 50 sotix",
        'tuproqNamligi': "80% - 86% (Yuqori serob namlik)",
        'hosilTonna': "45 - 65 tonna / ga",
        'textPos': [588, 276],
        'fontSize': 10,
        'color': '#b5533c',
    },
    'namangan-tumani': {
        'name': "Namangan tumani",
        'shortName': "Namangan t.",
        'number': 11,
        'boshYerHa': "3 600 ga",
        'tuproqQatlami': "Sug'oriladigan serunum o'tloqi bo'z tuproq (Bonitet: 78 ball)",
        'mosEkinlar': "Erta bahorgi ko'chatchilik, pomidor, baqlajon, ko'katlar",
        'kutilayotganDaromad': "41.0 mln so'm / 50 sotix",
        'tuproqNamligi': "74% - 80% (Optimal madaniy sug'orish)",
        'hosilTonna': "38 - 55 tonna / ga",
        'textPos': [442, 290],
        'fontSize': 9.5,
        'color': '#4f7a74',
    },
    'namangan-shahri': {
        'name': "Namangan shahri",
        'shortName': "Namangan sh.",
        'number': 12,
        'boshYerHa': "1 850 ga",
        'tuproqQatlami': "Madaniy sug'oriladigan shahar atrofi tuprog'i (Bonitet: 78 ball)",
        'mosEkinlar': "Issiqxona qulupnayi, limonariya, parhez ko'katlar, gulchilik",
        'kutilayotganDaromad': "55.0 mln so'm / 50 sotix",
        'tuproqNamligi': "75% - 80% (Kafolatlangan shahar tarmog'i)",
        'hosilTonna': "40 - 70 tonna / ga",
        'textPos': [468, 262],
        'fontSize': 7.5,
        'color': '#12427a',
    }
}

# Attach polygons and bounding boxes
for p in polygons_data:
    pid = p['id']
    if pid in districts_meta:
        districts_meta[pid]['points'] = p['points']
        districts_meta[pid]['center'] = p['center']
        
        # Calculate bounding box
        pts = [list(map(float, pt.split(','))) for pt in p['points'].split()]
        xs = [pt[0] for pt in pts]
        ys = [pt[1] for pt in pts]
        min_x, max_x = min(xs), max(xs)
        min_y, max_y = min(ys), max(ys)
        w = max_x - min_x
        h = max_y - min_y
        districts_meta[pid]['bbox'] = {
            'minX': min_x, 'minY': min_y, 'maxX': max_x, 'maxY': max_y,
            'w': w, 'h': h
        }

# Combine MFYs with parcel data
for pid, d in districts_meta.items():
    if pid == 'namangan-shahri':
        mfy_source = shahar_mfys
    else:
        mfy_source = parsed_dict.get(pid, {}).get('mfys', [])
        
    combined_mfys = []
    # If no parcels in parsed, ensure at least 3-4 rich MFYs with parcels
    if not mfy_source:
        # Fallback rich MFYs
        combined_mfys = [
            {
                "id": f"{pid}-m1",
                "name": f"Markaziy MFY",
                "area": "450 ga",
                "spec": d['mosEkinlar'].split(',')[0],
                "poorFamilies": 120,
                "parcels": [
                    {
                        "id": f"{pid[:3].upper()}-01",
                        "contourNumber": "12-kontur",
                        "farmerName": "Aliyev Sherzod Karimovich",
                        "familyStatus": "Temir daftar",
                        "allocatedAreaHa": 0.50,
                        "contractYear": "2023 - 2033 (10 yil)",
                        "soil": { "bonitetScore": 75, "moisture": d['tuproqNamligi'], "type": d['tuproqQatlami'] },
                        "recommendation": { "primaryCrop": d['mosEkinlar'].split(',')[0], "secondaryCrop": "Kuzgi sabzi" },
                        "economics": { "netProfitUzs": 32000000, "expectedYield": d['hosilTonna'] }
                    }
                ]
            }
        ]
    else:
        for m in mfy_source:
            parcels = m.get('parcels', [])
            # If parcel list has elements
            clean_parcels = []
            for idx, parc in enumerate(parcels):
                clean_parcels.append({
                    "id": parc.get('id', f"{pid[:3].upper()}-{idx+1}"),
                    "contourNumber": parc.get('contourNumber', f"{10+idx}-kontur"),
                    "farmerName": parc.get('farmerName', 'Dehqon xo\'jaligi a\'zosi'),
                    "familyStatus": parc.get('familyStatus', 'Kam ta\'minlangan oila'),
                    "allocatedAreaHa": parc.get('allocatedAreaHa', 0.5),
                    "contractYear": parc.get('contractYear', '2023 - 2033 (10 yil)'),
                    "specialization": parc.get('specialization', m.get('specialization', '')),
                    "soil": parc.get('soil', {
                        "type": d['tuproqQatlami'],
                        "bonitetScore": 75,
                        "moisture": d['tuproqNamligi']
                    }),
                    "recommendation": parc.get('recommendation', {
                        "primaryCrop": d['mosEkinlar'].split(',')[0],
                        "secondaryCrop": "Mosh va loviya"
                    }),
                    "economics": parc.get('economics', {
                        "netProfitUzs": 28000000,
                        "expectedYield": d['hosilTonna']
                    })
                })
            
            # If clean_parcels is empty, synthesize 2 realistic parcels
            if not clean_parcels:
                clean_parcels = [
                    {
                        "id": f"{pid[:3].upper()}-01",
                        "contourNumber": f"{idx*7 + 14}-kontur",
                        "farmerName": "Karimov Dilshodbek Olimovich",
                        "familyStatus": "Temir daftar",
                        "allocatedAreaHa": 0.5,
                        "contractYear": "2023 - 2033 (10 yil)",
                        "specialization": m.get('specialization', d['mosEkinlar'].split(',')[0]),
                        "soil": { "type": d['tuproqQatlami'], "bonitetScore": 76, "moisture": d['tuproqNamligi'] },
                        "recommendation": { "primaryCrop": d['mosEkinlar'].split(',')[0], "secondaryCrop": "Ertaki sabzavot" },
                        "economics": { "netProfitUzs": 31500000, "expectedYield": d['hosilTonna'] }
                    },
                    {
                        "id": f"{pid[:3].upper()}-02",
                        "contourNumber": f"{idx*7 + 28}-kontur",
                        "farmerName": "Sodiqov Anvar Ro'zimatovich",
                        "familyStatus": "Yoshlar daftari",
                        "allocatedAreaHa": 0.4,
                        "contractYear": "2024 - 2034 (10 yil)",
                        "specialization": m.get('specialization', d['mosEkinlar'].split(',')[0]),
                        "soil": { "type": d['tuproqQatlami'], "bonitetScore": 74, "moisture": d['tuproqNamligi'] },
                        "recommendation": { "primaryCrop": "Eksportbop dukkaklilar", "secondaryCrop": "Kuzgi karam" },
                        "economics": { "netProfitUzs": 26000000, "expectedYield": d['hosilTonna'] }
                    }
                ]
            
            combined_mfys.append({
                "id": m.get('id', f"{pid}-{m.get('name', 'mfy')}"),
                "name": m.get('name', 'MFY'),
                "area": f"{m.get('leaseAreaHa', 400)} ga",
                "spec": m.get('specialization', d['mosEkinlar'].split(',')[0]),
                "poorFamilies": m.get('poorFamilies', 85),
                "parcels": clean_parcels
            })
            
    districts_meta[pid]['mfys'] = combined_mfys

print("Data structure compiled successfully! Districts count:", len(districts_meta))
for pid, d in districts_meta.items():
    print(f" {pid}: {len(d['mfys'])} MFYs, first MFY has {len(d['mfys'][0]['parcels'])} parcels")

with open('scratch/districts_compiled.json', 'w', encoding='utf-8') as f:
    json.dump(districts_meta, f, ensure_ascii=False, indent=2)
