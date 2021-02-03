from bs4 import BeautifulSoup
from urllib.request import urlopen

# Set page parameters
url = "http://olympus.realpython.org/profiles/dionysus"
page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser") # create a beautifulsoup object and assign the html, and html parser to it

# Outputs 
print(soup.get_text())
# print(soup.find("Name")) # find the value in name (Dionysus)
print(soup.find_all("img"))