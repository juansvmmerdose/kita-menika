import urllib.request
import re
import html
import time

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
    'Sec-Fetch-Dest': 'iframe',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'cross-site'
}

codes = [
    ("jawara", "DZfMeWEGdnY"),
    ("sandi", "DdB34NMD5lr"),
    ("kitakancerita", "DV2iXGGCSz6"),
    ("nijo", "DaQBRhFGCvF"),
    ("neiscala", "DeB1C4kH5vS"),
    ("lunanouva", "DdRiiJqj3xs")
]

for name, code in codes:
    url = f"https://www.instagram.com/p/{code}/embed/captioned/"
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=8) as r:
            content = r.read().decode('utf-8', errors='ignore')
        
        # Look for EmbeddedMediaImage or any cdn image
        imgs = re.findall(r'<img[^>]+src="([^">]+)"', content)
        clean_imgs = [html.unescape(i) for i in imgs if not i.startswith('data:')]
        print(f"=== {name} ({code}) ===")
        print(f"Found {len(clean_imgs)} real img URLs")
        for u in clean_imgs[:3]:
            print("  IMG:", u[:100])
        time.sleep(2)
    except Exception as e:
        print(f"Err {name}: {e}")
