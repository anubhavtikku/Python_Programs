a=[1, 2, 3, 4, 5.7, 'hello', 5.7, 'world']
a1=0
a2=0.0
a3=""
for i in a:
    if type(i)==int:
            a1=a1+i
    elif type(i)==float:
            a2=a2+i
    elif type(i)==str:
            a3=a3+i
print(a1)
print(a2)
print(a3)
	
