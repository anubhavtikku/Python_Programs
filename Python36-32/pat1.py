import re
fil=open(r"C:\Users\Mahe\Desktop\a.txt")
s=fil.read()
fil.close()
l1=re.findall("<\w+>",s)
l2=[]
for i in l1:
    l2=l2+[i[1:-1]]
    
lst=re.findall("\w+",s)
k=0
for i in lst:
    if i in l2:
        if k==0:
            print(i,':',end=' ')
            k=1
        else:
            print('')
            k=0
    else:
        print(i,end=' ')
    
       
       




