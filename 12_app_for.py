list = [False, 10, "PSK","SPK"] # list can be collection of different types of elements
for item in list:
    print(item)

item = list[0] + 10 # False is 0, True is 1
print(item)
print("*" * 20)
print("Odds")
for item in range(1,10,2):
    print(item)
print("Evens")
for item in range(2,10,2):
    print(item)


print("*" * 20)
print("total cost")
prices = [10, 24, 53, 46, 312, 123]
total = 0

for price in prices:
    total += price

print(f"Total cart bill: {total}")