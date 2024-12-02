from random import randint
list_1=[]
list_2=[]
list_3=[]
for i in range(30):
    num=randint(1,1000)
    if i <10:
        list_1.append(num)
    elif i>=10 and i<20:
        list_2.append(num)
    else:
        list_3.append(num)
print(list_1)
print(list_2)
print(list_3)
for n in range(10):
    print(f'when n={n}:{list_1[n]+list_2[n]+list_3[n]}')