files = ['index.html', 'namangan_interaktiv_xarita.html', 'public/namangan_interaktiv_xarita.html']

# 1. Old buttons block in View 3 Header
old_header_buttons = """          <div style="display: flex; gap: 10px; flex-wrap: wrap;">
            <button class="d-btn" onclick="downloadCropTemplate()" style="background: rgba(255,255,255,0.2); color: #fff; border: 1px solid rgba(255,255,255,0.35); padding: 9px 16px; font-size: 12.5px; backdrop-filter: blur(8px);">
              📥 Excel shablonini olish
            </button>
            <button class="d-btn" onclick="document.getElementById('aiViewExcelInput').click()" style="background: #10b981; color: #fff; border: none; padding: 9px 18px; font-size: 12.5px; box-shadow: 0 4px 12px rgba(16,185,129,0.35);">
              📤 Yangi jadval yuklash
            </button>
            <input type="file" id="aiViewExcelInput" accept=".xlsx, .xls, .csv" style="display:none;" onchange="handleAiViewExcelUpload(event)">
          </div>"""

# 2. Old banner below table in View 3
old_table_bottom_banner = """              <!-- Quick Upload banner below table -->
              <div style="margin-top: 14px; border: 1.5px dashed rgba(2, 132, 199, 0.4); border-radius: 12px; padding: 12px 16px; background: rgba(2, 132, 199, 0.03); display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 10px;">
                <div style="display: flex; align-items: center; gap: 10px;">
                  <span style="font-size: 22px;">📁</span>
                  <div>
                    <div style="font-size: 12px; font-weight: 800; color: var(--text);">Yangi ma'lumotlar bazasini yuklash (Excel / CSV)</div>
                    <div style="font-size: 11px; color: var(--muted);">Yangi fayl yuklasangiz, ushbu jadval va AI tahlili avtomatik yangilanadi</div>
                  </div>
                </div>
                <button onclick="document.getElementById('aiViewExcelInput').click()" class="action-link-btn" style="padding: 6px 14px;">
                  Fayl tanlash
                </button>
              </div>"""

# 3. Enhanced confirmCropImport to update currentAiCrops & sync View 3 immediately
old_confirm_crop = """    // Save crop database
    try {
      localStorage.setItem('namangan_crop_database', JSON.stringify(cropDatabase));
    } catch(e) { console.warn('Crop DB save error:', e); }

    // Run AI distribution
    runAiDistribution();

    alert(`🎉 ${cropDatabase.length} ta ekin muvaffaqiyatli bazaga saqlandi va AI taqsimlash bajarildi!`);

    document.getElementById('cropExcelInput').value = '';
    document.getElementById('cropPreviewSection').style.display = 'none';"""

new_confirm_crop = """    // Save crop database
    try {
      localStorage.setItem('namangan_crop_database', JSON.stringify(cropDatabase));
    } catch(e) { console.warn('Crop DB save error:', e); }

    // Synchronize into 'Hosil olish bo\\'yicha AI xizmati'
    if (typeof initAiServiceView === 'function') {
      initAiServiceView();
    }

    // Run AI distribution across MFYs
    runAiDistribution();

    alert(`🎉 ${cropDatabase.length} ta ekin muvaffaqiyatli bazaga saqlandi! Ushbu ma'lumotlar 'Hosil olish bo\\'yicha AI xizmati' jadvalida va MFY xaritalarida avtomatik aks ettirildi.`);

    document.getElementById('cropExcelInput').value = '';
    document.getElementById('cropPreviewSection').style.display = 'none';"""

for filepath in files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    cn = content.replace('\r\n', '\n')

    # Remove header buttons
    if old_header_buttons.replace('\r\n', '\n') in cn:
        cn = cn.replace(old_header_buttons.replace('\r\n', '\n'), '')
        print(f"Header buttons removed from {filepath}")
    else:
        print(f"Header buttons NOT found in {filepath}")

    # Remove table bottom banner
    if old_table_bottom_banner.replace('\r\n', '\n') in cn:
        cn = cn.replace(old_table_bottom_banner.replace('\r\n', '\n'), '')
        print(f"Table bottom banner removed from {filepath}")
    else:
        print(f"Table bottom banner NOT found in {filepath}")

    # Enhance confirmCropImport
    if old_confirm_crop.replace('\r\n', '\n') in cn:
        cn = cn.replace(old_confirm_crop.replace('\r\n', '\n'), new_confirm_crop)
        print(f"confirmCropImport synced in {filepath}")
    else:
        print(f"confirmCropImport NOT found in {filepath}")

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(cn)

print("Finished applying updates!")
