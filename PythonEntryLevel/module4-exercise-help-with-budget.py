# John has a hard time keeping his budget. Write a program to help him analyse his spendings. You are given a list with John's spendings for each month. Go through the list, and count the number of times...
#
# a. the spendings were low (< 1000.0)
# b. the spendings were normal (between 1000.0 and 2500.0 inclusive)
# c. the spendings were high (> 2500.0)
#
# Then, print the following to the output:
#
# Numbers of months with low spendings: {}, normal spendings: {}, high spendings: {}.
#
# Hint: Note where the space characters are in the message you are supposed to print. For example, after the low spendings amount, there immediately comes a comma (without a space). If you just use the default print() settings, you may end up with too many space characters. Luckily, you know the sep='' keyword argument of print() now... :)

spendings = [1346.0, 987.50, 1734.40, 2567.0, 3271.45, 2500.0, 2130.0, 2510.30, 2987.34, 3120.50, 4069.78, 1000.0]

low_count = 0
normal_count = 0
high_count = 0

for spending in spendings:
    if spending < 1000.00:
        low_count += 1
    elif spending > 2500.00:
        high_count += 1
    else:
        normal_count += 1

print('Numbers of months with low spendings: ', low_count, ', normal spendings: ', normal_count, ', high spendings: ', high_count, '.', sep='')
