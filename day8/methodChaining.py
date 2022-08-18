#used to call multiple methods sequentially


class Car:

    def turn_on(self):
        print('the engine is on')
        return self
    def drive(self):
        print('the car is moving')
        return self
    def brake(self):
        print('the car is braking')
        return self
    def turn_off(self):
        print('the engine is off')
        return self

car = Car()

#car.turn_on().drive()
car.turn_on()\
    .drive()\
    .brake()\
    .turn_off()


