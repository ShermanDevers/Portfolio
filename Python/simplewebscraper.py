import requests

url = input("Input Url to scrape> ")

r = requests.get(url)
with open(
    "/Users/sd320/OneDrive/Desktop/PythonCode/pythonsite.html", "wb"
) as pysitew:
    pysitew.write(r.content)
