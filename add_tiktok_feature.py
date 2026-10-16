import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Update <nav> to include TikTok icon right beside Home
old_nav = """    <!-- BOTTOM APP NAVIGATION DOCK (BERSIH 3 MENU: EKSPLOR, BUDGET, TERSIMPAN) -->
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
    </nav>"""

new_nav = """    <!-- BOTTOM APP NAVIGATION DOCK (4 MENU: EKSPLOR, TIKTOK WEDDING, BUDGET, TERSIMPAN) -->
    <nav class="absolute bottom-0 left-0 right-0 h-16 bg-black/95 backdrop-blur border-t border-neutral-900 flex justify-around items-center px-3 z-40">
      
      <!-- 1. IKON RUMAH (EKSPLOR) -->
      <button onclick="switchTab('home')" id="navHome" class="flex flex-col items-center justify-center space-y-1 text-white px-2">
        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6"/></svg>
        <span class="text-[10px] font-semibold tracking-wider">Eksplor</span>
      </button>

      <!-- 2. IKON TIKTOK (PERSIS DI SAMPING IKON RUMAH - KONTEN WEDDING INDONESIA) -->
      <button onclick="switchTab('tiktok')" id="navTikTok" class="flex flex-col items-center justify-center space-y-1 text-neutral-500 hover:text-white transition group px-2 relative">
        <div class="relative">
          <svg class="w-5 h-5 transition group-hover:scale-110" viewBox="0 0 24 24" fill="currentColor">
            <path d="M19.59 6.69a4.83 4.83 0 0 1-3.77-4.25V2h-3.45v13.67a2.89 2.89 0 0 1-5.2 1.74 2.89 2.89 0 0 1 2.31-4.64 2.93 2.93 0 0 1 .88.13V9.4a6.84 6.84 0 0 0-1-.05A6.33 6.33 0 0 0 5 20.1a6.34 6.34 0 0 0 10.86-4.43v-7a8.16 8.16 0 0 0 4.77 1.52v-3.4a4.85 4.85 0 0 1-1.04-.1z"/>
          </svg>
          <span class="absolute -top-1 -right-1 w-2 h-2 rounded-full bg-red-500 animate-pulse"></span>
        </div>
        <span class="text-[10px] font-semibold tracking-wider flex items-center space-x-0.5">
          <span>TikTok</span>
        </span>
      </button>

      <!-- 3. BUDGET -->
      <button onclick="switchTab('budget')" id="navBudget" class="flex flex-col items-center justify-center space-y-1 text-neutral-500 hover:text-white transition px-2">
        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 7h6m0 10v-3m-3 3h.01M9 17h.01M9 14h.01M12 14h.01M15 11h.01M12 11h.01M9 11h.01M7 21h10a2 2 0 002-2V5a2 2 0 00-2-2H7a2 2 0 00-2 2v14a2 2 0 002 2z"/></svg>
        <span class="text-[10px] font-semibold tracking-wider">Budget</span>
      </button>

      <!-- 4. TERSIMPAN -->
      <button onclick="switchTab('saved')" id="navSaved" class="flex flex-col items-center justify-center space-y-1 text-neutral-500 hover:text-white transition px-2">
        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z"/></svg>
        <span class="text-[10px] font-semibold tracking-wider">Tersimpan</span>
      </button>
    </nav>"""

if old_nav in html:
    html = html.replace(old_nav, new_nav)
    print("Updated bottom nav with TikTok icon beside home!")
else:
    print("Could not match old_nav directly, using regex replace...")
    html = re.sub(r'<!-- BOTTOM APP NAVIGATION DOCK.*?<nav.*?</nav>', new_nav, html, flags=re.DOTALL)
    print("Replaced nav with new_nav via regex!")

# 2. Add VIEW 5: viewTikTok right before the closing </div> of main container
tiktok_view_html = """
      <!-- VIEW 5: TIKTOK WEDDING INDONESIA (FYP & REELS KHUSUS INSPIRASI WEDDING INDO) -->
      <div id="viewTikTok" class="hidden pb-20 space-y-4">
        
        <!-- TIKTOK TOP BAR & CLIENT ACCOUNT CONNECTION -->
        <div class="px-5 pt-3 space-y-3 bg-gradient-to-b from-neutral-950 via-black to-black border-b border-neutral-900 pb-3">
          <div class="flex justify-between items-center">
            <div class="flex items-center space-x-2">
              <div class="w-7 h-7 rounded-full bg-gradient-to-tr from-cyan-400 via-pink-500 to-red-500 p-0.5">
                <div class="w-full h-full rounded-full bg-black flex items-center justify-center text-white">
                  <svg class="w-3.5 h-3.5" viewBox="0 0 24 24" fill="currentColor">
                    <path d="M19.59 6.69a4.83 4.83 0 0 1-3.77-4.25V2h-3.45v13.67a2.89 2.89 0 0 1-5.2 1.74 2.89 2.89 0 0 1 2.31-4.64 2.93 2.93 0 0 1 .88.13V9.4a6.84 6.84 0 0 0-1-.05A6.33 6.33 0 0 0 5 20.1a6.34 6.34 0 0 0 10.86-4.43v-7a8.16 8.16 0 0 0 4.77 1.52v-3.4a4.85 4.85 0 0 1-1.04-.1z"/>
                  </svg>
                </div>
              </div>
              <div>
                <h2 class="text-sm font-bold text-white tracking-wide flex items-center space-x-1.5">
                  <span>TikTok Wedding Indo</span>
                  <span class="text-[9px] bg-red-500/20 text-red-400 border border-red-500/30 px-1.5 py-0.2 rounded font-mono font-bold">FYP</span>
                </h2>
                <p class="text-[10px] text-neutral-400">100% Konten Pernikahan Tradisional & Modern Indonesia</p>
              </div>
            </div>

            <!-- TAUTKAN AKUN TIKTOK KLIEN -->
            <button onclick="openTikTokConnectModal()" id="btnConnectTikTok" class="px-3 py-1.5 rounded-full bg-gradient-to-r from-cyan-500/20 via-pink-500/20 to-red-500/20 border border-pink-500/40 text-pink-300 hover:text-white text-[10px] font-bold transition flex items-center space-x-1 shadow-sm active:scale-95">
              <span id="labelConnectTikTok">🔗 Tautkan TikTok</span>
            </button>
          </div>

          <!-- STATUS AKUN TIKTOK KLIEN (JIKA SUDAH TERHUBUNG) -->
          <div id="boxConnectedTikTok" class="bg-neutral-900/90 border border-neutral-800 rounded-2xl p-2.5 flex items-center justify-between">
            <div class="flex items-center space-x-2.5">
              <div class="w-8 h-8 rounded-full bg-gradient-to-tr from-cyan-500 via-pink-500 to-red-500 p-0.5 shrink-0">
                <img id="avatarClientTikTok" src="assets/vendors/avatars/jawara.jpg" class="w-full h-full rounded-full object-cover">
              </div>
              <div>
                <div class="flex items-center space-x-1">
                  <span id="handleClientTikTok" class="text-xs font-bold text-white font-mono">@klien.kitamenikah</span>
                  <span class="text-cyan-400 text-[10px]" title="Terhubung">✓</span>
                </div>
                <span class="text-[9px] text-neutral-400 font-sans block">Akun TikTok Klien Terhubung • Wishlist & Video Disinkronkan</span>
              </div>
            </div>
            <a href="https://www.tiktok.com/tag/weddingjogja" target="_blank" rel="noopener noreferrer" class="text-[10px] bg-neutral-800 hover:bg-neutral-700 text-neutral-200 hover:text-white px-2.5 py-1 rounded-xl border border-neutral-700 font-medium">
              Buka FYP ↗
            </a>
          </div>

          <!-- HASHTAG WEDDING TRENDING TIKTOK INDO -->
          <div class="flex space-x-1.5 overflow-x-auto no-scrollbar pb-1 text-[10px] font-mono">
            <span class="px-2.5 py-1 rounded-full bg-neutral-900 border border-neutral-800 text-neutral-300 whitespace-nowrap">🔥 #WeddingJogja</span>
            <span class="px-2.5 py-1 rounded-full bg-neutral-900 border border-neutral-800 text-neutral-300 whitespace-nowrap">✨ #PaesAgeng</span>
            <span class="px-2.5 py-1 rounded-full bg-neutral-900 border border-neutral-800 text-neutral-300 whitespace-nowrap">🤍 #AkadNikahHaru</span>
            <span class="px-2.5 py-1 rounded-full bg-neutral-900 border border-neutral-800 text-neutral-300 whitespace-nowrap">🍽️ #CateringWedding</span>
            <span class="px-2.5 py-1 rounded-full bg-neutral-900 border border-neutral-800 text-neutral-300 whitespace-nowrap">👰 #SpillGaunPengantin</span>
          </div>
        </div>

        <!-- TIKTOK REELS VERTICAL FEED (KONTEN WEDDING INDO OTENTIK) -->
        <div id="tiktokFeedContainer" class="px-4 space-y-5">
          
          <!-- REEL 1: PAES AGENG MAMUK MAKEUP -->
          <div class="relative w-full rounded-3xl overflow-hidden bg-neutral-950 border border-neutral-800 shadow-2xl">
            <!-- Background Image Poster (Paes Ageng Asli) -->
            <div class="relative w-full aspect-[9/14] overflow-hidden">
              <img src="assets/vendors/slides/mamuk_slide_1.jpg" class="w-full h-full object-cover">
              
              <!-- Gradient Vignette -->
              <div class="absolute inset-0 bg-gradient-to-t from-black via-black/25 to-black/30 pointer-events-none"></div>

              <!-- Top Reels Tag -->
              <div class="absolute top-3 left-3 flex items-center space-x-2">
                <span class="bg-black/70 backdrop-blur text-white border border-white/20 text-[9px] font-bold px-2.5 py-0.5 rounded-full flex items-center space-x-1">
                  <span class="w-1.5 h-1.5 rounded-full bg-red-500 animate-ping"></span>
                  <span>TIKTOK VIRAL INDO</span>
                </span>
                <span class="bg-pink-950/80 text-pink-300 border border-pink-500/30 text-[9px] px-2 py-0.5 rounded-full font-mono">
                  #PaesAgengJogja
                </span>
              </div>

              <!-- Right Action Sidebar (TikTok Style: Like, Comment, Bookmark, Share, Music Vinyl) -->
              <div class="absolute right-3 bottom-14 flex flex-col items-center space-y-3.5 z-20">
                
                <!-- Creator Avatar with Follow Plus -->
                <div class="relative">
                  <div class="w-10 h-10 rounded-full border-2 border-white overflow-hidden bg-neutral-900 shadow">
                    <img src="assets/vendors/avatars/mamuk.jpg" class="w-full h-full object-cover">
                  </div>
                  <button onclick="toggleFollowTikTok(this)" class="absolute -bottom-1.5 left-1/2 -translate-x-1/2 w-4 h-4 rounded-full bg-red-500 text-white flex items-center justify-center text-[10px] font-bold shadow">
                    +
                  </button>
                </div>

                <!-- Like Button -->
                <button onclick="toggleTikTokLike(this, 148200)" class="flex flex-col items-center space-y-0.5 group">
                  <div class="w-10 h-10 rounded-full bg-black/50 backdrop-blur border border-white/20 flex items-center justify-center text-white group-hover:scale-110 active:scale-90 transition">
                    <svg class="w-5 h-5 heart-icon transition" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z"/></svg>
                  </div>
                  <span class="text-[10px] text-white font-mono font-bold count-label">148.2K</span>
                </button>

                <!-- Comment Button -->
                <button onclick="showTikTokComments('Mamuk Tukang Makeup')" class="flex flex-col items-center space-y-0.5 group">
                  <div class="w-10 h-10 rounded-full bg-black/50 backdrop-blur border border-white/20 flex items-center justify-center text-white group-hover:scale-110 transition">
                    <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 12h.01M12 12h.01M16 12h.01M21 12c0 4.418-4.03 8-9 8a9.863 9.863 0 01-4.255-.949L3 20l1.395-3.72C3.512 15.042 3 13.574 3 12c0-4.418 4.03-8 9-8s9 3.582 9 8z"/></svg>
                  </div>
                  <span class="text-[10px] text-white font-mono font-bold">2.418</span>
                </button>

                <!-- Save/Bookmark Button -->
                <button onclick="toggleTikTokBookmark(this)" class="flex flex-col items-center space-y-0.5 group">
                  <div class="w-10 h-10 rounded-full bg-black/50 backdrop-blur border border-white/20 flex items-center justify-center text-white group-hover:scale-110 transition">
                    <svg class="w-5 h-5 bookmark-icon" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 5a2 2 0 012-2h10a2 2 0 012 2v16l-7-3.5L5 21V5z"/></svg>
                  </div>
                  <span class="text-[10px] text-white font-mono font-bold">19.3K</span>
                </button>

                <!-- Share Button -->
                <a href="https://www.tiktok.com/@mamuktukangmakeupjogja" target="_blank" rel="noopener noreferrer" class="flex flex-col items-center space-y-0.5 group">
                  <div class="w-10 h-10 rounded-full bg-black/50 backdrop-blur border border-white/20 flex items-center justify-center text-white group-hover:scale-110 transition">
                    <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8.684 13.342C8.886 12.938 9 12.482 9 12c0-.482-.114-.938-.316-1.342m0 2.684a3 3 0 110-2.684m0 2.684l6.632 3.316m-6.632-6l6.632-3.316m0 0a3 3 0 105.367-2.684 3 3 0 00-5.367 2.684zm0 9.316a3 3 0 105.368 2.684 3 3 0 00-5.368-2.684z"/></svg>
                  </div>
                  <span class="text-[9px] text-neutral-300 font-mono">Share</span>
                </a>

                <!-- Spinning Vinyl Music Disc -->
                <div class="w-10 h-10 rounded-full bg-neutral-900 border-2 border-neutral-700 flex items-center justify-center animate-spin" style="animation-duration: 6s;">
                  <div class="w-4 h-4 rounded-full bg-red-500 border border-white"></div>
                </div>

              </div>

              <!-- Bottom Content Overlay (Caption, Audio, Link to Vendor) -->
              <div class="absolute bottom-3 left-3 right-16 space-y-2 z-20">
                <div class="flex items-center space-x-1.5">
                  <span class="text-xs font-bold text-white drop-shadow">@mamuktukangmakeupjogja</span>
                  <span class="text-cyan-400 text-xs">✓</span>
                </div>
                <p class="text-xs text-neutral-100 line-clamp-3 leading-relaxed drop-shadow">
                  MasyaAllah proses paes ageng prada emas keraton Jogja bener-bener bikin merinding syahdu. Auranya manglingi banget manten putri 🥺👑 #weddingjogja #paesageng #muajogja #fypwedding
                </p>
                <div class="flex items-center space-x-1.5 text-[10px] text-neutral-300 drop-shadow">
                  <svg class="w-3.5 h-3.5 text-white animate-pulse" fill="currentColor" viewBox="0 0 24 24"><path d="M12 3v10.55c-.59-.34-1.27-.55-2-.55-2.21 0-4 1.79-4 4s1.79 4 4 4 4-1.79 4-4V7h4V3h-6z"/></svg>
                  <marquee class="w-48 font-mono">Gending Manten Jawa - Ketawang Larasmoyo (Audio Asli Keraton)</marquee>
                </div>

                <!-- DIRECT VENDOR BOOKING BADGE PADA VIDEO TIKTOK -->
                <div class="pt-1">
                  <button onclick="openVendorModal('mua-mamuk')" class="w-full bg-white/95 hover:bg-white text-black text-xs font-bold py-2 px-3 rounded-xl flex items-center justify-between shadow-lg active:scale-95 transition">
                    <div class="flex items-center space-x-2">
                      <span class="w-2 h-2 rounded-full bg-emerald-500 animate-ping"></span>
                      <span class="truncate">🏷️ Vendor: Mamuk Tukang Makeup (Rp 9.5M)</span>
                    </div>
                    <span class="text-neutral-700 text-[11px]">Cek Paket →</span>
                  </button>
                </div>
              </div>

            </div>
          </div>


          <!-- REEL 2: SUNGKEMAN & AKAD HARU JAWARA PHOTO -->
          <div class="relative w-full rounded-3xl overflow-hidden bg-neutral-950 border border-neutral-800 shadow-2xl">
            <div class="relative w-full aspect-[9/14] overflow-hidden">
              <img src="assets/vendors/slides/jawara_slide_1.jpg" class="w-full h-full object-cover">
              <div class="absolute inset-0 bg-gradient-to-t from-black via-black/25 to-black/30 pointer-events-none"></div>

              <div class="absolute top-3 left-3 flex items-center space-x-2">
                <span class="bg-black/70 backdrop-blur text-white border border-white/20 text-[9px] font-bold px-2.5 py-0.5 rounded-full flex items-center space-x-1">
                  <span>TRENDING WEDDING</span>
                </span>
                <span class="bg-red-950/80 text-red-300 border border-red-500/30 text-[9px] px-2 py-0.5 rounded-full font-mono">
                  #SungkemanHaru
                </span>
              </div>

              <!-- Right Action Sidebar -->
              <div class="absolute right-3 bottom-14 flex flex-col items-center space-y-3.5 z-20">
                <div class="relative">
                  <div class="w-10 h-10 rounded-full border-2 border-white overflow-hidden bg-neutral-900 shadow">
                    <img src="assets/vendors/avatars/jawara.jpg" class="w-full h-full object-cover">
                  </div>
                  <button onclick="toggleFollowTikTok(this)" class="absolute -bottom-1.5 left-1/2 -translate-x-1/2 w-4 h-4 rounded-full bg-red-500 text-white flex items-center justify-center text-[10px] font-bold shadow">+</button>
                </div>

                <button onclick="toggleTikTokLike(this, 284500)" class="flex flex-col items-center space-y-0.5 group">
                  <div class="w-10 h-10 rounded-full bg-black/50 backdrop-blur border border-white/20 flex items-center justify-center text-white group-hover:scale-110 active:scale-90 transition">
                    <svg class="w-5 h-5 heart-icon transition" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z"/></svg>
                  </div>
                  <span class="text-[10px] text-white font-mono font-bold count-label">284.5K</span>
                </button>

                <button onclick="showTikTokComments('Jawara Photo')" class="flex flex-col items-center space-y-0.5 group">
                  <div class="w-10 h-10 rounded-full bg-black/50 backdrop-blur border border-white/20 flex items-center justify-center text-white group-hover:scale-110 transition">
                    <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 12h.01M12 12h.01M16 12h.01M21 12c0 4.418-4.03 8-9 8a9.863 9.863 0 01-4.255-.949L3 20l1.395-3.72C3.512 15.042 3 13.574 3 12c0-4.418 4.03-8 9-8s9 3.582 9 8z"/></svg>
                  </div>
                  <span class="text-[10px] text-white font-mono font-bold">4.120</span>
                </button>

                <button onclick="toggleTikTokBookmark(this)" class="flex flex-col items-center space-y-0.5 group">
                  <div class="w-10 h-10 rounded-full bg-black/50 backdrop-blur border border-white/20 flex items-center justify-center text-white group-hover:scale-110 transition">
                    <svg class="w-5 h-5 bookmark-icon" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 5a2 2 0 012-2h10a2 2 0 012 2v16l-7-3.5L5 21V5z"/></svg>
                  </div>
                  <span class="text-[10px] text-white font-mono font-bold">34.1K</span>
                </button>

                <div class="w-10 h-10 rounded-full bg-neutral-900 border-2 border-neutral-700 flex items-center justify-center animate-spin" style="animation-duration: 6s;">
                  <div class="w-4 h-4 rounded-full bg-cyan-400 border border-white"></div>
                </div>
              </div>

              <!-- Bottom Content Overlay -->
              <div class="absolute bottom-3 left-3 right-16 space-y-2 z-20">
                <div class="flex items-center space-x-1.5">
                  <span class="text-xs font-bold text-white drop-shadow">@jawara.photo</span>
                  <span class="text-cyan-400 text-xs">✓</span>
                </div>
                <p class="text-xs text-neutral-100 line-clamp-3 leading-relaxed drop-shadow">
                  Gak pernah gagal bikin nangis satu pendopo saat sungkeman minta restu bapak ibu. Selamat menempuh hidup baru Prima & Fauzan 🤍🕊️ #bersamajawara #weddingtiktok #akadsakral
                </p>
                <div class="flex items-center space-x-1.5 text-[10px] text-neutral-300 drop-shadow">
                  <svg class="w-3.5 h-3.5 text-white animate-pulse" fill="currentColor" viewBox="0 0 24 24"><path d="M12 3v10.55c-.59-.34-1.27-.55-2-.55-2.21 0-4 1.79-4 4s1.79 4 4 4 4-1.79 4-4V7h4V3h-6z"/></svg>
                  <marquee class="w-48 font-mono">Sal Priadi - Gala Bunga Matahari (Official Wedding Audio)</marquee>
                </div>

                <div class="pt-1">
                  <button onclick="openVendorModal('fg-jawara')" class="w-full bg-white/95 hover:bg-white text-black text-xs font-bold py-2 px-3 rounded-xl flex items-center justify-between shadow-lg active:scale-95 transition">
                    <div class="flex items-center space-x-2">
                      <span class="w-2 h-2 rounded-full bg-rose-500 animate-ping"></span>
                      <span class="truncate">🏷️ Vendor: Jawara Photo (Paket Rp 3.8M)</span>
                    </div>
                    <span class="text-neutral-700 text-[11px]">Cek Paket →</span>
                  </button>
                </div>
              </div>

            </div>
          </div>


          <!-- REEL 3: WO ILONA ORGANIZER CREW IN ACTION -->
          <div class="relative w-full rounded-3xl overflow-hidden bg-neutral-950 border border-neutral-800 shadow-2xl">
            <div class="relative w-full aspect-[9/14] overflow-hidden">
              <img src="assets/vendors/slides/ilona_slide_1.jpg" class="w-full h-full object-cover">
              <div class="absolute inset-0 bg-gradient-to-t from-black via-black/25 to-black/30 pointer-events-none"></div>

              <div class="absolute top-3 left-3 flex items-center space-x-2">
                <span class="bg-black/70 backdrop-blur text-white border border-white/20 text-[9px] font-bold px-2.5 py-0.5 rounded-full flex items-center space-x-1">
                  <span>BEHIND THE SCENE</span>
                </span>
                <span class="bg-purple-950/80 text-purple-300 border border-purple-500/30 text-[9px] px-2 py-0.5 rounded-full font-mono">
                  #TeamWOJogja
                </span>
              </div>

              <!-- Right Action Sidebar -->
              <div class="absolute right-3 bottom-14 flex flex-col items-center space-y-3.5 z-20">
                <div class="relative">
                  <div class="w-10 h-10 rounded-full border-2 border-white overflow-hidden bg-neutral-900 shadow">
                    <img src="assets/vendors/avatars/ilona.jpg" class="w-full h-full object-cover">
                  </div>
                  <button onclick="toggleFollowTikTok(this)" class="absolute -bottom-1.5 left-1/2 -translate-x-1/2 w-4 h-4 rounded-full bg-red-500 text-white flex items-center justify-center text-[10px] font-bold shadow">+</button>
                </div>

                <button onclick="toggleTikTokLike(this, 92400)" class="flex flex-col items-center space-y-0.5 group">
                  <div class="w-10 h-10 rounded-full bg-black/50 backdrop-blur border border-white/20 flex items-center justify-center text-white group-hover:scale-110 active:scale-90 transition">
                    <svg class="w-5 h-5 heart-icon transition" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z"/></svg>
                  </div>
                  <span class="text-[10px] text-white font-mono font-bold count-label">92.4K</span>
                </button>

                <button onclick="showTikTokComments('Ilona Wedding Organizer')" class="flex flex-col items-center space-y-0.5 group">
                  <div class="w-10 h-10 rounded-full bg-black/50 backdrop-blur border border-white/20 flex items-center justify-center text-white group-hover:scale-110 transition">
                    <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 12h.01M12 12h.01M16 12h.01M21 12c0 4.418-4.03 8-9 8a9.863 9.863 0 01-4.255-.949L3 20l1.395-3.72C3.512 15.042 3 13.574 3 12c0-4.418 4.03-8 9-8s9 3.582 9 8z"/></svg>
                  </div>
                  <span class="text-[10px] text-white font-mono font-bold">1.850</span>
                </button>

                <button onclick="toggleTikTokBookmark(this)" class="flex flex-col items-center space-y-0.5 group">
                  <div class="w-10 h-10 rounded-full bg-black/50 backdrop-blur border border-white/20 flex items-center justify-center text-white group-hover:scale-110 transition">
                    <svg class="w-5 h-5 bookmark-icon" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 5a2 2 0 012-2h10a2 2 0 012 2v16l-7-3.5L5 21V5z"/></svg>
                  </div>
                  <span class="text-[10px] text-white font-mono font-bold">12.8K</span>
                </button>

                <div class="w-10 h-10 rounded-full bg-neutral-900 border-2 border-neutral-700 flex items-center justify-center animate-spin" style="animation-duration: 6s;">
                  <div class="w-4 h-4 rounded-full bg-purple-500 border border-white"></div>
                </div>
              </div>

              <!-- Bottom Content Overlay -->
              <div class="absolute bottom-3 left-3 right-16 space-y-2 z-20">
                <div class="flex items-center space-x-1.5">
                  <span class="text-xs font-bold text-white drop-shadow">@ilonaorganizer</span>
                  <span class="text-cyan-400 text-xs">✓</span>
                </div>
                <p class="text-xs text-neutral-100 line-clamp-3 leading-relaxed drop-shadow">
                  POV: 12 jam kru WO Ilona siap siaga jagain pengantin & keluarga. Dari rundown akad sampai resepsi beres tanpa pusing! 🥰🤍 #ilonaorganizer #weddingplannerjogja #ddaywedding
                </p>
                <div class="flex items-center space-x-1.5 text-[10px] text-neutral-300 drop-shadow">
                  <svg class="w-3.5 h-3.5 text-white animate-pulse" fill="currentColor" viewBox="0 0 24 24"><path d="M12 3v10.55c-.59-.34-1.27-.55-2-.55-2.21 0-4 1.79-4 4s1.79 4 4 4 4-1.79 4-4V7h4V3h-6z"/></svg>
                  <marquee class="w-48 font-mono">Nadin Amizah - Rayuan Perempuan Gila (Wedding Acoustic)</marquee>
                </div>

                <div class="pt-1">
                  <button onclick="openVendorModal('wo-ilona')" class="w-full bg-white/95 hover:bg-white text-black text-xs font-bold py-2 px-3 rounded-xl flex items-center justify-between shadow-lg active:scale-95 transition">
                    <div class="flex items-center space-x-2">
                      <span class="w-2 h-2 rounded-full bg-purple-500 animate-ping"></span>
                      <span class="truncate">🏷️ Vendor: Ilona Wedding Organizer (Rp 4.5M)</span>
                    </div>
                    <span class="text-neutral-700 text-[11px]">Cek Paket →</span>
                  </button>
                </div>
              </div>

            </div>
          </div>

          <!-- REEL 4: CATERING PRASMANAN VIDI -->
          <div class="relative w-full rounded-3xl overflow-hidden bg-neutral-950 border border-neutral-800 shadow-2xl">
            <div class="relative w-full aspect-[9/14] overflow-hidden">
              <img src="assets/vendors/slides/vidi_slide_1.jpg" class="w-full h-full object-cover">
              <div class="absolute inset-0 bg-gradient-to-t from-black via-black/25 to-black/30 pointer-events-none"></div>

              <div class="absolute top-3 left-3 flex items-center space-x-2">
                <span class="bg-black/70 backdrop-blur text-white border border-white/20 text-[9px] font-bold px-2.5 py-0.5 rounded-full flex items-center space-x-1">
                  <span>FOOD REVIEW JOGJA</span>
                </span>
                <span class="bg-amber-950/80 text-amber-300 border border-amber-500/30 text-[9px] px-2 py-0.5 rounded-full font-mono">
                  #CateringEnak
                </span>
              </div>

              <!-- Right Action Sidebar -->
              <div class="absolute right-3 bottom-14 flex flex-col items-center space-y-3.5 z-20">
                <div class="relative">
                  <div class="w-10 h-10 rounded-full border-2 border-white overflow-hidden bg-neutral-900 shadow">
                    <img src="assets/vendors/avatars/vidi.jpg" class="w-full h-full object-cover">
                  </div>
                  <button onclick="toggleFollowTikTok(this)" class="absolute -bottom-1.5 left-1/2 -translate-x-1/2 w-4 h-4 rounded-full bg-red-500 text-white flex items-center justify-center text-[10px] font-bold shadow">+</button>
                </div>

                <button onclick="toggleTikTokLike(this, 76100)" class="flex flex-col items-center space-y-0.5 group">
                  <div class="w-10 h-10 rounded-full bg-black/50 backdrop-blur border border-white/20 flex items-center justify-center text-white group-hover:scale-110 active:scale-90 transition">
                    <svg class="w-5 h-5 heart-icon transition" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z"/></svg>
                  </div>
                  <span class="text-[10px] text-white font-mono font-bold count-label">76.1K</span>
                </button>

                <button onclick="showTikTokComments('Vidi Catering')" class="flex flex-col items-center space-y-0.5 group">
                  <div class="w-10 h-10 rounded-full bg-black/50 backdrop-blur border border-white/20 flex items-center justify-center text-white group-hover:scale-110 transition">
                    <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 12h.01M12 12h.01M16 12h.01M21 12c0 4.418-4.03 8-9 8a9.863 9.863 0 01-4.255-.949L3 20l1.395-3.72C3.512 15.042 3 13.574 3 12c0-4.418 4.03-8 9-8s9 3.582 9 8z"/></svg>
                  </div>
                  <span class="text-[10px] text-white font-mono font-bold">980</span>
                </button>

                <button onclick="toggleTikTokBookmark(this)" class="flex flex-col items-center space-y-0.5 group">
                  <div class="w-10 h-10 rounded-full bg-black/50 backdrop-blur border border-white/20 flex items-center justify-center text-white group-hover:scale-110 transition">
                    <svg class="w-5 h-5 bookmark-icon" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 5a2 2 0 012-2h10a2 2 0 012 2v16l-7-3.5L5 21V5z"/></svg>
                  </div>
                  <span class="text-[10px] text-white font-mono font-bold">9.4K</span>
                </button>

                <div class="w-10 h-10 rounded-full bg-neutral-900 border-2 border-neutral-700 flex items-center justify-center animate-spin" style="animation-duration: 6s;">
                  <div class="w-4 h-4 rounded-full bg-amber-500 border border-white"></div>
                </div>
              </div>

              <!-- Bottom Content Overlay -->
              <div class="absolute bottom-3 left-3 right-16 space-y-2 z-20">
                <div class="flex items-center space-x-1.5">
                  <span class="text-xs font-bold text-white drop-shadow">@vidicatering</span>
                  <span class="text-cyan-400 text-xs">✓</span>
                </div>
                <p class="text-xs text-neutral-100 line-clamp-3 leading-relaxed drop-shadow">
                  Gubukan sate ayam & zuppa soup gak pernah sepi antre! Definisi tamu kondangan pulang kenyang dan senyum bahagia 🤤🍱 #cateringjogja #vidicatering #prasmananmanten
                </p>
                <div class="flex items-center space-x-1.5 text-[10px] text-neutral-300 drop-shadow">
                  <svg class="w-3.5 h-3.5 text-white animate-pulse" fill="currentColor" viewBox="0 0 24 24"><path d="M12 3v10.55c-.59-.34-1.27-.55-2-.55-2.21 0-4 1.79-4 4s1.79 4 4 4 4-1.79 4-4V7h4V3h-6z"/></svg>
                  <marquee class="w-48 font-mono">Trending TikTok Sound - Wedding Food Tasting Review</marquee>
                </div>

                <div class="pt-1">
                  <button onclick="openVendorModal('cat-vidi')" class="w-full bg-white/95 hover:bg-white text-black text-xs font-bold py-2 px-3 rounded-xl flex items-center justify-between shadow-lg active:scale-95 transition">
                    <div class="flex items-center space-x-2">
                      <span class="w-2 h-2 rounded-full bg-amber-500 animate-ping"></span>
                      <span class="truncate">🏷️ Vendor: Vidi Catering (Mulai Rp 65.000 / pax)</span>
                    </div>
                    <span class="text-neutral-700 text-[11px]">Cek Menu →</span>
                  </button>
                </div>
              </div>

            </div>
          </div>

        </div>
      </div>
"""

# Insert viewTikTok right after viewSaved
if 'id="viewTikTok"' not in html:
    html = html.replace('</div>\n\n    </div>\n\n    <!-- BOTTOM APP NAVIGATION DOCK', '</div>\n' + tiktok_view_html + '\n    </div>\n\n    <!-- BOTTOM APP NAVIGATION DOCK')
    print("Inserted viewTikTok markup successfully!")

# 3. Add Modal Connect TikTok Client
tiktok_modal_html = """
    <!-- MODAL CONNECT TIKTOK ACCOUNT KLIEN -->
    <div id="tiktokConnectModal" class="hidden absolute inset-0 z-50 bg-black/95 backdrop-blur-md flex flex-col justify-end transition-all">
      <div class="bg-neutral-950 border-t border-neutral-800 rounded-t-3xl p-5 space-y-4 max-h-[85%] overflow-y-auto">
        <div class="w-12 h-1 bg-neutral-800 rounded-full mx-auto"></div>
        
        <div class="text-center space-y-1">
          <div class="w-12 h-12 rounded-full bg-gradient-to-tr from-cyan-500 via-pink-500 to-red-500 p-0.5 mx-auto">
            <div class="w-full h-full rounded-full bg-black flex items-center justify-center text-white">
              <svg class="w-6 h-6" viewBox="0 0 24 24" fill="currentColor">
                <path d="M19.59 6.69a4.83 4.83 0 0 1-3.77-4.25V2h-3.45v13.67a2.89 2.89 0 0 1-5.2 1.74 2.89 2.89 0 0 1 2.31-4.64 2.93 2.93 0 0 1 .88.13V9.4a6.84 6.84 0 0 0-1-.05A6.33 6.33 0 0 0 5 20.1a6.34 6.34 0 0 0 10.86-4.43v-7a8.16 8.16 0 0 0 4.77 1.52v-3.4a4.85 4.85 0 0 1-1.04-.1z"/>
              </svg>
            </div>
          </div>
          <h3 class="text-base font-bold text-white tracking-wide">Tautkan Akun TikTok Klien</h3>
          <p class="text-xs text-neutral-400">Sinkronkan video favorit & wishlist inspirasi wedding TikTok Indonesia langsung ke akun KITA MENIKAH Anda.</p>
        </div>

        <div class="space-y-3 pt-2">
          <div>
            <label class="text-xs text-neutral-300 font-medium block mb-1">Username TikTok Anda</label>
            <div class="relative">
              <span class="absolute left-3.5 top-2.5 text-neutral-500 text-xs font-mono font-bold">@</span>
              <input type="text" id="inputTikTokUsername" value="pengantinjogja_2026" placeholder="username_tiktok" class="w-full bg-neutral-900 border border-neutral-700 rounded-xl pl-8 pr-4 py-2.5 text-xs text-white font-mono focus:outline-none focus:border-pink-500">
            </div>
          </div>

          <div class="bg-neutral-900/60 border border-neutral-800 rounded-xl p-3 space-y-1.5 text-[11px] text-neutral-400">
            <div class="flex items-center space-x-2 text-neutral-200 font-semibold">
              <span class="text-emerald-400">✓</span>
              <span>100% Konten Pernikahan Indonesia</span>
            </div>
            <p>Hanya video ber-tagar pernikahan (#WeddingJogja, #PaesAgeng, #DekorWedding) yang akan dikurasi dan disinkronkan ke feed Anda.</p>
          </div>

          <div class="flex space-x-2 pt-2">
            <button onclick="closeTikTokConnectModal()" class="flex-1 bg-neutral-900 hover:bg-neutral-800 text-neutral-300 text-xs font-bold py-3 rounded-xl border border-neutral-800 transition">
              Batal
            </button>
            <button onclick="saveTikTokAccountConnection()" class="flex-1 bg-gradient-to-r from-cyan-500 via-pink-500 to-red-500 text-white text-xs font-bold py-3 rounded-xl hover:opacity-95 transition shadow-lg active:scale-95">
              Simpan & Tautkan
            </button>
          </div>
        </div>

      </div>
    </div>
"""

if 'id="tiktokConnectModal"' not in html:
    html = html.replace('<!-- MODAL 1: VENDOR DETAIL', tiktok_modal_html + '\n\n    <!-- MODAL 1: VENDOR DETAIL')
    print("Inserted tiktokConnectModal markup successfully!")

# 4. Update switchTab function to include TikTok
old_switch_tab = """    function switchTab(tab) {
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
    }"""

new_switch_tab = """    function switchTab(tab) {
      if (currentAppMode === 'vendor') {
        toggleAppMode(); // switch back to client when clicking dock tabs
      }

      ['Home', 'TikTok', 'Budget', 'Saved'].forEach(t => {
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
      } else if (tab === 'tiktok') {
        document.getElementById('viewTikTok').classList.remove('hidden');
        document.getElementById('navTikTok').classList.add('text-white');
        document.getElementById('navTikTok').classList.remove('text-neutral-500');
        window.scrollTo({ top: 0, behavior: 'smooth' });
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
    }"""

if old_switch_tab in html:
    html = html.replace(old_switch_tab, new_switch_tab)
    print("Updated switchTab to handle TikTok tab!")
else:
    print("Could not match old_switch_tab directly, updating via regex...")
    html = re.sub(r'function switchTab\(tab\)\s*\{.*?\n    \}', new_switch_tab, html, flags=re.DOTALL)
    print("Replaced switchTab with new_switch_tab via regex!")

# 5. Add TikTok interactive helper functions in JS
tiktok_js_helpers = """
    // TIKTOK WEDDING INTERACTIVE CONTROLS
    let connectedTikTokUser = '@pengantinjogja_2026';

    function openTikTokConnectModal() {
      document.getElementById('tiktokConnectModal').classList.remove('hidden');
    }

    function closeTikTokConnectModal() {
      document.getElementById('tiktokConnectModal').classList.add('hidden');
    }

    function saveTikTokAccountConnection() {
      const val = document.getElementById('inputTikTokUsername').value.trim();
      if (val) {
        connectedTikTokUser = val.startsWith('@') ? val : '@' + val;
        document.getElementById('handleClientTikTok').innerText = connectedTikTokUser;
        document.getElementById('labelConnectTikTok').innerText = connectedTikTokUser;
      }
      closeTikTokConnectModal();
      alert(`Berhasil menghubungkan akun TikTok ${connectedTikTokUser}! Konten wedding Indonesia kini tersinkronisasi.`);
    }

    function toggleTikTokLike(btn, baseCount) {
      const heart = btn.querySelector('.heart-icon');
      const label = btn.querySelector('.count-label');
      const isLiked = heart.classList.contains('fill-red-500');

      if (isLiked) {
        heart.classList.remove('fill-red-500', 'text-red-500');
        heart.classList.add('text-white');
        label.innerText = ((baseCount) / 1000).toFixed(1) + 'K';
      } else {
        heart.classList.add('fill-red-500', 'text-red-500', 'scale-125');
        setTimeout(() => heart.classList.remove('scale-125'), 200);
        label.innerText = ((baseCount + 1) / 1000).toFixed(1) + 'K';
      }
    }

    function toggleTikTokBookmark(btn) {
      const icon = btn.querySelector('.bookmark-icon');
      const isSaved = icon.classList.contains('fill-yellow-400');
      if (isSaved) {
        icon.classList.remove('fill-yellow-400', 'text-yellow-400');
        icon.classList.add('text-white');
      } else {
        icon.classList.add('fill-yellow-400', 'text-yellow-400');
      }
    }

    function toggleFollowTikTok(btn) {
      if (btn.innerText === '+') {
        btn.innerText = '✓';
        btn.classList.remove('bg-red-500');
        btn.classList.add('bg-neutral-800', 'text-white');
      } else {
        btn.innerText = '+';
        btn.classList.remove('bg-neutral-800', 'text-white');
        btn.classList.add('bg-red-500');
      }
    }

    function showTikTokComments(vendorName) {
      alert(`Komentar TikTok untuk ${vendorName}:\\n- "Spill MUA Paes Ageng nya dong kak, manglingi bgt! 🥺"\\n- "Ini paketnya berapaan ya di KITA MENIKAH?"\\n- "Kak rundown acaranya boleh dishare?"\\n\\n(Klik tombol '🏷️ Vendor' di video untuk langsung booking & chat resmi vendor!)`);
    }
"""

# Insert tiktok_js_helpers before init on load
html = html.replace('// INIT ON LOAD', tiktok_js_helpers + '\n    // INIT ON LOAD')

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Saved updated index.html with TikTok Wedding integration successfully!")
