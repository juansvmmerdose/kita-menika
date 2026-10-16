import urllib.request
import re
import json

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5'
}

url = "https://www.instagram.com/jawara.photo/"
req = urllib.request.Request(url, headers=headers)
try:
    with urllib.request.urlopen(req, timeout=5) as r:
        html = r.read().decode('utf-8', errors='ignore')
        # check meta og:image
        og_img = re.findall(r'<meta[^>]+property="og:image"[^>]+content="([^"]+)"', html)
        print("og:image:", og_img)
        # check profile_pic_url
        pp = re.findall(r'"profile_pic_url":"([^"]+)"', html)
        print("profile_pic_url:", pp)
        # check profile_pic_url_hd
        pp_hd = re.findall(r'"profile_pic_url_hd":"([^"]+)"', html)
        print("profile_pic_url_hd:", pp_hd)
except Exception as e:
    print("Err:", e)
