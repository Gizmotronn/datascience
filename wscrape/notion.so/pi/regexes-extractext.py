import re
from urllib.request import urlopen

# Setting page parameters
url = "http://olympus.realpython.org/profiles/dionysus"
page = urlopen(url)
html = page.read().decode("utf-8")
#print(html)

# Find title
pattern = "<title.*?>.*?</title.*>"
match_results = re.search(pattern, html, re.IGNORECASE)
title = match_results.group()
title = re.sub("<.*?>", "", title) # remove HTML tags
print(title)

# Find Name
namePattern = "<h2.*?>.*?</h2.*>"
name_results = re.search(namePattern, html, re.IGNORECASE)
name = name_results.group()
name = re.sub("<.*?>", "", name)
print(name)

# Find name & favourite colour
for string in ["Name: ", "Favorite Color:"]:
    string_start_idx = html_text.find(string)
    text_start_idx = string_start_idx + len(string)

    next_html_tag_offset = html_text[text_start_idx:].find("<")
    text_end_idx = text_start_idx + next_html_tag_offset

    raw_text = html_text[text_start_idx : text_end_idx]
    clean_text = raw_text.strip(" \r\n\t")
    print(clean_text)