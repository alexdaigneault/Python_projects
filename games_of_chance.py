import random
import time

money = 100

###First part: Coin game### 
def flipping_coin(guess, bet):
    coin_sides = ["null", "Heads!", "Tails!"]
    
    #Promping the player for guess and bet
    print("Heads or Tails? Press 1 for Heads, press 2 for Tails!")
    print("You guessed: ", coin_sides[int(guess)]) 
    print("You bet: $", bet)

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
#print(cho_han(2,2))

###Card battle game###
def card_battle(player1_bet, player2_bet):
    #Promping the player for it's bet
    print("Players, please enter your bet!")
    print("Player 1 bet: $", player1_bet)
    print("Player 2 bet: $", player2_bet)

    #Picking the cards
    print("Player 1, pick your card...")
    time.sleep(1)
    player1_pick = random.randint(1, 10)
    print("Player 2, pick your card...")
    time.sleep(1)
    player2_pick = random.randint(1, 10)
    print("Player 1, you picked " + str(player1_pick) + "!")
    print("Player 2, you picked " + str(player2_pick) + "!")
  
    #Deciding who won
    if player1_pick > player2_pick:
        return "Player 1, you won $" + str(player1_bet) + "!" + " Player 2, you lost $" + str((-int(player2_bet))) + "!"
    elif player2_pick > player1_pick:
        return "Player 2, you won $" + str(player2_bet) + "!" + " Player 1, you lost $" + str((-int(player1_bet))) + "!"
    else:
        return "It's a tie! Play again!"

#Calling the card battle game
print(card_battle(2, 5))
