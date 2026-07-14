class Car:

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.orometer_reading = 0

    def get_description(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name

    def read_odometer(self):
        print("This car has "+ str(self.orometer_reading) + " miles on it")

    def update_orometer(self,miles):
        if miles >= self.orometer_reading:
            self.orometer_reading = miles
        else:
            print("You can'troll back an odometer")

    def increase(self,miles):
        self.orometer_reading +=miles

class Battery():
    #An attempt to simulate electric vehicle charging
    def __init__(self, battery_size = 70):
        #Initialize electrical frequency properties
        self.battery_size = battery_size

    def describe_battery(self):
        print("This car has a "+ str(self.battery_size) + " -kwh battery")

    def get_range(self):
        #Print a message describing the battery range
        if self.battery_size == 80:
            range_ = 260
        elif self.battery_size == 85:
            range_ = 270
        
        message = "This kind of car can go approximately " + str(range_) + " miles on a full charge"
        print(message)

class ElectricCar(Car):
    #Special features of simulated electric vehicles

    def __init__(self,make, model, year):
        super().__init__(make, model, year) #super is a special function that helps Python associate parent and child classes
        self.battery = Battery() #A new battery class is defined here