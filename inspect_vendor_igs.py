import json
import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

m = re.search(r'const\s+vendors\s*=\s*(\[\s*\{.*?\}\s*\]);', text, re.DOTALL)
vendors = json.loads(m.group(1))

print(f"Total vendors: {len(vendors)}")
for i, v in enumerate(vendors):
    has_ig = bool(v.get('igUrl') and v.get('igHandle'))
    avatar = v.get('avatar', '')
    print(f"{i+1:2d}. [{v['category']:11s}] {v['name'][:30]:30s} | {v.get('igHandle', 'NO_HANDLE'):25s} | IG_URL: {v.get('igUrl', 'NO_URL'):40s} | Avatar: {avatar}")
