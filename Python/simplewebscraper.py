import requests
from bs4 import BeautifulSoup

url = input("Input Url to scrape> ")

content = requests.get(url)

with open(
    "scraped_website.html", "wb") as pysitew:
    contents = BeautifulSoup(content.text,"html.parser")

    contents = contents.prettify()
    pysitew.write(bytes(contents, "utf-8"))
