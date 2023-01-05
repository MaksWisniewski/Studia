from crawler import *
from Element import Element
import time

# test

# def test(start_site, max_d, keyword):
#     for url, answer in crawl( Element(start_site, 0, max_d), max_d, keyword):
#         print(f"{url}")
#         for a in answer:
#             print(a, end="\n\n")

def test(start_site, max_d, keyword, NO_THREADS):
    start = time.time()
    run_threads( Element(start_site, 0, max_d), max_d, keyword, NO_THREADS)
    end = time.time()

    for url, answer in result:
        print(f"{url}")
        for a in answer:
            print(a, end="\n\n")
    print('Execution Time: {}'.format(end-start))

def test1(NO_THREADS=8):
    test("https://en.wikipedia.org/wiki/Python_(programming_language)", 2, "Python", NO_THREADS)

def test2(NO_THREADS=8):
    test("http://www.ii.uni.wroc.pl", 2, "python", NO_THREADS)

def test3(NO_THREADS=8):
    test("https://www.lipsum.com/", 1, "pain", NO_THREADS)

# ASK ABOUT ISSUE WITH CLOSURE

if __name__ == "__main__":
    test2(12)
    # test2(4)
