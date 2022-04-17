import random


def sort_expensive():
    my_list = random.sample(range(1_000_000), 1_000)
    my_list.sort()


def sort_cheap():
    my_list = random.sample(range(1_000), 10)
    my_list.sort()


if __name__ == '__main__':
    sort_expensive()
    for i in range(1000):
        sort_cheap()
