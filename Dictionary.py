# Dictionary


user = {
    "name": "Mohamed",
    "age": 25,
    "Country": "Egypt",
    "Skills": ["Kotlin", "Java", "Python"]
}

print(user)
print(user["age"])
print(user.get("name"))
print(user.keys())
print(user.values())

languages = {
    "One": {
        "name": "Kotlin",
        "prog": "90%"
    },
    "Two": {
        "name": "Java",
        "prog": "89%"
    }
}

print(languages)
print(languages["Two"]["name"])
print(len(languages))

# clear()
languages2 = {
    "One": {
        "name": "Kotlin",
        "prog": "90%"
    },
    "Two": {
        "name": "Java",
        "prog": "89%"
    }
}
languages2.clear()
print(languages2)

# update()

user2 = {
    "name": "Tamer",
    "age": 25
}
user2.update({"Country": "Egypt"})
print(user2)
