# Mini-project #1 — Rock-paper-scissors-lizard-Spock
# Skanda S Bharadwaj

# Referecnce to game
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors



import random


# Fuction to convert name to number
def name_to_number(name):
    if (name == "rock"):
        return 0
    elif (name == "paper"):
        return 2
    elif (name == "scissors"):
        return 4
    elif (name == "lizard"):
        return 3
    elif (name == "Spock"):
        return 1
    else :
        return none
    

# Fuction to convert number to name
def number_to_name(number):
    if (number == 0):
        return "rock"
    elif (number == 2):
        return "paper"
    elif (number == 4):
        return "scissors"
    elif (number == 3):
        return "lizard"
    elif (number == 1):
        return "Spock"
    else :
        return none
    
    
# Function to implement the RPSLS game
def rpsls(player_choice): 
    
    # Player's choice
    print "Player chooses",player_choice
    player_choice_number = name_to_number(player_choice)
    
    # Computer's choice
    computer_choice_number = random.randrange(0,5)
    computer_choice_name = number_to_name(computer_choice_number)
    print "Computer chooses",computer_choice_name
    
    # Differnce between the two taken modulo 5
    differnce_between_choices = (computer_choice_number - player_choice_number) % 5
   
    # Decide winner
    if (differnce_between_choices == 0 ):
        print "Player and computer tie!"
    elif (differnce_between_choices <= 2 ):
        print "Computer wins!"
    else : 
        print "Player wins!"
        
    print
    
    
# Test cases
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

#Cheers
