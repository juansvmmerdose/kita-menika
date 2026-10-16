with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re

# Check for unclosed scripts or syntax errors
scripts = re.findall(r'<script>(.*?)</script>', text, re.DOTALL)
print(f"Total inline scripts: {len(scripts)}")
for idx, s in enumerate(scripts):
    print(f"Script {idx+1} length: {len(s)} chars")

# Check all buttons in quick menu
buttons = re.findall(r'id="(qnav-btn-[^"]+)"', text)
print("Quick nav buttons found:", buttons)

boxes = re.findall(r'id="(qnav-box-[^"]+)"', text)
print("Quick nav boxes found:", boxes)
