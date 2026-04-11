#TIY 5-1
car='bugatti chiron'
print("Is car=='bugatti chiron'? I predict True.")
print(car=='bugatti chiron')
print("Is car=='bugatti'? I predict False.")
print(car=='bugatti')
print("Is car=='Bugatti Chiron'? I predict False.")
print(car=='Bugatti Chiron')
print("Is car=='bugatti chiron'.title()? I predict True.")
print(car=='bugatti chiron'.title())
print("Is car=='bugatti chiron'.upper()? I predict False.")
print(car=='bugatti chiron'.upper())
print("Is car=='bugatti chiron'.lower()? I predict False.")
print(car=='bugatti chiron'.lower())
print("Is car=='bugatti chiron'.capitalize()? I predict False.")
print(car=='bugatti chiron'.capitalize())
#TIY 5-3
alien_color='green'
if alien_color=='green':
    print("You just earned 5 points")
elif(alien_color=='yellow'):
    print("")
#TIY 5-4
alien_color='green'
if alien_color=='green':
    print("You just earned 5 points")
elif(alien_color!='green'):
    print("You just earned 10 points")
#TIY 5-5
if(alien_color=='green'):
    print("You just earned 5 points")
elif(alien_color=='yellow'):
    print("You just earned 10 points")
else:
    print("You just earned 15 points")
#TIY 5-6
age=21
if age<2:
    print("You are a baby")
elif age>=2 and age<4:
    print("You are a toddler")
elif age>=4 and age<13:
    print("You are a kid")
elif age>=13 and age<20:
    print("You are a teenager")
elif age>=20 and age<65:
    print("You are an adult")
elif age>=65:
    print("You are an elder")
#TIY 5-7
favourite_fruits=['apple', 'bananas', 'mango', 'grapes', 'strawberries', 'watermelon']
for fruit in favourite_fruits:
    print(f"You really like {fruit}")
#TIY 5-8, 5-9 and 5-10
user_names=['vat01', 'vat02', 'vat03', 'vat04', 'vat05', 'admin']
if(len(user_names)==0):
    print("We need to find some users.")
for name in user_names:
    if name=='admin':
        print("Hello admin, would you like to see the status report")
    else:
        print(f"Hello {name}, thank you for logging in again.")
current_users=['vat01', 'vat02', 'vat03', 'vat04', 'vat05']
new_users=['vat05', 'vat04', 'vat08', 'vat09', 'vat10']
for user1 in new_users:
    for user2 in current_users:
        if user1==user2:
            print("Username in use, choose another")
        else:
            print("Username available")
#TIY 5-11
numbers = list(range(1, 10))
for num in numbers:
    if num == 1:
        print(f"{num}st")
    elif num == 2:
        print(f"{num}nd")
    elif num == 3:
        print(f"{num}rd")
    else:
        print(f"{num}th")

