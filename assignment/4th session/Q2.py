print("A: ",end="")
try:
    exec("6 * ----------8")
    print("6 * ----------8 dosn't make SyntaxError")
except SyntaxError:
    pass
    print("6 * ----------8 makes SyntaxError")
except:
    print("6 * ----------8 dosn't make OtherError")


# Case B makes SyntaxError
print("B: ",end="")
try:
    exec("8 = people")
    print("8 = people dosn't make SyntaxError")
except SyntaxError:
    pass
    print("8 = people makes SyntaxError")
except:
    print("8 = people dosn't make OtherError")


print("C: ",end="")
try:
    exec("((((4 ** 3))))")
    print("((((4 ** 3)))) dosn't make SyntaxError")
except SyntaxError:
    pass
    print("((((4 ** 3)))) makes SyntaxError")
except:
    print("((((4 ** 3)))) dosn't make OtherError")


print("D: ",end="")
try:
    exec("(-(-(-(-5))))")
    print("(-(-(-(-5)))) dosn't make SyntaxError")
except SyntaxError:
    pass
    print("(-(-(-(-5)))) makes SyntaxError")
except:
    print("(-(-(-(-5)))) dosn't make OtherError")


# Case E makes SyntaxError
print("E: ",end="")
try:
    exec("4 += 7 / 2")
    print("4 += 7 / 2 dosn't make SyntaxError")
except SyntaxError:
    pass
    print("4 += 7 / 2 makes SyntaxError")
except:
    print("4 += 7 / 2 dosn't make OtherError")