import React, { useState } from 'react';
import { X, PlusCircle, CheckCircle, MapPin, User, Sprout, DollarSign } from 'lucide-react';
import { DISTRICTS_DATA } from '../data/namanganData';

export default function AddParcelModal({ isOpen, onClose, onAddParcel }) {
  if (!isOpen) return null;

  const [districtId, setDistrictId] = useState(DISTRICTS_DATA[0].id);
  const [mfyName, setMfyName] = useState('');
  const [contourNumber, setContourNumber] = useState('');
  const [farmerName, setFarmerName] = useState('');
  const [familyStatus, setFamilyStatus] = useState('Temir daftar');
  const [allocatedAreaHa, setAllocatedAreaHa] = useState(0.5);
  const [primaryCrop, setPrimaryCrop] = useState('Ertapishar kartoshka');
  const [soilType, setSoilType] = useState("O'tloqi bo'z tuproq");
  const [bonitetScore, setBonitetScore] = useState(72);
  const [moisture, setMoisture] = useState('68% (Optimal namlik)');
  const [netProfitMln, setNetProfitMln] = useState(35);

  const selectedDist = DISTRICTS_DATA.find(d => d.id === districtId);

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!farmerName || !contourNumber) {
      alert("Iltimos, fuqaro F.I.Sh. va kontur raqamini kiriting!");
      return;
    }

    // Generate random coordinates around district center
    const latOffset = (Math.random() - 0.5) * 0.02;
    const lngOffset = (Math.random() - 0.5) * 0.02;
    const baseLat = selectedDist.center[0] + latOffset;
    const baseLng = selectedDist.center[1] + lngOffset;

    const newParcel = {
      id: `NEW-${Date.now()}`,
      contourNumber: `${contourNumber}-kontur`,
      farmerName,
      familyStatus,
      familyMembers: 5,
      allocatedAreaHa: Number(allocatedAreaHa),
      contractYear: "2026 - 2036 (10 yil)",
      coordinates: [baseLat, baseLng],
      polygon: [
        [baseLat - 0.001, baseLng - 0.0015],
        [baseLat + 0.001, baseLng - 0.001],
        [baseLat + 0.0008, baseLng + 0.0015],
        [baseLat - 0.0012, baseLng + 0.001]
      ],
      soil: {
        type: soilType,
        bonitetScore: Number(bonitetScore),
        moisture: moisture,
        salinity: "Sho'rlanmagan",
        groundwaterDepth: "2.1 metr",
        waterSource: "Kafolatlangan oqim ariq suvi"
      },
      recommendation: {
        primaryCrop: primaryCrop,
        secondaryCrop: "Dukkakli mosh va ko'katlar",
        rationale: "Tuproq boniteti va namlik ko'rsatkichlariga to'liq mos keladi.",
        cycleMonths: "Aprel - Oktyabr"
      },
      economics: {
        expensesUzs: Math.round(Number(allocatedAreaHa) * 12000000),
        expectedYield: `${(Number(allocatedAreaHa) * 26).toFixed(1)} tonna`,
        grossRevenueUzs: Math.round(Number(netProfitMln) * 1000000 * 1.25),
        netProfitUzs: Math.round(Number(netProfitMln) * 1000000),
        paybackMonths: 3.5
      }
    };

    onAddParcel(districtId, mfyName || selectedDist.mfys[0]?.name || "Markaz MFY", newParcel);
    onClose();
  };

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-3 sm:p-4 bg-slate-950/80 backdrop-blur-sm animate-in fade-in">
      <div className="bg-slate-900 border border-slate-700/80 rounded-3xl w-full max-w-xl max-h-[92vh] overflow-hidden flex flex-col shadow-2xl text-white">
        {/* Header */}
        <div className="p-5 border-b border-slate-800 bg-gradient-to-r from-emerald-950/50 via-slate-900 to-slate-900 flex items-center justify-between">
          <div className="flex items-center gap-3">
            <div className="w-10 h-10 rounded-2xl bg-emerald-500/20 border border-emerald-500/30 flex items-center justify-center text-emerald-400 font-bold text-lg">
              <PlusCircle className="w-5 h-5 text-emerald-400" />
            </div>
            <div>
              <h2 className="text-base font-bold text-white">
                Yangi ijara yer konturini qo'shish
              </h2>
              <p className="text-xs text-slate-400">
                Xonadonga ajratilgan yangi yer maydonini GIS xaritasiga kiritish
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

        {/* Form Body */}
        <form onSubmit={handleSubmit} className="flex-1 overflow-y-auto p-5 space-y-4">
          <div className="grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs">
            <div>
              <label className="block text-slate-300 font-medium mb-1">Tuman:</label>
              <select
                value={districtId}
                onChange={(e) => setDistrictId(e.target.value)}
                className="w-full bg-slate-800 border border-slate-700 rounded-xl px-3 py-2 text-white focus:outline-none focus:border-emerald-500"
              >
                {DISTRICTS_DATA.map(d => (
                  <option key={d.id} value={d.id}>{d.name}</option>
                ))}
              </select>
            </div>

            <div>
              <label className="block text-slate-300 font-medium mb-1">MFY nomi:</label>
              <input
                type="text"
                value={mfyName}
                onChange={(e) => setMfyName(e.target.value)}
                placeholder="Masalan: Paxtakor MFY"
                className="w-full bg-slate-800 border border-slate-700 rounded-xl px-3 py-2 text-white focus:outline-none focus:border-emerald-500"
              />
            </div>

            <div>
              <label className="block text-slate-300 font-medium mb-1">Kontur raqami:</label>
              <input
                type="text"
                required
                value={contourNumber}
                onChange={(e) => setContourNumber(e.target.value)}
                placeholder="Masalan: 154"
                className="w-full bg-slate-800 border border-slate-700 rounded-xl px-3 py-2 text-white focus:outline-none focus:border-emerald-500"
              />
            </div>

            <div>
              <label className="block text-slate-300 font-medium mb-1">Ajratilgan maydon (gektar):</label>
              <input
                type="number"
                step="0.05"
                min="0.1"
                max="5"
                value={allocatedAreaHa}
                onChange={(e) => setAllocatedAreaHa(e.target.value)}
                className="w-full bg-slate-800 border border-slate-700 rounded-xl px-3 py-2 text-white focus:outline-none focus:border-emerald-500"
              />
            </div>

            <div className="sm:col-span-2">
              <label className="block text-slate-300 font-medium mb-1">Xonadon egasi (F.I.Sh.):</label>
              <input
                type="text"
                required
                value={farmerName}
                onChange={(e) => setFarmerName(e.target.value)}
                placeholder="Masalan: Aliyev Botir Olimovich"
                className="w-full bg-slate-800 border border-slate-700 rounded-xl px-3 py-2 text-white focus:outline-none focus:border-emerald-500"
              />
            </div>

            <div>
              <label className="block text-slate-300 font-medium mb-1">Ijtimoiy toifasi:</label>
              <select
                value={familyStatus}
                onChange={(e) => setFamilyStatus(e.target.value)}
                className="w-full bg-slate-800 border border-slate-700 rounded-xl px-3 py-2 text-white focus:outline-none focus:border-emerald-500"
              >
                <option value="Ijtimoiy himoya reyestrida">Ijtimoiy himoya reyestrida</option>
                <option value="Temir daftar">Temir daftar</option>
                <option value="Ayollar daftari">Ayollar daftari</option>
                <option value="Yoshlar daftari">Yoshlar daftari</option>
              </select>
            </div>

            <div>
              <label className="block text-slate-300 font-medium mb-1">Tavsiya etilgan ekin:</label>
              <input
                type="text"
                value={primaryCrop}
                onChange={(e) => setPrimaryCrop(e.target.value)}
                className="w-full bg-slate-800 border border-slate-700 rounded-xl px-3 py-2 text-white focus:outline-none focus:border-emerald-500"
              />
            </div>

            <div>
              <label className="block text-slate-300 font-medium mb-1">Tuproq ball boniteti (0-100):</label>
              <input
                type="number"
                min="30"
                max="95"
                value={bonitetScore}
                onChange={(e) => setBonitetScore(e.target.value)}
                className="w-full bg-slate-800 border border-slate-700 rounded-xl px-3 py-2 text-white focus:outline-none focus:border-emerald-500"
              />
            </div>

            <div>
              <label className="block text-slate-300 font-medium mb-1">Kutilayotgan sof foyda (mln so'm):</label>
              <input
                type="number"
                min="5"
                max="150"
                value={netProfitMln}
                onChange={(e) => setNetProfitMln(e.target.value)}
                className="w-full bg-slate-800 border border-slate-700 rounded-xl px-3 py-2 text-white focus:outline-none focus:border-emerald-500"
              />
            </div>
          </div>

          <div className="p-3 bg-emerald-500/10 border border-emerald-500/30 rounded-xl text-xs text-emerald-300 flex items-center gap-2">
            <span>ℹ️</span>
            <span>Ushbu yer maydoni xaritada avtomatik koordinata va yashil kontur bilan ko'rsatiladi.</span>
          </div>

          {/* Footer Submit */}
          <div className="pt-3 border-t border-slate-800 flex justify-end gap-2">
            <button
              type="button"
              onClick={onClose}
              className="px-4 py-2 bg-slate-800 hover:bg-slate-700 text-white rounded-xl text-xs font-medium transition"
            >
              Bekor qilish
            </button>
            <button
              type="submit"
              className="px-5 py-2 bg-emerald-600 hover:bg-emerald-500 text-white rounded-xl text-xs font-bold shadow-lg shadow-emerald-600/30 transition active:scale-95 flex items-center gap-1.5"
            >
              <PlusCircle className="w-4 h-4" />
              <span>Yer maydonini kiritish</span>
            </button>
          </div>
        </form>
      </div>
    </div>
  );
}
