import re, nltk, bs4


def match_word(word : str, text : str):
    parser = bs4.BeautifulSoup(text, 'html.parser')

    # Get list of html elements containing text
    filter_elements = ['script', 'style', 'head', 'title', 'meta']
    text = filter(lambda element: element.parent.name not in filter_elements, parser.findAll(text=True))
    
    word = re.compile(word+'[^a-zA-Z]')

    for element in text:
        yield from filter(lambda sentence: word.search(sentence), nltk.sent_tokenize(element.string))

