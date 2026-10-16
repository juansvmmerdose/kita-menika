import urllib.request
import re

friends = [
    ("sandi.liem", "DdB34NMD5lr"),
    ("luxvisual.id", "DZm2Kbgj4ZZ"),
    ("kitakancerita", "DV2iXGGCSz6"),
    ("thenijophotograph", "DaQBRhFGCvF"),
    ("neiscala", "DeB1C4kH5vS"),
    ("lunanouovastudio__", "DdRiiJqj3xs")
]

for name, code in friends:
    url = f"https://www.instagram.com/p/{code}/embed/captioned/"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
    try:
        with urllib.request.urlopen(req, timeout=5) as r:
            page = r.read().decode('utf-8', errors='ignore')
        
        handles = [h for h in re.findall(r'instagram\.com/([a-zA-Z0-9_.-]+)', page) if h not in ['rsrc.php', 'explore', 'v', 'p', 'stories', 'reel']]
        print(f"Vendor: {name} (code: {code}) -> Handles: {set(handles)}")
    except Exception as e:
        print(f"Error {name}: {e}")
