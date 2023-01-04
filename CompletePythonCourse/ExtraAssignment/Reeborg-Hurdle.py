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


def move_twice():
    move()
    move()


def move_four_times():
    move_twice()
    move_twice()


def move_eight_time():
    move_four_times()
    move_four_times()

# Hurdle 1 and 2
while not at_goal():
    move()
    turn_left_move()
    turn_right_move()
    turn_right_move()
    turn_left()

# Hurdle 3

while not at_goal():
    if wall_in_front():
        turn_left_move()
        turn_right_move()
        turn_right_move()
        turn_left()
    else:
        move()

# Hurdle 4
while not at_goal():
    if wall_in_front():
        turn_left_move()
    else:
        move()
        continue
    while wall_on_right():
        move()
    turn_right_move()
    turn_right_move()
    while not wall_in_front():
        move()
    turn_left()