
def square_generator(items):
    for item in items:
        yield item ** 2


# The square_generator is a simple generator to return the squared number.
# There are two ways to use this generator.

# First approach
items = list(range(10000))
my_generator_1 = square_generator(items=items)
print(f'The first output of the my_generator_1 is {next(my_generator_1)}')

# Second approach
# This approach is more efficient in time and memory usage.
my_generator_2 = square_generator(items=range(10000))
print(f'The first output of the my_generator_2 is {next(my_generator_2)}')
