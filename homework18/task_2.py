results = {}
# a
with open('data.txt','r') as file:
    max_quantity = 0
    max_person = []
    
    for line in file:
        line = line.strip()
        columns = line.split(',')
        
        person=columns[0]
        quantity = float(columns[3])
        
        if quantity >= max_quantity:
            max_quantity = quantity
            max_person = [person]
    
    print(f'\nperson who bought maximum quantity ({max_quantity}):')
    for person in max_person:
        print(person)
results['max_quantity_persons'] = {'quantity':max_quantity,'persons':max_person}
print()

#b

with open('data.txt','r') as file:
    for line in file:
        line = line.strip().split(',')
        
        customers = line[0]
        quantity = float(line[2])
        price = float(line[3])
        total_purchase = quantity * price
        max_purchase = 0
        max_purchase_person = []
        
        for  customer in customers:
            if total_purchase >= max_purchase:
                max_purchase = total_purchase
                max_purchase_person += customer
    print(f'\nperson who purchased maximum  ({max_purchase}):')
    for person in max_purchase_person:
        print(person)
results[max_purchase_person] = {'maximum purchase':max_purchase,'person':max_purchase_person}
            
        
        


