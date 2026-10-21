import React from 'react';
import { X, Sprout, CheckCircle2, TrendingUp, Droplets, MapPin } from 'lucide-react';
import { CROPS_CATALOG } from '../data/namanganData';

export default function CropsCatalogModal({ isOpen, onClose }) {
  if (!isOpen) return null;

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-3 sm:p-4 bg-slate-950/80 backdrop-blur-sm animate-in fade-in">
      <div className="bg-slate-900 border border-slate-700/80 rounded-3xl w-full max-w-4xl max-h-[90vh] overflow-hidden flex flex-col shadow-2xl text-white">
        {/* Header */}
        <div className="p-5 border-b border-slate-800 bg-gradient-to-r from-emerald-950/60 via-slate-900 to-slate-900 flex items-center justify-between">
          <div className="flex items-center gap-3">
            <div className="w-10 h-10 rounded-2xl bg-emerald-500/20 border border-emerald-500/30 flex items-center justify-center text-emerald-400 font-bold text-xl">
              <Sprout className="w-5 h-5 text-emerald-400" />
            </div>
            <div>
              <h2 className="text-base font-bold text-white">
                Namangan viloyati uchun tavsiya etiladigan ekinlar katalogi
              </h2>
              <p className="text-xs text-slate-400">
                Tuproq unumdorligi, namlik talabi va kutilayotgan daromad ko'rsatkichlari
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

        {/* Catalog Grid */}
        <div className="flex-1 overflow-y-auto p-5">
          <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
            {CROPS_CATALOG.map(crop => (
              <div
                key={crop.id}
                className="bg-slate-800/70 border border-slate-700/80 rounded-2xl p-4 hover:border-emerald-500/50 transition shadow-lg flex flex-col justify-between"
              >
                <div>
                  <div className="flex items-center justify-between gap-2 border-b border-slate-700/60 pb-2 mb-3">
                    <div className="flex items-center gap-2.5">
                      <span className="text-2xl">{crop.icon}</span>
                      <h3 className="font-bold text-sm text-white">{crop.name}</h3>
                    </div>
                    <span className="bg-emerald-500/20 text-emerald-300 text-[11px] font-semibold px-2 py-0.5 rounded-full border border-emerald-500/30">
                      {crop.avgProfitPer50Sotix}
                    </span>
                  </div>

                  <div className="space-y-2 text-xs text-slate-300 mb-3">
                    <div className="flex items-start gap-2">
                      <span className="text-slate-400 shrink-0 font-medium">🌱 Tuproq talabi:</span>
                      <span>{crop.suitableSoil} (min. {crop.minBonitet} ball)</span>
                    </div>

                    <div className="flex items-start gap-2">
                      <span className="text-slate-400 shrink-0 font-medium">💧 Namlik rejimi:</span>
                      <span className="text-sky-300">{crop.optimalMoisture} ({crop.irrigationFreq})</span>
                    </div>

                    <div className="flex items-start gap-2">
                      <span className="text-slate-400 shrink-0 font-medium">⚖️ O'rtacha hosil:</span>
                      <span className="text-amber-300 font-semibold">{crop.avgYieldPerHa}</span>
                    </div>

                    <div className="flex items-start gap-2">
                      <span className="text-slate-400 shrink-0 font-medium">💵 Bozor narxi:</span>
                      <span className="text-white font-medium">{crop.marketPricePerKg}</span>
                    </div>
                  </div>
                </div>

                <div className="pt-2 border-t border-slate-700/60 flex items-center justify-between text-[11px] text-slate-400">
                  <span className="flex items-center gap-1 text-emerald-400">
                    <MapPin className="w-3.5 h-3.5" />
                    <span>Mos tumanlar:</span>
                  </span>
                  <span className="text-slate-300 truncate max-w-[200px]" title={crop.bestDistricts.join(', ')}>
                    {crop.bestDistricts.join(', ')}
                  </span>
                </div>
              </div>
            ))}
          </div>
        </div>

        {/* Footer */}
        <div className="p-4 border-t border-slate-800 bg-slate-900/90 flex justify-end">
          <button
            onClick={onClose}
            className="px-5 py-2 bg-slate-800 hover:bg-slate-700 text-white rounded-xl text-xs font-semibold border border-slate-700 transition"
          >
            Yopish
          </button>
        </div>
      </div>
    </div>
  );
}
