import requests
from bs4 import BeautifulSoup

class Scrape:
    def __init__(self,url,file_name):
        self.url = url
        self.file_name = file_name

    def scrape(url,file_name):
        content = requests.get(url)

        with open(file_name, "wb") as pysitew:

            contents = BeautifulSoup(content.text,"html.parser")
            content_pretty = contents.prettify()
            pysitew.write(bytes(content_pretty, "utf-8"))
            print("File Created")



url = input("Input Url to scrape> ")
file_name = input("File Name to put html content in: ")

Scrape.scrape(url,file_name)
