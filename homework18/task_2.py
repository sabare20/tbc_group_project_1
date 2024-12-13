results = {}
# a - max_quantity_person
with open('homework18/data.txt','r') as file:
    max_quantity = 0
    max_person = []
    
    for line in file:
        line = line.strip()
        columns = line.split(',')
        
        person=columns[0]
        quantity = float(columns[3])
        
        if quantity > max_quantity:
            max_quantity = quantity
            max_person = [person]
        elif quantity == max_quantity:
            max_person.append(person)
    
    print(f'\nperson who bought maximum quantity ({max_quantity}):',end=' ')
    for person_ in max_person:
        print(person)
        
results['max_quantity_persons'] = {'quantity':max_quantity,'persons':max_person}


#b - max_purchase_person

with open('homework18/data.txt','r') as file:
    person_purchase = {}
    for line in file:
        line = line.strip().split(',')
        customer = line[0]
        quantity = float(line[2])
        price = float(line[3])
        max_purchase_person = []
        max_purchase = 0
        total_purchase = quantity * price
        if customer not in person_purchase.keys():
            person_purchase[customer] = quantity * price 
        else:
            person_purchase[customer] += quantity * price
        
    for customers_,purchase in person_purchase.items():
        if purchase > max_purchase :
            max_purchase_person = [customers_]
            max_purchase = purchase
        elif purchase == max_purchase :
            max_purchase_person.append(customers_)
        
    print(f'\nperson who purchased maximum  ({max_purchase}):',end=' ')
    for person in max_purchase_person:
        print(person)
results['max_purchase_person'] = {'maximum purchase':max_purchase,'person':max_purchase_person}

#c - avg_value_sales

with open('homework18/data.txt','r') as file:
    sum_value = 0
    line_count = 0
    for line in file :
        
        line = line.strip().split(',')
        quantity = float(line[2])
        price = float(line[3])
        
        sum_value += quantity * price
        line_count += 1
      
    avg_value = sum_value / line_count
    
    print(f'\naverage value of sales is: {avg_value}')  
    
results['average_value_sales'] = avg_value

#d - avg_quantity
    
with open('homework18/data.txt','r') as file:
    sum_quantity = 0
    line_count = 0
    for line in file:
        line = line.strip().split(',')
        quantity = float(line[2])
        
        sum_quantity += quantity
        line_count += 1
        
    avg_quantity = sum_quantity / line_count 
    
    print(f'\naverage quantity of sales is : {avg_quantity}')

results['average_quantity_sales'] = avg_quantity

#e - max_quantity_prodact
    
with open('homework18/data.txt','r') as file:
    products_quantity = {}
    for line in file :
        line=line.strip().split(',')
        products = line[1]
        quantity = int(line[2])
        max_quantity_product = []
        max_qunatity_by_prod = 0
        if products not in products_quantity.keys():
            products_quantity[products] = quantity
        else:
            products_quantity[products] += quantity
            
    for product,quantity_ in products_quantity.items():
        if quantity_ > max_qunatity_by_prod :
            max_qunatity_by_prod = quantity_
            max_quantity_product = [product]
        elif quantity == max_qunatity_by_prod:
            max_quantity_product.append(product)
    
    print(f'\nmaximum quantity products ({max_qunatity_by_prod}) are:',end=' ')
    for product_ in max_quantity_product:
        print(product_,end=' ')

results['maximum_quantity_product'] = {'maximum qunatity':max_qunatity_by_prod,'product':max_quantity_product}
print()
print()
print(results)