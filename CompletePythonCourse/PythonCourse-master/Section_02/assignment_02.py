# ### DONE ###

# Assignment 2:
"""
Using some of the collection data types we learned about
in the course so such as a list and dictionary, create a
data structure that best represents the following scenario:

Tom has a salary of 20000 and is 22 years old. He owns a few items such as
a jacket, a car, and TV. Mike is another person who makes 24000 and is 27 years old
who owns a bike, a laptop and boat.
"""

# your code below:
my_collection = {
                    'Tom': {'Salary': 20000, 'Age': 22, 'Items': ['Jacket', 'car', 'TV']},
                    'Mike': {'Salary': 24000, 'Age': 27, 'Items': ['Bike', 'Laptop', 'Boat']}
                }
print(my_collection['Tom']['Salary'])

















































# Solution

# my_list = [{'Tom': {'salary': 20000, 'age': 22, 'owns': ['jacket', 'car', 'TV']}},
#            {'Mike': {'salary': 24000, 'age': 27, 'owns': ['bike', 'laptop', 'boat']}}]
