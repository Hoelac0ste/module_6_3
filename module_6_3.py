class Horse:
    x_distance = 0
    sound = 'Frrr'

    def run(self, dx):
        self.x_distance += dx


class Eagle:
    y_distance = 0
    sound = 'I train, eat, sleep, and repeat'

    def fly(self, dy):
        self.y_distance += dy

class Pegasus(Horse, Eagle):

    def run(self, dx):
            super().run(dx)

    def fly(self, dy):
            super().fly(dy)

    def move(self, dx, dy):
        super().run(dx)
        super().fly(dy)

    def get_pos(self):
        pos = (self.x_distance, self.y_distance)
        return pos

    def voice(self):
        return super().sound

p1 = Pegasus()
p1.fly(3)
print(p1.y_distance)

p1.move(2, 3)
print(p1.x_distance, p1.y_distance)

print(p1.get_pos())
print(p1.voice())