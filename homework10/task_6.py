def search_car(producer_company,year='2024',**parameters):
    print(f'producer company :{producer_company}')
    print(f'releasing year :{year}')
    for parameter, value in parameters.items():
            print(f'{parameter}: {value}')
    if not parameters:
        print('no additional parameters')     
search_car('mercedes','2022',transmition_types='manual',mileage='87000')