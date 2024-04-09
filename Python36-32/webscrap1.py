from bs4 import BeautifulSoup

"""
#soup=BeautifulSoup(open("C:\\Users\\Mahe\\Desktop\\t.html"))
soup=BeautifulSoup("<html><head><title>hello world</title></head><body><h1>hello world</h1></body></html>")
print(soup.prettify())
#print(soup.find_all('p'))
#print(soup.b.parent)
#print(soup.title.next)
#print(soup.html.contents)
#print(soup.body.contents)
#print(soup.body.p.nextSibling.nextSibling)
"""
"""soup=BeautifulSoup('<b class="Price" id="first" border="2">new price</b>'
                   '<h1>web scrapping demo</h1>')
tag=soup.h1
#tag=soup.b
#print(tag)
#print(tag.attrs)
#for k,v in  tag.attrs.items():
#    print(k,v)
#print(tag["class"])
#print(tag["id"])
#print(soup)
print(tag.string)
"""
