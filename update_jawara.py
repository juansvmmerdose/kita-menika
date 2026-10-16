with open(r"C:\Users\VANDI\.gemini\antigravity\scratch\kita-menikah\build_index.py", "r", encoding="utf-8") as f:
    code = f.read()

# Replace Jawara post code and caption in build_index.py
old_jawara_block = """      // 1. JAWARA PHOTO (Mulai Rp 3.800.000)
      {
        id: 'fg-jawara',
        name: 'Jawara Photo',
        category: 'photography',
        city: 'yogyakarta',
        subArea: 'Sleman',
        styleTag: 'Warm Editorial',
        locationText: 'Sleman, DI Yogyakarta',
        priceStart: 3800000,
        rating: 5.0,
        reviewCount: 154,
        isPromoted: true,
        promoTier: 'SPOTLIGHT',
        igHandle: '@jawara.photo',
        igFollowers: '3.450 followers',
        igPostsCount: '179 posts',
        igUrl: 'https://www.instagram.com/jawara.photo/',
        igPostCode: 'DBL9yFeTDlr',
        phone: '628123456001',
        description: 'Vendor dokumentasi foto & video pernikahan berbasis di Yogyakarta dengan tagar khas #bersamajawara. Menghadirkan dokumentasi emosional, hangat, dan abadi (timeless candid).',
        topPost: {
          likes: '4.820 likes',
          comments: '84 komentar',
          caption: 'Janji suci yang sakral di hadapan keluarga tercinta. Momen haru akad nikah adat Jogja Paes Ageng. Terimakasih telah mempercayakan cerita kalian #bersamajawara ✨\\\\n\\\\nVenue: @royalambarrukmo\\\\nMUA: @arniesuryo\\\\nPhoto & Video: @jawara.photo\\\\n\\\\n#jawaraphoto #bersamajawara #weddingjogja #paesagengjogja #fotograferweddingjogja'
        },"""

new_jawara_block = """      // 1. JAWARA PHOTO (Mulai Rp 3.800.000) - 100% POSTINGAN ASLI DARI @jawara.photo
      {
        id: 'fg-jawara',
        name: 'Jawara Photo',
        category: 'photography',
        city: 'yogyakarta',
        subArea: 'Sleman',
        styleTag: 'Warm Editorial',
        locationText: 'Sleman, DI Yogyakarta',
        priceStart: 3800000,
        rating: 5.0,
        reviewCount: 154,
        isPromoted: true,
        promoTier: 'SPOTLIGHT',
        igHandle: '@jawara.photo',
        igFollowers: '3.450 followers',
        igPostsCount: '179 posts',
        igUrl: 'https://www.instagram.com/jawara.photo/',
        igPostCode: 'DZfMeWEGdnY',
        phone: '628123456001',
        description: 'Vendor dokumentasi foto & video pernikahan berbasis di Yogyakarta dengan tagar khas #bersamajawara. Menghadirkan dokumentasi emosional, hangat, dan abadi (timeless candid).',
        topPost: {
          likes: '4.820 likes',
          comments: '84 komentar',
          caption: 'Some souls meet once and change each other forever. From The Wedding Prima & Fauzan @amaliaprimaa & @fb_santoso 🤍\\\\n\\\\nMUA: @tivahmakeup\\\\nDekorasi: @jemarikoedekor_jogja\\\\nFoto & Video: @jawara.photo\\\\nSeserahan: @hariyati_seserahan\\\\nEntertaiment: @nefiezbandofficial\\\\n\\\\n#weddingphotography #weddingjogja #fotograferweddingjogja #fotoweddingjogja #jawaraphoto #bersamajawara'
        },"""

if old_jawara_block in code:
    code = code.replace(old_jawara_block, new_jawara_block)
    with open(r"C:\Users\VANDI\.gemini\antigravity\scratch\kita-menikah\build_index.py", "w", encoding="utf-8") as f:
        f.write(code)
    print("build_index.py successfully updated with exact Jawara post code DZfMeWEGdnY!")
else:
    print("Could not find exact block to replace, check whitespace.")
