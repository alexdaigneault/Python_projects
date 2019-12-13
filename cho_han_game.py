import random
import time

###Cho-Han game###
def cho_han():
    choices = ["null", "Odd", "Even"]
    
    #Prompting the player for his guess and bet
    print("Odd or even? Press 1 for odd, press 2 for even.")
    guess = input("Enter your choice: ")
    print("You guessed: ", choices[int(guess)])  
    bet = input("Enter your bet: ")
    print("You bet: $", bet)
    
    #Rolling the dice
    print("Rolling the dice...")
    time.sleep(1)
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    time.sleep(1)
    result = dice1 + dice2
    print("The total is %d. " % result)
    
    #Check if the sum of the dice if odd or even
    if (result % 2) == 0:
        answer = choices[2]
        print("It's an even number!")
    else:
        answer = choices[1]
        print("It's an odd number!")
    
    #Win or lose 
    if choices[int(guess)] == answer:
        return "You won $" + str(bet) + "!"
    else:
        return "You lost $" + str((-int(bet))) + "!"
   
    
#Calling the Cho-Han game function
print(cho_han())