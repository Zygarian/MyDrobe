from PIL import Image, ImageDraw, ImageFont
import math

def create_icon(size=192):
    img = Image.new('RGBA', (size, size), (173, 216, 255, 255)) # Baby blue background
    draw = ImageDraw.Draw(img)
    
    cx, cy = size // 2, size // 2
    
    # Draw coat hanger silhouette (white)
    # Top hook
    hook_y = size * 0.15
    hook_width = size * 0.12
    draw.ellipse([cx - hook_width/2, hook_y, cx + hook_width/2, hook_y + hook_width], fill=(255, 255, 255))
    
    # Hanger bar
    bar_y = size * 0.25
    bar_width = size * 0.7
    bar_height = size * 0.06
    draw.rounded_rect([cx - bar_width/2, bar_y, cx + bar_width/2, bar_y + bar_height], radius=bar_height/2, fill=(255, 255, 255))
    
    # Hanger curves
    left_start = cx - bar_width/2
    right_start = cx + bar_width/2
    curve_down = size * 0.2
    left_end = left_start + size * 0.05
    right_end = right_start - size * 0.05
    bottom_width = size * 0.15
    
    # Left curve
    points_left = [(left_start, bar_y), (left_start, bar_y + curve_down/2), (cx - bottom_width/2, bar_y + curve_down)]
    draw.pieslice([left_start - size*0.02, bar_y, left_start + size*0.02, bar_y + curve_down], 0, 360, fill=(255, 255, 255))
    
    # Right curve
    draw.pieslice([right_start - size*0.02, bar_y, right_start + size*0.02, bar_y + curve_down], 0, 360, fill=(255, 255, 255))
    
    # Bottom bar
    bottom_y = bar_y + curve_down
    bottom_bar_width = bottom_width
    draw.rounded_rect([cx - bottom_bar_width/2, bottom_y, cx + bottom_bar_width/2, bottom_y + bar_height], radius=bar_height/2, fill=(255, 255, 255))
    
    # "M" and "D" initials
    # Create text image
    text_size = size * 0.35
    try:
        font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", text_size)
    except:
        font = ImageFont.load_default(size=text_size)
    
    text = "MD"
    text_img = Image.new('RGBA', (size, size), (232, 244, 253, 0))
    text_draw = ImageDraw.Draw(text_img)
    
    bbox = text_draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    text_x = cx - text_width // 2
    text_y = size * 0.65
    
    # Draw baby blue outline
    offset = size * 0.01
    for dx in [-offset, 0, offset]:
        for dy in [-offset, 0, offset]:
            text_draw.text((text_x + dx, text_y + dy), text, fill=(74, 144, 226, 255), font=font)
    
    # Draw white text on top
    text_draw.text((text_x, text_y), text, fill=(255, 255, 255, 255), font=font)
    
    # Composite
    img = Image.alpha_composite(img, text_img)
    
    return img

# Generate icons
try:
    img_192 = create_icon(192)
    img_192.save("/tmp/mydrobe/icon-192.png")
    print("Icon 192x192 created successfully!")
except Exception as e:
    print(f"Error creating 192 icon: {e}")

try:
    img_512 = create_icon(512)
    img_512.save("/tmp/mydrobe/icon-512.png")
    print("Icon 512x512 created successfully!")
except Exception as e:
    print(f"Error creating 512 icon: {e}")