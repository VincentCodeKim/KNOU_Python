import random

number = random.randint(0,100)

print("0과 100사의 미지숫자를 맞춰보세요:",number)

guess = eval(input("얼마일까요? : "))

if guess == number:
    print ("맞았습니다. 미지의 숫자는 ", number, "입니다.")
     
elif guess > number :
    print ("입력값 같이 너무 큽니다.")

else :
    print("입력한  값이 너무 적습니다.")
    