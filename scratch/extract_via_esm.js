import fs from 'fs';
import { DISTRICTS_DATA } from '../src/data/namanganData.js';

console.log('Districts count:', DISTRICTS_DATA.length);
console.log('Districts:', DISTRICTS_DATA.map(d => ({ id: d.id, name: d.name, mfysCount: d.mfys ? d.mfys.length : 0 })));
fs.writeFileSync('scratch/namangan_parsed_data.json', JSON.stringify(DISTRICTS_DATA, null, 2), 'utf8');
console.log('Saved to scratch/namangan_parsed_data.json successfully!');
