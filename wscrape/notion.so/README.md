# Code Repository for Web Scraping Course

This repository contains Jupyter Notebooks with code examples relating to the Real Python video course on Building a Web Scraper with `requests` and Beautiful Soup.

The notebooks 01-03 represent the **web scraping pipeline** discussed in the course:

- **Part 1: Inspect** `01_inspect.ipynb`
- **Part 2: Scrape** `02_scrape.ipynb`
- **Part 3: Parse** `03_parse.ipynb`

The notebooks 04-05 contain tasks to work on individually for each learner to keep practicing the discussed concepts and personalize the project for themselves:

- **Tasks** `04_pipeline.ipynb`
- **Solution** `05_pipeline_solution.ipynb`

Attempt to build out your individual pipeline by yourself and use the solution document only if you get stuck. All the best, and keep learning! :)

# Practical Introduction
[Notion](https://www.notion.so/skinetics/Practical-Introduction-6e3cc304fa9544cbb2b101ec626131a9)

# Urllib
```py
from urllib.request import urlopen 
url = https://olympus.realpython.org/profiles/aphrodite
page = urlopen(url) # taking url variable as an argument/parameter
```

[File](https://github.com/acord-robotics/datascience/blob/main/wscrape/pi/main.py) -> `pi/main.py` inside this folder