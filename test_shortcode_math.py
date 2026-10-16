def shortcode_to_media_id(shortcode):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_'
    media_id = 0
    for char in shortcode:
        media_id = media_id * 64 + alphabet.index(char)
    return str(media_id)

shortcodes = {
    "jawara_1": "DZfMeWEGdnY",
    "jawara_2": "DTILEXJkeLK",
    "jawara_3": "DMskguExr-y",
    "lux_1": "DZm2Kbgj4ZZ",
    "kitakancerita_1": "DV2iXGGCSz6",
    "nijo_1": "DaQBRhFGCvF",
    "neiscala_1": "DeB1C4kH5vS",
    "lunanouva_1": "DdRiiJqj3xs"
}

for k, sc in shortcodes.items():
    mid = shortcode_to_media_id(sc)
    print(f"{k} ({sc}) -> media_id: {mid}")
