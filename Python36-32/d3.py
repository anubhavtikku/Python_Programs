dic1={1:10, 2:20,3:30, 4:40}
j=int(input('Enter no '))
k=0
for i in dic1.keys():
    if j==i:
        k=1
        break
if k==1:
    print('Key exists')
else:
    print('Key doesn''t exist')
