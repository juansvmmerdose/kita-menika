import urllib.request
import json

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
    url = f"https://api.instagram.com/oembed/?url=https://www.instagram.com/p/{code}/"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req, timeout=5) as r:
            data = json.loads(r.read().decode('utf-8'))
            print(f"=== {name} ===")
            print("Title:", data.get('title'))
            print("Author:", data.get('author_name'), f"(@{data.get('author_url')})")
            print("Thumbnail:", data.get('thumbnail_url'))
            print("HTML embed snippet len:", len(data.get('html', '')))
    except Exception as e:
        print(f"{name} err:", e)
