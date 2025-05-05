secretNumber = 7
attempts = 0
while attempts < 3:
    guess = int( input("Guess the secret number: ") )
    attempts += 1
    if guess == secretNumber:
        print(f"Awesome, {secretNumber} is correct")
        break
else:
     print("Wrong! You've exhausted your attempts")
    
       

        
    