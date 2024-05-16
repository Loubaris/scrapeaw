<h3 align="center">ScrapeAW</h3>


<p align="center">ScrapeAW is a framework that without API scrapes
IPs<br>across the world using Shodan</p>


```python

Modules needed: (request)
Usage: scrape <shodan> <subject1+subject2> <path_to_save>

#Example running scrapaw.py
(scrapaw)>scrape shodan Android+Debug+Bridge /Desktop/

#Example importing scrapaw
from scrapaw import scrape

scrape("scrape shodan Denver+Webcams /HiddenFolder/")

```
