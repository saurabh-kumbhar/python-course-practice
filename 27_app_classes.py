class Point:
    def move(self):
        print("moving")

    def draw(self):
        print("drawing")


point = Point()
point.move()  # function calls
point.draw()

point.x = 10  # Can be added on the go, only applicable for point.
# If not defined print will throw Attribute Errors
point.y = 20
print(f"{point.x} : {point.y}")

