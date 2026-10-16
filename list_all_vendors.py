import json
import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

m = re.search(r'const\s+vendors\s*=\s*(\[\s*\{.*?\}\s*\]);', text, re.DOTALL)
if m:
    data = json.loads(m.group(1))
    print(f'Total vendors: {len(data)}')
    from collections import Counter
    cats = Counter([v['category'] for v in data])
    for c, n in cats.items():
        print(f'  {c}: {n}')
    print('\nVendors list:')
    for v in data:
        print(f"  [{v['category']}] {v['name']} ({v.get('igHandle', '-')})")
