name=input("Write something ")
x=len(name)
if x<2:
    print("Small string")
else:
    str=name[0]+name[1]+name[-2]+name[-1]
    print(str)
