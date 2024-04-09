from bs4 import BeautifulSoup
import urllib.request

url="https://www.imdb.com/chart/top"
link=urllib.request.urlopen(url)
res=link.read()
bs=BeautifulSoup(res)
link.close()
print(bs)
for links in bs.find_all("td",{"class":"titleColumn"}):
    print(links.find_next("a").string,links.find_next("strong").string,links.find_next("span").string)
