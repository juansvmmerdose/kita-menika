file_path = r"C:\Users\VANDI\.gemini\antigravity\scratch\kita-menikah\index.html"
with open(file_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

for i, l in enumerate(lines):
    if "function switchTab" in l or "tabSequence" in l:
        print(f"Line {i+1}: {l.strip()}")
