import turtle

# 4개의 변수 모두 0으로 초기화
i, k, tX, tY = [0] * 4 
swidth, sheight = 800, 450 

if __name__ == "__main__" :
    turtle.title("거북이 99단")
    turtle.shape("turtle")
    turtle.setup(width = swidth + 50, height = sheight + 50)
    turtle.screensize(swidth, sheight)
    turtle.penup()
    tX, tY = -500, 250
    turtle.goto(tX, tY)

    for i in range(1, 10):
        for j in range(2, 10):
            turtle.goto(tX + 80 * j, tY - 40 * i)
            gugu = str(j) + ' x ' + str(i) + ' = ' + str(j * i)
            turtle.write(gugu, font = ("Arial", 12, "bold"))

    turtle.goto(0, -sheight // 2 + 20)
    turtle.write("99단 작성 완료!!!", align="center", font=("Arial", 16, "bold"))
    
    turtle.done()