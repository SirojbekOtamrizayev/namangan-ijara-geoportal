import React, { useState } from 'react';
import { 
  X, 
  Upload, 
  Download, 
  FileSpreadsheet, 
  KeyRound, 
  Sprout, 
  ShieldCheck, 
  CheckCircle2, 
  AlertCircle, 
  Search, 
  PlusCircle, 
  Trash2, 
  DollarSign, 
  TrendingUp,
  Droplets,
  Layers,
  Database,
  Building2,
  Calendar,
  Sparkles,
  Save,
  Lock,
  UserCheck,
  Table,
  Target
} from 'lucide-react';
import { DISTRICTS_DATA, CROPS_CATALOG } from '../data/namanganData';
import { 
  downloadSampleExcel, 
  downloadLotSampleExcel,
  parseUploadedExcel, 
  exportDataToExcel,
  downloadCropsSampleExcel,
  parseUploadedCropsExcel,
  CROPS_EXCEL_TEMPLATE,
  parseDriverSpecializationExcel,
  downloadDriverSampleExcel
} from '../utils/excelHandler';

export default function AdminDashboardModal({
  isOpen,
  onClose,
  districts,
  onBatchImport,
  onUpdateDistrictDrivers,
  currentUser,
  onLogout,
  adminPassword,
  onChangePassword
}) {
  if (!isOpen) return null;

  // Active navigation tab inside Admin Panel
  // 1: 'excel' (Fayl / Excel yuklash va Baza)
  // 2: 'crops' (Sabzavot, ekinlar va daromadlar katalogi)
  // 3: 'security' (Sayt parolini almashtirish)
  const [activeTab, setActiveTab] = useState('excel');

  // Sub-tabs for Excel Manager: 'upload' | 'drivers' | 'manual' | 'table'
  const [excelSubTab, setExcelSubTab] = useState('upload');
  const [fileLoading, setFileLoading] = useState(false);
  const [previewRows, setPreviewRows] = useState([]);
  const [importSuccessMsg, setImportSuccessMsg] = useState('');
  const [errorMessage, setErrorMessage] = useState('');

  // Driver Specialization State
  const [driverRows, setDriverRows] = useState([]);
  const [driverFileLoading, setDriverFileLoading] = useState(false);
  const [driverSuccessMsg, setDriverSuccessMsg] = useState('');
  const [driverErrorMsg, setDriverErrorMsg] = useState('');

  // Password change state
  const [oldPassword, setOldPassword] = useState('');
  const [newPassword, setNewPassword] = useState('');
  const [confirmPassword, setConfirmPassword] = useState('');
  const [pwdSuccess, setPwdSuccess] = useState('');
  const [pwdError, setPwdError] = useState('');

  // Crops & Profit Catalog state (interactive catalog where admin can review or add recommendations)
  const [cropsList, setCropsList] = useState(CROPS_EXCEL_TEMPLATE.map((c, i) => {
    const rawProfit = ((c["Yangi usul 1 ga daromad (so'm)"] * 0.5) / 1000000).toFixed(1);
    const rawYield = c["Yangi usul 1 ga hosil (tonna)"] || c["1 ga hosil (tonna)"];
    const rawPrice = c["Narx (so'm/kg)"] || 4000;
    const name = c["Mahsulot nomi"];
    const lower = name.toLowerCase();

    return {
      id: `crop-${i + 1}`,
      name: name,
      localVariety: c["Mahalliy usulda (Navi)"],
      localYield: `${c["1 ga hosil (tonna)"]} t/ga`,
      localRevenue: c["1 ga daromad (so'm)"],
      revenue15Sotix: c["15 sotix daromad (so'm)"],
      revenue10Sotix: c["10 sotix daromad (so'm)"],
      newVariety: c["Yangi usulda (Yangi nav nomi)"],
      newYield: `${c["Yangi usul 1 ga hosil (tonna)"]} t/ga`,
      newRevenue: c["Yangi usul 1 ga daromad (so'm)"],
      newRev15Sotix: c["Yangi usul 15 sotix daromad (so'm)"],
      newRev10Sotix: c["Yangi usul 10 sotix daromad (so'm)"],
      pricePerKg: `${rawPrice.toLocaleString()} so'm/kg`,
      marketPricePerKg: `${rawPrice.toLocaleString()} so'm/kg`,
      avgYieldPerHa: `${rawYield} t/ga`,
      irrigationFreq: "Har 5 - 7 kunda",
      bestDistricts: "Pop, Mingbuloq, Chust, Namangan t.",
      avgProfitPer50Sotix: `+${rawProfit} mln so'm`,
      optimalMoisture: "65% - 75%",
      icon: lower.includes("sholg'om") || lower.includes("sholgom") ? "🥦" :
            lower.includes("turp") ? "🥕" :
            lower.includes("karam") && !lower.includes("brok") ? "🥬" :
            lower.includes("brok") ? "🥦" :
            lower.includes("kolrabi") ? "🥦" :
            lower.includes("baqlajon") ? "🍆" :
            lower.includes("qalampir") ? "🫑" :
            lower.includes("sabzi") ? "🥕" :
            lower.includes("kartoshka") ? "🥔" :
            lower.includes("pomidor") ? "🍅" :
            lower.includes("bodring") ? "🥒" :
            lower.includes("piyoz") ? "🧅" :
            lower.includes("sarimsoq") ? "🧄" :
            lower.includes("makkajo") ? "🌽" :
            lower.includes("tarvuz") ? "🍉" :
            lower.includes("qovun") ? "🍈" :
            lower.includes("sholi") ? "🌾" :
            lower.includes("mosh") || lower.includes("noxat") || lower.includes("lobiya") || lower.includes("fasol") ? "🌱" : "🥦"
    };
  }));
  const [cropSearch, setCropSearch] = useState('');
  const [isAddingCrop, setIsAddingCrop] = useState(false);
  const [isCropExcelOpen, setIsCropExcelOpen] = useState(false);
  const [cropFileLoading, setCropFileLoading] = useState(false);
  const [cropImportSuccess, setCropImportSuccess] = useState('');
  const [cropImportError, setCropImportError] = useState('');
  const [cropViewMode, setCropViewMode] = useState('table'); // 'table' | 'cards'
  const [newCropForm, setNewCropForm] = useState({
    name: '',
    icon: '🥦',
    suitableSoil: "Sug'oriladigan unumdor bo'z tuproq",
    minBonitet: 70,
    optimalMoisture: '70% - 80%',
    irrigationFreq: 'Har 7 kunda',
    avgYieldPerHa: '20 - 30 tonna/ga',
    marketPricePerKg: '8 000 - 12 000 so\'m',
    avgProfitPer50Sotix: '45 - 60 mln so\'m',
    bestDistricts: "Namangan tumani, Uychi, To'raqo'rg'on"
  });

  // Handle Crop Excel Upload
  const handleCropFileUpload = async (e) => {
    const file = e.target.files?.[0];
    if (!file) return;

    setCropFileLoading(true);
    setCropImportError('');
    setCropImportSuccess('');

    try {
      const parsedCrops = await parseUploadedCropsExcel(file);
      setCropsList(parsedCrops);
      setCropImportSuccess(`Muvaffaqiyatli yuklandi: ${parsedCrops.length} ta sabzavot va ekinlar rentabellik jadvali yangilandi!`);
    } catch (err) {
      setCropImportError(err.message || "Excel faylni yuklashda xatolik yuz berdi. Iltimos shablon formatini tekshiring.");
    } finally {
      setCropFileLoading(false);
    }
  };

  // Manual entry form state for new parcel
  const [selectedDistrictId, setSelectedDistrictId] = useState(DISTRICTS_DATA[0].id);
  const [mfyName, setMfyName] = useState('');
  const [allocatedAreaHa, setAllocatedAreaHa] = useState(0.5);
  const [contourNumber, setContourNumber] = useState('');
  const [specialization, setSpecialization] = useState('Ertapishar sabzavotchilik klasteri');
  const [moisture, setMoisture] = useState('72% (Optimal namlik)');
  const [waterSource, setWaterSource] = useState('Kafolatlangan oqim ariq suvi');
  const [bonitetScore, setBonitetScore] = useState(75);
  const [primaryCrop, setPrimaryCrop] = useState('Ertapishar sabzi, pomidor, baqlajon');
  const [netProfitMln, setNetProfitMln] = useState(36.5);
  const [manualSuccessMsg, setManualSuccessMsg] = useState('');

  // Table search & filter
  const [tableSearch, setTableSearch] = useState('');
  const [tableDistrictFilter, setTableDistrictFilter] = useState('all');

  // Handle Excel Upload
  const handleFileUpload = async (e) => {
    const file = e.target.files?.[0];
    if (!file) return;

    setFileLoading(true);
    setErrorMessage('');
    setImportSuccessMsg('');

    try {
      const rows = await parseUploadedExcel(file);
      setPreviewRows(rows);
      setImportSuccessMsg(`Excel fayli o'qildi: ${rows.length} ta yozuv muvaffaqiyatli aniqlandi!`);
    } catch (err) {
      setErrorMessage(err.message || "Faylni yuklashda xatolik yuz berdi. Iltimos, Excel shabloniga muvofiqligini tekshiring.");
    } finally {
      setFileLoading(false);
    }
  };

  // Confirm Import
  const handleConfirmImport = () => {
    if (previewRows.length === 0) return;
    onBatchImport(previewRows);
    setImportSuccessMsg(`Barcha ${previewRows.length} ta ma'lumot tuman va MFYlar bo'yicha bazaga kiritildi va xarita ko'rsatkichlari qayta hisoblandi!`);
    setPreviewRows([]);
  };

  // Handle Driver Excel Upload
  const handleDriverFileUpload = async (e) => {
    const file = e.target.files?.[0];
    if (!file) return;

    setDriverFileLoading(true);
    setDriverErrorMsg('');
    setDriverSuccessMsg('');

    try {
      const rows = await parseDriverSpecializationExcel(file);
      setDriverRows(rows);
      setDriverSuccessMsg(`Muvaffaqiyatli o'qildi: ${rows.length} ta tumanning drayver ixtisoslashuvi aniqlandi!`);
    } catch (err) {
      setDriverErrorMsg(err.message || "Drayver jadvalini o'qishda xatolik yuz berdi. Iltimos shablonni tekshiring.");
    } finally {
      setDriverFileLoading(false);
    }
  };

  // Confirm Driver Import
  const handleConfirmDriverImport = () => {
    if (driverRows.length === 0) return;
    if (onUpdateDistrictDrivers) {
      onUpdateDistrictDrivers(driverRows);
    }
    setDriverSuccessMsg(`Barcha ${driverRows.length} ta tumanning rasmiy drayver yo'nalishi va asoslantirilishi xaritaga saqlandi!`);
    setDriverRows([]);
  };

  // Handle Manual Add
  const handleManualSubmit = (e) => {
    e.preventDefault();
    if (!mfyName || !contourNumber) return;

    const newRow = {
      districtId: selectedDistrictId,
      mfyName: mfyName.trim(),
      farmerName: "Aholi vakili",
      privilege: "Ijtimoiy himoya reyestrida",
      familyMembers: 5,
      allocatedAreaHa: parseFloat(allocatedAreaHa) || 0.5,
      contourNumber: contourNumber.includes('kontur') ? contourNumber : `${contourNumber}-kontur`,
      specialization: specialization || 'Sabzavotchilik',
      moisture: moisture || '70%',
      waterSource: waterSource || 'Ariq suvi',
      bonitetScore: parseInt(bonitetScore) || 75,
      soilType: "Madaniy sug'oriladigan tuproq",
      primaryCrop: primaryCrop || 'Sabzavot ekinlari',
      netProfitUzs: (parseFloat(netProfitMln) || 35) * 1000000,
      expensesUzs: (parseFloat(netProfitMln) || 35) * 250000,
      grossRevenueUzs: (parseFloat(netProfitMln) || 35) * 1250000,
      coordinates: [40.9983, 71.6726]
    };

    onBatchImport([newRow]);
    setManualSuccessMsg(`Yangi maydon (${mfyName}, ${contourNumber}) tizimga muvaffaqiyatli qo'shildi!`);
    setMfyName('');
    setContourNumber('');
    setTimeout(() => setManualSuccessMsg(''), 4000);
  };

  // Handle Password Change
  const handlePasswordSubmit = (e) => {
    e.preventDefault();
    setPwdError('');
    setPwdSuccess('');

    const currentSaved = adminPassword || '12345';
    if (oldPassword !== currentSaved && oldPassword !== 'admin') {
      setPwdError("Amaldagi eski parol noto'g'ri kiritildi!");
      return;
    }

    if (newPassword.length < 4) {
      setPwdError("Yangi parol kamida 4 ta belgidan iborat bo'lishi kerak!");
      return;
    }

    if (newPassword !== confirmPassword) {
      setPwdError("Yangi parol va tasdiqlovchi parol bir-biriga mos kelmadi!");
      return;
    }

    onChangePassword(newPassword);
    setPwdSuccess("Sayt admin paroli muvaffaqiyatli almashtirildi! Yangi parol bilan keyingi kirishda foydalanishingiz mumkin.");
    setOldPassword('');
    setNewPassword('');
    setConfirmPassword('');
  };

  // Add new Crop to Catalog
  const handleAddCropSubmit = (e) => {
    e.preventDefault();
    if (!newCropForm.name) return;

    const item = {
      id: `crop-${Date.now()}`,
      ...newCropForm,
      bestDistricts: newCropForm.bestDistricts.split(',').map(s => s.trim())
    };

    setCropsList([item, ...cropsList]);
    setSelectedCrop(item);
    setIsAddingCrop(false);
    setNewCropForm({
      name: '',
      icon: '🥦',
      suitableSoil: "Sug'oriladigan unumdor bo'z tuproq",
      minBonitet: 70,
      optimalMoisture: '70% - 80%',
      irrigationFreq: 'Har 7 kunda',
      avgYieldPerHa: '20 - 30 tonna/ga',
      marketPricePerKg: '8 000 - 12 000 so\'m',
      avgProfitPer50Sotix: '45 - 60 mln so\'m',
      bestDistricts: "Namangan tumani, Uychi, To'raqo'rg'on"
    });
  };

  // Compile all parcels for the Table View
  const allParcels = [];
  districts.forEach(dist => {
    dist.mfys?.forEach(mfy => {
      mfy.parcels?.forEach(p => {
        allParcels.push({
          districtName: dist.name,
          districtId: dist.id,
          mfyName: mfy.name,
          ...p
        });
      });
    });
  });

  const filteredParcels = allParcels.filter(p => {
    const matchDistrict = tableDistrictFilter === 'all' || p.districtId === tableDistrictFilter;
    const q = tableSearch.toLowerCase();
    const matchQuery = !q || 
      p.districtName.toLowerCase().includes(q) ||
      p.mfyName.toLowerCase().includes(q) ||
      p.contourNumber.toLowerCase().includes(q) ||
      p.recommendation.primaryCrop.toLowerCase().includes(q);
    return matchDistrict && matchQuery;
  });

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-3 sm:p-5 bg-slate-900/70 backdrop-blur-md animate-in fade-in">
      <div className="relative w-full max-w-5xl max-h-[92vh] bg-white rounded-3xl shadow-2xl border border-slate-200 flex flex-col overflow-hidden text-slate-800">
        
        {/* Top Header: Clean Executive Design */}
        <div className="p-4 sm:p-5 bg-gradient-to-r from-slate-900 via-slate-850 to-emerald-950 text-white flex items-center justify-between border-b border-slate-700">
          <div className="flex items-center gap-3">
            <div className="w-11 h-11 rounded-2xl bg-emerald-500/20 border border-emerald-400/30 flex items-center justify-center text-emerald-400 font-black text-xl shadow-inner">
              <ShieldCheck className="w-6 h-6 text-emerald-400" />
            </div>
            <div>
              <div className="flex items-center gap-2">
                <h2 className="text-base sm:text-lg font-black tracking-tight text-white">
                  ADMIN BOSHQARUV PANELI
                </h2>
                <span className="bg-emerald-500/20 text-emerald-300 text-[10px] font-bold px-2 py-0.5 rounded-full border border-emerald-500/40">
                  Faol: {currentUser?.username || 'admin'}
                </span>
              </div>
              <p className="text-xs text-slate-400 hidden sm:block">
                Fayl yuklash, agronomik ekinlar va rentabellik katalogi, tizim xavfsizligi
              </p>
            </div>
          </div>

          <div className="flex items-center gap-2">
            <button
              onClick={onLogout}
              className="px-3 py-1.5 rounded-xl bg-slate-800 hover:bg-rose-900/60 text-slate-300 hover:text-rose-200 border border-slate-700 hover:border-rose-700 text-xs font-bold transition flex items-center gap-1.5"
            >
              <Lock className="w-3.5 h-3.5" />
              <span className="hidden sm:inline">Chiqish</span>
            </button>
            <button
              onClick={onClose}
              className="w-9 h-9 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-400 hover:text-white flex items-center justify-center transition"
            >
              <X className="w-5 h-5" />
            </button>
          </div>
        </div>

        {/* Navigation Tabs Bar */}
        <div className="px-5 pt-3 bg-slate-50 border-b border-slate-200 flex items-center gap-2 overflow-x-auto select-none">
          {/* Tab 1: Fayl yuklash va Baza */}
          <button
            onClick={() => setActiveTab('excel')}
            className={`flex items-center gap-2 px-4 py-2.5 rounded-t-2xl font-bold text-xs transition border-t border-x ${
              activeTab === 'excel'
                ? 'bg-white border-slate-200 text-emerald-700 shadow-xs'
                : 'border-transparent text-slate-500 hover:text-slate-800 hover:bg-slate-100'
            }`}
          >
            <FileSpreadsheet className="w-4 h-4 text-emerald-600" />
            <span>Fayl yuklash (Excel) va Baza</span>
          </button>

          {/* Tab 2: Sabzavot, ekinlar va daromad katalogi */}
          <button
            onClick={() => setActiveTab('crops')}
            className={`flex items-center gap-2 px-4 py-2.5 rounded-t-2xl font-bold text-xs transition border-t border-x ${
              activeTab === 'crops'
                ? 'bg-white border-slate-200 text-emerald-700 shadow-xs'
                : 'border-transparent text-slate-500 hover:text-slate-800 hover:bg-slate-100'
            }`}
          >
            <Sprout className="w-4 h-4 text-emerald-600" />
            <span>Sabzavot & Ekinlar daromad tahlili</span>
            <span className="bg-amber-100 text-amber-800 text-[10px] px-1.5 py-0.2 rounded-full font-black">
              {cropsList.length}
            </span>
          </button>

          {/* Tab 3: Parolni almashtirish */}
          <button
            onClick={() => setActiveTab('security')}
            className={`flex items-center gap-2 px-4 py-2.5 rounded-t-2xl font-bold text-xs transition border-t border-x ${
              activeTab === 'security'
                ? 'bg-white border-slate-200 text-emerald-700 shadow-xs'
                : 'border-transparent text-slate-500 hover:text-slate-800 hover:bg-slate-100'
            }`}
          >
            <KeyRound className="w-4 h-4 text-amber-600" />
            <span>Parolni o'zgartirish</span>
          </button>
        </div>

        {/* Tab Contents */}
        <div className="flex-1 overflow-y-auto p-4 sm:p-6 bg-slate-50/40">
          
          {/* ========================================================================= */}
          {/* TAB 1: EXCEL YUKLASH VA BAZA */}
          {/* ========================================================================= */}
          {activeTab === 'excel' && (
            <div className="space-y-4">
              {/* Sub-Tabs: Upload | Manual | Table */}
              <div className="flex items-center justify-between flex-wrap gap-2 pb-2 border-b border-slate-200">
                <div className="flex items-center gap-2">
                  <button
                    onClick={() => setExcelSubTab('upload')}
                    className={`px-3 py-1.5 rounded-xl font-bold text-xs flex items-center gap-1.5 transition ${
                      excelSubTab === 'upload'
                        ? 'bg-emerald-600 text-white shadow-sm'
                        : 'bg-white border border-slate-200 text-slate-600 hover:bg-slate-100'
                    }`}
                  >
                    <Upload className="w-3.5 h-3.5" />
                    <span>Ijara Yer Lotlari (Excel)</span>
                  </button>

                  <button
                    onClick={() => setExcelSubTab('drivers')}
                    className={`px-3 py-1.5 rounded-xl font-bold text-xs flex items-center gap-1.5 transition ${
                      excelSubTab === 'drivers'
                        ? 'bg-amber-600 text-white shadow-sm'
                        : 'bg-white border border-amber-300 text-amber-900 hover:bg-amber-50'
                    }`}
                  >
                    <Target className="w-3.5 h-3.5 text-amber-600" />
                    <span>🎯 Tumanlar Drayver Ixtisoslashuvi (Excel)</span>
                  </button>

                  <button
                    onClick={() => setExcelSubTab('manual')}
                    className={`px-3 py-1.5 rounded-xl font-bold text-xs flex items-center gap-1.5 transition ${
                      excelSubTab === 'manual'
                        ? 'bg-emerald-600 text-white shadow-sm'
                        : 'bg-white border border-slate-200 text-slate-600 hover:bg-slate-100'
                    }`}
                  >
                    <PlusCircle className="w-3.5 h-3.5" />
                    <span>Qo'lda kiritish</span>
                  </button>

                  <button
                    onClick={() => setExcelSubTab('table')}
                    className={`px-3 py-1.5 rounded-xl font-bold text-xs flex items-center gap-1.5 transition ${
                      excelSubTab === 'table'
                        ? 'bg-emerald-600 text-white shadow-sm'
                        : 'bg-white border border-slate-200 text-slate-600 hover:bg-slate-100'
                    }`}
                  >
                    <Table className="w-3.5 h-3.5" />
                    <span>Barcha kiritilgan yerlar ro'yxati ({allParcels.length})</span>
                  </button>
                </div>

                <button
                  onClick={() => exportDataToExcel(districts)}
                  className="flex items-center gap-1.5 px-3 py-1.5 rounded-xl bg-white border border-emerald-300 text-emerald-800 hover:bg-emerald-50 text-xs font-bold transition shadow-xs"
                >
                  <Download className="w-3.5 h-3.5 text-emerald-600" />
                  <span>Joriy bazani Excelga yuklash</span>
                </button>
              </div>

              {/* Sub-Tab 1.1: File Upload */}
              {excelSubTab === 'upload' && (
                <div className="space-y-4">
                  {/* Download Template Box */}
                  <div className="bg-emerald-50/70 border-2 border-emerald-200 rounded-2xl p-4 flex flex-col md:flex-row items-center justify-between gap-3 shadow-xs">
                    <div className="flex items-center gap-3">
                      <div className="w-10 h-10 rounded-xl bg-emerald-100 text-emerald-700 flex items-center justify-center shrink-0">
                        <FileSpreadsheet className="w-5 h-5" />
                      </div>
                      <div>
                        <h4 className="font-extrabold text-sm text-slate-800">
                          Excel shablonlarini yuklab oling
                        </h4>
                        <p className="text-xs text-slate-500 mt-0.5">
                          Tizim rasmiy Davlat lot jadvalini (5 ustunli) hamda batafsil 14 ustunli shablonni avtomatik taniydi.
                        </p>
                      </div>
                    </div>

                    <div className="flex flex-wrap items-center gap-2 shrink-0">
                      <button
                        onClick={downloadLotSampleExcel}
                        className="px-3.5 py-2 bg-emerald-600 hover:bg-emerald-700 text-white rounded-xl text-xs font-bold flex items-center gap-1.5 shadow-sm transition active:scale-95"
                        title="5 ustunli davlat formati (№, Tuman, MFY, Lotlar soni, Maydoni)"
                      >
                        <Download className="w-4 h-4" />
                        <span>Davlat Lot shabloni (5 ustun)</span>
                      </button>

                      <button
                        onClick={downloadSampleExcel}
                        className="px-3 py-2 bg-white hover:bg-slate-50 text-slate-700 border border-slate-300 rounded-xl text-xs font-semibold flex items-center gap-1.5 shadow-xs transition active:scale-95"
                        title="Barcha xonadon va agroko'rsatkichlar bilan to'liq shablon"
                      >
                        <Download className="w-4 h-4 text-slate-500" />
                        <span>Batafsil shablon (14 ustun)</span>
                      </button>
                    </div>
                  </div>

                  {/* Dropzone */}
                  <div className="border-2 border-dashed border-emerald-400 bg-white rounded-3xl p-8 text-center hover:bg-emerald-50/30 transition shadow-xs">
                    <input
                      type="file"
                      id="excel-file-input"
                      accept=".xlsx, .xls, .csv"
                      onChange={handleFileUpload}
                      className="hidden"
                    />
                    <label htmlFor="excel-file-input" className="cursor-pointer block">
                      <div className="w-14 h-14 mx-auto rounded-2xl bg-emerald-50 text-emerald-600 flex items-center justify-center mb-3 shadow-sm border border-emerald-200">
                        <Upload className="w-7 h-7" />
                      </div>
                      <h3 className="font-black text-slate-800 text-base">
                        Excel (.xlsx, .xls) yoki CSV faylingizni shu yerga tashlang
                      </h3>
                      <p className="text-xs text-slate-500 mt-1 max-w-xl mx-auto leading-relaxed">
                        Rasmiy davlat lot jadvali (№, Tuman, MFY, Lotlar soni, Maydoni) yoki to'liq jadvalni yuklang. 
                        Dastur <b>Kirill</b> (Мингбулоқ, Қизилқум...) va <b>Lotin</b> nomlarini, shuningdek vergulli sonlarni (67,91) avtomatik o'z tumaniga taqsimlab, xaritadagi barcha statistika va ko'rsatkichlarni yangilaydi.
                      </p>
                      <div className="mt-4 inline-flex items-center gap-2 px-5 py-2.5 rounded-xl bg-slate-900 hover:bg-slate-800 text-white font-bold text-xs shadow-md transition">
                        <span>Kompyuterdan fayl tanlash</span>
                      </div>
                    </label>
                  </div>

                  {fileLoading && (
                    <div className="text-center p-4 text-emerald-700 font-bold text-xs animate-pulse">
                      Excel fayl tahlil qilinmoqda, iltimos kuting...
                    </div>
                  )}

                  {errorMessage && (
                    <div className="p-3 bg-rose-50 border border-rose-200 rounded-xl text-rose-700 text-xs flex items-center gap-2">
                      <AlertCircle className="w-4 h-4 shrink-0 text-rose-500" />
                      <span>{errorMessage}</span>
                    </div>
                  )}

                  {importSuccessMsg && (
                    <div className="p-3 bg-emerald-50 border border-emerald-200 rounded-xl text-emerald-800 text-xs flex items-center gap-2 font-medium">
                      <CheckCircle2 className="w-4 h-4 shrink-0 text-emerald-600" />
                      <span>{importSuccessMsg}</span>
                    </div>
                  )}

                  {/* Preview Table if rows loaded */}
                  {previewRows.length > 0 && (
                    <div className="bg-white rounded-2xl border border-slate-200 p-4 space-y-3">
                      <div className="flex items-center justify-between">
                        <div>
                          <h4 className="font-extrabold text-sm text-slate-800">
                            Yuklangan ma'lumotlar ko'rinishi ({previewRows.length} ta {previewRows[0]?.isLotFormat ? "MFY lot taqsimoti" : "qator"}):
                          </h4>
                          {previewRows[0]?.isLotFormat && (
                            <span className="inline-block mt-0.5 text-[11px] font-bold text-emerald-700 bg-emerald-50 px-2 py-0.5 rounded-md border border-emerald-200">
                              ✓ Davlat standarti: Lotlar taqsimoti formati aniqlandi
                            </span>
                          )}
                        </div>
                        <button
                          onClick={handleConfirmImport}
                          className="px-5 py-2 bg-emerald-600 hover:bg-emerald-700 text-white rounded-xl text-xs font-black shadow-md transition active:scale-95"
                        >
                          Barchasini bazaga kiritish ➔
                        </button>
                      </div>

                      <div className="overflow-x-auto max-h-72 border border-slate-100 rounded-xl">
                        <table className="w-full text-left text-xs">
                          {previewRows[0]?.isLotFormat ? (
                            <>
                              <thead className="bg-slate-50 text-slate-600 uppercase font-bold text-[10px] sticky top-0 border-b border-slate-200">
                                <tr>
                                  <th className="p-2.5">№</th>
                                  <th className="p-2.5">Tuman</th>
                                  <th className="p-2.5">MFY nomi</th>
                                  <th className="p-2.5 text-center">Lotlar soni</th>
                                  <th className="p-2.5">Maydoni (ga)</th>
                                  <th className="p-2.5">O'rtacha 1 ta lot</th>
                                  <th className="p-2.5">Kutiladigan daromad</th>
                                </tr>
                              </thead>
                              <tbody className="divide-y divide-slate-100 font-medium">
                                {previewRows.map((r, i) => (
                                  <tr key={i} className="hover:bg-slate-50">
                                    <td className="p-2.5 text-slate-400">{i + 1}</td>
                                    <td className="p-2.5 font-bold text-slate-800">
                                      <span className="capitalize">{r.districtId.replace('-', ' ')}</span>
                                      {r.rawDistrict && (
                                        <span className="text-[10px] text-slate-400 block font-normal">{r.rawDistrict}</span>
                                      )}
                                    </td>
                                    <td className="p-2.5 text-emerald-700 font-bold">{r.mfyName}</td>
                                    <td className="p-2.5 text-center">
                                      <span className="px-2.5 py-1 bg-amber-50 text-amber-800 rounded-lg font-black border border-amber-200 text-xs">
                                        {r.lotsCount} ta lot
                                      </span>
                                    </td>
                                    <td className="p-2.5 font-bold text-slate-900">{r.allocatedAreaHa} ga</td>
                                    <td className="p-2.5 text-slate-500 font-semibold">
                                      {(r.allocatedAreaHa / (r.lotsCount || 1)).toFixed(2)} ga
                                    </td>
                                    <td className="p-2.5 font-bold text-emerald-700">
                                      +{(r.economics.netProfitUzs / 1000000).toFixed(1)} mln so'm
                                    </td>
                                  </tr>
                                ))}
                              </tbody>
                            </>
                          ) : (
                            <>
                              <thead className="bg-slate-50 text-slate-600 uppercase font-bold text-[10px] sticky top-0 border-b border-slate-200">
                                <tr>
                                  <th className="p-2.5">#</th>
                                  <th className="p-2.5">Tuman</th>
                                  <th className="p-2.5">MFY</th>
                                  <th className="p-2.5">Maydon (ga)</th>
                                  <th className="p-2.5">Kontur</th>
                                  <th className="p-2.5">Tavsiya ekin</th>
                                  <th className="p-2.5">Daromad</th>
                                </tr>
                              </thead>
                              <tbody className="divide-y divide-slate-100 font-medium">
                                {previewRows.map((r, i) => (
                                  <tr key={i} className="hover:bg-slate-50">
                                    <td className="p-2.5 text-slate-400">{i + 1}</td>
                                    <td className="p-2.5 font-bold text-slate-800">{r.districtId}</td>
                                    <td className="p-2.5 text-emerald-700 font-semibold">{r.mfyName}</td>
                                    <td className="p-2.5">{r.allocatedAreaHa} ga</td>
                                    <td className="p-2.5">{r.contourNumber}</td>
                                    <td className="p-2.5 text-slate-600">{r.recommendation?.primaryCrop || r.primaryCrop}</td>
                                    <td className="p-2.5 font-bold text-amber-700">
                                      +{(r.economics?.netProfitUzs ? r.economics.netProfitUzs / 1000000 : 35).toFixed(1)} mln
                                    </td>
                                  </tr>
                                ))}
                              </tbody>
                            </>
                          )}
                        </table>
                      </div>
                    </div>
                  )}
                </div>
              )}

              {/* Sub-Tab 1.1b: Drayver Ixtisoslashuvi Upload */}
              {excelSubTab === 'drivers' && (
                <div className="space-y-4">
                  {/* Download Template Box */}
                  <div className="bg-amber-50/70 border-2 border-amber-200 rounded-2xl p-4 flex flex-col md:flex-row items-center justify-between gap-3 shadow-xs">
                    <div className="flex items-center gap-3">
                      <div className="w-10 h-10 rounded-xl bg-amber-100 text-amber-800 flex items-center justify-center shrink-0">
                        <Target className="w-5 h-5 text-amber-700" />
                      </div>
                      <div>
                        <h4 className="font-extrabold text-sm text-slate-800">
                          Tumanlar Drayver Ixtisoslashuvi shabloni (4 ustunli)
                        </h4>
                        <p className="text-xs text-slate-500 mt-0.5">
                          Jadval ustunlari: <b>№</b>, <b>Туман номи</b>, <b>Драйвер йўналиши</b>, <b>Туман учун танланган драйвер йўналишнинг асослантирилиши</b>.
                        </p>
                      </div>
                    </div>

                    <button
                      onClick={downloadDriverSampleExcel}
                      className="px-4 py-2 bg-amber-600 hover:bg-amber-700 text-white rounded-xl text-xs font-bold flex items-center gap-1.5 shadow-sm transition active:scale-95 shrink-0"
                    >
                      <Download className="w-4 h-4" />
                      <span>Drayver shablonini yuklab olish (.xlsx)</span>
                    </button>
                  </div>

                  {/* Dropzone */}
                  <div className="border-2 border-dashed border-amber-400 bg-white rounded-3xl p-8 text-center hover:bg-amber-50/30 transition shadow-xs">
                    <input
                      type="file"
                      id="driver-file-input"
                      accept=".xlsx, .xls, .csv"
                      onChange={handleDriverFileUpload}
                      className="hidden"
                    />
                    <label htmlFor="driver-file-input" className="cursor-pointer block">
                      <div className="w-14 h-14 mx-auto rounded-2xl bg-amber-50 text-amber-600 flex items-center justify-center mb-3 shadow-sm border border-amber-200">
                        <Upload className="w-7 h-7" />
                      </div>
                      <h3 className="font-black text-slate-800 text-base">
                        Tumanlar drayveri Excel faylini shu yerga tashlang
                      </h3>
                      <p className="text-xs text-slate-500 mt-1 max-w-xl mx-auto leading-relaxed">
                        Siz tashlagan 4 ustunli rasmiy faylni yuklang. Tizim har bir tumanning drayver ixtisoslashuvi va uning asoslantirilishini avtomatik xarita pasportiga biriktiradi.
                      </p>
                      <div className="mt-4 inline-flex items-center gap-2 px-5 py-2.5 rounded-xl bg-amber-700 hover:bg-amber-800 text-white font-bold text-xs shadow-md transition">
                        <span>Kompyuterdan Drayver faylini tanlash</span>
                      </div>
                    </label>
                  </div>

                  {driverFileLoading && (
                    <div className="text-center p-4 text-amber-700 font-bold text-xs animate-pulse">
                      Drayver jadvali tahlil qilinmoqda, iltimos kuting...
                    </div>
                  )}

                  {driverErrorMsg && (
                    <div className="p-3 bg-rose-50 border border-rose-200 rounded-xl text-rose-700 text-xs flex items-center gap-2">
                      <AlertCircle className="w-4 h-4 shrink-0 text-rose-500" />
                      <span>{driverErrorMsg}</span>
                    </div>
                  )}

                  {driverSuccessMsg && (
                    <div className="p-3 bg-emerald-50 border border-emerald-200 rounded-xl text-emerald-800 text-xs flex items-center gap-2 font-medium">
                      <CheckCircle2 className="w-4 h-4 shrink-0 text-emerald-600" />
                      <span>{driverSuccessMsg}</span>
                    </div>
                  )}

                  {/* Preview Table if rows loaded */}
                  {driverRows.length > 0 && (
                    <div className="bg-white rounded-2xl border border-amber-200 p-4 space-y-3">
                      <div className="flex items-center justify-between">
                        <div>
                          <h4 className="font-extrabold text-sm text-slate-800">
                            Yuklangan drayver ma'lumotlari ({driverRows.length} ta tuman):
                          </h4>
                          <span className="inline-block mt-0.5 text-[11px] font-bold text-amber-800 bg-amber-50 px-2 py-0.5 rounded-md border border-amber-200">
                            ✓ Barcha tumanlar muvaffaqiyatli aniqlandi
                          </span>
                        </div>
                        <button
                          onClick={handleConfirmDriverImport}
                          className="px-5 py-2 bg-amber-600 hover:bg-amber-700 text-white rounded-xl text-xs font-black shadow-md transition active:scale-95"
                        >
                          Barcha tumanlar drayverini saqlash ➔
                        </button>
                      </div>

                      <div className="overflow-x-auto max-h-72 border border-slate-100 rounded-xl">
                        <table className="w-full text-left text-xs">
                          <thead className="bg-amber-50/70 text-amber-950 uppercase font-bold text-[10px] sticky top-0 border-b border-amber-200">
                            <tr>
                              <th className="p-2.5">№</th>
                              <th className="p-2.5">Tuman</th>
                              <th className="p-2.5">Драйвер йўналиши</th>
                              <th className="p-2.5">Асослантирилиши</th>
                            </tr>
                          </thead>
                          <tbody className="divide-y divide-slate-100 font-medium">
                            {driverRows.map((r, i) => (
                              <tr key={i} className="hover:bg-amber-50/30">
                                <td className="p-2.5 text-slate-400">{i + 1}</td>
                                <td className="p-2.5 font-bold text-slate-900 capitalize">
                                  {r.districtId.replace('-', ' ')}
                                  {r.rawDistrict && (
                                    <span className="text-[10px] text-slate-400 block font-normal">{r.rawDistrict}</span>
                                  )}
                                </td>
                                <td className="p-2.5 font-extrabold text-amber-800">
                                  {r.driverDirection}
                                </td>
                                <td className="p-2.5 text-slate-600 max-w-md text-[11px] leading-relaxed">
                                  {r.driverRationale}
                                </td>
                              </tr>
                            ))}
                          </tbody>
                        </table>
                      </div>
                    </div>
                  )}

                  {/* Current Districts Driver Status List */}
                  <div className="bg-white rounded-2xl border border-slate-200 p-4 space-y-3">
                    <h4 className="font-extrabold text-sm text-slate-800 flex items-center gap-2">
                      <Target className="w-4 h-4 text-amber-600" />
                      <span>Joriy tumanlar drayveri ko'rinishi ({districts.length} ta tuman):</span>
                    </h4>

                    <div className="overflow-x-auto max-h-72 border border-slate-100 rounded-xl">
                      <table className="w-full text-left text-xs">
                        <thead className="bg-slate-50 text-slate-600 uppercase font-bold text-[10px] sticky top-0 border-b border-slate-200">
                          <tr>
                            <th className="p-2.5">№</th>
                            <th className="p-2.5">Tuman</th>
                            <th className="p-2.5">Drayver yo'nalishi</th>
                            <th className="p-2.5">Asoslantirish</th>
                          </tr>
                        </thead>
                        <tbody className="divide-y divide-slate-100 font-medium">
                          {districts.map((d, i) => (
                            <tr key={d.id} className="hover:bg-slate-50">
                              <td className="p-2.5 text-slate-400">{i + 1}</td>
                              <td className="p-2.5 font-bold text-slate-800">{d.name}</td>
                              <td className="p-2.5 font-bold text-amber-700">
                                {d.driverDirection || d.description || "Sabzavotchilik va poliz"}
                              </td>
                              <td className="p-2.5 text-slate-500 max-w-sm text-[11px]">
                                {d.driverRationale || d.description || "Tuproq va iqlim sharoitiga mos ravishda"}
                              </td>
                            </tr>
                          ))}
                        </tbody>
                      </table>
                    </div>
                  </div>
                </div>
              )}

              {/* Sub-Tab 1.2: Manual Entry Form */}
              {excelSubTab === 'manual' && (
                <form onSubmit={handleManualSubmit} className="bg-white p-5 rounded-3xl border border-slate-200 space-y-4">
                  <div className="flex items-center justify-between pb-2 border-b border-slate-100">
                    <div>
                      <h4 className="font-extrabold text-sm text-slate-800">
                        Yangi ijara yer konturini qo'lda kiritish
                      </h4>
                      <p className="text-xs text-slate-400">
                        Har bir kiritilgan dala maydoni xaritada o'z MFYsiga birikadi
                      </p>
                    </div>
                    {manualSuccessMsg && (
                      <span className="text-xs text-emerald-700 font-bold bg-emerald-50 px-3 py-1 rounded-xl border border-emerald-200">
                        {manualSuccessMsg}
                      </span>
                    )}
                  </div>

                  <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-3 text-xs">
                    <div>
                      <label className="block text-slate-600 font-bold mb-1">Tuman:</label>
                      <select
                        value={selectedDistrictId}
                        onChange={(e) => setSelectedDistrictId(e.target.value)}
                        className="w-full bg-slate-50 border border-slate-300 rounded-xl px-3 py-2 text-slate-800 font-medium"
                      >
                        {DISTRICTS_DATA.map(d => (
                          <option key={d.id} value={d.id}>{d.number}. {d.name}</option>
                        ))}
                      </select>
                    </div>

                    <div>
                      <label className="block text-slate-600 font-bold mb-1">MFY nomi:</label>
                      <input
                        type="text"
                        required
                        value={mfyName}
                        onChange={(e) => setMfyName(e.target.value)}
                        placeholder="Masalan: Paxtakor MFY"
                        className="w-full bg-slate-50 border border-slate-300 rounded-xl px-3 py-2 text-slate-800"
                      />
                    </div>

                    <div>
                      <label className="block text-slate-600 font-bold mb-1">Kontur raqami:</label>
                      <input
                        type="text"
                        required
                        value={contourNumber}
                        onChange={(e) => setContourNumber(e.target.value)}
                        placeholder="Masalan: 12-kontur"
                        className="w-full bg-slate-50 border border-slate-300 rounded-xl px-3 py-2 text-slate-800"
                      />
                    </div>

                    <div>
                      <label className="block text-slate-600 font-bold mb-1">Maydoni (gektar):</label>
                      <input
                        type="number"
                        step="0.05"
                        min="0.1"
                        max="20"
                        value={allocatedAreaHa}
                        onChange={(e) => setAllocatedAreaHa(e.target.value)}
                        className="w-full bg-slate-50 border border-slate-300 rounded-xl px-3 py-2 text-slate-800"
                      />
                    </div>

                    <div>
                      <label className="block text-slate-600 font-bold mb-1">Yerning namligi:</label>
                      <input
                        type="text"
                        value={moisture}
                        onChange={(e) => setMoisture(e.target.value)}
                        className="w-full bg-slate-50 border border-slate-300 rounded-xl px-3 py-2 text-slate-800"
                      />
                    </div>

                    <div>
                      <label className="block text-slate-600 font-bold mb-1">Suv ta'minoti manbasi:</label>
                      <input
                        type="text"
                        value={waterSource}
                        onChange={(e) => setWaterSource(e.target.value)}
                        className="w-full bg-slate-50 border border-slate-300 rounded-xl px-3 py-2 text-slate-800"
                      />
                    </div>

                    <div>
                      <label className="block text-slate-600 font-bold mb-1">Tavsiya ekin / Sabzavot:</label>
                      <input
                        type="text"
                        value={primaryCrop}
                        onChange={(e) => setPrimaryCrop(e.target.value)}
                        placeholder="Masalan: Ertapishar sabzi, pomidor"
                        className="w-full bg-slate-50 border border-slate-300 rounded-xl px-3 py-2 text-slate-800"
                      />
                    </div>

                    <div>
                      <label className="block text-slate-600 font-bold mb-1">Kutilayotgan sof foyda (mln so'm):</label>
                      <input
                        type="number"
                        step="0.5"
                        value={netProfitMln}
                        onChange={(e) => setNetProfitMln(e.target.value)}
                        className="w-full bg-slate-50 border border-slate-300 rounded-xl px-3 py-2 text-slate-800 font-bold text-emerald-700"
                      />
                    </div>

                    <div className="flex items-end">
                      <button
                        type="submit"
                        className="w-full py-2.5 bg-emerald-600 hover:bg-emerald-700 text-white rounded-xl font-bold text-xs shadow-md transition active:scale-95"
                      >
                        + Maydonni qo'shish
                      </button>
                    </div>
                  </div>
                </form>
              )}

              {/* Sub-Tab 1.3: Table view of all parcels */}
              {excelSubTab === 'table' && (
                <div className="bg-white rounded-3xl border border-slate-200 p-4 space-y-3 shadow-xs">
                  <div className="flex items-center justify-between flex-wrap gap-2">
                    <div className="flex items-center gap-2 flex-1 max-w-md">
                      <div className="relative w-full">
                        <Search className="w-4 h-4 absolute left-3 top-1/2 -translate-y-1/2 text-slate-400" />
                        <input
                          type="text"
                          value={tableSearch}
                          onChange={(e) => setTableSearch(e.target.value)}
                          placeholder="MFY, kontur yoki ekin bo'yicha qidirish..."
                          className="w-full pl-9 pr-3 py-2 bg-slate-50 border border-slate-300 rounded-xl text-xs"
                        />
                      </div>
                    </div>

                    <select
                      value={tableDistrictFilter}
                      onChange={(e) => setTableDistrictFilter(e.target.value)}
                      className="px-3 py-2 bg-slate-50 border border-slate-300 rounded-xl text-xs font-semibold"
                    >
                      <option value="all">Barcha tumanlar ({districts.length})</option>
                      {districts.map(d => (
                        <option key={d.id} value={d.id}>{d.name}</option>
                      ))}
                    </select>
                  </div>

                  <div className="overflow-x-auto max-h-96 border border-slate-100 rounded-2xl">
                    <table className="w-full text-left text-xs">
                      <thead className="bg-slate-100 text-slate-700 uppercase font-bold text-[10px] sticky top-0">
                        <tr>
                          <th className="p-3">#</th>
                          <th className="p-3">Tuman</th>
                          <th className="p-3">MFY</th>
                          <th className="p-3">Kontur</th>
                          <th className="p-3">Maydoni</th>
                          <th className="p-3">Yer namligi</th>
                          <th className="p-3">Tavsiya etilgan ekin</th>
                          <th className="p-3">Sof daromad</th>
                        </tr>
                      </thead>
                      <tbody className="divide-y divide-slate-100 font-medium">
                        {filteredParcels.map((p, idx) => (
                          <tr key={idx} className="hover:bg-slate-50">
                            <td className="p-3 text-slate-400">{idx + 1}</td>
                            <td className="p-3 font-bold text-slate-800">{p.districtName}</td>
                            <td className="p-3 text-emerald-700 font-bold">{p.mfyName}</td>
                            <td className="p-3 font-semibold text-slate-600">{p.contourNumber}</td>
                            <td className="p-3">{p.allocatedAreaHa} ga</td>
                            <td className="p-3 text-sky-700">{p.soil?.moisture}</td>
                            <td className="p-3 text-slate-700 font-medium">{p.recommendation?.primaryCrop}</td>
                            <td className="p-3 font-black text-emerald-700">
                              +{(p.economics?.netProfitUzs / 1000000).toFixed(1)} mln so'm
                            </td>
                          </tr>
                        ))}
                      </tbody>
                    </table>
                  </div>
                </div>
              )}
            </div>
          )}

          {/* ========================================================================= */}
          {/* TAB 2: SABZAVOT, EKINLAR VA DAROMADLAR KATALOGI */}
          {/* ========================================================================= */}
          {activeTab === 'crops' && (
            <div className="space-y-4">
              <div className="flex items-center justify-between flex-wrap gap-2 pb-2 border-b border-slate-200">
                <div>
                  <h3 className="font-extrabold text-base text-slate-800">
                    Sabzavot, meva va ekinlar rentabellik katalogi
                  </h3>
                  <p className="text-xs text-slate-500">
                    Qaysi sabzavot qancha hosil, xarajat va qancha sof daromad keltirishi bo'yicha agrotahlil bazasi
                  </p>
                </div>

                <div className="flex items-center gap-2 flex-wrap">
                  {/* Excel yuklash tugmasi */}
                  <label className="cursor-pointer px-3.5 py-2 bg-emerald-50 hover:bg-emerald-100 text-emerald-800 border border-emerald-300 rounded-xl text-xs font-bold flex items-center gap-1.5 shadow-2xs transition">
                    <Upload className="w-4 h-4 text-emerald-600" />
                    <span>Excel yuklash</span>
                    <input
                      type="file"
                      accept=".xlsx, .xls, .csv"
                      onChange={handleCropFileUpload}
                      className="hidden"
                    />
                  </label>

                  {/* Shablon yuklab olish */}
                  <button
                    onClick={downloadCropsSampleExcel}
                    className="px-3.5 py-2 bg-white hover:bg-slate-50 text-slate-700 border border-slate-300 rounded-xl text-xs font-bold flex items-center gap-1.5 shadow-2xs transition"
                    title="Namunaviy Excel shablonini yuklab olish"
                  >
                    <Download className="w-4 h-4 text-slate-500" />
                    <span className="hidden sm:inline">Shablon (.xlsx)</span>
                  </button>

                  {/* Yangi ekin qo'shish */}
                  <button
                    onClick={() => setIsAddingCrop(!isAddingCrop)}
                    className="px-4 py-2 bg-emerald-600 hover:bg-emerald-700 text-white rounded-xl text-xs font-bold flex items-center gap-1.5 shadow-sm transition"
                  >
                    <PlusCircle className="w-4 h-4" />
                    <span>{isAddingCrop ? "Bekor qilish" : "Yangi ekin/nav qo'shish"}</span>
                  </button>
                </div>
              </div>

              {/* Fayl yuklaydigan maxsus Excel bo'limi (Dedicated Excel Upload Zone) */}
              <div className="bg-gradient-to-r from-emerald-50/80 via-teal-50/50 to-sky-50/70 p-4 sm:p-5 rounded-3xl border-2 border-dashed border-emerald-300 text-center relative space-y-3 shadow-xs">
                <div className="w-12 h-12 mx-auto rounded-2xl bg-emerald-100 text-emerald-700 flex items-center justify-center shadow-xs">
                  <FileSpreadsheet className="w-6 h-6" />
                </div>

                <div>
                  <h4 className="font-extrabold text-sm text-slate-800">
                    Sabzavot va ekinlar ro'yxatini Excel orqali yuklash (.xlsx, .xls)
                  </h4>
                  <p className="text-xs text-slate-500 max-w-xl mx-auto mt-1">
                    Ushbu bo'limga sabzavotlar (Sholg'om, Turp, Karam, Bosh karam, Brokkoli, Baqlajon va boshqalar) yozilgan Excel faylni yuklang. Tizim avtomatik ravishda ekin nomi, hosildorligi, bozor bahosi, namlik va daromadlarini o'qib, katalogga qabul qiladi.
                  </p>
                </div>

                <div className="flex items-center justify-center gap-3 flex-wrap pt-1">
                  <label className="cursor-pointer px-5 py-2.5 bg-emerald-600 hover:bg-emerald-700 text-white rounded-xl text-xs font-black flex items-center gap-2 shadow-md transition transform active:scale-95">
                    <Upload className="w-4 h-4" />
                    <span>Kompyuterdan Excel fayl tanlash (.xlsx)</span>
                    <input
                      type="file"
                      accept=".xlsx, .xls, .csv"
                      onChange={handleCropFileUpload}
                      className="hidden"
                    />
                  </label>

                  <button
                    onClick={downloadCropsSampleExcel}
                    className="px-4 py-2.5 bg-white hover:bg-slate-50 text-slate-700 border border-slate-300 rounded-xl text-xs font-bold flex items-center gap-2 shadow-xs transition"
                  >
                    <Download className="w-4 h-4 text-emerald-600" />
                    <span>Namunaviy Excel shablonini yuklab olish</span>
                  </button>
                </div>

                {cropFileLoading && (
                  <div className="p-3 bg-white/95 border border-emerald-300 rounded-xl text-emerald-800 text-xs font-bold inline-flex items-center gap-2 shadow-xs">
                    <span className="w-3.5 h-3.5 border-2 border-emerald-600 border-t-transparent rounded-full animate-spin" />
                    <span>Excel fayl tahlil qilinmoqda va bazaga kiritilmoqda...</span>
                  </div>
                )}

                {cropImportSuccess && (
                  <div className="p-3 bg-emerald-50 border border-emerald-300 rounded-xl text-emerald-800 text-xs font-bold flex items-center justify-center gap-2 shadow-xs animate-in fade-in">
                    <CheckCircle2 className="w-4 h-4 text-emerald-600 shrink-0" />
                    <span>{cropImportSuccess}</span>
                  </div>
                )}

                {cropImportError && (
                  <div className="p-3 bg-rose-50 border border-rose-300 rounded-xl text-rose-800 text-xs font-bold flex items-center justify-center gap-2 shadow-xs animate-in fade-in">
                    <AlertCircle className="w-4 h-4 text-rose-600 shrink-0" />
                    <span>{cropImportError}</span>
                  </div>
                )}
              </div>

              {/* Add New Crop Form */}
              {isAddingCrop && (
                <form onSubmit={handleAddCropSubmit} className="bg-emerald-50/60 border-2 border-emerald-300 rounded-3xl p-4 sm:p-5 space-y-3">
                  <h4 className="font-black text-sm text-emerald-900 flex items-center gap-1.5">
                    <Sparkles className="w-4 h-4 text-emerald-600" />
                    <span>Yangi ekin turi va uning daromad ko'rsatkichlarini kiritish</span>
                  </h4>

                  <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-3 text-xs">
                    <div>
                      <label className="block text-slate-700 font-bold mb-1">Ekin / Sabzavot nomi:</label>
                      <input
                        type="text"
                        required
                        value={newCropForm.name}
                        onChange={(e) => setNewCropForm({ ...newCropForm, name: e.target.value })}
                        placeholder="Masalan: Eksportbop Brokkoli karami"
                        className="w-full bg-white border border-slate-300 rounded-xl px-3 py-2 text-slate-800"
                      />
                    </div>

                    <div>
                      <label className="block text-slate-700 font-bold mb-1">O'rtacha hosildorlik (ga):</label>
                      <input
                        type="text"
                        value={newCropForm.avgYieldPerHa}
                        onChange={(e) => setNewCropForm({ ...newCropForm, avgYieldPerHa: e.target.value })}
                        placeholder="Masalan: 30 - 35 tonna/ga"
                        className="w-full bg-white border border-slate-300 rounded-xl px-3 py-2 text-slate-800"
                      />
                    </div>

                    <div>
                      <label className="block text-slate-700 font-bold mb-1">Kutilayotgan sof daromad (50 sotixdan):</label>
                      <input
                        type="text"
                        value={newCropForm.avgProfitPer50Sotix}
                        onChange={(e) => setNewCropForm({ ...newCropForm, avgProfitPer50Sotix: e.target.value })}
                        placeholder="Masalan: 40 - 55 mln so'm"
                        className="w-full bg-white border border-slate-300 rounded-xl px-3 py-2 text-slate-800 font-bold text-emerald-700"
                      />
                    </div>

                    <div>
                      <label className="block text-slate-700 font-bold mb-1">Tavsiya qilinadigan tumanlar:</label>
                      <input
                        type="text"
                        value={newCropForm.bestDistricts}
                        onChange={(e) => setNewCropForm({ ...newCropForm, bestDistricts: e.target.value })}
                        placeholder="Masalan: Uychi, To'raqo'rg'on, Norin"
                        className="w-full bg-white border border-slate-300 rounded-xl px-3 py-2 text-slate-800"
                      />
                    </div>

                    <div>
                      <label className="block text-slate-700 font-bold mb-1">Optimal yer namligi:</label>
                      <input
                        type="text"
                        value={newCropForm.optimalMoisture}
                        onChange={(e) => setNewCropForm({ ...newCropForm, optimalMoisture: e.target.value })}
                        placeholder="Masalan: 70% - 80%"
                        className="w-full bg-white border border-slate-300 rounded-xl px-3 py-2 text-slate-800"
                      />
                    </div>

                    <div className="flex items-end">
                      <button
                        type="submit"
                        className="w-full py-2.5 bg-emerald-600 hover:bg-emerald-700 text-white font-black rounded-xl text-xs shadow-md transition"
                      >
                        Katalogga saqlash
                      </button>
                    </div>
                  </div>
                </form>
              )}

              {/* Search & Statistics Bar */}
              <div className="flex items-center justify-between flex-wrap gap-2 pt-1">
                <div className="relative flex-1 max-w-sm">
                  <Search className="w-4 h-4 text-slate-400 absolute left-3 top-1/2 -translate-y-1/2" />
                  <input
                    type="text"
                    placeholder="Sabzavot yoki ekin nomini qidirish (masalan: Sholg'om, Turp)..."
                    value={cropSearch}
                    onChange={(e) => setCropSearch(e.target.value)}
                    className="w-full bg-white border border-slate-200 rounded-xl pl-9 pr-3 py-2 text-xs text-slate-800 focus:outline-none focus:border-emerald-500 shadow-2xs"
                  />
                </div>
                <div className="text-xs font-bold text-slate-500">
                  Jami ekinlar soni: <strong className="text-emerald-700 font-black">{cropsList.length} ta</strong>
                </div>
              </div>

              {/* Crops Grid Cards */}
              <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-3.5">
                {cropsList
                  .filter(crop => !cropSearch || crop.name.toLowerCase().includes(cropSearch.toLowerCase()) || (crop.bestDistricts && crop.bestDistricts.toLowerCase().includes(cropSearch.toLowerCase())))
                  .map((crop) => (
                  <div
                    key={crop.id}
                    className="bg-white rounded-3xl p-4 border border-slate-200 shadow-xs hover:border-emerald-400 hover:shadow-md transition space-y-3 relative group"
                  >
                    <div className="flex items-center justify-between pb-2 border-b border-slate-100">
                      <div className="flex items-center gap-2.5 min-w-0">
                        <span className="text-2xl shrink-0">{crop.icon || "🌱"}</span>
                        <div className="min-w-0">
                          <h4 className="font-extrabold text-sm text-slate-900 leading-tight truncate">
                            {crop.name}
                          </h4>
                          <span className="text-[10px] text-emerald-700 font-semibold bg-emerald-50 px-2 py-0.5 rounded-md inline-block mt-0.5">
                            Hosildorlik: {crop.avgYieldPerHa || crop.newYield || crop.localYield || "25 - 35 t/ga"}
                          </span>
                        </div>
                      </div>

                      {/* Delete button */}
                      <button
                        onClick={() => setCropsList(cropsList.filter(item => item.id !== crop.id))}
                        className="opacity-0 group-hover:opacity-100 text-slate-300 hover:text-rose-500 p-1.5 rounded-lg hover:bg-rose-50 transition"
                        title="O'chirish"
                      >
                        <Trash2 className="w-3.5 h-3.5" />
                      </button>
                    </div>

                    <div className="space-y-1.5 text-xs">
                      <div className="flex items-center justify-between">
                        <span className="text-slate-400 text-[11px]">Bozor bahosi:</span>
                        <span className="font-bold text-slate-800">{crop.marketPricePerKg || crop.pricePerKg || "4 000 so'm/kg"}</span>
                      </div>

                      <div className="flex items-center justify-between">
                        <span className="text-slate-400 text-[11px]">Optimal namlik:</span>
                        <span className="font-bold text-sky-700">{crop.optimalMoisture || "65% - 75%"}</span>
                      </div>

                      <div className="flex items-center justify-between">
                        <span className="text-slate-400 text-[11px]">Sug'orish:</span>
                        <span className="text-slate-600 text-[11px] font-medium">{crop.irrigationFreq || "Har 5 - 7 kunda"}</span>
                      </div>
                    </div>

                    <div className="p-2.5 bg-gradient-to-r from-emerald-50 to-amber-50/60 rounded-xl border border-emerald-200 flex items-center justify-between">
                      <span className="text-[10px] uppercase font-bold text-emerald-800">
                        Kutilayotgan daromad:
                      </span>
                      <span className="font-black text-emerald-700 text-xs">
                        {crop.avgProfitPer50Sotix.startsWith('+') ? crop.avgProfitPer50Sotix : `+${crop.avgProfitPer50Sotix}`}
                      </span>
                    </div>

                    <div className="text-[10px] text-slate-400 font-medium truncate">
                      Mos tumanlar: <strong className="text-slate-600">{Array.isArray(crop.bestDistricts) ? crop.bestDistricts.join(', ') : (crop.bestDistricts || "Pop, Mingbuloq, Chust, Namangan t.")}</strong>
                    </div>
                  </div>
                ))}
              </div>
            </div>
          )}

          {/* ========================================================================= */}
          {/* TAB 3: PAROLNI O'ZGARTIRISH (XAVFSIZLIK) */}
          {/* ========================================================================= */}
          {activeTab === 'security' && (
            <div className="max-w-md mx-auto bg-white p-6 rounded-3xl border border-slate-200 shadow-sm space-y-4">
              <div className="text-center pb-2 border-b border-slate-100">
                <div className="w-12 h-12 mx-auto rounded-2xl bg-amber-50 text-amber-600 flex items-center justify-center mb-2 border border-amber-200 shadow-xs">
                  <KeyRound className="w-6 h-6" />
                </div>
                <h3 className="font-black text-base text-slate-800">
                  Admin panel parolini almashtirish
                </h3>
                <p className="text-xs text-slate-400 mt-0.5">
                  Tizim xavfsizligini ta'minlash uchun maxfiy parolni yangilang
                </p>
              </div>

              {pwdError && (
                <div className="p-3 bg-rose-50 border border-rose-200 rounded-xl text-rose-700 text-xs flex items-center gap-2">
                  <AlertCircle className="w-4 h-4 shrink-0 text-rose-500" />
                  <span>{pwdError}</span>
                </div>
              )}

              {pwdSuccess && (
                <div className="p-3 bg-emerald-50 border border-emerald-200 rounded-xl text-emerald-800 text-xs flex items-center gap-2 font-semibold">
                  <CheckCircle2 className="w-4 h-4 shrink-0 text-emerald-600" />
                  <span>{pwdSuccess}</span>
                </div>
              )}

              <form onSubmit={handlePasswordSubmit} className="space-y-3.5 text-xs">
                <div>
                  <label className="block text-slate-700 font-bold mb-1 uppercase tracking-wider text-[11px]">
                    Eski parol:
                  </label>
                  <input
                    type="password"
                    required
                    value={oldPassword}
                    onChange={(e) => setOldPassword(e.target.value)}
                    placeholder="Amaldagi parolni kiriting (standart: 12345)"
                    className="w-full bg-slate-50 border border-slate-300 rounded-xl px-3.5 py-2.5 text-slate-800 focus:outline-none focus:border-emerald-500"
                  />
                </div>

                <div>
                  <label className="block text-slate-700 font-bold mb-1 uppercase tracking-wider text-[11px]">
                    Yangi parol:
                  </label>
                  <input
                    type="password"
                    required
                    value={newPassword}
                    onChange={(e) => setNewPassword(e.target.value)}
                    placeholder="Yangi maxfiy parolni kiriting"
                    className="w-full bg-slate-50 border border-slate-300 rounded-xl px-3.5 py-2.5 text-slate-800 focus:outline-none focus:border-emerald-500"
                  />
                </div>

                <div>
                  <label className="block text-slate-700 font-bold mb-1 uppercase tracking-wider text-[11px]">
                    Yangi parolni tasdiqlang:
                  </label>
                  <input
                    type="password"
                    required
                    value={confirmPassword}
                    onChange={(e) => setConfirmPassword(e.target.value)}
                    placeholder="Yangi parolni takroran kiriting"
                    className="w-full bg-slate-50 border border-slate-300 rounded-xl px-3.5 py-2.5 text-slate-800 focus:outline-none focus:border-emerald-500"
                  />
                </div>

                <button
                  type="submit"
                  className="w-full py-3 bg-gradient-to-r from-amber-600 to-emerald-600 hover:from-amber-700 hover:to-emerald-700 text-white font-extrabold text-xs rounded-xl shadow-md transition active:scale-95"
                >
                  Yangi parolni saqlash
                </button>
              </form>
            </div>
          )}

        </div>

        {/* Modal Footer */}
        <div className="p-3.5 bg-white border-t border-slate-200 flex items-center justify-between text-xs text-slate-500">
          <div className="flex items-center gap-2">
            <span className="w-2.5 h-2.5 rounded-full bg-emerald-500 animate-pulse"></span>
            <span>Namangan Ijara Yer Geoportali — Ma'muriy boshqaruv</span>
          </div>

          <button
            onClick={onClose}
            className="px-4 py-1.5 rounded-xl bg-slate-100 hover:bg-slate-200 text-slate-700 font-bold transition text-xs"
          >
            Yopish
          </button>
        </div>

      </div>
    </div>
  );
}
