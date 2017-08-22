class Numbers(object):
    def __init__(self, number):
        self.number = number

    def __mul__(self, other):
        return self.number + other.number

num_1 = Numbers(5)
num_2 = Numbers(2)
print num_1 * num_2