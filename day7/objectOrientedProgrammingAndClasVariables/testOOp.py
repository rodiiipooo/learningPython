from OOP import Car

car1 = Car('maserati','ghibly',2017)
car2 = Car('bentley','mulsanne',2015)

carNum = car2

print(carNum.make)
print(carNum.model)
print(carNum.year)

carNum.drive()
carNum.stop()


