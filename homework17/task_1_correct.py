def nums(n):
    counter=0
    print(n,end=' ')
    while n > 1:
        if n % 2 == 0:  # If n is even
            n = n // 2
        else:           # If n is odd
            n = 3 * n + 1 
        counter+=1
        print(n,end=' ')
    print()
    print(f'count is - {counter}')
    

def cached_nums(n,cache):
    cached_counter=0
    k=n
    result=[]
    while n > 1:
        if cache.get(n):
            result.extend(cache.get(n))
            break
        if n % 2 == 0:  # If n is even
            n = n // 2
        else:           # If n is odd
            n = 3 * n + 1    
        cached_counter+=1
        result.append(n)  
    
    print(f'cached count is - {cached_counter}') 
    print([k]+result )   
    cache[k]=result
    print(cache)
    
cache={}
def main():
    cached_nums(6,cache)
    print(50*"_")
    
    cached_nums(12,cache)
    print(50*"_")
    
    nums(6)
    print(50*"_")
    
    nums(12)

if __name__=='__main__' :
    main()