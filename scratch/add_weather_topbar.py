files = ['index.html', 'namangan_interaktiv_xarita.html', 'public/namangan_interaktiv_xarita.html']

old_block = """        <button class="topbar-update-btn" onclick="refreshDashboard()">Yangilash</button>


      </div>
    </header>"""

new_block = """        <button class="topbar-update-btn" onclick="refreshDashboard()">Yangilash</button>

        <!-- Weather Widget in topbar -->
        <div class="weather-widget" style="background:rgba(2,132,199,0.1); border:1px solid rgba(2,132,199,0.25);">
          <div class="weather-sun" id="weatherIconTop">&#x2600;&#xFE0F;</div>
          <div class="weather-info">
            <div class="weather-tags">
              <span class="weather-city-pill" id="weatherCityTop">Namangan sh.</span>
              <span class="weather-air-pill" id="weatherAirTop">&#x1F4A8; PM 2.5 &mdash; A&rsquo;lo</span>
            </div>
            <div class="weather-temp" id="weatherTempTop" style="font-size:12px;">+9&deg; &mdash; +20&deg;</div>
          </div>
        </div>

      </div>
    </header>"""

for filepath in files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    content_norm = content.replace('\r\n', '\n')
    old_norm = old_block.replace('\r\n', '\n')
    
    if old_norm in content_norm:
        content_norm = content_norm.replace(old_norm, new_block)
        print(f"Replaced in {filepath}")
    else:
        print(f"NOT FOUND in {filepath}")
        continue
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content_norm)
