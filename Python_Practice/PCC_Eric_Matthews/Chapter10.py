from pathlib import Path
import json
'''
path=Path('/Users/vatsalpathak/Quantum_Computing/Python_Practice/PCC_Eric_Matthews/pi_digits.txt')
contents=path.read_text().rstrip()
print(contents)
lines=contents.splitlines()
pi_string=''
for line in lines:
    pi_string+=line.lstrip()
print(pi_string)
print(len(pi_string))
#TIY 10-1
path1=Path('/Users/vatsalpathak/Quantum_Computing/Python_Practice/PCC_Eric_Matthews/learning_pyhton.txt')
contents1=path1.read_text()
random_string=''
for line in contents1.splitlines():
    random_string+=line.strip()
print(random_string)
print(len(random_string))
random_string=random_string.replace('is', 'are')
#TIY 10-4
path2=Path('programming.txt')
guest=input("Enter your name: ")
path2.write_text(guest)
#TIY 10-5
path3=Path('guest_book.txt')
cond=True
content=''
while cond==True:
    name=input("Enter your name")
    content+=name
    path3.write_text(content)
    ques=input("Do you want to add another name? (yes/no)")
    if ques=='no':
        cond=False
#TIY 10-6
try:
    num1=int(input("Enter the number 1"))
    num2=int(input("Enter the number 2"))
    value=num1+num2
    print(value)
except ValueError:
    print("Bro enter integers not text")
#TIY 10-7
cond=True
while cond==True:
    try:
        num1=int(input("Enter the number 1"))
        num2=int(input("Enter the number 2"))
        value=num1+num2
        print(value)
    except ValueError:
        print("Bro enter integers not text")
        cond=False
#TIY 10-8
try:
    file1=Path('cats.txt')
    file2=Path('dogs.txt')
    content1=file1.read_text()
    content2=file2.read_text()
    zzz=''
    for line in content1.splitlines():
        zzz+=line
    for line in content2.splitlines():
        zzz+=line
except FileNotFoundError:
    print("brother your file is missing")

numbers=[2,3,5,7,11,13]
path=Path('numbers.json')
contents=json.dumps(numbers)
path.write_text(contents)
username=input("enter your username sir") 
content1=json.dumps(username)
path.write_text(contents)
print(f"We'll remember you when you come back, {username}!")
readingcontent=path.read_text()
username2=json.loads(contents)
print(f"Welcome Back, {username2}")
'''
#TIY 10-11 and 10-12
path=Path('favNum.txt')
if path.exists():
    content2=path.read_text()
    num2=json.loads(content2)
    print(f"We know your favorite number is {num2}")
else:
    num1=int(input("Enter your favororite number"))
    content1=json.dumps(num1)
    path.write_text(content1)
#TIY 10-13
user={}
user['name']=input("Enter your name")
user['age']=input("Enter your age")
user['city']=input("Enter your city")
path2=Path('user.txt')
content_new=json.dumps(user)
path2.write_text(content_new)
content_read=path2.read_text()
user_details=json.loads(content_read)
print(user_details)
#TIY 10-14
def get_stored_username(path2):
    if path2.exists():
        return json.loads(path2.read_text())
    return None
def get_new_username(path2):
    username=input("Enter your username")
    path2.write_text(json.dumps(username))
    return username
def greet_user():
    path2=Path('user.txt')
    username=get_stored_username(path2)
    if username:
        confirm=input(f"Are you {username}? (yes/no)")
        if confirm.lower()=='yes':
            print(f"Welcome back, {username}")
        else:
            username=get_new_username(path2)
            print(f"You will be remembered as {username}")
    else:
        username=get_new_username(path2)
        print(f"We'll remember you as {username}")
greet_user()










