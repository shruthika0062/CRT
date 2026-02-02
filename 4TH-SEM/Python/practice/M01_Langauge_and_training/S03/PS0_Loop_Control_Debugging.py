#types of errors
#syntax error
#runtime error
#logical error


import pdp
def add(a,b):
    pdp.set_trace()
    return a+b
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
print(add(a,b))