import json
import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Update Logo & Sticky Search Bar structure
old_header_pattern = r'<!-- TOP STICKY HEADER -->\s*<header class="px-5 pt-3 pb-3 border-b border-neutral-900 bg-black/95 backdrop-blur sticky top-0 z-40 space-y-2.5">.*?</header>'

new_header_replacement = """<!-- TOP NON-STICKY LOGO HEADER (IKUT HILANG / SCROLL KE ATAS SAAT DIGULIRKAN) -->
      <div id="topBrandHeader" class="px-5 pt-3.5 pb-2.5 bg-black flex justify-between items-center border-b border-neutral-900/60">
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

      <!-- STICKY SEARCH & CITY FILTER (HANYA INI YANG MENEMPEL DI ATAS SAAT DIGULIRKAN) -->
      <header id="stickySearchHeader" class="px-5 py-2.5 border-b border-neutral-900 bg-black/95 backdrop-blur sticky top-0 z-40 space-y-2">
        <!-- SEARCH BAR (HANYA MUNCUL DI MODE KLIEN) -->
        <div id="clientSearchBar" class="relative">
          <svg class="w-4 h-4 text-neutral-500 absolute left-3 top-2.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"/></svg>
          <input type="text" id="searchInput" oninput="filterVendors()" placeholder="Cari Jawara, Sandi Liems, Lux Visual, Nijo, Neiscala, Ilona, Mamuk..." class="w-full bg-neutral-900 border border-neutral-800 rounded-xl pl-9 pr-4 py-2 text-xs text-white placeholder-neutral-500 focus:outline-none focus:border-white transition">
        </div>

        <!-- LOKASI & PILIHAN KOTA -->
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
      </header>"""

html = re.sub(old_header_pattern, new_header_replacement, html, flags=re.DOTALL)
print("Updated header to non-sticky logo + sticky search bar!")

# 2. Make clientQuickMenu non-sticky (remove sticky top-[108px] z-30 backdrop-blur)
html = html.replace(
    'id="clientQuickMenu" class="px-4 py-3 bg-neutral-950/90 border-b border-neutral-900 sticky top-[108px] z-30 backdrop-blur"',
    'id="clientQuickMenu" class="px-4 py-3 bg-neutral-950/90 border-b border-neutral-900"'
)
print("Removed sticky from clientQuickMenu so it scrolls with the page content!")

# 3. Update toggleAppMode JS to target stickySearchHeader
html = html.replace("document.getElementById('clientSearchBar').classList.add('hidden');", "document.getElementById('stickySearchHeader').classList.add('hidden');")
html = html.replace("document.getElementById('clientSearchBar').classList.remove('hidden');", "document.getElementById('stickySearchHeader').classList.remove('hidden');")

# 4. Update vendor card template with prominent official Instagram badge and direct IG buttons
old_ig_link_in_card = """                  <a href="${v.igUrl}" target="_blank" onclick="event.stopPropagation()" class="text-[10px] text-neutral-400 hover:text-white font-mono flex items-center space-x-1">
                    <span>${v.igHandle}</span>
                    <span class="text-[9px]">↗</span>
                  </a>"""

new_ig_badge_in_card = """                  <a href="${v.igUrl}" target="_blank" rel="noopener noreferrer" onclick="event.stopPropagation()" class="inline-flex items-center space-x-1.5 px-2.5 py-0.5 rounded-full bg-gradient-to-r from-purple-500/20 via-pink-500/20 to-orange-500/20 border border-pink-500/40 hover:border-pink-300 text-pink-300 hover:text-white transition group shadow-sm" title="Buka profil resmi ${v.igHandle} di Instagram">
                    <svg class="w-3 h-3 text-pink-400 group-hover:scale-110 transition" fill="currentColor" viewBox="0 0 24 24">
                      <path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z"/>
                    </svg>
                    <span class="text-[10px] font-bold">${v.igHandle}</span>
                    <svg class="w-2.5 h-2.5 text-pink-400 opacity-80" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14"/></svg>
                  </a>"""

if old_ig_link_in_card in html:
    html = html.replace(old_ig_link_in_card, new_ig_badge_in_card)
    print("Updated vendor card header with official Instagram pill badge!")

# 5. Add direct Instagram button in card footer
old_card_footer_buttons = """              <div class="flex items-center space-x-2">
                <button onclick="event.stopPropagation(); openChatWithVendorById('${v.id}')" class="w-8 h-8 rounded-xl bg-neutral-800 border border-neutral-700 flex items-center justify-center text-emerald-400 hover:text-white hover:border-neutral-500 transition" title="Chat Vendor">
                  <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 12h.01M12 12h.01M16 12h.01M21 12c0 4.418-4.03 8-9 8a9.863 9.863 0 01-4.255-.949L3 20l1.395-3.72C3.512 15.042 3 13.574 3 12c0-4.418 4.03-8 9-8s9 3.582 9 8z"/></svg>
                </button>
                <button onclick="openVendorModal('${v.id}')" class="bg-white text-black text-xs font-bold px-3 py-1.5 rounded-xl hover:bg-neutral-200 transition">
                  Lihat Paket
                </button>
              </div>"""

new_card_footer_buttons = """              <div class="flex items-center space-x-1.5">
                <a href="${v.igUrl}" target="_blank" rel="noopener noreferrer" onclick="event.stopPropagation()" class="px-2.5 py-1.5 rounded-xl bg-gradient-to-tr from-purple-900/40 via-pink-900/40 to-orange-900/40 border border-pink-500/35 hover:border-pink-300 text-pink-300 hover:text-white flex items-center space-x-1 text-xs transition active:scale-95 shadow-sm" title="Buka Instagram Resmi ${v.name}">
                  <svg class="w-3.5 h-3.5 text-pink-400" fill="currentColor" viewBox="0 0 24 24"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z"/></svg>
                  <span class="text-[10px] font-bold">IG</span>
                </a>
                <button onclick="event.stopPropagation(); openChatWithVendorById('${v.id}')" class="w-8 h-8 rounded-xl bg-neutral-800 border border-neutral-700 flex items-center justify-center text-emerald-400 hover:text-white hover:border-neutral-500 transition active:scale-95" title="Chat Vendor">
                  <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 12h.01M12 12h.01M16 12h.01M21 12c0 4.418-4.03 8-9 8a9.863 9.863 0 01-4.255-.949L3 20l1.395-3.72C3.512 15.042 3 13.574 3 12c0-4.418 4.03-8 9-8s9 3.582 9 8z"/></svg>
                </button>
                <button onclick="openVendorModal('${v.id}')" class="bg-white text-black text-xs font-bold px-3 py-1.5 rounded-xl hover:bg-neutral-200 transition active:scale-95 shadow">
                  Lihat Paket
                </button>
              </div>"""

if old_card_footer_buttons in html:
    html = html.replace(old_card_footer_buttons, new_card_footer_buttons)
    print("Updated vendor card footer with direct IG button!")

# 6. Update openVendorModal with big prominent Instagram button
old_modal_header = """            <div>
              <h2 class="text-base font-bold text-white tracking-wide">${v.name}</h2>
              <div class="flex items-center space-x-2 mt-0.5">
                <span class="text-xs text-neutral-400 font-mono">${v.igHandle}</span>
                <span class="text-[10px] text-neutral-500">•</span>
                <span class="text-xs text-neutral-400">${v.igFollowers}</span>
              </div>
              <span class="text-[11px] text-neutral-400 block mt-1">📍 ${v.locationText}</span>
            </div>
          </div>"""

new_modal_header = """            <div>
              <h2 class="text-base font-bold text-white tracking-wide">${v.name}</h2>
              <div class="flex items-center space-x-2 mt-0.5">
                <span class="text-xs text-pink-400 font-mono font-bold">${v.igHandle}</span>
                <span class="text-[10px] text-neutral-500">•</span>
                <span class="text-xs text-neutral-400">${v.igFollowers}</span>
              </div>
              <span class="text-[11px] text-neutral-400 block mt-0.5">📍 ${v.locationText}</span>
            </div>
          </div>

          <!-- TOMBOL DIRECT LINK BUKA PROFIL INSTAGRAM RESMI -->
          <a href="${v.igUrl}" target="_blank" rel="noopener noreferrer" class="w-full py-2.5 px-4 rounded-xl bg-gradient-to-r from-purple-900/50 via-pink-900/40 to-orange-900/40 border border-pink-500/40 hover:border-pink-300 flex items-center justify-between text-xs font-bold text-white transition active:scale-98 shadow">
            <div class="flex items-center space-x-2">
              <svg class="w-4 h-4 text-pink-400 shrink-0" fill="currentColor" viewBox="0 0 24 24"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z"/></svg>
              <span>Kunjungi Profil Resmi ${v.igHandle} di Instagram</span>
            </div>
            <span class="text-pink-300 font-mono text-xs">Buka IG ↗</span>
          </a>"""

if old_modal_header in html:
    html = html.replace(old_modal_header, new_modal_header)
    print("Updated openVendorModal with direct Instagram profile button!")

# 7. Update vendors array captions & tags to match real authentic images
m_vendors = re.search(r'const\s+vendors\s*=\s*(\[\s*\{.*?\}\s*\]);', html, re.DOTALL)
if m_vendors:
    vendors = json.loads(m_vendors.group(1))
    
    for v in vendors:
        # Update Mamuk
        if v["id"] == "mua-mamuk":
            v["slides"][0]["tag"] = "👑 MAESTRO PAES AGENG JOGJA"
            v["slides"][0]["likes"] = "15.820 likes"
            v["slides"][0]["caption"] = "Mahakarya Paes Ageng Kraton Ngayogyakarta Hadiningrat prada emas keraton. Keagungan tradisi adiluhung manten putri @mamuktukangmakeupjogja 🤍👑"
        # Update Arnie Suryo
        elif v["id"] == "mua-arnie":
            v["slides"][0]["tag"] = "✨ PAES AGENG JANGAN MENIR"
            v["slides"][0]["likes"] = "12.400 likes"
            v["slides"][0]["caption"] = "Tata rias Paes Ageng Jangan Menir beludru hijau lumut prada emas keraton. Anggun, ningrat, dan sakral @arniesuryo 🌿✨"
        # Update Vidi Catering
        elif v["id"] == "cat-vidi":
            v["slides"][0]["tag"] = "🍽️ PRASMANAN MEWAH & LIVE STALL"
            v["slides"][0]["likes"] = "5.640 likes"
            v["slides"][0]["caption"] = "Penyajian catering prasmanan istimewa pernikahan Jogja. Sate panggang live cooking, ragam gubukan tradisional, rasa otentik bintang 5 @vidicatering ✨"
        # Update Ilona
        elif v["id"] == "wo-ilona":
            v["slides"][0]["tag"] = "🤝 CREW WO ATTENTIVE & SEAMLESS"
            v["slides"][0]["likes"] = "4.310 likes"
            v["slides"][0]["caption"] = "Pendampingan penuh kehangatan dan eksekusi hari-H tanpa celah oleh tim Ilona Organizer bersama kedua mempelai tercinta @ilonaorganizer 🤍"
        # Update Albertus MC
        elif v["id"] == "mc-albertus":
            v["slides"][0]["tag"] = "🎤 MC BILINGUAL & MODERN"
            v["slides"][0]["likes"] = "3.890 likes"
            v["slides"][0]["caption"] = "Memandu jalannya resepsi ageng dengan hangat, elegan, dan penuh sukacita bersama kedua mempelai @albertus_mcjogja 🎤✨"
        # Update Pro Sound
        elif v["id"] == "sound-pro":
            v["slides"][0]["tag"] = "🔊 DIGITAL MIXING & LINE ARRAY"
            v["slides"][0]["likes"] = "2.980 likes"
            v["slides"][0]["caption"] = "Audio fidelity tinggi crystal clear untuk resepsi ballroom. Tata suara akustik dan tata lampu megah @prosound.jogja 🔊💡"

    new_vendors_json = "const vendors = " + json.dumps(vendors, indent=4, ensure_ascii=False) + ";"
    html = html[:m_vendors.start()] + new_vendors_json + html[m_vendors.end():]
    print("Updated vendor descriptions, tags, and likes in const vendors!")

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Saved updated index.html successfully!")
