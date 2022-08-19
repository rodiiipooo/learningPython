# dictionary comprehension = create dictionaries using an expression
#                            can replace for loops and certain lambda functions

# dicitonary = {key: expression for (key,value) in interable}
# dicitonary = {key: expression for (key,value) in interable if conditional}
# dicitonary = {key: (if/else) for (key,value) in interable}
# dicitonary = {key: function(value) for (key,value) in interable}

citiesF = {'new york': 32, 'boston': 75, 'los angeles': 100, 'chicago': 50}

#citiesC = {
#    key: round((value - 32) * (5 / 9)) for (key, value) in citiesF.items()}

#print(citiesC)

#citiesF = {
#    'new york': 'sunny',
#    'boston': 'sunny',
##    'chicago': 'snowing'}

#sunnyCits = {key: value for (key, value) in citiesF.items() if value == 'sunny'}

#print(sunnyCits)


def checkTemp(value):
    if value >= 70:
        return 'hot'
    elif 69 >= value >= 40:
        return 'warm'
    else:
        return 'cold'


descWeather = {key: checkTemp(value) for (key, value) in citiesF.items()}

print(descWeather)