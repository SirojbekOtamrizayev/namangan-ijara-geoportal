import json

# Let's check node execution to parse the JS data directly using node!
node_script = """
const fs = require('fs');
// read src/data/namanganData.js
let content = fs.readFileSync('src/data/namanganData.js', 'utf8');
// remove export const
content = content.replace(/export const /g, 'const ');
content += '\\nmodule.exports = { DISTRICTS_DATA, CROPS_DATA };';
fs.writeFileSync('scratch/temp_data.cjs', content, 'utf8');
const data = require('./scratch/temp_data.cjs');
console.log('Districts count:', data.DISTRICTS_DATA.length);
console.log('Districts:', data.DISTRICTS_DATA.map(d => ({ id: d.id, name: d.name, mfysCount: d.mfys ? d.mfys.length : 0 })));
fs.writeFileSync('scratch/namangan_parsed_data.json', JSON.stringify(data.DISTRICTS_DATA, null, 2), 'utf8');
console.log('Saved to scratch/namangan_parsed_data.json');
"""

with open('scratch/extract_via_node.js', 'w', encoding='utf-8') as f:
    f.write(node_script)
