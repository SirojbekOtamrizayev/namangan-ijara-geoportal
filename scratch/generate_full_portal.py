import json

with open('scratch/districts_compiled.json', 'r', encoding='utf-8') as f:
    districts = json.load(f)

with open('scratch/districts_polygons.json', 'r', encoding='utf-8') as f:
    polygons_list = json.load(f)

district_centers = {
    'pop': [40.875, 71.100],
    'chust': [41.005, 71.230],
    'mingbuloq': [40.755, 71.500],
    'toraqorgon': [41.002, 71.515],
    'kosonsoy': [41.135, 71.550],
    'yangiqorgon': [41.195, 71.730],
    'chortoq': [41.065, 71.820],
    'uychi': [41.085, 71.905],
    'uchqorgon': [41.115, 72.080],
    'norin': [40.935, 72.020],
    'namangan-tumani': [40.985, 71.650],
    'namangan-shahri': [40.998, 71.672]
}

for did, coords in district_centers.items():
    if did in districts:
        districts[did]['latlon'] = coords

svg_polygons = []
svg_labels = []
buttons_html = []

for p in polygons_list:
    pid = p['id']
    dinfo = districts.get(pid, {})
    name = dinfo.get('name', p['name'])
    short_name = dinfo.get('shortName', p['name'])
    color = dinfo.get('color', p['color'])
    pts = p['points']
    tpos = dinfo.get('textPos', p['center'])
    fsize = dinfo.get('fontSize', 11)
    
    svg_polygons.append(f'''      <polygon id="poly-{pid}" data-id="{pid}" class="district-poly" points="{pts}" fill="{color}"><title>{name}</title></polygon>''')
    svg_labels.append(f'''      <text id="label-{pid}" x="{tpos[0]}" y="{tpos[1]}" class="district-label" data-id="{pid}" style="font-size:{fsize}px;">{short_name}</text>''')
    shahar_class = " shahar-highlight" if pid == 'namangan-shahri' else ""
    buttons_html.append(f'''      <button class="d-btn{shahar_class}" data-id="{pid}"><span class="d-btn-dot" style="background-color:{color};"></span><span>{short_name}</span></button>''')

districts_json = json.dumps(districts, ensure_ascii=False)

# Read modal part and js part
with open('scratch/modal_part.txt', 'r', encoding='utf-8') as f:
    modal_part = f.read()

with open('scratch/js_part.txt', 'r', encoding='utf-8') as f:
    js_part = f.read()

# Replace Python escaped {{ }} back to single { } in js_part and modal_part
js_part_clean = js_part.replace('{{', '{').replace('}}', '}')
modal_part_clean = modal_part.replace('{{', '{').replace('}}', '}')

# Replace DATA placeholder with actual JSON
js_part_clean = js_part_clean.replace('{districts_json}', districts_json)

template = """<!DOCTYPE html>
<html lang="uz" class="light">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Namangan Viloyati Bandlik va Geoportal Tizimi</title>
  <!-- SheetJS (xlsx) kutubxonasi Excel fayllarni o'qish uchun -->
  <script src="https://cdn.jsdelivr.net/npm/xlsx@0.18.5/dist/xlsx.full.min.js"></script>
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800;900&display=swap');

    /* --- LIGHT MODE --- */
    :root {
      --bg: #f4f6fa;
      --card: #ffffff;
      --border: #e2e8f0;
      --border-subtle: #edf2f7;
      --text: #0f172a;
      --text-sub: #475569;
      --muted: #64748b;
      --primary: #0284c7;
      --primary-hover: #0369a1;
      --primary-light: #e0f2fe;
      --sidebar-bg: #ffffff;
      --sidebar-border: #e2e8f0;
      --sidebar-active: #0284c7;
      --header-bg: #ffffff;
      --header-border: #e2e8f0;
      --inner: #f8fafc;
      --hover: #f1f5f9;
      --badge-bg: #ecfdf5;
      --badge-text: #047857;
      --map-bg: #1e293b;
      --card-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.06), 0 1px 2px 0 rgba(0, 0, 0, 0.04);
      --card-shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.07), 0 4px 6px -2px rgba(0, 0, 0, 0.03);
    }

    /* --- DARK MODE --- */
    html.dark {
      --bg: #0b1120;
      --card: #151e32;
      --border: #1e293b;
      --border-subtle: #1e293b;
      --text: #f8fafc;
      --text-sub: #cbd5e1;
      --muted: #94a3b8;
      --primary: #38bdf8;
      --primary-hover: #0284c7;
      --primary-light: rgba(56, 189, 248, 0.15);
      --sidebar-bg: #0f172a;
      --sidebar-border: #1e293b;
      --sidebar-active: #0284c7;
      --header-bg: #0f172a;
      --header-border: #1e293b;
      --inner: #1e293b;
      --hover: #1e293b;
      --badge-bg: rgba(6, 78, 59, 0.5);
      --badge-text: #6ee7b7;
      --map-bg: #090e1a;
      --card-shadow: 0 4px 12px rgba(0, 0, 0, 0.4);
      --card-shadow-lg: 0 14px 28px rgba(0, 0, 0, 0.5);
    }

    * { 
      box-sizing: border-box; 
      margin: 0; 
      padding: 0; 
      font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      -webkit-font-smoothing: antialiased;
    }

    body { 
      background: var(--bg); 
      color: var(--text); 
      min-height: 100vh;
      display: flex;
      overflow-x: hidden;
      transition: background .25s, color .25s; 
    }

    /* SIDEBAR */
    .app-sidebar {
      width: 250px;
      background: var(--sidebar-bg);
      border-right: 1px solid var(--sidebar-border);
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      flex-shrink: 0;
      z-index: 50;
      transition: all 0.25s ease;
    }

    .sidebar-brand {
      padding: 16px 18px;
      display: flex;
      align-items: center;
      gap: 12px;
      border-bottom: 1px solid var(--sidebar-border);
    }

    .sidebar-gerb {
      width: 36px;
      height: 36px;
      object-fit: contain;
      flex-shrink: 0;
    }

    .sidebar-org-text {
      display: flex;
      flex-direction: column;
      line-height: 1.15;
    }
    .sidebar-org-title {
      font-size: 8.5px;
      font-weight: 800;
      color: var(--primary);
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }
    .sidebar-org-sub {
      font-size: 10.5px;
      font-weight: 800;
      color: var(--text);
      line-height: 1.25;
      margin-top: 2px;
    }

    .sidebar-menu {
      padding: 14px 10px;
      display: flex;
      flex-direction: column;
      gap: 4px;
      flex: 1;
    }

    .menu-item {
      display: flex;
      align-items: center;
      gap: 11px;
      padding: 10px 14px;
      border-radius: 10px;
      font-size: 13px;
      font-weight: 700;
      color: var(--text-sub);
      cursor: pointer;
      transition: all 0.15s ease;
      text-decoration: none;
      position: relative;
    }

    .menu-item:hover {
      background: var(--hover);
      color: var(--text);
    }

    .menu-item.active {
      background: #0284c7;
      color: #ffffff;
      box-shadow: 0 4px 12px rgba(2, 132, 199, 0.3);
    }

    .menu-item.active .menu-icon {
      color: #ffffff;
    }

    .menu-icon {
      font-size: 16px;
      width: 20px;
      display: flex;
      align-items: center;
      justify-content: center;
      color: var(--muted);
      flex-shrink: 0;
    }

    .menu-arrow {
      margin-left: auto;
      font-size: 11px;
      color: var(--muted);
    }
    .menu-item.active .menu-arrow {
      color: #ffffff;
    }

    /* MAIN WRAPPER */
    .app-main {
      flex: 1;
      display: flex;
      flex-direction: column;
      min-width: 0;
      min-height: 100vh;
    }

    /* TOP NAVBAR */
    .app-topbar {
      height: 64px;
      background: var(--header-bg);
      border-bottom: 1px solid var(--header-border);
      padding: 0 24px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 16px;
      position: sticky;
      top: 0;
      z-index: 40;
    }

    .topbar-left {
      display: flex;
      align-items: center;
      gap: 14px;
    }

    .topbar-menu-toggle {
      font-size: 18px;
      cursor: pointer;
      color: var(--muted);
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 6px;
      border-radius: 8px;
    }
    .topbar-menu-toggle:hover { background: var(--hover); }

    .region-badge {
      display: flex;
      align-items: center;
      gap: 8px;
      font-size: 13.5px;
      font-weight: 800;
      color: var(--text);
    }
    .region-dot {
      width: 8px;
      height: 8px;
      border-radius: 50%;
      background: #10b981;
      box-shadow: 0 0 6px #10b981;
    }

    .topbar-right {
      display: flex;
      align-items: center;
      gap: 10px;
      flex-wrap: nowrap;
    }

    .topbar-select {
      background: var(--inner);
      border: 1px solid var(--border);
      border-radius: 9px;
      padding: 6px 10px;
      font-size: 12px;
      font-weight: 700;
      color: var(--text);
      outline: none;
    }

    .topbar-update-btn {
      background: #0284c7;
      color: #ffffff;
      border: none;
      padding: 7px 14px;
      border-radius: 9px;
      font-size: 12px;
      font-weight: 800;
      cursor: pointer;
      transition: background 0.2s;
    }
    .topbar-update-btn:hover { background: #0369a1; }

    .user-pill {
      display: flex;
      align-items: center;
      gap: 8px;
      padding: 4px 10px;
      background: var(--inner);
      border: 1px solid var(--border);
      border-radius: 99px;
      font-size: 12px;
      font-weight: 800;
      color: var(--text);
    }
    .user-avatar {
      width: 24px;
      height: 24px;
      border-radius: 50%;
      background: #0284c7;
      color: #fff;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 11px;
    }

    .top-weather {
      display: flex;
      align-items: center;
      gap: 6px;
      background: var(--inner);
      border: 1px solid var(--border);
      border-radius: 9px;
      padding: 4px 10px;
      font-size: 12px;
      font-weight: 800;
    }

    .top-admin-btn {
      background: linear-gradient(135deg, #0284c7 0%, #0369a1 100%);
      color: #ffffff;
      border: 1px solid rgba(255, 255, 255, 0.2);
      padding: 6px 12px;
      border-radius: 9px;
      font-size: 12px;
      font-weight: 800;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 6px;
      transition: transform 0.15s;
    }
    .top-admin-btn:hover { transform: translateY(-1px); }

    .top-theme-btn {
      background: var(--inner);
      border: 1px solid var(--border);
      color: var(--text);
      width: 32px;
      height: 32px;
      border-radius: 9px;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 15px;
      transition: all 0.2s;
    }
    .top-theme-btn:hover { border-color: var(--primary); }

    .app-content {
      padding: 22px 24px;
      flex: 1;
      display: flex;
      flex-direction: column;
      gap: 20px;
    }

    .view-container { display: none; }
    .view-container.active { display: flex; flex-direction: column; gap: 20px; }

    /* DASHBOARD STYLES */
    .dash-header-title {
      font-size: 18px;
      font-weight: 900;
      color: var(--text);
      letter-spacing: -0.01em;
      text-transform: uppercase;
      margin-bottom: 2px;
    }

    .kpi-row {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 16px;
    }
    @media (max-width: 1200px) {
      .kpi-row { grid-template-columns: repeat(2, 1fr); }
    }
    @media (max-width: 640px) {
      .kpi-row { grid-template-columns: 1fr; }
    }

    .kpi-card {
      background: var(--card);
      border: 1px solid var(--border);
      border-radius: 16px;
      padding: 16px 18px;
      display: flex;
      flex-direction: column;
      gap: 12px;
      box-shadow: var(--card-shadow);
      position: relative;
    }

    .kpi-title-row {
      display: flex;
      align-items: center;
      gap: 8px;
      font-size: 12px;
      font-weight: 800;
      color: var(--text-sub);
      text-transform: uppercase;
      letter-spacing: 0.04em;
    }
    .kpi-icon {
      font-size: 16px;
      color: #0284c7;
    }

    .kpi-numbers {
      display: flex;
      align-items: baseline;
      justify-content: space-between;
    }
    .kpi-col {
      display: flex;
      flex-direction: column;
      gap: 2px;
    }
    .kpi-lbl {
      font-size: 10.5px;
      font-weight: 700;
      color: var(--muted);
      text-transform: uppercase;
    }
    .kpi-val {
      font-size: 22px;
      font-weight: 900;
      color: var(--text);
      letter-spacing: -0.02em;
    }
    .kpi-val.primary {
      color: #0284c7;
    }

    .kpi-progress {
      width: 100%;
      height: 6px;
      background: var(--inner);
      border-radius: 99px;
      overflow: hidden;
      display: flex;
    }
    .kpi-progress-bar {
      height: 100%;
      background: #10b981;
      border-radius: 99px;
    }

    .kpi-footer {
      display: flex;
      align-items: center;
      justify-content: space-between;
      font-size: 11px;
      font-weight: 700;
      color: var(--muted);
      border-top: 1px solid var(--border-subtle);
      padding-top: 8px;
    }

    .charts-row {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 16px;
    }
    @media (max-width: 900px) {
      .charts-row { grid-template-columns: 1fr; }
    }

    .chart-card {
      background: var(--card);
      border: 1px solid var(--border);
      border-radius: 16px;
      padding: 18px 20px;
      box-shadow: var(--card-shadow);
      display: flex;
      flex-direction: column;
      gap: 14px;
    }
    .chart-title {
      font-size: 14px;
      font-weight: 800;
      color: var(--text);
    }

    .donut-layout {
      display: flex;
      align-items: center;
      gap: 24px;
      flex-wrap: wrap;
    }

    .donut-circle {
      width: 130px;
      height: 130px;
      border-radius: 50%;
      position: relative;
      display: flex;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
    }
    .donut-inner {
      width: 80px;
      height: 80px;
      background: var(--card);
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 12px;
      font-weight: 800;
      color: var(--text);
    }

    .legend-list {
      display: flex;
      flex-direction: column;
      gap: 8px;
      flex: 1;
    }
    .legend-item {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 10px;
      font-size: 12px;
      font-weight: 700;
      color: var(--text);
    }
    .legend-dot-name {
      display: flex;
      align-items: center;
      gap: 8px;
    }
    .legend-dot {
      width: 10px;
      height: 10px;
      border-radius: 50%;
      flex-shrink: 0;
    }

    .sectors-card {
      background: var(--card);
      border: 1px solid var(--border);
      border-radius: 16px;
      padding: 18px 20px;
      box-shadow: var(--card-shadow);
      display: flex;
      flex-direction: column;
      gap: 14px;
    }

    .sectors-grid {
      display: grid;
      grid-template-columns: repeat(6, 1fr);
      gap: 12px;
    }
    @media (max-width: 1100px) {
      .sectors-grid { grid-template-columns: repeat(3, 1fr); }
    }
    @media (max-width: 600px) {
      .sectors-grid { grid-template-columns: repeat(2, 1fr); }
    }

    .sector-item {
      background: var(--inner);
      border: 1px solid var(--border);
      border-radius: 12px;
      padding: 12px;
      display: flex;
      flex-direction: column;
      gap: 6px;
    }
    .sector-name {
      font-size: 11.5px;
      font-weight: 800;
      color: var(--text-sub);
    }
    .sector-numbers {
      display: flex;
      align-items: baseline;
      justify-content: space-between;
      gap: 4px;
    }
    .sec-plan {
      font-size: 10px;
      color: var(--muted);
      font-weight: 700;
    }
    .sec-fact {
      font-size: 13.5px;
      font-weight: 900;
      color: #0284c7;
    }

    /* GEOPORTAL MAP STYLES */
    .geo-header {
      background: linear-gradient(135deg, #0284c7 0%, #0369a1 50%, #0f172a 100%);
      border-radius: 18px;
      padding: 16px 24px;
      color: #ffffff;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 16px;
      flex-wrap: wrap;
      box-shadow: var(--card-shadow);
    }
    .geo-tag {
      font-size: 11px;
      font-weight: 800;
      color: #38bdf8;
      text-transform: uppercase;
      letter-spacing: 0.1em;
    }
    .geo-title {
      font-size: 20px;
      font-weight: 900;
      color: #ffffff;
      letter-spacing: -0.02em;
    }

    .grid { display: grid; grid-template-columns: 1fr; gap: 18px; align-items: start; }
    @media(min-width:992px) { .grid { grid-template-columns: 7fr 5fr; } }

    .card { 
      background: var(--card); 
      border: 1px solid var(--border); 
      border-radius: 20px; 
      padding: 20px;
      box-shadow: var(--card-shadow); 
      display: flex; 
      flex-direction: column; 
      gap: 16px; 
    }
    .card-header { display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 8px; }
    .card-title { font-size: 15px; font-weight: 800; color: var(--text); display: flex; align-items: center; gap: 8px; }
    .badge { 
      font-size: 11px; 
      font-weight: 800; 
      background: var(--badge-bg); 
      color: var(--badge-text);
      padding: 3px 10px; 
      border-radius: 99px; 
      border: 1px solid rgba(16, 185, 129, 0.3); 
    }

    .map-wrap { 
      background: var(--map-bg); 
      border: 1px solid var(--border);
      border-radius: 16px; 
      padding: 12px; 
      overflow: hidden;
      box-shadow: inset 0 2px 14px rgba(0,0,0,.3); 
    }
    svg.main-map { width: 100%; height: auto; display: block; filter: drop-shadow(0 4px 12px rgba(0,0,0,0.3)); }
    .district-poly { 
      cursor: pointer; 
      stroke: rgba(255, 255, 255, 0.9); 
      stroke-width: 1.4; 
      stroke-linejoin: round;
      transition: filter .25s ease, stroke-width .2s ease; 
    }
    .district-poly:hover { 
      filter: brightness(1.22) drop-shadow(0 0 10px rgba(56, 189, 248, 0.8)); 
      stroke: #ffffff;
      stroke-width: 2.8; 
    }
    .district-poly.active { 
      filter: brightness(1.28) drop-shadow(0 0 16px #f59e0b); 
      stroke: #f59e0b; 
      stroke-width: 3.5; 
    }
    .district-label { 
      font-weight: 800; 
      text-anchor: middle; 
      dominant-baseline: middle;
      pointer-events: none; 
      fill: #ffffff; 
      paint-order: stroke fill;
      stroke: rgba(0,0,0,.95); 
      stroke-width: 3px; 
      stroke-linecap: round; 
      letter-spacing: 0.02em;
    }

    .btn-box { display: flex; flex-direction: column; gap: 8px; }
    .btn-label { font-size: 11.5px; font-weight: 800; color: var(--muted); text-transform: uppercase; letter-spacing: .06em; }
    .btn-grid { display: flex; flex-wrap: wrap; gap: 6px; }
    .d-btn { 
      background: var(--inner); 
      border: 1px solid var(--border); 
      border-radius: 10px; 
      padding: 6px 11px;
      font-size: 11.5px; 
      font-weight: 700; 
      color: var(--text); 
      cursor: pointer;
      display: inline-flex; 
      align-items: center; 
      gap: 6px; 
      transition: all .2s; 
    }
    .d-btn:hover { 
      border-color: #38bdf8; 
      background: var(--hover); 
      transform: translateY(-1px); 
    }
    .d-btn.active { 
      background: #0284c7; 
      color: #ffffff; 
      border-color: #38bdf8; 
      box-shadow: 0 2px 8px rgba(2, 132, 199, 0.4); 
    }
    .d-btn.shahar-highlight { 
      border-color: rgba(56, 189, 248, 0.4); 
      background: rgba(56, 189, 248, 0.12); 
    }
    .d-btn-dot { width: 8px; height: 8px; border-radius: 50%; flex-shrink: 0; box-shadow: 0 0 4px rgba(0,0,0,0.4); }

    .detail-header { display: flex; align-items: center; justify-content: space-between; border-bottom: 1px solid var(--border); padding-bottom: 12px; gap: 8px; }
    .detail-name-row { display: flex; align-items: center; gap: 10px; }
    .color-dot { width: 14px; height: 14px; border-radius: 4px; box-shadow: 0 0 8px rgba(0,0,0,.2); }
    .district-name { font-size: 18px; font-weight: 900; color: var(--text); }
    .metrics-grid { display: grid; grid-template-columns: repeat(2,1fr); gap: 10px; }
    @media(max-width:600px) { .metrics-grid { grid-template-columns: 1fr; } }
    .metric { 
      background: var(--inner); 
      border: 1px solid var(--border); 
      border-radius: 12px; 
      padding: 10px 12px;
      display: flex; 
      flex-direction: column; 
      gap: 4px; 
    }
    .metric-k { font-size: 10.5px; font-weight: 700; color: var(--muted); }
    .metric-v { font-size: 13.5px; font-weight: 800; color: var(--text); line-height: 1.35; }
    .green { color: #059669; } .gold { color: #d97706; }
    html.dark .green { color: #34d399; } html.dark .gold { color: #fbbf24; }

    .open-drill-btn { 
      background: linear-gradient(135deg, #10b981 0%, #059669 100%); 
      color: #fff; 
      border: 1px solid rgba(255, 255, 255, 0.15);
      padding: 12px 18px; 
      border-radius: 12px; 
      font-size: 13px; 
      font-weight: 800; 
      cursor: pointer;
      display: flex; 
      align-items: center; 
      justify-content: center; 
      gap: 8px;
      box-shadow: 0 4px 14px rgba(16, 185, 129, 0.35); 
      transition: all .2s ease; 
    }
    .open-drill-btn:hover { 
      transform: translateY(-2px); 
      box-shadow: 0 6px 18px rgba(16, 185, 129, 0.5); 
    }

    .mfy-section { border-top: 1px solid var(--border); padding-top: 12px; display: flex; flex-direction: column; gap: 8px; }
    .mfy-header { display: flex; align-items: center; justify-content: space-between; }
    .mfy-title { font-size: 12.5px; font-weight: 800; color: var(--text); display: flex; align-items: center; gap: 6px; }
    .mfy-list { display: flex; flex-direction: column; gap: 6px; max-height: 180px; overflow-y: auto; padding-right: 4px; }
    .mfy-item { 
      background: var(--inner); 
      border: 1px solid var(--border); 
      border-radius: 10px; 
      padding: 8px 10px;
      display: flex; 
      align-items: center; 
      justify-content: space-between; 
      gap: 6px;
      font-size: 11.5px; 
      cursor: pointer; 
      transition: all .15s; 
    }
    .mfy-item:hover { 
      background: var(--hover); 
      border-color: rgba(56, 189, 248, 0.4); 
      transform: translateX(2px);
    }
    .mfy-name { font-weight: 800; color: var(--text); }
    .mfy-spec { font-size: 10.5px; color: var(--muted); }
    .mfy-area-tag { 
      font-weight: 800; 
      color: #059669; 
      font-size: 11px;
      background: var(--badge-bg); 
      padding: 2px 7px; 
      border-radius: 6px; 
      white-space: nowrap; 
    }
    html.dark .mfy-area-tag { color: #34d399; }

    .note { 
      background: rgba(245, 158, 11, 0.08); 
      border: 1px solid rgba(245, 158, 11, 0.25); 
      border-radius: 12px;
      padding: 10px 14px; 
      font-size: 11.5px; 
      color: #d97706; 
      line-height: 1.45; 
    }
    html.dark .note { color: #fde68a; background: rgba(245,158,11,.12); }

    /* MODAL STYLES */
    .modal-overlay {
      display: none;
      position: fixed; inset: 0; z-index: 1000;
      background: rgba(0,0,0,.65);
      backdrop-filter: blur(4px);
      padding: 20px;
      align-items: center;
      justify-content: center;
    }
    .modal-overlay.open { display: flex; }
    .modal-box {
      background: var(--card);
      border: 1px solid var(--border);
      border-radius: 20px;
      width: 100%;
      max-width: 1320px;
      max-height: 92vh;
      display: grid;
      grid-template-columns: 310px 1fr 340px;
      grid-template-rows: auto 1fr;
      overflow: hidden;
      box-shadow: 0 25px 50px rgba(0,0,0,.5);
    }
    @media(max-width:1100px) { .modal-box { grid-template-columns: 260px 1fr 300px; } }
    @media(max-width:860px) { .modal-box { grid-template-columns: 1fr; grid-template-rows: auto auto auto auto; max-height: 95vh; overflow-y: auto; } }

    .modal-header {
      grid-column: 1 / -1;
      background: var(--card);
      border-bottom: 1px solid var(--border);
      padding: 12px 18px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 12px;
    }
    .modal-title-row { display: flex; align-items: center; gap: 8px; }
    .modal-color-dot { width: 14px; height: 14px; border-radius: 4px; }
    .modal-district-name { font-size: 16px; font-weight: 900; color: var(--text); }
    .modal-close-btn {
      background: #ef4444; color: #fff; border: none;
      width: 32px; height: 32px; border-radius: 8px;
      font-size: 16px; font-weight: 900; cursor: pointer;
      display: flex; align-items: center; justify-content: center;
    }
    .modal-close-btn:hover { background: #dc2626; }

    .modal-mfy-panel { border-right: 1px solid var(--border); display: flex; flex-direction: column; gap: 8px; padding: 14px; overflow: hidden; }
    .modal-panel-title { font-size: 12px; font-weight: 800; color: var(--text); display: flex; align-items: center; gap: 6px; border-bottom: 1px solid var(--border); padding-bottom: 6px; }
    .modal-search { width: 100%; background: var(--inner); border: 1px solid var(--border); border-radius: 8px; padding: 7px 10px; font-size: 11.5px; color: var(--text); outline: none; }
    .modal-search:focus { border-color: var(--primary); }
    .modal-mfy-scroll { display: flex; flex-direction: column; gap: 6px; overflow-y: auto; flex: 1; padding-right: 4px; }
    .modal-mfy-item { background: var(--inner); border: 1px solid var(--border); border-radius: 10px; padding: 8px 10px; cursor: pointer; display: flex; flex-direction: column; gap: 3px; transition: all .15s; }
    .modal-mfy-item:hover { border-color: var(--primary); background: var(--hover); transform: translateX(2px); }
    .modal-mfy-item.active { background: rgba(16,185,129,.1); border-color: var(--primary); box-shadow: 0 0 0 1px var(--primary); }
    .mmfy-name { font-size: 12px; font-weight: 800; color: var(--text); }
    .mmfy-spec { font-size: 10.5px; color: var(--muted); }
    .mmfy-meta { display: flex; align-items: center; gap: 6px; font-size: 10px; margin-top: 2px; }
    .mmfy-tag { background: var(--badge-bg); color: var(--badge-text); padding: 1px 5px; border-radius: 4px; font-weight: 700; }

    .modal-map-panel { display: flex; flex-direction: column; gap: 8px; padding: 14px; overflow: hidden; }
    .zoom-map-frame { background: #000; border-radius: 14px; flex: 1; min-height: 360px; position: relative; overflow: hidden; border: 1px solid var(--border); }
    .gmaps-iframe { width: 100%; height: 100%; min-height: 360px; border: none; display: block; }
    .gmaps-floating-badge { position: absolute; top: 10px; left: 10px; background: rgba(15, 23, 42, 0.85); backdrop-filter: blur(4px); color: #38bdf8; border: 1px solid rgba(56, 189, 248, 0.4); padding: 4px 10px; border-radius: 99px; font-size: 11px; font-weight: 800; z-index: 10; pointer-events: none; }
    .map-stats { display: grid; grid-template-columns: repeat(3,1fr); gap: 6px; }
    .map-stat { background: var(--inner); border: 1px solid var(--border); border-radius: 8px; padding: 6px 8px; display: flex; flex-direction: column; gap: 1px; }
    .ms-k { font-size: 9.5px; color: var(--muted); }
    .ms-v { font-size: 11px; font-weight: 800; color: var(--text); }

    .modal-parcel-panel { border-left: 1px solid var(--border); display: flex; flex-direction: column; gap: 8px; padding: 14px; overflow: hidden; }
    .parcel-panel-header { border-bottom: 1px solid var(--border); padding-bottom: 6px; }
    .parcel-panel-title { font-size: 13px; font-weight: 800; color: var(--text); }
    .parcel-panel-sub { font-size: 10.5px; color: var(--muted); margin-top: 1px; }
    .parcel-scroll { display: flex; flex-direction: column; gap: 8px; overflow-y: auto; flex: 1; padding-right: 4px; }
    .parcel-card { background: var(--inner); border: 1px solid var(--border); border-radius: 12px; padding: 10px; display: flex; flex-direction: column; gap: 6px; }
    .parcel-top { display: flex; align-items: center; justify-content: space-between; border-bottom: 1px dashed var(--border); padding-bottom: 5px; }
    .kontur-badge { background: #0284c7; color: #fff; font-size: 10.5px; font-weight: 800; padding: 2px 7px; border-radius: 5px; }
    .area-green { color: #059669; font-weight: 800; font-size: 12px; }
    .farmer-name { font-size: 12px; font-weight: 800; color: var(--text); }
    .farmer-sub { font-size: 10.5px; color: var(--muted); }
    .parcel-props { display: grid; grid-template-columns: repeat(2,1fr); gap: 5px; }
    .prop-box { background: var(--card); border: 1px solid var(--border); border-radius: 6px; padding: 5px 6px; display: flex; flex-direction: column; gap: 1px; }
    .pk { font-size: 9.5px; color: var(--muted); }
    .pv { font-size: 11px; font-weight: 700; color: var(--text); }
    .pv.gold { color: #d97706; } .pv.green { color: #059669; }
    .gmaps-link-btn { display: inline-flex; align-items: center; justify-content: center; gap: 4px; background: #1e293b; color: #38bdf8; border: 1px solid #38bdf8; border-radius: 6px; padding: 5px 8px; font-size: 10.5px; font-weight: 700; text-decoration: none; cursor: pointer; }
    .no-select-msg { display: flex; flex-direction: column; align-items: center; justify-content: center; flex: 1; gap: 8px; color: var(--muted); font-size: 12px; text-align: center; padding: 16px; }

    /* ADMIN MODALS */
    .admin-modal-overlay { display: none; position: fixed; inset: 0; z-index: 2000; background: rgba(0,0,0,.75); backdrop-filter: blur(5px); padding: 20px; align-items: center; justify-content: center; }
    .admin-modal-overlay.open { display: flex; }
    .admin-login-box { background: var(--card); border: 1px solid var(--border); border-radius: 18px; width: 100%; max-width: 400px; padding: 22px; display: flex; flex-direction: column; gap: 14px; box-shadow: 0 25px 50px rgba(0,0,0,.6); }
    .admin-modal-box { background: var(--card); border: 1px solid var(--border); border-radius: 20px; width: 100%; max-width: 1050px; max-height: 90vh; display: flex; flex-direction: column; overflow: hidden; box-shadow: 0 30px 60px rgba(0,0,0,.6); }
    .admin-modal-header { background: var(--card); border-bottom: 1px solid var(--border); padding: 16px 20px; display: flex; align-items: center; justify-content: space-between; }
    .admin-header-title { display: flex; align-items: center; gap: 8px; }
    .admin-title-text { font-size: 16px; font-weight: 900; color: var(--text); }
    .admin-badge { background: #0284c7; color: #fff; font-size: 10.5px; font-weight: 800; padding: 2px 8px; border-radius: 99px; }
    .admin-content-tabs { display: flex; background: var(--inner); border-bottom: 1px solid var(--border); padding: 0 20px; gap: 6px; overflow-x: auto; }
    .admin-tab { padding: 10px 14px; font-size: 12px; font-weight: 800; color: var(--muted); cursor: pointer; border-bottom: 3px solid transparent; transition: all 0.2s; white-space: nowrap; }
    .admin-tab.active { color: var(--primary); border-bottom-color: var(--primary); }
    .admin-body { padding: 18px 20px; overflow-y: auto; flex: 1; display: flex; flex-direction: column; gap: 14px; }
    .admin-form-grid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 12px; }
    .form-group { display: flex; flex-direction: column; gap: 4px; }
    .form-label { font-size: 11.5px; font-weight: 700; color: var(--text); }
    .form-input, .form-select { background: var(--inner); border: 1px solid var(--border); border-radius: 8px; padding: 8px 10px; font-size: 12px; color: var(--text); outline: none; }
    .admin-submit-btn { background: linear-gradient(135deg, #10b981 0%, #059669 100%); color: #fff; border: none; padding: 10px 16px; border-radius: 10px; font-size: 12.5px; font-weight: 800; cursor: pointer; display: inline-flex; align-items: center; justify-content: center; gap: 6px; }
    .data-table-container { border: 1px solid var(--border); border-radius: 12px; overflow-x: auto; max-height: 380px; }
    .admin-table { width: 100%; border-collapse: collapse; font-size: 11.5px; text-align: left; }
    .admin-table th { background: var(--inner); padding: 9px 12px; font-weight: 800; color: var(--muted); border-bottom: 1px solid var(--border); white-space: nowrap; }
    .admin-table td { padding: 9px 12px; border-bottom: 1px solid var(--border); color: var(--text); }
  </style>
</head>
<body>

  <!-- LEFT SIDEBAR -->
  <aside class="app-sidebar" id="appSidebar">
    <div class="sidebar-brand">
      <img src="gerb.svg" alt="Gerb" class="sidebar-gerb" onerror="this.src='https://upload.wikimedia.org/wikipedia/commons/7/77/Emblem_of_Uzbekistan.svg'">
      <div class="sidebar-org-text">
        <span class="sidebar-org-title">O'ZBEKISTON RESPUBLIKASI</span>
        <span class="sidebar-org-sub">Kambag'allikni qisqartirish va bandlik vazirligi</span>
      </div>
    </div>

    <nav class="sidebar-menu">
      <div class="menu-item active" id="menuStats" onclick="switchMainView('stats')">
        <span class="menu-icon">📊</span>
        <span>Asosiy statistika</span>
      </div>
      <div class="menu-item" id="menuMap" onclick="switchMainView('map')">
        <span class="menu-icon">🗺️</span>
        <span>Xaritali statistika</span>
      </div>
      <div class="menu-item" onclick="switchMainView('stats')">
        <span class="menu-icon">📋</span>
        <span>Asosiy ro'yxat</span>
      </div>
      <div class="menu-item" onclick="switchMainView('stats')">
        <span class="menu-icon">🛡️</span>
        <span>Mehnat inspeksiyasi</span>
        <span class="menu-arrow">⌄</span>
      </div>
      <div class="menu-item" onclick="switchMainView('stats')">
        <span class="menu-icon">📈</span>
        <span>Hisobotlar</span>
        <span class="menu-arrow">⌄</span>
      </div>
      <div class="menu-item" onclick="switchMainView('stats')">
        <span class="menu-icon">💼</span>
        <span>Investitsiya loyihalari</span>
      </div>
      <div class="menu-item" onclick="openAdminModal()">
        <span class="menu-icon">👥</span>
        <span>Foydalanuvchilar</span>
      </div>
      <div class="menu-item" onclick="window.open('https://t.me', '_blank')">
        <span class="menu-icon">✈️</span>
        <span>Telegram guruh</span>
      </div>
    </nav>
  </aside>

  <!-- MAIN WRAPPER -->
  <div class="app-main">
    
    <!-- TOP NAVBAR -->
    <header class="app-topbar">
      <div class="topbar-left">
        <div class="topbar-menu-toggle" onclick="toggleSidebar()" title="Menyuni yopish/ochish">☰</div>
        <div class="region-badge">
          <span class="region-dot"></span>
          <span>Namangan viloyati</span>
        </div>
      </div>

      <div class="topbar-right">
        <span style="font-size:11.5px; color:var(--muted); font-weight:700;">Hududiy kuzatuvchi</span>
        <select class="topbar-select">
          <option>2026-yil</option>
          <option>2025-yil</option>
        </select>
        <select class="topbar-select">
          <option>Yanvar</option>
          <option>Fevral</option>
          <option>Mart</option>
          <option>Aprel</option>
          <option>May</option>
          <option>Iyun</option>
          <option>Iyul</option>
          <option>Avgust</option>
          <option selected>Sentyabr</option>
          <option>Oktyabr</option>
        </select>
        <button class="topbar-update-btn">Yangilash</button>

        <!-- Weather Widget -->
        <div class="top-weather">
          <span id="weatherIcon">☀️</span>
          <span id="weatherTemp">+19° — +22°</span>
        </div>

        <!-- Admin Button -->
        <button class="top-admin-btn" onclick="openAdminModal()" title="Admin boshqaruv paneli">
          <span>⚙️</span>
          <span>Admin</span>
        </button>

        <!-- Theme Toggle -->
        <button class="top-theme-btn" id="themeBtn" title="Tun/Kun">
          <span id="themeIcon">🌙</span>
        </button>

        <!-- User Profile -->
        <div class="user-pill">
          <div class="user-avatar">👤</div>
          <span>ZAFAR IKRAMOV</span>
        </div>
      </div>
    </header>

    <!-- CONTENT BODY -->
    <main class="app-content">

      <!-- VIEW 1: ASOSIY STATISTIKA (Birinchi rasmingizdagi boshqaruv paneli) -->
      <section id="viewStats" class="view-container active">
        <h2 class="dash-header-title">2026 YILDA AHOLINI DAROMADLI MEHNAT BILAN TA'MINLASH</h2>

        <!-- 4 KPI CARDS -->
        <div class="kpi-row">
          <!-- KPI 1 -->
          <div class="kpi-card">
            <div class="kpi-title-row">
              <span class="kpi-icon">📊</span>
              <span>Jami ko'rsatkich</span>
            </div>
            <div class="kpi-numbers">
              <div class="kpi-col">
                <span class="kpi-lbl">Reja</span>
                <span class="kpi-val">330 058</span>
              </div>
              <div class="kpi-col" style="text-align:right;">
                <span class="kpi-lbl">Amalda</span>
                <span class="kpi-val primary">353 622</span>
              </div>
            </div>
            <div class="kpi-progress">
              <div class="kpi-progress-bar" style="width: 100%;"></div>
            </div>
            <div class="kpi-footer">
              <span>Ayollar: 166 327 (47%)</span>
              <span>Yoshlar: 113 880 (32.2%)</span>
            </div>
          </div>

          <!-- KPI 2 -->
          <div class="kpi-card">
            <div class="kpi-title-row">
              <span class="kpi-icon">💼</span>
              <span>Doimiy ish bilan band qilish</span>
            </div>
            <div class="kpi-numbers">
              <div class="kpi-col">
                <span class="kpi-lbl">Reja</span>
                <span class="kpi-val">53 513</span>
              </div>
              <div class="kpi-col" style="text-align:right;">
                <span class="kpi-lbl">Amalda</span>
                <span class="kpi-val primary">47 019</span>
              </div>
            </div>
            <div class="kpi-progress">
              <div class="kpi-progress-bar" style="width: 87.9%; background:#0284c7;"></div>
            </div>
            <div class="kpi-footer">
              <span>Ayollar: 19 401 (41.3%)</span>
              <span>Yoshlar: 16 999 (36.2%)</span>
            </div>
          </div>

          <!-- KPI 3 -->
          <div class="kpi-card">
            <div class="kpi-title-row">
              <span class="kpi-icon">📑</span>
              <span>Legallashtirish</span>
            </div>
            <div class="kpi-numbers">
              <div class="kpi-col">
                <span class="kpi-lbl">Reja</span>
                <span class="kpi-val">41 222</span>
              </div>
              <div class="kpi-col" style="text-align:right;">
                <span class="kpi-lbl">Amalda</span>
                <span class="kpi-val primary">42 405</span>
              </div>
            </div>
            <div class="kpi-progress">
              <div class="kpi-progress-bar" style="width: 100%; background:#10b981;"></div>
            </div>
            <div class="kpi-footer">
              <span>Ayollar: 18 663 (44%)</span>
              <span>Yoshlar: 13 695 (32.3%)</span>
            </div>
          </div>

          <!-- KPI 4 -->
          <div class="kpi-card">
            <div class="kpi-title-row">
              <span class="kpi-icon">📈</span>
              <span>Daromadni oshirish</span>
            </div>
            <div class="kpi-numbers">
              <div class="kpi-col">
                <span class="kpi-lbl">Reja</span>
                <span class="kpi-val">235 323</span>
              </div>
              <div class="kpi-col" style="text-align:right;">
                <span class="kpi-lbl">Amalda</span>
                <span class="kpi-val primary">264 198</span>
              </div>
            </div>
            <div class="kpi-progress">
              <div class="kpi-progress-bar" style="width: 100%; background:#f59e0b;"></div>
            </div>
            <div class="kpi-footer">
              <span>Ayollar: 128 263 (48.5%)</span>
              <span>Yoshlar: 83 186 (31.5%)</span>
            </div>
          </div>
        </div>

        <!-- CHARTS ROW: Jins va Yosh kesimida -->
        <div class="charts-row">
          <!-- Gender chart -->
          <div class="chart-card">
            <div class="chart-title">Jins kesimida</div>
            <div class="donut-layout">
              <div class="donut-circle" style="background: conic-gradient(#0284c7 0% 53%, #ec4899 53% 100%);">
                <div class="donut-inner">353k</div>
              </div>
              <div class="legend-list">
                <div class="legend-item">
                  <div class="legend-dot-name">
                    <span class="legend-dot" style="background:#0284c7;"></span>
                    <span>Erkaklar:</span>
                  </div>
                  <strong>187 295 (53%)</strong>
                </div>
                <div class="legend-item">
                  <div class="legend-dot-name">
                    <span class="legend-dot" style="background:#ec4899;"></span>
                    <span>Ayollar:</span>
                  </div>
                  <strong>166 327 (47%)</strong>
                </div>
              </div>
            </div>
          </div>

          <!-- Age chart -->
          <div class="chart-card">
            <div class="chart-title">Yosh kesimida</div>
            <div class="donut-layout">
              <div class="donut-circle" style="background: conic-gradient(#ef4444 0% 0.1%, #10b981 0.1% 32.2%, #f59e0b 32.2% 86.2%, #0284c7 86.2% 100%);">
                <div class="donut-inner">100%</div>
              </div>
              <div class="legend-list">
                <div class="legend-item">
                  <div class="legend-dot-name">
                    <span class="legend-dot" style="background:#ef4444;"></span>
                    <span>18 yoshgacha:</span>
                  </div>
                  <strong>4 (0%)</strong>
                </div>
                <div class="legend-item">
                  <div class="legend-dot-name">
                    <span class="legend-dot" style="background:#10b981;"></span>
                    <span>18-30 yosh:</span>
                  </div>
                  <strong>113 879 (32.2%)</strong>
                </div>
                <div class="legend-item">
                  <div class="legend-dot-name">
                    <span class="legend-dot" style="background:#f59e0b;"></span>
                    <span>31-50 yosh:</span>
                  </div>
                  <strong>190 821 (54%)</strong>
                </div>
                <div class="legend-item">
                  <div class="legend-dot-name">
                    <span class="legend-dot" style="background:#0284c7;"></span>
                    <span>51 yoshdan katta:</span>
                  </div>
                  <strong>48 918 (13.8%)</strong>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- SECTORS ROW: Doimiy ish bilan band qilish sohalari -->
        <div class="sectors-card">
          <div class="chart-title">Sohalar kesimida doimiy bandlik</div>
          <div class="sectors-grid">
            <div class="sector-item">
              <span class="sector-name">Investitsiya loyihalari</span>
              <div class="sector-numbers">
                <span class="sec-plan">Reja: 4 305</span>
                <span class="sec-fact">3 065</span>
              </div>
            </div>
            <div class="sector-item">
              <span class="sector-name">Moliya sohasi</span>
              <div class="sector-numbers">
                <span class="sec-plan">Reja: 12 767</span>
                <span class="sec-fact">11 806</span>
              </div>
            </div>
            <div class="sector-item">
              <span class="sector-name">Qishloq xo'jaligi</span>
              <div class="sector-numbers">
                <span class="sec-plan">Reja: 2 096</span>
                <span class="sec-fact">1 389</span>
              </div>
            </div>
            <div class="sector-item">
              <span class="sector-name">Qurilish sohasi</span>
              <div class="sector-numbers">
                <span class="sec-plan">Reja: 2 407</span>
                <span class="sec-fact">1 682</span>
              </div>
            </div>
            <div class="sector-item">
              <span class="sector-name">Bo'sh ish o'rinlari</span>
              <div class="sector-numbers">
                <span class="sec-plan">Reja: 8 022</span>
                <span class="sec-fact">6 542</span>
              </div>
            </div>
            <div class="sector-item">
              <span class="sector-name">Tijorat banklari</span>
              <div class="sector-numbers">
                <span class="sec-plan">Reja: 23 916</span>
                <span class="sec-fact">22 535</span>
              </div>
            </div>
          </div>
        </div>

      </section>

      <!-- VIEW 2: XARITALI STATISTIKA (Biz yaratgan to'liq interaktiv geoportal) -->
      <section id="viewMap" class="view-container">
        
        <div class="geo-header">
          <div>
            <span class="geo-tag">Namangan viloyati ijara yerlar geoportali</span>
            <h2 class="geo-title">NAMANGAN VILOYATI TUMANLARI INTERAKTIV XARITASI</h2>
          </div>
          <div style="font-size:12px; font-weight:800; background:rgba(255,255,255,0.15); padding:6px 14px; border-radius:99px;">
            12 ta tuman va shahar
          </div>
        </div>

        <!-- Main Map Grid -->
        <div class="grid">
          <!-- Left: Map -->
          <div class="card">
            <div class="card-header">
              <div class="card-title">🗺️ Namangan viloyati xaritasi</div>
              <span class="badge">12 ta tuman va shahar</span>
            </div>

            <div class="map-wrap">
              <svg class="main-map" viewBox="0 0 687 501" xmlns="http://www.w3.org/2000/svg">
                <g id="polygonsGroup">
__SVG_POLYGONS__
                </g>
                <g id="labelsGroup">
__SVG_LABELS__
                </g>
              </svg>
            </div>

            <div class="btn-box">
              <div class="btn-label">Tuman yoki shaharni tanlang (ichki MFY va yerlarni ko'rish uchun bosing):</div>
              <div class="btn-grid" id="btnGrid">
__BUTTONS_HTML__
              </div>
            </div>
          </div>

          <!-- Right: Info card -->
          <div class="card">
            <div class="detail-header">
              <div class="detail-name-row">
                <div id="colorDot" class="color-dot" style="background:#357963;"></div>
                <h2 id="distName" class="district-name">Pop tumani</h2>
              </div>
              <span id="distBadge" class="badge">#1 hudud</span>
            </div>

            <div class="metrics-grid">
              <div class="metric"><span class="metric-k">🌾 Bo'sh yer maydoni</span><span id="mBosh" class="metric-v green">—</span></div>
              <div class="metric"><span class="metric-k">🧪 Tuproq qatlami</span><span id="mTuproq" class="metric-v">—</span></div>
              <div class="metric"><span class="metric-k">🥦 Mos ekinlar</span><span id="mEkin" class="metric-v">—</span></div>
              <div class="metric"><span class="metric-k">💰 Kutilayotgan daromad</span><span id="mDaromad" class="metric-v gold">—</span></div>
              <div class="metric"><span class="metric-k">💧 Tuproq namligi</span><span id="mNamlik" class="metric-v">—</span></div>
              <div class="metric"><span class="metric-k">⚖️ Kutilayotgan hosil</span><span id="mHosil" class="metric-v">—</span></div>
            </div>

            <button class="open-drill-btn" id="openModalBtn">
              🔍 <span id="openBtnLabel">Tuman ichki xaritasi va MFY ma'lumotlarini ochish</span> ➔
            </button>

            <div class="mfy-section">
              <div class="mfy-header">
                <span class="mfy-title">🏘️ MFYlar ro'yxati (bosib ichiga kiring)</span>
                <span id="mfyBadge" class="badge">0 ta MFY</span>
              </div>
              <div id="mfyPreview" class="mfy-list"></div>
            </div>

            <div class="note">
              <strong>ℹ️ Ma'muriy-hududiy eslatma:</strong> Xaritada <strong>Davlatobod</strong> va <strong>Yangi Namangan</strong> tumanlari chegaralari alohida ajratilmagan — ular Namangan shahri va Namangan tumani tarkibida ko'rsatilgan. Geoportalda MFYlari alohida belgilangan.
            </div>
          </div>
        </div>

      </section>

    </main>
  </div>

__MODAL_PART__

__JS_PART__

<script>
  /* ---- VIEW SWITCHER (SIDEBAR NAVIGATION) ---- */
  function switchMainView(viewName) {
    document.getElementById('viewStats').classList.toggle('active', viewName === 'stats');
    document.getElementById('viewMap').classList.toggle('active', viewName === 'map');

    document.getElementById('menuStats').classList.toggle('active', viewName === 'stats');
    document.getElementById('menuMap').classList.toggle('active', viewName === 'map');

    if (viewName === 'map') {
      renderInfo(selectedDistrict || 'pop');
    }
  }

  function toggleSidebar() {
    const sb = document.getElementById('appSidebar');
    if (sb.style.display === 'none') {
      sb.style.display = 'flex';
    } else {
      sb.style.display = 'none';
    }
  }
</script>

</body>
</html>
"""

final_html = template.replace('__SVG_POLYGONS__', '\n'.join(svg_polygons))
final_html = final_html.replace('__SVG_LABELS__', '\n'.join(svg_labels))
final_html = final_html.replace('__BUTTONS_HTML__', '\n'.join(buttons_html))
final_html = final_html.replace('__MODAL_PART__', modal_part_clean)
final_html = final_html.replace('__JS_PART__', js_part_clean)

with open('namangan_interaktiv_xarita.html', 'w', encoding='utf-8') as f:
    f.write(final_html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(final_html)

with open('public/namangan_interaktiv_xarita.html', 'w', encoding='utf-8') as f:
    f.write(final_html)

print("Generated clean HTML successfully! Size:", len(final_html))
