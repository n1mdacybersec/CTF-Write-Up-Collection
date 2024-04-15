# binhexa

## Description
How well can you perfom basic binary operations? <br>
Additional details will be available after launching your challenge instance.

**NOTE: This is an instance challenge, start the instance to get more information**

## Points
100

## Solution
After connecting to the server, there will be binary operations for 2 binary numbers.
The binary operations consist of addition (+), substraction (-), multiplication (*), bitwise right shift (>>), bitwise left shift (<<), AND (&), and OR (|).
The binary operations for each session will have different sequence for the binary operations.

To perform the binary operations easier, we can use python to help us for this task.
First let define our 2 binary numbers, namely `a` for binary number 1 and `b` for binary number 2 with this python code.
Then we can make a function for each binary operations. For the last question it will also print the hexadecimal value of the binary number.
For binary number please ignore the `0b` and for hexadecimal number please ignore the `0x`

```py
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
```

## Flag
` picoCTF{b1tw^3se_0p3eR@tI0n_su33essFuL_d6f8047e}`
