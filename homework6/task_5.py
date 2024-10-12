input_num=int(input('enter number from 1 to 10 :'))
x=input_num
z=0

while input_num-z>=0:
    y=0
    while input_num-z-y>0:
        print(' ',end='')
        y+=1
    m=0
    n=0
    while abs(-m)<=m and m<=input_num:
        print(abs(-m),end='')
        m+=1
    print()
    z+=1
    