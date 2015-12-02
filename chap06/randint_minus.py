import random

number1 = random.randint(0,9)
number2 = random.randint(0,9)

if number1 < number2:
    number1 ,number2 = number2 , number1

answer = eval(input (str(number1) + " - "  + str(number2)+ \
                        "은/는 얼마인가?"))    
    
print(str(number1) + " -" + str(number2) + "-"+ str(answer) + \
       "은/는" , number1 - number2 == answer, "입니다." )

       