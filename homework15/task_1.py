from random import randint
odd_counter=0
even_counter=0
for i in range(100):
    rand_num=randint(1,1000)
    if rand_num%2==0:
        even_counter+=1
    else:
        odd_counter+=1
counter={'odd':odd_counter,'even':even_counter}
print(counter)       

    
    