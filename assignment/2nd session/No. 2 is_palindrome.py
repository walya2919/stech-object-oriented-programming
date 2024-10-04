import random

def is_palindrome(num : int):
    num_str = list(str(num))

    num_revstr = num_str[:]
    num_revstr.reverse()
    print(num_str)
    print(num_revstr)

    if num_str == num_revstr:
        return True
    else:
        return False

def test_is_palindrome():
    for _ in range(5):
        pali = random.randint(1,100)
        rep = random.randint(0,1)

        pali = list(str(pali))
        li = pali[:]
        
        
        if not rep:
            pali.pop()
        
        pali.reverse()
        li = li + pali

        if not is_palindrome(int(str(li))):
            return False

           