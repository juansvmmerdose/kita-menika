with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
m = re.search(r'const\s+vendors\s*=\s*(\[.*?\]);', text, re.DOTALL)
if m:
    print('Found const vendors! Length of array text:', len(m.group(1)))
    # print first vendor object
    print(m.group(1)[:500])
else:
    print('No const vendors found, looking for vendors = ')
    m2 = re.search(r'vendors\s*=\s*(\[.*?\]);', text, re.DOTALL)
    if m2:
        print('Found vendors = ! Length:', len(m2.group(1)))
        print(m2.group(1)[:500])
    else:
        print('Searching for "category":')
        matches = [line.strip() for line in text.splitlines() if 'category' in line.lower()][:15]
        for line in matches:
            print(line)
