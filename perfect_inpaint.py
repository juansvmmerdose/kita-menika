import numpy as np
from PIL import Image

screen = Image.open(r'C:\Users\VANDI\.gemini\antigravity\scratch\kita-menikah\screen_crop.png').convert('RGB')
arr = np.array(screen)

# In the AssistiveTouch area (y from 710 to 820, x from 360 to 458):
# The curve comes in from the left and continues to the bottom-right.
# Notice at y=710: arr[710, 360] is (244, 98, 126), arr[710, 458] is (245, 99, 125)
# In fact, let's look at the colors on the boundary around the circle:
center_x, center_y = 413, 765
radius = 45

# We can perform simple Poisson/harmonic inpainting or smooth Laplace interpolation inside the circle:
# For each pixel inside radius, solve Laplace equation (d2I/dx2 + d2I/dy2 = 0) with Dirichlet boundary conditions!
# That gives a mathematically PERFECT smooth gradient matching the boundaries seamlessly!

mask = np.zeros((screen.height, screen.width), dtype=bool)
for y in range(center_y - radius - 5, center_y + radius + 6):
    for x in range(center_x - radius - 5, center_x + radius + 6):
        if (x - center_x)**2 + (y - center_y)**2 <= radius**2:
            mask[y, x] = True

# Also for the top notch (y from 0 to 40, x from 90 to 370)
# But wait! For the top notch, in iPhone 16 Pro, the Dynamic Island will be placed right in the center (x: 180 to 280, y: 15 to 45)!
for y in range(0, 42):
    for x in range(95, 365):
        if arr[y, x, 0] < 80 and arr[y, x, 1] < 80 and arr[y, x, 2] < 80:
            mask[y, x] = True

# Solve Laplace equation on mask using Jacobi iterations (1000 iterations is instant)
res = arr.astype(float).copy()
for _ in range(1200):
    # compute 4-neighbor average
    up = np.roll(res, -1, axis=0)
    down = np.roll(res, 1, axis=0)
    left = np.roll(res, -1, axis=1)
    right = np.roll(res, 1, axis=1)
    avg = (up + down + left + right) / 4.0
    res[mask] = avg[mask]

inpainted = Image.fromarray(np.clip(res, 0, 255).astype(np.uint8))
inpainted.save(r'C:\Users\VANDI\.gemini\antigravity\scratch\kita-menikah\assets\ios_homescreen_perfect.png')
inpainted.save(r'C:\Users\VANDI\.gemini\antigravity\brain\98605af6-0ebd-4ed8-a33b-bdbb36cb2699\assets\ios_homescreen_perfect.png')
print("Laplace inpainting completed and saved to ios_homescreen_perfect.png!")
