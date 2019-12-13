import random
import time

###Card battle game###
def card_battle():
    #Promping the player for it's bet
    player1_bet = input("Player 1, place your bet: ")
    player2_bet = input("Player 2, place your bet: ")
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
print(card_battle())
      