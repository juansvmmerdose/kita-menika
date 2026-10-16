from test_lookaside_nijo import download_from_lookaside
import shutil

shutil.copy("real_wedding_sample.jpg", "assets/vendors/slides/sandiliem_slide_1.jpg")
print("Copied sandiliem_slide_1.jpg")

download_from_lookaside("3710291904749004283", "assets/vendors/slides/sandiliem_slide_2.jpg")
