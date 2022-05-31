print("Loading Car Game... Valid commands: help, start, stop, exit!")
print("*" * 60)

is_car_started = False

while True:
    car_input = input(">")
    if car_input.lower() == "start" and is_car_started:
        print("Car is already running...")
        print("     ------ ")
        print(" ---/      |        O O")
        print("|          |      0 ")
        print(" -----------= o o ")
        print("  O o   o O")
    elif car_input.lower() == "stop" and not is_car_started:
        print("Car is already stopped!")
        print("     ------ ")
        print(" ---/      |")
        print("|          |")
        print(" -----------=")
        print("  O o   o O")
    elif car_input.lower() == "start" and not is_car_started:
        print("Car started")
        print("     ------ ")
        print(" ---/      /        O O")
        print("/          /      0 ")
        print(" ---------- = o o ")
        print("  O o   o O")
        is_car_started = True
    elif car_input.lower() == "stop" and is_car_started:
        print("Car stopped")
        print("     ------ ")
        print(" ---/      \\")
        print("\\          \\")
        print(" -------------=")
        print("  O o   o O___")
        is_car_started = False
    elif car_input.lower() == "help":
        print('''
     ---------------------=
----/                     |
| start: to start the car |
| stop: to stop the car   |
| exit: to exit           |
--------------------------==
   O  o            o O
        ''')
    elif car_input.lower() == "exit":
        print("Have a great time!")
        break
    else:
        print("I do not understand that!")
    print()
