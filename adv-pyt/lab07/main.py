# Maksymilian Wiśniewski Lab 6, Task 1.

import requests, bs4, re


"""Predicate that check if word is in text using regex.

is_word_in_text("Python", "python is awesome.") -> True
is_word_in_text("Python", "camelCase is pythonic.") -> False
is_word_in_text("Python", "At the end is Python") -> True"""

def is_word_in_text(word : str, text : str) -> bool:
    pattern = r'(^|[^\w]){}([^\w]|$)'.format(word)
    pattern = re.compile(pattern, re.IGNORECASE)
    matches = re.search(pattern, text)
    return bool(matches)

    
# Function crawl is depth first serch on links starting from start, that satisfy the predicate(i.e a function that tells if the 
# target_word is in the web page, and if it is it continues the search until current_depth fits certain range.)
# node must be a link to a page.



# NLTK/




def crawl(node : str, max_depth : int, target_word : str, visited=set()):
    #print(f"debug {node}")
    reqs = requests.get(node).text
    soup = bs4.BeautifulSoup(reqs, 'html.parser')

    # yields webpage if satisfies the predicate
    if is_word_in_text(target_word, reqs):
        yield node

    # mark current page as visited
    if visited is None:
        visited = ()
    visited.add(node)

    # find all subpages starting from current webpage
    urls = []
    for link in soup.find_all('a'):
        urls.append(link.get('href'))


    # if distance fits in the range call crawl recursively
    if max_depth > 0:
        for page in urls:
            if not page in visited:
                try:
                    yield from crawl(page, max_depth-1, target_word, visited)
                except:
                    # unable to reach the page
                    continue



def test1():
    for url in crawl("https://pl.wikipedia.org/wiki/Guido_van_Rossum", 2, "python"):
        print(f"{url}")

def test2():
    for url in crawl("http://www.ii.uni.wroc.pl", 1, "python"):
        print(f"{url}")

def test3():
    for url in crawl("https://oeis.org/", 2, "triangle"):
        print(f"{url}")

if __name__ == "__main__":
    # for url in crawl("https://pl.wikipedia.org/wiki/Czechy", 1, "Brno"):
    #     print(f"{url}")
    test1()

