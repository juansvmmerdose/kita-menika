from PIL import Image

im2 = Image.open(r'C:\Users\VANDI\.gemini\antigravity\brain\98605af6-0ebd-4ed8-a33b-bdbb36cb2699\.user_uploaded\media_1792118531376_8b379333.png')

# Let's inspect:
# 1. Outer bounds of im2:
# 2. What color is the metal bezel of im2?
# In find_screen_bounds earlier:
# x=3 to 9: highlights, silver/titanium luster
# x=10 to 24: dark brushed titanium bezel
# x=25: screen border starts
print("Outer frame color at x=6, y=500:", im2.getpixel((6, 500)))
print("Inner bezel color at x=20, y=500:", im2.getpixel((20, 500)))
print("Screen pixel at x=26, y=500:", im2.getpixel((26, 500)))

# Let's check im1:
im1 = Image.open(r'C:\Users\VANDI\.gemini\antigravity\brain\98605af6-0ebd-4ed8-a33b-bdbb36cb2699\.user_uploaded\media_1792118524573_31782ee0.jpg')
# im1 is the official Black Titanium iPhone 16 Pro from Apple.
# What does im2 have?
# im2 is an iPhone mock with the exact wallpaper and apps!
