input_num=int(input('enter number from 10 to 5432 :'))
if input_num>=10 and input_num<=5432:
    counter=0
    for i in range(1,input_num+1):
        if i % 13 ==0:
            print(i)
            counter+=1
    print(f'counter={counter}')
else:
    exit(1)