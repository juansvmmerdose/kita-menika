import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Let's inspect if any broken image path or missing file exists
images_in_html = re.findall(r"['\"](assets/vendors/[^'\"]+)['\"]", html)
print(f"Total assets referenced in index.html: {len(images_in_html)}")
import os
for img in set(images_in_html):
    exists = os.path.exists(img)
    print(f"  {img}: {'EXISTS' if exists else 'MISSING'}")
