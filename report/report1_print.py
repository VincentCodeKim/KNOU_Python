lists = ["a",1,2,3,4]
starNum=0;
for i in lists: # 배열정보 크기 만큼 loop
    
    for n in range(3): #0~2 반복문을 수행한다. for(int i=0;i < 3;i++ 동일
        if(starNum == 0):
            tmp = n+1; #시작이 0이기 때문에 +1을 더해 제곱을 수행할수 있도록한)다.
            print(i,"^",tmp, end="\t\t");
        else:
            tmp = n+1; #시작이 0이기 때문에 +1을 더해 제곱을 수행할수 있도록한)다.
            print(i**tmp, end="\t\t");
    starNum=starNum+1 #문자 첫번째 배열을 판단하기 위해서
    print("\n")
