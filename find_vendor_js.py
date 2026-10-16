with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if 'vendorList' in line or 'vendorsData' in line or 'function filterVendors' in line:
        print(f"{i+1}: {line.strip()[:100]}")
