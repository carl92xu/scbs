class Car:
    def __init__(self, registration, make):
        self.registration = registration
        self.make = make
        self.milage = 0
        self.dayofinspection = ""

    def get_registration(self):
        return self.registration

    def get_make(self):
        return self.make

    def get_mileage(self):
        return self.milage

    def get_dayofinspection(self):
        return self.dayofinspection

    def set_data(self, mileage, dayofinspection):
        self.milage = mileage
        self.dayofinspection = dayofinspection


mycar = Car("ABC123", "BMW")
mycar.set_data(1234, "12/4/2016")
print(mycar.get_dayofinspection())
