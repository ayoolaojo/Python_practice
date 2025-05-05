Command = ""
Started = False
while True:
    Command = input("> ").lower()
    if Command == "start":
        if Started:
            print(" car already started.")
        else:
            Started = True
            print("Car starts..")
            
        
            
    elif Command == 'stop':
        print(" Car stopped.")
    elif Command == "help":
        print("""
 start - to start the  car
 stop  - to stop the car
 quit  - to quit the game
 """)
    elif Command == "quit":
        break
    else:
        print(" Sorry! I don't understand what you're saying")
