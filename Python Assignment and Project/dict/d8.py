D={'d':4,'c':3,'b':2,'a':1}
e={}
for i in sorted(D):
    e.update({i:D[i]})
print(e)
