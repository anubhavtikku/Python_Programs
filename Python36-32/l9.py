a=[1, 2, 3,5.7, 'hello', 5.7, 'world']
b=[1,2,3]
c=[]
for i in a:
    if i in b:
        c.append(i)
c=c+["q9"]
print(c)
