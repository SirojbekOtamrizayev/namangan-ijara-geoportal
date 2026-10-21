import React, { useState, useRef } from 'react';
import { 
  X, 
  Upload, 
  Download, 
  FileSpreadsheet, 
  PlusCircle, 
  Table, 
  CheckCircle2, 
  AlertCircle, 
  Trash2, 
  Search, 
  Sparkles,
  TrendingUp,
  Droplets,
  Sprout,
  DollarSign,
  UserCheck,
  Building2
} from 'lucide-react';
import { DISTRICTS_DATA } from '../data/namanganData';
import { 
  downloadSampleExcel, 
  parseUploadedExcel, 
  exportDataToExcel 
} from '../utils/excelHandler';

export default function DataManagerModal({
  isOpen,
  onClose,
  districts,
  onBatchImport,
  onAddSingleParcel
}) {
  if (!isOpen) return null;

  const [activeTab, setActiveTab] = useState('import'); // 'import' | 'manual' | 'table'
  const [fileLoading, setFileLoading] = useState(false);
  const [previewRows, setPreviewRows] = useState([]);
  const [importSuccessMsg, setImportSuccessMsg] = useState('');
  const [errorMessage, setErrorMessage] = useState('');
  const fileInputRef = useRef(null);

  // Manual entry form state
  const [selectedDistrictId, setSelectedDistrictId] = useState(DISTRICTS_DATA[0].id);
  const [mfyName, setMfyName] = useState('');
  const [farmerName, setFarmerName] = useState('');
  const [privilege, setPrivilege] = useState("Ijtimoiy himoya reyestrida");
  const [familyMembers, setFamilyMembers] = useState(5);
  const [allocatedAreaHa, setAllocatedAreaHa] = useState(0.5);
  const [contourNumber, setContourNumber] = useState('');
  const [specialization, setSpecialization] = useState('Ertapishar sabzavotchilik klasteri');
  const [moisture, setMoisture] = useState('72% (Optimal namlik)');
  const [waterSource, setWaterSource] = useState('Kafolatlangan oqim ariq suvi');
  const [bonitetScore, setBonitetScore] = useState(75);
  const [soilType, setSoilType] = useState("Sug'oriladigan o'tloqi bo'z tuproq");
  const [primaryCrop, setPrimaryCrop] = useState('Ertapishar sabzi, pomidor, baqlajon');
  const [netProfitMln, setNetProfitMln] = useState(36.5);

  // Table search & filter
  const [tableSearch, setTableSearch] = useState('');
  const [tableDistrictFilter, setTableDistrictFilter] = useState('all');

  // Handle File Upload & Parse
  const handleFileUpload = async (e) => {
    const file = e.target.files?.[0];
    if (!file) return;

    setFileLoading(true);
    setErrorMessage('');
    setImportSuccessMsg('');

    try {
      const rows = await parseUploadedExcel(file);
      setPreviewRows(rows);
    } catch (err) {
      setErrorMessage(`Faylni o'qishda xatolik: ${err.message}`);
    } finally {
      setFileLoading(false);
    }
  };

  // Commit batch import to system
  const handleCommitImport = () => {
    if (previewRows.length === 0) return;

    onBatchImport(previewRows);
    setImportSuccessMsg(`Muvaffaqiyatli! ${previewRows.length} ta xonadon ma'lumotlari tuman va MFYlar bo'yicha taqsimlandi va raqamlar qayta hisoblandi.`);
    setPreviewRows([]);
    setTimeout(() => {
      setActiveTab('table');
    }, 1500);
  };

  // Handle Manual Form Submit
  const handleManualSubmit = (e) => {
    e.preventDefault();
    if (!farmerName || !contourNumber || !mfyName) {
      alert("Iltimos, barcha majburiy maydonlarni to'ldiring!");
      return;
    }

    const dist = DISTRICTS_DATA.find(d => d.id === selectedDistrictId);
    const latOffset = (Math.random() - 0.5) * 0.02;
    const lngOffset = (Math.random() - 0.5) * 0.02;
    const baseLat = (dist?.center[0] || 40.99) + latOffset;
    const baseLng = (dist?.center[1] || 71.67) + lngOffset;

    const newRecord = {
      rowId: `MANUAL-${Date.now()}`,
      rawDistrict: dist?.name || "Pop tumani",
      districtId: selectedDistrictId,
      mfyName: mfyName.trim(),
      farmerName: farmerName.trim(),
      privilege: privilege,
      familyMembers: Number(familyMembers),
      allocatedAreaHa: Number(allocatedAreaHa),
      contourNumber: contourNumber.includes("kontur") ? contourNumber : `${contourNumber}-kontur`,
      specialization: specialization,
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
        groundwaterDepth: "1.8 metr",
        waterSource: waterSource
      },
      recommendation: {
        primaryCrop: primaryCrop,
        secondaryCrop: "Dukkakli mosh va ko'katlar",
        rationale: `${soilType} va ${moisture} namlik sharoitida yuqori hosil beradi.`,
        cycleMonths: "Aprel - Noyabr"
      },
      economics: {
        expensesUzs: Math.round(Number(netProfitMln) * 1000000 * 0.2),
        expectedYield: `${Math.round(Number(allocatedAreaHa) * 26)} tonna`,
        grossRevenueUzs: Math.round(Number(netProfitMln) * 1000000 * 1.25),
        netProfitUzs: Math.round(Number(netProfitMln) * 1000000),
        paybackMonths: 3.5
      }
    };

    onBatchImport([newRecord]);
    alert(`${farmerName} ma'lumotlari ${dist?.name}ga muvaffaqiyatli qo'shildi!`);
    setFarmerName('');
    setContourNumber('');
    setActiveTab('table');
  };

  // Compile all parcels across all districts for the table view
  const allParcelsList = [];
  let totalAreaSum = 0;
  let totalProfitSum = 0;

  districts.forEach(d => {
    d.mfys?.forEach(m => {
      m.parcels?.forEach(p => {
        totalAreaSum += p.allocatedAreaHa || 0;
        totalProfitSum += (p.economics?.netProfitUzs || 0);

        allParcelsList.push({
          districtName: d.name,
          districtId: d.id,
          mfyName: m.name,
          parcel: p
        });
      });
    });
  });

  // Filter table
  const filteredParcels = allParcelsList.filter(item => {
    const q = tableSearch.toLowerCase();
    const matchSearch = 
      item.districtName.toLowerCase().includes(q) ||
      item.mfyName.toLowerCase().includes(q) ||
      item.parcel.farmerName.toLowerCase().includes(q) ||
      item.parcel.familyStatus?.toLowerCase().includes(q) ||
      item.parcel.contourNumber.toLowerCase().includes(q) ||
      item.parcel.recommendation.primaryCrop.toLowerCase().includes(q);

    const matchDistrict = tableDistrictFilter === 'all' || item.districtId === tableDistrictFilter;
    return matchSearch && matchDistrict;
  });

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-2 sm:p-4 bg-slate-950/85 backdrop-blur-md animate-in fade-in">
      <div className="bg-slate-900 border border-slate-700/80 rounded-3xl w-full max-w-5xl max-h-[94vh] overflow-hidden flex flex-col shadow-2xl text-white">
        
        {/* Header */}
        <div className="p-4 sm:p-5 border-b border-slate-800 bg-gradient-to-r from-emerald-950/70 via-slate-900 to-slate-900 flex items-center justify-between gap-4">
          <div className="flex items-center gap-3">
            <div className="w-11 h-11 rounded-2xl bg-emerald-500/20 border border-emerald-500/40 flex items-center justify-center text-emerald-400 font-bold text-xl shadow-inner">
              <FileSpreadsheet className="w-6 h-6 text-emerald-400" />
            </div>
            <div>
              <h2 className="text-base sm:text-lg font-black text-white flex items-center gap-2">
                <span>Tuman va MFYlar Kesimida Ma'lumot Kiritish Markazi</span>
                <span className="bg-emerald-500/20 text-emerald-300 text-[10px] font-bold px-2.5 py-0.5 rounded-full border border-emerald-500/40">
                  EXCEL & BAZA
                </span>
              </h2>
              <p className="text-xs text-slate-400">
                Xonadon egalari, imtiyoz toifalari, yer namligi, ixtisoslashuvi, sabzavotlar va daromadlar hisobi
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

        {/* Navigation Tabs */}
        <div className="px-5 pt-3 bg-slate-900 border-b border-slate-800 flex items-center gap-2">
          <button
            onClick={() => setActiveTab('import')}
            className={`flex items-center gap-2 px-4 py-2.5 rounded-t-xl text-xs font-bold transition border-b-2 ${
              activeTab === 'import'
                ? 'bg-slate-800 text-emerald-400 border-emerald-500'
                : 'text-slate-400 hover:text-white border-transparent'
            }`}
          >
            <Upload className="w-4 h-4" />
            <span>Excel / Fayldan yuklash</span>
          </button>

          <button
            onClick={() => setActiveTab('manual')}
            className={`flex items-center gap-2 px-4 py-2.5 rounded-t-xl text-xs font-bold transition border-b-2 ${
              activeTab === 'manual'
                ? 'bg-slate-800 text-emerald-400 border-emerald-500'
                : 'text-slate-400 hover:text-white border-transparent'
            }`}
          >
            <PlusCircle className="w-4 h-4" />
            <span>Yakka tartibda kiritish</span>
          </button>

          <button
            onClick={() => setActiveTab('table')}
            className={`flex items-center gap-2 px-4 py-2.5 rounded-t-xl text-xs font-bold transition border-b-2 ${
              activeTab === 'table'
                ? 'bg-slate-800 text-emerald-400 border-emerald-500'
                : 'text-slate-400 hover:text-white border-transparent'
            }`}
          >
            <Table className="w-4 h-4" />
            <span>Barcha kiritilgan yerlar ro'yxati ({allParcelsList.length})</span>
          </button>
        </div>

        {/* Tab 1: Excel Import */}
        {activeTab === 'import' && (
          <div className="flex-1 overflow-y-auto p-5 space-y-4">
            
            {/* Download Template Banner */}
            <div className="bg-gradient-to-r from-emerald-950/60 via-slate-850 to-slate-850 border border-emerald-500/40 rounded-2xl p-4 flex flex-col sm:flex-row items-center justify-between gap-4 shadow-lg">
              <div>
                <h4 className="font-bold text-white text-sm flex items-center gap-2">
                  <Sparkles className="w-4 h-4 text-emerald-400" />
                  <span>Tayyor Excel shablonini yuklab oling</span>
                </h4>
                <p className="text-xs text-slate-300 mt-1">
                  Ushbu shablonda barcha ustunlar (Tuman, MFY, Imtiyoz toifasi, Namlik, Suv ta'minoti, Sabzavotlar, Daromad) to'liq shakllantirilgan.
                </p>
              </div>

              <button
                onClick={downloadSampleExcel}
                className="flex items-center gap-2 px-4 py-2 bg-emerald-600 hover:bg-emerald-500 text-white rounded-xl text-xs font-bold shadow-lg shadow-emerald-600/30 transition shrink-0"
              >
                <Download className="w-4 h-4" />
                <span>Namuna shablonni yuklab olish (.xlsx)</span>
              </button>
            </div>

            {/* Drag & Drop Upload Zone */}
            <div 
              onClick={() => fileInputRef.current?.click()}
              className="border-2 border-dashed border-slate-700 hover:border-emerald-500 rounded-3xl p-8 text-center cursor-pointer bg-slate-850/50 hover:bg-slate-800/80 transition-all duration-200"
            >
              <input
                ref={fileInputRef}
                type="file"
                accept=".xlsx, .xls, .csv"
                onChange={handleFileUpload}
                className="hidden"
              />

              <div className="w-14 h-14 rounded-2xl bg-emerald-500/10 border border-emerald-500/30 flex items-center justify-center text-emerald-400 mx-auto mb-3">
                <Upload className="w-7 h-7" />
              </div>

              <h3 className="font-extrabold text-base text-white">
                Excel (.xlsx, .xls) yoki CSV faylingizni shu yerga tashlang
              </h3>
              <p className="text-xs text-slate-400 mt-1 max-w-md mx-auto">
                Faylni yuklaganingizda dastur har bir xonadonni o'z tumaniga va MFY siga avtomatik taqsimlaydi va statistikalarni qayta aylantiradi.
              </p>
              <button
                type="button"
                className="mt-4 px-5 py-2 bg-slate-800 hover:bg-slate-700 text-slate-200 rounded-xl text-xs font-bold border border-slate-700"
              >
                Kompyuterdan fayl tanlash
              </button>
            </div>

            {/* Success / Error Messages */}
            {importSuccessMsg && (
              <div className="p-3 bg-emerald-500/20 border border-emerald-500/50 rounded-2xl text-xs text-emerald-300 flex items-center gap-2">
                <CheckCircle2 className="w-5 h-5 text-emerald-400 shrink-0" />
                <span>{importSuccessMsg}</span>
              </div>
            )}

            {errorMessage && (
              <div className="p-3 bg-rose-500/20 border border-rose-500/50 rounded-2xl text-xs text-rose-300 flex items-center gap-2">
                <AlertCircle className="w-5 h-5 text-rose-400 shrink-0" />
                <span>{errorMessage}</span>
              </div>
            )}

            {/* Preview of Parsed Rows */}
            {previewRows.length > 0 && (
              <div className="bg-slate-850 rounded-2xl p-4 border border-slate-700 space-y-3">
                <div className="flex items-center justify-between">
                  <div className="font-bold text-sm text-white flex items-center gap-2">
                    <CheckCircle2 className="w-4 h-4 text-emerald-400" />
                    <span>Yuklangan fayldan {previewRows.length} ta xonadon aniqlandi:</span>
                  </div>

                  <button
                    onClick={handleCommitImport}
                    className="flex items-center gap-2 px-5 py-2 bg-emerald-600 hover:bg-emerald-500 text-white rounded-xl text-xs font-black shadow-lg shadow-emerald-600/30 transition active:scale-95"
                  >
                    <span>Tizimga yuklash va raqamlarni yangilash ➔</span>
                  </button>
                </div>

                <div className="overflow-x-auto max-h-60 rounded-xl border border-slate-750">
                  <table className="w-full text-left text-[11px] text-slate-300">
                    <thead className="bg-slate-900 text-slate-400 uppercase font-bold sticky top-0">
                      <tr>
                        <th className="p-2.5">Tuman</th>
                        <th className="p-2.5">MFY</th>
                        <th className="p-2.5">Xonadon egasi</th>
                        <th className="p-2.5">Imtiyoz toifasi</th>
                        <th className="p-2.5">Maydon (ga)</th>
                        <th className="p-2.5">Yer namligi</th>
                        <th className="p-2.5">Tavsiya sabzavot</th>
                        <th className="p-2.5">Sof daromad</th>
                      </tr>
                    </thead>
                    <tbody className="divide-y divide-slate-800">
                      {previewRows.map((r, i) => (
                        <tr key={r.rowId || i} className="hover:bg-slate-800/60">
                          <td className="p-2.5 font-bold text-white">{r.rawDistrict}</td>
                          <td className="p-2.5 text-emerald-300 font-semibold">{r.mfyName}</td>
                          <td className="p-2.5">{r.farmerName}</td>
                          <td className="p-2.5 text-amber-300">{r.privilege}</td>
                          <td className="p-2.5 font-mono">{r.allocatedAreaHa} ga</td>
                          <td className="p-2.5 text-sky-300">{r.soil?.moisture}</td>
                          <td className="p-2.5 font-medium text-white">{r.recommendation?.primaryCrop}</td>
                          <td className="p-2.5 font-bold text-amber-400">+{(r.economics?.netProfitUzs / 1000000).toFixed(1)} mln</td>
                        </tr>
                      ))}
                    </tbody>
                  </table>
                </div>
              </div>
            )}
          </div>
        )}

        {/* Tab 2: Manual Form Entry */}
        {activeTab === 'manual' && (
          <form onSubmit={handleManualSubmit} className="flex-1 overflow-y-auto p-5 space-y-4">
            <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-3 text-xs">
              
              {/* 1. Tuman */}
              <div>
                <label className="block text-slate-300 font-bold mb-1">Tuman / Shahar:</label>
                <select
                  value={selectedDistrictId}
                  onChange={(e) => setSelectedDistrictId(e.target.value)}
                  className="w-full bg-slate-800 border border-slate-700 rounded-xl px-3 py-2 text-white focus:outline-none focus:border-emerald-500 font-medium"
                >
                  {DISTRICTS_DATA.map(d => (
                    <option key={d.id} value={d.id}>#{d.number} {d.name}</option>
                  ))}
                </select>
              </div>

              {/* 2. MFY */}
              <div>
                <label className="block text-slate-300 font-bold mb-1">MFY (Mahalla) nomi:</label>
                <input
                  type="text"
                  required
                  value={mfyName}
                  onChange={(e) => setMfyName(e.target.value)}
                  placeholder="Masalan: Shohand MFY"
                  className="w-full bg-slate-800 border border-slate-700 rounded-xl px-3 py-2 text-white focus:outline-none focus:border-emerald-500"
                />
              </div>

              {/* 3. Xonadon egasi */}
              <div>
                <label className="block text-slate-300 font-bold mb-1">Xonadon egasi (F.I.Sh.):</label>
                <input
                  type="text"
                  required
                  value={farmerName}
                  onChange={(e) => setFarmerName(e.target.value)}
                  placeholder="Masalan: Karimov Anvar Jo'rayevich"
                  className="w-full bg-slate-800 border border-slate-700 rounded-xl px-3 py-2 text-white focus:outline-none focus:border-emerald-500"
                />
              </div>

              {/* 4. Imtiyoz toifasi */}
              <div>
                <label className="block text-slate-300 font-bold mb-1">Qanday imtiyozlarga ega?:</label>
                <select
                  value={privilege}
                  onChange={(e) => setPrivilege(e.target.value)}
                  className="w-full bg-slate-800 border border-slate-700 rounded-xl px-3 py-2 text-white focus:outline-none focus:border-emerald-500"
                >
                  <option value="Ijtimoiy himoya reyestrida">Ijtimoiy himoya reyestrida</option>
                  <option value="Boquvchisini yo'qotgan oila">Boquvchisini yo'qotgan oila</option>
                  <option value="Temir daftar ro'yxatida">Temir daftar</option>
                  <option value="Ayollar daftari (ko'p bolali)">Ayollar daftari</option>
                  <option value="Yoshlar daftari">Yoshlar daftari</option>
                  <option value="Nogironligi bor oila a'zosi">Nogironligi bor oila a'zosi</option>
                </select>
              </div>

              {/* 5. Maydon (ga) */}
              <div>
                <label className="block text-slate-300 font-bold mb-1">Ajratilgan maydon (gektar):</label>
                <input
                  type="number"
                  step="0.05"
                  min="0.1"
                  max="10"
                  value={allocatedAreaHa}
                  onChange={(e) => setAllocatedAreaHa(e.target.value)}
                  className="w-full bg-slate-800 border border-slate-700 rounded-xl px-3 py-2 text-white focus:outline-none focus:border-emerald-500"
                />
              </div>

              {/* 6. Kontur raqami */}
              <div>
                <label className="block text-slate-300 font-bold mb-1">Dala kontur raqami:</label>
                <input
                  type="text"
                  required
                  value={contourNumber}
                  onChange={(e) => setContourNumber(e.target.value)}
                  placeholder="Masalan: 34-kontur"
                  className="w-full bg-slate-800 border border-slate-700 rounded-xl px-3 py-2 text-white focus:outline-none focus:border-emerald-500"
                />
              </div>

              {/* 7. Nimaga ixtisoslashgan */}
              <div>
                <label className="block text-slate-300 font-bold mb-1">Yer nimaga ixtisoslashgan?:</label>
                <input
                  type="text"
                  value={specialization}
                  onChange={(e) => setSpecialization(e.target.value)}
                  placeholder="Masalan: Ertapishar sabzavotchilik"
                  className="w-full bg-slate-800 border border-slate-700 rounded-xl px-3 py-2 text-white focus:outline-none focus:border-emerald-500"
                />
              </div>

              {/* 8. Yer namligi */}
              <div>
                <label className="block text-slate-300 font-bold mb-1">Yerning namlik darajasi:</label>
                <input
                  type="text"
                  value={moisture}
                  onChange={(e) => setMoisture(e.target.value)}
                  placeholder="Masalan: 72% (Optimal namlik)"
                  className="w-full bg-slate-800 border border-slate-700 rounded-xl px-3 py-2 text-white focus:outline-none focus:border-emerald-500"
                />
              </div>

              {/* 9. Suv ta'minoti */}
              <div>
                <label className="block text-slate-300 font-bold mb-1">Suv ta'minoti manbai:</label>
                <input
                  type="text"
                  value={waterSource}
                  onChange={(e) => setWaterSource(e.target.value)}
                  placeholder="Masalan: Shimoliy Farg'ona kanali"
                  className="w-full bg-slate-800 border border-slate-700 rounded-xl px-3 py-2 text-white focus:outline-none focus:border-emerald-500"
                />
              </div>

              {/* 10. Tuproq unumdorligi (ball) */}
              <div>
                <label className="block text-slate-300 font-bold mb-1">Tuproq ball boniteti (0-100):</label>
                <input
                  type="number"
                  min="30"
                  max="95"
                  value={bonitetScore}
                  onChange={(e) => setBonitetScore(e.target.value)}
                  className="w-full bg-slate-800 border border-slate-700 rounded-xl px-3 py-2 text-white focus:outline-none focus:border-emerald-500"
                />
              </div>

              {/* 11. Nima sabzavotlar eksa bo'ladi */}
              <div className="sm:col-span-2">
                <label className="block text-slate-300 font-bold mb-1">Nima sabzavot/ekin eksa bo'ladi?:</label>
                <input
                  type="text"
                  value={primaryCrop}
                  onChange={(e) => setPrimaryCrop(e.target.value)}
                  placeholder="Masalan: Ertapishar sabzi, pomidor, baqlajon, mosh"
                  className="w-full bg-slate-800 border border-slate-700 rounded-xl px-3 py-2 text-white focus:outline-none focus:border-emerald-500"
                />
              </div>

              {/* 12. Qancha daromad oladi */}
              <div>
                <label className="block text-slate-300 font-bold mb-1">Kutiladigan sof daromad (mln so'm):</label>
                <input
                  type="number"
                  step="0.5"
                  value={netProfitMln}
                  onChange={(e) => setNetProfitMln(e.target.value)}
                  className="w-full bg-slate-800 border border-slate-700 rounded-xl px-3 py-2 text-white focus:outline-none focus:border-emerald-500 font-bold text-amber-300"
                />
              </div>

            </div>

            <div className="pt-3 border-t border-slate-800 flex justify-end gap-2">
              <button
                type="button"
                onClick={onClose}
                className="px-4 py-2 bg-slate-800 text-slate-300 rounded-xl text-xs font-semibold"
              >
                Bekor qilish
              </button>

              <button
                type="submit"
                className="px-5 py-2 bg-emerald-600 hover:bg-emerald-500 text-white rounded-xl text-xs font-black shadow-lg shadow-emerald-600/30 flex items-center gap-1.5"
              >
                <PlusCircle className="w-4 h-4" />
                <span>Baza va xaritaga qo'shish</span>
              </button>
            </div>
          </form>
        )}

        {/* Tab 3: Full Table View with Search & Live Stats */}
        {activeTab === 'table' && (
          <div className="flex-1 overflow-y-auto p-5 space-y-4">
            {/* Live Stats Header ("Aniq sifiralar aylansin") */}
            <div className="grid grid-cols-2 sm:grid-cols-4 gap-3 text-xs">
              <div className="bg-slate-850 p-3 rounded-2xl border border-slate-750">
                <div className="text-[10px] text-slate-400 font-bold uppercase">Jami xonadonlar:</div>
                <div className="text-xl font-black text-emerald-400 mt-1">
                  {allParcelsList.length} ta oila
                </div>
              </div>

              <div className="bg-slate-850 p-3 rounded-2xl border border-slate-750">
                <div className="text-[10px] text-slate-400 font-bold uppercase">Jami ijara maydon:</div>
                <div className="text-xl font-black text-sky-400 mt-1">
                  {totalAreaSum.toFixed(1)} gektar
                </div>
              </div>

              <div className="bg-slate-850 p-3 rounded-2xl border border-slate-750">
                <div className="text-[10px] text-slate-400 font-bold uppercase">Kutiladigan sof foyda:</div>
                <div className="text-xl font-black text-amber-300 mt-1">
                  {(totalProfitSum / 1000000).toFixed(1)} mln so'm
                </div>
              </div>

              <div className="bg-slate-850 p-3 rounded-2xl border border-slate-750 flex items-center justify-center">
                <button
                  onClick={() => exportDataToExcel(districts)}
                  className="w-full h-full flex items-center justify-center gap-1.5 bg-emerald-600/20 hover:bg-emerald-600/30 text-emerald-300 border border-emerald-500/40 rounded-xl font-bold text-xs transition"
                >
                  <Download className="w-4 h-4" />
                  <span>Excelga eksport (.xlsx)</span>
                </button>
              </div>
            </div>

            {/* Filter & Search Bar */}
            <div className="flex flex-col sm:flex-row items-center gap-3">
              <div className="relative flex-1 w-full">
                <Search className="w-4 h-4 absolute left-3 top-1/2 -translate-y-1/2 text-slate-400" />
                <input
                  type="text"
                  value={tableSearch}
                  onChange={(e) => setTableSearch(e.target.value)}
                  placeholder="Xonadon egasi, MFY, imtiyoz yoki sabzavot bo'yicha qidirish..."
                  className="w-full bg-slate-800 border border-slate-700 rounded-xl pl-9 pr-3 py-2 text-xs text-white focus:outline-none focus:border-emerald-500"
                />
              </div>

              <select
                value={tableDistrictFilter}
                onChange={(e) => setTableDistrictFilter(e.target.value)}
                className="bg-slate-800 border border-slate-700 rounded-xl px-3 py-2 text-xs text-white focus:outline-none focus:border-emerald-500 font-semibold w-full sm:w-auto"
              >
                <option value="all">Barcha 14 ta tuman</option>
                {DISTRICTS_DATA.map(d => (
                  <option key={d.id} value={d.id}>#{d.number} {d.name}</option>
                ))}
              </select>
            </div>

            {/* Main Interactive Table */}
            <div className="overflow-x-auto rounded-2xl border border-slate-750">
              <table className="w-full text-left text-xs text-slate-300">
                <thead className="bg-slate-900 text-slate-400 uppercase font-bold text-[10px] tracking-wider sticky top-0">
                  <tr>
                    <th className="p-3">Tuman va MFY</th>
                    <th className="p-3">Xonadon egasi</th>
                    <th className="p-3">Imtiyoz toifasi</th>
                    <th className="p-3">Ixtisoslashuvi</th>
                    <th className="p-3">Yer namligi</th>
                    <th className="p-3">Maydon</th>
                    <th className="p-3">Tavsiya sabzavot</th>
                    <th className="p-3 text-right">Sof daromad</th>
                  </tr>
                </thead>
                <tbody className="divide-y divide-slate-800">
                  {filteredParcels.map((item, idx) => {
                    const p = item.parcel;
                    return (
                      <tr key={p.id || idx} className="hover:bg-slate-800/50 transition">
                        <td className="p-3">
                          <div className="font-bold text-white">{item.districtName}</div>
                          <div className="text-[11px] text-emerald-400">{item.mfyName} • {p.contourNumber}</div>
                        </td>
                        <td className="p-3 font-semibold text-white">
                          {p.farmerName}
                          <div className="text-[10px] text-slate-400">{p.familyMembers || 5} kishi</div>
                        </td>
                        <td className="p-3">
                          <span className="inline-block px-2 py-0.5 rounded-md bg-amber-500/20 text-amber-300 border border-amber-500/30 text-[10px] font-semibold">
                            {p.familyStatus}
                          </span>
                        </td>
                        <td className="p-3 font-medium text-sky-300 text-[11px]">
                          {p.specialization || "Sabzavotchilik"}
                        </td>
                        <td className="p-3 text-[11px]">
                          <span className="text-white font-semibold">{p.soil.moisture.split(' ')[0]}</span>
                          <div className="text-[10px] text-slate-400 truncate max-w-[130px]">{p.soil.waterSource}</div>
                        </td>
                        <td className="p-3 font-mono font-bold text-white">
                          {p.allocatedAreaHa} ga
                        </td>
                        <td className="p-3 text-white font-medium max-w-[180px]">
                          {p.recommendation.primaryCrop}
                        </td>
                        <td className="p-3 text-right">
                          <div className="font-black text-amber-400 text-sm">
                            +{(p.economics.netProfitUzs / 1000000).toFixed(1)} mln
                          </div>
                          <div className="text-[10px] text-emerald-400 font-medium">
                            {p.economics.paybackMonths} oyda o'zini qoplaydi
                          </div>
                        </td>
                      </tr>
                    );
                  })}
                </tbody>
              </table>
            </div>

          </div>
        )}

        {/* Footer */}
        <div className="p-4 border-t border-slate-800 bg-slate-900 flex items-center justify-between text-xs">
          <div className="text-slate-400">
            Kiritilgan har bir xonadon avtomatik ravishda GIS xaritasida o'z MFY siga biriktiriladi.
          </div>
          <button
            onClick={onClose}
            className="px-5 py-2 bg-slate-800 hover:bg-slate-700 text-white rounded-xl font-bold transition"
          >
            Yopish
          </button>
        </div>

      </div>
    </div>
  );
}
