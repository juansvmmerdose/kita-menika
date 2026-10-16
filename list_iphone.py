import urllib.request
import ssl
import json

ssl._create_default_https_context = ssl._create_unverified_context
url = "https://api.github.com/repos/SniperGER/iOS-Wallpapers/contents/iPhone"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    with urllib.request.urlopen(req) as resp:
        data = json.loads(resp.read().decode('utf-8'))
        print([x['name'] for x in data])
except Exception as e:
    print("Error:", e)
