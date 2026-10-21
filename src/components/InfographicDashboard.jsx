import React, { useState } from 'react';
import { MapPin, Sparkles, CheckCircle2, ChevronRight, Layers } from 'lucide-react';
import NamanganMapGraphic from './NamanganMapGraphic';
import { REGION_STATS } from '../data/namanganData';

export default function InfographicDashboard({ districts, onSelectDistrict, totalArea }) {
  const [hoveredDistrict, setHoveredDistrict] = useState(null);

  return (
    <div className="w-full h-full overflow-y-auto bg-gradient-to-br from-slate-50 via-sky-50/40 to-emerald-50/30 p-3 sm:p-4 lg:p-5 flex flex-col justify-between">
      {/* 1-rasm: Bosh sarlavha "AHOLIGA AJRATILGAN IJARA YER MAYDONLARI" */}
      <div className="text-center max-w-4xl mx-auto mb-2 select-none">
        <div className="inline-flex items-center gap-2 px-3.5 py-1 rounded-full bg-emerald-100/80 border border-emerald-200/80 text-emerald-800 text-xs font-bold mb-1 shadow-sm">
          <Sparkles className="w-3.5 h-3.5 text-emerald-600" />
          <span>NAMANGAN VILOYATI IJARA YERLAR GEOPORTALI</span>
        </div>

        <h1 className="text-xl sm:text-3xl lg:text-4xl font-black text-slate-900 tracking-tight uppercase">
          AHOLIGA AJRATILGAN IJARA YER MAYDONLARI
        </h1>
      </div>

      {/* Main 2-Side Layout: 
          Left Side: 3-rasm (14 ta tuman bir qatorga terilgan) va uni eng tepasida 4-rasm (Jami ajratilgan maydon nishoni)
          Right Side: 2-rasm (14 TA TUMAN VA SHAHAR INTERAKTIV XARITASI) xarita tepasida va kattaroq xarita
      */}
      <div className="grid grid-cols-1 lg:grid-cols-12 gap-4 lg:gap-6 items-start max-w-7xl mx-auto w-full flex-1 my-auto">
        
        {/* Chap tomon: 3-rasm (Tumanlar bir qatorga) va uning tepasida 4-rasm (Jami maydon) */}
        <div className="lg:col-span-5 xl:col-span-4 bg-slate-50/80 p-3 sm:p-3.5 rounded-3xl border border-slate-200/80 shadow-xs flex flex-col gap-2.5">
          {/* 4-rasm: Jami ajratilgan maydon nishoni - Tumanlar ro'yxatining eng tepa qismida */}
          <div className="bg-gradient-to-r from-emerald-500 via-teal-500 to-sky-500 p-[1.5px] rounded-2xl shadow-sm">
            <div className="bg-white/95 backdrop-blur-md px-4 py-2 rounded-2xl flex items-center justify-between gap-2">
              <span className="text-[11px] font-extrabold text-slate-600 uppercase tracking-wider">
                Jami ajratilgan maydon:
              </span>
              <div className="flex items-center gap-1.5">
                <span className="text-lg sm:text-xl font-black text-slate-900">
                  {(totalArea || REGION_STATS.totalLeaseAreaHa).toLocaleString()}
                </span>
                <span className="bg-emerald-600 text-white text-[10px] font-black px-2 py-0.5 rounded-md shadow-xs">
                  GEKTAR
                </span>
              </div>
            </div>
          </div>

          {/* 3-rasm sarlavhasi */}
          <div className="flex items-center justify-between px-1 pt-0.5">
            <span className="text-xs font-bold text-slate-700 flex items-center gap-1.5 uppercase tracking-wider">
              <MapPin className="w-3.5 h-3.5 text-emerald-600" />
              <span>Namangan viloyati tumanlari (1 - 14)</span>
            </span>
            <span className="text-[10px] bg-emerald-100 text-emerald-800 font-extrabold px-2.5 py-0.5 rounded-full border border-emerald-200">
              14 ta hudud
            </span>
          </div>

          {/* 3-rasm: Tumanlar bir qatorga (1 ustunda tartib bilan) terilgan */}
          <div className="grid grid-cols-1 gap-1.5 max-h-[500px] overflow-y-auto pr-1">
            {districts.map(d => {
              const isHovered = hoveredDistrict === d.id;
              return (
                <div
                  key={d.id}
                  onClick={() => onSelectDistrict(d)}
                  onMouseEnter={() => setHoveredDistrict(d.id)}
                  onMouseLeave={() => setHoveredDistrict(null)}
                  className={`group cursor-pointer select-none rounded-xl p-2 px-3 border transition-all duration-200 flex items-center justify-between gap-2 shadow-xs ${
                    isHovered
                      ? 'bg-white border-emerald-500 scale-[1.01] shadow-md ring-2 ring-emerald-500/20'
                      : 'bg-white border-slate-200/90 hover:bg-emerald-50/20 hover:border-emerald-300'
                  }`}
                >
                  {/* Number & Name */}
                  <div className="flex items-center gap-2.5 min-w-0">
                    <div 
                      className="w-5 h-5 rounded-full flex items-center justify-center font-black text-[11px] text-white shrink-0 shadow-xs"
                      style={{ backgroundColor: d.color }}
                    >
                      {d.number}
                    </div>
                    
                    <div className="min-w-0">
                      <h3 className="font-bold text-xs sm:text-[13px] text-slate-800 truncate group-hover:text-emerald-700 transition">
                        {d.name}
                      </h3>
                      <div className="text-[10px] text-slate-400 truncate">
                        {d.poorFamiliesCount} ta oila
                      </div>
                    </div>
                  </div>

                  {/* Stat Pill */}
                  <div 
                    className="px-2.5 py-1 rounded-xl font-bold text-xs text-white text-right shrink-0 shadow-xs flex items-center gap-0.5 transition-all"
                    style={{ backgroundColor: d.color }}
                  >
                    <span>{d.totalLeaseAreaHa.toLocaleString()}</span>
                    <span className="text-[10px] font-medium opacity-90">ga</span>
                  </div>
                </div>
              );
            })}
          </div>
        </div>

        {/* O'ng tomon: 2-rasm (Xarita sarlavhasi) xarita tepasida va ozgina kattalashtirilgan sifatli xarita */}
        <div className="lg:col-span-7 xl:col-span-8 flex flex-col items-center justify-center p-1 w-full">
          {/* 2-rasm: 14 TA TUMAN VA SHAHAR INTERAKTIV XARITASI xarita tepasiga joylandi */}
          <div className="text-center mb-2.5 select-none">
            <h2 className="text-base sm:text-xl lg:text-2xl font-black text-emerald-700 tracking-wide uppercase">
              14 TA TUMAN VA SHAHAR INTERAKTIV XARITASI
            </h2>
            <p className="text-xs text-slate-500 mt-0.5">
              👉 Quyidagi xaritadan tuman ustiga olib boring yoki bosing
            </p>
          </div>

          <NamanganMapGraphic
            districts={districts}
            selectedDistrict={null}
            onSelectDistrict={onSelectDistrict}
            hoveredDistrict={hoveredDistrict}
            setHoveredDistrict={setHoveredDistrict}
          />
        </div>

      </div>

      {/* Bottom Summary Footer */}
      <div className="mt-2.5 pt-2 border-t border-slate-200 max-w-7xl mx-auto w-full flex flex-wrap items-center justify-between text-xs text-slate-500 gap-3">
        <div className="flex items-center gap-4">
          <div className="flex items-center gap-1.5 text-emerald-700 font-semibold">
            <CheckCircle2 className="w-4 h-4 text-emerald-600" />
            <span>14 ta tuman va shahar qamrovi</span>
          </div>
          <div>•</div>
          <div>Jami oilalar bandligi: <strong className="text-slate-800 font-bold">{districts.reduce((a, c) => a + (c.poorFamiliesCount || 0), 0).toLocaleString()}+</strong></div>
        </div>

        <div className="flex items-center gap-2 text-[11px] text-slate-500">
          <span>Har bir tumanda MFYlar, yer konturlari, namlik va daromad hisob-kitobi mavjud.</span>
        </div>
      </div>
    </div>
  );
}
