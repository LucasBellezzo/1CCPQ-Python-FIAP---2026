import math
from math import radians

num = 17
raiz = math.sqrt(num)
print(f"A Raiz de {num} é {raiz:.2f}.")


graus = 90
radiano = graus / 180 * math.pi
seno = math.sin(radiano)
print(seno)


import random

num_random = random.random()
print(num_random*10)

num_rand_int = random.randint(1, 10)
print(num_rand_int)