import json
import re

with open("build_26_vendors_index.py", "r", encoding="utf-8") as f:
    lines = f.readlines()

# Extract lines 5 to 1258 (0-indexed: lines 4 to 1258)
json_text = "".join(lines[4:1258])
# Remove "vendors = " at the beginning
json_text = json_text.strip()
if json_text.startswith("vendors ="):
    json_text = json_text[len("vendors ="):].strip()

vendors_list = json.loads(json_text)
print("Successfully loaded", len(vendors_list), "vendors!")

# Save to vendors_data.json
with open("vendors_data.json", "w", encoding="utf-8") as jf:
    json.dump(vendors_list, jf, indent=2, ensure_ascii=False)

# Read index.html
with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Replace vendors array
pattern = r"const vendors = \[[\s\S]*?\];\s*// INITIAL BOOKINGS DATA"
replacement = "const vendors = " + json.dumps(vendors_list, indent=4, ensure_ascii=False) + ";\n\n    // INITIAL BOOKINGS DATA"

new_html = re.sub(pattern, replacement, html)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(new_html)

brain_file = r"C:\Users\VANDI\.gemini\antigravity\brain\98605af6-0ebd-4ed8-a33b-bdbb36cb2699\preview_prototype.html"
with open(brain_file, "w", encoding="utf-8") as f:
    f.write(new_html)

print("Injected into index.html and preview_prototype.html successfully!")
