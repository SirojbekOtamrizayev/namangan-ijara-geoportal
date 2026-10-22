files = ['index.html', 'namangan_interaktiv_xarita.html', 'public/namangan_interaktiv_xarita.html']

old_block = """        <!-- Admin Button -->
        <button class="top-admin-btn" onclick="openAdminModal()" title="Admin boshqaruv paneli" style="background:linear-gradient(135deg, #0284c7 0%, #0369a1 100%); color:#fff; border:none; padding:6px 12px; border-radius:8px; font-weight:800; cursor:pointer;">
          <span>⚙️ Admin</span>
        </button>

        <!-- User Profile -->
        <div class="user-pill">
          <div class="user-avatar">👤</div>
          <span>ZAFAR IKRAMOV</span>
        </div>"""

for filepath in files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Try direct replacement
    if old_block in content:
        content = content.replace(old_block, "")
        print(f"Direct match replaced in {filepath}")
    else:
        # Normalize CRLF / LF
        content_norm = content.replace('\r\n', '\n')
        old_norm = old_block.replace('\r\n', '\n')
        if old_norm in content_norm:
            content_norm = content_norm.replace(old_norm, "")
            content = content_norm
            print(f"Normalized match replaced in {filepath}")
        else:
            print(f"NOT FOUND in {filepath}")
            
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
