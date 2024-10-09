import math
import random
from integral import f1, f2, f3, f4, f5

# define the derivative
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
    # x is float in range 0-10
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

def sign(num : float):
    if num > 0:
        return 1
    elif num < 0:
        return -1
    else:
        return 0

# return every proximate int to solution in [st_point, end_point)
def guess_find_point(f, st_point, end_point):
    x = st_point + 1
    pre_fx = sign(f(st_point))
    find_points = list()

    while x <= end_point:
        fx = sign(f(x))
        
        if pre_fx == 0 | pre_fx != fx:
            find_points.append(min(x, x-1, key = lambda x : math.fabs(f(x))))
        
        pre_fx = fx
        x += 1
    
    return find_points

def newton_method(f, st_point):
    eps = 0.000000001
    x = st_point

    while math.fabs(f(x)) > eps:
        x = x - (f(x)/defferential(f, x))
    
    return x

def find_solution(f, st_point, ed_point):
    find_points = guess_find_point(f, st_point, ed_point)
    solutions = list()

    for find_point in find_points:
        solutions.append(newton_method(f, find_point))
    
    return solutions