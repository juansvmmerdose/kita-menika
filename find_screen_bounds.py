from PIL import Image

im2 = Image.open(r'C:\Users\VANDI\.gemini\antigravity\brain\98605af6-0ebd-4ed8-a33b-bdbb36cb2699\.user_uploaded\media_1792118531376_8b379333.png')

# Find the outer bounding box where alpha > 0
# And find the inner screen boundary
# Let's check horizontal slice at y=500
row500 = [im2.getpixel((x, 500)) for x in range(im2.width)]
first_solid = None
last_solid = None
for x in range(im2.width):
    if row500[x][3] > 10:
        if first_solid is None: first_solid = x
        last_solid = x

print(f"y=500: solid starts at x={first_solid}, ends at x={last_solid}")
print("Colors across y=500 at x from first_solid to first_solid+30:")
for x in range(first_solid, first_solid+25):
    print(f"x={x}: {row500[x]}")

# Let's also check vertical slice at x=255
col255 = [im2.getpixel((255, y)) for y in range(im2.height)]
first_y = None
last_y = None
for y in range(im2.height):
    if col255[y][3] > 10:
        if first_y is None: first_y = y
        last_y = y
print(f"x=255: solid starts at y={first_y}, ends at y={last_y}")
for y in range(first_y, first_y+25):
    print(f"y={y}: {col255[y]}")

# Let's also check what im1 is vs im2
# User prompt: "oke nice, sekarang kita ubah iphone nya mengunakan ini ya, dan view home screennya pakai yang ini, toong satukan dengan rapih dan perfect"
# "menggunakan ini ya" -> uploaded media 1 (the iPhone 16 Pro titanium photo from Apple)
# "dan view home screennya pakai yang ini" -> uploaded media 2 (the iOS homescreen)
# "tolong satukan dengan rapih dan perfect"
