from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

def getTitle(url):
    try:
        html=urlopen(url)
    except HTTPError as e:
        return None
    try:
        bs = BeautifulSoup(html.read(),'html.parser')
        title = bs.h1
    except AttributeError as e:
        return None
    return title

title = getTitle('http://www.pythonscraping.com/exercises/exercise1.html')
if title == None:
    print('找不到标题')
else:
    print(title)