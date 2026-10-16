import json
import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

m = re.search(r'const\s+vendors\s*=\s*(\[\s*\{.*?\}\s*\]);', text, re.DOTALL)
data = json.loads(m.group(1))
print(json.dumps(data[0], indent=2))
