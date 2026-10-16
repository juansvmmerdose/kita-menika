import urllib.request
import re

codes = ['DMp2hgkxsto', 'DTILEXJkeLK', 'DZfMeWEGdnY', 'DMskguExr-y']

for c in codes:
    url = f"https://www.instagram.com/p/{c}/embed/captioned/"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
    with urllib.request.urlopen(req, timeout=5) as r:
        html = r.read().decode('utf-8', errors='ignore')
    
    # look for text in Caption block
    # In Instagram embed, captions often appear in <div class="Caption"> or <div class="CaptionComments">
    captions = re.findall(r'<div class="Caption"[^>]*>(.*?)</div>', html, re.DOTALL)
    if not captions:
        # look for any text between </a> and </div>
        captions = re.findall(r'class="CaptionText"[^>]*>(.*?)</div>', html, re.DOTALL)
    print(f"=== {c} ===")
    print("Found captions:", captions)
