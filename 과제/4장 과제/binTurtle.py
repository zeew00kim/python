import turtle # 거북이 모양의 거북이 그래픽 모듈

num = 0
swidth = 500 # 화면 너비 설정
sheight = 300 # 화면 높이 설정
x, y = 0, 0 # 거북이 아이콘의 시작 위치 좌표

if __name__ == "__main__" :
    turtle.title("expression of binary number by turtle")
    turtle.shape("turtle")  # 거북이 모양으로 설정
    turtle.setup(width = swidth + 50, height = sheight + 50) # 전체 그래픽 창 크기
    turtle.screensize(swidth, sheight) # 거북이가 움직일 수 있는 가상 화면 크기
    turtle.penup() # 거북이가 이동 시 선을 그리지 않게 설정
    turtle.left(90) # 거북이의 머리가 위를 향하도록 설정

    num = int(input("enter the integer : "))
    binary = bin(num)
    x = swidth / 2
    y = 0
    
    for i in range(len(binary) - 2):  # 이진수임을 나타내는 접두어 0b 제외한 만큼 반복
        turtle.goto(x, y)
        if num & 1: # 비트 값이 1이라면 거북이는 red, 2
            turtle.color("red")
            turtle.turtlesize(2)
        else: # 비트 값이 0일 경우 blud, 1
            turtle.color("blue")
            turtle.turtlesize(1)
        turtle.stamp()
        x -= 50 # 다음에 stamp 하게 될 거북이의 좌표
        num >>= 1 # 다음 비트 검사

    turtle.done()