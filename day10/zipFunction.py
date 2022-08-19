#zip(*iterables) = aggregate elements from two or more iterables
#                  zip object with paired elements stored in tuples for each element

from collections import UserString

usernames = ['dude', 'bro', 'mister']
passwords = ('password', 'abc123', '123cheese')
logindate = ['1/1/1', '2/2/2', '3/3/3']

users = zip(usernames, passwords, logindate)

for i in users:
    print(i)
