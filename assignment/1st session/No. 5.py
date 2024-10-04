# 컴퓨터가 가위, 바위, 혹은 보를 내기 위함
import random

# 0을 가위로, 1을 바위로, 2를 볼 반환하기
def num_to_choise(num):
    if num == 0:
        return "scissor"
    elif num == 1:
        return "rock"
    else:
        return "paper"

# 플레이어와 컴퓨터의 승리횟수를 선언하기
cpu_win = 0; player_win = 0

# 승리횟수중 하나라도 2 이상이 될 때
while (cpu_win < 2)&(player_win < 2):
    # 플레이어가 고를 패 선택하기
    print("select sissor (0), rock(1), paper(2) : ", end = "")
    player_choose = int(input())

    # randint를 통해 컴퓨터가 낼 패 정하기
    cpu_choose = random.randint(0, 2)

    # 승, 패, 무승부에서 동일하게 출력하는 부분 출력하기
    print("you sellect {0}. Computer choose {1}.".format(num_to_choise(player_choose), \
                  num_to_choise(cpu_choose)), end=" ")
    
    # 플레이어의 승, 패, 무승부 조건문으로 나누기
    if player_choose == cpu_choose:
        print("Draw")
    elif ((player_choose==0)&(cpu_choose==1))|\
    ((player_choose==1)&(cpu_choose==2))|\
    ((player_choose==2)&(cpu_choose==0)):
        print("The computer won.")
        cpu_win += 1
    else:
        print("You won.")
        player_win += 1

# 승리횟수를 통해 최종승자 출력하기
if cpu_win == 2:
    print("The computer won more than twice. Game Over.")
else:
    print("You won more than twice. Game Over")