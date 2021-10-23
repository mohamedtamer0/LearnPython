# Built_In_Function


# all()

x = [1, 2, 3, 4, []]
if all(x):
    print("Done")
else:
    print("Error")

# any()
y = [1, 2, 3, 4, []]
if any(y):
    print("Done")
else:
    print("Error")

# bin()
print(bin(100))

# id()
a = 1
b = 2
print(id(a))
print(id(b))

# sum(iterable, start)
s = [3, 46, 343, 532]
print(sum(s))
print(sum(s, 54))

# round(number, numofdigits)
print(round(140.449))
print(round(140.449, 2))

# range(start , end, step)
print(list(range(0, 20, 2)))

# abs()
print(abs(-100))

# pow()
print(pow(2, 5, 10))

# min()
print(min(3, -4, 2, 42, 2, 0, -1))
