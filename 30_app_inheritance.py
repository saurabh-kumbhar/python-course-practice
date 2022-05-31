class Animal:
    def walk(self):
        print("walking")


class Dog(Animal):
    def bark(self):
        print("barking")
    # pass  # Can't have empty class. Pass will work


class Cat(Animal):
    def meow(self):
        print("meowing")


Dog().walk()
Dog().bark()
Cat().walk()
Cat().meow()