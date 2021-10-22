# Set


# Not Ordered And Not Indexed
mySet1 = {"Tamer", 100, False}
print(mySet1)

# Has Only Immutable Data Type
mySet2 = {"Tamer", 100, True, 122.4, (1, 2, 3)}
print(mySet2)

# clear()
mySet3 = {"Tamer", 100, True, 122.4, (1, 2, 3)}
mySet3.clear()
print(mySet3)

# Union
a = {1, 2, 3, 4, 5}
b = {6, 7, 8}
print(a | b)

# add()
d = {1, 2, 3, 4, 5}
d.add(99)
print(d)

# pop()
i = {"A", True, 1, 2, 3, 4, 5}
print(i.pop())  # Random Element

# update()
j = {1, 2, 3, 4}
k = {3, 4, "A", 8, 98, 656}
j.union(k)
print(j)

# issuperset()
x = {1, 2, 3, 4, 5, 6}
y = {1, 2, 3, 4}
print(x.issuperset(y))
