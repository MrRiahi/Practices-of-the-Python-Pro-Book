from datetime import datetime


class Greeter:

    def __init__(self, name):
        self.name = name

    @staticmethod
    def _day():
        """
        Get the current day.
        :return:
        """

        return datetime.now().strftime('%A')

    @staticmethod
    def _get_part_of_day():
        """
        Get part of the day. 'morning', 'afternoon', and 'evening'.
        :return:
        """

        hour = datetime.now().hour

        if hour < 12:
            day_state = 'morning'

        elif 12 <= hour < 17:
            day_state = 'afternoon'

        else:
            day_state = 'evening'

        return day_state

    def greet(self, store):
        """
        Greet.
        :param store:
        :return:
        """

        print(f'Hi, my name is {self.name}, and welcome to {store}!\n'
              f'How\'s your {self._day()} {self._get_part_of_day()} going?\n'
              f'Here\'s a coupon for 20% off!')


if __name__ == '__main__':
    greeter = Greeter(name='Mohammadreza')
    greeter.greet(store='Amazon')
