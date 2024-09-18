import random
import datetime 
def birth_weekday() :
    year=random.randint(1900,2024)
    month=random.randint(1,12)
    day=random.randint(1,31)
    weekday=datetime.date(year,month,day).isoweekday()
    print(weekday)
    
birth_weekday()