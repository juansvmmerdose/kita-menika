from PIL import Image

im2 = Image.open(r'C:\Users\VANDI\.gemini\antigravity\brain\98605af6-0ebd-4ed8-a33b-bdbb36cb2699\.user_uploaded\media_1792118531376_8b379333.png')

# In iOS, icons are arranged in 4 columns:
# x centers are approximately:
# width is 460 (screen from 25 to 485)
# margin left ~ 25 + 25 = 50
# col 0: ~ 78
# col 1: ~ 180
# col 2: ~ 282
# col 3: ~ 384
#
# Let's inspect rows:
# y for row 1: ~ 130
# row 2: ~ 240
# row 3: ~ 350
# row 4: ~ 460
# row 5: ~ 570
# row 6: ~ 680
# dock: ~ 910
#
# Let's check pixel colors around these locations:
for r, y in enumerate([140, 250, 360, 470, 580, 690, 920]):
    cols = [im2.getpixel((x, y))[:3] for x in [80, 180, 280, 380]]
    print(f"Row {r} (y={y}): {cols}")
