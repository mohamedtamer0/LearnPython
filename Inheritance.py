# Inheritance

class Food:

    def __init__(self, name, price):
        self.name = name
        self.price = price
        print(f"{self.name} Is Created From Base Class")

    def eat(self):
        print("Eat Method From Base Class")


class Apple(Food):

    def __init__(self, name, price):
        super().__init__(name, price)
        print(f"{self.name} Is Created From Derived Class And Price Is {self.price}")

    def eat(self):
        print("Eat Method From Derived Class")


food_one = Apple("Apple", 30)
food_one.eat()
