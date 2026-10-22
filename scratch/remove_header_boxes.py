files = ['index.html', 'namangan_interaktiv_xarita.html', 'public/namangan_interaktiv_xarita.html']

# Remove left red box: header-logo-box (emblem + org title)
old_logo = """      <div class="header-logo-box">
        <img src="gerb.svg" alt="O'zbekiston Davlat Gerbi" class="header-gerb-img" onerror="this.onerror=null; this.src='https://upload.wikimedia.org/wikipedia/commons/7/77/Emblem_of_Uzbekistan.svg';">
        <span class="header-org-title">Namangan viloyati Kambag'allikni qisqartirish va bandlik boshqarmasi</span>
      </div>"""

# Remove right red box: header-actions div (weather + admin btn + theme btn)
old_actions = """    <div class="header-actions">
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
    </div>"""

for filepath in files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    changed = False
    
    # Try direct match first, then normalized
    for old in [old_logo, old_actions]:
        if old in content:
            content = content.replace(old, '')
            changed = True
        else:
            cn = content.replace('\r\n', '\n')
            on = old.replace('\r\n', '\n')
            if on in cn:
                content = cn.replace(on, '')
                changed = True
    
    if changed:
        print(f"Patched {filepath}")
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
    else:
        print(f"Could not find blocks in {filepath}")
