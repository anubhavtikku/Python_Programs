a=[1, 2, 3, 4, 5.7, 'hello', 5.7, 'world']
a1=0

for i in a:
    if type(i)==int or type(i)==float:
        if i>a1:
            a1=i
        
print(a1) 
