def hello_world():
    print()
    print('==%==%==%==%==')
    print(' HELLO WORLD ! ')
    print('==%==%==%==%==')
    print()
    print('enter "exit" as your name to leave my fun game!')
    print()
    greet()


def greet():
    user_input = input('whats ya name? ')
    check_input(user_input)
    print('hello', user_input)
    hello_world()


def check_input(u_input):
    if u_input == 'exit':
        print('goodbye!')
        exit(0)


hello_world()


