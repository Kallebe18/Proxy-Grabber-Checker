import requests
from zipfile import ZipFile
from bs4 import BeautifulSoup as bsoup

url = "http://www.vipsocks24.net"

req = requests.get(url)

soup = bsoup(req.text, "lxml")
element = soup.find("h3", class_="post-title entry-title")
link = element.findChildren("a", recursive=False)[0]["href"]

req = requests.get(link)
soup = bsoup(req.text, "lxml")
link = soup.find("img", alt="Download").parent["href"]

req = requests.get(link)
soup = bsoup(req.text, "lxml")
link = soup.find("a", id="download-url")["href"]

req = requests.get(link, stream=True)
with open("vipsocks.zip", "wb") as raw:
	raw.write(req.content)

with ZipFile("vipsocks.zip", "r") as ZipObj:
	ZipObj.extract("vipsocks.txt")
