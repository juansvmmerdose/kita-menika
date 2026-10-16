with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
cats = set(re.findall(r'category:\s*["\']([^"\']+)["\']', text))
print('Existing vendor categories in data:', sorted(list(cats)))

# Let's count how many vendors per category
from collections import Counter
counts = Counter(re.findall(r'category:\s*["\']([^"\']+)["\']', text))
for cat, cnt in counts.items():
    print(f'  {cat}: {cnt} vendors')
