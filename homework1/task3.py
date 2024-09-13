a=int(input('enter lenght of side a :'))
b=int(input('enter lenght of side b :'))
c=int(input('enter lenght of side c :'))
p=a+b+c
s=(p/2*(p/2-a)*(p/2-b)*(p/2-c))**0.5
print(p,s)