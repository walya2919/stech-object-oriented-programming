a, b, c = map(float, input().split())
Max = max(a, b, c)

if Max * 2 < a + b + c:
    print("the perimeter is {0}".format(str(a+b+c)))
else:
    print("Input is invalid")