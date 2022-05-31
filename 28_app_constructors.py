class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        print("moving")

    def draw(self):
        print("drawing")


point = Point(10, 20)
print(f"{point.x} : {point.y}")

point.move()
point.draw()
