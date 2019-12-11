import random
import time

###Coin game###
def flipping_coin():
    coin_sides = ["null", "Heads!", "Tails!"]

    #Prompting the player for his guess and bet
    print("Heads or Tails? Press 1 for Heads, press 2 for Tails!")
    guess = input("Enter your choice: ")
    print("You guessed: ", coin_sides[int(guess)]) 
    bet = input("Enter your bet: ")
    print("You betted: $", bet)

    #Flipping the coin 
    print("Flipping the coin...")
    time.sleep(1)
    coin_flip = random.randint(1, 2)
    print(coin_sides[coin_flip])
  
    #Win or lose
    if coin_sides[int(guess)] == coin_sides[int(coin_flip)]:
        return "You won $" + bet + "!"
    else:
        return "You lost $" + str((-int(bet))) + "!"

#Calling the Coin game function
print(flipping_coin())


