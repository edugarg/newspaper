import re
from collections import Counter
from newspaper import Article

def body(url):
    article = Article(url)
    article.download()
    article.parse()
    #re.split("[^a-zA-Z\d]",article.text)
    #re.split("[^a-z\d]",article.text.lower())
    return Counter(re.split(r'[\W\d]+',article.text))