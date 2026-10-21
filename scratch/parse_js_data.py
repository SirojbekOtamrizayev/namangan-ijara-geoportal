import re
import json

with open('src/data/namanganData.js', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's inspect the districts in DISTRICTS_DATA
# DISTRICTS_DATA is an array of objects: id, name, ..., mfys: [...]
# We can find all { id: 'pop', name: 'Pop tumani', ... }
district_blocks = re.split(r'\{\s*id:\s*[\'"]([a-z0-9\-]+)[\'"],\s*name:\s*[\'"]([^\'"]+)[\'"]', text)

print(f"Total parts split: {len(district_blocks)}")
for i in range(1, len(district_blocks), 3):
    d_id = district_blocks[i]
    d_name = district_blocks[i+1]
    print(f"District: {d_id} -> {d_name}")
