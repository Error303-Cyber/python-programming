import turtle

tar = turtle.Turtle()
window = turtle.Screen()
window.bgcolor("#B0BF1A")
tar.shape("turtle")
tar.width(5)
tar.color("green")

def A():
    tar.speed(1)
    tar.penup()
    tar.left(180)
    tar.fd(35)
    tar.right(108.29)
    tar.pendown()
    tar.fd(105.95)
    tar.right(141.42)
    tar.fd(105.95)
    tar.bk(35)
    tar.right(108.29)
    tar.fd(46.88)
    tar.penup()
    tar.left(90)
    tar.fd(33.04)
    tar.left(90)
    tar.fd(68.44)
    tar.pendown()
#A()
def B():
    tar.speed(1)
    tar.penup()
    tar.left(180)
    tar.pendown()
    tar.fd(35)
    tar.right(90)
    tar.fd(100)
    tar.right(90)
    tar.fd(70)
    tar.right(90)
    tar.fd(50)
    tar.right(90)
    tar.fd(70)
    tar.bk(70)
    tar.left(90)
    tar.fd(50)
    tar.right(90)
    tar.fd(35)
    tar.penup()
    tar.bk(45)
    tar.pendown()
#B()
def C():
    tar.speed(1)
    tar.left(180)
    tar.fd(35)
    tar.right(90)
    tar.fd(100)
    tar.right(90)
    tar.fd(70)
    tar.right(90)
    tar.penup()
    tar.fd(100)
    tar.right(90)
    tar.pendown()
    tar.fd(35)
    tar.penup()
    tar.bk(45)
    tar.pendown()
#C()
'''def D():
    tar.speed(1)
    tar.left(180)
    tar.fd(35)
    tar.right(90)
    tar.fd(100)
    tar.right(90)
    tar.fd(70)
    tar.right(90)
    tar.fd(100)
    tar.right(90)
    tar.fd(35)
    tar.penup()
    tar.bk(45)
    tar.hideturtle()
    window.exitonclick()
D()
def E():
    tar.fd(35)
    tar.bk(70)
    tar.left(90)
    tar.fd(100)
    tar.right(90)
    tar.fd(70)
    tar.penup()
    tar.right(90)
    tar.fd(40)
    tar.right(90)
    tar.pendown()
    tar.fd(70)
    tar.penup()
    tar.left(90)
    tar.fd(60)
    tar.left(90)
    tar.fd(80)
    tar.hideturtle()
E()
def F():
    tar.left(180)
    tar.penup()
    tar.fd(35)
    tar.right(90)
    tar.pendown()
    tar.fd(100)
    tar.right(90)
    tar.fd(70)
    tar.penup()
    tar.bk(20)
    tar.right(90)
    tar.fd(40)
    tar.right(90)
    tar.pendown()
    tar.fd(50)
    tar.penup()
    tar.left(90)
    tar.fd(60)
    tar.left(90)
    tar.fd(80)
    tar.hideturtle()
F()
def G():
    tar.speed(1)
    tar.penup()
    tar.fd(35)
    tar.left(90)
    tar.fd(100)
    tar.left(90)
    tar.pendown()
    tar.fd(70)
    tar.left(90)
    tar.fd(100)
    tar.left(90)
    tar.fd(70)
    tar.left(90)
    tar.fd(40)
    tar.left(90)
    tar.fd(35)
    tar.penup()
    tar.left(90)
    tar.fd(40)
    tar.left(90)
    tar.fd(45)
    tar.hideturtle()
G()
def H():
    tar.speed(1)
    tar.penup()
    tar.fd(35)
    tar.pendown()
    tar.left(90)
    tar.fd(100)
    tar.bk(50)
    tar.left(90)
    tar.fd(70)
    tar.right(90)
    tar.fd(50)
    tar.bk(100)
    tar.penup()
    tar.right(90)
    tar.fd(80)
    tar.hideturtle()
H()
def I():
    tar.speed(1)
    tar.left(90)
    tar.fd(100)
    tar.right(90)
    tar.fd(5)
    tar.bk(10)
    tar.fd(5)
    tar.right(90)
    tar.fd(100)
    tar.right(90)
    tar.fd(5)
    tar.bk(10)
    tar.penup()
    tar.bk(10)
    tar.hideturtle()
    window.exitonclick()
I()
def J():
    tar.speed(1)
    tar.penup()
    tar.left(180)
    tar.fd(35)
    tar.right(90)
    tar.fd(100)
    tar.right(90)
    tar.pendown()
    tar.fd(70)
    tar.right(90)
    tar.fd(100)
    tar.right(90)
    tar.fd(60)
    tar.right(90)
    tar.fd(35)
    tar.penup()
    tar.bk(35)
    tar.right(90)
    tar.fd(70)
    tar.hideturtle()
J()
def K():
    tar.speed(1)
    tar.penup()
    tar.left(180)
    tar.fd(35)
    tar.right(90)
    tar.pendown()
    tar.fd(100)
    tar.bk(50)
    tar.right(45)
    tar.fd(70)
    tar.bk(70)
    tar.right(90)
    tar.fd(70)
    tar.penup()
    tar.left(45)
    tar.fd(10)
    tar.hideturtle()
K()
def L():
    tar.speed(1)
    tar.penup()
    tar.left(180)
    tar.fd(35)
    tar.right(90)
    tar.fd(100)
    tar.pendown()
    tar.bk(100)
    tar.right(90)
    tar.fd(70)
    tar.penup()
    tar.fd(10)
    tar.hideturtle()
L()
def M():
    tar.left(90)
    tar.fd(100)
    tar.right(150)
    tar.fd(45)
    tar.left(120)
    tar.fd(45)
    tar.right(150)
    tar.fd(100)
    tar.hideturtle()
    tar.penup()
    tar.left(90)
    tar.fd(10)
    tar.pendown()
M()
def N():
    tar.left(90)
    tar.fd(100)
    tar.right(145)
    tar.fd(122)
    tar.left(145)
    tar.fd(100)
    tar.penup()
    tar.hideturtle()
    tar.backward(100)
    tar.right(90)
    tar.fd(10)
    tar.pendown()
N()
def O():
    for i in range(36):
        tar.fd(9)
        tar.left(10)
    tar.penup()
    tar.fd(55)
    tar.pendown()
O()
def P():
    tar.left(90)
    tar.fd(100)
    tar.right(90)
    tar.fd(70)
    tar.right(90)
    tar.fd(55)
    tar.right(90)
    tar.fd(70)

    tar.penup()
    tar.left(90)
    tar.forward(50)
    tar.left(90)
    tar.fd(80)
    tar.pendown()
P()
def Q():
    tar.left(90)
    tar.fd(100)
    tar.right(90)
    tar.fd(70)
    tar.right(90)
    tar.fd(100)
    tar.right(90)
    tar.fd(70)
    tar.bk(70)
    tar.left(130)
    tar.fd(10)
    tar.bk(20)
    tar.penup()
    tar.fd(10)
    tar.left(50)
    tar.fd(10)
    tar.pendown()
Q()
def R():
    tar.left(90)
    tar.fd(100)
    tar.right(90)
    tar.fd(70)
    tar.right(90)
    tar.fd(50)
    tar.right(90)
    tar.fd(70)
    tar.bk(20)
    tar.left(135)
    tar.fd(70)
    tar.hideturtle()
    tar.penup()
    tar.left(45)
    tar.fd(10)
    tar.pendown()
R()
def S():
    tar.left(90)
    tar.penup()
    tar.fd(100)
    tar.right(90)
    tar.pendown()
    tar.fd(70)
    tar.back(70)
    tar.right(90)
    tar.fd(50)
    tar.left(90)
    tar.fd(70)
    tar.right(90)
    tar.fd(50)
    tar.right(90)
    tar.fd(70)
    tar.right(180)
    tar.hideturtle()
    tar.penup()
    tar.fd(80)
    tar.pendown()
S()
def T():
    tar.left(90)
    tar.fd(100)
    tar.right(90)
    tar.fd(35)
    tar.bk(70)
    tar.hideturtle()
    tar.penup()
    tar.right(90)
    tar.fd(100)
    tar.left(90)
    tar.fd(80)
    tar.pendown()
T()
def U():
    tar.left(90)
    tar.penup()
    tar.fd(122)
    tar.right(180)
    tar.pendown()
    tar.fd(78)

    for i in range(22):
        tar.fd(6)
        tar.left(8)

    tar.left(6)
    tar.fd(88)
    tar.penup()
    tar.right(180)
    tar.hideturtle()
    tar.fd(122)
    tar.left(88)
    tar.fd(10)
    tar.pendown()
U()
def V():
    tar.left(112)
    tar.fd(100)
    tar.bk(100)
    tar.right(45)
    tar.fd(102)
    tar.right(158)
    tar.penup()
    tar.fd(94)
    tar.left(90)
    tar.fd(10)
    tar.pendown()
V()
def W():
    tar.left(95)
    tar.fd(100)
    tar.bk(100)
    tar.right(15)
    tar.fd(102)

    tar.right(160)
    tar.fd(100)
    tar.left(165)
    tar.forward(100)
    tar.hideturtle()
    tar.penup()
    tar.right(175)
    tar.fd(100)
    tar.left(90)
    tar.fd(10)
W()
def X():
    tar.left(90)
    tar.penup()
    tar.fd(70)
    tar.pendown()
    tar.right(135)
    tar.forward(100)
    tar.left(135)
    tar.penup()
    tar.forward(70)
    tar.pendown()
    tar.left(135)
    tar.forward(100)
    tar.hideturtle()
    tar.penup()
    tar.left(135)
    tar.fd(80)
    tar.pendown()
X()
def Y():
    tar.left(90)
    tar.penup()
    tar.fd(50)
    tar.pendown()
    tar.left(35)
    tar.fd(50)
    tar.bk(50)
    tar.right(70)
    tar.fd(52)
    tar.back(52)
    tar.right(145)
    tar.forward(50)
    tar.hideturtle()
    tar.penup()
    tar.left(90)
    tar.fd(45)
    tar.pendown()
Y()
def Z():
    tar.left(90)
    tar.penup()
    tar.fd(100)
    tar.right(90)
    tar.pendown()
    tar.fd(70)
    tar.right(135)
    tar.forward(135)
    tar.left(135)
    tar.forward(70)
    tar.hideturtle()
    tar.penup()
    tar.fd(20)
    tar.pendown()
Z()
'''
a = "Aa"; b = "Bb"; c = "Cc"

i = str(input("your name: "))
for p in i:
    if p in a:
        print(A())
    elif p in b:
        print(B())
    else:
        print("Sorry")
window.exitonclick()


tar.getscreen()._root.mainloop()