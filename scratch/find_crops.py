with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()
import re
crops = re.findall(r'"Mahsulot nomi":\s*"([^"]+)"', c)
print('Template crops found:', set(crops))
