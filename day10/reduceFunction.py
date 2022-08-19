# reduce() = applies function of choosing to single cum value
#            performs function on first two ele and repeats until 1 value remains

# reduce(funciton, iterable)
import functools

#letters = ('H', 'E', 'L', 'L', 'O')
#word = functools.reduce(lambda x, y: x + y, letters)
#print(word)


def factorial(num):
    factorial = []
    i = 1
    while i < num + 1:
        factorial.append(i)
        i += 1

    result = functools.reduce(lambda x, y: x * y, factorial)
    print(result)


factorial(5)