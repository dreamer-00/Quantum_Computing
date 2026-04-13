""" #TIY 8-1
def display_message():
    print("Hii! I am learning python")
display_message()
#TIY 8-2
def favorite_book():
    title=input("Enter the title: ")
    print(f"One of my favorite books is {title}")
favorite_book()
#TIY 8-3
def make_shirt(size, text):
    print(f"The size of shirt is {size} and the text printed on it is {text}")
make_shirt(40, "I am a Man")
make_shirt(size=40, text="I am a Man")
#TIY 8-4
def make_shirt(size="L", text="I love python"):
    print(f"The size of shirt is {size} and the text printed on it is {text}")
make_shirt()
make_shirt(size="M")
make_shirt(size="M", text="I love You")
#TIY 8-5
def describe_city(city, country="India"):
    print(f"{city.title()} is in {country.title()}")
describe_city("agra")
describe_city(city="san-francisco", country="USA")
describe_city(city="Delhi")
#TIY 8-6
def city_country(city, country):
    str1= f"{city.title()}, {country.title()}"
    return str1
str=city_country("santiago", "chile")
print(str)
str=city_country("delhi", "india")
print(str)
str=city_country("los angeles", "usa")
print(str)
str=city_country("dubai", "uae")
print(str)
#TIY 8-7
def make_album(artist, album, songs=None):
    dict1={'Artist':artist, 'Album':album,}
    if songs:
        dict1['Songs']=songs
    return dict1
print(make_album("weekend", "starboy", "starboy"))
print(make_album("weekend", "Timeless"))
print(make_album("weekend", "Cry for Me"))
#TIY 8-8
status=True
while status:
    artist=input("Enter the artist: ")
    album=input("Enter the album's name")
    print(make_album(artist, album))
    choice=input("Do you want to continue? yes/no\n")
    if choice=='no':
        status=False
"""
#TIY 8-9
list1=['hii', 'how are you?', 'how do you do?', 'hehe']
def show_messages():
    while list1:
        current_message=list1.pop()
        print(current_message)
show_messages()
#TIY 8-10
list1=['hii', 'how are you?', 'how do you do?', 'hehe']
sent_messages=[]
def send_messages():
    while list1:
        current_message=list1.pop()
        sent_messages.append(current_message)
    print(sent_messages)
send_messages()
#TIY 8-11
print(list1)
send_messages()
#TIY 8-12
def sandwiches(*items):
    print(items)
sandwiches('egg', 'chicken', 'vegetables')
sandwiches('chicken', 'chicken', 'vegetables', 'eggs')
sandwiches('egg', 'chicken', 'vegetables', 'eggs', 'chicken')
#TIY 8-13
def build_profile(first, last, **user_info):
    user_info['first_name']=first
    user_info['last_name']=last
    return user_info
user_profile=build_profile('albert', 'einstein', location='princeton', field='physics')
print(user_profile)
#TIY 8-14
def make_car(manufacturer, model, **info):
    info['manufacturer']=manufacturer
    info['model']=model
    return info
car=make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)
