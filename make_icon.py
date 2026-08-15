#!/usr/bin/env python3
from PIL import Image, ImageDraw, ImageFont
import math

def create_logo(size):
    # Create circular badge with baby blue gradient
    img = Image.new('RGB', (size, size), (0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    cx, cy = size // 2, size // 2
    r = size // 2
    
    # Draw solid baby blue circle
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(168, 216, 255))
    
    # "MD" text
    font_size = size // 3
    try:
        font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", font_size)
    except:
        font = ImageFont.load_default(size=font_size)
    
    text = "MD"
    dummy = Image.new('RGB', (size, size))
    dd = ImageDraw.Draw(dummy)
    bbox = dd.textbbox((0, 0), text, font=font)
    tw = bbox[2] - bbox[0]
    th = bbox[3] - bbox[1]
    tx = cx - tw // 2
    ty = cy - th // 2
    
    # Blue outline
    for dx in [-2, 0, 2]:
        for dy in [-2, 0, 2]:
            draw.text((tx + dx, ty + dy), text, fill=(93, 173, 226), font=font)
    
    # White fill
    draw.text((tx, ty), text, fill=(255, 255, 255), font=font)
    
    return img

img = create_logo(512)
img.save('/tmp/mydrobe/icon-512.png')
print("Done")