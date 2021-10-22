# Tuple
# Tuple Are Immutable

myTuple1 = ("Mohamed", "Tamer")
myTuple2 = "Mohamed", "Tamer"

print(myTuple1)
print(myTuple2)

print(type(myTuple1))
print(type(myTuple2))

# Tuple Indexing
myTuple3 = (1, 2, 3, 4, 5)
print(myTuple3[2])

# Tuple Items
myTuple4 = ("Mohamed", 1, 100.5, True)
print(myTuple4[-1])

# ---------------------------------------
# Method
# Tuple With One Element
myTuple5 = ("Tamer",)  # Don't Forget >> ,
myTuple6 = "Tamer",
print(type(myTuple5))
print(type(myTuple6))
print(len(myTuple5))
print(len(myTuple6))

# Tuple Concatenation
a = (1, 2, 3, 4, 5)
b = (6, 7, 8)
c = a + b
print(c)



# Tuple , List , String Repeat(*)
myRep = "Tamer "
print(myRep * 5)




# count()
cou = (1,4,6,3,4,6,3,3,2)
print(cou.count(4))















