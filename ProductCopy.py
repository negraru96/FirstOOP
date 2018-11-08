class Product:
    def __init__(self, price, itemname, weight, brand, tax):
        self.price = price
        self.itemname = itemname
        self.weight = weight
        self.brand = brand
        self.status = "For Sale"
        self.tax = tax

    def sell(self):
        self.status = "sold"
        # print(self.status)
        return self

    def addtax(self, tax):
        self.price = self.price * self.tax
        print(self.price)
        return self

    def returnitem(self, reason_for_return):
        if reason_for_return == "defective":
            self.status = "defective"
            self.price = 0
            print(self.status)
            print(self.price)
        else:
            if reason_for_return == "like_new":
                self.status = "for sale"
                print(self.status)
            if reason_for_return == "opened":
                self.status = "used"
                self.price = (self.price * 0.2)
                print(self.status)
                print(self.price)

    def displayinfo(self):
      # print(self.price)
      print(self.itemname)
      print(self.weight)
      print(self.brand)
      # print(self.status)
      return self

product1 = Product(34, "soda", "34 lbs", "coca-cola", 2)
product1.displayinfo()
product1.sell()
product1.addtax(2)
product1.returnitem("like_new")
