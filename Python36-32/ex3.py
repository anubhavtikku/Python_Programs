name=input("Write something ")
a=name[0]
b="$"
name1=""+name[0]
for i in range(1,len(name)):
    if name[i]==a:
        name1=name1+b
    else:
        name1=name1+name[i]
print(name1) 
