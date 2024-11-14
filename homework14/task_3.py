def fib(n):
    x_0=0
    x_1=1
    fib_nums=[]
    for i in range(0,n-1): # რადგან n ცალი წევრის მობრუნება ვინდა და აქ მიმდევრობა ნულოვაით იწყება 1 გამოვაკელი
        if i==0:
            fib_nums.append(x_0)
        if i==1:
            fib_nums.append(x_1)
        else:
            x_n=x_0+x_1
            fib_nums.append(x_n)
            x_0=x_1
            x_1=x_n
            
    return fib_nums
def main():
    fib_list=fib(5) 
    print(list(map(lambda x:x,fib_list)))
    fib_list=fib(8) 
    print(list(map(lambda x:x,fib_list)))
        
if __name__=='__main__':
    
    main()

    
    