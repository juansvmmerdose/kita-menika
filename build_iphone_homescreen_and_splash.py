import re

file_path = r"C:\Users\VANDI\.gemini\antigravity\scratch\kita-menikah\index.html"
with open(file_path, "r", encoding="utf-8") as f:
    html = f.read()

# 1. Tambahkan CSS Animations untuk Ring Drop, Diamond Sparkle, Font Emerge, dan App Zoom
new_styles = '''
    /* LUXURY SPLASH SCREEN & IPHONE HOMESCREEN ANIMATIONS */
    @keyframes ringDrop {
      0% {
        transform: translateY(-110px) scale(0.4) rotate(-16deg);
        opacity: 0;
        filter: blur(10px) brightness(1.6);
      }
      55% {
        transform: translateY(14px) scale(1.08) rotate(3deg);
        opacity: 1;
        filter: blur(0px) brightness(1.3);
      }
      75% {
        transform: translateY(-6px) scale(0.96) rotate(-1deg);
      }
      100% {
        transform: translateY(0) scale(1) rotate(0deg);
        opacity: 1;
        filter: blur(0px) brightness(1);
      }
    }

    @keyframes fontEmerge {
      0% {
        opacity: 0;
        transform: translateY(18px);
        letter-spacing: 0.12em;
        filter: blur(6px);
      }
      100% {
        opacity: 1;
        transform: translateY(0);
        letter-spacing: 0.28em;
        filter: blur(0);
      }
    }

    @keyframes diamondGlint {
      0%, 100% {
        opacity: 0;
        transform: scale(0) rotate(0deg);
      }
      45% {
        opacity: 1;
        transform: scale(1.6) rotate(90deg);
      }
      70% {
        opacity: 0.9;
        transform: scale(1.1) rotate(140deg);
      }
    }

    @keyframes pulseAura {
      0%, 100% {
        transform: scale(1);
        opacity: 0.35;
      }
      50% {
        transform: scale(1.25);
        opacity: 0.75;
      }
    }

    .animate-ring-drop {
      animation: ringDrop 1.25s cubic-bezier(0.22, 1, 0.36, 1) forwards;
    }

    .animate-font-emerge {
      animation: fontEmerge 1.1s cubic-bezier(0.16, 1, 0.3, 1) 0.5s both;
    }

    .animate-diamond-glint {
      animation: diamondGlint 1s ease-in-out 0.7s forwards;
    }

    .animate-pulse-aura {
      animation: pulseAura 2.5s ease-in-out infinite;
    }
'''

# Masukkan new_styles sebelum </style>
if '/* LUXURY SPLASH SCREEN & IPHONE HOMESCREEN ANIMATIONS */' not in html:
    html = html.replace('</style>', new_styles + '\n  </style>')
    print("CSS animations added!")

# 2. Definisikan komponen HTML:
# - Earpiece speaker slit
# - #iosHomeScreen (iOS 18 Realistic Homescreen)
# - #appSplashScreen (Cincin jatuh + font kita menikah)
# - Wrap #appContainer & #bottomDockWrapper di dalam #appMainScreen

homescreen_and_splash_html = '''
    <!-- IPHONE SPEAKER EARPIECE SLIT (AT TOP BEZEL FOR PHYSICAL REALISM) -->
    <div class="absolute top-1.5 left-1/2 -translate-x-1/2 w-14 h-1 bg-[#151518] rounded-full z-50 pointer-events-none border-t border-white/5"></div>

    <!-- ============================================================ -->
    <!-- REALISTIC iOS 18 HOMESCREEN (STARTING STATE) -->
    <!-- ============================================================ -->
    <div id="iosHomeScreen" class="absolute inset-0 z-40 flex flex-col justify-between pt-14 pb-3 px-5 bg-gradient-to-b from-[#0c0e18] via-[#080910] to-[#030306] select-none transition-all duration-500 overflow-hidden">
      
      <!-- Top iOS Widgets (Real-time Clock, Date, Weather) -->
      <div class="space-y-4">
        <!-- iOS Clock & Date Widget Card -->
        <div class="bg-white/10 backdrop-blur-2xl rounded-3xl p-4 border border-white/15 shadow-2xl flex justify-between items-center text-white">
          <div>
            <span id="homescreenDateLabel" class="text-xs font-semibold text-white/80 block uppercase tracking-wider font-sans">JUMAT, 16 OKTOBER</span>
            <div id="homescreenBigClock" class="text-3xl font-bold font-mono tracking-tight text-white mt-0.5">09:41</div>
          </div>
          <div class="text-right">
            <span class="text-xs font-medium text-white/90 flex items-center justify-end space-x-1">
              <span>🌤️ 28°C</span>
            </span>
            <span class="text-[10px] text-white/60 font-sans block mt-0.5">Yogyakarta • Cerah</span>
          </div>
        </div>

        <!-- APP ICONS GRID (4 COLUMNS - AUTHENTIC iOS 18 LAYOUT) -->
        <div class="grid grid-cols-4 gap-y-5 gap-x-4 pt-1">
          
          <!-- App 1: FaceTime -->
          <div class="flex flex-col items-center">
            <div class="w-14 h-14 rounded-[16px] bg-gradient-to-tr from-emerald-600 to-green-400 p-3 flex items-center justify-center shadow-lg active:scale-90 transition">
              <svg class="w-8 h-8 text-white" fill="currentColor" viewBox="0 0 24 24"><path d="M17 10.5V7a1 1 0 0 0-1-1H4a1 1 0 0 0-1 1v10a1 1 0 0 0 1 1h12a1 1 0 0 0 1-1v-3.5l4 4v-11l-4 4z"/></svg>
            </div>
            <span class="text-[11px] text-white/90 font-medium tracking-tight mt-1">FaceTime</span>
          </div>

          <!-- App 2: Kalender -->
          <div class="flex flex-col items-center">
            <div class="w-14 h-14 rounded-[16px] bg-white text-black p-2 flex flex-col items-center justify-center shadow-lg active:scale-90 transition">
              <span class="text-[8px] font-bold text-red-500 uppercase leading-none">JUM</span>
              <span class="text-xl font-bold leading-none mt-0.5">16</span>
            </div>
            <span class="text-[11px] text-white/90 font-medium tracking-tight mt-1">Kalender</span>
          </div>

          <!-- App 3: Foto -->
          <div class="flex flex-col items-center">
            <div class="w-14 h-14 rounded-[16px] bg-white p-2.5 flex items-center justify-center shadow-lg active:scale-90 transition">
              <div class="w-7 h-7 rounded-full bg-gradient-to-tr from-yellow-400 via-pink-500 to-sky-400 flex items-center justify-center">
                <div class="w-3.5 h-3.5 rounded-full bg-white"></div>
              </div>
            </div>
            <span class="text-[11px] text-white/90 font-medium tracking-tight mt-1">Foto</span>
          </div>

          <!-- App 4: Kamera -->
          <div class="flex flex-col items-center">
            <div class="w-14 h-14 rounded-[16px] bg-gradient-to-tr from-neutral-800 to-neutral-700 p-3 flex items-center justify-center shadow-lg active:scale-90 transition">
              <svg class="w-7 h-7 text-neutral-300" fill="currentColor" viewBox="0 0 24 24"><path d="M12 9a3 3 0 1 0 0 6 3 3 0 0 0 0-6m-7 8a2 2 0 0 1-2-2V9a2 2 0 0 1 2-2h1.172a2 2 0 0 0 1.414-.586l.828-.828A2 2 0 0 1 9.828 5h4.344a2 2 0 0 1 1.414.586l.828.828A2 2 0 0 0 17.828 7H19a2 2 0 0 1 2 2v6a2 2 0 0 1-2 2H5z"/></svg>
            </div>
            <span class="text-[11px] text-white/90 font-medium tracking-tight mt-1">Kamera</span>
          </div>

          <!-- App 5: Mail -->
          <div class="flex flex-col items-center">
            <div class="w-14 h-14 rounded-[16px] bg-gradient-to-tr from-blue-600 to-sky-400 p-3 flex items-center justify-center shadow-lg active:scale-90 transition">
              <svg class="w-7 h-7 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"/></svg>
            </div>
            <span class="text-[11px] text-white/90 font-medium tracking-tight mt-1">Mail</span>
          </div>

          <!-- App 6: Instagram -->
          <div class="flex flex-col items-center">
            <div class="w-14 h-14 rounded-[16px] bg-gradient-to-tr from-yellow-500 via-rose-500 to-purple-600 p-3 flex items-center justify-center shadow-lg active:scale-90 transition">
              <svg class="w-7 h-7 text-white" fill="currentColor" viewBox="0 0 24 24"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z"/></svg>
            </div>
            <span class="text-[11px] text-white/90 font-medium tracking-tight mt-1">Instagram</span>
          </div>

          <!-- App 7: TikTok -->
          <div class="flex flex-col items-center">
            <div class="w-14 h-14 rounded-[16px] bg-black border border-white/20 p-3 flex items-center justify-center shadow-lg active:scale-90 transition">
              <svg class="w-7 h-7 text-white" viewBox="0 0 24 24" fill="currentColor"><path d="M19.59 6.69a4.83 4.83 0 0 1-3.77-4.25V2h-3.45v13.67a2.89 2.89 0 0 1-5.2 1.74 2.89 2.89 0 0 1 2.31-4.64 2.93 2.93 0 0 1 .88.13V9.4a6.84 6.84 0 0 0-1-.05A6.33 6.33 0 0 0 5 20.1a6.34 6.34 0 0 0 10.86-4.43v-7a8.16 8.16 0 0 0 4.77 1.52v-3.4a4.85 4.85 0 0 1-1.04-.1z"/></svg>
            </div>
            <span class="text-[11px] text-white/90 font-medium tracking-tight mt-1">TikTok</span>
          </div>

          <!-- ============================================================ -->
          <!-- ★ APP UTAMA: KITA MENIKAH (SESUAI PERMINTAAN USER) -->
          <!-- ============================================================ -->
          <div class="flex flex-col items-center cursor-pointer group" onclick="launchKitaMenikahApp()" id="appIconKitaMenikahWrapper">
            <div class="relative">
              <!-- Ambient Glow Aura -->
              <div class="absolute -inset-1 bg-gradient-to-r from-pink-500/30 to-amber-500/30 rounded-[20px] blur-sm animate-pulse-aura"></div>
              
              <!-- Ikon Kotak Bulat (Bubble Aplikasi dengan Logo Rings User) -->
              <div id="bubbleKitaMenikah" class="relative w-14 h-14 rounded-[16px] overflow-hidden bg-black border border-white/30 shadow-2xl p-0.5 group-hover:scale-105 active:scale-90 transition-transform duration-200">
                <img src="assets/app_logo.png" alt="Kita Menikah" class="w-full h-full object-cover rounded-[14px]">
              </div>

              <!-- Notification Badge (1 Wedding Booking) -->
              <span class="absolute -top-1 -right-1 w-4 h-4 rounded-full bg-red-500 text-white text-[9px] font-bold flex items-center justify-center border border-black shadow">1</span>
            </div>

            <!-- Teks di Bawah Bubble Aplikasi: (kita menikah) -->
            <span class="text-[11px] font-medium text-white/95 tracking-tight block text-center mt-1 drop-shadow font-sans">
              (kita menikah)
            </span>
          </div>

        </div>
      </div>

      <!-- Bottom Page Dots & iOS Dock -->
      <div class="space-y-3 pb-1">
        <!-- Page Indicator Dots -->
        <div class="flex justify-center items-center space-x-1.5 opacity-60">
          <span class="w-1.5 h-1.5 rounded-full bg-white"></span>
          <span class="w-1.5 h-1.5 rounded-full bg-white/40"></span>
        </div>

        <!-- FROSTED GLASS iOS BOTTOM DOCK -->
        <div class="bg-white/10 backdrop-blur-2xl rounded-[30px] p-2.5 flex justify-around items-center border border-white/15 shadow-2xl">
          <!-- Dock 1: Phone -->
          <div class="w-12 h-12 rounded-[14px] bg-emerald-500 p-2.5 flex items-center justify-center shadow-md active:scale-90 transition cursor-pointer">
            <svg class="w-6 h-6 text-white" fill="currentColor" viewBox="0 0 24 24"><path d="M6.62 10.79a15.053 15.053 0 0 0 6.59 6.59l2.2-2.2a1 1 0 0 1 1.02-.24 11.72 11.72 0 0 0 3.67.59 1 1 0 0 1 1 1V20a1 1 0 0 1-1 1A17 17 0 0 1 3 4a1 1 0 0 1 1-1h3.5a1 1 0 0 1 1 1 11.72 11.72 0 0 0 .59 3.67 1 1 0 0 1-.24 1.02l-2.22 2.1z"/></svg>
          </div>
          <!-- Dock 2: Safari -->
          <div class="w-12 h-12 rounded-[14px] bg-gradient-to-tr from-sky-500 to-blue-600 p-2.5 flex items-center justify-center shadow-md active:scale-90 transition cursor-pointer">
            <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10" stroke-width="2"/><polygon points="16.24 7.76 14.12 14.12 7.76 16.24 9.88 9.88 16.24 7.76" fill="currentColor"/></svg>
          </div>
          <!-- Dock 3: Messages -->
          <div class="w-12 h-12 rounded-[14px] bg-green-500 p-2.5 flex items-center justify-center shadow-md active:scale-90 transition cursor-pointer">
            <svg class="w-6 h-6 text-white" fill="currentColor" viewBox="0 0 24 24"><path d="M20 2H4c-1.1 0-2 .9-2 2v18l4-4h14c1.1 0 2-.9 2-2V4c0-1.1-.9-2-2-2z"/></svg>
          </div>
          <!-- Dock 4: Music -->
          <div class="w-12 h-12 rounded-[14px] bg-gradient-to-tr from-rose-500 to-red-600 p-2.5 flex items-center justify-center shadow-md active:scale-90 transition cursor-pointer">
            <svg class="w-6 h-6 text-white" fill="currentColor" viewBox="0 0 24 24"><path d="M12 3v10.55c-.59-.34-1.27-.55-2-.55-2.21 0-4 1.79-4 4s1.79 4 4 4 4-1.79 4-4V7h4V3h-6z"/></svg>
          </div>
        </div>

        <!-- Homescreen Bottom Indicator -->
        <div class="w-32 h-1 bg-white/40 rounded-full mx-auto pointer-events-none"></div>
      </div>

    </div>

    <!-- ============================================================ -->
    <!-- ELEGANT SPLASH SCREEN (ANIMASI CINCIN JATUH + SUSUL FONT) -->
    <!-- ============================================================ -->
    <div id="appSplashScreen" class="hidden absolute inset-0 z-50 bg-black flex-col items-center justify-center p-6 text-center select-none transition-all duration-700" onclick="skipSplashAnimation()">
      
      <!-- Ambient Silver Radial Glow -->
      <div class="absolute w-72 h-72 rounded-full bg-white/5 blur-3xl pointer-events-none"></div>

      <!-- ANIMASI CINCIN JATUH (RINGS DROP WITH BOUNCE) -->
      <div id="splashRingsWrapper" class="relative mb-6">
        <!-- Glowing Halo Backdrop -->
        <div class="absolute -inset-4 bg-gradient-to-tr from-white/20 via-sky-300/15 to-transparent rounded-full blur-xl pointer-events-none"></div>
        
        <!-- Center Rings Image (from user's uploaded logo) -->
        <div class="relative w-36 h-36 flex items-center justify-center">
          <img src="assets/rings_only.png" alt="Wedding Rings" class="w-full h-full object-contain filter drop-shadow-[0_15px_35px_rgba(255,255,255,0.4)]">
          
          <!-- DIAMOND SPARKLE GLINT EFFECT (KILAUAN PERMATA) -->
          <div id="splashDiamondSparkle" class="absolute top-2 right-8 pointer-events-none opacity-0">
            <svg class="w-8 h-8 text-white filter drop-shadow-[0_0_12px_#ffffff]" viewBox="0 0 24 24" fill="currentColor">
              <path d="M12 0L14.59 9.41L24 12L14.59 14.59L12 24L9.41 14.59L0 12L9.41 9.41L12 0Z"/>
            </svg>
          </div>
        </div>
      </div>

      <!-- SUSUL FONT "KITA MENIKAH" SECARA ELEGAN -->
      <div id="splashTypography" class="space-y-1.5 opacity-0">
        <span class="text-[9px] tracking-[0.35em] text-neutral-400 uppercase font-sans font-medium block">
          The Curated Wedding Marketplace
        </span>
        <h1 class="text-2xl font-bold tracking-[0.28em] font-serif-luxury text-white uppercase drop-shadow-lg">
          K I T A &nbsp; M E N I K A H
        </h1>
        <div class="w-16 h-0.5 bg-gradient-to-r from-transparent via-white/50 to-transparent mx-auto my-2"></div>
        <span class="text-[8px] tracking-[0.3em] text-neutral-500 font-mono block">
          DI YOGYAKARTA • 2026
        </span>
      </div>

      <!-- Skip Button Hint at Bottom -->
      <span class="absolute bottom-6 text-[10px] text-neutral-600 font-mono tracking-widest uppercase">
        Sentuh layar untuk melewati
      </span>
    </div>

    <!-- ============================================================ -->
    <!-- KITA MENIKAH APP MAIN SCREEN WRAPPER -->
    <!-- ============================================================ -->
    <div id="appMainScreen" class="absolute inset-0 z-30 flex flex-col bg-black transition-all duration-500">
'''

# Cari posisi awal appContainer:
# <!-- MAIN APP SCREEN WRAPPER -->
# <div id="appContainer"
pos_app_container = html.find('<!-- MAIN APP SCREEN WRAPPER -->')

if pos_app_container != -1:
    html = html[:pos_app_container] + homescreen_and_splash_html + '\n    ' + html[pos_app_container:]
    print("Homescreen and splash screen HTML injected!")
else:
    print("Warning: pos_app_container not found!")

# Sekarang cari penutup appContainer & bottomDockWrapper:
# <!-- IPHONE BOTTOM HOME INDICATOR BAR -->
# <div class="w-28 h-1 bg-white/35 rounded-full mx-auto my-1 pointer-events-none"></div>
# </div>
# Kita ubah home indicator bar agar interaktif: bisa diklik/diswipe untuk kembali ke Homescreen!
old_home_indicator = '''      <!-- IPHONE BOTTOM HOME INDICATOR BAR -->
      <div class="w-28 h-1 bg-white/35 rounded-full mx-auto my-1 pointer-events-none"></div>
    </div>'''

new_home_indicator = '''      <!-- IPHONE BOTTOM HOME INDICATOR BAR (INTERAKTIF: KETUK UNTUK KEMBALI KE HOMESCREEN) -->
      <div onclick="returnToHomeScreen()" title="Ketuk untuk kembali ke Homescreen iPhone" class="group py-1 cursor-pointer flex flex-col items-center">
        <div class="w-32 h-1 bg-white/40 group-hover:bg-white/90 group-hover:h-1.5 active:scale-95 transition-all rounded-full shadow-sm"></div>
      </div>
    </div>
  </div> <!-- CLOSE #appMainScreen -->'''

if old_home_indicator in html:
    html = html.replace(old_home_indicator, new_home_indicator)
    print("Home indicator updated and appMainScreen closed!")
else:
    print("Warning: old_home_indicator not matched exactly!")

# 3. Tambahkan Javascript untuk membuka app, animasi cincin jatuh & audio, dan kembali ke homescreen
new_app_launcher_js = '''
    // ============================================================
    // CONTROLLER BUKA APLIKASI, SPLASH SCREEN & KEMBALI KE HOMESCREEN
    // ============================================================
    let isAppOpen = false;
    let splashTimer = null;

    function playAppLaunchChime() {
      try {
        const AudioContext = window.AudioContext || window.webkitAudioContext;
        if (!AudioContext) return;
        const ctx = new AudioContext();
        if (ctx.state === 'suspended') ctx.resume();

        // Romantic crystal bell notes: E5 (659Hz) -> G#5 (830Hz) -> B5 (987Hz)
        const notes = [659.25, 830.61, 987.77];
        notes.forEach((freq, i) => {
          setTimeout(() => {
            const osc = ctx.createOscillator();
            const gain = ctx.createGain();
            osc.type = 'sine';
            osc.frequency.setValueAtTime(freq, ctx.currentTime);

            gain.gain.setValueAtTime(0.0001, ctx.currentTime);
            gain.gain.exponentialRampToValueAtTime(0.09, ctx.currentTime + 0.04);
            gain.gain.exponentialRampToValueAtTime(0.0001, ctx.currentTime + 1.2);

            osc.connect(gain);
            gain.connect(ctx.destination);
            osc.start(ctx.currentTime);
            osc.stop(ctx.currentTime + 1.2);
          }, i * 160);
        });
      } catch(e) {
        console.log('Audio chime not allowed yet:', e);
      }
    }

    function launchKitaMenikahApp() {
      if (isAppOpen) return;
      isAppOpen = true;

      const homescreen = document.getElementById('iosHomeScreen');
      const splash = document.getElementById('appSplashScreen');
      const mainScreen = document.getElementById('appMainScreen');
      const ringsWrapper = document.getElementById('splashRingsWrapper');
      const diamondSparkle = document.getElementById('splashDiamondSparkle');
      const typography = document.getElementById('splashTypography');

      // 1. Play Soft Luxury Wedding Chime Sound
      playAppLaunchChime();

      // 2. Hide homescreen with scale-up transition
      if (homescreen) {
        homescreen.classList.add('scale-125', 'opacity-0', 'pointer-events-none');
      }

      // 3. Show Splash Screen with Falling Rings Animation
      if (splash) {
        splash.classList.remove('hidden');
        splash.classList.remove('opacity-0', 'pointer-events-none', 'scale-105');
        splash.classList.add('flex', 'opacity-100');

        // Reset and apply animation classes
        if (ringsWrapper) {
          ringsWrapper.classList.remove('animate-ring-drop');
          void ringsWrapper.offsetWidth; // trigger reflow
          ringsWrapper.classList.add('animate-ring-drop');
        }

        if (diamondSparkle) {
          diamondSparkle.classList.remove('animate-diamond-glint');
          void diamondSparkle.offsetWidth;
          diamondSparkle.classList.add('animate-diamond-glint');
        }

        if (typography) {
          typography.classList.remove('animate-font-emerge');
          void typography.offsetWidth;
          typography.classList.add('animate-font-emerge');
        }
      }

      // 4. Auto-transition to Main App after 1.8 seconds
      splashTimer = setTimeout(() => {
        skipSplashAnimation();
      }, 1900);
    }

    function skipSplashAnimation() {
      if (splashTimer) clearTimeout(splashTimer);
      const splash = document.getElementById('appSplashScreen');
      const mainScreen = document.getElementById('appMainScreen');

      if (splash) {
        splash.classList.add('opacity-0', 'pointer-events-none', 'scale-105');
        setTimeout(() => {
          splash.classList.add('hidden');
          splash.classList.remove('flex');
        }, 600);
      }

      if (mainScreen) {
        mainScreen.classList.remove('translate-y-full', 'opacity-0');
      }
    }

    function returnToHomeScreen() {
      isAppOpen = false;
      const homescreen = document.getElementById('iosHomeScreen');
      const splash = document.getElementById('appSplashScreen');
      const mainScreen = document.getElementById('appMainScreen');

      // Slide down main screen
      if (mainScreen) {
        mainScreen.classList.add('translate-y-full', 'opacity-0');
      }

      // Hide splash if any
      if (splash) {
        splash.classList.add('hidden', 'opacity-0', 'pointer-events-none');
        splash.classList.remove('flex');
      }

      // Reveal iOS Homescreen
      if (homescreen) {
        homescreen.classList.remove('scale-125', 'opacity-0', 'pointer-events-none');
      }
    }

    // UPDATE HOMESCREEN LIVE CLOCK & DATE
    function updateHomescreenClock() {
      const now = new Date();
      const hrs = String(now.getHours()).padStart(2, '0');
      const mins = String(now.getMinutes()).padStart(2, '0');
      
      const bigClock = document.getElementById('homescreenBigClock');
      if (bigClock) bigClock.innerText = `${hrs}:${mins}`;

      const days = ['MINGGU', 'SENIN', 'SELASA', 'RABU', 'KAMIS', 'JUMAT', 'SABTU'];
      const months = ['JANUARI', 'FEBRUARI', 'MARET', 'APRIL', 'MEI', 'JUNI', 'JULI', 'AGUSTUS', 'SEPTEMBER', 'OKTOBER', 'NOVEMBER', 'DESEMBER'];
      
      const dateLabel = document.getElementById('homescreenDateLabel');
      if (dateLabel) {
        dateLabel.innerText = `${days[now.getDay()]}, ${now.getDate()} ${months[now.getMonth()]}`;
      }
    }
    setInterval(updateHomescreenClock, 1000);
    updateHomescreenClock();
'''

pos_script_close = html.rfind('</script>')
if pos_script_close != -1:
    html = html[:pos_script_close] + new_app_launcher_js + '\n  ' + html[pos_script_close:]
    print("App launcher JS logic added!")

with open(file_path, "w", encoding="utf-8") as f:
    f.write(html)

print("Updated index.html saved! New length:", len(html))
