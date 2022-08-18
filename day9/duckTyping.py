#concept whre class of object is less inportmat than objects/attri butes


class Duck:

    def walk(self):
        print('this duck is walking')
    def talk(self):
        print('this duck is quacking')

class Chicken:

    def walk(self):
        print('this chicken is walking')
    def talk(self):
        print('this chicken is quacking')


class Person():

    def catch(self, Chicken):
        duck.walk()
        duck.talk()
        print('you caught the critter')

duck = Duck()
chicken = Chicken()
person = Person()

person.catch(duck)

