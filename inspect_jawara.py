import urllib.request
import re

codes = ['DBL9yFeTDlr', 'DMp2hgkxsto', 'DTILEXJkeLK', 'DKTt3oDxspc', 'DZfMeWEGdnY', 'DMskguExr-y', 'DeIc4RTTSWd']

for c in codes:
    url = f"https://www.instagram.com/p/{c}/embed/"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req, timeout=5) as r:
            html = r.read().decode('utf-8', errors='ignore')
            title = re.findall(r'<title>(.*?)</title>', html)
            # find any mentions of username or caption
            user = re.findall(r'"username":"([^"]+)"', html)
            print(f"Code {c}: Title={title} | User={user}")
    except Exception as e:
        print(f"Code {c} err: {e}")
