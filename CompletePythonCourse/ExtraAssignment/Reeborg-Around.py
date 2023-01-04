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


# Around 1
put()
while True:
    if not wall_in_front():
        move()
    else:
        turn_left()
    if len(object_here()) > 0:
        break

# Around 1 - Apple

move()
while not at_goal():
    if len(object_here()) > 0:
        take()
    if not wall_in_front():
        move()
    else:
        turn_left()

# Around 2

put()
while True:
    if wall_in_front():
        turn_left()
    elif wall_on_right():
        move()
    else:
        turn_right()
        move()
    if len(object_here()) > 0:
        break

# Around 3

put()
while True:
    if wall_in_front():
        turn_left()
        move()
    elif wall_on_right():
        move()
    else:
        turn_right()
        move()
    if len(object_here()) > 0:
        break

count = 0
while not wall_in_front():
    count += 1
    move()

turn_around()

for i in range(int(count/2)):
    move()

put()