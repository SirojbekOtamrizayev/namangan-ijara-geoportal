files = ['index.html', 'namangan_interaktiv_xarita.html', 'public/namangan_interaktiv_xarita.html']

old_header_block = """  <!-- Header -->
  <header>
    <div class="header-left">

      <div class="header-titles">
        <span class="portal-tag">Namangan viloyati ijara yerlar geoportali</span>
        <h1 class="main-title">NAMANGAN VILOYATI TUMANLARI INTERAKTIV XARITASI</h1>
        <div class="accent-bar"></div>
      </div>
    </div>
    

  </header>"""

new_header_block = """  <!-- Header -->
  <header style="padding: 12px 24px;">
    <div class="header-left">
      <div class="header-titles">
        <span class="portal-tag" style="font-size: 13px; letter-spacing: 0.08em;">Namangan viloyati ijara yerlar geoportali</span>
      </div>
    </div>
  </header>"""

old_card_header = """      <div class="card-header">
        <div class="card-title">🗺️ Namangan viloyati xaritasi</div>
        <span class="badge">12 ta tuman va shahar</span>
      </div>"""

for filepath in files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    cn = content.replace('\r\n', '\n')
    
    # 1. Replace header to keep only "Namangan viloyati ijara yerlar geoportali"
    if old_header_block in cn:
        cn = cn.replace(old_header_block, new_header_block)
        print(f"Header updated in {filepath}")
    else:
        print(f"Header NOT FOUND in {filepath}")

    # 2. Remove card-header
    if old_card_header in cn:
        cn = cn.replace(old_card_header, '')
        print(f"Card header removed in {filepath}")
    else:
        print(f"Card header NOT FOUND in {filepath}")

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(cn)
