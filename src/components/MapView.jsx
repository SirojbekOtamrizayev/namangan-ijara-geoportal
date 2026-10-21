import React, { useEffect, useRef } from 'react';
import L from 'leaflet';
import 'leaflet/dist/leaflet.css';
import { NAMANGAN_CENTER, DEFAULT_ZOOM } from '../data/namanganData';
import { 
  Navigation, 
  Compass, 
  Layers, 
  Droplets, 
  Sprout, 
  DollarSign, 
  ExternalLink, 
  MapPin, 
  Sparkles,
  User,
  X
} from 'lucide-react';

export default function MapView({
  districts,
  selectedDistrict,
  selectedMFY,
  selectedParcel,
  onSelectDistrict,
  onSelectMFY,
  onSelectParcel,
  mapMode,
  setMapMode
}) {
  const mapContainerRef = useRef(null);
  const mapInstanceRef = useRef(null);
  const tileLayerRef = useRef(null);
  const layerGroupRef = useRef(null);

  // Initialize Leaflet Map
  useEffect(() => {
    if (!mapContainerRef.current) return;

    if (!mapInstanceRef.current) {
      const map = L.map(mapContainerRef.current, {
        center: NAMANGAN_CENTER,
        zoom: DEFAULT_ZOOM,
        zoomControl: false,
        attributionControl: false
      });

      // Add Zoom Control at bottom left
      L.control.zoom({ position: 'bottomleft' }).addTo(map);

      mapInstanceRef.current = map;
      layerGroupRef.current = L.layerGroup().addTo(map);
    }

    return () => {
      if (mapInstanceRef.current) {
        mapInstanceRef.current.remove();
        mapInstanceRef.current = null;
      }
    };
  }, []);

  // Handle Tile Layer Switch (Streets vs Satellite)
  useEffect(() => {
    const map = mapInstanceRef.current;
    if (!map) return;

    if (tileLayerRef.current) {
      map.removeLayer(tileLayerRef.current);
    }

    if (mapMode === 'satellite') {
      // Esri World Imagery
      tileLayerRef.current = L.tileLayer(
        'https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
        {
          maxZoom: 19,
          attribution: 'Esri, Maxar, Earthstar Geographics'
        }
      ).addTo(map);
    } else {
      // OpenStreetMap Standard
      tileLayerRef.current = L.tileLayer(
        'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
        {
          maxZoom: 19,
          attribution: '© OpenStreetMap contributors'
        }
      ).addTo(map);
    }
  }, [mapMode]);

  // Fly to selected MFY or Parcel immediately when changed
  useEffect(() => {
    const map = mapInstanceRef.current;
    if (!map) return;

    if (selectedParcel) {
      // Fly to parcel coordinates with optimal zoom
      map.flyTo(selectedParcel.coordinates, 16, { 
        duration: 1.2,
        paddingTopLeft: [0, 0],
        paddingBottomRight: [350, 0] // Offset right so floating card does not obscure parcel contour
      });
    } else if (selectedMFY) {
      const primaryParcel = selectedMFY.parcels?.[0];
      const targetCoords = primaryParcel ? primaryParcel.coordinates : selectedMFY.center;
      map.flyTo(targetCoords, 16, { 
        duration: 1.2,
        paddingBottomRight: [350, 0]
      });
    } else if (selectedDistrict) {
      map.flyTo(selectedDistrict.center, selectedDistrict.zoom || 12, { duration: 1.0 });
    }
  }, [selectedMFY, selectedParcel]);

  // Render Map Markers, Districts, MFYs and Polygons
  useEffect(() => {
    const map = mapInstanceRef.current;
    const layerGroup = layerGroupRef.current;
    if (!map || !layerGroup) return;

    layerGroup.clearLayers();

    // 1. If NO district is selected:
    if (!selectedDistrict) {
      districts.forEach(dist => {
        const customIcon = L.divIcon({
          className: 'custom-district-marker',
          html: `
            <div style="
              background: linear-gradient(135deg, ${dist.color}, #0f172a);
              color: white;
              padding: 6px 10px;
              border-radius: 12px;
              border: 2px solid #ffffff;
              box-shadow: 0 4px 12px rgba(0,0,0,0.35);
              font-family: sans-serif;
              font-size: 11px;
              font-weight: 700;
              white-space: nowrap;
              cursor: pointer;
              display: flex;
              align-items: center;
              gap: 6px;
              transform: translate(-50%, -50%);
              transition: all 0.2s ease;
            ">
              <span style="display:inline-block; width:8px; height:8px; border-radius:50%; background:#22c55e;"></span>
              <span>${dist.name}</span>
              <span style="background:rgba(255,255,255,0.25); font-size:10px; padding:1px 6px; border-radius:8px;">
                ${dist.totalLeaseAreaHa} ha
              </span>
            </div>
          `,
          iconSize: [140, 36],
          iconAnchor: [70, 18]
        });

        const marker = L.marker(dist.center, { icon: customIcon });
        marker.on('click', () => {
          onSelectDistrict(dist);
        });

        marker.bindTooltip(`
          <div style="padding:6px; font-family:sans-serif;">
            <strong style="color:#0f172a; font-size:13px;">${dist.name}</strong><br/>
            <span style="color:#16a34a; font-weight:600;">Ijara yer maydoni:</span> ${dist.totalLeaseAreaHa} ga<br/>
            <span style="color:#0284c7; font-weight:600;">Biriktirilgan oilalar:</span> ${dist.poorFamiliesCount} ta<br/>
            <span style="color:#64748b; font-size:10px;">Batafsil MFYlarni ko'rish uchun bosing</span>
          </div>
        `, { direction: 'top', offset: [0, -10] });

        layerGroup.addLayer(marker);
      });
    }

    // 2. If a District IS selected:
    if (selectedDistrict) {
      // Render MFYs of this District
      selectedDistrict.mfys?.forEach(mfy => {
        const isMfyActive = selectedMFY?.id === mfy.id;

        const mfyIcon = L.divIcon({
          className: 'custom-mfy-marker',
          html: `
            <div style="
              background: ${isMfyActive ? '#10b981' : '#ffffff'};
              color: ${isMfyActive ? '#ffffff' : '#0f172a'};
              padding: 6px 11px;
              border-radius: 12px;
              border: 2px solid ${isMfyActive ? '#ffffff' : '#10b981'};
              box-shadow: 0 4px 14px rgba(0,0,0,0.35);
              font-family: sans-serif;
              font-size: 11px;
              font-weight: 800;
              white-space: nowrap;
              cursor: pointer;
              display: flex;
              align-items: center;
              gap: 6px;
              transform: translate(-50%, -50%);
              transition: all 0.2s ease;
            ">
              <span>📍</span>
              <span>${mfy.name}</span>
              <span style="background:${isMfyActive ? 'rgba(255,255,255,0.3)' : '#e0f2fe'}; color:${isMfyActive ? '#fff' : '#0369a1'}; font-size:10px; padding:1px 6px; border-radius:6px;">
                ${mfy.leaseAreaHa} ga
              </span>
            </div>
          `,
          iconSize: [140, 34],
          iconAnchor: [70, 17]
        });

        const mfyMarker = L.marker(mfy.center, { icon: mfyIcon });
        mfyMarker.on('click', () => {
          onSelectMFY(mfy);
          if (mfy.parcels && mfy.parcels[0]) {
            onSelectParcel(mfy.parcels[0]);
          }
        });
        layerGroup.addLayer(mfyMarker);

        // Render Parcels (Ijara yer konturlari)
        mfy.parcels?.forEach(parcel => {
          const isSelected = selectedParcel?.id === parcel.id;

          // Draw Polygon for Land Contour
          const polygon = L.polygon(parcel.polygon, {
            color: isSelected ? '#fbbf24' : '#10b981',
            weight: isSelected ? 4 : 2.5,
            fillColor: isSelected ? '#f59e0b' : '#10b981',
            fillOpacity: isSelected ? 0.65 : 0.45,
            dashArray: isSelected ? '4, 4' : null
          });

          polygon.on('click', () => {
            onSelectMFY(mfy);
            onSelectParcel(parcel);
          });

          // Tooltip on Hover
          polygon.bindTooltip(`
            <div style="font-family:sans-serif; min-width:190px; padding:4px;">
              <div style="font-weight:800; color:#0f172a; border-bottom:1px solid #e2e8f0; padding-bottom:3px; margin-bottom:4px;">
                🌾 ${parcel.contourNumber} (${parcel.allocatedAreaHa} ga ijara yer)
              </div>
              <div style="font-size:11px; color:#0284c7; margin-bottom:2px;">
                💧 Namligi: <strong>${parcel.soil.moisture}</strong>
              </div>
              <div style="font-size:11px; color:#059669; font-weight:700; margin-bottom:2px;">
                🌱 Tavsiya: ${parcel.recommendation.primaryCrop}
              </div>
              <div style="font-size:11px; color:#d97706; font-weight:800;">
                💰 Kutilayotgan sof foyda: ${(parcel.economics.netProfitUzs / 1000000).toFixed(1)} mln so'm
              </div>
            </div>
          `, { sticky: true, direction: 'auto' });

          layerGroup.addLayer(polygon);

          // Center icon with crop badge
          const parcelCenterIcon = L.divIcon({
            className: 'custom-pulse-marker',
            html: `
              <div style="
                background: ${isSelected ? '#f59e0b' : '#059669'};
                color: white;
                width: 28px;
                height: 28px;
                border-radius: 50%;
                border: 2px solid white;
                box-shadow: 0 3px 10px rgba(0,0,0,0.4);
                display: flex;
                align-items: center;
                justify-content: center;
                font-size: 13px;
                cursor: pointer;
              ">
                🌾
              </div>
            `,
            iconSize: [28, 28],
            iconAnchor: [14, 14]
          });

          const parcelMarker = L.marker(parcel.coordinates, { icon: parcelCenterIcon });
          parcelMarker.on('click', () => {
            onSelectMFY(mfy);
            onSelectParcel(parcel);
          });
          layerGroup.addLayer(parcelMarker);
        });
      });
    }

  }, [districts, selectedDistrict, selectedMFY, selectedParcel]);

  // Active parcel to inspect (either selectedParcel or first parcel of selectedMFY)
  const activeParcel = selectedParcel || selectedMFY?.parcels?.[0];

  return (
    <div className="relative w-full h-full overflow-hidden bg-slate-950">
      {/* Map Container */}
      <div ref={mapContainerRef} className="w-full h-full z-0" />

      {/* FLOATING AGRO-INSPECTOR PANEL: Appears immediately when MFY is clicked */}
      {activeParcel && (
        <div className="absolute top-4 right-4 z-20 w-80 sm:w-96 bg-white/95 backdrop-blur-md border-2 border-emerald-500 rounded-3xl p-4 shadow-xl text-slate-800 animate-in fade-in slide-in-from-right-4">
          {/* Header */}
          <div className="flex items-center justify-between pb-2.5 mb-2.5 border-b border-slate-200">
            <div className="flex items-center gap-2 min-w-0">
              <span className="w-8 h-8 rounded-xl bg-emerald-100 text-emerald-700 border border-emerald-200 flex items-center justify-center text-sm font-bold shrink-0">
                🌾
              </span>
              <div className="min-w-0">
                <h3 className="font-extrabold text-sm text-slate-900 truncate">
                  {selectedMFY?.name || "MFY"} • {activeParcel.contourNumber}
                </h3>
                <div className="text-[11px] text-emerald-700 font-bold">
                  {activeParcel.allocatedAreaHa} ga ({activeParcel.allocatedAreaHa * 100} sotix ijara yer)
                </div>
              </div>
            </div>

            <button
              onClick={() => onSelectParcel(null)}
              className="w-7 h-7 rounded-lg bg-slate-100 hover:bg-slate-200 text-slate-500 hover:text-slate-800 flex items-center justify-center transition"
            >
              <X className="w-4 h-4" />
            </button>
          </div>

          {/* Key Agro Details matching user request */}
          <div className="space-y-2.5 text-xs">
            {/* 1. Nimaga ixtisoslashgan */}
            <div className="bg-slate-50 p-2.5 rounded-xl border border-slate-200">
              <div className="text-[10px] uppercase font-bold text-slate-500 tracking-wider">
                🌟 Nimaga ixtisoslashgan:
              </div>
              <div className="font-bold text-sky-800 text-xs mt-0.5">
                {selectedMFY?.specialization || activeParcel.specialization || "Ertapishar sabzavotchilik klasteri"}
              </div>
            </div>

            {/* 2. Yerning namligi */}
            <div className="bg-slate-50 p-2.5 rounded-xl border border-slate-200">
              <div className="text-[10px] uppercase font-bold text-slate-500 tracking-wider flex items-center gap-1">
                <Droplets className="w-3.5 h-3.5 text-sky-600" />
                <span>Yerning namligi va suv ta'minoti:</span>
              </div>
              <div className="font-bold text-slate-900 text-xs mt-0.5">
                {activeParcel.soil.moisture}
              </div>
              <div className="text-[10px] text-slate-600 mt-0.5 font-medium">
                💧 Sizot suvlari: <strong className="text-sky-700">{activeParcel.soil.groundwaterDepth}</strong> • Suv: <span className="text-emerald-700 font-bold">{activeParcel.soil.waterSource}</span>
              </div>
            </div>

            {/* 3. Nima sabzavot eksa bo'ladi */}
            <div className="bg-gradient-to-r from-emerald-50 to-teal-50/60 p-2.5 rounded-xl border border-emerald-200">
              <div className="text-[10px] uppercase font-bold text-emerald-800 tracking-wider flex items-center gap-1">
                <Sprout className="w-3.5 h-3.5 text-emerald-600" />
                <span>Nima sabzavot/ekin eksa bo'ladi?:</span>
              </div>
              <div className="font-black text-slate-900 text-sm mt-0.5">
                {activeParcel.recommendation.primaryCrop}
              </div>
              <div className="text-[11px] text-emerald-800 mt-0.5 font-medium">
                Ikkinchi hosil: <strong className="font-bold">{activeParcel.recommendation.secondaryCrop}</strong>
              </div>
              <div className="text-[10px] text-slate-500 mt-1 italic font-medium">
                {activeParcel.recommendation.rationale}
              </div>
            </div>

            {/* 4. Qancha daromad olsa bo'ladi */}
            <div className="bg-gradient-to-r from-amber-50 to-orange-50/60 p-2.5 rounded-xl border border-amber-200">
              <div className="text-[10px] uppercase font-bold text-amber-800 tracking-wider flex items-center justify-between">
                <span>💰 Qancha daromad olsa bo'ladi?:</span>
                <span className="text-emerald-700 font-bold">{activeParcel.economics.paybackMonths} oyda qoplaydi</span>
              </div>
              <div className="grid grid-cols-2 gap-2 mt-1.5 pt-1 border-t border-amber-200/80 text-center">
                <div className="bg-white p-1.5 rounded-lg border border-slate-200">
                  <div className="text-[10px] text-slate-500">Xarajat:</div>
                  <div className="font-bold text-rose-600 text-xs">{(activeParcel.economics.expensesUzs / 1000000).toFixed(1)} mln</div>
                </div>
                <div className="bg-emerald-100/80 p-1.5 rounded-lg border border-emerald-300">
                  <div className="text-[10px] text-emerald-800 font-bold">SOF FOYDA:</div>
                  <div className="font-black text-emerald-700 text-sm">+{(activeParcel.economics.netProfitUzs / 1000000).toFixed(1)} mln so'm</div>
                </div>
              </div>
            </div>
          </div>

          {/* Action Buttons: Google Maps Navigation & Full Modal */}
          <div className="mt-3 pt-2.5 border-t border-slate-200 flex items-center gap-2">
            <a
              href={`https://www.google.com/maps/dir/?api=1&destination=${activeParcel.coordinates[0]},${activeParcel.coordinates[1]}`}
              target="_blank"
              rel="noopener noreferrer"
              className="flex-1 flex items-center justify-center gap-1.5 py-2 px-3 bg-emerald-600 hover:bg-emerald-700 text-white rounded-xl text-xs font-bold shadow-md shadow-emerald-600/20 transition active:scale-95"
            >
              <Navigation className="w-3.5 h-3.5" />
              <span>Lokatsiyaga borish</span>
              <ExternalLink className="w-3 h-3 opacity-90" />
            </a>

            <button
              onClick={() => onSelectParcel(activeParcel)}
              className="py-2 px-3 bg-slate-100 hover:bg-slate-200 text-slate-700 rounded-xl text-xs font-bold border border-slate-300 transition"
            >
              To'liq pasport
            </button>
          </div>
        </div>
      )}

      {/* Floating Map Legend (Bottom left) */}
      <div className="absolute bottom-6 left-4 z-10 pointer-events-auto bg-white/95 backdrop-blur-md border border-slate-200 rounded-2xl p-2.5 shadow-md text-slate-700 text-xs hidden sm:block">
        <div className="space-y-1 text-[11px] text-slate-600 font-medium">
          <div className="flex items-center gap-2">
            <span className="w-3 h-3 rounded bg-emerald-500 border border-emerald-600 inline-block"></span>
            <span>Ijara yer konturi</span>
          </div>
          <div className="flex items-center gap-2">
            <span className="w-3 h-3 rounded bg-amber-500 border border-amber-600 inline-block"></span>
            <span>Tanlangan maydon</span>
          </div>
        </div>
      </div>
    </div>
  );
}
