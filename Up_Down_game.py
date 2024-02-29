import random

while True:
    random_number = random.randint(1, 100)
    game_count=1

    while True:
        my_answer=int(input("숫자를 입력하세요: "))

        if my_answer == random_number:
            print("맞았습니다")
            print(f"시도한 횟수:{game_count}")
            break
        elif my_answer > random_number:
            print("다운")
            game_count+=1
        else:
            print("업")
            game_count+=1

    regame=input("다시하겠습니까? (y/n):")
    if regame=="n":
        print("게임을 종료합니다")
        break