from PIL import Image, ImageDraw, ImageFont

# Create a blank image (width x height)
img = Image.new("RGB", (300, 40), color=(120, 120, 120))
draw = ImageDraw.Draw(img)

# Load pixel font (or use default)
try:
    font = ImageFont.truetype("PixelOperator.ttf", 16)  # install a pixel font
except:
    font = ImageFont.load_default()

# Draw "879" box
draw.rectangle([10, 10, 30, 20], fill=(0, 0, 0))
draw.text((12, 10), "879", font=font, fill=(255, 255, 255))

# Envelope icon
draw.rectangle([60, 5, 90, 30], outline="black", fill=(255, 255, 200),width=2)
draw.line([60, 5, 75, 20, 90, 5], fill="black", width=2)
# draw.line([60, 35, 75, 20, 90, 35], fill="black")

# Speaker icon
# draw.polygon([(110, 10), (115, 10), (125, 15), (125, 25), (115, 30), (110, 30)], fill=(255, 255, 0), outline="black")

# Speaker base (rectangle part)
draw.rectangle([105, 15, 110, 25], fill=(255, 255, 0), outline="black")

# Speaker cone (triangle part)
# draw.polygon([(110, 15), (125, 20), (110, 25)], fill=(255, 255, 0), outline="black")

# Battery icon
draw.rectangle([135,15,145,25],fill="black")
draw.rectangle([140, 10, 180, 30], outline="black", fill=(255, 255, 200),width=3)
draw.rectangle([162, 15, 167, 25], fill="black")
draw.rectangle([170, 15, 175, 25], fill="black")

# T9a text
draw.text((200, 10), "T9a", font=font, fill=(255, 255, 200))

# Save image
img.save("topbar_pixel.png")
img.show()
