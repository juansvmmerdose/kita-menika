import json
import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

m = re.search(r'const\s+vendors\s*=\s*(\[\s*\{.*?\}\s*\]);', text, re.DOTALL)
if not m:
    print("Could not find const vendors")
    exit(1)

vendors = json.loads(m.group(1))
print(f"Current count: {len(vendors)}")

mc_sound_vendors = [
    {
        "id": "mc-albertus",
        "name": "Albertus MC Wedding Jogja",
        "category": "mc",
        "city": "yogyakarta",
        "styleTag": "Bilingual & Modern",
        "locationText": "Kotagede, DI Yogyakarta",
        "priceStart": 2500000,
        "rating": 4.9,
        "reviewCount": 88,
        "isPromoted": true,
        "promoTier": "POPULAR",
        "igHandle": "@albertus_mcjogja",
        "igFollowers": "8.920 followers",
        "igPostsCount": "412 posts",
        "igUrl": "https://www.instagram.com/albertus_mcjogja/",
        "avatar": "assets/vendors/avatars/albertusmc.jpg",
        "description": "Master of Ceremony profesional pernikahan Jogja spesialis konsep Modern, Intimate, dan Bilingual (Indonesia - English). Suasana hangat, elegan, dan anti-canggung.",
        "slideIndex": 0,
        "slides": [
            {
                "image": "assets/vendors/slides/albertusmc_slide_1.jpg",
                "tag": "🔥 PALING BANYAK LIKE DI IG",
                "likes": "3.120 likes",
                "caption": "Memandu momen sakral & resepsi bahagia The Wedding of Kevin & Sarah di Grand Ballroom Jogja. Energy, elegance, and pure emotion! 🎤✨"
            }
        ],
        "packages": [
            {
                "id": "albertus-p1",
                "name": "MC Resepsi Modern (Bilingual)",
                "priceNum": 2500000,
                "price": "Rp 2.500.000",
                "detail": "MC resepsi durasi 3 jam, bilingual ID/EN, briefing keluarga & rundown koordinasi bersama WO, free meeting persiapan."
            },
            {
                "id": "albertus-p2",
                "name": "Paket Akad & Resepsi Full Day",
                "priceNum": 3800000,
                "price": "Rp 3.800.000",
                "detail": "Pemandu prosesi akad nikah sakral + MC resepsi perayaan, koordinasi vendor entertainment, gladi bersih H-1."
            },
            {
                "id": "albertus-p3",
                "name": "All-In MC + Live Band Akustik Wedding",
                "priceNum": 6500000,
                "price": "Rp 6.500.000",
                "detail": "MC utama berpengalaman + formasi akustik (vokal, keyboard, bass, cajon) + sound monitor panggung 3 jam."
            }
        ]
    },
    {
        "id": "mc-dimas",
        "name": "Dimas Pranatacara Adat Jogja",
        "category": "mc",
        "city": "yogyakarta",
        "styleTag": "Pranatacara Gagrag Ngayogyakarta",
        "locationText": "Kraton, DI Yogyakarta",
        "priceStart": 3000000,
        "rating": 5.0,
        "reviewCount": 92,
        "isPromoted": false,
        "promoTier": "VERIFIED",
        "igHandle": "@dimas_pranatacara",
        "igFollowers": "6.340 followers",
        "igPostsCount": "285 posts",
        "igUrl": "https://www.instagram.com/dimas_pranatacara/",
        "avatar": "assets/vendors/avatars/dimasmc.jpg",
        "description": "Pranatacara adat Jawa Gagrag Ngayogyakarta Hadiningrat bersertifikasi. Menguasai panyandra upacara panggih, siraman, kacar-kucur, dan temu manten ageng.",
        "slideIndex": 0,
        "slides": [
            {
                "image": "assets/vendors/slides/dimasmc_slide_1.jpg",
                "tag": "✨ UPACARA PANGGIH ADAT JOGJA",
                "likes": "2.890 likes",
                "caption": "Panyandra adiluhung upacara panggih manten gagrag Ngayogyakarta. Hangracik suwasana sakral kebak ing kabagyan. Nuwun 🙏"
            }
        ],
        "packages": [
            {
                "id": "dimas-p1",
                "name": "Pranatacara Upacara Panggih Adat",
                "priceNum": 3000000,
                "price": "Rp 3.000.000",
                "detail": "Pemandu upacara adat panggih (balangan suruh, wijidadi, sinduran, kacar-kucur, dulangan, sungkeman) krama inggil halus."
            },
            {
                "id": "dimas-p2",
                "name": "Paket Lengkap Siraman + Midodareni + Panggih",
                "priceNum": 5500000,
                "price": "Rp 5.500.000",
                "detail": "Rangkaian adat 2 hari: siraman sekar 7 sritaman, malam midodareni srah-srahan jonggolan, dan resepsi panggih ageng."
            }
        ]
    },
    {
        "id": "sound-pro",
        "name": "Pro Sound & Acoustics Jogja",
        "category": "sound",
        "city": "yogyakarta",
        "styleTag": "Line Array & Digital Mixing",
        "locationText": "Depok, Sleman",
        "priceStart": 3500000,
        "rating": 4.9,
        "reviewCount": 110,
        "isPromoted": true,
        "promoTier": "TOP RATED",
        "igHandle": "@prosound.jogja",
        "igFollowers": "7.810 followers",
        "igPostsCount": "320 posts",
        "igUrl": "https://www.instagram.com/prosound.jogja/",
        "avatar": "assets/vendors/avatars/prosound.jpg",
        "description": "Rental audio profesional pernikahan & event indoor/outdoor di Jogja. Menggunakan speaker line array RCF, digital console Allen & Heath, dan teknisi bersertifikat.",
        "slideIndex": 0,
        "slides": [
            {
                "image": "assets/vendors/slides/prosound_slide_1.jpg",
                "tag": "🔥 RIGGING & LINE ARRAY INDOOR",
                "likes": "2.410 likes",
                "caption": "Setting sound audio crystal clear untuk ballroom wedding 800 pax. Zero feedback, suara vokal MC & band empuk merata ke seluruh ruangan. 🔊"
            }
        ],
        "packages": [
            {
                "id": "prosound-p1",
                "name": "Paket Sound Intimate (5.000 Watt)",
                "priceNum": 3500000,
                "price": "Rp 3.500.000",
                "detail": "Kapasitas hingga 300 tamu, 4 mic wireless Shure UHF, mixer digital, 2 teknisi audio standby selama acara (6 jam)."
            },
            {
                "id": "prosound-p2",
                "name": "Paket Ballroom & Gedung (10.000 Watt)",
                "priceNum": 6000000,
                "price": "Rp 6.000.000",
                "detail": "Sistem speaker line array aktif, 6 wireless mic, stage monitor akustik, genset silent backup 30 kVA + operator."
            },
            {
                "id": "prosound-p3",
                "name": "Concert Grade Sound & Stage Production (20k Watt)",
                "priceNum": 11000000,
                "price": "Rp 11.000.000",
                "detail": "Kapasitas 1000+ tamu, tata suara konser band lengkap, sub-bass ground stack, digital mixing wireless iPad kontrol."
            }
        ]
    },
    {
        "id": "sound-mataram",
        "name": "Mataram Sound & Lighting Jogja",
        "category": "sound",
        "city": "yogyakarta",
        "styleTag": "High Fidelity & Lighting Ambience",
        "locationText": "Bantul, DI Yogyakarta",
        "priceStart": 4000000,
        "rating": 4.8,
        "reviewCount": 78,
        "isPromoted": false,
        "promoTier": "VERIFIED",
        "igHandle": "@mataramsound_jogja",
        "igFollowers": "5.620 followers",
        "igPostsCount": "194 posts",
        "igUrl": "https://www.instagram.com/mataramsound_jogja/",
        "avatar": "assets/vendors/avatars/mataramsound.jpg",
        "description": "Penyedia tata suara dan lighting panggung pernikahan elegan Jogja. Paket kombo hemat audio fidelity tinggi dengan tata lampu panggung dramatis & romantis.",
        "slideIndex": 0,
        "slides": [
            {
                "image": "assets/vendors/slides/mataramsound_slide_1.jpg",
                "tag": "✨ AMBIENCE LIGHTING & AUDIO",
                "likes": "1.980 likes",
                "caption": "Mewujudkan malam pernikahan berkesan dengan sound system premium dan tata cahaya moving head panggung di Jogja. 💡🎵"
            }
        ],
        "packages": [
            {
                "id": "mataram-p1",
                "name": "Combo Sound 7.500 Watt + Ambience Par LED",
                "priceNum": 4000000,
                "price": "Rp 4.000.000",
                "detail": "Tata suara 7.500 Watt + 8 unit Par LED warm light pelaminan, 4 mic Sennheiser, sound engineer & lighting man."
            },
            {
                "id": "mataram-p2",
                "name": "Full Production Sound 15k Watt + Beam Moving Head",
                "priceNum": 8500000,
                "price": "Rp 8.500.000",
                "detail": "Sound system line array 15.000 Watt + 4 moving head beam 380W + follow spot pengantin + mesin efek asap (dry ice)."
            }
        ]
    }
]

# Check if already in list
existing_ids = {v['id'] for v in vendors}
for n in mc_sound_vendors:
    if n['id'] not in existing_ids:
        vendors.append(n)

print(f"New total vendors count: {len(vendors)}")
