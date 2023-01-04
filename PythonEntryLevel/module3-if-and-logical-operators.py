# < less than
# > greater than
# <= less than or equal
# => greater than or equal
# == equal
# != not equal

# not: highest priority
# and
# or: lowest priority

user_age = int(input('What is your age? '))

if user_age < 17:
    print ('Get lost, you are under age for this!')
elif user_age == 17:
    print('Just wait few months!')
else: 
    user_country = input('What is your country? ')
    if user_country == 'INDIA' or user_country == 'India':
        print('Welcome to the Voting!')
    else:
        print('Get lost, you are not Indian!')
