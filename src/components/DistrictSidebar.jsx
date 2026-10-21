import React, { useState } from 'react';
import { 
  MapPin, 
  ChevronRight, 
  ChevronDown, 
  Users, 
  Sprout, 
  TrendingUp, 
  Layers, 
  Droplets,
  ArrowLeft,
  Navigation,
  Sparkles,
  CheckCircle2,
  DollarSign,
  Target
} from 'lucide-react';

export default function DistrictSidebar({
  districts,
  selectedDistrict,
  selectedMFY,
  selectedParcel,
  onSelectDistrict,
  onSelectMFY,
  onSelectParcel,
  onResetToDashboard,
  searchQuery,
  setSearchQuery
}) {
  const [collapsed, setCollapsed] = useState(false);

  // If no district is selected, show general overview
  if (!selectedDistrict) return null;

  // Filter MFYs of the selected district
  const mfys = selectedDistrict.mfys || [];
  const filteredMFYs = mfys.filter(mfy => {
    if (!searchQuery) return true;
    const q = searchQuery.toLowerCase();
    const matchName = mfy.name.toLowerCase().includes(q);
    const matchSpec = mfy.specialization?.toLowerCase().includes(q);
    const matchParcel = mfy.parcels?.some(p => 
      p.farmerName.toLowerCase().includes(q) ||
      p.recommendation.primaryCrop.toLowerCase().includes(q) ||
      p.contourNumber.toLowerCase().includes(q)
    );
    return matchName || matchSpec || matchParcel;
  });

  return (
    <div className={`h-full bg-white border-r border-slate-200 flex flex-col transition-all duration-300 z-20 shadow-sm ${collapsed ? 'w-16' : 'w-80 md:w-96'}`}>
      
      {/* Sidebar Header: Selected District & Back Button */}
      <div className="p-4 border-b border-slate-200 bg-gradient-to-b from-slate-50 to-white">
        {!collapsed && (
          <div className="space-y-3">
            {/* Back button to return to 14 districts dashboard */}
            <div className="flex items-center justify-between">
              <button
                onClick={onResetToDashboard}
                className="flex items-center gap-1.5 text-xs font-bold text-emerald-700 hover:text-emerald-800 transition bg-emerald-50 hover:bg-emerald-100 px-3 py-1.5 rounded-xl border border-emerald-300 shadow-xs"
              >
                <ArrowLeft className="w-3.5 h-3.5" />
                <span>Bosh sahifaga qaytish</span>
              </button>

              <button
                onClick={() => setCollapsed(!collapsed)}
                className="p-1.5 rounded-lg bg-slate-100 text-slate-500 hover:text-slate-800 hover:bg-slate-200 transition"
                title="Kichraytirish"
              >
                <ChevronDown className="w-4 h-4" />
              </button>
            </div>

            {/* Current District Title Badge */}
            <div className="flex items-center gap-2.5 pt-1">
              <span 
                className="w-4 h-4 rounded-full shrink-0 shadow-sm ring-2 ring-emerald-500/30"
                style={{ backgroundColor: selectedDistrict.color }}
              />
              <div className="min-w-0">
                <div className="flex items-center gap-2">
                  <span className="text-xs font-bold text-slate-400">#{selectedDistrict.number}</span>
                  <h2 className="font-black text-slate-800 text-base truncate">
                    {selectedDistrict.name}
                  </h2>
                </div>
                <div className="flex items-center gap-2 text-[11px] text-slate-500 mt-0.5">
                  <span className="text-emerald-700 font-bold">{selectedDistrict.totalLeaseAreaHa} ga yer</span>
                  <span>•</span>
                  <span>{selectedDistrict.poorFamiliesCount} oila band</span>
                </div>
              </div>
            </div>

            {/* Drayver yo'nalishi nishoni */}
            {selectedDistrict.driverDirection && (
              <div className="bg-amber-50/90 rounded-xl p-2.5 border border-amber-200/90 text-[11px] text-amber-950 shadow-2xs">
                <div className="flex items-center gap-1.5 font-bold text-amber-800 text-[11px]">
                  <Target className="w-3.5 h-3.5 text-amber-600 shrink-0" />
                  <span>Drayver yo'nalishi:</span>
                </div>
                <div className="font-extrabold text-slate-900 mt-0.5 leading-snug">
                  {selectedDistrict.driverDirection}
                </div>
                {selectedDistrict.driverRationale && (
                  <p className="text-[10px] text-slate-600 mt-1 line-clamp-3 leading-relaxed border-t border-amber-200/50 pt-1">
                    {selectedDistrict.driverRationale}
                  </p>
                )}
              </div>
            )}

            {/* Subtitle instruction */}
            <div className="bg-emerald-50/70 rounded-xl p-2.5 border border-emerald-200/80 text-[11px] text-slate-700 flex items-start gap-1.5 font-medium leading-relaxed">
              <span className="text-emerald-600 mt-0.5">💡</span>
              <span>Quyidagi MFY lardan birini tanlang — xaritada o'sha yer maydoni, namligi, ekin tavsiyasi va daromadi chiqadi.</span>
            </div>
          </div>
        )}

        {collapsed && (
          <button
            onClick={() => setCollapsed(!collapsed)}
            className="w-full p-2 rounded-xl bg-slate-100 text-slate-600 hover:text-slate-900 flex items-center justify-center transition"
            title="Kengaytirish"
          >
            <ChevronRight className="w-5 h-5" />
          </button>
        )}
      </div>

      {/* MFYs Section Header */}
      {!collapsed && (
        <div className="px-4 py-2.5 bg-slate-50 border-b border-slate-200 flex items-center justify-between text-xs">
          <div className="flex items-center gap-2 font-bold text-slate-700">
            <Layers className="w-4 h-4 text-emerald-600" />
            <span>Mahalla fuqarolar yig'inlari (MFY)</span>
          </div>
          <span className="text-[11px] bg-white text-emerald-700 font-extrabold px-2.5 py-0.5 rounded-full border border-emerald-200 shadow-xs">
            {filteredMFYs.length} ta MFY
          </span>
        </div>
      )}

      {/* Dedicated MFY List - Clean, compact with elegant hover effect */}
      <div className="flex-1 overflow-y-auto p-3 space-y-2.5 bg-slate-50/50">
        {filteredMFYs.map((mfy) => {
          const isSelected = selectedMFY?.id === mfy.id;
          const parcel = mfy.parcels?.[0]; // Primary parcel for this MFY

          return (
            <div
              key={mfy.id}
              onClick={() => {
                onSelectMFY(mfy);
                if (parcel) {
                  onSelectParcel(parcel);
                }
              }}
              className={`group relative rounded-2xl border transition-all duration-200 cursor-pointer select-none p-3 flex items-center justify-between gap-2.5 ${
                isSelected
                  ? 'bg-emerald-50/80 border-2 border-emerald-500 shadow-md shadow-emerald-500/15 ring-2 ring-emerald-500/10'
                  : 'bg-white border-slate-200/90 shadow-xs hover:border-emerald-400 hover:bg-emerald-50/30 hover:shadow-md hover:-translate-y-0.5 hover:scale-[1.01]'
              }`}
            >
              {/* Left Pin Marker & Names */}
              <div className="flex items-center gap-2.5 min-w-0">
                <span className={`w-8 h-8 rounded-xl flex items-center justify-center text-sm shrink-0 transition-all duration-200 ${
                  isSelected 
                    ? 'bg-emerald-600 text-white font-bold shadow-sm' 
                    : 'bg-slate-100 text-slate-500 group-hover:bg-emerald-100 group-hover:text-emerald-700 group-hover:scale-105'
                }`}>
                  📍
                </span>
                
                <div className="min-w-0">
                  <h3 className={`font-extrabold text-sm truncate transition-colors duration-200 ${
                    isSelected ? 'text-emerald-800' : 'text-slate-800 group-hover:text-emerald-700'
                  }`}>
                    {mfy.name}
                  </h3>
                  <div className="text-[11px] text-slate-400 group-hover:text-slate-500 mt-0.5 transition-colors">
                    {mfy.poorFamilies} ta oila biriktirilgan
                  </div>
                </div>
              </div>

              {/* Right Area Badge & Arrow Indicator */}
              <div className="flex items-center gap-2 shrink-0">
                <span className={`font-black text-xs px-2.5 py-1 rounded-xl border transition-all duration-200 ${
                  isSelected 
                    ? 'bg-emerald-600 text-white border-emerald-600 shadow-xs' 
                    : 'bg-slate-50 text-slate-700 border-slate-200 group-hover:bg-emerald-50 group-hover:border-emerald-300 group-hover:text-emerald-800'
                }`}>
                  {mfy.leaseAreaHa} ga
                </span>

                <ChevronRight className={`w-4 h-4 transition-all duration-200 ${
                  isSelected 
                    ? 'text-emerald-600 translate-x-0.5' 
                    : 'text-slate-400 group-hover:text-emerald-600 group-hover:translate-x-1'
                }`} />
              </div>
            </div>
          );
        })}
      </div>

      {/* Footer Info */}
      {!collapsed && (
        <div className="p-3 border-t border-slate-200 bg-white text-xs text-slate-500 flex items-center justify-between">
          <div className="flex items-center gap-1.5 text-emerald-700 font-semibold">
            <CheckCircle2 className="w-4 h-4 text-emerald-600" />
            <span className="text-[11px]">Haqiqiy GPS lokatsiya va agrotahlil</span>
          </div>
          <span className="text-[10px] text-slate-400 font-medium">Namangan 2026</span>
        </div>
      )}
    </div>
  );
}
