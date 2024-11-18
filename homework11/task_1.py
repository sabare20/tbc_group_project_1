def switch_temp(value=35,measure='C'):
    if measure=='C':
        F=value*9/5+32
        return F
    elif measure=='F':
        C=(value-32)*5/9
        return C
    else :
        return 'measure is incorrect !'
    
print(switch_temp())
        