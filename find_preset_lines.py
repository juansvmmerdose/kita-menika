file_path = r"C:\Users\VANDI\.gemini\antigravity\scratch\kita-menikah\index.html"
with open(file_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

for i, l in enumerate(lines):
    if "applyBudgetPreset" in l:
        print(f"applyBudgetPreset at line {i+1}")
    if "filterSavedCategory" in l:
        print(f"filterSavedCategory at line {i+1}")
