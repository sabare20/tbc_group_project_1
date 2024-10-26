def prime_num_detector(x):
    x=int(x)
    prime=False
    is_prime=''
    if x>1:
        for i in range(2,x//2+1):
            if x%i==0:
                prime=True
                is_prime=f'{x} is not prime '
                break
        if prime==False:
            is_prime=f'{x} is prime'
        return is_prime
    else:
        is_prime='1 is not prime number  and also is not composite number.please enter numberwhich is different to 1 '
    return is_prime

print(prime_num_detector(1))
        
        
        
        