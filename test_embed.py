import urllib.request
import re

shortcodes = {
    "jawara": "DBL9yFeTDlr",
    "sandi": "DdB34NMD5lr",
    "lux": "DZm2Kbgj4ZZ",
    "kitakancerita": "DV2iXGGCSz6",
    "nijo": "DaQBRhFGCvF",
    "neiscala": "DeB1C4kH5vS",
    "lunanouva": "DdRiiJqj3xs"
}

for name, code in shortcodes.items():
    url = f"https://www.instagram.com/p/{code}/embed/"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
    try:
        with urllib.request.urlopen(req, timeout=5) as r:
            html = r.read().decode('utf-8', errors='ignore')
            # Extract author, likes, and image if possible
            author = re.findall(r'"username":"([^"]+)"', html)
            imgs = re.findall(r'(https://[a-zA-Z0-9.-]+\.cdninstagram\.com/[^"\'\s<>]+)', html)
            fbcdn = re.findall(r'(https://scontent[a-zA-Z0-9.-]*\.cdninstagram\.com/[^"\'\s<>]+)', html)
            print(f"{name} ({code}) -> Status 200 OK | HTML len: {len(html)} | User: {author[:1]} | CDN imgs: {len(imgs) + len(fbcdn)}")
    except Exception as e:
        print(f"{name} err: {e}")
