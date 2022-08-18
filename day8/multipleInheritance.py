class Prey:
    def flee(self):
        print('this animal flees')

class Predator:
    def hunt(self):
        print('this animal hunts')

class Rabbit(Prey):
    pass
class Hawk(Predator):
    pass
class Fish(Prey, Predator):
    pass