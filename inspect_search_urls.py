from fetch_all_real_slides import find_lookaside_and_images

res = find_lookaside_and_images("sandi.liem instagram wedding yogyakarta")
print("Sandi Liem results:", len(res))
for u in res[:10]:
    print("  ", u)

res2 = find_lookaside_and_images("thenijophotograph instagram wedding")
print("Nijo results:", len(res2))
for u in res2[:10]:
    print("  ", u)
