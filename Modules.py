# Modules

# Import Main Module


import random

print(f'Print Random {random.random()}')

# --------------------------------

print(dir(random))

# Import One Or Two Fun From Module
from random import randint

print(f"print Random {randint(100, 900)}")

# --------------------------------
print("#" * 30)

import Tamer as obj

# print(dir(Tamer))

obj.sayHello("Tamer")
obj.howAreYou("Mohamed")

# --------------------------------
print("#" * 30)
