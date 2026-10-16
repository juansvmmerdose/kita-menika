from test_tailored_search import search_bing_murls

queries = [
    ("jawara_logo", 'jawara photo jogja logo'),
    ("sandi_logo", 'sandi liem wedding logo'),
    ("lux_logo", 'lux visual jogja logo'),
    ("kitakancerita_logo", 'kitakancerita jogja logo'),
    ("nijo_logo", 'thenijophotograph logo'),
    ("neiscala_logo", 'neiscala wedding logo'),
    ("lunanouva_logo", 'lunanouva studio logo')
]

for label, q in queries:
    res = search_bing_murls(q)
    print(f"\n[{label}] {q}: found {len(res)}")
    for u in res[:3]:
        print("  ", u)
