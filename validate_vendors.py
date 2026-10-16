import json
import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

m = re.search(r'const\s+vendors\s*=\s*(\[\s*\{.*?\}\s*\]);', text, re.DOTALL)
vendors = json.loads(m.group(1))

print(f"Total vendors successfully parsed: {len(vendors)}")
from collections import Counter
c = Counter(v['category'] for v in vendors)
for cat, cnt in c.items():
    print(f" - {cat}: {cnt} vendor(s)")
