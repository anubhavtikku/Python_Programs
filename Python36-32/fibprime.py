def prime(x):
    l=True
    for i in range(2,x):
        if x%i==0:
            l=False
            break
    if l:
        return x
    else:
        pass
    

def fib(x):
    a=[0]
    if x==1:
        return a;
    a=a+[1]
    if x==2:
        return a;

    for i in range(2,x):
        k=a[-1]+a[-2]
        a=a+[k]
    return a

def sqr(i):
    return i*i
    
#lst=list(map(prime,fib(10)))
#lst=list(filter(prime,fib(10)))
#lst=list(map(sqr,fib(10)))
lst=list(map(lambda i:i*i,fib(10)))
print(lst)
        
