class Point:
    
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def move(self):
        print("move")
        
    def draw(self):
        print("draw")
        
Point1 = Point(10,20)  
# Point1.x = 20 
# Point1.y = 30  
print(Point1.x) 
print(Point1.y) 



class Person:
    def __init__(self, name):
        self.name = name
        
    def talk(self):
        print(f"Hi, I am {self.name}")
        
person1 = Person("Ayoola")
person1.talk()


person2 = Person("Bob Smith")
person2.talk()
