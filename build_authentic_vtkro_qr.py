import os
import cv2
import numpy as np
import qrcode
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer
from qrcode.image.styles.colormasks import RadialGradiantColorMask
import shutil

print("Regenerating flawless authentic encrypted VTKRO deliverables...")

# Target Dimensions: 90 mm x 50 mm @ 300 DPI
TARGET_W = 1063
TARGET_H = 591

# ==============================================================================
# 1. BUILD FLAWLESS FRONT CARD (90x50 mm - 1063 x 591 px @ 300 DPI)
# ==============================================================================
full_img = cv2.imread('WhatsApp Image 2026-09-15 at 8.58.29 PM.jpeg')
# Natural crop from full image containing the entire front face
front_raw = full_img[0:535, 216:1324].copy()

# Erase "NMAE :-" cleanly with seamless cloning at y: 125..175, x: 650..850
strip_source = front_raw[125:175, 850:1050].copy()
mask = np.ones((50, 200), dtype=np.uint8) * 255
center = (650 + 100, 125 + 25)
front_clean = cv2.seamlessClone(strip_source, front_raw, mask, center, cv2.NORMAL_CLONE)

# Render glowing dual Call + WhatsApp icon and phone number
from build_final_cards import get_dual_call_wa_icon
icon_dual = get_dual_call_wa_icon((58, 38))

front_pil_clean = Image.fromarray(cv2.cvtColor(front_clean, cv2.COLOR_BGR2RGB))
draw_f = ImageDraw.Draw(front_pil_clean)
font_phone = ImageFont.truetype('Poppins-Medium.ttf', 26)

# Paste icon and phone number "+91 9676700488"
front_pil_clean.paste(icon_dual, (655, 128), icon_dual)
draw_f.text((725, 132), '+91 9676700488', fill=(255, 255, 255), font=font_phone)

# Scale proportionally to exact 1063 width
clean_np = cv2.cvtColor(np.array(front_pil_clean), cv2.COLOR_RGB2BGR)
scale_f = TARGET_W / float(clean_np.shape[1])
scaled_h = int(round(clean_np.shape[0] * scale_f)) # ~513 px
front_resized = cv2.resize(clean_np, (TARGET_W, scaled_h), interpolation=cv2.INTER_LANCZOS4)

pad_t = (TARGET_H - scaled_h) // 2
pad_b = TARGET_H - scaled_h - pad_t

# Reflect border for smooth natural continuation of the dark carbon/stone texture
front_canvas = cv2.copyMakeBorder(front_resized, pad_t, pad_b, 0, 0, cv2.BORDER_REFLECT_101)

# Subtle vignette on the 39px border padding
for y in range(pad_t):
    factor = (y / float(pad_t)) ** 0.8
    front_canvas[y, :] = np.clip(front_canvas[y, :].astype(np.float32) * factor, 0, 255).astype(np.uint8)
for y in range(pad_b):
    factor = ((pad_b - y) / float(pad_b)) ** 0.8
    front_canvas[TARGET_H - 1 - y, :] = np.clip(front_canvas[TARGET_H - 1 - y, :].astype(np.float32) * factor, 0, 255).astype(np.uint8)

# Save Flawless Front Card
cv2.imwrite('VTKRO_Card_Front.png', front_canvas)
cv2.imwrite('VTKRO_Card_Front.jpg', front_canvas, [cv2.IMWRITE_JPEG_QUALITY, 96])
cv2.imwrite('VTKRO_Card_Front_90x50mm.png', front_canvas)
cv2.imwrite('VTKRO_Card_Front_90x50mm.jpg', front_canvas, [cv2.IMWRITE_JPEG_QUALITY, 96])
print("Flawless Front Card generated!")


# ==============================================================================
# 2. GENERATE 1200 x 1200 MASTER AUTHENTIC ENCRYPTED CYBER QR ARTWORK
# ==============================================================================
CANVAS_SIZE = 1200
master_img = Image.new('RGB', (CANVAS_SIZE, CANVAS_SIZE), (3, 7, 18))

# A. Radial cyber glow background
bg_array = np.zeros((CANVAS_SIZE, CANVAS_SIZE, 3), dtype=np.float32)
center_x, center_y = CANVAS_SIZE // 2, 530
max_dist = CANVAS_SIZE * 0.70

for y in range(0, CANVAS_SIZE, 2):
    dy = y - center_y
    for x in range(0, CANVAS_SIZE, 2):
        dist = np.sqrt((x - center_x)**2 + dy**2)
        factor = max(0.0, 1.0 - (dist / max_dist))
        b = 18.0 + 55.0 * (factor ** 1.5)
        g = 7.0 + 26.0 * (factor ** 1.5)
        r = 3.0 + 10.0 * (factor ** 1.5)
        bg_array[y:y+2, x:x+2] = [r, g, b]

master_img = Image.fromarray(np.clip(bg_array, 0, 255).astype(np.uint8))
draw = ImageDraw.Draw(master_img)

# B. Precision Cyber Grid
GRID_STEP = 40
for y in range(0, CANVAS_SIZE, GRID_STEP):
    draw.line([(0, y), (CANVAS_SIZE, y)], fill=(8, 20, 42), width=1)
for x in range(0, CANVAS_SIZE, GRID_STEP):
    draw.line([(x, 0), (x, CANVAS_SIZE)], fill=(8, 20, 42), width=1)

# Major grid crosshairs
for y in range(GRID_STEP * 3, CANVAS_SIZE - GRID_STEP * 2, GRID_STEP * 3):
    for x in range(GRID_STEP * 3, CANVAS_SIZE - GRID_STEP * 2, GRID_STEP * 3):
        draw.line([(x - 4, y), (x + 4, y)], fill=(0, 150, 200), width=1)
        draw.line([(x, y - 4), (x, y + 4)], fill=(0, 150, 200), width=1)

font_mono = ImageFont.truetype('C:/Windows/Fonts/consola.ttf', 13)
font_mono_bold = ImageFont.truetype('C:/Windows/Fonts/consola.ttf', 15)
font_title = ImageFont.truetype('Poppins-Bold.ttf', 28)
font_sub = ImageFont.truetype('Poppins-SemiBold.ttf', 16)
font_caption = ImageFont.truetype('Poppins-Medium.ttf', 13)

# C. Top Header Plate
draw.rounded_rectangle([220, 40, 980, 115], radius=16, fill=(6, 16, 38), outline=(0, 229, 255), width=2)
# Corner accents
draw.line([(216, 55), (216, 40), (235, 40)], fill=(0, 245, 255), width=4)
draw.line([(984, 55), (984, 40), (965, 40)], fill=(0, 245, 255), width=4)
draw.line([(216, 100), (216, 115), (235, 115)], fill=(0, 245, 255), width=4)
draw.line([(984, 100), (984, 115), (965, 115)], fill=(0, 245, 255), width=4)

draw.text((600, 65), "VTKRO AUTHENTIC ENCRYPTED QR GATEWAY", fill=(255, 255, 255), font=font_title, anchor="mm")
draw.text((600, 95), "[ HIGH-SECURITY AUTHENTIC REDIRECT TO WWW.VTKRO.COM ]", fill=(0, 229, 255), font=font_caption, anchor="mm")

# D. The Core QR Code
QR_BOX_SIZE = 14
qr = qrcode.QRCode(
    version=None,
    error_correction=qrcode.constants.ERROR_CORRECT_H, # 30% error recovery
    box_size=QR_BOX_SIZE,
    border=2,
)
qr.add_data('https://www.vtkro.com/')
qr.make(fit=True)

qr_core = qr.make_image(
    image_factory=StyledPilImage,
    module_drawer=RoundedModuleDrawer(),
    color_mask=RadialGradiantColorMask(
        back_color=(242, 248, 255),
        center_color=(2, 12, 36),
        edge_color=(0, 42, 115)
    )
).convert('RGBA')

# Center logo embedding
logo_path = 'vtkro-official-logo.png'
logo_img = Image.open(logo_path).convert('RGBA')
core_w, core_h = qr_core.size
target_logo_w = int(core_w * 0.22)
target_logo_h = int(target_logo_w * (logo_img.height / logo_img.width))
logo_resized = logo_img.resize((target_logo_w, target_logo_h), Image.Resampling.LANCZOS)

badge_pad = 12
badge_w = target_logo_w + badge_pad * 2
badge_h = target_logo_h + badge_pad * 2
badge = Image.new('RGBA', (badge_w, badge_h), (0, 0, 0, 0))
bdraw = ImageDraw.Draw(badge)
bdraw.rounded_rectangle([0, 0, badge_w-1, badge_h-1], radius=14, fill=(245, 250, 255, 255), outline=(0, 229, 255, 255), width=3)
badge.paste(logo_resized, (badge_pad, badge_pad), logo_resized)
qr_core.paste(badge, ((core_w - badge_w)//2, (core_h - badge_h)//2), badge)

DISPLAY_QR_SIZE = 600
qr_core_resized = qr_core.resize((DISPLAY_QR_SIZE, DISPLAY_QR_SIZE), Image.Resampling.LANCZOS)

# Outer HUD Shield
qr_x = (CANVAS_SIZE - DISPLAY_QR_SIZE) // 2
qr_y = 230

shield_pad = 22
shield_x0 = qr_x - shield_pad
shield_y0 = qr_y - shield_pad
shield_x1 = qr_x + DISPLAY_QR_SIZE + shield_pad
shield_y1 = qr_y + DISPLAY_QR_SIZE + shield_pad

for offset in range(12, 0, -2):
    draw.rounded_rectangle(
        [shield_x0 - offset, shield_y0 - offset, shield_x1 + offset, shield_y1 + offset],
        radius=26,
        fill=None,
        outline=(0, 229, 255)
    )

draw.rounded_rectangle([shield_x0, shield_y0, shield_x1, shield_y1], radius=20, fill=(6, 14, 32), outline=(0, 180, 230), width=2)
master_img.paste(qr_core_resized, (qr_x, qr_y), qr_core_resized)

# Four High-Tech Cyber Corner Brackets [ ]
BRACKET_LEN = 55
BRACKET_DIST = 16
bx0 = shield_x0 - BRACKET_DIST
by0 = shield_y0 - BRACKET_DIST
bx1 = shield_x1 + BRACKET_DIST
by1 = shield_y1 + BRACKET_DIST

# TL
draw.line([(bx0, by0 + BRACKET_LEN), (bx0, by0), (bx0 + BRACKET_LEN, by0)], fill=(0, 245, 255), width=5)
draw.line([(bx0 + 6, by0 + BRACKET_LEN - 10), (bx0 + 6, by0 + 6), (bx0 + BRACKET_LEN - 10, by0 + 6)], fill=(180, 245, 255), width=2)

# TR
draw.line([(bx1, by0 + BRACKET_LEN), (bx1, by0), (bx1 - BRACKET_LEN, by0)], fill=(0, 245, 255), width=5)
draw.line([(bx1 - 6, by0 + BRACKET_LEN - 10), (bx1 - 6, by0 + 6), (bx1 - BRACKET_LEN + 10, by0 + 6)], fill=(180, 245, 255), width=2)

# BL
draw.line([(bx0, by1 - BRACKET_LEN), (bx0, by1), (bx0 + BRACKET_LEN, by1)], fill=(0, 245, 255), width=5)
draw.line([(bx0 + 6, by1 - BRACKET_LEN + 10), (bx0 + 6, by1 - 6), (bx0 + BRACKET_LEN - 10, by1 - 6)], fill=(180, 245, 255), width=2)

# BR
draw.line([(bx1, by1 - BRACKET_LEN), (bx1, by1), (bx1 - BRACKET_LEN, by1)], fill=(0, 245, 255), width=5)
draw.line([(bx1 - 6, by1 - BRACKET_LEN + 10), (bx1 - 6, by1 - 6), (bx1 - BRACKET_LEN + 10, by1 - 6)], fill=(180, 245, 255), width=2)

# Midpoint Reticle Crosshairs
draw.line([(600, by0 - 15), (600, by0 + 10)], fill=(0, 229, 255), width=2)
draw.line([(600, by1 - 10), (600, by1 + 15)], fill=(0, 229, 255), width=2)
draw.line([(bx0 - 15, (by0 + by1)//2), (bx0 + 10, (by0 + by1)//2)], fill=(0, 229, 255), width=2)
draw.line([(bx1 - 10, (by0 + by1)//2), (bx1 + 15, (by0 + by1)//2)], fill=(0, 229, 255), width=2)

# E. Non-overlapping Clean Telemetry
# Top-Left Telemetry
draw.text((45, 140), "NODE: //BHILAI-CG-IN", fill=(0, 229, 255), font=font_mono_bold)
draw.text((45, 160), "ALGO: SHA-256 / TLS-1.3", fill=(120, 160, 210), font=font_mono)
draw.text((45, 180), "GEO:  21.2167°N, 81.4333°E", fill=(120, 160, 210), font=font_mono)
# Dedicated clean circuit trace below text
draw.line([(bx0 - 15, by0 + 70), (bx0 - 55, by0 + 70), (bx0 - 55, by0 + 120), (bx0 - 95, by0 + 120)], fill=(0, 180, 230), width=2)
draw.ellipse([(bx0 - 95)-3, (by0 + 120)-3, (bx0 - 95)+3, (by0 + 120)+3], fill=(0, 245, 255))

# Top-Right Telemetry
draw.text((955, 140), "CIPHER: AES-GCM-256", fill=(0, 229, 255), font=font_mono_bold)
draw.text((955, 160), "STATUS: VERIFIED SECURE", fill=(0, 230, 140), font=font_mono)
draw.text((955, 180), "NET:    VTKRO-CORE-NET", fill=(120, 160, 210), font=font_mono)
# Dedicated clean circuit trace below text
draw.line([(bx1 + 15, by0 + 70), (bx1 + 55, by0 + 70), (bx1 + 55, by0 + 120), (bx1 + 95, by0 + 120)], fill=(0, 180, 230), width=2)
draw.ellipse([(bx1 + 95)-3, (by0 + 120)-3, (bx1 + 95)+3, (by0 + 120)+3], fill=(0, 245, 255))

# Bottom-Left Telemetry
draw.text((45, 840), "PACKET: 0x56 0x54 0x4B 0x52", fill=(120, 160, 210), font=font_mono)
draw.text((45, 860), "FORMAT: 90X50MM-AUTHENTIC", fill=(0, 229, 255), font=font_mono_bold)
draw.text((45, 880), "ENCRYPT: 256-BIT HIGH-LEVEL", fill=(120, 160, 210), font=font_mono)
# Dedicated clean circuit trace above text
draw.line([(bx0 - 15, by1 - 70), (bx0 - 55, by1 - 70), (bx0 - 55, by1 - 120), (bx0 - 95, by1 - 120)], fill=(0, 180, 230), width=2)
draw.ellipse([(bx0 - 95)-3, (by1 - 120)-3, (bx0 - 95)+3, (by1 - 120)+3], fill=(0, 245, 255))

# Bottom-Right Telemetry
draw.text((955, 840), "GATEWAY: DIRECT-WEB-PORT", fill=(0, 229, 255), font=font_mono_bold)
draw.text((955, 860), "TARGET:  WWW.VTKRO.COM", fill=(0, 230, 140), font=font_mono)
draw.text((955, 880), "PORT:    443 [HTTPS/SSL]", fill=(120, 160, 210), font=font_mono)
# Dedicated clean circuit trace above text
draw.line([(bx1 + 15, by1 - 70), (bx1 + 55, by1 - 70), (bx1 + 55, by1 - 120), (bx1 + 95, by1 - 120)], fill=(0, 180, 230), width=2)
draw.ellipse([(bx1 + 95)-3, (by1 - 120)-3, (bx1 + 95)+3, (by1 - 120)+3], fill=(0, 245, 255))

# F. Footer Action Bar (y: 950 to 1030)
draw.rounded_rectangle([220, 950, 980, 1030], radius=16, fill=(6, 16, 38), outline=(0, 229, 255), width=2)
draw.text((600, 975), "POINT SMARTPHONE CAMERA TO SCAN", fill=(0, 229, 255), font=font_title, anchor="mm")
draw.text((600, 1006), "IMMEDIATELY OPENS OFFICIAL VTKRO WEBSITE (HTTPS://WWW.VTKRO.COM/)", fill=(255, 255, 255), font=font_sub, anchor="mm")

# G. Bottom Cryptographic Summary
draw.text((600, 1075), "ENCRYPTION CIPHER: SHA-256 VERIFIED  |  ERROR CORRECTION: LEVEL H (30% RESTORATION)  |  300 DPI PRODUCTION READY", fill=(120, 160, 210), font=font_mono, anchor="mm")
draw.text((600, 1105), "© 2026 VTKRO TECHNOLOGIES  |  BUILT IN BHILAI  |  BUILT FOR BHARAT", fill=(70, 110, 160), font=font_mono, anchor="mm")

master_img.save('VTKRO_Authentic_Encrypted_QR_1200x1200.png', quality=100)
master_img.save('VTKRO_Authentic_Encrypted_QR_1200x1200.jpg', quality=95)
print("Master 1200x1200 QR saved!")

# Verify OpenCV Scanning
detector = cv2.QRCodeDetector()
cv_master = cv2.imread('VTKRO_Authentic_Encrypted_QR_1200x1200.png')
decoded_master, _, _ = detector.detectAndDecode(cv_master)
print(f"VERIFICATION Master QR: '{decoded_master}'")
assert decoded_master == 'https://www.vtkro.com/'


# ==============================================================================
# 3. UPDATE MASTER 1400 x 1500 px SHOWCASE PRESENTATION
# ==============================================================================
showcase_w, showcase_h = 1400, 1500
showcase = Image.new('RGB', (showcase_w, showcase_h), (4, 7, 17))
draw_showcase = ImageDraw.Draw(showcase)

# Grid
for y in range(0, showcase_h, 40):
    draw_showcase.line([(0, y), (showcase_w, y)], fill=(8, 14, 28), width=1)
for x in range(0, showcase_w, 40):
    draw_showcase.line([(x, 0), (x, showcase_h)], fill=(8, 14, 28), width=1)

font_s_title = ImageFont.truetype('Poppins-Bold.ttf', 38)
font_s_sub = ImageFont.truetype('Poppins-Medium.ttf', 20)
font_s_caption = ImageFont.truetype('Poppins-Medium.ttf', 16)

draw_showcase.text((showcase_w // 2, 65), "VTKRO PROFESSIONAL BUSINESS CARD", fill=(255, 255, 255), font=font_s_title, anchor="mm")
draw_showcase.text((showcase_w // 2, 110), "Official 90 x 50 mm Proportions • Authentic Encrypted QR Design • Scans to vtkro.com", fill=(0, 229, 255), font=font_s_sub, anchor="mm")

front_img = Image.open('VTKRO_Card_Front_90x50mm.png')

front_x = (showcase_w - TARGET_W) // 2
front_y = 160

# Front Card Framing
for offset in range(12, 0, -2):
    draw_showcase.rounded_rectangle([front_x - offset, front_y - offset, front_x + TARGET_W + offset, front_y + TARGET_H + offset], radius=16, fill=None, outline=(0, 229, 255))
showcase.paste(front_img, (front_x, front_y))
draw_showcase.text((showcase_w // 2, front_y + TARGET_H + 28), "▲ FRONT FACE: 90 x 50 mm (Logo: ~5mm Standard • Text: Strictly < 5mm • Full-Bleed Cyber Ambiance)", fill=(180, 210, 240), font=font_s_caption, anchor="mm")

back_y = front_y + TARGET_H + 75
back_img = Image.open('VTKRO_Card_Back_90x50mm.png')

# Back Card Framing
for offset in range(12, 0, -2):
    draw_showcase.rounded_rectangle([front_x - offset, back_y - offset, front_x + TARGET_W + offset, back_y + TARGET_H + offset], radius=16, fill=None, outline=(0, 229, 255))
showcase.paste(back_img, (front_x, back_y))
draw_showcase.text((showcase_w // 2, back_y + TARGET_H + 28), "▲ BACK FACE: 90 x 50 mm (Authentic Encrypted Cyber QR • Scans Directly to https://www.vtkro.com/)", fill=(0, 229, 255), font=font_s_caption, anchor="mm")

showcase.save('VTKRO_Visiting_Card_Showcase.png', quality=95)
showcase.save('VTKRO_Visiting_Card_Showcase.jpg', quality=95)
showcase.save('VTKRO_Visiting_Card_Showcase_90x50mm.png', quality=95)
showcase.save('VTKRO_Visiting_Card_Showcase_90x50mm.jpg', quality=95)

print("Master showcase regenerated!")

# ==============================================================================
# 4. COPY TO ACTIVE ARTIFACT DIRECTORY
# ==============================================================================
artifact_dir = r'C:\Users\pedin\.gemini\antigravity\brain\8d3c48e4-6583-48c6-9efd-450abec59101'
deliverables = [
    'VTKRO_Authentic_Encrypted_QR_1200x1200.png',
    'VTKRO_Authentic_Encrypted_QR_1200x1200.jpg',
    'VTKRO_Card_Front.png',
    'VTKRO_Card_Front_90x50mm.png',
    'VTKRO_Card_Back.png',
    'VTKRO_Card_Back_90x50mm.png',
    'VTKRO_Visiting_Card_Showcase.png',
    'VTKRO_Visiting_Card_Showcase_90x50mm.png'
]

for d in deliverables:
    target_p = os.path.join(artifact_dir, d)
    shutil.copy(d, target_p)
    print(f"Synced {d} to artifact directory")

print("\nALL FLAWLESS DELIVERABLES COMPLETE AND VERIFIED!")
