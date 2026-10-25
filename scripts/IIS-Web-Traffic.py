import random
import requests
import time

urls = [
    "http://10.10.10.10/",
    "http://10.10.10.10/login.html",
    "http://10.10.10.10/admin.html",
    "http://10.10.10.10/downloads.html",
    "http://10.10.10.10/notfound",
    "http://10.10.10.10/phpmyadmin",
    "http://10.10.10.10/wp-admin",
]

while True:
    try:
        url = random.choice(urls)
        r = requests.get(url, timeout=5)

        print(
            f"{time.strftime('%H:%M:%S')} "
            f"{r.status_code} "
            f"{url}"
        )

    except Exception as e:
        print(e)

    time.sleep(random.randint(2, 10))
