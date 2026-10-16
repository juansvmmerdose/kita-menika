from PIL import Image

im2 = Image.open(r'C:\Users\VANDI\.gemini\antigravity\brain\98605af6-0ebd-4ed8-a33b-bdbb36cb2699\.user_uploaded\media_1792118531376_8b379333.png')
print("im2 size:", im2.size)
# Sample pixels along edges and middle
print("Top-left:", im2.getpixel((10, 10)))
print("Top-center:", im2.getpixel((255, 10)))
print("Top-center (y=40):", im2.getpixel((255, 40)))
print("Center:", im2.getpixel((255, 512)))
print("Bottom-center:", im2.getpixel((255, 1010)))

# Let's save a few thumbnail or inspect layout
# Let's check row transparency
transparent_rows = []
for y in range(0, im2.height, 50):
    row_alphas = [im2.getpixel((x, y))[3] for x in range(0, im2.width, 20)]
    print(f"y={y}: min_alpha={min(row_alphas)}, max_alpha={max(row_alphas)}")
