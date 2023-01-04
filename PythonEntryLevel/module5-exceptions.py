# try:
#     value = int(input('Enter an integer: '))
#     print('The inverse of', value, 'is', 1/value)
# except ValueError:
#     print('Invalid input, expected number!')
# except ZeroDivisionError:
#     print('Invalid operation, not expected zero!')
# except:
#     print('Something went wrong!')


# function propogation
# def get_day(birthday):
# 	day = int(input('Enter day of the birthday: '))
# 	birthday.append(day)


# def get_month(birthday):
# 	month = int(input('Enter month of the birthday: '))
# 	birthday.append(month)


# def get_year(birthday):
# 	year = int(input('Enter year of the birthday: '))
# 	birthday.append(year)


# def get_birthday():
# 	try:
# 		birthday = []
# 		get_day(birthday)
# 		get_month(birthday)
# 		get_year(birthday)
# 		return birthday
# 	except ValueError:
# 		return 'Invalid input, expected integer value!'


# print(get_birthday())

# assertions
def cal_inverse(num):
	assert (num != 0), 'Zero not allowed!'
	return 1/num

cal_inverse(int(input('Enter number (not zero): ')))
