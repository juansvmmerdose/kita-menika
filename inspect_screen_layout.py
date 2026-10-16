from PIL import Image

screen = Image.open(r'C:\Users\VANDI\.gemini\antigravity\scratch\kita-menikah\screen_crop.png')
print("Screen size:", screen.size)

# Let's check:
# Row 0: y=110..180
# Row 1: y=220..290
# Row 2: y=330..400
# Row 3: y=440..510
# Row 4: y=550..620
# Row 5: y=660..730
# Dock: y=860..940
#
# Let's inspect each row in screen_crop:
# We have 4 columns:
# x0: ~55, x1: ~160, x2: ~265, x3: ~370 (icon size is ~60x60 to 65x65)
