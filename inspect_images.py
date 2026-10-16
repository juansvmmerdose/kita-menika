import os
from PIL import Image

def inspect_folder(folder):
    print(f"=== {folder} ===")
    for f in sorted(os.listdir(folder)):
        path = os.path.join(folder, f)
        if os.path.isfile(path) and f.endswith(('.jpg', '.png', '.jpeg')):
            try:
                im = Image.open(path)
                print(f"  {f:30s} {im.size} {im.mode} ({os.path.getsize(path)//1024} KB)")
            except Exception as e:
                print(f"  {f:30s} ERROR: {e}")

inspect_folder("assets/vendors/avatars")
inspect_folder("assets/vendors/slides")
