import React, { useState } from 'react';
import Navbar from './components/Navbar';
import MapView from './components/MapView';
import DistrictSidebar from './components/DistrictSidebar';
import InfographicDashboard from './components/InfographicDashboard';
import ParcelDetailModal from './components/ParcelDetailModal';
import AgroCalculatorModal from './components/AgroCalculatorModal';
import CropsCatalogModal from './components/CropsCatalogModal';
import DataManagerModal from './components/DataManagerModal';
import AdminLoginModal from './components/AdminLoginModal';
import AdminDashboardModal from './components/AdminDashboardModal';
import { DISTRICTS_DATA } from './data/namanganData';

export default function App() {
  const [districts, setDistricts] = useState(DISTRICTS_DATA);
  const [selectedDistrict, setSelectedDistrict] = useState(null); // null = Infographic Dashboard
  const [selectedMFY, setSelectedMFY] = useState(null);
  const [selectedParcel, setSelectedParcel] = useState(null);

  const [mapMode, setMapMode] = useState('streets'); // 'streets' | 'satellite'
  const [searchQuery, setSearchQuery] = useState('');

  // Admin Authentication & Password State
  const [currentUser, setCurrentUser] = useState(null);
  const [isAdminLoginOpen, setIsAdminLoginOpen] = useState(false);
  const [adminPassword, setAdminPassword] = useState('12345'); // Default password, changeable by admin

  // Modals
  const [isDataManagerOpen, setIsDataManagerOpen] = useState(false);
  const [isPassportModalOpen, setIsPassportModalOpen] = useState(false);
  const [isCalculatorOpen, setIsCalculatorOpen] = useState(false);
  const [isCropsCatalogOpen, setIsCropsCatalogOpen] = useState(false);

  // Dynamic live calculations across all districts ("aniq sifiralar aylansin")
  const totalDynamicArea = districts.reduce((acc, d) => acc + (d.totalLeaseAreaHa || 0), 0);
  const totalDynamicFamilies = districts.reduce((acc, d) => acc + (d.poorFamiliesCount || 0), 0);

  // Handle District Selection from Dashboard
  const handleSelectDistrict = (district) => {
    // Look up fresh district object from current state
    const currentDist = districts.find(d => d.id === district.id) || district;
    setSelectedDistrict(currentDist);
    if (currentDist?.mfys && currentDist.mfys.length > 0) {
      setSelectedMFY(currentDist.mfys[0]);
      if (currentDist.mfys[0].parcels && currentDist.mfys[0].parcels.length > 0) {
        setSelectedParcel(currentDist.mfys[0].parcels[0]);
      }
    } else {
      setSelectedMFY(null);
      setSelectedParcel(null);
    }
  };

  // Handle MFY Selection (Flies to location & selects parcel)
  const handleSelectMFY = (mfy) => {
    setSelectedMFY(mfy);
    if (mfy?.parcels && mfy.parcels.length > 0) {
      setSelectedParcel(mfy.parcels[0]);
    }
  };

  // Handle Parcel Selection (Inspect on map)
  const handleSelectParcel = (parcel) => {
    setSelectedParcel(parcel);
  };

  // Reset to Main Infographic Dashboard
  const handleResetView = () => {
    setSelectedDistrict(null);
    setSelectedMFY(null);
    setSelectedParcel(null);
    setIsPassportModalOpen(false);
    setSearchQuery('');
  };

  // BATCH IMPORT (Excel yoki Formadan kiritilganda "patumanu o'zi tortib olsin va aniq sifiralar aylansin")
  const handleBatchImport = (newRecords) => {
    if (!newRecords || newRecords.length === 0) return;

    setDistricts(prev => {
      // Clone array
      const updated = prev.map(d => ({
        ...d,
        mfys: d.mfys ? d.mfys.map(m => ({ ...m, parcels: [...(m.parcels || [])] })) : []
      }));

      newRecords.forEach(rec => {
        // 1. Tumanini avtomatik aniqlash ("patumanu o'zi tortib olsin")
        let targetDist = updated.find(d => d.id === rec.districtId);
        if (!targetDist) {
          targetDist = updated[0]; // fallback
        }

        // 2. MFY ni topish yoki yangi MFY ochish
        const cleanMfyName = (rec.mfyName || "Yangi MFY").trim();
        let targetMfy = targetDist.mfys.find(m => m.name.toLowerCase() === cleanMfyName.toLowerCase());

        // Koordinatalarni hisoblash
        const baseLat = rec.coordinates 
          ? rec.coordinates[0] 
          : targetDist.center[0] + (Math.random() - 0.5) * 0.02;
        const baseLng = rec.coordinates 
          ? rec.coordinates[1] 
          : targetDist.center[1] + (Math.random() - 0.5) * 0.02;

        const lotsToAdd = rec.lotsCount || 1;

        const parcelToAdd = {
          id: rec.rowId || `PARCEL-${Date.now()}-${Math.random()}`,
          contourNumber: rec.contourNumber,
          farmerName: rec.farmerName,
          familyStatus: rec.privilege,
          familyMembers: rec.familyMembers || 5,
          allocatedAreaHa: rec.allocatedAreaHa,
          contractYear: "2024 - 2034 (10 yil)",
          coordinates: [baseLat, baseLng],
          specialization: rec.specialization,
          polygon: rec.polygon || [
            [baseLat - 0.001, baseLng - 0.0015],
            [baseLat + 0.001, baseLng - 0.001],
            [baseLat + 0.0008, baseLng + 0.0015],
            [baseLat - 0.0012, baseLng + 0.001]
          ],
          soil: rec.soil,
          recommendation: rec.recommendation,
          economics: rec.economics,
          isLotSummary: rec.isLotFormat || false,
          lotsCount: lotsToAdd
        };

        if (targetMfy) {
          targetMfy.leaseAreaHa = Math.round((targetMfy.leaseAreaHa + rec.allocatedAreaHa) * 100) / 100;
          targetMfy.poorFamilies = (targetMfy.poorFamilies || 0) + lotsToAdd;
          targetMfy.specialization = targetMfy.specialization || rec.specialization;
          targetMfy.parcels.push(parcelToAdd);
        } else {
          targetDist.mfys.push({
            id: `mfy-${Date.now()}-${Math.random()}`,
            name: cleanMfyName,
            specialization: rec.specialization,
            leaseAreaHa: Math.round(rec.allocatedAreaHa * 100) / 100,
            poorFamilies: lotsToAdd,
            center: [baseLat, baseLng],
            parcels: [parcelToAdd]
          });
        }

        // 3. Tuman statistikalarini qayta hisoblash ("aniq sifiralar aylansin")
        targetDist.totalLeaseAreaHa = Math.round((targetDist.totalLeaseAreaHa + rec.allocatedAreaHa) * 100) / 100;
        targetDist.poorFamiliesCount = (targetDist.poorFamiliesCount || 0) + lotsToAdd;
        targetDist.activeContracts = (targetDist.activeContracts || 0) + lotsToAdd;
      });

      return updated;
    });

    // If only one record was added, fly to that district
    if (newRecords.length === 1) {
      const singleDist = districts.find(d => d.id === newRecords[0].districtId);
      if (singleDist) {
        setSelectedDistrict(singleDist);
      }
    }
  };

  // Tumanlar drayver yo'nalishlarini yangilash
  const handleUpdateDistrictDrivers = (driverUpdates) => {
    if (!driverUpdates || driverUpdates.length === 0) return;

    setDistricts(prev => {
      return prev.map(d => {
        const update = driverUpdates.find(u => u.districtId === d.id);
        if (update) {
          return {
            ...d,
            driverDirection: update.driverDirection,
            driverRationale: update.driverRationale,
            rawDriverDirection: update.rawDriverDirection,
            rawDriverRationale: update.rawDriverRationale
          };
        }
        return d;
      });
    });
  };

  return (
    <div className="flex flex-col h-screen w-screen overflow-hidden bg-slate-50 font-sans text-slate-800 select-none">
      {/* Top Navbar */}
      <Navbar
        selectedDistrict={selectedDistrict}
        onSelectDistrict={handleSelectDistrict}
        mapMode={mapMode}
        setMapMode={setMapMode}
        onOpenCalculator={() => setIsCalculatorOpen(true)}
        onOpenCropsCatalog={() => setIsCropsCatalogOpen(true)}
        onOpenDataManager={() => setIsDataManagerOpen(true)}
        onResetView={handleResetView}
        searchQuery={searchQuery}
        setSearchQuery={setSearchQuery}
        totalArea={totalDynamicArea}
        totalFamilies={totalDynamicFamilies}
        currentUser={currentUser}
        onOpenAdminLogin={() => setIsAdminLoginOpen(true)}
        onLogout={() => {
          setCurrentUser(null);
          setIsDataManagerOpen(false);
        }}
      />

      {/* Main Content Area */}
      <div className="flex-1 overflow-hidden relative">
        {!selectedDistrict ? (
          /* 1. Main Infographic Dashboard (1-7 | Map | 8-14) with Live Numbers */
          <InfographicDashboard
            districts={districts}
            onSelectDistrict={handleSelectDistrict}
            totalArea={totalDynamicArea}
          />
        ) : (
          /* 2. District GIS Map View with dedicated MFY Sidebar */
          <div className="flex h-full w-full overflow-hidden">
            {/* Left Sidebar: ONLY MFYs of this selected district */}
            <DistrictSidebar
              districts={districts}
              selectedDistrict={selectedDistrict}
              selectedMFY={selectedMFY}
              selectedParcel={selectedParcel}
              onSelectDistrict={handleSelectDistrict}
              onSelectMFY={handleSelectMFY}
              onSelectParcel={handleSelectParcel}
              onResetToDashboard={handleResetView}
              searchQuery={searchQuery}
              setSearchQuery={setSearchQuery}
            />

            {/* Interactive Leaflet GIS Map with Live Agro-Inspector Card */}
            <div className="flex-1 h-full relative">
              <MapView
                districts={districts}
                selectedDistrict={selectedDistrict}
                selectedMFY={selectedMFY}
                selectedParcel={selectedParcel}
                onSelectDistrict={handleSelectDistrict}
                onSelectMFY={handleSelectMFY}
                onSelectParcel={(parcel) => {
                  setSelectedParcel(parcel);
                }}
                mapMode={mapMode}
                setMapMode={setMapMode}
              />
            </div>
          </div>
        )}
      </div>

      {/* Full Parcel Detail Modal (Opened when requested) */}
      {isPassportModalOpen && (
        <ParcelDetailModal
          parcel={selectedParcel}
          district={selectedDistrict}
          mfy={selectedMFY}
          onClose={() => setIsPassportModalOpen(false)}
        />
      )}

      {/* Comprehensive Admin Dashboard Modal (Excel Upload, Crops/Profit Catalog & Password Change) */}
      <AdminDashboardModal
        isOpen={isDataManagerOpen}
        onClose={() => setIsDataManagerOpen(false)}
        districts={districts}
        onBatchImport={handleBatchImport}
        onUpdateDistrictDrivers={handleUpdateDistrictDrivers}
        currentUser={currentUser}
        onLogout={() => {
          setCurrentUser(null);
          setIsDataManagerOpen(false);
        }}
        adminPassword={adminPassword}
        onChangePassword={(newPwd) => setAdminPassword(newPwd)}
      />

      {/* Admin Login Modal with dynamic password */}
      <AdminLoginModal
        isOpen={isAdminLoginOpen}
        onClose={() => setIsAdminLoginOpen(false)}
        adminPassword={adminPassword}
        onLoginSuccess={(user) => {
          setCurrentUser(user);
          setIsDataManagerOpen(true); // Open admin dashboard modal upon successful admin login
        }}
      />

      {/* Agro Calculator Modal */}
      <AgroCalculatorModal
        isOpen={isCalculatorOpen}
        onClose={() => setIsCalculatorOpen(false)}
      />

      {/* Crops Catalog Modal */}
      <CropsCatalogModal
        isOpen={isCropsCatalogOpen}
        onClose={() => setIsCropsCatalogOpen(false)}
      />
    </div>
  );
}
