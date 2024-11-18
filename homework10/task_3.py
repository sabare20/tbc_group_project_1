def factorial(x):
    x=int(x)
    i=0
    factorial=1
    if x==0:
        factorial=1
    while x-i>0:
        factorial*=x-i
        i+=1
    return factorial
print(factorial(3))
        