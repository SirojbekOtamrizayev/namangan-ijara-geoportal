files = ['index.html', 'namangan_interaktiv_xarita.html', 'public/namangan_interaktiv_xarita.html']

old_block = """        <!-- SECTORS ROW -->
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
        </div>"""

for filepath in files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    cn = content.replace('\r\n', '\n')
    on = old_block.replace('\r\n', '\n')
    
    if on in cn:
        cn = cn.replace(on, '')
        print(f"Removed from {filepath}")
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(cn)
    else:
        print(f"NOT FOUND in {filepath}")
