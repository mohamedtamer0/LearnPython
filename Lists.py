# Lists


myList = ["Mohamed", 1, 100.5, True]
print(myList)
print(myList[0])
print(myList[-1])

print(myList[1:3])
print(myList[:4])
myList[0] = "Tamer"
print(myList)

# ---------------------------------------
# Methods

# append()
myList2 = ["Mohamed", "Tamer", "Habiba"]
myList2.append("Ahmed")
myList2.append(100)
print(myList2)
myList2.append(myList)
print(myList2)
print(myList2[5][0])


# extend()

a = [1, 2, 3, 4]
b =["A","B","C"]
a.extend(b)
print(a)



# remove()
myList3 = ["Mohamed", "Tamer", "Habiba"]
myList3.remove("Tamer")
print(myList3)


# sort()

num = [153, 22, 323, 2354]
num.sort()
print(num)





# clear()

cc = [1, 2, 3, 4]
cc.clear()
print(cc)










