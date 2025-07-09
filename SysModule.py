#1
import sys
print("Script name:", sys.argv[0])
print("All args:", sys.argv[1:])
if len(sys.argv)>1:
  print("First arg : " ,sys.argv[1])
else:
  print("No argument Provided")


#2
import sys
num1 = int(sys.argv[1])
num2 = int(sys.argv[2])
num3 = int(sys.argv[3])
print("product:", num1*num2*num3)


#3
import sys
if len(sys.argv) != 3:
    print("Usage: python Sys.py length breadth")
else:
    try:
        l = float(sys.argv[1])
        b = float(sys.argv[2])
        print("Calculated area:", l * b)
    except ValueError:
        print("Please enter valid numbers.")


#4
import sys

if len(sys.argv) < 2:
    print("Usage: python Sys.py n1 n2 ...")
    sys.exit()

numbers = [int(arg) for arg in sys.argv[1:]]
total = sum(numbers)
print("Numbers:", numbers)
print("Sum:", total)
