import random

while True:
    chose=['가위','바위','보자기']
    computer_chose= random.choice(chose)

    user = input("가위,바위,보자기 중 하나를 선택하세요:")


    if computer_chose == '가위':
        print("컴퓨터: 가위")
        if user == '가위':
            print("사용자: 가위")
            print("무승부 입니다")
        elif user == '바위':
            print("사용자: 바위")
            print("사용자 승리!")
        elif user == '보자기':
            print("사용자: 보자기")
            print("컴퓨터 승리!")

    if computer_chose == '바위':
        print("컴퓨터: 바위")
        if user == '가위':
            print("사용자: 가위")
            print("컴퓨터 승리!")
        elif user == '바위':
            print("사용자: 바위")
            print("무승부 입니다")
        elif user == '보자기':
            print("사용자: 보자기")
            print("사용자 승리!")

    if computer_chose == '보자기':
        print("컴퓨터: 보자기")
        if user == '가위':
            print("사용자: 가위")
            print("사용자 승리!")
        elif user == '바위':
            print("사용자: 바위")
            print("컴퓨터 승리!")
        elif user == '보자기':
            print("사용자: 보자기")
            print("무승부 입니다")


    regame=input("다시하겠습니까? (y/n):")
    if regame=="n":
        print("게임을 종료합니다")
        break


