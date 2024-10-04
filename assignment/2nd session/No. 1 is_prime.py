import math
import random
import sympy

def is_prime(num : int):
    # 1인 경우 반복문의 
    if num == 1:
        return False

    for _ in range(2, int(math.sqrt(num)) + 1):
        if 0 == (num % _):
            return False
        
    return True

def test_is_prime():
    prime = set(sympy.primerange(1, 101))
    non_prime = set(range(1,101))-prime

    prime = list(prime)
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

print(test_is_prime())