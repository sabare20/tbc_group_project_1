from random import randint
#for i in range(100):
    #random_num=randint(1,100000000)
    #list_num.append(random_num) 
list_num=[randint(1,100000) for i in range(100)]   
    

sorted_list_num=sorted(list_num)
longest_num=max(sorted_list_num)
smallest_num=min(sorted_list_num)
sorted_list_num_reversed=sorted(list_num,reverse=True)
print(sorted_list_num)
print(longest_num)
print(smallest_num)
print(sorted_list_num_reversed)


        
        
    
    
    
    
    
