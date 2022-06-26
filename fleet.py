from robot import Robot

class Fleet:
    def __init__(self):
        self.robots = []

    def create_fleet(self):
        self.robots.append(Robot('Optimus Prime'))
        self.robots.append(Robot('Machina'))
        self.robots.append(Robot('Screwie'))