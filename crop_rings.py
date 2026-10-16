from PIL import Image

img = Image.open('assets/app_logo.png')
w, h = img.size

# The rings are centered in the logo
# Let's crop the center area where the two rings and diamond are
# In a 1024x1024 image, the squircle is roughly from 200 to 824
# The rings are inside roughly from (280, 300, 744, 730)
box = (250, 280, 774, 740)
cropped = img.crop(box)

# Let's make black transparent in cropped if desired, or keep as is with black background
# Since splash screen background is pitch black (#000000), black background blends perfectly!
cropped.save('assets/rings_only.png')
print('Cropped rings saved: size', cropped.size)
