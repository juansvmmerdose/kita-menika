import re

with open('embed_dump.html', 'r', encoding='utf-8') as f:
    text = f.read()

scontent = re.findall(r'https://[^"\'\s<>\\]*scontent[^"\'\s<>\\]*', text)
print(f'Total scontent urls: {len(scontent)}')
for s in list(set(scontent))[:15]:
    print('SCONTENT:', s[:140])

# Also check for JSON or display_url
urls = re.findall(r'https:\\/\\/[^"\'\s<>]+', text)
print(f'Escaped urls: {len(urls)}')
for u in urls[:10]:
    clean = u.replace('\\/', '/')
    if 'scontent' in clean or 'cdninstagram' in clean:
        print('CLEAN ESCAPED:', clean[:140])
