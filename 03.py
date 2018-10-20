import turtle
import math
#定义多给点
x1,y1=100,100
x2,y2=100,-100
x3,y3=-100,-100
x4,y4=-100,100

#绘制
turtle.penup()
turtle.goto(x1,y1)
turtle.pendown()
turtle.goto(x2,y2)
turtle.goto(x3,y3)
turtle.goto(x4,y4)

distance=math.sqrt((x4-x1)**2+(y4-y1)**2)
turtle.write(distance)
