customer = {
    "name": "SPK",
    "age": "121",
    "salary": "USD 75000"
}

print(customer)

print(customer["name"])

print(customer.get("salary"))

# print(customer["birthdate"])  # Error
print(customer.get("birthdate"))  # None
print(customer.get("birthdate", "31st December 1900"))  # None

customer["name"] = "SPK"
print(customer)

print("--- Get in Words Exercise ---")

digit_words = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine",
    "10": "Ten"
}

input_number = input("Enter Number: ")
number_in_words = ""

for number in input_number:
    number_in_words += f"{digit_words.get(number, 'INVALID')} "

print(number_in_words)
