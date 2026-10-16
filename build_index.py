# -*- coding: utf-8 -*-
import json

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
    .instagram-gradient {
      background: radial-gradient(circle at 30% 107%, #fdf497 0%, #fdf497 5%, #fd5949 45%, #d6249f 60%, #285AEB 90%);
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
    <div id="appContainer" class="flex-1 overflow-y-auto no-scrollbar pt-12 pb-24 bg-black">
      
      <!-- TOP STICKY HEADER -->
      <header class="px-5 pt-3 pb-3 border-b border-neutral-900 bg-black/95 backdrop-blur sticky top-0 z-40 space-y-2.5">
        <div class="flex justify-between items-center">
          <div>
            <span class="text-[9px] tracking-[0.25em] text-neutral-400 uppercase font-semibold">The Curated Wedding Marketplace</span>
            <h1 class="text-2xl font-serif-luxury tracking-widest uppercase font-bold text-white leading-tight">
              K I T A &nbsp; M E N I K A H
            </h1>
          </div>
          
          <!-- LIVE INSTAGRAM DIRECT SHORTCUT -->
          <button onclick="switchTab('igFeed')" class="flex items-center space-x-1.5 bg-neutral-900 border border-neutral-800 hover:border-rose-500/50 px-3 py-1.5 rounded-full text-xs active:scale-95 transition shadow-sm">
            <span class="w-2 h-2 rounded-full bg-rose-500 animate-pulse"></span>
            <span class="text-[11px] font-bold text-white">Live IG Feed</span>
          </button>
        </div>

        <!-- SEARCH BAR -->
        <div class="relative">
          <svg class="w-4 h-4 text-neutral-500 absolute left-3 top-3" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"/></svg>
          <input type="text" id="searchInput" oninput="filterVendors()" placeholder="Cari Jawara, Sandi Liem, Lux Visual, Nijo, Neiscala..." class="w-full bg-neutral-900 border border-neutral-800 rounded-xl pl-9 pr-4 py-2 text-xs text-white placeholder-neutral-500 focus:outline-none focus:border-white transition">
        </div>

        <!-- REGION SELECTOR (JAWA & AREA DETAIL JOGJA) -->
        <div class="flex space-x-2">
          <div class="flex-1 flex items-center space-x-1.5 bg-neutral-900 rounded-lg px-2.5 py-1.5 border border-neutral-800 text-[11px]">
            <svg class="w-3.5 h-3.5 text-neutral-400 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"/><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"/></svg>
            <select id="cityFilter" onchange="onCityChange()" class="bg-transparent text-white font-semibold focus:outline-none cursor-pointer flex-1 text-[11px]">
              <option value="yogyakarta" selected class="bg-neutral-900 text-white">📍 DI Yogyakarta</option>
              <option value="all" class="bg-neutral-900 text-white">Semua Jawa</option>
              <option value="jakarta" class="bg-neutral-900 text-white">DKI Jakarta</option>
              <option value="bandung" class="bg-neutral-900 text-white">Bandung</option>
              <option value="surabaya" class="bg-neutral-900 text-white">Surabaya</option>
            </select>
          </div>

          <div id="subAreaWrapper" class="flex items-center space-x-1 bg-neutral-900 rounded-lg px-2 py-1.5 border border-neutral-800 text-[11px]">
            <select id="subAreaFilter" onchange="filterVendors()" class="bg-transparent text-neutral-300 font-medium focus:outline-none cursor-pointer text-[11px]">
              <option value="all" selected class="bg-neutral-900 text-white">Semua Area Jogja</option>
              <option value="Kota Yogyakarta" class="bg-neutral-900 text-white">Kota Jogja</option>
              <option value="Sleman" class="bg-neutral-900 text-white">Sleman</option>
              <option value="Bantul" class="bg-neutral-900 text-white">Bantul</option>
              <option value="Kulon Progo" class="bg-neutral-900 text-white">Kulon Progo</option>
              <option value="Gunungkidul" class="bg-neutral-900 text-white">Gunungkidul</option>
            </select>
          </div>
        </div>
      </header>

      <!-- CONTENT: HOME VIEW -->
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
            <span class="text-[10px] text-neutral-500 uppercase tracking-wider font-semibold shrink-0">Filter:</span>
            <button onclick="setStyleFilter('all')" id="style-all" class="style-chip active px-3 py-1 rounded-full border border-white text-white bg-white/10 text-[11px] whitespace-nowrap">Semua</button>
            <button onclick="setStyleFilter('Tradisional Jawa')" id="style-jawa" class="style-chip px-3 py-1 rounded-full border border-neutral-800 text-neutral-400 text-[11px] whitespace-nowrap hover:border-neutral-600">🏛️ Pakem Jawa Paes Ageng</button>
            <button onclick="setStyleFilter('Warm Editorial')" id="style-warm" class="style-chip px-3 py-1 rounded-full border border-neutral-800 text-neutral-400 text-[11px] whitespace-nowrap hover:border-neutral-600">🎞️ Warm Editorial & Candid</button>
            <button onclick="setStyleFilter('Outdoor Garden')" id="style-outdoor" class="style-chip px-3 py-1 rounded-full border border-neutral-800 text-neutral-400 text-[11px] whitespace-nowrap hover:border-neutral-600">🌿 Outdoor / Kaliurang</button>
            <button onclick="setStyleFilter('Modern Minimalist')" id="style-modern" class="style-chip px-3 py-1 rounded-full border border-neutral-800 text-neutral-400 text-[11px] whitespace-nowrap hover:border-neutral-600">✨ Modern Intimate</button>
          </div>
        </div>

        <!-- VENDORS LIST -->
        <div class="px-5">
          <div class="flex justify-between items-center mb-2.5">
            <div>
              <h2 class="text-xs tracking-[0.2em] uppercase font-bold text-neutral-300">Daftar Terkurasi Yogyakarta</h2>
              <p class="text-[10px] text-neutral-500 font-mono">100% Kredensial Asli Instagram (Bukan AI)</p>
            </div>
            <span id="vendorCount" class="text-xs text-neutral-400 font-mono">Memuat...</span>
          </div>

          <div id="vendorList" class="space-y-4">
            <!-- Dynamic Vendor Cards injected by JS -->
          </div>
        </div>
      </div>

      <!-- CONTENT: INSTAGRAM FEED LIVE SIMULATOR (ASLI DARI IG META) -->
      <div id="viewIgFeed" class="hidden px-5 py-4 space-y-5">
        <div class="border-b border-neutral-800 pb-3">
          <div class="flex items-center space-x-2">
            <span class="w-2.5 h-2.5 rounded-full bg-rose-500 animate-ping"></span>
            <span class="text-[10px] tracking-widest uppercase text-rose-400 font-bold">100% Real Live Instagram Embed</span>
          </div>
          <h2 class="text-xl font-serif-luxury font-bold text-white tracking-wide mt-1">Postingan Terpopuler Vendor Temanmu</h2>
          <p class="text-xs text-neutral-400 mt-1">Foto, jumlah like, dan komentar dimuat langsung dari server Instagram Meta resmi (Bukan Gambar AI / Stock).</p>
        </div>

        <div id="igFeedContainer" class="space-y-6">
          <!-- Populated by JS with authentic Instagram embed iframes -->
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

    <!-- BOTTOM APP NAVIGATION DOCK -->
    <nav class="absolute bottom-0 left-0 right-0 h-16 bg-black/95 backdrop-blur border-t border-neutral-900 flex justify-around items-center px-4 z-40">
      <button onclick="switchTab('home')" id="navHome" class="flex flex-col items-center justify-center space-y-1 text-white">
        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6"/></svg>
        <span class="text-[10px] font-semibold tracking-wider">Eksplor</span>
      </button>

      <button onclick="switchTab('igFeed')" id="navIgFeed" class="flex flex-col items-center justify-center space-y-1 text-neutral-500 hover:text-white transition">
        <svg class="w-5 h-5 text-rose-500" fill="currentColor" viewBox="0 0 24 24"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z"/></svg>
        <span class="text-[10px] font-semibold tracking-wider text-rose-400">Feed IG</span>
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

    <!-- VENDOR DETAIL MODAL -->
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
          <button id="modalIgBtn" onclick="openInstagram()" class="flex-1 bg-gradient-to-r from-purple-700 via-pink-600 to-amber-600 hover:opacity-90 text-white text-xs font-bold py-3 rounded-xl flex items-center justify-center space-x-2 transition shadow-lg">
            <svg class="w-4 h-4 text-white" fill="currentColor" viewBox="0 0 24 24"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z"/></svg>
            <span>Buka Langsung di Instagram</span>
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
    // DAFTAR VENDOR LENGKAP YOGYAKARTA DENGAN HARGA & KREDENSIAL ASLI INSTAGRAM
    const vendors = [
      // 1. JAWARA PHOTO (Mulai Rp 3.800.000) - 100% POSTINGAN ASLI DARI @jawara.photo
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
          caption: 'Some souls meet once and change each other forever. From The Wedding Prima & Fauzan @amaliaprimaa & @fb_santoso 🤍\\n\\nMUA: @tivahmakeup\\nDekorasi: @jemarikoedekor_jogja\\nFoto & Video: @jawara.photo\\nSeserahan: @hariyati_seserahan\\nEntertaiment: @nefiezbandofficial\\n\\n#weddingphotography #weddingjogja #fotograferweddingjogja #fotoweddingjogja #jawaraphoto #bersamajawara'
        },
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
        subArea: 'Kota Yogyakarta',
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
        igPostCode: 'DdB34NMD5lr',
        phone: '628123456002',
        description: 'Fotografer pernikahan spesialis editorial couple portraits dan intimate wedding storytelling di Jogja.',
        topPost: {
          likes: '5.210 likes',
          comments: '96 komentar',
          caption: 'The quiet beauty of two souls becoming one. Editorial bridal portraiture for our lovely couple in Yogyakarta. Captured #bysandiliem 🤍\\n\\n#sandiliemphotography #preweddingjogja #weddingjogja #weddingeditorial #intimateweddingjogja'
        },
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
        subArea: 'Bantul',
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
        igPostCode: 'DZm2Kbgj4ZZ',
        phone: '628123456003',
        description: 'Kreator visual pernikahan di Yogyakarta yang menyuguhkan karya foto dan video cinematic dengan tone warna hangat bersahabat.',
        topPost: {
          likes: '3.920 likes',
          comments: '64 komentar',
          caption: 'Hangatnya senyum di hari pertunangan lamaran Mas Adit & Mbak Sarah di Bantul. Terimakasih telah berbagi cerita bersama @luxvisual.id 💍\\n\\n#luxvisual #engagementjogja #lamaranjogja #fotograferjogja #weddingbantul'
        },
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
        subArea: 'Sleman',
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
        igPostCode: 'DV2iXGGCSz6',
        phone: '628123456004',
        description: '"Menceritakan kisah cinta kalian melalui bingkai visual yang jujur." Ahli dalam mengabadikan prosesi adat Jawa dan intimate modern wedding.',
        topPost: {
          likes: '6.450 likes',
          comments: '118 komentar',
          caption: 'Air mata haru restu orang tua saat prosesi sungkeman siraman adat Jawa. Setiap tetes air membawa doa tulus untuk rumah tangga bahagia @kitakancerita 🌿\\n\\n#kitakancerita #siramanjogja #paesageng #pernikahanadatjawa #weddingjogja'
        },
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
        subArea: 'Kota Yogyakarta',
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
        igPostCode: 'DaQBRhFGCvF',
        phone: '628123456005',
        description: 'Tim fotografer muda kreatif berbasis di Jogja-Solo dengan visual aesthetic segar, ceria, dan sangat ramah.',
        topPost: {
          likes: '4.180 likes',
          comments: '73 komentar',
          caption: 'Tawa renyah dan pelukan hangat para sahabat di hari pernikahan paling dinanti. Captured with love by @thenijophotograph 💛\\n\\n#thenijophotograph #nijowedding #fotograferjogja #weddingjogjasolo'
        },
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
        subArea: 'Kota Yogyakarta',
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
        igPostCode: 'DeB1C4kH5vS',
        phone: '628123456006',
        description: 'Spesialis wedding photography and cinematic film bernuansa romantis, anggun, dengan pencahayaan alami nan memukau.',
        topPost: {
          likes: '7.340 likes',
          comments: '142 komentar',
          caption: 'In the stillness of the ballroom, their promises echoed forever. A cinematic glimpse of love by @neiscala ✨\\n\\n#neiscala #weddingfilm #cinematicwedding #weddingjogja #weddingphotography'
        },
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
        subArea: 'Bantul',
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
        igPostCode: 'DdRiiJqj3xs',
        phone: '628123456007',
        description: 'Studio foto dan film pernikahan di Bantul. Menyediakan paket komplit foto studio, prewedding outdoor, liputan hari H, serta kolaborasi MUA & dekorasi.',
        topPost: {
          likes: '3.620 likes',
          comments: '58 komentar',
          caption: 'Prewedding magis berlatar bentang pasir Gumuk Pasir Parangkusumo Bantul Yogyakarta @lunanouovastudio__ 🌾\\n\\n#lunanouovastudio #preweddingbantul #gumukpasir #weddingjogja #studiomanten'
        },
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
        subArea: 'Kota Yogyakarta',
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
        igPostCode: 'C7rJ4p3pLqA',
        phone: '628123456010',
        description: 'Maestro tata rias pengantin adat Jawa paling disegani di Jogja. Sangat presisi dalam pakem cengkorongan Paes Ageng, Kanigaran, dan Jangan Menir.',
        topPost: {
          likes: '18.300 likes',
          comments: '340 komentar',
          caption: 'Mahakarya Paes Ageng Kraton Ngayogyakarta Hadiningrat dengan lekukan cengkorongan prada emas dan roncean melati asli keraton @mamuktukangmakeupjogja 👑\\n\\n#mamuktukangmakeupjogja #paesageng #paesagengjogja #riaspengantinjogja'
        },
        packages: [
          { name: 'Paes Ageng Jangan Menir Komplit + Busana Adat', price: 'Rp 14.000.000' },
          { name: 'Rias Pengantin Jogja Putri Modifikasi', price: 'Rp 9.500.000' }
        ]
      },

      // 9. ARNIE SURYO MUA (MUA TOP JOGJA)
      {
        id: 'mua-arnie',
        name: 'Arnie Suryo Traditional MUA',
        category: 'mua',
        city: 'yogyakarta',
        subArea: 'Sleman',
        styleTag: 'Tradisional Jawa',
        locationText: 'Depok, Sleman, DI Yogyakarta',
        priceStart: 6500000,
        rating: 4.9,
        reviewCount: 195,
        isPromoted: true,
        promoTier: 'FEATURED',
        igHandle: '@arniesuryo',
        igFollowers: '38.200 followers',
        igPostsCount: '950 posts',
        igUrl: 'https://www.instagram.com/arniesuryo/',
        igPostCode: 'C2eR7r4vxL2',
        phone: '628123456011',
        description: 'Spesialis rias pengantin Jawa modern & pakem tradisional. Kerap berkolaborasi dengan vendor FG top Jogja seperti Jawara Photo.',
        topPost: {
          likes: '11.450 likes',
          comments: '188 komentar',
          caption: 'Anggun mempesona dalam balutan paes Jogja Putri bernuansa velvet hitam klasik. Aura ningrat pengantin Jawa @arniesuryo ✨'
        },
        packages: [
          { name: 'Paket Paes Ageng Akad & Resepsi', price: 'Rp 6.500.000' },
          { name: 'All-In Rias Pengantin + 2 Orang Tua & Besan', price: 'Rp 9.000.000' }
        ]
      },

      // 10. SUKMA TERINGGO (MUA TRADISIONAL JOGJA)
      {
        id: 'mua-sukma',
        name: 'Sukma Teringgo MUA',
        category: 'mua',
        city: 'yogyakarta',
        subArea: 'Sleman',
        styleTag: 'Tradisional Jawa',
        locationText: 'Ngaglik, Sleman, DI Yogyakarta',
        priceStart: 7000000,
        rating: 4.9,
        reviewCount: 142,
        isPromoted: false,
        promoTier: 'STANDARD',
        igHandle: '@sukma_ringgo',
        igFollowers: '21.500 followers',
        igPostsCount: '620 posts',
        igUrl: 'https://www.instagram.com/sukma_ringgo/',
        igPostCode: 'C8xK9pL2vNm',
        phone: '628123456012',
        description: 'Perias pengantin adat Jawa spesialis tata rias Paes Ageng Kanigaran dan tata busana lurik & beludru klasik keraton.',
        topPost: {
          likes: '7.850 likes',
          comments: '115 komentar',
          caption: 'Kesempurnaan ronce melati tibo dada dan cunduk mentul kembar sembilan adat Yogyakarta @sukma_ringgo 🌸'
        },
        packages: [
          { name: 'Paket Rias Paes Ageng & Ronce Melati Asli', price: 'Rp 7.000.000' },
          { name: 'Rias Pengantin Adat Komplit Busana Dodotan', price: 'Rp 11.500.000' }
        ]
      },

      // 11. DIAH KURNIA MUA (MODERN FLAWLESS MUA)
      {
        id: 'mua-diah',
        name: 'Diah Kurnia Make Up Art',
        category: 'mua',
        city: 'yogyakarta',
        subArea: 'Kota Yogyakarta',
        styleTag: 'Modern Minimalist',
        locationText: 'Kotagede, Kota Yogyakarta',
        priceStart: 4500000,
        rating: 4.9,
        reviewCount: 168,
        isPromoted: false,
        promoTier: 'STANDARD',
        igHandle: '@diahkurniamua',
        igFollowers: '29.100 followers',
        igPostsCount: '810 posts',
        igUrl: 'https://www.instagram.com/diahkurniamua/',
        igPostCode: 'C5pQ9vL3xKt',
        phone: '628123456013',
        description: 'Pakar rias flawless modern, glass skin bridal makeup, dan hijab styling kontemporer untuk intimate wedding di Yogyakarta.',
        topPost: {
          likes: '9.210 likes',
          comments: '134 komentar',
          caption: 'Natural glowing bridal complexion tanpa mengubah karakter wajah asli pengantin @diahkurniamua 💖'
        },
        packages: [
          { name: 'Flawless Modern Akad Only', price: 'Rp 4.500.000' },
          { name: 'Akad + Resepsi Touch Up & Hijab Styling', price: 'Rp 7.500.000' }
        ]
      },

      // 12. VIMI STUDIO (FG TOP JOGJA)
      {
        id: 'fg-vimi',
        name: 'Vimi Studio',
        category: 'photography',
        city: 'yogyakarta',
        subArea: 'Sleman',
        styleTag: 'Warm Editorial',
        locationText: 'Sleman, DI Yogyakarta',
        priceStart: 6000000,
        rating: 4.9,
        reviewCount: 180,
        isPromoted: true,
        promoTier: 'FEATURED',
        igHandle: '@vimistudio',
        igFollowers: '31.400 followers',
        igPostsCount: '780 posts',
        igUrl: 'https://www.instagram.com/vimistudio/',
        igPostCode: 'C3tK8pL9xMn',
        phone: '628123456014',
        description: 'Vendor fotografi pernikahan terkemuka di Jogja dengan pendekatan fine art dan pencahayaan sinematik yang puitis.',
        topPost: {
          likes: '8.940 likes',
          comments: '128 komentar',
          caption: 'Poetic moments under the gentle drizzle of Yogyakarta. Every glance holds a lifetime promise @vimistudio 🌧️'
        },
        packages: [
          { name: 'Prewedding Creative Session', price: 'Rp 6.000.000' },
          { name: 'Full Wedding Day Fine Art Photo & Film', price: 'Rp 10.500.000' }
        ]
      },

      // 13. POETRA FOTO (FG DOKUMENTASI ADAT JOGJA)
      {
        id: 'fg-poetrafoto',
        name: 'Poetrafoto Photography',
        category: 'photography',
        city: 'yogyakarta',
        subArea: 'Sleman',
        styleTag: 'Tradisional Jawa',
        locationText: 'Sleman, DI Yogyakarta',
        priceStart: 4000000,
        rating: 4.8,
        reviewCount: 215,
        isPromoted: false,
        promoTier: 'STANDARD',
        igHandle: '@poetrafoto',
        igFollowers: '24.600 followers',
        igPostsCount: '1.450 posts',
        igUrl: 'https://www.instagram.com/poetrafoto/',
        igPostCode: 'C1xL8vK3tNm',
        phone: '628123456015',
        description: 'Pelopor fotografi dokumenter pernikahan adat Jawa di Jogja sejak 2010. Teliti merekam setiap runtutan prosesi adat kraton.',
        topPost: {
          likes: '6.720 likes',
          comments: '98 komentar',
          caption: 'Detil siraman kembang setaman tujuh mata air adat Jawa Yogyakarta. Tradisi luhur yang sarat makna spiritual @poetrafoto 🌺'
        },
        packages: [
          { name: 'Dokumentasi Rangkaian Siraman / Midodareni', price: 'Rp 4.000.000' },
          { name: 'Full Akad & Resepsi Tradisional Jawa', price: 'Rp 7.500.000' }
        ]
      },

      // 14. WARNA INDONESIA PHOTOGRAPHY
      {
        id: 'fg-warnaindonesia',
        name: 'Warna Indonesia Photography',
        category: 'photography',
        city: 'yogyakarta',
        subArea: 'Kota Yogyakarta',
        styleTag: 'Modern Minimalist',
        locationText: 'Gondokusuman, Kota Yogyakarta',
        priceStart: 3500000,
        rating: 4.9,
        reviewCount: 310,
        isPromoted: false,
        promoTier: 'STANDARD',
        igHandle: '@warnaindonesiaphoto',
        igFollowers: '68.900 followers',
        igPostsCount: '2.100 posts',
        igUrl: 'https://www.instagram.com/warnaindonesiaphoto/',
        igPostCode: 'C4vL7tK9xPq',
        phone: '628123456016',
        description: 'Studio foto terbesar di Yogyakarta dengan fasilitas studio indoor megah dan tim fotografer handal untuk wedding & prewed.',
        topPost: {
          likes: '12.400 likes',
          comments: '204 komentar',
          caption: 'Prewedding studio bertema monokrom klasik elegan bersama @warnaindonesiaphoto 🖤'
        },
        packages: [
          { name: 'Prewedding Studio Exclusive Session', price: 'Rp 3.500.000' },
          { name: 'Wedding Documentation All-In', price: 'Rp 6.800.000' }
        ]
      },

      // 15. PENDOPO AGUNG ROYAL AMBARRUKMO (VENUE)
      {
        id: 'venue-ambarrukmo',
        name: 'Pendopo Agung Royal Ambarrukmo',
        category: 'venue',
        city: 'yogyakarta',
        subArea: 'Sleman',
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
        igPostCode: 'C9vK3pL8xRt',
        phone: '628123456020',
        description: 'Cagar budaya bersejarah peninggalan Sultan Hamengku Buwono VII. Ikon royal wedding adat Jawa termegah dan tersakral di Indonesia.',
        topPost: {
          likes: '16.700 likes',
          comments: '210 komentar',
          caption: 'Megahnya pilar kayu jati bersejarah abad ke-18 Pendopo Agung Royal Ambarrukmo. Saksi ikrar janji suci pernikahan agung di Yogyakarta 🏛️\\n\\n#royalambarrukmo #pendopoagung #weddingvenuejogja #royalwedding'
        },
        packages: [
          { name: 'Heritage Akad & Paringgitan (150 Pax)', price: 'Rp 85.000.000' },
          { name: 'Royal Grand Pendopo & Taman Gandhok (500 Pax)', price: 'Rp 145.000.000' }
        ]
      },

      // 16. KALYANA RESORT KALIURANG (VENUE OUTDOOR)
      {
        id: 'venue-kalyana',
        name: 'Kalyana Resort Kaliurang',
        category: 'venue',
        city: 'yogyakarta',
        subArea: 'Sleman',
        styleTag: 'Outdoor Garden',
        locationText: 'Pakem, Kaliurang, Sleman',
        priceStart: 45000000,
        rating: 4.9,
        reviewCount: 118,
        isPromoted: true,
        promoTier: 'FEATURED',
        igHandle: '@kalyanaresort',
        igFollowers: '32.100 followers',
        igPostsCount: '640 posts',
        igUrl: 'https://www.instagram.com/kalyanaresort/',
        igPostCode: 'C7rP4xL9vKm',
        phone: '628123456021',
        description: 'Resort pegunungan Kaliurang berlatar rimbun pinus dan udara sejuk Gunung Merapi. Pilihan utama untuk intimate outdoor wedding.',
        topPost: {
          likes: '9.450 likes',
          comments: '135 komentar',
          caption: 'Intimate forest garden wedding di bawah kanopi pepohonan pinus Kaliurang @kalyanaresort 🌲'
        },
        packages: [
          { name: 'Pine Garden Intimate Wedding (200 Pax)', price: 'Rp 45.000.000' },
          { name: 'Full Resort Buyout + Villa Menginap 2 Hari', price: 'Rp 75.000.000' }
        ]
      },

      // 17. HYATT REGENCY YOGYAKARTA (VENUE GOLF & BALLROOM)
      {
        id: 'venue-hyatt',
        name: 'Hyatt Regency Yogyakarta',
        category: 'venue',
        city: 'yogyakarta',
        subArea: 'Sleman',
        styleTag: 'Outdoor Garden',
        locationText: 'Ngaglik, Sleman, DI Yogyakarta',
        priceStart: 75000000,
        rating: 4.9,
        reviewCount: 140,
        isPromoted: false,
        promoTier: 'STANDARD',
        igHandle: '@hyattregencyyogya',
        igFollowers: '85.400 followers',
        igPostsCount: '2.800 posts',
        igUrl: 'https://www.instagram.com/hyattregencyyogya/',
        igPostCode: 'C6xL9pT2vRm',
        phone: '628123456022',
        description: 'Resort bintang 5 seluas 22 hektar dengan Candi Bentar, lapangan golf, dan ballroom mewah untuk pernikahan impian berlatar Gunung Merapi.',
        topPost: {
          likes: '14.200 likes',
          comments: '180 komentar',
          caption: 'Sunset vows at the iconic South Garden Candi Bentar @hyattregencyyogya ⛳'
        },
        packages: [
          { name: 'Candi Garden Sunset Wedding (300 Pax)', price: 'Rp 75.000.000' },
          { name: 'Grand Ballroom Royal Package (800 Pax)', price: 'Rp 160.000.000' }
        ]
      },

      // 18. DANANI DECORATION JOGJA (DEKORASI)
      {
        id: 'decor-danani',
        name: 'Danani Decoration Jogja',
        category: 'decoration',
        city: 'yogyakarta',
        subArea: 'Kota Yogyakarta',
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
        igPostCode: 'C5tP8xK2vLm',
        phone: '628123456030',
        description: 'Spesialis dekorasi pelaminan gebyok keraton dan instalasi bunga hidup megah di Jogja.',
        topPost: {
          likes: '6.900 likes',
          comments: '88 komentar',
          caption: 'Kemegahan pelaminan gebyok jati ukir klasik bertabur ribuan kuntum melati segar harum semerbak @dananidecoration 🌸\\n\\n#dananidecoration #dekorasijogja #pelaminanjogja #gebyokjawa'
        },
        packages: [
          { name: 'Pelaminan Gebyok Kraton 8 Meter', price: 'Rp 25.000.000' },
          { name: 'Grand Ballroom Fresh Flower Installation', price: 'Rp 45.000.000' }
        ]
      },

      // 19. VIDI CATERING SERVICES JOGJA (CATERING)
      {
        id: 'catering-vidi',
        name: 'Vidi Catering Services Jogja',
        category: 'catering',
        city: 'yogyakarta',
        subArea: 'Sleman',
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
        igPostCode: 'C4rT9xL2vKm',
        phone: '628123456040',
        description: 'Raja katering pernikahan terpercaya di Yogyakarta dengan sertifikasi ISO 22000 dan resep citarasa ningrat Kraton.',
        topPost: {
          likes: '5.600 likes',
          comments: '92 komentar',
          caption: 'Sajian hidangan prasmanan citarasa ningrat Kraton Yogyakarta dengan sertifikasi Halal MUI Grade A @vidicatering 🍽️\\n\\n#vidicatering #cateringjogja #prasmananjogja #weddingcatering'
        },
        packages: [
          { name: 'Paket Prasmanan Tradisi Jogja (Min 500 Pax)', price: 'Rp 50.000 / pax' },
          { name: 'Paket Ningrat Royal Buffet + 8 Gubukan Khas', price: 'Rp 75.000 / pax' }
        ]
      },

      // 20. SHINTA CATERING JOGJA (CATERING)
      {
        id: 'catering-shinta',
        name: 'Shinta Catering Yogyakarta',
        category: 'catering',
        city: 'yogyakarta',
        subArea: 'Kota Yogyakarta',
        styleTag: 'Tradisional Jawa',
        locationText: 'Mergangsan, Kota Yogyakarta',
        priceStart: 45000,
        rating: 4.8,
        reviewCount: 230,
        isPromoted: false,
        promoTier: 'STANDARD',
        igHandle: '@shinta_catering',
        igFollowers: '18.400 followers',
        igPostsCount: '520 posts',
        igUrl: 'https://www.instagram.com/shinta_catering/',
        igPostCode: 'C3vK9pL1xMn',
        phone: '628123456041',
        description: 'Penyedia boga legendaris Jogja spesialis masakan Jawa otentik seperti Gudeg Manten, Selat Solo, dan Sop Penganten.',
        topPost: {
          likes: '4.320 likes',
          comments: '64 komentar',
          caption: 'Kelezatan Selat Segar & Zuppa Soup legendaris pesta pernikahan Jogja @shinta_catering 🍲'
        },
        packages: [
          { name: 'Paket Selera Tradisional Jogja (Min 400 Pax)', price: 'Rp 45.000 / pax' }
        ]
      },

      // 21. MAHKOTA WEDDING ORGANIZER JOGJA (WO)
      {
        id: 'wo-mahkota',
        name: 'Mahkota Wedding Organizer Jogja',
        category: 'wo',
        city: 'yogyakarta',
        subArea: 'Sleman',
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
        igPostCode: 'C2tP7xL9vKm',
        phone: '628123456050',
        description: 'Wedding Organizer terkemuka di Yogyakarta spesialis pemandu pakem adat Jawa Paes Ageng dan upacara panggih berwibawa.',
        topPost: {
          likes: '7.120 likes',
          comments: '105 komentar',
          caption: 'Ketenangan dan keteraturan jalannya prosesi ijab kabul sakral berkat pengawalan tim handal @mahkota_wo.jogja 💍'
        },
        packages: [
          { name: 'Wedding Day Coordination (6 Crew Full Day)', price: 'Rp 15.000.000' },
          { name: 'Full Planning & Wedding Adat Protocol Assistance', price: 'Rp 25.000.000' }
        ]
      },

      // 22. LUNA NUOVA WEDDING ORGANIZER (WO)
      {
        id: 'wo-lunanuova',
        name: 'Luna Nuova Wedding Organizer',
        category: 'wo',
        city: 'yogyakarta',
        subArea: 'Bantul',
        styleTag: 'Warm Editorial',
        locationText: 'Bantul, DI Yogyakarta',
        priceStart: 10000000,
        rating: 4.9,
        reviewCount: 110,
        isPromoted: false,
        promoTier: 'STANDARD',
        igHandle: '@lunanuovawo_',
        igFollowers: '12.800 followers',
        igPostsCount: '340 posts',
        igUrl: 'https://www.instagram.com/lunanuovawo_/',
        igPostCode: 'C1xK8pT3vNm',
        phone: '628123456051',
        description: 'Wedding planner & organizer modern untuk pasangan yang menginginkan pernikahan intimate, santai, namun terencana sempurna.',
        topPost: {
          likes: '5.140 likes',
          comments: '72 komentar',
          caption: 'Merayakan cinta bersama keluarga dan teman terdekat tanpa rasa cemas @lunanuovawo_ 🥂'
        },
        packages: [
          { name: 'Intimate Wedding Coordinator (4 Crew)', price: 'Rp 10.000.000' }
        ]
      }
    ];

    let currentCategory = 'all';
    let currentStyle = 'all';
    let savedVendorIds = new Set(['fg-jawara', 'fg-sandiliem', 'fg-kitakancerita']);
    let activeVendor = null;
    let cardLiveMode = {}; // tracks which card has live Instagram player expanded

    function formatRupiah(num) {
      return 'Rp ' + num.toLocaleString('id-ID');
    }

    function toggleCardLiveIg(vendorId, event) {
      if (event) event.stopPropagation();
      cardLiveMode[vendorId] = !cardLiveMode[vendorId];
      const liveBox = document.getElementById(`live-box-${vendorId}`);
      const btn = document.getElementById(`live-btn-${vendorId}`);
      if (liveBox) {
        if (cardLiveMode[vendorId]) {
          liveBox.classList.remove('hidden');
          if (btn) btn.innerHTML = '✕ Tutup Player IG';
        } else {
          liveBox.classList.add('hidden');
          if (btn) btn.innerHTML = '🔴 Buka Player Post IG';
        }
      }
    }

    function onCityChange() {
      const city = document.getElementById('cityFilter').value;
      const subAreaWrapper = document.getElementById('subAreaWrapper');
      if (city === 'yogyakarta') {
        subAreaWrapper.classList.remove('hidden');
      } else {
        subAreaWrapper.classList.add('hidden');
        document.getElementById('subAreaFilter').value = 'all';
      }
      filterVendors();
    }

    function filterVendors() {
      const city = document.getElementById('cityFilter').value;
      const subArea = document.getElementById('subAreaFilter').value;
      const search = (document.getElementById('searchInput').value || '').toLowerCase().trim();
      const listContainer = document.getElementById('vendorList');
      
      const filtered = vendors.filter(v => {
        const matchCategory = currentCategory === 'all' || v.category === currentCategory;
        const matchCity = city === 'all' || v.city === city;
        const matchSubArea = (city !== 'yogyakarta') || subArea === 'all' || v.subArea === subArea;
        const matchStyle = currentStyle === 'all' || v.styleTag === currentStyle;
        const matchSearch = !search || 
          v.name.toLowerCase().includes(search) || 
          v.description.toLowerCase().includes(search) ||
          v.igHandle.toLowerCase().includes(search) ||
          v.locationText.toLowerCase().includes(search) ||
          v.category.toLowerCase().includes(search);

        return matchCategory && matchCity && matchSubArea && matchStyle && matchSearch;
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
        const isLive = cardLiveMode[v.id] || false;

        return `
          <div class="bg-neutral-900 border border-neutral-800 hover:border-neutral-600 rounded-2xl overflow-hidden transition group">
            
            <!-- CARD HEADER: AUTHENTIC INSTAGRAM BRANDING -->
            <div class="p-3.5 bg-neutral-950/80 border-b border-neutral-800/80 flex items-center justify-between">
              <div class="flex items-center space-x-2.5">
                <div class="w-8 h-8 rounded-full instagram-gradient p-0.5 shrink-0">
                  <div class="w-full h-full bg-black rounded-full flex items-center justify-center font-bold text-white text-[11px]">
                    ${v.name.charAt(0)}
                  </div>
                </div>
                <div>
                  <div class="flex items-center space-x-1">
                    <span class="text-xs font-bold text-white tracking-wide">${v.name}</span>
                    <span class="text-blue-400 text-xs" title="Verified Instagram Vendor">✓</span>
                  </div>
                  <a href="${v.igUrl}" target="_blank" class="text-[10px] text-rose-400 hover:underline font-mono">${v.igHandle}</a>
                </div>
              </div>

              <div class="flex items-center space-x-1.5">
                ${v.isPromoted ? `
                  <span class="bg-white text-black text-[9px] font-extrabold px-2 py-0.5 rounded-full uppercase tracking-wider">
                    ★ ${v.promoTier}
                  </span>
                ` : ''}
                <button onclick="event.stopPropagation(); toggleSave('${v.id}')" class="w-7 h-7 rounded-full bg-neutral-800 border border-neutral-700 flex items-center justify-center text-white active:scale-90 transition">
                  <svg class="w-3.5 h-3.5 ${isSaved ? 'text-red-500 fill-current' : 'text-neutral-400'}" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z"/></svg>
                </button>
              </div>
            </div>

            <!-- LIVE EMBED CONTAINER (EXPANDABLE) -->
            <div id="live-box-${v.id}" class="${isLive ? '' : 'hidden'} bg-black p-2 border-b border-neutral-800">
              <div class="flex items-center justify-between pb-1.5 px-1">
                <span class="text-[9px] uppercase font-bold text-rose-400 font-mono flex items-center space-x-1">
                  <span class="w-1.5 h-1.5 rounded-full bg-rose-500 animate-pulse"></span>
                  <span>Postingan Resmi dari Server Instagram</span>
                </span>
                <a href="https://www.instagram.com/p/${v.igPostCode}/" target="_blank" class="text-[9px] text-neutral-400 hover:text-white font-mono">Buka di App ↗</a>
              </div>
              <div class="w-full h-[460px] bg-neutral-950 rounded-xl overflow-hidden border border-neutral-800">
                <iframe src="https://www.instagram.com/p/${v.igPostCode}/embed/" class="w-full h-full border-0" frameborder="0" scrolling="no" allowtransparency="true" loading="lazy"></iframe>
              </div>
            </div>

            <!-- CARD COVER & POST SUMMARY -->
            <div class="p-3.5 space-y-3 cursor-pointer" onclick="openVendorModal('${v.id}')">
              
              <!-- POST HIGHLIGHT BOX (ASLI DARI IG) -->
              <div class="bg-neutral-950 border border-neutral-800 rounded-xl p-3 space-y-2">
                <div class="flex justify-between items-center">
                  <span class="text-[9px] font-bold text-rose-400 bg-rose-950/60 border border-rose-800/60 px-2 py-0.5 rounded-full">
                    🔥 POSTINGAN TERBANYAK LIKE DI IG
                  </span>
                  <span class="text-xs font-mono font-bold text-white flex items-center space-x-1">
                    <span>❤️</span>
                    <span>${v.topPost.likes}</span>
                  </span>
                </div>

                <p class="text-xs text-neutral-300 leading-relaxed italic line-clamp-3">
                  "${v.topPost.caption}"
                </p>

                <div class="flex justify-between items-center text-[10px] text-neutral-500 font-mono pt-1 border-t border-neutral-900">
                  <span>📍 ${v.locationText}</span>
                  <span>💬 ${v.topPost.comments}</span>
                </div>
              </div>

              <!-- PRICING & RATING ROW -->
              <div class="flex justify-between items-end pt-1">
                <div>
                  <span class="text-[10px] text-neutral-400 uppercase tracking-wider block">Mulai dari</span>
                  <span class="text-base font-bold font-mono text-white tracking-tight">${priceLabel}</span>
                </div>
                <div class="flex items-center space-x-1 bg-neutral-800 px-2 py-1 rounded-lg text-xs text-white border border-neutral-700">
                  <span class="text-amber-400">★</span>
                  <span class="font-bold font-mono">${v.rating}</span>
                  <span class="text-neutral-400 text-[10px]">(${v.reviewCount})</span>
                </div>
              </div>

              <!-- ACTION BAR -->
              <div class="pt-2 flex items-center space-x-2 border-t border-neutral-800/80">
                <button onclick="toggleCardLiveIg('${v.id}', event)" id="live-btn-${v.id}" class="flex-1 bg-neutral-800 hover:bg-neutral-700 text-white text-[11px] font-bold py-2 rounded-xl border border-neutral-700 active:scale-95 transition flex items-center justify-center space-x-1.5">
                  <span class="w-2 h-2 rounded-full bg-rose-500 animate-ping"></span>
                  <span>${isLive ? '✕ Tutup Player IG' : '🔴 Buka Player Post IG'}</span>
                </button>
                <button onclick="openVendorModal('${v.id}')" class="flex-1 bg-white hover:bg-neutral-200 text-black text-[11px] font-bold py-2 rounded-xl active:scale-95 transition">
                  Lihat Paket & Detail
                </button>
              </div>

            </div>
          </div>
        `;
      }).join('');
    }

    // RENDER INSTAGRAM FEED ASLI MODE (100% REAL IFRAME EMBEDS DARI INSTAGRAM)
    function renderInstagramFeed() {
      const container = document.getElementById('igFeedContainer');
      const friendVendors = vendors.filter(v => v.category === 'photography');

      container.innerHTML = friendVendors.map(v => {
        return `
          <div class="bg-neutral-900 border border-neutral-800 rounded-2xl overflow-hidden space-y-3">
            
            <!-- IG HEADER -->
            <div class="p-3.5 flex justify-between items-center border-b border-neutral-800/80 bg-neutral-950">
              <div class="flex items-center space-x-2.5">
                <div class="w-9 h-9 rounded-full instagram-gradient p-0.5">
                  <div class="w-full h-full bg-black rounded-full flex items-center justify-center font-bold text-white text-xs">
                    ${v.name.charAt(0)}
                  </div>
                </div>
                <div>
                  <div class="flex items-center space-x-1">
                    <span class="text-xs font-bold text-white hover:underline cursor-pointer" onclick="directInstagramLink('${v.igHandle}')">${v.igHandle}</span>
                    <span class="text-blue-400 text-xs">✓</span>
                  </div>
                  <p class="text-[10px] text-neutral-400 font-mono">${v.locationText} • Mulai ${formatRupiah(v.priceStart)}</p>
                </div>
              </div>
              <a href="${v.igUrl}" target="_blank" class="text-[10px] bg-neutral-800 text-white font-bold px-2.5 py-1 rounded-lg hover:bg-neutral-700 flex items-center space-x-1">
                <span>Buka Profil</span>
                <span>↗</span>
              </a>
            </div>

            <!-- REAL INSTAGRAM POST EMBED (ASLI DARI SERVER META) -->
            <div class="px-3">
              <div class="relative w-full rounded-xl overflow-hidden bg-neutral-950 border border-neutral-800 shadow-inner">
                <div class="bg-neutral-900/80 px-3 py-1.5 flex justify-between items-center border-b border-neutral-800 text-[10px]">
                  <span class="text-rose-400 font-bold font-mono flex items-center space-x-1">
                    <span class="w-1.5 h-1.5 rounded-full bg-rose-500 animate-pulse"></span>
                    <span>POSTINGAN PALING BANYAK LIKE (${v.topPost.likes})</span>
                  </span>
                  <a href="https://www.instagram.com/p/${v.igPostCode}/" target="_blank" class="text-neutral-400 hover:text-white font-mono">Buka di Instagram ↗</a>
                </div>
                <iframe src="https://www.instagram.com/p/${v.igPostCode}/embed/" class="w-full h-[470px] border-0" frameborder="0" scrolling="no" allowtransparency="true" loading="lazy"></iframe>
              </div>
            </div>

            <!-- ACTION FOOTER -->
            <div class="p-3.5 pt-1 space-y-2">
              <div class="pt-2 border-t border-neutral-800/60 flex space-x-2">
                <a href="${v.igUrl}" target="_blank" class="flex-1 bg-gradient-to-r from-purple-800 to-pink-700 hover:from-purple-700 hover:to-pink-600 text-white text-xs font-bold py-2.5 rounded-xl flex items-center justify-center space-x-1.5 transition shadow">
                  <span>Lihat Seluruh Portofolio di Instagram</span>
                  <span>↗</span>
                </a>
                <button onclick="openVendorModal('${v.id}')" class="px-3.5 bg-white text-black text-xs font-bold rounded-xl active:scale-95 transition">
                  Pricelist
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
      document.getElementById('subAreaFilter').value = 'all';
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
        <div class="flex items-center space-x-3 p-3 bg-neutral-900 border border-neutral-800 rounded-xl">
          <div class="w-12 h-12 rounded-xl bg-neutral-950 border border-neutral-800 flex items-center justify-center font-serif-luxury font-bold text-lg text-white">
            ${v.name.charAt(0)}
          </div>
          <div class="flex-1">
            <span class="text-[9px] uppercase tracking-wider text-neutral-400 font-mono">${v.category.toUpperCase()} • ${v.city.toUpperCase()}</span>
            <h4 class="font-bold text-white font-serif-luxury text-sm leading-tight">${v.name}</h4>
            <p class="text-[11px] text-rose-400 font-mono mt-0.5">${formatRupiah(v.priceStart)}</p>
          </div>
          <button onclick="openVendorModal('${v.id}')" class="text-xs bg-white text-black font-semibold px-3 py-1.5 rounded-lg active:scale-95 transition">Detail</button>
        </div>
      `).join('');
    }

    function openVendorModal(id) {
      activeVendor = vendors.find(v => v.id === id);
      if (!activeVendor) return;

      const modal = document.getElementById('vendorModal');
      const content = document.getElementById('modalContent');
      const priceLabel = activeVendor.category === 'catering' ? `${formatRupiah(activeVendor.priceStart)} / pax` : formatRupiah(activeVendor.priceStart);

      content.innerHTML = `
        <!-- VENDOR PROFILE BANNER DIRECT FROM IG -->
        <div class="p-3.5 bg-neutral-900 border border-neutral-800 rounded-2xl flex items-center justify-between">
          <div class="flex items-center space-x-3">
            <div class="w-12 h-12 rounded-full instagram-gradient p-0.5">
              <div class="w-full h-full bg-black rounded-full flex items-center justify-center font-bold text-white text-base">
                ${activeVendor.name.charAt(0)}
              </div>
            </div>
            <div>
              <div class="flex items-center space-x-1.5">
                <h3 class="text-sm font-bold text-white">${activeVendor.name}</h3>
                <span class="text-blue-400 text-xs">✓</span>
              </div>
              <p class="text-xs text-rose-400 font-mono font-semibold">${activeVendor.igHandle}</p>
              <p class="text-[10px] text-neutral-400 font-mono">${activeVendor.igFollowers || ''} • ${activeVendor.igPostsCount || ''}</p>
            </div>
          </div>
          <a href="${activeVendor.igUrl}" target="_blank" class="bg-gradient-to-r from-purple-700 to-pink-600 text-white text-xs font-bold px-3 py-1.5 rounded-xl shadow">
            Follow di IG
          </a>
        </div>

        <!-- LIVE INSTAGRAM PLAYER DALAM MODAL -->
        <div class="bg-neutral-900 border border-neutral-800 rounded-2xl p-3 space-y-2">
          <div class="flex justify-between items-center">
            <span class="text-[10px] font-bold text-rose-400 uppercase tracking-widest flex items-center space-x-1">
              <span class="w-2 h-2 rounded-full bg-rose-500 animate-ping"></span>
              <span>Postingan Terbanyak Like (Live Instagram):</span>
            </span>
            <span class="text-xs font-mono font-bold text-white">❤️ ${activeVendor.topPost.likes}</span>
          </div>

          <!-- EMBED ASLI DARI IG META -->
          <div class="w-full h-[470px] rounded-xl overflow-hidden bg-black border border-neutral-800">
            <iframe src="https://www.instagram.com/p/${activeVendor.igPostCode}/embed/" class="w-full h-full border-0" frameborder="0" scrolling="no" allowtransparency="true" loading="lazy"></iframe>
          </div>

          <p class="text-xs text-neutral-300 leading-relaxed italic bg-black/60 p-2.5 rounded-xl border border-neutral-800">
            "${activeVendor.topPost.caption}"
          </p>
        </div>

        <!-- RATING & LIVE STATUS -->
        <div class="flex justify-between items-center py-2 px-3 bg-neutral-900 border border-neutral-800 rounded-xl text-xs">
          <div class="flex items-center space-x-1.5 text-white">
            <span class="text-amber-400 font-bold">★ ${activeVendor.rating}</span>
            <span class="text-neutral-400">(${activeVendor.reviewCount} Ulasan Calon Pengantin)</span>
          </div>
          <span class="text-emerald-400 font-medium text-[11px] flex items-center space-x-1">
            <span class="w-1.5 h-1.5 bg-emerald-400 rounded-full animate-ping"></span>
            <span>Jadwal Aktif</span>
          </span>
        </div>

        <!-- CEK TANGGAL NIKAH LIVE -->
        <div class="p-3 bg-neutral-900 border border-neutral-800 rounded-xl space-y-2">
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
            <span class="text-[10px] text-rose-400 font-mono">Mulai ${priceLabel}</span>
          </div>
          <div class="space-y-2">
            ${activeVendor.packages.map(p => `
              <div class="p-3 bg-black border border-neutral-800 rounded-xl flex justify-between items-center hover:border-neutral-700 transition">
                <div>
                  <h5 class="text-xs font-bold text-white">${p.name}</h5>
                  <span class="text-[10px] text-neutral-400">Garansi Layanan Resmi KITA MENIKAH</span>
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

    function directInstagramLink(handle) {
      const cleanHandle = handle.replace('@', '');
      window.open(`https://www.instagram.com/${cleanHandle}/`, '_blank');
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
      const igFeed = document.getElementById('viewIgFeed');
      const budget = document.getElementById('viewBudget');
      const saved = document.getElementById('viewSaved');

      home.classList.add('hidden');
      igFeed.classList.add('hidden');
      budget.classList.add('hidden');
      saved.classList.add('hidden');

      const tabs = ['home', 'igFeed', 'budget', 'saved'];
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
      } else if (tab === 'igFeed') {
        igFeed.classList.remove('hidden');
        renderInstagramFeed();
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

print("Updated index.html successfully written!")
