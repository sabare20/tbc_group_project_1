high_num=int(input('enter number fro 1 to 50 :'))
tree='/|\\'
if high_num>0 and high_num<50:
    for i in range(1,high_num+2):
        if i==1 :
            print(' *')
        elif i>1 :
            print(tree)
else:
    print('entered number is out of range, please enter number within range.')
    exit(1)