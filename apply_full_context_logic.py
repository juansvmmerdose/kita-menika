file_path = r"C:\Users\VANDI\.gemini\antigravity\scratch\kita-menikah\index.html"
with open(file_path, "r", encoding="utf-8") as f:
    html = f.read()

# 1. Pastikan tabSequence didefinisikan sebelum switchTab
old_before_switch = '''    function switchTab(tab) {
      if (currentAppMode === 'vendor') {
        toggleAppMode(); // switch back to client when clicking dock tabs
      }
      const idx = tabSequence.indexOf(tab);
      if (idx !== -1) currentTabIndex = idx;'''

new_before_switch = '''    var tabSequence = ['home', 'tiktok', 'budget', 'saved'];
    var currentTabIndex = 0;

    function switchTab(tab) {
      if (currentAppMode === 'vendor') {
        toggleAppMode(); // switch back to client when clicking dock tabs
      }
      const idx = tabSequence.indexOf(tab);
      if (idx !== -1) currentTabIndex = idx;'''

if old_before_switch in html:
    html = html.replace(old_before_switch, new_before_switch)
    print("tabSequence declared before switchTab!")

# 2. Ganti renderSavedList dengan versi lengkap yang mendukung filter kategori wishlist, total estimasi, export rekapan, reset, dan chat
old_render_saved = '''    function renderSavedList() {
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
    }'''

new_render_saved_and_helpers = '''    // LOGIC KHUSUS TAB BUDGET (PRESET ANGGARAN CEPAT)
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

    // LOGIC KHUSUS TAB TERSIMPAN (WISHLIST DENGAN FILTER KATEGORI)
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

      // Hitung total estimasi harga mulai
      const totalEst = allSaved.reduce((acc, v) => acc + (v.priceStart || 0), 0);
      if (totalEstEl) totalEstEl.innerText = formatRupiah(totalEst);
      if (countBadge) countBadge.innerText = `${allSaved.length} Vendor`;

      if (filtered.length === 0) {
        container.innerHTML = `
          <div class="text-center py-8 border border-dashed border-neutral-800 rounded-2xl p-5 bg-neutral-950/60">
            <span class="text-2xl block mb-2">🔖</span>
            <p class="text-xs text-neutral-300 font-semibold">${allSaved.length === 0 ? 'Belum ada vendor yang disimpan.' : 'Tidak ada vendor tersimpan di kategori ini.'}</p>
            <p class="text-[10px] text-neutral-500 mt-1">Tekan ikon bookmark pada postingan vendor di menu Eksplor.</p>
            <button onclick="switchTab('home')" class="mt-3 text-xs bg-white text-black px-3.5 py-1.5 rounded-lg font-bold hover:bg-neutral-200 transition">Jelajahi Vendor</button>
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
                <span>${v.igHandle}</span> • <span class="text-emerald-400 font-bold">Mulai ${formatRupiah(v.priceStart)}</span>
              </div>
            </div>
          </div>
          <div class="flex items-center space-x-1.5">
            <button onclick="event.stopPropagation(); openChatWithVendorById('${v.id}')" class="w-8 h-8 rounded-lg bg-neutral-800 hover:bg-neutral-700 text-emerald-400 flex items-center justify-center text-xs transition" title="Chat Vendor">
              💬
            </button>
            <button onclick="event.stopPropagation(); toggleSave('${v.id}')" class="w-8 h-8 rounded-lg bg-neutral-800 hover:bg-red-950/60 text-red-400 flex items-center justify-center text-xs transition" title="Hapus dari Wishlist">
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

    // SWIPE GESTURE DETECTION (USAP KIRI / KANAN UNTUK BERPINDAH TAB)
    let touchStartX = 0;
    let touchStartY = 0;

    function initSwipeGestures() {
      const target = document.getElementById('iphoneDeviceFrame');
      if (!target) return;

      target.addEventListener('touchstart', (e) => {
        touchStartX = e.changedTouches[0].screenX;
        touchStartY = e.changedTouches[0].screenY;
      }, { passive: true });

      target.addEventListener('touchend', (e) => {
        const touchEndX = e.changedTouches[0].screenX;
        const touchEndY = e.changedTouches[0].screenY;
        const diffX = touchEndX - touchStartX;
        const diffY = touchEndY - touchStartY;
        
        // Cek jika usapan horizontal lebih dominan daripada vertikal & minimal 60px
        if (Math.abs(diffX) > Math.abs(diffY) && Math.abs(diffX) > 60) {
          if (diffX < 0) {
            // Swipe ke kiri -> Tab selanjutnya
            currentTabIndex = (currentTabIndex + 1) % tabSequence.length;
            switchTab(tabSequence[currentTabIndex]);
          } else {
            // Swipe ke kanan -> Tab sebelumnya
            currentTabIndex = (currentTabIndex - 1 + tabSequence.length) % tabSequence.length;
            switchTab(tabSequence[currentTabIndex]);
          }
        }
      }, { passive: true });
    }'''

if old_render_saved in html:
    html = html.replace(old_render_saved, new_render_saved_and_helpers)
    print("Replaced renderSavedList with full budget & wishlist logic + swipe gestures!")
else:
    print("Warning: old_render_saved not found directly!")

# 3. Panggil initSwipeGestures() di akhir sebelum filterVendors()
old_init = '// INIT ON LOAD\n    filterVendors();'
new_init = '// INIT ON LOAD\n    initSwipeGestures();\n    filterVendors();'
if old_init in html:
    html = html.replace(old_init, new_init)
    print("initSwipeGestures() added to init block!")

with open(file_path, "w", encoding="utf-8") as f:
    f.write(html)

print("Updated index.html saved! New length:", len(html))
