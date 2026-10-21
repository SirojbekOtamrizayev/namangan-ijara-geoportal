import cv2
import numpy as np
import json

img_path = r'C:/Users/AKT/.gemini/antigravity/brain/42055879-6243-4b91-b748-ee83f798369b/.user_uploaded/media_1792475783463_1d745236.png'
img = cv2.imread(img_path)
h, w = img.shape[:2]
print(f"Image dimensions: {w} x {h}")

# Background: dark blue [51, 34, 24] in BGR
diff_bg = np.linalg.norm(img.astype(float) - [51, 34, 24], axis=2)
is_bg = diff_bg < 28

# Text detection
is_white = (img[:, :, 0] > 180) & (img[:, :, 1] > 180) & (img[:, :, 2] > 180)

# Namangan shahri is roughly around (455..485, 245..275)
shahar_mask = np.zeros((h, w), dtype=bool)
shahar_mask[245:275, 455:485] = True

is_dark_text = (img[:, :, 0] < 50) & (img[:, :, 1] < 50) & (img[:, :, 2] < 50) & (~is_bg)
text_mask = ((is_white | is_dark_text) & (~shahar_mask)).astype(np.uint8) * 255

kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
text_mask = cv2.dilate(text_mask, kernel, iterations=1)
text_mask[is_bg] = 0

inpainted = cv2.inpaint(img, text_mask, 5, cv2.INPAINT_TELEA)

districts_info = [
    {'id': 'pop', 'name': 'Pop', 'color': [99, 121, 53], 'roi': (0, 0, 230, h), 'fill_color': '#357963'},
    {'id': 'chust', 'name': 'Chust', 'color': [159, 111, 47], 'roi': (190, 150, 390, 350), 'fill_color': '#2f6f9f'},
    {'id': 'mingbuloq', 'name': 'Mingbuloq', 'color': [58, 128, 176], 'roi': (250, 300, 480, h), 'fill_color': '#b0803a'},
    {'id': 'kosonsoy', 'name': 'Kosonsoy', 'color': [60, 83, 181], 'roi': (370, 100, 470, 270), 'fill_color': '#b5533c'},
    {'id': 'yangiqorgon', 'name': 'Yangiqo\'rg\'on', 'color': [110, 141, 60], 'roi': (420, 0, 520, 260), 'fill_color': '#3c8d6e'},
    {'id': 'chortoq', 'name': 'Chortoq', 'color': [159, 111, 47], 'roi': (470, 40, 570, 260), 'fill_color': '#2f6f9f'},
    {'id': 'toraqorgon', 'name': 'To\'raqo\'rg\'on', 'color': [166, 90, 122], 'roi': (350, 200, 435, 340), 'fill_color': '#7a5aa6'},
    {'id': 'namangan-tumani', 'name': 'Namangan tumani', 'color': [116, 122, 79], 'roi': (410, 230, 520, 340), 'fill_color': '#4f7a74'},
    {'id': 'uychi', 'name': 'Uychi', 'color': [58, 128, 176], 'roi': (530, 160, 600, 260), 'fill_color': '#b0803a'},
    {'id': 'uchqorgon', 'name': 'Uchqo\'rg\'on', 'color': [166, 90, 122], 'roi': (530, 160, w, 280), 'fill_color': '#7a5aa6'},
    {'id': 'norin', 'name': 'Norin', 'color': [60, 83, 181], 'roi': (500, 230, w, 320), 'fill_color': '#b5533c'},
    {'id': 'namangan-shahri', 'name': 'Namangan shahri', 'color': [122, 66, 18], 'roi': (450, 245, 490, 280), 'fill_color': '#12427a'}
]

results = []

for d in districts_info:
    target_c = np.array(d['color'])
    diff = np.linalg.norm(inpainted.astype(float) - target_c, axis=2)
    mask = (diff < 35).astype(np.uint8) * 255
    x1, y1, x2, y2 = d['roi']
    roi_mask = np.zeros_like(mask)
    roi_mask[y1:y2, x1:x2] = mask[y1:y2, x1:x2]
    
    # Close any small gaps
    roi_mask = cv2.morphologyEx(roi_mask, cv2.MORPH_CLOSE, np.ones((7, 7), np.uint8))
    
    cnts, _ = cv2.findContours(roi_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = [c for c in cnts if cv2.contourArea(c) > 100]
    
    if len(cnts) > 1:
        # Merge if multiple components (like user said: yozuv sababli bir tuman ikki bo'lakka bo'linib qolsa, birlashtir)
        # We can either take the union or bridge them
        merged_mask = np.zeros_like(roi_mask)
        for c in cnts:
            cv2.drawContours(merged_mask, [c], -1, 255, -1)
        # Dilate to connect then erode
        merged_mask = cv2.dilate(merged_mask, np.ones((9, 9), np.uint8))
        merged_mask = cv2.erode(merged_mask, np.ones((9, 9), np.uint8))
        cnts, _ = cv2.findContours(merged_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cnts = [c for c in cnts if cv2.contourArea(c) > 100]
    
    if len(cnts) == 0:
        print(f"ERROR: No contour for {d['name']}")
        continue
        
    main_cnt = max(cnts, key=cv2.contourArea)
    
    # Simplify polygon with approxPolyDP for clean SVG while keeping high accuracy
    epsilon = 0.0025 * cv2.arcLength(main_cnt, True)
    approx = cv2.approxPolyDP(main_cnt, epsilon, True)
    
    # Compute center for text placement
    M = cv2.moments(main_cnt)
    if M['m00'] != 0:
        cx = int(M['m10'] / M['m00'])
        cy = int(M['m01'] / M['m00'])
    else:
        cx, cy = approx[0][0]
        
    points_str = " ".join([f"{pt[0][0]},{pt[0][1]}" for pt in approx])
    
    results.append({
        'id': d['id'],
        'name': d['name'],
        'color': d['fill_color'],
        'points': points_str,
        'pt_count': len(approx),
        'center': [cx, cy],
        'area': int(cv2.contourArea(main_cnt))
    })
    print(f"{d['name']:16}: {len(approx)} points, center=({cx}, {cy}), area={cv2.contourArea(main_cnt):.0f}")

with open('scratch/districts_polygons.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, ensure_ascii=False, indent=2)
print("Saved to scratch/districts_polygons.json successfully!")
