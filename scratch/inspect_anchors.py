with open('namangan_interaktiv_xarita.html', 'r', encoding='utf-8') as f:
    orig = f.read()

# Let's find key anchors
head_end = orig.find('</head>')
body_start = orig.find('<body>')
header_start = orig.find('<header>')
main_start = orig.find('<main class="grid">')
main_end = orig.find('</main>')
body_end = orig.find('</body>')

print("head_end:", head_end)
print("body_start:", body_start)
print("header_start:", header_start)
print("main_start:", main_start)
print("main_end:", main_end)
print("body_end:", body_end)
