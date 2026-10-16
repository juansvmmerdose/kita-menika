import urllib.request
import ssl
import json

ssl._create_default_https_context = ssl._create_unverified_context
url = "https://api.github.com/repos/SniperGER/iOS-Wallpapers/contents/iPhone/iOS%2013"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    with urllib.request.urlopen(req) as resp:
        data = json.loads(resp.read().decode('utf-8'))
        for item in data:
            print(item['name'], item.get('download_url'))
except Exception as e:
    print("Error:", e)
