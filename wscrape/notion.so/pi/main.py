# Import modules & libraries
from urllib.request import urlopen
import re
"""
"""

"""Reg exes"""
re.findall("ab*c", "ac", re.IGNORECASE) 
match_results = re.search("ab*c", "ABC", re.IGNORECASE)
match_results.group()

"""Page 1"""
# Set basic parameters
url1 = 'http://olympus.realpython.org/profiles/aphrodite'
page1 = urlopen(url)
html_bytes1 = page1.read()
html1 = html_bytes1.decode("utf-8")

# Finding title information
title_index1 = html1.find("<title>")
start_title_index1 = title_index1 + len("<title>")
end_title_index1 = html1.find("</title>")
htmlTitle1 = html1[start_title_index1:end_title_index1]



"""Page 2"""
# Set basic parameters of page
url2 = "http://olympus.realpython.org/profiles/poseidon'
page2 = urlopen(url2)
html_bytes2 = page2.read()
html2 = html_bytes2.decode("utf-8")

title_index2 = html2.find("<title>")
start_title_index2 = title.index2 + len("<title>")
end_title_index2 = html2.find("</title>")
htmlTitle2 = html2[start_title_index2:end_title_index2]