import os

file_path = r"C:\Users\VANDI\.gemini\antigravity\scratch\kita-menikah\index.html"
backup_path = r"C:\Users\VANDI\.gemini\antigravity\scratch\kita-menikah\index.html.bak"

# Make a backup first
if os.path.exists(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    with open(backup_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("Backup created successfully.")
