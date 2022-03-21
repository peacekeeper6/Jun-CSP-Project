{% include navigation.html %}
<a href="https://github.com/peacekeeper6/Jun-CSP-Project">Link to GitHub Repository for code</a>

<iframe height="800px" width="100%" src="https://replit.com/@TWIYJun/Jun-CSP-Project?lite=true"></iframe>



This is what prints the data in the InfoDB loop

``
def print_data(n):
    print(InfoDb[n]["Book_Title"], "by", InfoDb[n]["Author"])  # using comma puts space between values
    print("\t", "Genre: ", end="")  # \t is a tab indent, end="" make sure no return occurs
    print(", ".join(InfoDb[n]["Genre"]))  # join allows printing a string list with separator
    print("\t", "Another book by the Author: ", end="")
    print(InfoDb[n].get("Author_Books")[0])
    print()

def for_loop():
    for n in range(len(InfoDb)):
        print_data(n)
      
def while_loop(n):
    while n < len(InfoDb):
        print_data(n)
        n += 1
    return
  
def recursive_loop(n):
    if n < len(InfoDb):
        print_data(n)
        recursive_loop(n + 1)
    return # exit condition

def tester():
  print('*' * 10)
  print("For loop")
  print('*' * 10)
  for_loop()
  print('*' * 10)
  print("While loop")
  print('*' * 10)
  while_loop(0)
  print('*' * 10)
  print("Recursive loop")
  print('*' * 10)
  recursive_loop(0)

if __name__ == "__main__":
  tester()
``

This is the fibonacci code. It indexes at 1, then adds to a sequence.

``
def fibo(n):
  if n == 1:
    return 1
  else: 
    return (fibo(n-1) + fibo(n-2))
``
