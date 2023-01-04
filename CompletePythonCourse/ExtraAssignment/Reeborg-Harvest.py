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


def u_turn_right():
    turn_right()
    move()
    turn_right()


def u_turn_left():
    turn_left()
    move()
    turn_left()


def harvest_row():
    while not wall_in_front():
        while len(object_here()) > 0:
            take()
        move()


def fix_one_row(length):
    while True:
        length -= 1
        count = len(object_here())
        if count > 0:
            while len(object_here()) > 0:
                take()
        else:
            put()
        if length == 0:
            return
        move()


# Harvest 1 and 2


move()
move()
turn_left()
for i in range(6):
    harvest_row()
    if i % 2 == 0:
        u_turn_right()
    else:
        u_turn_left()


# Harvest 3

def fix_one_row(length):
    while True:
        length -= 1
        while len(object_here()) > 0:
            take()
        put()
        if length == 0:
            return
        move()


move()
move()
turn_left()
move()
move()
right = True
for i in range(3,9):
    fix_one_row(6)
    if right:
        u_turn_right()
        right = False
    else:
        u_turn_left()
        right = True
