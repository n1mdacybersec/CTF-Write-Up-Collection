def bin_operations(a, b, operations):
  if operations == '+':
    result = bin(a + b)
  elif operations == '-':
    result = bin(a - b)
  elif operations == '*':
    result = bin(a * b)
  elif operations == '>>':
    num = input("Choose number a or b: ")
    if num == 'a':
      result = bin(a >> 1)
    elif num == 'b':
      result = bin(b >> 1)
    else:
      print("Invalid number to choose")
  elif operations == '<<':
    num = input("Choose number a or b: ")
    if num == 'a':
      result = bin(a << 1)
    elif num == 'b':
      result = bin(b << 1)
    else:
      print("Invalid number to choose")
  elif operations == '&':
    result = bin(a & b)
  elif operations == '|':
    result = bin(a | b)
  else:
    print("Invalid operations")
  
  return(result)

if __name__ == "__main__":
  a = input("Input number a: ")
  b = input("Input number b: ")
  a = int(a, 2)
  b = int(b, 2)

  for i in range(6):
    operations = input("Choose the binary operations: ")

    result = bin_operations(a, b, operations)
    print("Binary result: ", result)
    if i == 5:
        print(f"Hexadecimal result: {hex(int(result, 2))}")