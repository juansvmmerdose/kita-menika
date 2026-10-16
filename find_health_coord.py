from PIL import Image

screen = Image.open(r'C:\Users\VANDI\.gemini\antigravity\scratch\kita-menikah\screen_crop.png')
# Health icon has a white background with a red heart.
# Let's find white pixels around x=60, y=550 to 650:
for y in range(560, 670, 5):
    p = screen.getpixel((60, y))
    p_label = screen.getpixel((60, y+10))
    print(f"y={y}: center={p}")
