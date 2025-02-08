class Vehicle:
    def move(self):
        """Base method to be overridden"""
        pass

class Car(Vehicle):
    def move(self):
        print("🚗 Driving on the road!")

class Plane(Vehicle):
    def move(self):
        print("✈️ Flying in the sky!")

class Boat(Vehicle):
    def move(self):
        print("🚢 Sailing on the water!")

# Creating different vehicle objects
vehicles = [Car(), Plane(), Boat()]

# Calling move() for each vehicle (polymorphism in action!)
for v in vehicles:
    v.move()
