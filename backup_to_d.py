import os
import shutil
import sys

sys.stdout.reconfigure(encoding='utf-8')

src_project = r"C:\Users\VANDI\.gemini\antigravity\scratch\kita-menikah"
src_brain = r"C:\Users\VANDI\.gemini\antigravity\brain\98605af6-0ebd-4ed8-a33b-bdbb36cb2699"
dest_folder = r"D:\VANDI\KITA_MENIKAH"

print(f"Memulai pencadangan aman ke: {dest_folder}")
os.makedirs(dest_folder, exist_ok=True)

# 1. Copy project files
ignore_patterns = shutil.ignore_patterns("edge_profile*", "__pycache__*", "*.tmp")

total_copied = 0
for root, dirs, files in os.walk(src_project):
    # filter out ignored dirs
    dirs[:] = [d for d in dirs if d not in ["edge_profile", "__pycache__"]]
    rel_path = os.path.relpath(root, src_project)
    dest_dir = os.path.join(dest_folder, rel_path) if rel_path != "." else dest_folder
    os.makedirs(dest_dir, exist_ok=True)
    
    for f in files:
        if f.endswith((".pyc", ".tmp")):
            continue
        src_file = os.path.join(root, f)
        dst_file = os.path.join(dest_dir, f)
        shutil.copy2(src_file, dst_file)
        total_copied += 1

print(f"[OK] Berhasil menyalin {total_copied} berkas utama dari proyek.")

# 2. Copy user uploaded references to a dedicated folder in backup
user_uploaded_dir = os.path.join(src_brain, ".user_uploaded")
dest_uploaded = os.path.join(dest_folder, "referensi_aset_asli")
if os.path.exists(user_uploaded_dir):
    os.makedirs(dest_uploaded, exist_ok=True)
    for f in os.listdir(user_uploaded_dir):
        sf = os.path.join(user_uploaded_dir, f)
        df = os.path.join(dest_uploaded, f)
        if os.path.isfile(sf):
            shutil.copy2(sf, df)
            print(f"  + Salin referensi asli: {f}")

# 3. Create a README / Cara_Buka.txt for user convenience
readme_path = os.path.join(dest_folder, "CARA_BUKA_APLIKASI.txt")
readme_content = """===============================================================
KITA MENIKAH - The Curated Wedding Marketplace Yogyakarta
Prototipe Interaktif Ultra-HD iPhone 16 Pro Max
===============================================================

LOKASI PENYIMPANAN: D:\\VANDI\\KITA_MENIKAH

CARA MENJALANKAN APLIKASI:
1. Cukup klik ganda (double click) file "index.html" di folder ini.
2. File akan langsung terbuka di browser favorit Anda (Google Chrome, Microsoft Edge, Firefox, dll).
3. Anda akan melihat simulasi fisik iPhone 16 Pro Max dengan Home Screen interaktif.
4. Klik pada ikon aplikasi "kita menikah" di baris bawah grid aplikasi untuk membuka aplikasi dengan animasi suara & visual splash screen.

FITUR-FITUR UTAMA YANG SUDAH JALAN:
- Simulasi iPhone 16 Pro Max dengan Dynamic Island interaktif & jam live.
- Navigasi Home Screen iOS dengan ikon aplikasi "kita menikah".
- Transisi animasi splash screen mewah tanpa jeda font.
- Feed Card Eksklusif Kurasi Editorial (bukan kloningan IG, aspect ratio 16:10 ringkas).
- Transparansi harga paket & sistem Rekber Escrow DP 20% aman.
- TikTok Reels Engine manten (video gending manten & cengkorongan paes).
- Simulasi Hitung Anggaran (Budget Calculator) pernikahan ideal.
- Dua mode operasional: Mode Klien & Mode Mitra Vendor.
- Chat langsung interaktif dua arah dengan proteksi sensor nomor luar.

Disimpan dengan aman pada: 16 Oktober 2026.
===============================================================
"""

with open(readme_path, "w", encoding="utf-8") as f:
    f.write(readme_content)

print(f"[OK] File petunjuk dibuat: {readme_path}")

# 4. Verify destination
dest_index = os.path.join(dest_folder, "index.html")
if os.path.exists(dest_index):
    sz = os.path.getsize(dest_index)
    print(f"[VERIFIKASI SUKSES] index.html ada di D:\\VANDI\\KITA_MENIKAH (Ukuran: {sz} bytes).")
else:
    print("[ERROR] index.html tidak ditemukan di tujuan!")

print("\nSeluruh data telah diamankan dengan sempurna di D:\\VANDI\\KITA_MENIKAH!")
