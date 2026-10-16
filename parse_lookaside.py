import re
import html

with open('test_lookaside.jpg', 'r', encoding='utf-8', errors='ignore') as f:
    t = f.read()

og = re.findall(r'<meta[^>]+property="og:image"[^>]+content="([^"]+)"', t)
print('og:image:', [html.unescape(x)[:120] for x in og])

sc = re.findall(r'https://[^\s"\'<>\\]*scontent[^\s"\'<>\\]*', t)
print('scontent:', len(sc))
for s in list(set(sc))[:5]:
    print('  ', s[:120])
