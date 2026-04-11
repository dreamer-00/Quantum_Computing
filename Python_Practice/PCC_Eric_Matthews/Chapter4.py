#TIY 4-1
pizzas=['Peppy Paneer', 'Cheese Burst', 'Margherita']
for pizza in pizzas:
    print(f"I like {pizza} pizza")
print("I really love pizza!")
#TIY 4-2
animals=['dog', 'cat', 'rabbit']
for animal in animals:
    print(f"A {animal} would make a great pet")
print("Any of these animals would make a great pet!")
#TIY 4-3
for value in range(1, 21):
    print(value)
#TIY 4-4
numbers=list(range(1, 1000001))
print(numbers)
#TIY 4-5
print(min(numbers))
print(max(numbers))
print(sum(numbers))
#TIY 4-6
odd_numbers=list(range(1, 21, 2))
for number in odd_numbers:
    print(number)
#TIY 4-7
multiples_of_three=list(range(3, 31, 3))
for number in multiples_of_three:
    print(number)
#TIY 4-8
cubes=[]
for number in range(1,11):
    print(number**3)
#TIY 4-10
pizzas=['Peppy Paneer', 'Cheese Burst', 'Margherita']
print(pizzas[0:3])
print(pizzas[0:2])
print(pizzas[-3:])
#TIY 4-11
friend_pizzas=['Peppy Paneer', 'Cheese Burst', 'Margherita']
friend_pizzas.append('Burn to hell')
pizzas.append('Burn to hell')
print(pizzas)
print(friend_pizzas)
for pizza in pizzas:
    print(f"My favourite pizzas are: {pizza}")
for pizza in friend_pizzas:
    print(f"My friend's favourite pizzas are: {pizza}")
#TIY 4-12
my_foods=['pizza', 'falafel', 'carrot cake']
friend_foods=my_foods[:]
my_foods.append('cannoli')
friend_foods.append('ice cream')
print("My favourite foods are:")
print(my_foods)
print("My friend's favourite foods are:")
print(friend_foods)
#TIY 4-13
buffet_foods=('omelette', 'boiled eggs', 'oats', 'salad')
for food in buffet_foods:
    print(food)
buffet_foods[0]='pizza'
buffet_foods=('pizza', 'boiled eggs', 'oats', 'salad')
for food in buffet_foods:
    print(food)
