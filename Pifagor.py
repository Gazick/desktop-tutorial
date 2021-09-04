class Point:
    def set_coordinates(self, x=0, y=0):
        self.x = x
        self.y = y

    def get_distance(self, val):
        try:
            return (((val.x - self.x) ** 2 + (val.y - self.y) ** 2) ** 0.5)
        except:
            print("Передана не точка")

p1 = Point()
p2 = Point()
p1.set_coordinates(1, 2)
p2.set_coordinates(4, 6)
d = p1.get_distance(p2)
p1.get_distance(10)
