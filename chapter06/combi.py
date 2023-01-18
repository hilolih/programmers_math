def c(n,k):
  if n == k or k == 0 :
    return 1
  elif k > 0 and n > k:
    return c(n-1, k-1) + c(n-1, k)
  else:
    return 0
  
print(c(5,3))
    