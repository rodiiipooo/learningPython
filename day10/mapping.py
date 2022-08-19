# map() = applies a function to each item in an iterable (list, tuple, etc)

# map(function, iterable)

store = [('jeans', 20.00), ('tshirt', 15.00), ('bag', 50.00)]

toEuros = lambda data: (data[0], round(data[1] * 0.82, 2))
toDollars = lambda data: (data[0], round(data[1] / 0.82, 2))

storeEuros = list(map(toEuros, store))
storeDollars = list(map(toDollars, store))

for i in storeDollars:
    print(i)
