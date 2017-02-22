'''
Create a class called  Car. In the__init__(), allow the user to specify the following attributes: price, speed, fuel, mileage. If the price is greater than 10,000, set the tax to be 15%. Otherwise, set the tax to be 12%.

Create six different instances of the class Car. In the class have a method called display_all() that returns all the information about the car as a string. In your __init__(), call this display_all() method to display information about the car once the attributes have been defined.
'''

class Car(object):
    def __init__(self, price, speed, fuel, mileage):
        print "Created new car!"
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if self.price > 10000:
            self.price = int(self.price * .15) + self.price
            self.tax = 0.15
        else:
            self.price = int(self.price * .12) + self.price
            self.tax = 0.12


    def display_all(self):
        print "Price: ${}, Speed: {}MPH, Fuel: {}, Mileage: {}, Tax: {} (Included in Price).".format(self.price, self.speed, self.fuel, self.mileage, self.tax)

car1 = Car(1000, 65, 17, 130000)
car1.display_all()

car2 = Car(11000, 75, 30, 5)
car2.display_all()

car3 = Car(60000, 85, 21, 600)
car3.display_all()

car4 = Car(75000, 65, 35, 25000)
car4.display_all()

car5 = Car(5000, 65, 20, 13000)
car5.display_all()

car6 = Car(50000, 76, 37, 1000)
car6.display_all()
