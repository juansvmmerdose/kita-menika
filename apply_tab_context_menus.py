import re

file_path = r"C:\Users\VANDI\.gemini\antigravity\scratch\kita-menikah\index.html"
with open(file_path, "r", encoding="utf-8") as f:
    html = f.read()

# 1. Pindahkan #stickySearchHeader dan #clientQuickMenu ke dalam #viewHome
# Cari bagian:
# <!-- STICKY SEARCH & CITY FILTER ... -->
# ...
# <!-- VIEW 1: HOME VIEW (EKSPLORASI KLIEN) -->
# <div id="viewHome" class="space-y-4">

search_and_menu_pattern = r'(<!-- STICKY SEARCH & CITY FILTER[\s\S]*?<!-- VIEW 1: HOME VIEW \(EKSPLORASI KLIEN\) -->\s*<div id="viewHome" class="space-y-4">)'

# Kita ingin memindahkan stickySearchHeader dan clientQuickMenu ke dalam viewHome:
# <div id="viewHome" class="space-y-4">
#    <!-- STICKY SEARCH & CITY FILTER -->
#    ...
#    <!-- 8 IKON KATEGORI & MENU TERKURASI -->
#    ...

target_start_str = '<!-- STICKY SEARCH & CITY FILTER (HANYA INI YANG MENEMPEL DI ATAS SAAT DIGULIRKAN) -->'
target_viewhome_str = '<div id="viewHome" class="space-y-4">'

pos_start = html.find(target_start_str)
pos_viewhome = html.find(target_viewhome_str)

if pos_start != -1 and pos_viewhome != -1:
    headers_and_menu = html[pos_start:pos_viewhome].strip()
    # Hapus dari posisi sebelum viewHome
    html = html[:pos_start] + '<!-- VIEW 1: HOME VIEW (EKSPLORASI KLIEN) -->\n      <div id="viewHome" class="space-y-3">\n\n        ' + headers_and_menu + '\n\n' + html[pos_viewhome + len(target_viewhome_str):]
    print("Berhasil memindahkan stickySearchHeader dan clientQuickMenu ke dalam viewHome!")
else:
    print("Warning: tidak menemukan target header & quickmenu!")

# 2. Tambahkan Menu yang Sesuai di #viewBudget (Preset Anggaran Cepat dengan 4 Tombol Warna)
old_view_budget = '''      <!-- VIEW 3: BUDGET PLANNER TAB -->
      <div id="viewBudget" class="hidden px-5 py-4 space-y-6">
        <div>
          <span class="text-[10px] tracking-widest uppercase text-neutral-400">Fitur Pintar</span>
          <h2 class="text-xl font-serif-luxury font-bold text-white tracking-wide">Kalkulator Estimasi Anggaran</h2>
          <p class="text-xs text-neutral-400 mt-1">Kalkulasi pembagian anggaran ideal pernikahanmu di Jogja.</p>
        </div>'''

new_view_budget = '''      <!-- VIEW 3: BUDGET PLANNER TAB (DENGAN MENU PINTAR KHUSUS ANGGARAN) -->
      <div id="viewBudget" class="hidden space-y-4">

        <!-- DEDICATED BUDGET QUICK MENU (MENGGANTIKAN MENU TERKURASI DI TAB BUDGET) -->
        <section id="budgetQuickMenu" class="px-4 py-3 bg-neutral-950/95 border-b border-neutral-900 sticky top-0 z-30 space-y-2.5">
          <div class="flex items-center justify-between px-1">
            <div class="flex items-center space-x-1.5">
              <span class="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></span>
              <span class="text-[9px] tracking-[0.2em] uppercase font-bold text-neutral-200">Preset Anggaran Cepat</span>
            </div>
            <span class="text-[9px] text-neutral-400 font-mono">1 Klik Terapkan</span>
          </div>

          <!-- 4 PRESET ANGGARAN DENGAN WARNA KHAS MASING-MASING -->
          <div class="grid grid-cols-4 gap-2">
            <!-- 1. INTIMATE 50 JT (Rose Neon) -->
            <button onclick="applyBudgetPreset(50000000, 200, 'intimate')" id="preset-btn-intimate" class="preset-budget-btn group flex flex-col items-center text-center p-1.5 rounded-xl transition active:scale-95 bg-neutral-900/60 border border-neutral-800 hover:border-rose-500/60">
              <div class="w-10 h-10 rounded-xl bg-rose-500/15 border border-rose-500/40 text-rose-400 flex items-center justify-center group-hover:scale-105 transition shadow-sm">
                <span class="text-xs font-bold font-mono">50Jt</span>
              </div>
              <span class="text-[9px] font-bold text-rose-300 mt-1">Intimate</span>
              <span class="text-[8px] text-neutral-400">200 Tamu</span>
            </button>

            <!-- 2. STANDAR 100 JT (Warm Amber) -->
            <button onclick="applyBudgetPreset(100000000, 400, 'standar')" id="preset-btn-standar" class="preset-budget-btn group flex flex-col items-center text-center p-1.5 rounded-xl transition active:scale-95 bg-neutral-900/60 border border-neutral-800 hover:border-amber-500/60">
              <div class="w-10 h-10 rounded-xl bg-amber-500/15 border border-amber-500/40 text-amber-400 flex items-center justify-center group-hover:scale-105 transition shadow-sm">
                <span class="text-xs font-bold font-mono">100Jt</span>
              </div>
              <span class="text-[9px] font-bold text-amber-300 mt-1">Standar</span>
              <span class="text-[8px] text-neutral-400">400 Tamu</span>
            </button>

            <!-- 3. AGENG 200 JT (Sky Blue) -->
            <button onclick="applyBudgetPreset(200000000, 800, 'ageng')" id="preset-btn-ageng" class="preset-budget-btn group flex flex-col items-center text-center p-1.5 rounded-xl transition active:scale-95 bg-neutral-900/60 border border-neutral-800 hover:border-sky-500/60">
              <div class="w-10 h-10 rounded-xl bg-sky-500/15 border border-sky-500/40 text-sky-400 flex items-center justify-center group-hover:scale-105 transition shadow-sm">
                <span class="text-xs font-bold font-mono">200Jt</span>
              </div>
              <span class="text-[9px] font-bold text-sky-300 mt-1">Ageng</span>
              <span class="text-[8px] text-neutral-400">800 Tamu</span>
            </button>

            <!-- 4. SULTAN 350 JT (Royal Purple) -->
            <button onclick="applyBudgetPreset(350000000, 1000, 'sultan')" id="preset-btn-sultan" class="preset-budget-btn group flex flex-col items-center text-center p-1.5 rounded-xl transition active:scale-95 bg-neutral-900/60 border border-neutral-800 hover:border-purple-500/60">
              <div class="w-10 h-10 rounded-xl bg-purple-500/15 border border-purple-500/40 text-purple-400 flex items-center justify-center group-hover:scale-105 transition shadow-sm">
                <span class="text-xs font-bold font-mono">350Jt</span>
              </div>
              <span class="text-[9px] font-bold text-purple-300 mt-1">Sultan</span>
              <span class="text-[8px] text-neutral-400">1.000 Tamu</span>
            </button>
          </div>
        </section>

        <div class="px-5 space-y-4">
          <div>
            <span class="text-[10px] tracking-widest uppercase text-neutral-400">Alokasi & Simulasi</span>
            <h2 class="text-xl font-serif-luxury font-bold text-white tracking-wide">Kalkulator Anggaran Jogja</h2>
            <p class="text-xs text-neutral-400 mt-0.5">Rincian proporsional vendor berdasarkan standar harga pernikahan di Jogja.</p>
          </div>'''

if old_view_budget in html:
    html = html.replace(old_view_budget, new_view_budget)
    print("Berhasil memasang menu khusus Budget!")
else:
    print("Warning: old_view_budget tidak cocok persis, mencoba regex...")
    html = re.sub(
        r'<!-- VIEW 3: BUDGET PLANNER TAB -->\s*<div id="viewBudget"[^>]*>[\s\S]*?<div>\s*<span class="text-\[10px\] tracking-widest uppercase text-neutral-400">Fitur Pintar</span>[\s\S]*?</div>',
        new_view_budget,
        html,
        count=1
    )

# 3. Tambahkan Menu yang Sesuai di #viewSaved (Filter Wishlist & Quick Action Bar)
old_view_saved = '''      <!-- VIEW 4: SAVED VENDORS TAB -->
      <div id="viewSaved" class="hidden px-5 py-4 space-y-4">
        <div>
          <span class="text-[10px] tracking-widest uppercase text-neutral-400">Favorit Pasangan</span>
          <h2 class="text-xl font-serif-luxury font-bold text-white tracking-wide">Vendor Disimpan</h2>
        </div>
        <div id="savedList" class="space-y-3">
          <!-- Injected by JS -->
        </div>
      </div>'''

new_view_saved = '''      <!-- VIEW 4: SAVED VENDORS TAB (DENGAN MENU PINTAR KHUSUS WISHLIST) -->
      <div id="viewSaved" class="hidden space-y-4">

        <!-- DEDICATED SAVED QUICK MENU (MENGGANTIKAN MENU TERKURASI DI TAB TERSIMPAN) -->
        <section id="savedQuickMenu" class="px-4 py-3 bg-neutral-950/95 border-b border-neutral-900 sticky top-0 z-30 space-y-2.5">
          <div class="flex items-center justify-between px-1">
            <div class="flex items-center space-x-1.5">
              <span class="w-2 h-2 rounded-full bg-pink-500 animate-pulse"></span>
              <span class="text-[9px] tracking-[0.2em] uppercase font-bold text-neutral-200">Filter Koleksi Tersimpan</span>
            </div>
            <span id="savedCountBadge" class="text-[9px] text-neutral-400 font-mono">0 Vendor</span>
          </div>

          <!-- KATEGORI FILTER HORIZONTAL KHUSUS WISHLIST -->
          <div class="flex space-x-1.5 overflow-x-auto no-scrollbar py-0.5">
            <button onclick="filterSavedCategory('all')" id="saved-cat-all" class="saved-cat-pill px-3 py-1 rounded-full bg-white text-black text-[10px] font-bold whitespace-nowrap shadow-sm transition">
              Semua Disimpan
            </button>
            <button onclick="filterSavedCategory('photography')" id="saved-cat-photography" class="saved-cat-pill px-2.5 py-1 rounded-full bg-neutral-900 border border-neutral-800 text-neutral-300 text-[10px] font-semibold whitespace-nowrap hover:text-white transition">
              📸 Foto
            </button>
            <button onclick="filterSavedCategory('catering')" id="saved-cat-catering" class="saved-cat-pill px-2.5 py-1 rounded-full bg-neutral-900 border border-neutral-800 text-neutral-300 text-[10px] font-semibold whitespace-nowrap hover:text-white transition">
              🍽️ Catering
            </button>
            <button onclick="filterSavedCategory('venue')" id="saved-cat-venue" class="saved-cat-pill px-2.5 py-1 rounded-full bg-neutral-900 border border-neutral-800 text-neutral-300 text-[10px] font-semibold whitespace-nowrap hover:text-white transition">
              🏛️ Venue
            </button>
            <button onclick="filterSavedCategory('wo')" id="saved-cat-wo" class="saved-cat-pill px-2.5 py-1 rounded-full bg-neutral-900 border border-neutral-800 text-neutral-300 text-[10px] font-semibold whitespace-nowrap hover:text-white transition">
              📋 WO
            </button>
            <button onclick="filterSavedCategory('mua')" id="saved-cat-mua" class="saved-cat-pill px-2.5 py-1 rounded-full bg-neutral-900 border border-neutral-800 text-neutral-300 text-[10px] font-semibold whitespace-nowrap hover:text-white transition">
              💄 MUA
            </button>
            <button onclick="filterSavedCategory('mc')" id="saved-cat-mc" class="saved-cat-pill px-2.5 py-1 rounded-full bg-neutral-900 border border-neutral-800 text-neutral-300 text-[10px] font-semibold whitespace-nowrap hover:text-white transition">
              🎤 MC
            </button>
            <button onclick="filterSavedCategory('sound')" id="saved-cat-sound" class="saved-cat-pill px-2.5 py-1 rounded-full bg-neutral-900 border border-neutral-800 text-neutral-300 text-[10px] font-semibold whitespace-nowrap hover:text-white transition">
              🔊 Sound
            </button>
          </div>

          <!-- SUMMARY TOTAL ESTIMASI & REKAPAN BUTTONS -->
          <div class="flex items-center justify-between pt-1 border-t border-neutral-900 px-1">
            <div class="text-[10px] text-neutral-400 font-mono">
              <span>Total Estimasi: </span>
              <span id="savedTotalEstimate" class="font-bold text-emerald-400">Rp 0</span>
            </div>
            <div class="flex items-center space-x-1.5">
              <button onclick="exportSavedWishlist()" class="px-2.5 py-1 rounded-lg bg-neutral-900 border border-neutral-800 hover:border-emerald-500 text-[9px] text-neutral-300 hover:text-white transition flex items-center space-x-1 shadow-sm">
                <span>📄 Rekapan</span>
              </button>
              <button onclick="clearAllSaved()" class="px-2 py-1 rounded-lg bg-red-950/40 border border-red-800/40 hover:border-red-500 text-[9px] text-red-400 hover:text-white transition">
                Reset
              </button>
            </div>
          </div>
        </section>

        <div class="px-5 space-y-3">
          <div class="flex justify-between items-center">
            <div>
              <span class="text-[10px] tracking-widest uppercase text-neutral-400">Favorit Terpilih</span>
              <h2 class="text-base font-serif-luxury font-bold text-white tracking-wide">Daftar Vendor Wishlist</h2>
            </div>
            <button onclick="chatAllSavedVendors()" class="px-2.5 py-1 rounded-lg bg-emerald-500/15 border border-emerald-500/40 text-emerald-400 text-[10px] font-bold hover:bg-emerald-500/25 transition flex items-center space-x-1">
              <span>💬 Chat Vendor</span>
            </button>
          </div>
          <div id="savedList" class="space-y-3">
            <!-- Injected by JS -->
          </div>
        </div>
      </div>'''

if old_view_saved in html:
    html = html.replace(old_view_saved, new_view_saved)
    print("Berhasil memasang menu khusus Saved!")
else:
    print("Warning: old_view_saved tidak cocok persis, mencoba regex...")
    html = re.sub(
        r'<!-- VIEW 4: SAVED VENDORS TAB -->\s*<div id="viewSaved"[^>]*>[\s\S]*?</div>\s*</div>',
        new_view_saved,
        html,
        count=1
    )

# 4. Tambahkan logic JS untuk:
# - applyBudgetPreset(total, guests, key)
# - filterSavedCategory(cat)
# - exportSavedWishlist()
# - clearAllSaved()
# - chatAllSavedVendors()
# - swipe gesture detection antar tab
new_js_logic = '''
    // LOGIC PRESET ANGGARAN KHUSUS TAB BUDGET
    function applyBudgetPreset(total, guests, key) {
      const budgetInput = document.getElementById('budgetInput');
      const guestCount = document.getElementById('guestCount');
      if (budgetInput) budgetInput.value = total;
      if (guestCount) guestCount.value = guests;
      
      calculateBudget();

      // Highlight active preset button
      document.querySelectorAll('.preset-budget-btn').forEach(btn => {
        btn.classList.remove('ring-1', 'ring-white', 'bg-neutral-800');
        btn.classList.add('bg-neutral-900/60');
      });
      const activeBtn = document.getElementById(`preset-btn-${key}`);
      if (activeBtn) {
        activeBtn.classList.remove('bg-neutral-900/60');
        activeBtn.classList.add('ring-1', 'ring-white', 'bg-neutral-800');
      }
    }

    // LOGIC KHUSUS TAB TERSIMPAN (WISHLIST)
    let currentSavedCategoryFilter = 'all';

    function filterSavedCategory(cat) {
      currentSavedCategoryFilter = cat;
      document.querySelectorAll('.saved-cat-pill').forEach(btn => {
        btn.classList.remove('bg-white', 'text-black', 'font-bold');
        btn.classList.add('bg-neutral-900', 'text-neutral-300', 'font-semibold');
      });
      const activePill = document.getElementById(`saved-cat-${cat}`);
      if (activePill) {
        activePill.classList.remove('bg-neutral-900', 'text-neutral-300', 'font-semibold');
        activePill.classList.add('bg-white', 'text-black', 'font-bold');
      }
      renderSavedList();
    }

    function renderSavedList() {
      const container = document.getElementById('savedList');
      const countBadge = document.getElementById('savedCountBadge');
      const totalEstEl = document.getElementById('savedTotalEstimate');
      
      const allSaved = vendors.filter(v => savedVendorIds.has(v.id));
      const filtered = currentSavedCategoryFilter === 'all' 
        ? allSaved 
        : allSaved.filter(v => v.category === currentSavedCategoryFilter);

      // Hitung total estimasi
      const totalEst = allSaved.reduce((acc, v) => acc + (v.priceStart || 0), 0);
      if (totalEstEl) totalEstEl.innerText = formatRupiah(totalEst);
      if (countBadge) countBadge.innerText = `${allSaved.length} Vendor`;

      if (filtered.length === 0) {
        container.innerHTML = `
          <div class="text-center py-8 border border-dashed border-neutral-800 rounded-2xl p-5 bg-neutral-950/60">
            <span class="text-2xl block mb-2">🔖</span>
            <p class="text-xs text-neutral-300 font-semibold">${allSaved.length === 0 ? 'Belum ada vendor yang disimpan.' : 'Tidak ada vendor tersimpan di kategori ini.'}</p>
            <p class="text-[10px] text-neutral-500 mt-1">Tekan ikon bookmark pada postingan vendor di menu Eksplor.</p>
            <button onclick="switchTab('home')" class="mt-3 text-xs bg-white text-black px-3 py-1.5 rounded-lg font-bold">Jelajahi Vendor</button>
          </div>
        `;
        return;
      }

      container.innerHTML = filtered.map(v => `
        <div class="bg-neutral-900/90 border border-neutral-800 rounded-xl p-3 flex items-center justify-between cursor-pointer hover:border-neutral-700 transition" onclick="openVendorModal('${v.id}')">
          <div class="flex items-center space-x-3">
            <div class="w-11 h-11 rounded-full overflow-hidden border border-neutral-700 bg-neutral-950 shrink-0">
              <img src="${v.avatar}" class="w-full h-full object-cover">
            </div>
            <div>
              <div class="flex items-center space-x-1.5">
                <h4 class="text-xs font-bold text-white tracking-wide">${v.name}</h4>
                <span class="text-[9px] bg-neutral-800 text-neutral-300 px-1.5 py-0.2 rounded font-mono uppercase">${v.category}</span>
              </div>
              <div class="text-[10px] text-neutral-400 font-mono mt-0.5">
                <span>${v.igHandle}</span> • <span class="text-emerald-400 font-bold">${formatRupiah(v.priceStart)}</span>
              </div>
            </div>
          </div>
          <div class="flex items-center space-x-1">
            <button onclick="event.stopPropagation(); openChatWithVendorById('${v.id}')" class="w-7 h-7 rounded-lg bg-neutral-800 text-emerald-400 flex items-center justify-center text-xs hover:bg-neutral-700">
              💬
            </button>
            <button onclick="event.stopPropagation(); toggleSave('${v.id}')" class="w-7 h-7 rounded-lg bg-neutral-800 text-red-400 flex items-center justify-center text-xs hover:bg-red-950/60" title="Hapus dari Wishlist">
              ✕
            </button>
          </div>
        </div>
      `).join('');
    }

    function exportSavedWishlist() {
      const allSaved = vendors.filter(v => savedVendorIds.has(v.id));
      if (allSaved.length === 0) {
        alert('Wishlist masih kosong. Simpan beberapa vendor terlebih dahulu!');
        return;
      }
      const total = allSaved.reduce((sum, v) => sum + (v.priceStart || 0), 0);
      let summary = `📋 REKAPAN VENDOR WISHLIST KITA MENIKAH\\n-----------------------------------------\\n`;
      allSaved.forEach((v, i) => {
        summary += `${i+1}. [${v.category.toUpperCase()}] ${v.name} (${v.igHandle})\\n   Harga Mulai: ${formatRupiah(v.priceStart)}\\n`;
      });
      summary += `-----------------------------------------\\nTOTAL ESTIMASI: ${formatRupiah(total)}\\nGaransi Escrow Rekber Resmi KITA MENIKAH.`;
      alert(summary);
    }

    function clearAllSaved() {
      if (savedVendorIds.size === 0) return;
      if (confirm('Yakin ingin mereset seluruh daftar vendor yang disimpan?')) {
        savedVendorIds.clear();
        updateSavedBadge();
        renderSavedList();
        filterVendors();
      }
    }

    function chatAllSavedVendors() {
      const allSaved = vendors.filter(v => savedVendorIds.has(v.id));
      if (allSaved.length === 0) {
        alert('Belum ada vendor di wishlist untuk dihubungi.');
        return;
      }
      openChatWithVendorById(allSaved[0].id);
    }

    // SWIPE GESTURE DETECTION ANTAR TAB (EKSPLOR <-> TIKTOK <-> BUDGET <-> TERSIMPAN)
    let touchStartX = 0;
    let touchStartY = 0;
    const tabSequence = ['home', 'tiktok', 'budget', 'saved'];
    let currentTabIndex = 0;

    const phoneFrame = document.getElementById('iphoneDeviceFrame');
    if (phoneFrame) {
      phoneFrame.addEventListener('touchstart', (e) => {
        touchStartX = e.changedTouches[0].screenX;
        touchStartY = e.changedTouches[0].screenY;
      }, { passive: true });

      phoneFrame.addEventListener('touchend', (e) => {
        const touchEndX = e.changedTouches[0].screenX;
        const touchEndY = e.changedTouches[0].screenY;
        handleSwipeGesture(touchStartX, touchStartY, touchEndX, touchEndY);
      }, { passive: true });
    }

    function handleSwipeGesture(startX, startY, endX, endY) {
      const diffX = endX - startX;
      const diffY = endY - startY;
      
      // Pastikan gerakan horizontal lebih dominan daripada vertikal & minimal 60px
      if (Math.abs(diffX) > Math.abs(diffY) && Math.abs(diffX) > 60) {
        if (diffX < 0) {
          // Swipe ke kiri -> Tab berikutnya
          currentTabIndex = (currentTabIndex + 1) % tabSequence.length;
          switchTab(tabSequence[currentTabIndex]);
        } else {
          // Swipe ke kanan -> Tab sebelumnya
          currentTabIndex = (currentTabIndex - 1 + tabSequence.length) % tabSequence.length;
          switchTab(tabSequence[currentTabIndex]);
        }
      }
    }
'''

# Sisipkan new_js_logic sebelum updateSavedBadge();
pos_script_end = html.find('updateSavedBadge();')
if pos_script_end != -1:
    html = html[:pos_script_end] + new_js_logic + "\n      " + html[pos_script_end:]
    print("Berhasil menyisipkan JS logic baru untuk Budget, Saved, dan Swipe gestures!")

# Pastikan di switchTab, saat tab berpindah, currentTabIndex juga ikut tersinkronisasi
old_switch_tab = '''    function switchTab(tab) {
      if (currentAppMode === 'vendor') {
        toggleAppMode(); // switch back to client when clicking dock tabs
      }'''

new_switch_tab = '''    function switchTab(tab) {
      if (currentAppMode === 'vendor') {
        toggleAppMode(); // switch back to client when clicking dock tabs
      }
      const idx = tabSequence.indexOf(tab);
      if (idx !== -1) currentTabIndex = idx;'''

if old_switch_tab in html:
    html = html.replace(old_switch_tab, new_switch_tab)
    print("Tersinkronisasi currentTabIndex di switchTab!")

with open(file_path, "w", encoding="utf-8") as f:
    f.write(html)

print("Updated index.html saved! New length:", len(html))
