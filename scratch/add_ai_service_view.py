# Python script to build the "Hosil olish bo'yicha AI xizmati" view into index.html, namangan_interaktiv_xarita.html, and public/namangan_interaktiv_xarita.html

import re

# 1. New View HTML Definition
new_view_html = '''
      <!-- VIEW 3: HOSIL OLISH BO'YICHA AI XIZMATI -->
      <section id="viewAiService" class="view-container">
        
        <!-- Header banner -->
        <div style="background: linear-gradient(135deg, #0284c7 0%, #0369a1 50%, #0f172a 100%); border-radius: 18px; padding: 22px 28px; color: #fff; box-shadow: var(--card-shadow); display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 16px;">
          <div>
            <div style="display: inline-flex; align-items: center; gap: 8px; background: rgba(255,255,255,0.15); padding: 4px 12px; border-radius: 99px; font-size: 11.5px; font-weight: 800; text-transform: uppercase; letter-spacing: 0.08em; margin-bottom: 8px;">
              <span>🤖</span> Aqlli Agrotexnologik AI Platforma
            </div>
            <h2 style="font-size: 22px; font-weight: 900; margin: 0; line-height: 1.2;">Hosil olish bo'yicha AI xizmati</h2>
            <p style="font-size: 13px; color: #e0f2fe; margin: 6px 0 0 0; max-width: 650px;">
              Qishloq xo'jaligi va ijara yerlari uchun ekinlar ma'lumotlar bazasi, sarf-xarajatlar (rasxod), kutilayotgan hosildorlik hamda sof daromadni interaktiv tahlil qiluvchi sun'iy intellekt xizmati.
            </p>
          </div>
          <div style="display: flex; gap: 10px; flex-wrap: wrap;">
            <button class="d-btn" onclick="downloadCropTemplate()" style="background: rgba(255,255,255,0.2); color: #fff; border: 1px solid rgba(255,255,255,0.35); padding: 9px 16px; font-size: 12.5px; backdrop-filter: blur(8px);">
              📥 Excel shablonini olish
            </button>
            <button class="d-btn" onclick="document.getElementById('aiViewExcelInput').click()" style="background: #10b981; color: #fff; border: none; padding: 9px 18px; font-size: 12.5px; box-shadow: 0 4px 12px rgba(16,185,129,0.35);">
              📤 Yangi jadval yuklash
            </button>
            <input type="file" id="aiViewExcelInput" accept=".xlsx, .xls, .csv" style="display:none;" onchange="handleAiViewExcelUpload(event)">
          </div>
        </div>

        <!-- 4 Stat Metric Cards -->
        <div class="kpi-row" style="grid-template-columns: repeat(4, 1fr);">
          <div class="kpi-card">
            <div class="kpi-title-row">
              <span class="kpi-icon">🌾</span>
              <span>Bazadagi ekin turlari</span>
            </div>
            <div class="kpi-numbers">
              <div class="kpi-col">
                <span class="kpi-lbl">Jami ekinlar</span>
                <span class="kpi-val primary" id="aiTotalCropsCount">8 ta</span>
              </div>
            </div>
            <div class="kpi-footer">
              <span>Sabzavot, poliz, dukkakli</span>
            </div>
          </div>

          <div class="kpi-card">
            <div class="kpi-title-row">
              <span class="kpi-icon">💰</span>
              <span>O'rtacha daromad (1 ga)</span>
            </div>
            <div class="kpi-numbers">
              <div class="kpi-col">
                <span class="kpi-lbl">Gektariga sof foyda</span>
                <span class="kpi-val emerald" id="aiAvgIncomeVal">72.5 mln</span>
              </div>
            </div>
            <div class="kpi-footer">
              <span>Eng yuqori: 150 mln so'm</span>
            </div>
          </div>

          <div class="kpi-card">
            <div class="kpi-title-row">
              <span class="kpi-icon">🚜</span>
              <span>O'rtacha xarajat (rasxod)</span>
            </div>
            <div class="kpi-numbers">
              <div class="kpi-col">
                <span class="kpi-lbl">1 ga urug'+o'g'it+suv</span>
                <span class="kpi-val amber" id="aiAvgExpenseVal">16.8 mln</span>
              </div>
            </div>
            <div class="kpi-footer">
              <span>Rentabellik: 320% - 450%</span>
            </div>
          </div>

          <div class="kpi-card">
            <div class="kpi-title-row">
              <span class="kpi-icon">⚡</span>
              <span>AI Tavsiya aniqligi</span>
            </div>
            <div class="kpi-numbers">
              <div class="kpi-col">
                <span class="kpi-lbl">Bonitet & iqlim mosligi</span>
                <span class="kpi-val primary">96.4%</span>
              </div>
            </div>
            <div class="kpi-footer">
              <span>Namangan 12 hududi bo'yicha</span>
            </div>
          </div>
        </div>

        <!-- MAIN 2-COLUMN LAYOUT: Left (Interactive Table & DB) / Right (AI Advisor Chat & Simulator) -->
        <div style="display: grid; grid-template-columns: 1.4fr 1fr; gap: 20px;">

          <!-- LEFT COLUMN: Crop Database Table with Filter & Upload -->
          <div style="display: flex; flex-direction: column; gap: 16px;">
            
            <div class="districts-table-card" style="padding: 20px;">
              <div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 12px; margin-bottom: 6px;">
                <div style="display: flex; align-items: center; gap: 10px;">
                  <span style="font-size: 20px;">📊</span>
                  <div>
                    <h3 style="font-size: 15px; font-weight: 800; color: var(--text); margin: 0;">Ekinlar va Iqtisodiy Ko'rsatkichlar Bazasi</h3>
                    <p style="font-size: 11.5px; color: var(--muted); margin: 2px 0 0 0;">Jadvaldagi istalgan ekin ustiga bosing — AI uning rasxodi, hosili va foydasini tahlil qiladi</p>
                  </div>
                </div>

                <div style="display: flex; align-items: center; gap: 8px;">
                  <input type="text" id="aiCropSearchInput" oninput="filterAiCropsTable()" placeholder="Ekin nomini qidirish..." style="background: var(--inner); border: 1px solid var(--border); border-radius: 8px; padding: 6px 12px; font-size: 12px; color: var(--text); outline: none;">
                </div>
              </div>

              <!-- Data table -->
              <div class="table-responsive" style="max-height: 480px; overflow-y: auto;">
                <table class="gov-table" id="aiCropsGovTable">
                  <thead>
                    <tr>
                      <th>Ekin nomi</th>
                      <th>Navi (sort)</th>
                      <th>1 ga hosildorlik</th>
                      <th>Kutilayotgan daromad</th>
                      <th>10/50 sotix daromad</th>
                      <th>Bozor narxi (kg)</th>
                      <th>AI Tahlil</th>
                    </tr>
                  </thead>
                  <tbody id="aiCropsTableBody">
                    <!-- Dynamically rendered -->
                  </tbody>
                </table>
              </div>

              <!-- Quick Upload banner below table -->
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
              </div>
            </div>

          </div>

          <!-- RIGHT COLUMN: AI MASLAHAT VA TAHLIL OYNACHASI (Interactive AI Agro Advisor) -->
          <div style="display: flex; flex-direction: column; gap: 16px;">
            
            <!-- AI Advisor Panel -->
            <div style="background: var(--card); border: 1px solid var(--border); border-radius: 18px; padding: 20px; box-shadow: var(--card-shadow); display: flex; flex-direction: column; gap: 14px;">
              
              <!-- AI Box Header -->
              <div style="display: flex; align-items: center; justify-content: space-between; border-bottom: 1px solid var(--border); padding-bottom: 12px;">
                <div style="display: flex; align-items: center; gap: 10px;">
                  <div style="width: 36px; height: 36px; border-radius: 10px; background: linear-gradient(135deg, #10b981 0%, #0284c7 100%); display: flex; align-items: center; justify-content: center; font-size: 20px; box-shadow: 0 4px 10px rgba(16,185,129,0.3);">
                    🤖
                  </div>
                  <div>
                    <div style="font-size: 14px; font-weight: 800; color: var(--text); display: flex; align-items: center; gap: 6px;">
                      <span>AI Agromaslahatchi</span>
                      <span style="background: #ecfdf5; color: #047857; font-size: 10px; font-weight: 800; padding: 2px 7px; border-radius: 99px; border: 1px solid rgba(16,185,129,0.3);">Online</span>
                    </div>
                    <div style="font-size: 11px; color: var(--muted);">Namangan iqlimi va tuproq boniteti tahlili</div>
                  </div>
                </div>
                <button class="d-btn" onclick="resetAiConsultant()" style="font-size: 11px; padding: 4px 8px;" title="Tahlilni yangilash">
                  🔄 Qayta hisoblash
                </button>
              </div>

              <!-- Interactive Simulator Inputs -->
              <div style="background: var(--inner); border: 1px solid var(--border); border-radius: 14px; padding: 14px; display: flex; flex-direction: column; gap: 10px;">
                <div style="font-size: 11.5px; font-weight: 800; color: var(--text-sub); text-transform: uppercase; letter-spacing: 0.04em;">
                  ⚡ Tezkor AI Simulyator (Hosil & Xarajat)
                </div>

                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 8px;">
                  <div>
                    <label style="font-size: 10.5px; font-weight: 700; color: var(--muted); display: block; margin-bottom: 3px;">Ekin turini tanlang:</label>
                    <select id="aiSimCropSelect" onchange="runAiCropAnalysis()" class="topbar-select" style="width: 100%;">
                      <!-- Populated dynamically -->
                    </select>
                  </div>
                  <div>
                    <label style="font-size: 10.5px; font-weight: 700; color: var(--muted); display: block; margin-bottom: 3px;">Yer maydoni:</label>
                    <select id="aiSimAreaSelect" onchange="runAiCropAnalysis()" class="topbar-select" style="width: 100%;">
                      <option value="0.1">10 sotix (0.1 ga)</option>
                      <option value="0.15">15 sotix (0.15 ga)</option>
                      <option value="0.5" selected>50 sotix (0.5 ga - standart ijara)</option>
                      <option value="1.0">1 gektar (1.0 ga)</option>
                      <option value="2.0">2 gektar (2.0 ga)</option>
                      <option value="5.0">5 gektar (5.0 ga)</option>
                    </select>
                  </div>
                </div>

                <div>
                  <label style="font-size: 10.5px; font-weight: 700; color: var(--muted); display: block; margin-bottom: 3px;">Tuman/Hudud tanlang:</label>
                  <select id="aiSimDistrictSelect" onchange="runAiCropAnalysis()" class="topbar-select" style="width: 100%;">
                    <option value="pop">Pop tumani (Qumloq-bo'z tuproq, bonitet: 64)</option>
                    <option value="chust">Chust tumani (Qalampir & Sabzi, bonitet: 68)</option>
                    <option value="mingbuloq">Mingbuloq tumani (Poliz & Dukkakli, bonitet: 66)</option>
                    <option value="toraqorgon">To'raqo'rg'on tumani (Sabzavotchilik, bonitet: 72)</option>
                    <option value="kosonsoy">Kosonsoy tumani (Bog'dorchilik & Sabzi, bonitet: 67)</option>
                    <option value="yangiqorgon">Yangiqo'rg'on tumani (Kartoshkachilik, bonitet: 70)</option>
                    <option value="chortoq">Chortoq tumani (Meva & Gilos, bonitet: 69)</option>
                    <option value="uychi">Uychi tumani (Uch faslli sabzavot, bonitet: 73)</option>
                    <option value="uchqorgon">Uchqo'rg'on tumani (Sholi & Mevalar, bonitet: 74)</option>
                    <option value="norin">Norin tumani (Piyoz & Sabzavot, bonitet: 71)</option>
                    <option value="namangan-tumani">Namangan tumani (Ko'chatchilik, bonitet: 72)</option>
                    <option value="namangan-shahri">Namangan shahri (Issiqxona & Gullar, bonitet: 75)</option>
                  </select>
                </div>
              </div>

              <!-- AI Analysis Output Box -->
              <div id="aiAdvisorOutput" style="background: linear-gradient(135deg, rgba(2, 132, 199, 0.05) 0%, rgba(16, 185, 129, 0.05) 100%); border: 1.5px solid rgba(2, 132, 199, 0.25); border-radius: 14px; padding: 16px; display: flex; flex-direction: column; gap: 12px;">
                <!-- Populated by JS runAiCropAnalysis -->
              </div>

              <!-- AI Agromaslahatchiga savol berish (Quick Chat) -->
              <div style="display: flex; flex-direction: column; gap: 8px;">
                <label style="font-size: 11px; font-weight: 800; color: var(--text-sub);">💬 AI Agromaslahatchiga erkin savol bering:</label>
                <div style="display: flex; gap: 8px;">
                  <input type="text" id="aiCustomQuestionInput" placeholder="Masalan: 50 sotixga nima eksam ko'p foyda olaman?" style="flex: 1; background: var(--inner); border: 1px solid var(--border); border-radius: 10px; padding: 8px 12px; font-size: 12px; color: var(--text); outline: none;" onkeydown="if(event.key==='Enter') sendAiQuestion()">
                  <button class="topbar-update-btn" onclick="sendAiQuestion()" style="padding: 8px 14px; border-radius: 10px;">
                    Yuborish ➔
                  </button>
                </div>
                <div id="aiQuickAnswersBox" style="display: none; background: var(--inner); border: 1px solid var(--border); border-radius: 10px; padding: 10px 12px; font-size: 12px; line-height: 1.5; color: var(--text);">
                </div>
              </div>

            </div>

          </div>

        </div>

      </section>
'''

# 2. JS Code for the AI Service view
new_view_js = '''
  /* ========================================================= */
  /*   VIEW 3: HOSIL OLISH BO'YICHA AI XIZMATI LOGIKASI       */
  /* ========================================================= */

  // Standart bazaviy ekinlar (agar foydalanuvchi hali Excel yuklamagan bo'lsa)
  const defaultAiCrops = [
    {
      id: 'crop-1',
      name: "Eksportbop Mosh (Radost)",
      category: "Dukkakli",
      sort: "Navro'z / Radost",
      haYield: 2.8, // tonna
      haExpense: 8500000, // so'm (rasxod)
      pricePerKg: 14000, // so'm
      haIncome: 39200000,
      haNetProfit: 30700000,
      vegetationDays: 85,
      waterNeed: "Kam suv talab qiladi (2 marta sug'orish)",
      bestSoils: ["Qumloq", "Bo'z tuproq", "Adir yerlar"],
      aiPros: "Qisqa muddatda pishadi, tuproqni azot bilan boyitadi, eksport talabi juda yuqori."
    },
    {
      id: 'crop-2',
      name: "Ertapishar Qizil Sabzi",
      category: "Sabzavot",
      sort: "Kaskad F1 / Qizil Nur",
      haYield: 35.0,
      haExpense: 14000000,
      pricePerKg: 2500,
      haIncome: 87500000,
      haNetProfit: 73500000,
      vegetationDays: 95,
      waterNeed: "Mo'tadil sug'orish talab qiladi",
      bestSoils: ["Yumshoq bo'z", "Qumloq unumdor tuproq"],
      aiPros: "Bahorgi va yozgi ikki hosil olish imkoni, barqaror ichki va tashqi bozor narxi."
    },
    {
      id: 'crop-3',
      name: "Poliz (Eksportbop Qovun va Tarvuz)",
      category: "Poliz",
      sort: "Mirzacho'l / Torpedo / Krimin",
      haYield: 32.0,
      haExpense: 11500000,
      pricePerKg: 2200,
      haIncome: 70400000,
      haNetProfit: 58900000,
      vegetationDays: 80,
      waterNeed: "Dastlabki vegetatsiyada suv kerak, pishishda to'xtatiladi",
      bestSoils: ["Qumloq", "Issiq quyoshli yerlar"],
      aiPros: "Pop va Mingbuloq iqlimiga 100% mos, 50 sotixdan kamida 25-30 mln so'm sof foyda beradi."
    },
    {
      id: 'crop-4',
      name: "Chust Achchiq Qalampiri",
      category: "Sabzavot",
      sort: "Chustiy 1 / Uchqun",
      haYield: 18.0,
      haExpense: 16000000,
      pricePerKg: 6500,
      haIncome: 117000000,
      haNetProfit: 101000000,
      vegetationDays: 120,
      waterNeed: "Doimiy namlik zarur (tomchilatib)",
      bestSoils: ["Bo'z tuproq", "Gilli unumdor tuproq"],
      aiPros: "Brend mahsulot, quritib ham sotish mumkin, eksportyorlar to'g'ridan-to'g'ri daladan sotib oladi."
    },
    {
      id: 'crop-5',
      name: "Kuzgi Sarimsoqpiyoz (Chesnok)",
      category: "Sabzavot",
      sort: "Yubiley Gribovskiy",
      haYield: 12.0,
      haExpense: 18000000,
      pricePerKg: 12000,
      haIncome: 144000000,
      haNetProfit: 126000000,
      vegetationDays: 210,
      waterNeed: "Bahorda 2-3 marta sug'oriladi",
      bestSoils: ["Unumdor engil tuproq", "Begona o'tsiz"],
      aiPros: "Eng yuqori rentabelli ekinlardan biri, erta bahorda bozorga birinchi chiqadi."
    },
    {
      id: 'crop-6',
      name: "Yangicha Karam (May Kvin F1)",
      category: "Sabzavot",
      sort: "May Kvin F1 / Gibrid",
      haYield: 38.0,
      haExpense: 15000000,
      pricePerKg: 3000,
      haIncome: 114000000,
      haNetProfit: 99000000,
      vegetationDays: 65,
      waterNeed: "Ko'p suv talab qiladi",
      bestSoils: ["Sug'oriladigan tipik bo'z tuproq"],
      aiPros: "Tezpishar, bir mavsumda 2 martagacha ekish mumkin."
    },
    {
      id: 'crop-7',
      name: "Nanay Kartoshkasi",
      category: "Ildizmeva",
      sort: "Sante / Arizona",
      haYield: 28.0,
      haExpense: 22000000,
      pricePerKg: 4200,
      haIncome: 117600000,
      haNetProfit: 95600000,
      vegetationDays: 90,
      waterNeed: "Mo'tadil, toshqin suvsiz",
      bestSoils: ["Tog' oldi va adir maydonlari, Yangiqo'rg'on"],
      aiPros: "Yuqori kraxmallik, shirin ta'm, talab yil bo'yi barqaror yuqori."
    },
    {
      id: 'crop-8',
      name: "Limonariya va Issiqxona Bodringi",
      category: "Issiqxona",
      sort: "Meva / Orzu F1",
      haYield: 24.0,
      haExpense: 25000000,
      pricePerKg: 7000,
      haIncome: 168000000,
      haNetProfit: 143000000,
      vegetationDays: 75,
      waterNeed: "Tomchilatib sug'orish",
      bestSoils: ["Gumusi boy engil tuproq"],
      aiPros: "Davlatobod va Namangan shahri MFYlari uchun 10 sotixdan 30-40 mln sof foyda beradi."
    }
  ];

  let currentAiCrops = [];

  function initAiServiceView() {
    // Check if custom cropDatabase exists in localStorage
    try {
      const saved = localStorage.getItem('namangan_crop_database');
      if (saved) {
        const parsed = JSON.parse(saved);
        if (Array.isArray(parsed) && parsed.length > 0) {
          // Map user imported crops
          currentAiCrops = parsed.map((c, i) => ({
            id: c.id || ('crop-' + (i+1)),
            name: c.name || c['Mahsulot nomi'] || 'Ekin ' + (i+1),
            category: c.categories ? c.categories[0] : 'Qishloq xo\'jaligi',
            sort: c.sort || c.newCropName || 'Mahalliy / Gibrid',
            haYield: parseFloat(c.haYield) || 20,
            haExpense: (parseFloat(c.haIncome) || 50000000) * 0.25, // estimate 25% rasxod
            pricePerKg: parseFloat(c.price) || 3000,
            haIncome: parseFloat(c.haIncome) || 50000000,
            haNetProfit: (parseFloat(c.haIncome) || 50000000) * 0.75,
            vegetationDays: 80,
            waterNeed: "Me'yorda sug'orish",
            bestSoils: ["Unumdor bo'z tuproq"],
            aiPros: c.rationale || "AI hisob-kitobiga ko'ra Namangan viloyati tuproq bonitetiga to'liq mos keladi."
          }));
        }
      }
    } catch(e) { console.warn(e); }

    if (currentAiCrops.length === 0) {
      currentAiCrops = [...defaultAiCrops];
    }

    renderAiCropsTable(currentAiCrops);
    populateAiCropSelect(currentAiCrops);
    runAiCropAnalysis();
  }

  function renderAiCropsTable(crops) {
    const tbody = document.getElementById('aiCropsTableBody');
    if (!tbody) return;
    tbody.innerHTML = '';

    const countEl = document.getElementById('aiTotalCropsCount');
    if (countEl) countEl.textContent = crops.length + ' ta';

    crops.forEach((c, idx) => {
      const tr = document.createElement('tr');
      tr.style.cursor = 'pointer';
      tr.onclick = () => selectCropForAiSim(c.id);

      const incomeFmt = (c.haIncome / 1000000).toFixed(1) + " mln";
      const s10Fmt = ((c.haIncome * 0.1) / 1000000).toFixed(1) + " / " + ((c.haIncome * 0.5) / 1000000).toFixed(1) + " mln";
      const priceFmt = (c.pricePerKg || 3000).toLocaleString() + " so'm";

      tr.innerHTML = `
        <td>
          <div style="display:flex; align-items:center; gap:8px;">
            <span style="font-size:16px;">🌱</span>
            <div>
              <strong style="color:var(--text); font-size:12.5px;">${c.name}</strong>
              <div style="font-size:10px; color:var(--muted);">${c.category || 'Ekin'}</div>
            </div>
          </div>
        </td>
        <td><span class="badge" style="background:var(--inner); border:1px solid var(--border); font-size:11px;">${c.sort}</span></td>
        <td><strong style="color:#0284c7;">${c.haYield} tonna</strong></td>
        <td><strong style="color:#059669;">${incomeFmt}</strong></td>
        <td><span style="color:#d97706; font-weight:700;">${s10Fmt}</span></td>
        <td>${priceFmt}</td>
        <td>
          <button class="action-link-btn" onclick="event.stopPropagation(); selectCropForAiSim('${c.id}')">
            ⚡ AI Tahlil
          </button>
        </td>
      `;
      tbody.appendChild(tr);
    });
  }

  function populateAiCropSelect(crops) {
    const sel = document.getElementById('aiSimCropSelect');
    if (!sel) return;
    sel.innerHTML = '';
    crops.forEach(c => {
      const opt = document.createElement('option');
      opt.value = c.id;
      opt.textContent = `${c.name} (${c.sort})`;
      sel.appendChild(opt);
    });
  }

  function filterAiCropsTable() {
    const query = (document.getElementById('aiCropSearchInput')?.value || '').toLowerCase();
    const filtered = currentAiCrops.filter(c => 
      c.name.toLowerCase().includes(query) || 
      (c.sort && c.sort.toLowerCase().includes(query)) ||
      (c.category && c.category.toLowerCase().includes(query))
    );
    renderAiCropsTable(filtered);
  }

  function selectCropForAiSim(cropId) {
    const sel = document.getElementById('aiSimCropSelect');
    if (sel) {
      sel.value = cropId;
      runAiCropAnalysis();
    }
  }

  function runAiCropAnalysis() {
    const cropId = document.getElementById('aiSimCropSelect')?.value;
    const area = parseFloat(document.getElementById('aiSimAreaSelect')?.value || '0.5');
    const districtKey = document.getElementById('aiSimDistrictSelect')?.value || 'pop';
    const output = document.getElementById('aiAdvisorOutput');
    if (!output) return;

    const crop = currentAiCrops.find(c => c.id === cropId) || currentAiCrops[0];
    if (!crop) return;

    // District metadata
    const distNames = {
      'pop': "Pop tumani (64 ball)",
      'chust': "Chust tumani (68 ball)",
      'mingbuloq': "Mingbuloq tumani (66 ball)",
      'toraqorgon': "To'raqo'rg'on tumani (72 ball)",
      'kosonsoy': "Kosonsoy tumani (67 ball)",
      'yangiqorgon': "Yangiqo'rg'on tumani (70 ball)",
      'chortoq': "Chortoq tumani (69 ball)",
      'uychi': "Uychi tumani (73 ball)",
      'uchqorgon': "Uchqo'rg'on tumani (74 ball)",
      'norin': "Norin tumani (71 ball)",
      'namangan-tumani': "Namangan tumani (72 ball)",
      'namangan-shahri': "Namangan shahri (75 ball)"
    };

    // Calculations based on chosen area
    const totalYieldTons = (crop.haYield * area).toFixed(1);
    const totalExpense = Math.round(crop.haExpense * area);
    const totalGrossIncome = Math.round(crop.haIncome * area);
    const totalNetProfit = Math.round(totalGrossIncome - totalExpense);
    const rentability = Math.round((totalNetProfit / (totalExpense || 1)) * 100);

    const expenseMln = (totalExpense / 1000000).toFixed(1);
    const incomeMln = (totalGrossIncome / 1000000).toFixed(1);
    const profitMln = (totalNetProfit / 1000000).toFixed(1);

    output.innerHTML = `
      <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid rgba(2,132,199,0.2); padding-bottom:8px;">
        <span style="font-size:13.5px; font-weight:900; color:var(--text);">🌱 ${crop.name}</span>
        <span class="badge" style="background:#0284c7; color:#fff; font-weight:800;">${area >= 1 ? area + ' ga' : (area * 100) + ' sotix'}</span>
      </div>

      <!-- Financial breakdown cards -->
      <div style="display:grid; grid-template-columns:repeat(3, 1fr); gap:8px;">
        <div style="background:var(--card); border:1px solid var(--border); border-radius:10px; padding:8px 10px; text-align:center;">
          <div style="font-size:10px; color:var(--muted); font-weight:700; text-transform:uppercase;">Kutilayotgan Hosil</div>
          <div style="font-size:15px; font-weight:900; color:#0284c7; margin-top:2px;">${totalYieldTons} tonna</div>
        </div>

        <div style="background:var(--card); border:1px solid var(--border); border-radius:10px; padding:8px 10px; text-align:center;">
          <div style="font-size:10px; color:var(--muted); font-weight:700; text-transform:uppercase;">Umumiy Rasxod</div>
          <div style="font-size:15px; font-weight:900; color:#ef4444; margin-top:2px;">${expenseMln} mln</div>
          <div style="font-size:9px; color:var(--muted);">urug'+o'g'it+traktor</div>
        </div>

        <div style="background:var(--card); border:1px solid var(--border); border-radius:10px; padding:8px 10px; text-align:center;">
          <div style="font-size:10px; color:var(--muted); font-weight:700; text-transform:uppercase;">Sof Foyda</div>
          <div style="font-size:15px; font-weight:900; color:#10b981; margin-top:2px;">+${profitMln} mln</div>
          <div style="font-size:9px; color:#10b981; font-weight:700;">Rentabellik: ${rentability}%</div>
        </div>
      </div>

      <!-- AI Recommendation Insights -->
      <div style="background:rgba(255,255,255,0.7); dark:background:rgba(0,0,0,0.2); border-radius:10px; padding:10px; font-size:11.5px; line-height:1.5; color:var(--text);">
        <div style="font-weight:800; color:#0284c7; margin-bottom:4px; display:flex; align-items:center; gap:5px;">
          <span>💡 AI Agrotexnik Tavsiyasi (${distNames[districtKey] || districtKey}):</span>
        </div>
        <div>${crop.aiPros || "Ushbu ekin turi hudud tuprog'iga to'liq mos bo'lib, eng tejamkor agrotexnika talab qiladi."}</div>
        <div style="margin-top:6px; font-size:11px; color:var(--muted); border-top:1px dashed var(--border); padding-top:4px;">
          💧 <strong>Suv talabi:</strong> ${crop.waterNeed || "Mo'tadil"} | ⏱️ <strong>Vegetatsiya:</strong> ${crop.vegetationDays || 85} kun
        </div>
      </div>
    `;
  }

  function sendAiQuestion() {
    const input = document.getElementById('aiCustomQuestionInput');
    const box = document.getElementById('aiQuickAnswersBox');
    if (!input || !box) return;
    const q = input.value.trim().toLowerCase();
    if (!q) return;

    box.style.display = 'block';
    box.innerHTML = `<span style="color:#0284c7; font-weight:700;">AI tahlil qilmoqda... ⏳</span>`;

    setTimeout(() => {
      let answer = "";
      if (q.includes('50 sotix') || q.includes('sotix') || q.includes('eng ko\'p') || q.includes('foyda')) {
        answer = `🤖 <strong>AI maslahati (50 sotix ijara yer uchun):</strong><br>
        50 sotix yerda eng yuqori sof foyda beruvchi ekinlar:<br>
        1. <strong>Ertapishar sabzi yoki piyoz</strong> — rasxod: ~7 mln so'm, sof foyda: <strong>32-38 mln so'm</strong>.<br>
        2. <strong>Qalampir (Chust navi)</strong> — rasxod: ~8 mln so'm, sof foyda: <strong>45-50 mln so'm</strong>.<br>
        3. <strong>Poliz (qovun/tarvuz) + orqasidan kuzgi mosh</strong> — ikki hosildan sof daromad: <strong>40 mln so'mdan oshadi</strong>.`;
      } else if (q.includes('rasxod') || q.includes('xarajat') || q.includes('kam xarajat')) {
        answer = `🤖 <strong>Kam rasxodli ekinlar bo'yicha AI tavsiyasi:</strong><br>
        Eng kam xarajat talab qiluvchi ekin — <strong>Eksportbop Mosh va Dukkaklilar</strong> (gektariga rasxod 8-9 mln so'm, 50 sotixga atigi 4-4.5 mln so'm). Suvni kam ichadi va tuproqni qayta tiklaydi.`;
      } else if (q.includes('suv') || q.includes('suvsiz') || q.includes('adir')) {
        answer = `🤖 <strong>Suv tanqis yoki adir yerlar uchun:</strong><br>
        Pop va Chust adirlarida tomchilatib sug'oriladigan <strong>uzumzorlar, bodomzorlar</strong> va qator oralariga mosh yoki no'xat ekish tavsiya etiladi.`;
      } else {
        answer = `🤖 <strong>AI tahlil javobi:</strong><br>
        Namangan viloyatining tuproq boniteti (64–75 ball oralig'ida) intensiv sabzavotchilik, polizchilik va dukkakli ekinlarga to'liq imkon beradi. 
        50 sotix maydondan to'g'ri agrotexnika bilan yiliga kamida <strong>30-55 mln so'm</strong> sof daromad olish kafolatlanadi. Chapdagi jadvaldan ekin tanlab aniq rasxod va hosilni hisoblashingiz mumkin.`;
      }
      box.innerHTML = answer;
    }, 400);
  }

  function handleAiViewExcelUpload(event) {
    const file = event.target.files[0];
    if (!file) return;

    if (typeof XLSX === 'undefined') {
      alert("XLSX kutubxonasi hali yuklanmoqda, iltimos qayta urinib ko'ring.");
      return;
    }

    const reader = new FileReader();
    reader.onload = function(e) {
      try {
        const data = new Uint8Array(e.target.result);
        const workbook = XLSX.read(data, { type: 'array' });
        const firstSheet = workbook.Sheets[workbook.SheetNames[0]];
        const json = XLSX.utils.sheet_to_json(firstSheet);

        if (!json || json.length === 0) {
          alert("Excel faylida ma'lumot topilmadi!");
          return;
        }

        // Map uploaded rows into currentAiCrops
        const uploadedCrops = json.map((r, i) => {
          const name = r['Mahsulot nomi'] || r['mahsulot'] || r['Nomi'] || r['name'] || ('Ekin ' + (i+1));
          const sort = r['Mahalliy nav (sort)'] || r['Nav'] || r['Yangicha usul mahsulot nomi'] || 'Standart';
          const haYield = parseFloat(r['1 ga etishtiriladigan (tonna)'] || r['1 ga hosil'] || r['Yangicha usul 1 ga (tonna)'] || 25);
          const haIncome = parseFloat(r['1 ga olinadigan daromad'] || r['Yangicha usul 1 ga daromad'] || 60000000);
          const price = parseFloat(r['Narx (UZS/kg)'] || r['narx'] || 3000);
          const haExpense = haIncome * 0.25;

          return {
            id: 'crop-up-' + (i+1),
            name: name,
            category: "Yuklangan ekin",
            sort: sort,
            haYield: haYield,
            haExpense: haExpense,
            pricePerKg: price,
            haIncome: haIncome,
            haNetProfit: haIncome - haExpense,
            vegetationDays: 85,
            waterNeed: "Mo'tadil sug'orish",
            bestSoils: ["Bo'z tuproq"],
            aiPros: `Excel bazadan yuklangan: 1 ga maydondan ${haYield} tonna hosil va ${(haIncome/1000000).toFixed(1)} mln so'm daromad kutilmoqda.`
          };
        });

        currentAiCrops = uploadedCrops;
        try {
          localStorage.setItem('namangan_crop_database', JSON.stringify(uploadedCrops));
        } catch(err) { console.warn(err); }

        renderAiCropsTable(currentAiCrops);
        populateAiCropSelect(currentAiCrops);
        runAiCropAnalysis();

        alert(`✅ Muvaffaqiyatli yuklandi! Jami ${uploadedCrops.length} ta ekin bazaga kiritildi va AI tahlili yangilandi.`);
      } catch(err) {
        alert("Excel faylini o'qishda xatolik: " + err.message);
      }
    };
    reader.readAsArrayBuffer(file);
  }

  function resetAiConsultant() {
    runAiCropAnalysis();
    const box = document.getElementById('aiQuickAnswersBox');
    if (box) box.style.display = 'none';
  }
'''

files = ['index.html', 'namangan_interaktiv_xarita.html', 'public/namangan_interaktiv_xarita.html']

for filepath in files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    cn = content.replace('\r\n', '\n')

    # 1. Update Sidebar Menu Item
    # Replace Hisobotlar with "Hosil olish bo'yicha AI xizmati"
    old_menu = """      <div class="menu-item" onclick="switchMainView('stats')">
        <span class="menu-icon">📈</span>
        <span>Hisobotlar</span>
        <span class="menu-arrow">⌄</span>
      </div>"""

    new_menu = """      <div class="menu-item" id="menuAiService" onclick="switchMainView('aiService')">
        <span class="menu-icon">🌱</span>
        <span>Hosil olish bo'yicha AI xizmati</span>
      </div>"""

    if old_menu in cn:
        cn = cn.replace(old_menu, new_menu)
        print(f"Menu item updated in {filepath}")
    else:
        # Fallback regex search if spacing differs
        cn = re.sub(
            r'<div class="menu-item"[^>]*onclick="switchMainView\(\'stats\'\)"[^>]*>\s*<span class="menu-icon">📈</span>\s*<span>Hisobotlar</span>.*?</div>',
            new_menu,
            cn,
            flags=re.DOTALL
        )
        print(f"Menu item regex updated in {filepath}")

    # 2. Inject New View Section before </main> or before <section id="viewMap"
    if 'id="viewAiService"' not in cn:
        view_map_marker = '<section id="viewMap"'
        if view_map_marker in cn:
            cn = cn.replace(view_map_marker, new_view_html + '\n      ' + view_map_marker)
            print(f"View section injected in {filepath}")
        else:
            print(f"Could not find viewMap marker in {filepath}")

    # 3. Update switchMainView JS to support 'aiService'
    old_switch = """  function switchMainView(viewName) {
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
  }"""

    new_switch = """  function switchMainView(viewName) {
    const statsEl = document.getElementById('viewStats');
    const mapEl = document.getElementById('viewMap');
    const aiEl = document.getElementById('viewAiService');
    const menuStats = document.getElementById('menuStats');
    const menuMap = document.getElementById('menuMap');
    const menuAi = document.getElementById('menuAiService');

    if (statsEl) statsEl.classList.toggle('active', viewName === 'stats');
    if (mapEl) mapEl.classList.toggle('active', viewName === 'map');
    if (aiEl) aiEl.classList.toggle('active', viewName === 'aiService');

    if (menuStats) menuStats.classList.toggle('active', viewName === 'stats');
    if (menuMap) menuMap.classList.toggle('active', viewName === 'map');
    if (menuAi) menuAi.classList.toggle('active', viewName === 'aiService');

    if (viewName === 'map' && typeof renderInfo === 'function') {
      renderInfo(typeof selectedDistrict !== 'undefined' ? selectedDistrict : 'pop');
    }
    if (viewName === 'aiService' && typeof initAiServiceView === 'function') {
      initAiServiceView();
    }
  }"""

    if old_switch in cn:
        cn = cn.replace(old_switch, new_switch)
        print(f"switchMainView updated in {filepath}")
    else:
        # Normalize
        old_switch_norm = old_switch.replace('\r\n', '\n')
        if old_switch_norm in cn:
            cn = cn.replace(old_switch_norm, new_switch)
            print(f"switchMainView norm updated in {filepath}")
        else:
            print(f"switchMainView not found in {filepath}")

    # 4. Inject JS logic before </script>\n</body>
    if 'initAiServiceView' not in cn:
        cn = cn.replace('</script>\n</body>', new_view_js + '\n</script>\n</body>')
        print(f"JS logic injected in {filepath}")

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(cn)

print("All files updated successfully!")
