import requests, sys
url = sys.argv[1] if len(sys.argv) > 1 else "https://example.org"
r = requests.get(url, timeout=10)
print(f"[SCRAPER] Fetched {url} -> {len(r.text)} bytes")
