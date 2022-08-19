# filter() = creates a collection of ele from iterable
#            from which a function returns true

# filter(function, iterable)

friends = [('rachel', 19), ('bob', 20), ('tom', 15), ('ross', 18)]

over18 = lambda data: (data[1] > 18)

drinkBuds = (list(filter(over18, friends)))
