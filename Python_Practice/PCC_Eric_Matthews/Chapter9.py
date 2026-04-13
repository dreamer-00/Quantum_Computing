class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
    def describe_restaurant(self):
        print(f"The restaurant name is {self.restaurant_name}")
        print(f"The cuisine type is {self.cuisine_type}")
    def open_restaurant(self):
        print("The restaurant is open")
my_restaurant=Restaurant('dominos', 'margerita')
print(f"My favorite restaurant is {my_restaurant.restaurant_name}")
print(f"My favorite cuisine is {my_restaurant.cuisine_type}")
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
#TIY 9-2
my_restaurant2=Restaurant('hocco', 'chole bhature')
my_restaurant3=Restaurant('lapinoz', 'cheeseBurst')
my_restaurant2.describe_restaurant()
my_restaurant3.describe_restaurant()
#TIY 9-3
class user:
    def __init__(self, first_name, last_name, age, ethinicity):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
        self.ethinicity=ethinicity
    def describe_user(self):
        print(f"The user's name is {self.first_name} {self.last_name} of age {self.age} and ethinicity {self.ethinicity}")
    def greet_user(self):
        print(f"Hello {self.first_name} {self.last_name}, you are welcome here!")
person1=user('larry', 'ellison', 81, 'american')
person1.describe_user()
person1.greet_user()
#TIY 9-4
