# Classy:
class factorial:
  def __call__(self, n):
        input = 1
        for i in range(1,n+1):
          input = input * i
        return input

def display():
  a = int(input("Factorial of:"))
  printfactorial = factorial()
  print(printfactorial(a))


# Classless:
# def facty(n):
#   if n <= 1:
#     return 1
#   else: 
#     return (n * facty(n-1))
  
# def display():
#   terms = int(input("How many numbers do you want?"))
#   try:
#     print("Your Factorial Sequence:")
#     for i in range(terms):
#       print(facty(i))
#   except:
#     terms < 0
#     print("A Positive Number")
    