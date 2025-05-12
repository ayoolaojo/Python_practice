try:
    age = int(input("Age: "))
    print(age)
    
except ValueError:
    print("invalid input")
except ZeroDivisionError:    
    print("age cannot be divided by zero")
    