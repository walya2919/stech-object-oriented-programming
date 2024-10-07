import math

# the answer of integral f1 from 0 to 1 is 2
a1 = float(2)
def f1(x : float):
    return (x*2) + 1

# the answer of integral f2 from -2 to 2 is 4/3
a2 = 4/3
def f2(x : float):
    return (x**2) - 1

# the answer of integral f3 from 1 to 3 is 2 * sqrt(3) - 2/3
a3 = (2 * math.sqrt(3)) - (2/3)
def f3(x : float):
    return math.sqrt(x)

# the answer of integral f4 from 0 to 1 is e - 1
a4 = math.e - 1
def f4(x : float):
    return math.exp(x)

# the answer of integral f5 from 0 to pi/2 is 1
a5 = 1
def f5(x : float):
    return math.cos(x)

def integral(f, a : int, b : int):
    # delta x = 0.00001
    # use a right endpoint
    x = float(a)
    delta_x = 0.00001
    sum = 0

    x += delta_x
    while x <= b:
        sum += delta_x * f(x)
        x += delta_x
    
    # this is for when b-a is not n * delta_x (n is natural number)
    delta_x = b - x + delta_x
    sum += delta_x * f(b)

    return sum

def test_integral():
    if math.fabs(a1 - integral(f1, 0, 1)) > 0.001:
        return False
    if math.fabs(a2 - integral(f2, -2, 2)) > 0.001:
        return False
    if math.fabs(a3 - integral(f3, 1, 3)) > 0.001:
        return False
    if math.fabs(a4 - integral(f4, 0, 1)) > 0.001:
        return False
    if math.fabs(a5 - integral(f5, 0, math.pi / 2)) > 0.001:
        return False
    
    return True
