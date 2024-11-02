from random import randint
a=[]
new_a=[]
for i in range(50):
    num=randint(1,30)
    a.append(num)
    for n in range(num):
        new_a.append(num) # len of new_a must be equal of sum of a
        
print(a)
print(new_a)
print(len(new_a))
print(sum(a))

    

