import datetime
from forex_python.bitcoin import BtcConverter

def different_usd_amount():
    b=BtcConverter
    purchase_year=int(input('enter urchase year :'))
    
    purchase_month=int(input('emter purchase month :'))
    
    purchase_day=int(input('enter purchase day :'))
    
    purchase_date=datetime.date(purchase_year,purchase_month,purchase_day)
    
    purchased_amount_usd=int(input('enter amount of dolars :'))
    print(purchase_date)
    
    btc_to_usd_previous = b.get_previous_price( 'USD' , purchase_date)
    
    print(btc_to_usd_previous) 
    
    purchased_amount_btc=purchased_amount_usd*btc_to_usd_previous
    
    btc_to_usd_present = b.get_latest_price('USD')
    
    present_amount_usd=purchased_amount_usd/btc_to_usd_present
    
    difference=present_amount_usd-purchased_amount_usd
    
    print(difference)
    
different_usd_amount()


