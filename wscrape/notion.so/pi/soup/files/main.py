from bs4 import beautifulsoup #https://www.notion.so/skinetics/Practical-Introduction-6e3cc304fa9544cbb2b101ec626131a9
from urllib.request import urlopen 

# Set page parameters
url = "http://olympus.realpython.org/profiles/dionysus"
page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")
print(soup.get_text())