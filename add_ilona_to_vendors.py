import json
import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

m_vendors = re.search(r'const\s+vendors\s*=\s*(\[\s*\{.*?\}\s*\]);', html, re.DOTALL)
if not m_vendors:
    print("Could not find const vendors")
    exit(1)

vendors = json.loads(m_vendors.group(1))

# Check if ilona already exists
if any(v["id"] == "wo-ilona" for v in vendors):
    print("Ilona already exists in vendors, skipping add.")
else:
    ilona_vendor = {
        "id": "wo-ilona",
        "name": "Ilona Wedding Organizer",
        "category": "wo",
        "city": "yogyakarta",
        "styleTag": "Seamless & Intimate Planning",
        "locationText": "Sleman & Kota, DI Yogyakarta",
        "priceStart": 4500000,
        "rating": 5.0,
        "reviewCount": 98,
        "isPromoted": True,
        "promoTier": "RECOMMENDED",
        "igHandle": "@ilonaorganizer",
        "igFollowers": "5.480 followers",
        "igPostsCount": "340 posts",
        "igUrl": "https://www.instagram.com/ilonaorganizer/",
        "avatar": "assets/vendors/avatars/ilona.jpg",
        "description": "Wedding Planner & Organizer berdedikasi berbasis di Yogyakarta. Menghadirkan pendampingan pernikahan penuh kehangatan, detail terencana sempurna, koordinasi vendor seamless, dan eksekusi hari-H bebas stres (peace of mind).",
        "slideIndex": 0,
        "slides": [
            {
                "image": "assets/vendors/slides/ilona_slide_1.jpg",
                "tag": "🔥 PALING BANYAK LIKE DI IG",
                "likes": "3.740 likes",
                "caption": "Every love story is beautiful, but yours is our favorite. The sacred and joyful wedding day with @ilonaorganizer #weddingplannerjogja #ilonaorganizer #weddingjogja ✨💍"
            },
            {
                "image": "assets/vendors/slides/ilona_slide_2.jpg",
                "tag": "✨ SEAMLESS D-DAY EXECUTION",
                "likes": "2.910 likes",
                "caption": "Menjaga setiap detik momen berjalan syahdu dan lancar tanpa beban bagi kedua mempelai dan keluarga tercinta. Warmest congratulations! 🤍"
            }
        ],
        "packages": [
            {
                "id": "ilona-p1",
                "name": "Paket D-Day Coordination (6 Crew Akad & Resepsi)",
                "priceNum": 4500000,
                "price": "Rp 4.500.000",
                "detail": "Pengawalan intensif hari-H akad & resepsi, 6 profesional crew (1 koordinator utama, 1 pendamping pengantin, 1 pendamping keluarga, 1 konsumsi & VIP, 2 stage/rundown), briefing H-7, koordinasi vendor H-14."
            },
            {
                "id": "ilona-p2",
                "name": "Paket Full Wedding Planner & Organizer (9 Crew)",
                "priceNum": 8500000,
                "price": "Rp 8.500.000",
                "detail": "Pendampingan dari H-3 bulan: budgeting breakdown, kurasi vendor terpercaya, meeting berkala, gladi resik, 9 crew profesional hari-H, pendampingan akad nikah, upacara adat/nasional, & resepsi."
            },
            {
                "id": "ilona-p3",
                "name": "Paket All-In Intimate Wedding + Konsultasi Adat Lengkap",
                "priceNum": 12000000,
                "price": "Rp 12.000.000",
                "detail": "Perencanaan komprehensif dari konsepsi tema hingga pasca acara, pengawalan rangkaian siraman/midodareni & hari-H, 12 crew terlatih, emergency kit pengantin lengkap, family liaison VIP."
            }
        ]
    }

    # Find position of wo vendors and insert Ilona right at the top of WO or near Mahkota
    wo_idx = -1
    for i, v in enumerate(vendors):
        if v["category"] == "wo":
            wo_idx = i
            break
    
    if wo_idx != -1:
        vendors.insert(wo_idx, ilona_vendor)
    else:
        vendors.append(ilona_vendor)

    print(f"Added Ilona Wedding Organizer! Total vendors: {len(vendors)}")

# Update count in button
html = re.sub(r'<span>Semua \(\d+\)</span>', f'<span>Semua ({len(vendors)})</span>', html)

# Serialize back
new_vendors_json = "const vendors = " + json.dumps(vendors, indent=4, ensure_ascii=False) + ";"
html = html[:m_vendors.start()] + new_vendors_json + html[m_vendors.end():]

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Saved updated index.html successfully!")
