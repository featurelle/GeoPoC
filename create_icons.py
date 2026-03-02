from PIL import Image, ImageDraw, ImageFont

# Create 192x192 icon
img192 = Image.new('RGB', (192, 192), color='black')
draw192 = ImageDraw.Draw(img192)
try:
    font192 = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 80)
except:
    font192 = ImageFont.load_default()
draw192.text((96, 96), "G", fill="white", font=font192, anchor="mm")
img192.save("icon-192.png", "PNG")

# Create 512x512 icon
img512 = Image.new('RGB', (512, 512), color='black')
draw512 = ImageDraw.Draw(img512)
try:
    font512 = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 200)
except:
    font512 = ImageFont.load_default()
draw512.text((256, 256), "G", fill="white", font=font512, anchor="mm")
img512.save("icon-512.png", "PNG")

print("Icons created: icon-192.png, icon-512.png")
