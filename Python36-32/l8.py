a=[[1, 2, 3],[4,5,6],[7,8,9]]
c1=0
x=0
u=-1
for i in a:
    t=0
    for j in i:
        t=t+j
    if t>c1:
        c1=t
        u=x
    x=x+1
print(a[u])
