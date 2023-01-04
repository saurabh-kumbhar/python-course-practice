# help(print)

# print(type(print))


def greet_person(name='Buddy'):
    """
    This returns greeting with provided name

      name:
        Name of person
    """
    return 'Hello, ' + name + '!'


def get_remainder(num1, num2):
    """
        This returns remainder. num1 % num2.

          num1:
            Dividend
          num2
            Divisor
    """
    return num1 % num2


def my_sum(*args):
    """
            This returns summation of given numbers

              args:
                more than 1 numerical values
        """
    sum = 0

    for i in args:
        sum += i

    return sum


def convert_weight(**kwargs):
    unit = kwargs['unit']
    weight = kwargs['weight']
    if unit == 'lbs':
        return weight * 2.205
    if unit == 'kgs':
        return weight / 2.205

9
print(greet_person('SPK'))
print(get_remainder(14, 5))
print(my_sum(10, 24, 35, 46, 765, 78, 23, 462, 13))
print(convert_weight(unit='kgs', weight=102))
