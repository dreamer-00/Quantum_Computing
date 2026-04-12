#TIY 6-1
person1={'first_name': 'larry', 'last_name': 'ellison', 'age': 65, 'city': 'san-fransisco'}
print(person1['first_name'])
print(person1['last_name'])
print(person1['age'])
print(person1['city'])
#TIY 6-2
favorite_numbers={'larry':1, 'elon': 2, 'pavel': 3, 'peter': 4, 'steve': 5}
for name, number in favorite_numbers.items():
    print(f"The favorite number of {name.title()} is {number}")
#TIY 6-3 and 6-4
glossary={'print': 'function used for output', 'comment':'statements that are not executed just written for reading purposes', 'variables': 'defined for storing values', 'functions':'block of code that does a specific task', 'lists':'collections of unordered items'}
for key, value in glossary.items():
    print(f"{key.title()} \n{value}")
#TIY 6-5
rivers={'Egypt':'Nile', 'India':'Ganga', 'North-America': 'Mississippi', 'South-America':'Parana', 'Europe':'Danube'}
for key, value in rivers.items():
    print(f"{value} runs through {key}")
for key, value in rivers.items():
    print(key, value)
#TIY 6-6
favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'rust',
'phil': 'python',
}
listofpeople=['jen', 'edward', 'mark', 'peter', 'tom']
for people in listofpeople:
    if people in favorite_languages:
        print(f"Thank you {people} for taking the poll.")
    else:
        print(f"{people}, kindly take the poll.")
#TIY 6-7
person1={'first_name':'vatsal', 'last_name':'pathak', 'age':21}
person2={'first_name':'larry', 'last_name':'ellison', 'age':60}
person3={'first_name':'elon', 'last_name':'musk', 'age':53}
people=[person1, person2, person3]
for person in people:
    print('\nPerson Details:')
    for key, value in person.items():
        print(f"{key}:{value}")
#TIY 6-8
pet1 = {'animal': 'dog', 'owner': 'vatsal'}
pet2 = {'animal': 'cat', 'owner': 'sarah'}
pet3 = {'animal': 'rabbit', 'owner': 'john'}
pets = [pet1, pet2, pet3]
for pet in pets:
    print(f"\nPet Details:")
    for key, value in pet.items():
        print(f"{key}:{value}")
#TIY 6-9
favorite_places = {
    'vatsal': ['san-francisco', 'geneva', 'singapore'],
    'elon': ['mars'],
    'mark': ['hawaii', 'paris']
}
for name, places in favorite_places.items():
    print(f"\n{name}'s favorite places:")
    for place in places:
        print(f"-{place}")
#TIY 6-10
favorite_numbers = {
    'vatsal': [7, 11, 21],
    'elon': [42],
    'mark': [3, 9]
}
for name, numbers in favorite_numbers.items():
    print(f"\n{name}'s favorite numbers:")
    for num in numbers:
        print(num)
#TIY 6-11
cities = {
    'mumbai': {
        'country': 'india',
        'population': '20 million',
        'fact': 'financial capital of India'
    },
    'tokyo': {
        'country': 'japan',
        'population': '37 million',
        'fact': 'largest metropolitan area'
    },
    'paris': {
        'country': 'france',
        'population': '2 million',
        'fact': 'city of lights'
    }
}
for city,info in cities.items():
    print(f"\nCity: {city}")
    for key, value in info.items():
        print(f"{key}:{value}")
#TIY 6-12
favorite_places = {
    'vatsal': ['san-francisco', 'geneva', 'singapore'],
    'elon': ['mars'],
    'mark': ['hawaii', 'paris']
}
for name, places in favorite_places.items():
    print(f"\n{name.title()}'s Favorite Places:")
    print(", ".join(place.title() for place in places))

    



    