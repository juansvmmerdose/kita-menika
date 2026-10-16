from PIL import Image

im2 = Image.open(r'C:\Users\VANDI\.gemini\antigravity\brain\98605af6-0ebd-4ed8-a33b-bdbb36cb2699\.user_uploaded\media_1792118531376_8b379333.png')

# Let's crop the top left corner, side border, top dynamic island of im2
# and inspect its appearance
im2.crop((0, 0, 100, 100)).save(r'C:\Users\VANDI\.gemini\antigravity\scratch\kita-menikah\corner_crop.png')
im2.crop((180, 0, 330, 80)).save(r'C:\Users\VANDI\.gemini\antigravity\scratch\kita-menikah\notch_crop.png')
print("Crops saved.")
