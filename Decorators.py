# Decorators

def myDecorator(func):
    def nestedFunc(num1, num2):
        print("Before")
        func(num1, num2)
        print("After")

    return nestedFunc


@myDecorator
def calc(n1, n2):
    print(n1 + n2)

calc(10, 90)
