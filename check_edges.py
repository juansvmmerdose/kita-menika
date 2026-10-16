from PIL import Image

im1 = Image.open(r'C:\Users\VANDI\.gemini\antigravity\brain\98605af6-0ebd-4ed8-a33b-bdbb36cb2699\.user_uploaded\media_1792118524573_31782ee0.jpg')

# At y=300 (middle of the phones), check x from 245 to 275
for x in range(245, 275):
    print(f"x={x}: {im1.getpixel((x, 300))}")

# And let's check top y around x=390 (center of front phone)
for y in range(10, 30):
    print(f"y={y}: {im1.getpixel((390, y))}")

# And bottom y around x=390
for y in range(570, 590):
    print(f"y={y}: {im1.getpixel((390, y))}")
