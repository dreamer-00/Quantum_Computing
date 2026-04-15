#TIY 9-1
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
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
        self.number_served=0
    def describe_restaurant(self):
        print(f"The restaurant name is {self.restaurant_name}")
        print(f"The cuisine type is {self.cuisine_type}")
    def open_restaurant(self):
        print("The restaurant is open")
    def set_number_served(self, number):
        self.number_served=number
    def increment_number_served(self, increment):
        self.number_served+=increment
my_restaurant=Restaurant('dominos', 'margerita')
print(f"My favorite restaurant is {my_restaurant.restaurant_name}")
print(f"My favorite cuisine is {my_restaurant.cuisine_type}")
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
my_restaurant.set_number_served(50)
print(f"Customers served : {my_restaurant.number_served}")
my_restaurant.increment_number_served(120)
print(f"Customers served after increment : {my_restaurant.number_served}")
#TIY 9-5
class user:
    def __init__(self, first_name, last_name, age, ethinicity):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
        self.ethinicity=ethinicity
        self.login_attempts=0
    def describe_user(self):
        print(f"The user's name is {self.first_name} {self.last_name} of age {self.age} and ethinicity {self.ethinicity}")
    def greet_user(self):
        print(f"Hello {self.first_name} {self.last_name}, you are welcome here!")
    def increment_login_attempts(self):
        self.login_attempts+=1
    def reset_login_attempts(self):
        self.login_attempts=0
person1=user('larry', 'ellison', 81, 'american')
person1.describe_user()
person1.greet_user()
person1.increment_login_attempts()
person1.increment_login_attempts()
person1.increment_login_attempts()
print(f"Total login attempts of {person1.last_name} is {person1.login_attempts}")
person1.reset_login_attempts()
print(f"Reset login attempts of {person1.last_name} is {person1.login_attempts}")
#TIY 9-6
class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors=[]
    def displayflavors(self):
        print("Available IceCream Flavors: ")
        for flavor in self.flavors:
            print(f"-{flavor}")
ice_cream_shop=IceCreamStand("ZZCool Scoops", "Ice Cream")
ice_cream_shop.flavors=["Vanilla", "Chocolate", "Strawberry", "Mango"]
ice_cream_shop.displayflavors()
#TIY 9-7
class Admin(user):
    def __init__(self, first_name, last_name, age, ethinicity):
        super().__init__(first_name, last_name, age, ethinicity)
        self.privileges=[]
    def show_privileges(self):
        print("Available Privileges: ")
        for privilege in self.privileges:
            print(f"-{privilege}")
admin1=Admin("Peter", "Theil", 50, "American")
admin1.privileges=["Can delete post", "Can add post", "Can ban user"]
admin1.describe_user()
admin1.show_privileges()     
#TIY 9-8
class Privileges:
    def __init__(self):
        self.privileges=[]
    def show_privileges(self):
        print("Available Privileges: ")
        for privilege in self.privileges:
            print(f"-{privilege}")
class Admin(user):
    def __init__(self, first_name, last_name, age, ethinicity):
        super().__init__(first_name, last_name, age, ethinicity)
        self.privileges=Privileges()
admin1 = Admin("Peter", "Thiel", 50, "American")
admin1.privileges.privileges=["Can delete post", "Can add post", "Can ban user"]
admin1.describe_user()
admin1.privileges.show_privileges()
#TIY 9-9
class Car:
    def __init__(self, make, model, year):
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading=0
    def get_descriptive_name(self):
        long_name=f"{self.year} {self.make} {self.model}"
        return long_name.title()
    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")
    def update_odometer(self, mileage):
        if mileage>=self.odometer_reading:
            self.odometer_reading=mileage
        else:
            print("You can't roll back your odometer!")
    def increment_odometer(self, miles):
        self.odometer_readings+=miles
class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery=Battery()
    def fill_gas_tank(self):
        print("This car doesn't have a gas tank you fool!")
class Battery:
    def __init__(self, battery_size=40):
        self.battery_size=battery_size
    def describe_battery(self):
        print(f"This car has a {self.battery_size}-Kwh battery")
    def get_range(self):
        if self.battery_size==40:
            range=150
        elif self.battery_size==65:
            range=225
        print(f"This car can go about {range} miles on a full charge")
    def upgrade_battery(self):
        if self.battery_size!=65:
            self.battery_size=65
my_leaf=ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())
my_leaf.battery.describe_battery()
print("Range without upgrading the battery:--")
my_leaf.battery.get_range()
my_leaf.battery.upgrade_battery()
print("Range after upgrading the battery:--")
my_leaf.battery.get_range()
#TIY 9-13
import random
class Die:
    def __init__(self, sides=6):
        self.sides=sides
    def roll_die(self):
        result=random.randint(1, self.sides)
        print(result)
print("Rolling the 6-sided die:")
die6=Die()
for _ in range(10):
    die6.roll_die()
print("\nRolling 10-sided die:")
die10=Die(10)
for _ in range(10):
    die10.roll_die()
print("\nRolling 20-sided die:")
die20=Die(20)
for _ in range(10):
    die10.roll_die()
#TIY 9-14
list1=[1,2,3,4,5,6,7,8,9,10, 'A', 'B', 'C', 'D', 'E']
winning_ticket=random.sample(list1, 4)
print(f"Winning ticket: {winning_ticket}")
print("Any ticket matching these 4 numbers/letters wins a prize!")
#TIY 9-15
my_ticket=[1, 'A', 5, 'C']
attempts=0
won=False
while not won:
    attempts+=1
    winning_ticket=random.sample(list1, 4)
    if set(my_ticket)==set(winning_ticket):
        won=True
print(f"You won after {attempts} attempts!")
print(f"Winning ticket: {winning_ticket}")


    

