from PIL import Image

im2 = Image.open(r'C:\Users\VANDI\.gemini\antigravity\brain\98605af6-0ebd-4ed8-a33b-bdbb36cb2699\.user_uploaded\media_1792118531376_8b379333.png')

# Let's save a crop of row 3, 4, 5 to see what icons are there
# row 3: y ~ 410 to 520
# row 4: y ~ 520 to 630
# row 5: y ~ 630 to 740
# row 6: y ~ 740 to 850 (dots / search bar)
# dock: y ~ 850 to 980

im2.crop((30, 400, 480, 850)).save(r'C:\Users\VANDI\.gemini\antigravity\scratch\kita-menikah\lower_half.png')
print("Lower half saved, inspecting...")

# Let's check the dots / search bar area:
# In iOS 16/17/18, there is a "Search" pill or dots above the dock at y ~ 780-840
print("Pixel at x=255, y=810:", im2.getpixel((255, 810)))
