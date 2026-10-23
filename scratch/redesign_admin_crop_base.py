# Script to redesign adminTabCropBase into a modern two-column database workbench with direction categories and auto-sync
import re

files = ['index.html', 'namangan_interaktiv_xarita.html', 'public/namangan_interaktiv_xarita.html']

new_crop_base_html = """    <!-- Body Tab: Crop Database (AI) - Modern Database Management Center -->
    <div class="admin-body" id="adminTabCropBase" style="display: none;">
      <div style="display: flex; flex-direction: column; gap: 14px;">

        <!-- Top Header & Status Toolbar -->
        <div style="background: linear-gradient(135deg, rgba(2, 132, 199, 0.08) 0%, rgba(16, 185, 129, 0.08) 100%); border: 1px solid var(--border); border-radius: 14px; padding: 14px 18px; display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 12px;">
          <div style="display: flex; align-items: center; gap: 12px;">
            <div style="width: 40px; height: 40px; border-radius: 10px; background: #0284c7; color: #fff; display: flex; align-items: center; justify-content: center; font-size: 20px; box-shadow: 0 4px 10px rgba(2, 132, 199, 0.3);">
              🌾
            </div>
            <div>
              <div style="display: flex; align-items: center; gap: 8px;">
                <h3 style="font-size: 15px; font-weight: 800; color: var(--text); margin: 0;">Ekinlar va Agrotexnologiya Ma'lumotlar Bazasi Markazi</h3>
                <span class="badge" id="cropDbCategoryCountBadge" style="background:#0284c7; color:#fff;">Baza faol</span>
              </div>
              <p style="font-size: 11.5px; color: var(--muted); margin: 2px 0 0 0;">
                O'ng tarafdagi yo'nalishlar bo'yicha Excel yuklang — tizim avtomatik <strong>"Hosil olish bo'yicha AI xizmati"</strong> jadvaliga va barcha MFY xaritalariga tortib oladi.
              </p>
            </div>
          </div>

          <div style="display: flex; gap: 8px; flex-wrap: wrap;">
            <button class="d-btn" onclick="downloadCropTemplate()" style="background: var(--inner); border: 1px solid var(--border); font-size: 11.5px; padding: 7px 12px;">
              📥 Shablon (.xlsx)
            </button>
            <button class="d-btn" onclick="syncAndRefreshAllAiViews()" style="background: #10b981; color: #fff; border: none; font-size: 11.5px; padding: 7px 14px; box-shadow: 0 2px 8px rgba(16,185,129,0.3);">
              🔄 AI Xizmatiga Yangilash
            </button>
          </div>
        </div>

        <!-- 2-COLUMN DATABASE WORKBENCH: Left (Live Database Table & Search) / Right (Direction-based Upload Panels) -->
        <div style="display: grid; grid-template-columns: 1.4fr 1fr; gap: 16px;">

          <!-- LEFT: Stored Database Table with category tabs & search -->
          <div style="background: var(--card); border: 1px solid var(--border); border-radius: 14px; padding: 14px; display: flex; flex-direction: column; gap: 10px;">
            <div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 8px;">
              <div style="display: flex; align-items: center; gap: 8px;">
                <span style="font-size: 16px;">📋</span>
                <span style="font-size: 13px; font-weight: 800; color: var(--text);">Joriy Ekinlar Bazasi</span>
                <span class="badge" id="cropDbCount" style="font-size: 10.5px;">0 ta mahsulot</span>
              </div>
              <input type="text" id="adminCropSearchInput" oninput="filterAdminCropDbTable()" placeholder="Ekin nomi bo'yicha..." style="background: var(--inner); border: 1px solid var(--border); border-radius: 8px; padding: 5px 10px; font-size: 11.5px; color: var(--text); outline: none; width: 170px;">
            </div>

            <!-- Category Pills Filter -->
            <div style="display: flex; gap: 5px; flex-wrap: wrap;" id="cropCategoryPills">
              <button class="d-btn active" onclick="filterAdminCropCategory('all', this)" style="font-size: 10.5px; padding: 4px 8px;">Barchasi</button>
              <button class="d-btn" onclick="filterAdminCropCategory('sabzavot', this)" style="font-size: 10.5px; padding: 4px 8px;">Sabzavotlar</button>
              <button class="d-btn" onclick="filterAdminCropCategory('poliz', this)" style="font-size: 10.5px; padding: 4px 8px;">Poliz</button>
              <button class="d-btn" onclick="filterAdminCropCategory('dukkakli', this)" style="font-size: 10.5px; padding: 4px 8px;">Dukkakli</button>
              <button class="d-btn" onclick="filterAdminCropCategory('ildizmeva', this)" style="font-size: 10.5px; padding: 4px 8px;">Ildizmeva</button>
              <button class="d-btn" onclick="filterAdminCropCategory('issiqxona', this)" style="font-size: 10.5px; padding: 4px 8px;">Issiqxona</button>
            </div>

            <!-- Table -->
            <div class="data-table-container" style="max-height: 380px; overflow-y: auto;">
              <table class="admin-table">
                <thead>
                  <tr>
                    <th>#</th>
                    <th>Ekin nomi</th>
                    <th>Navi (sort)</th>
                    <th>1 ga hosil</th>
                    <th>1 ga daromad</th>
                    <th>Narx/kg</th>
                    <th>Taqsimot</th>
                  </tr>
                </thead>
                <tbody id="cropDbTbody"></tbody>
              </table>
            </div>

            <div style="font-size: 10.5px; color: var(--muted); border-top: 1px dashed var(--border); padding-top: 6px; display: flex; justify-content: space-between;">
              <span>⚡ Bazadagi barcha ekinlar <strong>Hosil olish bo'yicha AI xizmati</strong> bo'limida avtomatik tahlil qilinadi</span>
              <a href="javascript:void(0)" onclick="clearCropDatabase()" style="color: #ef4444; font-weight: 700; text-decoration: none;">Bazani tozalash</a>
            </div>
          </div>

          <!-- RIGHT: Direction-based Data Importer (Har bir yo'nalish bo'yicha yuklash) -->
          <div style="background: var(--inner); border: 1px solid var(--border); border-radius: 14px; padding: 14px; display: flex; flex-direction: column; gap: 10px;">
            <div style="display: flex; align-items: center; justify-content: space-between;">
              <span style="font-size: 12.5px; font-weight: 800; color: var(--text);">📂 Yo'nalishlar Bo'yicha Ma'lumot Yuklash</span>
              <span style="font-size: 10px; color: var(--muted);">Excel / CSV</span>
            </div>

            <!-- Direction Selector Cards -->
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 8px;">
              <div onclick="selectUploadDirection('sabzavot', 'Sabzavot ekinlari bazasi', this)" class="upload-dir-card active" style="background:var(--card); border:1.5px solid #0284c7; border-radius:10px; padding:8px 10px; cursor:pointer; display:flex; align-items:center; gap:8px;">
                <span style="font-size: 18px;">🥕</span>
                <div>
                  <div style="font-size: 11px; font-weight: 800; color: var(--text);">Sabzavotchilik</div>
                  <div style="font-size: 9.5px; color: var(--muted);">Sabzi, piyoz, karam, qalampir</div>
                </div>
              </div>

              <div onclick="selectUploadDirection('poliz', 'Poliz ekinlari bazasi', this)" class="upload-dir-card" style="background:var(--card); border:1px solid var(--border); border-radius:10px; padding:8px 10px; cursor:pointer; display:flex; align-items:center; gap:8px;">
                <span style="font-size: 18px;">🍉</span>
                <div>
                  <div style="font-size: 11px; font-weight: 800; color: var(--text);">Polizchilik</div>
                  <div style="font-size: 9.5px; color: var(--muted);">Qovun, tarvuz, qovoq</div>
                </div>
              </div>

              <div onclick="selectUploadDirection('dukkakli', 'Dukkakli ekinlar bazasi', this)" class="upload-dir-card" style="background:var(--card); border:1px solid var(--border); border-radius:10px; padding:8px 10px; cursor:pointer; display:flex; align-items:center; gap:8px;">
                <span style="font-size: 18px;">🌱</span>
                <div>
                  <div style="font-size: 11px; font-weight: 800; color: var(--text);">Dukkaklilar</div>
                  <div style="font-size: 9.5px; color: var(--muted);">Mosh, loviya, no'xat</div>
                </div>
              </div>

              <div onclick="selectUploadDirection('issiqxona', 'Issiqxona va Intensiv ekinlar', this)" class="upload-dir-card" style="background:var(--card); border:1px solid var(--border); border-radius:10px; padding:8px 10px; cursor:pointer; display:flex; align-items:center; gap:8px;">
                <span style="font-size: 18px;">🍋</span>
                <div>
                  <div style="font-size: 11px; font-weight: 800; color: var(--text);">Issiqxona</div>
                  <div style="font-size: 9.5px; color: var(--muted);">Limon, bodring, gullar</div>
                </div>
              </div>
            </div>

            <!-- Active Direction Upload Box -->
            <div style="border: 2px dashed #0284c7; border-radius: 12px; padding: 16px; text-align: center; background: rgba(2, 132, 199, 0.04); display: flex; flex-direction: column; align-items: center; gap: 6px;">
              <input type="file" id="cropExcelInput" accept=".xlsx, .xls, .csv" style="display:none;" onchange="handleCropExcelUpload(event)">
              <div style="font-size: 26px;" id="uploadDirIcon">🥕</div>
              <div style="font-size: 12px; font-weight: 800; color: var(--text);" id="uploadDirTitle">Sabzavot ekinlari bazasini yuklash</div>
              <div style="font-size: 10.5px; color: var(--muted); margin-bottom: 4px;">
                Excel faylni tanlang — ma'lumotlar bazaga qo'shiladi va AI xizmatiga avtomatik uzatiladi
              </div>
              <button type="button" class="admin-submit-btn" style="background: #0284c7; padding: 8px 16px; font-size: 11.5px;" onclick="document.getElementById('cropExcelInput').click()">
                📂 Faylni tanlash (.xlsx)...
              </button>
            </div>

            <!-- Preview Table Inside Admin -->
            <div id="cropPreviewSection" style="display:none; flex-direction:column; gap:8px;">
              <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:6px;">
                <span style="font-size:12px; font-weight:800; color:var(--text);" id="cropPreviewTitle">O'qilgan: 0 ta</span>
                <button class="admin-submit-btn" onclick="confirmCropImport()" style="background:#059669; padding:6px 12px; font-size:11.5px;">
                  ✅ Bazaga Saqlash va AI ga Tortish
                </button>
              </div>

              <div class="data-table-container" style="max-height:160px; overflow-y:auto;">
                <table class="admin-table">
                  <thead>
                    <tr>
                      <th>#</th>
                      <th>Mahsulot</th>
                      <th>Nav</th>
                      <th>1 ga hosil</th>
                      <th>1 ga daromad</th>
                      <th>Narx</th>
                    </tr>
                  </thead>
                  <tbody id="cropPreviewTbody"></tbody>
                </table>
              </div>
            </div>

            <!-- Auto-Sync Status Bar -->
            <div style="background: var(--card); border: 1px solid var(--border); border-radius: 10px; padding: 8px 10px; font-size: 11px; display: flex; align-items: center; gap: 8px; color: var(--text);">
              <span style="color: #10b981; font-size: 14px;">⚡</span>
              <div>
                <strong>Avtomatik sinxronizatsiya:</strong> Bazaga saqlangan har bir jadval to'g'ridan-to'g'ri <em>"Hosil olish bo'yicha AI xizmati"</em> jadvalini to'ldiradi.
              </div>
            </div>

          </div>

        </div>

      </div>
    </div>
"""

# Helper JavaScript functions to inject
js_helpers = """
  /* Direction upload selection */
  let currentUploadDirection = 'sabzavot';

  function selectUploadDirection(dirKey, dirTitle, el) {
    currentUploadDirection = dirKey;
    document.querySelectorAll('.upload-dir-card').forEach(c => {
      c.classList.remove('active');
      c.style.borderColor = 'var(--border)';
    });
    if (el) {
      el.classList.add('active');
      el.style.borderColor = '#0284c7';
    }
    const titleEl = document.getElementById('uploadDirTitle');
    const iconEl = document.getElementById('uploadDirIcon');
    if (titleEl) titleEl.textContent = dirTitle + ' yuklash';
    
    const icons = {
      'sabzavot': '🥕',
      'poliz': '🍉',
      'dukkakli': '🌱',
      'issiqxona': '🍋'
    };
    if (iconEl) iconEl.textContent = icons[dirKey] || '🌾';
  }

  function filterAdminCropCategory(catKey, btn) {
    document.querySelectorAll('#cropCategoryPills .d-btn').forEach(b => b.classList.remove('active'));
    if (btn) btn.classList.add('active');

    const tbody = document.getElementById('cropDbTbody');
    if (!tbody) return;

    if (catKey === 'all') {
      refreshCropDbTable();
      return;
    }

    const filtered = cropDatabase.filter(c => {
      const name = (c.name || '').toLowerCase();
      if (catKey === 'sabzavot') return name.includes('sabzi') || name.includes('piyoz') || name.includes('karam') || name.includes('qalampir') || name.includes('pomidor') || name.includes('bodring');
      if (catKey === 'poliz') return name.includes('qovun') || name.includes('tarvuz') || name.includes('poliz') || name.includes('qovoq');
      if (catKey === 'dukkakli') return name.includes('mosh') || name.includes('loviya') || name.includes('no\'xat') || name.includes('fasol');
      if (catKey === 'ildizmeva') return name.includes('sabzi') || name.includes('turp') || name.includes('shalg') || name.includes('lavlagi');
      if (catKey === 'issiqxona') return name.includes('issiqxona') || name.includes('limon') || name.includes('gul') || name.includes('pomidor');
      return true;
    });

    renderAdminFilteredCrops(filtered);
  }

  function renderAdminFilteredCrops(list) {
    const tbody = document.getElementById('cropDbTbody');
    if (!tbody) return;
    tbody.innerHTML = '';
    if (list.length === 0) {
      tbody.innerHTML = '<tr><td colspan="7" style="text-align:center; color:var(--muted); padding:16px;">Ushbu yo\\'nalishda ekinlar topilmadi.</td></tr>';
      return;
    }
    list.forEach((c, idx) => {
      const fmtIncome = c.haIncome ? (c.haIncome / 1000000).toFixed(1) + ' mln' : '-';
      const fmtPrice = c.price ? c.price.toLocaleString() + " so'm" : '-';
      const mfyList = c.assignedMfys && c.assignedMfys.length > 0 ? c.assignedMfys.slice(0, 2).join(', ') : 'Taqsimlanmagan';
      const tr = document.createElement('tr');
      tr.innerHTML = `
        <td>${idx + 1}</td>
        <td><strong>${c.name}</strong></td>
        <td>${c.sort || '-'}</td>
        <td>${c.haYield || '-'} t</td>
        <td>${fmtIncome}</td>
        <td>${fmtPrice}</td>
        <td><span style="font-size:10px; color:var(--muted);">${mfyList}</span></td>
      `;
      tbody.appendChild(tr);
    });
  }

  function filterAdminCropDbTable() {
    const q = (document.getElementById('adminCropSearchInput')?.value || '').toLowerCase();
    const filtered = cropDatabase.filter(c => (c.name || '').toLowerCase().includes(q) || (c.sort || '').toLowerCase().includes(q));
    renderAdminFilteredCrops(filtered);
  }

  function syncAndRefreshAllAiViews() {
    if (typeof initAiServiceView === 'function') {
      initAiServiceView();
    }
    refreshCropDbTable();
    alert("✅ Baza muvaffaqiyatli 'Hosil olish bo\\'yicha AI xizmati' bo'limi bilan sinxronlashtirildi!");
  }

  function clearCropDatabase() {
    if (confirm("Haqiqatan ham ekinlar bazasini tozalamoqchimisiz?")) {
      cropDatabase = [];
      try {
        localStorage.removeItem('namangan_crop_database');
      } catch(e) {}
      refreshCropDbTable();
      if (typeof initAiServiceView === 'function') {
        initAiServiceView();
      }
      alert("Baza tozalandi. Standart tavsiyalar tiklandi.");
    }
  }
"""

for filepath in files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    cn = content.replace('\r\n', '\n')

    # Replace <div class="admin-body" id="adminTabCropBase"... up to <!-- Body Tab 3: Security
    tab_start = cn.find('<div class="admin-body" id="adminTabCropBase"')
    tab_end = cn.find('<!-- Body Tab 3: Security')
    
    if tab_start != -1 and tab_end != -1:
        cn = cn[:tab_start] + new_crop_base_html + '\n    ' + cn[tab_end:]
        print(f"adminTabCropBase redesigned in {filepath}")
    else:
        print(f"Could not find tab boundaries in {filepath}")

    # Inject js_helpers before </script>\n</body> if not present
    if 'selectUploadDirection' not in cn:
        cn = cn.replace('</script>\n</body>', js_helpers + '\n</script>\n</body>')
        print(f"js_helpers injected in {filepath}")

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(cn)

print("All done!")
