#Module file for Restauraunt
class Restauraunt:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"{self.restaurant_name} {self.cuisine_type}")

    def open_restaurant(self):
        print("The restauraunt is open for business")

    def set_number_served(self, num):
        self.number_served = num

    def increment_number_served(self, num):
        self.number_served += num

class IceCreamStand(Restauraunt):

    def __init__(self, restauraunt_name, cuisine_type, flavours):
        self.restaurant_name = restauraunt_name
        self.cuisine_type = cuisine_type
        self.flavours = flavours

    def showFlavours(self):
         print(self.flavours)
