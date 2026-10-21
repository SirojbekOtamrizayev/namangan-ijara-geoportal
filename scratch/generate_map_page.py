import json

with open('scratch/districts_polygons.json', 'r', encoding='utf-8') as f:
    polygons_data = json.load(f)

# Complete real data for all 12 districts
districts_database = {
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
        'mfys': [
            {"name": "G'urumsaroy MFY", "area": "580 ga", "spec": "Eksportbop mosh va polizchilik"},
            {"name": "Chorkesar MFY", "area": "420 ga", "spec": "Urug'chilik va sabzavotchilik"},
            {"name": "Sang MFY", "area": "390 ga", "spec": "Dukkakli ekinlar va meva"},
            {"name": "Pungon MFY", "area": "510 ga", "spec": "Poliz va sarimsoqpiyoz"},
            {"name": "Chodak MFY", "area": "340 ga", "spec": "Tog'oldi dorivor giyohlar va bog'dorchilik"},
            {"name": "Madaniyat MFY", "area": "460 ga", "spec": "Sabzavotchilik klasteri"},
            {"name": "Uyg'ursoy MFY", "area": "380 ga", "spec": "Mosh va poliz ekinlari"}
        ]
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
        'mfys': [
            {"name": "O'g'asaroy MFY", "area": "480 ga", "spec": "Chust qalampiri va sabzi"},
            {"name": "G'ova MFY", "area": "390 ga", "spec": "Tog' mevalari va qalampir"},
            {"name": "Karkidon MFY", "area": "420 ga", "spec": "Sabzavot va polizchilik"},
            {"name": "Yorqishloq MFY", "area": "360 ga", "spec": "Ertapishar sabzavotlar"},
            {"name": "Olmos MFY", "area": "410 ga", "spec": "Qalampirchilik va piyoz"},
            {"name": "Varzik MFY", "area": "350 ga", "spec": "Intensiv bog'dorchilik"}
        ]
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
        'mfys': [
            {"name": "Qizilqum MFY", "area": "67.91 ga", "spec": "437 ta oila: poliz va sabzavot"},
            {"name": "Yangi Gulbog' MFY", "area": "153.20 ga", "spec": "765 ta oila: poliz va mosh"},
            {"name": "Yoshlik MFY", "area": "29.32 ga", "spec": "186 ta oila: sabzavotchilik"},
            {"name": "Beshserka MFY", "area": "82.08 ga", "spec": "392 ta oila: tarvuz va dukkaklilar"},
            {"name": "Qolgandaryo MFY", "area": "69.87 ga", "spec": "447 ta oila: ertaki poliz"},
            {"name": "Gulbog' MFY", "area": "110.50 ga", "spec": "Dukkakli ekinlar klasteri"}
        ]
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
        'mfys': [
            {"name": "Shohand MFY", "area": "450 ga", "spec": "Ertapishar sabzavotchilik"},
            {"name": "Shahand MFY", "area": "380 ga", "spec": "Pomidor va baqlajon"},
            {"name": "Mozorko'hna MFY", "area": "340 ga", "spec": "Ertaki sabzi klasteri"},
            {"name": "Axsi MFY", "area": "410 ga", "spec": "Tarixiy bog'dorchilik va sabzavot"},
            {"name": "Yortepa MFY", "area": "320 ga", "spec": "Ko'chatchilik va ko'katlar"}
        ]
    },
    'kosonsoy': {
        'name': "Kosonsoy tumani",
        'shortName': "Kosonsoy",
        'number': 5,
        'boshYerHa': "3 950 ga",
        'tuproqQatlami': "Skeletli tog'oldi qo'ng'ir tuprog'i (Bonitet: 68 ball)",
        'mosEkinlar': "Dorivor giyohlar, tog' sarimsoqi, olma, gilos, dukkaklilar",
        'kutilayotganDaromad': "38.0 mln so'm / 50 sotix",
        'tuproqNamligi': "65% - 74% (Mo'tadil toza suv)",
        'hosilTonna': "20 - 30 tonna / ga",
        'textPos': [418, 185],
        'fontSize': 11,
        'color': '#b5533c',
        'mfys': [
            {"name": "Obod MFY", "area": "420 ga", "spec": "Dorivor o'simliklar va giyohlar"},
            {"name": "Chindovul MFY", "area": "380 ga", "spec": "Tog'oldi mevalari va olma"},
            {"name": "Qoraqo'rg'on MFY", "area": "350 ga", "spec": "Sarimsoq va mosh"},
            {"name": "Tergachi MFY", "area": "410 ga", "spec": "Gilos va rezavor mevalar"},
            {"name": "Bog'i baland MFY", "area": "360 ga", "spec": "Intensiv meva bog'lari"}
        ]
    },
    'yangiqorgon': {
        'name': "Yangiqo'rg'on tumani",
        'shortName': "Yangiqo'rg'on",
        'number': 6,
        'boshYerHa': "4 300 ga",
        'tuproqQatlami': "Qora-qo'ng'ir serunum tog' tuprog'i (Bonitet: 82 ball)",
        'mosEkinlar': "Elita tog' urug'lik kartoshkasi, malina, sarimsoq, yong'oq",
        'kutilayotganDaromad': "47.8 mln so'm / 50 sotix",
        'tuproqNamligi': "76% - 84% (Tabiiy yuqori namlik)",
        'hosilTonna': "32 - 45 tonna / ga",
        'textPos': [472, 148],
        'fontSize': 10,
        'color': '#3c8d6e',
        'mfys': [
            {"name": "Nanay MFY", "area": "520 ga", "spec": "Elita virusdan xoli kartoshka"},
            {"name": "Zarkent MFY", "area": "480 ga", "spec": "Malinachilik va rezavorlar"},
            {"name": "Poromon MFY", "area": "410 ga", "spec": "Tog' kartoshkasi va sabzavot"},
            {"name": "Bekobod MFY", "area": "390 ga", "spec": "Urug'chilik klasteri"},
            {"name": "Navkent MFY", "area": "440 ga", "spec": "Sarimsoq va mevali bog'lar"}
        ]
    },
    'chortoq': {
        'name': "Chortoq tumani",
        'shortName': "Chortoq",
        'number': 7,
        'boshYerHa': "3 250 ga",
        'tuproqQatlami': "Madaniy sug'oriladigan o'tloqi bo'z tuproq (Bonitet: 75 ball)",
        'mosEkinlar': "Intensiv gilos, olxo'ri, ertaki karam, sarimsoq, ko'katlar",
        'kutilayotganDaromad': "39.5 mln so'm / 50 sotix",
        'tuproqNamligi': "70% - 76% (Chortoq mineral suv havzasi)",
        'hosilTonna': "25 - 38 tonna / ga",
        'textPos': [516, 202],
        'fontSize': 11,
        'color': '#2f6f9f',
        'mfys': [
            {"name": "Muzbuloq MFY", "area": "410 ga", "spec": "Eksportbop shirin gilos"},
            {"name": "Alixon MFY", "area": "360 ga", "spec": "Olxo'ri va o'rikzorlar"},
            {"name": "Hazrati Shoh MFY", "area": "340 ga", "spec": "Sabzavotchilik va ko'katlar"},
            {"name": "Oydin MFY", "area": "380 ga", "spec": "Ertapishar karam"},
            {"name": "Gulshan MFY", "area": "350 ga", "spec": "Intensiv bog'dorchilik"}
        ]
    },
    'uychi': {
        'name': "Uychi tumani",
        'shortName': "Uychi",
        'number': 8,
        'boshYerHa': "3 350 ga",
        'tuproqQatlami': "Unumdor qumoq o'tloq tuprog'i (Bonitet: 77 ball)",
        'mosEkinlar': "Pomidor, bodring, bulg'ori, parrandachilik ozuqa ekinlari",
        'kutilayotganDaromad': "42.0 mln so'm / 50 sotix",
        'tuproqNamligi': "72% - 80% (Kafolatlangan sug'orish)",
        'hosilTonna': "40 - 60 tonna / ga",
        'textPos': [565, 202],
        'fontSize': 10,
        'color': '#b0803a',
        'mfys': [
            {"name": "Gulzor MFY", "area": "430 ga", "spec": "Pomidor va bodring issiqxonalari"},
            {"name": "Mashad MFY", "area": "390 ga", "spec": "Parrandachilik va yem ekinlari"},
            {"name": "Jiydakapa MFY", "area": "360 ga", "spec": "Ertapishar sabzavotlar"},
            {"name": "Qizil Ravot MFY", "area": "380 ga", "spec": "Sabzi va karam klasteri"}
        ]
    },
    'uchqorgon': {
        'name': "Uchqo'rg'on tumani",
        'shortName': "Uchqo'rg'on",
        'number': 9,
        'boshYerHa': "3 450 ga",
        'tuproqQatlami': "Daryobo'yi allyuvial toza oqim tuprog'i (Bonitet: 79 ball)",
        'mosEkinlar': "Intensiv baliqchilik havzalari, sholi, ko'katlar, qovun",
        'kutilayotganDaromad': "44.5 mln so'm / 50 sotix",
        'tuproqNamligi': "78% - 85% (Norin daryosi bo'yi)",
        'hosilTonna': "35 - 55 tonna / ga",
        'textPos': [616, 226],
        'fontSize': 9.5,
        'color': '#7a5aa6',
        'mfys': [
            {"name": "Qayqi MFY", "area": "460 ga", "spec": "Intensiv forel va baliqchilik"},
            {"name": "Yangiobod MFY", "area": "390 ga", "spec": "Sho'rvaxonlik va sholi"},
            {"name": "Qo'g'ay MFY", "area": "410 ga", "spec": "Poliz va sabzavotchilik"},
            {"name": "Sohil MFY", "area": "380 ga", "spec": "Daryobo'yi ekinzorlari"}
        ]
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
        'mfys': [
            {"name": "Haqqulobod MFY", "area": "490 ga", "spec": "Eksportbop Qizil piyoz"},
            {"name": "Uchtepa MFY", "area": "420 ga", "spec": "Elita sholi va dukkaklilar"},
            {"name": "Qorateri MFY", "area": "380 ga", "spec": "Piyozchilik va poliz"},
            {"name": "Sho'rariq MFY", "area": "360 ga", "spec": "Sabzavot klasteri"}
        ]
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
        'mfys': [
            {"name": "Mirishkor MFY", "area": "420 ga", "spec": "Ko'chatchilik va issiqxonalar"},
            {"name": "Sho'rqo'rg'on MFY", "area": "390 ga", "spec": "Ertapishar sabzi va pomidor"},
            {"name": "Qoratepa MFY", "area": "370 ga", "spec": "Baqlajon va bulg'ori"},
            {"name": "Tepaqo'rg'on MFY", "area": "380 ga", "spec": "Ko'katlar va parhez sabzavot"}
        ]
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
        'mfys': [
            {"name": "Yuksalish MFY", "area": "95 ga", "spec": "Issiqxona qulupnayi va sabzavot"},
            {"name": "Sihatgoh MFY", "area": "80 ga", "spec": "Gulchilik va limonariya"},
            {"name": "Afsona MFY", "area": "75 ga", "spec": "Erta pishar sabzavotchilik"},
            {"name": "Yangi Hayot MFY", "area": "65 ga", "spec": "Gidroponika ko'katlar"}
        ]
    }
}

# Attach polygon points
for p in polygons_data:
    pid = p['id']
    if pid in districts_database:
        districts_database[pid]['points'] = p['points']
        districts_database[pid]['center'] = p['center']

html_template = """<!DOCTYPE html>
<html lang="uz" class="light">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Namangan Viloyati Tumanlari Interaktiv Xaritasi</title>
  <style>
    :root {
      --bg-page: #f8fafc;
      --bg-card: #ffffff;
      --bg-card-border: #e2e8f0;
      --text-main: #0f172a;
      --text-muted: #64748b;
      --header-title: #0f172a;
      --line-green: #10b981;
      --primary: #10b981;
      --primary-hover: #059669;
      --map-bg: #182233;
      --map-stroke: #ffffff;
      --halo-color: #ffffff;
      --halo-text: #0f172a;
      --table-hover: #f1f5f9;
      --badge-bg: #ecfdf5;
      --badge-text: #065f46;
      --btn-active: #0f172a;
      --btn-active-text: #ffffff;
    }

    html.dark {
      --bg-page: #0b1120;
      --bg-card: #151e32;
      --bg-card-border: #1e293b;
      --text-main: #f8fafc;
      --text-muted: #94a3b8;
      --header-title: #f8fafc;
      --line-green: #34d399;
      --primary: #34d399;
      --primary-hover: #10b981;
      --map-bg: #0b1120;
      --map-stroke: #334155;
      --halo-color: #0b1120;
      --halo-text: #ffffff;
      --table-hover: #1e293b;
      --badge-bg: #064e3b;
      --badge-text: #a7f3d0;
      --btn-active: #38bdf8;
      --btn-active-text: #0f172a;
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
    }

    body {
      background-color: var(--bg-page);
      color: var(--text-main);
      min-height: 100vh;
      display: flex;
      flex-col;
      transition: background-color 0.3s, color 0.3s;
      padding: 16px;
    }

    .container {
      max-width: 1360px;
      margin: 0 auto;
      width: 100%;
      display: flex;
      flex-direction: column;
      gap: 16px;
    }

    /* Header styling */
    header {
      background: var(--bg-card);
      border: 1px solid var(--bg-card-border);
      border-radius: 20px;
      padding: 16px 24px;
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      justify-content: space-between;
      gap: 12px;
      box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
    }

    .header-left {
      display: flex;
      flex-direction: column;
      gap: 4px;
    }

    .portal-tag {
      font-size: 11px;
      font-weight: 800;
      color: var(--primary);
      text-transform: uppercase;
      letter-spacing: 0.08em;
    }

    .main-title {
      font-size: 22px;
      font-weight: 900;
      color: var(--header-title);
      letter-spacing: -0.02em;
    }

    .accent-bar {
      width: 100%;
      height: 4px;
      background: linear-gradient(90deg, #10b981 0%, #06b6d4 50%, #3b82f6 100%);
      border-radius: 99px;
      margin-top: 4px;
    }

    .header-right {
      display: flex;
      align-items: center;
      gap: 10px;
    }

    .theme-toggle-btn {
      background: var(--bg-page);
      border: 1px solid var(--bg-card-border);
      color: var(--text-main);
      padding: 8px 14px;
      border-radius: 12px;
      cursor: pointer;
      font-size: 13px;
      font-weight: 700;
      display: flex;
      align-items: center;
      gap: 6px;
      transition: all 0.2s;
    }
    .theme-toggle-btn:hover {
      border-color: var(--primary);
    }

    /* Main Grid */
    .dashboard-grid {
      display: grid;
      grid-template-columns: 1fr;
      gap: 16px;
      align-items: start;
    }

    @media (min-width: 992px) {
      .dashboard-grid {
        grid-template-columns: 7fr 5fr;
      }
    }

    /* Left Map Card */
    .map-card {
      background: var(--bg-card);
      border: 1px solid var(--bg-card-border);
      border-radius: 24px;
      padding: 20px;
      box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
      display: flex;
      flex-direction: column;
      gap: 14px;
    }

    .card-header-row {
      display: flex;
      align-items: center;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 8px;
    }

    .card-title {
      font-size: 15px;
      font-weight: 800;
      color: var(--text-main);
      display: flex;
      align-items: center;
      gap: 6px;
    }

    .badge-count {
      font-size: 11px;
      font-weight: 800;
      background: var(--badge-bg);
      color: var(--badge-text);
      padding: 3px 10px;
      border-radius: 99px;
      border: 1px solid var(--primary);
    }

    /* SVG Map Styling */
    .map-svg-wrap {
      background: var(--map-bg);
      border-radius: 18px;
      padding: 10px;
      position: relative;
      overflow: hidden;
      box-shadow: inset 0 2px 8px rgba(0,0,0,0.3);
    }

    svg.namangan-map {
      width: 100%;
      height: auto;
      display: block;
      overflow: visible;
    }

    .district-poly {
      cursor: pointer;
      transition: transform 0.2s ease, filter 0.2s ease, stroke-width 0.2s ease;
      stroke: #ffffff;
      stroke-width: 1.5;
      stroke-linejoin: round;
      stroke-linecap: round;
    }

    .district-poly:hover {
      filter: drop-shadow(0 0 10px rgba(255, 255, 255, 0.9)) brightness(1.15);
      stroke: #ffffff;
      stroke-width: 3;
    }

    .district-poly.active {
      filter: drop-shadow(0 0 14px #f59e0b) brightness(1.25);
      stroke: #f59e0b;
      stroke-width: 3.5;
    }

    .district-label {
      pointer-events: none;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      font-weight: 900;
      text-anchor: middle;
      paint-order: stroke fill;
      stroke: var(--halo-color);
      stroke-width: 3.5px;
      stroke-linejoin: round;
      fill: var(--halo-text);
      user-select: none;
      transition: all 0.2s;
    }

    /* Quick Selector Buttons */
    .button-selector-box {
      margin-top: 4px;
      display: flex;
      flex-direction: column;
      gap: 8px;
    }

    .selector-title {
      font-size: 12px;
      font-weight: 800;
      color: var(--text-muted);
      text-transform: uppercase;
      letter-spacing: 0.04em;
    }

    .district-buttons-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(130px, 1fr));
      gap: 6px;
    }

    .d-btn {
      background: var(--bg-page);
      border: 1px solid var(--bg-card-border);
      color: var(--text-main);
      padding: 7px 10px;
      border-radius: 10px;
      font-size: 11px;
      font-weight: 700;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 6px;
      transition: all 0.15s ease;
      text-align: left;
    }

    .d-btn:hover {
      border-color: var(--primary);
      background: var(--table-hover);
    }

    .d-btn.active {
      background: var(--btn-active);
      color: var(--btn-active-text);
      border-color: var(--primary);
      box-shadow: 0 2px 6px rgba(0,0,0,0.15);
    }

    .d-btn-dot {
      width: 10px;
      height: 10px;
      border-radius: 50%;
      flex-shrink: 0;
    }

    /* Special highlight for Namangan shahri button */
    .d-btn.shahar-highlight {
      border-color: #3b82f6;
      font-weight: 800;
    }

    /* Right Details Card */
    .details-card {
      background: var(--bg-card);
      border: 1px solid var(--bg-card-border);
      border-radius: 24px;
      padding: 24px;
      box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
      display: flex;
      flex-direction: column;
      gap: 16px;
    }

    .details-header {
      border-bottom: 1px solid var(--bg-card-border);
      padding-bottom: 12px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 10px;
    }

    .details-title-row {
      display: flex;
      align-items: center;
      gap: 10px;
    }

    .details-color-indicator {
      width: 14px;
      height: 14px;
      border-radius: 4px;
      box-shadow: 0 1px 3px rgba(0,0,0,0.2);
    }

    .selected-district-name {
      font-size: 20px;
      font-weight: 900;
      color: var(--text-main);
    }

    /* 6 Metrics Grid */
    .metrics-grid {
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 10px;
    }

    @media (max-width: 480px) {
      .metrics-grid {
        grid-template-columns: 1fr;
      }
    }

    .metric-item {
      background: var(--bg-page);
      border: 1px solid var(--bg-card-border);
      border-radius: 14px;
      padding: 12px;
      display: flex;
      flex-direction: column;
      gap: 4px;
      transition: all 0.2s;
    }

    .metric-label {
      font-size: 11px;
      font-weight: 700;
      color: var(--text-muted);
      text-transform: uppercase;
      letter-spacing: 0.03em;
      display: flex;
      align-items: center;
      gap: 4px;
    }

    .metric-value {
      font-size: 14px;
      font-weight: 800;
      color: var(--text-main);
      line-height: 1.35;
    }

    .metric-value.highlight-green {
      color: #059669;
    }
    .metric-value.highlight-gold {
      color: #d97706;
    }

    /* MFYs Section */
    .mfy-section {
      border-top: 1px solid var(--bg-card-border);
      padding-top: 14px;
      display: flex;
      flex-direction: column;
      gap: 10px;
    }

    .mfy-header-row {
      display: flex;
      align-items: center;
      justify-content: space-between;
    }

    .mfy-title {
      font-size: 13px;
      font-weight: 800;
      color: var(--text-main);
      display: flex;
      align-items: center;
      gap: 6px;
    }

    .mfy-list {
      display: flex;
      flex-direction: column;
      gap: 6px;
      max-height: 240px;
      overflow-y: auto;
      padding-right: 4px;
    }

    .mfy-item {
      background: var(--bg-page);
      border: 1px solid var(--bg-card-border);
      border-radius: 12px;
      padding: 8px 12px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 8px;
      font-size: 12px;
      transition: background 0.15s;
    }

    .mfy-item:hover {
      background: var(--table-hover);
    }

    .mfy-name {
      font-weight: 700;
      color: var(--text-main);
    }

    .mfy-spec {
      font-size: 11px;
      color: var(--text-muted);
    }

    .mfy-area {
      font-weight: 800;
      color: #059669;
      font-size: 11px;
      background: var(--badge-bg);
      padding: 2px 8px;
      border-radius: 6px;
      white-space: nowrap;
    }

    /* Official Disclaimers */
    .note-box {
      background: rgba(245, 158, 11, 0.08);
      border: 1px solid rgba(245, 158, 11, 0.3);
      border-radius: 14px;
      padding: 12px 16px;
      font-size: 12px;
      color: #92400e;
      line-height: 1.5;
    }
    html.dark .note-box {
      color: #fde68a;
      background: rgba(245, 158, 11, 0.12);
      border-color: rgba(245, 158, 11, 0.4);
    }
  </style>
</head>
<body>

  <div class="container">
    <!-- Header -->
    <header>
      <div class="header-left">
        <span class="portal-tag">Namangan viloyati ijara yerlar geoportali</span>
        <h1 class="main-title">NAMANGAN VILOYATI TUMANLARI INTERAKTIV XARITASI</h1>
        <div class="accent-bar"></div>
      </div>
      <div class="header-right">
        <button id="themeToggle" class="theme-toggle-btn">
          <span id="themeIcon">🌙</span>
          <span id="themeLabel">Tungi rejim</span>
        </button>
      </div>
    </header>

    <!-- Main Grid: Map & Card -->
    <main class="dashboard-grid">
      
      <!-- Left: Interactive Map -->
      <section class="map-card">
        <div class="card-header-row">
          <div class="card-title">
            <span>🗺️ Namangan viloyati xaritasi</span>
          </div>
          <span class="badge-count">12 ta tuman va shahar</span>
        </div>

        <!-- SVG Map Container -->
        <div class="map-svg-wrap">
          <svg class="namangan-map" viewBox="0 0 687 501" xmlns="http://www.w3.org/2000/svg">
            <defs>
              <filter id="halo-filter" x="-20%" y="-20%" width="140%" height="140%">
                <feDropShadow dx="0" dy="0" stdDeviation="1.5" flood-color="#ffffff" flood-opacity="0.95" />
              </filter>
            </defs>

            <!-- Polygons -->
            <g id="polygonsGroup">
              __SVG_POLYGONS__
            </g>

            <!-- Text Labels -->
            <g id="labelsGroup">
              __SVG_LABELS__
            </g>
          </svg>
        </div>

        <!-- Quick Selector Buttons -->
        <div class="button-selector-box">
          <div class="selector-title">Tumanlar nomi bilan tanlash (Ayniqsa kichik Namangan shahri uchun qulay):</div>
          <div class="district-buttons-grid" id="buttonsGrid">
            __BUTTONS__
          </div>
        </div>
      </section>

      <!-- Right: District Detail Passport Card -->
      <section class="details-card">
        <div class="details-header">
          <div class="details-title-row">
            <div id="districtColorIndicator" class="details-color-indicator" style="background-color: #357963;"></div>
            <h2 id="districtName" class="selected-district-name">Pop tumani</h2>
          </div>
          <span id="districtNumberBadge" class="badge-count">1-hudud</span>
        </div>

        <!-- 6 Metrics -->
        <div class="metrics-grid">
          <div class="metric-item">
            <span class="metric-label">🌾 Bo'sh yer maydoni</span>
            <span id="valBoshYer" class="metric-value highlight-green">5 200 ga</span>
          </div>

          <div class="metric-item">
            <span class="metric-label">🧪 Tuproq qatlami</span>
            <span id="valTuproq" class="metric-value">Qumloq va unumdor bo'z tuproq</span>
          </div>

          <div class="metric-item">
            <span class="metric-label">🥦 Mos ekinlar</span>
            <span id="valEkinlar" class="metric-value">Poliz (tarvuz, qovun), eksportbop mosh</span>
          </div>

          <div class="metric-item">
            <span class="metric-label">💰 Kutilayotgan daromad</span>
            <span id="valDaromad" class="metric-value highlight-gold">31.5 mln so'm / 50 sotix</span>
          </div>

          <div class="metric-item">
            <span class="metric-label">💧 Tuproq namligi</span>
            <span id="valNamlik" class="metric-value">58% - 65% (Mo'tadil)</span>
          </div>

          <div class="metric-item">
            <span class="metric-label">⚖️ Kutilayotgan hosil</span>
            <span id="valHosil" class="metric-value">25 - 35 tonna / ga</span>
          </div>
        </div>

        <!-- MFY List -->
        <div class="mfy-section">
          <div class="mfy-header-row">
            <span class="mfy-title">🏘️ MFYlar va yer maydonlari ro'yxati</span>
            <span id="mfyCount" class="badge-count">7 ta MFY</span>
          </div>
          <div id="mfyList" class="mfy-list">
            <!-- Dynamic MFY Items -->
          </div>
        </div>

        <!-- Official Disclaimer about Davlatobod & Yangi Namangan -->
        <div class="note-box">
          <strong>ℹ️ Ma'muriy-hududiy eslatma:</strong> Ushbu taqdim etilgan xarita tasvirida Namangan shahrining yangi tashkil etilgan <strong>Davlatobod tumani</strong> hamda <strong>Yangi Namangan tumani</strong> alohida chegaralarda ajratilmagan bo'lib, ular Namangan shahri va Namangan tumani hududida yaxlit qilib ko'rsatilgan.
        </div>
      </section>

    </main>
  </div>

  <script>
    const DISTRICTS_DATA = __DISTRICTS_JSON__;
    let selectedDistrictId = 'pop';

    function renderDetails(districtId) {
      selectedDistrictId = districtId;
      const data = DISTRICTS_DATA[districtId];
      if (!data) return;

      document.getElementById('districtColorIndicator').style.backgroundColor = data.color;
      document.getElementById('districtName').textContent = data.name;
      document.getElementById('districtNumberBadge').textContent = '#' + data.number + ' hudud';

      document.getElementById('valBoshYer').textContent = data.boshYerHa || '—';
      document.getElementById('valTuproq').textContent = data.tuproqQatlami || '—';
      document.getElementById('valEkinlar').textContent = data.mosEkinlar || '—';
      document.getElementById('valDaromad').textContent = data.kutilayotganDaromad || '—';
      document.getElementById('valNamlik').textContent = data.tuproqNamligi || '—';
      document.getElementById('valHosil').textContent = data.hosilTonna || '—';

      // MFY List
      const mfyListEl = document.getElementById('mfyList');
      mfyListEl.innerHTML = '';
      const mfys = data.mfys || [];
      document.getElementById('mfyCount').textContent = mfys.length + ' ta MFY';

      if (mfys.length === 0) {
        mfyListEl.innerHTML = '<div style="font-size:12px;color:var(--text-muted);padding:8px;">MFY ma\'lumotlari mavjud emas.</div>';
      } else {
        mfys.forEach(m => {
          const item = document.createElement('div');
          item.className = 'mfy-item';
          item.innerHTML = `
            <div>
              <div class="mfy-name">${m.name}</div>
              <div class="mfy-spec">${m.spec || 'Ixtisoslashuv ko\'rsatilmagan'}</div>
            </div>
            <div class="mfy-area">${m.area || '—'}</div>
          `;
          mfyListEl.appendChild(item);
        });
      }

      // Update active states on map and buttons
      document.querySelectorAll('.district-poly').forEach(p => {
        if (p.getAttribute('data-id') === districtId) {
          p.classList.add('active');
        } else {
          p.classList.remove('active');
        }
      });

      document.querySelectorAll('.d-btn').forEach(b => {
        if (b.getAttribute('data-id') === districtId) {
          b.classList.add('active');
        } else {
          b.classList.remove('active');
        }
      });
    }

    // Attach click events to polygons
    document.querySelectorAll('.district-poly').forEach(poly => {
      poly.addEventListener('click', () => {
        const id = poly.getAttribute('data-id');
        renderDetails(id);
      });
    });

    // Attach click events to buttons
    document.querySelectorAll('.d-btn').forEach(btn => {
      btn.addEventListener('click', () => {
        const id = btn.getAttribute('data-id');
        renderDetails(id);
      });
    });

    // Theme toggle
    const themeBtn = document.getElementById('themeToggle');
    const themeIcon = document.getElementById('themeIcon');
    const themeLabel = document.getElementById('themeLabel');

    themeBtn.addEventListener('click', () => {
      const isDark = document.documentElement.classList.toggle('dark');
      if (isDark) {
        themeIcon.textContent = '☀️';
        themeLabel.textContent = 'Kunduzgi rejim';
      } else {
        themeIcon.textContent = '🌙';
        themeLabel.textContent = 'Tungi rejim';
      }
    });

    // Initial render
    renderDetails('pop');
  </script>
</body>
</html>
"""

# Build SVG Polygons & Labels & Buttons
svg_polygons = []
svg_labels = []
buttons_html = []

for p in polygons_data:
    pid = p['id']
    dinfo = districts_database.get(pid, {})
    name = dinfo.get('name', p['name'])
    short_name = dinfo.get('shortName', p['name'])
    color = dinfo.get('color', p['color'])
    pts = p['points']
    tpos = dinfo.get('textPos', p['center'])
    fsize = dinfo.get('fontSize', 11)
    
    # Polygon element
    svg_polygons.append(f'''
      <polygon 
        id="poly-{pid}" 
        data-id="{pid}" 
        class="district-poly" 
        points="{pts}" 
        fill="{color}">
        <title>{name}</title>
      </polygon>
    ''')
    
    # Text label element
    svg_labels.append(f'''
      <text 
        x="{tpos[0]}" 
        y="{tpos[1]}" 
        class="district-label" 
        style="font-size: {fsize}px;">
        {short_name}
      </text>
    ''')
    
    # Button
    shahar_class = " shahar-highlight" if pid == 'namangan-shahri' else ""
    buttons_html.append(f'''
      <button class="d-btn{shahar_class}" data-id="{pid}">
        <span class="d-btn-dot" style="background-color: {color};"></span>
        <span>{short_name}</span>
      </button>
    ''')

# Assemble final HTML
final_html = html_template.replace('__SVG_POLYGONS__', '\n'.join(svg_polygons))
final_html = final_html.replace('__SVG_LABELS__', '\n'.join(svg_labels))
final_html = final_html.replace('__BUTTONS__', '\n'.join(buttons_html))
final_html = final_html.replace('__DISTRICTS_JSON__', json.dumps(districts_database, ensure_ascii=False))

with open('namangan_interaktiv_xarita.html', 'w', encoding='utf-8') as f:
    f.write(final_html)

with open('public/namangan_interaktiv_xarita.html', 'w', encoding='utf-8') as f:
    f.write(final_html)

print("Generated namangan_interaktiv_xarita.html and public/namangan_interaktiv_xarita.html successfully!")
