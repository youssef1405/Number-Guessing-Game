import random

# range between 1 and 10
LOWER = 1
UPPER = 10

# number of attempts user tries to guess the correct number
attempts = 0

# the least # of tries (initial)
best_score = 10000

# initial random number
random_number = random.randint(LOWER, UPPER)

# greeting to the user
print('****************************************')
print('Welcome to the Number Guessing Game :)')
print('****************************************\n')

# game loop
while True:
    try:
        user_guess = int(input('Please guess a number between 1 and 10: '))
        
        # check if user guess out of range
        if user_guess > UPPER or user_guess < LOWER:
            raise ValueError()
    except ValueError:
        print(':(')
        print('Invalid number. Please guess a number between 1 and 10:')
    else:
        # count number of valid attemtps 
        attempts += 1
        if user_guess == random_number:
            print('You Won! Congratulations')
            print(f'You guessed the correct number after {attempts} attempts')
            play_again = input('Would you like to play again? y/n: ')

            # user chooses to play again
            if (play_again.lower() == 'y'):
                # calculate user best score per game
                if attempts < best_score:
                    best_score = attempts
                    print(f'New best score: {best_score}')
                else:
                    print(f'your current best score: {best_score}')
                
                # generate new random # if user wants to play again
                random_number = random.randint(LOWER, UPPER)
                # reset # of attempts
                attempts = 0
                continue
            # user does not want to play again
            else: 
                break
        elif user_guess < random_number:
            print('Your guess is lower than the right answer')
        else:
            print('Your guess is higher than the right answer')

print('Thank you for trying the game :)')