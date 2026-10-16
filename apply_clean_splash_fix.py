import re

file_path = r"C:\Users\VANDI\.gemini\antigravity\scratch\kita-menikah\index.html"
with open(file_path, "r", encoding="utf-8") as f:
    html = f.read()

# 1. Update CSS Animations: Clean, minimal font slide & fade, NO BUBBLES
old_styles_pattern = r'/\* LUXURY SPLASH SCREEN & IPHONE HOMESCREEN ANIMATIONS \*/[\s\S]*?\.animate-pulse-aura\s*\{[\s\S]*?\}'

clean_styles = '''/* MINIMALIST & SLEEK SPLASH SCREEN ANIMATIONS */
    @keyframes splashLogoFade {
      0% {
        opacity: 0;
        transform: scale(0.92);
      }
      100% {
        opacity: 1;
        transform: scale(1);
      }
    }

    @keyframes splashFontEnter {
      0% {
        opacity: 0;
        transform: translateY(10px);
      }
      100% {
        opacity: 1;
        transform: translateY(0);
      }
    }

    .animate-splash-logo {
      animation: splashLogoFade 0.7s cubic-bezier(0.16, 1, 0.3, 1) forwards;
    }

    .animate-splash-font {
      animation: splashFontEnter 0.8s cubic-bezier(0.16, 1, 0.3, 1) 0.2s both;
    }'''

if re.search(old_styles_pattern, html):
    html = re.sub(old_styles_pattern, clean_styles, html, count=1)
    print("Replaced CSS animations with clean font entrance!")
else:
    print("Warning: old_styles_pattern not matched, trying manual replacement...")
    # fallback
    pos_s = html.find('/* LUXURY SPLASH SCREEN')
    pos_e = html.find('</style>')
    if pos_s != -1 and pos_e != -1:
        html = html[:pos_s] + clean_styles + '\n  ' + html[pos_e:]
        print("Fallback replacement of CSS animations done!")

# 2. Update Homescreen App Icon: Remove ambient aura bubble, keep clean authentic iOS icon
old_icon_block = '''          <!-- ============================================================ -->
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
          </div>'''

new_icon_block = '''          <!-- ============================================================ -->
          <!-- ★ APP UTAMA: KITA MENIKAH (BERSIH, TANPA BUBBLE ANEH) -->
          <!-- ============================================================ -->
          <div class="flex flex-col items-center cursor-pointer group" onclick="launchKitaMenikahApp()" id="appIconKitaMenikahWrapper">
            <div class="relative">
              <!-- Ikon iOS Asli Bersih -->
              <div id="bubbleKitaMenikah" class="w-14 h-14 rounded-[16px] overflow-hidden bg-black border border-white/20 shadow-xl group-hover:scale-105 active:scale-90 transition-transform duration-150">
                <img src="assets/app_logo.png" alt="Kita Menikah" class="w-full h-full object-cover">
              </div>

              <!-- Notification Badge (1) -->
              <span class="absolute -top-1 -right-1 w-4 h-4 rounded-full bg-red-500 text-white text-[9px] font-bold flex items-center justify-center border border-black shadow">1</span>
            </div>

            <!-- Teks di Bawah Aplikasi: (kita menikah) -->
            <span class="text-[11px] font-medium text-white/95 tracking-tight block text-center mt-1 drop-shadow font-sans">
              (kita menikah)
            </span>
          </div>'''

if old_icon_block in html:
    html = html.replace(old_icon_block, new_icon_block)
    print("Updated homescreen icon markup!")
else:
    print("Warning: old_icon_block not matched directly!")

# 3. Update Splash Screen: NO BUBBLES, NO WEIRD HALOS, CLEAN FONT ENTRY, TIDAK KITA MENI KAH
old_splash_block = '''    <!-- ============================================================ -->
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
    </div>'''

new_splash_block = '''    <!-- ============================================================ -->
    <!-- CLEAN & LUXURIOUS SPLASH SCREEN (ANIMASI FONT MASUK RAPI) -->
    <!-- ============================================================ -->
    <div id="appSplashScreen" class="hidden absolute inset-0 z-50 bg-black flex-col items-center justify-center p-6 text-center select-none transition-opacity duration-500" onclick="skipSplashAnimation()">
      
      <!-- Minimalist Logo Image -->
      <div id="splashLogoBox" class="w-20 h-20 rounded-2xl overflow-hidden mb-5 shadow-2xl opacity-0">
        <img src="assets/app_logo.png" alt="Kita Menikah" class="w-full h-full object-cover">
      </div>

      <!-- ANIMASI FONT MASUK YANG RAPI & PAS (SATU BARIS, TIDAK TERPOTONG) -->
      <div id="splashTypography" class="space-y-2 opacity-0 px-2 max-w-full">
        <h1 class="text-xl md:text-2xl font-serif-luxury font-bold tracking-[0.16em] text-white uppercase whitespace-nowrap text-center drop-shadow-md">
          KITA MENIKAH
        </h1>
        <p class="text-[9px] tracking-[0.22em] text-neutral-400 uppercase font-sans font-medium whitespace-nowrap text-center">
          The Curated Wedding Marketplace
        </p>
        <div class="w-12 h-px bg-neutral-800 mx-auto mt-2"></div>
        <span class="text-[8px] tracking-[0.25em] text-neutral-600 font-mono block">
          DI YOGYAKARTA
        </span>
      </div>

    </div>'''

if old_splash_block in html:
    html = html.replace(old_splash_block, new_splash_block)
    print("Replaced splash screen with clean font entrance!")
else:
    print("Warning: old_splash_block not matched directly!")

# 4. Update launchKitaMenikahApp() to use the new animations cleanly
old_launch_fn = '''    function launchKitaMenikahApp() {
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
    }'''

new_launch_fn = '''    function launchKitaMenikahApp() {
      if (isAppOpen) return;
      isAppOpen = true;

      const homescreen = document.getElementById('iosHomeScreen');
      const splash = document.getElementById('appSplashScreen');
      const mainScreen = document.getElementById('appMainScreen');
      const logoBox = document.getElementById('splashLogoBox');
      const typography = document.getElementById('splashTypography');

      // 1. Play Soft Subtle Chime Sound
      playAppLaunchChime();

      // 2. Smooth fade of homescreen
      if (homescreen) {
        homescreen.classList.add('opacity-0', 'pointer-events-none');
      }

      // 3. Show clean splash screen
      if (splash) {
        splash.classList.remove('hidden');
        splash.classList.remove('opacity-0', 'pointer-events-none');
        splash.classList.add('flex', 'opacity-100');

        // Apply clean logo and font animations
        if (logoBox) {
          logoBox.classList.remove('animate-splash-logo');
          void logoBox.offsetWidth;
          logoBox.classList.add('animate-splash-logo');
        }

        if (typography) {
          typography.classList.remove('animate-splash-font');
          void typography.offsetWidth;
          typography.classList.add('animate-splash-font');
        }
      }

      // 4. Snappy auto-transition to app after 1.25 seconds
      splashTimer = setTimeout(() => {
        skipSplashAnimation();
      }, 1300);
    }'''

if old_launch_fn in html:
    html = html.replace(old_launch_fn, new_launch_fn)
    print("Updated launchKitaMenikahApp logic!")
else:
    print("Warning: old_launch_fn not matched directly!")

with open(file_path, "w", encoding="utf-8") as f:
    f.write(html)

print("Updated index.html saved! Length:", len(html))
