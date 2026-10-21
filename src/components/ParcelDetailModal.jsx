import React from 'react';
import { 
  X, 
  MapPin, 
  Navigation, 
  Droplets, 
  Sprout, 
  DollarSign, 
  TrendingUp, 
  Award, 
  ShieldCheck, 
  User, 
  Calendar, 
  ExternalLink,
  Layers,
  Sparkles,
  Info
} from 'lucide-react';

export default function ParcelDetailModal({ parcel, district, mfy, onClose }) {
  if (!parcel) return null;

  const [lat, lng] = parcel.coordinates;
  const googleMapsUrl = `https://www.google.com/maps/dir/?api=1&destination=${lat},${lng}`;
  const yandexMapsUrl = `https://yandex.com/maps/?rtext=~${lat},${lng}`;

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-3 sm:p-4 bg-slate-950/80 backdrop-blur-sm animate-in fade-in">
      <div className="bg-slate-900 border border-slate-700/80 rounded-3xl w-full max-w-3xl max-h-[92vh] overflow-hidden flex flex-col shadow-2xl text-white">
        {/* Header */}
        <div className="p-5 border-b border-slate-800 bg-gradient-to-r from-emerald-950/60 via-slate-900 to-slate-900 flex items-center justify-between">
          <div className="flex items-center gap-3">
            <div className="w-11 h-11 rounded-2xl bg-emerald-500/20 border border-emerald-500/30 flex items-center justify-center text-emerald-400 font-bold text-xl shadow-inner">
              🌾
            </div>
            <div>
              <div className="flex items-center gap-2">
                <h2 className="text-lg font-bold text-white">
                  {parcel.contourNumber} — Ijara yer pasporti
                </h2>
                <span className="bg-emerald-500/20 text-emerald-300 text-xs font-semibold px-2.5 py-0.5 rounded-full border border-emerald-500/40">
                  {parcel.allocatedAreaHa} ga ({parcel.allocatedAreaHa * 100} sotix)
                </span>
              </div>
              <p className="text-xs text-slate-400 flex items-center gap-1.5 mt-0.5">
                <MapPin className="w-3.5 h-3.5 text-emerald-400" />
                <span>{district?.name || "Namangan"}</span>
                <span>•</span>
                <span>{mfy?.name || "MFY"}</span>
                <span>•</span>
                <span className="font-mono text-slate-300">{lat.toFixed(4)}° N, {lng.toFixed(4)}° E</span>
              </p>
            </div>
          </div>

          <button
            onClick={onClose}
            className="w-9 h-9 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-400 hover:text-white flex items-center justify-center transition"
          >
            <X className="w-5 h-5" />
          </button>
        </div>

        {/* Modal Body */}
        <div className="flex-1 overflow-y-auto p-5 space-y-5">
          {/* Section 1: Yerning agronomik xususiyati va Namgarchiligi */}
          <div className="bg-slate-800/60 border border-slate-700/70 rounded-2xl p-4">
            <div className="flex items-center justify-between mb-3">
              <div className="flex items-center gap-2 text-xs font-semibold text-sky-400 uppercase tracking-wider">
                <Droplets className="w-4 h-4" />
                <span>Yer xususiyati va namgarchilik ko'rsatkichlari</span>
              </div>
              <span className="text-[11px] text-slate-400">Laboratoriya va kosmik tahlil</span>
            </div>

            <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-3 text-xs mb-3">
              <div className="bg-slate-900/80 p-3 rounded-xl border border-slate-800">
                <div className="text-slate-400 text-[11px]">Tuproq turi</div>
                <div className="font-semibold text-white mt-1 text-sm">{parcel.soil.type}</div>
              </div>

              <div className="bg-slate-900/80 p-3 rounded-xl border border-slate-800">
                <div className="text-slate-400 text-[11px]">Tuproq ball boniteti</div>
                <div className="flex items-center gap-2 mt-1">
                  <span className="font-bold text-amber-400 text-base">{parcel.soil.bonitetScore} ball</span>
                  <div className="flex-1 bg-slate-800 h-2 rounded-full overflow-hidden">
                    <div 
                      className="bg-amber-400 h-full rounded-full" 
                      style={{ width: `${parcel.soil.bonitetScore}%` }}
                    />
                  </div>
                </div>
              </div>

              <div className="bg-slate-900/80 p-3 rounded-xl border border-slate-800">
                <div className="text-slate-400 text-[11px]">Namgarchilik darajasi</div>
                <div className="font-bold text-sky-300 mt-1 text-sm">{parcel.soil.moisture}</div>
              </div>

              <div className="bg-slate-900/80 p-3 rounded-xl border border-slate-800">
                <div className="text-slate-400 text-[11px]">Sho'rlanish darajasi</div>
                <div className="font-semibold text-white mt-1">{parcel.soil.salinity}</div>
              </div>

              <div className="bg-slate-900/80 p-3 rounded-xl border border-slate-800">
                <div className="text-slate-400 text-[11px]">Sizot suvlari chuqurligi</div>
                <div className="font-semibold text-sky-400 mt-1">{parcel.soil.groundwaterDepth}</div>
              </div>

              <div className="bg-slate-900/80 p-3 rounded-xl border border-slate-800">
                <div className="text-slate-400 text-[11px]">Suv ta'minoti manbai</div>
                <div className="font-semibold text-emerald-400 mt-1 truncate" title={parcel.soil.waterSource}>
                  {parcel.soil.waterSource}
                </div>
              </div>
            </div>
          </div>

          {/* Section 3: Nima eksak yaxshi bo'ladi? (Agro-tavsiya) */}
          <div className="bg-gradient-to-br from-emerald-950/40 via-slate-800/80 to-slate-800/60 border border-emerald-500/40 rounded-2xl p-4">
            <div className="flex items-center gap-2 text-xs font-semibold text-emerald-400 uppercase tracking-wider mb-2">
              <Sprout className="w-4 h-4 text-emerald-400" />
              <span>Nima eksak yaxshi bo'ladi? (Ilmiy agro-tavsiya)</span>
            </div>

            <div className="grid grid-cols-1 md:grid-cols-2 gap-3 mb-3">
              <div className="bg-slate-900/80 p-3.5 rounded-xl border border-emerald-500/30">
                <div className="text-[11px] text-emerald-300 font-medium">Asosiy ekin turi (1-mavsum)</div>
                <div className="text-base font-bold text-white mt-1 flex items-center gap-2">
                  <span>🌱</span>
                  <span>{parcel.recommendation.primaryCrop}</span>
                </div>
              </div>

              <div className="bg-slate-900/80 p-3.5 rounded-xl border border-slate-800">
                <div className="text-[11px] text-sky-300 font-medium">Ikkinchi hosil / Qator orasi (2-mavsum)</div>
                <div className="text-base font-bold text-white mt-1 flex items-center gap-2">
                  <span>🍂</span>
                  <span>{parcel.recommendation.secondaryCrop}</span>
                </div>
              </div>
            </div>

            <div className="bg-slate-900/60 rounded-xl p-3 border border-slate-800 text-xs leading-relaxed text-slate-300">
              <p className="flex items-start gap-2">
                <Info className="w-4 h-4 text-emerald-400 shrink-0 mt-0.5" />
                <span><strong>Tuproq va namlikka mosligi:</strong> {parcel.recommendation.rationale}</span>
              </p>
              <div className="mt-2 text-[11px] text-slate-400 pt-2 border-t border-slate-800 flex items-center gap-2">
                <Calendar className="w-3.5 h-3.5 text-amber-400" />
                <span>Mavsumiy davr: <strong className="text-white">{parcel.recommendation.cycleMonths}</strong></span>
              </div>
            </div>
          </div>

          {/* Section 4: Qanday daromad ko'radi? (Biznes-reja va Foyda) */}
          <div className="bg-gradient-to-br from-amber-950/30 via-slate-800/80 to-slate-800/60 border border-amber-500/40 rounded-2xl p-4">
            <div className="flex items-center justify-between mb-3">
              <div className="flex items-center gap-2 text-xs font-semibold text-amber-400 uppercase tracking-wider">
                <DollarSign className="w-4 h-4 text-amber-400" />
                <span>Qanday daromad ko'radi? (Xonadonning sof foydasi)</span>
              </div>
              <span className="text-[11px] text-emerald-400 font-semibold bg-emerald-500/10 px-2 py-0.5 rounded-full border border-emerald-500/20">
                Yuqori rentabellik
              </span>
            </div>

            <div className="grid grid-cols-2 sm:grid-cols-4 gap-3 text-xs mb-3">
              <div className="bg-slate-900/90 p-3 rounded-xl border border-slate-800">
                <div className="text-slate-400 text-[11px]">Kiritiladigan xarajat</div>
                <div className="font-bold text-rose-400 text-sm mt-1">
                  {(parcel.economics.expensesUzs / 1000000).toFixed(1)} mln so'm
                </div>
                <div className="text-[10px] text-slate-500 mt-0.5">urug', o'g'it, texnika</div>
              </div>

              <div className="bg-slate-900/90 p-3 rounded-xl border border-slate-800">
                <div className="text-slate-400 text-[11px]">Kutilayotgan hosil</div>
                <div className="font-bold text-sky-400 text-sm mt-1">
                  {parcel.economics.expectedYield}
                </div>
                <div className="text-[10px] text-slate-500 mt-0.5">agrotexnika asosida</div>
              </div>

              <div className="bg-slate-900/90 p-3 rounded-xl border border-slate-800">
                <div className="text-slate-400 text-[11px]">Yalpi tushum (Bozor)</div>
                <div className="font-bold text-amber-300 text-sm mt-1">
                  {(parcel.economics.grossRevenueUzs / 1000000).toFixed(1)} mln so'm
                </div>
                <div className="text-[10px] text-slate-500 mt-0.5">ulgurji/chakana sotish</div>
              </div>

              <div className="bg-emerald-950/70 p-3 rounded-xl border border-emerald-500/50 shadow-lg">
                <div className="text-emerald-300 font-semibold text-[11px]">SOF FOYDA (Daromad)</div>
                <div className="font-black text-emerald-400 text-base mt-1">
                  +{(parcel.economics.netProfitUzs / 1000000).toFixed(1)} mln so'm
                </div>
                <div className="text-[10px] text-emerald-300/80 mt-0.5">
                  {parcel.economics.paybackMonths} oyda o'zini oqlaydi
                </div>
              </div>
            </div>

            <div className="text-[11px] text-slate-400 bg-slate-900/50 p-2.5 rounded-xl border border-slate-800 flex items-center justify-between">
              <span>💡 Ajratilgan ushbu ijara maydoni orqali xonadon yuqori agrotahlil asosida o'z daromadini kafolatlaydi.</span>
            </div>
          </div>
        </div>

        {/* Modal Footer with Direct GPS Navigator Buttons */}
        <div className="p-4 border-t border-slate-800 bg-slate-900/95 flex flex-wrap items-center justify-between gap-3">
          <div className="text-xs text-slate-400 flex items-center gap-2">
            <span className="w-2 h-2 rounded-full bg-emerald-400"></span>
            <span>Koordinata: <strong>{lat.toFixed(5)}, {lng.toFixed(5)}</strong></span>
          </div>

          <div className="flex items-center gap-2">
            <a
              href={googleMapsUrl}
              target="_blank"
              rel="noopener noreferrer"
              className="flex items-center gap-2 px-4 py-2 bg-emerald-600 hover:bg-emerald-500 text-white rounded-xl text-xs font-bold shadow-lg shadow-emerald-600/30 transition active:scale-95"
            >
              <Navigation className="w-4 h-4" />
              <span>Google Maps orqali borish</span>
              <ExternalLink className="w-3.5 h-3.5 opacity-80" />
            </a>

            <a
              href={yandexMapsUrl}
              target="_blank"
              rel="noopener noreferrer"
              className="flex items-center gap-2 px-3.5 py-2 bg-slate-800 hover:bg-slate-700 text-slate-200 rounded-xl text-xs font-semibold border border-slate-700 transition"
            >
              <span>Yandex Xarita</span>
            </a>

            <button
              onClick={onClose}
              className="px-4 py-2 bg-slate-800 hover:bg-slate-700 text-white rounded-xl text-xs font-medium border border-slate-700 transition"
            >
              Yopish
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}
