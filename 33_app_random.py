import random

for i in range(5):
    print(random.random())
    print(random.randint(1, 10))

members = ["A", "B", "C", "D"]
print(random.choice(members))
