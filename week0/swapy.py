def swap(a, b):
    if b < a:
          a, b = b, a
    return a, b



if __name__ == "__main__":
  a = input("first number")
  b = input("second number")
  print(', '.join(swap(a, b)))
