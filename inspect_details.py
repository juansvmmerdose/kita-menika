from PIL import Image

im1 = Image.open(r'C:\Users\VANDI\.gemini\antigravity\brain\98605af6-0ebd-4ed8-a33b-bdbb36cb2699\.user_uploaded\media_1792118524573_31782ee0.jpg')
im2 = Image.open(r'C:\Users\VANDI\.gemini\antigravity\brain\98605af6-0ebd-4ed8-a33b-bdbb36cb2699\.user_uploaded\media_1792118531376_8b379333.png')

# Let's save crops or inspect what is inside both
# In im2, what does the screen show?
# Let's check the top notch / dynamic island in im2
# and let's check im1
print("im1 size:", im1.size)
print("im2 size:", im2.size)

# In im2, where does the inner screen start and end?
# Let's find the screen rectangle (where the wallpaper is)
# Between y=20 and y=1000, x=25 and x=485
# Let's find exact inner screen bounds
screen_top = 0
for y in range(20, 100):
    p = im2.getpixel((255, y))
    # Check if this is the dynamic island or wallpaper
    # Dynamic island is pure black (0,0,0) or near black
    pass

# Let's inspect the wallpaper colors and dynamic island
print("im2 at x=255, y=30:", im2.getpixel((255, 30)))
print("im2 at x=255, y=40:", im2.getpixel((255, 40)))
print("im2 at x=255, y=80:", im2.getpixel((255, 80)))
print("im2 at x=255, y=120:", im2.getpixel((255, 120)))
print("im2 at x=100, y=35:", im2.getpixel((100, 35))) # Time location
print("im2 at x=410, y=35:", im2.getpixel((410, 35))) # Battery location
