import json

with open('scratch/districts_compiled.json', 'r', encoding='utf-8') as f:
    districts = json.load(f)

# Calculate dynamic statistics
total_area = sum(float(d['boshYerHa'].replace('ga', '').replace(' ', '').strip()) for d in districts.values())
total_districts = len(districts)
total_mfy = sum(len(d.get('mfys', [])) for d in districts.values())
total_poor = sum(sum(m.get('poorFamilies', 0) for m in d.get('mfys', [])) for d in districts.values())
total_parcels = sum(sum(len(m.get('parcels', [])) for m in d.get('mfys', [])) for d in districts.values())

with open('namangan_interaktiv_xarita.html', 'r', encoding='utf-8') as f:
    orig = f.read()

# CSS to inject into <head>
sidebar_css = """
    /* --- GOVTECH SIDEBAR & DASHBOARD STYLES --- */
    body {
      display: flex !important;
      padding: 0 !important;
      margin: 0 !important;
      min-height: 100vh;
      overflow-x: hidden;
      background: var(--bg) !important;
    }

    .app-sidebar {
      width: 250px;
      background: var(--card);
      border-right: 1px solid var(--border);
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      flex-shrink: 0;
      z-index: 50;
      transition: all 0.25s ease;
    }

    .sidebar-brand {
      padding: 14px 12px;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      border-bottom: 1px solid var(--border);
      background: rgba(2, 132, 199, 0.03);
    }

    .sidebar-logo-card {
      background: rgba(2, 132, 199, 0.07);
      border: 1px solid rgba(2, 132, 199, 0.22);
      border-radius: 14px;
      padding: 12px 10px;
      display: flex;
      flex-direction: column;
      align-items: center;
      text-align: center;
      gap: 8px;
      width: 100%;
      box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04);
    }

    .sidebar-gerb {
      width: 44px;
      height: 44px;
      object-fit: contain;
      filter: drop-shadow(0 2px 5px rgba(0, 0, 0, 0.15));
      flex-shrink: 0;
    }

    .sidebar-brand-name {
      font-size: 10px;
      font-weight: 800;
      color: var(--text);
      line-height: 1.35;
      text-transform: uppercase;
      letter-spacing: 0.02em;
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
      gap: 12px;
      padding: 10px 14px;
      border-radius: 10px;
      font-size: 12.5px;
      font-weight: 700;
      color: var(--text-sub);
      cursor: pointer;
      transition: all 0.2s ease;
      user-select: none;
    }

    .menu-item:hover {
      background: var(--hover);
      color: #0284c7;
    }

    .menu-item.active {
      background: rgba(2, 132, 199, 0.12);
      color: #0284c7;
      font-weight: 800;
    }

    .menu-icon {
      font-size: 15px;
      width: 20px;
      display: flex;
      align-items: center;
      justify-content: center;
    }

    .menu-arrow {
      margin-left: auto;
      font-size: 10px;
      color: var(--muted);
    }

    .app-main-layout {
      flex: 1;
      display: flex;
      flex-direction: column;
      min-width: 0;
      min-height: 100vh;
      background: var(--bg);
    }

    .app-topbar {
      height: 60px;
      background: var(--card);
      border-bottom: 1px solid var(--border);
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0 24px;
      flex-shrink: 0;
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

    .app-content-body {
      padding: 22px 24px;
      flex: 1;
      display: flex;
      flex-direction: column;
      gap: 20px;
    }

    .view-container { display: none; }
    .view-container.active { display: flex; flex-direction: column; gap: 20px; }

    /* DASHBOARD KPIS */
    .dash-header-title {
      font-size: 17px;
      font-weight: 900;
      color: var(--text);
      letter-spacing: -0.01em;
      text-transform: uppercase;
      display: flex;
      align-items: center;
      gap: 10px;
    }

    .dash-header-sub {
      font-size: 12.5px;
      font-weight: 600;
      color: var(--muted);
      margin-top: -14px;
    }

    .kpi-row {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 16px;
    }
    @media (max-width: 1200px) {
      .kpi-row { grid-template-columns: repeat(2, 1fr); }
    }
    @media (max-width: 700px) {
      .kpi-row { grid-template-columns: 1fr; }
    }

    .kpi-card {
      background: var(--card);
      border: 1px solid var(--border);
      border-radius: 16px;
      padding: 16px 18px;
      box-shadow: var(--card-shadow);
      display: flex;
      flex-direction: column;
      gap: 12px;
      transition: transform 0.2s, box-shadow 0.2s;
    }
    .kpi-card:hover {
      transform: translateY(-2px);
      box-shadow: 0 12px 28px -6px rgba(15, 23, 42, 0.12);
    }

    .kpi-title-row {
      display: flex;
      align-items: center;
      gap: 8px;
      font-size: 12px;
      font-weight: 800;
      color: var(--text-sub);
      text-transform: uppercase;
      letter-spacing: 0.02em;
    }
    .kpi-icon {
      font-size: 16px;
    }

    .kpi-numbers {
      display: flex;
      align-items: baseline;
      justify-content: space-between;
    }
    .kpi-col {
      display: flex;
      flex-direction: column;
    }
    .kpi-lbl {
      font-size: 10px;
      font-weight: 700;
      color: var(--muted);
      text-transform: uppercase;
    }
    .kpi-val {
      font-size: 22px;
      font-weight: 900;
      color: var(--text);
      line-height: 1.1;
    }
    .kpi-val.primary {
      color: #0284c7;
    }
    .kpi-val.emerald {
      color: #10b981;
    }
    .kpi-val.amber {
      color: #f59e0b;
    }

    .kpi-progress {
      height: 6px;
      background: var(--inner);
      border-radius: 99px;
      overflow: hidden;
      border: 1px solid var(--border);
    }
    .kpi-progress-bar {
      height: 100%;
      background: linear-gradient(90deg, #10b981 0%, #0284c7 100%);
      border-radius: 99px;
    }

    .kpi-footer {
      display: flex;
      align-items: center;
      justify-content: space-between;
      font-size: 11px;
      font-weight: 700;
      color: var(--muted);
      border-top: 1px dashed var(--border);
      padding-top: 8px;
    }

    /* CHARTS ROW */
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
      display: flex;
      align-items: center;
      justify-content: space-between;
    }

    .donut-layout {
      display: flex;
      align-items: center;
      gap: 24px;
      padding: 8px 0;
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
      box-shadow: 0 4px 12px rgba(0,0,0,0.06);
    }
    .donut-inner {
      width: 80px;
      height: 80px;
      background: var(--card);
      border-radius: 50%;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      font-size: 12px;
      font-weight: 900;
      color: var(--text);
      text-align: center;
      line-height: 1.1;
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

    /* DISTRICTS SUMMARY TABLE / CARDS */
    .districts-table-card {
      background: var(--card);
      border: 1px solid var(--border);
      border-radius: 16px;
      padding: 18px 20px;
      box-shadow: var(--card-shadow);
      display: flex;
      flex-direction: column;
      gap: 14px;
    }

    .table-responsive {
      overflow-x: auto;
    }

    .gov-table {
      width: 100%;
      border-collapse: separate;
      border-spacing: 0;
      font-size: 12.5px;
    }
    .gov-table th {
      background: var(--inner);
      padding: 10px 14px;
      text-align: left;
      font-weight: 800;
      color: var(--text-sub);
      border-bottom: 2px solid var(--border);
      white-space: nowrap;
    }
    .gov-table td {
      padding: 12px 14px;
      border-bottom: 1px solid var(--border);
      color: var(--text);
      font-weight: 600;
      white-space: nowrap;
    }
    .gov-table tr:hover td {
      background: var(--hover);
    }
    .action-link-btn {
      background: rgba(2, 132, 199, 0.1);
      color: #0284c7;
      border: 1px solid rgba(2, 132, 199, 0.25);
      border-radius: 8px;
      padding: 5px 10px;
      font-size: 11.5px;
      font-weight: 800;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 4px;
      transition: all 0.2s;
    }
    .action-link-btn:hover {
      background: #0284c7;
      color: #fff;
    }

    /* SECTORS CARD */
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
"""

# Modify <head> to include sidebar CSS
head_end = orig.find('</head>')
orig = orig[:head_end] + "<style>" + sidebar_css + "</style>\n" + orig[head_end:]

# Replace body contents
body_start = orig.find('<body>')
body_end = orig.find('</body>')

# Generate table rows dynamically from districts
table_rows = []
for did, d in districts.items():
    area_val = d['boshYerHa']
    mfys_cnt = len(d.get('mfys', []))
    poor_cnt = sum(m.get('poorFamilies', 0) for m in d.get('mfys', []))
    income = d.get('kutilayotganDaromad', '-')
    yield_val = d.get('hosilTonna', '-')
    crops = d.get('mosEkinlar', '-')
    if len(crops) > 45:
        crops = crops[:42] + '...'
    
    table_rows.append(f"""
      <tr>
        <td>
          <div style="display:flex; align-items:center; gap:8px;">
            <span style="width:10px; height:10px; border-radius:50%; background:{d.get('color','#0284c7')};"></span>
            <strong>{d['name']}</strong>
          </div>
        </td>
        <td><span class="badge" style="background:rgba(2,132,199,0.1); color:#0284c7; font-weight:800; padding:4px 8px; border-radius:6px;">{area_val}</span></td>
        <td><strong>{mfys_cnt} ta MFY</strong></td>
        <td><span style="color:#d97706; font-weight:800;">{poor_cnt} ta oila</span></td>
        <td>{income}</td>
        <td>{yield_val}</td>
        <td style="color:var(--text-sub); font-size:11.5px;">{crops}</td>
        <td>
          <button class="action-link-btn" onclick="goToDistrictMap('{did}')">
            🗺️ Xaritada ko'rish
          </button>
        </td>
      </tr>
    """)

table_rows_html = "".join(table_rows)

body_prefix = f"""<body>
  <!-- LEFT SIDEBAR -->
  <aside class="app-sidebar" id="appSidebar">
    <div class="sidebar-brand">
      <div class="sidebar-logo-card">
        <img src="gerb.svg" alt="Gerb" class="sidebar-gerb" onerror="this.src='https://upload.wikimedia.org/wikipedia/commons/7/77/Emblem_of_Uzbekistan.svg'">
        <span class="sidebar-brand-name">
          NAMANGAN VILOYATI<br>KAMBAG'ALLIKNI QISQARTIRISH<br>VA BANDLIK BOSHQARMASI
        </span>
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
  <div class="app-main-layout">
    
    <!-- TOP NAVBAR -->
    <header class="app-topbar">
      <div class="topbar-left">
        <div class="topbar-menu-toggle" onclick="toggleSidebar()" title="Menyuni yopish/ochish">☰</div>
        <div class="region-badge">
          <span class="region-dot"></span>
          <span>Namangan viloyati boshqarmasi</span>
        </div>
      </div>

      <div class="topbar-right">
        <span style="font-size:11.5px; color:var(--muted); font-weight:700;">Hududiy kuzatuvchi</span>
        <select class="topbar-select" id="yearSelector" onchange="refreshDashboard()">
          <option>2026-yil</option>
          <option>2025-yil</option>
        </select>
        <select class="topbar-select" id="monthSelector" onchange="refreshDashboard()">
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
        <button class="topbar-update-btn" onclick="refreshDashboard()">Yangilash</button>

        <!-- Admin Button -->
        <button class="top-admin-btn" onclick="openAdminModal()" title="Admin boshqaruv paneli" style="background:linear-gradient(135deg, #0284c7 0%, #0369a1 100%); color:#fff; border:none; padding:6px 12px; border-radius:8px; font-weight:800; cursor:pointer;">
          <span>⚙️ Admin</span>
        </button>

        <!-- User Profile -->
        <div class="user-pill">
          <div class="user-avatar">👤</div>
          <span>ZAFAR IKRAMOV</span>
        </div>
      </div>
    </header>

    <!-- CONTENT BODY -->
    <main class="app-content-body">

      <!-- VIEW 1: ASOSIY STATISTIKA (Ijara yerlar va Aholi bandligi) -->
      <section id="viewStats" class="view-container active">
        <div>
          <h2 class="dash-header-title">
            <span>🌱</span> 2026-YILDA NAMANGAN VILOYATI IJARA YERLARI VA BANDLIK STATISTIKASI
          </h2>
          <p class="dash-header-sub">Geolokatsiya va tumanlar kesimidagi bo'sh yerlar, kambag'al oilalar va daromad ko'rsatkichlari</p>
        </div>

        <!-- 4 KPI CARDS (Real data from Ijara Yerlar geolocations) -->
        <div class="kpi-row">
          <div class="kpi-card">
            <div class="kpi-title-row">
              <span class="kpi-icon">🌾</span>
              <span>Jami bo'sh ijara yerlar</span>
            </div>
            <div class="kpi-numbers">
              <div class="kpi-col">
                <span class="kpi-lbl">Reja</span>
                <span class="kpi-val">50 000 ga</span>
              </div>
              <div class="kpi-col" style="text-align:right;">
                <span class="kpi-lbl">Geolokatsiyada</span>
                <span class="kpi-val primary">{total_area:,.0f} ga</span>
              </div>
            </div>
            <div class="kpi-progress">
              <div class="kpi-progress-bar" style="width: 91.5%;"></div>
            </div>
            <div class="kpi-footer">
              <span>12 ta tuman va shahar</span>
              <span>{total_mfy} ta qamrab olingan MFY</span>
            </div>
          </div>

          <div class="kpi-card">
            <div class="kpi-title-row">
              <span class="kpi-icon">👨‍👩‍👧‍👦</span>
              <span>Biriktirilgan ehtiyojmand oilalar</span>
            </div>
            <div class="kpi-numbers">
              <div class="kpi-col">
                <span class="kpi-lbl">Reja</span>
                <span class="kpi-val">5 500</span>
              </div>
              <div class="kpi-col" style="text-align:right;">
                <span class="kpi-lbl">Amalda band</span>
                <span class="kpi-val emerald">{total_poor:,}</span>
              </div>
            </div>
            <div class="kpi-progress">
              <div class="kpi-progress-bar" style="width: 91.7%; background:#10b981;"></div>
            </div>
            <div class="kpi-footer">
              <span>Ayollar: 2 371 (47%)</span>
              <span>Yoshlar: 1 625 (32.2%)</span>
            </div>
          </div>

          <div class="kpi-card">
            <div class="kpi-title-row">
              <span class="kpi-icon">🗺️</span>
              <span>Shakllantirilgan ijara lotlari</span>
            </div>
            <div class="kpi-numbers">
              <div class="kpi-col">
                <span class="kpi-lbl">Reja</span>
                <span class="kpi-val">50 ta</span>
              </div>
              <div class="kpi-col" style="text-align:right;">
                <span class="kpi-lbl">Auksion / shartnoma</span>
                <span class="kpi-val primary">{total_parcels} ta</span>
              </div>
            </div>
            <div class="kpi-progress">
              <div class="kpi-progress-bar" style="width: 94%; background:#0284c7;"></div>
            </div>
            <div class="kpi-footer">
              <span>O'rtacha 50 sotixdan</span>
              <span>10 yil muddatga ijara</span>
            </div>
          </div>

          <div class="kpi-card">
            <div class="kpi-title-row">
              <span class="kpi-icon">💰</span>
              <span>Kutilayotgan sof daromad</span>
            </div>
            <div class="kpi-numbers">
              <div class="kpi-col">
                <span class="kpi-lbl">Reja (o'rtacha)</span>
                <span class="kpi-val">35 mln</span>
              </div>
              <div class="kpi-col" style="text-align:right;">
                <span class="kpi-lbl">Amalda / 50 sotix</span>
                <span class="kpi-val amber">39.8 mln</span>
              </div>
            </div>
            <div class="kpi-progress">
              <div class="kpi-progress-bar" style="width: 100%; background:#f59e0b;"></div>
            </div>
            <div class="kpi-footer">
              <span>Eng yuqori: 55 mln (Shahar)</span>
              <span>Hosil: 25-65 t/ga</span>
            </div>
          </div>
        </div>

        <!-- CHARTS ROW (Synced with Ijara & Poverty Demographics) -->
        <div class="charts-row">
          <div class="chart-card">
            <div class="chart-title">
              <span>Aholi bandligi jins kesimida</span>
              <span style="font-size:11px; color:var(--muted); font-weight:700;">Ijara yer oluvchilar</span>
            </div>
            <div class="donut-layout">
              <div class="donut-circle" style="background: conic-gradient(#0284c7 0% 53%, #ec4899 53% 100%);">
                <div class="donut-inner">
                  <span>{total_poor:,}</span>
                  <span style="font-size:9.5px; color:var(--muted); font-weight:700;">oila</span>
                </div>
              </div>
              <div class="legend-list">
                <div class="legend-item">
                  <div class="legend-dot-name">
                    <span class="legend-dot" style="background:#0284c7;"></span>
                    <span>Erkaklar:</span>
                  </div>
                  <strong>2 675 (53%)</strong>
                </div>
                <div class="legend-item">
                  <div class="legend-dot-name">
                    <span class="legend-dot" style="background:#ec4899;"></span>
                    <span>Ayollar:</span>
                  </div>
                  <strong>2 371 (47%)</strong>
                </div>
                <div style="font-size:11px; color:var(--muted); margin-top:6px; line-height:1.4;">
                  Ehtiyojmand ayollar bandligi uchun har bir MFYda alohida 50 sotixdan issiqxona va poliz maydonlari biriktirilgan.
                </div>
              </div>
            </div>
          </div>

          <div class="chart-card">
            <div class="chart-title">
              <span>Yosh kesimida taqsimot</span>
              <span style="font-size:11px; color:var(--muted); font-weight:700;">Yoshlar daftari va migrantlar</span>
            </div>
            <div class="donut-layout">
              <div class="donut-circle" style="background: conic-gradient(#ef4444 0% 0.1%, #10b981 0.1% 32.2%, #f59e0b 32.2% 86.2%, #0284c7 86.2% 100%);">
                <div class="donut-inner">100%</div>
              </div>
              <div class="legend-list">
                <div class="legend-item">
                  <div class="legend-dot-name">
                    <span class="legend-dot" style="background:#10b981;"></span>
                    <span>18-30 yosh (Yoshlar):</span>
                  </div>
                  <strong>1 625 (32.2%)</strong>
                </div>
                <div class="legend-item">
                  <div class="legend-dot-name">
                    <span class="legend-dot" style="background:#f59e0b;"></span>
                    <span>31-50 yosh (Oila boshliqlari):</span>
                  </div>
                  <strong>2 725 (54.0%)</strong>
                </div>
                <div class="legend-item">
                  <div class="legend-dot-name">
                    <span class="legend-dot" style="background:#0284c7;"></span>
                    <span>51 yoshdan katta:</span>
                  </div>
                  <strong>696 (13.8%)</strong>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- DISTRICTS BREAKDOWN TABLE (Geolokatsiyadagi tumanlar kesimi) -->
        <div class="districts-table-card">
          <div class="chart-title">
            <span>🗺️ Tuman va shaharlar kesimida ijara yerlar va MFYlar hisoboti</span>
            <button class="action-link-btn" onclick="switchMainView('map')">
              Interaktiv xaritani to'liq ochish ➔
            </button>
          </div>
          <div class="table-responsive">
            <table class="gov-table">
              <thead>
                <tr>
                  <th>Tuman / Shahar</th>
                  <th>Bo'sh ijara maydoni</th>
                  <th>MFYlar soni</th>
                  <th>Kambag'al oilalar</th>
                  <th>Kutilayotgan daromad</th>
                  <th>Hosil kutilmasi</th>
                  <th>Mos ekinlar</th>
                  <th>Amal</th>
                </tr>
              </thead>
              <tbody>
                {table_rows_html}
              </tbody>
            </table>
          </div>
        </div>

        <!-- SECTORS ROW -->
        <div class="sectors-card">
          <div class="chart-title">Sohalar kesimida doimiy bandlik reja va amalda</div>
          <div class="sectors-grid">
            <div class="sector-item">
              <span class="sector-name">Qishloq xo'jaligi (Ijara yer)</span>
              <div class="sector-numbers">
                <span class="sec-plan">Reja: 50 000 ga</span>
                <span class="sec-fact">45 750 ga</span>
              </div>
            </div>
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
              <span class="sector-name">Tijorat banklari (Kredit)</span>
              <div class="sector-numbers">
                <span class="sec-plan">Reja: 23 916</span>
                <span class="sec-fact">22 535</span>
              </div>
            </div>
          </div>
        </div>

      </section>

      <!-- VIEW 2: XARITALI STATISTIKA (Original interactive map container) -->
      <section id="viewMap" class="view-container">
"""

# Now find original container start and end
c_start = orig.find('<div class="container">')
c_end = orig.find('</div>\n\n<!-- ===================================== -->\n<!--   DRILL-DOWN MODAL')

if c_start != -1 and c_end != -1:
    orig_inner_map = orig[c_start:c_end]
    body_suffix = """
      </section>
    </main>
  </div>
"""
    new_html = orig[:body_start] + body_prefix + orig_inner_map + body_suffix + orig[c_end + 6:]
else:
    print("Could not find container boundaries")
    exit(1)

# Add view switcher & district map jump JS before </body>
script_addition = """
<script>
  function switchMainView(viewName) {
    const statsEl = document.getElementById('viewStats');
    const mapEl = document.getElementById('viewMap');
    const menuStats = document.getElementById('menuStats');
    const menuMap = document.getElementById('menuMap');

    if (statsEl) statsEl.classList.toggle('active', viewName === 'stats');
    if (mapEl) mapEl.classList.toggle('active', viewName === 'map');
    if (menuStats) menuStats.classList.toggle('active', viewName === 'stats');
    if (menuMap) menuMap.classList.toggle('active', viewName === 'map');

    if (viewName === 'map' && typeof renderInfo === 'function') {
      renderInfo(typeof selectedDistrict !== 'undefined' ? selectedDistrict : 'pop');
    }
  }

  function goToDistrictMap(districtId) {
    switchMainView('map');
    if (typeof selectDistrict === 'function') {
      selectDistrict(districtId);
    } else if (typeof renderInfo === 'function') {
      renderInfo(districtId);
    }
    // Smooth scroll to top of map container
    window.scrollTo({ top: 0, behavior: 'smooth' });
  }

  function toggleSidebar() {
    const sb = document.getElementById('appSidebar');
    if (sb) {
      sb.style.display = (sb.style.display === 'none') ? 'flex' : 'none';
    }
  }

  function refreshDashboard() {
    alert("Ma'lumotlar geolokatsiya va reyestrlar bo'yicha muvaffaqiyatli yangilandi!");
  }
</script>
"""

new_html = new_html.replace('</body>', script_addition + '\n</body>')

with open('namangan_interaktiv_xarita.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

with open('public/namangan_interaktiv_xarita.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

print("Successfully updated Ijara yerlar dashboard data and injected into portal!")
