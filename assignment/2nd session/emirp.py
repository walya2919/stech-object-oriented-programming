import is_prime
import is_palindrome

def emirp(num : int):

    for i in range(1, num + 1):
        for_num = i
        rev_num = list(str(i))
        rev_num.reverse()
        rev_num = int(str(rev_num))

        if is_prime(for_num) and is_prime(rev_num) and \
            not is_palindrome(for_num) and not is_palindrome(rev_num):
            print(i)

