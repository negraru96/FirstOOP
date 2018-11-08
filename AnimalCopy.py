class Animal:
    def __init__(self, name):
        self.name = name
        self.health = 100
    def walk(self):
        self.health -= 1
        return self
    def run(self):
        self.health -= 5
        return self
    def displayhealth(self):
        print(self.health)
        return self

class Dog(Animal):
    def __init__(self, name):
        super(Dog, self).__init__(name)
        self.health = 150
    def pet(self):
        self.health += 5
        return self

class Dragon(Animal):
    def __init__(self, name):
        super(Dragon, self).__init__(name)
        self.health = 170
    def fly(self):
        self.health -= 10
        return self
    def displayhealth(self):
        super(Dragon, self).displayhealth()
        print("I am a Dragon")
        return self

# animal1 = Animal("Max")
# animal1.displayhealth()
# dog1 = Dog("Max")
# dog1.walk().run().displayhealth()
dragon1 = Dragon("Max")
dragon1.walk().run().fly().displayhealth()
