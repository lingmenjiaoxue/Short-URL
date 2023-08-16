import random
import string
import os

random_letters = ''.join(random.choices(string.ascii_letters, k=5))
print(random_letters)

os.system('pause')