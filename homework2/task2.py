number_1=int(input('enter first number :'))
number_2=int(input('enter second number :'))
division_reminder=number_1 % number_2
if division_reminder!=0 or number_1==0:
    print('first number is not multiple of second number ')
else:
    print('first number is multiple of second number')   