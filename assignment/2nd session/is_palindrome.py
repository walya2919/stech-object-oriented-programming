import random

def is_palindrome(num : int):
    num_str = list(str(num))

    num_revstr = num_str[::-1]

    if num_str == num_revstr:
        return True
    else:
        return False

def test_is_palindrome():
    # input non-palindrom number
    for _ in range(5):
        while True:
            num = random.randint(1,100000)
            for_num = str(num)
            rev_num = str(num)[::-1]
            if for_num != rev_num:
                break
        
        if is_palindrome(num):
            return False
    
    # input palindrom number
    for _ in range(5):
        while True:
            num = random.randint(1,100000)
            for_num = str(num)
            rev_num = str(num)[::-1]
            if for_num == rev_num:
                break
        
        if not is_palindrome(num):
            return False
    
    # if pass both of above test
    return True
