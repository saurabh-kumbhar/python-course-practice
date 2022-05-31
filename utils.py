# weight converters
def lbs_to_kg(weight):
    return weight / 2.205


def kg_to_lbs(weight):
    return weight * 2.205


# find max number
def find_max(numbers):
    max_number = numbers[0]
    for number in numbers:
        if number > max_number:
            max_number = number
    return max_number

