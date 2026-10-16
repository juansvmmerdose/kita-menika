from PIL import Image

im1 = Image.open(r'C:\Users\VANDI\.gemini\antigravity\brain\98605af6-0ebd-4ed8-a33b-bdbb36cb2699\.user_uploaded\media_1792118524573_31782ee0.jpg')
# Crop right half where front of iPhone is
front_crop = im1.crop((245, 10, 535, 590))
front_crop.save(r'C:\Users\VANDI\.gemini\antigravity\scratch\kita-menikah\front_crop.png')
print("Saved front_crop.png, size:", front_crop.size)

# Let's inspect what is on the screen of im1
# Is it the iPhone 16 Pro wallpaper with the gold/titanium rings?
print("front_crop center:", front_crop.getpixel((front_crop.width//2, front_crop.height//2)))
print("front_crop top-center (dynamic island):", front_crop.getpixel((front_crop.width//2, 30)))
