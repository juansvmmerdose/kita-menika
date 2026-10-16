import re

file_path = r"C:\Users\VANDI\.gemini\antigravity\scratch\kita-menikah\index.html"
with open(file_path, "r", encoding="utf-8") as f:
    html = f.read()

# 1. Update iPhone 16 Pro Max dimensions and bezel styling
old_promax_frame = '''<div id="iphoneDeviceFrame" class="relative bg-black rounded-[44px] md:rounded-[50px] border-[8px] md:border-[10px] border-[#252528] shadow-[0_25px_60px_-15px_rgba(0,0,0,0.95),0_0_0_1px_rgba(255,255,255,0.08),0_0_35px_rgba(255,255,255,0.03)] overflow-hidden flex flex-col transition-all"
       style="height: min(92vh, 760px); width: min(calc(min(92vh, 760px) * 0.465), 365px); max-height: calc(100vh - 20px); max-width: calc((100vh - 20px) * 0.465);">'''

new_promax_frame = '''<div id="iphoneDeviceFrame" class="relative bg-black rounded-[48px] md:rounded-[54px] border-[6px] md:border-[7px] border-[#1e1e22] shadow-[0_25px_70px_-15px_rgba(0,0,0,0.98),0_0_0_1px_rgba(255,255,255,0.1),0_0_40px_rgba(255,255,255,0.03)] overflow-hidden flex flex-col transition-all"
       style="height: min(94vh, 860px); width: min(calc(min(94vh, 860px) * 0.495), 425px); max-height: calc(100vh - 16px); max-width: calc((100vh - 16px) * 0.495);">'''

if old_promax_frame in html:
    html = html.replace(old_promax_frame, new_promax_frame)
    print("Replaced with iPhone 16 Pro Max expansive dimensions!")
else:
    # Use regex
    html = re.sub(
        r'<div id="iphoneDeviceFrame"[^>]*style="[^"]*"',
        '''<div id="iphoneDeviceFrame" class="relative bg-black rounded-[48px] md:rounded-[54px] border-[6px] md:border-[7px] border-[#1e1e22] shadow-[0_25px_70px_-15px_rgba(0,0,0,0.98),0_0_0_1px_rgba(255,255,255,0.1),0_0_40px_rgba(255,255,255,0.03)] overflow-hidden flex flex-col transition-all"
       style="height: min(94vh, 860px); width: min(calc(min(94vh, 860px) * 0.495), 425px); max-height: calc(100vh - 16px); max-width: calc((100vh - 16px) * 0.495);"''',
        html,
        count=1
    )
    print("Regex replacement of iPhone frame done!")

# 2. Update vendorListSection to edge-to-edge Instagram style
old_vendor_section = '''        <!-- VENDORS LIST -->
        <div id="vendorListSection" class="px-5 pt-2">
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
        </div>'''

new_vendor_section = '''        <!-- VENDORS LIST (INSTAGRAM FEED STYLE) -->
        <div id="vendorListSection" class="pt-2">
          <div class="flex justify-between items-center mb-2 px-3.5">
            <div>
              <div class="flex items-center space-x-1.5">
                <span class="w-2 h-2 rounded-full bg-pink-500 animate-pulse"></span>
                <h2 class="text-xs tracking-[0.15em] uppercase font-bold text-neutral-200">Feed Vendor Terkurasi</h2>
              </div>
              <p class="text-[10px] text-neutral-500 font-sans">Eksplorasi portofolio asli vendor dengan harga resmi & escrow</p>
            </div>
            <span id="vendorCount" class="text-[11px] text-neutral-400 font-mono">Memuat...</span>
          </div>

          <div id="vendorList" class="divide-y divide-neutral-900 border-t border-neutral-900">
            <!-- Dynamic Vendor Cards with Slides injected by JS -->
          </div>
        </div>'''

if old_vendor_section in html:
    html = html.replace(old_vendor_section, new_vendor_section)
    print("Replaced vendorListSection markup!")
else:
    print("Note: old_vendor_section not exact match, checking manually...")

# 3. Update updateCardSlide function to support carousel number badge
old_update_slide = '''    function updateCardSlide(v) {
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
    }'''

new_update_slide = '''    function updateCardSlide(v) {
      const currentSlide = v.slides[v.slideIndex];
      const imgEl = document.getElementById(`slide-img-${v.id}`);
      const tagEl = document.getElementById(`slide-tag-${v.id}`);
      const likesEl = document.getElementById(`slide-likes-${v.id}`);
      const captionEl = document.getElementById(`slide-caption-${v.id}`);
      const dotsEl = document.getElementById(`dots-${v.id}`);
      const numEl = document.getElementById(`slide-num-${v.id}`);

      if (imgEl && currentSlide.image) imgEl.src = currentSlide.image;
      if (tagEl) tagEl.innerText = currentSlide.tag;
      if (likesEl) likesEl.innerText = `❤️ ${currentSlide.likes}`;
      if (captionEl) captionEl.innerText = currentSlide.caption;
      if (numEl) numEl.innerText = `${v.slideIndex + 1}/${v.slides.length}`;

      if (dotsEl && v.slides.length > 1) {
        dotsEl.innerHTML = v.slides.map((_, idx) => `
          <span class="w-1.5 h-1.5 rounded-full transition ${idx === v.slideIndex ? 'bg-sky-400 scale-125' : 'bg-white/50'}"></span>
        `).join('');
      }
    }

    function toggleCardLike(vendorId, btn) {
      const icon = btn.querySelector('.heart-icon');
      if (!icon) return;
      const isLiked = icon.classList.contains('fill-red-500');
      if (isLiked) {
        icon.classList.remove('fill-red-500', 'text-red-500');
        icon.classList.add('text-white');
      } else {
        icon.classList.add('fill-red-500', 'text-red-500', 'scale-125');
        setTimeout(() => icon.classList.remove('scale-125'), 200);
      }
    }'''

if old_update_slide in html:
    html = html.replace(old_update_slide, new_update_slide)
    print("Replaced updateCardSlide & added toggleCardLike!")
else:
    print("Note: old_update_slide not matched exactly!")

# 4. Replace filterVendors card template with authentic Instagram post layout + wedding price card
# Find listContainer.innerHTML = filtered.map(v => { ... }).join('');
pattern_cards = r'listContainer\.innerHTML\s*=\s*filtered\.map\(v\s*=>\s*\{[\s\S]*?\}\)\.join\(\'\'\);'

new_cards_code = '''listContainer.innerHTML = filtered.map(v => {
        const isSaved = savedVendorIds.has(v.id);
        const priceLabel = v.category === 'catering' ? `${formatRupiah(v.priceStart)} / pax` : formatRupiah(v.priceStart);
        const currentSlide = v.slides[v.slideIndex || 0];
        const hasMultipleSlides = v.slides && v.slides.length > 1;

        return `
          <!-- INSTAGRAM POST REPLICA WITH WEDDING MARKETPLACE PRICING & ESCROW -->
          <article class="bg-black pb-4 pt-1">
            
            <!-- 1. INSTAGRAM POST HEADER (AVATAR, USERNAME, LOCATION, TRIPLE DOTS) -->
            <div class="px-3.5 py-2 flex items-center justify-between">
              <div class="flex items-center space-x-2.5 cursor-pointer" onclick="openVendorModal('${v.id}')">
                <!-- IG Story Ring Gradient on Avatar -->
                <div class="w-8 h-8 rounded-full p-[1.5px] bg-gradient-to-tr from-amber-400 via-rose-500 to-purple-600 shrink-0 shadow-sm">
                  <div class="w-full h-full rounded-full overflow-hidden bg-black border border-black">
                    <img src="${v.avatar}" alt="${v.name}" class="w-full h-full object-cover">
                  </div>
                </div>
                <div>
                  <div class="flex items-center space-x-1 leading-tight">
                    <span class="text-xs font-bold text-white tracking-tight hover:underline font-mono">${v.igHandle}</span>
                    <span class="text-sky-400 text-[11px]" title="Vendor Terverifikasi KITA MENIKAH">✓</span>
                    ${v.isPromoted ? `<span class="bg-amber-400/20 text-amber-300 border border-amber-400/40 text-[8px] font-bold px-1.5 py-0.2 rounded uppercase">${v.promoTier}</span>` : ''}
                  </div>
                  <div class="flex items-center space-x-1 text-[10px] text-neutral-400 font-sans mt-0.5">
                    <span class="truncate max-w-[140px] text-neutral-300 font-medium">${v.name}</span>
                    <span>•</span>
                    <span class="truncate max-w-[100px]">📍 ${v.locationText.split(',')[0]}</span>
                  </div>
                </div>
              </div>

              <!-- Right Header Actions (Direct IG link & Details) -->
              <div class="flex items-center space-x-1.5">
                <a href="${v.igUrl}" target="_blank" rel="noopener noreferrer" onclick="event.stopPropagation()" class="px-2 py-0.5 rounded-full bg-gradient-to-r from-purple-500/15 via-pink-500/15 to-orange-500/15 border border-pink-500/40 hover:border-pink-300 text-pink-300 text-[9px] font-bold flex items-center space-x-1 transition active:scale-95 shadow-sm" title="Buka Profil IG Asli">
                  <svg class="w-2.5 h-2.5 text-pink-400" fill="currentColor" viewBox="0 0 24 24"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z"/></svg>
                  <span>IG</span>
                </a>
                <button onclick="openVendorModal('${v.id}')" class="text-neutral-400 hover:text-white px-1 text-sm font-bold">•••</button>
              </div>
            </div>

            <!-- 2. INSTAGRAM SQUARE PHOTO CONTAINER (1:1 BERSIH & FOKUS) -->
            <div class="relative w-full aspect-square bg-neutral-950 overflow-hidden cursor-pointer select-none" onclick="openVendorModal('${v.id}')">
              <img id="slide-img-${v.id}" src="${currentSlide.image}" alt="${v.name}" class="w-full h-full object-cover transition duration-300">

              <!-- Carousel Indicator (Top Right: 1/3) -->
              ${hasMultipleSlides ? `
                <div class="absolute top-2.5 right-2.5 bg-black/75 backdrop-blur text-white text-[10px] font-mono font-bold px-2 py-0.5 rounded-full border border-white/20 shadow">
                  <span id="slide-num-${v.id}">${(v.slideIndex || 0) + 1}/${v.slides.length}</span>
                </div>
              ` : ''}

              <!-- Subtle Category/Style Badge (Top Left) -->
              <div class="absolute top-2.5 left-2.5 bg-black/70 backdrop-blur text-neutral-200 border border-white/20 text-[9px] font-semibold px-2 py-0.5 rounded-full shadow">
                <span id="slide-tag-${v.id}">${currentSlide.tag || v.styleTag}</span>
              </div>

              <!-- Slide Navigation Buttons (Minimalist ‹ ›) -->
              ${hasMultipleSlides ? `
                <button onclick="prevSlide('${v.id}', event)" class="absolute left-2 top-1/2 -translate-y-1/2 w-7 h-7 rounded-full bg-black/60 hover:bg-black/90 text-white flex items-center justify-center text-xs border border-white/20 transition active:scale-90 shadow-md">
                  ‹
                </button>
                <button onclick="nextSlide('${v.id}', event)" class="absolute right-2 top-1/2 -translate-y-1/2 w-7 h-7 rounded-full bg-black/60 hover:bg-black/90 text-white flex items-center justify-center text-xs border border-white/20 transition active:scale-90 shadow-md">
                  ›
                </button>
                <!-- Carousel Dots Indicator -->
                <div id="dots-${v.id}" class="absolute bottom-2 left-0 right-0 flex justify-center space-x-1 pointer-events-none">
                  ${v.slides.map((_, idx) => `
                    <span class="w-1.5 h-1.5 rounded-full transition ${idx === (v.slideIndex || 0) ? 'bg-sky-400 scale-125' : 'bg-white/50'}"></span>
                  `).join('')}
                </div>
              ` : ''}
            </div>

            <!-- 3. INSTAGRAM ACTION BUTTONS (LIKE, CHAT, SHARE, BOOKMARK) -->
            <div class="px-3.5 pt-2.5 pb-1 flex justify-between items-center">
              <div class="flex items-center space-x-3.5">
                <!-- Like Heart Button -->
                <button onclick="toggleCardLike('${v.id}', this)" class="text-white hover:text-red-500 transition active:scale-125 focus:outline-none" title="Suka Postingan">
                  <svg class="w-5 h-5 heart-icon transition" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z"/></svg>
                </button>

                <!-- Chat with Vendor Button -->
                <button onclick="event.stopPropagation(); openChatWithVendorById('${v.id}')" class="text-white hover:text-emerald-400 transition active:scale-110 focus:outline-none" title="Chat Vendor">
                  <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 12h.01M12 12h.01M16 12h.01M21 12c0 4.418-4.03 8-9 8a9.863 9.863 0 01-4.255-.949L3 20l1.395-3.72C3.512 15.042 3 13.574 3 12c0-4.418 4.03-8 9-8s9 3.582 9 8z"/></svg>
                </button>

                <!-- Share / Profile Link -->
                <a href="${v.igUrl}" target="_blank" rel="noopener noreferrer" onclick="event.stopPropagation()" class="text-white hover:text-pink-400 transition active:scale-110" title="Buka di Instagram">
                  <svg class="w-5 h-5 -rotate-12" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 19l9 2-9-18-9 18 9-2zm0 0v-8"/></svg>
                </a>
              </div>

              <!-- Wishlist Bookmark Button -->
              <button onclick="event.stopPropagation(); toggleSave('${v.id}')" class="text-white hover:text-amber-400 transition active:scale-125 focus:outline-none" title="Simpan ke Wishlist">
                <svg class="w-5 h-5 ${isSaved ? 'text-amber-400 fill-amber-400' : ''}" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 5a2 2 0 012-2h10a2 2 0 012 2v16l-7-3.5L5 21V5z"/></svg>
              </button>
            </div>

            <!-- 4. LIKES & CAPTION DESCRIPTION (AUTHENTIC IG TEXT) -->
            <div class="px-3.5 text-xs space-y-1">
              <div class="flex items-center space-x-2 font-bold text-white text-[11px] font-mono">
                <span id="slide-likes-${v.id}">❤️ ${currentSlide.likes || '2.450 suka'}</span>
                <span class="text-neutral-500 font-sans font-normal">•</span>
                <span class="text-neutral-400 font-sans font-normal">★ ${v.rating} (${v.reviewCount} ulasan)</span>
              </div>

              <div class="text-neutral-200 text-xs leading-snug">
                <span class="font-bold text-white mr-1.5 cursor-pointer font-mono" onclick="openVendorModal('${v.id}')">${v.igHandle}</span>
                <span id="slide-caption-${v.id}" class="text-neutral-300 font-sans">${currentSlide.caption || v.description}</span>
              </div>
            </div>

            <!-- 5. KITA MENIKAH SPECIAL WEDDING PRICING & ESCROW STRIP ("bukan IG karena ada harganya dll") -->
            <div class="mx-3.5 mt-2.5 p-2.5 rounded-xl bg-neutral-900/90 border border-neutral-800 flex items-center justify-between shadow-sm">
              <div class="space-y-0.5">
                <span class="text-[9px] uppercase tracking-wider text-neutral-400 font-semibold block">Paket Mulai</span>
                <div class="text-sm font-bold text-emerald-400 font-mono tracking-tight">${priceLabel}</div>
              </div>

              <div class="flex items-center space-x-1.5">
                <button onclick="event.stopPropagation(); openChatWithVendorById('${v.id}')" class="px-2.5 py-1.5 rounded-lg bg-neutral-800 border border-neutral-700 hover:border-emerald-500 text-emerald-400 hover:text-white text-[11px] font-bold transition active:scale-95 flex items-center space-x-1">
                  <span>💬</span>
                  <span>Chat</span>
                </button>
                <button onclick="openVendorModal('${v.id}')" class="px-3 py-1.5 rounded-lg bg-white hover:bg-neutral-200 text-black text-[11px] font-bold transition active:scale-95 shadow">
                  Lihat Paket
                </button>
              </div>
            </div>

            <!-- Escrow Guarantee Badge & Available Packages Link -->
            <div class="px-3.5 pt-1.5 flex items-center justify-between text-[10px] text-neutral-500 font-mono">
              <span class="flex items-center space-x-1">
                <span class="text-emerald-500">🛡️</span>
                <span>Rekber Resmi KITA MENIKAH</span>
              </span>
              <button onclick="openVendorModal('${v.id}')" class="text-neutral-400 hover:text-white underline">
                ${v.packages.length} paket siap →
              </button>
            </div>

          </article>
        `;
      }).join('');'''

if re.search(pattern_cards, html):
    html = re.sub(pattern_cards, new_cards_code, html, count=1)
    print("Replaced cards with Instagram post + wedding price replica!")
else:
    print("Warning: pattern_cards not matched!")

with open(file_path, "w", encoding="utf-8") as f:
    f.write(html)

print("Updated index.html successfully saved! Length:", len(html))
