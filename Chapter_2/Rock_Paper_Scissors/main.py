import random


OPTIONS = ['rock', 'paper', 'scissors']


def print_options():
    print('(1) Rock\n(2) Paper\n(3) Scissors')


def get_human_choice():
    human_choice_number = input('Enter the number of your choice: ')
    human_choice_action = OPTIONS[int(human_choice_number)]
    print(f'Your choice is {human_choice_action}')
    return human_choice_action


def get_computer_choice():
    computer_choice = random.choice(OPTIONS)
    print(f'Computer choice is {computer_choice}')


def get_result(human_choice, computer_choice):
    if human_choice == 'rock':
        if computer_choice == 'paper':
            print('Sorry, paper beat rock')
        elif computer_choice == 'scissors':
            print('Yes, rock beat scissors!')
        else:
            print('Draw!')

    elif human_choice == 'paper':
        if computer_choice == 'scissors':
            print('Sorry, scissors beat paper')
        elif computer_choice == 'rock':
            print('Yes, paper beat rock!')
        else:
            print('Draw!')

    elif human_choice == 'scissors':
        if computer_choice == 'rock':
            print('Sorry, rock beat scissors')
        elif computer_choice == 'paper':
            print('Yes, scissors beat paper!')
        else:
            print('Draw!')


if __name__ == '__manin__':
    print_options()
    get_human_choice()
    get_computer_choice()
