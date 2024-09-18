import random 
def my_card() :
    _type=random.randint(1,4)
    _name=random.randint(1,13)
    if _type== 1 :
        if _name>1 and _name<11:
            print('♦',_name)
        elif _name==1:
            print('♦','A')
        elif _name==11:
            print('♦','J')
        elif _name==12:
            print('♦','Q')
        else:
            print('♦','K')
    elif _type==2 :
        if _name>1 and _name<11:
            print('♥',_name)
        elif _name==1:
            print('♥','A')
        elif _name==11:
            print('♥','J')
        elif _name==12:
            print('♥','Q')
        else:
            print('♥','K')
    elif _type==3:
        if _name>1 and _name<11:
            print('♣',_name)
        elif _name==1:
            print('♣','A')
        elif _name==11:
            print('♣','J')
        elif _name==12:
            print('♣','Q')
        else:
            print('♣','K')
    elif _type==4 :
        if _name>1 and _name<11:
            print('♠',_name)
        elif _name==1:
            print('♠','A')
        elif _name==11:
            print('♠','J')
        elif _name==12:
            print('♠','Q')
        else:
            print('♠','K')
    else:
        print('error')
        
my_card()


def my_card2() :
    random_type=random.choice(('♣','♥','♦','♠'))
    random_name=random.choice(('2','3','4','5','6','7','8','9','10','J','Q','K','A'))
    print(random_type, random_name)
    
my_card2()