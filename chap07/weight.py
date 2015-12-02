#상용자 몸무게를 입력

weight = eval(input("몸무게를 입력해주세요 (예) 75.4:"))

#사용자 키 입력
height = eval (input("키를 입력해주세요 예)175:") )

#BMI 계산
heightMeter = height
heightMeter /= 100
bmi = weight / ( heightMeter * heightMeter)

#결과  출력
msg = "당신은"

if bmi < 18.5:
    msg += "저체중"
elif bmi < 25:
    msg += "정상"
elif bmi < 30 :
    msg += "비만"
    
print ( msg + " 입니다.")
