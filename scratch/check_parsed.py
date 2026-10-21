import json

with open('scratch/namangan_parsed_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for d in data:
    mfys = d.get('mfys', [])
    total_parcels = sum(len(m.get('parcels', [])) for m in mfys)
    print(f"{d['id']}: {d['name']} -> {len(mfys)} MFYs, {total_parcels} parcels")
    for m in mfys:
        print(f"   MFY: {m['name']} ({m.get('specialization', '')}) - {len(m.get('parcels', []))} parcels")
