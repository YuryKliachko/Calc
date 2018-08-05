import math
class Calc():

    def sum(self, num_1=0, num_2=0):
        return (num_1 + num_2)

    def substraction(self, num_1, num_2):
        return (num_1 - num_2)

    def multiplication(self, num_1, num_2):
        return (num_1 * num_2)

    def devision(self, num_1, num_2):
        if num_2 != 0:
            return (num_1 / num_2)
        else:
            return None

    def square(self, num_1):
        return num_1*num_1

    def square_root(self, num_1):
        return math.sqrt(num_1)


