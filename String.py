# Strings

msg1 = 'Hello World 1'
msg2 = "Hello World 2"
msg3 = 'Hello World 3 "Test"'
print(msg1)
print(msg2)
print(msg3)

msg4 = """"Hello
My Name Is Mohamed
My Age 25
"""
print(msg4)

# ---------------------------------#


# Indexing (Access Single Item)
myString = "I Love Coding"
print(myString[0])  # Index 0 >> I
print(myString[-1])  # Index -1 >> g

# Slicing
# [Start:End] End Not Included
# [Start:End:Steps]

print(myString[7:9])  # Cd
print(myString[:9])  # I Love Co

print(myString[0::1])  # Full Data
print(myString[::1])  # Full Data

# -----------------------------------------------#


# ---------------------------------#
#
# String Methods
#
# ---------------------------------#


method1 = "I Love Kotlin"
method2 = "         I Love       Kotlin"
print(len(method1))
print(len(method2))

# Strip
method3 = "         I Love Kotlin"
print(method3.strip())
method4 = "### I Love Kotlin"
print(method4.strip("#"))

# title()
title1 = "Brief about me, I'm an Android dev in both languages Java and Kotlin"
print(title1.title())

title2 = "Brief about me, I'm an Android dev in both languages Java and Kotlin"
print(title2.capitalize())

x, y, z = "1", "11", "111"
print(x.zfill(3))  # 001
print(y.zfill(3))  # 011
print(z.zfill(3))

# Split() rsplit()

split1 = "Brief about me, I'm an Android dev in both languages Java and Kotlin"
print(split1.split())

split2 = "Brief about me, I'm an Android dev in both languages Java and Kotlin"
print(split2.split(" ", 2))

split2 = "Brief about me, I'm an Android dev in both languages Java and Kotlin"
print(split2.rsplit(" ", 2))

# Center()
n = "Tamer"
print(n.center(9, "#"))

# count()
f = "Brief about me, I'm an Android dev in both languages Java and Kotlin"
print(f.count("Java"))  # count Java one word

# swapcase()
g = "I Love Python"
print(g.swapcase())

# index()

g2 = "I Love Python"
print(g2.index("o"))  # Index Number

# rjust(width,fill char) and ljust()
g3 = "I Love Python"
g4 = "I Love Python"
print(g3.rjust(50, "#"))
print(g4.ljust(50, "#"))

g5 = """"I Love Python
I Love Python
I Love Python
"""
print(g5.splitlines())

# replace(old value, new value, count)
g6 = "I Love Python"
print(g6.replace("Python", "Kotlin", 1))

# join(Iterable)

myList = ["Mohamed", "Tamer", "Habiba"]
print("-".join(myList))

# ---------------------------------#
#
# String Formatting
#
# ---------------------------------#

# Old Ways
# name= "Tamer"
# age= 25
# rank = 10
# print("My Name Is : %s and My Age is: %d and My Rank is : %f" %(name,age,rank))


# New Ways
name = "Tamer"
age = 25
rank = 10
print("My Name Is : {:s} and My Age is: {:d} and My Rank is : {:f}".format(name, age, rank))
