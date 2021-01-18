from bs4 import BeautifulSoup
import urllib.request

req = urllib.request.urlopen('https://www.ua-football.com/sport')
html = req.read()

soup = BeautifulSoup(html, 'html.parser')
news = soup.find_all('li', class_ = 'liga-news-item')
results = []

for item in news:
    title = item.find('span', class_='d-block').get_text(strip=True)
    print(title)
    desc = None
    href = None

