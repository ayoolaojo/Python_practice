name = input("enter your name :")

if len(name) < 3:
    print("name must be at least 3 characters")
elif len(name) > 50:
    print("name cannot be more than 50 characters")
else:
    print("name looks good")
