import math

house_price = 1000000
deposit =  0
has_good_credit = False

if has_good_credit:
    deposit = house_price * 0.1
else:
    deposit = house_price * 0.2
print(f"Your deposit is ${deposit}")
    