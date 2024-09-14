velocity=float(input('enter velocity :'))
if velocity>0 and  velocity<30 :
    print('slow')
elif velocity >=30 and velocity<60 :
    print('moderate')
elif velocity>=60 and velocity<120 :
    print('fast')
elif velocity >= 120 :
    print('very fast')
else :
    print('entered velocity is ivalid')
