import os, time, json
import requests
from bs4 import BeautifulSoup
from urllib.parse import quote

query = input("[?] Bing Search Images : ")
limit = int(input("[?] How many Images ? "))
query_encoded = quote(query)

headers = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 10; Mobile)"
}

def extract_image_urls(html):
    soup = BeautifulSoup(html, "html.parser")
    urls = []
    for img_tag in soup.find_all("a", {"class": "iusc"}):
        m = img_tag.get("m")
        if m:
            try:
                data = json.loads(m)
                url = data["murl"]
                urls.append(url)
            except:
                pass
    return urls

print("[*] Starting simulated scroll on Bing...")

images = []
count = 0
step = 30
max_first = 2000  # sécurité

while len(images) < limit and count <= max_first:
    print(f"  - Requête Bing async: first={count}")
    url = f"https://www.bing.com/images/async?q={query_encoded}&first={count}&count={step}&adlt=off"
    try:
        res = requests.get(url, headers=headers, timeout=10)
        new_urls = extract_image_urls(res.text)
        if not new_urls:
            print("[!] No more images found, stop.")
            break
        before = len(images)
        for u in new_urls:
            if u not in images:
                images.append(u)
                if len(images) >= limit:
                    break
        added = len(images) - before
        print(f"  - {len(new_urls)} urls extracted, {added} new added, {len(images)} found in total")
    except Exception as e:
        print(f"[!] Connection error: {e}, stop.")
        break
    count += step

print(f"[+] {len(images)} collected images.")

download_dir = os.path.expandvars(f"$HOME/storage/downloads/{query}")
os.makedirs(download_dir, exist_ok=True)

print("[*] Download with axel...")
for i, url in enumerate(images):
    ext = url.split('.')[-1].split("?")[0][:4]
    if not ext.isalpha() or len(ext) > 4:
        ext = "jpg"
    filename = os.path.join(download_dir, f"{query}_{i+1}.{ext}")
    cmd = f"axel -q -T 5 -n 4 -o \"{filename}\" \"{url}\""
    print(f"  [{i+1}] {cmd}")
    os.system(cmd)

print("[✓] Download complete.")