import json
import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Update const vendors with MC and Sound System
m_vendors = re.search(r'const\s+vendors\s*=\s*(\[\s*\{.*?\}\s*\]);', html, re.DOTALL)
if not m_vendors:
    print("Error: Could not find const vendors")
    exit(1)

vendors = json.loads(m_vendors.group(1))

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
        "isPromoted": True,
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
        "isPromoted": False,
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
        "isPromoted": True,
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
        "isPromoted": False,
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

existing_ids = {v['id'] for v in vendors}
for n in mc_sound_vendors:
    if n['id'] not in existing_ids:
        vendors.append(n)

new_vendors_json = "const vendors = " + json.dumps(vendors, indent=4, ensure_ascii=False) + ";"
html = html[:m_vendors.start()] + new_vendors_json + html[m_vendors.end():]

print(f"Updated const vendors: {len(vendors)} vendors total.")

# 2. Add Quick 8-icon navigation row right under header
quick_menu_html = """
      <!-- 8 IKON KATEGORI & MENU DENGAN WARNA KHAS MASING-MASING (SEKALI KLIK PINDAH MENU) -->
      <section id="clientQuickMenu" class="px-4 py-3 bg-neutral-950/90 border-b border-neutral-900 sticky top-[108px] z-30 backdrop-blur">
        <div class="flex items-center justify-between mb-2 px-1">
          <div class="flex items-center space-x-1.5">
            <span class="w-1.5 h-1.5 rounded-full bg-amber-400"></span>
            <span class="text-[9px] tracking-[0.2em] uppercase font-bold text-neutral-300">Menu & Kategori Terkurasi</span>
          </div>
          <button onclick="selectQuickCategory('all')" id="qnav-btn-all" class="text-[10px] text-neutral-400 hover:text-white font-semibold transition flex items-center space-x-1">
            <span>Semua (34)</span>
            <span>→</span>
          </button>
        </div>

        <!-- 8 GRID IKON DENGAN WARNA SENDIRI -->
        <div class="grid grid-cols-4 gap-2">
          
          <!-- 1. KAMERA BUAT FG (Rose / Coral Neon) -->
          <button onclick="selectQuickCategory('photography')" id="qnav-btn-photography" class="group flex flex-col items-center text-center p-1.5 rounded-xl transition active:scale-95">
            <div id="qnav-box-photography" class="quick-nav-box w-12 h-12 rounded-2xl bg-rose-500/15 border border-rose-500/40 text-rose-400 flex items-center justify-center transition-all duration-200 group-hover:bg-rose-500/25 group-hover:scale-105 shadow-sm shadow-rose-950/30">
              <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.8" d="M3 9a2 2 0 012-2h.93a2 2 0 001.664-.89l.812-1.22A2 2 0 0110.07 4h3.86a2 2 0 011.664.89l.812 1.22A2 2 0 0018.07 7H19a2 2 0 012 2v9a2 2 0 01-2 2H5a2 2 0 01-2-2V9z"/>
                <circle cx="12" cy="13" r="3.5" stroke-width="1.8"/>
              </svg>
            </div>
            <span class="text-[10px] font-bold text-rose-300 group-hover:text-white mt-1.5 leading-tight">FG Foto</span>
            <span class="text-[8px] text-neutral-400">Teman & Pro</span>
          </button>

          <!-- 2. MAKANAN BUAT CATHERING (Warm Amber / Gold) -->
          <button onclick="selectQuickCategory('catering')" id="qnav-btn-catering" class="group flex flex-col items-center text-center p-1.5 rounded-xl transition active:scale-95">
            <div id="qnav-box-catering" class="quick-nav-box w-12 h-12 rounded-2xl bg-amber-500/15 border border-amber-500/40 text-amber-400 flex items-center justify-center transition-all duration-200 group-hover:bg-amber-500/25 group-hover:scale-105 shadow-sm shadow-amber-950/30">
              <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.8" d="M12 4v2m0 0a7 7 0 017 7v1H5v-1a7 7 0 017-7zm-9 11h18a1 1 0 011 1v1a1 1 0 01-1 1H3a1 1 0 01-1-1v-1a1 1 0 011-1z"/>
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.8" d="M10 4a2 2 0 114 0"/>
              </svg>
            </div>
            <span class="text-[10px] font-bold text-amber-300 group-hover:text-white mt-1.5 leading-tight">Catering</span>
            <span class="text-[8px] text-neutral-400">Prasmanan</span>
          </button>

          <!-- 3. RUMAH BUAT VENUE (Sky Blue / Azure) -->
          <button onclick="selectQuickCategory('venue')" id="qnav-btn-venue" class="group flex flex-col items-center text-center p-1.5 rounded-xl transition active:scale-95">
            <div id="qnav-box-venue" class="quick-nav-box w-12 h-12 rounded-2xl bg-sky-500/15 border border-sky-500/40 text-sky-400 flex items-center justify-center transition-all duration-200 group-hover:bg-sky-500/25 group-hover:scale-105 shadow-sm shadow-sky-950/30">
              <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.8" d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6"/>
              </svg>
            </div>
            <span class="text-[10px] font-bold text-sky-300 group-hover:text-white mt-1.5 leading-tight">Venue</span>
            <span class="text-[8px] text-neutral-400">Joglo & Hotel</span>
          </button>

          <!-- 4. LOGO PELAYANAN UNTUK WO (Royal Purple / Violet) -->
          <button onclick="selectQuickCategory('wo')" id="qnav-btn-wo" class="group flex flex-col items-center text-center p-1.5 rounded-xl transition active:scale-95">
            <div id="qnav-box-wo" class="quick-nav-box w-12 h-12 rounded-2xl bg-purple-500/15 border border-purple-500/40 text-purple-400 flex items-center justify-center transition-all duration-200 group-hover:bg-purple-500/25 group-hover:scale-105 shadow-sm shadow-purple-950/30">
              <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.8" d="M15 17h5l-1.405-1.405A2.032 2.032 0 0118 14.158V11a6.002 6.002 0 00-4-5.659V5a2 2 0 10-4 0v.341C7.67 6.165 6 8.388 6 11v3.159c0 .538-.214 1.055-.595 1.436L4 17h5m6 0v1a3 3 0 11-6 0v-1m6 0H9"/>
              </svg>
            </div>
            <span class="text-[10px] font-bold text-purple-300 group-hover:text-white mt-1.5 leading-tight">WO Planner</span>
            <span class="text-[8px] text-neutral-400">Pelayanan</span>
          </button>

          <!-- 5. CERMIN DAN ORANG DANDAN BUAT MUA (Fuchsia / Hot Pink) -->
          <button onclick="selectQuickCategory('mua')" id="qnav-btn-mua" class="group flex flex-col items-center text-center p-1.5 rounded-xl transition active:scale-95">
            <div id="qnav-box-mua" class="quick-nav-box w-12 h-12 rounded-2xl bg-fuchsia-500/15 border border-fuchsia-500/40 text-fuchsia-400 flex items-center justify-center transition-all duration-200 group-hover:bg-fuchsia-500/25 group-hover:scale-105 shadow-sm shadow-fuchsia-950/30">
              <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <circle cx="12" cy="9" r="6" stroke-width="1.8"/>
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.8" d="M12 15v6m-3 0h6M9 9a3 3 0 013-3"/>
              </svg>
            </div>
            <span class="text-[10px] font-bold text-fuchsia-300 group-hover:text-white mt-1.5 leading-tight">MUA Rias</span>
            <span class="text-[8px] text-neutral-400">Paes Ageng</span>
          </button>

          <!-- 6. ORANG NGOMONG BUAT MC (Crimson Orange) -->
          <button onclick="selectQuickCategory('mc')" id="qnav-btn-mc" class="group flex flex-col items-center text-center p-1.5 rounded-xl transition active:scale-95">
            <div id="qnav-box-mc" class="quick-nav-box w-12 h-12 rounded-2xl bg-orange-500/15 border border-orange-500/40 text-orange-400 flex items-center justify-center transition-all duration-200 group-hover:bg-orange-500/25 group-hover:scale-105 shadow-sm shadow-orange-950/30">
              <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.8" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"/>
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.8" d="M18.5 7.5a3.5 3.5 0 010 5M20.5 5.5a6.5 6.5 0 010 9"/>
              </svg>
            </div>
            <span class="text-[10px] font-bold text-orange-300 group-hover:text-white mt-1.5 leading-tight">MC Acara</span>
            <span class="text-[8px] text-neutral-400">Adat & Modern</span>
          </button>

          <!-- 7. SOUND BUAT SOUNDSYSTEM (Electric Teal / Cyan) -->
          <button onclick="selectQuickCategory('sound')" id="qnav-btn-sound" class="group flex flex-col items-center text-center p-1.5 rounded-xl transition active:scale-95">
            <div id="qnav-box-sound" class="quick-nav-box w-12 h-12 rounded-2xl bg-teal-500/15 border border-teal-500/40 text-teal-300 flex items-center justify-center transition-all duration-200 group-hover:bg-teal-500/25 group-hover:scale-105 shadow-sm shadow-teal-950/30">
              <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.8" d="M15.536 8.464a5 5 0 010 7.072m2.828-9.9a9 9 0 010 12.728M5.586 15H4a1 1 0 01-1-1v-4a1 1 0 011-1h1.586l4.707-4.707C10.923 3.663 12 4.109 12 5v14c0 .891-1.077 1.337-1.707.707L5.586 15z"/>
              </svg>
            </div>
            <span class="text-[10px] font-bold text-teal-300 group-hover:text-white mt-1.5 leading-tight">Sound System</span>
            <span class="text-[8px] text-neutral-400">Audio & Light</span>
          </button>

          <!-- 8. CALCULATOR BUAT BUDGET (Emerald Mint Green) -->
          <button onclick="selectQuickCategory('budget')" id="qnav-btn-budget" class="group flex flex-col items-center text-center p-1.5 rounded-xl transition active:scale-95">
            <div id="qnav-box-budget" class="quick-nav-box w-12 h-12 rounded-2xl bg-emerald-500/15 border border-emerald-500/40 text-emerald-400 flex items-center justify-center transition-all duration-200 group-hover:bg-emerald-500/25 group-hover:scale-105 shadow-sm shadow-emerald-950/30">
              <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.8" d="M9 7h6m0 10v-3m-3 3h.01M9 17h.01M9 14h.01M12 14h.01M15 11h.01M12 11h.01M9 11h.01M7 21h10a2 2 0 002-2V5a2 2 0 00-2-2H7a2 2 0 00-2 2v14a2 2 0 002 2z"/>
              </svg>
            </div>
            <span class="text-[10px] font-bold text-emerald-300 group-hover:text-white mt-1.5 leading-tight">Kalkulator</span>
            <span class="text-[8px] text-neutral-400">Hitung Biaya</span>
          </button>

        </div>
      </section>
"""

# Replace header ending or place clientQuickMenu right after </header>
if 'id="clientQuickMenu"' not in html:
    html = html.replace('</header>', '</header>\n' + quick_menu_html)
    print("Inserted clientQuickMenu after </header>")

# 3. Add id="vendorListSection" to the vendor list wrapper for smooth scrolling
html = html.replace('<!-- VENDORS LIST -->\n        <div class="px-5">', '<!-- VENDORS LIST -->\n        <div id="vendorListSection" class="px-5 pt-2">')

# 4. Update the horizontal category slider buttons to also include mc and sound
old_pills = """            <button onclick="setCategory('catering')" id="cat-catering" class="cat-pill px-3.5 py-1.5 rounded-full border border-neutral-800 bg-neutral-900 text-neutral-300 text-xs font-semibold whitespace-nowrap hover:border-neutral-600 transition">
              🍽️ Catering
            </button>
            <button onclick="setCategory('wo')" id="cat-wo" class="cat-pill px-3.5 py-1.5 rounded-full border border-neutral-800 bg-neutral-900 text-neutral-300 text-xs font-semibold whitespace-nowrap hover:border-neutral-600 transition">
              📋 Wedding Organizer
            </button>"""

new_pills = """            <button onclick="setCategory('catering')" id="cat-catering" class="cat-pill px-3.5 py-1.5 rounded-full border border-neutral-800 bg-neutral-900 text-neutral-300 text-xs font-semibold whitespace-nowrap hover:border-neutral-600 transition">
              🍽️ Catering
            </button>
            <button onclick="setCategory('wo')" id="cat-wo" class="cat-pill px-3.5 py-1.5 rounded-full border border-neutral-800 bg-neutral-900 text-neutral-300 text-xs font-semibold whitespace-nowrap hover:border-neutral-600 transition">
              📋 Wedding Organizer
            </button>
            <button onclick="setCategory('mc')" id="cat-mc" class="cat-pill px-3.5 py-1.5 rounded-full border border-neutral-800 bg-neutral-900 text-neutral-300 text-xs font-semibold whitespace-nowrap hover:border-neutral-600 transition">
              🗣️ MC & Pranata Adat
            </button>
            <button onclick="setCategory('sound')" id="cat-sound" class="cat-pill px-3.5 py-1.5 rounded-full border border-neutral-800 bg-neutral-900 text-neutral-300 text-xs font-semibold whitespace-nowrap hover:border-neutral-600 transition">
              🔊 Sound System & Lighting
            </button>"""

if old_pills in html:
    html = html.replace(old_pills, new_pills)
    print("Updated category pills to include MC and Sound!")

# 5. Add selectQuickCategory and updateQuickNavHighlight functions in JS
js_functions = """
    // SELECT QUICK CATEGORY (PINDAH MENU LANGSUNG 1 KLIK)
    function selectQuickCategory(target) {
      if (currentAppMode === 'vendor') {
        toggleAppMode();
      }

      if (target === 'budget') {
        switchTab('budget');
        updateQuickNavHighlight('budget');
        window.scrollTo({ top: 0, behavior: 'smooth' });
        return;
      }

      // Pastikan ada di tab home
      switchTab('home');

      // Terapkan filter kategori
      setCategory(target);

      // Scroll halus langsung ke daftar vendor
      const section = document.getElementById('vendorListSection');
      if (section) {
        section.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }
    }

    function updateQuickNavHighlight(cat) {
      document.querySelectorAll('.quick-nav-box').forEach(box => {
        box.classList.remove('ring-2', 'ring-white', 'scale-105', 'shadow-lg');
      });
      const targetBox = document.getElementById(`qnav-box-${cat}`);
      if (targetBox) {
        targetBox.classList.add('ring-2', 'ring-white', 'scale-105', 'shadow-lg');
      }
    }
"""

# Insert js_functions right before function setCategory
html = html.replace('function setCategory(cat) {', js_functions + '\n    function setCategory(cat) {')

# Also inside setCategory, call updateQuickNavHighlight(cat)
old_set_cat = """function setCategory(cat) {
      currentCategory = cat;
      document.querySelectorAll('.cat-pill').forEach(btn => {
        btn.classList.remove('bg-white', 'text-black', 'active');
        btn.classList.add('bg-neutral-900', 'text-neutral-300', 'border-neutral-800');
      });
      const target = document.getElementById(`cat-${cat}`);
      if (target) {
        target.classList.remove('bg-neutral-900', 'text-neutral-300', 'border-neutral-800');
        target.classList.add('bg-white', 'text-black', 'active');
      }
      filterVendors();
    }"""

new_set_cat = """function setCategory(cat) {
      currentCategory = cat;
      document.querySelectorAll('.cat-pill').forEach(btn => {
        btn.classList.remove('bg-white', 'text-black', 'active');
        btn.classList.add('bg-neutral-900', 'text-neutral-300', 'border-neutral-800');
      });
      const target = document.getElementById(`cat-${cat}`);
      if (target) {
        target.classList.remove('bg-neutral-900', 'text-neutral-300', 'border-neutral-800');
        target.classList.add('bg-white', 'text-black', 'active');
      }
      updateQuickNavHighlight(cat);
      filterVendors();
    }"""

if old_set_cat in html:
    html = html.replace(old_set_cat, new_set_cat)
    print("Updated setCategory with updateQuickNavHighlight call!")

# Also inside toggleAppMode, hide/show clientQuickMenu
html = html.replace(
    "document.getElementById('clientSearchBar').classList.add('hidden');",
    "document.getElementById('clientSearchBar').classList.add('hidden');\n        document.getElementById('clientQuickMenu')?.classList.add('hidden');"
)
html = html.replace(
    "document.getElementById('clientSearchBar').classList.remove('hidden');",
    "document.getElementById('clientSearchBar').classList.remove('hidden');\n        document.getElementById('clientQuickMenu')?.classList.remove('hidden');"
)

# Save updated index.html
with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Successfully written updated index.html!")
