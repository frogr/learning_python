import random

correct_guess = random.randint(1, 100)
tries = 0


def main(tries, correct_guess):
    print('try counter: ', tries)
    user_input = input('guess a number: ')
    check_input(user_input, correct_guess, tries)


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


def game_won(tries):
    print()
    print('==%==%==%==%==%==%==%==%==')
    print('        YOU WIN!!! ')
    print('   IT TOOK YOU %s TRIES' % tries)
    print('==%==%==%==%==%==%==%==%==')
    print()
    exit(0)

main(tries, correct_guess)
