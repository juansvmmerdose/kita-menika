import urllib.request
import re

codes = ['DMp2hgkxsto', 'DTILEXJkeLK', 'DZfMeWEGdnY', 'DMskguExr-y']

for c in codes:
    url = f"https://www.instagram.com/p/{c}/embed/captioned/"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
    try:
        with urllib.request.urlopen(req, timeout=5) as r:
            html = r.read().decode('utf-8', errors='ignore')
            # Extract caption or text snippets
            print(f"=== POST {c} ===")
            print(f"URL: https://www.instagram.com/p/{c}/")
            # find all text in embed
            clean_text = re.sub(r'<[^>]+>', ' ', html)
            clean_text = ' '.join(clean_text.split())
            print("Text sample:", clean_text[:400])
    except Exception as e:
        print(f"Error {c}: {e}")
