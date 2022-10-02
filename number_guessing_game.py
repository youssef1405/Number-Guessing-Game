import random


LOWER = 1
UPPER = 10

random_number = random.randint(LOWER, UPPER)

print('****************************************')
print('Welcome to the Number Guessing Game :)')
print('****************************************\n\n')



while True:
    user_guess = int(input('Please guess a number between 1 and 10: '))

    if user_guess == random_number:
        print('You Won! Congratulations')
        break
    elif user_guess > UPPER or user_guess < LOWER:
        print(f'Your guess is outside the range. Enter a number between {LOWER} and {UPPER}')
    elif user_guess < random_number:
        print('Your guess is lower than the right answer')
    else:
        print('Your guess is higher than the right answer')
