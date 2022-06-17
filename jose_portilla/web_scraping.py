import bs4
import os
import requests

response = requests.get("https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)")
soup = bs4.BeautifulSoup(response.text, "lxml")

for item in soup.select(".toctext"):
    print(item.text)

image_link = requests.get("https:" + soup.select(".thumbimage")[0]["src"])

# Write binary
file = open(os.getcwd() + "/jose_portilla/web_scraping_image1.jpg", "wb")
file.write(image_link.content)
file.close()


###################################################################################################################################################


five_star_titles = []
titles_text_file = "web_scraping_books"

for page in range(1, 51):  # 50 pages
    base_url = f"http://books.toscrape.com/catalogue/page-{page}.html"
    response = requests.get(base_url)
    soup = bs4.BeautifulSoup(response.text, "lxml")
    books = soup.select(".product_pod")

    for book in books:
        # use dot to fill up the space "star-rating Five"
        if len(book.select(".star-rating.Five")) != 0:
            book_title = book.select("a")[1]["title"]
            five_star_titles.append(book_title)

print(f"\nWriting to {titles_text_file}.txt")

with open(os.getcwd() + f"/jose_portilla/{titles_text_file}.txt", "w") as file:
    for i, title in enumerate(five_star_titles):
        file.write(f"{i + 1}: {title}\n")

file.close()
print("Text file is created.")


###################################################################################################################################################


page = 10
authors = set()
quotes = []
tags = []

while str(soup.select("div")).find("No quotes found!") == -1:
    base_url = f"https://quotes.toscrape.com/page/{page}/"
    response = requests.get(base_url)
    soup = bs4.BeautifulSoup(response.text, "lxml")

    for name in soup.select(".author"):
        authors.add(name.text)

    for quote in soup.select(".text"):
        quotes.append(quote.text)

    for tag in soup.select(".tag-item"):
        tags.append(tag.text.replace("\n", ""))

    page += 1

print(authors)
print(quotes)
print(tags)

###################################################################################################################################################
