import math
import random
import sympy

def is_prime(num : int):
    # 1인 경우 반복문을 건너뛰어 소수가 아님에도 True가 반환되기에 예외처리
    if num == 1:
        return False

    for _ in range(2, int(math.sqrt(num)) + 1):
        if 0 == (num % _):
            return False
        
    return True

def test_is_prime():
    # 1-100 사이의 소수 list와 1 및 합성수 list 생성
    prime = set(sympy.primerange(1, 101))
    non_prime = set(range(1,101))-prime

    prime = list(prime)

    # list를 섞어 5번 pop을 통해 원하는 결과와 is_prime의 결과를 비교
    random.shuffle(prime)
    for _ in range(5):
        if not is_prime(prime.pop()):
            return False

    non_prime = list(non_prime)
    random.shuffle(non_prime)
    for _ in range(5):
        if is_prime(non_prime.pop()):
            return False
    
    # 10회 수행후 모든 결과가 잘 나왔다면 참을 반환
    return True

print(test_is_prime())