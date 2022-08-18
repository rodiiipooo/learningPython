class Car:

    color = None

class Motorcycle:

    color = None

def changeColor(vehicle, color):

    vehicle.color = color

car1 = Car()
car2 = Car()
car3 = Car()

bike1 = Motorcycle()
bike2 = Motorcycle()
bike3 = Motorcycle()

changeColor(bike1,'red')
changeColor(bike2,'white')
changeColor(bike3,'blue')

print(bike2.color)
print(bike1.color)
print(bike3.color)