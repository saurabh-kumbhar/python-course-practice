def turn_left():
    pass


def move():
    pass


def at_goal():
    pass


def wall_in_front():
    pass


def wall_on_right():
    pass


def sound(boolean):
    pass


def put():
    pass


def object_here():
    return []


#####################
def turn_around():
    turn_left()
    turn_left()


def turn_right():
    turn_around()
    turn_left()


def turn_left_move():
    turn_left()
    move()


def turn_right_move():
    turn_right()
    move()


def take():
    move()


# Center 1

count = 0
while not wall_in_front():
    count += 1
    move()

turn_around()

for i in range(int(count/2)):
    move()

put()

# Center 2

def go_to_center():
    count = 0
    while not wall_in_front():
        count += 1
        move()

    turn_around()

    for i in range(int(count/2)):
        move()

go_to_center()
turn_right()
go_to_center()
put()

