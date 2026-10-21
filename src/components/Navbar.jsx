import React from 'react';
import { 
  MapPin, 
  Layers, 
  Calculator, 
  Sprout, 
  Search, 
  Compass, 
  ArrowLeft,
  FileSpreadsheet,
  Lock,
  LogOut,
  ShieldCheck
} from 'lucide-react';
import { REGION_STATS, DISTRICTS_DATA } from '../data/namanganData';

export default function Navbar({
  selectedDistrict,
  onSelectDistrict,
  mapMode,
  setMapMode,
  onOpenCalculator,
  onOpenCropsCatalog,
  onOpenDataManager,
  onResetView,
  searchQuery,
  setSearchQuery,
  totalArea,
  totalFamilies,
  currentUser,
  onOpenAdminLogin,
  onLogout
}) {
  return (
    <header className="bg-white/95 backdrop-blur-md border-b border-slate-200 shadow-sm text-slate-800 sticky top-0 z-50">
      {/* Top Banner with Stats */}
      <div className="bg-gradient-to-r from-emerald-50 via-teal-50/60 to-slate-100 px-4 py-1.5 border-b border-emerald-100 text-xs hidden sm:flex items-center justify-between">
        <div className="flex items-center gap-2 text-emerald-800 font-semibold">
          <span className="inline-block w-2 h-2 rounded-full bg-emerald-500 animate-ping"></span>
          <span>Namangan viloyati: 14 ta tuman va shahar bo'yicha aholiga ajratilgan ijara yerlar dasturi</span>
        </div>
        <div className="flex items-center gap-6 text-slate-600">
          <div>Jami ijara yer: <strong className="text-slate-900 font-bold">{(totalArea || REGION_STATS.totalLeaseAreaHa).toLocaleString()}</strong> ga</div>
          <div>Band bo'lgan oilalar: <strong className="text-emerald-700 font-bold">{(totalFamilies || REGION_STATS.totalFamiliesEmployed).toLocaleString()}+</strong> ta</div>
          <div>O'rtacha daromad: <strong className="text-amber-700 font-bold">{REGION_STATS.averageFamilyNetProfitUzs}</strong></div>
        </div>
      </div>

      {/* Main Bar */}
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between gap-4">
        {/* Logo / Back Button */}
        <div className="flex items-center gap-3">
          {selectedDistrict ? (
            <button
              onClick={onResetView}
              className="flex items-center gap-2 px-3.5 py-2 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-white font-bold text-xs shadow-md shadow-emerald-600/20 transition active:scale-95"
            >
              <ArrowLeft className="w-4 h-4" />
              <span>Bosh sahifa (Dashboard)</span>
            </button>
          ) : (
            <div className="flex items-center gap-3 cursor-pointer select-none" onClick={onResetView}>
              <div className="w-10 h-10 rounded-xl bg-gradient-to-tr from-emerald-600 to-teal-500 flex items-center justify-center shadow-md shadow-emerald-500/20 text-white font-black text-xl">
                <Sprout className="w-6 h-6 text-white" />
              </div>
              <div>
                <div className="flex items-center gap-2">
                  <h1 className="font-extrabold text-lg leading-tight tracking-tight text-slate-900 flex items-center gap-1.5">
                    NAMANGAN <span className="text-emerald-600">IJARA YER</span>
                  </h1>
                  <span className="bg-emerald-100 text-emerald-800 text-[10px] font-bold px-2.5 py-0.5 rounded-full border border-emerald-200">
                    14 TUMAN
                  </span>
                </div>
                <p className="text-[11px] text-slate-500 hidden md:block">
                  Aholiga ajratilgan yer maydonlari • Agro-tahlil • Daromad monitoringi
                </p>
              </div>
            </div>
          )}

          {/* District Switcher Dropdown */}
          {selectedDistrict && (
            <div className="hidden md:flex items-center gap-2 pl-2 border-l border-slate-200">
              <span className="w-3 h-3 rounded-full" style={{ backgroundColor: selectedDistrict.color }}></span>
              <select
                value={selectedDistrict.id}
                onChange={(e) => {
                  const found = DISTRICTS_DATA.find(d => d.id === e.target.value);
                  if (found) onSelectDistrict(found);
                }}
                className="bg-slate-100 hover:bg-slate-200/80 text-slate-800 text-xs font-bold py-1.5 px-2.5 rounded-xl border border-slate-200 focus:outline-none focus:border-emerald-500 cursor-pointer transition"
              >
                {DISTRICTS_DATA.map(d => (
                  <option key={d.id} value={d.id}>
                    #{d.number} {d.name} ({d.totalLeaseAreaHa} ga)
                  </option>
                ))}
              </select>
            </div>
          )}
        </div>

        {/* Search Bar (Only shown in GIS mode) */}
        {selectedDistrict && (
          <div className="flex-1 max-w-xs hidden lg:block">
            <div className="relative">
              <Search className="w-3.5 h-3.5 absolute left-3 top-1/2 -translate-y-1/2 text-slate-400" />
              <input
                type="text"
                value={searchQuery}
                onChange={(e) => setSearchQuery(e.target.value)}
                placeholder="MFY, kontur yoki fuqaroni qidirish..."
                className="w-full bg-slate-100 hover:bg-slate-200/70 focus:bg-white text-slate-800 placeholder-slate-400 text-xs pl-8 pr-3 py-1.5 rounded-xl border border-slate-200 focus:border-emerald-500 focus:outline-none transition"
              />
              {searchQuery && (
                <button 
                  onClick={() => setSearchQuery('')}
                  className="absolute right-2.5 top-1/2 -translate-y-1/2 text-xs text-slate-400 hover:text-slate-700"
                >
                  ✕
                </button>
              )}
            </div>
          </div>
        )}

        {/* Actions & Map Controls */}
        <div className="flex items-center gap-2">
          {/* Map Mode Toggle: Satellite vs Street */}
          {selectedDistrict && (
            <div className="flex items-center bg-slate-100 p-0.5 rounded-xl border border-slate-200">
              <button
                onClick={() => setMapMode('streets')}
                className={`px-2.5 py-1.5 rounded-lg text-xs font-semibold flex items-center gap-1.5 transition ${
                  mapMode === 'streets' 
                    ? 'bg-emerald-600 text-white shadow-sm' 
                    : 'text-slate-600 hover:text-slate-900'
                }`}
                title="Oddiy xarita"
              >
                <Compass className="w-3.5 h-3.5" />
                <span className="hidden sm:inline">Oddiy</span>
              </button>
              <button
                onClick={() => setMapMode('satellite')}
                className={`px-2.5 py-1.5 rounded-lg text-xs font-semibold flex items-center gap-1.5 transition ${
                  mapMode === 'satellite' 
                    ? 'bg-emerald-600 text-white shadow-sm' 
                    : 'text-slate-600 hover:text-slate-900'
                }`}
                title="Sun'iy yo'ldosh xaritasi"
              >
                <Layers className="w-3.5 h-3.5" />
                <span className="hidden sm:inline">Sun'iy yo'ldosh</span>
              </button>
            </div>
          )}

          {/* Agro Calculator Button */}
          <button
            onClick={onOpenCalculator}
            className="flex items-center gap-1.5 px-3 py-1.5 bg-amber-50 hover:bg-amber-100 border border-amber-200 text-amber-800 rounded-xl text-xs font-semibold transition"
          >
            <Calculator className="w-3.5 h-3.5 text-amber-600" />
            <span className="hidden sm:inline">Kalkulyator</span>
          </button>

          {/* Crops Catalog Button */}
          <button
            onClick={onOpenCropsCatalog}
            className="flex items-center gap-1.5 px-3 py-1.5 bg-slate-100 hover:bg-slate-200 border border-slate-200 text-slate-700 rounded-xl text-xs font-medium transition"
          >
            <Sprout className="w-3.5 h-3.5 text-emerald-600" />
            <span className="hidden lg:inline">Ekinlar</span>
          </button>

          {/* Admin Panel (Placed at the far right) */}
          {currentUser ? (
            <div className="flex items-center gap-1.5 bg-emerald-50 border border-emerald-200 p-1 rounded-2xl ml-1">
              <button
                onClick={onOpenDataManager}
                className="flex items-center gap-1.5 px-3 py-1.5 bg-emerald-600 hover:bg-emerald-500 text-white rounded-xl text-xs font-bold shadow-sm transition active:scale-95"
                title="Admin: Excel orqali ma'lumot yuklash yoki qo'lda kiritish"
              >
                <FileSpreadsheet className="w-3.5 h-3.5" />
                <span>Ma'lumot yuklash (Excel)</span>
              </button>

              <div className="flex items-center gap-1 px-2 text-[11px] text-emerald-800 font-bold hidden md:flex">
                <ShieldCheck className="w-3.5 h-3.5 text-emerald-600" />
                <span>{currentUser.username}</span>
              </div>

              <button
                onClick={onLogout}
                className="p-1.5 text-slate-400 hover:text-rose-600 hover:bg-rose-50 rounded-lg transition"
                title="Admin paneldan chiqish"
              >
                <LogOut className="w-3.5 h-3.5" />
              </button>
            </div>
          ) : (
            <button
              onClick={onOpenAdminLogin}
              className="flex items-center gap-1.5 px-3.5 py-1.5 bg-slate-900 hover:bg-slate-800 text-white rounded-xl text-xs font-bold shadow-md shadow-slate-900/15 transition active:scale-95 ml-1"
              title="Admin panelga kirish (Login va parol bilan)"
            >
              <Lock className="w-3.5 h-3.5 text-emerald-400" />
              <span>Admin panel</span>
            </button>
          )}
        </div>
      </div>
    </header>
  );
}
