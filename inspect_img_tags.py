import re
import html
from PIL import Image
import urllib.request

with open('embed_dump.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's search for profile picture or any img tags
img_tags = re.findall(r'<img[^>]+>', text)
print("Total img tags in embed_dump:", len(img_tags))
for tag in img_tags:
    print("TAG:", tag)
