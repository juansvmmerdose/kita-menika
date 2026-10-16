with open('embed_dump.html', 'r', encoding='utf-8') as f:
    text = f.read()

keywords = ['jawara', 'prima', 'bersamajawara', 'caption', 'like', 'likes', 'edge_liked_by']
for kw in keywords:
    count = text.lower().count(kw.lower())
    print(f"'{kw}': {count} occurrences")
