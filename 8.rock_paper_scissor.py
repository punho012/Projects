import random

print('''
#############################################################################
This is a rock, paper, scissor game!!! Can you beat the machine? Good luck!!!
You have to win three rounds to win the game!!!
##############################################################################
''')




def play():
    player_point = 0
    machine_point = 0
    while True:
        if machine_point == 3:
            print("Game over, The winner is: MACHINE")
            question = input("Would you like to play one more game: ")
            if question == "yes":
                play()
            elif question ==  "no":
                exit()
            
        if player_point == 3:
            print("Game over, The winner is: Player")
        
            question = input("Would you like to play one more game: ")
            if question == "yes":
                play()
            elif question ==  "no":
                exit()

        opponent= ["rock", "paper", "scissor"]
        rnd = random.choice(opponent)
        player = input("What is your choice (rock, paper or scissor)?: ")          
        if player == "rock" and rnd == "paper":
            print("Sorry, you lost!!!")
            machine_point += 1
            continue

        elif player == "rock" and rnd == "rock":
            print("It is a draw!!!")
            continue

        elif player == "rock" and rnd == "scissor":
            print("Congrats, you won!!!")
            player_point += 1
            continue

        elif player == "paper" and rnd == "paper":
            print("It is a draw!!!")
            continue

        elif player == "paper" and rnd == "rock":
            print("Congrats, you won!!!")
            player_point += 1
            continue

        elif player == "paper" and rnd == "scissor":
            print("Sorry, you lost!!!")
            machine_point += 1
            continue

        elif player == "scissor" and rnd == "paper":
            print("Congrats, you won!")
            player_point += 1
            continue

        elif player == "scissor" and rnd == "rock":
            print("Sorry, you lost!!!")
            machine_point += 1
            continue

        elif player == "scissor" and rnd == "scissor":
            print("It is a draw!!!")
            continue
        
      
play()

