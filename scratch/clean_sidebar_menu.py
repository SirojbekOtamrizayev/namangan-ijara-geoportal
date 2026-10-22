files = ['index.html', 'namangan_interaktiv_xarita.html', 'public/namangan_interaktiv_xarita.html']

old_menu_items = """      <div class="menu-item" onclick="switchMainView('stats')">
        <span class="menu-icon">📋</span>
        <span>Asosiy ro'yxat</span>
      </div>
      <div class="menu-item" onclick="switchMainView('stats')">
        <span class="menu-icon">🛡️</span>
        <span>Mehnat inspeksiyasi</span>
        <span class="menu-arrow">⌄</span>
      </div>
      <div class="menu-item" onclick="switchMainView('stats')">
        <span class="menu-icon">📈</span>
        <span>Hisobotlar</span>
        <span class="menu-arrow">⌄</span>
      </div>
      <div class="menu-item" onclick="switchMainView('stats')">
        <span class="menu-icon">💼</span>
        <span>Investitsiya loyihalari</span>
      </div>"""

new_menu_items = """      <div class="menu-item" onclick="switchMainView('stats')">
        <span class="menu-icon">📈</span>
        <span>Hisobotlar</span>
        <span class="menu-arrow">⌄</span>
      </div>"""

for filepath in files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    cn = content.replace('\r\n', '\n')
    old_norm = old_menu_items.replace('\r\n', '\n')
    
    if old_norm in cn:
        cn = cn.replace(old_norm, new_menu_items)
        print(f"Updated menu in {filepath}")
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(cn)
    else:
        print(f"NOT FOUND in {filepath}")
