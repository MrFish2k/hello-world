import turtle

def drawSnake(rad, angle, len, neckrad):
    for i in range(len):
        turtle.circle(rad,angle)
        turtle.circle(-rad,angle)#画笔沿圆形轨迹运动，rad为半径，angle为弧度
    turtle.circle(rad,angle/2)
    turtle.fd(rad)    #turtle.fd()即位turtle.forward(),表示画笔直线移动，rad为距离
    turtle.circle(neckrad+1,180)
    turtle.fd(rad*2/3)

def main():
    turtle.setup(1300,800,0,0) #启动窗口并设置参数：宽，高，左上角坐标
    pythonsize = 30
    turtle.pensize(pythonsize) #画笔宽度（像素）
    turtle.pencolor("blue")    #颜色
    turtle.seth(-40)           #画笔启动时运行方向（角度值°）（-表示反向）
    drawSnake(40,80,5,pythonsize/2)#调用dra……函数，其参数对应调用中参数

main()