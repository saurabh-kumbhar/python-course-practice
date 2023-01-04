# DELETE
# cities = ['Pune', 'Mumbai', 'Nagpur', 'Nashik', 'Kolhapur']
# print(cities)
# # del cities[2]
# # del cities[3:]
# # del cities[:]
# # del cities
# print(cities)

# ADD
# booking_ratings = [8, 8, 9, 7, 9]
# print(booking_ratings)
# booking_ratings.append(7)
# print(booking_ratings)
# booking_ratings.insert(1, 10)
# print(booking_ratings)

# TRAVERSE
# cities = ['Pune', 'Mumbai', 'Nagpur', 'Nashik', 'Kolhapur']
# # for city in cities:
# #     print(cities.index(city), ':', city)
#
# for index in range(len(cities)):
#     print(index, ':', cities[index])

spendings = [90.50, 45, 35.50, 67.50, 12]
total = 0.0
for spending in spendings:
    total += spending
print('Total: ', total)
