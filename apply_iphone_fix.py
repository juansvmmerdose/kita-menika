import re

file_path = r"C:\Users\VANDI\.gemini\antigravity\scratch\kita-menikah\index.html"
with open(file_path, "r", encoding="utf-8") as f:
    html = f.read()

# 1. Update body and iPhone container
old_frame_pattern = r'''<body class="bg-\[#050507\] text-neutral-100 font-sans-clean h-screen w-screen overflow-hidden flex items-center justify-center p-2 sm:p-4 select-none antialiased">\s*<!-- OUTER IPHONE 16 PRO CONTAINER \(FIXED FIT, ZERO OUTER PAGE SCROLLBAR\) -->\s*<div id="iphoneDeviceFrame"[^>]*>\s*<!-- HARDWARE BUTTONS:[^>]*-->\s*<div class="hidden md:block absolute -left-\[13px\][^>]*></div>\s*<div class="hidden md:block absolute -left-\[13px\][^>]*></div>\s*<div class="hidden md:block absolute -left-\[13px\][^>]*></div>\s*<div class="hidden md:block absolute -right-\[13px\][^>]*></div>'''

new_frame_html = '''<body class="bg-[#07070a] text-neutral-100 font-sans-clean h-screen w-screen overflow-hidden flex items-center justify-center p-2 sm:p-3 select-none antialiased">

  <!-- OUTER IPHONE 16 PRO CONTAINER (100% UTUH, BEBAS SCROLL LUAR, PROPORSIONAL REALISTIS) -->
  <div id="iphoneDeviceFrame" class="relative bg-black rounded-[44px] md:rounded-[50px] border-[8px] md:border-[10px] border-[#252528] shadow-[0_25px_60px_-15px_rgba(0,0,0,0.95),0_0_0_1px_rgba(255,255,255,0.08),0_0_35px_rgba(255,255,255,0.03)] overflow-hidden flex flex-col transition-all"
       style="height: min(92vh, 760px); width: min(calc(min(92vh, 760px) * 0.465), 365px); max-height: calc(100vh - 20px); max-width: calc((100vh - 20px) * 0.465);">'''

if re.search(old_frame_pattern, html):
    html = re.sub(old_frame_pattern, new_frame_html, html, count=1)
    print("Successfully replaced iPhone outer frame and removed external hardware buttons!")
else:
    print("Regex for old frame didn't match directly, trying manual string replace...")
    # Manual target
    target_start = '<body class="bg-[#050507]'
    target_end = '<div id="iphoneStatusBar"'
    pos1 = html.find(target_start)
    pos2 = html.find(target_end)
    if pos1 != -1 and pos2 != -1:
        html = html[:pos1] + new_frame_html + "\n\n    <!-- IPHONE STATUS BAR & INTERACTIVE DYNAMIC ISLAND -->\n    " + html[pos2:]
        print("Manual replacement of outer frame successful!")

# 2. Adjust viewTikTok positioning so it sits cleanly between status bar and bottom dock
# Change: <div id="viewTikTok" class="hidden absolute inset-0 z-30 bg-black flex flex-col overflow-hidden">
# To: <div id="viewTikTok" class="hidden absolute inset-x-0 top-0 bottom-16 z-30 bg-black flex flex-col overflow-hidden">
html = html.replace(
    '<div id="viewTikTok" class="hidden absolute inset-0 z-30 bg-black flex flex-col overflow-hidden">',
    '<div id="viewTikTok" class="hidden absolute inset-x-0 top-0 bottom-16 z-30 bg-black flex flex-col overflow-hidden">'
)

# Fix bottom-18 to bottom-4 inside viewTikTok
html = html.replace('absolute bottom-18 left-3 right-16 space-y-1.5 z-20 pointer-events-auto', 'absolute bottom-3 left-3 right-16 space-y-1.5 z-20 pointer-events-auto')
html = html.replace('absolute right-2.5 bottom-20 flex flex-col items-center space-y-3 z-30', 'absolute right-2.5 bottom-6 flex flex-col items-center space-y-2.5 z-30')
html = html.replace('absolute bottom-16 left-0 right-0 h-0.5 bg-white/20 z-30', 'absolute bottom-0 left-0 right-0 h-0.5 bg-white/20 z-30')

# 3. Remove leftover static reels between line ~573 and ~813
# Specifically from <!-- REEL 2: SUNGKEMAN & AKAD HARU JAWARA PHOTO --> to right before </div> <!-- appContainer close -->
reel2_marker = "<!-- REEL 2: SUNGKEMAN & AKAD HARU JAWARA PHOTO -->"
bottom_dock_marker = "<!-- BOTTOM APP NAVIGATION DOCK (4 TABS) + IPHONE HOME INDICATOR -->"

pos_reel2 = html.find(reel2_marker)
pos_dock = html.find(bottom_dock_marker)

if pos_reel2 != -1 and pos_dock != -1:
    # Find the closing </div> of appContainer before bottom_dock_marker
    sub = html[pos_reel2:pos_dock]
    # We want to replace everything from pos_reel2 up to the </div> right before pos_dock
    last_div_idx = html.rfind("</div>", pos_reel2, pos_dock)
    if last_div_idx != -1:
        html = html[:pos_reel2] + "\n" + html[last_div_idx:]
        print("Successfully removed leftover static reels divs!")

# 4. Polish bottomDockWrapper
html = html.replace(
    '<!-- BOTTOM APP NAVIGATION DOCK (4 TABS) + IPHONE HOME INDICATOR -->',
    '<!-- BOTTOM APP NAVIGATION DOCK (TOMBOL TETAP BERADA DALAM IPHONE) -->'
)

# Save updated index.html
with open(file_path, "w", encoding="utf-8") as f:
    f.write(html)

print("Updated index.html saved! New length:", len(html))
