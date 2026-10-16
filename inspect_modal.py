with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re

# Find modal rendering
m = re.search(r'function openVendorModal\(.*?\n\s*function', text, re.DOTALL)
if m:
    content = m.group(0)
    print(content[:2500].encode('ascii', errors='replace').decode('ascii'))
