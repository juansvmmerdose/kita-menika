import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Update <style> to add TikTok animations, floating hearts, and iPhone styling
style_addition = """
    /* TIKTOK LITE & IPHONE ANIMATIONS */
    @keyframes heart-burst {
      0% { transform: translate(-50%, -50%) scale(0.4); opacity: 0; }
      40% { transform: translate(-50%, -50%) scale(1.3); opacity: 1; }
      70% { transform: translate(-50%, -50%) scale(1.1); opacity: 0.9; }
      100% { transform: translate(-50%, -120px) scale(1.4); opacity: 0; }
    }
    .heart-float {
      position: absolute;
      pointer-events: none;
      animation: heart-burst 0.9s cubic-bezier(0.175, 0.885, 0.32, 1.275) forwards;
      z-index: 60;
    }
    @keyframes spin-slow {
      from { transform: rotate(0deg); }
      to { transform: rotate(360deg); }
    }
    .animate-spin-slow {
      animation: spin-slow 7s linear infinite;
    }
    @keyframes music-wave {
      0%, 100% { height: 4px; }
      50% { height: 16px; }
    }
    .music-bar-1 { animation: music-wave 0.8s ease-in-out infinite; }
    .music-bar-2 { animation: music-wave 0.6s ease-in-out infinite 0.2s; }
    .music-bar-3 { animation: music-wave 0.9s ease-in-out infinite 0.4s; }
"""

if 'heart-burst' not in html:
    html = html.replace('</style>', style_addition + '\n  </style>')
    print("Added CSS animations for TikTok Lite and iPhone styling!")

# 2. Update <body> and Outer Device Mockup Container to iPhone 16 Pro (Fixed viewport height, zero outer page scroll)
body_pattern = r'<body.*?>\s*<!-- Outer Device Mockup Container -->\s*<div.*?>.*?<!-- iPhone Top Dynamic Island -->.*?</div>\s*</div>'

new_body_and_iphone = """<body class="bg-[#050507] text-neutral-100 font-sans-clean h-screen w-screen overflow-hidden flex items-center justify-center p-2 sm:p-4 select-none antialiased">

  <!-- OUTER IPHONE 16 PRO CONTAINER (FIXED FIT, ZERO OUTER PAGE SCROLLBAR) -->
  <div id="iphoneDeviceFrame" class="relative bg-black rounded-[46px] md:rounded-[52px] border-[8px] md:border-[10px] border-[#222226] shadow-[0_0_0_1px_rgba(255,255,255,0.08),0_25px_65px_-12px_rgba(0,0,0,0.95),0_0_40px_rgba(255,255,255,0.02)] overflow-hidden flex flex-col"
       style="height: min(95vh, 850px); aspect-ratio: 9 / 19.3; max-width: 414px; width: 100%;">
    
    <!-- HARDWARE BUTTONS: ACTION, VOLUME UP, VOLUME DOWN (LEFT) & POWER (RIGHT) -->
    <div class="hidden md:block absolute -left-[13px] top-24 w-1 h-6 bg-[#38383e] rounded-l-md shadow"></div>
    <div class="hidden md:block absolute -left-[13px] top-36 w-1 h-11 bg-[#38383e] rounded-l-md shadow"></div>
    <div class="hidden md:block absolute -left-[13px] top-52 w-1 h-11 bg-[#38383e] rounded-l-md shadow"></div>
    <div class="hidden md:block absolute -right-[13px] top-40 w-1 h-16 bg-[#38383e] rounded-r-md shadow"></div>

    <!-- IPHONE STATUS BAR & INTERACTIVE DYNAMIC ISLAND -->
    <div id="iphoneStatusBar" class="absolute top-0 left-0 right-0 z-50 flex justify-between items-center px-6 pt-3 pb-1 select-none pointer-events-none">
      <span id="statusBarClock" class="text-xs font-semibold tracking-wider text-white font-mono drop-shadow">09:41</span>
      
      <!-- INTERACTIVE DYNAMIC ISLAND -->
      <div id="dynamicIsland" class="pointer-events-auto cursor-pointer h-7 px-3 bg-black rounded-full border border-neutral-800 shadow-md flex items-center space-x-2 transition-all duration-300 hover:scale-105 active:scale-95" onclick="toggleDynamicIslandDetails()">
        <div class="w-2.5 h-2.5 rounded-full bg-neutral-900 border border-neutral-700/60"></div>
        <div class="w-1.5 h-1.5 rounded-full bg-blue-950/80 border border-blue-500/40"></div>
        <div id="islandMusicWaves" class="hidden items-end space-x-0.5 h-3">
          <div class="w-0.5 bg-emerald-400 rounded-full music-bar-1"></div>
          <div class="w-0.5 bg-emerald-400 rounded-full music-bar-2"></div>
          <div class="w-0.5 bg-emerald-400 rounded-full music-bar-3"></div>
        </div>
        <span id="dynamicIslandLabel" class="text-[9px] font-mono text-neutral-300 hidden">Gending Manten</span>
      </div>

      <!-- WIFI & BATTERY ICONS -->
      <div class="flex items-center space-x-1.5 text-white text-xs drop-shadow">
        <svg class="w-3.5 h-3.5" fill="currentColor" viewBox="0 0 24 24"><path d="M12 3c-4.97 0-9 4.03-9 9 0 2.12.74 4.07 1.97 5.61L4.35 19.4c-.39.39-.39 1.02 0 1.41.39.39 1.02.39 1.41 0l1.9-1.9C9.28 19.68 10.59 20 12 20c4.97 0 9-4.03 9-9s-4.03-9-9-9zm0 15c-3.31 0-6-2.69-6-6s2.69-6 6-6 6 2.69 6 6-2.69 6-6 6z"/></svg>
        <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 24 24"><path d="M15.67 4H14V2h-4v2H8.33C7.6 4 7 4.6 7 5.33v15.33C7 21.4 7.6 22 8.33 22h7.33c.74 0 1.34-.6 1.34-1.33V5.33C17 4.6 16.4 4 15.67 4z"/></svg>
      </div>
    </div>"""

html = re.sub(body_pattern, new_body_and_iphone, html, flags=re.DOTALL)
print("Updated body and device mockup to fixed iPhone 16 Pro styling!")

# 3. Update bottom nav to include Home Indicator bar
old_bottom_nav_dock = r'<!-- BOTTOM APP NAVIGATION DOCK.*?<nav id="bottomAppNav".*?</nav>'

new_bottom_dock = """<!-- BOTTOM APP NAVIGATION DOCK (4 TABS) + IPHONE HOME INDICATOR -->
    <div id="bottomDockWrapper" class="absolute bottom-0 left-0 right-0 z-40 bg-black/95 backdrop-blur border-t border-neutral-900/90 flex flex-col justify-end">
      <nav id="bottomAppNav" class="h-14 flex justify-around items-center px-2">
        <!-- 1. IKON RUMAH (EKSPLOR) -->
        <button onclick="switchTab('home')" id="navHome" class="flex flex-col items-center justify-center space-y-0.5 text-white px-2">
          <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6"/></svg>
          <span class="text-[9px] font-semibold tracking-wider">Eksplor</span>
        </button>

        <!-- 2. IKON TIKTOK (PERSIS DI SAMPING IKON RUMAH - TIKTOK LITE WEDDING INDO) -->
        <button onclick="switchTab('tiktok')" id="navTikTok" class="flex flex-col items-center justify-center space-y-0.5 text-neutral-500 hover:text-white transition group px-2 relative">
          <div class="relative">
            <svg class="w-5 h-5 transition group-hover:scale-110" viewBox="0 0 24 24" fill="currentColor">
              <path d="M19.59 6.69a4.83 4.83 0 0 1-3.77-4.25V2h-3.45v13.67a2.89 2.89 0 0 1-5.2 1.74 2.89 2.89 0 0 1 2.31-4.64 2.93 2.93 0 0 1 .88.13V9.4a6.84 6.84 0 0 0-1-.05A6.33 6.33 0 0 0 5 20.1a6.34 6.34 0 0 0 10.86-4.43v-7a8.16 8.16 0 0 0 4.77 1.52v-3.4a4.85 4.85 0 0 1-1.04-.1z"/>
            </svg>
            <span class="absolute -top-1 -right-1 w-2 h-2 rounded-full bg-red-500 animate-pulse"></span>
          </div>
          <span class="text-[9px] font-semibold tracking-wider">TikTok</span>
        </button>

        <!-- 3. BUDGET -->
        <button onclick="switchTab('budget')" id="navBudget" class="flex flex-col items-center justify-center space-y-0.5 text-neutral-500 hover:text-white transition px-2">
          <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 7h6m0 10v-3m-3 3h.01M9 17h.01M9 14h.01M12 14h.01M15 11h.01M12 11h.01M9 11h.01M7 21h10a2 2 0 002-2V5a2 2 0 00-2-2H7a2 2 0 00-2 2v14a2 2 0 002 2z"/></svg>
          <span class="text-[9px] font-semibold tracking-wider">Budget</span>
        </button>

        <!-- 4. TERSIMPAN -->
        <button onclick="switchTab('saved')" id="navSaved" class="flex flex-col items-center justify-center space-y-0.5 text-neutral-500 hover:text-white transition px-2">
          <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z"/></svg>
          <span class="text-[9px] font-semibold tracking-wider">Tersimpan</span>
        </button>
      </nav>

      <!-- IPHONE BOTTOM HOME INDICATOR BAR -->
      <div class="w-28 h-1 bg-white/35 rounded-full mx-auto my-1 pointer-events-none"></div>
    </div>"""

html = re.sub(r'<!-- BOTTOM APP NAVIGATION DOCK.*?<nav.*?</nav>', new_bottom_dock, html, flags=re.DOTALL)
print("Updated bottom nav with iPhone Home indicator!")

# 4. Replace viewTikTok with REAL FULL-SCREEN TIKTOK LITE PLAYER
tiktok_lite_view_html = """
      <!-- VIEW 5: TIKTOK LITE WEDDING INDONESIA (PLAYER LENGKAP BISA DIJALANKAN) -->
      <div id="viewTikTok" class="hidden absolute inset-0 z-30 bg-black flex flex-col overflow-hidden">
        
        <!-- TIKTOK TOP OVERLAY BAR: TABS, CLIENT ACCOUNT & SOUND TOGGLE -->
        <div class="absolute top-11 left-0 right-0 z-30 px-3 flex justify-between items-center pointer-events-auto">
          
          <!-- Category Tabs (TikTok Style) -->
          <div class="flex items-center space-x-2 text-xs font-bold drop-shadow">
            <button onclick="switchTikTokCategory('fyp')" id="tt-tab-fyp" class="text-white border-b-2 border-white pb-0.5">FYP</button>
            <button onclick="switchTikTokCategory('paes')" id="tt-tab-paes" class="text-neutral-400 hover:text-white pb-0.5">Paes MUA</button>
            <button onclick="switchTikTokCategory('akad')" id="tt-tab-akad" class="text-neutral-400 hover:text-white pb-0.5">Akad Haru</button>
            <button onclick="switchTikTokCategory('wo')" id="tt-tab-wo" class="text-neutral-400 hover:text-white pb-0.5">WO & Dekor</button>
          </div>

          <!-- Controls: Sound Toggle & Connect Account -->
          <div class="flex items-center space-x-1.5">
            <!-- Audio Sound Toggle Button (Bisa Dijalankan Bunyi Musik) -->
            <button onclick="toggleTikTokSound()" id="btnTikTokSound" class="w-8 h-8 rounded-full bg-black/60 backdrop-blur border border-white/25 flex items-center justify-center text-white active:scale-90 transition shadow-md" title="Nyalakan/Matikan Audio">
              <span id="iconSoundMuted">🔇</span>
              <span id="iconSoundPlaying" class="hidden">🔊</span>
            </button>

            <!-- Tautkan Akun Klien -->
            <button onclick="openTikTokConnectModal()" class="px-2 py-1 rounded-full bg-black/60 backdrop-blur border border-pink-500/40 text-pink-300 text-[10px] font-bold flex items-center space-x-1 shadow-sm active:scale-95">
              <span id="labelConnectTikTokSmall">@klien</span>
            </button>
          </div>
        </div>

        <!-- TIKTOK REELS SCREEN (FULL-HEIGHT ACTIVE REEL) -->
        <div id="tiktokPlayerScreen" class="relative flex-1 w-full h-full bg-black overflow-hidden flex items-center justify-center select-none" onclick="handleTikTokScreenClick(event)">
          
          <!-- Active Video Visual (Photo/Video Loop) -->
          <img id="ttActivePoster" src="assets/vendors/slides/mamuk_slide_1.jpg" class="w-full h-full object-cover filter brightness-95">
          
          <!-- Gradient Shadows for readability -->
          <div class="absolute inset-0 bg-gradient-to-t from-black via-transparent to-black/60 pointer-events-none"></div>

          <!-- Play / Pause Center Watermark -->
          <div id="ttPlayPauseIcon" class="hidden absolute inset-0 flex items-center justify-center pointer-events-none">
            <div class="w-16 h-16 rounded-full bg-black/50 backdrop-blur-md border border-white/30 flex items-center justify-center text-white text-2xl shadow-2xl animate-pulse">
              ▶
            </div>
          </div>

          <!-- Right Action Sidebar (Like, Comment, Save, Share, Next/Prev) -->
          <div class="absolute right-2.5 bottom-20 flex flex-col items-center space-y-3 z-30" onclick="event.stopPropagation()">
            
            <!-- Up / Previous Reel Button -->
            <button onclick="prevTikTokReel()" class="w-8 h-8 rounded-full bg-black/50 backdrop-blur border border-white/20 flex items-center justify-center text-white text-xs hover:bg-black/80 transition active:scale-90" title="Reel Sebelumnya">
              ▲
            </button>

            <!-- Creator Avatar with Follow Plus -->
            <div class="relative">
              <div class="w-10 h-10 rounded-full border-2 border-white overflow-hidden bg-neutral-900 shadow">
                <img id="ttAvatarImg" src="assets/vendors/avatars/mamuk.jpg" class="w-full h-full object-cover">
              </div>
              <button onclick="toggleFollowTikTok(this)" class="absolute -bottom-1.5 left-1/2 -translate-x-1/2 w-4 h-4 rounded-full bg-red-500 text-white flex items-center justify-center text-[10px] font-bold shadow">+</button>
            </div>

            <!-- Like Button -->
            <button onclick="toggleTikTokLikeBtn()" id="btnTTLike" class="flex flex-col items-center space-y-0.5 group">
              <div class="w-10 h-10 rounded-full bg-black/50 backdrop-blur border border-white/20 flex items-center justify-center text-white group-hover:scale-110 active:scale-90 transition">
                <svg id="ttHeartIcon" class="w-5 h-5 transition" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z"/></svg>
              </div>
              <span id="ttLikeCount" class="text-[10px] text-white font-mono font-bold drop-shadow">148.2K</span>
            </button>

            <!-- Comment Button -->
            <button onclick="openTikTokCommentSheet()" class="flex flex-col items-center space-y-0.5 group">
              <div class="w-10 h-10 rounded-full bg-black/50 backdrop-blur border border-white/20 flex items-center justify-center text-white group-hover:scale-110 active:scale-90 transition">
                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 12h.01M12 12h.01M16 12h.01M21 12c0 4.418-4.03 8-9 8a9.863 9.863 0 01-4.255-.949L3 20l1.395-3.72C3.512 15.042 3 13.574 3 12c0-4.418 4.03-8 9-8s9 3.582 9 8z"/></svg>
              </div>
              <span id="ttCommentCount" class="text-[10px] text-white font-mono font-bold drop-shadow">2.4K</span>
            </button>

            <!-- Save Bookmark Button -->
            <button onclick="toggleTikTokBookmarkBtn()" id="btnTTBookmark" class="flex flex-col items-center space-y-0.5 group">
              <div class="w-10 h-10 rounded-full bg-black/50 backdrop-blur border border-white/20 flex items-center justify-center text-white group-hover:scale-110 active:scale-90 transition">
                <svg id="ttBookmarkIcon" class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 5a2 2 0 012-2h10a2 2 0 012 2v16l-7-3.5L5 21V5z"/></svg>
              </div>
              <span class="text-[10px] text-white font-mono font-bold drop-shadow">19.3K</span>
            </button>

            <!-- Down / Next Reel Button -->
            <button onclick="nextTikTokReel()" class="w-8 h-8 rounded-full bg-black/50 backdrop-blur border border-white/20 flex items-center justify-center text-white text-xs hover:bg-black/80 transition active:scale-90" title="Reel Selanjutnya">
              ▼
            </button>

            <!-- Spinning Vinyl Album Art -->
            <div id="ttVinylDisc" class="w-9 h-9 rounded-full bg-neutral-900 border-2 border-neutral-700 flex items-center justify-center animate-spin-slow">
              <div class="w-3.5 h-3.5 rounded-full bg-pink-500 border border-white"></div>
            </div>

          </div>

          <!-- Bottom Left Information Overlay -->
          <div class="absolute bottom-18 left-3 right-16 space-y-1.5 z-20 pointer-events-auto" onclick="event.stopPropagation()">
            <div class="flex items-center space-x-1.5">
              <span id="ttCreatorName" class="text-xs font-bold text-white drop-shadow">@mamuktukangmakeupjogja</span>
              <span class="text-cyan-400 text-xs">✓</span>
              <span id="ttReelIndex" class="text-[9px] text-neutral-400 font-mono bg-black/50 px-1.5 py-0.2 rounded">1/5</span>
            </div>
            
            <p id="ttCaptionText" class="text-xs text-neutral-100 line-clamp-2 leading-relaxed drop-shadow">
              Proses cengkorongan paes ageng prada emas keraton Jogja. Auranya ningrat bgt manten putri 🥺👑 #weddingjogja #paesageng
            </p>

            <!-- Audio Track Title -->
            <div class="flex items-center space-x-1.5 text-[10px] text-neutral-300 drop-shadow">
              <svg class="w-3.5 h-3.5 text-white animate-pulse" fill="currentColor" viewBox="0 0 24 24"><path d="M12 3v10.55c-.59-.34-1.27-.55-2-.55-2.21 0-4 1.79-4 4s1.79 4 4 4 4-1.79 4-4V7h4V3h-6z"/></svg>
              <marquee id="ttAudioTitle" class="w-44 font-mono">Gending Manten Jawa - Ketawang Larasmoyo (Audio Asli Keraton)</marquee>
            </div>

            <!-- DIRECT VENDOR BOOKING BANNER PADA REEL TIKTOK -->
            <div class="pt-0.5">
              <button id="ttVendorBtn" onclick="openActiveReelVendor()" class="w-full bg-white/95 hover:bg-white text-black text-[11px] font-bold py-1.5 px-3 rounded-xl flex items-center justify-between shadow-lg active:scale-95 transition">
                <div class="flex items-center space-x-1.5 truncate">
                  <span class="w-2 h-2 rounded-full bg-emerald-500 animate-ping"></span>
                  <span id="ttVendorBtnLabel" class="truncate">🏷️ Vendor: Mamuk Tukang Makeup (Rp 9.5M)</span>
                </div>
                <span class="text-neutral-700 text-[10px]">Cek Paket →</span>
              </button>
            </div>
          </div>

          <!-- Video Progress Bar (TikTok Style) -->
          <div class="absolute bottom-16 left-0 right-0 h-0.5 bg-white/20 z-30">
            <div id="ttProgressBar" class="h-full bg-white transition-all duration-300" style="width: 35%;"></div>
          </div>

        </div>

        <!-- TIKTOK COMMENT SHEET (SLIDES UP FROM BOTTOM) -->
        <div id="tiktokCommentSheet" class="hidden absolute inset-x-0 bottom-0 top-36 z-50 bg-neutral-950/98 backdrop-blur-md rounded-t-3xl border-t border-neutral-800 flex flex-col overflow-hidden transition-all shadow-2xl">
          
          <!-- Sheet Header -->
          <div class="px-4 py-3 border-b border-neutral-800 flex justify-between items-center">
            <span id="sheetCommentHeader" class="text-xs font-bold text-white tracking-wide">2.418 Komentar Wedding</span>
            <button onclick="closeTikTokCommentSheet()" class="w-7 h-7 rounded-full bg-neutral-900 text-neutral-400 flex items-center justify-center text-xs hover:text-white">✕</button>
          </div>

          <!-- Comments List Container -->
          <div id="ttCommentsList" class="flex-1 overflow-y-auto p-4 space-y-3 text-xs no-scrollbar">
            <!-- Dynamic comments injected by JS -->
          </div>

          <!-- Comment Input Bar -->
          <div class="p-3 bg-neutral-900 border-t border-neutral-800 flex items-center space-x-2">
            <input type="text" id="inputNewComment" placeholder="Tulis komentar wedding inspiratif..." class="flex-1 bg-black border border-neutral-700 rounded-full px-3.5 py-2 text-xs text-white placeholder-neutral-500 focus:outline-none focus:border-pink-500">
            <button onclick="submitNewComment()" class="w-8 h-8 rounded-full bg-red-500 hover:bg-red-600 text-white flex items-center justify-center font-bold text-xs transition active:scale-90">
              ➤
            </button>
          </div>

        </div>

      </div>
"""

# Replace viewTikTok with tiktok_lite_view_html
html = re.sub(r'<!-- VIEW 5: TIKTOK WEDDING INDONESIA.*?</div>\s*</div>\s*</div>\s*</div>', tiktok_lite_view_html, html, flags=re.DOTALL)
print("Replaced viewTikTok with TikTok Lite full-screen player!")

# 5. Add JavaScript for TikTok Lite Player, Audio Synthesizer, Reels Data, and Comments
tiktok_lite_js = """
    // ==========================================
    // TIKTOK LITE WEDDING INDO REAL ENGINE
    // ==========================================
    const tiktokReelsData = [
      {
        id: 'reel-1',
        category: 'paes',
        vendorId: 'mua-mamuk',
        creator: '@mamuktukangmakeupjogja',
        creatorAvatar: 'assets/vendors/avatars/mamuk.jpg',
        poster: 'assets/vendors/slides/mamuk_slide_1.jpg',
        caption: 'Proses cengkorongan paes ageng prada emas keraton Jogja. Auranya ningrat bgt manten putri 🥺👑 #weddingjogja #paesageng #muajogja',
        audio: 'Gending Manten Jawa - Ketawang Larasmoyo (Audio Asli Keraton)',
        likes: 148200,
        likesText: '148.2K',
        commentsCount: 2418,
        vendorLabel: '🏷️ Vendor: Mamuk Tukang Makeup (Rp 9.5M)',
        comments: [
          { user: '@salsabila_bride', time: '1 jam lalu', text: 'MasyaAllah cengkorongan paesnya simetris bgt, maestro emang beda 🥺✨' },
          { user: '@dhimas_adit', time: '3 jam lalu', text: 'Ini paket Paes Ageng Jogja lengkap apa sudah termasuk melati?' },
          { user: '@mamuktukangmakeupjogja', isCreator: true, time: '2 jam lalu', text: 'Halo kak @dhimas_adit sudah lengkap sama paes prada keraton, ronce melati sekar cengkehan & asesoris manten ageng yaa 🙏' },
          { user: '@nadyawedding', time: '5 jam lalu', text: 'Bisa booking lewat rekening bersama KITA MENIKAH kak?' }
        ]
      },
      {
        id: 'reel-2',
        category: 'akad',
        vendorId: 'fg-jawara',
        creator: '@jawara.photo',
        creatorAvatar: 'assets/vendors/avatars/jawara.jpg',
        poster: 'assets/vendors/slides/jawara_slide_1.jpg',
        caption: 'Gak pernah gagal bikin nangis satu pendopo saat sungkeman minta restu bapak ibu. Bahagia selamanya Prima & Fauzan 🤍🕊️ #bersamajawara #weddingtiktok',
        audio: 'Sal Priadi - Gala Bunga Matahari (Official Wedding Audio)',
        likes: 284500,
        likesText: '284.5K',
        commentsCount: 4120,
        vendorLabel: '🏷️ Vendor: Jawara Photo (Paket Rp 3.8M)',
        comments: [
          { user: '@anisa_ramadhani', time: '30m lalu', text: 'Nangis bgt pas papanya bisikin doa restu 😭🤍' },
          { user: '@jawara.photo', isCreator: true, time: '20m lalu', text: 'Dokumentasi emosional abadi #bersamajawara kak 🙏' },
          { user: '@wedding_dreamy', time: '2 jam lalu', text: 'Tonality fotonya anget bgt ciri khas Jawara!' }
        ]
      },
      {
        id: 'reel-3',
        category: 'wo',
        vendorId: 'wo-ilona',
        creator: '@ilonaorganizer',
        creatorAvatar: 'assets/vendors/avatars/ilona.jpg',
        poster: 'assets/vendors/slides/ilona_slide_1.jpg',
        caption: 'POV: 12 jam kru WO Ilona siap siaga jagain penganten & keluarga. Dari rundown akad sampai resepsi beres tanpa pusing! 🥰🤍 #ilonaorganizer #weddingplannerjogja',
        audio: 'Nadin Amizah - Rayuan Perempuan Gila (Wedding Acoustic)',
        likes: 92400,
        likesText: '92.4K',
        commentsCount: 1850,
        vendorLabel: '🏷️ Vendor: Ilona Wedding Organizer (Rp 4.5M)',
        comments: [
          { user: '@kartika_putri', time: '1 jam lalu', text: 'Tim Ilona WO nya gercep bgt pas kebaya bridesmaid lepas kancing langsung dibenerin 👍' },
          { user: '@ilonaorganizer', isCreator: true, time: '45m lalu', text: 'Terima kasih kak Kartika! Kenyamanan & ketenangan pengantin prioritas nomor 1 kami 🤍' }
        ]
      },
      {
        id: 'reel-4',
        category: 'fyp',
        vendorId: 'cat-vidi',
        creator: '@vidicatering',
        creatorAvatar: 'assets/vendors/avatars/vidi.jpg',
        poster: 'assets/vendors/slides/vidi_slide_1.jpg',
        caption: 'Gubukan sate ayam & zuppa soup gak pernah sepi antre! Definisi tamu kondangan pulang kenyang dan senyum bahagia 🤤🍱 #cateringjogja #vidicatering',
        audio: 'Trending TikTok Sound - Wedding Food Tasting Review',
        likes: 76100,
        likesText: '76.1K',
        commentsCount: 980,
        vendorLabel: '🏷️ Vendor: Vidi Catering (Mulai Rp 65.000 / pax)',
        comments: [
          { user: '@foodie_jogja', time: '2 jam lalu', text: 'Sate ayam sama selat solonya Vidi emang legend bgt di nikahan Jogja!' },
          { user: '@budi_santoso', time: '4 jam lalu', text: 'Tamu-tamu kantor kemarin pada muji kateringnya enak semua.' }
        ]
      },
      {
        id: 'reel-5',
        category: 'paes',
        vendorId: 'mua-arnie',
        creator: '@arniesuryo',
        creatorAvatar: 'assets/vendors/avatars/arniesuryo.jpg',
        poster: 'assets/vendors/slides/arniesuryo_slide_1.jpg',
        caption: 'Tata rias Paes Ageng Jangan Menir beludru hijau lumut prada emas keraton. Anggun, ningrat, dan memancarkan aura sakral manten putri @arniesuryo 🌿✨',
        audio: 'Gending Jawa Penganten - Kebo Giro Sakral',
        likes: 112900,
        likesText: '112.9K',
        commentsCount: 1630,
        vendorLabel: '🏷️ Vendor: Arnie Suryo Paes Ageng (Rp 8.5M)',
        comments: [
          { user: '@dyah_paramita', time: '3 jam lalu', text: 'Warna hijau bludrunya ningrat bgt perpaduan sama emasnya!' },
          { user: '@arniesuryo', isCreator: true, time: '1 jam lalu', text: 'Matur nuwun sanget kak Dyah 🙏 Rahayu kagem sedaya.' }
        ]
      }
    ];

    let currentReelIndex = 0;
    let isTikTokPlaying = true;
    let isTikTokSoundOn = false;
    let audioCtx = null;
    let audioLoopTimer = null;
    let progressTimer = null;
    let currentProgress = 0;

    // WEB AUDIO API REAL WEDDING SOUND SYNTHESIZER (PENTATONIC CHIMES & WEDDING HARMONY)
    function initAudioContext() {
      if (!audioCtx) {
        audioCtx = new (window.AudioContext || window.webkitAudioContext)();
      }
      if (audioCtx.state === 'suspended') {
        audioCtx.resume();
      }
    }

    function playWeddingChime(freq, delay = 0, duration = 1.6) {
      if (!audioCtx || !isTikTokSoundOn) return;
      setTimeout(() => {
        if (!isTikTokSoundOn) return;
        const osc = audioCtx.createOscillator();
        const gain = audioCtx.createGain();
        osc.type = 'sine';
        osc.frequency.setValueAtTime(freq, audioCtx.currentTime);

        gain.gain.setValueAtTime(0.001, audioCtx.currentTime);
        gain.gain.exponentialRampToValueAtTime(0.08, audioCtx.currentTime + 0.04);
        gain.gain.exponentialRampToValueAtTime(0.0001, audioCtx.currentTime + duration);

        osc.connect(gain);
        gain.connect(audioCtx.destination);
        osc.start(audioCtx.currentTime);
        osc.stop(audioCtx.currentTime + duration);
      }, delay);
    }

    function startWeddingAudioLoop() {
      stopWeddingAudioLoop();
      initAudioContext();
      // Javanese Larasmoyo / Romantic Wedding Melody Notes: E4, G#4, A4, B4, E5, F#5
      const notes = [329.63, 415.30, 440.00, 493.88, 659.25, 493.88, 415.30];
      let noteIdx = 0;

      audioLoopTimer = setInterval(() => {
        if (!isTikTokSoundOn) return;
        playWeddingChime(notes[noteIdx % notes.length], 0, 1.8);
        if (noteIdx % 2 === 0) {
          playWeddingChime(notes[(noteIdx + 2) % notes.length] * 0.5, 120, 2.2); // bass drone
        }
        noteIdx++;
      }, 700);
    }

    function stopWeddingAudioLoop() {
      if (audioLoopTimer) clearInterval(audioLoopTimer);
      audioLoopTimer = null;
    }

    function toggleTikTokSound() {
      isTikTokSoundOn = !isTikTokSoundOn;
      const mutedIcon = document.getElementById('iconSoundMuted');
      const playingIcon = document.getElementById('iconSoundPlaying');
      const waves = document.getElementById('islandMusicWaves');
      const islandLabel = document.getElementById('dynamicIslandLabel');

      if (isTikTokSoundOn) {
        mutedIcon.classList.add('hidden');
        playingIcon.classList.remove('hidden');
        waves?.classList.remove('hidden');
        waves?.classList.add('flex');
        islandLabel?.classList.remove('hidden');
        islandLabel.innerText = '🎵 ' + tiktokReelsData[currentReelIndex].audio.split(' - ')[0];
        startWeddingAudioLoop();
      } else {
        mutedIcon.classList.remove('hidden');
        playingIcon.classList.add('hidden');
        waves?.classList.add('hidden');
        waves?.classList.remove('flex');
        islandLabel?.classList.add('hidden');
        stopWeddingAudioLoop();
      }
    }

    function renderActiveReel() {
      const reel = tiktokReelsData[currentReelIndex];
      document.getElementById('ttActivePoster').src = reel.poster;
      document.getElementById('ttAvatarImg').src = reel.creatorAvatar;
      document.getElementById('ttCreatorName').innerText = reel.creator;
      document.getElementById('ttCaptionText').innerText = reel.caption;
      document.getElementById('ttAudioTitle').innerText = reel.audio;
      document.getElementById('ttLikeCount').innerText = reel.likesText;
      document.getElementById('ttCommentCount').innerText = reel.commentsCount > 1000 ? (reel.commentsCount/1000).toFixed(1) + 'K' : reel.commentsCount;
      document.getElementById('ttVendorBtnLabel').innerText = reel.vendorLabel;
      document.getElementById('ttReelIndex').innerText = `${currentReelIndex + 1}/${tiktokReelsData.length}`;

      // Reset heart button state
      const heartIcon = document.getElementById('ttHeartIcon');
      heartIcon.classList.remove('fill-red-500', 'text-red-500');
      heartIcon.classList.add('text-white');

      // Update Dynamic Island label if playing
      const islandLabel = document.getElementById('dynamicIslandLabel');
      if (islandLabel && isTikTokSoundOn) {
        islandLabel.innerText = '🎵 ' + reel.audio.split(' - ')[0];
      }

      // Start simulated video progress bar
      currentProgress = 0;
      startProgressBar();
    }

    function startProgressBar() {
      if (progressTimer) clearInterval(progressTimer);
      const bar = document.getElementById('ttProgressBar');
      progressTimer = setInterval(() => {
        if (!isTikTokPlaying) return;
        currentProgress += 1;
        if (currentProgress > 100) currentProgress = 0;
        if (bar) bar.style.width = currentProgress + '%';
      }, 100);
    }

    function nextTikTokReel() {
      currentReelIndex = (currentReelIndex + 1) % tiktokReelsData.length;
      renderActiveReel();
    }

    function prevTikTokReel() {
      currentReelIndex = (currentReelIndex - 1 + tiktokReelsData.length) % tiktokReelsData.length;
      renderActiveReel();
    }

    function handleTikTokScreenClick(event) {
      // Double click detection
      const now = Date.now();
      if (window.lastClickTime && (now - window.lastClickTime) < 300) {
        spawnFloatingHeart(event.clientX, event.clientY);
        toggleTikTokLikeBtn(true);
        window.lastClickTime = 0;
        return;
      }
      window.lastClickTime = now;

      // Single click: Play/Pause toggle
      toggleTikTokPlay();
    }

    function toggleTikTokPlay() {
      isTikTokPlaying = !isTikTokPlaying;
      const playIcon = document.getElementById('ttPlayPauseIcon');
      const vinyl = document.getElementById('ttVinylDisc');

      if (isTikTokPlaying) {
        playIcon.classList.add('hidden');
        vinyl?.classList.add('animate-spin-slow');
        if (isTikTokSoundOn) startWeddingAudioLoop();
      } else {
        playIcon.classList.remove('hidden');
        vinyl?.classList.remove('animate-spin-slow');
        stopWeddingAudioLoop();
      }
    }

    function spawnFloatingHeart(x, y) {
      const container = document.getElementById('tiktokPlayerScreen');
      if (!container) return;
      const heart = document.createElement('div');
      heart.className = 'heart-float text-3xl text-red-500';
      heart.innerHTML = '❤️';
      const rect = container.getBoundingClientRect();
      heart.style.left = (x - rect.left) + 'px';
      heart.style.top = (y - rect.top) + 'px';
      container.appendChild(heart);
      setTimeout(() => heart.remove(), 900);
    }

    function toggleTikTokLikeBtn(forceLike = false) {
      const reel = tiktokReelsData[currentReelIndex];
      const heartIcon = document.getElementById('ttHeartIcon');
      const countLabel = document.getElementById('ttLikeCount');
      const isLiked = heartIcon.classList.contains('fill-red-500');

      if (isLiked && !forceLike) {
        heartIcon.classList.remove('fill-red-500', 'text-red-500');
        heartIcon.classList.add('text-white');
        countLabel.innerText = reel.likesText;
      } else {
        heartIcon.classList.add('fill-red-500', 'text-red-500', 'scale-125');
        setTimeout(() => heartIcon.classList.remove('scale-125'), 200);
        countLabel.innerText = ((reel.likes + 1) / 1000).toFixed(1) + 'K';
      }
    }

    function toggleTikTokBookmarkBtn() {
      const icon = document.getElementById('ttBookmarkIcon');
      const isSaved = icon.classList.contains('fill-yellow-400');
      if (isSaved) {
        icon.classList.remove('fill-yellow-400', 'text-yellow-400');
        icon.classList.add('text-white');
      } else {
        icon.classList.add('fill-yellow-400', 'text-yellow-400');
        alert('Video inspirasi pernikahan berhasil disimpan ke Wishlist TikTok KITA MENIKAH Anda!');
      }
    }

    function openActiveReelVendor() {
      const reel = tiktokReelsData[currentReelIndex];
      if (reel && reel.vendorId) {
        openVendorModal(reel.vendorId);
      }
    }

    function switchTikTokCategory(cat) {
      ['fyp', 'paes', 'akad', 'wo'].forEach(c => {
        const tab = document.getElementById(`tt-tab-${c}`);
        if (tab) {
          tab.classList.remove('text-white', 'border-b-2', 'border-white');
          tab.classList.add('text-neutral-400');
        }
      });
      const activeTab = document.getElementById(`tt-tab-${cat}`);
      if (activeTab) {
        activeTab.classList.add('text-white', 'border-b-2', 'border-white');
        activeTab.classList.remove('text-neutral-400');
      }

      // Filter to relevant reel
      if (cat !== 'fyp') {
        const idx = tiktokReelsData.findIndex(r => r.category === cat);
        if (idx !== -1) {
          currentReelIndex = idx;
          renderActiveReel();
        }
      }
    }

    // TIKTOK COMMENT SHEET CONTROLS
    function openTikTokCommentSheet() {
      const reel = tiktokReelsData[currentReelIndex];
      const sheet = document.getElementById('tiktokCommentSheet');
      const list = document.getElementById('ttCommentsList');
      const header = document.getElementById('sheetCommentHeader');

      header.innerText = `${reel.comments.length} Komentar Wedding`;
      list.innerHTML = reel.comments.map(c => `
        <div class="flex space-x-2.5 items-start">
          <div class="w-7 h-7 rounded-full bg-gradient-to-tr from-cyan-500 via-pink-500 to-red-500 p-0.5 shrink-0">
            <div class="w-full h-full rounded-full bg-neutral-900 flex items-center justify-center text-[10px] font-bold text-white">
              ${c.user[1].toUpperCase()}
            </div>
          </div>
          <div class="flex-1 space-y-0.5">
            <div class="flex items-center space-x-1.5">
              <span class="font-bold text-white text-[11px]">${c.user}</span>
              ${c.isCreator ? '<span class="text-[9px] bg-red-500 text-white px-1 rounded font-bold">Kreator</span>' : ''}
              <span class="text-[10px] text-neutral-500">${c.time}</span>
            </div>
            <p class="text-neutral-200 text-xs leading-relaxed">${c.text}</p>
          </div>
        </div>
      `).join('');

      sheet.classList.remove('hidden');
    }

    function closeTikTokCommentSheet() {
      document.getElementById('tiktokCommentSheet').classList.add('hidden');
    }

    function submitNewComment() {
      const input = document.getElementById('inputNewComment');
      const val = input.value.trim();
      if (!val) return;
      const reel = tiktokReelsData[currentReelIndex];
      reel.comments.unshift({
        user: connectedTikTokUser || '@klien.kitamenikah',
        time: 'Baru saja',
        text: val
      });
      input.value = '';
      openTikTokCommentSheet();
    }

    function toggleDynamicIslandDetails() {
      const label = document.getElementById('dynamicIslandLabel');
      if (label) {
        label.classList.toggle('hidden');
      }
    }
"""

# Replace old tiktok js helpers with complete tiktok_lite_js
if '// ==========================================' not in html:
    html = html.replace('// TIKTOK WEDDING INTERACTIVE CONTROLS', tiktok_lite_js + '\n    // TIKTOK WEDDING INTERACTIVE CONTROLS')
    print("Added TikTok Lite real engine JavaScript!")

# Update switchTab for TikTok: renderActiveReel
html = html.replace(
    "document.getElementById('viewTikTok').classList.remove('hidden');",
    "document.getElementById('viewTikTok').classList.remove('hidden');\n        renderActiveReel();"
)

# Update clock in status bar to live time
live_clock_script = """
    // REAL LIVE CLOCK ON IPHONE STATUS BAR
    function updateLiveClock() {
      const now = new Date();
      const hrs = String(now.getHours()).padStart(2, '0');
      const mins = String(now.getMinutes()).padStart(2, '0');
      const el = document.getElementById('statusBarClock');
      if (el) el.innerText = `${hrs}:${mins}`;
    }
    setInterval(updateLiveClock, 1000);
    updateLiveClock();
"""
html = html.replace('// INIT ON LOAD', live_clock_script + '\n    // INIT ON LOAD')

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Saved index.html with iPhone 16 Pro + TikTok Lite successfully!")
