import urllib.request
import re

url = "https://www.instagram.com/p/DeGKvCkSqw8/embed/"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
try:
    with urllib.request.urlopen(req, timeout=5) as r:
        html = r.read().decode('utf-8', errors='ignore')
        handles = re.findall(r'instagram\.com/([a-zA-Z0-9_.-]+)', html)
        print("Handles mentioned in DeGKvCkSqw8:", set(handles))
        # check for jawara in text
        lines = [l.strip() for l in html.split('\n') if 'jawara' in l.lower()]
        print(f"Lines containing jawara: {len(lines)}")
        for l in lines[:5]:
            print(l[:200])
except Exception as e:
    print('err:', e)
