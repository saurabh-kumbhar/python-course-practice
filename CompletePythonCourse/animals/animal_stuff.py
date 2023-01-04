class animal:

    def __init__(self, name):
        self.name = name

    def eat(self):
        raise NotImplementedError('Child class should be implementing this method')


    def move(self):
        raise NotImplementedError('Child class should be implementing this method')


class monkey(animal):

    def eat(self):
        print('eating banana...')

    def move(self):
        print('jumping...')

class bird(animal):

    def eat(self):
        print('eating worms')

    def move(self):
        print('flying...')