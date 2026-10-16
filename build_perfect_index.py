# -*- coding: utf-8 -*-

html_content = '''<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>KITA MENIKAH — The Curated Wedding Marketplace</title>
  <script src="https://www.gstatic.com/antigravity/web/dev/tailwindcss.min.js"></script>
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,600;0,700;1,400&family=Plus+Jakarta+Sans:wght@300;400;500;600;700&display=swap');
    
    .font-serif-luxury {
      font-family: 'Cormorant Garamond', Georgia, serif;
    }
    .font-sans-clean {
      font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
    }
    .no-scrollbar::-webkit-scrollbar {
      display: none;
    }
    .no-scrollbar {
      -ms-overflow-style: none;
      scrollbar-width: none;
    }
  </style>
</head>
<body class="bg-neutral-950 text-neutral-100 font-sans-clean min-h-screen flex items-center justify-center p-0 md:p-6 antialiased select-none">

  <!-- Outer Device Mockup Container -->
  <div class="relative w-full max-w-md h-screen md:h-[900px] bg-black md:rounded-[48px] shadow-2xl border-0 md:border-[10px] md:border-neutral-900 overflow-hidden flex flex-col">
    
    <!-- iPhone Top Dynamic Island -->
    <div class="absolute top-0 left-0 right-0 z-50 flex justify-between items-center px-7 pt-3 pb-2 bg-gradient-to-b from-black via-black/85 to-transparent">
      <span class="text-xs font-semibold tracking-wider text-neutral-400 font-mono">09:41</span>
      <div class="w-24 h-4 bg-neutral-900 rounded-full border border-neutral-800"></div>
      <div class="flex items-center space-x-1.5 text-neutral-400 text-xs">
        <svg class="w-3.5 h-3.5" fill="currentColor" viewBox="0 0 24 24"><path d="M12 3c-4.97 0-9 4.03-9 9 0 2.12.74 4.07 1.97 5.61L4.35 19.4c-.39.39-.39 1.02 0 1.41.39.39 1.02.39 1.41 0l1.9-1.9C9.28 19.68 10.59 20 12 20c4.97 0 9-4.03 9-9s-4.03-9-9-9zm0 15c-3.31 0-6-2.69-6-6s2.69-6 6-6 6 2.69 6 6-2.69 6-6 6z"/></svg>
        <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 24 24"><path d="M15.67 4H14V2h-4v2H8.33C7.6 4 7 4.6 7 5.33v15.33C7 21.4 7.6 22 8.33 22h7.33c.74 0 1.34-.6 1.34-1.33V5.33C17 4.6 16.4 4 15.67 4z"/></svg>
      </div>
    </div>

    <!-- MAIN APP SCREEN WRAPPER -->
    <div id="appContainer" class="flex-1 overflow-y-auto no-scrollbar pt-12 pb-20 bg-black">
      
      <!-- TOP STICKY HEADER (CLEAN & ELEGANT MONOCHROMATIC LOGO) -->
      <header class="px-5 pt-3 pb-3 border-b border-neutral-900 bg-black/95 backdrop-blur sticky top-0 z-40 space-y-3">
        <!-- LOGO UTAMA ELEGAN (PASTI 1 BARIS, TIDAK TURUN ATAU PATAH) -->
        <div class="text-center pt-1 pb-0.5">
          <span class="text-[9px] tracking-[0.3em] text-neutral-400 uppercase font-medium block">The Curated Wedding Marketplace</span>
          <h1 class="text-xl tracking-[0.22em] font-serif-luxury uppercase font-bold text-white mt-1 whitespace-nowrap">
            K I T A &nbsp; M E N I K A H
          </h1>
        </div>

        <!-- SEARCH BAR -->
        <div class="relative">
          <svg class="w-4 h-4 text-neutral-500 absolute left-3 top-2.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"/></svg>
          <input type="text" id="searchInput" oninput="filterVendors()" placeholder="Cari Jawara, Sandi Liems, Lux Visual, Nijo, Neiscala..." class="w-full bg-neutral-900 border border-neutral-800 rounded-xl pl-9 pr-4 py-2 text-xs text-white placeholder-neutral-500 focus:outline-none focus:border-white transition">
        </div>

        <!-- LOKASI & PILIHAN KOTA (SIMPEL & BERSIH) -->
        <div class="flex items-center space-x-2 bg-neutral-900 rounded-xl px-3 py-2 border border-neutral-800 text-xs">
          <svg class="w-4 h-4 text-neutral-400 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"/><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"/></svg>
          <select id="cityFilter" onchange="filterVendors()" class="bg-transparent text-white font-medium focus:outline-none cursor-pointer flex-1 text-xs">
            <option value="yogyakarta" selected class="bg-neutral-900 text-white">📍 DI Yogyakarta</option>
            <option value="all" class="bg-neutral-900 text-white">Semua Jawa</option>
            <option value="jakarta" class="bg-neutral-900 text-white">DKI Jakarta</option>
            <option value="bandung" class="bg-neutral-900 text-white">Bandung</option>
            <option value="surabaya" class="bg-neutral-900 text-white">Surabaya</option>
          </select>
        </div>
      </header>

      <!-- CONTENT: HOME VIEW (EKSPLOR) -->
      <div id="viewHome" class="space-y-4">

        <!-- CATEGORIES SLIDER -->
        <div class="px-5 pt-2">
          <div class="flex items-center justify-between mb-2">
            <h2 class="text-xs tracking-[0.2em] uppercase font-bold text-neutral-300">Kategori</h2>
            <span class="text-[10px] text-neutral-400">Geser →</span>
          </div>
          <div class="flex space-x-2 overflow-x-auto no-scrollbar pb-1">
            <button onclick="setCategory('all')" id="cat-all" class="cat-pill active px-3.5 py-1.5 rounded-full border border-white bg-white text-black text-xs font-semibold whitespace-nowrap transition">
              Semua Vendor
            </button>
            <button onclick="setCategory('photography')" id="cat-photography" class="cat-pill px-3.5 py-1.5 rounded-full border border-neutral-800 bg-neutral-900 text-neutral-300 text-xs font-semibold whitespace-nowrap hover:border-neutral-600 transition">
              📸 Fotografer (FG Teman & Top Jogja)
            </button>
            <button onclick="setCategory('mua')" id="cat-mua" class="cat-pill px-3.5 py-1.5 rounded-full border border-neutral-800 bg-neutral-900 text-neutral-300 text-xs font-semibold whitespace-nowrap hover:border-neutral-600 transition">
              💄 MUA & Paes Ageng
            </button>
            <button onclick="setCategory('venue')" id="cat-venue" class="cat-pill px-3.5 py-1.5 rounded-full border border-neutral-800 bg-neutral-900 text-neutral-300 text-xs font-semibold whitespace-nowrap hover:border-neutral-600 transition">
              🏛️ Venue Pernikahan
            </button>
            <button onclick="setCategory('decoration')" id="cat-decoration" class="cat-pill px-3.5 py-1.5 rounded-full border border-neutral-800 bg-neutral-900 text-neutral-300 text-xs font-semibold whitespace-nowrap hover:border-neutral-600 transition">
              🌸 Dekorasi
            </button>
            <button onclick="setCategory('catering')" id="cat-catering" class="cat-pill px-3.5 py-1.5 rounded-full border border-neutral-800 bg-neutral-900 text-neutral-300 text-xs font-semibold whitespace-nowrap hover:border-neutral-600 transition">
              🍽️ Catering
            </button>
            <button onclick="setCategory('wo')" id="cat-wo" class="cat-pill px-3.5 py-1.5 rounded-full border border-neutral-800 bg-neutral-900 text-neutral-300 text-xs font-semibold whitespace-nowrap hover:border-neutral-600 transition">
              📋 Wedding Organizer
            </button>
          </div>
        </div>

        <!-- STYLE CHIPS -->
        <div class="px-5">
          <div class="flex items-center space-x-2 overflow-x-auto no-scrollbar py-1 text-xs">
            <span class="text-[10px] text-neutral-500 uppercase tracking-wider font-semibold shrink-0">Konsep:</span>
            <button onclick="setStyleFilter('all')" id="style-all" class="style-chip active px-3 py-1 rounded-full border border-white text-white bg-white/10 text-[11px] whitespace-nowrap">Semua</button>
            <button onclick="setStyleFilter('Tradisional Jawa')" id="style-jawa" class="style-chip px-3 py-1 rounded-full border border-neutral-800 text-neutral-400 text-[11px] whitespace-nowrap hover:border-neutral-600">🏛️ Pakem Jawa Paes Ageng</button>
            <button onclick="setStyleFilter('Warm Editorial')" id="style-warm" class="style-chip px-3 py-1 rounded-full border border-neutral-800 text-neutral-400 text-[11px] whitespace-nowrap hover:border-neutral-600">🎞️ Warm Editorial & Candid</button>
            <button onclick="setStyleFilter('Outdoor Garden')" id="style-outdoor" class="style-chip px-3 py-1 rounded-full border border-neutral-800 text-neutral-400 text-[11px] whitespace-nowrap hover:border-neutral-600">🌿 Outdoor / Kaliurang</button>
            <button onclick="setStyleFilter('Modern Minimalist')" id="style-modern" class="style-chip px-3 py-1 rounded-full border border-neutral-800 text-neutral-400 text-[11px] whitespace-nowrap hover:border-neutral-600">✨ Modern Intimate</button>
          </div>
        </div>

        <!-- VENDORS LIST -->
        <div class="px-5">
          <div class="flex justify-between items-center mb-3">
            <div>
              <h2 class="text-xs tracking-[0.2em] uppercase font-bold text-neutral-300">Daftar Terkurasi</h2>
              <p class="text-[10px] text-neutral-500 font-mono">Geser slide kartu untuk melihat hasil foto asli</p>
            </div>
            <span id="vendorCount" class="text-xs text-neutral-400 font-mono">Memuat...</span>
          </div>

          <div id="vendorList" class="space-y-4">
            <!-- Dynamic Vendor Cards with Slides injected by JS -->
          </div>
        </div>
      </div>

      <!-- CONTENT: BUDGET PLANNER TAB -->
      <div id="viewBudget" class="hidden px-5 py-4 space-y-6">
        <div>
          <span class="text-[10px] tracking-widest uppercase text-neutral-400">Fitur Pintar</span>
          <h2 class="text-xl font-serif-luxury font-bold text-white tracking-wide">Kalkulator Estimasi Anggaran</h2>
          <p class="text-xs text-neutral-400 mt-1">Kalkulasi pembagian anggaran ideal pernikahanmu di Jogja.</p>
        </div>

        <div class="bg-neutral-900 border border-neutral-800 rounded-2xl p-4 space-y-4">
          <div>
            <label class="text-xs text-neutral-300 font-medium block mb-1.5">Total Target Budget (Rp)</label>
            <input type="number" id="budgetInput" value="100000000" step="5000000" class="w-full bg-black border border-neutral-700 rounded-xl px-3.5 py-2.5 text-sm text-white font-mono focus:outline-none focus:border-white">
          </div>
          <div>
            <label class="text-xs text-neutral-300 font-medium block mb-1.5">Estimasi Jumlah Tamu Undangan</label>
            <select id="guestCount" class="w-full bg-black border border-neutral-700 rounded-xl px-3.5 py-2.5 text-xs text-white focus:outline-none focus:border-white">
              <option value="200">Intimate Wedding (150 - 250 Tamu)</option>
              <option value="400" selected>Medium Wedding (300 - 500 Tamu)</option>
              <option value="800">Grand Wedding (600 - 1000 Tamu)</option>
            </select>
          </div>
          <button onclick="calculateBudget()" class="w-full bg-white text-black text-xs font-bold py-2.5 rounded-xl uppercase tracking-wider hover:bg-neutral-200 active:scale-95 transition">
            Hitung Rincian Alokasi
          </button>
        </div>

        <div id="budgetResult" class="space-y-2.5 bg-neutral-900/60 border border-neutral-800 rounded-2xl p-4">
          <!-- Populated by JS -->
        </div>
      </div>

      <!-- CONTENT: SAVED VENDORS TAB -->
      <div id="viewSaved" class="hidden px-5 py-4 space-y-4">
        <div>
          <span class="text-[10px] tracking-widest uppercase text-neutral-400">Favorit Pasangan</span>
          <h2 class="text-xl font-serif-luxury font-bold text-white tracking-wide">Vendor Disimpan</h2>
        </div>
        <div id="savedList" class="space-y-3">
          <!-- Injected by JS -->
        </div>
      </div>

    </div>

    <!-- BOTTOM APP NAVIGATION DOCK (BERSIH 3 MENU: EKSPLOR, BUDGET, TERSIMPAN) -->
    <nav class="absolute bottom-0 left-0 right-0 h-16 bg-black/95 backdrop-blur border-t border-neutral-900 flex justify-around items-center px-6 z-40">
      <button onclick="switchTab('home')" id="navHome" class="flex flex-col items-center justify-center space-y-1 text-white">
        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6"/></svg>
        <span class="text-[10px] font-semibold tracking-wider">Eksplor</span>
      </button>

      <button onclick="switchTab('budget')" id="navBudget" class="flex flex-col items-center justify-center space-y-1 text-neutral-500 hover:text-white transition">
        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 7h6m0 10v-3m-3 3h.01M9 17h.01M9 14h.01M12 14h.01M15 11h.01M12 11h.01M9 11h.01M7 21h10a2 2 0 002-2V5a2 2 0 00-2-2H7a2 2 0 00-2 2v14a2 2 0 002 2z"/></svg>
        <span class="text-[10px] font-semibold tracking-wider">Budget</span>
      </button>

      <button onclick="switchTab('saved')" id="navSaved" class="flex flex-col items-center justify-center space-y-1 text-neutral-500 hover:text-white transition">
        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z"/></svg>
        <span class="text-[10px] font-semibold tracking-wider">Tersimpan</span>
      </button>
    </nav>

    <!-- VENDOR DETAIL & PREVIEW MODAL -->
    <div id="vendorModal" class="hidden absolute inset-0 z-50 bg-black/95 backdrop-blur-md flex flex-col justify-end transition-all">
      <div class="bg-neutral-950 border-t border-neutral-800 rounded-t-3xl max-h-[92%] flex flex-col overflow-hidden">
        
        <!-- Modal Drag Handle & Close -->
        <div class="px-5 pt-3 pb-2 flex justify-between items-center border-b border-neutral-900">
          <div class="w-12 h-1 bg-neutral-800 rounded-full mx-auto"></div>
          <button onclick="closeVendorModal()" class="w-7 h-7 rounded-full bg-neutral-900 text-neutral-400 flex items-center justify-center text-xs hover:text-white">✕</button>
        </div>

        <div id="modalContent" class="p-5 overflow-y-auto no-scrollbar space-y-5 flex-1">
          <!-- Injected by JS -->
        </div>

        <!-- Floating CTA at bottom of Modal -->
        <div class="p-4 bg-neutral-900/95 backdrop-blur border-t border-neutral-800 flex space-x-2.5">
          <button id="modalIgBtn" onclick="openInstagram()" class="flex-1 bg-neutral-800 hover:bg-neutral-700 border border-neutral-700 text-white text-xs font-bold py-3 rounded-xl flex items-center justify-center space-x-2 transition shadow">
            <svg class="w-4 h-4 text-white" fill="currentColor" viewBox="0 0 24 24"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z"/></svg>
            <span>Buka di Instagram</span>
          </button>
          <button id="modalWaBtn" onclick="openWhatsAppFormatted()" class="flex-1 bg-white text-black text-xs font-bold py-3 rounded-xl flex items-center justify-center space-x-2 hover:bg-neutral-200 active:scale-95 transition">
            <svg class="w-4 h-4 text-emerald-600" fill="currentColor" viewBox="0 0 24 24"><path d="M.057 24l1.687-6.163c-1.041-1.804-1.588-3.849-1.587-5.946.003-6.556 5.338-11.891 11.893-11.891 3.181.001 6.167 1.24 8.413 3.488 2.245 2.248 3.481 5.236 3.48 8.414-.003 6.557-5.338 11.892-11.893 11.892-1.99-.001-3.951-.5-5.688-1.448l-6.305 1.654zm6.597-3.807c1.676.995 3.276 1.591 5.392 1.592 5.448 0 9.886-4.434 9.889-9.885.002-5.462-4.415-9.89-9.881-9.892-5.452 0-9.887 4.434-9.889 9.884-.001 2.225.651 3.891 1.746 5.634l-.999 3.648 3.742-.981zm11.387-5.464c-.074-.124-.272-.198-.57-.347-.297-.149-1.758-.868-2.031-.967-.272-.099-.47-.149-.669.149-.198.297-.768.967-.941 1.165-.173.198-.347.223-.644.074-.297-.149-1.255-.462-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.297-.347.446-.521.151-.172.2-.296.3-.495.099-.198.05-.372-.025-.521-.075-.148-.669-1.611-.916-2.206-.242-.579-.487-.501-.669-.51l-.57-.01c-.198 0-.52.074-.792.372s-1.04 1.016-1.04 2.479 1.065 2.876 1.213 3.074c.149.198 2.095 3.2 5.076 4.487.709.306 1.263.489 1.694.626.712.226 1.36.194 1.872.118.571-.085 1.758-.719 2.006-1.413.248-.695.248-1.29.173-1.414z"/></svg>
            <span>Tanya Jadwal di WA</span>
          </button>
        </div>

      </div>
    </div>

  </div>

  <script>
    // DATA VENDOR LENGKAP DENGAN FOTO PROFIL IG ASLI & FOTO SLIDE KARYA NYATA
    const vendors = [
      // 1. JAWARA PHOTO (Mulai Rp 3.800.000)
      {
        id: 'fg-jawara',
        name: 'Jawara Photo',
        category: 'photography',
        city: 'yogyakarta',
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
        avatar: 'assets/vendors/avatars/jawara.jpg',
        phone: '628123456001',
        description: 'Vendor dokumentasi foto & video pernikahan berbasis di Yogyakarta dengan tagar khas #bersamajawara. Menghadirkan dokumentasi emosional, hangat, dan abadi (*timeless candid*).',
        slideIndex: 0,
        slides: [
          {
            image: 'assets/vendors/slides/jawara_slide_1.jpg',
            tag: '🔥 PALING BANYAK LIKE DI IG',
            likes: '4.820 likes',
            caption: 'Some souls meet once and change each other forever. From The Wedding Prima & Fauzan @amaliaprimaa & @fb_santoso 🤍'
          },
          {
            image: 'assets/vendors/slides/jawara_slide_2.jpg',
            tag: '✨ TRADISIONAL PAES JOGJA',
            likes: '3.690 likes',
            caption: 'The Wedding @maretafwa & @knrw_wsnv 🤍 MUA: @scratchby.mwulandey #weddingjogja #bersamajawara'
          },
          {
            image: 'assets/vendors/slides/jawara_slide_3.jpg',
            tag: '🌿 INTIMATE STORYTELLING',
            likes: '2.840 likes',
            caption: 'From The Wedding Sisil & Dhimas. Detil kehangatan keluarga tanpa rekayasa #jawaraphoto'
          }
        ],
        packages: [
          { name: 'Paket Intimate Akad Only (1 FG + 1 VG)', price: 'Rp 3.800.000' },
          { name: 'Full Day Wedding Documentation + Cinematic Teaser', price: 'Rp 6.500.000' },
          { name: 'All-In Prewedding + Wedding Day + Exclusive Album Box', price: 'Rp 9.800.000' }
        ]
      },

      // 2. SANDI LIEMS (Mulai Rp 4.500.000)
      {
        id: 'fg-sandiliem',
        name: 'Sandi Liems Photography',
        category: 'photography',
        city: 'yogyakarta',
        styleTag: 'Modern Minimalist',
        locationText: 'Kota Yogyakarta, DI Yogyakarta',
        priceStart: 4500000,
        rating: 4.9,
        reviewCount: 112,
        isPromoted: true,
        promoTier: 'FEATURED',
        igHandle: '@sandi.liem',
        igFollowers: '5.820 followers',
        igPostsCount: '240 posts',
        igUrl: 'https://www.instagram.com/sandi.liem/',
        avatar: 'assets/vendors/avatars/sandiliem.jpg',
        phone: '628123456002',
        description: 'Fotografer pernikahan spesialis editorial couple portraits dan intimate wedding storytelling di Jogja.',
        slideIndex: 0,
        slides: [
          {
            image: 'assets/vendors/slides/sandiliem_slide_1.jpg',
            tag: '🔥 PALING BANYAK LIKE DI IG',
            likes: '5.210 likes',
            caption: 'The quiet beauty of two souls becoming one. Editorial bridal portraiture for our lovely couple in Yogyakarta. Captured #bysandiliem 🤍'
          },
          {
            image: 'assets/vendors/slides/sandiliem_slide_2.jpg',
            tag: '🎞️ EDITORIAL PORTRAIT',
            likes: '3.880 likes',
            caption: 'Timeless monochrome emotions. When words are unspoken, eyes convey eternity #sandiliemphotography'
          },
          {
            image: 'assets/vendors/slides/sandiliem_slide_3.jpg',
            tag: '✨ INTIMATE SUNSET',
            likes: '2.940 likes',
            caption: 'Gentle warmth embracing their eternal journey of devotion #bysandiliem'
          }
        ],
        packages: [
          { name: 'Intimate Couple Session / Prewedding', price: 'Rp 4.500.000' },
          { name: 'Full Day Wedding Coverage & Framed Canvas', price: 'Rp 8.000.000' }
        ]
      },

      // 3. LUX VISUAL (Mulai Rp 2.000.000)
      {
        id: 'fg-luxvisual',
        name: 'Lux Visual',
        category: 'photography',
        city: 'yogyakarta',
        styleTag: 'Warm Editorial',
        locationText: 'Bantul, DI Yogyakarta',
        priceStart: 2000000,
        rating: 4.9,
        reviewCount: 98,
        isPromoted: true,
        promoTier: 'FEATURED',
        igHandle: '@luxvisual.id',
        igFollowers: '4.100 followers',
        igPostsCount: '150 posts',
        igUrl: 'https://www.instagram.com/luxvisual.id/',
        avatar: 'assets/vendors/avatars/luxvisual.jpg',
        phone: '628123456003',
        description: 'Kreator visual pernikahan di Yogyakarta yang menyuguhkan karya foto dan video cinematic dengan tone warna hangat bersahabat.',
        slideIndex: 0,
        slides: [
          {
            image: 'assets/vendors/slides/luxvisual_slide_1.jpg',
            tag: '🔥 PALING BANYAK LIKE DI IG',
            likes: '3.920 likes',
            caption: 'Engagement kak Ira & Eko di Bantul. Dokumentasi kehangatan momen lamaran sakral @luxvisual.id 💍'
          },
          {
            image: 'assets/vendors/slides/luxvisual_slide_2.jpg',
            tag: '✨ CINEMATIC MOMENT',
            likes: '2.740 likes',
            caption: 'Senyum hangat dan tulus di hari akad nikah yang syahdu #luxvisual #weddingjogja'
          },
          {
            image: 'assets/vendors/slides/luxvisual_slide_3.jpg',
            tag: '🌸 INTIMATE ENGAGEMENT',
            likes: '2.150 likes',
            caption: 'Detil dekorasi dan tatapan penuh cinta di awal kisah baru'
          }
        ],
        packages: [
          { name: 'Paket Lamaran / Engagement Documentation', price: 'Rp 2.000.000' },
          { name: 'Akad Nikah Only Coverage (Foto + Reels)', price: 'Rp 3.500.000' }
        ]
      },

      // 4. KITAKANCERITA (Mulai Rp 5.000.000)
      {
        id: 'fg-kitakancerita',
        name: 'Kitakancerita',
        category: 'photography',
        city: 'yogyakarta',
        styleTag: 'Tradisional Jawa',
        locationText: 'Sleman, DI Yogyakarta',
        priceStart: 5000000,
        rating: 4.9,
        reviewCount: 130,
        isPromoted: true,
        promoTier: 'SPOTLIGHT',
        igHandle: '@kitakancerita',
        igFollowers: '6.750 followers',
        igPostsCount: '310 posts',
        igUrl: 'https://www.instagram.com/kitakancerita/',
        avatar: 'assets/vendors/avatars/kitakancerita.jpg',
        phone: '628123456004',
        description: '"Menceritakan kisah cinta kalian melalui bingkai visual yang jujur." Ahli dalam mengabadikan prosesi adat Jawa dan intimate modern wedding.',
        slideIndex: 0,
        slides: [
          {
            image: 'assets/vendors/slides/kitakancerita_slide_1.jpg',
            tag: '🔥 PALING BANYAK LIKE DI IG',
            likes: '6.450 likes',
            caption: 'Air mata haru restu orang tua saat prosesi sungkeman siraman adat Jawa @kitakancerita 🌿'
          },
          {
            image: 'assets/vendors/slides/kitakancerita_slide_2.jpg',
            tag: '👑 PAES AGENG JOGJA',
            likes: '4.910 likes',
            caption: 'Kidung doa mengalun pelan menyambut panggih temanten Jawa di pendopo agung #kitakancerita'
          },
          {
            image: 'assets/vendors/slides/kitakancerita_slide_3.jpg',
            tag: '🤍 SAKRALNYA AKAD',
            likes: '3.820 likes',
            caption: 'Dua insan yang mengikat janji seumur hidup di hadapan Sang Maha Kuasa'
          }
        ],
        packages: [
          { name: 'Akad / Pemberkatan Only (Full Documentation)', price: 'Rp 5.000.000' },
          { name: 'Full Day Wedding Story: 2 FG + 2 VG + Teaser 1 Min', price: 'Rp 8.500.000' }
        ]
      },

      // 5. THE NIJO PHOTOGRAPH (Mulai Rp 5.000.000)
      {
        id: 'fg-nijo',
        name: 'The Nijo Photograph',
        category: 'photography',
        city: 'yogyakarta',
        styleTag: 'Modern Minimalist',
        locationText: 'Yogyakarta & Solo',
        priceStart: 5000000,
        rating: 4.8,
        reviewCount: 89,
        isPromoted: false,
        promoTier: 'STANDARD',
        igHandle: '@thenijophotograph',
        igFollowers: '4.890 followers',
        igPostsCount: '190 posts',
        igUrl: 'https://www.instagram.com/thenijophotograph/',
        avatar: 'assets/vendors/avatars/nijo.jpg',
        phone: '628123456005',
        description: 'Tim fotografer muda kreatif berbasis di Jogja-Solo dengan visual aesthetic segar, ceria, dan sangat ramah.',
        slideIndex: 0,
        slides: [
          {
            image: 'assets/vendors/slides/nijo_slide_2.jpg',
            tag: '🔥 PALING BANYAK LIKE DI IG',
            likes: '4.180 likes',
            caption: 'Tawa renyah dan pelukan hangat para sahabat di hari pernikahan paling dinanti. Captured with love by @thenijophotograph 💛'
          },
          {
            image: 'assets/vendors/slides/nijo_slide_3.jpg',
            tag: '🌿 SUNSET INTIMATE',
            likes: '3.250 likes',
            caption: 'Golden hour embrace under the open sky of Yogyakarta #thenijophotograph'
          },
          {
            image: 'assets/vendors/slides/nijo_slide_1.jpg',
            tag: '✨ JOYFUL CANDID',
            likes: '2.680 likes',
            caption: 'Senyum lepas dan kebahagiaan yang menular di setiap sudut pesta'
          }
        ],
        packages: [
          { name: 'Intimate Wedding Documentation', price: 'Rp 5.000.000' },
          { name: 'Wedding Day Cinematic Photo & Video', price: 'Rp 7.800.000' }
        ]
      },

      // 6. NEISCALA (Mulai Rp 7.000.000)
      {
        id: 'fg-neiscala',
        name: 'Neiscala',
        category: 'photography',
        city: 'yogyakarta',
        styleTag: 'Modern Minimalist',
        locationText: 'Kota Yogyakarta, DI Yogyakarta',
        priceStart: 7000000,
        rating: 5.0,
        reviewCount: 94,
        isPromoted: true,
        promoTier: 'FEATURED',
        igHandle: '@neiscala',
        igFollowers: '7.120 followers',
        igPostsCount: '210 posts',
        igUrl: 'https://www.instagram.com/neiscala/',
        avatar: 'assets/vendors/avatars/neiscala.jpg',
        phone: '628123456006',
        description: 'Spesialis wedding photography and cinematic film bernuansa romantis, anggun, dengan pencahayaan alami nan memukau.',
        slideIndex: 0,
        slides: [
          {
            image: 'assets/vendors/slides/neiscala_slide_1.jpg',
            tag: '🔥 PALING BANYAK LIKE DI IG',
            likes: '7.340 likes',
            caption: 'In the stillness of the ballroom, their promises echoed forever. A cinematic glimpse of love by @neiscala ✨'
          },
          {
            image: 'assets/vendors/slides/neiscala_slide_3.jpg',
            tag: '🎞️ ROMANTIC CINEMATIC',
            likes: '5.620 likes',
            caption: 'Whispering sweet melodies of love amidst the pine trees of Kaliurang #neiscala'
          },
          {
            image: 'assets/vendors/slides/neiscala_slide_2.jpg',
            tag: '🤍 TIMELESS BRIDAL',
            likes: '4.110 likes',
            caption: 'Keanggunan gaun pengantin berpadu cahaya sore yang memukau'
          }
        ],
        packages: [
          { name: 'The Romantic Day (Photo & Cinematic Reel)', price: 'Rp 7.000.000' },
          { name: 'Grand Wedding All-In (Drone + 2 Album Cetak Mewah)', price: 'Rp 12.000.000' }
        ]
      },

      // 7. LUNA NOUVA STUDIO (Mulai Rp 4.000.000)
      {
        id: 'fg-lunanouva',
        name: 'Luna Nouva Studio',
        category: 'photography',
        city: 'yogyakarta',
        styleTag: 'Tradisional Jawa',
        locationText: 'Ringinharjo, Bantul, DI Yogyakarta',
        priceStart: 4000000,
        rating: 4.8,
        reviewCount: 76,
        isPromoted: false,
        promoTier: 'STANDARD',
        igHandle: '@lunanouovastudio__',
        igFollowers: '3.980 followers',
        igPostsCount: '185 posts',
        igUrl: 'https://www.instagram.com/lunanouovastudio__/',
        avatar: 'assets/vendors/avatars/lunanouva.jpg',
        phone: '628123456007',
        description: 'Studio foto dan film pernikahan di Bantul. Menyediakan paket komplit foto studio, prewedding outdoor, liputan hari H, serta kolaborasi MUA & dekorasi.',
        slideIndex: 0,
        slides: [
          {
            image: 'assets/vendors/slides/lunanouva_slide_1.jpg',
            tag: '🔥 PALING BANYAK LIKE DI IG',
            likes: '3.620 likes',
            caption: 'Prewedding magis berlatar bentang pasir Gumuk Pasir Parangkusumo Bantul Yogyakarta @lunanouovastudio__ 🌾'
          },
          {
            image: 'assets/vendors/slides/lunanouva_slide_3.jpg',
            tag: '✨ STUDIO MINIMALIST',
            likes: '2.890 likes',
            caption: 'Warm studio portraiture with natural light elegance #lunanouovastudio'
          },
          {
            image: 'assets/vendors/slides/lunanouva_slide_2.jpg',
            tag: '🌾 OUTDOOR STORY',
            likes: '2.140 likes',
            caption: 'Momen hening menatap ombak laut selatan bersama belahan jiwa'
          }
        ],
        packages: [
          { name: 'Paket Liputan Akad & Resepsi Bantul', price: 'Rp 4.000.000' },
          { name: 'Prewedding Studio + Outdoor Gumuk Pasir', price: 'Rp 2.800.000' }
        ]
      },

      // 8. MAMUK TUKANG MAKEUP JOGJA (MUA TOP JOGJA)
      {
        id: 'mua-mamuk',
        name: 'Mamuk Tukang Makeup Jogja',
        category: 'mua',
        city: 'yogyakarta',
        styleTag: 'Tradisional Jawa',
        locationText: 'Kraton, Kota Yogyakarta',
        priceStart: 9500000,
        rating: 5.0,
        reviewCount: 280,
        isPromoted: true,
        promoTier: 'SPOTLIGHT',
        igHandle: '@mamuktukangmakeupjogja',
        igFollowers: '52.400 followers',
        igPostsCount: '1.200 posts',
        igUrl: 'https://www.instagram.com/mamuktukangmakeupjogja/',
        avatar: 'assets/vendors/avatars/mamuk.jpg',
        phone: '628123456010',
        description: 'Maestro tata rias pengantin adat Jawa paling disegani di Jogja. Sangat presisi dalam pakem cengkorongan Paes Ageng, Kanigaran, dan Jangan Menir.',
        slideIndex: 0,
        slides: [
          {
            image: 'assets/vendors/slides/mamuk_slide_2.jpg',
            tag: '👑 MAESTRO PAES AGENG',
            likes: '18.300 likes',
            caption: 'Mahakarya Paes Ageng Kraton Ngayogyakarta Hadiningrat dengan lekukan cengkorongan prada emas asli keraton @mamuktukangmakeupjogja 👑'
          },
          {
            image: 'assets/vendors/slides/mamuk_slide_3.jpg',
            tag: '✨ KANIGARAN KLASIK',
            likes: '14.200 likes',
            caption: 'Busana beludru hitam bersulam benang emas dengan tata rias paes keraton yang agung'
          }
        ],
        packages: [
          { name: 'Paes Ageng Jangan Menir Komplit + Busana Adat', price: 'Rp 14.000.000' },
          { name: 'Rias Pengantin Jogja Putri Modifikasi', price: 'Rp 9.500.000' }
        ]
      },

      // 9. PENDOPO AGUNG ROYAL AMBARRUKMO (VENUE)
      {
        id: 'venue-ambarrukmo',
        name: 'Pendopo Agung Royal Ambarrukmo',
        category: 'venue',
        city: 'yogyakarta',
        styleTag: 'Tradisional Jawa',
        locationText: 'Depok, Sleman, DI Yogyakarta',
        priceStart: 85000000,
        rating: 5.0,
        reviewCount: 155,
        isPromoted: true,
        promoTier: 'SPOTLIGHT',
        igHandle: '@royalambarrukmo',
        igFollowers: '78.500 followers',
        igPostsCount: '2.400 posts',
        igUrl: 'https://www.instagram.com/royalambarrukmo/',
        avatar: 'assets/vendors/avatars/ambarrukmo.jpg',
        phone: '628123456020',
        description: 'Cagar budaya bersejarah peninggalan Sultan Hamengku Buwono VII. Ikon royal wedding adat Jawa termegah dan tersakral di Indonesia.',
        slideIndex: 0,
        slides: [
          {
            image: 'assets/vendors/slides/ambarrukmo_slide_1.jpg',
            tag: '🏛️ ROYAL HERITAGE VENUE',
            likes: '16.700 likes',
            caption: 'Megahnya pilar kayu jati bersejarah abad ke-18 Pendopo Agung Royal Ambarrukmo. Saksi ikrar janji suci pernikahan agung di Yogyakarta 🏛️'
          }
        ],
        packages: [
          { name: 'Heritage Akad & Paringgitan (150 Pax)', price: 'Rp 85.000.000' },
          { name: 'Royal Grand Pendopo & Taman Gandhok (500 Pax)', price: 'Rp 145.000.000' }
        ]
      },

      // 10. DANANI DECORATION JOGJA (DEKORASI)
      {
        id: 'decor-danani',
        name: 'Danani Decoration Jogja',
        category: 'decoration',
        city: 'yogyakarta',
        styleTag: 'Tradisional Jawa',
        locationText: 'Umbulharjo, Kota Yogyakarta',
        priceStart: 25000000,
        rating: 4.9,
        reviewCount: 92,
        isPromoted: true,
        promoTier: 'FEATURED',
        igHandle: '@dananidecoration',
        igFollowers: '19.200 followers',
        igPostsCount: '480 posts',
        igUrl: 'https://www.instagram.com/dananidecoration/',
        avatar: 'assets/vendors/avatars/danani.jpg',
        phone: '628123456030',
        description: 'Spesialis dekorasi pelaminan gebyok keraton dan instalasi bunga hidup megah di Jogja.',
        slideIndex: 0,
        slides: [
          {
            image: 'assets/vendors/slides/danani_slide_1.jpg',
            tag: '🌸 GEBYOK KRATON FLORAL',
            likes: '6.900 likes',
            caption: 'Kemegahan pelaminan gebyok jati ukir klasik bertabur ribuan kuntum melati segar harum semerbak @dananidecoration 🌸'
          },
          {
            image: 'assets/vendors/slides/danani_slide_3.jpg',
            tag: '✨ MODERN JAVANESE',
            likes: '5.140 likes',
            caption: 'Instalasi lampu gantung kristal berpadu ornamen kayu ukir klasik'
          }
        ],
        packages: [
          { name: 'Pelaminan Gebyok Kraton 8 Meter', price: 'Rp 25.000.000' },
          { name: 'Grand Ballroom Fresh Flower Installation', price: 'Rp 45.000.000' }
        ]
      },

      // 11. VIDI CATERING SERVICES JOGJA (CATERING)
      {
        id: 'catering-vidi',
        name: 'Vidi Catering Services Jogja',
        category: 'catering',
        city: 'yogyakarta',
        styleTag: 'Tradisional Jawa',
        locationText: 'Mlati, Sleman, DI Yogyakarta',
        priceStart: 50000,
        rating: 5.0,
        reviewCount: 420,
        isPromoted: true,
        promoTier: 'SPOTLIGHT',
        igHandle: '@vidicatering',
        igFollowers: '34.800 followers',
        igPostsCount: '890 posts',
        igUrl: 'https://www.instagram.com/vidicatering/',
        avatar: 'assets/vendors/avatars/vidi.jpg',
        phone: '628123456040',
        description: 'Raja katering pernikahan terpercaya di Yogyakarta dengan sertifikasi ISO 22000 dan resep citarasa ningrat Kraton.',
        slideIndex: 0,
        slides: [
          {
            image: 'assets/vendors/slides/vidi_slide_1.jpg',
            tag: '🍽️ CITARASA NINGRAT KRATON',
            likes: '5.600 likes',
            caption: 'Sajian hidangan prasmanan citarasa ningrat Kraton Yogyakarta dengan sertifikasi Halal MUI Grade A @vidicatering 🍽️'
          },
          {
            image: 'assets/vendors/slides/vidi_slide_2.jpg',
            tag: '🍲 PONDOKAN GUBUKAN MEWAH',
            likes: '4.820 likes',
            caption: 'Gubukan tradisional Selat Solo, Zuppa Soup, dan Sate Klathak istimewa'
          }
        ],
        packages: [
          { name: 'Paket Prasmanan Tradisi Jogja (Min 500 Pax)', price: 'Rp 50.000 / pax' },
          { name: 'Paket Ningrat Royal Buffet + 8 Gubukan Khas', price: 'Rp 75.000 / pax' }
        ]
      },

      // 12. MAHKOTA WEDDING ORGANIZER JOGJA (WO)
      {
        id: 'wo-mahkota',
        name: 'Mahkota Wedding Organizer Jogja',
        category: 'wo',
        city: 'yogyakarta',
        styleTag: 'Tradisional Jawa',
        locationText: 'Sleman, DI Yogyakarta',
        priceStart: 15000000,
        rating: 5.0,
        reviewCount: 160,
        isPromoted: true,
        promoTier: 'SPOTLIGHT',
        igHandle: '@mahkota_wo.jogja',
        igFollowers: '27.900 followers',
        igPostsCount: '670 posts',
        igUrl: 'https://www.instagram.com/mahkota_wo.jogja/',
        avatar: 'assets/vendors/avatars/mahkota.jpg',
        phone: '628123456050',
        description: 'Wedding Organizer terkemuka di Yogyakarta spesialis pemandu pakem adat Jawa Paes Ageng dan upacara panggih berwibawa.',
        slideIndex: 0,
        slides: [
          {
            image: 'assets/vendors/slides/mahkota_slide_1.jpg',
            tag: '💍 PROTOKOL ADAT KHIDMAT',
            likes: '7.120 likes',
            caption: 'Ketenangan dan keteraturan jalannya prosesi ijab kabul sakral berkat pengawalan tim handal @mahkota_wo.jogja 💍'
          },
          {
            image: 'assets/vendors/slides/mahkota_slide_3.jpg',
            tag: '✨ PANGGIH KERATON JOGJA',
            likes: '5.890 likes',
            caption: 'Prosesi balangan gantal dan wijidadi dibimbing secara khidmat dan runtut'
          }
        ],
        packages: [
          { name: 'Wedding Day Coordination (6 Crew Full Day)', price: 'Rp 15.000.000' },
          { name: 'Full Planning & Wedding Adat Protocol Assistance', price: 'Rp 25.000.000' }
        ]
      }
    ];

    let currentCategory = 'all';
    let currentStyle = 'all';
    let savedVendorIds = new Set(['fg-jawara', 'fg-sandiliem', 'fg-kitakancerita']);
    let activeVendor = null;

    function formatRupiah(num) {
      return 'Rp ' + num.toLocaleString('id-ID');
    }

    function prevSlide(vendorId, event) {
      if (event) event.stopPropagation();
      const v = vendors.find(x => x.id === vendorId);
      if (!v || !v.slides || v.slides.length <= 1) return;
      v.slideIndex = (v.slideIndex - 1 + v.slides.length) % v.slides.length;
      updateCardSlide(v);
    }

    function nextSlide(vendorId, event) {
      if (event) event.stopPropagation();
      const v = vendors.find(x => x.id === vendorId);
      if (!v || !v.slides || v.slides.length <= 1) return;
      v.slideIndex = (v.slideIndex + 1) % v.slides.length;
      updateCardSlide(v);
    }

    function updateCardSlide(v) {
      const currentSlide = v.slides[v.slideIndex];
      const imgEl = document.getElementById(`slide-img-${v.id}`);
      const tagEl = document.getElementById(`slide-tag-${v.id}`);
      const likesEl = document.getElementById(`slide-likes-${v.id}`);
      const captionEl = document.getElementById(`slide-caption-${v.id}`);
      const dotsEl = document.getElementById(`dots-${v.id}`);

      if (imgEl && currentSlide.image) imgEl.src = currentSlide.image;
      if (tagEl) tagEl.innerText = currentSlide.tag;
      if (likesEl) likesEl.innerText = `❤️ ${currentSlide.likes}`;
      if (captionEl) captionEl.innerText = `"${currentSlide.caption}"`;

      if (dotsEl) {
        dotsEl.innerHTML = v.slides.map((_, idx) => `
          <span class="w-1.5 h-1.5 rounded-full transition ${idx === v.slideIndex ? 'bg-white scale-125' : 'bg-white/40'}"></span>
        `).join('');
      }
    }

    function filterVendors() {
      const city = document.getElementById('cityFilter').value;
      const search = (document.getElementById('searchInput').value || '').toLowerCase().trim();
      const listContainer = document.getElementById('vendorList');
      
      const filtered = vendors.filter(v => {
        const matchCategory = currentCategory === 'all' || v.category === currentCategory;
        const matchCity = city === 'all' || v.city === city;
        const matchStyle = currentStyle === 'all' || v.styleTag === currentStyle;
        const matchSearch = !search || 
          v.name.toLowerCase().includes(search) || 
          v.description.toLowerCase().includes(search) ||
          v.igHandle.toLowerCase().includes(search) ||
          v.locationText.toLowerCase().includes(search) ||
          v.category.toLowerCase().includes(search);

        return matchCategory && matchCity && matchStyle && matchSearch;
      });

      document.getElementById('vendorCount').innerText = `${filtered.length} Vendor Siap`;

      if (filtered.length === 0) {
        listContainer.innerHTML = `
          <div class="text-center py-10 border border-dashed border-neutral-800 rounded-2xl p-6 bg-neutral-900/40">
            <p class="text-neutral-300 font-semibold text-xs">Tidak ditemukan vendor yang cocok.</p>
            <p class="text-neutral-500 text-[11px] mt-1">Coba gunakan kata kunci lain atau reset filter.</p>
            <button onclick="resetAllFilters()" class="mt-3 text-xs bg-white text-black px-3.5 py-1.5 rounded-lg font-bold">Reset Filter</button>
          </div>
        `;
        return;
      }

      listContainer.innerHTML = filtered.map(v => {
        const isSaved = savedVendorIds.has(v.id);
        const priceLabel = v.category === 'catering' ? `${formatRupiah(v.priceStart)} / pax` : formatRupiah(v.priceStart);
        const currentSlide = v.slides[v.slideIndex || 0];

        return `
          <div class="bg-neutral-900 border border-neutral-800 hover:border-neutral-700 rounded-2xl overflow-hidden transition duration-300">
            
            <!-- CARD TOP HEADER: FOTO PROFIL IG ASLI & USERNAME IG -->
            <div class="px-3.5 py-2.5 bg-neutral-950 flex justify-between items-center border-b border-neutral-800/80">
              <div class="flex items-center space-x-2.5">
                <div class="w-9 h-9 rounded-full overflow-hidden border border-neutral-700 bg-neutral-900 shrink-0">
                  <img src="${v.avatar}" alt="${v.name}" class="w-full h-full object-cover" onerror="this.src='https://ui-avatars.com/api/?name=${encodeURIComponent(v.name)}&background=171717&color=ffffff'">
                </div>
                <div>
                  <div class="flex items-center space-x-1">
                    <h3 class="text-xs font-bold text-white tracking-wide">${v.name}</h3>
                    <span class="text-neutral-400 text-[10px]">✓</span>
                  </div>
                  <a href="${v.igUrl}" target="_blank" class="text-[10px] text-neutral-400 hover:text-white font-mono flex items-center space-x-1">
                    <span>${v.igHandle}</span>
                    <span class="text-[9px]">↗</span>
                  </a>
                </div>
              </div>

              <div class="flex items-center space-x-2">
                ${v.isPromoted ? `
                  <span class="bg-white text-black text-[9px] font-extrabold px-2 py-0.5 rounded-full uppercase tracking-wider">
                    ★ ${v.promoTier}
                  </span>
                ` : ''}
                <button onclick="event.stopPropagation(); toggleSave('${v.id}')" class="w-7 h-7 rounded-full bg-neutral-900 border border-neutral-800 flex items-center justify-center text-white active:scale-90 transition">
                  <svg class="w-3.5 h-3.5 ${isSaved ? 'text-red-500 fill-current' : 'text-neutral-400'}" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z"/></svg>
                </button>
              </div>
            </div>

            <!-- SLIDE PREVIEW CONTAINER: PHOTO HASIL POSTINGAN ASLI DARI IG -->
            <div class="relative w-full aspect-square bg-neutral-950 overflow-hidden cursor-pointer group" onclick="openVendorModal('${v.id}')">
              <img id="slide-img-${v.id}" src="${currentSlide.image}" alt="${v.name}" class="w-full h-full object-cover filter brightness-95 group-hover:scale-105 transition duration-500">
              
              <!-- Gradient Overlay agar teks & tombol terbaca sempurna -->
              <div class="absolute inset-0 bg-gradient-to-t from-black/85 via-black/15 to-black/35 pointer-events-none"></div>

              <!-- Top Tags & Likes Counter -->
              <div class="absolute top-2.5 left-2.5 right-2.5 flex justify-between items-center pointer-events-none">
                <span id="slide-tag-${v.id}" class="bg-black/75 backdrop-blur text-neutral-200 border border-white/20 text-[9px] font-bold px-2 py-0.5 rounded-full uppercase tracking-wider">
                  ${currentSlide.tag}
                </span>
                <span id="slide-likes-${v.id}" class="bg-black/75 backdrop-blur text-white border border-white/20 text-[10px] font-mono font-bold px-2 py-0.5 rounded-full">
                  ❤️ ${currentSlide.likes}
                </span>
              </div>

              <!-- Bottom Caption Overlay -->
              <div class="absolute bottom-3 left-3 right-3 pointer-events-none">
                <p id="slide-caption-${v.id}" class="text-[11px] text-neutral-200 line-clamp-2 leading-relaxed drop-shadow italic">
                  "${currentSlide.caption}"
                </p>
                <span class="text-[9px] text-neutral-400 font-mono mt-1 block">📍 ${v.locationText}</span>
              </div>

              <!-- SLIDE ARROWS (‹ dan ›) -->
              ${v.slides.length > 1 ? `
                <button onclick="prevSlide('${v.id}', event)" class="absolute left-2.5 top-1/2 -translate-y-1/2 w-8 h-8 rounded-full bg-black/75 hover:bg-black border border-white/20 text-white flex items-center justify-center text-sm transition z-10 active:scale-90">‹</button>
                <button onclick="nextSlide('${v.id}', event)" class="absolute right-2.5 top-1/2 -translate-y-1/2 w-8 h-8 rounded-full bg-black/75 hover:bg-black border border-white/20 text-white flex items-center justify-center text-sm transition z-10 active:scale-90">›</button>
              ` : ''}

              <!-- SLIDE DOTS -->
              <div id="dots-${v.id}" class="absolute bottom-1 left-0 right-0 flex justify-center space-x-1.5 pointer-events-none">
                ${v.slides.map((_, idx) => `<span class="w-1.5 h-1.5 rounded-full transition ${idx === (v.slideIndex || 0) ? 'bg-white scale-125' : 'bg-white/40'}"></span>`).join('')}
              </div>
            </div>

            <!-- CARD FOOTER: HARGA, PREVIEW & IG CTA -->
            <div class="p-3.5 space-y-3 bg-neutral-900">
              <div class="flex justify-between items-baseline">
                <div>
                  <span class="text-[9px] text-neutral-400 uppercase tracking-widest block font-medium">Mulai dari</span>
                  <span class="text-base font-bold font-mono text-white">${priceLabel}</span>
                </div>
                <div class="flex items-center space-x-1 text-xs text-neutral-300">
                  <span class="text-amber-400">★</span>
                  <span class="font-bold font-mono">${v.rating}</span>
                  <span class="text-neutral-500 text-[10px]">(${v.reviewCount})</span>
                </div>
              </div>

              <!-- ACTION BUTTONS: PREVIEW & DIRECT INSTAGRAM -->
              <div class="flex items-center space-x-2 pt-0.5">
                <button onclick="openVendorModal('${v.id}')" class="flex-1 bg-white hover:bg-neutral-200 text-black text-xs font-bold py-2.5 rounded-xl transition active:scale-95 shadow-sm flex items-center justify-center space-x-1.5">
                  <span>Preview & Detail</span>
                </button>
                <a href="${v.igUrl}" target="_blank" class="px-3.5 py-2.5 bg-neutral-800 hover:bg-neutral-700 border border-neutral-700 rounded-xl text-white text-xs font-bold flex items-center justify-center space-x-1.5 transition active:scale-95" title="Buka Instagram Resmi Vendor">
                  <svg class="w-3.5 h-3.5 text-neutral-300" fill="currentColor" viewBox="0 0 24 24"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z"/></svg>
                  <span>Instagram</span>
                </a>
              </div>
            </div>

          </div>
        `;
      }).join('');
    }

    function setCategory(cat) {
      currentCategory = cat;
      document.querySelectorAll('.cat-pill').forEach(btn => {
        btn.classList.remove('border-white', 'bg-white', 'text-black');
        btn.classList.add('border-neutral-800', 'bg-neutral-900', 'text-neutral-300');
      });
      const activeBtn = document.getElementById(`cat-${cat}`);
      if (activeBtn) {
        activeBtn.classList.remove('border-neutral-800', 'bg-neutral-900', 'text-neutral-300');
        activeBtn.classList.add('border-white', 'bg-white', 'text-black');
      }
      filterVendors();
    }

    function setStyleFilter(style) {
      currentStyle = style;
      document.querySelectorAll('.style-chip').forEach(btn => {
        btn.classList.remove('border-white', 'text-white', 'bg-white/10');
        btn.classList.add('border-neutral-800', 'text-neutral-400');
      });
      const idMap = {
        'all': 'style-all',
        'Tradisional Jawa': 'style-jawa',
        'Warm Editorial': 'style-warm',
        'Outdoor Garden': 'style-outdoor',
        'Modern Minimalist': 'style-modern'
      };
      const active = document.getElementById(idMap[style]);
      if (active) {
        active.classList.remove('border-neutral-800', 'text-neutral-400');
        active.classList.add('border-white', 'text-white', 'bg-white/10');
      }
      filterVendors();
    }

    function resetAllFilters() {
      document.getElementById('searchInput').value = '';
      document.getElementById('cityFilter').value = 'yogyakarta';
      setCategory('all');
      setStyleFilter('all');
    }

    function toggleSave(id) {
      if (savedVendorIds.has(id)) {
        savedVendorIds.delete(id);
      } else {
        savedVendorIds.add(id);
      }
      filterVendors();
      renderSavedList();
    }

    function renderSavedList() {
      const savedList = document.getElementById('savedList');
      const savedItems = vendors.filter(v => savedVendorIds.has(v.id));

      if (savedItems.length === 0) {
        savedList.innerHTML = `<div class="text-center py-12 text-neutral-500 text-xs">Belum ada vendor favorit yang disimpan. Tekan tanda hati di kartu vendor untuk menyimpannya.</div>`;
        return;
      }

      savedList.innerHTML = savedItems.map(v => `
        <div class="flex items-center space-x-3 p-3.5 bg-neutral-900 border border-neutral-800 rounded-xl">
          <div class="w-11 h-11 rounded-xl overflow-hidden border border-neutral-800 bg-neutral-950 shrink-0">
            <img src="${v.avatar}" alt="${v.name}" class="w-full h-full object-cover">
          </div>
          <div class="flex-1">
            <span class="text-[9px] uppercase tracking-wider text-neutral-400 font-mono">${v.category.toUpperCase()} • ${v.city.toUpperCase()}</span>
            <h4 class="font-bold text-white font-serif-luxury text-sm leading-tight">${v.name}</h4>
            <p class="text-[11px] text-neutral-300 font-mono mt-0.5">${formatRupiah(v.priceStart)}</p>
          </div>
          <button onclick="openVendorModal('${v.id}')" class="text-xs bg-white text-black font-semibold px-3 py-1.5 rounded-lg active:scale-95 transition">Preview</button>
        </div>
      `).join('');
    }

    function openVendorModal(id) {
      activeVendor = vendors.find(v => v.id === id);
      if (!activeVendor) return;

      const modal = document.getElementById('vendorModal');
      const content = document.getElementById('modalContent');
      const priceLabel = activeVendor.category === 'catering' ? `${formatRupiah(activeVendor.priceStart)} / pax` : formatRupiah(activeVendor.priceStart);
      const currentSlide = activeVendor.slides[activeVendor.slideIndex || 0];

      content.innerHTML = `
        <!-- VENDOR PROFILE BANNER DENGAN FOTO PROFIL IG ASLI -->
        <div class="p-3.5 bg-neutral-900 border border-neutral-800 rounded-2xl flex items-center justify-between">
          <div class="flex items-center space-x-3">
            <div class="w-12 h-12 rounded-full overflow-hidden border border-neutral-700 bg-neutral-950 shrink-0">
              <img src="${activeVendor.avatar}" alt="${activeVendor.name}" class="w-full h-full object-cover">
            </div>
            <div>
              <div class="flex items-center space-x-1.5">
                <h3 class="text-sm font-bold text-white">${activeVendor.name}</h3>
                <span class="text-neutral-400 text-xs">✓</span>
              </div>
              <p class="text-xs text-neutral-400 font-mono font-medium">${activeVendor.igHandle}</p>
              <p class="text-[10px] text-neutral-500 font-mono">${activeVendor.igFollowers || ''} • ${activeVendor.igPostsCount || ''}</p>
            </div>
          </div>
          <a href="${activeVendor.igUrl}" target="_blank" class="bg-neutral-800 hover:bg-neutral-700 border border-neutral-700 text-white text-xs font-bold px-3 py-1.5 rounded-xl shadow">
            Buka IG ↗
          </a>
        </div>

        <!-- PRATINJAU KARYA (FOTO ASLI SLIDE) -->
        <div class="bg-neutral-900 border border-neutral-800 rounded-2xl overflow-hidden space-y-3">
          <div class="relative w-full aspect-square bg-neutral-950 overflow-hidden">
            <img src="${currentSlide.image}" alt="${activeVendor.name}" class="w-full h-full object-cover">
            <div class="absolute inset-0 bg-gradient-to-t from-black/80 via-transparent to-black/25"></div>
            
            <div class="absolute top-2.5 left-2.5 right-2.5 flex justify-between items-center">
              <span class="bg-black/75 backdrop-blur text-neutral-200 border border-white/20 text-[9px] font-bold px-2 py-0.5 rounded-full uppercase tracking-wider">
                ${currentSlide.tag}
              </span>
              <span class="bg-black/75 backdrop-blur text-white border border-white/20 text-[10px] font-mono font-bold px-2 py-0.5 rounded-full">
                ❤️ ${currentSlide.likes}
              </span>
            </div>

            <div class="absolute bottom-2.5 left-2.5 right-2.5">
              <p class="text-xs text-neutral-200 italic leading-relaxed">
                "${currentSlide.caption}"
              </p>
            </div>
          </div>

          <div class="px-3 pb-3 flex justify-between items-center text-[10px] text-neutral-400 font-mono">
            <span>📍 ${activeVendor.locationText}</span>
            <span>⭐ Rating: ${activeVendor.rating} (${activeVendor.reviewCount} ulasan)</span>
          </div>
        </div>

        <!-- CEK TANGGAL NIKAH -->
        <div class="p-3.5 bg-neutral-900 border border-neutral-800 rounded-xl space-y-2">
          <label class="text-[11px] uppercase tracking-wider text-neutral-300 font-bold block">Cek Ketersediaan Tanggal Nikahmu:</label>
          <div class="flex space-x-2">
            <input type="date" id="weddingDateCheck" value="2026-10-24" class="bg-black border border-neutral-700 text-white text-xs px-3 py-1.5 rounded-lg flex-1 focus:outline-none focus:border-white">
            <button onclick="checkDateAvailability()" class="bg-white text-black text-xs font-bold px-3 py-1.5 rounded-lg active:scale-95 transition">Cek Tanggal</button>
          </div>
          <p id="availabilityFeedback" class="text-[11px] text-emerald-400 hidden">✅ Tanggal ini masih tersedia untuk booking!</p>
        </div>

        <!-- TENTANG VENDOR -->
        <div class="space-y-1">
          <h4 class="text-[11px] uppercase tracking-wider text-neutral-400 font-bold">Bio & Tentang Vendor</h4>
          <p class="text-xs text-neutral-300 leading-relaxed">${activeVendor.description}</p>
        </div>

        <!-- PACKAGES LIST -->
        <div class="space-y-2">
          <div class="flex justify-between items-center">
            <h4 class="text-[11px] uppercase tracking-wider text-neutral-400 font-bold">Pilihan Paket Layanan</h4>
            <span class="text-[10px] text-neutral-300 font-mono">Mulai ${priceLabel}</span>
          </div>
          <div class="space-y-2">
            ${activeVendor.packages.map(p => `
              <div class="p-3 bg-black border border-neutral-800 rounded-xl flex justify-between items-center hover:border-neutral-700 transition">
                <div>
                  <h5 class="text-xs font-bold text-white">${p.name}</h5>
                  <span class="text-[10px] text-neutral-500">Garansi Layanan Resmi KITA MENIKAH</span>
                </div>
                <span class="text-xs font-mono font-bold text-white">${p.price}</span>
              </div>
            `).join('')}
          </div>
        </div>
      `;

      modal.classList.remove('hidden');
    }

    function closeVendorModal() {
      document.getElementById('vendorModal').classList.add('hidden');
      activeVendor = null;
    }

    function checkDateAvailability() {
      const feedback = document.getElementById('availabilityFeedback');
      feedback.classList.remove('hidden');
    }

    function openInstagram() {
      if (activeVendor) {
        window.open(activeVendor.igUrl, '_blank');
      }
    }

    function openWhatsAppFormatted() {
      if (activeVendor) {
        const text = encodeURIComponent(`Halo ${activeVendor.name}, saya melihat profil dan portofolio Anda di aplikasi KITA MENIKAH. Saya ingin menanyakan ketersediaan jadwal dan pricelist lengkap untuk acara pernikahan saya.`);
        window.open(`https://wa.me/${activeVendor.phone}?text=${text}`, '_blank');
      }
    }

    function calculateBudget() {
      const total = parseInt(document.getElementById('budgetInput').value) || 100000000;
      const guests = parseInt(document.getElementById('guestCount').value) || 400;

      const catering = total * 0.40;
      const venueDecor = total * 0.25;
      const photoVideo = total * 0.15;
      const muaAttire = total * 0.10;
      const woProtocol = total * 0.10;

      const container = document.getElementById('budgetResult');
      container.innerHTML = `
        <div class="border-b border-neutral-800 pb-2 mb-3">
          <span class="text-[10px] font-mono uppercase text-neutral-400">Rekomendasi Proporsi Alokasi Dana:</span>
          <p class="text-sm font-bold text-white font-mono mt-0.5">${formatRupiah(total)} (${guests} Tamu)</p>
        </div>

        <div class="space-y-2 text-xs">
          <div class="flex justify-between">
            <span class="text-neutral-400">🍽️ Catering (40%)</span>
            <span class="font-mono text-white font-semibold">${formatRupiah(catering)}</span>
          </div>
          <div class="flex justify-between">
            <span class="text-neutral-400">🏛️ Venue & Dekorasi (25%)</span>
            <span class="font-mono text-white font-semibold">${formatRupiah(venueDecor)}</span>
          </div>
          <div class="flex justify-between">
            <span class="text-neutral-400">📸 Fotografi & Film (15%)</span>
            <span class="font-mono text-white font-semibold">${formatRupiah(photoVideo)}</span>
          </div>
          <div class="flex justify-between">
            <span class="text-neutral-400">💄 MUA & Busana Paes (10%)</span>
            <span class="font-mono text-white font-semibold">${formatRupiah(muaAttire)}</span>
          </div>
          <div class="flex justify-between">
            <span class="text-neutral-400">📋 WO & Tak Terduga (10%)</span>
            <span class="font-mono text-white font-semibold">${formatRupiah(woProtocol)}</span>
          </div>
        </div>
      `;
    }

    function switchTab(tab) {
      const home = document.getElementById('viewHome');
      const budget = document.getElementById('viewBudget');
      const saved = document.getElementById('viewSaved');

      home.classList.add('hidden');
      budget.classList.add('hidden');
      saved.classList.add('hidden');

      const tabs = ['home', 'budget', 'saved'];
      tabs.forEach(t => {
        const navEl = document.getElementById('nav' + t.charAt(0).toUpperCase() + t.slice(1));
        if (navEl) {
          navEl.classList.remove('text-white');
          navEl.classList.add('text-neutral-500');
        }
      });

      const activeNav = document.getElementById('nav' + tab.charAt(0).toUpperCase() + tab.slice(1));
      if (activeNav) {
        activeNav.classList.remove('text-neutral-500');
        activeNav.classList.add('text-white');
      }

      if (tab === 'home') {
        home.classList.remove('hidden');
      } else if (tab === 'budget') {
        budget.classList.remove('hidden');
        calculateBudget();
      } else if (tab === 'saved') {
        saved.classList.remove('hidden');
        renderSavedList();
      }

      document.getElementById('appContainer').scrollTop = 0;
    }

    // INITIAL RENDER
    filterVendors();
    calculateBudget();
  </script>
</body>
</html>
'''

with open(r"C:\Users\VANDI\.gemini\antigravity\scratch\kita-menikah\index.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("Perfect index.html generated successfully!")
