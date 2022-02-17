import random


OPTIONS = ['rock', 'paper', 'scissors']


def print_options():
    """
    This function prints game's options
    :return:
    """

    print('(1) Rock\n(2) Paper\n(3) Scissors')


def get_human_choice():
    """
    This function gets the choice of the human
    :return:
    """

    human_choice_number = input('Enter the number of your choice: ')
    human_choice_action = OPTIONS[int(human_choice_number) - 1]
    print(f'Your choice is {human_choice_action}')

    return human_choice_action


def get_computer_choice():
    """
    This function gets the computer choice using a random number.
    :return:
    """

    computer_choice = random.choice(OPTIONS)
    print(f'Computer choice is {computer_choice}')

    return computer_choice


def print_win_lose_message(human_choice, computer_choice, human_beats, human_loses_to):
    """
    This function prints the win or lose message.
    :param human_choice:
    :param computer_choice:
    :param human_beats:
    :param human_loses_to:
    :return:
    """

    if computer_choice == human_beats:
        print(f'Yes, {human_choice} beats {computer_choice}')
    elif computer_choice == human_loses_to:
        print(f'Ops, {human_choice} loses to {computer_choice}')


def print_result(human_choice, computer_choice):
    """
    This function prints the result of the game.
    :param human_choice:
    :param computer_choice:
    :return:
    """

    if human_choice == computer_choice:
        print('Drawn, Please try again!')

    elif human_choice == 'rock':
        print_win_lose_message(human_choice=human_choice, computer_choice=computer_choice,
                               human_beats='scissors', human_loses_to='paper')
    elif human_choice == 'scissors':
        print_win_lose_message(human_choice=human_choice, computer_choice=computer_choice,
                               human_beats='paper', human_loses_to='rock')
    elif human_choice == 'paper':
        print_win_lose_message(human_choice=human_choice, computer_choice=computer_choice,
                               human_beats='rock', human_loses_to='scissors')


if __name__ == '__main__':
    print_options()

    human_choice = get_human_choice()
    computer_choice = get_computer_choice()

    print_result(human_choice=human_choice, computer_choice=computer_choice)
