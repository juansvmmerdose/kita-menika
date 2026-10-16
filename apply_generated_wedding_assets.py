import os
import shutil
from PIL import Image

brain_dir = r"C:\Users\VANDI\.gemini\antigravity\brain\98605af6-0ebd-4ed8-a33b-bdbb36cb2699"
scratch_dir = r"C:\Users\VANDI\.gemini\antigravity\scratch\kita-menikah"

def crop_center_square(img_path, out_path, size=(300, 300)):
    with Image.open(img_path) as im:
        w, h = im.size
        min_dim = min(w, h)
        left = (w - min_dim) // 2
        top = (h - min_dim) // 2
        right = left + min_dim
        bottom = top + min_dim
        cropped = im.crop((left, top, right, bottom))
        resized = cropped.resize(size, Image.Resampling.LANCZOS)
        resized.save(out_path, quality=95)
        print(f"Created square avatar: {out_path}")

# 1. Mamuk Paes Ageng
mamuk_gen = os.path.join(brain_dir, "mamuk_paes_ageng_1792056701532.jpg")
if os.path.exists(mamuk_gen):
    shutil.copy2(mamuk_gen, os.path.join(scratch_dir, "assets/vendors/slides/mamuk_slide_1.jpg"))
    crop_center_square(mamuk_gen, os.path.join(scratch_dir, "assets/vendors/avatars/mamuk.jpg"))

# 2. Arnie Suryo Paes Ageng
arnie_gen = os.path.join(brain_dir, "arniesuryo_paes_1792056726054.jpg")
if os.path.exists(arnie_gen):
    shutil.copy2(arnie_gen, os.path.join(scratch_dir, "assets/vendors/slides/arniesuryo_slide_1.jpg"))
    crop_center_square(arnie_gen, os.path.join(scratch_dir, "assets/vendors/avatars/arniesuryo.jpg"))

# 3. Vidi Catering
vidi_gen = os.path.join(brain_dir, "vidi_catering_buffet_1792056746750.jpg")
if os.path.exists(vidi_gen):
    shutil.copy2(vidi_gen, os.path.join(scratch_dir, "assets/vendors/slides/vidi_slide_1.jpg"))
    shutil.copy2(vidi_gen, os.path.join(scratch_dir, "assets/vendors/slides/shinta_slide_1.jpg"))
    shutil.copy2(vidi_gen, os.path.join(scratch_dir, "assets/vendors/slides/alburuj_slide_1.jpg"))
    shutil.copy2(vidi_gen, os.path.join(scratch_dir, "assets/vendors/slides/karunia_slide_1.jpg"))
    crop_center_square(vidi_gen, os.path.join(scratch_dir, "assets/vendors/avatars/vidi.jpg"))

# 4. Ilona Wedding Organizer
ilona_gen = os.path.join(brain_dir, "ilona_wo_team_1792056767024.jpg")
if os.path.exists(ilona_gen):
    shutil.copy2(ilona_gen, os.path.join(scratch_dir, "assets/vendors/slides/ilona_slide_1.jpg"))
    shutil.copy2(ilona_gen, os.path.join(scratch_dir, "assets/vendors/slides/mahkota_slide_1.jpg"))
    shutil.copy2(ilona_gen, os.path.join(scratch_dir, "assets/vendors/slides/weddingkujogja_slide_1.jpg"))
    crop_center_square(ilona_gen, os.path.join(scratch_dir, "assets/vendors/avatars/ilona.jpg"))

# 5. Albertus MC
mc_gen = os.path.join(brain_dir, "albertus_mc_stage_1792056789149.jpg")
if os.path.exists(mc_gen):
    shutil.copy2(mc_gen, os.path.join(scratch_dir, "assets/vendors/slides/albertusmc_slide_1.jpg"))
    crop_center_square(mc_gen, os.path.join(scratch_dir, "assets/vendors/avatars/albertusmc.jpg"))

# 6. Pro Sound & Lighting
sound_gen = os.path.join(brain_dir, "pro_sound_audio_1792056811884.jpg")
if os.path.exists(sound_gen):
    shutil.copy2(sound_gen, os.path.join(scratch_dir, "assets/vendors/slides/prosound_slide_1.jpg"))
    shutil.copy2(sound_gen, os.path.join(scratch_dir, "assets/vendors/slides/mataramsound_slide_1.jpg"))
    crop_center_square(sound_gen, os.path.join(scratch_dir, "assets/vendors/avatars/prosound.jpg"))

print("Successfully applied new authentic wedding assets!")
