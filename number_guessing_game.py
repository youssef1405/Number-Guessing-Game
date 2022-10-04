import random

# range between 1 and 10
LOWER = 1
UPPER = 10
# number of attempts user tries to guess the correct number
attempts = 0

random_number = random.randint(LOWER, UPPER)

print('****************************************')
print('Welcome to the Number Guessing Game :)')
print('****************************************\n\n')


while True:
    try:
        user_guess = int(input('Please guess a number between 1 and 10: '))
        # check if user guess out of range
        if user_guess > UPPER or user_guess < LOWER:
            raise ValueError(f'Your guess is outside the range. Enter a number between {LOWER} and {UPPER}')
    except ValueError as err:
        print(err)
    else:
        attempts += 1
        if user_guess == random_number:
            print('You Won! Congratulations')
            print(f'You guessed the correct number after {attempts} attempts')
            play_again = input('Would you like to play again? y/n: ')
            if (play_again.lower() == 'y'):
                random_number = random.randint(LOWER, UPPER)
                attempts = 0
                continue
            else: 
                break
        elif user_guess < random_number:
            print('Your guess is lower than the right answer')
        else:
            print('Your guess is higher than the right answer')

print('Thank you for trying the game :)')