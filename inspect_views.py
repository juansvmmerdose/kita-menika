with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
bottom_nav = re.search(r'(<nav.*?</nav>)', text, re.DOTALL)
if bottom_nav:
    print('BOTTOM NAV:')
    print(bottom_nav.group(1).encode('ascii', errors='replace').decode('ascii'))

views = re.findall(r'id=["\'](view[A-Za-z0-9]+)["\']', text)
print('Views found:', views)

funcs = re.findall(r'function\s+([A-Za-z0-9_]+)\s*\(', text)
print('Key functions:', [fn for fn in funcs if 'Tab' in fn or 'View' in fn or 'switch' in fn or 'Category' in fn or 'Mode' in fn])
