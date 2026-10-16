import numpy as np
from PIL import Image, ImageFilter

screen = Image.open(r'C:\Users\VANDI\.gemini\antigravity\scratch\kita-menikah\assets\ios_homescreen_complete.png').convert('RGB')
arr = np.array(screen).astype(float)

# In the region x: 370..455, y: 720..840
# The gradient should simply be a smooth vertical transition from magenta (y=720) down to purple/violet (y=840)
# Let's inspect the vertical gradient at x=340 (left of Spotify):
# At x=340, we have the true undisturbed iOS wallpaper colors!
for y in range(710, 850):
    true_color = arr[y, 220] # around x=220 or between icons where the purple wave is pure!
    # Let's check color at x=220
    # Actually, between col 2 and 3, at x=310 (space between Instagram and Spotify):
    # arr[y, 310] is the clean wallpaper!
    clean_wave_color = arr[y, 310]
    for x in range(375, screen.width):
        arr[y, x] = clean_wave_color

smooth_img = Image.fromarray(np.clip(arr, 0, 255).astype(np.uint8))
# Apply a smooth horizontal blur across x: 360..455, y: 710..850
smooth_img.save(r'C:\Users\VANDI\.gemini\antigravity\scratch\kita-menikah\assets\ios_homescreen_complete.png')
screen.save(r'C:\Users\VANDI\.gemini\antigravity\brain\98605af6-0ebd-4ed8-a33b-bdbb36cb2699\assets\ios_homescreen_complete.png')
print("Smooth wave fix applied!")
