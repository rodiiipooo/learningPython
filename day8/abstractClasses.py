#Prevent user from creating an object of that class
#abstract method prevents users from creating objects of the class
#class varName(ABC):

from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        print('the engine of your vehicle is now on')

    @abstractmethod
    def stop(self):
        print('you stop the vehicle')

    def run(self):
        print('the vehicle is moving')

class Motorcycle(Vehicle):
    def start(self):
        print('the engine of your motorcycle is now on')
    def stop(self):
        print('your harley has come to a halt')

class Car(Vehicle):
    def start(self):
        print('the engine of your car is now on')

    def stop(self):
        print('your car has come to a halt')


motorcycle = Motorcycle()
car = Car()

car.run()
motorcycle.run()