files = ['index.html', 'namangan_interaktiv_xarita.html', 'public/namangan_interaktiv_xarita.html']

removals = [
    # 1. Full map view header (portal-tag, h1, accent-bar)
    """  <!-- Header -->
  <header>
    <div class="header-left">

      <div class="header-titles">
        <span class="portal-tag">Namangan viloyati ijara yerlar geoportali</span>
        <h1 class="main-title">NAMANGAN VILOYATI TUMANLARI INTERAKTIV XARITASI</h1>
        <div class="accent-bar"></div>
      </div>
    </div>
    

  </header>""",
    # 2. card-header (xarita sarlavhasi + 12 ta tuman badge)
    """      <div class="card-header">
        <div class="card-title">🗺️ Namangan viloyati xaritasi</div>
        <span class="badge">12 ta tuman va shahar</span>
      </div>"""
]

for filepath in files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    cn = content.replace('\r\n', '\n')
    changed = False
    for old in removals:
        on = old.replace('\r\n', '\n')
        if on in cn:
            cn = cn.replace(on, '')
            changed = True
            print(f"  Removed block from {filepath}")
        else:
            print(f"  NOT FOUND in {filepath}: {old[:60]}")
    
    if changed:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(cn)
