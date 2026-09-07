#!/usr/bin/env python3
from py_compile import main

import requests
from bs4 import BeautifulSoup

url = "https://www.news24.com/news24/southafrica"

headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/150.0.0.0 Safari/537.36"
    ),
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
    "Referer": "https://www.google.com/",
    "Connection": "keep-alive"
}

response = requests.get(url, headers=headers, timeout=10)

print("Status code:", response.status_code)

if response.status_code == 200:

    soup = BeautifulSoup(response.text, "html.parser")

    print("\nSOUTH AFRICAN NEWS HEADLINES")
    print("----------------------------")

    links = soup.find_all("a")

    count = 0
    seen = set()

    for link in links:

        text = link.get_text(" ", strip=True)
        href = link.get("href", "")

        if (
            text
            and 30 < len(text) < 150
            and "/southafrica/" in href
            and text not in seen
        ):
            print("-", text)

            seen.add(text)
            count += 1

        if count == 10:
            break

    print("\nNumber of headlines found:", count)

else:
    print("Could not access the website.")
    print("Server response:", response.status_code)


if __name__ == "__main__":
    main()
