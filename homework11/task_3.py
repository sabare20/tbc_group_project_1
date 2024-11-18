from task_2 import GCD_rec

def LCM():
    X=int(input('enter number X from 1 to 10000 :'))
    Y=int(input('enter number Y from 1 to 10000 :'))
    if X in range(1, 10000) and Y in range(1, 10000):
        lcm=(X*Y)//GCD_rec(X,Y)
        return f'LCM of {X} and {Y} is {lcm}'
    else:
        return 'entered numbers are out of range '
print(LCM())