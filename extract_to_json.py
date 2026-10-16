import re
import json

# Replace true/false with True/False in build_26_vendors_index.py
with open("build_26_vendors_index.py", "r", encoding="utf-8") as f:
    code = f.read()

# Read fromvendors_data = [ ... ]
m = re.search(r"vendors_data = (\[[\s\S]*?\])\s*# Write updated script", code)
if m:
    raw_json = m.group(1).replace("True", "true").replace("False", "false")
    data = json.loads(raw_json)
    with open("vendors_data.json", "w", encoding="utf-8") as jf:
        json.dump(data, jf, indent=2, ensure_ascii=False)
    print("Saved vendors_data.json with", len(data), "vendors!")
else:
    print("Could not find vendors_data block")
