from random import randint

x=randint(1,50)
for i in range(1,x+1):
    print(i,'- ',end=" ")
    for n in range(1,i+1):
        if i % n==0:
            print(n,end=' ')       
    print()


    
