"""# TIY 7-1
car=input("Which kind of car you want to rent?\n")
print(f"Lets check if I can find you a {car}")
#TIY 7-2
people=int(input("How many people are in the dinner group\n"))
if people>8:
    print("You have to wait for the table")
else:
    print("Table is ready!")
#TIY 7-3
num=int(input("Enter the number here: "))
if num%10==0:
    print(f"{num} is a multiple of 10!")
else:
    print(f"{num} is not a multiple of 10!")

#TIY 7-4
topping=""
while topping!="quit":
    topping=input("Enter the topping:\n")
    if topping!="quit":
        print(f"{topping} added to pizza!")
#TIY 7-5
message=""
cost=0
while message!="quit":
    age=int(input("Enter the user's age"))
    if age<3:
        cost+=0
    elif age>3 and age<12:
        cost+=10
    elif age>12:
        cost+=15
    message=input("Do you want to add another person?(yes\quit)")
print(cost)
#TIY 7-7

while true:
    print("")
"""
#TIY 7-8
sandwich_orders=['egg sandwich', 'chicken sandwich', 'veg sandwich', 'mayo sandwich']
finished_orders=[]
while sandwich_orders:
    current_order=sandwich_orders.pop();
    print(f"I made your {current_order} sandwich")
    finished_orders.append(current_order)
print("\nThe following orders have been completed:")
for sandwich in finished_orders:
    print(sandwich.title())
#TIY 7-9
sandwich_orders=['egg sandwich', 'chicken sandwich', 'veg sandwich', 'mayo sandwich', 'pastrami', 'pastrami', 'pastrami']
print("Deli has run out of pastrami!")
finished_orders=[]
while sandwich_orders:
    current_order=sandwich_orders.pop();
    if current_order!='pastrami':
        print(f"I made your {current_order} sandwich")
        finished_orders.append(current_order)
print("\nThe following orders have been completed:")
for sandwich in finished_orders:
    print(sandwich.title())
#TIY 7-10
responses={}
status=True;
while status:
    name=input("Enter your name: ")
    response=input("What is your dream vacation place? ")
    responses[name]=response
    repeat=input("Would you like to let another person respond (yes/no) ?")
    if repeat=='no':
        status=False;
print("\n----Poll Results----")
for name, response in responses.items():
        print(f"{name}'s dream vacation place is {response}.")
