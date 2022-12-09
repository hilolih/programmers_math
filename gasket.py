from turtle import *
from collections import deque
len = 600
stX = -250
stY = -250

#スタート地点に戻る
def setHome():
    setheading(0)
    penup()
    setposition(stX,stY)
    pendown()
#指定した場所に移動して方向を水平に変更
def setXY(x,y):
    setheading(0)
    penup()
    setposition(x,y)
    pendown()

#最初に一度だけ描く大きい三角形
def drawBigTri(l):
    setHome()
    fillcolor('green')
    begin_fill()
    for _ in range(3):
        fd(l)
        rt(240)
    end_fill()

#再帰で小さい三角形を描画
def drawTri(l):
    l /= 2
    if l < 5:
      return
    qq = []
    for q in Q:
        qq.append(q)
    for q in qq:
        setXY(q[0],q[1])
        fd(l)
        rt(300)
        Q.append(list(position()))
        fillcolor('white')
        begin_fill()
        for i in range(3):
            if i == 2: Q.append(list(position()))
            fd(l)
            rt(240)
        end_fill()
    drawTri(l)

# n回に一回しかアニメーションを更新しない -> 早くなる
s = Screen()
s.tracer(8)

speed(0)
drawBigTri(len)
Q = deque()
Q.append([stX,stY])
drawTri(len)
done()