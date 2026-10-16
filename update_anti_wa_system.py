import os
import shutil

html_code = '''<!DOCTYPE html>
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
    @keyframes pulse-subtle {
      0%, 100% { opacity: 1; }
      50% { opacity: 0.6; }
    }
    .animate-subtle {
      animation: pulse-subtle 3s cubic-bezier(0.4, 0, 0.6, 1) infinite;
    }
  </style>
</head>
<body class="bg-neutral-950 text-neutral-100 font-sans-clean min-h-screen flex items-center justify-center p-0 md:p-6 antialiased select-none">

  <!-- Outer Device Mockup Container -->
  <div class="relative w-full max-w-md h-screen md:h-[920px] bg-black md:rounded-[48px] shadow-2xl border-0 md:border-[10px] md:border-neutral-900 overflow-hidden flex flex-col">
    
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
      
      <!-- TOP STICKY HEADER -->
      <header class="px-5 pt-3 pb-3 border-b border-neutral-900 bg-black/95 backdrop-blur sticky top-0 z-40 space-y-2.5">
        
        <!-- TOP ROW: TITLE & ROLE SWITCHER (KLIEN vs DASHBOARD VENDOR) -->
        <div class="flex justify-between items-center">
          <div class="text-left">
            <span class="text-[8px] tracking-[0.25em] text-neutral-400 uppercase font-medium block">The Curated Wedding Marketplace</span>
            <h1 class="text-lg tracking-[0.2em] font-serif-luxury uppercase font-bold text-white whitespace-nowrap">
              K I T A &nbsp; M E N I K A H
            </h1>
          </div>

          <!-- TOGGLE MODE: KLIEN / VENDOR -->
          <button onclick="toggleAppMode()" id="btnAppMode" class="flex items-center space-x-1.5 bg-neutral-900 border border-neutral-700 hover:border-white px-2.5 py-1.5 rounded-full text-[10px] font-bold transition active:scale-95 shadow">
            <span class="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></span>
            <span id="labelAppMode" class="text-neutral-200">Mode Mitra</span>
          </button>
        </div>

        <!-- SEARCH BAR (HANYA MUNCUL DI MODE KLIEN) -->
        <div id="clientSearchBar" class="relative">
          <svg class="w-4 h-4 text-neutral-500 absolute left-3 top-2.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"/></svg>
          <input type="text" id="searchInput" oninput="filterVendors()" placeholder="Cari Jawara, Sandi Liems, Lux Visual, Nijo, Neiscala..." class="w-full bg-neutral-900 border border-neutral-800 rounded-xl pl-9 pr-4 py-2 text-xs text-white placeholder-neutral-500 focus:outline-none focus:border-white transition">
        </div>

        <!-- LOKASI & PILIHAN KOTA (SIMPEL IKON + DROPDOWN KOTA) -->
        <div id="clientCityFilter" class="flex items-center space-x-2 bg-neutral-900 rounded-xl px-3 py-1.5 border border-neutral-800 text-xs">
          <svg class="w-3.5 h-3.5 text-neutral-400 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"/><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"/></svg>
          <select id="cityFilter" onchange="filterVendors()" class="bg-transparent text-white font-medium focus:outline-none cursor-pointer flex-1 text-xs">
            <option value="yogyakarta" selected class="bg-neutral-900 text-white">📍 DI Yogyakarta</option>
            <option value="all" class="bg-neutral-900 text-white">Semua Jawa</option>
            <option value="jakarta" class="bg-neutral-900 text-white">DKI Jakarta</option>
            <option value="bandung" class="bg-neutral-900 text-white">Bandung</option>
            <option value="surabaya" class="bg-neutral-900 text-white">Surabaya</option>
          </select>
        </div>
      </header>

      <!-- VIEW 1: HOME VIEW (EKSPLORASI KLIEN) -->
      <div id="viewHome" class="space-y-4">

        <!-- BANNER PROTEKSI TRANSAKSI RESMI -->
        <div class="px-5 pt-1">
          <div class="bg-gradient-to-r from-neutral-900 via-neutral-900 to-neutral-950 border border-neutral-800 rounded-2xl p-3 flex items-start space-x-2.5">
            <div class="w-7 h-7 rounded-full bg-emerald-500/10 border border-emerald-500/30 flex items-center justify-center shrink-0 mt-0.5">
              <svg class="w-3.5 h-3.5 text-emerald-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"/></svg>
            </div>
            <div class="flex-1">
              <span class="text-[10px] font-bold text-white tracking-wide flex items-center space-x-1">
                <span>Garansi Rekening Bersama Escrow</span>
                <span class="text-[9px] bg-emerald-500/20 text-emerald-300 px-1.5 py-0.2 rounded font-mono">100% Aman</span>
              </span>
              <p class="text-[10px] text-neutral-400 leading-snug mt-0.5">
                DP ditahan aman di platform & dicairkan ke vendor bertahap. Bebas risiko vendor kabur. Transaksi wajib di dalam aplikasi.
              </p>
            </div>
          </div>
        </div>

        <!-- CATEGORIES SLIDER -->
        <div class="px-5">
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

        <!-- VENDORS LIST -->
        <div class="px-5">
          <div class="flex justify-between items-center mb-3">
            <div>
              <h2 class="text-xs tracking-[0.2em] uppercase font-bold text-neutral-300">Daftar Terkurasi</h2>
              <p class="text-[10px] text-neutral-500 font-mono">Geser slide kartu ‹ › untuk melihat hasil foto asli dari IG</p>
            </div>
            <span id="vendorCount" class="text-xs text-neutral-400 font-mono">Memuat...</span>
          </div>

          <div id="vendorList" class="space-y-4">
            <!-- Dynamic Vendor Cards with Slides injected by JS -->
          </div>
        </div>
      </div>

      <!-- VIEW 2: VENDOR PARTNER DASHBOARD (DASHBOARD REKAPAN ORDER VENDOR) -->
      <div id="viewVendorDashboard" class="hidden px-5 py-3 space-y-4">
        <!-- VENDOR PROFILE HEADER IN DASHBOARD -->
        <div class="bg-gradient-to-br from-neutral-900 to-neutral-950 border border-neutral-800 rounded-2xl p-4 space-y-3">
          <div class="flex justify-between items-start">
            <div class="flex items-center space-x-3">
              <div class="w-12 h-12 rounded-full overflow-hidden border border-neutral-700 bg-black shrink-0">
                <img src="assets/vendors/avatars/jawara.jpg" class="w-full h-full object-cover">
              </div>
              <div>
                <span class="text-[9px] bg-neutral-800 text-neutral-300 font-mono px-2 py-0.5 rounded uppercase font-bold">Portal Mitra Resmi</span>
                <h3 class="text-sm font-bold text-white tracking-wide mt-0.5">Jawara Photo Studio</h3>
                <span class="text-[10px] text-neutral-400">@jawara.photo • Sleman, DI Yogyakarta</span>
              </div>
            </div>
            <span class="text-[10px] font-mono text-emerald-400 bg-emerald-500/10 border border-emerald-500/30 px-2 py-1 rounded-full font-bold">● Aktif</span>
          </div>

          <!-- SUMMARY CARDS: TOTAL ORDER & PENDAPATAN BERSIH -->
          <div class="grid grid-cols-3 gap-2 pt-1 border-t border-neutral-800/80">
            <div class="bg-black/60 rounded-xl p-2.5 border border-neutral-800">
              <span class="text-[9px] text-neutral-400 block">Total Booking</span>
              <span id="recapTotalOrders" class="text-xs font-bold text-white font-mono mt-0.5 block">3 Order</span>
            </div>
            <div class="bg-black/60 rounded-xl p-2.5 border border-neutral-800">
              <span class="text-[9px] text-neutral-400 block">Fee Platform</span>
              <span class="text-xs font-bold text-amber-400 font-mono mt-0.5 block">10%</span>
            </div>
            <div class="bg-black/60 rounded-xl p-2.5 border border-neutral-800">
              <span class="text-[9px] text-neutral-400 block">Omzet Bersih</span>
              <span id="recapNetEarnings" class="text-xs font-bold text-emerald-400 font-mono mt-0.5 block">Rp 15.120.000</span>
            </div>
          </div>
        </div>

        <!-- REKAPAN BOOKING MASUK -->
        <div class="space-y-2.5">
          <div class="flex justify-between items-center">
            <h3 class="text-xs font-bold uppercase tracking-wider text-neutral-300">Rekapan Booking Klien Masuk</h3>
            <span class="text-[10px] text-neutral-500 font-mono">Shopee-Style Escrow</span>
          </div>

          <div id="bookingOrdersList" class="space-y-3">
            <!-- Dynamic Booking Cards Injected by JS -->
          </div>
        </div>
      </div>

      <!-- VIEW 3: BUDGET PLANNER TAB -->
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

      <!-- VIEW 4: SAVED VENDORS TAB -->
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

    <!-- MODAL 1: VENDOR DETAIL & PACKAGE SELECTION -->
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

        <!-- Floating CTA at bottom of Modal (CHAT RESMI & PILIH PAKET - ZERO WA) -->
        <div class="p-4 bg-neutral-900/95 backdrop-blur border-t border-neutral-800 flex space-x-2.5">
          <button id="modalChatBtn" onclick="openChatWithActiveVendor()" class="flex-1 bg-neutral-800 hover:bg-neutral-700 border border-neutral-700 text-white text-xs font-bold py-3 rounded-xl flex items-center justify-center space-x-2 transition shadow">
            <svg class="w-4 h-4 text-emerald-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 12h.01M12 12h.01M16 12h.01M21 12c0 4.418-4.03 8-9 8a9.863 9.863 0 01-4.255-.949L3 20l1.395-3.72C3.512 15.042 3 13.574 3 12c0-4.418 4.03-8 9-8s9 3.582 9 8z"/></svg>
            <span>Chat Vendor</span>
          </button>
          <button id="modalBookBtn" onclick="openBookingCheckout()" class="flex-1 bg-white text-black text-xs font-bold py-3 rounded-xl flex items-center justify-center space-x-1.5 hover:bg-neutral-200 active:scale-95 transition shadow-lg">
            <span>⚡ Ambil Paket</span>
          </button>
        </div>

      </div>
    </div>

    <!-- MODAL 2: IN-APP CHAT (KOMUNIKASI 2 ARAH RESMI & PROTEKSI ANTI-WA) -->
    <div id="chatModal" class="hidden absolute inset-0 z-50 bg-black/95 backdrop-blur-md flex flex-col justify-end transition-all">
      <div class="bg-neutral-950 border-t border-neutral-800 rounded-t-3xl h-[88%] flex flex-col overflow-hidden">
        
        <!-- Chat Header -->
        <div class="px-4 py-3 bg-neutral-900 border-b border-neutral-800 flex justify-between items-center">
          <div class="flex items-center space-x-2.5">
            <div class="relative">
              <div class="w-9 h-9 rounded-full overflow-hidden border border-neutral-700 bg-black">
                <img id="chatVendorAvatar" src="" class="w-full h-full object-cover">
              </div>
              <span class="w-2.5 h-2.5 rounded-full bg-emerald-500 border border-black absolute -bottom-0.5 -right-0.5"></span>
            </div>
            <div>
              <div class="flex items-center space-x-1">
                <h3 id="chatVendorName" class="text-xs font-bold text-white tracking-wide"></h3>
                <span class="text-neutral-400 text-[10px]">✓</span>
              </div>
              <span class="text-[9px] text-emerald-400 font-mono">Online • Membalas < 5 mnt</span>
            </div>
          </div>
          <button onclick="closeChatModal()" class="w-7 h-7 rounded-full bg-neutral-800 text-neutral-400 flex items-center justify-center text-xs hover:text-white">✕</button>
        </div>

        <!-- Anti-Leakage Shield Notice Bar -->
        <div class="bg-emerald-950/40 border-b border-emerald-900/40 px-3.5 py-1.5 flex items-center space-x-2">
          <svg class="w-3.5 h-3.5 text-emerald-400 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z"/></svg>
          <span class="text-[9px] text-emerald-300 font-medium leading-tight">
            Chat resmi terlindungi. Nomor WA & kontak luar disembunyikan otomatis demi jaminan garansi 100%.
          </span>
        </div>

        <!-- Chat Messages Container -->
        <div id="chatMessages" class="flex-1 p-4 overflow-y-auto no-scrollbar space-y-3">
          <!-- Populated by JS -->
        </div>

        <!-- Anti-Leakage Warning Alert Box (Shows if user tries typing WA/Phone) -->
        <div id="chatWarningBox" class="hidden px-4 py-2 bg-amber-950/80 border-t border-amber-800 text-amber-300 text-[10px] flex items-center space-x-2">
          <span class="text-base">⚠️</span>
          <span>Nomor kontak/WA disembunyikan sistem. Transaksi hanya sah melalui KITA MENIKAH.</span>
        </div>

        <!-- Chat Input Bar -->
        <div class="p-3 bg-neutral-900 border-t border-neutral-800 flex items-center space-x-2">
          <input type="text" id="chatInputText" onkeydown="if(event.key==='Enter') sendChatMessage()" placeholder="Ketik pesan untuk vendor..." class="flex-1 bg-black border border-neutral-700 rounded-xl px-3.5 py-2 text-xs text-white placeholder-neutral-500 focus:outline-none focus:border-white">
          <button onclick="sendChatMessage()" class="w-9 h-9 rounded-xl bg-white text-black flex items-center justify-center hover:bg-neutral-200 transition active:scale-95">
            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"/></svg>
          </button>
        </div>

      </div>
    </div>

    <!-- MODAL 3: CHECKOUT BOOKING & VOUCHER KITA MENIKAH -->
    <div id="bookingModal" class="hidden absolute inset-0 z-50 bg-black/95 backdrop-blur-md flex flex-col justify-end transition-all">
      <div class="bg-neutral-950 border-t border-neutral-800 rounded-t-3xl max-h-[94%] flex flex-col overflow-hidden">
        
        <!-- Header Drag & Close -->
        <div class="px-5 pt-3 pb-2 flex justify-between items-center border-b border-neutral-900">
          <div class="flex items-center space-x-2">
            <span class="w-2 h-2 rounded-full bg-emerald-400"></span>
            <span class="text-xs font-bold text-white tracking-wider uppercase font-mono">Checkout Booking Resmi</span>
          </div>
          <button onclick="closeBookingModal()" class="w-7 h-7 rounded-full bg-neutral-900 text-neutral-400 flex items-center justify-center text-xs hover:text-white">✕</button>
        </div>

        <div id="bookingFormContent" class="p-5 overflow-y-auto no-scrollbar space-y-4 flex-1">
          <!-- Populated by JS -->
        </div>

        <!-- Floating Checkout Button -->
        <div class="p-4 bg-neutral-900/95 backdrop-blur border-t border-neutral-800">
          <button onclick="confirmSubmitBooking()" class="w-full bg-white text-black text-xs font-bold py-3.5 rounded-xl uppercase tracking-wider hover:bg-neutral-200 active:scale-95 transition shadow-xl flex items-center justify-center space-x-2">
            <svg class="w-4 h-4 text-emerald-600" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"/></svg>
            <span>Bayar DP & Masukkan ke Rekapan Vendor</span>
          </button>
          <span class="text-[9px] text-neutral-400 text-center block mt-1.5 font-mono">
            🛡️ Escrow KITA MENIKAH melindungi dana Anda hingga hari H.
          </span>
        </div>

      </div>
    </div>

    <!-- MODAL 4: BOOKING SUCCESS TOAST -->
    <div id="successModal" class="hidden absolute inset-0 z-50 bg-black/90 backdrop-blur-md flex items-center justify-center p-6">
      <div class="bg-neutral-900 border border-neutral-700 rounded-3xl p-6 text-center max-w-sm space-y-4 shadow-2xl">
        <div class="w-14 h-14 bg-emerald-500/10 border border-emerald-500/30 text-emerald-400 rounded-full flex items-center justify-center mx-auto">
          <svg class="w-7 h-7" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/></svg>
        </div>
        <div>
          <span id="successOrderId" class="text-[10px] font-mono text-emerald-400 bg-emerald-950 px-2.5 py-0.5 rounded-full border border-emerald-800 font-bold"></span>
          <h3 class="text-base font-bold text-white tracking-wide mt-2">Booking Berhasil Dikunci!</h3>
          <p class="text-xs text-neutral-300 mt-1 leading-relaxed">
            Rekapan pemesanan telah diteruskan ke kalender vendor. Dana DP diamankan di Escrow KITA MENIKAH.
          </p>
        </div>
        <div class="pt-2 flex space-x-2">
          <button onclick="viewInVendorDashboard()" class="flex-1 bg-neutral-800 text-white text-xs font-bold py-2.5 rounded-xl border border-neutral-700">
            Lihat Rekapan di Vendor
          </button>
          <button onclick="closeSuccessModal()" class="flex-1 bg-white text-black text-xs font-bold py-2.5 rounded-xl">
            Selesai
          </button>
        </div>
      </div>
    </div>

  </div>

  <script>
    // DATA VENDOR LENGKAP DENGAN PILIHAN PAKET PRICE LIST, FOTO IG ASLI & AVATAR
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
        description: 'Vendor dokumentasi foto & video pernikahan berbasis di Yogyakarta dengan tagar khas #bersamajawara. Menghadirkan dokumentasi emosional, hangat, dan abadi (*timeless candid*).',
        slideIndex: 0,
        slides: [
          {
            image: 'assets/vendors/slides/jawara_slide_1.jpg',
            tag: '🔥 PALING BANYAK LIKE DI IG',
            likes: '4.820 likes',
            caption: 'Some souls meet once and change each other forever. The Wedding Prima & Fauzan @amaliaprimaa & @fb_santoso #bersamajawara 🤍'
          },
          {
            image: 'assets/vendors/slides/jawara_slide_2.jpg',
            tag: '✨ TRADISIONAL PAES JOGJA',
            likes: '3.690 likes',
            caption: 'The Wedding @maretafwa & @knrw_wsnv 🤍 MUA: @scratchby.mwulandey #weddingjogja #bersamajawara'
          },
          {
            image: 'assets/vendors/slides/jawara_slide_3.jpg',
            tag: '🏛️ JOGLO HERITAGE',
            likes: '2.840 likes',
            caption: 'From The Wedding Sisil & Dhimas di pendopo joglo bersejarah #jawaraphoto'
          }
        ],
        packages: [
          { id: 'jawara-p1', name: 'Paket Intimate Akad Only (1 FG + 1 VG)', priceNum: 3800000, price: 'Rp 3.800.000', detail: 'Liputan akad 4 jam, 1 fotografer + 1 videografer, 50 edit foto, teaser 1 min reels, all raw files via cloud.' },
          { id: 'jawara-p2', name: 'Full Day Wedding Documentation', priceNum: 6500000, price: 'Rp 6.500.000', detail: 'Liputan akad & resepsi 8 jam, 2 FG + 2 VG, teaser cinematic 1 min, video highlights 3 min, 120 foto edit, flashdisk box.' },
          { id: 'jawara-p3', name: 'All-In Prewedding + Wedding Day Exclusive', priceNum: 9800000, price: 'Rp 9.800.000', detail: 'Prewedding Jogja outdoor + Full Day Wedding, cetak album kolase kulit mewah 20x30, 2 frame canvas 40x60, cinematic video 4K.' }
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
        description: 'Fotografer pernikahan spesialis editorial couple portraits dan intimate wedding storytelling di Jogja.',
        slideIndex: 0,
        slides: [
          {
            image: 'assets/vendors/slides/sandiliem_slide_1.jpg',
            tag: '🔥 PALING BANYAK LIKE DI IG',
            likes: '5.210 likes',
            caption: 'Megahnya pelaminan gebyok berhias burung merak dan instalasi bunga #bysandiliem 🤍'
          },
          {
            image: 'assets/vendors/slides/sandiliem_slide_2.jpg',
            tag: '🤍 AKAD RESMI JOGJA',
            likes: '3.880 likes',
            caption: 'Senyum bahagia mempelai berbalut busana akad putih sakral #sandiliemphotography'
          }
        ],
        packages: [
          { id: 'sandi-p1', name: 'Intimate Couple Session / Prewedding', priceNum: 4500000, price: 'Rp 4.500.000', detail: 'Sesi foto 5 jam di 2 lokasi Jogja pilihan, 40 edited photos, mini cinematic teaser, wooden box print.' },
          { id: 'sandi-p2', name: 'Full Day Wedding Coverage & Framed Canvas', priceNum: 8000000, price: 'Rp 8.000.000', detail: 'Liputan akad & resepsi penuh hari H, 2 FG master, teaser reels, album exclusive hardcover, frame canvas 50x70.' }
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
        description: 'Kreator visual pernikahan di Yogyakarta yang menyuguhkan karya foto dan video cinematic dengan tone warna hangat bersahabat.',
        slideIndex: 0,
        slides: [
          {
            image: 'assets/vendors/slides/luxvisual_slide_1.jpg',
            tag: '🔥 PALING BANYAK LIKE DI IG',
            likes: '3.920 likes',
            caption: 'Momen lamaran sakral penuh kehangatan keluarga @luxvisual.id 💍'
          }
        ],
        packages: [
          { id: 'lux-p1', name: 'Paket Lamaran / Engagement Documentation', priceNum: 2000000, price: 'Rp 2.000.000', detail: 'Liputan lamaran 3 jam, 1 FG + 1 VG, 35 foto edit, video reels siap unggah, drive link.' },
          { id: 'lux-p2', name: 'Akad Nikah Only Coverage (Foto + Reels)', priceNum: 3500000, price: 'Rp 3.500.000', detail: 'Liputan akad 4 jam, 2 personil foto & video, video sinematik 1 menit, 60 foto edit.' }
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
        description: '"Menceritakan kisah cinta kalian melalui bingkai visual yang jujur." Ahli dalam mengabadikan prosesi adat Jawa dan intimate modern wedding.',
        slideIndex: 0,
        slides: [
          {
            image: 'assets/vendors/slides/kitakancerita_slide_1.jpg',
            tag: '🔥 PALING BANYAK LIKE DI IG',
            likes: '6.450 likes',
            caption: 'Momen restu tulus orang tua saat prosesi lamaran dan temu keluarga @kitakancerita 🌿'
          }
        ],
        packages: [
          { id: 'kita-p1', name: 'Akad / Pemberkatan Only (Full Documentation)', priceNum: 5000000, price: 'Rp 5.000.000', detail: 'Dokumentasi khidmat prosesi akad / upacara adat, 2 FG profesional, 70 edit foto, cloud gallery.' },
          { id: 'kita-p2', name: 'Full Day Wedding Story: 2 FG + 2 VG', priceNum: 8500000, price: 'Rp 8.500.000', detail: 'Liputan full day panggih / resepsi, teaser 1 min, film pendek pernikahan 5 min, album box istimewa.' }
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
        description: 'Tim fotografer muda kreatif berbasis di Jogja-Solo dengan visual aesthetic segar, ceria, dan sangat ramah.',
        slideIndex: 0,
        slides: [
          {
            image: 'assets/vendors/slides/nijo_slide_1.jpg',
            tag: '🔥 PALING BANYAK LIKE DI IG',
            likes: '4.180 likes',
            caption: 'Prewedding gagah berbusana beskap dan blangkon Jogja di Gumuk Pasir @thenijophotograph 💛'
          },
          {
            image: 'assets/vendors/slides/nijo_slide_2.jpg',
            tag: '🍂 AUTUMN PROMISE',
            likes: '3.250 likes',
            caption: 'Genggaman jemari dan ikatan cincin abadi di tepian pantai selatan #thenijophotograph'
          },
          {
            image: 'assets/vendors/slides/nijo_slide_3.jpg',
            tag: '👑 SILUET SANGGUL JOGJA',
            likes: '2.680 likes',
            caption: 'Siluet anggun sanggul dan cunduk mentul pengantin putri Jawa karya NIJO'
          }
        ],
        packages: [
          { id: 'nijo-p1', name: 'Intimate Wedding Documentation', priceNum: 5000000, price: 'Rp 5.000.000', detail: 'Dokumentasi intimate 5 jam, 2 FG, 60 edit foto berestetika tinggi, all files drive.' },
          { id: 'nijo-p2', name: 'Wedding Day Cinematic Photo & Video', priceNum: 7800000, price: 'Rp 7.800.000', detail: 'Dokumentasi full day akad & resepsi, teaser cinematic, highlight video, album cetak premium.' }
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
        description: 'Spesialis wedding photography and cinematic film bernuansa romantis, anggun, dengan pencahayaan alami nan memukau.',
        slideIndex: 0,
        slides: [
          {
            image: 'assets/vendors/slides/neiscala_slide_1.jpg',
            tag: '🔥 PALING BANYAK LIKE DI IG',
            likes: '7.340 likes',
            caption: 'Among billions of souls, my heart found the one. Cinematic session @neiscala ✨'
          }
        ],
        packages: [
          { id: 'neiscala-p1', name: 'The Romantic Day (Photo & Cinematic Reel)', priceNum: 7000000, price: 'Rp 7.000.000', detail: 'Liputan akad & resepsi 6 jam, video sinematik 1 menit, 80 edit foto editorial.' },
          { id: 'neiscala-p2', name: 'Grand Wedding All-In (Drone + 2 Album Mewah)', priceNum: 12000000, price: 'Rp 12.000.000', detail: 'Full day 10 jam, 3 FG + 2 VG + pilot drone, film 7 menit 4K, 2 album kolase kulit.' }
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
        description: 'Studio foto dan film pernikahan di Bantul. Menyediakan paket komplit foto studio, prewedding outdoor, liputan hari H, serta kolaborasi MUA & dekorasi.',
        slideIndex: 0,
        slides: [
          {
            image: 'assets/vendors/slides/lunanouva_slide_1.jpg',
            tag: '🔥 PALING BANYAK LIKE DI IG',
            likes: '3.620 likes',
            caption: 'Potret anggun berbusana kebaya kutubaru khas Yogyakarta @lunanouovastudio__ 🌸'
          }
        ],
        packages: [
          { id: 'luna-p1', name: 'Paket Liputan Akad & Resepsi Bantul', priceNum: 4000000, price: 'Rp 4.000.000', detail: 'Liputan hari H 6 jam, 1 FG + 1 VG, 50 foto edit, mini teaser, USB exclusive.' },
          { id: 'luna-p2', name: 'Prewedding Studio + Outdoor Gumuk Pasir', priceNum: 2800000, price: 'Rp 2.800.000', detail: 'Sesi indoor studio Bantul + Gumuk Pasir Parangkusumo, 30 foto edit, cetak canvas.' }
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
        description: 'Maestro tata rias pengantin adat Jawa paling disegani di Jogja. Sangat presisi dalam pakem cengkorongan Paes Ageng, Kanigaran, dan Jangan Menir.',
        slideIndex: 0,
        slides: [
          {
            image: 'assets/vendors/slides/mamuk_slide_1.jpg',
            tag: '👑 MAESTRO PAES AGENG',
            likes: '18.300 likes',
            caption: 'Mahakarya Paes Ageng Kraton Ngayogyakarta Hadiningrat prada emas keraton @mamuktukangmakeupjogja'
          }
        ],
        packages: [
          { id: 'mamuk-p1', name: 'Rias Pengantin Jogja Putri Modifikasi', priceNum: 9500000, price: 'Rp 9.500.000', detail: 'Rias pengantin akad + resepsi, rias 2 ibu, aksesoris lengkap, paes pakem modif.' },
          { id: 'mamuk-p2', name: 'Paes Ageng Jangan Menir Komplit + Busana Adat', priceNum: 14000000, price: 'Rp 14.000.000', detail: 'Tata rias langsung maestro, busana beludru sepasang pengantin, cengkorongan prada emas asli.' }
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
        description: 'Cagar budaya bersejarah peninggalan Sultan Hamengku Buwono VII. Ikon royal wedding adat Jawa termegah dan tersakral di Indonesia.',
        slideIndex: 0,
        slides: [
          {
            image: 'assets/vendors/slides/ambarrukmo_slide_1.jpg',
            tag: '🏛️ ROYAL HERITAGE VENUE',
            likes: '16.700 likes',
            caption: 'Megahnya pilar kayu jati bersejarah abad ke-18 Pendopo Agung Royal Ambarrukmo'
          }
        ],
        packages: [
          { id: 'venue-p1', name: 'Heritage Akad & Paringgitan (150 Pax)', priceNum: 85000000, price: 'Rp 85.000.000', detail: 'Penggunaan Pendopo Agung 4 jam, sound system, kamar pengantin Ambarrukmo, izin acara.' },
          { id: 'venue-p2', name: 'Royal Grand Pendopo & Taman Gandhok (500 Pax)', priceNum: 145000000, price: 'Rp 145.000.000', detail: 'Penggunaan penuh indoor pendopo & taman outdoor, 2 kamar suite hotel, koordinasi teknis.' }
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
        description: 'Spesialis dekorasi pelaminan gebyok keraton dan instalasi bunga hidup megah di Jogja.',
        slideIndex: 0,
        slides: [
          {
            image: 'assets/vendors/slides/danani_slide_1.jpg',
            tag: '🌸 GEBYOK KRATON FLORAL',
            likes: '6.900 likes',
            caption: 'Kemegahan pelaminan gebyok jati ukir klasik bertabur ribuan kuntum bunga segar @dananidecoration'
          }
        ],
        packages: [
          { id: 'decor-p1', name: 'Pelaminan Gebyok Kraton 8 Meter', priceNum: 25000000, price: 'Rp 25.000.000', detail: 'Gebyok jati ukir klasik 8M, instalasi bunga hidup fresh, pergola masuk, pundi uang, lighting.' }
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
        description: 'Raja katering pernikahan terpercaya di Yogyakarta dengan sertifikasi ISO 22000 dan resep citarasa ningrat Kraton.',
        slideIndex: 0,
        slides: [
          {
            image: 'assets/vendors/slides/vidi_slide_1.jpg',
            tag: '🍽️ CITARASA NINGRAT KRATON',
            likes: '5.600 likes',
            caption: 'Sajian hidangan prasmanan citarasa ningrat Kraton Yogyakarta Halal MUI Grade A @vidicatering'
          }
        ],
        packages: [
          { id: 'cat-p1', name: 'Paket Prasmanan Tradisi Jogja (Min 500 Pax)', priceNum: 25000000, price: 'Rp 50.000 / pax', detail: 'Menu prasmanan komplit: Nasi, Sup Pengantin, Daging Lapis, Ayam Goreng Lengkuas, Es Doger, dessert.' }
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
        description: 'Wedding Organizer terkemuka di Yogyakarta spesialis pemandu pakem adat Jawa Paes Ageng dan upacara panggih berwibawa.',
        slideIndex: 0,
        slides: [
          {
            image: 'assets/vendors/slides/mahkota_slide_1.jpg',
            tag: '💍 PROTOKOL ADAT KHIDMAT',
            likes: '7.120 likes',
            caption: 'Ketenangan jalannya prosesi ijab kabul sakral berkat pengawalan tim @mahkota_wo.jogja'
          }
        ],
        packages: [
          { id: 'wo-p1', name: 'Wedding Day Coordination (6 Crew Full Day)', priceNum: 15000000, price: 'Rp 15.000.000', detail: '6 orang kru profesional, koordinasi teknis vendor hari H, pengawalan rundown adat panggih, HT crew.' }
        ]
      }
    ];

    // INITIAL BOOKINGS DATA (REKAPAN BOOKING KITA MENIKAH DENGAN TAKE-RATE 10%)
    let bookingOrders = [
      {
        orderId: 'KM-JAW-2026-081',
        vendorId: 'fg-jawara',
        vendorName: 'Jawara Photo',
        clientName: 'Mbak Sarah & Mas Adit',
        weddingDate: '24 Oktober 2026',
        venue: 'Pendopo Royal Ambarrukmo',
        packageName: 'Paket Intimate Akad Only',
        packagePrice: 3800000,
        voucherCode: 'JOGJAMANTEN',
        voucherDiscount: 300000,
        finalTotal: 3500000,
        platformFeeRate: 0.10, // 10%
        platformFeeAmount: 350000, // 10% dari transaksi
        vendorNet: 3150000, // 90% cair ke vendor
        status: 'DP_ESCROW_PAID',
        statusLabel: 'DP Diamankan di Escrow',
        createdAt: '15 Okt 2026, 11:30'
      },
      {
        orderId: 'KM-JAW-2026-082',
        vendorId: 'fg-jawara',
        vendorName: 'Jawara Photo',
        clientName: 'Mbak Dinda & Mas Rio',
        weddingDate: '15 November 2026',
        venue: 'Gedung Wanitatama Jogja',
        packageName: 'Full Day Wedding Documentation',
        packagePrice: 6500000,
        voucherCode: 'EARLYBIRD',
        voucherDiscount: 500000,
        finalTotal: 6000000,
        platformFeeRate: 0.10,
        platformFeeAmount: 600000,
        vendorNet: 5400000,
        status: 'CONFIRMED',
        statusLabel: 'Jadwal Dikunci Vendor',
        createdAt: '14 Okt 2026, 16:45'
      },
      {
        orderId: 'KM-SAN-2026-039',
        vendorId: 'fg-sandiliem',
        vendorName: 'Sandi Liems Photography',
        clientName: 'Mbak Anisa & Mas Farhan',
        weddingDate: '08 Desember 2026',
        venue: 'Omah Pakem Kaliurang',
        packageName: 'Full Day Wedding Coverage & Framed Canvas',
        packagePrice: 8000000,
        voucherCode: 'JOGJAMANTEN',
        voucherDiscount: 300000,
        finalTotal: 7700000,
        platformFeeRate: 0.10,
        platformFeeAmount: 770000,
        vendorNet: 6930000,
        status: 'DP_ESCROW_PAID',
        statusLabel: 'DP Diamankan di Escrow',
        createdAt: '12 Okt 2026, 09:15'
      }
    ];

    // CHAT DATA PRESETS (KOMUNIKASI 2 ARAH DI DALAM APLIKASI)
    let activeChatVendor = null;
    let chatHistories = {
      'fg-jawara': [
        { sender: 'vendor', time: '10:00', text: 'Halo kak! Selamat datang di Jawara Photo Official. Ada yang bisa kami bantu untuk konsep pernikahannya di Jogja? ✨' },
        { sender: 'client', time: '10:02', text: 'Halo kak Jawara, untuk tanggal 20 Desember 2026 di Sleman apakah slot fotonya masih available?' },
        { sender: 'vendor', time: '10:03', text: 'Kabar baik kak! Tanggal 20 Desember 2026 saat ini masih open 1 slot tim utama. Kakak berencana ambil Paket Intimate Akad atau Full Day Documentation?' },
        { sender: 'vendor', time: '10:04', text: 'Oiya kak, gunakan kode voucher JOGJAMANTEN saat ambil paket ya untuk potongan langsung Rp 300.000 dari platform KITA MENIKAH 🤍' }
      ],
      'fg-sandiliem': [
        { sender: 'vendor', time: '09:30', text: 'Halo kak, terima kasih telah mengunjungi profil Sandi Liems Photography. Boleh tahu rencana tanggal dan konsep wedding-nya? 🎞️' }
      ]
    };

    let currentCategory = 'all';
    let currentStyle = 'all';
    let savedVendorIds = new Set(['fg-jawara', 'fg-sandiliem', 'fg-kitakancerita']);
    let activeVendor = null;
    let selectedPackage = null;
    let currentAppMode = 'client'; // 'client' or 'vendor'
    let appliedVoucher = null;

    function formatRupiah(num) {
      return 'Rp ' + Number(num).toLocaleString('id-ID');
    }

    // TOGGLE APP MODE (KLIEN vs MITRA VENDOR)
    function toggleAppMode() {
      if (currentAppMode === 'client') {
        currentAppMode = 'vendor';
        document.getElementById('labelAppMode').innerText = 'Mode Klien';
        document.getElementById('btnAppMode').classList.add('bg-white', 'text-black', 'border-white');
        document.getElementById('btnAppMode').classList.remove('bg-neutral-900', 'text-neutral-200');
        
        document.getElementById('clientSearchBar').classList.add('hidden');
        document.getElementById('clientCityFilter').classList.add('hidden');
        document.getElementById('viewHome').classList.add('hidden');
        document.getElementById('viewVendorDashboard').classList.remove('hidden');
        renderVendorDashboard();
      } else {
        currentAppMode = 'client';
        document.getElementById('labelAppMode').innerText = 'Mode Mitra';
        document.getElementById('btnAppMode').classList.remove('bg-white', 'text-black', 'border-white');
        document.getElementById('btnAppMode').classList.add('bg-neutral-900', 'text-neutral-200');

        document.getElementById('clientSearchBar').classList.remove('hidden');
        document.getElementById('clientCityFilter').classList.remove('hidden');
        document.getElementById('viewVendorDashboard').classList.add('hidden');
        document.getElementById('viewHome').classList.remove('hidden');
        filterVendors();
      }
    }

    // RENDER VENDOR DASHBOARD (REKAPAN ORDER & OMZET HAK 9-12%)
    function renderVendorDashboard() {
      const container = document.getElementById('bookingOrdersList');
      const jawaraOrders = bookingOrders.filter(o => o.vendorId === 'fg-jawara');

      let totalGross = jawaraOrders.reduce((acc, curr) => acc + curr.finalTotal, 0);
      let totalFee = jawaraOrders.reduce((acc, curr) => acc + curr.platformFeeAmount, 0);
      let totalNet = jawaraOrders.reduce((acc, curr) => acc + curr.vendorNet, 0);

      document.getElementById('recapTotalOrders').innerText = `${jawaraOrders.length} Order`;
      document.getElementById('recapNetEarnings').innerText = formatRupiah(totalNet);

      container.innerHTML = jawaraOrders.map(order => `
        <div class="bg-neutral-900 border border-neutral-800 rounded-2xl p-4 space-y-3">
          <div class="flex justify-between items-center border-b border-neutral-800 pb-2">
            <div>
              <span class="text-[10px] font-mono text-neutral-400 font-bold">${order.orderId}</span>
              <h4 class="text-xs font-bold text-white tracking-wide mt-0.5">${order.clientName}</h4>
            </div>
            <span class="text-[9px] font-mono bg-emerald-500/20 text-emerald-300 border border-emerald-500/30 px-2 py-0.5 rounded-full font-bold">
              ${order.statusLabel}
            </span>
          </div>

          <div class="space-y-1 text-xs">
            <div class="flex justify-between text-neutral-300">
              <span class="text-neutral-500">Tanggal Hari H:</span>
              <span class="font-medium text-white">📅 ${order.weddingDate}</span>
            </div>
            <div class="flex justify-between text-neutral-300">
              <span class="text-neutral-500">Lokasi Venue:</span>
              <span class="text-neutral-300 font-medium">📍 ${order.venue}</span>
            </div>
            <div class="flex justify-between text-neutral-300">
              <span class="text-neutral-500">Paket Dipilih:</span>
              <span class="text-neutral-200 font-semibold">${order.packageName}</span>
            </div>
          </div>

          <!-- RINCIAN FINANSIAL & HAK PLATFORM KITA MENIKAH (10%) -->
          <div class="bg-black/60 rounded-xl p-3 border border-neutral-800 space-y-1 text-[11px] font-mono">
            <div class="flex justify-between text-neutral-400">
              <span>Nilai Transaksi Klien:</span>
              <span class="text-white">${formatRupiah(order.finalTotal)}</span>
            </div>
            <div class="flex justify-between text-amber-400">
              <span>Hak Platform KITA MENIKAH (10%):</span>
              <span>- ${formatRupiah(order.platformFeeAmount)}</span>
            </div>
            <div class="flex justify-between text-emerald-400 font-bold border-t border-neutral-800 pt-1 text-xs">
              <span>Hak Bersih Vendor (90%):</span>
              <span>${formatRupiah(order.vendorNet)}</span>
            </div>
          </div>

          <div class="flex space-x-2 pt-1">
            <button onclick="openChatFromVendor('${order.vendorId}', '${order.clientName}')" class="flex-1 bg-neutral-800 text-white text-xs font-bold py-2 rounded-xl border border-neutral-700 flex items-center justify-center space-x-1.5 hover:bg-neutral-700">
              <svg class="w-3.5 h-3.5 text-emerald-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 12h.01M12 12h.01M16 12h.01M21 12c0 4.418-4.03 8-9 8a9.863 9.863 0 01-4.255-.949L3 20l1.395-3.72C3.512 15.042 3 13.574 3 12c0-4.418 4.03-8 9-8s9 3.582 9 8z"/></svg>
              <span>Balas Chat Klien</span>
            </button>
            <button class="bg-white text-black text-xs font-bold px-3 py-2 rounded-xl hover:bg-neutral-200">
              Konfirmasi Jadwal
            </button>
          </div>
        </div>
      `).join('');
    }

    function openChatFromVendor(vendorId, clientName) {
      const v = vendors.find(x => x.id === vendorId);
      if (v) openChatWithVendor(v);
    }

    // SLIDE CONTROLS
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

      if (dotsEl && v.slides.length > 1) {
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
        const hasMultipleSlides = v.slides && v.slides.length > 1;

        return `
          <div class="bg-neutral-900 border border-neutral-800 hover:border-neutral-700 rounded-2xl overflow-hidden transition duration-300">
            
            <!-- CARD TOP HEADER: FOTO PROFIL IG ASLI & USERNAME IG -->
            <div class="px-3.5 py-2.5 bg-neutral-950 flex justify-between items-center border-b border-neutral-800/80">
              <div class="flex items-center space-x-2.5">
                <div class="w-9 h-9 rounded-full overflow-hidden border border-neutral-700 bg-neutral-900 shrink-0">
                  <img src="${v.avatar}" alt="${v.name}" class="w-full h-full object-cover">
                </div>
                <div>
                  <div class="flex items-center space-x-1">
                    <h3 class="text-xs font-bold text-white tracking-wide">${v.name}</h3>
                    <span class="text-neutral-400 text-[10px]">✓</span>
                  </div>
                  <a href="${v.igUrl}" target="_blank" onclick="event.stopPropagation()" class="text-[10px] text-neutral-400 hover:text-white font-mono flex items-center space-x-1">
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

              <!-- SLIDE NAVIGATION CONTROLS (TOMBOL KIRI & KANAN) -->
              ${hasMultipleSlides ? `
                <button onclick="prevSlide('${v.id}', event)" class="absolute left-2.5 top-1/2 -translate-y-1/2 w-8 h-8 rounded-full bg-black/60 hover:bg-black/90 text-white flex items-center justify-center text-sm border border-white/20 transition active:scale-90">
                  ‹
                </button>
                <button onclick="nextSlide('${v.id}', event)" class="absolute right-2.5 top-1/2 -translate-y-1/2 w-8 h-8 rounded-full bg-black/60 hover:bg-black/90 text-white flex items-center justify-center text-sm border border-white/20 transition active:scale-90">
                  ›
                </button>
                <div id="dots-${v.id}" class="absolute bottom-1.5 left-0 right-0 flex justify-center space-x-1.5 pointer-events-none">
                  ${v.slides.map((_, idx) => `
                    <span class="w-1.5 h-1.5 rounded-full transition ${idx === (v.slideIndex || 0) ? 'bg-white scale-125' : 'bg-white/40'}"></span>
                  `).join('')}
                </div>
              ` : ''}
            </div>

            <!-- CARD FOOTER: HARGA, TOMBOL CHAT & AMBIL PAKET (ZERO WA) -->
            <div class="p-3.5 bg-neutral-900 flex justify-between items-center border-t border-neutral-800">
              <div>
                <span class="text-[10px] text-neutral-400 block">Mulai dari:</span>
                <div class="text-sm font-bold text-white font-mono tracking-tight">${priceLabel}</div>
              </div>

              <div class="flex items-center space-x-2">
                <button onclick="event.stopPropagation(); openChatWithVendorById('${v.id}')" class="w-8 h-8 rounded-xl bg-neutral-800 border border-neutral-700 flex items-center justify-center text-emerald-400 hover:text-white hover:border-neutral-500 transition" title="Chat Vendor">
                  <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 12h.01M12 12h.01M16 12h.01M21 12c0 4.418-4.03 8-9 8a9.863 9.863 0 01-4.255-.949L3 20l1.395-3.72C3.512 15.042 3 13.574 3 12c0-4.418 4.03-8 9-8s9 3.582 9 8z"/></svg>
                </button>
                <button onclick="openVendorModal('${v.id}')" class="bg-white text-black text-xs font-bold px-3 py-1.5 rounded-xl hover:bg-neutral-200 transition">
                  Lihat Paket
                </button>
              </div>
            </div>

          </div>
        `;
      }).join('');
    }

    function setCategory(cat) {
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

    // OPEN VENDOR MODAL
    function openVendorModal(vendorId) {
      const v = vendors.find(x => x.id === vendorId);
      if (!v) return;
      activeVendor = v;
      selectedPackage = v.packages[0]; // default first package

      const modalContent = document.getElementById('modalContent');
      modalContent.innerHTML = `
        <div class="space-y-4">
          <div class="flex items-center space-x-3 pb-3 border-b border-neutral-800">
            <div class="w-14 h-14 rounded-full overflow-hidden border border-neutral-700 bg-neutral-900 shrink-0">
              <img src="${v.avatar}" alt="${v.name}" class="w-full h-full object-cover">
            </div>
            <div>
              <h2 class="text-base font-bold text-white tracking-wide">${v.name}</h2>
              <div class="flex items-center space-x-2 mt-0.5">
                <span class="text-xs text-neutral-400 font-mono">${v.igHandle}</span>
                <span class="text-[10px] text-neutral-500">•</span>
                <span class="text-xs text-neutral-400">${v.igFollowers}</span>
              </div>
              <span class="text-[11px] text-neutral-400 block mt-1">📍 ${v.locationText}</span>
            </div>
          </div>

          <p class="text-xs text-neutral-300 leading-relaxed">${v.description}</p>

          <div class="space-y-2 pt-2">
            <h4 class="text-xs font-bold text-neutral-200 uppercase tracking-wider">Koleksi Foto Terpopuler di Instagram:</h4>
            <div class="grid grid-cols-2 gap-2">
              ${v.slides.map(s => `
                <div class="relative rounded-xl overflow-hidden aspect-square border border-neutral-800">
                  <img src="${s.image}" class="w-full h-full object-cover">
                  <span class="absolute bottom-1 left-1 bg-black/80 text-[9px] px-1.5 py-0.5 rounded text-white font-mono">
                    ❤️ ${s.likes}
                  </span>
                </div>
              `).join('')}
            </div>
          </div>

          <!-- PILIHAN PAKET PRICE LIST RESMI -->
          <div class="space-y-2.5 pt-2">
            <div class="flex justify-between items-center">
              <h4 class="text-xs font-bold text-neutral-200 uppercase tracking-wider">Pilihan Paket & Price List Resmi:</h4>
              <span class="text-[10px] text-emerald-400 font-mono">Bisa Cicil DP</span>
            </div>

            <div class="space-y-2">
              ${v.packages.map((p, idx) => `
                <div onclick="selectPackageRadio('${p.id}')" id="pkg-card-${p.id}" class="pkg-card cursor-pointer bg-neutral-900 border ${idx === 0 ? 'border-white bg-neutral-800/60' : 'border-neutral-800'} rounded-xl p-3.5 space-y-1.5 transition">
                  <div class="flex justify-between items-start">
                    <div class="flex items-center space-x-2">
                      <input type="radio" name="pkgOption" id="radio-${p.id}" ${idx === 0 ? 'checked' : ''} class="accent-white">
                      <span class="text-xs font-bold text-white">${p.name}</span>
                    </div>
                    <span class="text-xs font-bold text-emerald-400 font-mono">${p.price}</span>
                  </div>
                  <p class="text-[11px] text-neutral-400 pl-5 leading-relaxed">${p.detail}</p>
                </div>
              `).join('')}
            </div>
          </div>
        </div>
      `;

      document.getElementById('vendorModal').classList.remove('hidden');
    }

    function selectPackageRadio(pkgId) {
      if (!activeVendor) return;
      selectedPackage = activeVendor.packages.find(p => p.id === pkgId);
      document.querySelectorAll('.pkg-card').forEach(card => {
        card.classList.remove('border-white', 'bg-neutral-800/60');
        card.classList.add('border-neutral-800');
      });
      const selectedCard = document.getElementById(`pkg-card-${pkgId}`);
      if (selectedCard) {
        selectedCard.classList.remove('border-neutral-800');
        selectedCard.classList.add('border-white', 'bg-neutral-800/60');
      }
      const radio = document.getElementById(`radio-${pkgId}`);
      if (radio) radio.checked = true;
    }

    function closeVendorModal() {
      document.getElementById('vendorModal').classList.add('hidden');
    }

    // IN-APP CHAT FUNCTIONS (ANTI-WA & DUA ARAH)
    function openChatWithActiveVendor() {
      if (activeVendor) {
        closeVendorModal();
        openChatWithVendor(activeVendor);
      }
    }

    function openChatWithVendorById(vendorId) {
      const v = vendors.find(x => x.id === vendorId);
      if (v) openChatWithVendor(v);
    }

    function openChatWithVendor(v) {
      activeChatVendor = v;
      document.getElementById('chatVendorName').innerText = v.name;
      document.getElementById('chatVendorAvatar').src = v.avatar;
      
      if (!chatHistories[v.id]) {
        chatHistories[v.id] = [
          { sender: 'vendor', time: '10:00', text: `Halo kak! Terima kasih telah berkunjung ke ${v.name}. Ada yang bisa kami bantu seputar konsep dan tanggal pernikahan? ✨` }
        ];
      }

      renderChatMessages();
      document.getElementById('chatModal').classList.remove('hidden');
    }

    function closeChatModal() {
      document.getElementById('chatModal').classList.add('hidden');
      document.getElementById('chatWarningBox').classList.add('hidden');
    }

    function renderChatMessages() {
      if (!activeChatVendor) return;
      const history = chatHistories[activeChatVendor.id] || [];
      const container = document.getElementById('chatMessages');

      container.innerHTML = history.map(msg => {
        const isClient = msg.sender === 'client';
        return `
          <div class="flex flex-col ${isClient ? 'items-end' : 'items-start'}">
            <div class="max-w-[75%] px-3.5 py-2.5 rounded-2xl text-xs leading-relaxed ${isClient ? 'bg-white text-black rounded-tr-none font-medium' : 'bg-neutral-900 border border-neutral-800 text-neutral-200 rounded-tl-none'}">
              ${msg.text}
            </div>
            <span class="text-[9px] text-neutral-500 font-mono mt-1 px-1">${msg.time}</span>
          </div>
        `;
      }).join('');

      container.scrollTop = container.scrollHeight;
    }

    // SMART DETECTION: SENSOR NOMOR WA / HP AGAR TIDAK BYPASS PLATFORM
    function sendChatMessage() {
      const inputEl = document.getElementById('chatInputText');
      const text = inputEl.value.trim();
      if (!text || !activeChatVendor) return;

      const now = new Date();
      const timeStr = `${String(now.getHours()).padStart(2, '0')}:${String(now.getMinutes()).padStart(2, '0')}`;

      // Check regex for WA/phone number leak (08xxx, +62xxx, wa, whatsapp, call)
      const phoneRegex = /(\+62|62|08)[0-9\s-]{7,14}/gi;
      const waKeywords = /(wa|whatsapp|wea|wasap|no\s*hp|telepon|direct\s*trf|trf\s*luar)/gi;

      let cleanText = text;
      let hasLeaked = false;

      if (phoneRegex.test(text) || waKeywords.test(text)) {
        hasLeaked = true;
        cleanText = text.replace(phoneRegex, '[Nomor disembunyikan sistem KITA MENIKAH]');
        cleanText = cleanText.replace(waKeywords, '[kontak luar diblokir]');
        document.getElementById('chatWarningBox').classList.remove('hidden');
      } else {
        document.getElementById('chatWarningBox').classList.add('hidden');
      }

      chatHistories[activeChatVendor.id].push({
        sender: 'client',
        time: timeStr,
        text: cleanText
      });

      inputEl.value = '';
      renderChatMessages();

      // Realistic Vendor Auto-reply after 1.5 seconds
      setTimeout(() => {
        if (!activeChatVendor) return;
        let reply = 'Siap kak, pertanyaan kakak kami catat. Untuk amankan jadwal pernikahan kakak, silakan klik tombol "Ambil Paket" ya agar sistem kami langsung mem-booking tanggal tersebut 🤍';
        if (hasLeaked) {
          reply = 'Mohon maaf kak, seluruh komunikasi dan transaksi wajib dilakukan di dalam KITA MENIKAH demi keamanan garansi uang kembali 100% dan perlindungan rekening bersama 🙏';
        }
        chatHistories[activeChatVendor.id].push({
          sender: 'vendor',
          time: timeStr,
          text: reply
        });
        renderChatMessages();
      }, 1200);
    }

    // CHECKOUT BOOKING & VOUCHER KITA MENIKAH
    function openBookingCheckout() {
      if (!activeVendor) return;
      closeVendorModal();

      if (!selectedPackage) {
        selectedPackage = activeVendor.packages[0];
      }

      appliedVoucher = null;
      renderBookingForm();
      document.getElementById('bookingModal').classList.remove('hidden');
    }

    function closeBookingModal() {
      document.getElementById('bookingModal').classList.add('hidden');
    }

    function renderBookingForm() {
      if (!activeVendor || !selectedPackage) return;

      const basePrice = selectedPackage.priceNum;
      const discount = appliedVoucher ? appliedVoucher.discount : 0;
      const finalPrice = Math.max(0, basePrice - discount);
      const dpAmount = Math.round(finalPrice * 0.30); // 30% DP

      const formContent = document.getElementById('bookingFormContent');
      formContent.innerHTML = `
        <div class="space-y-4">
          <!-- Vendor & Package Selected Box -->
          <div class="bg-neutral-900 border border-neutral-800 rounded-2xl p-4 flex items-center space-x-3">
            <div class="w-12 h-12 rounded-full overflow-hidden border border-neutral-700 bg-black shrink-0">
              <img src="${activeVendor.avatar}" class="w-full h-full object-cover">
            </div>
            <div class="flex-1">
              <span class="text-[9px] font-mono text-neutral-400 font-bold uppercase">${activeVendor.category}</span>
              <h3 class="text-xs font-bold text-white">${activeVendor.name}</h3>
              <p class="text-[11px] text-emerald-400 font-bold mt-0.5">${selectedPackage.name}</p>
            </div>
          </div>

          <!-- Wedding Date Picker -->
          <div class="space-y-1.5">
            <label class="text-xs font-bold text-neutral-300 block">Tanggal Hari H Pernikahan</label>
            <input type="date" id="inputWeddingDate" value="2026-12-20" class="w-full bg-black border border-neutral-700 rounded-xl px-3.5 py-2.5 text-xs text-white focus:outline-none focus:border-white">
          </div>

          <!-- Lokasi Venue / Rumah -->
          <div class="space-y-1.5">
            <label class="text-xs font-bold text-neutral-300 block">Nama Venue / Area di Yogyakarta</label>
            <input type="text" id="inputVenue" value="Royal Ambarrukmo / Pendopo Jogja" placeholder="Contoh: Pendopo Ndalem Ngabean" class="w-full bg-black border border-neutral-700 rounded-xl px-3.5 py-2.5 text-xs text-white placeholder-neutral-500 focus:outline-none focus:border-white">
          </div>

          <!-- Nama Pasangan Pengantin -->
          <div class="space-y-1.5">
            <label class="text-xs font-bold text-neutral-300 block">Nama Kedua Mempelai</label>
            <input type="text" id="inputCoupleNames" value="Mbak Nadya & Mas Rizky" placeholder="Contoh: Sarah & Adit" class="w-full bg-black border border-neutral-700 rounded-xl px-3.5 py-2.5 text-xs text-white placeholder-neutral-500 focus:outline-none focus:border-white">
          </div>

          <!-- VOUCHER PROMO PLATFORM KITA MENIKAH -->
          <div class="bg-neutral-900 border border-neutral-800 rounded-2xl p-3.5 space-y-2">
            <div class="flex justify-between items-center">
              <label class="text-xs font-bold text-white flex items-center space-x-1.5">
                <span>🎟️ Voucher KITA MENIKAH</span>
              </label>
              <span class="text-[10px] text-neutral-400">Gunakan: <strong class="text-white">JOGJAMANTEN</strong></span>
            </div>
            
            <div class="flex space-x-2">
              <input type="text" id="inputVoucherCode" placeholder="Masukkan kode voucher..." class="flex-1 bg-black border border-neutral-700 rounded-xl px-3 py-2 text-xs uppercase text-white font-mono placeholder-neutral-500 focus:outline-none focus:border-white">
              <button onclick="applyVoucherCode()" class="bg-white text-black text-xs font-bold px-3 py-2 rounded-xl hover:bg-neutral-200 transition">
                Gunakan
              </button>
            </div>

            ${appliedVoucher ? `
              <div class="bg-emerald-950/60 border border-emerald-800 rounded-xl p-2.5 flex justify-between items-center text-xs">
                <span class="text-emerald-300 font-bold font-mono">✓ Voucher ${appliedVoucher.code} Aktif</span>
                <span class="text-emerald-300 font-bold">- ${formatRupiah(appliedVoucher.discount)}</span>
              </div>
            ` : ''}
          </div>

          <!-- RINGKASAN PEMBAYARAN SHOPEE-STYLE ESCROW -->
          <div class="bg-neutral-900/80 border border-neutral-800 rounded-2xl p-4 space-y-2 text-xs">
            <h4 class="font-bold text-white uppercase tracking-wider text-[11px] mb-1">Rincian Pembayaran:</h4>
            <div class="flex justify-between text-neutral-400">
              <span>Harga Paket Resmi:</span>
              <span class="font-mono text-white">${formatRupiah(basePrice)}</span>
            </div>
            ${appliedVoucher ? `
              <div class="flex justify-between text-emerald-400 font-bold">
                <span>Diskon Voucher KITA MENIKAH:</span>
                <span class="font-mono">- ${formatRupiah(appliedVoucher.discount)}</span>
              </div>
            ` : ''}
            <div class="flex justify-between text-neutral-400">
              <span>Biaya Garansi Escrow Rekening Bersama:</span>
              <span class="text-emerald-400 font-mono font-bold">GRATIS</span>
            </div>
            <div class="flex justify-between text-white font-bold border-t border-neutral-800 pt-2 text-sm">
              <span>Total Nilai Booking:</span>
              <span class="font-mono text-emerald-400">${formatRupiah(finalPrice)}</span>
            </div>
            <div class="flex justify-between text-white font-bold bg-neutral-950 p-2.5 rounded-xl border border-neutral-800 mt-2">
              <div>
                <span class="text-xs block">Bayar DP Sekarang (30%):</span>
                <span class="text-[9px] text-neutral-400 font-normal">Pelunasan H-7 setelah konfirmasi vendor</span>
              </div>
              <span class="font-mono text-sm text-white">${formatRupiah(dpAmount)}</span>
            </div>
          </div>
        </div>
      `;
    }

    function applyVoucherCode() {
      const code = (document.getElementById('inputVoucherCode').value || '').toUpperCase().trim();
      if (code === 'JOGJAMANTEN') {
        appliedVoucher = { code: 'JOGJAMANTEN', discount: 300000 };
      } else if (code === 'EARLYBIRD') {
        appliedVoucher = { code: 'EARLYBIRD', discount: 500000 };
      } else {
        alert('Kode voucher tidak valid. Coba gunakan: JOGJAMANTEN atau EARLYBIRD');
        return;
      }
      renderBookingForm();
    }

    // SUBMIT BOOKING (MASUK KE REKAPAN VENDOR & SIMPAN KE REKBER)
    function confirmSubmitBooking() {
      if (!activeVendor || !selectedPackage) return;

      const date = document.getElementById('inputWeddingDate').value || '2026-12-20';
      const venue = document.getElementById('inputVenue').value || 'Yogyakarta';
      const client = document.getElementById('inputCoupleNames').value || 'Mbak & Mas Pengantin';

      const basePrice = selectedPackage.priceNum;
      const discount = appliedVoucher ? appliedVoucher.discount : 0;
      const finalPrice = Math.max(0, basePrice - discount);
      const feeRate = 0.10; // 10%
      const feeAmount = Math.round(finalPrice * feeRate);
      const vendorNet = finalPrice - feeAmount;

      const randomNum = Math.floor(100 + Math.random() * 900);
      const orderId = `KM-${activeVendor.id.replace('fg-','').toUpperCase().slice(0,3)}-2026-${randomNum}`;

      const newOrder = {
        orderId: orderId,
        vendorId: activeVendor.id,
        vendorName: activeVendor.name,
        clientName: client,
        weddingDate: date,
        venue: venue,
        packageName: selectedPackage.name,
        packagePrice: basePrice,
        voucherCode: appliedVoucher ? appliedVoucher.code : '-',
        voucherDiscount: discount,
        finalTotal: finalPrice,
        platformFeeRate: feeRate,
        platformFeeAmount: feeAmount,
        vendorNet: vendorNet,
        status: 'DP_ESCROW_PAID',
        statusLabel: 'DP Diamankan di Escrow',
        createdAt: 'Hari ini'
      };

      bookingOrders.unshift(newOrder);
      closeBookingModal();

      document.getElementById('successOrderId').innerText = orderId;
      document.getElementById('successModal').classList.remove('hidden');
    }

    function closeSuccessModal() {
      document.getElementById('successModal').classList.add('hidden');
    }

    function viewInVendorDashboard() {
      closeSuccessModal();
      if (currentAppMode !== 'vendor') {
        toggleAppMode();
      }
    }

    function switchTab(tab) {
      if (currentAppMode === 'vendor') {
        toggleAppMode(); // switch back to client when clicking dock tabs
      }

      ['Home', 'Budget', 'Saved'].forEach(t => {
        const view = document.getElementById(`view${t}`);
        const nav = document.getElementById(`nav${t}`);
        if (view) view.classList.add('hidden');
        if (nav) {
          nav.classList.remove('text-white');
          nav.classList.add('text-neutral-500');
        }
      });

      if (tab === 'home') {
        document.getElementById('viewHome').classList.remove('hidden');
        document.getElementById('navHome').classList.add('text-white');
        document.getElementById('navHome').classList.remove('text-neutral-500');
      } else if (tab === 'budget') {
        document.getElementById('viewBudget').classList.remove('hidden');
        document.getElementById('navBudget').classList.add('text-white');
        document.getElementById('navBudget').classList.remove('text-neutral-500');
        calculateBudget();
      } else if (tab === 'saved') {
        document.getElementById('viewSaved').classList.remove('hidden');
        document.getElementById('navSaved').classList.add('text-white');
        document.getElementById('navSaved').classList.remove('text-neutral-500');
        renderSavedList();
      }
    }

    function renderSavedList() {
      const container = document.getElementById('savedList');
      const list = vendors.filter(v => savedVendorIds.has(v.id));
      if (list.length === 0) {
        container.innerHTML = `<p class="text-xs text-neutral-500 py-6 text-center">Belum ada vendor yang disimpan.</p>`;
        return;
      }
      container.innerHTML = list.map(v => `
        <div class="bg-neutral-900 border border-neutral-800 rounded-xl p-3 flex items-center justify-between cursor-pointer" onclick="openVendorModal('${v.id}')">
          <div class="flex items-center space-x-3">
            <div class="w-10 h-10 rounded-full overflow-hidden border border-neutral-700 bg-neutral-950">
              <img src="${v.avatar}" class="w-full h-full object-cover">
            </div>
            <div>
              <h4 class="text-xs font-bold text-white">${v.name}</h4>
              <span class="text-[10px] text-neutral-400 font-mono">${v.igHandle} • Mulai ${formatRupiah(v.priceStart)}</span>
            </div>
          </div>
          <button onclick="event.stopPropagation(); toggleSave('${v.id}')" class="text-red-500 p-2">✕</button>
        </div>
      `).join('');
    }

    function calculateBudget() {
      const total = parseFloat(document.getElementById('budgetInput').value) || 100000000;
      const guests = parseInt(document.getElementById('guestCount').value) || 400;

      const items = [
        { cat: '🍽️ Katering & Jamuan (35%)', amount: total * 0.35, note: `Estimasi Rp ${( (total*0.35)/guests ).toLocaleString('id-ID')} / tamu` },
        { cat: '🏛️ Venue & Sewa Gedung (20%)', amount: total * 0.20, note: 'Pendopo / Ballroom Jogja' },
        { cat: '🌸 Dekorasi & Pelaminan (15%)', amount: total * 0.15, note: 'Gebyok / Modern Fresh Flower' },
        { cat: '📸 Fotografi & Video Liputan (12%)', amount: total * 0.12, note: 'Jawara / Sandi Liem / Nijo / Neiscala' },
        { cat: '💄 MUA, Busana Adat & Paes (10%)', amount: total * 0.10, note: 'Paes Ageng / Modern Bride' },
        { cat: '📋 Wedding Organizer (5%)', amount: total * 0.05, note: 'Pemandu Acara Adat & Rundown' },
        { cat: '🛡️ Dana Darurat & Souvenir (3%)', amount: total * 0.03, note: 'Keperluan tak terduga hari H' }
      ];

      const resContainer = document.getElementById('budgetResult');
      resContainer.innerHTML = `
        <h4 class="text-xs font-bold text-white uppercase tracking-wider mb-2">Simulasi Alokasi Anggaran Ideal:</h4>
        <div class="space-y-2">
          ${items.map(i => `
            <div class="flex justify-between items-center text-xs border-b border-neutral-800/60 pb-1.5">
              <div>
                <span class="text-neutral-200 font-medium">${i.cat}</span>
                <span class="text-[10px] text-neutral-500 block">${i.note}</span>
              </div>
              <span class="font-mono font-bold text-white">${formatRupiah(Math.round(i.amount))}</span>
            </div>
          `).join('')}
        </div>
      `;
    }

    function resetAllFilters() {
      document.getElementById('searchInput').value = '';
      document.getElementById('cityFilter').value = 'yogyakarta';
      setCategory('all');
    }

    // INIT ON LOAD
    filterVendors();
  </script>
</body>
</html>
'''

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_code)
print("Updated index.html with Anti-WA Shield, In-App Chat, Checkout & Vendor Dashboard!")

brain_artifact = r"C:\Users\VANDI\.gemini\antigravity\brain\98605af6-0ebd-4ed8-a33b-bdbb36cb2699\preview_prototype.html"
with open(brain_artifact, "w", encoding="utf-8") as f:
    f.write(html_code)
print("Updated brain preview_prototype.html successfully!")
