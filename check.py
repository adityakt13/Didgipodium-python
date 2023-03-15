def elec_bill(a,b):
    bill_amt = 0
    if a <=100:
        bill_amt = a * 60
    elif a <=300:
        bill_amt = (100*60) + ((a-100)*70)
    else:
        bill_amt = (100*60) + (200*70) + ((a-300)*80)
    print(bill_amt)
elec_bill(305,180,120)
import pandas as pd
a = ['python', 'pandas']
info = pd.DataFrame(a)
print(info) 