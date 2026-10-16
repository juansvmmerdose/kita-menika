import os
from PIL import Image

slides = [f for f in os.listdir("assets/vendors/slides") if f.endswith(".jpg")]
print(f"Total slides: {len(slides)}")

# Let's check size, ratio, and sample pixels
for s in sorted(slides):
    path = os.path.join("assets/vendors/slides", s)
    im = Image.open(path)
    print(f"{s:30s} {im.size} {im.mode}")
