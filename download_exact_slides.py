from test_lookaside_nijo import download_from_lookaside

tasks = [
    ("3803338563560530634", "assets/vendors/slides/jawara_slide_2.jpg"),
    ("3687482773079506866", "assets/vendors/slides/jawara_slide_3.jpg"),
    ("3920058736916268633", "assets/vendors/slides/luxvisual_slide_1.jpg"),
    ("3852417651935096058", "assets/vendors/slides/kitakancerita_slide_1.jpg"),
    ("3999711238721346514", "assets/vendors/slides/neiscala_slide_1.jpg"),
    ("3986119025620909164", "assets/vendors/slides/lunanouva_slide_1.jpg"),
    ("3931648076491008965", "assets/vendors/slides/nijo_slide_3.jpg")
]

for mid, path in tasks:
    print(f"Downloading {path} from media_id {mid}...")
    download_from_lookaside(mid, path)
