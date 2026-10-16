import urllib.request
import urllib.parse
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
}

queries = [
    "kitakancerita jogja instagram",
    "neiscala wedding jogja instagram",
    "lunanouva studio jogja instagram",
    "nijo wedding jogja instagram",
    "lux visual jogja instagram"
]

for q in queries:
    url = f"https://html.duckduckgo.com/html/?q={urllib.parse.quote(q)}"
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as resp:
            content = resp.read().decode('utf-8', errors='ignore')
            urls = re.findall(r'instagram\.com/([a-zA-Z0-9_.]+)', content)
            print(f"Query: {q}")
            print("IG profiles found:", list(dict.fromkeys([u for u in urls if u not in ['p', 'reel', 'explore', 'stories', 'about', 'legal']]))[:6])
    except Exception as e:
        print(f"Error {q}: {e}")
