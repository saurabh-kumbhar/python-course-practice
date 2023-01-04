# factorial 5! = 5 X 4 X 3 X 2 X 1

# loop

def fact_loop(num):
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i;
    return factorial


# recursion
def fact(num):
    if num == 1:
        return num
    else:
        return num * fact(num-1)


print(fact(4))
print(fact_loop(4))


# generator (similar to iterator)
def get_number():
    for i in range(1,4):
        yield i


print(get_number())
generator = get_number();
print(next(generator))
print(next(generator))
print(next(generator))
print('---')
for x in get_number():
    print(x)
print('---')
numbers = list(get_number())
print(numbers)
