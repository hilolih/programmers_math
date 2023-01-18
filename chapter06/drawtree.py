import turtle

def drawtree(n,angles=15,distance=30):
  """
  再帰的な図形を書く(P169)
  args:
    n 再帰回数
    angles 枝の角度。degrees指定
    distance 枝の長さ
  """
  if n == 0:
    return
  else:
    t.left(angles)
    t.forward(distance)
    drawtree(n-1, angles, distance)
    t.back(distance)
    t.right(angles)

    t.right(angles)
    t.forward(distance)
    drawtree(n-1, angles, distance)
    t.back(distance)
    t.left(angles)

t = turtle.Turtle()
s = turtle.Screen()
# n回に一回しかアニメーションを更新しない -> 早くなる
s.tracer(8)
# 右向いているので、上を向く
t.left(90)
# 0-10でスピード調整。0はアニメーションがない。
t.speed(0)
#
drawtree(10)
turtle.done()

