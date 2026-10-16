import json
import re
import os

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

m = re.search(r'const\s+vendors\s*=\s*(\[\s*\{.*?\}\s*\]);', text, re.DOTALL)
vendors = json.loads(m.group(1))

print("Checking avatars & slides for all vendors:")
for v in vendors:
    av = v.get('avatar')
    slides = [s.get('image') for s in v.get('slides', [])]
    print(f"[{v['category']}] {v['name']} ({v['igHandle']})")
    print(f"  Avatar: {av} (exists: {os.path.exists(av)})")
    print(f"  Slides: {slides}")
