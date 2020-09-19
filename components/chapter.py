from .anime import Anime
class Chapters(Anime):
    """This class will create instance of the anime chapter which includes the total pages, etc."""
    def __init__(self, name,):
        super().__init__(name)
        self.chapter_list = []

    def total(self)  -> int:
        return len(self.chapter_list)

    def latest(self) -> str:
        return self.chapter_list[0]