import json
mydictionary = {'name'}

name = {}
birthday = {}
siblings = {}
age = {}
pets = {}
location ={}
hobby = {}
food ={}
drink ={}
musicgenre ={}
word = ["name","birthday","siblings", "age", "pets","location", "hobby", "food", "drink", "musicgenre"]
users = {}
users['name'] = 1
print(users.get('name'))
print("HEY, LET'S TAKE A SURVEY!")
while True:
    name = input("What is your full name?\n")
    birthday = input("When is your birthday? (Use the reference, MM/DD/YY to answer)\n")
    siblings = input("Do you have any siblings? If so, how many?\n")
    age = input("How old are you?\n")
    pets = input("Do you have any pets? If so, how many?\n")
    location = input("Where do you live? City? Town? Country?\n")
    hobby = input("What do you like to do on your free time?\n")
    food = input("What is your favorite food?\n")
    drink = input("What is your favorite beverage to drink?\n")
    musicgenre = input("What genre of music do you like to listen to?\n")
    break
print("THANKS FOR TAKING THE SURVEY!\n")
answers = [name, birthday, siblings, age, pets, location, hobby, food, drink, musicgenre]

mydictionary = {}
for i in range(len(word)):
    mydictionary[word[i]] = answers[i]

print(mydictionary)

dictionaryToJson = json.dumps(mydictionary)

file = open("survey.json", "a")
file.write(dictionaryToJson)
file.close()

file1 = open("survey.json", "r")
