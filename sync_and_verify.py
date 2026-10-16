import shutil
import os

src = r"C:\Users\VANDI\.gemini\antigravity\scratch\kita-menikah\index.html"
dst = r"C:\Users\VANDI\.gemini\antigravity\brain\98605af6-0ebd-4ed8-a33b-bdbb36cb2699\preview_prototype.html"

# Copy index.html to preview_prototype.html
shutil.copy2(src, dst)
print("Copied successfully.")

# Verify key markers in index.html and preview_prototype.html
with open(dst, "r", encoding="utf-8") as f:
    content = f.read()

checks = [
    ("app_icon_squircle.png", "Squircle bubble asset used"),
    ("EXCLUSIVE CURATED EDITORIAL WEDDING MARKETPLACE CARD", "Exclusive editorial wedding card present"),
    ("aspect-[16/10]", "Compact aspect ratio present"),
    ("btnAppKitaMenikah", "App button present"),
    ("launchKitaMenikahApp", "Launch app function present"),
    ("Rekber Aman (DP 20%)", "Rekber badge present")
]

all_passed = True
for term, desc in checks:
    if term in content:
        print(f"[OK] {desc}")
    else:
        print(f"[FAILED] {desc}")
        all_passed = False

print(f"File size: {len(content)} bytes")
print("Status:", "ALL CHECKS PASSED" if all_passed else "SOME CHECKS FAILED")
