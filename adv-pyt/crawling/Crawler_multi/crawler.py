from Element import Element
from queue import Queue

import requests, bs4
from urllib.parse import urlparse, urljoin
from General import match_word

import threading

# create an instance of lock class
lock = threading.Lock()

# because i could figure out how to yield
result = []

# Queue is a thread safe structure, possibly containing Elements i.e websites to crawl.
q = Queue()

# Set containing strings (i.e links) that were invalid or processed
visited_pages = set()


def Init_queue(start_page : Element):
    # Add start_page to queue
    q.put( start_page )

# Proccess the top element of the queue
def process_top(max_depth : int, keyword : str):
    # Take element from the top of the queue.
    try:
        top = q.get()
    except:
        return
    # catch empty

    # Check if page fits the range
    if not top.isValid():
        return


    # lock
    # Check if page was processed in the past.
    with lock:
        if top.get_url() in visited_pages:
            return
        else:
            # Mark page as visited.
            visited_pages.add(top.get_url())
   

    # Start processing neighbours of page.
    try:
        html = requests.get(top.get_url()).text
    except:
        return

    # Yield result
    
    result.append( (top.get_url(), match_word(keyword, html)) )

    parser = bs4.BeautifulSoup(html, "html.parser")

    for page in (link.get("href") for link in parser.find_all("a")):
        # Check relative adreses
        if not urlparse(page).netloc:
            page = urljoin(top.get_url(), page)
        
        with lock:
            if not page in visited_pages:
                q.put( Element(page, top.get_depth()+1, max_depth) )
    
    return


def crawl(max_depth : int, keyword : str):
    print("------CRAWL ACTIVATED")
    while q.qsize():
        process_top(max_depth, keyword)
    
def boot(start_page : Element, max_depth : int, keyword : str):
    Init_queue(start_page)
    for _ in range(2):
        process_top(max_depth, keyword)

def run_threads(start_page : Element, max_depth : int, keyword : str, NO_THREADS):
    THREADS = list()
    boot(start_page, max_depth, keyword)
    for _ in range(NO_THREADS):
        x = threading.Thread(target=crawl, args=(max_depth, keyword)) # or args=(max_depth, keyword, ) ??
        THREADS.append(x)
        x.start()

    for X in THREADS:
        X.join()
