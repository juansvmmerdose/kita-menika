file_path = r"C:\Users\VANDI\.gemini\antigravity\scratch\kita-menikah\index.html"
with open(file_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

for i, l in enumerate(lines):
    if "viewTikTok" in l:
        print(f"viewTikTok: line {i+1}")
    if "<!-- REEL 2: SUNGKEMAN" in l:
        print(f"Reel 2 start: line {i+1}")
    if "<!-- REEL 4: CATERING" in l:
        print(f"Reel 4 start: line {i+1}")
    if "bottomDockWrapper" in l:
        print(f"bottomDockWrapper: line {i+1}")
