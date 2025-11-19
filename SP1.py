import requests
from bs4 import BeautifulSoup

url = "https://wikipedia.org"
response = requests.get(url)

if response.status_code != 200:
    print("Failed to retrieve the webpage")
    exit()

html_content = response.text   # store HTML

soup = BeautifulSoup(html_content, "html.parser")

headlines = soup.find_all("h1")

with open("headlines.txt", "w", encoding="utf-8") as file:
    for h in headlines:
        title = h.get_text(strip=True)
        if title:
            file.write(title + "\n")

print("Headlines saved to headlines.txt")
