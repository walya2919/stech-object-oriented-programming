# n 입력받기
# 설명상으로는 n을 9로 가정한다.
n = int(input())

# 숫자는 총 n개의 줄로 이뤄진다
for i in range(n):
    # 위 루프가 진행됨에 따라 8, 7, 6, •••, 1 순으로 실행된다.
    for _ in range(n-1-i):
        print("  ",end="")
    # 상위 루프가 진행됨에 따라 "", "2 ", "3 2 ", "4 3 2 ", ••• 순으로 진행된다.
    for _ in range(i):
        print("{} ".format(str(i+1-_)), end="")
    
    # 모든 줄에 공통으로 출력하는 "1 "
    print("1 ", end="")
    
    # 상위 루프가 진행됨에 따라 "", "2 ", "2 3 ", "2 3 4 ", ••• 순으로 진행된다.
    for _ in range(i):
        print("{} ".format(str(_+2)), end="")
    
    #상위루프 종료마다 개행문자를 삽입한다.
    print("")



