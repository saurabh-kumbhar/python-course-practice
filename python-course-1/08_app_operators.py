# Logical and / or / not operators
is_high_income = True
is_good_credit = True
is_criminal = True

if is_high_income and is_good_credit and not is_criminal:
    message = "Eligible for Loan."
else:
    message = "Eligible for Jail."

print(f"{message}")

# Comparison operators
print("-" * 10)
temperature = 28

if temperature > 28:
    message = "It's a hot day"
elif temperature == 28:
    message = "It's warm day"
elif 28 > temperature > 20:
    message = "It's a great day"
elif temperature < 20:
    message = "It's a cold day"
else:
    message = "Invalid temperature value"

print(f"{message}!")

print("-" * 10)
name = "SPK"

if len(name) < 3:
    message = "Name must be at least 3 characters"
elif len(name) > 20:
    message = "Name can be maximum of 20 characters"
else:
    message = "Name looks good"

print(f"{name}: {message}!")
