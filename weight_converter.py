weight = int( input("enter your weight "))
weight_unit = input("enter your weight unit in 'kg' or 'lbs' only:  ").lower()
converted_weight =""

if weight_unit == "kg":
    converted_weight =  weight * 2.2
    print(f"Your weight is {converted_weight} pounds")
    
elif weight_unit =="lbs":
    converted_weight = weight / 2.2
    print(f"Your weight is {converted_weight} kilos")
    
    
else:
    print("Weight has to be in kg or lbs")
