from utils.settings import *

class Anime():
    """This class will be the instance of every Anime that we will 
    going to scrape."""
    def __init__(self,name: str = None):
        self.name = name
        self.url = MANGA_WEBSITE_URL

    def supported(self):
        """This method will determine if the instace of anime is 
        currently supported by this application."""
        if self.name in ANIME_LIST:
            return True
        else:
            return False

    def total_supported(self):
        """This method  will return the total anime supported by this application."""
        return len(ANIME_LIST)

    def get_url(self):
        """This method will return the url of the anime that contains the list of chapters currently available."""
        anime_chpaters_url = self.url + self.name + '-manga'
        return anime_chpaters_url

    def __str__(self):
        return f"Anime: {self.name.replace('-', ' ')}."
    