import is_prime as pr
import is_palindrome as pa

# find prime number that reverse is also prime but not same to forword number
def emirp(num : int):
    for i in range(1, num + 1):
        if not pr.is_prime(i):
            continue
        if pa.is_palindrome(i):
            continue
        if pr.is_prime(int(str(i)[::-1])):
            print(i)
