#functions that either accpet function as arg or return function,
#functions are also treated as objects


#accepting function as argument

def loud(text):
    return text.upper()

def quiet(text):
    return text.lower()

def hello(func):
    text = func('hello')
    print(text)


#---
hello(loud)



def divisor(x):
    def dividend(y):
        return y / x
    return dividend

divide = divisor(2)

print(divide(10))