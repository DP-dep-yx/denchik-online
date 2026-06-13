#!/usr/bin/env python3
import urllib.request
import json

KEY = "3a658958acba03d12755f658d4ee9eb5"
HOST = "denchik.online"
BASE = f"https://{HOST}"

URLS = [
    f"{BASE}/",
    f"{BASE}/categories.html",
    f"{BASE}/cat-aksessuary.html",
    f"{BASE}/cat-elektronika.html",
    f"{BASE}/cat-igrushki.html",
    f"{BASE}/cat-instrumenty.html",
    f"{BASE}/cat-keramika.html",
    f"{BASE}/cat-odezhda-obuv.html",
    f"{BASE}/cat-odezhda.html",
    f"{BASE}/cat-orehi.html",
    f"{BASE}/cat-posuda.html",
    f"{BASE}/cat-stroymaterialy.html",
    f"{BASE}/cat-sukhofrukty.html",
    f"{BASE}/cat-tekstil.html",
    f"{BASE}/cat-tovary-doma.html",
    f"{BASE}/cat-zapchasti.html",
    f"{BASE}/nut-arakhis.html",
    f"{BASE}/nut-fistashki.html",
    f"{BASE}/nut-funduk.html",
    f"{BASE}/nut-greckiy-skorlupa.html",
    f"{BASE}/nut-greckiy-yadro.html",
    f"{BASE}/nut-greckiy.html",
    f"{BASE}/nut-kedrovyy.html",
    f"{BASE}/nut-keshu.html",
    f"{BASE}/nut-makadamia.html",
    f"{BASE}/nut-mindal.html",
    f"{BASE}/nut-pekan.html",
    f"{BASE}/nut-smes.html",
]

payload = {
    "host": HOST,
    "key": KEY,
    "keyLocation": f"{BASE}/{KEY}.txt",
    "urlList": URLS,
}

data = json.dumps(payload).encode("utf-8")
req = urllib.request.Request(
    "https://yandex.com/indexnow",
    data=data,
    headers={"Content-Type": "application/json; charset=utf-8"},
    method="POST",
)

with urllib.request.urlopen(req) as resp:
    print(f"Status: {resp.status}")
    body = resp.read().decode()
    if body:
        print(body)
    else:
        print("OK — URLs accepted")
