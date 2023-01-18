import sys
def hanoi(n, x, y, z):
  if n != 0:
    hanoi(n-1, x, z, y)
    sys.stdout.write("{}->{}, ".format(x, y))
    hanoi(n-1, z, y, x)

hanoi(8, 'A', 'B', 'C')
