import os
import shutil

src_dir = r'C:\Users\VANDI\.gemini\antigravity\scratch\kita-menikah\assets'
dst_dir = r'C:\Users\VANDI\.gemini\antigravity\brain\98605af6-0ebd-4ed8-a33b-bdbb36cb2699\assets'

os.makedirs(dst_dir, exist_ok=True)
for item in os.listdir(src_dir):
    s = os.path.join(src_dir, item)
    d = os.path.join(dst_dir, item)
    if os.path.isfile(s):
        shutil.copy2(s, d)
        print(f"Copied file: {item}")
print("Assets synced!")
