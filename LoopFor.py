# Loop For


myList = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for number in myList:
    print(number)

myName = "Tamer"
for letter in myName:
    print(f"[{letter.upper()}]")

# ==================================================

print("#" * 30)
myRange = range(1, 101)
for num in myRange:
    print(num)

# ==================================================

print("#" * 30)

list = {
    "Kotlin": "99%",
    "Java": "90%",
    "Python": "50%"
}

for skill in list:
    print(f"{skill} Is : {list[skill]}")

# ==================================================

print("#" * 30)

people = {
    "Tamer": {
        "Kotlin": "99%",
        "Java": "90%",
        "Python": "50%"
    },
    "Ahmed": {
        "Kotlin": "99%",
        "Java": "90%",
        "Python": "50%"
    },
    "Mohab": {
        "Kotlin": "99%",
        "Java": "90%",
        "Python": "50%"
    },
}

print(people["Tamer"])
for name in people:
    print(f"Skills and Progress For {name} Is: ")
    for skills in people[name] :
        print(f"{skills} => {people[name][skills]}")
