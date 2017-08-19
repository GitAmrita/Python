class car:
    def __init__(self):
        self.speed = 0
        self.odometer = 0
        self.time = 0

    def say_state(self):
        print ("i am going {} kph!".format(self.speed))

    def accelerate(self):
        self.speed += 5

    def brake(self):
        self.speed -= 5

    def step(self):
        self.odometer += self.speed
        self.time += 1

    def average_speed(self):
        if self.time == 0:
            return 0
        else:
            return self.odometer /self.time

if __name__ == '__main__':
    my_car = car()
    print ("I'm a car")
    while True:
        action = raw_input("What should I do? [A]ccelerate, [B]rake, "
                       "show [O]dometer, or show average [S]peed?").upper()
        if action not in 'ABOS' or len(action) != 1:
            print ('I do not know how to do that')
            continue
        if action == 'A':
            my_car.accelerate()
        elif action == 'B':
            my_car.brake()
        elif action == 'O':
            print ('The car has driven {} kilometers'.format(my_car.odometer))
        elif action == 'S':
            print ('The cars average speed was {} kilometers'.format(my_car.speed))
        my_car.step()
        my_car.say_state()

