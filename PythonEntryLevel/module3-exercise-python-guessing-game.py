# Ask the user to guess the year when Python 1.0 was released (the correct answer is 1994) with the following prompt:
#
# When was Python 1.0 released? << remember to add a space at the end of this prompt
#
# If the user answers 1994, show:
#
# Correct!
#
# and finish the program. If the user answers with a year later than 1994, show a hint and ask again for a new year on a new line:
#
# It was earlier than that!
# When was Python 1.0 released? << remember to add a space
#
# If the user answers with a year earlier than 1994, show a hint and ask again for a new year on a new line:
#
# It was later than that!
# When was Python 1.0 released? << remember to add a space

release_year = 1994

while True:
    input_year = int(input('When was Python 1.0 released? '))
    if release_year == input_year:
        print('Correct!')
        break
    elif release_year > input_year:
        print('It was later than that!')
    else:
        print('It was earlier than that!')
