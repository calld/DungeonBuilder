import random import randrange

def roll(count, size):
    s = 0
    for i in range(count):
        s += randrange(size) + 1
    return s
