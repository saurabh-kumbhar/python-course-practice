i = 0

print("Start...")
while i < 5:
    i += 1
    print("*" * i)
print("Done!!!")

guess_limit = 3
guess_count = 0
secret_number = 9
while guess_limit > guess_count:
    guess_limit -= 1
    guess = int(input("Guess number (1-9): "))
    if guess == secret_number:
        print("You Won!")
        break
    print(f"Remaining Attempts: {guess_limit}")
else:
    print("You Lost!")
