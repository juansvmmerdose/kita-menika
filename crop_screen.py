from PIL import Image

im2 = Image.open(r'C:\Users\VANDI\.gemini\antigravity\brain\98605af6-0ebd-4ed8-a33b-bdbb36cb2699\.user_uploaded\media_1792118531376_8b379333.png')

# In im2, let's inspect the exact inner screen image (without the frame).
# Frame borders:
# x: from 25 to 485 (width = 460)
# y: from 22 to 1002 (height = 980)
screen = im2.crop((25, 22, 485, 1002))
screen.save(r'C:\Users\VANDI\.gemini\antigravity\scratch\kita-menikah\screen_crop.png')
print("Screen crop saved with size:", screen.size)

# Also let's inspect the titanium frame of im1.
# In im1, front phone is at (250, 16, 527, 582).
im1 = Image.open(r'C:\Users\VANDI\.gemini\antigravity\brain\98605af6-0ebd-4ed8-a33b-bdbb36cb2699\.user_uploaded\media_1792118524573_31782ee0.jpg')
phone1 = im1.crop((250, 16, 527, 582))
phone1.save(r'C:\Users\VANDI\.gemini\antigravity\scratch\kita-menikah\phone1_crop.png')
print("Phone 1 crop saved with size:", phone1.size)
