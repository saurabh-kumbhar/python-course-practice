# ### DONE ###

# Assignment 2:
"""
    create a function called separate() that accepts a string as an argument
    and returns a list containing each of the characters of
    the string separated as individual items in the list.

    Make sure to test the function.
"""
# Your Code Below:


def separate_manual(string):
    list_str = []
    for ch in string:
        list_str.append(ch)
    return list_str


def separate(string):
    return list(string)


print(separate("Saurabh"))










































# Solution Below:

# def separate(str):
#     return list(str)
#
# print(separate("hello there"))