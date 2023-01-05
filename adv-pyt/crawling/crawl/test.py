from crawler import crawl
from Element import Element

# test

def test(start_site, max_d, keyword):
    for url, answer in crawl( Element(start_site, 0, max_d), max_d, keyword):
        print(f"{url}")
        for a in answer:
            print(a, end="\n\n")

def test1():
    test("https://en.wikipedia.org/wiki/Python_(programming_language)", 1, "Python")

def test2():
    test("http://www.ii.uni.wroc.pl", 2, "python")

def test3():
    test("https://www.lipsum.com/", 1, "pain")



if __name__ == "__main__":
    test1()