class Square:
    def __init__(self, length)->None:
        self.length = length

        if self.length < 0:
            raise ValueError("Length has to be positive and greater than zero")

        if type(self.length) not in [float,int]:
            raise TypeError('Length must be an integer or float')

    def area(self):
        return self.length * self.length