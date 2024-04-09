a=[1, 2, 3,5.7, 'hello', 5.7, 'world']
x=len(a)
for i in range(x):
    for j in range(i+1,x+1):
        print(a[i:j])

#for i in range(x):
#    for j in a[x-i-1:]:
#        print(j,end=' ')
#    print()
