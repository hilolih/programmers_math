def fib_memo(n):
  memo = [0]*(n+1)
  def fibonacci(n):
    if n == 0:
      return 0
    elif n == 1:
      return 1
    # すでにメモ化していれば、その数を返す
    if memo[n] != 0:
      return memo[n]
    memo[n] = fibonacci(n-1) + fibonacci(n-2)
    return memo[n]
  return fibonacci(n)
    
    

print(fib_memo(20))