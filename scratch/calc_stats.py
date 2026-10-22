import json

with open('scratch/districts_compiled.json', 'r', encoding='utf-8') as f:
    districts = json.load(f)

total_area = sum(float(d['boshYerHa'].replace('ga', '').replace(' ', '').strip()) for d in districts.values())
total_mfy = sum(len(d.get('mfys', [])) for d in districts.values())
total_poor = sum(sum(m.get('poorFamilies', 0) for m in d.get('mfys', [])) for d in districts.values())
total_parcels = sum(sum(len(m.get('parcels', [])) for m in d.get('mfys', [])) for d in districts.values())

print(f"Jami bo'sh ijara yer maydoni: {total_area:,.0f} ga")
print(f"Jami MFYlar: {total_mfy} ta")
print(f"Jami ehtiyojmand / kambag'al oilalar: {total_poor:,} ta")
print(f"Jami shakllantirilgan ijara lotlari (konturlar): {total_parcels} ta")

for did, d in districts.items():
    area = float(d['boshYerHa'].replace('ga', '').replace(' ', '').strip())
    pct = (area / total_area) * 100
    mfys = len(d.get('mfys', []))
    print(f"{d['shortName']}: {area:,.0f} ga ({pct:.1f}%) | {mfys} MFY | {d['kutilayotganDaromad']}")
