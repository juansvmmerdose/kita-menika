file_path = r"C:\Users\VANDI\.gemini\antigravity\scratch\kita-menikah\index.html"
with open(file_path, "r", encoding="utf-8") as f:
    text = f.read()

print("function applyBudgetPreset in script:", "function applyBudgetPreset" in text)
print("updateSavedBadge() in text:", "updateSavedBadge()" in text)
