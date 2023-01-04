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

#