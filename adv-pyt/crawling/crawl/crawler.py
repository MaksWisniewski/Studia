from Element import Element
from queue import Queue

import requests, bs4
from urllib.parse import urlparse, urljoin
from General import match_word



# Queue is a thread safe structure, possibly containing Elements i.e websites to crawl.
q = Queue()

# Set containing strings (i.e links) that were invalid or processed
visited_pages = set()

# q.put(1)

# def f():
#     print(type(q))
#     #global q
#     #q = Queue()

# f()

# while q.qsize():
#     print(q.get())

def crawl(start_page : Element, max_depth : int, keyword : str):
    # Add start_page to queue
    q.put( start_page )

    while q.qsize():

        # Take element from the top of the queue.
        top = q.get()

        # Check if page fits the range
        if not top.isValid():
            continue

        # Check if page was processed in the past.
        if top.get_url() in visited_pages:
            continue
        else:
            # Mark page as visited.
            visited_pages.add(top.get_url())
        
        # Start processing neighbours of page.
        try:
            html = requests.get(top.get_url()).text
        except:
            continue

        # Yield result
        
        yield (top.get_url(), match_word(keyword, html))

        parser = bs4.BeautifulSoup(html, "html.parser")

        for page in (link.get("href") for link in parser.find_all("a")):
            # Check relative adreses
            if not urlparse(page).netloc:
                page = urljoin(top.get_url(), page)
            
            if not page in visited_pages:
                q.put( Element(page, top.get_depth()+1, max_depth) )
    
    #idk if nessesary
    return

