def string_to_list(str_1):
    return str_1.split(',')

def combined_list_sort(list_1, list_2):
    list_combined = list_1 + list_2
    list_combined_sorted = []
    
    while list_combined:
        min_num = list_combined[0]
        for num in list_combined:
            if int(num) < int(min_num):
                min_num = num
        list_combined_sorted.append(min_num)
        list_combined.remove(min_num)
    
    return list_combined_sorted
if __name__=='__main__':
    input_string1 = input('Enter your list 1, separate elements with comma: ') 
    input_string2 = input('Enter your list 2, separate elements with comma: ')

    list_1 = string_to_list(input_string1)
    list_2 = string_to_list(input_string2)

    print(combined_list_sort(list_1, list_2))