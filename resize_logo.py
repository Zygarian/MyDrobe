from PIL import Image

img = Image.open('/tmp/mydrobe/logo.jpg').convert('RGBA')

for size in [192, 256, 512]:
    resized = img.resize((size, size))
    resized.save(f'/tmp/mydrobe/icon-{size}.png')
    print(f"Saved icon-{size}.png")