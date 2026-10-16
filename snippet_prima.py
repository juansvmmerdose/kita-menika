with open('embed_dump.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.lower().find('prima')
if idx != -1:
    start = max(0, idx - 200)
    end = min(len(text), idx + 800)
    print("--- SNIPPET AROUND 'prima' ---")
    print(text[start:end])
