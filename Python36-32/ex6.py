n1=input("Write something ")
n2=int(input("Enter number "))
n2=n2-1
n3=n1[:n2]+n1[n2+1:]
print(n3)
