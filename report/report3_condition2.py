var_shampoo_1_kg,var_shampoo_1_price = eval(input("샴푸 1의 용량과 가격을 입력하세요:"))
var_shampoo_2_kg,var_shampoo_2_price = eval(input("샴푸 2의 요량과 가격을 입력하세요:"))

# 샴푸1의 용량과 가격을 곱한다. 1원당 = 490g
cal_var_shampoo_1 = var_shampoo_1_price/var_shampoo_1_kg

# 샴푸2의 용량과 가격을 곱한다. 1원당= 472.5g
cal_var_shampoo_2 = var_shampoo_2_price/var_shampoo_2_kg 

print("샴푸1 ml당 가격:",cal_var_shampoo_1)
print("샴푸2 ml당 가격:",cal_var_shampoo_2)


#만약  결과 삼푸2결과가 1보다 크다면 샴푸1 조건이 더 좋음
if cal_var_shampoo_1 < cal_var_shampoo_2:
    print("샴푸 1의 조건이  더좋습니다.")
    
elif  cal_var_shampoo_1 == cal_var_shampoo_2:
    print("샴푸 1의 조건과 샴푸2의 조건이 동일합니다")
    
#위결과와 반대일경우 삼푸2의 결과가 더 좋음
else:
    print("샴푸 2의 조건이  더좋습니다.")
#종료
