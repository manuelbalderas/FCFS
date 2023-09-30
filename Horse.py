class Horse:
    def __init__(self, name, position_x, position_y, distance, time):
        self.name = name
        self.position_x = position_x
        self.position_y = position_y
        self.velocity = distance / time
        self.has_arrived = False

    def move(self):
        if not self.has_arrived:
            self.position_x += self.velocity

    def stop(self):
        self.has_arrived = True

    def __str__(self):
        return f'My name is {self.name}, im currently at ({self.position_x}, {self.position_y}) and my velocity is {self.velocity}'