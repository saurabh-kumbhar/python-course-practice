class vehicle:
    # class attribute, should not be changed outside class specification
    vehicle_counter = 0

    def __init__(self, body_type, make, model, color):
        self.vehicle_body = body_type  # object attribute
        self.vehicle_make = make  # object attribute
        self.vehicle_color = color  # object attribute
        self.vehicle_model = model  # object attribute
        vehicle.vehicle_counter += 1

    def __str__(self):
        return self.vehicle_model + \
            ' from ' + self.vehicle_make + \
            ' is of type ' + self.vehicle_body + \
            ' with popular color ' + self.vehicle_color

    def __len__(self):
        return 4

    def vehiclecount(self):
        return vehicle.vehicle_counter

    def wheelcount(self):
        return 'Could be 8 or 6 or 4 or 2';

    def drive(self):
        print('Driving vehicle...')


class car(vehicle):

    def wheelcount(self):
        return 4;

    def drive(self):
        print('Driving car...')


class bike(vehicle):

    def wheelcount(self):
        return 2;

    def drive(self):
        print('Driving bike...')

