
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def drive(self):
        print('this '+self.model+' is driving')
    def stop(self):
        print('this '+self.model+' is stopped')
