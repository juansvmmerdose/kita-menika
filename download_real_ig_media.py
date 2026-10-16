import urllib.request
import re
import os

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

vendors = [
    ("jawara", "jawara.photo"),
    ("sandiliem", "sandi.liem"),
    ("luxvisual", "luxvisual.id"),
    ("kitakancerita", "kitakancerita"),
    ("nijo", "thenijophotograph"),
    ("neiscala", "neiscala"),
    ("lunanouva", "lunanouovastudio__")
]

os.makedirs("assets/vendors/avatars", exist_ok=True)
os.makedirs("assets/vendors/slides", exist_ok=True)

for key, handle in vendors:
    url = f"https://greatfon.com/c/{handle}"
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as r:
            html = r.read().decode('utf-8', errors='ignore')
        
        # Look for user avatar: usually class="user__img" or inside .user-avatar
        avatar_match = re.findall(r'<div class="[^"]*user__img[^"]*"[^>]*style="background-image:\s*url\(\'([^\']+)\'\)', html)
        if not avatar_match:
            avatar_match = re.findall(r'<img[^>]+class="[^"]*user__avatar[^"]*"[^>]+src="([^"]+)"', html)
        if not avatar_match:
            avatar_match = re.findall(r'https://cdn2\.dumpor\.io/a/[a-zA-Z0-9-]+\.jpg', html)

        print(f"Vendor {key} ({handle}) found images: {len(avatar_match)}")
        
        # Download first image as avatar
        if avatar_match:
            av_url = avatar_match[0]
            print(f"Downloading avatar for {key}: {av_url}")
            try:
                img_req = urllib.request.Request(av_url, headers=headers)
                with urllib.request.urlopen(img_req, timeout=8) as img_resp:
                    with open(f"assets/vendors/avatars/{key}.jpg", "wb") as f:
                        f.write(img_resp.read())
                print(f"Saved assets/vendors/avatars/{key}.jpg")
            except Exception as e:
                print(f"Err downloading avatar for {key}: {e}")

        # Download up to 3 post images for slides
        post_imgs = re.findall(r'https://cdn2\.dumpor\.io/a/[a-zA-Z0-9-]+\.jpg', html)
        unique_posts = list(dict.fromkeys(post_imgs))
        # Skip the first if it was avatar, take next 3
        slides_to_save = unique_posts[1:4] if len(unique_posts) > 1 else unique_posts[:3]
        for idx, p_url in enumerate(slides_to_save):
            try:
                img_req = urllib.request.Request(p_url, headers=headers)
                with urllib.request.urlopen(img_req, timeout=8) as img_resp:
                    out_path = f"assets/vendors/slides/{key}_slide_{idx+1}.jpg"
                    with open(out_path, "wb") as f:
                        f.write(img_resp.read())
                print(f"Saved slide {idx+1} for {key}")
            except Exception as e:
                print(f"Err slide {idx+1} for {key}: {e}")
    except Exception as e:
        print(f"Err fetching {handle}: {e}")
