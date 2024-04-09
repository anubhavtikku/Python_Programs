a=['level','level', 'hello', 'world']
a1=0

for i in a:
    if len(i)>1 and i[0]==i[-1]: 
        a1=a1+1
        
print(a1)            
