# list comprehension = create a new list with less syntax
#                      can mimick certain lambda functions, easier to read
#
#   list = [exoression for item in iterable]

squares = []
for i in range(1, 11):
    squares.append(i * i)
print(squares)

squarez = [i * i for i in range(1, 11)]
print(squarez)
