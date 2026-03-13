#!/usr/bin/env python3
"""국내 견과류 비교 인포그래픽 이미지 생성"""

from PIL import Image, ImageDraw, ImageFont
import math

# ===== Config =====
W, H = 1200, 4200
BG = (15, 17, 23)
CARD_BG = (26, 29, 39)
BORDER = (45, 49, 72)
TEXT_WHITE = (232, 232, 237)
TEXT_MUTED = (156, 163, 175)
AMBER = (245, 158, 11)
GREEN = (16, 185, 129)
PURPLE = (99, 102, 241)
PINK = (236, 72, 153)
RED = (239, 68, 68)
TEAL = (20, 184, 166)

# Fonts
def get_font(size, bold=False):
    paths = [
        '/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc' if bold else '/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc',
        '/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc',
        '/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc',
    ]
    for p in paths:
        try:
            return ImageFont.truetype(p, size)
        except:
            continue
    return ImageFont.load_default()

font_title = get_font(52, bold=True)
font_subtitle = get_font(32, bold=True)
font_section = get_font(36, bold=True)
font_body = get_font(22)
font_body_bold = get_font(22, bold=True)
font_small = get_font(18)
font_small_bold = get_font(18, bold=True)
font_big_num = get_font(42, bold=True)
font_label = get_font(16)
font_hero_sub = get_font(26)

# ===== Nut Data =====
nuts = [
    {"name": "아몬드", "icon": "🥜", "cal": 579, "protein": 21.2, "fat": 49.9, "fiber": 12.5, "vite": 25.6, "price": 3500, "color": AMBER,
     "benefit": "피부 건강 · 항산화 · 혈당 조절", "intake": "23알 (30g)"},
    {"name": "호두", "icon": "🧠", "cal": 654, "protein": 15.2, "fat": 65.2, "fiber": 6.7, "vite": 0.7, "price": 4200, "color": PURPLE,
     "benefit": "두뇌 건강 · 기억력 향상 · 수면 개선", "intake": "7~8알 (30g)"},
    {"name": "캐슈넛", "icon": "🌰", "cal": 553, "protein": 18.2, "fat": 43.8, "fiber": 3.3, "vite": 0.9, "price": 3800, "color": GREEN,
     "benefit": "빈혈 예방 · 면역력 강화 · 다이어트", "intake": "15~18알 (30g)"},
    {"name": "마카다미아", "icon": "⚪", "cal": 718, "protein": 7.9, "fat": 75.8, "fiber": 8.6, "vite": 0.5, "price": 6500, "color": PINK,
     "benefit": "심혈관 건강 · 콜레스테롤 관리", "intake": "10~12알 (30g)"},
    {"name": "피스타치오", "icon": "💚", "cal": 560, "protein": 20.2, "fat": 45.3, "fiber": 10.6, "vite": 2.9, "price": 4500, "color": (34, 197, 94),
     "benefit": "눈 건강 · 혈당 조절 · 비타민B6", "intake": "49알 (30g)"},
    {"name": "땅콩", "icon": "🥜", "cal": 567, "protein": 25.8, "fat": 49.2, "fiber": 8.5, "vite": 8.3, "price": 1500, "color": RED,
     "benefit": "근육 생성 · 에너지 공급 · 가성비", "intake": "20~25알 (30g)"},
    {"name": "브라질너트", "icon": "🌿", "cal": 659, "protein": 14.3, "fat": 67.1, "fiber": 7.5, "vite": 5.7, "price": 7000, "color": TEAL,
     "benefit": "갑상선 건강 · 항산화 · 면역 강화", "intake": "1~2알 (10g)"},
    {"name": "헤이즐넛", "icon": "🤎", "cal": 628, "protein": 15.0, "fat": 60.8, "fiber": 9.7, "vite": 15.0, "price": 4000, "color": (168, 85, 247),
     "benefit": "피부 노화 방지 · 혈관 건강 · 엽산", "intake": "20알 (30g)"},
]

# ===== Drawing Helpers =====
def rounded_rect(draw, xy, radius, fill=None, outline=None, width=1):
    x1, y1, x2, y2 = xy
    draw.rounded_rectangle(xy, radius=radius, fill=fill, outline=outline, width=width)

def draw_bar(draw, x, y, w, h, fill_pct, color, radius=6):
    rounded_rect(draw, (x, y, x+w, y+h), radius, fill=(30, 33, 45))
    fw = max(int(w * fill_pct), radius * 2)
    rounded_rect(draw, (x, y, x+fw, y+h), radius, fill=color)

def text_center(draw, text, y, font, fill=TEXT_WHITE):
    bbox = draw.textbbox((0, 0), text, font=font)
    tw = bbox[2] - bbox[0]
    draw.text(((W - tw) // 2, y), text, font=font, fill=fill)

def gradient_color(c1, c2, t):
    return tuple(int(c1[i] + (c2[i] - c1[i]) * t) for i in range(3))

# ===== Create Image =====
img = Image.new('RGB', (W, H), BG)
draw = ImageDraw.Draw(img)

y = 0

# ===== HERO SECTION =====
# Background glow
for i in range(200):
    alpha = 1 - i / 200
    c = int(30 * alpha)
    draw.ellipse((100 - i*2, 40 - i, 500 + i*2, 240 + i), fill=(c + 15, int(c * 0.6) + 17, 23))
    draw.ellipse((600 - i*2, 60 - i, 1100 + i*2, 260 + i), fill=(15, 17, int(c * 0.8) + 23))

y = 60
text_center(draw, "KOREAN NUTS INFOGRAPHIC", y, font_small_bold, AMBER)
y += 50
text_center(draw, "국내 견과류", y, font_title, TEXT_WHITE)
y += 70
text_center(draw, "완벽 비교 가이드", y, font_title, AMBER)
y += 80
text_center(draw, "영양소 · 칼로리 · 효능 · 가격까지 한눈에 비교", y, font_hero_sub, TEXT_MUTED)
y += 50

# Divider line
draw.line((200, y, W - 200, y), fill=BORDER, width=1)
y += 50

# ===== SECTION 1: OVERVIEW CARDS =====
text_center(draw, "견과류 한눈에 보기", y, font_section, TEXT_WHITE)
y += 50
text_center(draw, "100g 기준 주요 영양 정보", y, font_body, TEXT_MUTED)
y += 60

# 2 columns x 4 rows of cards
card_w = 530
card_h = 140
card_gap = 24
col_start = [60, W - 60 - card_w]

for i, nut in enumerate(nuts):
    col = i % 2
    row = i // 2
    cx = col_start[col]
    cy = y + row * (card_h + card_gap)

    # Card background
    rounded_rect(draw, (cx, cy, cx + card_w, cy + card_h), 14, fill=CARD_BG, outline=BORDER, width=1)

    # Color accent bar on left
    draw.rounded_rectangle((cx, cy, cx + 6, cy + card_h), radius=3, fill=nut["color"])

    # Name and calories
    draw.text((cx + 24, cy + 16), nut["name"], font=font_subtitle, fill=TEXT_WHITE)
    cal_text = f'{nut["cal"]} kcal'
    bbox = draw.textbbox((0, 0), cal_text, font=font_body_bold)
    draw.text((cx + card_w - 24 - (bbox[2] - bbox[0]), cy + 20), cal_text, font=font_body_bold, fill=nut["color"])

    # Benefits
    draw.text((cx + 24, cy + 60), nut["benefit"], font=font_small, fill=TEXT_MUTED)

    # Daily intake
    draw.text((cx + 24, cy + 90), f'하루 권장: {nut["intake"]}', font=font_small, fill=gradient_color(nut["color"], TEXT_WHITE, 0.3))

y += 4 * (card_h + card_gap) + 40

# Divider
draw.line((100, y, W - 100, y), fill=BORDER, width=1)
y += 50

# ===== SECTION 2: CALORIE CHART =====
text_center(draw, "칼로리 비교", y, font_section, TEXT_WHITE)
y += 50
text_center(draw, "100g 기준 (kcal)", y, font_body, TEXT_MUTED)
y += 50

max_cal = max(n["cal"] for n in nuts)
sorted_nuts_cal = sorted(nuts, key=lambda x: x["cal"], reverse=True)

for i, nut in enumerate(sorted_nuts_cal):
    bar_x = 180
    bar_w = 700
    bar_h = 30
    by = y + i * 52

    draw.text((30, by + 2), nut["name"], font=font_body_bold, fill=TEXT_WHITE)
    pct = nut["cal"] / max_cal
    draw_bar(draw, bar_x, by, bar_w, bar_h, pct, nut["color"])
    draw.text((bar_x + bar_w + 16, by + 2), f'{nut["cal"]}', font=font_body_bold, fill=nut["color"])

y += 8 * 52 + 30

# Divider
draw.line((100, y, W - 100, y), fill=BORDER, width=1)
y += 50

# ===== SECTION 3: PROTEIN CHART =====
text_center(draw, "단백질 비교", y, font_section, TEXT_WHITE)
y += 50
text_center(draw, "100g 기준 (g)", y, font_body, TEXT_MUTED)
y += 50

max_protein = max(n["protein"] for n in nuts)
sorted_nuts_prot = sorted(nuts, key=lambda x: x["protein"], reverse=True)

for i, nut in enumerate(sorted_nuts_prot):
    bar_x = 180
    bar_w = 700
    bar_h = 30
    by = y + i * 52

    draw.text((30, by + 2), nut["name"], font=font_body_bold, fill=TEXT_WHITE)
    pct = nut["protein"] / max_protein
    draw_bar(draw, bar_x, by, bar_w, bar_h, pct, nut["color"])
    draw.text((bar_x + bar_w + 16, by + 2), f'{nut["protein"]}g', font=font_body_bold, fill=nut["color"])

y += 8 * 52 + 30

# Divider
draw.line((100, y, W - 100, y), fill=BORDER, width=1)
y += 50

# ===== SECTION 4: FAT CHART =====
text_center(draw, "지방 비교", y, font_section, TEXT_WHITE)
y += 50
text_center(draw, "100g 기준 (g)", y, font_body, TEXT_MUTED)
y += 50

max_fat = max(n["fat"] for n in nuts)
sorted_nuts_fat = sorted(nuts, key=lambda x: x["fat"], reverse=True)

for i, nut in enumerate(sorted_nuts_fat):
    bar_x = 180
    bar_w = 700
    bar_h = 30
    by = y + i * 52

    draw.text((30, by + 2), nut["name"], font=font_body_bold, fill=TEXT_WHITE)
    pct = nut["fat"] / max_fat
    draw_bar(draw, bar_x, by, bar_w, bar_h, pct, nut["color"])
    draw.text((bar_x + bar_w + 16, by + 2), f'{nut["fat"]}g', font=font_body_bold, fill=nut["color"])

y += 8 * 52 + 30

# Divider
draw.line((100, y, W - 100, y), fill=BORDER, width=1)
y += 50

# ===== SECTION 5: PRICE COMPARISON =====
text_center(draw, "국내 시중 가격 비교", y, font_section, TEXT_WHITE)
y += 50
text_center(draw, "100g 기준 평균 소비자가 (원)", y, font_body, TEXT_MUTED)
y += 60

max_price = max(n["price"] for n in nuts)
bar_area_h = 220
bar_bottom = y + bar_area_h
bar_w_each = 80
total_bars_w = len(nuts) * bar_w_each + (len(nuts) - 1) * 30
start_x = (W - total_bars_w) // 2

for i, nut in enumerate(nuts):
    bx = start_x + i * (bar_w_each + 30)
    pct = nut["price"] / max_price
    bh = int(bar_area_h * pct)

    # Bar
    rounded_rect(draw, (bx, bar_bottom - bh, bx + bar_w_each, bar_bottom), 8, fill=nut["color"])

    # Price on top
    price_text = f'{nut["price"]:,}'
    bbox = draw.textbbox((0, 0), price_text, font=font_small_bold)
    tw = bbox[2] - bbox[0]
    draw.text((bx + (bar_w_each - tw) // 2, bar_bottom - bh - 28), price_text, font=font_small_bold, fill=nut["color"])

    # Name below
    bbox = draw.textbbox((0, 0), nut["name"], font=font_small)
    tw = bbox[2] - bbox[0]
    draw.text((bx + (bar_w_each - tw) // 2, bar_bottom + 10), nut["name"], font=font_small, fill=TEXT_MUTED)

y = bar_bottom + 50

# Note
text_center(draw, "※ 가격은 시중 평균가 기준이며, 브랜드/원산지에 따라 달라질 수 있습니다", y, font_label, TEXT_MUTED)
y += 50

# Divider
draw.line((100, y, W - 100, y), fill=BORDER, width=1)
y += 50

# ===== SECTION 6: BEST FOR =====
text_center(draw, "목적별 추천 견과류", y, font_section, TEXT_WHITE)
y += 60

recommendations = [
    ("🧠  두뇌 건강", "호두", "오메가3 지방산이 풍부", PURPLE),
    ("💪  근육 생성", "땅콩", "단백질 25.8g / 100g", RED),
    ("✨  피부 미용", "아몬드", "비타민E 25.6mg / 100g", AMBER),
    ("❤️  심혈관 건강", "마카다미아", "올레산(단일불포화지방) 최다", PINK),
    ("🦴  뼈 건강", "아몬드", "칼슘 269mg / 100g", AMBER),
    ("🛡️  면역력 강화", "브라질너트", "셀레늄 1917mcg / 100g", TEAL),
    ("👁️  눈 건강", "피스타치오", "루테인·제아잔틴 풍부", (34, 197, 94)),
    ("⚡  다이어트", "캐슈넛", "칼로리 대비 포만감 우수", GREEN),
]

rec_card_w = 530
rec_card_h = 80
cols = [60, W - 60 - rec_card_w]

for i, (purpose, nut_name, reason, color) in enumerate(recommendations):
    col = i % 2
    row = i // 2
    cx = cols[col]
    cy = y + row * (rec_card_h + 16)

    rounded_rect(draw, (cx, cy, cx + rec_card_w, cy + rec_card_h), 12, fill=CARD_BG, outline=BORDER, width=1)
    draw.rounded_rectangle((cx, cy, cx + 6, cy + rec_card_h), radius=3, fill=color)

    draw.text((cx + 24, cy + 10), purpose, font=font_body, fill=TEXT_WHITE)
    draw.text((cx + 24, cy + 44), f'{nut_name}  ·  {reason}', font=font_small, fill=color)

y += 4 * (rec_card_h + 16) + 30

# Divider
draw.line((100, y, W - 100, y), fill=BORDER, width=1)
y += 50

# ===== SECTION 7: TIPS =====
text_center(draw, "견과류 섭취 꿀팁", y, font_section, TEXT_WHITE)
y += 60

tips = [
    ("01", "하루 한 줌(30g)", "견과류는 칼로리가 높으므로\n하루 한 줌(약 30g)이 적정량입니다."),
    ("02", "생견과 > 볶음견과", "볶거나 소금 첨가 시 영양소 파괴,\n나트륨 증가. 생견과를 선택하세요."),
    ("03", "밀봉 냉장 보관", "불포화지방산은 산화되기 쉽습니다.\n밀봉하여 냉장 보관이 최선입니다."),
    ("04", "다양하게 섭취", "여러 종류를 혼합 섭취하면\n다양한 영양소를 균형 있게 섭취!"),
]

tip_w = 530
tip_h = 120
tip_cols = [60, W - 60 - tip_w]

for i, (num, title, desc) in enumerate(tips):
    col = i % 2
    row = i // 2
    cx = tip_cols[col]
    cy = y + row * (tip_h + 16)

    rounded_rect(draw, (cx, cy, cx + tip_w, cy + tip_h), 12, fill=CARD_BG, outline=BORDER, width=1)

    # Big number
    draw.text((cx + 20, cy + 12), num, font=font_big_num, fill=AMBER)

    # Title & desc
    draw.text((cx + 100, cy + 14), title, font=font_body_bold, fill=TEXT_WHITE)
    lines = desc.split('\n')
    for j, line in enumerate(lines):
        draw.text((cx + 100, cy + 48 + j * 26), line, font=font_small, fill=TEXT_MUTED)

y += 2 * (tip_h + 16) + 40

# ===== FOOTER =====
draw.line((100, y, W - 100, y), fill=BORDER, width=1)
y += 30
text_center(draw, "국내 견과류 비교 인포그래픽 © 2025", y, font_small, TEXT_MUTED)
y += 30
text_center(draw, "식품의약품안전처, 농촌진흥청 식품성분표 참고", y, font_label, (100, 105, 120))

# ===== Save =====
# Crop to actual content
final_h = y + 60
img_cropped = img.crop((0, 0, W, min(final_h, H)))
img_cropped.save('/home/user/AI/korean_nuts_infographic.png', 'PNG', quality=95)
print(f"Saved: {W}x{min(final_h, H)} px")
