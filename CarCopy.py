class Car:
    def __init__(self, price, speed, fuel, mileage, tax):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        self.tax()

    def displayall(self):
        print("Price:", self.price)
        print("Speed:", self.speed)
        print("Fuel:", self.fuel)
        print("Mileage:", self.mileage)
        print("Tax:", self.tax)
        return self

    def tax(self):
    if self.price > 10000:
        self.tax = "15%"
    else:
        self.tax = "12%"

car1 = Car(1000,"20mph","Full","35mpg")
car2 = Car(10000,"35mph","Empty","20mpg")
car3 = Car(25000,"40mph","Half Full","45mpg")
car4 = Car(2000,"20mph","Full","25mpg")
car5 = Car(5000,"25mph","Quarter Full","20mpg")
car6 = Car(200000,"60mph","Empty","15mpg")

car1.displayall()
car2.displayall()
car3.displayall()
car4.displayall()
car5.displayall()
car6.displayall()
