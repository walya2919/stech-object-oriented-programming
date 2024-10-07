import math
import random
import sympy

def is_prime(num : int):
    # if variable is 1, the for statement is skipped
    # so make a exception
    if num == 1:
        return False

    for _ in range(2, int(math.sqrt(num)) + 1):
        if 0 == (num % _):
            return False
        
    return True

def test_is_prime():
    # make a prime number list in the range 1-100
    prime = set(sympy.primerange(1, 101))
    non_prime = set(range(1,101))-prime

    prime = list(prime)

    # shuffle the prime number list and non prime number list
    random.shuffle(prime)
    for _ in range(5):
        if not is_prime(prime.pop()):
            return False

    non_prime = list(non_prime)
    random.shuffle(non_prime)
    for _ in range(5):
        if is_prime(non_prime.pop()):
            return False
    
    return True
