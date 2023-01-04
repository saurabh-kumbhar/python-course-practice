# from machines.vehicle_stuff import vehicle, car, bike
from animals.animal_stuff import monkey, bird

# nexon = vehicle('Compact SUV', 'Tata', 'Nexon', 'DarkEdition')
# safari = vehicle('SUV', 'Tata', 'Safari', 'Red')
# altroz = vehicle('Hatchback', 'Tata', 'Altroz', 'White')
#
# print(nexon.vehicle_body)
# print(nexon.vehicle_make)
# print(nexon.vehicle_model)
# print(nexon.vehicle_color)
# altroz.number_of_wheels = 5  # changing for altroz object only
# # vehicle.number_of_wheels = 5  # changing for Class including all the object. can be done, not recommended
# print(altroz.number_of_wheels)
# print(nexon.number_of_wheels)
#
# nexon.vehicle_engine = '3 Cylinder'  # can be done, not recommended
# print(nexon.vehicle_engine)
#
# print('Number of vehicle created (nexon object):', nexon.get_vehicle_counter())
# print('Number of vehicle created (safari object):', safari.get_vehicle_counter())

# nexon = car('Compact SUV', 'Tata', 'Nexon', 'DarkEdition')
# safari = car('SUV', 'Tata', 'Safari', 'Red')
# altroz = car('Hatchback', 'Tata', 'Altroz', 'White')
# print(nexon.vehicle_body)
# print(nexon.vehicle_make)
# print(nexon.vehicle_model)
# print(nexon.vehicle_color)
# print(nexon.wheelcount())
# print(nexon.drive())
# print(vehicle.vehiclecount(nexon))
#
# fz = bike('Sports', 'Yamaha', 'FZs', 'Black')
#
# for vehicle in [nexon, safari, fz]:
#     print(vehicle.vehicle_model, 'from', vehicle.vehicle_make, 'is of type', vehicle.vehicle_body)

# abstract class
makad = monkey('makadya')
makad.eat()
makad.move()

print('---')
chimani = bird('chimanya')
chimani.eat()
chimani.move()
