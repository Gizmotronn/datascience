from urllib.request import urlopen
url = 'http://olympus.realpython.org/profiles/aphrodite'
page = urlopen(url)
page
html_bytes = page.read()
html = html_bytes.decode("utf-8")
print(html)
title_index = html.find("<title>")
title_index
print(title_index)
