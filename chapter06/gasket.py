import turtle
from collections import deque
# 
# シェルピンスキーのギャスケット(P172)
# <参考> https://masutomo.hatenablog.com/entry/2020/01/17/004114
# 

#指定した場所に移動して方向を水平に変更
def setXY(x,y):
  t.setheading(0)
  t.penup()
  t.setposition(x,y)
  t.pendown()

#最初に一度だけ描く大きい三角形
def drawBigGreenTri(l=600):
  t.fillcolor('red')
  t.begin_fill()
  for _ in range(3):
    t.forward(l)
    t.right(240)
  t.end_fill()

#再帰で小さい三角形を描画
def drawTri(l=600, limit=2):
  l /= 2
  # 三角形の辺が一定のサイズ以下になったら終了
  if l < limit:
    return
  qq = list(Q)
  for q in qq:
    # 底辺真ん中に移動
    setXY((q[0]+l),q[1])
    triangle(l)
  drawTri(l)

def triangle(l):
  """
  逆三角形を描画する
  """
  Q.append(list(t.position()))
  t.begin_fill()
  t.right(300)
  for i in range(3):
    if i == 2: Q.append(list(t.position()))
    t.forward(l)
    t.right(240)
  t.end_fill()


# len = 600
stX = -250
stY = -250
t = turtle.Turtle()
s = turtle.Screen()
# n回に一回しかアニメーションを更新しない -> 早くなる
s.tracer(8)
t.speed(5)

t.setheading(0)
t.penup()
# スタートへ移動
t.setposition(stX,stY)
t.pendown()

# 一番外側の大きな三角形を描画
drawBigGreenTri()
Q = deque()
Q.append([stX,stY])

# 逆三角形
t.fillcolor('black')
drawTri()

turtle.done()