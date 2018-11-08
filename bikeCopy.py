class Bike:
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0

    def displayinfo(self):
        print(self.price, self.max_speed, self.miles)
        return self
    def ride(self):
        self.miles += 10
        print("Riding", self.miles)
        return self
    def reverse(self):
        self.miles -= 5
        print("Reversing", self.miles)
        return self

bike1 = Bike(100,"16mph");
bike2 = Bike(150,"20mph");
bike3 = Bike(200,"25mph");

bike1.displayinfo().ride().reverse()
bike2.displayinfo().ride().reverse()
bike3.displayinfo().ride().reverse()
