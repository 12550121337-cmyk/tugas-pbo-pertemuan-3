class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0   

    def describe_restaurant(self):
        print(f"{self.restaurant_name} is a restaurant that serves {self.cuisine_type} food")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open now!")

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, additional):
        self.number_served += additional


restaurant = Restaurant('Ramen', 'Japanese')

print(f"The restaurant name is, {restaurant.restaurant_name}.")
print(f"This restaurant provides, {restaurant.cuisine_type} food.")
restaurant.describe_restaurant()
restaurant.open_restaurant()

print(f"Customers served: {restaurant.number_served}")

restaurant.number_served = 40
print(f"Updated customers served: {restaurant.number_served}")

restaurant.set_number_served(70)
print(f"Customers after set_number_served: {restaurant.number_served}")

restaurant.increment_number_served(20)
print(f"Customers after increment: {restaurant.number_served}")
print()
