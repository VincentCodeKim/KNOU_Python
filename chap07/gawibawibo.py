import random

# 가위바이보 게임
#컴퓨터 가위바위보 생성
computer  = random.randint(0,2)

#사용자의 가위바위보 입력
user = eval (input("가위 0 , 바위 1 , 보 2: "))

#평가
if computer == 0:
    if user ==0:
        print ("컴퓨터 가위, 당신도 가위 비겼습니다.")

    elif user==1:
        print("컴퓨터 가위, 당신은 바위 , 당신은 이겼습니다.")
    
    else:
        print ("당신이 졌습니다.")    

elif computer == 1:
    if user ==0:
        print ("컴퓨터 가위, 당신도 가위 비겼습니다.")

    elif user==1:
        print("컴퓨터 가위, 당신은 바위 , 당신은 이겼습니다.")
    else:
        print ("당신이 졌습니다.")
        
else:
    if user ==0:
        print ("컴퓨터 바위, 당신도 가위.")

    elif user==1:
        print("컴퓨터 바위, 당신은 바위 , 당신은 이겼습니다.")
    
    else:
        print ("당신이 졌습니다.")            