height, weight = map(int, input().split())
bmi = weight * 10000 / (height * height)

print("BMI 지수 : {},".format(str(round(bmi, 2))), end=" ")
if bmi < 18.5:
    print("저체중입니다.")
elif bmi < 23:
    print("정상입니다.")
elif bmi < 25:
    print("과체중입니다.")
elif bmi < 30:
    print("경도비만입니다.")
elif bmi < 35:
    print("중정도비만입니다.")
else:
    print("고도비만입니다.")