with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

assert 'id="btnAppKitaMenikah"' in text, "btnAppKitaMenikah missing"
assert 'onclick="launchKitaMenikahApp()"' in text, "onclick missing"
assert 'function launchKitaMenikahApp()' in text, "function missing"
assert 'function returnToHomeScreen()' in text, "returnToHomeScreen missing"
print("HTML verification passed!")
