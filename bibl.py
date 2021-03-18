#импорт функции randint из библиотеки random
from random import randint


x = 0
while x != 1:
    x = randint(0, 100)
    print(x)