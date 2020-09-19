import requests
from bs4 import BeautifulSoup
from components.chapter import Chapters

def main():
    #anime_name = input('Please enter the anime you want to download : ')

    new_anime = Chapters("boku-no-hero-academia")

    if new_anime.supported():
        source_code = requests.get(new_anime.get_url())
        soup = BeautifulSoup(source_code.text, "html.parser")
        for tr in soup.find_all('tr'):
            values = [td.text for td in tr.find_all('td')]
            print(values)
    else:
        print("This anime is not supported by this program at the moment.")

def download_images():
    url = "https://www.mangasail.co/content/boku-no-hero-academia-284"
    source = requests.get(url)
    soup = BeautifulSoup(source.text, 'html.parser')
    for div in soup.find('div', {'id': 'images'}):
        print(div)
        for img in div.find_all('img'):
            print(img['src'])

if __name__ == "__main__":
    #main()
    download_images()