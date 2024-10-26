def revers_str(string):
    lenght_str=len(string)
    i=1
    reversed_str=''
    while lenght_str-i>=0:
        reversed_str+=string[lenght_str-i]
        i+=1
    return reversed_str


print(revers_str('12345'))