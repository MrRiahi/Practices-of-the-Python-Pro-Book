from collections import Counter


def get_highest_number(numbers_dict):
    """
    Find the most frequent numbers.
    :param numbers_dict:
    :return:
    """

    number = max(numbers_dict, key=lambda x: numbers_dict[x])

    return number


def get_most_frequent(numbers):
    """
    Get most frequent numbers.
    :param numbers:
    :return:
    """

    counts = Counter(numbers)
    max_number = get_highest_number(numbers_dict=counts)

    return max_number


if __name__ == '__main__':
    numbers = [1, 1, 2, 1, 4, 6, 8, 2, 76, 8, 4, 5, 10, 5]
    max_number = get_most_frequent(numbers=numbers)
    print(f'{numbers}\nThe number with highest occurrence is {max_number}')
