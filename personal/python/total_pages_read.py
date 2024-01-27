#program that takes the data from goodreads and calculates the total number of pages read

#importing packages
import requests
import bs4
import re
import tqdm

def book_details(url):
    full_url = "https://www.goodreads.com" + url
    response = requests.get(full_url)
    soup = bs4.BeautifulSoup(response.text, "html.parser")
    title_element = soup.find("h1", {"class": "Text"})
    if title_element is not None:
        title = title_element.text
    else:
        title = "No title found"
    BookDetails = soup.find("div", {"class": "BookDetails"})
    try:
        page = BookDetails.find("p",{"data-testid" : "pagesFormat"}) # type: ignore
    except AttributeError:
        page = None
    if page is None:
        page = "No pages found"
    else:
        page = page.text # type: ignore
    try:
        pages = int(page.split()[0])
    except ValueError:
        pages = 0
    books[title] = pages

url = "https://www.goodreads.com/review/list/169588719?ref=nav_mybooks"
response = requests.get(url)
soup = bs4.BeautifulSoup(response.text, "html.parser")

books = {}

#find all a tag containing the words /book/show
book_tags = soup.find_all("a", href=re.compile("/book/show"))
book_url = [book.get("href") for book in book_tags]

for book in tqdm.tqdm(book_url):
    book_details(book)

for book, pages in books.items():
    print(f"{book}: {pages}")
print(f"Total pages read: {sum(books.values())}")