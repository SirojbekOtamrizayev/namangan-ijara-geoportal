with open('scratch/inject_govtech_portal.py', 'r', encoding='utf-8') as f:
    code = f.read()

# Replace the topbar-right section where Admin button and User Profile are defined
old_block = """        <!-- Admin Button -->
        <button class="top-admin-btn" onclick="openAdminModal()" title="Admin boshqaruv paneli" style="background:linear-gradient(135deg, #0284c7 0%, #0369a1 100%); color:#fff; border:none; padding:6px 12px; border-radius:8px; font-weight:800; cursor:pointer;">
          <span>⚙️ Admin</span>
        </button>

        <!-- User Profile -->
        <div class="user-pill">
          <div class="user-avatar">👤</div>
          <span>ZAFAR IKRAMOV</span>
        </div>"""

if old_block in code:
    code = code.replace(old_block, "")
    print("Found and removed from inject_govtech_portal.py")
else:
    print("Could not find exact block in inject_govtech_portal.py")

with open('scratch/inject_govtech_portal.py', 'w', encoding='utf-8') as f:
    f.write(code)
