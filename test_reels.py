import urllib.request
import re

codes = ['C3prud6Rkng', 'DeIc4RTTSWd']
for c in codes:
    url = f"https://www.instagram.com/reel/{c}/embed/"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
    try:
        with urllib.request.urlopen(req, timeout=5) as r:
            html = r.read().decode('utf-8', errors='ignore')
            handles = re.findall(r'instagram\.com/([a-zA-Z0-9_.-]+)', html)
            print(f"Code {c} handles:", set(handles))
    except Exception as e:
        print(f"Code {c} err: {e}")
