import random



def get_number():
    return random.randrange(1,9)




def main():
    random_number = get_number()
    print(random_number)
    life = 5
    guess= 1
    while True:  
        player_guess = int(input("Guess a number between 1 and 9: "))
        if random_number == player_guess:
            print("Yeah, this is the correct number!")
            print(f"You have guessed the correct number in {guess} guesses!")
            question = input("Would you like to continue the game?(yes or no): ")
            if question == "yes":
                main()
            else:
                exit()      
        elif random_number > player_guess:
            print("Nope, this number is too low!")
            guess += 1
            life -= 1
        elif random_number < player_guess:
            print("Nope, this number is too high!")
            guess += 1
            life -= 1 
        print(f'You have {life} lifes')
        if guess > 5:
            print("No more guesses!")
            question = input("Would you like to continue the game?(yes or no): ")
            if question == "yes":
                main()
            elif question == "no":
                exit()
                

main()








    






