import turtle
#외부 입력값을 세팅한다.
inputX1,inputY1 = eval(input("점의 위치 x,y 을 입력하세요  : "))

x,y= 100,50 #사각형 가로 세로 크기를 세팅한다.

#사각형을 그리기 위해
turtle.pensize(1) #펜사이즈를 1결정한다.
turtle.forward(x) #사각형을 그린다.
turtle.left(90) #90도 회전
turtle.forward(y)
turtle.left(90) #90도 회전
turtle.forward(x)
turtle.left(90) #90도 회전
turtle.forward(y)
turtle.left(90) #사각형을 그리기를 끝낸다.

#외부입력값 점을 그리기 위해
turtle.penup() #점을 그리기위해 펜을 들어올린다.
turtle.goto(inputX1,inputY1) #외부 입력된 x,y좌표로 이동한다.
turtle.pendown() #펜을 내려 그리기 준비를 한다.
turtle.pensize(2) # 펜사이즈를 2로 변경한다.
turtle.begin_fill() #원을 색을 채우기 위해 세팅한다.
turtle.color("red") #펜색을 빨강색으로 변경한다.
turtle.circle(2) #2만큼 원을 그린다.
turtle.end_fill() #원을 색을 채우기 위해 세팅한다.


turtle.penup()
turtle.goto(-20,-40)
turtle.pendown()
if (x >= inputX1) & (y >= inputY1) : 
    #사각형의 x,y값중 가중큰 x,y값에서 입력값보다 크거나 같으면 내부이다.
    turtle.write("점은 사각형 내부에 있습니다.")
else :
    turtle.write("점은 사각형 외부에 있습니다.")
    

turtle.penup() #펜을 들어올린다.
turtle.goto(-1000,-2000) #화살표를 뷰창크기보다 크게 화살표를 없앤다.
turtle.done() 
