with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re

m = re.search(r'listContainer\.innerHTML\s*=\s*filtered\.map\(v\s*=>\s*\{(.*?)\}\)\.join', text, re.DOTALL)
if m:
    content = m.group(1)
    print(content[2500:5500].encode('ascii', errors='replace').decode('ascii'))
