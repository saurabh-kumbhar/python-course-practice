print("------ positional and keyword parameters")


def addition(number, root):
    return number ^ root


print(addition(10, root=2))
# print(addition(number=10, 2))  # positional after keyword not allowed

