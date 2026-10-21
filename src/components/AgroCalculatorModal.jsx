import React, { useState } from 'react';
import { X, Calculator, Sprout, DollarSign, ArrowRight, Sparkles, TrendingUp } from 'lucide-react';
import { CROPS_CATALOG, DISTRICTS_DATA } from '../data/namanganData';

export default function AgroCalculatorModal({ isOpen, onClose }) {
  if (!isOpen) return null;

  const [selectedDistrict, setSelectedDistrict] = useState(DISTRICTS_DATA[0].name);
  const [areaSotix, setAreaSotix] = useState(50); // 50 sotix = 0.5 ga
  const [selectedCropId, setSelectedCropId] = useState('kartoshka');
  const [soilQuality, setSoilQuality] = useState('yaxshi'); // yaxshi, orta, past

  const selectedCrop = CROPS_CATALOG.find(c => c.id === selectedCropId) || CROPS_CATALOG[0];

  // Dynamic calculations based on area, crop and soil
  const areaHa = areaSotix / 100;
  const qualityMultiplier = soilQuality === 'yaxshi' ? 1.15 : soilQuality === 'orta' ? 1.0 : 0.85;

  let baseExpensePerSotix = 130000; // 130 ming so'm / sotix
  let baseYieldKgPerSotix = 300; // 300 kg / sotix
  let avgPricePerKg = 4500; // 4,500 so'm / kg

  if (selectedCropId === 'kartoshka') {
    baseExpensePerSotix = 145000;
    baseYieldKgPerSotix = 280;
    avgPricePerKg = 4800;
  } else if (selectedCropId === 'sabzi') {
    baseExpensePerSotix = 110000;
    baseYieldKgPerSotix = 350;
    avgPricePerKg = 3200;
  } else if (selectedCropId === 'piyoz') {
    baseExpensePerSotix = 150000;
    baseYieldKgPerSotix = 420;
    avgPricePerKg = 3000;
  } else if (selectedCropId === 'mosh') {
    baseExpensePerSotix = 70000;
    baseYieldKgPerSotix = 25;
    avgPricePerKg = 14000;
  } else if (selectedCropId === 'gilos') {
    baseExpensePerSotix = 160000;
    baseYieldKgPerSotix = 90;
    avgPricePerKg = 32000;
  } else if (selectedCropId === 'sholi') {
    baseExpensePerSotix = 140000;
    baseYieldKgPerSotix = 70;
    avgPricePerKg = 16000;
  }

  const totalExpense = Math.round(baseExpensePerSotix * areaSotix);
  const totalYieldKg = Math.round(baseYieldKgPerSotix * areaSotix * qualityMultiplier);
  const grossRevenue = Math.round(totalYieldKg * avgPricePerKg);
  const netProfit = Math.max(0, grossRevenue - totalExpense);

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-3 sm:p-4 bg-slate-950/80 backdrop-blur-sm animate-in fade-in">
      <div className="bg-slate-900 border border-slate-700/80 rounded-3xl w-full max-w-2xl max-h-[92vh] overflow-hidden flex flex-col shadow-2xl text-white">
        {/* Header */}
        <div className="p-5 border-b border-slate-800 bg-gradient-to-r from-amber-950/50 via-slate-900 to-slate-900 flex items-center justify-between">
          <div className="flex items-center gap-3">
            <div className="w-10 h-10 rounded-2xl bg-amber-500/20 border border-amber-500/30 flex items-center justify-center text-amber-400 font-bold text-lg">
              <Calculator className="w-5 h-5 text-amber-400" />
            </div>
            <div>
              <h2 className="text-base font-bold text-white">
                Agro-Daromad Kalkulyatori
              </h2>
              <p className="text-xs text-slate-400">
                Maydon o'lchami va ekin turiga qarab sof daromadni prognoz qilish
              </p>
            </div>
          </div>

          <button
            onClick={onClose}
            className="w-8 h-8 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-400 hover:text-white flex items-center justify-center transition"
          >
            <X className="w-4 h-4" />
          </button>
        </div>

        {/* Form & Calculations */}
        <div className="flex-1 overflow-y-auto p-5 space-y-5">
          {/* Inputs Section */}
          <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
            <div>
              <label className="block text-xs font-semibold text-slate-300 mb-1.5">
                Tuman yoki Shaharni tanlang:
              </label>
              <select
                value={selectedDistrict}
                onChange={(e) => setSelectedDistrict(e.target.value)}
                className="w-full bg-slate-800 border border-slate-700 rounded-xl px-3 py-2 text-xs text-white focus:outline-none focus:border-amber-400"
              >
                {DISTRICTS_DATA.map(d => (
                  <option key={d.id} value={d.name}>{d.name}</option>
                ))}
              </select>
            </div>

            <div>
              <label className="block text-xs font-semibold text-slate-300 mb-1.5">
                Ekin turini tanlang:
              </label>
              <select
                value={selectedCropId}
                onChange={(e) => setSelectedCropId(e.target.value)}
                className="w-full bg-slate-800 border border-slate-700 rounded-xl px-3 py-2 text-xs text-white focus:outline-none focus:border-amber-400"
              >
                {CROPS_CATALOG.map(crop => (
                  <option key={crop.id} value={crop.id}>
                    {crop.icon} {crop.name}
                  </option>
                ))}
              </select>
            </div>

            <div>
              <label className="block text-xs font-semibold text-slate-300 mb-1.5 flex items-center justify-between">
                <span>Ajratilgan yer maydoni:</span>
                <span className="text-amber-400 font-bold">{areaSotix} sotix ({areaHa} ga)</span>
              </label>
              <input
                type="range"
                min="10"
                max="200"
                step="5"
                value={areaSotix}
                onChange={(e) => setAreaSotix(Number(e.target.value))}
                className="w-full accent-amber-400"
              />
              <div className="flex justify-between text-[10px] text-slate-400 mt-1">
                <span>10 sotix</span>
                <span>50 sotix (0.5 ga)</span>
                <span>100 sotix (1 ga)</span>
                <span>200 sotix</span>
              </div>
            </div>

            <div>
              <label className="block text-xs font-semibold text-slate-300 mb-1.5">
                Tuproq unumdorligi va namligi:
              </label>
              <select
                value={soilQuality}
                onChange={(e) => setSoilQuality(e.target.value)}
                className="w-full bg-slate-800 border border-slate-700 rounded-xl px-3 py-2 text-xs text-white focus:outline-none focus:border-amber-400"
              >
                <option value="yaxshi">A'lo darajada (75+ ball bonitet, serob suv)</option>
                <option value="orta">O'rtacha darajada (60-74 ball bonitet)</option>
                <option value="past">Adir / Qumloq (Qo'shimcha o'g'it talab etiladi)</option>
              </select>
            </div>
          </div>

          {/* Results Cards */}
          <div className="bg-gradient-to-br from-emerald-950/50 via-slate-800 to-slate-900 border border-emerald-500/40 rounded-2xl p-4 shadow-xl">
            <div className="text-xs font-bold text-emerald-400 uppercase tracking-wider mb-3 flex items-center gap-2">
              <TrendingUp className="w-4 h-4" />
              <span>Hisoblangan daromad ko'rsatkichlari:</span>
            </div>

            <div className="grid grid-cols-2 sm:grid-cols-4 gap-3 text-xs mb-3">
              <div className="bg-slate-900/80 p-3 rounded-xl border border-slate-800">
                <div className="text-slate-400 text-[11px]">Sarf-xarajat</div>
                <div className="font-bold text-rose-400 text-sm mt-1">
                  {(totalExpense / 1000000).toFixed(1)} mln so'm
                </div>
              </div>

              <div className="bg-slate-900/80 p-3 rounded-xl border border-slate-800">
                <div className="text-slate-400 text-[11px]">Kutilayotgan hosil</div>
                <div className="font-bold text-sky-400 text-sm mt-1">
                  {totalYieldKg >= 1000 ? `${(totalYieldKg / 1000).toFixed(1)} tonna` : `${totalYieldKg} kg`}
                </div>
              </div>

              <div className="bg-slate-900/80 p-3 rounded-xl border border-slate-800">
                <div className="text-slate-400 text-[11px]">Yalpi tushum</div>
                <div className="font-bold text-amber-300 text-sm mt-1">
                  {(grossRevenue / 1000000).toFixed(1)} mln so'm
                </div>
              </div>

              <div className="bg-emerald-950/80 p-3 rounded-xl border border-emerald-500/60 shadow-lg">
                <div className="text-emerald-300 font-bold text-[11px]">SOF FOYDA</div>
                <div className="font-black text-emerald-400 text-base mt-1">
                  +{(netProfit / 1000000).toFixed(1)} mln so'm
                </div>
              </div>
            </div>

            <div className="bg-slate-900/60 p-3 rounded-xl border border-slate-800 text-xs text-slate-300 space-y-1">
              <div>🌱 <strong>Ekin xususiyati:</strong> {selectedCrop.name} — {selectedCrop.suitableSoil}.</div>
              <div>💧 <strong>Optimal namlik:</strong> {selectedCrop.optimalMoisture}, {selectedCrop.irrigationFreq}.</div>
              <div>📍 <strong>Mos tumanlar:</strong> {selectedCrop.bestDistricts.join(', ')}.</div>
            </div>
          </div>
        </div>

        {/* Footer */}
        <div className="p-4 border-t border-slate-800 bg-slate-900/90 flex justify-end">
          <button
            onClick={onClose}
            className="px-5 py-2 bg-emerald-600 hover:bg-emerald-500 text-white rounded-xl text-xs font-semibold transition"
          >
            Tushunarli, yopish
          </button>
        </div>
      </div>
    </div>
  );
}
