import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import time
  
news_items = []
#All you should need to edit are the sources.  I left these sources in as placeholders so you can see how the program works.    
sources = ["http://www.koco.com/topstories-rss", "http://feeds.marketwatch.com/marketwatch/realtimeheadlines/", "http://feeds.washingtonpost.com/rss/politics?itid=lk_inline_manual_2", "http://www.espn.com/espn/rss/news"]
while True:
    for sites in sources:
        url = sites
        resp = urllib.request.urlopen(url).read()
        soup = BeautifulSoup(resp, "html.parser")
        items = soup.findAll('item')
        for item in items:
            news_item = item.title.text
            if news_item in news_items:
                continue
            news_items.append(news_item)    
            print(news_item)
        time.sleep(15)