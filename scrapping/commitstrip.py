from bs4 import BeautifulSoup
import urllib.request
import requests

def download_image(img_url, name="image.jpg"):
    req = requests.get(img_url)
    with open(name, "wb") as fichier:
        fichier.write(req.content)


html = urllib.request.urlopen("https://www.commitstrip.com/fr/").read()
soup = BeautifulSoup(html, features="lxml")
#print(soup.prettify())

# soup.select(CSS_SELECTOR )  retourne la liste des elements correspond au selector
# soup.select_one(CSS Selector ) retourne le premier element qui correspond au selector

css_selector_link = "div.excerpts div.excerpt section a"

link = soup.select_one(css_selector_link)
print(link)
final_page_url = link.get('href')
print(final_page_url)
html = urllib.request.urlopen(final_page_url).read()
soup_final = BeautifulSoup(html, features="lxml")

date = soup_final.select_one("header.entry-header > div.entry-meta > a > time")
image = soup_final.select_one('div.entry-content > p > img')

print(date.get_text())
print(image.get('src'))
download_image(image.get('src'))