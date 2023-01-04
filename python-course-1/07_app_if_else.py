weather = "hot1"  # valid values: hot, cold, rainy

if weather == "hot":
    message = "Drink plenty of water."
elif weather == "cold":
    message = "Wear warm clothes."
elif weather == "rainy":
    message = "Carry umbrellas."
else:
    weather = "lovely day"
    message = ""

print(f"It's {weather} today.. {message} Enjoy!")
