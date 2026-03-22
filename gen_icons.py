from PIL import Image, ImageDraw, ImageFont
import os

def make_icon(size, path):
    img = Image.new('RGB', (size, size), '#0a0a0a')
    draw = ImageDraw.Draw(img)
    # Border
    draw.rectangle([4, 4, size-5, size-5], outline='#00ff88', width=3)
    # T letter
    cx, cy = size//2, size//2
    s = size // 3
    draw.rectangle([cx - s//2, cy - s//2, cx + s//2, cy - s//2 + s//5], fill='#00ff88')
    draw.rectangle([cx - s//10, cy - s//2, cx + s//10, cy + s//2], fill='#00ff88')
    img.save(path)

make_icon(192, '/home/claude/taskapp/icon-192.png')
make_icon(512, '/home/claude/taskapp/icon-512.png')
print("icons OK")
