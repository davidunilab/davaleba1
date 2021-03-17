import matplotlib.pyplot as plt
class Book:
    def __init__(self, name, pages, current_page):
        self.name = name
        self.pages = pages
        self.current_page = current_page
        self.bookmarks = []

    def progress(self):
        return self.current_page / self.pages * 100

    def pages_left(self):
        return self.pages - self.current_page

    def bookmark(self, page):
        self.bookmarks.append(page)

    def average_reading_speed(self):
        avg = sum(self.bookmarks) / len(self.bookmarks)
        plt.plot(self.bookmarks, marker="o")
        plt.title(f"კითხვის საშუალო სიჩქარეა - {avg}")
        plt.xlabel("დღეები")
        plt.ylabel("გვერდები")
        plt.grid()
        plt.show()
        return avg


shta = Book("შთა", 454, 39)
shta.bookmark(23)
shta.bookmark(45)
shta.bookmark(58)
shta.bookmark(123)
shta.bookmark(145)
shta.bookmark(167)
shta.bookmark(190)
shta.bookmark(200)
print(shta.average_reading_speed())

