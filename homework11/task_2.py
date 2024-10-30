

def GCD_iter(a,b):
    if a in range(1, 10000) and b in range(1, 10000):
        min_num=min(a,b)
        gcd=0
        for i in range(1,min_num):
            if a%i==0 and b%i==0:
                gcd=f'GCD of {a} and {b} is {i} '
        return gcd
    else:
        return 'entered numbers are out of range!'
    
    
def GCD_rec(a,b):
    if a in range(1, 10000) and b in range(0, 10000):  #  აქ b  ს ვერ ვადებ შეზღუდვას რომ 0 ზე მეტი იყოს იმიტომ, რომ ფუნქციაში აღარ შესრულდება პირველი if . 
        gcd_recrs=0
        if b==0:
            gcd_recrs=a
            return gcd_recrs
        else:
            return GCD_rec(b,a%b) # აქ იმიტომ არ დავაბრუნე ზედას მსგავსი აოუთფუთი ,რომ  შემდეგ თსქში მჭირდებოდა მთელი რიცხვი და ამის პასუხი სტრინგი იყო .
    else:
        return 'entered nubers are out of range!'
    
if __name__ == "__main__":
    print(GCD_rec(100,200))


# ინფუთბი ფუნცქიებში იმიტომ არ ჩვსვი რომ როცა იმპორტს ვაკეთბდი იქ ორჯერ მიწევდა. 



    

        


    
            
        
        