D={'a':1,'b':2,'c':3,'d':4}
print(D)
b=input('Enter char ')
if b in D.keys():
    D.pop(b)
    print("Key removed")
    print(D)
else:
    print("Key not present")
    
