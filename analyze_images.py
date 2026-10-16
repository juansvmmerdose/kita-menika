import os
from PIL import Image

im1 = Image.open(r'C:\Users\VANDI\.gemini\antigravity\brain\98605af6-0ebd-4ed8-a33b-bdbb36cb2699\.user_uploaded\media_1792118524573_31782ee0.jpg')
im2 = Image.open(r'C:\Users\VANDI\.gemini\antigravity\brain\98605af6-0ebd-4ed8-a33b-bdbb36cb2699\.user_uploaded\media_1792118531376_8b379333.png')

# In im1, it's 600x600. Left side has back of iPhone, right side has front of iPhone.
# Let's crop the front of the iPhone (right side) to see its bounding box
# Let's check non-white/non-black background in im1
print("im1 corner pixel:", im1.getpixel((0,0)), im1.getpixel((599,0)))

# Let's check im2
print("im2 corner pixel:", im2.getpixel((0,0)), im2.getpixel((509,0)))
