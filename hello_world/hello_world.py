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
    if user_input == 'exit':
        print('goodbye!')
        exit(0)
    print('hello', user_input)
    hello_world()


hello_world()


