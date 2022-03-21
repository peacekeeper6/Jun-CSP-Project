def fibo(n):
  if n == 1:
    return 1
  else: 
    return (fibo(n-1) + fibo(n-2))

def print_num():
  terms = int(input)("How many numbers do you want?")
  try:
    print("Your Fibonacci Sequence:")
    for i in range(terms):
      print(fibo(i))
  except:
    terms <= 0
    print("A Positive Number")