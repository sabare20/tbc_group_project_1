

def sorted_list(list_combined):
    list_combined_sorted=[]
    for i in range(len(list_combined)):
        min_num=int(list_combined[0])
        for num in list_combined:
            if int(num)<=int(min_num):
                min_num=num
        list_combined_sorted.append(min_num)
        list_combined.remove(min_num)
    return list_combined_sorted
    
def main():
    input_string1=input('enter your list 1 , separate elements with comma :')
    input_string2=input('enter your list 2 , separate elements with comma :')
    list_1=input_string1.split(',')
    list_2=input_string2.split(',')
    list_combined=list_1+list_2
    return list_1,list_2,list_combined,sorted_list(list_combined)
    


if __name__=='main':
    main()
    

    



    
    
    
