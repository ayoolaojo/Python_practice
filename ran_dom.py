import random

for i in  range(3):
   print(random.random()) 
   

for i in range(5):
    print(random.randint(10,20))
    

members= ["Ayoola", "Josh","Samuel", "Talato"]
leader = random.choice(members)
print(leader)

