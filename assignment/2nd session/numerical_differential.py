import math
import random
from integral import f1, f2, f3, f4, f5

def df1(x):
    return 2

def df2(x):
    return 2 * x

def df3(x):
    return 1 / (2 * math.sqrt(x))

def df4(x):
    return math.exp(x)

def df5(x):
    return -1 * math.sin(x)

def defferential(f, x, h = 0.00001):
    return (f(x+h) - f(x-h)) / (2 * h)

def test_defferential():
    # x is float in range
    x = random.random()
    if x == 0:
        x += 1
    x *= 10

    if math.fabs(df1(x) - defferential(f1, x)) > 0.001:
        print(1)
        return False
    if math.fabs(df2(x) - defferential(f2, x)) > 0.001:
        print(2)
        return False
    if math.fabs(df3(x) - defferential(f3, x)) > 0.001:
        print(3)
        return False
    if math.fabs(df4(x) - defferential(f4, x)) > 0.001:
        print(4)
        return False
    if math.fabs(df5(x) - defferential(f5, x)) > 0.001:
        print(5)
        return False
    
    return True
