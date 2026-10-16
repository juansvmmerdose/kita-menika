import urllib.request
import urllib.parse
import re

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

searches = [
    'site:instagram.com/p/ "luxvisual.id"',
    'site:instagram.com/p/ "luxvisual"',
    'site:instagram.com/reel/ "luxvisual.id"'
]

found_codes = set()
for q in searches:
    url = f"https://html.duckduckgo.com/html/?q={urllib.parse.quote(q)}"
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=8) as r:
            html = r.read().decode('utf-8', errors='ignore')
            codes = re.findall(r'instagram\.com/(?:p|reel)/([a-zA-Z0-9_-]{9,15})', html)
            for c in codes:
                found_codes.add(c)
    except Exception as e:
        pass

print("Candidate lux codes:", found_codes)

for c in list(found_codes)[:8]:
    url = f"https://www.instagram.com/p/{c}/embed/captioned/"
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=5) as r:
            page = r.read().decode('utf-8', errors='ignore')
            handles = [h for h in re.findall(r'instagram\.com/([a-zA-Z0-9_.-]+)', page) if h not in ['rsrc.php', 'explore', 'v', 'p', 'stories', 'reel']]
            print(f"Code {c} -> Handles: {set(handles)}")
    except Exception as e:
        pass
