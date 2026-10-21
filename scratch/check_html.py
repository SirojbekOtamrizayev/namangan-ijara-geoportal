with open('namangan_interaktiv_xarita.html', 'r', encoding='utf-8') as f:
    c = f.read()

# Check for districtView
idx = c.find('districtView')
print("districtView index:", idx)
print(c[idx:idx+200])

print("\n---\n")

# Check for drilldown-layout 
idx2 = c.find('drilldown-layout')
print("drilldown-layout index:", idx2)
print(c[idx2:idx2+200])

print("\n---\n")
# Check for view-container
idx3 = c.find('view-container')
print("view-container index:", idx3)
print(c[idx3:idx3+200])
