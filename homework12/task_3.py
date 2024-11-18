from random import randint
b=[]
new_b=[]
for i in range(50):
    num_1=randint(1,30)
    b.append(num_1)
    if num_1 not in new_b:
        new_b.append(num_1)
print(b)
print(len(b))
print(new_b)
print(len(new_b))
    