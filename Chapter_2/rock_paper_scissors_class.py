import random


class RockPaperScissorsSimulator:
    def __init__(self):
        self.options = ['rock', 'paper', 'scissors']
        self.computer_choice = None
        self.human_choice = None

    @staticmethod
    def print_options():
        """
        This method prints game's options
        :return:
        """

        print('(1) Rock\n(2) Paper\n(3) Scissors')

    def get_human_choice(self):
        """
        This method gets the choice of the human
        :return:
        """

        human_choice_number = input('Enter the number of your choice: ')
        self.human_choice = self.options[int(human_choice_number) - 1]
        print(f'Your choice is {self.human_choice}')

    def get_computer_choice(self):
        """
        This method gets the computer choice using a random number.
        :return:
        """

        self.computer_choice = random.choice(self.options)
        print(f'Computer choice is {self.computer_choice}')

    def print_win_lose_message(self, human_beats, human_loses_to):
        """
        This method prints the win or lose message.
        :param human_beats:
        :param human_loses_to:
        :return:
        """

        if self.computer_choice == human_beats:
            print(f'Yes, {self.human_choice} beats {self.computer_choice}')
        elif self.computer_choice == human_loses_to:
            print(f'Ops, {self.human_choice} loses to {self.computer_choice}')

    def print_result(self):
        """
        This function prints the result of the game.
        :return:
        """

        if self.human_choice == self.computer_choice:
            print('Drawn, Please try again!')

        elif self.human_choice == 'rock':
            self.print_win_lose_message(human_beats='scissors', human_loses_to='paper')

        elif self.human_choice == 'scissors':
            self.print_win_lose_message(human_beats='paper', human_loses_to='rock')

        elif self.human_choice == 'paper':
            self.print_win_lose_message(human_beats='rock', human_loses_to='scissors')

    def simulate(self):
        """
        This method runs the rock, paper and scissors game
        :return:
        """

        self.print_options()

        self.get_human_choice()
        self.get_computer_choice()

        self.print_result()


if __name__ == '__main__':
    RPS = RockPaperScissorsSimulator()
    RPS.simulate()
