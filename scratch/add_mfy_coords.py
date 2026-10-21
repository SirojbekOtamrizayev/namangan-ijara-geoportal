import json

# Re-compile dataset but also include MFY lat/lon centers from parsed data
with open('scratch/districts_compiled.json', 'r', encoding='utf-8') as f:
    districts = json.load(f)

with open('scratch/namangan_parsed_data.json', 'r', encoding='utf-8') as f:
    parsed_data = json.load(f)

# Build a lookup: mfy_id -> center coords
mfy_centers = {}
for d in parsed_data:
    for m in d.get('mfys', []):
        mid = m.get('id', '')
        ctr = m.get('center')
        if mid and ctr:
            mfy_centers[mid] = ctr

# Also gather from all parcels' coordinates
parcel_coords = {}
for d in parsed_data:
    for m in d.get('mfys', []):
        mid = m.get('id', '')
        for p in m.get('parcels', []):
            if p.get('coordinates') and mid not in parcel_coords:
                parcel_coords[mid] = p['coordinates']

print("MFY centers found:", len(mfy_centers))
print("Parcel coords found:", len(parcel_coords))

# Enrich districts compiled with center coords for MFYs
for did, d in districts.items():
    for m in d.get('mfys', []):
        mid = m.get('id', '')
        if mid in mfy_centers:
            m['latlon'] = mfy_centers[mid]
        elif mid in parcel_coords:
            m['latlon'] = parcel_coords[mid]
        else:
            # Fallback: use district-level approximate coordinates
            fallback_coords = {
                'pop': [40.9, 71.1], 'chust': [41.0, 71.35], 'mingbuloq': [40.8, 71.55],
                'toraqorgon': [40.98, 71.55], 'kosonsoy': [41.07, 71.56],
                'yangiqorgon': [41.15, 71.63], 'chortoq': [41.07, 71.73],
                'uychi': [41.09, 71.82], 'uchqorgon': [41.08, 71.9],
                'norin': [40.99, 71.85], 'namangan-tumani': [41.0, 71.72],
                'namangan-shahri': [41.0, 71.67]
            }
            m['latlon'] = fallback_coords.get(did, [41.0, 71.67])

with open('scratch/districts_compiled.json', 'w', encoding='utf-8') as f:
    json.dump(districts, f, ensure_ascii=False, indent=2)

print("Updated districts_compiled.json with MFY lat/lon coordinates!")
