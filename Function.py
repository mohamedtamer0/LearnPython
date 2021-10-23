# Function


def function_name():
    print("Hello World")


function_name()


def function_name2():
    return "Hello World"


print(function_name2())

# ==================================================

print("#" * 30)


def say_Hello(name):
    print(f"Hello {name}")


say_Hello("Ahmed")


# ==================================================

def addition(n1, n2):
    return n1 + n2


print(addition(4, 4))


# ==================================================

def additionError(num1, num2):
    if type(num1) != int or type(num2) != int:
        print("Only Integers Allowed")

    else:
        return num1 + num2


print(additionError(4, 57))

# ==================================================

print("#" * 30)


def namePeople(*names):
    for name in names:
        print(f"Hello {name}")


namePeople("Tamer", "Tamer", "Tamer", "Tamer", "Tamer", "Tamer", "Tamer")

# ==================================================

print("#" * 30)


# **KWArg

def show_skills(**skills):
    print(type(skills))
    for skill, value in skills.items():
        print(f"{skill} => {value}")


show_skills(Html="80%", Css="60%")

# ==================================================

print("#" * 30)

# Scope
x = 1  # Global Scope


def one():
    x = 5  # Local
    print(x)


one()
print(x)


# ==================================================

print("#" * 30)



