class Computer(object):
    def __init__(self):
        self. processor
        self. ram
        self.memory

    def get_spec(self, processor, ram, memory):
        self.processor = processor
        self.ram = ram
        self.memory = memory

    def display_spec(self):
        print "Processor: {0} ram: {1} memory {2}".format(self.processor, self.ram, self.memory)


class Desktop(Computer):
    def __init__(self, color):
        self.case_holder = color

    def display_spec(self):
        print "Desktop case color {0}".format(self.case_holder)


class Laptop(Computer):
    def __init__(self, size):
        self.size = size

    def display_spec(self):
        super(Laptop, self).display_spec()
        print "Laptop size {0}".format(self.size)

l = Laptop("red")
l.get_spec(1, 2, 3)
l.display_spec()
