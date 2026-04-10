#TIY 3-1
names=['vatsal', 'ellison', 'durov', 'musk']
print(names[0])
print(names[1])
print(names[2])
print(names[3])
#TIY 3-2
print(f"Hello {names[0]}, How are you?")
print(f"Hello {names[1]}, How are you?")
print(f"Hello {names[2]}, How are you?")
print(f"Hello {names[3]}, How are you?")
#TIY 3-3
transportation=['Ducati', 'Bugatti Chrion', 'Pagani', 'G650']
print(f"I would like to own a {transportation[0]}")
print(f"I would like to own a {transportation[1]}")
print(f"I would like to own a {transportation[2]}")
print(f"I would like to own a {transportation[3]}")
#TIY 3-4
names=['vatsal', 'ellison', 'durov', 'musk']
print(f"Dear {names[0]}, I would like to invite you to a dinner party at my house. Please let me know if you can make it.")
print(f"Dear {names[1]}, I would like to invite you to a dinner party at my house. Please let me know if you can make it.")
print(f"Dear {names[2]}, I would like to invite you to a dinner party at my house. Please let me know if you can make it.")
print(f"Dear {names[3]}, I would like to invite you to a dinner party at my house. Please let me know if you can make it.")
print(f"Dear {names[1]}, couldn't make it to the dinner party.")
#TIY 3-5
names.remove('ellison')
for name in names:
    print(f"Dear {name}, I would like to invite you to a dinner party at my house. Please let me know if you can make it.")
#TIY 3-6
for name in names:
    print(f"Dear {name}, I would like to invite you to a dinner party at my house. Please let me know if you can make it.")
names.insert(0, 'ellison')
names.insert(2, 'peter theil')
names.append('jensen huang')
for name in names:
    print(f"Dear {name}, I would like to invite you to a dinner party at my house. Please let me know if you can make it.")
#TIY 3-7
print("Sorry, can only invite two people to the dinner party.")
while(len(names) > 2):
    name=names.pop()
    print(f"Sorry {name}, I can't invite you to the dinner party.")
for name in names:
    print(f"Dear {name}, you are still invited to the dinner party.")
del names[0]
del names[0]
print(names)
#TIY 3-8
locations=['Switzerland', 'San Francisco', 'New York', 'London', 'Paris']
print(locations)
print(sorted(locations))
print(locations)
print(reversed(locations))
print(locations)
locations.reverse()
print(locations)
locations.sort()
print(locations)
locations.sort(reverse=True)
print(locations)
#TIY 3-9
n=len(names)
print(n)