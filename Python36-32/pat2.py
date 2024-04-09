import re
s='<customer>1</customer>\n<name>Dean Winchester</name>\n<course>Big Data and Hadoop</course>\n<city>London</city>\n<customer>2</customer>\n<name>Samuel Green</name>\n<course>Python for Big Data Analytics</course>\n<city>Paris</city>'
l1=re.findall("<(\w+)>(.+)</(\w+)",s)
for i in l1:
    print(i[0],':',i[1])

