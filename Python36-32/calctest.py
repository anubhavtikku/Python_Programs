"""this module contains functions that perform
basic operations"""
def addition(a,b):
    #this function performs addition of two numbers and returns a value
    return a+b

def subtraction(a,b):
    #this function performs subtraction of two numbers and returns a value
    return a-b

def multiplication(a,b):
    #this function performs multiplication of two numbers and returns a value
    return a*b

def division(a,b):
    #this function performs division of two numbers and returns a value
    return a/b

if __name__=="__main__":
    res1=addition(12,13)
    print("Sum of digits is {}".format(res1))

    res2=subtraction(12,13)
    print("Difference of digits is {}".format(res2))

    res3=multiplication(12,13)
    print("Multiplication of digits is {}".format(res3))
