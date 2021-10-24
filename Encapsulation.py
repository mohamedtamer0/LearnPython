# Encapsulation
# Protected  _
# Private __

class Member:
    def __init__(self, name):
        self.__name = name  # Private
        # self._name = name  # Protected

    def say_hello(self):
        return f"Hello {self.__name}"

    def set_name(self, newName):
        self.__name = newName

    def get_name(self):
        return self.__name


one = Member("Tamer")
print(one.get_name())
one.set_name("Mohamed")
print(one.get_name())