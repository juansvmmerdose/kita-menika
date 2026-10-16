import sys
sys.stdout.reconfigure(encoding='utf-8')

with open(r"C:\Users\VANDI\.gemini\antigravity\scratch\kita-menikah\index.html", "r", encoding="utf-8") as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if "(kita menikah)" in line or "(KITA MENIKAH)" in line:
        print(f"Line {i+1}: {line.strip()}")
