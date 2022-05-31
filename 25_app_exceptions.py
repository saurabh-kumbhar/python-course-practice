print("Program started...")

try:
    age = int(input("Age: "))
    income = int(input("income: "))
    risk = income / age
    print(age)
except ValueError:
    print("Invalid integer value.")
except ZeroDivisionError:
    print("Age cannot be 0.")

print("Program ended gracefully!")
