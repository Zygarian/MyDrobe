from PIL import Image, ImageDraw, ImageFont, ImageFilter
import math

def create_icon(size=512):
    # Create image with baby blue gradient background
    img = Image.new('RGB', (size, size), (135, 206, 235))
    draw = ImageDraw.Draw(img)
    
    # Draw circular badge
    cx, cy = size // 2, size // 2
    r = size * 0.9
    
    # Create circular clip mask
    mask = Image.new('L', (size, size), 0)
    mask_draw = ImageDraw.Draw(mask)
    mask_draw.ellipse([size // 2 - r, size // 2 - r, size // 2 + r, size // 2 + r], fill=255)
    
    # Baby blue gradient
    for y in range(size):
        ratio = y / size
        r_val = int(135 + ratio * 20)
        g_val = int(206 + ratio * 30)
        b_val = int(235 - ratio * 15)
        draw.line([(0, y), (size, y)], fill=(r_val, g_val, b_val))
    
    # Apply circular clip
    img = img.crop([0, 0, size, size])
    img = Image.fromarray(img) if hasattr(img, '__array_interface__') else img
    
    # Draw coat hanger silhouette (subtle white in background)
    draw.ellipse([cx - 40, 80, cx + 40, 100], fill=(255, 255, 255, 100))  # Hook
    draw.line([(cx - 150, 150), (cx + 150, 150)], fill=(255, 255, 255, 100), width=10)  # Bar
    draw.arc([cx - 150, 150, cx - 100, 250], 0, 360, fill=(255, 255, 255, 100), width=10)  # Left curve
    draw.arc([cx + 100, 150, cx + 150, 250], 0, 360, fill=(255, 255, 255, 100), width=10)  # Right curve
    
    # "M" and "D" initials - white with baby blue outline
    font_size = size * 0.3
    try:
        font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", font_size)
    except:
        font = ImageFont.load_default(size=font_size)
    
    text = "MD"
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    text_x = cx - text_width // 2
    text_y = size * 0.65
    
    # Baby blue outline (4 corners)
    offset = 3
    for dx in [-offset, 0, offset]:
        for dy in [-offset, 0, offset]:
            draw.text((text_x + dx, text_y + dy), text, fill=(93, 173, 226, 200), font=font)
    
    # White fill
    draw.text((text_x, text_y), text, fill=(255, 255, 255, 255), font=font)
    
    # Apply circular mask
    img = img.convert("RGBA")
    img.putalpha(mask)
    
    return img

# Generate icons
try:
    img_192 = create_icon(192)
    img_192.save("/tmp/mydrobe/icon-192.png")
    print("192x192 icon created!")
except Exception as e:
    print(f"Error: {e}")

try:
    img_512 = create_icon(512)
    img_512.save("/tmp/mydrobe/icon-512.png")
    print("512x512 icon created!")
except Exception as e:
    print(f"Error: {e}")