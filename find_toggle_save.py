file_path = r"C:\Users\VANDI\.gemini\antigravity\scratch\kita-menikah\index.html"
with open(file_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

for i, l in enumerate(lines):
    if "function toggleSave" in l:
        print(f"toggleSave at line {i+1}")
