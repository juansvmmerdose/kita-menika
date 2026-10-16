import re
import json

from build_26_vendors_index import vendors_data

with open("index.html", "r", encoding="utf-8") as f:
    text = f.read()

pattern = r"const vendors = \[[\s\S]*?\];\s*// INITIAL BOOKINGS DATA"
replacement = "const vendors = " + json.dumps(vendors_data, indent=4, ensure_ascii=False) + ";\n\n    // INITIAL BOOKINGS DATA"

new_html = re.sub(pattern, replacement, text)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(new_html)

brain_file = r"C:\Users\VANDI\.gemini\antigravity\brain\98605af6-0ebd-4ed8-a33b-bdbb36cb2699\preview_prototype.html"
with open(brain_file, "w", encoding="utf-8") as f:
    f.write(new_html)

print("Injected 26 vendors successfully!")
