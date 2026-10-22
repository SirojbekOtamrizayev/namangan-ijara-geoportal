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
      padding: 16px 18px;
      display: flex;
      align-items: center;
      gap: 12px;
      border-bottom: 1px solid var(--border);
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
      color: #0284c7;
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
      color: var(--muted);
      cursor: pointer;
      transition: all 0.15s ease;
      text-decoration: none;
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

    .app-main-layout {
      flex: 1;
      display: flex;
      flex-direction: column;
      min-width: 0;
      min-height: 100vh;
    }

    .app-topbar {
      height: 64px;
      background: var(--card);
      border-bottom: 1px solid var(--border);
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
      border-top: 1px solid var(--border);
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
"""

# Modify <head> to include sidebar CSS
head_end = orig.find('</head>')
orig = orig[:head_end] + "<style>" + sidebar_css + "</style>\n" + orig[head_end:]

# Replace body contents
body_start = orig.find('<body>')
body_end = orig.find('</body>')

body_prefix = """<body>
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
  <div class="app-main-layout">
    
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

      <!-- VIEW 1: ASOSIY STATISTIKA -->
      <section id="viewStats" class="view-container active">
        <h2 class="dash-header-title">2026 YILDA AHOLINI DAROMADLI MEHNAT BILAN TA'MINLASH</h2>

        <!-- 4 KPI CARDS -->
        <div class="kpi-row">
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

        <!-- CHARTS ROW -->
        <div class="charts-row">
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

        <!-- SECTORS ROW -->
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

      <!-- VIEW 2: XARITALI STATISTIKA (Original map container) -->
      <section id="viewMap" class="view-container">
"""

# Now find original container start and end
c_start = orig.find('<div class="container">')
c_end = orig.find('</div>\n\n<!-- ===================================== -->\n<!--   DRILL-DOWN MODAL')

if c_start != -1 and c_end != -1:
    orig_inner_map = orig[c_start:c_end]
    # Remove outer <div class="container"> and its closing </div>
    # Also adjust header in map view
    body_suffix = """
      </section>
    </main>
  </div>
"""
    # Replace body content up to modals
    new_html = orig[:body_start] + body_prefix + orig_inner_map + body_suffix + orig[c_end + 6:]
else:
    print("Could not find container boundaries")
    exit(1)

# Add view switcher JS before </body>
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

  function toggleSidebar() {
    const sb = document.getElementById('appSidebar');
    if (sb) {
      sb.style.display = (sb.style.display === 'none') ? 'flex' : 'none';
    }
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

print("Successfully injected GovTech sidebar and dashboard! New size:", len(new_html))
