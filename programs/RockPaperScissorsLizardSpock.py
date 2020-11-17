import random
import time
def name_to_number(name):
    if name == "rock":
        number = 0
    elif name == "spock":
        number = 1
    elif name == "paper":
        number = 2
    elif name == "lizard":
        number = 3
    else:
        number = 4
    return number

#assign number to given name
def number_to_name(number):
    if number == 0:
        name = "rock"
    elif number == 1:
        name = "spock"
    elif number == 2:
        name = "paper"
    elif number == 3:
        name = "lizard"
    else:
        name = "scissors"
    return name
def rpsls():
    
    
    print("battle started",end=" ")
    for i in range(0,5):
        print("->",end="")
        time.sleep(.4)        
    print("\nchoose your choice: [rock / spock / paper / lizard / scissors]")
    player_choice=input("Enter your choice here:")
    player=name_to_number(player_choice)
    computer = random.randrange(0,5)
    
    print("you choose ",end="")
    for i in range(0,5):
        print(".",end=" ")
        time.sleep(.3)
    print(player_choice)
    
    print("computer choose ",end="")
    for i in range(0,5):
        print(".",end=" ")
        time.sleep(.3)
    print(number_to_name(computer))
    print("result is ",end="")
    for i in range(0,5):
        print(".",end=" ")
        time.sleep(.5)
        
        
    sel=(player-computer)%5
    
    if sel==2 or sel==1:
        print("congratulations: you won !!!")
    elif sel==3 or sel==4:
        print("sorry!! better luck next time : computer won")
    else:
        print("don't be upset ~~ : you tied with computer")
    
    
rpsls()  
