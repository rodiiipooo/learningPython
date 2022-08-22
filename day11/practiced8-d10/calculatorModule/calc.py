# here we go

class settings():
    pass


class Rectangle():
    def __init__(self, length, width):
        self.length = length
        self.width = width


class Square(Rectangle):
    def __init__(self, length, width):
        super().__init__(length, width)

    def area(self):
        return self.length*self.width


square = Square()
square.area(2, 2)
