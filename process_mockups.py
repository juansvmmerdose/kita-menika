import os
from PIL import Image

img1_path = r'C:\Users\VANDI\.gemini\antigravity\brain\98605af6-0ebd-4ed8-a33b-bdbb36cb2699\.user_uploaded\media_1792118524573_31782ee0.jpg'
img2_path = r'C:\Users\VANDI\.gemini\antigravity\brain\98605af6-0ebd-4ed8-a33b-bdbb36cb2699\.user_uploaded\media_1792118531376_8b379333.png'

im1 = Image.open(img1_path)
print("Image 1 size:", im1.size, im1.mode)

im2 = Image.open(img2_path)
print("Image 2 size:", im2.size, im2.mode)
