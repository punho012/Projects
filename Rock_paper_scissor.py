import random

print('''
##############################################################################################################
This is a rock, paper, scissor game against a machine called "Robocop"!!! Can you beat "Robocop"? Good luck!!!
You have to win three rounds to win the game!!!
###############################################################################################################
''')



def player_win():
    opponent_point = 0
    player_point = 0
    while True:
        if opponent_point == 3:
            print("Game over, Robocop won the game!!!")
            question = input("Would you like to play one more game: ")
            if question == "yes":
                player_win()
            elif question ==  "no":
                exit()

        elif player_point == 3:
            print("Game over, You won the game!!!")
        
            question = input("Would you like to play one more game: ")
            if question == "yes":
                player_win()
            elif question ==  "no":
                exit()
        opponent= ["rock", "paper", "scissor"]
        rnd = random.choice(opponent)
        player = input("What is your choice (rock, paper or scissor)?: ") 
        if player == "rock" and rnd == "scissor" or player == "paper" and rnd == "rock" or player == "scissor" and rnd == "paper":
            player_point += 1
            print(f"Robocop's choice was:{rnd}")
            print("You are the winner")
            print(f"Robocop - You: {opponent_point} - {player_point}")
            continue
        elif player == rnd:
            print(f"Robocop's choice was:{rnd}")
            print("It is a draw")
            print(f"Robocop - You: {opponent_point} - {player_point}")
            continue
        else:
            opponent_point += 1
            print(f"Robocop's choice was:{rnd}")
            print("Robocop is the winner")
            print(f"Robocop - You: {opponent_point} - {player_point}")
            continue

player_win()


