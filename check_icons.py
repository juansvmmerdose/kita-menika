from PIL import Image

screen = Image.open(r'C:\Users\VANDI\.gemini\antigravity\scratch\kita-menikah\screen_crop.png')

# Let's save a summary of what's on row 3, 4, 5
# Icon center coordinates on screen_crop (460x980):
# xs: [60, 165, 270, 375] (approx, with icon size ~ 60x60)
# ys: [115, 225, 335, 445, 555, 665]
# Let's check average color & variance around each slot:
for r, y in enumerate([115, 225, 335, 445, 555, 665]):
    for c, x in enumerate([60, 165, 270, 375]):
        p = screen.getpixel((x, y))
        print(f"R{r}C{c} (x={x},y={y}): {p}")
