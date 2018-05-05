import random

correct_guess = random.randint(1, 100)
tries = 0


def main(tries, correct_guess):
    print('try counter: ', tries)
    user_input = input('guess a number: ')
    check_input(user_input, correct_guess, tries)


def game_won(tries):
    print()
    print('==%==%==%==%==%==%==%==%==')
    print(' YOU WIN!!! ')
    print(' IT TOOK YOU', tries, "TRIES")
    print('==%==%==%==%==%==%==%==%==')
    print()
    exit(0)


def check_input(user_input, correct_guess, tries):
    if int(user_input) > correct_guess:
        print('sorry, you guessed too high!')
        tries += 1
        main(tries, correct_guess)
    if int(user_input) < correct_guess:
        print('sorry, you guessed too low!')
        tries += 1
        main(tries, correct_guess)
    else:
        game_won(tries)


main(tries, correct_guess)
