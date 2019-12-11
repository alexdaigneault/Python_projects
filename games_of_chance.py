import random
import time

money = 100

###First part: Coin game### 
def flipping_coin(guess, bet):
    coin_sides = ["null", "Heads!", "Tails!"]
    
    #Promping the player for guess and bet
    print("Heads or Tails? Press 1 for Heads, press 2 for Tails!")
    print("You guessed: ", coin_sides[int(guess)]) 
    print("You betted: $", bet)

    #Flipping the coin 
    print("Flipping the coin...")
    time.sleep(1)
    coin_flip = random.randint(1, 2)
    print(coin_sides[coin_flip])
  
    #Win or lose
    if coin_sides[int(guess)] == coin_sides[int(coin_flip)]:
        return "You won $" + str(bet) + "!"
    else:
        return "You lost $" + str((-int(bet))) + "!"

#Calling the Coin game function
#first_trial = flipping_coin(1, 20)
#print(first_trial)

###Second part: Cho-Han game###
def cho_han(guess, bet):
    choices = ["null", "Odd", "Even"]
    
    #Promping the player for guess and bet
    print("Odd or even? Press 1 for odd, press 2 for even.")
    print("You guessed: ", choices[int(guess)]) 
    print("You betted: $", bet)   
    
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
        #print("It's an even number!")
        return "It's " + answer + "!"
    else:
        answer = choices[1]
        #print("It's an odd number!")
        return "It's " + answer + "!"
    
    #Win or lose TO BE FIXED
    if choices[guess] == answer:
        return "You won $" + str(bet) + "!"
    else:
        return "You lost $" + str((-int(bet))) + "!"
   
    
#Calling the Cho-Han game function
print(cho_han(2,2))
