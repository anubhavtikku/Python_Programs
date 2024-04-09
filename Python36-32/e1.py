a=["a","bb","ccc","dddd"]
for i in a[:]:
    if len(i)<4:
        a.append(i)
print(a)
