counter_cached=0
counter=0
def nums(n) :
    global counter 
    counter+=1
    if n==1 :
        return 1
    if n%2==0:
        print(n,end=' ')
        return nums(n/2)
    else:
        print(end=' ')
        return nums(3*n+1)

def cached_nums(n,cache) :
    global counter_cached
    counter_cached+=1
    if cache.get(n):
        return cache.get(n)
    if n==1:
        cache[n]=1
        return 1
    if n%2==0:
        cache[n]=cached_nums(n//2,cache)
    else:
        cache[n]=cached_nums(3*n+1,cache)
    return cache[n]
def main():
    print(cached_nums(12,{}))
    print(f'cached count is - {counter_cached}')
    print(nums(12))
    print(f'count is -{counter}')
    
if __name__=='__main__' :
    main()