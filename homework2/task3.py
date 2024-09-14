number=int(input('enter number from 1 to 10 :'))
if number<1 or number>10 :
    print('entered number is invalid')
    exit(1)

if number % 7==0 :
    print(7)
elif number % 5==0 and number % 2!=0:
    print(5)
elif number % 5==0  and number % 2==0 :
    print(2,5)
elif  number % 2==0 and number % 3==0 :
    print(2,3)
elif number % 2==0 and number % 3!=0 and number % 5!=0:
    print(2)
elif number % 3==0 and number % 2!=0:
    print(3)
    

    