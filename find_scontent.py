import urllib.request
import re
import html

url = "https://www.instagram.com/p/DBL9yFeTDlr/embed/"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'})
with urllib.request.urlopen(req, timeout=5) as r:
    page = r.read().decode('utf-8', errors='ignore')

# Look for scontent or cdninstagram image patterns
# Instagram images typically have scontent-*.cdninstagram.com/v/...
images = re.findall(r'(https?:\\?/\\?/[^"\'\s<>\\]*scontent[^"\'\s<>\\]*)', page)
print(f"scontent matches: {len(images)}")
clean_images = list(dict.fromkeys([html.unescape(img.replace('\\/', '/')) for img in images]))
print(f"Unique scontent: {len(clean_images)}")
for i, img in enumerate(clean_images[:5]):
    print(f"Image {i}: {img[:160]}")
