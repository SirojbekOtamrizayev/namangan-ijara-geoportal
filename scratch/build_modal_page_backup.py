import json

with open('scratch/districts_compiled.json', 'r', encoding='utf-8') as f:
    districts = json.load(f)

with open('scratch/districts_polygons.json', 'r', encoding='utf-8') as f:
    polygons_list = json.load(f)

# District centers in real WGS84 Lat/Lon
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

# Build SVG markup for main regional map
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

html = f"""<!DOCTYPE html>
<html lang="uz" class="light">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Namangan Viloyati Ijara Yerlar Geoportali</title>
  <!-- SheetJS (xlsx) kutubxonasi Excel fayllarni o'qish uchun -->
  <script src="https://cdn.jsdelivr.net/npm/xlsx@0.18.5/dist/xlsx.full.min.js"></script>
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800;900&display=swap');

    /* --- KUNDUZGI REJIM (YORUG', TINIQ, TOZA GOVTECH) --- */
    :root {{
      --bg: #f0f4f9; 
      --bg-gradient: radial-gradient(circle at 50% 0%, rgba(2, 132, 199, 0.1) 0%, transparent 70%);
      --card: #ffffff; 
      --border: #dbe4ee;
      --text: #0f172a; 
      --text-sub: #334155;
      --muted: #64748b; 
      --primary: #10b981;
      --primary-glow: rgba(16, 185, 129, 0.2);
      --map-bg: #1e293b; 
      --badge-bg: #ecfdf5; 
      --badge-text: #047857;
      --inner: #f8fafc; 
      --hover: #eef4fb;
      --header-gradient: linear-gradient(135deg, #0284c7 0%, #0369a1 50%, #0f172a 100%);
      --header-text: #ffffff;
      --card-shadow: 0 10px 25px -5px rgba(15, 23, 42, 0.08), 0 4px 10px -2px rgba(15, 23, 42, 0.04);
      --weather-bg: rgba(255, 255, 255, 0.15);
      --weather-border: rgba(255, 255, 255, 0.25);
      --weather-text: #ffffff;
    }}

    /* --- TUNGI REJIM (YUMSHOQ, MO'TADIL KO'K-KULRANG, ZULMAT EMAS) --- */
    html.dark {{
      --bg: #0f172a; 
      --bg-gradient: radial-gradient(circle at 50% 0%, rgba(56, 189, 248, 0.12) 0%, transparent 65%);
      --card: #1e293b; 
      --border: #334155;
      --text: #f8fafc; 
      --text-sub: #e2e8f0;
      --muted: #94a3b8; 
      --primary: #34d399;
      --primary-glow: rgba(52, 211, 153, 0.25);
      --map-bg: #090e1a; 
      --badge-bg: rgba(6, 78, 59, 0.5); 
      --badge-text: #6ee7b7;
      --inner: #253349; 
      --hover: #2e3e57;
      --header-gradient: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);
      --header-text: #ffffff;
      --card-shadow: 0 14px 35px -8px rgba(0, 0, 0, 0.55);
      --weather-bg: rgba(30, 41, 59, 0.8);
      --weather-border: rgba(255, 255, 255, 0.15);
      --weather-text: #ffffff;
    }}
    * {{ 
      box-sizing: border-box; 
      margin: 0; 
      padding: 0; 
      font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      -webkit-font-smoothing: antialiased;
      -moz-osx-font-smoothing: grayscale;
    }}
    body {{ 
      background: var(--bg); 
      background-image: var(--bg-gradient);
      color: var(--text); 
      min-height: 100vh; 
      padding: 20px; 
      transition: background .3s, color .3s; 
    }}
    .container {{ max-width: 1380px; margin: 0 auto; display: flex; flex-direction: column; gap: 18px; }}

    /* Weather widget - GovTech style compact */
    .weather-widget {{
      display: flex;
      align-items: center;
      gap: 8px;
      background: var(--weather-bg);
      border: 1px solid var(--weather-border);
      border-radius: 12px;
      padding: 4px 10px;
      backdrop-filter: blur(8px);
      box-shadow: 0 2px 8px rgba(0, 0, 0, 0.12);
      flex-shrink: 0;
    }}
    .weather-sun {{
      font-size: 18px;
      display: flex;
      align-items: center;
      animation: pulseSun 3s ease-in-out infinite alternate;
    }}
    @keyframes pulseSun {{
      0% {{ transform: scale(1); filter: drop-shadow(0 0 3px #fbbf24); }}
      100% {{ transform: scale(1.08); filter: drop-shadow(0 0 6px #f59e0b); }}
    }}
    .weather-info {{
      display: flex;
      flex-direction: column;
      gap: 1px;
    }}
    .weather-tags {{
      display: flex;
      align-items: center;
      gap: 4px;
    }}
    .weather-city-pill {{
      background: rgba(255, 255, 255, 0.15);
      border: 1px solid rgba(255, 255, 255, 0.25);
      border-radius: 99px;
      padding: 0 6px;
      font-size: 10px;
      font-weight: 700;
      color: #ffffff;
      letter-spacing: 0.02em;
    }}
    .weather-air-pill {{
      background: rgba(56, 189, 248, 0.2);
      border: 1px solid rgba(56, 189, 248, 0.4);
      border-radius: 99px;
      padding: 0 6px;
      font-size: 10px;
      font-weight: 700;
      color: #38bdf8;
      display: flex;
      align-items: center;
      gap: 3px;
    }}
    .weather-temp {{
      font-size: 15px;
      font-weight: 900;
      color: #ffffff;
      letter-spacing: -0.02em;
      line-height: 1.1;
    }}
    header {{ 
      background: var(--header-gradient); 
      border: 1px solid var(--border); 
      border-radius: 22px; 
      padding: 18px 28px;
      display: flex; 
      flex-wrap: wrap; 
      align-items: center; 
      justify-content: space-between; 
      gap: 14px;
      box-shadow: var(--card-shadow);
      position: relative;
      overflow: hidden;
    }}
    header::after {{
      content: '';
      position: absolute;
      top: 0; left: 0; right: 0;
      height: 1px;
      background: linear-gradient(90deg, transparent, rgba(56, 189, 248, 0.5), transparent);
    }}
    .header-left {{
      display: flex;
      align-items: center;
      gap: 16px;
    }}
    .header-logo-box {{
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      text-align: center;
      background: rgba(255, 255, 255, 0.08);
      border: 1px solid rgba(255, 255, 255, 0.16);
      border-radius: 14px;
      padding: 6px 12px;
      gap: 3px;
      backdrop-filter: blur(8px);
      box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
      flex-shrink: 0;
    }}
    .header-gerb-img {{
      width: 44px;
      height: 44px;
      object-fit: contain;
      filter: drop-shadow(0 2px 6px rgba(0, 0, 0, 0.3));
    }}
    .header-org-title {{
      font-size: 10px;
      font-weight: 800;
      color: #ffffff;
      text-transform: uppercase;
      letter-spacing: 0.03em;
      line-height: 1.2;
      max-width: 170px;
    }}
    .header-titles {{
      display: flex;
      flex-direction: column;
    }}
    .portal-tag {{ 
      font-size: 11px; 
      font-weight: 800; 
      color: #38bdf8; 
      text-transform: uppercase; 
      letter-spacing: .12em; 
      display: flex;
      align-items: center;
      gap: 6px;
    }}
    .main-title {{ 
      font-size: 22px; 
      font-weight: 900; 
      color: #ffffff; 
      letter-spacing: -.025em; 
      text-shadow: 0 2px 4px rgba(0,0,0,0.3);
    }}
    .accent-bar {{ 
      width: 100%; 
      height: 3px; 
      background: linear-gradient(90deg, #10b981 0%, #06b6d4 50%, #3b82f6 100%); 
      border-radius: 99px; 
      margin-top: 6px; 
    }}
    
    .header-actions {{
      display: flex;
      align-items: center;
      gap: 8px;
      flex-wrap: nowrap;
      margin-left: auto;
      align-self: flex-start;
    }}

    .admin-btn {{
      background: linear-gradient(135deg, #0284c7 0%, #0369a1 100%);
      color: #ffffff;
      border: 1px solid rgba(255, 255, 255, 0.2);
      padding: 6px 14px;
      border-radius: 12px;
      font-size: 12px;
      font-weight: 800;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 6px;
      box-shadow: 0 2px 8px rgba(2, 132, 199, 0.35);
      transition: all 0.2s ease;
      white-space: nowrap;
    }}
    .admin-btn:hover {{
      transform: translateY(-1px);
      box-shadow: 0 4px 12px rgba(2, 132, 199, 0.5);
      border-color: rgba(255, 255, 255, 0.4);
    }}

    .theme-btn {{ 
      background: rgba(255, 255, 255, 0.08); 
      border: 1px solid rgba(255, 255, 255, 0.2); 
      color: #ffffff; 
      width: 34px;
      height: 34px;
      padding: 0;
      border-radius: 10px; 
      cursor: pointer; 
      font-size: 16px; 
      display: flex; 
      align-items: center; 
      justify-content: center;
      transition: all .2s; 
      flex-shrink: 0;
    }}
    .theme-btn:hover {{ 
      background: rgba(255, 255, 255, 0.18); 
      border-color: #38bdf8; 
      transform: scale(1.05);
    }}

    /* MAIN GRID */
    .grid {{ display: grid; grid-template-columns: 1fr; gap: 18px; align-items: start; }}
    @media(min-width:992px) {{ .grid {{ grid-template-columns: 7fr 5fr; }} }}

    /* CARDS */
    .card {{ 
      background: var(--card); 
      border: 1px solid var(--border); 
      border-radius: 24px; 
      padding: 22px;
      box-shadow: var(--card-shadow); 
      display: flex; 
      flex-direction: column; 
      gap: 16px; 
      position: relative;
    }}
    .card-header {{ display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 8px; }}
    .card-title {{ font-size: 16px; font-weight: 800; color: var(--text); display: flex; align-items: center; gap: 8px; }}
    .badge {{ 
      font-size: 11.5px; 
      font-weight: 800; 
      background: var(--badge-bg); 
      color: var(--badge-text);
      padding: 4px 12px; 
      border-radius: 99px; 
      border: 1px solid rgba(16, 185, 129, 0.3); 
    }}

    /* MAP */
    .map-wrap {{ 
      background: var(--map-bg); 
      border: 1px solid var(--border);
      border-radius: 20px; 
      padding: 14px; 
      overflow: hidden;
      box-shadow: inset 0 2px 14px rgba(0,0,0,.3); 
    }}
    svg.main-map {{ width: 100%; height: auto; display: block; filter: drop-shadow(0 4px 12px rgba(0,0,0,0.3)); }}
    .district-poly {{ 
      cursor: pointer; 
      stroke: rgba(255, 255, 255, 0.9); 
      stroke-width: 1.4; 
      stroke-linejoin: round;
      transition: filter .25s ease, stroke-width .2s ease; 
    }}
    .district-poly:hover {{ 
      filter: brightness(1.22) drop-shadow(0 0 10px rgba(56, 189, 248, 0.8)); 
      stroke: #ffffff;
      stroke-width: 2.8; 
    }}
    .district-poly.active {{ 
      filter: brightness(1.28) drop-shadow(0 0 16px #f59e0b); 
      stroke: #f59e0b; 
      stroke-width: 3.5; 
    }}
    .district-label {{ 
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
    }}

    /* QUICK BUTTONS */
    .btn-box {{ display: flex; flex-direction: column; gap: 10px; }}
    .btn-label {{ font-size: 12px; font-weight: 800; color: var(--muted); text-transform: uppercase; letter-spacing: .06em; }}
    .btn-grid {{ display: flex; flex-wrap: wrap; gap: 7px; }}
    .d-btn {{ 
      background: var(--inner); 
      border: 1px solid var(--border); 
      border-radius: 11px; 
      padding: 7px 12px;
      font-size: 12px; 
      font-weight: 700; 
      color: var(--text); 
      cursor: pointer;
      display: inline-flex; 
      align-items: center; 
      gap: 7px; 
      transition: all .2s; 
    }}
    .d-btn:hover {{ 
      border-color: #38bdf8; 
      background: var(--hover); 
      transform: translateY(-1px); 
    }}
    .d-btn.active {{ 
      background: #0284c7; 
      color: #ffffff; 
      border-color: #38bdf8; 
      box-shadow: 0 2px 8px rgba(2, 132, 199, 0.4); 
    }}
    .d-btn.shahar-highlight {{ 
      border-color: rgba(56, 189, 248, 0.4); 
      background: rgba(56, 189, 248, 0.12); 
    }}
    .d-btn-dot {{ width: 8px; height: 8px; border-radius: 50%; flex-shrink: 0; box-shadow: 0 0 4px rgba(0,0,0,0.4); }}

    /* RIGHT PANEL */
    .detail-header {{ display: flex; align-items: center; justify-content: space-between; border-bottom: 1px solid var(--border); padding-bottom: 14px; gap: 8px; }}
    .detail-name-row {{ display: flex; align-items: center; gap: 12px; }}
    .color-dot {{ width: 16px; height: 16px; border-radius: 5px; box-shadow: 0 0 8px rgba(0,0,0,.2); }}
    .district-name {{ font-size: 20px; font-weight: 900; color: var(--text); }}
    .metrics-grid {{ display: grid; grid-template-columns: repeat(2,1fr); gap: 11px; }}
    @media(max-width:600px) {{ .metrics-grid {{ grid-template-columns: 1fr; }} }}
    .metric {{ 
      background: var(--inner); 
      border: 1px solid var(--border); 
      border-radius: 15px; 
      padding: 12px 14px;
      display: flex; 
      flex-direction: column; 
      gap: 5px; 
    }}
    .metric-k {{ font-size: 11px; font-weight: 700; color: var(--muted); }}
    .metric-v {{ font-size: 14px; font-weight: 800; color: var(--text); line-height: 1.35; }}
    .green {{ color: #059669; }} .gold {{ color: #d97706; }}
    html.dark .green {{ color: #34d399; }} html.dark .gold {{ color: #fbbf24; }}

    /* OPEN DRILL BTN */
    .open-drill-btn {{ 
      background: linear-gradient(135deg, #10b981 0%, #059669 100%); 
      color: #fff; 
      border: 1px solid rgba(255, 255, 255, 0.15);
      padding: 14px 20px; 
      border-radius: 15px; 
      font-size: 14px; 
      font-weight: 800; 
      cursor: pointer;
      display: flex; 
      align-items: center; 
      justify-content: center; 
      gap: 10px;
      box-shadow: 0 6px 16px rgba(16, 185, 129, 0.4); 
      transition: all .25s ease; 
    }}
    .open-drill-btn:hover {{ 
      transform: translateY(-2px); 
      box-shadow: 0 8px 22px rgba(16, 185, 129, 0.55); 
      border-color: rgba(255, 255, 255, 0.3);
    }}

    /* MFY PREVIEW */
    .mfy-section {{ border-top: 1px solid var(--border); padding-top: 14px; display: flex; flex-direction: column; gap: 10px; }}
    .mfy-header {{ display: flex; align-items: center; justify-content: space-between; }}
    .mfy-title {{ font-size: 13px; font-weight: 800; color: var(--text); display: flex; align-items: center; gap: 6px; }}
    .mfy-list {{ display: flex; flex-direction: column; gap: 7px; max-height: 200px; overflow-y: auto; padding-right: 4px; }}
    .mfy-item {{ 
      background: var(--inner); 
      border: 1px solid var(--border); 
      border-radius: 12px; 
      padding: 9px 12px;
      display: flex; 
      align-items: center; 
      justify-content: space-between; 
      gap: 8px;
      font-size: 12px; 
      cursor: pointer; 
      transition: all .15s; 
    }}
    .mfy-item:hover {{ 
      background: var(--hover); 
      border-color: rgba(56, 189, 248, 0.4); 
      transform: translateX(2px);
    }}
    .mfy-name {{ font-weight: 800; color: var(--text); }}
    .mfy-spec {{ font-size: 11px; color: var(--muted); }}
    .mfy-area-tag {{ 
      font-weight: 800; 
      color: #059669; 
      font-size: 11.5px;
      background: var(--badge-bg); 
      padding: 3px 8px; 
      border-radius: 7px; 
      white-space: nowrap; 
      border: 1px solid rgba(16, 185, 129, 0.25);
    }}
    html.dark .mfy-area-tag {{ color: #34d399; }}

    /* NOTE */
    .note {{ 
      background: rgba(245, 158, 11, 0.08); 
      border: 1px solid rgba(245, 158, 11, 0.25); 
      border-radius: 15px;
      padding: 13px 16px; 
      font-size: 12px; 
      color: #fbbf24; 
      line-height: 1.5; 
    }}
    html.dark .note {{ color: #fde68a; background: rgba(245,158,11,.12); border-color: rgba(245,158,11,.4); }}

    /* ===================================== */
    /*   DRILL-DOWN MODAL WINDOW (VIEWER)    */
    /* ===================================== */
    .modal-overlay {{
      display: none;
      position: fixed; inset: 0; z-index: 1000;
      background: rgba(0,0,0,.65);
      backdrop-filter: blur(4px);
      padding: 20px;
      align-items: center;
      justify-content: center;
    }}
    .modal-overlay.open {{
      display: flex;
    }}
    .modal-box {{
      background: var(--card);
      border: 1px solid var(--border);
      border-radius: 24px;
      width: 100%;
      max-width: 1320px;
      max-height: 92vh;
      display: grid;
      grid-template-columns: 310px 1fr 340px;
      grid-template-rows: auto 1fr;
      overflow: hidden;
      box-shadow: 0 25px 50px rgba(0,0,0,.5);
    }}
    @media(max-width:1100px) {{
      .modal-box {{ grid-template-columns: 260px 1fr 300px; }}
    }}
    @media(max-width:860px) {{
      .modal-box {{ grid-template-columns: 1fr; grid-template-rows: auto auto auto auto; max-height: 95vh; overflow-y: auto; }}
    }}

    /* Modal Header */
    .modal-header {{
      grid-column: 1 / -1;
      background: var(--card);
      border-bottom: 1px solid var(--border);
      padding: 14px 20px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 12px;
      flex-wrap: wrap;
    }}
    .modal-title-row {{
      display: flex;
      align-items: center;
      gap: 10px;
    }}
    .modal-color-dot {{
      width: 16px; height: 16px; border-radius: 5px;
    }}
    .modal-district-name {{
      font-size: 18px; font-weight: 900; color: var(--text);
    }}
    .modal-close-btn {{
      background: #ef4444; color: #fff; border: none;
      width: 36px; height: 36px; border-radius: 10px;
      font-size: 18px; font-weight: 900; cursor: pointer;
      display: flex; align-items: center; justify-content: center;
      transition: background .15s;
    }}
    .modal-close-btn:hover {{ background: #dc2626; }}

    /* Modal Left: MFY Sidebar */
    .modal-mfy-panel {{
      border-right: 1px solid var(--border);
      display: flex;
      flex-direction: column;
      gap: 10px;
      padding: 16px;
      overflow: hidden;
    }}
    .modal-panel-title {{
      font-size: 13px; font-weight: 800; color: var(--text);
      display: flex; align-items: center; gap: 6px;
      border-bottom: 1px solid var(--border);
      padding-bottom: 8px;
    }}
    .modal-search {{
      width: 100%; background: var(--inner); border: 1px solid var(--border);
      border-radius: 10px; padding: 8px 12px; font-size: 12px; color: var(--text); outline: none;
    }}
    .modal-search:focus {{ border-color: var(--primary); }}
    .modal-mfy-scroll {{
      display: flex; flex-direction: column; gap: 7px;
      overflow-y: auto; flex: 1; padding-right: 4px;
    }}
    .modal-mfy-item {{
      background: var(--inner); border: 1px solid var(--border);
      border-radius: 12px; padding: 10px 12px; cursor: pointer;
      display: flex; flex-direction: column; gap: 4px;
      transition: all .15s;
    }}
    .modal-mfy-item:hover {{ border-color: var(--primary); background: var(--hover); transform: translateX(2px); }}
    .modal-mfy-item.active {{ background: rgba(16,185,129,.1); border-color: var(--primary); box-shadow: 0 0 0 1px var(--primary); }}
    .mmfy-name {{ font-size: 12.5px; font-weight: 800; color: var(--text); }}
    .mmfy-spec {{ font-size: 11px; color: var(--muted); }}
    .mmfy-meta {{ display: flex; align-items: center; gap: 6px; font-size: 10.5px; margin-top: 2px; }}
    .mmfy-tag {{ background: var(--badge-bg); color: var(--badge-text); padding: 1px 6px; border-radius: 4px; font-weight: 700; }}

    /* Modal Center: Google Maps Container */
    .modal-map-panel {{
      display: flex;
      flex-direction: column;
      gap: 10px;
      padding: 16px;
      overflow: hidden;
    }}
    .zoom-map-frame {{
      background: #000;
      border-radius: 16px;
      flex: 1; min-height: 380px; position: relative;
      box-shadow: inset 0 2px 10px rgba(0,0,0,.4);
      display: flex; align-items: center; justify-content: center;
      overflow: hidden;
      border: 1px solid var(--border);
    }}

    /* Embed Google Maps Iframe */
    .gmaps-iframe {{
      width: 100%;
      height: 100%;
      min-height: 380px;
      border: none;
      display: block;
    }}

    /* Floating Satellite Indicator on Google Maps */
    .gmaps-floating-badge {{
      position: absolute;
      top: 12px;
      left: 12px;
      background: rgba(15, 23, 42, 0.85);
      backdrop-filter: blur(4px);
      color: #38bdf8;
      border: 1px solid rgba(56, 189, 248, 0.4);
      padding: 6px 12px;
      border-radius: 99px;
      font-size: 11.5px;
      font-weight: 800;
      z-index: 10;
      display: flex;
      align-items: center;
      gap: 6px;
      box-shadow: 0 4px 10px rgba(0,0,0,0.3);
      pointer-events: none;
    }}

    /* Map stats bar */
    .map-stats {{
      display: grid; grid-template-columns: repeat(3,1fr); gap: 8px;
    }}
    .map-stat {{ background: var(--inner); border: 1px solid var(--border);
      border-radius: 10px; padding: 7px 10px; display: flex; flex-direction: column; gap: 2px; }}
    .ms-k {{ font-size: 10px; color: var(--muted); }}
    .ms-v {{ font-size: 11.5px; font-weight: 800; color: var(--text); }}

    /* Modal Right: Parcel Details */
    .modal-parcel-panel {{
      border-left: 1px solid var(--border);
      display: flex;
      flex-direction: column;
      gap: 10px;
      padding: 16px;
      overflow: hidden;
    }}
    .parcel-panel-header {{
      border-bottom: 1px solid var(--border); padding-bottom: 8px;
    }}
    .parcel-panel-title {{ font-size: 14px; font-weight: 800; color: var(--text); }}
    .parcel-panel-sub {{ font-size: 11px; color: var(--muted); margin-top: 2px; }}
    .parcel-scroll {{
      display: flex; flex-direction: column; gap: 10px;
      overflow-y: auto; flex: 1; padding-right: 4px;
    }}
    .parcel-card {{
      background: var(--inner); border: 1px solid var(--border);
      border-radius: 14px; padding: 12px; display: flex; flex-direction: column; gap: 8px;
    }}
    .parcel-top {{
      display: flex; align-items: center; justify-content: space-between;
      border-bottom: 1px dashed var(--border); padding-bottom: 6px;
    }}
    .kontur-badge {{ background: #0284c7; color: #fff; font-size: 11px; font-weight: 800; padding: 2px 8px; border-radius: 6px; }}
    .area-green {{ color: #059669; font-weight: 800; font-size: 13px; }}
    .farmer-name {{ font-size: 13px; font-weight: 800; color: var(--text); }}
    .farmer-sub {{ font-size: 11px; color: var(--muted); }}
    .parcel-props {{ display: grid; grid-template-columns: repeat(2,1fr); gap: 6px; }}
    .prop-box {{ background: var(--card); border: 1px solid var(--border); border-radius: 8px; padding: 6px 8px; display: flex; flex-direction: column; gap: 1px; }}
    .pk {{ font-size: 10px; color: var(--muted); }}
    .pv {{ font-size: 11.5px; font-weight: 700; color: var(--text); }}
    .pv.gold {{ color: #d97706; }}
    .pv.green {{ color: #059669; }}

    /* Satellite Google Maps button */
    .gmaps-link-btn {{
      display: inline-flex; align-items: center; justify-content: center; gap: 6px;
      background: #1e293b; color: #38bdf8; border: 1px solid #38bdf8;
      border-radius: 8px; padding: 6px 10px; font-size: 11px; font-weight: 700;
      text-decoration: none; cursor: pointer; transition: all 0.2s; margin-top: 2px;
    }}
    .gmaps-link-btn:hover {{
      background: #38bdf8; color: #0f172a;
    }}

    .no-select-msg {{
      display: flex; flex-direction: column; align-items: center; justify-content: center;
      flex: 1; gap: 10px; color: var(--muted); font-size: 13px; text-align: center; padding: 20px;
    }}
    .no-select-msg span {{ font-size: 36px; }}

    /* ===================================== */
    /*   ADMIN LOGIN & PASSWORD MODAL        */
    /* ===================================== */
    .admin-login-box {{
      background: var(--card);
      border: 1px solid var(--border);
      border-radius: 20px;
      width: 100%;
      max-width: 420px;
      padding: 24px;
      display: flex;
      flex-direction: column;
      gap: 16px;
      box-shadow: 0 25px 50px rgba(0,0,0,.6);
    }}
    .login-header {{
      display: flex;
      align-items: center;
      justify-content: space-between;
    }}
    .login-title {{
      font-size: 17px;
      font-weight: 900;
      color: var(--text);
      display: flex;
      align-items: center;
      gap: 8px;
    }}
    .login-error {{
      color: #ef4444;
      font-size: 12px;
      font-weight: 700;
      display: none;
    }}
    .admin-change-pass-box {{
      background: var(--inner);
      border: 1px solid var(--border);
      border-radius: 14px;
      padding: 16px;
      display: flex;
      flex-direction: column;
      gap: 12px;
      max-width: 500px;
    }}
    .admin-modal-overlay {{
      display: none;
      position: fixed; inset: 0; z-index: 2000;
      background: rgba(0,0,0,.75);
      backdrop-filter: blur(5px);
      padding: 20px;
      align-items: center;
      justify-content: center;
    }}
    .admin-modal-overlay.open {{
      display: flex;
    }}
    .admin-modal-box {{
      background: var(--card);
      border: 1px solid var(--border);
      border-radius: 24px;
      width: 100%;
      max-width: 1100px;
      max-height: 92vh;
      display: flex;
      flex-direction: column;
      overflow: hidden;
      box-shadow: 0 30px 60px rgba(0,0,0,.6);
    }}
    .admin-modal-header {{
      background: var(--card);
      border-bottom: 1px solid var(--border);
      padding: 18px 24px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 12px;
    }}
    .admin-header-title {{
      display: flex;
      align-items: center;
      gap: 10px;
    }}
    .admin-title-text {{
      font-size: 18px;
      font-weight: 900;
      color: var(--text);
    }}
    .admin-badge {{
      background: #0284c7;
      color: #fff;
      font-size: 11px;
      font-weight: 800;
      padding: 3px 9px;
      border-radius: 99px;
    }}
    .admin-content-tabs {{
      display: flex;
      background: var(--inner);
      border-bottom: 1px solid var(--border);
      padding: 0 24px;
      gap: 8px;
    }}
    .admin-tab {{
      padding: 12px 18px;
      font-size: 13px;
      font-weight: 800;
      color: var(--muted);
      cursor: pointer;
      border-bottom: 3px solid transparent;
      transition: all 0.2s;
    }}
    .admin-tab:hover {{
      color: var(--text);
    }}
    .admin-tab.active {{
      color: var(--primary);
      border-bottom-color: var(--primary);
    }}
    .admin-body {{
      padding: 20px 24px;
      overflow-y: auto;
      flex: 1;
      display: flex;
      flex-direction: column;
      gap: 16px;
    }}
    .admin-form-grid {{
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 14px;
    }}
    @media(max-width: 700px) {{
      .admin-form-grid {{ grid-template-columns: 1fr; }}
    }}
    .form-group {{
      display: flex;
      flex-direction: column;
      gap: 5px;
    }}
    .form-label {{
      font-size: 12px;
      font-weight: 700;
      color: var(--text);
    }}
    .form-input, .form-select {{
      background: var(--inner);
      border: 1px solid var(--border);
      border-radius: 10px;
      padding: 9px 12px;
      font-size: 12.5px;
      color: var(--text);
      outline: none;
      transition: border-color 0.2s;
    }}
    .form-input:focus, .form-select:focus {{
      border-color: var(--primary);
    }}
    .admin-submit-btn {{
      background: linear-gradient(135deg, #10b981 0%, #059669 100%);
      color: #fff;
      border: none;
      padding: 12px 20px;
      border-radius: 12px;
      font-size: 13.5px;
      font-weight: 800;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
      box-shadow: 0 4px 12px rgba(16, 185, 129, 0.35);
      transition: all 0.2s;
    }}
    .admin-submit-btn:hover {{
      transform: translateY(-2px);
    }}
    .data-table-container {{
      border: 1px solid var(--border);
      border-radius: 14px;
      overflow-x: auto;
      max-height: 400px;
    }}
    .admin-table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 12px;
      text-align: left;
    }}
    .admin-table th {{
      background: var(--inner);
      padding: 10px 14px;
      font-weight: 800;
      color: var(--muted);
      border-bottom: 1px solid var(--border);
      white-space: nowrap;
    }}
    .admin-table td {{
      padding: 10px 14px;
      border-bottom: 1px solid var(--border);
      color: var(--text);
    }}
    .admin-table tr:hover {{
      background: var(--hover);
    }}
  </style>
</head>
<body>

<div class="container">
  <!-- Header -->
  <header>
    <div class="header-left">
      <div class="header-logo-box">
        <img src="gerb.svg" alt="O'zbekiston Davlat Gerbi" class="header-gerb-img" onerror="this.onerror=null; this.src='https://upload.wikimedia.org/wikipedia/commons/7/77/Emblem_of_Uzbekistan.svg';">
        <span class="header-org-title">Namangan viloyati Kambag'allikni qisqartirish va bandlik boshqarmasi</span>
      </div>
      <div class="header-titles">
        <span class="portal-tag">Namangan viloyati ijara yerlar geoportali</span>
        <h1 class="main-title">NAMANGAN VILOYATI TUMANLARI INTERAKTIV XARITASI</h1>
        <div class="accent-bar"></div>
      </div>
    </div>
    
    <div class="header-actions">
      <!-- Live Weather Widget (Namangan viloyati) -->
      <div class="weather-widget">
        <div class="weather-sun" id="weatherIcon">☀️</div>
        <div class="weather-info">
          <div class="weather-tags">
            <span class="weather-city-pill" id="weatherCity">Namangan sh.</span>
            <span class="weather-air-pill" id="weatherAir">💨 PM 2.5 — A'lo</span>
          </div>
          <div class="weather-temp" id="weatherTemp">+23° — +25°</div>
        </div>
      </div>

      <!-- Admin Panel Button -->
      <button id="adminBtn" class="admin-btn" onclick="openAdminModal()" title="Admin boshqaruv paneli">
        <span>⚙️</span>
        <span>Admin</span>
      </button>

      <!-- Theme Switcher (Faqat ikonka) -->
      <button id="themeBtn" class="theme-btn" title="Rejimni almashtirish">
        <span id="themeIcon">🌙</span>
      </button>
    </div>
  </header>

  <!-- Main Grid -->
  <main class="grid">

    <!-- Left: Map -->
    <section class="card">
      <div class="card-header">
        <div class="card-title">🗺️ Namangan viloyati xaritasi</div>
        <span class="badge">12 ta tuman va shahar</span>
      </div>

      <div class="map-wrap">
        <svg class="main-map" viewBox="0 0 687 501" xmlns="http://www.w3.org/2000/svg">
          <g id="polygonsGroup">
{chr(10).join(svg_polygons)}
          </g>
          <g id="labelsGroup">
{chr(10).join(svg_labels)}
          </g>
        </svg>
      </div>

      <div class="btn-box">
        <div class="btn-label">Tuman yoki shaharni tanlang (ichki MFY va yerlarni ko'rish uchun bosing):</div>
        <div class="btn-grid" id="btnGrid">
{chr(10).join(buttons_html)}
        </div>
      </div>
    </section>

    <!-- Right: Info card -->
    <section class="card">
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
    </section>
  </main>
</div>

<!-- ===================================== -->
<!--   DRILL-DOWN MODAL WINDOW (VIEWER)    -->
<!-- ===================================== -->
<div id="modalOverlay" class="modal-overlay" onclick="handleOverlayClick(event)">
  <div class="modal-box" onclick="event.stopPropagation()">

    <!-- Modal Header -->
    <div class="modal-header">
      <div class="modal-title-row">
        <div id="modalColorDot" class="modal-color-dot" style="background:#357963;"></div>
        <span id="modalDistrictName" class="modal-district-name">Pop tumani</span>
        <span id="modalDistrictBadge" class="badge">#1 hudud</span>
      </div>
      <button class="modal-close-btn" onclick="closeModal()" title="Yopish (ESC)">✕</button>
    </div>

    <!-- Left: MFY Sidebar -->
    <aside class="modal-mfy-panel">
      <div class="modal-panel-title">🏘️ MFYlar ro'yxati</div>
      <input type="text" id="mfySearch" class="modal-search" placeholder="MFY qidirish..." oninput="filterModal(this.value)">
      <div id="modalMfyScroll" class="modal-mfy-scroll"></div>
    </aside>

    <!-- Center: Interactive Google Maps Iframe -->
    <section class="modal-map-panel">
      <div class="card-header">
        <div class="card-title">🗺️ <span id="modalMapTitle">Google Maps — Sun'iy yo'ldosh xaritasi</span></div>
        <span id="modalActiveMfy" class="badge">MFY tanlanmagan</span>
      </div>

      <div class="zoom-map-frame">
        <!-- Floating status badge -->
        <div class="gmaps-floating-badge" id="gmapsBadge">
          <span>🛰️</span>
          <span id="gmapsBadgeText">Google Maps Satellite</span>
        </div>

        <!-- Google Maps Satellite View Embed -->
        <iframe 
          id="gmapsIframe" 
          class="gmaps-iframe" 
          loading="lazy" 
          allowfullscreen 
          referrerpolicy="no-referrer-when-downgrade">
        </iframe>
      </div>

      <div class="map-stats">
        <div class="map-stat"><span class="ms-k">Tuproq boniteti</span><span id="statBonitet" class="ms-v">—</span></div>
        <div class="map-stat"><span class="ms-k">Tuproq namligi</span><span id="statMoisture" class="ms-v">—</span></div>
        <div class="map-stat"><span class="ms-k">Asosiy ekin</span><span id="statCrop" class="ms-v">—</span></div>
      </div>
    </section>

    <!-- Right: Parcel Details -->
    <aside class="modal-parcel-panel">
      <div class="parcel-panel-header">
        <div id="parcelTitle" class="parcel-panel-title">Ijara yer maydonlari</div>
        <div id="parcelSub" class="parcel-panel-sub">MFY tanlang — konturlar ko'rinadi</div>
      </div>
      <div id="parcelScroll" class="parcel-scroll">
        <div class="no-select-msg">
          <span>🏘️</span>
          <div>Chap tomondagi MFY ro'yxatidan biron MFYni bosing — o'sha MFY kesimidagi ijara yerlar shu yerda ko'rinadi.</div>
        </div>
      </div>
    </aside>

  </div>
</div>

<!-- ===================================== -->
<!--   ADMIN LOGIN MODAL (XAVFSIZLIK)      -->
<!-- ===================================== -->
<div id="adminLoginOverlay" class="admin-modal-overlay" onclick="handleAdminLoginOverlayClick(event)">
  <div class="admin-login-box" onclick="event.stopPropagation()">
    <div class="login-header">
      <div class="login-title">
        <span>🔒</span>
        <span>Admin Tizimiga Kirish</span>
      </div>
      <button class="modal-close-btn" onclick="closeAdminLoginModal()" title="Yopish (ESC)">✕</button>
    </div>

    <div style="font-size:12px; color:var(--muted);">
      Geoportal ma'lumotlar bazasiga kirish uchun login va parolni kiriting.
    </div>

    <form onsubmit="handleAdminLogin(event)" style="display:flex; flex-direction:column; gap:12px;">
      <div class="form-group">
        <label class="form-label">Login:</label>
        <input type="text" id="adminLoginUser" class="form-input" placeholder="admin" required autocomplete="username">
      </div>

      <div class="form-group">
        <label class="form-label">Parol:</label>
        <input type="password" id="adminLoginPass" class="form-input" placeholder="Parolni kiriting..." required autocomplete="current-password">
      </div>

      <div id="loginErrorMsg" class="login-error">Login yoki parol noto'g'ri!</div>

      <button type="submit" class="admin-submit-btn" style="width:100%; margin-top:4px;">
        🔑 Tizimga Kirish
      </button>
    </form>
  </div>
</div>

<!-- ===================================== -->
<!--   ADMIN PANEL MODAL (MA'LUMOT BAZASI)  -->
<!-- ===================================== -->
<div id="adminModalOverlay" class="admin-modal-overlay" onclick="handleAdminOverlayClick(event)">
  <div class="admin-modal-box" onclick="event.stopPropagation()">

    <!-- Header -->
    <div class="admin-modal-header">
      <div class="admin-header-title">
        <span>⚙️</span>
        <span class="admin-title-text">Geoportal Ma'lumotlar Bazasi (Admin Boshqaruv)</span>
        <span class="admin-badge">Baza v2.0</span>
      </div>
      <button class="modal-close-btn" onclick="closeAdminModal()" title="Yopish (ESC)">✕</button>
    </div>

    /* Tabs */
    <div class="admin-content-tabs">
      <div class="admin-tab active" id="tabAddMfy" onclick="switchAdminTab('addMfy')">➕ Yangi MFY kiritish</div>
      <div class="admin-tab" id="tabExcelUpload" onclick="switchAdminTab('excelUpload')">📊 Excel orqali ommaviy yuklash</div>
      <div class="admin-tab" id="tabViewBase" onclick="switchAdminTab('viewBase')">📋 Barcha Ma'lumotlar Bazasi</div>
      <div class="admin-tab" id="tabCropBase" onclick="switchAdminTab('cropBase')">🌱 Ekinlar bazasi (AI)</div>
      <div class="admin-tab" id="tabSecurity" onclick="switchAdminTab('security')">🔐 Xavfsizlik & Parol</div>
    </div>

    <!-- Body Tab 1: Add Record -->
    <div class="admin-body" id="adminTabAddMfy">
      <form id="adminAddForm" onsubmit="handleAdminSubmit(event)">
        <div class="admin-form-grid">
          
          <div class="form-group">
            <label class="form-label">Tuman yoki Shaharni tanlang: *</label>
            <select id="admDistrict" class="form-select" required onchange="populateAdminMfyOptions()">
              <!-- Options populated dynamically -->
            </select>
          </div>

          <div class="form-group">
            <label class="form-label">MFY nomi: *</label>
            <input type="text" id="admMfyName" class="form-input" placeholder="Masalan: Jomasho'y MFY" required>
          </div>

          <div class="form-group">
            <label class="form-label">Ajratilgan umumiy maydon (ga):</label>
            <input type="text" id="admMfyArea" class="form-input" placeholder="Masalan: 230 ga">
          </div>

          <div class="form-group">
            <label class="form-label">Ixtisoslashuv / Asosiy yo'nalish:</label>
            <input type="text" id="admMfySpec" class="form-input" placeholder="Masalan: Sholichilik va Dukkakli mosh">
          </div>

          <div class="form-group">
            <label class="form-label">Google Maps Kenglik (Latitude): *</label>
            <input type="number" step="0.000001" id="admLat" class="form-input" placeholder="Masalan: 40.755400" required>
          </div>

          <div class="form-group">
            <label class="form-label">Google Maps Uzunlik (Longitude): *</label>
            <input type="number" step="0.000001" id="admLon" class="form-input" placeholder="Masalan: 71.500200" required>
          </div>

          <div class="form-group">
            <label class="form-label">Kontur raqami:</label>
            <input type="text" id="admContour" class="form-input" placeholder="Masalan: 105-kontur">
          </div>

          <div class="form-group">
            <label class="form-label">Kontur maydoni (ga):</label>
            <input type="number" step="0.01" id="admParcelArea" class="form-input" placeholder="Masalan: 0.60">
          </div>

          <div class="form-group">
            <label class="form-label">Ijara oluvchi dehqon / fuqaro F.I.Sh:</label>
            <input type="text" id="admFarmerName" class="form-input" placeholder="Masalan: Qambarov O'tkir Ne'matovich">
          </div>

          <div class="form-group">
            <label class="form-label">Ijtimoiy toifasi va ijara muddati:</label>
            <input type="text" id="admFamilyStatus" class="form-input" placeholder="Masalan: Temir daftar · 2024 - 2034 (10 yil)">
          </div>

          <div class="form-group">
            <label class="form-label">Tuproq boniteti (ball):</label>
            <input type="number" id="admBonitet" class="form-input" placeholder="Masalan: 66">
          </div>

          <div class="form-group">
            <label class="form-label">Kutilayotgan sof daromad (mln so'm):</label>
            <input type="number" step="0.1" id="admProfit" class="form-input" placeholder="Masalan: 40.6">
          </div>

        </div>

        <div style="margin-top: 18px; display: flex; justify-content: flex-end; gap: 10px;">
          <button type="submit" class="admin-submit-btn">
            💾 Bazaga saqlash va Xaritaga biriktirish
          </button>
        </div>
      </form>
    </div>

    <!-- Body Tab: Excel Upload -->
    <div class="admin-body" id="adminTabExcelUpload" style="display: none;">
      <div style="background:var(--inner); border:1px solid var(--border); border-radius:16px; padding:20px; display:flex; flex-direction:column; gap:14px;">
        <div style="display:flex; align-items:center; justify-content:space-between; flex-wrap:wrap; gap:10px;">
          <div>
            <h3 style="font-size:15px; font-weight:800; color:var(--text);">📊 Excel (.xlsx, .xls) fayldan ma'lumotlarni import qilish</h3>
            <p style="font-size:12px; color:var(--muted); margin-top:2px;">
              Excel jadvalini tanlang, tizim avtomatik barcha qatorlarni o'qib ma'lumotlar bazasiga va xaritaga biriktiradi.
            </p>
          </div>
          <button class="d-btn" onclick="downloadExcelTemplate()" style="background:#0284c7; color:#fff; border:none; padding:8px 14px;">
            📥 Excel Shablonini yuklab olish (.xlsx)
          </button>
        </div>

        <div style="border: 2px dashed var(--primary); border-radius: 12px; padding: 24px; text-align: center; background: rgba(16, 185, 129, 0.03);">
          <input type="file" id="excelFileInput" accept=".xlsx, .xls, .csv" style="display: none;" onchange="handleExcelFileSelect(event)">
          <div style="font-size: 32px; margin-bottom: 8px;">📑</div>
          <div style="font-size: 13.5px; font-weight: 800; color: var(--text); margin-bottom: 4px;">Excel faylingizni yuklang</div>
          <div style="font-size: 11.5px; color: var(--muted); margin-bottom: 12px;">Qo'llab-quvvatlanadi: .xlsx, .xls, .csv formatlar</div>
          <button type="button" class="admin-submit-btn" onclick="document.getElementById('excelFileInput').click()">
            📂 Faylni tanlash...
          </button>
        </div>

        <div id="excelPreviewSection" style="display:none; flex-direction:column; gap:10px;">
          <div style="display:flex; justify-content:space-between; align-items:center;">
            <span style="font-size:13px; font-weight:800; color:var(--text);" id="excelPreviewTitle">O'qilgan qatorlar: 0 ta</span>
            <button class="admin-submit-btn" onclick="confirmExcelImport()" style="background:#059669; padding:8px 16px; font-size:12.5px;">
              ✅ Barchasini Bazaga Saqlash
            </button>
          </div>

          <div class="data-table-container" style="max-height: 250px;">
            <table class="admin-table">
              <thead>
                <tr>
                  <th>#</th>
                  <th>Tuman</th>
                  <th>MFY nomi</th>
                  <th>Maydon</th>
                  <th>Ixtisoslashuv</th>
                  <th>Kenglik (Lat)</th>
                  <th>Uzunlik (Lon)</th>
                  <th>Kontur raqami</th>
                  <th>Dehqon F.I.Sh</th>
                </tr>
              </thead>
              <tbody id="excelPreviewTbody"></tbody>
            </table>
          </div>
        </div>

      </div>
    </div>

    <!-- Body Tab 2: View Database Records -->
    <div class="admin-body" id="adminTabViewBase" style="display: none;">
      <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:8px;">
        <span style="font-size:12.5px; font-weight:700; color:var(--muted);" id="adminTotalRecords">Jami kiritilgan yozuvlar</span>
        <button class="d-btn" onclick="exportDataToJson()" style="background:var(--primary); color:#fff; border:none;">
          📥 Bazani JSON fayl qilib yuklab olish
        </button>
      </div>

      <div class="data-table-container">
        <table class="admin-table">
          <thead>
            <tr>
              <th>#</th>
              <th>Tuman</th>
              <th>MFY nomi</th>
              <th>Maydoni</th>
              <th>Ixtisoslashuvi</th>
              <th>Koordinatalar (Sputnik)</th>
              <th>Kontur & Dehqon</th>
            </tr>
          </thead>
          <tbody id="adminTableBody">
            <!-- Populated dynamically -->
          </tbody>
        </table>
      </div>
    </div>

    <!-- Body Tab: Crop Database (AI) -->
    <div class="admin-body" id="adminTabCropBase" style="display: none;">
      <div style="background:var(--inner); border:1px solid var(--border); border-radius:16px; padding:20px; display:flex; flex-direction:column; gap:16px;">

        <!-- Header -->
        <div style="display:flex; align-items:center; justify-content:space-between; flex-wrap:wrap; gap:10px;">
          <div>
            <h3 style="font-size:15px; font-weight:800; color:var(--text);">🌱 Dehqon xo'jaligi ekinlari bazasi — AI taqsimlash</h3>
            <p style="font-size:12px; color:var(--muted); margin-top:3px; line-height:1.5;">
              Excel jadvaldan ekin mahsulotlari ma'lumotlarini yuklang. Tizim avtomatik har bir MFY tuproq turi, iqlimi va hududiga qarab mos ekinlarni <strong>AI algoritmi</strong> bilan taqsimlaydi.
            </p>
          </div>
          <div style="display:flex; gap:8px; flex-wrap:wrap;">
            <button class="d-btn" onclick="downloadCropTemplate()" style="background:#0284c7; color:#fff; border:none; padding:8px 14px;">
              📥 Ekin shablonini yuklab olish
            </button>
          </div>
        </div>

        <!-- Upload Zone -->
        <div style="border: 2px dashed #f59e0b; border-radius: 12px; padding: 22px; text-align: center; background: rgba(245,158,11,0.04);">
          <input type="file" id="cropExcelInput" accept=".xlsx, .xls, .csv" style="display:none;" onchange="handleCropExcelUpload(event)">
          <div style="font-size:30px; margin-bottom:6px;">🌾</div>
          <div style="font-size:13.5px; font-weight:800; color:var(--text); margin-bottom:4px;">Ekinlar jadvalini yuklang (Excel)</div>
          <div style="font-size:11.5px; color:var(--muted); margin-bottom:12px;">
            Ustunlar: Mahsulot nomi, Navi, Hosildorlik, Narx, Maydon va boshqalar
          </div>
          <button type="button" class="admin-submit-btn" style="background:linear-gradient(135deg,#f59e0b,#d97706);" onclick="document.getElementById('cropExcelInput').click()">
            📂 Excel faylni tanlash...
          </button>
        </div>

        <!-- Preview Table -->
        <div id="cropPreviewSection" style="display:none; flex-direction:column; gap:10px;">
          <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:8px;">
            <span style="font-size:13px; font-weight:800; color:var(--text);" id="cropPreviewTitle">O'qilgan ekinlar: 0 ta</span>
            <button class="admin-submit-btn" onclick="confirmCropImport()" style="background:#059669; padding:8px 16px; font-size:12.5px;">
              ✅ Bazaga Saqlash va AI Taqsimlash
            </button>
          </div>

          <div class="data-table-container" style="max-height:250px;">
            <table class="admin-table">
              <thead>
                <tr>
                  <th>#</th>
                  <th>Mahsulot nomi</th>
                  <th>Nav (sort)</th>
                  <th>1 ga hosil (tonna)</th>
                  <th>1 ga daromad</th>
                  <th>15 sotix hosil</th>
                  <th>10 sotix hosil</th>
                  <th>Yangicha usul mahsulot</th>
                  <th>Narx (UZS/kg)</th>
                </tr>
              </thead>
              <tbody id="cropPreviewTbody"></tbody>
            </table>
          </div>
        </div>

        <!-- AI Distribution Button -->
        <div id="cropAiSection" style="display:none; flex-direction:column; gap:12px;">
          <div style="background:linear-gradient(135deg,rgba(16,185,129,0.08),rgba(56,189,248,0.08)); border:1px solid rgba(16,185,129,0.3); border-radius:14px; padding:16px; display:flex; align-items:center; gap:14px;">
            <div style="font-size:32px;">🤖</div>
            <div style="flex:1;">
              <div style="font-size:14px; font-weight:800; color:var(--text);">AI Taqsimlash Natijasi</div>
              <div style="font-size:12px; color:var(--muted); margin-top:3px;" id="aiResultText">
                Tizim har bir MFY ning tuproq boniteti, namligi, iqlimi va mavjud ekin ixtisoslashuviga qarab eng mos ekinlarni avtomatik tanladi.
              </div>
            </div>
          </div>

          <!-- AI Results per District -->
          <div id="aiDistributionResults" style="display:flex; flex-direction:column; gap:10px; max-height:350px; overflow-y:auto; padding-right:4px;"></div>
        </div>

        <!-- Current Crop Database -->
        <div style="border-top:1px solid var(--border); padding-top:14px;">
          <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:10px;">
            <span style="font-size:13px; font-weight:800; color:var(--text);">📊 Saqlangan ekinlar bazasi</span>
            <span class="badge" id="cropDbCount">0 ta mahsulot</span>
          </div>
          <div class="data-table-container" style="max-height:250px;">
            <table class="admin-table">
              <thead>
                <tr>
                  <th>#</th>
                  <th>Mahsulot</th>
                  <th>Nav</th>
                  <th>1 ga hosil</th>
                  <th>1 ga daromad</th>
                  <th>Narx/kg</th>
                  <th>Taqsimlangan MFYlar</th>
                </tr>
              </thead>
              <tbody id="cropDbTbody"></tbody>
            </table>
          </div>
        </div>
      </div>
    </div>

    <!-- Body Tab 3: Security & Password Change -->
    <div class="admin-body" id="adminTabSecurity" style="display: none;">
      <div class="admin-change-pass-box">
        <h3 style="font-size:14px; font-weight:800; color:var(--text); margin-bottom:4px;">🔐 Admin Login va Parolini o'zgartirish</h3>
        <p style="font-size:12px; color:var(--muted); line-height:1.4;">
          Ushbu bo'limda yangi login va parol kiritishingiz mumkin. Kiritilgan yangi ma'lumotlar brauzerda doimiy saqlanadi.
        </p>

        <form onsubmit="handleChangeCredentials(event)" style="display:flex; flex-direction:column; gap:10px; margin-top:8px;">
          <div class="form-group">
            <label class="form-label">Yangi Login:</label>
            <input type="text" id="newAdminUser" class="form-input" placeholder="Yangi login..." required>
          </div>

          <div class="form-group">
            <label class="form-label">Eski Parol:</label>
            <input type="password" id="oldAdminPass" class="form-input" placeholder="Hozirgi parolingiz..." required>
          </div>

          <div class="form-group">
            <label class="form-label">Yangi Parol:</label>
            <input type="password" id="newAdminPass" class="form-input" placeholder="Yangi parol..." required minlength="4">
          </div>

          <div class="form-group">
            <label class="form-label">Yangi Parolni qayta kiriting:</label>
            <input type="password" id="confirmAdminPass" class="form-input" placeholder="Yangi parolni takrorlang..." required minlength="4">
          </div>

          <div id="changePassMsg" style="font-size:12px; font-weight:700; display:none;"></div>

          <button type="submit" class="admin-submit-btn" style="margin-top:6px;">
            🔒 Parolni yangilash va Saqlash
          </button>
        </form>
      </div>
    </div>

  </div>
</div>

<script>
  let DATA = {districts_json};
  let selectedDistrict = 'pop';
  let selectedMfy = null;

  // Load any previously saved user data from localStorage if exists
  try {{
    const saved = localStorage.getItem('namangan_geoportal_custom_data');
    if (saved) {{
      const customData = JSON.parse(saved);
      DATA = Object.assign(DATA, customData);
    }}
  }} catch(e) {{
    console.warn('LocalStorage load error:', e);
  }}

  /* ---- REGION MAP: Render right panel ---- */
  function renderInfo(did) {{
    selectedDistrict = did;
    const d = DATA[did];
    if (!d) return;

    document.getElementById('colorDot').style.background = d.color;
    document.getElementById('distName').textContent = d.name;
    document.getElementById('distBadge').textContent = '#' + d.number + ' hudud';
    document.getElementById('mBosh').textContent = d.boshYerHa || '—';
    document.getElementById('mTuproq').textContent = d.tuproqQatlami || '—';
    document.getElementById('mEkin').textContent = d.mosEkinlar || '—';
    document.getElementById('mDaromad').textContent = d.kutilayotganDaromad || '—';
    document.getElementById('mNamlik').textContent = d.tuproqNamligi || '—';
    document.getElementById('mHosil').textContent = d.hosilTonna || '—';
    document.getElementById('openBtnLabel').textContent = d.name + "ning ichki xaritasini va MFYlarini ko'rish ➔";

    const mfys = d.mfys || [];
    document.getElementById('mfyBadge').textContent = mfys.length + ' ta MFY';
    const list = document.getElementById('mfyPreview');
    list.innerHTML = '';
    mfys.forEach(m => {{
      const el = document.createElement('div');
      el.className = 'mfy-item';
      el.innerHTML = `<div><div class="mfy-name">${{m.name}}</div><div class="mfy-spec">${{m.spec || ''}}</div></div><div class="mfy-area-tag">${{m.area || '—'}}</div>`;
      el.onclick = () => {{ selectedMfy = m.id; openModal(did); }};
      list.appendChild(el);
    }});

    // Highlight polygon & button
    document.querySelectorAll('.district-poly').forEach(p => p.classList.toggle('active', p.dataset.id === did));
    document.querySelectorAll('.d-btn').forEach(b => b.classList.toggle('active', b.dataset.id === did));
  }}

  /* ---- MODAL OPEN / CLOSE (VIEWER) ---- */
  function openModal(did) {{
    if (did) selectedDistrict = did;
    const d = DATA[selectedDistrict];
    if (!d) return;

    document.getElementById('modalColorDot').style.background = d.color;
    document.getElementById('modalDistrictName').textContent = d.name;
    document.getElementById('modalDistrictBadge').textContent = '#' + d.number + ' hudud';

    // Stats
    const bonitetMatch = (d.tuproqQatlami || '').match(/\\d+\\s*ball/i);
    document.getElementById('statBonitet').textContent = bonitetMatch ? bonitetMatch[0] : '—';
    document.getElementById('statMoisture').textContent = d.tuproqNamligi ? d.tuproqNamligi.split(' ')[0] : '—';
    document.getElementById('statCrop').textContent = d.mosEkinlar ? d.mosEkinlar.split(',')[0] : '—';

    // Render MFY list sidebar
    const mfys = d.mfys || [];
    if (!selectedMfy || !mfys.some(m => m.id === selectedMfy)) {{
      selectedMfy = mfys.length > 0 ? mfys[0].id : null;
    }}

    const scroll = document.getElementById('modalMfyScroll');
    scroll.innerHTML = '';

    mfys.forEach((m) => {{
      const item = document.createElement('div');
      item.className = 'modal-mfy-item' + (m.id === selectedMfy ? ' active' : '');
      item.setAttribute('data-id', m.id);
      item.innerHTML = `
        <div style="display:flex;align-items:center;justify-content:space-between;gap:4px;">
          <span class="mmfy-name">📍 ${{m.name}}</span>
          <span class="mmfy-tag">${{m.area || '—'}}</span>
        </div>
        <span class="mmfy-spec">${{m.spec || ''}}</span>
        <div class="mmfy-meta">
          <span>📍 ${{(m.parcels || []).length}} kontur</span>
        </div>
      `;
      item.addEventListener('click', () => clickMfy(m.id));
      scroll.appendChild(item);
    }});

    // Update Google Maps iframe view with active MFY coordinates
    updateGoogleMapsView(selectedMfy);
    renderParcels(selectedMfy);

    document.getElementById('modalOverlay').classList.add('open');
    document.body.style.overflow = 'hidden';
  }}

  function updateGoogleMapsView(mfyId) {{
    const d = DATA[selectedDistrict];
    if (!d) return;
    const mfy = (d.mfys || []).find(m => m.id === mfyId) || (d.mfys || [])[0];
    const iframe = document.getElementById('gmapsIframe');
    const badgeText = document.getElementById('gmapsBadgeText');
    const titleText = document.getElementById('modalMapTitle');

    let lat = 40.998;
    let lon = 71.672;
    let zoom = 16;

    if (mfy) {{
      if (mfy.latlon && mfy.latlon.length >= 2) {{
        lat = mfy.latlon[0];
        lon = mfy.latlon[1];
      }} else if (d.latlon && d.latlon.length >= 2) {{
        lat = d.latlon[0];
        lon = d.latlon[1];
      }}
      badgeText.textContent = `🛰️ ${{mfy.name}} (Sputnik: ${{lat.toFixed(4)}}, ${{lon.toFixed(4)}})`;
      titleText.textContent = `${{mfy.name}} sun\\'iy yo\\'ldosh xaritasi`;
      document.getElementById('modalActiveMfy').textContent = mfy.name;
    }} else if (d.latlon) {{
      lat = d.latlon[0];
      lon = d.latlon[1];
      badgeText.textContent = `🛰️ ${{d.name}} markazi`;
      titleText.textContent = `${{d.name}} sun\\'iy yo\\'ldosh xaritasi`;
    }}

    // Google Maps Satellite Embed URL (t=k sets satellite view, z sets zoom level)
    const embedUrl = `https://maps.google.com/maps?q=${{lat}},${{lon}}&t=k&z=${{zoom}}&ie=UTF8&iwloc=&output=embed`;
    iframe.src = embedUrl;
  }}

  function closeModal() {{
    document.getElementById('modalOverlay').classList.remove('open');
    document.body.style.overflow = '';
  }}

  function handleOverlayClick(e) {{
    if (e.target === document.getElementById('modalOverlay')) closeModal();
  }}

  /* ---- MFY CLICK ---- */
  function clickMfy(mid) {{
    selectedMfy = mid;

    // Update sidebar highlight
    document.querySelectorAll('.modal-mfy-item').forEach(el => el.classList.toggle('active', el.dataset.id === mid));

    // Update Google Maps embedded view to this MFY location
    updateGoogleMapsView(mid);
    renderParcels(mid);
  }}

  /* ---- PARCELS RENDER ---- */
  function renderParcels(mid) {{
    const d = DATA[selectedDistrict];
    if (!d) return;
    const mfy = (d.mfys || []).find(m => m.id === mid);
    const scroller = document.getElementById('parcelScroll');

    if (!mfy) {{
      scroller.innerHTML = `<div class="no-select-msg"><span>🏘️</span><div>Chap paneldan MFY tanlang.</div></div>`;
      return;
    }}

    const ll = mfy.latlon || [41.0, 71.67];

    document.getElementById('parcelTitle').textContent = mfy.name + " — ijara yerlari";
    document.getElementById('parcelSub').innerHTML = `Maydon: ${{mfy.area || '—'}} | ${{mfy.spec || ''}}`;

    const parcels = mfy.parcels || [];
    if (parcels.length === 0) {{
      scroller.innerHTML = `<div class="no-select-msg"><span>📋</span><div>Ma'lumotlar tayyorlanmoqda.</div></div>`;
      return;
    }}

    scroller.innerHTML = '';
    parcels.forEach((p, idx) => {{
      const profit = p.economics?.netProfitUzs ? (p.economics.netProfitUzs / 1_000_000).toFixed(1) + " mln so'm" : '—';
      const bonitet = p.soil?.bonitetScore ? p.soil.bonitetScore + ' ball' : '—';
      const moisture = p.soil?.moisture || '—';
      const crop = p.recommendation?.primaryCrop || '—';
      
      const pcoord = p.coordinates || ll;
      const parcelGmapsUrl = `https://www.google.com/maps/place/${{pcoord[0]}},${{pcoord[1]}}/@${{pcoord[0]}},${{pcoord[1]}},18z/data=!3m1!1e3`;

      const el = document.createElement('div');
      el.className = 'parcel-card';
      el.innerHTML = `
        <div class="parcel-top">
          <span class="kontur-badge">${{p.contourNumber || (idx+1) + '-kontur'}}</span>
          <span class="area-green">${{p.allocatedAreaHa || '—'}} ga</span>
        </div>
        <div>
          <div class="farmer-name">${{p.farmerName || '—'}}</div>
          <div class="farmer-sub">${{p.familyStatus || '—'}} · ${{p.contractYear || '—'}}</div>
        </div>
        <div class="parcel-props">
          <div class="prop-box"><span class="pk">Tuproq boniteti</span><span class="pv green">${{bonitet}}</span></div>
          <div class="prop-box"><span class="pk">Tuproq namligi</span><span class="pv">${{moisture}}</span></div>
          <div class="prop-box"><span class="pk">Asosiy ekin</span><span class="pv">${{crop}}</span></div>
          <div class="prop-box"><span class="pk">Sof daromad</span><span class="pv gold">${{profit}}</span></div>
        </div>
        <a href="${{parcelGmapsUrl}}" target="_blank" class="gmaps-link-btn" title="Sun&apos;iy yo&apos;ldosh xaritasida ochish">
          🛰️ Google Maps to&apos;liq ekranda ↗
        </a>
      `;
      scroller.appendChild(el);
    }});

    // Show AI crop recommendations for this MFY if available
    const mfyCrops = mfy.aiCrops || [];
    if (mfyCrops.length > 0) {{
      const cropSection = document.createElement('div');
      cropSection.style.cssText = 'margin-top:8px; background:linear-gradient(135deg,rgba(245,158,11,0.06),rgba(16,185,129,0.06)); border:1px solid rgba(245,158,11,0.25); border-radius:14px; padding:12px; display:flex; flex-direction:column; gap:8px;';
      
      cropSection.innerHTML = `
        <div style="display:flex; align-items:center; gap:6px; border-bottom:1px solid var(--border); padding-bottom:6px;">
          <span style="font-size:14px;">🤖🌱</span>
          <span style="font-size:12.5px; font-weight:800; color:var(--text);">AI tavsiya: Mos ekinlar</span>
          <span class="badge" style="font-size:10px;">${{mfyCrops.length}} ta</span>
        </div>
      `;

      mfyCrops.forEach(crop => {{
        const cropEl = document.createElement('div');
        cropEl.style.cssText = 'background:var(--card); border:1px solid var(--border); border-radius:10px; padding:8px 10px; display:flex; flex-direction:column; gap:4px;';
        
        const fmtIncome = crop.haIncome ? (crop.haIncome / 1000000).toFixed(1) + " mln so'm" : '—';
        const fmtPrice = crop.price ? crop.price.toLocaleString() + " so'm/kg" : '—';

        cropEl.innerHTML = `
          <div style="display:flex; align-items:center; justify-content:space-between;">
            <span style="font-size:12px; font-weight:800; color:var(--text);">🌾 ${{crop.name}}</span>
            <span style="font-size:10px; font-weight:700; color:#f59e0b;">AI: ${{crop.aiScore}}</span>
          </div>
          <div style="display:grid; grid-template-columns:1fr 1fr; gap:4px; font-size:10.5px;">
            <div style="color:var(--muted);">Nav: <strong style="color:var(--text);">${{crop.sort || '—'}}</strong></div>
            <div style="color:var(--muted);">1 ga: <strong style="color:#059669;">${{crop.haYield || '—'}} t</strong></div>
            <div style="color:var(--muted);">Daromad: <strong style="color:#d97706;">${{fmtIncome}}</strong></div>
            <div style="color:var(--muted);">Narx: <strong style="color:var(--text);">${{fmtPrice}}</strong></div>
          </div>
          ${{crop.newCropName ? `<div style="font-size:10px; color:var(--muted);">Yangicha nav: <strong style="color:#0284c7;">${{crop.newCropName}}</strong> (${{crop.newHaYield || '—'}} t/ga)</div>` : ''}}
        `;
        cropSection.appendChild(cropEl);
      }});

      scroller.appendChild(cropSection);
    }}
  }}

  /* ---- MFY SEARCH FILTER ---- */
  function filterModal(q) {{
    const t = q.trim().toLowerCase();
    document.querySelectorAll('.modal-mfy-item').forEach(el => {{
      const txt = el.textContent.toLowerCase();
      el.style.display = txt.includes(t) ? '' : 'none';
    }});
  }}

  /* ======================================= */
  /*   ADMIN AUTH & CREDENTIAL MANAGEMENT    */
  /* ======================================= */
  let isAdminAuthenticated = false;

  function getStoredCredentials() {{
    const savedUser = localStorage.getItem('namangan_geoportal_admin_user') || 'admin';
    const savedPass = localStorage.getItem('namangan_geoportal_admin_pass') || 'admin123';
    return {{ user: savedUser, pass: savedPass }};
  }}

  function openAdminModal() {{
    if (!isAdminAuthenticated) {{
      openAdminLoginModal();
    }} else {{
      showAdminDashboard();
    }}
  }}

  function openAdminLoginModal() {{
    document.getElementById('loginErrorMsg').style.display = 'none';
    document.getElementById('adminLoginUser').value = '';
    document.getElementById('adminLoginPass').value = '';
    document.getElementById('adminLoginOverlay').classList.add('open');
    document.body.style.overflow = 'hidden';
  }}

  function closeAdminLoginModal() {{
    document.getElementById('adminLoginOverlay').classList.remove('open');
    document.body.style.overflow = '';
  }}

  function handleAdminLoginOverlayClick(e) {{
    if (e.target === document.getElementById('adminLoginOverlay')) closeAdminLoginModal();
  }}

  function handleAdminLogin(e) {{
    e.preventDefault();
    const u = document.getElementById('adminLoginUser').value.trim();
    const p = document.getElementById('adminLoginPass').value;
    const creds = getStoredCredentials();

    if (u === creds.user && p === creds.pass) {{
      isAdminAuthenticated = true;
      closeAdminLoginModal();
      showAdminDashboard();
    }} else {{
      document.getElementById('loginErrorMsg').style.display = 'block';
    }}
  }}

  function showAdminDashboard() {{
    populateAdminDistricts();
    refreshAdminDataTable();
    document.getElementById('adminModalOverlay').classList.add('open');
    document.body.style.overflow = 'hidden';
  }}

  function handleChangeCredentials(e) {{
    e.preventDefault();
    const newUser = document.getElementById('newAdminUser').value.trim();
    const oldPass = document.getElementById('oldAdminPass').value;
    const newPass = document.getElementById('newAdminPass').value;
    const confirmPass = document.getElementById('confirmAdminPass').value;
    const msg = document.getElementById('changePassMsg');
    const creds = getStoredCredentials();

    if (oldPass !== creds.pass) {{
      msg.style.display = 'block';
      msg.style.color = '#ef4444';
      msg.textContent = '❌ Amaldagi eski parol noto\\'g\\'ri kiritildi!';
      return;
    }}

    if (newPass !== confirmPass) {{
      msg.style.display = 'block';
      msg.style.color = '#ef4444';
      msg.textContent = '❌ Yangi parol va tasdiqlovchi parol mos kelmadi!';
      return;
    }}

    localStorage.setItem('namangan_geoportal_admin_user', newUser);
    localStorage.setItem('namangan_geoportal_admin_pass', newPass);

    msg.style.display = 'block';
    msg.style.color = '#10b981';
    msg.textContent = '✅ Login va parol muvaffaqiyatli o\\'zgartirildi!';
    document.getElementById('oldAdminPass').value = '';
    document.getElementById('newAdminPass').value = '';
    document.getElementById('confirmAdminPass').value = '';
  }}

  /* ======================================= */
  /*   ADMIN PANEL FUNCTIONS (MA'LUMOT BAZASI) */
  /* ======================================= */
  function closeAdminModal() {{
    document.getElementById('adminModalOverlay').classList.remove('open');
    document.body.style.overflow = '';
  }}

  function handleAdminOverlayClick(e) {{
    if (e.target === document.getElementById('adminModalOverlay')) closeAdminModal();
  }}

  function switchAdminTab(tab) {{
    document.getElementById('tabAddMfy').classList.toggle('active', tab === 'addMfy');
    document.getElementById('tabExcelUpload').classList.toggle('active', tab === 'excelUpload');
    document.getElementById('tabViewBase').classList.toggle('active', tab === 'viewBase');
    document.getElementById('tabCropBase').classList.toggle('active', tab === 'cropBase');
    document.getElementById('tabSecurity').classList.toggle('active', tab === 'security');
    document.getElementById('adminTabAddMfy').style.display = tab === 'addMfy' ? 'flex' : 'none';
    document.getElementById('adminTabExcelUpload').style.display = tab === 'excelUpload' ? 'flex' : 'none';
    document.getElementById('adminTabViewBase').style.display = tab === 'viewBase' ? 'flex' : 'none';
    document.getElementById('adminTabCropBase').style.display = tab === 'cropBase' ? 'flex' : 'none';
    document.getElementById('adminTabSecurity').style.display = tab === 'security' ? 'flex' : 'none';
    if (tab === 'viewBase') refreshAdminDataTable();
    if (tab === 'cropBase') refreshCropDbTable();
    if (tab === 'security') {{
      document.getElementById('newAdminUser').value = getStoredCredentials().user;
      document.getElementById('changePassMsg').style.display = 'none';
    }}
  }}

  function populateAdminDistricts() {{
    const sel = document.getElementById('admDistrict');
    sel.innerHTML = '';
    Object.keys(DATA).forEach(did => {{
      const opt = document.createElement('option');
      opt.value = did;
      opt.textContent = DATA[did].name;
      if (did === selectedDistrict) opt.selected = true;
      sel.appendChild(opt);
    }});
  }}

  function handleAdminSubmit(e) {{
    e.preventDefault();
    const did = document.getElementById('admDistrict').value;
    const mfyName = document.getElementById('admMfyName').value.trim();
    const area = document.getElementById('admMfyArea').value.trim() || '150 ga';
    const spec = document.getElementById('admMfySpec').value.trim() || 'Sabzavotchilik';
    const lat = parseFloat(document.getElementById('admLat').value);
    const lon = parseFloat(document.getElementById('admLon').value);
    const contour = document.getElementById('admContour').value.trim() || 'Yangi-kontur';
    const parcelArea = parseFloat(document.getElementById('admParcelArea').value) || 0.5;
    const farmerName = document.getElementById('admFarmerName').value.trim() || "Dehqon xo'jaligi a'zosi";
    const familyStatus = document.getElementById('admFamilyStatus').value.trim() || 'Temir daftar · 2024 - 2034';
    const bonitet = parseInt(document.getElementById('admBonitet').value) || 70;
    const profit = parseFloat(document.getElementById('admProfit').value) || 35.0;

    if (!DATA[did]) return;

    const newMfyId = `${{did}}-${{Date.now()}}`;
    const newParcel = {{
      id: `P-${{Date.now()}}`,
      contourNumber: contour,
      allocatedAreaHa: parcelArea,
      farmerName: farmerName,
      familyStatus: familyStatus,
      contractYear: "2024 - 2034 (10 yil)",
      coordinates: [lat, lon],
      soil: {{
        bonitetScore: bonitet,
        moisture: "70% (Yaxshi)"
      }},
      recommendation: {{
        primaryCrop: spec
      }},
      economics: {{
        netProfitUzs: profit * 1000000
      }}
    }};

    const newMfy = {{
      id: newMfyId,
      name: mfyName,
      area: area,
      spec: spec,
      poorFamilies: 75,
      latlon: [lat, lon],
      parcels: [newParcel]
    }};

    if (!DATA[did].mfys) DATA[did].mfys = [];
    DATA[did].mfys.unshift(newMfy);

    // Save in LocalStorage
    try {{
      localStorage.setItem('namangan_geoportal_custom_data', JSON.stringify(DATA));
    }} catch(err) {{
      console.warn('LocalStorage save failed:', err);
    }}

    alert(`✅ "${{mfyName}}" muvaffaqiyatli saqlandi va ${{DATA[did].name}} ma'lumotlar bazasiga qo'shildi!`);
    
    // Reset Form
    document.getElementById('adminAddForm').reset();

    // Re-render
    renderInfo(did);
    refreshAdminDataTable();
    switchAdminTab('viewBase');
  }}

  /* ======================================= */
  /*   EXCEL IMPORT & TEMPLATE EXPORT        */
  /* ======================================= */
  let parsedExcelRows = [];

  function downloadExcelTemplate() {{
    const templateData = [
      {{
        "Tuman": "Mingbuloq",
        "MFY nomi": "Jomasho'y MFY",
        "Umumiy maydon": "230 ga",
        "Ixtisoslashuv": "Sholichilik va Dukkakli mosh",
        "Kenglik (Latitude)": 40.7554,
        "Uzunlik (Longitude)": 71.5002,
        "Kontur raqami": "105-kontur",
        "Kontur maydoni (ga)": 0.60,
        "Dehqon F.I.Sh": "Qambarov O'tkir Ne'matovich",
        "Ijtimoiy toifasi": "Temir daftar · 2024 - 2034",
        "Tuproq boniteti": 66,
        "Sof daromad (mln)": 40.6
      }},
      {{
        "Tuman": "Pop",
        "MFY nomi": "G'urumsaroy MFY",
        "Umumiy maydon": "185 ga",
        "Ixtisoslashuv": "Poliz va Eksportbop Mosh",
        "Kenglik (Latitude)": 40.8920,
        "Uzunlik (Longitude)": 71.0850,
        "Kontur raqami": "142-kontur",
        "Kontur maydoni (ga)": 0.50,
        "Dehqon F.I.Sh": "Rustamov Jamshid Qodirovich",
        "Ijtimoiy toifasi": "Ijtimoiy himoya reyestrida",
        "Tuproq boniteti": 64,
        "Sof daromad (mln)": 31.5
      }}
    ];

    if (typeof XLSX !== 'undefined') {{
      const ws = XLSX.utils.json_to_sheet(templateData);
      const wb = XLSX.utils.book_new();
      XLSX.utils.book_append_sheet(wb, ws, "Ijara_Yerlar");
      XLSX.writeFile(wb, "Ijara_yerlar_shablon.xlsx");
    }} else {{
      alert("XLSX kutubxonasi yuklanmoqda, iltimos qayta urinib ko'ring.");
    }}
  }}

  function handleExcelFileSelect(event) {{
    const file = event.target.files[0];
    if (!file) return;

    const reader = new FileReader();
    reader.onload = function(e) {{
      try {{
        const data = new Uint8Array(e.target.result);
        const workbook = XLSX.read(data, {{ type: 'array' }});
        const firstSheetName = workbook.SheetNames[0];
        const worksheet = workbook.Sheets[firstSheetName];
        const json = XLSX.utils.sheet_to_json(worksheet);

        if (!json || json.length === 0) {{
          alert("Excel faylida ma'lumot topilmadi!");
          return;
        }}

        parsedExcelRows = json;
        renderExcelPreview(json);
      }} catch(err) {{
        console.error("Excel o'qishda xatolik:", err);
        alert("Excel faylini o'qishda xatolik yuz berdi: " + err.message);
      }}
    }};
    reader.readAsArrayBuffer(file);
  }}

  function matchDistrictId(tumanName) {{
    if (!tumanName) return 'pop';
    const norm = tumanName.toString().toLowerCase().replace(/[^a-z0-9]/g, '');
    for (let did of Object.keys(DATA)) {{
      const dnorm = DATA[did].name.toLowerCase().replace(/[^a-z0-9]/g, '');
      const snorm = DATA[did].shortName.toLowerCase().replace(/[^a-z0-9]/g, '');
      if (dnorm.includes(norm) || norm.includes(snorm) || did.replace(/[^a-z0-9]/g, '').includes(norm)) {{
        return did;
      }}
    }}
    return 'pop';
  }}

  function renderExcelPreview(rows) {{
    const previewSection = document.getElementById('excelPreviewSection');
    const tbody = document.getElementById('excelPreviewTbody');
    const title = document.getElementById('excelPreviewTitle');
    
    tbody.innerHTML = '';
    title.textContent = `O'qilgan qatorlar: ${{rows.length}} ta`;

    rows.forEach((r, idx) => {{
      const tuman = r['Tuman'] || r['tuman'] || r['Hudud'] || 'Pop';
      const mfy = r['MFY nomi'] || r['MFY'] || r['mfy'] || 'MFY';
      const area = r['Umumiy maydon'] || r['Maydon'] || '150 ga';
      const spec = r['Ixtisoslashuv'] || r['Mos ekin'] || 'Sabzavotchilik';
      const lat = r['Kenglik (Latitude)'] || r['Latitude'] || r['Lat'] || 40.9;
      const lon = r['Uzunlik (Longitude)'] || r['Longitude'] || r['Lon'] || 71.6;
      const contour = r['Kontur raqami'] || r['Kontur'] || (idx + 1) + '-kontur';
      const farmer = r['Dehqon F.I.Sh'] || r['Dehqon'] || 'Ijarachi';

      const tr = document.createElement('tr');
      tr.innerHTML = `
        <td>${{idx + 1}}</td>
        <td><strong>${{tuman}}</strong></td>
        <td>${{mfy}}</td>
        <td>${{area}}</td>
        <td>${{spec}}</td>
        <td><code>${{lat}}</code></td>
        <td><code>${{lon}}</code></td>
        <td>${{contour}}</td>
        <td>${{farmer}}</td>
      `;
      tbody.appendChild(tr);
    }});

    previewSection.style.display = 'flex';
  }}

  function confirmExcelImport() {{
    if (!parsedExcelRows || parsedExcelRows.length === 0) {{
      alert("Yuklash uchun ma'lumot yo'q!");
      return;
    }}

    let importedCount = 0;

    parsedExcelRows.forEach((r, idx) => {{
      const tuman = r['Tuman'] || r['tuman'] || r['Hudud'] || 'Pop';
      const did = matchDistrictId(tuman);
      const mfyName = r['MFY nomi'] || r['MFY'] || r['mfy'] || 'Yangi MFY';
      const area = (r['Umumiy maydon'] || r['Maydon'] || '150 ga').toString();
      const spec = (r['Ixtisoslashuv'] || r['Mos ekin'] || 'Sabzavotchilik').toString();
      const lat = parseFloat(r['Kenglik (Latitude)'] || r['Latitude'] || r['Lat'] || (DATA[did]?.latlon?.[0] || 40.9));
      const lon = parseFloat(r['Uzunlik (Longitude)'] || r['Longitude'] || r['Lon'] || (DATA[did]?.latlon?.[1] || 71.6));
      const contour = (r['Kontur raqami'] || r['Kontur'] || (idx + 1) + '-kontur').toString();
      const parcelArea = parseFloat(r['Kontur maydoni (ga)'] || r['Kontur maydoni'] || 0.5);
      const farmer = (r['Dehqon F.I.Sh'] || r['Dehqon'] || "Dehqon xo'jaligi").toString();
      const status = (r['Ijtimoiy toifasi'] || r['Toifa'] || 'Ijtimoiy reyestr').toString();
      const bonitet = parseInt(r['Tuproq boniteti'] || 70);
      const profit = parseFloat(r['Sof daromad (mln)'] || 35.0);

      if (!DATA[did]) return;

      const newParcel = {{
        id: `P-${{Date.now()}}-${{idx}}`,
        contourNumber: contour,
        allocatedAreaHa: parcelArea,
        farmerName: farmer,
        familyStatus: status,
        contractYear: "2024 - 2034 (10 yil)",
        coordinates: [lat, lon],
        soil: {{
          bonitetScore: bonitet,
          moisture: "70% (Optimal)"
        }},
        recommendation: {{
          primaryCrop: spec
        }},
        economics: {{
          netProfitUzs: profit * 1000000
        }}
      }};

      const newMfy = {{
        id: `${{did}}-xl-${{Date.now()}}-${{idx}}`,
        name: mfyName,
        area: area.includes('ga') ? area : (area + ' ga'),
        spec: spec,
        poorFamilies: 80,
        latlon: [lat, lon],
        parcels: [newParcel]
      }};

      if (!DATA[did].mfys) DATA[did].mfys = [];
      DATA[did].mfys.unshift(newMfy);
      importedCount++;
    }});

    // Save in LocalStorage
    try {{
      localStorage.setItem('namangan_geoportal_custom_data', JSON.stringify(DATA));
    }} catch(err) {{
      console.warn('LocalStorage save failed:', err);
    }}

    alert(`🎉 Tabriklaymiz! Excel fayldan jami ${{importedCount}} ta qator ma'lumotlar bazasiga muvaffaqiyatli yuklandi va xaritaga biriktirildi!`);

    document.getElementById('excelFileInput').value = '';
    document.getElementById('excelPreviewSection').style.display = 'none';
    parsedExcelRows = [];

    renderInfo(selectedDistrict);
    refreshAdminDataTable();
    switchAdminTab('viewBase');
  }}

  function refreshAdminDataTable() {{
    const tbody = document.getElementById('adminTableBody');
    tbody.innerHTML = '';
    let counter = 0;

    Object.keys(DATA).forEach(did => {{
      const d = DATA[did];
      (d.mfys || []).forEach(m => {{
        counter++;
        const tr = document.createElement('tr');
        const coords = m.latlon ? `${{m.latlon[0].toFixed(4)}}, ${{m.latlon[1].toFixed(4)}}` : '—';
        const pCount = (m.parcels || []).length;
        const firstFarmer = pCount > 0 ? (m.parcels[0].farmerName || '—') : '—';
        
        tr.innerHTML = `
          <td><strong>${{counter}}</strong></td>
          <td>${{d.name}}</td>
          <td><strong>${{m.name}}</strong></td>
          <td><span class="badge" style="background:#ecfdf5;color:#065f46;">${{m.area || '—'}}</span></td>
          <td>${{m.spec || '—'}}</td>
          <td><code>${{coords}}</code></td>
          <td>${{pCount}} ta kontur (${{firstFarmer}})</td>
        `;
        tbody.appendChild(tr);
      }});
    }});

    document.getElementById('adminTotalRecords').textContent = `Jami bazada mavjud: ${{counter}} ta MFY va ijara uchastkalari`;
  }}

  function exportDataToJson() {{
    const blob = new Blob([JSON.stringify(DATA, null, 2)], {{ type: 'application/json' }});
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = 'namangan_ijara_yerlar_bazasi.json';
    a.click();
    URL.revokeObjectURL(url);
  }}

  /* ======================================= */
  /*   CROP DATABASE & AI DISTRIBUTION       */
  /* ======================================= */
  let cropDatabase = [];
  let parsedCropRows = [];

  // Load saved crop database
  try {{
    const savedCrops = localStorage.getItem('namangan_crop_database');
    if (savedCrops) cropDatabase = JSON.parse(savedCrops);
  }} catch(e) {{ console.warn('Crop DB load error:', e); }}

  function downloadCropTemplate() {{
    const templateData = [
      {{
        "Mahsulot nomi": "shalg'om",
        "Mahalliy nav (sort)": "Petrovskaya 1",
        "1 ga etishtiriladigan (tonna)": 20,
        "1 ga olinadigan daromad": 60000000,
        "15 sotix etishtiriladigan (tonna)": 3.0,
        "15 sotix olinadigan daromad": 9000000,
        "10 sotix etishtiriladigan (tonna)": 2.0,
        "10 sotix olinadigan daromad": 6000000,
        "Yangicha usul mahsulot nomi": "Geytsin",
        "Yangicha usul 1 ga (tonna)": 35,
        "Yangicha usul 1 ga daromad": 105000000,
        "Yangicha usul 15 sotix (tonna)": 5.3,
        "Yangicha usul 15 sotix daromad": 15750000,
        "Yangicha usul 10 sotix (tonna)": 3.5,
        "Yangicha usul 10 sotix daromad": 10500000,
        "Narx (UZS/kg)": 3000
      }},
      {{
        "Mahsulot nomi": "turp",
        "Mahalliy nav (sort)": "Dunganskiy 12/8",
        "1 ga etishtiriladigan (tonna)": 20,
        "1 ga olinadigan daromad": 60000000,
        "15 sotix etishtiriladigan (tonna)": 3.0,
        "15 sotix olinadigan daromad": 9000000,
        "10 sotix etishtiriladigan (tonna)": 2.0,
        "10 sotix olinadigan daromad": 6000000,
        "Yangicha usul mahsulot nomi": "Rinam",
        "Yangicha usul 1 ga (tonna)": 35,
        "Yangicha usul 1 ga daromad": 105000000,
        "Yangicha usul 15 sotix (tonna)": 5.3,
        "Yangicha usul 15 sotix daromad": 15750000,
        "Yangicha usul 10 sotix (tonna)": 3.5,
        "Yangicha usul 10 sotix daromad": 10500000,
        "Narx (UZS/kg)": 3000
      }},
      {{
        "Mahsulot nomi": "karam",
        "Mahalliy nav (sort)": "Pekinskaya rannyaya",
        "1 ga etishtiriladigan (tonna)": 30,
        "1 ga olinadigan daromad": 90000000,
        "15 sotix etishtiriladigan (tonna)": 4.5,
        "15 sotix olinadigan daromad": 13500000,
        "10 sotix etishtiriladigan (tonna)": 3.0,
        "10 sotix olinadigan daromad": 9000000,
        "Yangicha usul mahsulot nomi": "May Kvin F1",
        "Yangicha usul 1 ga (tonna)": 30,
        "Yangicha usul 1 ga daromad": 150000000,
        "Yangicha usul 15 sotix (tonna)": 7.5,
        "Yangicha usul 15 sotix daromad": 22500000,
        "Yangicha usul 10 sotix (tonna)": 5.0,
        "Yangicha usul 10 sotix daromad": 15000000,
        "Narx (UZS/kg)": 3000
      }}
    ];

    if (typeof XLSX !== 'undefined') {{
      const ws = XLSX.utils.json_to_sheet(templateData);
      const wb = XLSX.utils.book_new();
      XLSX.utils.book_append_sheet(wb, ws, "Ekinlar_Bazasi");
      XLSX.writeFile(wb, "Ekinlar_bazasi_shablon.xlsx");
    }} else {{
      alert("XLSX kutubxonasi yuklanmoqda, qayta urinib ko'ring.");
    }}
  }}

  function handleCropExcelUpload(event) {{
    const file = event.target.files[0];
    if (!file) return;

    const reader = new FileReader();
    reader.onload = function(e) {{
      try {{
        const data = new Uint8Array(e.target.result);
        const workbook = XLSX.read(data, {{ type: 'array' }});
        const firstSheet = workbook.Sheets[workbook.SheetNames[0]];
        
        // Read as array of arrays to handle any header language
        const aoa = XLSX.utils.sheet_to_json(firstSheet, {{ header: 1 }});
        
        if (!aoa || aoa.length < 2) {{
          alert("Excel faylida yetarli ma'lumot topilmadi!");
          return;
        }}

        // Find the header row (first row with 3+ non-empty cells)
        let headerRowIdx = -1;
        for (let i = 0; i < Math.min(5, aoa.length); i++) {{
          const row = aoa[i] || [];
          const nonEmpty = row.filter(c => c !== undefined && c !== null && c.toString().trim() !== '').length;
          if (nonEmpty >= 3) {{
            headerRowIdx = i;
            break;
          }}
        }}
        if (headerRowIdx === -1) headerRowIdx = 0;

        // Safe headers mapping
        const headers = (aoa[headerRowIdx] || []).map(h => (h !== null && h !== undefined ? h.toString().trim() : ''));
        
        // Smart column detection by keyword patterns (works for both Cyrillic and Latin)
        function findCol(patterns) {{
          for (let i = 0; i < headers.length; i++) {{
            const h = (headers[i] || '').toLowerCase();
            if (patterns.some(p => p && h.includes(p.toLowerCase()))) return i;
          }}
          return -1;
        }}
        
        // Detect columns using multilingual keywords
        const colName = findCol(['\u043c\u0430\u04b3\u0441\u0443\u043b\u043e\u0442 \u043d\u043e\u043c', '\u043c\u0430\u0445\u0441\u0443\u043b\u043e\u0442 \u043d\u043e\u043c', 'mahsulot nom', 'mahsulot', '\u043d\u043e\u043c\u0438', 'nomi', '\u043c\u0430\u04b3\u0441\u0443\u043b\u043e\u0442']);
        const colSort = findCol(['\u043d\u0430\u0432\u0438 \u043d\u043e\u043c', '\u043c\u0430\u04b3\u0430\u043b\u043b\u0438\u0439', '\u043c\u0430\u0445\u0430\u043b\u043b\u0438\u0439', 'mahalliy', 'nav', 'sort', '\u044d\u0442\u0438\u0448\u0442\u0438\u0440\u0438\u0448']);
        const colHaYield = findCol(['1 \u0433\u0435\u043a\u0442\u0430\u0440', '1 \u0433\u0430', '1 ga', '1 gektar', '\u0442\u043e\u043d\u043d\u0430']);
        const colHaIncome = findCol(['1 \u0433\u0435\u043a\u0442\u0430\u0440\u0434\u0430\u043d \u043e\u043b\u0438\u043d', '1 \u0433\u0430 \u043e\u043b\u0438\u043d', '\u0434\u0430\u0440\u043e\u043c\u0430\u0434']);
        const colNewCrop = findCol(['\u044f\u043d\u0433\u0438\u0447\u0430', 'yangicha', '\u044f\u043d\u0433\u0438']);
        const colPrice = findCol(['\u043d\u0430\u0440\u0445', 'narx', '\u0441\u045e\u043c', 'uzs', '\u0432\u0430\u0437\u043d']);

        // Parse data rows
        const dataRows = aoa.slice(headerRowIdx + 1).filter(row => {{
          if (!row || row.length < 2) return false;
          const firstCell = (row[0] || '').toString().trim();
          const secondCell = (row[1] || '').toString().trim();
          return firstCell !== '' || secondCell !== '';
        }});

        if (dataRows.length === 0) {{
          alert("Ma'lumot qatorlari topilmadi!");
          return;
        }}

        // Check if first column is row number (all numeric)
        const firstColIsNum = dataRows.every(r => !isNaN(parseFloat(r[0])));
        const offset = firstColIsNum ? 1 : 0;

        // Map data using detected columns or positional fallback
        parsedCropRows = dataRows.map((row, idx) => {{
          const getVal = (colIdx, fallbackIdx) => {{
            if (colIdx >= 0 && row[colIdx] !== undefined) return row[colIdx];
            if (fallbackIdx !== undefined && row[fallbackIdx] !== undefined) return row[fallbackIdx];
            return '';
          }};

          return {{
            '_name': getVal(colName >= 0 ? colName : offset, offset),
            '_sort': getVal(colSort >= 0 ? colSort : offset + 1, offset + 1),
            '_haYield': getVal(colHaYield >= 0 ? colHaYield : offset + 2, offset + 2),
            '_haIncome': getVal(colHaIncome >= 0 ? colHaIncome : offset + 3, offset + 3),
            '_s15Yield': getVal(-1, offset + 4),
            '_s15Income': getVal(-1, offset + 5),
            '_s10Yield': getVal(-1, offset + 6),
            '_s10Income': getVal(-1, offset + 7),
            '_newCrop': getVal(colNewCrop >= 0 ? colNewCrop : offset + 8, offset + 8),
            '_newHaYield': getVal(-1, offset + 9),
            '_newHaIncome': getVal(-1, offset + 10),
            '_newS15Yield': getVal(-1, offset + 11),
            '_newS15Income': getVal(-1, offset + 12),
            '_newS10Yield': getVal(-1, offset + 13),
            '_newS10Income': getVal(-1, offset + 14),
            '_price': getVal(colPrice >= 0 ? colPrice : offset + 15, offset + 15),
            '_rawRow': row
          }};
        }});

        renderCropPreview(parsedCropRows);
      }} catch(err) {{
        console.error("Excel ekin o'qishda xatolik:", err);
        alert("Excel faylini o'qishda xatolik: " + err.message);
      }}
    }};
    reader.readAsArrayBuffer(file);
  }}

  function renderCropPreview(rows) {{
    const tbody = document.getElementById('cropPreviewTbody');
    const title = document.getElementById('cropPreviewTitle');
    tbody.innerHTML = '';
    title.textContent = `O'qilgan ekinlar: ${{rows.length}} ta`;

    rows.forEach((r, idx) => {{
      const name = r._name || r['Mahsulot nomi'] || r['mahsulot'] || r['Nomi'] || '—';
      const sort = r._sort || r['Mahalliy nav (sort)'] || r['Nav'] || r['Mahalliy usulda mahsulot etishtirish (navi nomi)'] || '—';
      const haYield = r._haYield !== '' && r._haYield !== undefined ? r._haYield : (r['1 ga etishtiriladigan (tonna)'] || '—');
      const haIncome = r._haIncome !== '' && r._haIncome !== undefined ? r._haIncome : (r['1 ga olinadigan daromad'] || '—');
      const s15Yield = r._s15Yield !== '' && r._s15Yield !== undefined ? r._s15Yield : (r['15 sotix etishtiriladigan (tonna)'] || '—');
      const s10Yield = r._s10Yield !== '' && r._s10Yield !== undefined ? r._s10Yield : (r['10 sotix etishtiriladigan (tonna)'] || '—');
      const newCrop = r._newCrop || r['Yangicha usul mahsulot nomi'] || '—';
      const price = r._price !== '' && r._price !== undefined ? r._price : (r['Narx (UZS/kg)'] || '—');

      const numIncome = parseFloat(haIncome);
      const fmtIncome = !isNaN(numIncome) && numIncome > 1000 ? (numIncome / 1000000).toFixed(1) + ' mln' : (haIncome || '—');

      const tr = document.createElement('tr');
      tr.innerHTML = `
        <td>${{idx + 1}}</td>
        <td><strong>${{name}}</strong></td>
        <td>${{sort}}</td>
        <td>${{haYield !== '—' ? haYield + ' t' : '—'}}</td>
        <td>${{fmtIncome}}</td>
        <td>${{s15Yield !== '—' ? s15Yield + ' t' : '—'}}</td>
        <td>${{s10Yield !== '—' ? s10Yield + ' t' : '—'}}</td>
        <td>${{newCrop}}</td>
        <td>${{price}}</td>
      `;
      tbody.appendChild(tr);
    }});

    document.getElementById('cropPreviewSection').style.display = 'flex';
  }}

  function confirmCropImport() {{
    if (!parsedCropRows || parsedCropRows.length === 0) {{
      alert("Yuklash uchun ekin ma'lumoti yo'q!");
      return;
    }}

    // Parse and normalize crop data
    cropDatabase = parsedCropRows.map((r, idx) => {{
      const name = (r._name || r['Mahsulot nomi'] || r['mahsulot'] || r['Nomi'] || 'Ekin ' + (idx+1)).toString();
      const sort = (r._sort || r['Mahalliy nav (sort)'] || r['Nav'] || '').toString();
      const haYield = parseFloat(r._haYield || r['1 ga etishtiriladigan (tonna)'] || 0) || 0;
      const haIncome = parseFloat(r._haIncome || r['1 ga olinadigan daromad'] || 0) || 0;
      const s15Yield = parseFloat(r._s15Yield || r['15 sotix etishtiriladigan (tonna)'] || 0) || 0;
      const s15Income = parseFloat(r._s15Income || r['15 sotix olinadigan daromad'] || 0) || 0;
      const s10Yield = parseFloat(r._s10Yield || r['10 sotix etishtiriladigan (tonna)'] || 0) || 0;
      const s10Income = parseFloat(r._s10Income || r['10 sotix olinadigan daromad'] || 0) || 0;
      const newCropName = (r._newCrop || r['Yangicha usul mahsulot nomi'] || '').toString();
      const newHaYield = parseFloat(r._newHaYield || r['Yangicha usul 1 ga (tonna)'] || 0) || 0;
      const newHaIncome = parseFloat(r._newHaIncome || r['Yangicha usul 1 ga daromad'] || 0) || 0;
      const price = parseFloat(r._price || r['Narx (UZS/kg)'] || 0) || 0;

      return {{
        id: 'crop-' + Date.now() + '-' + idx,
        name, sort, haYield, haIncome, s15Yield, s15Income, s10Yield, s10Income,
        newCropName, newHaYield, newHaIncome, price,
        assignedMfys: []
      }};
    }});

    // Save crop database
    try {{
      localStorage.setItem('namangan_crop_database', JSON.stringify(cropDatabase));
    }} catch(e) {{ console.warn('Crop DB save error:', e); }}

    // Run AI distribution
    runAiDistribution();

    alert(`🎉 ${{cropDatabase.length}} ta ekin muvaffaqiyatli bazaga saqlandi va AI taqsimlash bajarildi!`);

    document.getElementById('cropExcelInput').value = '';
    document.getElementById('cropPreviewSection').style.display = 'none';
    parsedCropRows = [];

    refreshCropDbTable();
  }}

  /* ---- AI DISTRIBUTION ALGORITHM ---- */
  function runAiDistribution() {{
    // Smart matching: each crop is assigned to MFYs based on soil, specialization keywords, and bonitet
    const cropKeywords = {{
      "poliz": ["tarvuz", "qovun", "poliz"],
      "sabzavot": ["pomidor", "baqlajon", "karam", "sabzi", "piyoz", "sarimsoq", "qalampir", "bodring", "rediska", "salat", "turp", "shalgom", "lavlagi", "kartoshka", "ko'katlar", "shivit", "ukrop", "petruska"],
      "dukkakli": ["mosh", "loviya", "no'xat", "fasol", "yasmiq"],
      "mevali": ["uzum", "olma", "o'rik", "shaftoli", "anor", "anjir", "gilos", "behi", "nok", "bodom"],
      "donli": ["bug'doy", "arpa", "makkajo'xori", "sholi", "suli"],
      "texnik": ["paxta", "kungaboqar", "zig'ir"],
      "rezavor": ["kartoshka"],
      "ildizmeva": ["sabzi", "turp", "lavlagi", "rediska", "shalgom"],
      "boshqa": ["kunjut", "yeryong'oq", "yabulat"]
    }};

    // Classify each crop
    cropDatabase.forEach(crop => {{
      const cname = (crop.name || '').toString().toLowerCase();
      crop.categories = [];

      // Check if crop name matches any category keywords
      Object.entries(cropKeywords).forEach(([cat, keywords]) => {{
        if (keywords.some(kw => cname.includes(kw))) {{
          crop.categories.push(cat);
        }}
      }});

      // Default: sabzavot
      if (crop.categories.length === 0) crop.categories.push('sabzavot');
    }});

    // Assign crops to MFYs based on their specialization and soil quality
    const results = [];

    Object.keys(DATA).forEach(did => {{
      const d = DATA[did];
      const mfys = d.mfys || [];

      mfys.forEach(mfy => {{
        const mfySpec = (mfy.spec || '').toString().toLowerCase();
        const mfySoilBonitet = (mfy.parcels && mfy.parcels[0] && mfy.parcels[0].soil) ? (mfy.parcels[0].soil.bonitetScore || 65) : 65;
        const assignedCrops = [];

        cropDatabase.forEach(crop => {{
          let score = 0;
          const cname = (crop.name || '').toString().toLowerCase();

          // 1. Check if MFY specialization mentions this crop or related category
          if (mfySpec.includes(cname)) score += 40;
          crop.categories.forEach(cat => {{
            if (mfySpec.includes(cat)) score += 20;
          }});

          // 2. Check if MFY spec mentions related words
          const specWords = ["poliz", "sabzavot", "mosh", "uzum", "sholi", "paxta", "meva", "bodom", "kartoshka", "pomidor", "baqlajon", "karam", "eksport", "dukkakli", "loviya", "ko'chatchilik"];
          specWords.forEach(sw => {{
            if (mfySpec.includes(sw) && (cname.includes(sw) || crop.categories.some(c => c.includes(sw)))) {{
              score += 15;
            }}
          }});

          // 3. Soil bonitet matching (higher bonitet = more crops suitable)
          if (mfySoilBonitet >= 75) score += 10; // excellent soil
          else if (mfySoilBonitet >= 65) score += 5; // good soil

          // 4. Randomized variety factor (to distribute different crops)
          score += Math.floor(Math.random() * 8);

          // 5. General crop compatibility  
          if (crop.categories.includes('sabzavot')) score += 5; // vegetables go everywhere
          if (crop.categories.includes('ildizmeva') && mfySoilBonitet >= 60) score += 7;

          if (score >= 15) {{
            assignedCrops.push({{ ...crop, aiScore: score }});
          }}
        }});

        // Sort by score and take top crops
        assignedCrops.sort((a, b) => b.aiScore - a.aiScore);
        const topCrops = assignedCrops.slice(0, Math.min(8, assignedCrops.length));

        if (topCrops.length > 0) {{
          results.push({{
            district: d.name,
            districtId: did,
            mfyName: mfy.name,
            mfyId: mfy.id,
            crops: topCrops
          }});

          // Also store assigned crops reference in crop database
          topCrops.forEach(tc => {{
            const originalCrop = cropDatabase.find(c => c.id === tc.id);
            if (originalCrop && !originalCrop.assignedMfys.includes(mfy.name)) {{
              originalCrop.assignedMfys.push(mfy.name);
            }}
          }});

          // Update MFY data with crop recommendations
          mfy.aiCrops = topCrops.map(c => ({{
            name: c.name,
            sort: c.sort,
            haYield: c.haYield,
            haIncome: c.haIncome,
            newCropName: c.newCropName,
            newHaYield: c.newHaYield,
            price: c.price,
            aiScore: c.aiScore
          }}));
        }}
      }});
    }});

    // Save updated data
    try {{
      localStorage.setItem('namangan_geoportal_custom_data', JSON.stringify(DATA));
      localStorage.setItem('namangan_crop_database', JSON.stringify(cropDatabase));
    }} catch(e) {{ console.warn('Save error:', e); }}

    // Render AI results
    renderAiDistributionResults(results);
  }}

  function renderAiDistributionResults(results) {{
    const container = document.getElementById('aiDistributionResults');
    const section = document.getElementById('aiSection');
    container.innerHTML = '';

    if (results.length === 0) {{
      document.getElementById('aiSection').style.display = 'none';
      return;
    }}

    document.getElementById('aiSection').style.display = 'flex';
    document.getElementById('aiResultText').textContent = `Jami ${{results.length}} ta MFY ga ekinlar taqsimlandi. Har bir MFY uchun tuproq va iqlim sharoitiga mos ekinlar tanlandi.`;

    results.forEach(r => {{
      const card = document.createElement('div');
      card.style.cssText = 'background:var(--inner); border:1px solid var(--border); border-radius:12px; padding:12px; display:flex; flex-direction:column; gap:6px;';

      const cropTags = r.crops.map(c => `<span style="background:var(--badge-bg); color:var(--badge-text); padding:2px 8px; border-radius:6px; font-size:11px; font-weight:700; border:1px solid rgba(16,185,129,0.2);">${{c.name}} (AI: ${{c.aiScore}})</span>`).join(' ');

      card.innerHTML = `
        <div style="display:flex; align-items:center; justify-content:space-between; gap:6px;">
          <div>
            <div style="font-size:12.5px; font-weight:800; color:var(--text);">📍 ${{r.mfyName}}</div>
            <div style="font-size:11px; color:var(--muted);">${{r.district}}</div>
          </div>
          <span class="badge">${{r.crops.length}} ta ekin</span>
        </div>
        <div style="display:flex; flex-wrap:wrap; gap:4px; margin-top:2px;">
          ${{cropTags}}
        </div>
      `;
      container.appendChild(card);
    }});
  }}

  function refreshCropDbTable() {{
    const tbody = document.getElementById('cropDbTbody');
    const countEl = document.getElementById('cropDbCount');
    tbody.innerHTML = '';

    if (cropDatabase.length === 0) {{
      countEl.textContent = '0 ta mahsulot';
      tbody.innerHTML = '<tr><td colspan="7" style="text-align:center; color:var(--muted); padding:20px;">Hali ekin ma\\'lumoti yuklanmagan. Yuqoridagi Excel yuklash orqali boshlang.</td></tr>';
      return;
    }}

    countEl.textContent = cropDatabase.length + ' ta mahsulot';

    cropDatabase.forEach((c, idx) => {{
      const fmtIncome = c.haIncome ? (c.haIncome / 1000000).toFixed(1) + ' mln' : '—';
      const fmtPrice = c.price ? c.price.toLocaleString() + " so'm" : '—';
      const mfyList = c.assignedMfys && c.assignedMfys.length > 0 ? c.assignedMfys.slice(0, 3).join(', ') + (c.assignedMfys.length > 3 ? ` (+${{c.assignedMfys.length - 3}})` : '') : 'Taqsimlanmagan';

      const tr = document.createElement('tr');
      tr.innerHTML = `
        <td>${{idx + 1}}</td>
        <td><strong>${{c.name}}</strong></td>
        <td>${{c.sort || '—'}}</td>
        <td>${{c.haYield || '—'}} t</td>
        <td>${{fmtIncome}}</td>
        <td>${{fmtPrice}}</td>
        <td style="font-size:11px;">${{mfyList}}</td>
      `;
      tbody.appendChild(tr);
    }});
  }}

  document.addEventListener('keydown', e => {{
    if (e.key === 'Escape') {{
      closeModal();
      closeAdminModal();
    }}
  }});

  /* ---- EVENTS ---- */
  document.querySelectorAll('.district-poly').forEach(poly => {{
    poly.addEventListener('click', () => {{
      const id = poly.dataset.id;
      renderInfo(id);
      openModal(id);
    }});
  }});

  document.querySelectorAll('.d-btn').forEach(btn => {{
    btn.addEventListener('click', () => {{
      const id = btn.dataset.id;
      renderInfo(id);
      openModal(id);
    }});
  }});

  document.getElementById('openModalBtn').addEventListener('click', () => openModal(selectedDistrict));

  /* ---- THEME TOGGLE ---- */
  document.getElementById('themeBtn').addEventListener('click', () => {{
    const dark = document.documentElement.classList.toggle('dark');
    document.getElementById('themeIcon').textContent = dark ? '☀️' : '🌙';
  }});

  /* ---- LIVE WEATHER FETCH (OPEN-METEO API) ---- */
  async function fetchLiveWeather() {{
    try {{
      // Namangan city coordinates: lat=40.998, lon=71.672
      const res = await fetch('https://api.open-meteo.com/v1/forecast?latitude=40.998&longitude=71.672&current=temperature_2m,relative_humidity_2m,weather_code&daily=temperature_2m_max,temperature_2m_min&timezone=Asia%2FTashkent');
      if (res.ok) {{
        const data = await res.json();
        if (data.daily && data.daily.temperature_2m_min && data.daily.temperature_2m_max) {{
          const minT = Math.round(data.daily.temperature_2m_min[0]);
          const maxT = Math.round(data.daily.temperature_2m_max[0]);
          const signMin = minT > 0 ? '+' : '';
          const signMax = maxT > 0 ? '+' : '';
          document.getElementById('weatherTemp').textContent = `${{signMin}}${{minT}}° — ${{signMax}}${{maxT}}°`;
        }}
        const code = data.current ? data.current.weather_code : 0;
        let icon = '☀️';
        if (code >= 1 && code <= 3) icon = '⛅';
        else if (code >= 45 && code <= 48) icon = '🌫️';
        else if (code >= 51 && code <= 67) icon = '🌧️';
        else if (code >= 71) icon = '🌨️';
        document.getElementById('weatherIcon').textContent = icon;
      }}
    }} catch(e) {{
      console.warn('Weather fetch error:', e);
    }}
  }}
  fetchLiveWeather();

  /* ---- INIT ---- */
  renderInfo('pop');
</script>
</body>
</html>
"""

with open('namangan_interaktiv_xarita.html', 'w', encoding='utf-8') as f:
    f.write(html)

with open('public/namangan_interaktiv_xarita.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f"Build complete! File size: {len(html)} chars ({len(html)/1024:.1f} KB)")
