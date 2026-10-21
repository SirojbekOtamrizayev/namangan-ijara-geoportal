import json

with open('scratch/districts_compiled.json', 'r', encoding='utf-8') as f:
    districts = json.load(f)

with open('scratch/districts_polygons.json', 'r', encoding='utf-8') as f:
    polygons_list = json.load(f)

# Build SVG markup for main region map
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
    
    # Polygon element
    svg_polygons.append(f'''
      <polygon 
        id="poly-{pid}" 
        data-id="{pid}" 
        class="district-poly" 
        points="{pts}" 
        fill="{color}">
        <title>{name} - Tanlash uchun bosing</title>
      </polygon>
    ''')
    
    # Text label element
    svg_labels.append(f'''
      <text 
        id="label-{pid}"
        x="{tpos[0]}" 
        y="{tpos[1]}" 
        class="district-label" 
        data-id="{pid}"
        style="font-size: {fsize}px;">
        {short_name}
      </text>
    ''')
    
    # Button
    shahar_class = " shahar-highlight" if pid == 'namangan-shahri' else ""
    buttons_html.append(f'''
      <button class="d-btn{shahar_class}" data-id="{pid}" title="{name}">
        <span class="d-btn-dot" style="background-color: {color};"></span>
        <span>{short_name}</span>
      </button>
    ''')

html_content = f"""<!DOCTYPE html>
<html lang="uz" class="light">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Namangan Viloyati Tumanlari va Ijara Yerlari Interaktiv Geoportali</title>
  <style>
    :root {{
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
      --table-hover: #f1f5f9;
      --badge-bg: #ecfdf5;
      --badge-text: #065f46;
      --btn-active: #0f172a;
      --btn-active-text: #ffffff;
      --card-inner-bg: #f8fafc;
    }}

    html.dark {{
      --bg-page: #0b1120;
      --bg-card: #151e32;
      --bg-card-border: #1e293b;
      --text-main: #f8fafc;
      --text-muted: #94a3b8;
      --header-title: #f8fafc;
      --line-green: #34d399;
      --primary: #34d399;
      --primary-hover: #10b981;
      --map-bg: #090e17;
      --map-stroke: #334155;
      --table-hover: #1e293b;
      --badge-bg: #064e3b;
      --badge-text: #a7f3d0;
      --btn-active: #38bdf8;
      --btn-active-text: #0f172a;
      --card-inner-bg: #0f172a;
    }}

    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
    }}

    body {{
      background-color: var(--bg-page);
      color: var(--text-main);
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      transition: background-color 0.25s, color 0.25s;
      padding: 16px;
    }}

    .container {{
      max-width: 1400px;
      margin: 0 auto;
      width: 100%;
      display: flex;
      flex-direction: column;
      gap: 16px;
    }}

    /* Header styling */
    header {{
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
    }}

    .header-left {{
      display: flex;
      flex-direction: column;
      gap: 4px;
    }}

    .portal-tag {{
      font-size: 11px;
      font-weight: 800;
      color: var(--primary);
      text-transform: uppercase;
      letter-spacing: 0.08em;
    }}

    .main-title {{
      font-size: 21px;
      font-weight: 900;
      color: var(--header-title);
      letter-spacing: -0.02em;
    }}

    .accent-bar {{
      width: 100%;
      height: 4px;
      background: linear-gradient(90deg, #10b981 0%, #06b6d4 50%, #3b82f6 100%);
      border-radius: 99px;
      margin-top: 4px;
    }}

    .header-right {{
      display: flex;
      align-items: center;
      gap: 10px;
    }}

    .back-btn {{
      background: #0284c7;
      color: #ffffff;
      border: none;
      padding: 9px 16px;
      border-radius: 12px;
      font-size: 13px;
      font-weight: 700;
      cursor: pointer;
      display: none;
      align-items: center;
      gap: 8px;
      box-shadow: 0 2px 4px rgba(2, 132, 199, 0.3);
      transition: all 0.2s;
    }}
    .back-btn:hover {{
      background: #0369a1;
      transform: translateY(-1px);
    }}

    .theme-toggle-btn {{
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
    }}
    .theme-toggle-btn:hover {{
      border-color: var(--primary);
    }}

    /* Main Dashboard Layouts */
    .view-container {{
      display: none;
      width: 100%;
    }}

    .view-container.active {{
      display: block;
    }}

    /* REGION VIEW (MODE 1) */
    .region-grid {{
      display: grid;
      grid-template-columns: 1fr;
      gap: 16px;
      align-items: start;
    }}

    @media (min-width: 992px) {{
      .region-grid {{
        grid-template-columns: 7fr 5fr;
      }}
    }}

    .card {{
      background: var(--bg-card);
      border: 1px solid var(--bg-card-border);
      border-radius: 24px;
      padding: 20px;
      box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
      display: flex;
      flex-direction: column;
      gap: 14px;
    }}

    .card-header-row {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 8px;
    }}

    .card-title {{
      font-size: 15px;
      font-weight: 800;
      color: var(--text-main);
      display: flex;
      align-items: center;
      gap: 6px;
    }}

    .badge-count {{
      font-size: 11px;
      font-weight: 800;
      background: var(--badge-bg);
      color: var(--badge-text);
      padding: 3px 10px;
      border-radius: 99px;
      border: 1px solid var(--primary);
    }}

    /* SVG Map Styling */
    .map-svg-wrap {{
      background: var(--map-bg);
      border-radius: 18px;
      padding: 10px;
      position: relative;
      overflow: hidden;
      box-shadow: inset 0 2px 8px rgba(0,0,0,0.3);
    }}

    svg.namangan-map {{
      width: 100%;
      height: auto;
      display: block;
      transition: all 0.5s cubic-bezier(0.2, 0.8, 0.2, 1);
    }}

    .district-poly {{
      cursor: pointer;
      transition: transform 0.2s ease, filter 0.2s ease, stroke-width 0.2s ease;
      stroke: #ffffff;
      stroke-width: 1.5;
      stroke-linejoin: round;
      stroke-linecap: round;
    }}

    .district-poly:hover {{
      filter: drop-shadow(0 0 10px rgba(255, 255, 255, 0.9)) brightness(1.15);
      stroke: #ffffff;
      stroke-width: 3;
    }}

    .district-poly.active {{
      filter: drop-shadow(0 0 14px #f59e0b) brightness(1.25);
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
      stroke: rgba(0, 0, 0, 0.85);
      stroke-width: 2.8px;
      stroke-linecap: round;
      stroke-linejoin: round;
    }}

    /* Quick Selector Buttons */
    .button-selector-box {{
      display: flex;
      flex-direction: column;
      gap: 8px;
      margin-top: 4px;
    }}

    .selector-title {{
      font-size: 12px;
      font-weight: 700;
      color: var(--text-muted);
      text-transform: uppercase;
      letter-spacing: 0.04em;
    }}

    .district-buttons-grid {{
      display: flex;
      flex-wrap: wrap;
      gap: 6px;
    }}

    .d-btn {{
      background: var(--bg-page);
      border: 1px solid var(--bg-card-border);
      border-radius: 10px;
      padding: 6px 10px;
      font-size: 11.5px;
      font-weight: 700;
      color: var(--text-main);
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      transition: all 0.15s;
    }}

    .d-btn:hover {{
      border-color: var(--primary);
      transform: translateY(-1px);
    }}

    .d-btn.active {{
      background: var(--btn-active);
      color: var(--btn-active-text);
      border-color: var(--btn-active);
    }}

    .d-btn.shahar-highlight {{
      border-color: #38bdf8;
      background: rgba(56, 189, 248, 0.1);
    }}

    .d-btn-dot {{
      width: 8px;
      height: 8px;
      border-radius: 50%;
      flex-shrink: 0;
    }}

    /* Metrics Grid */
    .details-header {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      border-bottom: 1px solid var(--bg-card-border);
      padding-bottom: 12px;
      gap: 8px;
    }}

    .details-title-row {{
      display: flex;
      align-items: center;
      gap: 10px;
    }}

    .details-color-indicator {{
      width: 14px;
      height: 14px;
      border-radius: 4px;
      box-shadow: 0 0 6px rgba(0,0,0,0.2);
    }}

    .selected-district-name {{
      font-size: 19px;
      font-weight: 900;
      color: var(--text-main);
    }}

    .metrics-grid {{
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 10px;
    }}

    @media (max-width: 600px) {{
      .metrics-grid {{
        grid-template-columns: 1fr;
      }}
    }}

    .metric-item {{
      background: var(--card-inner-bg);
      border: 1px solid var(--bg-card-border);
      border-radius: 14px;
      padding: 10px 12px;
      display: flex;
      flex-direction: column;
      gap: 4px;
    }}

    .metric-label {{
      font-size: 11px;
      font-weight: 700;
      color: var(--text-muted);
      display: flex;
      align-items: center;
      gap: 4px;
    }}

    .metric-value {{
      font-size: 13.5px;
      font-weight: 800;
      color: var(--text-main);
      line-height: 1.35;
    }}

    .metric-value.highlight-green {{
      color: #059669;
    }}
    .metric-value.highlight-gold {{
      color: #d97706;
    }}

    /* Enter District Drilldown Button */
    .drilldown-action-btn {{
      background: linear-gradient(135deg, #10b981 0%, #059669 100%);
      color: white;
      border: none;
      padding: 12px 18px;
      border-radius: 14px;
      font-size: 13.5px;
      font-weight: 800;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
      box-shadow: 0 4px 10px rgba(16, 185, 129, 0.35);
      transition: all 0.2s ease;
    }}
    .drilldown-action-btn:hover {{
      transform: translateY(-2px);
      box-shadow: 0 6px 14px rgba(16, 185, 129, 0.45);
    }}

    /* MFY List in Mode 1 */
    .mfy-section {{
      border-top: 1px solid var(--bg-card-border);
      padding-top: 12px;
      display: flex;
      flex-direction: column;
      gap: 8px;
    }}

    .mfy-header-row {{
      display: flex;
      align-items: center;
      justify-content: space-between;
    }}

    .mfy-title {{
      font-size: 12.5px;
      font-weight: 800;
      color: var(--text-main);
      display: flex;
      align-items: center;
      gap: 6px;
    }}

    .mfy-list {{
      display: flex;
      flex-direction: column;
      gap: 6px;
      max-height: 200px;
      overflow-y: auto;
      padding-right: 4px;
    }}

    .mfy-item {{
      background: var(--card-inner-bg);
      border: 1px solid var(--bg-card-border);
      border-radius: 10px;
      padding: 8px 10px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 8px;
      font-size: 12px;
      cursor: pointer;
      transition: all 0.15s;
    }}

    .mfy-item:hover {{
      background: var(--table-hover);
      border-color: var(--primary);
    }}

    .mfy-name {{
      font-weight: 700;
      color: var(--text-main);
    }}

    .mfy-spec {{
      font-size: 11px;
      color: var(--text-muted);
    }}

    .mfy-area {{
      font-weight: 800;
      color: #059669;
      font-size: 11px;
      background: var(--badge-bg);
      padding: 2px 7px;
      border-radius: 6px;
      white-space: nowrap;
    }}

    /* ======================================================== */
    /* DISTRICT DRILL-DOWN VIEW (MODE 2 - User's New Request)   */
    /* ======================================================== */
    .drilldown-layout {{
      display: grid;
      grid-template-columns: 1fr;
      gap: 16px;
      align-items: start;
    }}

    @media (min-width: 992px) {{
      .drilldown-layout {{
        grid-template-columns: 320px 1fr 340px;
      }}
    }}

    @media (min-width: 1200px) {{
      .drilldown-layout {{
        grid-template-columns: 340px 1.2fr 380px;
      }}
    }}

    /* Left: MFYs panel */
    .mfy-sidebar {{
      background: var(--bg-card);
      border: 1px solid var(--bg-card-border);
      border-radius: 20px;
      padding: 16px;
      display: flex;
      flex-direction: column;
      gap: 12px;
      max-height: 640px;
      box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
    }}

    .sidebar-header {{
      display: flex;
      flex-direction: column;
      gap: 4px;
      border-bottom: 1px solid var(--bg-card-border);
      padding-bottom: 10px;
    }}

    .sidebar-title {{
      font-size: 14px;
      font-weight: 800;
      color: var(--text-main);
      display: flex;
      align-items: center;
      gap: 6px;
    }}

    .sidebar-sub {{
      font-size: 11px;
      color: var(--text-muted);
    }}

    .search-input {{
      width: 100%;
      background: var(--card-inner-bg);
      border: 1px solid var(--bg-card-border);
      border-radius: 10px;
      padding: 8px 12px;
      font-size: 12px;
      color: var(--text-main);
      outline: none;
    }}
    .search-input:focus {{
      border-color: var(--primary);
    }}

    .sidebar-mfy-scroll {{
      display: flex;
      flex-direction: column;
      gap: 8px;
      overflow-y: auto;
      padding-right: 4px;
    }}

    .mfy-nav-item {{
      background: var(--card-inner-bg);
      border: 1px solid var(--bg-card-border);
      border-radius: 12px;
      padding: 10px 12px;
      cursor: pointer;
      display: flex;
      flex-direction: column;
      gap: 4px;
      transition: all 0.15s;
    }}

    .mfy-nav-item:hover {{
      background: var(--table-hover);
      border-color: var(--primary);
      transform: translateX(2px);
    }}

    .mfy-nav-item.active {{
      background: rgba(16, 185, 129, 0.12);
      border-color: var(--primary);
      box-shadow: 0 0 0 1px var(--primary);
    }}

    .mfy-nav-top {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 4px;
    }}

    .mfy-nav-name {{
      font-size: 13px;
      font-weight: 800;
      color: var(--text-main);
    }}

    .mfy-nav-spec {{
      font-size: 11px;
      color: var(--text-muted);
    }}

    .mfy-nav-meta {{
      display: flex;
      align-items: center;
      gap: 6px;
      font-size: 10.5px;
      margin-top: 2px;
    }}

    .meta-tag {{
      background: var(--badge-bg);
      color: var(--badge-text);
      padding: 1px 6px;
      border-radius: 4px;
      font-weight: 700;
    }}

    /* Middle: Zoomed District Map View */
    .district-map-center {{
      background: var(--bg-card);
      border: 1px solid var(--bg-card-border);
      border-radius: 20px;
      padding: 16px;
      display: flex;
      flex-direction: column;
      gap: 12px;
      box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
    }}

    .zoom-map-frame {{
      background: var(--map-bg);
      border-radius: 16px;
      overflow: hidden;
      position: relative;
      min-height: 400px;
      display: flex;
      align-items: center;
      justify-content: center;
      box-shadow: inset 0 2px 10px rgba(0,0,0,0.4);
    }}

    svg.zoomed-district-svg {{
      width: 100%;
      height: 420px;
      display: block;
      transition: all 0.4s ease;
    }}

    .mfy-pin-circle {{
      cursor: pointer;
      transition: transform 0.2s, filter 0.2s;
    }}
    .mfy-pin-circle:hover {{
      transform: scale(1.3);
      filter: drop-shadow(0 0 6px #ffffff);
    }}
    .mfy-pin-circle.active {{
      transform: scale(1.4);
      filter: drop-shadow(0 0 8px #f59e0b);
      stroke: #f59e0b;
      stroke-width: 2.5;
    }}

    /* Right: Parcels & Lease Details */
    .parcel-detail-panel {{
      background: var(--bg-card);
      border: 1px solid var(--bg-card-border);
      border-radius: 20px;
      padding: 16px;
      display: flex;
      flex-direction: column;
      gap: 12px;
      box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
    }}

    .parcel-header {{
      display: flex;
      flex-direction: column;
      gap: 4px;
      border-bottom: 1px solid var(--bg-card-border);
      padding-bottom: 10px;
    }}

    .parcel-title {{
      font-size: 15px;
      font-weight: 800;
      color: var(--text-main);
    }}

    .parcel-list-container {{
      display: flex;
      flex-direction: column;
      gap: 10px;
      max-height: 520px;
      overflow-y: auto;
      padding-right: 4px;
    }}

    .parcel-card {{
      background: var(--card-inner-bg);
      border: 1px solid var(--bg-card-border);
      border-radius: 14px;
      padding: 12px 14px;
      display: flex;
      flex-direction: column;
      gap: 8px;
      box-shadow: 0 1px 3px rgba(0,0,0,0.03);
    }}

    .parcel-card-top {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      border-bottom: 1px dashed var(--bg-card-border);
      padding-bottom: 6px;
    }}

    .contour-badge {{
      background: #0284c7;
      color: #ffffff;
      font-size: 11px;
      font-weight: 800;
      padding: 2px 8px;
      border-radius: 6px;
    }}

    .farmer-name {{
      font-size: 13px;
      font-weight: 800;
      color: var(--text-main);
    }}

    .parcel-props {{
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 6px;
      font-size: 11px;
    }}

    .parcel-prop-box {{
      display: flex;
      flex-direction: column;
      gap: 1px;
      background: var(--bg-card);
      padding: 6px 8px;
      border-radius: 8px;
      border: 1px solid var(--bg-card-border);
    }}

    .prop-k {{
      color: var(--text-muted);
      font-size: 10px;
    }}

    .prop-v {{
      color: var(--text-main);
      font-weight: 700;
      font-size: 11.5px;
    }}

    .highlight-money {{
      color: #d97706;
      font-weight: 800;
    }}

    .highlight-area {{
      color: #059669;
      font-weight: 800;
    }}

    /* Official Disclaimers */
    .note-box {{
      background: rgba(245, 158, 11, 0.08);
      border: 1px solid rgba(245, 158, 11, 0.3);
      border-radius: 14px;
      padding: 12px 16px;
      font-size: 12px;
      color: #92400e;
      line-height: 1.5;
    }}
    html.dark .note-box {{
      color: #fde68a;
      background: rgba(245, 158, 11, 0.12);
      border-color: rgba(245, 158, 11, 0.4);
    }}
  </style>
</head>
<body>

  <div class="container">
    <!-- Header -->
    <header>
      <div class="header-left">
        <span class="portal-tag">Namangan viloyati ijara yerlar geoportali</span>
        <h1 class="main-title" id="pageMainTitle">NAMANGAN VILOYATI TUMANLARI INTERAKTIV XARITASI</h1>
        <div class="accent-bar"></div>
      </div>
      <div class="header-right">
        <!-- Back to Full Map button -->
        <button id="backToRegionBtn" class="back-btn" onclick="switchView('region')">
          <span>⬅</span>
          <span>Viloyat xaritasiga qaytish</span>
        </button>

        <!-- Theme Toggle -->
        <button id="themeToggle" class="theme-toggle-btn">
          <span id="themeIcon">🌙</span>
          <span id="themeLabel">Tungi rejim</span>
        </button>
      </div>
    </header>

    <!-- ============================================== -->
    <!-- VIEW 1: REGION MAP OVERVIEW (BOSH XARITA)       -->
    <!-- ============================================== -->
    <main id="regionView" class="view-container active">
      <div class="region-grid">
        
        <!-- Left: Interactive Map -->
        <section class="card">
          <div class="card-header-row">
            <div class="card-title">
              <span>🗺️ Namangan viloyati xaritasi</span>
            </div>
            <span class="badge-count">12 ta tuman va shahar</span>
          </div>

          <!-- SVG Map Container -->
          <div class="map-svg-wrap">
            <svg class="namangan-map" viewBox="0 0 687 501" xmlns="http://www.w3.org/2000/svg">
              <!-- Polygons -->
              <g id="polygonsGroup">
                {chr(10).join(svg_polygons)}
              </g>

              <!-- Text Labels -->
              <g id="labelsGroup">
                {chr(10).join(svg_labels)}
              </g>
            </svg>
          </div>

          <!-- Quick Selector Buttons -->
          <div class="button-selector-box">
            <div class="selector-title">Tuman yoki shaharni tanlang (Ichki MFY va yerlarni ko'rish uchun bosing):</div>
            <div class="district-buttons-grid" id="buttonsGrid">
              {chr(10).join(buttons_html)}
            </div>
          </div>
        </section>

        <!-- Right: District Detail Passport Card -->
        <section class="card">
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

          <!-- Drill-down Button -->
          <button id="openDrilldownBtn" class="drilldown-action-btn" onclick="openDistrictDrilldown()">
            <span>🔍</span>
            <span id="drilldownBtnLabel">Ushbu tumanning MFY va ijara yerlariga o'tish</span>
            <span>➔</span>
          </button>

          <!-- MFY Preview List -->
          <div class="mfy-section">
            <div class="mfy-header-row">
              <span class="mfy-title">🏘️ MFYlar va ixtisoslashuv (tanlash uchun bosing)</span>
              <span id="mfyCount" class="badge-count">5 ta MFY</span>
            </div>
            <div id="mfyList" class="mfy-list">
              <!-- Dynamic MFY Items -->
            </div>
          </div>

          <!-- Official Disclaimer about Davlatobod & Yangi Namangan -->
          <div class="note-box">
            <strong>ℹ️ Ma'muriy-hududiy eslatma:</strong> Taqdim etilgan rasmiy xarita tasvirida Namangan shahrining <strong>Davlatobod tumani</strong> hamda <strong>Yangi Namangan tumani</strong> chegaralari alohida ajratilmagan bo'lib, Namangan shahri va Namangan tumani tarkibida ko'rsatilgan. Geoportalda ularning MFYlari alohida belgilab kiritilgan.
          </div>
        </section>

      </div>
    </main>

    <!-- ======================================================== -->
    <!-- VIEW 2: DISTRICT DRILL-DOWN (MFY & IJARA YERLAR OYNASI)  -->
    <!-- ======================================================== -->
    <main id="districtView" class="view-container">
      <div class="drilldown-layout">
        
        <!-- Left: MFYs List Sidebar -->
        <aside class="mfy-sidebar">
          <div class="sidebar-header">
            <div class="sidebar-title">
              <span>🏘️</span>
              <span id="drilldownDistrictTitle">Pop tumani MFYlari</span>
            </div>
            <span id="sidebarMfySubtitle" class="sidebar-sub">Ijara yerlarini ko'rish uchun MFY ustiga bosing</span>
          </div>

          <input type="text" id="mfySearchInput" class="search-input" placeholder="MFY nomini qidirish..." oninput="filterMfyList(this.value)">

          <div id="drilldownMfyScroll" class="sidebar-mfy-scroll">
            <!-- Dynamic MFY items populated by JS -->
          </div>
        </aside>

        <!-- Center: Isolated District Zoom Map -->
        <section class="district-map-center">
          <div class="card-header-row">
            <div class="card-title">
              <span>🗺️</span>
              <span id="zoomedMapTitle">Pop tumani ajratilgan xaritasi</span>
            </div>
            <span class="badge-count" id="activeMfyBadge">MFY tanlanmagan</span>
          </div>

          <!-- Zoomed SVG viewport -->
          <div class="zoom-map-frame">
            <svg id="zoomedDistrictSvg" class="zoomed-district-svg" viewBox="0 0 687 501" xmlns="http://www.w3.org/2000/svg">
              <g id="zoomedDistrictLayer"></g>
              <g id="zoomedMfyMarkersLayer"></g>
            </svg>
          </div>

          <!-- Brief district specs bar -->
          <div class="button-selector-box">
            <div class="selector-title">Tuman agronomik ko'rsatkichlari:</div>
            <div class="metrics-grid" style="grid-template-columns: repeat(3, 1fr);">
              <div class="metric-item">
                <span class="metric-label">Tuproq boniteti</span>
                <span id="drillBonitet" class="metric-value">64 ball</span>
              </div>
              <div class="metric-item">
                <span class="metric-label">Tuproq namligi</span>
                <span id="drillMoisture" class="metric-value">62%</span>
              </div>
              <div class="metric-item">
                <span class="metric-label">Asosiy ekin</span>
                <span id="drillMainCrop" class="metric-value">Poliz va Mosh</span>
              </div>
            </div>
          </div>
        </section>

        <!-- Right: Lease Land Parcels Panel (MFY kesimidagi ijara yerlar) -->
        <aside class="parcel-detail-panel">
          <div class="parcel-header">
            <div class="parcel-title" id="parcelPanelTitle">Ijara yer maydonlari</div>
            <span class="sidebar-sub" id="parcelPanelSubtitle">Tanlangan MFY bo'yicha ajratilgan konturlar</span>
          </div>

          <div id="parcelsContainer" class="parcel-list-container">
            <!-- Dynamic parcel cards -->
          </div>
        </aside>

      </div>
    </main>

  </div>

  <script>
    const DISTRICTS_DATA = {json.dumps(districts, ensure_ascii=False)};
    let selectedDistrictId = 'pop';
    let selectedMfyId = null;
    let currentView = 'region';

    // View Switching
    function switchView(viewName) {{
      currentView = viewName;
      const regionView = document.getElementById('regionView');
      const districtView = document.getElementById('districtView');
      const backBtn = document.getElementById('backToRegionBtn');
      const mainTitle = document.getElementById('pageMainTitle');

      if (viewName === 'district') {{
        regionView.classList.remove('active');
        districtView.classList.add('active');
        backBtn.style.display = 'inline-flex';
        renderDrilldownView(selectedDistrictId);
      }} else {{
        districtView.classList.remove('active');
        regionView.classList.add('active');
        backBtn.style.display = 'none';
        mainTitle.textContent = 'NAMANGAN VILOYATI TUMANLARI INTERAKTIV XARITASI';
        renderDetails(selectedDistrictId);
      }}
    }}

    function openDistrictDrilldown(districtId) {{
      if (districtId) selectedDistrictId = districtId;
      switchView('district');
    }}

    // Render Mode 1 (Region Overview)
    function renderDetails(districtId) {{
      selectedDistrictId = districtId;
      const data = DISTRICTS_DATA[districtId];
      if (!data) return;

      document.getElementById('districtColorIndicator').style.backgroundColor = data.color;
      document.getElementById('districtName').textContent = data.name;
      document.getElementById('districtNumberBadge').textContent = '#' + data.number + ' hudud';
      document.getElementById('drilldownBtnLabel').textContent = data.name + "ning MFY va ijara yerlariga o'tish";

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

      if (mfys.length === 0) {{
        mfyListEl.innerHTML = '<div style="font-size:12px;color:var(--text-muted);padding:8px;">MFY ma\'lumotlari mavjud emas.</div>';
      }} else {{
        mfys.forEach(m => {{
          const item = document.createElement('div');
          item.className = 'mfy-item';
          item.title = "MFY ijara yerlarini ko'rish uchun bosing";
          item.innerHTML = `
            <div>
              <div class="mfy-name">${{m.name}}</div>
              <div class="mfy-spec">${{m.spec || 'Ixtisoslashuv ko\'rsatilmagan'}}</div>
            </div>
            <div class="mfy-area">${{m.area || '—'}}</div>
          `;
          item.addEventListener('click', () => {{
            selectedMfyId = m.id;
            switchView('district');
          }});
          mfyListEl.appendChild(item);
        }});
      }}

      // Highlight active polygon and button
      document.querySelectorAll('.district-poly').forEach(p => {{
        if (p.getAttribute('data-id') === districtId) {{
          p.classList.add('active');
        }} else {{
          p.classList.remove('active');
        }}
      }});

      document.querySelectorAll('.d-btn').forEach(b => {{
        if (b.getAttribute('data-id') === districtId) {{
          b.classList.add('active');
        }} else {{
          b.classList.remove('active');
        }}
      }});
    }}

    // Render Mode 2 (District & MFY Drill-Down View)
    function renderDrilldownView(districtId) {{
      const data = DISTRICTS_DATA[districtId];
      if (!data) return;

      document.getElementById('pageMainTitle').textContent = data.name.toUpperCase() + " IJARA YERLARI VA MFY KESIMI";
      document.getElementById('drilldownDistrictTitle').textContent = data.name + " MFYlari";
      document.getElementById('zoomedMapTitle').textContent = data.name + " ajratilgan xaritasi";

      // Agronomic specs
      document.getElementById('drillBonitet').textContent = data.tuproqQatlami.match(/\\d+\\s*ball/i) ? data.tuproqQatlami.match(/\\d+\\s*ball/i)[0] : "72 ball";
      document.getElementById('drillMoisture').textContent = data.tuproqNamligi ? data.tuproqNamligi.split(' ')[0] : "65%";
      document.getElementById('drillMainCrop').textContent = data.mosEkinlar ? data.mosEkinlar.split(',')[0] : "Sabzavotchilik";

      // Render Zoomed District SVG Polygon
      const svg = document.getElementById('zoomedDistrictSvg');
      const layer = document.getElementById('zoomedDistrictLayer');
      const markersLayer = document.getElementById('zoomedMfyMarkersLayer');
      layer.innerHTML = '';
      markersLayer.innerHTML = '';

      // Calculate viewBox zoom based on bbox
      const bbox = data.bbox;
      const pad = Math.max(bbox.w, bbox.h) * 0.18;
      const zoomX = Math.max(0, bbox.minX - pad);
      const zoomY = Math.max(0, bbox.minY - pad);
      const zoomW = bbox.w + pad * 2;
      const zoomH = bbox.h + pad * 2;
      svg.setAttribute('viewBox', `${{zoomX}} ${{zoomY}} ${{zoomW}} ${{zoomH}}`);

      // Add main polygon
      const poly = document.createElementNS('http://www.w3.org/2000/svg', 'polygon');
      poly.setAttribute('points', data.points);
      poly.setAttribute('fill', data.color);
      poly.setAttribute('stroke', '#ffffff');
      poly.setAttribute('stroke-width', '2.5');
      poly.setAttribute('filter', 'drop-shadow(0 0 12px rgba(0,0,0,0.5))');
      layer.appendChild(poly);

      // Render MFY list in sidebar
      const mfyScroll = document.getElementById('drilldownMfyScroll');
      mfyScroll.innerHTML = '';
      const mfys = data.mfys || [];

      // Determine default selected MFY
      if (!selectedMfyId || !mfys.some(m => m.id === selectedMfyId)) {{
        selectedMfyId = mfys.length > 0 ? mfys[0].id : null;
      }}

      // Place visual markers for MFYs inside the zoomed polygon
      const center = data.center || [bbox.minX + bbox.w/2, bbox.minY + bbox.h/2];
      const mfyCount = mfys.length;

      mfys.forEach((mfy, idx) => {{
        // Calculate offset pin positions around the center
        const angle = (idx / mfyCount) * 2 * Math.PI;
        const radiusX = (bbox.w * 0.25) * Math.min(1, 0.5 + (idx % 2)*0.4);
        const radiusY = (bbox.h * 0.25) * Math.min(1, 0.5 + (idx % 2)*0.4);
        const pinX = center[0] + Math.cos(angle) * radiusX;
        const pinY = center[1] + Math.sin(angle) * radiusY;

        // SVG Marker
        const g = document.createElementNS('http://www.w3.org/2000/svg', 'g');
        g.setAttribute('class', 'mfy-pin-group');
        g.setAttribute('data-id', mfy.id);
        g.style.cursor = 'pointer';

        const circle = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
        circle.setAttribute('cx', pinX);
        circle.setAttribute('cy', pinY);
        circle.setAttribute('r', '6');
        circle.setAttribute('fill', '#f59e0b');
        circle.setAttribute('stroke', '#ffffff');
        circle.setAttribute('stroke-width', '1.5');
        circle.setAttribute('class', 'mfy-pin-circle');
        if (mfy.id === selectedMfyId) circle.classList.add('active');

        const text = document.createElementNS('http://www.w3.org/2000/svg', 'text');
        text.setAttribute('x', pinX);
        text.setAttribute('y', pinY - 8);
        text.setAttribute('text-anchor', 'middle');
        text.setAttribute('fill', '#ffffff');
        text.setAttribute('font-size', '7.5px');
        text.setAttribute('font-weight', '800');
        text.setAttribute('paint-order', 'stroke fill');
        text.setAttribute('stroke', '#000000');
        text.setAttribute('stroke-width', '2px');
        text.textContent = mfy.name.replace(' MFY', '');

        g.appendChild(circle);
        g.appendChild(text);
        g.addEventListener('click', () => selectMfy(mfy.id));
        markersLayer.appendChild(g);

        // Sidebar Item
        const item = document.createElement('div');
        item.className = 'mfy-nav-item' + (mfy.id === selectedMfyId ? ' active' : '');
        item.setAttribute('data-id', mfy.id);
        item.innerHTML = `
          <div class="mfy-nav-top">
            <span class="mfy-nav-name">${{mfy.name}}</span>
            <span class="meta-tag">${{mfy.area || '—'}}</span>
          </div>
          <div class="mfy-nav-spec">${{mfy.spec || 'Ixtisoslashuv mavjud'}}</div>
          <div class="mfy-nav-meta">
            <span>👨‍👩‍👦 ${{mfy.poorFamilies || 80}} ta oila</span>
            <span>•</span>
            <span>📍 ${{(mfy.parcels || []).length}} ta ijara konturi</span>
          </div>
        `;
        item.addEventListener('click', () => selectMfy(mfy.id));
        mfyScroll.appendChild(item);
      }});

      renderParcelsForMfy(selectedMfyId);
    }}

    function selectMfy(mfyId) {{
      selectedMfyId = mfyId;
      document.querySelectorAll('.mfy-nav-item').forEach(el => {{
        if (el.getAttribute('data-id') === mfyId) {{
          el.classList.add('active');
        }} else {{
          el.classList.remove('active');
        }}
      }});

      // Update pins active state
      document.querySelectorAll('.mfy-pin-circle').forEach(c => c.classList.remove('active'));
      const activeGroup = document.querySelector(`.mfy-pin-group[data-id="${{mfyId}}"] circle`);
      if (activeGroup) activeGroup.classList.add('active');

      renderParcelsForMfy(mfyId);
    }}

    function renderParcelsForMfy(mfyId) {{
      const distData = DISTRICTS_DATA[selectedDistrictId];
      if (!distData) return;

      const mfy = (distData.mfys || []).find(m => m.id === mfyId) || (distData.mfys || [])[0];
      const parcelsContainer = document.getElementById('parcelsContainer');
      const badge = document.getElementById('activeMfyBadge');

      if (!mfy) {{
        badge.textContent = 'MFY tanlanmagan';
        parcelsContainer.innerHTML = '<div style="color:var(--text-muted);font-size:12px;padding:12px;">Tanlangan MFY topilmadi.</div>';
        return;
      }}

      badge.textContent = mfy.name;
      document.getElementById('parcelPanelTitle').textContent = mfy.name + " ijara yerlari";
      document.getElementById('parcelPanelSubtitle').textContent = `Jami maydon: ${{mfy.area || '—'}} | Ixtisoslashuv: ${{mfy.spec || '—'}}`;

      parcelsContainer.innerHTML = '';
      const parcels = mfy.parcels || [];

      if (parcels.length === 0) {{
        parcelsContainer.innerHTML = '<div style="color:var(--text-muted);font-size:12px;padding:12px;">Ushbu MFY bo\'yicha yer maydonlari ro\'yxati tayyorlanmoqda.</div>';
        return;
      }}

      parcels.forEach((p, idx) => {{
        const card = document.createElement('div');
        card.className = 'parcel-card';
        card.innerHTML = `
          <div class="parcel-card-top">
            <span class="contour-badge">${{p.contourNumber || (idx+1) + '-kontur'}}</span>
            <span class="highlight-area">${{p.allocatedAreaHa || 0.5}} gektar</span>
          </div>

          <div>
            <div class="farmer-name">${{p.farmerName || 'Ijara oluvchi dehqon'}}</div>
            <div style="font-size:11px;color:var(--text-muted);">${{p.familyStatus || 'Ijtimoiy daftardagi oila'}} • Muddat: ${{p.contractYear || '10 yil'}}</div>
          </div>

          <div class="parcel-props">
            <div class="parcel-prop-box">
              <span class="prop-k">Tuproq boniteti</span>
              <span class="prop-v">${{p.soil && p.soil.bonitetScore ? p.soil.bonitetScore + ' ball' : '75 ball'}}</span>
            </div>
            <div class="parcel-prop-box">
              <span class="prop-k">Tuproq namligi</span>
              <span class="prop-v">${{p.soil && p.soil.moisture ? p.soil.moisture : '70%'}}</span>
            </div>
            <div class="parcel-prop-box">
              <span class="prop-k">Asosiy ekin</span>
              <span class="prop-v">${{p.recommendation && p.recommendation.primaryCrop ? p.recommendation.primaryCrop : 'Sabzavot'}}</span>
            </div>
            <div class="parcel-prop-box">
              <span class="prop-k">Kutilayotgan daromad</span>
              <span class="prop-v highlight-money">${{p.economics && p.economics.netProfitUzs ? (p.economics.netProfitUzs / 1000000).toFixed(1) + ' mln so\'m' : '30+ mln so\'m'}}</span>
            </div>
          </div>
        `;
        parcelsContainer.appendChild(card);
      }});
    }}

    function filterMfyList(query) {{
      const text = query.trim().toLowerCase();
      document.querySelectorAll('.mfy-nav-item').forEach(item => {{
        const name = item.querySelector('.mfy-nav-name').textContent.toLowerCase();
        const spec = item.querySelector('.mfy-nav-spec').textContent.toLowerCase();
        if (name.includes(text) || spec.includes(text)) {{
          item.style.display = 'flex';
        }} else {{
          item.style.display = 'none';
        }}
      }});
    }}

    // Event listeners for polygons on main regional map
    document.querySelectorAll('.district-poly').forEach(poly => {{
      poly.addEventListener('click', () => {{
        const id = poly.getAttribute('data-id');
        renderDetails(id);
        openDistrictDrilldown(id);
      }});
    }});

    // Event listeners for district buttons
    document.querySelectorAll('.d-btn').forEach(btn => {{
      btn.addEventListener('click', () => {{
        const id = btn.getAttribute('data-id');
        renderDetails(id);
        openDistrictDrilldown(id);
      }});
    }});

    // Theme toggle
    const themeBtn = document.getElementById('themeToggle');
    const themeIcon = document.getElementById('themeIcon');
    const themeLabel = document.getElementById('themeLabel');

    themeBtn.addEventListener('click', () => {{
      const isDark = document.documentElement.classList.toggle('dark');
      if (isDark) {{
        themeIcon.textContent = '☀️';
        themeLabel.textContent = 'Kunduzgi rejim';
      }} else {{
        themeIcon.textContent = '🌙';
        themeLabel.textContent = 'Tungi rejim';
      }}
    }});

    // Initial render
    renderDetails('pop');
  </script>
</body>
</html>
"""

with open('namangan_interaktiv_xarita.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

with open('public/namangan_interaktiv_xarita.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Generated full drill-down interactive map successfully!")
