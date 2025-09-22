from PIL import Image, ImageDraw

# Create a blank image (width x height)
img = Image.new("RGB", (48, 40), color=(120, 120, 120))
draw = ImageDraw.Draw(img)

# ================= Reference =================
# Battery icon
# draw.rectangle([135,15,145,25],fill="black")
# draw.rectangle([140, 10, 180, 30], outline="black", fill=(255, 255, 200),width=3)
# draw.rectangle([162, 15, 167, 25], fill="black")
# draw.rectangle([170, 15, 175, 25], fill="black")

# Battery icon
draw.rectangle([2,15,10,25],fill="black")
draw.rectangle([5, 10, 45, 30], outline="black", fill=(255, 255, 200),width=3)
draw.rectangle([27, 15, 32, 25], fill="black")
draw.rectangle([35, 15, 40, 25], fill="black")
img.save("./asset/prototype_battery.jpg")
img.show()
