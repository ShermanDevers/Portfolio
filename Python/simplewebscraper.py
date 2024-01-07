import requests
from bs4 import BeautifulSoup

url = input("Input Url to scrape> ")
file_name = input("File Name to put html content in: ")
content = requests.get(url)

with open(file_name, "wb") as pysitew:

    contents = BeautifulSoup(content.text,"html.parser")
    content_pretty = contents.prettify()
    pysitew.write(bytes(content_pretty, "utf-8"))
    print("File Created")
    
links = [link.get("href") for link in contents.find_all("link")]

for link in links:
    if link is None:
        continue
    if "/s" in link:
        print(link)