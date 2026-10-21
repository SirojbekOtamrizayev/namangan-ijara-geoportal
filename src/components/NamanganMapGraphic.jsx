import React, { useState } from 'react';
import { Sparkles, ArrowRight, MapPin } from 'lucide-react';

// Exact natural contour polygons hugging the complete territory of all 14 districts on 511x414
export const NATURAL_DISTRICTS = [
  {
    id: "uchqorgon",
    name: "Uchqo'rg'on tumani",
    shortName: "Uchqo'rg'on",
    number: 13,
    color: "#1e3a8a",
    glowColor: "#38bdf8",
    center: { x: 405, y: 100 },
    pinPos: { x: 395, y: 110 },
    // Hugs the entire dark navy territory including full text and pin
    polygon: "320,52 355,42 405,38 455,42 485,62 495,105 485,138 430,142 375,148 345,142 328,120 320,85"
  },
  {
    id: "norin",
    name: "Norin tumani",
    shortName: "Norin",
    number: 14,
    color: "#0284c7",
    glowColor: "#60a5fa",
    center: { x: 265, y: 75 },
    pinPos: { x: 260, y: 88 },
    polygon: "195,45 245,32 295,30 330,48 328,95 315,120 275,125 225,122 200,95 195,65"
  },
  {
    id: "namangan-tumani",
    name: "Namangan tumani",
    shortName: "Namangan t.",
    number: 7,
    color: "#1d4ed8",
    glowColor: "#93c5fd",
    center: { x: 95, y: 95 },
    pinPos: { x: 88, y: 98 },
    polygon: "25,65 75,45 135,42 170,75 175,115 155,148 115,155 65,158 25,140 18,95"
  },
  {
    id: "kosonsoy",
    name: "Kosonsoy tumani",
    shortName: "Kosonsoy",
    number: 9,
    color: "#38bdf8",
    glowColor: "#bae6fd",
    center: { x: 265, y: 165 },
    pinPos: { x: 262, y: 175 },
    polygon: "208,125 265,118 315,120 332,148 330,185 308,208 265,208 225,202 205,175 205,145"
  },
  {
    id: "mingbuloq",
    name: "Mingbuloq tumani",
    shortName: "Mingbuloq",
    number: 8,
    color: "#2dd4bf",
    glowColor: "#5eead4",
    center: { x: 165, y: 165 },
    pinPos: { x: 158, y: 160 },
    polygon: "115,145 165,130 205,128 225,155 222,195 185,205 145,205 120,188 112,165"
  },
  {
    id: "chortoq",
    name: "Chortoq tumani",
    shortName: "Chortoq",
    number: 12,
    color: "#34d399",
    glowColor: "#6ee7b7",
    center: { x: 415, y: 200 },
    pinPos: { x: 402, y: 205 },
    polygon: "345,145 395,140 455,142 488,165 490,215 465,248 415,258 365,245 345,210 342,175"
  },
  {
    id: "chust",
    name: "Chust tumani",
    shortName: "Chust",
    number: 5,
    color: "#0369a1",
    glowColor: "#38bdf8",
    center: { x: 75, y: 215 },
    pinPos: { x: 70, y: 225 },
    polygon: "28,162 75,148 115,145 132,185 128,235 105,265 65,268 25,255 15,215"
  },
  {
    id: "namangan-shahri",
    name: "Namangan shahri",
    shortName: "Namangan sh.",
    number: 1,
    color: "#056738",
    glowColor: "#4ade80",
    center: { x: 230, y: 245 },
    pinPos: { x: 228, y: 240 },
    polygon: "135,210 185,198 235,205 285,202 322,225 325,255 295,282 255,295 205,285 165,265 135,245"
  },
  {
    id: "yangi-namangan",
    name: "Yangi Namangan tumani",
    shortName: "Yangi Namangan",
    number: 2,
    color: "#16a34a",
    glowColor: "#86efac",
    center: { x: 315, y: 260 },
    pinPos: { x: 295, y: 260 },
    polygon: "285,235 325,228 352,255 348,285 318,292 288,275 282,250"
  },
  {
    id: "yangiqorgon",
    name: "Yangiqo'rg'on tumani",
    shortName: "Yangiqo'rg'on",
    number: 11,
    color: "#5eead4",
    glowColor: "#a5f3fc",
    center: { x: 365, y: 270 },
    pinPos: { x: 362, y: 272 },
    polygon: "305,225 365,215 425,212 435,255 428,295 385,325 335,320 305,285 298,255"
  },
  {
    id: "toraqorgon",
    name: "To'raqo'rg'on tumani",
    shortName: "To'raqo'rg'on",
    number: 6,
    color: "#9333ea",
    glowColor: "#e879f9",
    center: { x: 80, y: 325 },
    pinPos: { x: 78, y: 325 },
    polygon: "25,265 75,262 115,265 142,305 135,355 105,385 55,385 22,345 18,295"
  },
  {
    id: "uychi",
    name: "Uychi tumani",
    shortName: "Uychi",
    number: 10,
    color: "#0284c7",
    glowColor: "#93c5fd",
    center: { x: 152, y: 350 },
    pinPos: { x: 150, y: 350 },
    polygon: "102,305 155,292 198,295 205,345 195,385 155,405 115,395 98,355"
  },
  {
    id: "pop",
    name: "Pop tumani",
    shortName: "Pop",
    number: 4,
    color: "#1e3a8a",
    glowColor: "#60a5fa",
    center: { x: 242, y: 365 },
    pinPos: { x: 236, y: 375 },
    polygon: "198,315 245,310 285,312 292,365 275,412 235,415 195,408 192,360"
  },
  {
    id: "davlatobod",
    name: "Davlatobod tumani",
    shortName: "Davlatobod",
    number: 3,
    color: "#ea580c",
    glowColor: "#fdba74",
    center: { x: 335, y: 365 },
    pinPos: { x: 320, y: 362 },
    polygon: "278,328 335,312 385,335 402,375 382,408 335,412 288,395 278,355"
  }
];

export default function NamanganMapGraphic({
  districts,
  selectedDistrict,
  onSelectDistrict,
  hoveredDistrict,
  setHoveredDistrict
}) {
  return (
    <div className="relative w-full max-w-[680px] aspect-[511/414] mx-auto select-none group">
      {/* Clean map display with seamlessly blended edges (yonlari fonga birikib ketadi) */}
      <div 
        className="relative w-full h-full"
        style={{
          maskImage: 'radial-gradient(ellipse 96% 94% at 50% 50%, black 75%, transparent 100%)',
          WebkitMaskImage: 'radial-gradient(ellipse 96% 94% at 50% 50%, black 75%, transparent 100%)'
        }}
      >
        {/* SVG Interactive Map with Pixel-Perfect Natural Boundaries */}
        <svg
          viewBox="0 0 511 414"
          className="w-full h-full overflow-visible"
        >
          <defs>
            {/* Glowing filter for clean boundary highlight */}
            <filter id="natural-glow" x="-30%" y="-30%" width="160%" height="160%">
              <feDropShadow dx="0" dy="0" stdDeviation="5" floodColor="#10b981" floodOpacity="0.8" />
              <feDropShadow dx="0" dy="4" stdDeviation="8" floodColor="#000000" floodOpacity="0.25" />
            </filter>
          </defs>

          {/* 1. Base Map: Smooth natural lighting, seamlessly blended into background */}
          <image
            href="/namangan-poster-map.png"
            x="0"
            y="0"
            width="511"
            height="414"
            className="transition-all duration-300 pointer-events-none"
            style={{
              filter: hoveredDistrict ? 'brightness(0.92) contrast(0.98)' : 'brightness(1.02) contrast(1.03)'
            }}
          />

          {/* 2. Natural District Interactive Layers */}
          {NATURAL_DISTRICTS.map((nd) => {
            const districtObj = districts.find(d => d.id === nd.id);
            const isHovered = hoveredDistrict === nd.id;
            const isSelected = selectedDistrict?.id === nd.id;

            return (
              <g
                key={nd.id}
                className="cursor-pointer transition-all duration-200"
                onClick={() => {
                  if (districtObj) onSelectDistrict(districtObj);
                }}
                onMouseEnter={() => setHoveredDistrict(nd.id)}
                onMouseLeave={() => setHoveredDistrict(null)}
              >
                {/* When hovered: The exact colored district lifts and separates cleanly along its boundary! */}
                {isHovered && (
                  <g
                    style={{
                      transform: 'translateY(-6px) scale(1.015)',
                      transformOrigin: `${nd.center.x}px ${nd.center.y}px`,
                      transition: 'transform 0.2s cubic-bezier(0.16, 1, 0.3, 1)',
                      filter: `drop-shadow(0 12px 18px rgba(0,0,0,0.5)) drop-shadow(0 0 16px ${nd.glowColor}) brightness(1.2) contrast(1.1)`
                    }}
                  >
                    <image
                      href={`/districts/${nd.id}.png`}
                      x="0"
                      y="0"
                      width="511"
                      height="414"
                    />
                  </g>
                )}

                {/* Interactive Hitbox Polygon */}
                <polygon
                  points={nd.polygon}
                  fill={isSelected ? "#f59e0b" : "transparent"}
                  fillOpacity={isSelected ? 0.35 : 0}
                  stroke={isHovered ? "#ffffff" : isSelected ? "#f59e0b" : "transparent"}
                  strokeWidth={isHovered ? "3" : isSelected ? "3.5" : "0"}
                  strokeLinejoin="round"
                  className="transition-all duration-200"
                  style={{
                    transform: isHovered ? 'translateY(-6px)' : 'none',
                    transformOrigin: `${nd.center.x}px ${nd.center.y}px`,
                    transition: 'transform 0.2s cubic-bezier(0.16, 1, 0.3, 1)'
                  }}
                />

                {/* Animated Target Circle & Pin */}
                <g 
                  transform={`translate(${nd.pinPos.x}, ${nd.pinPos.y})`}
                  style={{
                    transform: isHovered 
                      ? `translate(${nd.pinPos.x}px, ${nd.pinPos.y - 8}px)` 
                      : `translate(${nd.pinPos.x}px, ${nd.pinPos.y}px)`,
                    transition: 'transform 0.2s cubic-bezier(0.16, 1, 0.3, 1)'
                  }}
                >
                  {/* Ping Ring on Hover */}
                  {isHovered && (
                    <circle
                      r="16"
                      fill="none"
                      stroke="#ffffff"
                      strokeWidth="2.5"
                      className="animate-ping opacity-90"
                    />
                  )}

                  {/* Pulsing Pin Marker */}
                  <circle
                    r={isHovered ? "10" : "7"}
                    fill={isHovered ? "#ffffff" : "transparent"}
                    stroke={isHovered ? nd.color : "transparent"}
                    strokeWidth="3"
                    className="transition-all duration-200 shadow-xl"
                  />

                  {isHovered && (
                    <circle
                      r="4.5"
                      fill={nd.color}
                    />
                  )}
                </g>
              </g>
            );
          })}
        </svg>

        {/* Floating Tooltip Card over the active separated district */}
        {hoveredDistrict && (() => {
          const dist = districts.find(d => d.id === hoveredDistrict);
          const nd = NATURAL_DISTRICTS.find(n => n.id === hoveredDistrict);
          if (!dist) return null;

          return (
            <div className="absolute bottom-3 left-1/2 -translate-x-1/2 bg-white/95 backdrop-blur-xl border-2 border-emerald-500 px-5 py-2.5 rounded-2xl shadow-[0_15px_35px_rgba(16,185,129,0.25)] text-center pointer-events-none z-30 animate-in fade-in zoom-in-95 max-w-[320px]">
              <div className="flex items-center justify-center gap-2">
                <span 
                  className="w-3.5 h-3.5 rounded-full ring-2 ring-emerald-500 shadow-sm animate-pulse"
                  style={{ backgroundColor: nd?.color || "#10b981" }}
                />
                <h4 className="text-slate-850 font-black text-sm">
                  #{dist.number} {dist.name}
                </h4>
              </div>

              <div className="flex items-center justify-center gap-3 text-xs text-slate-600 mt-1 pt-1 border-t border-slate-200">
                <span>Ijara yer: <strong className="text-emerald-600">{dist.totalLeaseAreaHa} ga</strong></span>
                <span>•</span>
                <span>Biriktirilgan oilalar: <strong className="text-sky-600">{dist.poorFamiliesCount} ta</strong></span>
              </div>

              <div className="text-[11px] text-emerald-800 font-bold mt-1.5 flex items-center justify-center gap-1.5 bg-emerald-50 py-1 px-3 rounded-lg border border-emerald-200">
                <span>MFY va dala maydonlarini ochish ➔</span>
              </div>
            </div>
          );
        })()}
      </div>

      {/* Map Interactive Caption */}
      <div className="flex items-center justify-between text-xs text-slate-500 mt-2.5 px-1 font-medium">
        <span className="flex items-center gap-1.5 text-emerald-700 font-bold text-[11px]">
          <Sparkles className="w-3.5 h-3.5 text-emerald-600" />
          <span>Tumanning ustiga mishkani olib boring — butun shakli ajralib, alohida ko'rinadi</span>
        </span>
        <span className="text-[11px] text-slate-500 hidden sm:inline">
          Ustiga bosing ➔ MFY va barcha ma'lumotlarga olib boradi
        </span>
      </div>
    </div>
  );
}
