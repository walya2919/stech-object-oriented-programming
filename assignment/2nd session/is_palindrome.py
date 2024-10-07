import random

def is_palindrome(num : int):
    num_str = list(str(num))

    num_revstr = num_str[::-1]

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

        if not is_palindrome(int("".join(li))):
            return False
    
    for _ in range(5):
        while True:
            num = random.randint(1,100000)
            for_num = str(num)
            rev_num = str(num)[::-1]
            if for_num != rev_num:
                break
        
        if is_palindrome(num):
            return False
    
    return (True)

true_count = 0
false_count = 0

for _ in range(10000000):
    if test_is_palindrome():
        true_count += 1
    else:
        false_count += 1

print("2종오류 발생율: {}%".format(str(false_count / 10)))