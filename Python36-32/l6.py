a=[1,2,3,44,5]
a1=max(a)
a2=min(a)

for i in a:
    if i<a1 and i>a2:
        a1=i
        
print(a1)     
