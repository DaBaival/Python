import turtle
import matplotlib.pyplot as plt
import pandas as pd
#窗口大小
turtle.setup(1500,580)

#画笔
t=turtle.Turtle()
l=turtle.Turtle()
p=turtle.Turtle()
b=turtle.Turtle()
u=turtle.Turtle()
m=turtle.Turtle()
n=turtle.Turtle()
w=turtle.Turtle()

#关闭动画
turtle.tracer(1)

#画笔属性
    
turtle.setup(2000,1000,0,0)#设置画布大小
turtle.screensize(1000,1000,'black')#设置画布属性
m.pensize(10)
p.pensize(10)
b.pensize(35)
turtle.pensize(10)
turtle.hideturtle()
l.hideturtle()
p.hideturtle()
b.hideturtle()
m.hideturtle()
b.hideturtle()
n.hideturtle()
t.hideturtle()
u.hideturtle()
w.hideturtle()

#背景色
b.fillcolor("lightblue")
b.begin_fill()
b.up()
b.goto(-250,260)
b.seth(-90)
b.fd(410)
b.seth(0)
b.fd(410)
b.seth(90)
b.fd(410)
b.seth(180)
b.fd(410)
b.down()
b.end_fill()

#背景图案1
u.fillcolor("plum")
u.begin_fill()
u.up()
u.goto(-250,260)
u.seth(-90)
u.fd(10)
u.seth(-40)
u.fd(200)
u.seth(90)
u.fd(110)
u.seth(145)
u.fd(45)
u.goto(-250,260)
u.down()
u.end_fill()

#背景图案2
u.up()
u.seth(-90)
u.fd(10)
u.fillcolor("paleturquoise")
u.begin_fill()
u.seth(-40)
u.fd(535)
u.seth(-90)
u.fd(55)
u.seth(180)
u.fd(150)
u.seth(140)
u.fd(350)
u.goto(-250,260)
u.down()
u.end_fill()

#篮球
p.fillcolor("darkorange")
p.begin_fill()
p.seth(170)
p.up()
p.goto(-180,20)
p.down()
for i in range(5):
    p.fd(13)
    p.left(5)
p.up()
p.seth(-90)
p.fd(25)
p.down()
p.seth(-15)
for i in range(5):
    p.fd(13)
    p.left(5)
p.seth(185)
for i in range(5):
    p.fd(13)
    p.right(5)
p.up()
p.seth(-90)
p.fd(40)
p.down()
p.seth(-25)
p.fd(75)
p.fd(-75)
p.up()
p.seth(-90)
p.fd(50)
p.down()
p.seth(-20)
for i in range(5):
    p.fd(17)
    p.right(5)
p.up()
p.seth(-40)
for i in range(5):
    p.fd(-17)
    p.right(-5)
p.seth(-90)
p.fd(50)
p.seth(0)
p.fd(80)


p.seth(90)
p.fd(59)
p.seth(180)
p.fd(15)
p.seth(90)
p.fd(30)
p.seth(0)
p.fd(30)
p.goto(-180,20)
p.down()
p.end_fill()


#脸色
t.fillcolor("Khaki1")
t.begin_fill()
t.up()
t.goto(-180,62)
t.down()
t.seth(-95)
for i in range(5):
    t.fd(22)
    t.left(i*5+5)
t.seth(-45)
t.circle(100,75)
t.seth(-15)
for i in range(5):
    t.fd(28)
    t.left(10)
t.seth(90)
t.fd(20)
t.seth(45)
t.circle(90,140)
t.seth(135)
t.fd(32)
t.seth(180)
for i in range(3):
    t.fd(30)
    t.left(5)
t.goto(-180,62)
t.end_fill()
#左眼白
t.pensize(10)
t.fillcolor("white")
t.begin_fill()
t.seth(-20)
t.up()
t.goto(-75,40)
t.down()
for i in range(2):
    t.circle(43,135)
    t.circle(58,45)
t.end_fill()
t.pensize(1)

#右眼白
t.pensize(10)
t.fillcolor("white")
t.begin_fill()
t.seth(-300)
t.up()
t.goto(78,70)
t.down()
for i in range(2):
    t.circle(43,135)
    t.circle(58,45)
t.end_fill()
t.pensize(1)

#左眼球
t.up()
t.goto(-30,70)
t.down()
t.fillcolor("black")
t.begin_fill()
t.circle(12)
t.end_fill()

#左眼球
t.up()
t.goto(70,74)
t.down()
t.fillcolor("black")
t.begin_fill()
t.circle(12)
t.end_fill()


#坤嘴
t.pensize(10)
t.fillcolor("orange")
t.begin_fill()
t.seth(-95)
t.up()
t.goto(-45,20)
t.down()
for i in range(2):
    t.circle(25,36)
    t.circle(30,36)
    t.circle(50,36)
    t.circle(30,36)
    t.circle(25,36)
t.end_fill()
t.up()
t.goto(-45,13)
t.down()
t.seth(-25)
t.circle(60,20)
t.circle(80,20)
t.circle(60,20)
t.pensize(1)

#左晒红
t.fillcolor("tomato")
t.up()
t.goto(-137,-17)
t.down()
t.seth(0)
t.begin_fill()
t.circle(33)
t.end_fill()


#右晒红
t.fillcolor("tomato")
t.up()
t.goto(115,-20)
t.down()
t.seth(-10)
t.begin_fill()
t.circle(33,-190)
t.goto(115,-20)
t.end_fill()
'''
#脸部阴影
t.fillcolor("silver")
t.seth(0)
t.up()
t.goto(-180,47)
t.down()
t.begin_fill()
t.seth(5)
t.fd(7)
t.seth(-75)
t.fd(15)
t.seth(-5)
for i in range(6):
    t.fd(8)
    t.left(5)
t.left(20)
t.fd(10)
t.left(60)
t.fd(10)
t.seth(25)
for i in range(5):
    t.fd(5)
    t.right(3)
t.seth(-35)
for i in range(5):
    t.fd(5)
    t.left(5)
t.seth(90)
for i in range(5):
    t.fd(17)
    t.right(7)
t.seth(3)
t.fd(40)
t.seth(-45)
for i in range(2):
    t.fd(25)
    t.right(3)
t.seth(-80)
t.fd(20)
t.seth(0)
t.fd(45)
t.seth(-90)
t.fd(20)
t.seth(-10)
t.fd(55)
t.seth(120)
t.fd(150)
t.seth(190)
t.fd(220)
t.goto(-180,47)
t.end_fill()
'''

#围脖
t.seth(210)
t.up()
t.goto(95,-29)
t.down()
t.fillcolor("#292421")
t.begin_fill()
for i in range(5):
    t.fd(18)
    t.right(6)
t.seth(-90)
t.fd(10)
t.seth(15)
t.fd(110)
t.goto(95,-29)
t.end_fill()

#缝缝补补

l.fillcolor("black")
l.begin_fill()
l.up()
l.goto(-175,-25)
l.down()
l.seth(-45)
l.fd(30)
l.seth(190)
l.fd(30)
l.goto(-175,-25)
l.end_fill()

turtle.up()
turtle.goto(-150,200)
turtle.fd(90)
turtle.down()


#左头发
turtle.fillcolor("darkgrey")
turtle.begin_fill()

turtle.seth(165)
turtle.fd(25)
turtle.fd(-1)
turtle.seth(200)
turtle.fd(40)

for i in range(4):
    turtle.left(i*3+4)
    turtle.fd(35)
    
turtle.seth(-45)
for i in range(5):
    turtle.fd(6)
    turtle.left(10)

turtle.seth(80)
turtle.fd(20)
turtle.right(45)
turtle.fd(5)
turtle.fd(-5)
turtle.seth(-100)
for i in range(5):
    turtle.fd(12)
    turtle.left(6)

turtle.seth(15)
turtle.fd(35)

turtle.seth(90)
for i in range(3):
    turtle.fd(25)
    turtle.right(9)
turtle.seth(72)
for i in range(3):
    turtle.fd(-25)
    turtle.right(-9)
turtle.seth(-90)
for i in range(3):
    turtle.fd(7)
    turtle.left(9)

turtle.seth(-5)
for i in range(5):
    turtle.left(5)
    turtle.fd(6)

turtle.seth(100)
for i in range(10):
    turtle.right(3)
    turtle.fd(3)
turtle.seth(70)
for i in range(5):
    turtle.right(-3)
    turtle.fd(-3)
turtle.seth(10)

for i in range(7):
    turtle.fd(5)
    turtle.left(5)

turtle.seth(140)
turtle.fd(8)
turtle.fd(-25)

turtle.seth(85)
for i in range(5):
    turtle.fd(23)
    turtle.right(5*i+2)
#右头发
turtle.up()
turtle.goto(-52,196)
turtle.down()
turtle.seth(53)
turtle.fd(12)
turtle.right(10)
for i in range(6):
    turtle.right(8)
    turtle.fd(8)

turtle.seth(-25)
for i in range(5):
    turtle.fd(40)
    turtle.right(6*i+3)

turtle.seth(-115)
turtle.fd(23)
for i in  range(5):
    turtle.right(17)
    turtle.fd(1)
turtle.fd(20)
turtle.seth(115)
for i in range(5):
    turtle.fd(15)
    turtle.left(4)
turtle.fd(20)
turtle.seth(136)
for i in range(5):
    turtle.fd(-15)
    turtle.left(-4)
    
turtle.seth(175)
turtle.fd(50)

turtle.seth(115)
for i in range(5):
    turtle.fd(21)
    turtle.left(3*i+5)

turtle.seth(-135)
turtle.fd(20)

turtle.up()
turtle.seth(200)
turtle.fd(37)
turtle.down()

turtle.seth(15)
for i in range(5):
    turtle.fd(16)
    turtle.right(6)
turtle.end_fill()

turtle.up()

turtle.seth(-13)
for i in range(5):
    turtle.fd(-10)
    turtle.right(-5)
turtle.seth(0)
turtle.fd(2)
turtle.seth(90)
turtle.fd(5)

turtle.fillcolor("darkgrey")
turtle.begin_fill()
turtle.fd(3)
turtle.seth(45)
turtle.fd(30)
turtle.seth(155)
turtle.fd(36)
turtle.seth(-135)
turtle.fd(10)
turtle.seth(-90)
turtle.fd(10)
turtle.seth(-15)
turtle.fd(7)
turtle.right(45)
turtle.fd(4)
turtle.right(70)
turtle.fd(33)
turtle.seth(20)
turtle.fd(10)
turtle.end_fill()

#头发阴影(灰白)
n.up()
n.goto(-50,185)
n.down()
n.seth(175)
n.color("whitesmoke")
n.pensize(6)
for i in range(3):
    n.fd(1)
    n.left(5)
n.up()
n.seth(180)
n.fd(10)
n.down()
n.seth(160)
for i in range(5):
    n.fd(4)
    n.left(5)
n.up()
n.goto(-65,175)
n.down()
n.seth(190)
n.fd(10)
n.up()
n.goto(-40,185)
n.down()
n.seth(45)
for i in range(4):
    n.fd(5)
    n.right(3)
n.up()
n.goto(-35,170)
n.down()
n.seth(80)
for i in range(5):
    n.fd(3)
    n.right(10)
n.seth(0)
n.up()
n.goto(-10,200)
n.down()
for i in range(5):
    n.fd(6)
    n.right(5)

n.up()
n.goto(55,170)
n.down()
n.seth(-35)
for i in range(5):
    n.fd(20)
    n.right(6)
n.up()
n.goto(15,180)
n.down()
n.seth(-25)
for i in range(5):
    n.fd(3)
    n.right(5)
n.up()
n.fd(13)
n.down()
n.seth(-37)
for i in range(5):
    n.fd(3)
    n.right(5)
n.up()
n.goto(50,130)
n.down()
n.seth(-50)
for i in range(5):
    n.fd(6)
    n.right(5)

n.up()
n.goto(-95,150)
n.down()
n.seth(-120)
n.fd(15)
n.up()
n.fd(20)
n.down()
n.seth(-120)
for i in range(5):
    n.fd(7)
    n.left(5)
n.up()
n.goto(-110,160)
n.down()
n.seth(-135)
for i in range(5):
    n.fd(20)
    n.left(10)
n.up()
n.goto(-135,170)
n.down()
n.seth(200)
for i in range(5):
    n.fd(15)
    n.left(9)
n.up()
n.goto(-170,130)
n.down()
n.seth(-125)
for i in range(5):
    n.fd(10)
    n.left(7)
n.seth(180)
n.up()
n.goto(-100,185)
n.down()
for i in range(5):
    n.fd(3)
    n.left(10)




#左轮廓
turtle.up()
turtle.goto(-180,62)
turtle.down()
turtle.seth(-95)
for i in range(5):
    turtle.fd(22)
    turtle.left(i*5+5)
turtle.right(26)
turtle.fd(-22)
turtle.seth(-135)
turtle.fd(10)
turtle.left(6)
turtle.fd(5)
turtle.left(6)
turtle.fd(5)
turtle.seth(-90)
turtle.fd(20)
turtle.left(25)
turtle.fd(10)
turtle.right(90)
turtle.seth(0)

for i in range(4):
    turtle.fd(30)
    turtle.right(30)
turtle.seth(-90)
for i in range(4):
    turtle.fd(-30)
    turtle.right(-30)
turtle.fd(5)
turtle.seth(-110)
turtle.fd(10)

turtle.left(15)
turtle.fd(5)
turtle.left(15)
turtle.fd(5)
turtle.seth(0)
turtle.fd(7)

turtle.fillcolor("black")
turtle.begin_fill()
for i in range(4):
    turtle.fd(21)
    turtle.right(35)
turtle.seth(180)
turtle.fd(45)

turtle.seth(85)
for i in range(2):
    turtle.fd(25)
    turtle.right(10)

turtle.end_fill()

#右轮廓
turtle.fillcolor("black")
turtle.begin_fill()
turtle.seth(25)
turtle.up()
turtle.goto(-178,-50)
turtle.down()
for i in range(5):
    turtle.fd(22)
    turtle.right(9)
turtle.fd(50)
turtle.left(10)
turtle.fd(40)
turtle.left(8)
turtle.fd(30)
turtle.left(19)
turtle.fd(40)
turtle.left(6)
turtle.fd(40)
turtle.seth(155)
turtle.fd(20)

turtle.fd(-20)
turtle.seth(-110)
for i in range(3):
    turtle.fd(12)
    turtle.right(i*30)
turtle.seth(-70)
turtle.fd(8)
turtle.seth(-90)
turtle.fd(8)
turtle.seth(190)
turtle.fd(10)
turtle.seth(-50)
turtle.fd(30)
turtle.seth(-65)
turtle.fd(20)
turtle.seth(-75)
turtle.fd(15)
turtle.seth(180)
turtle.fd(233)

turtle.seth(-90)
for i in range(4):
    turtle.fd(-30)
    turtle.right(-30)
turtle.seth(90)
turtle.fd(10)
turtle.end_fill()

turtle.seth(-75)
turtle.up()
turtle.goto(123,65)
turtle.down()
for i in range(4):
    turtle.fd(29)
    turtle.right(i*5+20)


#阴影
l.fillcolor("#292421")
l.begin_fill()
l.up()
l.goto(-175,-55)
l.down()
l.seth(-45)
l.fd(15)
l.seth(-15)
for i in range(5):
    l.fd(10)
    l.left(3)
l.seth(25)
for i in range(5):
    l.fd(3)
    l.right(5)
l.seth(8)
for i in range(6):
    l.fd(28)
    l.right(4)
l.seth(24)
for i in range(9):
    l.fd(6)
    l.left(2)
l.seth(197)
for i in range(6):
    l.fd(23)
    l.right(5)
l.seth(155)
for i in range(6):
    l.fd(15)
    l.left(4)
l.seth(180)
for i in range(5):
    l.fd(10)
    l.left(5)
l.seth(180)
l.goto(-175,-55)

l.end_fill()

#吊带
l.fillcolor("#292421")
l.begin_fill()
l.seth(-5)
l.up()
l.goto(-111,-94)
l.down()
for i in range(5):
    l.fd(35)
    l.left(2)
l.seth(-100)
for i in range(3):
    l.fd(10)
    l.left(5)
l.seth(-70)
l.fd(16)
l.seth(180)
l.fd(171)
l.seth(90)
for i in range(5):
    l.fd(10)
    l.left(4)
l.end_fill()

l.seth(-9)
l.up()
l.goto(-108,-100)
l.down()
l.fillcolor("white")
l.begin_fill()

l.fd(80)
l.seth(0)
l.fd(2)
l.seth(9)
l.fd(90)
l.right(45)
l.fd(1)
l.seth(-110)
l.fd(5)
l.seth(190)
l.fd(80)
l.seth(-90)
l.fd(5)
l.seth(0)
for i in range(5):
    l.fd(2)
    l.right(5)
l.seth(-45)
for i in  range(10):
    l.fd(2)
    l.right(5)
l.seth(180)
l.fd(36)
l.seth(90)
for i in range(4):
    l.fd(4)
    l.right(1)
l.seth(20)
for i in range(5):
    l.fd(2)
    l.right(3)
l.seth(90)
l.fd(5)
l.seth(171)
l.fd(82)
l.goto(-108,-100)
l.end_fill()

l.up()
l.goto(-35,-140)
l.down()
l.hideturtle()
l.color("darkgrey")
l.write("IKUN",font=('宋体',9,'italic','bold'))

#左背带
m.fillcolor("white")
m.begin_fill()
m.up()
m.goto(-175,-70)
m.down()
for i in range(7):
    m.fd(17)
    m.right(16)
m.seth(180)
m.fd(25)
m.seth(70)
for i in range(6):
    m.fd(15)
    m.left(22)
m.seth(180)
m.fd(10)
m.goto(-175,-70)
m.end_fill()

#右背带

turtle.fillcolor("white")
turtle.begin_fill()
turtle.up()
turtle.goto(105,-70)
turtle.down()
turtle.pensize(3)
turtle.seth(200)
turtle.up()
for i in range(4):
    turtle.fd(25)
    turtle.left(35)
turtle.seth(0)
turtle.fd(10)
turtle.seth(300)
for i in range(3):
    turtle.fd(-26)
    turtle.left(-40)
turtle.seth(80)
turtle.fd(10)
turtle.down()
turtle.end_fill()


#边框
b.up()
b.goto(-260,270)
b.down()
b.seth(-90)
b.fd(425)
b.seth(0)
b.fd(425)
b.seth(90)
b.fd(425)
b.seth(180)
b.fd(425)
b.up()
b.goto(-260,270)
b.down()
b.seth(0)
b.pensize(4)
b.color("white")
for i in range(4):
    b.fd(425)
    b.right(90)
b.up()
b.goto(-250,260)
b.down()
for i in range(4):
    b.fd(405)
    b.right(90)

#文字
w.color("white")
w.up()
w.goto(-257,-250)
w.down()
w.write("《世界名画》",font=('黑体',50,'bold','italic'))
w.pensize(5)
w.up()
w.fd(50)
w.down()
w.fd(310)

#文案
w.up()
w.goto(200,230)
w.seth(0)
w.pensize(1)
w.down()
w.write("唱,跳,rap篮球",font=('宋体',15,'bold'))
w.up()
w.goto(200,210)
w.seth(0)
w.pensize(1)
w.down()
w.write("练习时长两年半",font=('宋体',15,'bold'))
w.up()
w.goto(200,190)
w.seth(0)
w.pensize(1)
w.down()
w.write("小黑子露出鸡脚了吧",font=('宋体',15,'bold'))
w.up()
w.goto(200,170)
w.seth(0)
w.pensize(1)
w.down()
w.write("荔枝？你要我那我拿什么荔枝",font=('宋体',15,'bold'))
w.up()
w.goto(200,150)
w.seth(0)
w.pensize(1)
w.down()
w.write("你食不食油饼",font=('宋体',15,'bold'))
w.up()
w.goto(200,130)
w.seth(0)
w.pensize(1)
w.down()
w.write("鸡哥拒绝了你的打球邀请，并向你扔了一封律师函",font=('宋体',15,'bold'))
w.up()
w.goto(200,110)
w.seth(0)
w.pensize(1)
w.down()
w.write("再黑紫纱了",font=('宋体',15,'bold'))
w.up()
w.goto(200,90)
w.seth(0)
w.pensize(1)
w.down()
w.write("一个真正的man",font=('宋体',15,'bold'))
w.up()
w.goto(200,70)
w.seth(0)
w.pensize(1)
w.down()
w.write("鸡你太美",font=('宋体',15,'bold'))
w.up()
w.goto(200,50)
w.seth(0)
w.pensize(1)
w.down()
w.write("鸡你实在是太美",font=('宋体',15,'bold'))


#打开动画
turtle.update()
input("退出程序")