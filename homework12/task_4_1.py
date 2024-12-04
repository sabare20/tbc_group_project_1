input_string1=input('enter your list 1 , separate elements with comma :')
list_1=input_string1.split(',')

input_string2=input('enter your list 2 , separate elements with comma :')
list_2=input_string2.split(',')

print(list_1)
print(list_2)

list_combined=list_1+list_2
list_combined_sorted=[]
len_list_comb=len(list_combined)
print(list_combined)



for i in range(len_list_comb):
    min_num=int(list_combined[0])
    for num in list_combined:
        if int(num)<=int(min_num):
            min_num=num
    list_combined_sorted.append(min_num)
    list_combined.remove(min_num)
print(list_combined_sorted)