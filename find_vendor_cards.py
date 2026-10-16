with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if 'vendor-card' in line or 'id="vendorList"' in line or 'Mamuk Rahmadona' in line or 'Ilona' in line:
        print(f"{i+1}: {line.strip()[:100]}")
        if i > 500: # just show first few
            break
