import re

file_path = r"C:\Users\VANDI\.gemini\antigravity\scratch\kita-menikah\index.html"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

print("Original size:", len(content))

# 1. Check hardware buttons
has_hw_buttons = "-left-[13px]" in content
print("Hardware buttons present:", has_hw_buttons)

# 2. Check static reels
has_reel_2 = "<!-- REEL 2: SUNGKEMAN" in content
print("Reel 2 static present:", has_reel_2)

# Check line numbers around hardware buttons
lines = content.splitlines()
for idx, line in enumerate(lines[:100]):
    if "iphoneDeviceFrame" in line or "-left-[13px]" in line or "iphoneStatusBar" in line:
        print(f"Line {idx+1}: {line[:90]}")
