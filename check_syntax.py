import re

with open(r"C:\Users\VANDI\.gemini\antigravity\scratch\kita-menikah\index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Check script blocks
scripts = re.findall(r'<script>(.*?)</script>', html, re.DOTALL)
print(f"Found {len(scripts)} script blocks.")

# Check for obvious unclosed tags or syntax errors
for i, s in enumerate(scripts):
    open_braces = s.count('{')
    close_braces = s.count('}')
    print(f"Script {i+1}: open_braces={open_braces}, close_braces={close_braces}, diff={open_braces - close_braces}")

print("Index.html length:", len(html))
