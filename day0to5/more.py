#sets ,,, unordered, unindexed, no duplicate valeus
#utensils = {"fork", "knife","spoon"}
#utensils.add("napkin")
#utensils.remove("fork")
#untensils.clear()

#dishes = {"bowl", "plate", "cup" }
#dishes.update(utensils)
#dinnerTable = utensils.union(dishes)
#varA.difference(varB) ,, returns what sets do not share
#varA.intersection(varB) ,, retursn what sets share

#for x in dinnerTable:
 #   print(x)

#print(len(dinnerTable))

#......................................................


#dictionary = a changable unorderded collection of unique key value pairs
# use hashing and allow access to values quick

capitals = {'USA': 'Washinton DC',
            'India': 'new Delhi',
            'China': 'Bejing',
            'Russia': 'moscow'}
capitals.update({'germany': 'Berlin'})

print(capitals.get('germany'))
print(capitals.keys())
print(capitals.values())
print(capitals.items())

for key, value in capitals.items():
    print(key, value)


#.....................index operators

name = "rodrigo Celis-Duran"
    name = name.upper()
print(name)

firstName = (name[:7].lower()).capitalize()
lastName = (name[8:].lower()).capitalize()
print(firstName+" "+lastName)

#......................functions

#function is a block of code executed only when called

def profit(revenue,cost):

profit(1000,500)


#............return statement in functions
#send py values/objects back to the caller,, known as funcitons retunr value


def mult(num1,num2):
      return num1 * num2

x = mult(2,2)
print(x)


#....................keyword arguments
#keyword arguments = preceded by an identifier when we pass then to a function,
# position in function argument does not matter so long as name id precedes user input
# when function is called.

#example:

def hello(first,last,age):
    print("Hello "+first+" "+last+"! ")
    print("you are "+str(age)+" years old!")
hello("Rodrigo","Celis",21)

#in the above function, result is returned in a desirable order
#however, when input is swapped, returns error due to python identifying each
#input as its respective variable in the hello() function
#-----proof-----
def hello(first,last,age):
    print("Hello "+first+" "+last+"! ")
    print("you are "+str(age)+" years old!")
hello("Celos",21,"Rodrigo")

#use of keyword arguments example ::

def hello(first,last,age):
    print("Hello "+first+" "+last+"! ")
    print("you are "+str(age)+" years old!")
hello(age=21,last="Celis",first="Rodrigo")

#as you can see, despite hello() input being rearranged and not in same order
#as in hello() function, the result is the same as if it were. This is due to
#the keyword arguments directly assigning input value to the required variables in the
#hello() function.



#...............nested function calls.............
# already  know




#............variable scope......
# region that vaariable is recognized
name = "bro" #gloval scope, available inside and outside of function

def dispName():
    name = "code"  #local scope(name) only available in this one function
    print(name)
dispName()
print(name)

#........args parameter ,,, will pack all arguments into a tuple.
#.......tuple is unordered and unchangable
#..tuple example:::
student = ('rodrigo', 20, 'male')
print(student.count('rodrigo'))
print(student.index('male'))

#for x in student:
 #   print(x)


#args continued::::
#useful so a function accepts a varying amount of argumetns
#....below, function does not work due to excess arguments in the
#....call functoin
def add(num1,num2):
    sum = num1+num2
    return sum
print(add(1,2,3))


#....asterisc is most important
def add(*args):
    sum = 0
    for i in args:
        sum += i
    return sum
print(add(1,2,3))

def avg(*nums):
    sum = 0
    for i in nums:
        sum += i
    return(sum / len(list(nums)))

print(avg(2,2,2,2,2,2,2,2,2,2,2,2,2))

#.......**kwargs = parameter that will pack all arguments into a dictionary
#....... useful so a fucntion can accept varying amount of keyword arguments
# positional vs keyword arguments

def hello(first,last):
    print("hello "+first+" "+last+"!")
hello(last='Celis', first='Rodrigo')

def hello(**kwargs):
    print("hello "+kwargs['first']+" "+kwargs['last']+"!")
    print('Hello ', end="")
        print(value, end=" ")
hello(first='Rodrigo', second='Celis', last='Duran')

#..... format method str.format() optional method that gives
#..... users control when diplsaying output
#example::
animal = 'cow'
item = 'moon'
print('the {} jumped over the {}'.format(animal,item))
keyword identifiers can be used in format method
text = "the {} jumped over the {}"
print(text.format(animal,item))

text1 = "hello my name is {:^10} nice to meet you" #adding padding
name = "rod"
print(text1.format(name))

format method can also be used on numbers

import random as ran

x = ran.randint(1,6)
print(x)

y = ran.random()
print(y)

myList = ['rock', 'paper','scissors']
z = ran.choice(myList)
print(z)

#......exception = events detected during execution that
#...... interrupts flow of program

try:
    numerator = int(input('insert your numerator: '))
   result = numerator / denominator
except ZeroDivisionError:
    print('cant divide by 0 here')
except ValueError:
    print('only text pls')
  print('smth went south sorry')
finally:
    print('this always executes')


#...........file detection using python......
#check if file is somewhere in computer
import os

path =
if os.path.exists(path):
    print('this location exists!')
    if os.path.isfile(path):
        print('that is a file')
    elif os.path.isdir(path):
        print('that is a directory!')
else:
    print('that location does not exist')





